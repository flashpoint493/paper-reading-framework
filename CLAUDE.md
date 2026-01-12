# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Paper Reading Framework is an AI-powered academic paper analysis toolkit using Moonshot AI (Kimi). It provides intelligent paper fetching, deep AI analysis, personalized reading guidance, knowledge internalization, and code generation capabilities. It works as a skill/workflow for AI coding assistants (Claude Code, Cursor, Windsurf, etc.).

## Paper Processing Command

```bash
python3 .claude/skills/paper-reading/scripts/paper_skill.py <arxiv_id_or_url> [--action <action>] [--type <type>]
```

**Actions:**
- `download` - Download paper only
- `analyze` - Analyze existing paper
- `full` - Complete workflow (download + analyze + code generation)

**Analysis types:**
- `comprehensive` - Full analysis (default)
- `summary` - Brief summary
- `methodology` - Methodology details
- `innovation` - Innovation points
- `implementation` - Implementation guide

## Architecture

```
.claude/skills/paper-reading/    # Claude Code skill
├── SKILL.md                      # Skill definition with workflow instructions
└── scripts/
    └── paper_skill.py            # Main entry point for paper processing

original_code/                    # Original source code
├── src/
│   ├── api/                      # Moonshot AI client
│   ├── paper/                    # Paper fetching and parsing
│   ├── knowledge/                # Knowledge internalization
│   ├── reading/                  # Reading assistance
│   └── implementation/           # Code generation
└── config.yaml.example           # Configuration template
```

## Configuration

The framework uses environment variables or `config.yaml` for configuration:

**Required:**
- `MOONSHOT_API_KEY` - Your Moonshot AI API key (from .env file)

**Optional (in config.yaml):**
- `moonshot.model` - Model to use (moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k)
- `moonshot.temperature` - Temperature parameter (0.0-1.0)
- `paper_reading.paper_workspace_dir` - Output directory for results (default: data/papers)

## Usage Examples

### Quick Summary
```bash
python3 .claude/skills/paper-reading/scripts/paper_skill.py 2301.12345 --action analyze --type summary
```

### Full Analysis with Code
```bash
python3 .claude/skills/paper-reading/scripts/paper_skill.py 2301.12345 --action full
```

### Download Only
```bash
python3 .claude/skills/paper-reading/scripts/paper_skill.py 2301.12345 --action download
```

## Output Structure

Results are saved in `data/papers/<paper_id>/`:
- `notes/` - Structured notes
- `summaries/` - Paper summaries
- `code/` - Generated code framework
- `knowledge/` - Knowledge graph

## Prerequisites

Python 3.8+ with required packages:
- requests
- openai
- python-dotenv
- beautifulsoup4
- lxml
- PyPDF2
- markdown
- pyyaml
- tqdm
- aiohttp

## Git Workflow

Never push directly to `main`. Always:

1. Create a new branch: `git checkout -b feat/...` or `fix/...`
2. Commit changes
3. Push branch: `git push -u origin <branch>`
4. Create PR: `gh pr create`

## Environment Variables

The project uses `.env` file for sensitive information:
- `MOONSHOT_API_KEY` - Moonshot AI API key
- `GITHUB_TOKEN` - GitHub token for publishing
- `PYPI_TOKEN` - PyPI token for publishing

**Important:** Never commit `.env` file to the repository.
