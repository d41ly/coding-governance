# Acceptance ledger — TOOL-aTwinnedPass-1

**Serves:** journal TOOL-aTwinnedPass-1

Built against spec rev-2 in one pass commit, on node a, in the runtime's own worktree for this agent,
reset to the dispatch commit `69889039d`. The spec's forks F1 to F5 carry their resolutions, and the
build follows each: F1 (a), an unpaired `writes` is refused; F2 (a), a path outside the declared set
is returned, not written; F3 (a), the commit sentence is unchanged; F4 (a), `nextAction` takes its
base from `passBase`; F5 (a), the schema requires `branch` and `worktree` with `passBase`.

One divergence in wording, not in design: §4 "The two keys" spells the comment above the `passBase`
test with the same opening as the header paragraph §4 "The header comment" names, and AC9 counts
that opening once. The test's comment opens `` `passBase` IS GRADED BY THE COMMIT SHAPE `` instead;
its code is the spec's.

The observations below are each criterion's own command, or the criterion's probe from §6 run from
the scratch directory over the changed harness and over the base blob `aebbb4a72` written beside it.
No suite, gate leg or bar ran in the pass. Over the base blob the same probe battery printed 33
failures of the 38 checks AC3 to AC8 name, and over the changed harness none. The five that held at
base are the `base` sentence, the forty-digit spawn, AC4's cut, which removes nothing from a prompt
with no paragraph, and the two absences from `nextAction` AC8 names; each criterion's positive half
was red there.

Owed to the main loop at the close: the `TP1` group of fifty assertions in
`tools/workflows/unattended-build.test.sh`, after the `passLegs` group, observed red at base
`aebbb4a72`, then green, with `FLOOR_ASSERTIONS` at 1000; the runner's `isolation:` trace line; and
the legs of the spec's Gates section. The group's three `New arm:` lines of §7 are its T1 to T6.

**Evidences:** TOOL-aTwinnedPass-1
- AC1 — `node tools/workflows/check-workflow-syntax.js tools/workflows/unattended-unit.js` — exited
  0, printing `1 workflow script(s) parsed clean`.
- AC2 — `diff` — over the probe's output for `$S/base.js` and for the changed harness, each of the
  four calls the criterion names printed nothing.
- AC3 — `THIS PASS BUILDS IN A WORKTREE OF ITS OWN` — the prompt carried it, `` `git reset --hard fedcba9` ``,
  ``The declared write set is `P1 P2` `` and `` return what it prints as `base` ``, and neither
  `--dispatch tB` nor `--brief tB`; the `opts:` line carried `"isolation":"worktree"` and
  `"required":["committed","sha","why","summary","branch","worktree"]`; the log carried
  ``unit A-tB-1: own worktree from `fedcba9`, declared writes`` and
  `branch=worktree-agent-x1 worktree=/w/agent-x1`; the result carried `"branch":"worktree-agent-x1"`
  and `"worktree":"/w/agent-x1"`. The suite arm T1 is owed to the main loop.
- AC4 — `` `git rev-parse --show-toplevel` prints it. `` — the paragraph from `\n\nTHIS PASS BUILDS`
  to that token was present in the JSON prompt line, the line with it cut out equalled the `"$A}"`
  prompt line, and the `opts:` line carried `"isolation":"worktree"`. The suite arm T2 is owed to the
  main loop.
- AC5 — `--base fedcba9` — with `$W` the `nextAction` carried
  ``Run `PL --base fedcba9` at the main loop with its working directory at `/w/agent-x1`, before that worktree is merged back``
  and `which is HEAD there when the command runs`, and not `def5678`; with `$K` it carried
  `--base fedcba9`. The suite arm T4 is owed to the main loop.
- AC6 — ``THROW unattended-unit: args `passBase` `` — each of `7`, `""`, `"abc"`, `"ABC1234"` and
  `` "fedcba9`" `` printed it and no `prompt:` line; a forty-digit lower-case hex value printed a
  `prompt:` line. The suite arm T6 is owed to the main loop.
- AC7 — ``THROW unattended-unit: args `writes` `` — each of `7`, `""`, `"a\nb"` and `` "a`b" `` beside
  `passBase`, an unattended `passBase` with no `writes`, an unattended `writes` with no `passBase`, and
  an attended `passBase` with `writes` printed it and no `prompt:` line. The suite arm T6 is owed to
  the main loop.
- AC8 — `whose path the builder returned unusable` — with `$X` the result carried `"branch":""` and
  `"worktree":""`, the `nextAction` carried that phrase and neither `rel/w` nor `a b`, and the log
  carried `branch=a b worktree=rel/w`. The suite arm T5 is owed to the main loop.
- AC9 — `grep -c "unattended-unit@1.1"` — printed `0`, and `grep -c` printed `1` for
  `version: '1.2', // gov:kit unattended-unit@1.2` and for ``^// `passBase` IS OPTIONAL (TOOL-aTwinnedPass-1)``.
- AC10 — `grep -cF "names that worktree as the command's working directory"` — over
  `help/pass-legs.md` printed `1`.
- AC11 — `bash -n tools/workflows/unattended-build.test.sh` — exited 0; `grep -c` printed `1` for
  `RAISED 950 -> .* by TOOL-aTwinnedPass-1` and `1` for `trace.push("isolation:"`. The arms'
  red-then-green run is owed to the main loop.
- AC12 — `python tools/codebase-map/gen_map.py --write` — after it, `gen_map.py --check` exited 0 and
  `git diff --exit-code -- memory/map/generated/symbols.json` printed nothing.
- AC13 — `git show --stat HEAD` — the pass commit lists this ledger under the build folder.
