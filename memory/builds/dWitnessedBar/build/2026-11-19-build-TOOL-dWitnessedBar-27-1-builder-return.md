**Serves:** journal TOOL-dWitnessedBar-27

# TOOL-dWitnessedBar-27 — builder return 1 (run `wf_0f50444e-10c`), a divergence, nothing committed

## Why

DIVERGENCE: the spec memory/builds/dWitnessedBar/spec/2026-10-25-spec-TOOL-dWitnessedBar-27.md (rev-4) can't be built as written. I checked it against the tree at a50c0a56c and found four problems.

(1) §2 S5, §4 Inventory and the §7 `New arm:` line all create "section `2k`" in tools/lib/resolve-python.test.sh. That name is already used: `# ---- 2k. THE JS KIT RESOLVER PORT, BEHAVIOUR (TOOL-dFairHearing-32 S26)` is at :814, and 2l (:919) and 2m (:941) come after it. The spec has to name a free section, such as `2n`, in S5, Inventory and the New arm line.

(2) §4 "The population" pins 75 files ("PINNED, measured 2026-10-25": 70 inline carriers plus 5). That count no longer holds. Today `git grep -l '^# >>> resolve_python' -- tools skills .githooks` lists 83 files: 82 `.sh` plus `.githooks/pre-push`. Adding the files that name `resolve-python.sh` gives 95. (DERIVED, measured at `a50c0a56c`)
- The 20 files missing from Files touched: .githooks/pre-commit, .githooks/pre-commit.test.sh, tools/chain-packet.test.sh, tools/check-line-length.sh, tools/check-microformats.sh, tools/check-template-size.sh, tools/govkit/fixtures/release-0/deploy.toml, tools/govkit/registry.toml, tools/govkit/upgrade_steps.py, tools/lib/python-floor.sh, tools/loop/adopt-loop.sh, tools/memory-tree/corpus_ids.py, tools/playbook/adopt-playbook.sh, tools/policy/adopt-policy.sh, tools/policy/policy-shim.sh, tools/push-main.test.sh, tools/run-gates/pass-legs.sh, tools/unattended/check-brief-recorded.sh, tools/unattended/check-pass-order.sh, tools/workflows/spec-audit-optin.test.sh. (DERIVED, measured at `a50c0a56c`)
- Four of these only mention the name in prose and are not entry points: tools/govkit/registry.toml@aec2b8e3:240, tools/govkit/fixtures/release-0/deploy.toml@ad0b013a:48, tools/govkit/upgrade_steps.py@a814a6ae:462, tools/memory-tree/corpus_ids.py@242b5465:441.
- The spec has to re-pin the count, list the new entry points in Files touched, and say that prose-only mentions are outside the population.

(3) §4 Files touched lists `tools/govkit/govkit.py` as a copy of the resolver blocks, but it has no `resolve_bash_py` block. The list also leaves out three files that do have one: tools/loop/loop_witness.py (:106), tools/playbook/render_playbook.py (:138) and tools/policy/policy-mirror.js (:56).

(4) §2 S3 and AC5 don't say how the two shared library files carry the refusal.
- AC5's set includes tools/lib/resolve-python.sh, because it holds the `# >>> resolve_python` block. But it is a source-only library and never calls `resolve_python`, so S3's rule "before its first `resolve_python` call" gives no position for the call.
- S3's "sources `refuse-wrong-shell.sh` beside it" breaks if resolve-python.sh itself does the sourcing. These fixtures copy only resolve-python.sh into a scratch lib dir, so the missing sibling would make `refuse_wrong_shell || exit 2` exit 2 there: tools/memory-tree/merge-rows.test.sh@8ee4551f:850, :1903, :1961; tools/run-gates/run-gates.test.sh@37b9b01d:2309, :2352, :2429; tools/run-gates/run-gates.evidence.test.sh@88378836:483, :1097; tools/run-gates/run-gates.turnstile.test.sh@301faae7:331.
- The spec has to choose for resolve-python.sh: an inline block plus a call when it is sourced, or a separate rule for library members. That also covers tools/lib/pyrun.sh, which sources it at :29.

Nothing was written. The worktree is as I found it, with only the pre-existing staged RUN.md. I also did not run the `--brief` record verb, because it writes RUN.md and this pass commits nothing.

## Summary

TOOL-dWitnessedBar-27 is not built: the spec doesn't match the current tree, so nothing was written or committed. The `why` field lists the four mismatches, each with the spec section that needs revising.

Checks I ran (all read-only probes; none stands in for a gate):
- `git rev-parse HEAD` gave the base, a50c0a56c50caf5edd7d5f58d9dfa27b17d58f42.
- Read tools/lib/resolve_bash.py, tools/lib/resolve_bash.js, and the PARITY_ROWS table and section headings in tools/lib/resolve-python.test.sh.
- Re-counted the population with `git grep -l` and compared it to the spec's list: the spec has 75 files, the tree has 95. (DERIVED, measured at `a50c0a56c`)
- Listed every file holding a `resolve_bash_py` or `resolve_bash_js` block: 17, including the two canonicals.
- Checked how tools/lib/pyrun.sh sources resolve-python.sh, and which test fixtures copy only resolve-python.sh into a scratch lib dir.
- Checked WSL on this machine for AC1, AC2, AC4 and AC6: WSL's `pwd` in this worktree's tools/lib is a `/mnt/c/` path, `WSL_DISTRO_NAME` is Ubuntu, `/usr/bin/python3` is present, and `node` is missing, so AC6's JavaScript half would fall back to the AC7 truth table as the spec allows.

No criterion was observed and no arm is owed yet. Nothing ran past its time limit and nothing was skipped. I did not run the `--brief` record verb, because it writes memory/builds/dWitnessedBar/RUN.md and this pass commits nothing. I did not run the gotchas checklist either: there is no commit for it to read.

Once the spec is revised, the next dispatch will owe the RED-first observation of the New arm in tools/lib/resolve-python.test.sh, covering AC5 and AC7, at the close.
