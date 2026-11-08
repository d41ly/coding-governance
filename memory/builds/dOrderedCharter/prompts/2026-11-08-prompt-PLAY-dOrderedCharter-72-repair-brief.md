**Serves:** research PLAY-dOrderedCharter-72 PLAY-dOrderedCharter-73

# Brief: units 72 and 73 — the close bar's own code reds

## The prompt

> merge this branch to remote as well

— owner, 2026-11-05. The first full bar at VERIFYING reds 13 legs that are green on `origin/main`, so this build left them. The record fixes are
the main loop's; these two units take the code fixes.

## The brief

### Goal

Write specs 72 and 73, so each leg named below goes green over this tree, every fix taking the cause the checker's own remedy names.

### Items

1. **Unit 72: the positional lists leave `tools/`.** `tools/playbook/positional-refs.txt` (38,778 lines of gov's own record citations) and
   `positional-producers.txt` sit under a shipped kit, so they cause nearly all of the install-prefix red (18,745 of 18,847 hits), all 5
   dead-path hits (citations of deleted files), 18 of the 19 new drift-audit offenders, and one undeclared method carrier.
   - Move both to `memory/project/`, have `tools/playbook/positional.py` find them through `MEMORY_ROOT` instead of beside itself, drop their
     `project-owned` include from `tools/playbook/kit.toml`, declare them in `.memory-tree.conf`'s `PROJECT_REGISTRY_EXTRA`, and re-point
     every reader: `gov_tag.py`, `render_playbook.py#write_empty_lists`, unit 71's selftest arm, and any other a grep finds.
   - Test before choosing: whether a 38k-line list under `memory/project/` passes memory hygiene's budgets and its pin-gated checks. If it
     cannot, rule the home by the fork rule.
   - The other install-prefix hits: paths spelled as `tools/playbook/...` literals in `core.py` (26), `namespaces.toml` (12), `gov_tag.py` (10),
     `instruction_units.py` (9), `positional.py` (5), `tools/lexicon/selftest.py` (3), `adopt-playbook.sh` (2), `tools/run-gates/py_reads.py` (1)
     and `tools/memory-tree/gotchas.py` (1). Derive each from the file's own location or spell it with the `{prefix}` token, after checking
     the reader resolves `{prefix}` (for `namespaces.toml`'s `source` and `purpose-source`).
   - The 19th drift-audit offender: `namespaces.toml`'s `purpose-source` names a record under `memory/builds/dClosedLoop/`, and a comment in
     `principles.toml` names the same id. Point the row at a non-record anchor as its sibling rows do, and drop the id from the comment.
2. **Unit 73: the rest.**
   - Encoding posture: nine `subprocess.run(..., text=True)` calls with no `encoding=`, in `tools/lib/common_dir.py`,
     `tools/memory-tree/build_records.py` (2), `tools/memory-tree/id_grammar.py`, `tools/playbook/core.py` (2),
     `tools/playbook/instruction_units.py` and `tools/playbook/positional.py` (2). Add `encoding="utf-8"`.
   - Shell hygiene, the loop leg: `tools/unattended/unattended.sh#check_branch_carried` drains a `<<<"$out"` that a substitution fed. Drain it
     without a fork, by `mapfile -t` into an array, never by `< <(printf ...)`.
   - Shell hygiene, the fork leg: six `printf "%s" "$(derive_fx_unit ...)"` in `tools/memory-tree/merge-rows.test.sh` (a no-newline helper
     called directly); `$(dirname -- ...)` in `skills/session-kickoff/manifest-check.test.sh` and `tools/unattended/check-unattended.test.sh`
     (parameter expansion); two `printf ... | sed 's/^/      /'` in `tools/playbook/adopt-playbook.sh` (expansion in one `printf`).
   - Remote literals: `tools/playbook/instruction_units.py#check_unit_row` spells `("status", "origin")` inline; hoist it to a named module constant.
   - Acceptance matrix: `tools/govkit/matrix.py#SCRATCH_EXPECT` lacks the install-day verdicts of 'core selftest', 'tags bundle selftest' and
     'tags positional selftest', taken from a scratch install, never typed. And 'playbook render selftest' fails there because
     `tools/playbook/check_layers.py` resolves the memory-tree kit at import, a kit the scratch install lacks: decide by the fork rule between
     `playbook-render` requiring memory-tree and the import moving inside its use.
   - Policy census: `tools/run-gates/owed_rows.py` spells `budgets.py resolve <words>` in prose and in one message, which the census reads as cap
     names. Reword those lines.
   - Harness arms: three refusal sites in `tools/playbook/adopt-playbook.sh` (the layer-check, tag-resolver and edge-grammar failure exits)
     are neither armed nor pinned. Arm them if a sibling suite fits, else name the pinned rows the main loop writes.
3. **Overlap.** Both units touch `core.py`, `instruction_units.py` and `positional.py`: 72 builds first, and 73's spec says it reads 72's result.
4. **Not these units:** the record fixes (the kickoff manifest stamp, memory hygiene's records, the method-carrier and spawn-idiom rows), and
   the policy check's dFairHearing keys, which the merge with `origin/main` clears.

In each spec:

- Follow `memory/TEMPLATE-SPEC.md`, at `memory/builds/dOrderedCharter/spec/2026-11-08-spec-PLAY-dOrderedCharter-<n>.md`.
- Status `DEFERRED`, rev-1, dated 2026-11-08, base `93c4e987e`, `order 17`, advancing PLAY-dOrderedCharter-38, Tier-2, and the line
  `**Derived:** PLAY-dClosedLoop-2` after the status header, as specs 67 to 71 carry it.
- Declare each new arm on a `New arm:` line, each leg it moves in section 7, and every path in Files touched.
- New text cites code as `path#symbol`, outside the acceptance bullets. An acceptance bullet spells a plain tracked path, with no `#` and no
  `HEAD:` prefix, and never a file not yet tracked. New text names a section in words, and a check by what it checks.
- Any retirement word in section 2 owes its Readers clause.
- Stage each spec, then run the hygiene spec checks (`--only 12,25`).

### Acceptance

- Specs 72 and 73 exist and every code fix above has exactly one owner.

### Gates

Memory hygiene, as your role runs it.

### Non-goals

- No code. No edit to another spec.
