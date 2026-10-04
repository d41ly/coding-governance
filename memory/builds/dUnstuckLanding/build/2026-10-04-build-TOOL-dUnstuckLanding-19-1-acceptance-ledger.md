# TOOL-dUnstuckLanding-19 — acceptance ledger

**Serves:** journal TOOL-dUnstuckLanding-19

No merge bar and no self-test suite ran in this pass. Fixture F was built by a hermetic probe on
throwaway repositories under the user temp directory: a bare origin advertising HEAD, a clone on a
`unit` branch, a preflighted record with both attested items and one `dispatch` row declaring
work/a.txt, and three commits pushed to the origin's main from a second clone. The driver suite's new
block, run alone under a stub harness carrying the suite's own `hit`, `miss` and `same`, reported 28
assertions passing. A staged break that dropped the pathspec from the listing made the same block red
on exactly the other.txt row. The driver suite itself is owed to the close.

**Evidences:** TOOL-dUnstuckLanding-19
- AC1 — `2 of 3 commits` — the park printed the refresh line reading `2 of 3 commits since BASE`,
  listed the README and work/a.txt commits and not other.txt's, and the record read
  `refreshed-at: <origin main sha> · park · 2 touching`; a repeat of the same park printed no
  refresh line and left the record's blob unchanged.
- AC2 — `phase: ABORTED` — the abort printed the same two rows and the record read
  `refreshed-at: <sha> · abort · 2 touching` beside `phase: ABORTED`.
- AC3 — `· handoff · 2 touching` — after a committed park, `--handoff --code owner-decision`
  printed the two rows and `phase HELD · code owner-decision`, and the fact read
  `<sha> · handoff · 2 touching`.
- AC4 — `LANDER_MODE=primary` — a close with `parked-surfaced` removed printed the refresh line
  before the unmet attested item, exited 1, and left the record's blob unchanged; with overrides on
  `build-complete` and `closing-review-recorded` the close printed `close OK` and the record read
  `refreshed-at: <sha> · close · 2 touching` beside `phase: LANDING`.
- AC5 — `refreshed-at: unobserved · park` — with the origin pointed at a path that does not exist,
  after an earlier park recorded a tip, the park exited 0, printed that the advertised tip was NOT
  observed, parked q5, and the fact read `unobserved · park`.
- AC6 — `refreshed-at: <sha> · park · unlisted` — with the three commits unfetched, the park
  printed that the remote advertises a tip this clone does not have and recorded
  `<origin main sha> · park · unlisted`.
- AC7 — `LANDER_MODE=in-place` — the in-place close with an unmet item printed no `refresh —` line.
- AC8 — amended rev-2 — the helper is `derive_refreshed_at`, since the lexicon holds no `refresh`
  verb; the awk slice of it under that name piped to the grep printed `0`.
- AC9 — `cmp` — PROTOCOL section 2 carries fact 17, each of the four VERBS entries names
  `refreshed-at`, and `cmp` of each template against its render after `adopt-unattended.sh` reported
  no difference.
