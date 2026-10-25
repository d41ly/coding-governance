**Serves:** research TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79

# Promoted-fix brief — the round-4 promotions, before their commit

Fix the four specs the round-4 spec audit's disposal added, `TOOL-dDeclaredLoop-76` to `-79`, so
`python tools/check-spec-tokens.py` names no dDeclaredLoop spec and `bash tools/memory-tree/check-memory-hygiene.sh
--only 12,25` prints no dDeclaredLoop line, changing nothing else.

- Each `[path]` hit below: cite a file the build run will create by BASENAME in §6, full paths staying in §2, §4 and
  Files touched, as earlier rounds did. A URL a fixture plants (`ssh://…`, `https://…`) is a literal, not a path:
  spell it so the checker does not read it as one, for example by naming the planted remote in prose and giving
  the literal in a fenced block or in §4, keeping the criterion's observation unchanged.
- Each `[bar]` hit: a bar or suite is not an acceptance observation. Re-express the criterion as the observation of
  the unit's own code (the checker on a staged break, a fixture, a probe of the function, or a citation of the
  pinned lines), or move a needed suite arm to a `New arm:` line in §7.
- Each check-12 hit (an acceptance bullet naming no backticked witness): give the bullet the backticked command or
  file that observes it.
- The specs are uncommitted at rev-1, so edit them in place with no rev bump. Touch no deviation record and no spec
  numbered 1 to 75.
- Do not commit, do not stage, do not run the build-index generator. Re-run the hygiene checks (`--only 12,25`) and
  report each file changed and the dDeclaredLoop lines left.

## The hits, verbatim

- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md [path] `ssh://user@example.com/up.git` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-77.md [path] `https://u:SECRET@127.0.0.1:9/r.git` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [path] `tools/loop/commit_trailers.py` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [path] `tools/loop/kit.toml` — not tracked by git ls-files
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [bar] `tools/govkit/selftest.py` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md [bar] `tools/govkit/selftest.py` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
- memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-79.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC10
