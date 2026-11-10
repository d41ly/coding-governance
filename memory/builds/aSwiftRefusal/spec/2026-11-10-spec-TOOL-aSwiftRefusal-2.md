# TOOL-aSwiftRefusal-2 — the order gate lets a deferred earlier-order unit pass

**Status:** CLOSED · rev-3 · 2026-11-10 · node a · Tier-2 · base ae6735c1 · streams tooling · order 2 · closes TOOL-aRoutedQuill-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-1-agent-ledger.md) | journal | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-3 TOOL-aSwiftRefusal-4 |
| [2026-11-10-build-TOOL-aSwiftRefusal-2-1-acceptance-ledger.md](../build/2026-11-10-build-TOOL-aSwiftRefusal-2-1-acceptance-ledger.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-brief.md) | research | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-3 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-1-token-fix-brief.md) | research | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-3 |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-2-1-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-2-1-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-2-2-spec-writer.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-2-2-spec-writer.md) | journal | — |
| [2026-11-10-prompt-TOOL-aSwiftRefusal-2-edge-fix-brief.md](../prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-2-edge-fix-brief.md) | research | TOOL-aSwiftRefusal-3 |
| [2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md](../reviews/2026-11-10-review-TOOL-aSwiftRefusal-1-3-closing-diff-round1.md) | diff-review | TOOL-aSwiftRefusal-1 TOOL-aSwiftRefusal-3 |

<!-- /gen:spec-records -->

## 1. Goal

`--dispatch`'s order gate stops refusing a unit because an earlier-order sibling was set aside with
`--rescope --act defer`. Today the gate counts a DEFERRED sibling as an unfinished earlier step, so a
run that defers one unit cannot dispatch anything ordered after it without re-ordering specs.

## 2. Scope (IN)

- **S1** — One deferral predicate, `check_unit_deferred`, defined in `tools/unattended/unattended.sh`
  beside `check_pass_open`. It takes the run-state file, a unit id and that unit's spec status, and
  returns 0 only when the status is `DEFERRED` and the unit's last row among its `dispatch` rows and
  its `rescope · item defer` rows, in file order, is a defer row. Observed by AC1.
- **S2** — The order gate's sibling loop asks `check_unit_deferred` after its `CLOSED|WONTDO` skip and
  skips a sibling it answers 0 for, naming that sibling on stderr. The gate's refusal text is
  byte-identical. Observed by AC2, AC3, AC4 and AC7.
- **S3** — The edge refusal is not given the predicate: a unit whose spec consumes from a deferred
  unit of its own build stays refused. Observed by AC5.
- **S4** — A new arm in `tools/unattended/unattended.test.sh` re-observes AC2 to AC5 on the
  two-unit ordered `tRun` fixture, `ARCH-tRun-4` at `order 1` and `ARCH-tRun-5` at `order 2`.
  Observed by AC6.

## 3. Non-goals (OUT)

- The spec-token reorder (TOOL-aSwiftRefusal-1) and the open-pass release in `read_open_passes`
  (TOOL-aSwiftRefusal-3).
- The edge refusal's semantics, `pass_commit`, `check_pass_open`, `check_commit_message`, the hold
  gate and the spec-token checker, per the brief's non-goals.
- Any new `--rescope` act, and any change to how `verb_rescope` writes a defer row.
- The order gate's other unarmed branch, the sibling malformed-order refusal pinned at
  `tools/unattended/unarmed-branches.txt:54`. The `tRun` pair could arm it, and ask
  TOOL-dBriefedPass-6 asks for that with the equal-order and no-order branches; this unit neither
  closes nor advances that ask.
- Any kit version bump: versions move through the lander's `mint`.

### Edges

- **hands-off** `TOOL-aSwiftRefusal-3` — `check_unit_deferred`, which that unit's `read_open_passes`
  change calls rather than defining a second deferral predicate (README build-level rule 2).
- **hands-off** `TOOL-aSwiftRefusal-4` — `check_unit_deferred <run-state file> <unit> <spec status>`,
  which that unit moves into the kit library and calls from `--rescope` and check 23, changing no
  line of its body.

## 4. Design

### The predicate

The run-state file is append-only through `park` (`tools/unattended/unattended.sh:12687-12707`),
which writes `<UTC> <kind> · item <item> · reason <reason>` with no step field from either writer
below, so file order is row order. The two rows it reads:

| Row | Writer | Shape |
|---|---|---|
| dispatch | `verb_dispatch`, `unattended.sh:14674` | `<UTC> dispatch · item <anchor-sha> <unit> · reason <paths>` |
| defer | `verb_rescope`, `unattended.sh:14055` | `<UTC> rescope · item defer <unit> · reason <text>` |

`deviation_join.py:167` parses the defer row with the same grammar. One `awk` pass keeps the kind of
the last matching row for the unit. The unit must be a whole token, matched positionally: the id is
the token directly before ` · reason `, after `dispatch · item <hex> ` or `rescope · item defer `.
That anchoring is the order gate's own (`unattended.sh:14374-14378`); `id_rows`
(`lib-unattended.sh:693`) is not used, because it matches the id anywhere in the line, a reason
field included.

```bash
check_unit_deferred() { # run-state file · unit · spec status -> 0 deferred, 1 not
  [ "$3" = DEFERRED ] || return 1
  awk -v u="$2" '
    $0 ~ ("^[0-9][0-9-]*T[0-9:]*Z dispatch · item [0-9a-f]+ " u " · reason ") { k = "d" }
    $0 ~ ("^[0-9][0-9-]*T[0-9:]*Z rescope · item defer " u " · reason ")      { k = "f" }
    END { exit (k == "f") ? 0 : 1 }' "$1" 2>/dev/null
}
```

Both patterns anchor at line start, so the id is read only in the item field, never in a reason. An
id carries only letters, digits and hyphens, so it is safe inside the dynamic regex, as it already
is in the order gate's grep. An unreadable file answers non-zero (`awk` exits 2), which keeps the sibling
blocking: a failed read is a refusal, never an admission (the convention at `unattended.sh:14131`).
Status is passed in rather than read, because both callers already hold it: the order gate as
`_o_st` (`unattended.sh:14372`), and `read_open_passes` as `_st` (`unattended.sh:14106`).

### The order gate

One line after `case "$_o_st" in CLOSED|WONTDO) continue ;; esac` at `unattended.sh:14373`:

```bash
if check_unit_deferred "$rel" "$_o_id" "$_o_st"; then
  echo "unattended: dispatch — $_o_id (order $_o_ord) is DEFERRED with no dispatch after its defer row, so it does not hold back $unit" >&2
  continue
fi
```

The dispatched-row skip at `unattended.sh:14378` stays as it is. The behaviour change is the cases
below, read from the code; only the first row moves.

| Earlier-order sibling | BASE | After |
|---|---|---|
| DEFERRED, defer row, no dispatch row | blocks | passes, named on stderr |
| DEFERRED, no defer row | blocks | blocks |
| INPROGRESS (or any live status), defer row | blocks | blocks |
| DEFERRED, dispatch row after its defer row | passes as dispatched | passes as dispatched |

The brief's acceptance 3 says a unit whose dispatch row follows its defer row "still blocks". At the
gate it cannot: any dispatched sibling passes at `unattended.sh:14378`, at BASE and after. That case
is observed on the predicate (AC1), which is where it matters, since TOOL-aSwiftRefusal-3's open-pass
reservation reads the same answer.

### The arm

At BASE no suite arm reaches the order gate's blocker message. It is pinned unarmed at
`tools/unattended/unarmed-branches.txt:50`, because the suite's `readme` helper
(`unattended.test.sh:385-406`) writes one units row and `unit_ids_of` (`unattended.sh:4829-4834`)
reads the sibling roster from that region. TOOL-aSwiftRefusal-1, at order 1, builds first. Its AC2
adds the ordered pair `ARCH-tRun-4` and `ARCH-tRun-5` to the `tRun` fixture's units region, and its
AC5 takes the blocker row out of the pin file, since its own arm asserts that message. S4 reuses that
pair, the charter's `[reuse]` rule at a fixture's second instance, and adds the defer and dispatch
rows and spec statuses each case needs. It writes no fixture build and touches no pin row of its own.

If unit 1's pair is not in the suite when this unit builds, unit 1 was retired or deferred. That is a
spec change, so it goes back to the main loop rather than being absorbed here.

### Files touched (estimate)

`tools/unattended/unattended.sh`
`tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Admit on spec status alone.** A DEFERRED status with no defer row is a hand edit that nothing
  recorded, and the close's carry-forward refuses that exact state (`unattended.sh:5490-5491`). Admitting
  it would let the order gate pass a deferral the close will refuse.
- **Admit on a defer row's presence, ignoring dispatch rows.** dOrderedCharter re-dispatched unit 31
  after deferring it (the brief's drawn-from section), and a presence test would release that unit's
  paths in TOOL-aSwiftRefusal-3 while it builds.
- **Read the predicate's status inside it from `SPEC_ST`.** It couples the predicate to the map
  layout (`SPEC_ST` is keyed by spec path, not unit id), and both callers already hold the status.

## 5. Production-readiness checklist

- security — N/A: no new write path, input or surface. The gate only admits a case it refused
  before, and every other refusal in `verb_dispatch` still runs after it.
- perf / scale — one `awk` over the run-state file per earlier-order sibling that reads DEFERRED.
  Others return before the `awk`.
- error / empty / loading states — an unreadable run-state file, or no matching row, answers
  non-zero, and the sibling keeps blocking.
- observability — each admitted sibling is named on stderr, so a pass past a deferral is announced,
  never silent.
- risks — a deferred unit's later-ordered siblings may now build before it. A consumer of it stays
  refused by the edge refusal (S3), so only unrelated work proceeds.
- testing — the predicate is probed directly (AC1), the gate through a fixture repository (AC2 to
  AC5), and S4's suite arm is observed RED then GREEN at the close.
- migration — N/A: no data shape changes; existing run-state files already carry both row kinds.
- user docs — N/A: no page under `help/` covers `--dispatch`, and neither
  `tools/unattended/VERBS.template.md` nor the kit README describes the order gate
  (`grep -n "order gate"` over both returns nothing), so no published sentence goes stale.

## 6. Acceptance criteria

- **AC1** — When `check_unit_deferred` is sliced out of `tools/unattended/unattended.sh` and run over
  scratch run-state files, it returns 0 for DEFERRED with only a defer row, for DEFERRED with a
  dispatch row then a defer row, and for DEFERRED with a defer row followed by `ARCH-tRun-5`'s
  dispatch row whose reason field spells `ARCH-tRun-4 · reason`. It returns 1 for INPROGRESS with a
  defer row, DEFERRED with a defer row then a dispatch row, DEFERRED with no row, and DEFERRED where
  only `ARCH-tRun-44` has a defer row and `ARCH-tRun-4` is asked. A missing file returns non-zero.
  Red when: the predicate ignores the status, reads the first row instead of the last, or matches
  the id as a substring.
  fixture: scratch files under the run's scratchpad; the tree holds none today.
- **AC2** — When `unattended.sh --dispatch tRun --pass ARCH-tRun-5 --writes x` runs in a fixture
  repository where `ARCH-tRun-4` carries `order 1`, reads DEFERRED and has a `rescope · item defer`
  row and no dispatch row, it exits 0, appends the `ARCH-tRun-5` dispatch row, and prints the stderr
  line naming `ARCH-tRun-4`. At BASE the same call exits 49 with `neither terminal nor dispatched`.
  Red when: the `check_unit_deferred` call in the order gate is removed.
  fixture: the `%TEMP%` repository TOOL-aSwiftRefusal-1's AC2 builds, the `tRun` build with both
  units in its units region after `--preflight tRun`, with this criterion's rows and statuses
  written in; outside the suite the tree holds none.
  cost: about a minute when the fixture is rebuilt rather than reused.
- **AC3** — When the same `--dispatch` runs with `ARCH-tRun-4` reading INPROGRESS and carrying the
  defer row, it exits 49 with `an earlier step still holds a unit that is neither terminal nor
  dispatched: ARCH-tRun-4 (order 1, INPROGRESS)`.
  Red when: the order gate admits on the defer row without asking the spec status.
  fixture: AC2's.
- **AC4** — When the same `--dispatch` runs with `ARCH-tRun-4` reading DEFERRED and no defer row in
  the run-state file, it exits 49 with `neither terminal nor dispatched: ARCH-tRun-4 (order 1,
  DEFERRED)`.
  Red when: the order gate admits on the DEFERRED status alone.
  fixture: AC2's.
- **AC5** — When `ARCH-tRun-5`'s spec declares `consumes-from` `ARCH-tRun-4` and AC2's state holds,
  `--dispatch` exits 49 with `consumes from a unit of its own build that is neither CLOSED nor
  WONTDO` naming `ARCH-tRun-4 (DEFERRED)`.
  Red when: the edge refusal is given the deferral predicate.
  fixture: AC2's, with the Edges line added.
- **AC6** — When `grep -nE "does not hold back ARCH-tRun-5|ARCH-tRun-4 \(order 1, (INPROGRESS|DEFERRED)\)"`
  runs over the suite file the §7 `New arm:` line names, it prints a `hit` assertion for each: the
  admission line, the INPROGRESS blocker and the DEFERRED-without-row blocker.
  Red when: the arm is missing, or asserts the admission alone, which passes on a gate that admits
  every DEFERRED sibling.
- **AC7** — When `git show --format= <pass-sha> -- tools/unattended/unattended.sh` runs on this
  unit's pass commit, no removed line carries `fail`.
  Red when: a refusal message in `verb_dispatch` is reworded.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `tier2-review self-test` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `docs` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `pass-order history` · `routed commits name a specced unit` · `brief-recorded`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · staged break: delete the `check_unit_deferred` call in the order gate (the AC2 assertion reds), then call it with `DEFERRED` in place of `$_o_st` (the AC3 assertion reds) · none

The close runs the driver suite's shard that holds the arm, the bar, and the RED-then-GREEN
observation of the arm above. No unit pass runs any of them.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-10 · initial draft.
- rev-2 · 2026-11-10 · the spec-token `[bar]` hit on AC6's backticked suite path folded: AC6 greps
  the suite file the §7 `New arm:` line names, which now names the suite alone; the criterion is
  unchanged.
- rev-3 · 2026-11-10 · §3 Edges · mirrors `TOOL-aSwiftRefusal-4`'s `consumes-from` as `hands-off`,
  which check 12's reciprocity arm reported missing; from
  `memory/builds/aSwiftRefusal/prompts/2026-11-10-prompt-TOOL-aSwiftRefusal-2-edge-fix-brief.md`
  item 1. Nothing else moves.

## 10. Reuse audit

The seams this unit extends, each verified against source at `ae6735c1`. The predicate takes the
0-or-1 shape of `check_pass_open` (`tools/unattended/unattended.sh:14129-14147`), which
`read_open_passes` and `verb_dispatch` already share. It takes its row anchoring from the order
gate's own dispatch-row grep (`unattended.sh:14374-14378`, the brief's "row reader to share"). The
defer-row grammar is the one `verb_rescope` writes (`unattended.sh:14055`) and `deviation_join.py:167`
parses. `tools/codebase-map/reuse_lookup.py "whether a unit is deferred from its rescope defer row and
its spec status"` returned no deferral seam. Its ranked hits were generic row and spec helpers, and
the one in this kit, `id_rows` (`tools/unattended/lib-unattended.sh:693`), matches an id anywhere in a
line, so it is rejected above. The close's carry-forward reads defer rows by presence
(`unattended.sh:5463`, `unattended.sh:5490`) and never by order, so it is not a seam for the
ordering half. Recall returned TOOL-aRoutedQuill-13, the ask this closes, TOOL-dBriefedPass-6, the
unarmed order gate and its fixture limit, and dOrderedCharter's re-dispatch of a deferred unit
through the brief.

Recall terms used: `python tools/memory-recall/query.py "how does the dispatch order gate treat a
deferred unit carried forward by a rescope defer row" --terms "dispatch order gate deferred rescope
defer row run-state blocker sibling earlier step carry-forward"`
