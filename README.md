# 数据准备与语言模型的交叉前沿

本项目为可直接在 Overleaf 编译的中文综述。以用户上传的《04 数据准备与语言模型交叉技术的研究进展与发展趋势 - 编辑提问回答.docx》为底稿，将正文凝练至8162个汉字，平衡“语言模型用于数据准备”（LM4DP）和“面向语言模型的数据准备”（DP4LM），补充具身智能数据准备及近期研究。

- [LaTeX 编译稿 PDF](output/survey.pdf)
- [主文件](main.tex)、[正文](manuscript.tex)、[参考文献](references.bib)
- [两张研究脉络图与两幅原图](figures/README.md)
- [AI for Data Prep 矢量图](figures/ai4dp.pdf)、[Data Prep for AI 矢量图](figures/dp4ai.pdf)、[图稿来源与检查范围](figures/reviews/author_research_maps.json)
- [投稿文字清理记录](editorial/SUBMISSION_POLISH.md)
- [修订说明](editorial/REVISION_FRONTIER.md)、[文献证据](editorial/FRONTIER_EVIDENCE.md)、[编译检查](editorial/VALIDATION.md)

两条主线分别为2422字和2480字，具身部分1439字，涵盖跨机器人数据融合、时空对齐、分层标注、失败轨迹、仿真与评测。正文计数包含章节标题和图注，不含参考文献、作者简介、图内文字、标点及英文单词。无摘要、关键词、公式及技术表格，文末沿用范梅浩、范举的照片和简介。

引言后以两张英文研究脉络图分别展示AI for Data Prep与Data Prep for AI，直接嵌入作者绘制的`ai4dp.pdf`和`dp4ai.pdf`，在第2页的同一竖向页面上下排列，保留矢量线条和文字。每张图有六条独立主枝，同类论文沿所属主枝排列，枝内较新的工作位置较高。第一张图的灰色分支汇集共同基础和综述，第二张图以橙色突出具身数据。两图共49个节点，覆盖全部50项引用；AgiBot World 2026的数据卡与发布说明合并展示。原稿的两幅正文统计图以直接导出的矢量 PDF 嵌入，数量和类别保持原样，正文用于说明样本文献的任务分布，统计来源和背景保存在工程记录中。50项书目按 GB/T 7714—2015 顺序编码制著录，预印本用arXiv编号及版本标识著录。近期材料核验截至2026-09-10。本轮交付更新 LaTeX 工程，上传的 Word 文件保留在本地，不作修改。

## Overleaf 与本地编译

Overleaf 中选择 `main.tex` 为主文件、**XeLaTeX** 为编译器。工程使用 TeX Live 自带的 Fandol 字体、`ctex` 和 `biblatex-gb7714-2015`，Biber 由 latexmk 自动调用。所需插图及书目已包含在工程中，编译不依赖 Word、Office 或外部网络资源。

本地安装 XeLaTeX、Biber 和 latexmk 后运行：

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
python scripts/check_manuscript.py
python scripts/check_frontier_outputs.py
cp build/main.pdf output/survey.pdf
```

正文检查仅需 Python 3；PDF 检查另需 PyMuPDF，报告写入 `build/frontier_validation.json`。当前编译稿为13页。

书目核验记录保存在 [frontier_sources](editorial/frontier_sources)。如需从这些记录重建书目，可运行 `python scripts/build_frontier_bibliography.py`，依赖 `bibtexparser`、`lxml` 和 `requests`；正常编译无需重建。`scripts/collect_frontier_sources.py` 用于重新访问论文数据库和发布方页面。

## 历史记录

[上一轮8k修订说明](editorial/REVISION_8K.md)和[历史书目](editorial/previous_8k/references.bib)保留供核对，完整旧稿可从提交 `ddeaa78` 查阅。`python scripts/check_review_evidence.py` 检查上一轮120条检索记录及48项书目，不代表本轮50项书目的检索统计。
