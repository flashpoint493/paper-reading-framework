"""Test PDF parsing"""
from src.paper.parser import PaperParser

parser = PaperParser()
result = parser.parse_pdf('papers/2301.12345.pdf')

print(f"Title: {result.get('title', 'N/A')[:200]}")
print(f"Abstract length: {len(result.get('abstract', ''))}")
print(f"Full text length: {len(result.get('full_text', ''))}")
print(f"\nFirst 1000 chars of full text:")
print(result.get('full_text', '')[:1000])
print(f"\nError: {result.get('error', 'None')}")
