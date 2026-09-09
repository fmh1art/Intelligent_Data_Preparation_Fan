# 图3：数据准备流程中的核验与修订

本轮依据用户最新要求全新生成学术论文机制图，替换PPT演示风格。旧图与旧prompt、review已归档至 `figures/archive/overview_ppt_draft/`。以下为实际提交内置imagegen的完整prompt。

Use case: scientific-educational.
Asset type: original mechanism diagram for a Chinese academic survey article. Generate a completely new composition from this text, with no reference images. Landscape 3:2, preferably the highest native resolution supported, with a pure white background. This is a compact academic journal mechanism figure, not a presentation slide or an editorial cartoon. No overall title and no figure number.

VISUAL LANGUAGE
Use four plain rectangular nodes with thin straight black-gray borders and square corners. White node interiors. Medium-weight black or dark-gray Chinese sans-serif typography, disciplined alignment and clear whitespace. Primary labels around 32 px and short phrases around 26 px at 1536 px canvas width, without oversized display text. A single small monochrome line drawing inside each node explains its role. Connections are thin muted blue-gray lines with small conventional arrowheads. Very restrained muted teal may mark successful output, and low-saturation orange may distinguish the two feedback routes. No thick arrows, colored title bars, large colored panels, rounded cards, gradients, shadows, 3D, people, human silhouettes, cartoons, abundant icons, glowing effects, numerical values, fabricated table entries, code, formulas, logos or watermarks.

EXACT CONTENT AND MAIN FLOW
A single horizontal chain of FOUR nodes, left to right:
1. “任务说明” — one small outline document icon; two short phrases “目标” and “约束”.
2. “方案生成” — one small branching-operation line drawing; two short phrases “数据选择” and “操作组合”.
3. “工具执行” — one small thin-grid intermediate-table line drawing, without real entries; one short phrase “中间结果”.
4. “结果核验” — one small pair-of-documents comparison line drawing; two short phrases “规则检查” and “来源对照”.
The three primary solid directed arrows must connect 任务说明→方案生成→工具执行→结果核验. All four nodes have the same restrained size, with short text and one small relevant drawing in each. Do not insert another execution node.

Place a smaller plain rectangular output node in the upper-right whitespace, clearly separated from the main nodes, labeled exactly “输出数据”. A thin directed arrow labeled “通过” leaves the TOP of 结果核验 and enters this output node. Keep the output visually subordinate, with no overlapping boxes and no large report illustration.

HUMAN INVOLVEMENT AS TEXT
Beside 任务说明 put one modest small annotation “人工确认”. Beside 结果核验 put the same small annotation “人工确认”. These annotations may use a short thin leader line without an arrowhead. Do not use faces, bodies, avatars, person icons or a separate human-review module. Keep the annotations away from the feedback connections.

TWO DISTINCT FEEDBACK ROUTES
Use exactly two thin muted-orange return paths below the main chain:
- The shorter, higher return path leaves the BOTTOM-LEFT part of 结果核验, descends to its own clear horizontal channel, runs left, then points UP into the BOTTOM of 方案生成. Label it exactly “操作有误”. This path must return to 方案生成, NOT 工具执行: an erroneous operation requires revising the overall plan, then the main flow executes it again.
- The longer, lower return path leaves the BOTTOM-RIGHT part of 结果核验, descends to a separate lower channel, runs left, then points UP into the BOTTOM of 任务说明. Label it exactly “语义不明”.
These paths must have distinct starting points on the verification node. Their horizontal channels are vertically separated; the longer route descends farther right than the shorter one so the lines cannot cross. Each return path has exactly one arrowhead, at its target node. No arrows cross any label, icon, node interior or each other. Avoid floating unconnected path endpoints and avoid implying feedback originates from the human annotations.

LOWER RECORD STRIP
At the bottom draw one fine, unobtrusive horizontal bracket or line spanning the four main nodes, with the centered short text “保留来源与修改记录”. This is a record-keeping annotation, not a fifth processing stage. No filled banner or thick container.

READABILITY AND SEMANTICS
Use only the exact short Chinese labels listed above; do not invent supplementary sentences. Draw no overall heading such as 数据准备流程中的核验与修订; the surrounding article caption will supply the title. The figure explains verification and revision, not guaranteed correctness. There must be no correctness guarantee, score, percentage or fabricated data. The entire layout should be compact, carefully aligned and readily redrawn as a scholarly vector diagram.
