# Acceptance ledger — TOOL-dFairHearing-50

**Serves:** journal TOOL-dFairHearing-50

Built against spec rev-3 at the pass's parent `65ad5ac89`. No commit since the spec's base `bdd2e5f3` touched `tools/`, so every line the spec cites in the files this unit edits stood where it says, and each was read in the tree at its edit site. Each criterion's red value is the spec's, read at `bdd2e5f3`. Each green value below was read from the built files. The probes are the spec's fenced blocks, saved in the run's scratch directory and not at `$TEMP`, because the run's temp rule binds; each `mktemp` took its root from that directory, and the two probes that build a git fixture took a short root under the system temp directory, removed after. No suite, gate or bar ran in the pass. The `python tools/lexicon/lexicon.py --check` count, the role's one gate, read 1211 verb offenders at the pass's start and 1211 after the edit.

The render `tools/workflows/tier2-review.js` took the template's two edits by hand, the same lines byte for byte, because the parity script's `--render` mode is a suite file that a pass may not run. A diff of the two files' changed lines printed nothing. The close's `review-protocol parity (kit vs dogfood)` leg confirms the render.

No floor moved. `FLOOR_ASSERTIONS` stands at 638 in the tier2-review suite and 925 in the unattended-build suite, because the spec takes no hand count. By hand count the first suite gains one assertion and the second five, which the close confirms from a real run.

**Evidences:** TOOL-dFairHearing-50
- AC1 — `node $TEMP/fh50args.js` — it printed `30 field(s), length not read`. Owed to the close: `tier2-review self-test`, and the moved arm's RED-first observation.
- AC2 — `node $TEMP/fh50cut.js` — it printed `stated one 1 — it carries no` the by-design head, `stated none 0` and `no head null`. The `deriveStatedItems(` grep printed 3 over the render and 3 over the template, and the README phrase grep printed 1. Owed to the close: `tier2-review self-test`, with `FH23 AC27` and the new `FH50 AC2` arm, and that arm's RED-first observation.
- AC3 — `grep -c 'verifyOrder.length...MAX_VERIFIERS'` — it printed 1 over the review-join suite and 1 over the render, and the `allFindings` grep printed 0. Owed to the close: `review-join self-test`.
- AC4 — `grep -c '.claude/hooks/agent-cap.js'` — it printed 2 over the review-join suite, the `HKK` grep printed 0, and the population-shape grep printed 0. Owed to the close: `review-join self-test`.
- AC5 — `bash $TEMP/fh50slots` — on this MSYS host it printed `node opens it`, and the `cygpath` grep printed 1. Owed to the close: `verifier fan-out self-test`, its six named arms.
- AC6 — `grep -c 'rm -rf .*PFX}.{WF}'` — it printed 1. Owed to the close: `playbook parity selftest`.
- AC7 — `bash $TEMP/fh50merged` — it printed the two pinned lines, the `"merged":0,"unverified":48` and the `"raw":46` needles, and each needle grep printed 1. Owed to the close: `unattended-build self-test`.
- AC8 — `bash $TEMP/fh50gate` — it printed `exit 1: carries on, st=1`, `verifier-fanout: the rule could not run on x.js — why`, `exit 2: subshell 2` and `load refused: it exports no MAX_VERIFIERS,`. `bash $TEMP/fh50bound` printed `bound: split findings 1`, `bound: fallback findings 0` and `total: fallback findings 1`. The `WRITER_MARK` grep printed 0 and the two hook greps printed 1 each. Owed to the close: `unattended-build self-test`, with each `DGR74` and `DGR83` arm named and the four `FH50 AC8` arms, and their RED-first observations.
- AC9 — `bash $TEMP/fh50cites` — it printed `old home 0` and `fanout gate 2`, and the `once` grep printed 0. Owed to the close: `unattended-build self-test`.
- AC10 — `python $TEMP/fh50exempt.py` — it printed `undeclared 0 []` and `stale []`. Owed to the close: `spec-tokens self-test`.
- AC11 — `grep -c 'is graded there and set apart here'` — it printed 1, the two old-claim greps printed 0, and the `walk-red` grep printed 0 over each of the four documents. Owed to the close: `spec tokens (a spec's own names resolve)`.
- AC13 — `python $TEMP/fh50sites.py` — it printed `printf-subst 66`, and the `printf -v wr_ret` grep printed 1. Owed to the close: `shell hygiene (a fork spent on builtin work)`.
- AC14 — `bash $TEMP/fh50forks` — under bash 5.3.9 it printed `forks 45`, and the `_kit_file=` grep printed 4. Owed to the close: `spawn budget (forks per hot entrypoint)` and `check-wiring self-test`.
- AC15 — `grep -cE '(k|f|t)/(hooks|policy|workflows)/[a-z-]+\.js'` — it printed 0 over the resolver suite, and the `FG_HK=` grep printed 1. Owed to the close: `install-prefix (shipped surface)` and `python resolver (behaviour + inline parity + idiom ban)`.
- AC16 — `python $TEMP/fh50owner.py` — it printed `moved 5` and `dFairHearing rows 0`. The unit-cite grep printed 1 over the catalogue and 1 over the policy README, and the mirror's `"owner":` grep printed 0. Owed to the close: `policy check`, and the main loop's deviation record and ask the spec names.
