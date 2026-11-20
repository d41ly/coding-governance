# TOOL-dPlacedRequest-43 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-43

The unit was built from its spec at rev-11 on base `3fc16744c`. Built: S9 (the stops guide's
`leases.offline` row names `--entry-claim`), S14 and S33 (`--no-filters` on the `.typed` append in
`tools/unattended/unattended.sh#write_request_record` and on the read in
`tools/unattended/unattended.sh#check_request_consent`), S16 and S17 (`CARD_PUBLISH_BOUND` beside
`CARD_FETCH_BOUND` in `skills/session-kickoff/manifest-check.sh`, read by the card write alone, and a
killed write printing `remote-ref unknown`), S18 (`tools/hooks/scratch-guard.js#readCard`'s two spawns
pass the kill signal and a closed stdin), S19 (`skills/session-kickoff/manifest-check.sh#run_driver_bounded`,
called by `derive_overlaps_line`, `derive_claims_line`, `read_card_ref` and `write_build_card`), S20
(`skills/session-kickoff/manifest-check.sh#derive_node_tag` and
`tools/run-gates/run-selftests.sh#resolve_node_tag` case-fold and compare the user equal), S23
(`tools/loop/placement.py#write_typed_request` hashes `--no-filters`), S28
(`tools/push-main.sh#read_fence_line` returns an unanswered read apart and
`tools/push-main.sh#derive_push_failure` maps it to `unreachable`) and S30 (`requests.lock` around
the fold compare, the copy and the `.typed` append). The guides and help pages name each outcome.
No gate, suite or bar ran in this pass: every reading below is a probe of the unit's own code or its
CLI over a scratch fixture, the fixture repositories under the node's short temp path.

**Evidences:** TOOL-dPlacedRequest-43
- AC1, AC2, AC3, AC4, AC7, AC14, AC15, AC30, AC32 and AC33 — the new region-eight block of
  `tools/unattended/unattended.test.sh`, run alone over the suite's own prelude and fixture helpers,
  never the suite: every assertion passed and none failed, its executions (DERIVED)
  25, of which 24 are `same` and `hit` lines and one the `mutate` of `build_claim_held`. (DERIVED)
- AC14, AC33 and AC30 RED — the same block over the base driver `3fc16744c`: the `.typed` blob is the
  filtered hash, the CRLF rewrite still consents `|0`, and `--request` records under a held lock,
  four rows failing (DERIVED). AC1 to AC4, AC7, AC15 and AC32 are observations of built code and read the same
  on the base, as the spec's narrowing to observations says.
- AC9 — `grep 'leases.offline' memory/guides/UNATTENDED-STOPS.md | grep -c 'entry-claim'` printed
  `1`, and the guide is byte-identical to `tools/unattended/STOPS.template.md`. (DERIVED)
- AC11 — the naming line sits in this unit's spec, `## 4. Design`, "The closing mechanism (S11)", and
  the pass's diff touches no spec but this unit's status cell.
- AC16 — `awk` read `CARD_PUBLISH_BOUND` 140 and `REMOTE_BOUND` 60, the first over twice the (DERIVED)
  second plus 5; `CARD_FETCH_BOUND` reads 20 at the base and at the pass. (DERIVED)
- AC17 — `card-store.fixture.sh --plant publish-late` printed three `held` rows: the append names the
  store `remote-ref unknown: no answer within 2s`, never `not written`, and the bare remote holds the (PINNED)
  ref. RED: with the base engine under `CARD_FETCH_BOUND=2` the first two rows print `MISSED`. (PINNED) The
  `publish`, `publish-unwritten`, `publish-hung` and `lookup-hung` plants each still print `held`.
- AC18 — a `node -e` probe of `readCard` with a stub checker that never answers, and one that
  backgrounds a sleeping child and exits, each returned no card, named, in about 10040 ms against (DERIVED)
  the bound of 10000 ms read from `CARD_PATH_BOUND_MS` plus 1 s; the body count printed `2`, (DERIVED)
  and `0` on the base hook, its red. On Windows node's own timeout already bounds both stubs on the
  base hook too, so the count is the red there; the new arm's three rows passed when run alone.
- AC19 — `grep -cE 'timeout -k 2 .* bash '` printed `1` on the engine, the line inside
  `run_driver_bounded`, and `4` on the base engine. (DERIVED) A scratch repository with no `.unattended.conf`
  still writes `overlaps — skipped: no .unattended.conf in this tree` and the `claims —` twin.
- AC20 — with `USERNAME` set to each `fleet.toml` row's user, in its own case and upper case,
  `derive_node_tag`, `resolve_node_tag` and `resolve_fleet_tag` each printed that row's tag, `a` to
  `d`; `daily-agent2` reads UNKNOWN and no tag. RED on the base: `DAILY-AGENT` reads UNKNOWN in
  `derive_node_tag` while `daily-agent2` reads `a` in `resolve_node_tag`.
- AC23 — `python tools/loop/placement.py --fixture --plant relayed` printed `relayed exit 1 · typed
  exit 0 · held` and exited 0; the `--no-filters` grep prints `1`. (DERIVED)
- AC24 — `TOOL-dPlacedRequest-44`'s oracle text, run on the branch tip, took the merge-base form and
  printed its `version oracle:` line naming 232 commits and no `KIT_` line after it; its (DERIVED)
  prepared-merge form is the landing's.
- AC28 — the new arm 54 of `tools/push-main.test.sh`, run alone over its fixture helpers: `ok`, the
  landing exits 1 printing `push-main: unreachable —`. RED: the same arm over the base lander prints
  `push-main: fenced —` and names `claim-lost`.

## Items diverged

- S1, AC1 — under a renamed-away origin the take-over `--resume` refuses at check 27, its anchor
  read in `tools/unattended/unattended.sh#run_takeover`, before the strict claim read, while `--close`
  reaches check 109. The arm fails the claims fetch alone with a git shim, as the suite's AC19 does,
  and both verbs then refuse at check 109, nothing queued.
- S28 — `tools/push-main.test.sh` carries no assertion-count pin, so the arm raises no count.

## Owed at the close

- `New arm:` `tools/unattended/unattended.test.sh`, the region-eight TOOL-dPlacedRequest-43 block,
  `FLOOR_ASSERTIONS` raised to 3995 and `FLOOR_SHARD_8` to 1214; its RED-first observation (DERIVED)
  is the close's. Waived for this build's landing by README rule 8.
- `New arm:` `tools/push-main.test.sh` arm 54; `tools/hooks/scratch-guard.test.sh`'s three AC18 rows,
  `FLOOR_ASSERTIONS` raised to 396; `skills/session-kickoff/card-store.fixture.sh`'s (DERIVED)
  `publish-late` plant. Each RED-first observation is the close's.
- AC22 — `python tools/check-spec-tokens.py` after `gen_build_index.py --write`, a gate this role may
  not run: its `size join` line and any row naming a spec of this build go to the close. This spec
  measured 48028 bytes by `wc -c` at the pass, under the cap of 49152 the spec pins. (DERIVED)
- The legs the spec's Gates section names, run once by the main loop.
