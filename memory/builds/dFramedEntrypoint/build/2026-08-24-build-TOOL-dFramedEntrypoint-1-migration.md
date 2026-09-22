**Serves:** research TOOL-dFramedEntrypoint-1

*Research lens for the `dFramedEntrypoint` design pass — the cutoff patterns, the waiver registries, and who owns the repair. Produced 2026-08-24, node d, against base 9ddcc5c9. Findings in this record were subsequently adversarially verified; where the verification corrected a claim, the verification record wins.*

# Migration & ratchet lens — the closed build-README slot set

Worktree `C:/projects/coding-governance/.claude/worktrees/build-readme-governance-18d6ea`, HEAD `9ddcc5c9`,
identical to `origin/main` for `memory/builds/*/README.md`. Every count below carries the command that
derived it.

---

## 0. Two corrections to the brief, before anything else

### 0.1 The population is 61, not 19

```
git ls-tree -r --name-only HEAD -- memory/builds | grep -c 'README.md$'   # 61
git ls-tree -r --name-only origin/main -- memory/builds | grep -c 'README.md$'  # 61
ls memory/builds | wc -l                                                  # 61
```

**The "19" in the brief is a live signal's VALUE being read as its POPULATION.** `drift_report.py`
prints, on this tree today:

```
readme_mechanism_drift                                19     61  ok
```

That is 19 drift ROWS over 7 of 61 build READMEs, pinned in
`tools/drift-audit/drift_signals.py:187`, whose own comment says so verbatim: *"19 rows over 7 of 61
build READMEs. Report-only."* The corpus is 61 files, and every cost estimate in this design pass has
to be re-priced by 3.2x.

### 0.2 The authored half is 63% of the corpus by bytes, not a header

```
# authored half = every line before the first `<!-- gen:` or `<!-- roster:` marker
n=61  sum=352,889 B  min=359  median=4,185  max=33,798
# whole files
n=61  sum=563,963 B  mean=9,245  max=44,872
```

352,889 B of authored prose, 4,338 non-blank authored lines. If the closed slot set lands at a
plausible ~1,300 B per README (description + two short lists + optional rules paragraph), the contract
implies **deleting or relocating roughly 274 KB of authored prose across 61 files**, 45 of which
(`node:` front matter, `sort | uniq -c`) belong to node `a`, 7 to `c`, 6 to `d`, 3 to `b`.

That number is the whole migration question. Everything below is about who pays it and whether they
should.

---

## 1. The cutoff pattern — what the repeated discipline actually is

Sources: `.memory-tree.conf` lines 20–81 and 341–371, `.unattended.conf:93–105`,
`tools/memory-tree/check-memory-hygiene.sh:24–56`.

The live cutoffs are `SPEC_FORMAT_CUTOFF` (`:21`), `STREAMS_CUTOFF` (`:27`), `SPEC_WITNESS_CUTOFF`
(`:81`), `FORK_MARK_CUTOFF` (`:80`), `REVIEW_VERDICT_CUTOFF` (`:79`), `ACCEPTANCE_LEDGER_CUTOFF`
(`:353`), plus `SPEC10_CUTOFF` (declared in the engine at `check-memory-hygiene.sh:35`, not in this
repo's conf) and `UNITS_REGION_CUTOFF` (`.unattended.conf:105`).

### The checklist a new cutoff must satisfy

**C1 — Measure the corpus BEFORE choosing the predicate, and record the measurement in the conf.**
Not the repair list — the evidence. `SPEC_WITNESS_CUTOFF`'s block (`:36–41`) measured 774 acceptance
bullets, 181 naming nothing, and reports that three rival predicates flagged 218 and 247 *with false
positives* before the bare-backtick rule won. `REVIEW_VERDICT_CUTOFF`'s block (`:62–67`) measured 111
review records, 66 with a verdict line, 17 distinct values, and `CLEAN` — the token the method names
as the loop's only exit — occurring **zero** times.

**C2 — Observe the retroactive red count rather than assuming it.** Both blocks do this literally:
*"with this key set retroactively to 2026-01-01, check 12 reds 33 TERMINAL specs"* (`:57–58`); *"with
this key set retroactively to 2026-01-01, check 22 flags 60 records"* (`:69–70`). The number is
produced by running the check, not by reasoning about it.

**C3 — Set it strictly AHEAD of the newest member of the corpus it governs, and say against what.**
`STREAMS_CUTOFF`'s comment (`:24–26`): *"Set strictly ahead of every committed spec's filename date at
the flatten, so no landed spec is retroactively red."* `REVIEW_VERDICT_CUTOFF` (`:70`): *"set strictly
ahead of the newest tracked review filename date, which is 2026-08-20."*

**C4 — Because C3 means the corpus does not exercise the required arm, the self-test must carry
explicit red/green fixtures for it.** Stated twice: `:26` and `:34`. A cutoff that grandfathers
everything ships a check nobody has seen fire, which is §7's "a gate you have only ever seen pass is an
assertion about nothing".

**C5 — Name the repair that is deliberately NOT performed, and why.** `REVIEW_VERDICT_CUTOFF`
(`:74–78`) is the clearest: *"The repair is deliberately NOT to fill their verdict lines. A halt code
CLASSIFIES a reason its author already wrote, so deriving one is reading; a verdict ASSERTS a
conclusion nobody wrote, so deriving one would put this session words into another node record."* Then
the phrase the brief asked about: **"Forward-only in truth rather than in intent"** (`:79`). It means
the cutoff is not a scheduling convenience that someone will backfill later — the pre-cutoff corpus
can *never* conform, because conforming would require inventing content its authors did not write.
Contrast `SPEC10_CUTOFF`, where the pre-cutoff corpus *could* conform in principle and is forbidden to
(below).

**C6 — Decide whether the cutoff is a SWITCH or a SELECTOR, and know that a selector forbids voluntary
drain.** `STREAMS_CUTOFF`, `SPEC_WITNESS_CUTOFF`, `FORK_MARK_CUTOFF`, `REVIEW_VERDICT_CUTOFF` and
`ACCEPTANCE_LEDGER_CUTOFF` are SWITCHES: validated-when-present, required-after. `SPEC10_CUTOFF` is a
SELECTOR: it picks between a nine-section canon and a ten-section one
(`check-memory-hygiene.sh:1031`), and the canon is EXACT EQUALITY. The census measured the
consequence — *"a grandfathered file is FORBIDDEN to conform early. Adding `## 10. Reuse audit` to a
pre-`SPEC10_CUTOFF` spec reds the gate. That is why 0 of 11 grandfathered specs carry §10: voluntary
drain is mechanically impossible"* (`aMouldedFolio` census `:187–189`).

`SPEC10_CUTOFF` also carries the blank-resolves-FORWARD rule (`check-memory-hygiene.sh:36, 56`): the
shipped value is captured before the conf is sourced, so a blank resolves to the shipped default, never
to "off". That is because a selector with no value has no canon to select — the key cannot be a
switch even by accident.

**C7 — Prove the boundary direction with an arm.** `check_authorization`'s cutoff comment
(`unattended.sh:1276–1279`) records that the first implementation NEGATED the `sort -C` test and
therefore *"refused every BASE before the cutoff while admitting every one after: the precise inversion
the cutoff exists to prevent, and it would have refused the run that built this unit."*

**C8 — Prefer a NAMED grandfather list to moving the date, once the date is set.**
`ACCEPTANCE_LEDGER_GRANDFATHER` (`.memory-tree.conf:371`) holds nine unit ids. Its comment: *"Named
INDIVIDUALLY rather than by moving the cutoff, because moving it forward would re-open the gap for
every spec in between AND drop this build's own units out of the population, leaving a check whose
first run measures nothing. A dated exemption that cannot be audited is not an exemption."*

**C9 — A cutoff whose first run measures an empty set is an assertion about nothing, and the check
must SAY SO.** `ACCEPTANCE_LEDGER_CUTOFF` was set to its own build's date rather than the day after
precisely to avoid this (`:347–350`), and `check-memory-hygiene.sh:1168` prints *"check 23 measured NO
unit — every closed Tier-2 spec predates ACCEPTANCE_LEDGER_CUTOFF, so a green verdict here is coverage
of nothing"*. The census names the underlying trap: **`pop_guard` is blind to date vacuity** — it
measures the population *before* the date filter, so a cutoff governing zero files reports nothing
(census `:194–196`).

---

## 2. Does a build README even take a cutoff? — the recorded answer is NO, and it is still true

**This repo has already asked this exact question, measured it, and ruled.** `TOOL-aMouldedFolio-1`,
the doc-template census, §5, at
`memory/builds/aMouldedFolio/build/2026-08-11-build-TOOL-aMouldedFolio-1-doc-template-census.md:213`:

> **Why grandfathering build READMEs is not on the table.** A cutoff would key on `opened:` — an
> authored field, shape-checked, never cross-checked against git. The newest build opened 2026-08-10,
> so a cutoff set today exempts **25 of 25** … And any author extends the exemption by typing an older
> date.

That ruling is recorded in `memory/DECISIONS.md:45` as `TOOL-aMouldedFolio-1`. **Every clause of it is
still literally true, and two are worse.**

### Candidate keys, priced

| Key | Forgeable? | Coverage if set today (2026-08-25) | Verdict |
|---|---|---|---|
| front-matter `opened:` | **YES** | exempts **61 of 61** | REFUSED, on record |
| README's first-commit date (git) | no | exempts 61 of 61 | mechanically sound, cost/portability problems |
| derived live/terminal status | no (gated) | governs **12 of 61** | the only key that governs a non-empty set today |
| named grandfather list (C8 idiom) | no | governs 0, drains by hand | the exemption *mechanism*, not the key |

**`opened:` is validated for SHAPE ONLY, and nothing else has changed.** `gen_build_index.py:247`:

```python
if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", fm["opened"]):
    raise Problem(f"{path}: opened '{fm['opened']}' is not a YYYY-MM-DD date")
```

Measured now, against the git add-date of each README (`git log --diff-filter=A --format=%cs --follow -1`):

```
n=61  disagree=16  no-resolvable-add-commit=1   # 26% disagree
```

Sixteen of sixty-one already disagree with git, including `aWireWarden` (`opened: 2026-07-15`, added
`2026-08-08`) and `bThriftyBellows` (`2026-07-16` vs `2026-08-09`). So the field is not merely
forgeable in theory — a quarter of the corpus already carries a date git does not corroborate, for
entirely innocent reasons (the flatten re-filed old builds). A cutoff on this key would be a ratchet
whose teeth are made of a field that is wrong 26% of the time and that any author can set freely.

**Newest `opened:` is 2026-08-23** (`sort | tail -1`). Today is 2026-08-24. A C3-compliant cutoff of
2026-08-25 governs zero of the 61 — the census's "25 of 25" is now "61 of 61".

### The one thing that HAS changed, and it cuts the other way

The census measured 25 builds. There are now 61, and:

```
# builds whose `opened:` is 2026-08-10 or later
40
```

**40 new builds in 14 days — about 2.9 per day.** At that rate a forward-only cutoff reaches 61 new
governed builds in roughly three weeks. The census's implicit objection ("a forward cutoff buys
nothing for a long time") was priced against a corpus growing far more slowly. Today, forward-only
coverage is genuinely fast. That is the single strongest *new* argument for a cutoff, and it does not
rescue `opened:` as the key — it argues that the cutoff mechanism is worth having on a key that works.

### Git-date key: sound but expensive and not fully resolvable

`git log --diff-filter=A --follow` returned nothing for `cSightedPlumb` (1 of 61) — the rename history
does not resolve. It also costs 61 `git log` invocations per run, on a bar where node `d`'s AV taxes
every exec ~0.022 s (user memory: *process creation is the suite cost*). And it cuts against the
repo's stated preference for `git ls-files` membership over history reads: `.memory-tree.conf`'s
`DEAD_PATH_EXCLUDE` comment says *"Resolution never touches the filesystem — it is `git ls-files`
membership plus a prefix scan — so a checkout LOCATION classifies as dead identically on every node."*
A history-derived key is the same class of node-dependent input.

### Is a build README a ratified record? — NO, and this is settled

The append-only rule's scope is explicitly the DECISION LOG and nothing else:

- `AGENTS.md:219` / `coding-governance-agents.template.md:149` — *"the decision log is append-only
  (never rewrite a ratified record — supersede with a new id + note); the backlog is mutable"*.
- `memory/HYGIENE.md:50` — the no-broken-links exemption names *"the append-only log (`DECISIONS.md`,
  `decisions/`)"*.
- `memory/HYGIENE.md:81` — *"Rotation moves whole files — it never rewrites or renumbers a ratified
  record."*

Build READMEs are in none of those. Positively, the build method **mandates** editing them after the
fact:

- `memory/guides/BUILD-METHOD.md:237` — *"**Re-read the build README against the code before
  closing** — every owner ruling and every sentence naming a shipped mechanism."*
- `:38` — *"**Classify, first match wins.** Write it into the build README before acting on it."*
- `:133` — a runaway review loop *"promotes and lands anyway and says so in its output AND the build
  README."*

**So immutability is not the obstacle. Ownership is** (§4).

Note also what IS treated as ratified: `.memory-tree.conf:54` — *"rewriting a ratified record is
against this tree's own rule, so the cutoff carries the landed corpus instead"* — is said about
SPECS, and `:70` about REVIEW records. Both are the "forward-only in truth" class: nobody can write
another author's conclusion. **The new slot set is in exactly that class for the two judgment slots.**
An EXPECTED-IMPROVEMENTS list and a DETRIMENTS list are assertions about intent and cost that only the
build's own author can make. Deriving them for a closed build would put this session's words into
another node's record — the precise thing `REVIEW_VERDICT_CUTOFF` refused to do.

---

## 3. The waiver-registry pattern — shared conventions, and why one is the WRONG vehicle here

`memory/project/` holds eight files. Shared conventions, read off their headers and their consumers:

1. **Every one declares its empty state in line 1.** *"Empty = fully strict"* (`curation-debt.txt:1`),
   *"Empty = strict"* (`legacy-files.txt:1`), *"Measured 0 at DEAD_PATH_PIN=0, so this file is empty
   and the pin is a ratchet"* (`corpus-path-unresolved.txt:4`).
2. **Comments are `#`-prefixed and carry the reasoning, at length.** `curation-debt.txt` is 33 lines of
   which 26 are comment.
3. **SHRINK-ONLY is stated explicitly, and a stale row REDS.**
   `testsuite-count-waivers.txt:2–3` — *"a row leaves when its suite complies, and a row naming a
   compliant suite REDS as stale."* `trace-waiver.txt:14–17` — *"SELF-POLICING: a row is consumed only
   by a spec that is present, terminal and still untraceable. A waiver cannot outlive the thing it
   waives."*
4. **A row states its own DRAIN CONDITION.** *"each row drains when that build's owner curates it"*
   (`curation-debt.txt:5`); *"Drains when the row shape is revisited"* (`:23`, `:33`).
5. **BLAST RADIUS is stated and MEASURED before the row is added.** This is the discipline the brief
   asked for, and `curation-debt.txt` spells it twice:
   - `:26–30` — *"BLAST RADIUS, stated because a debt row is wider than the failure that earned it:
     this silences checks 6, 7 AND 8 on TOOL.md, not just the byte cap. MEASURED before listing it —
     the hygiene run that caught check 6 reported neither 7 nor 8, and the longest row is exactly 300
     chars against a 300 budget. So nothing is hidden today, but that row is AT the limit and the
     check that would catch it going over is now off."*
   - `:38–41` — the `dUnstalledConvoy` row does the same: *"BLAST RADIUS, measured before listing:
     this silences checks 6 and 7 on this file. Check 8's population is the backlog shards alone, so it
     never reached this path."*
6. **A registry silences a whole FILE for a set of RULES, never one rule.** `curation-debt.txt` exempts
   checks 6/7/8 together. `trace-waiver.txt` is per-(spec, signal). `unarmed-branches.txt` is the
   narrowest — keyed `gate<TAB>check<TAB>ordinal<TAB>signature`, and its header records that keying on
   path alone is what unpinned an earlier registry (`method-carriers.txt:4`: *"Keyed on PATH alone,
   never `<path>:<line>` — that keying is what unpinned `install-prefix-waivers.txt`"*).
7. **A row that cannot be armed says WHY.** `unarmed-branches.txt:7–10` — *"'not yet written' and
   'cannot be written from here' are indistinguishable in a bare pin, and only one of them is
   acceptable."*
8. **The header must not carry a count.** Same file, `:10–11`: *"`check-arms.py --report` prints the
   live count; this comment does not, because a number written here rots silently, and this header
   claimed EMPTY while carrying a row until `TOOL-aTetheredRecord-4`."*

### The verdict: a registry is the wrong vehicle, and the repo's own audit proves it

`drift_report.py --json`, `shrink_only_lists_not_shrinking`, on this tree today — **3 of 5, out of
tolerance**:

| Registry | seed | entries now | shrunk_by |
|---|---:|---:|---:|
| `id-orphan-waiver.txt` | 4 | 0 | **+4** |
| `unarmed-branches.txt` | 9 | 3 | **+6** |
| `corpus-path-unresolved.txt` | 0 | 0 | 0 |
| `trace-waiver.txt` | 5 | 7 | **−2** |
| `curation-debt.txt` | **0** | **7** | **−7** |

**`curation-debt.txt` — the closest possible analogue, "index files pending slimming" — has never
drained a single row and has grown from 0 to 7.** Two of its rows are build READMEs whose stated drain
condition is *"drains when that build's owner curates it"*, written 2026-08-16; nine days later none
has. Two more are marked "renderer-shaped, not curation-shaped" and drain only when a *different*
unit reshapes a row.

The two registries that DID drain (`id-orphan-waiver`, `unarmed-branches`) drained because a single
unit could mechanically satisfy every row: `TOOL-aTetheredRecord-1` added a family-qualified H1 to five
specs; arms were written for branches. **Both drains were within one session's own reach.** The two
that grew are exactly the ones whose rows name work belonging to somebody else.

A 61-row build-README registry is `curation-debt.txt` at nine times the size, with the same
"somebody else's prose" drain condition. It would seed at 61, never drain, and register as a permanent
`shrink_only_lists_not_shrinking` finding. **Do not build it.**

If a registry is nonetheless wanted, its rows should be the C8 shape — build SLUG, not path, one line,
with a stated drain condition — and it should be seeded **empty**, with the cutoff (not the registry)
carrying the corpus. That is `ACCEPTANCE_LEDGER_GRANDFATHER`'s design and it is the only registry idiom
here that was born small on purpose.

---

## 4. Who owns the repair — and the miscitation at the centre of the question

### The aMouldedFolio generated-prose record does not say what the registry says it says

`memory/project/curation-debt.txt:4`:

> `TOOL-aMouldedFolio-3` is the precedent that a build's own folder owns its own prose.

The phrase appears in exactly two places in the tree
(`grep -rn "owns its own prose"`): that line and `check-memory-hygiene.sh:1141`. **It appears nowhere
in `TOOL-aMouldedFolio-3` itself.** What that spec actually says, at
`memory/builds/aMouldedFolio/spec/2026-08-11-spec-TOOL-aMouldedFolio-3-generated-prose.md:14`:

> **S2** — the authored sentence is removed from every README carrying one, **BY THE GENERATOR**, in
> the same pass. **No file is hand-edited.**

and at `:128`:

> **AC8** — the generator performs the removal: with the remover disabled, the run REDS. This is S2's
> acceptance, which rev-1 had none for — **its criteria were all satisfiable by 17 hand-edits.**

and in Alternatives rejected, `:95`:

> **Validate the sentence instead of deriving it.** A validator over a fact the tree knows, redding 15
> READMEs on day one with no remedy but hand-editing all of them.

**`TOOL-aMouldedFolio-3` is the precedent that a build README corpus IS operated on wholesale — 31
files in one commit — provided the operation is MECHANICAL, and it gates specifically against the
hand-edit alternative.** The principle the curation-debt row invokes is real but narrower: it is
`TOOL-aMouldedFolio-3`'s **§3 non-goal**, *"No prose template for the authored narrative — 19 of 31
READMEs carry no `##` heading at all"*, and the census's §3 conclusion 3 at `:146`:

> **Narrative → leave authored and ungated.** A prose template would describe 8 files and invent a
> rule for 17. **Do not write it.** The entrypoint quality problem is real but it is an
> authoring-discipline problem, not a schema problem, and a template that 17 of 25 files violate on
> day one is decorative.

**This is the loudest thing in this report. The owner's ask is, in the census's own words, the prose
template it told this repo not to write.** Re-measured today, the ratio is worse, not better:

```
READMEs whose AUTHORED half carries no '## ' heading: 20  (was 17 of 25 → now 20 of 61)
READMEs whose AUTHORED half carries >=1 '## ' heading: 41
total '## ' headings across the 61 authored halves:  176
```

That does not make the ask wrong. It makes it a **superseding decision**, and §6 is explicit about the
form one takes: *"never rewrite a ratified record — supersede with a new id + note"*. The design pass
owes a new decision id that names `TOOL-aMouldedFolio-1` conclusion 3 and `TOOL-aMouldedFolio-3` §3,
says the owner has reversed them, and says on what evidence. Shipping the slot set without that note
leaves two ratified records silently contradicted, which is the two-answers-to-one-question class this
repo refuses by name.

### The analogous move: is there a "remove the readers" option here?

The brief points at `TOOL-aBoundedVerdict-11` S8, which retired the authored `roster:units` pair
*"by removing its READERS, not by editing the corpus"*
(`memory/builds/aBoundedVerdict/spec/2026-08-19-spec-TOOL-aBoundedVerdict-11.md:83`):

> **The four READMEs carrying an authored `roster:units` pair keep their bytes.** … a region nothing
> reads is inert, and deleting text from four build records to satisfy a code change is the wrong
> direction. What is OUT is any rewrite of those four files.

(The four is now **eleven** —
`git grep -l -- '<!-- roster:units -->' -- 'memory/builds/*/README.md' | wc -l` → 11 — because S8
kept `roster_ids` on the authored pair as the only carrier that can name a planned-but-unspecced unit.
So the retirement was partial and the population grew afterwards. Worth knowing before anyone plans
around "four".)

**The analogous move here is ADDITIVE-ONLY, and it is available.** The owner's contract has two
halves that behave completely differently:

- **The STRUCTURE half** (which slots exist, in what order, containing what shape) is mechanical.
  There is precedent for a generator inserting structure into an authored build README without moving
  an authored byte: `insert_region` (`gen_build_index.py:1009`) — *"Create a missing pair at its
  CANONICAL slot, moving no authored byte."*
- **The CONTENT half** (what the description says, which improvements were expected, which detriments
  were accepted) is NOT derivable and NOT another session's to write. It is the
  `REVIEW_VERDICT_CUTOFF` case exactly: *"a verdict ASSERTS a conclusion nobody wrote, so deriving one
  would put this session words into another node record."*

So "remove the readers" has no analogue — there is no reader to remove, the whole point is to ADD one.
But **"add the structure mechanically, never the content"** is the available move, and it must be
resisted anyway for one reason: inserting 61 empty `## Expected improvements` headings creates 61
empty slots nobody fills, and a gate satisfied by its own scaffolding is §7's "a gate satisfied by its
own comment prose". If the structure is inserted, the content check must NOT then be armed over it.

### And a design the repo already rejected once

`TOOL-aRuledFrontispiece-1`, Alternatives rejected, `:156`:

> Bounding the prose by a marker pair of its own was rejected: it makes every README carry two more
> lines to solve a problem that position already solves, and an author who puts prose in the wrong
> place is not helped by being asked to wrap it.

If the slot set is going to be delimited by markers, that record has to be superseded too.

### The ownership answer, stated plainly

No key makes this repair anyone's to do.

- 45 of 61 READMEs are node `a`'s; 7 `c`; 6 `d`; 3 `b`.
- Of the 12 LIVE builds: 10 node `a`, 1 node `b`, 1 node `d`.
- The build method (`:237`) says a build re-reads **its own** README before closing. It says nothing
  about anyone else's.
- The two registry rows that name build-README curation as another owner's job have sat undrained for
  nine days.

**Therefore: the only unit of repair this repo's own norms admit is "the next build to touch a README
brings it into contract".** That is not a migration plan — it is the absence of one, dressed as a
ratchet. Which is fine, and is what §5 recommends, provided nobody pretends the corpus will converge
on a schedule.

The one genuine precedent for a *deliberate, owned, corpus-wide* authored surgery is
`TOOL-aRuledFrontispiece-11`, and it is worth reading as the template for how such a thing is done
properly (`memory/builds/aRuledFrontispiece/build/2026-08-17-build-TOOL-aRuledFrontispiece-11-corpus-surgery.md`):

- the population was **derived, not chosen** — `--check-format` named the files; a hand estimate had
  said 14 and the real predicate said 6;
- it was its own unit at its own declared position in the build order, with the binding gate landing at
  a LATER position (`spec-1:151` — *"The surgery at position 9 conforms the corpus; the leg at position
  11 makes the refusal binding"*);
- **conservation was proved by a sorted-multiset hash per file**, because *"a diffstat cannot show
  this — a move reads as balanced additions and deletions whether or not a line was altered in
  transit"*;
- and a scope item that did not fire was **recorded rather than quietly dropped**: *"No `roster:units`
  pair was ADDED … Inventing the boundary per file is the judgement S4 refuses to make."*

That last bullet is the direct precedent for the present case. When a corpus surgery reached the point
where it would have had to decide, per file, where an authored plan begins and ends, **it stopped and
recorded that it had stopped.** The closed slot set asks a session to make that judgement 61 times.

---

## 5. Live vs terminal — and the argument the counts make

```
# LIVE builds = rows in memory/LIVE.md (a build leaves when every unit is terminal)
LIVE builds: 12
ALL builds:  61
CLOSED:      49
```

The 12 live ones, with their authored-half size and node:

| Build | node | authored half | roster pair |
|---|---|---:|---|
| aBatchedLintel | a | 401 B | no |
| aDeployScout | a | 492 B | no |
| aPortableWarden | a | 627 B | no |
| aMendedLedger | a | 796 B | no |
| aQuarriedLantern | a | 425 B | no |
| aFerriedDossier | a | 2,440 B | no |
| bConvergentLodestar | b | 2,987 B | no |
| aWalkedCorpus | a | 4,010 B | no |
| aTetheredScratch | a | 4,896 B | yes |
| aDeclaredBound | a | 6,694 B | yes |
| dScriptedRepeat | d | 9,429 B | no |
| aPacedTurnstile | a | 19,450 B | no |

**Sum: ~52.6 KB, against 352.9 KB for the whole corpus — the live set is 15% of the authored prose.**
Eight of the twelve are under 5 KB and would fit the new contract almost as-is.

### The argument: closed builds should be OUT of scope

1. **Nobody resumes from a closed build's README.** `memory/LIVE.md`'s own header states the
   membership rule: *"builds with at least one non-terminal unit… a build leaves this file when every
   one of its units reaches a terminal status."* A closed build is a historical artifact; the reader
   who needs it is doing archaeology, and archaeology is served by the narrative the contract would
   delete, not by a four-slot summary.
2. **The content cannot be honestly written for them.** EXPECTED-IMPROVEMENTS is a statement about what
   the author *expected*, made before the fact. Writing it after a build closed is not recording a
   judgement, it is inventing one — `REVIEW_VERDICT_CUTOFF`'s exact refusal.
3. **The cost falls entirely outside the repairing session's ownership.** 49 closed builds, of which
   at most 6 belong to node `d`.
4. **The three biggest closed READMEs are already gate-exempt for size.** `aBoundedVerdict` (44,872 B),
   `dUnstalledConvoy` (35,745 B) and `cBriefedPilot` (32,023 B) sit in `curation-debt.txt` because
   they blew `BUILD_README_CAP_BYTES` (25,600). Bringing them into a new contract means touching the
   exact files this repo has already twice declined to touch.
5. **The corpus doubles every ~three weeks** (40 builds in the last 14 days). A live-only rule reaches
   parity with today's whole corpus, in fully conforming files, in about 21 days — with **zero**
   authoring acts on anything already landed.

### The counter, stated fairly

The census's §5 objection to a cutoff was that it exempts *everything*, and it was right about
`opened:`. A live/terminal key does not have that defect: it governs **12 of 61 today**, which is a
non-empty population, so the check's first run is a real measurement rather than the "coverage of
nothing" that `check-memory-hygiene.sh:1168` has to apologise for. But it has its own defect worth
naming: **a build's live/terminal status is MUTABLE**. A unit can be re-opened by an M2 AMEND, so a
build can leave the population and re-enter it. For a *structural* rule that is harmless (the bytes do
not change while closed). For a *content* rule it means a build could close having satisfied the rule
and reopen with the rule's content now stale — which is precisely the `readme_mechanism_drift` class,
already pinned at 19 and already report-only.

---

## 6. Unattended-kit interaction — the verdict is SAFE, with three named conditions

### What is actually compared at BASE

Every BASE-relative read of a build README in the whole kit
(`grep -rn 'GIT show .*base' tools/unattended/*.sh`, excluding tests) is one of three, and none of
them touches authored prose:

| Site | What it reads at BASE |
|---|---|
| `unattended.sh:1127` (`check_authorization`) | the whole blob, parsed for: `---` at line 1, `slug:`, `authorized-by:`, `playbook:`, `pieces:` — then the `gen:build-units` region's **unit-ID set** |
| `check-unattended.sh:237` (merge-bar leg) | the `gen:build-units` region only, id-set delta vs HEAD |
| `lib-unattended.sh:180` (`baseline_units`) | the `gen:build-units` region only |

`roster_ids` (`unattended.sh:1487`) reads the **working tree** README, never a BASE blob.

The protocol says so in its own words, `memory/guides/UNATTENDED-PROTOCOL.md` §1:

> **Only its SHAPE is checked.** It resolves at BASE, parses as front matter, and its `slug:` names the
> build. No gate can tell whether the owner meant it.

and

> **IDS, never row bytes** — a row carries the unit's status, rev and date, so a byte comparison would
> refuse every run that BUILT anything.

And the generator already knows this and defends it — `gen_build_index.py:49–53`:

> The AUTHORED plan region. This generator NEVER writes between these two markers: the unattended
> kit's `check_authorization` byte-compares that slice across a run's pinned BASE, so a renderer that
> touched it would silently invalidate every run authorized against the file.

(That comment is now **stale** — S8 moved the comparison to the generated units region and `roster_ids`
reads only HEAD. It is harmless, because the generator not writing there is still correct behaviour,
but it is a live example of the drift class this whole design pass is about, sitting in the generator
that would implement it.)

### Verdict

**A corpus-wide restructure of the AUTHORED half invalidates no run's authorization**, provided:

- **U1** — front matter still opens at line 1 with `---` and still carries `slug:` matching the folder.
  `check_authorization` `fail 7` fires on the first byte otherwise.
- **U2** — the `gen:build-units` marker pair survives and its **id set never shrinks**. Additions are
  admitted (`fail 20`, `comm -23` BASE→HEAD). A restructure adds and removes prose, not ids, so this
  is satisfied by construction — but a "rewrite the file from a template" implementation would drop
  the region and break it.
- **U3** — the 11 authored `roster:units` pairs are left alone or migrated deliberately. `roster_ids`
  still feeds `missing_units`, and S8 explicitly kept it as *"the only carrier that can express a unit
  somebody planned and nobody specced"*.

### Is anything mid-run?

**No.** All 16 tracked run-state files are in a terminal phase:

```
# grep -m1 '^phase:' on each memory/builds/*/RUN.md
LANDED  11   (aBoundedVerdict aBranchedMandate aDeclaredBound aDeclaredCeiling aFusedCharter
              aPacedTurnstile aPromptedMandate aScannedThrottle aSealedCaravan aSiftedPlaybook
              dUnstalledConvoy)
ABORTED  5   (aMeteredTurnstile aWalkedCorpus cBriefedPilot dClosedLexicon dScriptedRepeat)
```

`PHASES_TERMINAL="LANDED ABORTED"` (`unattended.sh:239`), and `verb_resume` (`:2259`) refuses on a
terminal phase — *"nothing to resume — phase $p is terminal"*. So **no run can be resumed into a
post-surgery tree**, and none is holding a pinned BASE it will read again. A *new* run against any of
these build folders pins a fresh BASE from the remote's HEAD advertisement, which will be
post-surgery.

**The one residual race** is a run started on another node before the surgery lands and closing after.
Its `check_authorization` re-reads its own old BASE — which is fine, U2 holds — but the merge-bar leg
at `check-unattended.sh:237` compares that old BASE against the *merged* HEAD, still id-only. Safe.

### Safe ordering

1. Land the structural change **behind no flag at all but with the new check unarmed** (or scoped to
   a population of zero) first.
2. Any authored surgery lands **in its own commit**, touching zero generated bytes, verified by
   `gen_build_index.py --check` reporting the same clean verdict and artifact count at the surgery's
   tip as at its parent (this is `TOOL-aRuledFrontispiece-11`'s own AC1 shape) **and** by the sorted
   non-blank-line multiset hash per file.
3. The binding leg lands **after** the surgery, never with it.
4. Never run a surgery while any `RUN.md` is non-terminal. Check with the phase grep above; today it
   is clean.

---

## 7. Recommended landing plan

### 7.1 The mechanism: a SWITCH cutoff on the DERIVED status, not a date on `opened:`

**Key: the build's derived live/terminal status, as `gen_build_index.py` already computes it and
`memory/LIVE.md` already publishes it.** Population today: 12. Non-empty, so the check's first run is
a measurement (C9). Not forgeable without flipping a spec status header, which check 12 already gates
(C-implicit). Costs zero extra git calls — the generator has the value in hand.

Belt and braces, and this is the part that matters most: **make it a SWITCH, not a SELECTOR (C6).**
Validated-when-present for every one of the 61; REQUIRED only for builds in the live set. The census
measured why, at `:191`:

> **The soft shape is the only one that has ever drained.** `streams` is validated-when-present,
> required-only-after the cutoff — and **15 of 33** pre-cutoff specs adopted it with zero gate
> pressure, against **0 of 11** for §10.

45% voluntary adoption against 0%. A closed build that wants to conform may; a closed build that
cannot is never red; and nobody is forbidden from improving a record, which is `SPEC10_CUTOFF`'s
pathology.

If a date key is wanted anyway for portability to adopters (a live/terminal key needs a spec corpus; a
date does not), then declare `BUILD_README_SLOTS_CUTOFF` in `.memory-tree.conf` keyed on `opened:`
**and say in the comment that the key is forgeable and 26% divergent from git**, per C1/C5. Do not
present it as integrity. It is a scheduling device.

### 7.2 Closed builds: OUT of scope, permanently

Not "out for now". `RECORD_UNBOUND_PIN`'s comment is the model: a permanent exemption with a stated
reason beats a shrink-only pin nobody can drain. 49 files, 43 of them another node's, whose two
judgement slots cannot be honestly authored after the fact.

### 7.3 Who repairs what

| Population | n | Who | When |
|---|---:|---|---|
| New builds opened after the cutoff | ~2.9/day | the opening session | at DoR, as part of scaffolding |
| The 12 live builds | 12 | each build's own next session | at its next close, per `BUILD-METHOD.md:237` |
| The 49 closed builds | 49 | **nobody** | never — permanently exempt |
| The 3 over-cap giants | 3 | already in `curation-debt.txt` | unchanged |

**No corpus surgery.** If the owner insists on one, it is its own unit, at its own build-order
position, with the binding leg at a later position, with a derived population and a per-file
conservation hash — `TOOL-aRuledFrontispiece-11`'s exact shape — and it may relocate prose into each
build's `build/` folder but must not delete it.

### 7.4 Landing order, so the bar is never red

1. **Unit A — the slot grammar, documented and unarmed.** Write the contract into
   `tools/memory-tree/HYGIENE.template.md` **first**, re-render `memory/HYGIENE.md` from it (the
   direction matters — `aRuledFrontispiece-1:163` records that editing the pair "together" inverts
   the parity harness). Declare the conf key. No check reads it yet. Bar stays green trivially.
2. **Unit B — the predicate, run over the real tree, printing hits AND near-misses, still unwired.**
   §7's rule. This is where the "would this red an innocent file" question gets answered with data,
   and where C1's measurement is produced.
3. **Unit C — scaffolding for NEW builds.** The kickoff/opening path emits the slots. Population
   grows from here at ~2.9/day and every new member is born conforming.
4. **Unit D — the check, armed, on the live-set population, wired into the existing
   `build README slot contract` leg.** That leg already exists in `tools/gate-legs.json`
   (`python3 tools/memory-tree/gen_build_index.py --check-format`), has **no guard** so it runs on
   every bar, and is `"subject": "repo"` — so it survives the kit-self-test hold that
   `GATE_SELFTESTS` gates. It reports `slot contract clean (61 build README(s))` today. Extending it
   costs no new leg and no new declaration.
   **Its failing case must be observed before it lands** (§7: stage the break, confirm RED, unstage),
   and because the pre-cutoff corpus does not exercise the required arm (C4), `--selftest` carries
   explicit red/green fixtures for the required-and-missing case and for the
   present-but-malformed case.
5. **Unit E — the superseding decision record.** A new id, in `memory/DECISIONS.md`, naming
   `TOOL-aMouldedFolio-1` conclusion 3 and `TOOL-aMouldedFolio-3` §3 and stating that the owner has
   reversed the no-prose-template ruling, on what evidence. Per §6, a ratified record is superseded,
   never rewritten. If markers delimit the slots, `TOOL-aRuledFrontispiece-1`'s Alternatives-rejected
   entry at `:156` is superseded too.
6. **Unit F — fix `curation-debt.txt:4`.** The citation is wrong; `TOOL-aMouldedFolio-3` is the
   mechanical-surgery precedent, not the leave-it-alone one. The row's *conclusion* may well stand on
   the census's §3 instead — cite that.

### 7.5 What stays broken, registered rather than fixed

Stated explicitly, because an exemption is not coverage (§7):

- **49 closed build READMEs never conform.** Permanent, by declaration in the conf comment, not by a
  registry row. Compensating check: none, and none is possible — the content is unwritable after the
  fact. Say so, the way `ACCEPTANCE_LEDGER_GRANDFATHER`'s comment does for
  `TOOL-aMeteredTurnstile-1`: *"No compensating check is claimed for it, because none is possible."*
- **`readme_mechanism_drift` stays at 19 and stays report-only.** It is the only instrument in the
  tree that grades build README prose against reality, its own backlog row
  (`TOOL-dScriptedRepeat-14`, CLOSED) records that *"THE MOTIVATING INSTANCE IS INVISIBLE TO IT"*,
  and the new contract does not change that. Do not let a green slot check read as prose truth.
- **The 11 authored `roster:units` pairs stay.** S8's non-goal still binds and `roster_ids` still
  reads them.
- **The 4 over-cap READMEs stay in `curation-debt.txt`.** Untouched by this work.
- **`aPacedTurnstile` is 100 bytes under the 25,600 cap** (25,500 B) and is **not** exempt. Any change
  that adds bytes to it reds check 6. Named here so it is not discovered at the push boundary.
  `dScriptedRepeat` (24,296 B) has 1,304 B of headroom — roughly one slot set.
- **`gen_build_index.py:49–53`'s comment about `check_authorization` byte-comparing the plan region is
  stale** since `TOOL-aBoundedVerdict-11` S8. Correct it in whichever unit touches that file, or spawn
  a row. It is a two-answers-to-one-question in the generator that would implement this contract.

---

## Appendix — commands used

```bash
git ls-tree -r --name-only HEAD -- memory/builds | grep -c 'README.md$'
git ls-tree -r --name-only origin/main -- memory/builds | grep -c 'README.md$'
git grep -l -- '<!-- roster:units -->' -- 'memory/builds/*/README.md' | wc -l
grep -oE '\[([A-Za-z]+)\]\(builds/' memory/LIVE.md | sort -u | wc -l
for f in $(git ls-files 'memory/builds/*/README.md'); do sed -n 's/^node: *//p' "$f" | head -1; done | sort | uniq -c
for f in $(git ls-files 'memory/builds/*/README.md'); do awk '/^<!-- (gen:|roster:)/{exit} {print}' "$f" | wc -c; done
for f in $(git ls-files 'memory/builds/*/README.md'); do
  o=$(sed -n 's/^opened: *//p' "$f" | head -1); g=$(git log --diff-filter=A --format=%cs --follow -1 -- "$f"); done
for f in $(git ls-files 'memory/builds/*/RUN.md'); do grep -m1 '^phase:' "$f"; done
python tools/drift-audit/drift_report.py
python tools/drift-audit/drift_report.py --json
python tools/memory-tree/gen_build_index.py --check-format
grep -rn 'GIT show .*base' tools/unattended/*.sh
```
