# 交付检查

检查日期：2026-09-09。本记录对应两份审稿意见的大修版本。

- `latexmk -g -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex`：通过，XeLaTeX与Biber完成引用解析，生成20页A4 PDF。
- `python scripts/check_manuscript.py`：通过；48个引用键全部使用，无未定义或重复引用、DOI及标签；3幅图和9张表的引用完整，配图文件与prompt均存在。
- `python scripts/check_review_evidence.py`：通过；从固定查询原始返回复核120条记录、117项独立工作、34项复筛、10项检索纳入及4项额外补充；检查48项文献的覆盖映射、引用键与结果差值、费用换算。
- `python scripts/reproduce_example.py`：通过；SQLite执行直接连接及先聚合再连接，分别得到250与150；退款10变为15后分别为245与145，并验证订单键唯一性与独立总额恒等式。该脚本验证作者构造实例，不代表重跑被综述系统。
- 出版源检查：`main.tex`、`manuscript.tex`、`references.bib`不包含具身智能、机器人或Open X-Embodiment内容。
- 编译日志：无未定义引用、缺失字符或overfull/underfull排版警告；无要求重新运行Biber的提示。旧版TeX Live的fontspec对Fandol字体给出2项CJK Script元数据提示；实际中文字符完整呈现，未出现方框或缺字。
- PDF检查：20页均含有效文字，未发现超出页面边界的文字块；图1位于第5页、图2位于第11页、图3位于第12页。输出文件与本次编译文件逐字节一致。
- 视觉检查：标题与摘要、分类及能力比较、机制表、基准与结果表、参考文献和三幅图已渲染核查。最终排版抽查第9、11、12、14、15页，图表标签、数字、引用和图注可读，无裁切或图文重叠。
- 新图流程：详细prompt先保存，再由专门绘图agent调用imagegen生成及编辑；图3的输入、中间表、结果与回退箭头均与实例核对。生成记录及两版prompt随仓库保存。
- `git diff --check`：通过。
- 分发PDF：[output/survey.pdf](../output/survey.pdf)。图片约235 ppi（166 mm宽）；未指定投稿期刊，当前使用通用学术排版。

以上检查针对稿件、引用、筛选台账、算术实例与排版，没有重新运行原论文模型或实验。论文访问、版本及能力核验边界见[SOURCES.md](SOURCES.md)与[EVIDENCE.md](EVIDENCE.md)。
