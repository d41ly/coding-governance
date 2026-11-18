**Serves:** journal TOOL-dDeclaredLoop-18

# Builder return — TOOL-dDeclaredLoop-18, dispatch 3: a second divergence, the built unit restored

Run wf_ee1ee571-451. The dispatch gate admitted the pass. The builder built the unit, observed seven of its eight criteria, and restored its edits when the eighth failed on the live tree.

## Why

DIVERGENCE: spec rev-4 §4 "The four rows" / "Migration" / "Rollout" and AC8 say the four registry rows land additively with the `tags` leg green. They do not. Registering `command`, `item` and `policy` as namespace words makes three existing tags break `derive_tag_fault`'s rule "first segment is a namespace word":

- `kind.command` at tools/playbook/kinds.toml@f616569e:25
- `kind.item` at tools/playbook/kinds.toml@f616569e:155
- `kit.policy` at tools/policy/kit.toml@73fefee1:4 (the policy kit's descriptor `id`)

Observed with the unit fully built in the worktree: `check_tag_shape` over the live tree returned exactly those three reds, and `lexicon.py --tags` refuses the same three, so the `tags` leg would carry six reds at landing (three shape, three name-check). §4 "The catalogue in the `policy` namespace" pins `derive_tag_fault` only over the 264 new member tags and six family tags against the fourteen words; it never grades the tags already defined in other namespaces against the four new words. `step` collides with nothing today.

None of the three is in this unit's write set: `kinds.toml` is not in "Files touched", and §3 Non-goals forbids any change under `tools/policy/`. `kind.command` and `kind.item` are also cited in help/reference/kinds.md (with usage stamps) and tools/playbook/core-pending.txt.

What the spec would have to say: §4 must state how those three tags stay legal once the words are registered, and widen §2, "Files touched" and AC8 to match. The choices I can see are (a) rename the two kind rows and the policy kit's id, with their citations; (b) change the namespace-word rule in `derive_tag_fault` and the lexicon's twin so it does not fire across these namespaces; (c) register different words. Each is a design choice, not a builder's.

Everything else in rev-4 held against the code. The nine files I edited are restored; nothing is committed.

## Summary

TOOL-dDeclaredLoop-18 was not built to a commit: returned as a DIVERGENCE, spec left INPROGRESS, HEAD still 0ca2f812a.

**State of the worktree.** The nine edited files are restored by name. One path is still staged and uncommitted: memory/builds/dDeclaredLoop/RUN.md, two lines the driver wrote for `--dispatch` (declared and effective, exit 0) and `--brief` ("already recorded, unchanged", exit 0). I left it because it records acts that happened; the main loop decides whether to carry or drop it. No ledger, no deviation record, no `gen_build_index.py --write`, no `gotchas.py --for-diff` (no commit to run it over).

**What was built and observed before the stop** (all through `gov_tag.py --fixture --plant <case>` with the two `--set` flags, standing in for the §7 new arm on tools/playbook/adopt-playbook.sh, which was not run):
- AC1 `policy-ns-word`: exit 1, printed `· shape · policy.step.timeout · first segment 'step' is a namespace word`.
- AC2 `policy-catalogue`: exit 0, printed `264 members of 264 literal names, 6 families of 6 prefixes`.
- AC3 `loop-rows`: exit 0, printed `where: rc=0 0, check: rc=0`; `loop-bad-seg`: exit 1, printed `· shape · step.Plan · segment 'Plan' is outside [a-z0-9][a-z0-9-]*`.
- AC4 `command-rows`: exit 1, `command.corekit.old` cited and undeclared, no line holding `command.corekit.new`.
- AC6 `policy-family`: exit 1, `policy.review.build.nope` undeclared, the line `1 families, 2 cited under one, 1 declared by the catalogue`, no line holding `policy.review.build` alone.
- AC5: the three greps printed 4, 0 and 4.
- AC7: `printf 'policy.item.x\n' | python tools/lexicon/lexicon.py --tags` exited 1 with the expected line.
- AC8: failed. A `python -c` probe calling the changed checks over the live tree (not the `tags` leg itself) gave the three shape reds in `why`. The rest of AC8 held: no join or unresolved red, `step` and `item` pending, `policy` armed at 264, `command` unarmed, the two dossier spans gone.
- Unchanged plants `none`, `bad-ns` and `file-name` still exited 0, 1 and 0.

**For the spec writer, beyond the divergence:**
- help/tags.md has a second sentence that goes stale once `item` is registered (the edge-grammar paragraph listing `feature`, `item`, `commit` or `session` as unregistered words). S8 does not name it.
- memory/map/generated/symbols.json is the only generated map file the unit moves.
- With `step` registered in gov's registry, the existing `bad-ns` plant prints 1 red instead of 2 (the lexicon reads gov's registry, not the fixture's); its adopter row still matches.

**Cost note.** The `--dispatch` verb took about 25 minutes, most of it in `check-spec-tokens.py` → packet `--check` → `carries.py --report dDeclaredLoop`. I waited on it past the 600 s (PINNED) bound three times because writing was gated on it.

**Still owed at the close once the spec is revised and the unit rebuilt:** the §7 new arm, RED on `policy-ns-word`, `loop-bad-seg`, `command-rows` and `policy-family` then GREEN, and the `tags` leg over the real tree.

Files for the spec writer:
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/kinds.toml
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/policy/kit.toml
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/tag_index.py
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/help/reference/kinds.md
- C:/projects/coding-governance/.claude/worktrees/unattended-declared-loop-d56bf0/tools/playbook/core-pending.txt
