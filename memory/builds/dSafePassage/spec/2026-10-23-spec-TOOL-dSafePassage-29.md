# TOOL-dSafePassage-29 — the step contract's refused keys are the class git's own config list derives, held to it by an arm

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-29-deviation-75.md](../build/2026-10-23-build-TOOL-dSafePassage-29-deviation-75.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-27-28-29-30-31-32-33-34-35-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-30 TOOL-dSafePassage-32 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-33 TOOL-dSafePassage-31 TOOL-dSafePassage-34 TOOL-dSafePassage-35 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 15 to 26
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-15-16-17-18-19-20-21-22-23-24-25-26-spec-audit-round1.md`)
confirmed finding **id 12** at HIGH, its item **D-2**. TOOL-dSafePassage-24 §1 refuses a step when the
target's config declares "any key git runs as a program", while its §4 table lists six instances of
that class. The table omits `gpg.program` with `commit.gpgsign`, `core.editor`, `sequence.editor`,
`core.gitProxy`, `remote.<x>.uploadpack` and `receivepack`, and `submodule.<x>.update=!cmd`. The
report's skeptic ran a canary `gpg.program` under TOOL-dSafePassage-7's environment on a step's
`git commit` (git 2.54.0.windows.1). This unit's own probe on node d, 2026-10-23, found one more: a
`hook.canary.command` with `hook.canary.event = pre-commit` in the repository's config ran on
`git commit` with `core.hooksPath` overridden as TOOL-dSafePassage-7 overrides it. This unit is id
12's promotion. The table becomes the class, derived from git's own list of config keys, and an arm
re-derives that list on every run, so a key git adds later fails the arm instead of passing the
check.

## 2. Scope (IN)

- **S1** — The class, declared. `STEP_REFUSED_KEYS` in `tools/govkit/upgrade_steps.py` is the table
  `check_target_local_config` matches. It holds one row per key pattern, with its value rule and the
  verb that runs it, as §4 "Data model" lists. The table supersedes TOOL-dSafePassage-24's §4 table,
  whose six rows it keeps. Observed by AC1, AC2 and AC3.
- **S2** — The exceptions, declared. `STEP_UNREFUSED_KEYS` beside it holds every executor-shaped key
  the check does not refuse, each with its reason: the seven of §4 "Data model". Observed by AC4.
- **S3** — The class arm. A `tools/govkit/selftest.py` arm runs `git help --config` and keeps every
  key whose last segment, read case-insensitively, is one of the names of §4 "The predicate", or
  ends in `command` or `cmd`. It asserts that each kept key matches a `STEP_REFUSED_KEYS` row or a
  `STEP_UNREFUSED_KEYS` row, and reds naming every key that matches neither. A kept set of zero keys
  reds too, so a `git help --config` that prints nothing is never read as coverage.
  Observed by AC4.
- **S4** — The plants. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `local-gpg` and `local-hook`, each with a `-stub` that skips the refusal inside the fixture
  process only, as TOOL-dSafePassage-24's plants do. Both fixture steps commit what they stage.
  Observed by AC1 and AC2.
- **S5** — The docs. The "What a step can reach" section of `help/upgrade-steps.md`, which
  TOOL-dSafePassage-24 S5 writes, says that the refused keys are every key git runs as a program,
  derived from `git help --config`. It names the seven unrefused keys and why each is not refused.
  Observed by AC5.

## 3. Non-goals (OUT)

- Values that carry a credential rather than run a program, such as a URL with userinfo or an
  `http.<url>.sslKey`: finding 39, carried by the minors batch `TOOL-dSafePassage-35`. The keys
  finding 39 shares with this one, `gpg.program`, `gpg.<fmt>.program`, `core.gitProxy` and the two
  pack programs, are refused here.
- The repositories git enters from the target, a submodule's among them: id 38,
  `TOOL-dSafePassage-30`.
- `merge.<driver>.driver`, which TOOL-dSafePassage-24 §3 leaves uncovered and this unit lists among the
  unrefused keys.

### Edges

- **consumes-from** `TOOL-dSafePassage-24` — `check_target_local_config`, the refusal before a spawn and the isolation plants; without them there is no table to widen
- **hands-off** `TOOL-dSafePassage-35` — the credential-bearing values and the sentence naming every key the check leaves unrefused, which this unit's exception table starts
- **hands-off** `TOOL-dSafePassage-37` — the predicate's keys whose last segment ends in `hook`, `gc.recentObjectsHook` refused, and the `ext::` transport closed by a command-scope pair, the repair of finding 28 of the spec audit of units 27 to 35
- **hands-off** `TOOL-dSafePassage-42` — finding 9 of the spec audit of units 27 to 35, the predicate's names `tunnel`, `httpd` and `smtpserver`, and finding 5, S5's rewrite keeping TOOL-dSafePassage-24 AC5's literals

## 4. Design

### Data model

The refused rows, matched case-insensitively on the key git prints, a `<x>` segment matching any one
or more segments:

| Pattern | Value rule | What runs it |
|---|---|---|
| `filter.<x>.clean`, `filter.<x>.smudge`, `filter.<x>.process` | any | `add`, `checkout`, `status` |
| `core.fsmonitor` | not a git false | an index refresh |
| `diff.external`, `diff.<x>.textconv`, `diff.<x>.command` | any | `diff`, `log -p` |
| `core.sshCommand`, `core.askPass` | any | a fetch or a push |
| `http.extraHeader`, `http.<x>.extraHeader` | any | sent as a credential |
| `credential.<x>` | any | a helper, or a credential setting |
| `gpg.program`, `gpg.<x>.program`, `gpg.ssh.defaultKeyCommand` | any | a signed commit or tag, `log --show-signature`, `verify-commit` |
| `core.editor`, `sequence.editor` | any | `commit`, `tag` or `rebase` without a message |
| `core.gitProxy` | any | a `git://` fetch |
| `remote.<x>.uploadpack`, `remote.<x>.receivepack` | any | a local or ssh fetch or push |
| `core.alternateRefsCommand` | any | a fetch or a push |
| `submodule.<x>.update` | begins with `!` | `submodule update` |
| `hook.<x>.command` | any | the hook event its `hook.<x>.event` names |
| `alias.<x>`, `alias.<x>.command` | begins with `!`, or any for `.command` | `git <alias>` |
| `trailer.<x>.cmd`, `trailer.<x>.command` | any | `commit --trailer`, `interpret-trailers` |
| `difftool.<x>.cmd`, `difftool.<x>.path`, `mergetool.<x>.cmd`, `mergetool.<x>.path` | any | `difftool`, `mergetool` |
| `browser.<x>.cmd`, `browser.<x>.path`, `man.<x>.cmd`, `man.<x>.path`, `guitool.<x>.cmd` | any | `help -w`, `web--browse`, `gui` |
| `sendemail.ccCmd`, `sendemail.toCmd`, `sendemail.headerCmd` | any | `send-email` |

The unrefused rows, `STEP_UNREFUSED_KEYS`:

| Key | Why it is not refused |
|---|---|
| `merge.<driver>.driver` | a step does not merge, and gov's own checkout declares two (TOOL-dSafePassage-24 §3) |
| `core.hooksPath` | TOOL-dSafePassage-7's command-scope pair outranks it, measured in that unit's §4 |
| `core.pager` | git runs a pager only when stdout is a terminal, and a step's output is captured |
| `color.pager`, `column.clean` | a boolean and a layout option; they run nothing |
| `include.path`, `includeIf.<condition>.path` | read by `--includes`, so the included file's own keys are graded |

### The predicate

The arm keeps a key of `git help --config` when its last segment, lowercased, is one of `program`,
`command`, `cmd`, `editor`, `gitproxy`, `uploadpack`, `receivepack`, `driver`, `clean`, `smudge`,
`process`, `textconv`, `external`, `fsmonitor`, `sshcommand`, `askpass`, `helper`, `hookspath`,
`pager`, `path`, `update` or `extraheader`, or ends in `command` or `cmd`. On node d, git
2.54.0.windows.1, 2026-10-23, it kept 43 keys (PINNED): 36 match the refused rows and 7 the
unrefused ones. The arm re-derives the set on every run and states the counts it read.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the constants `STEP_REFUSED_KEYS` and
`STEP_UNREFUSED_KEYS`. Minted plants: `local-gpg`, `local-hook` and their two `-stub` twins. No
function, conf key, gate leg or policy key. The refusal is TOOL-dSafePassage-24's one `raise Refusal`
site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 4, after TOOL-dSafePassage-24 (order 3). It shares
`tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with `TOOL-dSafePassage-30` at the same
order, so the build run sequences the two passes by M6's disjointness rule.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **The report's lesser fix, naming each omitted key in §7 as uncovered.** A step that commits in an
  adopter with `commit.gpgsign` would still run adopter code.
- **A hand table with no arm.** It is the shape the finding faults; the next executor git adds would
  pass the check again.
- **Refusing every key the predicate keeps.** It refuses `core.hooksPath`, which gov's own checkout
  declares, so every gov-first step would refuse.

## 5. Production-readiness checklist

- security: deny by default over the whole class git documents; the exceptions are seven named rows,
  each with its reason.
- perf / scale: the check is unchanged, one `git config` spawn per phase; the arm adds one
  `git help --config` per self-test run.
- error / empty / loading states: a `git help --config` that fails or prints no key reds the arm.
- observability: the refusal names the step, the key and its file, as TOOL-dSafePassage-24 S2 says.
- risks: an adopter with a local `core.editor` or a difftool has every step refused until an
  operator runs it attended; the refusal names the key, and the help page says so.
- testing: the two plants and the class arm, through §7.
- migration: none.
- user docs: `help/upgrade-steps.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-gpg` runs,
  with the scratch target's `.git/config` setting `commit.gpgsign = true` and a canary
  `gpg.program`, the step is refused before any spawn, naming `gpg.program` and `.git/config`, the
  canary is absent, and the run exits 1; `--plant local-gpg-stub` lets the step commit and exits 1
  naming the canary.
  Red when: the step's commit runs the target's signing program.
- **AC2** — When the same family runs with `--plant local-hook`, setting `hook.canary.command` and
  `hook.canary.event = pre-commit`, the step is refused naming `hook.canary.command`;
  `local-hook-stub` exits 1 naming its canary.
  Red when: a config-declared hook runs on a step's commit.
- **AC3** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and matches
  `core.editor`, `sequence.editor`, `core.gitProxy`, `remote.origin.uploadpack`,
  `submodule.sub.update` with value `!sh x` and with value `checkout`, and `alias.x` with value
  `!sh x` against `STEP_REFUSED_KEYS`, every key is refused except `submodule.sub.update = checkout`.
  Red when: a key of the class passes, or a value rule refuses a value git does not run.
- **AC4** — When `git help --config` runs on node d and the arm's predicate is applied in a
  `python -c` probe beside the two tables, every kept key matches one row, the probe prints the kept
  count and the two matched counts, and with the `gpg.program` row taken out of a copy of the table
  it names `gpg.program`.
  Red when: a kept key matches neither table, or the kept set is empty and the probe passes.
  figure: the counts are DERIVED at observation; 43, 36 and 7 were read on 2026-10-23.
- **AC5** — When `git grep -n -e "git help --config" -e "gpg.program" -e "core.hooksPath" -- help/upgrade-steps.md`
  runs, the "What a step can reach" section names the derivation, a refused key and an unrefused one.
  Red when: the page lists instances and never says where the class comes from.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC4 · the self-test calls `upgrade_steps.py fixture isolation` with the two plants and runs the class arm over `git help --config`, its failing cases staged by the `-stub` twins and by a table copy missing one row · none

What the check does not cover: the seven keys of `STEP_UNREFUSED_KEYS`, `pager.<cmd>` for the reason
`core.pager` is not refused, and a key git adds later whose last segment the predicate does not name.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the round-1 spec audit of units 15 to 26's
  id 12 (HIGH, item D-2).
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the spec audit of units 27 to 35, written by the disposal stage: `TOOL-dSafePassage-37`, `TOOL-dSafePassage-42`; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-24's `check_target_local_config` and its table, specced and
unbuilt at the base. `python tools/codebase-map/reuse_lookup.py "refuse a git config key that runs a
program"` ranked `git`, `key`, `run` and `read_conf_key`, name-token matches, and no reader of git's
own config-key list exists in the tree, so no existing seam fits beyond that unit's spec. The
population is git's own: `git help --config`, read on node d with git 2.54.0.windows.1.

Recall terms used: `python tools/memory-recall/query.py "how were spec audit findings promoted into repair units placed beside the unit they repair" --terms "spec audit promoted unit repair blocker high minors batch disposal order edges rescope"`
