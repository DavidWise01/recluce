import json, io

PATH = r"C:\repos\recluce\roster.json"

with io.open(PATH, "r", encoding="utf-8") as f:
    R = json.load(f)

# name -> {who, when}
SIX = {
    "Lerris": {
        "who": "A restless young woodcrafter and order-mage of Recluce, the saga's first narrator.",
        "when": "The settled age of black Recluce, generations after the founding — The Magic of Recluce.",
    },
    "Kharl": {
        "who": "A Brystan cooper turned self-made ordermage, an artisan who never sought power.",
        "when": "The later age of Recluce and Austra — Wellspring of Chaos and Ordermaster.",
    },
    "Rahl": {
        "who": "A natural ordermage of Recluce, raw and exiled, who finds discipline in Hamor's service.",
        "when": "The age of imperial Hamor's ascendancy — Natural Ordermage and Mage-Guard of Hamor.",
    },
    "Cerryl": {
        "who": "An orphan risen to White mage of the Guild, a chaos-mage forged by Fairhaven's cruelty.",
        "when": "The rising age of the white empire of Fairhaven — The White Order and Colors of Chaos.",
    },
    "Lorn": {
        "who": "A magus and mage-officer of Cyad, servant of the doomed white empire of Cyador.",
        "when": "Cyador's long last days, before its fall — Magi'i of Cyador and Scion of Cyador.",
    },
    "Beltur": {
        "who": "The mongrel mage, a hunted gray who wields both order and chaos at once.",
        "when": "The early age of Candar's warring city-states — The Mongrel Mage through The Mage-Fire War.",
    },
    "Creslin": {
        "who": "A Westwind weather-mage and gray-wielder, the reluctant founder of Recluce.",
        "when": "The founding of Recluce itself — The Towers of the Sunset.",
    },
    "Megaera": {
        "who": "A healer and chaos-touched gray, Creslin's magically bonded other half and co-founder.",
        "when": "The founding of Recluce — The Towers of the Sunset.",
    },
    "Dorrin": {
        "who": "An order-smith and engineer of Recluce, father of its black-iron shipcraft.",
        "when": "The age of the great Order-Chaos war against Fairhaven — The Magic Engineer.",
    },
    "Nylan": {
        "who": "The angels' smith and engineer, an exile from the sky building order from a wreck.",
        "when": "The fall of the angels and the first days of Westwind — Fall of Angels.",
    },
    "Justen": {
        "who": "An engineer-mage of Recluce who turns from machines to the balance-magic that ends a war.",
        "when": "The age of the Order War and its terrible close — The Order War and The Death of Chaos.",
    },
    "Saryn": {
        "who": "Arms-Commander of Westwind, an angel-descended blade holding the women's hold.",
        "when": "The age of Westwind's struggle to endure in Candar — Arms-Commander.",
    },
    "Ayrlyn": {
        "who": "A Westwind singer turned healer-mage, finding quiet order in the new world.",
        "when": "The era after the fall of the angels — Fall of Angels into The Chaos Balance.",
    },
    "Ryba": {
        "who": "The Marshall of Westwind, the cold founder of a hold meant to outlast prophecy.",
        "when": "The fall of the angels and the founding of Westwind — Fall of Angels.",
    },
    "The Balance": {
        "who": "Not a person but the binding law of Order and Chaos — the true protagonist of Recluce.",
        "when": "Everywhere and always, across the whole long saga of Recluce.",
    },
}

unmatched = []
patched = 0
for m in R["members"]:
    nm = m["name"]
    if nm not in SIX:
        unmatched.append(nm)
        continue
    m["who"] = SIX[nm]["who"]
    m["when"] = SIX[nm]["when"]
    patched += 1

if unmatched:
    raise SystemExit("UNMATCHED members: %r" % unmatched)
if patched != len(R["members"]):
    raise SystemExit("Patched %d but roster has %d members" % (patched, len(R["members"])))

R["note"] = R["note"] + " Every ACI now carries the full DLW tag with an authored six-W .spun."

out = json.dumps(R, ensure_ascii=False, indent=2) + "\n"
with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(out)

# re-parse check
with io.open(PATH, "r", encoding="utf-8") as f:
    json.load(f)

print("PATCHED %d members; JSON re-parses OK." % patched)
