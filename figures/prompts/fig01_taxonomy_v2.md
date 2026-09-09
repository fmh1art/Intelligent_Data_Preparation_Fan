# 图1：智能数据准备任务体系，第二版生成提示词

执行方式：专门绘图 agent，内置 image_gen.imagegen；全新构图，旧图仅作内容核对。用途为中文学术综述中的独立 PNG。

## 完整生成 prompt

Use case: infographic-diagram; scientific academic infographic for a Chinese-language survey article. Produce a new, substantially redesigned information-rich figure, not a recoloring of an old image. Deliver a landscape 3:2 PNG at 3072×2048 or the highest native resolution available. All labels must remain clear in a 1536-pixel-wide preview. Do not render a figure number or large overall title.

Style: precision editorial scientific diagram on pure white. Ink navy text, medium blue #2865A8 and teal #138B84 primary colors, restrained lavender #7764A5 for semantics, muted amber #D69535 for repair. Very light blue/teal fills only where helpful. Thin consistent crisp lines, plenty of white space, immaculate alignment, large Chinese sans-serif type. Small real data diagrams and structured relational tables create visual richness, not generic office icons. No shadows, gradients, 3D, thick frames, dark full-width title bands, mock user interfaces, robot icons, decorative particles, or repeated chunky rounded cards. Each visual element has a semantic purpose.

Composition: a narrow INPUT column at left (about 17% width), a broad shared TASK WORKSPACE in the middle (about 64%), and a narrow OUTPUT column at right (about 15%), with comfortable gutters. Across the entire bottom, a lightweight shared mechanism rail and a separate tiny assessment rail. The central workspace has a short centered header “六类任务 · 按需组合”. Under it, six different mini scientific schematics on a spacious 3-column by 2-row grid. Use subtle short divider lines between neighboring diagrams, not six enclosed cards. THE SIX TASKS ARE PARALLEL AND COMPOSABLE, NEVER A SIX-STEP SEQUENCE. Never draw arrows from one task panel to another. Arrowheads inside each small before/after example are allowed. Use one thin bracket collecting the six diagrams, fed by the input column and pointing once to the output column. This says the complete task set can be composed, not that every task must run.

LEFT INPUT: two vertically separated entries. First label exactly “数据与元数据”, with a miniature stack of three distinct blue tables, a tiny document schema and small connected-field nodes; below use ONLY the short secondary text “表 · 文本 · 模式”. Second label exactly “任务与约束”, with a compact task specification sheet including a target field outline and two small checkboxes, plus a modest constraint bracket; below ONLY “目标 · 规则 · 预算”. Their arrows go into the shared workspace bracket, not across a series of task nodes.

SIX TASK DIAGRAMS: each has its exact Chinese task name as a large clean heading ABOVE its miniature data graphic. The data values are short and legible. Visually discriminate the task mechanism; do not replace any data diagram with a generic icon.

Upper left “数据发现”: a cluster of five differently shaped tiny source tables, two highlighted in blue, with a thin magnifying lens enclosing one table and a compact ranked output of two selected table thumbnails. Short secondary label “候选数据源”. This is selecting table sources, not copying rows or merging them.

Upper middle “语义理解”: a 3-column little table with readable headers “字段”, “值”, “类型”. Two example rows “city”, “北京”, “城市” and “date”, “2025”, “时间”. Curved fine lavender links attach the field/value region to type labels “城市” and “时间”. This illustrates assigning semantic types to columns, with no record-identity matching. Short secondary label “类型与字段映射”.

Upper right “清洗修复”: a tiny two-column table with headers “记录”, “值”, rows “r1”, “12” and “r2”, “?”. Highlight the missing “?” in restrained amber, then a thin arrow to a matching table with “r1”, “12” and “r2”, “15*”. A small amber asterisk on the estimated value is important. Short secondary label exactly “检测与修复 · 保留依据”. Do not imply an estimated value is verified truth. Do not invent any numerical performance claims.

Lower left “匹配融合”: two compact record strips from different sources, labeled “来源 A” and “来源 B”, containing respectively “e1 / 北京” and “e9 / Beijing”. Two precise matching lines converge to a small unified entity circle containing “E”, with two retained source dots attached. Short secondary label “统一实体 · 保留来源”. This is record identity and source-aware fusion, not schema alignment.

Lower middle “结构转换”: show a visually exact wide-to-long table transformation, with left wide-table headers “id”, “A”, “B” and ONE row “x”, “1”, “2”; thin arrow to right long-table headers “id”, “项”, “值” and TWO rows “x”, “A”, “1” and “x”, “B”, “2”. Both numbers and repeated identifier are exact. Short secondary label “重塑与程序生成”. This expresses structural transformation of known values, no semantic guessing.

Lower right “标注增强”: three short document strips with sample ids “s1”, “s2”, “s3”, flowing to a small selection gate and two crisp tag chips, “+” blue and “−” teal; retained selected documents have the corresponding attached tag chip. Short secondary label “标签与训练子集”. No robot, graduation cap, or people.

RIGHT OUTPUT: a slim vertically aligned stack of three artifacts, with exact labels “目标数据”, “可执行流程”, “验证记录”. Each artifact has a distinct meaningful miniature drawing: a clean small table with highlighted header, a tiny branching executable operator graph with three nodes and edges, and a short audit sheet with two check marks and one link marker. These are three parallel outputs connected to one shared collector, NOT successive pipeline stages. Give their labels enough width to avoid awkward character breaks.

BOTTOM MECHANISM RAIL: under the task workspace, a delicate horizontal connecting bracket and the short label “支撑机制”. Four evenly spaced items, exact text “规则约束”, “统计学习”, “语言模型”, “流程规划”. Pair with tiny purpose-specific symbols, respectively a constraint bracket over two equal fields, a few data points and fitted line, a compact text-token lattice, a branching search tree. Use fine outline drawings, not gears or generic computers. Mechanisms support all six tasks; no one-to-one mapping of four mechanisms to six tasks.

BOTTOM ASSESSMENT RAIL: below the mechanisms, use three evenly spaced small text items, exactly “质量评估”, “成本控制”, “数据溯源”, separated by ample spaces and small centered dots. Pair with very small check/clock/linked-node marks if room allows. No numerical charts or accuracy values.

Constraints: Exact six task names, four mechanism names, three output names, and three assessment names must be present and correctly written. Readable professional Chinese, short secondary text, no invented paragraph captions. The wide/long example must contain exactly the specified values; missing-value repair must retain “15*” to mark estimation. Make the diagrams visibly more informative and refined than a box-and-icon overview. Keep safe margins of at least 3% on all sides. No watermark. Do not draw embodied intelligence, robotics, sensory hardware, or control loops.
