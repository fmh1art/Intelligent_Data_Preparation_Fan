# 修订新增证据与编码依据

核验日期：2026-09-09。E1—E6与正文表4一致。数字来自原论文；百分点差和费用单位换算由本文计算。没有重跑所评述系统，不将不同数据、目标信息或模型下的分数合并排名。能力与机制的核验依据对应§3.7、§4.4和表2；正文中尚未核实的细节表示本次证据不足，不能解读为否定能力或未开源。

## 结果、基准与版本

| 编号/工作 | 原始来源及定位 | 核读字段与处理决定 |
|---|---|---|
| E1 / ATBench | [Auto-Tables正式PDF](https://www.vldb.org/pvldb/vol16/p3391-he.pdf)，§5.1、表2—3，3400—3401页；[作者评测代码](https://github.com/LiPengCS/Auto-Tables-Benchmark/blob/main/evaluate.py) | 244案例，26例多步；Hit@1=0.570、Hit@3=0.75；平均合成0.224秒。机器24 vCPU、4 P100。原文指示量求和记法与代码有差异，代码在首次命中标注算子/参数序列或替代真值后记1并停止；本文按实现解释，不视为任意等价程序的输出匹配。Hit@3保留候选选择环节，不写成75%全自动成功。其他方法时延排除了部分超时，不直接算加速倍数。 |
| E2 / AutoPrep | [作者v3正文](https://arxiv.org/html/2412.10422v3)，§6.1—6.2、表2；正式书目PVLDB18(10):3504—3517 | DeepSeek-V2.5-Chat，NL2SQL→加入AutoPrep：WikiTQ 52.83→66.09，TabFact 70.21→87.85；差13.26/17.64百分点。测量答案质量。上下文8192、温度0.01；该对照表未逐项给费用，不填0。 |
| E3 / DeepPrep | [正式PDF](https://www.vldb.org/pvldb/vol19/p3371-fan.pdf)，§6.1、表1、表2a及表3，3378—3380页 | Qwen3-14B、Synth-Spider：IL准确率61.70/完成率85.26%，DeepPrep67.18/97.21%。均仅用Synth-Spider训练；不能单独归因回退。Qwen3-8B表3：65.99→移除PAT后22.21。未估读费用曲线。 |
| E4—E5 / PrepBench | [作者arXiv v1全文](https://arxiv.org/html/2605.08687v1)，§3、§5.1—5.2、表6 | 306任务、829输入表、32领域、3—18步。费用单位**USD×10^-3/任务**，含相应路径中的调用和重试。GPT-5.1-Codex端到端代码54.9/115.40、工作流34.6/264.10；给无歧义说明85.3/82.74。Gemini 3 Flash端到端代码53.3/21.40。明确数字据v1；书目采用PVLDB正式元数据，不声称正式PDF已逐表校对。 |
| E6 / DiffPrep | [作者全文](https://arxiv.org/html/2308.10915v1)，§5.1、表2—3 | connect-4，逻辑回归，60/20/20划分；BoostClean0.690、DP-Fix0.732、DP-Flex0.701。BoostClean被适配为多分类。15/18→10/18是逻辑回归与两层网络下DP两变体合计达到最优的数据集数，不是错误减少比例。 |
| PARROT | [Text-to-Pipeline v2](https://arxiv.org/html/2505.15874v2)，表2—3、§4.5 | 17168任务、源池23009表、16算子；14388/1387/1393划分。原稿约1.8万的概数已改为v2统计。规范化比较忽略行列排列并使用数值容差。 |
| DeepPrep评测集 | 同上DeepPrep正式PDF表1及§6.1 | Synth-Spider训练6788/测试2008，Synth-Bird测试1150；改写Parrot测试1365、Buildings105。与原版PARROT测试1393不同，描述、算子数与比较规则也有差异，不合并比较。 |
| SportsTables | [期刊原文](https://link.springer.com/article/10.1007/s13222-023-00457-y)，§4.1—4.2 | 1187表、24838列、约86%数值列；宏/加权F1及文本、数值分组；重新训练模型而非直接零样本部署。 |
| EM任务画像 | [作者机构PDF](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Research/Web-based_Systems/pub/CIKM2020_Primpeli_Bizer.pdf)，摘要、§3—4；[机构记录](https://madoc.bib.uni-mannheim.de/57249/) | 21项既有任务的补充与画像；强调候选构造和难度，不使用跨论文平均F1。 |
| Valentine | [作者全文](https://arxiv.org/html/2010.07386v1)，§IV—VI；正式DOI10.1109/ICDE51399.2021.00047 | 540组合成表对；4 WikiData、7 Magellan、2 ING，后两组工业数据非公开；四种发现关联设置中的模式匹配。§II明确使用Recall@k（k=真值映射数，等价该位置的R-Precision），并不报告普通阈值Precision/Recall/F1。 |
| REIN | [EDBT正式PDF](https://openproceedings.org/2023/conf/edbt/3-paper-49.pdf)，摘要、§2及结论 | 14数据集、19检测器、19修复方法、33学习模型；499—511页、DOI10.48786/edbt.2023.43。Crossref题名首项误为ReClean，已拒绝；按正式PDF修正书目。 |

## 新增方法的定位证据

| 引用键 | 原始来源 | 采用范围 |
|---|---|---|
| tus | [出版DOI](https://doi.org/10.14778/3192965.3192973)，Crossref出版摘要 | 基于值域等证据的数据发现；不把可并表直接等同业务可用。 |
| santos | [作者预印本](https://arxiv.org/abs/2209.13589)、Crossref正式记录10.1145/3588689 | 列间关系与外部/合成知识库补充逐列语义。 |
| fishy | [ACL原始摘要及PDF](https://aclanthology.org/2025.trl-1.7/) | 简单方法与基准特征构成混杂；不推定所有发现方法无效。 |
| steer | [DFKI机构记录](https://www.dfki.de/web/forschung/projekte-publikationen/publikation/14385)、出版摘要 | 数据编程产生新域标签并适配类型模型；Christian Schalles重复名按机构记录纠正，文章号201。 |
| deepmatcher | [出版DOI](https://doi.org/10.1145/3183713.3196926)、出版元数据 | 深度实体匹配的组件化比较；仅作为方法路线参照。 |
| morpheus | [作者项目](https://utopia-group.github.io/morpheus/)、[作者PDF](https://www.cs.utexas.edu/~swarat/pubs/pldi17-morpheus.pdf)，§8—9 | I/O示例、类型引导枚举、SMT与部分求值；找到示例一致程序即停止，实验超时为5分钟；PLDI版与SIGPLAN Notices转载合并。 |
| versamatch | [出版DOI](https://doi.org/10.14778/3583140.3583148)、出版摘要 | 弱监督源与判别模型集成；本体映射为输出，弱标签是机制。 |
| autopipeline | [作者全文](https://arxiv.org/html/2106.13861v1)，§2—4 | 类比目标包含其他批次具体记录；目标键/依赖用于搜索，测试真值留出。§3搜索在候选数满足要求或达到最大深度时停止，再返回排序候选。 |
| baran | [正式DOI](https://doi.org/10.14778/3407790.3407801)、Crossref摘要；Jellyfish参考文献与REIN | 统一上下文与迁移修复，不写未核对的效果倍率。 |
| diffprep | 上方E6来源；[作者代码](https://github.com/chu-data-lab/DiffPrep) | 可微流程/模型联合优化，验证损失选轮；公开代码不表示本文复现。 |

## 能力与机制的核验依据

- **自动化**：区分人工决定下一步、完成局部任务、构造流程、依据反馈修订四种能力；不形成单调性能排序。原矩阵代号已从正文删除。
- **目标实例**指运行时可见目标表记录，训练标签、提示示例另计；Morpheus为当前输入输出，Auto-Pipeline为类比目标，无目标实例仍可能需要模式或标签。
- **独立检查**记录可利用的非生成性依据，不把约束参与HoloClean推断说成另设验证器；训练和评测真值与部署反馈分开。
- **回退/重试**区分搜索候选、局部重试和物化中间状态。DeepPrep依据正式§4.1—4.2；训练奖励依据§5。停止为模式满足及answer动作，另有探索轮数与扩展长度限制。
- **HAIPipe**依据[作者PDF](https://nantang.github.io/research/pubs/haipipe.pdf)§4—6与[作者代码](https://github.com/ruc-datalab/Haipipe)：枚举/采样人工和自动流程的组合，以下游表现选优。
- **AutoPrep**依据上方v3正文；其结论把多表扩展列为未来方向，因此不视为一般多表流程。
- **Pipeline-Agent**依据v2 §6—7：当前表/历史反馈及多表任务；历史状态恢复、确切步数上限未核定，正文保留核验边界。
- **BAT**依据[正式出版摘要](https://doi.org/10.1145/3802020)和[作者实现](https://github.com/ZJU-DAILY/BAT)。未获足以逐项核对的正式算法全文，停止细节留白；不把早期MontePrep全文的实测结果归给BAT。DeepPrep表内MontePrep基线也不等同当前BAT代码。
- **PrepBench代理**是基准评测配置，不是另一个新算法。v1 §5.1明确Clarify、Profile、Code、Translate；Profile最多2次，Code/Translate最多3次。澄清与接收初始指令分别讨论。
- **公开产物**依据论文/作者项目声明：[Auto-Tables基准](https://github.com/LiPengCS/Auto-Tables-Benchmark)、[AutoPrep](https://github.com/ruc-datalab/AutoPrep)、[DeepPrep](https://github.com/ruc-datalab/DeepPrep)、[PrepBench](https://github.com/TsinghuaDatabaseGroup/prepbench)。Jellyfish正式论文给出模型链接；尚未核验不表示不开源。均未重跑或验证完整复现条件。

## 图与构造实例

原任务体系图、通用执行反馈图已删除；任务边界由§2.2文字说明，流程角色及机制由§4.3、§4.4和表2说明。这些分类与关系仍属于本文归纳。

当前图1（原图3）为作者构造反例，[prompt与生成记录](../figures/GENERATION.md)随仓库保存。运行“python scripts/reproduce_example.py”可复核250/150，以及退款10变15后的245/145。脚本不统计真实错误频率或重现论文系统。第6节以连贯文字区分原论文结果、本文归纳和待验证设想，原E/S/H标签已删除，结果表的E1—E6编号继续用于定位。

补充公开代码核验：[HoloClean](https://github.com/HoloClean/holoclean)、[Raha](https://github.com/BigDaMa/raha)、[Ditto](https://github.com/megagonlabs/ditto)的作者仓库可访问；正文据此说明代码公开，仍未重跑实验。DeepPrep §6.3关于仅通过列重命名满足表面模式的行为作为失败类型证据，不另估计频率。
