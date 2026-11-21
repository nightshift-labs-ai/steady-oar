import os
import sys

TEXT = (
    "The lake is still at seven.\n"
    "A coot crosses it, slowly.\n"
    "She wades to her knees, then her waist,\n"
    "and waits for the cold to finish speaking.\n"
    "It does. Her breath comes back.\n"
    "She leans forward,\n"
    "and the water holds her."
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
