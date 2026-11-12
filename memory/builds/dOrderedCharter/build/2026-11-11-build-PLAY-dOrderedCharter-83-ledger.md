# PLAY-dOrderedCharter-83 — acceptance ledger

**Serves:** journal PLAY-dOrderedCharter-83

Each line is a probe this pass ran at rev-1 of the spec, over the merge commit `b0d43c0a1` (parents `60f222c17` and
`47ed57fab`) or over the pass commit that follows it. No leg, suite or bar ran in the pass: each checker the
criteria name is the close's, and where a line says "owed" the main loop observes it after every unit is terminal.

At pass start `origin/main` was still `47ed57fab` (PINNED, `git fetch origin main` printed it as FETCH_HEAD). The
conflict set re-taken at the pre-merge tip `60f222c17` printed tree `9cc6e920b992aefcb16b090fb5acfa7aa23b565c` and
fifty-one names: the scope table's fifty plus `memory/builds/dFairHearing/README.md`, whose two regions are its generated
`ids:` lines, resolved as the generated kind (deviation 831). `git merge --no-ff --no-commit 47ed57fab` left the same
fifty-one unmerged (PINNED, that run).

The order the scope's generated-output item names ran with one mechanical difference: `regen.py --write` stopped after
stage 2 both times, because `policy.py mirror --write` refuses while `tools/policy/catalogue.toml` is uncommitted, so
its stage 3 never ran. The codebase map's own write, `python tools/codebase-map/gen_map.py --write`, ran after the
second regen in its place, and the mirror stayed at the first parent's blob in the merge as the spec intends.
What each generator wrote, in the merge: stage 1 the instructions lock, `AGENTS.md`, the unattended Skill, the hygiene
guide, the spec format, the annotation guide, the playbook template, the review protocol and the four unattended
guides; stage 2 `memory/LIVE.md`, the playbook backlog view, three build READMEs, the dClosedLoop as-built view and the
gotcha index; the roles scaffold the two agent types and the build Skill; the map its four generated files.

**Evidences:** PLAY-dOrderedCharter-83
- AC1 — `git rev-list --parents -n 1` — printed `b0d43c0a16c69bee47713482065b65e19ac80eb3 60f222c176935e46c154f1d77c83e69243a4870b 47ed57fab692a005daa7c9850c59e033dfbddce3`.
- AC2 — `git merge-tree --write-tree --name-only` — re-taken as the opening paragraph records; `git grep -lE '^(<<<<<<<|>>>>>>>) '` over the merge printed nothing.
- AC3 — `git grep -c` — over the merge it printed one line, the spec's own AC3 line, which quotes the three old markers; no product file under the four paths carries one. Over each of the six unattended templates `grep -c '^<!-- gov:kit unattended@1.118 -->$'` printed 1 and the next line is the envelope line its `HEAD` side held. The criterion's absence is broken by its own record quoting the pattern; that is for the spec writer.
- AC4 — `bash tools/check-playbook-parity.sh` — owed: a role agent runs no leg. Over the merge the seven greps printed 1, 1, 0, 1, 1, 0 and 1, as stated.
- AC5 — `python tools/check-spec-tokens.py --spec` — printed `spec-tokens: REFUSING — --spec names no spec` and exited 2; the three greps printed 0, 3 and 1. The bare run on the pass commit is owed to the close.
- AC6 — `python tools/roles/render_agents.py --selftest` — owed: the main loop runs the selftest. The nine greps over the merge printed 1, 0, 1, 2, 2, 1, 1, 1 and 0, as stated.
- AC7 — `node --check` — exited 0 on both review-harness files, and each of the four greps printed 1 on each. Over the protocol template the four greps printed 1, 1, 0 and 1, and the `tomllib` read of `tools/workflows/kit.toml` printed `5 2`.
- AC8 — `python tools/lexicon/lexicon.py --measure` — printed `VERB_OFFENDER_PIN="1208"` over the merged tree, the value the spec pinned; the four greps over `.lexicon.conf` printed 1 each.
- AC9 — `bash -n` — exited 0 over the three suites. The floors read `FLOOR_ASSERTIONS=238` and `FLOOR_ASSERTIONS=690`, and the eight label greps printed 1 each. Recount of the spec-token suite: 179 top-level `arm` calls in the merge, 156 at the base, 159 at the pre-merge tip and 176 at `47ed57fab`, so 238 holds. The hygiene suite's 690 stays DERIVED from both sides' `RAISED` deltas: its loop-carried calls cannot be counted by a grep, and the suite run at the close observes it.
- AC10 — `help/roles.md` — the six greps printed 1, 1, 1, 1, 1 and 0; over `memory/guides/MERGE-BAR.md` the three printed 1, 0 and 1.
- AC11 — `memory/builds/dShippedRelease/README.md` — its row grep printed 1, the two `memory/builds/dIndexedDesign/README.md` row greps 1 each, and the eight record greps over the two gotchas and spec 78 printed 1, 1, 1, 1, 0, 2, 1 and 1, as stated.
- AC12 — `memory/guides/SESSION-KICKOFF.md` — at the merge `last-audit` names `60f222c176935e46c154f1d77c83e69243a4870b` and the merge body's `manifest-audit:` line greps 1, its count 18. The pass commit sets `last-body-change` to `b0d43c0a16c69bee47713482065b65e19ac80eb3`. The ratchet leg is owed to the close.
- AC13 — `git diff --quiet` — exited 0 between the first parent and the merge over `.governance/policy.json`. The pass commit carries `python tools/policy/policy.py mirror --write`'s render, `catalogue_blob` `7400f98e3501e3f48c6818d1bb1653eff6d9e351`, the blob `git ls-tree` gives the merged catalogue. `mirror --check` is owed to the close.
- AC14 — `python tools/run-gates/regen.py --write` — after `bash tools/roles/adopt-roles.sh --scaffold` it moved nothing in stage 1 over the merged tree; over `AGENTS.md` the two greps printed 0 and 1. `regen.py --check` runs kit suites and is owed to the close.
- AC15 — `git diff --name-only` — from the re-taken trial tree `9cc6e920b992aefcb16b090fb5acfa7aa23b565c` to the merge, over `tools` and `skills`, it listed twenty-one paths, the scope table's twenty-one under `tools/`.

**Owed to the close.** Every leg of the spec's Gates section and the runs its section on gates names after the pass
commit. The spec declares no `New arm:` line, and this pass adds no refusal site.
