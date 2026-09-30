# TOOL-dAlignedCarrier-3 — the research and solution-test directives bind every mode

**Status:** SPECCED · rev-1 · 2026-09-30 · node d · Tier-2 · base 87c245b3 · streams tooling · order 1 · closes TOOL-dDerivedDocket-71 · ratified 2026-09-30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-build-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |
| [2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md](../prompts/2026-09-30-prompt-TOOL-dAlignedCarrier-1-spec-brief.md) | journal | TOOL-dAlignedCarrier-1 TOOL-dAlignedCarrier-2 TOOL-dAlignedCarrier-4 TOOL-dAlignedCarrier-5 TOOL-dAlignedCarrier-6 |

<!-- /gen:spec-records -->

## 1. Goal

Two carriers disagree on when a build must research candidates. The driver's directive registry, the
Skill's directive table and protocol §10 scope `researched` and `solution-tested` to prompt runs,
while BUILD-METHOD M5 and M12 key on whether the solution was given, which an ask-driven run's
scaffolded README also leaves open. The owner ruled that both directives bind every mode and that
M12's "solution not given" decides when they apply. This unit makes the registry, the Skill and the
protocol say so, and keeps the scope machinery that the recipe-scoped directives still use.

## 2. Scope (IN)

- **S1** — In `DIRECTIVES_CORE` (`tools/unattended/unattended.sh:816` at BASE) the two entries become
  `researched:M12` and `solution-tested:M12`: the two-field form, which the registry grammar reads as
  scope `all`, as it does for the thirteen other all-scoped entries. The set's size is unchanged, so
  `DIRECTIVES_FLOOR` is untouched. Observed by AC1, AC6.
- **S2** — The Skill template's directive table (`tools/unattended/SKILL.template.md:144-145` at
  BASE) shows `all` in the Scope cell of both rows. The Carrier and From cells are unchanged.
  Observed by AC2, AC3.
- **S3** — The Skill's `**Scope**` paragraph under the table is rewritten so that no sentence scopes
  research or a solution test to `prompt`: it says both bind every mode and that the build method's
  M12 decides when a build owes them, which is when its solution was not given. Its `recipe` sentence
  and its waiver sentence are kept. Observed by AC4.
- **S4** — The Skill's prompt-path paragraph opening "**The research and test obligations bind this
  path and not the slug path**" is rewritten to say they bind this path and every other, both scoped
  `all`, with M12 deciding when. Observed by AC4.
- **S5** — The Skill's playbook-authoring paragraph that says "which this path's two scoped directives
  already bind" is reworded to name the two research directives without calling them scoped.
  Observed by AC4.
- **S6** — The rendered Skill follows in the same pass, by `bash tools/unattended/adopt-unattended.sh`.
  Observed by AC3.
- **S7** — Protocol §10's paragraph opening "**A directive may be SCOPED.**" is rewritten: the scope
  is `all` or an authorization mode, an absent third field is `all`, a mode scope binds only a run
  whose README declared that `authorized-by:` value, and which handle carries which scope is the
  Skill's table. The prompt-only rationale is gone from it. The next paragraph's sentence about a
  waiver of a `prompt`-scoped handle is generalised to a mode-scoped handle on a run of another mode.
  The render follows. The pass adds no bytes to the protocol. Observed by AC5.
- **S8** — `check_waiver_scope` and the kit gate's scope join are NOT edited. Both read the scope
  through the registry's own splitter, so S1 is all they need: a waiver of either handle is accepted
  on a run of any mode, and a waiver of a recipe-scoped handle on another mode is still refused by
  check 45. Observed by AC3, AC6.
- **S9** — The two suite arms that encoded the prompt scope are rewritten, not run. In
  `tools/unattended/unattended.test.sh` the check-45 arm that waives `researched` on the slug fixture
  `tFresh` asserts `preflight OK` and a recorded waiver instead of the refusal, and the comment above
  it names the recipe arm as the check-45 witness. In `tools/unattended/check-unattended.test.sh` the
  scope-disagreement arm mutates the `playbook-followed` row's cell from `recipe` to `all` instead of
  the `researched` row's `prompt`. Observed by AC7.

## 3. Non-goals (OUT)

- BUILD-METHOD M5 and M12. They already key on whether the solution was given, which is the rule the
  owner kept; the build-method file is unit 5's in this build.
- `AUTH_MODES`, `AUTH_SCOPES` and the scope grammar. `prompt` stays a legal scope value; no core entry
  uses it after this unit, and a project declaring one is refused by check 16 as before.
- Protocol §1's "closed set `prompt` / `slug`" for `authorized-by:`, which also omits `recipe`. It is
  a separate stale clause and not this ask's; it is left for a follow-up.
- The two comments in `tools/unattended/check-unattended.sh` that cite `M12:prompt` as the entry that
  once broke the splitter. They record a measurement, and the splitter they explain still serves the
  recipe entries.
- A `memory/DECISIONS.md` row: the owner's ruling row exists and supersedes the older prompt-only one.
- The kit version. The orchestrator moves it once, at VERIFYING.

### Edges

Files shared with a sibling, which are not edges. `tools/unattended/unattended.sh` is also written by
units 1, 4 and 6; this unit touches the `DIRECTIVES_CORE` line only. The Skill template and its render
are also written by unit 6, which owns the "While it runs" bullet and the Close section; this unit
owns the directive table's two rows, the Scope paragraph under it, the prompt-path paragraph and the
playbook-authoring paragraph. The protocol template and its render are also written by unit 2 (§4)
and unit 6 (the §8 table's `SELFTESTS_OWED_PATHS` row); this unit owns §10 and takes none of the
protocol's byte headroom. `tools/unattended/check-unattended.test.sh` is also written by unit 1, which
appends a new arm region; this unit edits the one scope-disagreement arm. `tools/unattended/unattended.test.sh`
is also written by units 4 and 6; this unit edits the check-45 arms and nothing else.

none

## 4. Design

### Evidence

Read at `87c245b3` on 2026-09-30. The registry line carries `researched:M12:prompt
solution-tested:M12:prompt`. `scope_of` returns the third field or `all` when there is none, and
`check_waiver_scope` refuses, as check 45, a handle whose scope is neither `all` nor the run's mode;
it has no other reader. The kit gate builds `corescope` from the same three-field split, defaulting
an absent third field to `all`, and compares it with the Skill table's Scope cells. The only carrier
sentences scoping research to prompt runs are the Skill's lines 149-155, 393-395 and 472 and the
protocol's lines 582-592; a repo grep over `tools/`, `memory/guides/`, `.claude/` and the root docs
finds no other.

The suites encode the old scope twice. `tools/unattended/unattended.test.sh:4388` waives `researched`
on the slug fixture and expects check 45; `tools/unattended/check-unattended.test.sh:2865` stages a
disagreement by editing `| M12 | prompt | D9 |`, which after S2 matches nothing, so the arm's `hit`
would fail on a sed that changed no byte.

### Why the two-field form

The registry grammar says an absent third field is `all`, and every all-scoped entry is written that
way. A `:all` suffix on two entries would make one value spelled two ways inside one constant. Both
readers resolve the two spellings identically, so the choice is spelling, and F2 records it.

### Rollout

The render is `bash tools/unattended/adopt-unattended.sh`, run in the same pass after the template
edit; it re-renders the Skill and re-copies the protocol and the stop contract. `bash tools/unattended/adopt-unattended.sh --check`
is the parity observation.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/SKILL.template.md` ·
`.claude/skills/unattended/SKILL.md` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- Keying the scope on the pinned `asks` fact, so ask-driven runs join prompt runs. The owner chose
  every mode, and that key would also need a scope token the gate's vocabulary does not hold.
- A per-directive refusal when a slug run's specs name no solution. No machine can read "solution not
  given"; M12 states it for the agent, which is where the owner put it.

## 5. Production-readiness checklist

- security — N/A: a directive scope governs which waivers `--preflight` accepts; the change widens
  acceptance of a waiver the owner writes, and no write surface moves.
- perf / scale — N/A.
- error / empty / loading states — a waiver of a recipe-scoped handle on another mode still refuses,
  which AC6's probe and the rewritten suite arm both keep observable.
- observability — N/A: `--preflight` prints the waivers it records, unchanged.
- risks — the kit gate's scope join goes vacuous if the Skill cells drift the same way as the
  registry; AC3 stages a disagreement to show it still fires.
- testing — the probe, the staged break and the greps below; the two suite arms, written and not run.
- migration — none: a run preflighted before the change keeps its recorded waivers, and the gate's
  check 17 reads recorded waivers against the handle set, which is unchanged.
- user docs — the Skill and the protocol are the user docs, and both change here.

## 6. Acceptance criteria

- **AC1** — When `grep -o -E '(researched|solution-tested):M12[^ "]*' tools/unattended/unattended.sh`
  runs after the pass, it prints `researched:M12` and `solution-tested:M12` and nothing carrying a
  third field; at BASE both carry `:prompt`.
  Red when: either entry keeps a scope suffix.
- **AC2** — When `grep -c -E '^ *\| .(researched|solution-tested). .*\| M12 \| all \|' tools/unattended/SKILL.template.md`
  runs, it prints 2, where BASE prints 0, and the same grep over `.claude/skills/unattended/SKILL.md`
  prints 2.
  Red when: either row's Scope cell reads anything but `all`, in the template or the render.
- **AC3** — When the `researched` row's Scope cell in `tools/unattended/SKILL.template.md` is set back
  to `prompt` and staged, `bash tools/unattended/check-unattended.sh` exits 1 with
  `UNATTENDED check 16 FAILED — the directive scopes the registry declares are not the scopes the
  Skill's table shows`. When the file is restored from a byte-identical backup, the same command exits
  0 with no `FAILED` line, and `bash tools/unattended/adopt-unattended.sh --check` exits 0.
  Red when: the join stays silent over the staged disagreement, or the restored tree reds.
  cost: two runs of the kit gate, 593 s each on node d on 2026-09-30 (PINNED).
- **AC4** — When `grep -c -i -E 'scoped .prompt.|not the slug path|two scoped directives' tools/unattended/SKILL.template.md`
  runs, it prints 0, where BASE prints 3; and `grep -c -i 'every mode' tools/unattended/SKILL.template.md`
  prints at least 2, where BASE prints 0, one in the Scope paragraph and one in the prompt-path
  paragraph, each naming M12.
  Red when: a Skill sentence still scopes research or a solution test to prompt runs.
- **AC5** — When `grep -c -E 'research and a solution test are obligations|prompt.-scoped handle' memory/guides/UNATTENDED-PROTOCOL.md`
  runs, it prints 0, where BASE prints 2; `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md`
  exits 0; `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 0; and
  `wc -c < tools/unattended/PROTOCOL.template.md`, read before and after the pass, has not grown.
  Red when: §10 keeps the prompt-only rationale, the render differs, or the pass spends headroom.
- **AC6** — When the three definitions `sed -n -e '/^DIRECTIVES_CORE=/p' -e '/^directives()/p' -e '/^scope_of()/,/^}/p' tools/unattended/unattended.sh`
  prints are written to a scratch file, sourced with `DIRECTIVES_EXTRA` empty, and `scope_of` is
  asked for `researched`, `solution-tested` and `playbook-followed`, it prints `all`, `all` and
  `recipe`.
  Red when: either research handle reads other than `all`, or `playbook-followed` reads `all`, which
  would mean the probe resolves nothing.
- **AC7** — When `grep -c 'M12 | prompt | D9' tools/unattended/check-unattended.test.sh` runs, it
  prints 0, where BASE prints 1; and `grep -n -A3 'tFresh --keepalive-id k1 --waive researched' tools/unattended/unattended.test.sh`
  shows the arm asserting `preflight OK` and a `waiver · item researched` row, with no check 45 text.
  Red when: either suite still stages or expects the prompt scope, which would red it the next time
  the owner runs it.
  permission: running either suite is waived for this landing by the build README's rule; the arms
  are written and their run is not observed here.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: `tools/unattended/unattended.test.sh` · the slug fixture's `--waive researched` now asserts acceptance; check 45 keeps its recipe arm · none
New arm: `tools/unattended/check-unattended.test.sh` · the scope-disagreement arm stages the `playbook-followed` cell · none

## 8. Open questions

- **F1 — Which runs do `researched` and `solution-tested` bind?** The owner ruled on this ask's parked
  decision: every mode, with BUILD-METHOD M12's "solution not given" deciding when they apply, and
  the older prompt-only scope and its rejection of an unconditional scope superseded. RESOLVED (owner,
  2026-09-30): scope `all` for both.
- **F2 — How is scope `all` spelled in the registry?** (a) The two-field entry, which the grammar
  reads as `all`. (b) An explicit `:all` third field. Both resolve identically in `scope_of` and in
  the gate's splitter. (b) would be the only three-field `all` in the constant. Recommendation (a).
  RESOLVED (agent, 2026-09-30, delegated): (a), one spelling for one value, matching the other
  all-scoped entries.

## 9. Revision log

- rev-1 · 2026-09-30 · initial draft, from the ask's accept clause, the owner's ruling and the
  build's spec brief.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a directive's scope decides which authorization modes it
binds"` ranked `derive_scope` in the process-monitor kit, a different concept that shares a word, and
reported `.sh` as an unscanned layer. The seam is the existing scope machinery, reused unchanged:
`scope_of` and `check_waiver_scope` in `tools/unattended/unattended.sh` and the `corescope` split in
`tools/unattended/check-unattended.sh`, which already treat an absent third field as `all`. This unit
edits data and prose and no reader.

Recall terms used: `researched solution-tested directive scope prompt all DIRECTIVES_CORE
check_waiver_scope check 45 M12 TOOL-aPromptedMandate-4`.
