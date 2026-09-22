**Serves:** diff-review TOOL-aWeldedTribunal-1 TOOL-aWeldedTribunal-2 TOOL-aWeldedTribunal-3 TOOL-aWeldedTribunal-4 TOOL-aWeldedTribunal-5 TOOL-aWeldedTribunal-6 TOOL-aWeldedTribunal-7 TOOL-aWeldedTribunal-8

# Closing diff review — aWeldedTribunal, all eight units

Tier-2 adversarial review of the landed code for the eight-unit set: a fan of primed finder lenses
over the diff, a skeptic pass prompted to REFUTE each finding, then this synthesis. Every finding
below was re-checked against the worktree while writing this report, and every agent-cap and
parse_conf finding was REPRODUCED by running the shipped file — the transcripts of those runs are
quoted inline.

**Range — ROUND 1:** `9b5ae68820500aafb32d0edde32936991472980c...HEAD`
(eight product commits, `cc8776b8` through `cd51decd`, plus their records.)

## Verdict: BLOCKED

Two blockers. One refuses `govkit update --write` for a defect that has nothing to do with the
update, after the bytes have already landed; the other denies a legal, correctly-marked fan-out
harness because a *comment* names the mutation it forbids. Both were the brief's named hunting
class — a verb that previously succeeded now refusing, and a legal script now denied — and both were
introduced by this diff. Three highs and one medium follow, then two lows. Nothing in units 1, 4 or
8 produced a confirmed finding.

## Review shape

- raw 18 · confirmed 14 · refuted 4 · unverified 0 · precision 0.78
- The 14 confirmed reports resolve to **8 distinct defects**: the govkit one was found independently
  four times, the `parse_conf_line` one three times, the agent-cap member-chain one twice. Merged
  here at synthesis; the harness discarded no duplicates of its own (see RUN INTEGRITY).

## RUN INTEGRITY

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdict(s) demoted to unverified · 0 spurious verdict(s) discarded · 0 duplicate(s)

Every counter is zero, so this run is complete: no lens died, and the finding set is not truncated
by a missing arm. Where this report reports an absence — no confirmed finding in units 1, 4 or 8 —
that absence rests on four lenses that all returned, not on a silent gap.

## Findings

| # | Sev | Site | Defect |
|---|-----|------|--------|
| F1 | BLOCKER | `tools/govkit/govkit.py:7507` | The coverage probe fails the write verb it was promised not to touch |
| F2 | BLOCKER | `tools/hooks/agent-cap.js:924` | A block comment naming `NAME.push(` revokes `NAME`'s bound |
| F3 | HIGH | `tools/hooks/agent-cap.js:924` | `obj.NAME.push(` withdraws the bound from an unrelated top-level `NAME` |
| F4 | HIGH | `tools/hooks/agent-cap.js:933` | The take-back does not propagate, so a derived name keeps a withdrawn bound |
| F5 | HIGH | `tools/memory-tree/corpus_ids.py:143` | `KEY="v"  # note` keeps the comment and a stray quote |
| F6 | MEDIUM | `tools/hooks/agent-cap.js:924` | A removal-only `splice` revokes a bound for "growth" that shrank the array |
| F7 | LOW | `tools/check-wiring.sh:202` | A line-number citation the same commit made stale |
| F8 | LOW | `tools/memory-tree/gen_build_index.py:284` +3 | Four readers import `parse_conf_line` and none call it |

---

### F1 — BLOCKER · `tools/govkit/govkit.py:7507` · the coverage probe can fail `update --write`

The new gap block hands `coverage_rows` the RUN's own `Report`:

```python
_gaps = coverage_rows(root, target, deploy, descs, _gap_selection, r)
```

`coverage_rows` (`:2263`) is called with no precomputed `rows`, so it runs
`planned_writes(root, target, deploy, descs, selection, r)` at `:2300` with that same report.
`planned_writes` calls `r.fail(...)` at `:2188` for every destination token the target's
`deploy.toml` does not answer, and `derive_rule_kind` calls `r.fail` at `:2083` for a role absent
from `ROLE_KINDS`. `Report.fail` (`:958`) appends and never raises, so the `except Exception`
wrapper around the block cannot intercept it — the wrapper catches the raise the author measured on
the `-11` escape fixture and nothing else.

Fifteen lines below, `decline_findings` is deliberately given a throwaway `_gr = Report()`, and the
comment above it states the rule: passing the run's own Report "would make a malformed or stale
`[[decline]]` row FAIL a write verb operators run constantly, for a defect that has nothing to do
with the update," and concludes "this verb's refusal surface is unchanged." The `coverage_rows` call
two lines earlier makes that sentence false.

The consequence is not a noisy line. `_cmd_update` reaches `if r.problems:` at `:7569` **after**
every byte-level write and the whole verify pass have completed, takes the not-re-stamped branch —
`receipt["schema"]` and `receipt["gov_commit"] = to_commit` are both skipped — and returns
`r.emit()` = 1. The target is left with post-update bytes on disk and a pre-update vintage in the
receipt, and the next `update` re-derives from that stale base. Before this diff `_cmd_update` never
called `planned_writes` at all (its only other call sites are `cmd_plan` at `:2623` and `:2869`,
each with its own Report), so this is a brand-new refusal surface on gov's main write verb.

Reachability is the update path itself: gov shipping a rule whose destination token an adopter's
descriptor has no answer for is precisely the case this coverage report was added to detect.
`selftest.py:327` already asserts the `"needs answer 'playbook_path'"` string out of this exact code
path for `plan`, so the arm is live, not theoretical.

**Fix.** Hoist the throwaway report above the coverage call and give it to both consumers:

```python
_gr = Report()
_gaps = coverage_rows(root, target, deploy, descs, _gap_selection, _gr)
...
for _p in _gr.problems:
    print(f"govkit update --   coverage: {_p}")
```

Nothing is hidden — the problems print — and the verb's exit code and stamping decision return to
what the comment claims they are.

**Left-shift gate.** A `selftest.py` arm over a fixture target whose descriptor leaves one
destination token unanswered in a *claimed* kit: `update --write` must exit 0 and the receipt's
`gov_commit` must have advanced. That arm fails today and is the class, not the instance — it pins
"a report may not change a write verb's verdict" rather than pinning this one call site.

---

### F2 — BLOCKER · `tools/hooks/agent-cap.js:924` · a block comment revokes the bound

Reproduced end to end, BASE rc=0 → HEAD rc=2:

```
const LENSES = [1,2,3]
/* never do LENSES.push(x) here */
await boundedParallel(LENSES.map((L)=>()=>agent(L)), 5)
```
```
rc=2  BLOCKED by agent-cap: a verify/fan-out stage spawns one agent per item.
  L3: await boundedParallel(LENSES.map((L)=>()=>agent(L)), 5)
        `LENSES` was GROWN by a mutation after its bounded assignment, which takes the bound back
```

The same script with the comment written as `//` exits 0, and `git show 5120332e^` exits 0 on the
block-comment form, so this is a measured regression rather than pre-existing behaviour.

`fanoutFindings` runs `GROWS_RECEIVER` over `code`, which is `renderLexedView`'s output, and that
view deliberately does not blank block comments. Its own header justifies the choice: un-blanked
comment text "can only ADD apparent code, never hide it." That argument is sound for the DETECTION
rules the view was built for and false for a REVOCATION sweep, where added apparent code *withdraws*
a bound and denies a legal script. `runBothViews` unions the two views, so a false positive under
the lexed view denies outright — the union closes the usual escape, and the sweep has no marker
escape of its own.

This is the project's `absence-assertion-over-whole-file-text` class in its purest form: the comment
documenting the rule reds the file. The operator's only route to green is deleting the sentence that
explains why the rule exists.

**Fix.** Run this one sweep over a block-comment-free rendering — `renderBlankedView` already blanks
`/*…*/` — and revoke only when the match survives there. A `/\*[\s\S]*?\*/` strip over the joined
text, local to the sweep, is the two-line version.

**Left-shift gate.** `check "a block comment naming <name>.push( does not take the bound back →
allow" 0`, with both the single-line and multi-line comment forms, beside the three positive growth
arms in `tools/hooks/agent-cap.test.sh`.

---

### F3 — HIGH · `tools/hooks/agent-cap.js:924` · the sweep captures the LAST name of a member chain

```js
const GROWS_RECEIVER = /\b([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g
```

`\b` matches after the dot, so on `state.lenses.push(x)` the capture is `lenses`, not `state`. There
is no left-boundary guard, unlike the sibling call-site walk ~30 lines below, which already spells
one: `/(^|[^.\w$)\]])[A-Za-z_$][\w$]*\s*\.\s*[A-Za-z_$][\w$]*\s*$/`. The asymmetry is an oversight,
not a choice.

Reproduced (rc=2 at HEAD, rc=0 with the bookkeeping line deleted):

```
const lenses = [1,2,3,4,5]
state.lenses.push("audit")
await boundedParallel(lenses.map((L)=>()=>agent(L)), 5)
```

The refusal names a variable nothing touched — "`lenses` was GROWN by a mutation after its bounded
assignment" — and the suggested remedy does not apply, so the operator's only route to green is
renaming an innocent property. The trigger needs the property name to equal the bounded array's
name; `journal.batches.push(n)` beside `const batches = chunk(...)` is exactly that collision, and
`batches` is the name this repo's own canonical harness shape uses. No tracked `.js` carries the
shape today, which is why the six new negative arms are green over it — but the hook's population is
scripts operators write in a Workflow call, not tracked files, so a clean tree is weak evidence here.

Note that the unit's own RESIDUALS paragraph enumerates only cases that UNDER-report (alias
mutation, `a[i] = x`, `.length = n`). Every one of F2, F3 and F6 is the OVER-reporting direction,
and the comment names none of them.

**Fix.** `const GROWS_RECEIVER = /(?:^|[^.\w$)\]])([A-Za-z_$][\w$]*)\s*\.\s*(?:push|unshift|splice)\s*\(/g`
— reusing the boundary the call-site walk already spells. `batches.push(` still matches;
`journal.batches.push(` no longer does.

**Left-shift gate.** `check "a member-chain push does not take a top-level bound back → allow" 0`
with `state.lenses.push(...)` above a bounded fan over `lenses`.

---

### F4 — HIGH · `tools/hooks/agent-cap.js:933` · the take-back does not propagate to derived names

The sweep deletes only the mutated name. It does not re-run the derivation blessing, and both scan
passes have already finished by the time it runs — so a name derived from the withdrawn one keeps a
bound the source no longer has. Reproduced at rc=0:

```
const batches = []
for (const f of allFindings) batches.push(f)
const groups = batches.filter(Boolean) // gov:fixed-verifiers
await boundedParallel(groups.map((g) => () => agent(g)), 5)
```

The direct spelling — fanning over `batches` itself — is correctly denied at rc=2. So the unit
closes TOOL-aCandidStub-1 for one statement and leaves an unbounded agent-per-finding fan admitted
one `.filter(Boolean)` away. This is the fail-OPEN direction, and it is the one that costs a
rate-limited phase.

`boundedBranch` blesses `groups` during `lines.forEach(scan)` on the strength of `ok.has('batches')`.
Verified that the pre-existing reassignment sweep has the identical hole (`let batches = [1,2]` /
`batches = allFindings` / same derivation → rc=0), so this is not purely new — but the new sweep
inherits it, and the fix belongs in one place for both.

**Fix.** Record `derivedFrom.set(name, source)` in the `FIXED_MARK` accept branch, then after both
sweeps drop transitively any name whose source is no longer in `ok` (one pass with the map, or
iterate to a fixed point).

**Left-shift gate.** Two arms, one per sweep: push-then-derive and reassign-then-derive, both
expecting deny. They fail today, which is the point — a gate whose failing case has never been
observed is an assertion about nothing.

---

### F5 — HIGH · `tools/memory-tree/corpus_ids.py:143` · a quoted value keeps its trailing comment

The inline-comment strip is gated on `if v[:1] not in ("'", '"')`, so it is skipped entirely for any
quoted value, and the closing `.strip('"')` then cannot peel a quote that is no longer terminal.
Measured against the shipped function:

```
'INDEX_CAP_BYTES="20480"         # a row document' -> ('INDEX_CAP_BYTES', '20480"         # a row document')
'DISCIPLINES="a b" # x'                           -> ('DISCIPLINES', 'a b" # x')
'MEMORY_ROOT="memory"  # note'                    -> ('MEMORY_ROOT', 'memory"  # note')
```

`set -a; . conf` gives `20480`, `a b` and `memory`. This is precisely the shell/python divergence
the docstring says the unit closes — "any spelling bash accepts and the python half mis-reads
REMOVES coverage while the gate stays green" — left half-closed. The guard was written for a `#`
INSIDE the quotes (`QUOTED="a # b"`, which still works); it does not cover a `#` AFTER the closing
quote, and the docstring's out-of-scope list names command substitution, parameter expansion, line
continuations and quoted whitespace but not this one.

Reachable today, in shipped adopter-facing code: `tools/memory-tree/.memory-tree.conf.example` uses
exactly that spelling on five lines (93, 95, 97, 108, 109), and an adopter copies that file
verbatim. The failure is the silent kind — a bogus `DISCIPLINES` member, a date cutoff that never
compares equal, a `MEMORY_ROOT` pointing at a directory that does not exist — while the shell gate
sourcing the same file reads it correctly. This repo's own `.memory-tree.conf` keeps its comments on
their own lines, so there is no live instance here; every one of the six readers routed through the
shared parser by unit 5 inherits it.

**Fix.** When the value opens with a quote, find the matching closing quote first, take the text
between them, and run the word-initial `#` scan over the remainder only. That handles both
directions with one branch.

**Left-shift gate.** Extend the arm that already pins `parse_conf_line` against `set -a; . conf` to
cover `Q="a # b"` → `a # b` and `Q="a" # b` → `a`, measured against bash rather than asserted.

---

### F6 — MEDIUM · `tools/hooks/agent-cap.js:924` · a removal-only `splice` revokes a bound

`splice` is in the growth vocabulary unconditionally, but `splice(start, n)` strictly SHRINKS the
array. Reproduced, BASE rc=0 → HEAD rc=2:

```
const LENSES = [1,2,3,4,5]
LENSES.splice(0, 2)
await boundedParallel(LENSES.map((L)=>()=>agent(L)), 5)
```

The denial asserts the array "was GROWN by a mutation" about an array that went 5 → 3, and the fan
it blocks is *smaller* than the 5-element literal the same hook blesses unmarked. The sweep's own
comment defines its question as "whether a statement GROWS the array named," and its neighbouring
paragraph records the mirror-image over-denial (`concat`/`flat`/`flatMap` withdrawing a bound on a
call that changes nothing) as a MEASURED defect — so the file's own standard classifies this the
same way. `push` and `unshift` always grow; only `splice` is wrong here. The existing fixture at
`agent-cap.test.sh:80` pins the 3-argument inserting form, which genuinely grows, so the
removal-only arm is untested.

**Fix.** Match `splice` only with three or more top-level arguments — `joinCall`/`topLevelArgs` are
already in this file — or drop `splice` from the vocabulary and name it in the residuals paragraph
beside the alias and `length =` cases.

**Left-shift gate.** `check "removal-only splice does not take the bound back → allow" 0` with
`LENSES.splice(0, 2)`, beside the existing 3-arg deny arm.

---

### F7 — LOW · `tools/check-wiring.sh:202` · a citation the same commit made stale

The new comment block cites `line 809` as the script's exit-code line. That was true at
`dc097122^`; the same commit inserted 51 lines at 185, so the exit line
(`[ "$unwired" = 0 ] && exit 0 || exit 1`) is now 860 and line 809 is blank. The whole argument for
`note` over `UNWIRED` — the fork resolution — is anchored on a pointer that now resolves to nothing.
`memory/gotchas/hookspath-resolves-into-another-checkout.md:65` repeats `check-wiring.sh:809`
verbatim, and unlike the ratified spec that is a live record.

This is AGENTS.md §6's own rule — "a value stated in prose beside the source that OWNS it rots
between changes" — broken inside the diff that restates it.

**Fix.** Drop the number from both live sites and name the thing: "`unwired` is what this script's
final `exit` reads." Leave the three `:809` citations in
`spec/2026-09-04-spec-TOOL-aWeldedTribunal-7.md` alone — a ratified record is cited verbatim, never
renumbered.

**Left-shift gate.** A hygiene check refusing a `<tracked-file>:<digits>` citation in a tracked
comment or `memory/gotchas/*.md` where the cited line is blank or does not contain the quoted
symbol. Cheap, and it fails on both live instances today.

---

### F8 — LOW · four readers import `parse_conf_line` and never call it

`tools/memory-tree/gen_build_index.py:284`, `gotchas.py:89`, `check-arms.py:79` and
`row_grammar.py:39` all import `parse_conf_line` alongside `parse_conf`; none of the four references
it again. Its only callers outside its own module are nobody — `read_declared_keys` and `parse_conf`
inside `corpus_ids.py` are the real consumers. No lint leg exists on the bar (`tools/gate-legs.json`
has no ruff/flake8/pyflakes entry), so nothing reds. The cost is a two-function shared contract
advertised where the shared surface is one function.

**Fix.** Import only `parse_conf` in the four readers. Keep `parse_conf_line` public in
`corpus_ids.py` — it is the tested unit and `read_declared_keys` needs it.

**Left-shift gate.** This is the one finding whose gate is worth more than the fix: a `pyflakes`
(or `ruff F401`) leg over `tools/**/*.py`, guarded on the python subject, catches this class
permanently instead of this instance. If that is judged too heavy, the fix stands alone and the
class stays ungated — say so rather than calling the import removal coverage.

---

## What this pass did not cover

- Unit 4 (`tier2-review.js` RUN INTEGRITY block) and unit 8 (the four backlog closures) produced no
  confirmed finding. Four lenses returned and none died, so that is a real absence rather than a
  gap — but unit 8 is a records-only change whose evidence is citations, and citation *accuracy* was
  spot-checked, not exhaustively re-derived.
- `check-wiring.sh`'s new hook-blob comparison (unit 7) was reviewed for the false-refusal class and
  produced only the stale-citation finding above; its behaviour against a genuinely divergent
  out-of-tree `core.hooksPath` was not exercised on a second checkout.
- No gate run was performed as part of this review. F1's fix, F2's fix and F4's fix each need their
  own arm before landing, and none of those arms exists yet.
