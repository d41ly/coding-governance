# TOOL-aQuotedBrief-6 — the closing review's minors: dispositions, re-preflight, the cutoff date, quoting, parks and arms

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aQuotedBrief-6-12-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aQuotedBrief-6-12-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aQuotedBrief-6-11-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aQuotedBrief-6-11-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review left eleven medium and low findings standing at its CONVERGED exit, and the build
method promotes them as ONE batched unit. Two matter beyond hygiene: `check_prompt_brief` re-grades
the join at every preflight, so a run that adds a unit mid-build is refused at its next re-preflight;
and the cutoff date this repo declares equals the `opened:` date of prompt-mode runs in flight, so one
of them refuses its next re-preflight with no override. The rest tighten the disposition grammar, the
park match and the record listing, correct one protocol sentence, and add the arms the review found
missing. Round 1 M2 to M6 and L1 to L4, round 2 low 1.

## 2. Scope (IN)

- **S1 (round 1 M3)** — `verb_preflight` calls `check_prompt_brief` only at a first preflight, the
  `_pf_first` gate `check_branch_carried` already uses. Observed by AC1.
- **S2 (round 1 M6)** — `.unattended.conf` declares `PROMPT_BRIEF_CUTOFF="2026-10-10"`, a date after
  the `opened:` of every prompt-mode run live on 2026-10-09, and its comment says a date must clear
  runs in flight as well as landed builds. Observed by AC2.
- **S3 (round 1 M2)** — `read_brief_items` gives a disposition only when its argument is non-empty
  for all four kinds, so a bare `[stale]` or `[parked]` is no disposition. Observed by AC3.
- **S4 (round 1 M4)** — every non-blank line under `### Items` that does not open `<n>.` is refused
  by join rule 1, naming the line, instead of being invisible to the join and to term 7. Observed by
  AC4.
- **S5 (round 1 L1)** — both prompt-record listings, in `check_prompt_brief` and `check_brief_items`,
  pass `-c core.quotepath=off`, so a non-ASCII record name is read rather than skipped. Observed by
  AC5.
- **S6 (round 1 L2)** — term 7 accepts a park only from a line whose ITEM field opens
  `brief item <n>:`, anchored to the shape `park()` writes, never from text inside a reason.
  Observed by AC6.
- **S7 (round 1 L3)** — the `build-complete` row of `tools/unattended/PROTOCOL.template.md` says
  `stale` and `duplicate` items are met at BASE, and its render follows, inside the size cap.
  NOT OBSERVED by a criterion of its own: the protocol size and parity legs grade the render.
- **S8 (round 1 L4, round 1 M5, round 2 low 1)** — arms in `tools/unattended/unattended.test.sh`:
  structural rules 2, 3 and 4 and the order and non-empty halves of rule 1; the two-disposition half
  of join rule 1; a term-7 close arm with `SPEC_THIN_CUTOFF` declared, which reaches the second call
  site; the slug-mode half of AC7 with a prompt record at its BASE; and the trailing build brief added
  to the join loop, so rule 3 is shown firing with a skip record sorting last. Observed by AC7.

## 3. Non-goals (OUT)

- Refusing a listed record whose `git show` fails. With `core.quotepath=off` the listing and the read
  agree, and a failure there is a repository fault, not a brief defect.
- A gate scanning `tools/` for unquoted `ls-tree --name-only`. The class is real; it is an ask for the
  memory-tree kit, filed in this build's wrap-up, not a change to this kit.
- Retrofitting grandfathered records.

### Edges

- **consumes-from** `TOOL-aQuotedBrief-4` — the cutoff reader the arms of S8 set up for.
- **consumes-from** `TOOL-aQuotedBrief-5` — the heading predicate the listings of S5 sit beside.

## 4. Design

### Evidence

Read at `5e2187386` on 2026-10-09; the round 1 and round 2 records under `reviews/` carry each
finding's file and line.

- `verb_preflight` gates `check_branch_carried` on `[ -z "$_pf_first" ]` and calls
  `check_prompt_brief` unconditionally.
- `read_brief_items` admits `k == "stale" || k == "parked" || a != ""` and skips any line not
  matching `^[0-9]+\.`.
- Both listings call `GIT ls-tree --name-only` with no quoting setting; `check_branch_carried` passes
  `-c core.quotepath=off`.
- Term 7 matches ` · item brief item $n:` anywhere in the run-state file.
- aLevelledCopy, a prompt-mode run opened 2026-10-09, carried no `## The prompt` heading when round 1
  read it.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` · `.unattended.conf`

### Alternatives rejected

- **Two batched units.** Every fix writes `unattended.sh` or its suite, so no split is disjoint, and
  the method allows a second batch only across disjoint write sets.
- **Keeping the check on every preflight and only moving the date (round 1 M6's corrected fix).** The
  date stops one in-flight run being stranded; it does not stop any run that grows its roster mid-build
  being refused at its next re-preflight, which only the first-preflight gate does.

## 5. Production-readiness checklist

- security — S6 narrows what satisfies a park; nothing widens.
- perf / scale — S1 removes the check from every re-preflight.
- error / empty / loading states — S4 refuses lines the join used to ignore.
- observability — each refusal names its rule and line.
- risks — the cutoff move leaves records opened 2026-10-09 ungraded, which is the purpose.
- testing — arms in `tools/unattended/unattended.test.sh`, run once at VERIFYING.
- migration — none.
- user docs — the protocol row of S7.

## 6. Acceptance criteria

- **AC1** — When a prompt-mode run that passed its first preflight adds a roster unit and runs
  `--preflight` again, the re-preflight prints `preflight OK`.
  Red when: a grown roster is refused at check 115 rule 3.
- **AC2** — When `grep -n "^PROMPT_BRIEF_CUTOFF=" .unattended.conf` runs, it reads `2026-10-10`.
  Red when: the date still equals an in-flight run's `opened:`.
- **AC3** — When an item reads `[stale]`, `--preflight` refuses at check 115 rule 1 naming that item.
  Red when: a disposition with no argument is accepted.
- **AC4** — When `### Items` holds a numbered item and a `- The docs.` line, `--preflight` refuses at
  check 115 rule 1.
  Red when: a line the join cannot read is ignored.
- **AC5** — When the record's file name carries a non-ASCII character, `--preflight` grades it.
  Red when: the record is skipped as not a prompt record.
- **AC6** — When a park for item 2 carries ` · item brief item 1:` in its reason, `--close` still
  reports item 1 unmet.
  Red when: a reason satisfies an item it does not name.
- **AC7** — When the slice of the prompt-record and term-7 arms runs, the rule-3 arm printing
  `rule 3, a roster unit no planned item names` among them, every arm named in S8 passes on
  the unit's driver, and each was observed red against the pre-unit driver or a staged break.
  Red when: an arm passes on both, so it observes nothing.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC3 AC4 AC5 AC6 AC7 · the pre-unit driver, or a staged break where the pre-unit driver already passes · none

## 8. Open questions

- **F1 — Gate the check on the first preflight, or keep it on every preflight with a later date?**
  Round 1's M3 and M6 fixes pulled in opposite directions. RESOLVED (agent, 2026-10-09, delegated):
  both the gate and the later date; together they satisfy every criterion either alone does, and
  neither trips a veto.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from the closing review's minors.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` found no new seam; every fix lands in a
function this build added. The `_pf_first` gate and the `core.quotepath=off` setting are reused from
`check_branch_carried` in `tools/unattended/unattended.sh`.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — the build's query.
