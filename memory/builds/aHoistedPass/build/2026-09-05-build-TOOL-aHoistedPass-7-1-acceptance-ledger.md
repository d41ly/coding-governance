**Serves:** journal TOOL-aHoistedPass-7

# Acceptance ledger — TOOL-aHoistedPass-7

Tier-2 · node a · 2026-09-05 · spec rev-7 · pass base `10940e9a`

Two mechanisms, and they are one unit because the second exists only to feed the first.
`tools/unattended/check-brief-recorded.sh` is a new merge-bar leg, `brief-recorded`, that asserts for
every unit a build README carries as CLOSED after a dated cutoff that the commit which BUILT that
unit carries a `brief · item <id>` row whose twelve-hex hash still joins to a tracked file at the
same commit. `build_commit()` in `tools/unattended/lib-unattended.sh` is the build-commit selection
that both this leg and `pass-order history` now share, lifted out of the sibling rather than copied.

**The lift was the risky half and it is why AC7 is written as a before/after pair.** At BASE
`e828f778` the sibling leg had ZERO top-level function definitions — `grep -c '^[A-Za-z_]*() *{'`
returns 0 — because `_find_build_commit` at `:337` and `_report` at `:325` are both indented inside
the per-unit loop. The symbol existed; the seam did not, and a grep for the name cannot tell those
apart. That is the fact spec rev-3 missed and rev-4 re-opened.

**What is graded by nothing.** `tools/unattended/check-brief-recorded.test.sh` is registered in
`run-unattended-gates.sh` as a selftest, and by the owner ruling of 2026-08-23 no boundary runs this
kit's self-tests, not even `GATE_FULL=1`. Every arm below is an observation this pass made by hand.
The compensating check is a person invoking `bash tools/unattended/run-unattended-gates.sh`, and that
is the Definition of Done for any later work touching either leg.

## Acceptance criteria

**Evidences:** TOOL-aHoistedPass-7

- **AC1** — MET — `bash tools/unattended/check-brief-recorded.test.sh` drives a matched pair. With
  the row present at the build commit the leg exits 0 and prints `graded 1 closed unit`; with the
  same fixture built by a pass that recorded nothing, it exits **1** and prints
  `ARCH-tBrief-1 — BUILT at <short sha> with NO brief row in memory/builds/tBrief/RUN.md at that
  commit`. Both the unit id and the short sha of the build commit are in the message. The failing
  case was observed RED before the leg was wired into any manifest.
- **AC2** — MET — `BRIEF_RECORDED_CUTOFF="2026-09-01"` on this tree, run by hand, cost 1979 s under
  four concurrent walks. Exit **1**, 24 violations. `grep -c TOOL-dBriefedPass-2` over the whole
  output returns **0** and `grep -c 'TOOL-dBriefedPass-1 '` returns **1**, which is the criterion
  exactly: the unit that built the brief verb is clean at its build commit and its sibling that
  recorded nothing is named. No arm asserts on the exit code, because asserting on it would have
  discarded the leg. Run against the live tree rather than a scratch clone — the leg reads its cutoff
  from the working conf and everything else from `HEAD`, so a back-dated conf is the same
  observation without the clone. The conf was restored to `2026-09-05` by the same command and both
  the tree and the index were re-checked afterwards.
  **This is also §7's run-the-candidate-over-the-real-tree pass, and it printed near-misses as well
  as hits**: the 24 are real historical units across `aStagedLane`, `aWeldedTribunal`, `dRetiredFork`
  and others whose build commits carry no row at all. That population is precisely why the cutoff is
  dated at the landing rather than back-dated.
- **AC3** — MET — the `stale` fixture writes the row, then overwrites the brief file inside the SAME
  commit, so the row's hash no longer describes what it names. The leg exits **1** with
  `carries hash <row hex> for <path>, but that path's blob at the same commit is <blob>`. Staged
  because no unit in real history exercises it: measured at `c4fcf5ad`, all 26 tracked rows join.
  A second arm covers the neighbouring shape, a row naming a path that is not tracked at that commit.
- **AC4** — MET — `graded` minus `unbuilt-in-range` is the count asserted, never `graded` alone.
  Under AC2's back-dated cutoff the line reads `graded 65 closed unit(s) · 83 build(s) skipped by the
  2026-09-01 cutoff · 4 build(s) with no pinned run BASE · 8 unit(s) unbuilt-in-range`, so the
  difference is **57**, comfortably above the 1 the criterion asks for. On the landing tree the same
  line prints `graded 0` with all four counts present, and the word `clean` appears nowhere in this
  leg's output in either run — an arm asserts that directly.
- **AC5** — MET — `BRIEF_RECORDED_CUTOFF=""` exits **0** over a fixture that reds without it, printing
  the sentence that names the key and says the term is OFF; `BRIEF_RECORDED_CUTOFF="last tuesday"`
  exits **2** naming the value. The grandfathering direction has its own arm: a cutoff later than the
  build's `opened:` exits 0 and COUNTS the skipped build rather than dropping it silently.
- **AC6** — MET — `sed -i 's/brief · item/brief-item/g'` over the fixture's driver, staged on the
  otherwise CONFORMING fixture so the grammar is the only thing that changed. The leg exits **2**,
  prints `DEAD PROBE`, and `grep`ing its whole output for `graded` returns nothing — so it refused
  before printing a violation or a liveness line, which is what the criterion asks. The probe reads
  TWO literals rather than the one the spec named, and rev-6 records why: the single leading-space
  spelling occurs in the driver only as an argument to its own `grep -F`, so asserting it would have
  coupled this leg to the driver's reader instead of its writer.
- **AC7** — MET — `bash tools/unattended/check-pass-order.test.sh` exits **0** with `--- 72 arms`
  and `grep -c '^FAIL'` returning 0, with no edit to a single arm. Cost 461 s.
  **The before/after pair, and the before-run was taken FIRST.** Both readings were taken from FROZEN
  copies of the three kit scripts rather than from the live tree — `HEAD`'s bytes for the before, the
  post-lift bytes for the after — because a bash script edited while it is running is read by byte
  offset and corrupts. The first before-run was started against the live tree and abandoned for
  exactly that reason when the lift landed under it. Both ran with cwd at the repo root, so both read
  the same history and the same conf. The two outputs are **byte-identical, 519 bytes each, `cmp`
  silent**:
  `graded 86 closed unit(s) · 83 build(s) skipped by the 2026-09-01 cutoff · 4 build(s) graded with
  no run-state file · 10 unit(s) unbuilt-in-range · 0 pre-anchor violation(s) · 2 waived by
  memory/project/pass-order-waiver.txt · 2 probe(s) truncated at the 400-commit cap`, exit 0 both
  times. Every count the lift could have moved is in there — including the two the pre-anchor window
  owns, which a five-argument helper would have silently zeroed.
- **AC14** — MET — `. tools/unattended/lib-unattended.sh` from a scratch script, then
  `build_commit "HEAD~14..HEAD" TOOL-aHoistedPass-9 memory/builds/aHoistedPass "<GENERATED_INDEXES>"
  "<SHARED_RECORDS>"` answers `b0b13b5442cca4dd2d59aa319b9581f2ec467acd`, which is
  `tooling(TOOL-aHoistedPass-9): the adopter without the harness is told, on every bar` — the correct
  build commit. The seven-argument capped form answers `TRUNCATED` at a cap of 3, and a unit id no
  commit names returns 1 with no output. The same test against BASE's `_find_build_commit` cannot be
  run at all, which is the point: sourcing that file EXECUTES the leg, and the definition does not
  exist until the loop it sits inside runs.
- **AC8** — MET — `python tools/govkit/govkit.py selfcheck` exits 0, reporting
  `95 in the manifest · 70 claimed · 25 exempt` and `0 unclaimed`. That is what proves the `[[gate_leg]]`
  row in `tools/unattended/kit.toml` and the `gate-legs` claim in `memory/map/features/unattended.md`
  are both present, since the leg is claimed by no other descriptor.
- **AC9** — MET — `bash tools/check-kit-versions.sh` in both directions, with the failing direction
  INVERTED from the spec's wording and the reason recorded rather than glossed. It exits 0 with
  `tools/unattended/check-brief-recorded.sh` in the four-name loop it walks. The spec said to stage
  the constant "back to 1.17", which was written when this unit expected to inherit a 1.17 → 1.18
  bump; `DEPL-aHoistedPass-1` parked that bump to the owner, so the kit is still AT 1.17 and staging
  it there breaks nothing. Staged to `1.18` instead: the gate exits **1** with two lines, one for the
  constant and one for the same-line marker. Both were observed, then reverted.
- **AC10** — MET — `graded 0`, which is the intended day-one population and not an accident.
  `bash tools/unattended/check-brief-recorded.sh` on the landing tree prints
  `graded 0 closed unit(s) · 95 build(s) skipped by the 2026-09-05 cutoff · 0 build(s) with no pinned
  run BASE · 0 unit(s) unbuilt-in-range`, in 38 s. The latest `opened:` across every tracked build
  README is `2026-09-04`, strictly earlier than the cutoff, so no build reaches grading.
- **AC11** — NOT MET on `bash tools/unattended/run-unattended-gates.sh --all`, and stated rather
  than argued. Both rows exist in that file — `run_one "brief-recorded" checks` beside the
  pass-order row and `run_one "brief-recorded selftest" selftests` beside its sibling — and both
  budget keys resolve: the runner's `-h` derives its total from this file's own `BUDGET_*`
  declarations and now reports 164 minutes, which it could not do if either key were misspelled
  against the label transform. But **neither GROUP was invoked whole**, and that is what the
  criterion asks for. `--checks` re-runs `pass-order history`, which measured 461 s to 1937 s on this
  node today; `--selftests` is a declared 164-minute group whose largest suite is already known RED
  for four reasons that predate this build. Each leg was run DIRECTLY instead — `brief-recorded` on
  the live tree and back-dated, `check-brief-recorded.test.sh` four times, `check-pass-order.sh`
  twice, `check-pass-order.test.sh` once, `check-unattended.sh` twice, `check-playbook.sh` and
  `adopt-unattended.sh --check` once each. The second half of the criterion, `run-gates.sh` reporting
  `brief-recorded` among the legs it ran, is the PUSH BOUNDARY's — M6 charges a build pass the
  diff-scoped gates and the full bar runs once, there — so it is deferred by the method rather than
  skipped by me. What nobody has observed, said plainly: this leg's name has never been printed by
  `tools/run-gates/run-gates.sh`.

## The one thing the spec got wrong, found by a gate rather than by reading

§5 said `memory/guides/UNATTENDED-PROTOCOL.md` is NOT edited by this unit. The kit gate disagreed as
a hard failure:

```
UNATTENDED check 22 FAILED — the protocol's binding key table and the declared conf disagree, so a
key is either configurable and undocumented or documented and dead.
undocumented in the protocol: BRIEF_RECORDED_CUTOFF
```

Check 22 joins every DECLARED conf key against the protocol's section 8 table in BOTH directions, and
S5 makes the key unavoidable — it is the leg's on/off switch. So the pair owes one table row. The
edit went into `tools/unattended/PROTOCOL.template.md` and was re-installed to the rendered half by
`bash tools/unattended/adopt-unattended.sh`, because check 10 byte-compares them. The declared write
set was WIDENED through `--dispatch` before either file was touched, and the spec is at rev-7 with
the amendment and its ordering recorded. `bash tools/unattended/check-unattended.sh` then exits **0**
in 1937 s.

## The bar legs this pass ran, and the one WARN that is not mine

| leg | verdict |
|---|---|
| `unattended kit gate` | 0, after the check-22 fix above |
| `pass-order history` | 0, byte-identical before and after the lift |
| `brief-recorded` | 0 on the landing tree, `graded 0` |
| `playbook validity gate` · `unattended skill wiring` | 0 |
| `kit version markers` · `govkit selfcheck` · `install-prefix (shipped surface)` | 0 |
| `codebase-map coverage + freshness` | 0, five tests |
| `harness arms` · `kickoff-manifest ratchet` · `line length` · `check-microformats` · `check-placeholders` · `check-testsuite-counts` | 0 |
| `memory hygiene` | see below |

`bash tools/check-template-size.sh` exits 0 but prints
`TEMPLATE-SIZE WARN — coding-governance-agents.template.md grew past its recorded high-water:
48378 -> 49144 (+766)`, leaving the charter **8 bytes** under its 49152 cap. This pass never touched
that file — `git diff --cached --name-only` does not list it — so the growth and the unrecorded
high-water both predate this unit. Reported, not repaired, because re-recording another unit's
high-water is deciding that its growth was intended.

## What this unit did not do

- **It did not move the kit version.** `S8`'s bump half was struck at rev-4 and `DEPL-aHoistedPass-1`
  then parked the move itself to the owner, so the assertion is that
  `bash tools/check-kit-versions.sh` exits 0 at 1.17 WITH the new carrier's constant and marker at
  that same value. It does.
- **It did not add a waiver registry.** F1 resolved at option (a): the cutoff is dated at the landing
  and `graded 0` is accepted, because a registry would make the leg green over a list of five
  historical units rather than over a fact, and an exemption is not coverage. The cost is stated
  plainly in `.unattended.conf` beside the key: this leg's first real verdict arrives with the first
  unattended run that lands after 2026-09-05.
- **It does not grade the brief's CONTENT, nor that the brief preceded the code.** Both are section 3
  non-goals and the leg's own header says so. The row and the code land in one commit, so nothing in
  the graph carries the order.
- **It does not claim to see the harness.** `dRetiredFork` ran without one and wrote 28 rows
  byte-identical to a harnessed run's, so a `harness-used` term would reproduce
  `passes-harnessed`'s failure one layer down.
- **It raised two ratchet rows BY HAND**, which the install-prefix arm is a BAN against doing
  automatically. `tools/check-kit-versions.sh` 33 → 34, because the four-name loop is a DECLARED
  population and globbing the kit dir would make a carrier that FORGETS the constant silently absent
  from its own check. Both new files got their first rows with the fixture-internal reason the
  sibling suite's row already carries.
