# Brief — dShippedRelease: the spec audit's round-2 disposal

**Serves:** research DEPL-dShippedRelease-49

## The prompt

> Dispose every confirmed finding of the round-2 spec audit of dShippedRelease, whose harness disposal stage died on a usage limit before it wrote anything.

## The brief

### Goal

Every confirmed finding in `memory/builds/dShippedRelease/reviews/2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md` promoted into a unit with a spec, exactly as the harness's disposal stage would have done it. The audit exited BOUNDED with 106 confirmed findings, 8 at BLOCKER and 19 at HIGH, and 0 unverified.

### Items

Read `memory/guides/BUILD-METHOD.md` WHOLE first, then the report, `memory/TEMPLATE-SPEC.md`, and `memory/builds/dShippedRelease/README.md`. Round 1's disposal is the worked example: its `--rescope` rows are in `memory/builds/dShippedRelease/RUN.md`, and units 49 to 78 are its specs.

1. Take each confirmed finding at the severity the report gives it. Every count is of RAW findings by report id, never of the items a report merges them into: a finding merged into an item takes that item's severity and still counts once, by its own id.
2. Each BLOCKER or HIGH id is its own unit even where the report merged several ids into one item, because the unit floor, the driver's owed count and check 2 all count raw ids: ids sharing an item each take a unit, and each unit's spec names its id and the item it shares. Unit ids start at DEPL-dShippedRelease-79: 32 to 48 are filed asks and 49 to 78 are round 1's units.
3. For each: `bash tools/unattended/unattended.sh --rescope dShippedRelease --act add --item <id> --reason "closes 2026-10-30-review-DEPL-dShippedRelease-49-spec-audit-round1.md id <n> (<SEV>, item <item>): <one line>"`, then author its spec at Tier-2, path `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-<n>.md`, with a mechanism that CLOSES the finding: the change to the design and the artifact that proves it. Header as units 49 to 78 write it, with `advances DEPL-dShippedRelease-32`.
4. Give each spec an `order` verb that places it immediately after the unit it repairs: one above that unit's own order. Units sharing an order are a parallel group, so a tie is the intended shape and nothing downstream is renumbered. A promotion that repairs no unit in particular takes an order above every unit in this build.
5. Promote every MEDIUM and every LOW too, batched: all of them into ONE unit whose spec names every finding by report id in its §1 and gives each its own §2 item. Use TWO units only when the minors split into two disjoint write sets by BUILD-METHOD M6's clauses. Add each by the same `--rescope --act add`, its reason naming every report id it closes. A finding is not an ask: name it in scope, never through the `closes` verb.
6. Nothing is folded, parked, waived, retired or re-reviewed. A CONFIRMED finding may not be refuted. Audited spec text stays as written: each promoted spec names what it supersedes.
7. Every §3 edge gets both its ends in this pass: a **consumes-from** `X` in one spec is a **hands-off** back in X's own §3, amended there as a rev-N bump with its §9 line.
8. Stage everything under `memory/builds/dShippedRelease/spec/` and commit nothing. Regenerate no index and touch no README, deviation record or `BACKLOG.md`. Temp files go under the session scratchpad spelled absolute, and a git clone under `%TEMP%/<short-name>`. Speak only in your return value.

### Acceptance

Your return names, for the 106 findings: `promoted` and `refuted` as counts by report id, every id counted once; `promotedIds`; `standing`, every finding not disposed, which must be empty; `edges`, every §3 edge bullet written or amended as `{from, verb, to}`, a paired edge appearing twice; and `placements`, one `{unit, repairs, order}` per promoted unit. A join of the report's raw ids against your specs finds none missing, extra or duplicated.

### Gates

`bash tools/memory-tree/check-memory-hygiene.sh --only 2,12,13,23,25` over the staged specs, and no other gate, suite or bar. Those checks grade tracked files, so stage first. `tools/check-spec-tokens.py` and `carries.py` are the main loop's.

### Non-goals

No product code. No edit to v2, the as-built view, the packet or an instrument. No spec of another build: a change one owes is stated in §8 as an ask with its target build and accept line, and your return names it.
