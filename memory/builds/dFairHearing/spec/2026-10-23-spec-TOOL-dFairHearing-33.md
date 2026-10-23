# TOOL-dFairHearing-33 — the version check reads every declared kit version constant through govkit's own reader, so no carrier's form escapes a typed pattern

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 23 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-33-deviation-331.md](../build/2026-10-23-build-TOOL-dFairHearing-33-deviation-331.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-1-spec-writer.md) | journal | — |
| [2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-33-promoted-fix-brief.md) | research | TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |
| [2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-33-37-spec-audit.md) | spec-audit | TOOL-dFairHearing-35 TOOL-dFairHearing-34 TOOL-dFairHearing-36 TOOL-dFairHearing-37 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit's finding id 22 (item H1, HIGH, shared with id 31,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md`) is
closed. `TOOL-dFairHearing-31` S3 matches version lines with one typed pattern,
`KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@`, over four directories. The build writes version constants
that pattern cannot match: the shell form of `tools/check-wiring.sh:51`, `KIT_CHECK_WIRING_VERSION=1.34`
with no spaces, and the marker kind of `coding-governance-agents.template.md`, `governance-template:
v4.4`. A hand bump there exits 0. This unit closes the constant half of item H1: it reads every kit's
declared constant through the registry, each by its own declared pattern, at the base and at `HEAD`,
and reports any value that moved. The marker half, the four-directory pathspec, is id 31's, in
`TOOL-dFairHearing-34`.

## 2. Scope (IN)

- **S1** — The population is declared, not typed. Every registry entry that
  `read_descriptors(root, load_registry(root), Report())` in `tools/govkit/govkit.py` returns and
  whose `version_from` names a file is read, and its value at each end is
  `resolve_version_value_at(root, desc, <commit>)` (`tools/govkit/govkit.py:13314`), the one reading
  `derive_epoch_state` grades a kit's epoch by. Each constant is matched by its own entry's `pattern`, so the shell,
  Python, JavaScript, harness `version: ` and marker-kind forms are each read in the form they have.
  Observed by AC1 and AC2.
- **S2** — The check. Given the base sha that unit 31's probe prints and `HEAD`, it prints `constants
  <n>`, then one `<entry> <old> -> <new>` line per moved constant, and exits 1 when it printed one and
  0 when it printed none. An entry resolving at neither end prints `absent <entry>`, and one resolving
  only at `HEAD` prints `new <entry> <value>`, a new kit under the rule's second half. Observed by AC1
  and AC2.
- **S3** — Every refusal names its cause and exits 2: an end that is not a commit, a registry that does
  not load, a constant resolving at the base and not at `HEAD`, and zero constants compared. An empty
  population is never a pass. Observed by AC3.
- **S4** — Supersession. Unit 31 S3's constant alternative, `KIT_[A-Z_]+_VERSION = `, and the clause of
  its AC1 that no constant line changed, are answered by this unit's S1 to S3 and AC1 to AC3. Unit 31's
  S1 and S2, the base, stand. Unit 31's acceptance ledger records them superseded here
  (`TOOL-dFairHearing-23` §8 F7's form). NOT OBSERVED by a criterion of this unit: it is a ledger entry
  in unit 31's record, read there.

## 3. Non-goals (OUT)

- No `gov:kit` marker and no pathspec. Markers in the files the build changed are id 31's mechanism,
  `TOOL-dFairHearing-34`; the two checks share no state and hold independently.
- No change to the version rule (unit 27 S15) and no change to govkit: the probe imports its readers.
- No new gate leg and no committed checker. The check is a scratch probe run at this unit's pass, as
  unit 31's is, and `kit version markers` keeps its own job.
- No help page: `help/` covers no build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-31` — the resolved base its probe prints, `base <sha> from <source>`; without it this check has no first end to read
- **hands-off** `TOOL-dFairHearing-40` — the round-5 spec audit's minors on this spec, ids 2, 3, 10, 17, 20, 23, 26, 31 and 33: AC1's build-wide Red when half re-read at the build's last pass commit on `base.py`'s sha, this unit's ledger naming whether `GATE_BASE` was set when AC1 ran, `RuntimeError` caught, `new` refused unless the descriptor is absent at the base, the registry read at both ends, AC3's two unstaged refusals and the `absent` and `new` outcomes staged, and §4's `(none declared)` sentence corrected (its S1 to S4, S18, S19, S26, S28 and S29)


## 4. Design

### Evidence

Measured on 2026-10-23 with the script below, PINNED. Over `3708a705..HEAD` it printed `constants
19` and exited 0; 19 is the count of `version_from = { file` lines across the kit descriptors. Over
`7d98741e3~1..7d98741e3`, a mint commit, it printed `absent branch-reconcile`, `absent roles`,
`constants 17`, `check-wiring 1.32 -> 1.33` and `unattended 1.100 -> 1.101`, and exited 1: two
shell-form constants outside the four directories unit 31 reads. A base of `nosuchref` exited 2, and a
root with no registry exited 2 naming the module that did not load.

### The check

```python
# constants.py <repo root> <base> [<head>] — every declared kit version constant, read at both ends
import pathlib, subprocess, sys
root = pathlib.Path(sys.argv[1]).resolve()
base, head = sys.argv[2], (sys.argv[3] if len(sys.argv) > 3 else "HEAD")
def refuse(why):
    print(f"version-constants: nothing compared: {why}", file=sys.stderr)
    sys.exit(2)
for end in (base, head):
    p = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "-q", f"{end}^{{commit}}"],
                       capture_output=True, text=True)
    if p.returncode:
        refuse(f"{end} does not resolve to a commit")
sys.path.insert(0, str(root / "tools" / "govkit"))
try:
    import govkit
    r = govkit.Report()
    descs = govkit.read_descriptors(root, govkit.load_registry(root), r)
except (ImportError, OSError, ValueError, KeyError) as e:
    refuse(f"the kit registry does not load: {e}")
if r.problems:
    refuse("; ".join(r.problems))
read, hits = 0, []
for eid, (d, _dpath) in sorted(descs.items()):
    vf = d.get("version_from") or {}
    if "none" in vf or not vf.get("file"):
        continue
    old = govkit.resolve_version_value_at(root, d, base)
    new = govkit.resolve_version_value_at(root, d, head)
    if old.startswith("(") and new.startswith("("):
        print(f"absent {eid}")
    elif old.startswith("("):
        print(f"new {eid} {new}")
    elif new.startswith("("):
        refuse(f"{eid}: its constant resolves at {base} and not at {head}: {new}")
    else:
        read += 1
        if old != new:
            hits.append(f"{eid} {old} -> {new}")
if read == 0:
    refuse("no declared constant resolved at both ends")
print(f"constants {read}")
for h in hits:
    print(h)
sys.exit(1 if hits else 0)
```

The pass writes it with its file-writing tool under its scratch directory. A value that does not
resolve comes back from govkit as a parenthesised sentinel, `(unresolvable)` or `(none declared)`,
which is what the `(` test reads.

### What it does not check

A copy of a constant: a same-line `gov:kit` marker, a rendered file, or a harness's render of its
template's `version: ` field. Markers are `TOOL-dFairHearing-34`'s; a render is held to its template by
the render's own parity leg. Nor does it read the descriptors at the base: an entry whose
`version_from` itself moved in the build is read by its `HEAD` declaration at both ends.

### Files touched (estimate)

None. The check is a scratch probe, and its result is a line in this unit's acceptance ledger.

### Alternatives rejected

- **Widen unit 31's regex with `^KIT_[A-Z_]+_VERSION=` and `governance-template: v`.** The next carrier
  form is missed the same way; the registry already declares every form, and govkit reads it.
- **Diff the whole tree with one pattern.** Prose quoting a constant would read as a version line,
  and the pattern is still typed.

## 5. Production-readiness checklist

- security — N/A: a read-only scratch probe; git runs with argv lists and no shell.
- perf / scale — two `git show` reads per declared constant, 19 today.
- error / empty / loading states — S3's four refusals, each exit 2 naming its cause; zero constants
  compared is a refusal.
- observability — the count of constants compared prints before any finding.
- risks — a kit removed by the build refuses rather than passes; this build removes none.
- testing — AC1 to AC3 as probes over this repository's own history.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`constants.py` is the script of §4, written under the pass's scratch directory, and `<base>` is the
sha unit 31's probe prints at this unit's commit.

- **AC1** — When `python constants.py . <base>` runs at this unit's commit, it prints `constants <n>`,
  where `<n>` equals the count `grep -h "^version_from = { file" tools/*/kit.toml tools/govkit/entries/*.kit.toml | wc -l`
  prints, prints no `->` line, and exits 0.
  Red when: a kit's declared constant moved on the branch, or fewer constants are compared than the
  descriptors declare.
  figure: `<n>` is DERIVED at observation time; it was 19 on 2026-10-23.
- **AC2** — When `python constants.py . 7d98741e3~1 7d98741e3` runs, it prints `check-wiring 1.32 ->
  1.33` and `unattended 1.100 -> 1.101` and exits 1.
  Red when: it exits 0, which means a shell-form constant outside the four directories reads as
  unchanged, the defect id 22 names.
  figure: the two lines are PINNED, measured on 2026-10-23 at mint commit `7d98741e3`.
- **AC3** — When the probe runs with `nosuchref` as its base it exits 2 naming the ref before any
  comparison. When its root is a scratch repository under `%TEMP%/fcr` holding one commit and no
  registry, it exits 2 naming the registry.
  Red when: either exits 0, which is the vacuous pass on an empty population.
  fixture: the repository under `%TEMP%/fcr`, made by the probe and removed after it.

## 7. Gates

`kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the check is a scratch probe, observed directly by §6.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 22 (item H1, HIGH, shared with id 31) of
  the round-4 spec audit of specs 28 to 32.
- rev-2 · 2026-10-23 · §3 · the round-5 spec audit's disposal: a hands-off edge to TOOL-dFairHearing-40 (nine minors).

## 10. Reuse audit

The seam extended is govkit's version reader: `read_descriptors` (`tools/govkit/govkit.py:13238`),
which `python tools/codebase-map/reuse_lookup.py "read every kit version constant at a commit and
compare two commits"` ranked as a SEAM with fan-in 3, and `resolve_version_value_at`
(`tools/govkit/govkit.py:13314`), which `derive_epoch_state` reads, so this probe and the epoch leg
cannot disagree about a value. The recall query returned `TOOL-aMendedFleet-64`, the
carrier writer that reads every `version_from`, `DEPL-dGaugedVintage-9`, which made the version
readable at a commit, and the audit's H1 item.

Recall terms used: `python tools/memory-recall/query.py "a version constant changed by hand in a shell form the regex cannot match" --terms "KIT_VERSION constant version_from pattern shell form resolve_version_value_at epoch hand bump carrier"`
