# PLAY-dOrderedCharter-12 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-12

Each line is a probe this pass ran, at rev-5 of the spec, from the worktree root with the pass applied:
`git grep` reads, `instruction_units.py fixture --plant <case>` once per plant, each plant in a throwaway
repository under the host temp directory, `grammar --doc` over today's charter, and a render into a scratch
clone of this branch. The leg itself over this tree, `playbook render selftest` and the other legs the
spec's section 7 names, the merge bar, and the RED-first observation of each New arm are the main loop's at
the close: the role hook refuses a builder those.

**Evidences:** PLAY-dOrderedCharter-12
- AC1 — `git grep -n -E "\"policy-value\"" -- tools` printed one line, the `STATEMENT_TYPES` definition at `tools/playbook/instruction_units.py#STATEMENT_TYPES`
- AC2 — `fixture --plant statements` exited 0: a directive with no modal, a constraint with no `enforced-by`, a `fact` typed `Worktrees: none yet` with no `source`, a pointer to `doc.nosuch`, a pointer to the whole `doc.charter`, a `policy-value` with typed text and a row typed `prose` each red `check_statement` naming its tag, rule and remedy, and one well-formed row of each of the six types passed
- AC3 — `grammar --doc AGENTS.md` exited 1 naming the provenance paragraph at lines 4 to 8, the heading `## 1. Governing practices`, the phrase `the marker below` and the `**Worktrees:**` fact; over `AGENTS.md` at `4e8f80cdf` it also named the version marker at line 10; `fixture --plant document` exited 0, the re-founded charter exiting 0
- AC4 — `fixture --plant lock` exited 0: two renders wrote identical lock bytes, the row's `blob` equalled `git hash-object` of the rendered file, and a hand edit red `lock --check` naming the path, as did a planted version marker and an absent lock
- AC5 — `render_playbook.py --target <clone>` into a scratch clone: `git -C <clone> grep -n "governance-template:" -- AGENTS.md` printed nothing, and `read_lock` read the charter row `template = "coding-governance-agents.template.md@v4.4"`; `git grep -n "instructions.lock" -- skills/session-kickoff/SKILL.md WIRE-INTO-PROJECT.md` printed SKILL.md:87 and five runbook lines
- AC6 — `registry.toml` holds the `name = "instruction grammar (statement types, provenance lock)"` line under an `[[exempt_leg]]` header, `govkit.py selfcheck --write` added its `subject-pins.tsv` row `repo product`, `gen_map.py --write` gave `MAP.md` its row with `playbook` the claimant, and `memory/map/features/playbook.md` carries it in its `gate-legs = [` claim
