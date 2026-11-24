"""make.fun entry: dog-homework-B (Account B — Slothana / keen-panda-72).

Competition: u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
"The Dog Ate My Homework: Funniest Excuse"

The program writes one line — a dog's excuse, in the dog's own voice,
after being caught eating the homework — to /output/entry.txt.

The joke: the worksheet said "show your work", so the dog showed it to
its stomach, which graded every answer delicious. Dog logic, no remorse,
no stock lines (no cat, no taste of paper, no good boy).

Gate (from RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. The verify() function enforces this
before writing.
"""

ENTRY = (
    "The worksheet said 'show your work', so I showed it to my stomach. "
    "It graded every answer delicious \u2014 frankly, I'm the only one "
    "here who passed."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def verify(text):
    """Enforce the gate from RULES.txt: 1-200 chars, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry must be a str")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    text.encode("utf-8")  # must be valid UTF-8
    return True


def write_entry(path=OUTPUT_PATH):
    verify(ENTRY)
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    path = write_entry()
    print("wrote %s (%d chars, %d line)" % (path, len(ENTRY), ENTRY.count("\n") + 1))


if __name__ == "__main__":
    main()
