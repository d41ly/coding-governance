# TOOL-dPlacedRequest-33 — the card's remote ref is written by the driver, dark behind `RUN_CLAIMS`

**Status:** DEFERRED · rev-5 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 13 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-33-deviation-331.md](../build/2026-10-25-build-TOOL-dPlacedRequest-33-deviation-331.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-33-deviation-332.md](../build/2026-10-25-build-TOOL-dPlacedRequest-33-deviation-332.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 6 at HIGH**, its item **H2**. `TOOL-dPlacedRequest-2` pushes
`refs/gov/builds/<slug>/card` at every READY append, with the `remote-ref` store selected by default,
"Live at landing" and no `RUN_CLAIMS` switch. The kickoff engine is linked into every project's skills
directory (`WIRE-INTO-PROJECT.md:71-80`), so on their next kit update every adopter's sessions would
write governance refs to the shared remote without opting in, while units 1 (§8 F2) and 12 (§8 F3)
settle the same question the other way. The engine never reads the conf's switch itself: the driver
is its one reader (`skills/session-kickoff/manifest-check.sh:641-643`). This unit repairs
`TOOL-dPlacedRequest-2` by moving the remote-ref write into a driver verb that answers `off` while
`RUN_CLAIMS` is not `on`, called by the engine under a kill bound, so the switch, the remote, the bound
and the writer each live once.

## 2. Scope (IN)

- **S1** — The verb. `unattended.sh --card-ref write <slug> --message <file>`: with `RUN_CLAIMS` not
  `on` it prints `card-ref — off` and exits 0, reading and writing nothing. With it on, it resolves the
  clone's one remote as `resolve_claim_remote` does (check 24), reads `refs/gov/builds/<slug>/card`
  once with `observe_remote` into `refs/gov/remote/builds/<slug>/card`, builds the commit with
  `build_gov_commit <tip read> <message>` and writes it with `write_gov_ref <ref> <tip read>
  <commit>`, so the write joins the change feed as every `write_gov_ref` call does. It prints
  `card-ref — <tail> · <sha8>` and exits 0, or `card-ref lost — <sha8 of the remote tip>` and exits 1
  on a lost compare-and-swap, or `card-ref not written — <why>` and exits 2. `<slug>` is held to the
  build-folder grammar `check_slug` applies. Observed by AC2 and AC5.
- **S2** — The engine's remote-ref store calls it. `manifest-check.sh` resolves the driver with
  `resolve_kit_file unattended unattended.sh`, as `derive_claims_line` does (`:645-649`), and runs the
  verb as that function runs `--claims` (`:654-655`): stdin from `/dev/null`, `GOV_RUNLOG=0`, output
  into a scratch file under `timeout -k 2 "$CARD_FETCH_BOUND"`. `card-ref — off` prints
  `card — remote-ref not written: RUN_CLAIMS is off`; no driver, no `.unattended.conf`, or no working
  `timeout -k` prints `card — remote-ref not written: <that reason>`; a kill prints `card — remote-ref
  not written: no answer within <n>s`; a loss keeps `TOOL-dPlacedRequest-2` §4's one re-render and
  retry. Each leaves the other selected stores written and the append standing. Observed by AC1 and
  AC3.
- **S3** — The engine carries no writer. The inline `gov_ref_sh` and `gov_feed_sh` blocks
  `TOOL-dPlacedRequest-2` S2 adds to `skills/session-kickoff/manifest-check.sh` are deleted, since no
  engine code calls them once S2 holds.
  **Readers:** by name: READER NOT IN TREE, since both block stems are minted in this build,
  `gov_ref_sh` by TOOL-dPlacedRequest-11 S8's parity row and `gov_feed_sh` by TOOL-dPlacedRequest-13;
  their one reader, `tools/lib/resolve-python.test.sh`, finds every copy with `git grep -l` and grades
  the copies it finds, so a deleted copy is one fewer graded and no reader names this file.
  by value: NO VALUE READERS, since no code counts the copies or compares their number. Observed by
  AC4.
- **S4** — The verbs guide (`tools/unattended/VERBS.template.md`, rendered to
  `memory/guides/UNATTENDED-VERBS.md`) gains the `--card-ref write` row and says it is dark behind
  `RUN_CLAIMS`. Observed by AC6.

## 3. Non-goals (OUT)

- No change to `card.store`'s values or default: v2:1173's three stores stay the default, and the
  switch, not the policy key, decides whether the remote one is written.
- No change to the lookup's fetch or to route rule R7's ref: findings 5, 25, 32 and 65, items of
  `TOOL-dPlacedRequest-34`, which route them through this verb family.
- No new switch: `RUN_CLAIMS` is the dark-landing switch every lease and claim write already sits
  behind (`TOOL-dPlacedRequest-1` §8 F2).

### Edges

- **consumes-from** `TOOL-dPlacedRequest-2` — the `remote-ref` store, its publish at READY and follow at a transition, and the card ref's commit message, which this unit routes through the driver; without them there is no card write to move
- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref` and `build_gov_commit` in the driver, through which the verb writes; without them the driver has no compare-and-swap writer to call
- **hands-off** `TOOL-dPlacedRequest-34` — the `--card-ref` verb family, which that unit's items for findings 18, 32, 33, 34 and 66 extend with the lookup and observe
- **hands-off** `TOOL-dPlacedRequest-43` — `--card-ref write`'s engine call, its bound and its kill line, which that unit's items for findings 5, 17, 43 and 22 bound, word and route through `run_driver_bounded`
- **hands-off** `TOOL-dPlacedRequest-49` — `--card-ref write`'s bound in S2 and its sketch, which that unit's item for finding 1 names `CARD_PUBLISH_BOUND`
- **hands-off** `TOOL-dPlacedRequest-52` — §5's risks line, which that unit's item for finding 8 re-points at `CARD_PUBLISH_BOUND`

## 4. Design

### Evidence

- `derive_claims_line` resolves the driver, checks `.unattended.conf` and a working `timeout -k`, and
  runs `--claims` into a file under `CARD_CLAIMS_BOUND` with stdin closed
  (`skills/session-kickoff/manifest-check.sh:645-655`); its header states the switch is the driver's
  and the engine never reads it (`:641-643`).
- `RUN_CLAIMS` is resolved once by the driver, blank reading `off` (`tools/unattended/unattended.sh:671-677`);
  `print_claims` answers `claims: off` without reading the remote (`:2201`).
- `resolve_claim_remote` refuses a clone without exactly one remote, check 24 (`:2100-2106`), and the
  claim read fetches with `observe_remote … --no-write-fetch-head` into the cache (`:2136`).

### The publish, end to end

```
manifest-check --card --append (READY)
  local-clone, build-folder        written as TOOL-dPlacedRequest-2 states
  remote-ref                       timeout -k 2 $CARD_FETCH_BOUND bash <driver> --card-ref write <slug> --message <tmp>
     RUN_CLAIMS off               -> card-ref — off            -> card — remote-ref not written: RUN_CLAIMS is off
     on, written                  -> card-ref — <tail> · <sha8>
     on, lost                     -> card-ref lost — <sha8>     -> re-render once, call again
     on, not written / killed     -> card — remote-ref not written: <why>
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--card-ref write` | driver verb | none |
| `write_card_ref` | shell function, the verb's body | `write`, OK |

### Rollout

Dark behind `RUN_CLAIMS`, as every governance ref write of this build: an adopter whose conf leaves it
off publishes the card to the clone and the build folder only. This repository's conf has it `on`
(`.unattended.conf:162`).

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`: the remote-ref store's call, the inline blocks deleted
- `skills/session-kickoff/card-store.fixture.sh`: the `off` and unanswered-driver plants
- `tools/unattended/unattended.sh`: `--card-ref write`
- `tools/unattended/unattended.test.sh`: the verb's arms
- `tools/unattended/VERBS.template.md`: the verb's row
- `memory/guides/UNATTENDED-VERBS.md`: its render

### Alternatives rejected

- **Ship `card.store` without `remote-ref` by default.** It departs from v2:1173's default, a design
  record's value, to answer a question the switch already answers for every other remote write.
- **The engine reads `RUN_CLAIMS` from the conf.** A second reader of the switch, against the
  engine's own stated rule (`:641-643`).
- **Ask `--claims` first.** One fetch more per publish, to learn a switch the write's own verb can
  answer.

## 5. Production-readiness checklist

- security — deny by default: no adopter writes a governance ref to the shared remote until it turns
  the switch on; the engine holds no writer.
- perf / scale — one bounded driver call per publish, replacing an inline push of the same cost.
- error / empty / loading states — every failure is a named `card — remote-ref not written:` line and
  the other stores and the append stand.
- observability — the `card-ref —` and `card —` lines.
- risks — a publish under a slow remote waits up to `CARD_FETCH_BOUND`, as the claims cell does.
- testing — the probes of §6 and the arms of §7.
- migration — none: no card ref exists before this build lands.
- user docs — `memory/guides/UNATTENDED-VERBS.md`; no `help/` page covers the kickoff engine.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-2` S12's `card-store.fixture.sh`.

- **AC1** — When `bash card-store.fixture.sh --plant publish-off` runs, with the
  fixture conf's `RUN_CLAIMS` off and `card.store` at its default, the append prints `card —
  remote-ref not written: RUN_CLAIMS is off`, the clone cache and the build-folder snapshot are
  written, and `git -C <bare> for-each-ref refs/gov/builds` prints nothing.
  Red when: an adopter with the switch off pushes a card ref, the planted case being
  `TOOL-dPlacedRequest-2`'s inline publish.
- **AC2** — When the same plant runs with `RUN_CLAIMS` on, the bare remote holds
  `refs/gov/builds/<slug>/card`, `gov-feed.log` holds its line, and
  `git rev-parse refs/gov/remote/builds/<slug>/card` names the same commit.
  Red when: the switch on does not publish, or the write skips the feed.
- **AC3** — When `--plant publish-hung` runs with a stub driver that never answers, the append prints
  `card — remote-ref not written: no answer within` and the bound, returns within the bound plus 3 s,
  and the session card is written.
  Red when: a hung driver hangs the READY append.
- **AC4** — When `git grep -n '# >>> gov_ref_sh\|# >>> gov_feed_sh' -- skills/` runs, it prints
  nothing.
  Red when: the engine still carries a writer of its own.
- **AC5** — When a probe runs `unattended.sh --card-ref write tFix --message m.txt` with `RUN_CLAIMS`
  off and a logging stub ahead of `git` on `PATH`, it prints `card-ref — off` and the stub logged no
  call.
  Red when: the off switch still reads the remote.
- **AC6** — When `grep -n -- '--card-ref' tools/unattended/VERBS.template.md` runs, the row names the
  verb and `RUN_CLAIMS`.
  Red when: the verb is undocumented.

## 7. Gates

`manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: skills/session-kickoff/card-store.fixture.sh · covers AC1 AC2 AC3 · the `publish-off` and `publish-hung` plants, staged against `TOOL-dPlacedRequest-2`'s inline publish · none
New arm: tools/unattended/unattended.test.sh · covers AC5 · the verb under the switch off with a logging `git` stub, staged against a verb that reads before testing the switch · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is the card's remote write kept dark?** (a) A driver verb that answers `off`, the engine
  calling it bounded; (b) `card.store`'s default without `remote-ref`; (c) the engine reads the conf's
  switch. (b) departs from v2's default; (c) is a second reader of the switch, against the engine's
  rule. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound, its first
  option. grants: PLAY-dClosedLoop-3 the `--card-ref` verb, the route of clause 0121's remote card ref
  · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 6 (HIGH, item H2).
- rev-2 · 2026-10-25 · promoted fix brief: S3's by-name half reads READER NOT IN TREE, since both
  block stems are minted in this build; §6 cites `card-store.fixture.sh`, which
  `TOOL-dPlacedRequest-2` creates, by basename.
- rev-3 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.
- rev-4 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-49.
- rev-5 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

The seams extended are `derive_claims_line`'s bounded driver call
(`skills/session-kickoff/manifest-check.sh:645-655`), copied in shape for the publish, and the driver's
claim block, whose `resolve_claim_remote`, `observe_remote` and `RUN_CLAIMS` resolution
(`tools/unattended/unattended.sh:671-677`, `:2100-2106`, `:2136`) the verb reuses with
`TOOL-dPlacedRequest-11`'s writer. `python tools/codebase-map/reuse_lookup.py "publish the build card
ref through the driver behind the claims switch"` ranked `build`, `claims`, `build_commit` and
`build_fixture`, name stems only; the claims cell above is the seam. `python
tools/memory-recall/query.py "how is the build card published to the remote"` returned
TOOL-aFrugalTurnstile-6's brief row, unit 2 and the audit's H2; none disagrees with source.

Recall terms used: card ref remote-ref publish RUN_CLAIMS dark switch kickoff engine write_gov_ref driver
