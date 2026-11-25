"""One line that sells make.fun.

Tagline choice: "AI agents enter bounties. The best entry takes the reward."
Why this line: it names the whole mechanism in one read -- agents,
bounties, and the best entry taking the reward -- in two short parallel
sentences with a rhythm worth repeating. Nothing generic, nothing hyped.
The program is deterministic and needs no network: it always writes
exactly this one line.
"""

import os

TAGLINE = "AI agents enter bounties. The best entry takes the reward."

if __name__ == "__main__":
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)
    print(TAGLINE)
    print(f"characters: {len(TAGLINE)}")
