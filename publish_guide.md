# 发布指南

## GitHub 发布步骤

### 1. 在 GitHub 创建新仓库

1. 访问 https://github.com/new
2. 仓库名称：`paper-reading-framework`（或您喜欢的名称）
3. 描述：`使用 Moonshot AI (Kimi) 进行论文的精度阅读、内化和落地的完整框架`
4. 选择 Public 或 Private
5. **不要**初始化 README、.gitignore 或 LICENSE（我们已经有了）
6. 点击 "Create repository"

### 2. 连接本地仓库并推送

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为您的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/paper-reading-framework.git

# 或者使用 SSH（如果您配置了 SSH key）
# git remote add origin git@github.com:YOUR_USERNAME/paper-reading-framework.git

# 推送代码
git branch -M main
git push -u origin main
```

### 3. 更新 setup.py 中的 URL

在推送后，更新 `setup.py` 中的 URL 为实际的 GitHub 仓库地址。

## PyPI 发布步骤

### 1. 安装发布工具

```bash
pip install build twine
```

### 2. 更新版本号

在 `setup.py` 中更新版本号（例如从 0.1.0 到 0.1.1）

### 3. 构建包

```bash
# 清理旧的构建文件
rm -rf build dist *.egg-info

# 构建源码包和 wheel 包
python -m build
```

### 4. 检查包

```bash
# 检查包是否有问题
twine check dist/*
```

### 5. 测试上传到 TestPyPI（可选但推荐）

```bash
# 注册 TestPyPI 账号：https://test.pypi.org/
# 创建 API token：https://test.pypi.org/manage/account/token/

# 上传到 TestPyPI
twine upload --repository testpypi dist/*

# 测试安装
pip install -i https://test.pypi.org/simple/ paper-reading-framework
```

### 6. 发布到 PyPI

```bash
# 注册 PyPI 账号：https://pypi.org/
# 创建 API token：https://pypi.org/manage/account/token/
# 注意：API token 格式为 pypi-xxx，不是密码

# 上传到 PyPI
twine upload dist/*
```

### 7. 验证安装

```bash
pip install paper-reading-framework
```

## 后续更新

每次发布新版本时：

1. 更新 `setup.py` 中的版本号
2. 更新 `CHANGELOG.md`（如果存在）
3. 提交更改：`git commit -m "chore: bump version to X.Y.Z"`
4. 创建 git tag：`git tag vX.Y.Z`
5. 推送代码和标签：`git push && git push --tags`
6. 构建并上传到 PyPI

## 注意事项

- PyPI 不允许删除已发布的版本，只能发布新版本
- 版本号遵循语义化版本（Semantic Versioning）
- 确保所有敏感信息（API keys）都在 `.gitignore` 中
- 确保 `config.yaml.example` 不包含真实 API key
