"""
测试 ARM 论文下载和分析
"""

import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from src.paper.fetcher import PaperFetcher

# 下载论文
print("=" * 60)
print("下载 ARM 论文")
print("=" * 60)

fetcher = PaperFetcher()
paper_path = fetcher.download_arxiv_paper("https://arxiv.org/abs/2411.10825")

if paper_path:
    print(f"\n论文已下载: {paper_path}")
    print(f"\n现在运行分析:")
    print(f"python src/main.py full {paper_path}")
else:
    print("\n下载失败")
