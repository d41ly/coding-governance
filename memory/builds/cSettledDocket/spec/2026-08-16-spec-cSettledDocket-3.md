# TOOL-cSettledDocket-3 — a rule called machine-checked that holds for one tier out of two

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-2 · base 1da67d9c · streams tooling

## 1. Goal

`memory/TEMPLATE-SPEC.md` says every §8 fork must be RESOLVED before a spec's status may go
`CLOSED`/`WONTDO`, and it calls the rule **machine-checked**. In
`tools/memory-tree/check-memory-hygiene.sh`, `if (hdr ~ /Tier-1/) next` cuts the awk record before
both the terminal-fork assertion and the §9 rev-log assertion, so neither runs on a Tier-1 spec.

The claim is true for Tier-2 and false for everything else — the false-claim class, in the file that
enforces the catalogue. Found while closing cBriefedPilot: two Tier-2 specs were refused for a
bold-prose §8 and a third with the identical shape passed, because it was Tier-1.

## 2. Scope (IN)

- **S1** — HOIST the §9 rev-log assertion and the terminal-§8 assertion ABOVE the `Tier-1` cut, so
  both run for every tier. `next` is a prefix cut and the two assertions sit AFTER two that must stay
  Tier-2-only, so no placement of the cut produces this: the edit is a block move, not a moved
  statement. §4 records the ordering that forces it.
- **S2** — key both hoisted assertions on the section TITLE, `^## [0-9]+\. Open questions` and
  `^## [0-9]+\. Revision log`, closing on the next `^## `. Keying on the NUMBER is a vacuity in a
  corpus where numbering is tier-conditional by design: non-goal 1 keeps Tier-1 exempt from the
  section canon, so a Tier-1 spec may legally number Open questions anything.
- **S3** — a terminal spec whose Open-questions range never OPENS prints
  `no Open questions section found` rather than nothing. Silence and pass are the same byte today,
  which is why the hole below survived its own acceptance set.
- **S4** — repair the Tier-1 specs the change reds, each by the repair its OWN failure needs, which
  is not one recipe. Measured against the SHIPPED mechanism: three, all §8, in two shapes; see §4.
- **S5** — arms, each paired with its Tier-2 twin so the arm proves the assertion MOVED rather than
  vanished: a Tier-1 terminal spec with an unresolved §8 reds; one with a resolved §8 is silent; one
  whose header rev is missing from §9 reds; one with non-canonical `## ` sections stays silent; and
  **a Tier-1 terminal spec whose Open questions sits at `## 7.` with an unresolved fork REDS** — that
  last arm is the one that distinguishes "the rule runs on Tier-1" from "the rule runs on Tier-1
  specs that happen to be numbered like Tier-2 ones".
- **S6** — `TEMPLATE-SPEC.md` keeps its "machine-checked" wording, which S2 and S3 are what make true.
- **S7** — `KIT_MEMORY_TREE_VERSION` moves, because `check-verdict-epoch.sh` dates this engine's
  verdicts and this is exactly the kind of change it exists to date.

## 3. Non-goals (OUT)

- **Subjecting Tier-1 specs to the section canon.** Tier-1 exists so a small unit can ship without
  the ten-section apparatus. That is the cut's real purpose and it survives — which is precisely why
  S2 cannot key on a section number.
- **The empty-section-body assertion.** It stays Tier-2-only, hoisted past nothing.
- **Re-deciding any fork.** The four repairs are shape-and-record only; no status moves.
- **The §10 reuse-audit body assertion.** Stays Tier-2-only; `TOOL-cBriefedPilot-3` records the
  separate visibility question it belongs to.

## 4. Design

### The ordering that forces a hoist rather than a moved cut

After `if (hdr ~ /Tier-1/) next` the assertions run in this order:

1. the canonical `## ` section compare — Tier-2 only
2. empty section bodies — Tier-2 only
3. the §9 rev-log high-water — should run for every tier
4. the terminal-§8 resolution — should run for every tier

`next` skips everything following it. Placing it after 2 runs 1 and 2 for Tier-1, which non-goal 1
forbids; leaving it where it is keeps skipping 3 and 4. **No placement works.** 3 and 4 move above
the cut. rev-1 of this spec said "nothing needs writing — a `next` needs to move"; that was wrong,
and it was wrong because the claim was made from reading the two assertions rather than the order of
the four.

### The measurement, taken by RUNNING the gate

rev-1 reported "4 of 18 fail §8, 0 fail §9-rev" from a Python reimplementation of the gate's logic.
Re-taken by copying the real script, neutralising line 626's cut, and running it over the corpus:

| Spec | Fails | Repair it needed |
|---|---|---|
| `cBriefedPilot-9` | terminal §8 | bold prose with no sub-head → `###` sub-head |
| `cBriefedPilot-17` | terminal §8 | bold prose with no sub-head → `###` sub-head |
| `aWrittenMethod-3` | terminal §8 | a `###` sub-head that carried no RESOLVED → put it in the head |
| `aWrittenMethod-5` | — | nothing: its §9 became findable once the range keyed on the title |

Two and two, not four and zero — measured with the cut neutralised and the ranges still keyed on
NUMBER. **The shipped mechanism gives a third answer: three, all §8.** Title-keying made
`aWrittenMethod-5`'s Revision log findable, which cleared it outright, and moved `-3` from §9 to §8
by making its Open-questions section visible for the first time. The three repairs are TWO shapes,
not one: a sub-head that carries no RESOLVED is a different defect from prose with no sub-head.

Three measurements, and only the last was taken with the mechanism that shipped. The first came from
a Python reimplementation of the gate; the second from the real gate with half the change; the third
from the whole of it. The lesson the repo already has a name for — a reimplementation of a checker is
not a second opinion on it — extends one step further: a measurement taken against half a mechanism
is not a measurement of that mechanism. The count was right by accident and **the attribution was inverted
for half the files**, so rev-1's single repair recipe could not have cleared two of them and its AC4
was unreachable. The lesson is the one this repo already has a name for: a reimplementation of a
checker is not a second opinion on it. The number is re-taken this way again at build time.

### Why keying on the title is load-bearing, not tidy

The terminal-§8 range opens only on the literal `^## 8\. Open questions`. With no match, the range
stays empty and the assertion is SILENT — indistinguishable from a pass. Tier-1 is canon-exempt, so
a Tier-1 spec may number that section anything; `aWrittenMethod-3` and `-5` are that shape today and
are silent on §8 even with the cut neutralised.

So hoisting alone closes the four current instances and leaves the rule bypassable by any future
Tier-1 spec doing something the same gate explicitly permits — the defect's instances fixed, the
defect intact. S2 keys on the title; S3 makes a never-opened range say so.

### Files touched

`tools/memory-tree/check-memory-hygiene.sh` (block hoist, two range patterns, one new refusal) ·
`tools/memory-tree/check-memory-hygiene.test.sh` (five arms) · the four spec files ·
`.memory-tree.conf` (`ARMS_FLOORS`, `KIT_MEMORY_TREE_VERSION`).

### Alternatives rejected

- **Weakening `TEMPLATE-SPEC` to "machine-checked on Tier-2".** Makes the document true by describing
  the gap instead of closing it, and the gap is about forks.
- **Exempting the four by date.** `SPEC_WITNESS_CUTOFF` shows the cost: a permanent second rule every
  reader must know. Four files is cheaper.

## 5. Production-readiness checklist

No new dependency, no new leg. A block hoist, two range patterns, one refusal, five arms, four
document repairs. `KIT_MEMORY_TREE_VERSION` moves with it. The risk is the blast radius, which is
measured by running the gate, enumerated by filename WITH its required repair, and re-taken at build.

## 6. Acceptance criteria

- **AC1** — a Tier-1 terminal spec with a bold-prose §8 makes `check-memory-hygiene.sh` print
  `terminal Status with unresolved §8 Open questions`, where today it is silent.
- **AC2** — a Tier-1 terminal spec whose header `rev-N` is absent from §9 prints
  `not logged in the §9 Revision log`.
- **AC3** — a Tier-1 terminal spec whose Open questions sits at `## 7.` **and carries an unresolved
  fork** prints the §8 refusal. This is the arm that fails if S2 is skipped, and rev-1 had nothing
  like it.
- **AC4** — a terminal spec with NO recognisable Open-questions section prints
  `no Open questions section found`, so a never-opened range is distinguishable from a resolved one.
- **AC5** — a Tier-1 spec with non-canonical `## ` sections stays SILENT, proving the cut still
  guards the canon.
- **AC6** — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the real corpus after the
  repairs, and each repair matches the row §4's table assigns it.
- **AC7** — `bash tools/memory-tree/check-verdict-epoch.sh` passes, proving
  `KIT_MEMORY_TREE_VERSION` moved with the engine.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/check-memory-hygiene.test.sh` ·
`bash tools/memory-tree/check-verdict-epoch.sh` · `python tools/memory-tree/check-arms.py` ·
`bash tools/run-gates.sh`.

## 8. Open questions

none — the decisions were whether to hoist or date-exempt (§4, against a permanent second rule) and
whether to key on number or title (§4, against a vacuity the corpus's own tier rule creates). Both
are taken and both have an AC that fails if the other choice were made.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-32`.
- rev-3 · 2026-08-16 · built. §4's table corrected to the measurement the SHIPPED mechanism gives —
  three specs, all §8, in two repair shapes — and the unplanned consequence recorded: hoisting §9-rev
  means a Tier-1 spec carrying a rev must log it, so Tier-1's light profile now includes a Revision
  log. The live corpus already complied.
- rev-2 · 2026-08-16 · M4 audit fold. Two blockers and a high: the measurement was taken from a
  Python reimplementation and had the §8/§9 attribution inverted for two of four files; the `next`
  is a prefix cut so the stated mechanism could not produce the stated behaviour; and the §8 range is
  keyed on a section NUMBER in a corpus whose numbering is tier-conditional, so the rule stayed
  bypassable while AC1-AC5 all passed. S2, S3, AC3 and AC4 are new; §4 now carries the per-file
  repair table.

## 10. Reuse audit

The two hoisted assertions are reused verbatim — the unit moves them and rekeys their range openers;
their `none`/`N/A` and bullet-or-sub-head item handling is untouched. The repair forms reuse what
`TEMPLATE-SPEC` already sanctions: a `###` sub-head for a resolution, a §9 log line for a rev. The
arms reuse the suite's existing Tier-1/Tier-2 fixture pair. `check-verdict-epoch.sh` is deliberately
NOT worked around: it exists to force `KIT_MEMORY_TREE_VERSION` when this engine's verdicts change,
and this change is one, so S7 pays it rather than dodging it.
