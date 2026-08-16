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
confirmed eleven defects and refuted **eight** suspected ones (nine were listed as refuted; round 3
withdrew one). The owner then ordered two things:
spec the fixes, and **raise the template size gate from 32 KiB to 48 KiB**.

The audit itself is committed at
[`build/2026-08-16-build-aSiftedPlaybook-1-playbook-audit.md`](build/2026-08-16-build-aSiftedPlaybook-1-playbook-audit.md)
with every defect and every refutation enumerated. It was previously summarised here and nowhere
else, which made completeness against the commissioning input unfalsifiable — only five of the
eleven carried ids anywhere, and a later session could not tell a dropped defect from one that never
existed. The figure has now moved twice for the same reason: it read "eight" until enumeration
forced it to nine (three count-claims collapsed into one bullet), then back to eight when round 3
withdrew R2 — the companion carries 14 placeholders, not 13, so that suspicion was correct all
along. Exactly the class of summary figure the report replaces.

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

The table below is GENERATED from the status
header of every spec in this folder — do not hand-edit it.

<!-- gen:build-index -->
**Build status:** SPECCED · 7 unit(s) · node a · opened 2026-08-16 · streams playbook+tooling · ids PLAY-aSiftedPlaybook-1 PLAY-aSiftedPlaybook-2 PLAY-aSiftedPlaybook-3 PLAY-aSiftedPlaybook-4 TOOL-aSiftedPlaybook-1 TOOL-aSiftedPlaybook-2 TOOL-aSiftedPlaybook-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-aSiftedPlaybook-1 — the template's claims reconverge with the kits they describe](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-1.md) | SPECCED | rev-8 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-2 — the default branch stops being hardcoded as `main`](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-2.md) | SPECCED | rev-7 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-3 — the playbook learns which kits it ships](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-3.md) | SPECCED | rev-10 | 2026-08-16 |
| [PLAY-aSiftedPlaybook-4 — the companions stop contradicting their own contents](spec/2026-08-16-spec-PLAY-aSiftedPlaybook-4.md) | SPECCED | rev-4 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-1 — the template ceiling moves to 48 KiB, as a recorded rule reversal](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-1.md) | SPECCED | rev-10 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-2 — the size gate's failing case gets observed for the first time](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-2.md) | SPECCED | rev-10 | 2026-08-16 |
| [TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked](spec/2026-08-16-spec-TOOL-aSiftedPlaybook-3.md) | SPECCED | rev-12 | 2026-08-16 |

Records live under `spec/`, `build/` and `reviews/`.
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

## Coverage — every audit defect to the scope item that fixes it

Derived from the committed audit report, not from recollection. `A*` are the eleven the audit
confirmed; `B*` were found or re-adjudicated after it closed and are NOT part of that count. **The
rows below ARE the `B*` enumeration and no count of them is stated** — the number said four while
the table carried six, one line apart, in the section this build declares authoritative for
completeness.

| Defect | Sev | Fixed by |
|---|---|---|
| A1 the `agent-cap` matcher value | high | `PLAY-1` S2 |
| A2 the hardcoded default branch, 17 sites | high | `PLAY-2` S1-S3 |
| A3 the false disjointness guarantee | high | `PLAY-4` S1, S2 |
| A4 two of four hook rules described | med | `PLAY-1` S3 |
| A5 the "19-check" count | med | `PLAY-1` S4 |
| A6 `drift-audit` named nowhere | med | `PLAY-3` S1 |
| A7 "build plan" vs "build folder" | med | `PLAY-1` S5 |
| A8 `pytest-parallel-guardrails` named nowhere | low-med | `PLAY-3` S2 |
| A9 `agent-instructions` named nowhere | low-med | `PLAY-3` S3 |
| A10 the §1→§8 circular landing reference | low | `PLAY-1` S6 |
| A11 the companion header's drop-shape claim | low | `PLAY-4` S3 |
| B1 the ≤6 lens array the hook denies | high | `PLAY-1` S1 |
| B2 §157's pre-1.3 enforcement reach | med | `PLAY-1` S8 |
| B3 §0's concurrency-only cap summary | low | `PLAY-1` S7 |
| B4 `gate-lint`, a fourth unnamed kit | med | `PLAY-3` S4 |
| B5 `govkit`, a twelfth kit arriving from main mid-build | med | `PLAY-3` S9 |
| B6 the companion carries 14 placeholders, not 13 | med | `PLAY-4` S4 |

`B5` post-dates the audit report. **`B6` does not** — it is the report's own `R2`, carried there as
a REFUTED suspicion and re-adjudicated in place ("REFUTATION WITHDRAWN 2026-08-16", round-3 H10), so
it is a report row whose verdict moved rather than a post-audit find. `B6` also closes the second
clause of the tracked OPEN backlog row `PLAY-aSealedCaravan-1`, whose first clause is `A3`; that row
was never cited by this build until round 3 found it, and it needs a disposition at landing.

Nothing is unassigned, and no scope item claims an audit provenance it does not have.

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
  0. Its `PRODUCT_GLOBS` are `tools/`, `skills/`, `.claude/`, **`memory/guides/SESSION-KICKOFF.md`
  by FILE path**, the three playbook files and `WIRE-INTO-PROJECT.md` — which means the very files
  these units edit are product source, and a spec id written into the template as provenance reds the
  bar. `AGENTS.md` and `memory/` are outside the globs **except that one manifest file**, which five
  of seven units re-stamp. An earlier version of this rule omitted it and said `memory/` was wholly
  outside, which would have let a unit write a non-terminal spec id into a file sitting at a
  zero-tolerance pin.

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

### The last two, resolved under delegated authority 2026-08-16

The owner delegated resolver authority for `TOOL-aSiftedPlaybook-3`'s two forks. Both are marked
`RESOLVED (agent, 2026-08-16, delegated)` — never `(owner, …)`, since the owner made the delegation
and not the picks, and the two must stay distinguishable afterwards.

| Fork | Resolution | On what grounds |
|---|---|---|
| `TOOL-3` F1 — pair list in the gate or in a data file | **In-script** | M3 tie-break, clause two: reuse of a seam M5 found. §10 already names `kit-dogfood-parity.PAIRS`; a data file would reuse nothing and split one mechanism across two files. Revisit trigger stated. |
| `TOOL-3` F2 — does a missing kit red or warn | **Red** | M3 veto 1: AC1 already read "the gate reds naming that kit", so warn-only contradicted the spec's own acceptance criterion. The fork had been closed since AC1 was written. |

Resolving F2 exposed a contradiction across three places: the waiver registry was described as
shrink-only while a red makes it the escape hatch, and a shrink-only file cannot gain the row an
experimental kit needs. It is now a declared exemption list draining through `TOOL-3` AC6's two
arms — kit gone, or kit named in the playbook — which is also the one deliberate divergence from
`tools/install-prefix-waivers.txt`.

**Every fork in this build is now resolved.** All seven specs' §8 read `none` with their items
marked in place, so no unit is classified FORKED.
