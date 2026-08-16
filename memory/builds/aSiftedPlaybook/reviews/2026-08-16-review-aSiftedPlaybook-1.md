# Review — aSiftedPlaybook spec set (M4 spec audit)

## Verdict: CLEAN WITH FIXES

**This review is INCOMPLETE and must not be read as a clean adversarial pass.** The workflow
`wf_4ed62ebb-cef` planned four primed lenses, three batched skeptics and one synthesis. **Seven of
its eight agents died on a weekly usage limit.** One lens (underspecification) completed and
returned 18 findings; every skeptic and the synthesis failed, so **not one finding was refuted or
confirmed by the harness**. Per `memory/guides/REVIEW-PROTOCOL.md`, a finding with no verdict is
UNVERIFIED, never refuted.

What follows is therefore: 18 findings from one lens, of which **9 were verified by hand** by the
orchestrator against source and folded, and **9 remain unverified**. The three lenses that never
ran — factual accuracy, decomposition/fork authority, and unstated assumptions/prior art — are
coverage this spec set has NOT received.

## Folded — verified by hand before folding

| # | Sev | Where | Finding | Fold |
|---|---|---|---|---|
| 1 | high | PLAY-2 AC1 | `grep -c` counts LINES; the 17 branch senses sit on 14 lines, so the AC failed a correct build. Measured: `\bmain\b` = 16 lines / 19 occurrences | rev-2: both figures stated, `grep -o … \| wc -l` |
| 2 | high | PLAY-2 AC2 | `\bmain\b` scores **zero** on `domain-rules` — no word boundary before the `m` — so the AC's greedy-substitution guard never watched the filename it claimed to | rev-2: split into two observations |
| 3 | high | PLAY-1 | S8 was in §2 and in nothing else: no Inventory row, no source of truth, no Files-touched entry, no AC. A builder working the ACs ships 7 of 8 fixes and passes | rev-3: row, `:157`, AC1b |
| 4 | high | README | The v2.8 marker bump and v2.7 snapshot belonged to no unit — "the last unit to land" is `TOOL-3`, which touches no playbook file | rev: owner named as the last TEMPLATE-touching unit |
| 5 | high | PLAY-3 AC1 | Quantified over a "declared not-adopter-facing set" existing only as prose inside the spec — unobservable | rev-2: S7 creates `tools/playbook-kit-waivers.txt` |
| 6 | med | TOOL-3 S1 | Match rule unspecified; a substring match certifies `lib` as documented on 7 hits of the `lib` inside "deliberately" — the vacuity class this unit exists to catch | rev-3: anchored path-segment match + an arm |
| 7 | med | TOOL-2 S2 | Never said how the harness learns `MAX_BYTES`; a harness exporting its own value tests the override 5× and never observes the shipped ceiling | rev-2: no-override + read the limit from the OK line |
| 8 | med | six §7 blocks | `drift_report.py` named as a gate without `--check`, so it reports and cannot fail | all six + TOOL-2 AC5 |
| 9 | med | TOOL-1 S5 | Range `:100-107` stops mid-paragraph; `:107-109` is the drift-signal warning that keeps this unit from redding the bar | rev-2: `:100-106`, survival of `:107-109` stated |

Also folded, same pass: TOOL-3 S3 compared an intersection the customize file never states
(compare-against-nothing) → restated structurally, with `PLAY-4` S1 now required to state it by
name; three units contended for `memory/map/features/playbook.md` and only two knew it → TOOL-3
extends and never mints; `PLAY-1` §1 said "six statements" against §2's eight; four Files-touched
tables omitted the `.claude/SESSION-KICKOFF.md` re-stamp their own §7 mandated; `TOOL-1` §10 called
`install-prefix.md` the smallest dossier (76-line `codebase-map.md` is); `PLAY-3` cited
`inventories.json:62` for the `kits` inventory (`:58`; `:62` is the string `"gate-lint"`);
`PLAY-2` said eleven `main`s are the filename (eleven are the word `domain`, ten the filename);
`PLAY-2` AC5 named an instantiation step this repo has no tool to perform.

## What the surviving lens verified and could NOT break

Recorded so a later session knows what was actually examined rather than assumed:
`tools/check-template-size.sh:14` and its rule statements at `:2-5`, `:8`, `:25-26`;
`AGENTS.md:16,97,178`; `README.md:12`; `.claude/SESSION-KICKOFF.md:6,99`; `tools/gate-legs.json:3,17`;
`memory/map/baseline.toml:35`, `inventories.json:46`, `MAP.md:53`; `MAX_LENSES = 5` at
`tools/hooks/agent-cap.js:119` with RULE 2/3/4 at `:90/:346/:549` and the miscount history at `:231`;
`"matcher": "Workflow|Agent"` at `.claude/settings.json:5`; `REVIEW-PROTOCOL.md:12-13,58-60,62-70,145`;
the 19-vs-20 hygiene count and its non-derivability from `check-memory-hygiene.sh` alone.

## Owed — this is not optional coverage

Re-run the three lenses that never executed, against the folded specs, once budget allows:

1. **Factual accuracy** — every remaining line-number and constant citation across the seven specs.
2. **Decomposition and fork authority** — M2 one-mechanism-per-spec (especially `PLAY-1`'s eight
   items), and whether any §8 fork carries a recommendation that forecloses the owner's real choice.
3. **Unstated assumptions and prior art** — attack the premise that raising the ceiling is safe;
   check for contradiction with ratified `memory/DECISIONS.md` rows; confirm the union of the seven
   specs' scope covers all eleven audit defects.

Command: `Workflow({scriptPath: '<session>/workflows/scripts/sifted-playbook-spec-audit-wf_4ed62ebb-cef.js',
resumeFromRunId: 'wf_4ed62ebb-cef'})` — the completed lens replays from cache, so only the failed
agents re-run.

**No spec in this set may go INPROGRESS on the strength of this record.** It is one lens of four
with no skeptic pass, and `BUILD-METHOD.md` M4's "stop once a synthesis pass calls the design clean"
has not been reached — there was no synthesis pass.
