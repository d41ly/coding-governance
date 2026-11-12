#!/usr/bin/env python3
"""pass_legs.py — which legs a unit pass runs, DERIVED and never typed. TOOL-aNimbleMend-2.

A leg's row in the leg manifest carries `"pass_leg": true` when this rule selects it, and no hand
writes that field. The rule ranks every leg by recorded reds per evidenced second and fills
PASS_BUDGET_SECONDS:

  1. COST      the leg's maximum in `ceiling-evidence.txt`, the figure the budget gate sums.
  2. EXCLUDED  `check_pass_eligible` gives the first reason that fits, in EXCLUSIONS' order.
  3. SCORE     reds / max(cost, 1.0). The one-second floor keeps a sub-second leg from outranking
               every other by division.
  4. ORDER     score descending, then cost ascending, then name.
  5. FILL      walk the order with a running sum of cost; a leg is `selected` while the sum with its
               cost stays at or under the budget, else `over-budget`, and the walk goes on, so a
               cheaper leg further down still enters.

Every recorded red counts, an inherited one included: the run log does not say whose a red was.
A row carrying `scope_of` is a cheap form of the leg it names, and `--write` credits it that leg's
reds beside its own (`read_scope_reds`, TOOL-aNimbleMend-4).

THE INPUTS. Red history lives in `<git-common-dir>/runlog/gates.log`, one line per bar with its
failing legs as `fail.<n>` fields, and the last seconds in `gate-ledger.tsv`. Both are node-local,
so `--write` distils them into the tracked `pass-leg-evidence.txt` and every other verb reads
tracked files only, the shape `derive-ceilings.py` has. The gate ledger keeps one row per leg and
no history, so a red count read from it would be 0 or 1.

  GOV_NODE=<tag> python pass_legs.py --write   distil this node's run log and ledgers, then apply
  python pass_legs.py --apply                  write the field onto the manifest from tracked files
  python pass_legs.py --check                  exit 1 unless the manifest is what --apply writes
  python pass_legs.py --report                 one line per leg: verdict, reds, cost, score, name

Exit 0 clean, 1 a finding or a DEAD PROBE, 2 a refusal with nothing written.
"""
import argparse
import datetime
import json
import os
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
EVIDENCE = HERE / "pass-leg-evidence.txt"
CEILINGS = HERE / "ceiling-evidence.txt"
# The leg manifest is this kit dir's SIBLING, and GATE_LEGS outranks it, as in derive-ceilings.py.
LEGS_BESIDE = HERE.parent / "gate-legs.json"

# What one unit pass may spend on its declared legs, in evidenced seconds.
PASS_BUDGET_SECONDS = 600
# No single leg takes more than a fifth of a pass (the spec's F1, resolved at 120).
PASS_LEG_CAP_SECONDS = 120

# The unattended kit gate is found by its SCRIPT, so a renamed row stays excluded.
UNATTENDED_GATE = "check-unattended.sh"
EXCLUSIONS = ("selftest", "e2e", "unattended-gate", "no-red", "unevidenced", "over-cap")

_NAME_LINE = re.compile(r'^    "name": (".*"),\s*$')
_FIELD_LINE = re.compile(r'^\s*"pass_leg"\s*:')
_FAIL_KEY = re.compile(r"^fail\.\d+$")


class Refusal(Exception):
    """Exit 2, nothing written."""


def resolve_manifest_path() -> pathlib.Path:
    # ponytail: a relative GATE_LEGS resolves against the working directory, not the repo root as
    # derive-ceilings.py does, because --check spawns nothing; every caller runs from the root.
    return pathlib.Path(os.environ.get("GATE_LEGS") or LEGS_BESIDE)


def read_manifest() -> tuple:
    """(text with LF line ends, parsed rows), or a Refusal when the manifest does not parse."""
    p = resolve_manifest_path()
    try:
        text = p.read_bytes().decode("utf-8").replace("\r\n", "\n")
        legs = json.loads(text)
    except (OSError, ValueError) as e:
        raise Refusal(f"the leg manifest {p} does not read as JSON: {e}")
    if not isinstance(legs, list) or not all(isinstance(l, dict) and "name" in l for l in legs):
        raise Refusal(f"the leg manifest {p} is not an array of named rows")
    return text, legs


def read_ceilings() -> dict:
    """{leg: evidenced maximum seconds} from the tracked ceiling evidence."""
    out = {}
    if not CEILINGS.is_file():
        return out
    for line in CEILINGS.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\t")
        try:
            out[f[0]] = float(f[1])
        except (IndexError, ValueError):
            continue
    return out


def read_pass_evidence():
    """(window fields, {leg: (reds, last seconds or None)}), or None when no evidence file exists."""
    if not EVIDENCE.is_file():
        return None
    window, rows = [], {}
    for line in EVIDENCE.read_text(encoding="utf-8").splitlines():
        f = line.split("\t")
        if f[0] == "# window":
            window = f[1:]
        if not line.strip() or line.startswith("#") or len(f) < 3:
            continue
        try:
            rows[f[0]] = (int(f[1]), None if f[2].strip() == "-" else float(f[2]))
        except ValueError:
            continue
    return window, rows


def read_red_counts(runlog: pathlib.Path, names) -> dict:
    """The bar run log's red history, or {} when the log is absent or holds no bar line.

    A bar is a `p=gates`, `ev=once` line. A leg named twice on one line counts once, and `fail_more`
    names no leg and adds nothing. `dropped` holds the failing names the manifest no longer carries.
    """
    if not runlog.is_file():
        return {}
    bars = red_bars = 0
    started, reds, dropped = [], {}, set()
    for line in runlog.read_text(encoding="utf-8", errors="replace").splitlines():
        kv = dict(f.split("=", 1) for f in line.split("\t") if "=" in f)
        if kv.get("p") != "gates" or kv.get("ev") != "once":
            continue
        bars += 1
        started.append(kv.get("started") or "-")
        failing = {v for k, v in kv.items() if _FAIL_KEY.match(k) and v}
        red_bars += bool(failing)
        for name in failing:
            if name in names:
                reds[name] = reds.get(name, 0) + 1
            else:
                dropped.add(name)
    if not bars:
        return {}
    return {"bars": bars, "red_bars": red_bars, "first": started[0], "last": started[-1],
            "reds": reds, "dropped": dropped}


def read_scope_reds(legs, reds: dict) -> dict:
    """`reds` with each row carrying `scope_of` credited the count of the leg it names, added to its
    own (TOOL-aNimbleMend-4). A scoped form runs because its parent redded, so the parent's count is
    its reason to run; the credit overstates it by the parent's reds the form does not grade. Every
    credit reads the counts as logged, so a form of a form gains one parent's and no more. A
    `scope_of` naming no manifest row is a Refusal.
    """
    names = {l["name"] for l in legs}
    out = dict(reds)
    for leg in legs:
        parent = leg.get("scope_of")
        if parent is None:
            continue
        if parent not in names:
            raise Refusal(f"`{leg['name']}` carries scope_of `{parent}`, a name no manifest row carries")
        credited = reds.get(leg["name"], 0) + reds.get(parent, 0)
        if credited:
            out[leg["name"]] = credited
    return out


def read_last_seconds(git_dirs) -> dict:
    """{leg: last seconds} over every `gate-ledger.tsv`; the row with the later ended-at wins.

    A linked worktree has run no bar of its own, and the common directory's ledger is the primary
    checkout's, so both are read.
    """
    best = {}
    for d in git_dirs:
        p = pathlib.Path(d) / "gate-ledger.tsv"
        if not p.is_file():
            continue
        for line in p.read_text(encoding="utf-8", errors="replace").splitlines():
            f = line.split("\t")
            try:
                seconds, ended = float(f[1]), int(f[4])
            except (IndexError, ValueError):
                continue
            if f[0] not in best or ended > best[f[0]][0]:
                best[f[0]] = (ended, seconds)
    return {name: v[1] for name, v in best.items()}


def resolve_git_dirs() -> list:
    out = subprocess.run(["git", "-C", str(HERE), "rev-parse", "--path-format=absolute",
                          "--git-dir", "--git-common-dir"],
                         capture_output=True, text=True, encoding="utf-8")
    if out.returncode != 0:
        raise Refusal("not a git work tree, so there is no run log to read")
    return [pathlib.Path(p) for p in out.stdout.split("\n") if p.strip()]


def check_pass_eligible(leg: dict, reds: dict, ceilings: dict) -> str:
    """The first reason `leg` is excluded from a pass, in EXCLUSIONS' order, or '' when none fits.

    `reds` is the evidence file's rows, {leg: (reds, last seconds or None)}, and `ceilings` the
    ceiling evidence, {leg: seconds}. The last-seconds half of `over-cap` exists because ceiling
    evidence can be stale low.
    """
    name = leg.get("name")
    if leg.get("chunk") == "selftests":
        return "selftest"
    if leg.get("chunk") == "e2e":
        return "e2e"
    if any(str(a).endswith(UNATTENDED_GATE) for a in leg.get("argv") or []):
        return "unattended-gate"
    if name not in reds:
        return "no-red"
    if name not in ceilings:
        return "unevidenced"
    last = reds[name][1]
    if ceilings[name] > PASS_LEG_CAP_SECONDS or (last is not None and last > PASS_LEG_CAP_SECONDS):
        return "over-cap"
    return ""


def derive_pass_legs(legs, reds: dict, ceilings: dict) -> list:
    """Every leg's verdict, ranked legs first in fill order, then the excluded in manifest order.

    Each entry is {name, verdict, reds, cost, score}; `cost` and `score` are None where unknown.
    Reads the manifest rows, the evidence rows and the ceiling evidence, and nothing else.
    """
    ranked, excluded = [], []
    for leg in legs:
        name = leg["name"]
        row = {"name": name, "verdict": check_pass_eligible(leg, reds, ceilings),
               "reds": reds[name][0] if name in reds else 0, "cost": ceilings.get(name),
               "score": None}
        if row["verdict"]:
            excluded.append(row)
        else:
            row["score"] = row["reds"] / max(row["cost"], 1.0)
            ranked.append(row)
    ranked.sort(key=lambda r: (-r["score"], r["cost"], r["name"]))
    spent = 0.0
    for row in ranked:
        if spent + row["cost"] <= PASS_BUDGET_SECONDS:
            spent += row["cost"]
            row["verdict"] = "selected"
        else:
            row["verdict"] = "over-budget"
    return ranked + excluded


def render_pass_field(text: str, selected) -> str:
    """The manifest's text with `"pass_leg": true` on exactly the `selected` rows, edited as TEXT.

    The file is hand-formatted and a JSON re-dump would rewrite every row. Every `pass_leg` line is
    dropped, and a selected row gains one directly after its `"name"` line, which opens every row.
    A Refusal unless the result parses to the old rows with only `pass_leg` keys differing.
    """
    out = []
    for line in text.split("\n"):
        if _FIELD_LINE.match(line):
            continue
        out.append(line)
        m = _NAME_LINE.match(line)
        if m and json.loads(m.group(1)) in selected:
            out.append('    "pass_leg": true,')
    new = "\n".join(out)
    try:
        after = json.loads(new)
    except ValueError as e:
        raise Refusal(f"the edited manifest would not parse ({e}); a `pass_leg` line typed as a "
                      f"row's last key leaves a trailing comma, so remove it by hand")

    def strip(rows):
        return [{k: v for k, v in r.items() if k != "pass_leg"} for r in rows]

    before = json.loads(text)
    declared = {r["name"] for r in after if r.get("pass_leg") is True}
    if strip(after) != strip(before) or declared != {r["name"] for r in before} & set(selected) \
            or any("pass_leg" in r and r["pass_leg"] is not True for r in after):
        raise Refusal("the edit would change more than the `pass_leg` field of the selected rows")
    return new


def derive_state() -> tuple:
    """(manifest text, verdict rows, selected names, evidence-or-None) from tracked files alone."""
    text, legs = read_manifest()
    evidence = read_pass_evidence()
    reds = evidence[1] if evidence else {}
    names = {l["name"] for l in legs}
    for stale in sorted(set(reds) - names):
        print(f"pass-legs: note — the evidence names `{stale}`, which the manifest no longer "
              f"carries", file=sys.stderr)
    rows = derive_pass_legs(legs, reds, read_ceilings())
    return text, legs, rows, [r["name"] for r in rows if r["verdict"] == "selected"], evidence


def render_summary(rows) -> str:
    chosen = [r for r in rows if r["verdict"] == "selected"]
    return (f"pass-legs: {len(chosen)} declared, {sum(r['cost'] for r in chosen):.1f}s of "
            f"{PASS_BUDGET_SECONDS}s")


def cmd_apply() -> int:
    text, _legs, rows, selected, evidence = derive_state()
    new = render_pass_field(text, selected).encode("utf-8")
    p = resolve_manifest_path()
    if new != p.read_bytes():
        p.write_bytes(new)
    print(render_summary(rows) if evidence else "pass-legs: not derived, no evidence file")
    return 0


def cmd_check() -> int:
    text, legs, rows, selected, evidence = derive_state()
    declared = [l["name"] for l in legs if "pass_leg" in l]
    bad = [f"`{n}` carries a pass_leg field the rule does not give it"
           for n in declared if n not in selected]
    bad += [f"`{n}` is selected and carries no pass_leg field" for n in selected if n not in declared]
    if not bad and render_pass_field(text, selected).encode("utf-8") != resolve_manifest_path().read_bytes():
        bad.append("the manifest's bytes differ from what --apply writes")
    if bad:
        for b in bad:
            print(f"pass-legs: {b}")
        print("pass-legs: the field is derived, never typed — run `pass_legs.py --apply`")
        return 1
    print(render_summary(rows) if evidence else "pass-legs: not derived, no evidence file")
    return 0


def cmd_report() -> int:
    _text, _legs, rows, _selected, evidence = derive_state()
    if not evidence:
        print("pass-legs: not derived, no evidence file")
    elif evidence[0]:
        print("# window\t" + "\t".join(evidence[0]))
    print("verdict\treds\tcost\tscore\tleg")
    for r in rows:
        cost = "-" if r["cost"] is None else f"{r['cost']:.1f}"
        score = "-" if r["score"] is None else f"{r['score']:.4f}"
        print(f"{r['verdict']}\t{r['reds']}\t{cost}\t{score}\t{r['name']}")
    return 0


def cmd_write() -> int:
    node = os.environ.get("GOV_NODE")
    if not node:
        raise Refusal("--write needs GOV_NODE set to the node whose run log is read; it is unset, "
                      "and a default would attribute this window to a machine that did not run it")
    _text, legs = read_manifest()
    read_scope_reds(legs, {})  # an unknown scope_of refuses before the log is read or a byte written
    git_dir, common = resolve_git_dirs()
    runlog = common / "runlog" / "gates.log"
    log = read_red_counts(runlog, {l["name"] for l in legs})
    if not log:
        print(f"pass-legs: DEAD PROBE — {runlog} is absent or holds no bar line, so there is no "
              f"red history to rank by. Nothing was written.", file=sys.stderr)
        return 1
    log["reds"] = read_scope_reds(legs, log["reds"])
    last = read_last_seconds([git_dir, common])
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    lines = ["# pass-leg-evidence.txt — recorded reds per gate leg, TRACKED so the pass-leg rule can read it.",
             "#",
             "# GENERATED by `GOV_NODE=<tag> python <prefix>/run-gates/pass_legs.py --write` from this",
             "# node's bar run log and gate ledgers. Do not hand-edit. A write replaces every row: the",
             "# file is one node's window and is not monotone.",
             "#",
             "# window TAB bars read TAB first bar's started TAB last bar's started TAB node TAB date",
             "# leg TAB reds TAB last seconds, or -",
             "# A row carrying `scope_of` holds its own reds plus those of the leg it names.",
             "\t".join(["# window", str(log["bars"]), log["first"], log["last"], node, today])]
    for name in sorted(log["reds"]):
        lines.append(f"{name}\t{log['reds'][name]}\t{last[name]:.1f}" if name in last
                     else f"{name}\t{log['reds'][name]}\t-")
    EVIDENCE.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))
    print(f"pass-legs: wrote {len(log['reds'])} row(s) from {log['bars']} bar(s), {log['red_bars']} "
          f"of them red; {len(log['dropped'])} failing name(s) the manifest no longer carries "
          f"were dropped")
    return cmd_apply()


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description="The pass-leg declaration, derived from recorded reds.")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--write", action="store_const", dest="verb", const=cmd_write,
                   help="distil this node's run log and ledgers into the evidence file, then apply")
    g.add_argument("--apply", action="store_const", dest="verb", const=cmd_apply,
                   help="write the pass_leg field onto the manifest from tracked files")
    g.add_argument("--check", action="store_const", dest="verb", const=cmd_check,
                   help="exit 1 unless the manifest is what --apply would write")
    g.add_argument("--report", action="store_const", dest="verb", const=cmd_report,
                   help="one line per leg: verdict, reds, cost, score, name")
    try:
        return ap.parse_args().verb()
    except Refusal as e:
        print(f"pass-legs: REFUSED — {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
