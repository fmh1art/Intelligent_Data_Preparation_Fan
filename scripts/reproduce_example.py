"""Deterministic counterexample; no paper method or performance experiment."""
import json
import sqlite3


def evaluate(refunds):
    db = sqlite3.connect(':memory:')
    db.executescript('''
      CREATE TABLE orders (oid TEXT PRIMARY KEY, customer TEXT, amount INTEGER);
      CREATE TABLE refunds (oid TEXT, refund INTEGER);
      INSERT INTO orders VALUES ('o1','A',100), ('o2','A',80);
    ''')
    db.executemany('INSERT INTO refunds VALUES (?,?)', refunds)
    direct = db.execute('''SELECT o.oid, o.amount, coalesce(r.refund,0)
       FROM orders o LEFT JOIN refunds r USING(oid) ORDER BY o.oid,r.refund DESC''').fetchall()
    good = db.execute('''WITH grouped AS
       (SELECT oid,sum(refund) refund FROM refunds GROUP BY oid)
       SELECT o.oid,o.amount,coalesce(g.refund,0)
       FROM orders o LEFT JOIN grouped g USING(oid) ORDER BY o.oid''').fetchall()
    wrong_total = sum(amount - refund for _, amount, refund in direct)
    correct_total = sum(amount - refund for _, amount, refund in good)
    independent = db.execute('''SELECT
       (SELECT sum(amount) FROM orders)-(SELECT sum(refund) FROM refunds)''').fetchone()[0]
    assert len({row[0] for row in direct}) < len(direct)
    assert len({row[0] for row in good}) == len(good)
    assert correct_total == independent
    assert wrong_total != independent
    db.close()
    return dict(direct_join=direct, aggregated_join=good,
                wrong=wrong_total, correct=correct_total, invariant=independent)


if __name__ == '__main__':
    original = evaluate([('o1',20),('o1',10)])
    perturbation = evaluate([('o1',20),('o1',15)])
    assert (original['wrong'], original['correct']) == (250,150)
    assert (perturbation['wrong'], perturbation['correct']) == (245,145)
    assert len(original['direct_join']) == len(perturbation['direct_join'])
    print(json.dumps({'original':original,'refund_value_perturbation':perturbation},indent=2))
