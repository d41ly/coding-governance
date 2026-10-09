# TOOL-aDistilledCharter-8 — the closing review's round-2 findings, closed as one batch

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling+playbook · order 13

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Round 2 of the closing review confirmed five MEDIUM and LOW findings in the renderer and the text
around it (`reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md`). Their write
sets intersect in `render_playbook.py` and the template, so BUILD-METHOD M4 batches them.

## 2. Scope (IN)

- **S1** — N2: the checkout directory is `[charter]` or `[answers]` `checkout_dir` when stated, else
  `project_name`, so a product named apart from its clone states the clone once. Observed by AC1.
- **S2** — N3: the playbook README's Nodes section says one user holds one tag, and why: the readers
  match the user alone. NOT OBSERVED by a criterion: a sentence.
- **S3** — N4: the claim's message, the charter's claim note and the runbook say gov re-renders its
  own charter in the claim's commit. Observed by AC2.
- **S4** — N5: `--check` prints the notes on a legacy block and an older template marker that the
  write mode prints. Observed by AC3.
- **S5** — N6: the playbook parity gate compares `TEMPLATE_MAJOR` with the template marker's major,
  and the render refuses a `legacy` row in a template at or past that major. Observed by AC4.

## 3. Non-goals (OUT)

- Host-aware readers, so one user could hold two machines. Filed as the follow-up it is.

### Edges

- **consumes-from** `PLAY-aDistilledCharter-5` — both edit the template; this lands second.

## 4. Design

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/playbook/README.md` · `tools/check-playbook-parity.sh` · `tools/check-playbook-parity.test.sh` · `coding-governance-agents.template.md` · `AGENTS.md` · `WIRE-INTO-PROJECT.md` · `tools/govkit/entries/playbook.kit.toml`

## 5. Production-readiness checklist

- security — N/A — no new input surface.
- perf / scale — N/A — no measurable change.
- error / empty / loading states — a v4 template naming a legacy placeholder is refused by name.
- observability — `--check` now shows the reseed note an update would hide.
- risks — none beyond the items.
- testing — renderer and parity self-tests.
- migration — none: `checkout_dir` defaults to the existing answer.
- user docs — the playbook README and the runbook.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` renders a fixture with
  `project_name = "App"` and `checkout_dir = "app/main"`, every default row reads `<root>/app/main`.
  Red when: the product name stands in for the clone.
- **AC2** — When `grep -n 'own charter' coding-governance-agents.template.md` runs, the claim note
  prints. Red when: the note omits gov's own re-render.
- **AC3** — When `render_playbook.py --target <fixture> --check` runs over a v3-marked template, its
  output carries `reseed`. Red when: `--check` is silent about it.
- **AC4** — When the parity self-test sets `TEMPLATE_MAJOR = 3` in its fixture engine, the gate
  reds naming `template major`; when a v4 fixture template names `{{TAG_A}}`, the render refuses.
  Red when: either passes.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `playbook parity` · `playbook parity selftest` · `harness arms (fail branches armed or pinned)` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: tools/playbook/render_playbook.py · covers AC1 AC3 AC4 · the round-1 fold's renderer · none
New arm: tools/check-playbook-parity.test.sh · covers AC4 · a fixture engine whose major disagrees with its template · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, the batch promoted from the closing review round 2.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; every item
extends `tools/playbook/render_playbook.py` or the parity gate's S2 list.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
