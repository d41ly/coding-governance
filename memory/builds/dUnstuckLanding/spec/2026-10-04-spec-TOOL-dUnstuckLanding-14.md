# TOOL-dUnstuckLanding-14 — the attended terminal: a handed record derives LANDED, `--settle` writes it, and a landed ABORTED record gains `work-landed-at`

**Status:** CLOSED · rev-2 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 2 · closes TOOL-dUnstuckLanding-4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-14-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-14-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |

<!-- /gen:spec-records -->

## 1. Goal

A run that `--handoff` ended `HELD` is landed later by a person, and nothing in the kit notices: the
record says `HELD` for ever, and the 28 legacy `ABORTED` records whose work reached the default
branch say `ABORTED` for ever. This unit makes the record agree with git in two moves. A HELD record
under a hand-off code whose own commit is on the advertised tip READS `LANDED (attended)` wherever
the kit derives a phase, and a new verb, `--settle`, WRITES that reading durably. For a legacy
ABORTED record, and for a run interrupted with no verb written, `--settle` adds one fact,
`work-landed-at`, decided by a content predicate rather than by witness ancestry, which review item
H1 showed is structural for any record read from the tip. Check 15 then grades that fact as upheld,
not merely present.

## 2. Scope (IN)

- **S1 — the landing commit of a handed record.** `read_landing_commit` in
  `tools/unattended/lib-unattended.sh` takes an optional second argument, the hand-off code list.
  With it, HEAD's copy may also read `phase: HELD` with a `hold-code` in that list, and the answer is
  the commit that last changed the path, exactly as for `LANDING`. Without it the function is
  byte-unchanged in behaviour. The driver passes `$HOLD_CODES_HANDOFF`, and the leg passes the same
  constant read from the driver by `core_of`, so the list is spelled once. Observed by AC1, AC2.
- **S2 — the derivation.** `read_derived_phase` derives `LANDED` for a HELD record whose `hold-code`
  is a hand-off code and whose landing commit is an ancestor of the advertised tip, and sets a new
  global, `DP_BY=attended`. A HELD record under any other code is never derived and never observes
  the remote. `--status` prints the phase as `LANDED (attended)`. `--liveness`, which takes no
  network, reads the same landing commit offline against the ref its `finished-unstamped` test
  already resolves, and reports `state: terminal`. Observed by AC1, AC2.
- **S3 — every deriving reader follows.** `--resume` over a handed record that derives LANDED writes
  nothing and names `--settle`. `--preflight` rotates it, and its scratch copy gains
  `landed-by: attended` beside the facts the rotation already writes. The leg's
  `check_derived_landed` admits it, so check 7's exclusion and check 23's share the reading.
  Observed by AC1, AC3, AC9.
- **S4 — the content predicate.** A new library function, `check_work_landed`, takes a record and
  an advertised tip and returns 0 landed, 1 not landed, or 2 undecidable with the reason in
  `WL_WHY`. Landed means all three of these hold:
  - the record's `witness` is not an ancestor of its `base`, and `base..witness` holds at least one
    attributable commit, one whose subject names the slug or that touches `memory/builds/<slug>/`;
  - every attributable commit is an ancestor of the tip;
  - no commit on the tip's first-parent line since the landing, `git rev-list --first-parent <tip>
    ^<witness>`, carries a `This reverts commit <sha>` line naming one of them. That is the design
    record's clause (iii) as written, and `TOOL-dUnstuckLanding-15` reads the same line.

  A missing `base`, a `base` or `witness` this clone cannot resolve, or an unreadable range is
  undecidable, never a guess. It is shared by `--settle` and check 15, so the writer and the grader
  cannot disagree about one record. Observed by AC4.
- **S5 — `--settle <slug>`, implemented as `run_settle`.** It reads the RECORDED phase and takes
  exactly one of four branches, refusing everything else with a number and before any write:
  - **A handed record.** HELD under a hand-off code, deriving LANDED: it writes `phase: LANDED`,
    `witness: <landing commit>`, `landed-derived: <landing commit> <tip>` and `landed-by: attended`.
    `units-at-landing` is already there, written by the hand-off.
  - **A legacy ABORTED record.** First committed before `HANDOFF_CUTOFF` by
    `read_first_commit_date`, and the predicate reads landed: it writes `work-landed-at: <witness>
    <tip>` and nothing else. A record first committed on or after the cutoff, or not committed, is
    refused, because from that date ABORTED means discard. A blank `HANDOFF_CUTOFF` refuses every
    ABORTED settle, naming the key.
  - **A lease-dead working record.** Any non-terminal phase but HELD, whose liveness verdict is
    `STALE` or `UNBOUND` and whose work the predicate reads landed: it writes `work-landed-at` and
    `abandoned: <utc>` under the CURRENT phase, never a terminal.
  - **Already settled.** A record carrying the fact this branch would write prints that and writes
    nothing, exit 0.

  The refusals are a HELD record under any other code, a record that does not derive or whose work
  does not read landed, an undecidable predicate, a `LIVE` or `ELSEWHERE` lease, a recorded
  `LANDING` or `LANDED` (whose verbs are `--landed` and `--preflight`), a record differing from
  HEAD's copy in more than its lease lines, and a remote that does not answer. Observed by AC1, AC2,
  AC4, AC5, AC6, AC8.
- **S6 — the settle commit.** `--settle` stages the record and never commits. It prints the commit
  owed and that the commit rides the next landing from the same tree, or a batched owner pass. Every
  deriving reader reads the record correctly before that commit lands. Observed by AC1.
- **S7 — the abandoned marker is read.** `--preflight`'s concurrent-run announcement excludes a
  record carrying `abandoned`, printing why, and the leg's check 7 report does the same, so the two
  count one population. Observed by AC6.
- **S8 — check 15, upheld rather than present.** For every record, live or archived, carrying
  `work-landed-at`, the leg runs `check_work_landed` against the advertised tip and reds when it does
  not read landed, when the record is ABORTED and first committed on or after `HANDOFF_CUTOFF`, or
  when `abandoned` stands without `work-landed-at`. An unanswered remote is reported as a skip, as
  check 15's `landed-derived` arm already does. The fact-set arm gains a population, `attended`: a
  recorded LANDED carrying `landed-by: attended` owes `units-at-landing`, `landed-derived` and
  `landed-by`, through `read_missing_landed_facts`. Observed by AC1, AC7.
- **S9 — the recipe's last line.** The `handoff` row the hand-off writes gains a final
  ` && bash <kit>/unattended.sh --settle <slug>`, the kit path derived from the driver's own
  `KIT_DIR` relative to the top of the repository holding the kit, and `--handoff` prints the same
  line as its settle hint. Observed by AC10.
- **S10 — the carriers.** `STOPS.template.md` §1, whose "Only `--landed` and `--abort` still write a
  terminal" gains `--settle` and whose `--preflight`-over-HELD refusal gains the handed-and-landed
  exception; §8, a resume-matrix row for that record; and §12, the derivation, the predicate, the
  two facts and the `attended` population. `PROTOCOL.template.md` §3, both the "two ends" sentence
  and the exception beside "A run that is already terminal cannot be moved at all": `--settle` may
  add `work-landed-at` to a legacy ABORTED record, and that is the only write a terminal record
  admits. `VERBS.template.md` gains a `--settle` entry, and `SKILL.template.md` invokes it in the
  hand-off section. The renders are re-copied in the same pass. Observed by AC11, AC12.
- **S11 — the arms.** Every new numbered branch gets an arm in its sibling suite asserting a literal
  slice of its own text. Observed by AC13.

## 3. Non-goals (OUT)

- The drift-audit signals that list unsettled and discarded records: `TOOL-dUnstuckLanding-15`.
- Settling an ARCHIVED record. A rotated record is immutable, its name carries its blob, and
  `--preflight` refuses to retire anything it would then have to edit. `--settle` addresses a slug's
  live `RUN.md` only, and an archived ABORTED record stays for the drift signal to report.
- Writing `work-landed-at` during a rotation. A follow-up could, and it is not asked for here.
- Committing the settle record. It rides a later landing, by the design's rev-2 L1.
- Any new conf key. `HANDOFF_CUTOFF` is `TOOL-dUnstuckLanding-13`'s.
- The kit version marker, moved once by the orchestrator at VERIFYING.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-13` — the two hand-off codes and the constant naming them,
  the `units-at-landing` fact a settled record carries, the `handoff` recipe row this unit extends,
  and `HANDOFF_CUTOFF`. Without them nothing derives and every ABORTED settle refuses.
- **hands-off** `TOOL-dUnstuckLanding-15` — the `work-landed-at` fact the signal must find upheld,
  the content predicate it must agree with, and the three negative fixture shapes its liveness is
  drawn from. Archived ABORTED records are beyond `--settle`'s reach, so the signal decides how it
  counts them.
- **hands-off** `TOOL-dUnstuckLanding-18` — the derived attended terminal, which the table's "act on
  another run's record" row rests on.

## 4. Design

### Evidence

Read at `98926870` on 2026-10-04, PINNED to that sha; `tools/` is unchanged since `0c16a66b`.

- `read_landing_commit` (`tools/unattended/lib-unattended.sh:1065-1073`) returns nothing unless
  HEAD's copy reads `phase: LANDING`, so a HELD record can never derive today.
- `read_derived_phase` (`tools/unattended/unattended.sh:1160-1180`) returns at once for any phase
  but `LANDING`, and observes the remote only through `read_advertised_tip`.
- `--preflight` derives and tests `is_terminal` at `:5080-5081`, rotates through a scratch copy that
  writes `phase`, `witness` and `landed-derived`, refuses with fail 81 when that copy misses a fact
  the arm requires (`:5127`), and only then reaches its HELD refusal (`:5141-5142`), which reads the
  derived phase again. A handed record that derives LANDED therefore rotates, and the facts it needs
  are `units-at-landing` and `landed-derived` (`lib-unattended.sh:1156`).
- `refuse_if_terminal` (`unattended.sh:2675`) is fail 26, and reads the derived phase unless passed
  `--recorded`.
- `print_liveness` (`unattended.sh:6200`) reads the RECORDED phase and takes no network. Its
  offline `finished-unstamped` test checks a witness against `dref`, the remote-tracking default
  ref, at `:6239`. Its verdicts are `TERMINAL`, `ELSEWHERE`, `FINISHED-UNSTAMPED`, `HELD`,
  `UNBOUND`, `STALE` and `LIVE` (`:6275-6281`).
- The preflight concurrent-run loop is at `unattended.sh:2223-2240`; the leg's check 7 report and
  `check_derived_landed` are at `tools/unattended/check-unattended.sh:2676-2695` and `:437-445`.
- Check 15's `landed-derived` arm tests the commit against the advertised tip at
  `check-unattended.sh:2040-2050`, and its fact-set arm picks a population at `:1867-1890`.
- `verb_abort` writes `witness` = HEAD and then commits the record over it (`unattended.sh:4746-4752`),
  which is why ancestry cannot be the predicate (review item H1).
- The run-state file carries a `base` fact, written once by `--preflight`.
- gov's ABORTED records at BASE: eight live `RUN.md` files and four archives, by
  `git grep -l '^phase: ABORTED' -- 'memory/builds/*/RUN*.md'` on 2026-10-04, PINNED.

### Data model

| Fact | Written by | Value | Graded by |
|---|---|---|---|
| `phase: LANDED` | `--settle`, handed branch | — | the existing terminal checks |
| `landed-derived` | `--settle` and the rotation | `<landing commit> <advertised tip>` | check 15's existing anchor arm |
| `landed-by` | `--settle` and the rotation | `attended` | the fact-set arm's `attended` population |
| `work-landed-at` | `--settle`, legacy ABORTED and lease-dead branches | `<witness> <advertised tip>` | check 15's new upheld arm |
| `abandoned` | `--settle`, lease-dead branch | UTC, ISO-8601 with a trailing `Z` | check 15's new arm, and the two live counts |

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `--settle` | verb | none; joined by the leg's check 26 |
| `run_settle` | shell function | `sh.function`, asked `--suggest run_settle --as sh.function` on 2026-10-04: OK |
| `check_work_landed` | shell function, in the library | `sh.function`, asked on 2026-10-04: OK |
| `derive_liveness` | shell function | `sh.function`, `derive` leads, snake |
| `DP_BY` · `WL_WHY` | globals | no `sh.constant` cell is declared |
| `landed-by` · `work-landed-at` · `abandoned` | facts | none |
| `attended` | fact-set population | none |

`derive_liveness` is the verdict half of `print_liveness`, factored out so `run_settle` reads the
verdict without printing it. `print_liveness` calls it and prints exactly what it prints at BASE.

### Ordering inside `run_settle`

Every refusal comes before the first write, in this order: the slug and the record; the
already-settled test, which writes nothing and so may answer first, since a settle is staged and a
re-run meets a record differing from HEAD by exactly what it wrote; the record's own difference
from HEAD; the recorded phase and the branch it selects; the advertised tip, through
`read_advertised_tip`, refused when unanswered; the branch's own test, which is the derivation, the
cutoff and predicate, or the liveness verdict and predicate. Then the facts are written with
`set_fact`, the record is staged with `stage_or_fail`, and the owed commit is printed.

### Fail numbers

The new refusals take the next free numbers after `TOOL-dUnstuckLanding-13`'s. None is pinned here,
and the acceptance criteria grep each refusal's own text.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/unattended/SKILL.md`

### Rollout

Nothing in the tree carries a hand-off code or either new fact at BASE, so the derivation and the
upheld arm are inert until a run hands off or an owner settles. The eight live legacy ABORTED
records in gov are settled, or refused, by an owner pass after this build lands; this unit does not
run that pass.

### Alternatives rejected

- **Witness ancestry as the predicate.** Rejected by review item H1: a record read from the tip
  carries its witness on the tip by construction, so the probe reads ON for every record it acts on.
- **A third terminal, `LANDED-ATTENDED`.** Rejected in the design record's §2: it is a terminal
  written over a terminal, which fail 26 exists to stop, and it costs six phase-set readers.
- **Derivation only, nothing written.** Rejected there too: STOPS §12 keeps the committed live index
  out of the deriving readers, so the most-read file would say HELD for ever.
- **`--liveness` asking the remote.** It is the out-of-session reader the stop-guard and the resume
  tick call, and its contract is offline; the ref its `finished-unstamped` test resolves already
  answers the question without a network round-trip.

## 5. Production-readiness checklist

- security — `--settle` writes only what the advertised tip and the record's own history prove,
  and only to the slug's live record, staged and uncommitted. A hand-written `work-landed-at` reds
  check 15, so the fact cannot be planted to silence a later signal. The one exception to fail 26 is
  a single fact on a dated class of records, and is stated in the protocol beside the rule.
- perf / scale — one `ls-remote` per settle, and per record carrying `work-landed-at` in the leg,
  against the advertised tip the leg already resolves once. The predicate walks `base..witness` and
  the tip's first-parent line since the witness, which are a run's own range and the history since.
- error / empty / loading states — undecidable is its own return and its own refusal; an unanswered
  remote refuses the verb and is a reported skip in the leg, never a red.
- observability — `--status` prints `LANDED (attended)`; `--settle` prints which branch it took,
  what it wrote and the commit owed.
- risks — the derivation reaches every deriving reader at once. AC2 and AC9 pin the two that could
  go wrong: a non-hand-off HELD record must stay HELD, and `--resume` must not take over a landed
  hand-off.
- testing — the fixture observations below, and one arm per new branch.
- migration — none; no record changes until somebody runs `--settle`.
- user docs — the VERBS entry and the Skill's hand-off section.

## 6. Acceptance criteria

- **AC1** — When a fixture record handed off under `owner-landing` is merged to the fixture origin's
  default branch, `--status tRun` prints `LANDED (attended)`, `--liveness tRun` prints
  `state: terminal`, and `--settle tRun` writes `phase: LANDED`, `landed-by: attended` and a
  `landed-derived:` line naming the landing commit, stages the record and leaves HEAD unmoved. Then
  `bash tools/unattended/check-unattended.sh --skip 28` over that fixture prints the fact-set line
  counting one record in the `attended` population and no check 15 failure.
  Red when: any reader still prints HELD, the settle commits, or the arm reds a settled record.
  fixture: none in the tree. The pass builds one under `%TEMP%/<short-name>` the way the suite's
  `bcsetup` helper does, runs `--handoff` from `TOOL-dUnstuckLanding-13` over it, and merges the
  branch to the bare origin's default branch.
  cost: one scoped leg run over a small fixture.
- **AC2** — When the same fixture's record is instead held with `--hold tRun --code inherited-red
  --until "probe gate"` and merged the same way, `--status tRun` prints `HELD`, and `--settle tRun`
  is refused with a number and a message naming the hold code, with the record byte-unchanged.
  Red when: a non-hand-off hold derives a terminal, which would end a live run through fail 26
  (review item M13).
- **AC3** — When `--preflight tRun --keepalive-id KA-2` runs over the AC1 record before it is
  settled, it rotates the record to an archive under `RUN.LANDED.` whose bytes carry
  `landed-by: attended` and `units-at-landing`, and it prints neither fail 81 nor fail 82; over a
  settled record it rotates the same way.
  Red when: either rotation refuses, or the archive lacks a fact the fact-set arm requires.
- **AC4** — When `--settle` runs over four fixture ABORTED records, each first committed before a
  `HANDOFF_CUTOFF` of `2099-01-01`: one whose `witness` equals its `base`, one whose `witness` is
  another build's commit, one whose work was merged and then reverted on the default branch, and one
  whose work was merged and kept, then the first three are each refused with the not-landed text
  and the fourth gains `work-landed-at:` naming its witness and the tip. With the fourth record's
  `base` fact removed, it is refused with the undecidable text.
  Red when: any of the first three gains the fact, or the fourth does not, which would mean the
  predicate cannot read ON or cannot read OFF over the population it acts on.
- **AC5** — When the fourth AC4 record is graded under a `HANDOFF_CUTOFF` earlier than its first
  commit, `--settle` refuses with a message saying the record meant discard; with `HANDOFF_CUTOFF`
  blank it refuses naming the key.
  Red when: either writes the fact (review item M2).
- **AC6** — When a fixture record at `BUILDING` with no lease facts, whose `--liveness` verdict is
  `UNBOUND`, carries work the predicate reads landed, `--settle` writes `work-landed-at` and
  `abandoned:` and leaves `phase: BUILDING`; a `--preflight` of another fixture slug then prints the
  record as EXCLUDED rather than counting it. With a fresh lease making the verdict `LIVE`, the
  settle is refused.
  Red when: a terminal is written, the marker is not read, or a live run is settled.
- **AC7** — When the fourth AC4 record is edited by hand to carry `work-landed-at:` while its work is
  reverted on the tip, `bash tools/unattended/check-unattended.sh --skip 28` prints a check 15
  failure naming `work-landed-at` and the file; restored to the settled bytes, it prints none. A
  fixture record carrying `abandoned:` with no `work-landed-at:` also reds.
  Red when: the hand-written fact is accepted on presence alone (review item M3).
  cost: one scoped leg run per arm over a small fixture.
- **AC8** — When the fixture's origin URL is pointed at a path that does not exist, `--settle` over
  the AC1 record is refused with a number and a message saying the tip was not observed, and the
  record is byte-unchanged.
  Red when: the verb guesses, or writes.
- **AC9** — When `--resume tRun --keepalive-id KA-3` runs over the AC1 record before it is settled,
  it prints nothing to resume, names `--settle`, and writes nothing.
  Red when: the HELD take-over row of the resume matrix fires over a landed hand-off.
- **AC10** — When `--handoff` runs over a fresh fixture, its `handoff` row's reason ends with
  `--settle tRun`, and the path before it does not begin with an absolute drive or `/`.
  Red when: the settle line is missing, or the kit path is spelled as a literal.
- **AC11** — When `grep -c 'unattended.sh --settle '` runs over `tools/unattended/SKILL.template.md`
  it prints at least 1; `grep -c '^- `--settle` — '` over `tools/unattended/VERBS.template.md` prints
  1; `grep -c 'work-landed-at'` over `tools/unattended/PROTOCOL.template.md` and over
  `tools/unattended/STOPS.template.md` each print at least 1; and STOPS §1 no longer reads "Only
  `--landed` and `--abort` still write a terminal".
  Red when: a carrier states the old rule, which is review item H4's class.
- **AC12** — When `cmp` runs over each of `tools/unattended/PROTOCOL.template.md`,
  `tools/unattended/STOPS.template.md` and `tools/unattended/VERBS.template.md` against its render
  under `memory/guides/`, each reports no difference, and
  `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: a template changed without its render.
- **AC13** — When `python tools/memory-tree/check-arms.py --report` runs after the arms are written,
  every new numbered branch of `tools/unattended/unattended.sh` and
  `tools/unattended/check-unattended.sh` reads armed, and neither unarmed registry gains a row.
  Red when: a new branch reads unarmed or pinned.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · the AC1 to AC10 fixtures, each staging its derivation, its refusal or its write · the suite's own arm count moves by the arms added
New arm: tools/unattended/check-unattended.test.sh · the AC7 hand-written fact and the orphan `abandoned` marker, and the AC1 `attended` population · none

## 8. Open questions

- **F1 — Does `--settle` reach an archived record?** (a) No: the slug's live record only. (b) Yes:
  it edits the archive too. An archive's name carries its blob, and the kit states that nothing
  edits a record once it is archived; (b) breaks both, which is a carrier change the design did not
  name. Recommendation (a). RESOLVED (agent, 2026-10-04, delegated): (a); (b) is discarded by veto 2.
  The consequence for the drift signal is handed to `TOOL-dUnstuckLanding-15` in §3.
- **F2 — What does a blank `HANDOFF_CUTOFF` mean to `--settle`?** (a) Every ABORTED record is
  legacy, so it may be settled. (b) No ABORTED record may be settled until the project dates the
  meaning. (a) lets a discard-meaning record be silenced in any adopter that has not dated the key,
  which is review item M2 reopened. (b) costs one conf line. Recommendation (b). RESOLVED (agent,
  2026-10-04, delegated): (b); (a) is discarded by veto 3, since it widens the write surface on
  terminal records past what this unit prices.
- **F3 — Does `--liveness` derive the attended terminal?** (a) It asks the remote, as
  `read_derived_phase` does. (b) It reads the landing commit offline against the ref its
  `finished-unstamped` test already resolves. (c) It stays HELD. (a) breaks the verb's stated
  offline contract, which the stop-guard and the tick rely on; (c) leaves the out-of-session reader
  disagreeing with `--status`. Recommendation (b). RESOLVED (agent, 2026-10-04, delegated): (b), the
  most feature-rich survivor; (a) is discarded by veto 2.
- **F4 — Which liveness verdicts make a working record lease-dead?** (a) `STALE` and `UNBOUND`. (b)
  `STALE` only. The census's four interrupted records predate the lease facts, so (b) refuses every
  one of them and the unit answers none of review item M16's population. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a), satisfying the ask's lease-dead clause over its own
  population.
- **F5 — Does the leg's check 7 report read `abandoned` too?** (a) Yes, with `--preflight`'s
  announcement. (b) The announcement only, as the design names. (b) leaves two counts of one
  population disagreeing, the two-answers class. Recommendation (a). RESOLVED (agent, 2026-10-04,
  delegated): (a); it is a report line and changes no verdict.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from ask TOOL-dUnstuckLanding-4, the design record's §2 (c1)
  and (c2) at rev-2, review items H1, H4, M2, M3, M6, M13 and M16, and the spec brief for units 13
  to 20.
- rev-2 · 2026-10-04 · the build pass settled three details the design left open, none moving an
  acceptance criterion. S9's settle command is spelled `bash <kit>/unattended.sh`, as the Skill and
  the lander invoke scripts, and its path is the kit's own prefix in the repository holding it,
  which a fixture running the source kit reads as the kit's prefix too. The ordering puts the
  already-settled test first, because a staged settle differs from HEAD's copy and a re-run would
  otherwise meet the difference refusal; a recorded `LANDED` carrying `landed-by: attended` reads as
  settled rather than as the LANDED refusal. The protocol's §3 exception is paid for by trimming one
  history clause in §9, leaving 52 bytes of its cap for units 16 and 18.

## 10. Reuse audit

The probe, run on 2026-10-04:

```
python tools/codebase-map/reuse_lookup.py "derive a landed terminal from the advertised tip and write it durably into a run record"
```

It ranked name-stem seams only (`run`, `write`, `records`, `derive_scope`) and reported `.sh` as an
unscanned layer, so it cannot see the driver or the library. None of its hits derives a phase. The
seams reused are read from source: `read_landing_commit` and `read_missing_landed_facts` in
`tools/unattended/lib-unattended.sh`, extended rather than copied, so the driver and the leg keep
one answer each; `read_derived_phase`, `read_advertised_tip` and the rotation's scratch-copy writes
in `tools/unattended/unattended.sh`; `print_liveness`'s offline ancestry test; and check 15's
`landed-derived` arm in `tools/unattended/check-unattended.sh`, which the upheld arm follows. For
the content predicate no existing seam fits: nothing in the kit attributes commits to a run by
content, and the design record's §2 records why ancestry, the one predicate that exists, is unsound.

Recall terms used: read_derived_phase read_landing_commit landed-derived rotation preflight fail-81 refuse_if_terminal fail-26 LANDED_FACTS_CUTOFF fact-set derived terminal

The question passed with them: "how is LANDED derived from the advertised tip and written at
rotation, and what may be written onto a terminal record". It returned this build's ask, the reader
table of `TOOL-dDerivedDocket-22`'s spec, the design record and STOPS §12, and nothing that
contradicts the source read above.
