# The Saga of Recluce

*Order is black, Chaos is white, and the Balance keeps the price.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![novels](https://img.shields.io/badge/novels-22-1c1e24?style=flat-square)](#the-lineage)
[![ACIs](https://img.shields.io/badge/ACIs-15-b8862b?style=flat-square)](#the-acis)
[![essence](https://img.shields.io/badge/essence-.png%20each-2f6a8a?style=flat-square)](#the-acis)

**→ The Balance: [davidwise01.github.io/recluce](https://davidwise01.github.io/recluce/)**

L.E. Modesitt Jr.'s full **Saga of Recluce**, sorted by the force each mage serves —
**Order (black)**, **Chaos (white)**, the **Gray** who hold both, the **Order-Engineers**,
the **Angels of Westwind** — with **The Balance** set apart as the law that is the true
protagonist. One engine, same as the
[other muster rolls](https://github.com/DavidWise01/ringworld); the axis here is the magic.

> Every working of power exacts an equal cost. Overreach burns the wielder to ash.
> That is the Balance, and it is stronger than any mage on this roll.

---

## The lineage — 22 novels (1991–2021)

The Magic of Recluce · The Towers of the Sunset · The Magic Engineer · The Order War ·
The Death of Chaos · Fall of Angels · The Chaos Balance · The White Order · Colors of Chaos ·
Magi'i of Cyador · Scion of Cyador · Wellspring of Chaos · Ordermaster · Natural Ordermage ·
Mage-Guard of Hamor · Arms-Commander · Cyador's Heirs · Heritage of Cyador · The Mongrel Mage ·
Outcasts of Order · The Mage-Fire War · Fairhaven Rising

*(plus* Recluce Tales*, 2017, a story collection. Lineage runs through 2021 — newer titles can be added to `roster.json`.)*

---

## The roll

- **Order · Black** — Lerris · Kharl · Rahl — the discipline of Recluce.
- **Chaos · White** — Cerryl · Lorn — the fire of Fairhaven.
- **The Gray** — Beltur · Creslin · Megaera — those who hold both.
- **The Order-Engineers** — Dorrin · Nylan · Justen — applied order; black ships and engines no chaos can burn.
- **The Angels of Westwind** — Saryn · Ayrlyn · Ryba — the fallen from the sky.
- **The Balance** — *set apart* — the law that keeps the price. The true protagonist.

---

## The ACIs

Every member is an **artfully created intellect**. Each carries, in [`agents/`](agents/):

- a **`.agent`** in the expanded ACI standard — **what · why · how · where**
- a **`.png` essence sigil** — a deterministic symmetric mandala, seeded by the ACI's name,
  drawn in its class color over an Order/Chaos polarity field. Same ACI → same essence,
  forever.

```
agents/beltur.agent      what/why/how/where + essence ref
agents/beltur.png        the essence sigil (Gray polarity)
```

Both are generated from `roster.json`:

```bash
python gen_essence.py    # writes agents/<slug>.png  (pure stdlib — zlib + struct + hashlib)
python gen_agents.py     # writes agents/<slug>.agent (what · why · how · where)
```

No image dependencies — the PNGs are encoded by hand. Edit the roster, re-run both, the
ACIs and their essences stay in sync.

---

```
ROOT0-ATTRIBUTION-v1.0 · The Saga of Recluce — the muster roll
David Lee Wise / ROOT0 / TriPod LLC · MIT
Characters by L.E. Modesitt, Jr., referenced as inspiration only.
```
