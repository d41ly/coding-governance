**Serves:** research TOOL-dSafePassage-3

# Brief: TOOL-dSafePassage-3's S5 says what a re-run over an existing receipt writes

## The prompt

No owner prompt: the build run's builder handed TOOL-dSafePassage-3 back as a DIVERGENCE before writing code
(`wf_c9c7c9a6-fee`), and the run revises the spec under M2.

## The brief

### Goal

S5 states what `apply` and `adopt --re-adopt` write when a prior receipt exists, so that a re-run over a schema-4 receipt keeps its `steps` rows and a re-run over a schema-3 receipt never lifts it to schema 4 without the step `govkit/receipt-schema-4`, and every sibling spec agrees.

**The defect.** S5 says `apply` and `adopt` "write a fresh receipt at schema 4 with `"steps": []`", and also "schema 4 on an existing receipt is the step's alone". At HEAD `2ac1c347` neither write is always a fresh receipt:

- `apply` reads the prior receipt (`tools/govkit/govkit.py:7570`), rebuilds `_rcpt_doc` from scratch at `:8014-8025` carrying only `orders`, `after` and `gate_runner` forward, and rewrites it at `:8330` and `:8436`.
- `adopt --re-adopt` (`:13114-13136`) carries exactly five install-record keys from the receipt it replaces — `orders`, `baseline`, `after`, `hook_block`, `gate_runner` — under the code's own D2 rule: a key that records an EVENT is carried verbatim, never re-measured.

As written, (a) a re-apply or re-adopt over a schema-4 receipt replaces `steps` with `[]`, erasing every `applied`, `failed` and `rolled-back` row so the next walk re-runs or re-applies steps the operator ran or rolled back; (b) the same over a schema-3 receipt lifts an existing receipt to schema 4 without the step, which S5's last sentence and §8 F2's reasoning forbid.

**The direction.** The builder's reading, which satisfies both halves of S5: `steps` is an event-recording key, carried verbatim by `apply`'s rebuild and added to `adopt`'s carried keys; a prior receipt's schema below 4 is kept as it is, so only a FIRST install (no prior receipt) is born at schema 4 with `"steps": []`. Take it unless the specs or code show it breaks a criterion already written; if it does, that is a fork for §8, marked as `memory/TEMPLATE-SPEC.md` states.

### Items

1. **Revise TOOL-dSafePassage-3** as a rev bump dated 2026-10-26, still `DEFERRED`: S5 states the first-install and re-run cases; the §4 Inventory rows for `apply` and `adopt` name the re-run behaviour at their current lines (`:8014-8025`, `:8330`, `:8436`, `:13114-13136`); §8 F3's wording matches; an acceptance criterion observes the re-run case on a planted schema-4 receipt carrying a `steps` row and on a planted schema-3 receipt, each re-applied and re-adopted, and the selftest `New arm:` line's `covers` list names it. Refresh every govkit.py line the spec cites to HEAD while you are in it (constant :50, back-fill :9377-9387, integrity message :9441-9445, re-stamp :12475, adopt envelope :13098, apply :8015, check :5449). One §9 line names this brief.
2. **Cross-read every sibling spec** that writes or reads the receipt's `steps` or its schema — at least TOOL-dSafePassage-15, -16, -19 and -20, and -2 and -4 for the walk — on M2's four axes. Fix a disagreement in exactly the one document that is wrong, as a rev bump with a §9 line naming this brief.
3. **Commit nothing.** Return the files you wrote; the main loop commits them.

### Acceptance

- `grep -n '"steps": \[\]' memory/builds/dSafePassage/spec/2026-10-23-spec-TOOL-dSafePassage-3.md` prints only lines that name a first install.
- The new criterion names both planted receipts and both commands.
- `bash tools/memory-tree/check-memory-hygiene.sh --staged`, run over a copy of the index with only your files staged through `GIT_INDEX_FILE`, names no finding in them.
- `bash tools/unattended/unattended.sh --plan dSafePassage --paths` lists TOOL-dSafePassage-3 READY.

### Gates

Only the memory hygiene gate (`--staged`, over a copy of the index) and the naming lexicon, as the role allows.

### Non-goals

- No product code.
- No commit, no stage into the real index, no deviation record: the main loop writes those.
- No change to the receipt's other carried keys or to D2's rule.

### Reuse

`tools/govkit/govkit.py:13114-13136`'s carried-keys list is the seam the re-adopt case extends; the 2026-10-26 TOOL-dSafePassage-61 brief in this folder for the shape of a build-run revision.
