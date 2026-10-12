# KICK-aOrientedCast-2 — acceptance ledger

**Serves:** journal KICK-aOrientedCast-2

Direct checks only; no gate, suite or bar ran in the pass. AC1 and AC3 to AC11 ran in the worktree
on the staged tree; AC2 ran in a fixture repository at `%TEMP%/kc2` holding the pass's template,
adopter, catalogue and conf; AC12 ran in a `git clone --local` of the worktree at `%TEMP%/kx2` with
the pass's template and adopter copied in, a committed `zFixtureCast` build and a card the clone's
kickoff checker wrote and filled (`0 unverified`). Every refusal arm of the adopter was observed RED
on a staged break and GREEN once restored: an appended byte and a removed render (AC1), `build`
moved to stage 8, `gate-bar` deleted, an emptied catalogue, a `## Stage 9 — deploy` heading and a
`{{NOPE}}` token (AC2), plus two arms no criterion names, a deleted `## Stage 4 — spec-review`
heading (exit 1 naming the unnamed entry) and an absent `.memory-tree.conf` (exit 2 naming it). At
the pass's base no adopter existed. The close owes `kickoff-manifest ratchet`, `kickoff engine size
<=18KiB`, `install-prefix (shipped surface)`, `codebase-map coverage + freshness`, `kit version
markers`, `lexicon naming predicates`, `memory hygiene`, `spec tokens`, the recall floor legs and the
`manifest-check`, `scratch-guard` and `check-wiring` self-tests; the adopter's own gate leg and
regression arms are `TOOL-aOrientedCast-8`'s.

**Evidences:** KICK-aOrientedCast-2
- AC1 — `--scaffold` — printed `.claude/skills/build/SKILL.md` and the restart line; the file opens with `name: build` in its front matter, `grep -c "{{"` printed 0, and `--check` exited 0. One appended byte made `--check` exit 1 naming the path, a removed render exited 1 naming it as not rendered, each restored exited 0, and `--bogus` exited 2 with usage.
- AC2 — `{{NOPE}}` — `build` at stage 8 exited 1 naming `## Stage 5 — build` and the entry `build` at stage 8; `gate-bar` deleted exited 1 naming `## Stage 7 — gate-bar` as naming no entry; the emptied catalogue exited 2 naming a dead probe; `## Stage 9 — deploy` exited 1 naming the heading and no entry; the `{{NOPE}}` template exited 1 naming line 7. Each restored file exited 0.
- AC3 — `harness-args unattended-unit` — `grep -c` printed at least 1 for each of the twelve strings, and `## Stage 1 — orient` to `## Stage 7 — gate-bar` appear once each, at lines 27, 31, 36, 45, 49, 65 and 72.
- AC4 — `unattended.sh --plan` — the sorted unique `grep -oE` output was that one line.
- AC5 — `## Shared with /unattended` — the `grep -cE` over the render printed 0, and the table names `M8`, `M9` and the verbs guide's carrier in its rows.
- AC6 — `continues in ./build. where` — printed 1; `the sealed fields:` printed 0 where BASE `646d4a73` prints 1; the READY prompt string's `grep -qF` exited 0; `check-template-size.sh` printed `18310 / 18432 bytes (122 under, 99.3%)` with no `WARN` line, as §4 predicted.
- AC7 — `runs through ./build. after` — the `grep -c` printed 1 and `manifest-check.sh` exited 0 on the staged tree with both stamps at `5692b36d7`; the manifest measures 25578 bytes against check 7's 25600, the bullet paid for by three trims in §B.
- AC8 — `rendered-skills = .*build` — `git grep` printed one line, `memory/map/features/roles.md:17`, and `gen_map.py --check` exited 0 after `--write` added `render_skill`.
- AC9 — `eol: lf` — `git check-attr eol` printed it for `.claude/skills/build/SKILL.md` and `tools/roles/SKILL.template.md`.
- AC10 — `--offenders` — the nine keys printed all name `check_roles.py`, `render_agents.py` or `roles_lib.py`, inherited from earlier units; none names the template or the adopter.
- AC11 — `wc -c` — the CR-stripped render measured 5076 bytes against the pinned 6144.
- AC12 — `harness-args` — the render line `## Before stage 3` spells, filled as `--role gov-builder --build zFixtureCast --unit TOOL-zFixtureCast-1 --input spec=<that spec>` with `--part task` kept and `CLAUDE_CODE_SESSION_ID=kx2`, exited 0 printing a `gov:handoff` marker and one `## Task`; `handoff.py check` on the marker's path exited 0; `harness-args` for `unattended-build`, `unattended-unit` and `tier2-review` each exited 0 with a non-empty JSON object. RED: the line run with its `<key>=<value>` placeholder unfilled exited 2 naming the key.
