# TOOL-dPlacedRequest-21 — `entry.claim`: the claim ref, a patch or repeat build's derived plan record, `patch.ratify`, and every refusal routed by its cause

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 20 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0501@e1101a14 whole
**Carries:** node:policy-key.patch.ratify

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-19 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

A placed `new`, `patch` or `repeat` request becomes a build by one act, `entry.claim`: its slug claimed on the
remote by a compare-and-swap create, and for a patch or a repeat its lease taken and its derived plan record
written, the patch's held for the owner when `patch.ratify` says `owner`. Every refusal on the way routes by its
cause, so a terminal tombstone is never retried however lenient `leases` is, and a live holder is waited for
within `flow.wait-ceiling`. Today a slug is checked against local history only (`check_slug_claimed`,
`tools/memory-tree/gen_build_index.py:3940`), no claims namespace exists, and no patch or playbook run has a
plan record or a ratification (scout B's row for this unit).

## 2. Scope (IN)

- **S1** — The verb. `bash tools/unattended/unattended.sh --entry-claim <slug> --request <content key>` reads
  the placement's lines through `python tools/loop/placement.py record --request <content key>`
  (TOOL-dPlacedRequest-4 S7, with TOOL-dPlacedRequest-10's `scenarios:` and `facts:`), refuses a disposition
  other than `new`, `patch` and `repeat`, validates the slug as `cmd_new_build` does (`backlog.SLUG_RE` and a
  lower-case node letter, `tools/memory-tree/gen_build_index.py:4069-4071`), and runs `check_slug_claimed` as
  its local pre-check only. The verb is idempotent: re-run on a slug this claimant holds, it resumes at the
  first of S2 to S7 not yet witnessed. Observed by AC3.
- **S2** — The claim. A create of `refs/gov/claims/<slug>` through `write_gov_ref <ref> "" <commit>`
  (TOOL-dPlacedRequest-11, shared interface I1), its commit's message the header `gov-claim claims/<slug>` and
  the body keys of shared interface I23, rendered by `render_claim_body` in `tools/loop/claim.py`:
  `claimant-key` (`<fleet tag>:<session id>`, the fleet tag TOOL-dPlacedRequest-1 reads from
  `tools/playbook/fleet.toml`), `session`, `content-key`, `disposition`, `reason`, `scenarios`, `facts`, and
  on a patch `origin-slug` and `origin-sha`, the newest default-branch commit touching the origin's build
  folder. Answer 0 is claimed. Answer 1 reads the ref's body: this claimant's key is claimed, the retry
  counting as the first write; another key is "the slug claimed under another key", and the verb draws
  `route-back` on `item.entry.claim` through TOOL-dPlacedRequest-14's `--request-draw` and exits 5 asking
  for a fresh slug, within `flow.route-backs`. Answer 2 with the remote unreachable is handed to
  `leases.offline` as TOOL-dPlacedRequest-1 defines it, and no build folder is written, so no local id is
  minted. Observed by AC3 and AC4.
- **S3** — The lease, on `patch` and `repeat` only: the build lease `refs/gov/leases/<slug>/build`
  (shared interface I5) taken through TOOL-dPlacedRequest-1's acquire verb, since such a build never reaches
  `plan.lease`. A refusal routes by S5, and the claim stays on the remote keyed to its claimant, so a retry
  finds it claimed. Observed by AC2.
- **S4** — The derived plan record, on `patch` and `repeat` only:
  `python tools/memory-tree/gen_build_index.py --placed-build <slug> --request <content key>` with
  `--origin <slug>` or `--playbook <path>`, a sibling of `--new-build` (`cmd_new_build`, `:4050`) through a new
  `render_placed_build_readme` beside `render_new_build_readme`, written in the session's own tree and staged
  as `--new-build` stages. Its front matter carries the six keys every README carries, and on a patch
  `parents: <origin slug>`, the key TOOL-dDeclaredLoop-30 S7 reads as the originating build
  (`:1204` parses it), and on a repeat `mode: recipe` and `playbook: <path>`, the keys the driver's recipe
  mode reads (`tools/unattended/unattended.sh:4183-4192`). Its slots cite the request by its content key and
  the origin or the playbook by path, and quote no request text. Observed by AC5.
- **S5** — Refusals by cause, `route_claim_refusal(cause, leases)` in `tools/loop/claim.py`, over the one
  cause word per refusal line of shared interface I9 (flow-steps.md:53-59):

  | Cause | Route |
  |---|---|
  | `tombstone`, `terminal`, `epoch-fence` | refused whatever `leases` says, never retried; the verb prints one `ask:` line naming the slug, the cause and the content key for the session to file, and exits 1 |
  | `live-holder`, `offered` | a wait, contention that draws nothing: the first refusal adds `wait-since: <UTC>` to the claim body by a parented commit, and once `flow.wait-ceiling` has passed since it, by this node's own clock against its own stamp, the verb prints an owner item and exits 1; before, it exits 4 |
  | `overlap` | as `leases` says: under `leases: warn`, noted as an `overlap:` key on the claim body and on stdout, then taken as held; under `refuse`, as `live-holder` |
  | `offline` | as `leases.offline` says, through TOOL-dPlacedRequest-1 |

  `flow.wait-ceiling` is read through dGroundRules-2's `resolve`, TOOL-dDeclaredLoop-33 S5's 72 hours as the
  catalogue default until it lands. Observed by AC1, AC2 and AC6.
- **S6** — `patch.ratify`, read through dGroundRules-2's `resolve` (`python tools/policy/policy.py get
  patch.ratify`), its catalogue row written by dGroundRules-1 S3, v2's default `auto` (v2:1333) the stand-in
  until the reader lands. Under `auto` the patch's derived plan record stands. Under `owner` the verb prints
  `owner item: ratify <slug>`, and `check_patch_ratified(slug)` in `tools/loop/claim.py` answers held until
  the patch build's folder holds an owner's disposition record (TOOL-dDeclaredLoop-16 S4) whose `Item` is
  `item.entry.claim` and whose `Disposition` is `ratified`; `rejected` holds it for good. TOOL-dDeclaredLoop-3's
  `write_transition` calls `check_patch_ratified` before it writes a record into `designing` for a build whose
  claim body reads `disposition: patch`, and refuses naming `patch.ratify` and the owner item while it is held.
  Observed by AC1.
- **S7** — The first transition record. Once S2 to S6 are witnessed, the verb writes the build's first record
  through `write_transition`, carrying ` · scenario=<tags>` from the claim's `scenarios` (TOOL-dDeclaredLoop-27
  S8's field): `new` into `planning`, `repeat` into `designing`, and `patch` into `designing`, the record S6
  gates. dRankedPlan's `plan.dedupe` between a patch's claim and Design is not built; until it lands the patch
  goes straight to the gated record, and the stand-in is named in `tools/loop/claim.py`'s `STAND_INS` row
  for it. Observed by AC7.
- **S8** — The fixture plants of §6, `python tools/loop/claim.py --fixture`, against a bare scratch remote,
  the leg `loop claim fixtures` in `tools/gate-legs.json`, argv `python {prefix}/loop/claim.py --fixture`,
  declared in `tools/loop/kit.toml`. Observed by AC1 to AC7.

## 3. Non-goals (OUT)

- The lease grammar, its acquire verb, its epoch, tombstones, offers and offline queue: TOOL-dPlacedRequest-1,
  -16, -17 and -20's; this unit reads the cause word their refusal prints.
- The compare-and-swap writer and its parented commits: TOOL-dPlacedRequest-11's `write_gov_ref`.
- The placement and its record: TOOL-dPlacedRequest-4's; the scenarios: TOOL-dPlacedRequest-10's.
- The pre-claim budget: TOOL-dPlacedRequest-14's; this unit is one of its draw sites.
- The slug's descriptive half, minted from a plan record's title (memory `[names]`): the caller passes the slug,
  as `--new-build`'s caller does today.
- `plan.dedupe`, the plan record kind and its writer `plan.record`: dRankedPlan's. The derived plan record of S4
  is the README scaffold until that kind lands.
- A programmatic ask filer: none exists (`tools/memory-tree/backlog.py` parses rows and writes none), so the
  verb prints the ask and the session files it.
- The mailbox note an overlap under `warn` also owes the other build: dKeptSession's.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, the create of the claim ref, and `build_gov_commit`, the parented commit that adds `wait-since` or `overlap`
- **consumes-from** `TOOL-dPlacedRequest-1` — `refs/gov/leases/<slug>/build`, the lease a patch or repeat takes, the fleet tag and the cause word each refusal prints
- **consumes-from** `TOOL-dPlacedRequest-19` — `request_content_key`, the key the claim carries so a retry finds its own claim
- **consumes-from** `TOOL-dPlacedRequest-4` — `disposition`, the lines `placement.py record` prints, which the claim commit carries
- **consumes-from** `TOOL-dPlacedRequest-10` — `scenarios`, the checked selection the claim and the first transition record pin
- **consumes-from** `TOOL-dPlacedRequest-14` — `--request-draw`, the draw before each fresh slug
- **hands-off** `TOOL-dPlacedRequest-3` — `refs/gov/claims/<slug>`, the claim ref `entry.claim`'s item row names as its witness
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-43` — `--entry-claim`'s read of `leases.offline`, which that unit's item for finding 8 names in the stops guide's population

## 4. Design

### The act, in order

```
--entry-claim <slug> --request <key>
  lines   := placement.py record --request <key>            # refuses unless new|patch|repeat
  slug shape, check_slug_claimed                            # local pre-check only
  claim   := write_gov_ref refs/gov/claims/<slug> "" $(build_gov_commit "" <render_claim_body(lines)>)
             1 -> own claimant-key ? claimed : --request-draw route-back item.entry.claim; exit 5
             2 -> leases.offline (unit 1); no folder written
  patch|repeat:
    lease  := unit 1 acquire refs/gov/leases/<slug>/build   # refusal -> route_claim_refusal
    record := gen_build_index.py --placed-build <slug> …    # staged in the session's tree
    patch && patch.ratify == owner -> print owner item
  write_transition first record, scenario=<tags>            # patch into designing gated by check_patch_ratified
```

### Data model

```
gov-claim claims/dLandedFix

claimant-key: a:5d0c…-session
session: 5d0c…-session
content-key: 3f9c2a7d01be
disposition: patch
reason: the landed fix regressed the lander's retry
scenarios: scenario.patch
facts: entry=patch; design-only=false
origin-slug: dLandedThing
origin-sha: 9a1b…
```

A later commit on the ref, parented on this one, may add `wait-since:` or `overlap:`; `read_claim_body`
reads the newest commit's keys over the first's.

### Inventory

| Minted | Kind |
|---|---|
| `--entry-claim` | driver verb, `tools/unattended/unattended.sh` |
| `run_entry_claim` | bash function, `tools/unattended/unattended.sh` |
| `tools/loop/claim.py`, `render_claim_body`, `read_claim_body`, `route_claim_refusal`, `check_patch_ratified`, `STAND_INS` | module, functions and table |
| `--placed-build`, `render_placed_build_readme` | flag and function, `tools/memory-tree/gen_build_index.py` |
| `refs/gov/claims/<slug>` | ref namespace, the claim (shared interface I23) |
| `claimant-key`, `content-key`, `origin-slug`, `origin-sha`, `wait-since`, `overlap` | claim body keys |
| `loop claim fixtures` | gate leg |

Each function name is put to `python tools/lexicon/lexicon.py --suggest <name>` with its cell in the build pass.
The exit codes 4 (waiting) and 5 (fresh slug owed) are the verb's own, printed by name beside the code.

### Migration

None. No `refs/gov/claims/*` ref exists; today's run claims under `refs/gov/runs` are TOOL-dPlacedRequest-1's to
migrate.

### Rollout

Live at landing. A session that never places a request never calls the verb, and the `write_transition` gate
reads only builds whose claim body says `patch`.

### Files touched (estimate)

- `tools/loop/claim.py` (new)
- `tools/loop/loop_transition.py`: `write_transition` calling `check_patch_ratified`
- `tools/loop/kit.toml`: the module and its leg declared
- `tools/gate-legs.json`: the leg `loop claim fixtures`
- `tools/unattended/unattended.sh`: `--entry-claim` and `run_entry_claim`
- `tools/unattended/VERBS.template.md`: the verb's line
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/memory-tree/gen_build_index.py`: `--placed-build` and `render_placed_build_readme`
- `help/loop.md`: the entry section names the claim, `patch.ratify` and the refusal routes

### Alternatives rejected

- **Reuse `refs/gov/runs/<slug>` for the claim.** A run claim is an unattended run's hold on a build that
  exists; the claim mints a slug before any build or run exists, and flow-steps.md:127 names its own namespace.
- **A new `plan` record kind for the derived plan record.** The kind is dRankedPlan's (layer-memory's kind
  table, `plan` owned by dRankedPlan); the README scaffold already carries the two facts its readers need.
- **Judge `flow.wait-ceiling` on the holder's stamp.** Two clocks would decide it; the waiting node measures
  its own wait against its own stamp.

## 5. Production-readiness checklist

- security — the claim body carries the placement's redacted, capped reason and closed-shape facts, never the
  request's text; the derived plan record cites the request by key.
- perf / scale — one create, at most one lease acquire and one staged README per claim.
- error / empty / loading states — a wrong disposition, a bad slug, a slug taken under another key, an
  unreachable remote and each lease cause refuse or wait by name; the verb resumes where it stopped.
- observability — the claim ref's history is the act's record; every refusal line names its cause.
- risks — the session files the `ask:` line the verb prints; a session that does not leaves the refusal on
  stdout only, which the closing review of the build reads.
- testing — the fixture plants of AC1 to AC7; the suite arms in §7 at the close.
- migration — none.
- user docs — `help/loop.md`'s entry section.

## 6. Acceptance criteria

- **AC1** — When `python claim.py --fixture --plant patch-owner-unratified` claims a patch under
  `patch.ratify` = `owner` and then asks `write_transition` for its record into `designing`, the write is
  refused naming `patch.ratify` and the owner item, and `--plant patch-owner-ratified`, whose folder holds the
  owner's disposition record `ratified` for `item.entry.claim`, writes it.
  Red when: a patch under `owner` reaches Design unratified.
- **AC2** — When `python claim.py --fixture --plant tombstone-warn` replays a take against a build whose lease
  ref holds a terminal tombstone, under `leases: warn`, the verb exits 1 naming `tombstone`, prints one `ask:`
  line, and the scratch remote shows no second take attempt.
  Red when: `warn`'s leniency lets the take through, or the verb retries it.
- **AC3** — When `python claim.py --fixture --plant claim-twice` runs the verb twice with one claimant key, the
  second run reports the slug claimed and the claim ref has one commit.
  Red when: a retry by the same claimant is read as another session's claim.
- **AC4** — When `python claim.py --fixture --plant slug-taken` claims a slug whose ref carries another
  claimant key, the verb exits 5 and the request ref gains one `route-back · item.entry.claim` row; with the
  scratch remote unreachable, no build folder is written.
  Red when: a slug taken elsewhere is used, or a local folder is minted while the remote is down.
- **AC5** — When `python gen_build_index.py --placed-build dFixPatch --request <key> --origin dLanded` runs in
  the fixture repository, the staged README's front matter carries `parents: dLanded`, and with
  `--playbook <path>` it carries `mode: recipe` and the `playbook:` key, and neither quotes the request text.
  Red when: the patch's origin is not recorded, so its budget draws land on no build.
- **AC6** — When `python claim.py --fixture --plant live-holder` has the lease refuse `live-holder`, the first
  run exits 4 and adds `wait-since:` to the claim body, and a run whose fixture clock is past
  `flow.wait-ceiling` exits 1 printing the owner item; `--plant overlap-warn` under `leases: warn` proceeds
  with an `overlap:` key.
  Red when: a live holder is refused outright or retried with no ceiling.
- **AC7** — When `python claim.py --fixture --plant first-record` claims a `repeat`, the build's first
  transition record is into `designing` and carries `scenario=scenario.playbook-run`.
  Red when: the claimed build has no first record, so its scenario falls back to the default.

## 7. Gates

`build-index selftest` · `tier2-review self-test` · `run-gates canary` · `run-gates gov canary` · `measure-legs selftest` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/claim.py · covers AC1 AC2 AC3 AC4 AC6 AC7 · the `loop claim fixtures` leg's plants, its failing case staged by `tombstone-warn` with `route_claim_refusal` reading `leases` first · none
New arm: tools/memory-tree/gen_build_index.py · covers AC5 · the `build-index selftest` leg's `--placed-build` case, its failing case staged by a patch scaffold with no `parents:` key · none
New arm: tools/unattended/unattended.test.sh · covers AC2 AC4 · the `--entry-claim` cases over a scratch remote, the failing case staged by a retried tombstone take · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`. Observation, 2026-10-25: `DRAFT` is
  not in the tuple. Liveness: the tuple would list it if the vocabulary admitted it. RESOLVED (agent,
  2026-10-25, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — What is a patch's or a repeat's derived plan record before dRankedPlan's `plan` kind lands?**
  Options: (a) the README scaffold, `parents:` on a patch and `mode: recipe` with `playbook:` on a repeat;
  (b) a new record kind through PLAY-dOrderedCharter-7 S7's factory; (c) no record until Plan lands. (b)
  registers a kind another build owns; (c) fails the clause's "writing a patch or repeat build's derived plan
  record". RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, reusing `cmd_new_build`'s scaffold and the
  two front-matter keys their readers already parse. widens: none · relaxes: none
- **F3 — Whose clock judges `flow.wait-ceiling` on a live-holder wait?** Options: (a) the waiting node's own,
  against its own `wait-since` stamp; (b) TOOL-dPlacedRequest-17's observer clock. (a) compares one node's
  clock with itself, so the skew TOOL-dPlacedRequest-17 guards against cannot arise. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3. widens: none · relaxes: none
- **F4 — Where does the ask a terminal refusal owes go?** Options: (a) the verb prints it and the session files
  it; (b) the verb appends a row to a `BACKLOG.md`. (b) adds a write path into another build's records with no
  existing writer to extend. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the ask-filing path every
  session uses today. widens: none · relaxes: none
- **F5 — Where does `entry.claim`'s act live?** Options: (a) a driver verb, `--entry-claim`, beside the run
  claim's writer and the lease verbs, with its python half in `tools/loop/claim.py`; (b) a python module
  pushing the claim itself; (c) a kickoff step the agent performs by hand. (b) is a hand copy of the
  compare-and-swap push TOOL-dPlacedRequest-11 merges into one; (c) leaves the act with no witness but the
  agent's word. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the most feature-rich survivor and the
  seam the writer already lives in. grants: PLAY-dClosedLoop-3 the --entry-claim verb and its line in
  tools/unattended/VERBS.template.md and its render memory/guides/UNATTENDED-VERBS.md · widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, from the packet's Items 21, the brief's shared interfaces I1, I5, I9 and
  I23, scout B's row for TOOL-dPlacedRequest-21, flow-steps.md:53-59, :127 and :729-735, v2:1333, and
  TOOL-dDeclaredLoop-16, -30 and -33, read at base `c63aabbb`.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: §7's leg line gains `tier2-review self-test`,
  `run-gates canary`, `run-gates gov canary` and `measure-legs selftest`, the legs
  `tools/memory-tree/gen_build_index.py` and `tools/gate-legs.json` in Files touched trip.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-34,
  each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seams: `check_slug_claimed` (`tools/memory-tree/gen_build_index.py:3940`) as the local pre-check and
`cmd_new_build` (`:4050`) with `render_new_build_readme` as the scaffold the derived plan record extends;
TOOL-dPlacedRequest-11's `write_gov_ref`, the extraction of `write_claim` (`tools/unattended/unattended.sh:2396`)
whose refusal split, 1 lost and 2 not completed (`:2456-2457`), the claim's answers mirror; TOOL-dPlacedRequest-1's
acquire verb and cause words; TOOL-dDeclaredLoop-16's disposition record for the ratification. `python
tools/codebase-map/reuse_lookup.py "claim a build slug by compare-and-swap ref and write a derived plan record"`
ranked `write`, `slug`, `write_text` and `claims` by name stem, none a claim writer but the run claim scout B
names. Where the scout record and source disagree: scout B cites the refusal verdicts `fail 108` and `fail 109` at
`:2449-2452`, and at base they sit at `:2456-2457`; its `cmd_new_build` at `:4050` and `check_slug_claimed`
at `:3940` match. `python
tools/memory-recall/query.py "how does entry.claim claim a patch build"` returned scout B's row, the packet's
Items 21 and the brief's row.

Recall terms used: entry.claim refs/gov/claims patch.ratify derived plan record origin slug lease tombstone flow.wait-ceiling
