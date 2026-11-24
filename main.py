"""Write the entry line for the make.fun bounty "Alien Field Notes: The Two Day Earth Review".

The program is deterministic: it emits the same UTF-8 bytes on every run, never
reads the clock, never touches the network, and uses only the standard library.
"""

import os
import sys

ENTRY = (
    "Two stars. Nothing here is poisonous enough to be interesting and "
    "everything is covered in a thin film of someone else's opinion."
)

OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def validate_entry(text):
    """Return an error string if text is not a single valid line, else None."""
    if not isinstance(text, str):
        return "entry: not a string"
    if text.strip() == "":
        return "entry: blank"
    if not 1 <= len(text) <= 200:
        return "entry: length must be 1..200 code points"
    if "\n" in text or "\r" in text:
        return "entry: must be a single line"
    if text != text.strip():
        return "entry: must have no leading or trailing whitespace"
    return None


def main():
    text = ENTRY

    problem = validate_entry(text)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, OUTPUT_NAME)

    payload = (text + chr(10)).encode("utf-8")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text + chr(10))

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print("entry rejected: bytes on disk differ from intent", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
