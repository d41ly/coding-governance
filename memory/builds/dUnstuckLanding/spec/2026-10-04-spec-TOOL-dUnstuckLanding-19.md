# TOOL-dUnstuckLanding-19 — refresh before a verdict: one helper, the `refreshed-at` fact

**Status:** CLOSED · rev-2 · 2026-10-04 · node d · Tier-2 · base 98926870 · streams tooling · order 7 · closes TOOL-dUnstuckLanding-9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-dUnstuckLanding-19-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-dUnstuckLanding-19-1-acceptance-ledger.md) | journal | — |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-build-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-20 |
| [2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md](../prompts/2026-10-04-prompt-TOOL-dUnstuckLanding-13-spec-brief.md) | journal | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-20 |
| [2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md](../reviews/2026-10-04-review-TOOL-dUnstuckLanding-13-implementation-diff-round1.md) | diff-review | TOOL-dUnstuckLanding-13 TOOL-dUnstuckLanding-14 TOOL-dUnstuckLanding-15 TOOL-dUnstuckLanding-16 TOOL-dUnstuckLanding-17 TOOL-dUnstuckLanding-18 TOOL-dUnstuckLanding-20 TOOL-dUnstuckLanding-25 |

<!-- /gen:spec-records -->

## 1. Goal

A run that parks, hands off, aborts or closes takes a verdict against the BASE it pinned, and the
census found three verdicts that main had already overtaken (design section 6). Give the driver one
quiet helper that observes the remote's advertised tip, prints the commits on it since BASE that
touch this build's README or its declared writes, and records the tip as a `refreshed-at` fact, so
a stale verdict is visible in the record instead of to the next person who trips on it.

## 2. Scope (IN)

- **S1 — the helper.** One function in `tools/unattended/unattended.sh`, named `derive_refreshed_at`,
  because the lexicon's closed verb table holds no `refresh` and `--suggest` returned no name. It takes
  the run-state file, the slug and the calling verb's name. It never calls `fail`, never writes, and
  never touches the global `status`. It sets one global, the fact value, for the caller to write.
  Observed by AC1, AC2, AC5, AC6, AC8.
- **S2 — the observation.** The tip comes from `read_advertised_tip`, the existing quiet,
  once-per-process observer, which reuses an anchor `observe_anchor` already took in this process.
  The helper does no second `ls-remote` when one was already made. Observed by AC4, AC5.
- **S3 — the touch set and the listing.** The touch set is the build README, from `readme_of`, plus
  every path any `dispatch` row in the run-state file declares. The listing is the commits reachable
  from the tip and from neither BASE nor HEAD, restricted to the touch set, read with literal
  pathspecs. It prints at most ten rows and then a count of the rest, and always prints the full
  count. Observed by AC1, AC2.
- **S4 — the fact.** `refreshed-at: <tip sha> · <verb> · <n> touching` when the tip was observed
  and is in this clone; `refreshed-at: <tip sha> · <verb> · unlisted` when it was advertised but the
  object is absent; `refreshed-at: unobserved · <verb>` when the remote did not answer, the bound
  fired, or the record has no `base` fact. It is a singleton the next call overwrites. Observed by
  AC1, AC5, AC6.
- **S5 — the four call sites.**
  - `--park`, after its idempotent no-op check and before `park`. An idempotent re-park writes
    nothing and does not refresh.
  - `--abort`, after both attested items read met and before the phase write.
  - `--handoff`, the verb `TOOL-dUnstuckLanding-13` ships, after its last refusal and before its
    first write.
  - `--close` under `LANDER_MODE=primary` only. The listing prints after `observe_anchor` and
    before the Definition of Done loop, so a close that refuses still shows it. The fact is written
    with the close's other writes, after the DoD is met, so a refusing close still writes no
    `refreshed-at`.

  Observed by AC1, AC2, AC3, AC4, AC7.
- **S6 — the carriers.** `tools/unattended/VERBS.template.md` gains one sentence on each of the four
  entries. `tools/unattended/PROTOCOL.template.md` §2 gains the fact as the next numbered authored
  fact. Both renders under `memory/guides/` are re-copied by `bash tools/unattended/adopt-unattended.sh`
  in the same pass. Observed by AC9.

## 3. Non-goals (OUT)

- No refusal. Candidate (a) of design section 6, refusing until the run merges the tip, was rejected
  there: it adds a mid-run write that can conflict, and it makes the cheapest honest act the most
  expensive one.
- No fetch. The helper changes no ref. A tip this clone lacks is reported as `unlisted`.
- No call from `--hold`, `--phase`, `--status`, `--resume`, or from `--close` under `in-place`.
  Under `in-place` the run's `--prepare` already merges the tip before the bar.
- No conf key. The helper runs on every call site with no switch.
- No touch set wider than the README and the declared writes. Specs, the build's `BACKLOG.md` and
  sibling builds' folders are follow-ups if a census shows a verdict overtaken through them.
- No reader of the fact. The wrap-up and `runlog` may read it later; no gate grades it here.

### Edges

- **consumes-from** `TOOL-dUnstuckLanding-13` — the `--handoff` verb, which this unit adds one call
  to. Without it S5's third call site has nothing to sit in, and AC3 cannot run.

## 4. Design

### Data model

One authored fact in `RUN.md`'s run-facts region, written through `set_fact`:

```
refreshed-at: <sha40|unobserved> · <verb> · <n> touching|unlisted
```

The verb field is the calling verb without dashes. The third field is absent on `unobserved`.

### The helper's flow

1. If the record has no `base` fact, print that the verdict cannot be refreshed and set the value
   to `unobserved · <verb>`. Return 0.
2. Call `read_advertised_tip`. On a non-zero return with `ADVQ_SHA` empty, print
   `unattended: refresh — the advertised tip was NOT observed, so this verdict stands on BASE <b8>
   alone: <ADVQ_WHY>` and set `unobserved`. On a non-zero return with `ADVQ_SHA` set, the tip was
   advertised and is absent here: print that, and set `<sha> · <verb> · unlisted`.
3. Build the touch set: the README path, then each `dispatch` row's reason field split on spaces.
   The rows are already normalised by `--dispatch`'s `normpath`.
4. `GIT --literal-pathspecs log --format='%h %s' <tip> --not <base> HEAD -- <set>`, bounded to
   ten printed rows. Also count `<tip> --not <base> HEAD` without paths, so the line reads
   `<n> of <m> commits`.
5. Print `unattended: refresh — <ref> at <sha8> · <n> of <m> commits since BASE <b8> touch this
   build's README or declared writes`, then the rows indented, then `… and <k> more` past ten.

### Why `read_advertised_tip` and not `observe_anchor`

`observe_anchor` refuses through `fail`, which prints and sets the global `status` with no reset,
so a verb calling it would exit non-zero after a correct write. `read_advertised_tip` was written
for exactly that reason (`tools/unattended/unattended.sh:1182-1187`) and is once per process. On
`--close`, when `observe_anchor` already failed, the helper must not pay a second bounded wait: the
close marks the quiet observer done with the anchor's refusal as its reason before calling the
helper.

### Inventory

- The helper function (S1). Its name is graded by the lexicon gate's shell cell; ask
  `python3 tools/lexicon/lexicon.py --suggest <name> --as sh.function` before writing it.
- The fact key `refreshed-at`.
- No new `fail` branch, so no arm or unarmed-branches row is owed for one.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/PROTOCOL.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-PROTOCOL.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- Listing `<base>..<tip>`. After an in-run merge of main it lists commits the run already has, which
  is noise in the one read the owner gets. Excluding HEAD keeps "since BASE" and drops what is
  already integrated.
- Writing the fact before the close's DoD loop. A refusing `--close` would then write, and "a
  refusal writes nothing" is an invariant the driver suite pins.
- Leaving a stale `refreshed-at` in place on an unanswered remote. It would claim a refresh that
  did not happen, so the value becomes `unobserved`.

## 5. Production-readiness checklist

- security — no new authority. The helper reads refs and an advertisement the driver already
  trusts, writes one fact through `set_fact`, and uses literal pathspecs so a declared path cannot
  carry pathspec magic.
- perf / scale — one bounded `ls-remote` per verb call, at most `REMOTE_BOUND` seconds when the
  remote does not answer, and none on `--close`, which reuses its anchor. Two `git log` walks over
  the commits since BASE.
- error / empty / loading states — no base fact, an unanswered remote, a fired bound, an absent
  tip object, an empty touch set and zero touching commits each print one line and record a value.
  None of them stops the verb.
- observability — the listing on stdout, and the fact in the record the wrap-up reads.
- risks — an offline `--park` now waits up to the remote bound before writing. The bound is the
  existing one and is announced on the line that reports it.
- testing — arms in the driver suite, named in §7.
- migration — none. Old records simply lack the fact.
- user docs — the VERBS entries and PROTOCOL §2, rendered into `memory/guides/`.

## 6. Acceptance criteria

Fixture F, used below unless a criterion says otherwise. `fixture:` the tree holds none today; the
builder makes it under `%TEMP%/rf19`. A bare origin and a clone. The clone carries this tree's kit
under `tools/unattended/`, the kit example conf as `.unattended.conf`, and a build `fx` with a
README and a `RUN.md` carrying `phase: BUILDING`, `base: <B>`, both attested items met, and one
`dispatch` row declaring work/a.txt. The origin's main then gains three commits past B: one
touching the fixture README, one touching work/a.txt, one touching other.txt. The
clone fetches and does not merge. UNVERIFIED that the example conf alone satisfies the driver's
startup reads; the builder adds what it refuses on.

- **AC1** — When `bash tools/unattended/unattended.sh --park fx --item q1 --reason r1` runs in F,
  stdout carries a `refresh —` line reading `2 of 3 commits`, lists the README commit and the
  work/a.txt commit, and does not list the other.txt commit. `RUN.md` then reads
  `refreshed-at: <origin main sha> · park · 2 touching`.
  Red when: the listing omits either touching commit, lists other.txt's, or the fact is absent.
- **AC2** — When `--abort fx --code external-prerequisite --reason r2` runs in a fresh copy of F,
  stdout carries the same two rows and `RUN.md` reads `refreshed-at: <sha> · abort · 2 touching`
  beside `phase: ABORTED`.
  Red when: the abort completes with no refresh line or no fact.
- **AC3** — When `--handoff fx --code owner-decision --reason r3 --reaped <id>` runs in a fresh copy
  of F after AC1's park, stdout carries the two rows and the fact reads `· handoff · 2 touching`.
  Red when: the hand-off writes HELD with no refresh line or no fact.
  `fixture:` needs `TOOL-dUnstuckLanding-13` built first.
- **AC4** — When `--close fx` runs under `LANDER_MODE=primary` in a copy of F whose DoD has an unmet
  item, stdout carries the `refresh —` line before the unmet item, and `git diff` over the fixture RUN.md
  shows no `refreshed-at` line added. When the same close runs in a copy whose DoD is met, `RUN.md`
  reads `refreshed-at: <sha> · close · 2 touching` beside `phase: LANDING`.
  Red when: the refusing close writes the fact, or the met close does not.
  `cost:` the met arm needs a fixture whose every machine item passes; build it by hand from the
  recipe the driver suite's met-close fixture uses, minutes rather than seconds.
- **AC5** — When F's clone runs `git remote set-url origin <a path that does not exist>` and then
  `--park fx --item q5 --reason r5`, stdout says the advertised tip was NOT observed, the verb exits
  0, the decision is parked, and `RUN.md` reads `refreshed-at: unobserved · park`.
  Red when: the park refuses, exits non-zero, or keeps an older tip in the fact.
- **AC6** — When F's clone has NOT fetched the origin's three commits, `--park fx --item q6 --reason r6`
  prints that the tip is advertised and absent here, and records `refreshed-at: <sha> · park · unlisted`.
  Red when: an absent tip is reported as unobserved, or as zero touching commits.
- **AC7** — When `--close fx` runs under `LANDER_MODE=in-place` in a copy of F whose DoD has an
  unmet item, stdout carries no `refresh —` line.
  Red when: the in-place close prints one.
- **AC8** — When `awk '/^derive_refreshed_at\(\)/,/^}/' tools/unattended/unattended.sh` slices the helper,
  a `grep -cE '^[[:space:]]*(fail [0-9]|set_fact |park )'` over the slice prints `0`.
  Red when: the helper calls `fail`, writes a fact, or parks.
- **AC9** — When `grep -n 'refreshed-at' tools/unattended/PROTOCOL.template.md tools/unattended/VERBS.template.md`
  runs, PROTOCOL §2 carries the numbered fact and each of the four verb entries mentions it, and
  `cmp` of each template against its `memory/guides/UNATTENDED-*.md` render reports no difference.
  Red when: a template is edited and its render is not re-copied, or an entry is missing.

## 7. Gates

`unattended kit gate` · `unattended protocol size` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `recall floor` · `recall floor arms`

The suite arms are held self-tests and run only on demand; they are declarations, not part of this
unit's verification, which is the direct checks in §6.

New arm: tools/unattended/unattended.test.sh · a park, an abort and a primary close over a fixture whose origin moved past BASE, then an unreachable remote · none
New arm: tools/unattended/unattended.test.sh · an in-place close over the same fixture, asserting no refresh line · none

## 8. Open questions

- **F1 — which observer the helper uses.** (a) `observe_anchor`, as design section 6 says. (b)
  `read_advertised_tip`. RESOLVED (agent, 2026-10-04, delegated): (b). Option (a) fails AC5,
  because its `fail` sets the global status and the verb would exit non-zero over a completed park;
  (b) satisfies every criterion and reuses a seam already written for this reason.
- **F2 — which commits count as "since BASE".** (a) `<base>..<tip>`. (b) the tip `--not` BASE and
  HEAD. RESOLVED (agent, 2026-10-04, delegated): (b). It keeps the ask's "since BASE" and drops
  commits the run already merged, so more of the listing is signal; no criterion is lost.
- **F3 — what the close does when the DoD is unmet.** (a) print and write the fact anyway. (b)
  print, and write only on a met DoD. RESOLVED (agent, 2026-10-04, delegated): (b). Option (a)
  breaks the pinned invariant that a refusing close writes nothing, so it fails a gate already
  written.
- **F4 — an advertised tip this clone lacks.** (a) fetch it. (b) report `unlisted`. RESOLVED (agent,
  2026-10-04, delegated): (b). Option (a) adds a ref write the design ruled out and widens the
  verb's write surface (veto 3).

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from design section 6 at rev-2 and ask `TOOL-dUnstuckLanding-9`.
- rev-2 · 2026-10-04 · at build. The helper's name: the lexicon refused the verb refresh and its
  suggest offered none, so S1 and AC8 name `derive_refreshed_at`, which sets a derived value and
  prints. Two edges the flow did not state: a record with no Run facts section prints one line and
  records no fact, since `set_fact` would refuse there and the verb must not stop; and a tip taken
  from an anchor this process observed is object-tested here, since the quiet observer skips that
  test for a reused anchor. Status CLOSED.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "observe the remote advertised tip and list commits since
base touching the build's declared write set before a park or abort verdict"` returned only Python
name-stem neighbours, and its own coverage line reports `.sh` as an unscanned layer, so the map is
blind to the driver. The recall probe found the seam the map could not: `read_advertised_tip` in
`tools/unattended/unattended.sh:1187`, cited by `TOOL-dDerivedDocket-22`'s spec as the quiet
observer in `branch_tip_quiet`'s shape. That is the seam this unit extends. The touch set reuses
`readme_of` and the `dispatch` rows `verb_dispatch` parks, already normalised. The fact goes through
`set_fact`. The design record says "`observe_anchor` already does the first"; verified against
source, that function refuses through `fail` and is the wrong seam for a verb that must complete,
so the record and the source disagree and this spec follows the source.

Recall terms used: `python tools/memory-recall/query.py "how does a run observe the remote's
advertised tip before a verdict, and was a stale base ever caught at park or abort" --terms
"observe_anchor advertised tip stale BASE ls-remote refresh park abort verdict unattended run-state fact"`
