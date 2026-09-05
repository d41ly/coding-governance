**Serves:** journal TOOL-aSurfacedLexicon-2 TOOL-aSurfacedLexicon-3

# Build pass, step 1 — the acceptance ledger for the two order-1 units

Node `a` · 2026-09-05 · build `aSurfacedLexicon` · streams tooling. Both units were built in one pass,
SEQUENCED rather than parallel: their write sets intersect on `tools/lexicon/lexicon.py` and
`tools/lexicon/selftest.py`, which BUILD-METHOD M6 clause 1 forbids dispatching together.

Every OBSERVED line below was re-run by an adversarial verifier that staged the breaks itself rather
than reading the builder's report. Where the verifier and the builder disagreed, the verifier's
reading is the one recorded.

**Evidences:** TOOL-aSurfacedLexicon-2
- AC1 — `python tools/lexicon/lexicon.py --check` — exits 0 printing `P1 verb` and `P2 suffix` and no third predicate row; the `P3 layer` row is gone.
- AC2 — `import map_lib` staged into `tools/lexicon/scaffold_lexicon.py` — RED observed: exit 1, `NOT SELF-CONTAINED` naming the file, the line and the module. Unstaged, exit 0.
- AC3 — `python tools/lexicon/lexicon.py --check` — the population line ships in the required SHAPE, naming imports judged and modules beside the engine. Its values read 43 over 6, not the 44 the criterion names: the sibling unit at this build order removed one import. Rev-5 already scoped both figures as gov-only and non-reproducible by an adopter, which is why the shape and not the number is what the criterion asserts.
- AC4 — `grep -c LAYER .lexicon.conf` — returns 0, and `--measure` emits exactly two pin lines.
- AC5 — `python tools/lexicon/selftest.py` and `python tools/drift-audit/selftest.py` — both exit 0, with the layer fixtures and the layer pin strings removed.
- AC6 — `bash tools/check-dead-paths.sh` on a simulated landing commit — green. The gate derives its needles from `git log --diff-filter=D`, so it cannot see an uncommitted deletion; the verifier cloned the tree, replayed the diff, committed, and ran the real gate.
- AC7 — `bash tools/lexicon/adopt-lexicon.sh --check` — exits 0, `Skill in sync`.
- AC8 — `bash tools/check-template-size.sh` on both carriers — template 49144 to 49022, rendered 64506 to 64384. Both net-negative, both under ceiling.
- AC9 — amended rev-8 — narrowed from the whole bar to the three unguarded legs this commit moves, because the full bar runs once at the push boundary over every unit's cumulative diff and no per-unit pass can observe it. Logged in section 9. All three legs green on this commit.
- AC10 — `--check` and `--measure` with the same break staged — RED observed in both, and the refusal SETS compared equal, which is the asymmetry this unit exists to close.
- AC11 — the walk pointed at an empty directory — RED observed at both the function level and the CLI level: `DEAD PROBE` rather than a reassuring zero.
- AC12 — `grep -nE 'LAYERS|resolve_import|_glob_match|P3' memory/map/features/lexicon.md` — every surviving mention is past tense; the dossier no longer describes a live predicate.
- AC13 — `python tools/codebase-map/test_codebase_map.py` — exits 0 after the generated artifacts were regenerated in this same commit.

**Evidences:** TOOL-aSurfacedLexicon-3
- AC1 — `python tools/lexicon/lexicon.py --check` — the surviving verdict lines are byte-identical in shape and the graded figures moved only by this unit's own deletions. NOT observable as a literal before/after diff: the "before" tree is one where the order-1 sibling landed and this unit did not, and that tree was never built. Recorded as a reconstruction rather than a diff, which is what it is.
- AC2 — `python tools/lexicon/lexicon.py --measure` — exits 0 and every surviving pin is unmoved by this unit. Same reconstruction limit as AC1.
- AC3 — `python tools/lexicon/lexicon.py --brief` and `--probe` — both print the usage block and exit 2, naming neither flag among the modes accepted.
- AC4 — a measure-only refusal staged, then its mirror in the check path — BOTH REDS observed by the verifier, in both directions, which is what makes the differential arm a test rather than an assertion.
- AC5 — `grep -c DEAD_TOKENS tools/codebase-map/selftest.py` — returns 0, and that suite exits 0 with 26 arms executed.
- AC6 — amended rev-7 — the equality against `grep -c "check("` is unsatisfiable by construction: 104 against a printed 131, because the grep counts the definition line and counts a loop-bound call site once. Replaced by a de-collected-arm observation, which is the green-by-absence property it was always for. Logged in section 9.
- AC7 — `bash tools/lexicon/adopt-lexicon.sh --check` and `python tools/check-kit-placeholders.py` — both exit 0.
- AC8 — `git grep -n -- "--brief"` and `--probe` over the kit and the rendered Skill — zero lines each.
- AC8b — `git grep` over the tracked set excluding the kit — 36 lines across 7 files, the exact split the criterion names, all of them the unrelated flag of the same spelling.
- AC9 — `grep -n "tracked_files(\|extract(" tools/lexicon/lexicon.py tools/lexicon/scaffold_lexicon.py` — exactly four call sites survive and they are the four named; five walks became one.
- AC10 — `python tools/codebase-map/test_codebase_map.py` — exits 0 after the regeneration landed in this commit.

## What this pass changed about the specs, and why that is not scope creep

Three criteria were AMENDED rather than satisfied, and each was found unsatisfiable BY BUILDING IT.
That is the case for building against a spec rather than around it: unit 3's AC6 asked for an
equality no tree can produce, unit 2's AC9 asked a single pass to observe a bar that runs once for
the whole build, and both had survived four adversarial audit rounds unnoticed because reading a
criterion is not running it.

Nine line citations into `tools/lexicon/lexicon.py` also went stale in this pass, caught by the
`spec tokens` leg. The file went from 1201 lines to 859, so every spec that cited a line number in it
was pointing at nothing. They are now symbol-anchored. It is the same class as citing a sibling spec
by revision number, which an earlier round closed: a reference into something the build itself
rewrites rots by construction, and the fix is to cite the name rather than the position.
