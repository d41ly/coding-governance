## Verdict: BLOCKED

**Reviewed range:** `5498254bac558344140fa206e6c8e450f9efbe66...HEAD` — the cumulative diff landing on
main (`06015fa` unit 2 built · `8a5fd19` unit 1 built · `446f7f5` the four-legs fix-up, plus the
merge and reconcile commits `00fd177`/`9f919e2` already in the range's base).

**Serves:** diff-review TOOL-aLoosenedCeiling-1 TOOL-aLoosenedCeiling-2 TOOL-aLoosenedCeiling-3

**Review shape:** raw 18 · confirmed 12 · refuted 6 · unverified 0 · precision **0.67**.

The 12 confirmed findings collapse to **7 distinct defects** — four of them were reported by more
than one lens (the zero-byte-cap guard three times, the `isdigit`/`int()` gap twice, the drift-audit
pin twice, the stale conf comment twice). Duplicates are folded below and their source ids named, so
the count in the shape line and the count of sections do not have to match. Two of the seven are
**blockers that are red on the merge bar right now** — both re-run and reproduced at HEAD while
writing this report, not inferred from the diff.

**The bar at HEAD:** three legs red — `verdict epoch`, `verdict-epoch self-test` (its live-tree arm),
and `drift-audit records`. `.githooks/pre-push` runs the full bar with `GATE_FULL=1` on a
default-branch push, so this range cannot land as it stands.

---

## BLOCKER 1 — the kit-version bump is older than the change it dates

**`tools/memory-tree/check-memory-hygiene.sh:13`** *(reported as id 3)*

`KIT_MEMORY_TREE_VERSION` was bumped to `2.20` in `8a5fd19`, but the later fix commit `446f7f5`
moved 10 non-comment lines of the delegate `tools/memory-tree/corpus_ids.py` (the
`_conf_int` → `_parse_conf_int` rename) with no further bump. The rule is topological — the bump
must be ancestor-or-equal to the last behaviour-bearing engine change — so an earlier bump does not
excuse a later change.

Reproduced at HEAD:

```
verdict-epoch: FAILED — the bump is OLDER than the change it claims to date.
verdict-epoch:   last behaviour-bearing engine change: 446f7f5 (10 line(s))
verdict-epoch:   moved: tools/memory-tree/corpus_ids.py
verdict-epoch:   last KIT_MEMORY_TREE_VERSION change:  8a5fd19
```

**Impact.** Two legs red: `verdict epoch` and the verdict-epoch self-test's live-tree arm. Beyond the
red, `hygiene-parity.test.sh` derives its baseline floor from that constant, so the floor points
*before* the `corpus_ids.py` change — the parity comparison is against a stale baseline.

**Fix.** Bump to `2.21` in all three carriers together, in a commit at or after `446f7f5`:
`tools/memory-tree/check-memory-hygiene.sh:13` (the constant **and** the `gov:kit` marker on that
same line), `tools/memory-tree/HYGIENE.template.md:1`, `memory/HYGIENE.md:1` — then
`bash tools/memory-tree/kit-dogfood-parity.test.sh --render`.

**Left-shift.** The gate already exists and already prints the exact remedy; what failed is that it
ran at the push boundary rather than at the commit that broke it. `check-verdict-epoch.sh` is cheap
(git-only, no corpus walk) and its guard scopes it to the kit dir — add it to `.githooks/pre-commit`'s
fast leg set so a delegate edit without a bump reds at the commit that introduces it, when the fix is
one line in the same commit rather than a fourth commit on top.

---

## BLOCKER 2 — product source cites two specs whose status is still OPEN

**`memory/builds/aLoosenedCeiling/spec/2026-08-18-spec-TOOL-aLoosenedCeiling-1.md:3`**
*(reported as ids 10 and 4)*

Units 1 and 2 shipped their product code inside this range (`8a5fd19`, `06015fa`) and the source now
cites both ids — `tools/memory-tree/corpus_ids.py:51` cites `TOOL-aLoosenedCeiling-1`,
`tools/memory-tree/check-memory-hygiene.test.sh:1016` cites `TOOL-aLoosenedCeiling-2` — while both
spec status headers still read `OPEN`. The record says the work is unstarted; the tree says it
landed.

Reproduced at HEAD (`python tools/drift-audit/drift_report.py --check`, exit 1):

```
non_terminal_specs_cited_by_product_source = 4 (pin 2) — this list is shrink-only
  ... aBatchedLintel-1 (INPROGRESS)   <- pre-existing pin
  ... aGuardedTally-1  (INPROGRESS)   <- pre-existing pin
  ... TOOL-aLoosenedCeiling-1 (OPEN, cited in tools/memory-tree/corpus_ids.py)
  ... TOOL-aLoosenedCeiling-2 (OPEN, cited in tools/memory-tree/check-memory-hygiene.test.sh)
```

**Impact.** The `drift-audit records` leg in `tools/gate-legs.json` carries **no `guard` field**, so it
runs even on a diff-scoped run — this is red on every run, not only at the push boundary. The pin is
shrink-only, so raising it is not an available escape. `446f7f5`'s commit message acknowledges the
breakage and defers it; nothing in the range closes it.

**Fix.** Flip both spec status headers to their terminal value in the same commit that lands the
code, update the matching rows in `memory/builds/aLoosenedCeiling/README.md`, re-render
`memory/LIVE.md` (`gen_build_index.py --write`), and re-run the leg — it returns to the pin of 2.
Do **not** move the pin.

**Left-shift.** This is the same shape as blocker 1: a status header that should have moved in the
commit that moved the code. The signal is already gateable and already runs on every diff — what is
missing is that it runs *after* the commit. Two cheap options, either sufficient: (a) add the
drift-audit records leg to the pre-commit fast set, or (b) since `446f7f5`'s own message names this
defect and ships anyway, make the deferral impossible to spell — a commit whose message names a
gateable signal it leaves over-pin is the thing to catch, and the pre-commit already parses the
message for the branch guard.

---

## MEDIUM 3 — rule 6's prose says TWO classes while enumerating three

**`memory/HYGIENE.md:130`** (and the byte-identical `tools/memory-tree/HYGIENE.template.md:130`)
*(reported as id 5)*

The rewritten bullet still opens with "TWO classes" and closes with "`curation-debt.txt` exempts
either" while enumerating three cap families — `INDEX_CAP_*`, `GUIDE_CAP_*`, `BUILD_README_CAP_*`.
The engine has had three tiers since `TOOL-aRuledFrontispiece-5` (`check-memory-hygiene.sh` awk block
~L418–435: `icb/icl`, `gcb/gcl`, `rcb/rcl`, with the inline comment "A build README: its own tier"),
and `06015fa`'s own commit message says "a check that has three classes".

Separately, the inserted abort sentence detached the trailing `(grandfather: curation-debt.txt …)`
parenthetical from the caps sentence it used to close. It now dangles off the *refusal* sentence, so
it reads as if `curation-debt.txt` could exempt an unusable cap declaration — it cannot;
curation-debt only skips a FILE (`in_debt "$f" && continue`).

**Impact.** The shipped rule document contradicts itself and the engine, in the document an adopter
receives. This is this repo's own `two-answers-to-one-question` gotcha class, and kit/dogfood parity
keeps both halves *equally* wrong, so no gate can see it.

**Fix.** "TWO classes" → "THREE classes"; "exempts either" → "exempts any of them"; move the
`(grandfather: …)` parenthetical back onto the cap sentence, ahead of the new abort sentence. Apply
the identical edit to `tools/memory-tree/HYGIENE.template.md:130`/`:137` so parity stays green.

**Left-shift.** Parity between kit and dogfood is checked; agreement between the doc and the *engine*
is not, and parity actively hides this class by keeping two copies of one wrong sentence. Cheapest
real gate: extend `check-playbook-parity.sh`'s declared-pairs mechanism (a value the doc STATES
equals the source that OWNS it) with one pair for rule 6 — extract the cap-family prefixes the awk
block binds (`INDEX_CAP_`, `GUIDE_CAP_`, `BUILD_README_CAP_`) and assert the count against the
number-word in `HYGIENE.md:130`. Anti-vacuity applies: a pair whose extraction matches nothing must
red, not compare empty to empty.

---

## MEDIUM 4 — the six new cap keys never reached the shipped conf catalogue

**`tools/memory-tree/.memory-tree.conf.example:63`** *(reported as id 11)*

The engine now reads all six check-6 cap keys from `.memory-tree.conf`
(`check-memory-hygiene.sh:33-35` defaults, sourced conf at `:36`, validation loop at `:43`, awk
bindings at `:418-420`), and its own comment says the point is that an adopter should not have to
fork a kit script. But the six names appear only in the engine, its test, the spec's design table and
the HYGIENE prose — never in `tools/memory-tree/.memory-tree.conf.example`, and never in this repo's
own `.memory-tree.conf`. Only `READ_PATH_HEADROOM` was added.

Meanwhile `memory/HYGIENE.md:66-67` and `tools/memory-tree/HYGIENE.template.md:66-67` both state
"every cap is declared in `.memory-tree.conf` (`INDEX_CAP_*`, `GUIDE_CAP_*`, `BUILD_README_CAP_*`)",
and `adopt-memory-tree.sh:40` copies that example verbatim into the adopter's root as their conf.

**Impact.** A freshly scaffolded tree ships a committed rule document pointing at conf keys that are
not in the conf. The adopter greps, finds nothing, and either concludes the install is broken or
forks the kit script — which is exactly what the engine comment says the change exists to prevent.
Same class as the OPEN row `memory/backlog/TOOL.md:70` (`TOOL-cSettledDocket-14`). The build's own
spec required it: `spec-TOOL-aLoosenedCeiling-2.md:44` (S7) and its files-touched line 141 name
`.memory-tree.conf.example` as carrying "six declarations and their comment". **No acceptance
criterion covered S7, which is why it slipped.**

**Fix.** Either add the six keys to `.memory-tree.conf.example` with their shipped values (NOT blank
— a blank value trips the validation abort) plus the one-paragraph comment S7 asks for; or, if they
are meant to stay engine-side defaults, reword `HYGIENE.template.md:66-67` and `memory/HYGIENE.md:66-67`
from "every cap is declared in `.memory-tree.conf`" to "overridable in `.memory-tree.conf`; the
shipped defaults live at the top of `check-memory-hygiene.sh`".

**Left-shift.** Two independent gaps, both worth closing. (a) The conf catalogue is unchecked: add a
leg asserting that every `${NAME:-default}` conf read in `check-memory-hygiene.sh` has a row in
`.memory-tree.conf.example` — a one-pass grep on both sides, and it drains in the deletion direction
too (an example row for a key the engine stopped reading). (b) A spec step with no acceptance
criterion is the process defect underneath: check 12 already grades acceptance bullets for backticked
witnesses, so extend it to assert every `S<n>` in the design section is named by at least one
acceptance bullet.

---

## MEDIUM 5 — the ceiling conf comment says the engine that reads it has not landed

**`.memory-tree.conf:102`** *(reported as ids 14 and 8)*

Lines 102-103 read "The engine that READS that declaration is TOOL-aLoosenedCeiling-1; until that
unit lands, `--measure` still uses its own built-in 20,480 and the declaration below is inert", and
lines 116-117 repeat "which is 20,480 B until it lands". That unit landed inside this same range at
`8a5fd19`, which touched no conf file, so the comment was never revised. At HEAD
`corpus_ids.py:53` sets `DEFAULT_READ_PATH_HEADROOM = 25600`, `:83` registers `READ_PATH_HEADROOM` as
a conf key, and `_measure_lines` (`:495`) reads it — proved by the new selftest arms and by running
it: `--measure` prints `READ_PATH_CEILING="112987"   # measured 87387 B + 25600 B headroom`.

**Impact.** The one file an operator opens to change the ceiling tells them the key beneath it does
nothing. The comment justifies itself as protection against a reader believing the tree is configured
when it is not; it now produces the exact inverse error, against its own warning that "a declaration
nothing reads is worse than an absent one". It is the only authored record of the headroom policy,
so the seventh ceiling movement will read it.

**Fix.** Rewrite lines 102-103 and 116-117 in landed tense: `READ_PATH_HEADROOM` is read by
`corpus_ids.py --measure` as of `TOOL-aLoosenedCeiling-1`, and the kit's shipped default is 25,600 B.
Drop both "until it lands" clauses.

**Left-shift.** A comment naming a spec id and a state ("until X lands") is a record→reality claim
that no gate reads. `drift_report.py` already owns this question — add a signal that scans tracked
conf and doc comments for a spec id paired with a not-yet-landed phrase, and reds when that id's spec
has reached a terminal status. Narrow, mechanical, and it drains: the phrase disappears with the fix.

---

## LOW 6 — the zero-byte-cap guard matches only the literal `0`

**`tools/memory-tree/check-memory-hygiene.sh:47`** *(reported three times — ids 2, 6 and 17)*

The validation block at `:44-50` has two arms, `*[!0-9]*|""` and the literal `0`. `INDEX_CAP_BYTES=00`
(also `000`, `020`) matches neither, so it is **accepted**; awk's `icb+0` belt then coerces it to 0
rather than rejecting it.

Reproduced in a scratch repo: with `INDEX_CAP_BYTES=00` the exit-2 abort never fires and the gate
prints `HYGIENE check 6 FAILED … memory/README.md (2B 1L > 0B/250L)`, reding every file in the class.
That is precisely the outcome the block's own header comment (`:30-31`) says it prevents — "a gate
that reds everything or nothing with no message" — and because it is a check FAILURE rather than the
abort, a run under a typo'd conf reports findings *about the tree* instead of refusing to run.

The Python twin `corpus_ids.py:_parse_conf_int` rejects `"00"` (isdigit passes, then
`int(raw) < minimum`), so the two validators for one rule disagree.

**Fix.** Make the zero test arithmetic rather than textual, in the digits-only branch:

```sh
case "$_k" in *_BYTES) [ "$_v" -eq 0 ] && _capbad="$_capbad $_k='$_v' (a zero byte cap reds every file in its class)" ;; esac
```

Do **not** use `$((_v))` — bash treats `08`/`09` as an invalid octal constant.

**Left-shift.** The suite exercises only the single-character `0`
(`check-memory-hygiene.test.sh:1100`), which is why the hole is unarmed. Add `INDEX_CAP_BYTES=00` to
the `_bad` loop there. Structurally: this is a guard whose arm tests one *spelling* of a value rather
than the value — worth a line in the gotcha classes (`gotchas.py`) so a review of any future
conf-validation diff is prompted to ask whether the arm covers alternate spellings.

---

## LOW 7 — `_parse_conf_int` gates on `isdigit()`, then calls `int()` on what it admitted

**`tools/memory-tree/corpus_ids.py:115`** *(reported twice — ids 1 and 7)*

`if not raw.isdigit() or int(raw) < minimum:` — the short-circuit still evaluates `int(raw)` whenever
`isdigit()` is true, and `isdigit()` is true for values `int()` rejects: non-decimal Unicode digits
(U+00B2 SUPERSCRIPT TWO and friends), as is any decimal over 4300 digits. Verified: `'²'.isdigit()`
is `True`; `int('²')` raises `ValueError`.

**Impact.** `main()` (`:858`) catches only `Problem`, so a conf value like `READ_PATH_CEILING="10²"`
escapes as a raw interpreter traceback: checks 14/15/16 and `--measure` die with exit 1 and no
`HYGIENE ` line for a consumer to parse — indistinguishable in status from a real hygiene regression.
That is exactly the contract this accessor's docstring ("never a raw ValueError traceback") and
`class Problem` ("Never a traceback") promise, and exactly the class `8a5fd19`'s commit message says
the accessor was written to drain. It now guards four keys (`READ_PATH_CEILING`,
`READ_PATH_HEADROOM`, `DEAD_PATH_PIN`, `ORPHAN_ID_PIN`) across four call sites (`:408`, `:441`,
`:451`, `:495`), where it replaced three bare `int()` calls — so the blast radius grew.

Honestly low: it needs an exotic conf typo. ASCII typos and Arabic-Indic digits are already handled
correctly.

**Fix.** One word — `raw.isdecimal()` on line 115, which also matches the docstring's "decimal
integer" wording. `row_grammar.pin_of:198` carries the identical pattern and takes the same one-line
change.

**Left-shift.** Add a selftest arm beside the existing `c7i` one using `READ_PATH_HEADROOM = "10²"`
and asserting the same "must be a whole number of at least" text — that arm fails today and passes
after the fix. Repo-wide: `isdigit()` guarding an `int()` is a two-site pattern here already, so a
grep-level ban (the same shape as the retired `command -v python3 || python` idiom) is proportionate
if a third site ever appears; two sites do not yet earn a gate.

---

## What was NOT checked

The six refuted findings are not reproduced here. Nothing in this pass re-derived the ceiling
arithmetic itself (`--measure`'s 87387 B + 25600 B), re-ran the full 21-check hygiene sweep against a
mutated corpus, or exercised the adopter e2e for the memory-tree kit — the conf-catalogue gap in
MEDIUM 4 was established by reading `adopt-memory-tree.sh:40` and grepping both trees, not by running
an install. Findings 3 and 2/10 were each re-run live at HEAD while writing this report; the rest are
read-verified against source in this worktree.
