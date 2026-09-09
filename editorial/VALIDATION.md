# 交付检查

检查日期：2026-09-09。

- `latexmk -xelatex -outdir=build main.tex`：通过；XeLaTeX与Biber完成引用解析，生成13页A4 PDF。
- `python scripts/check_manuscript.py`：通过；34个引用键全部使用，无未定义或重复引用、DOI及标签；2幅图和4张表的引用完整，配图文件与prompt均存在。
- 出版源检查：`main.tex`、`manuscript.tex`、`references.bib`不包含具身智能、机器人或Open X-Embodiment内容；旧应用示意图及相关条目已移除。
- 编译日志：无未定义引用、缺失字符或overfull/underfull排版警告。旧版TeX Live的fontspec对Fandol字体给出2项CJK Script元数据提示；实际中文字符完整呈现，未出现方框或缺字。
- PDF检查：13页均含有效文字；图1位于第4页、图2位于第8页；通过文本坐标检查，未发现超出页面边界的文字块。
- 视觉抽查：标题与摘要页、两幅图、方法及评测比较表、两页参考文献均已渲染检查；标签、表格边界、引用编号和图注可读，无裁切及图文重叠。
- `git diff --check`：通过。
- 分发PDF：[output/survey.pdf](../output/survey.pdf)，由本次正文及参考文献编译得到。图片约235 ppi（166 mm宽），若具体期刊要求更高分辨率，需按该要求另行生成；当前未指定投稿期刊。

以上检查针对稿件、引用和排版，没有重新运行原论文中的模型或实验。具体文献访问和核验边界见[SOURCES.md](SOURCES.md)。
