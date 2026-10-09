# KICK-aDistilledCharter-1 — the kickoff manifest's §B becomes one-liners, every evicted bullet recorded

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-1 · base 6473ae38 · streams kickoff · order 9

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`memory/guides/SESSION-KICKOFF.md` §B has grown the same disease as the charter: paragraph bullets
of situational rules, several restating what a gate's refusal already says. This unit cuts §B to
one-line bullets, each a pointer or a trap, and records where every evicted bullet went.

## 2. Scope (IN)

- **S1** — Every §B bullet above the pointer map is one line, or leaves. A leaving bullet goes to
  the gotcha catalogue when it names a recurring class, or is deleted when a gate's refusal or a
  guide states it; the build record lists each with its fate. Observed by AC1 and AC2.
- **S2** — The pointer map, gate commands, tier rule, id protocol, dated corrections and traps keep
  their sections; their text moves only where it cites v3.x section numbers. Observed by AC1.
- **S3** — `last-audit` and `last-body-change` re-stamp in the same commit. Observed by AC3.

## 3. Non-goals (OUT)

- `skills/session-kickoff/MANIFEST-TEMPLATE.md` and the checker. This is gov's own manifest only.
- The sealed §A task skeleton, which check 10 byte-compares.

## 4. Design

### Files touched (estimate)

`memory/guides/SESSION-KICKOFF.md` · `memory/gotchas/`

## 6. Acceptance criteria

- **AC1** — When `awk` counts the continuation lines between §B's first bullet and the pointer map
  heading, the count is zero. Red when: a bullet wraps.
- **AC2** — When the build record's `## Evictions` table is read, every §B bullet of BASE has a row
  with a fate. Red when: one is missing.
- **AC3** — When `bash skills/session-kickoff/manifest-check.sh` runs, it exits 0.
  Red when: a stamp is stale.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
