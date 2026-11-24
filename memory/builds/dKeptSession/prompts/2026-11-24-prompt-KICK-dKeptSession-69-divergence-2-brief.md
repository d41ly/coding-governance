**Serves:** research KICK-dKeptSession-69

# Brief — dKeptSession: KICK-dKeptSession-69's criteria that its own route cannot meet, amended before it closes

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-69 is DEFERRED to the close. Its reconcile merged as `ad02f1a6a`, and its ledger still owes AC2, AC3,
AC9 and AC11 to AC14. The main loop read each one at the close. Every fact behind them holds, and five criteria read
as written cannot: they ask for a trailer check 49 refuses, a leg the bar holds, or a command that does not parse.
Revise the spec to what was built and can be observed. No code changes.

### Items

1. AC2 and S1, the trailer: `ad02f1a6a` carries `Pass: none`, since check 49 can admit no merge trailered with a unit
   id. KICK-dKeptSession-80 rev-2 §4 "Two commits" gives the reason and names the checks; point at it and do not
   restate it. AC2 reads both parents at `ad02f1a6a`, `8b8b1374c4fc89be2ae3a5aae88dafd74e6acd8e` and `e7ab8c81`, the
   merge's `Pass: none` once, and `Pass: KICK-dKeptSession-69` once on the unit's closing pass commit.
2. AC3, AC11, AC12, AC13 and AC14 say which commit they read. `git diff HEAD^2 HEAD` in AC11 and AC12 becomes
   `git diff ad02f1a6a^2 ad02f1a6a`; everything else reads at the run head the close is at.
3. AC9: `policy fixtures` is a held leg (subject `kit`), which the bar runs only under `GATE_SELFTESTS=1`, and the owner
   holds that flag. AC9 reads the three cases through `python tools/policy/check_policy.py --fixture <case>`, each
   exiting 0 and printing `0 wrong`. Its `permission:` line says why. AC18's last sentence reads the same three runs.
4. AC8 and AC16: at `ad02f1a6a` the leg exits 1 over seven `arm_reader_coverage` findings `8b8b1374` prints too, which
   the ledger's AC16 answer records as INHERITED. AC8 reads the `arm_reader_join` and `arm_purposes` lines, each with
   no finding, and not the leg's exit; AC16 keeps its INHERITED clause and drops "AC8's run prints no
   `arm_reader_coverage` finding", which its own INHERITED clause contradicts.
5. AC17: the pipe into two greps is two commands, each a `tr -s` of the ledger into one `grep -c`.
6. Bump the spec one rev, with one revision-log line naming this brief by its file stem. Leave the status cell
   DEFERRED. Keep it under the live-spec cap, and pin every figure.

### Acceptance

These report nothing for the spec:
- `bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`
- `python tools/check-spec-tokens.py --spec <path>`
- `bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-69`
- a PLAIN `python tools/playbook/writing_practice.py check pinned-facts`

### Gates

The spec's own checks above. No suite and no bar.

### Non-goals

- No edit to any other spec, no ledger edit and no product code.
- No commit: the main loop commits the revision.
- No criterion is weakened beyond the items above. AC1, AC4 to AC7, AC10 and AC15 stand.
