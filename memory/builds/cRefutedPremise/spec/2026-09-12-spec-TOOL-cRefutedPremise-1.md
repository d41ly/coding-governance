# TOOL-cRefutedPremise-1 — two refuted claims, corrected in every live carrier rather than in the two that were reported

**Status:** CLOSED · rev-2 · 2026-09-13 · node c · Tier-1 · base 09a22d2b · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Two claims in this tree were contradicted by observation on 2026-09-12, node `d`.

**Claim A — "a sidechain runs no hooks."** `tools/hooks/agent-cap.js` gave this as the reason the
`Workflow` half must be a static scan. Observed: `tools/hooks/scratch-guard.js`, a project-level
`PreToolUse` hook wired in `.claude/settings.json` on matcher `Bash|PowerShell`, DENIED a Bash
command issued by an agent inside a `Workflow` sidechain. That is exactly the
matcher-on-a-tool-the-sidechain-does-hold experiment that
`memory/builds/cBriefedPilot/build/2026-08-15-build-TOOL-cBriefedPilot-15-2-parallelism-routes.md`
asked for and could not run.

**Claim B — "settings are not hot-reloaded."** `tools/hooks/agent-cap.js` and
`memory/guides/REVIEW-PROTOCOL.md` gave this as the reason a `PostToolUse[Agent]` probe could not be
settled where the question was found. Observed: the public hooks reference states that direct edits
to hooks in settings files are normally picked up by the file watcher, and session `a6d954d0` shows
the wired `agent-cap` command changing mid-session after commit `206af3de` retargeted
`.claude/settings.json` — two denials in one transcript naming two different commands.

Both are load-bearing reasons, not decoration. A false reason attached to a correct conclusion is the
shape that survives review longest, because the conclusion keeps testing true.

**Claim B was already refuted IN THIS REPO, a month before this unit.**
`memory/guides/SESSION-KICKOFF.md` has carried `Editing .claude/settings.json takes effect
MID-SESSION — hooks are re-read, not snapshotted at start`, measured 2026-08-10, while
`tools/hooks/agent-cap.js` and `memory/guides/REVIEW-PROTOCOL.md` went on asserting the opposite. The
contradiction sat inside the one document every session front-loads at kickoff, and nothing reads two
carriers together. That is `TOOL-dUnstalledConvoy-16` with the evidence already in the building.

## 2. Scope (IN)

- **S1 — claim A is corrected wherever it is live**, with the accurate reason in its place: a script's
  `agent()` is a runtime call and not a TOOL call, so the `Workflow|Agent` matcher has nothing to
  match, and a sidechain agent holds neither tool to re-fan-out with. Observed by AC1.
- **S2 — claim B is corrected in both its carriers**, citing the public reference and the transcript.
  Observed by AC2.
- **S3 — the carrier set is derived by grep rather than taken from the report.** The two documents
  named in the request hold four of the seven live carriers. Observed by AC3.
- **S4 — every rendered or parity-checked carrier is changed at its SOURCE** and re-rendered, never
  edited in the render. Observed by AC4.
- **S5 — the shipped `agent-cap` engine bytes change, so its version marker moves.** Observed by AC5.

## 3. Non-goals (OUT)

- Building the `PostToolUse[Agent]` probe the corrected comment now says can be wired in place. The
  release-keyed-on-`tool_use_id` fix stays unbuilt and `SLOT_TTL_MS` stays the primary mechanism.
- A gate for the multi-carrier class itself. That is `TOOL-dUnstalledConvoy-16`, still OPEN, and this
  unit is one more instance of it rather than its remedy.
- Append-only build records that quote the old claims. `cBriefedPilot`'s record asked the question
  this unit answers and is left as written.

### Edges

- **Takes** the two observations as given by the owner, plus the public hooks reference fetched at
  writing time.
- **Leaves** `TOOL-dUnstalledConvoy-16` unchanged in substance, with this unit cited on the row as a
  second measured instance.

## 4. Design

The correction is prose only. No predicate, no control flow, no gate arm moves.

The carriers were found by grepping the live tree for the claim's several spellings rather than by
editing the files the report named. `TOOL-dUnstalledConvoy-16` records the failure mode this avoids:
a correction landing in one carrier while its siblings keep shipping the refuted sentence, which is
exactly what happened the last time claim A was partly corrected.

### Inventory

| Carrier | Claim | Route |
|---|---|---|
| `tools/hooks/agent-cap.js` header, two sites | A | direct |
| `tools/hooks/agent-cap.js` RULE 4 | A | direct |
| `tools/hooks/agent-cap.js` `SLOT_TTL_MS` | B | direct |
| `memory/map/features/agent-cap.md` Gaps | A | direct |
| `tools/workflows/unattended-unit.js` | A | direct |
| `tools/workflows/REVIEW-PROTOCOL.template.md` | A and B | source; rendered to `memory/guides/REVIEW-PROTOCOL.md` |
| `coding-governance-agents.template.md` §8 | A | source; rendered into `AGENTS.md` |

The charter carrier is the one a reader would have caught: `never inside the script, where no hook
reaches` sat one line above `hooks DO fire in it, both measured`. The clause was deleted rather than
rewritten, which shrinks the size-gated template.

### Alternatives rejected

Correcting only `tools/hooks/agent-cap.js` and `memory/guides/REVIEW-PROTOCOL.md` as reported. That
leaves the refuted sentence shipping to every adopter from the charter template and from the map
dossier, which is the defect `TOOL-dUnstalledConvoy-16` names.

## 5. Production-readiness checklist

- **security** — N/A. No predicate changes; `agent-cap` denies exactly what it denied before.
- **perf/scale** — N/A. Comments.
- **a11y / i18n** — N/A.
- **error/empty/loading states** — N/A.
- **observability** — improved. A reader who reached for "why is the `Workflow` half static" was
  getting a refuted answer.
- **testing/gates** — the full bar with kit self-tests, since `agent-cap` is a kit file.
- **migration/rollback** — revert. An adopter on `agent-cap@1.13` loses nothing but the correction.
- **help/ docs** — none. No user-facing surface.

## 6. Acceptance criteria

- **AC1** — no live carrier asserts that a sidechain runs no hooks, observed by
  `grep -rn "no hook runs there\|with no hooks\|don't run hooks\|reaches no hook\|where no hook reaches"`
  over the tree excluding `memory/builds/`, `memory/archive/`, `memory/ledger/` and `memory/backlog/`.
  Red when: a carrier was missed, or a corrected sentence reintroduces the claim in one of the four
  other spellings the grep covers.
  figure: DERIVED by that grep.
- **AC2** — every surviving occurrence of `not hot-reloaded` is immediately followed by its own
  refutation, observed by `grep -rn "not hot-reloaded"` — three hits, each inside the corrected
  sentence. Red when: a hit stands alone as an assertion, which is the pre-correction state.
  figure: DERIVED by that grep.
- **AC3** — seven carriers changed across seven files, observed by `git diff --stat`. Red when: the
  grep of AC1 finds a live carrier this count did not include, which is the `TOOL-dUnstalledConvoy-16`
  failure repeating. figure: PINNED at 2026-09-12; it is the carrier count this unit found, not a
  standing property of the tree.
- **AC4** — `memory/guides/REVIEW-PROTOCOL.md` matches its template rendered for this install,
  observed by `bash tools/workflows/check-protocol-parity.test.sh`; and `AGENTS.md` matches a fresh
  charter render, observed by `bash tools/playbook/adopt-playbook.sh --target . --check`. Red when:
  either rendered copy was edited directly, so the next render silently reverts the correction.
- **AC5** — `KIT_AGENT_CAP_VERSION` and the `gov:kit agent-cap@` marker both read `1.14`, observed by
  `bash tools/check-kit-versions.sh`. Red when: one token moved and the other did not, which is the
  unpaired-marker hole that gate's own header records.
- **AC6** — both edited `.js` files parse, observed by `node tools/workflows/check-workflow-syntax.js`
  for `unattended-unit.js` and by `bash tools/hooks/agent-cap.test.sh`, which EXECUTES the hook, for
  `agent-cap.js`. Red when: a comment edit closed a block comment early or unbalanced a quote, which
  this file has shipped before.
  fixture: `node --check` was the first draft of this criterion and is NOT a syntax gate on node v24 —
  module auto-detection retries the parse and swallows the failure, per the kickoff manifest. A
  criterion that cannot fail is the class §7 names.
- **AC7** — the declared merge bar is green, observed by
  `GATE_FULL=1 bash tools/run-gates/run-gates.sh` — 51/51 at rev-2, with the 55 self-test legs HELD.
  Red when: any leg fails; the agent-cap restatement gate and the line-length gate are the two this
  diff could plausibly trip.
  cost: **THE SELF-TEST BAR THIS CRITERION ORIGINALLY DEMANDED DID NOT COMPLETE ON NODE `c`, and that
  is recorded as a skip rather than folded into the green.** `GATE_FULL=1 GATE_SELFTESTS=1` was run
  and KILLED by its own 21600s wall with `govkit selftest` still executing; that leg alone declares an
  11750s ceiling. The one self-test this unit's kit actually owes was run standalone instead:
  `bash tools/hooks/agent-cap.test.sh`, 215 passed / 0 failed. It took 1926s against a 740s ceiling,
  so the ceiling does not fit this node either — a cost verdict about node `c`, not about this diff.
  `memory-hygiene self-test` (900s ceiling) likewise timed out and was not re-run; it is not this
  unit's kit.

## 7. Gates

`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`. Tier 1 — prose only, no new write
path, no migration, no shared-contract change, so gates plus one focused self-review of the diff.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-12 · written after the corrections landed in the working tree, at the owner's
  instruction to land the work as a tracked unit rather than a loose prose fix.
- rev-2 · 2026-09-13 · MOVED AC6 and AC7 to what was actually observed. AC6 named `node --check`,
  which the kickoff manifest records as no syntax gate on node v24; it now names the two checks that
  can fail. AC7 demanded a self-test bar that node `c` could not finish inside its own 21600s wall,
  so it now names the declared merge bar and carries the skip, the timings and the one kit self-test
  run standalone. Neither edit touches the product.

## 10. Reuse audit

Nothing to build. Both rendered carriers already own a renderer and a parity gate —
`check-protocol-parity.test.sh --render` and `adopt-playbook.sh --target .` — and both were used
rather than hand-editing the rendered copies.
