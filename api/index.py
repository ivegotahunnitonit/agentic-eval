import sys
import os
from pathlib import Path

# Set up PYTHONPATH for Vercel Serverless
root_dir = Path(__file__).resolve().parent.parent
backend_dir = root_dir / "python_backend"
app_dir = backend_dir / "app"

for d in [str(root_dir), str(backend_dir), str(app_dir)]:
    if d not in sys.path:
        sys.path.insert(0, d)

from python_backend.app.main import app
