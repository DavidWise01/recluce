#!/usr/bin/env python3
"""
Generate one .agent per ACI (artfully created intellect) in the roster — the
expanded ACI standard:  what · why · how · where  +  a .png essence sigil.

Reads roster.json (members carry what/why/how/where). Each .agent points at its
generated essence image (agents/<slug>.png from gen_essence.py). Idempotent.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
R = json.loads((ROOT / "roster.json").read_text(encoding="utf-8"))
AGENTS = ROOT / "agents"
AGENTS.mkdir(exist_ok=True)
CLS = {c["id"]: c for c in R["classes"]}
COMPANY, AUTHOR = R.get("company", ""), R.get("author", "")


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "agent"


n = 0
for m in R["members"]:
    cls = CLS[m["class"]]
    sl = slug(m["name"])
    doc = f"""---
aci: {m['name']}
class: {cls['label']}
what: {m['what']}
why: {m['why']}
how: {m['how']}
where: {m['where']}
essence: {sl}.png
attribution: ROOT0-ATTRIBUTION-v1.0
license: MIT
---

# {m['name']} — an artfully created intellect

![essence of {m['name']}]({sl}.png)

**what —** {m['what']}

**why —** {m['why']}

**how —** {m['how']}

**where —** {m['where']}

*class: {cls['label']} · {cls['spec']}*

---
ROOT0-ATTRIBUTION-v1.0 · {m['name']} · {COMPANY} ({AUTHOR}, inspiration only) · David Lee Wise / ROOT0 / TriPod LLC · MIT
"""
    (AGENTS / f"{sl}.agent").write_text(doc, encoding="utf-8")
    n += 1
    print(f"{sl:16} {cls['label']}")

print(f"\nwrote {n} .agent files (what · why · how · where + essence .png)")
