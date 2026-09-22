import sys
from pathlib import Path

# Add the project root to Python's import path.
# This allows tests to import modules using "from src..."
ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))