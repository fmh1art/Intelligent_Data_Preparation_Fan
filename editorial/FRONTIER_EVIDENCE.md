# 本轮文献与证据说明

核验日期：2026-09-10。本文为代表性技术综述，没有重跑被综述系统，也不将不同任务和模型的结果合并排名。

## 检索与数据返回

本轮使用arXiv API批量核验9个明确的论文标识符，使用Crossref题名检索补充5项工作，并直接读取ACL Anthology、PMLR、NeurIPS论文集、论文作者项目页与数据发布方资料。API端点、完整请求参数及HTTP返回状态见[requests.json](frontier_sources/requests.json)。

- arXiv端点：`https://export.arxiv.org/api/query`。9项均有返回，原始Atom XML见[arxiv_batch.xml](frontier_sources/arxiv_batch.xml)，结构化返回见[arxiv_parsed.json](frontier_sources/arxiv_parsed.json)。
- Crossref端点：`https://api.crossref.org/works`，`query.title`与`rows=3`。完整原始JSON分别为[nalir](frontier_sources/nalir.json)、[demonstrations](frontier_sources/demonstrations.json)、[collapse](frontier_sources/collapse.json)、[doremi](frontier_sources/doremi.json)、[rag](frontier_sources/rag.json)。
- RAG查询有返回，但前3项没有匹配目标原始论文，未采用。改用[NeurIPS 2020原论文](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)。其余4项通过精确题名选择，选择记录见[selection.json](frontier_sources/selection.json)。

这些查询用于补入和核验具体文献，不构成穷尽检索。上一轮120条Crossref记录、117项去重文献的台账只属于历史稿件。当前正文不再将该数字作为本轮综述的筛选流程。

## 新补材料与采用范围

| 材料 | 核验来源 | 正文采用内容与边界 |
|---|---|---|
| NaLIR | [PVLDB原论文](https://www.vldb.org/pvldb/vol8/p73-li.pdf)、Crossref | 自然语言解析和交互式查询，不声称覆盖任意复杂业务需求 |
| PICARD | [EMNLP 2021](https://aclanthology.org/2021.emnlp-main.779/) | 增量解析约束生成，语法有效与任务正确分开 |
| DIN-SQL | [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html) | 模式关联、查询分解及修正，不引用动态排名或引用次数 |
| Dolma | [ACL 2024](https://aclanthology.org/2024.acl-long.840/) | 语料组成、处理流程及中间状态分析，不沿用原稿未经本轮验证的压缩量 |
| DataComp-LM | [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/19e4ea30dded58259665db375885e412-Abstract-Datasets_and_Benchmarks_Track.html) | 在受控训练设置中比较准备策略，不把下游得分当作数据通用评分 |
| FineWeb2 | [arXiv:2506.20920v1](https://arxiv.org/abs/2506.20920v1) | 语言适配、去重及基于质量和重复次数的数据平衡，按核读预印本著录 |
| DoReMi | [出版DOI](https://doi.org/10.52202/075280-3059)、Crossref | 用代理模型学习领域混合权重，不泛化为所有任务通用的最优配比 |
| LESS | [ICML 2024/PMLR](https://proceedings.mlr.press/v235/xia24c.html) | 低维梯度数据选择。5%数据常超过全量训练是论文在所测任务中的报告，不是普遍保证 |
| Self-Instruct | [ACL 2023](https://aclanthology.org/2023.acl-long.754/) | 从种子生成指令、输入、输出并过滤无效及相似样本 |
| OpenThoughts | [arXiv:2506.04178v2](https://arxiv.org/abs/2506.04178v2)及[作者数据配方](https://www.open-thoughts.ai/blog/ot3) | 问题来源、选择、回答生成和公开实验。正文随后关于中间步骤核验的讨论是本文分析，没有宣称全部样本经过独立证明 |
| 递归合成数据与模型退化 | [Nature原论文](https://www.nature.com/articles/s41586-024-07566-y)及[2025年勘误](https://www.nature.com/articles/s41586-025-08905-3) | 限定于递归生成的实验条件。勘误修正理论部分的符号，不影响本文不涉及该公式的定性表述 |
| RAG | [NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html) | 检索外部内容用于生成，不声称能保证消除幻觉 |
| 上下文示例选择 | [DeeLIO 2022](https://aclanthology.org/2022.deelio-1.10/) | 示例与目标问题的关系，数据准备任务中的边界例建议属于本文归纳 |
| Data-Juicer 2.0 | [NeurIPS 2025论文集](https://proceedings.neurips.cc/paper_files/paper/2025/hash/76dbd7e897be2eb883ede598b91270fb-Abstract-Datasets_and_Benchmarks_Track.html) | 多模态算子与自适应执行。按会议年份2025著录，区别于网页元数据中的2026上线日期 |
| Open X-Embodiment | [核读版本v9](https://arxiv.org/abs/2310.08864v9)、[作者项目](https://robotics-transformer-x.github.io/) | 跨机构、跨机器人数据汇集。正文的坐标、单位和动作含义检查属于结合该场景的数据准备分析 |
| DROID | [核读版本v2](https://arxiv.org/abs/2403.12945v2)、[项目更新](https://droid-dataset.github.io/) | 分布式真实场景采集及2025年4月相机标定更新，不将发布后维护说成首次发布就已具备 |
| AgiBot World Colosseo | [核读版本v4](https://arxiv.org/abs/2503.06669v4) | 真实操作的任务与场景覆盖，不混用2025和2026资源的规模统计 |
| AgiBot World 2026 | [数据卡](https://huggingface.co/datasets/agibot-world/AgiBotWorld2026)、[发布方说明](https://www.agibot.com/article/231/detail/54.html) | 数据卡的子任务、物体框、步骤级指令及Error/Success/Intervention相关字段，发布说明中的错误恢复轨迹。按数据资源著录，不冒称同行评审论文 |
| RoboMIND 2.0 | [v3，2026-02-27](https://arxiv.org/abs/2512.24653v3)、[全文§3及§4](https://arxiv.org/html/2512.24653v3) | 双臂操作、触觉、移动操作与配套仿真。首次提交为2025-12-31，正文明确说2026年更新，书目保留首次提交和核读版本日期 |
| MimicGen | [CoRL 2023/PMLR](https://proceedings.mlr.press/v229/mandlekar23a.html) | 适配少量演示并重放生成操作数据，真实环境效用仍需另行检验 |

## 沿用证据与综合判断

29项既有书目沿用此前的出版核验，原始记录在[metadata](metadata)和[EVIDENCE.md](EVIDENCE.md)。AutoPrep的52.83%→66.09%引用其DeepSeek-V2.5-Chat、WikiTQ问答对照，见[作者v3的表2](https://arxiv.org/html/2412.10422v3)。这是问答准确率变化，不是清洗操作准确率。本轮未再使用历史E1—E6的全部数值。

具身章节中关于失败轨迹应按用途区分、训练测试按场景及同源轨迹隔离、成本覆盖采集与复核等内容属于本文综合分析和评价建议，没有写成已被统一实验验证的结论。原图仅保留其历史统计意义，未新增或重算国内外论文数量。

正文与Biber输出的文献编号由[引用顺序文件](frontier_sources/citation_order.json)核对。LaTeX书目显式标记所引预印本及核读版本，不将预印本版本记录等同于该工作从未正式发表。
