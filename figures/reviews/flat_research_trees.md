# 平面分枝研究图：生成与审校

历史记录：下文针对此前生成的两张PNG。当前论文已改用作者提供的`ai4dp.pdf`和`dp4ai.pdf`，来源及检查范围见[当前PDF记录](author_research_maps.json)。

日期：2026-09-11。将此前的装饰性双树图改为两张独立的横向分枝图，参考用户提供的平面曲线、圆点末端、分类标题和短标签样式。当前稿件的图1、图2分别位于PDF第2、3页；原有统计图顺延为图3、图4，位于第4、6页。

## 分类与年代

每张图有六条独立主枝，论文标签由短枝连接至所属主枝；同一枝内较新的论文在上方。各枝的高度不代表统一时间尺度，虚线只是背景辅助线。

| 图 | 分支 | 节点数 |
|---|---|---:|
| AI for Data Prep | Discovery & semantics | 4 |
| AI for Data Prep | Query & transformation | 5 |
| AI for Data Prep | Integration & matching | 4 |
| AI for Data Prep | Cleaning & repair | 5 |
| AI for Data Prep | Pipelines & evaluation | 5 |
| AI for Data Prep | Foundations & surveys | 6 |
| Data Prep for AI | Pretraining curation | 4 |
| Data Prep for AI | Selection & synthesis | 4 |
| Data Prep for AI | Inference context | 2 |
| Data Prep for AI | Processing systems | 2 |
| Data Prep for AI | Embodied data | 6 |
| Data Prep for AI | Surveys & perspectives | 2 |

第一张图灰色分支中的数据质量与治理文献为两个方向的共同基础，图注明确这一含义。共49个节点对应50项引用，[44,45]为同一数据资源。RoboMIND 2.0仅显示书目主年份2025；六处星号表示预印本，版本链接仍保留在书目中。论文标签不包含核读过程说明。

## 生成

使用imagegen技能及内置image_gen.imagegen，以用户提供的image.png为风格参考，各生成一次后采用。未使用CLI、子代理或代码绘图，没有后期叠字、修改像素或插值放大。最终PNG从工具输出逐字节复制。

- [图1](../fig01_ai_for_data_prep_flat.png)与[精细PROMPT](../prompts/fig01_ai_for_data_prep_flat.md)
- [图2](../fig02_data_prep_for_ai_flat.png)与[精细PROMPT](../prompts/fig02_data_prep_for_ai_flat.md)
- [生成来源、尺寸及SHA-256](flat_research_trees.json)
- [书目分类清单](../two_research_trees_manifest.json)

风格参考的论文标签、页码和标识没有复用，也未嵌入投稿PDF。参考图仅用于生成，不是LaTeX编译依赖。

## 核验

逐项目视检查49个标签、12个分类标题、六处预印本标记和所有标签到主枝的连接。Tesseract的PSM 6、11和12为其中35个引用编号提供位置佐证，其余14个由目视核对。所有论文的简称、年份和引用编号均另行逐项检查。

审校记录保存各枝的独立标签区域和节点边界，中心位置核读误差为正负3像素；这些是实际图像的位置记录，并非绘图坐标。自动检查确认每个节点位于其指定分支范围内，各枝标签区域不重叠，枝内跨年份倒置为0。记录以图像SHA-256绑定，见[审校JSON](flat_research_trees_audit.json)。

两图均为1774×887像素、不透明RGB。横向页面中显示宽度约253毫米，约178 ppi；未宣称为300 dpi印刷图。PDF中的图像与源PNG逐像素一致，各自仅出现一次。已检查两页图形及中文图注的显示，主体章节、原有统计图、书目和作者信息继续通过常规编译检查。

此前[v4](../fig00_two_research_trees_v4.png)及其[审校记录](fig00_two_research_trees.md)保留作为历史版本，当前稿件不再引用。
