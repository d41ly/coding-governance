# TOOL-dUnstuckLanding-18 — the close-decision table, and a build that lands with its rest carried forward

**Status:** CLOSED · rev-3 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 6 · closes TOOL-dUnstuckLanding-8 · ratified 2026-10-04

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-18-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-18-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-19 TOOL-dUnstuckLanding-20 |

<!-- /gen:spec-records -->

## 1. Goal

Across the three repositories the census read, 46 closing decisions were left to an owner who was
not there, and each one ended as an abort or an override (design §5, census K2). This unit gives the
close a standing disposition for every decision kind the census found. It adds a closed table that
maps each kind to LAND, HAND OFF or ABORT, and lets `build-complete` meet when every unfinished unit
is DEFERRED against an open ask this build filed. It also adds one sentence to BUILD-METHOD M3: at
the close, a park is never an abort. Owner ruling `TOOL-dUnstuckLanding-23` supersedes D8 as
`build-complete` applies it, and this unit builds that ruling.

## 2. Scope (IN)

- **S1 — the close-decision table.** A new last section of `tools/unattended/STOPS.template.md`,
  headed `The close-decision table`. Its rows are CLOSED, and each maps one decision kind to an exit
  and to the record that exit writes. The rows are listed under §4 Data model. Two rules follow the
  table. A decision of a kind the table does not list is a HAND OFF under `owner-decision`, because
  the work is sound and only a turn is missing. ABORT is reserved for work that must not land as it
  stands. The render `memory/guides/UNATTENDED-STOPS.md` is re-copied in the same pass. Observed by
  AC7.
- **S2 — the carry-forward term.** In `tools/unattended/unattended.sh`, `build-complete`'s fifth
  term stops failing on a non-terminal unit when that unit meets all five conditions below. The term
  then reports one `carried forward` line per such unit, naming the unit and its ask. Every unmet
  condition names the unit and the condition it failed. Observed by AC1 to AC5.
  1. Its status is `DEFERRED`.
  2. The roster at the run's pinned BASE carries it, read through `baseline_units`. So a unit this
     run added cannot be carried forward, whether a review promotion or an adopted discovery added
     it.
  3. The run-state file carries a `rescope · item defer <unit>` row for it.
  4. Its spec header names an ask with `closes` or `advances`. This build's `BACKLOG.md` at HEAD
     files that ask under this build's own slug, and the ask witness reads its status as neither
     CLOSED nor WONTDO. A blank `ASKS_CMD` leaves the condition unmet, naming the missing contract.
  5. No CLOSED unit's spec declares a `consumes-from` edge onto it.
- **S3 — the edge reader.** `read_consumes_from` in `tools/unattended/lib-unattended.sh` prints the
  unit ids a spec's `### Edges` block declares as `consumes-from`, one per line. It reads the
  backticked ids the TEMPLATE-SPEC §3 grammar admits, and it skips the `external` form. It reads text
  only, as `read_fork_cutoff` reads the memory kit's conf, because the unattended kit installs
  without the memory kit's checker. Observed by AC2.
- **S4 — `defer`, a fourth rescope act.** `verb_rescope` accepts `--act defer`. The unit must
  already be in the roster, and `--successor` is refused, because a deferral names no unit that
  follows it. `PARK_ACTS_OWED` gains `defer`, so the row is surfaced to the owner at the wrap-up, and
  declared scope set aside still reaches their one read. The kit gate's act-axis probe in
  `tools/unattended/check-unattended.sh`, which greps the driver for the literal three-act
  alternation, is widened to the four-act one, or that probe refuses. The usage line at the driver's
  head and the `--rescope` entry in `VERBS.template.md` name the new act. Observed by AC6.
- **S5 — the protocol row.** PROTOCOL §4's `build-complete` row says that a unit carried forward
  under the stop contract's close-decision table is not unfinished, and §9's sentence on a run that
  stops early names the recorded deferral beside the recorded `--override` as its escapes. The render
  is re-copied, and it stays within its declared size cap. Observed by AC9.
- **S6 — the M3 sentence.** `tools/memory-tree/BUILD-METHOD.template.md` M3 gains one sentence
  beside "No survivors → park". It says that at the close a park is never an abort: the run records
  the park and takes the exit the unattended-run protocol's close-decision table names. M8's Landing
  line says that a partial landing is one of the landings it points at. The render
  `memory/guides/BUILD-METHOD.md` is re-rendered by
  `bash tools/memory-tree/adopt-memory-tree.sh --render` and stays within 30720 bytes. Observed by
  AC8.
- **S7 — the Skill.** In `tools/unattended/SKILL.template.md`, the two `land-once-done` waiver
  sentences say an override is still owed at close unless every unfinished unit is carried forward.
  The Close section names the defer act and the carry-forward term. The paragraph listing the exits a
  promoted unit may never take gains this one, with the reason. The rendered Skill
  `.claude/skills/unattended/SKILL.md` is regenerated by `bash tools/unattended/adopt-unattended.sh`.
  Observed by AC11.
- **S8 — the ruling is cited where the rule lives.** The comment above `build-complete` quotes the
  owner's "merge and push only when the entire build is fully done". It gains the superseding
  ruling's id, `TOOL-dUnstuckLanding-23`, and that ruling's own words. The ruling row already stands
  in `memory/DECISIONS.md`, and this unit writes no row there. Observed by AC10.
- **S9 — the kickoff manifest is re-stamped**, because `memory/guides/BUILD-METHOD.md` is in its
  `watch:` list. Observed by AC12.
- **S10 — the two mirrors of the owed acts.** `tools/drift-audit/drift_report.py` and
  `tools/runlog/model.py` each spell the driver's `PARK_ACTS_OWED`, and each kit's self-test holds
  its copy to the driver both ways. Both gain `defer`. The runlog ledger sources gain
  `rescope-defer` after `rescope-supersede`, so the owed kinds and acts still lead that tuple, and
  the runlog ledger fixture and the drift-audit run-record fixture each gain one defer row. Two
  existing driver-suite arms move with the code they pin: the `--act` refusal names four acts, and
  the driver now calls `baseline_units` from two sites. Observed by AC13.

## 3. Non-goals (OUT)

- **The kit versions.** The unattended and memory-tree versions move once, at VERIFYING, by the
  orchestrator, per the build's brief.
- **Check 24.** It requires a rescope row for a unit that became WONTDO since BASE. Asking the same
  for a unit that became DEFERRED is a separate rule, and `build-complete`'s condition 3 is the binding
  observation for the only case where it matters.
- **The refreshed tip.** The table's "a question the default branch already answered" row tells the
  run to observe the advertised tip before it parks. The `refreshed-at` fact that records the tip is
  `TOOL-dUnstuckLanding-19`'s, built after this unit.
- **`CLOSE_GRANTS`, and a pre-asked close.** Design §5 tested both and rejected both.
- **The `land-once-done` directive's registry row.** Its name and its M8 section are unchanged.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-13` — `--handoff` with `owner-landing` and
  `owner-decision`, which five rows of the table name as their exit. Without it those rows name a verb
  that does not exist.
- **consumes-from** `TOOL-dUnstuckLanding-14` — the derived attended terminal, which the "act on
  another run's record" row rests on when it says no act is needed.
- **consumes-from** `TOOL-dUnstuckLanding-17` — the history legs graded over the run's own range,
  which the "move a shrink-only pin" row rests on when it says the kit's legs no longer ask it.
- **hands-off** external — the "publish another session's commits" row rests on `in-place` landing
  reaching the adopters, which ask `TOOL-dUnstuckLanding-11` carries.
- **hands-off** `TOOL-dUnstuckLanding-20` — the close-decision table, which that unit extends by one
  row for a run on a node that cannot land.

## 4. Design

### Evidence

Read at base `98926870`. Line numbers are PINNED to that reading; the builder locates each by the
quoted text.

| Site | Where | What it does today |
|---|---|---|
| `build-complete` | `unattended.sh:7944-8040` | six terms; term 5 is `nonterminal_units`, which reds any row not CLOSED or WONTDO |
| `nonterminal_units` | `unattended.sh:3103` | the unit rows whose status is neither CLOSED nor WONTDO |
| `asks_filed_by` | `unattended.sh:3411` | the asks a BACKLOG text files under one slug |
| `run_ask_witness`, `ask_field` | `unattended.sh:3243` | the ask generator's derived status per ask, through `ASKS_CMD` |
| `spec_ask_verbs` | used at `unattended.sh:8465` | a spec header's `closes` or `advances` ids |
| `baseline_units` | `lib-unattended.sh:1277` | the roster at the run's BASE, which check 24 and `--rescope` already read |
| `verb_rescope` | `unattended.sh:9520` | the closed act case `retire\|supersede\|add` |
| `PARK_ACTS_OWED` | `unattended.sh:696` | `retire supersede`, the acts surfaced to the owner |
| the act-axis probe | `check-unattended.sh:893` | greps the driver for the literal three-act alternation |
| the protocol render | 65589 of 65692 bytes | `wc -c` against `tools/template-size-limits.txt`, DERIVED at base |
| the method render | 27422 of 30720 bytes | the same, for `memory/guides/BUILD-METHOD.md` |

### Data model

The table, as S1 writes it. Five of its exits are `--handoff` codes that `TOOL-dUnstuckLanding-13`
ships.

| Decision kind | Exit | Record |
|---|---|---|
| land a partial build | LAND, when `build-complete`'s carry-forward term meets; otherwise HAND OFF `owner-decision` | one `rescope · item defer` row per carried unit |
| move a shrink-only pin | the kit's history legs grade only the run's own range, so they no longer ask it; a pin the run's own diff must move is HAND OFF `owner-decision` | the decision park row |
| act on another run's record | no act: concurrent runs are permitted, and a landed record derives its terminal | none |
| publish another session's commits | does not arise under `in-place`; under `primary`, HAND OFF `owner-landing` | the handoff row |
| land in a dependency order across repositories | HAND OFF `owner-landing`, the recipe naming each repository in order | the handoff row |
| choose a fix where every option touches a carrier | HAND OFF `owner-decision` | the decision park row |
| a question the default branch already answered | observe the advertised tip first, and take the exit the answer selects; unanswered, HAND OFF `owner-decision` | the park row |

The carry-forward term's per-unit order is the S2 list's order, and each condition returns early
with its own message. That is how the existing terms report, and the reason is the same: a reader
who cannot tell which condition failed reaches for `--override`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_consumes_from` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_consumes_from --as sh.function` answered OK |
| `defer` | rescope act | none |
| `carried forward` | `build-complete` message head | none |
| `The close-decision table` | STOPS section heading | none |

### Rollout

1. Write S3 and S4, then S2, then the carriers S1 and S5 to S8, then re-copy and re-render.
2. Observe each acceptance criterion directly, in the slice and greps it names.
3. Re-stamp the manifest and commit once, with the unit id in the subject.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/STOPS.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/SKILL.template.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `.claude/skills/unattended/SKILL.md`
- `tools/memory-tree/BUILD-METHOD.template.md`
- `memory/guides/BUILD-METHOD.md`
- `memory/guides/SESSION-KICKOFF.md`
- `tools/drift-audit/drift_report.py`
- `tools/drift-audit/selftest.py`
- `tools/runlog/model.py`
- `tools/runlog/selftest.py`

### Alternatives rejected

Each was rejected by a test, and §8 carries the fork it decided.

- **The table as a new PROTOCOL subsection**, where the design placed it. The protocol render
  measures 65589 bytes against a declared cap of 65692, so 103 bytes are free, and the table is about
  2 KB. Fitting it means raising a declared size cap, which is an owner call.
- **A new `--ask` field on the defer row.** It would be a second join between a unit and its ask,
  beside the spec header verbs `asks-disposed` already reads.
- **Carrying forward any DEFERRED unit.** A promoted unit flipped to DEFERRED would then meet both
  `build-complete` and check 2's promotion count, which counts new non-WONTDO ids. M4's severity rule
  forbids exactly that.

## 5. Production-readiness checklist

- security — no new write path. `--rescope --act defer` inherits every field refusal `--rescope`
  already makes, and condition 4 reads the ask witness rather than the run's own prose.
- perf / scale — one spec read per non-terminal unit and one witness call per close; both already
  happen in `asks-disposed`.
- error / empty / loading states — a blank `ASKS_CMD`, an unreadable baseline roster and an
  unreadable spec each leave the term unmet with the reason; none of them reads as met.
- observability — each carried unit prints on its own line, and the defer row is surfaced at the
  wrap-up through `PARK_ACTS_OWED`.
- risks — the protocol render has 103 bytes of headroom at base, and units 13, 14 and 16 also write
  it. If S5's row does not fit after them, the unit parks with the measured figure, because raising
  the cap is an owner call. `TOOL-dUnstuckLanding-17` makes its own row shorter, which helps.
- testing — the arms under §7, each observed through a scratch slice of the driver suite.
- migration — none. A build with no DEFERRED unit grades exactly as before.
- user docs — the stop contract, the protocol row, the verbs entry, the Skill and BUILD-METHOD.

## 6. Acceptance criteria

- **AC1** — When a scratch slice of the driver suite runs the new carry-forward arm, `--close` on a
  fixture build meets `build-complete`. The fixture has one CLOSED unit, and one DEFERRED unit that
  is in the BASE roster, carries a `rescope · item defer` row, and whose spec `closes` an OPEN ask
  filed under the build's slug. The close's output carries `carried forward` naming the DEFERRED unit
  and its ask.
  Red when: term 5 is left as `nonterminal_units` alone, so the DEFERRED row reds the item.
  fixture: the driver suite's own build fixture with a stub `ASKS_CMD`; nothing in this tree is
  needed.
- **AC2** — When the same fixture's CLOSED unit spec declares `**consumes-from**` onto the DEFERRED
  unit, `build-complete` is unmet, and its message names both unit ids and the edge.
  Red when: `read_consumes_from` is staged to print nothing, so the term meets over the edge.
- **AC3** — When the DEFERRED unit's ask is, in turn, absent from `BACKLOG.md`, derived CLOSED by the
  stub witness, or filed under another build's slug, `build-complete` is unmet each time, naming the
  unit.
  Red when: the `asks_filed_by` slug filter is staged out, so another build's ask satisfies the third
  case.
- **AC4** — When the DEFERRED unit is one the run added with `--rescope --act add`, absent from the
  BASE roster, `build-complete` is unmet and names the unit as added during this run.
  Red when: condition 2 is staged out, so a unit the run added is carried forward.
- **AC5** — When the defer row is removed from the fixture's run-state file, `build-complete` is
  unmet and names the missing row.
  Red when: condition 3 is staged out.
- **AC6** — When `--rescope <slug> --act defer --item <unit> --reason <r>` runs in the slice's
  fixture, it writes one `rescope · item defer <unit>` row and exits 0. With `--successor` added, it
  is refused by number. `grep -n '^PARK_ACTS_OWED=' tools/unattended/unattended.sh` prints a value
  carrying `defer`. The kit gate's act-axis grep, copied from `tools/unattended/check-unattended.sh`
  into a scratch script and run against the driver, prints the four-act alternation.
  Red when: the leg's probe still spells the three-act alternation, so it matches nothing and check 2
  would refuse.
- **AC7** — When `grep -c '^## .*The close-decision table' memory/guides/UNATTENDED-STOPS.md` runs it
  prints 1, a grep for each of the seven decision kinds of §4 Data model finds each one in that
  section, and `cmp tools/unattended/STOPS.template.md memory/guides/UNATTENDED-STOPS.md` exits 0.
  Red when: a kind is missing, or the render was not re-copied.
- **AC8** — When `sed -n '/^## M3/,/^## M4/p' memory/guides/BUILD-METHOD.md | grep -c 'never an abort'`
  runs it prints 1, and `wc -c memory/guides/BUILD-METHOD.md` prints at most 30720.
  Red when: the sentence sits outside M3, or the render outgrows its budget.
  figure: 30720 is PINNED, the budget M1 states; the byte count is DERIVED.
- **AC9** — When `grep -n 'build-complete' tools/unattended/PROTOCOL.template.md` runs, the §4 row
  names a unit carried forward. `wc -c memory/guides/UNATTENDED-PROTOCOL.md` prints at most the
  figure `tools/template-size-limits.txt` declares for that path, and
  `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` exits 0.
  Red when: the row is unchanged, the render outgrows its cap, or it was not re-copied.
  figure: both figures are DERIVED at observation time.
- **AC10** — When `grep -n 'TOOL-dUnstuckLanding-23' tools/unattended/unattended.sh` runs, it prints
  a line inside the comment above `build-complete`, and
  `grep -n 'TOOL-dUnstuckLanding-23' memory/DECISIONS.md` prints the ruling row superseding D8.
  Red when: the comment still cites the owner's whole-build rule alone.
  fixture: the DECISIONS row is present at base.
- **AC11** — When `grep -c 'carried forward' tools/unattended/SKILL.template.md` runs it prints at
  least 3, and the same grep over `.claude/skills/unattended/SKILL.md` prints the same number.
  Red when: a waiver sentence still says an override is owed unconditionally, or the rendered Skill
  was not regenerated.
- **AC12** — When `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` runs at the pass's
  commit, it shows the `last-audit:` line moved.
  Red when: `memory/guides/BUILD-METHOD.md` moved in the commit and the stamp did not.
- **AC13** — When `PARK_ACTS_OWED` is read from the driver, `tools/runlog/model.py` and
  `tools/drift-audit/drift_report.py` each spell the same three acts, and runlog's leading
  `LEDGER_SOURCES` are the driver's owed kinds plus `rescope-defer` and the other owed acts.
  Red when: a mirror is left at two acts, so its kit's parity arm reds at the close.
  figure: three acts is DERIVED from the driver at observation time.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `unattended skill wiring` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `build-method size` · `kit/dogfood doc parity` · `method carriers (every pointer declared)` · `harness arms (fail branches armed or pinned)` · `kickoff-manifest ratchet` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `memory hygiene` · `drift-audit selftest` · `runlog selftest` · `runlog record schema` · `pre-push run-log line` · `run-gates run-log line`

New arm: tools/unattended/unattended.test.sh · the carry-forward block: met, the edge, the three ask cases, an added unit, a missing defer row, and `--rescope --act defer` with and without `--successor` · none

The suites themselves are held from the bar by the 2026-08-23 owner ruling. The close runs them
once, under `TOOL-dUnstuckLanding-24`.

## 8. Open questions

- **F1 — Where does the table live?** (a) A new PROTOCOL subsection, as the design placed it.
  (b) A new section of the stop contract, with PROTOCOL's `build-complete` row pointing at it. The
  protocol render has 103 bytes free under its declared cap, and the table needs about 2 KB, so (a)
  means raising the cap. That is a governance change the design did not price, which veto 2 reserves
  for the owner. The stop contract has no declared cap, and it already holds every exit that is not
  LAND, the inherited-red disposition among them. Recommendation (b).
  RESOLVED (agent, 2026-10-04, delegated): (b).
- **F2 — How does a DEFERRED unit join its ask?** (a) The spec header's `closes` or `advances`
  verb. (b) A new `--ask` field on the defer row. (c) A BACKLOG `DEFERRED` disposition row whose
  slot names the unit. (a) is the join `asks-disposed` already reads. (b) adds a grammar, and (c)
  bends a slot that names what an ask waits on. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).
- **F3 — May a unit the run added be carried forward?** (a) Yes. (b) No, only units in the BASE
  roster. (a) lets a promoted BLOCKER or HIGH land deferred, which M4's severity rule forbids, so
  veto 1 discards it. Recommendation (b).
  RESOLVED (agent, 2026-10-04, delegated): (b).
- **F4 — How does the deferral reach the owner?** (a) A fourth rescope act, `defer`, owed through
  `PARK_ACTS_OWED`. (b) A `decision` park row. (c) The spec status alone. (c) drops declared scope
  with nothing recorded, which M3 refuses, so veto 1 discards it. (b) records a question nobody is
  asked, where a deferral is a declared amendment, which is rescope's register. Recommendation (a).
  RESOLVED (agent, 2026-10-04, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief, design §5 at rev-2, review items M5 and
  M14, and the driver, the kit gate, the kit library and the four carriers read at base `98926870`.
- rev-2 · 2026-10-04 · the build pass found an interface S4 did not name: drift-audit and runlog
  each mirror `PARK_ACTS_OWED` and hold it to the driver both ways, so `defer` added to the driver
  alone reds two self-tests at the close. S10 adds both mirrors, the runlog ledger source, one
  fixture row in each kit, and the two driver-suite arms that pin what S4 changes; §4 lists the four
  files and §7 the legs they guard, and AC13 observes the mirrors. No rev-1 criterion moved.
- rev-3 · 2026-10-04 · the bug-class checklist over the build commit selected
  amendment-leaves-its-other-half-standing: protocol §9 still said a run stopping early with units
  unbuilt has one escape, the recorded `--override`. S5 now also names that sentence, which gains
  the recorded deferral beside it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "decide whether a build is complete when some units are deferred with an open ask"`
ranked name-stem neighbours only, `build_*` symbols, and printed `unscanned layers: .sh`, so it
cannot see the driver. No existing seam fits the table itself, which is new prose. The term was read
directly instead, and this unit extends the seams it found there: `build-complete`'s term 5 and
`nonterminal_units` in `tools/unattended/unattended.sh`, and `asks_filed_by`, `run_ask_witness` and
`spec_ask_verbs`, which `asks-disposed` already joins. It also extends `baseline_units` in
`tools/unattended/lib-unattended.sh`, `verb_rescope`'s closed act case with `PARK_ACTS_OWED`, and
`read_fork_cutoff`'s precedent for reading another kit's grammar as text. The recall probe returned
this build's ask, the review's M5, the owner ruling `TOOL-dUnstuckLanding-23`, the parked decision
the ruling answered, and `TOOL-cBriefedPilot-7`, which gave D8 its checker.

Recall terms used: build-complete land-once-done D8 DEFERRED carry-forward partial landing consumes-from edge override close-decision park

The question passed with them: "may a build land its closed units while other units are deferred to
an open ask".
