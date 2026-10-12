"""Stage one break at a time into a copy of check-arms.py beside it, run its --selftest, report which arms red."""
import os
import subprocess
import sys

SRC = sys.argv[1]
DST = os.path.join(os.path.dirname(SRC), "_ca_break.py")
BREAKS = [
    ("ceiling compare", "        if got > ceil:\n            bad.append(f\"check-arms: {gate_rel} has {got}",
     "        if got > ceil + 1:\n            bad.append(f\"check-arms: {gate_rel} has {got}"),
    ("ceiling date", "        date = next((p for p in rest if DATE_SHAPE_RE.fullmatch(p)), None)",
     "        date = next((p for p in rest if DATE_SHAPE_RE.fullmatch(p)), \"2026-01-01\")"),
    ("ceiling id carried", "        if not check_id_carried(ident, log):\n            bad.append(f\"check-arms: REFUSAL_CEILINGS",
     "        if False:\n            bad.append(f\"check-arms: REFUSAL_CEILINGS"),
    ("family over ceiling", "            elif got > ceil:", "            elif got > ceil + 5:"),
    ("family dead pattern", "            if got == 0:", "            if got == -1:"),
    ("survivor signature", "        elif sv.group(2) not in (", "        elif False and sv.group(2) not in ("),
    ("replay field", "        if not rp:", "        if False:"),
    ("survivor field", "        if not sv:\n", "        if sv is None and False:\n"),
    ("retirement id carried", "        if not check_id_carried(ident, log):\n            bad.append(f\"check-arms: {rel}:{i} names",
     "        if False:\n            bad.append(f\"check-arms: {rel}:{i} names"),
    ("report unbudgeted", "            unbudgeted.append(gate_rel)", "            pass"),
]
text = open(SRC, "rb").read().decode("utf-8")
nl = "\r\n" if "\r\n" in text else "\n"
for label, old, new in BREAKS:
    old, new = old.replace("\n", nl), new.replace("\n", nl)
    if text.count(old) != 1:
        print(f"BREAK NOT STAGED {label}: anchor found {text.count(old)} times")
        continue
    open(DST, "wb").write(text.replace(old, new).encode("utf-8"))
    out = subprocess.run([sys.executable, DST, "--selftest"], capture_output=True, text=True,
                         encoding="utf-8").stdout
    reds = [l for l in out.split("\n") if l.startswith("arm FAIL")]
    print(f"== {label}: {len(reds)} arm(s) red")
    for l in reds:
        print("   " + l[:160])
os.remove(DST)
