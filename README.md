# 智能数据准备研究综述

本稿依据历史上内容最多的eae7c34版本压缩修订，保留48项国内外文献、六类准备任务、流程机制、评测基准与原论文结果，结合范举、李国良、高云君及国际研究，说明应用需求、研究进展和发展方向。

- [综述PDF](output/survey.pdf)
- [3幅学术风格PNG、图注与详细prompt](figures/README.md)
- [正文](manuscript.tex)、[主文件](main.tex)、[参考文献](references.bib)
- [文末作者简介](author_bios.tex)、[照片与信息来源](editorial/AUTHOR_INFO.md)
- [本轮8k修订说明](editorial/REVISION_8K.md)、[交付检查](editorial/VALIDATION.md)
- [文献筛选台账](editorial/search/README.md)、[原论文证据记录](editorial/EVIDENCE.md)

正文约8000字，按汉字统计为7871字，含章节标题和图注，不含参考文献、作者简介、图内文字及标点。保留3幅插图，省略摘要、关键词、公式和技术表格。文后按GB/T 7714—2015顺序编码制著录48项参考文献，文章最后提供两位作者各约150字的简介及各1张照片。

三幅图由专门绘图agent调用内置imagegen重新生成，使用白底、细线框、克制配色和小型机制图标。PNG及prompt供作者后续PPT复绘参考；当前实际1536×1024像素，未放大。作者照片使用本次提供的原文件，按比例排版。

## 编译

需要XeLaTeX、Biber、ctex和biblatex-gb7714-2015，字体使用TeX Live自带Fandol。

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex
python scripts/check_manuscript.py
python scripts/check_review_evidence.py
python scripts/reproduce_example.py
mkdir -p output
cp build/main.pdf output/survey.pdf
```

Overleaf中以main.tex为主文件，选择XeLaTeX。版式为通用中文学术综述格式，并非期刊官方模板。

## 修订与历史

最新要求为“基于历史内容最多版本压缩到8k”，已取代中途约5000字的改写方案。[完整底稿eae7c34](https://github.com/fmh1art/Intelligent_Data_Preparation_Fan/tree/eae7c34)及[前期语言润色版67f0fa6](https://github.com/fmh1art/Intelligent_Data_Preparation_Fan/tree/67f0fa6)可供对照。

[审稿回复](editorial/REVIEW_RESPONSE.md)、[中文综述写法参照](editorial/REVISION.md)、[语言复核](editorial/STYLE_REVIEW.md)、[前期图表精简](editorial/SIMPLIFICATION.md)、[公式审计](editorial/FORMULA_AUDIT.md)和[书目核验](editorial/SOURCES.md)作为历史记录保留。其中旧图表编号和页数不用于当前稿；本轮对应关系见[REVISION_8K.md](editorial/REVISION_8K.md)。
