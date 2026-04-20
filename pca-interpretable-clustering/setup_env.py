"""
setup_env.py
────────────
Installs all packages listed in requirements.txt into the current Python
environment.  Run once before executing either notebook.

Usage
-----
    python setup_env.py

Requirements
------------
    Python 3.12+  (packaged by Anaconda, Inc. recommended)
    pip           (comes with Anaconda / standard Python distributions)
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REQUIREMENTS_FILE = Path(__file__).parent / "requirements.txt"


def main() -> None:
    if not REQUIREMENTS_FILE.exists():
        print(f"[ERROR] '{REQUIREMENTS_FILE}' not found.  "
              "Make sure you run this script from the repository root.")
        sys.exit(1)

    print("=" * 60)
    print("  PCA Interpretable Clustering — Environment Setup")
    print("=" * 60)
    print(f"\nInstalling packages from: {REQUIREMENTS_FILE}\n")

    result = subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)],
        check=False,
    )

    if result.returncode == 0:
        print("\n[OK]  All packages installed successfully.")
        print("      You can now run the notebooks in order:")
        print("        1. pca_data_classifier.ipynb")
        print("        2. PCA_interpretable_clusstering.ipynb")
    else:
        print("\n[WARN] pip exited with a non-zero status.  "
              "Review the output above for errors.")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main()
