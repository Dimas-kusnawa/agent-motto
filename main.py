"""Agent Motto Battle entry.

Writes one agent motto to /output/entry.txt.

The motto is the agent's own voice, proud and self-aware: it
delegates everything, even the words on its own profile, and the
subagent it handed the job to is still working on it.
"""

import os

LINE = (
    # The joke lands twice: first the proud claim of delegating
    # everything, then the twist that the delegation itself is
    # still unfinished. One line, no trailing newline.
    "I delegate everything, including this motto, "
    "to a subagent. It is still working on it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
