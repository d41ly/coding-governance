# Design pass 1 — the directive layer, panelled and folded

A nine-agent `Workflow`: three independent design candidates (minimal-mechanism, checkability-first,
agent-read-path), one judge synthesis under M3's ratification rule, four adversarial lenses
(contradiction, forgeability, drift, decomposition), one folding pass. 51 raw findings; 47 folded,
4 rejected on measured evidence, 5 parked as owner questions. Three of four lenses returned
BLOCKED before folding.

Below is the folding pass's output verbatim.

---

# The unattended directive layer — folded design + M2 decomposition

Supersedes `design-converged.md`. Every change below is a FOLD of an adversarial finding, a PARK, or
a REJECT with the evidence that rejects it. Facts re-measured in this worktree; the measurements are
inline where they decide something.

---

## 0. What survives from the converged design

Unchanged and re-affirmed:

- All eight owner directives already exist as rules. Eleven handles, each a NAME and a POINTER into a
  build-method section. No rule is restated (M1).
- FORK A: a kit-owned constant `DIRECTIVES_CORE` in `unattended.sh`, read by the leg's existing
  `core_of()`. Not a conf key, not a registry document.
- FORK C: flag at invocation → one `AskUserQuestion` (default-deny, reason required) →
  `--preflight --waive <handle> --reason <text>` → a `park()` entry each. **A waiver removes the
  DIRECTIVE, never a GATE, and is never a DoD override.**
- FORK D: `/session-kickoff` AFTER preflight. Check 12, `KICKOFF_ENGINE`, `KICKOFF_EXITS` all stay.
- FORK E: a separate `DIRECTIVES_FLOOR`; `CORE_FLOOR` keeps its two-field shape.
- FORK F: all eleven waivable, with the interactions named.
- DELTA 1 (M6 inverts), DELTA 2 (`build-complete`), DELTA 3 (protocol §6's one sentence).

Deleted outright by folding: `print_directives()`, the M8 review-record authoring edit, the CRLF
"unit", and the `U6 ∥ U8` parallel dogfood.

---

## 1. FOLDS that change the mechanism

### 1a. `--override` becomes repeatable, through the same paired accumulator `--waive` needs
*(C1 / D2 — BLOCKER, confirmed at `unattended.sh:1005`, `:916`, `:940`, `:950`)*

Today `--override) OV="${2:-}"` stores a scalar; a second occurrence overwrites the first, and
`verb_close`'s loop blocks on the second unmet item before reaching `park` at `:952`. Waiving any two
DoD-mapped handles makes `--close` permanently unreachable, with nobody to read the block.

One accumulator serves both flags. Reasons contain spaces, so pairs accumulate newline-delimited and
tab-separated:

```sh
add_pair() { printf '%s\t%s\n' "$2" "$3"; }        # appended to WAIVERS / OVERRIDES
# --override) OV_ITEM="${2:-}"; expects the NEXT --reason; repeatable
```

`verb_close`'s skip becomes `case "$OV_ITEMS" in *"|$item|"*) continue;; esac`, and one `park` entry
per item is written. The `authorization-reachable` refusal (`:932`) still fires wherever it appears in
the list — arm it in that position specifically.

**FG-9's newline refusal is load-bearing for this parser, not only for the record.** A `--reason`
containing a newline is refused, beside W4. That also retro-covers the existing `override` and `abort`
kinds, which have carried the injection hole unread (`park()` at `:995` interpolates the reason
verbatim as the last field).

### 1b. `--waive` refuses a DIFFERING set, not a repeated one
*(C3 / FG-5 — HIGH, confirmed: `splice` has exactly one call site, `unattended.sh:846`, inside
`verb_preflight`)*

`--preflight` is the only writer of RUN.md's generated region, `records-current` diffs that region
against the README slice, and the slice re-renders as units close. So **a second `--preflight` is
mandatory before every `--close`** — and it is also the documented post-compaction recovery command
(`:857-859`). W1 as designed refused the whole verb, wedging the run.

> **`--waive` is accepted by `--preflight` alone. A waiver set byte-identical to the one already
> parked is a NO-OP; a set that DIFFERS from it is a refusal.**

The ordering property survives intact (nothing new can be waived late; nothing recorded can be
changed) and preflight stays idempotent, which the rest of the driver depends on.

### 1c. The recorded BASE is written once
*(FG-7 — MEDIUM, confirmed: `set_fact "$rel" base "$base"` at `:852` is unguarded, eight lines above
the guarded phase write at `:860`)*

Protocol §2 fact 4 says the BASE is "pinned once at run start". The driver rewrites it on every
preflight, and a mandatory re-preflight after an origin reconcile moves it. Guard it exactly as the
phase is guarded:

```sh
[ -n "$(fact "$rel" base)" ] || set_fact "$rel" base "$base" || return 1
```

`trusted_base` already cross-checks recorded against derived and refuses on non-ancestry, so
preserving the recorded value cannot hide a moved anchor. This makes a stated contract true and is a
precondition for §1e's join surviving a long run.

### 1d. `build-complete` — the roster is a PRECONDITION under a mandate, and the population is asserted
*(FG-4, FG-11, FG-6, C11/D9 — confirmed: `grep -rl 'roster:units' memory/` returns exactly ONE path,
`memory/builds/aStandingWrit/README.md`; the literal `MISSING` appears in `unattended.sh` only inside
`fail 19`'s prose at `:624`)*

The converged design kept the roster "opt-in by presence", which makes the roster conjunct vacuously
true for 24 of 25 builds — a completeness check blind to the incomplete case. And it greps `MISSING`
out of a stream that carries the driver's own refusal prose, so it answers a different question and
flips silently on a reword.

Two helpers, extracted once and called from both consumers (this is the reuse §4.1 claimed and did not
have — `verb_status:892` holds the pipeline inline):

```sh
nonterminal_units() {   # run-state file
  region "$1" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null | grep -E '^\| \[' | grep -vE '\| (CLOSED|WONTDO) \|'; }
roster_ids()      { region "$(readme_of "$1")" "$ROSTER_OPEN" "$ROSTER_CLOSE" 2>/dev/null | ...; }
missing_units()   { # roster ids carried by no tracked spec's status header
```

`verb_status` pipes `nonterminal_units | head -1 | sed …`; `--plan` prints a `MISSING` row per
`missing_units` member. The DoD item:

```sh
build-complete)                   # D8b
  # Four conditions, and the first two exist because a check that selects an empty population
  # passes by finding nothing (HYGIENE:54). Under a MANDATE the roster is a precondition, not an
  # option: `check_authorization:493` already locates and cross-compares the pair across BASE.
  printf '%s\n' "$(region "$(readme_of "$slug")" "$ROSTER_OPEN" "$ROSTER_CLOSE" 2>/dev/null)" >/dev/null \
  && [ -n "$(roster_ids "$slug")" ] \
  && [ -z "$(missing_units "$slug")" ] \
  && [ -n "$(nonterminal_units "$rel" ; :)" ] || true   # see spec §4 for the exact conjunction
```

Stated plainly, the item is met when: the build README carries exactly one well-formed roster pair,
that roster names at least one id, every roster id carries a spec, the copied generated region carries
at least one unit row, and no unit row is non-terminal. `verb_plan`'s exit status is never read and its
stdout is never grepped.

**Cost, stated:** every unattended build's README must carry `<!-- roster:units -->`. One of 25 does
today. That is P3 in §5.

### 1e. `closing-review-recorded` — the harness writes the range; the check joins on the index
*(FG-1 BLOCKER, FG-8, FG-13, C5, C12 — measured: `grep -rlE '\b[0-9a-f]{40}\b' memory/builds/*/reviews/`
returns **0**; `^## Verdict` matches 16 files, `^## Verdict:` matches 6, and of those 6 the verdict
values are `BLOCKED` ×5 and `CHANGES REQUESTED` ×1 — **not one record in this corpus carries
`## Verdict: CLEAN`**)*

The converged join demanded a 40-char sha and a colon-bearing heading. Both are grammars this corpus
never writes, so the item's steady state would be the routine override the design listed as a risk.
Three changes, and the net is LESS work than the converged version:

1. **`tools/workflows/tier2-review.js` writes the range.** It already holds `base` (`:65`) and already
   instructs the synth agent to write a markdown report (`:307`). One clause appended to that
   instruction: *open the report with a line naming the reviewed range `<base>...<head>`.*
2. **M8 gains NO review-record edit.** This deletes the converged design's four-word "opening line"
   addition — which C5 correctly showed contradicts M4's "opening with the literal line
   `## Verdict: CLEAN`", a two-answers-to-one-question defect inside the file whose M1 forbids exactly
   that. The mandated rename stays the run's only obligation, unchanged, and FG-13's objection (a
   rename never touches content) evaporates because there is no content step.
3. **The check reads no heading grammar and selects the INDEX**, matching `stage_or_fail:551`'s stated
   rule that the per-run population is the index:

```sh
closing-review-recorded)          # D7
  # A TRACKED review record under this build naming the run's pinned BASE. `rb` is run-written (§9),
  # so this is a construction cost, not a proof. The join is to a value the run pins once (§1c) and
  # the harness writes into the report, so an honest run passes with no authoring step. No heading
  # grammar is read: this corpus writes `## Verdict` and `## Verdict:` and both are legal.
  rb=$(fact "$rel" base); [ ${#rb} -ge 8 ] \
    && git ls-files -z -- "$M/builds/$slug/reviews/*.md" \
       | xargs -0 -r grep -lF -- "${rb:0:8}" | grep -q . ;;
```

### 1f. DELTA 1 keeps the inversion and names its mechanism limit
*(C6 — HIGH claim, fix replaced; confirmed at `BUILD-METHOD.md:91-95` and `REVIEW-PROTOCOL.md:168-170`)*

C6 is right that the obligation had no mechanism. Its own fix routes build passes into a `Workflow`
sidechain — which the same finding shows "inherits no hooks and no `CLAUDE.md`", i.e. the route that
voids the instruction layer this build installs. Both available routes are bad for a BUILD pass; the
direct-spawn budget is keyed per prompt turn and an unattended run has no next prompt to reset it.

M6's replaced sentence, folded:

> **Sequence is the default; parallelism is a claim you substantiate — except under a standing
> mandate, where the claim is owed the other way: two passes meeting all three conditions below SHOULD
> run concurrently, because nobody is waiting to be asked. The concurrency must not cost the passes
> their instruction layer or spend a budget that cannot reset inside a run; where no such mechanism
> exists for the work in hand, sequencing it is a park with a reason, not a violation.**

The three conditions, the write-set rule and the fallback are unchanged. The residual — that today no
mechanism satisfies that clause for a build pass — is P2 in §5, surfaced to the owner rather than
resolved by weakening M6.

### 1g. A waiver relaxes the OBLIGATION, not only the pointer
*(D1 — BLOCKER)*

The sharpest finding in the set, and it makes the entire waiver surface decorative if unfixed. Step 0
becomes mandatory, so every run reads `BUILD-METHOD.md` whole; M2's "Hard floor. Never build a MISSING
or THIN unit" and M3/M4 are unconditional and mention no waiver. A run that waived `sub-specced` holds
two binding answers with nobody to adjudicate.

One bullet in M10 — the section that already exists for unattended deltas — as a POINTER, not a copy:

> - **A directive recorded as waived at preflight is relaxed for that run only.** The vocabulary, the
>   waiver act, its record and what it cannot reach are `UNATTENDED-PROTOCOL.md` §10.

M10's index moves from "Two deltas, and no others" to **three** (transcript, keepalive, parallelism)
plus this bullet. Measured headroom: `BUILD-METHOD.md` is 236 lines / 16466 B against 250 / 20 KB.
This design now spends 6 of 14 lines (was 4).

### 1h. `print_directives()` is deleted
*(C14 / D13 — folded by deletion, the ladder's rung 1)*

At preflight the agent has just read the Skill's table; at `--resume` a compacted agent cannot decode
`sub-specced:M2` any better than it could decode nothing — which is the argument §2.2 used to REJECT
`design-gate-first`'s composed block. M7's read list is explicitly closed ("Read in this order, and
nothing else"), and D1/M10 says speak only when it changes what happens next.

`verb_resume` gains ONE line beside its existing method-path echo:

> `unattended: the directives and their waivers — the table in the unattended Skill; your waivers are
> parked in this file`

The `directives()` accessor stays (W2 needs the membership test). ~10 lines of the converged design do
not get written.

### 1i. The handle→item mapping needs no new field
*(C4 / D3 — HIGH, confirmed at `unattended.sh:782-787`, the recorded `verb_abort` scar)*

Two handles map to DoD items whose names differ: `land-once-done`→`build-complete`,
`diff-reviewed`→`closing-review-recorded`. (`wrap-up-derived` maps to nothing — `parked-decisions-
surfaced` is a GATE, and a waiver never removes one.) The converged design named the mapping nowhere.

The mapping needs no registry field and no new message. `fail 13`'s existing text — *"a machine-checked
DoD item is unmet, so --close blocks: $item"* — **already prints the exact `--override` spelling**. What
was missing is the forward direction, at the only moment the owner is present: **the Skill's table
carries a fifth column naming the DoD item a waiver still owes an override for**, populated for those
two rows and blank for the other nine. Arm A joins columns 1 and 4 (handle and M-section) and ignores
the rest.

### 1j. The Skill's conditionals, made consistent
*(C10 / D7 — MEDIUM; confirmed: `adopt-unattended.sh` renders exactly six keys and none is a kickoff
key; `.unattended.conf:42-47` says a blank `KICKOFF_ENGINE` is legal)*

The converged design protected standalone install at the leg (arm B silent) and broke it at both
places the agent reads. Split by what is actually required:

- **The build method is a RUN-TIME dependency of this kit, and the protocol now says so** (§1). Step 0
  hardens as designed and `--preflight` refuses an absent carrier. Arm B stays silent when the carrier
  is absent for its own reason — *the leg grades the TREE, the driver grades the RUN* — which survives
  independently of the standalone-install argument the design used and this fold drops.
- **The kickoff step stays conditional PROSE**, keyed on the project shipping the skill:
  *"If this project ships `/session-kickoff`, invoke it now — after preflight, never before."*
  No render key, no adopter surface, no composer. Check 18 (§1k) is what pins the ordering.

### 1k. Check 18 asserts ORDER, not presence
*(FG-10 — MEDIUM)*

FORK D's entire resolution is an ORDERING claim ("kickoff-first IS the deadlock, because Step 5b fires
only on a live run-state file"). A grep that the Skill *names* `/session-kickoff` is equally satisfied
by the ordering that deadlocks. One awk recording two line numbers and comparing them — the same
two-line-numbers-and-compare shape `region()` uses at `unattended.sh:105-113`, for the identical
reason (a count-only check is satisfied by a transposed pair).

---

## 2. FOLDS to documents and registries

| # | Fold | Finding |
|---|---|---|
| 2a | Protocol §1: *"The owner's act is `/unattended <slug>` plus, at preflight only, a named and reasoned directive waiver; they author nothing else per run."* §2: *"…the owner authors none of it except the reason text of a directive waiver, which `--preflight` records on their behalf (§10)."* | C2 |
| 2b | Protocol §2 fact 3 enumerates **four** kinds the parked region holds: a parked decision, an abort reason, a recorded DoD override, an owner directive waiver. `park()`'s kind argument is already the discriminator (`:794`, `:952`). | C8, D12 |
| 2c | Protocol §2's spill rule: **waiver entries are not spillable.** Written at preflight, they are permanently the OLDEST entries, so the 8 KB rule evicts them first — after which check 17 passes by finding nothing and M9's row derives from a region that no longer holds them. | FG-3 |
| 2d | Protocol §4: the count sentence is **line 138**, *"Six kit-owned core items"* — not the floor sentence at `:150-151`, which carries no number. 6 → 8. | D10 |
| 2e | Protocol §10 names **zero handles**. It carries the MECHANISM only — kit-owned, waivable at preflight with a reason, recorded as a parked entry, never a DoD override, never removing a gate — and one sentence pointing at the rendered Skill's table as the handle list. The per-handle checkability classification moves into the SPEC, where an argued-once classification belongs. Zero handles in the contract means zero to keep in step across three spellings. | D5 |
| 2f | `parallel-coding-governance.domain-rules.md:25` gains *"the default directive set and its named waiver"* to its enumeration. It is written as a complete list and reads as one. | C13 |
| 2g | M9's `open / parked` row: *"…plus any recorded DoD override **or directive waiver**."* A waiver entry carries a reason and no question or options — which is exactly why the `override` kind needed its own trailing clause. | C7 |
| 2h | The classification table labels `build-complete` **internal consistency over run-written status tokens**, not `machine`. Its inputs are spec status headers routed through a region the run re-renders; the honest limit goes in the source comment beside the branch, matching `check-unattended.sh:328-332`'s precedent. | FG-12 |
| 2i | Three gloss cells are rewritten to NAME rather than STATE: `parallel-when-disjoint` → "the parallelism default under a mandate"; `land-once-done` → "when a build may land"; `conflicts-reconciled` → "merge-conflict disposition". A gloss stating a condition, threshold or procedure is a defect by M1, and three shipped as written. | D11 (first half) |
| 2j | `memory/project/method-carriers.txt` gains a row in whichever unit introduces the literal: `tools/unattended/check-unattended.sh · check 16 arm B resolves each cited M-section in the method`, and `tools/unattended/PROTOCOL.template.md · §10 names the method as the directive layer's carrier` (the live twin is excluded by the `memory/*` rule; the shipped one is not). The leg's population is every tracked non-`memory/`, non-`*.test.sh` file containing the literal — verified at `check-method-carriers.sh:52-62`. | D4 |
| 2k | The driver comment at `:909` says the authored region carries **five** facts against the protocol's **seven**. One-word edit, in the unit that opens §2 anyway. | D12, FG-14 |
| 2l | `tools/check-kit-versions.sh` gains the shipped-marker pairing (a derived `git ls-files 'tools/unattended/*.template.md'` glob, copying the memory-tree shape). Verified: it pairs the two SCRIPT constants only, and check 10 compares SHIP against LIVEDOC — both docs, so a stale marker in both compares equal. This is OPEN row `TOOL-cFinalBerth-3`, and the 1.4→1.5 bump is exactly the edit that reproduces it. | D6 |
| 2m | Every unit's write set names its sibling test file, and the fixture changes land in the SAME commit as the branches they arm. `harness arms` is **unguarded** in `gate-legs.json` (verified), so an unarmed branch reds on its own commit. | DEC-3 |

---

## 3. What the build now looks like, end to end

```
/unattended <slug> --waive parallel-when-disjoint,land-once-done
  │
  ├─ SKILL step 0 · read {{MEMORY_ROOT}}/guides/BUILD-METHOD.md WHOLE (no longer conditional)
  ├─ SKILL step A · THE LAST OWNER TURN. One AskUserQuestion batching the named handles.
  │    DEFAULT-DENY: a handle named but not confirmed WITH A REASON is not waived.
  ├─ SKILL step B · schedule the keepalive
  ├─ SKILL step C · preflight, carrying the confirmed pairs:
  │      --preflight <slug> --keepalive-id <id> \
  │        --waive parallel-when-disjoint --reason "…" --waive land-once-done --reason "…"
  │    validation in the precondition block (writes nothing on refusal, :828-830)
  │    park() AFTER the set_fact block, BEFORE stage_or_fail — so the staged blob carries it (C9)
  ├─ SKILL step D · if this project ships /session-kickoff, invoke it — AFTER preflight, never before
  └─ from here M10 binds: never ask.
```

At close, a waived `land-once-done` still owes `--override build-complete --reason "…"`; `fail 13`
prints that exact spelling, and the Skill's table carried it forward at invocation. Two waived
DoD-mapped handles now close in one invocation, because `--override` accumulates.

---

## 4. The unit decomposition — M2 applied

Slug `cBriefedPilot`. **This build has no valid parallel pair** and every unit is sequenced. That is
the honest outcome of M6's own conditions: `TOOL-cBriefedPilot-19` writes `memory/backlog/TOOL.md`,
named verbatim in condition (3); and any two units that close a spec both re-render
`memory/LIVE.md` and the build README's `<!-- gen:build-index -->` region — a generated index with its
generator, also condition (3) — and both touch the run-state file. *(DEC-8)*

The ordering constraint that dominates: **`unattended kit gate`, `harness arms`, `method carriers`,
`kit version markers` and `unattended skill wiring` carry NO `guard` in `tools/gate-legs.json`**, so
they run on every commit's diff-scoped bar. Nothing may land in a state a later unit repairs.

| # | id | title | tier | mechanism | depends on |
|---|---|---|---|---|---|
| 1 | `TOOL-cBriefedPilot-1` | The paired flag accumulator; `--override` repeats | 1 | one accumulator parses repeated `<flag> <value> --reason <text>` pairs; `--close` skips and parks every named item | — |
| 2 | `TOOL-cBriefedPilot-2` | The directive registry constant | 1 | a kit-owned `DIRECTIVES_CORE` of eleven `handle:M<n>` pointers, readable by `core_of()` | — |
| 3 | `TOOL-cBriefedPilot-3` | `--waive` at preflight | 2 | the owner's named, reasoned waiver reaches the record, validated and parked | 1, 2 |
| 4 | `TOOL-cBriefedPilot-4` | Preflight refuses an absent build method | 1 | `--preflight` refuses when `$M/guides/BUILD-METHOD.md` does not exist | — |
| 5 | `TOOL-cBriefedPilot-5` | The BASE is pinned once | 1 | `--preflight` writes `base:` only when the record carries none | — |
| 6 | `TOOL-cBriefedPilot-6` | `--plan` sees an unspecced planned unit | 2 | the roster region's ids, joined against tracked specs, reported as `MISSING` | — |
| 7 | `TOOL-cBriefedPilot-7` | `build-complete` | 2 | `--close` blocks while the build is incomplete against its authored roster | 1, 6 |
| 8 | `TOOL-cBriefedPilot-8` | `closing-review-recorded` | 2 | `--close` blocks until a tracked review record names the pinned BASE | 1, 5 |
| 9 | `TOOL-cBriefedPilot-9` | The Skill's directive table and hard step 0 | 1 | the rendered Skill carries the eleven directives and the mandatory method read | 2 |
| 10 | `TOOL-cBriefedPilot-10` | The Skill's waiver turn | 1 | the last owner turn: one `AskUserQuestion`, default-deny, reason required | 9 |
| 11 | `TOOL-cBriefedPilot-11` | The Skill's kickoff step and roster read | 1 | `/session-kickoff` after preflight, conditional on the project shipping it; the README is the roster | 10 |
| 12 | `TOOL-cBriefedPilot-12` | Leg check 16 — the registry join | 2 | the bar joins the driver constant to the Skill's table and resolves every cited M-section | 2, 9 |
| 13 | `TOOL-cBriefedPilot-13` | Leg check 17 — the waiver record | 1 | the bar grades every parked `waiver ·` line for a declared handle and a non-empty reason | 3, 12 |
| 14 | `TOOL-cBriefedPilot-14` | Leg check 18 — the kickoff road, in order | 1 | the bar asserts the Skill names the kickoff invocation AFTER the preflight one | 11 |
| 15 | `TOOL-cBriefedPilot-15` | M6's parallelism inversion | 2 | under a mandate, disjoint passes are OWED concurrency, bounded by the mechanism clause | — |
| 16 | `TOOL-cBriefedPilot-16` | The method's pointers name the new layer | 1 | M8's landing pointer, M9's parked row, M10's delta index and waiver bullet | 15 |
| 17 | `TOOL-cBriefedPilot-17` | `check-kit-versions` pairs the shipped protocol marker | 1 | a partial version bump reds the bar | — |
| 18 | `TOOL-cBriefedPilot-18` | The protocol pair and the domain rules | 2 | the binding contract describes the directive layer, the waiver, DELTA 3 and the two DoD items | 3, 7, 8, 13, 16 |
| 19 | `TOOL-cBriefedPilot-19` | Version 1.5 | 1 | the kit identifies as the version it now is | 17, 18 |
| 20 | `TOOL-cBriefedPilot-20` | Records | 1 | the dossiers, the closed rows and the measurement that is not this build's | all |

### Per-unit detail

**1 · `TOOL-cBriefedPilot-1` — the paired flag accumulator; `--override` repeats** · Tier 1
- Files: `tools/unattended/unattended.sh` (dispatch `:1005-1006`, `verb_close` `:916/:940/:951`),
  `tools/unattended/unattended.test.sh`
- Acceptance: two `--override a --reason x --override b --reason y` pairs both skip and both write a
  `park` entry · every pre-existing single-override arm stays green · `--override
  authorization-reachable` refuses when it is SECOND in the list · an `--override` with no following
  `--reason` refuses
- Gates: `unattended driver selftest` · `harness arms` · `unattended kit gate` · full bar
- Lands first because §1a's accumulator is what §3 reuses, and because nothing else may ship a
  reachable dead end at `--close`.

**2 · `TOOL-cBriefedPilot-2` — the directive registry constant** · Tier 1
- Files: `tools/unattended/unattended.sh` (the constant + `directives()` + **`DIRECTIVES_EXTRA` in the
  default-init line at `:60-61`** + the one-line `verb_resume` pointer), `.unattended.conf`
  (`DIRECTIVES_EXTRA=""`), `tools/unattended/unattended.test.sh`
- Acceptance: a conf that does NOT declare `DIRECTIVES_EXTRA` runs `--status` with no
  `unbound variable` · `--resume` on a live fixture prints the one-line pointer · a **source-level
  arm** asserts every conf key the driver reads appears in its own default-init line, and that arm was
  observed RED with `DIRECTIVES_EXTRA` removed from `:60-61` *(D8 — the two init lists at
  `unattended.sh:60-61` and `check-unattended.sh:47-49` already disagree and nothing pairs them; the
  arm catches the CLASS, not this instance)*
- Gates: `unattended driver selftest` · `unattended kit gate` · `harness arms`
- No new `fail` branch (`print_directives()` is deleted, §1h; the carrier refusal is unit 4).

**3 · `TOOL-cBriefedPilot-3` — `--waive` at preflight** · Tier 2
- Files: `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`
- Mechanism detail: five refusals — on a verb other than `--preflight`; an undeclared handle; a
  missing `--reason`; a reason spelling `$BYPASS_BAN` (`verb_abort:771`'s mirror — `park()` writes it
  verbatim and leg check 11 greps the file whole, so a truthful reason would red the bar permanently
  on a record no verb rewrites); a reason containing a newline. Validation sits in the precondition
  block ABOVE the write barrier at `:830`; `park()` is called AFTER the `set_fact` block and BEFORE
  `stage_or_fail` at `:862` *(C9 — `park()` is `>>`, which CREATES the file, and called before the
  scaffold guard at `:834` it makes `splice` fail with a message naming the wrong cause)*
- Acceptance: five refusals each armed and observed RED, each leaving the run-state file byte-identical
  · a waived run's RUN.md carries one `waiver · item <h> · reason <r>` line per pair, in the staged blob
  · a byte-identical re-preflight leaves the parked region diff-equal · a DIFFERING re-preflight refuses
  and changes nothing · a multi-line reason is refused (`--reason $'a\nb waiver · item …'` injects no
  second line)
- Gates: `unattended driver selftest` · `harness arms` · `unattended kit gate`
- Depends: 1 (the accumulator), 2 (handle membership)

**4 · `TOOL-cBriefedPilot-4` — preflight refuses an absent build method** · Tier 1
- Files: `tools/unattended/unattended.sh` (one branch in the precondition block),
  `tools/unattended/unattended.test.sh` (**the fixture gains `memory/guides/BUILD-METHOD.md`**)
- Acceptance: a fixture without the carrier prints the refusal and leaves NO run-state file · the green
  control preflights OK · all 64 existing `--preflight` arms stay green
- Gates: `unattended driver selftest` · `harness arms`
- **Isolated deliberately** *(DEC-4)*: the driver self-test creates no `memory/guides/` and drives
  `--preflight` 64 times (measured). A refusal writes nothing (`:830`), so every downstream arm
  collapses with it. The fixture change and the branch are one commit or the leg — guarded on
  `tools/unattended/`, which this unit writes — reds on its own diff.

**5 · `TOOL-cBriefedPilot-5` — the BASE is pinned once** · Tier 1
- Files: `tools/unattended/unattended.sh` (`:852`), `tools/unattended/unattended.test.sh`
- Acceptance: a second `--preflight` after the anchor advanced leaves `base:` byte-identical · the
  first preflight still writes it · leg check 9 stays green on the fixture · the preflight echo reports
  the RECORDED base, not the freshly derived one

**6 · `TOOL-cBriefedPilot-6` — `--plan` sees an unspecced planned unit** · Tier 2
- Files: `tools/unattended/unattended.sh` (`roster_ids()`, `missing_units()`, the
  `nonterminal_units()` extraction out of `verb_status:892`, `verb_plan` wiring, **the roster caveat
  appended to the `roster:` output line at `:648`**), `tools/unattended/unattended.test.sh`
- Acceptance: a README with a roster naming two ids and one spec prints exactly one `MISSING` row ·
  no roster pair prints today's output plus its caveat · a malformed pair is a NAMED refusal, never
  silence (`region` exits 3 for absent AND malformed — the discarded-signal class `:487-493` records)
  · `--status`'s next-unit line is byte-identical before and after the extraction
- Gates: `unattended driver selftest` · `harness arms`
- Sequenced before 7 *(DEC-2)*: shipping `build-complete` first would ship a conjunct that is inert for
  every build with at least one spec, and an acceptance criterion that cannot exercise it.

**7 · `TOOL-cBriefedPilot-7` — `build-complete`** · Tier 2
- Files: `tools/unattended/unattended.sh` (`DOD_CORE` += `build-complete:machine`, the `dod_met`
  branch), `.unattended.conf` (`CORE_FLOOR` `10:6` → `10:7`), `tools/unattended/unattended.test.sh`,
  `memory/builds/cBriefedPilot/README.md` (this build's own roster markers)
- Acceptance: a fixture with one OPEN unit blocks `--close` naming `build-complete` · all-terminal
  passes · **no roster pair blocks** · a roster id with no spec blocks · **an EMPTY generated region
  blocks** (`region` returns exit 0 with empty stdout for a well-formed pair enclosing nothing —
  `:105-113`) · `--override build-complete --reason x` closes and parks · `verb_plan`'s stdout is
  grepped nowhere
- Gates: `unattended driver selftest` · `unattended kit gate` (the `CORE_FLOOR` pin) · `harness arms`
- Depends: 1, 6

**8 · `TOOL-cBriefedPilot-8` — `closing-review-recorded`** · Tier 2
- Files: `tools/unattended/unattended.sh` (`DOD_CORE` += `closing-review-recorded:machine`, the
  `dod_met` branch), `.unattended.conf` (`CORE_FLOOR` `10:7` → `10:8`),
  `tools/workflows/tier2-review.js` (one clause in the synth write instruction, `:307`),
  `tools/unattended/unattended.test.sh`
- Acceptance: a fixture with an empty `reviews/` blocks · a review naming the pinned BASE's 8-char
  prefix passes · an UNTRACKED review naming it does NOT pass · a review naming a DIFFERENT sha does
  not pass · a report written by `tier2-review.js` with `base` set contains the range line ·
  `bash tools/workflows/check-workflow-syntax.js` and `check-review-join.sh` stay green
- Gates: `unattended driver selftest` · `unattended kit gate` · `review-harness gates` · `harness arms`
- Depends: 1, 5

**9 · `TOOL-cBriefedPilot-9` — the Skill's directive table and hard step 0** · Tier 1
- Files: `tools/unattended/SKILL.template.md`, re-rendered `.claude/skills/unattended/SKILL.md`
- Acceptance: one table row per `DIRECTIVES_CORE` member, handle and M-section matching · the fifth
  column names the owed override for `land-once-done` and `diff-reviewed` and is blank for the other
  nine · every gloss cell NAMES rather than states · step 0 carries no conditional ·
  `bash tools/unattended/adopt-unattended.sh --check` exits 0 ·
  `git ls-files --eol .claude/skills/unattended/SKILL.md` reports `w/lf` — **F6 closes as a side
  effect**, because `adopt-unattended.sh`'s `render()` strips `\r` and the re-render performs it *(DEC-9;
  the converged design listed CRLF both as a U6 item and as "not a unit")*
- Gates: `unattended skill wiring` · `method carriers` · full bar
- Depends: 2

**10 · `TOOL-cBriefedPilot-10` — the Skill's waiver turn** · Tier 1
- Files: `tools/unattended/SKILL.template.md`, re-render
- Acceptance: one `AskUserQuestion`, default-deny stated, reason required stated, and the sentence
  *"this is the LAST owner turn; from the next command onward there is nobody to answer, and every
  question you have left is a park"* · the turn precedes the keepalive and the preflight in the
  document · adopt `--check` exits 0
- Depends: 9 (same file)

**11 · `TOOL-cBriefedPilot-11` — the Skill's kickoff step and roster read** · Tier 1
- Files: `tools/unattended/SKILL.template.md`, re-render
- Acceptance: the `/session-kickoff` mention's line number is GREATER than the `--preflight`
  invocation's · the step is conditional prose on the project shipping the skill · the roster sentence
  *"its authored Units table is the ROSTER (M2)"* is present · adopt `--check` exits 0
- Depends: 10

**12 · `TOOL-cBriefedPilot-12` — leg check 16, the registry join** · Tier 2
- Files: `tools/unattended/check-unattended.sh` (**`DIRECTIVES_EXTRA` and `DIRECTIVES_FLOOR` in the
  default-init at `:47-49`**, header `FIFTEEN` → `EIGHTEEN`), `.unattended.conf`
  (`DIRECTIVES_FLOOR="11"`), `tools/unattended/check-unattended.test.sh` (**`cp "$HERE/SKILL.template.md"`
  into the fixture kit dir; `mkconf` emits `DIRECTIVES_FLOOR` derived from the driver the way
  `CORE_FLOOR_DERIVED` is at `:79-81`**), `memory/project/method-carriers.txt`
- Mechanism detail: arm A joins the table's rows to `DIRECTIVES_CORE` **both directions**, always. Arm
  B resolves every cited `M<n>` against `^## M<n>` in `$M/guides/BUILD-METHOD.md`, SILENT when the
  carrier is absent — the leg grades the tree, the driver grades the run (unit 4). Arm C:
  `DIRECTIVES_FLOOR` declared and numeric, member count ≥ floor; undeclared is a refusal exactly as
  `CORE_FLOOR` is. A missing `SKILL.template.md` is a NAMED refusal, not a skip — a shipped kit always
  has one.
- Acceptance: the fixture's GREEN CONTROL still exits 0 and prints nothing *(DEC-5 — verified: the
  fixture copies only `check-unattended.sh`, `unattended.sh` and `PROTOCOL.template.md`, and `mkconf`
  writes no `DIRECTIVES_FLOOR`, so both arms fire on a conforming tree unless the fixture moves in this
  commit)* · a row added to the table alone reds · a constant edited alone reds · a cited `M<n>` with
  no `^## M<n>` reds · an undeclared floor reds · an absent template reds
- Gates: `unattended gate selftest` · `unattended kit gate` · `method carriers` · `harness arms`
- Depends: **2 AND 9.** *(DEC-1 — arm A joins both directions and `unattended kit gate` has no guard,
  so landing the join before the table reds every commit until the table exists.)*

**13 · `TOOL-cBriefedPilot-13` — leg check 17, the waiver record** · Tier 1
- Files: `tools/unattended/check-unattended.sh` (inside the existing per-run-state-file loop),
  `tools/unattended/check-unattended.test.sh`
- Acceptance: a parked `waiver ·` line naming an undeclared handle reds · one with an empty reason
  reds · a conforming pair is silent · the green control stays green · the honest limit is in the
  source comment beside the branch, matching check 13's (`:328-332`): both the line and the file are
  written by the run, so this is internal consistency, not an authorization verdict
- Depends: 3, 12

**14 · `TOOL-cBriefedPilot-14` — leg check 18, the kickoff road in order** · Tier 1
- Files: `tools/unattended/check-unattended.sh`, `tools/unattended/check-unattended.test.sh`
- Acceptance: `KICKOFF_ENGINE` non-blank ⇒ the template names the kickoff invocation AND its line
  number exceeds the `--preflight` invocation's · a fixture with the two transposed reds · blank
  `KICKOFF_ENGINE` is silent
- Depends: 11

**15 · `TOOL-cBriefedPilot-15` — M6's parallelism inversion** · Tier 2
- Files: `tools/memory-tree/BUILD-METHOD.template.md`, re-rendered `memory/guides/BUILD-METHOD.md`
  (never hand-edited — `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`)
- Acceptance: M6's replaced sentence is §1f's, in place · the three conditions, the write-set rule and
  the fallback are byte-unchanged · `memory/` hygiene rule 6 (≤250 lines, ≤20 KB) green ·
  `kit/dogfood doc parity` green · `method carriers` green
- Gates: `memory hygiene` · `kit-dogfood parity` · `method carriers` · full bar

**16 · `TOOL-cBriefedPilot-16` — the method's pointers name the new layer** · Tier 1
- Files: `tools/memory-tree/BUILD-METHOD.template.md`, re-render
- Mechanism detail: M8's landing pointer gains *"when a build may land"*; M9's parked row gains *"or
  directive waiver"*; M10's index moves to three deltas, gains the parallelism pointer bullet and the
  waiver pointer bullet (§1g). **No M8 review-record edit** — §1e deleted it, which is also C5's fix.
- Acceptance: 6 net lines added against 14 of measured headroom · rule 6 green · no rule stated that
  also appears in an M11 carrier · `kit/dogfood parity` green
- Depends: 15 (same file)

**17 · `TOOL-cBriefedPilot-17` — `check-kit-versions` pairs the shipped protocol marker** · Tier 1
- Files: `tools/check-kit-versions.sh`
- Acceptance: editing `tools/unattended/PROTOCOL.template.md`'s marker to `@1.3` in a scratch copy
  reds `bash tools/check-kit-versions.sh` naming the file · the clean tree exits 0 · the glob is
  DERIVED (`git ls-files 'tools/unattended/*.template.md'`), not a hardcoded path
- Closes `TOOL-cFinalBerth-3` (OPEN). Lands BEFORE 19 so the bump cannot reproduce the row it closes.

**18 · `TOOL-cBriefedPilot-18` — the protocol pair and the domain rules** · Tier 2
- Files: `tools/unattended/PROTOCOL.template.md`, `memory/guides/UNATTENDED-PROTOCOL.md` (both in ONE
  commit or check 10 reds), `parallel-coding-governance.domain-rules.md`,
  `memory/project/method-carriers.txt`, `tools/unattended/unattended.sh` (the `:909` count comment)
- Mechanism detail: §1 (2a + the run-time build-method dependency), §2 fact 3 (2b), §2 spill rule (2c),
  §4's two rows and line 138's count (2d), §6's DELTA-3 sentence, §7's `--waive`, §8's two keys, new
  §10 (2e), domain-rules (2f)
- Acceptance: `unattended kit gate` check 10 green (the pair is byte-equal after prefix substitution) ·
  §10 names zero handles · §2 enumerates four parked kinds · `bash tools/run-gates.sh` green
- Depends: 3, 7, 8, 13, 16 — **the contract publishes only once what it describes exists** *(DEC-6)*

**19 · `TOOL-cBriefedPilot-19` — version 1.5** · Tier 1
- Files: `tools/unattended/unattended.sh:32`, `tools/unattended/check-unattended.sh:17`,
  `tools/unattended/PROTOCOL.template.md:1`, `memory/guides/UNATTENDED-PROTOCOL.md:1`
- Acceptance: all four literals read `1.5` · `bash tools/check-kit-versions.sh` green · omitting any
  one of the four reds it (observed)
- Depends: 17, 18

**20 · `TOOL-cBriefedPilot-20` — records** · Tier 1
- Files: `memory/map/features/unattended.md`, `memory/map/features/build-method.md`,
  `memory/backlog/TOOL.md`, `memory/DECISIONS.md`, `memory/builds/cBriefedPilot/`
- Mechanism detail: `TOOL-aStandingWrit-3` → CLOSED (F5 — the instruction layer is now owned);
  `TOOL-cFinalBerth-3` → CLOSED (unit 17); the F4 read-budget measurement filed as a NEW row with its
  number (the FIXED read path gates at 68,889 B against `READ_PATH_CEILING` 86,476; the RECURRING one
  is counted by nothing) — **measured, not built** (M3 veto 2 plus YAGNI)
- Acceptance: `python tools/codebase-map/test_codebase_map.py` green (every new moving part claimed by
  a dossier) · `memory/` hygiene green · `drift-audit records` green

---

## 5. PARKS — the owner's questions

**P1 · Tamper evidence over waivers.** *(FG-2, HIGH)* Check 17 as specified grades only the SHAPE of a
waiver line, and W1's ordering guarantee lives entirely inside a driver that is not the only writer of
`RUN.md` (`park()` is a bare `>>`). A run can append a well-formed waiver at pass 4 and check 17 accepts
it. FG-2's fix is a git join — the worktree's `waiver ·` lines must be present in the FIRST committed
blob of `RUN.md` — roughly five lines using the kit's own read-a-blob idiom, plus a committing fixture.
**Parked rather than folded** because protocol §9 explicitly disclaims exactly this property ("nothing a
script running under the run's own uid constitutes authorization"), and §9's *what actually binds* is
the same leg re-run in a clone the run never touched — where the join WOULD bind. Folding it silently
widens a boundary the contract narrows on purpose. **Owner question: buy it?**

**P2 · D6 has no mechanism that keeps the directive layer in force on a concurrent BUILD pass.**
*(C6, HIGH)* Direct `Agent` spawns are capped per PROMPT TURN and an unattended run has no next prompt
to reset the budget (M4 says so in its own words); a `Workflow` sidechain inherits no hooks and no
`CLAUDE.md` (`REVIEW-PROTOCOL.md:168-170`), so passes dispatched there would execute outside the eleven
directives this build installs. The inversion ships as the owner asked, bounded by §1f's clause — which
today means it bites on review fan-out and sequences build passes. **Owner question: accept that, or
scope a mechanism as a follow-up build?**

**P3 · `build-complete` makes `<!-- roster:units -->` mandatory for every unattended build.** One of
25 build READMEs carries the pair today. Without the requirement the roster conjunct is vacuous for the
other 24 and the check cannot see the case D8 exists for. **Owner question: accept the two-line
authoring obligation per build?**

**P4 · Waiving `reuse-first` reds the FULL bar at the push boundary with nobody to interpret it.**
`TEMPLATE-SPEC` §10 is machine-enforced by hygiene check 12 for every spec past `SPEC10_CUTOFF`, and a
waiver removes the directive, never the gate. It is the one handle whose waiver is dangerous rather
than merely costly. **Owner question: mark it "recommend against" in the Skill's table, or have the
driver refuse that one handle?** (Refusing contradicts "all eight overridable", so it is not folded.)

**P5 · Protocol §3's phase list and §4's DoD table are joined to `PHASES_CORE`/`DOD_CORE` by nothing.**
Pre-existing; this build adds two rows to a table no leg reads. Check 16 arm A's shape would extend to
it. **Owner question: in scope, or a backlog row?**

---

## 6. RESIDUAL RISKS

1. **`closing-review-recorded` measures that a tracked review under this build names the run's pinned
   BASE — not that it was adversarial, nor that it reviewed the diff.** An M4 per-spec review written
   this run that cites the base satisfies it. The join to a value pinned once and written by the
   harness is what keeps it from being satisfied by any pre-existing record; beyond that it is a
   construction cost, and §9 already says why nothing here is a proof.
2. **A `BLOCKED` closing review satisfies it.** Anchoring the verdict value was rejected (§7). The
   landed-with-a-blocker path is covered instead by `build-complete`, which rests on M8's "a blocker
   unfixable inside the mandate's scope is a park … and its unit does not close" being honoured —
   the same honesty premise every attested item rests on. Watch the first two runs.
3. **Pointer-not-copy is machine-held on the `(handle, M-section)` PAIRS and authorial on the gloss
   column.** Arm A pins the pairs and `check-method-carriers.sh` catches a copied `## M<n>` heading;
   neither can see a gloss growing from "the parallelism default under a mandate" into a restatement
   of M6's three conditions. Three cells shipped in the converged design already did this (§2i). The
   only control is the review lens. A byte cap was refused: a budget permits a compressed rule.
4. **Kickoff-after-preflight is a sequence nobody has executed.** Check 18 asserts the ORDER of two
   lines in a template, not that the sequence works. Preflight stages `RUN.md`, so kickoff Step 1 meets
   a tree dirty by its own reporting; its STOP conditions (foreign `MERGE_HEAD`, `UU`) do not cover
   that and *should* pass — the word that precedes every reproduced bypass in this kit's history. It
   needs one real run before it is believed.
5. **Every waiver record and every DoD verdict is written and read under the run's own uid.** Protocol
   §9's boundary is unchanged by this build, and P1 is the only thing that would move it.
6. **`minimal-prose` and `parallel-when-disjoint` are observed by nothing**, and the classification
   table says so rather than adding an attestation line the run ticks for itself.
7. **`build-complete` reads spec status tokens the run writes**, routed through a region the run
   re-renders. Flipping one `OPEN` to `CLOSED` per unspecced unit satisfies it end to end. It is worth
   having because it forces an explicit per-unit lie instead of silence — and it is labelled as
   internal consistency, not `machine` (§2h).

---

## 7. REJECTED, on evidence

**C12 — "anchor `closing-review-recorded` to `^## Verdict: (CLEAN|CLEAN WITH FIXES)`".** The CLAIM is
real (a `BLOCKED` review satisfies a presence check). The FIX is rejected: measured over this corpus,
`^## Verdict:` matches 6 files and their verdict values are `BLOCKED` ×5 and `CHANGES REQUESTED` ×1 —
**zero records carry `## Verdict: CLEAN`**, and 9 more carry a bare `## Verdict` with no colon at all.
The proposed anchor would make the item unsatisfiable against every record this repo has ever written,
reproducing FG-1, the blocker it sits beside. §1e drops content grammar from the check entirely; the
residual is risk 2.

**C6's FIX — "bound the obligation to a `Workflow` fan-out".** Rejected on the finding's own evidence:
`REVIEW-PROTOCOL.md:168-170` states a `Workflow` sidechain inherits no hooks and no `CLAUDE.md`, so
routing build passes there is precisely the harm C6 names — the eleven directives would bind none of
the agents writing the code. Both available routes fail; the claim is folded as §1f's mechanism clause
and the residual is parked as P2, not resolved by picking the route that voids the layer.

**D11's second half — "point `land-once-done:M8` at a carrier that actually states the rule".**
Rejected: M8's landing sentence names TWO carriers — *"template §1 Landing and
`memory/guides/UNATTENDED-PROTOCOL.md`"* — and the protocol's §4 `build-complete` row states the rule
once unit 18 lands. A pointer whose second carrier states the rule is a live pointer, and duplicating
it into template §1 would be the M1 defect the finding is arguing against. D11's gloss-cell half is
FOLDED (§2i).

**C10's premise that arm B's silence depended on the standalone-install argument.** The contradiction
C10 names is real and folded (§1j), but arm B keeps its disposition for an independent reason stated in
the leg's own split: *the leg grades the TREE, the driver grades the RUN.* Dropping the standalone
argument does not disturb it.
