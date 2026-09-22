**Serves:** diff-review TOOL-dSpentCeiling-1

# Diff review — TOOL-dSpentCeiling-1, round 1

**Range:** `70df24ea1963afd7ee12749acb3bd323e5fa239a...HEAD` · **Round:** 1 · node `d` · 2026-08-25 ·
Tier-2 · 11 commits, 28 files.

## Verdict: BLOCKED

One blocker and four distinct highs. The blocker and the first high are the same story told from two
sides: the unit removed a gate that was arguably measuring the wrong thing, and what replaced it
neither gates nor speaks. On this repo, at this commit, a charter citation to an uncapped file lands
with no red and no printed line at all — which is strictly less coverage than the instrument the unit
retired, in the exact check the unit exists to make un-silenceable.

The retirement argument itself survives review. The measurement is sound (27 movements in 17 days, 26
up; the one drop forced by check 11), check 6 genuinely does cap all six read-path members at 61440 B
each, and the 54.0% cross-kit share is the finding the budget never surfaced in 26 raises. Nothing
below argues the pin should come back. Everything below is about the landing.

## Review shape

| | |
|---|---|
| Raw findings | 31 |
| Confirmed by an adversarial skeptic | 28 |
| Refuted | 3 |
| Unverified / outstanding | 0 |
| Precision (confirmed / confirmed+refuted) | 0.90 |

The 28 confirmed raw findings consolidate into **15 distinct defects** — several lenses landed on the
same line independently, which is signal about where the diff is thin rather than noise. Each entry
below names its constituent raw ids. Merged severity counts: **1 blocker · 4 high · 6 medium · 4
low**. Raw severity counts, for comparison: 1 blocker, 7 high, 10 medium, 10 low.

Three clusters drew four lenses each — `read_declared_keys` being defined twice, the "blank pins turn
check 16 off" claim surviving in four carriers, and the notes swallow. A defect that four independent
lenses trip over is a defect sitting on the diff's main path.

---

## BLOCKER

### B1 — the gate discards every check-16 note, so the grace and the retirement announcement are both dead on arrival

*Raw ids 6, 15, 25 (three lenses, independently reproduced) · `tools/memory-tree/check-memory-hygiene.sh:1053`*

The only wired caller of `corpus_ids.py --check` is:

```sh
if ! ids=$("$_PY" "$HERE/corpus_ids.py" --check 2>&1); then
  printf '%s\n' "$ids"; status=1
fi
```

Stdout is captured into `$ids` and printed **only on a non-zero exit**. The whole `notes` channel
this unit added is exit-0 by construction: `main()` prints `notes`, then `bad`, then returns
`1 if bad else 0`. So every note is computed, captured, and thrown away.

Reproduced end to end on this tree, twice. Appending `READ_PATH_CEILING="135677"` to
`.memory-tree.conf` makes `python tools/memory-tree/corpus_ids.py --check` print the retired-key
notice at exit 0; `bash tools/memory-tree/check-memory-hygiene.sh` on the same tree prints nothing at
exit 0. Appending an uncapped charter citation makes the module print the grace banner plus the
rule-3 finding at exit 0; the gate again prints nothing.

Three separate promises are false as shipped:

- `.memory-tree.conf.example:59` tells an adopter a retired key is ANNOUNCED on every run. It is not.
  Adopters run the gate, never the module, so the retirement has no notification channel at all and a
  conf still declaring the dead pin is never mentioned to anybody.
- `corpus_ids.py:504` says "THE GRACE ANNOUNCES ITSELF. A rule that is not gating and does not say so
  is indistinguishable from a rule that found nothing." Through the gate, it is exactly that.
- `memory/HYGIENE.md:217` repeats the claim in the rendered doc.

The consequence compounds with H1 below. The grace is invisible for its entire life, and then at
engine 2.44 rules 3 and 4 flip to gating and red with zero prior warning — which is precisely the
skip-that-looks-like-a-pass §7 bans, bought at the price of a release.

No selftest arm reaches it: every check-16 arm goes through the local `_rp()` helper calling
`check_read_path()` directly and asserting on the returned tuple (`corpus_ids.py:883-885` and every
`arm(...)` below it). Nothing exercises the shell wrapper. The callee changed its contract — stdout
became meaningful on exit 0 — and the caller was never told.

**Fix.** Print the capture whenever it is non-empty, independently of the exit code:

```sh
ids=$("$_PY" "$HERE/corpus_ids.py" --check 2>&1); rc=$?
[ -n "$ids" ] && printf '%s\n' "$ids"
[ "$rc" -ne 0 ] && status=1
```

**Left-shift.** An arm in `check-memory-hygiene.test.sh` that declares a retired key in a fixture conf
and asserts the NOTE text appears in **the gate's own stdout on a green run**. That is the arm whose
absence let this ship, and it generalises: the class is "a non-gating channel added to a delegated
checker, with every arm calling the callee directly." Stage the break first — confirm the arm reds
against today's wrapper — then fix the wrapper.

---

## HIGH

### H1 — the grace is unconditional on engine version, so it suspends rules 3 and 4 in trees where they were already gating

*Raw ids 16, 26 · `tools/memory-tree/corpus_ids.py:503`*

`_resolve_sink(root, bad, notes, found)` routes findings to `notes` whenever
`_read_kit_version(root) < READ_PATH_GATES_FROM`. Its signature does not even take `conf`. The
decision is engine version and nothing else.

The stated rationale is narrower than the implementation: these rules "have never run in any tree that
did not declare the retired ceiling, so gating immediately would red an adopter for a pre-existing
condition." That covers trees which never declared the ceiling. The code covers every tree.

**This repo is in the over-covered population.** At BASE, `armed()` read
`any(conf[k] for k in ("DEAD_PATH_PIN", "ORPHAN_ID_PIN", "READ_PATH_CEILING"))` and
`.memory-tree.conf` declared `READ_PATH_CEILING="135677"`, so check 16 ran armed and its rule-3
findings went into `bad` — a hard red on the bar. Verified against the pre-diff blob at `47f9ba6b~1`.
After the diff, the same finding is a note until 2.44, and per B1 the note reaches nobody.

Net effect at HEAD, reproduced: an uncapped charter citation produces `rc=0` and zero printed output.
Coverage that was live on the merge bar at BASE is gone for a release, silently. The unit's premise is
closing a gating gap; this opens one.

**Fix.** The discriminator is already computed in the same function — `written = read_declared_keys(root)`
at `corpus_ids.py:456`. Pass it into `_resolve_sink` and skip the grace for any tree that declared
either retired key: declaring the ceiling is proof rules 3 and 4 were live and green there, so nothing
is pre-existing and gating is honest.

```python
if found and not (written & RETIRED_KEYS) and _read_kit_version(root) < READ_PATH_GATES_FROM:
```

**Left-shift.** Two arms, both sides: a fixture declaring `READ_PATH_CEILING` whose rule-3 finding
**gates**, and one declaring neither whose finding **reports**. A grace with only the reporting side
armed is a grace nobody has watched decline to fire.

### H2 — `--print-kit-version` reads the constant AFTER the project conf is sourced, so a conf line spoofs the engine version and silences the grace flip forever

*Raw id 1 · `tools/memory-tree/check-memory-hygiene.sh:107` (constant at `:13`, source at `:55`)*

`KIT_MEMORY_TREE_VERSION=2.43` is assigned at line 13. `. "$ROOT/.memory-tree.conf"` runs at line 55.
The new `--print-kit-version` arm at line 107 reads the variable after that source. A project conf
that assigns the same name wins.

Reproduced: adding `KIT_MEMORY_TREE_VERSION="0.0"` to a scratch `.memory-tree.conf` made
`check-memory-hygiene.sh --print-kit-version` print `0.0`. Driven through the new code,
`_read_kit_version()` returned `(0,0)` and a rule-4 finding went from `BAD: [...] EXIT 1` to
`NOTES: [...] EXIT 0` on that one line. The other direction works too: `=9.9` returns `(9,9)` and
gates early.

The comment on line 13 says the constant is set there "never from `.memory-tree.conf` (a project conf
must not spoof it)", and `_read_kit_version`'s docstring asserts the same. Three carriers state the
invariant — those two plus `memory/map/features/memory-tree-hygiene.md:37` — and the code does not
hold it, so no reviewer will go looking. Nothing gates it either: `check-kit-versions.sh` and
`check-verdict-epoch.sh` both grep/sed the constant out of the FILE, so they stay correct while the
only runtime reader is spoofable, and check 16's `RETIRED_KEYS` notice covers only the two
`READ_PATH_*` names.

`--print-kit-version` is new in this diff (`47f9ba6b`), so the exposure is new. After the 2.44 bump the
bypass becomes permanent and invisible: one conf line, and rules 3 and 4 never gate in that tree
again. The unit exists to stop a structural check depending on a blankable pin; as landed it depends
on a spoofable conf key instead.

**Fix.** Move the whole `--print-kit-version` case above line 55 — it needs nothing the conf supplies,
and the PRINT MODES block's own comment already promises "these return before check 1". Failing that,
use the capture-before-source idiom this file already runs at line 36 for `SPEC10_CUTOFF`:
`_KIT_VERSION_SHIPPED="$KIT_MEMORY_TREE_VERSION"` right after line 13, printed at 107.

**Left-shift.** An arm with a fixture conf declaring `KIT_MEMORY_TREE_VERSION="0.0"` that asserts
`--print-kit-version` still prints the engine's real version. Better, generalise it: assert that every
`_SHIPPED`-style invariant constant in this file is captured before the source — the class is
"identity constant readable after an adopter-writable source".

### H3 — the NOT-ASKED escape never fires for a freshly scaffolded tree, because the shipped conf example declares `CHARTER="AGENTS.md"`

*Raw id 8 · `tools/memory-tree/corpus_ids.py:467`*

The escape keys on `"CHARTER" not in written`, and its comment claims "A freshly scaffolded tree
declares no CHARTER ... Measured — this is exactly what `adopt-memory-tree.sh --scaffold` produces."
That is false. `tools/memory-tree/.memory-tree.conf.example:48` ships an uncommented
`CHARTER="AGENTS.md"`, and `adopt-memory-tree.sh:48` copies the example verbatim. The scaffolder
writes no `AGENTS.md` — the string does not occur anywhere in the script.

Reproduced end to end: `git init`, two `--scaffold` runs per its own runbook, commit, then
`corpus_ids.py --check` prints `check 16: CHARTER 'AGENTS.md' is declared and is not a tracked file,
so the read path has no source and rules 3 and 4 graded nothing`. So `read_declared_keys` returns
CHARTER, the escape cannot fire, and the FINDING branch is taken.

Today that lands as a grace note at exit 0 — invisible, per B1. At 2.44 it becomes a red, and **every
fresh adopter reds on the day they adopt**, which is the precise outcome the escape hatch was written
to prevent. The adoption hint on failure names only `MEMORY_ROOT`, `DISCIPLINES` and `FAMILIES`, so
nothing tells them to touch CHARTER either.

The selftest at `:964` hand-strips the `CHARTER=` line from its fixture conf before asserting
"not asked" — it certifies a tree state the scaffolder does not produce. Green over a population of
one that does not exist in the field.

**Fix.** Either blank `CHARTER` in `.memory-tree.conf.example` (keep the row as documentation), or
treat a declared-but-untracked charter whose value equals the shipped default as the same not-asked
case. Then rebuild the fixture at `:964` by actually running `adopt-memory-tree.sh --scaffold`.

**Left-shift.** An arm that scaffolds with the real adopter script and asserts a clean check-16 result
— not a hand-edited conf. The class is "a fixture hand-tuned into a state the installer never
produces", and it is worth one arm wherever the kit grades a fresh tree.

### H4 — `READ_PATH_GATES_FROM = (2, 44)` collides with a live concurrent branch already shipping 2.43, so the grace ends by merge order

*Raw id 9 · `tools/memory-tree/corpus_ids.py:63`*

`main` is still at `KIT_MEMORY_TREE_VERSION=2.41`. The merge-base of this branch and
`origin/branch/build-readme-governance-e1c044` is `60ba1d60` at 2.40. Both branches then independently
minted 2.42 and 2.43: here `8d5b8be0` then `03682a88`; there `00abe19e` then `3fc5fc3f`/`a2832066`.
`git merge-base --is-ancestor` puts none of them on `main`. Two materially different engines currently
answer `2.43` to `--print-kit-version`.

The mechanism is worse than a naming clash. Because both sides carry the identical literal `2.43`,
the second merge will **not conflict on that line** — git auto-resolves it — so the collision stays
silent until `check-verdict-epoch` fires on an engine whose content moved without a version bump,
forcing 2.44. That is exactly `READ_PATH_GATES_FROM`.

So the grace ends because of merge ORDER, not because anyone judged the corpus clean. The comment two
lines above the constant warns against precisely this: "Bumping the engine WITHOUT moving this would
end the grace silently." Combined with H3, that flip immediately reds every freshly scaffolded
adopter, and combined with B1 nobody saw a warning first.

**Fix.** Pin the flip clear of the in-flight collision (2.46, say), or key the grace on something a
version bump cannot move — a dated cutoff in the `SPEC10_CUTOFF` / `REVIEW_VERDICT_CUTOFF` style this
kit already uses, or an explicit boolean the owner flips deliberately.

**Left-shift.** A gate leg that reds if `KIT_MEMORY_TREE_VERSION` reaches `READ_PATH_GATES_FROM` while
this repo's own rules 3 and 4 still report findings. That converts "the grace ended and nobody
noticed" into a red at the moment of the bump, which is the only moment anyone can act on it.

---

## MEDIUM

### M1 — `--print-index-set` runs below checks 1-5, so their failure text pollutes `capped` and rule 3 falsely passes

*Raw id 3 · `tools/memory-tree/corpus_ids.py:483`, `tools/memory-tree/check-memory-hygiene.sh:435`*

`capped` is built from the raw stdout of `--print-index-set`. That arm sits at line 435, **below**
checks 1-5 (lines 217-400), unlike the two arms at 106-107 which really do return before check 1.
`fail()` writes to stdout, and check 3's body is bare `memory/<name>` paths at column 0. The print
mode hardcodes `exit 0` and `ask_shell` only rejects a non-zero exit, so that text is folded into
`capped` verbatim.

Reproduced: a fixture with a stray tracked `memory/NOTES.md` and a charter citing it returned
`HYGIENE check 3 FAILED — unexpected entries (structure):` followed by four bare paths, at exit 0.
`"memory/NOTES.md" in capped` was `True` and `check_read_path` returned `([], [])` — rule 3 silent on
the exact member it exists to catch.

The collision is structural, not incidental: check 3's population **is** unexpected entries under
`memory/`, the same class rule 3 targets. The bug pre-dates the diff (same line at 452 in the
merge-base), but the diff widens it materially — pre-diff, `main()` returned before `checks()` when
`armed(conf)` was False, so this path ran only on a pinned tree; now `check_read_path` runs on every
tree. It also falsifies the comment at line 104. The outer run is already red from check 3, which
bounds the impact, but check 16 reports a false clean on that run.

**Fix.** Hoist `INDEX_SET`'s computation and its `case` arm into the PRINT MODES block near line 105,
beside the other two, so that block's comment is true of all three.

**Left-shift.** Make `ask_shell` raise a `Problem` when stdout carries a line matching `^HYGIENE `, so
a polluted set is a named refusal rather than a silently widened `capped`. That is the liveness
assertion §7 asks for — a probe that cannot answer says so instead of returning a reassuring set.

### M2 — `read_declared_keys` is defined twice, byte-identically; the first 18 lines are dead, and the map recorded the duplicate as fact

*Raw ids 4, 13, 17, 27 (four lenses) · `tools/memory-tree/corpus_ids.py:107` and `:125`*

Both definitions are byte-identical including the docstring; Python binds the name to the second, so
the first is unreachable. Introduced by this build — `git show b788026a -- tools/memory-tree/corpus_ids.py`
shows two `+def read_declared_keys` in one commit, and `git show 70df24ea:...` has none. A half-applied
edit.

Behaviour is unchanged today, which is what makes it worth filing: this function is the sole arbiter
of which conf keys count as DECLARED. It decides whether a retired key is announced and whether an
undeclared CHARTER means "not asked". A later parsing correction — inline comments, `export KEY=`,
quoted keys, shell-vs-python skew against the sourced conf — applied to the copy a reader finds by
scrolling down from `load_conf` is silently a no-op, and every test keeps passing against the other
binding. It is also the function H1's fix needs to reach.

`memory/map/generated/symbols.json` gained two identical `{"id": "read_declared_keys", "file":
"tools/memory-tree/corpus_ids.py"}` entries in this diff and nothing reds, so the map's symbol tier
now carries a duplicate key as fact. The 19-line shift is also what forced the third re-pin of
`tools/install-prefix-waivers.txt` in this build.

Nothing could have caught it: `tools/gate-legs.json` has no Python lint leg, so ruff/flake8 F811 never
runs, and `check-arms.py`'s population is `*.sh` only.

**Fix.** Delete lines 107-123, keeping the definition at 125. Regenerate `symbols.json` in the same
commit and re-pin the two `corpus_ids.py` rows in `install-prefix-waivers.txt` (836/840 to 817/821).

**Left-shift.** Two candidates, both cheap. A map-side assertion that no `(file, id)` pair appears
twice in `symbols.json` — the generator had the evidence and said nothing. And an `ast`-based
duplicate-definition check over the kit's Python files, which is a few lines and does not need a whole
lint leg.

### M3 — four carriers still tell adopters that blank pins turn check 16 off

*Raw ids 5, 18, 19, 30 (four lenses) · `tools/memory-tree/kit.toml:98` · `tools/memory-tree/README.md:21`
· `tools/memory-tree/check-memory-hygiene.sh:1051` · `tools/memory-tree/corpus_ids.py:22` ·
`tools/memory-tree/.memory-tree.conf.example:50-52`*

Check 16 is now structural — `main()` calls `check_read_path` unconditionally, outside `armed()`, and
its own docstring says "STRUCTURAL: it runs whenever the conf is loadable. Behind no pin,
deliberately." Five carriers say the opposite:

- `kit.toml:98` — "Blank means checks 13-16 are simply OFF, so the hygiene leg exits 0 with the hole
  wide open."
- `README.md:21` — "blank pins turn the unit off", for a unit it introduces as checks 13-16.
- `check-memory-hygiene.sh:1051` — "blank pins turn the whole unit off."
- `corpus_ids.py:22` — "with every pin blank the grammar module is never imported and checks 13-16 are
  simply off." This is the first thing a reader of the engine sees, seven lines above the check-16
  summary line the diff DID update, and it contradicts `armed()`'s new docstring thirty lines below.
- `.memory-tree.conf.example:50-52` — "(checks 13-16) ... Blank turns its check off", directly above a
  retirement comment that correctly says rules 3 and 4 are behind no pin.

The `kit.toml` one is the worst placed. It is a deployer descriptor, `govkit.py:2508-2509` writes
`h.get('why')` verbatim into the adopting repo's `.governance/outbox/`, and the `discharge` line
directly beneath it WAS updated by this same commit to drop `READ_PATH_CEILING`. The file now
contradicts itself twice within twenty lines, in the surface an adopter reads before adopting.

An adopter who blanks the pins on that promise starts getting red at exactly 2.44.

**Fix.** All five to the split the code implements: checks 13-15 behind `DEAD_PATH_PIN` /
`ORPHAN_ID_PIN`, check 16 structural and behind no pin. `HYGIENE.md` and `HYGIENE.template.md` were
already corrected in this diff — copy their wording so the carriers agree.

**Left-shift.** This is the "one fact in one place" rule losing to five hand-typed copies. The
durable fix is derivation: have the engine print its own armed/structural split (it already prints its
index set and, now, its version), and have the carriers cite the derivation. Short of that, a parity
check comparing each carrier's claimed check range against `armed()`'s actual tuple.

### M4 — nine carriers say the retirement shipped in "memory-tree 2.42"; the shipping engine is 2.43

*Raw ids 10, 23 · `tools/memory-tree/.memory-tree.conf.example:59` and eight more*

`KIT_MEMORY_TREE_VERSION=2.43`, and every rendered `gov:kit memory-tree@` marker in the diff says 2.43
(7 occurrences against 7 removed 2.41s). 2.42 existed only as intermediate commit `8d5b8be0` on this
branch, superseded by `03682a88` before anything landed; `main` is 2.41. No adopter will ever hold a
2.42 engine carrying this retirement.

Nine non-spec carriers: `.memory-tree.conf:143`, `memory/HYGIENE.md:151` and `:208`,
`tools/memory-tree/HYGIENE.template.md:151` and `:208`, `tools/memory-tree/kit.toml:8`,
`tools/memory-tree/check-memory-hygiene.test.sh:1410`, `tools/memory-recall/extract.py:242`,
`tools/memory-tree/.memory-tree.conf.example:59`.

The tree already contradicts itself: `memory/builds/dSpentCeiling/build/2026-08-25-build-TOOL-dSpentCeiling-1-1.md:17`
states the shipping release is 2.43 and the grace ends at 2.44. The conf example is the one that ships,
telling adopters an engine they can install already dropped the keys, when it did not.

**Fix.** `s/memory-tree 2.42/memory-tree 2.43/` across the nine, `kit.toml:8`'s "structural since
memory-tree 2.42" included.

**Left-shift.** The pair moved once mid-build already, so retyping it a tenth time is the wrong
answer. A parity check comparing prose version claims (`memory-tree \d+\.\d+`) against
`KIT_MEMORY_TREE_VERSION` would red on the next mid-build bump instead of shipping it.

### M5 — the kickoff manifest front-loads a deleted pin, in future tense

*Raw ids 11, 20 · `memory/guides/SESSION-KICKOFF.md:100-103`*

The bullet reads: "The read path is NOT full, and the ceiling measuring it is being retired. The pin
went 135677 -> 161120 on 2026-08-25, leaving 25600 B — four days at the measured 6184 B/day ...
`TOOL-dSpentCeiling` deletes it ... Prune then."

Every clause is stale within its own diff. `git show HEAD:.memory-tree.conf` has no
`READ_PATH_CEILING` assignment — only the retirement comment at `:142` — so the pin never reaches
161120 at this branch's HEAD, and `memory/ledger/2026-08.md:60` marks dSpentCeiling CLOSED while this
bullet describes it as in flight.

This is the one document every session front-loads before touching code, and its `watch:` list at
`SESSION-KICKOFF.md:6` names `.memory-tree.conf` — the exact file this commit stripped of that pin. A
session reading it will hunt for a ceiling that does not exist, or re-add one, and will act on advice
about an instrument that is gone. §1's DoD requires re-stamping `last-audit` when a unit changes what
the manifest front-loads; this unit changed it and left the old text.

**Fix.** Rewrite in past tense to the closed-state fact: the byte budget is retired by
TOOL-dSpentCeiling-1, check 6's per-class caps (61440 B for a guide) are the only bound, and check 16
grades charter citations structurally, reporting rather than gating until the version in
`READ_PATH_GATES_FROM`. Re-stamp `last-audit` with the delta line.

Note on a claim the skeptic trimmed: 161120 does appear elsewhere in the tree (the build record, the
ceiling-history exhibit, the spec, the selftest fixtures) — the accurate charge is that it never
reaches the live conf. And the neighbouring gotcha at `:312` reads as past-tense history, so it is
weaker than filed; mark it historical if you are in there anyway, but it is not the defect.

**Left-shift.** The manifest ratchet already exists. What it does not do is notice that a `watch:`
file lost a key the manifest's prose names. A check that greps every conf key cited in
`SESSION-KICKOFF.md` against the confs on its own `watch:` list would have redded this commit.

### M6 — `_parse_conf_int`'s named-refusal branch lost all three of its arms and gained none

*Raw id 29 · `tools/memory-tree/corpus_ids.py:165`*

At BASE the selftest carried three arms hitting `must be a whole number of at least ...` — malformed
headroom, zero headroom, malformed ceiling, at lines 764-773. The diff deleted all three with the
retired keys and replaced none. `grep -n "whole number"` over the selftest now returns nothing.

Reproduced by instrumenting: wrapping `_parse_conf_int` and running `cmd_selftest()` at HEAD gives 38
calls, all with raw values `"0"`, `"1"` or `"2"`, and **0** hits on the raise at `:165-167`.

The branch is still live in production — both surviving call sites (`:561` ORPHAN_ID_PIN, `:594`
DEAD_PATH_PIN) parse an adopter-written conf value, so `ORPHAN_ID_PIN="abc"` reaches it — and the
module docstring explicitly promises a named refusal rather than a traceback out of a gate. That
promise is now asserted by nothing. Nothing else covers it either: the selftest's line tracer gates on
`frame.f_code is walk.__code__` so it never enters this function, `check-arms.py` filters to `*.sh`
and cannot see a Python raise, and the two consumers in `check-memory-hygiene.test.sh` both write
well-formed pins.

**Fix.** Two arms: `ORPHAN_ID_PIN="not a number"` asserting the named refusal, and the unicode-digit
case the comment names (`"²"`) asserting the same — that is the escape the ASCII-only regex exists to
close, so it is the arm worth having.

**Left-shift.** This is coverage lost as collateral when its subject was retired, which is a class
rather than an instance: deleting a key should not silently delete the arms for the shared accessor it
used. Worth an explicit item on the retirement checklist — when a pin goes, re-home its accessor arms
rather than deleting them with it.

---

## LOW

### L1 — `_parse_conf_int`'s docstring still describes the parameter this commit deleted

*Raw id 14 · `tools/memory-tree/corpus_ids.py:147, :150`*

The signature is now `_parse_conf_int(conf, key, default=None)` — `*, minimum: int = 0` was deleted and
the raise hardcoded to "at least 0" — but the surviving first paragraph still says "anything else that
is not a decimal integer at or above `minimum` is a named failure", and still ends "One accessor, four
keys" when two call sites remain (the other two keys are the retired pair). The paragraph immediately
below correctly explains the removal, so the docstring contradicts itself within eight lines and a
reader cannot tell which half is current.

**Fix.** Drop the `minimum` reference, state the floor as a flat 0, and either name the two surviving
callers or drop the count rather than restate a derived figure.

**Left-shift.** Nothing gates prose against a signature. The honest answer is the general one already
open as TOOL-dSpentCeiling-5: stop writing counts of derived populations beside the population.

### L2 — `read_set` still carries the "check 12's finding, not ours" misattribution the diff removed everywhere else

*Raw ids 22, 31 · `tools/memory-tree/corpus_ids.py:416`*

The line producing the `absent` set still reads `# tracked but missing: check 12's finding, not ours`.
Seventy-four lines below, the diff's new comment at `:490-493` says this is "NOT a duplicate of check
12, whatever this line used to claim ... the comment that said otherwise was an invitation to delete
it", and a new selftest arm at `:933-934` asserts the emitted message no longer names check 12.

The arm greps the emitted MESSAGE only, so the source comment that seeded the false belief is outside
its population and survives untouched — on the line that generates the very set rule 4 consumes, which
is the copy a reader hits first when tracing where `absent` comes from. One fact, two contradictory
answers, one file. (The line is pre-existing; the diff created the contradiction by correcting one of
the two copies.)

**Fix.** Rewrite it to match: tracked-but-absent is check 16 rule 4's finding, and it is the ONLY
detector for a charter-cited guide, because check 12's arm covers `builds/*/spec/*.md` and
`index_set()` drops absent files before check 6 measures.

**Left-shift.** When an arm is written against a corrected MESSAGE, grep the file for the old claim
before landing. Cheap habit, and it is the same "gate the class, not the instance" rule §7 states.

### L3 — the map dossier's reuse seam cites the wrong line and ends in a fragment that does not parse

*Raw ids 12, 21 · `memory/map/features/memory-tree-hygiene.md:110`*

Two defects in one three-line replacement, both introduced here. The citation is wrong:
`check-memory-hygiene.sh:56` is `: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"`, while `:79` is an unrelated
prose comment about the converged cap scheme. A reader following the dossier to `:79` lands on the cap
block and cannot find the one seam the section tells them to copy. (The `:36` half is correct.)

And the paragraph ends mid-sentence — "...restores it with `: "${SPEC10_CUTOFF:=$_SPEC10_SHIPPED}"`
after. There is / the same channel." — the tail of a deleted sentence left attached to the new text.

Worth noting the irony: H2 above is a defect that this exact seam, correctly applied, would have
prevented.

**Fix.** `:79` to `:56`, and delete the orphaned "There is / the same channel." fragment.

**Left-shift.** These pins are line-numbered and brittle, which is already filed as
TOOL-dSpentCeiling-6. Until that lands, anchor dossier seams on the variable name rather than the
line — a name survives an edit above it, a number does not.

### L4 — the codebase-map `guides` extractor still justifies itself by the deleted budget

*Raw id 24 · `tools/codebase-map/map_extractors.py:118`*

The comment reads "Charter-cited binding documents — each one spends from the read-path budget
(hygiene 16)". That is the stated reason `memory/guides/*.md` is a machine-enumerated inventory key at
all, and its premise is now void: check 16 sums nothing. A later reader auditing whether the extractor
still earns its keys reads a rationale that no longer holds and cannot tell whether it should stay.
It should — rule 3 grades exactly this population, which is a better argument than the one written
there. A cross-kit carrier the retirement sweep missed because it lives outside `tools/memory-tree/`.

**Fix.** "Charter-cited binding documents — hygiene check 16 rule 3 requires every one of them to be
byte-capped by check 6 or waived."

**Left-shift.** The sweep for this retirement was scoped to the owning kit. When a kit retires a
concept, grep the whole tree for the concept's NAME, not the kit's directory — `READ_PATH` and
"read-path budget" both, since a carrier that names it in prose is invisible to a symbol grep.

---

## Coverage of the hunt list

The brief named seven specific hazards. Where each landed:

| Hunted for | Result |
|---|---|
| Silent coverage loss in the restructure | **Found** — H1 (grace over-covers armed trees), M6 (`_parse_conf_int` arms deleted), and B1 (the notes channel is unreachable). Three distinct losses. |
| An adopter state that reds on upgrade | **Found** — H3. A freshly scaffolded tree takes the finding branch and reds at 2.44 on adoption day. |
| The grace defeatable or ending unintentionally | **Found, both** — H2 defeats it permanently with one conf line; H4 ends it by merge order rather than judgement. |
| `check_read_path` reaching `walk()`/`grammar()` | **Clean.** Traced: it calls `read_set` with a minimal dict, `ask_shell`, `read_declared_keys` and `_read_kit_version`. No path to `walk()` or `grammar()`, and the conditional memory-recall dependency holds. |
| The `(bad, notes)` split leaking either way | **Found in one direction** — H1. Findings that should gate go to `notes`. No leak the other way: `_resolve_sink` is the single decision point, which is the right shape and is why the fix is one predicate. |
| `read_declared_keys` disagreeing with `load_conf` | **Not found as a behavioural disagreement**, but see M2 — the function is defined twice, so the question has two answers waiting to diverge. |
| Anything false in the ~15 updated carriers | **Found, extensively** — M3 (five carriers), M4 (nine carriers), M5, L1, L2, L4. Carrier staleness is this diff's dominant defect class by count. |

## What was refuted

Three raw findings did not survive the skeptic and are recorded here as absent from the numbered list
above. They were dropped for want of reachability or impact, not for want of interest, and should not
be re-hunted in round 2.

Two further claims were trimmed rather than dropped, and the trims are noted inline: M5's "161120
appears nowhere in the tree" (it appears in records, just not in the live conf) and its companion
claim about the `:312` gotcha, which reads as history rather than as a live mechanism.

## Landing advice

B1 and H1 are one merge decision. Fixing either alone leaves a real defect — fix B1 only, and the grace
speaks while still over-covering armed trees; fix H1 only, and this repo gates again while every note
and every adopter's grace banner stays silent. Land them together, each with the arm named above
observed RED first.

H2 is a one-line move and should ride the same commit: it is the cheapest fix in this review and the
most permanent bug in it.

H3 and H4 are both about what happens at 2.44 and neither is urgent this week, but both must be
resolved before the bump — and H4 in particular wants a decision now, because the colliding branch is
live and the second merge will not conflict on the line that matters.

The mediums and lows are a documentation sweep plus one dead-code deletion. M2 should land with the
regenerated `symbols.json` and the re-pinned waivers in the same commit, per §1.
