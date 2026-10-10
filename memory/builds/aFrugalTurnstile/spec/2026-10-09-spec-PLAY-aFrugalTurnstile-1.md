# PLAY-aFrugalTurnstile-1 — the charter's §1 Landing states the scoped-then-full path

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams playbook · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-PLAY-aFrugalTurnstile-1-1-acceptance-ledger.md](../build/2026-10-09-build-PLAY-aFrugalTurnstile-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 DEPL-aFrugalTurnstile-1 |
| [2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md](../reviews/2026-10-10-review-TOOL-aFrugalTurnstile-1-11-diff-review-round1.md) | diff-review | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 TOOL-aFrugalTurnstile-11 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's prompt asks for charter text for part E: a landing may take the scoped bar when a full
bar runs after the merge and its red is binding through a recorded state, never a log line. At base
the charter's §1 Landing says only that the push boundary decides whether a full bar is owed against
a recorded green and a staleness bound, which an adopter's stricter rule (a full bar per unattended
landing) reads as the whole of the safety argument. This unit implements design D12 for
`coding-governance-agents.template.md` and its render in `AGENTS.md`: one directive line in the
charter's voice, stating the condition and the binding red, and pointing rather than restating.

## 2. Scope (IN)

- **S1 — one directive line in §1 Landing.** Directly after the bullet "After each merge run a
  diff-scoped gate …; the push boundary DECIDES whether a full bar is owed, against a recorded green
  and a declared staleness bound.", the template gains, outside every `kit:` and `when:` block:

  ```markdown
  - A landing may take the scoped bar only where a full bar is DECLARED to run after the merge, and that bar's red BINDS: a recorded state the push boundary reads, forcing the full bar on every later landing until a full green descends from it — never just a log line.
  ```

  The bullet above it is unchanged. Observed by AC1 and AC6.
- **S2 — the render follows.** `AGENTS.md` is re-rendered with
  `bash tools/playbook/adopt-playbook.sh --target .`, so its `gov:playbook` region carries the same
  line at the same place. Observed by AC2.
- **S3 — the two high-water rows record the intended growth.** `bash tools/check-template-size.sh
  --bump` re-records `coding-governance-agents.template.md`, and the same verb with `AGENTS.md`
  re-records the charter's row, in `tools/template-size-highwater.txt`. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- The mechanism, its key and its ref: the build's code units, the unattended protocol's landing rule
  and the runbook own those, so the line names neither (charter §6).
- The existing kit-conditional bullet "An unattended run lands by its protocol's landing rule, not
  the local-first one above." It already points an unattended run at the protocol, where this
  build's protocol unit writes the mechanism, and stays byte-for-byte.
- The charter's version line and snapshot, bumped once at the close with the kit versions.
- The size limit rows in `tools/template-size-limits.txt`, which this growth stays under.

### Edges

- **consumes-from** external — the post-merge bar, its binding ref and the boundary's decision are
  built by this build's code units at later orders. The line states a rule and names none of them,
  so no criterion rests on them.

## 4. Design

### Evidence

Read at base `bef97330`.

- `bash tools/check-template-size.sh` prints `48597 / 49152 bytes (555 under, 98.9%)`;
  `tools/template-size-highwater.txt` records 48597, so any growth prints the advisory WARN until
  re-recorded.
- `bash tools/check-template-size.sh AGENTS.md` prints `54472 / 64512` and a WARN, because its
  high-water row records 54377: the render already sat 95 bytes above its record before this build
  (PINNED, 2026-10-09).
- `bash tools/check-line-length.sh` reports 0 lines over 450 characters in both files; the new line
  is 267 characters.
- `bash tools/playbook/adopt-playbook.sh --target . --check` prints `render-playbook OK`. The bullet
  S1 follows sits at template line 59 and `AGENTS.md` line 111, outside the `kit:unattended` block
  that ends at template line 58.
- The line measures 269 bytes with its newline (PINNED, 2026-10-09), leaving the template 286 bytes
  under its 49152 ceiling. This design's ceiling on the growth is 300 bytes.
- `.claude/rules/product.md` asks to prefer externalizing to spending the template's headroom. One
  rule line is not activity-scoped or one-time, so it belongs in the template.

### What this unit's gate does not check

N/A — this unit adds no gate.

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `AGENTS.md`
- `tools/template-size-highwater.txt`

### Rollout

The template renders into every adopter's charter on its next `govkit update`; the line is
unconditional, because the rule binds any project whose boundary lands on a scoped bar, unattended
or not.

### Alternatives rejected

- **Rewriting the existing "After each merge" bullet to carry both rules.** One line per directive
  is the charter's own rule, and the existing bullet's two clauses already make one directive.
- **Naming `GATE_POST_MERGE` and `refs/gov/bar-red` in the line.** Both are owned by the code and
  stated in the protocol and the runbook; a third statement in the charter is the copy that rots.
- **Putting the line inside the `kit:unattended` block.** An attended push lands on the boundary's
  scoped bar too, so the rule is not the unattended kit's.

## 5. Production-readiness checklist

- security — N/A — one prose line; no write path.
- perf / scale — every session reads 269 bytes more of the charter.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — the two size legs print the new figures; S3 keeps them free of WARN.
- risks — the rule tells an adopter a scoped landing is safe only with a binding post-merge bar; an
  adopter without one keeps today's full-bar decisions, which is the boundary's own default.
- testing — direct greps, the renderer's `--check`, the size and line-length checkers run directly.
- migration — N/A — no stored state.
- user docs — the charter is the document.

## 6. Acceptance criteria

No refusal is added, so nothing here is observed RED on a staged break; each `Red when:` names the
break the named command reports.

- **AC1** — When `awk '/^\*\*Landing — merge protocol:\*\*/,/^\*\*Kickoff-manifest merge exception/'`
  runs over `coding-governance-agents.template.md` and over `AGENTS.md`, each output carries the S1
  line once, directly after the "After each merge run" bullet, checked with
  `grep -c 'DECLARED to run after the merge'`. Red when: the line is absent, duplicated, or placed
  inside a `kit:` block.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it prints
  `render-playbook OK`. Red when: the template moved and the render did not.
- **AC3** — When `bash tools/check-template-size.sh` runs after S3, it exits 0, prints a figure at most
  300 above 48597 with no `WARN` line, and `grep '^coding-governance-agents.template.md'
  tools/template-size-highwater.txt` prints that same figure.
  Red when: the growth passed the design's ceiling, or the high-water still reads 48597.
  figure: 48597 and 300 are PINNED; the new figure is DERIVED.
- **AC4** — When `bash tools/check-template-size.sh AGENTS.md` runs after S3, it exits 0 with no `WARN`
  line, and `grep '^AGENTS.md' tools/template-size-highwater.txt` prints the figure it reports.
  Red when: the charter's high-water was not re-recorded.
- **AC5** — When `bash tools/check-line-length.sh` runs, it reports 0 lines over 450 for both files.
  Red when: the line was written past the declared width.
- **AC6** — When `grep -n 'DECLARED to run after the merge' coding-governance-agents.template.md` is
  piped to `grep -cE 'GATE_POST_MERGE|refs/gov|post-merge.sh'`, it prints 0.
  Red when: the charter restates a key, a ref or a script the protocol and the runbook own.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `playbook render wiring` · `playbook parity` · `agent-cap restatement` · `python resolver (behaviour + inline parity + idiom ban)` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `run-gates canary` · `run-gates evidence` · `foreign-prefix parity (every self-test at three prefixes)` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` · `kit-placeholders self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The twelve legs after `agent-cap restatement` are owed by the broad `tools/` guard that
`tools/template-size-highwater.txt` trips, named as the build's brief asks. All run once, at the
close.

## 8. Open questions

- **F1 — does the charter line point at the protocol by path?** Options: (a) a rule line with no
  path, relying on the existing kit-conditional bullet that already sends an unattended run to the
  protocol's landing rule; (b) a path to the protocol inside the line, which a target without the
  unattended kit renders as a dead pointer; (c) a second, kit-conditional line carrying the path.
  (b) breaks every adopter without that kit. (c) spends about 150 more of 555 bytes on a pointer
  the block above already makes. (a) satisfies every criterion. RESOLVED (agent, 2026-10-09,
  delegated): (a).
- **F2 — does S3 re-record `AGENTS.md`'s high-water, which trailed the render by 95 bytes before this
  build?** Options: (a) re-record it, the commit naming both the 95 bytes found at base and this
  unit's 269; (b) re-record only the template's row and leave the charter's WARN standing. (b) keeps
  an advisory WARN that now also hides this unit's intended growth. (a) satisfies AC4 and records
  the state in the open. RESOLVED (agent, 2026-10-09, delegated): (a).

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and design D12, with the line
  measured against the base template.

## 10. Reuse audit

The seams are the template's §1 Landing list, the renderer `tools/playbook/adopt-playbook.sh` and
the size ratchet `tools/check-template-size.sh --bump`. No code is added.
`python tools/codebase-map/reuse_lookup.py "state in the unattended protocol's landing rule that a
scoped landing is safe when a post-merge full bar's red binds"` returned name-stem matches only, so
no existing seam fits beyond those named. Recall named this build's prompt, brief and design, and
`TOOL-aMendedFleet-117`, an open ask that the charter's landing text describe a remote ruleset,
which this unit leaves to that ask. Where the brief and the tree disagree: none found for this
unit; the bullet the brief quotes is at template line 59 as quoted.

Recall terms used: `python tools/memory-recall/query.py "which records govern the landing rule
text in the unattended protocol, the charter section 1 Landing and the runbook's gate-env
declarations" --terms "landing rule push boundary scoped bar full bar post-merge binding red
gate-env declaration INHERITED_RED GATE_DOC_PATHS charter Landing protocol size"`
