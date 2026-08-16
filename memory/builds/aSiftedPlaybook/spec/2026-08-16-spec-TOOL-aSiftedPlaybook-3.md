# TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked

**Status:** SPECCED · rev-10 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams tooling · ratified 2026-08-16

## 1. Goal

Every other unit in this build corrects a hand-kept claim that drifted from its source. Nothing
stops them drifting again, and the evidence says they will: four of the defects this build fixes are
recurrences of defects a previous build already fixed. Add one gate that holds the three classes.

## 2. Scope (IN)

One new gate, `tools/check-playbook-parity.sh`, with three check families and a sibling self-test.

- **S1 — kit coverage.** Every tracked kit dir under `tools/` is named in at least one of the three
  playbook files, or listed in `tools/playbook-kit-waivers.txt` with a reason. The kit set is
  DERIVED from the tree, never hand-listed. **The registry is a declared exemption list, not a
  shrink-only count** (see §8 F2): it must be able to gain a row for a genuinely experimental kit,
  and it drains through AC6's two arms instead — a row whose kit is gone reds as stale, and a row
  whose kit IS named in the playbook reds as redundant. A waiver therefore disappears when it stops
  excusing something.

  **The match is a path segment, anchored and case-sensitive** — `tools/<kit>/` or a backticked
  `<kit>/` — never a bare substring. A naive substring search makes this check pass vacuously:
  measured against the trio at BASE, the kit `lib` scores seven substring hits — six inside
  "deliberate"/"deliberately" and one inside **`stdlib`** at `parallel-coding-governance.template.md:109`.
  Two unrelated false-positive words, neither of which has anything to do with `tools/lib/`. A gate
  that certifies `lib` as documented on that evidence is the exact `vacuous-selector` shape this
  unit exists to prevent, committed by the unit itself.
- **S2 — value parity.** A declared pair list: each row names a value the playbook STATES and the
  source that OWNS it, plus the extraction for each side. The gate extracts both and compares.
  Seeded with the two pairs this build proved necessary — the lens-array bound against
  `MAX_LENSES` in `tools/hooks/agent-cap.js`, and the hook matcher string against
  `.claude/settings.json`.
- **S3 — catalogue arithmetic.** The placeholder counts stated in
  `parallel-coding-governance.customize.md` equal the measured sets: the per-file group sizes and
  the union total. This is the check that would have caught 23 + 14 = 37 against a stated 36.

  **The intersection is checked structurally, not arithmetically.** The file states two counts and a
  total, never an intersection size, so there is no third number to compare — an arithmetic check on
  it would compare against nothing and pass. Instead: the placeholder the file names as shared
  appears in BOTH group listings, and the measured intersection contains exactly that placeholder.
  This depends on `PLAY-aSiftedPlaybook-4` S1/S2 having named it; if that unit did not land, S3
  reds rather than skipping.
- **S4 — the self-test.** `tools/check-playbook-parity.test.sh`, red and green observed per arm, plus
  an `ARMS_FLOORS` entry in `.memory-tree.conf`.
- **S5 — the wiring, for TWO legs, not one.** This unit ships a gate AND a self-test, and the
  charter's convention — which `TOOL-aSiftedPlaybook-2` §4 invokes to insist its own test be wired —
  makes both merge-bar legs. So: **two** `tools/gate-legs.json` entries, **two** inventory keys
  claimed in `memory/map/features/playbook.md`, and **two** script paths cited in `AGENTS.md`'s
  gate-suite section, where `_charter_mentions_every_leg` runs at pin 0 with zero tolerance. An
  earlier draft said one of each throughout, which would have left the self-test leg unclaimed and
  uncited and redded two gates.

## 3. Non-goals (OUT)

- **Checking prose for accuracy in general.** Undecidable. The gate holds three STRUCTURAL classes;
  a fluent paraphrase that is subtly wrong still passes, and the gate must say so in its own header
  rather than implying coverage it lacks — the same honesty `check-method-carriers.sh` already
  practises.
- **Enforcing `baseline.toml`'s shrink-only rule.** Discovered unenforced during this build (four
  written statements, zero mechanical checks, proved by simulation), and **the owner then relied on
  that gap deliberately** in resolving `TOOL-aSiftedPlaybook-1` F1 to an in-place key swap. A gate
  written here would red that resolution on the day it landed, so this stays firmly out of scope and
  becomes a follow-up row rather than a quiet addition. If the convention is ever to be enforced, the
  swap it would have caught needs a waiver first — which is the ordering, not a reason to skip it.
- **Extending the pair list beyond the two seeded rows.** Every additional pair is a judgement about
  what is worth pinning; growing the list is ordinary maintenance, not this unit's job.
- **Seeding or extending `tools/playbook-kit-waivers.txt`.** `PLAY-aSiftedPlaybook-3` S7 owns its
  contents. This unit only READS it. Stated as a non-goal because the alternative is live: if this
  gate re-seeded "from the measured population" at its own build time it would either overwrite
  PLAY-3's curated rows, or — with PLAY-3 not yet landed — waive all four of the kits PLAY-3 exists
  to add, and then certify coverage that does not exist. Same resolution as the map dossier, one
  file over.

## 4. Design

### Why one gate and not three

The three families share a failure mode — a hand-kept copy of something the tree already knows — and
share the anti-vacuity discipline below. Splitting them would triple the wiring cost (three leg
entries, three charter citations, three dossier claims) for no separation of concern. This mirrors
`tools/unattended/check-unattended.sh`, which carries thirteen checks under one leg.

### Anti-vacuity is the load-bearing design constraint

`parallel-coding-governance.domain-rules.md:98` names the exact failure this gate is most likely to
have: "a coverage check that greps for a literal the real code never spells … matches the empty set
and passes checking nothing". Three arms, not one, guard against it:

1. **Every S2 pair must extract a NON-EMPTY value on BOTH sides.** An extraction that matches
   nothing reds by name — it never silently compares empty to empty.
2. **The S1 kit set must be non-empty and must contain a hand-frozen SENTINEL member**
   (`memory-tree`, which cannot plausibly leave). An empty or broken derivation reds by name rather
   than reporting universal coverage.
3. **S4 proves each arm reds** by feeding it a synthetic violation, per `domain-rules.md:44-45`.

### The derivation is read, not rewritten

`tools/codebase-map/map_extractors.py` and `tools/check-install-prefix.sh:38` already enumerate
`tools/*` kit dirs. A third enumeration would be a third thing to drift —
`domain-rules.md:99`'s "a gate's OWN vocabulary hardcoded as a mirror of the codebase's real exports
drifts silently". This gate reads one of the existing two.

### The evidence: four recurrences, not a hypothetical

| Fixed once by | Recurred as |
|---|---|
| `aCandidStub` S2 — "§8 stops prescribing a denied script", because a script written to it exits 2 under the hook | `PLAY-aSiftedPlaybook-1` S1 — the same line prescribes a 6-element lens fan the hook denies |
| `aCandidStub` S4 — the companion header reconciled against the drop list | `PLAY-aSiftedPlaybook-4` S3 — the same header, the same drop list, drifted on shape instead of count |
| The kit-version count, de-numbered in `AGENTS.md` | The hygiene check count — the commit that de-numbered the charter called it "the third count to rot this way" |
| `aCandidStub` review id 19 — kit omissions raised and refuted | `PLAY-aSiftedPlaybook-3` — the omission persisted and grew a fourth member |

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/check-playbook-parity.sh` | new |
| `tools/check-playbook-parity.test.sh` | new |
| `tools/playbook-kit-waivers.txt` | **consumed, never created** — `PLAY-aSiftedPlaybook-3` S7 seeds it; this gate reds and stops if it is absent, and never adds a row |
| `tools/gate-legs.json`, `AGENTS.md`, `.memory-tree.conf` | wiring |
| `tools/govkit/registry.toml` | the two new depth-1 `tools/` paths above DECLARED — an entry's file rules or an `[[exempt]]` row each. Undeclared, `govkit selfcheck` reds; AC10 observes it and §7 runs it, and this row is the third carrier so all three receivers of that obligation match |
| `memory/guides/SESSION-KICKOFF.md` | `last-audit` re-stamp — `tools/gate-legs.json` is a watched pathspec |
| `memory/map/features/playbook.md` | the new leg key claimed — EXTENDED, never created (see Rollout) |
| `memory/map/generated/*` | regenerated by `gen_map.py --write`, never hand-edited |

### Rollout

**Lands last, and `PLAY-aSiftedPlaybook-3` is a hard prerequisite** — it seeds
`tools/playbook-kit-waivers.txt`, without which S1 has no exemption registry to read. Every other
unit changes the values this gate would pin, so building it first means building it against values
about to change.

**This unit EXTENDS `memory/map/features/playbook.md` and never creates it.** The owner resolved
`TOOL-aSiftedPlaybook-1` F1 to the in-place `baseline.toml` swap, so that unit mints no dossier and
**`TOOL-aSiftedPlaybook-2` is the minter**. If the dossier is absent when this unit builds, it
**reds and stops** rather than minting a second one; two dossiers claiming overlapping keys is a
coverage failure in both directions. It is also the only unit the owner may reasonably defer
indefinitely without leaving the tree inconsistent — the others fix falsehoods, this one prevents
future ones.

### Alternatives rejected

- **Extend `kit-dogfood-parity.test.sh` instead of a new gate.** Rejected: that harness compares a
  rendered file against its template byte-for-byte. This gate compares an extracted VALUE against a
  differently-shaped source. Same word, different mechanism; overloading it would make one file do
  two unrelated jobs and make its name a lie.
- **A drift-audit signal instead of a gate leg.** Rejected: `signal_shrink_only` and its siblings are
  `gateable=False` by construction — they report. Every defect in this build was reportable for days.
  The class needs a red, not a row.

## 5. Production-readiness checklist

- security — N/A.
- perf / scale — three greps and a set comparison; sub-second, scheduled early.
- a11y / i18n — N/A.
- error / empty / loading states — an unresolvable pair, an empty extraction and an empty kit set
  each have their own named failure message. See §4's anti-vacuity arms.
- observability — the gate prints the offending pair or kit by name, never a bare count.
- risks — **the gate itself is the risk.** A parity gate that passes vacuously is worse than no gate
  because it certifies coverage that does not exist, and this repo has landed that defect before —
  `domain-rules.md:98` exists because of it. §4's three arms and S4's self-test are the response,
  and a `fail` message carrying a bare positional cannot be armed, so every value binds to a name
  and sits after the literal sentence. A second authoring trap applies directly: this gate is mostly
  regexes, and generating its source through a shell heredoc into a non-raw string turns an escape
  into a control byte, after which the compiled pattern silently stops matching and only `repr()`
  shows it. Write the gate with a file tool.
- testing + left-shift gates — S4 IS the left-shift; this unit is the left-shift for the rest of the
  build.
- migration / rollback — new files plus wiring; revert cleanly. No adopter impact — this gate is
  gov-internal and checks gov's own copy of the playbook.
- user docs — the gate's own header documents what it does and does not catch.

## 6. Acceptance criteria

- **AC1** — When a kit dir is added under `tools/` and named in no playbook file and no waiver, the
  gate reds naming that kit. Observed by creating one, not asserted. **Quantified over the live
  derivation, never a count** — a twelfth kit (`govkit`) arrived from main mid-build and a spelled
  number did not notice; `PLAY-aSiftedPlaybook-3` S9 gives it a disposition and AC9 there re-derives
  the same population this gate reads.
- **AC2** — When `MAX_LENSES` in `tools/hooks/agent-cap.js` is changed by hand and the template's
  stated bound is not, the gate reds naming that pair. This reproduces
  `PLAY-aSiftedPlaybook-1` S1's defect and is the unit's central proof.
- **AC3** — When a placeholder is added to one deploy file and `customize.md`'s counts are not
  updated, the gate reds naming the count that disagrees. Reproduces the 23 + 14 = 37 defect.
- **AC4** — When either side of a declared pair extracts nothing, `bash tools/check-playbook-parity.sh`
  reds naming the pair as unresolvable — it never compares empty to empty and reports ok.
- **AC5** — When the kit derivation is broken by hand to return an empty set,
  `bash tools/check-playbook-parity.sh` reds on the missing `memory-tree` sentinel rather than reporting universal coverage.
- **AC6** — When a waiver row names a kit that no longer exists, the gate reds as stale. When a
  waiver row names a kit that IS present in the playbook, it also reds — otherwise a waiver that
  excuses nothing would otherwise sit in the registry forever, which is how `workflows/` nearly
  shipped one. This arm is also what lets the registry accept a new row safely (§8 F2) — it can
  grow, but only for a kit that genuinely needs excusing.
- **AC9** — When `tools/playbook-kit-waivers.txt` is absent, the gate reds naming it and stops. It
  never creates or extends the file; `PLAY-aSiftedPlaybook-3` S7 owns its contents.
- **AC7** — When `bash tools/check-playbook-parity.test.sh` runs it exits 0; when any single arm's
  assertion is inverted it exits non-zero naming that arm.
- **AC8** — When `python tools/memory-tree/check-arms.py --report` runs, the new gate is in its
  population with a NUMERIC `ARMS_FLOORS` floor rather than `unset`. **An undeclared floor is not a
  refusal** — `check-arms.py` skips a gate it finds no entry for — so this AC reads the report
  directly rather than trusting the gate to complain.
- **AC10** — When `python tools/govkit/govkit.py selfcheck` runs, it is green with both new depth-1
  paths (`tools/check-playbook-parity.sh` and its `.test.sh`) declared in
  `tools/govkit/registry.toml`.

## 7. Gates

- `bash tools/check-playbook-parity.test.sh` — the new leg's own proof.
- `python tools/memory-tree/check-arms.py` — the new gate enters the meta-gate population.
- `python tools/codebase-map/test_codebase_map.py` — new leg key, coverage + freshness.
- `python tools/drift-audit/drift_report.py --check` — the charter citation, pin 0, zero tolerance.
- `bash skills/session-kickoff/manifest-check.sh` — `tools/gate-legs.json` is watched.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `python tools/govkit/govkit.py selfcheck` — two new depth-1 paths must be declared.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none — both forks below are RESOLVED (agent, 2026-08-16, delegated). The owner delegated resolver
authority for these two on 2026-08-16; neither needed a §3 non-goal changed, a new dependency or
install location, or any widening of a write surface, so M3's vetoes 2 and 3 do not reach them and
they did not have to go back.

- **F1 — should S2's pair list live in the gate, or in a declared data file?**
  **RESOLVED (agent, 2026-08-16, delegated): IN-SCRIPT.** Neither option is more feature-rich —
  both satisfy every stated AC and leave the same follow-ups — so M3's tie-break decides it, and its
  second clause is "reuse of a seam M5 found". §10 already names that seam:
  `kit-dogfood-parity.PAIRS` at `tools/memory-tree/kit-dogfood-parity.test.sh:53` is an in-script,
  space-separated pair list iterated with per-pair diagnostics, and this unit was already going to
  copy its shape. Extracting the pairs to `tools/playbook-parity-pairs.tsv` would reuse nothing and
  split one mechanism across two files: a pair here is a regex per side plus a comparison, and a
  regex is not data.

  **Revisit trigger, so this is a decision and not a permanent posture:** if the pair list passes
  ten rows, or if a pair is ever needed by a second consumer, the data-file option becomes the
  better one and this fork reopens.
- **F2 — does S1 red on a kit missing from the playbook, or only warn?**
  **RESOLVED (agent, 2026-08-16, delegated): RED, by veto — this fork was never actually open.**
  M3's veto 1 discards any option that "fails an acceptance criterion or gate already written in the
  spec", and **AC1 already reads "the gate reds naming that kit"**. The warn-only option contradicts
  this unit's own acceptance criterion, so it was disqualified from the moment AC1 was written and
  the fork should have been closed then. A fork whose options are already decided by the spec that
  states them is not a fork; leaving it open invited an answer the spec would then have refused.

  The escape hatch stands: an experimental kit takes a one-line row in
  `tools/playbook-kit-waivers.txt`, which is a visible and reviewable act rather than silence.

  **One consequence, and it corrects a real contradiction this resolution exposed.** The registry
  was described as *shrink-only* in S1, in §10 and in `PLAY-aSiftedPlaybook-3` S7 — but a
  shrink-only file cannot GAIN the row the escape hatch depends on. Both cannot be true. The
  registry is therefore **not a shrink-only count**; it is a declared exemption list with two
  draining arms, already specced as AC6: a row whose kit no longer exists reds as stale, and a row
  whose kit IS named in the playbook reds as redundant. Those drain it without a count pin, and they
  drain it for the right reason — a waiver disappears when it stops excusing something, not when a
  number says so. This is where it diverges from `tools/install-prefix-waivers.txt`, whose entries
  can only ever be removed.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. The four-recurrence table is drawn from `aCandidStub`'s spec
  and review records plus this build's own findings; the unenforced `baseline.toml` convention was
  proved by simulation during `wf_4e13d9e7-550` and is recorded in §3 as an out-of-scope sibling gap.
- rev-10 · 2026-08-16 · folded round-4 L4. The `govkit selfcheck` obligation reached all three
  receiving units but sat in a different subset of sections in each: this unit had the §7 gate line
  and AC10 but no `tools/govkit/registry.toml` row in §4 Files touched. Added, so the next reader
  does not have to re-derive which subset is load-bearing. (Round 4's fold list named rev-9 as the
  target; this spec was already at rev-9, so the bump is to rev-10 — the review computed from the
  rev round 3 had asked for rather than the one that landed.)
- rev-9 · 2026-08-16 · folded round-3 B1's tail. AC1 now says explicitly that it quantifies over the
  live kit derivation rather than any count, which is what a twelfth kit arriving mid-build proved
  necessary.
- rev-8 · 2026-08-16 · folded round-3 H2, M2 and B2. AC8 repeated the false "an undeclared floor is
  its own refusal" premise — `check-arms.py` silently skips one — so it now reads `--report`
  directly. The waiver key grammar is pinned (bare kit name, verbatim), because S1 derived bare names
  while `PLAY-3` S7 spelled them with a trailing slash and nothing said which joins. Both new depth-1
  `tools/` paths need `govkit/registry.toml` declarations or the `govkit selfcheck` leg reds.
- rev-7 · 2026-08-16 · both forks RESOLVED under delegated authority, per M3. F1 → in-script, on
  the tie-break's "reuse of a seam M5 found" — §10 already named `kit-dogfood-parity.PAIRS` and a
  data file would reuse nothing; a revisit trigger is stated so it is a decision, not a posture.
  F2 → red, by veto 1: AC1 already read "the gate reds naming that kit", so the warn-only option
  contradicted this spec's own acceptance criterion and the fork had been closed since AC1 was
  written. Resolving it exposed a contradiction now fixed in S1, §10 and `PLAY-3` S7 — the waiver
  registry cannot be BOTH shrink-only and the escape hatch a red requires, so it is a declared
  exemption list that drains through AC6's two arms instead of through a count.
- rev-6 · 2026-08-16 · folded round-2 mediums and lows. S5 wired ONE leg where this unit ships two
  (the gate and its self-test), which would have left the self-test unclaimed in the map and uncited
  in the charter — two reds, one of them zero-tolerance. S1's `lib` evidence corrected: six hits are
  "deliberate", the seventh is `stdlib`, which makes the point better.
- rev-5 · 2026-08-16 · folded round-2 audit finding H4. `tools/playbook-kit-waivers.txt` had TWO
  declared creators — this spec's Files-touched row and `PLAY-aSiftedPlaybook-3` S7 — and since the
  README lets this unit be deferred indefinitely, a re-seed here would have either overwritten
  PLAY-3's curated rows or permanently waived the four kits PLAY-3 exists to add, with the gate then
  certifying coverage that does not exist. Resolved the same way rev-3/rev-4 resolved the identical
  collision for the map dossier: consumed, never created. Added AC9 for the refusal, a non-goal
  banning row additions, PLAY-3 as a stated prerequisite, and an AC6 arm that drains a waiver whose
  kit IS named.
- rev-4 · 2026-08-16 · absorbed the owner's `TOOL-aSiftedPlaybook-1` F1 resolution. The minter of
  `memory/map/features/playbook.md` is now fixed as `TOOL-aSiftedPlaybook-2`, not "whichever lands
  first". Sharpened the `baseline.toml` non-goal: the convention is not merely unenforced, it was
  deliberately relied upon, so gating it here would red an owner decision — the waiver has to come
  first if it is ever gated.
- rev-3 · 2026-08-16 · folded the spec audit `wf_4ed62ebb-cef`, three findings. S1 never specified
  its match rule, and a substring match would have certified `lib` as documented on seven hits of
  the `lib` inside "deliberately" — the vacuity class this unit exists to catch, inside this unit.
  S3 compared an intersection the customize file never states, so that comparand was a
  compare-against-nothing; it is now structural. Named this unit as the EXTENDER of the map dossier,
  since three units wanted it and only two had noticed each other. Added the manifest re-stamp and
  the regenerated map artifacts to Files touched.
- rev-2 · 2026-08-16 · added the heredoc-to-control-byte authoring trap to §5, selected by
  `gotchas.py --for-diff` over this build's own first commit. This gate is mostly regexes, which is
  the exact population that class destroys silently.

## 10. Reuse audit

**Two existing seams are extended rather than reinvented**, both found via
`python tools/codebase-map/reuse_lookup.py "template size ceiling gate enforcement"`:

- `tools/install-prefix-waivers.txt` is the model for S1's waiver file: one `<key>` per row with a
  reason after whitespace, and a row whose target is gone reds as stale. **The key grammar is pinned
  here and nowhere else**: the BARE kit directory name exactly as the derivation yields it (`lib`,
  `hooks` — no trailing slash, no path prefix), compared verbatim. `install-prefix-waivers.txt`'s own
  keys are `<path>:<line>`, a different shape, so "modelled on" settles the row layout and not the
  key; a waiver whose key does not join leaves its kit unexcused and reds AC1, which is the
  vacuous-selector class S1 exists to prevent. Its header prose is the
  template for the new file's. **One deliberate divergence** (§8 F2): `install-prefix-waivers.txt`
  is shrink-only and can only lose rows, while this registry must be able to gain one for an
  experimental kit, so it drains through AC6's two arms rather than through a count.
- `kit-dogfood-parity.PAIRS` (`tools/memory-tree/kit-dogfood-parity.test.sh:53`) is the model for
  S2's declared pair list — a space-separated `a:b` pair set iterated with per-pair diagnostics.
  The SHAPE is reused; the comparison is not, for the reason in §4 Alternatives rejected.

The kit enumeration for S1 is read from `tools/codebase-map/map_extractors.py` or
`tools/check-install-prefix.sh:38`, never re-derived — recorded here because writing a third
enumeration is the specific defect `domain-rules.md:99` describes, and a gate that commits it while
checking others for it would be the funniest possible outcome.

Recall terms used, recorded per M5: `template size gate byte ceiling externalize companion
domain-rules headroom strict limit raise refuse stub`. No prior record proposes this gate; the
nearest prior art is `tools/memory-tree/check-method-carriers.sh`, which solves the structurally
identical problem one corpus over — every file pointing at the build method is declared in a
per-repo registry and points rather than copies — including its honest statement that it catches a
copied section and not a fluent paraphrase.
