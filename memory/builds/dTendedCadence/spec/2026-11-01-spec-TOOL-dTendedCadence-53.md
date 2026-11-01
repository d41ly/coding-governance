# TOOL-dTendedCadence-53 — a cyclic playbook's repeat text names the last finished cycle's build, so each cycle files once and an open cycle still recurs

**Status:** DEFERRED · rev-1 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 18 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-46 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-49-to-59-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-56 TOOL-dTendedCadence-55 TOOL-dTendedCadence-57 TOOL-dTendedCadence-54 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 15 of `reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md`,
BLOCKER, which shares item B2 with id 40 (TOOL-dTendedCadence-54). Unit 45 makes the repeat intake's
text period-free (spec-45 §4 "The intake", :47-52), so every cycle of one playbook renders one text
and one content key. Unit 8's filing answers `survivor` when a build README naming that key under
`**Caused-by:**` reads CLOSED or WONTDO, and otherwise appends a `seen` receipt to the intake on
record (spec-8 §4 "The patch intake", :199-210). Once the first cycle's repeat build closes, no later
cycle files again, so a cyclic playbook runs one cycle, against unit 11's goal of one repeat intake per
cycle and its S6. This unit keeps the period out of the text and adds what ends a cycle's key: the
slug of the last finished cycle's build.

## 2. Scope (IN)

- **S1** — The reader. `read_caused_by_build(root, ck)` in `tools/drift-audit/readings.py` answers
  `(slug, status)` for the one tracked build README at `HEAD` naming `**Caused-by:** <ck>`, its status
  the `**Build status:**` token, or None; two READMEs naming one key raise naming both.
  `write_patch_intake`'s `survivor` branch (unit 8 S7) calls it, so the lookup is written once.
  Observed by AC1.
- **S2** — The text. `derive_repeat_text(root, path, pieces, cycle)` in
  `tools/drift-audit/playbook_cycle.py` starts from unit 45's four lines. While
  `read_caused_by_build` answers CLOSED or WONTDO for the text's content key, the text takes the fifth
  line `after: <that build's slug>`, in place of any earlier `after:` line, and the key is taken
  again. It stops at the first key with no build or a live one. A slug met twice exits 2 naming it.
  The content key is the one unit 8's filing computes, `request.py key -`
  (TOOL-dPlacedRequest-19 S1). Observed by AC1 and AC2.
- **S3** — The run. `run_repeat_intakes` (unit 11 S5) hands the filing the text S2 returns, so a
  cycle after a finished build files a new intake and a cycle whose build or intake is still open
  appends a receipt, printed `seen <period>` as unit 45 S2 prints it. The filing never answers
  `survivor` for a repeat intake, and no repeat breach reaches `item.maintain.file`. Observed by AC2.
- **S4** — The docs. `help/maintain.md`'s section "Cyclic playbooks" shows the `after:` line and says
  which build it names. Observed by AC3.

## 3. Non-goals (OUT)

- The period on the run's line: unit 45 S2, unchanged.
- An intake closed without a build: unit 45 §5's risk, unchanged; its key has no README, so the
  cycle stays a receipt.
- Placing the new intake as `repeat`: Entry's (TOOL-dPlacedRequest-4), unchanged.
- The two-cycle arm through the real filing: TOOL-dTendedCadence-54.

### Edges

- **consumes-from** `TOOL-dTendedCadence-45` — the period-free four lines, which this unit extends with the `after:` line
- **consumes-from** `TOOL-dTendedCadence-8` — `write_patch_intake`'s `**Caused-by:**` lookup, which this unit extracts as `read_caused_by_build` and calls from both sides
- **hands-off** `TOOL-dTendedCadence-54` — `derive_repeat_text`, whose cycles that unit's arm files through the real filing
- **hands-off** `TOOL-dTendedCadence-59` — `read_caused_by_build`, the committed source that unit's cross-node dedupe reads (review id 41)

## 4. Design

### The text

```
repeat <path>
playbook: <path>
pieces: <cycle_pieces>
cycle: <daily|weekly>
after: <slug of the last CLOSED or WONTDO build of this chain>     # absent on the first cycle
```

```
derive_repeat_text(root, path, pieces, cycle):
    text = unit 45's four lines;  met = {}
    loop:
        found = read_caused_by_build(root, key(text))
        found is None or found.status not in (CLOSED, WONTDO)  -> return text
        found.slug in met                                       -> exit 2
        met += found.slug;  text = four lines + "after: " + found.slug
```

Each finished cycle names its own build, so the chain from the first key runs one step per finished
cycle and ends at the open one. The text still carries no period, value or sha, so unit 8's rule
holds: one cycle, one key.

### Evidence

- Spec-8 :201-206 answers `survivor` from a CLOSED or WONTDO README naming the key, and `seen` from
  `intake.py show <ck>` exiting 0.
- Spec-11 S6 (:76-79) conditions `seen` on the previous intake being still open.
- Spec-47 S2 closes the same class for breach asks with `· regressed after <ask id>`.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `read_caused_by_build` | function, `readings.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `derive_repeat_text` | function, `playbook_cycle.py` | `py.function`, OK by `lexicon.py --suggest` at writing |
| `after:` | repeat intake text line | none |

### Files touched (estimate)

- `tools/drift-audit/readings.py`: S1
- `tools/drift-audit/playbook_cycle.py`: S2, S3
- `tools/drift-audit/selftest.py`: the cases of §6
- `help/maintain.md`: S4

### Alternatives rejected

- **The cycle ordinal in the text.** It is a count no record holds, so two nodes can disagree on it,
  and it moves on a cycle whose build is still open.
- **Route `survivor` for a repeat to a re-filing with a clause.** The caller would learn the build only
  after a filing it then discards; deciding the text first files once.

## 5. Production-readiness checklist

- security — N/A — the text names a tracked path, two counts and a build slug.
- perf / scale — one `git grep -F` per finished cycle of the chain, bounded by its builds.
- error / empty / loading states — no README for a key ends the chain; two READMEs for one key and a
  repeated slug exit 2 naming them.
- observability — the run line names the content key filed, as unit 11 S5 prints it.
- risks — a build README rewritten to name another key breaks its chain at that step, which then files
  a new intake.
- testing — the criteria of §6.
- migration — N/A — the filer is new in this build.
- user docs — `help/maintain.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `derive_repeat_text` runs in a fixture where no README names the first key, it
  returns unit 45's four lines; with a README naming that key planted CLOSED as `rB1`, it returns
  five lines ending `after: rB1`; with a second README `rB2` naming that text's key planted OPEN, it
  returns the `after: rB1` text again.
  Red when: a finished cycle's key is returned, or an open cycle's chain moves past its build.
- **AC2** — When `python playbook_cycle.py --cycle weekly` runs over unit 11's `file-weekly` plant
  with `rB1` planted CLOSED and a recording filer, the recorded text ends `after: rB1`, the filing's
  answer is `filed`, and the filer recorded is `playbook-cycle-weekly`, never `item.maintain.file`.
  Red when: a cycle after a closed build is absorbed as `seen` or handed on as a survivor.
- **AC3** — When `grep -n "after:" maintain.md` runs in `help/`, it matches inside "Cyclic playbooks".
  Red when: the page omits the line.

## 7. Gates

`drift-audit selftest` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · planted CLOSED and OPEN READMEs naming chained keys and a recording filer, staged against the period-free text with no `after:` line · none

## 8. Open questions

- **F1 — What ends a cycle's key?** Options: (a) the slug of the last finished build of the chain; (b)
  the cycle ordinal; (c) the period, unit 11 as first written. (c) is unit 45's defect reversed: an
  open cycle stacks a second build. (b) is counted by no record. RESOLVED (agent, 2026-11-01,
  delegated): (a), rung 3, the report's first option and the one a committed README already holds.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 15 (BLOCKER, item B2) of the round-1
  spec audit of units 35 to 48.

## 10. Reuse audit

The seams extended are unit 8's `write_patch_intake`, whose README lookup becomes the shared reader,
and unit 45's text. `python tools/codebase-map/reuse_lookup.py "find the build a request caused and
whether it closed"` ranked name stems only, `build`, `build_commit`
(`tools/unattended/lib-unattended.sh`) and `build_grammar` (`tools/memory-tree/backlog.py`), none a
reader of a README's `**Caused-by:**` line, and `readings.py` is absent at base, so no existing seam
fits beyond unit 8's own lookup.

Recall terms used: `python tools/memory-recall/query.py "how does a cyclic playbook file one repeat
intake per cycle once a cycle's build closed" --terms "repeat intake cycle playbook content key
survivor seen Caused-by build closed period-free"`
