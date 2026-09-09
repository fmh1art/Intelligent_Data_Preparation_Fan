# 智能数据准备研究综述

本文围绕数据发现、语义理解、清洗修复、匹配融合、结构转换和标注增强，整理范举、李国良、高云君等学者及国内外相关研究，进一步比较任务感知流程与评测方法。

- [编译后的综述 PDF](output/survey.pdf)
- [唯一保留的PNG配图与预览](figures/README.md)
- [LaTeX 主文件](main.tex)、[正文](manuscript.tex)、[参考文献](references.bib)
- [两份审稿意见的逐条回应](editorial/REVIEW_RESPONSE.md)
- [检索协议与筛选台账](editorial/search/README.md)、[结果及机制证据](editorial/EVIDENCE.md)
- [文献来源、核验范围与版本说明](editorial/SOURCES.md)
- [算术核查与原公式处理记录](editorial/FORMULA_AUDIT.md)
- [中文综述写法参照与修改说明](editorial/REVISION.md)
- [中文学术表达复核记录](editorial/STYLE_REVIEW.md)
- [图表精简说明](editorial/SIMPLIFICATION.md)
- [绘图记录](figures/GENERATION.md)、[图1详细prompt](figures/prompts/fig01_error_propagation.md)

## 编译

需要 XeLaTeX、Biber、ctex 和 biblatex-gb7714-2015；使用 TeX Live 自带的 Fandol 字体。

```bash
latexmk -xelatex -outdir=build main.tex
python scripts/check_manuscript.py
python scripts/check_review_evidence.py
python scripts/reproduce_example.py
mkdir -p output
cp build/main.pdf output/survey.pdf
```

Overleaf 中将 `main.tex` 设为主文件，编译器选择 XeLaTeX。当前版式是通用学术综述排版，不是期刊官方模板；作者简介素材单独保存在 `author_bios.tex`，默认不载入。

文献检索截止日期为2026年9月9日。当前稿件18页，含48项参考文献、4张精简比较表和1幅实例图。为减少手工重绘工作，删除两幅概念图，将说明性表格改为正文；审稿要求的筛选统计、机制比较、基准与结果证据继续保留。本文采用结构化范围取样，未重新执行所评述方法的实验。`editorial/metadata/` 保存Crossref原始返回与请求端点；网络复核脚本为 `scripts/collect_metadata.py`，它只读取出版元数据，不修改参考文献库。

固定检索120条，去重117项、复筛34项，新增纳入10项并另补充4项；原稿34项单列。复筛后24项因范围取样未纳入，理由保留。联网重放可执行“python scripts/collect_search.py --output /tmp/idp-search-replay”，新快照不会覆盖统计输入。
