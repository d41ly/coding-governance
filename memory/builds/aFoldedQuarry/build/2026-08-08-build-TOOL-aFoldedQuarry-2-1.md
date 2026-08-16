# Build journal — TOOL-aFoldedQuarry

**Serves:** journal TOOL-aFoldedQuarry-2

Node `a` · branch `branch/port-ledger-ttrove-governance-8b6ea4` · base `42c3f4dc`.
One section per unit, appended as it lands.

## Environment note found on arrival

`.claude/skills/memory-recall/SKILL.md` was CRLF in this worktree while `main`'s checkout of the same
commit is LF, so `adopt-memory-recall.sh --check` reported every line as drift before a single edit
was made. `.gitattributes` pins that path `eol=lf`, and the index normalises on commit, so
`git status` was clean and nothing pointed at the file. `rm` plus `git checkout --` restored LF.
Worth knowing because the symptom — a whole-file diff on a file the session never touched — reads
like a broken gate rather than a checkout artifact.

## U6 — index-keyed verdict join (spec `TOOL-aFoldedQuarry-2`, CLOSED)

### What landed

`tools/workflows/tier2-review.js` keeps its name, its four lenses, its cap-6 fan-out, its `args`
validation and all of its trust reporting. Only the join changed.

| Before | After |
|---|---|
| `verdictByRef[v.ref] = v` on a plain object | `verdictById` `Map` keyed on an integer |
| the skeptic re-typed `file:line` | the skeptic echoes `id=<n>` the orchestrator printed |
| two findings at one location shared one verdict | each finding carries its own id |
| a repeat verdict overwrote silently | agreeing repeat counted; disagreeing repeat demotes to UNVERIFIED |
| a verdict for an unknown key was stored | an unassigned id is counted `spurious` and discarded |
| nothing judged returned with NO report | the outstanding list is synthesized into the report |

Two gates ship with it. `tools/workflows/check-review-join.sh` bans three spellings of the retired
join across every tracked `tools/**/*.js`. `tools/workflows/check-workflow-syntax.js` parses each
workflow script as the async-function body its runtime evaluates.

### Three things measurement changed

**`node --check` is not a syntax gate.** It was in the acceptance criteria as AC7 until it was run:
on node v24 it exits 0 for `export const x=1` followed by `let y=(`. Module auto-detection retries
the parse and swallows the failure. The replacement constructs an `AsyncFunction` from the source
with the `export` keyword stripped, which is the only shape that accepts module export, top-level
`await` and top-level `return` at once — and it goes red on the same fixture with
`SyntaxError: Unexpected token '}'`.

**Comment stripping is load-bearing, not politeness.** The harness now carries a comment that spells
the retired join verbatim in order to explain why it is gone. A whole-file-text absence assertion
would red on the documentation of its own fix. The stripper is a character scan rather than a regex
on `//`, because a regex cannot tell the `//` that opens a comment from the one inside
`"https://…"`, and cutting on the wrong one turns a code line into prose and the ban into a no-op.
Both cases are armed in the self-test.

**A repeat verdict that AGREES is not a conflict.** The first draft demoted any id receiving a second
verdict to unverified. A chatty skeptic listing one finding twice with the same verdict would have
lost a real adjudication and inflated the unverified count, which then reads as harness degradation.
Only a DISAGREEING repeat is a conflict.

### The empty-population arm

Both gates fail rather than pass when they find nothing to look at. A discovery run over zero
workflow scripts, or an explicit run over files that do not exist, prints "which is not a pass" and
exits 1. A gate whose population evaporates otherwise prints a green line forever.

### Verification

`bash tools/workflows/check-review-join.test.sh` — 16 arms, every one asserting the SPECIFIC message
its branch emits, `PASS` printed after the last arm. Five red arms (three ban spellings, the
url-in-a-string case, the remedy text), three green arms (comment-only prose, the shipped tree, the
dialect fixture), one empty-population arm, three syntax-gate arms, and five positive assertions that
the shipped harness actually carries the indexed join — an absence ban alone proves only that the old
join is gone.

`bash tools/run-gates.sh` — 21/21 legs green, 1 skipped as unchanged. Three legs are new:
the ban, the syntax gate, and the self-test. `tools/run-gates.test.sh` needed `node` added to its
allowed launcher set, which is a deliberate widening recorded here rather than a quiet edit.

## U1 — the flatten (spec `TOOL-aFoldedQuarry-3`, CLOSED)

### What landed

The discipline directory axis is gone from the kit and from this repo's tree. `memory/` now holds one
append-only `DECISIONS.md`, per-family backlog shards under `backlog/`, and every build at
`builds/<slug>/` — no date prefix, no family prefix. Which discipline a spec served is a `streams`
value in its status header, validated against the closed `DISCIPLINES` enum whenever present and
required once the filename date reaches `STREAMS_CUTOFF`.

Tracked files under `memory/`: 86 before, 76 after. The delta is exactly the four discipline
`README.md`, the four discipline `TREE.md`, three of the four `DECISIONS.md` (merged into one), one
of the two `aPrunedCeremony` build READMEs (merged), and the two new records this unit wrote. No file
was dropped.

### One slug, two families

`playbook/builds/2026-07-19-PLAY-aPrunedCeremony` and `tooling/builds/2026-07-19-TOOL-aPrunedCeremony`
were ONE session under two disciplines. Flattening made that visible as a collision: two `README.md`
and two pairs of `spec-…-1.md` / `spec-…-2.md` wanting the same names. They merged into
`builds/aPrunedCeremony/`, which is the case the flatten exists for, and the recording grammar gained
an OPTIONAL FAMILY qualifier — `<date>-<kind>-<FAMILY>-<slug>-<seq>.md` — over the CLOSED alternation
from `FAMILIES`. A generic `[A-Z]+` there would have admitted a family that does not exist and made
the rejection arm vacuous.

### The finding that shaped the unit

Six path selectors changed segment count at once. A selector left at the old count matches nothing,
`grep … || true` yields empty, `[ -n "$bad" ]` is false, and the check prints nothing — which is
exactly what a passing check prints. The gate would have gone green over an unlinted tree with no
symptom at all.

So every retargeted selector now asserts a NON-EMPTY population. The first draft of that guard was
wrong in the opposite direction: it redded a freshly scaffolded tree, because a repo with no builds
yet legitimately has an empty build population. Measured by running `adopt-memory-tree.sh --scaffold`
into a scratch repo, not by reading the code. The guard therefore compares TWO granularities — a
PRECONDITION that asks whether a file of that KIND exists anywhere under the memory root, and the
POPULATION at the exact path the check expects. Equal-and-zero is a young tree. Precondition non-zero
with an empty population is a mis-segmented selector, and only that reds. Both states are armed in
the self-test, the half-migrated one built from the actual pre-flatten paths.

### The kit/dogfood divergence nobody was watching

`SPEC-TEMPLATE.template.md` — the file an adopter copies — still described a NINE-section canon and
carried no `SPEC10_CUTOFF` section, while this repo's installed `memory/TEMPLATE-SPEC.md` and the
gate had required TEN sections since 2026-08-04. An adopter would have installed a template the gate
rejects. Nothing connected the two files, so nothing caught it.

`tools/memory-tree/kit-dogfood-parity.test.sh` now does, as a gate leg: the shipped copies must equal
the installed ones modulo one declared substitution — the `tools/` install prefix, since the kit
ships tool-root-relative and an adopter chooses where the kits live. `--render` rewrites the shipped
copies from the live ones. Its first run reported the whole tree as drift because it derived the
prefix by string-stripping `git rev-parse --show-toplevel` (`C:/projects/…`) from `pwd`
(`/c/projects/…`) — the two-spellings trap already recorded in the kickoff manifest, arriving in new
code the same day it was read. Both sides now go through the same `cd … && pwd` chain.

### Verification

`bash tools/memory-tree/check-memory-hygiene.test.sh` — 64 assertions, up from 37. New arms: four
streams arms (post-cutoff with and without the field, an illegal value, and a TIER-1 post-cutoff
spec, which proves the check sits above the Tier-1 exit), the FAMILY-qualifier pair, the flat
folder-name rejection, the backlog shard-name rejection, and the two empty-population arms.

`bash tools/run-gates.sh` — 22/22 legs green, 1 skipped. The bar grew the kit/dogfood parity leg.

## U2 — the generated build index (spec `TOOL-aFoldedQuarry-4`, CLOSED)

### What landed

`gen-memory-tree.sh` and `memory/TREE.md` are gone. `tools/memory-tree/gen_build_index.py` replaces
them and carries something the listing could not: STATUS. It reads exactly two sources — each build's
README front matter and every `**Status:**` header under that build's `spec/` — and renders three
artifacts: the generated region inside each build README, `memory/LIVE.md`, and
`memory/ledger/<month>.md` shards. A build's status is a pure function of its units', so a build
leaves `LIVE.md` when its last unit goes terminal and nobody edits anything.

Fourteen build READMEs gained front matter; seven of them did not exist and were authored. Check 9
now delegates to this generator's `--check`, and a new leg runs its `--selftest`.

### One source of truth per build, and the four builds that forced the rule

The design said the status is derived from unit statuses. Counting the corpus rather than reading it
found four builds — `aDeployScout`, `aKitHardener`, `aLeanRework`, `aRatchetForge` — whose only specs
are grandfathered recordings with no status header at all. Every default was wrong: CLOSED contradicts
the memory index for one of them, live parks three finished builds in `LIVE.md` forever, and dropping
them is the silent-departure blind spot this unit exists to close, arriving through a different door.

So the rule is explicit in both directions. A build with any parseable header has its status DERIVED,
and an authored `status:` key there is an ERROR — two answers to one question is the drift being
removed. A build with none REQUIRES `status:`, and its absence is a named error. Four builds author
one line each, once. Both arms are armed in the selftest.

The review that produced this rule said "three builds" and listed three. The fourth was found by
counting. That is the second time in this build a claim about the corpus survived reading and died on
measurement; the review record carries the correction rather than hiding it.

### The three upstream blind spots, closed and armed

A README with an unpaired marker used to leave the index silently — it is now a named error quoting
the counts found. An absent README used to kill both modes with a traceback — it is now a named error
that says why an unindexed build is a problem. An orphaned generated file used to be permanent and
invisible — `--check` reports it and `--write` deletes it, BOUNDED to a `ledger/<YYYY-MM>.md` name;
anything else under `ledger/` is reported and left alone, because a generator that deletes inside the
memory tree on its own authority is a data-loss path.

### Two hazards the corpus surfaced

`---` opens front matter AND is a markdown horizontal rule, and one already separates the two merged
halves of `builds/aPrunedCeremony/README.md` from U1. A parser scanning for the first two `---`
anywhere would have swallowed that whole half. Front matter therefore opens at LINE 1 and nowhere
else.

The gate byte-compares, so the generated files are pinned `eol=lf` in `.gitattributes` AND the
comparison normalises CR. Either alone leaves the failure mode this repo has now hit twice: a
generated file that reds on every line on a Windows checkout, and passes only right after a render.

### Verification

`python tools/memory-tree/gen_build_index.py --selftest` — 15 arms including a write-then-check
fixed-point arm, without which a renderer that emits CRLF is green on the run that wrote it and red
forever after. `bash tools/run-gates.sh` — 23/23 green. A fresh `adopt-memory-tree.sh --scaffold`
into an empty repo produces a hygiene-clean tree, verified by running it.

## U3 — one id grammar, one walk, every consumer (spec `TOOL-aFoldedQuarry-5`, CLOSED)

### What landed

`tools/memory-tree/corpus_ids.py` classifies the corpus's ids and repo-path citations in one walk and
adds four checks to the hygiene gate.

| Check | What it catches |
|---|---|
| 13 | one id claimed by two different build folders |
| 14 | an id cited but never defined — waiver, shrink-only pin, stale-entry guard |
| 15 | a rooted repo-path citation that resolves to nothing — registry, four rules |
| 16 | the charter's read path: total under a ceiling, every member under a byte cap or waived |

It declares no grammar and no set it does not own. The id grammar comes from the memory-recall kit;
the append-only areas and the byte-capped index set are ASKED of `check-memory-hygiene.sh`, which
gained two print modes for the purpose. Upstream transcribed the index set into Python and had to
guard the transcription in both directions; asking removes the class instead of guarding it.

### The measurement, which is a deliverable and not a by-product

| Quantity | Measured |
|---|---|
| ids defined | 29 |
| ids cited | 33 |
| orphan ids | 4 |
| ids claimed by two build folders | 0 |
| dead repo-path citations | 0 |
| charter read path under `memory/` | 1 file, 3670 B |

Pins: `ORPHAN_ID_PIN=4`, `DEAD_PATH_PIN=0`, `READ_PATH_CEILING=24150` (3670 + 20480 headroom). The
four orphans are exactly the four grandfathered builds U2 also had to declare a status for, so the
waiver shrinks as those gain conforming specs rather than sitting as permanent debt. A zero pin on an
empty registry is not a vacuous check: the selector covers the whole present-tense corpus and finds
nothing, so the next unresolving citation reds until it is registered or repaired.

### Three findings that only measurement produced

**Check 13 is not "defined twice".** The first reading made any id with two defining anchors a
collision. Measured: ten ids in this corpus are anchored by a `DECISIONS.md` row AND by their spec's
H1, which is the index pointing at the record and entirely correct. The test is "claimed by two BUILD
FOLDERS", which is 0 here and fires the day two builds share an id.

**Check 16's read path is scoped to the memory root.** Deriving it from every path the charter names
produced 32 files and 308 KB — mostly gate scripts. Thirty of them would have needed waiving, and a
rule whose population is almost entirely waived has no signal. Scoped to `MEMORY_ROOT` it is one file
and 3670 B, and the byte caps it cross-references govern exactly that tree.

**The orphan fixture was passing by finding nothing.** Its first cut put the orphan id in a backlog
row — but `- <id> ·` IS an anchor, so the row DEFINED the id and the corpus had no orphan at all. The
arm asserted a message that never appeared for a reason that had nothing to do with the rule.

### Two environment traps paid for here

`subprocess.run(["bash", …])` on this node resolves the System32 WSL launcher, not git-bash. WSL sees
a different filesystem, so a path that plainly exists reports `No such file or directory` and a
relative path resolves under `/mnt/c/`. `resolve_bash()` names the executable and skips the two known
launchers by path; `GOV_BASH` overrides.

`extract.repo_root()` anchors on the KIT's own file, deliberately, so no `chdir` can point its
grammar at another tree. A caller classifying a different root got this repo's family alternation and
therefore matched NOTHING — and a grammar that recognises nothing yields an empty classification,
which is exactly what a clean corpus yields. The first selftest run reported a clean scratch corpus
while using the wrong grammar. `extract.grammar_for(root)` is the accessor added for this, so there
is still one grammar and it can now be bound to an explicit root.

### Verification

`python tools/memory-tree/corpus_ids.py --selftest` — 16 arms: every rule of checks 13-16 with a red
and a green side, both directions of rule 1, the shrink-only pins, the stale waiver row, the missing
charter, and the blank-pin off switch. `bash tools/run-gates.sh` — 24/24 green.

## U4 — the bug-class catalogue and its per-diff checklist (spec `TOOL-aFoldedQuarry-6`, CLOSED)

### What landed

`tools/memory-tree/gotchas.py` plus eight authored records under `memory/gotchas/`, a generated
`INDEX.md`, and three checks. `--for-diff <base>..<head>` prints the classes a diff can actually hit;
its stdout IS the checklist. Run against this build's own last commit it selected five anchored
classes plus the two universal ones out of eight — which is the shape the unit is for.

| Check | What it catches |
|---|---|
| 17 | a stale `gotchas/INDEX.md` |
| 18 | a class record that neither names a gate nor says it has none |
| 19 | a record that can never fire: no anchor and not universal, or anchors reaching only append-only paths |

### The corpus is this repo's failure history, not inCMS's

inCMS's 178 records are its own history; here they would be 178 anchors matching nothing. The eight
records are the classes THIS build paid for, each citing the measurement that produced it: the
vacuous selector, the absence assertion that reds on its own documentation, the byte-compare gate
that needs both an eol pin and a normalising comparison, the subprocess that resolves a different
shell, the grammar bound to the wrong root, the fixture that passes by finding nothing, the pin
copied from another corpus, and two answers to one question.

Two are `universal: true` against a budget of 3. Upstream designed for 10 and measured 40, and 40 of
a 68-entry checklist are the always-emitted core — so the budget is a conf value with a measurement
behind it rather than a number that drifts.

### One carried defect turned out not to apply

The handoff listed three upstream harvest defects to carry. Two hold here: a token containing `::`
inside backticks harvests to nothing, and an anchor's basename matches tree-wide however much path
precedes it (kept — it is what makes short-form anchors usable). The third does not: upstream's token
pattern required a non-empty tail after the slash, so a directory anchor written with a trailing
slash harvested to nothing and its record was silently unanchored. This pattern allows an empty tail,
so the directory token IS harvested and selects everything beneath it.

The arm asserts the DIFFERENCE rather than upstream's behaviour, with the reason written next to it.
Carrying a defect that is not present would have been deference to a document over a measurement, and
pinning the actual behaviour means a future tightening of the pattern reintroduces the upstream
defect loudly instead of quietly.

### The catalogue does not select itself

Every record cites paths under `gotchas/` while describing its own class, and selection matches on
basename — so without an exclusion a diff touching the catalogue would emit most of the catalogue.
Noise on a checklist is how reviewers learn to skip it, so `selectable()` never returns a path inside
the catalogue.

### Verification

`python tools/memory-tree/gotchas.py --selftest` — 19 arms: every check with a red and a green side,
both `--declares` directions (a body that says it has no gate declares; a `description` carrying the
word "gated" does not), the indented-front-matter error, all three harvest behaviours, the
self-exclusion, the universal budget, and four `--for-diff` arms proving it emits anchored hits and
universals and omits misses and non-class records. Check 19's fixture carries a POPULATED append-only
area, without which the inert arm can never fire and the rule ships green forever.

`bash tools/run-gates.sh` — 25/25 green.

## U5 — the harness disciplines, made mechanical (spec `TOOL-aFoldedQuarry-7`, CLOSED)

### What landed

`tools/memory-tree/check-arms.py` turns the transferable harness disciplines into a gate. Every
`fail` branch in the hygiene gate is either ARMED — a POSITIVE assertion in the test file naming a
literal slice of that branch's own failure text — or listed in
`memory/project/unarmed-branches.txt`, shrink-only.

| Discipline | How it is mechanical here |
|---|---|
| key on the CALL SITE | `(check number, ordinal)`; this gate has 14 branches behind 12 numbers |
| pin BOTH directions | `ARMS_BRANCH_FLOOR=14` and `ARMS_ARMED_FLOOR=5` |
| an arm is POSITIVE | a bare `check N`, an absence assertion and a comment all fail to arm |
| exclude the pin from its own scan | the scan reads the test file and nothing else |
| batch the fixtures | the existing self-tests keep their one-scratch-repo shape |
| PASS after the LAST arm | every self-test in this build prints its verdict last |

Measured: 14 branches, 0 armed. Five gained real arms in this unit and nine are pinned, so the gap is
visible and shrinks instead of being assumed away.

### Why the key is the call site

Checks 5 and 6 each fail for two different reasons. A pin keyed on the NUMBER would let the cheapest
arm empty a number while its sibling branch stayed unwritten AND invisible — which is what upstream
hit at 41 branches behind 25 numbers.

### Why both floors

A branch count catches a DELETED guard. It does not catch an assertion dropped by WIDENING the pin:
the branch count falls, the pin still holds, and the gate is quieter than it was with nothing to say
so. The armed floor is the second direction.

### Three findings from the closing pass

The first `fail` pattern was start-anchored and missed check 9 entirely, whose call sits inside an
`if ! drift=$(…); then`. Thirteen of fourteen, silently — the exact failure this meta-check exists to
prevent, inside the meta-check. Finding it also surfaced a message (`build index:`) too short to
assert on, so check 9's message was reworded.

A COMMENT naming a branch's message armed it. The test file's own prose quotes the messages it
covers, so a comment-blind scan let a sentence describing an arm count as the arm — the same shape as
the two cases the function already refused.

And the same environment defect landed THREE times in one session: source written through a shell
heredoc into a non-raw Python string turned `\b` into a literal backspace byte, which reached the
compiled regex. The symptoms were all silent and all different — a citation scan returning zero ids
while anchors kept working, anchors matching without boundaries, and a branch parser finding zero
branches in a file with fourteen. Each looked like a logic bug. A sweep repaired the last one, and
the first sweep found nothing because it scanned TRACKED files only while the offending module was
still unstaged — the population-selected-too-narrowly class this build already catalogued. It is now
`memory/gotchas/heredoc-escape-reaches-the-regex.md` and a kickoff-manifest trap.

### Order note

This unit was built before its spec was written, because the design is a function of a measurement
and the measurement needed the parser that became the module. The adversarial pass therefore ran
against the IMPLEMENTATION rather than a draft, which is stronger evidence. The deviation is recorded
in the sub-spec's §8 Fork B rather than tidied away.

### Verification

`python tools/memory-tree/check-arms.py --selftest` — 12 arms covering every red and green path,
including a signature present only in the PIN arming nothing. `bash tools/run-gates.sh` — 27/27
green.
