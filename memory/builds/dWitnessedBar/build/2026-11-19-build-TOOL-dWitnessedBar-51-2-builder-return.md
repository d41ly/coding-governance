**Serves:** journal TOOL-dWitnessedBar-51

# TOOL-dWitnessedBar-51 — builder return 2 (run `wf_3454832f-9ef`), committed 55e427e66a73824c5943546e4b4d00d150472073

## Why

TOOL-dWitnessedBar-51 is built from spec rev-7 and committed as one pass commit. The pass picked up the unverified partial edits the earlier builder left in 43 files, checked each one against the spec, and finished what was missing. The commit carries the `Pass: TOOL-dWitnessedBar-51` trailer and sets the spec status header to CLOSED, dated 2026-11-20. (DERIVED from the builder's probe)

## Summary

Pass commit 55e427e66 on base 99c65d5e3. 57 files changed. Every hook passed on the second attempt.

**Checked from the resumed pass (unverified until now):**
- S2, S4/S20, S5/S6, S8, S13, S15, S16, S19, S21, S25, S27–S29, S31–S37, S44, S45, S47, S48, S50 and S51 are in the tree and match the spec.
- The new inline blocks (`acceptance_reader`, `arm_walk`, `hold_predicate`) and every `resolve_bash_py` and `legacy_ledger_py` copy match their canonicals byte for byte. I checked this by running the parity extractor by hand.
- I fixed one defect in its work. The S32/AC28 fixture line in `tools/lib/resolve-python.test.sh` used a `printf` that wrote a Python file with an unterminated string. It is now written line by line.

**Added in this pass:**
- **S1:** I measured shell-role after all edits: 23 files grown, 1 new (`tools/run-gates/lib-verdict.sh`), 3 shrunk. All 24 grown or new keys went through one `ratchet.py widen shell-role ... --unit TOOL-dWitnessedBar-51`, which wrote `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-51-widen-1.md`. Every owed row was then set to its measured count. A re-measure shows no difference, and all 24 `widened:` rows name `widen-1`. (DERIVED from the builder's probe)
- **AC27 arm:** three new cases (1m) in `tools/memory-tree/merge-rows.test.sh`.
- **Deviation records:** `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-51-deviation-514.md` (S15, departs from the dClosedLoop `test.flakes` row) and `memory/builds/dWitnessedBar/build/2026-11-20-build-TOOL-dWitnessedBar-51-deviation-515.md` (F2: Bound, Tier, Reason). Both pass `build_records.py read`.
- **Acceptance ledger:** `memory/builds/dWitnessedBar/build/2026-11-19-build-TOOL-dWitnessedBar-51-1-acceptance-ledger.md`, one line per criterion.
- **Records and regenerated files:** `memory/guides/SESSION-KICKOFF.md` `last-audit` re-stamped at the base, the codebase map's `symbols.json` regenerated, and `gen_build_index.py --write` output committed.
- `owed_rows.py --base HEAD` reported 0 rows owed and one size breach that the warn setting admits. (DERIVED from the builder's probe)

**Write set:** my `--dispatch` for the five added paths replaced the earlier declared set instead of adding to it, so the commit hook (check 49) refused the first commit. I re-declared the union the refusal printed, all paths already in the spec's Files touched, and the second commit passed.

**Checks that ran (probes, standing in for the gates named):**
- AC2: `seen_red.py` fixtures `unseen-arm-with-args` exited 1, `arm-outside-gates` exited 0, and `--build dWitnessedBar` owes `shell-hygiene selftest` and `product-test contract (tests.product)`. Stands in for `memory-hygiene self-test`.
- AC6, AC26, AC29: `ratchet.py --fixture` plants `cutoff-none`, `no-base-remedy`, `cutoff-later`, `cutoff-blank`, `new-population` and `regrammared` all passed. Stands in for `ratchet selftest`.
- AC16, AC31: `fix_keeps.py --fixture` plants `light-profile`, `writes-fixture`, `writes-product`, `writes-test-file` and `acceptance-fixture` all passed. These cover the waived unattended suite.
- AC17: `drift_report.py --gate-health --fixture` `held`, `differs` and `short` all read OK. Stands in for `drift-audit selftest`.
- AC12: `cmd_flakes(record_only=True)` over a planted green run wrote one record under `record` and `quarantine` with no re-entry line, and nothing under `retry-only`.
- AC13: `inherited_red.py up` over a scratch target printed the `undeclared` line.
- AC21: `run_probe_in_empty_dir` returned None when `Refusal` was raised.
- AC25: `refuse-wrong-shell.sh --coverage` over a scratch repo exited 1 naming `late.sh` only; over the real tree it read 93 members and exited 0. Stands in for `python resolver`.
- AC28, AC40, AC41: seed probes in `%TEMP%/ll51` printed `armed p 1` under `sys.executable` at the root, and `refused p header disagrees` with exit 2 and the home unchanged. The `conf-scalar-pins` argv resolves `{prefix}`.
- AC27: `merge-rows.py` over the three planted cases.
- AC30: `render_cut_tail` and `render_fenced` (8191 bytes that decode, a 4-backtick fence, forged field lines shielded). (DERIVED from the builder's probe)
- AC5: `check_declarations` with no `purpose` names the leg.
- AC35: tags re-derived for the 16 rows with no mismatch. (DERIVED from the builder's probe)
- AC3, AC11, AC14, AC15, AC19, AC20, AC23, AC36–AC39: greps and the AC15 probe.
- The naming lexicon passed all 11 new names.

**Finding on AC27:** removed-against-changed exits 1 only through the driver's whole-file RowLoss fallback, not a per-key conflict region. It behaves the same at HEAD, and I recorded this in a `Decided:` trailer.

**Owed to the close (main loop):**
- Every leg of section 7, and in particular:
  - AC1: the `portability (shell lines only shrink)` leg and `ratchet.py never-gains`.
  - AC4: the `--print-bindings` fixture.
  - AC5, AC30: the `--selftest` runs.
  - AC7, AC8, AC33, AC34: present at HEAD, not re-run here.
  - AC10: `check-memory-hygiene.sh --only 3` in a scratch adopter.
  - AC14: `check-arms.py --check`.
  - AC18: `gen_build_index.py --check`.
  - AC21: a no-bash `govkit selfcheck`.
  - AC24, AC32: the evidence-suite arms (its floor was raised to 302).
  - AC38: the `GOV_RUNLOG=0` fixture.
  - The harness-arms count for the new driver block in `unattended.sh`.
- The RED-first observation of all seven `New arm:` lines: `check-memory-hygiene.test.sh` (AC2), `leg_factory.py` (AC5), `ratchet.py` (AC6, AC29), `resolve-python.test.sh` (AC16, AC17, AC25, AC28, AC40), `merge-rows.test.sh` (AC27), `run-gates.evidence.test.sh` (AC24, AC30, AC32) and `unattended.test.sh` (AC16, AC31).

**Bug-class checklist:** `gotchas.py --for-diff HEAD~1..HEAD` selected 99 classes. I acted on these:
- heredoc-escape: the fixture `printf` I fixed.
- an-attested-count: 5 new `ok`/`nope` pairs, matching 297 to 302.
- two-answers-to-one-question: the kit-hold copies in `run-selftests.sh` and `govkit.py` stay, each with its reason written beside it.
- move-inventory-misses-readers-by-path: the AC3 grep is empty.
- subprocess-resolves-a-different-shell: a `bash` head resolves through `scan_bash`.

**Left alone:**
- `help/reference/drive.md` and `help/reference/units.md` show as modified only by line endings and were already like that, so I left them unstaged.
- The brief's trailer `Claude Opus 5` was used as AGENTS.md requires.

No command hit its time bound and nothing was skipped.
