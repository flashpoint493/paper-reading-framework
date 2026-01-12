# Paper Reading Framework CLI 使用指南

Paper Reading Framework 提供了一个命令行工具，用于将技能安装到不同的 AI 助手中。

## 安装

通过 pip 安装后，CLI 工具会自动可用：

```bash
pip install paper-reading-framework
```

## 使用方法

### 查看可用命令

```bash
paper-reading-init --help
```

### 列出所有支持的 AI 助手

```bash
paper-reading-init list
```

支持的 AI 助手：
- `claude` - Claude Code (claude.ai/code)
- `cursor` - Cursor IDE
- `windsurf` - Windsurf IDE
- `antigravity` - Antigravity (.agent + .shared)
- `copilot` - GitHub Copilot
- `kiro` - Kiro
- `codex` - Codex (Skills)
- `gemini` - Gemini CLI

### 安装到特定 AI 助手

```bash
# 安装到 Claude Code
paper-reading-init --ai claude

# 安装到 Cursor
paper-reading-init --ai cursor

# 安装到 Windsurf
paper-reading-init --ai windsurf

# 安装到 Antigravity
paper-reading-init --ai antigravity

# 安装到 GitHub Copilot
paper-reading-init --ai copilot

# 安装到 Kiro
paper-reading-init --ai kiro

# 安装到 Codex
paper-reading-init --ai codex

# 安装到 Gemini CLI
paper-reading-init --ai gemini
```

### 安装到所有 AI 助手

```bash
paper-reading-init --ai all
```

### 指定项目目录

默认情况下，CLI 会在当前目录安装技能。你也可以指定其他目录：

```bash
paper-reading-init --ai claude --dir /path/to/your/project
```

## 安装后的目录结构

安装后，技能文件会被复制到相应的目录：

### Claude Code
```
.claude/
└── skills/
    └── paper-reading/
        ├── SKILL.md
        └── scripts/
            └── paper_skill.py
```

### Cursor
```
.cursor/
└── commands/
    └── paper-reading.md
.shared/
└── paper-reading/
    └── scripts/
        └── paper_skill.py
```

### Windsurf
```
.windsurf/
└── workflows/
    └── paper-reading.md
.shared/
└── paper-reading/
    └── scripts/
        └── paper_skill.py
```

### Antigravity
```
.agent/
└── workflows/
    └── paper-reading.md
.shared/
└── paper-reading/
    └── scripts/
        └── paper_skill.py
```

### GitHub Copilot
```
.github/
└── prompts/
    └── paper-reading.prompt.md
```

### Kiro
```
.kiro/
└── steering/
    └── paper-reading.md
.shared/
└── paper-reading/
    └── scripts/
        └── paper_skill.py
```

### Codex
```
.codex/
└── skills/
    └── paper-reading/
        ├── SKILL.md
        └── scripts/
            └── paper_skill.py
```

### Gemini CLI
```
.gemini/
└── skills/
    └── paper-reading/
        ├── SKILL.md
        └── scripts/
            └── paper_skill.py
.shared/
└── paper-reading/
    └── scripts/
        └── paper_skill.py
```

## 使用示例

### 完整工作流

1. 安装包：
```bash
pip install paper-reading-framework
```

2. 进入你的项目目录：
```bash
cd /path/to/your/project
```

3. 安装技能到 Claude Code：
```bash
paper-reading-init --ai claude
```

4. 在 Claude Code 中使用：
```
Analyze paper 2301.12345 and generate implementation code
```

### 多平台安装

如果你使用多个 AI 助手，可以一次性安装到所有平台：

```bash
paper-reading-init --ai all
```

## 故障排除

### 找不到技能文件

如果 CLI 提示找不到技能文件，请确保：
1. 已正确安装 `paper-reading-framework` 包
2. 包已正确安装到 Python 环境中

### 权限错误

如果遇到权限错误，请确保：
1. 对目标目录有写权限
2. 使用适当的用户权限运行命令

### 文件已存在

如果目标文件已存在，CLI 会覆盖它们。如果需要保留原有文件，请先备份。

## 更新技能

要更新已安装的技能，只需重新运行安装命令：

```bash
paper-reading-init --ai claude
```

CLI 会自动覆盖旧文件。

## 卸载

要卸载技能，只需删除相应的目录：

```bash
# 卸载 Claude Code 技能
rm -rf .claude/skills/paper-reading

# 卸载 Cursor 技能
rm -rf .cursor/commands/paper-reading.md
rm -rf .shared/paper-reading
```

## 更多信息

更多使用信息，请参考：
- [README.md](../README.md)
- [SKILL.md](../.claude/skills/paper-reading/SKILL.md)
- [CLAUDE.md](../CLAUDE.md)
