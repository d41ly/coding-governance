**Serves:** journal TOOL-aBatchedArm-5

# Build brief — TOOL-aBatchedArm-5, the evidence-derived pooled hang bound, the parity verdict, and the dark flip

The spec is `memory/builds/aBatchedArm/spec/2026-09-13-spec-TOOL-aBatchedArm-5.md` at rev-6. It
survived four adversarial audit rounds and its loop exited NON-CONVERGENT with disposition FOLD, so
it is not re-reviewed: **build what it says**, and where it names a line number or a text anchor,
that is the edit. Every anchor below was re-read against the tree at `5d582ed8`, whose `tools/` is
byte-identical to the spec's BASE `1c736fd9`.

## THE OWNER RULINGS, which bind this unit before the spec does

- 2026-09-13: build agents run NO self-test on every step — build first, verify once when the
  build is complete.
- 2026-09-14: land as it stands, and **run no gate until every unit of the build is built.**

Together they mean: **this unit runs NO suite and NO gate leg at all.** Not
`run-selftests.test.sh`, not the fixture, not the bar, not `run-unattended-gates.sh` in any mode.
The one verification pass is the BUILD's, after units 1 and 2 are built, and it is
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` plus the landing order in the
spec's S5. What you MAY run, because they execute no suite and cost seconds: `bash -n` over every
`.sh` you touch; `run-selftests.sh --help`, `--list` and `--check` on the real tree (they parse the
declaration and your evidence file, and refuse or print — no row runs); the record gates the
pre-commit hook runs (memory hygiene, manifest ratchet, install-prefix, line length, template size) — those are
hooks, not suites, and they run on `git commit` whether you like it or not.

So every acceptance criterion in §6 is ledgered in the AMENDED form — `- ACn — amended rev-6 —
NOT OBSERVED under the 2026-09-14 ruling; owed at the build's final gate pass by
`<the exact command>`, whose fixture is …` — with the command that WILL observe it written out, so
the final pass is a checklist and not a rediscovery. You write the arms; you do not run them. Write
each arm so that a reader can see its red case from the staged-break string alone, because nobody
observed it RED, and say so in the arm's comment: `# NOT YET OBSERVED RED — owner ruling 2026-09-14;
observed at the build's final gate pass`.

## The one sentence

The runner's `--pooled` mode stops bounding rows at `budget × factor`: it bounds each row at
`max(serial budget, worst calibrated reading) + margin` from a tracked evidence file keyed by (row,
token, node), REFUSES any row with no reading, grades PARITY — (rc, `FAIL` count, executed count)
against the calibrated baseline, with every non-completion outcome counted by name — and a declared
`--pooled --calibrate` mode takes the readings under the serial-sum wall while grading nothing. The
four DoD carriers go DARK (`--serial --pooled after calibration`); the flip itself is the build's
landing step and is NOT in this unit.

## Read these before the first edit, in this order

1. The spec, whole. §2 S1–S5 is the edit list, §4 says why each shape was chosen over the one an
   audit rejected, §6 is what the final pass will observe, §7 names the parity-reached arms.
2. `tools/run-gates/run-selftests.sh`: `:77` (usage — gains `--calibrate`, `--reset <row>`, and
   the parity question), `:116-123` (`--kit`; `--pooled|--sweep` is ONE path, so every sweep arm
   runs your parity render), `:490-495` (the factor header refusal — RETIRED), `:507`, `:533`,
   `:599`, `:633` (every `SWEEP_FACTOR` bound — replaced by the evidence bound and the derived
   wall), `:581-586` and `:798` (`FP_BEFORE`/`FP_AFTER` — your evidence write goes AFTER `:798`),
   `:596` (`SWEEP_CONDITION=` — the token), `:642` (`"$d/out"` — the filed output your trailer and
   `^FAIL` reads come from), `:701-753` (the render loop: `killed=0; walled=""; unrun=""` at `:701`,
   the unresolved row `:707`, the could-not-start row `:723`, the `FAIL` branch `:750-752` you
   turn into parity/MISMATCH keeping the `:752` grep beneath), `:787` (the pool-ran-wider guard —
   KEPT), `:816-829` (the summary lines — keep `NO cost verdict was issued` and the `WITHHELD`
   line; re-word `:829`'s serial re-run pointer to the parity question).
3. `tools/run-gates/run-selftests.test.sh`: `:31` (`SELFTEST_FLOOR=55` — re-derive from your arm
   count minus the one retired), `:36-118` (`build_repo` — add the charter stub with ONE registry
   row for `${USERNAME:-$USER}`, the fixture `ceiling-margin.txt`, the seeded and `git add`ed
   evidence file under BOTH tokens `pooled@2x1` and `pooled@1x2`, and remove the
   `sweep-ceiling-factor` line at `:67`), then every pooled arm: `:252`, `:260`, `:277`, `:279`
   (RETIRE — the factor-absent refusal), `:297`, `:313`, `:318-325` (`4 x 2 = 8s`), `:340`
   (RE-CUT to the parity wording), `:371`, `:428`, `:436`, `:455-457` (UNRUN — seed rows `three`
   and `four`), `:463` (`run wall 140s`), `:465`.
4. `tools/unattended/run-unattended-gates.sh`: `:299-311` (the pooled branch: `st` follows the
   runner's `PIPESTATUS[0]`, which now means parity; the `WITHHELD` parse at `:304` must still
   match), `:26-27`, `:187`, `:233` (the DoD-phrase and carrier lines — `:27` goes dark; `:187`
   and `:26` are re-worded ONLY at the flip, not here; `:233` is byte-unchanged).
5. `tools/run-gates/derive-ceilings.py` `:58-90` (`read_margin`) and `:113-131` (`read_evidence`)
   — the RULE you reuse in bash, not the code; `tools/drift-audit/drift_report.py:1790-1804`
   (`_resolve_node_tag` — the registry-row regex you reuse, reading `$ROOT/AGENTS.md` then
   `$ROOT/CLAUDE.md`).
6. `tools/run-gates/kit.toml:60-78` (the `project-owned` rules — add one for
   `selftest-pooled-evidence.txt`), `tools/run-gates/selftest-budgets.txt:49` (the factor header —
   delete), `.githooks/gate-env.sh:27` and `tools/unattended/kit.toml:125-126` (two of the four
   dark carriers).

## The write set, declared before any edit

`tools/run-gates/run-selftests.sh` · `tools/run-gates/run-selftests.test.sh` ·
`tools/run-gates/selftest-pooled-evidence.txt` (new) · `tools/run-gates/kit.toml` ·
`tools/run-gates/selftest-budgets.txt` · `tools/gate-legs.json` ·
`tools/unattended/run-unattended-gates.sh` · `tools/unattended/kit.toml` · `.githooks/gate-env.sh` ·
`memory/guides/SESSION-KICKOFF.md` (the `last-audit` re-stamp only — `run-selftests.sh` is on its
`watch:` line; NO body edit, it is 10 bytes under its cap) · `memory/builds/aBatchedArm/`
(records). Declare all with `--dispatch` before the first edit. NOT in the set, by the spec's §3:
`AGENTS.md`, `tools/unattended/README.md`, `SESSION-KICKOFF.md:169`, `run-unattended-gates.sh:233`
— the four pointers are byte-unchanged.

## Traps this repo has already recorded, so you do not pay for them again

- **Every `.sh` edit is verified at the BYTE level.** `core.autocrlf=true` here: the working copy
  may be CRLF, committed bytes are LF, `git show rev:path` smudges. Trust `git cat-file -p <oid>`.
  Edit with the Edit tool, never a Python `open()` in text mode. Never pass a backslash escape
  through a bash heredoc.
- **The install-prefix leg is a BAN.** `run-selftests.sh` is pinned at its carried literal count;
  your new evidence file names row NAMES and no path, so it needs no row, and your runner edits must
  add no `tools/...` literal — derive siblings as `$HERE/...` as the file already does. Run
  `bash tools/check-install-prefix.sh` before each commit (seconds, not a suite).
- **The manifest is a ratchet.** Touching `run-selftests.sh` reds check 5 unless `last-audit` is
  re-stamped in the SAME commit at the merge-base sha with a delta line in the commit message;
  unit 3's checkpoint commit `cbf8ebce` shows the shape. Do not edit the manifest body.
- **`kit.toml:125-126` are COMMENT lines** inside the descriptor; the dark spelling goes into the
  comment text. `kit.toml:130`'s `landed dark` comment is re-worded ONLY at the flip — leave it.
- **The `run-selftests self-test` leg is already killed at its 300 s ceiling** (ledger `300.333
  fail`). Keep every new arm's sleep at or under 3 s; do NOT re-declare the ceiling — the spec owes
  that at the final pass from an observed wall, and there is none yet. Add `tools/gate-legs.json`
  to the dispatch anyway, with no edit, so the final pass's edit is inside a declared set.
- **`--only 28` is broken** (`TOOL-aHoistedPass-37`) and is not yours.
- **A predicate written into a spec was run over the tree before it was written** — both S5
  predicates are path-scoped and their yields are enumerated; run them yourself with `git grep -nE`
  under the stated scopes, paste the output in the ledger, and if the yield differs from the
  spec's enumeration STOP and write a rev-7 line before editing.

## What done looks like

- Every S item built; every AC ledgered AMENDED with the command that will observe it at the final
  pass, in `memory/builds/aBatchedArm/build/2026-09-14-build-TOOL-aBatchedArm-5-1-acceptance-ledger.md`,
  shaped like unit 3's ledger beside it (check 23's grammar: `- ACn — amended rev-6 — …`, the
  first line carrying `amended rev-6` and NO backtick).
- `bash -n` clean on both `.sh` files; `run-selftests.sh --check` GREEN on the real tree with the
  evidence file present and the factor header gone; `--list --kit tools/unattended` still names
  the fourteen rows; `--help` names `--calibrate`, `--reset` and the parity question.
- The four DoD carriers read `--serial --pooled after calibration`; the four pointers are
  byte-identical to BASE (`git diff BASE -- <path>` empty for each).
- `bash tools/check-install-prefix.sh`, `bash tools/check-line-length.sh` and the pre-commit hook
  green on each commit.
- Two commits: S1–S4 (the runner, its test, the evidence file, the descriptor rule, the retired
  header) and S5 (the four dark carriers, the kit runner's summary parse, the manifest re-stamp),
  each with the unit id in its subject; the spec's status header CLOSED in the second, with a
  rev-7 §9 line recording that every AC is owed at the final pass under the ruling and anything
  that diverged from rev-6.
- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` run after each commit and acted on.

Do NOT run any suite, fixture, self-test leg, bar, or `run-unattended-gates.sh`. The unit's
observation is the build's final pass and nothing else is owed now.
