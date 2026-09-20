# TOOL-dDerivedDocket-30 — checker defects from the stop census

**Status:** SPECCED · rev-4 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 30

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

Three recorded unattended runs stopped on defects in the unattended kit's own gate leg. At BASE two
are still open and the first is half closed. Check 23 now excuses the path a unit's brief row names,
but on the path alone, so a row can excuse a path that is no brief and an edited brief goes unseen;
`check-unattended.sh --only 28` dies on an unbound variable; and the leg's conf allow-list is a
hand-typed key set nothing joins. Finish the first and fix the other two, and gate the CLASS behind
the second: a flag a parser accepts that no document names and no arm exercises is the one
invocation nobody runs.

## 2. Scope (IN)

- **S1** Check 23 covers a committed path P, and stops reporting it, only when all three hold: the
  run-state file carries a `brief · item <unit> · reason <h12> P` row for THE unit whose pass commit
  is under test; P lies under the build's own `prompts/`; and P's blob at that commit starts with
  `<h12>`. The first condition LANDED in `TOOL-aRatifiedRulings-2`, which built the owner ruling
  `TOOL-aLeakedHandle-7`: `read_brief_paths` in `tools/unattended/lib-unattended.sh` reads the unit's
  rows from the run-state file at the pass commit, check 23 excuses exactly those paths with a
  `report` line, and `pass_commit` subtracts the same set. The remainder is the other two, applied
  inside `read_brief_paths`, so the commit selector and check 23 still excuse one set. Any other
  outside path is reported exactly as at BASE. Observed by AC1 and AC2.
- **S2** The conf import, the whole of check 1's block, moves above the `only28` guard, so every
  conf-read value is set whatever the scope. Under `--only 28` each numbered check after the 28
  region prints one announced skip naming itself on the leg's REPORT channel, and the list of those
  checks is derived from the file's own check headers rather than typed. Observed by AC3.
- **S3** The check-22 allow-list join. The keys the shipped `.unattended.conf.example` declares AND
  the leg's initialiser block initialises, minus the keys between the bare `gov:conf-allow-begin`
  and `gov:conf-allow-end` sentinels, must be empty. One direction only. Two `fail 22` branches: a
  missing, repeated or empty sentinel region, and a non-empty difference naming each key. The
  comment recording the join as withdrawn is replaced. Observed by AC4.
- **S4** Check 26 gains a flag arm. The parser population is every `--<name>` token on a
  non-comment line inside a new bare sentinel pair, `gov:argv-begin` and `gov:argv-end`, around the
  driver's top-level argument loop, sub-loops included, PLUS every member of `VERBS_SLUG` and
  `VERBS_INLINE`, read from their declarations, because a slug verb is recognised by set membership
  and never appears as a token inside the loop (§8 F5). The documented population is every
  `--<name>` token on the driver header's `#   unattended.sh` lines. A documented flag with no parser
  token fails 26, and so does a parser flag the header never names. Observed by AC5, AC6, AC7 and
  AC12.
- **S5** The driver header documents every flag the parser accepts. At BASE seven are parsed and
  undocumented — `--code`, `--framed`, `--playbook-sha`, `--records-root`, `--run`, `--set` and
  `--waive` — and `--framed` goes on the `--plan` header line beside `[--paths]`; any flag an earlier
  unit of this build added is graded the same way at this unit's commit. Observed by AC7 and AC12.
- **S6** Every argument a parser accepts appears in an arm. Check 26's flag arm also requires each
  driver parser flag on a non-comment line of `unattended.test.sh`, and each argument the leg's own
  scope parser accepts — every `--<name>` token on a non-comment line between the same bare pair,
  `gov:argv-begin` and `gov:argv-end`, placed around the `case "${1:-}"` block in
  `tools/unattended/check-unattended.sh` (`:85-90` at BASE) and extracted by the same exact-line
  match — on a non-comment line of `check-unattended.test.sh`. Where a suite is not installed, which
  is every adopter tree, the arm prints one announced skip naming the suite on the REPORT channel.
  The four arms missing at BASE are added: a `--version` smoke arm and a `--framed` arm in
  `unattended.test.sh`, and `--only 28` and `--skip 28` runs of the leg in
  `check-unattended.test.sh`. Observed by AC8 and AC13.
- **S7** Every new `fail` branch has an arm in `check-unattended.test.sh`, and `ARMS_FLOORS` in
  `.memory-tree.conf` moves in the same commit. The unattended suites run once under unit 1's
  attribution at VERIFYING, after the last unit, and they are on no bar leg; D12-i8's in-pass
  lift is parked (§9). Observed by AC9.
- **S8** The check 31 comment that justifies `${core:-}` and `${M:-}` by the crash this unit fixes
  is rewritten to say they are now belt and braces. Observed by AC10. NOT OBSERVED for the version:
  the unattended kit moves once in this build's landing range, in `TOOL-dDerivedDocket-1`, and this
  unit's bytes ride that move; `kit version markers` grades only the final tree's agreement.
- **S9** The kickoff manifest's `last-audit` is re-stamped in the same commit, with a delta line in
  the commit message, because `.memory-tree.conf` is in its `watch:` list and the staged leg refuses
  a watched change without one. The §B claims that file feeds are re-read first; only the
  `ARMS_FLOORS` figure moves, and no §B claim states that figure. That re-stamp is NOT a trim
  and claims nothing from the manifest's headroom: rewriting the `last-audit:` line at
  `memory/guides/SESSION-KICKOFF.md:5` is the bookkeeping every unit touching a watched file
  owes, a timestamp and a sha replaced in place by a timestamp and a sha. Another unit of this
  build rewrites the same line for the same reason, and that is NOT a collision. This unit
  writes no other byte of the file, so it displaces nothing and funds nothing, and AC14 reads
  the carrier only to catch a stamp written as an added line. Observed by AC11 and AC14.

## 3. Non-goals (OUT)

- Check 23 stays report-only. It prints and does not fail at BASE, and turning the class into a
  gate is not in DR's scope for this unit.
- Check 23 recognising an ABSORB commit as a sanctioned out-of-set write is the inherited-red
  unit's work (DR 22.1, D12-i5), in the same block.
- No scoping of the leg to an arbitrary check. Checks 1 to 27 still share state, and the header's
  statement of that stays true.
- The reverse direction of the allow-list join. A key read through a default expansion, as
  `UNITS_REGION_CUTOFF` is at BASE, is initialised nowhere, so the reverse reds a correct tree.
- The verb carrier and the Skill do not join flags. They describe verbs, and at BASE most flags
  appear in neither, so a join there would red the tree for no finding a reader acts on.
- The unarmed branches already pinned in `memory/project/unarmed-branches.txt` stay pinned.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-1` — `run-unattended-gates.sh --attribute`, whose attributed
  verdict, `verdict clean` with every inherited suite filed, is the only criterion the unattended
  suites can meet, since they are red at BASE for causes this unit does not own. Added by this spec;
  the brief's table does not list it.

## 4. Design

### Check 23 — what the three conditions buy

The subset test at `tools/unattended/check-unattended.sh:2407-2426` compares every path the pass
commit touched against the declared set. The driver's `--brief` verb STAGES the brief it records, so
the pass commit carries it without the pass ever having written it. Measured on the real tree with
`--skip 28` on 2026-09-14 at `abac6d59`: 29 check 23 lines across two builds, every one naming a
`prompts/` path, and five of them naming nothing else. PINNED as that measurement; the arm's own
fixture is what re-derives the behaviour.

What BASE already does, from `TOOL-aRatifiedRulings-2`: `read_brief_paths` at
`tools/unattended/lib-unattended.sh:132-141` prints, normalised, every path a
`brief · item <unit> · reason` row names in the run-state file AT a given commit; check 23 drops
those exact paths from the subset test and announces each through `report`; and `pass_commit`
subtracts the same set at `tools/unattended/lib-unattended.sh:207`, so a `{run-state, brief}`
bookkeeping commit is skipped rather than graded clean. Its arms A to F in
`tools/unattended/check-unattended.test.sh` cover a matching row, a stray file beside the brief, a
row appended after the commit, a row naming a directory, a `./` spelling, and the bookkeeping
commit. Its own check 23 comment says what it does not buy: a row naming a path no brief was handed
at is excused and joined by nothing.

Each condition closes a distinct over-exemption. Without the unit match, which BASE has, a pass
could commit a sibling unit's brief unreported. Without the directory condition, a row could name
any path and excuse it. Without the blob prefix, a pass that EDITED its brief after `--brief` hashed
it would have that edit excused, which is the write the declare-before-dispatch rule exists to see.
The blob comes from `git rev-parse <commit>:<P>`, read through the pinned `GIT` wrapper like every
other dereference in the leg, and compared with `<h12>` as a 12-character prefix. Both new conditions
go inside `read_brief_paths`, because its two consumers must excuse one set: narrowed in check 23
alone, `pass_commit` would still skip a commit carrying an edited brief as bookkeeping, and the
commit that edited it would never be the one graded.

### The hoist, and the announced skip

The import at `:147-199` and its initialiser block at `:116-121` sit inside
`if [ "$SCOPE" != only28 ]` at `:110`. Check 30 reads `$MEMORY_ROOT` at `:3293`, outside both scope
guards, so `--only 28` dies there with `set -u`. Measured on the real tree at `abac6d59` on
2026-09-14: exit 1, `line 3224: MEMORY_ROOT: unbound variable`; at BASE the guard, the initialisers
and the import are byte-identical and check 30's read has moved to `:3293`, so the crash stands. Moving the conf presence test, the initialisers,
the subshell import and its sentinel test above the guard costs nothing on either scope: the import
is one subshell and it ran on every unscoped run already.

Under `--only 28` the checks after the 28 region are skipped because the flag's contract is "the 28
region alone", not because they would crash. Each prints
`check <n> skipped under --only 28 — this run asked for the 28 region alone` through `report`, the
channel `GOV_UNATTENDED_REPORT=1` turns on. That keeps the leg's header contract, exit 0 with no
output on a clean tree, true under both scopes. The numbers come from the `# ---- check <n>`
headers after the region's closing guard, so a check added later is skipped and announced without
anyone editing a list.

### Check 22's join

The sentinel region is extracted by an exact-line match on the two bare sentinels, and a region that
is absent, doubled or yields no key fails 22 by name. That refusal is the join's liveness: a region
that reads as empty would otherwise pass every key. The difference is computed with `comm` over three
sorted sets, in the idiom check 22's existing table join already uses at `:1701-1703`. The exact-line
match is what avoids the recorded first-draft trap, an anchored range whose pattern the extractor's
own source line matched, which read 38 keys instead of 20.

Re-measured at BASE: 36 keys in the example, 20 initialised, 20 in the allow-list, and the difference
is empty. The three example keys `abac6d59` lacked, `REVIEW_ROUNDS`, `SPEC_TOKENS_CLI` and
`UNIT_STALL_BOUND`, came with aProbedUnit and aDeferredBar and are initialised by no line of the leg,
so the one-direction join does not read them. Units of this build ordered before this one add conf keys, and this join grades every one
of them the moment it lands; a key one of them forgot to admit is fixed in this unit's commit.

### Check 26's flag arm

At BASE the driver's argument loop starts at `tools/unattended/unattended.sh:5215`, and the header
usage lines are `:5-23`. Measured at BASE on 2026-09-16 with the population rule of S4, distinct
tokens counted, PINNED as that measurement:

- tokens `--<name>` on non-comment lines of the argument loop (`:5215` `while [ $# -gt 0 ]; do` to
  `:5313` `done`): 30; members of `VERBS_SLUG` and `VERBS_INLINE` (`:88-91`): 19; union: 45.
  Header `#   unattended.sh` lines (`:5-23`): 38 tokens.
- loop tokens alone against the header: 15 header tokens have no loop token — `--abort`,
  `--attest`, `--audit`, `--brief`, `--close`, `--dispatch`, `--landed`, `--park`, `--preflight`,
  `--propose`, `--record-piece`, `--record-set`, `--rescope`, `--resume` and `--status`, every slug
  verb but `--review` — because they dispatch by `VERBS_SLUG` membership through `is_slug_verb`
  (`:93`) in the loop's catch-all arm.
- the union against the header: no header token is missing; 7 parser tokens are undocumented —
  `--code`, `--framed`, `--playbook-sha`, `--records-root`, `--run`, `--set` and `--waive`.
- suite halves: `--framed` and `--version` appear on no non-comment line of `unattended.test.sh`;
  `--only` and `--skip` appear on no non-comment line of `check-unattended.test.sh`.

At `abac6d59` the same probe read 30, 18, 44 and 37 over `:4936-5034` and `:5-22`, with 14 header
tokens missing from the loop. The one difference is `--audit`, which `TOOL-aProbedUnit-3` added as a
slug verb with its own header line and suite arms, so it changes no finding.

```bash
awk 'NR>=5215 && NR<=5313 && $0 !~ /^[[:space:]]*#/' tools/unattended/unattended.sh | grep -oE -- '--[a-z][a-z0-9-]*' | sort -u
grep -E '^VERBS_(SLUG|INLINE)=' tools/unattended/unattended.sh | grep -oE -- '--[a-z][a-z0-9-]*' | sort -u
awk 'NR>=5 && NR<=23' tools/unattended/unattended.sh | grep -E '^#   unattended\.sh' | grep -oE -- '--[a-z][a-z0-9-]*' | sort -u
```

The line numbers are BASE's; after S4 the loop is read between its sentinels. Every one of the seven
is a real argument of a documented verb. S5 adds each to its verb's header line, which also puts it
in the rendered usage text. `--witness`, `--paths` and `--framed` are parsed inside the `--phase` and
`--plan` arms rather than as case labels, which is why the population is tokens in the fenced region
and not case labels alone.

The suite half measures `--version` and `--framed` as the two driver flags no non-comment line of
`unattended.test.sh` names, and `--only` and `--skip` as the two leg flags no non-comment line of
`check-unattended.test.sh` names; all four are added. The arm grades PRESENCE on a non-comment line
and says so in its header: it cannot tell an arm that asserts something about a flag from one that
merely passes it.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `gov:argv-begin`, `gov:argv-end` | bare sentinel comments in the driver AND in the leg, around each file's own argument parser | none; bare so no extractor line can match them |
| new `fail 22` and `fail 26` branches | leg refusals | `harness arms` population; each is armed or the floor does not move |
| any new shell helper | shell function | lexicon `sh` function cell; each name passes `python tools/lexicon/lexicon.py --suggest <name>` before it is written |

### Files touched (estimate)

`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/lib-unattended.sh` (`read_brief_paths`) ·
`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `.memory-tree.conf`
(`ARMS_FLOORS`) · `memory/guides/SESSION-KICKOFF.md` (the stamp) · `memory/map/features/unattended.md`
prose.

### Alternatives rejected

- **`${MEMORY_ROOT:-}` at check 30.** Costed in `TOOL-aHoistedPass-37`: it trades the crash for a
  silent skip of check 30's corpus walk, which removes the liveness assertion that check exists for.
- **Exempting all of `prompts/` in check 23.** DR names it as the break: a sibling's brief and an
  edited brief would both vanish.
- **Pinning the two check-22 branches as unarmed.** `TOOL-aHoistedPass-40` weighed it and the drift
  audit already reports that registry as not shrinking; this unit may run the suite, so the reason
  that forced the pin is gone.
- **Joining flags to the verb carrier.** Rejected in §3.

## 5. Production-readiness checklist

- security — the leg reads more of the driver and its suites and writes nothing. The hoist moves the
  subshell import unchanged, so a hostile conf still cannot end or take over the leg.
- perf / scale — one extra read of the driver and of two suites per run; `--only 28` becomes usable,
  which is the saving the flag was written for.
- error / empty / loading states — an absent sentinel region fails by name, an absent suite is an
  announced skip, and a brief row with a malformed hash does not cover anything.
- observability — the per-check skip lines under `--only 28`, the covered-brief report line, and the
  key and flag names in every new refusal.
- risks — the header gains seven flags, which changes the rendered usage text; nothing parses that
  text except check 26 itself.
- testing — arms in `tools/unattended/check-unattended.test.sh` for each new branch and each staged
  break in §6, run once under `--attribute` after the last unit, at VERIFYING.
- migration — adopters receive the hoist and the new arms with their next kit upgrade, and the suite
  half skips in their trees because the suites are withheld from them.
- user docs — the header lines are the usage text; the leg's own block comments are the rest.

## 6. Acceptance criteria

- **AC1** — When a fixture pass commit carries its own unit's brief under `prompts/` and a matching
  `brief · item` row, check 23 in `tools/unattended/check-unattended.test.sh` prints no line for it;
  when the brief was edited after hashing, when the row names a sibling unit, or when the row names a
  path outside the build's own `prompts/`, the line is printed; and a commit touching only the
  run-state file and an edited brief is not skipped by `pass_commit` as bookkeeping.
  Red when: the blob prefix or the directory is not compared, so an edited brief or a row naming a
  product file goes unreported as it does at BASE; or the two conditions narrow check 23 alone, so
  `pass_commit` skips the commit that edited the brief and check 23 never grades it.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC2** — When `bash tools/unattended/check-unattended.sh --skip 28` runs on the real tree, no
  check 23 line names a brief whose row, directory and blob all match.
  Red when: the blob is read from the working tree instead of the pass commit, so a brief edited
  and committed later still matches.
  figure: the 29 lines and the five brief-only ones in §4 are PINNED 2026-09-14 at `abac6d59`,
  before the landed exclusion; this criterion states the property, not a count.
  permission: this is the `unattended kit gate` leg's own command over the REAL tree, so under
  rule 1's narrow reading it DEFERS to the run at VERIFYING rather than running in this pass;
  the same command over a fixture would stay in the pass.
- **AC3** — When `GOV_UNATTENDED_REPORT=1 bash tools/unattended/check-unattended.sh --only 28` runs
  on the real tree, it exits 0 and prints one skip line each for checks 30 and 31; without the
  variable it exits 0 and prints nothing.
  Red when: the conf read stays inside the guard, and the run exits 1 on
  `MEMORY_ROOT: unbound variable`.
  permission: this is the `unattended kit gate` leg's own command over the REAL tree, so under
  rule 1's narrow reading it DEFERS to the run at VERIFYING rather than running in this pass;
  the same command over a fixture would stay in the pass.
- **AC4** — When a fixture copy of the leg removes one key from between the `gov:conf-allow`
  sentinels, the leg fails 22 naming that key; with one sentinel deleted, it fails 22 naming the
  region.
  Red when: the region is extracted by a pattern the extractor's own source line matches, which
  reads keys from outside the list and hides the removal.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC5** — When a fixture copy of the driver documents `--frobnicate` on a header line with no parser
  token, the leg fails 26 naming `--frobnicate`.
  Red when: the flag arm reads only case labels, so a documented flag parsed nowhere is not missed.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC6** — When a fixture copy of the driver adds a parser arm `--frobnicate)` that no header line
  names, the leg fails 26 naming it.
  Red when: the arm joins one direction only, and an undocumented flag reaches no reader.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC7** — When `bash tools/unattended/check-unattended.sh` runs on the real tree after this unit,
  the flag arm passes with every parser flag, the seven §4 names included, on its verb's header line,
  and with every slug verb found through `VERBS_SLUG`.
  Red when: the header is left as at BASE, which the new arm reds seven times, or the population
  reads the loop alone, which reds fifteen documented slug verbs.
  permission: this is the `unattended kit gate` leg's own command over the REAL tree, so under
  rule 1's narrow reading it DEFERS to the run at VERIFYING rather than running in this pass;
  the same command over a fixture would stay in the pass.
- **AC8** — When a fixture copy of `unattended.test.sh` drops every line naming `--version`, the leg
  fails 26 naming it; with the suite absent, the leg's REPORT channel carries one skip line naming
  the suite and the exit status is the other checks' verdict; and when a fixture copy of
  `unattended.test.sh` drops every line naming `--framed`, the leg fails 26 naming it.
  Red when: an absent suite is read as an empty one and reds every flag in an adopter tree.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC9** — When `bash tools/unattended/run-unattended-gates.sh --attribute <BASE>` runs once after
  the last unit, at VERIFYING, its attribution summary reads `verdict clean`, meaning no NEW FAIL,
  no `DEAD PROBE at L` and no `OVER BUDGET at L`. Every suite it reports with INHERITED lines or
  `DEAD PROBE at R` is named by its file path in a filed backlog row or ask that is not CLOSED, as
  `git grep -n '<suite file>' -- memory/backlog 'memory/builds/*/BACKLOG.md'` shows. And
  `python3 tools/memory-tree/check-arms.py --check` passes with the moved `ARMS_FLOORS` row.
  Red when: a new branch ships with no arm, so the harness arms leg reds on the floor; or an arm this
  unit added fails, or an existing arm newly fails because of it; or the attributed run is read by
  its NEW count alone, so a suite this unit's change aborted before its first FAIL line, or pushed
  past its budget, reads as clean; or an inherited failure is attributed away with no record filing
  it.
  cost: the unattended suites' declared budgets, once, with the BASE side cached.
  permission: the unattended suites are on no bar leg; they run at VERIFYING, after the last unit,
  not at this unit's end (D12-i8's in-pass lift is parked, §9). The
  `python3 tools/memory-tree/check-arms.py --check` half is a read-only verb and stays an in-pass
  observation.
- **AC10** — When `grep -n 'belt and braces' tools/unattended/check-unattended.sh` runs after this
  unit, the check 31 comment names `${core:-}` and `${M:-}` as belt and braces and no longer gives
  the `--only 28` crash as their reason.
  Red when: the comment still justifies them by a crash that no longer happens, so a reader keeps
  two guards for a reason that is false.
- **AC11** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes with the re-stamped `last-audit`.
  Red when: the conf moves with no re-stamp, which the staged leg refuses at the commit.
  permission: the command is the `kickoff-manifest ratchet` leg; it runs at the build's one
  post-build bar.
- **AC12** — When a fixture copy of the driver keeps a slug verb's header line but drops the verb
  from `VERBS_SLUG`, the leg fails 26 naming it; with the verb restored to the set and no case label
  anywhere, the leg passes.
  Red when: the parser population is the loop's case labels alone, so a verb the set dispatches
  reads as undocumented-parser or missing-parser by accident.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC13** — When a fixture copy of `check-unattended.test.sh` drops every line naming `--skip`, the
  leg fails 26 naming `--skip`; with the leg's `gov:argv-begin` sentinel deleted, it fails 26 naming
  the region.
  Red when: the leg half has no fenced population, so an implementation grading only the driver half
  passes every other criterion.
  permission: the leg suite is on no bar leg; it runs at VERIFYING, after the last unit, through
  `bash tools/unattended/run-unattended-gates.sh`, not at this unit's end (D12-i8's in-pass lift
  is parked, §9).
- **AC14** — When `wc -c < memory/guides/SESSION-KICKOFF.md` is read at this unit's commit and at
  its parent, the reading at this unit's commit is NO LARGER than the reading at the parent, and
  `git diff --numstat` over `memory/guides/SESSION-KICKOFF.md` between those same two commits,
  resolved by sha rather than by `HEAD^ HEAD`, reports one line added and one removed; where a
  pass lands more than one commit the pair is the stamp commit and its parent, so a fix-up
  landing after the stamp does not red a stamp that landed correctly.
  Red when: the re-stamp is written as an extra line rather than in place, or any other §B claim
  is edited here, so a carrier other units of this build write too grows on a unit whose whole edit
  is a stamp. The cap half is red by the `memory hygiene` leg's index-cap check; the NET delta
  against the parent is the half no leg reads, which is why this criterion reads it.
  permission: both readings are `wc -c` and `git diff` over tracked files in the pass. NO CAP IS
  RAISED by this unit: moving the 61440 is an owner turn.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `shell hygiene (a loop fed by a command substitution)` · `lexicon naming predicates` · `line length` · `codebase-map coverage + freshness` · `kickoff-manifest ratchet` · `memory hygiene`

New arm: `tools/unattended/check-unattended.test.sh` · an edited brief, a sibling's brief, and a matching brief in a fixture pass commit · the check-unattended arms floor and the leg suite's executed-assertion floor
New arm: `tools/unattended/check-unattended.test.sh` · a removed allow-list key, a deleted sentinel, a documented flag with no parser token, a parser flag with no header line, a suite missing `--version` · the check-unattended arms floor and the leg suite's executed-assertion floor
New arm: `tools/unattended/check-unattended.test.sh` · the leg run with `--only 28` · the leg suite's executed-assertion floor
New arm: `tools/unattended/unattended.test.sh` · the driver run with `--version` · the driver suite's executed-assertion floor
New arm: `tools/unattended/unattended.test.sh` · the driver run with `--plan --framed` · the driver suite's executed-assertion floor
New arm: `tools/unattended/check-unattended.test.sh` · the leg run with `--skip 28` · the leg suite's executed-assertion floor

## 8. Open questions

- **F1** — Which direction does the flag join grade? Options: (a) documented to parser, DR's third
  criterion; (b) both. (b) reds seven flags at BASE, which S5 documents in the same commit.
  RESOLVED (agent, 2026-09-14, delegated): (b). It satisfies DR's criterion and also catches the
  flag nobody can read about, at the cost of seven header edits.
- **F2** — Where does the suite-arm class gate live? Options: (a) inside each suite, asserting its own
  coverage; (b) in the leg's check 26, with an announced skip where a suite is absent. (a) runs only
  when the suite runs, and the unattended suites are on no bar, so it would be a gate nobody runs.
  RESOLVED (agent, 2026-09-14, delegated): (b).
- **F3** — One skip line, or one per check, under `--only 28`? RESOLVED (agent, 2026-09-14,
  delegated): one per check, derived from the check headers, because a skip whose subject is a set
  cannot say which check it was about; check 31's header states the same rule.
- **F4** — Does check 23's exemption read the brief's blob from the working tree or from the pass
  commit? RESOLVED (agent, 2026-09-14, delegated): from the pass commit, since the question is what
  that commit wrote.
- **F5 — how does the flag arm see verbs dispatched by set membership?** Options: (a) the parser
  population includes the `VERBS_SLUG` and `VERBS_INLINE` members, read from their declarations; (b) a
  second fence around the post-loop `case "$VERB"` dispatch. The driver states that the set is the
  dispatch, and check 26's verb join already reads it. RESOLVED (agent, 2026-09-14, delegated): (a).

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft. Adds one edge the brief's table does not list,
  consumes-from unit 1, for the attributed suite run.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H6, M23, M7; G1 M11). H6: S4's parser
  population adds the `VERBS_SLUG` and `VERBS_INLINE` members (F5, AC12); seven flags are
  undocumented at BASE, not six, `--framed` among them, and the probe and its BASE output, re-run by
  the fold, are in §4 (S5, AC7, and F1's count); `--framed` and `--skip` gain arms (S6, AC8). M23:
  S6 fences the leg's own scope parser with the same sentinel pair (AC13). M7 with G1 M11: S8's
  version half is a pointer to unit 1 under the build's one-owner rule, and AC10 now observes the
  check 31 comment S8 rewrites.
- rev-3 · 2026-09-16 · spec-audit round 2 fold, second pass. Plan c1 E41, G1 H1 (2, 24), a sibling
  fold from the G1 round-2 record: §6 AC9 reads unit 1's `verdict clean` and the inherited-suite
  filing, and the §3 consumes-from edge to unit 1 is updated. Fold verification: §6 AC3's `Red when:`
  code span, which opened on one line and closed on the next, is reflowed onto one line; the words
  are unchanged. Third pass, from the fold-2 verifier problem that §6 AC9's `Red when:` carried only
  the shorter consumer clause: AC9 now also reds when an arm this unit added fails or an existing arm
  newly fails, when a suite is pushed past its budget, and when an inherited failure is attributed
  away with no record filing it, so each positive clause of unit 1 S10's criterion has a red, as
  units 16, 17 and 18 state them.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). `TOOL-aRatifiedRulings-2` (merge
  b6bbfa7b, fix 71893b91) built `TOOL-aLeakedHandle-7` as an exact-path, same-unit, pass-commit
  exclusion in `read_brief_paths`, shared by check 23 and `pass_commit`: §1 and §2 S1 point at it and
  keep the directory and blob-prefix conditions as the remainder, applied inside that function; §4's
  check 23 section says what landed; §6 AC1 now stages the two remaining conditions and the selector
  half; Files touched gains `tools/unattended/lib-unattended.sh`. Line citations moved: the subset
  test to `:2407-2426`, check 30's read to `:3293`, check 22's `comm` join to `:1701-1703`, check 26
  to `:2542-2601`, the driver loop to `:5215-5313`, its header to `:5-23`, the verb sets to `:88-91`
  and `is_slug_verb` to `:93`. `TOOL-aProbedUnit-3`'s `--audit` re-measures §4's probe at 19, 45, 38
  and fifteen, and §6 AC7 reads fifteen; the seven undocumented flags and the four suite gaps are
  unchanged. §4's check 22 figure reads 36 example keys, the difference still empty. §10's BASE
  paragraph records the gate-guard conflict with D12-i8, reported rather than decided.
  Extended 2026-09-20, same base, by the build-wide consolidation pass. That conflict is now FOLDED
  on its conservative reading, and still not decided: §2 S7, §5 testing and §6 AC9 move the
  attributed suite run from this unit's end to the run made at VERIFYING, after the last unit, and
  AC9's `permission:` line names the parked lift rather than claiming it, while
  its `python3 tools/memory-tree/check-arms.py --check` half stays in the pass because a read-only
  verb is admitted. Every other criterion whose observation is the leg suite or the
  `unattended kit gate` leg's own argv gained the same kind of line, so §6 is consistent with
  itself; the leg SUITE is on NO bar leg, because its `*.test.sh` row left
  `tools/gate-legs.json`, while the leg itself is a bar leg and defers to the post-build bar; AC10 reads a tracked file with `grep` and keeps its in-pass observation, and AC11's
  command is the `kickoff-manifest ratchet` leg's argv and defers. §7's four `· none` `New arm:`
  third fields are replaced: `tools/unattended/unattended.test.sh` and
  `tools/unattended/check-unattended.test.sh` each pin an executed-assertion floor, so `none` never
  described them; the two rows naming an arms floor keep that figure, which an arm covering a new
  branch also moves, and now name the executed-assertion floor beside it, because one arm raises
  both and `ARMS_FLOORS` alone would leave the suite's own pin slack. The
  four suite-half claims of §4 were re-run at HEAD and hold: `--version` and `--framed` occur on no
  non-comment line of the driver suite, and `--only` and `--skip` on none of the leg suite's. The
  one capped carrier this unit writes is `memory/guides/SESSION-KICKOFF.md`, 20057 bytes against
  the 61440 its class declares, and S9 only re-stamps it.
  Extended again 2026-09-20, same base, by the closing consolidation pass, which applied the
  build's NET-ZERO rule to every capped carrier rather than only to the contested ones. §2 S9 now
  NAMES its passage, the `last-audit:` line at `memory/guides/SESSION-KICKOFF.md:5`, records that
  a stamp displaces no text, and new §6 AC14 reads the carrier at this unit's commit against its
  PARENT and reds any growth, with a `git diff --numstat` half that reds a stamp written as an
  added line. Naming the line is what lets the orchestrator see that no sibling unit trims the
  same one: inside this closing set the passages taken are the §B `TMPDIR` trap, the ceiling
  line, the §B M6 claim and this stamp. A stamp is not a contested passage at all — every unit
  touching a watched path rewrites it, the passes are ordered, and each leaves the file the same
  size. The header date moves to the last-change date; the rev does not.
  Closed 2026-09-20, same base, by the last consolidation pass before the spec audits re-run.
  §2 S9 STOPS CALLING THE MANIFEST RE-STAMP A TRIM, on the orchestrator's ruling: rewriting the
  `last-audit:` line at `memory/guides/SESSION-KICKOFF.md:5` is the bookkeeping every unit
  touching a watched file owes, it claims nothing from that carrier's headroom, and a sibling
  unit rewriting the same line is NOT a collision. S9 now says that in those terms, and AC14's
  job is narrowed in words to catching a stamp written as an added line rather than funding
  anything. Rule 1's NARROW reading is ratified and applied: AC2, AC3 and AC7 run the
  `unattended kit gate` leg's own command over the REAL tree, so they keep deferring to the run
  at VERIFYING and now SAY that is why, while the fixture-copy criteria keep deferring for the
  different reason that they observe through a `*.test.sh` file invocation with no read-only
  verb. One verifier finding is repaired rather than carried: AC14's second half read
  `git diff --numstat HEAD^ HEAD`, which reds a correctly landed stamp whenever a pass lands more
  than one commit; it now resolves the stamp commit and its parent by sha and says so. One §7
  `New arm:` third field spelled the arms floor as a backticked conf key while the row above it
  spelled the same floor in words; both now read the same way, so no field of this spec carries
  a bare identifier. The header date stays at the last-change date; the rev does not move.

## 10. Reuse audit

Every seam is in the leg or its driver. The subshell conf import and its bare sentinel pair already
exist at `tools/unattended/check-unattended.sh:147-199`; S3 reads the pair it was fenced for, and S4
copies that fence for the argument loop. Check 22's `comm` join at `:1701-1703` is the idiom for S3.
Check 26's verb join at `:2542-2601`, which reads each carrier once into memory, is the loop S4
extends. `read_brief_paths` at `tools/unattended/lib-unattended.sh:132-141`, with its two consumers,
is where S1's remainder goes. Check 31's one-announced-skip-per-subject pattern is S2's and S6's. The driver's
`--brief` row grammar, `brief · item <unit> · reason <h12> <path>` from `verb_brief`, is what S1
matches, exactly as written. `python tools/codebase-map/reuse_lookup.py "join every flag a
command-line parser accepts against its documented usage and its test arms"` returned only
Python parser neighbours such as `parse_args` in `tools/govkit/govkit.py`, and reports `.sh` as an
unscanned layer; no existing seam joins a shell parser's flags to anything. Recall returned
`TOOL-aHoistedPass-37` and `TOOL-aHoistedPass-40`, which carry the costed options for S2 and S3, and
the owner ruling `TOOL-aLeakedHandle-7`, which S1 executes.

Where DR, the records and the source disagree at BASE: DR cites check 23 at `:2347-2357` of
`abac6d59`, where the subset test spanned `:2344-2357`; at BASE it spans `:2407-2426`. The owner
ruling excludes "the path a brief row names", and DR narrows that with three conditions. The landed
build of the ruling applies the unit condition only. S1 follows DR, because each case the narrowing
removes, an edited brief or a path no brief was handed at, is one the ruling's own reason does not
reach: in both, the committed bytes are not what `--brief` staged for this pass. `TOOL-aHoistedPass-40` names the two check-22 branches only by shape, so S3
defines them.

BASE is `fb07ca25`, origin/main 210 commits past the `abac6d59` this spec was first audited at. Of
the three defects, check 23's is half closed by aRatifiedRulings, as S1 records; `--only 28` still
dies at check 30; the allow-list is still unjoined, and `TOOL-aHoistedPass-37` and
`TOOL-aHoistedPass-40` are both still OPEN. aDeferredBar added `tools/unattended/gate-guard.js`,
which denies `run-unattended-gates.sh` and every `.test.sh` in a run phase before VERIFYING, and
aProbedUnit's child prompt orders no suite inside a unit pass. §2 S7 and §6 AC9 run the unattended
suites once at this unit's end under D12-i8's lift, which predates both; that conflict is reported to
the orchestrator and is not decided here.

Recall terms used: `check-unattended conf-allow sentinel allow-list check 22 only28 MEMORY_ROOT
unbound check 23 brief prompts dispatch`
