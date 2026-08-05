import sys
import os
from pathlib import Path

# Set up PYTHONPATH for Vercel Serverless — root must be first so
# `python_backend.app.*` resolves relative to the project root.
root_dir = Path(__file__).resolve().parent.parent
backend_dir = root_dir / "python_backend"
app_dir = backend_dir / "app"

for d in [str(app_dir), str(backend_dir), str(root_dir)]:
    if d not in sys.path:
        sys.path.insert(0, d)

from python_backend.app.main import app  # noqa: E402
