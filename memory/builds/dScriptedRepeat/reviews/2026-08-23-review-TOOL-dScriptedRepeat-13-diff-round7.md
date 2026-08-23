**Serves:** diff-review TOOL-dScriptedRepeat-13 TOOL-dScriptedRepeat-14 TOOL-dScriptedRepeat-15

# dScriptedRepeat — diff review, round 7 (13, 14 and 15, the cumulative diff landing on main)

**Range:** `2b69704015b739a1736f79d5c35c661ddd8bb148...HEAD` — 11 commits, 33 files, 2335 insertions
and 62 deletions. The code half is `tools/unattended/check-playbook.sh`,
`tools/unattended/check-unattended.sh`, `tools/unattended/run-unattended-gates.sh` and
`tools/drift-audit/drift_report.py`; the rest is specs, records, gotchas and generated map artifacts.
**ROUND 7.**

**Review shape:** raw 17 · confirmed 16 · refuted 1 · unverified 0 · precision 0.94. The 16 confirmed
findings collapse to **9 distinct defects**. Four clusters were filed independently by two or three
lenses each; that corroboration is recorded per defect rather than counted as separate findings. Every
mechanism below was reproduced against the working tree before it was written down, and the
reproductions are quoted where they are the evidence.

## Verdict: BLOCKED

Three blockers, one high, one medium, four lows.

**The grading rule, stated so you can disagree with it.** A finding is a BLOCKER when it makes the
unit's own load-bearing claim false — not when it is merely severe. Unit 13's claim is "the bypass
flag is read back out of what landed"; blockers 2 and 3 each make that false, by a different route.
Unit 15's claim is written into its own comment — "the rc branches below therefore fire with the same
text, the same number of times" — and blocker 1 falsifies it verbatim. Unit 14 ships a report-only
signal with `gateable: False`, so nothing it does can change a merge verdict; its four defects are
graded on report quality and none is a blocker.

**The shape underneath the three blockers, stated once.** All three are the same mistake at three
sites: **a guard whose liveness assertion counts the wrong thing.** Check 10 prints how many records
it *opened*, not whether the literal it grepped is still the declaration (blocker 3) nor whether the
corpus it enumerated is the whole corpus (blocker 2). `_pbatch` fills every slot with a fabricated
`(rc 0, "")` and returns 0, so no channel learns the harness could not speak (blocker 1). In each
case the check that is not running is byte-indistinguishable from the check that found nothing, which
is the exact class §7 of the charter names and which this leg gates against everywhere else. None of
the three is a spelling problem, and none is fixed by adding a spelling.

**What the current suite sees: none of it.** The full bar and both new test arms are green over every
defect below. `check-playbook.test.sh`'s new arms all write
`BYPASS_BAN="--no-verify"` with no comment and no single quotes, and all use the fixture playbook,
which declares `grain` — so blockers 2 and 3 are outside the fixture by construction. `_pbatch`'s
misalignment path needs a parser whose answer spans a line, which no shipped specimen produces. I did
not re-run the full bar in this pass; the lenses' reproductions were all done in hermetic scratch
clones built from the kit's own `seed()`.

**The named high-value lenses that came back clean, recorded as negatives** — a review that only
prints hits is not distinguishable from one that did not look.

- **Check 26's `case` patterns faithfully reproduce the three EREs they replaced.** `^#   unattended.sh VERB( |$)`
  becomes two patterns against a corpus with a `\n` sentinel prepended and appended, one for the
  space case and one for the end-of-line case; the corpus is `$'\n'$(cat …)$'\n'`, so the first and
  last lines both anchor correctly. `^- .VERB. — ` becomes `*$'\n'"- "?"$v"?" — "*`, and a `case`
  `?` is exactly the ERE `.` for a single character. The Skill's fixed substring is unchanged. `$v`
  is inside double quotes in every pattern, so a verb is never read as a glob. No finding.
- **28b's hoisted corpora are true supersets, and the re-applied shell predicates match the EREs.**
  A line matching `declared_(list|scalar) .* KEY)` necessarily contains `declared_list ` or
  `declared_scalar `; a line matching `\^KEY([^A-Za-z_]|$)` necessarily contains `\^[A-Za-z_]`,
  because every template key begins with a lowercase letter or underscore. The comment filter moved
  from after the key test to before it, which cannot change the resulting set. `( |$)` is reproduced
  as the pair `*"^$_k")` and `*"^$_k"[!A-Za-z_]*`, and `[!…]` is the portable spelling. The
  `<file>TAB<rest>` record is split on its FIRST tab, so a tab inside the text survives. The per-file
  `break` reproduces the old once-per-file increment. No finding. One latent narrowing worth a
  comment rather than a fix: the caret prefilter would silently drop a key not starting with
  `[A-Za-z_]`, which the upstream `^[a-z_]+[[:space:]]*=` extraction makes unreachable today.

---

## BLOCKER 1 — `_pbatch`'s misaligned-reply fallback fabricates the PASSING answer, and check 28's only grader of the shipped template goes green on a real break

**`tools/unattended/check-unattended.sh:2240`** (the fallback), **`:2225`** (the comment that is
false), **`:2325`** and **`:2358`** (the two arms it silences).

Filed independently by three lenses. The comment above `_pbatch` asserts that a broken parser makes
the reply short, that every slot is then filled with the batch's own exit status, and that "the rc
branches below therefore fire with the same text, the same number of times". The first half is exact
and I confirmed it: an emptied parser body gives 127, a syntax error gives 2, both byte-identical to
what the removed `dl_run`/`ds_run` wrappers handed each caller. The second half is false. The same
branch is reached when the batch **ran fine** and the reply merely misaligned — one specimen whose
answer contains a newline overruns `_pairs` — and then `_rc` is the batch's own **0**. Every slot
becomes `(rc 0, "")`.

`(rc 0, "")` is the PASSING value in both template arms:

```
_tl_rows (2325):  if [ "$rc" -ne 0 ] … elif [ -n "$got" ] … fail 28
_ts_rows (2358):  if [ "$rc" -ne 0 ] … else case "$got" in *'#'*) fail 28
```

Reproduced three ways. (1) A standalone harness over the real driver parser bodies: inserting
`printf 'X\n'` at the top of `declared_list` drops the declared-list specimen loop from **10 failures
under the per-specimen wrapper to 4 under `_pbatch`** — the six specimens whose expected answer is
empty (`k = []`, `k =`, `k = [ ]`, `k =# globs`, `k =#globs`, `k = # globs…`) go RED to GREEN because
the fabricated empty answer equals what they wanted, and the four that still fail report `got []`
instead of the real answer. (2) A `declared_list` broken to newline-join its members — exactly the
drift this check polices — gives 6 failures naming real answers under the old path, two of them
through the rc arm, against 4 under `_pbatch`, none through the rc arm. (3) The decisive one: patching
`declared_scalar` identically in `unattended.sh` and `check-playbook.sh` (so the byte-compare at 28
stays green) to emit one extra stdout line **only when its body argument spans multiple lines**, rc
unchanged, leaves the whole leg at **rc 0 with zero output**. The single-line specimen batches stay
aligned and pass; the two template batches feed the multi-line `$tpl_block`, misalign, and both arms
read the fabricated silence as a clean parse. `tpl_list`/`tpl_scalar` still count rows, so the
per-loop liveness assertions pass too.

That is the leg's own stated invariant — "a dead harness must not be byte-indistinguishable from a
working one" — failing in the one direction the arms cannot see, in the loop the code itself calls
the shipped template's only grader.

**Scoping, so the blocker is not over-claimed.** A parser broken for ALL inputs still reds through the
fixed specimen arms (verified: an unconditional extra line produces 5 check-28 failures). The exposure
is input-shape-dependent breakage — which is precisely the shape the multi-line template block
presents and the shape a comment-leak regression takes.

**Fix.** Do not substitute a synthetic answer for slots the batch actually spoke for. Split the two
cases: keep the `$_rc` fill only when `_res` is empty (the body did not run), and when `_res` is
non-empty but its line count is not `_pairs`, `fail 28` once naming the parser, `_pairs` and the
received line count, filling `_PB_RC` with a nonzero sentinel so every arm's rc branch fires. Either
that, or make the framing newline-proof — `printf '%s\t%s\0'` read back with `read -r -d ''`, or emit
the answer length before the answer — so an embedded newline can never misalign the reply. Keeping
`dl_run`/`ds_run` as the fallback body is the cheapest way to make the degraded shape identical by
construction rather than by argument.

**Left-shift gate.** A check-28 self-test arm that patches a parser to emit a multi-line answer *for
multi-line input only* and asserts the leg REDS — the arm this diff would have failed. Generalise it:
for each `_pbatch` call site, an arm that makes the reply misalign and asserts a non-zero exit. The
class is stated in the gotcha corpus as **"a fallback that fabricates the passing value"** — a
degraded-mode substitute must never be a value any assertion reads as clean.

---

## BLOCKER 2 — check 10's bypass scan is nested inside the `grain` guard, so a `records`-without-`grain` playbook has its whole evidence corpus skipped, and the zero does not red

**`tools/unattended/check-playbook.sh:500`** (the scan), **`:386`** (the `if [ -n "$gr" ] && [ -n "$rr" ]`
it sits inside), **`:383`** (the only pairing refusal, which covers the inverse), **`:529`** (the note
that hides it).

Filed independently by three lenses. Check 10 needs only `$rr`; it enumerates `$rr/*.md`. It is
written inside a block that also requires `$gr`, and the only grain/records refusal in the leg is
line 383, which reds **grain-declared-without-records** — the reverse pairing. There is no
requiredness check on `grain` anywhere in the leg. `grain` and `records` are independent declared
nulls in `PLAYBOOK-TEMPLATE.template.md` (lines 47 and 49), so a playbook declaring `records` with
`grain = ""` is legal and passes every leg.

Reproduced in a scratch clone. With the shipped fixture playbook, `BYPASS_BAN="--no-verify"` and a
tracked record naming the flag: **grain declared → `PLAYBOOK check 10 FAILED`, exit 1, `bypass scan -
3 tracked evidence record(s) read`.** Change ONLY `grain` to `""`, records untouched → **exit 0,
`bypass scan - 0 tracked evidence record(s) read for the declared flag`, no failure anywhere.**

The state is not exotic. `verb_record_set` (`unattended.sh:3401`) writes `$root/set-$runid.md` from a
records root alone, grain irrelevant, including via the caller-supplied `RP_ROOT` form — so records
under such a root are written, tracked, and never read back. The driver's own grain refusal
(`unattended.sh:1207`, `fail 46`) guards only the `recipe`-mode authorization branch. A set-scoped-only
playbook is exactly the shape `set_checks` designs for, and its `set_checks` reader is inside the same
skipped block.

**The liveness assertion cannot see it, in two ways.** `BYPASS_SEEN` is one repo-wide counter (init
243, printed once at 529), so any other grained playbook keeps it non-zero and the line still reads
healthy while N records went unopened. And even at a true zero the line is a `note`, which never reds
— the DEAD PROBE branch is itself inside the skipped block, so it does not fire either. The block's
own "WHAT THIS DOES NOT REACH" paragraph at 496 names only the caller-supplied `--record-set` root, so
a reader is explicitly told the coverage shape is narrower than it actually is.

**Fix.** Hoist the check-10 loop out of the `gr && rr` block to just after
`rr=$(declared_scalar "$body" records)`, guarded on `[ -n "$rr" ] && [ -n "$CONF_BYPASS" ]` alone.
Then give the note teeth: track whether any playbook declared a records root at all, and `fail 10`
— not `note` — when a flag is declared, at least one root was declared, and `BYPASS_SEEN` is still 0.
A declared root that enumerates nothing is a scan that cannot move. If the loop must stay where it is,
the grain-less case belongs in the header's stated gap and the note must become per-root
(`bypass scan - <root> N record(s)`) so a root that contributed zero is visible.

**Left-shift gate.** A `check-playbook.test.sh` arm with `grain = ""`, `records` declared, and a
set record carrying the flag, asserting RED. Beyond the instance: a class gate over the leg's own
source asserting that every check whose population derives from `$rr` is reachable without `$gr` —
or, more cheaply, a structural arm that blanks each independently-declared playbook key in turn and
asserts the leg's printed population counts do not silently drop to zero. This is the round-5 lesson
(instance gates versus class gates) applied one level up.

---

## BLOCKER 3 — check 10 parses `BYPASS_BAN` with `sed | tr -d '"'` while every other reader SOURCES the same file, so a legal conf spelling makes it grep for a literal no record can contain — and it still reports armed

**`tools/unattended/check-playbook.sh:85`.**

Filed independently by three lenses. `check-playbook.sh:85` is the ONLY reader of `BYPASS_BAN` that
does not source the conf. `unattended.sh:216`, `check-unattended.sh:111` and `adopt-unattended.sh:126`
all do `. "$CONF"`. `.unattended.conf` is a sourced shell file, so both of these are legal and both
diverge:

| conf line | sourced value (driver, sibling leg) | check 10's value |
|---|---|---|
| `BYPASS_BAN='--no-verify'` | `--no-verify` | `'--no-verify'` (`tr -d '"'` strips only double quotes) |
| `BYPASS_BAN="--no-verify"   # the flag` | `--no-verify` | `--no-verify   # the flag` |

Reproduced end to end in a hermetic scratch repo built from the kit's own `seed()`. In both arms a
tracked evidence record literally containing `--no-verify` takes the leg from **RC=1 to RC=0**, and
the leg still prints `playbook: bypass scan - 3 tracked evidence record(s) read for the declared
flag`. `CONF_BYPASS` is non-empty, so the honest `bypass scan SKIPPED` branch is never reached. The
write-time guard at `unattended.sh:3305` keeps working — it sources — so the pair the charter asks
for on a guarded surface silently becomes one guard, and the only signal a reader gets says the scan
ran.

Nothing constrains the spelling. `check-unattended.sh`'s check 1 tests only non-emptiness after
sourcing; check 22 (`check-unattended.sh:1087`) joins `^[A-Z_]+=` key NAMES against the doc table and
never touches value syntax. The byte-compare at check 28 covers the two `declared_scalar` copies, not
this pipeline. `head -1` is a third divergence in the same line: it takes the first assignment where
sourcing takes the last.

**Why this is graded a blocker and not a high.** The kit's threat model — stated in the unit's own
security model — is a run that could supply the playbook it is measured against. `.unattended.conf`
is a working-tree file the run itself can commit. This is a one-line, gate-green way to blind the
readback half of a both-ends guard while the leg asserts it ran. **Mitigation worth stating:** no
current `.unattended.conf` or `.unattended.conf.example` puts a comment on the assignment line — all
of them sit above it — so the trigger is a legal future edit rather than today's state.

**Fix.** Read the key the way its three siblings do:

```sh
CONF_BYPASS=$( . ./.unattended.conf >/dev/null 2>&1; printf '%s' "${BYPASS_BAN:-}" )
```

If sourcing is deliberately refused here, keep the `sed` read AND compare it against the sourced
value, redding on any difference — an unarmed predicate must red, not print a population count. Either
way, arm the parse: red if the resolved `CONF_BYPASS` contains whitespace or a `#`, because no bypass
flag does. The kit already carries a correct comment-and-quote-stripping parser (`declared_scalar`)
that this line does not use.

**Left-shift gate.** Two `check-playbook.test.sh` arms — `BYPASS_BAN='--no-verify'` and
`BYPASS_BAN="--no-verify"   # comment` — each with a record carrying the flag, both asserting RED.
Beyond the instance, the class gate that would have caught it and would catch the next one: a check
that enumerates every reader of `.unattended.conf` in the kit source and refuses any that resolves a
key by a pipeline rather than by sourcing. The class name for the gotcha corpus is **"two readers of
one config, one of them re-derived"** — the same class check 28 exists to close for the parsers, one
file over.

---

## HIGH 1 — the record list is word-split, so `BYPASS_SEEN` counts records it never opened and skips the one containing the flag

**`tools/unattended/check-playbook.sh:501`.**

Filed by two lenses. `for bp_ in $(GITLS "$rr/*.md")` splits on IFS, and `git ls-files` does not quote
a space-containing path (quoting kicks in only for control characters, quotes, backslashes and
non-ASCII under `core.quotePath`). A tracked record `tools/unattended/fixture-records/tools~a b~c.md`
carrying `--no-verify` splits into `…tools~a` and `b~c.md`; neither exists, `grep -qF` exits 2 with
stderr only, the `&&` is not taken — and `BYPASS_SEEN` increments **twice**. Reproduced: with that
record the only flag-bearing one in the tree, the leg exits 0 and prints `bypass scan - 5 tracked
evidence record(s) read for the declared flag` over 4 real records.

The number that exists to prove the scan reached the corpus is inflated by exactly the record it
failed to read. That is the worst possible direction for a liveness counter, and it is why this is
graded HIGH rather than the medium and low it was filed as: the defect does to the liveness signal
what blockers 2 and 3 do, by a third route. It is not a blocker because the trigger is not reachable
by an ordinary edit — it needs whitespace in a deliverable filename.

Reachability is real, not theoretical. Pieces come from the playbook's declared grain glob
(`pieces=$(GITLS "$gr")`, line 387); `record_path_of` (`unattended.sh:3235`) folds only `/`→`~`, so a
space survives into the record path; and `record_piece`'s composite write-guard rejects a newline, the
` · ` separator and the bypass flag, but says nothing about a plain space.

**Fix.** Iterate without splitting, the shape the 28b corpora loops already use:

```sh
while IFS= read -r bp_; do … done <<EOF
$(GITLS "$rr/*.md")
EOF
```

and increment `BYPASS_SEEN` only after `[ -f "$bp_" ]` confirms the file is readable, failing 10 on a
tracked-but-absent record rather than counting it as read.

**The class is wider than this call site, and that is the finding worth keeping.** The same unquoted
expansion sits at `:138` (`record_for`), `:387`/`:391` (`for pc in $pieces`), `:471` and `:510`, and
none of them pins `core.quotePath=false` — so the kit's own explicitly supported non-ASCII piece path
(`unattended.test.sh:3031`) breaks through the adjacent quoting route. Fix the class, not the line.

**Left-shift gate.** A fixture piece whose filename contains a space, asserting that the printed
`bypass scan - N` equals the tracked record count and that the flag-bearing record still reds. Plus a
source-level scan of the kit's shell for `for … in $(GITLS` and `for … in $pieces`, which is a
zero-false-positive predicate over this tree.

---

## MEDIUM 1 — the new drift signal dates its two sides on different clocks, and the shipped pin was seeded through the skew

**`tools/drift-audit/drift_report.py:889`** (`_build_blame_dates`), **`tools/drift-audit/drift_signals.py:185`**
(the pin).

`_build_blame_dates` converts the porcelain `author-time` epoch with `timezone.utc` and never reads
the `author-tz` line that immediately follows it, while `_REVLOG_RE` takes a **hand-typed local date**
from the spec revision log. The two sides of the comparison are offset by the author's timezone.

Measured on this tree. Monkey-patching only that function to honour `author-tz` — which is what
`git blame --date=short` prints and what a human types into a revision log — drops the signal from
**31 rows to 20**: 11 rows are pure timezone artifacts, 0 new rows appear, and 7 surviving rows carry
a `line_dated` one day early. The cited instance is exact:
`memory/builds/aBoundedVerdict/README.md:91` is `author-time 1787094871`, `author-tz +0300` — 2026-08-18
23:14 UTC, 2026-08-19 02:14 local — and `git blame --date=short` prints `2026-08-19`. At node d's
+0300, any README line written between 00:00 and 03:00 local is backdated a day, so a spec revision
made the SAME day compares as `rd > d` and fires.

Nothing reds (`gateable: False`), so this is a report-quality defect — but roughly a third of the
drain list is noise, and `drift_signals.py:185` pins `readme_mechanism_drift: 31` **measured through
the skewed instrument**, with a comment telling the reader each row is one README sentence to
re-read. Fixing the clock later will read as an improvement against a pin that was never right.

**Fix.** Buffer `author-time` and apply the `author-tz` offset before formatting:
`fromtimestamp(t + tz_offset, timezone.utc).strftime('%Y-%m-%d')`. Re-measure the pin afterwards — it
lands at 20 on this corpus.

**Left-shift gate.** The selftest cannot currently observe this: `selftest.py:832` and `:898` pin
`GIT_AUTHOR_DATE` to `+0000`. Give at least one arm a non-UTC `GIT_AUTHOR_DATE` (say `+0300` at
01:00) with a spec revision on the same local day, and assert **no** row. That single arm closes the
class for every date-comparing signal this file grows later.

---

## LOW 1 — the signal emits one row per backtick OCCURRENCE, so a README line naming a token twice is counted twice

**`tools/drift-audit/drift_report.py:956`.**

Confirmed by running the signal: `value 31, rows 31, distinct (readme, mechanism) pairs 30`. The
duplicate is `memory/builds/aBoundedVerdict/README.md:283` / `--attest`, on a line that does name it
twice. `_TICK_RE.findall(ln)` yields one candidate per occurrence and nothing dedups by `(line, tok)`,
so `cand` gets two entries and `rows` gets two. `value` is `len(rows)`, so the duplicate is baked into
the shipped pin, whose comment tells the reader "each row is one README sentence to re-read" when one
of them is the same sentence twice. Every future line repeating a token inflates the count for no new
work.

**Fix.** Keep a `seen` set of `(i, tok)` inside the per-README loop and `continue` on a repeat; leave
`tok_pop` alone, since liveness only needs non-zero. Re-seed the pin from the corrected count —
together with MEDIUM 1, that is one re-measurement, not two.

**Left-shift gate.** A selftest arm whose fixture README line names one mechanism twice, asserting
exactly one row. Cheap, and it pins the invariant the pin's own comment claims.

---

## LOW 2 — `--help` still quotes the pre-unit cost, in the same file this unit edited to re-declare it

**`tools/unattended/run-unattended-gates.sh:45`.**

Lines 45–46 print `BUDGET ~60 MINUTES, measured node d 2026-08-23: the gate selftest alone is ~38
min`. Line 71 declares `BUDGET_gate_selftest=1800  # derived 1342 s after TOOL-dScriptedRepeat-15`
— about 22 minutes — with a 25-line derivation below it. Two numbers for one quantity in one file, and
the stale copy is the one an operator reads before deciding whether to launch the run. The advice
built on it ("Do NOT wrap this in a timeout under an hour") is now over-provisioned by roughly 1.5×
against the new derived sum. This is §6's "a value stated in prose beside the source that OWNS it
rots", broken inside the file that owns the value, in the commit that changed it.

**Fix.** Drop the hard numbers from the help text and point at the declarations — "budget: the sum of
the `BUDGET_*` ceilings declared below; the gate selftest dominates it" — or derive the figure at
emission time by summing the `BUDGET_*` variables for the selected `--kind`.

**Left-shift gate.** The generic form is already this repo's rule and already has a checker shape:
extend the drift-audit `handkept` family with a probe that reds when a `--help` string in a kit
script contains a minutes/seconds figure that no `BUDGET_*` declaration in the same file reproduces.
Deriving it in the script is strictly better and needs no gate at all.

---

## LOW 3 — the signal keys builds by absolute path index, so an adopter with a nested `MEMORY_ROOT` gets cross-build false positives

**`tools/drift-audit/drift_report.py:912`** (and `:918`).

`path.split("/")[2]` assumes `ctx.memory_root` is exactly one path segment. `Ctx.__init__` (line 1001)
sets `self.memory_root = conf.get("MEMORY_ROOT", "memory").strip("/")` with no such constraint, and
these two lines are the only index-based path splits in the file — every sibling signal addresses the
tree by glob and is depth-agnostic. At `MEMORY_ROOT=docs/memory`, index 2 is the literal `builds` for
every README and every spec, `specs_by_build` collapses to one key, and each README is graded against
every build's revision log — extra rows whose `build` field reads `builds`.

Not hypothetical for a copy-in kit: `memory/guides/SESSION-KICKOFF.md:228` records `MEMORY_ROOT="docs/mem"`
as a real adopter value. Low is right — the signal is report-only, so the cost is false-positive rows
in an adopter's report, never a wrong merge verdict, and this repo's own layout can never surface it.

**Fix.** Derive the slug relative to the root:
`PurePosixPath(rel).relative_to(f"{ctx.memory_root}/builds").parts[0]`.

**Left-shift gate.** A selftest arm that builds its fixture under a two-segment `MEMORY_ROOT`. One
arm covers this defect and every future signal that reaches for an index — which is the reason to add
it even though the fix here is one line.

---

## LOW 4 — a blind `git blame` reports a reassuring zero as `ok`, because `live` does not watch the blame stage

**`tools/drift-audit/drift_report.py:876`.**

`Git.run` (line 228) is a plain `subprocess.run` that never raises, and `_build_blame_dates` reads
only `.stdout`. Any blame failure yields `{}`, every candidate hits `if d is None: continue`, and the
build contributes zero rows. `live` (line 979) is `bool(tok_pop and rev_pop)`, both accumulated
**before** the blame call at 959, so the row prints `ok` rather than DEAD PROBE. That is the shape
this file's own header and §7 refuse, and it is weaker than the sibling at line 804, which explicitly
marks a shard "tracked but not on disk" and drops it from judgeable.

**Reachability is narrower than it first looks, and the correction is worth recording.** The
`ls-files`-quoting route does NOT reach blame: `_read` fails on the quoted path first, `cand` stays
empty and the loop `continue`s — same for a tracked README deleted from the worktree. Two adjacent
theories are closed: `-L 1,<past EOF>` clamps at rc 0, and `git -C root` makes cwd irrelevant. The
route that does reproduce is an unborn HEAD: `git blame --porcelain -L 1,2 -- f.md` on a
staged-but-never-committed file exits 128 with empty stdout.

**Fix.** Count the READMEs that reached the blame stage and got no dates back, and fold it into
liveness — `live = bool(tok_pop and rev_pop and blamed_ok)` — or surface a `blame_failed` count so the
row is not silently indistinguishable from a clean one.

**Left-shift gate.** A selftest arm run against a repo with no commits, asserting the signal reports
DEAD PROBE rather than `ok`. The generalisation, which is the item worth carrying: **every signal
whose `live` field is computed before its most expensive stage is lying about that stage.** A
structural check over `drift_report.py` that reds when a `live` expression references only names
bound above the signal's last subprocess call would catch the class.

---

## The refuted one

One finding did not survive the skeptic. It is not restated here because nothing in it was salvaged;
precision for the round is 16/17 = 0.94, which is above the §8 tightening threshold and does not call
for a scope change.

---

## Left-shift summary — what should exist before round 8

Ranked by what they would have caught, not by cost.

1. **A `_pbatch` misalignment arm** (blocker 1) — a parser patched to answer multi-line for
   multi-line input only, asserting the leg REDS. Class: a degraded-mode fallback must never
   fabricate a value an assertion reads as clean.
2. **A `grain = ""` playbook arm** (blocker 2) and, above it, a class check that every `$rr`-derived
   check is reachable without `$gr`.
3. **Two conf-spelling arms** (blocker 3) and, above them, a source check refusing any reader of
   `.unattended.conf` that resolves a key by pipeline instead of by sourcing. Class name for the
   gotcha corpus: *two readers of one config, one of them re-derived*.
4. **A spaced-filename fixture piece** (high 1) plus a source scan for `for … in $(GITLS` across the
   kit. Class: a liveness counter must count what was OPENED, never what was enumerated.
5. **A non-UTC `GIT_AUTHOR_DATE` selftest arm** (medium 1) — closes the class for every
   date-comparing signal this file grows later.
6. **A nested-`MEMORY_ROOT` selftest arm** (low 3) and an **unborn-HEAD arm** (low 4).

Three of the four defects in the unattended kit are one class: a guard whose liveness assertion
counts something other than whether the guard could fire. That is the gotcha worth writing down this
round, and it is worth writing down as a *predicate on liveness assertions* rather than as three
separate arms — a liveness number that would be unchanged by the guard being disarmed is not a
liveness number.
