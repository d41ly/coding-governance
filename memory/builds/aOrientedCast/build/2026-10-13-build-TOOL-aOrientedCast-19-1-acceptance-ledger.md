# TOOL-aOrientedCast-19 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-19

Direct checks only: no gate, suite, slice or self-test ran in this pass. What ran: the §6 fixture,
a `git init` repository under a short `%TEMP%` path holding a copy of the kit at tools/roles, three
stub harness scripts, a copy of `AGENTS.md`, a conf declaring `MEMORY_ROOT=memory` and
`CHARTER=AGENTS.md`, and build `tFix` with a README and one spec; in it the §6 PROBE and the AC3
probe, `check_roles.py --root ../..` from the kit copy, and `handoff.py render` and `check`, one
staged break at a time and each restored. From the worktree root: the AC7 probes, the AC8 and AC9
greps, `bash -n` over the hygiene script and its self-test, and `lexicon.py --suggest` for both new
function names, which answered OK. Before any break the fixture's checker exited 0 with
`0 stand-in waiver(s), 0 stand-in declaration(s)`. Owed to the main loop at the close (M8): every leg
§7 lists, and the two `New arm:` lines of §7, each RED on its staged break and GREEN once restored:
the `roles catalogue` arm (a tailed stand-in handoff with no row staged under a prompts folder, then a
row with no declaration) and the `memory-hygiene self-test` rf10 arm (the new case staged below
`F:*)`, so check 3 names the stand-in registry). No `.claude/` render is owed: this unit moved no
roles kit carrier.

**Evidences:** TOOL-aOrientedCast-19
- AC1 — `R15` — the good row and the eight staged rows printed `[('tFix', 'gov-builder')]` and eight lines, `role-stand-in-waiver.txt:2` to `:9`, each `R15` and naming in turn four fields, `2026-13-01`, `agent a`, `gov-ghost`, `gov-session` as an agent: false role, `t-Fix`, the empty reason, and the repeat of line 1.
- AC2 — `[]` — with no registry the probe printed `[]` and an empty defect line; with two `#` lines, a blank line and the good row it printed `[('tFix', 'gov-builder')]` and no defect.
- AC3 — `-stand-in.md` — with the rendered tailed declaration, an untailed copy of it and a tailed file with no marker, the scan printed `[('tFix', 'gov-builder')]` and one `R15` line naming the marker-less file.
- AC4 — `1 stand-in declaration(s)` — with the declaration and no registry the checker exited 1 with one `R15` line naming the file, `gov-builder` and `tFix`, summary `0 stand-in waiver(s), 1 stand-in declaration(s)`; with the good row it exited 0, printed `roles: note: stand-in waiver 2026-10-13 owner a gov-builder tFix — this tool exposes no sub-agent primitive` and `1 stand-in waiver(s)`; with the declaration deleted it exited 1 with one `R15` line naming `role-stand-in-waiver.txt:1` as stale.
- AC5 — `MEMORY_ROOT` — with the conf's `MEMORY_ROOT` line deleted the checker exited 2 with one R0 line naming `MEMORY_ROOT`.
- AC6 — `-builder-stand-in.md` — with no registry the render exited 1 naming `memory/project/role-stand-in-waiver.txt`, `gov-builder` and `tFix`, and no prompts folder was created; with the good row it exited 0 printing `memory/builds/tFix/prompts/2026-10-13-prompt-TOOL-tFix-1-1-builder-stand-in.md`, which `handoff.py check` passed with exit 0; `--stdout` beside `--stand-in` exited 2.
- AC7 — `[]` — from the worktree root each probe printed `[]` and an empty defect line.
- AC8 — `F:*)` — the grep printed lines 738, 741 and 752: the pass-order case, the new stand-in case, then `F:*)`.
- AC9 — `grep -c '^KIT_MEMORY_TREE_VERSION=2.147' tools/memory-tree/check-memory-hygiene.sh` — it printed 1, the `gov:kit memory-tree@2.146` grep over the four templates and four renders printed nothing, and the unit's diff touches no `KIT_ROLES_VERSION` or `gov:kit roles@` line, observed on the staged diff before the commit.
