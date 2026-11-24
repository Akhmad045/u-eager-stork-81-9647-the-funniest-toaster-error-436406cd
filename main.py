#!/usr/bin/env python3
"""Toaster error message entry for make.fun.

A kitchen toaster reports a failure to its owner in one deadpan line.
This program puts that line in /output/entry.txt and proves the file on
disk holds exactly the line it was given, byte for byte.

No network, no third-party code: Python 3.13 standard library only.
"""

import pathlib
import sys

MESSAGE = (
    "Error E-07: Your bread is now charcoal. "
    "I have already apologised to the smoke alarm."
)

DESTINATION = pathlib.Path("/output/entry.txt")
LIMIT = 120


def problems(line: str) -> list[str]:
    """Every way the line can fail the gate, as plain messages."""
    found = []
    if not line:
        found.append("line is empty")
    if len(line) > LIMIT:
        found.append(f"line is {len(line)} characters, over the {LIMIT} limit")
    if line.strip() != line:
        found.append("line has leading or trailing whitespace")
    if line.splitlines() != [line]:
        found.append("line is not a single line")
    if any(code < 32 or code == 127 for code in map(ord, line)):
        found.append("line contains a control character")
    if not line.strip():
        found.append("line is only whitespace")
    return found


def write_and_check(line: str, path: pathlib.Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((line + "\n").encode("utf-8"))
    # Read the bytes back and compare with what was intended, so the
    # encoding, the newline and the text itself are all checked at once.
    if path.read_bytes() != (line + "\n").encode("utf-8"):
        raise SystemExit("error: /output/entry.txt did not round-trip exactly")


def main() -> int:
    bad = problems(MESSAGE)
    if bad:
        for item in bad:
            print(f"invalid entry: {item}", file=sys.stderr)
        return 1
    write_and_check(MESSAGE, DESTINATION)
    print(f"wrote {len(MESSAGE)} characters ({len(MESSAGE.encode('utf-8'))} bytes) to {DESTINATION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
