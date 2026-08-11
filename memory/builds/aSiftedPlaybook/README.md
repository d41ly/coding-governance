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

The raise also **removes the funding constraint** that shaped the audit's original sequencing. At
32768 the template had 86 bytes free and every fix had to be funded by externalizing prose; at
49152 it has 16470, and the fixes land on their own merits. `PLAY-aCandidStub-2` (externalize §14)
is therefore **decoupled, not closed** — see the owner menu below.

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
| [TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked](spec/2026-08-11-spec-TOOL-aSiftedPlaybook-3.md) | SPECCED | rev-1 | 2026-08-11 |
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

| Unit | Tier | Mechanism |
|---|---|---|
| `TOOL-aSiftedPlaybook-1` | 2 | The ceiling moves 32768 → 49152, in the gate constant and in every carrier that states it, including the gate-leg label and the codebase-map inventory key that label is. |
| `TOOL-aSiftedPlaybook-2` | 2 | The size gate's failing case gets observed for the first time — it ships today with no self-test and no `ARMS_FLOORS` entry, which the repo's own domain-rules §7 forbids. |
| `TOOL-aSiftedPlaybook-3` | 2 | A carrier-parity leg: every kit under `tools/` is named in the playbook or declared exempt, and no count stated in the trio contradicts its source. The class-level fix; **sequenced last**, because every other unit changes the values it would pin. |
| `PLAY-aSiftedPlaybook-1` | 2 | The template's claims about the kits reconverge with the kits — eight defects, two of which make the ruleset prescribe behaviour the hook denies. |
| `PLAY-aSiftedPlaybook-2` | 2 | `{{DEFAULT_BRANCH}}` becomes the 37th placeholder; the template stops hardcoding `main` in seventeen places, two of which are MANDATORY byte-stable micro-formats. |
| `PLAY-aSiftedPlaybook-3` | 2 | The four shipped-but-unnamed kits — `drift-audit`, `pytest-parallel-guardrails`, `agent-instructions`, `gate-lint` — get template coverage and a customize conditional row each. |
| `PLAY-aSiftedPlaybook-4` | 1 | The companions' self-descriptions stop contradicting their own contents: the placeholder arithmetic, the false disjointness guarantee, and the drop-shape claim. |

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
