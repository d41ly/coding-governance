# PLAY-aMendedFleet-3 — the charter's wiring rule stops stating which file Claude Code reads

**Status:** CLOSED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams playbook · ratified 2026-10-04 · order 94

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The charter template's §6 opens its wiring rule with a vendor fact: writing the charter to
`AGENTS.md` alone "ships a repo Claude Code cannot read, because it does not read that name
natively". Unit 69's F3 probe found that fact stale: Claude Code reads `AGENTS.md` from 2.1.277, but
only in a project with no `CLAUDE.md`, while node a's PATH CLI is 2.1.178 and still does not. The
sentence is now true for some installs and false for others, and it is rendered into this repo's
`AGENTS.md`. The rule itself, one canonical file with thin imports verified by a check, does not
depend on which tool reads which name. This unit replaces the vendor clause with the version-neutral
reason, in the template and its render, so the charter states nothing that the next CLI release can
falsify; the dated fact lives once, stamped, in the agent-instructions kit README, which unit 69
owns.

## 2. Scope (IN)

- **S1** — In `coding-governance-agents.template.md` §6, the first bullet's second and third lines
  change from the vendor clause to the text in §4, and nothing else in the bullet moves. The bullet
  shrinks by 20 bytes, PINNED by a byte count of both versions on 2026-10-04. Observed by AC1 and
  AC3.
- **S2** — `AGENTS.md`'s rendered region is re-rendered with
  `bash tools/playbook/adopt-playbook.sh --target .`, so the render carries the same text and
  nothing else in it moves. Observed by AC2 and AC4.
- **S3** — The kickoff manifest's `last-audit:` line is re-stamped, because the template is on its
  `watch:` list, with a delta line in the commit message. Observed by AC5.

## 3. Non-goals (OUT)

- The agent-instructions kit's README, adopter header and `AGENTS.md` line 14, which state and stamp
  the Claude Code fact. Unit 69 owns them, and this unit points nowhere new.
- Any other §6 bullet, or the template's other stale claims, which other units of this build carry.
- The template's version marker, `governance-template: v3.3`, owed once at the close after the
  build's last template edit, which another unit of this build also makes.
- The template's and the charter's size rows and high-water records. The edit shrinks both files,
  and the high-water ratchet only warns on growth.

### Edges

- **consumes-from** `TOOL-aMendedFleet-69` — its F3 probe result, which established that the vendor
  fact changes with the CLI version, and its stamped kit README, which §1 names as the fact's one
  home once this clause leaves the template.

## 4. Design

### Evidence

Read at the worktree HEAD `8312d315`, whose template and `AGENTS.md` bytes equal base `7af5f564`'s.

- The clause is lines 146 and 147 of the template and lines 215 and 216 of `AGENTS.md`, and
  `git grep` outside the build and archive folders finds it nowhere else, so no checker, test or
  carrier reads its words.
- `bash tools/check-template-size.sh` prints 48193 of 49152 bytes for the template, 959 under, and
  `bash tools/check-template-size.sh AGENTS.md` prints 64344 of 64512, 168 under, both on
  2026-10-04. A replacement must not grow either.
- `tools/line-length-limits.txt` declares 450 for both files; the replacement's two lines are 93 and
  85 characters.
- Unit 69 measured, on 2026-10-04: `anthropics/claude-code` issue 6235 closed COMPLETED on
  2026-08-17, and its changelog adds `AGENTS.md` support at 2.1.277 for projects with no `CLAUDE.md`.

### The replacement

The bullet's lines 2 and 3 today:

```
  filename: writing the filled charter to `AGENTS.md` alone ships a repo Claude Code cannot read,
  because it does not read that name natively. Make ONE file canonical and the others thin imports of
```

After:

```
  filename, and which names a tool reads moves with its version, so one name alone can ship a
  repo some agent never reads. Make ONE file canonical and the others thin imports of
```

### Files touched (estimate)

- `coding-governance-agents.template.md`
- `AGENTS.md`
- `memory/guides/SESSION-KICKOFF.md`

### Alternatives rejected

- **Restate the current fact with its version.** A version-pinned vendor fact in a project-agnostic
  template is the claim that just went stale, and the charter's §6 asks such a claim to carry a
  verified stamp the template has no place for.
- **Point at the agent-instructions kit README.** The bullet is unconditional, and an adopter without
  that kit would carry a dangling pointer; a `kit:` fence inside one bullet costs more bytes than the
  clause it replaces.

## 5. Production-readiness checklist

- security — N/A — prose.
- perf / scale — N/A — the charter shrinks by 20 bytes.
- error / empty / loading states — N/A — no code.
- observability — N/A — no code.
- risks — the render must match the template; AC2 observes it with the renderer's own check.
- testing — AC1 to AC5 directly.
- migration — N/A — an adopter receives the text at its next re-render.
- user docs — the charter is the doc.

## 6. Acceptance criteria

- **AC1** — When `git grep -n "cannot read," -- coding-governance-agents.template.md AGENTS.md` runs
  at the unit's tip it prints nothing, and `grep -c "moves with its version" coding-governance-agents.template.md`
  prints 1.
  Red when: either file still carries the vendor clause.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs at the unit's tip it
  exits 0, and `grep -c "moves with its version" AGENTS.md` prints 1.
  Red when: the template was edited and the render was not, so the check names the region.
- **AC3** — When `bash tools/check-template-size.sh` runs at the unit's tip and at its parent, the
  tip's byte figure is the smaller.
  Red when: the replacement grew the template.
  figure: both byte counts are DERIVED at observation time.
- **AC4** — When `bash tools/check-template-size.sh AGENTS.md` and `bash tools/check-line-length.sh`
  run at the unit's tip, both exit 0.
  Red when: the render outgrew its row or a line its limit.
- **AC5** — When `git diff HEAD~1 HEAD -- memory/guides/SESSION-KICKOFF.md` runs at the unit commit,
  it shows the `last-audit:` line moved.
  Red when: a watched file moved and the manifest stamp did not.

## 7. Gates

`template size <=48KiB` · `charter size` · `playbook render wiring` · `playbook validity gate` · `playbook placeholder catalogue` · `playbook parity` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: none · a prose edit whose only reader is the renderer, which AC2 observes · none

## 8. Open questions

- **F1** — What replaces the vendor clause?
  Options: the current fact with its version; a pointer to the agent-instructions kit README; the
  version-neutral reason. The first rots at the next release, the second dangles where that kit is
  not adopted, and the third states only what the rule needs.
  RESOLVED (agent, 2026-10-04, delegated): the version-neutral reason, per §4.
- **F2** — Is the edit within this run's authority over a governance carrier?
  Options: an owner turn; the run mandate's third answer, which grants the stale-fact fixes in
  governance carriers.
  RESOLVED (agent, 2026-10-04, delegated): within the third answer; this is a stale-fact fix.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from unit 69's F3 probe, the template and `AGENTS.md` at base,
  and both size checks.
- rev-2 · 2026-10-04 · §3 · M2 cross-read: the edge on unit 69 was written `external` for a sibling
  this unit builds after and relies on; it now names `TOOL-aMendedFleet-69`, which declares the
  reciprocal hands-off.

## 10. Reuse audit

No existing seam fits: the change is two lines of prose, rendered by the existing renderer.
`python tools/codebase-map/reuse_lookup.py "the charter template's rule on wiring the governing doc
so every agent reads it"` returned only name-stem neighbours such as `read_text` and `read_conf`,
none of which owns the sentence. Recall returned the clause verbatim in the archived v3.0, v3.1 and
v3.2 template snapshots, so it has stood unchanged since v3.0, and `TOOL-dSettledRoster-1`, that no
path gate reaches `AGENTS.md`, which is why AC1 greps both files. Where the brief and the tree
disagree: the roster names this unit as stating what each tool reads today; the spec states the
version-neutral reason instead, per §8 F1, and leaves the dated fact to unit 69's stamped README.

Recall terms used: `python tools/memory-recall/query.py "why does the charter say an AGENTS.md-only
repo ships a repo Claude Code cannot read" --terms "AGENTS.md CLAUDE.md import canonical wiring
governing doc charter template agent-instructions natively Claude Code reads"`
