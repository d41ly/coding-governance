# TOOL-aSweptBar-4 — shipped-surface bans: each ban's own remedy, applied to the offenders it names

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-1 · base 53b25884 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aSweptBar-1-brief.md](../prompts/2026-10-13-prompt-TOOL-aSweptBar-1-brief.md) | research | TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |
| [2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aSweptBar-1-6-closing-diff-round1.md) | diff-review | TOOL-aSweptBar-1 TOOL-aSweptBar-2 TOOL-aSweptBar-3 TOOL-aSweptBar-5 TOOL-aSweptBar-6 |

<!-- /gen:spec-records -->

## 1. Goal

The full bar with self-tests over local main `53b25884` reds the shipped-surface ban arms S1 to
S10 name, on offenders that landings merged without a bar left behind. Apply each arm's own printed
remedy to the offenders it names, so each reads green with no waiver and no ban, predicate or arm
changed.

## 2. Scope (IN)

- **S1** — install-prefix, scratch-guard: every role-gate arm of `tools/hooks/scratch-guard.test.sh`
  spells its kit segment through a variable, and passes the hook the same command bytes as at the
  unit's parent. Observed by AC1 and AC2.
- **S2** — install-prefix, agent-cap: the rule-6 fixture of `tools/hooks/agent-cap.test.sh` spells
  its harness directory through `HO_WF`, its bytes otherwise unchanged. Observed by AC3.
- **S3** — install-prefix, `tools/run-gates/README.md`: the two `run-held-wsl.sh` invocations take
  the drained `<prefix>/` token. Observed by AC4.
- **S4** — remote literals: `tools/run-gates/run-held-wsl.sh --setup` resolves its remote through
  an inlined, marked `remote_ladder_sh` copy, and `memory/project/spawn-idiom-sites.txt` declares the
  fork idioms that copy carries. Observed by AC5 and AC6.
- **S5** — encoding posture: `read_git` in `tools/run-gates/held_halves.py` names
  `encoding="utf-8"`. Observed by AC7.
- **S6** — python resolver: `tools/govkit/selftest.py` resolves the run-gates seed's `{prefix}`
  through its inlined `resolve_prefix_token`, and `tools/hooks/format-guard.test.sh` reads its
  `resolve_kit_dir` heredoc with the builtin `read`. Observed by AC8 and AC9.
- **S7** — memory-hygiene `--render`: `tools/memory-tree/SPEC-TEMPLATE.template.md` spells the
  review protocol as `{{REVIEW_PROTOCOL}}`, and gov's `memory/TEMPLATE-SPEC.md` is its re-render.
  Observed by AC10.
- **S8** — playbook parity check 16: `tools/memory-tree/README.md` cites the charter's `[security]`
  handle where it cited a numbered section. Observed by AC11.
- **S9** — check-wiring BP2 AC12: `KIT_FILE_PAIRS` in `tools/check-wiring.sh` lists the
  `roles workflows.toml` pair its `check_roles` call site passes. Observed by AC12.
- **S10** — shell hygiene, a loop fed by a command substitution: the held-tier selection loop of
  `tools/run-gates/run-gates.sh` and the agent-type population loop of
  `tools/workflows/check-protocol-parity.test.sh` read a scratch file, so each file's measured count
  equals its row in `memory/project/substitution-fed-loops.txt`. Observed by AC13.

## 3. Non-goals (OUT)

- Anything under `tools/roles/`, `.claude/agents/`, `.claude/skills/build/` or `tools/playbook/`.
  The playbook-parity check 16 hits there are aOrientedCast's, which re-keys the roles kit.
- The python resolver leg's findings under `memory/builds/` (a bare launcher in build records, and a
  hand `{prefix}` in `-12-select-sim.py`). They are `TOOL-aSweptBar-6`'s.
- The memory-hygiene self-test's `GIT_INDEX_FILE` arm, which is `TOOL-aSweptBar-1`'s, and the fork
  idioms `tools/hooks/format-guard.test.sh`, `tools/hooks/scratch-guard.test.sh` and
  `tools/run-gates/run-gates.sh` carry, which are `TOOL-aSweptBar-5`'s.
- Converting the `var-pipe` idioms inside the remote ladder. The canonical and every inlined copy
  move together or the parity arm reds, which is a unit of its own across every copy.
- Kit version bumps. Off the push boundary `kit epoch` prints `owed at the lander` and does not fail
  (`tools/govkit/govkit.py`, the `epoch` docstring at line 13060), so the lander mints them.
- Renaming an arm or changing what any arm asserts: only how a command or path is spelled.

### Edges

- **hands-off** `TOOL-aSweptBar-6` — S9 lets `check_roles` resolve its pair inside the one batched
  python start, so the `check-wiring` row of `memory/project/fork-ceilings.txt` may measure lower
  over this unit's tree; that unit lowers the row to the count it measures.

## 4. Design

One mechanism: the remedy each ban arm prints beside its finding, applied to the offenders it named
over `53b25884`. The leg logs under `.git/worktrees/bar-53b2/gate-logs/` are the evidence, and every
line number below is at that base.

**S1.** The 44 role-gate arms (lines 1082-1142, PINNED from the leg log) type a kit name after the
fixture's literal `kit/` prefix, which rule 3 of `tools/check-install-prefix.sh` counts. The gate's
header names the fixture form in its first DOES-NOT-CHECK row: a kit name held in a variable. The
run-gates segment reads `RUN_GATES`, which the suite already derives at line 126. The seven other
kits read bare assignments `SG_K_<KIT>=<kit>`, written once above the
`write_gate_manifest kit/gate-legs.json` call with one comment line naming the gate's row, as
`tools/memory-tree/check-memory-hygiene.test.sh:3351-3353` does for its playbook fixture. An arm
whose command now holds a variable is double-quoted, and a `$` the shell must not expand (the
PowerShell arm's `$env:`) is escaped. The manifest `write_gate_manifest` writes keeps its
`{prefix}/<kit>/` spellings, which rule 5 drains. The invariant is the command bytes: G1 compares a
command word for word with that manifest (`tools/hooks/scratch-guard.js:109`), so a mis-expanded
command would turn a deny arm into a vacuous allow.

**S2.** Seven lines (2355 to 2502) spell `tools/workflows`, which rule 2 counts. One assignment
`HO_WF=workflows` sits beside `HOREPO=`. Each of the seven spells `tools/$HO_WF`, and inside the two
single-quoted JSON bodies the splice `'"$HO_WF"'`. Rule 6 compares a harness by its path relative to
the checkout (`tools/hooks/agent-cap.js:2154`), so only the bytes matter, and they do not move.

**S3.** Lines 699 and 703 spell `bash <prefix>/run-gates/run-held-wsl.sh`, rule 5's prose token.

**S4.** `--setup` reads the hosted URL with `git remote get-url origin` (line 166). The
`remote_ladder_sh` block of `tools/lib/resolve-remote.sh` is inlined, markers included and
byte-identical, after `print_refusal` is defined. The setup step then runs
`resolve_remote_sh || print_refusal "$RR_WHY"`, and refuses an empty `RR_REMOTE`, because a clone
with no remote has no hosted URL to name. It reads `GH` from `git remote get-url "$RR_REMOTE"`. The next refusal names
`$RR_REMOTE` where it named origin. On gov's node `origin` is the only remote, so the URL is the
same. On a node with several remotes and no branch remote, `--setup` now refuses naming
`GOV_REMOTE`, which is the ladder's contract. The mirror's own remote keeps the name `origin` the
README gives it. The parity arm of `tools/lib/resolve-python.test.sh` finds the copy by its marker
(line 208), so no parity row is added.

The block carries three `var-pipe` sites the `shell hygiene (a fork spent on builtin work)` leg
counts (`scan_spawn_file` over `tools/lib/resolve-remote.sh`, PINNED 2026-10-13 at `53b25884`), and
a byte-identical copy cannot convert them in place. They are declared as one row
`tools/run-gates/run-held-wsl.sh`, `var-pipe`, with a reason naming the inlined block, in the shape
the `tools/run-gates/post-merge.sh` and `tools/push-main.sh` rows carry for theirs. The leg's printed
remedy names a declared row as one of its two answers, and the growth is the one the remote-literals
remedy decides, so the brief's no-raise rule is met.

**S5.** The `subprocess.run` inside `read_git` (line 326) passes `encoding="utf-8"` beside
`text=True`.

**S6.** `tools/govkit/selftest.py` line 2779 resolves `{prefix}` by hand,
`.replace("{prefix}", PFX[:-1])`. It calls `resolve_prefix_token(x, PFX.rstrip("/"))` instead,
as line 608 already does, and keeps its `{kit}` replace. At a root install `PFX` is empty, where the hand form produced a
leading `/` and the resolver drops the token with its slash. `tools/hooks/format-guard.test.sh`
line 62 captures its heredoc with `$(cat <<'RKD'`. Its wrapper takes the builtin-read form
`tools/hooks/scratch-guard.test.sh` carries at lines 75-123, and the block between the markers is
untouched.

**S7.** `tools/memory-tree/SPEC-TEMPLATE.template.md` line 384 names `REVIEW-PROTOCOL.md`, a gov
path in every adopter's render (TOOL-aDistilledCharter-9). It spells `{{REVIEW_PROTOCOL}}`, which
`derive_kit_paths` answers with the review-harness kit's receipt row or the phrase "the review
protocol of this repo" (`tools/memory-tree/adopt-memory-tree.sh:303,310`). The dogfood copy is
re-rendered, never hand-edited, by `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.
Gov answers the phrase, as `memory/guides/BUILD-METHOD.md` line 130 already does.

**S8.** Line 526 says "any charter §9 surface". It names the surface by the charter's `[security]`
handle (`AGENTS.md` line 39), the form `tools/memory-tree/BUILD-METHOD.template.md:285` uses for
`[land]`.

**S9.** `KIT_FILE_PAIRS` (`tools/check-wiring.sh:574`) gains `roles workflows.toml`, the pair
`check_roles` passes `resolve_kit_file` at line 1688 (TOOL-aOrientedCast-8). A refused pair prints
an empty line in the batched start (line 534), so a tree without the roles kit is unaffected.

**S10.** Two sites the scan measures past their rows (`scan_file` probe, PINNED 2026-10-13):
`tools/run-gates/run-gates.sh` line 3060 reads `<<<"$_sel_out"` (TOOL-aSparedSpawn-12), and
`tools/workflows/check-protocol-parity.test.sh` line 445 reads `$_at_tracked` through a heredoc
(TOOL-aOrientedCast-4). Each takes the leg's printed remedy, a scratch file. The selection program
writes `"$WORK/held-select"` with its `|| echo` refusal kept, and the loop reads that file. The
population is written once to `"$TMPD/at-tracked"` and the loop reads it there, while
`_at_tracked` stays for the membership `case` inside the loop. The registry is unchanged, because
each file's count returns to its row.

### Inventory

| Identifier | Where | Graded by |
|---|---|---|
| `SG_K_HOOKS`, `SG_K_GOVKIT`, `SG_K_MEMORY_TREE` | `tools/hooks/scratch-guard.test.sh` | no cell: `.lexicon.conf` grades `sh.function` only |
| `SG_K_ROLES`, `SG_K_LEXICON`, `SG_K_WORKFLOWS`, `SG_K_UNATTENDED` | the same | no cell |
| `HO_WF` | `tools/hooks/agent-cap.test.sh` | no cell |
| `held-select`, `at-tracked` | scratch files under each script's own scratch dir | none |

No function is minted. `resolve_remote_sh` arrives as a copy of an existing canonical, and no new
file or inventory key is added.

### Files touched (estimate)

- `tools/hooks/scratch-guard.test.sh`
- `tools/hooks/agent-cap.test.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-held-wsl.sh`
- `memory/project/spawn-idiom-sites.txt`
- `tools/run-gates/held_halves.py`
- `tools/govkit/selftest.py`
- `tools/hooks/format-guard.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `tools/memory-tree/README.md`
- `tools/check-wiring.sh`
- `tools/run-gates/run-gates.sh`
- `tools/workflows/check-protocol-parity.test.sh`

### Alternatives rejected

- S2, a fixture directory with a non-kit name: rule 6 reads only the relative path, so it would
  pass, but the gate header names the variable form for a fixture and the harness home stays real.
- S4, the remote resolved in Python by `held_halves.py --host` through the inlined
  `remote_ladder_py`: it carries no fork idiom, but it moves the `--host` output contract and adds a
  `sed` parse on the shell side.
- S4, `git ls-remote --get-url` with no remote: it spells no literal, but git's own default is not
  the ladder and ignores `GOV_REMOTE`.
- S10, `done < <(...)`: the process substitution keeps the same EOF dependency and the leg only
  reports it, while the leg's remedy is a file.

## 5. Acceptance criteria

- **AC1** — When `grep -cE 'kit/(run-gates|hooks|govkit|memory-tree|roles|lexicon|workflows|unattended)/' tools/hooks/scratch-guard.test.sh`
  runs at the unit's tip, it prints 0. Red when: one role-gate arm still types a kit name after the
  fixture's `kit/` prefix.
- **AC2** — When a scratch probe stubs `run_role_bash` to print its sixth argument, evaluates the
  suite's own `SG_K_` and `RUN_GATES` assignments, then evaluates every arm line, the printout over
  the parent's file and over the tip's is identical and non-empty. Red when: a misspelled variable
  or a changed quote passes the hook a command other than the parent's.
- **AC3** — When `grep -c 'tools/workflows' tools/hooks/agent-cap.test.sh` runs at the tip, it
  prints 0. Reversing the substitution, `HO_WF` and its quote splice back to `workflows` and its
  assignment line dropped, reproduces the parent's file byte for byte. Red when: a fixture line keeps
  the literal, or the rule-6 block changed anything else.
- **AC4** — When `grep -c 'tools/run-gates/' tools/run-gates/README.md` runs, it prints 0, and
  `grep -c 'bash <prefix>/run-gates/run-held-wsl.sh' tools/run-gates/README.md` prints 2. Red when:
  either invocation keeps the literal prefix.
- **AC5** — When `grep -c 'get-url origin' tools/run-gates/run-held-wsl.sh` runs, it prints 0, and
  `grep -c 'get-url "$RR_REMOTE"' tools/run-gates/run-held-wsl.sh` prints 1. The lines between
  `# >>> remote_ladder_sh` and `# <<< remote_ladder_sh` in that file, CRs dropped, equal those of
  `tools/lib/resolve-remote.sh`. Red when: the literal remains, or the copy drifts by one byte.
- **AC6** — When `scan_spawn_file` of `tools/gate-lint/sh_hygiene.py` is imported and run over
  `tools/run-gates/run-held-wsl.sh`, every class it counts equals that file's row in
  `memory/project/spawn-idiom-sites.txt`, the `var-pipe` row included. Red when: the row is absent
  or its count differs from the scan's.
  figure: DERIVED, the scanner counts at observation time.
- **AC7** — When `python -I -B -c "import sys; sys.path.insert(0, 'tools/run-gates'); import held_halves as h; print(h.read_git(['rev-parse', 'HEAD']))"`
  runs at the tip, it prints the tip's sha, and the `subprocess.run` inside `read_git` carries
  `encoding="utf-8"`. Red when: the call has no `encoding=`, or the read returns empty.
- **AC8** — When `grep -nE "\.replace\([\"']\{prefix\}" tools/govkit/selftest.py` runs, every line
  it prints lies between `# >>> resolve_prefix_token` and `# <<< resolve_prefix_token`. Red when:
  the run-gates seed still resolves the token by hand.
- **AC9** — When `grep -c "IFS= read -r -d '' _rkd <<'RKD'" tools/hooks/format-guard.test.sh` runs,
  it prints 1, and `bash -n tools/hooks/format-guard.test.sh` exits 0. Red when: the `cat` capture
  remains, or the wrapper no longer parses.
- **AC10** — When a scratch adopter laid out as the memory-hygiene self-test's adopter-declared-paths
  arm lays it out (its lines 3357-3371) runs `adopt-memory-tree.sh --render`, its `TEMPLATE-SPEC.md`
  holds no `REVIEW-PROTOCOL.md`, and `grep -c 'pattern of the review protocol of this repo' memory/TEMPLATE-SPEC.md`
  prints 1 for gov's own render. Red when: the template still names the file.
  fixture: built under `%TEMP%` at a short name; none is in the tree. At `53b25884` the same
  fixture's line 384 names `REVIEW-PROTOCOL.md`, observed 2026-10-13, so the probe can read red.
- **AC11** — When `grep -cE '(charter|template|playbook|governance)s? ?§ ?[0-9]' tools/memory-tree/README.md`
  runs, it prints 0, and the R4 sentence names the `[security]` handle. Red when: line 526 still
  cites a numbered charter section.
- **AC12** — When the check-wiring self-test's BP2 AC12 comparison, its `_kfp` awk program lifted
  into a scratch probe, runs over `tools/check-wiring.sh`, it prints no `unlisted` pair.
  Red when: `KIT_FILE_PAIRS` lacks `roles workflows.toml`.
- **AC13** — When `scan_file` of `tools/gate-lint/sh_hygiene.py` is imported and run over the bar's
  runner and the protocol-parity suite, each file's gated sites per delimiter equal its row in
  `memory/project/substitution-fed-loops.txt`, and `bash -n` exits 0 over both.
  Red when: a converted loop still reads a heredoc or here-string over a substituted variable.
  figure: DERIVED, the scanner counts and the registry declares.

## 6. Gates

The close runs each of these, and each reads green over this unit's tree. These are the legs this
unit's offenders redden:

`install-prefix (shipped surface)` · `remote literals (kit code names no remote)` · `encoding posture (text IO names its encoding)` ·
`python resolver (behaviour + inline parity + idiom ban)` · `memory-hygiene self-test` · `playbook parity` ·
`check-wiring self-test` · `shell hygiene (a loop fed by a command substitution)`

These guard what the change touches, by the manifest's guards or by subject:

`shell hygiene (a fork spent on builtin work)` · `held-halves selftest` · `review-protocol parity (kit vs dogfood)` ·
`run-gates canary` · `kit/dogfood doc parity` · `agent-cap self-test` · `scratch-guard self-test` ·
`format-guard self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` ·
`govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms` ·
`straggler-guard arms` · `transition-audit arms` · `tier2-review self-test` · `unattended-build self-test`

No arm is added or moved, so this unit declares no new arm.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-13 · initial draft from the build brief's item 4, every offender re-read at
  `53b25884` and in the bar's leg logs.

## 9. Reuse audit

The probe, run as `reuse_lookup.py` with the phrase "fixture names a kit through a variable so
the install-prefix ban sees no literal", returned the `resolve_kit_dir` and `resolve_prefix_token`
seams, and the `memory/map/features/install-prefix.md` and `memory/map/features/run-gates.md`
dossiers cover the files touched. Every remedy extends a seam that already exists, and no new
mechanism is needed. The seams, each verified in source at `53b25884`:

- the `remote_ladder_sh` canonical in `tools/lib/resolve-remote.sh`, inlined as the remote-literals
  gate's remedy names, with `tools/run-gates/post-merge.sh` as the nearest consumer;
- the inlined `resolve_prefix_token` at `tools/govkit/selftest.py` lines 53-64, already called at
  line 608;
- the builtin-read `resolve_kit_dir` wrapper of `tools/hooks/scratch-guard.test.sh` lines 75-123;
- the `{{REVIEW_PROTOCOL}}` token `derive_kit_paths` already renders, used by
  `tools/memory-tree/BUILD-METHOD.template.md` at lines 130 and 331;
- the variable-held kit name of `tools/memory-tree/check-memory-hygiene.test.sh` lines 3351-3353;
- the scratch-file feed the loop leg prints as its remedy (`tools/gate-lint/sh_hygiene.py:461`).

The recall probe agreed with source on every seam it named. The brief cites `run-gates.sh:3060` and
the parity suite's loop as the two new sites; the `scan_file` probe confirmed both and placed the
parity suite's at line 445.

Recall terms used: install-prefix ban drained token remote ladder resolve_remote_sh
resolve_prefix_token encoding posture inline parity shipped surface. The question passed with them
was "how does a shipped file resolve a remote, a prefix token or a sibling kit without spelling a
literal".
