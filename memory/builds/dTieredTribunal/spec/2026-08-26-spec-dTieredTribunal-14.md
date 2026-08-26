# TOOL-dTieredTribunal-14 — the ref-keyed-join ban reaches an inline script

**Status:** SPECCED · rev-3 · 2026-08-26 · node a · Tier-2 · base cd971285 · order 3 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round1.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-15 |
| [2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md](../reviews/2026-08-26-review-TOOL-dTieredTribunal-11-spec-audit-round2.md) | spec-audit | TOOL-dTieredTribunal-11 TOOL-dTieredTribunal-12 TOOL-dTieredTribunal-13 TOOL-dTieredTribunal-15 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/check-review-join.sh` bans a ref-keyed verdict join over every `*.js` under
`tools/`, and it cannot see the modality where that defect actually happens. An ad-hoc review harness
is an inline `script` string on a `Workflow` tool call and is never a file. Lift the gate's awk
predicate into `tools/hooks/agent-cap.js`, the one enforcement point that reads that string, and make
the file gate delegate to it rather than keeping a second implementation. Owner ruling
`TOOL-dTieredTribunal-8` authorizes this and sequences it after `TOOL-dTieredTribunal-13`, so the
marked-derivation hole in the hook is closed before another rule is added to that file.

The gap was reproduced at HEAD `96f11c0e` rather than taken from the research record. A cap-compliant
inline harness carrying a ref-keyed join returns rc=0 from `node tools/hooks/agent-cap.js` and rc=1
from `bash tools/workflows/check-review-join.sh` on the identical bytes. Only the gate that cannot
see an inline script catches the defect.

## 2. Scope (IN)

- **S1** — `tools/hooks/agent-cap.js` gains a fifth rule: the three bans the gate's awk implements,
  ported verbatim in MEANING. A new `scanJoinFindings(script)` returns the same `{n, line, why}`
  shape `fanoutFindings` and `capFindings` already return, so the existing message formatter in
  `main()` carries it with no new plumbing. The three bans and their `why` strings are pinned in
  section 4 Data model, because the gate's self-test asserts those exact strings and this port must
  not change one byte of them.
- **S2** — the predicate reads `blankLiterals(script)`, the literal-blanked view already defined at
  `tools/hooks/agent-cap.js:372`, rather than a second character scanner. That is a measured
  behaviour change and section 4 Migration states exactly what it changes and what it does not.
- **S3** — the new rule is the LAST script rule in `main()`, and reaching it requires INVERTING the
  `offendingLines` block that begins at `tools/hooks/agent-cap.js:821`. That block alone is written
  as an early exit — `:822` is `if (bad.length === 0) process.exit(0)` — so a rule merely appended
  after it never runs for a script carrying no raw `parallel(`/`pipeline(`, which is every script the
  join ban exists to judge. It becomes `if (bad.length) { <the existing message>; process.exit(2) }`
  with a single `process.exit(0)` moved to the end of `main()` after `scanJoinFindings`. The two
  rules above it, `fan` at `:786` and `caps` at `:806`, already use that additive shape and are
  untouched. The three rules above it all prevent a BURST, which is the expensive failure this hook
  exists for; a ref-keyed join is a wrong verdict, which is cheap to re-run. `main()` still exits on
  the first rule that fires, so the order decides which message an operator sees and nothing else.
  **The inversion also reaches a file this unit does not otherwise edit, and that is DISCLOSED here
  rather than left to be discovered.** `tools/workflows/check-verifier-fanout.sh:72-77` pipes each
  harness to `node "$HOOK"` with no `--only` flag, so once the early exit is gone that gate enforces
  the S1 join ban too and stops being a one-rule gate. No verdict moves: its population is a SUBSET of
  the join gate's, and section 4 measured zero live hits over the wider set. What it costs instead is
  a merge-bar leg whose own header describes a gate it no longer is, which is a structural check
  reading as a semantic one — the class the charter names. Two lines carry that false description, the
  subject line at `:2` and the exit legend at `:7`. Section 3 therefore carves exactly those two out
  of its own Non-goal, AC15 grades the corrected pair, and section 9 rev-3 records the amendment.
  A silent widening was the alternative and it is refused.
- **S4** — the hook gains an `--only=<rule>` argv selector over a CLOSED set whose only member today
  is `join`. Absent, every rule runs, which is the wiring's invocation and is unchanged. Present and
  equal to `join`, only the S1 rule runs. Present and anything else, the hook REFUSES with exit 2 and
  a message naming the closed set. A selector that silently matched nothing would be this repo's own
  vacuous-selector-empty-population class, arriving in the file whose job is to refuse what it cannot
  resolve.
- **S5** — `tools/workflows/check-review-join.sh` deletes its awk block at `:72-92`, the ban-list
  comment at `:53-59` and the stripper note at `:67-71`, and delegates. Those two comment paragraphs
  describe the awk's own `//`-tail rule and its string-surviving behaviour, both of which S2 removes,
  so they are replaced by one short comment naming the hook's `blankLiterals` as the stripper and
  section 4 Migration as the record of the narrowing; the three ban descriptions now live in the
  hook's own rule, where section 4 Data model pins them. The `SCAN` build and its
  `none of the named files exist` refusal at `:60-65` are KEPT.
  The payload is built by node, copied from the shape at `tools/workflows/check-verifier-fanout.sh:72-77`,
  and the invocation is `node "$HOOK" --only=join`. Everything else about that gate is KEPT: the
  population selector at `:43-44`, which takes every `tools/**/*.js` with no `export const meta =`
  filter, both explicit-path and discovery modes, exit 1 for a ban and exit 2 for misconfiguration,
  and all three of its own refusal messages. The gate also keeps a missing-hook and a missing-node
  refusal, matching `tools/workflows/check-verifier-fanout.sh:24-25`, because a gate whose predicate
  is absent must say so rather than pass.
- **S6** — `SELF_EXCLUDE` at `tools/workflows/check-review-join.sh:31` grows
  `^tools/hooks/agent-cap\.js$`. This is measured and not defensive. The hook is clean today, but S1
  puts the retired-identifier ban into it as a bare regex literal, a regex literal survives
  `blankLiterals`, and the candidate predicate run over a file holding that ban table returns one hit
  on exactly the table's own line. The gate's header already declares the doctrine and says
  `SELF_EXCLUDE` keeps it true if the predicate is ever written in JavaScript. After S1 it is.
- **S7** — `tools/check-wiring.sh` asserts that the WIRED `agent-cap.js` command carries no `--only`,
  in the `check_agentcap` arm at `:128-148`. `matchers_of` at `:64-71` extracts the matcher and
  discards the command, so the arm needs a command-text read beside it. A wired `--only=join` would
  turn off the three cap rules with no diff and a hook that still looks wired, which is the same
  class as the `AGENT_CAP` environment knob this file deleted and whose header records that it
  survived two releases by appearing to work.
- **S8** — the failing case is OBSERVED before this lands, as new arms in `tools/hooks/agent-cap.test.sh`,
  in that file's existing `js <name> <expected-exit>` heredoc style. The arms are enumerated in
  section 4 Inventory and include the two fixtures that pin S2's deliberate narrowing.
  `tools/workflows/check-review-join.test.sh` also gains `tools/hooks/agent-cap.js` copied into its
  `$TMP/discover` and `$TMP/emptyrepo` scratch repos, after `:133` and after `:163` — the arms at
  `:141`, `:153` and `:165` run the gate inside those repos, which hold no hook, so S5's missing-hook
  refusal fires there otherwise. **Those two lines are SPELLED below rather than pointed at.** The
  sibling's `tools/workflows/check-verifier-fanout.test.sh:63` resolves the hook through a `$HERE`
  that this file never binds, and this file sets `set -u` at `:14`, so lifting it as it stands aborts
  the WHOLE self-test in the main shell rather than failing one `cp`: run, it prints
  `E: unbound variable`, returns rc=1, and nothing after the line executes. Write instead, after
  `:133`:
  `mkdir -p "$D/tools/hooks" && cp "$ROOT/tools/hooks/agent-cap.js" "$D/tools/hooks/agent-cap.js"`,
  and after `:163` the same line with `$E` in place of `$D`. `ROOT` is this file's own repo-root
  resolver, bound and `cd`-ed to at `:15-16`, which is what `:17` already resolves the gate against.
  The scratch variable is
  per SITE and not shared: `E` is not bound until `:160`, so an `$E` spelling at the `:133` site is
  the abort above and not a typo.
  S6 is load-bearing for the second of those two lines, not merely defensive. The `$E` copy puts a
  `.js` into the one repo whose whole point is an EMPTY population; run at base without S6's
  `SELF_EXCLUDE` row that arm reds with `clean — no ref-keyed verdict join under tools/`, and with the
  row the population is empty again and the refusal fires. Both halves were run.
  This file also gains a third scratch repo holding no hook and one arm asserting S5's missing-hook
  refusal, copying the sibling's `:74-79` SHAPE, so the new refusal's own failing case is observed.
  That repo is NOT named `D`, which `:121` already binds to `$TMP/discover`; this unit spells it
  `N="$TMP/nohook"`. Run at base the arm reds with
  `review-join: no JavaScript under tools/ — the population is empty, which is not a pass`, because
  the refusal it asserts is the one S5 adds — which is the failing case, observed.
- **S9** — `.claude/hooks/agent-cap.js` is refreshed from the kit copy in the same commit. It is the
  WIRED copy, the parity arm at `tools/hooks/agent-cap.test.sh:501-508` compares them, and that arm
  fails outright when the wired copy is absent.
- **S10** — the agent-cap kit version moves from `1.7` to `1.8`. `TOOL-dTieredTribunal-13` is
  order 2 and already moves 1.6 to 1.7 across all FOUR carriers — `tools/hooks/agent-cap.js`,
  `.claude/hooks/agent-cap.js`, `tools/hooks/scratch-guard.js` and `.claude/hooks/scratch-guard.js`
  — so this unit, at order 3, moves what that one leaves behind and carries the same four sites. Both tokens sit on one line,
  `tools/hooks/agent-cap.js:52`, and `tools/check-kit-versions.sh:46-47` asserts the constant and the
  `gov:kit agent-cap@` marker are EQUAL rather than merely present, so a half-bump reds. The bump is
  owed because an adopter's scripts that pass today can deny tomorrow, which is a contract move.
- **S11** — `tools/hooks/README.md` gains the join denial under its existing
  `What the hook DENIES, and how to satisfy it` list, and a short statement of the `--only` selector
  and of the fact that a wired command must never carry it. That file is the declared home of this
  hook's grammar, it ships with the kit, and an adopter receiving a new refusal they cannot satisfy
  is the reason it ships. No digit adjacent to a bound word enters it, so
  `tools/check-agent-cap-restatement.sh` has nothing new to see.
- **S12** — the guards of `review-join self-test` and `verifier fan-out self-test` gain
  `tools/hooks/`, in `tools/gate-legs.json` AND in `tools/workflows/kit.toml`. Both legs test gates
  whose predicate now lives in `tools/hooks/`, and both are guarded on `tools/lib/` and
  `tools/workflows/` only, so an edit to the hook alone arms neither. Both legs, not just this
  unit's, because the sibling has carried the same too-narrow guard since it started delegating and
  fixing the instance while leaving the class is the shape the charter names. `govkit selfcheck`
  compares a descriptor and the manifest on NAME and SUBJECT and not on guard, so the two files must
  be edited together by hand or they drift silently.
- **S13** — two dossiers are refreshed in the same commit as the code.
  `memory/map/features/review-harnesses.md` has a Gaps bullet stating that the two enforcement points
  disagree and a `check-review-join.sh` reuse-affordance line saying to extend the gate by adding a
  predicate to its awk. This unit falsifies both. `memory/map/features/agent-cap.md` gains the fifth
  rule and the selector in its prose, and a Gaps bullet for the residual S7 leaves standing. Neither
  edit touches a `[claims]` block, so no generated map artifact is re-rendered.

## 3. Non-goals (OUT)

- **The `unverified` whitelist.** The research prices it as low false-positive and cheap, and it is
  refused here on merit rather than on cost. Section 8 F1 carries the argument and resolves it.
- **The uncounted-`filter(Boolean)` predicate.** The research measured it reddening two shipped
  harnesses as live instances rather than as false positives, which makes it a fix-the-tree unit and
  not a port. `TOOL-dTieredTribunal-3` section 8 F1 already deferred it with the words that the hook
  work is its own unit. This IS that unit and it still declines, because wiring a predicate that reds
  the tree alongside a predicate that does not makes one landing answer two questions. It is left
  where that fork left it and no new row is minted for it here, since four sibling specs are minting
  ids in this same run.
- **A new gate leg.** The two legs this unit touches already exist under the names section 7 lists.
- **A sibling PreToolUse hook file.** The research allows one. It is refused: it would duplicate
  `blankLiterals`, need its own kit rules, its own settings fragment, its own wiring arm and its own
  version constant, to hold three regexes.
- **Merging `check-review-join.sh` into `check-verifier-fanout.sh`.** After this unit both gates
  delegate to one file, which invites it. They keep different POPULATIONS — every `tools/**/*.js`
  against only the files carrying `export const meta =` — and that difference is recorded as a real
  selection seam in `memory/map/features/review-harnesses.md`. Collapsing them narrows the join ban
  from seven files to three.
- **Any change to `tools/workflows/check-verifier-fanout.sh` beyond its guard row AND its two header
  lines.** It is the shape being copied, not a thing being edited. The two-line CARVE-OUT is `:2`'s
  subject line and `:7`'s exit legend, it is an amendment to this non-goal rather than an exception
  hiding inside it, and it is owed rather than optional: S3's inversion hands that gate the join ban
  as well, so leaving its header alone ships a merge-bar leg whose own description is false. AC15
  grades the corrected pair and section 9 rev-3 logs the amendment. Nothing else in that file moves —
  not the population selector, not the delegation block at `:72-77`, and not the clean message at
  `:84`, which its own self-test reads.
- **Widening either gate's population beyond `tools/`.** A script saved under
  `memory/builds/<slug>/` stays invisible to the file gate. The hook is what reaches it, and only
  when it is run rather than when it is written.
- **The three recorded holes in this hook that this unit does not close.** The enclosing-opener walk
  defeated by two nested wrappers or fifty-nine lines of distance is `TOOL-aNumeralWarden-2`. The
  empty-array-literal blessing is `TOOL-aCandidStub-1`. The marked-derivation branch is
  `TOOL-dTieredTribunal-13`, which is `order 2` and lands before this unit.

## 4. Design

### Inventory

The two entry points, what each can see, and what each says today. Every row was run at HEAD
`96f11c0e` against a single fixture file rather than read from the research record.

| Entry point | Sees an inline script | Sees a committed file | Verdict on the fixture |
|---|---|---|---|
| `node tools/hooks/agent-cap.js` | yes | only via `scriptPath` | rc=0, allowed |
| `bash tools/workflows/check-review-join.sh` | no, by construction | yes | rc=1, two hits named |

The fixture is a cap-compliant harness: a three-element lens array fanned through
`boundedParallel(…, 5)`, a marked `chunk(all, Math.ceil(all.length / 5))` split, and then
`for (const v of verdicts.flat()) map[v.ref] = v`. After this unit both rows read the same verdict,
which is the whole deliverable.

The candidate predicate was run over the REAL tree before being wired, printing hits and
near-misses, as the charter requires. The population is the seven files
`git ls-files --cached --others --exclude-standard -- '*.js' | grep -E '^tools/.*\.js$'` returns,
plus the three copies under `.claude/hooks/`. Result: **zero hits and one near-miss**. The near-miss
is `tools/workflows/tier2-review.js:132`, a `//` comment that necessarily spells the banned
expression while documenting the retired join. That is the load-bearing comment-stripping case, and
it is why a whole-file-text absence assertion is refused here as it is in the gate's header. The
research record cites that comment at `:256`; the line at HEAD is `:132`, re-derived.

The new self-test arms in `tools/hooks/agent-cap.test.sh`, which are what "the failing case has been
observed" means for this unit:

| Arm | Fixture | Expected |
|---|---|---|
| the bracket ban fires with no raw primitive present | `verdicts[v.ref] = v` and no `parallel(`/`pipeline(` | exit 2 |
| the Map ban fires | `m.set(f.ref, v)` | exit 2 |
| the retired identifier fires | `const verdictByRef = new Map()` | exit 2 |
| a comment documenting the join is prose | the gate's own `comment-only` fixture | exit 0 |
| a string mentioning the join is prose | `const s = "do not write m[f.ref] = v"` | exit 0 |
| a template mentioning the join is prose | a prompt naming `verdictByRef` | exit 0 |
| the integer-keyed join is untouched | `verdictById.set(f.id, v)` | exit 0 |
| the selector selects | a rule-2 breach with no join, under `--only=join` | exit 0 |
| the same script unfiltered still denies | that fixture with no flag | exit 2 |
| an unrecognised selector refuses | `--only=bogus` | exit 2 |

The last three are one arm set and none of them is optional. Without the ninth, the eighth proves
only that the fixture is harmless; without the tenth, the selector is a silent switch.

### Data model

`scanJoinFindings(script)` returns an array of `{n, line, why}`, the shape the two existing rules
return, so `main()` formats it with the code already there. The three `why` strings are FROZEN at the
bytes the gate's self-test asserts, because those arms are this port's regression suite and an
unedited arm proving an unchanged verdict is worth more than a prettier string:

| Ban | Matches | `why` |
|---|---|---|
| 1 | an object or Map literal indexed by a `.ref` string | `object/Map literal keyed by a .ref string` |
| 2 | `.get`, `.set`, `.has` or `.delete` called on a `.ref` string | `Map keyed by a .ref string` |
| 3 | the retired identifier, in any position | `the retired verdictByRef identifier` |

The deny message must also carry the remedy sentence the gate prints today, which begins
`Key the join on the integer id`, because `tools/workflows/check-review-join.test.sh:79` asserts it.
The gate keeps its own three strings, which are its own and which no rule change touches:
`clean — no ref-keyed verdict join`, `nothing was scanned, which is not a pass` and
`the population is empty, which is not a pass`.

Two reporting differences follow from delegating and neither is a verdict change. The hook caps a
message at six findings where the awk printed all of them, and the FILE name now comes from the
gate's per-file header rather than from the predicate, since the gate invokes the hook once per file
exactly as `tools/workflows/check-verifier-fanout.sh:66-82` does.

### Migration

**The stripper changes and the change is measured.** The awk at
`tools/workflows/check-review-join.sh:72-92` drops comments and KEEPS string contents.
`blankLiterals` drops comments and BLANKS the contents of quoted strings and of template literals.
Two fixtures were run to find the divergence rather than reason about it. A file whose only banned
spelling sits inside a double-quoted string, and a file whose only banned spelling sits inside a
template literal, are each rc=1 under the awk today and produce zero hits under the candidate.

This narrowing is DELIBERATE and is scoped as such. A verdict join is a code construct and cannot
live inside a string literal, so the awk's wider reading has no defect to catch there. It has a false
positive to cause: `tools/workflows/tier2-review.js` builds every prompt as a template literal, and a
prompt telling a child not to key a join on a ref would red the gate that exists to ban the join.
That is the documentation-of-its-own-fix trap the gate's header already names for comments, live and
unguarded one prompt-edit away. Both fixtures become permanent arms so the narrowing is asserted
rather than incidental.

**No live verdict moves.** Over the ten files probed, the awk and the candidate agree everywhere: the
single near-miss is a `//` comment, which both strippers drop. So this unit changes no verdict on any
file in the tree today, and no pre-existing arm in `tools/workflows/check-review-join.test.sh` has
its EXPECTED STRING edited. Three of those arms do need their SETUP changed, which is what S8 copies
the hook into their two scratch repos for. Each of the five fixtures those arms use was traced through `blankLiterals` by hand
and reaches the same verdict, including the two whose point is that a `//` inside a URL must not
truncate the code line.

**What an adopter sees.** A script that passed the hook and now denies. That is the contract move S10
bumps the kit version for. An adopter who copies only `tools/workflows/check-review-join.sh` and not
`tools/hooks/agent-cap.js` gets exit 2 and a message saying the gate has no predicate to delegate to,
which is why `tools/workflows/kit.toml` already declares `requires = ["agent-cap"]`.

### Rollout

There is no flag and nothing lands dark. The rule denies from the commit that adds it, which is the
point of a guard, and the population it newly reaches is inline scripts that do not yet exist. The
one-commit unit is: hook, gate, wiring arm, self-tests, mirror, version, README, leg guards,
dossiers. Rollback is reverting that commit; nothing generated or migrated is left behind.

This unit is `order 3`. `TOOL-dTieredTribunal-13` is `order 2` and edits the same file's
marked-derivation branch, which is the sequencing the owner ruled in `TOOL-dTieredTribunal-8`. The
two units touch different functions and neither reads the other's, but the builder rebases on 13
rather than developing beside it.

### Files touched (estimate)

- `tools/hooks/agent-cap.js` — S1 through S4, and the S10 version line.
- `.claude/hooks/agent-cap.js` — the S9 mirror refresh, and the S10 version line.
- `tools/hooks/scratch-guard.js` and `.claude/hooks/scratch-guard.js` — the S10 marker line each
  carries at `:41`. `tools/check-kit-versions.sh` reads neither, so AC11's greps are their only witness.
- `tools/hooks/agent-cap.test.sh` — the S8 arms.
- `tools/hooks/README.md` — S11.
- `tools/workflows/check-review-join.sh` — S5 and S6.
- `tools/workflows/check-verifier-fanout.sh` — its two header lines ONLY, `:2` and `:7`, under the
  section 3 carve-out S3 discloses. Listed here because a scope item with no row in this table is the
  omission this build's own audit rounds keep finding.
- `tools/workflows/check-review-join.test.sh` — the two S8 divergence arms and the S8 no-hook arm,
  appended; the hook copied into the two scratch repos after `:133` and `:163`; no existing arm's
  expected string edited.
- `tools/check-wiring.sh` and `tools/check-wiring.test.sh` — S7.
- `tools/gate-legs.json` and `tools/workflows/kit.toml` — S12.
- `memory/map/features/review-harnesses.md` and `memory/map/features/agent-cap.md` — S13.

The review-harness kit version is NOT bumped. `tools/workflows/kit.toml` declares `version_from` over
`tier2-review.js`'s `version:` field, and this unit does not touch that file.
`TOOL-dTieredTribunal-11` is `order 4`, edits it, and owns that decision.

### Alternatives rejected

- **Keep the awk and add a second copy of the predicate to the hook.** Rejected by
  `TOOL-aBatchedTribunal-1d`, which ruled exactly this question for the sibling gate: two
  implementations of one rule do not disagree loudly, they drift.
- **Let the gate run the WHOLE hook, like its sibling, and read the exit code.** Rejected, and it is
  the trap this design nearly fell into. `tools/hooks/agent-cap.js` DENIES ITSELF at exit 2 when fed
  to itself, because its remediation text spells a `batches.map((g) => () => agent(…))` fan-out. The
  sibling gate never meets this because it filters its population to files carrying
  `export const meta =`; this gate does not filter, and narrowing it to match would cut the join
  ban's population from seven files to three.
- **Have the gate grep the hook's stderr for a join marker and ignore any other denial.** Rejected as
  fail-open. Any early exit the hook takes before the join rule — an unparseable payload, a set
  `AGENT_CAP`, a future rule — would read as clean, and a decision procedure whose default is PASS is
  the class this hook's own header refuses.
- **Discriminate a file gate's payload from a real hook payload by the absence of `session_id`.**
  Rejected as UNVERIFIED. The hook's rule-4 comment records that field as MEASURED for an `Agent`
  payload; nothing here measured it for a `Workflow` one, and a guard resting on an unmeasured
  envelope field is the mechanism-that-cannot-fire shape this repo gates against.
- **Fire the rule only on a script that also calls `agent(`.** Rejected. It reduces a false-positive
  class with zero instances in the corpus, and it would silently green four of the gate's existing
  RED fixtures, none of which calls an agent. Keeping the predicate's meaning byte-identical to the
  awk's is what makes the unedited arms a regression suite.
- **A `gov:` marker escape on a line the join ban fires on.** Rejected on this file's own record: the
  first cut of rule 2 allowed a marker on the fan-out line and put the entire whitelist behind one
  comment.

## 5. Production-readiness checklist

- security — the hook is a deny-by-default guard and this unit widens what it denies. The one new
  surface is the `--only` selector, whose defeat is a wired command carrying it; S7 is the control
  and section 8 F3 prices its residual honestly.
- perf / scale — measured on this worktree's `<git-dir>/gate-ledger.tsv`: `review-join ban (no ref-keyed join)` is
  0.723 s of awk over seven files, and the delegating sibling is 1.452 s of node over three. This
  gate becomes six node invocations after S6 removes the hook from its population, which puts the leg
  near three seconds. `tools/gate-legs.json` has no ceiling field, its key union being `argv`,
  `chunk`, `guard`, `impure`, `name` and `subject`, so the cost is recorded here and in the ledger
  rather than declared in the manifest.
- a11y — N/A. A hook and two shell gates, no user interface.
- i18n — N/A. Same reason.
- error / empty / loading states — the gate's two "not a pass" refusals are kept verbatim, and two
  more are added for an absent hook and an absent node, matching the sibling. A gate whose predicate
  cannot be reached must not print clean.
- observability — the hook's deny message names the file, the line, the ban and the remedy. The gate
  adds the filename header. Nothing is silent and nothing is skipped.
- risks — the predicate's population widens from seven committed files to every `Workflow` call. A
  non-review workflow that legitimately indexes something by a `.ref` key would be denied with no
  escape hatch, which is a false positive the file gate could never produce. Zero such instances
  exist in the corpus, no escape marker is added on the record above, and the residual is written
  into the `agent-cap` dossier so it is discoverable when it first bites.
- testing + left-shift gates — the failing case is observed in `tools/hooks/agent-cap.test.sh` before
  the rule lands, and the gate's existing arms are the regression suite for the port. No new leg.
- migration / rollback — one commit, reverted whole. The kit version bump is the adopter-visible
  half and section 4 Migration states what changes for them.
- user docs — `tools/hooks/README.md` under S11. It is agent-facing, which is what `help/` means for
  a kit that ships a hook.

## 6. Acceptance criteria

- **AC1** — When a `Workflow` payload whose script contains `verdicts[v.ref] = v` and no raw
  `parallel(` or `pipeline(` is piped to
  `node tools/hooks/agent-cap.js`, it exits 2 and stderr carries
  `object/Map literal keyed by a .ref string`. The same holds for `m.set(f.ref, v)` with
  `Map keyed by a .ref string`, and for a bare `verdictByRef` with
  `the retired verdictByRef identifier`. At the pinned base all three payloads exit 0, which was run
  rather than assumed.
- **AC2** — When that deny message is read, it carries the remedy sentence beginning
  `Key the join on the integer id`, the string `tools/workflows/check-review-join.test.sh:79`
  asserts. A message that names the ban and not the remedy fails this criterion.
- **AC3** — When a script that breaks the verifier-arity rule and contains no ref-keyed join is
  piped to `node tools/hooks/agent-cap.js --only=join`, it exits 0; when the identical bytes are
  piped with no flag, it exits 2. Both halves, because the first alone cannot tell a working selector
  from a harmless fixture.
- **AC4** — When any payload is piped to `node tools/hooks/agent-cap.js --only=bogus`, it exits 2 and
  the message names the closed value set. A selector value that matches no rule and allows the script
  fails this criterion.
- **AC5** — When `grep -c awk tools/workflows/check-review-join.sh` runs it returns 0, and when
  `grep -F -- '--only=join' tools/workflows/check-review-join.sh` runs it returns a hit. The gate has
  one predicate and it is the hook's.
- **AC6** — When `bash tools/workflows/check-review-join.test.sh` runs it prints
  `PASS — review-join + workflow-syntax gates: all arms held` and exits 0, and when
  `git diff cd971285 -- tools/workflows/check-review-join.test.sh` is read, no `arm '…' '…'` line
  that existed at the pinned base has a changed expected string — the only edits to pre-existing
  lines are scratch-repo setup. An arm whose expected string had to be changed to make this pass is a
  verdict change and fails this criterion.
- **AC7** — When the reproduction fixture from section 4 Inventory is written to a file, then
  `bash tools/workflows/check-review-join.sh <that file>` exits 1 and a `Workflow` payload built from
  the identical bytes piped to `node tools/hooks/agent-cap.js` also exits 2. The two entry points
  agreeing on one byte sequence is this unit's headline and is the criterion that fails if the port
  is cosmetic.
- **AC8** — When `bash tools/workflows/check-review-join.sh tools/hooks/agent-cap.js` runs with that
  explicit path, it exits 1 and names the line holding the rule's own ban table, which S1 is what
  puts there. When `bash tools/workflows/check-review-join.sh` runs with no arguments over the
  shipped tree, it prints `clean — no ref-keyed verdict join` and exits 0. Both halves together prove
  `SELF_EXCLUDE` is a POPULATION exclusion and not a hole in the predicate; the first half alone
  fails if the exclusion were written as a predicate carve-out instead.
- **AC9** — When `tools/check-wiring.sh` runs against a settings file whose `agent-cap.js` command
  carries `--only`, it reports `UNWIRED` and names the flag; against the shipped settings it reports
  `ok`. Observed by an arm in `tools/check-wiring.test.sh`, and
  `bash tools/check-wiring.test.sh` exits 0.
- **AC10** — When `bash tools/hooks/agent-cap.test.sh` runs it exits 0, and every arm listed in the
  section 4 Inventory table is present in that file. When
  `diff tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` runs it prints nothing.
- **AC11** — When `grep -rn 'agent-cap@1\.7' tools/hooks/ .claude/hooks/` runs it returns no hits,
  and when `grep -rln 'agent-cap@1\.8' tools/hooks/ .claude/hooks/` runs it names all four carriers,
  and when `bash tools/check-kit-versions.sh` runs it exits 0. The greps are what bind: that leg
  grades CONSISTENCY and not movement, because `tools/check-kit-versions.sh:46-47` asserts the
  constant and its same-line marker are EQUAL, and it reads neither `scratch-guard.js` copy at all.
  Both halves fail at this unit's own base, where `TOOL-dTieredTribunal-13` has left all four
  carriers at `1.7`.
- **AC12** — When the `review-join self-test` and `verifier fan-out self-test` rows are read in
  `tools/gate-legs.json`, each `guard` names `tools/hooks/`, and the matching `[[gate_leg]]` blocks
  in `tools/workflows/kit.toml` name `{prefix}/hooks/`. One file edited and not the other fails this
  criterion, because `govkit selfcheck` compares name and subject only and will not catch it.
- **AC13** — When `memory/map/features/review-harnesses.md` is read at HEAD, its Gaps section no
  longer claims that a cap-compliant inline script carrying a ref-keyed join passes the hook and
  fails the file gate, and its `check-review-join.sh` reuse-affordance line no longer says to extend
  the gate by adding a predicate to its awk. When `memory/map/features/agent-cap.md` is read, its
  prose names the join rule and the `--only` selector, and its Gaps section names the wired-flag
  residual. When `bash tools/run-gates/run-gates.sh` runs, `codebase-map coverage + freshness` stays
  green, because neither edit touches a `[claims]` block.
- **AC14** — When the denial list in `tools/hooks/README.md` is read, it names the ref-keyed join and
  the `--only` selector, and when `bash tools/check-agent-cap-restatement.sh` runs it exits 0. A
  README bullet that states a bound as a digit reds that gate.
- **AC15** — Three observations over `tools/workflows/check-verifier-fanout.sh`, each of which fails
  at the pinned base, where the measured values are `0`, `1` and `1` — run, not assumed.
  `grep -n 'ref-keyed' tools/workflows/check-verifier-fanout.sh` returns hits on BOTH line 2 and
  line 7, so the subject line and the exit legend each name the join ban beside the verifier cap;
  today it returns nothing at all. `grep -cF '1 = a per-item verify fan-out survives'` returns `0`,
  because a legend offering one route to exit 1 on a gate with two is the defect and not a wording
  preference. `grep -cF "obey the review protocol's verifier cap"` returns `0` for the same reason on
  the subject line. The token is `ref-keyed` and not `ref-keyed join`, deliberately: the gate's own
  clean message spells it `ref-keyed verdict join`, and a criterion that reds the natural spelling
  would be a gate on wording. This is the ONLY criterion in this unit that grades a file section 3
  otherwise forbids editing — the carve-out there authorizes it, S3 is what makes it owed, and neither
  half is optional.

## 7. Gates

This unit adds no gate leg. Every name, subject and guard below was read from `tools/gate-legs.json`
at HEAD rather than typed from memory, and the list is the legs whose SUBJECT this unit touches, not
the run's full leg set. A builder runs the bar and reads the manifest for what will execute.

TWO INDEPENDENT THINGS DECIDE WHETHER A LEG RUNS. A `guard` scopes a leg to a diff. A `subject` of
`kit` makes the runner HOLD the leg entirely unless `GATE_SELFTESTS=1` is set, whatever its guard
says. So an unguarded leg does not run on every bar, and a guarded leg that arms may still be held.
This unit's Definition of Done therefore needs the run that sets both `GATE_SELFTESTS=1` and
`GATE_FULL=1`, and that is not optional here: four of the twelve legs below are `subject: kit`, and
all four of those are this unit's own evidence.

Carrying no guard and `subject: repo`, so they run on every bar and this unit must red none:
`review-join ban (no ref-keyed join)`, `verifier fan-out`, `workflow script syntax`,
`agent-cap restatement`, `kit version markers`, `codebase-map coverage + freshness` and
`memory hygiene`.

Guarded and `subject: kit`, so they arm on this diff and are held until `GATE_SELFTESTS=1`:
`agent-cap self-test` on `tools/hooks/` and `tools/lib/`, `check-wiring self-test` on `.claude/`,
`tools/` and `tools/lib/`, and — only after S12 lands — `review-join self-test` and
`verifier fan-out self-test`. Before S12 those last two are guarded on `tools/lib/` and
`tools/workflows/`, which this unit does edit, so they arm either way; S12 is what makes a
hook-only diff arm them in future.

`review-protocol parity (kit vs dogfood)` is `subject: repo` and guarded on
`memory/guides/REVIEW-PROTOCOL.md`, `tools/lib/` and `tools/workflows/`. The gate edit arms it and it
runs. This unit changes no protocol text, so it must stay green untouched.

## 8. Open questions

- **F1 — should the `unverified` whitelist ride this unit?** The research prices it as low
  false-positive and cheap: a script containing both `verdict` and `agent(` must contain the token
  `unverified`, and all three shipped harnesses already carry it. Options seen: wire it here beside
  the join ban; wire it as its own unit; or refuse it. RESOLVED (agent, 2026-08-26, delegated):
  refuse it. It is satisfiable by a comment, so what it actually proves is that somebody typed a
  word, while what a reader will believe it proves is that the harness has an unverified bucket. The
  charter names that exact trade — a structural check reading as a semantic one, whose false
  confidence is worse than the gap. It is also not a port: unlike the join ban it has no working
  predicate behind it and no observed instance in this corpus, so it would be a new invention landing
  in the same commit as a port, which is two questions in one landing. A stronger form exists — a
  check that the token reaches a RETURNED field rather than any line — and that is a unit, not a
  rider.
- **F2 — should the gate keep judging non-harness `.js` files at all?** The join defect can only
  occur in a review harness, and three of the seven files in the population are not one. Options
  seen: narrow the population to the `export const meta =` marker, which would make this gate
  identical to its sibling; or keep it wide. RESOLVED (agent, 2026-08-26, delegated): keep it wide.
  The wide population is recorded as a deliberate selection seam in
  `memory/map/features/review-harnesses.md`, it is what grades a new harness from its first commit
  before anyone has added the marker, and narrowing it is a scope reduction this unit was not asked
  to make.
- **F3 — OPEN, and the owner's.** S7's control on the `--only` selector is ADVISORY, not a merge-bar
  leg. `tools/check-wiring.sh` runs at SessionStart and through `check-wiring self-test`, which is
  `subject: kit` and held on a default bar, so a hand-wired `--only=join` is caught at the next
  session start rather than at a push. Options: accept the advisory control, which is the regime
  every other hook in this repo already lives under; or promote `check-wiring.sh` to a `subject: repo`
  leg, which is a new leg and touches every wiring arm, not just this one. Recommendation: accept it
  for this unit and price the promotion separately, because a leg that runs the whole wiring checker
  on every bar is a decision about all nine wiring arms and not about this flag. Left open because
  the residual is a real hole in a guard whose own history is an override knob that appeared to work,
  and this run should not resolve that against the owner's judgement.

## 9. Revision log

- rev-1 · 2026-08-26 · initial draft. Every line citation re-derived against source at HEAD
  `96f11c0e`; the research record's `tier2-review.js:256` is `:132` here. The enforcement gap, the
  hook's self-denial, the predicate's self-match on its own retired-identifier ban, the
  awk-against-`blankLiterals` divergence and the two leg timings were each measured rather than
  quoted.
- rev-2 · 2026-08-26 · spec-audit round 1 fold, closing findings 1, 11, 14, 21, 22, 24, 33, 36 and
  41. AC11 re-pointed from the string unit 13 removes to `1.7`/`1.8` over both hook directories, with
  both `scratch-guard.js` carriers added to Files touched and the consistency-not-movement limit of
  `check-kit-versions.sh` stated — 1, 11, 24, 36 and the Files-touched half of 33. S3 states the
  `offendingLines` inversion and its moved `process.exit(0)`, and AC1 plus the first Inventory arm
  pin a fixture with no raw primitive, which is the observation that fails if the rule is merely
  appended — 21. S8, Files touched, section 4 Migration and AC6 carry the hook copy into both scratch
  repos and the no-hook arm for the new refusal's own failing case — 22. S5 widens its deletion to
  the ban-list comment and the stripper note, which is what makes AC5 satisfiable — 14 and 41.
- rev-3 · 2026-08-26 · spec-audit round 2 fold, closing findings 3, 15 and 17. Every claim below was
  read back out of this file's BODY after the edit, not asserted from this entry.
  **Findings 3 and 17 — the verbatim hook copy.** S8 no longer says `verbatim` and no longer cites
  `check-verifier-fanout.test.sh:63`; that instruction is DELETED rather than negated beside. In its
  place S8 spells the two adapted lines in this file's own idiom, resolving the hook from `$ROOT`
  (`:15-16`) and using the scratch variable in scope at each SITE — `$D` after `:133`, `$E` after
  `:163`. The stronger reading the round-2 record flags is taken and reproduced rather than quoted:
  under `set -u` the `$E` spelling at the `:133` site aborts the whole self-test in the main shell,
  measured as `E: unbound variable` with rc=1 and no line after it executing. The third scratch repo
  is renamed off `D`, which `:121` already binds, to `N="$TMP/nohook"`. One thing NOT in either
  filing and found by running the patched file: the `$E` copy puts a `.js` into the repo whose arm
  asserts an EMPTY population, so that arm reds at base with `clean — no ref-keyed verdict join under
  tools/` and holds only once S6's `SELF_EXCLUDE` row lands. Both halves were run and S8 now states
  that S6 is load-bearing for it. No acceptance criterion moved; AC6's "scratch-repo setup only"
  clause already binds these edits.
  **Finding 15 — the undisclosed sibling-gate widening.** S3 gains a disclosure paragraph: inverting
  the `offendingLines` early exit hands `tools/workflows/check-verifier-fanout.sh` the join ban too,
  because its delegation at `:72-77` pipes to `node "$HOOK"` with no `--only` flag — re-derived at
  HEAD. This is the one fix in this round that AMENDS A NON-GOAL, and it lands as a visible carve-out
  rather than a silent widening: section 3's `check-verifier-fanout.sh` bullet now reads `beyond its
  guard row AND its two header lines`, names `:2` and `:7` as the whole of the carve-out, and pins
  what still does not move — the population selector, the delegation block, and the `:84` clean
  message its own self-test reads. Section 4's Files touched gains the matching row, because a scope
  item with no table row is the defect class that dominated this round. AC15 is new and grades the
  corrected legend on three observations whose base values were measured at `0`, `1` and `1`, so all
  three fail today. Its token is `ref-keyed` and not `ref-keyed join`, because the gate's own clean
  message spells it `ref-keyed verdict join` and the narrower token would have redded a correct
  implementation — caught by running the grep, not by reading it. Section 7 is unchanged and owes
  nothing: `verifier fan-out` is unguarded `subject: repo` and `verifier fan-out self-test` is guarded
  on `tools/workflows/`, which this unit already edits, both read from `tools/gate-legs.json` at HEAD.

## 10. Reuse audit

The seam is `tools/workflows/check-verifier-fanout.sh`, and specifically its delegation shape at
`:9-18` and `:72-77`: a merge-bar gate that builds the hook's payload with node and reports what the
hook says, so there is never a second implementation to drift. `memory/map/features/agent-cap.md`
already names it as an affordance — `seam: check-verifier-fanout.delegation` — and
`memory/map/features/review-harnesses.md` names it a second time as the shape any second entry point
on a hook predicate should copy. This unit copies it rather than inventing one.

The second seam is inside the hook: `blankLiterals` at `tools/hooks/agent-cap.js:372` already
produces the comment-and-literal-stripped view the ported predicate needs, and it is the only view in
that file that survives a template literal spanning lines. Reusing it is why S1 is three regexes and
not a second character scanner, and it is also why S2 exists as a disclosed behaviour change rather
than an accident.

`python tools/codebase-map/reuse_lookup.py` was run for the phrase naming a merge-bar file gate that
delegates its predicate to the PreToolUse fan-out hook so one predicate serves both entry points. The
symbol half of the ranking is name-stem noise and is reported as such; the useful row is the
affordance-seam hit on the `agent-cap` dossier, which matched on the largest term overlap in the
result and is the dossier that owns both seams above.

`python tools/memory-recall/query.py` was run with the question of why a file gate delegates its
predicate to the agent-cap hook instead of re-implementing it, terms
`agent-cap hook delegate predicate file gate ref-keyed join inline script PreToolUse verifier
fan-out enforcement modality`. Thirty-seven hits. The decisive one is `TOOL-aBatchedTribunal-1d`,
which ruled this same question for the sibling gate and is quoted in section 4 Alternatives rejected.
`TOOL-aBatchedTribunal-1b` is the companion: the enforcement point is the tool call and not a file
gate, measured from a transcript where every `Workflow` call passed an inline script and none passed
a `scriptPath`. Both were read at their cited locations rather than trusted from the excerpt.
