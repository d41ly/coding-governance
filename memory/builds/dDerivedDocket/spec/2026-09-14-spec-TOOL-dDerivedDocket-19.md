# TOOL-dDerivedDocket-19 — authority only from an owner-committed README

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 19

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-1-spec-audit-g3-round1.md) | spec-audit | TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-20 |

<!-- /gen:spec-records -->

## 1. Goal

The ask envelope lets an ask carry a `may` clause, an authority grant that would lift the build
method's veto 2 for the paths it names (DR §19.3). Honoured from an ask row, a run could file an ask
granting itself a carrier change and then act on it, which was the blocker the critique found (fix
F1). Make authority come from exactly one place, by owner ruling D12-j: a `may:` line in a build
README the owner committed at the default-branch anchor. Nothing a run writes, and no scaffold, may
add to it, and the leg says so when something tries.

## 2. Scope (IN)

- **S1** The authorization scan (`tools/unattended/unattended.sh:1375-1381`) reads a `may:`
  front-matter line from the same blob it already parses. Preflight pins it as the run fact `may:`
  ONLY when the resolved mode is `slug`, and pins `may: none` when the key is absent. Observed by
  AC1.
- **S2** Preflight REFUSES a README whose mode is `prompt` or `recipe` and which carries a `may:`
  line, under a new driver code. Such a README resolves at a run-writable anchor, so its grant is
  one the run could have written, and a refusal makes the attempt loud where ignoring it would not.
  Observed by AC2.
- **S3** The `may:` value is one physical line of space-separated grants, each a repo path or a
  decision id, or the single word `none`. A token that is neither refuses preflight as a typo guard.
  Observed by AC3.
- **S4** Three leg arms. The `may:` fact equals the README's `may:` line at the recorded BASE. A
  `may:` fact other than `none` on a record whose mode is not `slug` reds. No commit inside a run's
  own range adds or changes a `may:` line in ANY build README, which closes the cross-run route of a
  run landing a README that grants the next run. Observed by AC4, AC5 and AC6.
- **S5** A `SCOPE` row carrying a `may` clause is a V13 failure in the backlog verdicts, which unit
  15 introduces. Observed by AC7.
- **S6** The scaffold `gen_build_index.py --new-build <slug> --asks <ids>` never emits a `may:`
  line, even when a named ask carries a `may` clause. Observed by AC8.
- **S7** Carrier text. Protocol §1, in the template and its installed copy, states the rule once:
  where a grant is honoured, what it lifts, what it does not, and that ask-row and `SCOPE`-row
  clauses honour nothing. BUILD-METHOD M3, in its template and rendered copy, gains ONE sentence
  pointing at it. Observed by AC9.
- **S8** A `memory/DECISIONS.md` row under this unit's own id records the M3 boundary change, as fix
  F1 requires. Observed by AC10.

## 3. Non-goals (OUT)

- The `may` clause grammar on ask rows and the `--asks --ready` Grant column are unit 15's and do
  not change. Under D12-j an ask-row `may` is a PROPOSAL the owner may copy into a README by hand; it
  is printed, and it is never honoured.
- The ids start, E3's recipe and `asks:` pinning are unit 16's.
- Enforcing M3's vetoes in code. The run's M3 resolution is agent judgement; the kit pins the grant
  and states the rule, and nothing here claims to observe what the agent then did.
- Lifting veto 3. A grant lifts veto 2 only; see §8 F1.
- Deciding whether a README on the default branch was typed by the owner or landed by an earlier
  run. The anchor cannot tell, which is why S4's third arm refuses the run-side route instead.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-16` — the one-scan front-matter parse that `asks:` joins,
  the pinned-fact seam at preflight, and the resolved mode. Without them `may:` has no scan to join
  and no mode to condition on.
- **consumes-from** `TOOL-dDerivedDocket-15` — the V13 verdict S5 extends and the `--new-build`
  scaffold S6 constrains.
- **hands-off** `TOOL-dDerivedDocket-20` — the Skill and protocol text for the authority rule, which
  this spec's §5 places with the carriers unit.

## 4. Design

### What a grant is, and where it is honoured

| Source of a `may` value | Honoured? | Why |
|---|---|---|
| `may:` in a README resolved in `slug` mode | yes, pinned at preflight | `slug` resolves only at the default-branch anchor, so a folder already existed there before the run |
| `may:` in a README resolved in `prompt` or `recipe` mode | refused at preflight | those modes admit the second anchor, which the run can write |
| a `may` clause on an ask row | never | anyone holding the ask's slug writes the row |
| a `may` clause on a `SCOPE` row | refused as V13 | a triager writes it about someone else's ask |
| the scaffold's output | never emitted | a generated README carries no authored authority |

`slug` mode implies the default-branch anchor because the second anchor admits only
`SECOND_ANCHOR_MODES="prompt recipe"` (`tools/unattended/unattended.sh:497`), and leg check 29
already reds a `slug` record whose BASE came from the second anchor.

### What a grant lifts

A path grant lifts veto 2 for a change confined under that path. A decision-id grant lifts veto 2
for the change that `memory/DECISIONS.md` row ratifies. Veto 1 and veto 3 are untouched. The protocol
states this once, in §1, and M3's added sentence points there, so the rule is not stated twice
(M1's one rule).

### The cross-run arm

A run lands commits on the default branch; a README it lands becomes a default-branch README for
the next run, so without a guard one run could grant another. The arm walks each run's own range,
BASE to its witness for a terminal record or BASE to HEAD for a live one, and reds a commit whose
diff adds or changes a `may:` front-matter line in any `memory/builds/*/README.md`. It reads the diff,
never the run's own claim. It does not see a grant typed by a person on the default branch, which is
the owner's act and is the channel D12-j keeps open.

### Fail codes

The S2 and S3 refusals take new driver codes, and the S4 arms report under the leg's check 19 beside
the mode arms they extend. New numbers are allocated at build time as the next free integer, because
other units of this build allocate codes concurrently.

### Rollout

No gov README carries `may:` today, so every run pins `may: none` and every arm passes over an
honest absence. The fixtures carry the coverage.

### Inventory

- the README front-matter key `may:` and the run fact `may:`;
- two driver refusal codes, numbers allocated at build time;
- one `memory/DECISIONS.md` row under this unit's own id.

Any new shell function is named through `python tools/lexicon/lexicon.py --suggest <identifier>
--as <cell>`.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` ·
`tools/unattended/check-unattended.sh` · `tools/unattended/check-unattended.test.sh` ·
`tools/unattended/PROTOCOL.template.md` · `memory/guides/UNATTENDED-PROTOCOL.md` ·
`tools/memory-tree/BUILD-METHOD.template.md` · `memory/guides/BUILD-METHOD.md` ·
`tools/memory-tree/backlog.py` and its selftest · `tools/memory-tree/gen_build_index.py`'s selftest ·
`memory/DECISIONS.md` · `.memory-tree.conf` for `ARMS_FLOORS`.

### Budgets

BUILD-METHOD's ≤27648 B is shared with units 20 and 31 and stood at 26439 B at BASE. This unit's
net growth there is at most 300 B; raising M1's budget is an owner turn under veto 2 and is not
this unit's to take. The protocol's guide cap is 61440 B against 57815 B at BASE, shared with at
least five units of this build; this unit's net growth there is at most 600 B.

### Alternatives rejected

- **Honour the union of `may` clauses on mandated asks, read at M-BASE (DR §19.2).** Rejected by
  fix F1 and ruling D12-j: M-BASE is on the default branch, but the row's writer is anyone holding
  the ask's slug, including a run that filed it.
- **Ignore a `may:` line on a prompt-mode README silently.** It leaves a self-grant attempt invisible
  in every record; S2's refusal costs a legitimate prompt run nothing, because such a README has no
  reason to carry the key.

## 5. Production-readiness checklist

- security — this unit narrows an authority surface to one owner channel and adds a refusal for the
  run-side route; it adds no write path.
- perf / scale — one more key in an existing scan; the cross-run arm is one diff per run range,
  over the README glob only.
- error / empty / loading states — absent key pins `none`; a malformed grant is a named refusal; a
  prompt-mode grant is a named refusal.
- observability — the pinned fact is printed at preflight and re-read by the leg.
- risks — the anchor cannot prove a default-branch README was typed by the owner; S4's third arm
  closes the kit's own route and states the rest.
- testing — arms in the driver and leg suites and in the backlog and build-index selftests, each
  observed by hand in a scratch fixture repo with a local bare remote (D12-h method (b)); the suites
  themselves run at the build's one post-build bar.
- migration — none; no README carries the key.
- user docs — protocol §1 and one M3 sentence; the Skill's own text is unit 20's.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a `slug`-mode fixture README carrying `may:` with a path
  and a decision id, the record pins those grants as `may:`; with no key it pins `may: none`. Proven
  in `tools/unattended/unattended.test.sh`.
  Red when: the fact is pinned in `prompt` mode as well, so a run-written README grants.
  permission: this unit may not run the unattended suites; the observation is made by hand in a
  scratch fixture repo with a local bare remote, and the suite runs at the post-build bar.
- **AC2** — When `--preflight` runs over a `prompt`-mode fixture README carrying `may:`, it refuses
  under its new code and writes nothing.
  Red when: preflight pins `may: none` and continues, which hides the attempt.
- **AC3** — When the `may:` value carries a token that is neither path-shaped nor id-shaped, preflight
  refuses naming the token.
  Red when: the token is pinned as a grant.
- **AC4** — When a fixture record's `may:` fact differs from the README's line at its recorded BASE,
  `bash tools/unattended/check-unattended.sh` reds check 19 naming both values.
  Red when: the arm compares against the README at HEAD.
- **AC5** — When a fixture record in `prompt` mode carries `may:` other than `none`, check 19 reds.
  Red when: the arm grades only `slug` records.
- **AC6** — When a commit inside a fixture run's range adds a `may:` line to another build's README,
  check 19 reds naming the commit and the README.
  Red when: the arm reads only the run's own README, so the cross-run grant passes.
- **AC7** — When a fixture `BACKLOG.md` carries a `SCOPE` row with a `may` clause, the backlog
  verdicts report V13 naming the row.
  Red when: V13 grades only the clause grammar and admits the label.
- **AC8** — When `python tools/memory-tree/gen_build_index.py --new-build` scaffolds a README over a
  fixture ask carrying a `may` clause, the output has no `may:` line.
  Red when: the scaffold copies the clause into front matter.
- **AC9** — When `bash tools/unattended/check-unattended.sh` and the `kit/dogfood doc parity` leg
  run after S7, both copies of protocol §1 and of BUILD-METHOD are byte-identical to their
  templates, and the `build-method size` leg stays green.
  Red when: the sentence lands in one copy only, or BUILD-METHOD exceeds its byte cap.
  permission: unit passes run no gate legs (fix F7); this observation is made at the build's one
  post-build bar.
- **AC10** — When `git grep -n "TOOL-dDerivedDocket-19" memory/DECISIONS.md` runs, it returns one row
  recording that a grant is honoured only from an owner-committed README and lifts veto 2 only.
  Red when: the row is absent, so the M3 boundary change lives only in carrier prose.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `memory hygiene` · `kit/dogfood doc parity` · `build-method size` · `build-index selftest` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a `slug` README with `may:`, a `prompt` README with `may:`, a malformed grant · `ARMS_FLOORS` for `tools/unattended/unattended.sh`
New arm: `tools/unattended/check-unattended.test.sh` · a forged fact, a `prompt` record with a grant, a run range adding `may:` to a foreign README · `ARMS_FLOORS` for `tools/unattended/check-unattended.sh`

## 8. Open questions

- **F1 — does a grant lift veto 3 as well as veto 2?** Lifting both is the more feature-rich option,
  and it is discarded by veto 3 itself: a grant that widens a security or write surface beyond the
  tier's pricing is exactly what veto 3 refuses. RESOLVED (agent, 2026-09-14, delegated): veto 2
  only.
- **F2 — where may authority come from?** RESOLVED (owner, 2026-09-13): D12-j, only from an
  owner-committed build README at the default-branch anchor; the scaffold never emits `may:`.
- **F3 — the brief's edge table has unit 16 consuming from this unit, against the declared order.**
  Unit 16 is ordered before this unit, and the hygiene edge arm reds a consumes-from whose target is
  ordered after the consumer. The dependency runs the other way: this unit extends unit 16's scan
  and pinning. RESOLVED (agent, 2026-09-14, delegated): this unit declares consumes-from unit 16;
  unit 16's spec owes the matching hands-off, and its consumes-from this unit is dropped.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from fix F1 and ruling D12-j. Reverses the brief's edge between
  this unit and unit 16 (§8 F3) and adds consumes-from unit 15, whose V13 verdict and scaffold this
  unit constrains. Adds the cross-run arm, which neither DR nor the brief names, after the regrounding
  found that a `slug` README on the default branch can be one an earlier run landed.

## 10. Reuse audit

The seam is the authorization scan's single `awk` over the README blob at BASE
(`tools/unattended/unattended.sh:1375-1381`), which unit 16 extends with `asks:` and this unit with
`may:`, plus leg check 19's re-parse of the same blob. `reuse_lookup.py "authority grant honoured
only from an owner committed record"` returns the `unattended` dossier's `.unattended.conf` seam and
generic record helpers; no seam in the lookup grades authority, and its scan reports `.sh` unscanned.
The recall probe surfaced `TOOL-aStandingWrit-1`, which names the property S4's third arm closes: a
run that lands a new build README authorizes the next run. Where DR and the source disagree: DR
§19.2's "union of `may` clauses" is superseded by F1 and D12-j, and no code implements either yet.

Recall terms used: `veto-2 governance-carrier authority grant owner-committed default-branch anchor
prompt-mode run-authored mandate scaffold delegated resolver`
