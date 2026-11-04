# PLAY-dOrderedCharter-1 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-1

Each line is a probe this pass ran at rev-8 of the spec, from the worktree root with the pass applied: `git grep`
and `grep` reads, the unit's own CLI, and two scratch scripts that drive `render` and an installed engine over
committed targets under the host temp directory. A builder runs no leg, so no leg of the spec's Gates list ran
here, `gov_tag.py check` and `core.py meta-check` included. Those, the merge bar and the RED-first observation of
both `New arm:` lines are the main loop's at the close. The render selftest's new arm was not run: the scratch
script reads its fixture tables and repeats its cases through `render`.

**Evidences:** PLAY-dOrderedCharter-1
- AC1 — `python instruction_units.py practices --list` printed 39 rows; the 36 `foundation` tags equal, in order, what `RULE_LINE_RE` reads from section one of `AGENTS.md`; each of the 36 rows' `line` equals the template's text at the prior HEAD; `git ls-files '*instructions.toml'` printed nothing.
- AC2 — `practices --check <fixture>` exited 1 over all six planted catalogues, naming the row or the `foundation` entry, and 0 over the shipped catalogue.
- AC3 — `practices --active <value>` exited 1 for the empty set and for `practice.nope`, naming each, and with no value printed the 36 `foundation` tags.
- AC4 — `python tools/playbook/render_playbook.py --target . --check` printed OK; the re-render left `AGENTS.md` byte-identical, `git diff ce13efbe -- AGENTS.md` shows no changed practice line, and the lock's `AGENTS.md` row reads `coding-governance-agents.template.md@v4.5`.
- AC5 — over a committed target on `main`, a `deploy.toml` with no roles kit rendered no `[roles]` line, and one selecting it rendered the line.
- AC6 — `drop_blocks = ["cross-os"]` over a v4.5 template with the `when:cross-os` fence and one with none each lost the `[cross-os]` line and carried the `retired` note, the first its fenced text too; a `v4.4` template with the fence rendered with no note, and one with no fence kept the `no when fence` refusal.
- AC7 — `cd help && grep -n "charter.practices" charter.md README.md` hit both files; the page holds one `usage: policy:charter.practices` anchor at the fingerprint the docs reader computes, the `policy:charter.practices` row is gone from `memory/project/docs-undocumented.txt`, and `practice.repo.x` in `help/tags.md` sits in a double-backtick span.
- AC8 — a `charter.practices` scratch run: unset rendered the `foundation` set with the derived note; a scratch install with no policy kit rendered the 35 lines its kits admit with the `no policy kit` note; a one-tag value rendered one line; `charter.practices = []` refused with `this set is never empty`; a directory that is no git repository and a repository on `master` each refused with `refs/heads/main names no commit`; an install with the policy kit and no `memory-tree` kit refused naming both, and each refusal wrote nothing.
- AC9 — the `python -c` read printed `dOrderedCharter`, `True`, `True`; `tools/policy/unsummarised-keys.txt` holds no `charter.practices` line; `python "tools/policy/policy.py" lists --check` exited 0; and `read_policy_value("charter.practices"` sits on one line of `tools/playbook/`.
- AC10 — `git grep -n -F 'tools/playbook/practices.toml'` over the two modules printed the `PRODUCER_PATHSPECS` line and the `LADDER_SOURCES` line; `producers` printed no hit in the catalogue.
- AC11 — the `sed` read of `tools/playbook/practices.toml` printed 5, the digit `MAX_VERIFIERS` holds; the `verify-agent total` pair reads `${PB_DIR}/practices.toml`; and `verify agents TOTAL` is gone from `coding-governance-agents.template.md`.
