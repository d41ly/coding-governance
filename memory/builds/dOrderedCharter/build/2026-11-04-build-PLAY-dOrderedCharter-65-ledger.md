# PLAY-dOrderedCharter-65 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-65

Each line is a probe this pass ran, at rev-1 of the spec, from the worktree root with the pass applied: the
spec's own one-liners over the real tree, and `core.py fixture` over its scratch fixture repository under the
host temp directory. The tags resolver run of AC2 and the old-spelling worktree of AC3 are the main loop's at
the close, because a role agent's scratch guard refuses them, and so are the legs the spec's section 7 names
and the merge bar. The spec declares no new arm. This record cites no code line.

**Evidences:** PLAY-dOrderedCharter-65
- AC1 — the register's tags piped to `lexicon.py --tags` exited 0 and printed `lexicon: tags · 17 graded, 0 refused`
- AC2 — OWED: `gov_tag.py check --json | reds` from the repo root at the pass tip, the main loop's at the close
- AC3 — OWED: the Design section's old-spelling worktree fixture, the main loop's at the close
- AC4 — `core.py fixture --plant practice` printed the label `practice: new charter-practice demo --line x` and ended `fixture · green · 0 expectation(s) failed`; `core.py fixture --plant kinds` ended the same
- AC5 — the `run_kinds` probe printed `0` and `core: kinds · 17 registered, 14 pending`; the `run_practices` probe printed `0`
- AC6 — `core.py new practice demo --line x`, `new kit demo --line x` and `new layer demo --line x` each exited 2 and printed `refused · kind.practice is no kind the register holds`, then `kind.kit` and `kind.layer`; no file under `tools/playbook` was written by them
- AC7 — the retired-spelling `git grep` over `tools`, `help` and `skills` printed nothing (exit 1), and `grep -n 'never a namespace word' tools/playbook/kinds.toml` printed the register's new rule sentence
