**Serves:** diff-review TOOL-cBriefedPilot-5 TOOL-cBriefedPilot-7 TOOL-cBriefedPilot-8 TOOL-cBriefedPilot-13 TOOL-cBriefedPilot-14 TOOL-cBriefedPilot-22 TOOL-cBriefedPilot-23  <!-- inferred: the finishing pass over the units its header enumerates -->

## Verdict: CHANGES REQUESTED — no blocker; one high makes `--close` unmeetable on an honest run

**Tier-2 code review · cBriefedPilot · 2026-08-16 · the FINISHING pass · reviewed range:
`9ad3531...HEAD` (`9ad3531..25f1857`, 8 commits, units 7 · 8 · 13 · 14 · 22 · 5 · 23 · 36 plus the
REVIEW-PROTOCOL correction)**

**Review shape:** raw 19 · confirmed 12 · refuted 7 · unverified 0 · **precision 0.63**.
Three of the twelve confirmed findings (ids 5, 9, 17) are three independent hunters landing on the
same defect — the preflight echo printing a live anchor after unit 5 froze the recorded one — so the
twelve collapse to **10 distinct defects: 0 blockers · 1 high · 5 medium · 4 low**. Every finding
below survived an adversarial skeptic pass; nothing is carried as unverified.

**The one thing to fix before this lands.** `closing-review-recorded` (§1) joins on an eight-char
base prefix in a repo whose git abbreviates to seven. Executed against this build's own recorded
base it returns 1 where the seven-char form returns 0 — the DoD item cannot be met by any review
record this corpus has ever written, and the diff has already begun paying for it with seven
`--override closing-review-recorded` spellings in the driver's own suite.

**The shape of the rest.** The dominant defect class named in the brief — *a check that cannot
fail* — did not reproduce as the top finding. What reproduced instead is its mirror: **a check that
cannot pass**, twice as a permanent red wedge on a terminal record no verb can rewrite (§2, §3).
Both are the same underlying error — grading a frozen historical record against a moving present —
and both are the wedge unit 36 fixed for check 8 *in this very diff*, reintroduced one check later.
The genuine cannot-fail instances that survived are smaller: one arm silently disabled by CRLF (§8)
and one helper defined and never called (§10).

Three prose-vs-code drifts round it out (§4, §5, §9). All three sit in documents the kit tells an
outside reader are authoritative, and all three are green on the bar, because every parity gate in
this repo compares **copies to each other** and never a copy to the code.

---

## 1 · HIGH · `tools/unattended/unattended.sh:1235` — `closing-review-recorded` joins on eight chars; this repo abbreviates to seven, so the item is unmeetable

**Claim.** The new DoD item resolves the recorded BASE to `${rb:0:8}` and greps the build's tracked
review records for it. This repo's git abbreviates to **seven**, and 29 of 48 tracked review records
spell the sha at exactly seven. The item can never be satisfied by an honestly-written record.

**Reproduced against the live tree.** `RUN.md:44` pins
`base: 709d260da8c81551e59da769aceca47202bb5923`, so the needle is `709d260d`:

```
git grep --cached -qF -- 709d260d -- 'memory/builds/cBriefedPilot/reviews/*.md'   → exit 1
git grep --cached -qF -- 709d260  -- 'memory/builds/cBriefedPilot/reviews/*.md'   → exit 0
git rev-parse --short 709d260da8c8…                                              → 709d260
```

Both records under this build spell the range at seven (`709d260..c32161b`), and both are tracked,
so `--cached` is not the blocker. Corpus-wide the convention holds: of 48 tracked review records
only 11 carry a token that resolves to a commit at ≥8 chars; 35 do at ≥7.

**Impact.** Every `--close` blocks on a machine item, and in an unattended run with no owner turn the
only exit is `--override closing-review-recorded --reason …` **written by the run itself**. A gate
that always fails trains its own bypass and spends the override budget on every run. The diff has
already normalised this: `unattended.test.sh` now carries seven `--override closing-review-recorded`
spellings on closes that previously ran clean, and the green control writes its fixture at
`${rb:0:8}` — a convention nothing else in the corpus follows, so the suite proves the checker works
only against a spelling no writer produces. The code comment's justification ("15 of 46 tracked
records carry an eight-hex token") counts *any* 8-hex string, keepalive ids included, not a
resolvable base prefix; measured, only 11 of 48 carry a resolvable ≥8 token.

**Fix.** Join on git's own abbreviation instead of a hardcoded 8:

```sh
nb=$(GIT rev-parse --short "$rb" 2>/dev/null) || return 1   # 7 today, auto-scales as the repo grows
[ ${#rb} -ge 8 ] && GIT grep --cached -qF -- "$nb" -- "$M/builds/$slug/reviews/*.md"
```

keeping the length/shape guard on `$rb`. Cheaper alternative if the constant must stay: `${rb:0:7}`,
which is what every writer in this corpus already emits.

**Left-shift gate.** The green control is the thing that lied. Add an arm to
`unattended.test.sh` that writes the fixture record **at `git rev-parse --short` of the base**, not
at a slice the test picks — a control whose fixture is generated by the same convention the corpus
uses would have failed on the first run. Cheaper still, and worth having regardless: a red arm in
`check-unattended.test.sh` asserting `dod_met closing-review-recorded` is satisfiable against a
record written the way this repo writes them.

---

## 2 · MEDIUM · `tools/unattended/check-unattended.sh:406` — check 17's waiver selector is an unanchored substring grep, so an override reason quoting the grammar reds the bar permanently

**Claim.** The population selector is `grep -F ' waiver · item ' "$f" | grep -F ' · reason '` —
whole-line substring, unanchored, no discrimination of the parked KIND. `park()`
(`unattended.sh:1250-1252`) writes all four kinds through one grammar
`<ts> <kind> · item <item> · reason <text>`, so a free-text reason that quotes the waiver grammar is
read as a waiver. This contradicts the block's own comment ("Only the waiver kind is joined") and
protocol §2 ("of four kinds, which `park()`'s own kind argument already discriminates").

**Reproduced end to end.** The line

```
2026-08-16T00:00:00Z override · item gates-green · reason superseding the earlier waiver · item land-once-done · reason owner said so
```

is SELECTED; `wh=${wl#* waiver · item }` (line 387) strips at the **first** occurrence, yielding
`land-once-done`; membership against `DIRECTIVES_CORE` passes (`unattended.sh:90` contains
`land-once-done:M8`); `wr` is non-empty. The first-blob join at 402-404 then **fails**, because an
override is parked only at `verb_close` (`unattended.sh:1169`) and so cannot be in the record's first
committed blob.

**Impact.** Permanent RED merge bar on a terminal record no verb rewrites — `refuse_if_terminal`
blocks `--close`/`--abort`. That is the exact wedge `park()`'s fail 41 and `--abort`'s fail 36 exist
to prevent, reached through free text an owner types: `verb_close`'s override validation
(1136-1151) checks membership, non-emptiness and the authorization carve-out only, with no content
guard. Decisive: the driver's own `recorded_waivers()` (`unattended.sh:465-471`) anchors
`^<ts> waiver · item \([^ ]*\) · reason ` and its comment names this precise mis-parse as the reason
the anchor exists. **The leg carries the weaker grammar the driver already rejected.** Trigger needs
a reason quoting the U+00B7 grammar, which is exotic — but this repo pays two dedicated refusals to
prevent exactly this wedge class.

**Fix.** Reuse the driver's grammar rather than inventing a second one:

```sh
grep -E '^[0-9][0-9-]*T[0-9:]*Z waiver · item [^ ]+ · reason ' "$f"
# handle: sed -n 's/^[0-9][0-9-]*T[0-9:]*Z waiver · item \([^ ]*\) · reason .*$/\1/p'
```

**Left-shift gate.** Add a red arm whose fixture parks an **override** whose reason quotes the waiver
grammar, and assert check 17 stays silent. More durably: the record grammar is now parsed in two
files with two regexes — hoist the anchored pattern into one place both read, or add a leg asserting
the leg's selector and `recorded_waivers()` accept the same language. A second parser for a grammar
that already has one is the reusable lesson here.

---

## 3 · MEDIUM · `tools/unattended/check-unattended.sh:389` — check 17 grades historical waivers against the CURRENT directive set, with no repair path

**Claim.** `RUNS` (line 138) selects every tracked `$M/builds/*/RUN.md` with no phase filter, and
check 17's membership arm joins each parked waiver handle against
`" $DIRECTIVES_CORE $DIRECTIVES_EXTRA "` **as declared today**. `DIRECTIVES_EXTRA` is
project-editable (`.unattended.conf:62`) and `DIRECTIVES_FLOOR="11"` pins only the COUNT of the core
set (lines 517-526).

**Impact.** Removing a project handle, or renaming a core one in `DIRECTIVES_CORE`
(`unattended.sh:90`), passes every floor while reddening every landed run that waived the old
handle — permanently, since `refuse_if_terminal` blocks every verb on a terminal record, and
hand-editing the handle to the new spelling then trips the first-blob arm at line 402 instead.
Grading a historical record against the present config is a genuine logic error in a check whose own
message reasons about the past ("a rule no verb would have accepted"). It is the same wedge unit 36
fixed for check 8 one check earlier in this diff.

Two caveats that do not change the verdict: it is latent today (no `waiver · item` line exists in any
tracked RUN.md), and "no repair path" is slightly overstated — deleting the waiver line, or re-adding
the retired handle to `DIRECTIVES_EXTRA`, clears it.

**Fix.** Join against the directive set **at the record's own pinned BASE**, not at HEAD. A blanket
terminal exemption is *not* the fix here: check 17 is the second opinion on what landed, so exempting
terminal records would gut it.

**Left-shift gate.** This is the third instance of one shape in one build. Add a standing arm to
`check-unattended.test.sh` for the class, not the instance: a fixture with a LANDED record, then
mutate the *config* (retire a `DIRECTIVES_EXTRA` handle, bump a floor) and assert the leg stays
silent. Any check that reads a terminal record and a live constant in the same comparison should have
to answer that fixture.

---

## 4 · MEDIUM · `tools/unattended/PROTOCOL.template.md:148` — "Six kit-owned core items." now introduces an eight-row table

**Claim.** Verified directly: line 148 reads `Six kit-owned core items.` and the table beneath it
(151-160) has **eight** rows. `git show HEAD~6:` of the same file shows the six-row table, so units 7
and 8 added `build-complete` and `closing-review-recorded` (lines 157-158) without touching the
sentence above them. `memory/guides/UNATTENDED-PROTOCOL.md:148` is byte-identical.

**Impact.** The binding contract states a population size contradicting both the table under it and
the constant the driver enforces (`DOD_CORE` = 8 at `unattended.sh:78`; `.unattended.conf`
`CORE_FLOOR="10:8"`) — a third spelling of one fact, in the document an outside reader is told is
authoritative. Check 16 arm E, added in this same diff precisely to stop this drift, joins the row
NAMES both ways (`check-unattended.sh:554-566`) but not the count. Check 10's parity passes because
both copies are equally wrong.

**Fix.** Delete the number in both copies — "Kit-owned core items. Each names its checker…" — since
the table IS the population and this repo already bans prose counts that rot (the govkit registry and
the memory-tree kit-version comment both say so). If a count is wanted, write "Eight" in both files
**and** extend arm E to join it to `$(printf '%s\n' $DOD_CORE | grep -c .)`.

**Left-shift gate.** The generalisable one: a leg that flags any **cardinal number word or digit
immediately preceding a table or list** in the two protocol copies, unless that number is joined to a
derived value by an existing arm. This repo has now been bitten by a prose count three times (the
govkit spec twice, this once); the charter's own rule — *no population count is written in prose* —
deserves a mechanical arm rather than a convention.

---

## 5 · MEDIUM · `memory/map/features/unattended.md:151` — three "known gaps" bullets became false in this diff and now tell a reader the opposite of the code

**Claim.** Verified factually. Lines 149-153 still describe check 17 as "PARKED unbuilt … a waiver's
shape and its provenance are unchecked on the bar today". Lines 154-157 say `build-complete` and
`closing-review-recorded` are "both parked", so "`--close` therefore still blocks on nothing where
completeness is concerned". All three shipped in this same range: `65a94c8` (unit 7), `90205a0`
(unit 8) — both live in `dod_met`, both members of `DOD_CORE` — and `17305a1` (unit 13, check 17 at
`check-unattended.sh:377-407`, inside the gated leg). The dossier's last touch is `c32161b`
(unit 20), which predates all three.

**Impact.** The map is the queried catalog for this feature. `reuse_lookup.py` and any agent orienting
on the kit are told the exact opposite of what the code does, and will re-plan work that shipped.
`python tools/codebase-map/test_codebase_map.py` passes over it (verified green): the gate checks
inventory coverage and generated-artifact freshness, not dossier prose.

**Fix.** Rewrite the three bullets: check 17 is a leg with three arms and a green control; both DoD
items are in `DOD_CORE` with `CORE_FLOOR=10:8`. Move whatever residual survives — e.g. that check 17
proves nothing when the run authors both sides locally, which the source comment already states —
into a single accurate row.

**Left-shift gate.** Cheap and mechanical: have the codebase-map gate red when a dossier's last
touching commit is older than the last commit touching any file the dossier claims. It cannot grade
prose, but "the code moved and the dossier did not" is a pure git question and catches this whole
class. A dossier that describes a built thing as parked is worse than no dossier.

---

## 6 · MEDIUM · `tools/unattended/unattended.sh:1060` — the preflight echo still prints the LIVE anchor after unit 5 froze the recorded one

*(Three confirmed findings — ids 5, 9, 17 — are this one defect.)*

**Claim.** Verified in source. `AREF`/`ASHA`/`AURL` are assigned only at line 181 (empty init) and
line 249 (inside `observe_anchor`, from the live `ls-remote` advertisement) and are never re-read
from the record. Lines 1037-1039 gained the freeze guard (`[ -n "$(fact …)" ] || set_fact …`), but
unlike `base` — deliberately re-read at line 1036 with a comment naming the hazard — the echo at
line 1060 still interpolates `$AREF`/`$ASHA`:

```sh
echo "unattended: preflight OK — base $base · anchor $AREF at $ASHA · keepalive $kid · …"
```

The adjacent comment states the invariant being violated: *"A second preflight that printed a base it
did not write would be the same lie in the operator's face."*

**Impact.** On a second preflight after the remote's default tip moved, the driver prints
`anchor refs/heads/main at <new sha>` while `anchor-sha:` holds the old one. Re-preflight is the verb
the driver *tells* a run to re-run after a compaction, and the mandated lander reconciles origin
before the gate, so divergence is the normal case on this fleet — with nobody present to notice.
Protocol §2 records facts 5-7 as the EVIDENCE an outside party uses to re-derive the pin. It also
leaves unit 5's own AC4 ("The preflight echo names the value on the record",
`spec-cBriefedPilot-5.md:118`) unmet while the unit is recorded CLOSED. Impact is print-only — no
authorization decision changes.

**The kit's own fixture proves reachability rather than refuting it.**
`unattended.test.sh:729-751` advances the anchor on the fake origin, pushes, fetches by remote name,
re-runs `--preflight`, then asserts `asha2 == asha1` (frozen) AND `now != asha1` ("the anchor really
did move, so the freeze has something to resist"). At that exact point `$out` carries the NEW sha.
The block asserts `hit "$out" "base $base1"` for the base and **nothing** for the anchor, which is
why it stays green.

**Fix.** Mirror the base re-read immediately after the three guarded writes:

```sh
AREF=$(fact "$rel" anchor-ref); ASHA=$(fact "$rel" anchor-sha)   # AURL too if it is ever echoed
```

**Left-shift gate.** One line in the fixture that already exists:
`hit "$out" "anchor $aref1 at $asha1"`, beside the `same "the anchor sha did not move"` assertion.
The general rule this build keeps rediscovering — **an arm that reads the FILE is not an arm that
reads the OUTPUT** — is worth a note in the unattended suite's header: any fact frozen on the record
gets two arms, one per surface.

---

## 7 · LOW · `tools/unattended/check-unattended.sh:255` — check 8's terminal exemption swallows the two MALFORMED-MARKER refusals, keyed on a field the run itself writes

**Claim.** Reproduced on the live tree. Line 255 wraps **all three** `fail 8` branches — both
MALFORMED-MARKER refusals and the drift comparison — in one
`! case " $PHASES_TERMINAL " in *" $ph "*` guard. Test: duplicating `<!-- run:generated -->` in
`memory/builds/cBriefedPilot/RUN.md` (`phase: ABORTED`) leaves the leg at exit 0; flipping only
`phase:` to `RUNNING` on the identical bytes produces
`UNATTENDED check 8 FAILED — a run-state file's generated markers are malformed`.

**Impact.** The stated justification covers only the byte comparison ("a finished snapshot cannot
track a moving README"). Marker well-formedness is not something a moving README can break, so the
carve-out is strictly wider than its reason. A record at `phase: ABORTED` or `LANDED` now passes the
bar with a duplicated or transposed marker pair; `region()` exits 3 with empty stdout on exactly that
shape, and `unit_rows`/`nonterminal_units` swallow it via `2>/dev/null`, so `verb_status` reports
"(no non-terminal unit)" rather than an error for every later reader. Check 26 blocks `--preflight`
on a terminal record, so no verb can re-splice it: the malformed state becomes permanent and
invisible. This is live coverage loss, not hypothetical — both tracked run-state files on this tree
are terminal, and check 8 is the only validator of these markers anywhere in the repo, so the
malformed arm currently guards **zero** files.

The same file names this exact shape as a defect 40 lines below, at check 9: *"A phase-keyed
carve-out is not the fix either — the run writes `phase:`, so it would be a one-line escape from this
check."*

**Fix.** Three lines moved, no new branch: compute `a` and `b` unconditionally (both still `fail 8`
on a malformed pair), then guard only `[ "$a" = "$b" ] || fail 8 …` with the `PHASES_TERMINAL` test.
The arm the suite already added for the terminal case still passes.

**Left-shift gate.** For each phase-keyed exemption, the suite should carry a fixture proving the
arms **outside** the exemption's stated justification still fire on a terminal record. Concretely
here: one arm with a terminal record and a duplicated marker, asserting the leg reds. Broader and
cheaper: a lint over `check-unattended.sh` flagging any `PHASES_TERMINAL` guard whose body contains
more than one distinct `fail` message, since that is the signature of an exemption wider than its
reason.

---

## 8 · LOW · `tools/unattended/check-unattended.sh:388` — check 17's waiver parse is the file's only reader that does not strip a trailing CR, so the empty-reason arm cannot fire on a CRLF checkout

**Claim.** Reproduced. `wr=${wl#* · reason }` runs on a line read straight out of
`grep -F ' waiver · item ' "$f"` (line 406) with no CR strip anywhere on the path. With `wl` ending
in CRLF and an empty reason, `wr` is `$'\r'`, so `[ -n "$wr" ]` passes and the arm at line 393 cannot
fire. The "only reader that doesn't strip" claim checks out: `core_of` (67) and `fact_of` (153) do
`l=${l%$'\r'}`; `region()` (169) does `sub(/\r$/,"",ln)`; check 10 (424-425) seds `\r$`; check 12
(445) and check 16 arms A/D/E (485, 543, 556) all `tr -d '\r'`.

**Impact.** One of check 17's three arms is silently dead for an adopter whose memory tree lacks
gov's `memory/**/*.md text eol=lf` pin — and the kit ships no `.gitattributes` guidance for the
memory root. The arm is deliberate and asserted (`check-unattended.test.sh:714-716` builds the
empty-reason fixture in LF and asserts the message), so this is a live arm a CRLF checkout disables
while the leg exits 0 — the "green by accident" shape the file's own check-12 comment (443-446)
writes out. One correction to framing: on a CRLF *worktree* over an LF *blob*, the first-blob join at
402 would red loudly; the fully-silent outcome needs the blob itself committed CRLF.

**Fix.** `wl=${wl%$'\r'}` immediately after the `read`, matching `fact_of`'s line-155 idiom. Strip
once at the top of the loop body so the `grep -qF` needle and haystack are stripped consistently.

**Left-shift gate.** `check-unattended.sh` now has nine CR-strip sites and one omission; a convention
followed eight times out of nine is a gate waiting to be written. Add a leg arm that runs the whole
suite once against CRLF-committed fixtures (the kit already builds `mktemp -d` scratch repos, so this
is a `.gitattributes`-free clone, not new infrastructure). Failing that, the cheapest version: grep
the file for every `read`/`grep` that feeds a `${var#…}` parse and assert a `%$'\r'` within two lines.

---

## 9 · LOW · `tools/workflows/REVIEW-PROTOCOL.template.md:175` — the shipped kit template cites a gov-specific build path as evidence

**Claim.** Verified. `grep -n 'memory/\|{{'` over the file returns exactly five path-bearing lines:
four are `{{TOOL_ROOT}}`-templated (26, 33, 55, 137) and line 175 is the lone hardcoded
repo-specific pointer `memory/builds/cBriefedPilot/build/`. The comparison template one kit over,
`tools/memory-tree/BUILD-METHOD.template.md`, cites `memory/builds/<slug>/` generically — this is the
only concrete gov slug in any shipped `*.template.md`.

**Impact.** An adopter installing the review-protocol kit receives a BINDING document whose one
evidence pointer resolves to nothing in their tree. Both gates stay green by construction:
`check-install-prefix.sh`'s regex is `($kit-alternation)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)`, so
a `memory/builds/…` prose path is outside its population entirely; `check-protocol-parity.test.sh`
renders `{{TOOL_ROOT}}` and diffs the two copies, and `memory/guides/REVIEW-PROTOCOL.md` carries the
identical line. Same class the install-prefix gate exists for, one directory over. Genuinely small —
a provenance footnote, not an operational path.

**Fix.** Either template the memory root and the slug out of it, or drop the citation from the shipped
template and keep it only in `memory/guides/REVIEW-PROTOCOL.md` (the parity test substitutes, so an
intentional asymmetry needs the substitution rule extended).

**Left-shift gate.** Extend `check-install-prefix.sh` — the gate whose whole thesis is *what strands
an adopter is a path SPELLED in something they receive* — from kit paths to **any repo-rooted path in
a shipped `*.template.md` that is not `{{`-templated and does not use a `<placeholder>` segment**.
The existing shrink-only waiver file gives deliberate spellings somewhere to live. The build slug
alternation is derivable from `memory/builds/*`, so a hardcoded gov slug in a shipped artifact is a
one-line predicate.

---

## 10 · LOW · `tools/unattended/unattended.test.sh:149` — `mutate()` is defined here and called zero times

**Claim.** Verified: `mutate()` is defined at lines 149-155 and grep finds no call site anywhere in
the file (only the comment at 148 and the definition). The suite's 30 `sed -i` fixture edits — 11 of
them added by this diff in the unit 7/8 blocks — all bypass it. The helper's two-way self-test lives
only in `check-unattended.test.sh:835-841`, where it is actually used (270-271, 762-789).

**Impact.** Unit 23's S4 states the helper is "ADOPTED by the arms whose fixtures this build caught
doing nothing", and one of the three shapes it names — the fetch-by-path anchor advance — lives in
this file. What landed here is the fix plus a control, not the guard. In the suite with the most
fixture edits, a `sed` that stops matching after a fixture reshape still reports nothing, which is
exactly the class the unit exists for. It also carries an `n=$((n+1))` site that never runs, so the
`FLOOR_ASSERTIONS` pin for this file is measured over a function nothing exercises.

**Fix.** Route the new unit 7/8 fixture edits through `mutate` — they are precisely its shape
(`mutate memory/builds/tRun/README.md 's/| OPEN | rev-1 |/| CLOSED | rev-1 |/'`) — and re-measure
`FLOOR_ASSERTIONS`. Or delete the unused copy and record in the spec that this suite got the control
rather than the helper.

**Left-shift gate.** A defined-and-never-called function in a `*.test.sh` is the cheapest possible
lint and it belongs beside `check-arms.py`, which already reasons about arms in these files: flag any
function defined in a suite with zero call sites in the same file. It would also have caught the
duplicated copy on the commit that introduced it.

---

## What this pass says about the build's method

**The dominant class inverted.** The brief asked hardest for *a check that cannot fail*. Two of the
top three findings are *a check that cannot pass* (§1, §2) plus one that cannot pass in the future
(§3). All three share one root: **a predicate that joins a frozen historical value to a live present
one** — a base to a hardcoded abbreviation length, a landed waiver to today's directive set, a
terminal record to a moving config. Unit 36 fixed exactly this for check 8 in this same diff and the
lesson did not generalise one check to the left. That is the single most valuable standing fixture to
add: *take a terminal record, move the world around it, assert the leg stays silent.*

**Every parity gate in the kit compares copies, never a copy to the code.** §4 (prose count vs
`DOD_CORE`), §5 (dossier vs shipped checks) and §9 (shipped template vs adopter reality) are all
green because check 10 diffs two protocol copies, `check-protocol-parity.test.sh` diffs two protocol
copies, and the codebase-map gate grades inventories and byte-freshness. Check 16 arms D and E, added
in this very diff, are the right instinct — they join a declaration to prose in both directions —
and they are the only gate in the kit that does. Extending that pattern to the count in §4 is a
five-line change and closes a class.

**Three hunters on one defect, zero on the neighbouring surface.** §6 was found three times because
everyone read the freeze diff; nobody wrote the one-line output assertion that would have caught it,
because the fixture that *demonstrates* the bug asserts only against the file. When a build freezes a
fact, the arm count should go to two — record and transcript.
