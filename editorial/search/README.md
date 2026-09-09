# 可核查的补充检索与范围取样

日期：2026-09-09。本次大修重新建立补充检索记录；不反推既有34项参考文献的历史筛选数量。不是PRISMA系统综述，不宣称穷尽召回，也未实施独立双人复筛。

## 数据源及执行参数

结构化来源为Crossref REST API。ACM、IEEE、PVLDB、ACL Anthology、arXiv、中文期刊官网和作者机构页面用于原文/版本核查，不作为声称完整检索过的独立数据库。未调用CNKI、Scopus、Web of Science。

所有查询均为GET /works，设置rows=15、filter=from-pub-date:2009-01-01,until-pub-date:2026-09-09；仅取相关度排序前15条。select字段为DOI,title,author,published,container-title,abstract,type,URL。准确端点、参数、发布日期字段及原始返回保存为Q1.json至Q16.json。

| 查询 | 字段 | 检索词 | 用途 |
|---|---|---|---|
| Q1 | query | data discovery table union search | 试探 |
| Q2 | query | table semantic type detection representation learning | 试探 |
| Q3 | query | data cleaning error detection repair | 试探 |
| Q4 | query | entity matching schema matching benchmark | 试探 |
| Q5 | query | data transformation pipeline synthesis | 试探 |
| Q6 | query | weak supervision data labeling coreset | 试探 |
| Q7 | query | data preprocessing pipeline search | 试探 |
| Q8 | query | data preparation language models benchmark | 试探 |
| Q9 | query.title | table union search | 固定筛选 |
| Q10 | query.title | semantic type detection | 固定筛选 |
| Q11 | query.title | data cleaning | 固定筛选 |
| Q12 | query.title | entity matching | 固定筛选 |
| Q13 | query.title | table transformation | 固定筛选 |
| Q14 | query.title | weak supervision | 固定筛选 |
| Q15 | query.title | data preprocessing pipeline | 固定筛选 |
| Q16 | query.title | data preparation | 固定筛选 |

第一轮宽泛字段出现大量同名异义及领域应用，因此改用题名字段检查相关研究。题名字段仍是相关度检索，不是布尔AND或引号精确检索；查询没有作者、机构或引用量过滤。Q1—Q8共120条仅作为查询设计记录，不计入固定筛选分母。Q9—Q16共120条进入逐项台账。

## 规则和实际流程

1. 合并重复DOI与明确版本。Morpheus的PLDI/SIGPLAN Notices两DOI合并；Multilingual Entity Matching的会议/SSRN记录合并；同一补充材料的版本合并。不会仅因“Data Cleaning”等通用题名相同就合并不同作者的文献。
2. 初筛按题名、可用摘要和文献类型排除同名异义、一般领域应用、目录/百科/一般说明资料。实际117项独立工作中83项排除，34项进入复筛。
3. 复筛采用**目的性范围取样**：保留能够增加机制、目标监督、状态搜索或评测维度的研究。新增TUS、SANTOS、基准再分析、STEER、SportsTables、DeepMatcher、匹配画像、Morpheus、VersaMatch、DiffPrep共10项。另24项在台账中明确标为“范围取样未纳入”，并按其技术族说明取舍；这不表示它们不相关、质量低或没有全文，也不声称逐一精读24篇全文。
4. 补充引文和主题发现4项：Auto-Pipeline来自DeepPrep及Text-to-Pipeline的参考文献；Baran来自Jellyfish及REIN；Valentine来自Chen等综述参考文献；REIN通过面向清洗评测的独立题名查找取得正式EDBT全文。补充入口及出版核对见[EVIDENCE.md](../EVIDENCE.md)。
5. 既有34项加新增14项，最终48项全部在正文引用。本文不把种子文献与新增检索记录的相关度排名解释为影响力排序。

[screening.json](screening.json)含120条原始记录映射和117项工作级决定；[counts.json](counts.json)记录漏斗数量；[coverage.json](coverage.json)记录全部48项的任务/流程/背景归类。范围取样的24项候选可用于下一轮扩展，但没有被隐藏在“不相关”统计中。

## 覆盖及局限

36项为方法/基准，12项为综述、规范或仅主题背景。非互斥覆盖为数据发现5、语义理解8、清洗修复14、匹配融合7、结构转换11、标注增强4，另有11项流程构造/评测。论文按可独立评价的输出对象编码，不因标签是模型输入而自动归入标注增强。数字不是领域发表量。

范围明显偏重关系表和流程；训练语料/标注方向覆盖较少。每式前15条截断、Crossref收录不均衡、作者种子追溯和单轮目的性筛选仍可能遗漏重要研究，因此新增统计提高可核查性，不等于已经证明完整性。

## 复核

离线运行“python scripts/check_review_evidence.py”可从原始返回和台账重新核对120→117→34→10及覆盖数量；“python scripts/check_manuscript.py”检查引用。

联网重放执行“python scripts/collect_search.py --output /tmp/idp-search-replay”。脚本读取已存请求参数，向新目录写入当前时间的查询快照，不覆盖2026-09-09台账。数据库的排序与元数据会更新，重放不保证获得完全相同的结果；已提交的响应是本文统计的固定输入。
