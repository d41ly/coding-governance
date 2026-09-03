# Acceptance ledger — DEPL-dRetiredFork-7

**Serves:** journal DEPL-dRetiredFork-7

Tier-2 · node d · 2026-09-03

The census tool is [tools/govkit/census.py](../../../../tools/govkit/census.py), its arms are
[census.test.sh](../../../../tools/govkit/census.test.sh), and the three measurements are records
1, 2 and 3 beside this one.

## Where the measurement disagreed with the spec

Three of the spec's figures were measured at `b0108f13` and do not reproduce today. **In each case
the measurement wins and the difference is recorded**, because this census is the input to every
other unit's sizing and a number carried forward unchecked would mis-size the build.

| Spec said | Measured 2026-09-03 | Why |
|---|---|---|
| 23,384 blobs in gov's index | 25,837 objects with a path label | gov's history grew; the tool DERIVES this and never carries it |
| gov `gen_build_index.py` is 2519 lines / 59 defs | 2785 lines / 63 top-level symbols | **this build changed that file** — the rot is self-inflicted, which is the point |
| swydee: 3 files diverge | **1** diverges | one of the three the spec named is a gov VINTAGE, not a divergence |

The third is the one that matters. The spec's §2 S2 calls `tools/run-gates.sh` "a 70-line ancestor
of gov's 1480-line runner" and counts it among the divergent. The line counts are exactly right —
70 against 1480 — but its blob is byte-identical to gov commit `a86fc3ee` (2026-08-08), which by
this census's own definition is DRIFT. An ancestor is a vintage. The only true divergence in
swydee's kit population is `tools/gate-legs.json`, and gov's own registry says that file is
supposed to be project-authored: *"a target's leg list is emitted from the selected kits'
`[[gate_leg]]` blocks, never copied."*

**So swydee's convergence cost is not low, it is approximately zero**, which strengthens F3's
recommendation considerably. F3 asked that the measurement go in front of the owner because it may
invert the ordering argument. It does — more than the spec knew.

## Acceptance criteria

**Evidences:** DEPL-dRetiredFork-7

- AC1 — MET — `python tools/govkit/census.py --adopter C:/projects/incms/main` — its section
  *UNDECLARED FORK, still declared `engine` (11)* names eleven files, reproducing the spec's number
  exactly, `scripts/recall/extract.py` among them. The predicate is pinned: kits.json's per-kit role
  is `engine` AND the on-disk blob is in no gov commit ever. Under install.json's role instead the
  answer is 13, and the two registers disagreeing is itself AC7's finding
- AC2 — MET, and exceeded — the same command against `C:/projects/nicocares/main` names
  `.githooks/pre-commit` and `scripts/check-wiring.sh` under *In NO register at all*, both FORK.
  It names nine more the registers omit, including `.githooks/pre-push.test.sh`, which is
  byte-identical to gov HEAD and still in neither register
- AC3 — PARTIALLY MET — the same command run with `--derive-map` over the kit dirs reports
  `DRIFT: 32`, reproducing the spec's central
  number exactly. The differing total is 33, not 35, and the divergent count is 1, not 3. See the
  table above; the reason is a mis-assignment in the spec, not a defect in the census
- AC4 — MET — `bash tools/govkit/census.test.sh` arms 5 to 7: a receipt mapping zero files exits 2,
  prints REFUSED and says why a zero map is not a clean tree. The failing case was STAGED and
  observed RED (the refusal removed, all three arms red), then restored. Arm 8 is the negative half,
  so the refusal cannot pass by always firing
- AC4b — MET — census record 1, `## PROFILE`: gov 2785 lines / 63 top-level symbols against inCMS
  518 / 14, sharing exactly three names, `_fixture` `collect` `main`. Every figure is derived by the
  tool from an AST walk; none is typed into the report
- AC5 — MET — `WIRE-INTO-PROJECT.md`, *Recording a kit file you deliberately EDITED*. The worked
  example retires one carve-out touching only its own files, and the zero state was EXECUTED both
  ways: readable registry with zero rows and zero tags passes, while the `declared -eq 0` form fails
  on the same input
- AC6 — MET — `DEPL-dRetiredFork-11` carries `govkit.py:5870` and `selftest.py:745` with the
  measurement that the flag string is its only occurrence in the file; `DEPL-dRetiredFork-12`
  carries the eleven-file count and the byte-identical one
- AC7 — MET — `DEPL-dRetiredFork-10` quotes gov's `tools/memory-recall/kit.toml:79` against inCMS's
  `kits.json` and `install.json`. Neither adopter tree was written: census.test.sh arm 11 asserts the
  tool leaves both trees byte-clean, and `git status` in each adopter is unchanged

**AC3 is reported as PARTIALLY MET rather than argued into a pass.** Its central number — 32 —
reproduces exactly. Its other two do not, and the reason is a mis-assignment in the spec rather
than a defect in the census: calling an exact-match ancestor "divergent" is the very conflation
this unit exists to remove. Recording it as MET would mean the census agreeing with a claim it
just disproved.

## What the census exposed that no criterion asked for

- **inCMS's two registers disagree on 30 paths.** The spec's S4 framed this as gov-versus-inCMS
  over one file set. It is also inCMS-versus-inCMS: `kits.json` says `diverged` where
  `install.json` says `engine`, 28 times, plus the two `recall` files where the split is
  `engine`/`forked` and `project-owned`/`forked`. Recorded in `DEPL-dRetiredFork-10`.
- **NicoCares carries eleven gov-named files in no register at all**, one of which
  (`.githooks/pre-push.test.sh`) is byte-identical to gov HEAD. A receipt that omits a file it
  could have matched by OID is surface the ratchet cannot see. Filed as `DEPL-dRetiredFork-12`.
- **The `--add-kits` defect is confirmed exactly as S5 described it.** The flag appears once in
  `govkit.py`, inside the message at line 5870, and the parser never defines it; the arm at
  `selftest.py:745` asserts the string is in stdout, so it grades the message. Filed as
  `DEPL-dRetiredFork-11`.

## The ledger contract, and why rule 3 is the load-bearing one

NicoCares' census arm (`scripts/check-wiring.sh:152`) fails when it finds zero carve-outs. That is
correct anti-vacuity reasoning — the same grep has twice been scoped so narrowly it reached none of
its subjects, and `PKG-dReadoptedGovernor-17` is one of those — but it makes the retirement
programme's SUCCESS state indistinguishable from a broken probe. The contract keeps the instinct
and moves its target: assert the REGISTRY is readable, not that the count is non-zero.

A second defect in that arm is worth recording though nobody asked: `denom` is derived with
`sort -u | tr -d '\n'`, so if the tags ever disagree about the denominator mid-edit, the two values
CONCATENATE — a tree carrying both `/19` and `/20` yields `denom=1920` and a refusal reading
"declared 19, denominator says 1920". It passes today only because all twenty tags agree.

Both belong to NicoCares. gov owns neither file, this unit edited neither tree, and the contract is
handed over rather than applied.

## Reuse

`tools/govkit/census.py` needs no registry row: `registry.toml` already exempts `tools/govkit`
wholesale — *"the deployer itself ... never installed into a target"* — and the surface is depth-1
under `tools/*`, so this file is covered by construction. F1 recommended a registry-exempt home
with a stated reason; the reason exists and is the right one, so the correct action was to VERIFY
that rather than add a duplicate row.

Deliberately not a bar leg, per the spec's §5 and §7's rule that an exemption states its
compensating check: the census reads trees gov does not own, so a leg would red where the adopters
are absent and pass by finding nothing where they are. The arms run on demand against synthetic
repositories and need no adopter present.
