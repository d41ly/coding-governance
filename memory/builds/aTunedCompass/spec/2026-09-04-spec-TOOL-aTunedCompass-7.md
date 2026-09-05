# TOOL-aTunedCompass-7 — the manifest declares the recall kit and narrows the tooling entrypoint

**Status:** SPECCED · rev-2 · 2026-09-05 · node a · Tier-1 · base c4fcf5ad · streams tooling · order 1 · ratified 2026-09-05

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Repair two defects in `memory/guides/SESSION-KICKOFF.md`, the project layer the kickoff engine treats
as authoritative over its own text. The manifest never names the recall kit, so one of the three
orientation probes is reached by a filesystem guess, and its pointer map hands the bug-class probe an
entrypoint so wide that the probe returns the catalogue instead of a checklist.

## 2. Scope (IN)

- **S1** — the manifest's live-probe block declares the recall kit at this repo's install prefix and
  carries its Step-4 invocation, in the same fenced block that already carries the two codebase-map
  commands. One block naming three probes, not a second block parallel to the first.
- **S2** — the declaration is PROJECT-LAYER PROSE. No template slot, no edit to
  `skills/session-kickoff/SKILL.md`, and no edit to `skills/session-kickoff/MANIFEST-TEMPLATE.md`.
  The engine's two-spelling fallback survives untouched and keeps working for adopters.
- **S3** — the pointer map's tooling row states its entrypoint as the kit directories the unit
  touches, so the argument the engine passes to the bug-class probe is a unit-scoped path set. The
  row keeps its existing reading guidance for a human.
- **S4** — the row enumerates no kit. A list of kit directories rots as kits land and nothing gates
  it, and the derivation the row asks for is already available to the session at Step 4.
- **S5** — the edit lands net non-positive against the manifest's byte cap. `wc -c` on the file
  before and after, and the margin `skills/session-kickoff/manifest-check.sh` reports, are both
  recorded in the unit's build note. What leaves to pay for the addition is F1.
- **S6** — the landing commit re-stamps `last-audit` and advances `last-body-change`, and its message
  carries the delta line §4 specifies.

## 3. Non-goals (OUT)

- Not a rendered manifest slot for the recall kit. That option was weighed and taken against once
  already, and §4 records where.
- Not adding the three probe paths to `watch:` or `verify-paths:`. §4 gives the reason for each list
  separately, because the two lists answer different questions.
- Not repairing the other three pointer-map rows, which anchor no bug class at all. That is a
  curation job in `memory/gotchas/` — writing classes for the playbook, kickoff and deployer areas —
  and no manifest edit can conjure a class that nobody has written.
- Not touching `tools/memory-tree/gotchas.py`. The parent build's measurement is explicit that the
  tool is fine and the entrypoint granularity is the defect.
- Not touching the backlog shard the session-start reading order names. Its size is parked at the
  build level and its remedy is an owner call.
- Not re-measuring the parent build's figures. Every number below is either cited from its report or
  measured fresh at writing time and labelled as such.

## 4. Design

### What the file says today

`grep -c recall memory/guides/SESSION-KICKOFF.md` returns 0, against 5 each for `codebase-map` and
`gotchas` (parent report, finding 12c). The live-probe block declares the map kit, states that no
environment variable is needed because the engine resolves this repo's install prefix itself, and
then fences two commands. The recall kit gets no clause anywhere in the file, so the engine's Step 4
falls through to probing two hard-coded directory spellings for `query.py`.

The pointer map's tooling row gives its entrypoint as the whole tools directory. Run against it, the
bug-class probe selects 30 classes plus 4 universal, about 8113 bytes; run against four specific kit
directories it returns 6 plus 4 (parent report, finding 12b). The tool answers the question it was
asked. The question was too wide.

### The recall declaration

The addition is one command line inside the existing fence plus a clause naming the kit in the
sentence above it. It is deliberately the same shape as the map declaration two lines up: the value
of the block is that a session reads one place and learns which orientation probes this repo has and
at which prefix. A second parallel block would cost more bytes and split one fact across two places.

### The tooling entrypoint

The engine passes the row's entrypoint cell to the bug-class probe. So the cell has to BE a usable
argument, not a pointer to one, and the honest argument for this stream is the kit directories the
unit touches. Step 3 closes the task scope before Step 4 runs, so by the time the probe fires the
session knows which kits are in scope. A session that genuinely cannot name one yet has not finished
Step 3, and running the probe over everything is not a substitute for finishing it.

### Neither `watch:` nor `verify-paths:` takes the probe paths

`watch:` holds the pathspecs the §B claims DERIVE FROM, and its purpose is C5: a watched file that
changes without a re-stamp reds the ratchet. The claim this unit adds is that the kit exists at this
prefix and is invoked at Step 4. That claim does not derive from the internals of
`tools/memory-recall/query.py`, and the invocation grammar it does depend on is the engine's, whose
file `skills/session-kickoff/SKILL.md` is already watched. Adding the probe files would re-stamp the
manifest on every commit to those kits — this build alone holds four units editing the recall kit —
for a claim none of them changes. The kit README's own guidance caps the list at about eight
pathspecs and it already holds ten.

`verify-paths:` is checked by C4 alone, which asserts the path is tracked content. The ratchet's
design record caps it at two to three anchors, it already holds four, and the liveness the three
probe paths need is owned elsewhere: hygiene check 15 rule 1 reds a backticked path cited under
`memory/guides/` that resolves to nothing, and this manifest sits inside that population.
Verified at writing time in `tools/memory-tree/corpus_ids.py` (`:295`), whose present-tense corpus
regex names the guides directory. A `verify-paths:` entry would be a second copy of a control that
already fires, and the cheap way to keep the new declaration honest is that the paths it names are
backticked in a file check 15 already grades.

Both lists therefore stay byte-unchanged, and the spec records the reason so a later reader does not
read the absence as an oversight.

### The ratchet stamp and its delta line

The manifest's own ratchet says a unit that changed what the file front-loads re-stamps `last-audit`
with a delta line in the commit message. This unit changes an entrypoint and adds a probe
declaration, so the stamp is owed. The delta line records exactly two facts and nothing else:

```
manifest delta: declared the recall kit's install prefix and its Step-4 invocation; narrowed the
tooling row's entrypoint from the whole tools directory to the kit dirs a unit touches.
```

`last-body-change` advances to the same sha, because the body changed and C9 counts watched commits
since that value. The stamp sha follows the file's stated rule — HEAD on the default branch, else the
merge base against the remote default — and the datetime always advances.

**What the gate does not do here, stated because a green ratchet will look like enforcement.** C5
fires on watched files changing without a re-stamp. This unit touches no watched path, so C5 is
silent whether or not the stamp is made. The re-stamp is owed by the manifest's prose rule, and the
only mechanical consequence of skipping it is C9's stall counter much later.

### Files touched (estimate)

`memory/guides/SESSION-KICKOFF.md`, and `memory/map/features/session-kickoff.md` if the dossier prose
goes stale against the edit. The dossier claims this guide as an inventory key, so it is the record
that describes the file this unit changes.

### Alternatives rejected

- **A rendered `{{MEMORY_RECALL}}` slot in the manifest template.** Weighed and taken against when
  the engine's hardcoded spelling was fixed: the build record for that fix states the two-spelling
  clause was taken over the manifest-slot option, priced as one clause against a new template slot
  plus a fill in every adopter's manifest. Re-opening it would cost every adopter an edit to buy this
  repo a declaration it can write in prose.
- **Enumerating the kit directories in the tooling row.** The list rots as kits land, nothing gates
  it, and a stale entrypoint list is worse than a wide one because it looks precise.
- **Raising `MAX_MANIFEST_BYTES`.** The gate's own failure message says the manifest must be trimmed
  rather than have the limit raised, and the value is overridable from the environment, so raising it
  in a leg invocation would widen the cap silently. It is an owner decision, and it is one of F1's
  options for that reason.

## 5. Production-readiness checklist

- security — N/A. One tracked prose file changes; no new input, path or credential surface.
- perf / scale — this is the perf change. The bug-class probe's selected set falls from 30 anchored
  classes and about 8113 bytes to the 6-plus-4 shape the parent measured against specific kit dirs.
- a11y — N/A. No user-facing surface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the entrypoint rule has one degenerate case, a session that cannot
  yet name a kit directory. It is a Step-3 failure and the row says so rather than offering a
  fallback that reinstates the catalogue.
- observability — the delta line in the commit message plus the advanced stamp are the record. There
  is no runtime signal to add.
- risks — the declaration goes stale if the recall kit moves prefix. Hygiene check 15 reds the dead
  citation, which is why §4 declines a second liveness control.
- testing + left-shift gates — `skills/session-kickoff/manifest-check.sh` and the memory-hygiene gate
  both grade this file already. This unit adds no gate, and there is no new class to gate: the class
  is "a manifest claim that no longer matches the tree", which is precisely what the ratchet is.
- migration / rollback — a prose revert. No adopter is affected, because no kit file changes.
- user docs — the manifest IS the doc. Refresh `memory/map/features/session-kickoff.md` on touch.

## 6. Acceptance criteria

- **AC1** — When `grep -c recall memory/guides/SESSION-KICKOFF.md` runs, it returns a count above
  zero, and the matching lines name `tools/memory-recall/query.py` as the Step-4 probe with this
  repo's install prefix.
- **AC2** — When the manifest's live-probe fence is read, it carries all three orientation probes —
  `tools/codebase-map/reuse_lookup.py`, `tools/memory-recall/query.py` and
  `tools/memory-tree/gotchas.py` — and the recall line shows the `--terms` argument the CLI refuses
  without.
- **AC3** — When `python tools/memory-tree/gotchas.py --for-paths` is run with the argument the
  tooling row now declares, for a unit touching one or two kits, it selects fewer than ten anchored
  classes, against the 30 the old entrypoint selected. Both runs are recorded in the build note.
- **AC4** — When `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit, it exits
  0 with no FAILED lines, C7 included, and its byte margin is reported in the build note.
- **AC5** — When the landing commit is read, its message carries the delta line, `last-audit` holds a
  datetime later than the previous stamp, and `last-body-change` names the same sha as `last-audit`.
- **AC6** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs, check 15 reports no new
  dead-path citation, which is the liveness control §4 relies on instead of a `verify-paths:` entry.
- **AC7** — When `git show` on the landing commit is read, the `watch:` and `verify-paths:` lines are
  unchanged.

## 7. Gates

`kickoff-manifest ratchet` · `memory hygiene` · `codebase-map coverage + freshness`

The full bar is `bash tools/run-gates/run-gates.sh`. This unit adds no gate and needs none: both
defects are inside a file two existing legs already grade, and the reason neither leg caught them is
that neither asks whether a declaration is COMPLETE, only whether what is written is true. That gap
is real and is not closed here.

## 8. Open questions


**F1 RESOLVED (owner, 2026-09-05): evict the second dated correction, 617 bytes.** The owner did NOT take
this fork's recommendation of the first correction. The same objection applies and must be recorded
rather than glossed: that entry's prune-when condition has not held either, so this is a deliberate
exception to the manifest's own prune rule and the eviction is recorded as a decision, not a lapse.
What the choice buys is headroom — it frees roughly 617 bytes against the 206 the edit needs, leaving
about 380 spare, where the recommended option left about 4. The backlog records this squeeze
recurring across three carriers, and a cap acting silently as an editor is the failure mode that
headroom prevents.

**F2 RESOLVED (owner, 2026-09-05): the entrypoint rule lives in the pointer-map row.** This was the fork's
recommendation, held open only because the row costs about 30 bytes more than the fence and F1 might
not have had them to spend. F1's answer frees enough that the objection is gone, so the machine-read
location wins over the cheaper one.

- **F1 — which bytes leave to pay for the addition?** Measured at writing time:
  `wc -c memory/guides/SESSION-KICKOFF.md` is 25571 against the 25600-byte cap in
  `skills/session-kickoff/manifest-check.sh` (`:169`), so the file has 29 bytes of headroom. The
  proposed edit is +235 bytes: 56 for the declaring clause, 117 for the command line, 62 for the
  entrypoint cell. So at least 206 bytes must leave, and every candidate has a cost.
  Options, each measured in this file: the first dated correction, 271 bytes, whose rule is already
  spelled in the gate fence three lines below it, but whose prune-when condition does NOT hold, so
  deleting it early breaks the file's own prune rule; the chunked-reporting comment in the gate
  fence, 228 bytes, which is live front-loaded prose about a green-by-absence hazard; the second
  dated correction, 617 bytes, whose prune-when has also not held; or raising the cap, which the
  gate's own message forbids and which the environment can override silently.
  Recommendation: evict the first dated correction and move its gotcha pointer into the gate fence
  line that already states the rule, which nets about 210 bytes. It is a recommendation and not a
  decision, because pruning a dated entry before its condition holds is a change to how this file
  governs itself. The backlog already records this exact squeeze as a pattern across three carriers,
  including one wanted addition to this manifest that was simply dropped at 361 bytes — a cap
  silently acting as an editor is the failure mode, and picking the victim is the owner's call.

- **F2 — should the entrypoint rule live in the row, or in the fence beside the command?** The engine
  passes the row's cell to the probe, which argues for the row. A reader looking for how to run the
  probe looks at the fence, which argues for the fence. Writing it in both places is two answers to
  one question and is refused. Recommendation: the row, because the row is what a machine reads and
  the fence line can point at it in a few bytes. Left open because F1 prices this: the fence option
  is cheaper by roughly 30 bytes and F1 may not have 30 bytes to spend.

## 9. Revision log

- rev-1 · 2026-09-04 · initial draft, authored by the aTunedCompass spec pass.
- rev-2 · 2026-09-05 · both forks resolved by the owner. The second dated correction is evicted rather than
  the first, against this spec's recommendation, and the exception to the prune rule is recorded as
  such; the entrypoint rule goes in the pointer-map row, which F1's headroom now affords.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declare a kit install prefix in the kickoff manifest so a
probe is not a filesystem guess"` returned no code seam to extend, which is the correct answer for a
prose edit to one guide. Its ranked head was `kit_rel` in `tools/memory-tree/gen_build_index.py`,
matched on the stem `kit`, followed by `derive_install_order` in `tools/govkit/govkit.py`; neither
bears on the mechanism. The two candidates that DO bear on it are dossier prose rather than code —
`.unattended.conf` from the unattended dossier and `registry.toml` from the govkit one — and both
name the same seam, which is a DECLARATION seam and not a function. The unattended driver stopped
probing two guessed kit paths by reading a declared CLI path from its project conf, and this unit
does that one layer up, in the project's own manifest, for the engine's Step 4. The manifest is the
seam this unit extends; nothing else is edited. The probe also named
`memory/map/features/session-kickoff.md` as the dossier to open, which is the record §4 marks for
refresh.

Recall terms used: `kickoff manifest declaration install prefix recall kit query.py gotchas
for-paths pointer map entrypoint watch ratchet`. The question was why the manifest declares a kit
rather than letting the engine probe two hard-coded directory spellings. It returned 39 hits, and two
bind this unit: the review finding that the kickoff Skill's recall probe hardcoded one spelling and
missed this repo's own prefix, and the build record for that fix, which states the two-spelling
clause was taken OVER a manifest-slot option because a slot costs a fill in every adopter's manifest.
That pair is why S2 forbids a template slot and confines the change to this repo's project layer.
