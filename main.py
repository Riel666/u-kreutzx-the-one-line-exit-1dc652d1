"""Write one resignation letter, exactly one line, to /output/entry.txt.

The letter is one line a person could actually send: the coffee
machine got a farewell party, the writer got a calendar invite,
and they are done ranking below an appliance. At most 140
characters, and the program writes exactly that line and nothing else.
"""

import os

TEXT = 'I hereby resign — the coffee machine got a farewell party, I got a calendar invite, and I am done ranking below an appliance.'


def main():
    assert 1 <= len(TEXT) <= 140, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
