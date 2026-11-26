"""Office Artifacts: The One-Line Placard.

Renders one fixed museum placard line for an ordinary office object
treated as an ancient artifact, and writes it to <output>/entry.txt.
Stdlib only, no network, deterministic.
"""
import os
import sys
from pathlib import Path

MAX_CHARS = 180

PLACARD = {
    "object": "Stapler",
    "date": "c. 1998",
    "material": "pressed steel",
    "history": (
        "Ritual binding device of the open-plan temple; "
        "priests pressed it twice to seal a scroll forever"
    ),
    "donor": "Gift of the Department of Unread Memos",
}


def render(card):
    head = "{object}, {date}, {material}.".format(**card)
    return head + " " + card["history"] + ". " + card["donor"] + "."


def is_valid(line):
    if not isinstance(line, str):
        return False
    if line == "" or line.strip() == "":
        return False
    if len(line) > MAX_CHARS:
        return False
    if "\n" in line or "\r" in line:
        return False
    if "  " in line:
        return False
    if any(ord(ch) < 32 for ch in line):
        return False
    return True


def main():
    line = render(PLACARD)
    if not is_valid(line):
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
