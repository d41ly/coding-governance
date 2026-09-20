**Serves:** diff-review TOOL-aDeferredBar-1 TOOL-aDeferredBar-2 TOOL-aDeferredBar-3

# aDeferredBar — closing diff review of the three-unit build, round 2

*Node `a`, 2026-09-14, unattended. Round 2 reviews the FIX, not the diff again: the five fold
commits round 1's disposition asked for, the records commit that carried their left-shifts, and
nothing that round 1 already graded. Four primed finder lenses, five batched skeptic passes prompted
to REFUTE every finding, one synthesis. Every exit code and count below was re-run on this tree
during synthesis — `python tools/memory-tree/check-arms.py --check` on the clean tip, the suite's own
launcher grep over `unattended.sh` at HEAD and at the round-1 base, the `--selftest` population of
`tools/gate-legs.json` with its ceilings, and thirteen commands fed to `tools/unattended/gate-guard.js`
on stdin as Bash and PowerShell tool-use payloads with this worktree's `cwd` while its `RUN.md` reads
`phase: REVIEWING` — and the figures are what those runs printed. The security model is read as
given: the hook is a textual, fail-open hygiene guard, exactly as `tools/hooks/scratch-guard.js` says
of itself; a runtime-assembled path walks past it by design. No finding below argues with that
ceiling.*

**Reviewed range:** `9a47292d...HEAD`, HEAD being `19814c77`. Base `9a47292d` is round 1's recorded
tip. In range: the round-1 record commit `082da5cd`, the five fold commits `8b5b3f0c` (F1, the
ratchet row), `50c4418a` (unit 2: F2 F9 F3 F4 F10), `8b8d70b7` (unit 2: the two fixture-token
markers), `bb85cbfe` (unit 3: F2 F5 F6 F7 F8 F11) and `5ac7d1aa` (unit 3's records), and one records
commit `19814c77` carrying five backlog rows. **Round: 2.**

## Verdict: CLEAN WITH FIXES

No blocker, three highs, seven mediums, seven lows, after consolidating the twenty-six confirmed
arrivals into the seventeen distinct defects below. Two of the highs are deterministic reds at HEAD
— `check-arms.py`, an unguarded `subject = repo` bar leg, prints five lines and exits 1; and the
driver's own suite, deferred to VERIFYING by design, fails at its source-level "no python launcher"
arm on the two lines the F3 fold added — so the fold is not optional and the loop stays open. They
are highs and not blockers by the rule round 1 set: the review adds nothing by holding the loop on a
defect a machine already refuses, and each is cleared by a small, well-defined edit; severity
follows the shape of the fix, not the colour of the bar. The third high is the residue of round 1's
F2: both parity arms drop every `--selftest` leg by rule, without announcing it, and the population
they certify as "every whole-suite selftests leg" is silently short by eight, one of them a suite
the ledger records at 599 s.

What round 2 finds is otherwise of one kind: the round-1 fix gated the INSTANCE the finding named
and left the sibling standing — one cutoff key of two, one `$env:` spelling of three, one launcher
list that omits the spelling this repo's own resolver falls back to, one `$( )` form of two — and
in three places the fix's own arm or comment now certifies coverage the code lacks.

**Review shape.** Raw 28, confirmed 26, refuted 2, unverified 0, precision 0.93. The twenty-six
confirmed arrivals collapse to seventeen: the `$env:` regex arrived three times (ids 6, 14, 26), the
adopter's remedy three times (3, 17, 25), the `py` launcher three times (4, 11, 21), the raw kept
span twice (1, 27), the string tail after a span twice (5, 16), and the legline cutoff twice (2, 15).
The harness itself dropped no duplicate; the collapse is this synthesis.

**Run integrity.** Lenses 4/4 returned, 0 DIED; skeptic batches 5/5 returned, 0 DIED; 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates dropped by the harness.
The finding set is therefore complete for what four lenses can reach, and a zero below is evidence
within that coverage rather than an artefact of a dead lens. The one zero worth naming: no finding
landed on the re-keyed ratchet rows in `tools/install-prefix-carried.txt`, and
`check-install-prefix.sh` was not re-run here; that zero rests on the lenses, not on a leg.

## Findings, severity-ranked

| # | Sev | Where | Defect |
|---|-----|-------|--------|
| R1 | HIGH | `tools/unattended/unattended.sh:4713`, `memory/project/unarmed-branches.txt:68`, `:72` | Three `fail 49` refusals inserted mid-`verb_dispatch` renumber check 49's ordinals; two pin rows now pin the wrong branches, two test patterns omit the signatures; `harness arms` is RED at HEAD, five lines |
| R2 | HIGH | `tools/unattended/unattended.sh:4718`, `:4720`, `tools/unattended/unattended.test.sh:2282` | The F3 fold adds a python launcher to the driver; the suite's pre-existing "no python dependency" arm is green at base and RED at HEAD on both lines, unreconciled |
| R3 | HIGH | `tools/unattended/gate-guard.test.sh:142`, `tools/check-spec-tokens.test.sh:385` | Both parity arms drop every `--selftest` leg by rule and silently; eight legs are missing from the certified population, `corpus_ids.py --selftest` at ceiling 2690 s among them, and the hook admits it at BUILDING |
| R4 | MEDIUM | `tools/unattended/gate-guard.js:228` | `FLAG_RE` reads only lowercase glued `$env:NAME=`; `$Env:`, `$ENV:`, `${env:…}` and `$env:NAME = 1` all run the flagged bar under the PowerShell tool and print rc=0 |
| R5 | MEDIUM | `tools/unattended/gate-guard.js:139` | The kept `$( … )` span is copied into the view RAW: quoted strings inside it stay visible and quoted parens count toward depth, so a grep target or a printf argument is read as a command — false DENY on legitimate count and log lines |
| R6 | MEDIUM | `tools/unattended/gate-guard.js:202` | After a kept span, the rest of the same double-quoted string is its own segment whose view is blanks plus the closing `"`, so the heredoc skip does not fire and its tokens are read as a command — false DENY on `echo "$(date) <suite>"` |
| R7 | MEDIUM | `tools/check-spec-tokens.py:257`, `:341` | The F10 ISO refusal covers `SPEC_DIRECT_CUTOFF` only; `SPEC_LEGLINE_CUTOFF="2026-9-8"` is armed by the same string compare, prints as set, and grades nothing |
| R8 | MEDIUM | `tools/unattended/unattended.sh:4720`, `:4724` | `_stpy=python3` is EXECUTED on the adopter layout, where `python3` may be the MS-Store stub; every `--dispatch` then refuses with the "checker reds over the live tree" diagnosis and an empty tail |
| R9 | MEDIUM | `tools/unattended/adopt-unattended.sh:361` | The event resolver keeps the LAST `"Key":[` of the previous flattened line, so a matcherless first group hides its event and the group after it inherits `PreToolUse`; the repo's own `SessionStart` shape prints `wired` for a misfiled marker |
| R10 | MEDIUM | `tools/unattended/adopt-unattended.sh:357`, `:368` | The UNWIRED remedy omits `$SJ`, so on the out-of-tree layout F5 exists for it writes the in-tree decoy; a declared `GOV_SETTINGS_JSON` that is not a file reads as UNWIRED where `check-wiring.sh` REFUSES |
| R11 | LOW | `tools/check-spec-tokens.py:260` | The ISO refusal checks the SHAPE, not the date: `2026-13-45` and `2026-19-14` pass and arm |
| R12 | LOW | `tools/unattended/gate-guard.js:281`, `tools/check-spec-tokens.py:116` | Neither reader knows `py`, the third candidate `tools/lib/resolve-python.sh` returns; after F7 the two readers also disagree on `-u` and `timeout -k` while spec 2 rev-5 calls them one rule |
| R13 | LOW | `tools/unattended/gate-guard.js:139` | Only the `$(` spelling is kept inside double quotes; the backtick substitution stays blanked and `printf "%s" "`bash <suite>`"` prints rc=0 |
| R14 | LOW | `tools/unattended/gate-guard.js:277` | The timeout grammar skips a value after `-k`/`-s` only; `--kill-after 5 120 bash <suite>` makes `120` the head and prints rc=0 |
| R15 | LOW | `tools/unattended/adopt-unattended.test.sh:98` | Arm 1a's five UNWIRED expectations read the fixture's `.claude/settings.json` only because `GOV_SETTINGS_JSON` happens to be unset; the adopter now honours it and the suite never clears it |
| R16 | LOW | `tools/unattended/unattended.test.sh:5471`, `:5500`, `tools/unattended/gate-guard.test.sh:323` | Floors rose by six for five assertions; "six" is stated in two comments and two spec lines; the gate-guard comment credits F2 with four arms where five execute |
| R17 | LOW | `tools/unattended/kit.toml:87` | `optional_keys` omits the new `SPEC_TOKENS_CLI`; the conf, the example and the protocol row name "the memory-tree kit's checker", which no kit ships |

## R1 — three inserted refusals renumbered check 49, and the unguarded leg is red (HIGH)

`python tools/memory-tree/check-arms.py --check` on the clean tip exits 1 with exactly five lines:
branch 17 (`--dispatch: SPEC_TOKENS_CLI names a file that is not there…`) and branches 21 and 22
(the two order-gate refusals) have no positive assertion and are not pinned; rows 72 and 68 of
`memory/project/unarmed-branches.txt` pin branches 18 and 19 "with a stale signature — the message
was reworded". Nothing was reworded. The F3 fold at `50c4418a` inserted three `fail 49` calls into
`verb_dispatch` above the order gate, so every branch after them moved up by three; the pin rows are
keyed by ordinal and now name the new refusals under the old branches' signatures, while the
order-gate branches they described sit at 21 and 22 unpinned. The two refusals `unattended.test.sh`
does assert omit the signature `check-arms` keys on — the `--dispatch: ` prefix on the missing-file
line and the trailing ` (` on the reds line — so the arms that exist certify nothing the leg can
see. `tools/gate-legs.json`'s `harness arms (fail branches armed or pinned)` row is `subject: repo`
with no guard, so it runs on every bar and the lander reds on this tip. This is the ordinal-keyed
pin class the memory note "install-prefix waivers are line-keyed" already records, one file over.

- **Fix.** Re-key the two pin rows 18→21 and 19→22. Make the two `unattended.test.sh` patterns
  carry the full signatures: `--dispatch: SPEC_TOKENS_CLI names a file that is not there, so the
  spec-token check would pass by running nothing` and `…and the unit would build against it (`.
  Pin branch 18 (no usable python launcher) with its reason — `resolve_python` cannot be made to
  fail from the fixture without hiding python from PATH. Re-run `check-arms.py --check` to exit 0.
- **Left-shift.** The leg caught it, which is the gate working; what let it reach the record is that
  the fold ran no bar and no direct check. The unattended fold step should run every unguarded
  `subject = repo` leg whose ceiling is under a declared direct-check bound before it records the
  fold — a set DERIVED from the manifest, not typed into the protocol — so a records-only red is
  observed by the run that made it rather than by the lander. The longer fix is the class: pin rows
  keyed by signature rather than by ordinal, which `check-arms` already half-does (it reports the
  stale signature) and could finish by matching on the signature alone.

## R2 — the driver grew a python dependency and its own suite says it must not (HIGH)

`tools/unattended/unattended.test.sh:2279-2283` greps `unattended.sh` for
`(^|[^-[:alnum:]])(python3?|py) ` outside column-0 comments and FAILs on any hit, under a comment
stating the premise: every other kit carries the resolver because it needs python, and this one does
not. Ran that grep on this tree: at HEAD it hits lines 4718 (the message text `no usable python
launcher resolves`) and 4720 (`_stpy=python3   # gov:literal-python`); at `9a47292d` it hits
nothing. `git diff 9a47292d..HEAD -- tools/unattended/unattended.test.sh` touches the F3 block and
the floors and leaves this arm as it was. The suite is owed for kit work by the DoD and deferred to
VERIFYING by design, so the main loop's first verdict on this branch is a certain FAIL at an arm
whose premise the fold made false — the amendment-leaves-its-other-half-standing class round 1's
gotcha recorded, on the fix that recorded it. Deleting the arm blindly and leaving it are both wrong:
the driver now does invoke a launcher, and the arm's job becomes asserting it is the RESOLVED one.

- **Fix.** Reconcile the pair deliberately. Carry the marker-delimited `# >>> resolve_python` block
  INLINE in `unattended.sh` — byte-identical, which `resolve-python.test.sh` already gates — invoke
  the checker as `"$_stpy"` only, and delete the bare `python3` fallback (R8 is the same edit).
  Rewrite the arm at `:2282` to exclude the `>>> … <<<` block and assert that the only launcher
  spelling left in the driver is the resolved variable. Observe the arm RED on the current `:4720`
  before the change, green after.
- **Left-shift.** The arm is source-level and fixture-free — a grep over one file, seconds — and
  nothing but its home in a 20-minute suite kept it from running during BUILDING. Split the
  driver's SOURCE-level arms (this one, the `trusted_base` guard above it, the syntax check) into a
  direct check the hook admits, so a fold that changes the driver's shape runs them before it
  records itself; the suite keeps them too, so nothing is lost at VERIFYING.

## R3 — the parity arms certify a population they silently trimmed (HIGH)

Both arms derive the `chunk = selftests` population from `tools/gate-legs.json` and drop every argv
carrying `--selftest` by rule (`gate-guard.test.sh:142`, `check-spec-tokens.test.sh:385`), on the
premise the corpus record's Reading 3 states — that the flag form is the seconds-long direct check
the hook admits — and Reading 3 in turn defers the flag form's admission to "the parity arms", which
assert nothing about it. Read the manifest: eight `--selftest` legs are `chunk = selftests`, and
`python3 tools/memory-tree/corpus_ids.py --selftest` is declared at ceiling 2690 s with the ledger
at 599 s (`gen_build_index.py --selftest`: 350 s, 89 s). Fed to the hook at REVIEWING on this tree,
`corpus_ids.py --selftest` exits 0: the head token matches neither `.test.sh$` nor `selftest.py$`.
Unlike `PARITY_EXEMPT`, the flag-form skip prints nothing, so the green line "every whole-suite
selftests leg … is a hit ($popn legs, 1 exempt)" is emitted over a population that is eight short,
and a ten-minute suite walks past the hook at BUILDING under the mandate this build exists to
enforce. Spec 3's D4 row says the arm "derives every `chunk = selftests` argv … asserts each is a
hit, one exemption announced", which the arm does not do. The skeptic's correction stands: this is
not the longest-ceilinged python suite (govkit's `selftest.py` at 11750 s and memory-recall's at
2730 s are higher, and both ARE hits); it is the longest one the arm hides.

- **Fix.** Exclude by ceiling, not by flag. Keep `--selftest` legs in the population; exempt only
  those whose manifest `ceiling` is at or under a declared direct-check bound (120 s reads right
  against the ledger); print every exemption with its ceiling; red on any excluded leg above the
  bound. That red then forces `corpus_ids` and `gen_build_index` onto a `selftest.py` entrypoint the
  textual D4 rule already denies — the hook cannot read the manifest and should not. Amend
  Reading 3 and the spec-3 D4 row to say what the arm asserts.
- **Left-shift.** The class is "a skip that looks like a pass" (§7), and the arm already knows how
  to announce one — `PARITY_EXEMPT` is printed and asserted live. Make the ceiling bound the ONE
  exemption rule and delete the flag rule, so there is no unannounced skip left to grow. A one-line
  assertion that `popn` plus the printed exemptions equals the manifest's `chunk = selftests` count
  closes the shape for good.

## R4 — one `$env:` spelling of at least three (MEDIUM)

`FLAG_RE` at `gate-guard.js:228` is `/^(?:\$env:)?(GATE_FULL|GATE_SELFTESTS)=(.*)$/`: case-sensitive
on `env`, no brace form, `=` glued inside one token. Fed to the hook under `tool_name: PowerShell`
on this tree: `$env:GATE_SELFTESTS=1; bash tools/run-gates/run-gates.sh` exits 2 naming the flagged
bar; `$Env:GATE_SELFTESTS=1; …` and `$env:GATE_SELFTESTS = 1; …` exit 0, and the skeptics added
`$ENV:GATE_FULL=1;` and `${env:GATE_FULL}=1;` to the rc=0 set. PowerShell drive names are
case-insensitive, `$Env:NAME = value` is the documented spelling, and a skeptic ran all three under
`pwsh -NoProfile` with a bash child that printed the variable, so each reaches the bar. The comment
at `:225-227` and spec 3 rev-6 §3 (line 81) both rest on `$env:NAME=value;` being "that tool's ONLY
spelling of the act", which is false in exactly the way the regex keys on it. The corpus holds no
`$env:` spelling at all, so reachability is by the wired tool rather than by observed use; the hook
is wired on `Bash|PowerShell` precisely to cover it.

- **Fix.** `const FLAG_RE = /^(?:\$\{?[Ee][Nn][Vv]:)?(GATE_FULL|GATE_SELFTESTS)\}?=(.*)$/` for the
  case and brace forms; for the spaced form, in `scanDenyHits` before the `FLAG_RE` test: when a
  token matches `^\$\{?[Ee][Nn][Vv]:(GATE_FULL|GATE_SELFTESTS)\}?$` and `toks[k+1] === '='` with a
  non-empty `toks[k+2]`, push the D1 hit and advance three. Arms: `$Env:GATE_SELFTESTS = 1; bash
  <bar>` deny, `$Env:GATE_FULL = ""; bash <bar>` allow, observed rc=0 first. Amend the comment and
  the spec-3 §3 sentence to "spellings".
- **Left-shift.** The F8 arm tested the one spelling the fix was written against. A table-driven
  arm — every `(casing × brace × spacing)` product of the assignment, each asserted deny — is a
  loop over nine strings and cannot be satisfied by the instance again.

## R5 — the kept span is raw, so a quoted argument inside it is a command (MEDIUM)

`buildCommandView` at `gate-guard.js:139-149` copies the `$( … )` span verbatim into the view,
counting every paren toward depth and blanking nothing inside. Two consequences, both reproduced on
stdin at REVIEWING. A `(` inside a single-quoted argument splits the segment there, `readTokenAt`
opens a quote at the stray `'` and reads the rest — a grep TARGET — as the command head: `echo
"$(grep -c 'foo(' tools/x.test.sh)"` exits 2 with `suite:  tools/x.test.sh`, the leading space being
the crossed quote, and the lens observed the live form `echo "n: $(grep -c 'n=\$((n+1))'
tools/unattended/unattended.test.sh)"` blocked the same way while reviewing this very diff. A
separator inside a quoted argument does the same: `git commit -m "$(printf '%s' 'fix; bash
tools/x.test.sh')"` is a D4 hit. Base `9a47292d` allowed all of them because the whole double-quoted
body was blank. The header's contract at `:41-42` — a grep argument is invisible by construction of
the view — is false for this shape, and a build agent denied on a legitimate count line learns to
route around the hook. The mirror image, a quoted `)` inside the span closing it early and blanking a
real run (`echo "$(: ')'; bash tools/x.test.sh)"` exits 0), is the textual ceiling and not new, but
the same fix closes it.

- **Fix.** Blank the span body recursively before keeping it: walk from the `(` quote-aware, count
  only unquoted parens toward depth, and append `'$(' + buildCommandView(inner) + ')'` to `keep` —
  length-preserving, so offsets still line up. Arms: `echo "$(grep -c 'foo(' <suite>)"` allow and
  the printf commit form allow, each observed rc=2 first; the quoted-`)` deny arm beside them.
- **Left-shift.** The view has a property the header states and no arm measures: for every deny
  payload P in the suite, the pure MENTION `echo "P"` with no substitution must allow. Derive that
  arm from the deny list rather than writing mentions by hand, so a new deny shape gets its mention
  control for free and a view regression on quoting shows up as a batch of false denies.

## R6 — the string tail after a kept span is read as a command (MEDIUM)

Once a span is kept, its `)` is a segment separator in the view (`:216`), so the remainder of the
double-quoted string up to the closing `"` forms its own segment. Its view is blanks plus the quote
mark; `:202`'s skip fires only when the view is all-blank, so `readTokenAt` reads the ORIGINAL bytes
as a command. Reproduced on stdin: `echo "$(date) tools/x.test.sh"` exits 2 naming
`suite: tools/x.test.sh`, and the skeptics added `printf "%s\n" "$(git log -1 --format=%h) bash
tools/x.test.sh"` and `msg="$(head -1 f) GATE_SELFTESTS=1 held"; git commit -m "$msg"` (D1) to the
rc=2 set, all rc=0 at base. The control `echo "a tools/x.test.sh"` still allows, isolating the
regression to the kept span. A second shape in the class: `echo "$(date)" bash tools/x.test.sh` hits
with token ` bash tools/x.test.sh`, read through an unclosed quote. Distinct from R5 — this is text
after a correctly closed span — though scanning the span body as a sub-command the way D5 does
closes both.

- **Fix.** Either the R5 recursion (which turns the tail back into content) or, cheaper and
  independent, one more skip after `:202`: a segment whose view has nothing but whitespace and quote
  marks and whose original does not OPEN with a quote is the tail of a string, not a command
  (`!/[^\s"']/.test(view.slice(s, e)) && !/^\s*["']/.test(cmd.slice(s, e))`). A skeptic verified
  that predicate on a scratch copy: all eight false-deny and control payloads allow, every F7/F2/F8
  deny arm still exits 2, and the fully-quoted head `"tools/x.test.sh"` still denies. Add the three
  payloads as allow arms beside the F7 denies.
- **Left-shift.** Same derived mention-control arm as R5.

## R7 — the ISO refusal gated one cutoff key of two (MEDIUM)

`check-spec-tokens.py:260` refuses a non-ISO `SPEC_DIRECT_CUTOFF`. `SPEC_LEGLINE_CUTOFF` is read by
the same `read_conf_key` three lines up (`:257`), armed by the same `>=` string comparison at `:341`,
and printed as set at `:419` with no validation at all. `'2026-09-14' >= '2026-9-8'` is False in
Python, so `SPEC_LEGLINE_CUTOFF="2026-9-8"` is truthy, arms nothing dated 2026-0x, and reports on the
summary line as set — the announced-zero shape F10 named, one key over. A skeptic wrote the value
into `.memory-tree.conf`, ran the checker, watched it exit 0 printing `SPEC_LEGLINE_CUTOFF 2026-9-8`
as set over zero graded specs, and restored the conf. The module docstring at `:52-54` now claims
without qualification that a cutoff that is not an ISO date refuses, so the header certifies coverage
the sibling key lacks — the instance gated, not the class (§7).

- **Fix.** One helper applied to both keys before either comparison — in `read_conf_key` itself, or
  a loop over the two — refusing any set value that is not a date and naming the key. With R11 folded
  into it, that helper is `datetime.date.fromisoformat` in a `try`. Arm: `SPEC_LEGLINE_CUTOFF=
  "2026-9-8"` → `REFUSING`; raise the floor by one.
- **Left-shift.** The two keys are read, compared and printed by three pieces of code each; a
  single `cutoffs = {KEY: validated_value}` built once and consumed everywhere leaves no second key
  to forget.

## R8 — the adopter-layout fallback executes the one launcher the resolver exists to avoid (MEDIUM)

`unattended.sh:4715-4722` sources `$KIT_DIR/../lib/resolve-python.sh` when it exists and otherwise
assigns `_stpy=python3` under a `gov:literal-python` marker — then EXECUTES it via
`run_bounded "$_stpy" "$SPEC_TOKENS_CLI"`. Every other marked site in the tree (`check-wiring.sh:183`,
`adopt-codebase-map.sh:93`, `adopt-lexicon.sh:109`, `adopt-memory-recall.sh:144`) and the exemption's
own definition in `resolve-python.test.sh` ("a launcher NAME printed or rendered rather than
executed") cover names that are never run. `tools/lib` is a registry exemption that ships nothing
(`registry.toml:164`: the canonical block was inlined into every shipped file that had one), so an
adopter ALWAYS takes the literal branch — the resolver's own header says shipped scripts inline the
block for exactly this reason. On a Windows adopter `python3` is the MS-Store stub that exits 9009
without running anything; the non-zero lands in the `:4724` message "the declared spec-token checker
reds over the live tree, so a live spec names a bar…" with an empty tail, because the grep over
`RB_OUT` finds no `spec-tokens:` line. Every `--dispatch` is then refused with the wrong diagnosis,
and no arm exercises the branch, so the suite cannot see it. One premise is overstated and the
skeptic said so: three sibling SUITES carry the identical executed `TESTPY=python3` fallback and
`resolve-python.test.sh:149` names that class as sanctioned — but those are withheld from adopters,
whereas the driver ships and this is its only adopter path.

- **Fix.** The R2 edit: inline the canonical block, invoke `"$_stpy"` only, delete the fallback.
  Separately, make the `:4724` refusal distinguish "the checker did not run" (no `spec-tokens:`
  line in `RB_OUT`: name the rc and the first stderr line) from "the checker graded and found a hit".
- **Left-shift.** An arm that runs `--dispatch` with `../lib/` moved aside and a `python3` shim on
  PATH that exits 9009, asserting the refusal names the launcher and not the tree. It is the fixture
  the resolver's own suite already builds for the stub; reuse it.

## R9 — a matcherless first group hides its event from the resolver (MEDIUM)

The awk at `adopt-unattended.sh:359-366` keeps the LAST `"Key":[` of the previous flattened line and
leaves `ev` unchanged when that key is `hooks`. An event whose first group is matcherless —
`"SessionStart":[{"hooks":[…]},{"matcher":…` — is therefore never seen: its `"hooks":[` is the last
key, `ev` stays `PreToolUse`, and the matcher group after it inherits the previous event. A skeptic
ran the awk verbatim over `{"PreToolUse":[{"matcher":"Bash|PowerShell","hooks":[scratch-guard]}],
"SessionStart":[{"hooks":[check-wiring]},{"matcher":"Bash|PowerShell","hooks":[gate-guard.js]}]}`
and it printed `wired`; the same marker misfiled directly under `PostToolUse`, or under
`SessionStart` with the matcher group FIRST, prints nothing. The real `.claude/settings.json` has
two matcherless `SessionStart` groups, so the shape is the repo's own. Arm 1a
(`adopt-unattended.test.sh:104-109`) covers `PostToolUse`-direct and the wrong matcher, not this.

- **Fix.** Track the last NON-hooks key inside the loop — `if (key != "hooks") ev = key` — and
  drop the post-loop `if`. Arm: the marker under `SessionStart` behind a matcherless group, observed
  `wired` first on the current awk, then nothing.
- **Left-shift.** This is the second resolver of the same JSON (`check-wiring.sh` has the first),
  and backlog row TOOL-aDeferredBar-7 already records the two-resolver problem. One resolver — a
  python one-liner over the parsed file, which every adopter has because the kit now resolves
  python anyway — replaces both awks and cannot mis-parse a shape the JSON parser sees correctly.

## R10 — the remedy names the wrong file, and a typo reads as a wiring gap (MEDIUM)

`adopt-unattended.sh:356` resolves `SJ=${GOV_SETTINGS_JSON:-$ROOT/.claude/settings.json}` and `:367`
names `$SJ` in the diagnosis, but the remedy at `:368` is `python …/settings-merge.py --fragment
…/gate-guard.fragment.json` with no settings path. `settings-merge.py` takes the file as a
positional defaulting to `.claude/settings.json` (`:422`) and reads no `GOV_SETTINGS_JSON` (grep:
none), so for the out-of-tree layout F5 was folded to support, following the printed remedy writes
the in-tree decoy `check-wiring.sh:52-56` warns about while `--check` keeps reading the declared path
and reds again — a wedge with a wrong instruction, handed to the one operator the fix exists for.
Separately, a declared `GOV_SETTINGS_JSON` that is not a file falls through `[ -f "$SJ" ] &&` at
`:357` to empty `GG_WIRED` and the same UNWIRED text, where `check-wiring.sh:66-68` — the resolver
this arm's comment claims to mirror — prints `REFUSED — GOV_SETTINGS_JSON names …, which is not a
file`. Three lenses reproduced both halves. Arm 1a's `:113` covers only the wired out-of-tree case.

- **Fix.** Refuse a declared non-file first, in `check-wiring`'s wording, before the wiring read;
  append `"$SJ"` as the positional to the remedy whenever it is not the in-tree default. One arm
  each: the unwired out-of-tree case asserting the remedy names `$SJ`, and the missing-file case
  asserting REFUSED.
- **Left-shift.** The remedy is a string the check prints and never runs. An arm that RUNS the
  printed remedy against the fixture and re-checks for `wired` turns the instruction into an
  observation, and would have caught this on the fold.

## R11 — the ISO refusal checks a shape, not a date (LOW)

`re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", …)` at `check-spec-tokens.py:260` admits `2026-13-45`,
`2026-00-10`, `2026-02-30`. A fat-fingered month (`2026-19-14` for `2026-09-14`) passes the refusal,
is "strictly past" every commit date, matches no spec filename, and a skeptic watched the bar join
print `0 token(s) examined in 0 live spec(s) at/after SPEC_DIRECT_CUTOFF 2026-19-14` while a spec
carrying `GATE_SELFTESTS=1 bash run-gates.sh` went ungraded — set while grading nothing, the F10
class the comment above the regex says is refused. `datetime.date.fromisoformat` rejects all four
values and `2026-9-15` too.

- **Fix.** Replace the regex with `datetime.date.fromisoformat` in a `try`/`except ValueError`; the
  message already says "not an ISO date". With R7, one helper for both keys. Arm: `2026-13-45`
  beside the `2026-9-15` one.
- **Left-shift.** Covered by R7's single validated `cutoffs` table.

## R12 — neither reader knows `py`, and the two readers no longer agree (LOW)

`gate-guard.js:281` accepts `python`/`python3` as a launcher; `BAR` at `check-spec-tokens.py:116`
has `python3?\s+`. `tools/lib/resolve-python.sh:30` lists `py` as its third candidate — the Windows
launcher, the one a node falls to when the MS-Store `python3` stub shadows the real one, and the one
the kit is wired on PowerShell to meet. Fed to the hook at REVIEWING: `py tools/govkit/selftest.py`
exits 0 while `python tools/govkit/selftest.py` exits 2; `BAR.search` is False and True on the same
two strings. So the kit's own launcher list disagrees with both its predicates, and a node whose only
launcher is `py` has the 3445 s govkit suite walk past the hook under the spelling the resolver would
itself print. The skeptic's caveat stands: the resolver falls to `python` before `py`, so the gap is
real but narrower than every Windows node, and no corpus run spells `py`. Second half: after F7 the
hook denies `python -u <selftest.py>` and `timeout -k 5 120 bash <suite>` where `BAR` misses both,
while spec 2 rev-5 (lines 153-160) presents the two readers as one rule with a parity arm each.

- **Fix.** `t === 'py'` (and `/^python3\.\d+$/`) in the launcher branch; `py\s+` in `BAR`'s
  launcher group; one deny arm and one `BAR` case. Either give `BAR` the option and timeout-option
  slots the hook grew at F7, or drop the "same rule" sentence from spec 2.
- **Left-shift.** The launcher set exists in one place already — the resolver's candidate list.
  Derive the readers' launcher alternation from it (a marker-delimited render, byte-gated like the
  block itself) rather than restating it twice by hand. For the reader parity, one shared payload
  table both suites feed to their reader and assert the same verdict on, so a shape one reader grows
  reds the other's arm.

## R13 — the backtick substitution stays blanked (LOW)

The F7 departure at `gate-guard.js:139` keys only on `$(`. A backtick inside double quotes is a
command in bash just the same, and stays content to the view: `printf "%s" "`bash tools/x.test.sh`"`
exits 0 at REVIEWING while `printf "%s" "$(bash tools/x.test.sh)"` exits 2 and the unquoted
`echo `bash tools/x.test.sh`` is a hit. Same class the header names as the deliberate exception, one
spelling short. Backticks are rare in agent-typed commands, hence low.

- **Fix.** In the same branch, a backtick inside a double-quoted string opens a kept span to the next
  backtick, blanked recursively as R5 does for `$(`; `scanSegments` already honours the backtick
  separator. One deny arm.
- **Left-shift.** R5's derived mention-control arm, plus one deny arm per substitution spelling
  bash has — there are two.

## R14 — the timeout grammar skips a value after the short flags only (LOW)

`gate-guard.js:277` skips a value after `-k`/`-s`; the space-separated long forms `--kill-after N`
and `--signal SIG` are consumed as bare flags, their value is taken as the duration at `:280`, and
the real duration becomes the head. Reproduced: `timeout --kill-after 5 120 bash tools/x.test.sh`
exits 0 while `--kill-after=5`, `-k 5` and `--foreground` forms exit 2. GNU timeout documents both
long spellings.

- **Fix.** `/^(-[ks]|--kill-after|--signal)$/` in the value-taking test. One deny arm per long form.
- **Left-shift.** None beyond the arms; the grammar is three lines and now names every value-taking
  option GNU timeout has.

## R15 — arm 1a inherits the machine's `GOV_SETTINGS_JSON` (LOW)

`adopt-unattended.sh:356` now prefers `GOV_SETTINGS_JSON` over the fixture's `.claude/settings.json`,
and `adopt-unattended.test.sh` never unsets or overrides it — `:113` sets it for one arm and the
other five expectations in arm 1a (moved-aside `:98-101`, `PostToolUse` and wrong-matcher
`:103-109`, arm 1's `--check` at `:84`, the restored-tree arm at `:122`) edit the fixture file while
the adopter would grade the ambient path. On a node exporting a wired real file the UNWIRED
expectations flip to rc=0 and FAIL; on one exporting an unwired file the moved-aside case
false-passes. That node is the population F5 exists for, and its shell necessarily exports the
variable because that is how the resolver reads it. The sibling `check-wiring.test.sh` shares the
exposure, which makes this a class rather than a refutation. The suite could not be run here (the
hook denies it at REVIEWING); the behaviour follows from `:356` and the suite's own `:113`.

- **Fix.** `unset GOV_SETTINGS_JSON` at the top of arm 1a, keeping `:113` as its only reader; the
  same line in `check-wiring.test.sh`.
- **Left-shift.** Every suite that exercises a resolver reading the environment should start from a
  scrubbed one: a shared `env -i`-style preamble in the suites' common header, or a one-line
  `check-testsuite-counts`-style assertion that a suite naming `GOV_` in its subject also unsets it.

## R16 — the floors credit six for five, and three records say six (LOW)

The F3 block at `unattended.test.sh:4166-4192` carries five `n=$((n+1))` lines (refuses, `[bar]`,
announces, still declares, missing path) and `git diff 9a47292d..HEAD` adds exactly five arms and
removes none, yet `FLOOR_ASSERTIONS` went 706→712 (`:5471`) and `FLOOR_SHARD_2` 510→516 (`:5500`),
and "six" is stated in both floor comments and in spec 2's S11 line (426) and §7 New-arm line (689).
A floor one above its count eats a unit of the declared headroom silently. `gate-guard.test.sh:323`
credits F2 with four arms ("selftest.py deny, --selftest flag allow, two parity assertions") where
five execute — `check_names "F2 selftest.py"` counts. Every stated count is wrong in the direction
the prose-count class §7 bans.

- **Fix.** Either 711/515 or leave the floors and correct every "six" to "five"; correct the
  gate-guard comment to five (103 stays valid as a shrink-only floor under a 104 static count).
- **Left-shift.** `check-testsuite-counts.sh` grades the floor against the count; nothing grades the
  COMMENT beside the floor against the diff that moved it. Drop the per-fold count from the comment
  — the floor's git history carries it — so there is no second number to be wrong.

## R17 — the descriptor does not declare the key the driver reads (LOW)

`tools/unattended/kit.toml:87` `optional_keys` ends at `RECALL_CLI`, `MAP_CLI`; `SPEC_TOKENS_CLI` is
read by the driver (`unattended.sh:291`, `:4712`) and declared in `.unattended.conf:84`, the
example (`:89`) and both protocol copies (`:482`), none of which the descriptor lists, and spec 2
S11's register list omits the descriptor too. All three prose registers call the target "the
memory-tree kit's checker", while `tools/govkit/registry.toml:185` exempts
`tools/check-spec-tokens.py` from shipping ("grades gov's OWN corpus against gov's OWN manifest …
prescribed for copy nowhere") and no `kit.toml` under `tools/` claims it. An adopter following the
example looks for a checker no kit installs. Nothing machine-compares `optional_keys` to the
example's keys (govkit check 7 reads the lists for `requires_if` names only), so the gap is silent.

- **Fix.** Add `SPEC_TOKENS_CLI` to `optional_keys`; reword the conf, the example and the protocol
  row to say the checker is gov-only today and the key is filled only where a project carries its
  own spec-token checker.
- **Left-shift.** A govkit arm asserting every `KEY=` the example conf declares is in
  `required_keys_*` or `optional_keys` of its kit — the example is already the parity source for
  one direction, and this is the other.

## What this review did not do

It did not run the merge bar or any self-test suite, per the mandate this build exists to enforce.
The direct checks exercised were `check-arms.py --check` (seconds), the suite's own launcher grep
over the driver at two shas, a read of the manifest's `--selftest` legs with their ceilings, and the
hook as a program on stdin with thirteen payloads; `check-install-prefix.sh` was not re-run, so the
ratchet rows' clean state rests on the lenses. It did not re-open the two refuted findings. It did
not grade the records under `memory/builds/aDeferredBar/` beyond the lines R3, R4, R12 and R16 cite
in the corpus record's Reading 3, spec 3 rev-6 §3 and spec 2 rev-5. R1 and R2 are the only two
findings that name a red at HEAD; the other fifteen were found by feeding the predicates the
populations they claim to cover, which is the same method round 1 used for F2 and F8 and the reason
R3 is rated as it is: an arm built from that method that then trims its population by rule is the
one shape the method cannot see through.

**Disposition.** Fold R1 and R2 first, as one edit to the driver and its pin file — the leg and the
suite refuse everything until they move — with R8 riding the same inline-resolver change. Then R3 as
one edit to the two parity arms and the two records that describe them. R5, R6 and R13 are one edit
to `buildCommandView` plus the segment skip, with their arms; R4 and R14 are the two regexes with
theirs; R7 and R11 are one helper in the checker; R9, R10 and R15 are one pass over the adopter and
its suite; R12, R16 and R17 are the small ones and should not wait for a round of their own.
Re-review the FIX, not the diff again, per the method — and this time the fold's own arms and
comments are in scope, since three of the seventeen are the fix certifying itself.
