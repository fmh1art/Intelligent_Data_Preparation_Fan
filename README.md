# 智能数据准备研究综述

本文围绕数据发现、语义理解、清洗修复、匹配融合、结构转换和标注增强，整理范举、李国良、高云君等学者及国内外相关研究，进一步比较任务感知流程与评测方法。

- [编译后的综述 PDF](output/survey.pdf)
- [LaTeX 主文件](main.tex)、[正文](manuscript.tex)、[参考文献](references.bib)
- [文献来源、核验范围与版本说明](editorial/SOURCES.md)
- [中文综述写法参照与修改说明](editorial/REVISION.md)
- [绘图记录](figures/GENERATION.md)、[图1 prompt](figures/prompts/fig01_taxonomy.md)、[图2 prompt](figures/prompts/fig02_workflow.md)

## 编译

需要 XeLaTeX、Biber、ctex 和 biblatex-gb7714-2015；使用 TeX Live 自带的 Fandol 字体。

```bash
latexmk -xelatex -outdir=build main.tex
python scripts/check_manuscript.py
mkdir -p output
cp build/main.pdf output/survey.pdf
```

Overleaf 中将 `main.tex` 设为主文件，编译器选择 XeLaTeX。当前版式是通用学术综述排版，不是期刊官方模板；作者简介素材单独保存在 `author_bios.tex`，默认不载入。

文献检索截止日期为2026年9月9日。本文为代表性文献综述，未重新执行所评述方法的实验。`editorial/metadata/` 保存Crossref原始返回与请求端点；网络复核脚本为 `scripts/collect_metadata.py`，它只读取出版元数据，不修改参考文献库。
