"""Setup standard skill directory structure"""
from pathlib import Path
import shutil

# Create directory structure
base_dir = Path("skills/paper_reading")
dirs = [
    base_dir / "data" / "input_data",
    base_dir / "data" / "output_data",
    base_dir / "scripts",
]

for dir_path in dirs:
    dir_path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {dir_path}")

print("\nDirectory structure created successfully!")
