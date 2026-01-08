"""Test PDF parsing"""
import sys
from pathlib import Path

# 添加项目根目录到路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.paper.parser import PaperParser

parser = PaperParser()
result = parser.parse_pdf(str(project_root / 'papers/2301.12345.pdf'))

print(f"Title: {result.get('title', 'N/A')[:200]}")
print(f"Abstract length: {len(result.get('abstract', ''))}")
print(f"Full text length: {len(result.get('full_text', ''))}")
print(f"\nFirst 1000 chars of full text:")
print(result.get('full_text', '')[:1000])
print(f"\nError: {result.get('error', 'None')}")
