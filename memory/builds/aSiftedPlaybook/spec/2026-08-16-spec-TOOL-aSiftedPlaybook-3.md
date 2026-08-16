# TOOL-aSiftedPlaybook-3 — the playbook's claims about the repo become machine-checked

**Status:** SPECCED · rev-3 · 2026-08-16 · node a · Tier-2 · base 91ef1b05 · streams tooling

## 1. Goal

Every other unit in this build corrects a hand-kept claim that drifted from its source. Nothing
stops them drifting again, and the evidence says they will: four of the defects this build fixes are
recurrences of defects a previous build already fixed. Add one gate that holds the three classes.

## 2. Scope (IN)

One new gate, `tools/check-playbook-parity.sh`, with three check families and a sibling self-test.

- **S1 — kit coverage.** Every tracked kit dir under `tools/` is named in at least one of the three
  playbook files, or listed in a shrink-only `tools/playbook-kit-waivers.txt` with a reason. The kit
  set is DERIVED from the tree, never hand-listed. A waiver whose kit no longer exists reds as
  stale, so the file cannot outlive what it excuses.

  **The match is a path segment, anchored and case-sensitive** — `tools/<kit>/` or a backticked
  `<kit>/` — never a bare substring. A naive substring search makes this check pass vacuously:
  measured against the trio at BASE, the kit `lib` scores seven hits, every one of them the `lib`
  inside "deliberate" and "deliberately". A gate that certifies `lib` as documented on that evidence
  is the exact `vacuous-selector` shape this unit exists to prevent, committed by the unit itself.
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
- **S5 — the wiring.** A `tools/gate-legs.json` entry, the charter citation in `AGENTS.md`'s
  gate-suite section, and the codebase-map dossier claim for the new leg key.

## 3. Non-goals (OUT)

- **Checking prose for accuracy in general.** Undecidable. The gate holds three STRUCTURAL classes;
  a fluent paraphrase that is subtly wrong still passes, and the gate must say so in its own header
  rather than implying coverage it lacks — the same honesty `check-method-carriers.sh` already
  practises.
- **Enforcing `baseline.toml`'s shrink-only rule.** Discovered unenforced during this build (four
  written statements, zero mechanical checks, proved by simulation). It is a real finding and a real
  gap, but it is the codebase-map kit's invariant, not the playbook's. Follow-up row.
- **Extending the pair list beyond the two seeded rows.** Every additional pair is a judgement about
  what is worth pinning; growing the list is ordinary maintenance, not this unit's job.

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
| `tools/playbook-kit-waivers.txt` | new, seeded from the measured population |
| `tools/gate-legs.json`, `AGENTS.md`, `.memory-tree.conf` | wiring |
| `.claude/SESSION-KICKOFF.md` | `last-audit` re-stamp — `tools/gate-legs.json` is a watched pathspec |
| `memory/map/features/playbook.md` | the new leg key claimed — EXTENDED, never created (see Rollout) |
| `memory/map/generated/*` | regenerated by `gen_map.py --write`, never hand-edited |

### Rollout

**Lands last.** Every other unit changes the values this gate would pin, so building it first means
building it against values about to change.

**This unit EXTENDS `memory/map/features/playbook.md` and never creates it.** Three units need that
dossier — `TOOL-aSiftedPlaybook-1` F1 option 3, `TOOL-aSiftedPlaybook-2`'s new leg key, and this
one — and the README fixes the order as TOOL-1 → TOOL-2 → TOOL-3, so the minter is whichever of the
first two lands under a fork resolution that calls for it. If the dossier is absent when this unit
builds, it **reds and stops** rather than minting a second one; two dossiers claiming overlapping
keys is a coverage failure in both directions. It is also the only unit the owner may reasonably defer
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
  gate reds naming that kit. Observed by creating one, not asserted.
- **AC2** — When `MAX_LENSES` in `tools/hooks/agent-cap.js` is changed by hand and the template's
  stated bound is not, the gate reds naming that pair. This reproduces
  `PLAY-aSiftedPlaybook-1` S1's defect and is the unit's central proof.
- **AC3** — When a placeholder is added to one deploy file and `customize.md`'s counts are not
  updated, the gate reds naming the count that disagrees. Reproduces the 23 + 14 = 37 defect.
- **AC4** — When either side of a declared pair extracts nothing, the gate reds naming the pair as
  unresolvable — it never compares empty to empty and reports ok.
- **AC5** — When the kit derivation is broken by hand to return an empty set, the gate reds on the
  missing sentinel rather than reporting universal coverage.
- **AC6** — When a waiver row names a kit that no longer exists, the gate reds as stale.
- **AC7** — When `bash tools/check-playbook-parity.test.sh` runs it exits 0; when any single arm's
  assertion is inverted it exits non-zero naming that arm.
- **AC8** — When `python tools/memory-tree/check-arms.py` runs, the new gate is in its population
  with a declared `ARMS_FLOORS` entry, and an undeclared floor is its own refusal.

## 7. Gates

- `bash tools/check-playbook-parity.test.sh` — the new leg's own proof.
- `python tools/memory-tree/check-arms.py` — the new gate enters the meta-gate population.
- `python tools/codebase-map/test_codebase_map.py` — new leg key, coverage + freshness.
- `python tools/drift-audit/drift_report.py --check` — the charter citation, pin 0, zero tolerance.
- `bash skills/session-kickoff/manifest-check.sh` — `tools/gate-legs.json` is watched.
- `bash tools/run-gates.test.sh` — the canary over the changed manifest.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

- **F1 — should S2's pair list live in the gate, or in a declared data file?** In-script is simpler
  and keeps the extraction beside its pair. A data file (`tools/playbook-parity-pairs.tsv`) is
  editable without touching a merge-bar gate and matches the `gate-legs.json` precedent.
  **Recommendation: in-script.** The extractions are regexes, not data; a pair is a regex on each
  side plus a comparison, and splitting the regex from its pair puts half a mechanism in each file.
  Revisit if the list passes roughly ten rows.
- **F2 — does S1 red on a kit missing from the playbook, or only warn?** Redding means a new kit
  cannot land until the playbook mentions it, which is the forcing function the ceiling used to
  provide and is arguably the point. It also means an experimental kit cannot sit in `tools/`
  unmentioned even briefly.
  **Recommendation: red, with the waiver file as the escape hatch** — an experimental kit takes a
  one-line waiver, which is a visible, shrink-only, reviewable act rather than silence. This is the
  owner's call because it changes what it costs to add a kit.

## 9. Revision log

- rev-1 · 2026-08-16 · initial draft. The four-recurrence table is drawn from `aCandidStub`'s spec
  and review records plus this build's own findings; the unenforced `baseline.toml` convention was
  proved by simulation during `wf_4e13d9e7-550` and is recorded in §3 as an out-of-scope sibling gap.
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
  reason after whitespace, shrink-only, and a row whose target is gone reds as stale. Its header
  prose is the template for the new file's.
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
