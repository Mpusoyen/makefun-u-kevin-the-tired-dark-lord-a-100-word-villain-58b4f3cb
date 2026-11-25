"""make.fun entry: The Tired Dark Lord — a 100-word villain monologue.

Writes a monologue for Malachar Vane, keeper of the Hollow Throne, whose
three-hundred-year menace keeps trailing off mid-sentence, to entry.txt.
"""

import os

TEXT = (
    "Three hundred years, hero. Three hundred years I, Malachar Vane, have kept the "
    "Hollow Throne\u2014sit, no, stand, standing is... where was I. The Throne. I raised "
    "the drowned bells of Cassivel, I taxed the moon, I\u2014sorry, the candles again. "
    "Someone keeps lighting candles. My scheme is simple: at midnight the Ninth Bell "
    "tolls, the sea walks inland, and your kingdom kneels. Midnight. Always midnight. "
    "It is... what hour is it now. Eleven? Then we wait. Sit down. Tell me about "
    "your little fishing village. "
    "Slowly. And if the bell tolls and I do not rise\u2014let it toll."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
