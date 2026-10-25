**Serves:** research TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34

# Promoted fix brief — dPlacedRequest, the round-1 promotions' gate hits

The round-1 spec audit's disposal added TOOL-dPlacedRequest-23 to -34 under `memory/builds/dPlacedRequest/spec/`,
closing the findings of `memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`,
and folded a hands-off edge into the roster specs they amend. Read the spec brief
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md` ("Every spec, whatever
its unit", "Shared interfaces", "Edges") and the first fix brief
`memory/builds/dPlacedRequest/prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md` (its rules per hit class
bind here too) first. Fix every hit below by editing the named spec, and nothing else: no product code, no commit, no
index render, no `**Carries:**` or `**Derived:**` line. A fix that changes a spec's design is out of scope; a hit you
judge false goes in your return with the reason.

Two classes the first brief did not meet:

- **[bar]**: a criterion names a suite as its observation. Observe the checker or the function on a staged break or
  a fixture instead, and move the suite to a `New arm:` line in §7 if a new arm is owed.
- **[size]**: TOOL-dPlacedRequest-34 is over the 49152-byte spec ceiling (`tools/template-size-limits.txt`). Cut it
  under the ceiling by tightening prose and dropping repetition, never by dropping a finding the unit closes: every
  finding id its rescope row in `memory/builds/dPlacedRequest/RUN.md` names stays closed by a scope item and a
  criterion.

A path to a file a dDeclaredLoop or dOrderedCharter unit creates (`tools/loop/loop_lib.py`,
`tools/playbook/tag_index.py`) is cited the same way as one this build creates: by basename in §6. A node-local
file under the git common dir (`requests/<key>.md`) and a ref name are written so they are not read as a repository
path, for instance with the `<git-common-dir>/` prefix the shared interfaces spell.

Bump each edited spec's rev and add its §9 line. When done, run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` (the specs are staged) and return each hit's
disposition; the main loop runs `check-spec-tokens.py`.

## The hits

```text
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md [path] `tools/lib/gov-feed.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md [path] `tools/lib/gov-feed.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md [path] `requests/<key>.md` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-30.md [path] `requests/<key>.typed` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md [path] `requests/<key>.md` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md [path] `requests/<key>.typed` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-31.md [path] `requests/<key>.typed` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-32.md [path] `requests/<key>.typed` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md [path] `skills/session-kickoff/card-store.fixture.sh` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [path] `tools/loop/loop_lib.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [path] `refs/gov/remote/runs/tFix.lock` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [path] `skills/session-kickoff/RESUME.md` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [path] `tools/playbook/tag_index.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [path] `tools/loop/request.py` — not tracked by git ls-files
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [bar] `.githooks/pre-push.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [bar] `tools/hooks/scratch-guard.test.sh` — a bar or suite is not an acceptance observation: observe the checker on a staged break, a --selftest flag or a fixture; name the suite under New arm:; the bar and the suites run once, after the build is complete
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md [handoff] `TOOL-dPlacedRequest-24>TOOL-dPlacedRequest-34:write_node_lock` — this bullet hands the token to that sibling and the sibling's own spec never names it: name it there, or correct the bullet — the join proves the sibling NAMES the token, never that it does the work
spec-tokens: memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md [size] `size <- memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md` — 50800 bytes, 1648 over the spec ceiling 49152; split the spec or move history out of it
HYGIENE check 12 FAILED — spec files dated >= 2026-07-15 not conforming to memory/TEMPLATE-SPEC.md:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (acceptance bullets naming no backticked witness, required at/after SPEC_WITNESS_CUTOFF): 2026-08-15 -- AC25
HYGIENE check 25 FAILED — §2 scope items of LIVE specs that retire a named thing, and every **Readers:** clause, must answer by name: with names a reader spells and by value: with a reader or NO VALUE READERS and a reason:
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-24.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S1
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (§2 items that retire a named thing carry no **Readers:** clause; write **Readers:** then by name: and the readers that spell the name, then by value: and the readers of its value, or NO VALUE READERS and a reason): S2, S15, S30, S38
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (§2 items whose **Readers:** clause carries no by name: half; write by name: and the readers that spell the name, or READER NOT IN TREE and a reason): S35
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (§2 items whose **Readers:** clause carries no by value: half after its by name:; write by value: and the readers of the value, or NO VALUE READERS and a reason): S26
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md (§2 item S3: by name: lists `gov_ref_sh`, which no reader spells and no tracked path is or ends with; name a reader that spells it, or write READER NOT IN TREE and a reason on that half)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-33.md (§2 item S3: by name: lists `gov_feed_sh`, which no reader spells and no tracked path is or ends with; name a reader that spells it, or write READER NOT IN TREE and a reason on that half)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (§2 item S8: by name: lists `refs/gov/builds/<slug>/card`, which no reader spells and no tracked path is or ends with; name a reader that spells it, or write READER NOT IN TREE and a reason on that half)
memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md (§2 item S8: by name: lists `TOOL-dPlacedRequest-2`, which no reader spells and no tracked path is or ends with; name a reader that spells it, or write READER NOT IN TREE and a reason on that half)
```
