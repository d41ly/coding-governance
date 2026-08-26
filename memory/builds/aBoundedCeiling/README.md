---
slug: aBoundedCeiling
node: a
opened: 2026-08-27
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-2 TOOL-aBoundedCeiling-3 TOOL-aBoundedCeiling-4
---

# aBoundedCeiling — a leg that cannot hang forever, and a landing that pays for the bar once

Node `a` · opened 2026-08-27 · streams tooling · base pinned at preflight.

Started from an owner prompt, recorded verbatim with its measurements at
[the prompt record](prompts/2026-08-27-prompt-TOOL-aBoundedCeiling-1.md). Read that first: every
figure this file leans on is derived there, from `tools/gate-legs.json` and the runner's own
`gate-ledger.tsv`, and none of it is authored twice.

## The goal

**Make the merge bar's cost a VERDICT rather than a complaint, and make a hang a RED rather than a
wedge — in a way that ships to every adopter of the run-gates kit, not just to this repository.**

That sentence is the build's immutable description. Three symptoms, one root: the bar has no bound of
any kind on a single leg, so a leg may take forever and nothing notices, and the only lever anyone has
ever had is to delete legs from the manifest.

## Why the obvious answers are the wrong ones

**Not "make the self-tests faster."** They are 82% of the bar's leg-seconds and the cost is process
creation on an antivirus-fronted machine, which is a property of the node and not of the tree. The
class is already catalogued and it says outright that no portable gate for it can exist. Speeding one
suite is instance work; it does not stop the ninth suite arriving unbounded.

**Not "arm the profile-wide `timeout=`."** One number must cover a 1 s leg and an 1320 s leg. To let
the longest live, the bound has to sit near 2000 s — which converts an infinite hang into a
thirty-three-minute hang and catches nothing else. It fails the one recorded symptom it would have to
catch: a leg silent at 240 s that normally finishes in 812 s.

**Not "delete more legs."** That is the move that produced this situation, and it is the move an
adopter cannot audit.

## The shape of the answer

A ceiling belongs to a LEG, declared where the leg population already lives, and the runner enforces
it as that leg's deadline. One mechanism then does three jobs that currently have zero, one and two
implementations respectively: it bounds a hang, it makes slowness fail, and it refuses a leg that
arrives with no ceiling at all. The remaining two units are about paying for that bar once per landing
instead of twice, and about a forced run keeping the guards that scope it.

## Units

| id | delivers | tier | deps |
|---|---|---|---|
| TOOL-aBoundedCeiling-1 | per-leg wall-clock ceilings in the leg manifest, enforced by the runner | 2 | — |
| TOOL-aBoundedCeiling-2 | one landing pays for one bar, not two | 2 | — |
| TOOL-aBoundedCeiling-3 | a forced full run stops meaning "bypass every guard" | 2 | 2 |
| TOOL-aBoundedCeiling-4 | one ceiling implementation in the tree, not two | 1 | 1 |

**TOOL-aBoundedCeiling-1** is the spine. A leg declares its ceiling in `tools/gate-legs.json`; the
runner passes it to the per-leg deadline it already implements; a breach is a RED naming the leg and
its declared ceiling, never a skip and never a green; a leg with no ceiling reds by that fact. This
closes the open half of `TOOL-aBoundedVerdict-10` and implements charter §7's already-written rule at
the place legs actually run.

**TOOL-aBoundedCeiling-2** — `--close` records a green the push boundary is structurally unable to
accept, so every unattended landing runs the bar twice and the second run is the expensive one.

**TOOL-aBoundedCeiling-3** — `GATE_FULL=1` switches off all 47 guards, so a landing that touched only
`memory/` still pays 45 kit self-test legs. Forcing should select the leg SET; the guards should still
scope it.

**TOOL-aBoundedCeiling-4** — `run-unattended-gates.sh` implements declare-a-ceiling-and-red-on-breach
for eight suites, and unit 1 implements it for eighty-five. Two implementations of one rule is the
drift class this repo gates elsewhere; whether the answer is a shared seam or a deletion is that
spec's to resolve.

## BUILD-LEVEL RULES

Classification per M2 is written here as each unit is classified. All four are MISSING at open — no
spec exists yet.

**Standing constraint, from the prompt record and not re-argued:** no unit may return the unattended
kit's `*.test.sh` legs to `tools/gate-legs.json`. That removal was an owner ruling of 2026-08-23.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aBoundedCeiling-1` | 2 | per-leg wall-clock ceilings in the leg manifest, enforced by the runner |
| 2 | `TOOL-aBoundedCeiling-2` | 2 | one landing pays for one bar, not two |
| 3 | `TOOL-aBoundedCeiling-3` | 2 | a forced full run stops meaning "bypass every guard" |
| 4 | `TOOL-aBoundedCeiling-4` | 1 | one ceiling implementation in the tree, not two |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-08-27 · streams tooling
ids TOOL-aBoundedCeiling-1 TOOL-aBoundedCeiling-2 TOOL-aBoundedCeiling-3 TOOL-aBoundedCeiling-4

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
