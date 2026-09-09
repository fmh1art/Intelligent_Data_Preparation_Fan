# 交付检查

检查日期：2026-09-09。本记录对应最新图表精简版本：18页、48项参考文献、1图4表。

- 编译：`latexmk -xelatex -interaction=nonstopmode -halt-on-error -outdir=build main.tex`通过；XeLaTeX与Biber完成引用解析。
- 正文检查：`python scripts/check_manuscript.py`通过，48个文献键全部使用，无重复DOI、缺失引用或标签错误；1幅图、4张表的引用完整，图片与prompt存在。
- 检索与证据：`python scripts/check_review_evidence.py`通过；复核固定查询120条记录、117项独立工作、34项复筛、10项查询纳入和4项补充，检查48项文献覆盖映射及结果差值、费用换算。
- 算术实例：`python scripts/reproduce_example.py`通过。SQLite直接连接与先聚合再连接分别得到250和150；退款10改为15后分别为245和145，订单键唯一性与独立总额恒等式成立。此检查仅针对作者构造实例。
- 主题与公式：出版源文件不包含具身智能、机器人或Open X-Embodiment内容。原概括性目标公式及引用已删除；退款算术与Hit@k实现口径继续保留。历史核查记录中的编号更新为当前图1、表4。
- 图表精简：删除两幅概念图；筛选、任务定义、组件比较及评测要求改为正文，能力矩阵与流程机制合并。四张保留表格以短语及数字呈现，实验条件、数据来源、停止条件和局限移入正文。详见[删改映射](SIMPLIFICATION.md)。
- 编译日志：无未定义引用、缺失字符、overfull/underfull或重跑Biber提示；现有TeX Live的fontspec仍给出FandolSong与FandolFang的2项CJK Script元数据提示，已查看渲染页，未见缺字或方框。
- PDF检查：18页均含有效文字，未发现越出页面边界的文字块；图1在第10页，表1—4依次位于第3、9、12、13页。标题摘要、四张表、实例图和参考文献末页已渲染检查，未见裁切或图文重叠。
- 图片检查：仅保留1张RGB、1536×1024 PNG，可解码；它与上一轮原图3字节一致，SHA-256为`f8aaa212554658bbc7659e68e0168df19e32d315ecf8cb91b1b07777e74678d6`。本轮只重命名，未生成新图或修改像素。
- 文档与链接：同步更新README、PNG预览、生成与核查记录、审稿回复和公式审计中的编号；本地Markdown链接检查通过。删除图像及旧prompt在Git历史可查。
- 交付：`output/survey.pdf`与本次`build/main.pdf`逐字节一致；`git diff --check`及暂存区空白检查通过。

当前只有[1张配图](../figures/README.md)需要手工重绘。[新版PDF](../output/survey.pdf)与源文件一并提交。本轮检查不等同于重新运行原论文模型或实验；论文版本及能力核验边界见[SOURCES.md](SOURCES.md)与[EVIDENCE.md](EVIDENCE.md)。
