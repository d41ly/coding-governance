# TOOL-aOrientedCast-15 — acceptance ledger

**Serves:** journal TOOL-aOrientedCast-15

Direct checks only: under the owner's rule for this run no gate, suite, slice or self-test ran in
this pass. What ran: `handoff.py render` over a scratch card, and over a scratch checker printing
seven labels as the refusal; a scratch repository holding a copy of the roles kit and the charter,
scaffolded under an `export MEMORY_ROOT=memory  # note` conf by this pass's adopter and by the
parent's (`git show HEAD:…`) as the RED; in that repository, a `gov-researcher` handoff rendered with
`--part task`, piped as an `Agent` payload into `node tools/hooks/agent-cap.js` under
`env -u CLAUDE_PROJECT_DIR`, then the same payload with one task word changed as the liveness RED
(rule 6 refused it, exit 2), and `handoff.py check` over the file; `tools/check-wiring.sh --check`
there with `.claude/roles.json` truncated to `{`, this pass's and the parent's; and
`manifest-check.sh --card --append` in a scratch clone, this pass's and the parent's. Owed to the main
loop at the close (M8): the six `New arm:` lines of §7, each RED on its staged break and GREEN
restored, the `FLOOR_ASSERTIONS` raises (workflows suite 631 to 643, manifest-check 302 to 304,
roles adopter 10 to 13), and every leg §7 lists. The OC4 empty-roles byte comparisons assume a
`"roles":{}` run prints the same prompts and result as a run with no key; §4 asks the builder to
confirm that on the arm's first run, which this pass could not make, so the close's first run of
the `unattended-build self-test` leg is that confirmation.

**Evidences:** TOOL-aOrientedCast-15
- AC1 — owed to the main loop — `grep -c '646d4a73' tools/workflows/unattended-build.test.sh` printed 0 in the pass; the `unattended-build self-test` leg at the close observes every `OC4 AC1` arm, and the empty-roles comparisons, passing against the current harnesses.
- AC2 — `handoff.py render` — over a scratch card filling all eight fields, `--role gov-reuse-scout --part task --stdout` exited 0 and its `### task:in` block held the card's IN scope value; `grep -c 'Goal (1–2 sentences)' tools/roles/handoff.py` printed 0; a scratch checker printing seven labels refused the render, exit 1, naming the checker and the count.
- AC3 — owed to the main loop — the `roles adopter self-test` leg at the close observes arm 6; in the pass, a `handoff.py render` task part piped to `agent-cap.js` exited 0 with empty stderr, a one-word edit of it exited 2 naming rule 6, and `handoff.py check` printed the marker's `task-sha`.
- AC4 — `manifest-check.sh --card --append` — in a scratch clone, an OUT field written `(explicit cut-line) : …` exited 1 naming `OUT / non-goals` a placeholder, and `(explicit cut-line) : the stored card` appended, exit 0; the parent's checker appended the placeholder body, exit 0.
- AC5 — `adopt-roles.sh --scaffold` — under `export MEMORY_ROOT=memory  # note` it exited 0, `--check` exited 0, and `grep -c '# note' .claude/skills/build/SKILL.md` printed 0; the parent's adopter exited 2, "MEMORY_ROOT is blank or absent".
- AC6 — `check-wiring.sh --check` — with `.claude/roles.json` truncated to `{` it exited 1 and printed one `UNWIRED  roles` line naming `.claude/roles.json` and `adopt-roles.sh --scaffold`, and no `ok       roles` line; the parent's printed a note and `ok       roles`.
- AC7 — owed to the main loop — the `roles render selftest` leg at the close observes arm 13 passing, and RED on a staged `render_agents: note` line without `'absent'` beside a separate `'absent'` line.
- AC8 — `KIT_ROLES_VERSION` — `grep -c '^KIT_ROLES_VERSION = "1.2"' tools/roles/roles_lib.py` printed 1, `grep -c 'gov:kit roles@1.2'` printed 1 over each of the README, the Skill template and the re-rendered `.claude/skills/build/SKILL.md`, and `grep -rn 'roles@1.1' tools/roles .claude/skills/build` printed nothing.
