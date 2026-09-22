#!/usr/bin/env python3
"""DEPL-dCarriedReceipt-9 S13 — the committed inCMS-derived fixture, and the script that made it.

WHAT S13 ASKED FOR AND WHY IT WAS DEFERRED ONCE. AC1 and AC2 grade `classify_row`'s `carry` rungs
and the needle derivation over a REAL adopter population rather than an authored one. The unit was
built on node `d`, where the inCMS checkout is not reachable, so S13 shipped DEFERRED and AC1's
distribution was measured over a synthetic fixture instead — 4 verbatim / 1 eol / 2 relocate /
3 no rung, against a spec that says 21 / 6 / 5. Neither figure was reproducible anywhere. Reopened
by owner ruling 2026-08-26 on node `a`, where both live adopter checkouts are in hand.

INCMS CARRIES NO GOVKIT RECEIPT, and that is the whole reason this script exists rather than a
`cp`. At `2cff5855` its `.governance/` holds `kits.json` and a GENERATED `install.index` written by
its own `scripts/check_kit_sync.py` — a TSV of `<blob-oid> <role> <kit> <gov-commit> <path>`. That
is the same *evidence* a govkit receipt carries, in a different shape and under a different owner.
So the fixture is RECONSTRUCTED, and every field below says where it came from.

THE RECONSTRUCTION IS THE ENGINE'S OWN, not a heuristic. A row's gov SOURCE is resolved through
gov's `registry.toml` at the row's recorded commit: registry entry -> descriptor -> `home`, then the
longest tail of the target path that resolves to a tracked gov file under that home. The first cut
of this used a basename match and left 13 of 54 rows unresolved, because five kits do not live at
`tools/<kit>/` — `agent-cap` is `tools/hooks`, `review-harness` is `tools/workflows`,
`kickoff-manifest` is `skills/session-kickoff`, and three single-file kits sit directly under
`tools`. Reading the registry is not a refinement of the heuristic; it is the difference between
guessing and asking.

THE POPULATION, MEASURED AND NOT ASSUMED. 92 rows in the index; 54 carry a resolvable gov commit
(38 read `unverified`); of those 54, exactly 52 also resolve a gov source at that commit. The two
that do not are `scripts/check-docs-hygiene.sh` and its `.test.sh`, which gov has since renamed —
they are REPORTED by name on every run rather than dropped quietly, because a reconstruction that
silently discards rows is how a fixture starts grading a subset of itself. 52 is the figure S13
names, arrived at independently here.

`diverged` IS INCMS'S WORD, AND IT MAPS TO `engine`. inCMS's checker uses it for "gov owns these
bytes and a local repath is sanctioned", which is not a member of gov's `ROLE_KINDS`. In gov's
vocabulary that is an `engine` row whose destination moved — precisely what the `relocate` rung
exists to prove — so writing it through as `engine` is what lets those rows reach the rung at all.
Mapped rather than passed through, and the count is printed.

RUN IT:
    python tools/govkit/fixtures/make_incms_receipt.py \
        --incms C:/projects/incms/main --incms-rev 2cff5855 --gov-rev ce5dca99

The output is committed beside this file so AC1 and AC2 re-run with NEITHER live repository
present. Re-running with the same three revisions reproduces it byte for byte; nothing here reads a
clock, a random source, or the working tree of either repo.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
import tomllib

HERE = pathlib.Path(__file__).resolve().parent
GOV_ROOT = HERE.parents[2]

# inCMS's role vocabulary -> gov's. `diverged` is the only translation; the rest are already gov's
# words. A role absent from this map is written through unchanged and counted, so a vocabulary drift
# in either repo shows up as a count rather than as a silent pass.
ROLE_MAP = {"diverged": "engine"}


def read_gov_text(rev: str, path: str) -> str:
    return subprocess.run(["git", "-C", str(GOV_ROOT), "show", f"{rev}:{path}"],
                          capture_output=True, text=True).stdout


def read_gov_tree(rev: str) -> set[str]:
    out = subprocess.run(["git", "-C", str(GOV_ROOT), "ls-tree", "-r", "--name-only", rev],
                         capture_output=True, text=True).stdout
    return {t for t in out.split("\n") if t.strip()}


def read_gov_blob(rev: str, path: str) -> tuple[str, str] | None:
    """`(oid, sha256)` for a gov source at a revision, or None when gov has no blob there."""
    out = subprocess.run(["git", "-C", str(GOV_ROOT), "rev-parse", f"{rev}:{path}"],
                         capture_output=True, text=True)
    if out.returncode != 0:
        return None
    oid = out.stdout.strip()
    raw = subprocess.run(["git", "-C", str(GOV_ROOT), "cat-file", "blob", oid],
                         capture_output=True).stdout
    import hashlib
    return oid, hashlib.sha256(raw).hexdigest()


def derive_lf_oid(incms: pathlib.Path, oid: str) -> str:
    """The oid of the TARGET's blob with its line endings normalised — the `eol` rung's witness.

    WHY THIS FIELD EXISTS AND WHY IT IS NOT VENDORED BYTES. `verbatim` and `relocate` are provable
    from the receipt alone: both compare the target's blob oid against a transformation of gov's
    bytes, and an oid IS that comparison. `eol` is not, because the rung normalises BOTH sides —
    `derive_lf(ours) == derive_lf(base)` — and an oid cannot be un-hashed to be normalised. Without
    a witness the arm would need the target's object store, which is what deferred S13 the first
    time; with one, the whole fixture stays about 30 KiB instead of a 540 KiB pack of another
    project's source vendored into this repo.

    IT IS NOT CIRCULAR, and the direction is the point. This applies `derive_lf` to INCMS's bytes,
    once, here, where inCMS is reachable. The arm applies the same function to GOV's bytes and
    compares. Same function, opposite inputs — which is exactly the equality the rung claims. A
    fixture storing the ANSWER (`carry: "eol"`) would be circular; this stores an independent
    measurement of the target that the rung has to reproduce.

    THE NORMALISATION IS THE ENGINE'S OWN, imported rather than re-spelled. The first cut wrote
    `.replace(CRLF, LF).replace(CR, LF)` here, which handles a lone CR that `derive_lf` does not —
    a fixture whose witness is stricter than the rung it grades, and two spellings of one rule in
    the file whose own docstring calls that the class it spends most of its comments on.
    """
    raw = subprocess.run(["git", "-C", str(incms), "cat-file", "blob", oid],
                         capture_output=True).stdout
    return load_govkit().blob_oid(load_govkit().derive_lf(raw))


def load_govkit():
    """The deployer, loaded as a module. The fixture must grade the engine, never a copy of it."""
    global _GK
    if _GK is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location("gk", GOV_ROOT / "tools/govkit/govkit.py")
        _GK = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_GK)
    return _GK


_GK = None


def resolve_kit_homes(gov_rev: str) -> dict[str, str]:
    """kit id -> `home`, read from gov's own registry at the recorded commit."""
    reg = tomllib.loads(read_gov_text(gov_rev, "tools/govkit/registry.toml"))
    homes: dict[str, str] = {}
    for entry in reg.get("entry", []):
        txt = read_gov_text(gov_rev, entry["descriptor"])
        if not txt.strip():
            continue
        try:
            homes[entry["id"]] = (tomllib.loads(txt).get("home") or "").rstrip("/")
        except tomllib.TOMLDecodeError:
            continue
    return homes


def resolve_source(path: str, home: str, tree: set[str]) -> str | None:
    """The longest tail of `path` that resolves under `home` in gov's tree.

    Longest first, so a nested fixture path such as `fixture-pieces/one/piece.md` keeps its shape
    instead of collapsing onto a same-named file at the kit root. Shortest-first found two rows
    whose basename collided across directories and mapped both to one source.
    """
    parts = path.split("/")
    for i in range(len(parts)):
        cand = "/".join(([home] if home else []) + parts[i:])
        if cand in tree:
            return cand
    return None


def build(incms: pathlib.Path, incms_rev: str, gov_rev: str) -> dict:
    index = subprocess.run(
        ["git", "-C", str(incms), "show", f"{incms_rev}:.governance/install.index"],
        capture_output=True, text=True)
    if index.returncode != 0:
        raise SystemExit(f"inCMS {incms_rev} carries no .governance/install.index: {index.stderr}")

    homes = resolve_kit_homes(gov_rev)
    tree = read_gov_tree(gov_rev)

    raw = []
    for line in index.stdout.splitlines():
        if line.startswith("#") or not line.strip():
            continue
        oid, role, kit, commit, path = line.split("\t")
        raw.append(dict(oid=oid, role=role, kit=kit, commit=commit, path=path))

    # ---- THE SECOND POPULATION, and it is not the same question. AC1 grades rows whose recorded
    # ---- COMMIT resolves, because a rung is proved against gov's bytes AT THAT COMMIT. AC2 grades
    # ---- the needle map, which is derived from (source, destination) pairs and needs no commit at
    # ---- all — so its population is every row whose gov SOURCE resolves, which is 86 rather than
    # ---- 52. The spec measured its Inventory over one and wrote its criterion against the other,
    # ---- which is why AC2's figures never reproduced. Both are emitted here, named, so neither
    # ---- criterion has to borrow the other's population again.
    pairs_86 = []
    for r in raw:
        src = resolve_source(r["path"], homes.get(r["kit"], ""), tree)
        if src:
            pairs_86.append([src, r["path"]])
    pairs_86.sort()

    rows, unresolved, unverified = [], [], []
    roles_seen: dict[str, int] = {}
    for r in raw:
        if r["commit"] == "unverified":
            unverified.append(r["path"])
            continue
        src = resolve_source(r["path"], homes.get(r["kit"], ""), tree)
        if src is None:
            unresolved.append((r["kit"], r["path"]))
            continue
        blob = read_gov_blob(r["commit"], src)
        if blob is None:
            unresolved.append((r["kit"], r["path"]))
            continue
        gov_oid, sha256 = blob
        role = ROLE_MAP.get(r["role"], r["role"])
        roles_seen[role] = roles_seen.get(role, 0) + 1
        rows.append({"path": r["path"], "source": src, "role": role,
                     "commit": r["commit"], "gov_oid": gov_oid, "oid": r["oid"],
                     "sha256": sha256, "kit": r["kit"],
                     "lf_oid": derive_lf_oid(incms, r["oid"])})

    rows.sort(key=lambda x: x["path"])
    print(f"incms-fixture: {len(raw)} index row(s); {len(unverified)} carry `unverified` and are "
          f"out of scope; {len(rows)} resolved a gov source at {gov_rev}")
    for kit, path in unresolved:
        print(f"incms-fixture: UNRESOLVED  [{kit}] {path} — gov holds no such source at {gov_rev}")
    print(f"incms-fixture: AC2 population (gov source resolves): {len(pairs_86)} pair-bearing row(s)")
    print(f"incms-fixture: roles after mapping: "
          + ", ".join(f"{k} {v}" for k, v in sorted(roles_seen.items())))
    return {
        "schema": 3,
        "gov_commit": gov_rev,
        "gov_source": "(reconstructed — see make_incms_receipt.py)",
        "provenance": {
            "adopter": "inCMS",
            "adopter_rev": incms_rev,
            "adopter_record": ".governance/install.index",
            "gov_rev": gov_rev,
            "generated_by": "tools/govkit/fixtures/make_incms_receipt.py",
            "index_rows": len(raw),
            "unverified_rows": len(unverified),
            "unresolved": [f"[{k}] {p}" for k, p in unresolved],
        },
        # AC2's population: every row whose gov SOURCE resolves, commit or no commit. Pairs only —
        # the needle derivation reads nothing else, and carrying oids here would imply it did.
        "carry_map_population": pairs_86,
        "files": rows,
    }


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--incms", required=True)
    ap.add_argument("--incms-rev", default="2cff5855")
    ap.add_argument("--gov-rev", default="ce5dca99")
    ap.add_argument("--out", default=str(HERE / "incms-2cff5855.receipt.json"))
    a = ap.parse_args(argv)

    doc = build(pathlib.Path(a.incms), a.incms_rev, a.gov_rev)
    pathlib.Path(a.out).write_text(json.dumps(doc, indent=1, sort_keys=True) + "\n",
                                   encoding="utf-8", newline="\n")
    print(f"incms-fixture: wrote {len(doc['files'])} row(s) to {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
