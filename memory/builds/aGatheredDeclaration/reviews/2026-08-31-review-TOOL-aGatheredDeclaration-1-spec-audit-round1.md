**Serves:** spec-audit TOOL-aGatheredDeclaration-1 TOOL-aGatheredDeclaration-2 TOOL-aGatheredDeclaration-3 TOOL-aGatheredDeclaration-4 TOOL-aGatheredDeclaration-5 TOOL-aGatheredDeclaration-6 TOOL-aGatheredDeclaration-7

# Spec audit — aGatheredDeclaration, round 1

Reviewed 2026-08-31 on node `a`, in worktree
`.claude/worktrees/gate-bar-tooling-review-020565`, against the working tree at base `44734f15`.
The seven specs were audited AS SPECS — underspecification, sibling contradiction on M2's four axes
(scope, interface, ordering, acceptance), unstated assumptions, and prior art the specs missed.
Every source citation below was re-derived against the tree at this base rather than carried from a
finder's claim.

**Range · ROUND 1.**
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-1.md@ac944c5d2475575e2d5d839368cc57cd10cf56ef` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-2.md@d731f6a8ba7199d8e68dc72bbcb5c03fee6ede34` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-3.md@bf8d99de8af8799ef7e4ff748c61fdc8cfc93581` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-4.md@59fdcac33fad58f3d6247b65c5944402152460b4` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-5.md@00f09d403bd19dfed1be6099299dc19854ead1f9` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-6.md@cab7390208416e9497bfaef9c431101f796f11b9` ·
`memory/builds/aGatheredDeclaration/spec/2026-08-31-spec-TOOL-aGatheredDeclaration-7.md@099e4cdb1efa7245465c3652bf034fc9593cb58c`

## Verdict: BLOCKED

Five blockers. Three of them (F1, F2, F3) red a leg that runs on EVERY bar at the landing of the
unit that causes them, so the build as specced cannot reach a green. The other two are an
unsatisfiable acceptance pair and a silent interpreter-floor rise in the one kit whose stated purpose
is that it travels with nothing. None of the five is a design disagreement; each is a spec that does
not yet say what the implementer has to do.

## Review shape

Raw 76 · confirmed 32 · refuted 44 · unverified 0 · precision 0.42.

The 32 confirmed findings de-duplicate to **29 rows** below: three pairs were the same defect reached
from two directions and are merged (25+62, 27+66, 35+55), with their source ids named on each row.
Precision at 0.42 is at the bottom of the useful band the charter names; the refuted half was
dominated by lens claims about runner behaviour that the runner's own header already answers, which
is a priming problem rather than a scope one.

**Severity criterion, stated so the ranking is readable.** BLOCKER — a merge-bar leg reds at the
unit's own landing, or two criteria in the reviewed set cannot both pass. HIGH — nothing in the
build catches it: a could-not-fail acceptance criterion, a guard disarmed by absence, or a sibling
contradiction the ACs are blind to. MEDIUM — a real gap that an existing acceptance criterion or gate
WILL catch during the build, at the cost of a rework loop rather than a wrong landing.

## Findings

| # | Sev | Unit | Address | Defect |
|---|---|---|---|---|
| F1 | BLOCKER | 6 | §4 Inventory, S7 | `check-testsuite-counts.sh` hard-exits 2 on the deleted JSON; the leg runs on every bar |
| F2 | BLOCKER | 6 | §2 S1, §4 Files touched | the govkit subject ratchet collapses; `--write` is a guard reading the state the change corrupts |
| F3 | BLOCKER | 2 | §4 Migration, §6 AC7 | the `subject` → `opt_in` mapping silently reverts the 2026-08-26 chunk ruling on six legs |
| F4 | BLOCKER | 2 | §2 S2, §4, §5 | `tomllib` raises the runner's interpreter floor to CPython 3.11+ with no stated refusal |
| F5 | BLOCKER | 7 | §6 AC2 vs AC4, §2 S3 | `full_only` is unmapped, so AC2 and AC4 cannot both pass on an honest fixture |
| F6 | HIGH | 2 | §2 S1, §4 optional keys | the schema contradicts the unit-1 §S4 ruling it cites by name |
| F7 | HIGH | 2 / 6 | u2 §1 Goal, §3; u6 §2, §4 | no unit owns `gate-profiles.txt`'s retirement |
| F8 | HIGH | 2 | §2 S2 | S2 names a tab-separated wire format; the real one is RS/US and deliberately so |
| F9 | HIGH | 2 | §2 S2 vs S6/S7, §4 | "the dispatch loop does not change" is false; the unit's largest change is unpriced |
| F10 | HIGH | 2 | §3 non-goals, §4 Rollout | the stamp/pre-push blob pair splits, forcing a full bar on every push until unit 6 |
| F11 | HIGH | 2 | §8 F1 | the `GATE_SELFTESTS` rename breaks pre-push predicate 8 and the stamp's coverage byte |
| F12 | HIGH | 2 | §4 Migration, `timeout=` | `PROF_TIMEOUT` has two live consumers, one of which unit 4 §3 relies on |
| F13 | HIGH | 2 | §2 S8, §4 Files touched | folding the profile table disarms the pinned-knob arm by absence |
| F14 | HIGH | 3 | §6 AC2 | AC2 grades execution order, which the runner explicitly disclaims |
| F15 | HIGH | 3 | §4, §6 AC5 vs AC6 | the query verbs' insertion point is unspecified and the two ACs pull it apart |
| F16 | HIGH | 4 | §4 table vs §6 AC1-AC8 | no criterion exercises the declared value — the key the build exists to add |
| F17 | HIGH | 4 | §2 S7, §4, §6 | the adopter seed item has neither a file nor an acceptance criterion |
| F18 | HIGH | 5 | §4 table vs §6 AC1-AC6 | same could-not-fail shape: the declared `true` is never exercised |
| F19 | HIGH | 5 | §4 Data model | a TOML boolean into a `!= 0` string test ships the turnstile ENABLED |
| F20 | HIGH | 6 | §2 S7, §6 AC7 | two guards name the deleted JSON; AC7 is held off a default bar and passes over it |
| F21 | HIGH | 7 | §5, §6 | the upgrader writes TOML into a target without probing whether it can read one |
| F22 | MEDIUM | 2 | §8 F1 vs §2, §6 | `GATE_OPTIN` has no scope item and no acceptance criterion |
| F23 | MEDIUM | 2 | §5 error states | the unknown-key refusal is dropped; unit 7 S7 keeps it for foreign manifests |
| F24 | MEDIUM | 2 | §2 S1/S8, u6 §2 S1 | the manifest-key floor and the canary's pinned key set are unnamed |
| F25 | MEDIUM | 2 vs 6 | u2 §6 AC7, u6 §2 S7 | AC7's parity arm is what unit 6's dead-path leg forbids |
| F26 | MEDIUM | 4 | §2 S4 | the run record's new key has no acceptance criterion |
| F27 | MEDIUM | 6 | §2 S1, §6 AC1 | "gains the new file name" understates govkit's grammar enum by three changes |
| F28 | MEDIUM | 6 | §4 Files touched, §7 | the unit edits two size-gated files and lists neither gate |
| F29 | MEDIUM | 7 | §2 S3, §8 F1 vs §6 AC8 | nothing emits the `[[lane]]` rows the mapped lanes need |

---

## BLOCKERS

### F1 — the reader inventory misses a checker that hard-exits on the deleted file

**Address:** unit 6, §4 Inventory table and §2 S7.
*(source id 57)*

`tools/check-testsuite-counts.sh:27` hardcodes `MANIFEST=tools/gate-legs.json` and `:32` hard-exits 2
when it is absent, with the message "no tools/gate-legs.json, so the population would be empty and
this leg would pass by finding nothing". Its manifest row —
`testsuite counts (every bar self-test prints one)` — is `chunk = declarations`, `subject = repo`,
`guard` absent, so it runs on EVERY bar including a records-only one. S7 deletes the file it reads.

The script appears in neither §4's inventory table, nor §4's files-touched list, nor any acceptance
criterion, while §10 asserts the inventory "was derived by grepping `gate-legs` across the tree" and
that "the grep is the evidence here". The grep hits this file at line 17 and line 27. The evidence
the unit cites for its own completeness is the evidence that refutes it.

**Fix.** Add `tools/check-testsuite-counts.sh` to §4's inventory and files-touched with its own
scope item — its population selector is `grep -oE '"[^"]*\.test\.sh"'` over the manifest BYTES, which
needs re-stating for TOML — and re-run the grep to close the inventory before this unit is built.
`tools/memory-tree/check-memory-hygiene.sh`, `tools/template-size-limits.txt` and
`tools/workflows/drift-audit-state.js` also name the file.

**Left-shift gate.** The generalisable defect is that a hand-listed reader inventory was certified by
a grep nobody re-ran. Add an arm to `run-gates.gov.test.sh` that greps the tracked tree for the
manifest filename and fails when any hit is outside a declared allow-list — the same
declared-population-versus-tracked-surface shape §7 of the charter already prescribes for kits, one
level down.

### F2 — moving govkit onto a `subject`-less declaration collapses the subject ratchet

**Address:** unit 6, §2 S1 and §4 Files touched.
*(source id 58)*

`govkit.py:1354` is `live = {nm: (manifest_subject.get(nm) or "repo") for nm in manifest if nm}`,
pinned one row per leg against `tools/govkit/subject-pins.tsv`. Unit 2's RESOLVED F1 replaces
`subject` with `opt_in`. After S1 moves govkit onto that declaration, all 40 kit-subject legs resolve
to the `repo` default and `govkit selfcheck` — `chunk = declarations`, `subject = repo`, no guard,
therefore on every bar — reds once per kit-subject leg.

The escape is worse than the failure. If an implementer clears it with `selfcheck --write`, the
ratchet whose whole stated purpose is that a subject cannot move without the move appearing in a diff
records the ENTIRE population moving, as a generated file. That is a guard reading the state the
change corrupts, which is a named class in this tree.

Neither `subject-pins.tsv` nor the ratchet is named in any spec, files-touched list, or acceptance
criterion across the whole build folder. Unit 2's F1 costs out only the `GATE_SELFTESTS` meaning
change and never reaches this.

**Fix.** Add a scope item to S1: the ratchet pins `opt_in` instead of `subject`, the pin file and its
header move in the same commit, and an acceptance criterion asserts that a flipped `opt_in` value
reds `govkit selfcheck` against the unchanged pin file — observed RED first. Add
`tools/govkit/subject-pins.tsv` to §4's files-touched.

**Left-shift gate.** Extend `govkit`'s own selftest with an arm that fails when the pin file's value
column holds exactly one distinct value across more than N rows. A ratchet whose entire population
has collapsed to one default is indistinguishable from a ratchet that is working, and that is the
only signal available once the key is gone.

### F3 — the migration silently reverts a recorded fix on six legs, and no criterion can see it

**Address:** unit 2, §4 Migration (the `subject` → `opt_in` mapping) against §6 AC7.
*(merged from source ids 25 and 62 — the same defect reached from the mapping side and from the
criterion side)*

Re-derived from `tools/gate-legs.json` at this base: 86 legs, 40 with `subject = kit`, 43 with
`chunk = selftests`, union 46. Exactly six carry `subject = repo` AND `chunk = selftests` —
`branch-guard self-test`, `pre-push self-test`, `push-main self-test`, `recall floor arms`,
`run-gates canary`, `run-gates gov canary`.

The shipped hold predicate is the union, at `run-gates.sh:947`:

```
  if { [ "${subjects[$i]}" = kit ] || [ "${chunks[$i]}" = selftests ]; } \
     && [ -z "${GATE_SELFTESTS:-}" ]; then
```

and the comment block at `:934-946` records the 2026-08-26 owner ruling that produced it: "The
`subject = kit` predicate alone left SIX legs in the `selftests` chunk running on every bar, because
they carry `subject = repo`". Unit 2 §4 maps `subject` alone.

Both outcomes are bad and neither is visible. Either the union's chunk arm survives, and the
declaration disagrees with the runner about six legs — two answers to one question, inside the file
built to end that — or the hold unifies on `opt_in` and those six return to every default bar, which
is a behaviour change shipped inside a migration the spec calls field-for-field. AC7 pins only the
`subject = "kit"` → `opt_in = true` direction, AC1 compares leg count and order, and AC8 asserts the
count is unchanged at 86. Not one of the three can distinguish the two outcomes.

**Fix.** State the mapping as `opt_in = true` iff `subject == "kit" OR chunk == "selftests"` (46
legs), carrying `run-gates.sh:934-947` into the TOML's own comment as the reason. Rewrite AC7 to
compare the RESOLVED held SET before and after the migration — the set of names the JSON's hold
predicate selects against the set of `opt_in = true` names — rather than per-row on `subject`.

**Left-shift gate.** Add a canary arm that computes the held set from the declaration and compares it
against the set the dispatch loop actually holds in a scratch run. A parity arm that grades a KEY
rather than the RESOLVED BEHAVIOUR is how this defect stayed invisible; grading the resolution is the
version that can fail.

### F4 — `tomllib` raises the runner's interpreter floor, silently, in the kit built to travel

**Address:** unit 2, §2 S2, §4 Data model, §5 error/empty states.
*(source id 46)*

`run-gates.sh` today parses JSON through `json`, stdlib since forever, and
`tools/lib/resolve-python.sh` accepts any candidate that survives `-c 'import sys'` — there is no
version gate anywhere in the chain. `tomllib` needs CPython 3.11+.

The counterexample is measured and recorded in this repo. `govkit.py:452-462` documents a WSL
`python3` at 3.10.12 that "died on `import tomllib`, which needs 3.11", reddening a whole leg. Today
that class cannot reach `run-gates`; after this unit it can. A target whose resolved python is
pre-3.11 gets `parse error: No module named tomllib` → `run-gates: cannot parse` → exit 2 with ZERO
legs run — precisely the outcome `tools/run-gates/kit.toml`'s header says the kit was made deployable
to prevent, arriving through the loader instead of through `tools/lib/`.

§5 mentions `tomllib` only to say it does not execute, and its error-states line covers an
unparseable file, an unknown lane, an unresolvable concurrency and an empty list — never a missing
module.

**Fix.** State the interpreter floor in §4 and specify an explicit refusal in the loader modelled on
`govkit.py:74-77` ("this tool needs tomllib (CPython 3.11+)"), naming the resolved interpreter and
its version. Add an acceptance criterion that a python without `tomllib` produces that named refusal
rather than a bare parse error, and say in §5 whether the JSON arm is the documented fallback for
such a target.

**Left-shift gate.** Give `tools/lib/resolve-python.sh` a declared minimum and make the candidate
probe run it, so every kit that needs a floor states one and gets a named refusal instead of an
import traceback. One resolver, one floor, checked at the seam every kit already routes through.

### F5 — unit 7's AC2 and AC4 cannot both pass on a fixture derived from the real manifest

**Address:** unit 7, §6 AC2 vs AC4, with §2 S3.
*(source id 1 — see F6, which is its root cause in unit 2)*

S3's field-mapping table lists `cwd`, `tool`, `ceiling`, `guard`, `chunk` and `impure` as map-by-name,
plus the `subject`/`optIn` → `opt_in` and `phase` → `lane` rules. It does not cover `full_only`,
which unit 1's §S4 census records on 4 inCMS rows with the ruling "Retain as optional; it is 4 rows
in one repo and costs one key". §3's non-goals drop `pg`, `scoped` and `pg_autowire` and report them
as dropped — so `pg_autowire` is ruled on and AC4 does not fire for it. `full_only` is ruled the
other way and is still unmapped.

So on a dialect-B fixture honestly derived from inCMS's 66 rows, AC4's unmapped-key refusal fires on
four of them, and AC2's "all 66 legs are emitted" cannot hold. The only way to green both is a fixture
with those keys stripped, which is the `fixture-passes-by-finding-nothing` class this same spec names
in §10 and unit 5 names in its own F1. The two criteria are in direct contradiction on the acceptance
axis.

*(The count is four, not five. `pg_autowire` is correctly excluded by §3.)*

**Fix.** Add `full_only` to S3's mapping table with its explicit ruling, then split AC4 into two
criteria: an UNRULED key refuses with exit 2, and a ruled-DROP key is reported as dropped with the
leg still emitted. Pin the fixture to the real key census in the adopter review rather than to a
hand-built row.

**Left-shift gate.** Add an arm asserting that the mapping table's key set is a SUPERSET of the union
of keys in both fixture dialects, computed from the fixtures rather than typed. That arm fails the
moment a real manifest carries a key nobody ruled on, which is the class rather than the instance.

---

## HIGH

### F6 — the schema contradicts the ruling it cites by name

**Address:** unit 2, §2 S1 and §4's optional-keys line.
*(source id 13 — the root cause of F5)*

S1 states its field set is "ruled by `TOOL-aGatheredDeclaration-1` §S4". Unit 1's §S4 table rules
`full_only` "Retain as optional". Unit 2's field set and its optional-keys line (`cwd`, `lane`,
`opt_in`, `guard`, `impure`, `tool`, `ceiling`) never declare it. Unit 7's S3 then inherits the gap,
which is the mechanism behind F5.

**Fix.** Either declare `full_only` in S1 and add it to §4's optional-keys line, or record in §3 that
the ruling is overturned and why — so unit 7's mapping has one source to follow. A citation to a
ruling the citing document contradicts is worse than no citation.

**Left-shift gate.** Extend the memory hygiene gate with a check that a spec section claiming a field
set is "ruled by `<id>` §<n>" declares every key that section's table retains. Cheap, and it grades
the exact shape that produced both F5 and F6.

### F7 — no unit owns `gate-profiles.txt`'s retirement

**Address:** unit 2 §1 Goal and §3 Non-goals against §2 S3; unit 6 §2 S1-S8 and §4.
*(merged from source ids 27 and 66)*

Unit 2's Goal replaces BOTH `gate-legs.json` and `tools/run-gates/gate-profiles.txt`. §3 defers
deletion of only the JSON to unit 6. S3's dual-format fallback is defined only over the leg manifest.
`gate-profiles.txt` appears in NO unit's scope, §4 inventory, or files-touched list — not unit 2's,
not unit 5's, not unit 6's.

It is very much alive. `tools/run-gates/kit.toml:146` pins it as an `[[lf_pin]]`; the table's own
header declares `GATE_PROFILES=<path>` "the documented rollback for this whole mechanism", which the
TOML design never re-homes; and four suites name it. Two of those actively REQUIRE carriers to keep
naming it: `run-gates.test.sh:1241-1242` reds if the kit README stops naming `gate-profiles.txt`, and
`run-gates.gov.test.sh:234-235` reds if the charter does — both legs unit 6 lists in its own §7 while
rewriting exactly those carriers.

So either the "one file" goal is never reached, or the file goes with a stale `lf_pin`, an orphaned
`GATE_PROFILES` override, and two canaries reddening with no commit assigned to fix them.

**Fix.** State in unit 2's S3 that the JSON fallback is the PAIR (`gate-legs.json` +
`gate-profiles.txt`) and that `gate-profiles.txt` survives until unit 6. Add the file, the `kit.toml`
`lf_pin`, the `GATE_PROFILES` override's fate, and the four suites to unit 6's S7 and its
files-touched list.

**Left-shift gate.** `tools/check-dead-paths.sh` already grades a carrier naming a deleted path. The
missing half is the inverse: a leg asserting that every `[[lf_pin]]` pattern in a kit's `kit.toml`
matches a tracked path. A pin naming a file that no longer exists is a declaration that has stopped
declaring anything, and it is the same could-not-fail shape as the guard in F20.

### F8 — S2 names the wrong wire format, and the field it would collapse is the common case

**Address:** unit 2, §2 S2.
*(source id 47)*

S2 says the reader emits "the same tab-separated table the current JSON path emits". The current path
is deliberately not tab-separated. `run-gates.sh:840-901` emits
`name \x1e guard \x1e argv(\x1f-joined) \x1e impure \x1e chunk \x1e subject \x1e ceiling`, and its own
comment states why: RS/US are "non-whitespace, so an empty guard field survives `read`; a tab would
collapse". The reader at `:905-910` splits on `IFS=$'\x1e'`.

Of 86 legs, 36 carry no guard. An empty guard field is not an edge case, it is 42% of the manifest.
Implemented as S2 literally reads, every one of those rows shifts each later field left and argv is
parsed as the guard list. AC1 cannot catch it, because it compares the new loader against a JSON
loader rewritten to the same wrong separator.

**Fix.** Correct S2 to name the RS/US wire format and pin it as an interface the TOML reader must
reproduce byte-for-byte, including field ORDER and the append-only rule the emitter's own comments
state — a field inserted before an existing one is parsed AS that one by any reader that has not
moved in the same commit. Add an acceptance criterion that a leg with an empty guard round-trips.

**Left-shift gate.** Add a canary arm that feeds the loader a leg with every optional field empty and
asserts the parsed tuple field-by-field. A round-trip arm over the sparsest legal row is what catches
a separator change; comparing two loaders that share a bug catches nothing.

### F9 — the unit's largest behavioural change is scoped and reviewed as a format change

**Address:** unit 2, §2 S2 against S6 and S7, and §4 Design.
*(source id 48)*

S2 asserts "the dispatch loop below it does not change". Today there is ONE bounded pool at a single
width (`JOBS=${GATE_JOBS:-$PROF_WIDTH}` at `:372`, `while [ "$(live)" -lt "$JOBS" ]` at `:1272`), fed
by a single GLOBAL longest-first dispatch hint built over all legs at `:846-870`.

S6 (per-lane concurrency and `short_circuit`) and S7 (a pre-run tool probe) cannot be implemented
without rewriting that loop: lanes need phase ordering, a per-phase width, a skip-marking pass for
short-circuited lanes, and a per-lane order hint — the current global hint would interleave `fast`
and `heavy` legs and defeat S6 outright. §4 prices `run-gates.sh` as "(loader)" and §5 claims "No
regression".

**Fix.** Either split lanes and the tool probe into their own unit, or add a §4 subsection designing
the dispatcher: phase order, the width each lane takes, how the line-1 hint is partitioned per lane,
and which verb a short-circuited leg reports. The existing `skip` tail reads "unchanged vs
`<branch>`", which is false for a short-circuit skip and would misreport it.

**Left-shift gate.** Add an arm asserting the reported verb for a short-circuited leg is distinct
from the guard-skip verb, and that its reason names the short circuit. Two different reasons rendering
as one string is how a skip stops announcing itself, which §7 of the charter names as its own class.

### F10 — the stamp and the hook's blob predicate split, forcing a full bar on every push

**Address:** unit 2, §3 non-goals (pre-push deferred to unit 6) and §4 Rollout.
*(source id 49)*

`run-gates.sh:1430` stamps `manifest_blob` as `git hash-object -- "$LEGS_FILE"`, and unit 2 §10 makes
`LEGS_FILE` resolve to the TOML first. `.githooks/pre-push:203` compares the recorded blob against
`git hash-object -- tools/gate-legs.json`. They can never match.

I checked the stamp is still reachable during the window: `ondemand` is its own counter
(`run-gates.sh:69`, `:1174`), not `skips`, so an ordinary held-selftests push still satisfies the
stamp's preconditions and writes a record carrying the TOML blob. Predicate 7 then fires on EVERY
default-branch push until unit 6 moves the hook — a permanent full bar, on a bar with a 26-minute
floor, which is the exact cost this build exists to remove. It reads as caution rather than as a bug,
which is why nothing would surface it.

§4 Rollout's "nothing outside this kit has to move" is the sentence the pair falsifies.

**Fix.** Name the stamp/hook pair in §3 as an exception to the deferral and add a scope item: either
the hook's two hardcoded pathspecs move in unit 2, or the stamp keeps writing the JSON blob until
unit 6 lands. Add an acceptance criterion over `.githooks/pre-push.test.sh` asserting a scoped push is
still reachable on the commit that introduces the TOML.

**Left-shift gate.** Add an arm to `.githooks/pre-push.test.sh` that runs a bar, then a push, in one
scratch repo and asserts the push is NOT forced. Today every predicate is tested in isolation, so a
pair that disagrees about which file it hashes passes both halves.

### F11 — the `GATE_SELFTESTS` rename breaks a push-boundary predicate no unit names

**Address:** unit 2, §8 F1 RESOLVED.
*(source id 63)*

F1 keeps `GATE_SELFTESTS` as an alias for the new `GATE_OPTIN` and describes this as breaking no
adopter's hook. It breaks gov's own. `.githooks/pre-push:213` gates predicate 8 on
`[ -n "${GATE_SELFTESTS:-}" ]` against `rec_st` read at `:151`, and `run-gates.sh:1435` writes that
stamp field from `${GATE_SELFTESTS:+1}`.

A push run under the new spelling sets neither. The stamp under-records what the run covered, and —
the direction that actually bites — predicate 8 no longer fires for a push that WILL run the opt-in
legs against a record earned with them held. That is precisely the case `TOOL-dUnstalledConvoy-27`
wrote it for. Unit 6 S2 scopes pre-push to the manifest path and the install prefix, not the stamp
key, so no unit owns it.

**Fix.** Add a scope item and an acceptance criterion to unit 2 (or unit 6 S2) covering the run-record
key and predicate 8 under BOTH spellings — the alias must set the same stamp byte and satisfy the same
predicate. Unit 4's S5/AC6 does exactly this work for `enforce_ceilings` and is the model.

**Left-shift gate.** Parameterise the pre-push selftest's predicate-8 arms over both spellings. An
alias tested in only one spelling is an alias whose second spelling is undefined behaviour.

### F12 — dropping `timeout=` removes a knob two live consumers read, one of them a sibling's invariant

**Address:** unit 2, §4 Migration, the paragraph "**`timeout=` does not travel.**"
*(source id 64)*

The removal is argued solely from the current VALUE: "All three profile rows declare `timeout=0`".
That is true of the value and false of the consumers. `PROF_TIMEOUT` has two:

- `run-gates.sh:434` — `TS_TTL=$(( PROF_TIMEOUT * 3 ))`, whose ponytail comment at `:431` names
  setting `timeout=` on the profile row as the PRESCRIBED fix for a leg reaped mid-run, explicitly in
  preference to raising the constant.
- `run-gates.sh:1104` — `bound=$PROF_TIMEOUT`, the per-leg fallback, provenance `TOOL-aBoundedCeiling-1`.

The sibling contradiction is verbatim. Unit 4 §3 lists as an out-of-scope invariant "The turnstile's
TTL, which is derived from the profile row's `timeout=`" — a sentence unit 2 makes false in the same
build, on the interface axis. Unit 2's own §10 re-verifies that derivation at `:430-441` and then
drops the knob feeding it.

**Fix.** Name both consumers in the migration paragraph and say what replaces each: `[bar].default_ceiling`
for the leg fallback, and an explicit `[bar].turnstile_ttl` (or the promoted `GATE_TURNSTILE_TTL`) for
the TTL. Re-word unit 4 §3 to point at the surviving source rather than at a knob unit 2 removes.

**Left-shift gate.** Before a knob is removed, grep its resolved variable name — not the knob's
spelling — across the kit, and add the hit list to the migration paragraph. A knob argued dead from
its VALUE is the recurring shape; the check is that the argument must cite consumers, not readings.

### F13 — folding the profile table disarms the arm that enforces the table's governing invariant

**Address:** unit 2, §2 S8 and §4 Files touched.
*(source id 65)*

`run-gates.test.sh:1035-1052` pins `PINNED_KNOBS="timeout width"` and SKIPS the whole pinned-knob arm
when `$PTBL` (`$KITREL/gate-profiles.txt`) is absent, announcing "this tree declares no knobs to
grade". That message becomes false the moment the knobs live in `gate-legs.toml`, and the arm retires
by absence while the suite stays green.

What stops being graded is this build's own README rule: "A knob may never turn a leg into a PASS or
a SKIP… survives the move verbatim". S8's arms cover the reader, the dual-format branch and the
schema refusals; AC7's parity arm covers legs only. Nothing regrades the knob invariant. Arm 4l
(`:1235-1243`) compounds it — it REQUIRES `run-gates.sh` and `README.md` to name `gate-profiles.txt`,
so the move touches this suite whether the spec says so or not (see F7).

**Fix.** Add to S8: repoint the pinned-knob arm at the `[[profile]]` rows in the TOML, drop `timeout`
from `PINNED_KNOBS` in the same edit (F12), and give it an acceptance criterion that the arm FAILS on
an unpinned knob key in the TOML, observed RED first — so it can no longer pass by finding no file.

**Left-shift gate.** Make the skip conditional itself a failure once the format has moved: an
announced skip whose antecedent is a file the tree no longer has is a green-by-absence, and the arm
should red rather than announce. Generalisable rule for the suite — a skip guard naming a path must
assert that path is tracked, exactly as `run-gates.test.sh:268-283` already does for leg guards.

### F14 — AC2 grades a property the runner explicitly disclaims

**Address:** unit 3, §6 AC2.
*(source id 51)*

AC2 asserts two `--leg` legs "run in MANIFEST order rather than argument order, asserted by the marker
files' mtime ordering". `run-gates.sh:16-17` states the opposite as a design property: "Execution
order is a scheduling detail; REPORTING is always manifest order", and `:842-844` dispatches
longest-first from the timing cache.

Marker-file mtime observes EXECUTION, not reporting. At any pool width above 1 the two legs launch
concurrently and AC2 is a race; at width 1 the order is the cache's, not the manifest's. Nothing in
§2 asks for serialised `--leg` dispatch, and §3 explicitly says the unit "does not change dispatch,
the pool". So the criterion is either flaky or forces a change the spec rules out of scope.

**Fix.** Restate AC2 over REPORTING order — the `GATE ok` rows in captured output are in manifest
order — and drop the mtime mechanism. If execution order genuinely matters for `--leg`, add an
explicit scope item saying so and price the dispatcher change.

**Left-shift gate.** No new gate; this is a spec-side repair. The reusable rule is that an acceptance
criterion asserting ORDER must name which of the two orders the runner distinguishes, and a criterion
whose mechanism is a timestamp on a concurrently-launched process is not timing-independent — the
same discipline unit 2's AC6 already applies by asserting file ABSENCE instead.

### F15 — the query verbs' insertion point is unspecified, and two ACs demand different ones

**Address:** unit 3, §4 Design and §6 AC5 vs AC6.
*(source id 52)*

`--list` and `--manifest` are specified as query verbs, but nothing says they bypass the turnstile or
suppress the profile line, and both sit between argument parsing and the manifest load.

`PROF_LINE` is echoed to STDOUT at `run-gates.sh:405`. The turnstile acquires at `:420` with
`TS_MAXWAIT = TS_TTL * 4` — 7200 s on the shipped 1800 s fallback. The manifest is not loaded until
`:846`. So a verb needing leg names cannot exit before either, and a read-only `--list` would queue
behind a running bar for up to two hours.

The two criteria then pull in opposite directions: AC5's "stdout is exactly the leg names" is
unsatisfiable unless the verb exits before `:405`, while AC6 needs `profile <row> width <w>` in the
`--manifest` header, i.e. after profile selection. §4 says only that argument PARSING sits above every
env read, which settles neither. Unit 5 shipping the turnstile off masks this in gov but not in an
adopter who turned it on.

**Fix.** Add an explicit ordering statement to §4: the query verbs load the manifest early, never
acquire the turnstile, and write only their payload to stdout — profile and queue lines go to stderr
for these verbs. State it as an interface property, and give AC5/AC6 a concurrency arm: `--list` while
a beacon is planted returns immediately.

**Left-shift gate.** Add a turnstile-suite arm asserting that every query verb completes with a
beacon planted, with an elapsed-time bound against an untimed control. That arm fails the moment a
read-only verb acquires a lock, which is the class rather than these two verbs.

### F16 — unit 4's acceptance set never exercises the declared value

**Address:** unit 4, §4 Data model (the three-row resolution table) against §6 AC1-AC8.
*(source id 30)*

The resolution table has three rows and the criteria reach two. AC2 exercises the env row, AC1 the
"neither" row, AC5 an invalid env value. The middle row — `[bar].enforce_ceilings = true` with the env
unset, the key this entire build exists to introduce — is exercised in neither of its values.

An implementation that reads only `GATE_CEILINGS` and hardcodes the default off passes AC1, AC3, AC4,
AC5 and AC8 unchanged, leaving the declaration decorative. Unit 2 §3 hands enforcement policy to this
unit explicitly, so no sibling covers it.

AC1's antecedent compounds it: after unit 2 ships `enforce_ceilings = false`, "neither is set"
describes a tree state that no longer exists, so AC1 grades a scratch state rather than the shipped
one.

**Fix.** Add a criterion: with `[bar].enforce_ceilings = true` and `GATE_CEILINGS` unset, the
over-ceiling scratch leg is killed and `--manifest` reports enforcement on with source `declaration`.
Reword AC1 to the shipped state (declared `false`) rather than "neither is set".

**Left-shift gate.** For any resolution table in this kit, add a suite arm per ROW, driven from the
table itself. A three-row precedence table with two arms is a could-not-fail shape, and it appears
twice in this build (see F18) — which makes it the class, not the instance.

### F17 — the adopter-seed scope item has neither a file nor an acceptance criterion

**Address:** unit 4, §2 S7 against §4 Files touched and §6.
*(merged from source ids 35 and 55)*

S7 requires the kit's adopter seed to declare `enforce_ceilings = false`, "so no adopter inherits
enforcement by arriving". §4's files-touched lists `run-gates.sh`, `gate-legs.toml`, `.unattended.conf`,
`unattended.sh`, `.githooks/pre-push`, the test file and the README — neither `adopt-run-gates.sh` nor
`tools/run-gates/kit.toml`, and gov's own `gate-legs.toml` is not the adopter seed. None of AC1-AC8
mentions it.

The asymmetry is inside this build. Unit 5's structurally identical S3 (`turnstile = false`) carries
`tools/run-gates/kit.toml` (the `[gate_runner_seed]` block) in its §4 AND AC5, which asserts the
seeded declaration via `adopt-run-gates.sh --check`. So one of two seeded `[bar]` keys has an owner,
a file and an arm; the other has none, and lands unimplemented behind the unit's own green.

**Fix.** Add an acceptance criterion mirroring unit 5's AC5 — `adopt-run-gates.sh --check` against a
freshly seeded target carries `enforce_ceilings = false` — add the seed file to §4, and say whether
the seed is written by `adopt-run-gates.sh` or by govkit's `[gate_runner_seed]` block. Unit 5 names
the latter; unit 4 names neither, and two units writing two keys through two paths is how they
diverge.

**Left-shift gate.** Add an arm to `adopt-run-gates.test.sh` asserting the seeded `[bar]` table's KEY
SET equals the key set gov's own `gate-legs.toml` declares, computed from both files. A seed missing a
key it should carry then reds by construction, whichever unit forgot it.

### F18 — unit 5's acceptance set never proves the declaration enables anything

**Address:** unit 5, §4 Data model (resolution table) against §6 AC1-AC6.
*(source id 31)*

Same three-row table, same gap: AC1 grades the shipped-off path, AC3 the `GATE_TURNSTILE=1` path,
AC4/AC5/AC6 the reporting and the seed. No arm proves `[bar].turnstile = true` with the env unset
actually enables the mechanism.

A runner that ignores `[bar].turnstile` entirely and flips `run-gates.sh:420`'s `${GATE_TURNSTILE:-1}`
literal to `0` satisfies every criterion — AC6 only requires the profile line to NAME a source, which
a hardcoded path can print. The unit's own F1 RESOLVED names this class in the mirror direction ("a
suite that only ever exercises the non-default path proves nothing about what ships"), so the spec
states the rule and then fails to apply it to its own declaration.

**Fix.** Add a criterion: with `[bar].turnstile = true` and `GATE_TURNSTILE` unset, a beacon and a
ticket ARE created and a second concurrent bar queues, asserted in `run-gates.turnstile.test.sh`.

**Left-shift gate.** Same as F16 — one arm per row of the resolution table, driven from the table.
Both units need it and neither has it, which is what makes it worth building once.

### F19 — a TOML boolean into a `!= 0` string test ships the turnstile ENABLED

**Address:** unit 5, §4 Data model resolution table.
*(source id 56)*

Both guards are string tests: `run-gates.sh:420` and `:726` are `[ "${GATE_TURNSTILE:-1}" != 0 ]`. S2
prescribes the substitution literally — "the `1` becomes the declared value". A TOML boolean
substituted there yields `[ "false" != 0 ]`, which is TRUE. `turnstile = false` would ship the
turnstile ENABLED: the exact inversion of this unit's goal, and it would read as "the declaration is
wired" because the value visibly reaches the guard.

No criterion closes it. AC1's fixture is "neither `GATE_TURNSTILE` nor `[bar].turnstile` is set",
which is not the shipped configuration since S1 declares `turnstile = false`; AC6 grades only what the
profile line SAYS, which would report off while the guard ran on. Taken with F18, an inverted
declaration ships behind a fully green suite.

Unit 4 §4 has the same unstated join between a TOML boolean and `GATE_CEILINGS=0|1`.

**Fix.** State in §4 that the declared boolean is marshalled to `0`/`1` at the loader boundary and
that the guards compare only those two bytes. Make the marshalling the stated mechanism so unit 4 can
reuse it rather than restating it.

**Left-shift gate.** Add a loader arm asserting that every `[bar]` boolean emerges from the reader as
exactly `0` or `1`, byte-compared. One arm covers both units' joins and every `[bar]` boolean added
later.

### F20 — two guards name the deleted JSON, and AC7 is held off the bar that would catch it

**Address:** unit 6, §2 S7 and §6 AC7.
*(source id 60)*

`run-gates canary` guards `["tools/", "tools/gate-legs.json", "tools/lib/"]` and `run-gates gov canary`
guards `["tools/run-gates/", "tools/gate-legs.json"]`. `run-gates.test.sh:268-283` fails on "guard
pathspec matches no tracked path (the leg would skip forever)". Those guard lists live in
`tools/gate-legs.toml` after unit 2, which is absent from §4's files-touched — only the JSON is, as
deleted.

AC7 asserts the bar is GREEN with no JSON present. Both canaries are `chunk = selftests`, so a default
bar HOLDS them and AC7 passes green while the guards are dead. The unit ships a silently-skipping
guard past an acceptance criterion written to catch exactly that shape.

**Fix.** Add the guard edit to S7 explicitly, list `tools/gate-legs.toml` in §4's files-touched, and
re-anchor AC7 on a `GATE_SELFTESTS=1` run so the canary that grades guard liveness actually executes.

**Left-shift gate.** Promote the guard-liveness assertion out of the held canary: make the
`gate-legs` declaration check that runs on every bar assert every guard pathspec matches a tracked
path. A liveness assertion held off the default bar is a liveness assertion nobody gets.

### F21 — the upgrader writes a file into a target that may not be able to read it

**Address:** unit 7, §5 production-readiness and §6.
*(source id 61)*

Same floor as F4, one repository further out. Unit 2 S3 makes `gate-legs.toml` win where it exists, so
the moment `--upgrade` lands the file, a target whose resolved `python3` predates 3.11 has a bar that
exits 2 with zero legs run. The upgrade converts a working merge bar into a dead one, and
`--force`/rollback is discoverable only after the breakage.

This build already ruled on it and unit 7 does not carry the ruling: R10 in
`build/2026-08-31-build-TOOL-aGatheredDeclaration-2-architecture-recommendations.md` ends "Unit 7's
`--upgrade` must therefore REFUSE on a sub-3.11 interpreter rather than writing a file that tree
cannot read." Unit 7's spec-records block says "No record names this unit", §5 covers path escape and
field loss only, and no criterion probes the target's interpreter.

*One correction to the finding as filed, flagged rather than rested on: the 3.10.12 interpreter is
node `d`'s WSL python (`govkit.py:461`, `TOOL-dSettledRoster-3`), not a measurement of inCMS. The
population at risk is any target whose resolved python is pre-3.11; no such measurement exists for
either named adopter. The finding stands without that detail.*

**Fix.** Add a pre-write probe to S1/S7: run the target's resolved python with `import tomllib` and
refuse (exit 2, naming the interpreter and its version) unless `--force`; report it in S6's test
report as a required target change. Add an acceptance criterion over a fixture target whose python
cannot import `tomllib`.

**Left-shift gate.** One shared preflight in `adopt-run-gates.sh` that every write verb calls, and an
arm asserting each verb refuses on the fixture target. A per-verb probe is a probe the next verb
forgets.

---

## MEDIUM

### F22 — the env-var rename has no scope item and no acceptance criterion

**Address:** unit 2, §8 F1 RESOLVED, against §2 and §6. *(source id 33)*

`GATE_OPTIN` and `GATE_SELFTESTS` appear ONLY inside F1's own text — no S-item in §2, no criterion in
§6, no mention in units 3, 6 or 7. The contrast is inside the same build: F2's resolution
(`GATE_CEILINGS`) was folded into unit 4's S2, its §4 table, and AC1/AC2/AC5. F1's was folded nowhere,
so an env-var replace-plus-alias ships with no scope line and no test, while unit 6 S6 promises the
carriers only "the sharding verbs". The runner's user-facing strings at `run-gates.sh:1175`, `:1347`
and `:1366` all still speak `subject`/self-test, and `AGENTS.md`'s command block documents
`GATE_SELFTESTS=1` with the old semantics. F11 is this defect's concrete consequence.

**Fix.** Add an S-item covering `GATE_OPTIN`, the `GATE_SELFTESTS` alias and the three runner message
strings, plus a criterion asserting both spellings select an identical leg set. Extend unit 6 S6 to
the opt-in rename.

**Left-shift gate.** Add a gov-canary arm asserting the charter's command block names every env var
the runner reads, derived from the runner's source rather than from a typed list.

### F23 — the migration drops an existing refusal

**Address:** unit 2, §5 error/empty states. *(source id 50)*

Today an unknown knob key in a profile row and a selected row with no width each `prof_die`
(`run-gates.sh:292`, `:320`), with the reason recorded inline: "A silently ignored knob is a knob the
operator believes they set, so an unknown key REFUSES". `tomllib` accepts any key silently, so a
typo'd `widht = 8` in a `[[profile]]` or a misspelled `ceilling` on a `[[leg]]` becomes an ignored key
with a defaulted value. §5's refusal list enumerates four arms and none is unknown-key; §4's
"Optional keys and their defaults" paragraph does not state it either.

Sibling asymmetry: unit 7 S7 refuses exactly this shape — "a leg carrying a key no mapping covers" —
for a FOREIGN manifest, while gov's own reader would tolerate it.

**Fix.** Add to §5, and to an acceptance criterion, a closed-key-set refusal for `[bar]`,
`[[profile]]`, `[[lane]]` and `[[leg]]` tables: exit 2 naming the offending key and row, matching unit
7 S7 so the two readers agree.

**Left-shift gate.** The closed-key-set check IS the gate; the canary's existing pinned-key arm
(`run-gates.test.sh:98-115`) is the model and should be repointed at the TOML rather than rewritten.

### F24 — the manifest-key floor and the canary's pinned key set are unnamed

**Address:** unit 2, §2 S1 and S8; unit 6, §2 S1. *(source id 71)*

Adding `opt_in`, `lane`, `cwd` and `tool` while removing `subject` bypasses the mechanism this repo
built the last time the manifest gained a key. `run-gates.sh:19-22` records that the manifest gained
`subject` at kit version 1.1 and that "A target below 1.1 REDS on a leg row carrying the key";
`SUBJECT_FLOOR_RUN_GATES = (1, 1)` and `check_target_reads_subject` (`govkit.py:2974-3001`, used at
`:4333`) implement the withholding; and the canary's `KNOWN` set
`{name, argv, guard, impure, chunk, subject, ceiling}` refuses any stray key.

Neither unit names the floor, the pinned key set, or the `KIT_RUN_GATES_VERSION` bump. Unit 2's §7
does list `run-gates canary` and `kit version markers`, so the key-set and version halves are forced
by legs already in its own gate list — the genuinely unowned half is the floor's retirement, and a
floor keyed to a key the format no longer has protects nothing.

**Fix.** Unit 2 S8 adds the pinned `KNOWN`-set update and the `1.3 -> 1.4` version bump with its
provenance line. Unit 6 S1 states the fate of `SUBJECT_FLOOR_RUN_GATES` / `check_target_reads_subject`
— retargeted at the FORMAT (a target whose runner cannot read TOML) or deleted with its reason
recorded.

**Left-shift gate.** Add a govkit selftest arm asserting every declared floor names a key or a
capability the current emitter actually emits. A floor referencing a retired key is dead code that
still looks like protection.

### F25 — AC7's parity arm is what unit 6's dead-path leg forbids

**Address:** unit 2 §6 AC7 against unit 6 §2 S7 and AC6. *(source id 36)*

AC7 mandates a parity arm reading both `gate-legs.toml` and `gate-legs.json`. Unit 6 S7 deletes the
JSON and AC6 asserts `check-dead-paths.sh` finds no carrier naming it — a checker whose header
confirms it scans everything outside `memory/`, test-suite literals deliberately included. Unit 6 §3
simultaneously KEEPS the loader's JSON arm, which must name the file to probe for it. 29 tracked
carriers outside `memory/` name it today and unit 6 §4 lists a subset. Neither spec retires AC7's arm.

**Fix.** Mark AC7's parity arm in unit 2 §6 as a one-landing migration check, and name
`tools/run-gates/run-gates.test.sh` in unit 6's files-touched as the place the arm is removed in the
S7 commit. State the allow-list for the loader's own probe literal in the same place.

**Left-shift gate.** `check-dead-paths.sh` already grades this; the missing piece is an explicit
allow-list entry with its reason, so the surviving probe literal is a declared exception rather than a
finding somebody waives under landing pressure.

### F26 — the run record's new key has no acceptance criterion

**Address:** unit 4, §2 S4. *(source id 73)*

S4 gives the run record an `enforce_ceilings` key and its source "so a later reader can tell which
kind of green a recorded run was" — and nothing grades it. AC3 grades the stderr banner, AC4 grades
`gate-last-summary.txt`, AC6 the stamp, AC8 `--manifest`. The run record is a distinct durable
artifact: `run-gates.sh:765+` builds a per-run directory of append-once files while `:158` writes the
summary, so AC4's grep does not reach it. Unit 5's AC4 does exactly this work for its own keys by
reading the record rather than the stream.

Shipped ungraded, an absent or misspelled key turns S5's coverage comparison into one that reads
nothing and defaults quietly.

**Fix.** Add a criterion modelled on unit 5 AC4: after a run, the run record carries
`enforce_ceilings` and its source key, read from the record file rather than from the stream, in both
the env-override and declared-default cases.

**Left-shift gate.** Add an evidence-suite arm asserting the run record's key set matches a declared
schema, so a key added to the record without an arm reds by construction.

### F27 — "gains the new file name" understates govkit's grammar work by three changes

**Address:** unit 6, §2 S1 and §6 AC1. *(source id 59)*

`govkit.py:2947` fails on `grammar` not in `(None, "json-array")`, `:2912` refuses a `kind` outside its
vocabulary, and `GR_REQUIRED` (`:2900`) makes `grammar` a required key of a complete manifest
promotion. `tools/run-gates/kit.toml:107-108` declares `grammar = "json-array"` beside
`file = "{prefix}/gate-legs.json"`. Emitting TOML rows under a grammar literally named `json-array` is
incoherent, so S1 needs a new grammar member, a validator arm, a TOML emitter, and a migration for
every already-seeded target's `[gate_runner]` block. AC1 asserts only the emitted path and its rows,
so it certifies the half that is spelled out.

**Fix.** Expand S1 to name the grammar enum, the `GR_REQUIRED` validator and the emitter as three
separate changes, and add a criterion that a target whose `[gate_runner]` still declares `json-array`
gets a named refusal pointing at unit 7's `--upgrade`, rather than a silent JSON emit.

**Left-shift gate.** Add a govkit selftest arm asserting every grammar value appearing in any tracked
`kit.toml` is a member of the emitter's enum. A grammar nobody implements then reds where it is
declared.

### F28 — the unit edits two size-gated files and lists neither gate

**Address:** unit 6, §4 Files touched (S6) against §7 Gates. *(source id 44)*

Measured on this tree: `AGENTS.md` is 64471 of its declared 64512 bytes — 41 under — and
`coding-governance-agents.template.md` is 48907 of 49152, 245 under, and is ALREADY warning that it
grew past its recorded high-water (48378 → 48907). Both are `subject = repo`, unguarded legs that run
on every bar. §4 touches both files and S6 says the command block "gains the sharding verbs and drops
nothing", which reds both legs on roughly the first line added, while §7 lists nine gates and neither
of these.

**Fix.** Add `charter size` and `template size` to §7 and a criterion that both files stay under their
ceilings after S6 — or state in §4 what is externalized to pay for the added verbs. 41 bytes is not a
budget.

**Left-shift gate.** No new gate; the legs exist. The reusable rule is that a unit's §7 must name every
gate over a file in its own §4 files-touched, which is mechanically checkable against
`tools/gate-legs.json` argv paths and would have caught this at spec time.

### F29 — nothing emits the `[[lane]]` rows the mapped lanes need

**Address:** unit 7, §2 S3 and §8 F1 against §6 AC8, with unit 2 AC3. *(source id 37)*

Unit 7's §2 and §4 describe only a per-leg field mapping table; nothing emits file-level `[[lane]]`
rows, `[bar]` or `[[profile]]` tables. Unit 2 AC3 makes a leg naming an undeclared lane exit 2.
Dialect B maps inCMS's three `phase` values to `lane`, and F1 defaults dialect A's 40 lane-less legs
to `heavy` — in both cases the emitted TOML references lanes no row declares. AC8, which hands the
output to `run-gates.sh --manifest` and expects the source's leg count, therefore cannot pass on
either dialect. §3's non-goals withhold none of this.

**Fix.** Add an S-item: emit one `[[lane]]` row per distinct resolved lane, with `concurrency`
defaulting to the profile width and `short_circuit` unset, and assert the rows in AC1 and AC2.

**Left-shift gate.** AC8's end-to-end load is the gate and it already fails — the repair is to the
spec, not the suite. Worth stating in unit 7 §5 that a self-consistency check (every referenced lane
is declared) runs before the file is written, so the refusal names the missing lane rather than
surfacing as a downstream parse failure in the target.

---

## Cross-cutting observations

**Two shapes account for eleven of the twenty-nine findings, and both are named in this repo's own
charter.**

*The could-not-fail acceptance criterion.* F16 and F18 are the same defect in two units: a three-row
resolution table with arms on two rows, where the missing row is the declared value the build exists
to introduce. F17, F22, F26 and F2 are its scope-side twin — a scope item with no file, no criterion,
or both. In every case an implementation that never reads the new key passes the unit's own green.
The single highest-value edit across the whole set is a rule for this build: every resolution table
gets one arm per row, and every S-item gets either an acceptance criterion or an explicit line saying
which sibling's criterion covers it.

*The guard disarmed by absence.* F13 (a skip when the profile table is gone), F20 (guards naming a
deleted path, held off the default bar), F1 (a hard exit on a deleted manifest) and F24 (a floor
keyed to a retired key) are four instances of a check that stops checking when the thing it names goes
away — the green-by-absence class. A format migration is unusually rich in this shape because it
deletes the antecedent of every guard written against the old format. Before unit 6 is built, the
grep §10 claims as its evidence should be re-run and its output pasted into §4, because the inventory
that grep produced is provably incomplete (F1).

**A note on what was NOT found.** No finding contradicts the owner's two rulings, and none argues the
build should be shaped differently. Unit 1 is clean — its census is correctly derived, its
`UNVERIFIED` marks are honest, and the one gap it leaves (`full_only`) is a downstream failure to read
its ruling rather than a defect in the ruling. Unit 3 is the healthiest of the six Tier-2 specs: two
findings, both acceptance-side, no scope or interface gap.

## Round exit

BLOCKED. F1, F2 and F3 must be resolved before unit 2 is built, because F3 changes the migration
itself and F1/F2 change what unit 6 has to touch — deferring them means unit 2 lands a mapping that
unit 6 then has to unpick. F4, F5 and the sixteen HIGH rows are spec edits, not code, and can land as
a single rev-2 pass across the seven files.
