# 使用 TeX Live 自带中文字体，不需要上传任何字体文件。
# 默认 pdfLaTeX 配置下也将实际调用 XeLaTeX；建议 Overleaf 中明确选择 XeLaTeX。
$pdf_mode = 5;
$xelatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';
$pdflatex = 'xelatex -interaction=nonstopmode -file-line-error %O %S';
$max_repeat = 5;
$bibtex_use = 2;
