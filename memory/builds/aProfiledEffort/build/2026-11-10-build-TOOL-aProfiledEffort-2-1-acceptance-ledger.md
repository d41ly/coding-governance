# Acceptance ledger — TOOL-aProfiledEffort-2

**Serves:** journal TOOL-aProfiledEffort-2

Built against spec rev-1 at the pass's parent `017560adc`. Each line below is a probe of the changed code, made in the pass with the names of the spec's section 6 set. The base archive, the fixtures `u2/kit` and `u2/bad` and the two scratch scripts sat in the run's scratch directory and are not tracked. No suite, gate leg or bar ran in the pass, so arm 19's own code has not executed. Owed to the main loop at the close: the legs of the spec's Gates section, the `codebase-map coverage + freshness` leg that section does not list, and arm 19 observed RED on each of its two staged breaks and GREEN restored, recorded here under a `Pass: none` commit.

**Evidences:** TOOL-aProfiledEffort-2
- AC1 — `for w in $W; do same_as_base stage-efforts $w || echo moved; done` — it printed nothing over the four workflows, and the same loop over `harness-args` for the three harnesses printed nothing: every no-flag line is the base archive's line byte for byte.
- AC2 — `5 22 ['medium']` — the no-flag command printed `5 22 ['high', 'medium']`, and the command with `--model claude-fable-5-2` and again with `--model claude-fable-6-0` printed exactly this.
- AC3 — `cmp` — exited 0 and printed nothing between the no-flag lines and the lines for `--model vendor-other-9`.
- AC4 — `"gov-builder":"max"` — over the scratch copy with the `tfam` profile appended, `role-efforts --model vendor-tfam-9` printed a line carrying it with every other role at `low`, and `stage-efforts closing-review --model vendor-tfam-9` printed `{"diffFinder":"low","skeptic":"low","synthesis":"xhigh"}`. The copy's no-flag lines compared equal to `$X/plain`, its Fable lines printed `5 22 ['medium']`, and `cmp $H "$K/handoff.py"` exited 0.
- AC5 — `9 True True` — the criterion's command printed exactly this.
- AC6 — `--model is empty` — both commands printed the usage block, then a stderr line carrying it, then `2`, and no JSON. Over the copy with `default = "loud"`, `role-efforts` printed two `R12` lines, for `effort.default` and for the seeded profile's default, then `1`, with no traceback.
- AC7 — `grep -c 'separators=' $H` — the six commands printed `1`, `1`, `1`, `1`, `0` and `0`, in the criterion's order.
- AC8 — `bash -n "$S"` — exited 0; the two `grep -c` commands printed `4` and `1`, and the floor's rise against the pass's start printed `4`, from 51 to 55.
- AC9 — `tools/roles/handoff.py` — the suite did not run in the pass, so no `ok   arm 19` line and no `PASS` line has been seen and neither staged break has been applied. What the pass observed in its place: a scratch driver read the arm's inline program out of the suite file and ran it against the scratch copy and this repository's role index, and its three lines equalled the verbs' no-flag lines for `spec-write`, `closing-review` and `role-efforts` byte for byte, with the `tfam` profile already appended. The calls of 19b, 19c and 19d are the calls AC3, AC4 and AC6 made. The arm's run, RED and then GREEN, is the main loop's.
