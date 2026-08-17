#!/usr/bin/env python3
"""Arms for check-recall.py — one per row of the spec's degradation table, plus every refusal.

    python test_recall_floor.py        # exit 0 = the floor can still FAIL for the right reason

GOV-ONLY, and that is the point rather than an accident. These arms are keyed on THIS repo's record
ids, so they are meaningless in an adopter's tree; `kit.toml` withholds this file, `check-recall.py`
and `recall-fixture.json` through a non-landable rule. The sibling `selftest.py` is the adopter-run
leg and is deliberately untouched by this unit — an arm naming `TOOL-aWrittenMethod-4` inside a file
that ships and runs as a declared `[[gate_leg]]` would red in every adopting tree.

THE TWO ARMS THAT MATTER are the single-direction ones. A floor and a per-id assertion that always
red together are indistinguishable from one check wearing two names, so the design's whole claim is
that each can fire ALONE:

    floor alone    drop only the DECISIONS.md home of a MULTI-HOMED hitting target
                   -> the id still resolves; the question falls out of the top k
    per-id alone   retire every home of a NON-hitting target
                   -> the id stops resolving; the normalised score RISES

Each arm drives the real program as a subprocess over a filtered `--data-dir`, so what is exercised
is the shipped entry point and not a re-implementation of it.
"""

from __future__ import annotations

import json
import pathlib
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

KIT = pathlib.Path(__file__).resolve().parent
CHECK = KIT / "check-recall.py"
FIXTURE = KIT / "recall-fixture.json"
ROOT = KIT.parent.parent

_checks: list[tuple[str, str, str]] = []


def check(name):
    def arm(fn):
        try:
            _checks.append(("ok", name, fn() or ""))
        except AssertionError as exc:
            _checks.append(("FAIL", name, str(exc)))
        except Exception as exc:  # noqa: BLE001 — a crash is a failure, not a stack trace
            _checks.append(("FAIL", name, f"{type(exc).__name__}: {exc}"))
        return fn

    return arm


# ------------------------------------------------------------------ harness

_BASE: pathlib.Path | None = None


def build_base_dir() -> pathlib.Path:
    """Extract this repo's corpus ONCE. Every arm filters a copy of it.

    Extraction is ~0.4 s and there are a dozen arms; doing it per arm would put the whole leg's cost
    into a step none of them is testing.
    """
    global _BASE
    if _BASE is None:
        out = pathlib.Path(tempfile.mkdtemp(prefix="recallarm-base-"))
        import query  # noqa: PLC0415 — imported here so a missing sibling fails as an arm, not at load

        sys.path.insert(0, str(KIT))
        proc = subprocess.run(
            [sys.executable, str(KIT / "extract.py"), str(ROOT), str(out),
             "--chunk-max", str(query.CHUNK_MAX)],
            capture_output=True, text=True, cwd=str(ROOT),
        )
        assert proc.returncode == 0, f"extract failed: {proc.stderr[-400:]}"
        _BASE = out
    return _BASE


def build_filtered(drop=None) -> pathlib.Path:
    """A copy of the base data dir with `records.jsonl` rows removed by a predicate."""
    src = build_base_dir()
    dst = pathlib.Path(tempfile.mkdtemp(prefix="recallarm-"))
    for name in ("spine", "records", "chunks"):
        rows = [ln for ln in (src / f"{name}.jsonl").read_text(encoding="utf-8").splitlines() if ln.strip()]
        if name == "records" and drop is not None:
            rows = [ln for ln in rows if not drop(json.loads(ln))]
        (dst / f"{name}.jsonl").write_text("\n".join(rows) + ("\n" if rows else ""),
                                           encoding="utf-8", newline="\n")
    shutil.copy(src / "anchors.json", dst / "anchors.json")
    return dst


def run_check(*args, conf_floor: str | None = None, fixture: pathlib.Path | None = None):
    """Drive the shipped program. `conf_floor` swaps the pin by pointing --repo at a stub repo."""
    argv = [sys.executable, str(CHECK), *args]
    if fixture is not None:
        argv += ["--fixture", str(fixture)]
    repo = ROOT
    tmp = None
    if conf_floor is not None:
        tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallconf-"))
        (tmp / ".memory-tree.conf").write_text(
            'MEMORY_ROOT=memory\nFAMILIES="tooling:TOOL"\n' + conf_floor,
            encoding="utf-8", newline="\n")
        repo = tmp
    argv += ["--repo", str(repo)]
    try:
        return subprocess.run(argv, capture_output=True, text=True, cwd=str(ROOT))
    finally:
        if tmp is not None:
            shutil.rmtree(tmp, ignore_errors=True)


def read_lines(proc) -> str:
    return proc.stdout + proc.stderr


# ------------------------------------------------------------------ the baseline


@check("baseline is green and prints both verdicts")
def test_baseline_green():
    d = build_filtered()
    p = run_check("--data-dir", str(d))
    out = read_lines(p)
    assert p.returncode == 0, f"expected 0, got {p.returncode}\n{out}"
    assert "per-id ok" in out, out
    assert "RECALL_FLOOR ok" in out, out
    return "per-id ok + RECALL_FLOOR ok, exit 0"


# ------------------------------------------------------------------ the two single-direction arms


@check("the FLOOR reds alone (per-id stays green)")
def test_floor_reds_alone():
    # TOOL-aWrittenMethod-4 has three homes; removing only the DECISIONS.md one leaves the id
    # resolvable through the archive and build-README rows while the question falls out of the top 5.
    d = build_filtered(lambda r: r.get("id") == "TOOL-aWrittenMethod-4"
                       and r["path"] == "memory/DECISIONS.md")
    p = run_check("--data-dir", str(d))
    out = read_lines(p)
    assert p.returncode != 0, f"expected a red\n{out}"
    assert "per-id ok" in out, f"per-id should stay GREEN\n{out}"
    assert "RECALL_FLOOR RED" in out, f"floor should red\n{out}"
    assert "0.7500" in out, f"expected normalised 0.7500\n{out}"
    return "floor RED at 0.7500, per-id ok — the directions are independent"


@check("PER-ID reds alone (the floor stays green and RISES)")
def test_per_id_reds_alone():
    # TOOL-aMouldedFolio-1 is single-homed and does NOT hit today, so retiring it drops R without
    # dropping h: the normalised score goes UP while the id stops resolving.
    d = build_filtered(lambda r: r.get("id") == "TOOL-aMouldedFolio-1")
    p = run_check("--data-dir", str(d))
    out = read_lines(p)
    assert p.returncode != 0, f"expected a red\n{out}"
    assert "per-id RED" in out and "TOOL-aMouldedFolio-1" in out, f"per-id should name the id\n{out}"
    assert "RECALL_FLOOR ok" in out, f"floor should stay GREEN\n{out}"
    assert "0.9091" in out, f"expected normalised 0.9091\n{out}"
    return "per-id RED naming the id, floor ok at 0.9091 — it rose"


@check("one retirement of a HITTING target is free by construction")
def test_one_retirement_is_free():
    d = build_filtered(lambda r: r.get("id") == "TOOL-aStandingWrit-2")
    p = run_check("--data-dir", str(d))
    out = read_lines(p)
    assert "RECALL_FLOOR ok" in out, f"the derived pin must absorb one retirement\n{out}"
    assert "0.8182" in out, f"expected the (h-1)/(R-1) worst case 0.8182\n{out}"
    assert "per-id RED" in out, out
    return "normalised 0.8182 >= 0.81, floor ok — the headroom the pin is derived from"


@check("dropping the whole record file reds BOTH (the plumbing arm)")
def test_both_red_on_wholesale_drop():
    d = build_filtered(lambda r: r["path"] == "memory/DECISIONS.md")
    p = run_check("--data-dir", str(d))
    out = read_lines(p)
    assert p.returncode != 0, out
    assert "per-id RED" in out and "RECALL_FLOOR RED" in out, f"both should red\n{out}"
    assert "0.2000" in out, f"expected normalised 0.2000\n{out}"
    return "both RED at 0.2000 — proves the score responds to the corpus, not that retrieval is good"


# ------------------------------------------------------------------ the refusals


@check("an ABSENT fixture reds by name and does not skip")
def test_absent_fixture_reds():
    missing = pathlib.Path(tempfile.gettempdir()) / "no-such-recall-fixture.json"
    p = run_check("--data-dir", str(build_filtered()), fixture=missing)
    out = read_lines(p)
    assert p.returncode == 2, f"expected refusal 2, got {p.returncode}\n{out}"
    assert "fixture absent" in out and missing.name in out, out
    return "REFUSED naming the path"


@check("an EMPTY fixture reds at the precondition, never downstream")
def test_empty_fixture_reds():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "empty.json"
    fx.write_text('{"queries": []}', encoding="utf-8", newline="\n")
    try:
        p = run_check("--data-dir", str(build_filtered()), fixture=fx)
        out = read_lines(p)
        assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
        assert "carries no queries" in out, out
        return "REFUSED — a question set with no questions cannot grade anything"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@check("an ALL-MISS fixture reds on per-id and reports the floor as not evaluated")
def test_all_miss_fixture():
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "allmiss.json"
    fx.write_text(json.dumps({"queries": [
        {"query": "what colour is the boojum", "expected_ids": ["TOOL-zNoSuchThing-9"]},
    ]}), encoding="utf-8", newline="\n")
    try:
        p = run_check("--data-dir", str(build_filtered()), fixture=fx)
        out = read_lines(p)
        assert p.returncode == 1, f"expected 1, got {p.returncode}\n{out}"
        assert "per-id RED" in out, out
        assert "not evaluated" in out, f"the floor must say so, never divide 0/0\n{out}"
        return "per-id RED, floor `not evaluated` — no 0/0"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@check("an EMPTY graded set refuses (the branch that replaced one that could not fail)")
def test_empty_graded_set_refuses():
    p = run_check("--data-dir", str(build_filtered()),
                  conf_floor='RECALL_FLOOR="spine:fts5:r@5>=0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "is EMPTY" in out and "spine" in out, out
    return "REFUSED — spine extracts to zero docs, so a floor over it grades nothing"


@check("an ABSENT pin reds naming the key, with no default")
def test_absent_pin_reds():
    p = run_check("--data-dir", str(build_filtered()), conf_floor="")
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "RECALL_FLOOR is not declared" in out, out
    return "REFUSED naming RECALL_FLOOR"


@check("a MALFORMED pin reds naming the key")
def test_malformed_pin_reds():
    p = run_check("--data-dir", str(build_filtered()), conf_floor='RECALL_FLOOR="0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "does not parse" in out, out
    return "REFUSED — a bare scalar names no cell"


@check("an OUT-OF-VOCABULARY pin reds at the pin, not inside bench.load")
def test_out_of_vocabulary_pin_reds():
    p = run_check("--data-dir", str(build_filtered()),
                  conf_floor='RECALL_FLOOR="record:fts5:r@5>=0.81"')
    out = read_lines(p)
    assert p.returncode == 2, f"expected 2, got {p.returncode}\n{out}"
    assert "names set 'record'" in out, f"a one-character typo must red HERE\n{out}"
    assert "Traceback" not in out, f"it must not raise\n{out}"
    return "REFUSED naming the key — no FileNotFoundError"


# ------------------------------------------------------------------ the anti-tautology arms


@check("--audit-fixture is green on the committed set and prints the derivation")
def test_audit_green():
    p = run_check("--audit-fixture", "--data-dir", str(build_filtered()))
    out = read_lines(p)
    assert p.returncode == 0, f"expected 0\n{out}"
    assert "h=10 R=12" in out, out
    assert "0.8182" in out, f"the pin's own derivation must print\n{out}"
    return "h=10 R=12, (h-1)/(R-1) = 0.8182 against the declared 0.81"


@check("a TAUTOLOGICAL fixture reds the overlap audit")
def test_tautological_fixture_reds():
    # The exact fixture round-2 built to defeat the prose version of this property: each question IS
    # its target record's own text. It scores a perfect r@5 and proves nothing.
    base = build_base_dir()
    recs = {}
    for ln in (base / "records.jsonl").read_text(encoding="utf-8").splitlines():
        if ln.strip():
            r = json.loads(ln)
            if "id" in r:
                recs.setdefault(r["id"], r)
    picks = ["TOOL-aStandingWrit-2", "TOOL-cSteadyMetronome-1", "TOOL-aWidenedGuide-1"]
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "tautology.json"
    fx.write_text(json.dumps({"queries": [
        {"query": recs[i]["text"], "expected_ids": [i], "from": "copied from the record"}
        for i in picks
    ]}), encoding="utf-8", newline="\n")
    try:
        p = run_check("--audit-fixture", "--data-dir", str(build_filtered()), fixture=fx)
        out = read_lines(p)
        assert p.returncode == 1, f"expected the audit to RED, got {p.returncode}\n{out}"
        assert "AUDIT RED" in out and "OVERLAP_MAX" in out, out
        return "copied text overlaps ~1.0 and reds — the property is a gate, not a sentence"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@check("a fixture whose declared `hits` disagrees with the measurement reds")
def test_hits_disagreement_reds():
    blob = json.loads(FIXTURE.read_text(encoding="utf-8"))
    for q in blob["queries"]:
        if q.get("hits") is False:
            q["hits"] = True          # claim a miss is a hit
            break
    tmp = pathlib.Path(tempfile.mkdtemp(prefix="recallfx-"))
    fx = tmp / "lying-hits.json"
    fx.write_text(json.dumps(blob), encoding="utf-8", newline="\n")
    try:
        p = run_check("--audit-fixture", "--data-dir", str(build_filtered()), fixture=fx)
        out = read_lines(p)
        assert p.returncode == 1, f"expected a red\n{out}"
        assert "declares hits=True and measures False" in out, out
        return "the hand-kept column is documentation a gate keeps honest"
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


@check("the kit payload WITHHOLDS all three gov-only files")
def test_kit_payload_withholds():
    """Asserted against the PAYLOAD, never against `selfcheck`'s exit code.

    govkit has no `exclude` key. A rule carrying one parses as TOML, passes `selfcheck` — which has
    no unknown-key arm — and ships the file anyway, which is how the first attempt at this was a
    silent no-op. The only honest observation is the resolved pool itself.
    """
    import tomllib  # noqa: PLC0415

    sys.path.insert(0, str(ROOT / "tools" / "govkit"))
    import govkit as G  # noqa: PLC0415

    desc = tomllib.loads((KIT / "kit.toml").read_text(encoding="utf-8"))
    home = "tools/memory-recall"
    ctx = {"kit": home, "relpath": "", "memory_root": "memory"}
    wild = [r for r in desc["files"] if r.get("include") == "**"][0]
    pool = {pathlib.PurePosixPath(p).name for p in G.resolve_rule_pool(ROOT, desc, wild, ctx, home)}
    leaked = {"recall-fixture.json", "check-recall.py", "test_recall_floor.py"} & pool
    assert not leaked, f"these ship to every adopter: {sorted(leaked)}"
    assert "selftest.py" in pool, "the adopter-run kit selftest must still ship"
    return f"3 withheld, selftest.py still shipped ({len(pool)} files in the ** pool)"


def main() -> int:
    for state, name, detail in _checks:
        mark = {"ok": "ok  ", "FAIL": "FAIL"}[state]
        print(f"{mark} {name}" + (f" — {detail}" if detail else ""))
    bad = [c for c in _checks if c[0] == "FAIL"]
    print(f"\n{len(_checks) - len(bad)}/{len(_checks)} arms green")
    if _BASE is not None:
        shutil.rmtree(_BASE, ignore_errors=True)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
