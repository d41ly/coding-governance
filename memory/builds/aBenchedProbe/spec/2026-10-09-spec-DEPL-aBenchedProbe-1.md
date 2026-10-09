# DEPL-aBenchedProbe-1 — govkit selfcheck reds a descriptor self-test leg whose subject is not `kit`

**Status:** CLOSED · rev-1 · 2026-10-09 · node a · Tier-1 · base 2b26f187 · streams deployer · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-1-spec-brief.md) | journal | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-2 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1-2-build-brief.md) | journal | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-2 |
| [2026-10-09-prompt-TOOL-aBenchedProbe-1.md](../prompts/2026-10-09-prompt-TOOL-aBenchedProbe-1.md) | research | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-2 |
| [2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md](../reviews/2026-10-09-review-TOOL-aBenchedProbe-1-closing-diff-round1.md) | diff-review | TOOL-aBenchedProbe-1 TOOL-aBenchedProbe-2 DEPL-aBenchedProbe-2 |

<!-- /gen:spec-records -->

## 1. Goal

A new `govkit selfcheck` arm refuses any `[[gate_leg]]` that gov holds as a self-test but ships to
adopters unheld. The three hook self-tests reached every adopter bar that way, at up to an hour a
bar, and nothing in the deployer could see it. The owner's scope item (c) asks that the class cannot
recur.

## 2. Scope (IN)

- **S1** — A new arm `7j4` in `selfcheck` in `tools/govkit/govkit.py`, placed directly after `7j3`
  and reusing its loop over `descs` with `canonical_ctx` and `resolve_tokens`. It reads gov's leg
  manifest chunk from the `manifest_chunk` map the `7h` block already builds from
  `tools/gate-legs.json`. It adds no second descriptor reader and no second manifest load. Observed
  by AC1 and AC2.
- **S2** — The predicate. A leg is SELF-TEST-SHAPED when its manifest chunk is `selftests`, OR when
  the basename of any resolved argv element matches `*.test.sh`, `test_*.py` or `*selftest*`. The
  last glob also matches the bare `--selftest` flag, so no separate flag clause is written. A leg is
  EXEMPT when its manifest chunk is present and is not `selftests`: gov has classified it as a check
  it runs on every bar, and `tools/govkit/subject-pins.tsv` pins that chunk, so moving a leg there
  shows in a diff. The arm REDS a self-test-shaped, non-exempt leg whose descriptor `subject` is not
  `kit`. Observed by AC1, AC2 and AC3.
- **S3** — The refusal names the entry, the leg, what matched (the chunk or the argv element) and
  both fixes. Either hold it everywhere, with `subject = "kit"` in the descriptor and the manifest
  and then `selfcheck --write`. Or run it everywhere, by filing it in a chunk other than `selftests`.
  Observed by AC1.
- **S4** — Liveness and honesty. The arm's note line prints how many legs it graded, how many were
  self-test-shaped, and the names of the exempt ones. The arm reds when it graded zero legs, and
  when it found zero self-test-shaped legs. Its header comment says what it does NOT check, as §4
  lists. The counts are observed by AC3; the zero-population reds are NOT OBSERVED, because staging
  either needs every descriptor leg or the manifest's chunk field removed, which no direct check here
  can do without rewriting gov's registry.

## 3. Non-goals (OUT)

- Not flipping the three push-main legs to `kit`. That is `TOOL-aBenchedProbe-1`, and this arm reds
  the real tree until it lands, which is why this unit is `order 2`.
- Not grading legs that reach an adopter outside `[[gate_leg]]`. The `run-gates canary` is one, and
  `TOOL-aScouredKit-27` stays open for it.
- Not grading `[[exempt_leg]]` rows. They ship to no adopter. `pre-push run-log line` is one: it runs
  a `*.test.sh` with subject `repo` in chunk `selftests`, and it is held on gov's bar and withheld
  from every target, so it is outside this class.
- Not judging whether gov's chunk classification is right. The subject pin grades that as change only.
- Not making `chunk` travel to adopters. Subject already travels, and this arm makes the two agree at
  the source instead.
- Not adding a fixture arm to `tools/govkit/selftest.py`. The arm runs on every gov bar against the
  real descriptors through the `govkit selfcheck` leg, and its S4 liveness reds catch a predicate that
  stops matching. A fixture would grade the same lines a second time, inside a suite this build does
  not run.
- No kit-version bump inside this unit. The build bumps each touched kit once, after the last unit.
- No edit to `memory/DECISIONS.md`, any backlog, `WIRE-INTO-PROJECT.md` or anything aThriftyLanding
  owns.

### Edges

- **consumes-from** `TOOL-aBenchedProbe-1` — the three push-main legs declared `subject = "kit"` in
  the descriptor, the manifest and the pin file. Without it this arm reds the real tree on those
  three, and the build cannot close.

## 4. Design

### The predicate, reduced to what it decides today

Every one of the 128 rows in `tools/gate-legs.json` carries a chunk (counted at BASE on 2026-10-09;
re-derived by the S4 note line, which counts the population it grades). So the filename clause
cannot red any leg in today's tree: a leg it matches either sits in `selftests`, where the chunk
clause already matched it, or sits in another chunk and is exempt. In today's tree the arm therefore
decides `chunk == selftests AND subject != kit`, which is the exact disagreement between gov's hold
and the adopter's hold. The filename clause has one live population, a manifest row with NO chunk.
That is the shape a new leg takes when its author forgets the field, and run-gates then files it
under `default` and runs it on every bar. The header comment states this reduction, so a reader does
not take the filename clause for coverage it does not have.

### Measured at BASE

The enumeration, run as a read-only probe through `govkit.load_registry`, `read_descriptors`,
`canonical_ctx` and `resolve_tokens`, over the real tree on 2026-10-09:

| fact | count |
|---|---|
| descriptor `[[gate_leg]]` rows graded | 59 |
| self-test-shaped | 22 |
| would red: `push-main self-test`, `pre-push self-test`, `pre-push bar self-test` | 3 |
| exempt, chunk `declarations`: `kit/dogfood doc parity`, `marker contracts`, `review-protocol parity (kit vs dogfood)` | 3 |
| shaped, subject `kit`, pass | 16 |

The three exempt legs are the ones `TOOL-aQuenchedHarness-3` §3 says adopters SHOULD run. One
near-miss by NAME: `testsuite counts (every bar self-test prints one)` says self-test in its name and
runs `check-testsuite-counts.sh`, a repo check. The predicate reads argv and chunk, never the name,
so it does not match, which is right.

### Placement

`manifest_chunk` is bound only inside 7h's `if legs_path.is_file():`. The build initialises it to an
empty map ahead of that `if`, so 7j4 can read it unconditionally. When the manifest is absent, the
arm prints a refusal naming the missing manifest instead of grading, because without chunks it
cannot tell an exempt leg from a held one.

### What the header comment says it does NOT check

- Legs outside `[[gate_leg]]`, such as `run-gates canary`, and `[[exempt_leg]]` rows.
- Whether gov's chunk value is right; `subject-pins.tsv` grades that as change only.
- A self-test whose file name matches none of the three globs, and an argv element that runs one
  indirectly, for example through `sh -c`.
- That an exempt leg is cheap. Exemption means gov runs it on every bar too, so its cost is gov's to
  see.

### Inventory

One arm label, `7j4`, beside `7j3`. No new function, so no lexicon cell is graded.

### Files touched (estimate)

- `tools/govkit/govkit.py`

### Alternatives rejected

- **A filename predicate alone.** It reds the three `declarations` legs adopters must run, which is
  why `TOOL-aQuenchedHarness-3` rejected a filename-derived HOLD predicate.
- **A hand-kept exemption list in the registry.** It would be a second copy of the chunk
  classification gov already owns and pins.
- **Exempting only the `declarations` chunk.** See §8 F1.

## 5. Production-readiness checklist

- security: N/A — a read-only check over gov's own descriptors; no write path.
- perf / scale: one pass over 59 legs inside a loop that already runs; no new subprocess or file read.
- error / empty / loading states: a missing manifest is a named refusal (§4 Placement); an empty
  population reds (S4).
- observability: the note line prints graded, shaped and exempt counts on every run.
- risks: reds the real tree until `TOOL-aBenchedProbe-1` lands; the `order 2` header sequences it.
- testing: AC1 to AC3, each a direct `govkit selfcheck` run on a staged break or on the clean tree.
- migration: N/A — no data shape changes.
- user docs: N/A — no user-facing `help/` surface; the arm's refusal text is its documentation.

## 6. Acceptance criteria

- **AC1** — When one push-main leg, `pre-push self-test`, is set back to `subject = "repo"` in
  `tools/govkit/entries/push-main.kit.toml` AND in `tools/gate-legs.json` (so 7h's parity stays
  green) and `python tools/govkit/govkit.py selfcheck` runs, it prints a 7j4 refusal naming entry
  `push-main`, the leg, chunk `selftests` and both fixes. Restore both files, re-run, and no 7j4 line
  appears.
  Red when: the staged break produces no 7j4 line, or the restored tree still prints one.
  cost: one selfcheck run per state, each under the leg's 310 s ceiling on a contended host.
  fixture: needs `TOOL-aBenchedProbe-1` landed on the branch; the subject pin ratchet also reds on
  the break, and only the 7j4 line is this criterion's.
- **AC2** — When the `chunk` key is deleted from the `marker contracts` row of `tools/gate-legs.json`
  and `python tools/govkit/govkit.py selfcheck` runs, it prints a 7j4 refusal naming that leg and the
  argv element that runs the marker-contract suite file. Restore, re-run, no 7j4 line. This observes the
  filename clause, which no chunk-bearing row can reach.
  Red when: the chunkless row is not refused, or the refusal names the chunk instead of the argv
  element.
  fixture: the pin ratchet also reds on the break; only the 7j4 line is this criterion's.
- **AC3** — When `python tools/govkit/govkit.py selfcheck` runs on the clean tree after
  `TOOL-aBenchedProbe-1`, it prints no 7j4 refusal, and the 7j4 note line names
  `kit/dogfood doc parity`, `marker contracts` and `review-protocol parity (kit vs dogfood)` as
  exempt with nonzero graded and shaped counts.
  Red when: any 7j4 refusal prints, an exempt leg is missing from the note, or a count reads zero.
  figure: DERIVED at observation; 59 graded, 22 shaped and 3 exempt were measured at BASE and are
  not pinned.

## 7. Gates

`govkit selfcheck` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms`

New arm: tools/govkit/govkit.py selfcheck 7j4 · covers AC1 AC2 AC3 · a push-main leg set back to repo, and a chunkless filename-shaped row · none

The guarded legs above are the ones whose guard `{prefix}/govkit/` the estimate's path trips. The
`{prefix}/` guard is broad and excluded by the checker. The close runs them; no pass does.

## 8. Open questions

- **F1 — Which chunks exempt a filename-shaped leg: any chunk other than `selftests`, or only
  `declarations`?**
  Any other chunk is the brief's design: the chunk is gov's classification, and the pin file makes a
  move visible. Only `declarations` would red a future `*.test.sh` filed under `product`, `wiring`,
  `records` or `e2e`. The discriminating probe: today both choices exempt exactly the same three legs,
  all in `declarations`, so neither fails a criterion. Only `declarations` adds a rule no record
  states, that a test file run on the bar may sit in one chunk alone, and its fix would be to move a
  legitimate check into `declarations`, which is the same diff-visible move the wider rule already
  exposes. Recommendation: any chunk other than `selftests`.
  RESOLVED (agent, 2026-10-09, delegated): any chunk other than `selftests` exempts. The narrower
  option buys no observable case today and its only remedy is the move the pin file already shows.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

The seam is arm `7j3` in `selfcheck` in `tools/govkit/govkit.py`, which already walks every
descriptor's `[[gate_leg]]` through `canonical_ctx` and `resolve_tokens`, and the `manifest_chunk`
map arm `7h` builds from `tools/gate-legs.json`. `tools/codebase-map/reuse_lookup.py` on "flag a
descriptor gate leg that runs a self-test while its subject is not kit" returned `read_descriptors`
and `check_target_reads_subject` in `tools/govkit/govkit.py` and no checker of this predicate; the
arms themselves are inline in `selfcheck` and invisible to the symbol tier, so the seam was confirmed
by reading source at lines 2667-2760 and 3211-3232. The recall probe returned `TOOL-aScouredKit-27`
(chunk does not travel), `TOOL-aQuenchedHarness-3` (the three `declarations` legs adopters should
run, and the rejected filename HOLD predicate) and the `TOOL-dUnstalledConvoy-26` closing review
(subject parity in 7h). The enumeration in §4 was re-run for this spec, not copied from the brief,
and agreed with it: 59 graded, 22 shaped, 3 red, 3 exempt. Candidates tested and rejected are in §4
Alternatives rejected and §8 F1.

Recall terms used: `python tools/memory-recall/query.py "should a deployer check refuse a descriptor gate leg that ships a self-test to adopters as a repo subject" --terms "selfcheck descriptor gate_leg subject kit repo selftests chunk held adopter emitter exempt_leg ondemand"`
