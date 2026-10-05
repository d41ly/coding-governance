# TOOL-aMendedFleet-64 — `govkit selfcheck --fix` writes every kit-version carrier from its `version_from` constant

**Status:** SPECCED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · closes DEPL-aHoistedPass-10 · advances TOOL-aBoundedVerdict-29 · order 64

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Every kit declares ONE version constant in its `kit.toml` `version_from`, and that value is then
copied by hand into the kit's other carriers: same-line constant copies, `gov:kit <id>@<n>` markers
in templates and READMEs, and the `version:` field of workflow harnesses. The review counted about
147 commits that move nothing but markers, and since the 09-28 switch-over the carriers are the main
source of merge conflict hunks. `govkit selfcheck` already derives each kit's carrier population and
reds on a stale one (its check 5c); nothing writes them. This unit adds `--fix` to `selfcheck`: it
writes every carrier in that derived population from the constant, then grades as `selfcheck`
always does. A bump becomes one edit and one command, which is what a lander needs before it can
mint versions itself.

## 2. Scope (IN)

- **S1** — ONE POPULATION. Check 5c's basis becomes `derive_marker_basis` in
  `tools/govkit/govkit.py`: each entry's `entry_members` plus its declared `marker_carriers`, every
  tracked path, `*.test.sh` excluded. Check 5c and S2 both read it, so the fixer writes exactly what
  the check grades. Observed by AC1 and AC6.
- **S2** — THE WRITE. `write_version_carriers` takes every entry whose `version_from` names a file
  and a pattern; the wanted value is the first dotted number on the line `entry_version` returns.
  Within that entry's basis it rewrites:
  - every `gov:kit <id>@<n>` marker whose id is this entry's and whose number differs;
  - on a line, other than the constant's own line, that matches ANY registry entry's `version_from`
    pattern followed by an optional quote and a dotted number, that number, and every
    `gov:kit <alias>@<n>` marker on the same line whose alias is not another registry entry's id,
    when either that line carries this entry's marker, or the file carries this entry's marker on
    another line and no other registry entry's marker anywhere;
  - on the constant's own line, when it carries this entry's marker, every such alias marker too.
    Its number is the source and is never rewritten.
  Observed by AC1, AC2 and AC3.
- **S3** — BYTES PRESERVED. Each file is read and written with `newline=""` in UTF-8, written only
  when a byte changed, so a CRLF working copy keeps its line endings and an untouched file keeps its
  timestamp. A file that does not decode is named and skipped. Observed by AC4.
- **S4** — THE VERB. `selfcheck` accepts `--fix` as it accepts `--write`, alone or with it; any
  other argument is refused with both flags named. Under `--fix` it runs S2 first, prints one line
  per rewritten carrier as `govkit: fix <path> · <id> <old> -> <new>`, one line per entry it moved
  naming that entry's declared `[[regenerate]]` argv as the next command, or saying it declares
  none, and a total; then it runs every selfcheck arm as without the flag, and exits with their
  verdict. Without `--fix`, `selfcheck` writes nothing it did not write at base. Observed by AC1,
  AC5 and AC6.
- **S5** — IDEMPOTENT. A second `selfcheck --fix` over a fixed tree rewrites nothing and prints a
  total of 0. Observed by AC4.
- **S6** — THE USAGE text in `tools/govkit/govkit.py` spells `selfcheck [--write] [--fix]` and one
  sentence on what `--fix` writes and what it leaves to the regenerate step. Observed by AC7.
- **S7** — A selftest arm in `tools/govkit/selftest.py` bumps a fixture entry's constant and asserts
  S2's rewrites and S5's zero. NOT OBSERVED by a criterion here: the selftest runs once at the
  close, and the arm is declared under `New arm:` in §7.
- **S8** — `memory/map/generated/symbols.json` is regenerated for the new definitions. NOT OBSERVED
  by a criterion here: `python tools/codebase-map/gen_map.py --check` at the close is its check, and
  §7 names the leg that reads it.

## 3. Non-goals (OUT)

- Running the `[[regenerate]]` argv. Rendered copies outside a kit's claim, such as
  `memory/guides/UNATTENDED-PROTOCOL.md` or a `.claude/skills/` render, are their adopter's to
  re-make; `--fix` prints the command and does not run it, because each adopter has refusals of its
  own.
- Minting the new value. The author, or the lander, writes the constant; `--fix` propagates it.
- Rewriting `tools/check-kit-versions.sh` to read the registry, or retiring its hand-declared rows.
  It stays the independent grader every criterion here reads.
- The verdict-epoch remedy text that names three files, which is the rest of
  `TOOL-aBoundedVerdict-29`: it lives in the memory-tree kit, and naming the deployer from there is
  a sibling-kit literal. This unit advances that ask; it does not close it.
- Bumping the govkit kit version, owed once at the close.

### Edges

- **hands-off** `TOOL-aMendedFleet-65` — minting kit versions at the lander, which calls this
  fixer and then the regenerate commands it prints.

## 4. Design

### Evidence

Read at the worktree HEAD `725b1449`, whose bytes under `tools/` equal base `7af5f564`'s.

- `selfcheck`'s check 5c builds `_claimed[eid]` from `entry_members` and `marker_carriers`, every
  tracked path but `*.test.sh`, and fails on a `gov:kit <eid>@<n>` marker whose number differs from
  the constant. A second loop fails on a marker for an entry that neither claims its file nor
  declares it. That is the population S1 lifts.
- `tools/check-kit-versions.sh` grades, besides markers: `KIT_UNATTENDED_VERSION` copies in
  `check-unattended.sh`, `check-pass-order.sh` and `check-brief-recorded.sh`, each with its own
  same-line marker; `version: '<n>'` in `tools/workflows/tier2-review.js`, whose line also carries a
  `gov:kit tier2-review@` alias and a `gov:kit review-harness@` marker; and `version: '<n>'` on line 3
  of the two drift-audit harnesses, whose only marker is `gov:kit drift-audit@` on line 15. Its
  clean run reports 16 declared carriers, DERIVED by the script on each run.
- `review-harness` declares `version_from` with pattern `version: ` over `tools/workflows/`, which
  also holds the drift-audit harnesses. A rule that rewrote every pattern match in an entry's basis
  would write review-harness's number into drift-audit's `version:` field. S2's ownership clause is
  the guard, and AC3 observes it.
- `tier2-review` is not a registry entry id; `review-harness` is. So the alias on that line is
  rewritten with its line, and never graded as an entry of its own.
- S2's predicate was run over the real tree before it was written here, through govkit's own
  `read_descriptors`, `entry_members` and `marker_carriers` reads, printing hits and near-misses.
  Hits outside each constant's own line: the three `KIT_UNATTENDED_VERSION` copies,
  `tier2-review.js` line 3, and line 3 of the four drift-audit harness files, rendered and template.
  Near-misses, all correctly excluded: line 3 of the drift-audit harnesses under review-harness,
  and the `version:` lines of `unattended-build.js`, its template, `unattended-unit.js` and
  `orient-counterfactual.js`, whose markers name ids no registry entry carries. A first wording
  that admitted any file carrying no OTHER registry marker would have written review-harness's
  number into those four, which is why S2 also requires this entry's own marker in the file.
  Measured 2026-10-04; DERIVED, so it is re-run by AC3.
- `DEPL-aHoistedPass-10` records the unattended README's line-1 marker as a ninth carrier outside
  the version gate's populations. It is inside check 5c's basis, so S2 writes it.
- `selfcheck` takes `--write` today and refuses every other argument; `USAGE` spells
  `govkit.py selfcheck` with no flag at all.
- Kit descriptors declare `[[regenerate]]` argv, for example `adopt-unattended.sh` for unattended
  and `adopt-memory-tree.sh --render` for memory-tree.
- `python tools/govkit/govkit.py selfcheck` exits 0 here in about 9 s, and
  `bash tools/check-kit-versions.sh` prints clean in about 5 s. PINNED, node a, 2026-10-04.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_marker_basis` | python function | `py.function`; `python tools/lexicon/lexicon.py --suggest derive_marker_basis --as py.function` answered OK |
| `write_version_carriers` | python function | `py.function`; the lexicon answered OK |
| `--fix` | `selfcheck` flag | none |

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `tools/govkit/selftest.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A `--fix` on `tools/check-kit-versions.sh`.** Its carriers are hand-declared rows, so a fixer
  there writes the enumerated list the ask says must be derived.
- **A new govkit verb.** The population and the grade are `selfcheck`'s; a second verb would build
  the basis a second time or import it, and `selfcheck` already owns a writing flag.
- **Rewrite every occurrence of the old value in a file.** A README line naming an older version in
  prose would move; S2 rewrites only a marker or a number immediately after a declared pattern.

## 5. Production-readiness checklist

- security — writes only tracked files inside a registry entry's claim or declared carriers, and
  only the number after a declared pattern or marker; no argv is built from file content.
- perf / scale — one read per basis file, the population check 5c already reads; seconds.
- error / empty / loading states — an entry with a constant and no carrier is check 5c's existing
  refusal, which still runs after the fix; an undecodable file is named and skipped.
- observability — one line per carrier rewritten, the regenerate line per moved entry, a total.
- risks — the fixer and check 5c share S1's basis, so a basis that misses a file misses it in both.
  `tools/check-kit-versions.sh` keeps its own declared rows, and every criterion grades with it.
- testing — AC1 to AC7; the arm in S7.
- migration — N/A: no stored format changes.
- user docs — S6.

## 6. Acceptance criteria

- **AC1** — When, in a `git clone --local` of the unit's tip under a short `%TEMP%` root, the
  number on the `KIT_UNATTENDED_VERSION=` line of `tools/unattended/unattended.sh` alone is edited
  to `9.99`, `bash tools/check-kit-versions.sh` exits 1 naming the three leg scripts; after
  `python tools/govkit/govkit.py selfcheck --fix`, it exits 0, and `git grep -l` for the old
  `gov:kit unattended@` value over `tools/`, excluding `*.test.sh`, prints nothing.
  Red when: S2 writes only markers, so the three same-line constant copies keep the old value and
  the version gate still exits 1.
  cost: seconds after the clone.
  fixture: the clone's `selfcheck` exits 0 before the edit; that is checked first.
- **AC2** — When the same clone's `KIT_DRIFT_AUDIT_VERSION` number in
  `tools/drift-audit/drift_report.py` is edited and `selfcheck --fix` runs, `grep -n "version: '"`
  over `tools/workflows/drift-audit-code.js` prints the new number on line 3, and
  `bash tools/check-kit-versions.sh` exits 0.
  Red when: S2's pattern-of-any-entry clause is staged to this entry's pattern only, so the
  harnesses' `version:` field keeps the old number.
- **AC3** — When the clone's `version: '` number in `tools/workflows/tier2-review.template.js` is
  edited and `selfcheck --fix` runs, line 3 of `tools/workflows/tier2-review.js` carries the new
  number in its `version:` field, its `tier2-review@` alias and its `review-harness@` marker, while
  `git diff --quiet -- tools/workflows/drift-audit-code.js tools/workflows/drift-audit-state.js
  tools/workflows/unattended-build.js tools/workflows/unattended-unit.js` exits 0.
  Red when: the ownership clause is staged out or loosened to "no other registry marker", so
  review-harness's number lands in a harness that versions under another id.
- **AC4** — When `selfcheck --fix` runs a second time in the AC1 clone, its total reads 0 and
  `git status --porcelain` prints what it printed after the first run; and when a carrier is
  converted to CRLF with `unix2dos` before the first run, `git diff --stat` after it shows one
  changed line in that file, not every line.
  Red when: the fixer rewrites unchanged files, or writes LF over a CRLF working copy.
- **AC5** — When `python tools/govkit/govkit.py selfcheck` runs without the flag after AC1's edit,
  it exits 1 naming check 5c's stale markers, and `git status --porcelain` lists only the edited
  file.
  Red when: the plain verb writes.
- **AC6** — When the AC1 run's output is read, it carries a `govkit: fix` line for each rewritten
  carrier, and one line naming `adopt-unattended.sh` as the unattended entry's regenerate command;
  and `python tools/govkit/govkit.py selfcheck --bogus` is refused naming both `--write` and `--fix`.
  Red when: a moved entry prints no next command, or an unknown flag is accepted.
- **AC7** — When `grep -n "selfcheck \[--write\] \[--fix\]" tools/govkit/govkit.py` runs, it hits
  the `USAGE` text.
  Red when: the flag ships unspelled in the usage.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit runbook parity` · `codebase-map coverage + freshness` · `kit version markers` · `recall floor arms` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `recall floor`

New arm: `tools/govkit/selftest.py` · a fixture entry whose constant is bumped alone, then `selfcheck --fix`; a second run rewriting nothing; staged red by skipping the same-line clause · none

## 8. Open questions

- **F1** — Where does the fixer live?
  Options: a `--fix` on `selfcheck`; a new govkit verb; a `--fix` on the version gate script. The
  gate script's carriers are declared rows, which is the enumeration the ask wants gone; a new verb
  re-derives the basis `selfcheck` owns.
  RESOLVED (agent, 2026-10-04, delegated): `selfcheck --fix`, per S4.
- **F2** — Which carriers beyond markers does it write?
  Options: markers only; every line matching the entry's own pattern; every line matching any
  entry's pattern under an ownership clause. Markers only leaves the same-line constant copies and
  the harness `version:` fields stale, so the version gate stays red after the fix. The entry's own
  pattern misses the drift-audit harnesses and, for review-harness, would write into them.
  RESOLVED (agent, 2026-10-04, delegated): any entry's pattern under the ownership clause, per S2.
- **F3** — Does `--fix` run the regenerate commands?
  Options: run them; print them. Each adopter has its own refusals and writes beyond markers, and a
  selfcheck flag that ran them would write outside every kit's claim.
  RESOLVED (agent, 2026-10-04, delegated): print them, per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 64, report items [A#5] and [B#12],
  the two asks, check 5c and `entry_version` in `tools/govkit/govkit.py`, and the version gate's
  declared rows, read at base.
- rev-2 · 2026-10-04 · S8 · §4 · §7 · M2 cross-read: the two Python definitions move
  `memory/map/generated/symbols.json`, which the build's other Python-adding units declare with the
  coverage leg and this spec omitted.
- rev-3 · 2026-10-05 · S2 · the build pass: `tier2-review.template.js` holds review-harness's
  constant AND a `gov:kit tier2-review@` alias on that one line, and rev-2 excluded the whole
  constant line, so a bump left the template's alias on the old number while the rendered `.js`
  moved; the alias clause now reaches the constant's own line, never its number.

## 10. Reuse audit

The seam is `selfcheck`'s check 5c in `tools/govkit/govkit.py`, whose basis S1 lifts into one
function, with `entry_members`, `entry_version` and the `marker_carriers` key it already reads.
`python tools/codebase-map/reuse_lookup.py "rewrite every kit version marker from the declared
version constant"` returned `marker_pair` and `declares_outcome_for` in govkit and the kit-dir
resolvers, none of which writes a carrier; `git grep` for a writer of `gov:kit` markers over
`tools/` found none, and the version gate and check 5c both only read. Recall returned the two asks
this unit names, `DEPL-cMendedVintage-5`, which records that check 5c makes a bump move every
marker carrier, `DEPL-dGaugedVintage-5` on the marker each entry ships, and a closing review
proposing that the descriptor be the single source. Where the report and the tree disagree: the
synthesis corrected "no single version source" to "`version_from` exists and the carriers are not
derived from it", which is what this unit builds on.

Recall terms used: `python tools/memory-recall/query.py "how are kit version carriers kept in step
with the version_from constant, and is there a fixer" --terms "version_from kit.toml gov:kit marker
carrier bump check-kit-versions selfcheck 5c marker_carriers fix"`
