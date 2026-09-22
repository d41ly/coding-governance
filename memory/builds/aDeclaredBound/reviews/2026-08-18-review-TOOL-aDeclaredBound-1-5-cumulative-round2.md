# Tier-2 review — the cumulative diff landing on main, `93a0574b21408e940883b22be17b4e52aafcb209...HEAD`

**Serves:** diff-review TOOL-aDeclaredBound-1 TOOL-aDeclaredBound-2 TOOL-aDeclaredBound-3 TOOL-aDeclaredBound-4 TOOL-aDeclaredBound-5

## Verdict: BLOCKED

## Review shape

- **raw 17 · confirmed 14 · refuted 3 · unverified 0 · precision 0.82**
- Confirmed severities as rated: **0 BLOCKER · 4 HIGH · 9 MEDIUM · 1 LOW.**
- After dedupe the 14 confirmed findings collapse to **6 distinct defects: 2 HIGH, 3 MEDIUM, 1 LOW.**
  Nothing was downgraded; the duplicates are the same defect reached by separate lenses. The raw id
  set behind each defect is printed in its heading so the join back to the pipeline stays checkable.
- Every finding below survived an adversarial skeptic pass and carries a reproduction. Nothing is
  outstanding for want of a verdict.

This range is one commit — `40d8d1f`, "fix all 15 findings from the closing review". It is a
remediation round, so the question is not whether the fixes are present but whether they hold. Four
of them do. Two traded one hole for another, and that is why this reds.

The unit's premise is that a bare digit in prose is a second answer that goes stale. Round 5 removed
the gate's ability to see the *only file in this tree that still carries live bare digits* (H1), and
gave two of the four replacement parity pairs a constant that no acceptance path in the hook reads
(H2). Both gates are green over both. The exclusion's own in-file comment — "the exclusion covers
nothing that is merely unwatched" — is measurably false today, not hypothetically after some future
edit.

---

## HIGH

### H1 — the playbook exclusion is file-wide; the control it defers to is statement-wise, and covers 1 of its 4 carriers
`tools/check-agent-cap-restatement.sh:75` (raw ids 1, 6, 10) · ships to adopters via
`tools/govkit/entries/check-agent-cap-restatement.kit.toml`

`PARITY_OWNED='^parallel-coding-governance\.template\.md$'` drops the whole playbook from the scan
(line 129, `grep -zvE "$PARITY_OWNED"`), on the stated grounds that `check-playbook-parity.sh` binds
its numbers. Measured: running the gate's own `PAT` over the excluded file with the gate's own flags
(`grep -HIniE`) yields **four** carriers on two lines —

```
parallel-coding-governance.template.md:182:CONCURRENCY ≤ 5
parallel-coding-governance.template.md:182:cap-5
parallel-coding-governance.template.md:182:at most 5 verify
parallel-coding-governance.template.md:189:≤5 cap
```

Of the five `PAIRS` rows in `check-playbook-parity.sh:105-112`, exactly **one** — `verify-agent
total` (:108) — extracts one of those four. The other three digit pairs key on *different digit
occurrences on the same lines*: `array LITERAL of ≤5 elements` (:106), `boundedParallel(thunks, 5)`
(:109), `cannot resolve to an integer ≤5` (:110). None of those three is a `PAT` hit; none of the
three unbound `PAT` hits has a pair. So `CONCURRENCY ≤ 5`, `cap-5` and `the ≤5 cap` are checked by
**neither** gate and can drift from `MAX_VERIFIERS`/`MAX_LENSES`/`CAP` with the entire bar green.

Two aggravations, both self-inflicted in this same commit:

1. `cap-5` and `CONCURRENCY ≤ 5` are precisely the shapes the header comment says `REV` and `NB`
   were added to catch — and three of the six shapes frozen as must-catch fixtures at
   `tools/check-agent-cap-restatement.test.sh:96-102` (`the ≤5 cap is enforced at the Workflow
   tool-call`, `Route ALL Workflow fan-out through cap-5 helpers.`, `CONCURRENCY ≤ 5, ALWAYS`) are
   verbatim copies of the very lines the gate stopped scanning. The suite proves the gate catches
   shapes the gate is no longer permitted to look at, in the one file where they live.
2. The self-test's own `hole` arm (`check-agent-cap-restatement.test.sh:157-163`) writes a playbook
   fixture containing `cap-5`, adds one unrelated `lens-array` pair, and asserts `rc=0`. The
   condition it certifies as correct behaviour IS the defect.

**Fix.** Add declared pairs in `tools/check-playbook-parity.sh` for the three unbound digits —
`CONCURRENCY ≤ N` and `the ≤N cap` against `MAX_VERIFIERS`, `cap-N helpers` against the constant
that actually governs it (see H2) — or drop the file-wide `PARITY_OWNED` and waive the four
parity-bound sentences by TEXT in `tools/agent-cap-restatement-waivers.txt`, so a digit nobody paired
still reds.

**Left-shift gate.** Make the exclusion prove its own coverage instead of asserting it in a comment:
run `$PAT` over the excluded file and refuse unless every hit's line yields a digit under some
declared pair's stated-side extraction. That is the same "anti-vacuity, per-item" shape
`check-playbook-parity.sh` already uses for unresolvable pairs, and it turns this class from a review
finding into a leg.

---

### H2 — the two new parity pairs certify against `const CAP`, which no acceptance path in the hook reads
`tools/check-playbook-parity.sh:109` and `:110` (raw ids 5, 8)

Both new pairs name `sed -n 's/^const CAP = \([0-9]\+\).*/\1/p'` in `tools/hooks/agent-cap.js` as the
owning source. `const CAP = 5` (`agent-cap.js:55`) is referenced only in comments and in remediation
template strings (`:741`, `:776`, `:777`). **No acceptance decision reads it.** Every resolved-K
decision goes through `boundedK()` (`agent-cap.js:127-128`), which compares against `MAX_VERIFIERS`
(`:114`), and the refusal text the playbook sentence at :110 restates is `agent-cap.js:466` —
"cannot resolve to an integer at or under `${MAX_VERIFIERS}`". `:109`'s subject is the same:
a `boundedParallel(thunks, 5)` call-site width is resolved by `boundedK` against `MAX_VERIFIERS`, and
`agent-cap.js:130` names the call site as consumer S1 of "THE ONE BINDER".

Both pairs are green today only because `CAP` and `MAX_VERIFIERS` both happen to be `5`, and nothing
in the tree pins them equal — I searched; there is no such assertion, and
`check-playbook-parity.test.sh:36` writes a fixture with both at 5, so the self-test cannot
distinguish them either. Move `MAX_VERIFIERS` to 3: the playbook keeps saying ≤5, this gate reports
"pairs in agreement", and every script an agent writes from the playbook is DENIED by the hook. That
is the exact stale-second-answer class the pairs were added to close, reproduced by the pairs.

The gate's own doctrine is that a stated value must equal the source that OWNS it. Ownership is
decided by which constant changes the outcome: changing `CAP` alone leaves the playbook's instruction
still accepted; changing `MAX_VERIFIERS` makes it denied. `MAX_VERIFIERS` owns both sentences.

**Fix.** Point both owning extractions at `MAX_VERIFIERS`:
`sed -n 's/^const MAX_VERIFIERS = \([0-9]\+\).*/\1/p'`. Better and shorter: delete `const CAP`
entirely and let the three remediation strings interpolate `MAX_VERIFIERS`, so the hook carries one
enforced number instead of two that must be kept accidentally equal.

**Left-shift gate.** Nothing here is catchable by reading; it needs a mechanical owner test. Cheapest
honest one: in `check-playbook-parity.test.sh`, build the hook fixture with the two constants
**different** (`CAP = 9`, `MAX_VERIFIERS = 5`) and assert the pairs still agree with the playbook —
a pair keyed on the wrong constant reds immediately. That single fixture edit would have caught this
before the commit and costs one line.

---

## MEDIUM

### M1 — the anti-hole guard tests existence (`-ge 1`), never coverage
`tools/check-agent-cap-restatement.sh:90` (raw ids 11, 16)

```sh
_pairs=$(grep -cE '^[^~]+~\$TEMPLATE~.*\[0-9\]' "$PARITY_GATE" 2>/dev/null || true)
[ "$_excluded" -eq 0 ] || [ "$_pairs" -ge 1 ] || { …refuse… }
```

`_pairs` counts pair lines whose sed text contains the literal `[0-9]` — lines 106, 108, 109, 110 of
`check-playbook-parity.sh`, i.e. 4 today, none keyed to a specific carrier. Delete the
`verify-agent total` pair — per H1 the only one binding a carrier this gate would otherwise scan —
and `_pairs` is 3, the guard stays green, and the exclusion becomes precisely the hole its own error
text describes. Nothing else notices: `check-playbook-parity.sh`'s anti-vacuity arm only fires for
pairs that still exist but extract nothing; a *deleted* row is silent everywhere.

The deletion path is not hypothetical. Rewording that playbook sentence makes the parity gate red
with "an extraction matched NOTHING", and deleting the offending pair is the tempting one-line fix.
The comment above the guard claims "ASSERT it rather than trusting the comment"; what is asserted is
only that someone once wrote a pair. The self-test arms total deletion only
(`check-agent-cap-restatement.test.sh:163`, `# no pairs left`), so the partial case is uncovered.

**Fix.** Assert by pair LABEL, not by count: require each of `lens-array bound`, `verify-agent
total`, `bounded-helper width`, `resolved-K ceiling` to be present in `$PARITY_GATE`. Failing that,
at minimum pin the count shrink-only (`PARITY_PAIR_FLOOR=4`) in the repo's usual shape so losing any
one pair reds.

**Left-shift gate.** Add the partial-deletion arm beside the existing total-deletion one: fixture
with one pair removed, assert `rc=2`. It is four lines in a suite that already builds the fixture.

---

### M2 — `MEMORY_ROOT` is read with no quote/comment/whitespace/CR stripping and interpolated unescaped into an ERE
`tools/check-agent-cap-restatement.sh:59` (raw ids 2, 7, 12, 15)

```sh
MEMORY_ROOT=$(sed -n 's/^MEMORY_ROOT=\(.*\)$/\1/p' .memory-tree.conf 2>/dev/null | head -1)
FROZEN="^$MEMORY_ROOT/(builds|archive|gotchas|backlog)/"
```

Two failure modes, both reproduced against the live script in a scratch repo:

1. **Quoted / commented / CR-terminated value → the frozen-tree exclusion vanishes.** With
   `MEMORY_ROOT="docs/mem"` the extraction keeps the quotes, `FROZEN` becomes
   `^"docs/mem"/(builds|archive|gotchas|backlog)/`, matches no path, and every committed build,
   archive, gotcha and backlog record is scanned as a live carrier — `docs/mem/builds/rec.md` reds,
   exit 1. `MEMORY_ROOT=docs/mem   # the tree` fails identically; a CRLF-committed conf fails the
   same way on Linux. This is the precise outcome the comment at :55-58 says the read exists to
   prevent ("the gate would red an adopter's whole history on install"). Unquoted LF exits 0 clean,
   which is why the `relocated` fixture at :144 cannot see it.
2. **A `|` in the value silently SHRINKS the population.** With `MEMORY_ROOT=docs|memory`, `FROZEN`
   becomes `^docs|memory/(builds|…)/`; the top-level alternation makes `^docs` swallow the whole
   `docs/` subtree, and the gate printed `clean — 1 markdown file(s) scanned, 0 waiver(s)` and exited
   0 over a live `at most 5 agents TOTAL` carrier. The vacuity arm (:133) only fires at
   `scanned == 0`, so partial exclusion reads as green.

This reader is the only one in the repo that strips nothing. Every sibling handles it:
`check-memory-hygiene.sh:53` SOURCES the conf (bash strips quotes and comments),
`drift_report.load_conf:98-100` strips CR and surrounding quotes, `recall_conf.py:203` strips,
`adopt-drift-audit.sh:49` pipes through `tr -d '\r'` with a comment naming the CRLF-on-Linux case,
`check-wiring.test.sh:513` strips both on the identical extraction. And the grammar genuinely permits
what this breaks on: 26 of 27 keys in the shipped `.memory-tree.conf.example` are quoted,
`recall_conf.py:70-93` explicitly parses quoted values, `memory-recall/selftest.py:167` pins a
fixture with a trailing comment on this exact key, and `adopt-memory-tree.sh:41` tells the adopter to
edit `MEMORY_ROOT` by hand.

**Fix.** Match the siblings and refuse a value that is not a plain path:

```sh
MEMORY_ROOT=$(tr -d '\r' < .memory-tree.conf 2>/dev/null | sed -n 's/^[[:space:]]*MEMORY_ROOT=//p' \
  | head -1 | sed 's/[[:space:]]*#.*$//; s/^["'\'']//; s/["'\'']$//; s/[[:space:]]*$//')
: "${MEMORY_ROOT:=memory}"
case $MEMORY_ROOT in *[!A-Za-z0-9._/-]*)
  echo "agent-cap-restatement: MEMORY_ROOT '$MEMORY_ROOT' is not a plain path"; exit 2 ;; esac
```

One extra line turns a silent narrowing into a refusal.

**Left-shift gate.** Two fixture arms beside the existing `relocated` one — a quoted
`MEMORY_ROOT="docs/mem"` (assert `rc=0`, records still excluded) and a metacharacter value
(assert `rc=2`). Longer-term the repo has four hand-rolled readers of one conf grammar; a shared
`read_conf_key` in `tools/lib/` would make this class unrepeatable, but that is a follow-up, not a
condition of this merge.

---

### M3 — the AGENT_CAP remedy now says the number lives in "this file, which is the one place it is written". Both halves are false
`tools/hooks/agent-cap.js:697` and its byte-pinned copy `.claude/hooks/agent-cap.js` (raw ids 3, 17)

The diff replaced "change it in `tools/hooks/agent-cap.js` and in `memory/guides/REVIEW-PROTOCOL.md`,
where the rule is stated" with "change it in this file, which is the one place it is written". The
refusal fires first on any `Workflow`/`Agent` payload and exits 2, so it is reached exactly when an
operator is trying to raise the cap.

1. **"this file" is the wrong file.** `.claude/settings.json:9` wires
   `node "${CLAUDE_PROJECT_DIR}/.claude/hooks/agent-cap.js"`, so the copy printing this message is
   the deployed one. `tools/hooks/agent-cap.test.sh:459-469` requires the two byte-identical, names
   `tools/hooks/agent-cap.js` as the kit source, and prints the remedy
   `cp tools/hooks/agent-cap.js .claude/hooks/agent-cap.js` — so an operator who does what the
   message says and then clears the resulting red silently discards their own edit. The message
   gives no hint a kit source exists.
2. **It is not one place.** The file carries three literals that must move together (`CAP`:55,
   `MAX_VERIFIERS`:114, `MAX_LENSES`:119), and `check-playbook-parity.sh:106-110` now hard-binds four
   playbook sentences to them — changing only the constant reds the parity leg too. Worse, the
   pointer this commit deleted led to `memory/guides/REVIEW-PROTOCOL.md`, which still carries at
   least five unbound copies of the same numbers: `:92` `array LITERAL with ≤ 5 elements`, `:97`
   `a literal above 5`, `:99` `an integer literal ≤ 5`, `:118` `boundedParallel(thunks, 5)` /
   `boundedPipeline(items, 5, …stages)`, `:165` `Ratified at 5` — mirrored in
   `tools/workflows/REVIEW-PROTOCOL.template.md`. Every one is nounless or code-shaped, so the
   restatement gate scans that file and matches none of them; `check-protocol-parity.test.sh:95`
   only greps the section for the literal `agent-cap.js` and compares no digit. So this commit gave
   the *playbook* mechanical pairs, gave the **BINDING** protocol prose, and removed the operator's
   pointer to it. The protocol instructs an agent to inline the literal `boundedParallel(thunks, 5)`;
   drop `MAX_VERIFIERS` and the hook denies the form the protocol mandates.

**Fix.** Rewrite the string in both copies (they are byte-pinned) to name the kit file and the
redeploy: "…to change the number, edit `tools/hooks/agent-cap.js`, copy it to
`.claude/hooks/agent-cap.js`, and re-run `bash tools/run-gates.sh` — the playbook's stated digits are
bound to it by `tools/check-playbook-parity.sh`." Separately, add parity pairs with
`memory/guides/REVIEW-PROTOCOL.md` as the stated file for `MAX_LENSES` and `MAX_VERIFIERS`, so the
BINDING document gets the treatment the playbook just got.

**Left-shift gate.** Any operator-facing string naming a file path is a record-vs-reality claim, which
this repo already gates elsewhere. Cheapest arm: in `agent-cap.test.sh`, assert the AGENT_CAP remedy
text names `tools/hooks/agent-cap.js` (not "this file") — one grep beside the existing byte-parity
assertion.

---

## LOW

### L1 — the exclusion is anchored to the gov-only source filename, so every adopter inherits four unwaived hits
`tools/check-agent-cap-restatement.sh:75` (raw id 13)

`PARITY_OWNED` is anchored `^parallel-coding-governance\.template\.md$`. `WIRE-INTO-PROJECT.md:79`
deploys the playbook as `<project>/docs/PARALLEL.md` (or as `AGENTS.md` via the agent-instructions
kit), so the anchor never matches in an adopter tree, `_excluded` is 0 there and the M1 guard also
stays quiet. Meanwhile `tools/govkit/entries/check-agent-cap-restatement.kit.toml` registers this
gate as a leg and seeds `agent-cap-restatement-waivers.txt` **empty by design**, and
`tools/govkit/registry.toml:173` lists `check-playbook-parity.sh` as an EXEMPTION — "prescribed for
copy nowhere in the runbook" — so the stronger control the exclusion defers to never ships at all.

Net: an adopter installing the playbook plus this kit gets a red bar on first run over four sentences
gov itself shipped them. It is new with this diff — measured, the pre-diff `PAT` (no `cap`/`verify`/
`concurrency` nouns, no `REV`/`NB` shapes) matches **zero** lines of the playbook; the widened one
matches four.

**Fix.** Either seed the four playbook sentences as waiver rows in the adopter's registry from the
playbook kit's adopt step, or key the exclusion on the playbook's own `governance-template: vN.N`
marker rather than on the un-instantiated filename, so a renamed deployed copy is recognised as the
same document.

**Left-shift gate.** The repo already treats "a path spelled in something an adopter receives" as a
gateable class (`check-install-prefix.sh`). The analogous arm here: a fixture that copies the
playbook to `docs/PARALLEL.md` and asserts the gate's verdict is the same as with the gov-side name.

---

## Carried corrections

Three sub-claims from the raw findings did not survive verification intact and are recorded so they
are not carried forward as fact:

- **id 2** claimed `+`, `(` and `[` in `MEMORY_ROOT` misbehave like `|`. They do not: an invalid ERE
  makes `grep` emit nothing and the vacuity arm exits 2, and `mem+notes` un-excludes the record tree
  and reds loudly. Only `|` shrinks silently (`.` harmlessly widens). The defect stands on the `|`
  case and on the quoting case; the blast radius is narrower than stated.
- **id 3** called `REVIEW-PROTOCOL.md:120`'s "the digit here is checked, not trusted" false. It is a
  stretch — the line means the hook re-resolves the width at the call site of a script that inlines
  it, which it does. The diff also removed two digit copies from that file rather than only adding
  one.
- **id 13** said "four lines" of the playbook match. It is four texts on **two** lines (182, 189).

## Refuted (3)

Three raw findings were refuted by the skeptic pass and are not reported. Precision 0.82.
