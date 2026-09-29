# dDerivedDocket — the ratified design (research record)

**Serves:** research TOOL-dDerivedDocket-1..36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1

## Provenance

Composed in the attended session that preceded this run (node `d`, session `2588f719`,
2026-09-12 to 2026-09-14): three adversarially reviewed design workflows and a judge, then three
rounds of owner decisions and the prompt path's single owner turn. The scratchpad file it was
composed in is not tracked; these bytes are the copy of record. It was measured at `09a22d2b`;
this run's BASE is later, so every spec re-grounds its claims against the pinned BASE.
Example ids in the text use the undeclared family `EXMP` (34 rewritten), so no example is
counted as a citation of a real id. Paths under `scratchpad/` name that session's untracked
scratch files and are provenance, not repo paths.

## Design unit label to build unit id

| Design label | Unit | Mechanism |
|---|---|---|
| U16 | `TOOL-dDerivedDocket-1` | held-suite failure baseline |
| U18 | `TOOL-dDerivedDocket-2` | in-place landing merge |
| U19 | `TOOL-dDerivedDocket-3` | the run's landing path |
| U26 (phase, lease, derived_phase) | `TOOL-dDerivedDocket-4` | the HELD phase |
| U26 (scheduler, D12-i9) | `TOOL-dDerivedDocket-5` | auto-resume scheduler |
| U1 (parse and fold) | `TOOL-dDerivedDocket-6` | ask/disposition parser and the status fold |
| U1 (view, guards, print modes; L4) | `TOOL-dDerivedDocket-7` | generated family view |
| U2 | `TOOL-dDerivedDocket-8` | hygiene engine, corpus_ids and row_grammar in builds mode |
| L1+L2 (18r, A1 A3 A5 A6 A7) | `TOOL-dDerivedDocket-9` | transition-merge audit |
| L3 (A2) | `TOOL-dDerivedDocket-10` | merge driver refuses a shard-into-view merge |
| U3 (planner) | `TOOL-dDerivedDocket-11` | migration planner |
| U3 (relocate/ingest/repair/stragglers; A4) | `TOOL-dDerivedDocket-12` | relocation tools |
| U4b (L5, L6, A8) | `TOOL-dDerivedDocket-13` | straggler guard hook bodies and inventory |
| U0 | `TOOL-dDerivedDocket-14` | check 10 for shards-mode adopters |
| U10 | `TOOL-dDerivedDocket-15` | ask envelope and READY |
| U11 | `TOOL-dDerivedDocket-16` | driver ask-awareness |
| U12 | `TOOL-dDerivedDocket-17` | asks-disposed DoD item |
| U13 | `TOOL-dDerivedDocket-18` | leg second opinions |
| F1 / D12-j | `TOOL-dDerivedDocket-19` | authority only from an owner-committed README |
| U4 + U14 | `TOOL-dDerivedDocket-20` | unattended carriers and the two-key refusal |
| U17 | `TOOL-dDerivedDocket-21` | remote-relative bases and complete guards |
| U20 (KF4 KF5) | `TOOL-dDerivedDocket-22` | derived terminal |
| U21 (KF14 KF3) | `TOOL-dDerivedDocket-23` | red attribution |
| U22 (KF2; D12-i4 i5) | `TOOL-dDerivedDocket-24` | inherited-red policy |
| U23 | `TOOL-dDerivedDocket-25` | runner hygiene |
| U24 (D12-i6) | `TOOL-dDerivedDocket-26` | honest verdicts under contention |
| U25 (D12-i7) | `TOOL-dDerivedDocket-27` | declared GATE_WALL bound stack |
| U27 | `TOOL-dDerivedDocket-28` | run-owned process ledger |
| U28 | `TOOL-dDerivedDocket-29` | review durability |
| U29 | `TOOL-dDerivedDocket-30` | checker defects |
| U30 (D12-i10) | `TOOL-dDerivedDocket-31` | build-method carriers |
| U9 (D11-b, D12-i12) | `TOOL-dDerivedDocket-32` | remote CI |
| U3b + D2 table (delegated) | `TOOL-dDerivedDocket-33` | delegated signing: D2 table and D6 sweep |
| U5 | `TOOL-dDerivedDocket-34` | THE FLIP |
| U15 | `TOOL-dDerivedDocket-35` | arming |
| U6 (tooling docs) | `TOOL-dDerivedDocket-36` | memory-tree docs and carriers |
| U6 (charter; D12-i3) | `PLAY-dDerivedDocket-1` | charter template |
| U6 (runbook) | `DEPL-dDerivedDocket-1` | adopter runbook |

---

# Recommended backlog design: asks filed per build, status derived, one generated view per family

Judge's synthesis of the `derive`, `minimal` and `ops` designs and their three critiques. Gov worktree
`build-readme-governance-18d6ea` at `09a22d2b`, 2026-09-13, read-only. Gov paths are repo-relative.
New measurements are throwaway scripts under `scratchpad/judge/`:

| Script | What it measured |
|---|---|
| `judge/mk.py` + a `merge-rows.py` replay | three disposition layouts through the real row driver |
| `judge/anchors.py` | the real `extract.anchor_at` on every line shape proposed below |
| `derive_measure2.py` (re-run) | the check-13 hazard: 27 live row ids already anchored in a foreign build |
| `git for-each-ref` + `rev-list main..<ref> -- memory/backlog` | straggler branches that still edit authored shards |

## 0. Verdict

| Criterion | derive | minimal | ops |
|---|---|---|---|
| (a) status drift made impossible, not counted | 3 | 2 | 3 |
| (b) zero shared-write conflicts for sources | 3 | 4 | 4 |
| (c) enforcement strength and liveness | 4 | 3 | 3 |
| (d) migration cost and risk of loss | 3 | 2 | 2 |
| (e) fit with kits, unattended kit, adopters | 2 | 3 | 3 |
| (f) simplicity for a filing or closing session | 3 | 4 | 2 |
| **total** | **18** | **18** | **17** |

**The spine is `derive`.** It ties with `minimal` on total, and wins on (a) and (c), the two criteria
the owner's question is actually about. Its order-free status fold and named-release holds are the
only status rules that no critique broke. Its `--replay` is the only answer any design gives to
straggler branches. Every one of its confirmed defects is fixed by grafting a part another design
already got right:

| derive defect (critique finding) | graft | from |
|---|---|---|
| a filed slot token that goes stale beside the derived status (F2) | ask rows carry NO status at all | ops |
| a disposition table the row driver cannot merge (F5) | status-first dash disposition rows | ops |
| the `**Answers:**` line can fall out of its 12-line window (F6) | a `closes` verb in the spec status header tail | minimal |
| rows leave check 15, so pointer grading regresses (F7, risk 5) | swap `backlog/` for `builds/*/BACKLOG.md` in the present corpus | minimal |
| the implicit same-id "full answer" closes unrelated asks (F1) | a declared `unit` marker, plus a forward refusal | critique fix |
| no triage forcing function (F16) | a clock-free closeout at build close | ops, re-derived without dates |

## 1. The answer on one screen

- **Where an ask lives.** An ask is filed ONCE, in `memory/builds/<slug>/BACKLOG.md`, where `<slug>` is
  its own id's slug. It is never edited for status, by anyone.
- **What decides its status.** Status is a pure function of three kinds of authored record, and none of
  them is a status token on the ask:
  - the ask row itself, which carries only an optional `unit` marker;
  - spec status headers that name the ask in a `closes` or `advances` verb;
  - disposition rows that any session writes in its OWN `BACKLOG.md`.

  The fold is order-free: no dates, no file order, no git history.
- **What everybody reads.** `memory/backlog/<FAMILY>.md` keeps its path and becomes GENERATED, exactly
  like `LIVE.md`. It lists live asks only, one table row each, with the filed date and what decided the
  status. Check 9 byte-compares it. An id missing from it is terminal, and
  `gen_build_index.py --asks <id>` prints why.
- **What it retires.** Rotation, backlog archives, the curation-debt waiver on `TOOL.md`, check 8 on
  backlog files, the drift pin of 27, the eighth token `WITHDRAWN`, and the BLOCKED dead end.
  `TOOL-aWeighedCompass-3`'s split-or-shorten question dissolves (§14).

## 2. Storage layout and grammar

```
memory/
├── backlog/<FAMILY>.md        GENERATED view, one per declared family (never authored)
└── builds/<slug>/
    ├── BACKLOG.md             NEW: this slug's asks + this slug's dispositions about ANY ask
    ├── README.md              unchanged; absent only for a FILING HOME (§2.4)
    └── spec/ build/ reviews/ prompts/ RUN.md    unchanged (a spec header may carry `closes`)
```

### 2.1 `BACKLOG.md`

```markdown
# aFoo — asks

> Written by sessions holding slug aFoo. Asks carry no status: it is derived, read it in memory/backlog/.

## Asks

- EXMP-aFoo-3 · filed 2026-09-12 · push-main.sh reports a gate RED as a network failure: … → `tools/push-main.sh`
- EXMP-aFoo-4 · filed 2026-09-12 · unit · the cache unit, planned before its spec exists
- EXMP-aFoo-1 · filed 2026-09-13 · runbook step 4 tests the root prefix while step 1 installs under tools/

## Dispositions

- CLOSED · EXMP-dBar-7 · by EXMP-aFoo-2 · the retry guard landed with unit 2
- WONTDO · EXMP-cBaz-3 · refuted: 0 of 40 fixture runs double-count
- BLOCKED · EXMP-aFoo-3 · on TOOL-aWeighedCompass-3 · waits on the split call
- DEFERRED · EXMP-aFoo-1 · until EXMP-aFoo-4 · re-measure after the cache unit lands
- KEEP · EXMP-aFoo-3 · still wanted after this build closed; outside its goal
```

```
ask         := "- " ID " · filed " DATE [" · unit"] " · " TEXT [" → " POINTER]
disposition := "- " VERB " · " ID " · " FIELD " · " WHY
VERB/FIELD  := CLOSED "by " (ID | SHA7+)  |  WONTDO <none>  |  BLOCKED "on " ID
             | DEFERRED "until " ID       |  KEEP <none>        (KEEP only under closeout, §4.5)
ID          := <FAMILY>-<slug>-<digits>, FAMILY from .memory-tree.conf FAMILIES
```

- **An ask row carries no status token.** Both the `derive` and `minimal` critiques found that a
  filed token disagrees with the derived one on day one: 46 and 43 rows respectively. That is the
  authored-beside-derived shape the generator already calls an ERROR (`gen_build_index.py:30-33`,
  refusal at `:644-649`). With no token there is nothing to disagree with, and recall cannot serve a
  stale status.
- **The ask row is the only definition of its id.** Measured with the real grammar
  (`judge/anchors.py`): the ask row anchors `EXMP-aFoo-3`, and disposition rows, view rows, view
  headings and a spec header carrying `closes` all return `None`. That covers the four shapes at
  `tools/memory-recall/extract.py:116-121`. So checks 13-15, recall and the row driver see each id
  defined once, and a foreign disposition claims nothing. That is the UNATTENDED-PROTOCOL anchor ban
  (`memory/guides/UNATTENDED-PROTOCOL.md:246-251`) made structural.
- **`filed` is authored once and is never a status input.** It feeds the forward-only cutoff (§4.4)
  and the view's age column. Its granularity is a day, so node clock skew cannot matter.
- **Text is free prose of any length, on one physical line.** The ask IS the record now, so the
  300-character budget no longer applies to it: that budget existed because a row was an index entry
  (`TOOL-aDrainedSluice-1`, `memory/archive/DECISIONS.2026-08-10.md:46`). The index is the view,
  whose width is bounded at render time. Continuation lines are refused, because the driver classes an
  indented line as STRUCTURE and can detach it (`tools/memory-tree/merge-rows.py:252`; critic G13).
- **One disposition per (file, target).** A disposer changes its mind by editing or deleting its own
  row. That keeps the fold a function of a SET.

### 2.2 The spec side: two header verbs

The status header tail already carries declared verbs (`memory/TEMPLATE-SPEC.md:75-83`), and
`HDR_RE` has no end anchor (`gen_build_index.py:155-159`). Two verbs join `order <n>`:

```
**Status:** INPROGRESS · rev-2 · 2026-09-14 · node d · Tier-1 · base 09a22d2b · streams tooling · closes EXMP-dBar-5..7
**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base 09a22d2b · streams tooling · advances EXMP-cBaz-3
```

- `closes <IDLIST>` means this unit fully answers the ask. `advances <IDLIST>` means it partly serves
  the ask and contributes only while it is live. Ranges expand through `_expand_ids`
  (`gen_build_index.py:500-517`). The parse copies `_parse_order` (`:385-405`): permitted and never
  required, and a malformed value is a refusal, not a silent misread.
- **Why the header and not a body line.** The header must sit in the first 5 unfenced lines
  (`gen_build_index.py:416`). A body line in a 12-line window can be pushed out by the generated
  records region, which `add_spec_records_region` inserts above the first `## `
  (`gen_build_index.py:1594-1602`; `memory/TEMPLATE-SPEC.md:41-52`). If that happened, a CLOSED ask
  would silently revert (derive critique F6, ops critique #10). A verb in the header tail cannot move.
  The form has a live precedent in inCMS (`· closes DBL-bWovenGuardrail-2`), and gov has no header
  carrying `closes` today.
- **Retroactive closure is a disposition, not a header edit.** A landed spec is frozen, so linking an
  ask to a CLOSED spec after the fact is `- CLOSED · <ask> · by <spec-id> · why` in the closer's own
  file. `closes` is the forward tool, and a disposition is the backward one.

### 2.3 The `unit` marker: pairing is declared, never inferred

- **The ask is the unit.** `unit` on an ask says "my same-id spec is my answer". It is written by the
  filer when a unit is PLANNED before its spec exists, which is the protocol's own rule ("a planned
  unit is minted as a backlog row before the run-state file names it",
  `memory/guides/UNATTENDED-PROTOCOL.md:250`). Until the spec exists, the ask derives OPEN.
- **Why not infer it from equal ids.** `derive` (R1) and `ops` (fold step 1) both inferred the pairing,
  and both critiques refuted that on this corpus. I spot-checked two:
  - The row for `TOOL-dFramedEntrypoint-1` is about the agent-cap `parallel([...])` sentence
    (`memory/backlog/TOOL.md:44`). The spec is "the build README's authored half becomes a closed
    heading canon" (its spec file `:1`).
  - The row for `TOOL-aSealedCaravan-1` is waiver-key fragility (`TOOL.md:93`). The spec is "one declared
    install prefix".

  The critiques add `TOOL-cBriefedPilot-23` and `TOOL-aBoundedVerdict-22`, plus 33 low-overlap pairs
  among 150 by heuristic.
- **Forward refusal.** An ask filed on or after `ASK_CUTOFF` whose id equals a spec H1 and which does
  NOT carry `unit` is refused. A defect found in a unit takes a fresh seq. Legacy pairs are adjudicated
  once, at migration (§9, owner decision D2).
- **Which units owe an ask.** Only planned-before-spec ones. The claim that "template section 1
  MANDATES a backlog row" (`tools/unattended/lib-unattended.sh:202-205`; critic G10) is false and is
  rewritten. 471 of 570 units have no row, and that stays legal.

### 2.4 Filing homes

- **What a filing home is.** A folder whose only tracked file is `BACKLOG.md` is a FILING HOME. It
  needs no README and never appears in `LIVE.md` or the ledger.
- **Who needs one.** Six README-less slugs own rows today: aFlaggedScaffold, aSiftedFork, aTracedSpawn,
  aWiredReckoning, aResumedRelay and aWidenedGuide.
- **What changes.** `collect()` skips such a folder instead of raising (`gen_build_index.py:764-768`),
  and check 4 admits `F:BACKLOG.md` (`check-memory-hygiene.sh:512`). HYGIENE's "a single-file build is
  one spec file plus its backlog row — no README" (`memory/HYGIENE.md:39-40`) is false today, because
  the generator refuses it (critic G11). It is REPLACED with the filing-home sentence and not patched.

## 3. Who writes what, stated honestly

| Byte | Writer | Where |
|---|---|---|
| ask row `F-S-n`, and later edits to its text | sessions holding slug S | `builds/S/BACKLOG.md` |
| a disposition about any ask | the disposer, slug T | `builds/T/BACKLOG.md` |
| `closes` / `advances`, spec status | the spec's own build | its spec header |
| views, README regions, `LIVE.md`, ledger | the generator only | outputs, never read back |

- **What the argument proves.** Every authored backlog byte lives in its writer's own folder. A foreign
  session changes an ask's status only by appending to its OWN file. What used to be a merge conflict
  over a status token becomes a derivation over the union of files, and git produces that union when
  it merges disjoint paths.
- **What it does NOT prove (derive critique F5, minimal F7).** One folder slug IS written by more than
  one session and node:
  - `aBoundedVerdict` carries specs from nodes a and c;
  - the unattended driver makes ids follow the FOLDER slug (the `9528b80f` re-mint).

  So "one writer per file" is a practice, not a construction. `merge=rows` moves from
  `memory/backlog/*.md` (`.gitattributes:65`) to `memory/builds/*/BACKLOG.md` to cover the same slug
  on two branches.
- **Residual: a foreign text amendment.** Nothing mechanical stops a session from editing another
  slug's ask TEXT. The generator reads no git (`gen_build_index.py:27`), so it cannot see who wrote a
  line. One such edit is SANCTIONED: repointing a dead path after a rename (§6, check 15). Every other
  change goes through your own file.

## 4. Status model

### 4.1 Vocabulary

The seven tokens stay (`gen_build_index.py:150`). None is authored on an ask.

| Token | Meaning on an ask | How it arises | Released by |
|---|---|---|---|
| OPEN | wanted, nobody on it, not held | default | any event |
| SPECCED | a closing or advancing unit is specced | a spec OPEN/SPECCED in `closes`/`advances`/`unit` | the spec moving |
| INPROGRESS | a closing or advancing unit is being built | a spec INPROGRESS | the spec moving |
| BLOCKED | held on a NAMED prerequisite | a `BLOCKED on X` row with X live, or a BLOCKED spec | X going terminal: automatic |
| DEFERRED | parked by decision until a NAMED id | a `DEFERRED until X` row with X live, or a DEFERRED spec | X going terminal: automatic |
| CLOSED | answered | a CLOSED `closes`/`unit` spec, or a CLOSED disposition | absorbing |
| WONTDO | declined, refuted, withdrawn or superseded | a WONTDO disposition, or a WONTDO `unit` spec | absorbing |

`WITHDRAWN` (`memory/backlog/TOOL.md:337,386,436,442`) becomes a `WONTDO` disposition whose reason
says "withdrawn". It is not an eighth token.

### 4.2 The fold: first matching rule wins, over SETS

For ask A:
- C(A) is every spec whose header `closes` A, plus A's same-id spec when A carries `unit`;
- P(A) is every spec whose header `advances` A;
- D(A) is every disposition row naming A, in any file.

```
R1 CLOSED      some spec in C(A) reads CLOSED, or some D(A) is CLOSED
R2 WONTDO      some D(A) is WONTDO, or A is `unit` and its spec reads WONTDO
R3 INPROGRESS  some spec in C(A) ∪ P(A) reads INPROGRESS
R4 SPECCED     some spec in C(A) ∪ P(A) reads OPEN or SPECCED
R5 BLOCKED     some spec in C(A) ∪ P(A) reads BLOCKED, or some "BLOCKED on X" in D(A) has X live
R6 DEFERRED    some spec in C(A) ∪ P(A) reads DEFERRED, or some "DEFERRED until X" in D(A) has X live
R7 OPEN        otherwise
```

- **Order-free.** Status depends on sets, never on dates or position. That removes four `ops`
  failures together:
  - a rev bump re-dating a spec changes a status (ops critique #4; the header date is the last-CHANGE
    date, `memory/TEMPLATE-SPEC.md:65-68`);
  - a same-day tie has no honest fix (#5);
  - status depends on merge order (#16);
  - a spec-versus-spec tie has no rule (#16).
- **Terminal evidence beats live evidence.** A stale live spec therefore cannot hide a recorded
  closure, which fixes minimal critique F2. `TOOL-aPacedTurnstile-14` shows the case: its row says
  CLOSED by `TOOL-dHonouredPark-1` (`memory/backlog/TOOL.md:186`), while its spec still reads SPECCED
  (spec `:3`). It derives CLOSED, and drift reports the stale spec.
- **CLOSED beats WONTDO.** Both are terminal, so the order is only a tie-break, and drift reports the
  contest.
- **A non-`unit` closing spec reading WONTDO contributes nothing.** The ask survives an abandoned
  attempt. This is the `763201ad` / `TOOL-aQuenchedHarness-9` case (`TOOL.md:426`).
- **Resolving a hold target X.** X is a filed ask (its derived status) or a spec H1 (its header
  token). A filed ask wins when X is both (derive critique F12). X may not be a decision id, which has
  no status, and may not be A itself. A cycle is a verdict (§5.2).
- **The hold rule is closed.** Waits resolve against the FULL derived status of X, so both
  minimal-critique F5 dead ends are closed: a target decided by an authored row, and a target that is
  a decision id.

### 4.3 How a session files, closes, parks and reopens

| Act | What you write | Where |
|---|---|---|
| file an ask | one ask row, `filed <today>` | your own `BACKLOG.md` |
| close by work | `closes <id>` on your spec header; the ask closes when the spec does | your spec |
| close by judgement (Tier-1 fix, triage, refutation) | `- CLOSED · <id> · by <id-or-sha> · why` or `- WONTDO · <id> · why` | your own `BACKLOG.md` |
| park | `- BLOCKED · <id> · on <id> · why` or `- DEFERRED · <id> · until <id> · why` | your own `BACKLOG.md` |
| "until the owner decides" | file one ask that IS the question, and hold against it; closing it releases every hold at once | your own `BACKLOG.md` |
| an external prerequisite | file an ask naming it ("vendor X ships Y") and hold on that | your own `BACKLOG.md` |
| reopen | not possible: terminal is absorbing. A regression is a NEW ask citing the old one. A disposer may delete its OWN mistaken disposition | — |
| a partial unit | `advances <id>`; the ask shows SPECCED/INPROGRESS while the unit is live and returns to OPEN after | your spec |

**The ask owner uses the same forms.** Its declines and holds are disposition rows in its own file, so
there is ONE decline form with ONE precedence. That fixes minimal critique F6, where a third party's
decline outranked the filer's.

### 4.4 Precedence against the measured corpus

| Case | Result | Instances (critiques' counts) |
|---|---|---|
| a `unit` ask whose spec is CLOSED | CLOSED (R1) | 9 SPECCED + 16 OPEN + 1 BLOCKED rows today, once adjudicated `unit` |
| a same-id pair that is NOT a mirror (e.g. `dFramedEntrypoint-1`) | the ask stays live, decided by its own evidence | ≥4 known, 33 flagged by heuristic |
| terminal evidence beside a live spec | terminal (R1/R2), reported **stale spec** | 3: `aPacedTurnstile-14`, `aMendedLedger-8`, `dScaffoldedMirror-13` |
| an ask whose closure is recorded only in spec PROSE | a MINED disposition, owner-reviewed (§9) | `aStandingWrit-3`, `cFinalBerth-3` (`cBriefedPilot-20` spec `:35`, AC4 at `:135`); about 18 more by heuristic |
| slot INPROGRESS with no spec | OPEN | 1: `TOOL-aGradedDoorway-2` |

The `drift_report.py:1583-1642` signal counted only the first class, and its stance "COUNTED, NEVER
REFUSED ... a row's ask can be legitimately WIDER than the unit" (`:1591-1594`) is what `unit` +
`advances` replace. A wider ask is simply not marked `unit`. A DECISIONS row records that
supersession (minimal critique F3).

### 4.5 Closeout: the triage forcing function, clock-free

Rotation was the only thing that ever made anyone look at a row, and it cannot bound a live set (rules
report §2.5). Measured by `ops`: 275 of 346 live asks sit on 60 terminal builds. The replacement:

- **The rule.** For a build B whose README `opened:` is on or after `ASK_CUTOFF` and whose DERIVED build
  status is terminal, every ask filed in B that derives OPEN must carry a disposition row in B's own
  file: KEEP, BLOCKED, DEFERRED, CLOSED or WONTDO.
- **It needs no dates.** It reads an authored `opened:` and derived statuses, and never a header date,
  which is what broke `ops` A6 (#4c). It upstreams nicocares' `closed-build rows` gate
  (`C:/projects/nicocares/main/scripts/check_closed_build_rows.py:2,16-17`) with a keep escape.
- **It is not a live-count refusal.** That is the thing `TOOL-aRelaxedShard-4` refused
  (`memory/DECISIONS.md:24`).
- **How it ships.** Report-only first, gating second, as owner decision D6.

## 5. The generator and the view

### 5.1 Seams (a sibling module, `tools/memory-tree/backlog.py`)

- **THREE SOURCES grows to four** (`gen_build_index.py:21-28`): README front matter, spec status
  headers (now with `closes`/`advances`), every tracked `builds/*/BACKLOG.md`, and the roster scan.
  There is still no history and no mtime.
- **`rosters()` skips `{m}/backlog/` in builds mode only**, beside `LIVE.md` and `ledger/`
  (`gen_build_index.py:684-686`). An unconditional skip changes 31 of 107 rosters in shards mode and
  would red every shards adopter's check 9 on upgrade (ops critique #14). In builds mode the asks are
  read from `BACKLOG.md`, so rosters do not change: the `minimal` simulation measured 0 README `ids:`
  changes.
- **`plan()` adds one artifact per declared family** beside `LIVE.md` (`:1723-1724`). A family with no
  live ask renders `*No live ask.*`, so every declared family HAS a view. That closes the
  one-directional check 3 (gates report §2.1).
- **`collect()` tolerates filing homes** (§2.4).
- **A liveness line on every run.** `build-index: backlog A ask(s) · D disposition(s) · L link(s) in H
  file(s) · V live · K verdict(s)`. A tracked `BACKLOG.md` that yields no ask and no disposition is a
  verdict, because a mis-segmented parser looks exactly like a clean file.

### 5.2 Render path versus verdicts (ops critique #6)

`plan()` serves both `--check` and `--write` (`gen_build_index.py:1737-1738`, `:1897-1898`), and
`main()` turns any `Problem` into exit 1 with nothing written (`:2781-2783`). The module's own rule is
that a raising parser "would let one unannotated record refuse to render every artifact" (`:447-450`).
So:

- **Backlog content never raises on the render path.** An unparseable line is skipped. An
  undecidable status renders a named placeholder, `CYCLE` or `UNRESOLVED`. Every rule in §6's table is
  a VERDICT that `cmd_check` reports and check 9 reds.
- **The one exception is the data-loss guard.** Before overwriting a view, `--write` reads it. If any
  line leads with an id after a list marker (the `A_DASH` shape) or carries a conflict marker, that
  line is authored content the view grammar never emits, and overwriting it would erase it. In that
  case `--write` writes every OTHER artifact, leaves that view untouched, names the lines and
  `migrate_backlog.py --ingest`, and exits 1. `--check` reports the same thing.
  - This is the fix for the two HIGH/BLOCKER findings: minimal F1 and ops #1. Their failure is today's
    remedy line, `build-index DRIFT — run: ... --write` (`gen_build_index.py:1751`), which silently
    erases an authored row that a straggler branch merged into a view.
  - The generator's own docstring names this class: "a generator that deletes inside the memory tree
    on its own authority is a data-loss path" (`:39-41`).
- **A mode guard.** A tracked `builds/*/BACKLOG.md` under `BACKLOG_MODE=shards` is a verdict, which
  catches a half-migration (ops A8).

### 5.3 View grammar

```markdown
<!-- generated by tools/memory-tree/gen_build_index.py --write — do not hand-edit -->
# memory/backlog/TOOL.md — live asks, family TOOL

Derived, never authored. Each ask is filed once in builds/<slug>/BACKLOG.md; its status is computed
from that file, the specs that close or advance it, and dispositions. An id NOT listed here is terminal:
`python tools/memory-tree/gen_build_index.py --asks <id>` prints what decided it. Cite ids, never lines.

| Ask | Status | Decided by | Filed | Summary |
|---|---|---|---|---|
| [EXMP-aFoo-3](../builds/aFoo/BACKLOG.md) | BLOCKED | on TOOL-aWeighedCompass-3 | 2026-09-12 | push-main.sh reports a gate RED as a network… |
| [EXMP-aFoo-4](../builds/aFoo/BACKLOG.md) | INPROGRESS | EXMP-aFoo-4 | 2026-09-12 | the cache unit, planned before its spec exists |
```

- **It defines no id.** The first cell is link-wrapped, so `A_TABLE` misses it (measured, §2.1), and
  there are no dash rows, so `A_DASH` and check 20's unkeyed rule (`row_grammar.py:181-182`) never
  fire. The selftest asserts this with the REAL `extract.anchor_at` when it is importable, and falls
  back to a local copy otherwise (derive critique F13).
- **How the summary is cut.**
  - text before the first ` → `;
  - links reduced to their text;
  - backticks stripped, so the view carries no path token check 15 could grade (derive critique F7);
  - `|` becomes `/`;
  - cut at the last space before `BACKLOG_EXCERPT_CHARS` (default 72), then `…`.
- **Merge-stable.** Rows are sorted by (slug, numeric seq), and there is no count, total or
  per-status section. The Filed column gives age without a clock.
- **Size.** `minimal` measured the table at 50,067 B for TOOL at excerpt 72, with 324 live rows and a
  widest line of 186 characters. The Filed column adds about 4 KB. Today's shard is 359,423 B. A
  tooling session's stated reading order falls from 485,059 B to roughly 180 KB.
- **Print modes, which write nothing and always exit 0.**
  `--asks [FAM|ID] [--all] [--status S] [--build S] [--json]` lists derived status plus the deciding
  evidence, terminal asks included. `--json` feeds drift-audit and the agent carriers (ops
  critique #13).

## 6. Gates (all under `BACKLOG_MODE=builds`; `shards` stays byte-identical)

| Gate | Change | Does NOT check | Liveness |
|---|---|---|---|
| check 9 (`check-memory-hygiene.sh:760-763`) | ADDED: views byte-compared; verdicts V1-V10 below | ask truth; intent; who typed a line | the backlog liveness line; a tracked `BACKLOG.md` with nothing parsed is a verdict |
| check 4 (`:512`) | CHANGED: `F:BACKLOG.md` admitted in builds mode, still refused in shards mode | content | existing `pop_guard 4` |
| check 6 (`:551-579`, remedy `:636`) | CHANGED: `builds/*/BACKLOG.md` joins the row class with its OWN remedy text ("move detail into a build/ recording; never rotate"; minimal F9); views leave check 6 under D3(b) | view bytes, under D3(b) | existing `pop_guard 6` |
| check 7 (`ex7`, `:651`) | CHANGED: `BACKLOG.md` joins `ex7`, because the ask is the record; views STAY, short by construction | ask width | existing |
| check 8 (`:715-754`) | RETIRED in builds mode, and prints `check 8: backlog layout builds — graded by check 9`. `pop_guard 8` learns the mode (`PRE_STATUSY` at `:289` already counts `BACKLOG.md`) | — | the announcement |
| check 13 (`corpus_ids.py:392-393`) | CHANGED: `def_builds` ignores `builds/*/BACKLOG.md`. Re-measured: 27 live row ids are already anchored in another build's records (e.g. `TOOL-aMeteredTurnstile-6` in `aScannedThrottle`), so they would red on day one otherwise; V1 owns an ask's home | foreign anchors of ask ids, as today | existing |
| check 15 (`corpus_ids.py:372-375`) | CHANGED: the present corpus drops `backlog/` and adds `builds/[^/]+/BACKLOG\.md`. Asks keep their grading (227 path tokens in 129 live rows, ops #9), and views are ungraded derived text. A path-only repoint of a foreign ask after a rename is the sanctioned exception to §3 (D9) | view text | existing |
| check 20 (`row_grammar.py:136-146`) | CHANGED: `row_docs` drops `backlog/` in builds mode; V3 carries ask uniqueness corpus-wide, closing the per-file gap (`memory/HYGIENE.md:259-261`) | `BACKLOG.md` | existing |
| check 10 (`:925-932`) | unchanged in gov, where no backlog archive exists after §9; its silent `continue` (`:928`) should announce | — | — |
| drift `backlog_rows_outliving_closed_specs` (`drift_report.py:1583-1642`, pin 27 at `drift_signals.py:260`) | RETIRED in the SAME commit as the flip, so no reassuring zero sits between units (ops #15) | — | — |
| drift `live_backlog_rows_per_shard` (`:1332-1373`) | RE-POINTED at `--asks --json`; watermark `89 -> <measured>` through RATCHETS (`drift_signals.py:354-355`) | — | DEAD PROBE when 0 asks parse while a `BACKLOG.md` is tracked |
| drift `backlog_asks_contested`, `backlog_closeout_pending`, `backlog_evidence_sha` | ADDED, report-only: contested and stale-spec pairs; closeout debt (D6); sha evidence resolved with git (derive F10) | which side is right | examined count > 0 |

**Verdicts inside check 9.** Each must be staged RED in the selftest AND on the real tree before it
lands (charter §7).

| # | Verdict | Note |
|---|---|---|
| V1 | an ask's id slug is not its folder | |
| V2 | a grammar or continuation-line failure; any line outside H1, blockquote, the two headings and rows | |
| V3 | two ask rows for one id anywhere | |
| V4 | two dispositions for one target in one file | |
| V5 | SPECCED, INPROGRESS or OPEN used as a disposition verb | |
| V6 | a hold target that is not an ask or a spec H1, a self-hold, or a cycle | |
| V7 | a disposition target, or a `closes`/`advances` id, that is not a filed ask | the typo guard |
| V8 | a CLOSED disposition without `by`, or whose id evidence resolves to nothing | a sha is shape-checked here, existence-checked by drift |
| V9 | a non-`unit` ask filed on or after `ASK_CUTOFF` whose id equals a spec H1 | |
| V10 | closeout (§4.5) | report-only until D6 promotes it |

V1, V3, V6 and V7 compare files that different sessions write. Each branch can be green alone and the
merge red (derive critique F9). Each verdict names both files and both slugs, and the lander fixes it
with one edit. That is a documented property, not a claim that sources "cannot conflict".

## 7. Merge behaviour

- **Sources.** Per-writer files merge as a union.
- **The residual: one slug on two branches.** Measured through the real driver (`judge/`):
  - status-first disposition rows appended on both sides merge CLEAN, rc 0: 3 keyed and 3 hashed, 0
    conflicts;
  - the `derive` TABLE layout gives `1 structure conflicts, CONFLICT`, rc 1, which reproduces derive
    critique F5;
  - both branches disposing the SAME target differently fail CLOSED into a whole-file conflict. The
    id-half duplicate postcondition fires (`merge-rows.py:356-385`, `row_ids` at `:329-338`). That is
    loud, not lossy, and it is a real semantic contest. V4 forbids the shape anyway.
- **Views.** They carry no merge attribute, like `LIVE.md`. They text-merge or conflict, and the fix is
  `--write`, which the §5.2 guard stops from erasing an authored row. A clean-but-stale merge was
  measured by `ops` #17 ("6 live" against a true 7). Check 9 catches it at the next memory-staged
  commit or at pre-push, and the lander runs `--check` after every merge (minimal F10).
- **What disappears.**
  - the rotation-against-edit whole-file fail-closed (merge report v6; replay `43eb6b10`);
  - concurrent same-day rotations, which produced `archive/TOOL.2026-08-17.md`: 66 non-terminal rows
    under a "terminal only" header, and the lost `TOOL-cBriefedPilot-1` flip;
  - the SESSION-KICKOFF union-reconcile trap (`memory/guides/SESSION-KICKOFF.md:201-204`).

## 8. Unattended kit

- **Gov's conf, changed in the flip commit.** `.unattended.conf:206` drops `memory/backlog` from
  `SHARED_RECORDS`. `:207` gains `memory/backlog:tools/memory-tree/gen_build_index.py` and
  `memory/backlog:tools/memory-tree/backlog.py`. One pair per renderer file, because a pair naming only
  the generator never fires for a pass editing the sibling (derive critique F11).
- **The kit default at `tools/unattended/unattended.sh:328` stays.** Shards-mode adopters still hold
  their authored shard as a shared record (derive critique F8).
- **A new, kit-internal refusal.** A path in both `SHARED_RECORDS` and `GENERATED_INDEXES` is named.
  It compares the kit's own two keys and reads no memory-tree state.
- **`build_commit` needs no change** (`tools/unattended/lib-unattended.sh:197-220`). It already
  excludes the build's whole folder and every `GENERATED_INDEXES` index half, so pass-order and
  brief-recorded verdicts cannot move. The protocol rule that keeps this true: **during a run, every
  ask, disposition and header verb is written in the run's own build folder, minted under the folder
  slug.** That is stated as the charter §2 exception it is. The false "template section 1 MANDATES a
  backlog row" comment (`:202-205`) is rewritten.
- **What a pass may now do.** A pass may declare its build's `BACKLOG.md`, so it can file and dispose
  without an orchestrator `records(...)` commit (`memory/backlog/TOOL.md:6`). Two CONCURRENT passes of
  one build still cannot both declare it, because condition 1 (`unattended.sh:4853` onward) refuses
  them. That claim is scoped to sequential passes; the orchestrator files between concurrent ones
  (ops #11). The view behaves exactly like `LIVE.md` under dispatch.
- **Carrier text.**
  - BUILD-METHOD M6 clause 3 (`memory/guides/BUILD-METHOD.md:192-195`) drops `memory/backlog/*.md`.
    The view is "a generated index TOGETHER WITH its generator", and `BACKLOG.md` is per-build.
  - M9's derivation table (`:271-277`) gains "asks filed and disposed | `--asks --build <slug>`".
  - The protocol's planned-unit rule (`UNATTENDED-PROTOCOL.md:250`) becomes a `unit` ask in the run's
    own file. A declined discovery (`:606-611`) becomes an ask the run files itself.
  - `--close` gains the closeout step once D6 gates it.

## 9. Migration (`tools/memory-tree/migrate_backlog.py --plan | --write | --ingest <ref>`)

1. **Straggler inventory, BEFORE anything is written (minimal F1, ops #1).** On this node alone, 11
   refs carry unmerged commits touching `memory/backlog`. They include `origin/main`,
   `cld/derived-harness-paths` (5 commits) and `origin/branch/gate-bar-tooling-review-020565` (3).
   Every node runs `git rev-list main..<ref> -- memory/backlog` over every ref. Known branches are
   merged before the flip. The rest are listed, and `--ingest <ref>` lifts each one's shard delta
   (merge-base..ref) into asks and owner-folder dispositions afterwards (derive's `--replay`, kept).
2. **Collect.** 499 live and 161 archived row copies: 592 distinct ids over 89 slugs. The parser is
   permissive and never drops a row; it REPORTS what it cannot parse and blocks. It accepts:
   - id-first and status-first rows;
   - `·` or ASCII ` - ` separators;
   - `CLOSED by …` slots and `WITHDRAWN`;
   - the wrapped row at `TOOL.md:61-63`;
   - backticked `| CLOSED |` prose.
3. **Choose one copy per id.** A live copy beats an archived one. Among archived copies, a terminal copy
   beats a non-terminal one, which settles `TOOL-aBranchedMandate-2/-3`
   (`archive/TOOL.2026-08-17.md:86-87,94-95`). The 7 status-disagreeing pairs all resolve to the live
   CLOSED copy.
4. **Write the ask row.** The body stays verbatim minus the status slot. `filed` is the first-seen date
   from `git log`, a one-time input: the generator never reads git.
5. **The same-id adjudication table (D2).** 150 row ids are also spec H1 ids, 99 of them live.
   - PROPOSED `unit`: the rows specced in place (legacy token SPECCED or INPROGRESS; 19 historical
     OPEN→SPECCED flips) and rows born in their spec's own commit.
   - PROPOSED not-`unit`: everything else, with the heuristic low-overlap pairs flagged first. The four
     measured collisions are never `unit`.
   - The owner or a delegated reviewer signs the table before `--write`.
6. **Dispositions in the OWNER's folder.** These are written only where the fold would not derive the
   legacy status:
   - CLOSED `by <sha>` of the commit that set it CLOSED, mined once, so the evidence is real rather
     than a token;
   - WONTDO with the row's own reason;
   - WITHDRAWN as WONTDO "withdrawn";
   - `CLOSED by deletion (TOOL-dSpentCeiling-1)` (`TOOL.md:169`) as `by TOOL-dSpentCeiling-1`;
   - a BLOCKED or DEFERRED row that names an id as a hold on that id; otherwise a hold on ONE triage
     ask the migrating session files once.

   The migration is the one sanctioned cross-folder writer, because it transfers text the owner
   already wrote.
7. **Mined closures (ops #3).** The migrator mines closing phrases from spec bodies and design passes
   ("CLOSED against", "absorbs", "→ CLOSED") into PROPOSED dispositions, and the owner reviews them.
   `TOOL-aStandingWrit-3` and `TOOL-cFinalBerth-3` are the verified cases: `cBriefedPilot-20` closed
   both (spec `:35`, AC4 `:135`), and the 08-17 reconcile lost the flips.
8. **Acceptance ledger: a per-id STATUS report, not an id count.** For all 592 ids it shows the legacy
   token beside the derived one. Every difference is classed as one of: mirror closed, stale spec,
   mined closure, recovered flip, or collision kept live. Acceptance is "the signed table, applied
   exactly". A pinned count like derive's "exactly 29 OPEN→CLOSED" would red the very review that
   catches an error (derive F1).
9. **Conservation.** Each of the 592 ids has exactly one ask row. The texts are equal apart from:
   - the slot removed;
   - the `filed` and `unit` fields inserted;
   - the declared wrapped-row join.

   Adopters compare normalized fields, not bytes, and relative links are REBASED when text moves:
   swydee's `](../builds/…)` would resolve to `builds/builds/…` (derive critique F4).
10. **In the same commit.**
    - render the views;
    - delete the three backlog archives (their 5 citing records are frozen and backticked, so check 2
      is unaffected);
    - delete the `curation-debt.txt:46` row and retarget `.gitattributes:65`;
    - retire the drift pin and re-point the live-rows signal;
    - edit `.unattended.conf` and add recall's `DURABLE` alternative `builds/[^/]+/BACKLOG\.md`
      (`extract.py:144-149`);
    - set `BACKLOG_MODE=builds` and `ASK_CUTOFF=<flip date>`.

    Run the `recall floor` leg standalone before and after, because 10 of its 12 fixture ids are
    backlog rows (derive F15, ops #19). The pre-commit hook needs `timeout 600000`.

## 10. Adopters

The default is absent `BACKLOG_MODE`, which reads as `shards`: byte-identical, so an upgrade shows no
diff. Each adopter migrates in a DEPL build of its own, after a `--plan` census over its own tree
(derive critique F3). The per-engine edit list is explicit (ops critique #7):

| Adopter | Engine facts | What its migration build must decide |
|---|---|---|
| nicocares | its generator is gov's byte for byte (CR-stripped md5 `f8c6daf520eb` on both); its FORKED files are the engine, `row_grammar.py` and `corpus_ids.py` | re-point `LIVE_ROW_PIN`, `SEVERITY_UNLABELLED_PIN` and `closed-build rows` at `--asks --json` (closeout replaces the last); decide its DEFERRED-as-terminal divergence (`scripts/row_grammar.py:321-322`) as a conf-declared terminal set, never a view choice; 46 DEFERRED + 3 BLOCKED rows with no same-id spec need holds; hand-map 12 legacy rows |
| inCMS | own 27-check engine; generator is a two-way fork (`scripts/gen_build_index.py:2-4`); decision/backlog family split | hand-port the seams; `ASK_FAMILIES` so decision families render no view; 56-58 LEGACY-era rows (`ABL-015` etc.; I count 56) have no slug to route by, so it needs a declared legacy home exempt from V1 (minimal F8, ops #12); retire `rotate_index.py`/`carry_backlog.py`/`dedupe_backlog.py`; check 27 learns `BACKLOG.md` |
| swydee | 2.2 stock, 6 status-first rows, driver inert | only inside its kit upgrade; the migrator's fixtures ARE its two row shapes; rebase links. NOT the pilot: six rows prove nothing (derive F4). The pilot is `--ingest` replaying gov's own recent backlog merges |

## 11. What gets deleted in gov

- **Records.** The authored bodies of `memory/backlog/*.md`, `archive/TOOL.2026-08-{14,17,17b}.md`
  (D8), the `curation-debt.txt:46` row, and `.gitattributes:65`.
- **Checks and signals.** Check 8's backlog population, the outliving signal with its pin, and
  `_TERMINAL_STATUSES` in drift (`drift_report.py:1324`), which reads the kit's derived output instead.
- **HYGIENE text.**
  - backlog rotation (`memory/HYGIENE.md:78-81`);
  - the live-row floor (`:74-77`), rewritten as "the view's size is its live count";
  - "Status vocabulary (backlogs)" (`:83-90`), rewritten;
  - the single-file-build sentence (`:39-40`).
- **Other prose.**
  - the shard-header "leads with one status token" wording (critic G12), which was the literal source
    of swydee's status-first rows;
  - the SESSION-KICKOFF trap (`:201-204`) and its check-8 note (`:250`);
  - the `lib-unattended.sh:202-205` claim.
- **Charter template.** `:59`'s "(backlogs, indexes)" and `:149`'s "status updated in place" become
  "asks are filed per build; status is derived (§5)". The template is 49,032 B against 49,152 B, so the
  edit must be net-negative (minimal critique F11), and it is.

## 12. Critique findings, and where each is folded

"Confirmed" means I re-verified the finding against code or by measurement. "Accepted" means I found
it sound on reading and did not re-measure it.

| Finding | Status | Folded into |
|---|---|---|
| derive F1 / ops #2: the implicit same-id pairing closes unrelated asks | CONFIRMED (`TOOL.md:44`, `:93` against their specs) | §2.3 `unit`; V9; §9 step 5 |
| derive F2 / minimal F4: a filed status token disagrees with the derived one | CONFIRMED by mechanism (`gen_build_index.py:30-33`) | §2.1: no status on an ask |
| derive F3: adopter migration loses state | accepted | §10: census per adopter; conf-declared terminal set |
| derive F4: the swydee pilot | accepted | §9 step 9; §10 |
| derive F5: the disposition table conflicts; the slug is not session-exclusive | CONFIRMED (`judge/` replay: T rc 1, D rc 0) | §2.1 dash dispositions; §3 |
| derive F6 / ops #10: the Answers/Closes line leaves its window | CONFIRMED (`gen_build_index.py:1594-1602`) | §2.2 header verb |
| derive F7 / ops #9: check 15 coverage | CONFIRMED (`corpus_ids.py:372-375`) | §6 check 15; stripped view backticks |
| derive F8: the unattended default flips early; `build_commit` | CONFIRMED (`unattended.sh:328`; `lib-unattended.sh:197-220`) | §8 |
| derive F9: cross-file refusals fire post-merge | accepted | §6, stated as a property |
| derive F10: fabricated evidence | accepted | V8 + drift sha check |
| derive F11: the wrong generator pair | accepted | §8, two pairs |
| derive F12: a hold target that is both an ask and a unit | accepted | §4.2 |
| derive F13: the anchor assertion checks a copy | accepted | §5.3, the real `anchor_at` |
| derive F14: a staged-RED that cannot red | accepted | U1 stages it together with a deletion |
| derive F15: loose ends | accepted | §9 steps 2, 6, 10; §11 |
| derive F16: growth and no triage | accepted | Filed column; §4.5; D7 |
| minimal F1 / ops #1: the flip erases straggler rows | CONFIRMED (11 refs; `gen_build_index.py:1751`, `:1897-1907`) | §5.2 guard; §9 step 1; `--ingest` |
| minimal F2: a stale self-spec outranks a closure | CONFIRMED (`TOOL.md:186` against spec `:3`) | §4.2, terminal first |
| minimal F3: wider asks and the ledger condition | accepted | §4.4 DECISIONS row; post-cutoff CLOSED specs already owe a ledger (`memory/HYGIENE.md:315-344`) |
| minimal F5: BLOCKED dead-end cases | accepted | §4.2 hold rule |
| minimal F6: two decline forms | accepted | §4.3, one form |
| minimal F7: the hot view; folder-slug minting | accepted | §3; §8 |
| minimal F8 / ops #12: legacy-era ids | CONFIRMED (inCMS, 56 by my regex) | §10 |
| minimal F9: check 6's remedy says rotate | accepted | §6 check 6 |
| minimal F10: a stale clean merge | accepted | §7 |
| minimal F11: headroom, map, HYGIENE | CONFIRMED (49,032 B) | §11; U6 |
| ops #3: conservation counts ids, not statuses | CONFIRMED (`cBriefedPilot-20` spec `:35`, `:135`) | §9 steps 7-8 |
| ops #4 / #5 / #16: the date-ordered fold | CONFIRMED (`memory/TEMPLATE-SPEC.md:65-68`) | §4.2, order-free |
| ops #6: A-rules block `--write` | CONFIRMED (`gen_build_index.py:447-450`, `:2781-2783`) | §5.2 |
| ops #7: engine-edit claims | CONFIRMED (md5) | §10 |
| ops #8: severity is minter-only | accepted | D7: SEV event rows if adopted |
| ops #11: parallel passes | accepted | §8, scoped |
| ops #13: carriers | accepted | U6 |
| ops #14: the roster skip is mode-conditional | CONFIRMED (`gen_build_index.py:684-686`) | §5.1 |
| ops #15: a reassuring drift zero | accepted | §6, same commit |
| ops #17: view merge stability | accepted | §7 |
| ops #18: per-build cap and sweeps | accepted | §6 check 6 remedy; dispositions stay one clause |
| ops #19: recall floor | accepted | §9 step 10 |
| NEW (judge): one slug on two branches disposes one target | measured, fail-closed | §7; V4 |

## 13. Owner decisions (genuine forks)

- **D1: adopt this model at all?**
  - (a) Yes: per-build asks and a derived view.
  - (b) No: stay authored and answer `TOOL-aWeighedCompass-3` inside the shard model.

  **Recommend (a).** (b) keeps every measured defect: status authored and drifting, a waiver hiding
  six check-8 faults, rotation that cannot bound a live set, and lost flips.
- **D2: legacy same-id pairs.**
  - (a) Default not-`unit`, with a reviewed PROPOSED list.
  - (b) Default `unit`, which auto-closes 16+ OPEN rows.

  **Recommend (a).** At least four pairs are different subjects, and a CLOSED is absorbing.
- **D3: cap the view?**
  - (a) Keep it in check 6 at 61,440 B. That is a hard live-ask cap near 400 TOOL asks, about a week
    of headroom.
  - (b) Report-only live count, watermarked through RATCHETS.

  **Recommend (b).** Closeout (D6) is the forcing function, and `TOOL-aRelaxedShard-4` refused a hard
  live-row bound.
- **D4: terminal is absorbing, with no REOPEN verb?**

  **Recommend yes.** A regression is a new ask, and a disposer may retract its own row. A reopen verb
  needs an ORDER, and ordering by dates is exactly what broke `ops`.
- **D5: must DEFERRED name a release id?**

  **Recommend yes.** Open-ended parking uses an "owner call" ask. Otherwise DEFERRED becomes the new
  dead end (nicocares already reads it as terminal).
- **D6: closeout at build close.**
  - (a) Report-only, then a gate once observed.
  - (b) A gate at the flip.
  - (c) Never.

  **Recommend (a)**, forward-only by `opened:`.
- **D7: severity.**
  - (a) Defer.
  - (b) Adopt nicocares' `BLOCKER/HIGH/MED/LOW` now, forward-only, with `SEV · <id> · <level>` event
    rows so triage never edits a foreign file.

  **Recommend (a)** until the view has run for a while.
- **D8: delete the three backlog archives after the conservation proof?**

  **Recommend yes.** Kept, they are second definitions of 49+ ids, and recall surfaces their stale
  statuses (critic G2). Git keeps them.
- **D9: keep check 15 grading ask path tokens, with a sanctioned path-only repair of a foreign ask?**

  **Recommend yes.** The alternative drops 227 graded tokens.
- **D10: flip timing.**
  - (a) Drain the known straggler branches on all nodes first, with `--ingest` as the backstop.
  - (b) Flip anytime and ingest after.

  **Recommend (a).**

## 14. Relation to `TOOL-aWeighedCompass-3` (split or shorten `TOOL.md`)

- **This design answers the call with a third option.** It splits the backlog BY BUILD, and it
  generates the index.
  - A family split would need a new `FAMILIES` entry, because check 3 admits only `<FAMILY>.md`
    (`check-memory-hygiene.sh:389-393`). It would also churn id routing, the §6 reading order and the
    codebase-map `backlog-shards` keys (`tools/codebase-map/map_extractors.py:120-123`;
    `memory/map/baseline.toml:68-72`; critic G1). None of that is needed.
  - Shortening would rewrite 313 essays to 300 characters. That is not needed either: the essays
    become records in 89 per-build files, where no entry budget applies, and the family view is about
    50 KB of one-line live asks.
- **What happens to the call at the flip.** The flip commit disposes `TOOL-aWeighedCompass-3` as WONTDO
  "superseded by <flip unit id>". Its waiver row (`memory/project/curation-debt.txt:46`) drains in the
  same commit.
- **Until the flip.** Nothing further should be spent on shortening. The waiver already holds.
- **If the owner declines D1,** "shorten" remains the only option that keeps check 3 and the map
  intact, and it should be done with a compressor like inCMS's `carry_backlog.py` rather than by hand
  (critic A2).
- **The check-10 pair.** `TOOL-cTracedPromise-6` and `TOOL-aBoundedVerdict-9` become moot for gov but
  stay true for shards-mode adopters. U0 fixes them there.

## 15. Phased units: each phase leaves the bar green

| # | Unit | Tier | Lands green because | Depends |
|---|---|---|---|---|
| U0 | (optional, independent) check 10 for shards mode: FAMILIES lookup for `backlog/` archives, the `b` suffix, and an ANNOUNCED skip; closes `TOOL-cTracedPromise-6` + `TOOL-aBoundedVerdict-9` for adopters | 1 | gov's archives referenced on lines 1-3 in the same commit, staged RED first | — |
| U1 | `backlog.py` + generator seams, DARK. Covers: parser; `closes`/`advances` in `parse_spec`; the order-free fold; verdicts V1-V10 in `cmd_check` only; placeholders; the data-loss and mode guards; the table view; `--asks`; `BACKLOG_MODE` (default `shards`); `ASK_CUTOFF`; `BACKLOG_EXCERPT_CHARS`; the mode-conditional roster skip; filing homes; the liveness line. Selftest arms: each verdict staged RED; `--write` succeeds on a tree carrying each verdict; the guard REDs on a straggler-merge fixture; the anchor-free assertion with the real grammar | 2 | gov stays `shards`: `--check` clean with ZERO artifact diff; no gov header carries `closes` today | — |
| U2 | Hygiene engine + `corpus_ids` + `row_grammar` mode switch for checks 4, 6 (with remedy text), 7, 8 (announced), 13, 15, 20; conf example keys; HYGIENE and TEMPLATE-SPEC TEMPLATE text describing both modes; hygiene selftest fixtures on a builds-mode scratch tree | 2 | dark under `shards`; any new shell `fail` branch gets its arm and `ARMS_FLOORS` moves in the same commit | U1 |
| U3 | `migrate_backlog.py --plan` and `--ingest`, read-only on the tree. Produces: the straggler inventory, the D2 adjudication table, mined-closure proposals, the per-id status report and the conservation proof over gov; plus a read-only census over nicocares, inCMS and swydee. Filed as a build record for owner sign-off | 2 | writes only its own build record | U1 |
| U4 | Unattended kit: the two-key contradiction refusal; the `--close` closeout step behind conf; the lib comment rewrite; PROTOCOL/SKILL text for folder-slug filing and `unit` asks; BUILD-METHOD M6/M9 template text. Gov's `.unattended.conf` does NOT change here | 2 | the kit default is unchanged; gov's conf is untouched until U5 | U1 |
| U5 | **THE FLIP**, one atomic commit, after D1, D2 and D10. Contents: `--write` with the signed table; views; archive and waiver deletion; `.gitattributes` retarget; drift retire and re-point (plus the three report-only signals); gov `.unattended.conf`; recall `DURABLE`; `TOOL-aWeighedCompass-3` disposed. Stage a break on the REAL tree (V1 on a folder-mismatched ask; the guard with a merged authored row), confirm RED, unstage | 2 | the §9 acceptance ledger; `recall floor` equal or better; the full bar `GATE_FULL=1 GATE_SELFTESTS=1` (kit work) | U2, U3, U4 |
| U6 | Docs, same day. Covers: HYGIENE/TEMPLATE-SPEC instances; the charter template §1/§5/§6, net-negative under 48 KiB; AGENTS.md; SESSION-KICKOFF pointer map and trap removal (manifest re-stamp); WIRE-INTO-PROJECT §3 migrate step and attribute retarget; the scaffold header; the merge-driver dossier; the `map_extractors.py:120` comment; the agent carriers (`tools/workflows/tier2-review.js:315`, `drift-audit-state.js:198`, `tools/drift-audit/SKILL.template.md:109`, `REVIEW-PROTOCOL.template.md:179`, `tools/memory-recall/SKILL.template.md:91`) pointed at `--asks --json`; a codebase-map dossier `memory-tree-backlog` claiming the three `backlog-shards` keys out of `baseline.toml`, with the map regenerated in the same commit | 1 | template size gate + playbook parity + map coverage | U5 |
| U7 | Promote closeout (D6) to a verdict once drift has shown it firing; severity + SEV/NOTE event rows if D7(b) | 1-2 | forward-only by `ASK_CUTOFF`/`opened:` | U5 |
| U8+ | Adopters, one DEPL build each (§10), none owed now | 2 each | adopters stay on `shards` until their own flip | U6 |

## 16. Residual risks (stated, not solved)

1. An over-claiming `closes` closes an ask silently. It is visible in the view's "Decided by" column and
   in a diff-review lens on header tails.
2. A foreign text edit is undetectable, because the generator reads no history. Only the path-repoint
   edit is sanctioned.
3. The view regrows about 1.4 KB a day at the measured +10 live asks a day until closeout bites (D6).
4. Adopter kit defaults cap a row document at 20,480 B. Three gov builds' `BACKLOG.md` would exceed
   that; on defaults, the remedy is moving detail into `build/` recordings.
5. 222 `memory/backlog/<F>.md:<n>` line citations in frozen build records point into a generated file
   afterwards (critic G8). They are ungraded, and the view header says to cite ids.
6. Two code paths, `shards` and `builds`, live in the kit until the last adopter flips. Each has its
   own selftest arms.

## 17. Owner decisions, ratified 2026-09-13

The owner answered every fork in §13 in chat on 2026-09-13 (node d, session 2588f719). Two answers
differ from the recommendation, D4 and D6. Each of them changes the design, and the changes are
written out below.

| # | Decision | Recommended? |
|---|---|---|
| D1 | ADOPT: per-build asks, derived status, generated family view | yes |
| D2 | Legacy same-id pairs are NOT linked by default. The migrator proposes a list and the OWNER signs it (not delegated) | yes |
| D3 | The view gets a report-only live-ask count, watermarked; no hard byte cap | yes |
| D4 | **REOPEN is allowed.** Ordering rule: a REOPEN cancels NAMED closing evidence (order-free) | **no**, amended |
| D5 | DEFERRED must name a release id | yes |
| D6 | **The closeout is a GATE from the switch-over, retroactive.** Every open ask on a finished build is triaged BEFORE U5 lands, with no grandfather list | **no**, amended |
| D7 | **Severity adopted NOW**, forward-only, as SEV event rows | **no** |
| D8 | Delete the three backlog archives after the conservation proof | yes |
| D9 | Check 15 keeps grading ask paths; a path-only repoint of a foreign ask is sanctioned | yes |
| D10 | Merge the straggler branches on all four nodes BEFORE U5; `--ingest` is the backstop | yes |

### 17.1 D4: REOPEN, order-free

```
disposition += "- REOPEN · " ID " · of " (ID | SHA7+) " · " WHY
```

- **What a REOPEN does.** It cancels exactly one closing or declining record for that ask, and it
  names that record: a spec in C(A), or a CLOSED or WONTDO disposition.
- **The fold changes one clause.** R1 reads "some closing evidence NOT named by any REOPEN of A". R2
  reads "some declining evidence not named by any REOPEN of A". Status is still a function of sets,
  with no dates and no merge order.
- **Re-closing needs NEW evidence.** That means a new spec that `closes` A, or a CLOSED disposition
  `by` a different sha or id. Re-citing the cancelled record stays cancelled.
- **A new verdict, V11.** A REOPEN whose `of` does not name a record that currently closes or declines
  A is refused. That is the typo guard.
- **Undoing your own close.** "One disposition per (file, target)" still holds, so a session never
  REOPENs its own CLOSED row. It deletes the row instead, which it may do.
- **Closeout (§4.5).** A REOPEN counts as that ask's KEEP, because the reopener has asserted the ask
  is still wanted.

### 17.2 D6: the closeout gate at the flip, retroactive with a sweep first

- **Where the closing record may sit.** The closeout is satisfied by a disposition naming the ask in
  ANY file. §4.5 said "in B's own file", but a finished build's sessions do not come back, so a later
  triager records KEEP, a hold or a close in THEIR own folder. The one-writer rule is unchanged.
- **The sweep is a new unit, U3b, sitting before U5.** Every ask that derives OPEN on a finished build
  gets exactly one of: KEEP, BLOCKED on, DEFERRED until, CLOSED by, or WONTDO. It also gets a SEV
  (D7).
  - The ops designer measured 275 asks on 60 finished builds on 2026-09-13. Re-measure at U3.
  - U3's planner pre-fills proposals: mined closures, asks whose pointer target no longer exists,
    and asks whose closing spec is terminal.
  - Delegate sessions may propose. The owner signs, which matches D2's signing rule.
  - The output is a signed triage table filed as a build record.
- **The migrator applies the triage table in U5,** alongside the D2 table. It is already the
  sanctioned cross-folder writer at the flip, so TOOL.md is never edited twice.
- **V10 is a GATE from U5.** It is no longer report-only. It must be staged RED on the real tree
  before U5 lands. U7's "promote closeout" is absorbed.

### 17.3 D7: severity now, forward-only

```
disposition += "- SEV · " ID " · " ("BLOCKER" | "HIGH" | "MED" | "LOW") " · " WHY
```

- **Where SEV rows go.** They are event rows in the labeller's own file, so triage never edits a
  foreign file. A filer labels its own new ask with a SEV row in the same `BACKLOG.md`.
- **Multiple SEV rows.** They resolve order-free. The proposed default is **the most severe wins**. It
  is conservative and it is a set function. This is a spec-level choice the owner can override at the
  U1 spec audit.
- **Forward-only (new verdict V12).** An ask filed on or after `ASK_CUTOFF` with no SEV row in any
  file is refused. Legacy asks may stay unlabelled, though the U3b sweep labels every ask it touches.
- **The view** gains a `Sev` column, of about 8 B per row. Drift-audit gains
  `backlog_asks_unlabelled` as a report-only count.
- **nicocares** can re-point `SEVERITY_UNLABELLED_PIN` at `--asks --json` in its own DEPL build.

### 17.4 The revised unit plan

| # | Unit | Change from §15 |
|---|---|---|
| U0 | check 10 for shards-mode adopters | unchanged, optional |
| U1 | `backlog.py` + generator seams | adds REOPEN and V11, SEV rows and V12, the Sev column, V10 live under builds mode, and closeout accepting any file |
| U2 | hygiene engine mode switch | unchanged |
| U3 | migration planner | adds the triage worksheet for U3b |
| U3b | **NEW** triage sweep: a signed table for every open ask on a finished build | new; owner signs |
| U4 | unattended kit | unchanged |
| U5 | the flip | also applies the triage table; V10 gates from this commit; the stragglers are drained on nodes a, b, c and d first (D10) |
| U6 | docs | also documents REOPEN, SEV and the closeout gate |
| U7 | — | absorbed into U1 and U5 |
| U8+ | adopters | unchanged |

## 18. D11, the pre-adoption straggler guard (owner requirement, 2026-09-13)

**The requirement.** Any branch that forked before the flip and still edits authored shards is told,
mechanically, to relocate those edits into the per-build files. It is told BEFORE it can land them,
and no one has to remember it exists. D10's drain covers the branches someone knows about. This
section covers the rest.

### 18.1 Two facts that decide where the guard must live (verified 2026-09-13, node d)

- **Old branches run main's hook files.** `core.hooksPath` is repo-global and absolute
  (`C:\projects\coding-governance\.githooks`), so every worktree on a node runs the PRIMARY tree's hook
  files. Once main carries a hook, a branch that forked months ago runs it too.
- **They run their own copy of the checkers.** The hooks resolve what they run through the committing
  worktree's `$top` (`.githooks/pre-commit:10`, `:48`; `.githooks/pre-push:40`), so a pre-flip branch
  runs its OWN old kit. A guard written only inside the kit, in the hygiene engine or the generator,
  never reaches it.
- **Therefore the detection lives in the hook body.** It is self-contained shell that reads git
  objects, never the branch's kit.
- **There is no `pre-merge-commit` hook today.** The lander `tools/push-main.sh` merges without one.

### 18.2 The detection predicate (content-based, no flip sha needed)

A commit cannot embed its own sha, so the guard never names the flip commit. It compares CONTENT:

- **P1, the flip is live.** `git show <default>:.memory-tree.conf` declares `BACKLOG_MODE=builds`.
  - It is read from the default branch's committed object, not a working copy, so it is the same from
    every worktree.
  - While P1 is false the guard is dormant, which is how it lands dark before U5.
- **P2, the branch predates the flip.** The branch tip's own `.memory-tree.conf` does not declare
  builds mode.
- **P3, the branch has something to relocate.** `git diff --name-only <merge-base>..HEAD` plus the
  index touches `memory/backlog/`.

The verdicts:
- P1 and P2 without P3: a one-line notice, "merge <default> before filing backlog asks".
- P1, P2 and P3: a STRAGGLER. Print the relocation recipe (§18.4).

### 18.3 Where it fires: layered, each layer a different moment

| # | Moment | Carrier | Behaviour |
|---|---|---|---|
| G1 | commit on the straggler | `.githooks/pre-commit` body (global, every worktree on the node) | REFUSES a commit that stages `memory/backlog/*.md` and prints the recipe. Any other commit on a straggler gets a one-line notice and is never refused. `--no-verify` is the deliberate bypass |
| G2 | push of the straggler | `.githooks/pre-push` body | On a feature-branch push: prints the recipe, does not block. On a default-branch push: REFUSES and names the recipe, before the bar |
| G3 | merge INTO the default branch | NEW `.githooks/pre-merge-commit`, plus a `MERGE_HEAD` probe in pre-commit for conflicted merges finished by `git commit` | REFUSES merging a straggler ref into the default branch |
| G4 | landing | `tools/push-main.sh` | refuses to land a straggler branch, same predicate, same recipe |
| G5 | inside a conflict | the generated view's header | carries the relocate instruction verbatim, so a straggler that merges main and conflicts on `memory/backlog/<F>.md` READS the instruction inside the conflict region. This covers `git rebase`, which runs no pre-commit on replayed commits |
| G6 | after the fact | check 9 and the `--write` data-loss guard (§5.2) | already designed; their messages name `--relocate` as the remedy |
| G7 | inventory | `migrate_backlog.py --stragglers` and drift signal `backlog_stragglers` | walks every local and remote-tracking ref. Report-only, with liveness: refs examined > 0, or DEAD PROBE. Used for D10's drain before U5, and it keeps reporting after the flip until the count is 0 |

### 18.4 The remedy the guard prints (one tool, two entry points)

```
This branch predates the per-build backlog (the default branch is in BACKLOG_MODE=builds; this branch is not)
and edits memory/backlog/<F>.md. Those files are now GENERATED; your rows must move to your build folder.
  1. git merge <default>                                  # brings in the new kit
  2. python tools/memory-tree/migrate_backlog.py --relocate --as <your-slug>
  3. git add memory/ && git commit                         # views re-rendered, rows relocated
Nothing is lost: --relocate refuses unless every row your branch changed is accounted for.
```

- **`--relocate`** runs ON the straggler after it has merged the default branch.
  - It takes the branch's shard delta, `merge-base(default, pre-merge tip)..pre-merge tip`, where the
    pre-merge tip is the merge's first parent or `--from <ref>`.
  - It classifies EVERY changed row:
    - **new row:** an ask in `builds/<id-slug>/BACKLOG.md`;
    - **status flip of an existing row:** a disposition in the `--as` slug's own file, where CLOSED
      carries `by <sha>` of the branch commit that flipped it;
    - **text amendment of an existing row:** relocated only if it is a path repoint (D9). Anything else
      is listed for a human, because that text is now someone else's record;
    - **row already present on the default branch:** no-op.
  - It restores the views from the default branch, re-renders them, and prints a conservation table.
    It REFUSES to finish while any row is unclassified.
- **`--ingest <ref>`** is the same delta engine, run from the default branch for a straggler nobody
  will revisit: an abandoned branch, or one on another node.
- **The branch has no build folder.** `--as <slug>` creates a filing home (§2.4) for that session slug.

### 18.5 What it does not cover (stated)

- **Only nodes whose primary tree has fast-forwarded the default branch** run the new hooks. Until
  then, G7 from any fetched node and G6 on the default branch are the net.
- **`--no-verify` skips G1 to G3.** G4 and G6 still bind, and G7 reports the branch.
- **A straggler on another node, never fetched here, is invisible here** until fetched. D10 stays
  necessary.
- **Adopters' hooks are their own.** The hook bodies ship in the kit's hook guidance, and each adopter
  wires them in its own DEPL build.

### 18.6 Units and ordering

- **U3 gains** `--stragglers` and `--relocate`, beside `--ingest`.
- **NEW U4b (Tier-2):** G1 to G5 and G7's drift signal. It lands BEFORE U5 and dormant under P1, so the
  guard is already live on every node that has pulled main at the moment the flip lands. The hook
  test files gain staged-RED arms: a fixture repo whose default branch is in builds mode, and a
  pre-flip branch staging a shard edit.
  - The hook must refuse with the recipe.
  - Breaking the predicate must turn the test red.
- **U5 adds** a real-tree staged-RED of G1 against a scratch pre-flip branch.

## 18 rev-2. D11 made fleet-wide and time-independent (owner, 2026-09-13), SUPERSEDING §18.1-18.6

**The owner's emphasis.** "Old branches exist OUTSIDE of just this node and may be merged LATER." §18
leaned on this node's global hooks, and that is not a guarantee:

- a node that has not pulled main runs OLD hook files;
- a merge can happen months after the flip, on any node.

The guarantee must come from something every pre-flip lineage carries INTO the merge. The merge that
joins an old branch to new main always brings the NEW kit into the MERGED tree. So every check below
runs from that merged tree or from main's history, and never from the old branch's tree.

### 18r.1 Measured git behaviour (scratch lab `scratchpad/gitexp/run.sh`, git 2.54.0.windows.1)

| Operation | Attributes and merge driver used | Hooks that fired |
|---|---|---|
| merge post-flip main INTO an old branch | the OLD branch's (the old row driver ran) | pre-commit, when the merge is concluded by `git commit` |
| merge an old branch INTO post-flip main | the NEW main's | pre-merge-commit on a clean merge, with `MERGE_HEAD` NOT yet written; pre-commit on a conflicted one |
| `git merge --squash old` onto main | the NEW main's | pre-commit only; no merge link is recorded |
| `git rebase main`, and `git pull --rebase`, on an old branch | the NEW main's during the replay | `pre-rebase` fires in BOTH, with the upstream as argv |
| a feature push of an old branch | not applicable | pre-push |

### 18r.2 Seven layers, strongest first

| # | Layer | Where it runs | Why it reaches a branch on ANY node at ANY time |
|---|---|---|---|
| L1 | **Transition-merge audit.** Runs in the full hygiene run, on an unguarded bar leg (§18r.2.1) | every bar run on every node that has the merge; pre-push on a default-branch push | it reads main's HISTORY, so it does not care which node merged, when, or whether that node had hooks |
| L2 | **The same check at commit time.** The hygiene engine's `--staged` mode runs it whenever `MERGE_HEAD` exists and one parent is in shards mode | pre-commit, when a conflicted merge is concluded | the hook resolves the engine through `$top`, so after the merge it runs the NEW engine from the merged tree, even when the node's own hook file is years old. Any gov hook that runs hygiene on memory-staged commits is enough |
| L3 | **The post-flip row driver refuses a shard-into-view merge.** `memory/backlog/*.md` KEEPS `merge=rows` rather than being retargeted, and `builds/*/BACKLOG.md` is ADDED. The new `merge-rows.py` recognises "one side is a generated view, the other an authored shard" and fails closed with a banner carrying the recipe | whenever main's attributes govern: merge INTO main, squash, rebase, `pull --rebase` (all measured) | it is the same driver NAME every gov node already configured (`merge.rows.driver`), so nothing new has to be wired |
| L4 | **An in-conflict banner.** The view's header carries the recipe | when the OLD branch's attributes govern: its old driver conflicts because main rewrote the whole file, and the conflict shows main's header | it is pure content and needs no code on the old branch |
| L5 | **Early instruction on the branch's own node.** Global `pre-commit`, `pre-rebase` and `pre-push` bodies use the §18.2 predicate, and a primary-tree SessionStart step runs `--stragglers` over that node's LOCAL refs | a node that has pulled main | a courtesy, not the guarantee: it reaches unpushed branches on their own node once that node updates |
| L6 | **Fleet inventory.** `--stragglers` over local and remote-tracking refs, plus a drift signal `backlog_stragglers` (report-only, with liveness) | every node's drift run, forever | every node sees every PUSHED straggler |
| L7 | **Remote CI.** L1 and check 9 run as REQUIRED checks on `origin/main` | GitHub | the only layer no node can skip. It does not exist today, and wiring it needs a workflow-scoped push |

#### 18r.2.1 How L1 works

- **What counts as a transition.** Any merge in HEAD's history whose tree is in builds mode and which
  has a parent in shards mode.
- **What is checked.** That parent's changes to `memory/backlog/`, from the merge base up to the
  shards-mode parent, must be ACCOUNTED FOR in HEAD's tree (§18r.3). If they are not, L1 reds and
  prints `migrate_backlog.py --repair <merge-sha>`.
- **Why it catches late losses.** A loss that landed through `--no-verify` reds the next bar anywhere,
  and is repaired FORWARD without rewriting history.
- **No flip sha needed.** It classifies merges by the CONTENT of their parents' `.memory-tree.conf`.
- **Cost.** Per-merge deltas are immutable, so they are cached under the git dir.

### 18r.3 What "accounted for" means (mechanical, and it survives later edits)

For each changed row in a transition delta:

- **A new id.** The id has an ask row somewhere in HEAD's `builds/*/BACKLOG.md`.
- **A status flip or a text edit of an existing row.** Some ask or disposition in HEAD cites the SHA
  of the old-branch commit that made the change, for example `- CLOSED · TOOL-x-3 · by <sha> · …`. A
  path-only edit also counts when the ask text now carries it (D9).
- **A deliberate drop.** It is recorded as `- WONTDO · <id> · by <sha> · dropped at relocation: why`.
  There is no waiver registry; the record grammar carries it.
- **Why citations survive.** A later REOPEN cancels a named record rather than deleting it, and later
  text edits leave the sha in place.
- **Who writes them.** `--relocate`, `--ingest` and `--repair` write these citations; nobody types
  them.

### 18r.4 The recipe, identical in every banner and message

```
This branch predates the per-build backlog. Its edits to memory/backlog/<F>.md must be relocated, not merged.
  git merge <default>          # MERGE, never rebase or squash: those leave no merge for the audit to check
  python tools/memory-tree/migrate_backlog.py --relocate --as <your-slug>
  git add memory/ && git commit
Already landed without this? Any node:  python tools/memory-tree/migrate_backlog.py --repair <merge-sha>
```

### 18r.5 Permanence

A pre-flip lineage can surface at any time: from an offline node, an old clone, or an adopter's fork.
So these are PERMANENT, and none of them retires with the shards-mode code path:

- L1;
- the legacy shard parser;
- `--relocate`, `--ingest` and `--repair`;
- the row driver's shard recognition.

L1 costs one `git cat-file --batch` over merge commits, plus the cached deltas.

The flip's own landing merge is itself a transition: main pre-flip, against the build branch. So L1
also audits that the rows main gained during the build were carried across.

### 18r.6 Holes that remain (stated)

1. **A history rewrite that DROPS rows.** A rebase, squash or cherry-pick of an old branch whose
   conflict is resolved by discarding the incoming rows leaves no merge for L1 to see.
   - L3's banner and L5's `pre-rebase` refusal instruct against it.
   - Nothing mechanical stops someone deliberately discarding content.
2. **`--no-verify` with no CI.** A bad merge LANDS, and L1 then reds the next bar on every node until
   someone runs `--repair`. It is detected after landing and repaired forward. L7 would close it
   before landing.
3. **A shallow clone.** It cannot walk history, so L1 skips with an announcement, the same way
   `BASE_RESOLVE_CUTOFF` does. A CI checkout serving L7 must fetch full history.
4. **An unpushed branch on a node that never runs a post-flip session.** It is invisible until it
   merges; at that moment L1 to L4 apply.
5. **Two nodes repairing the same transition at once.** They write the same ask twice. V3 (one ask
   per id) reds after the merge, and one edit fixes it.

### 18r.7 Units

- **U1:** L3 (the row driver's shard-versus-view refusal) and L4 (the view header's banner).
- **U2:** L1 and L2 (the transition audit, in full and `--staged` modes), with staged-RED arms in a
  fixture repo, one per row of the §18r.1 table.
- **U3:** `--stragglers`, `--relocate`, `--ingest` and `--repair`.
- **U4b:** L5 (the hook bodies and the session-start inventory) and L6 (the drift signal).
- **NEW U9, an owner decision:** L7, remote CI with L1 and check 9 as required checks.
- **D10 is demoted.** Draining known branches first reduces repair traffic; it is no longer what
  makes the flip safe.

## 19. Ask-driven unattended runs (D12)

**The requirement, verbatim (owner, 2026-09-13).** "Unattended kit needs to be brought in scope to
ensure that there is enough information to just point an unattended session (prompt or slug) at the
ids/slug to thoroughly execute a build to completion."

Sources: the three reader reports `scratchpad/unattended-{contract,driver,practice}.md`, and one new
measurement, `scratchpad/d12_anchor27.py` (read-only). Driver line numbers were re-read at `09a22d2b`.

**The design in one paragraph.**
- **The ask supplies WHAT:** its observable, pointer, acceptance and cut-line.
- **The owner's act supplies WHICH:** a slug, an id list, or a prompt naming either.
- **Records reachable at the remote-observed BASE supply AUTHORITY**, and nothing the run writes can add
  to it.
- **Completion is DERIVED** by the same fold that renders the family view.
- **Units link to asks with the ratified `closes`/`advances` verbs.** This makes the drift the practice
  reader measured impossible by construction: 12 of the 15 asks answered by a CLOSED unit still read
  OPEN.

### 19.1 Facts that bind this section

| # | Fact | Evidence |
|---|---|---|
| K1 | Every start path and every verb is addressed by slug. Nothing accepts ids, and an id passed as a slug fails 6 | `tools/unattended/SKILL.template.md:54-59`; `VERBS_SLUG` at `unattended.sh:87`; fail 6 at `:1357-1360` |
| K2 | A unit carries its FOLDER's slug, so a foreign ask id can never be a unit | `roster_ids` at `unattended.sh:1762-1777`; `unit_ids_of` at `:1806-1811`; `9528b80f` |
| K3 | The authorization scan reads four front-matter keys: `slug`, `authorized-by`, `playbook`, `pieces` | the awk at `unattended.sh:1375-1381` |
| K4 | `--plan` refuses a build that has a roster but no spec. Its terminal `next:` line knows nothing about asks | fail 19 at `:2059-2061`; `next:` at `:2182-2190`; measured on `aWeighedCanon` (contract §3.5) |
| K5 | The DoD has 12 core items, and none concerns asks. Two cannot be overridden | `DOD_CORE` at `:348`; `DOD_NO_OVERRIDE` at `:390`; `CORE_FLOOR="12:12"` at `.unattended.conf:64` |
| K6 | Gov admits the second anchor, and only for `prompt` and `recipe` runs | `.unattended.conf:110`; `SECOND_ANCHOR_MODES` at `unattended.sh:497` |
| K7 | Three runs out of 50 builds were pointed at foreign ids. All three derived acceptance with no clarification, and 12 of the 15 asks they answered still read OPEN | practice §6.3-6.4 |
| K8 | Of 153 decision and abort entries, 57 are information an ask could carry. 67 are the kit's or the fleet's | practice §5 |
| K9 | **All 27 hazard ids are anchored in unattended runs' own records.** These are the 27 live ids that check 13 would red if it counted `BACKLOG.md`. The anchors sit in 8 files, as 31 lines: 14 under `prompts/`, 10 under `build/` and 7 in specs. The three id-driven runs' hand-typed resolution tables account for 14 of the 27 ids | `scratchpad/d12_anchor27.py`; for example `memory/builds/dSealedTally/prompts/2026-09-04-prompt-DEPL-dSealedTally-1-0-run-mandate.md:26-31` |

### 19.2 Entry modes, and how each resolves to a mandate

| Invocation | Resolves to | `authorized-by:` | Folder written by | Anchor | Owner commits |
|---|---|---|---|---|---|
| **E1** `/unattended <slug>`, where a README exists at BASE | today's slug path. The mandated ask set M is the README's `asks:` key, empty when the key is absent. `unit` asks are roster, not M | `slug` | the owner, beforehand | default branch only (fail 50) | the folder, as today; or ONE line, `asks: …`, added to an existing README |
| **E2** `/unattended <id> <id>…` | the ids path. The run mints a fresh session slug and writes a new folder whose `asks:` is the list | `prompt` | the run | `published` (K6). Elsewhere, refused with the E3 recipe | nothing |
| **E3** `gen_build_index.py --new-build <slug> --asks <ids>`, then E1 | a scaffolded folder that no human authored, landed by the owner's own push | `slug` | the owner's attended session, through the scaffold | default branch | one generated README with no authored prose |
| **E4** `/unattended <filing-home slug>` | E2 over that folder's live asks at M-BASE. The filing home itself is never written | `prompt` | the run | `published` | nothing |
| **E5** `/unattended --prompt "<text>"` | the IDLIST is extracted from the text. A lone slug gives E1. One or more ids give E2, with the leftover prose recorded as the owner's cut-line. No ids gives today's prompt path | as resolved | as resolved | as resolved | nothing |
| resume, `--resume <slug>` | unchanged; the ask facts were pinned at preflight | recorded | none | none | none |

**Mixing is refused.** An invocation carrying a slug and ids together, or a prompt naming both, is
refused with the two legal forms printed. A run cannot extend a committed mandate, so a mixed
invocation has no honest reading. This is the same fence that refuses an ambiguous prompt value
today (`SKILL.template.md:204-220`).

```
IDLIST   := ITEM ( SEP ITEM )*
SEP      := " " | ", " | " and "
ITEM     := ID [ ".." DIGITS ]          ; EXMP-aFoo-3..5
          | "-" DIGITS                   ; continues the previous ITEM's family and slug
asks-key := "asks: " ID [".." DIGITS] ( " " ID [".." DIGITS] )*   ; canonical form, ONE physical line
```

- **Why the bare `-n` continuation exists.** An owner typed it: "build TOOL-aProvenReuse-3 -4 and -6"
  (`memory/builds/aClosedDocket/prompts/2026-08-31-prompt-TOOL-aClosedDocket-1.md:11`). It is resolved
  once, at invocation, and is never written into a record.
- **What `asks:` accepts.** Only the canonical form, which `expand_id_runs` (`unattended.sh:1985-2000`)
  and `_expand_ids` (`gen_build_index.py:500-517`) already expand.
- **Why one line.** Held to one line, the key anchors nothing (anchor ban,
  `UNATTENDED-PROTOCOL.md:246-251`). A YAML list would anchor every foreign id under this build.

**The mandate model: the protocol's four properties become six.** Today's four still stand: the
folder is asserted, it is reachable from BASE, only its shape is checked, and its mode is recorded
(`UNATTENDED-PROTOCOL.md:28-61`). Two properties join them. Both are checked against **M-BASE**, the
first anchor's merge-base `merge-base(ASHA, HEAD)` (`resolve_base`, `unattended.sh:887-917`). That
holds even when the README itself resolved at the second anchor.

- **P5: every mandated ask is a record the run did not create.** Each mandated id has its ask row,
  `^- <ID> · filed `, in `M-BASE:<M>/builds/<slug(id)>/BACKLOG.md`. That is one `git show` and a line
  match; filing is not status, so the driver still does not re-implement the fold
  (`lib-unattended.sh:18-19`). A run cannot satisfy P5 by construction without moving the remote's
  HEAD. An ask filed in an unpushed commit is therefore not mandatable: push it first.
- **P6: the ask set is pinned once and cannot move.** `asks:` is read from the README at BASE and
  pinned as the fact `asks:`, beside `playbook`/`pieces` (the pattern at `unattended.sh:2736-2741`).
  The README's `asks:` line must be byte-equal at HEAD. Units still grow through `--rescope add`; the
  ASK set does not grow at all.

What the owner's act grants:
- **Scope.** The mandated asks' texts and their `out` clauses, added to the goal bound in the README's
  problem slot. In E2 the run writes that slot as "the mandated asks, as filed at `<M-BASE sha7>`".
- **Authority.** The union of the `may` clauses on mandated asks, read at M-BASE only (§19.3). A clause
  written inside BASE..HEAD grants nothing.
- **Landing.** Unchanged (`UNATTENDED-PROTOCOL.md:94`).

**How small the owner's commit can be.**
- **E2 and E4: zero bytes.** The invocation is the act, as on today's prompt path.
- **E1 on an existing folder: one front-matter line.**
- **E3: one command.** The scaffold writes everything, including the readme-contract row and the five
  canon slots. The prompt path omits both today (G8, contract §7). It also refuses a slug that §2's
  all-time grep finds.
- **What cannot shrink further:** the ask rows themselves, which must already be on the default branch
  (P5). That is what makes E2 safe: the run chooses only among records it did not write.

**The residual, stated.** E2, E4 and E5 inherit today's prompt-path residual: the id LIST is witnessed
only by the prompt record the run writes (`SKILL.template.md:260-287`; driver report §8(b)2). A leg can
confirm that `asks:` equals the IDLIST extracted from that record, which catches a mistake and not a
liar. P5 bounds what a liar can reach: filed asks only. E1 and E3 carry no such residual.

**The ids path, end to end** (E2, the `dSealedTally` shape made mechanical):

1. The keepalive, first, as on every path.
2. `gen_build_index.py --asks --ready <ids>`. If every id grades `no`, stop without writing anything
   (§19.3).
3. The run writes the folder, the README and the prompt record in one commit, and pushes the branch.
   The README is written by `--new-build <run-slug> --asks <canonical> --mode prompt`, and the prompt
   record holds the invocation verbatim.
4. `--preflight`. It pins `asks:` and `asks-ready:`, checks P5 and P6, and reports the rows it read.
5. Orientation, per ask (§19.3). Each ask ends as a planned unit, a stale or duplicate disposition, or
   an owner-call park.
6. Roster rows, then specs carrying `closes`, ordered as §19.4 derives. Then M4's audit and the build
   loop.
7. Dispose of the build's own asks. Then `--close`, which runs `asks-disposed` (§19.5). Then the
   landing, and `--landed`, which freezes `asks-at-landing`.

### 19.3 Executability: the ask envelope and READY

| Practice field | Carried by | New? |
|---|---|---|
| F1: a resolvable id with its status visible | the ask row (§2.1) and `--asks` | no |
| F2: an observable claim, with the probe that re-observes it | the `seen` clause | yes |
| F3: durable pointers | `→ POINTER` | no |
| F4: acceptance | the `accept` clause. `seen` implies it for a defect | yes |
| F5: a cut-line | the `out` clause. An owner-held fork is a hold on an owner-call ask (§4.3) | yes |
| F6: an authority grant | the `may` clause, honoured only at M-BASE | yes |
| F7: holds and relations | BLOCKED, DEFERRED and WONTDO rows (§4.1) | no |
| F8: a verification route | the `verify` clause. Absent, it means the bar | yes |
| C1: a data boundary | the `data` clause, required when a pointer leaves the repo | yes |
| C2: a partial-landing rule | build-level, §19.5 T3 | — |
| severity | SEV rows (D7). A tie-break in ordering only: 0 of 56 run records used it (practice §7) | no |

```
ask     := "- " ID " · filed " DATE [" · unit"] " · " TEXT CLAUSE* [" → " POINTER]
scope   := "- SCOPE · " ID CLAUSE+                  ; an event row, in the WRITER's own BACKLOG.md
CLAUSE  := " · " LABEL " " VALUE
LABEL   := "seen" | "accept" | "out" | "may" | "verify" | "data"
seen    := LOCATOR [ " `" COMMAND "`" ]             ; LOCATOR := `repo-path`[":"LINE] | <repo>":"path"@"SHA7+
may     := "none" | GRANT ( " " GRANT )*            ; GRANT := `repo-path` | decision-ID
```

Illustrative rows, reusing §2.1's example ids; the line number is invented:

```markdown
- EXMP-aFoo-3 · filed 2026-09-12 · push-main.sh reports a gate RED as a network failure · seen `tools/push-main.sh`:212 · accept a RED bar prints GATE FAIL and exits non-zero · out retry policy · may none → `tools/push-main.sh`
- SCOPE · EXMP-cBaz-5 · accept 0 of 40 fixture runs double-count · verify the hygiene leg alone · may `memory/HYGIENE.md`
```

- **How the clause tail is parsed.** It is the row's suffix of ` · <label> ` segments, read right to
  left, and TEXT is whatever precedes it. A label appears at most once per row. A TEXT that happens to
  contain ` · accept ` is misread, and it shows up as V13 once the misread value fails its clause
  grammar.
- **SCOPE follows the SEV pattern (§17.3).** Triage never edits a foreign ask, and the rule is one SCOPE
  row per (file, target), as V4 rules for dispositions.
- **How clauses merge.** Values merge per label, over the ask row and every SCOPE row naming it.
  `seen`, `accept`, `out`, `verify` and `data` conjoin. `may` is a union in which `none` is absorbed.
- **SCOPE derives no status.** R1-R7 and V5 are unchanged.
- **A `seen` command is never run by default.** Ask text is written by whoever filed it, so executing it
  verbatim would be a new write-to-exec surface (charter §9; D12-e). The run READS the locator.

**READY**, evaluated at M-BASE over a mandated set M. The view with no set treats M as `{A}`.

```
R1 FILED       A has exactly one ask row, in builds/<slug(A)>/BACKLOG.md                    (F1; V1, V3)
R2 LIVE        status(A) is OPEN, BLOCKED or DEFERRED; or A is a `unit` ask of the target folder, not terminal
R3 UNHELD      every live hold on A names a target inside M, where it is ORDER (§19.4)          (F7)
R4 LOCATED     the POINTER or `seen` names a repo path present in the M-BASE tree, or an external LOCATOR (F3)
R5 ACCEPTABLE  A carries `accept` or `seen`                                                     (F2, F4)
R6 BOUNDED     an external LOCATOR or POINTER implies a `data` clause                          (C1)
ready(A) = yes     if R1..R6 all hold
         = legacy  if R1, R2, R3 and R6 hold, R4 or R5 fails, and `filed` < ASK_CUTOFF
         = no      otherwise
```

- **Why `legacy` exists.** The 499 live rows all predate clauses, and the three id-driven runs derived
  acceptance from rows like them without asking anyone (practice §6.3). A `legacy` ask is admitted and
  graded at orientation. A `no` ask never is.
- **Why SPECCED and INPROGRESS are `no` in R2.** Another build's unit is already on the ask, and a
  second unit duplicates the work. `TOOL-aProvenReuse-4` was answered by one build and credited to
  another (practice §6.4).

```
$ python tools/memory-tree/gen_build_index.py --asks --ready TOOL-aProvenReuse-3 EXMP-aFoo-3 EXMP-aFoo-4
| Ask | Status | Sev | Ready | Missing | Holds | Grant | Home |
|---|---|---|---|---|---|---|---|
| [EXMP-aFoo-3](memory/builds/aFoo/BACKLOG.md) | BLOCKED | HIGH | no | R3 | on TOOL-aWeighedCompass-3 | none | aFoo |
| [EXMP-aFoo-4](memory/builds/aFoo/BACKLOG.md) | OPEN | MED | yes | — | — | `tools/push-main.sh` | aFoo |
| [TOOL-aProvenReuse-3](memory/builds/aProvenReuse/BACKLOG.md) | OPEN | — | legacy | R5 | — | none | aProvenReuse |
asks: 3 examined · 1 ready · 1 legacy · 1 not ready · at the working tree
```

- **`--tsv`** prints one line per ask: `ask⇥id⇥status⇥decided-by⇥home⇥sev⇥ready⇥missing⇥holds⇥grant⇥closers`,
  followed by `examined⇥<n>`.
- **`--at <rev>`** reads one tree through `git ls-tree` and `git cat-file --batch`. That is one tree,
  not history, so the rule at `gen_build_index.py:27` holds.
- **Both are print modes.** They write nothing and exit 0, as §5.3 rules for `--asks`.
- **The driver reads `--tsv`, not `--json`.** It has no JSON parser, and kit precedent is a TAB machine
  line (`plan_row`, `unattended.sh:2020-2023`). `--json` stays for drift-audit and for agents.
- **The first cell is link-wrapped**, so a pasted copy anchors nothing (K9).

**An ask that is not ready is parked. It is never guessed.**

- **At invocation, before any write.** If every mandated ask grades `no`, stop and print the missing
  rules. That is the prompt path's disqualifier stop (`SKILL.template.md:256-259`): nothing is staged,
  and there is nothing to abort.
- **After preflight, each `no` ask gets these rows, in one commit, in the run's own folder:**
  ```markdown
  - EXMP-dRun-9 · filed 2026-09-14 · owner call: EXMP-aFoo-3 is not ready (R5, no acceptance) · accept a SCOPE row naming EXMP-aFoo-3 carries accept, and this ask is CLOSED
  - SEV · EXMP-dRun-9 · MED · owner call
  - BLOCKED · EXMP-aFoo-3 · on EXMP-dRun-9 · not ready: R5
  - KEEP · EXMP-dRun-9 · awaiting the owner; V10 wants it disposed once this build is terminal
  ```
  It also gets `--park --item EXMP-aFoo-3 --reason "not ready: R5; held on EXMP-dRun-9"`. This is
  §4.3's owner-call idiom. The owner writes the SCOPE row and closes `EXMP-dRun-9`, the hold releases,
  and the next run finds the ask `yes`.
- **A `legacy` ask whose acceptance proves underivable at orientation** takes the same rows.
- **A `yes` ask whose locator no longer shows the defect is STALE, not unready.** The run records it as
  `WONTDO · A · stale: <locator> no longer shows it`, or as `CLOSED · A · by <pre-BASE sha or foreign
  id>`. §19.5 T5 surfaces both.
- **What the run never does:** guess an acceptance, widen `may`, or pick past M3's vetoes 2 and 3
  (`BUILD-METHOD.md:83-94`).

### 19.4 Roster derivation

**Slug mode (E1, E3).**
- **The roster.** It is the authored `roster:units` table together with the folder's `unit` asks.
  `roster_ids` (`unattended.sh:1762-1777`) reads both, through the same folder-slug filter.
- **What that buys.** A `unit` ask that has no table row still shows as MISSING in `--plan`, and it
  still refuses `build-complete` term 3.
- **What the slug alone does not mandate.** The folder's non-`unit` asks are leftovers, outside the goal
  bound, until an `asks:` key names them.

**Ids mode (E2, E4, E5).**
- **Where units are minted.** Under the run's own folder slug, in the family of the ask each one
  closes. Never under the ask's slug (K2; §8's charter §2 exception).
- **One unit per mandated ask, by default.** Its spec header carries `closes <ask>`, or
  `advances <ask>` when the unit answers only part of it (§2.2).
- **Grouping.** It is allowed in exactly two cases:
  - orientation records two mandated asks as the same defect, so one unit `closes` them all. The
    `--landed` ordering defect was filed four times (practice §6.4);
  - two asks share a POINTER file and the joint change is still one Tier-1 diff (charter §1).

  Grouping is written ONLY as the `closes` list, so no second carrier can disagree with it.
- **Coverage.** Every mandated ask is named either by exactly one `closes`/`advances` of a unit of this
  build, or by one disposition in this build's `BACKLOG.md`. Two live units of one build closing the
  same ask are a refusal row in `--plan --asks`.
- **Before any spec exists.** Planned units are rows of the authored roster table. `--plan` lists them
  as MISSING even when there are zero specs, which fixes K4: fail 19 now fires only when the roster is
  empty too. A `unit` ask is optional, filed only for a unit that must stay visible in the family view
  beyond this run.
- **Adopting a foreign ask mid-run** (for example, a prerequisite found at orientation). The unit that
  takes it is added with `--rescope --act add`, which check 24 already demands for a unit entering
  after BUILDING (`check-unattended.sh:2180`). That unit's spec `closes` the ask.

**Order.**
```
1  holds: an edge B → A when A carries a live BLOCKED on / DEFERRED until naming B, and both are in M.
   Topological order; a cycle is V6.
2  within a layer, SEV rank: BLOCKER > HIGH > MED > LOW > unlabelled
3  then position in the pinned asks: fact, which is the owner's own listing order
4  then numeric <seq>, never the string sort that puts -10 before -2 (gen_build_index.py:865-866)
The order is computed over UNITS: a hold edge between two asks lifts to the units that close them,
and steps 2-4 take a unit's most severe, earliest-listed, lowest-seq ask. The run writes the result as
`order <n>` in each spec header (memory/TEMPLATE-SPEC.md:77-83).
```

- **A new refusal under code 49.** `--dispatch` refuses a unit that closes A while a mandated ask B,
  which A holds on, is not yet terminal. The order gate that this joins already exists
  (`unattended.sh:4699-4720`), but it enforces only declared orders.
- **SEV is only a tie-break.** Runs have chosen by dependency, size and tier
  (`memory/builds/aTunedCompass/RUN.md:63`). Holds carry the dependency, and SEV decides what lands
  first when a run cannot finish everything.

**`--plan --asks`** is an OUTPUT MODE, the way `--paths` is. A new verb would owe four carriers under
check 26 (`check-unattended.sh:2488-2528`).
- **The ASK rows.** One per mandated ask: its id, derived status, readiness, the unit or disposition
  covering it, and its rank.
- **Under `--paths`**, an ASK row carries exactly three TAB fields: `ASK`, the id, and a `k=v;…`
  summary. Every existing caller skips any line with fewer than four fields (`unattended.sh:2017-2018`),
  so the harness can never dispatch an ask as though it were a unit.
- **One new `next:` shape**, printed only after every unit shape is exhausted:

  ```
  next: EXMP-aFoo-3 (UNDECIDED - plan a unit that closes it, or dispose it)
  ```
- **The false "done" goes away.** `next: none - every tracked spec is terminal` is never printed while
  an ask in M, or an OPEN ask filed in this folder, is undecided.
- **The existing literals stay byte-identical.** Check 30 parses them (`check-unattended.sh:3215`).
  `--status` and `--resume` read the same ask-aware next (`unattended.sh:2810`, `:2892`).

### 19.5 Completion: the `asks-disposed` item

A 13th core item, `asks-disposed:machine`. Its scope is M plus every ask filed in this build's own
folder, which absorbs U4's "closeout step behind conf" (§15).

```
T0  no mandate: no asks: fact, and no ask in the folder at BASE
      -> MET and announced (the pieces-complete idiom, unattended.sh:3117-3120)
T1  a mandate while ASKS_CMD is blank
      -> refused at --preflight, never discovered here
T2  run `ASKS_CMD <scope>` on HEAD through run_bounded; one row per id, and examined = |scope|
      -> otherwise DEAD PROBE, refused
T3  each A in M must be one of:
      CLOSED or WONTDO;
      live and held (BLOCKED on / DEFERRED until) by a row in THIS folder;
      KEEP in THIS folder, where a CLOSED unit of this build `advances` A (a delivered partial).
    each A filed in the folder carries a disposition (V10's rule, enforced here without the override)
T4  A derived CLOSED `by <sha>`, with the sha in BASE..HEAD
      -> refused unless that sha is a CLOSED unit's build commit (build_commit, lib-unattended.sh:207-285)
T5  each A in M that is NOT derived CLOSED by a CLOSED unit of this build
      -> named by an owed-class park row in RUN.md (decision, or rescope retire/supersede)
```

- **Why T4.** A disposition that closes a mandated ask with the run's own in-range commit is product work
  with no unit. Pass-order, brief-recorded and specs-audited never grade it, because all three grade
  CLOSED units only (`check-pass-order.sh:341-346`; driver report §0.8).
- **Why T5.** A mandated ask that ends anywhere other than "closed by our unit" is scope the run did not
  deliver: declined, found stale, held, or closed with someone else's evidence. The argument is
  `PARK_ACTS_OWED`'s (`unattended.sh:370-382`): M3 delegates scope RESOLUTION, never scope
  abandonment. `parked-decisions-surfaced` then counts these without being widened.
- **KEEP on a mandated ask is refused, except after a delivered partial (D12-c).** KEEP means "still
  wanted after this build closed; outside its goal" (§2.1), and a mandated ask is inside the goal by
  definition.
- **The item cannot be overridden (D12-b).** The `pieces-complete` argument applies word for word: "the
  item that says the run produced what the owner asked for" (`unattended.sh:383-390`). Holds are the
  legitimate escape, and each one is surfaced.
- **The witness.** The driver parses `--asks --tsv`, the TAB projection of the same fold that renders
  the family view (§19.3). The kit holds no second implementation of status.
- **The freeze.** `--landed` writes `asks-at-landing: <id>=<status> …` on one line, beside
  `units-at-landing` (`unattended.sh:2435-2437`). D4 made CLOSED non-absorbing, so without a freeze a
  landed record's answer would change when someone later REOPENs the ask. That is the rationale of
  protocol `:211-214`.
- **Carriers that move.** `CORE_FLOOR` becomes `12:13` (`.unattended.conf:64` and the example).
  Protocol §4 gains a row and its "Twelve" sentence changes (leg check 16). `DOD_NO_OVERRIDE` gains
  the item.

**With D6 (the closeout verdict, V10).**
- **When V10 starts to red.** From the commit that makes the build derive terminal, which is the commit
  closing its last unit (`gen_build_index.py:635-654`; driver report §9). So the run disposes of each
  discovery in the commit that files it, or at the latest in that last closing commit.
- **What T3 adds.** Its second clause is V10, enforced at `--close` without `gates-green`'s override.
- **Foreign mandated asks.** V10 binds them only when their own build is terminal. The U3b sweep gives
  each of those a triage disposition, often KEEP. T3 asks for more than that: a closing unit of this
  build, or a hold written here.

**With D4 (REOPEN).**
- **A mandated id already terminal at M-BASE** grades `no` (R2). If orientation's locator still shows
  the defect, the run writes `- REOPEN · A · of <the closing record> · still observed at <locator>` in
  its own file, parks it (T5), and treats A as live. Closing A again needs NEW evidence (§17.1), which
  this run's unit supplies.
- **A REOPEN arriving through the lander's reconcile, after `--close`,** leaves A live in the landed
  tree. `asks-at-landing` is computed at `--landed` on that tree, so it records this truthfully. The run
  is not re-graded.
- **A later REOPEN naming this run's spec** is a quality signal for the run. Drift can count "mandated
  asks REOPENed after landing" per build, from the frozen fact.

**With D7 (SEV, V12).** Every ask the run files after `ASK_CUTOFF` needs a SEV row, or `gates-green`
reds at close. That covers owner-call asks, discoveries and `unit` asks. The Skill says to file the SEV
row in the same commit as the ask.

### 19.6 Discoveries

Protocol §11's three dispositions keep their tests (`UNATTENDED-PROTOCOL.md:583-611`); only the records
change. Every record is written in the run's own folder and minted under the folder slug.

| Discovery | Test | Record |
|---|---|---|
| strictly beneficial, inside the goal | clauses 1-3 pass | ADOPT: `--rescope --act add --item <F>-<slug>-<n>` plus a spec, which `closes` any pre-existing ask it answers |
| declined | fails clause 1 or 2 | FILE: an ask row carrying `seen` and `accept`, a SEV row, and a KEEP no later than the last closing commit |
| trips a veto | M3 veto | PARK: an owner-call ask with its SEV, a hold on it for every mandated ask it blocks, and `--park` |
| a pre-existing ask found stale, duplicated or already fixed | orientation | `WONTDO · X · duplicate of Y`, or `CLOSED · X · by <pre-BASE evidence>`. T5 surfaces it when X is in M |

- **A pass may write its own build's `BACKLOG.md`.** It declares it through `--dispatch --writes`: the
  file sits inside the build folder and does not overlap `RUN.md` (`lib-unattended.sh:100-105`). Two
  concurrent passes still cannot both declare it (condition 1, `unattended.sh:4853-4869`). That
  removes the three blocked filings the practice reader found: `aLeakedHandle/RUN.md:67`,
  `aHoistedPass/RUN.md:79` and `aWeldedTribunal/README.md:49`.
- **A discovery is filed with its clauses already in hand.** The filer is usually a run: 259 run-slug
  ids appeared inside 39 run windows (practice §5). Filing `seen` and `accept` at the moment of
  discovery is how the next run finds that ask graded `yes` (practice §8 item 4).
- **A foreign path repoint (D9) rides a commit whose subject names no unit id.** `build_commit` picks a
  commit by a whole-token subject match plus any path outside the build folder
  (`lib-unattended.sh:276-282`). A repoint inside a commit that names a unit would therefore become
  that unit's build commit, and pass-order would then grade that commit's parent.

### 19.7 The two carried risks, as they reach a run

**Check 13 skipping `BACKLOG.md`** (§6, check 13; `corpus_ids.py:622-627`).
- **The cause, measured.** K9: every one of the 27 is a run's own anchor, and 14 come from the three
  hand-typed resolution tables. A row like `` | `DEPL-dRatifiedSeam-2` | … | `` is an anchor, because
  `A_TABLE` admits a backticked first cell (`tools/memory-recall/extract.py:120`). D12 makes that the
  normal case, so without a rule every ask-driven run adds to the 27.
- **Layer 1: the run never types a resolution table.** Its records cite mandated ids inline in prose,
  or paste `--asks --ready`, whose first cell is link-wrapped (measured non-anchoring, §5.3). This is
  the protocol's anchor ban (`UNATTENDED-PROTOCOL.md:246-251`) widened from `RUN.md` to the whole
  folder.
- **Layer 2: the leg enforces it (U13).** No line in the run's folder may anchor an id whose ask row is
  filed in another folder, judged by the real `extract` shapes.
- **A refinement to the ratified change (D12-g).** Once `def_builds` ignores `BACKLOG.md`, a single
  foreign anchor reds nothing anywhere, because the ask's home no longer counts as a claim. Scoping the
  skip to asks filed before `ASK_CUTOFF` keeps the 27 legacy anchors quiet and brings check 13 back for
  every ask filed afterwards. It reads the ask's own `filed` field, so no waiver list is needed.
- **Resolution never goes through recall.** The 27 are exactly the ids whose recall anchor sits in the
  wrong build. The resolver reads `--asks`, which answers with V1's home.

**Filing homes (§2.4).**
- **Today.** `/unattended aFlaggedScaffold` fails 6, 46 and 9 at preflight (`unattended.sh:1357-1360`,
  `:2625-2629`, `:2677-2681`).
- **Under D12 it is E4.** The Skill finds no README at M-BASE and exactly one `BACKLOG.md`, lists that
  folder's live asks with `--asks --build <slug> --at <M-BASE>`, and continues as E2 under the run's
  fresh slug. Fail 6's message names this route (U11), so a mistyped invocation explains itself.
- **The run never writes into a filing home.** Minting there would put a node-d run's ids under a
  node-a slug, which breaks §2's by-construction disjointness. It would also force every new sequence
  number above every filed ask's, or V9 reds. D12-f records the alternative. The homes that
  `--relocate --as` creates (§18.4) are treated the same way.

### 19.8 Units, slotted into §15, §17.4 and §18r.7

- **Every unit lands before U5, and DARK.** The kit default for `ASKS_CMD` is blank, meaning "not
  adopted". It is announced and skipped, the way `RECALL_CLI` is (`UNATTENDED-PROTOCOL.md:474`).
- **Gov stays in `shards` mode until U5,** so no `BACKLOG.md` exists for the new code to read.
- **U15 arms everything after U5.**

| # | Unit | Tier | Lands green because | Depends |
|---|---|---|---|---|
| U10 | **memory-tree.** In `backlog.py`: the clause tail and SCOPE rows; the READY predicate; `--asks --ready`, `--tsv` and `--at <rev>`; V13 (clause grammar; a SCOPE row targeting something that is not a filed ask); V14 per D12-d. `--new-build <slug> --asks <ids> [--mode]`, a scaffold that writes a conforming README, its readme-contract row and the `--write` render, closing G8 for the prompt path too. The check-13 refinement per D12-g | 2 | the print modes write nothing; the verdicts fire in builds mode only; the scaffold writes only when invoked | U1, U2 |
| U11 | **The driver, made ask-aware.** `ASKS_CMD`, with its conf entry, example entry, protocol §8 row and leg check 22. `asks:` in the one scan (`:1375-1381`). At preflight: P5, P6, READY at M-BASE, and the facts `asks:` and `asks-ready:`. The subset and byte-equality rules. `roster_ids` ∪ `unit` asks. `--plan` over a zero-spec roster, and numeric order for MISSING. `--plan --asks`, the UNDECIDED shape, and an ask-aware `--status`/`--resume`. `--rescope`: retiring a `unit` ask, and refusing an add that reuses a non-`unit` ask's id. The `--dispatch` hold refusal. Fail 6's filing-home message. A preflight notice when `BACKLOG_MODE` differs between ASHA and HEAD (driver report §9) | 2 | every new branch sits behind a non-blank `ASKS_CMD` or an `asks:` key, and no gov README carries one | U10 |
| U12 | **The DoD.** `asks-disposed` T0-T5; `DOD_NO_OVERRIDE`; `CORE_FLOOR` to `12:13`; `asks-at-landing`; the protocol §4 row. A companion guide, `UNATTENDED-ASKS.md`: kit template, install, and a byte-compare pair beside the VERBS pair (`check-unattended.sh:1580-1600`). It carries §19.2-19.6 as contract text | 2 | T0 is MET and announced on every existing build; the floor moves in the same commit as the item | U11 |
| U13 | **The leg's second opinions.** The `asks:` fact against the README at the recorded BASE (check 19's pattern, `check-unattended.sh:1395-1418`). P5, re-derived. The folder-wide anchor ban on foreign ask ids. `asks-at-landing` present on every LANDED record that carries a mandate | 2 | every arm is vacuous when there is no `asks:` fact, and each arm announces its skip | U11, U12 |
| U14 | **Carriers.** Skill routing rows E1-E5 and the zero-turn ids steps. Orientation: re-observing `seen`, stale and duplicate dispositions, the REOPEN rule. Owner-call parking; discovery filing with SEV and closeout timing; the repoint rule; the relocate recipe for a pre-flip BASE. A note in BUILD-METHOD M2 that the `closes` list is the grouping carrier. `unattended-build.js` passes each unit's `closes` ids into its SPEC brief. The stale sentences in contract §8 | 1 | the template byte-compare legs and check 26 | U11-U13 |
| U15 | **ARM, after U5.** Gov sets `ASKS_CMD`. Stage RED on the real tree, confirm, and unstage, for three cases: preflight on an unfiled id; `asks-disposed` on a fixture run with an undisposed mandated ask; the leg on a typed resolution table. Then the first ask-driven pilot, over a READY set the owner picks | 1 | U5's views exist; the pilot's own DoD is the witness | U5, U14 |

- **What moves in the existing plan.**
  - U4 loses its "`--close` closeout step" to U12, which does that job without an override.
  - U4 keeps the two-key refusal, the `build_commit` comment rewrite and the M6/M9 text.
  - U4b's L5 hooks are unaffected.
- **U5 gains one staged RED:** V13 on a malformed clause.
- **U6 gains the charter sentence the contract reader found stale.** "A committed build folder the run
  did not create" (`AGENTS.md:129`) is false for every prompt-mode run, and E2 is one. The edit must
  stay net-negative in the template.
- **Protocol budget.** The protocol is 57,815 B and 666 lines, against the guide cap of 61,440 B and 750
  lines (`check-memory-hygiene.sh:84`). The §4 row fits. Everything else goes to the companion, on the
  §7 precedent (`UNATTENDED-PROTOCOL.md:437-439`).
- **Self-tests.** U11, U12 and U13 add shell `fail` branches, and each branch needs its arm, with an
  `ARMS_FLOORS` move, in the same commit. Charter §7 also requires every failing case to be OBSERVED.
  The standing instruction not to run the unattended self-tests collides with that; see D12-h.

### 19.9 Owner decisions this raises

| # | Question | Options | Recommend, and why |
|---|---|---|---|
| D12-a | How strong must E2 be? | (a) E2 as specified: prompt-mode strength plus P5, zero owner commits. (b) Ids always go through E3, so the owner lands the scaffold first. (c) Both: E2 where `ANCHOR_SCOPE=published`, E3 elsewhere | **(c).** (a) alone strands adopters whose anchor scope is blank (`.unattended.conf.example:128`). (b) alone costs a push per run for a list the owner already typed |
| D12-b | May `asks-disposed` be overridden? | (a) No; holds are the escape, each one surfaced. (b) Yes, as `gates-green` may | **(a).** It is the item that says the run made what was asked for |
| D12-c | KEEP on a mandated ask? | (a) Refused, except after a CLOSED unit of this build `advances` the ask. (b) Always allowed | **(a).** Otherwise KEEP is a silent way to not do the work |
| D12-d | Grade readiness at filing? | (a) Report-only: `--ready`, plus a drift watermark on the `no` count. (b) A forward-only verdict, V14: an ask filed on or after `ASK_CUTOFF` carries `seen` or `accept` | **(b).** It matches the owner's D6 and D7 choices, and the filer, usually a run, has the evidence in hand. `may`, `out` and `verify` stay optional |
| D12-e | Execute `seen` commands? | (a) Never: `seen` is a locator the run reads. (b) Only commands under a conf prefix list, `PROBE_ALLOW` | **(b), shipped blank**, which is (a) until a project declares a list |
| D12-f | Filing-home targets? | (a) E4: a new folder under the run's slug; the filing home is untouched. (b) The run writes a README into the filing home and mints under its slug (driver report §8(a2)) | **(a).** (b) breaks cross-node slug ownership and inherits V9's sequence constraint |
| D12-g | Scope the ratified check-13 skip to asks filed before `ASK_CUTOFF`? | yes, or keep the blanket skip | **Yes.** No waiver is needed, and it restores the forward check the blanket skip loses (§19.7) |
| D12-h | Self-tests for U11-U13? | (a) Lift the standing instruction for these three units only. (b) Keep it: observe each failing case by hand, by running the driver verb itself in a scratch fixture repo with a local bare remote, which is not a self-test. Record it in the unit's build record, and run the suites once, owner-run, as U15's landing gate | **(b).** It keeps the instruction and still satisfies charter §7 |
| D12-i | The kit's own half: 67 of 153 entries and 10 of 15 aborts no ask can carry (practice §5, §8). `push-main.sh` refusing a worktree alone left 4 records stuck at LANDING or BUILDING (practice §2.1) | (a) Put the landing blockers inside D12. (b) A separate build | **(b).** They share no code with asks. D12's "to completion" is still bounded by them, as §19.10 says |

### 19.10 What this does not solve (stated)

1. **The id list on E2, E4 and E5** is witnessed by a record the run writes (§19.2 residual).
2. **Over-claims are not caught.** An over-claiming `closes`, or a false `CLOSED by <foreign id>` on a
   mandated ask, goes through. T5 makes it visible to the owner, which is not a refusal (§16 risk 1).
3. **Mid-run owner turns remain.** At least 18 of 50 builds took one (practice §1). Better asks remove
   the 37% of stops that are ask-carriable. The rest is D12-i.
4. **A `legacy` ask carries no mechanical acceptance.** The run's orientation judgement is the gate,
   backed by `acceptance-underivable` and the park.
5. **Late arrivals at landing go unexamined.** A REOPEN or a new hold that arrives through the landing
   reconcile is recorded by the freeze, and nothing re-runs the build.

## 18 rev-3. Amendments from the bypass hunt (adopted 2026-09-13)

**Source.** The lab is `scratchpad/bypasslab`, and the report is `critique-straggler.md`: 25
bypasses, of which 1 is a blocker and 6 are high.

- **A1: classify a transition by lineage, not by the tip (this fixes the blocker).**
  - A merge is a transition when some parent P has a commit in `merge-base --all(P, others)..P` whose
    OWN tree is in shards mode and which touches `memory/backlog/` or `memory/archive/`.
  - It does not matter what P's tip conf or the merge tree reads. A straggler that pulled main's
    `.memory-tree.conf` early can no longer blind L1.
  - L5 uses the same predicate in place of §18.2's P2.
  - The key name `BACKLOG_MODE` and its spelling are frozen forever.
- **A2: `.gitattributes:65` (`memory/backlog/*.md merge=rows`) is KEPT.**
  - §7, §9 step 10, §11 and U5's "retarget" are corrected to "ADD `memory/builds/*/BACKLOG.md
    merge=rows`".
  - A repo-subject assertion checks that `git check-attr merge memory/backlog/TOOL.md` reads `rows`.
  - Without the attribute, `-X ours` merged clean and dropped a flip (e04g2).
- **A3: L1 gets a liveness guard.**
  - It prints `transitions examined N`, and reds as a DEAD PROBE when N=0 on a builds-mode tree. The
    flip's own landing merge guarantees N≥1.
  - The transition set and each verdict are pinned in a shrink-only repo registry, graded by the
    unguarded `memory hygiene` leg.
  - There is one staged-RED arm each for L1 and L3, in a REPO-subject leg rather than a held kit
    self-test.
- **A4: accounting uses a provenance row the fold ignores:**
  `- RELOCATED · <id> · by <sha> · kept|dropped|amended: why`.
  - Each changed row needs exactly one.
  - WONTDO is FORBIDDEN as an accounting record, because it would decline a live ask. That was the
    old §18r.3 wording, and it also violated §2.1.
- **A5: the L1 delta also spans `memory/archive/`.**
  - A REMOVED row needs a provenance row.
  - After the flip, any tracked backlog archive is a check 9 verdict (D8). Test e08 showed a
    rotated-away CLOSED flip landing clean.
- **A6: criss-cross histories.**
  - A row version counts as a straggler change only if it differs at EVERY merge base, and main's
    history never held it.
  - `--repair` refuses to write any record that changes an ask's current derived status without
    explicit confirmation. In e09b it had written CLOSED over main's deliberate reopen.
- **A7: L2's carrier is the `commit-msg` hook.**
  - It sees `MERGE_HEAD` on concluded merges.
  - pre-commit runs hygiene only when `memory/**` is staged, and on a clean merge only
    pre-merge-commit fires.
- **A8: squash and rebase landings erase the transition merge (e10, e14).**
  - L5's pre-push runs L1 over a pushed FEATURE branch and refuses an unaccounted transition before it
    can be squashed away.
  - L6 keeps flagging a straggler ref until its shards-mode backlog commits are accounted for on
    `origin/main`, judged by CONTENT, not ancestry.
  - Remote enforcement is D11-b.
- **A9: shallow checkouts.** L1 refuses on one as a DEAD PROBE and never reports a reassuring zero.
  L7's CI checkout fetches full history.
- **A10: an unattended run never performs a relocation.** It parks with the recipe.

## 19 fixes. Amendments from the critique (adopted 2026-09-13)

**Source.** `critique-unattended.md`, verdict sound-with-fixes: 1 blocker, 5 high.

- **F1: authority grants (this fixes the blocker).**
  - A `may` grant is honoured ONLY from an owner-committed record at the default-branch anchor. The
    choice between options is D12-j.
  - SCOPE rows may never carry `may`.
  - Run-written mandates (E2, E4, E5) honour no `may`, so veto 2 parks exactly as it does today.
  - The M3 boundary change is ratified as a DECISIONS row.
- **F2: IDLIST parsing is all-or-nothing.**
  - Any token with an id prefix that fails ITEM refuses the whole invocation. `...` and `…` ranges are
    admitted or refused by name.
  - The re-typed dSealedTally prompt silently narrowed six asks to two.
  - A new U13 arm checks that the prompt record's IDLIST is a subset of the `asks:` fact.
  - An absent `asks:` fact on E2, E4 or E5 with ids in the prompt record is a refusal.
- **F3: `asks-disposed` is keyed on a pinned `asks-ready:` fact.** For a `yes` ask, T3 admits only:
  - a closing spec of THIS build;
  - terminal evidence written OUTSIDE the run's range;
  - a hold whose decision park names the tripped M3 veto.

  Two further restrictions:
  - A self-filed owner-call hold is admitted only for `no` or `legacy` asks.
  - An in-range WONTDO on a `yes` ask is UNMET unless both a stale witness and a decision park exist.
    Without this, a run could meet the DoD with no delivered work.
- **F4: M-BASE is pinned at preflight** as `m-base:` = merge-base(anchor-sha, HEAD@preflight).
  - P5, READY and `may` are read there.
  - T4's range is `m-base..HEAD`.
  - U13 re-derives it from the pinned anchor-sha, never from `base:`.
- **F5: R2 and the target folder's own specs.**
  - SPECCED and INPROGRESS are admitted when every live closing spec lives in the TARGET folder.
  - A foreign live spec grades `no` only when its build has a non-terminal RUN.md. Otherwise it is
    `stale-claim` and the spec is named.
- **F6: what READY requires.**
  - `accept`, or a `seen` that carries a command.
  - Locators carry `@SHA7` or a content pattern, never a bare line number.
  - `stale` means the pinned probe shows the defect at M-BASE and not at HEAD.
  - `legacy` requires at least one of R4 and R5.
- **F7: gates (owner rule, 2026-09-13).**
  - Unit passes run no gates, and the harness passes `closes` ids into SPEC briefs with "run no gate".
  - `asks-disposed` is graded at `--close`, after the one post-build gate run.

## 20. Owner decisions, round 2 (2026-09-13, node d, session 2588f719)

| # | Decision | Recommended? |
|---|---|---|
| D11-b | Remote CI (U9) runs L1 and check 9 on every push to main. The OWNER sets GitHub to disallow squash and rebase PR merges | yes |
| D11-c | Landing stays DIRECT PUSH. CI detects after landing, no node can skip it, and losses are repaired forward | yes |
| D12-a | An ids-driven run ALWAYS starts from an owner-landed README. E2, the zero-commit ids start, is DROPPED. E4 and E5 route to E3 | no; this is the strongest option |
| D12-b | `asks-disposed` is OVERRIDABLE with a recorded reason, like gates-green | no |
| D12-c | KEEP on a mandated ask is allowed only after a CLOSED unit of this build `advances` it | yes |
| D12-d | New asks must be runnable (V14, forward-only): `accept`, or a `seen` that carries a command | yes |
| D12-e | `seen` commands run only under a conf prefix allow-list, which ships EMPTY | yes |
| D12-f | A run targeting a filing home builds in a NEW folder under its own slug. The filing home is never written | yes |
| D12-g | Check 13's BACKLOG.md skip covers only asks filed before `ASK_CUTOFF` | yes |
| D12-h | The standing do-not-run-unattended-self-tests instruction is LIFTED, but only for this build's unattended-kit units (U11-U13) | no |
| D12-i | The kit's own stop causes are INSIDE this build: 67 of 153 recorded stop entries and 10 of 15 aborts | no |
| D12-j | Authority (`may:`) comes ONLY from an owner-committed build README at the default-branch anchor. The scaffold never emits `may:` | yes |

### 20.1 Consequences

- **D12-a.** There is one authorization path.
  - `/unattended <ids>`, `/unattended --prompt "…ids…"` and `/unattended <filing-home>` each print the
    E3 recipe and stop without writing anything. The recipe is
    `gen_build_index.py --new-build <slug> --asks <ids>`.
  - The owner lands the generated README. That is one command and no prose, and `may:` appears only if
    the owner types it by hand. Then `/unattended <slug>` runs as E1.
  - P5 and P6 read the owner-landed `asks:` line.
  - The run-authored-folder residual in §19.2 is gone.
  - F2's check becomes "the recipe's IDLIST equals the landed `asks:` line".
- **D12-b.**
  - An override is written on the landing record, and drift counts it as `asks_disposed_overrides`
    (report-only).
  - F3's hardening still governs the path without an override.
  - CORE_FLOOR still moves from 12 to 13, but the item is NOT in the set that cannot be overridden.
- **D11-c.**
  - L7 detects AFTER landing. That is L1's timing, but it runs independently of every node's hooks.
  - With direct-push landing, no layer blocks a `--no-verify` push before it lands; this is §18r.6 hole
    2, now accepted by the owner.
  - The GitHub merge-method setting still stops squash and rebase on any PR.
- **D12-h.**
  - U11-U13 may run the unattended suites.
  - The standing note's method still applies: a hermetic probe first, and a suite once per unit at its
    end, never once per arm.
  - This does not change the owner rule that unit passes run no GATE legs.
- **D12-i.** This needs its own design pass over the kit-share stop entries and aborts that the practice
  report classified (`unattended-practice.md`). It produces new units, U16 onwards.

## 21. The kit's own stop causes (D12-i)

*Status: COMPLETE, awaiting owner review (designer pass, session 2588f719, node d, 2026-09-13).
Sections 21.1-21.9; U16-U30.*

**The requirement.** D12-i (§20) puts the kit's own stop causes inside this build: the 67 of 153
recorded decision and abort entries that no ask can carry, and the aborts among them. This section
turns every OPEN cause into a unit, U16 to U30, and measures each unit's reach against the census
entry by entry. It keeps the three binding rules unchanged:
- **landing is a DIRECT PUSH** through the lander and the pre-push bar (D11-c); no PR path appears;
- **a merge to main and a push each need an explicit ask, or a committed mandate the run did not
  create** (charter §1, `AGENTS.md:128-129`); no unit below lets a run write what authorizes it;
- **unit passes run no gates**; the whole bar runs once after every unit is built (F7), and U9's
  remote CI detects after landing.

Sources: the four analyst passes `scratchpad/kitstop-{landing,foreign-reds,kit-defects,host}.md`, the
census `scratchpad/unattended-practice.md` with `practice/handclass.json`, and three artifacts made in
this pass. All three are read-only on the repo and scratch-only:
- `scratchpad/ks_extract.py` re-splits all 153 entries with their record path and line;
- `scratchpad/ks_reach.py` assigns each of the 67 entries one outcome and the unit set that removes
  it, then COMPUTES every count in §21.5; its per-entry table is `scratchpad/ks_reach.tsv`;
- `scratchpad/inplacelab/run.sh` (output `inplacelab/out.txt`) exercises the landing shape of U18
  against a byte copy of `.githooks/pre-push`, with `GOV_GATE_CMD=true`. It ran no run-gates.sh, no
  `*.test.sh`, no self-test and no unattended kit code.

### 21.1 The population, reconciled

| Class (handclass) | Entries | Builds | Aborts in the 153 |
|---|---|---|---|
| landing and repo state | 20 | 13 | 6 (i7, i20, i29, i53, i78, i151) |
| reds belonging to other builds | 18 | 12 | 1 (i100) |
| kit defects found mid-run | 22 | 12 | 1 (i125) |
| environment and host | 7 | 5 | 1 (i63) |
| **total** | **67** | | **9** |

- **Aborts: 9 in the corpus, 10 as events.** The brief's "9 of 15" counts the aborts inside the 153.
  The census's "10 against 5" (`unattended-practice.md:403`) adds the deleted dHonouredPark abort
  (`git show 994a93b0^:memory/builds/dHonouredPark/RUN.md`), which is outside the 153. Both are right.
- **i7 (aBoundedVerdict's abort)** sits in landing by handclass and under "reds belonging to others"
  in the census abort table (`unattended-practice.md:257`). Its mechanism was check 7 counting a
  stuck LANDING record, so it stays in landing here.
- **i29 (aFusedCharter's abort)** moves from the landing analyst's C3 (fixed) to C4. The run aborted
  because the merge surfaced reds neither parent had, which U19 finds in the run's own tree. Fixing
  check 7 only turns that abort into a handoff, and a handoff is still a stop.
- **Entries that are not what their class says.** None of these is recounted; each keeps its class:
  - i31 and i133 are the build's own reds (a sibling unit; its own INPROGRESS pin);
  - i66 and i67 are one event, the run editing the tree its own bar graded (self-contention);
  - i22, i25, i27 and i71 are host or platform causes that the census filed as verification-route.
- **Outcomes over the 67**, from `ks_reach.py`:

| Outcome | Entries | Meaning |
|---|---|---|
| FIXED | 18 | removed by commits already on main (landing 6, kit 12) |
| DESIGN | 4 | removed by the ratified U1-U15 plan or rule F7 (i31, i133, i45, i58) |
| REMOVED | 31 | removed by a U16+ unit set, under either inherited-red policy |
| POLICY | 5 | removed under `INHERITED_RED=land`; under `park` they end HELD `inherited-red` (§21.7) |
| RULING | 3 | removed only if the owner rules for U30 (i10, i126, i139) |
| HELD | 3 | irreducible; the stop now ends HELD and resumable (i62, i63, i108) |
| OWNER | 2 | owner-initiated turns at the landing boundary (i38, i77) |
| METHOD | 1 | a method property that stops nothing (i148) |

### 21.2 Facts that bind this section (re-read at `09a22d2b`)

| # | Fact | Evidence |
|---|---|---|
| K10 | The lander runs only with the default branch checked out, and a run may never be on it. So every mandated landing must leave the run's tree | `tools/push-main.sh:63-67`; `tools/unattended/unattended.sh:1086-1091` |
| K11 | The lander pushes the node's whole local default branch, which every build on the node shares | `tools/push-main.sh:95` |
| K12 | The pre-push hook asks two things of the pushing tree: the lander marker in its OWN git dir, and HEAD equal to the pushed tip. It does not ask for the primary tree | `.githooks/pre-push:157-160`, `:164-169`, `:202` |
| K13 | The full-green stamp is per git dir, written only by a clean, unskipped, unmoved run, and the push boundary reuses it when it is at most 10 commits behind the pushed tip | `tools/run-gates/run-gates.sh:102`, `:1855-1870`; `.githooks/pre-push:192`, `:212-222` |
| K14 | `gates-green` is one boolean over `$GATE_CMD` in the run's tree. It does not grade the merge that lands, and it does not attribute a red | `unattended.sh:3075-3094` |
| K15 | `GATE_BOUND=3600` wraps the queue wait AND the bar, while the runner's own wall is 21600 s, armed after the turnstile, and the queue may wait 7200 s | `.unattended.conf:32`; `unattended.sh:182-198`; `tools/run-gates/gate-profiles.txt:66-74`; `run-gates.sh:422`, `:601` |
| K16 | There are 12 phases with no non-terminal hold, 7 halt codes with none for a host or platform stop, and a terminal is reached only by a verb | `unattended.sh:337-338`, `:472`; `memory/guides/UNATTENDED-PROTOCOL.md:305-309`; `CORE_FLOOR="12:12"` is phases:dod (`.unattended.conf:64`, `tools/unattended/check-unattended.sh:670-680`) |
| K17 | drift-audit keeps only the bare branch name of `origin/HEAD` and so compares against LOCAL main | `tools/drift-audit/drift_report.py:1858-1868` |
| K18 | The hook sources the repo's gate policy from the PUSHED working tree | `.githooks/pre-push:198-200` |
| K19 | **Lab.** The run's own worktree can make the `--no-ff` landing merge onto the observed remote tip and move its branch there as a fast-forward (T^1 = R, T^2 = old tip). The push from that worktree is refused without the marker and accepted with it. The runner and the hook resolve the same git dir, and another build's unpushed local-main commit is not carried. After the remote moves, reconciling it INTO the branch keeps the graded merge an ancestor of the pushed tip. A carry-set predicate names a foreign commit that arrived through a merge of local main | `scratchpad/inplacelab/out.txt`, arms P, Q, R, S, F |

### 21.3 The design in one paragraph

- **Land from the run's own tree.** The run makes the landing merge in place, onto the tip the remote
  advertises. It grades that merge once and pushes it. Neither the primary tree nor local main is
  involved (C1, C2, C4).
- **Terminal by evidence.** A LANDING commit is landed once the remote carries it (C5).
- **Attribute every red at the advertised tip**, using inputs the run cannot reach. The inherited-red
  policy is read there too (R1, R2, R6).
- **Make the bar honest about time.** The bar retries a timeout once. It bounds the queue separately
  from the run. It says HOST when the host is at fault, and it never passes silently (R3, C8, RC-B to
  RC-D).
- **End irreducible stops HELD.** A HELD run is non-terminal and resumable, with a generated
  checkpoint. It never ends ABORTED and never as a prose handoff (RC-E, RC-F).
- **Fix three checker defects**, and on the owner's ruling two method carriers.

### 21.4 Units

How to read each unit:
- Acceptance lines read *criterion — break → red*.
- Driver and lander breaks are observed by hand in a scratch fixture repo with a local bare remote,
  which is D12-h's method (b).
- Breaks in a repo-subject leg are observed on the one post-build bar.
- "Closes" rows become the `closes` list in the unit's spec header (§2.2).

**U16 — Held-suite failure baseline (R2; Tier 2; unattended + run-gates).**
- *Changes.*
  - `tools/unattended/run-unattended-gates.sh` and `tools/run-gates/run-selftests.sh` gain
    `--attribute <R>`. It runs the suite at R in a detached scratch worktree and normalises FAIL lines
    (repo path, scratch path, durations). It prints NEW, INHERITED and FIXED sets, plus
    `attributed N of M`.
  - `unattended.test.sh` gets its one-character `$1` fix (TOOL-aHoistedPass-36 cause 1,
    `memory/backlog/TOOL.md:416`).
  - `kit.toml:122-130`'s compensating check, and a KIT DoD's `GATE_SELFTESTS=1` run, pass on "no NEW
    FAIL, every INHERITED FAIL filed" instead of GREEN.
- *Acceptance.*
  1. A FAIL present at R and at L reads INHERITED, and a FAIL only at L reads NEW — break: drop the
     normalisation → the inherited FAIL reads NEW.
  2. A suite that aborts at L before any arm is a DEAD PROBE — break: an abort read as an empty set →
     green.
  3. The unsharded suite completes — break: revert the `$1` fix → it aborts.
- *Removes.*
  - i46, i48, i50 (`aHoistedPass/RUN.md:81,87,113`);
  - i80, i81, i82 (`aQuenchedHarness/RUN.md:39,41,43`);
  - i84 (`aReapedSpinner/RUN.md:65`);
  - with U22, i85 (`:67`).
- *Order.* **First, and before U11-U13.** D12-h has those units run suites that TOOL-aHoistedPass-36
  and -38 say are red at BASE. Needs D12-i8.
- *Closes and advances.* Closes TOOL-aHoistedPass-36. Advances TOOL-aBoundedCeiling-10, whose
  periodic half is U9's.

**U17 — Remote-relative bases and complete guards (R6, R1 prevention; Tier 1; drift-audit + run-gates).**
- *Changes.*
  - `drift_report.py:1868` keeps `refs/remotes/origin/<def>`, prints the base sha, and refuses when
    it does not resolve.
  - A sweep of `tools/` converts every bare default-branch comparison base, or waives it with a
    reason.
  - The lexicon leg's guard gains `.lexicon.conf` (`tools/gate-legs.json:1056-1066`).
  - A repo-subject canary reds any guarded leg whose argv reads a root `*.conf` missing from its
    guard.
- *Acceptance.*
  1. Local main ahead of origin, behind it, or equal to it gives one drift verdict — break: the bare
     name → i152's "sh: parser -> dark" returns.
  2. Removing the pin file from the guard reds the canary.
- *Removes.* i120 (`dFramedEntrypoint/RUN.md:41`), and the drift half of i12 and i152.
- *Order.* Any time before U21.

**U18 — The in-place landing merge (C1, C2; Tier 2; `tools/push-main.sh`, DEPL-visible).**
- *Changes.* Two new flags. The attended no-flag path is unchanged, and neither flag touches local
  `<def>`.
  - `--prepare`, run in the run's worktree on branch B:
    - observes the remote tip R and detaches there;
    - runs `git merge --no-ff B` with a subject that names the build slug and no unit id;
    - fast-forwards B to that merge, T;
    - on conflict, restores B and refuses, naming `git merge origin/<def>`.
  - `--land` refuses unless HEAD holds such a T with T^1 on the advertised tip. It refuses a
    non-empty foreign carry set (K19 arm F), naming each sha and its build. Otherwise it:
    - writes `push-main-active` in THIS git dir;
    - pushes `HEAD:refs/heads/<def>`;
    - on `race`, merges the new tip INTO B (today's reconcile shape, `push-main.sh:78-87`) and
      retries within `GOV_PUSH_MAIN_MAX_RETRIES`.
- *Why in place, not the analyst's lane worktree.* The graded merge, its full-green stamp and the push
  share one git dir (K13, K19). So the push reuses the run's green. The adopters' verbatim hook
  (`.githooks/pre-push:55`) does not change.
- *Acceptance.*
  1. With an unpushed foreign commit on local main, `--land` pushes only T — break: push local `<def>`
     (`:95`) → the foreign sha lands.
  2. A foreign commit that entered through local main is named — break: drop the local-main term.
  3. T^1 = R and T^2 = the old tip — break: a plain `git merge origin/<def>` → `--land` refuses.
  4. Without the marker the hook still refuses (arm Q).
  5. `build_commit` (`lib-unattended.sh:207-285`) picks the same commit per unit before and after —
     break: a merge subject naming a unit id → pass-order grades the merge.
- *Removes, with U19.*
  - i13 (`aBranchedMandate/RUN.md:52`) and i37 (`aGradedMandate/RUN.md:51`);
  - i59 (`aLexedStripper/RUN.md:47`);
  - i65 (`aPacedTurnstile/RUN.LANDED.a1fd98d8.md:32`) and i68 (`aPacedTurnstile/RUN.md:42`);
  - i76 (`aPromptedMandate/RUN.md:34`);
  - i88 (`aScouredKit/RUN.md:101`) and i132 (`dRetiredFork/RUN.md:156`);
  - with U25 as well, the i53 abort (`aHoistedPass/RUN.md:133`).
- *Order.* Early, and before U19. Adopters get it through their DEPL builds (U8+).
- *Closes, with U19.* TOOL-aPacedTurnstile-15 (`TOOL.md:187`).

**U19 — The run's landing path (C1, C2 residual, C4; Tier 2; unattended).**
- *Changes.*
  - `LANDER_MODE=primary|in-place`, with `primary` (today) as the default. Gov sets `in-place`.
  - The Skill's Land step (`SKILL.template.md:752-760`) and protocol §6 become three steps:
    `{{LANDER}} --prepare`, then `--close`, then `{{LANDER}} --land`. Reconcile from `origin/<def>`
    only. "Merge just in case" becomes "push the branch and stop" (C6).
  - `gates-green` gets a numbered refusal unless HEAD carries a prepared merge. It then runs
    `$GATE_CMD` with `GATE_FULL=1`, plus `GATE_SELFTESTS=1` when the DoD owes it. That run is F7's one
    bar, and the push reuses its stamp.
  - It runs before `--close` writes anything, because the stamp needs a clean tree
    (`run-gates.sh:1855-1857`).
  - The carry-set refusal also runs at `--close`.
  - `--close` commits its records on T (TOOL-dUnstalledConvoy-24, `TOOL.md:46`). The push boundary's
    scoped bar then covers only that records-only delta, and that bar belongs to the hook; it is not a
    second full bar.
- *Acceptance.*
  1. A branch that is green alone and red once merged onto a moved tip is UNMET — break: grade the
     bare tip.
  2. `--close` without `--prepare` refuses.
  3. The hook reads `scoped gate` from T — break: a stamp in another git dir → FULL.
  4. A Skill missing either flag reds the template byte-compare and check 26.
- *Removes.* i28 and i29 (`aFusedCharter/RUN.md:40,42`), plus U18's list.
- *Order.* After U18. Orthogonal to U11-U13.

**U20 — The terminal (C5, C3 residuals; Tier 2; unattended; D12-i2).**
- *Changes*, under D12-i2 (a):
  - A LANDING record whose own commit is reachable from the advertised tip DERIVES LANDED. That holds
    in `--status`, check 7, the LIVE generator and the leg. It widens TOOL-aPrimedKeepalive-7
    (`check-unattended.sh:1494-1551`) from "not counted" to "landed".
  - `units-at-landing` freezes at `--close`, on the pushed tree, and so does `asks-at-landing` after
    U12.
  - `--landed` stays for the primary path. Its check 34 becomes ancestry: the marker's M is on the
    advertised tip, and the witness is an ancestor of M or M itself (TOOL-dUnstalledConvoy-38).
  - Preflight pins `branch-ref` on every anchor (`unattended.sh:2742-2745`). This gap had no row.
  - The leg checks each terminal record's fact set (TOOL-aBoundedCeiling-11, weak form).
- *Under (b)* instead: append-only `pending|landed <def> <merge> <tip>` marker lines
  (TOOL-aUnblockedFleet-7), the `pending` acceptance, and a numbered second landing.
- *Acceptance.*
  1. A LANDING commit on the remote derives LANDED, and one only on local `<def>` does not.
  2. Killing the lander after its push still derives LANDED (the i150 window) — break: require the
     marker.
  3. A hand-set LANDED with no `landed-anchor` reds the leg.
  4. A default-branch preflight writes `branch-ref`.
- *Removes.* i150 (`dTieredTribunal/RUN.md:55`). Knock-on effects, not counted:
  - the four LANDING records with merged work (`unattended-practice.md:80-90`) derive LANDED;
  - the defect `TOOL-aBoundedCeiling-9` records disappears, because no LANDED commit follows the push.
- *Order.* After U19 and U12.

**U21 — Red attribution, report-only (R1; Tier 2; run-gates + pre-push + unattended).**
- *Changes.*
  - **Re-run at R.** With `GATE_ATTRIBUTE=<R>`, after the pool drains, each red leg re-runs alone at
    R. It uses a detached scratch worktree, R's own manifest row (`GATE_LEGS`, `run-gates.sh:91`) and
    `GATE_FULL=1`.
  - **Classify.** ATTR (`kitstop-foreign-reds.md` §4) gives each red leg one verdict:
    - OWN if it is green at R, absent from R's manifest, or R..L touches its comparator;
    - INHERITED if S(L) ⊆ S(R);
    - otherwise MIXED, whose delta counts as OWN;
    - a timeout is CONTENDED and goes to U24.

    The equal-input-key shortcut stays rejected, because guards omit inputs.
  - **Signatures.** An optional `signature` argv, first declared on lexicon, install-prefix,
    drift-audit records and memory hygiene.
  - **Output.** `$RUNDIR/attribution` and the line `attributed N of M red legs`; N < M is a DEAD
    PROBE. The hook exports the tip it reads. Exit codes are unchanged.
- *Acceptance.*
  1. R with one offender and L with one more → INHERITED 1 and OWN 1 — break: compare counts.
  2. A leg whose checker the branch edited is OWN — break: drop the comparator clause.
  3. A leg that cannot run at R is a DEAD PROBE, never INHERITED.
  4. Fixture replays of `aStagedLane/RUN.md:51` and `dCarriedReceipt/RUN.md:89` both read OWN.
- *Removes.* Nothing alone. With U22 it removes the five POLICY entries.
- *Order.* After U17.

**U22 — Inherited-red policy (R1; Tier 2; pre-push + unattended; D12-i4, D12-i5).**
- *Changes.*
  - **Where the policy lives.** `INHERITED_RED=park|land` and `INHERITED_RED_MAX_AGE` are read by
    `git show <R>:<policy file>`, never from the pushed tree (this closes K18 for them). The default
    is `park`.
  - **What the policy does.**
    - Under `land`, a bar whose every red leg is INHERITED, not worsened and within the age limit
      passes, and the push carries the attribution.
    - Under `park`, the run holds as `inherited-red --until probe gate` (U26).
  - **Refusals.** A "not mine" override is refused, and so is `--abort --code
    gate-red-out-of-scope`, unless the attribution shows at least one INHERITED leg and no OWN leg.
  - **ABSORB** goes in the protocol and the Skill. An inherited red may be fixed in-run only when
    all five conditions hold:
    - A3 names the owner;
    - the fix touches only the declared write set;
    - no M3 veto is tripped;
    - the fix is its own commit whose subject names no unit id;
    - the fix is recorded CLOSED in the run's `BACKLOG.md`.
  - **Auto-file.** Each INHERITED leg auto-files an ask carrying `seen` (the argv at R), `accept`
    ("leg green"), `→` (the owning commit) and a SEV row. It stays dark until U10 and U5, and U15 arms
    it.
- *Acceptance.*
  1. A policy committed on the branch but not at R has no effect — break: read the tree → a run
     enables its own landing.
  2. A replay of aStagedLane's override is refused.
  3. Under `land`, a red that is only INHERITED lands and files its ask, and a MIXED red does not.
  4. A red past the age limit parks.
- *Removes*, under `land`:
  - i12 (`aBranchedMandate/RUN.md:48`, with U17);
  - i69 (`aPrimedKeepalive/RUN.md:45`) and i93 (`aThawedCorpus/RUN.md:47`);
  - the i100 abort (`aWalkedCorpus/RUN.md:50`);
  - i152 (`dTracedLattice/RUN.md:39`, with U17 and U24).

  Under either policy it removes i85, with U16.
- *Order.* After U21. The auto-file needs U10 and U5.

**U23 — Runner hygiene (RC-B, RC-D; Tier 2; run-gates).**
- *Changes.*
  - `TMPDIR="$WORK/tmp"` is set before dispatch.
  - Each bar sweeps any `$WORK` whose pid is dead (`ts_alive`, `run-gates.sh:611`).
  - The runner prints `TMPDIR entries <n>`, and callers invoke it by absolute path.
  - On `tree_moved=yes` it exits with a distinct TREE MOVED status. `gates-green` reads that as UNMET
    and re-runs once.
- *Acceptance.*
  1. A tree that moves mid-bar gives TREE MOVED even when every leg is green — break: exit 0.
  2. The entries count does not grow across two killed bars.
- *Removes.* i66 and i67 (`aPacedTurnstile/RUN.md:36,38`), as the backstop to F7, and the adjacent
  i22.
- *Closes.* TOOL-aMeteredTurnstile-2 and TOOL-aReapedSpinner-14.
- *Order.* Any time before U24.

**U24 — Honest verdicts under contention (R3, RC-C runner half; Tier 2; run-gates).**
- *Changes.*
  - **Retry.** A leg that ends rc 124/137 with a fired ceiling re-runs once, serially, after the
    drain. A pass reads `ok, retried after timeout`. A second timeout is FAIL. Both readings go to
    the ledger.
  - **Neighbours.** The FAIL tail records the neighbour count.
  - **Acquire line.** The runner prints `acquired <iso>`. U25 reads that stdout line and no
    queue-status file, which sidesteps all three refutations of TOOL-aUnblockedFleet-6.
  - **Calibration.** Spawn time is measured against this clone's recorded minimum. A kill while it
    is over K times that minimum exits HOST. K is a ratio, never a wall clock.
  - **No silent pass.** Exit 0 needs a verdict line and a leg verdict, or "0 legs selected". The hook
    reads a missing verdict line as RED. TOOL-aSurfacedLexicon-25 (`TOOL.md:350`) records a landing
    push that ran no bar. U18 is only as safe as this.
  - **Drift signal.** drift gains `legs_retried_after_timeout`.
- *Acceptance.*
  1. A timeout beside a spinning sibling ends `ok, retried`, and a hang alone ends FAIL.
  2. A planted dead-holder beacon still yields a verdict — break: the reap path exits 0.
  3. HOST requires the calibration.
- *Removes.* i70 (`aPrimedKeepalive/RUN.md:47`), i91 (`aSurfacedLexicon/RUN.md:97`), i97 with U25, and
  i152's timeout half.
- *Closes.* TOOL-dSpentCeiling-8 and TOOL-aSurfacedLexicon-25.
- *Order.* After U23.

**U25 — The driver's bound stack (kit C8, RC-C driver half; Tier 2; unattended; D12-i7).**
- *Changes*, under D12-i7 (a):
  - The bar's budget is the runner's wall. That wall is armed after the turnstile and already exceeds
    the largest ceiling (`gate-profiles.txt:66-72`).
  - The queue has its own `GATE_QUEUE_BOUND`, defaulting to `TS_MAXWAIT`.
  - `GATE_BOUND` becomes a backstop: wall + queue + margin, read from `--print-profile`
    (`run-gates.sh:511-519`) at preflight and pinned there. A lower hand-set value is refused, naming
    both numbers. A command with no profile keeps its own value, announced.
  - A kill before `acquired` holds as `host-degraded --until probe gate`. A HOST exit holds as `probe
    host`.
- *Acceptance.*
  1. A bar that queues past 3600 s and then passes is MET — break: charge the queue to the bar.
  2. A wedged runner dies at the backstop and reads "never started".
- *Removes.* i97 (`aUnblockedFleet/RUN.md:36`, with U24) and the killed-close half of i53. With U24
  and U26 it turns i62 and i63 into HELD.
- *Closes.* TOOL-aUnblockedFleet-8.
- *Order.* After U24 and U26.

**U26 — HELD (RC-F; the clean end for RC-C, RC-E and inherited reds; Tier 2; unattended).**
This adopts `kitstop-host.md` §5, plus one more code.
- **The phase.** HELD joins PHASES_CORE as a non-terminal phase, so `CORE_FLOOR` becomes `13:13`
  after U12.
- **The verb.** `--hold <slug> --code <c> --until <cond> --reason <text>`.
  - Codes are `host-degraded`, `platform-limit`, `platform-unavailable`, `host-owner-action` and
    `inherited-red`, plus `HOLD_CODES_EXTRA`.
  - Conditions are `after <ISO-UTC>`, `probe host|gate|api` or `owner`.
  - It refuses unless the keepalives are reaped or recorded `keepalive-unreachable: <node>`, the tree
    is clean and committed (and pushed where `ANCHOR_SCOPE=published`, `.unattended.conf:110`), and
    the run's own processes are reaped (U27).
- **The checkpoint.** It is generated, and every gate claim in it is a pointer. It records the
  witness, the next unit, the last bar's run record, any pending runId (U28), the parked count, the
  code and the condition.
- **Resume from HELD.** `--resume` works in order:
  1. If the condition is unmet, print "still held" and exit 0 with no writes.
  2. Reap.
  3. Name any interrupted acts: a staged index, a bar with no verdict, a ticket held by a dead pid.
  4. Re-verify authorization at the pinned BASE.
  5. Accept `--keepalive-id`.
  6. Return to the working phase.
- **Presumed stopped.** `--status` derives `presumed-stopped` when the keepalive is gone and the last
  commit is older than a bound.
- **What stays the same.** `keepalive-reaped` checks a list fact. A HELD run cannot close or land.
  Only `--landed` and `--abort` write a terminal phase.
- **Where the text goes.** The contract goes to a companion guide, `UNATTENDED-STOPS.md`. The
  protocol gains two rows, because it stands at 57,815 of 61,440 B (§19.8).
- *Acceptance.*
  1. An unmet `after` writes nothing.
  2. `--hold` refuses on a dirty tree.
  3. A reason that states a gate verdict never reaches the gate field (the `dCarriedReceipt/RUN.md:89`
     class).
  4. A cross-node resume records the unreachable keepalive and continues.
  5. `--landed` on a HELD run refuses.
- *Converts to HELD.*
  - i62 and i63 (`aMeteredTurnstile/RUN.md:31,33`);
  - i108 (`dCarriedReceipt/RUN.md:87`);
  - the dHonouredPark abort;
  - under `park`, the five POLICY entries.
- *Closes.* TOOL-aBranchedMandate-8, TOOL-aReapedTicket-5, and part of TOOL-aPromptedMandate-11. With
  U11 it also closes TOOL-aBoundedVerdict-23.
- *Order.* Early (D12-i11), and before U25 and U27. It does not wait for U11: its checkpoint names
  whatever next unit `--status` computes.

**U27 — Run-owned process ledger (RC-A; Tier 2; unattended + process-monitor).**
- *Changes.*
  - The driver records the pid of every bar or suite the run starts, in
    `<git-common-dir>/unattended/<slug>.procs`.
  - `--preflight`, `--resume` and `gates-green` reap any recorded pid whose session is gone. They do
    it through `PROCMON_CMD` (blank means off, announced) and `reap.py --kill <pid>`, which "bypasses
    the MODE, never the FENCE" (`tools/process-monitor/reap.py:321`).
  - `--status` shows the orphan count.
  - Rule: nothing kills a process this RUN did not start.
- *Acceptance.*
  1. A recorded orphan is reaped — break: matching by command line kills a same-named foreign
     process.
  2. An unrecorded pid is never killed.
- *Removes.* i1 (`aBoundedCeiling/RUN.md:33`: the question becomes the rule) and i26
  (`aFusedCharter/RUN.md:36`: its bars were the run's own).
- *Order.* After U26.

**U28 — Review durability under platform limits (RC-E; Tier 2; workflows).**
- *Changes.*
  - Every lens and skeptic writes its output before returning, and a re-run skips any lens whose file
    exists at the same subject sha.
  - A new `deferred-platform` exit, distinct from BLOCKED.
  - The runId is recorded as a run fact.
- *Acceptance.*
  1. When two of five lenses die, the re-run dispatches two.
  2. When all five die, the exit is `deferred-platform`, never CLEAN.
- *Removes.* None of the 67. It reaches the dHonouredPark abort and the adjacent i27
  (`aFusedCharter/RUN.md:38`).
- *Closes.* Part of DEPL-aHoistedPass-8.
- *Order.* Any time. It is independent of U1-U15, and U26 reads the runId it records.

**U29 — Checker defects (kit C5, C6, C1 recurrence; Tier 2; unattended).**
- *Changes.*
  - **Check 23** (`check-unattended.sh:2347-2357`) covers a committed path P only when all three
    hold:
    - this unit's `brief · item <unit> · reason <h12> P` row exists;
    - P lies under the build's `prompts/`;
    - the blob starts with `<h12>`.
  - **The conf-read hoist (`TOOL-aHoistedPass-37`).** Hoist the conf read above the `only28` guard, and announce that checks
    30 and later are skipped.
  - **The check-22 join (`TOOL-aHoistedPass-40`).** Land the check-22 join with both `fail 22` branches armed.
  - **Class gates.** Every argument the parser accepts must appear in an arm, and check 26 now grades
    flags as well as verbs.
- *Acceptance.*
  1. An edited brief is still reported, and so is a sibling unit's brief — break: exempt all of
     `prompts/`.
  2. `--only 28` completes.
  3. A documented flag with no parser arm reds check 26.
- *Removes.* i49 and i52 (`aHoistedPass/RUN.md:111,129`), and i57 (`aLeakedHandle/RUN.md:55`).
- *Order.* After U13. It works on the same file, under the same self-test lift.

**U30 — Method carriers, on the owner's ruling (kit C9, C10; Tier 1-2; D12-i10).**
- *Changes.*
  - **§8 forks.** They become column-0 `- **F<n>** — <question>` items, graded per item by
    `plan_state` (`unattended.sh:1700-1741`) and by the hygiene reader.
    - A quoted mark does not count (TOOL-dHonouredPark-7).
    - The rule applies forward-only, after `FORK_ITEM_CUTOFF`.
  - **M6** (`BUILD-METHOD.md:188-195`) binds delegated passes. An inline author may sequence disjoint
    units and says so in the brief. A DECISIONS row carries the rule out of node d's local memory.
  - **No before-state line.**
- *Acceptance.*
  1. After the cutoff, an unresolved F-item under a resolved one reds.
  2. A quoted RESOLVED does not count.
- *Removes.* i10 (`aBoundedVerdict/RUN.md:33`) and i139 (`dSealedTally/RUN.md:54`). i126
  (`dPromptedSeam/RUN.md:34`) stays an accepted cost, and it stopped nothing.
- *Order.* After U2, on the ruling.

### 21.5 Reach, measured

`ks_reach.py` computes every figure below from one outcome per entry; `ks_reach.tsv` lists each entry
with its record path and the unit set that removes it. "Removes" means that, judged from the record's
own text, the run would have written no decision or abort at that point.

| Unit | Entries it is needed for | Of which aborts | Notes |
|---|---|---|---|
| U16 | 8: i46 i48 i50 i80 i81 i82 i84 i85 | 0 | i85 with U22 |
| U17 | 3: i12 i120 i152 | 0 | alone for i120 |
| U18 | 9: i13 i37 i53 i59 i65 i68 i76 i88 i132 | 1 (i53) | every one with U19 |
| U19 | 11: U18's nine + i28 i29 | 2 (i29, i53) | alone for i28, i29 |
| U20 | 1: i150 | 0 | plus 4 stuck records, knock-on |
| U21 | 5: i12 i69 i93 i100 i152 | 1 (i100) | only with U22 |
| U22 | 6: U21's five + i85 | 1 (i100) | five of them only under `land` |
| U23 | 2: i66 i67 | 0 | adjacent i22 |
| U24 | 6: i62 i63 i70 i91 i97 i152 | 1 (i63) | i62, i63 end HELD |
| U25 | 4: i53 i62 i63 i97 | 2 (i53, i63) | |
| U26 | 3 converted to HELD: i62 i63 i108 | 1 (i63) | + dHonouredPark; + 5 POLICY under `park` |
| U27 | 2: i1 i26 | 0 | |
| U28 | 0 | 0 | dHonouredPark and adjacent i27 only |
| U29 | 3: i49 i52 i57 | 0 | |
| U30 | 3: i10 i126 i139 | 0 | the recommended ruling removes i10, i139 |

**Totals over the 67:**

| Outcome after U16-U30 | `INHERITED_RED=land` | `park` |
|---|---|---|
| already gone (FIXED 18, DESIGN 4) | 22 | 22 |
| removed by U16-U30 | 36 | 31 |
| removed by the recommended U30 ruling | 2 | 2 |
| end HELD, resumed with no owner answer | 3 | 8 |
| owner-initiated turns (i38, i77) | 2 | 2 |
| method (i148) and accepted cost (i126) | 2 | 2 |

**Aborts, all 10 events:**
- 5 are already fixed: i7, i20, i78, i125 and i151.
- U19 removes i29. U18, U19 and U25 together remove i53.
- i100 is removed under `land` and ends HELD under `park`.
- i63 and the dHonouredPark abort end HELD.
- **No non-carriable stop ends ABORTED any more.**

**Adjacent, not counted.** These are host-caused entries that the census filed as verification-route:
- i22 is removed by U23;
- i25 ends HELD;
- i27 ends HELD, with its lenses kept by U28;
- i71 was not re-measured.

**Records, not units.** Three OPEN rows describe fixes that have already landed:
TOOL-aBoundedCeiling-12, TOOL-aPromptedMandate-9, and the per-leg half of TOOL-aBoundedVerdict-10
(`kitstop-host.md` §4 RC-A). They go into the U3b worksheet, pre-filled as `CLOSED · … · by <sha>`.

### 21.6 Ordering against U1-U15 and U9

**Hard edges:**
- U16 before U11. The suites D12-h runs are red at BASE.
- U18, then U19, then U20. U20 also comes after U12, because it freezes `asks-at-landing`.
- U17, then U21, then U22. U22's auto-file needs U10 and U5, and U15 arms it.
- U23, then U24, then U25. U26 also comes before U25, and U26 before U27.
- U29 after U13, in the same file.
- U30 after U2.

**Recommended sequence (D12-i11).** First build U16, U18, U19 and U26: they make THIS build's own run
survivable, meaning its suites, its landing and its stops. Then U17, U21, U23 and U24 go in beside
U1-U4. U20, U22, U25, U27 and U29 follow their edges, and U28 is free.
- U26 does not wait for U11. Its checkpoint names whatever next unit `--status` computes, and that
  becomes dependency-ordered once U11 lands. U11 and U26 together close TOOL-aBoundedVerdict-23.
- None of U16-U30 needs builds mode, except U22's auto-file.
- U5's flip commit is unaffected.

**U9.** Remote CI is the ideal per-sha oracle for U21's A2 and A3, and the missing periodic half of
U16. Two additions belong in U9's spec: a scheduled run of the held suites that publishes a per-sha
FAIL set, and a per-sha bar verdict. `land` does not wait for U9, because D11-c already accepts
detection after landing, and U9 is where that detection happens.

**This build's own landing.** It lands once, with one bar (F7). With U18 and U19 built, it lands in
place. That is the first real-remote use of the new lander, so it runs under the owner's explicit
ask. The mandate substitute starts with the U15 pilot.

### 21.7 What remains irreducible, and how such a stop ends

| Stop | Why no kit change removes it | Clean end |
|---|---|---|
| account usage or session limit (i108, dHonouredPark) | the quota lives outside the repo | HELD `platform-limit --until after <reset UTC>`; if the session dies first, the passive path |
| API 529 / overload (adjacent i27) | platform availability | HELD `platform-unavailable --until probe api`, with finished lenses on disk (U28) |
| a degraded or co-tenant host (i62, i63; adjacent i25) | node a pays about 251 ms per process against node d's 19-39 ms (TOOL-aGradedDoorway-10), and other repositories share the host | HELD `host-degraded --until probe host`. When only an admin act helps, such as scanner exclusions (TOOL-aScannedThrottle-3), `host-owner-action --until owner`: the owner fixes the MACHINE and decides nothing about the build |
| an inherited red under `park` | the red is another build's, and ABSORB's five conditions fail | HELD `inherited-red --until probe gate`, plus the auto-filed ask |
| process death or compaction with no announcement | the agent is gone | `presumed-stopped`; `--resume` reaps, names interrupted acts and re-verifies authorization |
| an owner-initiated turn (i38, i77) | the owner may always intervene | recorded as today; with U18 and U19 nothing sits on local main, so no later landing inherits it |
| two green changes that fail together | nothing prevents it | not a stop: it surfaces at the one bar on the prepared merge as OWN, and the run fixes it (U19) |
| a left-shift written after the closing review (i148) | a method property | a gotchas record, or an ask for the next build |
| a kit defect found mid-run in future | the class never reaches zero | an ask with `seen` and `accept` in the run's own `BACKLOG.md` (§19.6); a park only when the fix trips an M3 veto |

**The rules for how a stop ends, under the U26 contract:**
- A stop the run did not decide never ends ABORTED, and never as a prose handoff.
- It ends HELD, but only after all of this holds:
  - the tree is clean and committed, and the branch is pushed;
  - every recorded keepalive is reaped or recorded unreachable;
  - every run-owned process is reaped.
- The checkpoint is generated, and each gate claim in it is a pointer to a run record.
- The restart is `/unattended --resume <slug>`. It carries no answer, so §19.10(3) does not count it
  as an owner turn. An owner-declared scheduler (D12-i9) may issue the same restart.

### 21.8 "Execute a build to completion", restated

The owner lands a README (D12-a) and says `/unattended <slug>`. From then on, the run carries the build
to a LANDING commit that the remote carries, with no owner ANSWER in between. Along the way:
- every unit is built with no gate;
- the bar runs once, on the landing merge prepared onto the advertised tip;
- the mandated asks are disposed (§19.5);
- the landing is a direct push through the lander and the hook.

The run may PAUSE, and a pause never asks anything. A HELD stop resumes when its condition holds, or
when someone restarts it, and the restart carries no answer. Two kinds of turn remain, and this section
does not measure either:
- turns the owner starts;
- the ask half's owner-call parks (§19.3, §19.10).

**The residual, measured over the 67** (under `land`, with the recommended rulings):
- **0 need an owner answer.**
- 3 end HELD and resume on a restart; under `park` that is 8.
- 2 are turns the owner started.
- 1 is a method property, and 1 is an accepted cost.
- 0 of the 10 non-carriable aborts would end ABORTED.

**Caveats.**
- Every class is a hand call, ±3 (`unattended-practice.md:267`).
- "Would have removed" is a counterfactual judged from each record's text.
- i62 and i63 are counted conservatively as HELD, although the turnstile, U23 and U25 may simply
  remove them.

### 21.9 Owner decisions this raises

| # | Question | Options | Recommend, and why |
|---|---|---|---|
| D12-i1 | The landing shape | (a) in place on the run's branch (U18); (b) a lander-owned lane worktree, with the full-green stamp moved to the common dir; (c) the primary-tree lander only | **(a).** One git dir gives one bar, and the hook that adopters receive verbatim is untouched. Lab K19 |
| D12-i2 | How a landing becomes terminal (touches `UNATTENDED-PROTOCOL.md:305`) | (a) DERIVED: the LANDING commit is reachable from the advertised tip; (b) a numbered second landing plus marker lines; (c) LANDED committed on the branch before the push, and carried by it | **(a).** It removes all five marker failure modes and TOOL-aBoundedCeiling-9. (c) is rejected because a refused push would leave a false LANDED on the branch |
| D12-i3 | Charter §1, "Land on local `main` first" (`AGENTS.md:128`; `coding-governance-agents.template.md:54`) | (a) "make the landing merge onto the observed remote tip, verify it, push that tip", as a PLAY row and net-negative template bytes in U6; (b) keep it, and add an unattended exception | **(a).** Local main as the staging ref is C2's root cause |
| D12-i4 | Gov's `INHERITED_RED` | (a) `land`, with an age bound of 10 first-parent landings, matching `GATE_FULL_MAX_LAG`; (b) `park`, the kit default | **(a).** It removes 5 entries. Under (b) they still need no answer, but they wait for another build's fix |
| D12-i5 | ABSORB's bound | the declared write set, or wider | **The write set**, which is exactly what i85 did |
| D12-i6 | May a timeout that passes its serial retry count as green? | yes, or no | **Yes**, with the drift watermark |
| D12-i7 | Where `GATE_BOUND` comes from | (a) derived: the runner's wall plus the queue bound, which is about 8 h on gov's `capable` profile; (b) hand-set, passed down as `GATE_WALL`; (c) today's | **(a).** Two hang bounds with different numbers is the defect in K15. The cost: a wedged close waits up to the backstop |
| D12-i8 | Extend D12-h's self-test lift to D12-i's unattended units (U16, U19, U20, U22, U25, U26, U27, U29)? | (a) extend it, with U16 first so the criterion is "no NEW FAIL"; (b) observe by hand only | **(a).** Charter §7 wants every failing case observed, and U16 alone needs the suites to run |
| D12-i9 | A durable resume scheduler | (a) opt-in via conf, off by default; (b) none | **(a).** It is a standing-configuration write, so it sits behind a default-OFF gate (charter §9) |
| D12-i10 | The method carriers (U30) | §8 as F-items, forward-only; M6 binding delegated passes; no before-state line | **Adopt all three.** i126 stays an accepted cost |
| D12-i11 | Order, and the first use | U16, U18, U19 and U26 first; this build's own landing runs in place, under an explicit ask | **Yes** |
| D12-i12 | U9's scope | add the held-suite schedule and a per-sha verdict publish | **Yes, when U9 is specced** |


## 21 fixes. Critique amendments adopted (critique-kitstops.md, verdict sound-with-fixes; 2026-09-13)

- **KF14 (the blocker): attribution must not read a run's own new failure as inherited.** A red leg
  counts as INHERITED only when both of these hold:
  - S(L) is non-empty;
  - the leg declares a per-offender signature, OR its normalised output is byte-identical at L and R.

  Every other red leg that is also red at R counts as MIXED. An empty S(L) with a non-zero exit is a
  DEAD PROBE. Two breaks are staged:
  - a new offender line without a FAIL line must read MIXED;
  - an empty set at both L and R must read DEAD PROBE.
- **KF2: a separate stamp for landings over inherited reds.** The new stamp kind is
  `gate-inherited-green`, and it records the attributed leg set and R.
  - The hook accepts it only when attribution at the new R shows the same INHERITED set or a
    smaller one.
  - It never satisfies predicate 1 for a later scoped push.
  - This means neither a second FULL bar at the push nor a relaxed stamp that certifies a red tree.
- **KF3: nobody grades their own grader.** When R..L touches `run-gates.sh`, `gate-fingerprint.sh`,
  `.githooks/pre-push` or the attribution module, every red is forced to OWN and the policy to park.
  The staged break: edit the classifier and the red must still read OWN. U21's header says the
  runner already grades itself, and that this predates this build.
- **KF4: in `LANDER_MODE=in-place`, `--landed` refuses the local arm** with a numbered code.
  `branch-ref` is NOT pinned on a default-branch anchor. Acceptance: an in-place run merged into
  local main and then given `--landed` is refused.
- **KF5: U20 derives LANDED only in `--status` and the leg**, which already observe ADV_HEAD, or in
  a print-only mode. It NEVER does so in the LIVE generator, which is committed and freshness-gated.
  Doing it there would red check 9 after every landing.
- **KF7: a per-slug lease under the git common dir.**
  - The keepalive tick and `run_bounded` refresh it.
  - `presumed-stopped` means the lease is older than max(backstop, declared bound).
  - `--resume` refuses a fresh lease with a numbered code, so no two sessions can drive one slug.
  - Acceptance: a resume while this slug's bar is running is refused.
- **KF15: one `derived_phase()` shared by the phase readers.** `refuse_if_terminal`, rotation,
  `--resume` and `--status` all use it.
  - Preflight on a derived-LANDED build ROTATES the record, as `RUN.LANDED.<blob>.md` plus a
    `landed-derived` fact. It never overwrites the record.
  - `--resume` on a landed record never re-drives `--land`.

## 22. Owner decisions, round 3: the kit's stop causes (2026-09-13/14, node d, session 2588f719)

| # | Decision | Recommended? |
|---|---|---|
| D12-i1 | In-place landing on the run branch: `push-main.sh --prepare`, then `--close`, then `--land` (U18/U19) | yes |
| D12-i2 | LANDED is DERIVED: the LANDING commit is reachable from the advertised tip. Only `--status` and the leg compute it (KF5) | yes |
| D12-i3 | Charter §1 "Land on local main first" is KEPT for attended landings. Unattended runs get a written EXCEPTION | no |
| D12-i4 | INHERITED_RED=land, age bound 10 first-parent landings, recorded with a `gate-inherited-green` stamp (KF2, KF14, KF3) | yes |
| D12-i5 | ABSORB is WIDER: an in-run fix of an inherited red may go outside the declared write set when all five ABSORB conditions hold | no |
| D12-i6 | A timed-out leg that passes its single serial retry counts as green; `legs_retried_after_timeout` is tracked | yes |
| D12-i7 | GATE_WALL is HAND-SET in conf, exported to the runner, and the driver bound derives from it | no |
| D12-i8 | The self-test exception is EXTENDED to U16, U19, U20, U22, U25, U26, U27 and U29. U16 runs first, so the criterion is "no NEW failure" | yes |
| D12-i9 | Auto-resume from HELD: the kit ships it OFF (adopters opt in) and gov's conf turns it ON. This is the reading of "opt-in, on by default" | amended |
| D12-i10 | U30 method carriers adopted: per-item F<n> §8 forks (forward-only), M6 binding delegated passes only, no before-state line | yes |
| D12-i11 | U16, U18, U19 and U26 are built FIRST. This build's own landing is the new lander's first real use, under the owner's explicit ask | yes |
| D12-i12 | U9 also carries a scheduled held-suite run and a per-sha verdict publish | yes |

### 22.1 Consequences

- **D12-i3.**
  - The charter text: §1's Landing gains one clause, "unattended runs land per the unattended
    protocol's in-place landing". The rule itself lives in `UNATTENDED-PROTOCOL.md` or its
    companion, NOT in the charter.
  - The template edit must still be net-negative. It sits at 49,032 of 49,152 B, so bytes elsewhere
    in §1 pay for the clause.
  - U6 carries the edit and a PLAY row records the exception.
  - Left standing: attended landings through local main can still publish other builds' unpushed
    commits (C2's mechanism). Only unattended runs are protected by construction. The carry-set
    check from U18 may be offered to attended `push-main.sh` as an opt-in flag.
- **D12-i5.**
  - ABSORB's five conditions stay the gate, but the write-set clause is dropped.
  - Every ABSORB fix lands as its own commit, whose message names the inherited leg and R.
  - KF3 still binds: an ABSORB fix that touches the runner, fingerprint, pre-push or the attribution
    module forces OWN plus park.
  - Check 23 (declared versus actual writes) records the out-of-set write as an ABSORB, not as an
    anomaly.
- **D12-i7.**
  - One declared number: `GATE_WALL` in `.unattended.conf`.
  - The driver's GATE_BOUND = GATE_WALL + the runner's queue bound.
  - `run-gates.sh` receives GATE_WALL through the environment.
  - Initial value: 21600 s, the runner's current wall on gov's profile. The owner may change it.
  - A conf check reds when GATE_WALL is below the largest declared leg ceiling.
- **D12-i9.**
  - The conf keys are `RESUME_SCHEDULE_*`. The kit default is OFF.
  - The gov conf sets it ON in the same unit that ships it. U26's scope grows by the scheduler; its
    cleanest carrier is a harness scheduled task, and a per-node OS task is the alternative.
  - The scheduler only ever issues `/unattended --resume <slug>`.
  - The KF7 lease makes a resume refuse while a live session still holds the slug.
- **D12-i8.** It sits beside D12-h and follows the standing note's method: a hermetic probe first,
  and each suite once per unit at the unit's end.
