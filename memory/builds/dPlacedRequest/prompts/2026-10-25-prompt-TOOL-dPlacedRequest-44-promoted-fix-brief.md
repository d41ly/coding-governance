**Serves:** research TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49

# Promoted fix brief — dPlacedRequest, the round-3 promotions' gate hits

The round-3 spec audit's disposal added TOOL-dPlacedRequest-44 to -49, closing the findings of
`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`. Read the first fix
brief, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md`, and the round-1
promoted fix brief, `memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md`:
their rules per hit class bind here. Fix every hit below by editing the named spec, and nothing else: no product code,
no commit, no index render.

One class the earlier briefs did not meet:

- **[carries] unbound**: a spec this build's audit promoted carries no clause, so it binds to the decision that
  derives it. Add the line `**Derived:** PLAY-dClosedLoop-2` at column 0 on its own line, directly below the status
  header and its blank line, exactly as `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-35.md`
  line 5 does. This is the only binding-line edit allowed.
- **check 12, failure mode**: the named acceptance bullet names an observation but no failure mode; add the
  red case it catches, as its sibling criteria do.

Bump each edited spec's rev and add its §9 line. Run `bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25`
(the specs are staged) and return each hit's disposition; the main loop runs `check-spec-tokens.py`.

## The hits

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md [path] `help/loop.md` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md [bar] `scratch-guard.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md [bar] `manifest-check.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-44.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-45.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-46.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-48.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-48.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md [carries] `carries <- unbound:memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md` — carries nothing and is derived from nothing: a chain spec names the clause or node it carries, or the decision it derives from
HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-49.md (acceptance bullets naming no failure mode, required at/after SPEC_FAILURE_MODE_CUTOFF 2026-09-08): AC26
```
