---
slug: dLandedVerdict
node: d
opened: 2026-08-19
streams: tooling
roster: TOOL
ids: TOOL-dLandedVerdict-1 TOOL-dLandedVerdict-2
---

# dLandedVerdict — a spec that landed and never said so

Node `d` · opened 2026-08-19 · streams tooling.

`memory/LIVE.md` is generated from spec status headers, so it is only as true as those headers. At
BASE `098bebd` it lists 17 builds. A ground-truth pass over all 17 — artifact-level verification at
`main`, every LANDED claim then handed to a skeptic told to refute it — found **14 of them have
their product work on `main` already**. Only three are honestly not-landed: `aBoundedVerdict`,
`aPortableWarden`, `aFerriedDossier`.

The repo has two drift signals that exist to catch exactly this and neither does. Their shared
docstring in `tools/drift-audit/drift_report.py` claims they "cover both ways a status can lie about
git". They do not:

| signal | asks | why it misses this |
|---|---|---|
| `non_terminal_specs_cited_by_product_source` | is a non-terminal spec's id cited in product SOURCE? | reads source files, not history — sees 2 specs where 20 have their id in a landing commit |
| `closed_specs_with_no_product_commit` | does a CLOSED spec have a product commit? | the opposite direction entirely |

Neither asks the question this build asks: **is a spec still non-terminal although its unit's work
already landed?**

## What this build decided

**"Landed" and "closeable" are different predicates, and the signal only claims the first.** The
refutation pass is what forced this. Five builds landed their code and must still NOT be closed:
`aSealedCaravan` (a DoD naming three legs, not all present), `aTetheredConvoy` (unit 7 unlanded),
`bConvergentLodestar` (unit 1 unlanded), `aMendedLedger` (owner-reserved decisions never ratified),
`aQuarriedLantern` (the record forbids closure and a gate enforces it). No predicate over git
history or record bindings can separate those five from the nine that are genuinely closeable —
that separation needs a human read of a DoD. A signal that claimed otherwise would be wrong five
times out of fourteen.

So the signal reports CANDIDATES and never gates. `gateable: False`, a shrink-only pin, the posture
`live_backlog_rows_per_shard` and `shrink_only_lists_not_shrinking` already use. The alternative was
priced and refused: `drift-audit records` is an UNGUARDED merge-bar leg, so a gateable version turns
five legitimately-open builds into a standing refusal with no escape short of a waiver registry this
build would also have to invent.

**The predicate is id-keyed, not slug-keyed.** Three candidates were measured against the real tree
(46 non-terminal specs) before one was chosen:

| predicate | flags | why not |
|---|---|---|
| unit id in a product commit subject | 20/46 | **chosen** — misses records-only units, and those misses are honest |
| slug in a product commit subject | 37/46 | reproduces the upstream 107/126 over-flag; `aSealedCaravan`'s genuinely-open unit is flagged via its CLOSED sibling |
| `**Serves:** diff-review <id>` | 15/46 | misses `aTetheredRecord`, `cKeyedLaunchpad` and `aTimedTurnstile` — their closing reviews were filed as `spec-audit` |

The slug arm is not a fresh finding: `drift_report.py:298-303` already records that slug-keying was
tried upstream and over-flagged 107 of 126, because every id of a build shares its slug. The
measurement here reproduces it rather than rediscovering it.

**The signal ships BEFORE the close-out that drains it.** A predicate is run before it is trusted,
not after, and seeding the pin against a corpus already cleaned would certify nothing.

## The two units

**U1** — the signal `landed_specs_left_non_terminal` in `tools/drift-audit/drift_report.py`, its
pin in `drift_signals.py`, its `RATCHETS` row, and its arms in `selftest.py`. Report-only. The pin
is seeded at whatever it measures at BASE.

**U2** — the close-out: the 7 confirmed-closeable builds' 23 spec headers go terminal, their build
READMEs follow, `memory/LIVE.md` is re-rendered, and the 9 matching backlog rows close. U1's pin
drops by construction, and that drop is U2's acceptance.

Two builds inside the confirmed-landed set are deliberately EXCLUDED from U2: `aWalkedCorpus`, whose
one non-terminal spec is `DEFERRED` — a chosen state, not an oversight — and `aDeployScout`, a
research record carrying no status header at all.

<!-- roster:units -->

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-dLandedVerdict-1` | 2 | the report-only drift signal for a spec that landed and stayed non-terminal, and its pin |
| 2 | `TOOL-dLandedVerdict-2` | 1 | the close-out of the confirmed-closeable builds, which drops U1's pin by construction |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** INPROGRESS · 2 unit(s) · node d · opened 2026-08-19 · streams tooling
ids TOOL-dLandedVerdict-1 TOOL-dLandedVerdict-2

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dLandedVerdict-1 — the signal for a spec that landed and never said so](spec/2026-08-19-spec-TOOL-dLandedVerdict-1.md) | — | 2 | INPROGRESS | rev-1 | 2026-08-19 |
| [TOOL-dLandedVerdict-2 — the close-out: seven builds that landed and never said so](spec/2026-08-19-spec-TOOL-dLandedVerdict-2.md) | — | 1 | INPROGRESS | rev-1 | 2026-08-19 |
<!-- /gen:build-units -->

Records: 1 bound to this build, across 2 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dLandedVerdict-1 TOOL-dLandedVerdict-2.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->