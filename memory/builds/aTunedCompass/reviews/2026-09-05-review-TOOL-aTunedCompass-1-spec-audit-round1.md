**Serves:** spec-audit TOOL-aTunedCompass-1 TOOL-aTunedCompass-2 TOOL-aTunedCompass-3 TOOL-aTunedCompass-4 TOOL-aTunedCompass-5 TOOL-aTunedCompass-6 TOOL-aTunedCompass-7 TOOL-aTunedCompass-8 TOOL-aTunedCompass-9 TOOL-aTunedCompass-10 TOOL-aTunedCompass-11

# aTunedCompass — spec audit of the eleven-unit set, round 1: the instruments that grade the instruments

*Node `a`, 2026-09-05. A Tier-2 adversarial pass over the eleven specs as DESIGNS, not over code:
underspecification, internal contradiction, unstated assumption, and prior art this repo already
owns. A primed finder fan, a skeptic stage prompted to REFUTE every finding, one synthesis. Every
claim any finding made about existing code was re-checked at source during synthesis; the two
claims that moved on that re-check are named inside the findings that carried them. The parent
report `aWeighedCompass` is taken as measured fact and was not re-derived.*

**Round: 1.** Subjects, pinned at the blobs they were read at:

- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-1.md@dd2d6e6e6a767d1ca8b37e940bfc039fcd868584`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-2.md@f12d9d8f2cade5560ba1d2794a2d64b72c6f80b3`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-3.md@e3cc1315289ad10f8c27556313736cbe299e1061`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-4.md@671db4f1627bbdfc7a3fa9d2d8b97c350fe6a57c`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-5.md@27d38500a9636ea586673d2d56221ece8ed017c3`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-6.md@0518ec0c5bd61237b32c509696983f2413bb7d81`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-7.md@5dca3d1b69761f07d452e55e1a07baedad1175bf`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-8.md@30011d2c88adbcc266f18a31566718925f6a7a5d`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-9.md@105bffb17da55a2906d928fbc42489b754b676df`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-10.md@8e668fe43371a9149daa346cfe43bae317da6e88`
- `memory/builds/aTunedCompass/spec/2026-09-04-spec-TOOL-aTunedCompass-11.md@a911b1f4504fd2d48f427772a02049b8fabfb3bb`

## Verdict: BLOCKED

Three blockers, seven highs, nine mediums, one low. The three blockers are not wording slips. Each
is a unit whose acceptance set, followed literally, produces either a build that cannot pass its own
criteria or a green result that proves nothing, and no gate in this repo catches a spec disagreeing
with itself.

The set's failure mode is one shape repeated. An owner resolution or a revision changed what a unit
claims, and the change was written into the fork or the revision log but never propagated into the
scope list, the Files-touched table, or the acceptance criteria that a builder actually works from.
Eight of the twenty defects below are that shape. It is the single highest-value thing to gate.

Units 1 and 7 drew no confirmed finding. Both are Tier-1, both are short, and with the lens fan
intact that is weak positive evidence — it is not a clean bill.

### Review shape

Raw 57, confirmed 27, refuted 30, unverified 0, precision 0.47.

The 27 confirmed findings resolve to **20 distinct defects**: five defects were reported by more
than one lens at different addresses, and the severity adjudicated here is mine, not the reporting
lens's. Each merged entry names its source ids. Precision at 0.47 sits right at the line §8 names as
the point to tighten scope rather than add agents, which is worth noting for round 2 — the refuted
half was dominated by findings that read a spec's prose as a promise the template does not make.

### Run integrity

- Lenses 4/4 returned, 0 DIED.
- Skeptic batches 5/5 returned, 0 DIED.
- 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates.
- 0 outstanding unverified findings.

Every count is zero, so no lens gap qualifies the finding set. A zero here is evidence.

### Severity ledger

| # | Sev | Unit | Address | The defect | Source ids |
|---|---|---|---|---|---|
| B1 | blocker | 9 | §2 S2, §4, §6 AC1/AC2 | `expected_paths` cannot express "the passage, not the record" | 37, 48 |
| B2 | blocker | 4 | §4 Migration + Files touched, §6 AC9 | AC9 asserts a cache hit the unit's own kit-version bump forbids | 16, 39, 49 |
| B3 | blocker | 6 | §8 F2 vs §2 S6, §3, §4, §6 AC4 | the resolved replay harness exists in no scope item, and unit 10 depends on it | 3, 20, 51 |
| H1 | high | 11 | §2 S2/S3, §4 (absent), §6 AC1, §7 | a new `.unattended.conf` key needs four carriers; the spec names one | 41 |
| H2 | high | 11 | §2, §6, §7 | the watched-path edit owes a `last-audit` re-stamp no item covers | 1 |
| H3 | high | 9 | §2 (no `kit.toml` item), §3, §8 F2 | the new fixture ships to every adopter | 42, 50 |
| H4 | high | 4 | §2 S8, §6 AC1/AC3, §8 F1 | the headline measurement names two different fields, neither of which answers it | 40 |
| H5 | high | 8 | §6 AC4, §4 | AC4's premise is a `GIT_DIR` mechanism the kit does not have | 38 |
| H6 | high | 4 | header `order 1` vs §4, §6 AC4 | the unit depends on a fixture that does not exist at its declared order | 17 |
| H7 | high | 4 | §2 S6, §6 AC5, §8 F1 | scope mandates the measurement the resolution defers | 18 |
| M1 | medium | 9, 10, 11 | §6 | criteria carry no `AC` labels, so the resolutions cite unresolvable ids and check 23 reds | 31 |
| M2 | medium | 11, 9 | §7 vs §2 | §7 points at an `S6` that does not exist; the test arms are unscoped | 33 |
| M3 | medium | 9 | §2 S3/S5, §6 | the new fixture inherits neither the provenance rule nor the tautology audit | 52 |
| M4 | medium | 11 | §2, §6 AC1 | `MAP_CLI` is never declared in this repo's own conf, so the reader ships switched off | 47 |
| M5 | medium | 10 | §2 S6, §6 crit 4 | pins "133 graded phrases" that unit 6's scope does not commit to producing | 55 |
| M6 | medium | 10 | §2 S1/S2 | the population figures are the raw symbol index, not the corpus the arm sees | 28 |
| M7 | medium | 9, 10, 11 | §5 | the ten-line readiness sweep is collapsed to four or five prose clauses | 32 |
| M8 | medium | 4 | §2 S3, §6 | the second fusion call site is required by scope and observed by nothing | 5 |
| M9 | medium | — | `README.md` roster vs generated region | the authored roster contradicts the generated status on eight rows | 34 |
| L1 | low | 8 | §3, third bullet | `order 2` in the body against `order 3` in the header | 25, 57 |

---

## Blockers

### B1 — unit 9: `expected_paths` cannot express the property the whole unit rests on

*`spec/2026-09-04-spec-TOOL-aTunedCompass-9.md`, §2 S2, the discrimination argument in §4, and §6
criteria 1 and 2. Source ids 37, 48.*

The unit exists to build a fixture that can tell the two-set ensemble from its records half. §4's
load-bearing claim is that a passage inside an anchored record "is not answerable by returning the
enclosing record". S2 adopts `expected_paths` as the target mechanism, and that mechanism cannot
express the claim.

`bench.expected_by_target` resolves a path target by whole-FILE equality
(`tools/memory-recall/bench.py:362-365`, `hits = {i for i,r in enumerate(docs) if r["path"] == tp}`),
and a record-level document carries the enclosing file's own path (`tools/memory-recall/extract.py:499`).
So for exactly the question shape S1 names, the `records` set satisfies the target by returning the
record — the case §4 argues is impossible.

Two consequences. AC1, the unit's only real requirement, is left to ranking luck rather than to the
expectation mechanism: `records:fts5` may still come in under 1.000, but nothing in the design makes
it. AC2 is worse than weak, it is vacuous — "chunks `ceiling` is 1.00, proving the expected passages
exist" is true of any file that has chunks at that path, which is every file. Units 2 and 3 are
blocked on this fixture, and unit 3 would later pin the merge bar to a floor resting on it.

The prior art is already in this repo, twice. `bench.py`'s own docstring at `:340-347` warns that
path matching credits all ~40 chunks of a long file, and the `aWalkedCorpus` round-1 review's F2
ruled that an `expected_paths` question needs a deliberate stated exception.

One correction from synthesis: the source finding called AC1 "unreachable". It is not unreachable,
it is unguaranteed — AC1 is an empirical measurement and could come out below 1.000 by ranking
alone. The mechanism/property mismatch and the vacuous AC2 stand.

**Fix.** In S2, name a target kind a record-level document cannot satisfy: chunk-level
`expected_ids` resolved through the anchor map plus an in-text id match, or a per-question target the
unit defines. Add a §4 paragraph stating why `expected_paths` alone is defeated by the record
sharing the path. If `expected_paths` is kept, restrict it to files carrying no anchored record and
say so — that is the only case where it discriminates.

**Left-shift gate.** Extend the fixture audit `check-recall.py --audit-fixture` already owns with a
discrimination arm: for every question carrying `expected_paths`, report whether the `records` set
alone resolves the target, and fail on a question it does resolve unless that question carries a
stated exception. This makes `aWalkedCorpus` F2's ruling machine-checkable instead of remembered,
and it gates the CLASS rather than this one fixture.

### B2 — unit 4: AC9 asserts a cache hit that the unit's own Files-touched forbids

*`spec/2026-09-04-spec-TOOL-aTunedCompass-4.md`, §4 "Migration" and "Files touched" against §6 AC9.
Source ids 16, 39, 49.*

AC9 requires that a pre-change warm cache reports `cached` rather than a rebuild. §4 Files touched
bumps `KIT_MEMORY_RECALL_VERSION`. That constant is inside the hashed digest blob
(`tools/memory-recall/recall_conf.py:229`), and `query.ensure_cache` keys freshness on
`man.get("conf_digest") == CONF.digest()` (`tools/memory-recall/query.py:602`), printing
`rebuilt Ns` otherwise (`:1197`). The criterion is unsatisfiable at any ordering: the version bump
moves the digest, so the run rebuilds.

This is not an open question the set left standing. `Conf.digest`'s docstring says out loud that the
kit version is in the blob and prices "one rebuild per kit bump", and sibling unit 5's S7 states the
identical mechanism correctly for the same kit. Unit 4 is the document that disagrees with the
repo and with its own sibling.

The failure mode if it ships unfixed is the bad one, not the loud one. A builder who hits the red
criterion has two exits, and the tempting one is to drop the kit-version bump — which is the field
`check-kit-versions.sh` and the selftest marker arm force for a behaviour change. The other exit is
to "verify" AC9 by checking only `CACHE_VERSION` and reporting a cached run that never happened.

**Fix.** Rewrite AC9 to observe what actually holds: `CACHE_VERSION` did not move, and the single
rebuild the run performs is attributable to `conf_digest` — assert `man['version'] == CACHE_VERSION`
on the old manifest, that the first post-change run rebuilds with the digest named as the cause, and
that the second reports `cached`. Correct §4 Migration, which currently claims no rebuild is forced.

**Left-shift gate.** Make the mechanism self-announcing rather than remembered: have `query.py`'s
rebuild line print the CAUSE (`conf_digest`, `CACHE_VERSION`, or absent manifest) beside `rebuilt Ns`.
An acceptance criterion can then name the cause and become observable, which is the property this
whole build exists to restore. Pair it with a §10 checklist entry, since the spec-level half is not
gateable: an AC asserting a cache HIT is checked against the digest's declared input list before it
is written.

### B3 — unit 6: the resolved replay harness exists in no scope item, and unit 10's acceptance depends on it

*`spec/2026-09-04-spec-TOOL-aTunedCompass-6.md`, §8 F2 RESOLVED against §2 S6, §3's last bullet, §4
"Files touched", and §6 AC4. Source ids 3, 20, 51.*

F2's resolution and rev-3's log commit the replay harness as a tracked, registered, on-demand script
that runs on no leg and therefore "owes a declared wall-clock ceiling". Nothing downstream of the
fork was updated. S6 still specifies "a one-time before-and-after measurement ... recorded in this
build's folder", which is the recorded one-off the owner rejected. §3's last bullet still says the
replay "has no ceiling anyone has declared". §4 Files touched enumerates `reuse_lookup.py`,
`selftest.py`, `map_lib.py` and the dossier, calls it "Four source files", and names no script. AC4
observes only a record under `memory/builds/aTunedCompass/build/`.

A builder cannot satisfy both readings, cannot tell which file to create, and cannot tell where the
ceiling is declared. Nothing observes the script's existence, its registration, or its ceiling, and
this repo reds a suite that arrives without one.

Two knock-ons make it a blocker rather than a high. First, `tools/codebase-map/kit.toml` carries
`[[files]] include = "**" role = "engine"`, so a new file under that kit ships verbatim to every
adopter — here, a harness that parses this repo's own build records for probe phrases. That is the
same shipping defect the memory-recall descriptor was written to prevent. Second,
`TOOL-aTunedCompass-10`'s S6 and its criterion 4 depend on "the replay harness `TOOL-aTunedCompass-6`
commits" — an artifact unit 6's scope does not produce, so unit 10's acceptance breaks with it.

**Fix.** Add a scope item naming the harness's tracked path, its explicit `[[files]]` role in
`tools/codebase-map/kit.toml` (`project-owned`, mirroring how the memory-recall kit withholds its
fixture), and where its wall-clock ceiling is declared — the unattended kit's on-demand runner is
the precedent F2 invokes and it carries its budget in the script itself. Add all of it to §4. Add an
AC observing that the path is tracked, that `govkit selfcheck` and the bar's testsuite count stay
green with it declared, and that the ceiling is enforced by the runner that owns it. Delete the
stale §3 bullet and rewrite S6's one-off wording.

**Left-shift gate.** A hygiene check that every RESOLVED fork in §8 carries a `folded into:` pointer
naming the `S<n>` and `AC<n>` items that absorbed it, and that the pointer resolves against §2 and
§6. This is the set's dominant defect shape — a resolution written into the fork and never
propagated — and it accounts for B3, H7, and half of H6. One check, three defects, and it turns the
propagation step into something a machine notices instead of something a reader has to.

---

## High

### H1 — unit 11: a new `.unattended.conf` key has four carriers and the spec names one

*`spec/2026-09-04-spec-TOOL-aTunedCompass-11.md`, §2 S2/S3, §6 AC1, §7; no §4 Files-touched list
exists. Source id 41.*

`MAP_CLI` cannot be declared in the driver alone. `check-unattended.sh` check 22 (`:1372-1420`)
joins `tools/unattended/.unattended.conf.example` against §8's key table in
`memory/guides/UNATTENDED-PROTOCOL.md` in both directions, plus a third direction over the project's
own conf. Check 10 (`:1323-1345`) byte-compares that installed guide against
`tools/unattended/PROTOCOL.template.md` after prefix substitution. The spec names only
`unattended.sh:3588`.

`unattended kit gate` runs `check-unattended.sh` with `subject = repo` and a null guard, so it is on
every ordinary bar, and §7 names it as binding. The landing commit reds with "undocumented in the
protocol: MAP_CLI", and `PROTOCOL.template.md:338`'s `reuse-probed` row keeps describing a
recall-only item. The protocol also carries a byte cap that §7 of that document was moved out to
relieve, and no section here budgets the new rows against it.

**Fix.** Add scope items and a §4 Files-touched list covering
`tools/unattended/.unattended.conf.example`, §8's key table and the `reuse-probed` row in
`PROTOCOL.template.md`, the re-rendered `memory/guides/UNATTENDED-PROTOCOL.md`,
`tools/unattended/kit.toml`'s `optional_keys`, and `unattended.sh`'s default init. Add an AC that
checks 10 and 22 pass with the key present. Price the protocol's byte cap the way
`TOOL-aTunedCompass-7` prices the manifest's.

**Left-shift gate.** The cheapest universal ratchet catches this and H2 together: a hygiene check
refusing a Tier-2 spec with no §4 Files-touched list. Unit 11 has none, which is why both omissions
were invisible. On top of that, a check that a spec whose body introduces a new `.unattended.conf`
key names every carrier the kit's check 22 joins — the carrier list is derivable from
`check-unattended.sh` itself rather than typed into the checker.

### H2 — unit 11: the watched-path edit owes a `last-audit` re-stamp no item covers

*`spec/2026-09-04-spec-TOOL-aTunedCompass-11.md`, §2 S2, §6 AC1, §7. Source id 1.*

S2 puts the `MAP_CLI` declaration "beside `RECALL_CLI`", and this repo declares `RECALL_CLI` in
`.unattended.conf:70`. `.unattended.conf` is the ninth entry on the `watch:` line of
`memory/guides/SESSION-KICKOFF.md:6`. Check 5 of `skills/session-kickoff/manifest-check.sh` is
exactly "no unaudited watch drift", and the blocking pre-commit variant requires the re-stamp
bundled into the same commit. No scope item, no criterion, and no gate name in §7 covers it, so the
landing commit reds `kickoff-manifest ratchet`.

Unit 11 is the one spec in the set that touches a watched path without carrying this obligation.
`TOOL-aTunedCompass-2` carries it as S10 plus AC8, and `TOOL-aTunedCompass-3` as AC10, both for
`.memory-tree.conf`. This is inconsistency inside the set, not an open question, and the commit is
refused by a hook rather than argued about in review.

**Fix.** Add an S-item mirroring unit 2's S10 (re-stamp `last-audit`, advance `last-body-change`,
delta line in the commit message), add `kickoff-manifest ratchet` to §7, and add an AC in unit 2's
AC8 shape: when `bash skills/session-kickoff/manifest-check.sh` runs on the landing commit it exits
0 against the re-stamped `last-audit`.

**Left-shift gate.** A hygiene check that intersects a spec's §4 Files-touched with the `watch:`
line read live out of `memory/guides/SESSION-KICKOFF.md`, and requires the `kickoff-manifest ratchet`
leg in §7 on any hit. Both sides are machine-readable and neither is authored twice. Note the
recorded gotcha "Stamps are not one stamp" — the remedy names three carriers where five exist, so
have the check name the full set rather than restating a subset.

### H3 — unit 9: the new fixture ships to every adopter

*`spec/2026-09-04-spec-TOOL-aTunedCompass-9.md`, §2 (no `kit.toml` item), §3 non-goals, §8 F2's
resolution. Source ids 42, 50.*

`tools/memory-recall/kit.toml` claims the kit dir with `[[files]] include = "**" role = "engine"`,
and `govkit.py`'s `LANDABLE_ROLES` is `(engine, seed)`, so an engine-claimed file is written by
`apply`. The three gov-only files are withheld only by an explicit `project-owned` rule naming
exactly three literals, and the `cp -r` path is separately handled by the
`rm -f {check-recall.py,recall-fixture.json,test_recall_floor.py}` line at `WIRE-INTO-PROJECT.md:364`.

F2 resolves to a second fixture beside the existing one, i.e. inside the kit dir, so it defaults to
`role = engine` and ships through both paths. The spec claims neither carrier and carries no
non-goal for it. What an adopter would receive is a question set sampled from this repo's own query
log and keyed on this repo's record ids — the outcome the `kit.toml` comment forbids by name,
citing `memory/gotchas/pin-copied-from-another-corpus.md`. `TOOL-aTunedCompass-2`'s §3 asserts the
withholding "stays true", so this is the set contradicting itself.

**Fix.** Add a scope item claiming the new fixture path as `role = "project-owned"` in
`tools/memory-recall/kit.toml` beside the existing three, and adding it to the removal line in
`WIRE-INTO-PROJECT.md`. Add an AC observing that `govkit`'s apply path does not land it in a target
and that the runbook's list names it.

**Left-shift gate.** A check that every path under `tools/<kit>/` named in any spec's §4
Files-touched is claimed by an explicit `[[files]]` rule with a stated role in that kit's
`kit.toml`. The default-to-shipping behaviour has burned this repo once already and is recorded as a
gotcha, which is precisely the bar for turning a remembered rule into a gate.

### H4 — unit 4: the headline measurement names two fields, and neither answers it

*`spec/2026-09-04-spec-TOOL-aTunedCompass-4.md`, §2 S8, §6 AC1 and AC3, §8 F1's resolution. Source
id 40.*

AC1 asks for each path appearing "at most once FROM THE CHUNK SOURCE". That cannot be observed from
the field the spec names. `shown_paths` is documented in-code as "Paths only" with no `set` label
(`tools/memory-recall/query.py:1251`), so the records arm contributes the same path indistinguishably.
The only field carrying `set` is `results`, and it is truncated at `RESULT_CAP = 5` (`:136`, emitted
at `:1241`).

Compounding it, F1's resolution names `results` as the evidence while S8 and AC3 name `shown_paths`.
Those are two different populations — a five-slot prefix against the full emitted list — yielding
two different duplicate rates. The de-duplication measurement the owner's resolution makes the
unit's whole claim therefore has no single defined source.

**Fix.** Pick one field and say what it can answer. Either drop the "from the chunk source"
qualifier and make AC1 and AC3 the total duplicate-path rate over `shown_paths` before and after, or
add a scope item that records per-slot provenance for the measured runs — an instrumented run, or a
widened `results` for the measurement only — and name which.

**Left-shift gate.** A check that any emitter field named in a spec's §6 exists in the emitting
program's declared output keys. `query.py`'s JSON keys are enumerable, and a criterion citing a field
that does not carry the label it is being asked for is exactly the "criterion that cannot fail"
class. The durable half is a code change: label the source on every emitted slot, or stop emitting
the unlabelled list.

### H5 — unit 8: AC4's premise is a mechanism the kit does not have, and running it contaminates the evidence

*`spec/2026-09-04-spec-TOOL-aTunedCompass-8.md`, §6 AC4, with §4 "Where it is written". Source id 38.*

AC4 assumes the log path resolves through `GIT_DIR`. It does not. `_resolve_git_dir`
(`tools/codebase-map/reuse_lookup.py:392-404`) is pure path math over `root/.git` with an explicit
"NO child process" docstring, and `root` is `m.repo_root()`, which reads only `CODEBASE_MAP_ROOT`
(`map_lib.py:113-119`). `GIT_DIR` appears nowhere under `tools/codebase-map/`.

So the criterion cannot fail for the reason it names, and run as written it does the opposite of
what it asserts: with `GIT_DIR` pointed at nothing the probe still resolves the real common dir and
APPENDS a row to the live `lookups.jsonl`. The criterion guarding the never-fatal write both
certifies nothing and writes into the corpus AC5 exists to protect.

**Fix.** Restate AC4 against the real mechanism: run with `CODEBASE_MAP_ROOT` pointed at a scratch
tree with no `.git` (or whose `.git` file names a missing gitdir), assert candidates still print,
exit 0, no row written anywhere, and the real log's hash unchanged. Have §4 state that the
resolution is `root/.git` plus `commondir`, not the git environment.

**Left-shift gate.** Two, both cheap. A hygiene check extracting `[A-Z][A-Z0-9_]{3,}` tokens that a
§6 criterion presents as environment variables and requiring each to grep-hit inside the paths named
in §4 — zero hits is a red, and it catches a false premise at spec time for the price of a grep. And
a kit rule with teeth: any criterion that exercises the probe runs under a `CODEBASE_MAP_ROOT`
scratch tree, with the selftest asserting the real log is byte-unchanged after the arm.

### H6 — unit 4: `order 1` against a dependency on `order 2`, and an AC that needs it

*`spec/2026-09-04-spec-TOOL-aTunedCompass-4.md`, the status header against §4's "Why this depends on
unit 2" and §6 AC4. Source id 17.*

The header reads `order 1`. §4 still carries a heading declaring the unit depends on
`TOOL-aTunedCompass-2`, which is `order 2` and BLOCKED, and AC4 requires running bench against "the
terms-carrying fixture" that only unit 2 creates. rev-2 moved this unit from order 3 to order 1 on
F1's de-duplication result and left both untouched; its own log claims "nothing it now claims
depends on the fixture", which the body contradicts.

At its declared order AC4 is unsatisfiable, and the build-order region the README derives from these
headers is wrong. Unit 8's rev-2 caught and fixed this exact ordering-axis defect, so the class is
already known to the build.

**Fix.** Delete the "Why this depends on unit 2" sub-head, whose content is now historical, and
either drop AC4 or mark it deferred alongside AC5 with an explicit `until TOOL-aTunedCompass-2
lands` clause, so the order-1 acceptance set is exactly what an order-1 unit can observe.

**Left-shift gate.** A hygiene check that a spec body naming a sibling unit as a dependency must not
name one whose header `order` is greater than or equal to its own. Both sides are already parsed —
`gen_build_index.py` reads the headers to render the build-order region — so this is a comparison,
not a new parser. The same check retires L1.

### H7 — unit 4: scope mandates the measurement the resolution defers

*`spec/2026-09-04-spec-TOOL-aTunedCompass-4.md`, §2 S6 and §6 AC5 against §8 F1 RESOLVED. Source id
18.*

S6 makes running the F1 measurement in-scope: "the measurement that settles §8's F1 is run and its
result recorded ... The unit does not land on an assumption about the ensemble", and §5's risks
repeat it. F1's resolution says the opposite: "AC5 is explicitly deferred until unit 9 reports and
this unit claims nothing about ensemble recall in the meantime". AC5 nonetheless sits in §6 with no
deferral qualifier.

The Definition of Done therefore contains a criterion the owner's resolution forbids the unit from
meeting, and a scope item mandating the measurement the resolution defers. A builder cannot tell
whether the unit is done without AC5, and the acceptance ledger will have to answer a line that was
never allowed to run.

**Fix.** Rewrite S6 to name only the de-duplication measurement (S8's before and after), and prefix
AC5 with `DEFERRED — TOOL-aTunedCompass-9` so the deferral is visible in the acceptance section
rather than only inside the resolved fork.

**Left-shift gate.** Covered by B3's `folded into:` pointer check, plus one clause: an AC that a
RESOLVED fork names as deferred must carry a `DEFERRED` marker in §6. A deferral recorded only in
§8 is a deferral the acceptance ledger cannot see.

---

## Medium

### M1 — units 9, 10, 11: §6 numbers no criterion, and check 23 reds on close

*`spec/…-9.md`, `…-10.md`, `…-11.md`, §6 against §8. Source id 31.*

All three write §6 as a bare `1.`…`6.` ordered list while their §8 resolutions veto options by citing
AC1/AC4/AC5 (unit 9), AC1/AC2 (unit 10) and AC6 (unit 11) — labels the section never defines. The
resolutions' entire veto reasoning points at identifiers a reader cannot resolve.

Not cosmetic. Check 23 of `tools/memory-tree/check-memory-hygiene.sh` matches criteria with
`^([ \t]*(-|\*)[ \t]*)?(\*\*)?AC[0-9]+` (`:1477`) and fails with `alnolab` — "a CLOSED Tier-2 spec
carries an acceptance-criteria section that numbers no criterion, so every claim about its coverage
is vacuously true" (`:1525`). These three red the hygiene gate the moment they close, and the
acceptance-ledger grammar keys each answered line to an `ACn` label, so they cannot produce a
conforming ledger. `TEMPLATE-SPEC` §6 lists three permitted label forms and a bare number is not one.
The other eight specs use `- **AC1** — `.

**Fix.** Relabel §6 in all three as `- **AC1** — ` matching their siblings. No criterion text needs
to change.

**Left-shift gate.** Already gated — check 23 — but it fires at CLOSED, which is far too late for a
label the owner's own resolutions cite at scope approval. Move the label arm to fire at SPECCED as
well. That is a guard relocation, not a new check.

### M2 — unit 11 §7 points at an `S6` that does not exist, and unit 9 mirrors it

*`spec/…-11.md` §7 against §2; `spec/…-9.md` §7 against §2. Source id 33.*

Unit 11's §2 ends at S5 (reader, `MAP_CLI` declaration, declaration-not-probe, ledger correction,
spec correction), while §7 says "S6's arms run through `bash tools/unattended/run-unattended-gates.sh`
on demand". The three arms §5 names — adopted-and-present, adopted-and-empty, not-declared — and
which criteria 2, 3 and 4 require, appear in no scope item at all. A builder working from §2 ships
the reader with no test arms, and §7 points at a scope id that does not exist. Unit 9 has the mirror
defect: its S6 is a report rather than an arm, and the `selftest.py` arm criterion 6 requires is
likewise unscoped.

**Fix.** Add an S6 to unit 11 naming the three arms and their suite, and correct unit 9's §7 to
point at the scope item that actually holds its `selftest.py` arm once one is added.

**Left-shift gate.** A hygiene check that every `S<n>` and `AC<n>` cross-reference anywhere in §3–§8
resolves to a defined item in §2 or §6. It shares its parser with M1's label arm, so the marginal
cost is a few lines, and it is the same "dangling id" class the repo already knows from
`memory/gotchas/citing-a-dangling-id-creates-it-as-an-orphan.md`.

### M3 — unit 9: the new fixture inherits neither the provenance rule nor the tautology audit

*`spec/…-9.md` §2 S3/S5 and §6. Source id 52.*

The committed fixture's `_README` carries a PROVENANCE RULE — every question's answer determined by
a person writing a record that states it, cited in `from` — and the anti-tautology rule
`check-recall.py --audit-fixture` enforces against `OVERLAP_MAX` (`:87`). The sampled, agent-judged
set inherits neither. Worse, nothing on the bar would audit it even if it did: `check-recall.py:303`
defaults to `KIT / FIXTURE_NAME`, a single constant, and the bar's argv passes no `--fixture`.

Unit 3 is to pin the merge bar against this population — F2's own resolution says so — so an
unaudited set whose answers were judged rather than recorded becomes the bar's basis. F1's
resolution has an agent pick the expected passage from what the log SHOWED, which is the direction
`memory/gotchas/fixture-passes-by-finding-nothing.md` names as the failure.

**Fix.** State in S5 which of the two rules the new set inherits. Give each question a `from`, or
record a written waiver of the provenance rule with its reason. Add an AC running
`check-recall.py --audit-fixture --fixture <new file>` and requiring every question under
`OVERLAP_MAX`.

**Left-shift gate.** Make `--audit-fixture` iterate every fixture under the kit rather than the
single `FIXTURE_NAME` constant. Derive over author: a second fixture is then audited the day it
lands, and nobody has to remember to widen a constant.

### M4 — unit 11: `MAP_CLI` is never declared in this repo's own conf

*`spec/…-11.md` §2 (no project-conf item) and §6 AC1. Source id 47.*

AC1 greps only `tools/`, and no scope item declares `MAP_CLI` in this repo's `.unattended.conf`,
where `RECALL_CLI="tools/memory-recall/query.py"` lives at `:70`. With `MAP_CLI` blank the
`reuse-probed` arm takes the announced-skip path (`unattended.sh:3624-3625`), so the reader ships but
stays switched off here, and `TOOL-aTunedCompass-8`'s new field lands against a consumer that reads
nothing in this tree. That is the stated reason the owner blocked unit 8 on unit 11.

The other horn is H2: if the key IS declared there, the watched-path obligation fires.

**Fix.** Add a scope item declaring `MAP_CLI` in this repo's `.unattended.conf`, an AC observing the
item counts map-log rows in THIS tree, and the re-stamp plus the `kickoff-manifest ratchet` leg the
watched-file edit then owes.

**Left-shift gate.** Folded into H2's watch-line intersection check. Add one clause: a spec claiming
a feature is adopted in this repo must name this repo's own conf in §4, not only the kit's example.

### M5 — unit 10 pins a phrase count unit 6 does not commit to producing

*`spec/…-10.md` §2 S6 and §6 criterion 4, against `spec/…-6.md` §4. Source id 55.*

S6 and criterion 4 pin "the same 133 graded probe phrases the parent report left behind". Unit 6's
§4 states the cost plainly: of 186 tracked records carrying a literal invocation, only 74 hold the
phrase on a single line inside double quotes, "so a parser that joins wrapped invocations is the
difference between grading 74 phrases and grading the parent's 133". No scope item in unit 6 commits
to building that parser, and unit 6's own AC4 deliberately declines to pin a count, asking instead
for the phrase count it actually graded.

So unit 10's criterion is either unmeetable or quietly met by grading 74 and reporting 133 — the
shape this build exists to remove.

**Fix.** Replace the literal 133 in S6 and criterion 4 with the count the harness actually graded,
recorded beside the result, matching unit 6's AC4 wording. If 133 is required, add the wrapping
parser as an explicit requirement on the harness in unit 6's scope.

**Left-shift gate.** The cross-unit half of B3's pointer check: a spec referencing a sibling unit's
deliverable must name an artifact that appears in that sibling's §2 or §4. A build is a set of
documents that promise things to each other, and nothing currently checks that a promise was made.

### M6 — unit 10 prices its argument on the wrong population

*`spec/…-10.md` §2 S1 and S2. Source id 28.*

S1 says "of 769 indexed symbols, 731 are kind `function`", measured at base `c4fcf5ad`. Unit 6's §4,
measuring the same predicate at the same base, reports 645 candidates, 616 functions and 28 classes.
Both were re-measured during synthesis: `git show c4fcf5ad:memory/map/generated/symbols.json` gives
exactly 769/731, so S1 is quoting the raw index — but the `same kind` arm iterates
`corpus.candidates` (`reuse_lookup.py:231`), which loads to 648 kinded candidates and 619 functions
at HEAD, matching unit 6's figures at base.

So S1 names a pool 19% larger than the one the arm sees, and S2's "five to seven times" reach
reduction is priced the same way: grouped by kit dir the raw index gives 152/151/135/92 functions,
while the arm's actual pool gives 134/133/101/81 — a reduction of 4.6x for the largest kit, below
the stated range. The conclusions survive. The figures do not, and two units of one build report
different denominators for one predicate at one base, which is exactly the disease this build was
opened to cure.

One correction from synthesis: the source finding's explanation was wrong. `symbols.json` holds no
private names; the gap is name-deduplication at load. The material claim checks out.

**Fix.** Restate S1 and S2 over the probe's own corpus — the `# corpus: N symbols` line a live run
prints at BASE — and re-derive the per-kit-directory group sizes from the same filtered set before
repeating the reach-reduction figure.

**Left-shift gate.** This one resists a clean gate, so it is a documented check: a population figure
in a spec is quoted from the command that printed it, with the command named on the same line.
§7 already states the rule for code ("NO count of a derived population is written in prose"); the
left-shift here is extending it to specs in `TEMPLATE-SPEC` so the next author reads it while
writing §2.

### M7 — units 9, 10, 11: the ten-line readiness sweep is collapsed

*`spec/…-9.md`, `…-10.md`, `…-11.md` §5. Source id 32.*

`TEMPLATE-SPEC` makes §5 a ten-item sweep, "one line each (what's needed, or N/A — <why>)", and
states the rationale directly: an absent line is indistinguishable from a forgotten one. Unit 9's §5
is four prose clauses (observability, testing, migration, cost), unit 10's is five, unit 11's five.
Between five and six lines are dropped each, none marked `N/A`, while units 1 through 8 carry all
ten. The dropped lines include security in units 9 and 10, and error/empty states, risks and user
docs in all three.

§5 is the section a Tier-2 unit's unresolved items become the owner's scope menu from, and these
three units were ADDED at scope approval — so the owner has never been offered a menu for them.

**Fix.** Restore all ten labelled lines in the three units, each either stating what is needed or
`N/A — <why>`, and surface anything unresolved as an owner menu item.

**Left-shift gate.** A hygiene check that a Tier-2 spec's §5 carries all ten labelled lines. Derive
the label list from `TEMPLATE-SPEC` rather than typing it into the checker, so the gate and the
template cannot drift apart.

### M8 — unit 4: the second fusion call site is required by scope and observed by nothing

*`spec/…-4.md` §2 S3 against §6. Source id 5.*

S3 requires both fusion call sites to change together — the first attempt and the rebuild after a
`sqlite3.DatabaseError` — and names the exact failure mode: "a rollup applied to only one of them
makes the served shape depend on whether the cache was healthy". Then it leaves it unobserved.
`query.py:1177` and `:1181` are two literal copies of
`rrf([search(dirp,"records",expr,k), search(dirp,"chunks",expr,k)])`, the second inside the `except`
rebuild. AC1, AC3 and AC9 all run the healthy path, AC2's selftest arm goes through the normal path,
and AC9 explicitly asserts a `cached` run. A half-applied rollup passes every criterion and surfaces
only on a corrupted cache in a live session.

**Fix.** The lazy fix is the root-cause fix: extract the fused call into one function so there is
one call site, and the existing arms then cover both paths. If the duplication stays, add an AC in
the S7 arm's shape — with the chunk cache corrupted so the rebuild path is taken, the served result
set carries the same de-duplicated shape as the healthy path for the same question.

**Left-shift gate.** Prefer deletion to a new check: one call site cannot be half-edited. Where a
duplicated pair must survive, the durable gate is a selftest arm that forces the error path, which
is the "a gate you have only ever seen pass is an assertion about nothing" rule applied to the arm
rather than the gate.

### M9 — the build README's authored roster contradicts its own generated region

*`memory/builds/aTunedCompass/README.md`, the `roster:units` region against `gen:build-units` and
every spec header. Source id 34.*

The two tables sit in the same file and disagree. The authored roster lists Status `OPEN` for eight
units, while the generated region a few lines below and those eight spec headers read `SPECCED`. The
three BLOCKED rows (units 2, 3, 8) agree. The roster is authored, not generated —
`gen_build_index.py`'s comment at `PLAN_OPEN` says a renderer writing there would corrupt a plan, and
it is listed only so the slot walk can find it — so nothing regenerates it and the staleness
persists. The README's own prose contradicts it too.

One correction from synthesis: the source finding said all eleven roster rows read `OPEN`. Eight do.
The disagreement is real on eight rows, not eleven.

This is "status is DERIVED, never authored" broken in the build's master overview, which is the
first document a reader opens.

**Fix.** Drop the Status column from the authored roster. The generated region already carries
status, and one fact in one place is the rule.

**Left-shift gate.** The gate is the absence of the field: a column that cannot exist cannot go
stale. If the column is kept for any reason, the hygiene check is a comparison of the authored
roster's status cells against the parsed spec headers, which the index generator already reads.

---

## Low

### L1 — unit 8: `order 2` in the body against `order 3` in the header

*`spec/…-8.md` §3, third bullet. Source ids 25, 57.*

The status header reads `order 3` and rev-3's §9 line says the unit "moves to order 3", while §3's
third bullet still reads "this unit carries `order 2` against that unit's `order 1`". The sibling it
names, unit 6, does carry order 1, so only unit 8's own value is stale. The generated build-order
region places unit 8 at step 3, confirming the header is the machine-read half. rev-2 of this same
spec exists to fix a header-versus-body order disagreement, and rev-3 reintroduced it in the other
direction one revision later.

The disjointness conclusion survives; a reader deriving the pass grouping from §3 reads a value the
header contradicts. The two source lenses split on severity, medium and low; I took low after
reading the file, because nothing downstream consumes the body's literal.

**Fix.** Update the §3 sentence to `order 3` and name `TOOL-aTunedCompass-11` as the blocker that
moved it, so the sentence records both reasons rather than the superseded one.

**Left-shift gate.** Retired by H6's order-consistency check: an `order N` literal in a spec body
must match that spec's header, and a named dependency must carry a lower order. Both halves come
from the same comparison, and the class has now recurred three times in this one build.

---

## What round 2 should carry

Four of the twenty defects are the same missing mechanism, and one check retires them: a RESOLVED
fork must name the scope and acceptance items that absorbed it, and the pointer must resolve
(B3, H7, M5, and half of H6). Two more (M1, M2) share a parser with it. A round-2 pass that lands
those two hygiene arms would have caught six of the twenty at authoring time, before an audit was
needed at all — which is the left-shift the charter asks for, applied to the specs themselves rather
than to the code they describe.

The residual risk this audit did NOT cover: these are designs, so nothing here says the eleven units
build the right thing, only that eight of them currently ask a builder to do two contradictory
things or to observe something that cannot fail. The parent's measurement was taken as given.
