#!/usr/bin/env python3
"""Entry point for the 19 November 2026 news poster.

The poster itself is drawn once by build_poster.py and stored in this
repository as entry.png. This program only copies that file into the
output directory the grader provides, so both runs produce identical
bytes. It uses only the standard library and touches no network.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
