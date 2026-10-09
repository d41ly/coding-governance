# DEPL-aFrugalTurnstile-1 — the runbook states what an adopter declares to use each part

**Status:** CLOSED · rev-2 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams deployer · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-DEPL-aFrugalTurnstile-1-1-acceptance-ledger.md](../build/2026-10-09-build-DEPL-aFrugalTurnstile-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-2-build-brief.md) | journal | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-1 TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's prompt asks that this build "state plainly what an adopter must declare to opt in", and
the adoption session acts on that statement for inCMS and NicoCares once this lands.
`WIRE-INTO-PROJECT.md` is the runbook an adopting agent follows, and at base it documents one
push-boundary declaration, `GATE_DOC_PATHS`. This unit implements design D12 for the runbook: the
design record's §4 table, in the runbook's own voice, beside that existing paragraph, with the
remote-CI job spelled out.

## 2. Scope (IN)

- **S1 — one optional item beside the doc-class item.** Directly after the bullet opening
  "**Optional, to stop a doc push paying the whole bar**", in the same list, a new bullet opens
  "**Optional, to land on the scoped bar and run the full bar after the merge**". Its first
  sentences say: declare `GATE_POST_MERGE=local` or `GATE_POST_MERGE=ci` in `.githooks/gate-env.sh`
  and commit it; the push then lands on the bar the boundary decides; the full bar runs on the landed
  sha; its red is published as `refs/gov/bar-red` on the adopter's remote and forces the full bar on
  every later landing until a full green descends from it. Observed by AC1.
- **S2 — the table, one row per part, under that bullet.** The rows are the design record's §4, in
  the text of §4 "The table" below: nothing to declare for the first-parent bound, the tree cover and
  lineage reuse; nothing for a wrapper bar's own green; the `--hold` entry for a bar that is not the
  runner; `GATE_POST_MERGE` for the post-merge bar, its binding red and the unattended close's
  scoped landing; the remote-CI job; and relaxing an adopter's own stricter unattended rule as that
  adopter's change. Observed by AC2.
- **S3 — the remote-CI row is concrete.** It says the job runs `<prefix>/run-gates/post-merge.sh
  <sha>` on every push to the default branch, with a token that can push `refs/gov/*`. Observed by
  AC2.
- **S4 — every kit path is spelled with `<prefix>/`.** The runbook names no install prefix, which
  the install-prefix leg grades on the shipping surface. Observed by AC3.

## 3. Non-goals (OUT)

- The mechanism: the build's code units.
- The `GATE_POST_MERGE` line and its comment in gov's own `.githooks/gate-env.sh`, decided at the
  close once the code exists.
- An `INHERITED_RED` paragraph. The brief names it as documented beside `GATE_DOC_PATHS`; at base
  the runbook carries no mention of it (§10), and documenting it is outside this build's prompt.
- Any adopter's own change: inCMS's unattended condition 3 and both adopters' declarations belong
  to the adoption session, on the owner's yes.

### Edges

- **consumes-from** external — `post-merge.sh`, the `--hold` verb, `refs/gov/bar-red` and the
  `covered` decision are built by this build's code units at later orders. Each criterion here is
  textual and rests on none of them; the closing review reads the paragraph against the built code.

## 4. Design

### Evidence

Read at base `bef97330`.

- `WIRE-INTO-PROJECT.md` lines 784-787 hold the `GATE_DOC_PATHS` item, the last bullet of the list
  that opens with the wiring-health self-heal and closes before "**Also copy, if you want the gates
  this repo runs on itself**". `grep -c INHERITED_RED WIRE-INTO-PROJECT.md` prints 0.
- `git ls-files --eol WIRE-INTO-PROJECT.md` reports `i/lf w/crlf attr/text=auto`: the index holds
  LF and the working copy CRLF, so a multi-line scripted replace on the working copy matches nothing
  (memory note "CRLF defeats a multi-line replace"). The builder edits with the Edit tool and checks
  the staged bytes.
- The runbook spells every kit path `<prefix>/…`, as `TOOL-aRepatriatedFork-26` made it.

### The table

```markdown
| To get | Declare | Where |
|---|---|---|
| the lag counted in first-parent landings, a push whose tree already carries a recorded green running no bar, and a full bar after a red re-running only what failed or moved | nothing: `govkit update` | — |
| the green of your own wrapper bar recorded, at the push boundary and at the unattended close | nothing: both record it | — |
| one bar per machine, for a bar that is not the runner | enter it through `<prefix>/run-gates/run-gates.sh --hold -- <your bar>`, or have the bar script re-exec itself through that | your bar script |
| the post-merge full bar, its binding red, and the unattended close landing on the scoped bar | `GATE_POST_MERGE=local`, where the lander starts it on the landing machine, or `GATE_POST_MERGE=ci`, where remote CI runs it; committed | `.githooks/gate-env.sh` |
| remote CI running it | a job that runs `<prefix>/run-gates/post-merge.sh <sha>` on every push to the default branch, with a token that can push `refs/gov/*` | your CI workflow |
| the unattended close landing without a full bar | relaxing any rule of your own that demands a full bar per unattended landing; this kit does not change it for you | your charter |
```

### What this unit's gate does not check

N/A — this unit adds no gate.

### Files touched (estimate)

- `WIRE-INTO-PROJECT.md`

### Rollout

The runbook is gov's and is read by an adopting agent at wiring time; nothing is installed. The
adoption session reads the new item when it wires inCMS and NicoCares after this lands.

### Alternatives rejected

- **A prose list instead of a table.** Six parts, each with a declaration and a place, are
  enumerable facts, which the spec format and the runbook both put in a table.
- **A new top-level section.** The doc-class item is the model the brief names, and a separate
  section would split two push-boundary declarations an adopter makes in the same file.

## 5. Production-readiness checklist

- security — the remote-CI row asks for a token that can push `refs/gov/*`; the row names that
  scope and nothing wider. No write path in gov.
- perf / scale — N/A — documentation.
- error / empty / loading states — N/A — no runtime behaviour.
- observability — N/A — documentation.
- risks — the rows name mechanisms built by later units; if one parks, its row is false until the
  close's review reconciles it, which M8 owes.
- testing — direct greps over the runbook and the install-prefix checker run directly.
- migration — N/A — no stored state.
- user docs — the runbook is the document.

## 6. Acceptance criteria

No refusal is added, so nothing here is observed RED on a staged break; each `Red when:` names the
break the named command reports.

- **AC1** — When `grep -n 'Optional, to land on the scoped bar' WIRE-INTO-PROJECT.md` runs, it prints
  one line, numbered after the line `grep -n 'Optional, to stop a doc push' WIRE-INTO-PROJECT.md`
  prints and before `grep -n 'Also copy, if you want the gates' WIRE-INTO-PROJECT.md`; and the
  bullet's text carries `GATE_POST_MERGE=local`, `GATE_POST_MERGE=ci` and `refs/gov/bar-red`.
  Red when: the item is missing, misplaced, or omits the declaration or the binding ref.
- **AC2** — When `grep -cE '^ *\| ' WIRE-INTO-PROJECT.md` is compared with its base count, it has
  grown by seven, the table sitting indented under its bullet, and `grep -n -e '--hold --' -e 'post-merge.sh <sha>' -e 'relaxing any rule of your own'
  WIRE-INTO-PROJECT.md` hits each of the three. Red when: a row of the design's §4 table is missing.
  figure: seven is DERIVED from §4's table, a header and six rows; its `|---|` separator carries no
  `| ` and the pattern does not count it.
- **AC3** — When `bash tools/check-install-prefix.sh` runs, it exits 0, and
  `grep -n 'run-gates/post-merge.sh' WIRE-INTO-PROJECT.md` shows every hit spelled with `<prefix>/`.
  Red when: the new text names gov's own install prefix.
- **AC4** — When `git diff --cached -- WIRE-INTO-PROJECT.md | cat -A` is read before the commit, no
  added line ends in `^M$`. Red when: the CRLF working copy leaked carriage returns into the index.

## 7. Gates

`install-prefix (shipped surface)` · `govkit runbook parity` · `dead-path carriers (deleted files still named)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

All run once, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and the design record's §4 table.
- rev-2 · 2026-10-09 · AC2's figure is seven, not eight: the `^ *\| ` pattern does not match the
  table's `|---|` separator, found by the build pass.

## 10. Reuse audit

The seam is the runbook's existing optional doc-class item, which the new item sits beside and
copies in shape; the table is the design record's §4, re-voiced. No code is added.
`python tools/codebase-map/reuse_lookup.py "state in the unattended protocol's landing rule that a
scoped landing is safe when a post-merge full bar's red binds"` returned name-stem matches only, so
no existing seam fits beyond the runbook item named. Recall named this build's prompt, brief and
design, and the dThriftyLanding text unit that added the doc-class item. Where the brief and the
tree disagree: the brief says `GATE_DOC_PATHS` and `INHERITED_RED` are both documented beside the
gate-env paragraph; at base only `GATE_DOC_PATHS` is, and `grep -c INHERITED_RED` over the runbook
prints 0.

Recall terms used: `python tools/memory-recall/query.py "which records govern the landing rule
text in the unattended protocol, the charter section 1 Landing and the runbook's gate-env
declarations" --terms "landing rule push boundary scoped bar full bar post-merge binding red
gate-env declaration INHERITED_RED GATE_DOC_PATHS charter Landing protocol size"`
