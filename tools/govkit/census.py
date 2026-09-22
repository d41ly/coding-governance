#!/usr/bin/env python3
"""The undeclared-fork census — DEPL-dRetiredFork-7.

Answers one question per adopter file: does this content appear in gov's history AT ALL?

Three classes, and the middle one is the whole reason this is blob-against-FULL-HISTORY rather
than a diff against HEAD:

  IN-SYNC   the blob is gov's HEAD blob at the mapped gov path
  DRIFT     the blob is in some gov commit, just not the current one — a stale copy, not a fork
  FORK      the blob is in NO gov commit ever — content gov never shipped

Diffing against HEAD alone collapses DRIFT into FORK and inflates the retirement programme by
every stale copy in every adopter. swydee is the proof: nearly every one of its differing kit
files is a gov vintage, and a HEAD diff would have called every one of them divergent. NO COUNT
IS WRITTEN HERE -- run the tool. The first draft of this docstring carried the spec's figures and
was wrong about them within the same pass that wrote it, which is the rule this file is about.

GOV-INTERNAL, and deliberately neither a kit nor a bar leg: it reads repositories gov does not
own, so it can never run in an adopter's tree and nothing on gov's bar can reach outside this
repository. It is covered by registry.toml's existing `tools/govkit` exemption -- "the deployer
itself ... never installed into a target" -- which is exact-path against a depth-1 `tools/*`
surface, so this file needs no row of its own and deliberately does not get one.

This script MEASURES. It changes nothing, in any tree, ever -- every git call below is a read.
"""

import argparse
import io
import json
import os
import subprocess
import sys

CLASS_SYNC = "IN-SYNC"
CLASS_DRIFT = "DRIFT"
CLASS_FORK = "FORK"
CLASS_ABSENT = "ABSENT"      # the register names a file the adopter does not have on disk
CLASS_UNMAPPED = "UNMAPPED"  # no gov path could be derived, so no question can be asked


def run(args, cwd, check=True):
    """A read-only git call. `errors="replace"` because adopter trees carry non-UTF-8 bytes."""
    p = subprocess.run(
        args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace",
    )
    if check and p.returncode != 0:
        raise SystemExit("census: %s failed in %s\n%s" % (" ".join(args[:3]), cwd, p.stderr[:400]))
    return p.stdout


# ------------------------------------------------------------------ gov's side of the comparison

def build_gov_index(gov):
    """Every blob gov has EVER committed, with the paths it was seen at, plus HEAD's tree.

    `rev-list --objects --all` is REACHABLE-only, which is the semantics this census needs:
    "in some gov commit ever". `cat-file --batch-all-objects` would also report unreachable
    objects -- content that was written and never committed -- and calling that "gov shipped it"
    is the false-reassuring direction.

    Each object is printed ONCE, labelled with the FIRST path the traversal saw it at, so the
    path map is a hint and never a proof. Membership is the exact part; the label is for the
    report. A file moved between paths with identical bytes has one blob and one label, which is
    why classification below tests membership first and consults the label only to describe.
    """
    ever = {}
    for line in run(["git", "rev-list", "--objects", "--all"], gov).splitlines():
        if " " not in line:
            continue  # a commit, or a tree at the root -- no path label
        oid, path = line.split(" ", 1)
        ever.setdefault(oid, set()).add(path)

    head = {}
    for line in run(["git", "ls-tree", "-r", "HEAD"], gov).splitlines():
        if "\t" not in line:
            continue
        meta, path = line.split("\t", 1)
        parts = meta.split()
        if len(parts) == 3 and parts[1] == "blob":
            head[path] = parts[2]
    return ever, head


def confirm_blobs(gov, oids):
    """Ask gov which of these oids it actually holds AS BLOBS.

    The path map above cannot distinguish a blob oid from a tree oid, and this census must not
    report a directory as shipped content. One batch call, not one per file.
    """
    if not oids:
        return set()
    p = subprocess.run(
        ["git", "cat-file", "--batch-check"], cwd=gov,
        input="\n".join(sorted(oids)) + "\n",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        encoding="utf-8", errors="replace",
    )
    good = set()
    for line in p.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 2 and parts[1] == "blob":
            good.add(parts[0])
    return good


# --------------------------------------------------------------- the adopter's side: the mapping

def hash_file(repo, relpath):
    """The git oid of what is ON DISK, which is the thing being classified.

    Not the register's recorded oid: the register is one of the things under test, and trusting
    its hash would make the census agree with it by construction.
    """
    full = os.path.join(repo, relpath)
    if not os.path.isfile(full):
        return None
    return run(["git", "hash-object", "--", relpath], repo, check=False).strip() or None


def map_from_receipt(adopter):
    """inCMS and NicoCares: install.json's `source` field IS the declared gov path."""
    p = os.path.join(adopter, ".governance", "install.json")
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8") as fh:
        d = json.load(fh)
    rows = []
    for r in d.get("files", []):
        rows.append({
            "path": r.get("path"),
            "gov_path": r.get("source"),
            "role": r.get("role", "?"),
            "kit": r.get("kit", "?"),
            "declared_oid": r.get("oid"),
        })
    return {"rows": rows, "gov_commit": d.get("gov_commit"), "kits": d.get("kits", [])}


def map_by_basename(adopter, gov_paths, kit_dirs):
    """swydee: no receipt exists, so the mapping is DERIVED and its ambiguity is reported.

    A basename that resolves to several gov paths is recorded AMBIGUOUS rather than guessed --
    a census that picks one silently would report a class it did not measure. The kit-dir hint
    breaks the common case, where an adopter holds a kit at the repo root and gov holds it one
    break stays ambiguous and visible.
    """
    by_base = {}
    for gp in gov_paths:
        by_base.setdefault(os.path.basename(gp), set()).add(gp)

    tracked = run(["git", "ls-files"], adopter).splitlines()
    rows = []
    for rel in tracked:
        top = rel.split("/")[0]
        if not any(rel.startswith(k) for k in kit_dirs):
            continue
        cands = by_base.get(os.path.basename(rel), set())
        if not cands:
            continue
        gov_path, note = None, ""
        if rel in gov_paths:
            # EXACT PATH WINS, and it is the common case rather than the lucky one. swydee's
            # layout is gov's HISTORICAL layout -- the kits sat at the repo root before they
            # moved under the tools directory -- so the adopter's own relative
            # path is usually literally a gov path, just an old one. Preferring the basename
            # here would call a kit's own README ambiguous against 120 other READMEs and
            # refuse to classify a file whose mapping is not in doubt at all.
            gov_path = rel
        elif len(cands) == 1:
            gov_path = next(iter(cands))
        else:
            hinted = [c for c in cands if c.endswith("/" + rel) or ("/" + top + "/") in ("/" + c)]
            if len(hinted) == 1:
                gov_path = hinted[0]
            else:
                # CAPPED. An unbounded candidate list buries the report it appears in: the
                # first run of this printed 120 paths on one row for `README.md`.
                shown = sorted(cands)
                note = "AMBIGUOUS across %d gov paths: %s%s" % (
                    len(shown), ", ".join(shown[:4]),
                    ", ..." if len(shown) > 4 else "")
        rows.append({"path": rel, "gov_path": gov_path, "role": "derived",
                     "kit": top, "declared_oid": None, "note": note})
    return {"rows": rows, "gov_commit": None, "kits": sorted(kit_dirs)}


# ------------------------------------------------------------------------- the second register(s)

def read_kits_json(adopter):
    p = os.path.join(adopter, ".governance", "kits.json")
    if not os.path.isfile(p):
        return None
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def declared_in_kits_json(kj):
    """Every adopter path kits.json says ANYTHING about, across all of its registers."""
    if not kj:
        return set()
    named = set()
    named.update(kj.get("divergence", {}).keys())
    named.update(kj.get("lone_cr", {}).keys())
    named.update(kj.get("rendered_graders", {}).keys())
    for e in kj.get("exempt", []):
        g = e.get("glob", "")
        if g and "*" not in g:
            named.add(g)
    for e in kj.get("residue", []) + kj.get("role_dispositions", []):
        if e.get("path"):
            named.add(e["path"])
    for kit in kj.get("kits", {}).values():
        named.update(kit.get("files", {}).keys())
    return named


def roles_from_kits_json(kj):
    """kits.json's PER-KIT role map, which is a different register from install.json's `role`.

    Both exist, both are per-path, and they disagree on 30 of inCMS's paths. This census reports
    the disagreement rather than picking a winner: which one is right is the adopter's call and
    gov owns neither file.
    """
    roles = {}
    if not kj:
        return roles
    for kit_name, kit in kj.get("kits", {}).items():
        for path, role in kit.get("files", {}).items():
            roles[path] = (role, kit_name)
    return roles


def profile_symbols(path):
    """Line and top-level-symbol counts, DERIVED. No count in this report is typed by hand.

    Used to justify a `project-owned` disposition: two files sharing a name, one 5x the size of
    the other with almost no symbol overlap, are two programs rather than a fork of one.
    """
    import ast
    try:
        src = io.open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return None
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return {"lines": src.count("\n") + 1, "defs": None, "names": set()}
    names = {n.name for n in tree.body
             if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))}
    return {"lines": src.count("\n") + 1, "defs": len(names), "names": names}


def carve_out_sites(adopter, roots):
    """NicoCares' second register: the `nc carve-out N/M` tags, and where they sit.

    Read with the adopter's OWN grep roots, because that scoping is itself part of what this
    census grades -- a tag outside them is invisible to the check that counts them.
    """
    tagged = {}
    for root in roots:
        out = run(["git", "grep", "-nIE", "nc carve-out [0-9]+/[0-9]+", "--", root],
                  adopter, check=False)
        for line in out.splitlines():
            if ":" not in line:
                continue
            path = line.split(":", 1)[0]
            tagged.setdefault(path, 0)
            tagged[path] += 1
    return tagged


# ------------------------------------------------------------------------------ the census itself

def classify(rows, adopter, ever, head, blobs):
    for r in rows:
        gp = r.get("gov_path")
        oid = r.get("oid")
        if oid is None:
            r["class"] = CLASS_ABSENT
            continue
        if not gp:
            r["class"] = CLASS_UNMAPPED
            continue
        if head.get(gp) == oid:
            r["class"] = CLASS_SYNC
        elif oid in ever and oid in blobs:
            r["class"] = CLASS_DRIFT
            seen = sorted(ever[oid])
            r["seen_at"] = seen
            if gp not in seen:
                r["note"] = ("%s; gov's label for this blob is %s"
                             % (r.get("note", ""), ", ".join(seen))).strip("; ")
        else:
            r["class"] = CLASS_FORK
    return rows


def vintage(gov, oid):
    """Name a commit that carried this blob, for the report. Best-effort, never a verdict."""
    out = run(["git", "log", "--all", "-1", "--format=%h %ad", "--date=short",
               "--find-object=%s" % oid], gov, check=False).strip()
    return out or "(no commit found by --find-object)"


def main():
    ap = argparse.ArgumentParser(description="the undeclared-fork census")
    ap.add_argument("--adopter", required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--gov", default=".")
    ap.add_argument("--derive-map", action="store_true",
                    help="no receipt: derive the gov mapping by basename (swydee)")
    ap.add_argument("--kit-dirs", default="memory-tree,memory-recall,tools,scripts,.claude,.githooks")
    ap.add_argument("--carve-roots", default="")
    ap.add_argument("--vintages", action="store_true", help="name a commit for each DRIFT row")
    ap.add_argument("--profile", action="append", default=[],
                    help="ADOPTER_PATH=GOV_PATH — emit a symbol profile justifying a disposition")
    a = ap.parse_args()

    gov = os.path.abspath(a.gov)
    adopter = a.adopter
    if not os.path.isdir(os.path.join(adopter, ".git")) and not os.path.isfile(os.path.join(adopter, ".git")):
        raise SystemExit("census: %s is not a git repository" % adopter)

    ever, head = build_gov_index(gov)

    if a.derive_map:
        gov_paths = set(head) | {p for ps in ever.values() for p in ps}
        reg = map_by_basename(adopter, gov_paths, [k for k in a.kit_dirs.split(",") if k])
    else:
        reg = map_from_receipt(adopter)
        if reg is None:
            raise SystemExit("census: %s has no .governance/install.json and --derive-map was not given"
                             % adopter)

    rows = reg["rows"]

    # AC4 -- THE VACUITY REFUSAL. A census that mapped nothing has measured nothing, and printing
    # "0 forks" for it is the exact shape this build spent a unit removing elsewhere: a clean
    # report produced by a probe that could not reach its subject. The index is built from
    # rev-list, so an empty map is DETECTABLE rather than indistinguishable from a clean tree.
    if not rows:
        print("census: REFUSED -- mapped 0 files in %s." % adopter)
        print("        gov's index holds %d blobs, so the index is live and the map is empty."
              % len(ever))
        print("        A census with no subjects cannot report a clean tree.")
        return 2
    if not ever:
        print("census: REFUSED -- gov's object index is EMPTY, so every file would read as a fork.")
        return 2

    # Hash every mapped file ONCE. classify() reads what this records; hashing again inside it
    # would double a per-file subprocess over a few hundred files, and process creation is the
    # measured cost on this node.
    for r in rows:
        r["oid"] = hash_file(adopter, r["path"])
    blobs = confirm_blobs(gov, {r["oid"] for r in rows if r["oid"]})
    classify(rows, adopter, ever, head, blobs)

    counts = {}
    for r in rows:
        counts[r["class"]] = counts.get(r["class"], 0) + 1

    print("# Census — %s" % a.name)
    print()
    print("- adopter: `%s`" % adopter)
    print("- gov index: %d objects with a path label, %d blobs at HEAD"
          % (len(ever), len(head)))
    print("- register: %s" % ("DERIVED by basename (no .governance/)" if a.derive_map
                              else "`.governance/install.json`, gov_commit `%s`"
                                   % (reg.get("gov_commit") or "?")))
    print("- mapped: %d files" % len(rows))
    for k in (CLASS_SYNC, CLASS_DRIFT, CLASS_FORK, CLASS_ABSENT, CLASS_UNMAPPED):
        if counts.get(k):
            print("- %s: %d" % (k, counts[k]))
    print()

    # The second register, where one exists.
    kj = read_kits_json(adopter)
    second = declared_in_kits_json(kj)
    carve = {}
    if a.carve_roots:
        carve = carve_out_sites(adopter, [r for r in a.carve_roots.split(",") if r])
        print("- carve-out tags: %d distinct sites across %s"
              % (len(carve), a.carve_roots))
        print()

    if second or carve:
        receipt_paths = {r["path"] for r in rows}
        neither = sorted(receipt_paths - second - set(carve))
        # Only interesting for files that ARE gov-derived and NOT in sync: a synced engine file
        # needs no second-register row, and saying otherwise would bury the ones that matter.
        by_path = {r["path"]: r for r in rows}
        flagged = [p for p in neither if by_path[p]["class"] in (CLASS_DRIFT, CLASS_FORK)]
        print("## Declared in the receipt, absent from the second register")
        print()
        if flagged:
            for p in flagged:
                print("- `%s` — %s, role `%s`" % (p, by_path[p]["class"], by_path[p]["role"]))
        else:
            print("- none")
        print()

        # ---- THE POPULATION THE SECTION ABOVE STRUCTURALLY CANNOT SEE.
        # Everything above is keyed on the receipt's own rows, so a gov-derived file that is in
        # NO register at all never appears -- it has no row to iterate. That is the same
        # could-not-fail shape one level up: a report that quantifies over a register can never
        # report what the register omitted. This section quantifies over the TREE instead, and it
        # is how `.githooks/pre-commit` and `scripts/check-wiring.sh` were found at NicoCares.
        #
        # "gov-derived by name" is a deliberately WIDE net -- a basename gov also uses -- because
        # a narrow one would reintroduce the omission it exists to catch. False positives here
        # are cheap and visible; a miss is the whole defect.
        gov_basenames = {os.path.basename(p) for p in head}
        gov_basenames |= {os.path.basename(p) for ps in ever.values() for p in ps}
        tracked = run(["git", "ls-files"], adopter, check=False).splitlines()
        roots = [r for r in (a.carve_roots or "").split(",") if r]
        unregistered = []
        for rel in tracked:
            if roots and not any(rel.startswith(r) for r in roots):
                continue
            if rel in receipt_paths or rel in second or rel in carve:
                continue
            if os.path.basename(rel) not in gov_basenames:
                continue
            oid = hash_file(adopter, rel)
            cls = CLASS_FORK if (oid and oid not in ever) else CLASS_DRIFT
            if oid and head.get(rel) == oid:
                cls = CLASS_SYNC
            unregistered.append((rel, cls))
        print("## In NO register at all, but named like a gov file (%d)" % len(unregistered))
        print()
        if unregistered:
            print("Neither register mentions these. The class is this census's own verdict.")
            print()
            for rel, cls in sorted(unregistered):
                print("- `%s` — %s" % (rel, cls))
        else:
            print("- none")
        print()

    for cls, title in ((CLASS_FORK, "UNDECLARED FORK — in no gov commit ever"),
                       (CLASS_DRIFT, "DRIFT — a gov vintage, not gov's HEAD"),
                       (CLASS_ABSENT, "ABSENT — declared, not on disk"),
                       (CLASS_UNMAPPED, "UNMAPPED — no gov path derivable")):
        sel = [r for r in rows if r["class"] == cls]
        if not sel:
            continue
        print("## %s (%d)" % (title, len(sel)))
        print()
        for r in sorted(sel, key=lambda r: r["path"]):
            line = "- `%s` — role `%s`, kit `%s`" % (r["path"], r["role"], r["kit"])
            if r.get("gov_path"):
                line += ", gov `%s`" % r["gov_path"]
            if r.get("note"):
                line += " — %s" % r["note"]
            if cls == CLASS_DRIFT and a.vintages and r.get("oid"):
                line += " — vintage %s" % vintage(gov, r["oid"])
            print(line)
        print()

    # ---- the ENGINE-declared forks: the headline number, and the one AC1 asks for.
    # A fork gov never shipped is only alarming where the adopter still calls the file an ENGINE
    # -- gov's bytes, kept in sync. A row already declared `diverged` or `project-owned` is a
    # decision somebody made and recorded; an `engine` row that matches nothing gov ever shipped
    # is a claim contradicted by the object store.
    kj_roles = roles_from_kits_json(kj)
    if kj_roles:
        eng = sorted(r["path"] for r in rows
                     if r["class"] == CLASS_FORK and kj_roles.get(r["path"], ("",))[0] == "engine")
        # kits.json can name paths the receipt does not carry, so ask it about its own set too.
        extra = sorted(p for p, (role, _k) in kj_roles.items()
                       if role == "engine" and p not in {r["path"] for r in rows}
                       and (lambda o: o and o not in ever)(hash_file(adopter, p)))
        both = sorted(set(eng) | set(extra))
        print("## UNDECLARED FORK, still declared `engine` (%d)" % len(both))
        print()
        print("kits.json calls each of these gov's bytes. None is in any gov commit, ever.")
        print()
        for p in both:
            print("- `%s` — kit `%s`%s"
                  % (p, kj_roles.get(p, ("", "?"))[1],
                     "" if p in {r["path"] for r in rows} else " — not in install.json at all"))
        print()

        # The two registers, disagreeing with each other. Neither is gov's to correct.
        inst_roles = {r["path"]: r["role"] for r in rows}
        dis = [(p, kj_roles[p][0], inst_roles[p]) for p in sorted(kj_roles)
               if p in inst_roles and kj_roles[p][0] != inst_roles[p]]
        print("## The adopter's two registers disagree (%d paths)" % len(dis))
        print()
        for p, kj_role, inst_role in dis:
            # NOT `a`: that is the argparse namespace, and shadowing it here made every later
            # flag read as a string attribute lookup on it. Caught by --profile crashing.
            print("- `%s` — kits.json `%s`, install.json `%s`" % (p, kj_role, inst_role))
        print()

    for spec in a.profile:
        if "=" not in spec:
            continue
        ap_rel, gov_rel = spec.split("=", 1)
        pa = profile_symbols(os.path.join(adopter, ap_rel))
        pg = profile_symbols(os.path.join(gov, gov_rel))
        print("## PROFILE — `%s` against gov `%s`" % (ap_rel, gov_rel))
        print()
        if not pa or not pg:
            print("- one side is unreadable; no profile")
            print()
            continue
        row = next((r for r in rows if r["path"] == ap_rel), None)
        shared = sorted(pa["names"] & pg["names"])
        print("- census class: %s" % (row["class"] if row else "not in the mapped set"))
        print("- kits.json role: %s" % (kj_roles.get(ap_rel, ("(none)", ""))[0] if kj_roles else "(no kits.json)"))
        print("- gov `%s`: %d lines, %d top-level symbols" % (gov_rel, pg["lines"], pg["defs"]))
        print("- adopter `%s`: %d lines, %d top-level symbols" % (ap_rel, pa["lines"], pa["defs"]))
        print("- shared top-level names: %d%s"
              % (len(shared), (" — " + ", ".join("`%s`" % s for s in shared)) if shared else ""))
        print()

    print("## IN-SYNC (%d)" % counts.get(CLASS_SYNC, 0))
    print()
    print("Named only in aggregate: a file identical to gov HEAD is the uninteresting case, and")
    print("listing all of them would bury the %d that are not."
          % (len(rows) - counts.get(CLASS_SYNC, 0)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
