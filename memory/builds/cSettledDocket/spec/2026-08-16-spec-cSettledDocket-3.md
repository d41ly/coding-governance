# TOOL-cSettledDocket-3 — a rule called machine-checked that holds for one tier out of two

**Status:** OPEN · rev-1 · 2026-08-16 · node c · Tier-2 · base 1da67d9c · streams tooling

## 1. Goal

`memory/TEMPLATE-SPEC.md` says every §8 fork must be RESOLVED before a spec's status may go
`CLOSED`/`WONTDO`, and it says the rule is **machine-checked**. In
`tools/memory-tree/check-memory-hygiene.sh`, `if (hdr ~ /Tier-1/) next` sits ABOVE both the
terminal-fork assertion and the §9 rev-log assertion, so neither runs on a Tier-1 spec.

The claim is therefore true for Tier-2 specs and false for everything else. That is the same
false-claim class the catalogue exists for, in the file that enforces the catalogue.

Found while closing cBriefedPilot: two Tier-2 specs were refused for a bold-prose §8, and a THIRD
with the identical shape passed — because it was Tier-1.

## 2. Scope (IN)

- **S1** — move the `Tier-1` skip BELOW the terminal-fork assertion and the §9 rev-log assertion, so
  both grade every tier. Everything the skip currently protects — the canonical ten-section compare,
  the §10 body assertion — stays Tier-2-only.
- **S2** — repair the four Tier-1 specs the change reds, by converting each bold-prose resolution to
  the `###` sub-head form `TEMPLATE-SPEC` already sanctions. No status is changed and no fork is
  re-decided; only the shape moves.
- **S3** — arms in `tools/memory-tree/check-memory-hygiene.test.sh`: a Tier-1 terminal spec with an
  unresolved §8 REDS, a Tier-1 terminal spec with a resolved §8 is silent, and a Tier-1 spec whose
  header rev is missing from §9 reds. Each paired with its Tier-2 twin so the arm proves the skip
  moved rather than vanished.
- **S4** — an arm proving the skip still protects what it should: a Tier-1 spec with non-canonical
  `##` sections stays silent.
- **S5** — `TEMPLATE-SPEC.md` keeps its "machine-checked" wording, because after this it is true.

## 3. Non-goals (OUT)

- **Subjecting Tier-1 specs to the section canon.** Tier-1 exists so a small unit can ship without
  the full ten-section apparatus; that is the skip's real purpose and it survives.
- **Re-deciding any fork.** The four repairs are shape-only. A spec whose §8 records a genuinely
  unresolved question would need its status moved, and none of the four does.
- **The §10 reuse-audit body assertion.** It stays Tier-2-only. `TOOL-cBriefedPilot-3` measured that
  a waived reuse-first run is silent on a Tier-1 spec for this reason, and the fix for that is a
  visibility question rather than this one.
- **Auditing every OTHER `next` in the file.** There may be more; this unit fixes the one whose
  documented claim is false, and a sweep is its own row.

## 4. Design

### The measurement, taken twice

Before cBriefedPilot merged main: 4 of 15 Tier-1 terminal specs would fail the §8 rule. After the
46-commit reconcile: **4 of 18** — the Tier-1 population grew by three and the failures did not
move, so the four are a fixed historical set rather than a rate. **0** would fail the §9 rev-log
assertion. The number is re-measured again at build time, because main adds specs continuously and a
repair list that goes stale between spec and build is a repair list that misses files.

The four: `aWrittenMethod-3`, `aWrittenMethod-5`, `cBriefedPilot-9`, `cBriefedPilot-17`.

### Why moving the skip is the fix, not adding a second check

The assertions already exist and are already correct. Nothing needs writing — a `next` needs to move
three assertions later in the same awk program. A second Tier-1-specific check would be a second
implementation of a predicate that already works, which is the shape this repo bans by name.

### Why the repairs are shape-only, and how that is proved

All four write their resolution as a bold prose paragraph rather than a bullet or `###` sub-head.
`TEMPLATE-SPEC` sanctions both forms in as many words; the gate counts bullets and sub-heads. So each
repair is one line changing `**Question — RESOLVED: answer.**` to `### Question — RESOLVED: answer`.
The proof that nothing else moved is a `git diff --stat` showing one changed line per file plus the
prose that follows it.

### Files touched

`tools/memory-tree/check-memory-hygiene.sh` (the `next` moves) ·
`tools/memory-tree/check-memory-hygiene.test.sh` (four arms) · the four spec files ·
`.memory-tree.conf` if `ARMS_FLOORS` moves.

### Alternatives rejected

- **Weakening `TEMPLATE-SPEC`'s wording to "machine-checked on Tier-2".** That makes the document
  true by describing a gap instead of closing one, and the gap is a rule about forks — the thing this
  method treats most carefully.
- **Exempting historical specs by date.** A cutoff would spare the four and keep the rule true going
  forward, but `SPEC_WITNESS_CUTOFF` already shows what that costs: every reader must then know two
  rules and which date each applies to. Four files is cheaper than a permanent second rule.

## 5. Production-readiness checklist

No new dependency, no new leg. One `next` moves; four documents gain a heading. The risk is entirely
in the blast radius, which is measured, enumerated by filename, and re-measured at build time.

## 6. Acceptance criteria

- **AC1** — a Tier-1 terminal spec with a bold-prose §8 makes `check-memory-hygiene.sh` print
  `terminal Status with unresolved §8 Open questions`, where today it is silent.
- **AC2** — a Tier-1 terminal spec whose header `rev-N` is absent from §9 prints
  `not logged in the §9 Revision log`.
- **AC3** — a Tier-1 spec with non-canonical `## ` sections stays SILENT, proving the skip moved
  rather than being deleted.
- **AC4** — `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 over the whole real corpus after
  the four repairs.
- **AC5** — each repair is shape-only: `git diff` on the four spec files shows no `**Status:**` line
  changed.

## 7. Gates

`bash tools/memory-tree/check-memory-hygiene.sh` · `bash tools/memory-tree/check-memory-hygiene.test.sh` ·
`python tools/memory-tree/check-arms.py` · `bash tools/memory-tree/check-verdict-epoch.sh` ·
`bash tools/run-gates.sh`.

## 8. Open questions

none — the one decision was whether to move the skip or date-exempt the four historical specs, and
§4 takes it against the cost of a permanent second rule. The §10 body assertion staying Tier-2-only
is a scope line rather than a fork; `TOOL-cBriefedPilot-3` already records the separate visibility
question it belongs to.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-32`, found when two Tier-2 specs were
  refused for a shape a Tier-1 spec was passing with.

## 10. Reuse audit

Nothing is written. The terminal-fork and §9-rev assertions already exist, already handle both the
`none`/`N/A` opening and the bullet-or-sub-head item forms, and are reused verbatim — the unit moves
one `next` statement. The repair form reuses `TEMPLATE-SPEC`'s already-sanctioned `###` sub-head,
which cBriefedPilot used three times for the same reason, rather than inventing a marker. The arms
reuse the suite's existing Tier-1/Tier-2 fixture pair rather than building a new corpus.
Deliberately NOT reused: `check-verdict-epoch.sh`'s kit-version dating, which would let this change
land without moving `KIT_MEMORY_TREE_VERSION` — the epoch leg exists to force that bump and this
change is exactly the kind it dates.
