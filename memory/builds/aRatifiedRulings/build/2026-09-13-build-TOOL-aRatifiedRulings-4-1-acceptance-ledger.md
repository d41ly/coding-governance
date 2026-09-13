# TOOL-aRatifiedRulings-4 — acceptance ledger

**Serves:** journal TOOL-aRatifiedRulings-4

Every observation below was made on node `a` on 2026-09-13 over the working tree this unit
commits. The owner's per-pass rule in the build README bound this pass to the fast diff-scoped
gates and nothing held: `run-gates canary` is the held leg the new arm joins, and this pass did NOT
run it. The arm was observed through its OWN fixture in isolation, the way the brief and the spec's
§4 state — a scratch repo under `TEMP` holding one copy of the runner, the `selfkill.sh` fixture,
the `tbl-loose` profile row and the 4h-kill manifest row with its `ceiling` key dropped, driven by
the arm's three assertions byte-identical to the ones the suite now carries. The suite run AC1,
AC4 and AC5 spell whole, and the stubbed run AC7's second half reads, are the closing pass's.

## The red case is fixture-only, by class

Every leg in `tools/gate-legs.json` declares a `ceiling`, so no real leg on a host with a runnable
`timeout` reaches the branch; the fixture strips one. That is the class
`memory/gotchas/staged-break-substitutes-a-synthetic-value.md` names, the ruling
`TOOL-aLeakedHandle-9` accepted it with the class named, and the build README's rule says the same.
What the arm cannot show is the branch firing on a real leg an operator or an OOM killer killed
while running unbounded; the spec's §4 says where that observation waits.

## The observations

| criterion | how it was observed | read | verdict |
|---|---|---|---|
| AC1 shape, AC2 value, AC4 red-first | the isolated probe against HEAD's runner (`e96cf2f4`, the unfixed source) | tail `GATE FAIL  selfkilled  (exit 137)`, ledger `2.424`; the value assertion printed `'<no number found>'s where the ledger records '2.424's`, the shape assertion printed the `(exit 137)` line; exit 1 | RED, as required before the line lands |
| AC1 shape, AC2 value | the same probe against the working-tree runner with the one line added | tail `GATE FAIL  selfkilled  (killed after 3.070s)`, ledger `3.070`, byte-equal; the profile line read `gate profile: loose`; `PASS (3 assertions)`, exit 0 | GREEN |
| AC3 | not observed here — the `stubborn` and 4h-kill arms live inside the guarded half of the held suite | the sibling line is byte-identical in the diff (`git diff` shows it unchanged) and the new predicate is its negation, so the two partition rc=137 | closing pass's |
| AC5 | not observed here — a second whole-suite run under the `PATH` stub, which the per-pass rule holds | the arm, its three counters and the `tbl-loose` write sit outside the `if` at the guard, verified by line position: the write at `run-gates.test.sh:1135` above the `if` at `:1136`, the arm after the `fi` at `:1215` | closing pass's |
| AC6 | `bash skills/session-kickoff/manifest-check.sh --staged` before the commit, and the pre-commit hook's own run of it | check 5 green with the re-stamp bundled; the stamp sha stays `9fac2b53`, which is `git merge-base origin/main HEAD` on this branch, and only the datetime moves | GREEN |
| AC7 first half | `grep -E '^FLOOR_ASSERTIONS=' tools/run-gates/run-gates.test.sh` | `FLOOR_ASSERTIONS=149`, the base's 146 plus the arm's three `n=$((n+1))` | GREEN |
| AC7 second half | the stubbed suite run | not taken here | closing pass's |
| AC8 | `bash tools/check-kit-versions.sh` twice on this tree | with `run-gates.sh:19` at 1.7 and the README marker still at 1.6 it printed `kit-versions: tools/run-gates/README.md gov:kit marker != KIT_RUN_GATES_VERSION (1.7)` and exited 1; with both at 1.7 it exited 0 | RED then GREEN, the half-bump red seen live |

The two `-S` greps AC8 names resolve only after the commit exists and are the closing pass's to
read; both strings land in this one commit, so they name one sha.

## What the probe was

`arm-probe.sh`, a throwaway in the session scratchpad and not committed: it takes the runner file
to copy in, builds the scratch repo, runs the runner under `GATE_PROFILES=fx/tbl-loose.txt`, prints
the tail and the ledger value, then applies the arm's three assertions and exits 1 on any red. The
scratch root is a short path under `TEMP`, because a clone or a scratch under the session
scratchpad hits `MAX_PATH` on this box.
