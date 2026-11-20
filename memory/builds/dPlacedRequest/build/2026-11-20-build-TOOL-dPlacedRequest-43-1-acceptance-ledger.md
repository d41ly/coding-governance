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

THE BLOCK PROBE, the reading the lines below cite as "the block": the new region-eight block of
`tools/unattended/unattended.test.sh`, run alone over the suite's own prelude and fixture helpers,
never the suite, printed no failing row; it executes 25 rows, 24 `same` and `hit` lines and (DERIVED)
the one `mutate` of `build_claim_held`. Over the base driver `3fc16744c` the AC14, AC33 and AC30 rows
fail, four in all; the other rows observe code landed units built and read the same there. (DERIVED)

**Evidences:** TOOL-dPlacedRequest-43
- AC1 — `check 109` — the block: a take-over `--resume` and `--close`, the claims fetch failed by a git shim and `warn` planted, each exit non-zero printing `check 109`, no queue file made; see Items diverged for the renamed-away origin.
- AC2 — `add_gov_queue` — the block: a logging `add_gov_queue` stub in process logs no call from `--claims`, `--preflight`, the take-over `--resume` or `--close`, and logs one from a staged `read_claims` that queues on its failure, the stub's liveness.
- AC3 — `git rev-list --parents -n1` — the block: `--lease acquire` and `--lease take-over` over a `released` lease the feed sighted and the origin no longer holds each write epoch 5 parented on the feed's commit.
- AC4 — `tombstone` — the block: `--lease take-over` over a sighted, deleted build tombstone exits 1 printing `lease refused — tombstone`, the origin holding no such ref.
- AC7 — `IFS=$'\t' read -r ref tip commit utc` — the block: an offline create's queue line splits with a 40-hex `commit` field.
- AC9 — `grep 'leases.offline' memory/guides/UNATTENDED-STOPS.md | grep -c 'entry-claim'` — printed `1`, the guide byte-identical to `tools/unattended/STOPS.template.md`. (DERIVED)
- AC11 — `TOOL-dPlacedRequest-33` — the naming line sits in this unit's spec, section 4's "The closing mechanism (S11)", and the pass's diff touches no spec but this unit's status cell.
- AC14 — `core.autocrlf=true` — the block: a CRLF request's `.typed` blob equals `git hash-object --no-filters`, apart from the filtered blob; RED on the base driver.
- AC15 — `CW_CLS` — the block: `check_claim_writable` in `take-over` mode over a record of session `s1` and keepalive `k1`, read from `s2` under `k1`, sets a `foreign-` class.
- AC16 — `CARD_PUBLISH_BOUND` — `awk` read it 140 and `REMOTE_BOUND` 60, over twice that plus 5, and `CARD_FETCH_BOUND` 20 at the base and at the pass. (DERIVED)
- AC17 — `card — remote-ref unknown` — `bash skills/session-kickoff/card-store.fixture.sh --plant publish-late` printed three `held` rows, the remote holding the ref; RED, the base engine under `CARD_FETCH_BOUND=2` prints two `MISSED` rows. (DERIVED)
- AC18 — `readCard` — a `node -e` probe with a never-answering stub and an orphaning stub returned no card, named, in about 10040 ms against `CARD_PATH_BOUND_MS` 10000 plus 1 s; the body's kill-signal count is `2`, and `0` on the base hook. (DERIVED)
- AC19 — `run_driver_bounded` — `grep -cE 'timeout -k 2 .* bash ' skills/session-kickoff/manifest-check.sh` printed `1`, the line inside `run_driver_bounded`, and `4` on the base engine. (DERIVED)
- AC20 — `derive_node_tag` — with `USERNAME` each `fleet.toml` row's user, as given and upper-cased, `derive_node_tag`, `resolve_node_tag` and `resolve_fleet_tag` each printed the row's tag; on the base `DAILY-AGENT` read UNKNOWN in the first and `daily-agent2` read `a` in the second.
- AC22 — `gen_build_index.py --write` — the pre-commit hook rendered the records regions at this pass, and this spec, the build's one live spec, measured 48028 bytes by `wc -c` under the 49152 cap the spec pins; the checker's own `size join` line is owed to the close, see below. (DERIVED)
- AC23 — `python tools/loop/placement.py --fixture --plant relayed` — printed `relayed exit 1 · typed exit 0 · held` and exited 0; the `--no-filters` grep prints `1`. (DERIVED)
- AC24 — `version oracle:` — `TOOL-dPlacedRequest-44`'s oracle text on the branch tip took the merge-base form and printed 232 commits and no `KIT_` line; its prepared-merge form is the landing's. (DERIVED)
- AC28 — `unreachable` — the new arm 54 of `tools/push-main.test.sh`, run alone over its fixture helpers, printed `ok`, the landing exiting 1 `push-main: unreachable —`; over the base lander it prints `fenced` and names `claim-lost`.
- AC30 — `requests.lock busy` — the block: a live `requests.lock` refuses `--request` with exit 2 within 6 s, the store and the origin unchanged, and the freed lock lets it record; RED on the base driver. (PINNED)
- AC32 — `lease — off` — the block: `env -u CLAUDE_CODE_SESSION_ID` `--lease acquire build tFix` with `RUN_CLAIMS` off exits 0 printing `lease — off · tFix/build`.
- AC33 — `check_request_consent` — the block: qA's LF request consents, and its stored copy rewritten to CRLF reads `relayed`, exit 1; RED on the base driver.

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
  `publish-late` plant, which `skills/session-kickoff/manifest-check.test.sh`'s plant list does not
  name, so the close runs it directly. Each RED-first observation is the close's.
- AC22's checker, `python tools/check-spec-tokens.py`, a gate this role may not run: its `size join`
  line and any row naming a spec of this build go to the close.
- The legs the spec's Gates section names, run once by the main loop.
