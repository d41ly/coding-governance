# review-dClosedLexicon-7 — M8 closing review of the second run

## Verdict: BLOCKED — 2 blockers, 2 high

**Subject:** the three commits on top of `cb933ef`, and ONLY these three · streams `playbook`+`tooling` · node d · 2026-08-16

| commit | unit |
|---|---|
| `ed542e5` | PLAY-dClosedLexicon-1 — the §0 fallback rule, the §14 refutation, the lockstep bump to v2.10 |
| `be0ee6a` | TOOL-dClosedLexicon-2 — the verb table wired into the map ratchet and the drift signal set |
| `b95c231` | TOOL-dClosedLexicon-3 — the run-state unit list DERIVED instead of copied |

**Explicitly OUT of scope:** the lexicon kit itself (`cb933ef` and everything under it), which six prior
review rounds covered. No finding below re-raises a folded one.

## Review shape

| | |
|---|---|
| raw findings | 29 |
| confirmed (survived an adversarial skeptic) | 21 |
| refuted | 8 |
| unverified / outstanding | 0 |
| precision | 0.72 |

The 21 confirmed findings collapse to **12 distinct defects** — 2 blockers, 2 high, 2 medium, 6 low.
Convergence is heavy on the two blockers and is itself signal: **four independent verifiers**
reproduced the unguarded optional-kit import (ids 1, 10, 17, 26) and **four** reproduced the `-S`
pickaxe (ids 2, 8, 18, 25). Duplicates are recorded under each defect rather than repeated as rows.

**Every finding below was re-measured by me during write-up**, in this worktree, against the shipped
engines — not carried on the verifiers' word. Two blockers I reproduced end-to-end with fresh
fixtures; the reproductions are pasted inline. One defect (**M2**) is MINE, not a verifier's: it came
out of the owner's third question and no verifier raised it.

**Priming lenses** (the six classes the gotcha checklist selected by anchor for this diff):
`armed-but-unreachable-rule` · `assertion-between-two-derived-values` ·
`inputs-inside-the-subjects-reach` · `pin-copied-from-another-corpus` ·
`second-implementation-is-not-a-second-opinion` · `trailing-comma-counted-as-an-element`.
Four of the six earned a finding. **B2 is `armed-but-unreachable-rule` landing in the same build whose
own dossier claims that class** — the sharpest result in this review. `pin-copied-from-another-corpus`
and `trailing-comma-counted-as-an-element` produced nothing: the three lexicon pins are measured
against this corpus and honestly non-zero, and the `SIGNALS` list at `drift_report.py:666` is a real
8-element list with no phantom trailing member (I counted it against `--json` output: 8 in, 8 out).

**The headline.** All three units do what their specs say. But the drift-audit half of unit 2 shipped
**two signals that are worse than not shipping them**: one crashes the whole report — including a gate
leg — for adopter populations this repo explicitly keeps working, and the other is a gateable,
pinned-at-0 probe that **can never fire**, declaring `live: True` so the kit's own DEAD-PROBE
machinery cannot catch it. It shipped green through a 63/63 bar because its one falsifiability arm is
a false positive. The unattended unit (3) is the strongest of the three and its inversion is sound,
but it left a DoD item that now passes on a malformed file, a dead `splice()` a bar leg still drives,
and a header that still asserts the retired contract.

---

## Answers to the four questions asked

### (1) Does the drift-audit engine change break an adopter who has codebase-map or drift-audit but NOT the lexicon?

**An adopter with NEITHER conf nor kit: no, correctly** — `--check` returns 0 and both signals are
non-gateable. I verified this on a clean fixture.

**An adopter who has a `.lexicon.conf` but not the kit at `tools/lexicon`: YES, catastrophically.**
That is **B1**. The guard is written on the CONF; the dependency is the KIT DIR. Three reachable
populations hit it: the root-prefix adopter (`<root>/drift-audit/`, `<root>/lexicon/` — the dual
spelling `tools/install-prefix-waivers.txt` exists to keep working, and the shape drift-audit's OWN
`make_repo` fixture builds), the mid-teardown state, and any malformed conf (`ConfError` is unguarded
on the same path).

**And it is not confined to drift-audit.** `tools/codebase-map/map_extractors.py:155` repeats the
identical shape — conf-gated, then a hardcoded `ROOT / "tools" / "lexicon"` with an unguarded
`from lexicon_conf import load_conf`. A codebase-map adopter at the root prefix WITH a `.lexicon.conf`
takes a `ModuleNotFoundError` out of `all_inventories()`. No verifier flagged this second copy; I
found it reading the diff. Fix both or the fix is half a fix.

### (2) Can either new signal report a reassuring zero when it should say not-asked, or vice versa?

**Both, in the output humans actually read.** That is **H2**. `_build_not_asked` computes
`gateable: False` and a reason note, and the human renderer consults neither — it branches on `live`
first, so both signals print the kit's reserved alarm string. Measured on a no-conf fixture:

```
lexicon_verbs_declared_but_unused                      0      0  DEAD PROBE — signal cannot move, ignore its value
lexicon_ratified_older_than_language_surface           0      0  DEAD PROBE — signal cannot move, ignore its value
```

`AGENTS.md:129` — added in this same diff — claims "with no `.lexicon.conf` both report NOT ASKED
rather than a clean zero". That is true in `--json` and `--check` and **false in the default output**.
Every drift-audit adopter who never took the lexicon inherits two permanent false DEAD PROBEs, which
devalues the one alarm string this kit exists to make meaningful.

The reverse direction is worse: **B2**. `lexicon_ratified_older_than_language_surface` reports a
reassuring, gateable, permanent **0** for the one edit its docstring names, and declares `live: True`
so nothing can call it dead.

### (3) Is the emptiness invariant equivalent to what byte-equality bought?

**For an OPEN run, yes — and the inversion is right.** Byte-equality was unmaintainable in the
ordinary case (a spec rev bump moved the index; the region's only writer refused once a run was live;
the remedy string named a path no verb walks). One fact, one home is the correct call, and check 8's
rewrite states the new invariant honestly.

**For a FINISHED run record, no — something was lost, and it was not replaced.** This is **M2**, and
it is the answer to the "what can a reader of a finished run record still reconstruct" half of the
question. Under byte-equality, a LANDED `RUN.md` was a self-contained frozen record: the roster it
carried was provably the roster at close, and the check proved it had not been hand-forged. Under
emptiness, the roster is a **live query against a mutable document**. `memory/builds/aSiftedPlaybook/RUN.md`
is `phase: LANDED` and now records witness, keepalive, anchor triple, base — and **nothing about which
seven units the run covered**. Re-open a spec in that build, or add a unit to it next month, and the
landed record's derived answer changes retroactively. It happens to be correct today for both
migrated files (I diffed the derived slice against the deleted copy for `aSealedCaravan` — identical),
which is exactly why nothing reds.

### (4) Are the migrated run-state files still honest records?

**Honest about every fact they assert; no longer complete about the one they dropped.** Nothing in
the migration is a false statement — the banner change is accurate, the run facts are untouched, and
the two frozen copies I compared against today's README slice still agree. But `aSealedCaravan` is
`INPROGRESS`, so its README slice is expected to move, and `aSiftedPlaybook` is LANDED with no pinned
scope. The migration is correct as executed; the design gap is M2 and it is not the migration's
fault. Recommendation is in M2: pin the roster into the immutable `## Run facts` block at `--landed`,
where the driver already writes an immutable record.

---

## BLOCKERS

### B1 — an optional kit at an unexpected prefix takes down every signal and the gate leg

`tools/drift-audit/drift_report.py:569` and `:602` · also `tools/codebase-map/map_extractors.py:155`
*(ids 1, 10, 17, 26 — four independent reproductions)*

`_resolve_lexicon_conf` (`:558`) keys on `.lexicon.conf` existing. The code then imports the reader
from a **hardcoded** `ctx.root / "tools" / "lexicon"` and calls `load_conf` unprotected. Conf-present
and kit-importable-at-that-exact-path are different facts, so the guard does not guard the dependency.
`main()` at `:763` runs `out = [s(ctx) for s in SIGNALS]` with no per-signal guard and catches only
`DriftError`.

**Reproduced by me**, using the kit's own `selftest.make_repo` (which installs drift-audit at the ROOT
prefix, `<root>/drift-audit/`) plus a valid `.lexicon.conf` and no `tools/lexicon/`:

```
A conf-present kit-absent  RC: 1 | stdout bytes: 0
   err tail: ModuleNotFoundError: No module named 'lexicon'
```

RC 1, **zero stdout**, a traceback — all six pre-existing signals lost, and
`python tools/drift-audit/drift_report.py --check` (a bar leg) reds with no diagnostic. This directly
falsifies the docstring at `:559-561`: *"an adopter without the lexicon gets `gateable: False`, never a
raise and never a red."*

It is also the one place a shipped engine spells another kit's install prefix, against the charter rule
that every engine derives its own. The correct derivation is already used in `selftest.py:601`
(`__file__.resolve().parent.parent / "lexicon"`) and was not carried into the engine — and
`selftest.py:602` copies the kit to `r / "tools" / "lexicon"` while drift-audit itself sits at the root,
i.e. **the fixture was shaped around the hardcode**, which is why no leg sees it.

Reachability, three ways: (a) root-prefix adopters — `adopt-lexicon.sh` derives `KIT_DIR` from
`BASH_SOURCE` and installs anywhere; (b) mid-teardown — `tools/lexicon/README.md`'s new uninstall order
never mentions deleting the kit directory at all, and the new `--check` orphan arm only detects
conf-gone-extractor-remains, not the reverse; (c) a malformed conf, where `ConfError` propagates
identically.

**Fix.** Resolve the sibling from this engine's own location —
`pathlib.Path(__file__).resolve().parent.parent / "lexicon"`, falling back to `ctx.root/"tools"/"lexicon"`
— and wrap the import **and** the parse:

```python
try:
    from lexicon_conf import load_conf
    import lexicon as lex
except Exception:
    return _build_not_asked(name, f"a .lexicon.conf is present but the lexicon kit is not importable at {kit}")
```

Apply the same two changes to `map_extractors.py::_read_lexicon_verbs`, returning `[]` on failure as
its own docstring already promises for the absent-conf case.

**Left-shift gate.** Add a selftest arm that installs the lexicon at a **non-`tools/`** prefix (and a
second with the conf but no kit at all) and asserts `--check` returns 0 with both signals NOT ASKED.
Stronger and cheap: add a `drift_report.py` arm asserting that `--json` **never** exits non-zero for
any fixture state — the module docstring already claims this, so the arm is just making an existing
promise falsifiable. Consider a repo-wide predicate in `check-install-prefix.sh`'s family: no shipped
engine may spell `"tools" / "<another-kit>"` as a literal path segment.

### B2 — `signal_lexicon_ratified_stale` is a gateable probe that can never fire

`tools/drift-audit/drift_report.py:655` *(ids 2, 8, 18, 25 — four independent reproductions)*

```python
langs_at = ctx.git.run("log", "-1", "--format=%cI", "-S", "LANGS=", "--", ".lexicon.conf").stdout.strip()
```

`-S` is a pickaxe on the **occurrence count** of the literal. Widening `LANGS="py:python-ast:parser"`
to `LANGS="py:python-ast:parser js:js-regex:probe"` leaves the count of `LANGS=` at exactly 1, so that
commit is invisible and `log -1` falls back to the commit that **introduced** the declaration.

**Reproduced by me** in a scratch repo, commit 1 `add` / commit 2 `widen`:

```
--- -S ---   51d74f1 add
--- -G ---   4748922 widen
             51d74f1 add
```

`-G` sees it; `-S` does not. On this repo the effect is already live:
`git log -S "LANGS=" -- .lexicon.conf` returns exactly `b062615` even though `be0ee6a` and `d54f0ca`
both touched the file, and it always will.

So `langs_at` is frozen at the adoption commit forever, and the signal degenerates to "was
`.lexicon.conf` created after the `ratified` stamp". Today `langs_at[:10] == stamp == "2026-08-16"`,
so the reported 0 is produced by **equality**, not by judgement. The signal is `gateable: True` and
pinned at 0, and `"live": True` at `:660` is a **hardcoded literal** — so the DEAD-PROBE machinery in
`--check`, the exact mechanism this kit's charter makes load-bearing, cannot catch it either.

This is `armed-but-unreachable-rule`, shipped in the build whose dossier claims that gotcha class, in
the kit whose module docstring says it exists to refuse precisely this.

**Fix.** Two changes, both required:

1. `-S "LANGS="` → `-G "^LANGS="` (verified above: `-G` returns the widening commit).
2. Derive `live` instead of asserting it. `live` must be False — or the signal NOT ASKED — when the
   resolved commit is the one that first added the conf, because in that state nothing has moved since
   ratification that could have been checked. A hardcoded `True` on a signal is the shape that defeats
   the kit's own liveness contract; it deserves its own predicate (see the left-shift below).

**Left-shift gate.** Two, and take both. (i) In `selftest.py`, replace the arm at `:642` per **H1**,
adding the missing negative control. (ii) Add a structural arm over `drift_report.py` itself: no signal
may return a **literal** `"live": True` — every signal's liveness must be an expression over something
it measured. Grep-able, one line, and it would have red-flagged this signal at authoring time. Six of
the eight existing signals already derive it (`checked > 0`, `bool(used)`), so the pin is 1 and
shrink-only.

---

## HIGH

### H1 — the one falsifiability arm for B2 is a false positive

`tools/drift-audit/selftest.py:632-643` *(ids 3, 9, 19)*

The arm named *"a language surface widened after ratification fires the staleness signal"* does two
things in one commit: it rolls `ratified` back `2999-01-01` → `1999-01-01` **and** widens `LANGS`, then
commits both together and asserts `stale["value"] == 1`.

Because `-S` cannot match that commit (B2), `langs_at` resolves to the earlier `adopt the lexicon`
commit — dated today in the fixture — and the comparison is `"2026-08-16" > "1999-01-01"`, true off the
**stamp rollback alone**. Delete the `LANGS` widening entirely and the arm still passes. It never reads
`detail[0]["langs_changed"]`, which is the only value under test.

This is `assertion-between-two-derived-values` with both inputs moved at once, and it is the direct
answer to *how did B2 ship through a 63/63 bar*: the kit's own proof that the signal can move is
itself the bug.

**Fix.** Split into two commits with controlled dates and add the missing control:

1. Re-ratify at a date **on or after** the adopt commit; assert the signal reads **0**.
2. Widen `LANGS` in its **own** commit, stamp untouched; assert it reads **1** *and* that
   `detail[0]["langs_changed"]` equals that commit's `%cI[:10]`.
3. Negative control: move only `ratified` backwards, `LANGS` untouched; assert **0**.

Control (3) fails under the current implementation, which is what makes it a real arm. The stamp must
never move in the same commit as the surface, or the arm cannot tell its two inputs apart.

**Left-shift gate.** Every drift signal's firing arm must move **exactly one** input from the green
state. Worth writing into `memory/gotchas/` as the enforceable form of
`assertion-between-two-derived-values` for this kit, and worth a `selftest.py` convention that a firing
arm asserts a value **out of `detail`**, not just the scalar.

### H2 — NOT ASKED renders as DEAD PROBE, and the charter states the opposite

`tools/drift-audit/drift_report.py:581` (the producer) and `:774` (the renderer) · `AGENTS.md:129`
*(ids 4, 20)*

`_build_not_asked` returns `live: False`, and the human render loop tests `if not s["live"]` **first**,
falling through to the DEAD PROBE string for anything not in `DECLARED_EMPTY` (which holds only
`ledger_rows_contradicting_git`). `gateable` and the reason note are computed, passed, and never read
on that path. The reason is suppressed behind *"rerun with --json"*.

`DECLARED_EMPTY` is not the workaround: it is project-owned, and a shipped template cannot pre-declare
an optional kit's signals — nor should it, since these are `gateable: False`.

The function's own docstring says *"NOT ASKED is neither clean nor dead"*, and the kit's own
`DECLARED_EMPTY` arms (`selftest.py:700-706`) treat the **printed row** as the discriminating assertion
and explicitly demand NOT DEAD PROBE. The kit's own standard is not met for these two signals.

`--check` is correctly unaffected (rc 0 verified), which is exactly why nothing on the bar catches it.

**Fix.** Add an explicit `"asked": False` key in `_build_not_asked` and a renderer branch **above** the
`live` test:

```python
if not s.get("asked", True):
    status = f"not asked — {s['detail'][0]['note']}"
```

Then correct `AGENTS.md:129` — or leave it, once the code makes it true.

**Left-shift gate.** Extend the `DECLARED_EMPTY` arms' pattern to a third state: a fixture with no
`.lexicon.conf` asserting both rows print `not asked` and **NOT** `DEAD PROBE`. The arm shape already
exists at `selftest.py:700-706`; this is one more case row in it.

---

## MEDIUM

### M1 — `records-current` discards `region`'s exit status, so malformed markers satisfy the DoD item

`tools/unattended/unattended.sh:985` *(id 12)*

```bash
[ -z "$(region "$rel" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null | tr -d '[:space:]')" ] \
  && region "$(readme_of "$slug")" "$SRC_OPEN" "$SRC_CLOSE" >/dev/null 2>&1 ;;
```

Command substitution keeps stdout and **discards exit 3**. `region`'s awk prints nothing when the open
marker is absent or transposed (`inside` is never set), so an absent or malformed generated-marker pair
yields empty output and **satisfies** the machine-checked DoD item declared in `DOD_CORE` at line 78.

Under the retired byte-equality design this state failed (empty vs the non-empty README slice). It now
passes, so `--close` no longer blocks on it. This is also a genuine
`second-implementation-is-not-a-second-opinion`: `check-unattended.sh:255` asserts the same invariant
**correctly** with `a=$(region "$f" ...) || fail 8`, where the assignment does propagate the
substitution's status. Two implementations of one rule that disagree on the unreadable case.

The driver's only other validation of that pair is at `:851`, inside `--preflight` — which runs at the
**start** of the run. Between preflight and `--close` the run itself writes that file, which is
precisely the window this item exists to close.

**Fix.**

```bash
gen=$(region "$rel" "$GEN_OPEN" "$GEN_CLOSE" 2>/dev/null) || return 1
[ -z "$(printf '%s' "$gen" | tr -d '[:space:]')" ] \
  && region "$(readme_of "$slug")" "$SRC_OPEN" "$SRC_CLOSE" >/dev/null 2>&1
```

**Left-shift gate.** An arm in `unattended.test.sh`: corrupt the run-state file's open marker, then
assert `--close` REFUSES naming `records-current`. Generalizable — the four `region` call sites should
each have a malformed-pair arm, and the `marker-contract.test.sh` case table is where that belongs.

### M2 — a LANDED run record no longer pins the roster it landed

`memory/builds/aSiftedPlaybook/RUN.md` · `memory/builds/aSealedCaravan/RUN.md` ·
`tools/unattended/unattended.sh:894` *(mine — no verifier raised this; it is the owner's question 3)*

Full reasoning is in **Answers (3)** above. Short form: the inversion is right for an OPEN run and
lossy for a FINISHED one. `aSiftedPlaybook/RUN.md` is `phase: LANDED` and records witness, keepalive,
anchor triple and base — but nothing about which seven units the run covered. The roster is now a live
query against `README.md`, a document that keeps moving after the run ends, so the landed record's
answer changes retroactively and silently. Both migrated files are correct **today** (I diffed the
derived slice against each deleted copy), which is why nothing reds.

**Fix.** Not a revert. At `--landed`, append the derived roster **once** into the immutable
`## Run facts` block — `units-at-landing: <ids>` — where the driver already writes facts that must not
move. That keeps one live home for the roster (the README) and gives the finished record the one thing
it lost: what the run's scope actually was. Nothing to keep fresh, because a landed run has no next
read.

**Left-shift gate.** Add to `check-unattended.sh`: a run-state file at `phase: LANDED` must carry a
`units-at-landing:` fact. It is a pure record-shape predicate, the same family as check 8, and it
converts "the finished record is complete" from a habit into an assertion.

---

## LOW

### L1 — `splice()` is dead code that a bar leg still certifies

`tools/unattended/unattended.sh:117` · `tools/memory-tree/marker-contract.test.sh:99,153` · `AGENTS.md:221`
*(id 21)*

This diff removed the last call site (the `splice` in `verb_preflight`). Verified by repo-wide grep:
every remaining `splice` mention in the driver is a comment (`:97`, `:102`, `:442`) plus the definition
at `:117-128`. **No call site anywhere** in `tools/`, `skills/`, `.githooks/` or `.claude/`.

Meanwhile `marker-contract.test.sh` still drives it as one of the "four live readers", locating it by
`grep -n '^splice()' "$U"` + 12 lines — so the dead function is load-bearing for a bar leg, and
deleting it breaks the leg. AGENTS.md:221's *"drives all four live readers"* is now false.
`unattended.test.sh:452`'s *"the splice succeeded but there is nowhere to record a fact"* is stale for
the same reason; that arm now exercises marker validation.

**Fix.** Delete `splice()`, drop the `r_splice` reader from `marker-contract.test.sh` (`:99`, `:153`),
correct AGENTS.md to three readers, and refresh the `unattended.test.sh:452` comment. If the marker
contract genuinely wants a splice implementation under test, point the leg at
`gen_build_index.py::apply_region`, which still has callers.

**Left-shift gate.** The drift-audit kit already hunts dead code at Tier 1+. A cheap gateable version
for shell: every top-level `name()` in a kit engine has at least one non-comment reference elsewhere in
that kit, waived by a shrink-only list. This is the second dead-shell-function this repo has shipped.

### L2 — check 8's README guard is dead plumbing that silently narrows the check

`tools/unattended/check-unattended.sh:254` *(id 23)*

`rd=${f%/RUN.md}/README.md` is computed solely to gate `if [ -f "$rd" ]`, and **nothing inside the
block reads it** — after the rewrite both arms read only `$f`. Under byte-equality the guard was
load-bearing (the README was the comparison source; the removed `b=$(region "$rd" ...)` line is right
there in the diff). Under emptiness it only narrows the check for free: a tracked `RUN.md` with no
sibling `README.md` skips check 8 entirely, **malformed-marker arm included**. The kit's fixture always
has both files, so no arm covers the skip.

**Fix.** Delete `rd=` and the `if [ -f "$rd" ]` wrapper; run both arms unconditionally on `$f`. If the
README's presence is itself worth asserting for a run-state file, make that its own named `fail`, not a
silent skip.

**Left-shift gate.** An arm that drops a tracked `RUN.md` with a poisoned generated region and **no**
sibling README, asserting check 8 still fires. Green-by-absence is the class; the general form is that
every `if [ -f ... ]` guard in a check script needs an arm for the absent branch.

### L3 — the driver's header still declares the retired COPY invariant

`tools/unattended/unattended.sh:29-30`, and the `--preflight` synopsis at `:5` *(ids 14, 24)*

> *"It also derives NOTHING. The generated region is a COPY of the build README's already-derived,
> already-byte-compared slice. One derivation in the tree; this file is not a second one."*

Both halves are false after this unit, **two lines above** the `KIT_UNATTENDED_VERSION=1.5` the same
commit bumped. `verb_status:894` now derives from the README on every read (its own new comment says
so) and `dod_met`'s `records-current` asserts the copy's absence. The sibling header in
`check-unattended.sh` **was** updated in this same diff, which shows the pair is meant to track the
design and this one was missed. `:5` still advertises `--preflight` as "assert, pin, record, render"
although preflight no longer renders anything.

This is the single most authoritative in-code statement of the contract, it is the first thing a reader
of the driver sees, and it now contradicts the shipped protocol on both sides.

**Fix.** Replace with the 1.5 statement — the driver derives nothing and copies nothing; the unit list
is read from the build README on every read and the generated region is empty by contract — and drop
`render` from the `:5` synopsis.

**Left-shift gate.** The unattended kit already gates shipped-protocol ≡ installed-protocol. Extend it
one notch: the driver's contract paragraph and `check-unattended.sh`'s must both contain the
protocol's own invariant sentence. That is a `grep -qF` against one string in `PROTOCOL.template.md`
and it would have caught this exact miss.

### L4 — `AGENTS.md` still says "nine inventories"; there are ten

`AGENTS.md:155` *(id 15)*

`memory/map/generated/inventories.json` now holds **10** keys — `gate-legs`, `kits`, `git-hooks`,
`workflow-scripts`, `skill-engines`, `rendered-skills`, `gotcha-classes`, `guides`, `backlog-shards`,
`lexicon-verbs` — and this diff added exactly one of them. The bullet's count and its enumeration both
predate it. The drift-audit bullet three lines up **was** updated in the same diff, so this is an
oversight, not a scoping choice. It is also the counted-population-written-in-prose class that the
govkit bullet at `:172` explicitly forbids after it rotted twice.

**Fix.** Prefer dropping the numeral: *"every inventory `all_inventories()` declares"*, matching how
this charter already handles the dossier/baseline pair by pointing at `reuse_lookup.py`. Failing that,
"ten" plus "the declared verb table" in the enumeration.

**Left-shift gate.** `test_codebase_map.py` already knows the live count. Add an arm asserting the
charter states no numeral for it — or, if a numeral is kept, that it equals
`len(ext.all_inventories())`. The repo has already ruled that counts in prose rot; this makes the rule
enforceable rather than remembered.

### L5 — v2.10 ships with no history entry for what v2.10 changed

`parallel-coding-governance.template.md:3,6,12` *(id 16)*

Line 3 reads `Template **v2.10** · 2026-08-16` and line 12 carries
`<!-- governance-template: v2.10 -->`, both bumped here. The inline history's newest entry is still
`**v2.9 (2026-08-16):**` (line 6), with v2.8 below it. **No v2.10 entry exists anywhere in the file**,
so the deliverable this bump ships — the §0 "when no rule below covers it" fallback rule, this unit's
entire product — is undocumented in the file that carries it, while both prior bumps documented
themselves.

Nothing gates it: `check-placeholders.sh` compares the two markers, and both say v2.10, so the
marker-agreement predicate passes.

**Fix.** Prepend ahead of the v2.9 entry:
`**v2.10 (2026-08-16):** §0 gains a fallback rule for decisions no later section covers.`

**Left-shift gate.** Add a predicate to `check-placeholders.sh`: the version in the
`governance-template:` marker must appear as a `**vN.N (` history entry in the template body. One
regex, and it makes the lockstep gate check the thing the lockstep is FOR rather than only that two
numbers agree.

### L6 — a pin comment makes a behavioural claim the code refutes

`tools/drift-audit/drift_signals.py:197-198` *(id 13)*

> *"adding a LANGS entry without re-ratifying turns this to 1 the same day."*

False on two independent grounds. First, `stale = langs_at[:10] > stamp` is date-only and **strictly
greater**, so a LANGS change committed on the ratification date gives `"2026-08-16" > "2026-08-16"` =
False — never 1, same day. Second, B2 means no later change can raise the date either.

Measured live: `git log -1 -S "LANGS=" -- .lexicon.conf` → `b062615`, dated 2026-08-16;
`ratified="2026-08-16 node d"`. Today's 0 is produced by equality, not judgement.

A falsifiable behavioural claim contradicted by the code, in the one file whose entire subject is
records that stopped matching reality.

**Fix.** After fixing B2, restate to what the code does: same-day edits are indistinguishable at the
stamp's granularity, and only a LANGS commit on a **later calendar day** fires. If same-day detection
is wanted, compare full timestamps and require `ratified` to carry a time.

**Left-shift gate.** Nothing mechanical is worth building for one comment. The cheap habit: a pin
comment that states a behaviour must name the arm that proves it. Here the arm is H1's, and it does not
prove it — so the comment and the arm would have been fixed together.

---

## What is NOT wrong (measured, so the green is meaningful)

- **PLAY-dClosedLexicon-1 is otherwise clean.** The §0 fallback rule reads correctly, the §14 backlog
  row's WONTDO carries a real refutation rather than a deferral, and the marker lockstep across the
  template and domain-rules is genuine (both at v2.10; `check-placeholders.sh` agrees). Only the
  missing history entry (L5).
- **The `lexicon-verbs` extractor is in the right tier**, and its comment argues the case honestly per
  direction — the ADDITION half is weak for a hand-authored vocabulary and it says so; the DELETION
  half is load-bearing. Reading through the lexicon's own conf reader rather than hand-rolling a second
  parser is correct and avoids `second-implementation-is-not-a-second-opinion`. The defect is the
  unguarded prefix (B1), not the design.
- **The uninstall ORDER in `tools/lexicon/README.md` is the right shape** — it states plainly that the
  property is unachievable and only the procedure works, and the mid-teardown orphan arm in
  `adopt-lexicon.sh` names the state a hurried teardown actually lands in. One gap: it never says to
  delete the kit directory, which is what makes B1's teardown route reachable.
- **`SIGNALS` at `drift_report.py:666` has no phantom element.** The `trailing-comma-counted-as-an-element`
  lens found nothing: 8 declared, 8 in `--json`.
- **The three lexicon pins are measured against this corpus.** `pin-copied-from-another-corpus` found
  nothing; the unused-verb pin of 3 is honestly non-zero and its comment explains the direction
  correctly. Note that B2 makes the *staleness* pin of 0 vacuous — but the pin is right, the probe is
  broken.
- **TOOL-dClosedLexicon-3's inversion is correct and well-argued.** Check 8's rewrite, `records-current`
  following it, `ARMS_FLOORS` 39→38, protocol §2 rewritten in both copies with an explicit "this
  inverted an earlier design" paragraph — all sound. Its defects (M1, L1, L2, L3) are edges of a good
  change, and M2 is a design gap the change surfaced rather than caused.

---

## Closing note on the bar

The full bar is **63/63 green** and two of the twelve defects here are blockers, so this review's
value is entirely in explaining **why green was wrong**:

- **B1** is invisible because the fixture that would catch it was built around the hardcode.
- **B2** is invisible because `live: True` is a literal, which disarms the kit's own DEAD-PROBE guard.
- **H1** is why B2 shipped: the arm proving the signal can move fires off the wrong input.
- **H2** is invisible because `--check` is correct and only the human render is wrong.
- **M1**, **L2** are green-by-absence: the failing state has no fixture.
- **L1**, **L3**, **L4**, **L5**, **L6** are all prose or dead code, which no gate reads.

Every one of the five left-shift gates proposed for the blockers and highs is a few lines in a file
that already exists. The most valuable single one is **B2's**: *no signal may return a literal
`"live": True`*. It is grep-able, shrink-only, and it is the general form of the failure this kit
was built to refuse.
