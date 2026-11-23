# KICK-dKeptSession-11 — acceptance ledger

**Serves:** journal KICK-dKeptSession-11

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on win32
at the pass's base `0b4ff26da` over the working tree before the commit: by the unit's own plants, each
run alone by direct CLI (`loop_transition.py --fixture --plant <case>`); by an in-process probe running
`run_selftest` with its case list narrowed to the unit's fourteen cases, the tree's `definition`,
`default check` and `line-drift` among them; by scratch probes of this pass's own calling the sourced
driver's `print_progress` through `breakpoints.run_sourced`; and by the greps and one-liners AC4 to AC8
state.

Before the first edit the spec's cited code was probed at the base, units 24, 10, 25, 21, 6, 7, 35, 42
and 8 read as landed: `tools/loop/loop_transition.py#read_record_channels` held the policy read
`read_policy_value` extracts; `tools/loop/loop_transition.py#check_transition_definition` was read by
`check_transition_channels` and `run_selftest` alone; `tools/loop/loop_transition.py#write_transition`
read the set at HEAD before the mail guard, its `said` ending with the card follow's lines then the
Design exit's notices; `tools/loop/loop_transition.py#write_transition_plant` wrote one definition into
the fence; `tools/unattended/unattended.sh#run_loop_verb` sets `_bd_out`, `_bd_why` and `_bd_rc`;
`tools/unattended/unattended.sh#verb_park` echoes `decision parked —` after its stage and returns 0 on
the `already parked, unchanged` path before it; `tools/unattended/unattended.sh#verb_landed` returns 0 at
the in-place exit after its `phase LANDED (derived: …)` line and at the recorded exit after the `fi`
closing its two `phase LANDED · witness` lines, each ahead of `write_landed_notices`; the catalogue row
`notify.owner` and the charter's fence stood as S1 and S6 state. `PLANTS` held 26 (DERIVED,
`len(PLANTS)` at `0b4ff26da`), the count §4 expects once units 24, 7, 35 and 42 land.

How the build reconciled the spec's text with what landed: the bare-verb refusal read
`a verb, record, check or dependents, or --fixture --plant <case>` once unit 7 landed, so it now reads
`a verb, record, check, dependents or progress, or --fixture --plant <case>`; no arm greps it
(DERIVED, a grep of the tree). The budget row read proxy `r` 172.8 s and 260 (PINNED in the row's note, by unit 42) where §4's
table summed 141.3 s and 235, so it was re-read from unit 42's reading. The floors read 4173 and 1390
(DERIVED, the last assignment of each at `0b4ff26da`) where §4 read 4108 and 1325. `print_progress`
drops each carriage return of `_bd_out`, since a Windows python writes `\r\n` into the command
substitution (DERIVED, `od -c` of a capture), and the suite's arm compares whole lines. A policy file
whose `notify.owner` value is refused refuses `transitions.record` too, since the policy kit refuses the
revision whole, so `record` then exits 2 on the set before the `unread` line can print (DERIVED, a
scratch committing `owner = "loud"`); the line was observed under a read of `notify.owner` alone stood in
to raise.

## Criteria

**Evidences:** KICK-dKeptSession-11
- AC1 — `--fixture --plant notify-every` printed `progress — tFix · transition · planning → designing · item.plan.exit` before its `loop: recorded` line, then `progress — tFix · park · item fx-fork`, the landing line naming the witness's sha8 and `loop: fixture · progress 3`, exit 0; `notify-micro` printed no `progress —` line and `loop: fixture · progress 0`, exit 0 (DERIVED, the plants).
- AC2 — `notify-park-landing` printed its park and landing lines and `loop: fixture · progress 2`; `notify-park-only` its park line and `loop: fixture · progress 1`, each exit 0; `progress --build tFix --event lunch --detail x` printed `loop: unanswered · the event lunch is none of park, landing, transition`, exit 2, by CLI and as the in-process `run_selftest` case (DERIVED, the plants and the narrowed probe).
- AC3 — a sourced driver's `print_progress tRun park "item q"` over a scratch committing `[notify]` `owner = "park-only"` printed `progress — tRun · park · item q` and its landing call nothing; under `park-and-landing` both printed, the landing `progress — tRun · landing · abcdef12`; with no `notify` key neither printed; an event `lunch` printed the verb's `loop: unanswered` refusal; each returned 0 (DERIVED, the probe). `--park` and `--landed` themselves are the suite's arm, the close's.
- AC4 — the grep found the definition on the template's line 58, inside the microformats fence; `notify-shape` printed `loop: transition · definition · AGENTS.md reads progress — <slug> · <event>, while the renderer writes progress — <slug> · <event> · <detail>` and `· 1 finding(s)`, exit 1; `default` still printed `· 0 finding(s)` and the tree's `definition` case read `held` over the re-rendered `AGENTS.md` (DERIVED, the plants and the narrowed probe).
- AC5 — `grep -c 'notify.owner' loop.md` in `help/` printed 2 (DERIVED, that grep).
- AC6 — the one-liner printed `dKeptSession turn-micro-formats` and `policy.py get notify.owner` printed `turn-micro-formats` (DERIVED, those commands).
- AC7 — the probe printed 31 and the grep `plants=31`, and the five `notify-*` plants are keys of `PLANTS` (DERIVED, those commands).
- AC8 — `PROGRESS_LINE` 3 lines in the loop README, `notify.owner` 1 in the loop `kit.toml`, and the usage line found in `loop_transition.py`'s docstring and the README's usage block (DERIVED, those greps).

The five plants read 1.48, 1.45, 1.41, 1.46 and 1.57 s alone on node d (PINNED 2026-11-23, `date`
around each run), 7.4 s (DERIVED, their sum rounded), and one in-process `notify.owner` read 0.083 s
(PINNED 2026-11-23, ten reads timed), 5.8 s over at most 70 recorded moves (DERIVED, the product), so
the row's proxy `r` is 186.0 s and its budget 279 (DERIVED, x1.5), 159 s past the leg's 120 s ceiling
(PINNED 2026-11-23, `tools/gate-legs.json`), the owner's to raise and not raised here. The charter render
reads 23597 bytes (DERIVED, `wc -c`) and `--bump` moved the high-water from 23574; the `[events]` line is
197 characters (DERIVED, `len`). `check-arms.py --report`'s ceiling row read the driver at `347/347`
after the edits (DERIVED, that run). No added driver line carries `exit 1`, `status=1` or a `fail` call,
and none is a `while` loop fed by `<<<` or a heredoc (DERIVED, the diff's added lines). The new suite
block counts 3 region-eight `same` (DERIVED, its own lines), raising `FLOOR_ASSERTIONS` to 4176 and
`FLOOR_SHARD_8` to 1393, each with its `RAISED` line. `docs_leg.py --fingerprints` printed
`script:tools/loop/loop_transition.py#progress 0eca9616` (DERIVED, that run), the anchor the page
carries, and left the bare script row at `930359dc`. `python tools/lexicon/lexicon.py` exited 1 on its
verb-offender pin, 1432 over 1421 (DERIVED, that run), the count units 6 and 7 read at their bases, and
its output names none of this unit's functions. `gen_map.py --write` added `check_line_definition`,
`derive_owner_events`, `read_policy_value`, `render_progress_line` and `print_progress` and dropped
`check_transition_definition` in `memory/map/generated/symbols.json`, and rewrote no other map file.
The RED-first observations of the plants and the suite block, and the legs of §7, are the close's.
