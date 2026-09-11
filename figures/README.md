# 当前论文插图

## 图1、图2：两条研究主线的分枝图

直接使用作者提供的两张PDF，采用白底、六色平面主枝、圆点末端和短论文标签。每条主枝只连接一个子方向的文献，枝内按书目年份由下向上排列；不同主枝的高度不构成统一时间轴。

| 图 | 文件 | 页码 | 分支与节点 |
|---|---|---:|---|
| AI for Data Prep | [PDF](ai4dp.pdf) | 2（竖向，上） | 六条主枝，29个节点；灰色分支汇集共同基础与综述 |
| Data Prep for AI | [PDF](dp4ai.pdf) | 2（竖向，下） | 六条主枝，20个节点；橙色分支为具身数据准备 |

两图共49个节点，对应正文全部50项引用，[44,45]合并为同一资源节点。源文件分别为616×349和616×350 pt，在同一竖向页面按版心宽度等比上下排列，不栅格化、不修改原文件。RoboMIND 2.0标签保留书目年份2025及预印本标记，版本链接保留在书目中。

- [当前PDF的哈希与来源记录](reviews/author_research_maps.json)
- [文献分类清单](two_research_trees_manifest.json)
- [编译与内容检查](../editorial/frontier_sources/validation.json)

检查确认两个PDF的论文年份、引用编号与节点清单一致，并确认编译稿保留文字和矢量路径。源图`dp4ai.pdf`中RoboMIND 2.0/DROID标签边框与文字有重叠，另有“Model collaps”拼写；插入时均保留原样，未改动源图。此记录不进入论文正文或图注。

此前生成的[AI for Data Prep PNG](fig01_ai_for_data_prep_flat.png)、[Data Prep for AI PNG](fig02_data_prep_for_ai_flat.png)、[提示词及审校说明](reviews/flat_research_trees.md)，以及更早的[双树v4](fig00_two_research_trees_v4.png)均作为历史版本保留，当前论文只引用以上两个PDF。

## 图3、图4：上传文档的两幅统计图

本轮全部复用用户上传DOCX中的两幅原生统计图，不需要重新绘制。矢量PDF由原图直接渲染、裁去页边空白后嵌入LaTeX，PNG供独立预览或插入演示文稿。

| 原图 | 独立PDF | PNG预览 |
|---|---|---|
| 图1：基于语言模型的数据准备研究分布 | [PDF](original/original_lm4dp.pdf) | [PNG](original/original_lm4dp.png) |
| 图2：面向语言模型的数据准备研究分布 | [PDF](original/original_dp4lm.pdf) | [PNG](original/original_dp4lm.png) |

![原稿图1](original/original_lm4dp.png)

![原稿图2](original/original_dp4lm.png)

图1原始数据为国外学者17、6、12、16，国内学者7、13、7、11，依次对应发现、查询、融合和清洗。图2原始数据为国外学者13、4、3，国内学者3、11、8，依次对应预训练、指令微调和模型推理。这些数值均未更新，不代表2026年的完整研究分布。

LaTeX使用按原稿尺寸渲染后等比放大的矢量PDF。正文通过`main.tex`中的`articlefigure`命令引用，显示宽度为正文版心的72%。编译时直接使用随工程保存的PDF，无需重新提取或绘制。

原稿为用户本地上传的《04 数据准备与语言模型交叉技术的研究进展与发展趋势 - 编辑提问回答.docx》。提取方式为OOXML包读取及LibreOffice原生图表渲染，未调用图像生成模型。原稿、图表部件及导出文件的哈希见[provenance.json](original/provenance.json)，编译检查见[validation.json](../editorial/frontier_sources/validation.json)。本轮不修改或提交Word文件。

作者照片继续使用[fanju.jpg](fanju.jpg)与[fmh.jpg](fmh.jpg)，来源见[AUTHOR_INFO.md](../editorial/AUTHOR_INFO.md)。更早生成的三幅插图和prompt作为历史素材留存，当前稿件不引用。
