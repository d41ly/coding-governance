# TOOL-dRankedPlan-9 — the ratification predicate: the session's owner-origin intake read as the plan's ratification by `plan.ratification`

**Status:** DEFERRED · rev-3 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 3 · advances TOOL-dRankedPlan-17

**Carries:** cl-dClosedLoop-0377@a78b3ac9 whole
**Carries:** node:policy-key.plan.ratification

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-1-repin-return.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-repin-return.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 |
| [2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-reuse-scout-b.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-10 TOOL-dRankedPlan-15 |
| [2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dRankedPlan-1-spec-stage-returns.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-build-TOOL-dRankedPlan-9-deviation-91.md](../build/2026-10-26-build-TOOL-dRankedPlan-9-deviation-91.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-9-deviation-92.md](../build/2026-10-27-build-TOOL-dRankedPlan-9-deviation-92.md) | deviation | — |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-repin-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-repin-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 |
| [2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dRankedPlan-1-spec-brief.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 |
| [2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md) | spec-audit | TOOL-dRankedPlan-16 TOOL-dRankedPlan-1 TOOL-dRankedPlan-10 TOOL-dRankedPlan-2 TOOL-dRankedPlan-14 TOOL-dRankedPlan-13 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-15 TOOL-dRankedPlan-6 TOOL-dRankedPlan-8 TOOL-dRankedPlan-7 |

<!-- /gen:spec-records -->

## 1. Goal

A prompt yields a one-build brief and never a plan, and nothing says when a plan is the owner's
(gap-plan-03). The owner ruled that "starting a session and requesting a build _is_ ratification",
with hook-recorded keywords, a terminal command or a signed commit as owner-adjustable options (FR-1,
flow-roles.md:173-199). This unit lands the one predicate every Plan reader asks,
`read_plan_ratification`, which reads `plan.ratification` and answers from the session's intake log:
only an intake the owner typed in this session counts, never one relayed to it. dWellOiledMachine's
`entry.intake` prompt-submit hook writes that log (PM-9); until it lands, dPlacedRequest's typed
request record stands in, and every witness says so.

## 2. Scope (IN)

- **S1** — The predicate, I6. `read_plan_ratification(slug, root=".", why=None) -> (value, witness)` in
  the new module `tools/loop/ratify.py`. `value` is `plan.ratification`, read once through the policy
  reader, `resolve("plan.ratification", root)` (`tools/policy/policy.py:752`); `witness` is the line
  naming the evidence that ratifies the build's plan, or `None` when nothing does, the reason then
  appended to `why` when a list is given, as `render_handoff` appends its notes. A refused policy read
  raises, so no reader takes a refusal for a value. The CLI `python tools/loop/ratify.py <slug>` prints
  `ratified — <value> · <witness>` and exits 0, `unratified — <value> · <why>` and exits 1, and exits 2
  printing the refusal on a refused read or a malformed slug. Observed by AC1 to AC6.
- **S2** — `request`, the default. The build's request is the `content-key` of its claim, read by
  `read_claim_body` on `refs/gov/claims/<slug>` (TOOL-dPlacedRequest-21 S2,
  `tools/loop/claim.py`). The plan is ratified when `bash tools/unattended/unattended.sh
  --request-consent <key>` (TOOL-dPlacedRequest-5 S3) exits 0: the session typed that request here,
  its `.typed` line bound to the stored bytes (TOOL-dPlacedRequest-19 S5, TOOL-dPlacedRequest-31 S2).
  Witness `request <key> · typed in this session · log stand-in`. Exit 1 is unratified with the verb's
  own line, `relayed: data with provenance, never consent` or `no session`; no claim is unratified
  `no claim names a request for <slug>`. Observed by AC1 and AC2.
- **S3** — `hook-keyword`. The plan is ratified when the session's intake log holds a request whose
  text, stripped, is exactly `ratify <slug>`, `RATIFY_KEYWORD` being `ratify`, and `--request-consent`
  exits 0 for its key: the log is `<git-common-dir>/requests/<key>.md` (TOOL-dPlacedRequest-19 S2),
  each file's stem its key. Witness `hook-keyword <key> · ratify <slug> · log stand-in`. Observed by AC3.
- **S4** — `terminal-command`. The plan is ratified when the build's `build/` folder holds a
  disposition record (TOOL-dDeclaredLoop-16 S4) whose `Item` is `item.plan.exit` and whose `Channel` is
  `terminal`, read by the record factory's `read_record` (PLAY-dOrderedCharter-7 S7) and admitted by
  `check_disposition_record` (TOOL-dDeclaredLoop-16 S5). Witness `terminal-command <record path>`.
  Observed by AC4.
- **S5** — `signed-commit`. The plan is ratified when the newest commit that touched the build's plan
  record, the file `find_plan_record` returns (TOOL-dRankedPlan-16 S4), passes `git verify-commit`,
  whose trust is the repository's configured signers. Witness `signed-commit <sha8>`; no plan record,
  or a commit git does not verify, is unratified with the first line git printed. Observed by AC5.
- **S6** — The stand-in and its hand-over. `INTAKE_STAND_IN` in `ratify.py` names the log the `request`
  and `hook-keyword` arms read, `requests/<key>.md` and its `.typed` line, and the build that replaces
  it, dWellOiledMachine, whose `entry.intake` hook writes the session's intake log; each of those
  witnesses ends `log stand-in` while it stands. Both arms reach the log only through
  `--request-consent` and the `requests/` file names, so the hand-over re-points that one verb and
  touches no reader here. Observed by AC1 and AC3.
- **S7** — The fixture. `python tools/loop/ratify.py --fixture [--plant <case>]` builds a scratch
  repository under a short `%TEMP%` path with a build, a claim ref, a request record and a policy file
  committed on its default branch, one plant per case of §4 "The plants", and asserts each answer;
  `tools/loop/selftest.py` runs it, so the `loop selftest` leg grades it. Observed by AC1 to AC5.
- **S8** — The key's catalogue row gains its `summary` and `usage` in `tools/policy/catalogue.toml`
  (:531-534), and `python tools/policy/policy.py lists --write` drains it from
  `tools/policy/unsummarised-keys.txt`. Observed by AC7.
- **S9** — The docs: `help/plan.md` gains a section "Ratification" naming the four values, what each
  counts, the `log stand-in` mark and `ratify.py <slug>`; `tools/loop/README.md` names the module.
  Observed by AC8.

## 3. Non-goals (OUT)

- The prompt-submit hook, the intake record kind and the harness adapters: dWellOiledMachine's (PM-9).
- Plan's exit, the fallback to the owner gate under `request` while the intake is not installed, and
  its witness `intake not installed`: TOOL-dRankedPlan-10's, which wraps this predicate.
- Who may draft or reorder the plan: TOOL-dRankedPlan-2's. The triage batch: TOOL-dRankedPlan-3's.
- The request record, its content key, its `.typed` line and the consent verb: dPlacedRequest's,
  called here and never re-specced.
- The disposition record and the owner gate: dDeclaredLoop's.
- Choosing whose key may sign: `git verify-commit` reads the repository's signer configuration.

### Edges

- **consumes-from** `TOOL-dRankedPlan-16` — `record-kind.plan`, whose one record per build `find_plan_record` returns and whose newest commit `signed-commit` verifies
- **hands-off** `TOOL-dRankedPlan-10` — `read_plan_ratification`, the predicate Plan's exit asks once and wraps in its fallback under `request`
- **hands-off** `TOOL-dRankedPlan-2` — `read_plan_ratification`, whose witness marks the plan rows the owner has ratified
- **hands-off** `TOOL-dRankedPlan-3` — `read_plan_ratification`, the witness a held `owner-batches` batch needs before it is written
- **hands-off** `TOOL-dRankedPlan-15` — `read_plan_ratification`, which says whether a plan revision was ratified as the plan is
- **hands-off** `TOOL-dRankedPlan-5` — `read_plan_ratification`, the witness a live-build mapping record needs before it is written
- **consumes-from** external — dPlacedRequest: `read_claim_body` (TOOL-dPlacedRequest-21 S2), `--request-consent` (TOOL-dPlacedRequest-5 S3), the request files (TOOL-dPlacedRequest-19 S2, S5; TOOL-dPlacedRequest-31 S2)
- **consumes-from** external — dDeclaredLoop and dOrderedCharter: the disposition record and `check_disposition_record` (TOOL-dDeclaredLoop-16 S4, S5), the factory's `read_record` (PLAY-dOrderedCharter-7 S7)
- **consumes-from** external — dGroundRules: the policy reader `resolve` and `plan.ratification`'s catalogue row
- **hands-off** `TOOL-dRankedPlan-22` — `read_plan_ratification` and its CLI form, whose callers that unit bounds to the act they ratify (round-1 spec audit, id 37)
- **hands-off** `TOOL-dRankedPlan-24` — the `terminal-command` arm and `ratify.py --fixture`, which that unit re-points to the bounded `read_item_disposition` (round-1 spec audit, id 21)
- **hands-off** `TOOL-dRankedPlan-26` — the `terminal-command` arm, which that unit holds on a disposition of `ask` or `none` (round-1 spec audit, id 39)
- **hands-off** `TOOL-dRankedPlan-29` — `read_plan_ratification`'s policy read and its fixture, which that unit's S14 corrects (round-1 spec audit, id 16)
- **hands-off** `TOOL-dRankedPlan-33` — S7's `ratify.py --fixture`, whose base that unit seeds with a memory-tree kit and a witnessed plan record (spec audit of units 19 to 29, id 21)

## 4. Design

### Evidence

- `plan.ratification`'s row is in the catalogue at base (`tools/policy/catalogue.toml:531-534`), its
  values `request`, `hook-keyword`, `terminal-command`, `signed-commit`, default `request`, owner
  dRankedPlan, and no code reads it.
- No prompt-submit hook exists: `.claude/settings.json` registers no `UserPromptSubmit`, and no file
  under `tools/` or `skills/` names one (scout B, verified at base by `git grep`).
- The policy kit's reader coverage counts a key as read only by a call whose first argument is the key
  in quotes (`help/policy.md:132-137`), so S1 spells `resolve("plan.ratification", root)`.
- The consent predicate refuses a session that only received a key: "a relayed request is data with
  provenance and never consent" (TOOL-dPlacedRequest-19 S5), the rule FR-1's "never relayed by an
  agent" asks for.

### The answers

| Value | Ratified when | Witness |
|---|---|---|
| `request` | the claim's request was typed in this session | `request <key> · typed in this session · log stand-in` |
| `hook-keyword` | a typed request reads `ratify <slug>` | `hook-keyword <key> · ratify <slug> · log stand-in` |
| `terminal-command` | a disposition record for `item.plan.exit` on the `terminal` channel | `terminal-command <path>` |
| `signed-commit` | the plan record's newest commit verifies | `signed-commit <sha8>` |

### The plants

| Plant | Policy value | Planted | Expected |
|---|---|---|---|
| `request-typed` | `request` | claim, request, `.typed` line for the session | ratified |
| `request-relayed` | `request` | claim and request, no `.typed` line | unratified, `relayed` |
| `hook-keyword` | `hook-keyword` | a typed request `ratify tFix`; a typed `ratify tOther` | ratified for `tFix` only |
| `terminal-command` | `terminal-command` | a disposition record, `Channel` `terminal`; a second plant with `mailbox` | ratified; unratified |
| `signed-commit` | `signed-commit` | the plan record committed signed by an ssh key the fixture configures as a signer; then an unsigned commit to it | ratified; unratified |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/loop/ratify.py` | module | none |
| `read_plan_ratification` | function | `py.function`, asked at the pass |
| `RATIFY_KEYWORD`, `INTAKE_STAND_IN` | constants | none declared |
| `--fixture`, `--plant` | flags of `ratify.py` | none |
| the five plants of §4 | fixture cases | none |

### Migration

None. No reader asks the predicate before units 2, 3, 10 and 15 land.

### Rollout

Live at landing, read by nothing until its readers land.

### Files touched (estimate)

- `tools/loop/ratify.py` (new): S1 to S7
- `tools/loop/selftest.py`: S7's call
- `tools/loop/README.md`: S9's paragraph
- `tools/policy/catalogue.toml`, `tools/policy/unsummarised-keys.txt`: S8
- `help/plan.md`: S9's section

### Alternatives rejected

- **The transcript's owner classifier** (`_derive_owner_class`, `tools/runlog/extract.py:587`). It reads
  a session after the fact, from a transcript format that is no contract (§8 F1).
- **A refused policy read taken as `request`.** A ratification is a mandate; a read that cannot say
  which rule holds grants none.

## 5. Production-readiness checklist

- security — the predicate grants the mandate every unattended step after Plan runs under, so it
  denies by default: a refused read raises, and every arm answers unratified on a missing record. Until
  dWellOiledMachine's hook lands, the `.typed` line is written by `--request` on its caller's word, so
  an agent in the typing session could record words the owner never typed (TOOL-dPlacedRequest-19 §3);
  the `log stand-in` mark carries that limit into every witness, and deviation 91 records it.
- perf / scale — one policy read and at most one consent call per typed request in the session's log.
- error / empty / loading states — each unratified answer names its reason; no claim, no record and no
  plan record each have one.
- observability — the CLI's one line, and the `why` list for callers.
- risks — `terminal-command` takes the record's `Channel` as written; the factory records the channel
  its caller names.
- testing — the five plants, red and green.
- migration — none.
- user docs — `help/plan.md`, S9.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant request-typed` runs, `ratify.py tFix` prints
  `ratified — request · request <key> · typed in this session · log stand-in` and exits 0.
  Red when: the typed request is not read as the ratification, or the witness hides the stand-in.
- **AC2** — When the plant `request-relayed` runs, `ratify.py tFix` prints `unratified — request ·` and
  the consent verb's `relayed` line, and exits 1.
  Red when: a request this session did not type ratifies the plan.
- **AC3** — When the plant `hook-keyword` runs, `ratify.py tFix` prints `ratified — hook-keyword ·
  hook-keyword <key> · ratify tFix · log stand-in`, and `ratify.py tOther` under a policy naming the
  same value but with its request untyped exits 1.
  Red when: a keyword for another build, or one not typed here, ratifies.
- **AC4** — When the plant `terminal-command` runs, `ratify.py tFix` prints `ratified — terminal-command
  · terminal-command <path>` for the `terminal` record and exits 1 for the `mailbox` one.
  Red when: a disposition on another channel ratifies under `terminal-command`.
- **AC5** — When the plant `signed-commit` runs, `ratify.py tFix` prints `ratified — signed-commit ·
  signed-commit <sha8>` over the signed commit, and exits 1 once an unsigned commit touches the plan
  record.
  Red when: an unsigned newest commit ratifies.
  fixture: `ssh-keygen` on PATH, which Git for Windows ships; without it the plant exits 2 naming it.
- **AC6** — When `ratify.py tFix` runs in a fixture whose committed policy file sets
  `plan.ratification = "email"`, it exits 2 printing the reader's refusal and no `ratified` line.
  Red when: a refused read answers as a value.
- **AC7** — When `python tools/policy/policy.py get plan.ratification` runs in a repository whose
  policy file sets no value, it prints `request`, and after `policy.py lists --write` the unsummarised
  list no longer names `plan.ratification`.
  Red when: the row is missing or still unsummarised.
- **AC8** — When `grep -n "## Ratification" plan.md` runs over the help page, it finds S9's section
  naming `request`, `hook-keyword`, `terminal-command`, `signed-commit` and `log stand-in`.
  Red when: the page does not describe the predicate.

## 7. Gates

`memory hygiene` · `policy check` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 · `ratify.py --fixture`'s five plants and the refused read, run from the loop selftest, staged by a `request` arm that ratifies on the claim alone · none

## 8. Open questions

- **F1 — What stands in for the intake log until the hook lands?** Options: (a) dPlacedRequest's request
  record, `requests/<key>.md` with its `.typed` line, asked through `--request-consent`; (b) the run-log
  kit's transcript classifier, `_derive_owner_class` (`tools/runlog/extract.py:587`), which marks a
  turn typed, queued or an interrupt. (b) reads after the fact, from a format the harness does not
  promise. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor and the
  reuse of the consent predicate every request reader already asks. widens: none · relaxes: none
- **F2 — Does a relayed request ratify?** RESOLVED (agent, 2026-10-26, delegated): no, rung 1: FR-1
  says the ratification is "witnessed, never relayed by an agent", and the clause counts "its
  owner-origin intake alone". widens: none · relaxes: none
- **F3 — Where is the stand-in declared?** Options: (a) a `[[stand-in]]` row in `tools/loop/loop.toml`,
  as I7 proposed; (b) a constant in `ratify.py` and the `log stand-in` mark on every witness it shapes.
  TOOL-dDeclaredLoop-13 S8 reds a stand-in row naming no row item, and `item.entry.intake` has no
  `[[item]]` row, being outside the five programs (TOOL-dDeclaredLoop-12 §3), and is in none of the
  move rows B1 to B20 (TOOL-dDeclaredLoop-13 §4). RESOLVED (agent, 2026-10-26, delegated): (b), rung 1, the
  parent's own rule; KICK-dKeptSession-17 §4 took the same course for an interaction that is not a row
  item. The departure from I7's spelling is deviation record 91. widens: none · relaxes: none
- **F4 — What counts under the three other values?** FR-1 names them, "hook-recorded keywords", "a
  terminal command", "a signed commit", and no record gives their mechanism. Options per value were a
  typed `ratify <slug>` against any typed request; a disposition record on the `terminal` channel
  against a new verb; the plan record's newest commit against any signed commit on the branch.
  RESOLVED (agent, 2026-10-26, delegated): S3 to S5 as written, rung 3: each reuses a record a parent
  already writes, the disposition record's `Channel` set (TOOL-dDeclaredLoop-16 S4) and git's own
  verification, and each binds the evidence to this build. widens: none · relaxes: none
- **F5 — What does a refused policy read answer?** Options: (a) raise, and the CLI exits 2; (b) take the
  catalogue default `request`. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3: the charter's
  `[security]` rule denies by default, and a ratification is the mandate for every later step.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 9, the brief's I6 and I7, scout B's row -9,
  FR-1, v2:401 and v2:1224, and TOOL-dPlacedRequest-5, -19, -21 and -31.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-22`, the hands-off edge to `TOOL-dRankedPlan-24`, the hands-off edge to `TOOL-dRankedPlan-26`, the hands-off edge to `TOOL-dRankedPlan-29`, each the reciprocal of that promoted unit's own edge (round-1 spec audit, `reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`); no other section moves.
- rev-3 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-33`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are dPlacedRequest's consent predicate, through the read-only verb
`--request-consent` (TOOL-dPlacedRequest-5 S3) over the request files (TOOL-dPlacedRequest-19 S2, S5),
its claim reader `read_claim_body` (TOOL-dPlacedRequest-21 S2), dDeclaredLoop's disposition record and
`check_disposition_record` (TOOL-dDeclaredLoop-16 S4, S5), TOOL-dRankedPlan-16's `find_plan_record`, and
the policy reader `resolve` (`tools/policy/policy.py:752`). `python tools/codebase-map/reuse_lookup.py
"decide whether a plan is ratified by the owner from a typed request record"` ranked name stems
(`records`, `plan`, `read_records`, `plan_state`); none reads a ratification, so no existing seam fits
the predicate and S1 adds it in the loop kit beside `claim.py`. Scout B's row named
`_derive_owner_class` at `tools/runlog/extract.py:587`, verified at base and rejected in §8 F1; it
proposed a `[[stand-in]]` row, which TOOL-dDeclaredLoop-13 S8's rule refuses here (§8 F3). The recall
query returned scout B's row, the brief's I6 and I7, and TOOL-dPlacedRequest-19's brief row.

Recall terms used: `python tools/memory-recall/query.py "how is a build plan ratified by the owner's typed request and never by a relayed one" --terms "plan.ratification request hook-keyword terminal-command signed-commit intake typed relayed consent entry.intake owner-origin"`
