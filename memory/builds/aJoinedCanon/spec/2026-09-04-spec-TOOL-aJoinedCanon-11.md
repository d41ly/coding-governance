# TOOL-aJoinedCanon-11 — the base sha resolves to a real object

**Status:** SPECCED · rev-3 · 2026-09-05 · node a · Tier-1 · base 750ca0ca · streams tooling · order 11 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 |

<!-- /gen:spec-records -->

## 1. Goal

Check 12 asserts a spec's `base` field is eight hex characters and never asks git whether those
characters name anything. Resolve it, on live specs written from a dated cutoff onward, so the next
transposed digit is caught by the bar instead of by a reviewer.

## 2. Scope (IN)

- **S1** — a new cutoff key `BASE_RESOLVE_CUTOFF` in `.memory-tree.conf`, preset blank in
  `tools/memory-tree/check-memory-hygiene.sh` above the conf source, and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`. It takes the three rule cutoffs' semantics: blank
  means off. All three carriers move in one commit: the self-test's engine-preset parity arm derives
  its key set from the engine, so an undeclared key reds this unit's own landing commit on the
  `memory-hygiene self-test` leg S2 already owes — and, unfixed, leaves an adopter a dead arm
  reading as armed.
- **S2** — a check-12 arm that resolves the `base` sha of every selected spec whose filename date is
  on or after that cutoff and whose status is not `CLOSED` or `WONTDO`, failing when the sha names
  no commit in this object database.
- **S3** — the resolution runs as ONE `git cat-file --batch-check` for the whole population, driven
  by a sentinel record the existing awk emits, not by a fork per spec.
- **S4** — a shallow repository is detected once and the arm announces its own skip rather than
  passing silently or redding every spec.
- **S5** — two fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`, named from this unit's
  `tFixture-190` block upward per the build's `order`-allocated number space: a post-cutoff live spec
  whose base does not resolve (red, observed before landing) and one whose base is the scratch
  repo's own `HEAD` (silent).
- **S6** — the `base` bullet in `memory/TEMPLATE-SPEC.md` and its byte-compared twin
  `tools/memory-tree/SPEC-TEMPLATE.template.md` gains the resolution rule and names the cutoff, in
  one commit, with the kit version marker moved in every carrier that holds it.
- **S7** — check 12's catalog entry in `memory/HYGIENE.md` and its byte-compared twin
  `tools/memory-tree/HYGIENE.template.md` state the live-only population AND the gap it accepts:
  a spec whose base does not resolve can be silenced by closing it, and a unit that goes `SPECCED`
  to `CLOSED` in one commit is never graded at all. It sits beside that entry's existing
  `SHAPE only` caveat, in the same commit as S2, because a check whose own description omits what
  it does not check is the shape charter §7 refuses.

**What this arm buys, stated plainly because the honest answer is small.** All 22 spec files carrying
an unresolvable base are CLOSED, so this catches nothing that exists. Re-derived at `750ca0ca`:
477 tracked specs carry a base over 87 distinct values, 9 of which resolve to nothing, across
`aBatchedTribunal`, `aDrainedSluice`, `aRelaxedShard`, `aUnmannedHelm` and `cSettledDocket`. The
live population is 43 specs, 42 of them carrying a base, and **every one of those 42 resolves**. The
arm is purely forward-looking and its whole value is that it stops the next one.

The class is not hypothetical, and it has a measured price in review time rather than in gate time.
`memory/builds/aRelaxedShard/reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md:436` is finding M3: a
declared base of `86eefd8f` against a real commit `86eefd8e`, a transposed eighth character, found by
a human lens and explicitly noting that check 12's grammar validates shape alone.
`memory/builds/dCarriedReceipt/reviews/2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md:3`
is the same defect on a review's own range, again caught by a person.

## 3. Non-goals (OUT)

- **Retrofitting the 22 CLOSED specs.** Rewriting a ratified record is against this tree's rule, and
  the cutoff exists so the landed corpus is carried rather than repaired.
- **Asserting the base is an ANCESTOR of the default branch**, or that it is on any particular
  branch. Reachability is a different and much more expensive question, and a spec grounded on a
  branch tip is legitimate — `aRelaxedShard-4`'s own revision log records why.
- **Any claim about the CONTENT at that sha.** This resolves an object and stops.
- **Widening the population to terminal specs.** Ruled out by the owner on 2026-09-05 as §8's answer
  to F1. The never-graded bypass that leaves is an ACCEPTED gap, documented by S7, not a deferred
  decision and not a follow-up.
- **A second channel for the value.** No environment override, for the reason `TOOL-aDeclaredBound-2`
  retired the one `SPEC10_CUTOFF` had.

## 4. Design

### Data model

One conf key, following `SPEC10_EVIDENCE_CUTOFF`'s comment shape in `.memory-tree.conf`:

```
BASE_RESOLVE_CUTOFF="<date strictly ahead of every committed spec filename date>"
```

Preset as `BASE_RESOLVE_CUTOFF=""` in `check-memory-hygiene.sh`, in the block of `*_CUTOFF` presets
that opens at `STREAMS_CUTOFF=""` and ends above the conf source — anchored by that text rather than
by line, because units at a lower `order` edit this same file first. That placement is load-bearing
rather than tidy: the script runs `set -u` and `adopt-memory-tree.sh` never back-fills a key into an
existing conf, so without the preset the gate aborts on an unbound variable in every adopter tree
whose conf predates the key.

The third carrier is `tools/memory-tree/.memory-tree.conf.example`, and it is not optional. The
self-test's engine-preset parity arm derives the engine's key set with a `grep -oE
'^[A-Z][A-Z0-9_]*_CUTOFF='` over the comment-stripped script, unions it with the `${NAME:-}` read
form, exempts only `GOV_PYTHON` and `MAP_ROOT`, and fails naming any remaining key the shipped
example does not declare, on the ground that an adopter cannot discover it. All existing engine
presets are declared there today, and that arm's own comment records this hole swallowing
`FORK_MARK_CUTOFF` and `REVIEW_VERDICT_CUTOFF` once already. For THIS unit the omission is
especially pointed: an adopter's `BASE_RESOLVE_CUTOFF` would read as armed and never resolve a sha,
which is the could-not-fail shape the unit exists to close.

The value is set strictly ahead of the newest committed spec filename date, enumerated across
`git for-each-ref refs/heads` at build time rather than trusted from this branch. The newest tracked
spec filename date on this branch is 2026-09-04, which is this build's own date, so the cutoff lands
after it and this build's own specs are grandfathered. That also grandfathers all 26 existing
`base 0123abcd` fixtures in the self-test for free, which is why S5 needs two new ones rather than a
sweep of the old.

### Inventory

The arm rides the batched awk in `check-memory-hygiene.sh` — the one assigning `bad12_raw=$(printf
'%s\n' "$c12_sel" | awk`, cited by that text and not by line because units at a lower `order` edit
this file first — which already parses `hdr` and the filename date. It takes one more
`-v bcut="$BASE_RESOLVE_CUTOFF"` binding and, for each spec that qualifies, emits a sentinel record
instead of resolving anything itself:

```
print "\002\t" f "\t" sha
```

That sentinel idiom is not new here. The same awk already emits `print "\001\t" f` for the
section-canon excerpt, and the `case "$bad12_raw" in` post-pass rebuilds it in the shell, precisely
because reimplementing a shell capability inside awk is how two implementations drift. This arm
extends that seam rather than opening a second one.

The post-pass splits `bad12_raw` on the `\002` tag, feeds the distinct shas to ONE
`git cat-file --batch-check='%(objectname) %(objecttype)'` with each line suffixed `^{commit}`, and
turns every `missing` or `ambiguous` answer back into a finding line addressed to the existing
`[ -n "$bad12" ] && fail 12` site. Verified at `750ca0ca`: `1da67d9c^{commit}` answers `missing` and
`750ca0ca^{commit}` answers a full objectname plus `commit`, and an ambiguous abbreviation answers
on its own line rather than on stderr. The `^{commit}` peel is what stops an eight-hex prefix that
happens to name a tree or a blob from passing.

**Cost.** One process for the whole run, whatever the population. A `git cat-file -e` per spec would
be 43 forks today and one per live spec forever, which is the shape the batched awk was built to
delete — its own header records replacing roughly 13 forks per spec and 42.88s of an 81.77s run.

### The probe that cannot move

A shallow clone is the could-not-fail case. Every commit outside the fetch depth answers `missing`,
so the arm would either red honestly-written specs or, if written to ignore `missing`, pass on a
clone where it can never fail. `git rev-parse --is-shallow-repository` is probed once before the
batch — verified present here, answering `false` — and on `true` the arm is skipped with one line on
**stderr**:

```
HYGIENE check 12: base-resolution arm SKIPPED — shallow repository, no base sha can be resolved here
```

Stderr, not stdout, because the script's contract is that anything on stdout is a hygiene
regression. `run-gates.sh:1110-1111` merges both streams into the per-leg log, so the skip is
durable and readable where the leg's output is read. The script's own header comment is
amended in the same commit to say that stdout carries findings and stderr carries announced skips,
because a contract that a change quietly widens is worse than the change.

Prior art worth reading before touching this: `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-7.md:106`
measured that in a `--depth 1` clone a derived-commit probe does not fail and does not return
nothing — it returns the shallow root, which resolves perfectly. The lesson carried here is that the
shallow case must be DETECTED rather than inferred from what git answers.

A blobless partial clone (`--filter=blob:none`) still holds every commit, so commit resolution is
unaffected and no separate branch is needed for it.

### Files touched (estimate)

| File | What moves |
|---|---|
| `.memory-tree.conf` | S1, the declaration and its reasoning comment |
| `tools/memory-tree/.memory-tree.conf.example` | S1, the same key, shipped blank |
| `tools/memory-tree/check-memory-hygiene.sh` | S1 preset, S2/S3 arm and post-pass, S4 probe, the header contract comment |
| `tools/memory-tree/check-memory-hygiene.test.sh` | S5, two fixtures after the `git add -A && git commit -q -m fixtures` line |
| `memory/TEMPLATE-SPEC.md` | S6, the `base` bullet |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S6, the same bytes |
| `memory/HYGIENE.md` | check 12's catalog entry gains the clause and S7's accepted-gap sentence |
| `tools/memory-tree/HYGIENE.template.md` | the same bytes |
| `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` | kit version marker only |
| `memory/map/features/memory-tree-hygiene.md` | dossier prose, refreshed on touch |

The kit version row is the trap this repo has hit twice, recorded as `TOOL-aSiftedFork-5` and
`TOOL-dSettledRoster-4`. The carrier set is the tracked non-record files matching
`grep -rl 'gov:kit memory-tree@'` plus `KIT_MEMORY_TREE_VERSION` in `check-memory-hygiene.sh`, which
holds the same number in a form that grep does not find; it measured seven at `750ca0ca` and is
re-derived at the start of this unit's build pass rather than trusted from here. They move together
or `tools/check-kit-versions.sh` reds. The constant advances by one minor in this landing, in every
carrier; no value is named here, because units at a lower `order` bump it first.

### The green fixture's base

The scratch repo commits once, at `check-memory-hygiene.test.sh`'s `git add -A && git commit -q -m
fixtures` line. The green fixture is therefore written AFTER that line, with its base substituted
from `git rev-parse --short=8 HEAD`, then added with a single `git add` — the idiom already used for
`tFixture-4`. Writing it before the commit is not an option: there is no object to name yet, and a
fixture whose green arm is green because nothing resolved would be the could-not-fail shape this
unit exists to close.

### Alternatives rejected

- **A shape-only tightening**, such as demanding more hex characters. It does not distinguish
  `86eefd8f` from `86eefd8e`, which is the actual observed defect.
- **`git rev-parse --verify`** per spec. Same answer, one fork each, and it prints a fatal to stderr
  that the batch form does not.
- **Resolving without the `^{commit}` peel.** An abbreviation naming a tree would pass.
- **Failing on a shallow clone.** It converts a legitimate CI configuration into an unlandable one,
  and the charter's rule is that a skip announces itself, not that a blind probe reds.
- **Retrofitting by widening the population to CLOSED specs.** Named in §3 and ruled out by the
  owner on 2026-09-05, closing the §8 fork: a landed green spec must not be able to go red from
  history it does not control.

## 5. Production-readiness checklist

- **security** — N/A. The arm reads the local object database and writes nothing.
- **perf / scale** — one added process per run, independent of population size. The `memory hygiene`
  leg's ceiling in `tools/gate-legs.json` is 12720 and is not expected to move; measure it against
  `<git-dir>/gate-ledger.tsv` rather than asserting it.
- **a11y** — N/A. A shell gate with no user interface.
- **i18n** — N/A.
- **error / empty / loading states** — the empty case is real and already covered: a tree with no
  post-cutoff live spec emits no sentinel, the batch is skipped, and nothing is claimed. The
  shallow case is the announced skip in §4.
- **observability** — the failure line names the file AND the sha, so the reader can see the
  transposition without opening anything. The skip line names the condition.
- **risks** — a history rewrite that drops a `base` commit reds a previously green corpus with no
  legal remedy, since editing a ratified record is forbidden. Restricting the population to live
  specs is what bounds this, per the owner's ruling on F1. The residual risk is the bypass that
  ruling accepts — a bad base silenced by closing the spec — which S7 documents rather than closes.
- **testing + left-shift gates** — S5's two fixtures. The red one is staged, confirmed red, and kept
  as a fixture rather than unstaged, which is what the self-test is for.
- **migration / rollback** — blanking `BASE_RESOLVE_CUTOFF` turns the arm off completely, and the
  rest of check 12 is untouched.
- **user docs** — `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md`, with both twins.

## 6. Acceptance criteria

- **AC1** — When the self-test's new post-cutoff fixture carries a live status and a base of
  `0123abcd`, `bash tools/memory-tree/check-memory-hygiene.test.sh` observes check 12 reporting that
  file and that sha; the red is observed before the arm lands, per the build's own rule.
- **AC2** — When the sibling fixture carries the scratch repo's own `git rev-parse --short=8 HEAD`,
  the same run reports nothing for it.
- **AC3** — When an unresolvable base sits on a `CLOSED` fixture dated after the cutoff, check 12 is
  silent on it, so the terminal-status exemption in `check-memory-hygiene.sh` is exercised rather
  than assumed.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over this tracked tree, it
  stays green, proving the 22 grandfathered specs across `aBatchedTribunal`, `aDrainedSluice`,
  `aRelaxedShard`, `aUnmannedHelm` and `cSettledDocket` are not redded.
- **AC5** — When the gate runs in a `git clone --depth 1` scratch tree, `git rev-parse
  --is-shallow-repository` answers `true`, the skip line appears on stderr, and the process exits 0.
- **AC6** — When `BASE_RESOLVE_CUTOFF` is set to `""`, the arm emits no sentinel and the run is
  byte-identical to the pre-change run over the same tree.
- **AC7** — When `python tools/memory-tree/check-arms.py --report` is run twice over
  `tools/memory-tree/check-memory-hygiene.sh` — once on the tree as this unit finds it, before any
  edit, and once after — the pair it reports for that file is UNCHANGED between the two runs,
  confirming the arm adds a finding to the existing `fail 12` site rather than a new unarmed branch.
  figure: DERIVED at observation time. The pair is deliberately not named here: units at a lower
  `order` add `fail` branches to this same file, so any literal typed now is stale before this unit
  builds, and `--report` prints the discovered counts rather than the pin.
- **AC8** — When check 12's catalog entry is read in `memory/HYGIENE.md` after the change, it states
  both the live-only population and the never-graded bypass S7 names, and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` passes, proving
  `tools/memory-tree/HYGIENE.template.md` carries those same bytes.
- **AC9** — When `grep -qE '^BASE_RESOLVE_CUTOFF=' tools/memory-tree/.memory-tree.conf.example` runs
  after the edit it exits 0, and `bash tools/memory-tree/check-memory-hygiene.test.sh` exits 0 with
  its engine-preset parity arm satisfied. The key is absent from the shipped example today, so the
  grep is red before the edit, and that arm reds from the moment the engine gains the preset until
  the example declares it — the third carrier of S1 that no other criterion reaches.

## 7. Gates

Leg names are read from `tools/gate-legs.json`, never from a list typed here.

- `memory hygiene` — `tools/memory-tree/check-memory-hygiene.sh`, the changed gate itself.
- `memory-hygiene self-test` — `tools/memory-tree/check-memory-hygiene.test.sh`, which carries S5
  and, through its engine-preset parity arm, S1's third carrier as AC9 observes it.
- `harness arms (fail branches armed or pinned)` — the leg that grades this file's arm pin, which
  AC7 asserts this unit leaves where it found it.
- `kit/dogfood doc parity` — `tools/memory-tree/kit-dogfood-parity.test.sh`, which byte-compares
  `memory/TEMPLATE-SPEC.md` against `tools/memory-tree/SPEC-TEMPLATE.template.md` and both
  `HYGIENE` and `BUILD-METHOD` pairs at `:53`.
- `tools/check-kit-versions.sh` — the seven-carrier version marker, named because the two backlog
  rows above record it being missed twice.
- `bash tools/run-gates/run-gates.sh` at the push boundary. This is kit work, so the Definition of
  Done owes `GATE_FULL=1 GATE_SELFTESTS=1`.

No new gate leg. The arm is a finding inside check 12, which is already on the bar.

## 8. Open questions

- **F1 — does the arm grade live specs only, or every post-cutoff spec?** This spec is written for
  the live-only scope: the population is post-cutoff specs whose status is not `CLOSED` or `WONTDO`.
  The argument for it is that a landed green spec must not be able to go red from history it does not
  control, and this tree forbids editing a ratified record, so a corpus-wide scope has a failure mode
  with no legal remedy. The argument against it is a bypass: a spec redding on a bad base can be
  silenced by closing it, and a unit that goes `SPECCED` to `CLOSED` in one commit is never graded at
  all. Widening to every post-cutoff spec is a one-condition change in the same `if`, so this is a
  decision and not a rebuild. **Recommendation: live-only, with the never-graded case named in
  `memory/HYGIENE.md` as a known gap rather than implied away.**
  RESOLVED (owner, 2026-09-05): live specs only — post-cutoff specs whose status is not `CLOSED` or
  `WONTDO`, because a landed green spec must not be able to go red from history it does not control
  and this tree forbids editing a ratified record, so the corpus-wide scope has a failure mode with
  no legal remedy. The bypass is ACCEPTED, not closed: naming it in check 12's own catalog entry is
  a requirement of this unit, carried as S7 and graded by AC8.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft.
- rev-2 · 2026-09-05 · §8 · §2 · §3 · §4 · §5 · §6 · folded the owner's ruling on F1: live specs
  only, and the bypass it accepts became a requirement — S7 states it in check 12's catalog entry
  and its twin, AC8 grades it, §3 and §4 stop calling the widening an open decision, and §5's risk
  bullet names the residual rather than the fork.
- rev-3 · 2026-09-05 · §2 · §4 · §6 · §7 · §10 · folded spec-audit round 1, findings H2 and H3.
  H3: S1 gains `tools/memory-tree/.memory-tree.conf.example` as its third carrier, §4 states the
  self-test's engine-preset parity arm that enforces it, the Files-touched table gains its row, AC9
  observes the grep and the self-test, and §7 names the leg that carries it. H2: AC7 stops pinning
  `20:20` and instead asserts the reported pair is unchanged across a before-and-after `--report`,
  marked `figure: DERIVED at observation time`, with `harness arms` added to §7 as the leg that
  grades the pin. Under the build's new rules, three smaller moves: anchors into
  `check-memory-hygiene.sh` and its self-test are cited by literal source text instead of line
  number in §4 and §10, the kit-version carrier count is derived with `grep -rl` instead of pinned
  at seven, and S5's fixtures are allocated from this unit's `tFixture-190` block.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve a commit sha cited in a record against the
object database"` returns no seam that resolves a git object: its ranked hits are configuration and
path resolvers (`resolve` in `tools/memory-recall/recall_conf.py` at fan-in 26, `resolve_root` in
`tools/memory-tree/row_grammar.py`, `resolve_bash` in `tools/run-gates/profile_bar.py`), none of
which touches the object database. **No existing seam fits for sha resolution.** The seam this unit
extends is instead the one the probe cannot see because it is not a symbol: the awk `print "\001\t"
f` sentinel and the `case "$bad12_raw" in` post-pass that rebuilds it, which exists for exactly this
reason — keeping a shell capability in the shell instead of reimplementing it inside awk. The recall
probe found the design prior art the map does not index:
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-9.md:205` already reasons
about an absent sha, a shallow clone and a blobless partial clone resolving to a named dead probe
rather than a green line, and `-7.md:106` carries the measurement that a `--depth 1` clone returns
its shallow root instead of failing. Both are cited in §4.

Recall terms used: `base sha status header check 12 hygiene resolve cat-file cutoff grandfather
shallow clone spec format`.
