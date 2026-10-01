# TOOL-dDerivedDocket-14 — rotation-note check for shards-mode archives

**Status:** WONTDO · rev-1 · 2026-09-14 · node d · Tier-1 · base abac6d59 · streams tooling · order 14 · superseded by TOOL-cSpliceWarden-2, CLOSED before this build's BASE

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-6-spec-audit-g2-round1.md) | spec-audit | TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 |

<!-- /gen:spec-records -->

## 1. Goal

Design unit U0 asked hygiene check 10 to reach backlog archives for adopters that stay in shards
mode: resolve a rotated backlog archive's live index through the declared families, admit the
same-day `b` suffix, and announce a skip instead of taking it in silence. Regrounded at BASE, all of
it already shipped in the memory-tree kit, so this unit is retired rather than built twice.

## 2. Scope (IN)

N/A — retired; nothing is built. §4 maps each item design U0 named to the BASE code that already
carries it, and §6 re-observes that mapping.

## 3. Non-goals (OUT)

- No change to check 10, its self-test arms or `ROTATED_ARCHIVE_ERE`. Each is `TOOL-cSpliceWarden-2`'s
  and `TOOL-cSpliceWarden-3`'s, landed and closed.
- No change for builds mode. After the switch-over the three backlog archives are deleted (owner
  ruling D8), and a tracked backlog archive becomes a check 9 verdict owned by units 7 and 8.
- No adopter action. Adopters receive the landed check 10 with their next memory-tree kit upgrade.

## 4. Design

### Design U0, item by item, against BASE

| Design U0 asked for | Where it is at `abac6d59` | Landed by |
|---|---|---|
| resolve a backlog archive's live index through the families, not at `<M>/<stem>.md` | the basename resolution anywhere under the memory root outside `archive/`, `tools/memory-tree/check-memory-hygiene.sh:1076-1080` | `TOOL-cSpliceWarden-2` S1 |
| admit the same-day `b` suffix | `ROTATED_ARCHIVE_ERE`'s `[a-z0-9]*` after the date, derived from `FAMILIES`, `tools/memory-tree/check-memory-hygiene.sh:268` | `TOOL-cSpliceWarden-2` S3 |
| announce a skip instead of `continue` | a stem resolving to zero or several indexes is a named finding, `tools/memory-tree/check-memory-hygiene.sh:1081-1085` | `TOOL-cSpliceWarden-2` S2 |
| gov's own archives referenced in the index preamble | the preamble window, `tools/memory-tree/check-memory-hygiene.sh:1086-1087`, and the notes on lines 4 and 5 of `memory/backlog/TOOL.md` | `TOOL-cSpliceWarden-2` S4 and `TOOL-cSpliceWarden-4` |
| staged RED first | the backlog-archive arms in `tools/memory-tree/check-memory-hygiene.test.sh:1740-1791` | `TOOL-cSpliceWarden-2` S5 |

Design U0 also claimed to close `TOOL-cTracedPromise-6` and `TOOL-aBoundedVerdict-9` for adopters.
Both read CLOSED in `memory/backlog/TOOL.md` at BASE, the second as superseded by the first.

### Why retire and not re-scope

The only work U0 could still do is duplicate what `TOOL-cSpliceWarden-2` shipped, and the spec brief
for this build says to retire it in exactly that case. The design's §6 table also asked that check
10's silent `continue` announce; that is the third row above and is gone at BASE.

## 5. Production-readiness checklist

- security — N/A: nothing is built.
- perf / scale — N/A: nothing is built.
- error / empty / loading states — N/A: nothing is built.
- observability — N/A: nothing is built.
- risks — the regrounding could be wrong; §6 re-observes it so a reviewer can refute it cheaply.
- testing — N/A: the arms already exist and are cited in §4.
- migration — N/A: nothing is built.
- user docs — N/A: nothing is built.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh --print-rotated-archive-ere` runs at
  BASE, the printed pattern admits `memory/archive/TOOL.2026-08-17b.md`.
  Red when: the pattern still anchors `<date>\.md$`, so the same-day archive is never enumerated and
  this retirement is wrong.
- **AC2** — When `grep -n "resolves to 0 live index" tools/memory-tree/check-memory-hygiene.test.sh`
  runs at BASE, it finds the arm that fails when check 10 skips an unresolved archive in silence.
  Red when: the arm is absent, so a skipped archive still prints what a referenced one prints.
- **AC3** — When `git grep -n "TOOL-cSpliceWarden-2" -- memory/builds/cSpliceWarden/spec` runs at
  BASE, its spec header reads CLOSED.
  Red when: the superseding unit is not landed, so this retirement points at unfinished work.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

- **F1 — build design U0, or retire it?** Building it would re-land `TOOL-cSpliceWarden-2`'s four
  fixes over code that already carries them. RESOLVED (agent, 2026-09-14, delegated): retire, as the
  spec brief directs when regrounding finds check 10's backlog blindness closed.

## 9. Revision log

- rev-1 · 2026-09-14 · initial record, retired at authoring: every item design U0 named is on BASE.

## 10. Reuse audit

The seam is check 10 as it stands; nothing is added. `python tools/codebase-map/reuse_lookup.py
"rotation note check on archive files referenced on the first lines"` returned generic `check`
functions and `build_reference_index`, and reports `.sh` unscanned, so it cannot see check 10 at
all; the source and the recall hits were read instead. Recall returned `TOOL-cSpliceWarden-6`,
`TOOL-cSpliceWarden-1` and `TOOL-cTracedPromise-6`, which together record check 10's four defects,
their fix, and the declared `ROTATION_MODE` it now sits beside. Where the design and BASE disagree:
design §6 and §15 describe check 10 at `09a22d2b` with a fixed-path resolution and a silent
`continue`; both were removed by `TOOL-cSpliceWarden-2` before `abac6d59`.

Recall terms used: `check-10 rotation note archive backlog FAMILIES suffix ROTATION_MODE cut announce
skip`
