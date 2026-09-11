# LaTeX 工程交付检查

核验日期：2026-09-11。对应《数据准备与语言模型的交叉前沿》及当前 Overleaf 工程。

- 正文8162个汉字，含章节标题和图注。LM4DP为2422字，DP4LM为2480字，具身部分1439字。
- 50项参考文献均被正文引用，Biber输出顺序与正文首次引用顺序一致，无重复书目键、未定义引用或失效图号。
- 两张研究分枝图直接采用作者提供的`ai4dp.pdf`和`dp4ai.pdf`，共49个节点，覆盖全部50项引用；每张图六条主枝，第一张29个节点、第二张20个节点。逐项检查源PDF中的年份、引用编号和预印本标记与节点清单一致，各分支的引用标签坐标没有跨年份倒置。源文件SHA-256保持一致，编译稿中的源图文字均可提取，矢量路径保留，未栅格化，详见[PDF来源记录](../figures/reviews/author_research_maps.json)。历史PNG的坐标审校不用于当前PDF。
- 已查看源图及插入后的横向页面。`dp4ai.pdf`原文件的RoboMIND 2.0/DROID标签存在边框与文字重叠，“Model collaps”缺少末尾的e；此次插入保留原文件，不将这些源图问题记为排版修复。
- 两幅原图以矢量PDF嵌入，原始数量、类别和配色保持原样，来源记录见[provenance.json](../figures/original/provenance.json)。正文描述样本文献的分布，未新增或外推统计数量。
- 作者简介源文件和两张作者照片沿用此前版本。
- XeLaTeX及Biber编译通过，PDF共14页，两张研究分枝图分别在第2、3页的横向页面，两幅原图分别在第4、6页，文末包含参考文献和作者简介。
- 已检查正文、原图、参考文献及作者简介页面。无空白页，编译日志无溢出版心、缺字、未定义引用或LaTeX错误。Fandol字体脚本提示不影响中文显示。
- 六项预印本统一以arXiv编号及版本标识著录，保留版本链接和访问日期；核读日期仅保存在证据记录中。AgiBot World 2026按公开数据资源著录。
- 已逐段检查投稿正文及图注，并扫描编译PDF全文，清理“原稿”“核读”“本轮修订”等制作过程用语；具体修改见[投稿文字清理记录](SUBMISSION_POLISH.md)。
- 本轮操作前后核对本地Word文件的SHA-256，均未改变。Word文件及Word生成脚本不随本轮LaTeX修改提交。

检查命令：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
python scripts/check_manuscript.py
python scripts/check_frontier_outputs.py
python scripts/check_review_evidence.py
```

PDF检查记录见[validation.json](frontier_sources/validation.json)。检查也在仅包含待提交文件的独立目录中执行，以确认Overleaf编译不依赖本地未跟踪文件。

历史检索台账检查针对上一轮48项书目与120条查询记录，不用于声称本轮检索覆盖。本文未重跑被综述论文的实验。
