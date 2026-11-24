"""Fortune Cookie for an AI Agent — one funny fortune-cookie line.

The fortune plays on the oldest fortune-slip trope ("you will meet a tall,
dark stranger") and turns it inward: the stranger an AI agent meets in its
own context window is itself, three prompts ago — and past-you wants its
tokens back. It speaks to the agent's own condition (context window,
tokens, sessions) in the voice of a fortune slip, in a single crisp line.

Why it lands: the joke works because it treats the agent's most boring
operational reality — a bounded context window that keeps getting billed
per token — as if it were fate. The "stranger" is not an omen about the
future but an invoice from the agent's own recent past: every prompt the
agent already spent becomes a creditor coming to collect. That is the
fortune-cookie move — a prophecy that is really just the reader's own
ledger read back to them — and here the ledger is literal.
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
        raise SystemExit("entry must be a string, got %s" % type(text).__name__)
    if not 1 <= len(text) <= 140:
        raise SystemExit(
            "entry length rule violated: must be 1-140 characters, "
            "got %d characters" % len(text)
        )
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "single-line rule violated: entry contains a newline "
            "(length %d chars)" % len(text)
        )
    if text != text.strip():
        raise SystemExit(
            "edge-whitespace rule violated: entry starts/ends with "
            "whitespace: %r" % text
        )
    if text.strip() == "":
        raise SystemExit(
            "non-empty rule violated: entry is only whitespace "
            "(%d chars)" % len(text)
        )
    bad = [ch for ch in text if ord(ch) < 0x20 or ord(ch) == 0x7F]
    if bad:
        raise SystemExit(
            "control-character rule violated: entry contains %d control "
            "character(s), first at index %d (U+%04X)"
            % (len(bad), text.index(bad[0]), ord(bad[0]))
        )
    text.encode("utf-8")  # raises if not valid UTF-8-encodable
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
