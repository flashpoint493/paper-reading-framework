# 快速发布指南

## 当前状态
- ✅ Python 包已构建并通过检查
- ✅ GitHub 远程仓库已配置
- ⚠️ GitHub 仓库需要先创建
- ⚠️ PyPI 需要 API token

## 发布步骤

### 1. 创建 GitHub 仓库

**方法 1：网页创建（推荐）**
1. 访问：https://github.com/new
2. 仓库名：`paper-reading-framework`
3. 描述：`使用 Moonshot AI (Kimi) 进行论文的精度阅读、内化和落地的完整框架`
4. 选择：**Public**
5. **重要**：不要勾选任何初始化选项（README、.gitignore、LICENSE）
6. 点击 "Create repository"

**方法 2：使用 GitHub CLI（如果已安装）**
```bash
gh repo create paper-reading-framework --public --source=. --remote=origin --push
```

### 2. 推送到 GitHub

创建仓库后，运行：
```powershell
git push -u origin main
```

### 3. 发布到 PyPI

**获取 API Token：**
1. 访问：https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. 命名：`paper-reading-framework`
4. 作用域：整个账户
5. 复制 token（格式：`pypi-xxx`）

**发布：**
```powershell
twine upload dist/*
# 用户名：__token__
# 密码：pypi-xxx（您的 token）
```

## 一键命令

创建 GitHub 仓库后，运行：
```powershell
# 推送 GitHub
git push -u origin main

# 发布 PyPI（需要先获取 token）
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi-xxx"  # 替换为您的 token
twine upload dist/*
```
