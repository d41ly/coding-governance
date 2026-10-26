**Serves:** research TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-59

# Brief: the spec-token findings a live dispatch meets, fixed before each unit's builder flips its spec to INPROGRESS (set B)

## The prompt

No owner prompt: TOOL-dSafePassage-8's builder handed back a finished build (`wf_03819140-bb2`) because `--dispatch`'s spec-token check, which skips DEFERRED specs, graded spec 8 once its builder moved it to INPROGRESS and found §7 missing a guarded leg. The main loop then flipped every remaining dSafePassage spec to INPROGRESS in the working tree only, ran `python tools/check-spec-tokens.py` once (exit 1) and restored them; the findings below are that run's, for this set.

## The brief

### Goal

Every spec in this set passes `tools/check-spec-tokens.py` while live, so no builder's `--dispatch` is refused for a spec defect: §7 names every leg whose guard its Files touched trips, each backticked token the path join reads resolves or stops being backticked as a path, each hands-off bullet's token is named by its sibling, and no criterion cites a bar or suite as its observation.

The findings, verbatim from the checker (one per line, `[class] token — reason`):

- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-31.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-32.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-33.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [path] `{prefix}/process-monitor/census.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [path] `tools/govkit/step_gate.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-35.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-36.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-37.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [path] `render_redacted_config("http.https://u:p@h/.extraheader")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [path] `http.https://<redacted>@h/.extraheader` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-38.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-39.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-40.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-41.md [path] `commit>:tools/check-spec-tokens.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [path] `3708a705:tools/push-main.sh` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [path] `3708a705:tools/govkit/govkit.py` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-42.md [guards] `policy fixtures <- tools/govkit/govkit.py` — §4 files-touched names tools/govkit/govkit.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [path] `("url.ssh://git@github.com/.insteadof",` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `C:/x/sendmail.exe` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `url.https://first.last:dsppass45@host/.insteadof` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `test_credential_bearing("url.https://first.last:pw@host/.insteadof",` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `url.ssh://git@github.com/.insteadof` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `render_redacted_config("http.https://u:p@ss@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [path] `http.https://<redacted>@h/.sslkey` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-45.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-47.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-48.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `ssh://git@github.com/o/r.git` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `cret@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `render_redacted_config("http.https://u:se/cret@h/.sslkey")` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [path] `http.https://<redacted>@h/.sslkey` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-49.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-51.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-52.md [path] `tools/push-main.test.sh)";` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-53.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-54.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-56.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-57.md [path] `3708a705:tools/push-main.test.sh` — not tracked by git ls-files
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-59.md [guards] `policy fixtures <- tools/govkit/selftest.py` — §4 files-touched names tools/govkit/selftest.py, which trips the guard of leg 'policy fixtures', absent from the §7 leg line
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-44.md [handoff] `TOOL-dSafePassage-44>TOOL-dSafePassage-45:ssh-scheme-bare-user` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
- memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-48.md [handoff] `TOOL-dSafePassage-48>TOOL-dSafePassage-49:sendemail.<key>` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work

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
