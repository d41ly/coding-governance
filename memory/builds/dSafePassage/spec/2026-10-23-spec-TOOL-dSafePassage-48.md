# TOOL-dSafePassage-48 — the step contract refuses `sendemail.sendmailCmd` and every send-email executor key in its identity form

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 12 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-48-deviation-94.md](../build/2026-10-23-build-TOOL-dSafePassage-48-deviation-94.md) | deviation | — |
| [2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-47-48-49-50-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-47 TOOL-dSafePassage-50 TOOL-dSafePassage-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 43 to 46
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-43-44-45-46-spec-audit-round1.md`)
confirmed finding **id 10** at HIGH, its item **D-2**. The same defect was found at MEDIUM as id 27,
item D-8. That id is batched by its own id in `TOOL-dSafePassage-49`, which holds this unit's rows to
a derivation in the class arm.

This unit read git 2.54.0.windows.1's shipped `libexec/git-core/git-send-email` on node d,
2026-10-23. Its option table maps `tocmd`, `cccmd` and `headercmd` (`:381-384`) and `sendmailcmd`
(`:394`). It reads every known key under `sendemail.$identity` before the bare section
(`read_config(..., "sendemail.$identity")`, `:541`). It runs `$sendmail_cmd` through
`exec ("sh", "-c", ...)` (`:1787`). `git help --config` lists `sendemail.<identity>.*`, `ccCmd`,
`headerCmd` and `toCmd`, and no `sendmailCmd`. TOOL-dSafePassage-29's table row covers only
`sendemail.ccCmd`, `sendemail.toCmd` and `sendemail.headerCmd`, and its class arm keeps only keys
`git help --config` lists. TOOL-dSafePassage-45 S6 gives the identity form to `sendemail.smtpServer`
alone. So a target config holding `sendemail.sendmailCmd = <cmd>`, or `sendemail.work.ccCmd = <cmd>`,
passes the step contract, and any step that reaches git send-email runs it. This unit is id 10's
promotion: every send-email executor key is refused in both its forms, and the gap in git's own
listing is stated.

## 2. Scope (IN)

- **S1** — The class. Every `sendemail.<key>` row of `STEP_REFUSED_KEYS` (TOOL-dSafePassage-29 S1)
  also matches `sendemail.<x>.<key>`, because git-send-email reads each of its keys under the
  identity first. The rows so widened are `ccCmd`, `toCmd` and `headerCmd`, any value, and
  `smtpServer` under TOOL-dSafePassage-45 S5's absolute-path rule. TOOL-dSafePassage-45 S6 is read
  as this class, never as a single `smtpServer` row. Observed by AC1.
- **S2** — The unlisted key. `STEP_REFUSED_KEYS` gains `sendemail.sendmailCmd` and
  `sendemail.<x>.sendmailCmd`, any value, run by `send-email` through `sh -c`. The row's reason
  names git-send-email's option table, since `git help --config` does not list the key. Observed by
  AC1.
- **S3** — The plant. The `isolation` family of `python3 "tools/govkit/upgrade_steps.py" fixture`
  gains `sendemail-identity-cmd`: a target whose `.git/config` sets `sendemail.identity = work` and
  `sendemail.work.ccCmd` to a canary command. The step is refused before any spawn, naming the key
  and `.git/config`. Observed by AC2.
- **S4** — The texts. TOOL-dSafePassage-45 §7 "What the check does not cover" is read with this
  sentence beside it: `git help --config` does not list every key git's own scripts read, and
  `sendemail.sendmailCmd` is the one this build found and refuses by its own row. The "What a step
  can reach" section of `help/upgrade-steps.md` names `sendemail.sendmailCmd` and the identity form
  among the refused send-email keys. TOOL-dSafePassage-45's §3 hands-off bullet to this unit names
  the reading. Observed by AC3.

## 3. Non-goals (OUT)

- Holding the identity forms to a derivation in TOOL-dSafePassage-29's class arm: finding 27, item
  D-8, batched in `TOOL-dSafePassage-49`.
- Parsing git-send-email's option table at run time. The script is absent where git's email package
  is not installed, so a table read from it would grade nothing there.
- Send-email keys that run nothing, such as `sendemail.to` or `sendemail.smtpUser`.

### Edges

- **consumes-from** `TOOL-dSafePassage-29` — `STEP_REFUSED_KEYS` and its `sendemail.ccCmd`, `toCmd` and `headerCmd` row, which S1 widens and S2 extends; without them there is no table to hold the rows
- **consumes-from** `TOOL-dSafePassage-45` — S5's absolute-path rule and S6's identity form of `sendemail.smtpServer`, which S1 states as a class, and §7's uncovered sentence, which S4 reads
- **hands-off** `TOOL-dSafePassage-49` — the class arm widening each kept `sendemail.<key>` to its identity form and keeping `sendemail.sendmailCmd`, so a row S1 or S2 adds cannot be dropped unseen, finding 27 of the spec audit of units 43 to 46
- **hands-off** `TOOL-dSafePassage-51` — the smtpServer row's pin read as `:1782-1790`, AC3 read through that unit's one section probe, and the `sendemail.sendmailCmd` row the guard's selftest literal holds to, findings 12, 8 and 14 of the spec audit of units 47 to 50

## 4. Design

### Data model

The send-email rows of `STEP_REFUSED_KEYS` after this unit:

| Pattern | Value rule | What runs it |
|---|---|---|
| `sendemail.ccCmd`, `sendemail.<x>.ccCmd` | any | `send-email` (`git-send-email:383`) |
| `sendemail.toCmd`, `sendemail.<x>.toCmd` | any | `send-email` (`:381`) |
| `sendemail.headerCmd`, `sendemail.<x>.headerCmd` | any | `send-email` (`:384`) |
| `sendemail.sendmailCmd`, `sendemail.<x>.sendmailCmd` | any | `send-email`, through `sh -c` (`:394`, `:1787`) |
| `sendemail.smtpServer`, `sendemail.<x>.smtpServer` | an absolute path (TOOL-dSafePassage-45 S5) | `send-email` (`:1782-1789`) |

The identity form is read case-insensitively in its key name, as git prints it: `git config --list`
prints `sendemail.work.cccmd`. Line numbers are those of git 2.54.0.windows.1's
`libexec/git-core/git-send-email` on node d, read 2026-10-23 (PINNED).

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the rows of §4 "Data model" not in TOOL-dSafePassage-29's
table, and the plant `sendemail-identity-cmd`. No function, conf key, gate leg or policy key. The
refusal is TOOL-dSafePassage-24's one `raise Refusal` site, so `tools/govkit/refusal_join.py`'s
`BRANCH_PIN` does not move.

### Migration

None: no step row spawns before this build's walk lands.

### Rollout

Live at landing. It builds at order 12, one above TOOL-dSafePassage-45 (order 11), whose S6 it
repairs. It shares `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py` with
`TOOL-dSafePassage-47` at order 12, so the build run sequences the two passes by M6's first clause.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **One `<x>` row per key, typed beside each bare row.** The shape S6 had; the next send-email row
  would be added without its identity form, which is this finding. S1 states the class once.
- **Refusing every `sendemail.<x>.*` key.** `sendemail.<x>.to` and `sendemail.<x>.from` run nothing,
  and a target that configures an identity would be refused for addresses.

## 5. Production-readiness checklist

- security: closes a step-contract bypass through `sendemail.sendmailCmd` and the identity forms of
  the three `Cmd` keys.
- perf / scale: four more table rows.
- error / empty / loading states: unchanged; the refusal names each key and its file.
- observability: the refusal prints the key as git prints it.
- risks: a target whose own `.git/config` sends patches through `sendmailCmd` is refused; the same
  key in the user's global config is not a `local` or `worktree` row, so the check does not read it.
- testing: the probe of AC1 and the plant of AC2, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md`, S4.

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path, `STEP_REFUSED_KEYS`
  refuses `sendemail.sendmailcmd` and `sendemail.work.sendmailcmd` valued `x`,
  `sendemail.work.cccmd`, `sendemail.work.tocmd` and `sendemail.work.headercmd` valued `x`, and
  `sendemail.work.smtpserver` valued `/usr/bin/x`; it does not refuse `sendemail.work.to` valued
  `a@example.com` or `sendemail.work.smtpserver` valued `smtp.example.com`.
  Red when: an identity form or `sendmailCmd` passes, or a key that runs nothing is refused.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant sendemail-identity-cmd`
  runs, the step is refused before any spawn, naming `sendemail.work.cccmd` and `.git/config`, the
  canary is absent, and the run exits 1.
  Red when: the identity-form key passes and the step spawns.
- **AC3** — When `awk '/^#+ What a step can reach/{f=1;next} /^#+ /{f=0} f' help/upgrade-steps.md`
  runs, its output holds a line naming `sendemail.sendmailCmd` and a line naming the identity form.
  Red when: the section lists the send-email keys without either.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC2 · the self-test runs the eight key cases of AC1 and the `sendemail-identity-cmd` plant, its failing cases staged by a table copy without the `sendemail.<x>.ccCmd` form and by one without the `sendmailCmd` row · none

What the check does not cover: a key git's own scripts read that `git help --config` does not list
and this build has not found, beyond `sendemail.sendmailCmd`.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the promotion of the spec audit of units 43 to 46's id 10
  (HIGH, item D-2).
- rev-2 · 2026-10-23 · §3 · the Edges gain the end this unit owes the promotion `TOOL-dSafePassage-51` of the spec audit of units 47 to 50, written by the disposal stage; no other section moved.

## 10. Reuse audit

The seam extended is TOOL-dSafePassage-29's `STEP_REFUSED_KEYS`, with TOOL-dSafePassage-45 S5's value
rule, specced and unbuilt at the base. `python tools/codebase-map/reuse_lookup.py "refuse a config key under a send-email identity"`
ranked `key`, `keys`, `read_conf_key` and `CensusRefused`, name-token matches; none reads git
config keys, so no existing seam fits beyond that table. The key set was read from the shipped
`git-send-email` on node d, not from a record.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit finding on a submodule walk or a refused executor key is promoted and its reading carried to the faulted unit" --terms "spec audit promoted reading hands-off submodule walk repository shape refused executor sendemail identity"`
