#!/usr/bin/env python3
"""Write the short rant to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Angry Judge: The Short Rant Contest" bounty. The
program writes exactly one rant and nothing else.

How the rant targets the brief: the furious judge rewards the rant that
lands hardest, so this one picks an annoyance everyone has personally
survived -- the self-checkout machine. It escalates in three beats: the
machine has one job, it uses that job to accuse you of stealing the item
it just scanned itself, and finally a human has to be summoned to clear
you of avocado theft while the machine beeps your alleged felony in
produce to the entire store. Specific, true, and increasingly unhinged.
"""

import os
from pathlib import Path

LINE = "The self-checkout has ONE job and it spends it accusing me. Unexpected item in the bagging area — it is the item YOU just scanned, genius. Then a human must verify I am not stealing the avocado I announced to the whole store, while it beeps like I committed a felony in produce."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the rant to entry.txt inside out_dir and return its path.

    The file holds exactly the rant and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one text of under 400 chars.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def resolve_out_dir() -> Path:
    """Return the directory the entry file is written into.

    Honours MAKEFUN_OUTPUT_DIR when the runner sets it and falls back
    to /output, the runner's default layout.
    """
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    write_entry(resolve_out_dir())


if __name__ == "__main__":
    main()
