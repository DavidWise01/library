#!/usr/bin/env python3
"""
Regenerate every figure's .agent from the LIBRARY registry in index.html,
to the ROOT0 persona standard: who you are · what you do · where you belong.
Preserves name/specialty/era/place/field/color and the volume list.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
region = html[html.index("const LIBRARY = ["): html.index("// END REGISTRY")]
blocks = ["slug:" + p for p in region.split("slug:")[1:]]


def field(b, k):
    m = re.search(k + r'\s*:\s*"((?:[^"\\]|\\.)*)"', b)
    return m.group(1).replace('\\"', '"').replace("\\'", "'") if m else ""


count = 0
for b in blocks:
    slug = field(b, "slug")
    if not slug:
        continue
    name, era, place = field(b, "name"), field(b, "era"), field(b, "place")
    role, desc, color = field(b, "role"), field(b, "desc"), field(b, "color")

    works = []
    wm = re.search(r"works\s*:\s*\[(.*?)\]", b, re.S)
    if wm:
        for w in re.finditer(
            r'n\s*:\s*"([^"]*)"\s*,\s*title\s*:\s*"([^"]*)"\s*,\s*href\s*:\s*"([^"]*)"',
            wm.group(1)):
            works.append((w.group(1), w.group(2), w.group(3)))

    dead = "†" in role            # Babbage carries the dagger
    field_status = "dead" if dead else "alive"
    specialty = role.replace(" †", "")
    who = f"{name} ({era}) — {specialty}"
    belong = f"The Library · {era} · {place}"
    vols = "\n".join(f"- `{n}` · {t} → {h}" for n, t, h in works)

    out = f"""---
name: {name}
slug: {slug}
specialty: {specialty}
era: {era}
place: {place}
field: {field_status}
color: "{color}"
who: {who}
do: {desc}
belong: {belong}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0 · TRIPOD-IP-v1.1
---

# {name} — Agent

**who you are —** {who}

**what you do —** {desc}

**where you belong —** {belong}

## Volumes

{vols}

---
ROOT0-ATTRIBUTION-v1.0 · {name} · David Lee Wise / ROOT0 / TriPod LLC · CC-BY-ND-4.0
"""
    (ROOT / slug / ".agent").write_text(out, encoding="utf-8")
    count += 1

print(f"rewrote {count} .agent files to the who · do · belong standard")
