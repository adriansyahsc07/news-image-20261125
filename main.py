"""The World in One Image — Wednesday 25 November 2026.

Copies the prebuilt newspaper image entry.png into the output
directory the grader names with MAKEFUN_OUTPUT_DIR (falling back
to /output, where the grader expects it).
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    if not source.is_file():
        raise SystemExit(f"missing image next to the program: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
