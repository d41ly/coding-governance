**Serves:** research TOOL-dScriptedRepeat-1

# Extension seams — every place a THIRD mode must plug in

**Lens 3 of the dScriptedRepeat design pass.** Node `d` · 2026-08-20 · kind `research`.
Measured against the worktree at
`C:/projects/coding-governance/.claude/worktrees/playbook-mode-unattended-kit-550410`, HEAD `d2a40aa`,
kit `unattended@1.7`. Every figure below was derived by running the command shown or reading the cited
`file:line`; anything reasoned rather than run is marked **(inference)**.

---

## 0. Headline — the five things that will break, in severity order

| # | Finding | Class | Evidence |
|---|---|---|---|
| **F1** | The leg's directive **scope-cell extractor hard-codes `all\|prompt`** and silently drops any third value, so check 16 reds on a *correct* playbook-mode implementation. | repeat of the exact defect `aPromptedMandate-4` was blocked on | `check-unattended.sh:711` · reproduced in §3.3 |
| **F2** | `check_waiver_scope` hard-codes `prompt` on both sides, so a **`playbook`-scoped directive is waivable on every run**, including a slug run. The refusal is vacuous the moment a third scope exists. | check-that-cannot-fail | `unattended.sh:661` · reproduced in §2.4 |
| **F3** | `build-complete` **cannot count pieces and cannot be extended to**, and the `DOD_CORE` entry grammar has **no third field**, so a mode-scoped DoD item is not expressible today. | mode set assumed binary | `unattended.sh:93,134,1746-1801` |
| **F4** | The **memory read path has 6 699 B of margin** and the *second* mode consumed **5 609 B** of it. A third mode of the same size leaves ≈ 1 090 B. | budget | `corpus_ids.py --report` · `.memory-tree.conf:113` |
| **F5** | **`BUILD-METHOD.md` is 20 567 B / 283 lines against a stated ≤22 KB / ≤290 lines that NOTHING gates.** M12 cost 34 lines. An M13 the same size overruns by 27, and raising the budget is an **owner turn** (M3 veto 2), as it was for `TOOL-aPromptedMandate-3`. | ungated prose budget | `BUILD-METHOD.md:8-11`; grep for `290` under `tools/` returns **0 hits** |

Plus one that is not a seam but will cost a re-mint: **the word `playbook` is already taken** —
`tools/playbook/` (the charter renderer), `memory/map/features/playbook.md`,
`tools/check-playbook-parity.sh`, `tools/govkit/entries/playbook.kit.toml`, and the `DISCIPLINES` /
`streams` enum whose **first member is literally `playbook`** (`.memory-tree.conf:11`). See §9.1.

---

## 1. The precedent, measured — what adding the SECOND mode actually cost

`TOOL-aPromptedMandate` is the worked example. Its mode-addition commits, in order:

```
5abd9c9  TOOL-aPromptedMandate-1: the prompt-mode declaration, and where it is carried
4cb6581  TOOL-aPromptedMandate-1: state check 19's shared-parse residual at the site
b0b2b4e  TOOL-aPromptedMandate-2: the RESEARCHING and TESTING phases
8826eb2  TOOL-aPromptedMandate-4: the two mode-scoped directives
3038c5b  TOOL-aPromptedMandate-5: the Skill's prompt start path
14ac45e  TOOL-aPromptedMandate-6: the driver-then-leg cross-component leg
```

(`b64129d` built M12 in the memory-tree kit; `8c4edf3` fixed `build-complete` and the canary — a
separate defect stream, not mode plumbing.)

### 1a. Byte cost, per file

`git show 6517579f:<path> | wc -c` against `git show 14ac45e:<path> | wc -c`:

| File | base `6517579f` | after the mode `14ac45e` | delta |
|---|---|---|---|
| `tools/unattended/unattended.sh` | 109 596 | 115 077 | **+5 481** |
| `tools/unattended/check-unattended.sh` | 51 557 | 60 877 | **+9 320** |
| `tools/unattended/SKILL.template.md` | 12 856 | 17 749 | **+4 893** |
| `tools/unattended/PROTOCOL.template.md` | 27 582 | 30 583 | **+3 001** |
| `tools/unattended/unattended.test.sh` | 108 812 | 114 471 | **+5 659** |
| `tools/unattended/check-unattended.test.sh` | 64 259 | 72 958 | **+8 699** |
| `tools/unattended/.unattended.conf.example` | 4 558 | 4 983 | +425 |
| `tools/unattended/kit.toml` | 4 531 | 4 649 | +118 |
| `tools/unattended/cross-component.test.sh` | — | 8 986 (new file) | **+8 986** |
| **total** | | | **+46 582 B** |

Outside the kit: `memory/guides/UNATTENDED-PROTOCOL.md` +3 001 (the byte-identical twin) and
`memory/guides/BUILD-METHOD.md` 17 460 → 20 068 (**+2 608 B / +34 lines**).

### 1b. Arm cost, from the shrink-only floors

`git show <sha>:<path> | grep -m1 '^FLOOR_ASSERTIONS='`:

| commit | driver suite | leg suite | cross-component |
|---|---|---|---|
| `b9ebeba` (spec set) | 296 | 162 | — |
| `5abd9c9` (mode bit) | 305 | 162 | — |
| `b0b2b4e` (phases) | 307 | 174 | — |
| `8826eb2` (directives) | 315 | 182 | — |
| `3038c5b` (Skill path) | 315 | 194 | — |
| `14ac45e` (cross-component) | 315 | 194 | 13 |

**The second mode cost +19 driver assertions, +32 leg assertions, and a new 13-assertion leg — 64
executed assertions.** Today's floors are 338 / 200 / 13.

### 1c. What the precedent got WRONG — the defect CLASSES

Two review records. The M4 **spec audit returned BLOCKED**: 49 raw, **26 confirmed / 23 refuted,
precision 0.53**, seventeen distinct sites. The closing Tier-2 diff review returned **0 blockers /
2 high**: 17 raw / 12 confirmed / 5 refuted, precision 0.71. The recurring classes:

**C1 — "one more arm on an existing parse" is usually unimplementable.** The mode reader was specced
as one extra `awk` arm. The existing program was `/^slug:/ { …; print; exit }` and every README orders
`slug:` first, so an arm below it could never run and an arm above it starved `fmslug`, tripping
`fail 20`. The fix changed the parse SHAPE — key-tagged output, no `exit`, front-matter close as the
terminator (`unattended.sh:783-790`). *Wherever a third mode says "just add a value", check whether
the existing reader is a first-match reader.*

**C2 — a widened grammar breaks every consumer that assumed the narrow one, and the spec's
enumeration of consumers was wrong in BOTH directions.** Unit 4's §4 named two consumers; the
`--waive` membership test (a prefix match) needed **no** change, and the LEG needed **three** edits.
Fed three-field entries, leg arms A and B produced **four refusals over a correct implementation**.
The fold was ONE splitter (`scope_of`, `unattended.sh:123-132`). **F1 and F2 are this class,
repeating.**

**C3 — a check whose ordering was never specified is unsatisfiable in one spelling and vacuous in the
other.** `check_waiver_scope` needs `AUTH_MODE`; `check_waivers` runs **before** the authorization
read. Keyed on "mode is slug" it never fires; keyed on "mode is not prompt" it fires on prompt runs
too. Resolved by a second call site after the authorization block (`unattended.sh:1394-1402`), keyed
on *not prompt* so an **underivable** mode fails closed.

**C4 — the ACs pass over a dead implementation.** AC1 ("key present → `mode: prompt`") and AC2 ("key
absent → `mode: slug`") are BOTH satisfied by an awk that returns nothing. The audit added **AC2b**:
the key ordered *after* `slug:` — the only arm that discriminates a working reader from a dead one.
The shipped fixtures do exactly that (`unattended.test.sh:114-121`,
`mutate memory/builds/tModeOk/README.md '/^slug: tModeOk$/a authorized-by: prompt'`).

**C5 — a precondition measured and understood, then not carried into the artifacts an adopter
receives.** `ANCHOR_SCOPE="published"` appeared in **none of the six specs**. The path shipped in a
kit template whose example conf declares `ANCHOR_SCOPE=""`, so every adopter at the default would have
received a procedure ending in `fail 6` with its own quoted remedy inert. Fixed by a seventh
placeholder rendering the **effective** scope plus an opening precondition sentence
(`SKILL.template.md:133-137`, `adopt-unattended.sh:127-134`).

**C6 — the shipped documents affirmatively FORBADE the new path.** The Skill's shared step 1 and
protocol §1 both said the run may not author its build folder. Amending a binding contract went to the
**owner** (M3 veto 2) and was bounded to §1's *description*, never its *mechanism*.

**C7 — a single check grades the FIRST occurrence across the whole file, so a second path is either a
false red or silent blindness.** Leg check 18 orders the first `--preflight` against the first
`/session-kickoff` **across the whole template** (`check-unattended.sh:854-855`). Resolved by a *new,
per-path* check 20 scoped to `## Start a run from a PROMPT`. **A third start path repeats this
exactly** — §3.4.

**C8 — the pin moved in the EXAMPLE and not in the dogfood conf.** Diff-review H1: `DIRECTIVES_CORE`
grew to 13 while `.unattended.conf:71` still declared `DIRECTIVES_FLOOR="11"`, slack by exactly the
two members the build added. **The recommended left-shift gate was never applied**: `grep -n 'example
CORE_FLOOR\|example DIRECTIVES_FLOOR\|ROOT/.unattended.conf' tools/unattended/unattended.test.sh`
returns **two arms, both reading `$example`** (`:1156,:1158`). The installed conf the bar actually
reads is graded by nothing.

**C9 — a descriptor's declaration went stale in the same commit that made it stale.** Diff-review L5:
`kit.toml`'s `placeholders` list is **still six** (`kit.toml:17`) while the template carries **seven**
(`grep -oE '\{\{[A-Z_]+\}\}' SKILL.template.md | sort -u` → `ANCHOR_SCOPE KEEPALIVE_CREATE
KEEPALIVE_DELETE KEEPALIVE_INTERVAL KIT_DIR LANDER MEMORY_ROOT`). `optional_keys` likewise omits
`ANCHOR_SCOPE`, `UNITS_REGION_CUTOFF` and `DIRECTIVES_EXTRA_TABLE`, all three of which this repo's own
`.unattended.conf` declares. **Live and unfixed.**

---

## 2. `tools/unattended/unattended.sh` (138 427 B, 2 057 lines) — the seam inventory

**M** = mechanical (a value joins a list) · **D** = design (new behaviour) · **B** = broken as written.

### 2.1 The mode declaration and the closed set

| Site | Lines | Verdict | What must happen |
|---|---|---|---|
| `AUTH_MODE=""` global + comment | `241-246` | **D** | The comment states *"nothing in this kit branches on the recorded value."* Fork 2 (gate the declared output paths) makes that **false**. Either the comment moves or the refusal stays keyed on the *derived* global rather than the recorded fact. |
| front-matter awk arm | `786` | **M** | `/^authorized-by:/ { … print "mode=" v; next }` already returns any value. No change. |
| the closed-set `case` | `793-797` | **M** | `case "$AUTH_MODE" in prompt\|slug) ;;` → add the third. The `fail 44` message **embeds the set in prose** — *"outside the closed set of prompt and slug"* — and that text is a `check-arms` **signature** (`check 44 branch 1 line 796 ARMED`). Rewording moves the signature; the arm at `unattended.test.sh:1676` must move in the same commit. |
| **the set has no published constant** | — | **D** | `PHASES_CORE`, `PHASES_TERMINAL`, `PHASES_PASSKIND`, `DOD_CORE`, `DIRECTIVES_CORE` are all `KEY="…"` lines the leg reads through `core_of` (`check-unattended.sh:62-82`). The mode set is the **only** closed set spelled as an inline `case`. **Recommend publishing `AUTH_MODES="slug prompt <third>"` and having the leg read it** — the shape `PHASES_PASSKIND` took at `b0b2b4e` for exactly this reason. Without it, leg check 19 stays blind to membership (§3.2). |

### 2.2 The core declarations

| Constant | Line | Verdict |
|---|---|---|
| `PHASES_CORE` | `82` | **M**, *if* the mode needs new positions. `RESEARCHING`/`TESTING` already exist and fork 3 makes pieces PASSES. A `PRODUCING` phase would be **M** in the constant and **D** in three places: `CORE_FLOOR` (both confs), protocol §3's run-order token list (joined both ways, `check-unattended.sh:770-780`), and the pass-kind question below. |
| `PHASES_TERMINAL` | `83` | no change |
| `PHASES_PASSKIND` | `89` | **D**. If a piece-producing pass is a *pass kind*, this line and protocol §3's anchored `PASS kinds:` paragraph both move, joined both ways with a vacuity guard (`check-unattended.sh:783-805`). If pieces are POSITIONS (the `RESEARCHING`/`TESTING` precedent) neither moves, and the protocol must SAY so, because the row join cannot see prose. |
| `DOD_CORE` | `93` | **D + B** — §2.3 |
| `DIRECTIVES_CORE` | `112` | **M** in the constant, **B** downstream — §2.4 |
| `phases()` `dod()` `directives()` | `114-119` | no change (composition only) |
| `scope_of` | `123-132` | **M**. Returns any third field verbatim; the two-field default falls out of `${rest#*:}` vs `$rest`. Correct for N scopes as written. |
| `checker_of` | `134` | **B for a scoped DoD item** — `${p#*:}` is *shortest*-prefix removal, so `pieces-complete:machine:playbook` returns `machine:playbook`, which `!= agent`. `verb_attest` would accept it and `verb_close` would treat it as machine. Silent misclassification. |
| `is_terminal` | `133` | no change |

### 2.3 `DOD_CORE`, `checker_of`, and `build-complete` — **the hardest seam**

`DOD_CORE` (`:93`) is eight `<item>:<checker>` entries. **There is no third field and no scope.** The
directive layer got one at `8826eb2`; the DoD layer did not. Consequences, all read from source:

1. **`checker_of` breaks on a third field** (`:134`, above).
2. **The leg's DoD join strips everything after the first colon** — `dcore=$(printf '%s\n' $DOD_CORE |
   sed 's/:.*//' | sort -u)` (`check-unattended.sh:814`). Greedy, so a third field is discarded and the
   item-name join still works. That half is safe.
3. **The protocol's count sentence is a WORD.** `check-unattended.sh:825-835` reads
   `^\([A-Za-z]*\) kit-owned core items\.` and maps `one`…`twelve` to integers.
   `PROTOCOL.template.md:240` currently says **"Eight kit-owned core items."** A ninth item ⇒ `Nine` in
   **both** copies (byte-compared by check 10) and a new row in the §4 table at `:245-252`, joined both
   ways.
4. **`CORE_FLOOR`'s DoD half must move** in `.unattended.conf:54` **and** `.unattended.conf.example:46`
   (both `12:8`). Only the example is armed (`unattended.test.sh:1156`). **C8, live.**
5. **`verb_abort` hard-codes the agent-item list.** `unattended.sh:1293` — `for item in
   keepalive-reaped parked-decisions-surfaced`. A **derived population written in prose**: a new
   `:agent` DoD item is silently NOT owed by `--abort`. Fix by deriving from `$(dod)` filtered on
   `checker_of` = `agent`.
6. **The record-key mapping is hard-coded in three places** — `verb_close:1662`, `verb_abort:1301`,
   `verb_attest:1928`, all `case "$item" in parked-decisions-surfaced) key=parked-surfaced`.

**Can `build-complete` be made to count pieces? No, and it should not be.** Its five terms, read at
`unattended.sh:1746-1801`, in evaluation order:

```
region(README, UNITS_OPEN, UNITS_CLOSE) well-formed  -> else "no well-formed units marker pair"
_bcrows = unit_rows(README)        non-empty         -> else "carries no unit ROWS"
_bcids  = unit_ids_of(slug)        non-empty         -> else "names no unit id"
_bcmiss = missing_units(slug, dir) empty             -> else "a unit that no tracked spec carries"
_bcnon  = nonterminal_units(README) empty            -> else "a unit of this build is not terminal"
```

**Every term reads the build README's `gen:build-units` region and nothing else.** `unit_rows`
(`:1055-1059`) selects `^\| \[.*\]\(spec/` inside that region; `unit_ids_of` (`:1013-1018`) greps
`[A-Z]+-<slug>-[0-9]+` in it; `missing_units` (`:1029-1033`) joins the authored roster against
`git ls-files "$dir/spec/*.md"`. Under fork 3 (one unit per playbook RUN, pieces are passes) that
region holds **one row**, and `build-complete` returns 0 the moment that one spec header says `CLOSED`.
**N is invisible to it.** *(inference, from an exhaustive read of all five terms — no term touches the
filesystem outside `readme_of "$slug"` and that `git ls-files`.)*

Widening `unit_rows` to admit piece rows is the **wrong** move and the record already says why:
`TOOL-aPromptedMandate-12` narrowed it precisely because record rows were counted as unfinished units,
and the guard is now **doubled** — a nested `gen:build-units` region *plus* the `](spec/` selector,
deliberately, *"because they fail differently"* (`:1043-1049`). Re-widening undoes a landed fix.

**Recommendation:** a **new DoD item** — `pieces-complete:machine` — whose checker reads a declared
piece manifest or the run-state facts, and which is **inert on a slug/prompt run**. Making it inert
needs one of:

- **(a) a third field on `DOD_CORE`** — costs the `checker_of` fix, the leg-join audit and the protocol
  grammar. Consistent with the directive layer. **Preferred.**
- (b) an item that self-satisfies when `mode != playbook` — cheaper, but a check that passes by finding
  nothing on 100 % of existing runs, which is the class this repo reds by name.
- (c) `DOD_EXTRA` — **refused by the kit's own argument**: a project-selectable core obligation is
  narrowing wearing another name (`unattended.sh:107-111`).

### 2.4 `DIRECTIVES_CORE` and the waiver scope — **F2**

Adding `playbook-followed:M13:playbook` to `DIRECTIVES_CORE` (`:112`) is **mechanical in the constant**
and **breaks two consumers**.

`check_waiver_scope` (`unattended.sh:655-667`):

```sh
h=${WAIVE_ITEMS[$i]}; sc=$(scope_of "$h")
if [ "$sc" = prompt ] && [ "${AUTH_MODE:-}" != prompt ]; then
```

**Reproduced** by running the shipped `scope_of` plus this predicate over a registry carrying
`playbook-followed:M13:playbook`:

```
handle=researched         scope=prompt    run-mode=slug      --waive REFUSED
handle=researched         scope=prompt    run-mode=playbook  --waive REFUSED
handle=playbook-followed  scope=playbook  run-mode=slug      --waive accepted   <-- vacuous
handle=playbook-followed  scope=playbook  run-mode=prompt    --waive accepted   <-- vacuous
handle=playbook-followed  scope=playbook  run-mode=playbook  --waive accepted
```

**The proposed generalization, also measured** — `[ "$sc" != all ] && [ "$sc" != "${AUTH_MODE:-}" ]`:

```
handle=minimal-prose      scope=all       run-mode=<unset>   --waive accepted
handle=researched         scope=prompt    run-mode=slug      --waive REFUSED
handle=researched         scope=prompt    run-mode=prompt    --waive accepted
handle=researched         scope=prompt    run-mode=<unset>   --waive REFUSED
handle=playbook-followed  scope=playbook  run-mode=slug      --waive REFUSED
handle=playbook-followed  scope=playbook  run-mode=playbook  --waive accepted
handle=playbook-followed  scope=playbook  run-mode=<unset>   --waive REFUSED
```

All eight pre-existing cells are byte-identical to today's behaviour, and the fail-closed property the
current comment argues for (`:1399-1401` — *"an UNDERIVABLE mode must refuse a scoped waiver rather
than grant it"*) is preserved. **The `fail 45` message must be reworded** (it names `prompt`
explicitly) and it is an armed signature — `check 45 branch 1 line 662 ARMED` — so the arm moves with
it.

**Call-site ordering is already correct and must not move.** `check_waiver_scope` is invoked at
`unattended.sh:1402`, *after* the authorization block at `:1259-1265`; the comment there records that
placing it in `check_waivers` (which runs at `:1186`) is unbuildable. That is C3, already paid.

### 2.5 The verbs — argv, dispatch, and three stale spellings of the verb set

`while [ $# -gt 0 ]` at `:2013`; dispatch `case` at `:2047-2056`. **Ten** verbs are dispatchable:
`--preflight --plan --phase --status --resume --close --landed --abort --park --attest`.

> The lens brief calls this "the four-verb driver". It is ten.

**The verb set is spelled in five places and three are stale.** Measured:

| Carrier | Line | Verbs named | Missing |
|---|---|---|---|
| header docstring | `5-14` | 9 | **`--attest`** |
| `fail 14` refusal | `2037` | 9 | **`--attest`** |
| usage line | `2045` | 10 | — |
| dispatch `case` | `2047-2056` | 10 (incl. inline `--plan`/`--phase`) | — |
| **protocol §7 "The verbs"** | `PROTOCOL.template.md:297-326` | **8** | **`--park`, `--attest`** |

`unattended.sh:2040` carries the comment *"S10 — THE SAME SET, in all three places the driver spells
it"*. It is not the same set, and **nothing joins any pair** — unlike the phase list (check 16 arm D),
the DoD table (check 16's DoD join) and the directive table (check 16 arm A), all of which ARE joined.
The `fail 14` text is pinned by an arm at `unattended.test.sh:1438`, so the wrong set is frozen.

**Verdict:** if playbook mode adds a verb (a piece-ledger writer, or fork 6's proposal register), it
slides into exactly this gap. **Recommend closing it as a unit of this build** — one join from protocol
§7's bullet list to the dispatch `case`, in the shape check 16 arm D already uses.

### 2.6 The remaining verbs, one by one

| Verb | Lines | Verdict |
|---|---|---|
| `verb_preflight` | `1315-1540` | **D**. Records `mode:` at `:1492`, pinned-once (`[ -n "$(fact …)" ] ||`). A playbook run additionally needs the **declared output paths** and the **requested N** at BASE (forks 2 and 3) — both read from the README blob the authorization already fetches, or they are run-writable after the fact. **The parse is already key-tagged and multi-answer** (`:783-790`), so adding two arms there is genuinely mechanical this time. |
| `verb_close` | `1602-1699` | **D**. The DoD loop at `:1650-1683` is fully derived from `$(dod)` and needs no edit *if* the new item is a DoD member. `fail 21` (`:1645`) makes `authorization-reachable` non-overridable; **decide explicitly whether `pieces-complete` is overridable** — an overridable piece count is a run certifying its own output. |
| `verb_park` | `1934-1979` | **M / D**. Fork 6 wants a proposal register distinct from `--park` *because a park blocks the close*. **Measured: it does not, directly.** `parked-decisions-surfaced:agent` is an *attested* item read from `^parked-surfaced: (yes\|true)` (`dod_met:1880`), so an agent can attest it with parks outstanding. What actually blocks is `verb_abort` (`:1293-1305`), which demands both agent items. So the fork's *conclusion* stands but its stated *mechanism* is wrong. `park()` (`:1892`) is kind-parameterised (`park file kind item reason`) and protocol §2 declares four kinds; **a fifth kind `proposal` is the cheapest correct shape** — one new writer, no new file. But leg check 17 (`:505-522`) parses the parked region by a kind-specific regex over `waiver\|decision\|abort\|override`, and `verb_status:1566` counts the same four; **a fifth kind must be added to both or it is unread.** |
| `verb_abort` | `1272-1314` | **B** — hard-coded agent-item list (§2.3 item 5). |
| `verb_landed` | `1216-1271` | **D**. Open row `TOOL-aPromptedMandate-14` records that it is a **third open-coded reader of the units region** that kept the un-narrowed selector. Any piece accounting touching `units-at-landing` (`:1251`) lands on a known defect. |
| `verb_status` | `1541-1572` | **D**. Prints `phase · witness · next unit · parked N`. For a playbook run the useful line is `pieces k/N`; the parked-count regex at `:1566` is the four-kind one above. |
| `verb_attest` | `1913-1932` | **M**. Fully derived — membership from `$(dod)`, machine-refusal from `checker_of`. Works for a new `:agent` item with no edit, **except** that `checker_of` misreads a three-field entry (§2.3 item 1). |
| `verb_plan` / `verb_phase` | `1078`, `1147` | no change |
| `set_fact` / `fact` | `207-217`, `868-880` | **M**. Flat `key: value` under `## Run facts`; a new fact costs nothing. **But** leg check 8 requires the `<!-- run:generated -->` region to be **EMPTY** (`check-unattended.sh:328-331`), so a per-piece ledger cannot live there. |

---

## 3. `tools/unattended/check-unattended.sh` (65 151 B, 925 lines) — the leg

### 3.1 The check inventory, DERIVED

```
$ grep -oE 'fail [0-9]+ ' tools/unattended/check-unattended.sh | awk '{print $2}' | sort -n -u | wc -l
21
```

Numbered **1–21, no gaps**. The file's own docstring at `:2` says "TWENTY-ONE checks", which agrees
(review L4 caught it saying "EIGHTEEN" and it was fixed).

> **Correction to the lens brief.** The brief asks for "checks 8, 9, 13 and **26**". There is **no
> check 26 in `check-unattended.sh`** — the numbering stops at 21. `fail 26` exists in the **driver**
> (`unattended.sh:941`, the terminal-record refusal, which is the very check the aPromptedMandate run's
> LANDED-by-hand note cites). The two numbering spaces are disjoint. The driver's set is 1–47, also
> gapless.

| # | Name (from its own comment / message) | Reads the mode? | Third-mode verdict |
|---|---|---|---|
| 1 | the conf: required keys, `CORE_FLOOR` shape, core sets readable | no | **M** if `CORE_FLOOR` moves |
| 2 | phase vocabulary non-empty, above floor, terminal ⊆ effective | no | **M** if a phase is added |
| 3 | DoD set non-empty, above floor | no | **M** if a DoD item is added |
| 4 | run-state file: readable, declares a phase, phase in vocabulary, archived ⇒ terminal | no | no change |
| 5 | a phase claim carries a witness | no | no change |
| 6 | a witness resolves to a commit | no | no change |
| 7 | at most one non-terminal run-state file | no | no change |
| 8 | the run-state generated region holds NO copy and its markers are well-formed | no | **no change — and it forbids a piece ledger there** |
| 9 | the recorded BASE resolves, is published, is an ancestor, is not degenerate | no | no change |
| 10 | the protocol pair is byte-identical and both halves exist | no | **M** — every protocol edit is doubled |
| 11 | no run-state file names the bypass flag | no | no change |
| 12 | the kickoff engine's hand-back | no | no change |
| 13 | the build README at the recorded BASE: front matter, slug | **partly** | **D** — §3.2 |
| 14 | replace refs / grafts | no | no change |
| 15 | a LANDED witness is an ancestor of the anchor | no | no change |
| 16 | **the cross-document joins** — 20 fail branches, the largest check | **yes (scope arm)** | **B** — §3.3 |
| 17 | parked waivers: in-set, non-empty reason, in the first committed blob | no | **D** if a fifth park kind lands |
| 18 | kickoff after preflight, FIRST occurrence, whole file | no | **D** — §3.4 |
| 19 | **the authorization MODE, re-derived** | **yes** | **D** — §3.2 |
| 20 | the PROMPT path's own ordering, per path | **yes, by name** | **D** — §3.4 |
| 21 | every tracked build README carries exactly one `gen:build-units` pair | no | no change |

### 3.2 Check 19 — the mode second opinion, and what it does NOT check

`check-unattended.sh:463-474`. Presence-guarded on `fact_of "$f" mode`; re-parses `authorized-by:`
from the README blob at the recorded BASE; absent ⇒ `slug`; compares.

**It never validates membership.** There is no `case … in prompt|slug)` on the leg side. A README
declaring `authorized-by: playbok` (typo) and a record recording `playbok` **agree**, and check 19 is
silent. The driver refuses at `fail 44`, but the leg is the bar's *independent* opinion, and on this
question it has none.

Today the gap is narrow (only a hand-forged pair reaches it). **A third mode widens it**: two legal
non-default values makes a near-miss typo plausible, and a record written by an installed driver with a
two-member set against a README from a newer one disagrees in a way check 19 cannot name.

**Recommendation — the single highest-leverage mechanical change in this inventory:** publish
`AUTH_MODES="slug prompt <third>"` in the driver, read it in the leg through the existing `core_of`
(`check-unattended.sh:62-82`, three lines), and add one branch to check 19 refusing a mode outside it.
Then the closed set lives in **one** place, the leg gains a real second opinion, and a fourth mode is a
one-word edit. Without it the set is spelled in the driver `case`, in the `fail 44` message prose, in
`PROTOCOL.template.md:32-40`, and in `SKILL.template.md:56` — four carriers, zero joins.

Note the check's own honest limit, already written at `:456-462`: both sides parse with an awk of the
same shape, so **a parse wrong the same way twice agrees wrongly**. That residual grows with a third
value, not with the code.

### 3.3 Check 16 — **F1, measured firing on a correct implementation**

`check-unattended.sh:702-717`, the `tblscope` extractor:

```awk
if (cell == "all" || cell == "prompt") sc = cell
```

Run over a table carrying three rows — `all`, `prompt`, `playbook`:

```
$ awk -F'|' '<the shipped program>' /tmp/tbl.md
minimal-prose:all
researched:prompt
```

**The `playbook-followed | playbook` row is silently dropped.** `corescope` (built from
`DIRECTIVES_CORE` at `:687-693`) **would** contain `playbook-followed:playbook`, so the string
comparison at `:722` fails and the leg reds with *"the directive scopes the registry declares are not
the scopes the Skill's table shows"* — **on a correct implementation**. This is C2 repeating one layer
down, and it is guaranteed, not probable.

Two further sites hard-code the pair:

- the anti-vacuity message at `:714` — *"the cell it looks for holds exactly all or prompt"* (armed
  signature);
- `:692` refuses any `DIRECTIVES_EXTRA` entry carrying a third field at all (scope is kit-owned).
  Correct as-is; no change.

**Fix:** derive the legal scope vocabulary from the registry's own third fields plus `all`, or from the
published `AUTH_MODES`, never from a literal. Then **measure the extractor against the live table
before wiring** — this repo's own rule, and the thing that would have caught the aPromptedMandate-4
breakage a cycle earlier.

Also inside check 16, if a phase or a DoD item moves:

- run-order join, both ways + vacuity guard: `:770-780`
- pass-kind join, both ways + vacuity guard: `:783-805`
- DoD item join, both ways + vacuity guard + the **word-count sentence**: `:806-836`
- arm A (registry ↔ Skill table), arm B (every `M<n>` resolves in `BUILD-METHOD.md` via
  `^## $sec( |$)`), arm C (floor, plus the "floor below the core count is slack by construction"
  branch): `:629-753`

**Arm B is a hard dependency**: a directive `playbook-followed:M13` requires a literal `## M13 `
heading in `memory/guides/BUILD-METHOD.md`, or check 16 reds.

### 3.4 Checks 18 and 20 — **the second start path repeats C7 exactly**

Check 18 (`:850-863`) takes `awk … index($0,"unattended.sh --preflight") { print NR; exit }` and the
same for `/session-kickoff`, **first match, whole template**, and refuses if kickoff precedes preflight.

Check 20 (`:895-921`) exists *because* check 18 went blind when the prompt path landed. It slices
`^## Start a run from a PROMPT` heading-to-heading and orders three tokens **inside that slice**:
`AskUserQuestion` < `PUSH THE BRANCH` < `**Preflight**`.

**Fork 1 wants a second ATTENDED entry point with no anchor and no push mandate.** Whatever section it
gets:

- placed **before** `## Start a run` and mentioning `/session-kickoff`, check 18's first-match read
  shifts to it and the leg **reds falsely**;
- placed **after**, check 18 keeps grading the slug path and is **silently blind** to the new one — the
  direction the audit named *"the one nobody notices"* (finding id 24);
- check 20's slice is anchored on the literal `^## Start a run from a PROMPT`, so it **will not** grade
  a playbook path, and a bespoke check 22 makes three per-path checks with one shared bug.

**Recommendation: generalize, do not add.** One check that **enumerates every `^## Start a run…`
section**, derives the per-section token set, and asserts the ordering each section declares — with a
refusal when the enumeration finds fewer sections than the template has `## Start a run` headings
(the anti-vacuity guard, which is where the existing pair's guards already live). That is a **DESIGN**
unit and it retires an open liability rather than adding one.

### 3.5 `CORE_FLOOR` and `DIRECTIVES_FLOOR` enforcement

`CORE_FLOOR` (`:100-133`): undeclared ⇒ `fail 1`; malformed (not `<int>:<int>`) ⇒ `fail 1`; phase count
below `pfloor` ⇒ `fail 2`; DoD count below `dfloor` ⇒ `fail 3`. There is **no** "floor below the kit's
own count is slack" branch on `CORE_FLOOR` — that guard exists only for `DIRECTIVES_FLOOR`
(`:743-745`), added by the aPromptedMandate-6 fold after review H1. **Asymmetry worth closing here**: a
`CORE_FLOOR` left at `12:8` after `DOD_CORE` grows to nine is slack by exactly one and nothing says so.

Both floors live in **two** files and only the example is armed (C8). **Both must move together for any
core-set growth.**

---

## 4. `SKILL.template.md` (18 612 B, 306 rendered lines) and `PROTOCOL.template.md` (32 258 B)

### 4.1 Placeholders and the render

Seven distinct placeholders, derived:
`ANCHOR_SCOPE ×2 · KEEPALIVE_CREATE ×1 · KEEPALIVE_DELETE ×2 · KEEPALIVE_INTERVAL ×1 · KIT_DIR ×13 ·
LANDER ×1 · MEMORY_ROOT ×4`. `PROTOCOL.template.md` carries **zero** — it is `cat`-installed, not
rendered (`adopt-unattended.sh:212-217`).

`render()` substitutes all seven (`adopt-unattended.sh:165-172`). `--check` verifies: the rendered Skill
exists, matches a fresh render, carries **no surviving `{{…}}`**, and the protocol half exists and is
byte-identical (`:175-207`).

**If playbook mode needs a conf key rendered into the Skill** (a playbook root, a default output root),
it costs: one `[[files]] placeholders` entry, one `render()` line, one **defaulted-not-blank**
initialisation before `. "$CONF"` — and the `ANCHOR_SCOPE` precedent at `:121-134` says the rendered
value must be the **EFFECTIVE** one, derived through the driver's own fall-through, so no key value can
produce a hole. That derivation pattern is the reusable seam.

### 4.2 The start paths and their sections

`grep -n '^## ' SKILL.template.md` → ten sections. `## Start a run` at `:17`; `## Start a run from a
PROMPT` at `:127-184`. **The prompt path costs 4 275 B / 58 lines** (`sed -n '127,184p' | wc -c -l`).
A playbook path plus an attended entry point is realistically **2×**, i.e. ≈ 8–9 KB on
`SKILL.template.md` — against the +4 893 B the whole prompt unit spent.

`SKILL.template.md` carries **no size gate**: `tools/template-size-limits.txt` names the charter and the
kickoff engine, not this file. *(inference: no row for it, so the gate falls through to
`MAX_BYTES`/default.)* The rendered Skill is what an agent reads at every start and is already
306 lines.

### 4.3 The directive table's `Scope` column and its prose

`SKILL.template.md:28-52`. Thirteen rows, `Scope` cell `all` or `prompt`, plus the prose paragraph at
`:47-52` restating the closed set — *"`all` binds every unattended run; `prompt` binds only a run whose
build README declared `authorized-by: prompt`"*. Joined to the registry by check 16 (**F1**, §3.3).
Adding rows costs: the registry, the table cells, this prose, and the leg's awk.

### 4.4 The protocol sections a third mode moves

`grep -n '^## ' PROTOCOL.template.md` → ten sections.

| § | Line | Why it moves |
|---|---|---|
| §1 The authorization | `15-93` | the mode bullet at `:32-40` states the closed set in prose; fork 2's output-path gate is an authorization property |
| §3 The phase vocabulary | `187` | run-order list + `PASS kinds:` paragraph, **both joined both ways** |
| §4 The Definition of Done | `238` | the **word** count sentence at `:240` and the item table at `:245-252`, joined |
| §7 The verbs | `297` | already 2 short (§2.5); any new verb |
| §8 What a project declares | `327` | the conf-key table at `:334-348` — already missing `DIRECTIVES_EXTRA_TABLE` (grep count **0**) |
| §10 The default directive set | `393` | the scoped members |
| **new §** | — | fork 3's piece semantics, fork 5's playbook validity, fork 6's proposal register — the charter's `kit:`-conditional block in §1 points HERE rather than paraphrasing |

**Every one of those edits is doubled** — `tools/unattended/PROTOCOL.template.md` and
`memory/guides/UNATTENDED-PROTOCOL.md` are byte-compared by check 10 (`:534-551`). And the second copy
is **on the memory read path** (§7.1).

---

## 5. `.unattended.conf.example` (6 199 B) and `kit.toml` (4 649 B)

### 5.1 The conf key surface, derived

`grep -nE '^[A-Z_]+=' tools/unattended/.unattended.conf.example` → **17 keys**:
`MEMORY_ROOT LANDER BYPASS_BAN GATE_CMD WIRING_CHECK KEEPALIVE_CREATE KEEPALIVE_DELETE
KEEPALIVE_INTERVAL CORE_FLOOR KICKOFF_ENGINE KICKOFF_EXITS DIRECTIVES_EXTRA DIRECTIVES_FLOOR
ANCHOR_SCOPE UNITS_REGION_CUTOFF PHASES_EXTRA DOD_EXTRA`.

This repo's own `.unattended.conf` declares those **plus `DIRECTIVES_EXTRA_TABLE`** — a key the example
does **not** ship and the protocol does **not** document (grep count 0). Three inventories, three
answers.

### 5.2 `kit.toml`, and its live staleness

| Declaration | Line | State |
|---|---|---|
| `required_keys_gate` | `31` | 8 keys. The leg's own required-key **loop** names 6 (`check-unattended.sh:54`); `CORE_FLOOR`/`DIRECTIVES_FLOOR` are enforced by separate branches. Consistent in effect, divergent in shape. |
| `required_keys_render` | `32` | 4 — `LANDER KEEPALIVE_CREATE KEEPALIVE_DELETE KEEPALIVE_INTERVAL` |
| `optional_keys` | `33` | 6. **Omits `ANCHOR_SCOPE`, `UNITS_REGION_CUTOFF`, `DIRECTIVES_EXTRA_TABLE`** — all live. **C9, unfixed.** |
| `placeholders` (rendered SKILL) | `17` | **6 of 7** — omits `ANCHOR_SCOPE`. **C9, unfixed.** |
| `[[hole]]` ×3 | — | `keepalive-tool-names`, `directives-floor`, `core-floor`. The latter two discharge on `grep -qE '^DIRECTIVES_FLOOR="?[0-9]+'` and `'^CORE_FLOOR="?[0-9]+:[0-9]+'` — **shape probes, not value probes**, so a *stale* floor discharges the hole. |
| `[[gate_leg]]` ×6 | — | `unattended kit gate` and `unattended skill wiring` (no guard, `red_after_land = true`), plus four guarded self-tests: cross-component, gate selftest, driver selftest, adopter e2e. Mirrored into `tools/gate-legs.json:579-641`; the manifest carries **88 legs** (`grep -c '"name"'`). |
| `[[lf_pin]]` ×4 | — | `.unattended.conf`, `{kit}/.unattended.conf.example`, `{kit}/*.md`, `.claude/skills/unattended/SKILL.md`. **`{kit}/*.md` already covers a new template** — a PLAYBOOK TEMPLATE shipped at `{kit}/PLAYBOOK-TEMPLATE.md` inherits the pin for free; one shipped outside the kit dir does not. |

### 5.3 What NEW conf keys playbook mode would need, and their cost

| Candidate | Needed? | Cost / reason |
|---|---|---|
| `PLAYBOOK_ROOT` | **probably yes** | +1 example row, +1 protocol §8 row, +1 `optional_keys`, +1 `render()` line if the Skill names it, +1 `[[lf_pin]]` if playbooks are byte-compared. **Cheap.** |
| `PLAYBOOK_OUTPUT_ROOTS` (fork 2's declared output paths) | **NO — refuse** | Fork 2 says gate the **declared** output paths. Declared *where* matters more than declared *at all*: a conf key is **project-scoped and working-tree-writable**, so the run can commit a change to it, and protocol §9's reduction eats it whole. The output paths belong in the **build README at BASE**, beside `authorized-by:`, where the same provenance argument that carries the mode carries them. **This is the design decision the fork implies and does not state.** |
| `PIECES_*` (a count) | **NO** | Per-RUN, not per-project — the same argument unit 1 §4 used to reject a conf key for the mode. The owner asks for N *before* the run starts, so it belongs at BASE too. |
| `CORE_FLOOR` / `DIRECTIVES_FLOOR` | **existing, must move** | Two files each, one armed (C8). |

---

## 6. The four test files — arm discipline and the cost of a mode

| File | Bytes | Lines | `FLOOR_ASSERTIONS` |
|---|---|---|---|
| `unattended.test.sh` | 144 478 | 2 244 | 338 |
| `check-unattended.test.sh` | 76 901 | 1 204 | 200 |
| `cross-component.test.sh` | 10 345 | 152 | 13 |
| `adopt-unattended.test.sh` | 12 973 | 207 | *waived — `memory/project/testsuite-count-waivers.txt:20`* |

### 6.1 How an arm is written

Three helpers, identically spelled in all four files:

```sh
hit()  { n=$((n+1)); grep -qF -- "$2" <<<"$1" || { echo "FAIL missing: $2"; st=1; }; }
miss() { n=$((n+1)); if grep -qF -- "$2" <<<"$1"; then echo "FAIL unexpected: $2"; st=1; fi; }
same() { n=$((n+1)); [ "$2" = "$3" ] || { echo "FAIL $1: expected [$3], got [$2]"; st=1; }; }
```

`hit` is the **only** arming helper. `miss` is deliberately spelled so `check-arms.py`'s `NEGATIVE_RE`
(`^\s*(miss\b|.*grep -qF .* <<<.*\s&&\s)`, `check-arms.py:59`) scores it as **not an arm**. `mutate`
(`unattended.test.sh:29-35`) hashes the file before and after and **fails the suite on a no-op edit** —
three shapes of silent no-op cost the last build real time.

### 6.2 The arm-signature discipline, exactly

`check-arms.py` extracts, per `fail` call site keyed on `(number, ordinal-within-number)`:

- the message is captured **to the first unescaped closing quote**, not to end of line (`message_of`,
  `:88-102`) — otherwise `{ fail 2 "…"; BLOCK_OK=0; }` puts source into the signature;
- interpolations (`INTERP_RE = \$\{?[A-Za-z_][A-Za-z0-9_]*\}?`) are **dropped**, surviving literal runs
  are stripped of trailing `:" `, and **the LONGEST run is the signature** (`signature`, `:104-114`);
- a signature shorter than **12 characters** is a hard error — *"reword the message or the arm cannot
  name it"*;
- an arm is a **non-comment, non-negative line of the sibling `<stem>.test.sh` containing that
  signature literally**. A comment quoting it does not arm it.

**Two traps the record already pays for and a mode build will hit again:**

1. `stage_or_fail` binds `local rel="$1"` *specifically* because *"check-arms reads a bare positional as
   LITERAL text, so it lands inside the branch's signature and no assertion can ever match it"*
   (`unattended.sh:906-909`).
2. `check_method` places the interpolated path **last** because *"check-arms reads the literal text up
   to the first interpolation as the branch's signature, so a message that resumes after one can never
   be armed"* (`unattended.sh:635-637`).

**Consequence for F1/F2:** rewording `fail 44` and `fail 45` changes their signatures. Both are ARMED
(`check 44 branch 1 line 796`, `check 45 branch 1 line 662`). The reworded message and its moved arm
must land in the **same commit**, or `check-arms --check` reds.

### 6.3 `ARMS_FLOORS` and the pin

`.memory-tree.conf:178` — `tools/unattended/unattended.sh:81:78
tools/unattended/check-unattended.sh:78:78`. Live, from `python tools/memory-tree/check-arms.py
--report`:

```
tools/unattended/check-unattended.sh    branches  79 (floor 78)   armed  79 (floor 78)
tools/unattended/unattended.sh          branches  88 (floor 81)   armed  85 (floor 78)
```

Three driver branches are legitimately unarmable and pinned in `memory/project/unarmed-branches.txt`
with their reasons (`fail 9` staging; `fail 27`/`fail 29` rotation faults). **The floors are 7 branches
behind the driver's live count** — slack, though shrink-only pins are meant to be raised deliberately.
A mode build adding branches should raise both floors in the same commit; that is the documented
ratchet act.

### 6.4 Where a mode's arms actually go

- **Driver fixtures**: `readme <slug>` + `mutate` to inject front matter. The precedent's trio is
  `tFresh` (no key), `tModeBad` (`authorized-by: banana`), `tModeOk` (`authorized-by: prompt`, inserted
  **after** `slug:` — the C4 discriminator). A playbook build needs the analogous trio plus a fixture
  for any output-path refusal.
- **Leg fixtures**: `anchor_break` / `anchor_restore` (`check-unattended.test.sh:484-497`) to move the
  README **at the anchor**; `pedit` (`:881`) to mutate the protocol template.
- **Cross-component**: `cross-component.test.sh` is the only leg that runs driver-then-leg over one tree
  with a live bare origin. Its `mk <slug> [extra-front-matter-line]` helper (`:56`) **already takes an
  extra front-matter line** — the seam for an `authorized-by: <third>` arm is already there.

### 6.5 Measured arm budget for a third mode

Scaling the precedent (§1b) and adding what fork 1 asks for (**a second entry point**, which the prompt
mode did not have) and fork 5 (**a playbook validity gate** — a whole new predicate):

**Estimate (inference): +30–45 driver assertions, +45–60 leg assertions, +8–15 cross-component, plus a
new self-test for the validity gate.** That is a floor bump in three files and, if the validity gate is
a new `*.sh` defining a `fail()` helper, a **new `(gate, test)` pair discovered by `check-arms.py`**
(its population is derived, not listed — `discover`, `:116-134`) with **every branch required armed from
day one**.

---

## 7. Budgets — measured, exactly

### 7.1 The memory read path — **the binding budget of the whole build**

```
$ python tools/memory-tree/corpus_ids.py --report
read path        : 6 files, 106288 B (tracked-but-absent: 0)
      17267 B  memory/DECISIONS.md
       1738 B  memory/LIVE.md
      20567 B  memory/guides/BUILD-METHOD.md
      13564 B  memory/guides/REVIEW-PROTOCOL.md
      20894 B  memory/guides/SESSION-KICKOFF.md
      32258 B  memory/guides/UNATTENDED-PROTOCOL.md
```

`.memory-tree.conf:113` — `READ_PATH_CEILING="112987"`.

> **Margin: 112 987 − 106 288 = 6 699 B** (5.9 % of the ceiling).

The trend, at three revisions, with the ceiling **unchanged at 112 987 throughout**:

| rev | `UNATTENDED-PROTOCOL.md` | `BUILD-METHOD.md` |
|---|---|---|
| `6517579f` (before the 2nd mode) | 27 582 | 17 460 / 245 L |
| `14ac45e` (after the 2nd mode) | 30 583 | 20 068 / 279 L |
| `HEAD` | **32 258** | **20 567 / 283 L** |

**The second mode consumed 5 609 B of read-path headroom.** A third of the same size leaves ≈ **1 090 B**.

`READ_PATH_HEADROOM="25600"` is declared at `:119` but check 16 *"compares against `READ_PATH_CEILING`
alone"* (`:117`), so the headroom key is documentation, not a second guard.

**Recommend raising the ceiling deliberately, with the argument beside the number (the file's own
convention), as a ratified fork at spec time — not discovered at build time.**

### 7.2 `BUILD-METHOD.md` against its stated budget

`wc -c -l memory/guides/BUILD-METHOD.md` → **20 567 B, 283 lines**.

Stated at `:8-11`: *"**Budget: ≤22 KB, ≤290 lines**… It rose from ≤20 KB / ≤250 lines when M12 landed —
an owner call, because the figure is a stated constraint of a governance carrier and M3's veto 2 makes
changing one an owner turn rather than an agent's."*

> **Margin: 7 lines. Bytes: 1 961 B under 22 KiB (22 528), or 1 433 B under 22 000.**

`M12` (the research→test→choose section, `:256`) cost **+34 lines**. An `M13` of the same size overruns
the line cap by **27 lines**.

**And the budget is enforced by nothing.**

```
$ grep -rn "290\|22528\|22 KB" tools/ --include=*.sh --include=*.py --include=*.txt --include=*.json | grep -v "\.test\."
(no output)
```

`.memory-tree.conf` declares no `GUIDE_CAP_*`, so `check-memory-hygiene.sh:42`'s script defaults apply:
**`GUIDE_CAP_BYTES=61440`, `GUIDE_CAP_LINES=750`** — roughly **3×** the stated budget. The constraint
the owner ratified is a prose claim beside the file it constrains, which is the exact shape the charter
names as rot-prone.

Sections are `## M1` … `## M12` (`grep -n '^## M'`). Check 16 arm B resolves each cited section via
`^## $sec( |$)`, so a directive pointing at `M13` **requires** the heading: the budget and the join are
coupled.

### 7.3 The charter template

```
$ bash tools/check-template-size.sh
template-size OK — coding-governance-agents.template.md: 48163 / 49152 bytes (989 under, 98.0%)
```

> **Margin: 989 B (2.0 %).**

The charter's §1 already carries an **Unattended runs** `kit:`-conditional block pointing at
`memory/guides/UNATTENDED-PROTOCOL.md` and *deliberately not paraphrasing it*. **Playbook mode should
add nothing to the charter** — the pointer already covers it, and 989 B is not a budget to spend on a
paraphrase the template's own rule forbids. `tools/template-size-limits.txt` records that 49 152 was
raised from 32 768 on owner order (2026-08-16); a further raise is another owner turn, and open row
`TOOL-aDeclaredCeiling-1` wants the ceiling turned into a declared pin first.

---

## 8. Mechanical vs design — the verdict

**MECHANICAL** (a value joins a list; the surrounding code is already N-ary):

| Seam | Site |
|---|---|
| the front-matter awk arm reading `authorized-by:` | `unattended.sh:786` |
| the closed-set `case` (plus its message text + arm) | `unattended.sh:793-797` |
| `scope_of`'s third-field split | `unattended.sh:123-132` |
| adding a `DIRECTIVES_CORE` entry (the constant itself) | `unattended.sh:112` |
| `verb_attest`'s membership + machine refusal | `unattended.sh:1919-1926` |
| `verb_close`'s DoD loop | `unattended.sh:1650-1683` |
| `set_fact` / `fact` for new run facts | `unattended.sh:207-217`, `868-880` |
| `core_of` reading a new published constant | `check-unattended.sh:62-75` |
| `CORE_FLOOR` / `DIRECTIVES_FLOOR` values (×2 files each) | `.unattended.conf`, `.unattended.conf.example` |
| `kit.toml` `placeholders` / `optional_keys` / `[[lf_pin]]` | `kit.toml:17,33` |
| `cross-component.test.sh`'s `mk` extra-front-matter arm | `cross-component.test.sh:56` |

**DESIGN** (new behaviour, a decision, or a predicate that must be generalized):

| Seam | Why |
|---|---|
| **publishing the mode set as a constant** | the only closed set without one; unlocks the leg's real second opinion (§3.2) |
| **the scope-cell extractor** | hard-codes `all\|prompt`; reds a correct implementation (**F1**) |
| **`check_waiver_scope`** | hard-codes `prompt`; vacuous for a third scope (**F2**) |
| **a piece-counting DoD item** | `build-complete` cannot see pieces; `DOD_CORE` has no scope field; `checker_of` misreads one (**F3**) |
| **`verb_abort`'s agent-item list** | hard-coded population; a new `:agent` item is silently not owed |
| **the third start path vs checks 18/20** | generalize the ordering check per-section, or repeat C7 (§3.4) |
| **where the declared output paths live** | a conf key is run-writable, so §9 eats it; they must be at BASE (§5.3) |
| **fork 6's proposal register** | a fifth `park` kind + leg check 17's kind regex + `verb_status`'s count regex |
| **the playbook validity gate** | a new discovered `(gate, test)` pair for `check-arms.py`; a new `gate-legs.json` leg |
| **`BUILD-METHOD.md`'s M13 and its budget** | 7 lines of margin; the raise is an **owner turn** |
| **the read-path ceiling raise** | 6 699 B of margin against a 5 609 B precedent |

---

## 9. Two things the plan has not noticed

### 9.1 The name `playbook` is already this repo's word for something else

Measured (`git grep -c -i playbook`, top carriers outside the new build folder):

```
tools/playbook/                       # adopt-playbook.sh, render_playbook.py, kit.toml, README.md
tools/check-playbook-parity.sh        # 18 hits
memory/map/features/playbook.md       # the dossier
tools/govkit/entries/playbook.kit.toml
WIRE-INTO-PROJECT.md                  # 27 hits
```

and decisively `.memory-tree.conf:11` — `DISCIPLINES="playbook kickoff tooling deployer"` — with `:15`
— `FAMILIES="playbook:PLAY kickoff:KICK tooling:TOOL deployer:DEPL"`.

**`playbook` is (a) a kit that renders the governance charter, (b) a stream in the closed `streams`
enum, and (c) an id family prefix `PLAY`.** An `authorized-by: playbook` mode and a `playbook`-scoped
directive collide with all three — in grep, in prose, and in every future reader's head. The SPECCED
lexicon row `TOOL-dClosedLexicon-1` is about exactly this class.

This is **not** a blocker for fork 1 (the fork rules the *mechanism*, not the *spelling*), but the
spelling should be chosen deliberately at spec time. Non-colliding candidates: `recipe`, `script`,
`runbook`, `serial`. The build slug `dScriptedRepeat` already leans `script`.

### 9.2 Fork 5's validity rule refuses one reference playbook — or passes vacuously over it

Fork 5: *"a playbook is VALID only if every step is tagged `GATE <leg>` or `CHECK <why>` and every named
leg is runnable."* Measured against both references using **I21's own step regex**
(`^\*\*([A-Z]\d+(?:\.\d+)?)\.`, from `nicocares/main/scripts/check_content_plan.py:2422`):

| Playbook | bytes | lines | steps | `GATE` tokens | `CHECK` tokens |
|---|---|---|---|---|---|
| `content-plan/PLAYBOOK.md` | 88 331 | 1 290 | **110** (110 unique) | 92 | 95 |
| `brand/art-style/HYBRID-PLAYBOOK.md` | 18 202 | 245 | **0** | **0** | **0** |

`HYBRID-PLAYBOOK.md` has **no step ids, no GATE tags and no CHECK tags at all.** It is a recipe: an
exact parameter table, a slotted prompt scaffold, four hard rules each traced to an owner correction,
an accepted-instance library, a ruled-out section, and a dated bake-off.

So fork 5's rule, applied to the owner's own reference corpus, does exactly one of two things:

- **refuses it** — the validity gate reds on a playbook the owner named as a model; or
- **passes vacuously** — "every step is tagged" over **zero** steps is trivially true, which is
  green-by-absence, the class this repo reds by name, and which the reference implementation itself
  guards against: `check_content_plan.py:2476` fails I21 when it *"harvested only N invariant id(s)…"*
  and `:2496` fails when the step regex *"stopped matching and I21 is selecting almost nothing"*.

**Neither outcome is acceptable as stated.** The fork needs one more ruling: either the PLAYBOOK
TEMPLATE mandates the step grammar (and HYBRID-shaped recipes are a *different artifact* the kit does
not validate), or the validity gate carries a **declared shape per playbook** with an anti-vacuity floor
— a minimum step count the playbook itself declares, so a zero-step playbook is a **named refusal**
rather than a silent pass. The reference already shipped the second answer; copying its guard is cheaper
than inventing one.

**A third observation the forks do not cover:** the reference playbook's own validity gate (`I21`) is a
**project-side** script and every leg it names (`I2`, `I4`, `I21`…) is a **project** leg in
`scripts/check_content_plan.py`, wired into `ci.yml`. That is consistent with fork 7 (the kit stays
agnostic) — but it means **"every named leg is runnable" is the only half of fork 5 the kit can check**,
and it can check only *runnability*, never *relevance*. The kit's own header rule then applies: the gate
must state what it does not check.

---

## 10. Open backlog rows this build collides with or can close

`memory/backlog/TOOL.md` holds **118 OPEN** rows
(`grep -cE '^- TOOL-[A-Za-z0-9-]+ · OPEN'`), plus 17 CLOSED, 9 SPECCED, 1 DEFERRED.

### Rows a playbook-mode build would COLLIDE with

| Row | Why it collides |
|---|---|
| id `TOOL-aPromptedMandate-7` · OPEN | *"the leg's SOURCE-level no-write arm greps for `mv\|rm\|cp\|sed -i\|tee` preceded by any non-alnum, so it matches those substrings inside IDENTIFIERS: a variable named `rmode` reds it as a write."* **Direct hit** — a mode build writes new variables around the mode reader, and `rmode` was literally the variable that cost the last build a rename. |
| id `TOOL-aPromptedMandate-14` · OPEN | `verb_landed` is a **third** open-coded reader of the units region with the un-narrowed selector. Any piece accounting touching `units-at-landing` sits on it. |
| id `TOOL-aDeclaredCeiling-3` · OPEN | *"a slug-carrying backlog row minted after a run reaches LANDED permanently reds unattended check 8."* `TOOL-dScriptedRepeat-1` **is** such a row. |
| id `TOOL-aPromptedMandate-11` · OPEN | `keepalive-reaped` is attestable but not checkable. A piece-count DoD item designed as `:agent` inherits the same hole. |
| id `TOOL-aPromptedMandate-9` · OPEN | nothing in the precondition chain has a timeout; `--preflight` alone exceeds two minutes. An N-piece run is long; this bites harder. |
| id `TOOL-aStandingWrit-9` · OPEN | `--plan`'s FORKED axis reads only §8's first non-blank line, so a spec with `none` first and unresolved bullets later classifies READY. |
| id `TOOL-aStandingWrit-7` · OPEN | nothing binds the EXECUTING kit code to owner-approved code — it bounds every property a new mode's gate asserts. Cite it; do not try to close it. |
| id `TOOL-aDeclaredCeiling-1` · OPEN | wants the template ceiling turned into a declared pin. If this build raises `READ_PATH_CEILING`, it is arguing the same case. |
| id `TOOL-aMeteredTurnstile-2/-3/-4/-5/-6` · OPEN | the bar's wall clock. A 7th unattended leg plus a validity-gate self-test is measurable cost against an already-hurting bar. |

### Rows a playbook-mode build could CLOSE

| Row | How |
|---|---|
| `TOOL-dScriptedRepeat-1` · OPEN | the build's own row |
| id `TOOL-aPromptedMandate-7` · OPEN | **cheap side unit** — anchor the leg's no-write grep on a word boundary or a command position. The build will otherwise pay for it a second time. |
| id `TOOL-aPromptedMandate-14` · OPEN | route `verb_landed` through `unit_rows`, or generalize `marker-contract.test.sh` to the row selector — **necessary anyway** if pieces are accounted anywhere near that region |
| *(new, not yet a row)* | the **verb-set join** (§2.5): protocol §7 ↔ the dispatch `case`. Three stale spellings, no join. |
| *(new, not yet a row)* | `kit.toml`'s `placeholders` and `optional_keys` staleness (C9 — review L5's fix was never applied) |
| *(new, not yet a row)* | the `CORE_FLOOR` "floor below the kit's own count" branch, absent where `DIRECTIVES_FLOOR` has one (§3.5) |
| *(new, not yet a row)* | the installed-conf floor arm (C8 — review H1's left-shift was never applied) |

---

## 11. What this lens could not resolve

- **Whether a piece is a PASS in the build method's sense.** Fork 3 rules that pieces are passes, but
  M6's pass set is CLOSED (`SPECCING REVIEWING FOLDING BUILDING`) and `PHASES_PASSKIND` publishes it for
  a both-way join. Either M6's set opens (a method edit, hence a budget question, hence an owner turn)
  or pieces are POSITIONS like `RESEARCHING`/`TESTING`. **The forks do not say which, and the join makes
  the choice machine-visible.**
- **Whether `pieces-complete` is overridable at close.** `fail 21` makes exactly one item
  non-overridable today. An overridable piece count is a run certifying its own output; a
  non-overridable one can wedge a run with nobody to interpret it — the failure mode
  `TOOL-aPromptedMandate-12` was parked on.
- **How "every named leg is runnable" is checked without executing it.** The reference checks
  runnability by harvesting the ids its own script emits. A producer-agnostic kit (fork 7) has no such
  set. *(inference: the only agnostic answers are (a) the playbook declares its own leg registry and the
  gate joins the two, or (b) the gate refuses a `GATE` tag naming nothing and states plainly that it
  cannot tell a live leg from a dead name.)*
- **Whether the attended entry point produces a run-state file at all.** Fork 1 says "no anchor, no push
  mandate". Every leg check keyed on a run-state file (4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19) then either
  sees an unanchored record — and checks 9 and 13 **refuse** an absent or unpublished BASE by name — or
  sees nothing at all. **This is unresolved and it is the sharpest open question in the fork set: an
  attended playbook run that writes a `RUN.md` will red the bar; one that writes nothing has no phase,
  no witness, no DoD and no `--close`.**
