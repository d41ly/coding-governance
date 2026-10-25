# TOOL-dGroundRules-68 — the writer-split arms of the hook suite run inside a scratch checkout whose settings hold the stub limit, so rule 7 reads before it admits

**Status:** CLOSED · rev-1 · 2026-10-25 · node d · Tier-1 · base 7e845618 · streams tooling · order 22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-68-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-68-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-68-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-68-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-66 TOOL-dGroundRules-67 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

The four arms `TOOL-dGroundRules-18` added for a `gov:fixed-writers` split fail in every whole-suite
run of the hook suite, because their payloads carry no `cwd` and run from `$TMP`, which lies in no
checkout. Rule 7 refuses such a call before rule 2 judges it. This unit gives the block a scratch
checkout whose settings rule 7 admits, so each arm judges the rule it names. The fix is test-side.

## 2. Scope (IN)

- **S1** — The checkout. The `TOOL-dGroundRules-18` block of `tools/hooks/agent-cap.test.sh` builds
  its directory as a scratch git checkout on `main` with a committed tree, as the rule-7 block builds
  `$R7`. Its `.claude/settings.json` sets both agent-limit variables to `4`. Both payloads,
  `WS_WRITER` and `WS_VERIFIER`, carry that checkout as `cwd`. The stub `policy-mirror.js` beside the
  hook copy stays the only limit source. The block's comment is respelled to what holds, as §4 "The
  block" gives. Observed by AC1 and AC2.
- **S2** — The `no policy kit beside the hooks kit` arm keeps its name, its payload and its expected
  answer: exit 2, carrying `above the bound 5: MAX_VERIFIERS, as no policy kit`. Observed by AC3.
- **S3** — `tools/hooks/agent-cap.js` is unchanged. No arm is added to the suite or taken from it, and
  the suite carries no assertion floor to move. Observed by AC4.

## 3. Non-goals (OUT)

- Any change to `tools/hooks/agent-cap.js`. Rule 7 refuses a `cwd` it cannot read on purpose
  (`TOOL-dGroundRules-21` S38), and that refusal is correct here.
- The rule-7 block that builds `$R7`, the `$LIMREPO` arms, and every other block of the suite.
- A shared helper that builds a scratch checkout for both blocks. The suite has two such blocks after
  this unit, and the second adds three lines. The charter's factory rule applies to a kind, and a test
  fixture's setup lines are not one.
- Any other spec.

### Edges

none

This unit makes the arms of `TOOL-dGroundRules-18` (CLOSED) run as written, under the rule-7 refusal
`TOOL-dGroundRules-21` (CLOSED) added at `f6674a6a2`. It changes nothing either unit built in the hook.

## 4. Design

### Evidence

The main loop ran the hook suite at `4f76c4b39` in a scratch clone, and it printed 359 passed and 4
failed. The four failures are the block's first four arms. Each stderr was rule 7's refusal, that the
payload `cwd` is in no git checkout. This spec reproduced the same four failures at `7e8456181` with
the `WS_PROBE` block of §5, which printed `probe: 1 passed, 4 failed`.

The hook runs rule 6, then rule 7, then the script rules (`tools/hooks/agent-cap.js:1861`, `:1887`).
With a `policy-mirror.js` beside the hooks kit, `checkSettingsInForce` resolves the checkout root of
the payload `cwd`, or of the process directory when the payload names none (`:1784`). A directory in
no checkout is refused before any script rule runs (`:1785`). `run_limit_call` runs the hook from
`$TMP` (`tools/hooks/agent-cap.test.sh:1162`), and the block's payloads name no `cwd`
(`:1225-1226`). So the stub that arms rule 2's writer bound also arms rule 7's refusal. The comment at
`:1220` says rules 6 and 7 add nothing there. That stopped holding at `f6674a6a2`.

### The settings value

`checkSettingsInForce` reads the limit through the stub's `readPolicy`, which ignores the repository
and answers its literal. It then reads every settings layer under the checkout root
(`readSettingsLayers`, `:1979-2004`). It refuses a layer whose value is above the limit
(`Number(s) > limit`, `:1821`). The block writes stub limits of 4, then 6. A value of `4` is the
highest that both admit, and it sits at the lower stub's limit. Measured at `7e8456181`: with both
variables at `5`, the two stub-4 arms fail through rule 7 and the other three pass.

Rule 6 resolves the payload `cwd` first (`resolveRoleRoot`, `tools/hooks/scratch-guard.js:1396`).
The scratch checkout holds no `.claude/roles.json`, so `loadRoleIndex` answers absent (`:961`) and
rule 6 adds no rule. The suite unsets `CLAUDE_PROJECT_DIR` at its top (`tools/hooks/agent-cap.test.sh:10`).

### The block

Line `:1220` of the block's comment becomes the four lines below. Lines `:1218-1219` stay.

```
# policy-mirror.js answering the limit, which arms rule 7, so the arms run in a scratch checkout whose
# settings hold both variables at 4, at or under each stub limit below (TOOL-dGroundRules-68): rule 7
# admits, rule 6 finds no role index there, and each arm judges rule 2. With no stub, rule 7 adds no
# rule.
```

The `WS=` line (`:1221`) adds `"$WS/.claude"` to its `mkdir -p`. Directly after it go the settings
write and the checkout, before `write_limit_stub` is defined:

```
printf '{"env":{"CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS":"4","CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS":"4"}}\n' > "$WS/.claude/settings.json"
( unset GIT_DIR GIT_WORK_TREE; cd "$WS" && git init -q . && git symbolic-ref HEAD refs/heads/main && git config user.email t@t.test \
    && git config user.name t && git add -A && git commit -qm writer-split --no-verify )
```

The checkout line follows the `$R7` one (`:1198-1199`) and adds one thing: it unsets `GIT_DIR` and
`GIT_WORK_TREE` first, as the suite already does before its own git read (`:1190`). Otherwise an
exported `GIT_DIR` would point `git add -A` and `git commit` at another repository. The commit holds
the hook copy, `scratch-guard.js` and the settings file. The stub is written after it, by the
existing `write_limit_stub` calls, and the hook reads it from disk.

`WS_WRITER` and `WS_VERIFIER` (`:1225-1226`) each gain the `cwd` member directly after
`"tool_name":"Workflow",`. `NODEDIR` is the node-readable spelling of `$TMP` (`:775`), as the `$R7`
payload uses it (`:1200`):

```
"cwd":"'"$NODEDIR/writer-split"'",
```

No other line of the block changes. The five `run_limit_call` lines, `write_limit_stub` and the
`rm -f` of the stub keep their bytes.

### The no-policy-kit arm

Its expected answer does not move. With the stub gone, `checkSettingsInForce` returns at
`tools/hooks/agent-cap.js:1783`, before it resolves any checkout root, so rule 7 adds no rule in or
out of a checkout. Rule 2's `readWriterBound` then finds no `policy-mirror.js` and bounds the writer
split at `MAX_VERIFIERS`, naming `MAX_VERIFIERS, as no policy kit sits beside this hooks kit`
(`:467`). The settings file is not read there.

### The suite's floor and registries

The suite carries no executed-assertion floor: it is a row of
`memory/project/testsuite-count-waivers.txt` (`:10`). No arm is added or taken, so the suite's total
of 363 stands and the passed count rises by four. The added lines carry no command substitution, no
`cat` and no pipe, so the suite's rows in `memory/project/spawn-idiom-sites.txt` (`:116-117`) keep
their counts. They define no shell function, so the lexicon's function pins do not move.

### Alternatives rejected

- A bare `.git` directory, as `$LIMREPO` uses (`tools/hooks/agent-cap.test.sh:1158`). The root walk
  stats only `.git` (`tools/hooks/agent-cap.js:1317-1331`), so it would pass today. The brief names a
  real checkout built as `$R7` is, and a real checkout is what a harness starts in.
- Setting the variables through `GOV_SETTINGS_JSON`. That layer still needs a checkout root to read
  against (`:1986`), so it adds an export and saves nothing.

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/hooks/agent-cap.test.sh`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. AC1 to AC3 run the `WS_PROBE` block.
It evaluates the suite's own `run_limit_call` and the block's own lines, from the
`# TOOL-dGroundRules-18 ` comment to the no-policy-kit arm, so it exercises the built bytes without
running the suite.

```
WS_PROBE:
S=tools/hooks/agent-cap.test.sh; HERE="$PWD/tools/hooks"; TMP=$(mktemp -d); NODEDIR=$(cd "$TMP" && pwd -W 2>/dev/null || printf '%s' "$TMP"); pass=0; fail=0
eval "$(sed -n '/^run_limit_call() {/,/^}/p' "$S")"
eval "$(sed -n '/^# TOOL-dGroundRules-18 /,/^run_limit_call "writer split: no policy kit/p' "$S")"
echo "probe: $pass passed, $fail failed"; rm -rf "$TMP"
```

The whole suite is the `agent-cap self-test` leg, and the main loop's run at the close observes it
there. That run prints no `FAIL` line naming `writer split` or `verifier split`.

- **AC1** — When the `WS_PROBE` block runs, it prints five lines that begin `ok`, and its last line
  reads `probe: 5 passed, 0 failed`. At `7e8456181` it printed `probe: 1 passed, 4 failed`, with each
  of the four failures carrying rule 7's `is in no git checkout` refusal.
  Red when: the arms run outside a checkout again, as at `7e8456181`, or the settings value rises
  above `4`, which fails the two stub-4 arms through rule 7 (measured with `5`: `3 passed, 2 failed`).
  figure: 5 and 4 are PINNED, the count of the block's arms and its failures at `7e8456181`.
- **AC2** — When `grep -c "rules 6 and 7 add nothing" tools/hooks/agent-cap.test.sh` runs, it prints
  `0`. At `7e8456181` it printed `1`.
  Red when: the comment still says the block's directory lies in no checkout.
- **AC3** — When the `WS_PROBE` block runs, its fifth line reads
  `ok   writer split: no policy kit beside the hooks kit -> deny, against MAX_VERIFIERS (exit 2)`.
  Red when: the arm's expected answer or its needle is edited to fit a new path through rule 7.
- **AC4** — When `git diff --quiet 7e8456181 -- tools/hooks/agent-cap.js` runs, it exits 0.
  Red when: the hook is edited to admit a payload `cwd` in no checkout, which hides the arms' defect.

## 6. Gates

`agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test`

These are the legs whose guard `tools/hooks/agent-cap.test.sh` trips and that are not broad, from
`python tools/check-spec-tokens.py --legs-for tools/hooks/agent-cap.test.sh` at `7e8456181`. The arms
AC1 observes already exist in the `agent-cap self-test` suite, and this unit makes them run as written,
so it adds no suite arm and declares no arm line.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the build run's add row for this unit and its spec brief,
  `memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-68-spec-brief.md`,
  grounded at `7e8456181`. The `WS_PROBE` block was run at that commit, and against a scratch copy
  of the suite carrying §4 "The block", where it printed `probe: 5 passed, 0 failed`. One addition
  to the brief: the checkout line unsets `GIT_DIR` and `GIT_WORK_TREE`, as the suite's own git read
  does.

## 9. Reuse audit

The seam is the rule-7 block of the same suite, which builds `$R7` as a checkout and writes its
settings (`tools/hooks/agent-cap.test.sh:1194-1201`). This unit copies its two setup lines into the
writer-split block and adds no mechanism. `run_limit_call` and `write_limit_stub` are reused
unchanged.
`python tools/codebase-map/reuse_lookup.py "a hook suite arm runs its hook copy inside a scratch git checkout whose settings hold the agent limit"`
ranked name stems only (`git`, `run`, `arm`, `scratch`), and none builds a checkout for a hook suite.
The recall probe returned `TOOL-dGroundRules-18`, whose arms these are, `TOOL-dGroundRules-61`, whose
settings layers the arms now pass, and this build's `RUN.md`, which parked the defect.

Recall terms used: `python tools/memory-recall/query.py "writer split arms run outside a checkout, rule 7 refuses a payload cwd in no checkout" --terms "writer split gov:fixed-writers stub policy-mirror rule 7 checkSettingsInForce no git checkout agent-cap.test.sh R7 settings.json"`
