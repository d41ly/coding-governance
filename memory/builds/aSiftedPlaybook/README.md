---
slug: aSiftedPlaybook
node: a
opened: 2026-08-16
streams: playbook+tooling
roster: PLAY+TOOL
ids: PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3
---

# aSiftedPlaybook — the playbook reconverges again, and its ceiling moves

Node `a` · opened 2026-08-16 · streams playbook+tooling.

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
closed** — the owner kept it OPEN on 2026-08-16, re-justified on readability rather than bytes.

Records live under `spec/` and `reviews/`. The table below is GENERATED from the status header of
every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 7 unit(s) · node a · opened 2026-08-16 · streams playbook+tooling · ids PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-aSiftedPlaybook-1 — the template's claims reconverge with the kits they describe](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-1.md) | SPECCED | rev-4 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-2 — the default branch stops being hardcoded as `main`](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-2.md) | SPECCED | rev-4 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-3 — the playbook learns which kits it ships](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-3.md) | SPECCED | rev-3 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-4 — the companions stop contradicting their own contents](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-4.md) | SPECCED | rev-2 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-1 — the template ceiling moves to 48 KiB, as a recorded rule reversal](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-1.md) | SPECCED | rev-4 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-2 — the size gate's failing case gets observed for the first time](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-2.md) | SPECCED | rev-4 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-3.md) | SPECCED | rev-5 | 2026-08-16 |
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is a reservation range, not this roster.

**Each cell is a label, not a description.** The unit's §1 Goal owns the full statement, and this
table deliberately does not restate it — two cells here drifted from their specs within minutes of
being written (a unit's site count, and a kit count), which is `two-answers-to-one-question`
reproduced inside the build that exists to close it. Read the spec, not the cell.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aSiftedPlaybook-1` | 2 | the ceiling constant and its carriers |
| 2 | `TOOL-aSiftedPlaybook-2` | 2 | the size gate's missing self-test |
| 3 | `PLAY-aSiftedPlaybook-4` | 1 | the companions' self-descriptions |
| 4 | `PLAY-aSiftedPlaybook-1` | 2 | template claims vs the kits |
| 5 | `PLAY-aSiftedPlaybook-2` | 2 | the default-branch placeholder |
| 6 | `PLAY-aSiftedPlaybook-3` | 2 | the unnamed kits · **owns the v2.8 marker bump** |
| 7 | `TOOL-aSiftedPlaybook-3` | 2 | the carrier-parity leg |

**The order is TOTAL, not a set of hints, and units 4-6 are the reason.** All three edit the
template. PLAY-1 and PLAY-2 work from BASE line anchors; PLAY-3 INSERTS about 2 KB into §5, §6 and
§7, above and inside every one of those anchors — including `:107`, the very bullet PLAY-3 adds a
sibling to. Every anchored substitution therefore lands before any insertion. PLAY-1 and PLAY-2 also
both rewrite template `:51`, which carries a "build plan" and two branch senses at once, and
PLAY-1, PLAY-3 and PLAY-4 all edit `customize.md`. An earlier version of this table called PLAY-1
"independent"; it is not, and neither is anything else in the template lane.

`TOOL-3` is last because every other unit changes values it would pin, and it now has a hard
prerequisite: `PLAY-3` S7 seeds the waiver registry `TOOL-3` reads.

## Build-level rules

- **The version marker moves once, at the integration boundary**, not per unit. The template and
  `domain-rules.md` both carry `<!-- governance-template: vN.N -->` and are re-pulled in lockstep, so
  a unit landing a marker bump mid-build would ship a version that describes a partial change.
  **Owner: `PLAY-aSiftedPlaybook-3`, unit 6 — the last template-touching unit in the order above.**
  It carries this as **S8** with **AC7**, naming `parallel-coding-governance.template.md:12`,
  `parallel-coding-governance.domain-rules.md:3` and the v2.7 snapshot. Stating the rule here and
  nowhere else is what round 2 caught as a blocker: the receiving unit was never told, so its
  acceptance criteria would have gone green over a v2.7 marker on v2.8 content. If the order changes,
  the obligation moves with the lane AND the scope item moves with it.
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

## Owner decisions — RESOLVED 2026-08-16

All three build-level forks were put to the owner and answered. Marked in place in each spec's §8.

| Fork | Resolution |
|---|---|
| `TOOL-1` F1 — the gate-leg label | Rename to `template size <=48KiB` and swap `memory/map/baseline.toml:35` **in place**. No dossier minted here. |
| `TOOL-1` F2 — the forcing function | An advisory growth warning in the gate **and** `PLAY-aCandidStub-2` stays OPEN, re-justified on readability. Its *mechanism* was still unsettled here and was resolved in round 2 as a high-water ratchet — see below. |
| `PLAY-2` F1 — the §16 micro-formats | Parameterize both. Byte-stability describes the instantiated document, not the template. |

Three consequences the resolutions created, carried into the specs rather than left implicit:

- **`TOOL-aSiftedPlaybook-2` now mints `memory/map/features/playbook.md`.** `TOOL-1` renames an
  existing key and mints nothing; `TOOL-2` adds the first genuinely NEW leg key, which is an
  addition rather than a rename. `TOOL-3` extends and reds if it is absent.
- **`TOOL-aSiftedPlaybook-3` keeps `baseline.toml`'s unenforced shrink-only rule as a non-goal.**
  The owner relied on that gap deliberately, so a gate enforcing it would red the resolution on the
  day it landed. Enforcing it later needs a waiver for this swap first.
- **At landing, `PLAY-aCandidStub-2`'s backlog row needs rewriting.** It reads "the template is
  effectively FULL at v2.5", which `TOOL-1` falsifies; leaving it would keep the row open for a
  reason that no longer exists, when the actual reason is now per-session reading cost.

### The second round — four more, resolved 2026-08-16

Round 2 of the spec audit rejected the idea that a fork can be withheld as "unit-internal":
`BUILD-METHOD.md` M3 has no such category, and with no standing mandate every fork goes to the
owner. All three withheld ones were put and answered, alongside a blocker the audit surfaced.

| Fork | Resolution |
|---|---|
| `TOOL-1` B2 — the WARN threshold's value | **A high-water ratchet, not a constant.** No fixed value works: every conventional fraction is silent through this whole build, and anything tight enough to price it fires forever. |
| `PLAY-3` F1 — kit bullets | **Inline in the template.** Discoverability over per-session read cost; the ratchet is what prices the next such spend. |
| `TOOL-2` F1 — the `fail()` refactor | **Yes.** The gate enters `check-arms.py`'s population, with a mandatory `ARMS_FLOORS` entry. |
| `PLAY-1` F1 — RULE 4's clause | **§0**, where every session reads it. RULE 4 binds any fan-out, not only a review. |

**Two forks remain OPEN, both in `TOOL-aSiftedPlaybook-3`** — F1 (whether the value-parity pair list
lives inside the gate or in a declared data file) and F2 (whether a kit missing from the playbook
reds or only warns). They are not withheld: that unit is sequenced last, is the one the owner may
defer indefinitely, and both forks are about the gate's own design rather than anything the other
six units depend on. **`TOOL-3` is therefore classified FORKED, not READY**, per `BUILD-METHOD.md`
M2, and cannot be built until they are answered. The other six specs' §8 all read `none` with their
items marked RESOLVED in place.
