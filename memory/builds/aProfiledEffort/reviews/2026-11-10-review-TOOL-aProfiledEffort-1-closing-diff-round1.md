**Serves:** diff-review TOOL-aProfiledEffort-1 TOOL-aProfiledEffort-2 TOOL-aProfiledEffort-3

# Tier-2 closing diff review — aProfiledEffort, ROUND 1

*The cumulative diff landing on main. Finders `gov-diff-reviewer`, skeptic batches `gov-skeptic`,
synthesis `gov-synthesizer`. Every finding listed as an item survived a skeptic prompted to refute
it. The synthesizer re-ran nothing and adds no finding of its own.*

**Reviewed range:** 7c896db61b45b2e825779fe7ace29337e75cd095...c1d1e19f423c8e8ebe03378bdd383d107ce812df
ROUND 1.

## Verdict: CLEAN WITH FIXES

Zero items at BLOCKER, zero at HIGH, four at MEDIUM, three at LOW.
By item: 7 items. By raw confirmed finding: 7 findings (0 blocker, 0 high, 4 medium, 3 low).
No two confirmed findings describe one defect, so the two tallies agree.
No behaviour in the range is wrong on a common path.
One item is a narrow misreport by the `agents` verb, two are shipped texts that state more than the
mechanism does, and four are checks that cannot fail on a rule the diff states.

## Review shape

Intensity full, raw 13, confirmed 7, refuted 6, merged 0, unverified 0 (0 uncertain), precision 0.54.

| lens | returned | raw | confirmed | refuted | merged | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|---|
| security | yes | 2 | 0 | 2 | 0 | 0 | 0 | 0.00 |
| correctness | yes | 1 | 0 | 1 | 0 | 0 | 0 | 0.00 |
| seams | yes | 2 | 2 | 0 | 0 | 0 | 0 | 1.00 |
| verification | yes | 6 | 4 | 2 | 0 | 0 | 0 | 0.67 |
| intent | yes | 2 | 1 | 1 | 0 | 0 | 0 | 0.50 |

## Run integrity

- Lenses 5/5 returned, 0 died. Skeptic batches 5/5 returned, 0 died.
- 0 contradictory verdicts demoted to unverified, 0 orphaned duplicate refutations demoted to
  unverified, 0 duplicate refutations counted as merged confirmations, 0 spurious verdicts
  discarded, 0 duplicates.
- Fixes on confirmed findings: 5 judged sound, 1 judged UNSOUND, 1 judged INSTANCE-ONLY (it cures
  the cited instance and leaves its class standing), 0 none proposed, 0 not judged.
- Severity on confirmed findings: 0 ungraded by the skeptic, 0 re-graded by the skeptic.
- Unverified findings: 0 answered uncertain, 0 with no usable verdict.
- Lens notes: none supplied, so every lens ran on the kit's generic brief.
- Intent: neither `specs` nor `context` was supplied, so the lenses had only the range's commit
  messages to judge intent against.
- Checklist: 39 items, acquired by the harness from
  `--for-diff 7c896db61b45b2e825779fe7ace29337e75cd095..HEAD`, each assigned to exactly one of 5
  lenses: security 8, correctness 8, seams 8, verification 8, intent 7.
- By design: none supplied, no caller byDesign and a block of 0.
- Refuted findings shown to synthesis: 6. Same-address pairs shown: 3.
- Dispositions: unclassed refuse; 39 class slugs handed; 149 leg names read from
  `tools/gate-legs.json`.

Every integrity counter that marks a degraded run is zero.
The one unsound fix (item 4) is replaced below by the skeptic's corrected fix.

## Items

### 1. MEDIUM — the `agents` verb reports the agent type's default level as the level an agent ran at (id 4)

**Where:** `tools/roles/README.md:215`, `tools/roles/README.md:113`, `tools/roles/handoff.py:924-928`,
`tools/roles/render_agents.py:280`.

**What is wrong:** The new limits paragraph names the `agent` line as the one place that shows the
effort each agent ran at. When a transcript holds no assistant record carrying `effort`, that line
falls back to the `effort:` line of `.claude/agents/<role>.md`. The render resolves that line with
no model, so it is always the default tables' level. Under a matched profile the dispatched level
differs: `role-efforts` prints `gov-builder: high`, `role-efforts --model claude-fable-5-2` prints
`gov-builder: medium`.

**Consequence:** A Fable builder dispatched at medium with no recorded effort is reported as `high`,
as if observed. Nothing else refuses a call made without the flag, so the only audit channel
misreports on this path. The path is narrow: it needs a transcript with no assistant record that
carries `effort`.

**Fix (judged SOUND by the skeptic):** In the `agents` verb, print `unknown` when the transcript
records no effort instead of falling back to the agent type's line. Alternatively keep the fallback
and correct `README.md:215` and the field table at `README.md:113` to say the fallback is the type's
default-table level, not the dispatched one. The `unknown` branch changes a behaviour the base
documented, so the row at `README.md:113` and any arm asserting the fallback move with it.

**Left-shift gate:** an `agents` fixture in `roles adopter self-test` whose transcript has no
`effort`, under a policy with a matched profile, asserting the line does not print the type's level.

### 2. MEDIUM — no arm fails when a matched profile stops being read alone for stage overrides (id 6)

**Where:** `tools/roles/render_agents.py:676`, `tools/roles/render_agents.py:696`,
`tools/roles/roles_lib.py:655-659`, `tools/roles/adopt-roles.test.sh:773-779`.

**What is wrong:** The selftest's `base` policy holds no `[effort.stages]` table, so in every arm-19
row the default table's stage overrides are empty. Adopt arm 19 checks
`stage-efforts spec-write --model vendor-tfam-9` for exit 0 only, and its greps read the `roles` and
`closing-review` outputs alone.

**Consequence:** A resolver that merged the default table's `[effort.stages.<workflow>]` under the
profile's would pass every arm. The README's rule that the role and stage entries of the default
tables do not reach a model a profile matches is uncertified for stages. The role side is covered.

**Fix (judged SOUND by the skeptic):** In the selftest add `[effort.stages.w5] k2 = "high"` to `base`
(the plain row becomes `k2: high`) and keep 19c's expectation `k2: xhigh`. Or in adopt arm 19 assert
`"skeptic":"low"` in the spec-write output for the `tfam` id. Observe it red under the merge
mutation.

**Left-shift gate:** the added row lives in `roles render selftest` (or the assertion in
`roles adopter self-test`).

### 3. MEDIUM — the lower-casing of the model id has no check (id 7)

**Where:** `tools/roles/roles_lib.py:635`, `tools/roles/render_agents.py:695-699`,
`tools/roles/adopt-roles.test.sh:771-773`.

**What is wrong:** `resolve_profile` lower-cases the id before splitting it into words. Every model
id in selftest arm 19 and adopt arm 19 is already lower-case, so dropping `.lower()` changes no row.

**Consequence:** The docstring and README promise an id is matched after lower-casing. A regression
would send an id spelled `Claude-Fable-5-2` to the default tables with exit 0 and no note, and no
gate would notice.

**Fix (judged SOUND by the skeptic):** Add one row to arm 19's table, for example
`("19c", fam, "Vendor-FAM-9", <the 19c expectation>)`, and observe it red with `.lower()` removed.

**Left-shift gate:** the mixed-case row in `roles render selftest`.

### 4. MEDIUM — three shipped texts say every stage runs at medium, and two harness stages get no level (id 12)

**Where:** `tools/roles/house/policy.toml:26`, `tools/roles/README.md:195`, `help/roles.md:54-55`,
`tools/workflows/unattended-build.js:494`, `tools/workflows/tier2-review.js:520`,
`tools/roles/workflows.toml:37,47,67`.

**What is wrong:** The seeded fable profile is stated to run every role and stage at medium.
`committer` (unattended-build `ROLE_KEYS`) and `probe` (tier2-review `ROLE_KEYS`) are keys of no
workflow `stages` table, so `stage-efforts --model <id>` never prints them. Each harness spawns them
at the agent type's own level, else the session's.

**Consequence:** On a Fable session whose own effort is not medium, the spec-commit stage and the
review resume probe do not run at medium while three texts say every stage does. The README limits
paragraph names the case only generically. The effect is contained to two small stages.

**Fix (the finder's fix was REJECTED by the skeptic; this is the skeptic's corrected fix):** Narrow
the three texts (`tools/roles/house/policy.toml:26`, `tools/roles/README.md`, `help/roles.md`) to
"every role and every stage key of a workflow's `stages` table". Name `committer` and `probe` in the
README's limits paragraph as harness stages that take the agent type's level, else the session's.
Leave `tools/roles/workflows.toml` unchanged.

**Left-shift gate:** an arm in `roles adopter self-test` comparing the keys `stage-efforts` prints
against each harness's `ROLE_KEYS`, with the unkeyed stages held in a declared list the README names.

### 5. LOW — the seeded policy file contradicts itself on how a changed value reaches an agent (id 5)

**Where:** `tools/roles/house/policy.toml:2`, `tools/roles/house/policy.toml:28-29`.

**What is wrong:** The untouched header at line 2 says a changed value reaches an agent after
`render_agents.py --write` and a new session. The comment this diff adds says a profile reaches an
agent at dispatch, never through its rendered agent type.

**Consequence:** Comment only. An owner editing `[effort.profiles.*]` who follows the header
re-renders and restarts for nothing, because the render resolves with no model.

**Fix (judged SOUND by the skeptic):** Reword line 2 to scope it: a changed `[effort.roles]` or
`default` value reaches an agent type after `render_agents.py --write` and a new session; stage and
profile values apply at the next dispatch.

**Left-shift gate:** no leg grades a comment; enter it in the project's bug-class checklist under the
class named in the appendix.

### 6. LOW — a `match` list of more than one word is never exercised (id 8)

**Where:** `tools/roles/roles_lib.py:637`, `tools/roles/roles_lib.py:510-516`,
`tools/roles/render_agents.py:677-680,714-725`, `tools/roles/adopt-roles.test.sh:761`.

**What is wrong:** Every fixture profile and the seeded profile hold exactly one match word. A
resolver honouring only `match[0]` passes every arm. The duplicate-word defect check is likewise
reached only with single-entry lists.

**Consequence:** `help/roles.md` documents `match` as plural. A regression that reads one entry
leaves a second family word silently on the default levels. No current behaviour is wrong.

**Fix (the finder's fix was judged INSTANCE-ONLY by the skeptic; this is the skeptic's class-level
fix):** Give the selftest's `ven` profile a two-word match and add a row resolving an id that holds
only the second word. Also add a 19e defect row whose second entry collides with another profile,
for example `match = ["x", "fam"]` with `default = "low"`, expecting one R12 line under `x.match`,
so the validator's per-word loop is exercised past the first entry. The finder's proposal (the
two-word `ven` match and the second-word row alone) cures the cited instance only.

**Left-shift gate:** both rows in `roles render selftest`.

### 7. LOW — three verb-level branches the commit message states have no failing check (id 11)

**Where:** `tools/roles/handoff.py:991`, `tools/roles/handoff.py:993`, `tools/roles/handoff.py:1001`,
`tools/roles/adopt-roles.test.sh:765-783`.

**What is wrong:** Arm 19 passes `--model ""` but never a whitespace-only id. It runs both verbs only
over a valid policy and unambiguous ids, and discards stderr. So nothing exercises the whitespace
refusal, a policy defect exiting 1 with its R12 line from `role-efforts`, or a model two profiles
match exiting 1 through either verb.

**Consequence:** Weakening `not a.model.strip()` to an equality test, dropping `role-efforts` from
the tuple at line 993, or a `RolesError` escaping as a traceback would each leave every arm green.
The behaviour is correct today.

**Fix (judged SOUND by the skeptic):** In adopt arm 19 add a `--model ' '` call to 19d's loop. Add a
fifth assertion: after appending a second profile matching another word of `vendor-tfam-9`, both
verbs exit 1 with stderr holding `R12` and both `effort.profiles.*.match` keys and no `Traceback`.
Raise `FLOOR_ASSERTIONS` to 56.

**Left-shift gate:** the added assertion in `roles adopter self-test`.

**Not a twin of refuted ids 1 and 3**, which cite the same line. Those claimed the guard is too
narrow for a wordless id; this item says the guard's stated behaviour has no regression check.

## Twins

No refuted finding describes the same defect as a confirmed one.
Ids 1 and 3 against id 11 are covered under item 7.
Refuted id 9 (the seeded profile's values have no check) and confirmed id 12 (the texts overclaim
"every stage") sit at adjacent lines of `tools/roles/house/policy.toml` and are different defects.

## Outstanding

No finding is unverified.

review-shape kind=diff-review round=1 intensity=full at=synth raw=13 confirmed=7 refuted=6 merged=0 unverified=0 blocker=0 high=0 medium=4 low=3 agents=11 out-tokens=99959
review-round round=1 limit=- prior=- count=0 state=CONVERGED
## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes | disposition |
|---|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/roles/handoff.py:991 | low | - | refuted | Not a bug: the behaviour is the documented contract. I reproduced it (`--model "."` and `--model "???"` print {"builder":"high"} rc=0), but tools/roles/handoff.py:39 and :86 state that an id no profile matches answers the default levels with no note, and the unit's spec S4 scopes the exit-2 refusal to an empty or whitespace-only value. A wordless id is one more unmatched id, with the same outcome as a misspelt one: `--model claude-fabel-5-2` also printed {"builder":"high"} rc=0. The guard at :991 refuses a blank, which is what it claims to refuse; it does not claim to validate ids. | instance | - | - |
| 2 | security | tools/roles/SKILL.template.md:28 | low | - | refuted | Not established as a defect with the claimed consequence. `--model <id>` in the seven carriers is placeholder notation in prose, not a literal command line (a literal `<id>` would itself be a shell redirection). I ran the unquoted form in bash: `--model claude-fable-5-2[1m]` printed {"builder":"medium"} rc=0, the correct fable profile. The silent wrong-level case needs a file named `claude-fable-5-21` or `claude-fable-5-2m` in the working directory, which nothing in the repo creates. The zsh case fails loudly before the script runs, so it ships no wrong result. The finder ran neither case and graded it low; under the harness default a low finding that cannot be established is refuted. | sound | - | - |
| 3 | correctness | tools/roles/handoff.py:991 | low | - | refuted | Not a bug, and the same claim as id=1 (also refuted, so not marked duplicate). I reproduced the probes: `???`, `.` and `<id>` each print {"builder":"high"} rc=0, and `claude-fable-5-2` prints medium. But handoff.py:39 and :86 document that an unmatched id answers the defaults with no note, and spec S4 limits the refusal to empty or whitespace. A misspelt id with words (`claude-fabel-5-2`) falls back identically, so the wordless case contradicts nothing the guard promises. The finding's own example `<id>` contains the word `id`, so the proposed predicate would still let the unsubstituted placeholder through. | instance | - | - |
| 4 | seams | tools/roles/README.md:215 | medium | medium | confirmed | Observed tools/roles/handoff.py:924-928: `level = tr["effort"]`, and when that is None the level is read from `.claude/agents/<role>.md`'s `effort:` line. tools/roles/render_agents.py:280 calls `lib.resolve_effort(cat["policy"], slot)` with no model, so that line is always the default tables' level. The fallback code and the field-table row (README:113, `else the agent type's effort: line`) are unchanged from the base (base handoff.py:902-906, base README:108), but before this diff a role's rendered level was the level a direct spawn of that role ran at. This diff adds profiles that reach an agent only at dispatch (house/policy.toml ships `[effort.profiles.fable] default = "medium"` against `gov-builder = "high"`), and adds the README:214-215 sentence naming the `agent` line as what prints the effort each agent ran at. So the diff makes the fallback print a level that is not the dispatched one, unmarked. I did not run the finder's probe or count transcripts; the path is narrow by the finder's own account (only a transcript with no assistant record carrying `effort`), and the field table still discloses the fallback, so the effect is contained. Fix: either branch cures the cited defect; printing `unknown` removes the misreport and README:113 already names `unknown` as the nothing-answers value, and the doc-only branch makes the claim true. The `unknown` branch changes a behaviour the base documented, so the row at README:113 and any arm asserting the fallback must move with it. | sound | - | class:degradation-known-but-unreported |
| 5 | seams | tools/roles/house/policy.toml:29 | low | low | confirmed | Observed tools/roles/house/policy.toml: line 2 (byte-identical at the base) says `A changed value reaches an agent after render_agents.py --write and a new session`; the diff-added lines 28-29 say `A profile reaches an agent at dispatch, never through its rendered agent type`. render_agents.py:280 resolves with no model, so a profile edit moves no rendered file and the header is false for the values this diff adds to the file. Comment only, no behaviour effect. The header's looseness for `[effort.stages]` predates the diff, but the in-file contradiction is introduced by it. Fix: rewording line 2 to scope it to roles/default and name dispatch for stages and profiles cures it; the only other copy of the sentence is a historical spec under memory/builds/aOrientedCast, not a live surface. | sound | - | class:amendment-leaves-its-other-half-standing |
| 6 | verification | tools/roles/render_agents.py:696 | medium | medium | confirmed | Judged from source, not run. tools/roles/render_agents.py:676: `base` is `[effort] default=low` plus `[effort.roles] r-one=high` with no `[effort.stages]` table, and `fam`/`ven` build on it, so in every 19a/19c/19d/19f row the default table's `stages.w5` is empty. roles_lib.py:655-659 reads `stages` from the matched profile's table alone; a variant that merged the default table's stage overrides under the profile's would return the same values for every row, so 19c's `k2: xhigh` cannot red. In tools/roles/adopt-roles.test.sh arm 19, `stage-efforts spec-write --model vendor-tfam-9` only sets `_c19=0` on a non-zero exit; the greps that follow read a19.roles.tfam and a19.closing-review.tfam only, and the house policy holds no `[effort.stages.closing-review]`, so that workflow cannot tell either. The house policy does hold `[effort.stages.spec-write] skeptic/synthesis = medium` against the appended `tfam` default `low`, the distinguishing case, and its output is never asserted. No other file under tools/, skills/ or .github exercises profiles. The role side is certified (r-one high in base versus max under fam), so the gap is stages only: a real hole in a check, contained to one resolver rule. Fix: either option makes the mutation observable. With `[effort.stages.w5] k2 = "high"` in base, 19c still expects `k2: xhigh` and a merge would give `high`; asserting `"skeptic":"low"` in a19.spec-write.tfam does the same in the adopt arm. The selftest option also requires `plain` to change to k2 high, which the fix states. | sound | - | class:rule-stated-with-no-check-that-fails |
| 7 | verification | tools/roles/roles_lib.py:635 | medium | medium | confirmed | Observed: tools/roles/roles_lib.py:635 lower-cases the id before MODEL_SEGMENT_RE ([a-z0-9]+, line 49) splits it. Every model id in selftest arm 19 (tools/roles/render_agents.py:695-699: vendor-fam-9, vendor-other-9, affam-9, None) and in adopt arm 19 (tools/roles/adopt-roles.test.sh:771-773: vendor-other-9, vendor-tfam-9) is already lower-case, so dropping .lower() changes no row's result. Judged from source, not by running the selftest. The diff introduced both the function and the arm (resolve_profile is absent at the base). Spec TOOL-aProfiledEffort-1 section 7 says arm 19 covers AC3, whose red condition includes 'a Fable id in another spelling matches nothing', yet only AC3's one-off command uses a mixed-case id. A regression would send a mixed-case id to the default tables silently with exit 0; effect is contained to a missing check on a working path. Fix: with .lower() removed 'Vendor-FAM-9' splits to 'endor','9', matches nothing and resolves to the plain levels, so the proposed 19c row goes red; it covers the one lower-casing site both resolvers route through. | sound | - | class:rule-stated-with-no-check-that-fails |
| 8 | verification | tools/roles/roles_lib.py:637 | low | low | confirmed | Observed: every fixture profile holds a one-entry match list: fam ['fam'] and ven ['vendor'] (render_agents.py:677-680), x ['x'] and the defect rows (714-725), tfam ['tfam'] (adopt-roles.test.sh:761), and the shipped fable ['fable'] (house/policy.toml:26). roles_lib.py:637 intersects the id's words with the whole list, and a variant reading only match[0] returns the same result on every row; judged from source. The duplicate-word check at roles_lib.py:510-516 is likewise only reached with single-entry lists (row 725, ['fam']). Introduced by this diff. No current behaviour is wrong; this is a coverage gap on a documented plural grammar. Fix: giving ven ['vendor','vend2'] keeps both 19f rows valid and a second-word row would catch the match[0] regression, but it leaves the multi-entry duplicate-word path, which the finding also names, unexercised. | instance | - | class:rule-stated-with-no-check-that-fails |
| 9 | verification | tools/roles/house/policy.toml:25 | medium | - | refuted | By design, and partly inaccurate. Observed: the spec this diff adds, memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-1.md:405-407, records the gap deliberately: 'The seeded profile's values are seed data: R12 grades that medium is a level and fable is one word, and nothing grades that Fable runs at medium, which AC2 observes once. Arm 19 proves the matcher and the validator over its fixture's names, never over the seeded file.' adopt-roles.test.sh:49 and spec 2 line 236-240 repeat the exclusion, and policy.toml:1 marks the file 'Seeded: yours to edit'. Two of the three regressions the finding names are in fact caught: a misspelled match key hits 'effort.profiles.fable.match is absent' at roles_lib.py:503-504 (plus the unknown-key check at 501), which the roles catalogue leg runs over the real tree, and a matcher change that stops a hyphenated id splitting into words is caught by arm 19's fixture rows (vendor-fam-9 to fam, affam-9 to none). Only outright deletion or a value edit of the seed table is ungated, which is the owner-editable seed data the spec chose not to pin. | sound | - | - |
| 10 | verification | tools/roles/SKILL.template.md:28 | medium | - | refuted | By design, in the unit's own spec. The facts hold: my grep over the .md/.js carriers printed the same four unflagged lines (tools/workflows/tier2-review.js:210, tier2-review.template.js:210, unattended-build.js:224, unattended-build.template.js:224), and `--model` appears in adopt-roles.test.sh only in arm 19's verb calls (lines 771-775), with no arm reading a carrier. But memory/builds/aProfiledEffort/spec/2026-11-10-spec-TOOL-aProfiledEffort-3.md section 3 lists both as non-goals: the harness template header comments at exactly :210 and :224 ('this unit's disposition is to leave them as they are', since the caller still passes what the verb prints), and 'a hook or a gate arm that refuses ... a carrier whose call lacks the flag'. Section 5 risks states 'A later edit that adds a call without the flag is caught by no leg', section 7 repeats 'What no leg checks: that a carrier's call names the flag', and the shipped tools/roles/README.md limits paragraph says 'Nothing refuses a call made without the flag'. The finding restates a disclosed, deliberately accepted limit rather than a defect the diff hid. | instance | invariant-held-on-one-admission-path | - |
| 11 | verification | tools/roles/handoff.py:991 | low | low | confirmed | Observed in tools/roles/adopt-roles.test.sh:765-783: arm 19's loop calls both verbs with no flag, `--model vendor-other-9`, `--model vendor-tfam-9` and `--model ""` only, discards stderr on the first three, and appends one profile to a valid policy. So nothing exercises a whitespace id, the exit-1 path of the `except lib.RolesError` at tools/roles/handoff.py:1001, or `role-efforts` membership in the tuple at :993, which this diff added (base line 966 held only harness-args and stage-efforts). Read-only probe: `handoff.py role-efforts --model " "` exits 2 today; in roles_lib.resolve_profile a whitespace id yields no words and so no profile, so weakening `not a.model.strip()` to an equality test would resolve to the default levels with every arm green. The commit message of d1ef90538 states both behaviours ('An empty or whitespace --model exits 2', 'a policy defect exits 1 with its R12 line'). The two-profile refusal is covered at the resolver level only (render_agents.py:707, 19f), not through the verbs. Effect is contained: the behaviour is correct today and only the regression guard is missing, so low. The fix runs after the loop on the last arm's fixture, so it disturbs no earlier assertion, and one exit-1 assertion through both verbs covers the shared except branch. | sound | - | class:rule-stated-with-no-check-that-fails |
| 12 | intent | tools/roles/house/policy.toml:26 | medium | medium | confirmed | Reproduced. `handoff.py stage-efforts spec-write --model claude-fable-5-2` printed builder, disposal, skeptic, specFinder, specWriter, synthesis, and `stage-efforts closing-review --model claude-fable-5-2` printed diffFinder, skeptic, synthesis, all medium. Neither prints `committer` (tools/workflows/unattended-build.js:494 ROLE_KEYS) nor `probe` (tools/workflows/tier2-review.js:520 ROLE_KEYS), because tools/roles/workflows.toml:37,47,67 hold neither key. Each harness then logs 'the agent type's own, else the session's' for them (unattended-build.js:571-573, tier2-review.js:736-737) and spawns without `effort` (renderStageOpts). The tables are unchanged from base, but the claim is new in this diff: policy.toml:26 'every one runs at medium', tools/roles/README.md 'every role and stage runs at `medium`', help/roles.md:54-55, against a build README whose goal is 'every role and every stage at medium'. The README limits paragraph names the case only as 'a harness stage the workflow table gives no key' and none of the specs names committer or probe, so the unqualified 'every' overclaims on a Fable session whose own effort is not medium. Contained to two small stages (a spec commit and a resume probe), so medium. The fix's first alternative is unsound: `stages` also feeds `harness-args` (handoff.py:477 unions the stages tables into `roles`), so mapping committer and probe to a role would retype them as role agents, against 'the committer has no role span' (unattended-build.js:1282) and the probe's Plan default (tier2-review.js:539), and the audit's forwarded efforts carry only skeptic, specFinder and synthesis (unattended-build.js:575), so the audit's probe would still get no level. | unsound | - | class:policy-value-with-no-route |
| 13 | intent | memory/builds/aProfiledEffort/build/2026-11-10-build-TOOL-aProfiledEffort-1-1-acceptance-ledger.md:5 | low | - | refuted | The facts cited are accurate, but they describe a step the build method schedules after this review, not a defect the diff introduced. Observed: both ledgers (memory/builds/aProfiledEffort/build/2026-11-10-build-TOOL-aProfiledEffort-1-1-acceptance-ledger.md:5 and the -2-1 ledger :5 and :16) say outright that arm 19 has not executed and that RED then GREEN is owed to the main loop at the close under a `Pass: none` commit; the commit bodies of 2edd5cc06 and d1ef90538 say the same; FLOOR_ASSERTIONS=55 at tools/roles/adopt-roles.test.sh:86; no such record exists at c1d1e19f4, whose subject is `phase REVIEWING`. memory/guides/BUILD-METHOD.md:199-202 forbids a pass from running any suite or self-test and assigns a new arm's RED-first observation to the main loop at the close (M8). M8 (:255-281) orders the close as checklist, then the adversarial review, then `Observe the owed arms before the bar`, then landing. Spec 1 :275-276 and :402-403 and spec 2 :273 and :396 write the same order in: the pass sets the spec CLOSED in its own commit and the main loop observes arm 19 at the close. So the range is in the prescribed state for round 1 of the closing review. Nothing in it certifies an unobserved check: spec 2's AC9 ledger line says the suite did not run and no `ok   arm 19` line has been seen. The finder itself concedes the effect is contained because the close and the bar precede the lander. This is a restatement of a pending, disclosed, method-mandated step, so it is by design. | sound | - | - |
