#!/usr/bin/env python3
"""Write the funniest-toaster-error entry to /output/entry.txt.

One error message, at most 120 characters, that a kitchen toaster
shows its owner: the surprise comes from somewhere the obvious
toaster puns never go — not burnt bread or a stuck slice, but the
appliance calmly reclassifying an over-toasted bagel as a cracker,
with the flat authority of a real error message. The voice stays
deadpan to the end: the toaster is not joking, it is reporting a
legal fact, and that is what makes it funny on a single read.
"""
import os

TEXT = "WARNING: This bagel has been toasted 4 times. It is now legally a cracker."

def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(tmp, 0o644)
    os.replace(tmp, "/output/entry.txt")

if __name__ == "__main__":
    main()
