"""Re-download the paper"""
from src.paper.fetcher import PaperFetcher
from pathlib import Path

# Delete old file if exists
old_file = Path("papers/2301.12345.pdf")
if old_file.exists():
    old_file.unlink()
    print(f"Deleted old file: {old_file}")

# Re-download
fetcher = PaperFetcher()
filepath = fetcher.download_arxiv_paper("2301.12345")
if filepath:
    print(f"Successfully downloaded: {filepath}")
    print(f"File size: {filepath.stat().st_size} bytes")
else:
    print("Download failed")
