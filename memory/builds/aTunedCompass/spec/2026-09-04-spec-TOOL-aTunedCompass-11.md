# TOOL-aTunedCompass-11 — the map log gains the run-state reader a closed unit's acceptance claimed

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-2 · base c4fcf5ad · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aTunedCompass-1-spec-audit-round1.md) | spec-audit | TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 |

<!-- /gen:spec-records -->

## 1. Goal

Land the half of `TOOL-aClosedDocket-2` that did not land, and correct the acceptance ledger line that
says it did. That unit is CLOSED and ratified, its title is that `reuse_lookup.py` logs and the
run-state item counts either probe, and the logging half shipped. The reading half did not. This unit
ships the reader and makes `TOOL-aTunedCompass-8`'s new field land against something that consumes it.

## 2. Scope (IN)

- **S1** — the `reuse-probed` item in `tools/unattended/unattended.sh` (`:3588`) counts rows from the
  MAP log as well as the recall log, which is what `TOOL-aClosedDocket-2`'s S5 specified.
- **S2** — a `MAP_CLI` declaration beside `RECALL_CLI`, optional and blank by default, which is that
  unit's S4. Blank must mean not-adopted and announce the skip, exactly as the `RECALL_CLI` arm does,
  because a skip that looks like a pass is indistinguishable from coverage.
- **S3** — the declaration is a DECLARATION, never a probe of guessed paths. That unit's own spec
  records getting this wrong three ways, and the reasons still bind: a literal kit path breaks the
  declarations-not-constants rule, it raises the carried-prefix ratchet because it arrives verbatim in
  an adopter installed at another prefix, and it is unreachable by a self-test that runs the driver
  from outside the tree under test.
- **S4** — the acceptance ledger at
  `memory/builds/aClosedDocket/build/2026-08-31-build-TOOL-aClosedDocket-1-acceptance-ledger.md` gains
  a correction line for its AC8. That line asserts a merge-bar run was "check 22's key-table join
  accepting `MAP_CLI`", and `MAP_CLI` appears nowhere in the product. The correction supersedes rather
  than rewrites, because the ledger is evidence and rewriting evidence is worse than annotating it.
- **S5** — the same correction is recorded against `TOOL-aClosedDocket-2` itself, whose scope items S4
  and S5 describe work that is not in the tree. The unit stays CLOSED; what changes is that a reader
  meeting its claims also meets the correction.
- **S6** — three arms in the unattended kit's own suite, one per state the item can reach:
  adopted-and-present (a map log exists and its rows are counted), adopted-and-empty (declared, log
  absent — the item is UNMET and names which logs it looked for), and not-declared (`MAP_CLI` blank —
  an announced skip). The middle one is the state that silently passed before, so its RED is observed
  before the arm is written. §7 routes them, and until this item existed §7 pointed at an `S6` this
  section did not have.
- **S7** — `MAP_CLI` is declared in EVERY carrier the kit's own check 22 joins, not in the driver
  alone. Measured against `RECALL_CLI`, which is the shape this key copies, the set is:
  `tools/unattended/.unattended.conf.example` (`:74`); the `reuse-probed` row and the §8 key table in
  `tools/unattended/PROTOCOL.template.md` (`:338`, `:472`); the re-rendered
  `memory/guides/UNATTENDED-PROTOCOL.md`; `optional_keys` in `tools/unattended/kit.toml` (`:62`); and
  the driver's default init. Check 22 (`tools/unattended/check-unattended.sh` `:1372`-`:1420`) joins
  the example conf against the protocol's key table in BOTH directions, and check 10 (`:1323`-`:1345`)
  byte-compares the installed guide against the template after prefix substitution. `unattended kit
  gate` runs with `subject = repo` and a null guard, so it is on every ordinary bar: a landing commit
  that declares the key in one place reds with `undocumented in the protocol: MAP_CLI`.
- **S8** — the new protocol rows are priced against that document's byte cap, the way
  `TOOL-aTunedCompass-7` prices the manifest's. A cap that acts silently as an editor is the failure
  mode; the row states what it costs and what, if anything, leaves to pay for it.
- **S9** — `MAP_CLI` is declared in THIS repo's own `.unattended.conf` beside `RECALL_CLI` (`:70`),
  not only in the kit's example. Left undeclared here the reader ships switched off in the tree that
  built it, `TOOL-aTunedCompass-8`'s new field lands against a consumer reading nothing, and the
  announced-skip path (`tools/unattended/unattended.sh` `:3624`-`:3625`) makes that look like a pass.
- **S10** — `.unattended.conf` is the ninth entry on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md` (`:6`), so S9's edit owes the kickoff manifest a `last-audit`
  re-stamp, an advanced `last-body-change`, and a delta line in the commit message. Check 5 of
  `skills/session-kickoff/manifest-check.sh` is "no unaudited watch drift" and its pre-commit variant
  blocks, so this is a refused commit rather than a review argument. `TOOL-aTunedCompass-2` carries
  the same obligation as its S10 and `TOOL-aTunedCompass-3` as its AC10, both for `.memory-tree.conf`;
  this unit was the one spec in the set touching a watched path without it.

## 3. Non-goals (OUT)

- Not putting this item on the merge bar. `reuse-probed`'s own header explains why and the reasoning
  still holds: the evidence lives in the git common dir, is neither tracked nor pushed, and a leg
  could only ever report a dead probe in a fresh clone. This unit extends what the item reads, never
  where it runs.
- Not adding the returned paths to the log row. That is `TOOL-aTunedCompass-8`, which is BLOCKED on
  this unit and sequenced after it.
- Not widening what the item OBSERVES. Its header already declares its blind spots — that it cannot
  tell whether a probe ran for this build, whether its question was relevant, or whether its answer
  was read. This unit adds a second log to count, not a second claim to make.
- Not reopening `TOOL-aClosedDocket-2`. An id in the units region at a pinned BASE may not leave it,
  and its status stays CLOSED.

## 4. Design

The measurement that makes this a unit rather than a hunch: `grep -rn "MAP_CLI" tools/ .unattended.conf`
returns nothing, and `lookups.jsonl` appears exactly once in the product, at its writer in
`tools/codebase-map/reuse_lookup.py` (`:442`). So the map log is a write-only surface, and the
closed unit's AC8 asserts a gate accepted a declaration that does not exist.

That last part is the reason S4 and S5 are in scope at all. This build's unit 1 corrects two records
that assert facts their sources refute; this is a third, and it is the most serious of them, because
an acceptance ledger is the strongest claim shape this repo has. A ledger line that names a passing
gate as evidence for a thing that is absent is worse than an unfinished unit, since the next reader
has no reason to doubt it.

The row grammar the map logger writes is already compatible. `TOOL-aClosedDocket-2`'s S3 records that
`type` is the field the existing reader filters on first, and the map writer emits it, so the reader
change is a second path to count rather than a second parser.

### Files touched

rev-2 had no such list, which is why S7's five carriers and S10's re-stamp were both invisible: a
Tier-2 spec with no Files-touched table cannot be read for what it forgot to name.

| File | Why |
|---|---|
| `tools/unattended/unattended.sh` | the `reuse-probed` reader (`:3588`), and the key's default init |
| `tools/unattended/.unattended.conf.example` | the declaration, beside `RECALL_CLI` (`:74`) |
| `tools/unattended/PROTOCOL.template.md` | the §8 key-table row (`:472`) and the `reuse-probed` row (`:338`), which still describes a recall-only item |
| `memory/guides/UNATTENDED-PROTOCOL.md` | re-rendered from that template; check 10 byte-compares them |
| `tools/unattended/kit.toml` | `optional_keys` (`:62`) |
| `.unattended.conf` | this repo's own declaration (S9), beside `RECALL_CLI` (`:70`) |
| `memory/guides/SESSION-KICKOFF.md` | the `last-audit` re-stamp S10 owes for the watched file above |
| the unattended kit's test suite | S6's three arms |
| `memory/builds/aClosedDocket/build/2026-08-31-build-TOOL-aClosedDocket-1-acceptance-ledger.md` | S4's correction |
| `TOOL-aClosedDocket-2`'s spec | S5's correction |

## 5. Production-readiness checklist

- security — a second declared CLI path is a second thing an adopter's conf can point at. It is read
  for EXISTENCE only and never executed by this item, so the surface added is a path read, not an
  exec. That property is what makes the declaration safe and it is asserted, not assumed.
- perf / scale — N/A. One extra file read per close, on a log already bounded by the git common dir.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the three states ARE the design, and S6 gives each an arm:
  adopted-and-present, adopted-and-empty (UNMET, naming which logs it looked for), and not-declared
  (announced skip). The middle one is the state that silently passed before.
- observability — the not-adopted skip announces itself per S2, because a skip that looks like a pass
  is indistinguishable from coverage. The UNMET path names the logs it searched, so an unmet item is
  diagnosable rather than merely red.
- risks — the key can be declared in some carriers and not others, which check 22 catches in both
  directions and which S7 exists to prevent. The second risk is S8's: the protocol document carries a
  byte cap and new rows are spend against it.
- testing + left-shift gates — S6's three arms, run through `bash tools/unattended/run-unattended-gates.sh`
  on demand per the owner ruling of 2026-08-23. The left-shift for the class that produced H1 and H2
  is a hygiene check refusing a Tier-2 spec with no §4 Files-touched list, plus one intersecting that
  list against the live `watch:` line; both are recorded against this unit in the round-1 review.
- migration / rollback — an adopter who declares nothing keeps today's behaviour exactly; the key is
  optional by construction. Rollback is one arm, and reverting restores the recall-only count.
- user docs — N/A. `help/` pages cover user-facing features; the protocol row S7 adds IS the
  documentation for this one, and it is a required carrier rather than an optional page.

## 6. Acceptance criteria

- **AC1** — `grep -rn "MAP_CLI" tools/` returns the declaration, its reader, and its self-test arms —
  the command that returns nothing today is the acceptance for this unit.
- **AC2** — With a map log present and a recall log absent, the `reuse-probed` item is MET, verified
  by running the driver's check against a fixture built that way. That is the arm the closed unit
  claimed and never had.
- **AC3** — With neither log present and both CLIs declared, the `reuse-probed` item in
  `tools/unattended/unattended.sh` is NOT met and names which logs it looked for, so an unmet item is
  diagnosable rather than merely red.
- **AC4** — With `MAP_CLI` blank, the item announces a skip naming the missing declaration rather than
  passing silently, exercised by its own arm.
- **AC5** — `bash tools/unattended/run-unattended-gates.sh` passes, and the record states it was run
  on demand because that kit's suites are on no bar by owner ruling.
- **AC6** — The correction lines from S4 and S5 are present, and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with them staged.
- **AC7** — `bash tools/unattended/check-unattended.sh` exits 0 with the key present, which is checks
  10 and 22 passing together: the installed guide still byte-matches the template after prefix
  substitution, and the example conf and the protocol key table name the same key set in both
  directions. Staging the key in the driver alone and observing check 22 RED is the before half.
- **AC8** — `grep -n MAP_CLI .unattended.conf` returns the declaration, and a `reuse-probed` check run
  in THIS tree counts map-log rows rather than taking the announced-skip path.
- **AC9** — `bash skills/session-kickoff/manifest-check.sh` exits 0 on the landing commit against a
  re-stamped `last-audit`, in the shape `TOOL-aTunedCompass-2`'s AC8 uses.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with `unattended kit gate`, `memory hygiene`, `kit version
markers` and `kickoff-manifest ratchet` the legs that bind. The last of those is owed by S10: this
unit edits `.unattended.conf`, which is on the manifest's `watch:` line, and the ratchet's pre-commit
variant refuses the commit rather than reporting it. `unattended kit gate` runs `check-unattended.sh`
with `subject = repo` and a null guard, so it is on every ordinary bar and AC7 binds there.

The unattended kit's `*.test.sh` suites are on no bar by the owner ruling of 2026-08-23, so S6's arms
run through `bash tools/unattended/run-unattended-gates.sh` on demand and the record must say so
rather than reporting them green from an ordinary bar.

## 8. Open questions

**F1 RESOLVED (agent, 2026-09-05, delegated): annotate both, as superseding notes rather than edits.**
The two narrower options are vetoed on this spec's own acceptance text: AC6 requires the correction
lines from S4 AND S5 to be present, so annotating only the ledger, or neither, fails a criterion
already written here. Nothing in the second veto is tripped either — a closed build's spec and its
acceptance ledger are build records, not one of the governance carriers M11 names, and a superseding
note is exactly the act the append-only rule contemplates: the ratified decision is not rewritten, a
reader meeting the claim meets the correction beside it. `TOOL-aClosedDocket-2` stays CLOSED, per §3.

- **F1 — does the correction belong on the closed unit, or only in this build's record?** S4 and S5
  annotate a CLOSED, ratified unit and its acceptance ledger. Options: annotate both, so a reader
  meeting the claim meets the correction; annotate only the ledger, since that is where the false
  assertion lives; or record the correction only here and leave the closed unit untouched, on the
  principle that a ratified record is not rewritten.
  Recommendation: annotate both, as a superseding note rather than an edit. The append-only rule
  protects against rewriting a ratified decision, and a note that says "this claim was measured false
  on this date, here is the unit that closed it" is exactly what that rule contemplates. Left open
  because touching a ratified unit is the owner's call and the third option is defensible.

## 9. Revision log

- rev-1 · 2026-09-05 · first draft. Added by the restructure recorded in the build README, after the
  owner chose to land the missing reader before shipping `TOOL-aTunedCompass-8`'s new field. Scope
  grew beyond the reader once the closed unit's acceptance claim was checked and found false.
- rev-2 · 2026-09-05 · F1 resolved under the standing mandate, M3's rule. The two narrower options
  fail AC6, which names both correction lines; the survivor trips no veto, since a build record is
  not a governance carrier. No scope, acceptance or gate text moved.
- rev-3 · 2026-09-05 · round-1 spec audit folded, findings H1, H2, M1, M2, M4 and M7 — the most of
  any unit in the set, and the root cause of five of the six was that rev-2 carried no §4
  Files-touched list, so nothing made the omissions visible. H1 — a new `.unattended.conf` key has
  six carriers and the spec named one; check 22 joins the example conf against the protocol key table
  in both directions and check 10 byte-compares the installed guide, so the landing commit would have
  red with `undocumented in the protocol: MAP_CLI` on an ordinary bar. S7 names the set, S8 prices the
  protocol's byte cap, AC7 observes both checks. H2 — `.unattended.conf` is on the manifest's `watch:`
  line, so the edit owes a `last-audit` re-stamp the pre-commit ratchet BLOCKS on; S10 and AC9 carry
  it in unit 2's shape, and `kickoff-manifest ratchet` joins §7. M4 — `MAP_CLI` was never declared in
  this repo's own conf, so the reader would have shipped switched off in the tree that built it and
  the announced-skip path would have made that look like a pass; S9 and AC8. M2 — §7 pointed at an S6
  that did not exist and the three arms §5 names were unscoped; S6 now holds them. M1 — §6 relabelled
  `- **ACn** — `, since this spec's own F1 resolution cites AC6 and check 23 reds at CLOSED on a
  section that numbers no criterion. M7 — §5 restored to the full ten labelled lines.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a run reads its own probe log to prove an orientation
probe ran"` returned `read_text`, `run`, `read` and `owners_of` — four generic seams matched on the
stems `read`, `run` and `own`, none of which is the subject. **No existing seam fits from the probe.**
The seam was found by reading: it is the `reuse-probed` case in `tools/unattended/unattended.sh`
(`:3588`), whose `RECALL_CLI` arm is the exact shape the `MAP_CLI` arm copies, and the specification
of both arms already exists in `TOOL-aClosedDocket-2`'s S4 and S5. This unit implements a spec that
was written, reviewed and closed rather than designing a new one, which is the strongest form of reuse
available here.

Recall terms used: reuse-probed liveness map log MAP_CLI RECALL_CLI unattended definition-of-done
declaration adopter skip announce acceptance ledger
