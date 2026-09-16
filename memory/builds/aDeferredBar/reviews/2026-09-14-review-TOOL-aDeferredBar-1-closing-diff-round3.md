**Serves:** diff-review TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

# aDeferredBar — closing diff review of the three-unit build, round 3

*Node `a`, 2026-09-14, unattended. Round 3 reviews the round-2 FOLD only: the two fold commits, the
records that carried their left-shifts, and nothing round 2 already graded. Four primed finder
lenses, five batched skeptic passes prompted to REFUTE every finding, one synthesis. Round 2 found
three of its seventeen findings were the previous fold certifying itself, so this round's brief put
the fold's own arms and comments in scope beside the code. Every exit code and count below was
re-run on this tree during synthesis: the five direct checks the brief names, run on the clean tip
(`check-arms.py --check`, `check-install-prefix.sh`, `check-spec-tokens.py`, `check-unattended.sh`,
`adopt-unattended.sh --check`), the checker's `BAR` regex loaded as a module and probed on six
strings, twenty-two commands fed to `tools/unattended/gate-guard.js` on stdin as Bash and
PowerShell tool-use payloads with this worktree's `cwd` while its `RUN.md` reads `phase: REVIEWING`,
three heredoc payloads run under real bash in a scratch tree with a suite stub, and three
assignments run under this node's pwsh. The figures are what those runs printed; a repro credited
to a lens or a skeptic below is one the synthesis did not repeat and says so. The security model is
read as given: the hook is a
textual, fail-open hygiene guard, and a runtime-assembled path walks past it by design. No finding
below argues with that ceiling; every one names a shape the header or a comment claims to cover.*

**Reviewed range:** `19814c77...HEAD`, HEAD being `d4032575`. Base `19814c77` is round 2's recorded
tip. In range: the round-2 record commit `4d177329`, the two fold commits `15148b2a` (unit 2, the
checker and driver side: R1 R2 R3 R7 R8 R11 R12 R16 R17) and `593fa5c8` (unit 3, the hook and
adopter side: R3 R4 R5 R6 R9 R10 R12 R13 R14 R15 R16), five backlog rows `7dcb3641`, and one
citation fix `d4032575`. After the fold the main loop ran the plain scoped bar once, which the
mandate allows there: 47 of 48 legs green, the one red a backlog citation the dead-path check reads
whole, fixed in `d4032575`; 55 self-test legs held. **Round: 3.**

## Verdict: CLEAN WITH FIXES

No blocker, one high, four mediums, four lows, after consolidating the sixteen confirmed arrivals
into the nine distinct defects below. Nothing reds at HEAD: every direct check the brief named
exits 0 on the clean tip (figures under "What this review did"), so unlike round 2 no finding here
is a machine already refusing the tree. The high is the round-2 R13 fold reversing a correct deny
into a certified allow — bash expands `$( … )` and backticks inside an UNQUOTED heredoc body before
the consumer reads a line, the fold blanks every heredoc body regardless of its delimiter's quoting,
and the arm it added pins the payload bash executes as `allow`. It is rated high and not medium
because it is the one finding whose fix must start by turning a green arm red: the arm certifies the
defect, and the walker comment beside it states the false premise the next reader will trust.

What round 3 finds is otherwise the same kind round 2 named, one token later: the round-2 fix gated
the instance and left the sibling standing. The `timeout` grammar consumes a literal duration and
not the variable one the driver's own `run_bounded` spells; the `$env:` read covers three spacings
of the `=` and not the fourth PowerShell accepts; the `py` launcher was added without the one option
`py.exe` is known for; the D5 nesting cap is spent by a recursion whose comment says it needs none.
Five of the nine carry a comment or an arm asserting what the code does not do — the same
self-certifying shape round 2 counted three of, and the reason the fold's prose is in scope again.

**Review shape.** Raw 19, confirmed 16, refuted 3, unverified 0, precision 0.84. The sixteen
confirmed arrivals collapse to nine: the `py -3` launcher selector arrived four times (ids 3, 9, 13,
18), the PowerShell `$Env:NAME= 1` spacing three times (8, 12, 15), the unquoted heredoc twice (2,
11) and the `depth + 1` recursion twice (5, 17). The harness itself dropped no duplicate; the
collapse is this synthesis. The three refuted findings are not re-opened here.

**Run integrity.** Lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by
the harness. The finding set is therefore complete for what four lenses can reach, and a zero below
is evidence within that coverage rather than an artefact of a dead lens. Two zeros are worth naming
as positive: no finding landed on the driver's inline `resolve_python` block or on
`verb_dispatch`'s checker invocation, and no finding landed on `read_cutoff_key` or the re-keyed
pin rows of `memory/project/unarmed-branches.txt`; both zeros rest on the lenses AND on a direct
check that exits 0 on the tip (`check-arms.py --check`, `check-spec-tokens.py`), which is more than
round 2 could say of its install-prefix zero.

## Findings, severity-ranked

| # | Sev | Where | Defect |
|---|-----|-------|--------|
| T1 | HIGH | `tools/unattended/gate-guard.js:173`, `:119`, `tools/unattended/gate-guard.test.sh:293` | Every heredoc body is blanked as content, but an UNQUOTED delimiter substitutes: `cat <<EOF` / `$(bash <suite>)` runs the suite under bash and exits 0 from the hook; the R13 control arm pins that payload as `allow` |
| T2 | MEDIUM | `tools/unattended/gate-guard.js:322`, `:330` | `$Env:GATE_FULL= 1; bash <bar>` (glued `=`, space, value) assigns under PowerShell and exits 0; the comment declares it the OFF spelling, the header and spec 3 rev-7 §3 claim every spacing is read, no arm covers it |
| T3 | MEDIUM | `tools/unattended/gate-guard.js:205`, `:541` | A backtick inside double quotes opens a substitution span for BOTH tools, but under PowerShell it is the escape character; `` `$env: `` and `` `" `` in a commit message or `Write-Host` are false DENIES, observed live blocking a review probe |
| T4 | MEDIUM | `tools/unattended/gate-guard.js:145` | `buildCommandView` pairs `"` naively across a `$( )` span, so a double-quoted ARGUMENT inside a quoted substitution is un-blanked: `msg="$(printf "%s" "run bash <suite> next")"` exits 2 where rev-6 exited 0 — the R5 class, regressed |
| T5 | MEDIUM | `tools/unattended/gate-guard.js:297`, `:353` | `DURATION_RE` consumes a literal duration only; `timeout "$GATE_BOUND" bash <suite>`, `$T`, `${T}s`, `-k 5s "$GATE_BOUND"` and `1.5` all exit 0, while the checker's `BAR` grades each as a bar — the readers spec 2 rev-6 §9 says read alike diverge again |
| T6 | LOW | `tools/unattended/gate-guard.js:298`, `:374`, `tools/check-spec-tokens.py:124` | `py -3 <selftest.py>`, `py -3.12 …`, `python -X utf8 …`, `python -Xutf8 …` make the option the head; both readers miss in lockstep and the R12 arms certify bare `py` only |
| T7 | LOW | `tools/unattended/gate-guard.js:146`, `:212` | `buildCommandView` honours `\` only inside `"`; `readQuotedSubstitutions` honours it outside too, so `\"` outside a string opens a bogus one: `git commit -m \"msg\" && bash <suite>` exits 0 |
| T8 | LOW | `tools/unattended/gate-guard.js:409`, `:386` | The substitution recursion passes `depth + 1`, the counter D5 caps at `MAX_NEST = 1`, so a `bash -c` inside a quoted `$( )` is never opened; `echo "$(echo done; bash -c 'bash <suite>; echo x')"` exits 0 where the bare `bash -c` exits 2 |
| T9 | LOW | `tools/unattended/adopt-unattended.test.sh:101`, `:88` | The R15 `unset GOV_SETTINGS_JSON` lands after arm 1's `--check`, which reads the variable too; the comment's "the variable is clear here" is one arm short |

## T1 — an unquoted heredoc body substitutes, and the fold's arm certifies the miss (HIGH)

`buildHeredocView` at `gate-guard.js:115-131` blanks every heredoc body, and the `here` regex at
`:119` captures the delimiter's quote in group 1 and never reads it. `readQuotedSubstitutions` at
`:173` reuses that view under the comment "a heredoc body is content, whatever it spells". Bash
disagrees on exactly the bit the regex drops: a body under `<<EOF` (or `<<-EOF`) is expanded —
parameters, `$( … )` and backticks — before the consumer reads a line; only `<<'EOF'` and `<<"EOF"`
bodies are content. Verified under real bash in a scratch tree with a stub `tools/x.test.sh` that
prints `SUITE-RAN`: `cat <<EOF` / `$(bash tools/x.test.sh)` / `EOF` runs the suite, and the R13
control arm's payload VERBATIM — `python - <<EOF` / `x = "a `tools/x.test.sh` mention"` / `EOF` —
runs it before python receives a line, python then printing `a ran mention`; the `<<'EOF'` form
leaves the `$( )` literal. The skeptic added the `cat <<EOF > f` variant with `"$( )"` to the set
that runs. Fed to the hook on stdin at REVIEWING on this tree, all three exit 0, and so does the
quoted `<<'EOF'` control, which is the one allow of the four that is right. The arm at
`gate-guard.test.sh:293` pins the unquoted form
as `allow` under the comment at `:290` that a backtick in such a body "is prose, not a
substitution", which is false for `<<EOF` and true for `<<'EOF'`. Round 2's R13 asked for backticks
inside double quotes to be read as substitutions; the fold's first cut denied this payload, which
was the correct verdict, and the heredoc blanking was added to make the arm pass. Unquoted `<<EOF`
is the common agent spelling (`git commit -F - <<EOF`, `python - <<EOF`), and this repo's prose
habitually backticks command names, so a backticked suite in such a body is both a hook miss and a
run the agent did not mean to start. Not the declared ceiling at `:69-73`: that names a python
heredoc that itself SPAWNS a suite, and this is bash running it before python sees the body.

- **Fix.** In `readQuotedSubstitutions`, when `hm[1] === ''` (unquoted delimiter) do not blank the
  body: walk it as one double-quoted region — quote characters literal, `$( … )` and backtick spans
  collected across the whole body — and push each span the way a quoted span is pushed. Keep
  blanking quoted-tag bodies, and keep `buildCommandView`'s blanking for the segment scan. Flip the
  R13 arm to `<<'EOF'` as the allow control; add `<<EOF` with the same body as a deny naming
  `tools/x.test.sh`, and one for `cat <<EOF` / `$(bash <suite>)`; observe both RED on the tip
  first. Correct the `:173` comment. Re-key the install-prefix row and the floor by the diff.
- **Left-shift.** The arm was written to the walker's premise rather than to bash's. A control arm
  for a quoting rule should be observed against the SHELL before it is pinned against the hook: a
  three-line harness that runs the payload under `bash -c` in a scratch tree with a suite stub and
  asserts whether `SUITE-RAN` printed, beside the hook's verdict, cannot certify an allow bash
  executes. The heredoc regex already computes the bit; the class is "a computed value nobody
  reads", which the same harness makes visible the first time the two verdicts disagree.

## T2 — the fourth spacing of the PowerShell assignment runs the flagged bar (MEDIUM)

`FLAG_RE` at `gate-guard.js:322` matches `$Env:GATE_FULL=` with an empty value group and falls
through; `PS_FLAG_NAME_RE` at `:326` requires no trailing `=`, so the branch that reads the value
forward is never entered; the token becomes the head, `resolveFileRow` returns null, and the `1` is
dropped. The comment at `:330-331` declares this by design: a glued `NAME=` with nothing after it
"is the OFF spelling above, never read forward". That is bash's empty-assignment rule applied to a
`$env:`-prefixed token bash never treats as an assignment. PowerShell's assignment operator takes
whitespace on either side, so `$Env:GATE_FULL= 1` assigns: verified in pwsh on this node (`$Env:X=
1; $Env:X` prints `1`, `${env:X}= 7` prints `7`, and `$Env:X=;` is a PARSE ERROR, so PowerShell has
no glued-empty OFF spelling for the rule to protect). Fed to the hook on stdin under `tool_name:
PowerShell` on this tree: `$Env:GATE_FULL= 1; bash tools/run-gates/run-gates.sh` and `${env:GATE_FULL}=
1; …` exit 0, while `$Env:GATE_FULL=1`, `$Env:GATE_FULL = 1` and `$Env:GATE_FULL =1` exit 2. The header
at `:25` says "glued or with spaces around the `=`", spec 3 rev-7 §3 (`:85`) says "Row D1 reads every
one of those spellings", and the R4 arms at `gate-guard.test.sh:350-354` test the glued, ` = ` and
` =` forms only. PowerShell is this node's primary shell tool; the run is before VERIFYING; no arm
covers the shape either way.

- **Fix.** When `FLAG_RE` matches with an EMPTY value and the token carries the `$env:` / `${env:`
  prefix (`/^\$\{?[Ee][Nn][Vv]:/`), read forward one token the way the `PS_FLAG_NAME_RE` branch
  does: a present non-empty next token is a D1 hit carrying both tokens; an empty quoted token
  (`$Env:GATE_FULL= ""`) or end of segment stays OFF. Reading forward is safe under Bash because a
  `$env`-prefixed word is never a bash assignment. Add the deny arm `$Env:GATE_FULL= 1; bash <bar>`
  and the `${env:GATE_FULL}= 1` form, and the allow control `$Env:GATE_FULL= ""; bash <bar>`,
  observed rc=0 on the tip first. Correct the comment; it is the assertion the fold made against
  itself.
- **Left-shift.** Round 2's R4 left-shift asked for a table-driven arm over every (casing × brace ×
  spacing) product, and the fold wrote five hand-picked arms instead. Write the table: three
  casings, two brace forms, four spacings (`=1`, ` = 1`, ` =1`, `= 1`), each asserted deny under
  PowerShell, plus the two empty forms asserted allow — twenty-six strings in one loop that cannot
  be satisfied by the instance a third time.

## T3 — the PowerShell backtick is an escape, and the walker reads it as a substitution (MEDIUM)

`readQuotedSubstitutions` at `gate-guard.js:205` treats any backtick inside a double-quoted string
as a command substitution and slices to the next backtick or end of text, and `main()` at `:541`
drops `tool_name` before `checkCommand`, so the walker cannot tell the two wired tools apart even
though `TOOLS`, the fragment matcher `Bash|PowerShell`, and the `$env:` branch at `:288-293` make
PowerShell first-class. Under PowerShell the backtick is the escape character and never a
substitution: `` `$ `` is the ONLY way to write `$env:` literally inside a double-quoted string, and
`` `" `` the only way to embed a quote. Observed LIVE by a lens, not only on stdin: the wired
PreToolUse hook on this node blocked that lens's own PowerShell probe because it contained the
double-quoted literal `"[`$env:GATE_FULL=1 literal]"` — stderr `BLOCKED by gate-guard … flag:
$env:GATE_FULL=1`, exit 2, with the run at REVIEWING. Stdin, re-run here, agrees: `git commit -m "docs: the `$env:GATE_FULL=1
spelling"` exits 2 (D1) and `Write-Host "see `"tools/x.test.sh`" for the arm"` exits 2 (D4) under
`tool_name: PowerShell`. A fresh false-deny class of the R5/R6 kind, reachable on this node's primary
shell by any commit message or echo that mentions the very spellings this build documents.

- **Fix.** Pass `data.tool_name` into `checkCommand` and `scanDenyHits`; for PowerShell, treat a
  backtick inside double quotes as an escape (skip the next character) instead of opening a span,
  and keep the `$( … )` branch, which is a PowerShell subexpression. Two PowerShell allow arms for
  the payloads above, observed rc=2 on the tip first.
- **Left-shift.** The hook has been PowerShell-aware since R4 in one branch and Bash-only in every
  other, and nothing asserts the split. An arm that feeds every deny fixture under BOTH tool names
  and prints the pairs whose verdicts differ turns the question "which tool is this walker written
  for" into a printed table instead of a live block; the differing pairs are then either declared
  or fixed.

## T4 — a double-quoted argument inside a quoted span is read as a command again (MEDIUM)

`buildCommandView` at `gate-guard.js:143-151` pairs the outer `"` with the FIRST `"` inside a
`$( … )` span, so a double-quoted argument inside a quoted substitution is un-blanked in the view.
Reproduced on stdin against a BUILDING fixture: `msg="$(printf "%s\n" "run bash tools/x.test.sh
next")"` exits 2 naming `suite: tools/x.test.sh`, and `export MSG="$(printf "%s" "see bash
tools/x.test.sh for it")"` exits 2 too; the rev-6 hook at `4d177329` exits 0 on both. Traced: the
inner `"` closes the outer string, `run bash tools/x.test.sh next` becomes unquoted text,
`scanSegments` sees one segment, `readTokenAt` folds `msg=$(printf %s\n run` into an assignment
token `ASSIGN_RE` skips, `bash` is the launcher and `tools/x.test.sh` lands at head. It escapes only
when a non-assignment word such as `echo` is the head, which is why the R5 and R6 arms — a
SINGLE-quoted inner argument, or `echo` / `git commit -m` heads — stay green over the gap. The
corpus A/B (Reading 4) did not list this shape, so it is rare; but a false deny of a benign
assignment at BUILDING is the class R5 claimed retired, and this is a regression the round-2 fold
introduced.

- **Fix.** In the double-quote walk of `buildCommandView`, when `view[j] === '$' && view[j+1] ===
  '('` advance `j` past the matching `)` using the depth and quote tracking `readSpanEnd` already
  has (and past the closing backtick for a backtick span), blanking the whole span; the view then
  treats the substitution as content, which is right because `readQuotedSubstitutions` scans its
  body separately. Add the arm `msg="$(printf "%s" "run bash tools/x.test.sh next")"` → allow and
  observe it RED on the tip first.
- **Left-shift.** The two walkers were built to agree and nothing checks that they do. One arm
  that runs every double-quoted fixture through both `buildCommandView` and
  `readQuotedSubstitutions` and asserts the set of `$( )` spans each finds is identical closes the
  class; T7 is the same disagreement one character earlier and the same arm catches it.

## T5 — `timeout` consumes a literal duration, and the readers diverge on the variable one (MEDIUM)

`DURATION_RE` at `gate-guard.js:297` is `/^\d+[smhd]?$/`, and the option loop at `:353-365` leaves
`timeout` as the head whenever the next token is neither a literal duration nor an option. Fed to
the hook on stdin at REVIEWING on this tree: `timeout "$GATE_BOUND" bash tools/x.test.sh`, `timeout
$T …`, `timeout ${T}s …`, `timeout -k 5s "$GATE_BOUND" …` and `timeout 1.5 …` all exit 0, while
`timeout 120 …` and `timeout -k 5 120 …` exit 2. The checker's `BAR` at `check-spec-tokens.py:122-126`
takes the duration as `\S+` and grades every one of the five as a bar (probed by loading the module
and calling `BAR.search`). The two readers spec 2 rev-6 §9 says "read the one token alike again" and
the `:111-113` comment says "read alike in both" therefore diverge on exactly the spelling the
driver's own `run_bounded` uses — `timeout -k 5s "$GATE_BOUND" "$@"` at `unattended.sh:190` — so an
agent copying the repo's idiom is the case that walks past. Same class as round 2's R14, one token
later; the header at `:20-21` claims `timeout` "with its options and duration" without declaring
the exclusion.

- **Fix.** After the option loop, skip one more token as the duration whenever it is not itself a
  launcher or head candidate: `if (k < toks.length && (DURATION_RE.test(toks[k]) ||
  /^\$|^[0-9.]+[smhd]?$/.test(toks[k]))) k++`. Deny arms for `timeout "$GATE_BOUND" bash <suite>`
  and `timeout 1.5 bash <suite>` in `gate-guard.test.sh`; feed the same two strings to `BAR` in
  `check-spec-tokens.test.sh` so the readers are asserted on one payload.
- **Left-shift.** The parity arms compare each reader against the MANIFEST, and the manifest holds
  no `timeout` leg, so nothing compares the readers against EACH OTHER. One fixture file of
  launcher spellings read by both suites, each asserting its reader's verdict per line, makes "read
  alike" a gate rather than a sentence in a revision log; a spelling one reader takes and the other
  drops then reds in the suite of whichever reader is behind.

## T6 — `py -3` and `python -X utf8` make the option the head in both readers (LOW)

`SHORT_OPT_RE` at `gate-guard.js:298` is `/^-[A-Za-z]+$/` and the launcher branch at `:366-374`
skips one such option, so `-3` is not skipped and becomes the head; `-X` is consumed as a valueless
option so `utf8` becomes the head. On stdin: `py -3 tools/govkit/selftest.py`, `py -3.12 …`, `python
-X utf8 …` and `python -Xutf8 …` exit 0, while `py tools/govkit/selftest.py` and `python3.12 …` exit
2. `BAR` at `check-spec-tokens.py:124` has the same `-[A-Za-z]+` slot and misses the same four
(probed), so the readers miss in lockstep and the parity arms cannot see it: the manifest's
`selftest.py` legs all spell `python3`. `-3` is `py.exe`'s defining option and the PEP 397 spelling
on the MS-Store-stub node class R12 was added for; the repo's own resolver comment
(`tools/lib/resolve-python.sh:27`) names `py -3` as the launcher's real spelling it cannot use only
because its probe needs one word. One correction the skeptic made stands: the resolver's third
candidate is bare `py`, which IS caught, so the fold's target spelling does not walk past — the
everyday spelling beside it does. Low because no kit script emits it and the hook fails open by
design; real because the R12 arms at `gate-guard.test.sh:363-364` certify bare `py` only and neither
header declares the exclusion — the gate-the-instance shape R12 was itself accepted for.

- **Fix.** In the launcher branch accept a version selector or `-X` with its value as the skipped
  option: `SHORT_OPT_RE.test(toks[k]) || /^-\d+(\.\d+)?$/.test(toks[k])`, and skip one more token
  after a bare `-X`; keep the `-c` / `-m` bail-out. Give `BAR`'s slot the same grammar:
  `(?:(?!-[ncm]\s)(?:-[A-Za-z]+|-\d+(?:\.\d+)?|-X\s+\S+)\s+)?`. One deny arm per reader for `py -3
  <selftest.py>` and one for `python -X utf8 <selftest.py>`.
- **Left-shift.** The shared fixture file T5 asks for covers this too; a `py -3` line in it reds
  both readers today.

## T7 — the two walkers disagree on a backslash outside quotes (LOW)

`buildCommandView` at `gate-guard.js:146` honours `\` as an escape only INSIDE double quotes;
`readQuotedSubstitutions` at `:212` honours it outside too. An escaped quote outside any string
therefore opens a bogus string in the view, and the walker never enters a quoted state, so neither
sees a following `$( )`. On stdin: `echo \"$(bash tools/x.test.sh)\"` and `echo "$(echo \" ; bash
tools/x.test.sh)"` exit 0, and the skeptic ran both under real bash in a scratch tree and watched
the suite run. The cited spellings are contrived; the natural one the skeptic added is not: `git
commit -m \"msg\" && bash tools/x.test.sh` exits 0 (re-run here),
because the bogus string swallows the rest of the line, suite included. Over-escaped quotes in a
Bash tool call are a routine agent tic. Not among the ceilings the `:69-73` comment declares.

- **Fix.** In `buildCommandView`'s outside-quotes branch honour a backslash the way the walker
  does: `else if (ch === '\\') { out += ch + (view[i+1] || ''); i += 2 }` — one rule for both. Deny
  arms for `echo \"$(bash <suite>)\"` and `git commit -m \"msg\" && bash <suite>`.
- **Left-shift.** The walker-agreement arm under T4.

## T8 — the substitution recursion spends the cap its comment says it does not need (LOW)

`gate-guard.js:409` recurses over a quoted substitution body at `depth + 1`, and `:386` opens a
`bash -c` body only when `depth < MAX_NEST` (`= 1`), so a `-c` inside a quoted span is never opened.
On stdin against a BUILDING fixture: `echo "$(echo done; bash -c 'bash tools/x.test.sh; echo x')"`
exits 0 while `bash -c 'bash tools/x.test.sh; echo x'` exits 2; `echo "$(bash -c 'bash
tools/x.test.sh > out')"` exits 0 too, and the `\"…\"` form the finder thought still denied is also
rc=0 (the token reads as `\bash tools/x.test.sh\`). The `:405-407` comment says the recursion "needs
no cap of its own", which is true — the body is strictly shorter — yet the code spends D5's. The
unquoted form `x=$(bash -c '…')` is scanned at depth 0 and denied, so the "scanned the way row D5
scans a `bash -c` body" parity the header claims holds only outside double quotes. No arm covers a
`-c` inside a span. Low, and not by design.

- **Fix.** Pass `depth`, not `depth + 1`, when recursing over substitution bodies; add the deny arm
  `echo "$(bash -c 'bash tools/x.test.sh > out')"`, observed rc=0 on the tip first.
- **Left-shift.** None beyond the arm; the recursion is one call and the change is one token.

## T9 — the `unset` lands one arm short of the population R15 named (LOW)

`adopt-unattended.sh:359` resolves `SJ=${GOV_SETTINGS_JSON:-…}` on every `--check`, and the suite's
arm 1 `--check` at `adopt-unattended.test.sh:88` runs in a subshell that inherits the ambient
environment thirteen lines before the `unset GOV_SETTINGS_JSON` the fold placed at `:101`. The
comment at `:98-100` says "this arm reads the FIXTURE's file only because the variable is clear
here", which does not hold for the arm above it. The skeptic reproduced it on a seeded fixture
(not repeated here): with the variable clear, `--check` prints in sync; with it naming a non-file
the same fixture prints REFUSED (exit 1); with it naming an unwired out-of-tree file while the
fixture's own `settings.json` is wired it prints UNWIRED (exit 1). Round 2's R15 record itself
listed "arm 1's `--check` at `:84`" among the exposed
expectations and then prescribed the `unset` "at the top of arm 1a", and the implementer put it
exactly there.

- **Fix.** Move the `unset GOV_SETTINGS_JSON` into the suite prologue above the first `--check`;
  the out-of-tree arms that want it set it inline already.
- **Left-shift.** Round 2's R15 left-shift stands unimplemented: a scrubbed-environment preamble
  shared by every suite that exercises an environment-reading resolver, or a one-line
  `check-testsuite-counts`-style assertion that a suite whose subject reads a `GOV_` variable
  unsets it before its first arm.

## What this review did, and did not do

It did not run the merge bar or any self-test suite, per the mandate this build exists to enforce.
The direct checks the brief named were all run on the clean tip `d4032575`, and every one exits 0:
`python tools/memory-tree/check-arms.py --check` printed nothing; `bash tools/check-install-prefix.sh`
printed clean over 209 shipped files with 11 declared waivers and a carried-prefix clean over 136
recorded files, 38 hand-justified, none rising; `python tools/check-spec-tokens.py` graded 738 tokens
across 28 live specs with 22 waivers; `bash tools/unattended/adopt-unattended.sh --check` printed in
sync; `bash tools/unattended/check-unattended.sh` took 6 m 31 s of wall clock and exited 0, its
twenty-nine `check 23` lines being informational rows about other builds' dispatch windows
(`dRetiredFork`, `aClosedDocket`) and none a refusal. One figure from that run bears on T5 and T6:
the checker's bar join examined 0 tokens in 0 live specs, because `SPEC_DIRECT_CUTOFF` reads
`2026-09-15` and the 27 pre-cutoff live specs that carry a bar token are declared not graded; the
`BAR` divergences above therefore reach a live spec from tomorrow, and reach this tip only through
the suite's parity arm. The hook was exercised as a program: twenty-two payloads on stdin at
REVIEWING, and the exit codes above are theirs. It did not re-open the three refuted findings. It
did not grade the records under `memory/builds/aDeferredBar/` beyond the lines T2 and T5 cite in
spec 3 rev-7 §3 and spec 2 rev-6 §9. No finding names a red at HEAD; all nine were found by feeding
the predicates the populations their headers claim, which is the method rounds 1 and 2 used, and the
one that keeps finding the fold certifying itself.

**Disposition.** Fold T1 first and alone: flip the R13 control arm before touching the walker, so
the defect is observed RED by the arm that certified it. Then T4, T7 and T8 as one edit to
`buildCommandView` and the recursion depth with their arms; T2 and T3 as one edit to the PowerShell
side, carrying `tool_name` into the walker; T5 and T6 as one edit to the two grammars and the two
`BAR` slots, with the shared fixture file both suites read; T9 is one moved line. Re-review the FIX,
not the diff again, per the method, and keep the fold's own arms and comments in scope: five of nine
this round were the fix asserting what its code does not do, and the count is not falling.
