# 测试脚本

此目录包含各种测试脚本。

## 测试脚本列表

- `test_api.py` - 测试 Moonshot AI API 连接
- `test_arm_paper.py` - 测试 arXiv 论文下载
- `test_pdf_parse.py` - 测试 PDF 解析功能

## 使用方法

```bash
# 测试 API 连接
python tests/test_api.py

# 测试 arXiv 下载
python tests/test_arm_paper.py

# 测试 PDF 解析
python tests/test_pdf_parse.py
```

## 注意事项

- 运行 `test_api.py` 需要配置 Moonshot API Key
- 运行 `test_arm_paper.py` 需要网络连接
- 运行 `test_pdf_parse.py` 需要有效的 PDF 文件
