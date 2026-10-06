# TOOL-aMendedFleet-68 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-68

**Evidences:** TOOL-aMendedFleet-68
- AC1 — `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md` — exit 0 at the tip, `template-size OK — SKILL.md: 10059 / 10240 bytes (181 under, 98.2%)`, read against the new row; the same run with `--bump` recorded the high-water row at 10059
- AC2 — `handle:M<n>` — check 16 arm A's `awk` row filter, copied verbatim into a scratch script, over the base template and over the tip's `tools/unattended/SKILL.template.md`: the same 17 sorted pairs. Staged break: a copy of the tip with the `wrap-up-derived` row deleted reported RED
- AC3 — `items have NO override` — check 16d's paragraph filter over base and tip: the member set `authorization-reachable pieces-complete` both times. Staged break: a copy with both backticks around `pieces-complete` removed reported RED
- AC4 — `a process not in the ledger is never killed` — the tip template folded with `tr` and searched with `grep -qiF`: found. Staged break: a copy reading `sometimes killed` reported RED
- AC5 — `## Close` — check 43's extraction, copied verbatim, over base and tip: byte-identical. Staged break: a copy whose hold paragraph runs `--hold` before the commit reported RED
- AC6 — `bash tools/unattended/adopt-unattended.sh --check` — exit 0, `in sync (skill rendered from template + .unattended.conf)`; `grep -oE` over base and tip gave the same twelve distinct placeholders, `diff` empty
- AC7 — `--verb` — every distinct double-dash token of the base Skill (69, counting flags; an anchor fragment glued to a link is not a token) is named by the tip's router or by `## The paths, in order` in `tools/unattended/VERBS.template.md`. Staged break: a copy of the carrier with `--no-ff` respelled reported RED naming it
- AC8 — `--verb` — per path, the first-occurrence order of the driver's 24 verbs in the base Skill section against the same verbs in the ported subsection, over fifteen pairings: every one agreed. Staged break: a copy with the Close subsection's steps 1 and 2 swapped reported RED, `--close` ahead of `--phase`
- AC9 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — exit 0; `grep -c "{{" tools/unattended/VERBS.template.md` printed 0; `grep -n "The paths, in order"` hit `tools/unattended/README.md` and `tools/unattended/SKILL.template.md`
- AC10 — `.claude/skills/unattended/SKILL.md` — in a `git clone --local` under `%TEMP%`/f68, spelled by its long path, with the tip's limits file, checker and render copied in: exit 0 at 10059 bytes, then 11,000 bytes appended and `bash tools/check-template-size.sh .claude/skills/unattended/SKILL.md` exited 1, `10819 over 10240`
- AC11 — `last-audit:` — the staged diff of `memory/guides/SESSION-KICKOFF.md` moves `last-audit:` and `last-body-change:` together in the commit that adds the leg to `tools/gate-legs.json`, and the `.githooks/pre-commit` staged manifest leg admitted that commit; `bash skills/session-kickoff/manifest-check.sh` after it is reported in the pass's return

## The rules the port found stated two ways

- The Skill said a `--dispatch` re-declaration that NARROWS a write set is refused; the verb entry says
  a re-declaration is accepted wider, narrower or disjoint. The ported section follows the verb entry.

## Owed at the close

The kit gate's checks 16, 18, 20, 24, 25, 26, 41, 43 and 44 were observed through copies of their
extractions, never through the 16,040-second leg. That leg, `unattended skill wiring`, the kit suites
whose fixtures mutate the Skill template, and the new `unattended skill size` leg are the close's.
