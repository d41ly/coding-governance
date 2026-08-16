# Tier-2 review — W4, the four rows the closing review left open

**Serves:** diff-review TOOL-aBatchedTribunal-1 TOOL-aBatchedTribunal-6 TOOL-aBatchedTribunal-8  <!-- inferred: scoped to W4, the rows the closing review left open; that build's whole spec-defined set -->

- **subject** — `9b0f42f fix(tools): W4 — the four rows the closing review left open` (one commit,
  22 files, +721/-40), closing four backlog rows: the memory-recall BUILD MARKER, the
  `KIT_MEMORY_TREE_VERSION` 1.5 → 1.6 epoch gate, the `corpus_ids.py` STRUCTURAL reachability arm,
  and the invocation-shape launcher ban (§3b of `resolve-python.test.sh`).
- **review shape** — raw 31 · confirmed 24 · refuted 7 · unverified 0 · **precision 0.77**.
- **method** — every finding below was reproduced by RUNNING the code and planting mutations, then
  put through an adversarial skeptic pass. The 24 confirmed rows collapse to **12 distinct defects**
  (several were found independently by more than one pass); the duplicate ids are listed per row.
- **counts** — 1 blocker · 4 high · 5 medium · 2 low.

The commit's subject is *gates that cannot silently pass*. The dominant finding class is that the
new harnesses guarding those gates can themselves pass while the thing they guard is broken.

## What I ran

| Probe | Result |
|---|---|
| `bash tools/memory-tree/check-verdict-epoch.sh` (live tree) | `clean — 2 non-comment line(s) changed and the version moved 1.5 -> 1.6`, rc 0 |
| `check-verdict-epoch.test.sh` against a gate whose FAILED branch was mutated `exit 1` → `exit 0` | **all 10 arms `arm ok`, `PASS — all arms held`, RC=0** |
| `python tools/memory-recall/selftest.py` with `query.py:342` (`marker.write_text`) replaced by `pass` | **`28/28 checks passed`** |
| `python tools/memory-recall/selftest.py` with the deletion-time re-check (`query.py:562-564`) deleted | **`28/28 checks passed`** |
| `bare_scan` (extracted verbatim from `resolve-python.test.sh:130-140`) over synthetic launcher shapes | quoted / exported / mid-line / env-prefixed assignments all MISSED |
| `check-verdict-epoch.sh` in a `git clone --depth 1` with an unbumped engine change | `skip — no mainline base`, rc 0 |

Working tree restored after each mutation; `git status` clean.

---

## BLOCKER

### B1 — `arm()` never asserts an exit code, so the new merge-bar gate can be made fail-open with all 10 arms green

**`tools/memory-tree/check-verdict-epoch.test.sh:13`** *(confirmed id 15)*

```sh
out=$(cd "$dir" && bash "$GATE" $base 2>&1); rc=$?
case "$out" in
  *"$want"*) printf 'arm ok    %s\n' "$label" ;;
```

`rc` is captured and then read **only inside the failure `printf`** at line 16. No arm in the file
asserts an exit status. `tools/run-gates.sh:21` judges a leg *purely* by `rc=$?`, and
`tools/gate-legs.json` ships both the gate and this self-test as merge-bar legs — so the one value
the runner keys on is the one value the harness never checks.

**Verified by mutation.** I copied gate + test to a scratch dir, changed the FAILED branch's
`exit 1` (`check-verdict-epoch.sh:68`) to `exit 0`, and ran the untouched self-test: every arm
printed `arm ok`, the suite printed `PASS — check-verdict-epoch: all arms held`, RC=0 — while the
gate was still correctly *printing* the defect it is supposed to *block*. A one-character edit turns
the newest merge-bar gate into a printer and the bar stays fully green.

**Fix.** Give `arm` an expected exit code as a third positional (default 0) and assert it alongside
the substring:

```sh
arm() { # label · expected-substring · dir · [base] · [expected-rc]
  local label=$1 want=$2 dir=$3 base=${4:-} want_rc=${5:-0}
  out=$(cd "$dir" && bash "$GATE" $base 2>&1); rc=$?
  case "$out" in *"$want"*) ;; *) fail ;; esac
  [ "$rc" = "$want_rc" ] || fail
}
```

Arms 1 and 4b expect rc 1; arms 2, 3, 4a and 6 expect 0; arm 5's two misconfigured cases expect 2.

**Left-shift gate.** `tools/memory-tree/check-arms.py` already enforces "every `fail` branch armed by
a positive assertion naming its own failure text". Extend it with a companion rule keyed on
`tools/gate-legs.json`: for every `*.test.sh` whose subject is itself a leg in the manifest, require
the harness to reference `$rc`/`$?` in a **test position** (`[ "$rc" = … ]`, `case $rc`), not only
inside a diagnostic `printf`. That is a grep-shaped rule over the same population `check-arms.py`
already walks, and it fires on this exact file today.

---

## HIGH

### H1 — nothing arms the PRODUCER half of the build marker: deleting `marker.write_text` leaves the suite 28/28

**`tools/memory-recall/query.py:342`** *(confirmed ids 14, 26)*

Every marker arm in the suite plants `building` **by hand** through `_sib(marker_age=)`
(`selftest.py:579, 582, 601, 603, 643`). Grep finds no arm that calls `build_cache` or `ensure_cache`
at all. So the suite pins the **predicate** (`_mid_build`) and never the **writer**. The marker is
also unobservable after the fact — the `finally` removes it — so no existing arm can cover it
incidentally.

**Verified by mutation** (run here, at 9b0f42f): replacing line 342 with `pass` yields
`---- memory-recall selftest: 28/28 checks passed`. The resulting `FileNotFoundError` in the `finally`
is a subclass of `OSError` and is swallowed by the existing `except OSError: pass`, so nothing even
surfaces in the output.

**Consequence.** `build_cache` can stop announcing itself — a bad merge, a refactor that moves the
`mkdir` back below `_docs`, an exception path inserted before the write — and the whole
TOOL-aBatchedTribunal-2 fix silently reverts to the mtime-only test, which the code's own docstring
(`query.py:429-441`) documents as False for 31% of a build, with the merge bar green.

**Fix.** Observe the marker from outside a REAL build. Cheapest in-process form: import `query`,
monkeypatch `_docs` to record `(dirp / BUILD_MARKER).exists()` and then raise, call `build_cache`,
and assert the marker was present during extraction AND absent afterwards (which also arms the
`finally` on the raising path).

**Left-shift gate.** Add a "producer/consumer pairing" arm to `selftest.py`'s own meta-section: for
each module constant that names an on-disk protocol artifact (`BUILD_MARKER`), assert the suite
contains at least one arm that reaches the writing call path, not just the reading one. Mechanically:
`ast`-walk `query.py` for the function that writes the constant (`build_cache`), then assert that
name appears in `selftest.py`. Two lines, and it reds on today's tree.

---

### H2 — `t_budget_recheck_before_delete` never executes the re-check it is named for

**`tools/memory-recall/selftest.py:647`** *(confirmed ids 7, 17, 25)*

The racer's marker is planted **before** the run (`selftest.py:642-643`, `marker_age=0.0`), so
`_mid_build(racer)` is already True at the *candidate filter* (`query.py:536`). `racer` is therefore
never a candidate: `candidates` is empty, `plan` is empty, `projected == total > budget`, and
`evict_over_budget` returns at the shortfall branch (`query.py:550-557`) **without ever entering the
deletion loop at :558**. The re-check at `query.py:562-564` is never reached.

The assertion's disjunction makes this invisible:

```python
assert "cannot be brought under it" in proc.stderr or "did NOT evict" in proc.stderr
```

The first alternative is what actually fires, so the arm is green for a reason that has nothing to do
with the race.

**Verified by mutation:** deleting `query.py:562-564` entirely leaves the suite at 28/28 with this arm
reporting `ok`. Spec **AC3** ("When a build starts after the plan is made, the deletion loop skips it
and says so", spec-aBatchedTribunal-6 §6) therefore has **zero** backing coverage, and the message
`did NOT evict %s: a build started in it after the plan was made` is emitted by no test in the suite.

Note that spec **AC4** ("when the marker disjunct is removed, AC1-AC3 all red — verified by removing
it") does *not* rescue this: removing the disjunct reds this arm through the **candidate filter**
(racer becomes evictable and is deleted), not through the re-check, so the mutation that was actually
run cannot distinguish a present re-check from an absent one.

**Fix.** Make the marker appear BETWEEN the plan and the loop, and assert the specific message. Drop
the `or "cannot be brought under it"` escape hatch. In-process: import `query`, build the sibling tree
so `racer` is a legitimate candidate at snapshot time (no marker), monkeypatch `query._remove_cache_dir`
so its first call plants a fresh `building` marker in the NEXT planned directory, call
`evict_over_budget`, then assert the second directory survives AND `"did NOT evict"` is in the
returned lines.

**Left-shift gate.** A "message coverage" arm for `query.py`: collect every distinct literal appended
to `out` in `evict_over_budget` (an `ast` walk over `out.append` string constants), and assert each
one is asserted somewhere in `selftest.py`. `did NOT evict` is currently only reachable through a
disjunction, so tightening it to "each message is the *sole* subject of at least one assertion" reds
today. This generalizes past this one row — it is the repo's own "a gate that passes by finding
nothing" class applied to messages.

---

### H3 — the live-tree arm's expected substring prefixes every message the gate can emit, so it cannot fail

**`tools/memory-tree/check-verdict-epoch.test.sh:94`** *(confirmed ids 2, 8, 16, 28)*

```sh
# The live tree must be clean, and it must be clean because the constant MOVED — not because nothing
# changed. Asserting the message discriminates the two.
arm 'the live tree is clean for the current epoch' 'verdict-epoch:' "$HERE/../.."
```

**Every** line `check-verdict-epoch.sh` can print is prefixed `verdict-epoch:` — the exit-2 messages
(lines 25, 29, 42, 52), the loud skip (39), both clean variants (55, 70) and all nine FAILED lines
(60-67). Combined with B1 (rc never asserted), the arm passes on clean-unchanged, clean-moved, FAILED,
the shallow-clone skip and both misconfiguration exits. The only way it can fail is the gate printing
nothing at all.

**Verified by mutation:** setting `KIT_MEMORY_TREE_VERSION=1.5` in the working-tree engine made the
gate print `verdict-epoch: FAILED — … is 1.5 at BOTH ends` and return rc 1; the self-test still
printed `arm ok    the live tree is clean for the current epoch` and `PASS`. Repointing the same arm
at fixture repo `$A` (known to FAIL) likewise stays green.

The comment directly above it claims the exact opposite of what the code does — this is the
"a claim in a comment the code does not do" class, stated as covered.

**Fix.** Assert the discriminating text plus the exit code (once B1 lands):
`arm 'the live tree is clean for the current epoch' 'the version moved' "$HERE/../.." '' 0`.
`the version moved` is emitted only when a change was seen AND the constant moved; it is absent from
FAILED, from the skip, and from both exit-2 paths. Keep a second arm for the
`behaviour-bearing lines are unchanged` phrasing so the pair still passes after the epoch settles.

**Left-shift gate.** A vacuity check for substring assertions, runnable in `check-arms.py`: for each
`arm <label> <want>` in a `*.test.sh`, if `<want>` is a substring of **every** string literal the
subject script can `echo`, red it as a non-discriminating assertion. The subject's message set is
recoverable with `grep -oE 'echo "[^"]*"'` over the gate. This is the same "assertion must name its
own failure" principle the file already applies to `fail` branches, extended to `pass` branches.

---

### H4 — the invocation-shape ban matches only two narrow spellings, and misses live unmarked launchers already in this tree

**`tools/lib/resolve-python.test.sh:136-137`** *(confirmed ids 5, 9, 21, 29)*

The ban has two alternatives. Alternative 1 requires the launcher to be immediately preceded (modulo
whitespace) by a metacharacter or a keyword from a fixed list, with **no intervening argument**.
Alternative 2 is line-anchored and unquoted:

```awk
/^[[:space:]]*[A-Za-z_][A-Za-z0-9_]*=(python3|python|py)([[:space:]]|;|$)/
```

Measured against the shipped `bare_scan`, extracted verbatim — **all of these are MISSED**:

| Shape | Caught? |
|---|---|
| `PYBIN=python3` (the suite's own fixture, line 157) | yes |
| `PY="python3"` / `PY='python3'` | **no** — one quote character defeats it |
| `export PY=python3`, `readonly PY=python3`, `local PY=python3` | **no** — the `^` anchor |
| `PY=$(resolve_python) \|\| PY=python3` | **no** — mid-line |
| `GOV_X=1 python3 build.py` | **no** — env prefix; a genuine unresolved execution |
| `PYBIN=${GOV_PY:-python3}` | **no** |
| `bash -c "python3 -m json.tool"`, `xargs -n1 python3 run.py` | **no** |

**Three live unmarked sites in this tree pass the ban today** — `bash tools/lib/resolve-python.test.sh`
returns `PASS — 36 assertions held` with all three present:

- `tools/check-wiring.sh:56` — `PY=$(resolve_python) || PY=python3`. This is the identical
  print-only-launcher shape that line **58** carries a `gov:literal-python` marker for. **This commit
  marked line 58 and left 56 unmarked** — because the gate cannot see it.
- `tools/drift-audit/adopt-drift-audit.sh:137` — `2. Run:  python $KIT_REL/drift_report.py`, inside
  the `cat <<EOF` remedy, shipped to adopters.
- `tools/codebase-map/adopt-codebase-map.sh:53` — `MAP_PY=python3` in a usage string.

The §3b header cites `adopt-drift-audit.sh` as the motivating case — "this shipped, ran, and was
caught by a person" — and the ban still reports clean over an unmarked bare launcher in that very
file. The red-half arm at line 157 asserts only the line-anchored unquoted spelling, so the hole
reads as closed.

**Fix.** Key on the launcher TOKEN and let the marker be the only escape hatch: flag any non-comment,
non-marked line outside the resolver block matching
`(^|[^A-Za-z0-9_./-])(python3|python|py)([^A-Za-z0-9_./-]|$)`. Over the tracked `*.sh` population that
adds roughly six sites, each genuinely a launcher name in prose or a manifest token — mark them, and
fix the drift-audit remedy to name `$DA_PY` rather than `python`. If the token form is judged too
broad, the minimum is to widen alternative 2 to
`(^|[[:space:]]|[;&|(){}])(export|readonly|local|declare|typeset)?[[:space:]]*[A-Za-z_][A-Za-z0-9_]*=["']?(python3|python|py)["']?([[:space:]]|;|$)`
and allow an env prefix before a bare invocation. Add red-half arms for `PY="python3"`,
`export PY=python3`, `|| PY=python3` and `VAR=1 python3 x.py`.

**Left-shift gate.** A **scanner mutation arm** inside `resolve-python.test.sh`: keep a small table of
launcher shapes that MUST fire, generated by permuting the axes the regex is sensitive to (quoting ×
declaration keyword × line position × env prefix), and assert every permutation produces a hit. That
turns "which spellings does this cover?" from a reading exercise into an enumerated, extensible
assertion — and it is the same technique the commit's own `corpus_ids` work introduced (derive the
population, don't list it).

---

## MEDIUM

### M1 — an unresolvable base exits 0, so in a shallow clone the new leg is permanently green

**`tools/memory-tree/check-verdict-epoch.sh:38-41`** *(confirmed id 1)*

```sh
if [ -z "$BASE" ]; then
  echo "verdict-epoch: skip — no mainline base to compare against (shallow clone or no default branch)"
  exit 0
fi
```

**Proved** in a `git clone --depth 1` of this branch: appended `echo "an unbumped behaviour change"`
to `check-memory-hygiene.sh`, committed, ran the gate — `skip — no mainline base…`, rc 0.
`actions/checkout` defaults to `fetch-depth: 1`, and AGENTS.md states the plan is to run
`tools/run-gates.sh` in a workflow. The one gate whose entire job is "the constant cannot silently sit
still" would sit permanently green in exactly the environment it is headed for, while
`hygiene-parity.test.sh` keeps deriving its floor from the constant it no longer guards.

The "SKIP LOUDLY" defense fails on two facts. (a) `tools/run-gates.sh:21-23` captures each leg's
output and prints it **only on rc != 0**, so the loud skip is swallowed and the bar prints
`GATE ok    verdict epoch` — the gate's own stated rationale ("silence here would be indistinguishable
from *the constant is fine*") is precisely what happens through the runner it rides. (b) The sibling
harness from this same commit, `tools/memory-tree/hygiene-parity.test.sh:54-61`, meets the identical
missing-history condition and **exits 2** with "A shallow clone or a squashed import does that…
(CI: fetch-depth: 0)". Two harnesses, one class of unavailable history, opposite verdicts — and the
fail-open one is the gate whose whole job is that the constant cannot sit still.

**Fix.** Make the unresolvable base a hard error (exit 2) so a misconfigured checkout is loud; or fall
back to `HEAD~1` and exit 2 if even that is unavailable. If the skip must stay green for local
detached probes, gate it behind an explicit `GOV_EPOCH_ALLOW_SKIP=1` so CI cannot inherit it by
accident, and add a self-test arm asserting the CI shape reds.

**Left-shift gate.** A cross-harness consistency check: assert that every gate reading git history
handles "history unavailable" the same way. Concretely, add to `run-gates.test.sh` an arm that runs
the whole bar inside a depth-1 clone fixture and asserts no leg reports `ok` via a skip — i.e. the bar
grows a `--strict-history` mode that CI sets, under which any skip is a failure.

### M2 — the constant is compared only at the two ENDPOINTS of the range, so one bump excuses every later change in it

**`tools/memory-tree/check-verdict-epoch.sh:59`** *(confirmed id 27)*

**Reproduced in a throwaway repo.** c0 at 1.5; c1 bumps to 1.6 AND changes the engine; c2 changes the
engine again with no bump. `check-verdict-epoch.sh <c0>` prints
`clean — 4 non-comment line(s) changed and the version moved 1.5 -> 1.6`, rc 0 — while the same c2
judged against c1 correctly FAILS with `is 1.6 at BOTH ends`, rc 1.

This is exactly the defect the gate's own WHY section describes (verdicts moved across three commits
while the constant sat still): `hygiene-parity.test.sh:53`'s FLOOR resolves via
`git log -S"KIT_MEMORY_TREE_VERSION=$KITV" | tail -1` to the **bump** commit, which again predates a
verdict change. The gate's authoritative run is once at the push boundary over `merge-base..HEAD`,
which in this repo routinely spans several commits — so this is the normal path, not a corner.

**Fix.** Judge the range per-commit: for `c` in `git rev-list --reverse "$BASE"..HEAD`, if
`git diff -U0 "$c^" "$c" -- "$ENGINE"` has a non-comment added/removed line, require the constant to
differ between `$c^:$ENGINE` and `$c:$ENGINE`. Cheaper equivalent: require that the NEWEST commit in
the range which moves a behaviour-bearing engine line is also a commit that moves the constant.

**Left-shift gate.** Add the three-commit fixture above as arm 7 of the self-test — it is ~8 lines
given the existing `newrepo`/`engine` helpers and it reds on today's implementation.

### M3 — `ENGINE` is one file, but 8 of the 19 hygiene verdicts are produced by modules the gate never diffs

**`tools/memory-tree/check-verdict-epoch.sh:28`** *(confirmed id 10)*

`ENGINE=tools/memory-tree/check-memory-hygiene.sh` and the diff at line 46 is scoped `-- "$ENGINE"`.
But checks 9, 13-16 and 17-19 delegate to `gen_build_index.py`, `corpus_ids.py` and `gotchas.py`
(engine lines 425, 646, 656). A commit that changes only those modules changes what hygiene *says*
while the constant sits still and this gate prints `clean`.

**Reachable now, not hypothetical:** HEAD changes `corpus_ids.py` by 91 lines, and the constant moved
only because `check-memory-hygiene.sh` was independently touched. Nothing else covers it —
`check-kit-versions.sh` only asserts the constant/marker pair *exists*, and `hygiene-parity` derives
its floor from the same constant.

**Fix.** Make `ENGINE` a list — `check-memory-hygiene.sh gen_build_index.py corpus_ids.py gotchas.py`
— and run the same `-U0` diff + non-comment filter over each, failing if any moved without the
constant. The existing `^[[:space:]]*(#|$)` filter is already correct for Python comments.

**Left-shift gate.** Derive the list instead of hardcoding it: grep the engine for
`"$_PY" "$HERE"/*.py` invocations and diff exactly those files, then add a self-test arm that plants a
new delegated module in the fixture and asserts the gate picks it up. That way the gate's scope
follows the engine's real dependency set rather than a hand-maintained literal — the same
"population is derived, not listed" rule AC7 imposes on `corpus_ids`.

### M4 — the marker's pid is written and never read, and the `finally` unlink is unconditional

**`tools/memory-recall/query.py:342, 347`** *(confirmed ids 3, 11, 19)*

`BUILD_MARKER = "building"` (line 124) is a **fixed name**, and `cache_dir()` keys only on the
worktree path (line 248) — so all builders in one worktree share one marker path. Line 342 writes
`str(os.getpid())`; grep shows the only other read of the marker is `.stat().st_mtime` at line 452.
**The pid is write-only plumbing**, which is itself evidence the owner check was intended and omitted.
The `finally` at 345-349 unlinks unconditionally, with no owner check.

**Demonstrated against the real module:** with a previous build's files on disk (dbs older than the
manifest, so the mtime test is False), `_mid_build` was True while builder P2 held the marker, and
flipped to **False** the instant a second, shorter builder for the same directory ran its `finally`
unlink — while P2 was still mid-build.

`_mid_build` returning False is exactly the state in which another worktree's `evict_over_budget`
calls `_remove_cache_dir` on a live build — the `unable to open database file` data loss the marker
was added to stop. The spec's non-goal ("two builders writing one cache directory is already
survivable — last writer wins, the manifest is atomic") is reasoning about the databases' CONTENT
under two writers; it says nothing about licensing a third process to delete the directory, which is
the harm here.

**Fix.** Owner-scope the marker: write `building.<pid>` and have `_mid_build` treat the directory as
live if ANY unexpired `building.*` entry exists, with each builder unlinking only its own file. Keeps
the TTL semantics, removes the cross-process release, needs no lock protocol. (Minimal alternative:
read the marker before unlinking and remove it only when it still holds this pid.)

**Left-shift gate.** A "write-only field" lint for the recall kit's selftest: for each value written
into an on-disk protocol artifact, assert the module contains a read of it. `os.getpid()` written and
never parsed is the signal; it is a short `ast` walk and it fires here.

### M5 — the reachability checker's red half re-types the message instead of calling the checker, so it holds by construction

**`tools/memory-tree/corpus_ids.py:694-697`** *(confirmed ids 20, 31)*

```python
arm("...and the reachability checker can name an unreached branch",
    "is a `continue` no fixture reaches",
    lambda: "; ".join(f"corpus_ids.py:{n} is a `continue` no fixture reaches"
                      for n in sorted((want | {-1}) - _hit)))
```

`_hit` is populated only from `frame.f_lineno`, always a positive int, so `-1` is never removed, the
set is always non-empty, and the joined string always contains the asserted substring. I enumerated
the states — `want` empty, `_hit` empty, `want` fully hit, `want` unhit, tracer never fired — and the
arm passes in **every** one, including both total-failure states. `want` and `missed` are computed
outside the lambda, so there is no input under which it goes red.

It also **re-implements the f-string from lines 690-691**, so the format is now written twice and can
drift: a later edit to the wording or to the line-offset arithmetic in `_walk_continues` leaves this
arm green. Its stated purpose — telling "none missed" apart from "the tracer never ran" — is already
served by the population arm at line 698 (`len(want) >= 4`) plus the real arm at 689.

**Verified:** plant an unreachable `continue` in `walk()` AND replace the positive arm's lambda with
`lambda: ""`, and the suite still prints `PASS — corpus_ids: all arms held` with the unreached branch
undetected.

**Fix.** One source for the message:

```python
def _missed_msg(lines):
    return "; ".join(f"corpus_ids.py:{n} is a `continue` no fixture reaches" for n in lines)
```

Positive arm calls `_missed_msg(missed)`; red half calls `_missed_msg(sorted((want | {-1}) - _hit))`.
The red half then actually exercises the reporter it vouches for.

**Left-shift gate.** Extend `check-arms.py`'s remit to Python harnesses with one rule: a red-half arm
whose lambda contains no call to a function under test is a tautology. Detectable by `ast` — flag any
`arm(...)` lambda body composed solely of literals, comprehensions and set arithmetic over locals.
This class already has a name in this repo; it just is not yet enforced on the `.py` side.

---

## LOW

### L1 — an unreadable old constant fails OPEN

**`tools/memory-tree/check-verdict-epoch.sh:51, 59`** *(confirmed id 30)*

Any failure of `git show "$BASE:$ENGINE"`, or a base whose constant the `sed` cannot parse, leaves
`was` empty; line 59's `[ -n "$was" ]` guard then skips the equality test entirely and falls through
to line 70's unconditional `clean`, rc 0.

**Reproduced:** in a throwaway repo where the base blob spells the constant quoted
(`KIT_MEMORY_TREE_VERSION="1.5"`, which the sed capture reduces to empty) and HEAD adds
behaviour-bearing lines at the same version, the gate printed
`clean — 3 non-comment line(s) changed and the version moved <absent> -> 1.5`, rc 0, where the correct
verdict is FAIL. Also observed live: in a deep scratchpad path `git show` returned
`fatal: … Filename too long` and produced the same shape.

The asymmetry is the tell — an unreadable `now` is a named exit 2 (line 52) while an unreadable `was`
is a silent pass. Line 58's comment justifies fail-open only for "a base that predates the constant";
the code cannot distinguish that benign cause from an unreadable base. No self-test arm covers it.

**Fix.** Separate the two causes: if `git cat-file -e "$BASE:$ENGINE"` succeeds but the sed yields
nothing, `echo "verdict-epoch: could not read KIT_MEMORY_TREE_VERSION at $BASE"; exit 2`.

**Left-shift gate.** Fold this into the same `--strict-history` mode proposed in M1: under it, every
"could not read" path is exit 2 rather than a pass. One flag covers M1 and L1 together.

### L2 — the resolver-block exemption arm is vacuous: the line it plants does not match the ban at all

**`tools/lib/resolve-python.test.sh:166-167`** *(confirmed id 13)*

```sh
{ printf '# >>> resolve_python\n'; printf '  for c in python3 python py; do :; done\n'; printf '# <<< resolve_python\n'; } > "$plant"
[ -z "$(bare_scan "$plant")" ] || bad "the resolver block is not exempt from its own ban"; ok
```

**Measured:** that planted line produces no `bare_scan` hit **with the markers stripped** — neither
alternative matches (`for`/`in` are not in the keyword set, and the assignment alternative needs
`NAME=`). So the arm passes whether or not the block-exemption rules exist. I also ran a variant
scanner with both `>>> / <<< resolve_python` rules deleted across every tracked `*.sh`: 0 hits,
identical to the shipped scanner — the exemption protects nothing today either. The companion leak arm
at line 169 does not cover it (it fires on the post-marker `python x.py` regardless).

The §3b header calls this one of "TWO EXEMPTIONS, both narrow"; the author paired a red half for the
`gov:literal-python` exemption (line 165) and did not for this one.

**Fix.** Plant a line the ban actually matches inside the markers:

```sh
{ printf '# >>> resolve_python\n'; printf 'PY=python3\n'; printf '# <<< resolve_python\n'; } > "$plant"
```

Then removing the block rules reds the arm.

**Left-shift gate.** A self-consistency arm for exemption tests: for every "X is exempt" assertion,
assert that the SAME planted content **without** the exempting context DOES fire — the pattern already
used correctly at lines 164-165 for the marker. Making it a required pairing (each `[ -z "$(bare_scan …)" ]`
exemption arm must be adjacent to a `[ -n … ]` arm over the same body) is a structural rule
`check-arms.py` can enforce.

---

## What came back clean

Three of the requested hunt axes found nothing worth filing, and it is worth recording why:

- **A threshold inherited rather than measured here** — `BUILD_TTL_S = 900.0` is measured *in this
  repo*: `query.py:125-127` and spec §64 both give "~7700x the 0.117 s measured for this corpus", with
  the direction of safety argued (it cannot expire under a slow-but-live build on a far larger
  corpus). `SNIPPET_TOKENS = 64` cites FTS5's documented maximum; `DEFAULT_BUDGET = 20_000` cites a
  `union.py` measurement. This axis is genuinely well served.
- **The three-place version fact** (`check-memory-hygiene.sh`, `HYGIENE.template.md`,
  `memory/HYGIENE.md`) is a fact stated three times that CAN drift — but it is exactly what
  `check-kit-versions.sh` and `kit-dogfood-parity.test.sh` already pin, and the new gate's FAILED
  message names all three files. Covered.
- **The `corpus_ids` STRUCTURAL rewrite** is the strongest work in the commit: deriving the population
  from `walk()`'s AST via `sys.settrace` replaces a tautological shape filter with a real one, and
  AC7's "derived, not listed" is enforced by the `len(want) >= 4` arm. Only its red half (M5) is
  vacuous; the mechanism itself is sound and is the template the other three rows should follow.

## The pattern

Eight of the twelve defects are the same shape: **the new harness cannot observe the failure it was
written for.** B1 (rc never asserted), H1 (producer never called), H2 (the branch is never reached),
H3 (the substring matches everything), M5 (the red half re-types the message), L2 (the fixture doesn't
match the pattern) — plus M1 and L1, where the gate itself passes on an unreadable world.

The commit correctly identified that `hygiene-parity`'s floor rested on an unverified claim and built
a gate for it. The gate is right. What is missing is the same skepticism applied one level up: each
new arm needs a demonstration that it reds when its subject breaks. The single highest-leverage
left-shift is the one in B1 — extend `check-arms.py` from "every `fail` branch is armed" to
"every merge-bar harness asserts its subject's exit status" — because that one rule catches B1
directly and makes H3, M5 and L2 mechanically visible.
