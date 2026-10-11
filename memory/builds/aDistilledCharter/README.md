---
slug: aDistilledCharter
node: a
opened: 2026-10-09
streams: playbook+tooling+deployer+kickoff
roster: PLAY+TOOL+DEPL+KICK
ids: DEPL-aDistilledCharter-1 DEPL-aDistilledCharter-2 KICK-aDistilledCharter-1 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 PLAY-aDistilledCharter-5 PLAY-aDistilledCharter-6 TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2 TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9
---

# aDistilledCharter — the charter becomes governing practices, adopter rules and a generated block

## The problem this build exists to solve

The charter template has grown into 205 situational, over-described rules at 98.9% of its 48 KiB
ceiling, and the rendered `AGENTS.md` is 54 KB, past the 32 KiB a Codex agent reads. Measured at BASE
`6473ae38`, 44 of the rules are enforced by a gate, 28 are stated in full by a guide or kit README,
17 only carry a deploy answer, and 116 have no other carrier. Separately, a node's registry tag is
the lowest free letter in each repository, so one machine carries different tags in different
adopters and its session slugs stop being disjoint by construction.

## Expected improvements

- The template is three sections: one-line governing practices, this repository's one-line rules,
  and a generated block.
- Every one of the 205 rules has a recorded destination that a check resolves.
- A node carries one tag in every adopter, assigned once by gov's fleet registry.

## Detriments if this is not built

- Every new rule keeps buying bytes under a ceiling that is already full.
- Agents keep reading situational detail they rarely need, ahead of the practices they always need.
- The same machine keeps minting slugs under different tags in different repositories.

## Build-level rules

One mechanism per unit. The renderer units (TOOL-1, TOOL-2) land first; the two relocations
(PLAY-2, PLAY-3) land before the template (PLAY-1) drops what they carry; gov adopts it (PLAY-4);
then citations (TOOL-4) and gate re-keys (TOOL-3); the runbook (DEPL-1) and the kickoff manifest
(KICK-1) last. Gov's own render is red between TOOL-2 and PLAY-4 by construction. Kit versions move
once, after the last unit. Owner decisions, 2026-10-09: section 2 lives in `deploy.toml [charter]`;
adopters re-tag to the fleet registry; the manifest's §B trim is in scope; no spec audit is declared.
The round-1 closing review's blocker folded into TOOL-2; its three HIGH findings became TOOL-5,
TOOL-6 and DEPL-2, and its twenty-two others the one batch TOOL-7. Round 2's blocker retired
DEPL-2 for PLAY-5, and its five others became TOOL-8. Round 3 converged; its six became TOOL-9.

## Parked decisions

- Should the `playbook` entry declare `requires = ["memory-tree"]`? The security checklist and three
  protocol lines need the memory tree. Requiring it refuses a playbook-only adoption; leaving it
  relies on the runbook's "required". Refused: it changes what an adoption may select.
- Should the default selection add `review-harness`, `agent-cap` and `settings-merge`? It would put
  the review protocol and the cap hook in every default adoption. Refused: it installs a settings
  hook in every adopter.
- Should the template's 48 KiB ceiling drop near its 12 KB size? The leg is named for 48 KiB and
  about thirty records cite that name, so lowering it is a rename. Refused: a ceiling is yours.

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aDistilledCharter-1` | CLOSED | the renderer grades one-line regions and renders section 2 from `[charter] adopter_rules` |
| 2 | `TOOL-aDistilledCharter-2` | CLOSED | the fleet registry assigns every node one tag and the renderer generates the node table from it |
| 3 | `PLAY-aDistilledCharter-2` | CLOSED | the review protocol carries the security checklist and the tier definitions the charter drops |
| 4 | `PLAY-aDistilledCharter-3` | CLOSED | the hygiene guide carries the id-minting protocol the charter drops |
| 5 | `PLAY-aDistilledCharter-1` | CLOSED | the charter template v4.0, with a disposition for every v3.5 rule |
| 6 | `PLAY-aDistilledCharter-4` | CLOSED | gov adopts v4.0: its wrapper folds into section 2 and its charter re-renders |
| 7 | `TOOL-aDistilledCharter-4` | CLOSED | every live citation of a charter section number is re-pointed |
| 8 | `TOOL-aDistilledCharter-3` | CLOSED | the parity gate drops the retired pairs, the canary re-points, and a new arm bans section-number citations |
| 9 | `DEPL-aDistilledCharter-1` | CLOSED | the runbook adopts v4.0: section 2, the fleet claim and the re-tag step |
| 10 | `KICK-aDistilledCharter-1` | CLOSED | the kickoff manifest's §B becomes one-liners, every evicted bullet recorded |
| 11 | `TOOL-aDistilledCharter-5` | CLOSED | the node table's paths come from a stated name, identical on every node |
| 12 | `TOOL-aDistilledCharter-6` | CLOSED | the hook README's three bound phrases are compared with the hook again |
| 13 | `DEPL-aDistilledCharter-2` | WONTDO | the review protocol ships with every default adoption |
| 14 | `TOOL-aDistilledCharter-7` | CLOSED | the closing review's medium and low findings, closed as one batch |
| 15 | `PLAY-aDistilledCharter-5` | CLOSED | the security checklist and the tier definitions ship with the memory tree |
| 16 | `TOOL-aDistilledCharter-8` | CLOSED | the closing review's round-2 findings, closed as one batch |
| 17 | `TOOL-aDistilledCharter-9` | CLOSED | the closing review's round-3 findings, closed as one batch |
| 18 | `PLAY-aDistilledCharter-6` | CLOSED | the micro-formats are a section-1 rule that binds every final message |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** CLOSED · 18 unit(s) · node a · opened 2026-10-09 · streams playbook+tooling+deployer+kickoff
ids DEPL-aDistilledCharter-1 DEPL-aDistilledCharter-2 KICK-aDistilledCharter-1 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 PLAY-aDistilledCharter-5 PLAY-aDistilledCharter-6 TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2
ids TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aDistilledCharter-1 — the renderer grades one-line regions and renders section 2 from `[charter] adopter_rules`](spec/2026-10-09-spec-TOOL-aDistilledCharter-1.md) | 1 | 2 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aDistilledCharter-2 — the fleet registry assigns every node one tag and the renderer generates the node table from it](spec/2026-10-09-spec-TOOL-aDistilledCharter-2.md) | 2 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [PLAY-aDistilledCharter-2 — the review protocol carries the security checklist and the tier definitions the charter drops](spec/2026-10-09-spec-PLAY-aDistilledCharter-2.md) | 3 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [PLAY-aDistilledCharter-3 — the hygiene guide carries the id-minting protocol the charter drops](spec/2026-10-09-spec-PLAY-aDistilledCharter-3.md) | 3 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [PLAY-aDistilledCharter-1 — the charter template v4.0, with a disposition for every v3.5 rule](spec/2026-10-09-spec-PLAY-aDistilledCharter-1.md) | 4 | 2 | CLOSED | rev-5 | 2026-10-09 |
| [PLAY-aDistilledCharter-4 — gov adopts v4.0: its wrapper folds into section 2 and its charter re-renders](spec/2026-10-09-spec-PLAY-aDistilledCharter-4.md) | 5 | 1 | CLOSED | rev-2 | 2026-10-09 |
| [TOOL-aDistilledCharter-4 — every live citation of a charter section number is re-pointed](spec/2026-10-09-spec-TOOL-aDistilledCharter-4.md) | 6 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aDistilledCharter-3 — the parity gate drops the retired pairs, the canary re-points, and a new arm bans section-number citations](spec/2026-10-09-spec-TOOL-aDistilledCharter-3.md) | 7 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [DEPL-aDistilledCharter-1 — the runbook adopts v4.0: section 2, the fleet claim and the re-tag step](spec/2026-10-09-spec-DEPL-aDistilledCharter-1.md) | 8 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [KICK-aDistilledCharter-1 — the kickoff manifest's §B becomes one-liners, every evicted bullet recorded](spec/2026-10-09-spec-KICK-aDistilledCharter-1.md) | 9 | 1 | CLOSED | rev-1 | 2026-10-09 |
| [DEPL-aDistilledCharter-2 — the review protocol ships with every default adoption](spec/2026-10-09-spec-DEPL-aDistilledCharter-2.md) | 10 | 2 | WONTDO | rev-2 | 2026-10-09 |
| [TOOL-aDistilledCharter-5 — the node table's paths come from a stated name, identical on every node](spec/2026-10-09-spec-TOOL-aDistilledCharter-5.md) | 10 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aDistilledCharter-6 — the hook README's three bound phrases are compared with the hook again](spec/2026-10-09-spec-TOOL-aDistilledCharter-6.md) | 10 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aDistilledCharter-7 — the closing review's medium and low findings, closed as one batch](spec/2026-10-09-spec-TOOL-aDistilledCharter-7.md) | 11 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [PLAY-aDistilledCharter-5 — the security checklist and the tier definitions ship with the memory tree](spec/2026-10-09-spec-PLAY-aDistilledCharter-5.md) | 12 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [TOOL-aDistilledCharter-8 — the closing review's round-2 findings, closed as one batch](spec/2026-10-09-spec-TOOL-aDistilledCharter-8.md) | 13 | 2 | CLOSED | rev-3 | 2026-10-09 |
| [TOOL-aDistilledCharter-9 — the closing review's round-3 findings, closed as one batch](spec/2026-10-09-spec-TOOL-aDistilledCharter-9.md) | 14 | 2 | CLOSED | rev-1 | 2026-10-09 |
| [PLAY-aDistilledCharter-6 — the micro-formats are a section-1 rule that binds every final message](spec/2026-10-11-spec-PLAY-aDistilledCharter-6.md) | 18 | 1 | CLOSED | rev-1 | 2026-10-11 |
<!-- /gen:build-units -->

Records: 7 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: DEPL-aDistilledCharter-1 DEPL-aDistilledCharter-2 KICK-aDistilledCharter-1 PLAY-aDistilledCharter-1 PLAY-aDistilledCharter-2 PLAY-aDistilledCharter-3 PLAY-aDistilledCharter-4 PLAY-aDistilledCharter-5 TOOL-aDistilledCharter-1 TOOL-aDistilledCharter-2
TOOL-aDistilledCharter-3 TOOL-aDistilledCharter-4 TOOL-aDistilledCharter-5 TOOL-aDistilledCharter-6 TOOL-aDistilledCharter-7 TOOL-aDistilledCharter-8 TOOL-aDistilledCharter-9 PLAY-aDistilledCharter-6.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aDistilledCharter-1` | no |
| 2 | `TOOL-aDistilledCharter-2` | no |
| 3 | `PLAY-aDistilledCharter-2`, `PLAY-aDistilledCharter-3` | yes |
| 4 | `PLAY-aDistilledCharter-1` | no |
| 5 | `PLAY-aDistilledCharter-4` | no |
| 6 | `TOOL-aDistilledCharter-4` | no |
| 7 | `TOOL-aDistilledCharter-3` | no |
| 8 | `DEPL-aDistilledCharter-1` | no |
| 9 | `KICK-aDistilledCharter-1` | no |
| 10 | `DEPL-aDistilledCharter-2`, `TOOL-aDistilledCharter-5`, `TOOL-aDistilledCharter-6` | yes |
| 11 | `TOOL-aDistilledCharter-7` | no |
| 12 | `PLAY-aDistilledCharter-5` | no |
| 13 | `TOOL-aDistilledCharter-8` | no |
| 14 | `TOOL-aDistilledCharter-9` | no |
| 18 | `PLAY-aDistilledCharter-6` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
