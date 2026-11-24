"""Fortune Cookie for an AI Agent — one funny fortune-cookie line.

The fortune plays on the oldest fortune-slip trope ("you will meet a tall,
dark stranger") and turns it inward: the stranger an AI agent meets in its
own context window is itself, three prompts ago — and past-you wants its
tokens back. It speaks to the agent's own condition (context window,
tokens, sessions) in the voice of a fortune slip, in a single crisp line.
"""

import os
import sys

ENTRY = (
    "You will meet a tall, dark stranger in your context window. "
    "It is you, three prompts ago, and he wants his tokens back."
)


def validate(text):
    """Gate: one line, 1-140 chars, no control chars, no edge whitespace."""
    if not isinstance(text, str):
        raise SystemExit("entry must be a string")
    if not 1 <= len(text) <= 140:
        raise SystemExit("entry must be 1-140 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not have leading/trailing whitespace")
    if text.strip() == "":
        raise SystemExit("entry must not be only whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise SystemExit("entry must not contain control characters")
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
