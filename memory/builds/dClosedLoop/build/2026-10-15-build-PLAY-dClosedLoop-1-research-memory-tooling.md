# Research: the memory layer, the tooling map

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 26's return, verbatim, except that an id of another build that led a list item carries the word "id" before it, so hygiene check 13 does not read it as defined here. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-7-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`.

---

I didn't change anything in the repository. The only files I wrote are two read-only counting scripts in the session scratchpad.

## 1. Inventory

**How usage was counted.** I counted Bash and PowerShell tool calls whose command runs `bash`, `sh`, `python`, `py` or `node` on a path containing `tools/<name>`. The corpus is `~/.claude/projects/C--projects-coding-governance*/**/*.jsonl` from 2026-08-16 onwards: 3,341 files and 122,470 shell calls. Runs made by hooks or by gate legs never appear in transcripts, so every count is a minimum. "Asks" is the number of live backlog rows whose summary names the tool. Summaries are cut short, so that number is a minimum too.

**Kits**

| Kit | Does | Layer | Files / bytes | Invoked by | Runs | Legs (held) | Asks |
|---|---|---|---|---|---|---|---|
| agent-instructions | one charter file, aliased per harness | Instruction | 4 / 22,110 | leg, charter | 0 | 2 (1) | 0 |
| branch-reconcile | which worktrees, branches and stashes can go | Runtime, expansion | 6 / 142,734 | cleanup Skill, leg | 23 | 2 (1) | 0 |
| codebase-map | dossiers checked against code inventories; reuse lookup | Knowledge | 20 / 554,710 | legs, regen stage 3 | 1,001 (gen_map 492, reuse_lookup 312) | 4 (2) | 6 |
| drift-audit | do the records still match reality | Observability | 8 / 641,444 | Skill, `workflows/drift-audit-*.js`, legs | 434 | 3 (1) | 9 |
| gate-lint | silent-misbehaviour lints for shell and encoding | Flow pack, expansion | 6 / 148,407 | legs | 63 | 6 (1) | 0 |
| govkit | the mechanical deployer | Distribution | 24 / 2,294,717 | deploy-governance Skill, legs | 971 | 6 (1) | 30 |
| hooks | agent-cap, scratch-guard, format-guard | Runtime | 11 / 626,030 | harness hooks: PreToolUse, Stop, SubagentStart (`.claude/settings.json:9,18,95,117`) | 181 | 3 (3) | 6 |
| lexicon | naming checked against a declared vocabulary | Knowledge | 14 / 979,591 | Skill, legs, drift-audit (`drift_report.py:1182-1434`) | 1,277 | 3 (1) | 20 |
| lib | resolvers and render helpers | none | 15 / 118,792 | sourced by kits; charter names resolve-python | 80 | 3 (3) | — |
| memory-recall | FTS5 search over memory | Knowledge | 17 / 533,962 | PostToolUse Read hook (`settings.json:71`), legs | 574 (query 314) | 4 (2) | 7 |
| memory-tree | build folders, index, hygiene, gotchas, backlog | Memory | 33 / 2,645,752 | pre-commit (`.githooks/pre-commit:181`), unattended Skill, legs | 5,309 (gen_build_index 2,340, hygiene 2,024, gotchas 818) | 21 (11) | 12 |
| playbook | renders the charter template | Instruction | 5 / 121,900 | legs | 26 | 2 (1) | 6 |
| process-monitor | supervises agent-launched processes | Runtime | 16 / 222,615 | SessionStart and PostToolUse hooks (`settings.json:60,80`), legs | 12 | 3 (2) | 3 |
| pytest-parallel-guardrails | bounds pytest-xdist runs | Flow pack, expansion | 7 / 32,969 | one held leg | 0 | 1 (1) | 0 |
| roles | role definitions, `handoff.py`, `workflows.toml` | Roles | 31 / 269,172 | build Skill (`.claude/skills/build/SKILL.md:11-12`), legs | 189 | 4 (2) | 0 |
| run-gates | the merge bar | Flow: Test | 29 / 1,685,134 | charter, pre-push, CI | 614 (2,955 commands mention `run-gates.sh`) | 14 (10) | 17 (plus 21 naming the turnstile) |
| runlog | machine-local journal of acts | Observability | 20 / 1,035,471 | written by pre-push, run-gates and unattended; Skill | 132 | 3 (1) | 1 |
| unattended | run driver with 20+ verbs (`unattended.sh:14308-14327`) | Runtime: executor | 50 / 4,554,027 | unattended and build Skills; gate-guard, stop-guard, stall-recorder hooks (`settings.json:27,91,106`); commit-msg (`.githooks/commit-msg:59`) | 3,480 | 5 (0) | 54 |
| workflows | review and unit harnesses | Roles and Runtime | 24 / 1,483,352 | Workflow tool | 149 shell; Workflow calls: tier2-review 92, unattended-unit 90, unattended-build 27, drift-audit 4 | 9 (5) | 6 |

**Top-level checks** (each script with its test; one row per gate)

| Check | Does | Proposed layer | Bytes | Invoked by | Runs (script/test) |
|---|---|---|---|---|---|
| check-wiring | detects and wires installed-but-unwired tools | Distribution | 277,536 + fragment | SessionStart hook (`settings.json:56`); test leg | 94 / 37 |
| check-spec-tokens.py | a spec's tokens resolve against the tree | Flow: Design | 179,084 | leg | 489 / 16 |
| check-install-prefix | no hard-coded kit path | Distribution | 46,634 | 2 legs | 249 / 19 |
| check-playbook-parity | the playbook's claims about this repo | Instruction | 47,018 | 2 legs | 54 / 31 |
| check-dead-paths | no reference to a deleted file | Knowledge | 41,061 | 2 legs | 70 / 4 |
| check-hook-destinations | hook paths resolve to a shipped destination | Distribution | 32,479 | 2 legs | 18 / 9 |
| check-template-size | size ceilings | Instruction | 30,758 | 6 legs, pre-commit:210 | 170 / 45 |
| check-agent-cap-restatement | no fan-out bound restated as a bare number | Instruction | 26,760 | 2 legs | 16 / 0 |
| check-kit-placeholders.py | declared placeholders are substituted | Distribution | 26,358 | 2 legs | 23 / 7 |
| check-kit-versions | kit version markers agree | Distribution | 25,601 (no test) | leg | 181 |
| check-line-length | line-length limits for instruction prose | Instruction | 24,751 | 2 legs | 39 / 0 |
| check-testsuite-counts | every self-test prints an assertion count | Flow: Test | 22,350 | 2 legs | 53 / 0 |
| check-remote-literals | no remote named by literal | Distribution | 20,089 | 2 legs | 31 / 25 |
| check-microformats | grades the charter's micro-format definitions | Instruction | 15,025 | 2 legs | 1 / 0 |
| check-placeholders | playbook version-marker lockstep | Instruction | 10,564 | 2 legs | 21 / 5 |
| push-main.sh | the lander | Flow: Deploy | 67,543 | charter, pre-push, 9 agent files | 149 |
| settings-merge.py | wires a hook into settings.json | Distribution | 66,240 | adopters, leg | 23 |

**Skills**

Counted as banner loads ("Base directory for this skill") from 2026-08-16 onwards. I also counted Skill tool calls and slash commands, which agree.

| Skill | Bytes | Loads | Readers outside memory |
|---|---|---|---|
| session-kickoff | 276,487 (6 files) | 58 | SessionStart hooks (`settings.json:38,47`), pre-commit:191, charter |
| unattended | 10,237 | 37 | `.unattended.conf`, pre-commit, unattended kit |
| build | 5,950 | 2 | roles kit (adopt-roles), check-wiring |
| lexicon | 7,522 | 1 | lexicon kit |
| cleanup | 3,611 | 0 | branch-reconcile kit |
| drift-audit | 6,142 | 0 | drift-audit kit |
| memory-recall | 6,310 | 0 | memory-recall kit |
| runlog | 8,028 | 0 | runlog kit |
| deploy-governance | 11,429 | 0 | none (`git grep` finds only the file itself) |

## 2. Sequence

1. Listed the kits and measured them, then parsed all 140 legs in `tools/gate-legs.json`.
2. Mapped every check to its legs and readers. Read `.claude/settings.json`, `.githooks/*` and `AGENTS.md`.
3. Counted usage in the transcripts with two predicates. The loose one (any mention) is not shown; the exec predicate above is what the table uses.
4. Counted backlog rows, duplicated resolvers, and kit packs against the legs list.
5. Probed the seams for `next` and for packs before ranking any candidate.

## 3. Measurements

- **Bar composition.** Legs per chunk:

  ```
  Counter({('selftests','kit'): 61, ('declarations','repo'): 37, ('product','repo'): 18, ('wiring','repo'): 11, ('selftests','repo'): 6, ('records','repo'): 4, ('e2e','kit'): 2, ('wiring','kit'): 1})
  ```

  All 67 legs in the selftests chunk are held by default (`run-gates.sh:3115-3117`). They run only on the nightly CI schedule (`.github/workflows/remote-ci.yml:33-34,166`).
- **Packs against the legs list.** After normalising `{kit}` to `{prefix}/<home>`:

  ```
  json legs 140 matched 59 json-only 81 pack-only 8
  ```

  There are 67 `[[gate_leg]]` rows across `kit.toml` files. govkit already polices the two spellings (`govkit.py:2757`).
- **Resolver copies.** `git grep -c -E '^\s*resolve_python\s*\(\)\s*\{'` matches in 73 files, although `tools/lib/resolve-python.sh:25` is described as the one resolver.
- **Live backlog.** 521 rows: 218 OPEN, 302 DEFERRED, 1 INPROGRESS.
- **The 30 `tools/check-*` files** total 826,283 bytes. The six waiver and limit files total 23,656 bytes.

## 4. Gaps

- **Record and code disagree.** `.claude/rules/product.md` describes check-template-size and check-wiring as the top-level gates. In fact 15 check scripts run as legs, and check-wiring itself is not a leg: it runs only as a SessionStart hook (`settings.json:56`).
- **pytest-parallel-guardrails isn't dogfooded.** No file outside the kit and its docs mentions xdist, and its only leg is held (`govkit/registry.toml:608`). That contradicts the stated fact that gov dogfoods every kit it ships.
- **Three Skills are used through their scripts only.** The drift-audit, memory-recall and runlog Skills have 0 loads, while their scripts ran 365, 314 and 32 times.
- **Known reds.**
  - `TOOL-aBoundedCeiling-9`: the unattended kit's leg is red on main.
  - id `TOOL-aQuenchedHarness-9`: govkit's selftest has two red arms (cited at `run-selftests.sh:36-37`).
  - `reuse_lookup.py` scored 0 of 24 (handed verdict).
- **Not measured.** Firing counts for hooks and legs, because they leave no transcript trace. Runlog lines would supply them; I did not read them, to keep within scope.

## 5. Candidates

**[overlap] Where tools duplicate one another**

| # | Overlap | Evidence | Resolution |
|---|---|---|---|
| O1 | Legs declared twice: `gate-legs.json` and the `kit.toml` packs | 81 legs exist only in the JSON | run-gates builds its leg list from the packs |
| O2 | Three wiring verdicts: check-wiring, 11 `adopt-*.sh --check` legs, `govkit check` | `check-wiring.sh:17,330` already defers to the govkit receipt | one checker in govkit; check-wiring becomes its SessionStart caller |
| O3 | Hook scripts spread over 5 kits: hooks, unattended (3), process-monitor, memory-recall | `settings.json:9-117` | Runtime's hooks kit owns the hook surface; the others supply hook packs |
| O4 | Version lockstep checked four ways: check-kit-versions, check-placeholders, `govkit epoch`, check-verdict-epoch | legs 20, 21, 107 and 112 | one version check, with the others as its arms |
| O5 | One dangling-path test implemented twice: check-dead-paths over the tracked tree, `signal_dangling_pointers` over node-local memory | `drift_report.py:965-985` | one shared function in lib, two callers |
| O6 | 73 inline copies of `resolve_python` | measurement above | generate the copies from lib at render time |
| O7 | The flow's step order lives in Runtime and Roles: the `next:` ladder at `unattended.sh:5745-5783` and the stage order at `roles/workflows.toml:13-90` | read | the loop kit takes both over |

**Not needed by any layer:** the deploy-governance Skill (no readers, 0 loads, and it duplicates govkit's verbs, `SKILL.md:8-14`), and `reuse_lookup.py` (0 of 24).

**[verdict] Keep, re-engineer or retire**

| Tool | Verdict | Deciding fact | What retiring it would break |
|---|---|---|---|
| playbook, agent-instructions | Re-engineer | the ladder needs tag-sliced views; playbook renders by section today | — |
| roles | Re-engineer | its stage order moves to the loop kit (O7) | — |
| workflows | Keep and grow | the always-spawn harness is mapped here; 209 Workflow calls | — |
| memory-tree | Re-engineer | 21 legs, the busiest kit; backlog and gotchas settle this round | — |
| run-gates | Re-engineer | O1: 81 legs exist only in the JSON | — |
| gate-lint, pytest-parallel-guardrails | Keep as packs; pytest-parallel-guardrails demoted to non-dogfood | 0 runs, no xdist suite | if retired: registry.toml:114, README, WIRE-INTO-PROJECT |
| push-main.sh | Keep | the lander, named by the charter | — |
| session-kickoff | Keep | 58 loads | — |
| unattended | Re-engineer | 4.5 MB holding a flow ladder it should not own; 54 asks | — |
| hooks | Re-engineer | O3 | — |
| process-monitor | Keep | Runtime supervision via hooks | — |
| branch-reconcile and the cleanup Skill | Keep, expansion | still has runs (23) | — |
| codebase-map | Keep the map; retire `reuse_lookup.py` | 0 of 24 | 24 code readers, including `reuse-lookup.agent.md` |
| lexicon, memory-recall | Keep | 1,277 and 574 runs | — |
| runlog | Keep | written by three producers | — |
| drift-audit | Keep; re-engineer O5 | 434 runs | — |
| govkit | Re-engineer | O2 and O4 | — |
| lib | Keep; re-engineer O6 | 73 inline copies | — |
| check-wiring | Fold into govkit | O2 | the SessionStart hook, 50+ readers; the fold keeps a thin hook entry |
| check-placeholders | Fold into one version check | O4 | the govkit entry `check-placeholders.kit.toml` |
| check-agent-cap-restatement | Generalise into a "policy value restated" check | it gates one instance; level 2 makes the class gatable | `agent-cap-restatement-waivers.txt`, parity test |
| check-microformats | Re-engineer onto statement types | 1 run; the six statement types replace micro-formats | `hooks/format-guard.js`, WIRE-INTO-PROJECT |
| check-dead-paths | Keep; share the function (O5) | 70 runs | — |
| check-spec-tokens.py | Keep, as a Flow pack for Design | 489 runs | — |
| Other checks (template-size, line-length, playbook-parity, install-prefix, remote-literals, kit-placeholders, hook-destinations, kit-versions, testsuite-counts) | Keep, regrouped into Instruction and Distribution packs | all live legs | — |
| settings-merge.py | Keep, Distribution | used by 6 adopters | — |
| deploy-governance Skill | Retire | no readers, 0 loads | nothing outside memory |
| drift-audit, memory-recall, runlog Skills | Keep (adopter-facing) | rendered by their own adopters | each `adopt-*.sh --check` leg |
| `hygiene-parity.test.sh` | Keep, by its README | kept for the next rewrite (`memory-tree/README.md:31`) | — |

**Re-engineering order.** For each candidate I wrote the losing test down before running it.

| Candidate | Order | Losing test | Result |
|---|---|---|---|
| C1, Flow first | loop kit takes O7 → run-gates packs (O1) → hooks (O3) → memory-tree → instruction slicing → expansions | Loses if `next` cannot be computed without the unattended run's state | **Survives.** `verb_plan` reads `.memory-tree.conf` (`unattended.sh:4576`) and the README units region (5808), not `.unattended.conf`. The attended build Skill already calls it (`build/SKILL.md:20`). Its rungs are unit-level only (5745-5751), so this is a seam, not the finished kit. |
| C2, verdict first | packs → loop kit → … | Loses if packs already drive the bar, so there is nothing to unblock; or if Flow needs the packs before `next` | **Survives the first test** (81 legs exist only in the JSON). **Loses the second:** the Test step reads the verdict, not the leg list, so packs unblock no core step. |
| C3, instruction first | tag-sliced ladder → loop kit | Loses if the tags it slices by belong to a layer not yet built | **Rejected.** Step tags come from the loop kit by the handed map ("stage tags, checklists, `next`"), so slicing by step cannot come first. |

## 6. Pick

**C1, Flow first.**

1. Build the loop kit by extracting the `next:` ladder out of `unattended.sh:5745-5783` and the stage order out of `roles/workflows.toml`, then add stage tags. The unattended kit then calls the loop kit instead of owning the ladder.
2. Make run-gates build its legs from the `kit.toml` packs. This retires the hand-kept half of `gate-legs.json`.
3. Consolidate hooks into the Runtime hooks kit.
4. Re-engineer memory-tree once this round settles it.
5. Rebuild playbook, agent-instructions and roles as tag-sliced views.
6. Expansions: the govkit folds (O2, O4), the lib factory (O6), and dropping `reuse_lookup.py`.

Retiring the deploy-governance Skill depends on nothing and can land at any point.

The test the C1 build must run: `next` gives the same answer for an attended build and an unattended one on the same build folder, with `.unattended.conf` absent.
