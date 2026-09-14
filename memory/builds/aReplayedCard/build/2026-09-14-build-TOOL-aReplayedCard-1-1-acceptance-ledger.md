# Acceptance ledger — TOOL-aReplayedCard-1, the commit deny

**Serves:** journal TOOL-aReplayedCard-1

Every observation below was made at the dispatched base tree (`e4325047`, the branch tip the unit
was handed) with the unit's working-tree changes applied, by running the self-test whole and by
running its orientation section against staged mutants of the hook. No figure is copied from the
brief or the spec; where the spec's wording was changed before the code, the rev-5 line in its
section 9 says what and why.

## What was built

- `tools/hooks/scratch-guard.js`: the second check, `checkOriented`, after the scratch verdict and
  under the same fail-open wrap; the six spec'd functions (`readCard`, `resolveToplevel`,
  `resolveCommonDir`, `extractCommitTarget`, `checkAuthorizedReadme`, `checkOriented`) plus
  `renderOrientationDeny`; the constants `COMMIT_SHAPED`, `GIT_VALUE_FLAGS`, `ANCHOR_MODES`, and
  `VIEW_TOKEN`, `VALUE_FLAG`, `SENTINEL` the grammar is built from. The header gains the ceiling
  paragraph and records the witness-line departure from "Allow = print nothing". The exports gain
  `buildComparablePath` and `ANCHOR_MODES`, both read by the self-test and nothing else.
  `KIT_SCRATCH_GUARD_VERSION` 1.0 → 1.1; the kit-entry marker (`agent-cap@1.14`) is untouched
  because the kit version is `agent-cap.js`'s constant and no gate pairs this file's own.
- `tools/hooks/scratch-guard.test.sh`: the `run_card` variant (exit AND stderr, `empty`, `one` or
  `any` with `;;`-separated needles, the same liveness guard as `run`), the fixture (a scratch
  repository with one commit and a linked worktree), `build_comparable`, `write_card`,
  `extract_git_spans`, and 62 arms across AC1–AC12; `FLOOR_ASSERTIONS` 60 → 122.
- `tools/hooks/README.md`: the section "scratch-guard's second check".
- `tools/gate-legs.json`: `skills/session-kickoff/` joins the `scratch-guard self-test` leg's guard;
  nothing else in the manifest moved.
- `memory/map/features/agent-cap.md`: the check under "Constraints & why", its ceiling under "Gaps";
  `memory/map/generated/symbols.json` regenerated for the new symbols.

## The wall, measured

The whole self-test on node `a`, 2026-09-14: **1m31s** on its first green-shaped run and **2m01s**
on the second, with the mutation runner and a lexicon pass sharing the host during the second. The
orientation section alone, run against a mutant copy with the meta-arm off, is 60–110 s of that,
almost all of it node spawns at 0.5–1 s each; the base-blob writer (`--card --write`, about ten git
spawns) is 4–9 s of it. The meta-arm re-runs the whole file, section included, so the suite pays
the section twice. The leg's ceiling is 490 s and was not moved.

## The bar at the pass boundary

`bash tools/run-gates/run-gates.sh` scoped, on the staged tree: 47 of 48 legs green, 3 skipped as
unchanged versus main, 55 held (every self-test; `scratch-guard self-test` among them, run standalone
above at `PASS (124 assertions)`), and ONE red — `verdict epoch (kit version dates the engine)`,
which names `e4325047` (the `KICK-aReplayedCard-2` commit) for moving 41 behaviour-bearing lines of
`tools/memory-tree/corpus_ids.py` with `KIT_MEMORY_TREE_VERSION` still at 2.74. That red is at the
base this unit was dispatched from, in files outside this unit's declared write set, and is not
fixed here: it owes the three-carrier bump the leg prints, in a commit at or after `e4325047`. The
`run-gates canary`, run standalone because the bar holds it: `PASS (148 assertions)`, with the
`skills/session-kickoff/` guard accepted as a tracked path. `memory hygiene` standalone: exit 0 in
1m10s. `lexicon naming predicates`: 984 offenders against the pin of 984 after the two nested
arrows in `checkAuthorizedReadme` were renamed to declared verbs (`runGit`, `readPaths`).

## RED before it landed — how each arm was staged

The orientation section was extracted into a partial suite (the fixture and its helpers, the
pre-existing scratch arms dropped, the meta-arm off, the floor zeroed; 54 assertions) and run
against twenty mutant copies of the hook, one staged break each. Every `run_card` arm went red under
at least one mutation, and the mutation names the predicate the arm pins; the four structural arms
went red under breaks staged in a copy of the suite itself. The runner and its report are in the
session's scratchpad, not in the tree; the mapping, read off the report, is:

- **M0 — `checkOriented` returns null (no check at all):** 22 red — every deny arm and every
  witness-line arm; the 32 that stayed green are the absence-shaped allows, staged below.
- **M1 — the sentinel satisfies the predicate (`ready` always true):** 16 red — every sentinel deny
  and every exemption arm, because the exemption is never reached when the sentinel passes.
- **M2 — the two toplevels compared as raw bytes:** 5 red — AC2's real-READY allow, AC3's
  rewritten cell, AC9's folded `-C` allow, and both AC10 allows: the writer's `C:/…` cell against
  node's `C:\…` toplevel denies the fleet.
- **M3 — no drive fold before the walk:** 2 red — the `/c/` spelling walked to nothing, so the
  deny allowed with the unwalkable line and the real-card allow printed it.
- **M4 — the worktree bytes read for a staged file:** 2 red — the staged-versus-worktree pair,
  inverted.
- **M5 — the exemption keyed on the folder existing in the tree (`ls-files` and `HEAD:`):** 11 red
  — AC5 fired the exemption on every later commit, and every staged-new arm lost it.
- **M6 / M17 — the replay header not read:** 1 red each — AC1's replay-written card denied.
- **M7 — `agent_id` ignored:** 1 red — AC6.
- **M8 — `tool_use_id` joins the fail-open set:** 22 red — no payload here carries it, so every
  deny and witness arm allowed silently; AC7's third arm is the one that names the field.
- **M9 — an absent card denies:** 3 red — both AC1 absence arms and AC10's removed-card control.
- **M10 — `commit` matched at a word boundary, `push` in the set:** 2 red — `git commit-tree` and
  `git push origin main` denied. (The report shows a third line under M10: AC11's cleanup arm, red
  on `sgtest-stray.md` — the stray the by-hand AC11 observation below had placed in the real common
  dir while M10 was running. A contamination of the run, and the same arm firing for its own
  reason.)
- **M11 — the value flags not skipped (plain dash tokens only):** 5 red — the four value-flag
  denies and the unwalkable `-C /nowhere/x` allow, none of which matched.
- **M12 — the README rule loosened to any `README.md`:** 1 red — `rebuilds/z/README.md` exempted.
  `docs/README.md` stayed denied because the PATHSPEC `*builds/*/README.md` never lists it, which
  is why **M18** loosens both: 2 red, `docs/` and `rebuilds/z/`.
- **M13 — the deny omits the card path and the remedy:** 12 red — every deny arm, on its needles.
- **M14 — a passing card prints a witness line:** 5 red — every present-card empty-stderr allow.
- **M15 — `ANCHOR_MODES` holds `prompt` only:** 3 red — the `recipe` arm, the staged-blob arm
  whose blob carried `recipe`, and AC11's parity arm.
- **M16 — the `-C` target ignored, `cwd` walked instead:** 4 red — both outside-cwd denies, the
  folded `-C` allow and the unwalkable-target allow.
- **M19 — the grammar matches every command:** 22 red — every engine span, every literal, the
  `ls` payload of AC12, and the `-C` arms, all denied or printing.
- **By hand, in a copy of the suite:** `SG_SPAN_FLOOR=9` — `extracted 8 spans, under the floor of
  9`; the extractor's refusal removed — `the extractor passed a fixture engine with no git span`;
  `SG_WRITER_BASE=0000000` — `the writer at 0000000 did not run from the linked worktree`; a stray
  `sgtest-stray.md` in this repository's real common dir — `a fixture card leaked`; the floor at 55
  over 54 executed — `arms are UNREACHABLE rather than absent`. The fixture-built arm was not staged:
  a `git init` that fails is not a break this suite can stage honestly.

Three arms were found red by the FIRST full run, two defects in the suite and none in the hook's
predicate: the deny printed the card path as node spells it (`C:\…`) while the AC2 and AC10 arms
asserted the hook's own fold, so the hook now prints `buildComparablePath(card.path)` and the
needle is that fold; and the AC8 arm measured a fixture whose index was NOT empty, because `git rm --cached` REFUSES a file whose
index blob differs from both HEAD and the worktree — exactly the state the staged-versus-worktree
pair builds — and the refusal left the README staged without the key. Every fixture cleanup now
passes `-f`, with the comment naming why. Neither moved the hook.

**Evidences:** TOOL-aReplayedCard-1

- AC1 — `scratch-guard.test.sh` — a `git commit -m x` payload for `sgtest-a1` with no `orientation/` directory in the fixture's common dir: exit 0, stderr exactly one line carrying `absent` and the card's folded path; the same with the directory present: exit 0, one line, `absent`; a card for `sgtest-a2` whose header names `--card --replay` and whose only READY line is the sentinel: exit 0, one line carrying `replay-written` and the path. Red under M0 (nothing printed), M9 (absence denied) and M6/M17 (the replay card denied).
- AC2 — `scratch-guard.test.sh` — a `--write` card for `sgtest-b1` holding `READY — none yet` only: exit 2, stderr carrying the folded card path, the word `sentinel` and `/session-kickoff`; the same card with `READY — sgtest · node a · …` and a `tree —` cell naming the worktree: exit 0, stderr byte-empty. Red under M0, M1 (the sentinel satisfied the predicate), M13 (the deny omitted the path and the remedy) and M14 (the allow printed).
- AC3 — `scratch-guard.test.sh` — B is `git worktree add` of the fixture; a card written naming A in its `tree —` cell, a payload with B's `node -p process.cwd()`: exit 2, stderr naming A's toplevel as git spells it and `cd <B folded> && /session-kickoff`, the card found through B's `.git` FILE (`gitdir:` then `commondir` `../..`); the cell rewritten to B: exit 0, stderr byte-empty. Red under M0 and M2 (a byte compare denied the rewritten cell).
- AC4 — `scratch-guard.test.sh` — a staged new `builds/x/README.md` carrying `authorized-by: prompt` under a sentinel card: exit 0, one line carrying `exempt`, the path and `prompt`; the same at `memory/builds/y/README.md`: exit 0, one line; with `authorized-by: recipe`: exit 0, one line carrying `recipe`; the staged blob carrying the key and the worktree copy overwritten without it: exit 0; the staged blob lacking the key and the worktree copy carrying it: exit 2; a new `docs/README.md` and a new `rebuilds/z/README.md` carrying the key: exit 2 each. Red under M0, M4 (the worktree bytes were read: the pair inverted), M12 (the loosened rule exempted `rebuilds/z/`), M18 (the loosened pathspec and rule exempted `docs/` too) and M15 (`recipe` refused).
- AC5 — `scratch-guard.test.sh` — the `memory/builds/y/` folder committed in HEAD and `unrelated.txt` staged, a `git commit -m y` payload under the sentinel card: exit 2, stderr carrying `sentinel` and `/session-kickoff`. Red under M5 (the exemption keyed on the folder's existence and fired).
- AC6 — `scratch-guard.test.sh` — the sentinel card and a payload carrying `agent_id`: exit 0, stderr byte-empty. Red under M7.
- AC7 — `scratch-guard.test.sh` — a payload lacking `session_id`: exit 0, nothing printed; lacking `cwd`: exit 0, nothing printed; carrying both and lacking only `tool_use_id`, under the sentinel card: exit 2. Red under M0 and M8 (`tool_use_id` joined the fail-open set and the third arm allowed).
- AC8 — `scratch-guard.test.sh` — an untracked `memory/builds/y/README.md` carrying `authorized-by: prompt`, nothing staged, the sentinel card, and `git add memory && git commit -m z` from the fixture's `memory/` subdirectory as its payload `cwd`: exit 0, one line carrying `exempt` and the path. Red under M0 and M5, and red in the first full run for the suite's own `git rm --cached` defect above.
- AC9 — `scratch-guard.test.sh` — the arm extracted **8** inline `git ` spans from `skills/session-kickoff/SKILL.md` between `## Step 0` and `## Step 5` and printed the count against the pinned floor `8`; each span, the five Step 1 literals and `git merge-base origin/main HEAD`, `git log --grep commit`, `git commit-tree`, `git push origin main` fed under the sentinel card: exit 0 and stderr byte-empty, every one; `extract_git_spans` over a fixture engine with no span: exit 1 naming `empty population`; `git -C <fixture in /c/ spelling> commit -m y` from a payload `cwd` OUTSIDE the fixture, `git -C "<fixture toplevel>" commit -m y`, `git -c a=b commit` and `git -c "a=b" commit`: exit 2 each; the first with a real READY card naming the fixture: exit 0, stderr byte-empty; `git -C /nowhere/x commit`: exit 0 with one line carrying `no .git above`. Red under M10 (`git push origin main` and `git commit-tree` denied), M19 (every span and literal denied), M11 (the four value-flag denies allowed), M3 (the `/c/` spelling walked to nothing: the deny allowed with the unwalkable line and the real-card arm printed) and M16 (the `-C` target ignored: both outside-cwd denies allowed); the count arm and the extractor's refusal red by hand.
- AC10 — `scratch-guard.test.sh` — `git show c95fe32a:skills/session-kickoff/manifest-check.sh` extracted into the suite's mktemp and run as `--card --write --session sgtest-w1` from the linked worktree wrote the card under the fixture's common dir; the hook fed that file unchanged with the worktree's `node -p process.cwd()`: exit 2, stderr carrying `sentinel` and the folded card path; the sentinel line replaced by the real READY line through the suite's `sed`: exit 0, stderr byte-empty; the card removed: exit 0, one line carrying `absent`; a card holding the `/c/…` spelling of the worktree with the payload `C:\…`: exit 0, stderr byte-empty. Red under M0, M1, M2 (the writer's `C:/…` cell against node's `C:\…` toplevel denied on bytes) and M9; the writer arm red by hand at a base that does not resolve.
- AC11 — `scratch-guard.test.sh` — after the whole run, `git rev-parse --git-common-dir` from the suite's directory listed no `orientation/sgtest-*` entry in this repository's real common dir; the parity arm read `SECOND_ANCHOR_MODES="prompt recipe"` from the tracked `unattended.sh` found by `git ls-files -- '*/unattended.sh'` and found the hook's `ANCHOR_MODES` joined equal to it. Red under M15 (`prompt` alone against the driver's pair); the cleanup arm red by hand with a stray `sgtest-stray.md` placed in the real common dir before a run of the orientation-only copy, `a fixture card leaked into this repository's common dir: sgtest-stray.md`, removed after.
- AC12 — `scratch-guard.test.sh` — `PASS (124 assertions)` on node `a` against `FLOOR_ASSERTIONS=122`; an `ls` payload under the sentinel card: exit 0, stderr byte-empty. Red under M19 for the `ls` payload denied and M14 for the allow that printed; the floor red by hand on the orientation-only copy, `executed 54 assertions against a floor of 55`.
