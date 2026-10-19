# **Serves:** research PLAY-dClosedLoop-1
"""Check architecture v2's preset table against its policy catalogue: every presettable key assigned
in every preset, no excluded key present, every enumerated value allowed, and the `standard` column
equal to the catalogue's defaults. Reads one file; writes nothing; exit 1 on any finding.

Promoted from the session's scratchpad (`preset_check_canonical.py`) for the whole-design audit's Stage 0, which runs it in any tree;
byte for byte its scratch original but for this note and the Serves line.
"""
import re
import sys

text = open(sys.argv[1], encoding="utf-8").read()


def section(tag):
    m = re.search(r"^## \[" + re.escape(tag) + r"\].*?(?=^## \[|\Z)", text, flags=re.M | re.S)
    return m.group(0) if m else ""


def rows(block, ncols):
    out = []
    for line in block.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == ncols and cells[0].startswith("`"):
            out.append([cells[0].strip("`")] + cells[1:])
    return out


STAGES = ["plan", "design", "build", "test", "deploy", "maintain"]
never = re.search(r"Presets never touch (.*?):", section("presets"), flags=re.S)
if not never:
    sys.exit("v2 [presets] states no 'Presets never touch' list")
EXCLUDED = set(re.findall(r"`([^`]+)`", never.group(1))) | {"preset"}
if "the floor" in never.group(1):
    EXCLUDED.add("floor")
head = next((ln for ln in section("presets").splitlines() if ln.startswith("| Key |")), "")
NAMES = [c.strip().split(" ")[0] for c in head.strip().strip("|").split("|")[1:]]
catalogue = {}
for key, allowed, default, _src, _owner in rows(section("policies"), 5):   # the Owner column since PM-10
    keys = [key.replace("<stage>", s) for s in STAGES] if key == "review.<stage>" else [key]
    for k in keys:
        if key == "review.<stage>":
            d = "owed" if k == "review.build" else "opt-in"
        else:
            d = default
        catalogue[k] = (allowed, d)

presets = {r[0]: r[1:] for r in rows(section("presets"), 5)}
findings = []
expected = {k for k in catalogue if k not in EXCLUDED}
for k in sorted(expected - set(presets)):
    findings.append(f"presettable key missing from the preset table: {k}")
for k in sorted(set(presets) - expected):
    findings.append(f"preset table names a key that is excluded or not in the catalogue: {k}")

FREE = re.compile(r"seconds|hours|days|set of named|each cap|any subset|the role efforts|the models the harness adapter offers|a repo-declared|a retry count|a share of the window|a round count|a word range|a route-back count|KB per role")
for k, vals in presets.items():
    if k not in catalogue:
        continue
    allowed_text, default = catalogue[k]
    if not FREE.search(allowed_text):
        allowed = {a.strip() for a in re.split(r"[,;]", allowed_text) if a.strip()}
        for name, v in zip(NAMES, vals):
            if v not in allowed:
                findings.append(f"{k}: {name} = '{v}' is not an allowed value ({allowed_text})")
        if vals[1] != default:
            findings.append(f"{k}: standard = '{vals[1]}' but the catalogue default is '{default}'")

# The pair rules, each (higher, lower) in every preset, skipped, and said so, before both keys exist: the away pass's
# (its closing review, M1), the deprecation window at least the currency budget, so an adopter inside its budget never
# meets a removed surface; and the parked debt's review's, the round ceiling at least the design review's fixed count.
PAIRS = [("install.deprecation-window", "currency.max-behind"), ("review.max-rounds", "review.design.round-count")]
for PAIR in PAIRS:
    if all(k in presets for k in PAIR):
        for name, w, b in zip(NAMES, presets[PAIR[0]], presets[PAIR[1]]):
            if w.isdigit() and b.isdigit() and int(w) < int(b):
                findings.append(f"pair rule: {name} sets {PAIR[0]} {w} under {PAIR[1]} {b}")
    else:
        print(f"pair rule {PAIR[0]} >= {PAIR[1]}: not checked, a key is absent")
print(f"catalogue keys {len(catalogue)} · presettable {len(expected)} · preset rows {len(presets)}")
print("\n".join(findings) if findings else "no findings")
sys.exit(1 if findings else 0)
