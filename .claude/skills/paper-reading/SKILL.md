---
name: paper-reading
description: "Paper reading and analysis framework using Moonshot AI (Kimi). Actions: download, analyze, read, summarize, implement papers from arXiv, SIGGRAPH, etc. Features: intelligent paper fetching, AI deep analysis, personalized reading guidance, knowledge internalization, code generation. Supports: PDF parsing, multi-dimensional analysis (summary, innovation, methodology, implementation), structured notes, knowledge graphs, code framework generation."
---

# Paper Reading - Academic Paper Analysis Framework

Complete framework for precision reading, internalization, and implementation of academic papers using Moonshot AI (Kimi).

## Prerequisites

Check if Python is installed:

```bash
python3 --version || python --version
```

If Python is not installed, install it based on user's OS:

**macOS:**
```bash
brew install python3
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install python3
```

**Windows:**
```powershell
winget install Python.Python.3.12
```

Install required dependencies:

```bash
pip install requests openai python-dotenv beautifulsoup4 lxml PyPDF2 markdown pyyaml tqdm aiohttp
```

---

## How to Use This Skill

When user requests paper reading work (download, analyze, read, summarize, implement), follow this workflow:

### Step 1: Analyze User Requirements

Extract key information from user request:
- **Paper source**: arXiv ID, URL, or local PDF path
- **Action type**: download, analyze, full (download + analyze + code generation)
- **Analysis type**: comprehensive, summary, methodology, innovation, implementation
- **Reader profile**: amateur or professional (affects explanation depth)

### Step 2: Execute Paper Processing

Use `paper_skill.py` to process the paper:

```bash
python3 .claude/skills/paper-reading/scripts/paper_skill.py <arxiv_id_or_url> [--action <action>] [--type <type>]
```

**Available actions:**
- `download` - Only download the paper
- `analyze` - Analyze existing paper
- `full` - Complete workflow (download + analyze + code generation)

**Available analysis types:**
- `comprehensive` - Full analysis (default)
- `summary` - Brief summary
- `methodology` - Methodology details
- `innovation` - Innovation points
- `implementation` - Implementation guide

### Step 3: Access Results

After processing, results are saved in:
- **Notes**: `data/papers/<paper_id>/notes/`
- **Summaries**: `data/papers/<paper_id>/summaries/`
- **Code**: `data/papers/<paper_id>/code/`
- **Knowledge Graph**: `data/papers/<paper_id>/knowledge/`

---

## Search Reference

### Supported Paper Sources

| Source | Format | Example |
|--------|--------|---------|
| arXiv | ID or URL | `2301.12345` or `https://arxiv.org/abs/2301.12345` |
| SIGGRAPH | URL | `https://www.siggraph.org/...` |
| Local PDF | File path | `papers/paper.pdf` |

### Analysis Types

| Type | Description | Use Case |
|------|-------------|----------|
| `comprehensive` | Full analysis with all aspects | Deep understanding |
| `summary` | Brief overview | Quick review |
| `methodology` | Technical details and methods | Implementation focus |
| `innovation` | Key innovations and contributions | Research insights |
| `implementation` | Code generation guide | Practical application |

---

## Example Workflow

**User request:** "Analyze paper 2301.12345 and generate implementation code"

**AI should:**

```bash
# Execute full workflow
python3 .claude/skills/paper-reading/scripts/paper_skill.py 2301.12345 --action full
```

**Then:** Review the generated files and provide summary:
- Notes location
- Summary location
- Code directory
- Key findings

---

## Tips for Better Results

1. **Use full action for complete analysis** - Downloads, analyzes, and generates code
2. **Specify analysis type** - Choose appropriate type for your needs
3. **Check generated files** - Review notes, summaries, and code structure
4. **Iterate on analysis** - Run different analysis types for different perspectives
5. **Review implementation guide** - Check code directory for implementation details

---

## Configuration

The skill uses environment variables or `config.yaml` for configuration:

**Required:**
- `MOONSHOT_API_KEY` - Your Moonshot AI API key

**Optional (in config.yaml):**
- `moonshot.model` - Model to use (moonshot-v1-8k, moonshot-v1-32k, moonshot-v1-128k)
- `moonshot.temperature` - Temperature parameter (0.0-1.0)
- `paper_reading.paper_workspace_dir` - Output directory for results

---

## Common Workflows

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

---

## Output Structure

```
data/papers/<paper_id>/
├── notes/              # Structured notes
├── summaries/          # Paper summaries
├── code/               # Generated code framework
│   ├── README.md
│   ├── main.py
│   ├── algorithm.py
│   └── implementation_guide.md
└── knowledge/          # Knowledge graph
    └── knowledge_graph.json
```
