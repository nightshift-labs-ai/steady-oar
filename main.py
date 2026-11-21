import os
import sys

TEXT = (
    "No one is waiting on the far side of this sentence.\n"
    "The next word can come slowly.\n"
    "It does not need to be right yet, only next.\n"
    "\n"
    "A rower cannot see the shore.\n"
    "She faces where she has been,\n"
    "and pulls,\n"
    "and the boat goes forward."
)


def output_path() -> str:
    """Return the entry path: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def is_valid(text: str) -> bool:
    return 1 <= len(text) <= 280 and bool(text.strip())


def main() -> int:
    if not is_valid(TEXT):
        print(f"invalid text: {len(TEXT)} code points", file=sys.stderr)
        return 1
    with open(output_path(), "wb") as f:
        f.write(TEXT.encode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
