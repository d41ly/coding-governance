# TOOL-aDistilledCharter-7 — the closing review's medium and low findings, closed as one batch

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling+playbook+deployer · order 11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aDistilledCharter-1-acceptance-ledger.md) | journal | TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 DEPL-aDistilledCharter-1 KICK-aDistilledCharter-1 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 |
| [2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md](../reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round2.md) | diff-review | TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 DEPL-aDistilledCharter-2 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 closing review confirmed twenty-two MEDIUM and LOW findings across the renderer, the
parity gate, the canary and the charter's own text. Their write sets intersect — the renderer reads
the template the content fixes edit — so BUILD-METHOD M4 batches them into this one unit. Each scope
item names its finding id from `reviews/2026-10-09-review-PLAY-aDistilledCharter-1-closing-diff-round1.md`.

## 2. Scope (IN)

- **S1** — Renderer. R3: `read_fleet` and the claim refuse a user already in the fleet,
  case-folded, or one that contains or is contained in another, because every reader matches the
  user alone. R5: the claim refuses DEL and parses the whole new file before writing it. R6:
  `read_git` runs git with no inherited `GIT_*` variable in its environment. R7: a `[charter]` value carrying a one-line marker is
  refused. R8: the trailing-newline strip moves into `resolve_placeholder_value`, so `--answers`
  agrees with the render. R4 is closed by `TOOL-aDistilledCharter-2` rev-2, which keeps the legacy
  names declared. Observed by AC1 and AC2.
- **S2** — Parity gate. G2: at a root install S4's surface takes every derived kit directory. G3:
  the self-test header cites `charter [gate]`, and the predicate accepts a `.md` and a backtick
  after the charter's file name. G5: the predicate accepts a curly apostrophe, a non-breaking space,
  an en dash, `§§` and the trailing `§<n> of the charter` form, and excludes the protocol and spec
  templates. G6: S4 unsets the pathspec-mode variables. G8: the surface takes `CLAUDE.md` and the
  memory root's own live guides. G7: `ARMS_FLOORS` pins the gate at what `check-arms.py
  --emit-floors` measures. C7: a `kit:<id>` fence counts as naming the kit, and the `runlog` waiver
  row drains. Observed by AC3, AC4 and AC5.
- **S3** — Canary. G4: the two negative arms read `AGENTS.md` and the merge-bar guide both.
  Observed by AC6.
- **S4** — Charter text. C5: `[gate]` regains green-by-absence and the exemption rule, `[contract]`
  coupled releases, and the pytest line structural classes and opt-in parallelism. C6: the claim
  note, the CLI message and the runbook say a claim reaches a repository by `govkit update`. C8:
  `[pair]` regains the field rules. C10: the process-monitor line names no flag `reap.py` lacks.
  Observed by AC7.
- **S5** — Gov and the runbook. C2: gov's `kits` gains `runlog` and `process-monitor`. C9: two
  section-2 rules stop overstating. C3: the runbook stops claiming the pytest bug classes stay in
  the charter. C4: `manifest-check.sh`'s retrofit recipe and `README.md` stop sending a reader to
  pull manifest lines into the playbook. R1's runbook half: taking a new template means reseeding it.
  Observed by AC8.

## 3. Non-goals (OUT)

- Teaching `manifest-check.sh` or `run-selftests.sh` a host-aware match; S1 keeps the fleet
  unambiguous for the match they make.
- Rewording frozen backlog rows that cite v3.5 sections.

### Edges

- **consumes-from** `TOOL-aDistilledCharter-5` — both edit `render_playbook.py`; this lands second.
- **consumes-from** `TOOL-aDistilledCharter-6` — both edit `tools/check-playbook-parity.sh`.

## 4. Design

Each item is the fix its finding proposed, narrowed where noted: G3 keeps the whole-file exclusion
of the gate and its self-test, because excluding single lines from a `git grep` needs a second pass
for no reader's benefit, and fixes the one stale citation in the header instead.

### Files touched (estimate)

`tools/playbook/render_playbook.py` · `tools/check-playbook-parity.sh` · `tools/check-playbook-parity.test.sh` · `tools/run-gates/run-gates.gov.test.sh` · `.memory-tree.conf` · `tools/playbook-kit-waivers.txt` · `coding-governance-agents.template.md` · `AGENTS.md` · `.governance/deploy.toml` · `WIRE-INTO-PROJECT.md` · `skills/session-kickoff/manifest-check.sh` · `README.md` · `memory/guides/SESSION-KICKOFF.md`

## 5. Production-readiness checklist

- security — R6 stops a hook's inherited `GIT_DIR` steering the probes at another repository.
- perf / scale — N/A — no measurable change.
- error / empty / loading states — R5 leaves the fleet untouched when a claim would corrupt it.
- observability — every new refusal names its input.
- risks — the wider S4 predicate may red a citation it missed before; the remedy is the handle.
- testing — renderer and parity self-tests; a sliced canary run.
- migration — none.
- user docs — the template, the runbook and the playbook README.

## 6. Acceptance criteria

- **AC1** — When `python tools/playbook/render_playbook.py --selftest` runs, arms for R3, R5, R7 and
  R8 pass. Red when: a second fleet row for `bob` is claimable, a DEL lands in the file, a marker
  passes in `[charter]`, or `--answers` keeps a trailing newline.
- **AC2** — When the selftest runs with `GIT_DIR` exported to this repository's git dir, it still
  passes. Red when: an arm reads the ambient repository.
- **AC3** — When the parity self-test stages `the charter’s §7` (curly), `charter`+NBSP+`§7` and
  `§7 of the charter`, each reds, and `the protocol template's §13` does not. Red when: any miss or
  the false hit.
- **AC4** — When the parity self-test runs a root install with a kit file citing `§1 Landing`, it
  reds. Red when: the root surface misses kit directories.
- **AC5** — When `python3 tools/memory-tree/check-arms.py --emit-floors` runs, the parity gate's
  measurement equals its `ARMS_FLOORS` pin, and `bash tools/check-playbook-parity.sh` counts
  `runlog` documented with no waiver row. Red when: the pin is slack or the waiver remains.
- **AC6** — When a slice of the canary's G4/G5 block runs over an `AGENTS.md` carrying
  `min(8, nproc)`, it fails. Red when: only the guide is read.
- **AC7** — When `grep -c` counts the restored clauses in `coding-governance-agents.template.md`,
  each of C5, C6, C8 and C10 is present, and the render stays inside `ONE_LINE_MAX`. Red when: a
  clause is missing or a line overflows.
- **AC8** — When `grep -n 'runlog' AGENTS.md` runs it prints the tools line, and
  `grep -n 'playbook' skills/session-kickoff/manifest-check.sh` finds no pull-into-the-playbook step.
  Red when: either survives.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `playbook parity` · `playbook parity selftest` · `run-gates gov canary` · `harness arms (fail branches armed or pinned)` · `manifest-check self-test` · `kickoff-manifest ratchet` · `govkit runbook parity` · `line length` · `memory hygiene` · `govkit acceptance matrix` · `recall floor` · `recall floor arms` · `kit/dogfood doc parity` · `transition-audit arms` · `straggler-guard arms` · `scratch-guard self-test` · `lexicon naming predicates`

New arm: tools/playbook/render_playbook.py · covers AC1 AC2 · the BASE claim and probes · none
New arm: tools/check-playbook-parity.test.sh · covers AC3 AC4 · the BASE predicate and surface · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, the batch promoted from the closing review round 1.

## 10. Reuse audit

`reuse_lookup.py "render the node registry table into a charter"` is the set's probe; every item
extends a seam this build already touched: `render_playbook.py`, the parity gate's S2 and S4, the
canary's G4/G5 block and the template.

Recall terms used: `charter template playbook render AGENTS.md section parity size ceiling one-liner rule node registry tag`
