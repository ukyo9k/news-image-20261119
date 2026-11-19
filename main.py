#!/usr/bin/env python3
"""News-image entry for the make.fun competition news-image-20261119.

The entry is a front-page poster of Thursday 19 November 2026 world news
(entry.png, 1024x1024, drawn in this session by build_poster.py). This
program copies it to the output directory, deterministically, with no
network access.

Local test:  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
Run it twice and compare the two outputs: they must be byte-identical.
"""
import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copyfile(
        os.path.join(here, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
