# TOOL-dRedressedBar-10 — the round-1 spec audit's 12 mediums and 11 lows, batched: each criterion observed in a form that can pass and fail, each false sentence corrected, and settings-merge's accepted stop narrowed

**Status:** SPECCED · rev-3 · 2026-10-14 · node d · Tier-2 · base ebce889c · streams tooling · order 6 · ratified 2026-10-14

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-2-revision.md) | research | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-10-3-spec-writer.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-10-3-spec-writer.md) | journal | — |
| [2026-10-14-prompt-TOOL-dRedressedBar-19-2-revision.md](../prompts/2026-10-14-prompt-TOOL-dRedressedBar-19-2-revision.md) | research | TOOL-dRedressedBar-19 |
| [2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md](../reviews/2026-10-14-review-TOOL-dRedressedBar-10-11-spec-audit-round1.md) | spec-audit | TOOL-dRedressedBar-11 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 1 to 9
(`reviews/2026-10-14-review-TOOL-dRedressedBar-spec-audit-round1.md`) exited CONVERGED with 23
confirmed findings: no blocker, no high, 12 mediums and 11 lows. BUILD-METHOD M4 promotes every
one, the minors batched into ONE unit, and this is that unit. The findings land on eight specs, so
it repairs no unit in particular and is ordered after every unit the audit read. It closes, by report
id, with the report item each shares:

| id | grade | item | sits in | what is wrong | closed by |
|---|---|---|---|---|---|
| 1 | MEDIUM | M1 | unit 1 AC1 | `grep -c` counts 5 lines where 14 calls are expected | S1 |
| 2 | MEDIUM | M2 | unit 1 AC4 | the unset's placement is anchored on a comment and cannot fail | S2 |
| 3 | MEDIUM | M3 | unit 1 AC5 | one `FOREIGN_PREFIX_PROBE` line expected where the copied shape has two | S3 |
| 4 | MEDIUM | M4 | unit 8 AC6 | the diff runs from the build base, so siblings' edits red it | S4 |
| 5 | MEDIUM | M5 | unit 8 §6 | says the fork leg reads none of `run-gates.test.sh`; it grades it | S5 |
| 6 | LOW | L1 | unit 3 AC2 | no half reads S2's own fixture edit | S6 |
| 7 | LOW | L2 | unit 9 S5, S6 | claimed observed by criteria that never read the two files | S7 |
| 8 | LOW | L3 | unit 4 §3, Edges, §7 | says `adopt-roles.test.sh` ships from the roles kit | S8 |
| 9 | LOW | L4 | unit 7 §1, §3, §4, AC4 | still names units 1 to 6 after units 8 and 9 were added | S9 |
| 10 | MEDIUM | M6 | unit 3 AC5 | the unscoped-calls guard cannot match a scoped call | S10 |
| 11 | MEDIUM | M1 | unit 1 AC1 | as id 1, re-measured by the grounding lens | S11 |
| 12 | MEDIUM | M5 | unit 8 §6 | as id 5, re-measured by the grounding lens | S12 |
| 13 | LOW | L3 | unit 4 §3, §7 | as id 8, re-measured by the grounding lens | S13 |
| 14 | LOW | L5 | unit 5 §4, unit 6 §4 | cites `adopt-roles.test.sh` by base line numbers units 1 and 4 shift | S14 |
| 15 | MEDIUM | M7 | unit 5 AC1, AC2 | counts fork sites with a re-typed regex, not the leg's classifier | S15 |
| 16 | LOW | L6 | unit 3 §4 | restates unit 9's defect mechanism and contradicts it | S16 |
| 17 | LOW | L7 | unit 2 S4, §7 | the retirement inventory misses `symbols.json` as a reader | S17 |
| 18 | LOW | L3 | unit 4 §3, §7 | as id 8, from the blast-radius lens | S18 |
| 19 | LOW | L4 | unit 7 §1, §3, AC4 | as id 9, from the blast-radius lens | S19 |
| 20 | MEDIUM | M1 | unit 1 AC1 | as id 1, from the failure-envelope lens | S20 |
| 21 | MEDIUM | M2 | unit 1 AC4 | as id 2, from the failure-envelope lens | S21 |
| 22 | MEDIUM | M8 | unit 9 §4, §5 | understates the routes into the false-accept state | S22 |
| 23 | LOW | L4 | unit 7 §1, §3, AC4 | as id 9, from the failure-envelope lens | S23 |

Every sibling unit builds first, as written. This unit then observes, over the tree they leave, the
corrected form of each criterion the audit found could not pass or could not fail. It records each
reading in its own acceptance ledger, corrects the false prose in the sibling specs, and narrows
settings-merge's accepted stop to the two homes a static probe can see.

## 2. Scope (IN)

Item S<n> closes report id n. Items that share a report item share its observation, and each still
names its own id.

- **S1** — id 1, M1. Unit 1's S1 is observed by counting CALLS, not lines. Over the tree unit 1
  leaves, `grep -o` with `wc -l` reads 0 glued calls and 14 spaced ones. Spec 1's revision line
  states that AC1's `grep -c` half reads 5 lines over a correct build and names this unit's AC1 as
  the count. Observed by AC1.
- **S2** — id 2, M2. Unit 1's S4 placement is observed against the first EXECUTED push, found with a
  comment-excluding grep, and the observation is shown to red on a staged misplacement. Spec 1's
  revision line states that AC4's placement half was anchored on the header comment at line 2, and
  that its scratch-clone half drives only the hook, so it reads green at base and is a liveness
  reading of the forcing case. Observed by AC2.
- **S3** — id 3, M3. Unit 1's S5 is observed as the two lines every single-stop sibling carries, the
  attribution comment and the `if` line, with exactly one `FOREIGN_PREFIX_PROBE:-0` line reading
  `fail` and `n`. Spec 1's revision line names this unit's AC3 as the count. Observed by AC3.
- **S4** — id 4, M4. Unit 8's AC6 is observed over its own pass commit, `<p8>~1..<p8>`, never from
  the build base. Spec 8's revision line names this unit's AC4 as that reading. Observed by AC4.
- **S5** — id 5, M5. Spec 8's §6 sentence "the fork leg's argv excludes `*.test.sh`, so it reads none
  of this file" is corrected in place. The leg grades this file for the registry classes through
  `scan_spawn_tree` (`tools/gate-lint/sh_hygiene.py:843-850`), against the six rows at
  `memory/project/spawn-idiom-sites.txt:214-219`. Unit 8's pass is observed to add no counted site.
  Observed by AC5.
- **S6** — id 6, L1. Unit 3's S2 is observed in `tools/govkit/selftest.py` itself: the
  aQuenchedHarness-3 fixture's `kits` line and `--kits` argument carry `kickoff-manifest`, and its
  `[answers]` carry `manifest_path` and `user_skills`. Spec 3's revision line names this unit's AC6.
  Observed by AC6.
- **S7** — id 7, L2. Unit 9's S5 and S6 are observed directly: the `[dRB-9]` block in
  `tools/govkit/selftest.py`, the one `check_outcome_states` definition and its two calls in
  `tools/govkit/matrix.py`, and lexicon's two check labels, byte for byte as at the base. Spec 9's
  revision line names this unit's AC7. Observed by AC7.
- **S8** — id 8, L3. Spec 4 is corrected in place at three addresses: the kit-bump non-goal, its
  hands-off to `TOOL-dRedressedBar-7`, and the §7 epoch sentence. Only `tools/hooks/format-guard.js`
  ships and moves a version, for kit `agent-cap` (engine, `tools/hooks/kit.toml:87-90`).
  `tools/roles/adopt-roles.test.sh` is `project-owned` (`tools/roles/kit.toml:46-48`), outside
  `EPOCH_ROLES` (`tools/govkit/govkit.py:12935`), so it moves no roles version. The hooks kit is
  named by its id, `agent-cap` (`tools/hooks/kit.toml:3`). Observed by AC8.
- **S9** — id 9, L4. Spec 7 is corrected in place: §1's "the bytes units 1 to 6 move" and "the other
  six units", §4 "Why one unit"'s "the other six units", and AC4's "each kit that units 1 to 6
  moved" name every unit ordered before it, 1 to 6, 8 and 9. Its Edges gain
  `consumes-from TOOL-dRedressedBar-8` and `consumes-from TOOL-dRedressedBar-9`, and specs 8 and 9
  each gain the mirroring `hands-off TOOL-dRedressedBar-7`, in the same pass. Observed by AC9.
- **S10** — id 10, M6. Unit 3's S5 non-goal is observed by a grep keyed on the fixture alone, so a
  call scoped with `--kits` still prints, and the observation is shown to red on a staged scope.
  Spec 3's revision line names this unit's AC10. Observed by AC10.
- **S11** — id 11, M1. The grounding lens's re-measure of S1's defect: 13 glued calls and 1 spaced
  call on 5 lines at the base. Closed by S1's count. Observed by AC1.
- **S12** — id 12, M5. The grounding lens's reading of S5's defect, citing the leg argv at
  `tools/gate-legs.json:187-195`. Closed by S5's correction and its no-new-site reading. Observed by
  AC5.
- **S13** — id 13, L3. The grounding lens's reading of S8's defect. Closed by S8's correction.
  Observed by AC8.
- **S14** — id 14, L5, the skeptic's corrected fix. Spec 5 §4 states that units 1 and 4 add lines to
  `tools/roles/adopt-roles.test.sh` before unit 5 starts: unit 1's probe stop after arm 1, and unit
  4's `WORKFLOW_RUNS_DIR` comment and constant in `A9_WRITE`. Every cited site is re-mapped by
  content with `grep -n` at unit start, and no new offset is written. Spec 6 §4 carries the same
  sentence for its cites at `:100-107` and `:63`. Observed by AC11.
- **S15** — id 15, M7. Unit 5's AC1 path-subst and date-fmt half and its AC2 are observed through
  the leg's own classifier, `scan_spawn_file` (`tools/gate-lint/sh_hygiene.py:798-818`), read-only
  and not as the gate. Spec 5's revision line names this unit's AC12 as that count. Observed by AC12.
- **S16** — id 16, L6. Spec 3 §4's paragraph "S5, the exposed defect, fixed by unit 9" drops its
  restated mechanism, including "the two always arrive together there", and points at
  `TOOL-dRedressedBar-9` §4, "The defect, and where it sits", as its one owner. Observed by AC13.
- **S17** — id 17, L7. Spec 2's S4 Readers names `memory/map/generated/symbols.json` by name, which
  `gen_map.py --write` writes (the `[[generated]]` row at `tools/codebase-map/kit.toml:148-156`) and
  unit 7's `regen.py --write` re-derives. Spec 2's §7 names `codebase-map coverage + freshness` as
  reading stale until unit 7. Spec 9 carries the same note for `check_outcome_states`. Observed by
  AC14.
- **S18** — id 18, L3. The blast-radius lens's reading of S8's defect, citing `EPOCH_ROLES`. Closed
  by S8's correction. Observed by AC8.
- **S19** — id 19, L4. The blast-radius lens's reading of S9's defect. Closed by S9's correction.
  Observed by AC9.
- **S20** — id 20, M1. The failure-envelope lens's reading of S1's defect, 4, 5, 2, 2 and 1 calls on
  the five lines. Closed by S1's count. Observed by AC1.
- **S21** — id 21, M2. The failure-envelope lens's reading of S2's defect. Closed by S2's anchor.
  Observed by AC2.
- **S22** — id 22, M8, as §8 F1 recommends. Spec 9's §4 "What it does not check" and §5 security
  are corrected to name every route into the false-accept state: `apply --kits settings-merge` over a
  target already holding agent-cap, an `update` that gains settings-merge where agent-cap is already
  claimed, and agent-cap at a home the receipt records. The code-2 block in
  `tools/govkit/entries/settings-merge.kit.toml` takes a second `must_not_exist` term,
  `{prefix}/../hooks/agent-cap.js`, so the stop is refused wherever settings-merge.py's resolver can
  find the hook without the receipt. The receipt-homed residual is stated as open, never as accepted,
  and pointed at `TOOL-dRedressedBar-11`, whose receipt-reading probe term closes it. settings-merge's
  call to `check_outcome_states` in `tools/govkit/matrix.py` gains one row for the parent home.
  Observed by AC15, AC16, AC17 and AC18.
- **S23** — id 23, L4. The failure-envelope lens's reading of S9's defect, with the skeptic's caveat
  that each new edge's description is verified when written. S9's two edges are written from the
  readings in §4, not copied from the report. Observed by AC9.
- **S24** — The record. Each sibling spec the table names takes ONE rev bump in this pass, whose
  revision line names every report id this unit closes in it. Every reading above is written to this
  unit's acceptance ledger,
  `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-10-1-acceptance-ledger.md`,
  carrying `**Serves:** journal TOOL-dRedressedBar-10`. Observed by AC19.

## 3. Non-goals (OUT)

- Rewriting a sibling's criteria. Each sibling is built against its §6 as written. Its revision line
  states which half did not hold and names the criterion here that observes the corrected form.
  Prose that states a false fact is corrected in place, because that is a design claim and not a
  criterion something was built against.
- Re-running a sibling's build or re-observing a criterion the audit did not fault.
- The report's left-shift proposals: the spec-lint checks for `grep -c` against a call count, for a
  base-anchored diff in a parallel unit, for hard-coded unit ranges after an M2 ADD, and for a
  `[[generated]]` output in a Readers list, and the checklist entries. Each is its own mechanism, and
  none is needed to close these 23 findings.
- A receipt-reading probe term in `classify_outcome`, which closes the receipt-homed residual S22
  leaves. It is a new vocabulary in the descriptor contract three verbs read and a separate
  mechanism, so the owner added it as `TOOL-dRedressedBar-11` (§8 F1).
- No edit to `tools/govkit/govkit.py`, `tools/settings-merge.py`, `tools/hooks/kit.toml` or
  `tools/govkit/selftest.py`. No kit version bump: both product files sit under `{prefix}/govkit`,
  which the registry exempts (`tools/govkit/registry.toml:295-297`).
- No new function and no new suite arm beyond the one `check_outcome_states` row.

### Edges

- **consumes-from** `TOOL-dRedressedBar-1` — its built suites, which AC1, AC2 and AC3 read: the
  spaced GH33 calls, the `unset GATE_SELFTESTS` line and the roles probe stop. Its spec takes the one
  revision line S1, S2, S3, S11, S20 and S21 name.
- **consumes-from** `TOOL-dRedressedBar-2` — its rename, which AC14 reads in `symbols.json` after
  unit 7's regen, and its spec's S4 Readers and §7, which S17 corrects.
- **consumes-from** `TOOL-dRedressedBar-3` — its fixture edits in `tools/govkit/selftest.py`, which
  AC6 and AC10 read, and its spec's §4 S5 paragraph, which S16 corrects.
- **consumes-from** `TOOL-dRedressedBar-4` — its spec's kit-bump non-goal, hands-off line and §7
  epoch sentence, which S8, S13 and S18 correct. Its `A9_WRITE` lines are one of the two insertions
  S14 names.
- **consumes-from** `TOOL-dRedressedBar-5` — its conversions, which AC12 classifies, and its spec's
  §4, which S14 corrects.
- **consumes-from** `TOOL-dRedressedBar-6` — its arms in `tools/roles/adopt-roles.test.sh`, a file
  AC12 classifies, and its spec's §4 line cites, which S14 corrects.
- **consumes-from** `TOOL-dRedressedBar-7` — its `regen.py --write`, after which AC14 reads
  `symbols.json`, and its spec's population and Edges, which S9, S19 and S23 correct. Its mint runs
  before this unit, whose two product files are govkit-exempt and owe no bump.
- **consumes-from** `TOOL-dRedressedBar-8` — its pass commit, which AC4 and AC5 read, and its spec's
  §6 sentence and Edges, which S5, S12 and S9 amend.
- **consumes-from** `TOOL-dRedressedBar-9` — its code-2 block, which S22 narrows, its
  `check_outcome_states`, which S22's row joins, and its `[dRB-9]` arm, which AC7 reads. Its spec's
  §4 and §5 are corrected by S22, and its Edges gain S9's hands-off.
- **hands-off** `TOOL-dRedressedBar-11` — the receipt-homed residual S22 leaves open: agent-cap's
  hook at a home only the receipt records, with a `.claude/settings.json` that fails to parse or
  write, still reads as the accepted stop over this unit's two-term block. Unit 11's receipt-reading
  probe term in `classify_outcome` closes it, in the code-2 block this unit narrows.
- **hands-off** `TOOL-dRedressedBar-13` — the units-10-11 spec audit's minors on this spec, report
  ids 1, 2, 3, 4, 5, 8, 9, 12, 14, 15, 16, 18 and 19. Unit 13 observes, over the tree this unit
  leaves, the criterion halves of AC3, AC5, AC8 and AC12 in a form that can fail, and S17's spec-9
  half. It corrects this spec's §1, §3, §4, §5, §7 and §10 in one rev bump. It derives the
  parent-home matrix row's path through `resolve_prefix_token`.

## 4. Design

### Evidence, read at `38384036` on 2026-10-14

Every spec was read at the blob the report pins, and all nine hash to those blobs. The probes
below were re-run on that tree, whose `tools/` equals `ebce889c`'s.

- `grep -c "build_gh33_writer [A-Z]-tB-[0-9]'" tools/workflows/unattended-build.test.sh` prints 5.
  The same pattern through `grep -o … | wc -l` prints 13, and the spaced form prints 1. The calls sit
  on lines 2471, 2483, 2496, 2503 and 2512.
- `grep -n 'git push' .githooks/pre-push.test.sh` prints line 2, a header comment, first.
  `grep -nE '^[^#]*git push'` prints line 135 first, the first push the suite executes.
- `tools/agent-instructions/adopt-agent-instructions.test.sh:18-19` is a `# FOREIGN_PREFIX_PROBE`
  comment and an `if [ "${FOREIGN_PREFIX_PROBE:-0}" = 1 ]` line.
- `scan_spawn_file` over `tools/run-gates/run-gates.test.sh` counts cat-file 25, date-fmt 1,
  path-subst 12, printf-subst 2 and var-pipe 141, equal to the rows at
  `memory/project/spawn-idiom-sites.txt:214-219`. Over the five unit-5 files it counts var-pipe 3, 1,
  12, 0 and 70, path-subst 3, 3, 2, 1 and 6, and date-fmt 0, 0, 1, 0 and 0, in the order
  `adopt-branch-reconcile.sh`, `adopt-roles.sh`, `adopt-roles.test.sh`, `format-guard.test.sh`,
  `unattended-build.test.sh`. Called without its `library` argument, it classifies those classes as
  the leg does; only `pure-fn-subst` reads the library.
- `grep -nE 'run\("update", "--target", str\((up|u4|u9)\)' tools/govkit/selftest.py` prints lines
  3288, 3294, 3299, 3311, 6886, 6900, 7064, 7074 and 7088. Unit 3's AC5 regex does not match
  `run("update", "--target", str(up), "--kits", "check-wiring", "--write")`.
- The aQuenchedHarness-3 fixture opens at `tools/govkit/selftest.py:15273`. Its `kits` line is 15293
  and its `apply` is 15306, and neither names `kickoff-manifest`.
- `tools/roles/kit.toml:47-48` reads `include = ["adopt-roles.test.sh"]` and `role = "project-owned"`.
  `tools/run-gates/kit.toml:40-41` declares `run-gates.test.sh` `project-owned` the same way.
- `memory/map/generated/symbols.json:5420-5423` lists `clean` as a function of
  `tools/unattended/gate-guard.js`, and `check_outcome_probes` of `tools/govkit/matrix.py` is listed
  too, so matrix.py's functions are in the map's population. The `codebase-map coverage + freshness`
  row at `tools/gate-legs.json:814` carries no `guard`. The report cites a `[[regenerate]]` row at
  `tools/codebase-map/kit.toml:151-156`; the row there is `[[generated]]`, at lines 148-156.
- Lexicon's matrix check labels at the base are built at `tools/govkit/matrix.py:232-240` as
  `lexicon exit 1 after a failed first scaffold is REFUSED` and
  `lexicon exit 1 after a declaration removed after one is ACCEPTED`.

### S22 — the false-accept routes, and the narrowing

settings-merge.py finds the hook through `resolve_kit_dir("hooks", "agent-cap.js", <its own dir>)`
(`tools/settings-merge.py:192`). That reads the receipt first, then probes `<here>/hooks`, then
`<here>/../hooks` (`:78-108`). Where nothing is found, the declared-prefix fallback joins
`NO_HOOKS_KIT`, which names a path that exists nowhere (`:197-223`), so the bare run refuses with exit
2 at `:1040-1052`. Where the hook IS found, `run` still returns 2 on a malformed or non-object
`.claude/settings.json` (`_load`, `:491-500`) and on a write `OSError` (`:507-539`).

Unit 9's block refuses exit 2 only where `{prefix}/hooks/agent-cap.js` exists. Three routes reach a
found hook with that path absent, and in each no agent-cap adopter runs to report the failure:

| Route | Why agent-cap's adopter does not run | Cited |
|---|---|---|
| `apply --kits settings-merge` over a target already holding agent-cap | CONFIGURE runs only the selected kits | `tools/govkit/govkit.py:7740-7764` |
| `update` gaining settings-merge where agent-cap is already claimed | the loop runs adopters only for `gained` entries | `tools/govkit/govkit.py:11104-11126` |
| either verb, agent-cap homed elsewhere by `[kit.agent-cap] prefix` or a renamed directory | the receipt row finds it; the probe cannot read the receipt | `tools/govkit/govkit.py:1450-1456`, `tools/settings-merge.py:146-160` |

The narrowing adds the resolver's second static home to the probe:

```toml
probe = { must_exist = "{prefix}/settings-merge.py", must_not_exist = ["{prefix}/hooks/agent-cap.js", "{prefix}/../hooks/agent-cap.js"] }
```

`classify_outcome` already takes a list for either key (`tools/govkit/govkit.py:6313-6324`), and
the matrix's agreement rule reads a list through `derive_probe_paths` (`tools/govkit/matrix.py:199-201`).
No reader of the probe keys exists outside those two. With `prefix` at `tools`, the new term
normalises to `hooks/agent-cap.js` at the target root, inside the target. With `prefix` at `.`, it
resolves outside the target and reads absent there, which leaves the stop exactly as wide as unit 9's.

What still reads as an accepted stop: a hook the receipt alone locates, under either verb, with a
`settings.json` that fails to parse or write. The verb exits 0 and prints `no-agent-cap-to-wire`.
On the `update` route, a fragment the same run wires prints its own
`REFUSED by settings-merge (exit 2)` line first (`run_fragment_merges`,
`tools/govkit/govkit.py:5913-5917`), which names the parse failure without counting a problem.
Spec 9 §4 and §5 state it in those words, as an open false accept and not an accepted one, closed by
`TOOL-dRedressedBar-11`'s receipt-reading probe term (§8 F1).

The matrix row joins settings-merge's call to `check_outcome_states` as a fourth state: settings-merge.py
present, the hook present at the parent home only, rc 2, expected REFUSED. Its path is derived, never
typed: agent-cap's destination from `resolve_entry`, with settings-merge's `{prefix}` replaced by
that prefix's parent.

### The sibling rev bumps

Each of the nine sibling specs already carries, from this spec's writing, a `hands-off` line naming
this unit. The pass adds one rev bump per spec it amends, with the revision line S24 states:

| Spec | Ids | What moves in it |
|---|---|---|
| 1 | 1, 2, 3, 11, 20, 21 | the revision line only |
| 2 | 17 | S4 Readers, §7 |
| 3 | 6, 10, 16 | §4 S5 paragraph |
| 4 | 8, 13, 18 | §3 non-goal, Edges line, §7 sentence |
| 5 | 14, 15 | §4 working-set paragraph |
| 6 | 14 | §4, one sentence |
| 7 | 9, 19, 23 | §1, §4 "Why one unit", AC4 wording, Edges |
| 8 | 4, 5, 12, and S9's mirror | §6 sentence, Edges |
| 9 | 7, 17, 22, and S9's mirror | §4, §5, Edges |

### Files touched (estimate)

- `tools/govkit/entries/settings-merge.kit.toml`
- `tools/govkit/matrix.py`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-1.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-2.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-5.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-6.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-8.md`
- `memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md`
- `memory/builds/dRedressedBar/build/2026-10-14-build-TOOL-dRedressedBar-10-1-acceptance-ledger.md`

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| Fold each fix into its sibling spec now, before the siblings build | M4 forbids folding at a CONVERGED exit (owner, SPEC 2026-10-05) | Refused by the method |
| Rewrite each faulted criterion in place after its unit closes | The sibling's ledger answered the criterion as written; a rewrite leaves the ledger answering text that no longer exists | Rejected; the revision line points here instead |
| Two batch units split by write set | S7, S17 and S22 all write spec 9, so no split leaves two disjoint write sets (M6 clause 1) | Rejected |
| S22 by pricing alone, §8 F1 option (b) | It leaves a false accept a static probe can see, at the resolver's own second home, against the charter's deny-by-default rule | Recommended against in F1 |

## 5. Production-readiness checklist

- security — S22 narrows an accepted stop and widens nothing: one more state is refused, none is
  newly accepted. The receipt-homed residual is stated where unit 9's spec claimed none existed, as
  open and handed off to `TOOL-dRedressedBar-11`.
- perf / scale — N/A — one more `exists` call per settings-merge exit 2, and one matrix row.
- error / empty / loading states — An exit 2 with the hook at either static home now fails the
  verb, so a malformed `settings.json` is reported as a problem instead of an accepted stop.
- observability — Unchanged output shapes. A refused stop prints the existing
  `no declared outcome accepts that` and `adopter exit 2` lines.
- risks — The pass edits nine CLOSED specs. Each edit is one rev bump with a revision line, and no
  criterion text moves, so no ledger is contradicted. A narrowed probe that also matched the
  no-hook state would red unit 9's `[dRB-9]` arm, and AC16's first row refuses that.
- testing — AC1 to AC19 are direct probes, greps and scratch fixtures under `%TEMP%`, each seconds
  long except AC17. The one moved arm is declared in §7.
- migration — N/A — no receipt, conf or deploy field moves.
- user docs — N/A — `help/` holds no govkit page, and no runbook sentence names the accepted stop.

## 6. Acceptance criteria

`<pN>` is the commit of unit N's build pass, as unit N's acceptance ledger names it. Every command
runs from the worktree root.

- **AC1** — When `grep -o "build_gh33_writer [A-Z]-tB-[0-9]'" tools/workflows/unattended-build.test.sh | wc -l`
  runs over the tip, it prints 0, and the same command with a space before the quote prints 14.
  Red when: a call glues its id to its JSON again, and the first count reads above 0.
  figure: 13 and 1 at `ebce889c`, PINNED on 2026-10-14; 14 is their sum.
- **AC2** — When `grep -nE '^[^#]*git push' .githooks/pre-push.test.sh | head -1` and
  `grep -n '^unset GATE_SELFTESTS' .githooks/pre-push.test.sh` run over the tip, the second prints
  exactly one line, and its number is smaller than the first's. In a scratch copy with that line
  moved to the file's end, the same two readings put it after the push.
  Red when: the unset sits below the first executed push, as the staged copy shows.
  figure: the push line is DERIVED at observation; 135 at `ebce889c`.
- **AC3** — When `grep -n 'FOREIGN_PREFIX_PROBE' tools/roles/adopt-roles.test.sh` runs over the tip,
  it prints two lines, both between the `# ---- arm 1` and `# ---- arm 2` headers.
  `grep -n 'FOREIGN_PREFIX_PROBE:-0'` prints one of them, and that line reads `fail` and `n` and no
  `pass`. Red when: the stop is absent, or it reads `pass`, which this suite never sets.
- **AC4** — When `git diff --stat <p8>~1 <p8> -- tools/` runs, it lists one file,
  `tools/run-gates/run-gates.test.sh`. In `git diff <p8>~1 <p8> -- tools/run-gates/`, `MP_BOUND`
  appears only in `run_mp_bar` and on the one `ac14` call, and `FLOOR_ASSERTIONS=401` is unchanged.
  Red when: unit 8's pass moved a second `tools/` file or bounded another call.
- **AC5** — When a python program imports `tools/gate-lint/sh_hygiene.py` and prints, for
  `tools/run-gates/run-gates.test.sh` at `<p8>~1` and at `<p8>` (read with `git show`), the count of
  sites per class from `scan_spawn_file`, the two readings are equal for cat-file, date-fmt,
  path-subst, printf-subst and var-pipe, and each equals its row in
  `memory/project/spawn-idiom-sites.txt`. `grep -n 'reads none of this file'` over spec 8 prints
  nothing, and spec 8's Gates section, cut out with `sed -n '/^## 6. Gates/,/^## 7/p'`, carries
  `scan_spawn_tree` in the corrected sentence. The §3 hands-off line that names it does not count.
  Red when: unit 8's pass added a counted site, or the false sentence stands.
  figure: the rows are DERIVED by reading the registry at observation; 25, 1, 12, 2 and 141 at
  `ebce889c`.
- **AC6** — When the aQuenchedHarness-3 block is cut out with
  `sed -n '/TOOL-aQuenchedHarness-3 — a self-test never reaches/,/aQuenchedHarness-3: the apply itself succeeds/p' tools/govkit/selftest.py`,
  `grep -F 'kickoff-manifest'` over it prints the `kits = [` line and the `"--kits"` line, and
  `grep -F 'manifest_path'` and `grep -F 'user_skills'` each print at least one line.
  Red when: S2 of unit 3 is unbuilt, and every grep prints nothing, as at `ebce889c`.
- **AC7** — When `grep -n '\[dRB-9\]' tools/govkit/selftest.py` runs, its hits form one block after
  the `u2a` re-stamp arms, and that block reads `means` from the settings-merge descriptor.
  `grep -n 'def check_outcome_states' tools/govkit/matrix.py` hits once, and
  `grep -n 'check_outcome_states(' tools/govkit/matrix.py` hits three times. A python program that
  imports `tools/govkit/matrix.py`, replaces its module-level `check` with a recorder, and calls
  `check_outcome_probes` on a scratch directory records exactly two labels opening `lexicon `, equal
  to the two labels §4 pins.
  Red when: unit 9 left either file untouched, or its extraction changed lexicon's labels.
  figure: the two labels are PINNED from `tools/govkit/matrix.py:232-240` at `ebce889c`.
- **AC8** — When `grep -n 'roles kit' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-4.md`
  runs, no line says `adopt-roles.test.sh` ships from it. `grep -n 'project-owned'` over spec 4
  prints the corrected non-goal citing `tools/roles/kit.toml:47-48`, and its hands-off to
  `TOOL-dRedressedBar-7` names the `agent-cap` kit alone.
  Red when: the base sentence `from the roles kit (tools/roles/kit.toml:47)` stands.
- **AC9** — When `grep -nE 'units 1 to 6|six units' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-7.md`
  runs, it prints nothing. Spec 7's Edges hold `consumes-from` lines for `TOOL-dRedressedBar-8` and
  `TOOL-dRedressedBar-9`, citing `tools/run-gates/kit.toml:40-41` and
  `tools/govkit/registry.toml:295-297`. Specs 8 and 9 each hold a line opening
  ``- **hands-off** `TOOL-dRedressedBar-7` ``.
  Red when: a hard-coded range survives, or either edge lacks its other end.
- **AC10** — When `grep -nE 'run\("update", "--target", str\((up|u4|u9)\)' tools/govkit/selftest.py`
  runs over the tip, no printed line carries `--kits`. In a scratch copy with `"--kits", "check-wiring", `
  inserted before `"--write"` in the `str(up)` writing call, the same grep prints that line carrying
  `--kits`, and unit 3's AC5 regex prints nothing for it.
  Red when: a writing call over `up`, `u4` or `u9` is scoped, and the guard prints it.
- **AC11** — When spec 5's Design section is cut out with `sed -n '/^## 4. Design/,/^## 5/p'` and
  searched with `grep -n 'by content'`, it prints the sentence naming unit 1's probe stop and unit
  4's `WORKFLOW_RUNS_DIR` lines as the two insertions. The same cut and grep over spec 6 prints its
  §4 sentence.
  Red when: either spec cites base line numbers with no re-map instruction, as at its pinned blob.
- **AC12** — When a python program imports `tools/gate-lint/sh_hygiene.py` and prints the
  `scan_spawn_file` site counts for the five unit-5 files at the tip, var-pipe, path-subst and
  date-fmt read 0 for `tools/branch-reconcile/adopt-branch-reconcile.sh`, `tools/roles/adopt-roles.sh`,
  `tools/roles/adopt-roles.test.sh` and `tools/hooks/format-guard.test.sh`. For
  `tools/workflows/unattended-build.test.sh`, var-pipe and printf-subst equal that file's rows in
  `memory/project/spawn-idiom-sites.txt`.
  Red when: a converted file still carries a counted site, or the suite lands off its rows.
  figure: the base reading in §4 is PINNED as the red case; the rows are DERIVED at observation.
- **AC13** — When `grep -n 'always arrive together' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-3.md`
  runs, it prints nothing, and `grep -n 'The defect, and where it sits'` over spec 3 prints the
  pointer to unit 9.
  Red when: spec 3 still states its own mechanism for unit 9's defect.
- **AC14** — When spec 2's Scope section is cut out with `sed -n '/^## 2. Scope/,/^## 3/p'` and
  searched with `grep -n 'symbols.json'`, it prints S4's by-name Readers line, and spec 2's §7 leg
  line names `codebase-map coverage + freshness`.
  Over the tip, `grep -n 'renderAskQuote\|check_outcome_states' memory/map/generated/symbols.json`
  prints both names, and no `clean` entry names `tools/unattended/gate-guard.js`.
  Red when: the Readers list omits the map, or the map was not re-derived after unit 7.
- **AC15** — When `grep -n -A5 '^\[\[outcome\]\]' tools/govkit/entries/settings-merge.kit.toml`
  runs, it prints one block whose `must_not_exist` is the two-term list in §4, with `code = 2`,
  `must_exist = "{prefix}/settings-merge.py"`, `means = "no-agent-cap-to-wire"` and `ok = true`.
  Red when: the block keeps unit 9's single term.
- **AC16** — When a python program imports `tools/govkit/govkit.py`, reads the shipped descriptors
  with `read_descriptors`, and prints `outcome_accepted(2, classify_outcome(...), declares_outcome_for(d, 2))`
  for settings-merge over scratch directories, settings-merge.py is present in each. It prints
  ACCEPTED with no hook anywhere, REFUSED with the hook at `{prefix}/hooks/agent-cap.js`, REFUSED
  with the hook at the prefix's parent home only, and ACCEPTED with the hook at a third path only.
  Red when: the parent-home row reads ACCEPTED, as it does over unit 9's block, or the no-hook row
  reads REFUSED and unit 9's stop is lost.
  figure: the fourth row is PINNED as ACCEPTED at this unit's pass. No receipt in the scratch
  directory records the third path, and the receipt-homed route is `TOOL-dRedressedBar-11`'s.
- **AC17** — When a scratch target applies `--kits settings-merge`, then gets `hooks/agent-cap.js`
  at its root and a `.claude/settings.json` holding `{`, a second
  `python tools/govkit/govkit.py apply --target <t> --kits settings-merge` exits 1. Its output
  carries `adopter exit 2` and no `no-agent-cap-to-wire`. The same plant over unit 9's AC2 program
  makes `update --write` exit 1 and leaves `gov_commit` at `24f39915`.
  Red when: either verb exits 0 and prints the stop as accepted, which is what unit 9's block does.
  fixture: fresh `git init` targets under `%TEMP%/<short-name>`, never inside the worktree. The
  red half over unit 9's block is the report's traced reading for id 22 and was not run at spec
  time. The pass observes it first, with unit 9's single-term block staged in the scratch tree. A
  red half that does not exit 0 is returned to the main loop, not counted.
  cost: the update half builds a `stale_target`-shaped program, about a minute.
- **AC18** — When `grep -n 'reachable only by' memory/builds/dRedressedBar/spec/2026-10-14-spec-TOOL-dRedressedBar-9.md`
  runs, it prints nothing. Spec 9's §4 "What it does not check" names the three routes of §4's table,
  and its §5 security line names the receipt-homed residual and `TOOL-dRedressedBar-11`.
  Red when: the envelope still claims one route, or §5 still says the failure is always reported.
- **AC19** — When `git diff <p10>~1 <p10> -- memory/builds/dRedressedBar/spec/` runs at this unit's
  pass commit, each of specs 1 to 9 shows one header rev change and one new revision line, and that
  line names every report id §4's table assigns the spec. The ledger file S24 names exists and
  carries `**Serves:** journal TOOL-dRedressedBar-10`.
  Red when: a spec takes no bump, two bumps, or a revision line missing one of its ids.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene` · `codebase-map coverage + freshness`

New arm: tools/govkit/matrix.py · covers AC16 · stage unit 9's single-term block and the parent-home row of settings-merge's `check_outcome_states` call reads ACCEPTED · none

The main loop runs these once, at the close. `govkit selftest` reads unit 9's `[dRB-9]` arm and the
three arms unit 3 leaves unscoped over the narrowed block; their fixtures hold no hook at either
home, so they stay green. `memory hygiene` grades the nine rev bumps and their revision lines.

## 8. Open questions

- **F1 — How does S22 close id 22: narrow the accepted stop, or only price it?**
  The report offers two fixes after the envelope correction, and both close the finding.
  - (a) Narrow: the second `must_not_exist` term and the matrix row, with the receipt-homed residual
    stated and priced in spec 9. S22, AC15, AC16, AC17 and the §7 arm stand as written.
  - (b) Price only: spec 9's §4 and §5 name the three routes and the residual, and no product file
    moves. S22's descriptor and matrix halves, AC15, AC16, AC17 and the §7 arm drop, and AC18 stands.
  - (c) A receipt-reading probe term in `classify_outcome`, which closes every route. It is a new
    vocabulary in a contract three verbs read, so it is its own mechanism, and a minors batch may not
    hold it (M2, M4). It needs an owner ADD and is an M3 veto 2 turn.
  Recommendation: (a). It refuses a state the resolver reaches with no receipt and no per-kit
  prefix, at no new surface and no version bump. It leaves one follow-up, (c), for the owner to
  schedule.
  RESOLVED (owner, 2026-10-14): (c). This unit keeps S22 as (a) states it: the second
  `must_not_exist` term, the matrix row, AC15, AC16, AC17 and the §7 arm. The receipt-reading probe
  term is not held in this minors batch (M2, M4). The owner added it as `TOOL-dRedressedBar-11`, which
  the §3 Edges hand the receipt-homed residual to.

## 9. Revision log

- rev-1 · 2026-10-14 · initial draft, promoted at the CONVERGED exit of the round-1 spec audit. All
  23 confirmed findings, by report id, batched into this unit by M4, with each claim re-read at
  `38384036`.
- rev-2 · 2026-10-14 · §1 · S22 · §3 · §4 · §5 · AC16 · AC18 · §8 · the owner resolved F1 as (c).
  S22 keeps option (a)'s narrowing, AC15, AC16, AC17 and the §7 arm as written. The receipt-homed
  residual is no longer stated as priced or accepted: S22, the §3 non-goal, §4's residual paragraph,
  §5 security and AC16's figure line point it at `TOOL-dRedressedBar-11`, and AC18 also reads unit
  11's name in spec 9's §5. Edges gain the hands-off to `TOOL-dRedressedBar-11`. §1 says this unit
  follows every unit the audit read, since unit 11 follows it. The header carries `ratified
  2026-10-14`. No product file, criterion command or order moves.
- rev-3 · 2026-10-14 · §3 · Edges gain the hands-off to `TOOL-dRedressedBar-13`, the batch the
  units-10-11 spec audit's minors were promoted into, for report ids 1, 2, 3, 4, 5, 8, 9, 12, 14,
  15, 16, 18 and 19. No scope, design or criterion moves.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "an accepted adopter outcome probe that must not find a
sibling kit's hook at either static home"` ranked `classify_outcome`, `outcome_accepted`,
`declares_outcome_for` and `resolve_kit_dir`. The seam S22 extends is the declared-outcome probe
`classify_outcome` in `tools/govkit/govkit.py`, which already reads a list, and unit 9's
`check_outcome_states` in `tools/govkit/matrix.py`, which takes rows. No code is minted. The other
items extend existing readers: the leg's own classifier `scan_spawn_file` for AC5 and AC12, so no
regex is re-typed, and each sibling's own criteria commands, corrected. The recall probe returned
`TOOL-aEvidencedLens-20`, the precedent minors batch that observed a built unit's criteria and
corrected its prose with one rev bump, and this unit takes its shape. The gotchas checklist for the
two product paths selected `fixture-passes-by-finding-nothing`, which is why AC16's no-hook row and
AC10's staged scope are each shown to move. The report and the code disagree once: the
`codebase-map` row it cites as `[[regenerate]]` is `[[generated]]`.

Recall terms used: `python tools/memory-recall/query.py "how were a spec audit's medium and low
findings batched into one unit that corrects sibling specs after they were built" --terms "spec-audit
minors batch promoted unit corrects sibling spec prose rev bump ledger observed"`
