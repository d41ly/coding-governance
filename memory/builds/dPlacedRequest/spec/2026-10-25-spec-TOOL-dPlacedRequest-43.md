# TOOL-dPlacedRequest-43 — the round-1 promotions' minors: behavioural class checks, honest outcomes, every reader of a changed spelling, and the sizes kept

**Status:** OPEN · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 24 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 |
| [2026-10-25-build-TOOL-dPlacedRequest-43-deviation-431.md](../build/2026-10-25-build-TOOL-dPlacedRequest-43-deviation-431.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-35 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
exited CONVERGED with 42 confirmed findings. Its eight highs are units 35 to 42. This unit is the
batch BUILD-METHOD M4 makes of the rest: 24 MEDIUM and 10 LOW findings, one scope item per raw id,
each naming its finding and, in brackets, the review item holding it (M1 to M22, L1 to L9). Three
items hold a MEDIUM and a LOW finding of one defect (M7 and L8, M8 and L7, M9 and L9); each finding
still gets its own item and its own observation. The minors land on ten units, so this unit
repairs none in particular and sits above every unit of the build, at order 24, after unit 35 at 23.
Criterion ACn observes item Sn.

## 2. Scope (IN)

- **S1** — finding 3 (M1). A strict claim read never queues, observed by behaviour: over
  `TOOL-dPlacedRequest-23` AC1's fixture under planted `warn`, `--resume tOff` (`run_takeover`,
  `tools/unattended/unattended.sh:9037`) and `--close tOff` (`verb_close`, `:10839`) exit non-zero
  printing `check 109`, `gov-queue.log` unchanged. Observed by AC1.
- **S2** — finding 37 (M1). The same, seen from the queue: a sourced driver with a logging
  `add_gov_queue` stub runs `print_claims`, the `--preflight` claim, `run_takeover` and `verb_close`
  after a failed strict read, and the stub logs no call. Observed by AC2.
- **S3** — finding 4 (M2). `TOOL-dPlacedRequest-28` S4's class observed by behaviour: over a feed
  naming `refs/gov/leases/tFix/build` after the remote ref is gone, the online creates
  (`--lease acquire`, `take-over`, the `--preflight` run claim, `--lease offer`) each yield a commit
  with a parent. Observed by AC3.
- **S4** — finding 19 (M2). The same four paths with `read_feed_lease_tip` stubbed to print
  `tombstone` each exit 1 printing `tombstone`, nothing written. Observed by AC4.
- **S5** — finding 5 (M3). `TOOL-dPlacedRequest-33` AC5's stub logs only `fetch`, `ls-remote` and
  `push`, since the driver's startup `rev-parse` (`unattended.sh:546`) runs before any verb. Observed
  by AC5.
- **S6** — finding 6 (M4). `leases.offline: follow-leases` has one `--entry-claim` outcome,
  `awaiting` with exit 4, as `TOOL-dPlacedRequest-34` S14 routes it: `item.entry.claim`'s `refused`
  outcome in the loop kit's `loop.toml` and its help page lists `offline` under `refuse` alone.
  Observed by AC6.
- **S7** — finding 7 (M5). The queue line's empty-tip encoding is observed red on a line an `IFS`
  read would shift: `IFS=$'\t' read -r ref tip commit utc` over an offline create's line reads a
  40-hex `commit`. Observed by AC7.
- **S8** — finding 25 (M13). The cached-tip field is written and read through one function,
  `derive_queue_tip`, mapping empty to `-` and back. **Readers:** by name: READER NOT IN TREE, since
  the field's two readers, `add_gov_queue`'s base and `write_gov_queue`'s compare-and-swap and
  resolved-line rewrite, are minted in this build by TOOL-dPlacedRequest-1 and TOOL-dPlacedRequest-24.
  by value: NO VALUE READERS, since both reach the value only through `derive_queue_tip`.
  Observed by AC8.
- **S9** — finding 8 (M6). The stops guide's `leases.offline` row names its population as every
  non-strict reader, `--entry-claim` included (`TOOL-dPlacedRequest-21` S2 and S5). Observed by AC9.
- **S10** — finding 9 (L1). `TOOL-dPlacedRequest-31`'s binding is observed red on the base predicate: a
  planted session-only line `s2` beside a stored copy `s2` never submitted reads no consent. Observed
  by AC10.
- **S11** — finding 10 (L2). `TOOL-dPlacedRequest-34` S10, S13, AC10 and AC13 restate
  `TOOL-dPlacedRequest-33` S2, S3 and AC4; that spec gains, as a rev bump with its §9 line, one line
  naming unit 33 the closing mechanism of round-1 findings 33 and 34 in their place. Observed by AC11.
- **S12** — finding 11 (L3). `tools/unattended/VERBS.template.md:279`, the `'refs/gov/runs/*'` reader
  `TOOL-dPlacedRequest-34` S35 lists, names the lease namespace, and the check reads the bare
  `refs/gov/runs` so no spelling escapes it. Observed by AC12.
- **S13** — finding 12 (L4). Every line of `gov-feed.sh` spelling `gov-feed.lock` is a
  `write_node_lock` or `remove_node_lock` call or a comment, and no `mkdir` or `rmdir` of it is left.
  Observed by AC13.
- **S14** — finding 15 (M7). The `.typed` append and `check_request_consent` hash with
  `git hash-object --no-filters`, so the blob is of the submitted bytes on every node's config and
  agrees with `TOOL-dPlacedRequest-30`'s `cmp -s`. Observed by AC14.
- **S15** — finding 16 (M8). The identity rule as the code reads it: `mine` is both sessions present,
  equal and tags equal, or either session none and both keepalives present and equal; the
  prior-session and take-over rows (`unattended.sh:2261-2263`) are unchanged. Observed by AC15.
- **S16** — finding 17 (M9). `CARD_FETCH_BOUND=${CARD_FETCH_BOUND:-140}` sits beside
  `CARD_CLAIMS_BOUND` (`skills/session-kickoff/manifest-check.sh:228`), above the write verb's worst
  case of two `REMOTE_BOUND` calls plus the feed lock's 5 s retry. Observed by AC16.
- **S17** — finding 43 (L9). A killed publish prints `card — remote-ref unknown: no answer within
  <n>s`, never `not written`, and a write that landed before the kill reaches the feed at the next
  sighting (`TOOL-dPlacedRequest-13` S4). Observed by AC17.
- **S18** — finding 18 (M10). `readCard`'s bash call is `spawnSync(bash, args, { timeout: 5000,
  killSignal: 'SIGKILL' })`, and a checker that does not answer reads as no card, named. Observed by
  AC18.
- **S19** — finding 22 (M11). One helper, `run_driver_bounded <cell> <bound> <verb args>`, in
  `manifest-check.sh` holds the conf check, the kit resolve, the `timeout -k` probe, the scratch
  capture and the kill reading; `derive_overlaps_line` (`:555`), `derive_claims_line` (`:645`), the
  card publish and the card lookup call it. Observed by AC19.
- **S20** — finding 23 (M12). `TOOL-dPlacedRequest-34` S30's reason is corrected in the code's comment:
  `derive_node_tag` and `resolve_node_tag` read the governance file's `## Node registry` table, which
  `derive_node_table` (`tools/playbook/render_playbook.py:424`) renders from `fleet.toml`, so one
  registry; they stay because both kits read the rendered table, not the playbook kit. A resolver
  disagreeing with case-folded user equality on a `fleet.toml` row is brought to it. Observed by AC20.
- **S21** — finding 27 (M14). The protocol stays at or under 66860 bytes after
  `TOOL-dPlacedRequest-34` S35's 8 added bytes: the `RUN_CLAIMS` row
  (`tools/unattended/PROTOCOL.template.md:521`) names no ref and points at `UNATTENDED-STOPS.md` §7,
  which already states it. Observed by AC21.
- **S22** — finding 28 (M15). `TOOL-dPlacedRequest-34`'s spec is cut to at most 47104 bytes, 2 KiB
  under the 49152 ceiling, after its records render: its §4 "Measured sizes" and "The one deletion
  outside leases" go to a research record under `build/`, cited in one line, with S11's collapse.
  Observed by AC22.
- **S23** — finding 29 (M16). The `.typed` line's readers follow `TOOL-dPlacedRequest-31`'s grammar:
  `TOOL-dPlacedRequest-5`'s `relayed` plant writes `<session>` TAB the `--no-filters` blob of the
  stored copy, and `TOOL-dPlacedRequest-19` §4's file table reads one such line per session and words.
  **Readers:** by name: READER NOT IN TREE, since the one-field line's readers, unit 5's plant and
  unit 19's table, are built in this build and amended here. by value: NO VALUE READERS, since only
  `check_request_consent` compares a line, and S14 states its read. Observed by AC23.
- **S24** — finding 30 (M17). The version-bump oracle reads the build's own commits:
  `git log --first-parent --no-merges --invert-grep --grep='^mint:' -p c63aabbb..HEAD` over
  `unattended.sh` and `run-gates.sh`, never `git diff` from the fixed sha. Observed by AC24.
- **S25** — finding 31 (L6). `tools/unattended/README.md`'s health-event sentence names
  `node-lock-broken` and `node-lock-guard-cleared`, written by the feed's and the queue's locks.
  Observed by AC25.
- **S26** — finding 21 (L6). The README's event list is complete for the block: every event name
  the `gov_feed_sh` cut passes to `add_health_event` is spelled in it. Observed by AC26.
- **S27** — finding 34 (M18). A confirming `ls-remote` after a lost flush push that fails or times out
  keeps the line (rc 2) and prints one `queue: NOTE -` line; only an answered read decides landed or
  yield. Observed by AC27.
- **S28** — finding 35 (M19). The lander's re-fence keeps `TOOL-dPlacedRequest-15` S2's `lease refused
  — offline` for an unanswered `--after` read, and maps it to `unreachable` (exit 1, no abort remedy);
  `epoch-fence`, and so `fenced`, is kept for a read that answered. Observed by AC28.
- **S29** — finding 38 (M20). The tenure walk tests the tip: a one-commit tenure is its own renewing
  beat or its own oldest commit. Observed by AC29.
- **S30** — finding 39 (M21). `--request` takes `write_node_lock` on `requests.lock` in the common dir
  around the compare, the copy and the `.typed` append, so a racing second call re-runs the compare
  and is refused `collision`. Observed by AC30.
- **S31** — finding 40 (L7). In the `lease` mode, two present, differing sessions with equal
  keepalives and no prior-session fact are not `mine`. Observed by AC31.
- **S32** — finding 41 (M22). On `--lease`, the `RUN_CLAIMS`-off answer is tested before the
  identity refusal, so an id-less call on a dark adopter prints `lease — off` and exits 0. Observed by
  AC32.
- **S33** — finding 42 (L8). Consent does not survive an end-of-line rewrite of the stored copy.
  Observed by AC33.
- **S34** — finding 20 (L5). The claim-push family is gone whole from the map, `check_claim_push_clear`
  (`tools/push-main.sh:304`) included. Observed by AC34.

## 3. Non-goals (OUT)

- No second mechanism for a high: units 35 to 42 own those; S29 observes the tip case unit 35's walk
  also reads, at its own order.
- No change to a criterion of an earlier unit's spec, except S11's and S22's edits to
  `TOOL-dPlacedRequest-34`: each item here carries its own observation.
- No new gate leg: each arm joins an existing suite.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-1` — the offline branch, the queue and `resolve_fleet_tag`, which S7, S8 and S20 observe and amend
- **consumes-from** `TOOL-dPlacedRequest-3` — `item.entry.claim`'s outcome rows, which S6 amends
- **consumes-from** `TOOL-dPlacedRequest-5` — the `relayed` plant, which S23 writes in the two-field grammar
- **consumes-from** `TOOL-dPlacedRequest-19` — the `.typed` file and `--request`, whose table row S23 amends
- **consumes-from** `TOOL-dPlacedRequest-21` — `--entry-claim`'s use of `leases.offline`, which S9 names in the guide
- **consumes-from** `TOOL-dPlacedRequest-23` — the strict callers' split, which S1 and S2 observe
- **consumes-from** `TOOL-dPlacedRequest-24` — the queue's flush and the node lock, which S13 and S27 amend and S30 reuses
- **consumes-from** `TOOL-dPlacedRequest-26` — the tenure walk, whose tip case S29 observes
- **consumes-from** `TOOL-dPlacedRequest-28` — `read_feed_lease_tip` and its class, which S3 and S4 observe
- **consumes-from** `TOOL-dPlacedRequest-29` — the re-fence act and its classifier, which S28 amends
- **consumes-from** `TOOL-dPlacedRequest-30` — `--request`'s collision compare, which S30 locks
- **consumes-from** `TOOL-dPlacedRequest-31` — the `.typed` line and consent read, which S10, S14 and S33 amend
- **consumes-from** `TOOL-dPlacedRequest-32` — the identity rule and the id-less refusal, which S15, S31 and S32 amend
- **consumes-from** `TOOL-dPlacedRequest-33` — `--card-ref write` and its engine call, which S5, S16, S17 and S19 amend
- **consumes-from** `TOOL-dPlacedRequest-34` — its spec, S14, S30, S35, S38, S40, the lookup and `readCard`, which S6, S11, S12, S18 to S22, S24 and S34 amend
- **hands-off** `TOOL-dPlacedRequest-44` — S24 and AC24, which that unit re-ranges to the build's side of the prepared merge and rewrites in place
- **hands-off** `TOOL-dPlacedRequest-48` — S30's `requests.lock` and AC30, which that unit observes by a placed race and rewrites in place
- **hands-off** `TOOL-dPlacedRequest-49` — S6, S8, S15 to S22, S25, S26, S30 and their criteria, which that unit's items for the round-3 audit's minors re-point, re-bound and re-observe
- **hands-off** `TOOL-dPlacedRequest-52` — S19 and its sketch, S22, AC22 and S30, which that unit's items for findings 5, 7 and 20 pin and rewrite; this unit's own pass reads AC22 at 48128, the figure that unit sets

## 4. Design

### Evidence

- Strict callers: `print_claims` (`unattended.sh:2202`), `--preflight` (`:7477`), `run_takeover`
  (`:9037`, reached by `--resume` at `:9309`) and `verb_close` (`:10839`).
- The bounded driver call twice: `manifest-check.sh:560` and `:651` (`timeout -k 1 5 true`), `:564` and
  `:655` (`GOV_RUNLOG=0 timeout -k 2`). `CARD_OVERLAP_BOUND` and `CARD_CLAIMS_BOUND` are declared with
  `${…:-n}` defaults at `:220` and `:228`.
- `scratch-guard.js`'s one `spawnSync` (`:710`) passes no `timeout`; `readCard` is at `:667`.
- The rendered protocol measured 66859 bytes with CR stripped against its 66860 limit
  (`tools/template-size-limits.txt:143`), PINNED 2026-10-25; the spec ceiling is 49152
  (`:167`), and `TOOL-dPlacedRequest-34` measured 50111 bytes the same day, PINNED.
- `tools/unattended/README.md:246-252` lists the claim-push events `TOOL-dPlacedRequest-11` S7 drops.
- Today's identity rows: `unattended.sh:2260-2263`.

### The re-fence outcomes (S28)

| `--after` read | Line | Lander class | Exit |
|---|---|---|---|
| answered, same holder, on chain, same epoch | `fence — …` | `refenced` | retry |
| answered, otherwise | `lease refused — epoch-fence` | `fenced` | 1, `--abort … claim-lost` |
| no answer | `lease refused — offline` | `unreachable` | 1, no abort remedy |

### The bounded call (S19)

```
run_driver_bounded <cell> <bound> <verb args>     -> rc of the verb, output in "$RDB_OUT"
  no .unattended.conf | no driver | no timeout -k  -> print "<cell> — skipped: <why>", rc 125
  GOV_RUNLOG=0 timeout -k 2 <bound> bash <driver> <verb args> </dev/null >"$RDB_OUT"
  rc 124 or 137                                    -> the caller prints its kill line
```

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, S2, S7, S8, S14, S15, S27, S29 to S32
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/STOPS.template.md` and `memory/guides/UNATTENDED-STOPS.md`: S9
- `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`: S12
- `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`: S21
- `tools/unattended/README.md`: S25, S26
- `skills/session-kickoff/manifest-check.sh`: S16, S17, S19, S20
- `tools/hooks/scratch-guard.js` and `tools/hooks/scratch-guard.test.sh`: S18
- `tools/push-main.sh` and `tools/push-main.test.sh`: S28
- `tools/run-gates/run-selftests.sh`: S20
- the loop kit's `loop.toml`, its `placement.py` fixture and help page: S6, S23
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-34.md`: S11, S22, and its
  research record under `memory/builds/dPlacedRequest/build/`

### Alternatives rejected

- **Two batches.** Every item but S18 and S21 writes `unattended.sh`, `manifest-check.sh` or a file
  the kit epoch regenerates `tools/govkit/subject-pins.tsv` over, so no split gives M6 two disjoint
  write sets.
- **S20 by re-pointing both shell resolvers at `read_fleet`.** Neither kit carries the playbook kit,
  and the rendered table is the copy each adopter holds.

## 5. Production-readiness checklist

- security — S14 and S33 bind consent to bytes; S30 closes a racing overwrite of the stored words.
- perf / scale — S18 bounds a hook call at 5 s; S19 is one helper for four calls.
- error / empty / loading states — S17, S27 and S28 each name an outcome for no answer.
- observability — S25 and S26 document every lock event.
- risks — S16 lets a hung remote hold the READY append up to 140 s, the cost of never killing a writer
  mid-write.
- testing — the probes of §6 and the arms of §7.
- migration — none: every surface is new in this build.
- user docs — the stops, verbs and protocol guides and the kit README; no `help/` page covers the
  driver.

## 6. Acceptance criteria

The fixtures are the named units': unit 1's AC7 clone and bare origin for the driver, unit 2's card
store fixture for the engine, unit 19's two clones for requests, each `RUN_CLAIMS=on` unless stated.

- **AC1** — When `--resume tOff` and `--close tOff` run over a renamed-away origin under planted
  `warn`, each exits non-zero printing `check 109` and `gov-queue.log` is unchanged. Red when: a
  scratch copy's lease writer queues whenever its read failed.
- **AC2** — When a probe sources the driver with an `add_gov_queue` stub appending to `q.log` and runs
  the four strict callers over the failed read, `q.log` is empty. Red when: a strict caller reaches
  the queue through the writer.
- **AC3** — When the four online creates run over a feed naming a deleted lease, each new commit shows
  a parent under `git rev-list --parents -n1`. Red when: a create builds a parentless commit.
- **AC4** — When `read_feed_lease_tip` is stubbed to print `tombstone`, the four paths each exit 1
  printing `tombstone` and the remote is unchanged. Red when: a path skips the reader.
- **AC5** — When `--card-ref write tFix --message m.txt` runs with `RUN_CLAIMS` off and a stub `git`
  logging `fetch`, `ls-remote` and `push` only, it prints `card-ref — off` and the log is empty.
  Red when: the off switch reaches the remote.
- **AC6** — When `--entry-claim` runs offline under planted `follow-leases`, it exits 4 printing
  `claim not written — offline`, and `grep -n 'follow-leases'` over `loop.toml` names no `refused`
  line. Red when: one value has two outcomes.
- **AC7** — When an offline create of `tOff` is queued and `IFS=$'\t' read -r ref tip commit utc`
  reads its line, `commit` matches `^[0-9a-f]{40}$`. Red when: an empty field shifts the line.
- **AC8** — When the offline create runs twice, `grep -c '' gov-queue.log` prints 1, and the flush
  creates the ref. Red when: one side compares the raw empty field with `-`.
- **AC9** — When `grep -n 'entry-claim' tools/unattended/STOPS.template.md` runs, the `leases.offline`
  row names it. Red when: the guide's population omits a reader.
- **AC10** — When a session-only line `s2` sits beside a stored copy `s2` never submitted,
  `check_request_consent` in `s2` returns 1. Red when: the base whole-line predicate grants it.
- **AC11** — When `grep -c '^- \*\*AC1[03]\*\*' 2026-10-25-spec-TOOL-dPlacedRequest-34.md` runs, it
  prints 0, and a line there names `TOOL-dPlacedRequest-33` S2. Red when: the duplicates stand.
- **AC12** — When `git grep -n 'refs/gov/runs' -- tools/unattended/VERBS.template.md` runs, no line
  names the runs namespace as a claim's home. Red when: line 279's sentence survives.
- **AC13** — When `grep -n 'gov-feed.lock' gov-feed.sh | grep -v 'write_node_lock\|remove_node_lock\|#'`
  runs, it prints nothing, nor does a grep for `mkdir`/`rmdir` of it. Red when: the feed keeps a lock
  of its own.
- **AC14** — When a CRLF `a.md` is requested under `core.autocrlf=true`, its `.typed` blob equals
  `git hash-object --no-filters a.md`. Red when: the filtered blob is written.
- **AC15** — When two present, differing sessions with equal keepalives meet in `take-over` mode, the
  class is `same`. Red when: the keepalive alone makes `mine`.
- **AC16** — When `awk` reads `CARD_FETCH_BOUND`'s default from `manifest-check.sh` and
  `REMOTE_BOUND` from `unattended.sh`, the first exceeds twice the second plus 5. Red when: the
  writer runs under a reader's bound.
- **AC17** — When `--plant publish-late` runs a stub driver that writes the ref and sleeps past
  `CARD_FETCH_BOUND=2`, the card prints `remote-ref unknown`. Red when: a landed write reads `not
  written`.
- **AC18** — When a `node -e` probe calls `readCard` with a stub checker sleeping 30 s, it returns
  no card, named, within 6 s. Red when: the hook waits on a hung checker.
- **AC19** — When `grep -c 'timeout -k 1 5 true' skills/session-kickoff/manifest-check.sh` runs, it
  prints 1. Red when: a call site copies the bounded call.
- **AC20** — When a probe sets `USERNAME` to each `fleet.toml` row's user, `derive_node_tag`,
  `resolve_node_tag` and `resolve_fleet_tag` print that row's tag. Red when: two resolvers disagree.
- **AC21** — When `tr -d '\r' < memory/guides/UNATTENDED-PROTOCOL.md | wc -c` runs, it prints at most
  66860. Red when: the size leg's limit is crossed.
- **AC22** — When `gen_build_index.py --write` has rendered and `wc -c` reads unit 34's spec, it
  prints at most 47104. Red when: the records region pushes it over.
- **AC23** — When `python placement.py --fixture --plant relayed` runs, it passes with a two-field
  line and refuses `relayed` with a bare session line. Red when: the plant keeps the old grammar.
- **AC24** — When S24's `git log` is grepped for `^[+-]KIT_(UNATTENDED|RUN_GATES)_VERSION=` on the
  prepared merge, it prints nothing. Red when: a mint from main reads as a hand-bump.
- **AC25** — When `grep -c 'node-lock-broken\|node-lock-guard-cleared' tools/unattended/README.md`
  runs, it prints at least 1 for each. Red when: an emitted event is undocumented.
- **AC26** — When a probe lists each event the `gov_feed_sh` cut passes to `add_health_event` and greps
  `tools/unattended/README.md` for it, none is missing. Red when: a new event lands undocumented.
- **AC27** — When a stub `observe_remote` fails on the confirming read, the line stays and the health
  log gains no `lease-yielded` line. Red when: no answer reads as a yield.
- **AC28** — When a stub kills the `--after` read, `push-main.sh` prints `unreachable`, not
  `fenced`. Red when: a hiccup tells a holder to abort.
- **AC29** — When a one-commit tenure whose tip is `renews: yes` was sighted a minute ago, `--claims`
  prints `live`. Red when: the tip is skipped.
- **AC30** — When two background `--request` calls of differing date-only files run on one key,
  exactly one exits 2 printing `collision`. Red when: both copy.
- **AC31** — When a `lease`-mode record holds session `s1` and keepalive `k1` and a probe in `s2` with
  keepalive `k1` derives its class, it is a `foreign-` class. Red when: §4's pseudo-code is built.
- **AC32** — When `env -u CLAUDE_CODE_SESSION_ID` runs `--lease acquire build tFix` with `RUN_CLAIMS`
  off, it prints `lease — off` and exits 0. Red when: the identity test runs first.
- **AC33** — When a CRLF copy of `a.md` replaces the stored copy after `s1`'s request,
  `check_request_consent` in `s1` returns 1. Red when: the filtered blob matches.
- **AC34** — When `grep -c 'claim_push_lock\|check_claim_push_clear' memory/map/generated/symbols.json`
  runs after `gen_map.py --write`, it prints 0. Red when: a fourth function survives.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms` · `manifest-check self-test` · `scratch-guard self-test` · `agent-cap self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `format-guard self-test` · `push-main self-test` · `run-selftests self-test` · `unattended protocol size` · `codebase-map coverage + freshness`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC7 AC8 AC10 AC14 AC15 AC27 AC29 AC30 AC31 AC32 AC33 · each item's plant, staged against the unit it amends · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/push-main.test.sh · covers AC28 · a killed `--after` read, staged against the epoch-fence mapping · the suite's assertion count raised by the arm added
New arm: tools/hooks/scratch-guard.test.sh · covers AC18 · a stub checker that never answers, staged against the unbounded spawn · none

## 8. Open questions

- **F1 — Is the empty tip spelled once (S8)?** (a) One `derive_queue_tip` both readers call; (b) each
  reader normalises. (b) is the one-sided compare finding 25 names. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the review's fix judged sound. widens: none · relaxes: none
- **F2 — How do the node-tag resolvers stop disagreeing (S20)?** (a) Corrected reason and a parity
  probe over `fleet.toml`; (b) both re-pointed at `read_fleet`. (b) needs the playbook kit inside two
  copy-installed kits. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's second fix.
  widens: none · relaxes: none
- **F3 — What bounds the card publish (S16)?** (a) A 140 s default above the verb's worst case; (b)
  the bound passed into the driver. (b) adds a flag to a verb for one caller. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the review's first fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, the batch of the spec audit of the round-1 promotions' 24 MEDIUM
  and 10 LOW findings.
- rev-2 · 2026-10-25 · §7 leg line adds `agent-cap self-test`, `verifier fan-out self-test`,
  `review-join self-test` and `hook destinations self-test`, the legs whose `hooks/` guard
  `tools/hooks/scratch-guard.js` trips.
- rev-3 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-44 and TOOL-dPlacedRequest-48 and TOOL-dPlacedRequest-49.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

Each item extends the unit its finding names; the new code reuses three seams: `TOOL-dPlacedRequest-24`'s
`write_node_lock` for S30, the existing `CARD_*_BOUND` default pattern (`manifest-check.sh:220-229`)
for S16, and `derive_overlaps_line` (`:555`), the bounded call's other instance, which S19 extracts
with its sibling. `python tools/codebase-map/reuse_lookup.py "bounded driver call from the kickoff
engine with a timeout"` ranked `engine`, `boundedParallel`, `read_bound_key` and `init_bounded`, name
stems only, none the engine's call. `python tools/memory-recall/query.py "how are a review's minor
findings batched into one unit"` returned TOOL-dRenderedAnchor-7 and -3 and TOOL-dSafePassage-43,
batches of the same kind; none disagrees with source.

Recall terms used: minors batch behavioural class check spelling readers outcome bound size ceiling protocol consent no-filters
