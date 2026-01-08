# 发布指南

## 📦 包已构建完成

Python 包已成功构建并通过检查：
- ✅ `dist/paper_reading_framework-0.1.0-py3-none-any.whl` (wheel 包)
- ✅ `dist/paper_reading_framework-0.1.0.tar.gz` (源码包)

## 🚀 GitHub 发布

### 方法 1: 使用脚本（推荐）

```powershell
# 运行 GitHub 发布脚本
.\publish_to_github.ps1
```

### 方法 2: 手动操作

1. **在 GitHub 创建新仓库**
   - 访问 https://github.com/new
   - 仓库名：`paper-reading-framework`
   - 描述：`使用 Moonshot AI (Kimi) 进行论文的精度阅读、内化和落地的完整框架`
   - 选择 Public
   - **不要**初始化 README、.gitignore 或 LICENSE

2. **连接并推送代码**

```powershell
# 添加远程仓库
git remote add origin https://github.com/ocarina1024/paper-reading-framework.git

# 重命名分支为 main（如果需要）
git branch -M main

# 推送代码
git push -u origin main
```

## 📤 PyPI 发布

### 准备工作

1. **注册 PyPI 账号**
   - 访问 https://pypi.org/account/register/
   - 完成注册和邮箱验证

2. **创建 API Token**
   - 访问 https://pypi.org/manage/account/token/
   - 点击 "Add API token"
   - 命名：`paper-reading-framework`
   - 作用域：整个账户
   - **重要**：复制 token（格式：`pypi-xxx`），只显示一次

### 方法 1: 使用脚本（推荐）

```powershell
# 运行 PyPI 发布脚本（会构建包）
.\publish_to_pypi.ps1

# 然后手动上传（需要输入 token）
twine upload dist/*
```

### 方法 2: 手动操作

```powershell
# 1. 安装/更新工具
python -m pip install --upgrade build twine

# 2. 清理旧构建（如果存在）
Remove-Item -Recurse -Force build, dist, *.egg-info -ErrorAction SilentlyContinue

# 3. 构建包
python -m build

# 4. 检查包
twine check dist/*

# 5. 测试上传到 TestPyPI（推荐先测试）
twine upload --repository testpypi dist/*
# 输入用户名：__token__
# 输入密码：pypi-xxx（您的 token）

# 6. 发布到 PyPI
twine upload dist/*
# 输入用户名：__token__
# 输入密码：pypi-xxx（您的 token）
```

### 验证安装

发布后，验证包是否可以安装：

```bash
pip install paper-reading-framework
```

## 🔄 后续更新流程

每次发布新版本时：

1. **更新版本号**
   ```python
   # 在 setup.py 中
   version="0.1.1"  # 从 0.1.0 更新
   ```

2. **提交更改**
   ```powershell
   git add setup.py
   git commit -m "chore: bump version to 0.1.1"
   git tag v0.1.1
   git push && git push --tags
   ```

3. **重新构建和发布**
   ```powershell
   .\publish_to_pypi.ps1
   twine upload dist/*
   ```

## 📝 注意事项

- ✅ PyPI 不允许删除已发布的版本，只能发布新版本
- ✅ 版本号遵循语义化版本（Semantic Versioning）
- ✅ 确保所有敏感信息（API keys）都在 `.gitignore` 中
- ✅ 确保 `config.yaml.example` 不包含真实 API key
- ✅ 包名 `paper-reading-framework` 在 PyPI 上必须唯一

## 🔗 相关链接

- GitHub: https://github.com/ocarina1024/paper-reading-framework
- PyPI: https://pypi.org/project/paper-reading-framework/
- 文档: https://github.com/ocarina1024/paper-reading-framework#readme

## 🆘 遇到问题？

- **PyPI 上传失败**：检查 token 是否正确，网络是否正常
- **包名已存在**：需要修改 `setup.py` 中的 `name` 字段
- **版本冲突**：确保版本号递增且唯一
