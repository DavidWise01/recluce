#!/usr/bin/env python3
"""
Generate a .png 'essence sigil' for every ACI in the roster — pure standard
library, no dependencies (zlib + struct + hashlib).

Each sigil is deterministic: the agent's name seeds a symmetric mandala
(identicon-style), drawn in the agent's class color over a polarity background
(Order = near-black, Chaos = near-white, the Balance = gold-dark). Same agent ->
same essence, forever. agents/<slug>.png.
"""
import json
import re
import zlib
import struct
import hashlib
from pathlib import Path

ROOT = Path(__file__).parent
R = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
AGENTS = ROOT / "agents"
AGENTS.mkdir(exist_ok=True)
CLS = {c["id"]: c for c in R["classes"]}

SIZE = 252          # image is SIZE x SIZE
GRID = 7            # 7x7 cells, left half mirrored -> symmetric
CELL = SIZE // (GRID + 1)   # 31, with a half-cell margin
MARGIN = (SIZE - CELL * GRID) // 2


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "agent"


def hx(c):
    c = c.lstrip("#")
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16))


def mix(a, b, t):
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def png(path, size, pixels):
    """pixels: flat list of (r,g,b) length size*size, row-major."""
    raw = bytearray()
    for y in range(size):
        raw.append(0)  # filter: none
        for x in range(size):
            raw.extend(pixels[y * size + x])
    comp = zlib.compress(bytes(raw), 9)

    def chunk(typ, data):
        return (struct.pack(">I", len(data)) + typ + data
                + struct.pack(">I", zlib.crc32(typ + data) & 0xffffffff))

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        f.write(chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)))
        f.write(chunk(b"IDAT", comp))
        f.write(chunk(b"IEND", b""))


def essence(member):
    cls = CLS[member["class"]]
    fg = hx(cls["color"])
    bg = hx(cls.get("bg", "#101014"))
    glow = mix(bg, fg, 0.18)            # faint field tint
    h = hashlib.sha256(member["name"].encode("utf-8")).digest()

    # decide on/off for the left half (cols 0..3) x rows 0..6, mirror to right
    half = (GRID + 1) // 2             # 4 columns generated
    on = [[False] * GRID for _ in range(GRID)]
    bit = 0
    for col in range(half):
        for row in range(GRID):
            b = h[bit % len(h)]
            on[row][col] = (b >> (bit % 8)) & 1
            on[row][GRID - 1 - col] = on[row][col]   # mirror
            bit += 1

    px = [glow] * (SIZE * SIZE)
    # subtle round-ish frame in the class color
    for y in range(SIZE):
        for x in range(SIZE):
            edge = min(x, y, SIZE - 1 - x, SIZE - 1 - y)
            if edge < 3:
                px[y * SIZE + x] = mix(bg, fg, 0.5)
    # draw cells
    for row in range(GRID):
        for col in range(GRID):
            if not on[row][col]:
                continue
            x0 = MARGIN + col * CELL
            y0 = MARGIN + row * CELL
            for y in range(y0, y0 + CELL):
                base = y * SIZE
                for x in range(x0, x0 + CELL):
                    px[base + x] = fg
    return px


n = 0
for m in R["members"]:
    png(AGENTS / f"{slug(m['name'])}.png", SIZE, essence(m))
    n += 1
    print(f"{slug(m['name']):16} essence -> {m['class']}")

print(f"\nwrote {n} essence sigils (pure stdlib PNG, deterministic per ACI)")
