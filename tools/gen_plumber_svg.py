#!/usr/bin/env python3
"""Generate inline SVG pixel plumber frames (16x22 cells, 2 SVG units per cell)."""
from __future__ import annotations

W, H = 16, 22
# Characters: . empty, K black outline/shadow, R red cap, S skin, B blue overalls,
# W white glove, N brown shoe/hair, O dark blue overalls shadow
PALETTE = {
    ".": None,
    "K": "#181818",
    "R": "#E83800",
    "r": "#C02008",
    "S": "#F8C0A0",
    "s": "#E8A080",
    "B": "#2848F8",
    "b": "#1828C8",
    "W": "#F8F8F8",
    "N": "#884010",
    "n": "#602008",
    "O": "#102070",
}

# Frame A: left leg forward
GRID_A = """
......RRRR......
.....RRRRRR.....
....RRRRRRRR....
...KKRRRRRRKK...
...KRRRRRRRRK...
..KRRSSSSSSRRK..
..KRSSSSSSSSRK..
..KSSSSSSSSSKK..
..KSSKSSKKSSSK..
..KSSSSSSSSSK...
..KBWWBBWWBBK...
..KBWWBBWWBBK...
..KBBBBBBBBBK...
..KBBBBBBBBBK...
..KBOBBBBOBBK...
..KBBBBBBBBBK...
..KBBBBBBBBBK...
..KNBBBBBBBNK...
..KNBBBBBBBNK...
..KNN....NNNK...
..KN......NK....
...K......K.....
""".strip().split("\n")

# Frame B: other leg forward (boots shifted vs frame A)
GRID_B = [list(row) for row in GRID_A]
# Rows 0-16 identical; tweak stance 17-21
GRID_B[17] = list("..KNBBBBBBBNK...")
GRID_B[18] = list("..KNBBBBBBBNK...")
GRID_B[19] = list("..KN......NK....")
GRID_B[20] = list("..KNN....NNNK...")
GRID_B[21] = list("...K......K.....")
GRID_B = ["".join(row) for row in GRID_B]


def grid_to_svg_cells(grid: list[str], gid: str) -> str:
    rects = []
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == ".":
                continue
            color = PALETTE.get(ch)
            if color is None:
                raise ValueError(f"Bad char {ch!r} at {x},{y}")
            px, py = x * 2, y * 2
            rects.append(
                f'<rect x="{px}" y="{py}" width="2" height="2" fill="{color}"/>'
            )
    return f'<g id="{gid}">\n' + "\n".join(rects) + "\n</g>"


if __name__ == "__main__":
    print(grid_to_svg_cells(GRID_A, "plumber-run-a"))
    print()
    print(grid_to_svg_cells(GRID_B, "plumber-run-b"))
