# Acceptance ledger — TOOL-dFairHearing-9

**Serves:** journal TOOL-dFairHearing-9

Built against spec rev-2 and committed as pass commit `c70d6a020`, at parent `15c032dc2`. The main loop drafted this ledger at the close from the builder return `2026-11-02-build-TOOL-dFairHearing-9-1-builder-return.md` and the pass commit's message; nothing below was observed again for it. No suite, gate or bar ran in the pass: both `New arm:` lines, their floors of 418 and 905, and the spec's legs are owed to the close.

The close observed this unit's `New arm:` lines on 2026-11-08 at `4896589bc`: each row, RED or UNSEEN with its log line, is in `2026-11-08-build-TOOL-dFairHearing-1-arm-observations.md`, and every suite holding them exits 0 at that tip.

**Evidences:** TOOL-dFairHearing-9
- AC1 — `tools/memory-tree/gotchas.py` — `--for-paths` listed `portability-sweep` for `tools/check-wiring.sh`, `topology-sweep` for `tools/push-main.sh` and `adopter-migration-sweep` for `tools/govkit/registry.toml`, and none of the three for `tools/workflows/README.md`
- AC2 — `build_record` — a probe over each new record and its members showed every anchor of the record an anchor of a member, every member sharing one with it, and `universal` false
- AC3 — `python tools/memory-tree/gotchas.py --check` — it exited 0, and `--report` counted 6 universal records
- AC4 — `tools/workflows/tier2-review.js` — a scratch AsyncFunction harness modelled on the suite's stub agents, run over the new harness and over base at `HEAD~1`, showed each preset reading only its own entry. Both AC4 cases were red on base and passed on the new harness
- AC5 — `blast-radius` — the same harness's `topology` swap read `T` and reported `blast-radius` unread. Red on base, passing on the new harness
- AC6 — `lensNotes` — the three refusals threw before any agent, and the mixed object named both forms. The mixed-form case was red on base. The two typo cases already passed on base, which also names the legal keys
- AC7 — `lensNotes` — one key for the flat form, the per-preset form and base's harness over the flat form. Red on base, passing on the new harness
- AC8 — `tools/workflows/unattended-build.js` — a probe modelled on `run_wf` showed the build harness forwarding the `lensNotes` map unchanged and sending no key without it. Red on base, green after
- AC9 — `unit-spec` — the grep shows it in the `lensNotes` section of `tools/workflows/README.md`. The return records one wording defect in that section, a misplaced pair of sentences, which this grep does not read
