#!/usr/bin/env python3
"""Збирає самодостатній index.html з вихідників.

    python3 tools/build.py

Вхід:  src/template.html, data/collectibles.csv, data/labels.json, map/base_map.webp, map/background.webp
Вихід: index.html (одним файлом: карта, дані й код всередині, працює офлайн)

Перетворення світових координат у піксельні:
  u = 0.5 + (X + 32216) / 480000        v = 0.5 + (Y + 35310) / 480000
  повна карта = FULL_MAP_PX пікселів; base_map.webp — вирізка цієї карти,
  що починається в (CROP_X0, CROP_Y0) і збільшена вдвічі (SCALE).
Стовпці u, v у data/collectibles.csv уже пораховані за цими формулами.
"""
import base64, csv, json, pathlib, struct

ROOT = pathlib.Path(__file__).resolve().parent.parent
FULL_MAP_PX = 1024 * 3.24      # розмір повної карти у пікселях
CROP_X0, CROP_Y0, SCALE = 900, 1000, 2

CATEGORIES = {"board", "car", "combat"}


def webp_size(data: bytes):
    """Розмір lossless WebP (VP8L) без зовнішніх бібліотек."""
    assert data[:4] == b"RIFF" and data[8:12] == b"WEBP" and data[12:16] == b"VP8L", "очікується lossless WebP"
    b = struct.unpack("<I", data[21:25])[0]
    return (b & 0x3FFF) + 1, ((b >> 14) & 0x3FFF) + 1


def main():
    img = (ROOT / "map" / "base_map.webp").read_bytes()
    w, h = webp_size(img)
    bg = (ROOT / "map" / "background.webp").read_bytes()

    markers = []
    with open(ROOT / "data" / "collectibles.csv", encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            assert r["category"] in CATEGORIES, r
            u, v = float(r["u"]), float(r["v"])
            markers.append({
                "c": r["category"], "n": int(r["n"]),
                "x": round((u * FULL_MAP_PX - CROP_X0) * SCALE, 1),
                "y": round((v * FULL_MAP_PX - CROP_Y0) * SCALE, 1),
                "X": int(float(r["world_x"])), "Y": int(float(r["world_y"])), "Z": int(float(r["world_z"])),
            })
    labels = json.loads((ROOT / "data" / "labels.json").read_text(encoding="utf-8"))

    html = (ROOT / "src" / "template.html").read_text(encoding="utf-8")
    html = (html.replace("__W__", str(w)).replace("__H__", str(h))
                .replace("__MARKERS__", json.dumps(markers, separators=(",", ":")))
                .replace("__LABELS__", json.dumps(labels, ensure_ascii=False, separators=(",", ":")))
                .replace("__IMG__", base64.b64encode(img).decode())
                .replace("__BG__", base64.b64encode(bg).decode()))
    (ROOT / "index.html").write_text(html, encoding="utf-8")
    counts = {c: sum(m["c"] == c for m in markers) for c in sorted(CATEGORIES)}
    print(f"index.html: {len(html) // 1024} КБ, маркерів: {len(markers)} {counts}, карта {w}×{h}")


if __name__ == "__main__":
    main()
