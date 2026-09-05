# TOOL-aJoinedCanon-11 — the base sha resolves to a real object

**Status:** SPECCED · rev-5 · 2026-09-05 · node a · Tier-1 · base 750ca0ca · streams tooling · order 11 · ratified 2026-09-05

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round1.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round2.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 |
| [2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md](../reviews/2026-09-05-review-TOOL-aJoinedCanon-1-spec-audit-round3.md) | spec-audit | TOOL-aJoinedCanon-1 TOOL-aJoinedCanon-2 TOOL-aJoinedCanon-3 TOOL-aJoinedCanon-4 TOOL-aJoinedCanon-5 TOOL-aJoinedCanon-6 TOOL-aJoinedCanon-7 TOOL-aJoinedCanon-8 TOOL-aJoinedCanon-9 TOOL-aJoinedCanon-10 |

<!-- /gen:spec-records -->

## 1. Goal

Check 12 asserts a spec's `base` field is eight hex characters and never asks git whether those
characters name anything. Resolve it, on live specs written from a dated cutoff onward, so the next
transposed digit is caught by the bar instead of by a reviewer.

## 2. Scope (IN)

Every item below names the criterion that observes it. Round 3's H4 found S1 through S5 and S7
untagged after a fold that tagged S6 alone — the address-not-class close this build's README bans —
so the tags are here as a set, not one at a time.

- **S1** *(Observed by AC9 and AC6)* — a new cutoff key `BASE_RESOLVE_CUTOFF` in `.memory-tree.conf`, preset blank in
  `tools/memory-tree/check-memory-hygiene.sh` above the conf source, and shipped blank in
  `tools/memory-tree/.memory-tree.conf.example`. It takes the three rule cutoffs' semantics: blank
  means off. All three carriers move in one commit: the self-test's engine-preset parity arm derives
  its key set from the engine, so an undeclared key reds this unit's own landing commit on the
  `memory-hygiene self-test` leg S2 already owes — and, unfixed, leaves an adopter a dead arm
  reading as armed.
- **S2** *(Observed by AC1, AC2 and AC3)* — a check-12 arm that resolves the `base` sha of every
  selected spec whose filename date is on or after that cutoff and whose status is not `CLOSED` or
  `WONTDO`, failing when the sha names no commit in this object database. **BOTH TIERS.** The
  emission sits ABOVE the `if (hdr ~ /Tier-1/) next` line in that awk, not below it, because `base`
  is a status-header field a Tier-1 spec carries exactly as a Tier-2 one does; §4 states the
  placement and AC1 observes it on a Tier-1 fixture.
- **S3** *(Observed by AC12)* — the resolution runs as ONE `git cat-file --batch-check` for the whole
  population, driven by a sentinel record the existing awk emits, not by a fork per spec.
- **S4** *(Observed by AC5 and AC11)* — a shallow repository is detected once and the arm announces
  its own skip on stderr rather than passing silently or redding every spec, and
  `tools/memory-tree/check-memory-hygiene.sh`'s header states what each stream now carries: stdout
  for findings, stderr for announced skips AND for `resolve_python`'s refusal under a set-but-unusable
  `GOV_PYTHON`. The header half is here because AC11 graded it while no scope item built it — the
  same missing-owner shape as M4's dossier row, found by running that predicate over this section
  instead of over the table.
- **S5** *(Observed by AC1, AC2, AC3 and AC12)* — the fixtures and scratch trees every criterion
  needs, all of them, in `tools/memory-tree/check-memory-hygiene.test.sh`. Round 3's H5 found this
  item building two while three criteria needed artefacts nothing constructed, so it now enumerates
  the set against the criteria that read it. Fixture names come from this unit's `tFixture-190`
  block upward per the build's `order`-allocated number space:
  - `tFixture-190` — post-cutoff, LIVE, **Tier-1**, base `0123abcd`, which resolves to nothing. Red,
    observed before landing. Tier-1 by construction, so a branch placed below the Tier-1 cut goes
    silent on it; that is AC1's stated break, and `tFixture-54` and `tFixture-84` are the two
    existing fixtures built for the same purpose against other arms.
  - `tFixture-191` — post-cutoff, LIVE, base = the scratch repo's own `git rev-parse --short=8 HEAD`.
    Silent. Written after the fixtures commit, per "The green fixture's base" in §4.
  - `tFixture-192` — post-cutoff, **CLOSED**, base `0123abcd`. Silent, which is the terminal-status
    exemption AC3 grades and the only observation of grandfathering this unit makes.
  - The `BASE_RESOLVE_CUTOFF` declaration in the scratch conf that
    `check-memory-hygiene.test.sh` writes, dated one day ahead of the newest fixture filename date in
    that file — derived at build time, not pinned here, because six lower-`order` units add fixtures
    to the same file. Every pre-existing fixture is therefore grandfathered and 190 to 192 are dated
    after it.
  - A SECOND scratch tree for AC5, built by `git clone --depth 1 "file://$PWD"` from a scratch repo,
    because a `--depth 1` clone from a plain local path is not shallow at all. §4's "The probe that
    cannot move" carries the measurement.
  - A blank-key run for AC6, riding the existing blank-cutoff section of that self-test — the one
    that already rewrites the scratch `.memory-tree.conf` with a subset of keys and asserts the
    matching arms stay dark.
- **S6** *(Observed by AC10)* — the `base` bullet in `memory/TEMPLATE-SPEC.md` and its byte-compared twin
  `tools/memory-tree/SPEC-TEMPLATE.template.md` gains the resolution rule and names the cutoff, in
  one commit, with the kit version marker moved in every carrier that holds it.
- **S7** *(Observed by AC8)* — check 12's catalog entry in `memory/HYGIENE.md` and its byte-compared twin
  `tools/memory-tree/HYGIENE.template.md` state the live-only population AND the gap it accepts:
  a spec whose base does not resolve can be silenced by closing it, and a unit that goes `SPECCED`
  to `CLOSED` in one commit is never graded at all. It sits beside that entry's existing
  `SHAPE only` caveat, in the same commit as S2, because a check whose own description omits what
  it does not check is the shape charter §7 refuses.
- **S8** *(Observed by AC13)* — `memory/guides/SESSION-KICKOFF.md` is re-stamped: `last-audit` moves
  to a fresh `<ISO datetime> @ <sha>` per that manifest's own stamping rule, which this spec does not
  restate. Three of this unit's write-set paths — `tools/memory-tree/check-memory-hygiene.sh`,
  `.memory-tree.conf` and `memory/guides/BUILD-METHOD.md` — are `watch:` pathspecs of that manifest,
  and check C5 of `skills/session-kickoff/manifest-check.sh` is topological: it reds when the newest
  watch-touching commit is not an ancestor of the re-stamp, whatever the body says. So this landing
  reds an unguarded every-bar leg without S8. `last-body-change` does NOT move and §B gains no delta
  line: this unit changes no gate command, entrypoint, layout convention or front-loaded claim, and
  the charter's rule is "no delta → no touch". Round 3's H2: eight of the eleven units in this build
  edit a watched path and none carried this.
- **S9** *(Observed by AC14)* — `memory/map/features/memory-tree-hygiene.md` states the new arm: its
  conf key, the live-only population, and the accepted never-graded bypass S7 names. Charter §5 makes
  refreshing a touched dossier a Definition-of-Done item, and nothing on the bar notices dossier
  prose going stale — `codebase-map coverage + freshness` grades key claims, pinned headings and
  artifact freshness, not whether the prose still describes the engine. Round 3's M4: this was a
  Files-touched row with no scope item, no criterion and no leg, which is the same shape the round-2
  fold closed elsewhere in this spec.

**What this arm buys, stated plainly because the honest answer is small.** All 22 spec files carrying
an unresolvable base are CLOSED, so this catches nothing that exists. The arm is purely
forward-looking and its whole value is that it stops the next one.

Figures re-derived at `750ca0ca` for this revision, after round 3 found the rev-4 block reproducing
at neither that sha nor HEAD. The population selector is **S2's own**, not `check-spec-tokens`'
four-status LIVE set: a spec file's first `**Status:**` line, live iff its status word is neither
`CLOSED` nor `WONTDO`. At `750ca0ca`, 474 spec files carry a status header, all 474 carry a base,
over 86 distinct values; 40 of the 474 are live, all 40 carry a base, and **every one of those 40
resolves**. 9 distinct base values resolve to nothing, held by 22 files, every one of them `CLOSED`,
across `aBatchedTribunal`, `aDrainedSluice`, `aRelaxedShard`, `aUnmannedHelm` and `cSettledDocket`.
At HEAD the same derivation gives 485 files, 87 distinct values, 51 live — the corpus moves, the
9-over-22-all-CLOSED shape does not. The deriving command is beside the figures so the next fold
re-runs it rather than trusting the label:

```sh
git grep -n -E '^\*\*Status:\*\*' <rev> -- 'memory/builds/*/spec/*.md' \
  | sed -E "s#^<rev>:##" | sed -E 's#^([^:]+):[0-9]+:#\1\t#' | awk -F'\t' '!seen[$1]++'
```

then one record per file, status word from the header and `base [0-9a-f]{8}` from the same line, with
the distinct base values piped through `git cat-file --batch-check` suffixed `^{commit}`.

The class is not hypothetical, and it has a measured price in review time rather than in gate time.
In `memory/builds/aRelaxedShard/reviews/2026-08-18-review-TOOL-aRelaxedShard-4.md`, finding M3 opens
`git rev-parse 86eefd8f` → "fatal: ambiguous argument" and records a declared base of `86eefd8f`
against a real commit `86eefd8e` — a transposed eighth character, found by a human lens and
explicitly noting that check 12's grammar validates shape alone. In
`memory/builds/dCarriedReceipt/reviews/2026-08-26-review-DEPL-dCarriedReceipt-5-diff-review-round2.md`
the same defect lands on a review's own range, in the paragraph opening `The base sha as handed to
this reviewer does not resolve in this repo`, again caught by a person. Both are anchored by text
rather than by line: round 3's M5 found this spec's two `path:line` pins landing on headings, four
and twenty-three lines short of the sentences they were cited for.

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
after it and this build's own specs are grandfathered.

The self-test's scratch conf is a SEPARATE declaration with its own value, and the same property is
what grandfathers the fixtures already in that file: every existing `base` fixture there is dated on
or before the newest fixture filename date, and S5 sets the scratch `BASE_RESOLVE_CUTOFF` one day
ahead of that date, derived at build time. So none of them changes and S5's three fixtures are dated
after it. No count of those fixtures appears here: rev-4 claimed 26 and the literal `base 0123abcd`
reproduces on 23 lines and 33 times at this base, and six lower-`order` units add fixtures to that
same file before this one builds, so the number would be stale either way. The PROPERTY is what the
argument needs — that the existing fixtures fall on the grandfathered side — and it survives every
fixture those six units add.

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

**Where the branch sits, and the one thing it must NOT copy from that prior art.** The `\001`
sentinel lives BELOW the `if (hdr ~ /Tier-1/) next` line, inside the Tier-2-only band, because the
section canon is a Tier-2 rule. `base` is not: it is a status-header field both tiers carry, and S2
says both tiers. So the `\002` emission goes ABOVE that `next`, in the every-tier band the file's own
comment marks — the one reading "these two run for EVERY TIER, so they sit ABOVE the Tier-1 cut",
where the streams, witness and §9-rev assertions already live. The idiom is copied; the placement is
not. This matters because `next` is a PREFIX cut, so the failure is silent and asymmetric: below the
cut, every Tier-1 spec's base goes unresolved while `BASE_RESOLVE_CUTOFF` reads as armed — four of
this build's own eleven units are Tier-1. `tFixture-190` is Tier-1 for exactly this reason and AC1
names the misplacement as its break, which is the standard `tFixture-54` and `tFixture-84` already
set for two other arms in this file.

**The binding is named `bcut`, and that name is claimed.** `canon`, `canon10`, `cut10`, `mroot`,
`discalt`, `scut`, `wcut`, `fcut` and `ecut` are the nine `-v` bindings this awk invocation carries
today, and the siblings in this build have claimed `jcut` (unit 3), `mcut` (unit 4) and `rcut`
(unit 9), with unit 1 taking a fourth after round 3 found it colliding with unit 4 on `mcut`. `bcut`
is free of all of them, verified by grepping every spec in this build's own `spec/` folder as well as
the engine — which is the check round 3's blocker proved nobody was running, since a second `-v` of
the same name is last-wins for the whole program and silently regrades one arm by the other's key.
The name is registered in `TOOL-aJoinedCanon-3`'s namespace survey.

The post-pass splits `bad12_raw` on the `\002` tag, feeds the distinct shas to ONE
`git cat-file --batch-check='%(objectname) %(objecttype)'` with each line suffixed `^{commit}`, and
turns every `missing` or `ambiguous` answer back into a finding line addressed to the existing
`[ -n "$bad12" ] && fail 12` site. Verified at `750ca0ca`: `1da67d9c^{commit}` answers `missing` and
`750ca0ca^{commit}` answers a full objectname plus `commit`, and an ambiguous abbreviation answers
on its own line rather than on stderr. The `^{commit}` peel is what stops an eight-hex prefix that
happens to name a tree or a blob from passing.

**Cost.** One process for the whole run, whatever the population. A `git cat-file -e` per spec would
be one fork per live spec forever — 40 at `750ca0ca` and 51 at HEAD under S2's own selector, by the
derivation in §2 — which is the shape the batched awk was built to delete; its own header records
replacing roughly 13 forks per spec and 42.88s of an 81.77s run. This is the unit's central
implementation decision and AC12 is what observes it: round 3's H4 found every one of the eleven
criteria satisfied by a fork-per-spec build, which left this paragraph and §5's perf row resting on
an unobserved property.

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
regression. `run-gates.sh` merges both streams into the per-leg log — its leg dispatch redirects
with `>"$WORK/$i.raw" 2>&1` on both the bounded and unbounded branches — so the skip is durable and
readable where the leg's output is read.

**What the header amendment may and may not say.** The checker's stderr is NOT empty today: its one
`>&2` block is `resolve_python`'s refusal of a set-but-unusable `GOV_PYTHON`, which returns 1. So a
header claiming "stdout carries findings, stderr carries announced skips" would be FALSE of the file
before this unit writes a line — the could-not-fail shape pointed at prose instead of at an arm. The
amendment this unit makes is the true one: stdout carries findings, and stderr carries announced
skips AND the resolver's refusal to run under a broken override. Observed by AC11.

**Constructing a shallow repository is not what it looks like, and rev-4 got this wrong.**
`git clone --depth 1 <local path>` produces a repository that is NOT shallow: git prints
`warning: --depth is ignored in local clones; use file:// instead` and `--is-shallow-repository` then
answers `false`. Measured here on 2026-09-05, and every scratch tree in
`tools/memory-tree/check-memory-hygiene.test.sh` is a local `git init`, so this is the only form an
AC5 fixture can take. The form that works is `git clone --depth 1 "file://$PWD"`, measured the same
day against a one-commit scratch repo: `--is-shallow-repository` answers `true` and
`git rev-list --count HEAD` answers 1. Round 3's H6 is the finding — AC5 as rev-4 wrote it asserted a
`true` in a tree its own command could not build, so the only conjunct a builder could satisfy was
"exits 0", which every non-shallow run satisfies too. AC5 now asserts the probe as a PRECONDITION.

Prior art worth reading before touching this: `TOOL-dScaffoldedMirror-7`'s spec, in the section
headed `The base, and the failing case that replaces the research's`, measured that in a `--depth 1`
clone a derived-commit probe does not fail and does not return nothing — it returns the shallow root,
which resolves perfectly, observed as a derived base of `37bfdd19` against a true adoption commit of
`b0626152`. The lesson carried here is that the shallow case must be DETECTED rather than inferred
from what git answers.

A blobless partial clone (`--filter=blob:none`) still holds every commit, so commit resolution is
unaffected and no separate branch is needed for it.

### Files touched (estimate)

| File | What moves |
|---|---|
| `.memory-tree.conf` | S1, the declaration and its reasoning comment |
| `tools/memory-tree/.memory-tree.conf.example` | S1, the same key, shipped blank |
| `tools/memory-tree/check-memory-hygiene.sh` | S1 preset, S2/S3 arm and post-pass, S4 probe, the header contract comment |
| `tools/memory-tree/check-memory-hygiene.test.sh` | S5's whole set: the scratch-conf key, `tFixture-190` to `-192`, the shallow scratch tree, the blank-key arm, and AC12's `git` shim |
| `memory/TEMPLATE-SPEC.md` | S6, the `base` bullet |
| `tools/memory-tree/SPEC-TEMPLATE.template.md` | S6, the same bytes |
| `memory/HYGIENE.md` | check 12's catalog entry gains the clause and S7's accepted-gap sentence |
| `tools/memory-tree/HYGIENE.template.md` | the same bytes |
| `tools/memory-tree/BUILD-METHOD.template.md`, `memory/guides/BUILD-METHOD.md` | kit version marker only |
| `memory/map/features/memory-tree-hygiene.md` | S9, the dossier prose |
| `memory/guides/SESSION-KICKOFF.md` | S8, the `last-audit` re-stamp only; no body delta |

Every row above is named by a scope item or by a criterion. That is round 3's M4 closed over its
class rather than at its address: the dossier row was the one with no owner, and the same predicate
run over the whole table is what put S8's row here.

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
- **perf / scale** — one added process per run, independent of population size, which AC12 observes
  rather than asserts after round 3 found this row resting on nothing. The `memory hygiene`
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
- **testing + left-shift gates** — S5's set: three fixtures, a shallow scratch tree, a blank-key run
  and AC12's process count. `tFixture-190` is staged, confirmed red, and kept as a fixture rather
  than unstaged, which is what the self-test is for.
- **migration / rollback** — blanking `BASE_RESOLVE_CUTOFF` turns the arm off completely, and the
  rest of check 12 is untouched.
- **user docs** — `memory/TEMPLATE-SPEC.md` and `memory/HYGIENE.md`, with both twins, plus the
  dossier `memory/map/features/memory-tree-hygiene.md` under S9.

## 6. Acceptance criteria

- **AC1** — When `tFixture-190` carries a **Tier-1** live status, a post-cutoff filename date and a
  base of `0123abcd`, `bash tools/memory-tree/check-memory-hygiene.test.sh` observes check 12
  reporting that file and that sha; the red is observed before the arm lands, per the build's own
  rule. **The break that turns this red:** placing the `\002` emission below
  `if (hdr ~ /Tier-1/) next` in `tools/memory-tree/check-memory-hygiene.sh`. A Tier-1 fixture is the
  only thing that can tell the two placements apart, and the arm stays silently dark on every Tier-1
  spec if it is wrong.
- **AC2** — When `tFixture-191` carries the scratch repo's own `git rev-parse --short=8 HEAD`,
  the same run reports nothing for it.
- **AC3** — When `tFixture-192` carries an unresolvable base on a `CLOSED` status with a post-cutoff
  filename date, check 12 is silent on it, so the terminal-status exemption in
  `tools/memory-tree/check-memory-hygiene.sh` is exercised rather than assumed. This is the unit's
  only observation of grandfathering, per AC4.
- **AC4** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs over this tracked tree, it
  stays green. **What this can and cannot prove, stated because the earlier wording claimed more
  than it observes:** every spec carrying an unresolvable base is CLOSED, so S2's terminal-status
  conjunct excludes all of them before the cutoff is ever consulted — the green is therefore
  guaranteed by that conjunct and is NOT evidence that grandfathering works. It observes only that
  the arm adds no regression. The grandfathering itself is observed by AC3, on a fixture built for
  it.
- **AC5** — When the scratch tree is built with `git clone --depth 1 "file://$PWD"`, the criterion
  first asserts its own PRECONDITION — `git rev-parse --is-shallow-repository` prints `true` — and
  only then that the skip line appears on stderr and the process exits 0. A precondition, not a
  setup step: rev-4 built the tree with a plain local `git clone --depth 1`, which git ignores with a
  warning, so the tree was never shallow and the criterion could not go green. Asserting the state
  before grading it is what turns a silently non-shallow clone into an AC5 failure instead of an AC5
  pass. Measured 2026-09-05: the `file://` form answers `true` even on a one-commit source repo.
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

- **AC10** — When the `base` bullet is read in `memory/TEMPLATE-SPEC.md` after the change, it states
  that the sha is RESOLVED on a live spec rather than only shape-checked, and
  `bash tools/memory-tree/kit-dogfood-parity.test.sh` exits 0, proving
  `tools/memory-tree/SPEC-TEMPLATE.template.md` carries the same bytes. The phrase is absent from
  both files today — `grep -cF 'resolved on a live spec' memory/TEMPLATE-SPEC.md` returns 0 at this
  base — so the criterion is red before the edit and green after. figure: DERIVED, re-measured at
  build time. This is S6's observer; before rev-4 S6 had none.
- **AC11** — When the amended header of `tools/memory-tree/check-memory-hygiene.sh` is read, it names
  BOTH streams truthfully: stdout for findings, stderr for announced skips and for
  `resolve_python`'s refusal under a set-but-unusable `GOV_PYTHON`. Observed by reading the file, and
  falsified by the header as this unit finds it, which mentions neither stream. The refusal block is
  the file's only `>&2` today.
- **AC12** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs in the self-test's scratch
  tree with a shim named `git` first on `PATH` — one that appends its own argv to a log and then
  execs the real git — the log carries EXACTLY ONE `cat-file` invocation, over a population of at
  least two post-cutoff live specs carrying two DISTINCT base shas, which `tFixture-190` and
  `tFixture-191` already are. This is S3's observer and nothing else in §6 is. **The break that turns
  it red:** implementing the resolution as `git cat-file -e` per spec, or as one batch per distinct
  sha — both give two, and both satisfy every other criterion in this section. The shim is why the
  count is observed rather than asserted: `tools/memory-tree/check-memory-hygiene.sh` invokes `git`
  unqualified throughout, so `PATH` reaches every call site.
- **AC13** — When `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit it
  exits 0, and `memory/guides/SESSION-KICKOFF.md`'s `last-audit` names a sha at or after the commit
  that edits `tools/memory-tree/check-memory-hygiene.sh`. **The break:** revert S8 alone — keep the
  engine and conf edits, restore the old stamp — and check C5, `no unaudited watch drift`, reds
  naming the watched file changed with no re-stamp. `last-body-change` holds the SAME sha before and
  after, which is the half of this criterion that observes the "no delta → no touch" side of the
  rule rather than the re-stamp side.
- **AC14** — When `grep -c BASE_RESOLVE_CUTOFF memory/map/features/memory-tree-hygiene.md` is run
  after the change it returns a non-zero count, and the dossier prose names the live-only population
  and the accepted never-graded bypass. It returns 0 at this base, so the criterion is red before the
  edit and green after. **The break:** landing the arm with the dossier untouched, which no gate leg
  catches — `codebase-map coverage + freshness` grades key claims and artifact freshness, not prose,
  so this criterion IS the coverage and §7 says so.

## 7. Gates

Leg names are read from `tools/gate-legs.json`, never from a list typed here.

- `memory hygiene` — `tools/memory-tree/check-memory-hygiene.sh`, the changed gate itself.
- `memory-hygiene self-test` — `tools/memory-tree/check-memory-hygiene.test.sh`, which carries all of
  S5 — the three fixtures, the shallow scratch tree, the blank-key run and AC12's process count — and,
  through its engine-preset parity arm, S1's third carrier as AC9 observes it.
- `harness arms (fail branches armed or pinned)` — the leg that grades this file's arm pin, which
  AC7 asserts this unit leaves where it found it.
- `kit/dogfood doc parity` — `tools/memory-tree/kit-dogfood-parity.test.sh`, which byte-compares
  `memory/TEMPLATE-SPEC.md` against `tools/memory-tree/SPEC-TEMPLATE.template.md` and both the
  `HYGIENE` and `BUILD-METHOD` pairs, all three named on the `PAIRS` assignment in that file. Cited
  by that name and not by line: rev-4 pinned `:53`, and `TOOL-aJoinedCanon-9` edits that same file at
  `order` 9, two steps before this unit builds. A bare `:<n>` also escapes the citation sweep the
  siblings ran, which needs a filename before the colon.
- `kit version markers` — the leg `tools/check-kit-versions.sh` runs, named because the two backlog
  rows above record the carrier set being missed twice. The count of carriers is not written here;
  that script is the authority on it.
- `verdict epoch (kit version dates the engine)` — this unit changes the engine, so the epoch leg
  binds it. Round 2 found this leg missing from the §7 of every unit that touches the engine.
- `kickoff-manifest ratchet` — `subject = repo`, no guard, so it runs on every bar. It is here
  because three of this unit's write-set paths are `watch:` pathspecs of
  `memory/guides/SESSION-KICKOFF.md`; S8 carries the re-stamp and AC13 names the observed red.
- `codebase-map coverage + freshness` — named for what it does NOT cover. It grades key claims,
  pinned headings and artifact freshness, so S9's dossier prose is invisible to it. AC14 is the
  compensating check, and it is a documented manual one, not a leg.
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
- rev-4 · 2026-09-05 · §2 · §4 · §6 · §7 · folded spec-audit round 2: H4 (S6 had no
  observer — added AC10), M4 (§7 carried a script path where a leg name belongs, and omitted
  `verdict epoch`), M7 (AC4's green was guaranteed by S2's terminal-status conjunct and proved
  nothing about grandfathering — now says what it can and cannot show, with AC3 carrying the real
  observation), M8 (the prescribed header amendment was false of the file before writing, because
  stderr already carries `resolve_python`'s refusal — added AC11). Class sweep over all 23: also
  converted the `run-gates.sh:1110-1111` pin to a text anchor per the build's citation rule.
  THIS ENTRY WAS SPLICED INTO THE MIDDLE OF rev-2's by a hand-fold and rev-5 rejoined it; the two
  halves under rev-2 above are rev-2's own work, not this revision's.
- rev-5 · 2026-09-05 · §2 · §4 · §5 · §6 · §7 · §9 · §10 · folded spec-audit round 3, the TERMINATING
  fold: ten findings, all ten disposed here. H1 rebuilt this log — rev-4's entry had been spliced
  into the middle of rev-2's and logged before rev-3, so rev-2's two halves are rejoined and the
  order is now 1, 2, 3, 4, 5. H7: S2 and §4 now state that the sentinel emission sits ABOVE
  `if (hdr ~ /Tier-1/) next`, `tFixture-190` is Tier-1, and AC1 names the misplacement as its break.
  H6: AC5 builds its shallow tree with `git clone --depth 1 "file://$PWD"` and asserts
  `--is-shallow-repository` as a PRECONDITION; §4 carries the measurement that the local form is
  ignored with a warning. H4: AC12 added — a `git` shim counting exactly one `cat-file` invocation
  over two distinct shas, which is S3's only observer — and `Observed by` tags now sit on S1 to S9.
  H5: S5 enumerates its whole artefact set, three fixtures plus the shallow tree plus the blank-key
  run, and running H5's reverse join over §6 found AC11 grading a header amendment no scope item
  built — folded into S4. M1: the figures block is re-derived at `750ca0ca` under S2's own selector, with the deriving
  command beside it — 474 files, 86 distinct values, 40 live and all resolving, 9 unresolvable values
  over 22 CLOSED files. M2: the fixture count is replaced by the property that grandfathers them.
  M3: §7 cites the `PAIRS` assignment by name instead of `:53`. M4: the dossier is S9 with AC14,
  and every Files-touched row is now named by a scope item. M5: the four `path:line` citations in
  §2, §4 and §10 became text anchors. Cross-unit: H2's `last-audit` re-stamp is S8 with AC13 and
  the `kickoff-manifest ratchet` leg, and B1's namespace rule is answered in §4 — `bcut` checked
  against the engine's nine bindings and every sibling's claim.
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
`memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-9.md` already reasons
about an absent sha, a shallow clone and a blobless partial clone resolving to a named dead probe
rather than a green line — in the `error / empty / loading states` row of its §5, not at the section
heading rev-4 pinned — and `TOOL-dScaffoldedMirror-7`'s spec, in the section headed `The base, and
the failing case that replaces the research's`, carries the measurement that a `--depth 1` clone
returns its shallow root instead of failing. Both are cited in §4, both by text: round 3's M5 found
both pins landing on headings rather than on the sentences cited.

Recall terms used: `base sha status header check 12 hygiene resolve cat-file cutoff grandfather
shallow clone spec format`.
