# TOOL-dDeclaredLoop-56 — the round-1 spec audit's 47 minors: owed leg rows, one reader each, honest skew and failure paths, and the citations that drifted

**Status:** CLOSED · rev-7 · 2026-11-16 · node d · Tier-2 · base ed497191 · streams tooling · order 36 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-74 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |
| [2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-561.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-561.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-562.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-56-deviation-562.md) | deviation | — |
| [2026-10-25-build-TOOL-dDeclaredLoop-56-deviation-563.md](../build/2026-10-25-build-TOOL-dDeclaredLoop-56-deviation-563.md) | deviation | — |
| [2026-11-05-build-TOOL-dDeclaredLoop-56-deviation-564.md](../build/2026-11-05-build-TOOL-dDeclaredLoop-56-deviation-564.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-56-1-acceptance-ledger.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-56-1-acceptance-ledger.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-56-1-builder-return.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-56-1-builder-return.md) | journal | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-56-deviation-565.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-56-deviation-565.md) | deviation | — |
| [2026-11-16-build-TOOL-dDeclaredLoop-56-red-fix-54.md](../build/2026-11-16-build-TOOL-dDeclaredLoop-56-red-fix-54.md) | red-fix | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-55 |
| [2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md](../prompts/2026-10-25-prompt-TOOL-dDeclaredLoop-1-dorderedcharter-reground.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-46 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-1-parents-crosscheck.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks.md) | research | TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-1-spec-writer.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-1-spec-writer.md) | journal | — |
| [2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md](../prompts/2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade.md) | research | TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-56-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-56-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-56-2-spec-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-56-2-spec-brief.md) | research | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-56-3-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-56-3-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-56-build-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-56-build-brief.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-56-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-56-reground-brief.md) | research | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit.md`)
exited with every finding confirmed; its highs are units 36 to 55. This unit is the batch BUILD-METHOD M4
makes of the rest, every MEDIUM and every LOW, each by its report id and each its own scope item.

Rev-6 re-grounds the batch on the tree as built through order 33. Most minors were closed by the passes of
the units they named, each re-grounded onto its finding before it built; those leave this unit's scope, each
in §3 with what closed it. The fourteen that the built code leaves open stay here, under their rev-5 labels,
which sibling specs cite.

| Report item | Report ids | Rev-5 scope items | At rev-6 |
|---|---|---|---|
| M1 | 9, 40, 58 | S1, S2, S3 | §3 |
| M2 | 26, 39 | S4, S5 | §3 |
| M3 | 11, 29 | S6, S7 | §3 |
| M4 | 22, 43, 60 | S8, S9, S10 | S8, S9, S10 |
| M5 | 23, 57 | S11, S12 | §3 |
| M6 | 10 | S13 | §3 |
| M7 | 13 | S14 | §3 |
| M8 | 14 | S15 | §3 |
| M9 | 15 | S16 | §3 |
| M10 | 16 | S17 | §3 |
| M11 | 17 | S18 | S18 |
| M12 | 20 | S19 | §3 |
| M13 | 21 | S20 | S20 |
| M14 | 30 | S21 | §3 |
| M15 | 31 | S22 | §3, by §8 F6 |
| M16 | 32 | S23 | §3 |
| M17 | 36 | S24 | S24 |
| M18 | 37 | S25 | §3 |
| M19 | 38 | S26 | S26 |
| M20 | 27 | S27 | §3, by §8 F7 |
| M21 | 28 | S28 | §3 |
| M22 | 33 | S29 | §3, by §8 F8 |
| M23 | 41 | S30 | §3 |
| M24 | 42 | S31 | §3 |
| M25 | 44 | S32 | §3 |
| M26 | 45 | S33 | S33 |
| M27 | 46 | S34 | §3 |
| M28 | 53 | S35 | §3 |
| M29 | 56 | S36 | S36 |
| M30 | 59 | S37 | S37 |
| M31 | 61 | S38 | §3 |
| M32 | 62 | S39 | S39 |
| M33 | 63 | S40 | S40 |
| M34 | 64 | S41 | S41 |
| M35 | 65 | S42 | S42 |
| M36 | 66 | S43 | §3 |
| M37 | 67 | S44 | §3 |
| L1 | 12 | S45 | §3 |
| L2 | 24 | S46 | §3 |
| L3 | 34 | S47 | §3 |

## 2. Scope (IN)

The labels keep their rev-5 numbers, which sibling specs cite; every other rev-5 item is in §3.

- **S8** — id 22. The card's claims reader, `derive_claims_line` in
  `skills/session-kickoff/manifest-check.sh`, runs the driver's `--claims --with-key` and reads a row of six
  TAB fields, as today, or of five, whose key prints `-`. Every driver ignores a second `--claims` argument
  it does not know, so a newer card over an older driver keeps its claims cell and calls once. Observed by
  AC5.
- **S9** — id 43. The two suite arms that assert six fields read `--claims --with-key`: the AC2 row-shape
  arm of `tools/unattended/unattended.test.sh`, which also gains a five-field assertion over plain
  `--claims`, and the DL8 AC8 arm of `skills/session-kickoff/manifest-check.test.sh`. Observed by AC6.
- **S10** — id 60. `print_claims` in `tools/unattended/unattended.sh` prints five fields by default and the
  sixth, the claim's key, only under `--claims --with-key`, the one form that runs `derive_claim_keys`. The
  driver's usage line names the flag, the `--claims` entry of `tools/unattended/VERBS.template.md` and its
  render state it, and `help/loop.md`'s sentence on the sixth field states it, anchoring the usage row
  `verb:unattended.sh:--claims`, whose line in `memory/project/docs-undocumented.txt` goes with the anchor.
  Observed by AC5, AC43.
  **Readers:**
  by name: skills/session-kickoff/manifest-check.sh, the card's claims reader; skills/session-kickoff/manifest-check.test.sh; tools/unattended/unattended.test.sh; help/loop.md; tools/unattended/VERBS.template.md; tools/loop/README.md
  by value: skills/session-kickoff/manifest-check.sh prints the key's eight characters after `k1:`, and reads it from `--with-key` alone once this lands.
- **S18** — id 17. `read_withdrawn_parents` in `tools/loop/loop_parents.py` reads each parent's state
  through `tools/loop/loop_table.py`'s `derive_phase_position`, over the run fact `phase` and, where set,
  `halt-code` and `hold-code`, passing no `extra`. A parent reads withdrawn only where the state is
  `withdrawn`, so an `ABORTED` parent whose halt code is `budget-exhausted` reads `incomplete` and fires no
  route. A phase the map refuses raises ValueError naming the parent and the phase, which `route` prints as
  `loop: unanswered` and exits 2. Observed by AC13.
- **S20** — id 21. `check_terminal_proof` in `tools/lib/guarded_write.py` tests standard error per
  platform: on win32 both `sys.stderr.isatty()` and `GetConsoleMode` over the handle
  `msvcrt.get_osfhandle(sys.stderr.fileno())` gives, called through `ctypes`, so `NUL` reads as no
  terminal; elsewhere `sys.stderr.isatty()` alone. The block `guarded_write_py` is re-copied byte for byte
  into `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`. Observed by AC15.
- **S24** — id 36. The run-gates canary's key-set probe gains the control pair the other admitted keys
  carry, in `tools/run-gates/run-gates.test.sh`: a row carrying `stage` passes, one carrying `stages`
  fails. Observed by AC19.
- **S26** — id 38. `WIRE-INTO-PROJECT.md` gains an anchored `<!-- govkit:entry loop -->` section with a
  body, after the roles section: what the loop kit ships, its adopter's `--check`, and that the roles kit
  requires it. Observed by AC21.
- **S33** — id 45. `tools/roles/adopt-roles.test.sh` gains one arm: a fixture whose copy of the loop kit
  is taken away, where the adopter's `--check` exits non-zero naming `no loop kit places the workflows`.
  Observed by AC28.
- **S36** — id 56. In `tools/loop/position.py`, where the remote ladder `resolve_remote` names no remote,
  or the remote-tracking ref of its default branch does not resolve, the remote reads absent: the answer is
  taken on local witnesses, no unit reads `deployed`, and the interrupt line `interrupt — remote · none`
  prints. An absent remote adds no remote-tip claim and no `read` row, so no
  `interrupt — invalidated · remote tip` line and no `claim — remote tip` line prints (§8 F9). A ladder
  refusal, and a tracking ref whose newest reflog entry is older than the bound, still add today's claim
  and answer `stale-remote`. The plant `stale-remote` is staged anew as a remote whose tracking ref carries an
  aged reflog entry, and the plant `no-remote` joins `PLANTS`. Observed by AC31.
- **S37** — id 59. The plant `factory-restores-create` joins `tools/loop/factories.py`'s `PLANTS`: the
  hook factory, which creates its files, run with its gate red, after which no created file is on disk and
  the scratch reads porcelain clean. Observed by AC32.
- **S39** — id 62. `read_withdrawn_parents` reads a parent's run-state text at the tip of
  `refs/remotes/<remote>/<run-branch>` where that ref holds the file, `<remote>` by the loop kit's inline
  ladder in `tools/loop/claims.py` and `<run-branch>` the fact the tree's own copy carries; else it reads
  the tree's copy, as today. A parent with neither maps to None, and `derive_parent_route` prints
  `parent <p> · not withdrawn (no run record)` before its route line. Observed by AC34.
- **S40** — id 63. The up of `tools/govkit/steps/review_rounds.py` writes `.unattended.conf` alone. Where
  the target's policy file does not set every key the conf value maps to, it prints one
  `policy_edit.py set <key> <value>` line per key for the owner to run, and a `conflict` line per key set to
  another value, writes nothing and exits 1, the conf line kept. Once every mapped key reads its value, or
  the value maps to none, it takes the conf's `REVIEW_ROUNDS` lines out, as today. Observed by AC35.
  **Readers:**
  by name: tools/govkit/selftest.py, the review-rounds step arm; help/upgrade-steps.md; tools/unattended/kit.toml, the step row's comment
  by value: tools/loop/review_bounds.py reads `review.design.rounds`, `review.design.round-count` and `review.max-rounds`, which hold the same values once the owner's write lands.
- **S41** — id 64. `measure_class_occurrences` in `tools/workflows/review_dispose.py` counts a slug once per
  distinct review: a record's review is its file stem less a leading `<date>-review-` and a trailing
  `-round<n>`, a stem of no such shape its own review, and every record of `--record`'s review is skipped.
  Observed by AC36.
- **S42** — id 65. `build_commit` in `tools/unattended/lib-unattended.sh`, where its caller declares no
  `_SUBJ`, fills a map local to the call from one `read_attribution_tokens` run over the walk's own
  revision arguments before the walk, and each commit reads its line there. The per-commit
  `read_attribution_tokens -1` runs only for a commit a caller's declared `_SUBJ` lacks. Observed by AC37.

## 3. Non-goals (OUT)

- Any high: units 36 to 55, one per id.
- The spec lints and checklist entries the report names as left-shifts: each would be a new gate no clause of
  this build names; the classes are recorded at the close.
- Re-reviewing any repaired unit: M4 forbids it.

### The rev-5 items the built code closed

Read on branch `unattended-declared-loop-d56bf0` at `e8018d94f`.

| Item | What closed it at the tip |
|---|---|
| S1, S3 | Every row of `tools/gate-legs.json` carries `stage`, each loop leg `["step.test"]`; `TOOL-dDeclaredLoop-33` rev-6 S10 gives `loop termination` the same. |
| S2 | `tools/loop/stage_coverage.py`, run by the leg `loop stage coverage` on every bar, reds an unclaimed dossier, leg, workflow, role or hook. |
| S4 | Each loop leg carries its `enforces` by its own unit's pass (§8 F5). Two are `[[gate_leg]]` rows of `tools/loop/kit.toml`, `loop definition` and `loop transition tables`; every other is gov's own `[[exempt_leg]]` in `tools/govkit/registry.toml`, each with its reason, so rev-5's "an exempt row never answers" no longer describes the tree. |
| S5 | Each loop leg has its `tools/govkit/subject-pins.tsv` row and its `gate-legs` claim in `memory/map/features/loop.md`, and each held one its `tools/run-gates/selftest-budgets.txt` row. `tools/run-gates/ceiling-evidence.txt` is generated from run records and is never hand-written. |
| S6 | `refusal` is a member of `tools/runlog/model.py#PARK_KINDS` and of `tools/drift-audit/drift_report.py#_RUN_PARK_KINDS`. |
| S7, S21 | `tools/loop/position.py#read_refusals` loads runlog's `read_run_state` through `resolve_kit_dir` and parses no row itself; the engine takes the owed sets from the driver's `--plan` hand-over, its `owed` line, and holds no copy of `PARK_KINDS_OWED` outside its fixture's `FX_OWED`. |
| S11, S12 | `tools/roles/adopt-roles.sh` reads the orders through `tools/roles/roles_lib.py#read_workflow_order`, which finds the loop kit by `resolve_kit_dir` and calls its reader; no awk reads `loop.toml`. |
| S13 | Every reader of a disposition record matches `Item` as an item tag through `tools/loop/adapt.py#read_disposition_release`: the budget's ending, the breakpoints and the flow-change release. No reader matches a run-state `decision` row. |
| S14 | `tools/loop/loop_items.py#derive_new_item_row` refuses a non-role actor lacking `--input`, `--allowance` or `--returns`, and `new` grades the written file with the definition's own checks. |
| S15 | The `[[record-version]]` rows of `tools/loop/loop.toml` pin gov's typed kinds, and `tools/loop/loop_items.py#check_record_versions` grades each gov `returns` naming one; an unversioned reference reads as the pinned version. |
| S16 | `--exhausted` refuses unless the ending line's state reads `spent`. |
| S17 | `tools/loop/kit.toml` declares `requires = ["memory-tree"]`, and `tools/loop/loop_lib.py` imports `resolve_compare_base` from that kit's `coverage_join.py`. |
| S19 | `tools/runlog/model.py#read_git_range` keeps its own one-call format; `TOOL-dDeclaredLoop-23` §8 F8 left runlog off the re-point, so no format arm is owed. |
| S23 | `tools/workflows/review_dispose.py#measure_class_occurrences` reads through `parse_appendix_rows` and prints a refused record as `skipped`. |
| S25 | `tools/unattended/PROTOCOL.template.md` and its render measure 68050 bytes PINNED at the tip, under their row in `tools/template-size-limits.txt`, 68130 PINNED. |
| S28 | `tools/loop/loop_witness.py#run_witness_commands` runs `[bash, "-c", command]` with the inline `resolve_bash` under its `resolve_bash_py` parity row. |
| S30 | `tools/unattended/VERBS.template.md` and its render are byte-identical at the tip. |
| S31 | `memory/project/fork-ceilings.txt` keeps its `unattended-status` row, and its `unattended-plan-handover` row, set by `TOOL-dDeclaredLoop-112`, prices the `--plan` the engine calls for `--status`. |
| S32 | `TOOL-dDeclaredLoop-21` is CLOSED; its criterion is past. |
| S34 | `tools/hooks/scratch-guard.js#checkPolicyFile` finds the policy kit through `resolvePolicyHelper` and answers null with no policy kit beside the hook. |
| S35 | `--round-highs` is optional on every round (`TOOL-dDeclaredLoop-32` §8 F6), an absent one reading 0, so no spelled `--review` is refused. |
| S38 | `loop checklist tags` is gov's own `[[exempt_leg]]`, so no adopter carries the leg that would exit 2. |
| S43 | The trailer fixture in `tools/lib/commit_trailers.py` plants `TOOL-tFix-1` and `TOOL-tFix-2` as literals; no arm reads a historical sha. |
| S44 | `tools/loop/loop_transition.py#write_transition` resets the paths it staged, removes the records it wrote and cuts `RUN.md` back on a refused commit. |
| S45 | `tools/loop/scenario.py#check_default` resolves the bare value to `scenario.<value>`. |
| S46 | No live spec of this build but this one and `TOOL-dDeclaredLoop-67`, which quote it, carries the drifted citation; the CLOSED specs that do are frozen. |
| S47 | `check_owner_disposition` in `tools/unattended/unattended.sh` reads the disposition through `budget.py ending`, the factory's reader, and parses no record. |

### The rev-5 items a fork takes out

- S22, the mandate arm's derived phase: §8 F6 (b). The run-branch admission is the policy kit's
  `check_run_mandate` in `tools/policy/guard.py`, which reads the raw `phase` fact at HEAD. What that read
  does not check: a run whose record reads `LANDING` or a hand-off `HELD` while the driver derives it landed.
- S27, the witness normaliser: §8 F7 (b), handed to `TOOL-dDeclaredLoop-68`.
- S29, the upstream record through the factory: §8 F8 (b). `tools/loop/upstream.py#write_upstream_record`
  writes a `journal` record, created exclusively, which no reader reads.

### What the kept items do not do

- S37 does not install a SIGTERM handler: on win32, where this build runs, a terminate is not catchable,
  and on POSIX the restore runs for every exception, `KeyboardInterrupt` included. A gate already red before
  a factory's write still refuses the instance, its output naming the red.
- S36 does not restate the age source of `stale-remote`: `TOOL-dDeclaredLoop-65` reads it from what a fetch
  and a clone write.
- A held flow change whose row tag is no item tag cannot be released by a disposition record, whose `Item`
  must open `item.`; that is `TOOL-dDeclaredLoop-28`'s field rule, not a minor of this report.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — the roles adopter's loop read and the `loop` registry entry (ids 23, 26, 38, 39, 45, 57)
- **consumes-from** `TOOL-dDeclaredLoop-2` — the terminal proof, the mandate arm and scratch-guard's policy arm (ids 21, 26, 31, 39, 46)
- **consumes-from** `TOOL-dDeclaredLoop-3` — the transition writer's commit step (id 67)
- **consumes-from** `TOOL-dDeclaredLoop-4` — the `stage` claim and `loop stage coverage` (ids 9, 26, 36, 40, 58)
- **consumes-from** `TOOL-dDeclaredLoop-5` — `check_actor_list` and its compare base (id 16)
- **consumes-from** `TOOL-dDeclaredLoop-6` — the factory contract and its two legs (ids 9, 26, 39, 59)
- **consumes-from** `TOOL-dDeclaredLoop-7` — the engine's run-state read, its remote answer and `--status` (ids 26, 30, 39, 41, 42, 56)
- **consumes-from** `TOOL-dDeclaredLoop-8` — the keyed `--claims` rows and the card (ids 22, 26, 39, 41, 43, 60)
- **consumes-from** `TOOL-dDeclaredLoop-11` — `loop_checklist.py check` (id 61)
- **consumes-from** `TOOL-dDeclaredLoop-12` — the seeded item rows (id 14)
- **consumes-from** `TOOL-dDeclaredLoop-14` — the `refusal` park kind and its protocol text (ids 11, 26, 29, 37, 39, 41)
- **consumes-from** `TOOL-dDeclaredLoop-15` — `read_withdrawn_parents` (ids 17, 62)
- **consumes-from** `TOOL-dDeclaredLoop-16` — the disposition record's fields (id 10)
- **consumes-from** `TOOL-dDeclaredLoop-17` — `run_witness_commands` (ids 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-19` — the protocol text and the owner-gate release (ids 10, 37)
- **consumes-from** `TOOL-dDeclaredLoop-20` — the class count (ids 32, 64)
- **consumes-from** `TOOL-dDeclaredLoop-21` — AC5's grep and the review-rounds upgrade step (ids 9, 39, 44, 63)
- **consumes-from** `TOOL-dDeclaredLoop-23` — `read_commits`, `read_attribution_tokens` and the suite arm (ids 20, 65, 66)
- **consumes-from** `TOOL-dDeclaredLoop-24` — the item factory and the record-version grammar (ids 13, 14)
- **consumes-from** `TOOL-dDeclaredLoop-25` — the `loop splice check` leg (ids 9, 26, 39)
- **consumes-from** `TOOL-dDeclaredLoop-26` — the `loop composition fixtures` leg (ids 9, 39)
- **consumes-from** `TOOL-dDeclaredLoop-27` — `flow.scenario-default` and its leg (ids 9, 12, 39)
- **consumes-from** `TOOL-dDeclaredLoop-28` — the disposition match and its leg (ids 9, 10, 39)
- **consumes-from** `TOOL-dDeclaredLoop-29` — `upstream.py join --write` and its leg (ids 9, 33, 39)
- **consumes-from** `TOOL-dDeclaredLoop-30` — `budget_state` and its leg (ids 9, 15, 39)
- **consumes-from** `TOOL-dDeclaredLoop-31` — `--exhausted` and `check_owner_disposition` (ids 10, 15, 34)
- **consumes-from** `TOOL-dDeclaredLoop-32` — the `--round-highs` flag (id 53)
- **consumes-from** `TOOL-dDeclaredLoop-33` — the `loop termination` leg row (ids 26, 39, 58)
- **consumes-from** `TOOL-dDeclaredLoop-42` — the inline `resolve_bash` and the file-backed run (ids 27, 28)
- **consumes-from** `TOOL-dDeclaredLoop-46` — the `stage` key admitted to the canary (id 36)
- **consumes-from** `TOOL-dDeclaredLoop-52` — `derive_phase_position` and the `[[phase]]` rows, through which S18 reads a parent's halt code (id 17)
- **hands-off** `TOOL-dDeclaredLoop-65` — the remote-freshness age source of S36, which that unit reads from what a fetch and a clone write (the round-2 spec audit's id 55)
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 3, 4, 12, 22, 23, 24, 36, 50, 66 and 67, each a scope item of that unit
- **hands-off** `TOOL-dDeclaredLoop-68` — the witness normaliser of rev-5's S27, which that unit builds on the run-gates program directly, with no inline copy here to replace (§8 F7; the round-3 spec audit's id 1)
- **hands-off** `TOOL-dDeclaredLoop-70` — S18's `derive_phase_position` call in `read_withdrawn_parents`, onto which that unit writes `tree=root` when it builds after this one in order 36; S18 passes no `extra` and takes the `extra=()` default the tip already has (§4 Dependency; the round-3 spec audit's id 19; reciprocal to that unit's rev-4 consumes-from edge)

## 4. Design

### Why one unit and not two

The kept items meet in shared files: `tools/unattended/unattended.sh` and `tools/unattended/lib-unattended.sh`
(S10, S42), `tools/loop/loop_parents.py` (S18, S39), `help/loop.md` (S10, S18, S36) and the build's shared
records. BUILD-METHOD M6's clause 1 then fails for a split that keeps each half's items together, so one
unit, sequenced.

### Evidence

Read in an export of branch `unattended-declared-loop-d56bf0` at `e8018d94f`; this worktree is cut from
main at `179486e8f`, which holds no loop kit. Rev-7 re-read the edge with `TOOL-dDeclaredLoop-70`, the
counts and the three gaps the first builder return names at the tip `8b06bb0a4`, where that return found
every other claim below held.

- `tools/unattended/unattended.sh#print_claims` prints six TAB fields on every row, the sixth from
  `derive_claim_keys`, one python spawn per call; the `--claims)` arm of the dispatch passes no argument.
- `skills/session-kickoff/manifest-check.sh#derive_claims_line` places a row only where `NF == 6`, and any
  other non-empty line becomes the skip line `--claims printed a line this card cannot read`.
- Main's driver at `179486e8f` prints five fields, its `--claims)` arm reading no `$2`, and main's card
  places a row only where `NF == 5`: each side of the skew loses the claims cell today.
- `tools/loop/loop_parents.py#read_withdrawn_parents` reads the tree's `RUN.md` and compares
  `phase` with `WITHDRAWN_PHASE`, so every `ABORTED` parent reads withdrawn and no ref is named.
- `tools/lib/guarded_write.py#check_terminal_proof` answers `sys.stderr.isatty()` alone, which is true for
  `NUL` on win32; the block is gated byte-identical by the `guarded_write_py` row of
  `tools/lib/resolve-python.test.sh`. No copy keeps a typed confirmation, so rev-5's EOF clause binds nothing.
- `tools/run-gates/run-gates.test.sh` holds `stage` in both `KNOWN` sets and a control pair for each of
  `reads`, `enforces`, `pass_leg` and `scope_of`, none for `stage`.
- `tools/govkit/check_runbook_parity.py#PROBLEM_PIN` is 17 PINNED, an equality. By that checker's own
  predicate over the export, 18 PINNED registry entries lack an anchored section, `loop` among them, and
  none is exempt; this pass's section brings the count to the pin.
- `tools/roles/adopt-roles.test.sh`'s `build_fixture` copies the loop kit's `loop_lib.py` and `loop.toml`
  beside the roles kit; no arm reaches `roles_lib.py`'s `no loop kit places the workflows` refusal.
- `tools/loop/position.py#read_remote_claim` keys the remote claim over the ladder's tracking ref and its
  newest reflog entry, and `derive_answer` answers `stale-remote` whenever that claim is not `fresh`; the
  plant `stale-remote` stages no remote at all. Where the ladder names no remote, `read_remote_claim` keys
  its claim over `refs/remotes/?@?` with no reflog time, `derive_claim_verdict` in `tools/loop/claims.py`
  reads it `re-derived`, and `derive_interrupts` prints it as `interrupt — invalidated · remote tip
  refs/remotes/?`.
- `tools/loop/adapt.py`'s `mid-step` plant and `tools/loop/composition.py`'s `rename` plant each call
  `position.derive_position` over a scratch with no remote: the first compares `witnesses` and `frontier`,
  the second looks for its `composition@` row in `read`, and neither reads the answer or the claims.
- `tools/lib/guarded_write.py#write_guarded` removes a path that did not exist on any exception; the only
  restore plant, `factory-restores`, runs the policy-key factory, which writes existing files.
- `tools/govkit/steps/review_rounds.py` writes the mapped keys through `conf_to_policy.py`'s
  `render_policy_bytes` over whatever the policy file holds, so an owner's value is overwritten; main at
  `179486e8f` holds no such program, so its `[[upgrade]]` row in `tools/unattended/kit.toml` is unlanded
  and the frozen-row check reads none of its bytes.
- `tools/workflows/review_dispose.py#measure_class_occurrences` counts every record but `--record`, and its
  docstring names "two prior rows from two distinct reviews" among what it does not check;
  `tools/workflows/README.md` says `review_dispose.py classes` counts each slug "against every other
  review record under `--builds`".
- `tools/unattended/lib-unattended.sh#build_commit` falls back to `read_attribution_tokens -1` per commit on
  a cache miss; the driver's DoD read calls it per CLOSED unit with no `_SUBJ` declared.

### The claims flag (S8, S9, S10)

```
unattended.sh --claims               slug  node  status  beat-age-s  verdict            (five fields)
unattended.sh --claims --with-key    slug  node  status  beat-age-s  verdict  key|-     (six fields)
```

The `--claims)` arm reads `${2:-}` and passes it on; any other second argument is ignored, as every
released driver ignores it. The card's awk places `NF == 5 || NF == 6` with a known verdict, printing
` · key -` for five. No refusal is added.

### The parent read (S18, S39)

```
read_withdrawn_parents(build, root) -> {parent slug: run-state text, or None for no run record}
  text  = the file at refs/remotes/<remote>/<run-branch>, else the tree's own copy, else None
  facts = {k: read_run_fact(text, k) for k in ("halt-code", "hold-code") if set}
  withdrawn where derive_phase_position(phase, facts)[0] == "withdrawn"
```

The map keeps only withdrawn parents and parents with no run record. `derive_parent_route` prints one
`parent <p> · not withdrawn (no run record)` line per None, then answers over the rest as today.

### The review-rounds up (S40)

The keys a value maps to are today's: none for an unset value or 1; `review.design.rounds = "fixed-count"`
and `review.design.round-count = N` above 1, and `review.max-rounds = N` above 3. The target's
`.governance/policy.toml` is parsed with `tomllib`; an absent file sets nothing. Each mapped key the file
does not set prints `policy_edit.py set <key> <value>`, and each it sets otherwise prints
`conflict · <key> · policy <value> · conf <value>`. The before-image lists the conf alone. The witness is
unchanged.

### Inventory

| Minted | Kind | Where |
|---|---|---|
| `--with-key` | flag of `--claims` | `tools/unattended/unattended.sh` |
| `no-remote` | plant | `tools/loop/position.py` |
| `incomplete-parent`, `aborted-on-run-branch`, `no-run-record` | plants | `tools/loop/loop_parents.py` |
| `factory-restores-create` | plant | `tools/loop/factories.py` |

No function is minted.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`: its `last-audit` re-stamp, since `manifest-check.sh` is on its `watch:` line
- `tools/loop/loop_parents.py`
- `tools/loop/position.py`
- `tools/loop/factories.py`
- `tools/loop/README.md`
- `tools/lib/guarded_write.py`
- `tools/loop/policy_edit.py`
- `tools/playbook/instructions_edit.py`
- `tools/run-gates/run-gates.test.sh`
- `WIRE-INTO-PROJECT.md`
- `tools/roles/adopt-roles.test.sh`
- `tools/govkit/steps/review_rounds.py`
- `tools/unattended/kit.toml`: the comment above the step's `[[upgrade]]` row, which says the step writes the keys
- `tools/govkit/selftest.py`
- `tools/workflows/review_dispose.py`
- `tools/workflows/README.md`: the `review_dispose.py classes` sentence, which counts "against every other
  review record" and comes to count each slug once per other review, a review a record's file stem less a
  leading `<date>-review-` and a trailing `-round<n>`, `--record`'s own review skipped (S41)
- `tools/workflows/unattended-build.test.sh`
- `tools/run-gates/selftest-budgets.txt`
- `help/loop.md`
- `help/upgrade-steps.md`
- `memory/project/docs-undocumented.txt`

### Alternatives rejected

- **One unit per minor.** M4 forbids it: the batch is the one unit the one-mechanism rule admits.
- **A fallback `--claims` call when the flag is refused.** No driver refuses it, so the branch would never
  run.
- **Keeping rev-5's items the tree closed.** Each would be built twice or observed as written by another pass.

## 5. Production-readiness checklist

- security — S20 closes the win32 terminal-proof gap for `NUL`; S40 keeps the owner's policy file
  owner-written and never overwrites an owner value. §8 F6 leaves the mandate read at HEAD, and §3 states
  what it does not check.
- perf / scale — S42 takes the per-commit interpreter start off the driver's DoD walk; S10 takes the key
  spawn off a plain `--claims`.
- error / empty / loading states — S36 and S39 each turn an absent input into a named reading, never a red and
  never a silent green; S18 refuses an unmapped phase by name.
- observability — `interrupt — remote · none`, `not withdrawn (no run record)` and the step's `conflict`
  lines each name their subject.
- risks — S36 reads a remote whose tracking ref was deleted as absent, so such a node acts on local
  witnesses; S41 reads a review by its file name, so a misnamed round counts as its own review.
- testing — AC5 to AC43 as probes and plants; the arms under §7, observed RED then GREEN at the close.
- migration — S40 changes an unlanded step's up from a write to a proposal; no data migrates.
- user docs — `help/loop.md` (S10, S18, S39, S36), `help/upgrade-steps.md` (S40) and the runbook (S26).

### The sweep

Read at the tip `e8018d94f`, and the rows rev-7 moved at `8b06bb0a4`; counts PINNED there unless named
DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `--claims` prints five fields by default | `derive_claims_line`; the DL8 AC8 arm of `skills/session-kickoff/manifest-check.test.sh`; the AC2 arm of `tools/unattended/unattended.test.sh` | the card asks `--with-key`; both arms ask it too (S9) |
| the same | the nine other `--claims` calls of `tools/unattended/unattended.test.sh`, PINNED at `8b06bb0a4`: seven field reads, AC16's of fields 1, 4 and 5 and the six others' of fields 1, 3 and 5; AC1's `claims: none`; AC3's exit 2 | no read reaches the sixth field, and field positions are unchanged |
| the same | `tools/loop/README.md`'s sentence on the sixth field; `help/loop.md`'s; the VERBS entry and its render | each restated with the flag, the render re-copied byte for byte |
| `--with-key` added to the usage line | `docs` and `help page commands` through `tools/govkit/step_gate.py#VERB_SOURCES` | the anchor `verb:unattended.sh:--claims` lands on `help/loop.md`, its fingerprint from `docs_leg.py --fingerprints`, and its row leaves the shrink-only `memory/project/docs-undocumented.txt` |
| `read_withdrawn_parents` maps a no-record parent to None | `derive_parent_route`, its one caller; `TOOL-dDeclaredLoop-70` S5's planned fixture, which reads a `STAGING` parent | the route skips None; a `STAGING` parent is not withdrawn either way |
| the parent read takes `derive_phase_position` | the four existing plants of `tools/loop/loop_parents.py` | `ABORTED` with no halt code reads `withdrawn` and `BUILDING` reads `building`, by `TOOL-dDeclaredLoop-52`'s rows |
| `PLANTS` of `loop_parents.py` gains three | `loop parent routes` and its budget row, 60 seconds PINNED | each plant is one scratch; the row is re-priced from a timed run where a reading passes it |
| the no-remote reading | the plant `stale-remote`; `plan-line` and `status-line`, whose scratch has a bare remote; `tools/loop/breakpoints.py`'s `driver-plan`, which checks only that a `next:` line prints | `stale-remote` restaged with a remote; the others keep their remote |
| the same | `tools/loop/adapt.py`'s `mid-step` plant and `tools/loop/composition.py`'s `rename` plant, each calling `position.derive_position` over a scratch with no remote | their answers move off `stale-remote` and their claims lose the remote tip, and neither reads either: `mid-step` compares `witnesses` and `frontier`, and `rename` finds its `composition@` row in `read`, which held no remote row before |
| `PLANTS` of `position.py` gains `no-remote` | `loop position fixtures` and its budget row, 411 seconds PINNED | re-priced from a timed run where a reading passes it; `TOOL-dDeclaredLoop-65`'s `offline-stale` plant re-grounds on the restaged `stale-remote` at its own pass |
| `PLANTS` of `factories.py` gains a plant | `loop factories fixtures` and its budget row, 882 seconds PINNED | re-priced from a timed run where a reading passes it |
| `check_terminal_proof` | `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`, their inline copies; the parity row `guarded_write_py` under `python resolver (behaviour + inline parity + idiom ban)` | both copies re-copied byte for byte in the same commit |
| the canary's control pair | `run-gates canary` | one probe pair, as its four siblings |
| the runbook section | `govkit runbook parity` | the count meets `PROBLEM_PIN` |
| the roles adopter arm | `roles adopter self-test` and its suite's assertion floor | the floor rises by the arm's assertions |
| the review-rounds up | `check_review_rounds_step` in `tools/govkit/selftest.py`; `upgrade-walk`; `step-rows-frozen` | the arm's rows for 2 and 5 expect the refusal and then, with the keys set, the line taken out; the walk drives no `REVIEW_ROUNDS` fixture; the row is unlanded on main |
| `render_policy_text` loses this caller | `tools/govkit/steps/fanout_cap.py`, `tools/govkit/steps/conf_to_policy.py` | kept: the landed fan-out step still writes through it |
| the class count's review key | the DL20 AC7 arm of `tools/workflows/unattended-build.test.sh`, its records `r1.md`, `r2.md`, `r3.md`; the `review_dispose.py classes` sentence of `tools/workflows/README.md` | each stem is its own review, so its expectations hold; the sentence is restated with the review key |
| `build_commit`'s token read | `tools/unattended/check-pass-order.sh` and `tools/unattended/check-brief-recorded.sh`, which declare `_SUBJ`; the driver's DoD read; the arms of `tools/unattended/check-unattended.test.sh` and `tools/push-main.test.sh` | a declared cache takes today's path; an undeclared one reads the same tokens once |
| `memory/project/positional-refs.txt` | its 2 rows PINNED at `8b06bb0a4` for this spec, `BUILD-METHOD M4` and `BUILD-METHOD M6`, under `positional (the citation check alone)` | §1 still cites M4 and §4 M6, so no row moves and the pass leaves the file alone |
| sibling specs | `TOOL-dDeclaredLoop-65` (S36's age source), `TOOL-dDeclaredLoop-67` (AC30, AC41, S19, S20 and the items this revision moves to §3), `TOOL-dDeclaredLoop-68` (S27), `TOOL-dDeclaredLoop-70` (S18) | each re-grounds on this revision at its own pass; the labels S18, S20 and S36 keep their meaning |

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'                       # the driver's token, 343
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                          # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git show "$B:tools/govkit/check_runbook_parity.py" | grep '^PROBLEM_PIN'          # 17
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-56.md'   # 2
git grep -n -e '--claims' "$B" -- tools skills help
git grep -n -e 'read_withdrawn_parents' -e 'derive_parent_route' "$B" -- tools help
git grep -n -e 'stale-remote' "$B" -- tools help
git grep -n -e 'build_commit ' "$B" -- tools
git grep -n -e 'check_terminal_proof' "$B" -- tools
git grep -n -e 'REVIEW_ROUNDS' -e 'render_policy_text' "$B" -- tools help
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED, since no function is
  minted (§4 "Inventory"); a builder who mints one runs the lexicon's suggest verb on its name first.
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead, since no
  ceiling or pin is raised.
- The refusal ceilings and families: `tools/memory-tree/check-arms.py#branches` and
  `tools/memory-tree/check-arms.py#scan_refusal_sites` read the edited `*.sh` files, the driver,
  `lib-unattended.sh` and `manifest-check.sh`, and no `fail` call or refusal site is added to any. The
  driver's ceiling is 343 PINNED at the tip `8b06bb0a4`, under `TOOL-dDeclaredLoop-52`'s decision row;
  `tools/unattended/unattended.families.txt` does not move.
- Help anchors: the one flag added, `--with-key`, is anchored by S10; no verb is added.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added; no file of the
  memory-tree engine `check-verdict-epoch.sh` delegates to is edited; the one `[[upgrade]]` program edited is
  unlanded on main; `manifest-check.sh` is watched, so the manifest is re-stamped in the same commit.
- Shipped bytes: `install-prefix (shipped surface)` reads no new kit path literal in any edited file.
- The kits whose shipped bytes move, unattended, session-kickoff, loop, playbook, workflows, govkit and
  run-gates among them, have their versions minted at the lander.

### Dependency

`TOOL-dDeclaredLoop-52` (order 34) and `TOOL-dDeclaredLoop-63` (order 35) are CLOSED, and at the tip
`8b06bb0a4` `tools/loop/loop_table.py#derive_phase_position` reads `(phase, facts, phase_map=None,
extra=())` beside 52's `[[phase]]` rows. S18 passes no `extra` and takes that `()` default, which builds
nothing on another unit. `TOOL-dDeclaredLoop-70` (order 36, DEFERRED, rev-4) builds after this unit: it adds
`tree`, moves the `extra` default, and writes `tree=root` onto S18's call, by the hands-off edge in §3.
`TOOL-dDeclaredLoop-33` (order 34, CLOSED) edits `tools/loop/position.py`, `help/loop.md` and
`tools/run-gates/selftest-budgets.txt` at other sections and rows, and S36 builds over its landed engine. `TOOL-dDeclaredLoop-53` and `TOOL-dDeclaredLoop-64`
edit `help/loop.md` and the verbs carrier at other sections. `TOOL-dDeclaredLoop-54` and
`TOOL-dDeclaredLoop-55` share no file. At order 36, `TOOL-dDeclaredLoop-71` and `TOOL-dDeclaredLoop-72`
share no file with this unit. At order 37, `TOOL-dDeclaredLoop-65` edits `tools/loop/position.py` after
S36 and `TOOL-dDeclaredLoop-68` edits `tools/loop/loop_witness.py`, which this unit leaves alone.
`TOOL-dDeclaredLoop-34` is deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s
numeric direction against ask TOOL-dDeclaredLoop-114; neither shares a file. Every code claim was read in an
export of the branch tip; the reuse probe ran on the worktree at `179486e8f`.

## 6. Acceptance criteria

Each `python <module>.py` command below runs in the loop kit's folder unless it names a path.

- **AC5** — When a probe runs the new card's `derive_claims_line` over a stand-in driver printing one
  five-field row, the cell's row ends ` · key -`; and when main's card at `179486e8f` reads the new driver's
  plain `--claims`, its cell prints the row and no `cannot read` line.
  Red when: a skewed pair replaces the cell with the skip line.
- **AC6** — When `grep -c -- '--claims --with-key'` runs over each of the two suite files S9 names, each
  prints at least 1, and the kickoff suite's DL8 AC8 arm reads a six-field row through it.
  Red when: an arm asserts six fields over plain `--claims`.
- **AC13** — When `python loop_parents.py --fixture --plant incomplete-parent` runs, the parent's
  `phase: ABORTED` with `halt-code: budget-exhausted` answers `route none`.
  Red when: every `ABORTED` parent fires the withdrawal route.
- **AC15** — When a probe prints `check_terminal_proof()` of `tools/lib/guarded_write.py` on win32 with
  standard error sent to a pipe, to `NUL` and to a regular file, each prints `None`.
  Red when: `NUL` passes the terminal test.
- **AC19** — When the canary's key-set probe reads a scratch manifest whose row carries `stages`, it fails,
  and with `stage` it passes.
  Red when: the key set admits a key spelled near `stage`.
- **AC21** — When `grep -c '<!-- govkit:entry loop -->' WIRE-INTO-PROJECT.md` runs, it prints 1, and the
  line after the anchor opens a non-empty section.
  Red when: the `loop` entry stays unanchored, over the parity pin.
- **AC28** — When the roles adopter suite's no-loop arm runs the adopter's `--check` over a fixture without
  the loop kit, it exits non-zero and prints `no loop kit places the workflows`.
  Red when: the absent kit reads as an empty workflow table.
- **AC31** — When `python position.py --fixture --plant no-remote` runs, the answer is `act`, the line
  `interrupt — remote · none` prints, and no line names `remote tip`; `--plant stale-remote`, a remote
  whose tracking ref's newest reflog entry predates the bound, answers `stale-remote`.
  Red when: a scratch with no remote answers `stale-remote`.
- **AC32** — When `python factories.py --fixture --plant factory-restores-create` runs, the hook factory's
  gate is red, it exits 1, and none of the files it created is on disk.
  Red when: a created file survives a red gate.
- **AC34** — When `python loop_parents.py --fixture --plant aborted-on-run-branch` runs, the parent whose
  tree copy reads `BUILDING` and whose run branch's tracking tip reads `ABORTED` answers a route naming
  `parent tParent`; `--plant no-run-record` prints `parent tParent · not withdrawn (no run record)` and
  `route none`.
  Red when: the parent's phase is read from the child's tree alone.
- **AC35** — When `python tools/govkit/steps/review_rounds.py up <target>` runs over a scratch target whose
  conf sets `REVIEW_ROUNDS="2"`, it exits 1 printing a line opening `policy_edit.py set review.design.rounds`, and the
  tree's bytes are unchanged; with `review.design.rounds = "one"` set it prints a `conflict` line; with the
  two mapped keys set it exits 0 and the conf line is gone.
  Red when: the up writes the policy file, or overwrites an owner's value.
- **AC36** — When `review_dispose.py classes` counts over two rounds of one review, each disposing
  `class:stale-pin`, with the second as `--record`, no gate is earned.
  Red when: a review's own earlier round counts as a prior occurrence.
- **AC37** — When a probe wraps `read_attribution_tokens` with a call counter and runs `build_commit` with no
  `_SUBJ` over a fixture range of twenty commits naming no unit, the counter reads 1.
  Red when: the fallback starts one interpreter per commit.
- **AC43** — When `grep -c 'usage: verb:unattended.sh:--claims ' help/loop.md` runs it prints 1, and
  `grep -c '^verb:unattended.sh:--claims' memory/project/docs-undocumented.txt` prints 0.
  Red when: the flag ships with no help anchor.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `scratch-guard self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `govkit refusal join` · `govkit acceptance matrix` · `playbook render selftest` · `manifest-check self-test` · `kickoff-manifest ratchet` · `routed-commits selftest` · `pass-order history` · `brief-recorded` · `push-main self-test` · `loop parent routes` · `loop position fixtures` · `loop factories fixtures` · `roles adopter self-test` · `run-gates canary` · `govkit runbook parity` · `govkit selftest` · `upgrade-walk` · `step-rows-frozen` · `unattended-build self-test` · `workflow script syntax` · `python resolver (behaviour + inline parity + idiom ban)` · `docs` · `help page commands` · `help reference pages` · `every held leg is budgeted, every budget row resolves` · `install-prefix (shipped surface)` · `kit epoch (shipped bytes move, the version moves)` · `harness arms (fail branches armed or pinned)` · `spawn budget (forks per hot entrypoint)` · `codebase-map coverage + freshness` · `positional (the citation check alone)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC5 · the five-field stand-in driver, staged against the tip's card awk, which places `NF == 6` alone · the suite's assertion floor raised by the arm added
New arm: tools/loop/loop_parents.py · covers AC13 AC34 · the `incomplete-parent`, `aborted-on-run-branch` and `no-run-record` plants, staged against the tip's raw-phase, tree-only read · none
New arm: tools/loop/position.py · covers AC31 · the `no-remote` plant and the restaged `stale-remote`, staged against the tip's single not-fresh rule · none
New arm: tools/loop/factories.py · covers AC32 · the `factory-restores-create` plant, staged by dropping the created-path removal from a scratch copy of the guarded write · none
New arm: tools/run-gates/run-gates.test.sh · covers AC19 · the `stages` control row, staged against a key set that admits any key near `stage` · none
New arm: tools/roles/adopt-roles.test.sh · covers AC28 · the no-loop fixture, staged against a `read_workflow_order` that answers an empty table for an absent kit · the suite's assertion floor raised by the arm added
New arm: tools/govkit/selftest.py · covers AC35 · the review-rounds rows for a proposal, a conflict and keys already set, staged against the tip's up, which writes the policy file · none
New arm: tools/workflows/unattended-build.test.sh · covers AC36 · two rounds of one review, staged against the tip's count over every other record · the suite's FLOOR_ASSERTIONS raised by the arm added

The unattended kit's own self-test suites are waived for this build's landing by the README's build-level
rule; S9's edit to `tools/unattended/unattended.test.sh` keeps that suite truthful, and AC37 is a probe.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a)
  `**Derived:** PLAY-dClosedLoop-2`, as `TOOL-dDeclaredLoop-36` §8 F1 records for every promoted unit; (b) no
  binding line beyond the header's `advances`. (b) leaves the unit with no clause to answer to. First
  resolved 2026-10-24 by rung 3 and re-affirmed at rev-7. widens: none · relaxes: none ·
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F2 — One batch unit or two?** Options: (a) one; (b) two halves by write set. §4 shows the kept items
  meet in shared files, failing M6's clause 1. First resolved 2026-10-24 by rung 3 and re-affirmed at
  rev-7. widens: none · relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (a)
- **F3 — How does `--claims` survive kit skew (S10)?** Options: (a) six fields by default with a tolerant
  card; (b) five by default, six under `--with-key`. (a) still breaks an old card over a new driver, the
  skeptic's reason for judging the finder's fix unsound. The flag serves the clause's keyed claims, the
  surface `PLAY-dClosedLoop-3` grants for this build's clauses. First resolved 2026-10-24 by rung 3 and
  re-affirmed at rev-7. grants: PLAY-dClosedLoop-3 the --claims --with-key flag · widens: none ·
  relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (b)
- **F4 — Where does the review-rounds upgrade write (S40)?** Options: (a) a proposal the owner lands; (b) a
  new admitted shape in the guard. (b) widens the guard's write surface, veto 3, and the skeptic judged it
  unsound. First resolved 2026-10-24 by rung 3 and re-affirmed at rev-7. widens: none · relaxes: none ·
  RESOLVED (agent, 2026-11-16, delegated): (a)
- **F5 — Who writes `enforces` for a leg whose own unit names none?** Options: (a) each such unit's own pass
  writes the key, and S4 only observes; (b) S4 writes the keys at order 36; (c) a pending-list row. The
  owner's own pick, kept under the owner's mark, since an agent mark would sign the owner's decision as the
  agent's. RESOLVED (owner, 2026-11-05): (a)
- **F6 — Does the mandate arm read the driver's derived phase (rev-5 S22)?** The built guard admits a run's
  branch through the policy kit's `check_run_mandate`, which reads the raw `phase` at HEAD by its own
  contract. Options: (a) the loop guard, after that admission, runs the driver's `--status <slug>` and
  refuses a terminal phase on its first line; (b) leave the read where it is and state what it does not
  check; (c) source the driver and call its internal `read_derived_phase`. (a) runs the position engine and
  the driver's `--plan` inside a commit hook; (c) binds the guard to a function no contract declares.
  Recommendation: (b), by rung 3. widens: none · relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (b)
- **F7 — Does S27's inline normaliser land here (rev-5 S27)?** `TOOL-dDeclaredLoop-68`, at order 37,
  replaces it with the run-gates program. Options: (a) build the inline copy and its parity row here, for 68
  to replace one order later; (b) leave the normaliser to 68, which builds it on the run-gates program
  directly. (a) writes code whose only future is deletion. Recommendation: (b), by rung 3. widens: none ·
  relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (b)
- **F8 — Does the upstream join write through the record factory (rev-5 S29)?** Options: (a) register an
  `upstream` typed kind, in `tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS` and the factory's kind table,
  with its grammar section in the hygiene guide and its row in the typed-kinds plant, and write through
  `write_record`; (b) keep the module's `journal` record, created exclusively, which no reader reads. (a)
  moves the memory-tree kit's vocabulary, its guide and its verdict epoch for a record nothing reads.
  Recommendation: (b), by rung 3. widens: none · relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (b)
- **F9 — What does an absent remote do with the remote-tip claim (S36)?** At the tip `8b06bb0a4`,
  `read_remote_claim` keys a claim over `refs/remotes/?@?` with no reflog time, which reads `re-derived`
  and prints `interrupt — invalidated · remote tip refs/remotes/?`. Options: (a) an absent remote adds no
  remote-tip claim, and `interrupt — remote · none` alone names the absence; (b) the claim stays and prints
  its `claim —` line, and `derive_interrupts` skips it where the remote reads absent; (c) both interrupts
  print. (c) calls a witness invalidated that was never read, against "the remote reads absent"; (b) keeps
  a claim keyed over no ref, which nothing can re-derive. Recommendation: (a), by rung 3. widens: none ·
  relaxes: none · RESOLVED (agent, 2026-11-16, delegated): (a)

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, the batch of the round-1 spec audit's MEDIUM and LOW findings.
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-65 and TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.
- rev-3 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-68 and TOOL-dDeclaredLoop-70, written by the round-3 spec audit's disposal; nothing else moved.
- rev-4 · 2026-10-25 · §2 S4, S20 · §4 The owed leg rows, Files touched · §6 AC3, AC15 · §8 F5 ·
  re-grounded on dOrderedCharter at `462d20f35` by the cross-check record
  `build/2026-10-25-build-TOOL-dDeclaredLoop-1-dorderedcharter-crosscheck.md`, rows 126 and 127 and
  the `enforces` rows 7, 18, 23, 36 and 47: S4 takes only the `[[gate_leg]]` part from `owed_rows.py`,
  keeps its own `enforces` list with no pending-list fallback and refuses an `[[exempt_leg]]` answer;
  the table gains units 3, 17 and 27; S20 tests stderr, per PLAY-dOrderedCharter-15 F4.
- rev-5 · 2026-11-05 · S4 · §4 owed rows · §8 F5 · owner picked F5 (a), brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-3-owner-forks`; S4 observes only. Brief
  `2026-11-05-prompt-TOOL-dDeclaredLoop-56-owner-forks-cascade`: §4 owed rows states every unit's tag.
- rev-6 · 2026-11-16 · §1 to §10 · S8 to S10, S18, S20, S24, S26, S33, S36, S37, S39 to S42 · AC5, AC6,
  AC13, AC15, AC19, AC21, AC28, AC31, AC32, AC34 to AC37, AC43 · §8 F6 to F8 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `e8018d94f` and on the committed specs of TOOL-dDeclaredLoop-52,
  -63 and -70, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-56-1-spec-writer`: the items the built
  code closed move to §3 with what closed each, their criteria with them; S22, S27 and S29 leave by F6 to F8;
  S10's card needs no fallback call; S18 reads through `derive_phase_position`; S20's EOF clause binds
  nothing; S36 keeps the reflog age built and adds the no-remote reading; S37 is the created-path plant;
  S40 proposes and never overwrites; the runbook pin is 17; line citations made symbol citations; the sweep.
- rev-7 · 2026-11-16 · §2 S36 · §3 Edges · §4 Evidence, Files touched, the sweep, Budgets and records,
  Dependency · §6 AC31 · §8 F1 to F9 · per the return `2026-11-16-build-TOOL-dDeclaredLoop-56-1-builder-return`,
  whose dispatch check 49 refused this unit's edge to TOOL-dDeclaredLoop-70: that edge reads hands-off,
  naming S18's `derive_phase_position` call, reciprocal to 70's rev-4; Dependency reads the tip's `extra=()`
  default; the positional rows are 2, no row moves and the registry leaves Files touched; the suite's other
  `--claims` calls are nine; `tools/workflows/README.md` joins Files touched for S41; S36 adds no remote-tip
  claim for an absent remote, by the new F9; the sweep gains the `mid-step` and `rename` plants; the
  driver's ceiling reads 343; every agent fork ends on its delegated mark, F5 keeping the owner's.

## 10. Reuse audit

The seams are the driver's `print_claims` and the card's `derive_claims_line`, each gaining one branch;
`TOOL-dDeclaredLoop-52`'s `derive_phase_position`, which S18 calls rather than mapping phases again; the
loop kit's inline remote ladder `tools/loop/claims.py#resolve_remote`, which S39 and S36 read; the guarded
write's canonical block and its parity row, which S20 edits once; the canary's control-pair shape, the
factory plant shape and the selftest arm shape, each extended by one row; and `build_commit`'s existing
token reader, called once instead of per commit.

`python tools/codebase-map/reuse_lookup.py "read a parent build's run record at its run branch's remote-tracking tip and map its phase and halt code to a build state"`,
on the worktree at `179486e8f`, ranked generic name-stem neighbours such as `read_text`, `read`, `run_git`
and `phases`; the worktree holds no loop kit, so none is the phase map, which was read on the branch.

Recall terms used: claims with-key skew parent withdrawn halt-code derive_phase_position run-branch terminal proof console no-remote stale-remote review-rounds left-shift attribution tokens
