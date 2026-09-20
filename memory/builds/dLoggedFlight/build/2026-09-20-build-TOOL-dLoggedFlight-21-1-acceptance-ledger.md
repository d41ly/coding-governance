# Acceptance ledger — TOOL-dLoggedFlight-21

**Serves:** journal TOOL-dLoggedFlight-21

Tier-2 · node d · 2026-09-20 · the build pass of the commitment, against spec rev-2. Nothing in the
spec's design moved, so the pass flips its status and bumps no rev. The round-6 spec audit, the review
record naming this unit, drew no item against it.

No suite and no gate leg ran, per the owner's instruction of 2026-09-13: `tools/runlog/selftest.py`
was not run, imported or copied, and neither was any other suite. The change was observed instead by
one throwaway Python script kept outside the repository. It put the kit on `sys.path`, imported
`runlog_lib`, `model` and `record`, typed its own synthetic driver journal and its own `RunModel`, and
called `measure_commitment`, `render_record`, `parse_record` and `COMMITMENT_RE` over them. Twenty-one
observations held, including every staged break it could reach in memory. The two arm verdicts are
owed to the post-build run, each with the break that stages it RED named beside it.

An earlier attempt at this unit ran `--dispatch` and `--brief` and was killed by a usage limit before
it wrote code. Both verbs were re-run today; the brief was already recorded and unchanged, so the
driver said so rather than writing a second row.

## The criteria

**Evidences:** TOOL-dLoggedFlight-21

- AC1 — `measure_commitment` — over a synthetic model whose `journal_lines` names six driver lines,
  `measure_commitment` returned exactly `sha256` and `lines`, the count was six, and `render_record`
  rendered the Summary fact as `sha256` plus 64 hex characters and `lines 6`, byte-identical in the
  markdown and in the Data twin. `COMMITMENT_RE` fullmatched it and its two groups were the digest and
  the count. The value carries no `first`, no `last`, no `utc` token and no ISO date, and the render
  withheld nothing. Liveness: the four-field shape the old regex wanted does NOT match what renders,
  so the arm can distinguish the two.
- AC2 — `measure_commitment` — the recompute path, over the four cases S4 states, each measured with
  `count` set to the committed six. The untouched journal recomputed as committed. A line the run
  appended after the render recomputed as committed, so an append is not an edit. A line of the run
  inserted among the hashed ones changed the digest while the count held, so only `sha256` is named. An
  edited hashed line changed the digest with the count unchanged. A deleted hashed line changed both.
  Liveness: the digest is not the hash of an empty input, so it is the lines that are hashed and not
  the count. The CLI half — `runlog.py verify` exiting 0, 1 and 2 over the rotation fixture — is owed:
  `test_record_ac5_verify`, whose commitment-shape assertion now ends at the count, staged RED by the
  inserted line the arm writes into its own journal, or by reverting `check_commitment` to a floor.
  MET at the post-build run: `test_record_ac5_verify` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC3 — `TEMPLATE_PARSERS` — the pair check's logic was observed directly by the same script:
  `TEMPLATE_PARSERS` maps `commitment` to `COMMITMENT_RE` and nothing else, a clean render parsed in
  both copies, and with the schema's `commitment` template widened by a third field while the regex was
  left, the check named `commitment` and nothing else. The schema tuple was restored and asserted
  restored. The arm itself is owed: `test_record_template_pairs`, staged RED by that same widening,
  which it applies to the schema's own tuple inside a `try`/`finally`.
  MET at the post-build run: `test_record_template_pairs` is GREEN, inside `runlog selftest`'s
  `1543 passed, 0 failed (1543 assertions, floor 1543)`.
- AC4 — `grep -n "committed first" tools/runlog/README.md tools/runlog/record.py memory/map/features/runlog.md` — run directly, it exits 1 and finds nothing. The README's commitment paragraph now names the time-ordered prefix and the START of it, the module docstring says the count is the whole anchor, and the dossier's sentence says the commitment is a digest and a count with no time.

## What else the pass carried

- The residue bullet was REPLACED rather than removed. "A line inserted before the committed first
  time" is no longer a residue — S4 reports it. What remains is which line of a shifted prefix moved,
  which `verify` cannot say, because it holds a hash and a count and nothing positional.
- `render_journal_bytes` in the suite splices lines into a producer file BY TIME, so an arm staging an
  insertion does not also leave the file non-monotonic. `scan_template_pairs` is the pair check itself,
  so the clean arm and the staged break grade through one predicate.
- The suite's floor rises from 1338 to 1348: the one new arm's four checks plus the three decoy checks
  every arm carries, and AC2's three inside an arm that already existed. Two helpers arrive with none.
- `python tools/lexicon/lexicon.py --suggest` answered `OK` for `render_journal_bytes`,
  `scan_template_pairs` and `test_record_template_pairs`, each leading with a declared verb, so
  `VERB_OFFENDER_PIN` does not move. That query is not the leg.
- The runlog dossier lists `TOOL-dLoggedFlight-21` among its decisions and `memory/map/generated` was
  regenerated in the code commit; the three new function names are in `symbols.json`.
- **The dossier has almost no room left.** It sat 5 bytes under check 6's `DOSSIER_CAP_BYTES` before
  this unit, so the first draft of its commitment sentence put the file 452 bytes over and the cap was
  measured, not assumed. What landed is a one-sentence summary at 20 bytes of margin, and the full
  statement of S3 and S4 lives in the kit README and the `record.py` docstring, which have no cap.
  Units `-20`, `-22`, `-23`, `-24` and `-27` all still owe dossier prose and cannot each spend 20
  bytes. Splitting the dossier is what check 6 prescribes at the cap and it is a unit, not an edit, so
  it is named here rather than attempted.
- No committed run record exists in this tree, so nothing needs to read a four-field commitment line.
  The rendered Skill names the commitment nowhere, so it was not re-rendered.
- The sibling specs that consume this unit — `-20`, `-22`, `-23` and `-24` — already describe a
  commitment with no time, so no spec disagrees with what landed.

## Owed to the post-build gate run

- `runlog selftest` — `test_record_template_pairs` and the three new assertions in
  `test_record_ac5_verify`, at a floor of 1348, plus every record arm whose commitment value is now
  two fields. Its budget row moves by one more `build_class_model`, which builds a landed fixture.
- `lexicon naming predicates`, `codebase-map coverage + freshness` and `memory hygiene`, the gates the
  spec's section 7 names.

The post-build run happened at `9e948546`, the whole bar with every guard lifted and the kit
self-tests on: 111 legs ran and 110 are GREEN, in 690.8 s of wall at width 8 against the profile's
declared 21600 s. `runlog selftest` printed `1543 passed, 0 failed (1543 assertions, floor 1543)`,
so both owed arms are GREEN; this unit's floor of 1348 has risen with the units after it. The run
settles the hand-derived chain that carried it there: executed equals floor exactly, so no step in
it ever put the floor above the true total. The suite cost 80 s run directly, under the 93 s its
budget row declares, so `tools/run-gates/selftest-budgets.txt` does not move; inside the bar's
8-wide pool the same leg recorded 93.9 s, a contention reading that file's own header says to
re-read on a quiet box. `lexicon naming predicates`, `codebase-map coverage + freshness` and
`memory hygiene` are GREEN too. The run's one RED, `govkit selftest`, is on none of these legs:
its 30 failing assertions are the IDENTICAL set `origin/main` carries, pre-existing, untouched by
this build and being fixed in a separate session. It is not called green here.
