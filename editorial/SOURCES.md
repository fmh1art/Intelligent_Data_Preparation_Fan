# 文献来源与核验记录

> 历史记录：本文件中的章节、图表编号和页数对应前期长稿。当前8k版本的内容对应见[本轮修订](REVISION_8K.md)，排版检查见[VALIDATION.md](VALIDATION.md)。

核验日期：2026-09-09。修订后参考文献为48项，全部在正文引用。原稿及本次修订通过出版平台、作者公开论文和学术搜索发现文献，以Crossref检查DOI元数据，并以期刊官网与原文处理出版版本及中文条目。没有使用博客、自动翻译页面或模型生成摘要作为论文技术结论的证据。

## 检索与保留规则

检索围绕“数据准备 / data preparation”“数据清洗 / data cleaning”“实体匹配 / entity matching”“流程合成 / pipeline synthesis”“中文综述”和范举、李国良、高云君相关论文展开。追溯早期代表方法并关注2023—2026年的发展；保留具有明确技术问题、机制或评测设置的论文。

本次访问的结构化学术数据库为 **Crossref REST API**。请求端点采用 `https://api.crossref.org/works/{doi}`，题名发现采用 `https://api.crossref.org/works?query.bibliographic=...&rows=3`。每次请求的准确URL、状态码和原始JSON位于[metadata目录](metadata/)；题名检索实际选择的记录见[metadata_selection.json](metadata_selection.json)。可用[scripts/collect_metadata.py](../scripts/collect_metadata.py)复核元数据，脚本不自动把搜索首条结果写入BibTeX。

网页与预印本发现使用学术搜索、arXiv、ACM、IEEE、VLDB、ACL Anthology、中文期刊官网和作者主页。DBLP仅用于发现和记录交叉核对，不替代论文原文。未宣称检索CNKI、Web of Science等本次未调用的付费数据库；原稿没有完整筛选统计；审稿修订新增独立的固定查询筛选流程，见[检索协议与台账](search/README.md)，不倒推旧稿筛选数量。

## 近期中文参照

| 文献 | 已核验内容 | 写法借鉴及限制 |
|---|---|---|
| [刘祺等，2025，数据质量研究述评](https://sysengi.cjoe.ac.cn/CN/PDF/10.12011/SETP2023-2891) | 期刊PDF的题名、作者、卷页；全文文本中的摘要、引言、概念、分类与展望 | 概念—体系—方法—问题的学术组织方式；未引用其文献计量统计或经济损失数据 |
| [周立等，2025，不完整时序数据补全综述](https://crad.ict.ac.cn/cn/article/pdf/preview/10.7544/issn1000-1239.202550449.pdf) | 期刊PDF索引中的摘要、相关工作与概念定义片段；作者、卷页和DOI | 比较表与评测因素的组织；直接下载受代理限制，没有声称通读全部实验或重现实验 |
| [高云君等，2023，数据集成综述](https://www.jos.org.cn/jos/article/abstract/6808) | 官网索引摘要及出版信息 | 实体解析、融合、清洗的分类；直接打开全文返回403，采用已取得的期刊索引内容 |

上述3个中文DOI的Crossref查询均返回 **404**，保留原始失败响应；这表示该服务未返回对应元数据，不表示文章不存在。BibTeX依据期刊公布的信息手工录入。

## 关键出版版本决策

- **PrepBench**：原稿为2026-05-09预印本。Crossref正式记录为PVLDB **19(10): 2866–2879 (2026)**，DOI [10.14778/3828612.3828638](https://doi.org/10.14778/3828612.3828638)。已更新为正式条目。本次任务、基准规模及实验表6均核对[作者v1全文](https://arxiv.org/html/2605.08687v1)，正文明确该数字版本，不声称已对正式PDF逐表核对。
- **DeepPrep**：核对[VLDB正式PDF](https://www.vldb.org/pvldb/vol19/p3371-fan.pdf)，确认为19(11):3371–3384，DOI 10.14778/3836663.3836695。本次在原机制分析外，增加表1—3的规模、准确率、完成率与消融数据，详见[EVIDENCE.md](EVIDENCE.md)；仍不引用未核实的摘要倍率。
- **AutoPrep**：正式卷页由Crossref核验为18(10):3504–3517。技术机制核对[作者arXiv v3正文](https://arxiv.org/html/2412.10422v3)；该预印本内页的占位卷页不用于书目。
- **Text-to-Pipeline**：固定使用[arXiv v2](https://arxiv.org/abs/2505.15874v2)，2025-11-10，作者包含Zhangyan Ye；不混用v1作者列表或v1的分数。本次按v2表2—3更新为17168任务、16类算子，并区别DeepPrep改写后的Parrot。
- **BAT**：采用ACM正式条目4(3):143:1–143:25，DOI 10.1145/3802020。机制核对出版方存入Crossref的摘要及[作者实现仓库](https://github.com/ZJU-DAILY/BAT)。不把曾用题名MontePrep作为另一项独立研究；明确无目标表实例仍有目标模式。
- **Unicorn**：采用2023年PACMMOD原始论文，第一作者Jianhong Tu，DOI 10.1145/3588938。2024年SIGMOD Record研究亮点版本的第一作者和题名不同，不混合两版信息。
- **Data Management for Machine Learning: A Survey**：题名查询的首项误匹配到天文学书章，已拒绝；以准确DOI 10.1109/TKDE.2022.3148237重新检索。Crossref仍保留2022年early access及1–1占位页码；按[作者公开的正式PDF](https://luoyuyu.vip/files/DM4ML_Survey.pdf)使用2023年35(5):4646–4667。
- **Empowering Tabular Data Preparation with Language Models**：引用[ACL 2026正式记录](https://aclanthology.org/2026.acl-long.8/)，228–246，DOI 10.18653/v1/2026.acl-long.8；不继续使用2025预印本年份。
- **Can LLMs Clean Up Your Mess?**：引用[2026-01-22 arXiv v1](https://arxiv.org/abs/2601.17058v1)，明确为预印本。没有把预印本中的期刊模板当作正式发表证明。
- **FM、Ditto、Snorkel**：按PVLDB实际出版年分别保留2022、2020、2017，避免与会议举办年混淆。

## 原稿技术依据（修订扩展以EVIDENCE.md为准）

“全文片段”表示本次查看了相关原文部分，不表示逐页精读整篇。出版摘要可以支撑方法定位，不能支撑摘要未披露的训练、消融或性能细节。

| 引用键 / 工作 | 主要证据 | 正文使用范围 |
|---|---|---|
| demystify | [ACM DOI](https://doi.org/10.1145/3555041.3589406)、Crossref题名作者 | AI辅助数据准备的研究定位 |
| quality | [ACM DOI](https://doi.org/10.1145/1541880.1541883)、出版摘要 | 质量维度、方法比较及适用条件 |
| dm4ml | [正式PDF](https://luoyuyu.vip/files/DM4ML_Survey.pdf)、出版元数据 | 机器学习生命周期及发现、清洗、标注 |
| aurum | [MIT项目原始说明](https://www.csail.mit.edu/research/aurum-large-scale-data-discovery)、Crossref | 声明式数据发现和候选关系 |
| sato | [DOI](https://doi.org/10.14778/3407790.3407793)、出版摘要 | 列值、表上下文、主题与结构化预测 |
| fm | [VLDB PDF](https://www.vldb.org/pvldb/vol16/p738-narayan.pdf)、出版摘要 | 将数据整理任务表达为提示任务 |
| holoclean | [DOI](https://doi.org/10.14778/3137628.3137631)、出版摘要 | 约束、统计和参考信息的概率修复 |
| raha | [作者PDF](https://raulcastrofernandez.com/papers/raha.pdf)的摘要及贡献段、Crossref | 检测特征、聚类抽样和用户监督 |
| interactiveclean / Falcon | [作者PDF](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/sigmod2016-clean.pdf)的工作流及规则定义 | 从用户修复生成、确认SQL更新规则 |
| ditto | [DOI](https://doi.org/10.14778/3421424.3421431)、出版摘要 | 序列对分类及知识、摘要、增强机制 |
| unicorn | [作者原始论文PDF](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/Unicorn_PACMMOD.pdf)、出版摘要 | 多任务匹配、共享编码与专家混合 |
| icl_er / BATCHER | [ICDE正式PDF](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/ICDE24-ER.pdf)的摘要、方法及局限片段 | 示例选择、问题分批和标签成本 |
| jellyfish | [ACL正式PDF](https://aclanthology.org/2024.emnlp-main.497.pdf)的摘要及方法 | 指令微调、知识注入及四类预处理 |
| knowtrans | [IEEE正式DOI](https://doi.org/10.1109/ICDE65448.2025.00214)、Crossref作者与题名 | **仅保留知识增强与迁移的主题定位**；未取得可核读全文，不展开具体算法、few-shot配置或量化效果 |
| wrangler | [作者实验室页面](https://idl.uw.edu/papers/wrangler)、[作者PDF](https://idl.cs.washington.edu/files/2011-Wrangler-CHI.pdf)、Crossref | 交互式变换与脚本表达 |
| autotables | [VLDB正式PDF](https://www.vldb.org/pvldb/vol16/p3391-he.pdf)的任务、模型与搜索部分 | 输入表关系化、变换预测及多步搜索 |
| snorkel | [DOI](https://doi.org/10.14778/3157794.3157797)、出版摘要 | 标注函数和弱监督建模 |
| activeclean | [DOI](https://doi.org/10.14778/2994509.2994514)、出版摘要 | 凸损失模型条件下的渐进清洗 |
| goodcore | [作者正式PDF](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/goodcore.pdf)片段、出版摘要 | 不完整数据的核心子集选择与梯度近似 |
| haipipe | [作者实现](https://github.com/ruc-datalab/Haipipe)、出版摘要及作者论文片段 | 人工流程与自动流程组合及下游筛选 |
| autoprep | 上方版本决策所列来源 | 问题感知规划与逻辑、物理分层 |
| deepprep | 上方版本决策所列正式PDF的方法部分 | 中间状态、树状推理和回退；不声称可检测所有语义错误 |
| texttopipeline | arXiv v2原始摘要 | 指令与算子映射、中间反馈及基准组成 |
| bat | 出版摘要与作者仓库 | 操作沙箱、树搜索、执行反馈和目标模式条件 |
| prepbench | 正式元数据、arXiv原始摘要 | 交互消歧、代码生成与流程翻译的评测定义 |
| datajuicer | [作者预印本](https://arxiv.org/abs/2309.02033)、正式DOI元数据 | 可组合语料处理与分析系统 |
| llmdata | [JCST期刊原始页面](https://jcst.ict.ac.cn/article/doi/10.1007/s11390-026-5948-8) | 预训练、持续预训练和后训练的数据需求 |
| empower | ACL正式摘要与PDF | 获取、集成、清洗、转换的分类 |
| llm_ready | arXiv v1原始摘要 | 清洗、集成、增强的相关综述定位 |
| datasheets | [作者预印本摘要](https://arxiv.org/abs/1803.09010)、[CACM DOI](https://doi.org/10.1145/3458723)、出版元数据 | 数据来源、组成、处理及用途说明 |
| fair | [Scientific Data原文](https://www.nature.com/articles/sdata201618)、出版元数据 | 可查找、可访问、可互操作及可重用 |
| zh_quality / zh_timeseries / zh_integration | 本文“近期中文参照”所列期刊来源 | 概念、分类与评测写法；不复制实验结果 |

## 归纳性判断与未做事项

- 六类任务框架、四层评测组织及当前保留的多表实例属于本文归纳或构造；原统一目标表达式和两幅概念图已删除。
- 诸如“约束满足不等于事实恢复”“候选对F1不包含阻塞阶段遗漏”“单次输出一致不证明程序对其他输入正确”是对评价边界的分析，不归为某篇论文独有的实验发现。
- 不报告无法在同一模型、数据和预算下比较的优劣排名，不补写缺失的实验数据。
- 没有获取作者照片或添加未经原稿提供的作者履历。作者简介默认不进入正文。
- 原论文全文仅在本地临时目录用于核读；仓库保存书目元数据、链接与本次撰写的综述，不重新发布原论文全文。

## 审稿修订补充

新增14项文献的定位、监督与机制核验和E1—E6量化证据，集中记录于[EVIDENCE.md](EVIDENCE.md)。检索原始记录、初筛/复筛、非互斥任务覆盖见[search目录](search/README.md)。REIN正式版已通过OpenProceedings核对为EDBT2023:499—511，DOI10.48786/edbt.2023.43；保留Crossref题名误匹配的原始记录，未使用其首项ReClean。
