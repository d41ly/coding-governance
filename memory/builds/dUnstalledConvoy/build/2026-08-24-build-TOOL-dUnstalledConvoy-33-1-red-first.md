# TOOL-dUnstalledConvoy-33 — built, and what each arm was observed against

**Serves:** journal TOOL-dUnstalledConvoy-33

Eight assertions in `tools/unattended/unattended.test.sh`, six of them discriminating.

**They were NOT verified by running that suite.** A standing owner instruction of 2026-08-23 forbids
it, and the verification here is the substitute that instruction itself prescribes: a hermetic probe
built from the suite's own prologue — lines 1 to 381, `HERE=` repointed at the live kit — with only
the arms under test appended. Two probes, because the arms sit in two places in the file. Each runs
in well under a minute against the suite's 20-plus.

The red-first pass restored `unattended.sh` and `lib-unattended.sh` from `HEAD` and re-ran both
probes unchanged. **`git checkout --` did not work for that** — the files were already staged, so it
restored the staged copy and the first RED run silently tested the FIXED code and reported st=0.
`git show HEAD:<path>` is what actually reverted them. That is the
`checkout-restores-the-whole-file` family arriving through the index rather than through the
worktree.

## The arms, and the break each one was observed against

| arm | red-first verdict |
|---|---|
| AC3 no derivable baseline → refuse, with the new message | RED — the old refusal fired instead |
| AC2 a unit already in the baseline roster → still refused | RED — no such message existed |
| AC1 a unit in the region but not the baseline → accepted | RED — refused, as every such row was |
| AC1 the acceptance says the record is LATE | RED |
| AC4 `baseline_units` is defined once, in the shared library | RED — it did not exist |
| AC4 the driver calls it | RED — the driver decided the question its own way |
| AC4 the checker calls it | **passes without the fix** — the checker was not reverted for this run |
| the fixture roster actually grew | a sanity check on the fixture; green either way by design |

## What the wedge actually was

Check 24 asked *was this unit in the roster the run entered its live phase with*. Check 48 asked *is
this unit in the units region*. Both reasonable, and jointly unsatisfiable: the region is RENDERED
from the specs that exist, so the moment a run authors a spec the id is in it and the row is refused
forever — while the checker keeps demanding one.

The driver's own source carried a comment saying it had removed "the wedge shape this build exists to
remove". That was true of the IDEMPOTENT case, where a byte-identical row already exists. The general
case sat one branch below the comment claiming otherwise.

Recorded as a class: `memory/gotchas/two-guards-one-question-two-answers.md`.

## What was found in passing and NOT fixed

The suite's arm-coverage check reports three driver messages with no arm asserting them, all in the
`--record-piece` / `--record-set` bypass-flag family and all predating this unit. Left alone: they
are outside this unit's scope, and confirming a fix would need the suite run the standing instruction
forbids. Opened as a backlog item instead.
