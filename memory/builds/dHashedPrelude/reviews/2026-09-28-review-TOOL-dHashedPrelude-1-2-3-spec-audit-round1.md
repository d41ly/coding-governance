**Serves:** spec-audit TOOL-dHashedPrelude-1 TOOL-dHashedPrelude-2 TOOL-dHashedPrelude-3

# Tier-2 spec audit — TOOL-dHashedPrelude-1, -2, -3, ROUND 1

*Adversarial pre-code pass over the three-unit build that makes the memory-recall selftest's
live-query-log guard able to fail: unit 1 lifts the baseline digest out of `main()` to module scope,
unit 2 adds an arm that gates the resulting ordering, unit 3 re-derives a stale README figure and
moves the kit version. Node `d`, 2026-09-28, ROUND 1. Every finding below survived a skeptic
prompted to REFUTE it, and every line number, offset, byte count and grep population cited here was
re-read or re-run against the tree by the author of this report rather than transcribed from a lens.
Each row carries its address inside the spec, the fix, and the gate that would have caught it before
a reviewer had to.*

**Reviewed subjects, pinned at blob:**

- `memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-1.md`@`c9da51bf579d9cf13eedc40b0f8aff0683195397` — rev-1, never reviewed.
- `memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-2.md`@`e14dc1025941d19325ae09970f5bd31d22e0ff71` — rev-1, never reviewed.
- `memory/builds/dHashedPrelude/spec/2026-09-28-spec-TOOL-dHashedPrelude-3.md`@`e6d95da1e2cb7586f355a4761cfe0830aec8fc34` — rev-1, never reviewed.

All three blobs were re-hashed in the worktree at the time of writing and match the pins above.
`tools/memory-recall/selftest.py` is read here as the tree the units consume, not as a subject: no
row below grades the shipped file except where a spec makes a claim ABOUT it that is false.

## Verdict: BLOCKED

One row at BLOCKER, six at HIGH, four at MEDIUM, three at LOW. Those fourteen rows collapse to
**eight distinct defects**, and the table names which rows share one, so a fold that repairs a defect
repairs every row under it.

One defect is enough on its own. **Unit 2's arm, built as specified, reds on a correct tree**
(D-1). Section 4 stakes the whole correctness argument on first-occurrence substring search and then
never names the bytes it searches for. The obvious anchor for "the first decorated arm" is
`@check(`, and `selftest.py:145` contains that literal inside `check_provenance_chain()`'s docstring
— measured offset 7811, against 14426 for the first real decorator at :287 and roughly 14400 for the
baseline's intended home below `cleanup()`. `src.find("@check(")` therefore returns a position ABOVE
the baseline, the ordering assertion is false against the shipped file, and AC1's second clause
("Against the shipped file it reports ok") is unreachable. The unit whose entire deliverable is one
arm produces an arm that cannot go green, and section 10's reuse probe examined map seams without
ever looking at the target file's own occurrences of the anchor it depends on.

Behind that, two seams a builder would resolve by guessing. **Unit 1 is handed a false description of
the branch it relocates** (D-2): S2's "three outcomes" third state does not exist — an unreachable
repository sets `live = None` at `selftest.py:2640-2641` and the row is not emitted at all, guarded
by `if live is not None:` at :2700. A builder preserving "the three outcomes" literally emits a row
where none exists today, which moves `len(_checks)` — a behaviour change inside a unit whose S4
forbids any other movement, and one neither AC1 nor AC2 can reach, since both run in a reachable
repo. And **unit 3's AC2 cannot be signed off without ignoring its own text** (D-3): the grep it
names prints twelve lines today, not three, nine of them carrying no version at all.

The remaining five are mechanical and each carries its line number.

## Review shape

- raw 48 · confirmed 14 · refuted 34 · unverified 0 · precision 0.29
- adjudicated by ITEM: 1 BLOCKER · 2 HIGH · 3 MEDIUM · 2 LOW — eight items
- adjudicated by RAW CONFIRMED FINDING: 1 BLOCKER · 6 HIGH · 4 MEDIUM · 3 LOW — fourteen findings

The two tallies differ because six of the fourteen findings are duplicate sightings of two defects:
four lenses independently measured unit 3's AC2 grep (ids 4, 16, 30, 43) and two reported unit 1's
`(absent)` state set (ids 1, 32). Item severity is the highest severity any finding under it carried.

Precision at 0.29 sits well below the ~0.5 floor `AGENTS.md` §8 names as the point to tighten scope
or priming rather than add agents. The refuted two thirds were dominated by lenses re-deriving the
same four AC2 grep sightings from different angles and by finders grading `selftest.py` itself —
which is the tree these units consume, not a subject of this audit. **The next round over this build
should narrow the lens brief to the three spec documents and hand every lens the AC2 measurement as
already-known**, rather than adding coverage.

## Run integrity

- lenses 4/4 returned, 0 DIED
- skeptic batches 5/5 returned, 0 DIED
- 0 contradictory verdicts demoted to unverified · 0 spurious verdicts discarded · 0 duplicates dropped

No lens died, so a zero count in this report is evidence of absence within the lens brief that was
run. It remains bounded by that brief: this pass audited the three specs as designs and did not
review `selftest.py` for defects of its own beyond the claims these specs make about it.

## The defects

| # | Sev | Ids folded | Subject | Address | One line |
|---|-----|-----------|---------|---------|----------|
| D-1 | BLOCKER | 29 | unit 2 | spec-2 §4, §10 | The arm's unnamed anchor resolves 142 lines above its target, so the arm reds on a green tree |
| D-2 | HIGH | 1, 32 | unit 1 | spec-1 §2 S2, §5, §6 | S2's third "outcome" is a state the code does not have; the real fourth state is observed by nothing |
| D-3 | HIGH | 4, 16, 30, 43 | unit 3 | spec-3 §6 AC2 | The criterion's own grep prints twelve lines, not three — it cannot go green on a correct build |
| D-4 | MEDIUM | 17 | unit 2 | spec-2 §5, §4 | The declared defence against green-by-absence is an unreachable branch |
| D-5 | MEDIUM | 6, 31 | unit 2 | spec-2 §6 AC3 | The figure is read off an instrument that does not carry it |
| D-6 | MEDIUM | 22 | unit 3 | spec-3 §1, vs spec-1 §3 | Two specs give opposite accounts of which unit occasions unit 3's edit |
| D-7 | LOW | 9, 38 | unit 1 | spec-1 §2 S1, §4 | "The earliest point" is the latest such point, by about fifty lines |
| D-8 | LOW | 37 | unit 1 | spec-1 §5 | The perf row prices a 120 KB file; the file is 1,545,472 bytes |

---

### D-1 — BLOCKER — the arm's anchor resolves above its own target, so unit 2 ships an arm that reds on a correct tree

*ids folded: 29. Address: `spec-TOOL-dHashedPrelude-2.md` §4 Design, "compares three offsets in the
text"; and §10 Reuse audit.*

Section 4 says the arm "reads `__file__` and compares three offsets in the text: the module-scope
assignment, the first decorated arm, and the start of `main()`", and then builds its entire
correctness argument on first-occurrence search semantics — "if the assignment is moved into
`main()`, the first occurrence of the assignment literal becomes the arm's own string constant". It
never names the bytes any of the three searches look for.

Measured in the target file:

| anchor | `src.find(...)` offset | line |
|---|---|---|
| `@check(` | 7811 | 145 — inside `check_provenance_chain()`'s docstring |
| `\n@check(` | 14426 | 287 — the first real decorated arm |

`selftest.py:145` reads ``counting `@check(` decorators by reading the source — grades TEXT rather
than EXECUTION, which``. Spec-1 S1 puts the baseline below `cleanup()` (ends :281) and above the
arms banner (:284), so its offset lands near 14400 — ABOVE 7811. The ordering assertion
`offset(baseline) < offset(first arm)` is therefore **false against a correct shipped file**, and
AC1's second clause, "Against the shipped file it reports ok", is unreachable. An arm that fails on
the thing it certifies is the exact class this build exists to close, reproduced inside the closing
mechanism.

The same trap sits on the third offset: `def main() -> int:` is a unique string today, but nothing in
the spec says the search must be newline-anchored, and the arm's own source will contain whatever
literal it searches for.

Section 10 is the reason this went unseen. Its reuse probe ranked map seams and the name stem `run`;
it never enumerated the target file's own occurrences of the anchors the design depends on, which is
a two-second grep.

**Fix.** Name the exact anchor bytes in §4 and make them newline-anchored: `\n@check(` for the first
decorated arm, `\n_LIVE_LOG_BEFORE = ` for the assignment, `\ndef main() -> int:` for `main()`. Add
an AC that greps the shipped file for EVERY occurrence of each anchor and asserts the intended one is
first — `grep -c` on the plain form and the anchored form, with the two counts stated. Section 10
should record the occurrence census as part of the reuse pass.

**Left-shift gate.** Two, and the cheap one is worth more. (1) Product: the arm itself asserts its
anchor is unambiguous — `assert src.count("\n@check(") >= 1` and that the plain-find offset and the
anchored offset differ, so a future edit that introduces a second matching literal reds here rather
than silently re-pointing the comparison. (2) Corpus: a row in `memory/gotchas/` for the class
`anchor-literal-resolves-above-its-target`, so `python tools/memory-tree/gotchas.py --for-diff` surfaces
it on any diff that adds a `str.find`-over-`__file__` comparison. The general rule it instantiates is
already in §7 of the charter — run a candidate predicate over the real tree before wiring it, and
print hits AND near-misses — and this is the sighting that earns it a row.

---

### D-2 — HIGH — S2 preserves a state the code does not have, and the state it does have is observed by nothing

*ids folded: 1, 32. Address: `spec-TOOL-dHashedPrelude-1.md` §2 S2; §5 "error / empty / loading
states"; §6 (no criterion exists for it).*

S2 tells the implementer that "the three outcomes it can report are unchanged: a matching digest is
ok, a differing one is FAIL, and an unreachable repository yields the `(absent)` sentinel on both
ends." The third is false. At `selftest.py:2637-2641`:

```
    except Exception:  # noqa: BLE001 — no repo, no log to protect
        live, before = None, "(absent)"
```

and the emitter at :2700 is guarded:

```
    if live is not None:
```

So on an unreachable repository `before` is dead and **no row is emitted at all**. The state that
really produces `(absent)` on both ends is a different one — a reachable repo whose log file does not
exist, where `live.exists()` is false at both readings — and S2 never mentions it. §5's state-set row
propagates the error verbatim ("S2's three outcomes are the state set, and each is preserved").

The consequence is not academic, because unit 1 is the unit that moves this branch. Lifting the
try/except to module scope makes `_LIVE_LOG = None` an import-time outcome, and the implementer then
has two ways to go: drop the `if _LIVE_LOG is not None:` guard and crash on `None.exists()`, or keep
it and silently omit the row. An implementer preserving "the three outcomes" literally takes a third
route and emits a reassuring `ok` row where none exists today — which moves `len(_checks)`, inside a
unit whose S4 says nothing else in the file moves, and which is a green-by-absence of exactly the
class this build exists to close, on the same row it exists to repair.

Neither AC1 nor AC2 can reach any of this: both run in a reachable repository.

**Fix.** Rewrite S2 to name the four real states: reachable repo with a log, digests equal (`ok`,
detail is the first twelve hex chars); reachable repo with a log, digests differ (`FAIL`); reachable
repo with no log file (`(absent)` at both ends, row reports `ok`); repository unresolvable (today:
no row). Then RULE on the fourth rather than preserving it — the row is emitted with the `skip`
shape naming why it could not run, never omitted, per §7's "a skip must announce itself". Add S4 a
clause that the number of appended run-property rows is unchanged in the reachable case. Add:

> **AC5** — When the suite runs against a copy with `git_common_dir()` forced to raise, the row `the
> live query log is byte-identical after this run` is PRESENT and carries the `skip` state naming the
> unresolvable repository. Red when: the row is absent from the output, which is the pre-unit
> behaviour and is indistinguishable from a clean run.

**Left-shift gate.** The AC5 arm IS the gate, and it belongs in unit 2's arm set rather than as a
one-time observation: a permanent arm that drives `main()`'s live-log branch over a forced-raise
`git_common_dir` and asserts a row is appended. Beyond this build, the durable left-shift is a
`memory/gotchas/` row for `spec-enumerates-a-state-set-the-code-does-not-have`, since the defect is
a spec claiming to preserve behaviour it never read — and the cheap manual check that would have
caught it is "open the branch you say you are preserving."

---

### D-3 — HIGH — AC2's own command prints twelve lines, so the criterion cannot go green on a correct build

*ids folded: 4, 16, 30, 43. Address: `spec-TOOL-dHashedPrelude-3.md` §6 AC2, the grep clause and its
`figure:` line.*

AC2 asserts that `grep -rn "memory-recall@1\.13\|KIT_MEMORY_RECALL_VERSION" tools/memory-recall/`
"prints three lines all carrying 1.13", and labels the figure `the three markers are DERIVED by the
grep at observation time`.

Run today with 1.12 substituted, that pattern prints **twelve** lines:

```
tools/memory-recall/kit.toml:6          version_from pattern        — no version literal
tools/memory-recall/README.md:3         gov:kit memory-recall@1.12  — CARRIES the version
tools/memory-recall/README.md:21        prose naming the constant   — no version literal
tools/memory-recall/recall_conf.py:4    gov:kit memory-recall@1.12  — CARRIES the version
tools/memory-recall/recall_conf.py:50   KIT_MEMORY_RECALL_VERSION = "1.12"  — CARRIES the version
tools/memory-recall/recall_conf.py:252  a use                       — no version literal
tools/memory-recall/recall_conf.py:359  a use                       — no version literal
tools/memory-recall/selftest.py:655,657,659,662,1396  the mutation arm  — two of them deliberately assign "0.0" and "99.99"
```

Exactly three of the twelve carry a version literal. Unit 3 edits README line 26 only, so the
population after the bump is the same twelve. The criterion is therefore false in its intended
passing state, and its `figure:` line claims a derivation the named command does not perform: the
grep does not isolate the markers, it prints every mention of the identifier. Run as written, AC2
either reds for a reason that is not the defect, or the builder quietly rewrites the grep at
observation time — which is the point at which an acceptance criterion stops grading anything.

**One overstatement in the source finding, recorded so the fold does not carry it.** Id 43 argued
that `recall_conf.py:4` "is compared by nothing the criterion names", because `check-kit-versions.sh`
grades only the constant plus the README marker. The first half is right —
`tools/check-kit-versions.sh:214-217` compares the constant against `README.md` only. The conclusion
is not: `test_version_marker` at `selftest.py:1393` scans every `gov:kit memory-recall@` in BOTH
`README.md` and `recall_conf.py` against the constant, and unit 3 §7 lists `memory-recall kit
selftest` as a gate. S2's "all three carry the same value" is bound. The AC2 defect stands on its own
without that claim.

**Fix.** Pin the observation to the three carriers rather than asserting a count over an unanchored
pattern. Either name them as addresses — `README.md:3`, `recall_conf.py:4`, `recall_conf.py:50`,
which is what S2 already enumerates — or anchor the pattern on the value forms:

```
grep -rn 'gov:kit memory-recall@[0-9]\|^KIT_MEMORY_RECALL_VERSION = ' \
  tools/memory-recall/README.md tools/memory-recall/recall_conf.py
```

which returns exactly those three lines today, verified. Then mark the line count DERIVED from the
carrier list rather than typed, and keep the selftest row `kit version constant and the gov:kit
marker agree` named as the independent observation that all three agree, with `epoch` kept for what
it actually grades.

**Left-shift gate.** This one is genuinely machine-checkable and would pay for itself across the
corpus: a spec-audit leg that **executes every shell command a spec quotes inside an acceptance
criterion** at the spec's declared BASE and reds when the criterion's stated output shape (a line
count, an exit status, a "prints nothing") disagrees with what the command actually produces. Three
of this build's nine criteria quote a runnable command; one of them was never run. Short of that, a
`memory/gotchas/` row for the existing class name `criterion-asserts-what-its-own-command-cannot-show`,
which this repo has already filed once and which recurred here unprompted.

---

### D-4 — MEDIUM — the arm's declared defence against green-by-absence is an unreachable branch

*ids folded: 17. Address: `spec-TOOL-dHashedPrelude-2.md` §5 "error / empty / loading states",
against §4 Design.*

§5 claims: "a missing literal on either side is an assertion failure naming which one, not a silent
pass; this is the arm's own guard against passing by finding nothing."

§4 establishes the opposite as a deliberate property: "Two searches are deliberately anchored on
literals the arm itself also contains", and leans on it — a moved assignment still matches because
"the first occurrence of the assignment literal becomes the arm's own string constant." If the arm's
source always contains both literals, `str.find` can never return -1 and the not-found branch is
unreachable by construction. The guard §5 advertises does not exist.

§4's companion sentence fails by the same mechanism: "A rename of the module-scope name without a
matching edit here reds too, with a message naming the missing literal." It does not. The renamed
literal resolves to the arm's own string constant, which sits below the first decorated arm, so the
red is an ORDERING failure whose message points at the wrong cause — and the next maintainer, told to
expect a not-found diagnostic, will read that red as a relocation bug.

§7 of the charter treats a declared defence that does not exist as worse than the gap it hides, which
is what makes this worth a row rather than a note.

**Fix.** Pick one. Either make the branch reachable by taking `src` as a parameter — the shape
`check_provenance_chain(src=None, pinned=None)` already uses in this very file, whose docstring says
"Args are for the arm, which drives all three failure directions over synthetic sources" — and add a
criterion driving a synthetic source that lacks the literal. Or delete both claims and state plainly
in §4 and §5 that the not-found branch is unreachable by construction and a rename surfaces as an
ordering failure.

**Left-shift gate.** The first option converts the prose into an arm and is the real left-shift: the
new arm gets the same parameterised shape as `check_provenance_chain`, and one of its ACs drives the
not-found direction over a synthetic source. That also satisfies the standing memory note "a double
you wrote grades nothing" — the guard is mutation-tested rather than asserted. Corpus row:
`guard-that-cannot-fire`, for the class where a spec's stated defence sits on a branch its own design
makes unreachable.

---

### D-5 — MEDIUM — AC3 reads the arm count off an instrument that does not carry it

*ids folded: 6, 31. Address: `spec-TOOL-dHashedPrelude-2.md` §6 AC3, third clause and its `figure:`
line.*

AC3's third clause asks that "the summary line counts one more declared arm than it did at BASE", and
its figure line says "the declared count is DERIVED from the run's own summary line".

`selftest.py:2740` prints:

```
    print(f"---- memory-recall selftest: {len(_checks) - fails - skips}/{len(_checks)} checks passed{note}")
```

`_checks` holds the 71 arms **plus five appended run-property rows** — the arm-count pin, the
provenance chain, the live-log row, the git-environment scrub and the scratch sweep — so the
denominator is 76 today, not 71, and it is a count of check ROWS, not of arms. One of those five, the
live-log row at :2702, is emitted only under `if live is not None:`, so the total is environment-
dependent (D-2's fourth state, again).

The declared arm count is printed in exactly one place: the detail of the row `the declared arm count
matches its pin`, `f"{len(order)} == SELFTEST_ARMS"` at :2687 — a row AC3's FIRST clause already
requires to be `ok`. The +1 relation happens to hold on any host where the repo is reachable, so the
criterion passes for the wrong reason; the defect is that its stated derivation names a source that
does not carry the figure, which is the repo's own figure rule broken inside a criterion.

**Fix.** Rewrite the third clause to read the count off the row that carries it: "the row `the
declared arm count matches its pin` reports `ok` with detail `72 == SELFTEST_ARMS`". Drop the
summary-line derivation from the figure line, or keep it as a separate, correctly-described
observation: the summary total moves 76 to 77, and it counts rows rather than arms.

**Left-shift gate.** Product fix, and it removes the ambiguity for every future reader rather than
just this criterion: make the summary line carry both numbers, e.g. `---- memory-recall selftest:
N/M rows passed over K declared arms`. Then the instrument AC3 instinctively reached for actually
carries the figure, and the next spec that makes this mistake cannot. Corpus row:
`figure-derived-from-an-instrument-that-does-not-carry-it`.

---

### D-6 — MEDIUM — two specs give opposite accounts of which unit occasions unit 3's edit

*ids folded: 22. Address: `spec-TOOL-dHashedPrelude-3.md` §1 Goal, second sentence, against
`spec-TOOL-dHashedPrelude-1.md` §3 Edges and §6 AC4.*

Spec-3 §1: "It has not been 18 since 2026-08-03, and **units 1 and 2** move the number again."

Spec-1 §3 Edges: "**hands-off** `TOOL-dHashedPrelude-3` — this unit changes no count, so unit 3's
README claim is unaffected by it and moves for **unit 2's reason alone**." Spec-1 AC4 pins
`SELFTEST_ARMS` unchanged at 71. Spec-2's own Edges agrees with spec-1: "this unit changes the number
of arms the suite reports, which is the occasion for unit 3's README claim to move."

Two of the three specs say unit 2 alone; spec-3's stated justification names an effect unit 1
explicitly disclaims and pins against. Buildability is unaffected — nothing routes off this sentence
— but the set contradicts itself in the one place a later reader goes to learn why unit 3 exists, and
a build record whose units disagree about what each other do is the drift this repo gates elsewhere.

**Fix.** One word: spec-3 §1 becomes "unit 2 moves the number again", matching spec-1's Edges,
spec-1 AC4 and spec-2 S3.

**Left-shift gate.** `tools/memory-tree/gen_build_index.py` already parses the `### Edges` block and
its `hands-off` / `consumes-from` declarations. Extend it to assert **edge reciprocity** — where unit
A declares an edge to unit B, unit B carries the mirroring edge, and neither side's declared effect
contradicts the other's — and red when a spec's §1 prose names a sibling unit that its own Edges
block does not. That is a real gate leg over structured text the tool already reads, and it catches
the whole class rather than this instance.

---

### D-7 — LOW — "the earliest point" is the latest such point, by about fifty lines

*ids folded: 9, 38. Address: `spec-TOOL-dHashedPrelude-1.md` §2 S1 (the justifying clause) and §4
("The earliest legal home").*

S1 places the assignment "below `cleanup()`, which is the earliest point where `git_common_dir()` and
`recall_conf` are both defined", and §4 repeats it. Measured:

| name | line |
|---|---|
| `import recall_conf` | 49 |
| `def git_common_dir` | 225 |
| `def tree` / `def cache_of` / `_SWEPT` / `def _set_writable` / `def cleanup` | 234 / 243 / 250 / 253 / 273 |
| the arms banner | 284 |
| the first decorated arm | 287 |

Both names are available from :233. The site below `cleanup()` is the **latest** such point before
the arms, not the earliest — the claim is wrong by about fifty lines. §4's own rejected alternative
argues the opposite case for the whole region ("every statement between the import block and
`cleanup()` is a definition, and no definition writes"), so the spec argues both that the site is
forced and that it is free.

No behavioural consequence: everything in the window is a definition. The cost is that a later reader
treats the sentence as a constraint and will not move the assignment when a real reason arises.

**One correction folded in.** Id 38 added that §4's rejected alternative is "argued against the same
wrong boundary". It is not — that alternative sits ABOVE :225, where re-deriving the git common
directory inline genuinely would be required, and §4's reasoning about it is sound. Only the
"earliest" claim is false.

**Fix.** Restate the constraint as what it is: the home must be below `def git_common_dir` (:232) and
above the first decorated arm (:287); below `cleanup()` is a placement CHOICE, made so the assignment
reads adjacent to the arms it brackets. Drop "earliest" from S1 and from §4.

**Left-shift gate.** Cheap and general: a spec-lint that reds on a positional superlative about a
source file — "earliest", "latest", "only", "first", "the last" — unless the sentence carries a
`file:line` address and marks the figure DERIVED. This repo already requires figures to name their
source; a positional claim is a figure about ordering and should not be exempt. Until that leg
exists, a `memory/gotchas/` row: `positional-superlative-stated-without-a-line-address`.

---

### D-8 — LOW — the perf row prices the wrong file, by 13x

*ids folded: 37. Address: `spec-TOOL-dHashedPrelude-1.md` §5, the "perf / scale" row.*

§5 prices the new import-time hash as "one extra `sha256` of a 120 KB file at import time". Measured
on node `d`, the node that wrote the spec:

- `git rev-parse --git-common-dir` → `C:/projects/coding-governance/.git`
- `.git/recall/queries.jsonl` → **1,545,472 bytes** — roughly 13x the stated figure, and append-only,
  so it grows monotonically
- `tools/memory-recall/selftest.py` → 151,442 bytes

151 KB is the size of `selftest.py`, which is the figure spec-2's §5 correctly uses for the file IT
reads — so the two specs disagree about what unit 1 hashes, and the likely cause is that the wrong
file was measured. The cost is still trivial in absolute terms, but this is the one number a reader
uses to judge hashing at import against a growing corpus, and §10 never checked it.

**Fix.** Replace with the measured size of `<git-common-dir>/recall/queries.jsonl`, marked DERIVED at
observation time rather than PINNED because the log grows; or state the cost as a throughput ("one
sha256 pass at ~n MB/s over an append-only log currently at 1.5 MB") so it does not rot on the next
query.

**Left-shift gate.** The charter already rules that no count of a derived population is written in
prose, and a file size on a growing append-only log is exactly that. The practical leg is the same
one D-3 wants: a spec-audit pass that runs the measurements a spec's §5 states, where they are
runnable, and reds on a disagreement past a declared tolerance. Failing that, a documented manual
check in the spec-audit checklist — "every size or count in §5 was measured during this audit, not
recalled" — since the cost of getting it wrong here was one wrong sentence, not a wrong build.

---

## What this audit did NOT cover

Stated so a green row above is never misread as a verified one.

- **`selftest.py` itself was not reviewed.** It is read here only where a spec makes a claim about
  it. The five appended run-property rows, the arity assertion and the provenance chain were read to
  settle D-2 and D-5 and are otherwise ungraded.
- **The version-bump ruling is a fact, not a finding.** Spec-3 §8 records it as RESOLVED by the owner
  on 2026-09-28 against §4's own recommendation. This audit grades whether unit 3 implements it
  correctly, not whether it was the right call.
- **Spec-3 carries no §5 and no §10** (it jumps §4 → §6). It is declared Tier-1, and no row above
  turns on that absence; whether the spec template permits the omission at Tier-1 was not adjudicated
  here.
- **No unit was built and no gate was run.** Every observation in this report is a read of the tree
  at `f8e38c70` or a grep/hash executed against it. The selftest suite was not run.
