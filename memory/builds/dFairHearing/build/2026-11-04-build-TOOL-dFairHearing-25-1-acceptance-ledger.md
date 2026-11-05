# Acceptance ledger — TOOL-dFairHearing-25

**Serves:** journal TOOL-dFairHearing-25

Built in three passes: pass (a) `d3c98d523` against spec rev-5, pass (b) `8dd98d252` against rev-7, and pass (c) `7711f0e98` against rev-7, which closed the spec. The main loop drafted this ledger at the close from the four builder returns and the verdict record `2026-11-04-build-TOOL-dFairHearing-25-replay-verdicts.md`. No suite, gate or bar ran in any pass: the probes stood in for the legs, and the spec's gate legs are owed to the close. It declares no `New arm:` line.

**Evidences:** TOOL-dFairHearing-25
- AC1 — `git for-each-ref refs/replay/` — it printed nothing after pass (b) and again at pass (c). Over `fhr1b`, `fhr1c` and `fhr2b` each clone's `HEAD` is its own placement commit, with one commit outside `6cfd21619`'s history, two placed paths and blob `767187aa4073f6e64cb2b2ef6b798f0a538347fd`. Pass (b) saw a second recipe run into `fhr1b` exit 2 before any fetch
- AC2 — `node tools/workflows/spec-audit-optin.js` — the replayed payloads of `fhr1c` and `fhr2b` exited 0 on the placed subject and 2 naming `subjects` on the record's dClosedLoop path. Both reports sit under their clone's `memory/builds/dFairHearing/reviews/`, and each `Reviewed:` line names the placed path at `767187aa`
- AC3 — `replay_scorer.py --experiment` — over the committed manifest it printed `parsed design-audit: 2 of 2` before any figure, and a copy declaring dispatched 1 exited 2. `review_replay.py` printed `reviewed 26/59`, `escaped 1/6` and `high 5/8` for `fhr1c`, and `reviewed 26/59`, `escaped 0/6` and `high 6/8` for `fhr2b`. The verdict record states them against `45/59`, `4/6` and `7/8`. Before the runs, `check_same_file` returned True for the placed path and False for the flat path
- AC4 — amended rev-2 — the spec's hands-off edge to TOOL-dFairHearing-30 moved unit 15's replay out of this unit, so this unit ran no such replay. TOOL-dFairHearing-30 answers this criterion, as the Supersessions section below records
- AC5 — `DESIGN_RECORD_PRESET` — both runs miss in the verdict record, and it reads `unit-spec` at `tools/workflows/review_pin.py:47`, with the template's default `'unit-spec'` at :330. `BACKLOG.md` gains the ask TOOL-dFairHearing-42 with both runs' counts. At pass (b)'s commit the two-phrase grep printed nothing, and the rewritten sentences at lines 457 and 546 each name the constant
- AC6 — `--all-ungated` — pass (c) printed 0 from `grep -c -- --all-ungated gotchas.py`. The decision itself is unit 30's and is superseded out of this unit, see below
- AC7 — `git log --diff-filter=A --format=%P -1 -- <record>` — the record's first parent is `8ee00000a4316a999d4ec270887261ddc22bd651`, the orchestrating commit it names, and its line does not end `(derived)`. Unit 23's `7ff570cfa` is an ancestor, the three blobs equal the adding commit's, and the `git diff --name-only` over the three files printed nothing. Each clone's `HEAD` stands on its own line. The `ungated` class list is superseded, see below
- AC8 — `commit-tree` — it printed at README line 1050, inside the replay section at lines 1033 to 1097, and the placed path printed at line 1083, in the replay-1 paragraph. The trap count read 1, 1 on a copy whose prose holds a trap line, and 2 on a copy with a second trap line. In the `%TEMP%/fpl` fixture with `git bundle create` forced to fail, `refs/replay/` was empty, no temporary index was left, and `git status --porcelain` and `HEAD` were unchanged. The old trap left the index, and no trap left both
- AC9 — `fhr1a` — the record lists run 1's attempts `fhr1b`, void, and `fhr1c`, and run 2's attempt `fhr2b`, each in its own clone, with `fhr1b`'s cause beside it. It names `fhr1a` and `fhr2a` apart as clones no agent read, with the opt-in pack's refusal as the reason, and notes no third attempt. No run was void twice, so the `not run` branch has an empty population and is not counted as coverage

## Supersessions

Each one is named by the hands-off bullet to `TOOL-dFairHearing-30` in this unit's spec, and by that unit's S6.

- `TOOL-dFairHearing-25` S4 and AC4 — unit 15's replay is answered by `TOOL-dFairHearing-30` S1 to S5 and AC1 to AC4
- `TOOL-dFairHearing-25` S5 — the unit-15 half is answered by the same items
- `TOOL-dFairHearing-25` AC6 — answered by the same items
- `TOOL-dFairHearing-25` S6 and AC7 — the unit-15 lines, the `ungated` class set among them, are answered by the same items
