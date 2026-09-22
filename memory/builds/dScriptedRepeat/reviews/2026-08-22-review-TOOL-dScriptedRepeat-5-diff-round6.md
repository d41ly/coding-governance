**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 6 (the fold of round 5's ten)

**Range:** `22cbb7a3...0b5d5224` — one commit, `0b5d5224` (round 5's blocker and all nine, and the
three gates rewritten from instance gates into class gates). 11 files, 915 insertions, 89 deletions;
the code half is `check-playbook.sh`, `check-unattended.sh`, `unattended.sh` and two test suites.
**ROUND 6.**

**Review shape:** raw 29 · confirmed 29 · refuted 0 · unverified 0 · precision 1.00. The 29 confirmed
findings collapse to **10 distinct defects**; six clusters were found independently by two to four
lenses each, and that corroboration is recorded per defect rather than counted twice. Every mechanism
below was re-reproduced against the working tree by the synthesis pass before it was written down,
and the reproductions are quoted where they are the evidence.

The full bar is 92/92 green over this diff. It is green over every defect below.

## Verdict: BLOCKED

Two blockers, one high, four mediums, three lows.

**No lens filed a blocker.** Both blocker designations are mine, and the rule I applied is stated so
you can disagree with it: a finding is a blocker when it makes the fold's own load-bearing claim
false, or when it breaks the product for a legitimate user. BLOCKER 1 is the first; BLOCKER 2 is the
second. Everything else is graded as its strongest surviving filing, except where I say otherwise and
why.

**The standing pattern held for a SIXTH round, and this time it held inside the repair itself.**
Rounds 1–5 each broke on the previous round's blocker restored by the commit that fixed it, one level
up: no join, the wrong parser, `head -1` at the call sites, the terminator test on the raw line, then
the key strip eating the whitespace the comment strip needed. Round 5's own finding was that the
three structural gates round 4 added were INSTANCE gates. This fold rewrote all three over a derived
kit-source population — the right move, and it worked for one of them. Of the other two:

- **28b** now demands a positive parser binding for every template key, with an exemption for the one
  key that has no parser read. The exemption is iterated by an unquoted `for` over a string
  containing spaces, so its "the reader signature must still be present" literal truncates at the
  first space to the four-byte word `grep`, which appears 19 times in the file it names. The escape
  hatch of the fix is exactly as vacuous as the thing it replaced (**BLOCKER 1**).
- **28a** now tests the discard spellings first instead of whitelisting every line containing `||`.
  It enumerates three of them. `|| return 0` and `|| _x=""` — the two that actually produce the
  round-3/4 blocker — are not among them and still grade compliant (**HIGH 1**).

And the parser repair itself introduced a refusal of legal input. The positional closer test round 5
asked for is correct; it was placed before the whitespace and `\r` trims instead of after them, so a
closed single-line array with one trailing space is refused at rc 2 under a message saying it is
unterminated (**BLOCKER 2**).

**The shape underneath all of it, stated once.** Seven of these ten defects are one of two mistakes:
a classifier that tests CONTAINMENT over a whole line when the question is about one token
(`*'||'*`, `*'GIT '*`, and the comment strip's `[[:space:]]#`), or a structured record iterated with
an unquoted expansion so that only its first field survives (`KEY_EXEMPT`). Neither is a spelling
problem and neither is fixed by adding a spelling. The left-shift section at the end proposes the two
gotcha classes that would name them.

---

## BLOCKER 1 — 28b's key exemption is destroyed by word-splitting, so the freshness half of the rule cannot fail

**`tools/unattended/check-unattended.sh:1510`** (the value) and **`:1540`** (the unquoted iteration).
Found independently by four lenses; all four filed it HIGH.

`KEY_EXEMPT` holds one `key|file|literal` record whose third field contains spaces. Line 1540 is
`for _e in $KEY_EXEMPT`, unquoted, so the shell splits the record into three words before the
`case "$_e" in "$_k|"*` ever runs. Reproduced verbatim:

```
TOK1=[legs|check-playbook.sh|grep]
TOK2=[-oE]
TOK3=["(^[[:space:]]*|[{,][[:space:]]*)\"?$g\"?]
_exf=[check-playbook.sh] _exlit=[grep]
$ grep -cF -- "grep" tools/unattended/check-playbook.sh
19
```

So line 1549's `grep -qF -- "$_exlit" "$HERE/$_exf"` asks whether the string `grep` appears in
`check-playbook.sh`. It does, 19 times, and it will for any content that file ever holds. The
assertion has no failing input.

The preconditions are live, not theoretical, and I measured every one of them:

- `legs` IS one of the ten keys the shipped `PLAYBOOK-TEMPLATE.template.md` declares.
- It is the ONE key with zero `declared_(list|scalar) .* legs)` reads — 0 in all five non-test kit
  scripts — so the exemption branch is the only thing standing between it and 28b's refusal.
- The negative half does not cover it either: `grep -nE "\^legs([^A-Za-z_]|$)"` finds 0 hits in all
  five scripts.
- Its real reader is the bespoke `grep -oE "(^[[:space:]]*|[{,][[:space:]]*)\"?$g\"?…"` at
  **`check-playbook.sh:296`** — the pipeline check 6 resolves every `GATE <leg>` tag through.

Rewrite or delete that reader and `legs` is then read by no parser AND unaccounted for by its
exemption, and check 28 stays green. Two lenses demonstrated it end to end: one swapped the
`grep -oE` reader for an `awk` one-liner and got `bash tools/unattended/check-unattended.sh` at RC=0;
another replaced the whole reader with `ent=NOTAREADERANYMORE` and got RC=0 with no output. That is
verbatim the widening the comment at 1507–1509 says the literal exists to prevent.

The self-test cannot see it. The staged break at **`check-unattended.test.sh:1623`** sets
`KEY_EXEMPT="legs|check-playbook.sh|THIS_LITERAL_IS_GONE"` — a whitespace-free synthetic that splits
into one word, so the arm exercises a mechanism the shipped value does not have and passes for the
wrong reason. `fixture-passes-by-finding-nothing`, one level in: the fixture fires, over a value
whose shape is not the shipped one.

Secondary, same line: the unquoted expansion is also subject to pathname expansion. TOK3 contains
`*`, `?` and `[...]`, so the loop's behaviour depends on what happens to sit in the working directory.

**Fix.** Hold the table newline-separated and iterate it without splitting:

```sh
KEY_EXEMPT=$(printf '%s\n' 'legs|check-playbook.sh|grep -oE "(^[[:space:]]*|[{,][[:space:]]*)\"?$g\"?')
while IFS= read -r _e; do
  case "$_e" in "$_k|"*) _ex=$_e ;; esac
done <<EXEOF
$KEY_EXEMPT
EXEOF
```

I verified the payoff is real rather than notional: `grep -cF` of the FULL literal against
`check-playbook.sh` returns **1**, so once the record survives intact the exemption binds to exactly
one line and a rewrite of that line reds it.

**Left-shift gate.** Two arms, both inside 28b itself, so this cannot regress into the next fold:
(1) assert every parsed `_exlit` is longer than a floor (≈20 bytes) and matches **exactly one** line
of the file it names — a signature that degenerates into a common word then reds instead of
resolving, which is the property the exemption was written to have; (2) re-arm the stale-exemption
test by mutating the REAL reader
(`sed 's|^    ent=$(printf.*|    ent=NOTAREADERANYMORE|' check-playbook.sh`) rather than by
substituting `KEY_EXEMPT`, and add a positive control asserting the shipped exemption resolves
against the shipped reader and NOT against an arbitrary file that merely contains `grep`.

---

## BLOCKER 2 — the positional closer runs before the trims, so a legal array with trailing whitespace is refused at rc 2

**`tools/unattended/unattended.sh:2418`** and its byte-identical copy
**`tools/unattended/check-playbook.sh:187`**. Found independently by four lenses; filed HIGH once and
MEDIUM three times. I take the HIGH grading and promote it, because this is the only defect in the
set that breaks the product for a legitimate adopter, and this diff created it.

Round 5's MEDIUM 5 correctly asked for a positional terminator test in place of the containment test
`*'['*']'*` that admitted `k = ["a[0]",`. The replacement is right; its placement is not.
`case "$raw" in *']') ;; *'['*) return 2 ;; esac` runs **before** the `tr -d '\r'` and the
trailing-space trim two lines below it, so the case sees whatever the comment strip left. Measured on
the shipped body:

```
list rc=0 [a b]   <<< [outputs = ["a", "b"]]
list rc=2 []      <<< [outputs = ["a", "b"] ]      # one trailing space
list rc=2 []      <<< [outputs = ["a", "b"]<TAB>]
list rc=2 []      <<< [outputs = []  ]
```

Only a line carrying a trailing COMMENT survives, because the comment strip eats to end of line —
which is why the shipped template masks it completely (every declaration line in its toml fence
carries a trailing `#` comment) and why the 92/92 bar never presents a bare closer.

The consequences are fail-closed but wrong-cause, in the authorization path:

- **`unattended.sh:951`** turns rc 2 into `fail 46 "the playbook at the pinned BASE opens an
  output-glob list it does not close on the same line"` and returns 1 — refusing the entire
  recipe-mode run and pointing the author at a `]` that is plainly on the line.
- **`unattended.sh:2165`** returns `set-checks-recorded` not-met for the same false reason.
- **`check-playbook.sh:342`** reds check 8 and suppresses the census line, so `pieces-complete`
  reports a missing count.

An adopter who fills in `outputs = ["content/**"]` and deletes the template's prose comment is one
trailing space from all three. The playbook is a **markdown** file, where two trailing spaces are the
hard-line-break convention and trailing whitespace is invisible in every editor that does not paint
it. One lens confirmed end to end: appending one space to `playbook.fixture.md`'s legal
`piece_checks  = ["fixture-shape"]` makes `check-playbook.sh` exit 1 with the wrong-cause message.

The CR half is a platform split I could not reproduce on this box and am reporting as unconfirmed
rather than dropping: `GIT()` at **`lib-unattended.sh:20`** does no `tr -d '\r'` (unlike
`check-playbook.sh:121`'s `GITSHOW`), and the driver hands the raw blob to the parser at
`unattended.sh:938` and `:2147`, so a CRLF-committed playbook reaches the case with the `\r` intact.
MSYS grep strips CR in text mode, which is why every reproduction attempt here returned rc 0; GNU
grep on a Linux runner does not. If that reading is right, a playbook authorizes on Windows and reds
on CI. This repo's own memory carries `worktree-crlf-beyond-the-pinned-set`, so the mechanism is not
exotic here.

**Fix.** Trim before the test, in both copies byte-identically so check 28's compare stays green:

```sh
raw=$(printf '%s\n' "$1" | grep -m1 -E "^$2[[:space:]]*=" \
      | sed 's/[[:space:]][[:space:]]*#.*$//' \
      | sed "s/^$2[[:space:]]*=[[:space:]]*//" \
      | tr -d '\r' | sed 's/[[:space:]]*$//')
```

Keep the `*']')` / `*'['*) return 2` case exactly as written; it is correct once it sees the value's
real last character.

**Left-shift gate.** The specimen loop at `check-unattended.sh:1653` has five MUST-PARSE specimens and
five MUST-REFUSE ones, and not one of the MUST-PARSE specimens carries trailing whitespace — the
accept direction is unarmed for exactly the byte this defect turns on. Add `'Xk = ["a", "b"] X|Xa bX'`,
a tab-terminated variant, and a CR-bearing body to that loop, and the same to the scalar loop at
`:1665`. That converts "the parser refuses what it should" into "…and accepts what it should", which
is the half the fold's five new refusal specimens do not cover.

---

## HIGH 1 — 28a's discard case enumerates three spellings, and the two that produce the round-3/4 blocker are not among them

**`tools/unattended/check-unattended.sh:1489`**. Found by three lenses (one HIGH, two MEDIUM).

The rewritten case is:

```sh
*'||'*true*|*'||'*' :'*|*'||'*':;'*) ;;                # discard -> fail
*'if !'*|*'while !'*|*'until !'*|*'||'*) continue ;;   # compliant
```

The second arm still ends in a bare `*'||'*`, so the rule is "any line containing `||` is compliant
unless it also contains one of three literals". Ran the shipped arms over candidate spellings:

```
DISCARD-FAIL   _x=$(declared_list "$b" set_checks) || true
COMPLIANT      _x=$(declared_list "$b" set_checks) || return 0
COMPLIANT      _x=$(declared_list "$b" set_checks) || _x=""
COMPLIANT      _x=$(declared_list "$b" k) ||:
COMPLIANT      _x=$(declared_list "$b" k); [ -n "$_x" ] || DOD_OUT="none declared"
COMPLIANT      if ! _x=$(declared_list "$b" k); then
DISCARD-FAIL   _x=$(declared_list "$b" k) || { fail 3 "gave no true answer"; return 1; }
```

Two things in that table matter. The `|| _x=""` and `|| return 0` rows are round 3/4's blocker
restored: at the real call site **`unattended.sh:2165`**, one lens rewrote
`_declared=$(declared_list "$_blob" set_checks) || _declared=""` and the leg stayed RC=0 — the rc-2
refusal becomes the declared null, the `case` at **`unattended.sh:2172`** matches it as `''`, and
`set-checks-recorded` grades MET with no record, no verdict and no override entry. `|| return 0`
likewise, RC=0. The control `|| true` reds correctly, which is round 5's fix working on the one
spelling it was written for.

The last row is the other direction and is just as real: an honest caller spelling
`|| { fail 3 "…gave no true answer…"; return 1; }` matches `*'||'*true*` and would RED. This kit's
fail messages are long prose, so the substring is a live hazard, not a contrived one.

`||:` slips because `*'||'*' :'*` needs a space and `*'||'*':;'*` needs a `;`; it parses fine in bash
and is an ordinary discard idiom.

Today's four real call sites all spell `if ! x=$(…)` and grade correctly, so this is a latent gate
weakness rather than a live discard — which is exactly what it was last round, before the fold
restored the defect at a call site.

**Fix.** Stop enumerating discards and enumerate the COMPLIANT set instead, and strip to the
invocation before matching. Split the line at the closing `)` of the `$(declared_* …)` substitution,
then grade the remainder's leading token: accept `if !` / `while !` / `until !` prefixes, and a `||`
whose right-hand side provably refuses (`return [1-9]`, `exit [1-9]`, `fail `, a brace group
containing one of those); fail everything else, `|| return 0` and `|| <assignment>` included. That
inverts the default from "anything with `||` passes" to "only a proven refusal passes", which is the
only direction a new spelling cannot widen.

**Left-shift gate.** Add two staged-break arms to `check-unattended.test.sh`: one rewriting
`unattended.sh:2165` to `_declared=$(declared_list "$_blob" set_checks) || _declared=""` and one to
`|| return 0`, both asserting check 28 reds. Keep the existing honest-caller arm green, and add a
false-positive control whose refusal branch contains the word `true` in its prose.

---

## MEDIUM 1 — both parsers still return the comment TEXT at rc 0 when the `#` is not preceded by whitespace

**`tools/unattended/check-playbook.sh:178`** / **`:209`** and the byte-identical copies at
**`tools/unattended/unattended.sh:2410`** / **`:2441`**. Found by three lenses (two MEDIUM, one LOW).

This is round 5's blocker with one space deleted. The comment strip is
`sed 's/[[:space:]][[:space:]]*#.*$//'`, which requires whitespace before the `#`; `=#` has none, so
the comment survives the whole-line strip and the key strip hands it back as the value. Measured on
the shipped bodies:

```
list rc=0 [# globs. Where pieces land]   <<< [outputs =# globs. Where pieces land]
scal rc=0 [# who ratified]               <<< [curated =# who ratified]
scal rc=0 [# who ratified]               <<< [curated=# who ratified]
scal rc=0 []                             <<< [curated = # who ratified]   <- round 5's spelling, fixed
```

Both consumers are the two the round-5 blocker named, and both still pass on a non-empty comment
string: **`unattended.sh:962`**'s `case "$AUTH_OUTPUTS" in '')` is the ONLY guard on that value, so a
recipe-mode run declaring no output globs is authorized; **`check-playbook.sh:235`**'s `[ -n "$cur" ]`
passes the fork-4 freeze on an unratified playbook. `step_floor` is incidentally safe, protected by
its own `*[!0-9]*` guard.

**I did not promote this to blocker, and the argument for promoting it is real.** The consequences are
identical to round 5's blocker and land on `DOD_NO_OVERRIDE` items. What holds it at medium is
reachability: `key =#c` is not idiomatic TOML and no shipped template line spells it. Three lenses
graded it medium and low independently; I am recording the tension rather than resolving it by fiat.

**Fix.** A `#` can only be a member character INSIDE a quoted string, never at position 0 of a TOML
value, so emptying it is exact rather than heuristic. After the key strip in both copies:
`case "$raw" in '#'*) raw='' ;; esac` in `declared_list` (before the closer test), and the equivalent
`sed 's/^#.*$//'` stage in `declared_scalar`.

**Left-shift gate.** Add `'Xk =# globsX|XX'` and `'Xk =#who ratifiedX|XX'` to the list specimen loop
at `check-unattended.sh:1653` and `'Xk =# who ratified and whenX|XX'` to the scalar loop at `:1665`.
Both loops already assert the whitespace-preceded form; the un-spaced form is the one that has now
survived two rounds of repair to the same `sed`.

---

## MEDIUM 2 — 28c classifies a whole LINE as wrapper-routed on the substring `GIT `, so a comment defeats the pin test

**`tools/unattended/check-unattended.sh:1590`**. Found by three lenses (two MEDIUM, one LOW).

```sh
case "$_txt" in
  *'GIT '*) sha_wrapped=$((sha_wrapped + 1)); continue ;;
esac
```

That runs first and unconditionally, over the whole line, before any pin test. Reproduced: inserting

```sh
_probe() { git show "$1:$2" 2>/dev/null; }   # TODO route through GIT wrapper
```

into `unattended.sh` leaves the leg at RC=0; the byte-identical line with the comment removed reds
with "a sha is dereferenced without the replace-ref pin" naming that exact line. Only WHOLE-line
comments are filtered (`grep -vE '^[0-9]+:[[:space:]]*#'`), so trailing comments reach the
classifier. A line mixing a wrapper call and a raw dereference —
`if GIT merge-base --is-ancestor "$a" "$b" && git cat-file -e "$c"; then` — is graded on its wrapped
half for the same reason.

No live instance exists today, so this is latent. It is latent on the rule guarding the committed
BASE blob, which is one of exactly two inputs the security model places outside the run's own reach,
on `authorization-reachable`, which takes no override.

Measured alongside it, and it belongs to this finding: the raw arm's entire live population is **one
line**. Running the shipped predicate over all five non-test kit scripts yields 33 hits, of which
exactly one classifies raw — **`check-playbook.sh:121`**, `GITSHOW()`'s own definition, which carries
`core.useReplaceRefs=false` and is `continue`d immediately. So `[ "$sha_raw" -gt 0 ]` at `:1602` is
held up by a single line that is pinned by construction and can never reach the refusal below it. The
population went from 3 files to 5 and from 1 line to 33; the raw arm's reachable population is still
one, and it is the exemption.

**Fix.** Classify per INVOCATION, not per line. Run the two predicates as separate anchored greps —
`(^|[^-[:alnum:]_])GIT[[:space:]]+…` for wrapped, `(^|[^-[:alnum:]_])git[[:space:]]+…` for raw — and
take the raw arm's verdict independently of whether the line also matched the wrapped one. A line
matching both is graded on its raw half.

**Left-shift gate.** Two staged breaks: a raw `git show "$sha:$p"` with a trailing comment mentioning
`GIT `, and one line carrying both `GIT merge-base` and a bare `git cat-file`. Both must red. And give
the raw arm a liveness assertion that excludes its own exemption — `sha_raw` counted AFTER the
`core.useReplaceRefs=false` `continue`, reported explicitly, so the log says plainly that the bare arm
reached no candidate instead of implying it passed one.

---

## MEDIUM 3 — 28c's verb alternation omits every replace-ref-honouring verb the kit uses most

**`tools/unattended/check-unattended.sh:1598`**. Found by two lenses, both MEDIUM.

The header above the rule says "EVERY SHA DEREFERENCE IN THIS KIT GOES THROUGH A PINNED READ". The
alternation is `(show|cat-file|ls-tree|archive|rev-list|merge-base|diff-tree)`. Counted over the five
non-test kit scripts, the verbs it omits are used at **39 wrapper-routed sites and 8 bare ones**:

| verb | wrapper-routed (`GIT`) | bare (`git`) |
|---|---|---|
| `rev-parse` | 23 driver · 13 check-unattended · 3 lib | 6 |
| `log` | 5 check-unattended · 2 lib | 0 |
| `for-each-ref` | 0 | 1 |
| `grep` / `diff` | present | 1 |

`git log -1 --format=%s <sha>` reads the commit object and is moved by a replace ref exactly as
`git show` is; `lib-unattended.sh:82-83` feeds unit-id matching on commit subjects through it, which
is provenance-bearing.

**There is no live hole today**, and I verified that rather than assuming it: every bare
`rev-parse`/`for-each-ref` in the kit is `--show-toplevel`, `--path-format=absolute --git-common-dir`,
or `refs/replace/` — none takes an object. So this is a class gap plus a header that overclaims, on a
security-relevant control. The gap is asymmetric with the wrapper half: `_wrapdef` proves `GIT()` is
pinned, so the 39 wrapped sites are covered by construction, while the sixth bare `git log <sha>`
anyone writes is invisible.

**Fix.** Widen the alternation to
`(show|cat-file|ls-tree|archive|rev-list|rev-parse|log|grep|diff|diff-tree|merge-base|for-each-ref|describe|blame)`.
Per §7, run the widened predicate over the tree BEFORE wiring it and print hits and near-misses — the
`rev-parse`/`grep`/`diff` arms will pick up non-dereferencing uses (`--show-toplevel` and friends)
that need either the pin or a named, asserted exemption, and shipping the widened predicate without
that pass reds eight innocent lines.

**Left-shift gate.** Once widened, the seven `GIT log` sites land in `sha_wrapped`, so both liveness
assertions stay satisfied and the raw arm gains real coverage. Add a staged break inserting a bare
`git log -1 --format=%s "$sha"` and assert it reds — which is also the arm that keeps the header's
claim honest.

---

## MEDIUM 4 — 28a's per-FILE counter is dead, so the guarantee its own header states is not implemented

**`tools/unattended/check-unattended.sh:1480`** (init) and **`:1483`** (increment). Found by four
lenses (one HIGH, two MEDIUM, one LOW). **I did not take the HIGH grading**, for the reason two of the
four lenses gave themselves: the honest repair is partly to the comment, and a naive per-file floor
would be wrong.

`grep -n '_f_sites'` returns exactly two lines — the init and the increment. Nothing reads it. The
only liveness assertion is `[ "$_p_sites" -gt 0 ]` at `:1497`, a per-parser floor summed across the
whole population. The comment at `:1477-1479` states the rule the code does not implement:

> A parser whose calls all live in one file, and a file whose calls this pattern stopped matching,
> are different failures and neither may be masked by the other.

The masking is reachable. `declared_list` has call sites in two files — `unattended.sh:951,2165` and
`check-playbook.sh:342,425`. If the enumeration pattern `\$\(declared_list[[:space:]]` stops matching
one file's spelling (a reformat, `$( declared_list`, a line continuation, a redirect form), that
file's sites go invisible while the other keeps `_p_sites > 0` and 28a reports a clean nothing about
the blind file.

The suite knows. The staged break at `check-unattended.test.sh:1567-1568` mutates BOTH files, and its
comment says why: "Both files, because the counter is per parser: a call left in either one is still
a call site." The dead variable is the code's own record that a per-file guarantee was intended and
not written — §7's "a gate satisfied by its own comment prose", turned on the check that exists to
refuse it.

A blanket per-file floor is NOT the fix: measured, `declared_list` has 2 sites in `check-playbook.sh`,
2 in `unattended.sh`, and 0 in `adopt-unattended.sh`, `check-unattended.sh` and `lib-unattended.sh`,
so a blanket floor reds three of five files immediately.

**Fix.** Make the claim real on a reachable predicate: assert `[ "$_f_sites" -gt 0 ]` only for files
that mention the parser's NAME at all (`grep -q "$_p" "$_f"`), which catches a file whose call
spelling drifted while the parser is still referenced there and is silent about files that
legitimately never call it. If that is not wanted, delete `_f_sites` and rewrite the comment to say
the rule is per-parser only and to name which files go unpoliced when a spelling changes. Either is
acceptable; leaving the comment as-is beside a dead counter is not.

**Left-shift gate.** Add a staged break that renames `declared_list` calls in the DRIVER ONLY and
assert 28 reds, and confirm the existing both-files arm still reds. One arm per masking direction is
the whole point of the counter.

---

## LOW 1 — the `flo_bad` repair left the `elif` unguarded, so a non-numeric floor now prints a raw interpreter error

**`tools/unattended/check-playbook.sh:261`**. Found by two lenses, both LOW.

Line 246 sets `flo=""; flo_bad=1` on a non-numeric floor. Line 259's
`if [ -z "$flo" ] && [ -z "$flo_bad" ]` is then false, so control reaches
`elif [ "$nsteps" -lt "$flo" ]` with `$flo` empty. Reproduced:

```
$ nsteps=3; flo=""; [ "$nsteps" -lt "$flo" ]
bash: [: : integer expected
rc=2
```

Before this diff the empty `flo` was absorbed by the first branch and the comparison was unreachable,
so the fix opened the path it was written to tidy. The verdict is unaffected — `fail 3` has already
set the status and the elif is false — so round 5's LOW 10 is genuinely fixed. What is left is noise
in the wrong place: `unattended.sh:2075` captures the leg with `2>&1`, so the diagnostic rides into
`_raw` and can surface verbatim beside the leg's real words in a DoD refusal message. A leg whose
entire subject is honest reporting should not interleave an un-attributed interpreter error into its
own output on exactly the input the fix targets.

One correction to a supporting claim, since it was cited as evidence: the self-test's `run()` swallows
the message into a variable and prints it only on a failing arm, so it does NOT currently appear in
test output. The suite passes with 90 assertions and no `integer expected` anywhere in it.

**Fix.** `elif [ -z "$flo_bad" ] && [ "$nsteps" -lt "$flo" ]; then`, or `continue` after the numeric
refusal — no further check-3 arm can say anything useful about an unparseable floor.

**Left-shift gate.** Extend the existing non-numeric-floor arm at `check-playbook.test.sh:337` to
assert the leg's stderr contains no `integer expected`. That keeps the three arms of this if/elif from
drifting out of sync again, which is what happened here.

---

## LOW 2 — 28b's positive binding has no comment filter, while its negative half does

**`tools/unattended/check-unattended.sh:1518`**. One lens, LOW.

The positive predicate is a bare `grep -qE "declared_(list|scalar) .* $_k\)" "$_f"`. The negative half
three lines down pipes through `grep -vE '^[0-9]+:[[:space:]]*#'`. So a key can be certified as "read
by the parser this check certifies it through" by a COMMENT that merely quotes the call spelling. This
codebase's comments quote code verbatim constantly — the block directly above quotes
`s/^outputs[[:space:]]*=` and `s/^step_floor[[:space:]]*=`.

Measured over all ten template keys against all five non-test kit scripts today: zero comment-only
matches. Latent. It is still the shape that lets both halves of 28b be satisfied at once — the
positive by a leftover comment, the negative by a rewritten reader that does not spell `^<key>`.

**Fix.** Give the positive predicate the negative half's filter:
`grep -nE "declared_(list|scalar) .* $_k\)" "$_f" | grep -qvE '^[0-9]+:[[:space:]]*#'`.

**Left-shift gate.** Arm it by commenting out one real call site in the staged-break suite and
asserting the key is then reported unread.

---

## LOW 3 — `KIT_N` is dead state beside a comment explaining why a count floor was not used

**`tools/unattended/check-unattended.sh:1436`** (init) and **`:1441`** (increment). Found by three
lenses, all LOW.

`grep -n KIT_N` over the whole repo returns exactly those two lines. Nothing reads it. It sits
immediately above a comment arguing at length that a count floor is unreachable here, so it reads on
inspection as a live population counter and the next reader has to re-derive that it is not. Same
residue class as `_f_sites`.

**Fix.** Delete both lines. The comment already carries the reasoning the counter would otherwise
imply.

**Left-shift gate.** None worth building for this alone. If a shellcheck leg is ever added to the bar,
`SC2034` (assigned but never used) covers `KIT_N` and `_f_sites` together and would have caught both
before review — that is the honest gate suggestion, and it is one leg for two findings.

---

## Checked and clear

Recorded because "we looked and found nothing" is only worth anything when it names what was looked at.

- **The two branches deleted as unreachable really are unreachable.** The driver-membership branch:
  check 1 at `check-unattended.sh:107-110` does `fail 1 …; exit "$status"` when the driver's core sets
  are unreadable, nine hundred lines above 28's population build, so a driver-missing branch there
  could be reached by no fixture. The count floor: `check-unattended.sh` and `adopt-unattended.sh` are
  themselves non-test `*.sh` in the scanned directory, so the population is never empty and a
  `KIT_N -gt 0` floor could never fail. Both deletions are correct; only their counters were left
  behind (LOW 3, MEDIUM 4).
- **`$2` reaching `grep -E` unescaped** in both parsers (`check-playbook.sh:178,209`,
  `unattended.sh:2410,2441`) is inert today and I am not filing it. Every caller passes a literal key
  name, and the one dynamic source — 28b's template loop — derives keys through
  `awk '…/^[a-z_]+[[:space:]]*=/…'`, which cannot emit a regex metacharacter. It becomes live the
  moment a key is read from anywhere else, so it is worth a comment at the parser rather than a fix.
- **The copy-inline discipline holds.** `declared_list` and `declared_scalar` are byte-identical
  between `unattended.sh` and `check-playbook.sh`, and check 28's compare arms cover both parsers in
  both directions (missing-from-one, and drifted). Every parser defect above is therefore present in
  exactly two places and must be fixed in both, which the compare enforces.
- **The gotcha checklist for this diff** (`python tools/memory-tree/gotchas.py --for-diff
  22cbb7a3..HEAD`) selected nine classes. Three fired: `fixture-passes-by-finding-nothing` (BLOCKER 1's
  staged break, BLOCKER 2's missing accept specimen), `containment-tested-one-way` (HIGH 1, MEDIUM 2),
  and `two-answers-to-one-question` (MEDIUM 4's comment against its code).
  `inputs-inside-the-subjects-reach` is the standing frame for MEDIUM 2 and MEDIUM 3 rather than a
  finding of its own. `assertion-between-two-derived-values`, `status-set-in-a-subshell`,
  `id-matched-as-a-substring`, `heredoc-escape-reaches-the-regex` and
  `second-implementation-is-not-a-second-opinion` were checked against the diff and did not fire.

## The two classes worth minting, and why this keeps happening

Six rounds of the same shape is a signal about the METHOD, not about any one gate. Two candidate
gotchas would name what actually recurs, and neither exists in `memory/gotchas/` today:

- **`structured-record-split-on-whitespace`** — a multi-field record held in one shell variable and
  iterated with an unquoted expansion degenerates into its first field, and every assertion built on
  the later fields becomes unfalsifiable while looking exactly like a working one. BLOCKER 1 is the
  instance; the general form is any `for x in $VAR` over a value containing spaces. Gateable: a
  predicate over the kit's own sources for `for [A-Za-z_]* in \$[A-Z_]*` where the named variable's
  assignment contains a space.
- **`staged-break-substitutes-a-synthetic-value`** — an arm that proves a mechanism by REPLACING the
  shipped value with a simpler one proves the mechanism for the simpler value.
  `KEY_EXEMPT="…|THIS_LITERAL_IS_GONE"` cannot exhibit a split its replacement has no spaces to
  produce, and the arm passes green while the shipped construct is vacuous. The rule that would have
  caught it: **a staged break mutates the subject, never the constant the subject is measured
  against.** This is the sharper cousin of `fixture-passes-by-finding-nothing`, and it is the one this
  build keeps paying for.

The mechanical version of the same lesson, for §7: **a classifier decides on a TOKEN, never on a
line.** `*'||'*`, `*'GIT '*` and `[[:space:]]#` are three spellings of one mistake, and each of them
was introduced by a commit fixing the previous one.
