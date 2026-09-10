# LaTeX 工程交付检查

核验日期：2026-09-10。对应《数据准备与语言模型的交叉前沿》及当前 Overleaf 工程。

- 正文8267个汉字，含章节标题和图注。LM4DP为2454字，DP4LM为2484字，具身部分1445字。
- 50项参考文献均被正文引用，Biber输出顺序与正文首次引用顺序一致，无重复书目键、未定义引用或失效图号。
- 双树图49个节点覆盖全部50项引用，文献编号与首次引用顺序、年份与书目逐项核对。本次重构为12个独立子方向区域及1个共享根部区域，逐项核对论文归属、标题与分支连接，全部节点位于各自所属区域；记录区域边界和49个标签边界，计入坐标核读误差后没有枝内跨年份倒置，详见[分类与年代审校](../figures/reviews/fig00_two_research_trees_taxonomy.json)。本版采用枝内时间顺序，不同分支区域之间不共用时间轴；最终PNG无代码叠字或插值放大，原生尺寸为1086×1448像素。PDF内嵌图像与最终PNG逐像素一致。
- 两幅原图以矢量PDF嵌入，原始数量、类别和配色保持原样，来源记录见[provenance.json](../figures/original/provenance.json)。图内数据作为历史统计使用。
- 作者简介源文件和两张作者照片沿用此前版本。
- XeLaTeX及Biber编译通过，PDF共13页，双树总览图在第2页，两幅原图分别在第3、5页，文末包含参考文献和作者简介。
- 已检查正文、原图、参考文献及作者简介页面。无空白页，编译日志无溢出版心、缺字、未定义引用或LaTeX错误。Fandol字体脚本提示不影响中文显示。
- 六项核读预印本的版本说明在书目中显示。RoboMIND 2.0首次提交与2026年修订日期分开记录，AgiBot World 2026按公开数据资源著录。
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
