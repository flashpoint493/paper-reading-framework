# 发布脚本

此目录包含用于发布到 GitHub 和 PyPI 的脚本。

## 脚本说明

- `publish_now.ps1` - 一键发布脚本（GitHub + PyPI）
- `publish_to_github.ps1` - GitHub 发布脚本
- `publish_to_pypi.ps1` - PyPI 发布脚本

## 使用方法

### PowerShell

```powershell
# 一键发布（GitHub + PyPI）
.\scripts\publish_now.ps1

# 单独发布 GitHub
.\scripts\publish_to_github.ps1

# 单独发布 PyPI
.\scripts\publish_to_pypi.ps1
```

### 脚本说明

- **publish_now.ps1**: 一键发布脚本，自动处理 GitHub 和 PyPI 发布流程
- **publish_to_github.ps1**: 仅发布到 GitHub，需要先创建仓库
- **publish_to_pypi.ps1**: 仅发布到 PyPI，需要 API token

## 注意事项

- 发布到 GitHub 需要先创建仓库
- 发布到 PyPI 需要 API token
- 详细说明请查看根目录的 `PUBLISHING.md`
