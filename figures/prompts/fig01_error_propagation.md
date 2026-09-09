# 图1：多表错误传播实例（沿用原图3第二版）

本轮以正文第4.5节及共同视觉规格为依据完整重绘，不使用旧图作为风格参考。以下为实际提交给内置 imagegen 的完整 prompt。

Use case: scientific-educational.
Create a wholly redesigned, publication-quality Chinese database research figure, with a new side-by-side comparison composition. Native canvas requested: 3072 × 2048 pixels, landscape 3:2, or the highest native resolution supported. Do not simulate resolution with resizing. All text must remain clearly readable when viewed at 1536 pixels wide.

VISUAL DESIGN
Pure white background. Precise fine strokes, subtle table grid lines, dark ink-blue typography, restrained blue #2865A8, teal #138B84, violet #7764A5 for stored state, brick red #CA5949 only for incorrect results and rollback. Extremely pale fills only behind selected cells or subtle comparison areas. No saturated header bars, thick rounded boxes, gradients, shadows, glossy surfaces, 3D objects, people, large generic office icons, decorative particles, logos or marketing badges. Use excellent typesetting, large consistent Chinese sans-serif labels, tabular numerals, generous cell padding, and at least 3% outer whitespace. Rich visual detail comes from genuine table structure, keyed fields, aligned highlighted cells, join/group glyphs, and a restrained small magnifier/history icon, not extra prose. Intermediate tables should be the visual focus. Keep labels short. No figure number or large external heading.

COMPOSITION
A small task heading at top reads “按客户汇总净收入”, with subordinate phrase “订单金额仅计一次”.
Under it place a slim shared source-state band: two real tables side by side, titled “订单 O” and “退款 R”. A small state label reads “源表状态 S₀”. This is the shared input for both paths.
Below the source band, compare two vertically descending paths in two spacious aligned columns: left caption “直接连接后汇总”, right caption “先聚合退款再连接”. Use thin colored underlines, not banner blocks. Keep both intermediate tables at approximately the same height so the viewer can compare three rows against two rows. The left column is a cautionary brick-red path; the right column is a teal corrected path. The flow is top-to-bottom. Draw only necessary arrows and clear arrowheads.
At the bottom, place a clean horizontal independent-check area with a small magnifier glyph, distinct from both executable paths. Reserve outer-left whitespace for one rollback curve and the central gutter for the intermediate-check connector, so no arrows intersect.

EXACT DATA
Source “订单 O” has three columns:
订单 | 客户 | 金额
o1 | A | 100
o2 | A | 80
Source “退款 R” has two columns:
订单 | 退款
o1 | 20
o1 | 10
Do not add or remove any source rows or alter any values.

LEFT PATH
Show concise operation “按订单左连接”, accompanied by a small relational join glyph rather than a large icon card.
Its intermediate table has FOUR columns and exactly THREE rows:
订单 | 客户 | 金额 | 退款
o1 | A | 100 | 20
o1 | A | 100 | 10
o2 | A | 80 | 0
Highlight ONLY the two 100 cells with soft brick-red fill and a slim brace caption “重复计入”. This denotes duplicated contribution to the later sum; do not imply a SQL syntax failure or illegal one-to-many join.
Below the table show “逐行相减 · 按客户汇总”, then a restrained result table or result line “客户 A：250” with the small explicit label “错误结果”.
Retain this exact arithmetic in one readable line: “(100−20)+(100−10)+80=250”.
All operators are executable; the error is the task's order amount being counted twice.

RIGHT PATH
Start with a concise grouping step “退款按订单聚合” with a small grouping glyph.
Display the aggregated refund table:
订单 | 退款
o1 | 30
Then show “与订单左连接”. Keep a small source-reference chip “O” and a short bypass arrow entering this join to make clear the original order table is also used. The order source must NOT pass through refund aggregation. A source-reference chip “R” may mark the aggregation input. These chips reference the top source tables, not extra data.
The corrected intermediate table has FOUR columns and exactly TWO rows:
订单 | 客户 | 金额 | 退款
o1 | A | 100 | 30
o2 | A | 80 | 0
Below the table show “逐行相减 · 按客户汇总”, then a restrained result table or result line “客户 A：150” with small label “修订结果”.
Retain this exact arithmetic: “(100−30)+(80−0)=150”.
Soft teal highlights may emphasize the single refund value 30 and the single o1 row without making a high-saturation box.

INDEPENDENT CHECK AND ROLLBACK
The bottom area's title is “独立检查 · 预设口径”.
It contains exactly these two concise checks, typeset as two side-by-side items:
“每单净收入计算前：订单键唯一”
“净收入总额：180−30=150”
A small boundary note reads “检查范围：粒度与总额”. Do not claim these conditions prove complete correctness.
A thin dark-blue connector must leave the LEFT intermediate table into the clear central gutter and descend into this independent-check area. Route it without crossing the right path or either arithmetic line. A short connector from the right result into the check area is optional if it remains unambiguous and uncluttered.
One restrained brick-red rollback curve leaves the check area, routes around the outside LEFT edge, and ends with an arrowhead at the top “源表状态 S₀” band. Label it “回退 · 插入退款聚合”. Never point rollback at the wrong intermediate table or at a path caption. Do not draw crossing arrows or redundant execution loops.
The task checks are predefined business requirements, not an LLM self-score. A one-to-many left join is valid; only counting the order amount more than once violates this task.

BOTTOM ASSUMPTION LINE
In clear but secondary type, one line only:
“全部订单保留 · 同币种 · 无退款记0 · 退款事件有效且可加”
No additional paragraphs, no new numbers, no extra rows, no invented performance measures. The illustration is an author-constructed example and does not represent an empirical benchmark.
