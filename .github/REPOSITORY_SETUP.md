# GitHub 仓库设置指南

## 仓库描述

在仓库设置中添加以下描述：

```
使用 Moonshot AI (Kimi) 进行论文的精度阅读、内化和落地的完整框架。支持 arXiv 论文下载、AI 深度分析、知识图谱生成和代码框架自动生成。
```

## 网站（可选）

如果设置了 GitHub Pages，可以添加网站 URL。

## 主题（Topics）

参考 [TOPICS.md](TOPICS.md) 添加相关标签。

## 社交媒体预览图（可选）

可以添加一个 `og-image.png` 到仓库根目录，用于社交媒体分享时的预览图。

## 仓库可见性

当前设置为 Public，适合开源项目。

## 功能设置

### 建议启用的功能

- ✅ Issues - 用于问题跟踪和功能请求
- ✅ Discussions - 用于社区讨论
- ✅ Wiki - 可选，用于详细文档
- ✅ Projects - 可选，用于项目管理

### 建议禁用的功能

- ❌ Security - 如果不需要安全策略
- ❌ Insights - 根据需求决定

## 分支保护规则（可选）

如果需要保护 main 分支，可以设置：

1. 访问 Settings > Branches
2. 添加规则：`main`
3. 启用：
   - Require pull request reviews
   - Require status checks to pass
   - Require conversation resolution before merging
