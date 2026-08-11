---
slug: aSiftedPlaybook
node: a
opened: 2026-08-11
streams: playbook+tooling
roster: PLAY+TOOL
ids: PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3
---

# aSiftedPlaybook — the playbook reconverges again, and its ceiling moves

Node `a` · opened 2026-08-11 · streams playbook+tooling.

A read-only audit of the three shipped `parallel-coding-governance*.md` files at template v2.7
confirmed eleven defects and refuted eight suspected ones. The owner then ordered two things: spec
the fixes, and **raise the template size gate from 32 KiB to 48 KiB**.

The second order reverses a rule this repo currently states in four carriers and calls
non-negotiable. It is specced here as an explicit, recorded rule reversal rather than a constant
edit, because the rule has been cited as a binding constraint by at least three prior units —
`PLAY-aCandidStub-1` §3 named "raising the 32 KiB template gate" as an explicit non-goal, and
`TOOL-aGuardedTally-1` parked a §-stub it could not land, writing that "the gate is right to
refuse". A constant quietly changed under those records leaves them reading as current guidance.

The raise also **removes the funding constraint** that shaped the audit's original sequencing.
Measured at BASE `91ef1b05`: 32682 of 32768 bytes, 86 free, so every fix had to be funded by
externalizing prose. At 49152 the same file has 16470 free and the fixes land on their own merits.
Both figures are BASE-time snapshots — every unit re-measures from the gate rather than carrying a
number out of this paragraph. `PLAY-aCandidStub-2` (externalize §14) is therefore **decoupled, not
closed** — see the owner menu below.

Records live under `spec/` and `reviews/`. The table below is GENERATED from the status header of
every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 7 unit(s) · node a · opened 2026-08-11 · streams playbook+tooling · ids PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-aSiftedPlaybook-1 — the template's claims reconverge with the kits they describe](spec/2026-08-11-spec-PLAY-aSiftedPlaybook-1.md) | SPECCED | rev-2 | 2026-08-11 |
| [PLAY-aSiftedPlaybook-2 — the default branch stops being hardcoded as `main`](spec/2026-08-11-spec-PLAY-aSiftedPlaybook-2.md) | SPECCED | rev-1 | 2026-08-11 |
| [PLAY-aSiftedPlaybook-3 — the playbook learns which kits it ships](spec/2026-08-11-spec-PLAY-aSiftedPlaybook-3.md) | SPECCED | rev-1 | 2026-08-11 |
| [PLAY-aSiftedPlaybook-4 — the companions stop contradicting their own contents](spec/2026-08-11-spec-PLAY-aSiftedPlaybook-4.md) | SPECCED | rev-1 | 2026-08-11 |
| [TOOL-aSiftedPlaybook-1 — the template ceiling moves to 48 KiB, as a recorded rule reversal](spec/2026-08-11-spec-TOOL-aSiftedPlaybook-1.md) | SPECCED | rev-1 | 2026-08-11 |
| [TOOL-aSiftedPlaybook-2 — the size gate's failing case gets observed for the first time](spec/2026-08-11-spec-TOOL-aSiftedPlaybook-2.md) | SPECCED | rev-1 | 2026-08-11 |
| [TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked](spec/2026-08-11-spec-TOOL-aSiftedPlaybook-3.md) | SPECCED | rev-2 | 2026-08-11 |
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

**Each cell is a label, not a description.** The unit's §1 Goal owns the full statement, and this
table deliberately does not restate it — two cells here drifted from their specs within minutes of
being written (a unit's site count, and a kit count), which is `two-answers-to-one-question`
reproduced inside the build that exists to close it. Read the spec, not the cell.

| Unit | Tier | Mechanism | Order |
|---|---|---|---|
| `TOOL-aSiftedPlaybook-1` | 2 | the ceiling constant and its carriers | first |
| `TOOL-aSiftedPlaybook-2` | 2 | the size gate's missing self-test | after TOOL-1 |
| `TOOL-aSiftedPlaybook-3` | 2 | the carrier-parity leg | last |
| `PLAY-aSiftedPlaybook-1` | 2 | template claims vs the kits | independent |
| `PLAY-aSiftedPlaybook-2` | 2 | the default-branch placeholder | after TOOL-1, after PLAY-4 |
| `PLAY-aSiftedPlaybook-3` | 2 | the unnamed kits | after TOOL-1 |
| `PLAY-aSiftedPlaybook-4` | 1 | the companions' self-descriptions | before PLAY-2 |

## Build-level rules

- **The version marker moves once, at the integration boundary**, not per unit. The template and
  `domain-rules.md` both carry `<!-- governance-template: vN.N -->` and are re-pulled in lockstep, so
  a unit landing a marker bump mid-build would ship a version that describes a partial change. The
  last unit to land bumps both to **v2.8** and archives a v2.7 snapshot under `memory/archive/`.
- **Every template-touching unit re-measures.** `bash tools/check-template-size.sh` is an acceptance
  item in each, read FROM the gate, never carried between specs as a remembered number.
- **`memory/DECISIONS.md` is append-only.** The ceiling reversal supersedes prior records by minting
  a new id that names them; it never edits them.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` sits AT its pin of 2 with tolerance
  0. Its `PRODUCT_GLOBS` are `tools/`, `skills/`, `.claude/`, the three playbook files and
  `WIRE-INTO-PROJECT.md` — which means the very files these units edit are product source, and a
  spec id written into the template as provenance reds the bar. `AGENTS.md` and `memory/` are
  outside the globs and may cite freely.

## Owner decision menu

1. **`PLAY-aCandidStub-2` (externalize template §14) — keep open, or close as WONTDO?** The raise
   removes its funding rationale entirely. The remaining argument is readability, not bytes: §14 is
   1899 bytes of a document an agent reads every session, and the 32 KiB gate was a proxy for that
   cost rather than an end in itself. **Recommendation: keep OPEN, re-justified on readability.**
   Raising the ceiling answers "does it fit"; it does not answer "should an agent read it every
   session", and nothing else in the repo now asks that question.
2. **What replaces the forcing function?** At 32768 with 86 bytes free, every template edit was
   priced. At 49152 nothing prices them until 16470 bytes have been spent. `TOOL-aSiftedPlaybook-3`
   is the nearest replacement but it gates *correctness*, not *size*. Options are in that unit's §8.
3. **The §16 micro-format fork** — whether a MANDATORY byte-stable output format may contain a
   placeholder at all. Stated and argued in `PLAY-aSiftedPlaybook-2` §8; it is a genuine fork and is
   the owner's, not the agent's.
