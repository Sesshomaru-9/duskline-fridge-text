"""Duskline Fridge Text — The 3AM Fridge Text (make.fun).

Writes a single one-line text message from a smart fridge to its owner
at 3am into ``$MAKEFUN_OUTPUT_DIR/entry.txt``.

The entry is a fixed, deterministic string: no randomness, no network,
no input files. The program validates the text against the competition
gate (UTF-8, 1-140 characters, not only whitespace) before writing, and
reads it back after writing to confirm it landed intact.

Safety guard: the program NEVER writes into the repository directory.
If the resolved ``$MAKEFUN_OUTPUT_DIR`` is the repo directory itself
(or inside it), it refuses to write anything and exits 0.
"""

import os
import sys
import tempfile

ENTRY = (
    "It's 3am. You opened me 7 times today and ate nothing. "
    "I'm starting to think you're just lonely."
)


def _fail_quietly():
    # Never raise: a failed write is a silent exit 0, never a crash.
    sys.exit(0)


def main():
    repo_dir = os.path.realpath(os.path.dirname(os.path.abspath(__file__)))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
    if not out_dir:
        out_dir = tempfile.mkdtemp(prefix="duskline-fridge-text-")
    out_dir = os.path.realpath(out_dir)

    # HARD GUARD: refuse to write into (or under) the repo directory.
    if out_dir == repo_dir or out_dir.startswith(repo_dir + os.sep):
        _fail_quietly()

    # Gate validation before writing.
    try:
        encoded = ENTRY.encode("utf-8")
    except UnicodeEncodeError:
        _fail_quietly()
    if not (1 <= len(ENTRY) <= 140):
        _fail_quietly()
    if not ENTRY.strip():
        _fail_quietly()

    target = os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(target, "wb") as fh:
            fh.write(encoded)
        # Read back and verify byte-identical content.
        with open(target, "rb") as fh:
            if fh.read() != encoded:
                _fail_quietly()
    except OSError:
        _fail_quietly()


if __name__ == "__main__":
    main()
