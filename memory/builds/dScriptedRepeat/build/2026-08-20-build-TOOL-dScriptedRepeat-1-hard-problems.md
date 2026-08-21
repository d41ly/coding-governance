**Serves:** research TOOL-dScriptedRepeat-1

# Lens 5 — the four hard problems

*Research record · node d · 2026-08-20 · build `dScriptedRepeat` · adversarial lens.*

Every claim below is either MEASURED (a command, a `file:line`, a reproduction in a throwaway repo made
with `mktemp -d`) or explicitly marked **inference**. Nothing was written into this repo except this
record. Probe repos lived under one `mktemp -d` root as `repoB`, `repoC`, `repoP` and are discarded.

---

## 0. The five findings that change the design

Ranked by what they cost if the build starts without them.

1. **`DOD_EXTRA` cannot carry `pieces-complete`.** A project item declared `:machine` is satisfied by
   the run writing one line into the file it owns. Reproduced: with
   `DOD_EXTRA="pieces-complete:machine"` and `printf 'pieces-complete: yes' >> RUN.md`, `--close`
   passed the item with **zero pieces on disk and no tracked spec in the build**.
   `unattended.sh:1881-1882` is the whole checker for any item the kit does not name. Meanwhile
   `--attest` refuses that same item at `unattended.sh:1923` saying *"writing its key by hand is the
   self-certification the Definition of Done exists to prevent"*. The verb refuses it and the reader
   honours it. This is a live defect in landed code, not only a playbook-mode problem.
2. **The attended entry point cannot use `--close` at all.** Reproduced with no remote:
   `authorization-reachable` is UNMET, and `--override authorization-reachable` is refused by name at
   `unattended.sh:1645`. `closing-review-recorded` is unmet too, because it reads `base:` and refuses a
   value shorter than seven characters. Fork 1's anchorless attended path therefore cannot be a fourth
   mode of the same driver; it has to be a path that never reaches `verb_close`.
3. **A run-state file with no `base:` reds the merge bar forever.** `check-unattended.sh:335-339`:
   *"AN ABSENT `base:` LINE IS THE VIOLATION, not the exemption."* So the attended path must write NO
   run-state file, or it poisons `bash tools/run-gates/run-gates.sh` on a record no verb rewrites.
4. **The output-path gate is vacuously satisfiable, and I observed it.** Arm 4b in `repoC`: a
   playbook-mode branch that wrote a `RUN.md` and re-rendered `LIVE.md` and the ledger, and **no pieces
   at all**, scored `rc=0`. A gate phrased as "nothing outside the declared paths" is a negative
   predicate, and doing nothing satisfies every negative predicate. Fork 2 and fork 3 have to be ONE
   check or the pair is theatre.
5. **`git diff BASE HEAD` is the wrong diff by an order of magnitude.** Measured over the 13 tracked
   runs in this tree: `aSiftedPlaybook` shows **383 files** at `BASE..tip` against **17** for the
   commits it authored on its own first-parent chain; `aSealedCaravan` shows **423 against 36**. The
   surplus is `main` merged in mid-run. And `--no-merges` is not the repair: seven of
   `aSealedCaravan`'s first-parent merges carry combined-diff changes across 70+ files, including
   `tools/unattended/unattended.sh` and `tools/memory-tree/check-memory-hygiene.sh`, so conflict
   resolutions would be invisible to it.

Two more, smaller but load-bearing, are in the body: the reference playbook `HYBRID-PLAYBOOK.md`
contains **zero** occurrences of `GATE` or `CHECK` and would be rejected by fork 5's validity gate as
written (§4.3); and the build method's pass vocabulary is CLOSED and does not contain "a piece
produced" (§1.5).

---

## 1. PROBLEM A — "pieces are passes" against `build-complete`

### 1.1 What `build-complete` actually reads

`dod_met`, `unattended.sh:1763-1830`. Five terms, evaluated sequentially so each can name itself:

1. the build README carries exactly one well-formed `<!-- gen:build-units -->` pair;
2. `unit_rows` (`unattended.sh:1056-1060`) selects rows matching `^\| \[.*\]\(spec/` inside that pair, and the selection is non-empty;
3. `unit_ids_of` finds at least one `FAMILY-slug-N` in the region;
4. `missing_units` — every id in the AUTHORED `<!-- roster:units -->` pair has a tracked spec;
5. `nonterminal_units` — no selected row carries a status other than `CLOSED` or `WONTDO`.

Term 4 is the only one that can see a planned-but-unspecced unit, and it is inert when the authored
roster pair is absent: `roster_ids` returns 0 at `unattended.sh:1007` on a README with no `ROSTER_OPEN`.
Measured, `grep -l '^authorized-by:' memory/builds/*/README.md` matches **nothing**, and the driver's own
comment at `unattended.sh:1794-1798` records that only four of 49 build folders carried a roster pair
when that term was rewritten.

`TOOL-aPromptedMandate-12` narrowed term 2's selector from `^\| \[` to `^\| \[.*\]\(spec/` because the
generated region renders TWO tables and every review record was counting as an unfinished unit. Its spec
is `memory/builds/aPromptedMandate/spec/2026-08-18-spec-aPromptedMandate-12.md`, and two of its
decisions bind anything we add here:

- The discriminator is **the link target**, chosen over the status column because *"filtering rows that
  merely CONTAIN a status token would work today and rot the moment a record's kind column holds a word
  that looks like one"* (§4). A piece register rendered into that same region would have to avoid
  `](spec/` or it re-creates the exact defect that unit removed.
- Its §3 says **"No change to `gen_build_index.py`"**, and its §4 says the two-table render *"is the
  generator's design and other readers depend on it"*. Adding a third table to that region is a change
  the previous unit deliberately declined to make.

### 1.2 What `build-complete` therefore means for a playbook run

Under fork 3 — one unit per playbook RUN — the units table holds exactly one row, and `build-complete`
is green if and only if that one spec's status header says `CLOSED`. **The status header is authored by
the run.** Nothing in the five terms counts pieces, reads output paths, or looks at the filesystem
outside the spec set.

Reproduced in `repoB`: a build whose README carries one `CLOSED` row pointing at `spec/one.md`, where
`git ls-files 'memory/builds/tPlay/spec/*.md'` returns **empty**, passes `build-complete` without
complaint.

**Honest limit on that reproduction.** In the real repo the `memory hygiene` leg re-renders the region
and reds on drift (`check-memory-hygiene.sh:593`, *"generated build index differs from a fresh render"*),
so a hand-written row is caught by `gates-green` rather than by `build-complete`. My fixture had
`GATE_CMD="true"`. **What survives the fresh render is the real problem: a genuinely generated one-row
region, rendered from a genuinely CLOSED spec, over a run that produced zero pieces.** No render can see
that, because the renderer's input is the spec set.

### 1.3 The four mechanisms, scored against the house rules

| # | Mechanism | derive over author | no count in prose | probe can move | vacuity |
|---|---|---|---|---|---|
| A1 | a new generated region in the build README listing pieces | yes, rendered from the filesystem | yes | yes | **no floor** — renders 0 rows and is green |
| A2 | a manifest file the playbook declares | **no** — the run authors it | no | yes | trivially forged |
| A3 | per-piece status derived from the filesystem | yes | yes | yes | **no floor** — identical to A1 |
| A4 | a machine DoD item comparing a **BASE-pinned N** against a **diff-derived count** | yes for the count | yes | yes, if it refuses when N is unreadable | **closed on the default-branch anchor** |

A1 and A3 fail for the same reason, and it is the reason `build-complete`'s own term 3 exists. The
driver's comment at `unattended.sh:1770-1773` states it: *"term 5 is VACUOUSLY TRUE over an empty
selection — `region` exits 0 with empty stdout for a well-formed pair enclosing nothing"*. A piece
register derived from the filesystem is a selection, and a selection with no floor is satisfied by
producing nothing. Renders-zero-rows-and-is-green is that same defect one level up.

A2 fails on the first column and needs no further argument.

**A4 is the only one that cannot be satisfied vacuously, and the reason is provenance, not arithmetic.**
The floor `N` has to come from a blob the run cannot have written. That blob already exists and the
driver already reads it: `check_authorization` runs `GIT show "$base:$rel"` at `unattended.sh:764` and
parses front matter out of it with one awk at `:783-787`. `authorized-by:` is already an extra key read
exactly that way. Adding `pieces:` and `outputs:` beside it costs nothing — `parse_front_matter` at
`gen_build_index.py:190-228` validates only `REQUIRED_KEYS = ("slug", "node", "opened", "streams",
"roster", "ids")` and passes every other key through untouched.

### 1.4 What stops a run writing zero pieces and reporting green

Only this, and it has to be stated as a conjunction because either half alone is vacuous:

> `pieces-complete` is met when **N**, read from the build README front matter **at the pinned BASE**,
> equals the number of DISTINCT pieces the run's own diff touched under the output globs read from that
> same BASE blob; and it REFUSES — never passes — when the BASE blob is unreadable, when `pieces:` is
> absent, or when the glob set is empty.

The last clause is the liveness assertion. Without it the check reports a reassuring `0 == 0` exactly
when its inputs are gone, which is the shape `AGENTS.md` calls a probe that cannot move.

**And it cannot be a `DOD_EXTRA` item.** Reproduced in `repoB`:

```
$ printf 'pieces-complete: yes\n' >> memory/builds/tPlay/RUN.md
$ bash unattended.sh --close tPlay          # DOD_EXTRA="pieces-complete:machine"
(no complaint — the item is SATISFIED)

$ bash unattended.sh --attest tPlay --item pieces-complete
UNATTENDED check 47 FAILED — --attest refuses a MACHINE-checked item, because writing its key by
hand is the self-certification the Definition of Done exists to prevent
```

`dod_met`'s default arm is `grep -qE "^$item: (yes|true)" "$rel"` (`unattended.sh:1881-1882`), and the
merge-bar leg does not close it either — `check-unattended.sh:806` says outright *"Item NAMES only. The
checker column is deliberately not joined."* So `pieces-complete` must be a **core** item with real code
in `dod_met`, or the kit must grow a way for a project to declare a machine item with a COMMAND, at
which point `--attest`'s refusal and `dod_met`'s reader would finally agree with each other.

### 1.5 What fork 3 collides with

`memory/guides/BUILD-METHOD.md:133-134`:

> **A PASS is exactly one of:** a spec authored · a spec reviewed · a review's fixes folded in · a unit
> built · the closing diff review. **Nothing else is a pass.**

That set is CLOSED and it is machine-joined. `PHASES_PASSKIND="SPECCING REVIEWING FOLDING BUILDING"` at
`unattended.sh:88` is compared in both directions against the protocol's "PASS kinds:" list by
`check-unattended.sh:794-803`, and a phase published as a pass kind that is not in the core vocabulary
is `fail 16`.

So fork 3's phrase "pieces are PASSES, not units" is true in spirit and **false against the method's
vocabulary as written**. A piece is produced INSIDE the `a unit built` pass. Two consequences:

- The design must not introduce a fifth pass kind or a `PRODUCING` phase without moving
  `BUILD-METHOD.md` M6, `PHASES_PASSKIND` and the protocol's PASS-kinds list in one commit — three
  places the leg joins.
- M6's *"Commit at the end of every pass"* does NOT hand you one commit per piece for free. If the
  design wants commit-per-piece it must say so as a playbook-mode rule, and a commit subject is authored
  prose rather than a derivation. **Inference: commit counting is the wrong oracle for N.**

### 1.6 Recommendation — A

**Add `pieces-complete` as a ninth CORE machine item with its own arm in `dod_met`.** Read `pieces:` and
`outputs:` from the BASE blob `check_authorization` already fetches, so there is one `GIT show` and no
second reader. Derive the count from the run's own diff under those globs, scoped as §3 requires. Refuse
with a named message when any input is unreadable. Raise the DoD half of `CORE_FLOOR` in the same commit;
the leg pins it at `check-unattended.sh:130-132`.

Make the item **inert by declaration, and loudly**: a BASE blob with no `outputs:` key means this build is
not a playbook build, and the item reports the `skipped` shape with its reason. A silent pass is not
available — `AGENTS.md` §7 requires that a skip announce itself, and this is the branch where a silent
one would matter most, because it fires on every ordinary code build in every adopting repo.

**Strongest counter-argument.** It puts N outside the run's reach only on the default-branch anchor. On
the second (`published`) anchor the BASE is a tip the run itself pushed, so the run authors N — exactly
the concession `UNATTENDED-PROTOCOL.md` §1 already makes for the unit set (*"It does not hold on the
second anchor: there the BASE is a tip the run itself pushed, so it can re-satisfy the comparison against
its own new bytes"*). The honest answer is the one the protocol already gives: state in the same sentence
that this term does not hold on the branch anchor, and record which anchor was used. Do not let the item
read as though it did. A second counter is that nine core items is a growing, un-deletable surface for
every adopter; the inert-by-declaration rule is what pays that down, and it is why the rule is not
optional.

---

## 2. PROBLEM B — the attended entry point's authorization story

### 2.1 What `authorized-by:` is today

`unattended.sh:794-798`:

```
case "$AUTH_MODE" in
  prompt|slug) ;;
  *) fail 44 "…outside the closed set of prompt and slug, and defaulting an unrecognised mode would
      select a discipline nobody declared: $AUTH_MODE"
```

It is read from the blob at the pinned BASE (`:764`), defaulted to `slug` when absent (`:793`), recorded
into the run-state file (`:1492`), and **re-derived independently by the merge bar** from the README at
the run's recorded BASE (`check-unattended.sh:466-473`, check 19, whose comment is *"a value only the
driver ever reads is a value only the driver can be wrong about"*). Adding a third member is a one-line
change plus the leg's own knowledge. `scope_of` (`unattended.sh:123-132`) already supports a third field
on a directive entry, so `…:playbook`-scoped directives cost nothing.

One caveat, and it is a real edit rather than a note: `check_waiver_scope` at `unattended.sh:656-668`
hardcodes the literal `prompt` on both sides of its test. Generalising it to `[ "$sc" != all ] && [ "$sc"
!= "${AUTH_MODE:-}" ]` preserves the property its own comment states — an UNDERIVABLE mode must refuse a
scoped waiver rather than grant it — and stops the next mode needing a fourth branch.

**Measured caveat on the precedent.** `grep -l '^authorized-by:' memory/builds/*/README.md` matches
nothing. The `prompt` mode has zero live instances in this tree; every real build defaults to `slug`. So
fork 1's mode value is cheap to add, and the precedent it copies has never run end to end on a real build
in this repo.

### 2.2 What `authorized-by: playbook` MEANS with no mandate — the question is malformed

It means nothing, because with no anchor **the key is never read**. `AUTH_MODE` is set inside
`check_authorization`, which is reached only through `trusted_base`, which is reached only when
`observe_anchor` produced an `ASHA`. Reproduced in `repoB` with zero remotes:

```
UNATTENDED check 24 FAILED — this clone declares a number of remotes other than one …
UNATTENDED check 13 FAILED — a machine-checked DoD item is unmet, so --close blocks: authorization-reachable
UNATTENDED check 13 FAILED — a machine-checked DoD item is unmet, so --close blocks: closing-review-recorded
    the run-state file records no usable pinned base …
```

and the escape hatch is nailed shut:

```
$ bash unattended.sh --close tPlay --override authorization-reachable --reason "attended run has no anchor"
UNATTENDED check 21 FAILED — the authorization item is NOT overridable; an override on the
authorization check IS the authorization check
```

An attended run therefore **cannot close through this driver**, full stop. That kills two of the three
options outright.

### 2.3 The options, and precisely what breaks

**Option 1 — a fourth mode value for attended (`authorized-by: attended`).** Breaks at
`authorization-reachable`, unmet with no anchor and un-overridable at `unattended.sh:1645`; and at
`closing-review-recorded`, whose first term refuses `${#rb} -lt 7` (`unattended.sh:1846-1850`). To make it
work you would have to make two core DoD items conditional on the mode — that is, let a value the run can
influence switch off the item that checks whether the run could influence values. That is precisely the
shape `fail 21` exists to refuse. **Rejected.**

**Option 2 — a mode plus a flag (`--attended`).** The same breakage, plus one worse property: the flag is
an ARGV value, and §9 of the protocol is explicit that *"Nothing a script running under the run's own uid
constitutes authorization."* A flag that relaxes the authorization item is route 2 of the already
reproduced bypass wearing new clothes — the protocol records `GOV_DEFAULT_BRANCH` being demoted from an
input to a cross-check for exactly this reason (`unattended.sh:299-306`, check 29: *"a branch the run can
create with one push is not an anchor"*). **Rejected.**

**Option 3 — a separate non-driver path sharing only the playbook artifact and its gate.** The attended
path writes no run-state file, calls no verb, pins no BASE, and lands through the ordinary explicit-ask
rule in `AGENTS.md` §1. What it shares with the unattended path is exactly two things: the playbook file
and the validity gate over it. **This is the only option that does not require weakening a core item.**

The decisive constraint is not aesthetic. `check-unattended.sh:335-339`:

> `rb=$(fact_of "$f" base)`
> `if [ -z "$rb" ]; then fail 9 "a run-state file records no BASE, and the record is written by the run
> — an absent pin is not a satisfied one"`

with the comment *"Wrapping this in `if [ -n ]` meant deleting one line from a run-writable file disarmed
the only BASE check on the bar."* An attended run that writes a `RUN.md` with no `base:` reds the merge
bar from that commit onward, permanently, on a file no verb rewrites. There is no exemption available
that is not the exemption that comment records having already been removed once.

There is a second, quieter hazard on the same path. `check-unattended.sh:429` guards the whole
authorization block on `[ -n "$rb" ]`, so a record that somehow got past check 9 with an empty base would
**silently skip** checks 13 and 19 — no announcement, no row, no skip shape. That is fail-open under a
comment promising the opposite, and it is a second reason not to put an anchorless record into that
population at all.

### 2.4 `TOOL-aStandingWrit-2` — worse, better, or neither?

The row, `memory/backlog/TOOL.md:41`:

> SECURITY in landed code: the pinned BASE anchors on a remote-tracking ref that `unattended.sh:119-120`
> says needs a push to move. `git update-ref` moves it offline; reproduced with a control, a forged
> anchor passes preflight, the leg and close

**It is already closed on the driver path, and the row is stale about where the hazard now lives.** The
remote-tracking read is gone: `observe_anchor` takes the ref name and the tip from the remote's own HEAD
advertisement (`unattended.sh:285-296`); `GOV_DEFAULT_BRANCH` is demoted to a cross-check that can only
refuse (`:299-306`); and the leg's BASE path was rewritten off `refs/remotes/*` as well
(`check-unattended.sh:340-348`). §9 records the outcome as *"Two one-command offline forgeries that used
to pass every check silently … Both are now inert rather than detected — neither value is read at all."*
Independently, `memory/builds/aWalkedCorpus/spec/2026-08-17-spec-TOOL-aWalkedCorpus-3.md:221` uses
"retire `TOOL-aStandingWrit-2`" as a live retire candidate in its degradation table, which is the corpus
treating the row as closable.

**Verdict on the fork-1 question: NEITHER.** An anchorless attended path does not touch the
remote-tracking class, because it reads no anchor at all. It neither worsens nor improves this row. What
it does create is a *different* member of the same family — a path that lands with no machine-checkable
provenance whatsoever — and that is acceptable only because it also has no push mandate and stops at the
ordinary explicit ask. The moment anyone proposes letting the attended path push, it becomes strictly
worse than the class this row describes, and it should be refused with a pointer to §9's closing
paragraph: *"What actually binds … the same leg, re-run in a clone the run never touched."*

### 2.5 Recommendation — B

**Take option 3.** Say it plainly in the protocol: `authorized-by: playbook` is the third member of the
closed mode set and it governs the UNATTENDED path only. The attended entry point is a Skill section, not
a driver mode; it writes no run-state file; and the one artifact it shares with the unattended path is the
playbook plus its validity gate, which runs as a merge-bar leg over the tracked tree and is therefore
indifferent to who invoked it.

The shape has precedent. The Skill template already carries a second start path (`SKILL.template.md:127`,
"Start a run from a PROMPT"), and the merge bar already orders that section's steps inside its own slice —
`check-unattended.sh:895-925`, check 20, whose comment is the lesson to copy: *"Once a second start path
exists that check keeps grading the FIRST one and is SILENTLY BLIND to the other — which is the failure
direction nobody notices."* Any ordering rule the attended section needs gets its own slice-scoped arm,
never a whole-file one.

**Strongest counter-argument.** Two entry points that share an artifact but not a driver is exactly the
two-answers-to-one-question shape this repo keeps removing, and the attended path leaves no mechanical
record at all — you cannot later ask "was this playbook followed" of an attended run. That is real. The
mitigation is to make the piece-level record (§4) a property of the TREE rather than of the RUN: if the
per-piece record is a tracked file joined to its piece by a content hash, both paths produce the same
evidence and the merge bar reads it identically. The driver then records provenance; the tree records the
work. That is the only split that keeps one artifact and one gate while admitting honestly that the two
paths differ.

---

## 3. PROBLEM C — the output-path refusal and its observed failing case

### 3.1 What "the diff" is — measured, and the naive answer is wrong

I enumerated all 13 tracked run-state files and their pinned bases, then compared the two-dot diff against
the commits each run authored on its own first-parent chain:

| run | `git diff --name-only BASE tip` | own first-parent non-merge commits | ratio |
|---|---|---|---|
| `aSealedCaravan` | 423 | 36 | 11.8x |
| `aSiftedPlaybook` | 383 | 17 | 22.5x |
| `aPromptedMandate` | 181 | 29 | 6.2x |
| `cBriefedPilot` | 52 | 52 | 1.0x, no merges |

The surplus is `main` merged in mid-run. Bucketed by prefix, `aSealedCaravan`'s `BASE..tip` diff carries
**253 files under other builds' folders**; `aSiftedPlaybook`'s carries 222.

`--no-merges` is not the repair. Counting first-parent merges whose combined diff (`git diff-tree --cc`)
is non-empty:

- `aSealedCaravan` — **7** such merges, touching 70+ files including `tools/unattended/unattended.sh`,
  `tools/memory-tree/check-memory-hygiene.sh` and `tools/drift-audit/drift_report.py`;
- `aSiftedPlaybook` — 5; `aPromptedMandate` — 4; `aBranchedMandate` — 3.

Product code whose bytes were decided in a merge resolution is invisible to `--no-merges`. A refusal gate
with that blind spot is a refusal gate an agent walks through by resolving a conflict.

**The correct scope, and it needs a network read:** re-observe the remote's default-branch tip at close —
`observe_anchor` already performs that `ls-remote` — take `M = merge-base(fresh tip, HEAD)`, and diff
`M..HEAD`. That excludes everything merged IN, because those commits are ancestors of the fresh tip, and
it includes evil-merge resolutions, because those are not.

**Inference, partially measured.** My attempt to reproduce that scoping per-run was confounded because
two builds landed through one merge commit: `6382c564` is the landing merge for both `aSealedCaravan` and
`aSiftedPlaybook`, and under merge-target scoping both report the same 305 files. That confound is itself
a finding — **a landing that carries two builds cannot be attributed to one of them by any path-based
scope.** Playbook mode must land alone, or the scope is unattributable and the gate's verdict names the
wrong run.

### 3.2 The predicate, written and run

`scope.sh` in the probe dir. It buckets every path in the diff as `OUT` (matches a declared output glob),
`REC` (under this run's own build folder), `GEN` (the declared generated set), `PBK` (the playbook file
itself) or `FOREIGN` (everything else, and the only red).

Five arms, run in `repoC`, a fresh `git init`:

| arm | what it commits | wanted | **observed** |
|---|---|---|---|
| 1 | 3 pieces, `RUN.md`, `LIVE.md`, ledger, a playbook tweak | green | **rc=0, green** |
| 2 | the same plus `src/app.py` | **red** | **rc=1**, `FOREIGN src/app.py` |
| 3 | the same plus `memory/builds/dProbe/build/evil.sh` | red | **rc=0, GREEN — blind** |
| 4b | `RUN.md`, `LIVE.md`, ledger, **no pieces at all** | red | **rc=0, GREEN — vacuous** |
| 5 | the same plus `memory/DECISIONS.md` and `memory/backlog/TOOL.md` | green | **rc=1, RED — false red** |

Arm 2 is the observed failing case fork 2 needs. Arms 3, 4b and 5 are the holes.

### 3.3 The three holes, each measured

**Hole 1 — the own-records exemption already admits executable code.** `record_paths` in
`gen_build_index.py:311-315` selects *"any depth, ANY extension, under a build's non-spec kind folders"*,
and the binding parser's comment at `:274-276` says *"the corpus holds a non-markdown record (a shell
script), where the line can only be a comment."* Measured: `git ls-files 'memory/builds/**' | grep -vc
'\.md$'` returns **2** — `aBranchedMandate/build/2026-08-16-build-TOOL-aBranchedMandate-3-repro-c3.sh`
and `aMooredAnchor/build/2026-08-11-build-TOOL-aMooredAnchor-1-1-repro.sh`. The exemption is not
hypothetical; the tree already holds two live instances of the thing arm 3 smuggled.

**Hole 2 — the generated artifacts are unavoidable.** `memory/LIVE.md` and `memory/ledger/2026-08.md` are
touched by **13 of 13** runs, and they are the only two paths with that property. They are generated, so
exempting them is correct rather than a concession. But the exemption cannot be a path list typed into the
gate: it must be read from the declaration the generator itself reads, or it is a second copy of a fact
that `.memory-tree.conf` owns.

**Hole 3 — the mandated memory update is FOREIGN.** `AGENTS.md` §1's Definition of Done requires
*"Memory …, decision log/backlog, and the unit's own record updated"*. Measured across the 13 runs:
`memory/backlog/TOOL.md` in 12, `memory/DECISIONS.md` in 11, `memory/guides/SESSION-KICKOFF.md` in 12,
`AGENTS.md` in 12. Arm 5 shows the gate redding an innocent, mandated commit. The exemption set therefore
has to include the project's shared record files — a wide, project-declared exemption, and every
exemption widens the surface the gate was written to narrow.

### 3.4 What class this gate CANNOT see, and whether it is theatre

**It cannot see WHAT is in a file, only WHERE the file is.** Concretely:

- a shell script, a Python module or a build config written under `memory/builds/<slug>/build/` — measured
  live twice in this tree;
- a code change made inside an exempt shared record: `AGENTS.md` is a governing document AND the input to
  `tools/check-playbook-parity.sh`, and `.unattended.conf` is a declaration file the driver sources as
  shell;
- a piece that is itself executable. Nothing stops a declared output path from holding `.sh` or `.py`, and
  for a playbook that generates tests — which the brief names as a content kind — that is the ORDINARY
  case rather than the abuse. **This is fatal to any content-based refinement of the gate:** you cannot
  say "no code in the diff" when the requested content IS code.

**Is it theatre? No, but only if it stops being the whole story.** Arm 2 is a real, observed red on the
real threat model: a playbook run that wanders into the product tree. The class it misses is "code,
correctly filed", and that class is genuinely reachable. So fork 2's split is right, and its two halves
need different weights than the framing suggests — the machine half is a **blast-radius bound**, not a
refusal of code builds, and the CHECK half is the actual refusal. `AGENTS.md` §7 requires that *"A gate's
OWN header states what it does NOT check"*, and this gate's header is where that sentence has to live.

### 3.5 Recommendation — C

**Ship the scope gate as a blast-radius bound with a stated non-claim, and fold fork 3's count INTO it so
the negative predicate acquires a floor.** One check, two directions:

- nothing outside `outputs ∪ own-records ∪ declared-generated ∪ the playbook file` — the direction arm 2
  reds; and
- **at least, and exactly, N distinct pieces inside `outputs`** — the direction arm 4b reds once the floor
  exists.

Scope the diff to `merge-base(fresh remote default tip, HEAD)..HEAD`, never `BASE..HEAD` and never
`--no-merges`. Refuse when the remote does not answer, in the shape `check-unattended.sh:349-355` already
uses (*"this leg will not pass a run it could not check"*). Derive the exemption sets by reading the files
that own them rather than by typing paths. Write the gate as a `*.sh` defining a `fail()` helper, so
`tools/memory-tree/check-arms.py` forces every branch to be armed by a positive assertion in the sibling
`.test.sh` — that is this repo's existing machinery for "the failing case has been observed", and it is
free.

One derivation detail that will otherwise be decided by accident. "N distinct pieces" needs a declared
identity rule, because the same three-file diff yields three different counts. Measured in `repoP`, over a
run that added `content/p3/{body.md,meta.json}` and edited `content/p1/body.md`:

```
paths touched:            3
distinct piece dirs:      2   (content/p1, content/p3)
pieces that are NEW:      1   (content/p3)
```

A factor of three on a three-file diff. `outputs:` must therefore declare the piece GRAIN — a glob whose
match IS one piece — and the gate must refuse a grain it cannot resolve rather than picking one.

**Strongest counter-argument.** The exemption list is now four sets wide, three of them project-declared,
and a run that can commit `.unattended.conf` can widen its own output globs before the gate reads them.
True, and it is the same reduction §9 already states for every local input. The answer is the same one:
the globs that BIND are the ones in the BASE blob (§1.6), and the gate re-derives them from there rather
than from the working tree, so widening them requires a push the owner can see. On the attended path there
is no BASE, the gate reads the working tree, and it buys correspondingly less — which is a sentence that
belongs in the header, not in a document read at a different time.

---

## 4. PROBLEM D — what "follow the playbook to the letter" can mean

### 4.1 The strongest available evidence is a warning

`memory/backlog/TOOL.md:16`:

> `TOOL-aPromptedMandate-11 · OPEN · keepalive-reaped is attestable but not checkable: the driver records
> an id it can never verify, so an agent can attest it in good faith and be wrong. MEASURED here — this
> run asserted twice that two keepalives died with their processes because the store is session-scoped,
> and CronList showed both still firing. Needs a read-back the agent can be held to`

Read carefully, this is not "agents lie". It is worse for our purposes: **the agent's model of a subsystem
it could not observe was wrong twice in one run, and the attestation was sincere.** Step-level attestation
over N pieces multiplies that failure mode by steps × pieces. With the reference playbook's 110 steps and,
say, ten pieces, level-2 attestation asks for 1,100 sincere claims about things the attester may be unable
to see. **Inference, held strongly: attestation does not scale with N; it degrades with N.** The protocol
already refuses to let attested items spend the override budget for a related reason — §4:
*"pretending otherwise makes an override look like a check that failed."*

### 4.2 The four bindings, priced

**(1) The agent is told to follow it.** Cost: zero. Prevents: nothing. Observable failing case: none —
there is no artifact that can be wrong. This is the status quo, and it is what both reference playbooks
currently rely on.

**(2) A per-step attestation.** Cost: N × steps lines the run writes into files it owns. Prevents:
forgetting a step *silently* — an omitted verdict becomes visible. Observable failing case: a record
missing a step id. But every byte it produces is written by the subject, so it is `TOOL-aPromptedMandate-11`
at scale, and `dod_met`'s default arm (§1.4) is the live demonstration of how cheap a self-written "yes" is.

**(3) Each step's GATE leg runs and its result is recorded per piece.** This is the level the reference
corpus already implements, and it is worth reading before designing anything.
`C:/projects/nicocares/main/scripts/check_content_plan.py`:

- **I21** (`:2408-2496`) — the playbook's own rule, enforced. Every `^\*\*[A-Z]\d+\.` step's window,
  bounded at the next step **or heading**, must contain `CHECK` or a `GATE` that NAMES a leg. A `GATE`
  naming an id the script never emits is a separate failure — *"a tag claiming an invariant that does not
  exist is worse than an untagged step, because it reads as enforcement"*. Duplicate step ids are a
  failure. And it carries TWO liveness floors: `steps < 50` reds as I20 (*"the step regex has stopped
  matching and I21 is selecting almost nothing"*) and `len(known_ids) < 15` reds when the id harvest goes
  inert. Its own comments record two observed failing cases — `GATE check_content_plan.py I2/I99` exiting
  GREEN while `… I99` alone red, and a fixed-size lookahead letting D4 borrow D5's tag.
- **I32** (`:1228-1399`) — one JSON record per piece at `content-plan/reviews/<slug>.json`, where the
  **filename IS the join key**; `body_sha256` must match the shipped body (*"the article has moved on
  since it was reviewed, so the verdicts describe a different text"*); `body_words` is recomputed, never
  trusted; the verdict set must EQUAL the harvested Checklist-D step id set (*"an omitted one is
  indistinguishable from a pass nobody wrote"*); the verdict vocabulary is closed; an `N/A` cannot carry
  `fixed=true`; a `FAIL` carries anchors or a scope; anchors must resolve in the body.

Two things to steal, one to refuse.

Steal the **content hash**. It is the mechanism that makes a per-piece record non-vacuous, because it
binds the record to bytes its own author cannot change without invalidating it. Steal the **harvest plus
floor** idiom: the checker derives the step set from the playbook and reds when the harvest goes inert,
which is `AGENTS.md`'s "no count of a derived population in prose" and "a probe that cannot move says so"
implemented as one pattern.

Refuse the **generic-leg assumption**. I21's `LEG_RE` knows the shapes `I\d+`, `C\d+` and `check_*.py`
because they are that project's own. Fork 5 requires *"every named leg is runnable"*, and the kit has no
leg registry: `.unattended.conf` declares one `GATE_CMD`, not a set, and `tools/gate-legs.json` is a
run-gates artifact rather than a kit concept. **Fork 5 therefore needs a new declaration** — a per-project
map from a leg NAME to something runnable — or its "runnable" half is unimplementable and degrades to
"the tag is non-empty", which is exactly the enforcement-claiming-nothing case I21 reds on.

**(4) The playbook compiles to a machine-executable step list and the driver drives it.** Cost: highest,
and it collides with fork 7 head-on — the moment the driver executes steps, it knows HOW a piece is
produced. Prevents: skipping a step, genuinely. Observable failing case: a step that did not run.
**Inference: wrong trade for this kit,** and the reference corpus agrees by construction — 110 steps of
which 54 are CHECK-only cannot be compiled, because there is nothing to compile them TO.

### 4.3 The measurement that sizes the whole question

Over `C:/projects/nicocares/main/content-plan/PLAYBOOK.md`, 1290 lines, using I21's own step regex and
window rule:

```
GATE-only = 25    CHECK-only = 54    both = 31    untagged = 0    total = 110
```

**Forty-nine percent of the steps in the most mature playbook available carry no machine gate at all.**
Level 3 therefore covers at most 56 of 110 steps (GATE-only plus both), and for the other 54 the record
degrades to level 2 — a self-written verdict — however the design is drawn. That is not a defect in the
playbook; it is what content work is.

The second reference playbook is worse, in a way that hits fork 5 directly.
`C:/projects/nicocares/main/brand/art-style/HYBRID-PLAYBOOK.md`, 245 lines: `grep -cE 'GATE|CHECK'`
returns **0**, and `grep -nE '^\*\*[A-Z]?[0-9]+\.'` matches nothing — it has no step-shaped lines at all.
It is a RECIPE: a parameter table, a slotted prompt scaffold, four hard rules, a scene library, a
guardrail list, a ruled-out list and pipeline gotchas. Its §5 "Adding a NEW scene without drift" holds
five plain numbered sentences; its §6 "Guardrails (binding)" holds a *"Commercial-license check (pre-ship
gate)"* whose gate does not exist and an *"Attestation"* whose home the file itself says *"is an open
item"*.

**So fork 5, taken literally, rejects one of the two playbooks the owner named as the target shape.**
Either the validity gate admits a second playbook SHAPE — recipe as well as checklist, each with its own
rules — or the design must say out loud that `HYBRID-PLAYBOOK.md` is not a playbook under this kit and has
to be rewritten into one before it can be run. That is a decision, not mine to take, and it must be taken
before the template is frozen (fork 4), because the template is what decides which shape every NEW
playbook gets.

### 4.4 Recommendation — D

**Bind at level 3, but bind the RECORD to the piece rather than binding the agent to the step.** Three
rules, all machine-checkable, none of which requires the driver to know how a piece is made:

1. **Validity (fork 5), harvest-derived with a floor.** Every step carries `GATE <leg>` or `CHECK <why>`;
   a `GATE` naming a leg absent from the project's declared leg registry is its own failure with its own
   message; and the step harvest reds when it selects fewer steps than a pinned shrink-only floor. Copy
   I21's window rule — bounded at the next step OR heading — because its own comment records that a fixed
   lookahead let one step borrow the next step's tag, *"the 'a check that cannot fail is not a check'
   shape, caught by staging the break."*
2. **Per-piece record, hash-joined.** One tracked record per piece; the piece path is the join key; the
   record carries the piece's content hash and it must match; the verdict set must EQUAL the harvested
   step-id set, not merely intersect it. This is the part worth its cost, and the cost is real: one file
   per piece, invalidated by every edit — which is the point.
3. **A stated non-claim in the gate's own header.** Close to: *this checks that a verdict exists for every
   step and that it describes the bytes that shipped. It does not check that the step was performed, and
   for the CHECK-tagged steps — measured at roughly half of a mature playbook — no machine can.*

**Strongest counter-argument, and it is a good one.** Level 3's per-piece record is written by the run, so
at N pieces it is N sincere self-reports, and `TOOL-aPromptedMandate-11` is the measurement that sincere
self-reports go wrong. Everything rule 2 adds over plain attestation is the hash, which proves the record
describes THESE bytes — not that the verdict is true. **That is a smaller claim than "follow the playbook
to the letter" suggests, and the design should stop using that phrase for the mechanism.** What the
mechanism buys is: a step cannot be silently omitted, a record cannot outlive the artifact it describes,
and a playbook cannot claim enforcement it does not have. What it does not buy is that the agent did the
work — and the honest place to say so is the gate's own header, beside the count it derives.

---

## 5. Cross-findings against the seven ruled forks

None of these re-litigates a fork; each reports evidence its implementation will hit.

- **Fork 1** — implementable as a mode value; the attended half must be a non-driver path (§2.3), because
  `--close` is unreachable without an anchor and a `RUN.md` with no `base:` reds the bar forever. Also,
  `check_waiver_scope` hardcodes `prompt` and needs generalising (`unattended.sh:661`).
- **Fork 2** — the machine gate is real, but it is a blast-radius bound rather than a refusal of code
  (§3.4); three exemptions are forced, and one of them — own records — already admits shell scripts,
  measured twice in this tree.
- **Fork 3** — "pieces are passes" is false against `BUILD-METHOD.md` M6's CLOSED pass set, which the
  merge bar joins in two directions (§1.5). And the DoD cannot count pieces through `DOD_EXTRA`: an extra
  item declared `:machine` is satisfied by a line the run writes, reproduced (§1.4).
- **Fork 4** — the freeze has to decide which SHAPE it freezes; the two reference playbooks have
  incompatible shapes, and one of them carries zero tags (§4.3).
- **Fork 5** — needs a leg REGISTRY the kit does not have. Without one, "every named leg is runnable"
  degrades to "the tag is non-empty", which is the enforcement-claiming-nothing case I21 explicitly reds
  on.
- **Fork 6** — a proposal register that must not block the close is straightforward, but note where it
  cannot live. `park()` (`unattended.sh:1891-1893`) writes into the run-state file, which the merge bar
  greps whole for the bypass flag and whose waiver entries it joins to the first committed blob; a fifth
  `park` kind inherits all of that. A register OUTSIDE the run-state file is also outside §3's exemption
  set and would red the scope gate — so wherever it lands, it lands in the exemption list, and that list
  should be derived from one declaration rather than grown by hand.
- **Fork 7** — agnosticism survives levels 1 to 3 of §4 and dies at level 4. The reference corpus is the
  proof: I21 and I32 together are roughly 290 lines of project-specific checker over a project-specific
  playbook, and the only parts that generalise are the harvest, the floors, the hash join and the closed
  vocabulary. Ship those four; ship no producer knowledge.

---

## 6. One defect worth filing regardless of this build

`dod_met`'s default arm satisfies any `DOD_EXTRA` item, whatever checker it declares, from a line the run
writes — while `--close` prints it as *"a machine-checked DoD item"* and `--attest` refuses to write that
same key on the grounds that doing so is self-certification. The driver contradicts itself across two
verbs, and `check-unattended.sh:806` records that the leg deliberately does not join the checker column,
so nothing else catches it. Reproduced above. It is independent of playbook mode and it is the exact
mechanism playbook mode would otherwise reach for first.

---

## 7. Appendix — what was run

```
git ls-files 'memory/builds/*/RUN.md'                        # 13 runs; bases and phases extracted
git diff --name-only <base> <tip>                            # per run, bucketed by path prefix
git rev-list --first-parent --no-merges <base>..<tip>        # authored-commit file sets
git diff-tree --cc --name-only -r <merge>                    # evil-merge detection
git ls-files 'memory/builds/**' | grep -vc '\.md$'           # -> 2
grep -l '^authorized-by:' memory/builds/*/README.md          # -> no match
scope.sh, five arms, throwaway repoC                         # the §3.2 table
bash tools/unattended/unattended.sh --close tPlay  (repoB)   # §2.2 and §1.4 reproductions
python, I21's step regex and window rule, over PLAYBOOK.md   # 25 / 54 / 31 / 0 of 110
grep -cE 'GATE|CHECK' HYBRID-PLAYBOOK.md                     # -> 0
```

Probe repos were created with `mktemp -d` and are not in this tree. `repoB` mutates a fixture rather than
this repo: the driver ran with `MEMORY_ROOT` pointed at the fixture's own `memory/`.
