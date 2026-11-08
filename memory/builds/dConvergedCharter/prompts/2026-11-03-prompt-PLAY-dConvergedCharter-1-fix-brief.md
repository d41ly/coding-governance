**Serves:** research PLAY-dConvergedCharter-1 PLAY-dConvergedCharter-2 PLAY-dConvergedCharter-3 PLAY-dConvergedCharter-4 PLAY-dConvergedCharter-6 PLAY-dConvergedCharter-7 PLAY-dConvergedCharter-8 PLAY-dConvergedCharter-11 PLAY-dConvergedCharter-12 PLAY-dConvergedCharter-14 PLAY-dConvergedCharter-16 PLAY-dConvergedCharter-17 PLAY-dConvergedCharter-18 PLAY-dConvergedCharter-19 PLAY-dConvergedCharter-21

# Fix brief — dConvergedCharter, the spec stage's mechanical reds

The six writers authored all 23 specs under `memory/builds/dConvergedCharter/spec/`, staged and NOT committed. The main
loop ran the checks the spec brief names over them, and every red below is a finding in exactly one file. Fix each in
place, in the file it names, and nothing else: no design change, no new scope, no edit to a file this list does not
name. The specs have never been committed, so a fix stays at `rev-1` and owes no §9 line. Read the spec brief
`memory/builds/dConvergedCharter/prompts/2026-11-03-prompt-PLAY-dConvergedCharter-1-spec-brief.md`, section "What the
last spec runs had to fix after their writers returned", before the first edit. Spec paths below are
`memory/builds/dConvergedCharter/spec/2026-11-03-spec-PLAY-dConvergedCharter-<n>.md`, written `spec <n>`.

## Hygiene check 25 — a retirement with no complete `**Readers:**` clause

- spec 4, S7: the item retires a named thing and carries no `**Readers:**` clause. Write one: `by name:` and every
  reader that spells the name, then `by value:` and every reader of its value, or `NO VALUE READERS` and a reason;
  find each reader with `git grep` over the tree, never from a record.
- spec 4, S3: its `**Readers:**` clause has no `by value:` half after its `by name:`. Add it the same way.

## Hygiene check 12 — a one-sided §3 edge

- spec 14 declares no `consumes-from` `PLAY-dConvergedCharter-15` back for spec 15's `hands-off`
  `PLAY-dConvergedCharter-14` (`fates.toml`, the four `[[part]]` rows of spec 15's S1). Add it to spec 14's §3,
  naming `fates.toml`, and read those rows where spec 14 materializes the table.
- spec 6 declares no `hands-off` `PLAY-dConvergedCharter-2` back for spec 2's `consumes-from`
  `PLAY-dConvergedCharter-6` (`record_kinds.py`, read through a `--homes` print mode). Add the hands-off to spec 6's
  §3 naming `record_kinds.py`; if spec 6 does not provide the `--homes` mode spec 2 reads, state in spec 6 which unit
  adds it, as spec 2 says it does, so the two agree.

## Hygiene check 30 — a clause departure with no amends row

The as-built view refuses a deviation that departs from a clause and carries neither `amends` nor `supersedes` in its
`**Follow-through:**`. Each needs the amends form the passing records use (deviations 161, 201 and 81 of this build;
`memory/builds/dDeclaredLoop/build/2026-10-24-build-TOOL-dDeclaredLoop-6-deviation-61.md`):
`- **Follow-through:** amends <clause id>@<hash8>`. Keep each record's other fields; where the old follow-through named
something still owed (an ask, a scope item), move it into the record's `**Reason:**` or the spec's §2 so it is not lost.

- `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-11-deviation-111.md` —
  `cl-dClosedLoop-0485@dde21704` (today: `ask PLAY-dConvergedCharter-24`).
- `memory/builds/dConvergedCharter/build/2026-11-03-build-PLAY-dConvergedCharter-19-deviation-191.md` —
  `cl-dClosedLoop-0493@0d92d2e3` (today: `PLAY-dConvergedCharter-19 S6 and S8`); its `**Departs from:**` also carries a
  trailing `whole`, which no passing record carries: drop it.

The main loop re-renders the as-built view after you return and settles each spec's `**Carries:**` hash from it.

## `tools/check-spec-tokens.py` — the §7 leg line misses a leg its files trip

Each spec's §4 files-touched names a path that trips the guard of a leg its §7 leg line does not name. Add each leg to
that spec's §7 leg line, spelled exactly as quoted:

- spec 12, spec 16 and spec 17: `playbook render selftest` (from `tools/playbook/`).
- spec 18: `recall floor arms`, `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix` (from
  `tools/govkit/registry.toml`).
- spec 3: `recall floor arms`, `govkit refusal join`, `govkit acceptance matrix` (from
  `tools/govkit/steps/memory_journal_alias.py`).
- spec 6: `kit/dogfood doc parity`, `recall floor`, `recall floor arms` (from `memory/HYGIENE.md`).
- spec 7: `manifest-check self-test`, `lexicon naming predicates` (from `skills/session-kickoff/manifest-check.sh`),
  `govkit selftest`, `govkit refusal join` (from `tools/govkit/fixtures/release-0/deploy.toml`).

## `tools/check-spec-tokens.py` — other hits

- spec 21: `house/policy.toml` is read as a path no file tracks. Spell it `tools/roles/house/policy.toml` wherever the
  short form stands as a path.
- spec 8: an acceptance criterion names `bash tools/workflows/check-protocol-parity.test.sh`, and a bar or suite is not
  an acceptance observation. Observe the checker on a staged break, a `--selftest` flag or a fixture instead, and name
  the suite on a `New arm:` line in §7.
- spec 14: spec 20 hands it `check_adopters_converged`, which spec 14 never names. Name it in spec 14 where its
  `check --exit` runs spec 20's adopter exit arm beside the join (its `consumes-from` `PLAY-dConvergedCharter-20` line
  and the S-item that runs it).
- spec 11: the carries join finds two of clause `cl-dClosedLoop-0485`'s tokens in none of its carriers:
  `INHERITED_RED=park` and `roles_lib.load_policy`. Write each verbatim, in backticks, where spec 11 already means it
  (the scratch-clone proof that plants `park`; the house-file fallback that retires).

## Shared-interface agreement — one spelling across two specs

- spec 12 writes the explanation edge as `explains=<guide path>#<seg>`. Unit 7, I21's owner, refined it to
  `explains=doc.<name>#<seg>`, because PLAY-dOrderedCharter-24 S4 reds a target outside the `doc` namespace. Change
  spec 12's spelling to unit 7's wherever it appears.

## What you return

One line per item above: the file, what you changed, and anything you could not fix as asked with the reason. Run
`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,25` before returning and quote any red it prints on these files.
