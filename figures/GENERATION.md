# 学术综述配图生成记录

当前稿件只保留“错误传播与回退”实例图。该图来自上一轮LLM重绘，原为图3，现为图1。本轮仅重命名文件并更新引用，没有重新生成、编辑像素或插值放大。

## 当前文件与规格

- 正式文件：[fig01_error_propagation.png](fig01_error_propagation.png)。
- 生成前保存的实际规格：[详细prompt](prompts/fig01_error_propagation.md)；[逐项核查](reviews/fig01_error_propagation.md)。
- 生成日期：2026-09-09；执行者：专门学术绘图agent；实际工具：内置image_gen.imagegen，1次生成，0次编辑。
- 实际规格：PNG、RGB、1536×1024像素。Prompt请求3072×2048或最高原生尺寸，但工具实际返回1536×1024；166 mm排印宽度约为235 ppi。
- 原始输出：`/home/fanmeihao/.codex/generated_images/01a0847d-831d-7f12-a0fd-699f1b428217/exec-9a7be220-2359-4a9a-8f5d-40423458122d.png`。仓库正式文件按字节复制，论文不依赖该本机路径。
- SHA-256：`f8aaa212554658bbc7659e68e0168df19e32d315ecf8cb91b1b07777e74678d6`。

## 表达与核查

顶部为订单、退款两张共享源表；左侧展示先连接造成订单金额重复计入，右侧展示先聚合退款再连接；底部给出订单粒度及总额检查，并沿左外侧回退到源表状态。两张中间表均保留订单、客户、金额和退款，错误路径高亮两个100，修订路径突出聚合后的30。250、150及计算式与正文和SQLite实例一致。

白底、深蓝文字、蓝绿图形和少量强调色构成主要视觉样式。图形为栅格对象，文字、箭头和表格不能单独编辑；[独立PNG](README.md)供查看与手工重绘参照。视觉与算术核查不等同于原论文实验复现。

## 已移除内容与历史

任务体系和通用执行反馈两张概念图，与正文分类及机制分析重复，已按最新要求移除。当前目录仅保存保留图的PNG、实际prompt和核查记录。

三图及各轮prompt、编辑与核查记录可从[精简前提交3997142](https://github.com/fmh1art/Intelligent_Data_Preparation_Fan/tree/39971428f52cfe4d729c3f3021fad53a9833d44b/figures)查看；第一版可从[重绘前提交72020f4](https://github.com/fmh1art/Intelligent_Data_Preparation_Fan/tree/72020f4577c3be77efdad588bf7cc18016e148c7/figures)查看。
