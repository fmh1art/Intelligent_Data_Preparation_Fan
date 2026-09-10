# 双树总览图：分类分支与年代审校

当前采用[v4](../fig00_two_research_trees_v4.png)，置于《数据准备与语言模型的交叉前沿》引言后的第2页。正文、图注及读图说明为中文，图内标签为英文。

## 分支结构

蓝色左树对应AI for Data Prep，绿色右树对应Data Prep for AI，铜色突出具身数据准备。每棵树保留五个任务分支和一个综述分支。每个分支以有标题、有明确边界的独立区域汇集同一子方向的论文，各区域从所属树干独立分出。共享的数据质量与治理基础集中在灰色根部区域。

| 方向 | 分支 | 节点数 | 枝内年份范围 |
|---|---|---:|---|
| AI for Data Prep | Discovery & semantics | 4 | 2018—2023 |
| AI for Data Prep | Query & transformation | 5 | 2011—2023 |
| AI for Data Prep | Integration & matching | 4 | 2020—2024 |
| AI for Data Prep | Cleaning & repair | 5 | 2017—2024 |
| AI for Data Prep | Pipelines & evaluation | 5 | 2023—2026 |
| AI for Data Prep | Surveys & perspectives | 2 | 2023—2026 |
| Data Prep for AI | Pretraining curation | 4 | 2023—2025 |
| Data Prep for AI | Selection & synthesis | 4 | 2023—2025 |
| Data Prep for AI | Inference context | 2 | 2020—2022 |
| Data Prep for AI | Processing systems | 2 | 2024—2025 |
| Data Prep for AI | Embodied data | 6 | 2023—2026 |
| Data Prep for AI | Surveys & perspectives | 2 | 2023—2026 |
| 共同基础 | Shared foundations & quality | 4 | 2009—2025 |

每个分支内部按书目年份自下向上排列，较新的工作较高。不同分支区域之间不共用时间轴；根部表示共同概念基础，其位置不意味着所有基础文献均早于上方方法。时间间距不按比例。分支归属按本文主要论述位置确定，连线不表示直接技术继承、引用或因果关系。

49个节点覆盖当前全部50项引用。AgiBot World 2026的数据卡与发布说明合并为[44,45]。RoboMIND 2.0按首次提交的2025年在具身分支内排序，2026年核读修订作为标签补充。完整书目映射见[节点清单](../two_research_trees_manifest.json)。

## 生成记录

使用imagegen技能及内置image_gen.imagegen，以v3为蓝绿双树风格参考，按[精细PROMPT](../prompts/fig00_two_research_trees_taxonomy.md)重构分类区域，一次生成采用。未调用CLI或子代理，未使用代码叠字、改图、合成或插值放大；最终PNG从工具输出逐字节复制。

工具输出路径、实际尺寸与SHA-256见[生成记录](fig00_two_research_trees.json)。[v3](../fig00_two_research_trees_v3.png)、[v2](../fig00_two_research_trees_v2.png)与[初稿](../fig00_two_research_trees.png)作为历史版本保留。v3按全局年份分层时，不同子方向的论文沿连续树枝混排，分类不够清楚；v4以明确的分类分支为主要结构，在每个分支内保留年代递进。

## 检查方法与结果

逐项目视核对49个论文标签、50个引用编号、六处预印本标记、13个分支标题以及区域与树干的连接。每个分支只包含该子方向的论文，没有跨分类的论文连接。实际图像中的区域边界和全部标签边界均记录于[分类与年代审校JSON](fig00_two_research_trees_taxonomy.json)。

Tesseract的PSM 6、11和12为40个编号提供位置佐证；其余8个未识别编号及1个将[38]误读为[3]的位置由目视核对。所有文字和分类归属均另行目视检查，OCR结果不作为独立准确性保证。标签中心由目视边界计算，核读误差按正负3像素记录。

自动检查将审校记录用SHA-256绑定最终PNG，并与书目关联清单对照：每个节点恰好落入其指定分支，分支区域及枝内标签互不重叠，计入坐标误差后枝内跨年份倒置为0。检查对象为枝内年代次序，旧版全局年代审校仅对应v3。PDF内嵌图像与PNG逐像素一致，两幅原稿统计图和作者照片均保留。

最终PNG为不透明RGB图，原生分辨率1086×1448像素，论文显示约163×218毫米，约169 ppi。已目视检查最终PDF第2页：分类标题、论文标签及中文图注显示完整。图形区域大小不用于衡量研究规模或论文影响力。
