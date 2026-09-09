# 图2重绘提示词（v2）

执行方式：内置 imagegen，全新生成；原图只作语义核对，不继承旧构图。

Use case: infographic-diagram
Asset type: high-quality Chinese academic survey figure, standalone PNG, landscape 3:2, request native 3072×2048 or the highest native resolution available.
Create a completely NEW, refined scientific information graphic explaining task-aware data preparation with execution, independent verification, and feedback. This is an author's conceptual synthesis, not a commercial app or a named system. A white background, deep ink-blue text, precise delicate connectors, blue #2865A8 and teal #138B84, muted purple #7764A5 for saved states, amber #D69535 for corrective feedback. Very pale panel fills, generous whitespace, compact accurate Chinese text, consistent clean sans-serif. Strong visual hierarchy through position, small icons and structured mini diagrams; no thick title bars, no dark filled headers, no heavy outlines, no clip-art people, no gradients, no shadows, no huge chart title, no figure number.

COMPOSITION AND ARROW TOPOLOGY ARE ESSENTIAL:
Use four equal main modules across the center, left to right:
“流程规划” → “程序生成” → “工具执行” → “独立验证”.
Exactly three short solid right-pointing arrows connect their centers. Main modules occupy about y=32% to 68% of the canvas, with ample gutters.
Above module 1 a small pale panel “任务与约束” points DOWN only to planning. Above module 3 a small panel “原始数据” points DOWN only to execution. Above module 4 a small panel “验证依据” points DOWN only to independent verification.
Below module 3 a small purple panel “中间状态” receives a DOWN arrow from execution, labeled “保存”.
Below module 4 a teal panel “数据 · 流程 · 记录” receives a DOWN arrow from verification, labeled “通过”.
Below module 2 a small panel “人工澄清” has a dark-blue DASHED two-way connector to the lower edge of planning, labeled “语义歧义”. Use a short elbow within the left lower interior region. It must not intersect other connectors.
Draw ONE long solid amber feedback path from the RIGHT edge of verification, going right to a dedicated margin corridor, DOWN outside the output panel, LEFT along a clear bottom corridor, then UP the outer left margin, then RIGHT with its single terminal arrowhead entering the LEFT edge of planning. The path must be fully continuous, its origin unambiguous, no arrowhead at origin, and no intersection with any panel or other connector. Label its right downward section “失败反馈” and its bottom horizontal section “定位状态 · 回退修订”. These labels must not cross its line. Reserve 3–4% white outer margins.
The bottom corridor must remain outside all panels and outside the human clarification connector.
Near the bottom center, above the return path in spare whitespace, add the short statement “执行成功 ≠ 任务正确”.

DETAILED CONTENT, USE THIS EXACT SHORT CHINESE TEXT, NO EXTRA PARAGRAPHS:
Task input panel: header “任务与约束”; an abstract document with two aligned check rows and small text “目标模式” “业务口径”.
Raw input panel: header “原始数据”; TWO crisp miniature related tables, with blue/teal highlighted key columns joined by a tiny thin visual association; short text “多源表格”.
Evidence panel: header “验证依据”; three small distinct line glyphs: key/column constraints, reference table, checklist; their labels “结构约束” “参考数据” “任务判定”.
Planning module:
small step numeral “01”, large title “流程规划”, one short subline “候选操作与顺序”.
Rich, precise miniature DAG of alternative candidate workflows. A tiny start node branches to TWO candidates, with branches labeled “聚合” and “过滤”, both then joining a “连接” node and a final “候选流程” capsule. The tiny arrows need valid directions from start down to branch operations then down to join then down to candidate. Distinguish the selected branch in blue and an alternative in pale grey, not green success marks. These are candidate operations, not claims about fixed mandatory order.
Generation module:
small step numeral “02”, large title “程序生成”, subline “算子与参数”.
Show an elegant code document rectangle with three separated monospace token rows exactly “groupby(…)”, “join(…)”, “select(…)”. Beneath it show a small serial sequence of three blue numbered operator chips “1” “2” “3”, connected by thin arrows. Add short text “可执行程序”. No long source code, no bogus technical diagrams.
Execution module:
small step numeral “03”, large title “工具执行”, subline “确定性操作”.
Show a tiny precise table with columns “id” “value” and rows “a” “12”, “b” “8”; it is a generic illustration, not an experimental result. One thin arrow connects a two-column input table glyph to this result table; a small restrained gear attached to the arrow indicates an execution engine. Under the table show two tiny state chips “S₀” and “S₁” connected rightward, plus short text “物化表与日志”. Do not invent further data.
Verification module:
small step numeral “04”, large title “独立验证”, subline “依据与结果对照”.
Show a reference table and a result table as two neatly aligned miniature grids, with one small highlighted matched column and a careful comparison/check line between them. Below use three short check rows exactly “结构一致”, “统计合理”, “任务满足”. Icon checkmarks should be outlined, not large trophy/approval symbols. No shield, no large magnifying glass or decorative clip art.
Saved-state panel: header “中间状态”, three thin stacked table outlines, short text “表 · 参数 · 日志”.
Clarification panel: header “人工澄清”, a small clean two-speech-bubble line glyph; short text “补充任务语义”. No person silhouette.
Output panel: header “数据 · 流程 · 记录”, three small equal semantic glyphs: a table, a miniature DAG, a lined document; do not add further labels.

QUALITY:
Make the graphic more visually engaging through the meaningful miniature tables, candidate DAG, code tokens, execution state chips, and checking correspondences. All typography sharp, readable at 1536px-wide display; allow room for Chinese characters; do not cram long prose. Use hand-designed journal illustration discipline, optical alignment, consistent line weight, clear arrowheads at actual destinations. Main workflow, external evidence input, saved states, success output, failure loop, and human clarification are seven distinguishable relationships. Do not add undocumented arrows between modules, do not connect clarification to program generation merely because it sits below it, do not route the feedback over a main module or output.
