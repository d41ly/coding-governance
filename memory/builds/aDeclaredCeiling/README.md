---
slug: aDeclaredCeiling
node: a
opened: 2026-08-16
streams: playbook+tooling
roster: PLAY+TOOL
ids: PLAY-aDeclaredCeiling-1 TOOL-aDeclaredCeiling-1 TOOL-aDeclaredCeiling-2 TOOL-aDeclaredCeiling-3
---

# aDeclaredCeiling — the ceiling becomes a declaration, and three gaps aSiftedPlaybook left

Node `a` · opened 2026-08-16 · streams playbook+tooling.

`aSiftedPlaybook` landed at `96141ae` and left four follow-ups it named but could not mint: three
because they were genuinely out of its scope, and one because minting it would have redded the bar
it had just turned green. This build is those four, and the fourth is the reason the other three
could not be recorded when they were found.

**The design pass refuted one of them before it was specced.** The follow-up read
"`WIRE-INTO-PROJECT.md:464` calls agent-cap 'the review protocol's TWO rules' against four".
Measured: the line reads "the mechanical enforcement of the review protocol's TWO rules: route
fan-out through the cap-5 helpers, AND a review's verify stage spawns at most 5 agents TOTAL", and
`memory/guides/REVIEW-PROTOCOL.md` binds exactly two rules — its `## The hard cap` and
`## Concurrency` sections. The "four" is `agent-cap.js`'s four implementation RULES, which are a
different population. The claim is correct as written and two landed records say otherwise, so
`PLAY-aDeclaredCeiling-1` records the refutation rather than fixing a defect that does not exist.
That is the same class this whole lineage is about — a claim that drifted from its source — with
the drift in the AUDIT rather than in the subject.

The table below is GENERATED from the status header of every spec in this folder — do not
hand-edit it.

<!-- gen:build-index -->
**Build status:** CLOSED · 4 unit(s) · node a · opened 2026-08-16 · streams playbook+tooling · ids PLAY-aDeclaredCeiling-1 TOOL-aDeclaredCeiling-1 TOOL-aDeclaredCeiling-2 TOOL-aDeclaredCeiling-3

| Unit | Status | Rev | Last change |
|---|---|---|---|
| [PLAY-aDeclaredCeiling-1 — the refuted follow-up, recorded where it was asserted](spec/2026-08-16-spec-PLAY-aDeclaredCeiling-1.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-aDeclaredCeiling-1 — the size ceilings become one declaration with their history beside them](spec/2026-08-16-spec-TOOL-aDeclaredCeiling-1.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-aDeclaredCeiling-2 — the recall corpus reaches a constraint declared in a conf](spec/2026-08-16-spec-TOOL-aDeclaredCeiling-2.md) | CLOSED | rev-2 | 2026-08-16 |
| [TOOL-aDeclaredCeiling-3 — a landed run's frozen region stops being compared to a moving source](spec/2026-08-16-spec-TOOL-aDeclaredCeiling-3.md) | CLOSED | rev-3 | 2026-08-16 |

Records live under `spec/` and `reviews/`.
<!-- /gen:build-index -->

## Units — the authored roster (M2)

One mechanism per unit. The `ids:` key above is an OUTPUT, not this roster.

| # | Unit | Tier | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aDeclaredCeiling-3` | 2 | the terminal-run region comparison |
| 2 | `PLAY-aDeclaredCeiling-1` | 1 | the refuted follow-up, recorded |
| 3 | `TOOL-aDeclaredCeiling-1` | 2 | the ceiling as a declared pin |
| 4 | `TOOL-aDeclaredCeiling-2` | 2 | the recall corpus reaches conf declarations |

**The order is TOTAL, and unit 2 is the reason — not unit 1.** An earlier version of this section
called unit 2 "a records-only correction with no dependency" and justified unit 1 going first by
pointing at units 3 and 4. Both halves were wrong, and the spec audit reproduced it in an isolated
clone.

`PLAY-aDeclaredCeiling-1` rev-bumps a CLOSED `aSiftedPlaybook` spec. That moves the spec's status
header, `gen_build_index` re-renders that build's README table from it, and `aSiftedPlaybook`'s
`RUN.md` — frozen at `LANDED` — no longer matches its source. `UNATTENDED` check 8 reds, and
`--preflight` refuses to refresh a finished record. **Unit 2 has the hard dependency, and it is on
unit 1**: it is not merely convenient for `TOOL-aDeclaredCeiling-3` to land first, it is the only
thing that makes unit 2 landable at all. Units 3 and 4 touch no landed record and would have been
fine in any order.

Unit 4 is last because unit 3 creates a declaration unit 4 must be able to reach. That reason was
also empty in its first form: unit 3's declaration lands at `tools/template-size-limits.txt`, and
unit 4 as first drafted admitted only repo-ROOT confs, so the two units would not have met.
`TOOL-aDeclaredCeiling-2` S1 now takes repo-RELATIVE paths and seeds the limits file among them,
which is what makes the dependency real rather than asserted.

## Coverage — every follow-up to the unit that discharges it

| Follow-up, as `aSiftedPlaybook` recorded it | Disposition |
|---|---|
| `WIRE-INTO-PROJECT.md:464` "TWO rules" against four | **REFUTED** — `PLAY-aDeclaredCeiling-1` records it |
| the ceiling as a declared pin (`TOOL-aSiftedPlaybook-1` §4) | `TOOL-aDeclaredCeiling-1` |
| the recall corpus cannot reach a conf declaration (§10) | `TOOL-aDeclaredCeiling-2` |
| a row minted after LANDED reds unattended check 8 | `TOOL-aDeclaredCeiling-3` |

Nothing is unassigned, and one of the four is discharged by being disproved.

## Build-level rules

- **`memory/DECISIONS.md` is append-only.** Unit 3 changes where the ceiling is DECLARED, not what
  it is; `TOOL-aSiftedPlaybook-1`'s row records the value and stays untouched. If unit 3 also
  changes the value it mints a new row, and it does not.
- **No spec id in this build may be cited from product source while its status is non-terminal.**
  The drift signal `non_terminal_specs_cited_by_product_source` sits AT its pin of 2 with tolerance
  0, and `tools/`, `skills/`, `.claude/`, `memory/guides/SESSION-KICKOFF.md`, the three playbook
  files and `WIRE-INTO-PROJECT.md` are all product globs. `aSiftedPlaybook` took this signal to 4
  by writing two spec ids into `tools/` and had to strip them at close; the rule is repeated here
  because being bitten once is not a mechanism.
- **Every unit that creates a depth-1 `tools/` path carries the `govkit` obligation in §4, §7 and
  an AC.** Derived, never counted — the count went stale twice in the previous build.
- **A kit's behaviour is read from the kit, not inferred from its name.** `aSiftedPlaybook`'s
  closing review found a fabricated `gate-lint` description that had shipped into four carriers
  because nobody opened its README. Any unit here that describes a kit reads it first and says in
  its §10 that it did.
