**Serves:** research TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-17 TOOL-dSafePassage-21 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-61

# Brief: the spec-token findings a live dispatch meets, fixed before each unit's builder flips its spec to INPROGRESS (set A)

## The prompt

No owner prompt: TOOL-dSafePassage-8's builder handed back a finished build (`wf_03819140-bb2`) because `--dispatch`'s spec-token check, which skips DEFERRED specs, graded spec 8 once its builder moved it to INPROGRESS and found §7 missing a guarded leg. The main loop then flipped every remaining dSafePassage spec to INPROGRESS in the working tree only, ran `python tools/check-spec-tokens.py` once (exit 1) and restored them; the findings below are that run's, for this set.

## The brief

### Goal

Every spec in this set passes `tools/check-spec-tokens.py` while live, so no builder's `--dispatch` is refused for a spec defect: §7 names every leg whose guard its Files touched trips, each backticked token the path join reads resolves or stops being backticked as a path, each hands-off bullet's token is named by its sibling, and no criterion cites a bar or suite as its observation.

The findings, verbatim from the checker (one per line, `[class] token — reason`):

- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-10.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-12.md [path] `lib/python-floor-3.15` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-13.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-17.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-21.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/shims.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/fixtures/retired_edits.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/upgrade_walk.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/fixture_target.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/govkit/fixture_target.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `tools/unattended/lib-unattended.sh;` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `lib/python-floor-3.15` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [path] `3708a705:tools/govkit/selftest.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [bar] `tools/push-main.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-26.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-29.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-30.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md [path] `.governance/install.json` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md [path] `tools/govkit/usage.toml` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-5.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-6.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-8.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-9.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [path] `tools/govkit/steps/template_size_limits.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [path] `tools/govkit/steps/template_size_limits.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `run-gates canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates canary', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `run-gates gov canary <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'run-gates gov canary', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `measure-legs selftest <- tools/gate-legs.json` — §4 files-touched names tools/gate-legs.json, which trips the guard of leg 'measure-legs selftest', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `transition-audit arms <- .memory-tree.conf` — §4 files-touched names .memory-tree.conf, which trips the guard of leg 'transition-audit arms', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `straggler-guard arms <- .memory-tree.conf` — §4 files-touched names .memory-tree.conf, which trips the guard of leg 'straggler-guard arms', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-26-spec-TOOL-dSafePassage-61.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-9.md [handoff] `TOOL-dSafePassage-9>TOOL-dSafePassage-13:read_policy_value(key, root, rev=None)` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work

### Items

1. **`[guards]`**: add each named leg to that spec's §7 leg line, exactly as `tools/gate-legs.json` spells it (`policy fixtures` covers `{prefix}/govkit/govkit.py` and `{prefix}/govkit/selftest.py`). Add nothing else to §7.
2. **`[path]`**: a token that is a git revision path (`3708a705:...`), a URL, a config key, a code expression or a scratch path is not a repository path: change its markup so the join does not read it as one (the form `memory/TEMPLATE-SPEC.md` and sibling specs use — e.g. split the expression from the path, or move a literal value out of backticks), never by inventing a waiver. A token that names a file this unit or a later one CREATES belongs in §4 Files touched, which the join skips; move or restate it there if it is cited elsewhere as if it existed.
3. **`[handoff]`**: name the token in the sibling's own spec where the sibling consumes it, or correct the bullet if it hands the wrong token.
4. **`[bar]`**: rewrite the criterion to observe the checker on a staged break, a fixture or a `--selftest` flag, and name the suite on the `New arm:` line instead.
5. Each spec you change takes a rev bump dated 2026-10-26, still `DEFERRED`, and one §9 line naming this brief. Change no criterion's meaning, decision or Carries line beyond what the item needs.
6. **Commit nothing.** Return the files you wrote.

### Acceptance

- Re-run the probe over YOUR set only: in a scratch copy of the index or working tree, flip your set's specs to `INPROGRESS`, run `python tools/check-spec-tokens.py`, and report that no line names a spec in your set; restore the status before returning. If the scratch guard refuses the checker for your role, say so and the main loop runs it.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them other than check 9's stale build index.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code, no edit of a CLOSED spec, no spec outside this set (the other set has its own writer).
- No commit, no stage into the real index, no waiver row.
