# TOOL-dSafePassage-37 — the refused-key predicate keeps every key named as a hook, and the step environment closes the `ext::` transport by one command-scope pair

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-37-deviation-83.md](../build/2026-10-23-build-TOOL-dSafePassage-37-deviation-83.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-26-prompt-TOOL-dSafePassage-37-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-37-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-36 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-38 TOOL-dSafePassage-42 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 27 to 35
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md`)
confirmed finding **id 28** at HIGH, its item **D-2**, whose fix the skeptic REJECTED and corrected.
TOOL-dSafePassage-29's predicate keeps a key of `git help --config` only when its last segment is in a
typed list, and two executor routes pass it. First, `gc.recentObjectsHook`: this unit's probe on node
d, git 2.54.0.windows.1, 2026-10-23, set it in a scratch repository's config to a shell line writing a
canary, and `git gc --cruft --prune=now` spawned that line through `sh.exe -c` (`GIT_TRACE`) and wrote
the canary; auto-gc reaches `gc` from a step's `git commit`. Second, the `ext::` transport: with a local
`protocol.allow = always` and a remote URL `ext::sh -c touch% canary`, a plain `git fetch` wrote the
canary. With `GIT_CONFIG_COUNT=1` carrying `protocol.ext.allow = never`, the same fetch printed
`fatal: transport 'ext' not allowed` and wrote nothing, and so did a fetch whose `https` URL a local
`url.<ext::…>.insteadOf` rewrote. TOOL-dSafePassage-29 §5 claims deny by default over "the whole class
git documents". This unit is id 28's promotion, built from the skeptic's corrected fix: the predicate
keeps every key whose last segment ends in `hook`, and the `ext::` route is closed by the step
environment rather than by value rules on the keys that can reach it.

## 2. Scope (IN)

- **S1** — The predicate. TOOL-dSafePassage-29 §4 "The predicate" also keeps a key whose last segment,
  lowercased, ends in `hook`. Over git 2.54.0.windows.1's 1006-line listing on node d, 2026-10-23,
  this adds `advice.ignoredHook`, `gc.recentObjectsHook` and `uploadpack.packObjectsHook`, and the
  kept set moves from 43 keys to 46 (PINNED that date); `core.fsmonitorHookVersion` ends in `version`
  and is not kept. Observed by AC3.
- **S2** — The rows. `STEP_REFUSED_KEYS` gains `gc.recentObjectsHook`, any value, run by `gc` and by
  the auto-gc a commit or fetch starts. `STEP_UNREFUSED_KEYS` gains `advice.ignoredHook`, a boolean
  that runs nothing, and `uploadpack.packObjectsHook`, which git honours only from protected config,
  the system, global and command scopes (git 2.54.0's shipped `git-config.html`, read 2026-10-23),
  and which `build_step_env` sets in none of them. Observed by AC1 and AC3.
- **S3** — The transport, closed structurally. `build_step_env` (TOOL-dSafePassage-7 §4) adds a third
  command-scope pair, `GIT_CONFIG_KEY_2` = `protocol.ext.allow` and `GIT_CONFIG_VALUE_2` = `never`, and
  `GIT_CONFIG_COUNT` reads 3. The command scope outranks the local one, and `protocol.<name>.allow`
  outranks `protocol.allow`, so a local `protocol.allow`, `protocol.ext.allow`, `url.<base>.insteadOf`,
  `url.<base>.pushInsteadOf` or `remote.<x>.url = ext::…` all meet git's own refusal inside the step.
  No row of the refused table is added for those keys. TOOL-dSafePassage-26 S13's carried
  `core.autocrlf` and `core.eol` pairs take the indices after this one. Observed by AC2.
- **S4** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `local-recent-objects-hook`, whose fixture step makes an unreachable object and runs
  `git gc --prune=now`, with a `-stub` twin that skips the refusal inside the fixture process only;
  and `local-ext-transport`, whose target config sets `protocol.allow = always` and a remote whose
  URL is `ext::` writing a canary, and whose fixture step runs `git fetch`, with a `-stub` twin that
  spawns the step under an environment copy lacking the S3 pair. Observed by AC1 and AC2.
- **S5** — The texts. TOOL-dSafePassage-29 §5's "deny by default over the whole class git documents"
  is read as "over the class the predicate names", and its §7 "What the check does not cover" is read
  with this unit's §7 list of the executors the predicate reaches by no suffix. The "What a step can
  reach" section of `help/upgrade-steps.md` names `gc.recentObjectsHook` among the refused keys and
  says a step can never use the `ext::` transport. Observed by AC4.

## 3. Non-goals (OUT)

- `imap.tunnel`, `instaweb.httpd` and `sendemail.smtpServer`, the keys whose last segments the
  predicate does not name: finding 9, carried by the minors batch `TOOL-dSafePassage-42`.
- Credential-bearing keys and values: finding 30, `TOOL-dSafePassage-38`.
- Value rules for `protocol.*` and `url.*` keys. The command-scope pair answers every route to the
  transport at once, and a rule per key would miss the next key that can name a URL.

### Edges

- **consumes-from** `TOOL-dSafePassage-29` — `STEP_REFUSED_KEYS`, `STEP_UNREFUSED_KEYS`, the predicate and its class arm; without them there is no class to widen
- **consumes-from** `TOOL-dSafePassage-7` — `build_step_env` and its command-scope pairs; without it there is no step environment to carry the transport refusal
- **hands-off** `TOOL-dSafePassage-42` — the predicate's three further last-segment names and their rows, finding 9, which that batch adds to this unit's predicate
- **hands-off** `TOOL-dSafePassage-45` — S3 and AC2 read with `GIT_CONFIG_COUNT` equal to the pairs present, `protocol.ext.allow` found at index 2 and TOOL-dSafePassage-26 S13's pairs after it, this unit's pass editing TOOL-dSafePassage-7's isolation arm and naming the pair in the help page; and AC1 read with `gc.recentobjectshook` as git prints it; findings 1, 7, 14, 24 and 8 of the spec audit of units 36 to 42

## 4. Design

### Data model

The refused row this unit adds, in TOOL-dSafePassage-29 §4's shape:

| Pattern | Value rule | What runs it |
|---|---|---|
| `gc.recentObjectsHook` | any | `gc`, `repack --cruft`, and the auto-gc of `commit` and `fetch` |

The unrefused rows it adds:

| Key | Why it is not refused |
|---|---|
| `advice.ignoredHook` | a boolean advice switch; it runs nothing |
| `uploadpack.packObjectsHook` | honoured only from protected config, which the step environment does not set |

The step environment's pairs after this unit:

| Pair | Key | Value |
|---|---|---|
| 0 | `core.hooksPath` | an empty scratch directory (TOOL-dSafePassage-7) |
| 1 | `credential.helper` | the empty string (TOOL-dSafePassage-7) |
| 2 | `protocol.ext.allow` | `never` |

### Inventory

Minted: the plants `local-recent-objects-hook`, `local-ext-transport` and their two `-stub` twins. No
function, conf key, gate leg or policy key. `gc.recentObjectsHook`'s refusal is TOOL-dSafePassage-24's
one `raise Refusal` site, and the transport is refused by git, so `tools/govkit/refusal_join.py`'s
`BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 5, after TOOL-dSafePassage-29 (order 4), whose predicate and
tables it widens. It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with
`TOOL-dSafePassage-36` and other units at order 5, so the build run sequences those passes by M6's
disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The finder's fix, refusing `protocol.allow` and `url.<base>.insteadOf` by value.** The skeptic
  rejected it: `remote.<x>.url = ext::…` and `pushInsteadOf` reach the transport too, and a value rule
  per key misses the next one.
- **Refusing every key the suffix keeps.** `advice.ignoredHook` runs nothing, so refusing it would stop
  an adopter whose config silences an advice.

## 5. Production-readiness checklist

- security: the predicate's class grows by the hook-named keys, and one command-scope pair closes a
  transport no row could cover whole.
- perf / scale: one more environment pair per spawn.
- error / empty / loading states: a step that needs an `ext::` remote fails inside the step with git's
  own refusal line, which the walk records as the up's failure.
- observability: git names the transport in its refusal; the check names `gc.recentObjectsHook` and
  its file.
- risks: an adopter whose step legitimately fetches over `ext::` cannot run it; no shipped step does.
- testing: the two plants and the class arm, through §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-recent-objects-hook`
  runs, the step is refused before any spawn naming `gc.recentObjectsHook` and `.git/config`, the
  canary is absent, and the run exits 1; `--plant local-recent-objects-hook-stub` lets the step's
  `git gc --prune=now` run the hook and exits 1 naming the canary.
  Red when: the predicate keeps no hook-named key but `core.hooksPath` and `hook.<x>.command`, and a
  step's gc runs the target's hook.
- **AC2** — When the same family runs with `--plant local-ext-transport`, the step spawns, its
  `git fetch` exits non-zero with `transport 'ext' not allowed` on stderr, the canary is absent, and
  the run exits 1 with the up's failure; `--plant local-ext-transport-stub` writes the canary; and a
  `python -c` probe of `build_step_env` prints `GIT_CONFIG_COUNT` as `3` with the pair
  `protocol.ext.allow` and `never`.
  Red when: a local `protocol.allow = always` lets an `ext::` remote run its command inside a step.
- **AC3** — When `git help --config` runs on node d and the predicate is applied in a `python -c` probe
  beside the two tables, the kept set holds `gc.recentObjectsHook`, `advice.ignoredHook` and
  `uploadpack.packObjectsHook`, every kept key matches one row, and with the `gc.recentObjectsHook` row
  taken out of a copy of the refused table the probe names it.
  Red when: a hook-named key is kept by neither table, or the suffix is not applied and the three keys
  are never kept.
  figure: the kept count is DERIVED at observation; 46 was read on 2026-10-23.
- **AC4** — When `git grep -n -e "gc.recentObjectsHook" -e "ext::" -- help/upgrade-steps.md` runs, the
  "What a step can reach" section names the refused hook key and the closed transport.
  Red when: the page still says the refused keys are the whole class git documents.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 · the self-test calls `upgrade_steps.py fixture isolation` with the two plants and runs the class arm with the suffix, its failing cases staged by the `-stub` twins and by a table copy missing the `gc.recentObjectsHook` row · none

What the check does not cover, the executors the predicate reaches by no suffix: `imap.tunnel`,
`instaweb.httpd` and `sendemail.smtpServer` until `TOOL-dSafePassage-42` names them; `pager.<cmd>`, for
TOOL-dSafePassage-29's reason; and the `ext::` transport, which no row grades because S3's pair closes
it for every key that can name it.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 27 to 35's id 28
  (HIGH, item D-2), from the skeptic's corrected fix.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 36 to 42, written by the disposal stage: `TOOL-dSafePassage-45`; no other section moved.

## 10. Reuse audit

The seams extended are TOOL-dSafePassage-29's predicate and tables and TOOL-dSafePassage-7's
`build_step_env` pairs, both specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py
"block the ext transport for a spawned git command"` ranked `git`, `run_git`, `GIT` and
`read_git_output`, generic git spawners, none of which sets a protocol policy, so no existing seam fits
beyond those two specs. The population is git's own: `git help --config`, read on node d with git
2.54.0.windows.1.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's promoted repairs are placed and sequenced after the unit they repair" --terms "spec audit promoted repair unit order edges hands-off consumes-from minors batch disposal rescope"`
