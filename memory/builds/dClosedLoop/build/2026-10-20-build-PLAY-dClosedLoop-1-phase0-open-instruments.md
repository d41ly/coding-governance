**Serves:** research PLAY-dClosedLoop-1

# Instruments: the opening script's acceptance and red tests (Phase 0, P0.5 with P0.6 rules 1 and 2, P0.7, P0.8 row 9)

Dispatch 239's record, as its brief asks (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-brief-open.md`): every
command run for an acceptance check or a red test, in order, with its exit and the line that proves it; then
`--families`, `--driver-builds`, `--carriers` and `--summary` whole; then where the derivation differs from the plan's
probes. `build/` is `memory/builds/dClosedLoop/build/`. `open.py` is `build/2026-10-20-build-PLAY-dClosedLoop-1-open.py`,
at blob `43cdb6d77d9a04edfc242ab5091d9f9715e4eed0` in every run below and in the commit that carries this record.
`packet.py` and `bare-ids.py` are the sibling instruments of those names under `build/`, and `gen_build_index.py` is
`tools/memory-tree/gen_build_index.py`.

**Where the runs happened.** In "the acceptance clone": a `git clone --shared` of the main loop's worktree at
`429ad182d`, with `open.py` added byte for byte as one scratch commit (`f797b6179970`), so its own blob pins in every
packet. The opening was written there only. After acceptance step 9 the clone committed it as scratch commit
`c67e46ce6be7`, the opening commit `--carriers --check` reads, and each red test's plant was restored from that commit
before the next. Every command ran from the clone's root under a bounded timeout. Three probes ran beside the instruments, from
the session's scratch folder and never in the tree: `probe-bare.py` splits the bare-id predicate's output by file and
by whether the opening minted each id; `probe-slots.py` measures each opened README's authored slots in bytes, the
heading's next line to the line before the next heading, against `tools/memory-tree/build-readme-slot-limits.txt`,
and every authored line's width; `probe-carriers-a93.py` runs `open.py`'s carrier derivation at `a93477abc`.

**This record replaces the one committed at `429ad182d`**, whose runs were of blob `61a6fbf9`. The bug-class
checklist over that commit (`gotchas.py --for-diff HEAD~1..HEAD`) selected `two-answers-to-one-question`: P0.8 row
1's id was declared both in `packet.py` (`EXTRA_DECISION`) and in `open.py`. `open.py` now counts every decision and
clean-reading id on from `packet.py`'s one declaration. Every id it derives is unchanged, and every run below was made
again, on the new blob.

**Ids.** Every family id below is one the opening mints (a roster unit, a carry-forward ask, or one of dClosedLoop's
clean-reading asks, `PLAY-dClosedLoop-11` to `-17`) or one of P0.8's rows the main loop writes after it, the grant
`PLAY-dClosedLoop-3` and the extra unit's decision row `PLAY-dClosedLoop-2`, fixed for Phase 0 by the brief's item 3.
`open.py` builds every id from its parts and cites none.

## [acceptance]

1. `python open.py --write`: exit 0. "open: wrote and staged 44 files, 22 contract rows in
   memory/project/readme-contract.txt and 22 packets, opened 2026-10-20; run `gen_build_index.py --write` next". The
   44 files are 22 READMEs, 21 chain `BACKLOG.md` files (none for dTrueNorth) and dClosedLoop's `BACKLOG.md`.
2. `python gen_build_index.py --write`: exit 0. "build-index: wrote 1561 artifact(s)", over "backlog 889 ask(s) · 1270
   row(s) · 126 link(s) in 149 file(s) · 551 live · 0 verdict(s)". It filled each README's `ids:` and appended the
   three generated regions after the `roster:units` pair, and re-rendered `memory/LIVE.md`, the four family views
   under `memory/backlog/`, `memory/ledger/2026-10.md` and dClosedLoop's README.
3. `python open.py --check`: exit 0. "open: check of the opening of 2026-10-20 · 65 files byte-compared · roster arm
   over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 0"
4. `python gen_build_index.py --check`: exit 0. "build-index: clean (1561 artifact(s))", with "0 verdict(s)": every
   ask the opening files carries an `accept` clause and a SEV row.
5. `python gen_build_index.py --check-format`: not run. The scratch-guard hook refused it to this role: "BLOCKED by
   scratch-guard: a role agent runs no gate ... row G1 leg, the leg "build README slot contract"". It is owed at the
   close, with its red test (`[red]` 4). Acceptance step 8 is the probe that stands in for its budget arm until then.
6. `python packet.py --check <slug>`, once per chain build, exit 0 each. The line each printed, after its slug and
   packet path, was "byte compare green · completeness 0 findings over clauses C, gaps G, parents P, owed O, roster
   R, asks 7 · pin arm 6 instruments, 0 findings", with:

   | Build | C | G | P | O | R |
   |---|---|---|---|---|---|
   | dTrueNorth | 6 | 3 | 1 | 0 | 7 |
   | dGroundRules | 11 | 3 | 1 | 1 | 11 |
   | dSafePassage | 13 | 13 | 1 | 0 | 13 |
   | dOrderedCharter | 37 | 31 | 1 | 3 | 37 |
   | dFairHearing | 18 | 13 | 1 | 0 | 18 |
   | dDeclaredLoop | 34 | 17 | 2 | 4 | 34 |
   | dPlacedRequest | 21 | 18 | 1 | 0 | 21 |
   | dKeptSession | 28 | 8 | 2 | 1 | 28 |
   | dBoundRoles | 26 | 22 | 3 | 4 | 26 |
   | dFurnishedOrders | 20 | 13 | 1 | 0 | 20 |
   | dTotalRecall | 26 | 22 | 3 | 7 | 26 |
   | dLinkedLibrary | 25 | 23 | 1 | 0 | 25 |
   | dMindYourWords | 17 | 11 | 4 | 1 | 17 |
   | dWellOiledMachine | 61 | 63 | 3 | 5 | 61 |
   | dWitnessedBar | 30 | 27 | 1 | 0 | 30 |
   | dRankedPlan | 16 | 10 | 3 | 1 | 16 |
   | dIndexedDesign | 16 | 13 | 5 | 2 | 16 |
   | dScopedBuild | 15 | 10 | 4 | 1 | 15 |
   | dShippedRelease | 31 | 24 | 6 | 1 | 31 |
   | dTendedCadence | 18 | 14 | 5 | 2 | 18 |
   | dCalibratedLens | 17 | 13 | 2 | 0 | 17 |
   | dConvergedCharter | 23 | 15 | 4 | 1 | 23 |

   The six pinned instruments are `carries.py`, `deviations.py`, `asbuilt.py`, `packet.py`, the schedule script and
   `open.py`. dTrueNorth's roster of 7 is its six clauses and its extra unit.
7. `python bare-ids.py`: exit 1, 1084 lines. `python probe-bare.py <its output>`: exit 0, "opening's own files: 43
   files, 1062 hits, 0 of them ids the opening did not mint", and one file elsewhere: this record as committed at
   `429ad182d`, 22 hits on its `[summary]` rows and its `[red]` 9 line, "minted by the opening: 22 of 22". The
   opening's hits are roster units and carry-forward asks in its own packets (each roster line names its unit twice)
   and chain `BACKLOG.md` files (ask and SEV row). No other file under `memory/` holds a chain id. As the brief scopes
   it, this output names only ids the opening minted, the plan's known defect
   (`build/2026-10-20-build-PLAY-dClosedLoop-1-phase0-revision-brief.md`, finding 11), so it is recorded and not
   chased.
8. `python probe-slots.py`: exit 0. Largest authored slots: the problem 684 B (dWellOiledMachine) of 900; the
   improvements 364 B (dTrueNorth) of 500; the detriments 166 B (dDeclaredLoop) of 500; the build-level rules 1782 B
   (dWellOiledMachine) of 1800; the parked decisions 4 B of 1800. "over ceiling: none"; "lines over 350 characters
   (ids: excluded): none". Every slot's heading order matched the canon. The rules slot sits under its ceiling by 18
   B in the largest driver-changing build. Every opened README's rules slot is over the 823 B advisory high-water
   that `tools/memory-tree/build-readme-slot-highwater.txt` records, so `--check-format` will print an advisory line
   for each, which never changes its exit.
9. `python open.py --families`, `--driver-builds`, `--carriers` and `--summary`: exit 0 each, printed whole below.
10. `git add -A; git commit` (scratch, the opening commit `c67e46ce6be7`), then `python open.py --carriers --check`:
    exit 0. "open: carriers at HEAD c67e46ce6be7 against the list at the opening commit c67e46ce6be7 · 112 entries
    now, 112 listed · findings 0"

In the main loop's worktree, where nothing is opened, `python open.py --check` exits 2, "open:
memory/builds/dTrueNorth/README.md does not exist: nothing is opened to check", and
`python open.py --carriers --check` exits 2, "open: no commit in HEAD's history adds a chain build's README, so there
is no list at the opening commit to check against". Neither reads an empty population as green.

## [red]

Each plant goes into dGroundRules's opened files unless named otherwise, and is restored from the opening commit
after its run. `git diff --numstat` showed each edit's size before the run.

1. P0.7: a one-byte README edit (`goal bound.` to `goal bound!`, numstat "1 1"). `python open.py --check`: exit 1.
   "byte compare: memory/builds/dGroundRules/README.md differs from its render from line 19: gap-tool-24, gap-rt-34.
   Closing every one is this build's goal bound!"
2. P0.7: a roster missing one clause (the `cl-dClosedLoop-0012` row deleted, numstat "0 1").
   `python open.py --check`: exit 1, six findings, among them "roster arm: dGroundRules: `cl-dClosedLoop-0012` is in
   0 roster rows, not exactly one", beside the README's byte compare, the packet's byte compare and its packet arm
   (the packet carries the roster), and the summary arm's "Units reads `10` in the files, and the derivation gives
   `11`".
3. P0.7: a `parents:` typo (`dTrueNorth` to `dTrueNorht`, numstat "1 1"). `python gen_build_index.py --check`: exit
   1. "build-index: memory/builds/dGroundRules/README.md: parents: names 'dTrueNorht', which is not a build folder
   under memory/builds/ — an edge to nothing is a typo, not a relation". Then `python open.py --check`: exit 1, "byte
   compare: … from line 10: parents: dTrueNorht" and "summary arm: dGroundRules: `parents:` reads `dTrueNorht` in the
   files, and the derivation gives `dTrueNorth`".
4. P0.7: a removed contract row (`memory/builds/dGroundRules/README.md` deleted from `readme-contract.txt`, numstat
   "0 1"). `python open.py --check`: exit 1. "summary arm: dGroundRules: Contract row reads `absent` in the files,
   and the derivation gives `present, bound`". The red P0.7 names, `gen_build_index.py --check-format`'s, is owed at
   the close (acceptance step 5).
5. P0.5: a planted README whose family differs from its summary row (`roster: TOOL` to `roster: PLAY`, numstat "1
   1"). `python open.py --check`: exit 1. "byte compare: memory/builds/dGroundRules/README.md differs from its render
   from line 6: roster: PLAY" and "summary arm: dGroundRules: Family · `streams:` reads `PLAY · tooling` in the files,
   and the derivation gives `TOOL · tooling`". The summary arm names the disagreement on its own line.
6. P0.8 row 9: a planted new kit directory (`tools/newkit/kit.toml`, committed).
   `python open.py --carriers --check`: exit 1. "tools/newkit/ (routed product paths; tracked tools/newkit/kit.toml)
   is under a selector, and the list at the opening commit c67e46ce6be7 omits it", with "113 entries now, 112 listed".
7. The reverse arm, which reads the list both ways: a listed carrier removed (`git rm tools/settings-merge.py`,
   committed). `python open.py --carriers --check`: exit 1. "tools/settings-merge.py is on the list at the opening
   commit c67e46ce6be7, and nothing tracked at HEAD sits under it", with "111 entries now, 112 listed".
8. The owed-asks arm: one clean-reading ask row removed from dClosedLoop's `BACKLOG.md` (`PLAY-dClosedLoop-13`'s,
   numstat "0 1"). `python open.py --check`: exit 1, 67 findings: "owed asks: memory/builds/dClosedLoop/BACKLOG.md
   lacks the opening's row: - PLAY-dClosedLoop-13 · filed 2026-10-20 · …", and in all 22 packets, which carry every
   open ask in that file, a byte compare, a packet arm and a summary-arm Packet finding. Then
   `python open.py --write`: exit 1, "open: refused: memory/builds/dClosedLoop/BACKLOG.md exists without the
   opening's rows, and the opening writes it once".
9. The whole-run arm: a `BACKLOG.md` planted in dTrueNorth's folder (a copy of dGroundRules's).
   `python open.py --check`: exit 1. "byte compare: memory/builds/dTrueNorth/BACKLOG.md exists, and the opening
   writes none for a whole-run build" and "summary arm: dTrueNorth: Carry-forward ask reads `missing:TOOL-dGroundRules-12` in
   the files, and the derivation gives `none: whole run`".
10. The packet arm: a one-byte packet edit (`### Goal` to `### Goal!` in dGroundRules's packet, numstat "1 1").
    `python open.py --check`: exit 1. "byte compare: …-packet.md differs from its render", "packet arm: dGroundRules:
    byte compare: the packet differs from its render from line 13: ### Goal!" and the summary arm's Packet line,
    "30201 B · `packet.py --check` exit 1" against "30200 B · `packet.py --check` exit 0".
11. Every plant restored (`git status --short` empty): `python open.py --check`, exit 0, "findings 0";
    `python open.py --carriers --check`, exit 0, "112 entries now, 112 listed · findings 0".

## [families]

`python open.py --families`, whole:

```text
| Build | Stage | Slug noun | Word matched | Family |
|---|---|---|---|---|
| dTrueNorth | Fidelity | North | none | TOOL |
| dGroundRules | Policy | Rules | none | TOOL |
| dSafePassage | Supersession | Passage | none | TOOL |
| dOrderedCharter | Foundation | Charter | Charter | PLAY |
| dFairHearing | Review harness | Hearing | none | TOOL |
| dDeclaredLoop | Spine | Loop | none | TOOL |
| dPlacedRequest | Entry | Request | none | TOOL |
| dKeptSession | Session | Session | Session | KICK |
| dBoundRoles | Roles | Roles | none | TOOL |
| dFurnishedOrders | Orders | Orders | none | TOOL |
| dTotalRecall | Memory | Recall | none | TOOL |
| dLinkedLibrary | Library | Library | none | TOOL |
| dMindYourWords | Lexicon | Words | none | TOOL |
| dWellOiledMachine | Runtime | Machine | none | TOOL |
| dWitnessedBar | Test | Bar | none | TOOL |
| dRankedPlan | Plan | Plan | none | TOOL |
| dIndexedDesign | Design | Design | none | TOOL |
| dScopedBuild | Build | Build | none | TOOL |
| dShippedRelease | Deploy | Release | Deploy | DEPL |
| dTendedCadence | Maintain | Cadence | none | TOOL |
| dCalibratedLens | Review | Lens | none | TOOL |
| dConvergedCharter | Convergence | Charter | Charter | PLAY |
```

## [driver-builds]

`python open.py --driver-builds`, whole:

```text
The predicate (P0.5, walk answer 5): a v2 clause names `unattended.sh`, `check-unattended.sh`, `tools/unattended/`, the `/unattended` command, the unattended kit, `--plan`, `--status`, unattended's verbs, run claims; "the driver" alone is left out, since in v2 it names the loop's driver role. A build with an extra unit joins by it.

| Build | Clauses that touch the kit |
|---|---|
| dTrueNorth | its extra unit, the carry-forward condition in `unattended.sh` (the execution plan's `[phase-1]`) |
| dOrderedCharter | `cl-dClosedLoop-0047` (`unattended.sh`); `cl-dClosedLoop-0048` (`check-unattended.sh`) |
| dDeclaredLoop | `cl-dClosedLoop-0106` (`unattended.sh`, `check-unattended.sh`) |
| dPlacedRequest | `cl-dClosedLoop-0120` (run claims); `cl-dClosedLoop-0134` (run claims) |
| dWellOiledMachine | `cl-dClosedLoop-0280` (`--plan`, `--status`); `cl-dClosedLoop-0281` (unattended's verbs); `cl-dClosedLoop-0306` (the `/unattended` command, the unattended kit) |
| dWitnessedBar | `cl-dClosedLoop-0344` (the unattended kit) |
| dConvergedCharter | `cl-dClosedLoop-0485` (`unattended.sh`, `tools/unattended/`); `cl-dClosedLoop-0486` (`tools/unattended/`, the `/unattended` command, the unattended kit); `cl-dClosedLoop-0494` (the unattended kit); `cl-dClosedLoop-0496` (the unattended kit) |

7 builds, 13 clauses. Near misses, the clauses naming "unattended" that match no term, which the predicate leaves out:

- `cl-dClosedLoop-0032` (dOrderedCharter): "…fixed, rendered from the principle registry, the decision principles that resolve unattended forks, ranked above the practices, active practices, one…"
- `cl-dClosedLoop-0053` (dOrderedCharter): "a build run unattended by default from its request, said in the drive section,…"
- `cl-dClosedLoop-0108` (dDeclaredLoop): "…and trailer ids `routed_commits.py` reads and the trailer replacing the subject that unattended's `read_attribution_tokens` reads, each consumer naming…"
- `cl-dClosedLoop-0113` (dDeclaredLoop): "…says, a change that only adds items, roles, stages or stricter values applying unattended and recorded, one that removes, reorders or loosens…"
- `cl-dClosedLoop-0118` (dDeclaredLoop): "…set, which never passes, a wait declaring no deadline, a scenario successor cycle, an unattended raise of the budget, of a round count, of a retry count…"
- `cl-dClosedLoop-0123` (dPlacedRequest): "…by `placement` and recorded with its reason, its facts checked by `placement.check`, an unattended prompt placed the same way, the disposition carried in the…"
- `cl-dClosedLoop-0504` (dKeptSession): "…when the question arrives, and until dWellOiledMachine lands `next`, a question to an unattended build answered by the asker's declared default under…"
- `cl-dClosedLoop-0195` (dFurnishedOrders): "…lookup by a write set's paths retired with that selection, in the build method's and the unattended Skill's text among them, their readers inventoried by…"
- `cl-dClosedLoop-0240` (dLinkedLibrary): "…reuse scout's record instead, seen red on a planted spec citing `reuse_lookup` after it, unattended's `MAP_CLI`, re-pointed at the map's CLI, and the…"
- `cl-dClosedLoop-0426` (dShippedRelease): "an unattended `kits.offer` in a govkit mode that runs nothing from the…"

Clauses naming "the driver" and no term, left out: 8
```

## [carriers]

`python open.py --carriers`, whole. HEAD is the acceptance clone's scratch commit `f797b6179970`, `429ad182d` with
`open.py` added; no selector reaches `memory/builds/`, so the list is the same at `429ad182d`.

```text
Governance carriers at HEAD `f797b6179970`, P0.8 row 9's six selectors: 112 entries over 451 tracked paths.

1. routed product paths (`.memory-tree.conf` `ROUTED_PATHS`: tools/ skills/ coding-governance-agents.template.md WIRE-INTO-PROJECT.md): 63 entries, 17 kits with a `kit.toml`, 4 other directories, 42 files
   - `WIRE-INTO-PROJECT.md`
   - `coding-governance-agents.template.md`
   - `skills/deploy-governance/` · 1 tracked files
   - `skills/session-kickoff/` · 6 tracked files
   - `tools/agent-cap-restatement-waivers.txt`
   - `tools/agent-instructions/` · kit · 4 tracked files
   - `tools/branch-reconcile/` · kit · 6 tracked files
   - `tools/check-agent-cap-restatement.sh`
   - `tools/check-agent-cap-restatement.test.sh`
   - `tools/check-dead-paths.sh`
   - `tools/check-dead-paths.test.sh`
   - `tools/check-hook-destinations.sh`
   - `tools/check-hook-destinations.test.sh`
   - `tools/check-install-prefix.sh`
   - `tools/check-install-prefix.test.sh`
   - `tools/check-kit-placeholders.py`
   - `tools/check-kit-placeholders.test.sh`
   - `tools/check-kit-versions.sh`
   - `tools/check-line-length.sh`
   - `tools/check-line-length.test.sh`
   - `tools/check-microformats.sh`
   - `tools/check-microformats.test.sh`
   - `tools/check-placeholders.sh`
   - `tools/check-placeholders.test.sh`
   - `tools/check-playbook-parity.sh`
   - `tools/check-playbook-parity.test.sh`
   - `tools/check-remote-literals.sh`
   - `tools/check-remote-literals.test.sh`
   - `tools/check-spec-tokens.py`
   - `tools/check-spec-tokens.test.sh`
   - `tools/check-template-size.sh`
   - `tools/check-template-size.test.sh`
   - `tools/check-testsuite-counts.sh`
   - `tools/check-testsuite-counts.test.sh`
   - `tools/check-wiring.fragment.json`
   - `tools/check-wiring.sh`
   - `tools/check-wiring.test.sh`
   - `tools/codebase-map/` · kit · 20 tracked files
   - `tools/dead-path-waivers.txt`
   - `tools/drift-audit/` · kit · 8 tracked files
   - `tools/gate-legs.json`
   - `tools/gate-lint/` · kit · 6 tracked files
   - `tools/govkit/` · 24 tracked files
   - `tools/hooks/` · kit · 11 tracked files
   - `tools/lexicon/` · kit · 14 tracked files
   - `tools/lib/` · 15 tracked files
   - `tools/line-length-limits.txt`
   - `tools/memory-recall/` · kit · 17 tracked files
   - `tools/memory-tree/` · kit · 33 tracked files
   - `tools/playbook-kit-waivers.txt`
   - `tools/playbook/` · kit · 5 tracked files
   - `tools/process-monitor/` · kit · 13 tracked files
   - `tools/push-main.sh`
   - `tools/push-main.test.sh`
   - `tools/pytest-parallel-guardrails/` · kit · 7 tracked files
   - `tools/roles/` · kit · 31 tracked files
   - `tools/run-gates/` · kit · 45 tracked files
   - `tools/runlog/` · kit · 20 tracked files
   - `tools/settings-merge.py`
   - `tools/template-size-highwater.txt`
   - `tools/template-size-limits.txt`
   - `tools/unattended/` · kit · 50 tracked files
   - `tools/workflows/` · kit · 24 tracked files

2. git hooks (every tracked file under `.githooks/`, which `core.hooksPath` wires): 11 entries, 0 kits with a `kit.toml`, 0 other directories, 11 files
   - `.githooks/commit-msg`
   - `.githooks/gate-env.sh`
   - `.githooks/pre-commit`
   - `.githooks/pre-commit.test.sh`
   - `.githooks/pre-push`
   - `.githooks/pre-push.runlog.test.sh`
   - `.githooks/pre-push.test.sh`
   - `.githooks/pre-rebase`
   - `.githooks/pre_push_bar_selftest.py`
   - `.githooks/straggler-guard.sh`
   - `.githooks/straggler-guard.test.sh`

3. agent and role files (every tracked path under `.claude/`, a skill as its directory): 19 entries, 0 kits with a `kit.toml`, 7 other directories, 12 files
   - `.claude/agents/gov-builder.md`
   - `.claude/agents/gov-diff-reviewer.md`
   - `.claude/agents/gov-orienter.md`
   - `.claude/agents/gov-researcher.md`
   - `.claude/agents/gov-reuse-scout.md`
   - `.claude/agents/gov-skeptic.md`
   - `.claude/agents/gov-spec-reviewer.md`
   - `.claude/agents/gov-spec-writer.md`
   - `.claude/agents/gov-synthesizer.md`
   - `.claude/roles.json`
   - `.claude/rules/product.md`
   - `.claude/settings.json`
   - `.claude/skills/build/` · 1 tracked files
   - `.claude/skills/cleanup/` · 1 tracked files
   - `.claude/skills/drift-audit/` · 1 tracked files
   - `.claude/skills/lexicon/` · 1 tracked files
   - `.claude/skills/memory-recall/` · 1 tracked files
   - `.claude/skills/runlog/` · 1 tracked files
   - `.claude/skills/unattended/` · 1 tracked files

4. the charter (the template and its renders): 3 entries, 0 kits with a `kit.toml`, 0 other directories, 3 files
   - `AGENTS.md`
   - `CLAUDE.md`
   - `coding-governance-agents.template.md`

5. the method's guides (every tracked file under `memory/guides/`): 10 entries, 0 kits with a `kit.toml`, 0 other directories, 10 files
   - `memory/guides/ANNOTATION-STYLE.md`
   - `memory/guides/BUILD-METHOD.md`
   - `memory/guides/MERGE-BAR.md`
   - `memory/guides/PLAYBOOK-TEMPLATE.md`
   - `memory/guides/REVIEW-PROTOCOL.md`
   - `memory/guides/SESSION-KICKOFF.md`
   - `memory/guides/UNATTENDED-ASKS.md`
   - `memory/guides/UNATTENDED-PROTOCOL.md`
   - `memory/guides/UNATTENDED-STOPS.md`
   - `memory/guides/UNATTENDED-VERBS.md`

6. the root confs (a root `.<name>.conf`, `.gitattributes`, and every tracked file under `.governance/`): 7 entries, 0 kits with a `kit.toml`, 0 other directories, 7 files
   - `.codebase-map.conf`
   - `.gitattributes`
   - `.governance/deploy.toml`
   - `.lexicon.conf`
   - `.memory-tree.conf`
   - `.process-monitor.conf`
   - `.unattended.conf`
```

## [summary]

`python open.py --summary`, whole, read from the files the opening wrote in the acceptance clone:

```text
open: summary of the 22 chain builds, read from the files the opening wrote, opened 2026-10-20
| Build | Stage | `parents:` | Units | Family · `streams:` | Carry-forward ask | Packet | `may:` line | `spec-audit:` | Rule 8 · clean-reading ask | Contract row |
|---|---|---|---|---|---|---|---|---|---|---|
| dTrueNorth | Fidelity | dClosedLoop | 7 | TOOL · tooling | none: whole run | 18008 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 PLAY-dClosedLoop-2 | 2026-10-20 | yes · PLAY-dClosedLoop-11 | present, bound |
| dGroundRules | Policy | dTrueNorth | 11 | TOOL · tooling | missing:TOOL-dGroundRules-12 | 30200 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dSafePassage | Supersession | dGroundRules | 13 | TOOL · tooling | missing:TOOL-dSafePassage-14 | 30249 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dOrderedCharter | Foundation | dSafePassage | 37 | PLAY · playbook | missing:PLAY-dOrderedCharter-38 | 66983 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-12 | present, bound |
| dFairHearing | Review harness | dSafePassage | 18 | TOOL · tooling | missing:TOOL-dFairHearing-19 | 28948 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dDeclaredLoop | Spine | dOrderedCharter dFairHearing | 34 | TOOL · tooling | missing:TOOL-dDeclaredLoop-35 | 57328 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-13 | present, bound |
| dPlacedRequest | Entry | dDeclaredLoop | 21 | TOOL · tooling | missing:TOOL-dPlacedRequest-22 | 42163 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-14 | present, bound |
| dKeptSession | Session | dDeclaredLoop dPlacedRequest | 28 | KICK · kickoff | missing:KICK-dKeptSession-29 | 35754 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dBoundRoles | Roles | dDeclaredLoop dWitnessedBar dPlacedRequest | 26 | TOOL · tooling | missing:TOOL-dBoundRoles-27 | 43176 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dFurnishedOrders | Orders | dBoundRoles | 20 | TOOL · tooling | missing:TOOL-dFurnishedOrders-21 | 32034 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dTotalRecall | Memory | dDeclaredLoop dWitnessedBar dPlacedRequest | 26 | TOOL · tooling | missing:TOOL-dTotalRecall-27 | 45537 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dLinkedLibrary | Library | dTotalRecall | 25 | TOOL · tooling | missing:TOOL-dLinkedLibrary-26 | 38873 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dMindYourWords | Lexicon | dWellOiledMachine dWitnessedBar dLinkedLibrary dFurnishedOrders | 17 | TOOL · tooling | missing:TOOL-dMindYourWords-18 | 26856 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dWellOiledMachine | Runtime | dBoundRoles dTotalRecall dKeptSession | 61 | TOOL · tooling | missing:TOOL-dWellOiledMachine-62 | 110050 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-15 | present, bound |
| dWitnessedBar | Test | dDeclaredLoop | 30 | TOOL · tooling | missing:TOOL-dWitnessedBar-31 | 43018 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-16 | present, bound |
| dRankedPlan | Plan | dDeclaredLoop dTotalRecall dBoundRoles | 16 | TOOL · tooling | missing:TOOL-dRankedPlan-17 | 23925 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dIndexedDesign | Design | dDeclaredLoop dTotalRecall dKeptSession dBoundRoles dLinkedLibrary | 16 | TOOL · tooling | missing:TOOL-dIndexedDesign-17 | 28863 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dScopedBuild | Build | dIndexedDesign dWitnessedBar dWellOiledMachine dFurnishedOrders | 15 | TOOL · tooling | missing:TOOL-dScopedBuild-16 | 25472 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dShippedRelease | Deploy | dWitnessedBar dTotalRecall dBoundRoles dWellOiledMachine dLinkedLibrary dFurnishedOrders | 31 | DEPL · deployer | missing:DEPL-dShippedRelease-32 | 50810 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dTendedCadence | Maintain | dWitnessedBar dRankedPlan dWellOiledMachine dIndexedDesign dFurnishedOrders | 18 | TOOL · tooling | missing:TOOL-dTendedCadence-19 | 30709 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dCalibratedLens | Review | dTendedCadence dFairHearing | 17 | TOOL · tooling | missing:TOOL-dCalibratedLens-18 | 26499 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | no | present, bound |
| dConvergedCharter | Convergence | dScopedBuild dShippedRelease dCalibratedLens dMindYourWords | 23 | PLAY · playbook | missing:PLAY-dConvergedCharter-24 | 33804 B · `packet.py --check` exit 0 | may: PLAY-dClosedLoop-3 | 2026-10-20 | yes · PLAY-dClosedLoop-17 | present, bound |
```

## [comparison]

The plan's family table, driver-changing table and carrier list came from the plan writer's scratch probes at
`a93477abc` (P0.5, P0.8 row 9). v2 is byte-identical at `a93477abc` and at `429ad182d` (`git diff --quiet`, exit 0),
so every difference below is a difference of derivation, not of input.

- **Families.** No difference. All 22 rows match the plan's table cell for cell: the same slug noun, the same word
  matched (Charter for dOrderedCharter and dConvergedCharter, Session for dKeptSession, Deploy for dShippedRelease)
  and the same family, two PLAY, one KICK, one DEPL and eighteen TOOL.
- **Driver-changing builds.** The same seven builds and the same thirteen clauses as the plan's table. Two
  differences of presentation, none of membership:
  - order: the plan's table lists dWitnessedBar before dWellOiledMachine, and v2's `[chain]` lists dWellOiledMachine
    (row 14) first. `open.py` follows v2's order, as the brief's item 3 asks of the clean-reading asks, so
    dWellOiledMachine's is `PLAY-dClosedLoop-15` and dWitnessedBar's `PLAY-dClosedLoop-16`;
  - cells: the plan's table glosses what each clause does, and `open.py` names the predicate's term each clause
    matched.

  **A finding for the owner, not resolved here.** The near misses `--driver-builds` prints are ten clauses that say
  "unattended" and match no term. Three of them name a surface of the unattended kit by a word the predicate does not
  list:
  - `cl-dClosedLoop-0240` (dLinkedLibrary) re-points "unattended's `MAP_CLI`", a key `tools/unattended/unattended.sh`
    reads (its lines 562 and 10416-10418);
  - `cl-dClosedLoop-0195` (dFurnishedOrders) retires text from "the unattended Skill", `.claude/skills/unattended/`;
  - `cl-dClosedLoop-0108` (dDeclaredLoop) names "unattended's `read_attribution_tokens`", a function of
    `tools/unattended/lib-unattended.sh`. dDeclaredLoop is driver-changing already, by `cl-dClosedLoop-0106`.

  Under the predicate as P0.5 words it, which the plan's probe reproduced, neither dLinkedLibrary nor
  dFurnishedOrders is driver-changing, so neither README carries rule 8 and dClosedLoop's `BACKLOG.md` owes neither a
  clean-reading ask. If either build's change edits the kit, its close owes the unattended kit's suites with no
  waiver. `open.py` applies the predicate as written.
- **Carrier list.** No difference of membership: `probe-carriers-a93.py` derives 112 entries at `a93477abc` and the
  same 112 at HEAD. Against the plan's prose, the derivation finds 17 kits with a `kit.toml`, `tools/govkit/`,
  `tools/lib/`, 40 root-level files under `tools/` (scripts, their tests, `tools/gate-legs.json`, the waiver and
  limit lists), `skills/session-kickoff/` and `skills/deploy-governance/`, the two routed root files, 11 hooks, 9
  agent definitions, `roles.json`, 7 skills, `settings.json`, `rules/product.md`, the template, `AGENTS.md`,
  `CLAUDE.md`, the 10 guides and the 7 root confs. The plan gives no count for the root-level files under `tools/`,
  and lists the routed root files under the selector without counting them; the template sits under both the routed
  selector and the charter and is one entry.
- **How `--carriers --check` finds the row's list.** P0.8 row 9 says the row "quotes" the list `--carriers` derives
  at the opening commit. A `DECISIONS.md` row is one line within the 300-character entry budget, and the list is 112
  entries, so the row cannot hold it inline. `--carriers --check` therefore derives the list at the opening commit
  itself, the first commit in HEAD's history that adds dTrueNorth's README, and compares the list at HEAD against it
  both ways. This record's `[carriers]` section is the list as derived at `429ad182d`, which the opening does not
  change.

## [not-checked]

- `gen_build_index.py --check-format` over the opened tree, and its red on a removed contract row: refused to this
  role by the scratch-guard hook, owed at the close.
- The memory hygiene gate over the opened tree: a gate, run at the close.
- dTrueNorth's packet once the decision rows land. `packet.py` prints P0.8 row 1's id in its `missing:` form until
  `memory/DECISIONS.md` holds the row, so a packet rendered before the rows goes red on the byte compare once they
  land. The rows come first, then `open.py --write`.
- `handoff.py render` over the opened dTrueNorth, P0.3's acceptance, which the main loop re-observes.
- Whether a rule's or a slot's words say what the plan means: no arm reads meaning, and the owner reads dTrueNorth's
  README and packet whole (P0.7).

## The opening-read runs: nine driver builds and the README gap join

Dispatch 247's runs, as its brief asks (`build/2026-10-21-build-PLAY-dClosedLoop-1-phase0-brief-answers-builder.md`):
answers 3 and 5 of the execution record's `[phase0-answers-2]` applied to `open.py` and the gap join, and the opening
re-rendered on them. Every command, in order, with its exit and the line that proves it. `gap-join.py` is
`build/2026-10-19-build-PLAY-dClosedLoop-1-gap-join.py`, `<register>` the gap register and `<v2>` architecture v2,
both under `build/`. The runs happened in a `git clone --shared` of the main loop's worktree at `ddc6ba9fb`, on a
linked worktree at branch `p0-answers`, from its root under a bounded timeout. Its commits: `d07e3ca19` (the two
instruments), `e3369a999` (the bug-class checklist's fix to both), `bcc221781` (the re-rendered opening), and the
one that carries this section. Steps 4 to 10 ran on `d07e3ca19`'s blobs, and again in step 11 on `e3369a999`'s, which
every later step ran on: `open.py` blob `b1bb8b6d4c3a27d865a143de428b8331980778e9`, which every packet pins, and
`gap-join.py` blob `21a08df8d1633bbae649a61995137b200943b547`. The scratch probes sit in
the dispatch's scratch folder, never in the tree. A chain build's id appears here only in its `missing:` form, so the
build index joins none of them (P0.6).

### Before the change, at `ddc6ba9fb`

1. `python open.py --check`: exit 0. "open: check of the opening of 2026-10-21 · 65 files byte-compared · roster arm
   over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 0"
2. `python gap-join.py <register> <v2>`, the old blob `0c5d8fbb6`: exit 0. "register keys 386 · chain builds 22", then
   "unowned: none", "owned twice or more: none", "owned but not in the register: none", "builds owning nothing: none".
   Its output is kept as the comparison for steps 6 and 7.
3. `probe-arms.py`, which ran candidate arms over every v2 clause: exit 0. It printed 65 `KEY=` lines in
   `tools/unattended/.unattended.conf.example`, a superset of the 24 keys `tools/unattended/kit.toml`'s `[config]`
   lists. Five clauses name a kit key: `cl-dClosedLoop-0013` (`REVIEW_ROUNDS`, no re-point), `cl-dClosedLoop-0048`
   (`RECALL_CLI`, re-point), `cl-dClosedLoop-0106` (`REVIEW_ROUNDS`, re-point), `cl-dClosedLoop-0240` (`MAP_CLI`,
   re-point) and `cl-dClosedLoop-0284` (`RESUME_ATTEMPTS`, no re-point). One clause names the unattended Skill,
   `cl-dClosedLoop-0195`.

### The predicate (answer 3)

The arms: a clause that re-points a key the kit reads, read as a key of the kit's example conf, whole words, in the
same clause as a form of "re-point", and never a clause that only names a key; and a clause naming the unattended
Skill, whole words, any case. The conf is the source of the keys because its header says "The driver and the gate leg
READ these declarations; neither restates one", so no key is typed in `open.py`. v2's text for the two clauses
(v2:1773 and v2:1775): `cl-dClosedLoop-0195` retires the lookup "in the build method's and the unattended Skill's text
among them", and `cl-dClosedLoop-0240` names "unattended's `MAP_CLI`, re-pointed at the map's CLI". The seven builds
the walk's predicate counts keep `PLAY-dClosedLoop-11` to `-17`. A build that joins by answer 3's arms alone takes the
next id in v2's `[chain]` order: dFurnishedOrders (row 10) `PLAY-dClosedLoop-18` and dLinkedLibrary (row 12) `-19`.

4. `python open.py --driver-builds`: exit 0, whole:

   ```text
   The predicate (P0.5, walk answer 5): a v2 clause names `unattended.sh`, `check-unattended.sh`, `tools/unattended/`, the `/unattended` command, the unattended kit, `--plan`, `--status`, unattended's verbs, run claims; "the driver" alone is left out, since in v2 it names the loop's driver role. A build with an extra unit joins by it. The opening read's answer 3 adds two arms, whole words: a clause that re-points a key the kit reads, one of the 65 `KEY=` lines of `tools/unattended/.unattended.conf.example` beside a form of "re-point", never one that only names a key; and a clause naming the unattended Skill, whose text it edits.

   | Build | Clauses that touch the kit |
   |---|---|
   | dTrueNorth | its extra unit, the carry-forward condition in `unattended.sh` (the execution plan's `[phase-1]`) |
   | dOrderedCharter | `cl-dClosedLoop-0047` (`unattended.sh`); `cl-dClosedLoop-0048` (`check-unattended.sh`, `RECALL_CLI` re-pointed) |
   | dDeclaredLoop | `cl-dClosedLoop-0106` (`unattended.sh`, `check-unattended.sh`, `REVIEW_ROUNDS` re-pointed) |
   | dPlacedRequest | `cl-dClosedLoop-0120` (run claims); `cl-dClosedLoop-0134` (run claims) |
   | dFurnishedOrders | `cl-dClosedLoop-0195` (the unattended Skill) |
   | dLinkedLibrary | `cl-dClosedLoop-0240` (`MAP_CLI` re-pointed) |
   | dWellOiledMachine | `cl-dClosedLoop-0280` (`--plan`, `--status`); `cl-dClosedLoop-0281` (unattended's verbs); `cl-dClosedLoop-0306` (the `/unattended` command, the unattended kit) |
   | dWitnessedBar | `cl-dClosedLoop-0344` (the unattended kit) |
   | dConvergedCharter | `cl-dClosedLoop-0485` (`unattended.sh`, `tools/unattended/`); `cl-dClosedLoop-0486` (`tools/unattended/`, the `/unattended` command, the unattended kit); `cl-dClosedLoop-0494` (the unattended kit); `cl-dClosedLoop-0496` (the unattended kit) |

   9 builds, 15 clauses; 2 of the builds join by answer 3's arms alone (dFurnishedOrders, dLinkedLibrary), so their clean-reading asks take the ids after the others'. Near misses, the clauses naming "unattended" that match no term, which the predicate leaves out:

   - `cl-dClosedLoop-0032` (dOrderedCharter): "…fixed, rendered from the principle registry, the decision principles that resolve unattended forks, ranked above the practices, active practices, one…"
   - `cl-dClosedLoop-0053` (dOrderedCharter): "a build run unattended by default from its request, said in the drive section,…"
   - `cl-dClosedLoop-0108` (dDeclaredLoop): "…and trailer ids `routed_commits.py` reads and the trailer replacing the subject that unattended's `read_attribution_tokens` reads, each consumer naming…"
   - `cl-dClosedLoop-0113` (dDeclaredLoop): "…says, a change that only adds items, roles, stages or stricter values applying unattended and recorded, one that removes, reorders or loosens…"
   - `cl-dClosedLoop-0118` (dDeclaredLoop): "…set, which never passes, a wait declaring no deadline, a scenario successor cycle, an unattended raise of the budget, of a round count, of a retry count…"
   - `cl-dClosedLoop-0123` (dPlacedRequest): "…by `placement` and recorded with its reason, its facts checked by `placement.check`, an unattended prompt placed the same way, the disposition carried in the…"
   - `cl-dClosedLoop-0504` (dKeptSession): "…when the question arrives, and until dWellOiledMachine lands `next`, a question to an unattended build answered by the asker's declared default under…"
   - `cl-dClosedLoop-0426` (dShippedRelease): "an unattended `kits.offer` in a govkit mode that runs nothing from the…"

   Clauses naming "the driver" and no term, left out: 8

   Clauses naming a key the kit reads and no re-point, left out:

   - `cl-dClosedLoop-0013` (dGroundRules): `REVIEW_ROUNDS`
   - `cl-dClosedLoop-0284` (dWellOiledMachine): `RESUME_ATTEMPTS`
   ```

   dGroundRules stays out. Its `cl-dClosedLoop-0013` lists `REVIEW_ROUNDS` among the legacy homes and re-points
   nothing, the edge the plan writer's probe flagged and the main loop passed on. dWellOiledMachine's
   `cl-dClosedLoop-0284` names `RESUME_ATTEMPTS` as a cap and re-points nothing, and the build is driver-changing by
   three other clauses.
5. `python plant-arms.py`: exit 0. "plants: 8, wrong verdicts: 0", and "tree: 9 driver-changing builds; dGroundRules
   among them: False". The script runs `derive_kit_clauses` over planted clause texts, each a real v2 clause with at
   most one edit:
   - `cl-dClosedLoop-0013` as v2 writes it: not counted. With "re-pointed" planted beside its key: counted,
     "`REVIEW_ROUNDS` re-pointed";
   - `cl-dClosedLoop-0240` as written: counted, "`MAP_CLI` re-pointed". With its re-point removed: not counted. With
     the key misspelt `MAP_CLIX`: not counted, a whole-word miss;
   - `cl-dClosedLoop-0195` as written: counted, "the unattended Skill". With `Skillset` for `Skill`: not counted. With
     `skill` lower-cased: counted.

   The ids it derives: "dTrueNorth PLAY-dClosedLoop-11, dOrderedCharter PLAY-dClosedLoop-12, dDeclaredLoop
   PLAY-dClosedLoop-13, dPlacedRequest PLAY-dClosedLoop-14, dFurnishedOrders PLAY-dClosedLoop-18, dLinkedLibrary
   PLAY-dClosedLoop-19, dWellOiledMachine PLAY-dClosedLoop-15, dWitnessedBar PLAY-dClosedLoop-16, dConvergedCharter
   PLAY-dClosedLoop-17".
6. The plants seen red: `python plant-arms.py variants/open-names-key.py`, a scratch copy of `open.py` whose one
   changed line counts a key with or without a re-point (`if re.search(REPOINT, text)` made `if True`): exit 1. "BAD ·
   cl-0013 as v2 writes it: names `REVIEW_ROUNDS`, re-points nothing: counted", "BAD · cl-0240 with its re-point
   removed: … counted", "tree: 10 driver-changing builds; dGroundRules among them: True", "plants: 8, wrong verdicts:
   3". Under that variant dGroundRules would take `PLAY-dClosedLoop-18`, and dFurnishedOrders and dLinkedLibrary would
   shift to `-19` and `-20`.

### The gap join's README mode (answer 5)

`python gap-join.py --readmes <register> <v2> <builds dir>` reads the builds of v2's chain table, as the chain-table
mode does, and for each one the problem slot of `<builds dir>/<build>/README.md`. The slot is found by the heading
`gen_build_index.py`'s slot canon declares, and its lines are joined so a range wrapped across a line still expands.
A README that is absent, or holds no such slot, owns nothing. The join and its four findings are the chain-table
mode's, now one function both modes call.

7. `python gap-join.py <register> <v2>`, the new blob: exit 0, its output byte-identical to step 2's (`cmp`).
8. The chain-table mode's red is kept. A scratch copy of `<register>` gains one planted row, `| gap-zzz-01 | Plant |
   LOW | a planted orphan row | none | — |`. `python gap-join-old.py <it> <v2>` and `python gap-join.py <it> <v2>`:
   exit 1 each, their outputs byte-identical. "register keys 387 · chain builds 22", "unowned: ['gap-zzz-01']".
9. `python gap-join.py` with no arguments: exit 2, "usage: gap-join.py <register> <architecture> | --readmes
   <register> <architecture> <builds dir>". `python gap-join-old.py` with no arguments: exit 1, "IndexError: list
   index out of range".
10. `python gap-join.py --readmes <register> <v2> memory/builds`, on the opening as `ddc6ba9fb` holds it: exit 0.
    "register keys 386 · chain builds 22 · READMEs under memory/builds, 22 read, absent or without the problem slot:
    none" and the four findings "none". The opening does not change any problem slot, so the same holds at
    `bcc221781` (step 20).
11. `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` over `d07e3ca19`: exit 0. It selected
    `two-answers-to-one-question`. `open.py` spelled the whole-word key match twice, in the arm and in the
    left-out list, and `gap-join.py` spelled the range pattern twice. `e3369a999` gives each one spelling
    (`extract_kit_keys`, `RANGE`). Steps 4 to 10 ran again on it: `--driver-builds` printed the same bytes (`cmp`),
    the plants and the variant gave the same verdicts, and the join's outputs were byte-identical to step 2's and
    step 8's. The checklist over `e3369a999` selected the same classes and none applied.

### The opening re-rendered, at `e3369a999`

12. The 22 packet files removed from the working tree, so each renders fresh and pins every instrument at HEAD, as
    dispatch 244's re-render did. `packet.py`'s `render_packet` keeps an existing packet's pins, so a packet left in
    place would still pin `open.py`'s old blob `b8c9e9c04`, and its pin arm would red. That is a reading of the code,
    not a run. Then `python open.py --write --date 2026-10-21`, the date every opened README's `opened:` carries:
    exit 0. "open: wrote and staged 44 files, 22 contract rows in memory/project/readme-contract.txt and 22 packets,
    opened 2026-10-21; run `gen_build_index.py --write` next". dClosedLoop's `BACKLOG.md` existed, so `--write` added
    its two asks after `PLAY-dClosedLoop-17`'s row and its two SEV rows after `-17`'s, every other line kept.
13. `python gen_build_index.py --write`: exit 0. "build-index: wrote 1561 artifact(s)", over "backlog 891 ask(s) ·
    1272 row(s) · 126 link(s) in 149 file(s) · 553 live · 0 verdict(s)". Every file `git status` named was staged by
    name. Against `e3369a999`, the staged diff was 28 files. dFurnishedOrders' and dLinkedLibrary's READMEs gain rule
    8's two lines. dClosedLoop's `BACKLOG.md` gains four rows, and dClosedLoop's README its `ids:` through `-19`.
    `memory/LIVE.md` moves dClosedLoop's id count from 18 to 19, and `memory/backlog/PLAY.md` gains the two asks.
    Each of the 22 packets moves its `open.py` pin, its render HEAD and its two new ask lines. The two READMEs'
    packets also move every roster line number by two, the two lines rule 8 adds above the roster.
14. `python open.py --check`, staged and before the commit: exit 0, "… findings 0". Then the commit, `bcc221781`.

### On the committed opening, `bcc221781`

15. `python packet.py --check <slug>`, once per chain build: exit 0 each, "byte compare green · completeness 0
    findings over clauses C, gaps G, parents P, owed O, roster R, asks 9 · pin arm 7 instruments, 0 findings". C, G,
    P, O and R are `[acceptance]` step 6's for every build, unchanged. Each packet now carries the nine open asks of
    dClosedLoop's `BACKLOG.md`.
16. `python open.py --check`: exit 0. "open: check of the opening of 2026-10-21 · 65 files byte-compared · roster arm
    over 509 clauses · summary arm over 22 rows, 0 disagreements · findings 0"
17. `python gen_build_index.py --check`: exit 0. "build-index: clean (1561 artifact(s))", over "… 0 verdict(s)".
18. `python open.py --summary`: exit 0. Nine rows read "yes" in the rule 8 column: `PLAY-dClosedLoop-11` to `-17` as
    in `[summary]`, then "dFurnishedOrders … 33433 B · `packet.py --check` exit 0 … yes · PLAY-dClosedLoop-18" and
    "dLinkedLibrary … 40272 B · `packet.py --check` exit 0 … yes · PLAY-dClosedLoop-19". The other 13 read "no".
19. `python open.py --carriers --check`: exit 0. "open: carriers at HEAD bcc22178196a against the list at the opening
    commit b50573ef4b42 · 112 entries now, 112 listed · findings 0"
20. `python gap-join.py --readmes <register> <v2> memory/builds`: exit 0, as in step 10.
21. The README mode's plants, each in dGroundRules's README, `git diff --numstat` "1 1" or a removal, restored from
    `bcc221781` after its run:
    - an orphan gap, `gap-rt-34` removed from the problem slot: exit 1, "unowned: ['gap-rt-34']";
    - a double owner, dTrueNorth's `gap-mem-47` added to the slot: exit 1, "owned twice or more: {'gap-mem-47':
      ['dTrueNorth', 'dGroundRules']}";
    - the README removed: exit 1, "21 read, absent or without the problem slot: ['dGroundRules']", "unowned:
      ['gap-tool-24', 'gap-rt-34', 'gap-spine-06']", "builds owning nothing: ['dGroundRules']".

    Restored (`git status --short` empty): exit 0, every finding "none".
22. `open.py`'s red tests from `[red]`, each plant in dGroundRules's files unless named, restored after its run:
    - 1, a one-byte README edit (numstat "1 1"): exit 1, "byte compare: memory/builds/dGroundRules/README.md differs
      from its render from line 19: gap-tool-24, gap-rt-34. Closing every one is this build's goal bound!";
    - 2, the `cl-dClosedLoop-0012` roster row deleted ("0 1"): exit 1, six findings, among them "roster arm:
      dGroundRules: `cl-dClosedLoop-0012` is in 0 roster rows, not exactly one";
    - 3, a `parents:` typo ("1 1"): `gen_build_index.py --check` exit 1, "parents: names 'dTrueNorht', which is not a
      build folder under memory/builds/ …"; `open.py --check` exit 1, "summary arm: dGroundRules: `parents:` reads
      `dTrueNorht` in the files, and the derivation gives `dTrueNorth`";
    - 4, the contract row removed ("0 1"): exit 1, "summary arm: dGroundRules: Contract row reads `absent` in the
      files, and the derivation gives `present, bound`";
    - 5, `roster: TOOL` made `roster: PLAY` ("1 1"): exit 1, "summary arm: dGroundRules: Family · `streams:` reads
      `PLAY · tooling` in the files, and the derivation gives `TOOL · tooling`";
    - 8, `PLAY-dClosedLoop-13`'s ask row removed from dClosedLoop's `BACKLOG.md` ("0 1"): `open.py --check` exit 1, 67
      findings, "owed asks: memory/builds/dClosedLoop/BACKLOG.md lacks the opening's row: - PLAY-dClosedLoop-13 ·
      filed 2026-10-21 · …", with a packet arm in all 22 packets. Then `open.py --write --date 2026-10-21`: exit 1,
      "open: refused: memory/builds/dClosedLoop/BACKLOG.md exists without the opening's ask rows in order (8 of 9
      held), and the opening only adds the rows after its last". Nothing else was written;
    - 8b, the add path on a plant: `-19`'s ask row and SEV row removed ("0 2"), then `open.py --write --date
      2026-10-21` (exit 0) and `gen_build_index.py --write` (exit 0). `git diff HEAD --name-only` was empty: the
      working tree came back byte-identical to `bcc221781`, the two rows re-added where they were. The index held the
      authored halves `--write` staged, and was restored from HEAD;
    - 8c, dClosedLoop's `BACKLOG.md` with its two headings and no row: `open.py --write --date 2026-10-21` exit 1,
      "… exists without the opening's ask rows in order (0 of 9 held) …";
    - 9, a `BACKLOG.md` planted in dTrueNorth's folder (a copy of dGroundRules's): exit 1, "byte compare:
      memory/builds/dTrueNorth/BACKLOG.md exists, and the opening writes none for a whole-run build" and "summary arm:
      dTrueNorth: Carry-forward ask reads `missing:TOOL-dGroundRules-12` in the files, and the derivation gives `none:
      whole run`";
    - 10, `### Goal` made `### Goal!` in dGroundRules's packet ("1 1"): exit 1, "packet arm: dGroundRules: byte
      compare: the packet differs from its render from line 13: ### Goal!", and the summary arm's Packet line, "31600
      B · `packet.py --check` exit 1" against "31599 B · `packet.py --check` exit 0".

    Every plant restored (`git status --short` empty): `python open.py --check`, exit 0, "findings 0".
23. `python probe-rules-slot.py dFurnishedOrders dLinkedLibrary dWellOiledMachine dGroundRules`: exit 0. Against
    "## Build-level rules	1800" in `tools/memory-tree/build-readme-slot-limits.txt`: dFurnishedOrders 1780 B,
    dLinkedLibrary 1776 B, dWellOiledMachine 1782 B (as `[acceptance]` step 8 measured), dGroundRules 1540 B. The
    widest line is 118 characters.
24. `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` over `bcc221781`: exit 0. It selected 18 classes,
    none acted on. No row is missing: each packet reads `asks 9`, and the backlog view gains both asks. No path moved
    and nothing was `git rm`ed. The packets were staged by `open.py --write` before `gen_build_index.py --write` read
    the index.
25. With this section staged: `python bare-ids.py --opened`, exit 0, printing nothing, so no chain-slug id here or
    in the re-rendered opening joins a build it was not minted for; and `python gen_build_index.py --check`, exit 0,
    "build-index: clean (1561 artifact(s))".

### Where this changes the record above

- `[comparison]`'s finding for the owner is settled by answer 3: dLinkedLibrary and dFurnishedOrders are
  driver-changing, and their READMEs carry rule 8. `cl-dClosedLoop-0108` stays a near miss. It names a function of
  `tools/unattended/lib-unattended.sh`, which is no conf key and no Skill, and dDeclaredLoop is driver-changing by
  `cl-dClosedLoop-0106`.
- `[red]` 8's `--write` refusal still holds for a row lacked before a held one, now worded "exists without the
  opening's ask rows in order". A lacked row after the last held one is added (step 22, 8b), which is how this
  re-render filed `-18` and `-19`.

### Not checked here

- `[red]` 6 and 7, the carrier list's plants: each commits a change under `tools/`, which this pass may not make. This
  diff leaves `derive_entries` and `cmd_carriers` unchanged, and step 19 is green.
- `gen_build_index.py --check-format` and the memory hygiene gate over the re-rendered opening: gates, owed to the
  main loop.
- Whether a clause's re-point has the kit key it names for its object: the arm reads the two in one clause.
  `cl-dClosedLoop-0048` re-points the readers of the moved grammar, `check-unattended.sh`'s `RECALL_CLI` probe among
  them, and is driver-changing by `check-unattended.sh` in any case.
- A clause that edits the Skill's text without naming the unattended Skill, as by its path
  `.claude/skills/unattended/`: no v2 clause does, and no arm reads it.
