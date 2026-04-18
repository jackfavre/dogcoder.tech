#!/usr/bin/env python3
"""Generate two-frame SMW-style Small Mario run SVG groups.

Grid is 16 wide x 16 tall pixels per frame. Each pixel is rendered as a 2x2
rect in SVG so the final sprite viewBox is 32 x 32.

Palette (chosen to evoke Super Mario World SNES palette):
  . = transparent
  K = black outline         #101010
  R = bright red (hat, shirt)  #E02020
  r = dark red (shadow)     #981818
  N = brown (hair, boots)   #701C08
  S = skin                  #F8C088
  s = skin shadow           #D8906C
  B = blue overalls         #2838C8
  b = dark blue shadow      #101878
  W = white (glove)         #F8F8F8
  Y = yellow (button)       #F8D020
  M = mustache black        #181818
"""
from __future__ import annotations

PALETTE = {
    "K": "#101010",
    "R": "#E02020",
    "r": "#981818",
    "N": "#701C08",
    "S": "#F8C088",
    "s": "#D8906C",
    "B": "#2838C8",
    "b": "#101878",
    "W": "#F8F8F8",
    "Y": "#F8D020",
    "M": "#181818",
}

# Small Mario running (frame A) - SMW-style, facing right, 16x16.
# Canvas columns: 0..15.  Legend in PALETTE above.
FRAME_A = [
    ".....RRRRR......",  # 0  hat top
    "....RRRRRRRRR...",  # 1  hat brim
    "....NNNSSSSK....",  # 2  hair + forehead
    "...NSNSSSSSSK...",  # 3  sideburn + eye
    "...NSNNSSSSSK...",  # 4  eye pupil
    "....NSSSSSSSK...",  # 5  lower face
    ".....MMSSSK.....",  # 6  mustache line
    "...RRRBRBRRRK...",  # 7  shoulders + overall straps
    "..RRRRBRBRRRRK..",  # 8  upper torso
    "..WWBBBBBBBBWW..",  # 9  gloves + overalls front
    "..WWBYBBBBYBWW..",  # 10 yellow buttons + gloves
    "...KBBBBBBBK....",  # 11 torso bottom
    "...KBBB.BBBK....",  # 12 legs split
    "...NNN...NNN....",  # 13 upper boots
    "..NNN.....NNN...",  # 14 boot bodies
    "..NN.......NN...",  # 15 boot tips
]

# Frame B - mirrored leg pose (running cycle second step).
FRAME_B = list(FRAME_A)
FRAME_B[12] = "...KBBB.BBBK...."
FRAME_B[13] = "....NNN.NNN....."
FRAME_B[14] = "...NNN...NNN...."
FRAME_B[15] = "...NN.....NN...."

W = 16
H = 16


def to_rects(grid, cls):
    assert len(grid) == H, f"expected {H} rows, got {len(grid)}"
    for row in grid:
        assert len(row) == W, f"expected {W} cols, got {len(row)} in {row!r}"
    rects = []
    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == ".":
                continue
            color = PALETTE.get(ch)
            if color is None:
                raise ValueError(f"Unknown pixel {ch!r} at {x},{y}")
            rects.append(
                f'<rect x="{x*2}" y="{y*2}" width="2" height="2" fill="{color}"/>'
            )
    return f'<g class="{cls}">\n' + "\n".join(rects) + "\n</g>"


def build_svg() -> str:
    a = to_rects(FRAME_A, "smw-hero__run smw-hero__run--a")
    b = to_rects(FRAME_B, "smw-hero__run smw-hero__run--b")
    return (
        '<svg class="smw-hero__svg" viewBox="0 0 32 32" '
        'xmlns="http://www.w3.org/2000/svg" shape-rendering="crispEdges" '
        'aria-hidden="true">\n' + a + "\n" + b + "\n</svg>"
    )


if __name__ == "__main__":
    print(build_svg())
