#!/usr/bin/env python3
"""
Caer Hollow Sewer Map Generator
Session 17 — "The Deep Below"

Generates dungeon map images for each of the four sewer zones.
Rooms are labelled with codes (U1-A, 1-1, etc.) to cross-reference with
the Caer Hollow Sewers.md Obsidian note.

Requires: pip install Pillow

Usage:
  python sewer_gen.py                         # all zones, random seed
  python sewer_gen.py --seed 42               # reproducible output
  python sewer_gen.py --z1-rooms 4 8          # more rooms in zone 1
  python sewer_gen.py --z2-rooms 6 10 --z3-rooms 2 5
  python sewer_gen.py --zone 3 --cell 28      # single zone, bigger cells
  python sewer_gen.py --output ./maps         # save to a specific folder
"""

import argparse
import math
import os
import random
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Pillow is required.  Run:  pip install Pillow")


# ─── Zone data ──────────────────────────────────────────────────────────────
# Colours are (R, G, B) tuples.
# gW / gH are the base grid dimensions in cells; the script auto-scales them
# upward when more rooms are requested than the base layout can comfortably fit.

ZONES = {
    1: dict(
        id=1,
        name="Zone 1 — Upper Channels",
        sub="8ft ceiling · ankle-deep water · worn limestone",
        gW=36, gH=32,
        bg=(19, 18, 16),   grid=(28, 26, 23),   corr=(42, 39, 32),
        r_fill=(50, 47, 42),   r_border=(95, 94, 90),
        u_fill=(58, 54, 48),   u_border=(180, 178, 169),
        l_pri=(211, 209, 199), l_sec=(138, 137, 130), accent=(180, 178, 169),
        trans="Stone Arch → Zone 2",
        unique=[
            dict(id="U1-A", name="Entry\nChamber",  w=4, h=4),
            dict(id="U1-B", name="Modified\nWall",  w=4, h=3),
            dict(id="U1-C", name="Rat\nEncounter",  w=6, h=5),
        ],
        pool=[
            dict(name="Maintenance\nAlcove",     w=3, h=3),
            dict(name="Overflow\nChamber",       w=4, h=4),
            dict(name="Collapsed\nSection",      w=4, h=3),
            dict(name="Junction\nPassage",       w=3, h=6),
            dict(name="Rat Den",                 w=3, h=3),
            dict(name="Drainage\nPit",           w=2, h=3),
            dict(name="Guard Post\n(Abandoned)", w=3, h=3),
            dict(name="Plain\nPassage",          w=2, h=5),
        ],
        r_min=2, r_max=5,
    ),
    2: dict(
        id=2,
        name="Zone 2 — Modified Tunnels",
        sub="12ft ceiling · runic bracketing · bioluminescent fungus",
        gW=38, gH=36,
        bg=(12, 16, 24),   grid=(20, 28, 38),   corr=(28, 42, 60),
        r_fill=(33, 49, 68),   r_border=(46, 90, 138),
        u_fill=(28, 48, 72),   u_border=(133, 183, 235),
        l_pri=(181, 212, 244), l_sec=(55, 122, 221), accent=(55, 122, 221),
        trans="Descent Passage → Zone 3",
        unique=[
            dict(id="U2-A", name="Croc\nChannel",  w=6, h=8),
            dict(id="U2-B", name="Undead\nPatrol", w=4, h=9),
        ],
        pool=[
            dict(name="Fungus\nChamber",       w=4, h=4),
            dict(name="Tool\nStorage",         w=3, h=3),
            dict(name="Collapsed\nSub-level",  w=3, h=3),
            dict(name="Rune Study\nAlcove",    w=3, h=3),
            dict(name="Dead\nAnimal",          w=2, h=2),
            dict(name="Evidence\nChest",       w=2, h=2),
            dict(name="Flooded\nPassage",      w=3, h=6),
            dict(name="Worker's\nRefuge",      w=4, h=4),
            dict(name="Warded\nJunction",      w=3, h=4),
            dict(name="Empty\nCorridor",       w=2, h=5),
        ],
        r_min=4, r_max=7,
    ),
    3: dict(
        id=3,
        name="Zone 3 — Construction Site",
        sub="20ft ceiling · runes floor-to-ceiling · iron channels",
        gW=30, gH=28,
        bg=(20, 15, 4),    grid=(32, 25, 10),   corr=(45, 36, 16),
        r_fill=(56, 44, 20),   r_border=(138, 92, 16),
        u_fill=(64, 50, 20),   u_border=(239, 159, 39),
        l_pri=(250, 199, 117), l_sec=(186, 117, 23), accent=(239, 159, 39),
        trans="Doorway (no door) → Zone 4",
        unique=[
            dict(id="U3-A", name="Construction\nChamber", w=7, h=5),
            dict(id="U3-B", name="Evidence\nRoom",        w=4, h=4),
        ],
        pool=[
            dict(name="Material\nStaging",    w=4, h=4),
            dict(name="Unfinished\nChamber",  w=5, h=5),
            dict(name="Foreman's\nWorkspace", w=3, h=3),
            dict(name="Survey\nCollapse",     w=3, h=4),
            dict(name="Sealed\nAlcove",       w=2, h=2),
            dict(name="Rune\nCorridor",       w=2, h=5),
        ],
        r_min=1, r_max=3,
    ),
    4: dict(
        id=4,
        name="Zone 4 — Anchor Chamber",
        sub="circular · nothing grows here · node at centre",
        gW=18, gH=16,
        bg=(3, 14, 8),     grid=(7, 18, 12),    corr=(10, 24, 14),
        r_fill=(14, 40, 26),   r_border=(13, 92, 56),
        u_fill=(12, 36, 24),   u_border=(29, 158, 117),
        l_pri=(159, 225, 203), l_sec=(93, 202, 165), accent=(29, 158, 117),
        trans=None,
        unique=[
            dict(id="U4-A", name="Anchor\nChamber", w=8, h=8, circular=True),
        ],
        pool=[], r_min=0, r_max=0,
    ),
}


# ─── Font helpers ────────────────────────────────────────────────────────────

def find_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Search common OS font paths for a monospace face, fall back to default."""
    if sys.platform == "win32":
        base = os.environ.get("WINDIR", "C:/Windows") + "/Fonts/"
        candidates = [
            base + ("consolab.ttf" if bold else "consola.ttf"),
            base + ("courbd.ttf"   if bold else "cour.ttf"),
            base + ("arialbd.ttf"  if bold else "arial.ttf"),
        ]
    elif sys.platform == "darwin":
        candidates = [
            f"/Library/Fonts/Courier New{' Bold' if bold else ''}.ttf",
            "/System/Library/Fonts/Courier.ttc",
            f"/Library/Fonts/Arial{' Bold' if bold else ''}.ttf",
        ]
    else:
        sfx = "-Bold" if bold else "-Regular"
        dirs = [
            "/usr/share/fonts/truetype/dejavu/",
            "/usr/share/fonts/truetype/liberation/",
            "/usr/share/fonts/truetype/ubuntu/",
            "/usr/share/fonts/truetype/",
            "/usr/share/fonts/",
            os.path.expanduser("~/.fonts/"),
        ]
        stems = ["DejaVuSansMono", "LiberationMono", "UbuntuMono"]
        candidates = [
            d + stem + variant
            for d in dirs
            for stem in stems
            for variant in (sfx + ".ttf", ".ttf")
        ]

    for path in candidates:
        if os.path.isfile(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass

    try:
        return ImageFont.load_default(size=size)   # Pillow ≥ 10.1
    except TypeError:
        return ImageFont.load_default()            # Pillow < 10.1


def text_dims(font, text: str):
    """Return (width, height) for the given text rendered in font."""
    try:
        bb = font.getbbox(text)                    # Pillow ≥ 8.0
        return bb[2] - bb[0], bb[3] - bb[1]
    except AttributeError:
        try:
            return font.getsize(text)              # Pillow < 8.0 (deprecated but works)
        except Exception:
            sz = getattr(font, "size", 8)
            return len(text) * max(4, sz // 2), sz


def draw_text_centred(draw, cx: int, y: int, text: str, font, fill):
    """Draw text horizontally centred at cx, top edge at y."""
    w, _ = text_dims(font, text)
    draw.text((cx - w // 2, y), text, fill=fill, font=font)


# ─── Map generation ──────────────────────────────────────────────────────────

def build_map(zone: dict, r_min: int, r_max: int, seed: int):
    """
    Place all rooms on the grid and build L-shaped corridor connections.
    Unique rooms are always included; random rooms are drawn from the pool.
    If r_max exceeds the pool size the pool is cycled (duplicated room types
    get distinct IDs, e.g. 1-7 may share a name with 1-1 but is separate).

    Returns:
        placed    – list of room dicts with .x / .y populated
        corridors – list of (x1,y1,x2,y2) grid-unit segments
        gW, gH    – final grid dimensions (may exceed zone base if auto-scaled)
    """
    rng  = random.Random(seed)
    gW   = zone["gW"]
    gH   = zone["gH"]
    pool = zone["pool"]

    # Pick how many random rooms
    n_random = (r_min if r_min == r_max
                else r_min + int(rng.random() * (r_max - r_min + 1)))

    # Extend pool by cycling if needed
    pool_ext = (pool * (n_random // max(len(pool), 1) + 1))[:n_random] if pool else []
    rng.shuffle(pool_ext)
    randoms = [
        {**r, "id": f"{zone['id']}-{i+1}", "is_random": True}
        for i, r in enumerate(pool_ext)
    ]
    uniques = [{**u, "is_unique": True} for u in zone["unique"]]

    # Interleave: U [R R?] U [R R?] …
    all_rooms: list[dict] = []
    ui = ri = 0
    while ui < len(uniques) or ri < len(randoms):
        if ui < len(uniques):
            all_rooms.append(dict(uniques[ui])); ui += 1
        stride = 1 + (1 if ri < len(randoms) - 1 and rng.random() > 0.4 else 0)
        for _ in range(stride):
            if ri < len(randoms):
                all_rooms.append(dict(randoms[ri])); ri += 1

    # Auto-scale the grid so there is enough space for all rooms
    u_area = sum((r["w"] + 2) * (r["h"] + 2) for r in uniques)
    r_area = sum((r["w"] + 2) * (r["h"] + 2) for r in randoms)
    needed = (u_area + r_area) * 3.4
    if needed > gW * gH:
        scale = math.sqrt(needed / (gW * gH))
        gW    = int(gW * scale) + 2
        gH    = int(gH * scale) + 2

    # Always leave a few blank cells at the bottom for the transition marker
    gH += 3

    # --- Placement ---
    grid = [[False] * gW for _ in range(gH)]

    def fits(x, y, w, h) -> bool:
        if x < 1 or y < 1 or x + w >= gW - 1 or y + h >= gH - 1:
            return False
        for dy in range(-1, h + 1):
            for dx in range(-1, w + 1):
                gy, gx = y + dy, x + dx
                if 0 <= gy < gH and 0 <= gx < gW and grid[gy][gx]:
                    return False
        return True

    def mark(x, y, w, h):
        for dy in range(h):
            for dx in range(w):
                if y + dy < gH and x + dx < gW:
                    grid[y + dy][x + dx] = True

    placed: list[dict] = []
    N = len(all_rooms)

    for i, room in enumerate(all_rooms):
        # Target y band — spreads rooms from top to bottom
        t  = 0.5 if N == 1 else i / (N - 1)
        tY = max(2, int(t * (gH - room["h"] - 4)) + 2)
        spread = max(3, gH // (N + 1))

        placed_ok = False
        for attempt in range(1000):
            x  = 1 + int(rng.random() * max(1, gW - room["w"] - 2))
            dy = (int((rng.random() - 0.5) * spread * 2) if attempt < 350
                  else int((rng.random() - 0.5) * gH))
            y  = max(1, min(gH - room["h"] - 1, tY + dy))
            if fits(x, y, room["w"], room["h"]):
                room["x"] = x; room["y"] = y
                mark(x, y, room["w"], room["h"])
                placed.append(room); placed_ok = True; break

        if not placed_ok:
            if room.get("is_unique"):
                # Required rooms get a brute-force second pass
                for _ in range(10_000):
                    x = 1 + int(rng.random() * max(1, gW - room["w"] - 2))
                    y = 1 + int(rng.random() * max(1, gH - room["h"] - 2))
                    if fits(x, y, room["w"], room["h"]):
                        room["x"] = x; room["y"] = y
                        mark(x, y, room["w"], room["h"])
                        placed.append(room); placed_ok = True; break
                if not placed_ok:
                    # Absolute fallback — place without checking (rare edge case)
                    room["x"] = 1; room["y"] = tY
                    placed.append(room)
            # Random rooms that truly will not fit are silently skipped

    # --- L-shaped corridors ---
    corridors: list[tuple] = []
    for i in range(1, len(placed)):
        a, b = placed[i - 1], placed[i]
        if a.get("x") is None or b.get("x") is None:
            continue
        ax = a["x"] + a["w"] // 2;  ay = a["y"] + a["h"] // 2
        bx = b["x"] + b["w"] // 2;  by = b["y"] + b["h"] // 2
        if rng.random() > 0.5:
            corridors.append((ax, ay, bx, ay))
            corridors.append((bx, ay, bx, by))
        else:
            corridors.append((ax, ay, ax, by))
            corridors.append((ax, by, bx, by))

    return placed, corridors, gW, gH


# ─── Drawing ─────────────────────────────────────────────────────────────────

def draw_dashed_hline(draw, x0: int, y: int, x1: int, fill, dash=5, gap=4):
    """Draw a dashed horizontal line."""
    x = x0
    while x < x1:
        draw.line([(x, y), (min(x + dash, x1), y)], fill=fill, width=1)
        x += dash + gap


def render_zone(
    zone: dict,
    placed: list,
    corridors: list,
    gW: int,
    gH: int,
    cell: int,
    seed: int,        # shown in the watermark — pass the user-facing base seed
) -> Image.Image:
    """Render one zone map and return a PIL Image."""
    CW, CH = gW * cell, gH * cell
    img  = Image.new("RGB", (CW, CH), zone["bg"])
    draw = ImageDraw.Draw(img)

    # ── Grid dots ──
    for x in range(0, CW + 1, cell):
        for y in range(0, CH + 1, cell):
            draw.rectangle([(x, y), (x + 1, y + 1)], fill=zone["grid"])

    # ── Corridors (drawn first so rooms render on top) ──
    for (x1, y1, x2, y2) in corridors:
        if y1 == y2:   # horizontal
            draw.rectangle(
                [(min(x1, x2) * cell,       y1 * cell),
                 ((max(x1, x2) + 1) * cell, (y1 + 1) * cell)],
                fill=zone["corr"])
        else:          # vertical
            draw.rectangle(
                [(x1 * cell,       min(y1, y2) * cell),
                 ((x1 + 1) * cell, (max(y1, y2) + 1) * cell)],
                fill=zone["corr"])

    # ── Rooms ──
    for room in placed:
        if room.get("x") is None:
            continue
        px, py = room["x"] * cell, room["y"] * cell
        pw, ph = room["w"] * cell, room["h"] * cell
        is_u   = room.get("is_unique", False)
        fill   = zone["u_fill"]   if is_u else zone["r_fill"]
        border = zone["u_border"] if is_u else zone["r_border"]
        bw     = 2 if is_u else 1

        if room.get("circular"):
            cx, cy = px + pw // 2, py + ph // 2
            rad    = min(pw, ph) // 2 - 2
            draw.ellipse(
                [(cx - rad, cy - rad), (cx + rad, cy + rad)],
                fill=fill, outline=border, width=bw)
            # Lattice node dot at centre
            nr = max(2, int(rad * 0.2))
            draw.ellipse(
                [(cx - nr, cy - nr), (cx + nr, cy + nr)], fill=border)
            # Radial channels
            for deg in range(0, 360, 45):
                a   = math.radians(deg)
                rx1 = int(cx + math.cos(a) * rad * 0.28)
                ry1 = int(cy + math.sin(a) * rad * 0.28)
                rx2 = int(cx + math.cos(a) * rad * 0.88)
                ry2 = int(cy + math.sin(a) * rad * 0.88)
                draw.line([(rx1, ry1), (rx2, ry2)], fill=border, width=1)
        else:
            draw.rectangle(
                [(px, py), (px + pw - 1, py + ph - 1)],
                fill=fill, outline=border, width=bw)
            # Iron channels across U3-A (the construction chamber)
            if room.get("id") == "U3-A":
                step = max(8, cell // 2)
                for ly in range(py + step, py + ph - 3, step):
                    draw_dashed_hline(
                        draw, px + 4, ly, px + pw - 4,
                        fill=zone["u_border"], dash=5, gap=4)

        # ── Room labels ──
        min_d   = min(pw, ph)
        id_sz   = max(8,  min(cell - 2,  int(min_d * 0.27)))
        nm_sz   = max(6,  min(cell - 4,  int(min_d * 0.18)))
        font_id = find_font(id_sz, bold=True)
        font_nm = find_font(nm_sz, bold=False)
        cx_lbl  = px + pw // 2

        draw_text_centred(draw, cx_lbl, py + 3, room["id"], font_id, zone["l_pri"])

        # Only show name text if the room is tall / wide enough to read
        if ph > int(cell * 1.8) and pw > cell + 6:
            ny = py + 3 + id_sz + 3
            for line in (room.get("name") or "").split("\n"):
                draw_text_centred(draw, cx_lbl, ny, line, font_nm, zone["l_sec"])
                ny += nm_sz + 2

    # ── Entry marker above first room ──
    font_marker = find_font(max(8, int(cell * 0.55)), bold=True)
    if placed and placed[0].get("x") is not None:
        first  = placed[0]
        cx     = (first["x"] + first["w"] // 2) * cell
        ty     = first["y"] * cell
        lbl    = "▲  ENTRY"
        w, h   = text_dims(font_marker, lbl)
        tx     = max(2, min(CW - w - 2, cx - w // 2))  # clamp to image
        draw.text((tx, ty - h - 4), lbl, fill=zone["accent"], font=font_marker)

    # ── Transition marker below last room ──
    if zone.get("trans") and placed:
        last = placed[-1]
        if last.get("x") is not None:
            cx    = (last["x"] + last["w"] // 2) * cell
            by_px = (last["y"] + last["h"]) * cell
            lbl   = f"▼  {zone['trans']}"
            w, _  = text_dims(font_marker, lbl)
            tx    = max(2, min(CW - w - 2, cx - w // 2))  # clamp to image
            draw.text((tx, by_px + 4), lbl, fill=zone["accent"], font=font_marker)

    # ── Top-right watermark (avoids clashing with bottom transition text) ──
    font_title = find_font(max(9,  cell // 2),      bold=True)
    font_small = find_font(max(7,  cell // 3 + 1),  bold=False)
    n_vis  = sum(1 for r in placed if r.get("x") is not None)
    sub    = f"seed {seed}  ·  {n_vis} rooms"
    tw, th = text_dims(font_title, zone["name"])
    sw, sh = text_dims(font_small, sub)
    pad    = 6
    max_w  = max(tw, sw)
    # Opaque background so text reads cleanly over any nearby room
    draw.rectangle([(CW - max_w - pad * 2, 0), (CW, th + sh + pad * 2 + 4)],
                   fill=zone["bg"])
    draw.text((CW - tw - pad, pad),          zone["name"], fill=zone["l_pri"], font=font_title)
    draw.text((CW - sw - pad, pad + th + 3), sub,          fill=zone["l_sec"], font=font_small)

    return img


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        prog="sewer_gen.py",
        description="Caer Hollow sewer map generator — Session 17: The Deep Below",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
examples:
  python sewer_gen.py
  python sewer_gen.py --seed 42 --cell 24
  python sewer_gen.py --z1-rooms 4 8 --z2-rooms 6 10
  python sewer_gen.py --zone 2 --z2-rooms 8 12
  python sewer_gen.py --output ./maps --seed 1337
  python sewer_gen.py --cell 32 --output ./print_maps
""",
    )
    ap.add_argument(
        "--seed", type=int, default=None,
        help="RNG seed for reproducible output (default: random)")
    ap.add_argument(
        "--zone", type=int, choices=[1, 2, 3, 4], default=None,
        help="Generate a single zone (default: all 4)")
    ap.add_argument(
        "--cell", type=int, default=20,
        help="Pixels per grid cell (default: 20 — try 24-32 for printing)")
    ap.add_argument(
        "--output", type=str, default=".",
        help="Output directory (default: current directory)")
    ap.add_argument(
        "--z1-rooms", type=int, nargs=2, metavar=("MIN", "MAX"), default=[6, 10],
        help="Zone 1 random room count range (default: 2 5)")
    ap.add_argument(
        "--z2-rooms", type=int, nargs=2, metavar=("MIN", "MAX"), default=[6, 12],
        help="Zone 2 random room count range (default: 4 7)")
    ap.add_argument(
        "--z3-rooms", type=int, nargs=2, metavar=("MIN", "MAX"), default=[3, 5],
        help="Zone 3 random room count range (default: 1 3)")
    args = ap.parse_args()

    # Validate room ranges
    for label, vals in [
        ("--z1-rooms", args.z1_rooms),
        ("--z2-rooms", args.z2_rooms),
        ("--z3-rooms", args.z3_rooms),
    ]:
        if vals[0] < 0:
            ap.error(f"{label}: MIN must be ≥ 0")
        if vals[0] > vals[1]:
            ap.error(f"{label}: MIN must be ≤ MAX")

    base_seed = args.seed if args.seed is not None else random.randint(1, 99_999)
    out_dir   = Path(args.output)
    out_dir.mkdir(parents=True, exist_ok=True)

    room_cfg = {
        1: args.z1_rooms,
        2: args.z2_rooms,
        3: args.z3_rooms,
        4: [0, 0],          # Zone 4 is always a single fixed room
    }
    zones_to_run = [args.zone] if args.zone else [1, 2, 3, 4]

    print(f"Seed: {base_seed}  |  Cell size: {args.cell}px")
    print()

    saved = []
    for zid in zones_to_run:
        zone       = ZONES[zid]
        r_min, r_max = room_cfg[zid]

        # Each zone gets a deterministic derivative of the base seed
        z_seed = (base_seed + zid * 7_919) % 100_000

        placed, corridors, gW, gH = build_map(zone, r_min, r_max, z_seed)
        img = render_zone(zone, placed, corridors, gW, gH, args.cell, base_seed)

        slug  = zone["name"].split("—")[1].strip().lower().replace(" ", "_")
        fname = f"zone{zid}_{slug}.png"
        path  = out_dir / fname
        img.save(path)
        saved.append(path)

        n_unique = sum(1 for r in placed if r.get("is_unique"))
        n_rand   = sum(1 for r in placed if r.get("is_random"))
        ids      = [r["id"] for r in placed if r.get("x") is not None]

        print(f"Zone {zid}  {zone['name']}")
        print(f"  Grid: {gW}×{gH}  |  "
              f"{len(placed)} rooms ({n_unique} unique, {n_rand} random)")
        print(f"  Layout: {', '.join(ids)}")
        print(f"  Saved → {path.resolve()}")
        print()

    print(f"Done.  {len(saved)} file(s) in {Path(args.output).resolve()}")


if __name__ == "__main__":
    main()