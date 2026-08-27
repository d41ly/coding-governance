# DEPL-dCarriedReceipt-10 — role `forked`, report-only

**Status:** CLOSED · rev-7 · 2026-08-25 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-25-build-DEPL-dCarriedReceipt-10-acceptance-ledger.md](../build/2026-08-25-build-DEPL-dCarriedReceipt-10-acceptance-ledger.md) | journal | — |
| [2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md](../reviews/2026-08-24-review-DEPL-dCarriedReceipt-9-spec-precode.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round4.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round5.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md](../reviews/2026-08-25-review-DEPL-dCarriedReceipt-9-round6.md) | spec-audit | DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |
| [2026-08-26-review-DEPL-dCarriedReceipt-15-diff-review-round4.md](../reviews/2026-08-26-review-DEPL-dCarriedReceipt-15-diff-review-round4.md) | diff-review | DEPL-dCarriedReceipt-1 DEPL-dCarriedReceipt-2 DEPL-dCarriedReceipt-3 DEPL-dCarriedReceipt-4 DEPL-dCarriedReceipt-5 DEPL-dCarriedReceipt-6 DEPL-dCarriedReceipt-7 DEPL-dCarriedReceipt-8 DEPL-dCarriedReceipt-9 DEPL-dCarriedReceipt-11 DEPL-dCarriedReceipt-12 DEPL-dCarriedReceipt-13 DEPL-dCarriedReceipt-14 DEPL-dCarriedReceipt-15 |

<!-- /gen:spec-records -->

## 1. Goal

Three files gov ships are DERIVATIVES of an adopter's file rather than sources for it, and the
registry has no way to say so. Every role in `ROLE_KINDS` (`govkit.py:1242`) either lands bytes or
declines for a reason that is false of a fork, so the descriptor's only honest option today is to
call them `engine` and hope nobody runs `update`. The live consequence is measurable and bad:
inCMS's `.governance/install.index` declares `scripts/recall/extract.py` with role `engine`, while
gov's `tools/memory-recall/extract.py` is the fork — it carries `import recall_conf` at line 55 and
`CONF = recall_conf.resolve()` at line 57, and inCMS's `scripts/` tree contains no `recall_conf`
anywhere. One automatic update writes gov's blob over inCMS's and `scripts/recall/query.py`, which
does `import extract as E` at its line 66, dies at import with `ModuleNotFoundError: No module named
'recall_conf'` — reproduced, not predicted. That CLI is the one inCMS's own charter mandates every
session run. This unit adds the role that lets a descriptor say "this is a fork" and makes `update`
report it instead of writing it.

## 2. Scope (IN)

- **S1** — `ROLE_KINDS` gains `"forked"` mapped to a NEW kind, `forked`, so the derived
  `LANDABLE_ROLES` (`:1254`) excludes it automatically and no second list has to be remembered.
- **S2** — the new kind gets its row in `KIND_MARKS` (`:1258`), its line in `SKIP_REASONS` (`:1311`),
  and its place in `cmd_plan`'s printed summary (`:1457`), which hand-names five kinds today while
  `n` is derived from `KIND_MARKS` — so a kind added to the table alone is counted and never printed.
- **S3** — `UNLANDED_REASON` (`:236`) gains a `forked` line, which is what makes `selfcheck` arm 7g
  (`:843`) demand an `UPDATE_ROLE` row for it without that demand being written twice.
- **S4** — `UPDATE_ROLE` (`:2857`) gains `"forked": "report"`, the disposition `-2` introduces. A
  forked row prints one line with its verdict and, WHEN THE ROW CARRIES ONE, its `direction`; it is
  counted in the tally and is NEVER written in either direction. That is `-2` S3's `report` shape —
  one printed row, counted, no `r.fail` — with `direction` as an OPTIONAL trailing field rather than a
  second line or a second row. `-2` defines the disposition and this unit is its second consumer; the
  shape is not re-specified here, only the field appended to it. The printer TOLERATES an absent
  `direction`: `how = UPDATE_ROLE.get(role)` at `:2974` keys on the RECEIPT's role, so a row reaches
  this printer from receipts this unit never wrote — one stamped before the role existed, or one
  whose descriptor has since changed its keys — and a printer that raises `KeyError` on a
  report-only row converts a report into a crash. The missing-key refusal is S5's, and it fires on
  DESCRIPTORS only.
- **S5** — a `forked` rule declares two required keys, and a descriptor that omits either is a
  `selfcheck` failure by name. `direction` is one of `gov-from-target`, `target-from-gov` or `both`,
  and `record` is the id that ratified the fork. The demand is on the DESCRIPTOR rule and nowhere
  else: a receipt row is read by S4's printer, never validated by it. Required on write, tolerated
  on read — the refusal lives where an operator can fix it.
- **S6** — a `selfcheck` arm over gov's own kit-source surface: any source whose head carries a
  `FORKED from` header must be claimed by a rule whose role is `forked`. The predicate was run over
  the real tree before being proposed; §4 records what it hits and what it nearly hits.
- **S7** — `tools/memory-recall/kit.toml` gains the rule that declares its three forked sources, in
  the SAME commit as S6. Without it S6 reds gov's own registry on the first run and the unit cannot
  land alone.
- **S8** — `selftest.py` arms for each new refusal branch, plus one asserting a `forked` row is
  reported and not written by `update --write`, and one asserting a `forked` row with no `direction`
  is printed rather than raised on.

## 3. Non-goals (OUT)

- **Not** a reverse transform, an upstream verb, or any writing of target bytes back into gov. That
  is on the build-wide cut list, and `direction` is a LABEL on a report, never an instruction.
- **Not** a merge of a forked file. A fork is not a divergence to reconcile; `three_way` never runs
  on one, which is the difference between this role and `engine`.
- **Not** teaching `apply` to install a forked file at first install either. A fork's whole claim is
  that gov's bytes are wrong for the target, and that claim does not weaken because the target's copy
  is absent.
- **Not** auditing the adopter's side. inCMS's own `.governance/install.index` still says `engine` on
  `scripts/recall/extract.py` after this lands, and correcting that is the adopter-side build under
  slug `dPinnedVintage`, not this unit.
- **Dependency:** `-2` first. `report` is not a disposition at `9ddcc5c9`; `UPDATE_ROLE`'s values
  there are `table`, `report-reseed`, `skip`, `adopter`, `block` and `refuse`. S4 has nothing to
  dispatch to until `-2` lands, and this unit must not introduce a second one.

## 4. Design

### Data model

`ROLE_KINDS["forked"] = "forked"` — a new kind rather than a reuse of `blocked`, for two measured
reasons. `planned_writes` (`:1388`) previews a `blocked` rule from `rule_destinations` alone and
never from the source pool, so a forked rule derived from a `**` include with no `to` would preview
NOTHING; and `SKIP_REASONS["blocked"]` (`:1315`) reads "no verb here can write a gov-owned region
into a target-owned file", which is a statement about `merged` and is false of a fork. The forked
kind previews from the pool like every non-blocked role, prints its own mark, and carries its own
reason.

The DESCRIPTOR rule declares `direction` and `record`, and neither has a default: an unstated
direction is the same silence `version_from` already refuses, and a fork with no ratifying record is
a fork nobody agreed to. A written receipt row COPIES both from the rule that produced it — `-13` S5
binds a row's role and these two keys to the rule `resolve_entry` returned rather than to any
measurement — but the update-side printer treats them as OPTIONAL on read, because `UPDATE_ROLE` is
keyed on the receipt's role (`:2974`) and a receipt outlives the descriptor that wrote it. Required
on write, tolerated on read: one rule, two call sites, and no crash on the report path.

One pre-existing hazard sits directly under S1 and is recorded because a builder will meet it.
`LANDABLE_ROLES` is assigned TWICE at module level: a literal `("engine", "seed")` at `:230` and the
derived form at `:1254`, whose own comment says "DERIVED, never declared beside the table". The
second shadows the first, and the two coincide today only because `ROLE_KINDS` currently derives
exactly those two. S1 is correct as written because `:1254` is the assignment that survives — but the
dead literal at `:230` is the same two-spellings-of-one-fact class this file's comments forbid, and
it will read as the answer to anyone who greps. Deleting it is not this unit's scope; it is called
out so the builder does not "fix" S1 by editing the wrong line.

### Inventory

The S6 predicate, run over gov at `9ddcc5c9` before being proposed. Hits in the KIT-SOURCE
population — the sources `rule_sources` yields under each registry entry's `home`:

| Source | Direction | Why |
|---|---|---|
| `tools/memory-recall/extract.py` | `gov-from-target` | forked from inCMS `scripts/recall/extract.py` at `5318064`, six constructs wide |
| `tools/memory-recall/query.py` | `gov-from-target` | forked from inCMS `scripts/recall/query.py` at `5318064` |
| `tools/memory-recall/recall-opened.js` | `gov-from-target` | forked from inCMS `.claude/hooks/recall-opened.js` at `fd6274d` |

The near-miss, which is why the population is stated rather than assumed: a repo-wide `git grep -l
"FORKED from"` returns FOUR files. The fourth is gov's own `.claude/hooks/recall-opened.js`, which no
descriptor claims as a destination — `tools/hooks/kit.toml` claims `.claude/hooks/agent-cap.js` and
`.claude/hooks/scratch-guard.js` and nothing else. A predicate keyed on tracked files repo-wide would
therefore demand a `forked` declaration from an entry that does not own the path, and red gov for a
file that is gov's own hand-wired hook. Keyed on `rule_sources`, it matches exactly three.

The landmine, measured on both trees rather than argued:

| Fact | Evidence |
|---|---|
| inCMS declares the file `engine` | `.governance/install.index` row for `scripts/recall/extract.py` |
| gov's copy imports a module inCMS lacks | `tools/memory-recall/extract.py:55` and `:57` |
| gov ships that module inside the kit | `tools/memory-recall/recall_conf.py` |
| inCMS never took it | no `recall_conf` anywhere under `scripts/` |
| the breakage is at import | `scripts/recall/query.py:66` does `import extract as E` |

The same shape sits one row over and the brief does not name it: inCMS also declares
`.claude/hooks/recall-opened.js` with role `engine`, and gov's copy of that file is a fork too. Two
live rows, not one. `scripts/recall/query.py` is already `project-owned` on the inCMS side, so it is
the one of the three that is accidentally safe today.

### Alternatives rejected

- *Reuse `merged`'s `blocked` kind.* Rejected on the two measured grounds in the data-model section:
  a `**`-derived rule would preview as nothing, and the printed reason would be a sentence about
  gov-owned regions that has nothing to do with a fork.
- *Reuse `project-owned`.* It means gov supplies no bytes for that source, ever. Gov supplies bytes
  here and uses them itself; what it does not have is the right to send them. Collapsing those two
  makes the receipt unable to say which of them is true.
- *Leave the roles alone and just exclude the three paths from the memory-recall kit.* It fixes these
  three files and gates nothing, which is the could-not-fail shape one level up: the next fork lands
  as `engine` and nobody hears about it until an adopter's tool stops importing.
- *Refuse the run on a forked row instead of reporting it.* That is the `refuse` disposition `-2`
  exists to remove: one forked row would make every future `update` on that target exit non-zero and
  never re-stamp its receipt.

### Files touched (estimate)

`tools/govkit/govkit.py` (~30 lines across the four tables, the plan summary and the update
dispatch), `tools/memory-recall/kit.toml` (one rule), `tools/govkit/selftest.py` (6 arms).

## 5. Production-readiness checklist

- security — this is a data-integrity guard rather than a security boundary, but it closes a real
  supply-chain-shaped hole: gov currently ships a path where its own bytes silently replace an
  adopter's working program, and the adopter's index records that arrangement as intended.
- perf / scale — the S6 arm reads the head of each kit source once per `selfcheck`. The population is
  the tracked files under the entry homes, already walked by arms 3 and 4.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a `forked` rule missing `direction` or `record` fails by name in
  `selfcheck` rather than defaulting; a `forked` row in a receipt whose descriptor no longer declares
  the role is reported, not written, because `UPDATE_ROLE` is keyed on the RECEIPT's role — and such
  a row prints without a `direction` rather than raising on the missing key.
- observability — every forked row prints with its `direction` and its `record`, so the operator sees
  which way the derivation runs and which decision authorised it, without opening the file.
- risks — the residual risk is a fork with no header, which the S6 arm cannot see. Named rather than
  implied: the arm gates the class "a file gov marked as forked is declared as forked", not the class
  "every fork is marked". The second needs a convention nobody can enforce from inside the tool.
- testing + left-shift gates — SIX `selftest.py` arms, which is the number §4 estimates and the
  number S8 plus F3 enumerate: one per new refusal branch (S5's missing `direction`, S5's missing
  `record`, S6's undeclared fork), one asserting a `forked` row is reported and not written by
  `update --write`, one asserting a `forked` row carrying no `direction` is printed rather than
  raised on, and F3's bounded-head arm placing a marker below the 40-line bound and expecting no
  hit. They sit alongside the standing `selfcheck` predicate, which is a gate rather than an arm.
  The finding left-shifted is the memory-recall landmine, gated as a class over the whole registry
  rather than as a fix to three files.
- migration / rollback — none on disk. A receipt written before this unit carries no `forked` row, so
  nothing to migrate; reverting the role returns those three files to `engine`, which is the state
  this unit exists to end.
- user docs — `WIRE-INTO-PROJECT.md` gains the role in its role table, with the one sentence that
  matters: a forked file is reported in both directions and written in neither.

## 6. Acceptance criteria

- **AC1** — Copying gov's `tools/memory-recall/extract.py` over a copy of inCMS's `scripts/recall/`
  and running `python -c "import extract"` fails with `ModuleNotFoundError: No module named
  'recall_conf'` at `extract.py:55`. Observe RED first: this is the state at `9ddcc5c9` today, it is
  what an automatic `engine` update performs, and it has been reproduced rather than predicted.
- **AC2** — With the memory-recall descriptor declaring the three sources `forked`, a fixture receipt
  carrying those rows runs `govkit.py update --write` to exit `0`, prints one `report` line per row
  naming its `direction`, writes none of the three, and re-stamps `gov_commit`.
- **AC3** — The S6 `selfcheck` arm is GREEN over the shipped registry and reds when the `forked` rule
  is removed from `tools/memory-recall/kit.toml`, naming the source and the owning entry. Its hit set
  is exactly three sources; the arm asserts that count so a predicate that goes blind is caught.
- **AC4** — A descriptor declaring `role = "forked"` without `direction`, or without `record`, fails
  `python tools/govkit/govkit.py selfcheck` by name on the missing key. Observe RED first: at
  `9ddcc5c9` the role is not in `ROLE_KINDS` at all, so arm 3b refuses it as an unknown role rather
  than for the reason that matters.
- **AC5** — `python tools/govkit/govkit.py plan --target <fixture>` lists all three forked sources
  with the new mark, and the printed summary line counts them. Observe RED first: with the kind added
  to `KIND_MARKS` alone, `cmd_plan`'s summary at `:1457` names five kinds and the forked count is
  computed and never printed.
- **AC6** — `selfcheck`'s existing arm 7g stays green: every key of `UNLANDED_REASON` and every
  member of `LANDABLE_ROLES` still has a row in `UPDATE_ROLE`, now including `forked`.
- **AC7** — A receipt row carrying `role: "forked"` and NO `direction` key — the shape a receipt
  written before this unit produces, and the shape a descriptor edit leaves behind — is printed and
  counted by `govkit.py update --write`, writes no bytes, and the run exits `0`. Observe RED first:
  a printer that reads `row["direction"]` raises `KeyError` on that row, turning the report
  disposition into a traceback on the one path that exists to avoid acting.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar; specifically the `govkit selftest` and `govkit
selfcheck` legs. This unit adds refusal branches — S5's two missing-key refusals and S6's — so
`tools/govkit/refusal_join.py` applies: every branch needs an arm asserting it. `BRANCH_PIN` in
`tools/govkit/refusal_join.py:41` is a shrink-only FLOOR, so it is re-derived at landing rather than
pinned to a literal here, and it is moved in the SAME commit with both values named beside it, per
that file's own convention.

## 8. Open questions

- **F1 — should `direction` be a free string or a closed enum?** A closed enum of exactly
  `gov-from-target`, `target-from-gov` and `both`. A free string is a field two descriptors spell two
  ways, and the value is read by a human deciding whether to touch the file.
  RESOLVED (agent, 2026-08-24, delegated): closed enum, validated in `selfcheck`, under the
  full-scope approval.
- **F2 — what `record` do the three memory-recall sources cite, given no decision record ratifies
  their fork today?** They cite this unit. The fork is currently documented only inside the three
  file headers, which is exactly the state S5 exists to end, and inventing a plausible-looking prior
  id would be worse than citing the unit that made the declaration possible.
  RESOLVED (agent, 2026-08-24, delegated): `DEPL-dCarriedReceipt-10`, with its `DECISIONS.md` row
  landing in the same commit.
- **F3 — should the S6 arm read the whole file or only its head?** The head, bounded at the first 40
  lines. All three live markers sit at line 4 or 5, and an unbounded read invites a false hit from a
  file that merely discusses forking — this spec's own text being the obvious example.
  RESOLVED (agent, 2026-08-24, delegated): bounded head read, with the bound asserted by an arm that
  places a marker below it and expects no hit.

## 9. Revision log

- rev-7 · 2026-08-25 · built. §5's user-docs item names a role table in `WIRE-INTO-PROJECT.md`;
  there is no such table in that file, so the sentence landed in `skills/deploy-governance/SKILL.md`
  beside the other plan marks, which is where the marks are already documented for an operator.
  S6's first draft was keyed on `rule_sources` as the Inventory describes, and that arm COULD NOT
  FAIL: `rule_sources` skips any include carrying a glob character, and the rule that swallows an
  undeclared fork is exactly the `**` one. Observed — undeclaring `extract.py` left selfcheck GREEN.
  Re-aimed at `resolve_rule_pool`, the expanded pool, and re-observed RED. The Inventory's reasoning
  about the repo-wide near-miss stands and is unchanged; only the enumerator moved.
- rev-6 · 2026-08-25 · round-4 fold: L4 — §7's `BRANCH_PIN` sentence rendered an English clause as
  an inline code identifier, and the repair round 3 claimed landed in one spec of four. It now
  carries `-9` §7's repaired shape, identifier inside the backticks and property in prose beside it,
  citing `tools/govkit/refusal_join.py:41` where the constant actually sits.
- rev-5 · 2026-08-24 · round-4 fold: S4's print shape is bound to `-2` S3's `report` disposition
  explicitly — one counted row, no `r.fail`, with `direction` an optional trailing field rather
  than a second line. This unit is that disposition's second consumer and does not re-specify it.
- rev-4 · 2026-08-24 · round-3 fold: the literal `BRANCH_PIN` value is withdrawn, for the reason `-5` records.
- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass (5 lenses + fold). Every table
  and line number cited was opened at `9ddcc5c9`; the landmine was reproduced end to end rather than
  reasoned about, and the S6 predicate was run over the real tree before it was proposed. Three
  corrections to the brief are folded in. First: `"forked" -> "report"` cannot be the whole of the
  role addition — `ROLE_KINDS`, `UNLANDED_REASON`, `KIND_MARKS`, `SKIP_REASONS` and `cmd_plan`'s
  summary all key on it too, and `selfcheck` arm 7g reds without the `UNLANDED_REASON` line, so S1
  through S3 exist. Second: the S6 predicate matches three files only when its population is the kit
  SOURCE surface; repo-wide it matches four, and the fourth is gov's own hand-wired
  `.claude/hooks/recall-opened.js`, which no descriptor claims. Third: the landmine is two live rows
  rather than one — inCMS declares `.claude/hooks/recall-opened.js` as `engine` as well, and gov's
  copy of that file is also a fork.
- rev-2 · 2026-08-24 · folded the pre-code review: B3's `-10` half, which is that this unit made
  `direction` and `record` required on BOTH the descriptor rule and the receipt row while `-13` wrote
  forked rows carrying neither. The keys are now required on the DESCRIPTOR and tolerated on the
  receipt row S4's printer reads, with the reason stated — the dispatch at `:2974` keys on the
  receipt's role, so rows this unit never wrote reach that printer — and AC7 observes it. The
  companion half, binding a row's role to the rule rather than to the attribution walk, is `-13` S5's
  and lands there.
- rev-3 · 2026-08-24 · round-2 fold: the selftest arm count no longer contradicts itself. §5 said
  five arms while §4's files-touched estimate said six; re-counted against S8 and F3 the answer is
  SIX — three refusal branches, the reported-not-written arm, the absent-`direction` arm, and F3's
  bounded-head arm — so §5 now enumerates them and §4's estimate stands unchanged. Logged at the
  foot of this section because this file's revision log runs oldest-first.

## 10. Reuse audit

The reuse decision this unit turns on is that `ROLE_KINDS` is already the single table and
`LANDABLE_ROLES` is already DERIVED from it (`:1254`), so a role added with a non-`write` kind is
excluded from both writing verbs from one edit. S1 rides that rather than adding a second exclusion
list, which is what the table's own comment asks for. `UNLANDED_REASON` is reused the same way:
arm 7g's `known_roles` (`:843`) is built from it, so declaring the reason IS the mechanism that
demands the dispatch row, and no third place records that `forked` exists.

The descriptor rule reuses the existing carve-out shape rather than inventing one. The descriptor
`tools/memory-recall/kit.toml` already claims three sources out of its own `**` engine pool with a
`project-owned` rule, and S7 adds
a second rule of the same form — `scan_claimed_paths` drops them from the wildcard pool exactly as it
does today, so no precedence machinery changes.

The S6 arm extends `selfcheck`'s existing per-entry descriptor sweep, walking the same `descs` map
and the same `rule_sources` helper that arms 3 and 4 already walk, rather than adding a second pass
over the registry. `refusal_join.py`'s anchor-based join needs no change: the new branches are
ordinary `r.fail` call sites inside the functions it already enumerates — and the count does not
move on the read side, because the receipt-row tolerance added at S4 is the ABSENCE of a branch
rather than another one.
