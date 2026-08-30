# Architecture recommendations for this build — flexibility and performance

**Serves:** research TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-6

The prompt's last bullet asks for these explicitly. Each one is a RECOMMENDATION with the
observation behind it; three of them change a spec that is already written, and those are marked
**AMENDS**. Written before any code, so the amendments cost an edit rather than a rewrite.

## R1 — AMENDS unit 2: the emitter will destroy every comment, and merge-by-name will not save them

**This is the most important finding in this record and it invalidates the naive shape of the whole
build.** `tools/govkit/govkit.py` EMITS a target's leg manifest from the selected kits'
`[[gate_leg]]` descriptor rows, merging by `dedupe_key = "name"` — verified at `govkit.py:2949`.
Merge-by-name means an adopter's hand-authored legs SURVIVE an emit, which is the property that
makes "adopters declare their additional legs themselves" work today.

It does not extend to comments. A writer that parses TOML, merges rows and re-serialises produces a
file with no comments at all, because `tomllib` is a READER and Python ships no comment-preserving
TOML writer in the standard library. So the first `govkit apply` after this build lands would
silently delete every argument this build exists to make storable — including the whole of
`gate-profiles.txt`'s reasoning, which unit 2 §S4 carries across verbatim.

**Recommendation: the file gets a MARKER REGION, and the emitter only ever rewrites between the
markers.** The same mechanism this repo already uses for `<!-- gen:build-index -->` in a build
README and for the `<!-- roster:units -->` pair, applied to a TOML file with `#` comment markers:

```toml
# ---8<--- gov:emitted-legs — govkit rewrites everything between these two markers.
# Legs OUTSIDE the region are yours and are never touched.
[[leg]] …
# ---8<--- /gov:emitted-legs
```

The emitter then does a TEXTUAL splice rather than a parse-merge, which is the only operation that
preserves the comments in the authored half by construction rather than by care. The `[bar]` table,
the `[[profile]]` rows and the `[[lane]]` rows sit OUTSIDE the region and are owner-owned, which is
also what makes `enforce_ceilings` and `turnstile` genuinely the owner's switches rather than
something an emit can reset.

**Second-order consequence, and it is a benefit:** the comments on an EMITTED leg then have to live
in the kit descriptor that emits it, not in the manifest — which is correct, because that is where
the argument for a kit's leg belongs and is where a reader looking at the kit will find it.

## R2 — AMENDS unit 6: govkit will REFUSE this format, by name, and that is a scope item

`govkit.py:2947` refuses any `[gate_runner].grammar` other than `json-array`, with the message
`only 'json-array' is implemented`. It is a good refusal — it fails closed and names itself — and it
means unit 6 cannot merely point the emitter at a new filename. A `toml-legs` grammar is a genuine
addition to that validator and its writer, and unit 6 §S1 currently reads as if it were a path
change.

**Recommendation: unit 6 §S1 is split.** The grammar addition is its own sub-spec with its own
acceptance, because it is the piece an adopter's deployer route depends on, and it is the piece that
interacts with `TOOL-aFlaggedScaffold-3` — already recorded in units 6 and 7 as the prerequisite that
is NOT in this roster.

## R3 — AMENDS unit 2: ship the lane MECHANISM, do not assign 86 legs to lanes

Unit 2 introduces `[[lane]]` rows and a per-leg `lane`. gov's 86 legs today have no fast/heavy
distinction at all — every leg goes through one pool. Assigning them to lanes inside the commit that
changes the file format buries a BEHAVIOUR change inside a FORMAT change, and the closing review
then cannot tell which half a finding lands on. That is M2's "one mechanism per spec" applied to a
migration.

**Recommendation: every gov leg lands in one `heavy` lane, so the migration is provably
behaviour-neutral, and lane assignment becomes a later unit that reads
`<git-dir>/gate-ledger.tsv`.** Behaviour-neutrality is then assertable — same legs, same order, same
pool — which is exactly what unit 2's AC7 parity arm is for. This mirrors `gate-profiles.txt`'s own
`modest` row, which the profile table's comment says was made deliberately behaviour-neutral for the
same reason: *a knob whose first landing is also its first behaviour change has no control.*

## R4 — the performance lever is SHARDING, not concurrency, and the numbers say so

The bar's recorded shape on node `d`, 2026-08-23: 4926 s of leg-sum, longest leg 1565 s. **Wall
clock cannot fall below the longest leg however wide the pool is**, so 26 minutes is a floor that no
concurrency change can touch. Fifty of the ninety-two legs then present finished in under five
seconds each — the distribution is a handful of suites and a long tail of nothing.

Concurrency is also already at its measured optimum: `gate-profiles.txt`'s `capable` row states that
width 16 was tried and each leg dilates under load faster than the extra worker repays.
`TOOL-aScannedThrottle-6` measures the dilation at 1.5–1.85x inside the pool.

**Recommendation: land unit 3 (`--leg`) in the SAME release as unit 2, not after it.** Every
acceptance criterion in units 4, 5, 6 and 7 is verified by running a leg. Without `--leg` each of
those verifications costs a 26-minute floor; with it, each costs that leg's own seconds. The
sequencing that looks natural — declaration first, then the argument surface — is the expensive one.

## R5 — a declared ceiling with enforcement off will rot, so make `--manifest` grade it

Unit 4 turns enforcement off and keeps all 86 declarations. Nothing will then notice when a ceiling
drifts away from what its leg actually costs, and the owner who later turns enforcement ON meets the
2041-versus-2040 failure at the worst possible moment — a bar killed on a number nobody has looked
at in months.

`<git-dir>/gate-ledger.tsv` already carries one row per leg with its own measured seconds. The join
is free.

**Recommendation: `--manifest` prints, per leg, the declared ceiling AND the ledger's measured
seconds AND their ratio, flagging any leg whose ceiling is below 3x its measurement.** It reports;
it does not red. That is the cheapest possible guard against re-running the incident, and it fits
inside unit 3's verb rather than needing a unit.

## R6 — with the turnstile off, `push-main.sh`'s retry loop becomes the new cost

Unit 5 ships the turnstile disabled, so two concurrent landings both run the full bar. Whichever
loses the push race re-reconciles and RE-GATES, bounded by `GOV_PUSH_MAIN_MAX_RETRIES` at 3. On a
26-minute floor that is up to 78 minutes of gating for one landing, and the turnstile existed partly
to prevent exactly that.

The retry's tree differs from the first attempt's by ONE merge commit — the reconcile. A full bar on
that tree re-proves everything the first full green already proved plus the merge.

**Recommendation: after a first FULL green, a push-main retry runs the bar SCOPED to the reconcile
merge's diff.** `.githooks/pre-push` already has the machinery: it decides whether a full bar is
owed against a recorded green and a declared staleness bound. This is a follow-up unit rather than
scope creep here, and it is recorded so the turnstile flip does not silently move the cost from
"waiting in a queue" to "gating three times".

## R7 — NicoCares migrates first, and inCMS becomes migratable only because of unit 2

NicoCares already runs `run-gates` at 1.3; its migration is a data conversion and unit 7's
`--upgrade` does it in one command. inCMS is a runner swap, and today it is not even possible: its
66 legs use `cwd`, `phase` and `tool`, and gov's runner implements none of them.

**Recommendation: this is the argument for building `cwd`, `lane` and `tool` NOW rather than
deferring them as unasked-for expressiveness.** They are not speculative generality — they are the
exact three fields that stand between the fleet's largest adopter and the single runner the prompt
asks for. Stated here because "ship the minimum" would otherwise correctly cut all three.

## R8 — add no gate leg

Every one of the six Tier-2 specs says "No new leg", and that is deliberate rather than incidental.
The bar is the thing being made cheaper; adding legs to it while doing so is self-defeating, and
each of the new arms has an existing suite that is already a leg. Recorded so a later reviewer does
not read the absence as an oversight.

## R9 — the ordering, and what it buys

| step | units | why here |
|---|---|---|
| 1 | 2 + 3 together | R4: the shard is what makes everything after it verifiable at a sane cost |
| 2 | 4, then 5 | both are one-line defaults over unit 2's `[bar]` table; independent of each other |
| 3 | 6 | needs 3 for `--leg`, and R2's grammar work is the long pole |
| 4 | 7 | needs the format settled; nothing else needs it |

Units 4 and 5 are the only genuinely parallel pair — disjoint write sets, no shared contract beyond
the `[bar]` table each adds one key to. Their `--dispatch` declaration is the one this build should
make; everything else sequences.

## What this record does NOT claim

- No measurement was taken on this tree today. Every number above is read from a record — the
  charter's merge-bar section, `TOOL-aScannedThrottle-6`, `gate-profiles.txt`'s own comments — and
  each is cited so a reader can re-derive rather than trust it.
- R6's 78-minute figure is arithmetic on a recorded floor, not an observation. No push-main retry
  storm has actually been measured with the turnstile off, because the turnstile has never been off.
- Whether a textual splice (R1) survives every TOML shape an adopter might write is UNVERIFIED. The
  marker region makes it a string operation, which is why it is recommended, but a leg row spanning
  the marker would break it and unit 2 owes that refusal.
