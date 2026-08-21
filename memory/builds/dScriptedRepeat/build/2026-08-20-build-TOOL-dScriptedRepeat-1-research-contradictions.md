**Serves:** research TOOL-dScriptedRepeat-1

# Contradiction hunt — where the five research records disagree, and who is right

*Adversarial cross-read · node `d` · 2026-08-20 · build `dScriptedRepeat` · kind `research`.
Measured against the worktree at HEAD `0d88d5f2`. Not a summary and not a synthesis: only
disagreements, refuted claims, cite failures, equivocations and gaps.*

**Method.** All five records read in full. Every numeric or `file:line` claim that could be resolved
without writing to the tree was resolved — against `tools/unattended/unattended.sh`,
`tools/unattended/check-unattended.sh`, `.memory-tree.conf`, `.unattended.conf`,
`tools/unattended/kit.toml`, `memory/backlog/TOOL.md`, `memory/HYGIENE.md`, and against
`C:/projects/nicocares/main` for the two reference playbooks. Nothing was written except this record;
one probe staged the five research records to run `gen_build_index.py --print-bindings` and the index
was restored (`git status --porcelain` now shows only the untracked `build/` folder, as before).

**The headline.** The five records agree far more than they disagree, and where they disagree the
disagreements are load-bearing rather than cosmetic. Three things matter most:

1. **The five lenses do not agree on where the OUTPUT PATHS are declared, and the lens that follows
   the owner's fork literally supports it with a claim that is false against source** (§1.1).
2. **Two lenses count the reference recipe's steps at nine and two count them at zero, both
   correctly**, which is the two-answers-to-one-question defect landing squarely on fork 5's gate
   (§1.3).
3. **Four recommendations are refuted by another lens's evidence** — a REUSE verdict for an oracle no
   adopter has, a piece-count derived from filesystem presence, a witness field priced at one capture
   group, and a kind/extension narrowing the owner's own ask breaks (§2).

Line-number accuracy across the three source-reading lenses is high but not clean: **thirteen cites
do not resolve**, one of them materially (§3).

---

## 1. Head-to-head contradictions

### 1.1 Where the declared OUTPUT PATHS live — the playbook, or the build README

**`in-repo-prior-art` §8.3:**

> The declaration therefore belongs in the PLAYBOOK, at the pinned BASE, where `check_authorization`
> already reads a blob it cannot have written (`unattended.sh:763-770`, `GIT show "$base:$rel"`).

**`extension-seams` §5.3**, on `PLAYBOOK_OUTPUT_ROOTS`, verdict **NO — refuse**:

> The output paths belong in the **build README at BASE**, beside `authorized-by:`, where the same
> provenance argument that carries the mode carries them. **This is the design decision the fork
> implies and does not state.**

**`hard-problems` §1.3** agrees with `extension-seams`:

> Adding `pieces:` and `outputs:` beside it costs nothing — `parse_front_matter` at
> `gen_build_index.py:190-228` validates only `REQUIRED_KEYS`…

**And fork 2's ruling, from the build README, says the first thing:** *"The playbook declares OUTPUT
PATHS."*

**Verdict: `extension-seams` and `hard-problems` are right about the mechanism; `in-repo-prior-art`'s
justification is FALSE.** Measured: `unattended.sh:764` is `if ! blob=$(GIT show "$base:$rel"
2>/dev/null); then`, and `$rel` is the **build README** — the awk at `:782-787` extracts `slug:` and
`authorized-by:` from its front matter. The blob `check_authorization` reads is not the playbook, so
"where `check_authorization` already reads" does not support putting the declaration in the playbook.
Worse, the driver's own comment at `unattended.sh:781` forbids the second read that would be needed:

> Both keys are emitted KEY-TAGGED and nothing exits on a match; the front-matter close still
> terminates the scan, which is what bounds it. **No second `GIT show`: one blob, one parse.**

**What it changes for the design.** This is the sharpest genuinely-open fork in the set, because both
answers cost something real and nobody proposed the third:

- **README front matter** (two lenses): one blob, one parse, zero new machinery — but the *playbook*
  is then not self-describing, and every new run of the same playbook retypes its own output
  declaration. For a mode whose whole premise is repeatable content that is a structural regression,
  and neither lens says so.
- **The playbook** (fork 2, `in-repo-prior-art`): the artifact carries its own contract and travels —
  but it needs a second trusted read against an explicit design rule, and the *path* to the playbook
  still has to come from somewhere the run cannot have written.
- **Unproposed hybrid:** the README front matter at BASE names the playbook PATH; the gate takes a
  second `GIT show` of that path at BASE and reads the globs from the playbook. Costs the second read
  the driver comment argues against, and buys a self-describing artifact. **Nobody priced it.**

### 1.2 The GATE tag count — 92, 90, or 86

**Build README:** *"92 GATE tags, 95 CHECK tags, 110 numbered steps"*.
**`extension-seams` §9.2** re-states it as measured: `GATE` tokens **92**.
**`external-instruction-design` §1** and **`in-repo-prior-art` §8.5:** **86**.
**`corpus-anatomy` §0:**

> `GATE` tag emissions | **90** (86 single-line + 4 line-wrapped) … **92 is the count of the string
> `GATE`, not of tags** — two of those 92 are prose uses.

**Verdict: `corpus-anatomy` is right, exactly, and is the only lens that decomposed it.** Measured:

```
grep -o 'GATE'  PLAYBOOK.md | wc -l   -> 92
grep -o 'GATE ' PLAYBOOK.md | wc -l   -> 86
grep -cE 'GATE$' PLAYBOOK.md          -> 4
```

86 + 4 + 2 = 92, and the two remainders are at L6 and L992, both `` `GATE` `` inside backticks in
prose. `extension-seams` §9.2 presents 92 as its own measurement "using I21's own step regex" — the
step regex does not count tags, and the figure is the README's number carried forward unchecked.

**What it changes for the design — and this is not bookkeeping.** I confirmed the consequence
`corpus-anatomy` §3.4 staged and observed. Extracting every backticked single-line tag and splitting
compounds gives **52 distinct leg tokens**, and `I40` and `I44` are **not among them**. They appear
only in wrapped tags. So two invariants the reference playbook cites have never once been validated
by the reference playbook's own validity gate, live, today. That is a verified instance of exactly the
class fork 5 exists to prevent, sitting inside the artifact fork 5 was derived from. Fork 5's gate
must parse structurally, not per line, and its spec must state the count is derived.

### 1.3 Does `HYBRID-PLAYBOOK.md` have nine steps or zero?

**`corpus-anatomy` §0:** *numbered steps* — *"9 numbered items (4 hard rules + 5 new-scene steps)"*,
and §5.1 records HYBRID as FILLING required section **R7, "The step checklist"**, via *"§2 rules 1–4,
§5 steps 1–5, §7, §9, §10 bullets"*.

**`extension-seams` §9.2:** *"`brand/art-style/HYBRID-PLAYBOOK.md` … steps **0** … has **no step ids,
no GATE tags and no CHECK tags at all.**"*

**`hard-problems` §4.3:** *"`grep -nE '^\*\*[A-Z]?[0-9]+\.'` matches nothing — it has no step-shaped
lines at all."*

**Verdict: both are correct, about different populations, and neither says so.** Measured: HYBRID
carries nine numbered lines — `1.`–`4.` at L60/62/64/74 (the hard rules) and `1.`–`5.` at L144–148
(adding a new scene) — and **zero** lines matching `^\*\*[A-Z]\d+\.`, I21's selector.

**What it changes for the design.** This is the repo's own two-answers-to-one-question defect, and it
lands on the one predicate fork 5 is entirely made of. If the validity gate hardcodes a step
selector, HYBRID's nine real steps are invisible and the gate reports *"every step is tagged"* over an
empty selection — green-by-absence, the class this repo reds by name. `corpus-anatomy`'s proposed
escape (a declared `gates: none — <why>` at R8) does **not** rescue it: `gates: none` makes every step
a CHECK, but there are no steps to tag under the selector, so the vacuity survives. The only answer
that works is the one `extension-seams` §9.2 and `hard-problems` §4.3 converge on and
`corpus-anatomy` does not reach: **the playbook DECLARES its own step selector and a shrink-only
minimum step count**, and the gate refuses a selector that reaches fewer than the declared floor.
The reference already ships that guard (`check_content_plan.py:2496`, `steps < 50` reds as I20).

### 1.4 The read-path margin — 6,793 or 6,699

**Build README:** *"106,194 B against a declared ceiling of 112,987 — 6,793 B of margin"*.
**`in-repo-prior-art` §10** and **`extension-seams` §7.1:** 106,288 B, **6,699 B**.

**Verdict: the two lenses are right; the README is stale by exactly 94 bytes — and the cause is the
build itself.** Measured:

```
git show d2a40aa:memory/LIVE.md | wc -c   -> 1644
git show 0d88d5f2:memory/LIVE.md | wc -c  -> 1738
```

`0d88d5f2` is the commit that OPENED this build. Rendering `dScriptedRepeat`'s row into the generated
`memory/LIVE.md` cost 94 B of read path, and `memory/LIVE.md` is on the read path.

**What it changes for the design.** The README's own warning — *"this build's own generated row can
plausibly exhaust it"* — came true before a single design byte was spent, and neither lens noticed the
mechanism even though both re-measured the number. `extension-seams` §7.1's recommendation stands and
is now better founded: raise `READ_PATH_CEILING` as a ratified fork **at spec time**, with the
argument beside the number, not at build time. The precedent (`+5,609 B` for the second mode) leaves
≈1,090 B, and this build has already spent 94 of it on bookkeeping.

### 1.5 Fork 6 — "a separate register" versus a fifth `park()` kind

**Build README, fork 6:** *"**A separate register, surfaced at close.** … Distinct verb, distinct
region, distinct DoD treatment."*

**`in-repo-prior-art` §7.4:**

> **Verdict: reject a separate register, accept a fifth `park()` kind.** The fork's ruling is
> satisfied — distinct kind, distinct rows, distinct DoD treatment (none) — at roughly a tenth of the
> cost.

**`hard-problems` §5, fork 6:**

> a fifth `park` kind inherits all of that. A register OUTSIDE the run-state file is also outside §3's
> exemption set and would red the scope gate — so wherever it lands, it lands in the exemption list.

**Verdict: `in-repo-prior-art`'s cost case is right and its claim to satisfy the ruling is not.**
Measured: `park()` at `unattended.sh:1891` appends into the run-state file's parked region; a fifth
kind is one alternation in `verb_status`'s regex (`unattended.sh:1566`, verified to carry exactly
`(decision|abort|override|waiver)`) and one row in protocol §2 (`UNATTENDED-PROTOCOL.md:136`, *"of
four kinds"*). Check 17 joins **only** the waiver kind (`check-unattended.sh:489-491`, verified), so a
fifth kind costs no gate work. All of that is correct. But the fork says **distinct region**, and a
fifth kind is the *same* region in the *same* file with a different first token. `in-repo-prior-art`
re-reads "region" as "rows" and reports the ruling satisfied rather than reporting the tension.

**Both lenses also refuted the fork's stated PREMISE, and they disagree about what actually blocks.**
`in-repo-prior-art` §7.1: *"`verb_close`'s DoD loop (`:1650-1680`) blocks on the missing
ATTESTATION"*. `extension-seams` §2.6: *"What actually blocks is `verb_abort` (`:1293-1305`), which
demands both agent items."* Measured: both are partly right and the fork is wrong either way —
`verb_close` (opens `:1602`) blocks on any unmet DoD item including the two agent-attested ones, and
`verb_abort` hard-codes `for item in keepalive-reaped parked-decisions-surfaced` at `:1294`. **Neither
blocks on parks being OUTSTANDING.** The asymmetry fork 6 asks for already holds.

**One prerequisite only one lens priced.** `in-repo-prior-art` §7.3 flags `TOOL-aBoundedVerdict-6`
(`memory/backlog/TOOL.md:100`, verified OPEN at that line) — the run-state authored region's 8 KB
spill becomes load-bearing once parking is cheap — and calls it *"a prerequisite, not a follow-up"*.
`extension-seams` and `hard-problems` both design proposal-writing into the run-state file and neither
mentions it. A run emitting proposals across N pieces makes the spill likely, and crossing it mid-run
reds the bar and blocks `--close`.

### 1.6 Fork 5's runnability oracle — REUSE, or a declaration that does not exist

**`in-repo-prior-art` §1, row 4**, verdict **REUSE**:

> `tools/gate-legs.json` names + govkit's `[[gate_leg]]` join at `tools/govkit/govkit.py:859-905` |
> **REUSE** — gov has the runnability oracle the reference playbook's own checker lacks

**`hard-problems` §4.2:**

> the kit has no leg registry: `.unattended.conf` declares one `GATE_CMD`, not a set, and
> `tools/gate-legs.json` is a run-gates artifact rather than a kit concept. **Fork 5 therefore needs a
> new declaration** — a per-project map from a leg NAME to something runnable — or its "runnable" half
> is unimplementable.

**Verdict: `hard-problems` is right for the kit; `in-repo-prior-art` is right only for gov as its own
adopter, and the table row does not say so.** Measured: `grep -rn 'gate-legs.json' tools/unattended/*.sh
tools/unattended/*.toml` returns **nothing**. The unattended kit never reads the manifest.
`tools/gate-legs.json` holds 88 legs and is gov's run-gates artifact; an adopter of the unattended kit
receives no such file.

`in-repo-prior-art`'s own §8.5 concedes the degradation ("adopter HAS a leg manifest → the predicate
is set membership… adopter has NO leg manifest → a declared coverage mode… or a named refusal"). The
problem is the **verdict table**, which is the page a spec author reads first, and it says REUSE for a
seam that exists in exactly one repository.

**What it changes for the design.** Fork 5 costs a new per-project declaration that appears in nobody's
byte or arm estimate except `hard-problems`'. `extension-seams` §6.5's estimate (+30–45 driver,
+45–60 leg, +8–15 cross-component) does not include it.

### 1.7 The `TWENTY-ONE checks` docstring — a banned defect, or fine

**`in-repo-prior-art` §5.2:**

> `check-unattended.sh:2` reads *"the merge-bar leg for the unattended-run kit. TWENTY-ONE checks over
> the tree."* That is a count of a derived population written in prose, in a gate header — the class
> `AGENTS.md` bans by name… The clean move is to DRAIN the number rather than re-stamp it.

**`extension-seams` §3.1:**

> The file's own docstring at `:2` says "TWENTY-ONE checks", **which agrees** (review L4 caught it
> saying "EIGHTEEN" and it was fixed).

**Verdict: the facts agree, the verdicts do not, and `in-repo-prior-art` is right on the rule.**
Measured: `fail` numbers 1–21, gapless; the docstring says TWENTY-ONE. `AGENTS.md` §7: *"NO count of a
derived population is written in prose. The checker derives every figure it reports."* A number that
has already been wrong once, in this exact header, and was repaired by hand, is the textbook case.

**What it changes for the design.** `in-repo-prior-art` §5.2 also establishes that a new CHECK inside
this leg is far cheaper than a new gate LEG. Playbook mode brings at least three predicates (validity,
output scope, piece count). If any land as checks here, drain the number in the same commit — or the
build ships a false sentence under a green gate, which is the `TOOL-aMouldedFolio-1` class this build
is meant to be avoiding.

### 1.8 `DIRECTIVES_FLOOR` — a "live" defect that is not live

**`extension-seams` §1c, C8:**

> **C8 — the pin moved in the EXAMPLE and not in the dogfood conf.** Diff-review H1: `DIRECTIVES_CORE`
> grew to 13 while `.unattended.conf:71` still declared `DIRECTIVES_FLOOR="11"`, slack by exactly the
> two members the build added.

…tagged **"C8, live"** again in §2.3 item 4.

**`in-repo-prior-art` §8.6:** *"`DIRECTIVES_CORE` holds 13 against `DIRECTIVES_FLOOR="13"`."*

**Verdict: `in-repo-prior-art` states the current value correctly; `extension-seams`' header sentence
is false at HEAD.** Measured: `.unattended.conf:71` = `DIRECTIVES_FLOOR="13"`;
`.unattended.conf.example:62` = `"13"`. Both correct.

**What IS live is the finding underneath, and it is real.** Measured:
`grep -n 'example CORE_FLOOR\|example DIRECTIVES_FLOOR\|ROOT/.unattended.conf'
tools/unattended/unattended.test.sh` returns exactly two arms, at `:1156` and `:1158`, both reading
`$example`. **The installed conf the bar actually reads is graded by nothing.** Report the arm gap;
do not "fix" a value that is already right.

---

## 2. Recommendations refuted by another lens's evidence

### 2.1 `external-instruction-design` R1 counts pieces the run did not make

**`external-instruction-design` §6.2, R1:**

> Piece count = **files present at declared output paths**, derived, compared against requested N.
> Never the run's own tally.

**`hard-problems` §1.4** requires a different oracle:

> `pieces-complete` is met when **N**, read from the build README front matter **at the pinned BASE**,
> equals the number of DISTINCT pieces the **run's own diff** touched under the output globs read from
> that same BASE blob.

**Verdict: `hard-problems` wins, and R1 as written is unsafe for exactly this mode.** A
filesystem-presence count includes every piece produced by every PREVIOUS run of the same playbook.
The owner's ask is repeatable content against a growing corpus — the reference playbook plans 52 rows
over six months. Under R1, a run that produces **zero** new pieces passes whenever N or more pieces
already sit at the declared paths. `hard-problems` reproduced the shape it fixes (arm 4b in `repoC`:
a run that wrote `RUN.md`, `LIVE.md` and the ledger and no pieces at all scored `rc=0`).

**Second refutation of the same recommendation.** R1 does not declare a piece GRAIN.
`hard-problems` §3.5 measured a factor of three on one three-file diff — 3 paths, 2 piece
directories, 1 new piece — and concludes `outputs:` must declare a glob whose match IS one piece, with
the gate refusing a grain it cannot resolve. R1 is not implementable without it.

### 2.2 The witness field does not cost one capture group

**`external-instruction-design` §7, on fork 5** — the record's own loudest recommendation:

> **Add a mandatory witness field to the CHECK grammar** — `CHECK <why> · witness <field>` … **This
> costs one capture group in the checker and one column in the template**, and it is the difference
> between the 4% condition and the 97% condition.

**`corpus-anatomy` §3.5:**

> The checker's whole test is `has_check = "CHECK" in window`. … `CHECK` occurrences: 95 ·
> reason-joined form: 24 · other form: 71. … **If the kit's gate enforces the `<why>`, it will red 71
> of 95 tags in the very file it was derived from.**

**Verdict: the principle survives; the cost claim is FALSE.** Measured: the `` `CHECK` — `` form
occurs **23** times, so **72 of 95** CHECK tags fail even the weaker `<why>` rule (`corpus-anatomy`'s
71/24 is a ±1 selector artifact and its own point). Requiring a witness ON TOP means ~95 of 95 tags in
the reference playbook need rewriting. That is not one capture group; it is a migration of the
artifact fork 4 is deriving the template from.

**And the migration has no cheap grandfathering route in this repo.** `corpus-anatomy` §2.2 measured
the only worked precedent — hygiene check 12 — and found that grandfathering there is **by filename
date and is TOTAL EXEMPTION**: because the canon is exact equality, *"a grandfathered file is
FORBIDDEN to conform early"*, 0 of 11 grandfathered specs carry §10, while the soft
validated-when-present rule drained voluntarily in 15 of 33. **For a mode whose second verb is
"updates and tweaks EXISTING playbooks", a hard-equality canon is a wall.** `external` does not know
this; `corpus-anatomy` states it and does not connect it to `external`'s witness proposal. Together
they are one decision, and it is ranked #4 below.

### 2.3 The kind/extension narrowing dies on the owner's own ask

**`external-instruction-design` §6.3**, offered as the one recoverable slice of fork 2's conceded
class:

> **Partially recoverable, and worth proposing:** if each declared output path also declares a
> kind/extension set (`article -> .md`, `image -> .png|.webp`), a gate reds a `.py`/`.sh`/`.ts`/`.js`
> file appearing under a path declared as content.

**`hard-problems` §3.4:**

> a piece that is itself executable. Nothing stops a declared output path from holding `.sh` or `.py`,
> and for a playbook that generates tests — which the brief names as a content kind — that is the
> ORDINARY case rather than the abuse. **This is fatal to any content-based refinement of the gate.**

**Verdict: `hard-problems` wins, and the owner's ask settles it.** The build README quotes the ask
verbatim: *"repeating content (plans, images, videos, articles, web-pages, websites, **tests**)"*.

**What it changes for the design.** The narrowing is not a template rule and not a general gate arm.
At most it is an OPTIONAL per-path declaration a playbook may make about ITS OWN kinds, and the gate
must refuse to infer one. `external`'s framing — "converts the common case from unseen to red" — is
true only for playbooks that never emit executables, and the kit cannot know which those are.

### 2.4 Fork 1 got "no evidence against" from two lenses that did not look at the driver

**`corpus-anatomy` §6.7:** *"**No evidence against.** Nothing in either reference playbook depends on
how a run was authorized."*

**`external-instruction-design` §7, fork 1:** *"**No evidence against.**"* (with one note on
instruction hierarchy).

**`in-repo-prior-art` §8.1** treats fork 1 as a third `authorized-by:` member plus the uncompared
vocabulary, and **never addresses the attended half at all**.

**`extension-seams` §11:** *"**This is unresolved and it is the sharpest open question in the fork
set**: an attended playbook run that writes a `RUN.md` will red the bar; one that writes nothing has
no phase, no witness, no DoD and no `--close`."*

**`hard-problems` §2** reproduced it:

> An attended run therefore **cannot close through this driver**, full stop. … `check-unattended.sh`
> `fail 9 "a run-state file records no BASE, and the record is written by the run — an absent pin is
> not a satisfied one"`

**Verdict: `hard-problems` is right and the two "no evidence against" verdicts are worthless on this
fork, because they searched the reference playbooks for evidence about the driver.** Measured:
`fail 9` is at `check-unattended.sh:339`; `verb_close` opens at `unattended.sh:1602`; the
`authorization-reachable` override refusal is real. `hard-problems` option 3 — a non-driver attended
path that writes no run-state file — is the only survivor, and it answers what `extension-seams`
called unresolved.

**But its own counter-argument is unanswered by anyone.** Fork 1 ruled *"Two entry points, ONE
playbook artifact and ONE gate"*. Under option 3 the attended path leaves **no** mechanical record
that any leg reads — every run-state-keyed check (4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 19) sees nothing.
`hard-problems` proposes making the per-piece record a property of the TREE (hash-joined, tracked) so
both paths produce the same evidence. Nobody verified that the merge bar can read such a record
without a run-state file, and nobody costed it.

---

## 3. Claims that do not resolve

All against HEAD `0d88d5f2`, which is the tree all three source-reading lenses actually measured.

### 3.1 The wrong HEAD

`extension-seams` header: *"Measured against the worktree at … HEAD `d2a40aa`"*. **Measured:
`git rev-parse HEAD` is `0d88d5f2e0566927a8eb0faab35596e5aa0a1297`.** `d2a40aa` is `HEAD~1`. The
record's line numbers are consistent with `0d88d5f2`, so it measured the right tree and named the
wrong sha — which matters only because `AGENTS.md` §14 requires a review base pinned to an immutable
SHA and this one names a base the record did not use.

### 3.2 Cites that miss

| Record | Claim | Actual | Severity |
|---|---|---|---|
| `in-repo-prior-art` §8.4 | `PHASES_PASSKIND` at `unattended.sh:100` | **89** | 11 lines |
| `in-repo-prior-art` §1 | `scope_of` at `unattended.sh:120-129` | **123-132** | 3 lines |
| `in-repo-prior-art` §7.1 | `verb_attest` at `:1911-1932` | opens **1913** | 2 lines |
| `in-repo-prior-art` §8.2 | the scope comparison at `check-unattended.sh:723` | **722** | 1 line |
| `in-repo-prior-art` §8.5 | *"103 lines matching the bold-step shape"* | **110** | **wrong** |
| `in-repo-prior-art` §8.5 | *"35 distinct `GATE <leg>` strings"* | 58 raw / **52** tokens | **wrong** |
| `extension-seams` §0 F1 | the scope-cell hardcode at `check-unattended.sh:711` | **709** | 2 lines |
| `extension-seams` §2.1 | the closed-set `case` at `:793-797` | **794-797** | 1 line |
| `extension-seams` §2.3 | `unit_rows` at `:1055-1059` | **1056-1060** | 1 line |
| `extension-seams` §2.3 | `unit_ids_of` at `:1013-1018` | opens **1014** | 1 line |
| `hard-problems` §1.5 | `PHASES_PASSKIND` at `unattended.sh:88` | **89** | 1 line |
| `hard-problems` §1.1 | `build-complete` at *"`dod_met`, `unattended.sh:1763-1830`"* | arm is **1746-1800** | **materially wrong** |
| `hard-problems` §2.3 | `closing-review-recorded`'s `${#rb} -lt 7` at `:1846-1850` | **1831-1832** | 15 lines |

**The one that matters** is `hard-problems`' `1763-1830`. `dod_met` opens at `1703`; the
`build-complete)` arm runs `1746-1800` and `closing-review-recorded)` begins at `1801`. The cited
range starts mid-comment inside one DoD arm and ends inside a different one. The five terms it
enumerates are correct — `in-repo-prior-art`'s `1746-1800` is exact — but a spec author following the
cite reads two arms as one.

**The two `in-repo-prior-art` counts are wrong rather than off.** No selector I could construct yields
103 steps: I21's regex gives 110/110 distinct, `corpus-anatomy`'s gives 110/110, and the naive
space-requiring form gives 58. The record then uses 103 to argue *"the disagreement between two
hand-selectors over one file is itself the argument"* — the argument stands; the number supporting it
does not exist.

### 3.3 Cites that resolve exactly (so the misses above are not a pattern)

Spot-checked and confirmed byte-for-byte, so the spec can trust these: `unattended.sh:661/662`
(`check_waiver_scope`'s hardcode and `fail 45` — **all three** lenses correct);
`unattended.sh:795/796` (the closed-set arm and `fail 44`); `unattended.sh:1881-1882` (`dod_met`'s
default arm); `unattended.sh:1294` (`verb_abort`'s hard-coded agent list); `unattended.sh:1566`
(the four-kind parked regex); `check-unattended.sh:709/714` (the scope-cell hardcode and its refusal
text); `check-unattended.sh:339` (`fail 9`); `check-unattended.sh:806` (*"the checker column is
deliberately not joined"*); `.memory-tree.conf:178` (`ARMS_FLOORS`, seven gates — both lenses right
about different halves of the same line); `.memory-tree.conf:215` (`RECORD_UNBOUND_PIN="9"`);
`.memory-tree.conf:11/15` (`DISCIPLINES` / `FAMILIES`); `.lexicon.conf:92`; `check-memory-hygiene.sh:42`
(`GUIDE_CAP_BYTES=61440`); `gen_build_index.py`'s `record_paths`; `memory/backlog/TOOL.md:41/100/128`;
`ci.yml:68`; `check_content_plan.py:2422` (`step_re`) and `:404` (`LEG_RE`, `core's` in the
allowlist); `tests/test_v3_seed_profile.py:184` and `:192`. Also confirmed: **88** legs in
`tools/gate-legs.json`; govkit `88 · 71 claimed · 17 exempt` and `56 · 25 · 16 · 0`; **2** non-`.md`
tracked build records, exactly the two named; `grep -l '^authorized-by:' memory/builds/*/README.md`
matches **nothing**; `kit.toml`'s `placeholders` list is **6** against **7** live placeholders and
`optional_keys` omits `ANCHOR_SCOPE`, `UNITS_REGION_CUTOFF`, `DIRECTIVES_EXTRA_TABLE` — C9 live and
unfixed, as `extension-seams` says.

### 3.4 `corpus-anatomy`'s own prose counts, twice

- §3.1: *"`posts` survives in 5 places (L334, L514, L810, L814, L1163)"* — measured **4** (334, 514,
  814, 1163). L810 is not one. The finding itself is exact: `collections.json` has no `posts` key and
  `check_content_plan.py:2089` reads `_collection(collections, "journal")`.
- §3.5: *"reason-joined form: 24 · other form: 71"* — measured **23 / 72**.

Both are counts of derived populations written in prose, in a record that names that class as a defect
four times. Small, and it is the record's own argument for making the checker derive them.

### 3.5 The mandated first line reds check 21 — now measured on all five

`in-repo-prior-art` §10 predicted this for *"Both lens records in this build's `build/` folder"*.
There are five, and I ran it. Staged, `python tools/memory-tree/gen_build_index.py --print-bindings`
emits branch **A** for **all five**:

```
A  …-corpus-anatomy.md              first token TOOL-dScriptedRepeat-1 is not one of
                                    spec-audit diff-review journal research, and the line is not the none form
A  …-extension-seams.md             (same)
A  …-external-instruction-design.md (same)
A  …-hard-problems.md               (same)
A  …-in-repo-prior-art.md           (same)
```

The grammar is `memory/HYGIENE.md:249`: `**Serves:** <kind> <id>`, `<kind>` closed to
`spec-audit · diff-review · journal · research`. **This record is the sixth**, because the brief
mandated the same first line. `in-repo-prior-art`'s reading of the failure mode is also confirmed:
branch A fires before branch B, so *"no spec defines this id yet"* stays masked until the kind is
added. Fix all six to `**Serves:** research TOOL-dScriptedRepeat-1` when the set is folded, together
with the spec that DEFINES `TOOL-dScriptedRepeat-1`.

---

## 4. Same word, two things

Beyond §1.3's step count, three more:

- **"REUSE".** `in-repo-prior-art`'s verdict vocabulary means "wire through it unchanged" — but rows 3,
  4 and 9 reuse seams that exist **in gov**, and the kit's product is what an ADOPTER receives. Row 4
  is the live case (§1.6). The table needs a second column: reuse-in-gov versus reuse-in-an-adopter.
- **"the diff".** `in-repo-prior-art` §3 says the analogue of govkit's surface is *"a DIFF"* and
  reaches for the gate-leg `guard` pathspec precedent. `hard-problems` §3.1 measured that
  `BASE..HEAD` is wrong by up to **22.5x** (`aSiftedPlaybook`: 383 files against 17 authored) and that
  `--no-merges` is not the repair, because seven of `aSealedCaravan`'s merges carry combined-diff
  changes to `unattended.sh` and `check-memory-hygiene.sh`. Two lenses use "the diff" for two
  different populations and only one measured it.
- **"a park blocks the close".** The build README's fork-6 rationale, refuted by two lenses that then
  disagree about which verb blocks (§1.5).

---

## 5. Gaps — raised by one lens, unanswered by the lens that owned the question

1. **Set-scoped legs have no home.** `corpus-anatomy` §6.3 measured that every one of the four
   composition failures in the reference corpus was found by measuring the SET, not any piece:
   *"A DoD that counts pieces and declares each piece's legs green will ship N monocultured pieces and
   report GREEN."* Its §8 hands the question to the driver lens: *"Whether that is a new phase, a DoD
   item, or a `--close`-time leg is a driver question outside this lens."* **`extension-seams` never
   mentions set-scoped legs. `hard-problems` never mentions them.** `external-instruction-design`
   independently strengthens the need and also does not place them. `hard-problems`' recommended
   `pieces-complete` counts pieces and is silent on the set — so as specced today, the DoD ships the
   monoculture.
2. **Ten verbs, and only one lens counted.** `extension-seams` §2.5 found the verb set spelled in five
   places with three stale. **Verified exactly:** the header docstring (`:5-14`) names 9 and omits
   `--attest`; `fail 14` (`:2037`) names 9 and omits `--attest`; protocol §7 names **8** and omits
   both `--park` and `--attest`; the dispatch handles 10 (`--plan` at `:2030`, `--phase` at `:2035`,
   plus eight arms at `:2048-2055`). `AGENTS.md` calls it *"the four-verb driver"*. **No other lens
   noticed, and the brief inherited the error.** If fork 6 adds a verb it lands in this gap.
3. **The name `playbook` is already taken, and only `extension-seams` says so.** Verified:
   `.memory-tree.conf:11` `DISCIPLINES="playbook kickoff tooling deployer"` and `:15`
   `FAMILIES="playbook:PLAY …"`, plus `tools/playbook/` (the charter renderer),
   `tools/check-playbook-parity.sh`, `memory/map/features/playbook.md`. `in-repo-prior-art` cites
   `tools/playbook/render_playbook.py` and `tools/govkit/entries/playbook.kit.toml` across §2.3 and
   never notices that the mode value it recommends collides with all three.
4. **Nobody priced the template's own length.** `corpus-anatomy` §5.1 derives **12 REQUIRED** sections
   plus 9 optional. `external-instruction-design` §4 A2 requires *"a hard, derived word budget per
   addressable segment… computed and printed by the checker; never typed into prose"*, and §3 warns
   *"do not average them… a 7,000-word compromise that is still over the cliff"*. Nobody ran A2's
   budget over the R-set, and `corpus-anatomy` itself concedes R3 and R8 are ABSENT in HYBRID — so the
   12-required set forces a 245-line recipe to grow two sections it has no content for.
5. **Whether the merge bar can see an attended run at all.** §2.4. Raised implicitly by
   `extension-seams` §11 and answered by `hard-problems` only for the driver, not for the leg.
6. **Fork 3's "with its own commit".** `hard-problems` §1.5 is alone in observing that M6's *"Commit
   at the end of every pass"* does not hand you one commit per piece, and that *"commit counting is
   the wrong oracle for N"*. `in-repo-prior-art` §8.4 route 1 treats fork 3 as free.

---

## 6. What the forks got — tested versus assumed

| Fork | Actually tested by | Result |
|---|---|---|
| 1 mode + attended path | `hard-problems` (reproduced in `repoB`) | mode value cheap; **attended half must leave the driver**. `corpus-anatomy` and `external`'s "no evidence against" verdicts are non-evidence (§2.4). |
| 2 output paths | `hard-problems` (5 arms, `repoC`) | one observed RED (arm 2), one observed vacuous GREEN (arm 4b), one observed FALSE RED on the mandated memory update (arm 5). `external`'s narrowing refuted (§2.3). |
| 3 pieces as passes | `hard-problems` §1.5, `in-repo-prior-art` §8.4 | agree in substance: a piece is produced INSIDE `a unit built`. **New evidence neither cited:** `UNATTENDED-PROTOCOL.md:202-205` already states the pattern — *"`RESEARCHING` and `TESTING` are POSITIONS, not pass kinds"* — and `RUNNING` already exists as *"a run between named passes"*. Closer to settled than `extension-seams` §11 implies. |
| 4 corpus-derived then frozen | `corpus-anatomy` (both files, byte-level), `external` (23 queries) | `external` §6.5's caveat is the sharp one: **N=2, one repository, one author culture**, and the two contradict each other on exemplars and on a matter of fact. `in-repo-prior-art` §4 adds the one nobody else did: `adopt-lexicon.sh:93-97` refuses to re-scaffold over an existing conf, so **a derive-then-freeze artifact with no re-derivation mode is a one-way door** — and "updates existing playbooks" is half the feature. |
| 5 validity | `corpus-anatomy` (3 failing cases STAGED and observed), `hard-problems`, `extension-seams` | four measured defects in the reference implementation of exactly this rule, plus §1.3's selector split and §1.6's missing oracle. **The most damaged fork in the set.** |
| 6 proposal register | `in-repo-prior-art` §7, `extension-seams` §2.6 | premise refuted; ruling survives on other grounds; "distinct region" unresolved (§1.5). |
| 7 agnosticism | `hard-problems` §5, `corpus-anatomy` §6.6, `external` §7 | three-way agreement, cleanest fork in the set. `corpus-anatomy` §6.6 and `hard-problems` §5 independently land the same clarification: **the KIT is agnostic, the adopter's CHECKER is not and must not be.** Say it in the spec. |

---

## 7. RANKED — the design decisions still genuinely OPEN

Ranked by what it costs to start the spec set without the answer.

**1. Where `outputs:` and `pieces:` are declared — the playbook, the build README front matter, or a
named hybrid.** *(§1.1)* Fork 2 says the playbook; two lenses say the README and one of them flags
that as a deviation the fork does not state; the third lens's justification for the playbook is false
against source. **Settled by:** an owner ruling, with the mechanical input on the table — the driver's
*"No second `GIT show`: one blob, one parse"* rule at `unattended.sh:781`, and the fact that a
README-only declaration makes the playbook non-self-describing across runs, which is the opposite of
the mode's premise. Price the unproposed hybrid (README names the playbook path at BASE; the gate
reads the playbook at BASE) before choosing.

**2. Does the attended entry point produce any machine-readable evidence?** *(§2.4)* `hard-problems`
settled that it cannot be a driver mode. It did not settle what fork 1's *"ONE gate"* then means, and
no leg in `check-unattended.sh` can see a run with no run-state file. **Settled by:** deciding whether
the per-piece record is a property of the TREE (tracked, hash-joined to the piece, readable by a
merge-bar leg regardless of who invoked the run) or the attended path is explicitly evidence-free and
the protocol says so in its own header.

**3. The step SELECTOR and its anti-vacuity floor.** *(§1.3)* Nine steps or zero, depending on whose
regex. **Settled by:** the playbook declaring its own step selector plus a shrink-only minimum step
count, and then — per `AGENTS.md` §7 — running the candidate predicate over BOTH reference playbooks
and printing hits **and near-misses** before wiring it. Copy `check_content_plan.py:2496`'s floor and
its window rule (bounded at the next step **or heading**), both of which have observed failing cases
recorded in their own source.

**4. The `<why>`/witness grammar and its grandfathering rule — one decision, not two.** *(§2.2)*
`external` wants a witness; `corpus-anatomy` measured 72 of 95 tags failing the weaker rule already;
the only in-repo precedent grandfathers by TOTAL exemption, which forbids incremental adoption.
**Settled by:** choosing hard-equality-with-date-grandfathering versus validated-when-present, and
measuring the expected drain the way the `aMouldedFolio` census did (0 of 11 versus 15 of 33). A
hard canon and "updates existing playbooks" cannot both be true.

**5. Where the leg-runnability oracle comes from in an ADOPTER.** *(§1.6)* Verified: the unattended
kit never reads `tools/gate-legs.json`. **Settled by:** specifying a per-project leg-registry
declaration and a declared coverage mode in the lexicon's sense, with a **named refusal** — never a
silent skip — for an adopter that declares none. Add its cost to `extension-seams` §6.5's arm estimate,
which does not include it.

**6. `pieces-complete`'s shape, scope field, grain, and overridability.** *(§2.1)* Three sub-decisions,
none settled. `DOD_EXTRA` is out — `hard-problems` reproduced that a `:machine` extra item is
satisfied by a line the run writes (`unattended.sh:1881-1882`) while `--attest` refuses that same key
at `:1923` as self-certification, which is a live driver self-contradiction worth filing regardless of
this build. Open: (a) a ninth CORE item versus a third `DOD_CORE` field — note `checker_of`
(`unattended.sh:134`) uses shortest-prefix removal and would silently misclassify
`pieces-complete:machine:playbook` as machine; (b) the piece GRAIN glob, worth a factor of three;
(c) overridable at close or not — `extension-seams` §11 raises it, nobody answers, and both answers
are bad (an overridable count is a run certifying its own output; a non-overridable one can wedge a
run with nobody to interpret it). **Settled by:** a spec unit that names all three and observes the
failing case for each.

**7. Set-scoped legs — do they exist, and where do they run?** *(§5.1)* The one question raised by the
corpus lens and dropped by both driver lenses, with independent external evidence behind it.
**Settled by:** deciding between a `--close`-time leg, a DoD item, and a position — and note the
protocol already carries `RUNNING` (*"a run between named passes"*) and the POSITIONS precedent at
`UNATTENDED-PROTOCOL.md:202`, so this may need no new vocabulary at all.

**8. The spelling of the third mode.** *(§5.3)* `playbook` collides with the `DISCIPLINES` enum, the
`PLAY` family and the charter-renderer kit. **Settled by:** picking one at spec time —
`extension-seams` offers `recipe`, `script`, `runbook`, `serial`, and the build slug already leans
`script`. Costs nothing now and costs a rename later.

**9. Whether the mode set becomes a published constant.** Two lenses reached this independently:
`extension-seams` §3.2 calls `AUTH_MODES` *"the single highest-leverage mechanical change in this
inventory"*; `in-repo-prior-art` §8.1 calls the mode set *"the fifth vocabulary and the only uncompared
one"* and notes it is **not in the fork list**. **Settled by:** adding `AUTH_MODES` to the driver,
reading it in the leg through the existing `core_of`, and adding one membership branch to check 19 —
which today has no opinion on membership at all, so a README saying `playbok` and a record saying
`playbok` agree.

**10. Raising `READ_PATH_CEILING`.** *(§1.4)* 6,699 B against a 5,609 B precedent, and 94 B already
spent on this build's own generated row. **Settled by:** a ratified fork at spec time with the
argument beside the number, per the file's own convention — and note `TOOL-aDeclaredCeiling-1` (OPEN)
wants ceilings turned into declared pins first, so this build is arguing that row's case either way.

**11. The template's own length budget.** *(§5.4)* 12 required sections versus a measured 6,000-word
cliff. **Settled by:** computing `external` A2's derived budget over `corpus-anatomy`'s R-set and over
both references before fork 4's freeze, and deciding whether R3 and R8 are required-with-a-declared-null
or genuinely optional.

**12. The improvement register's home.** *(§1.5)* A fifth `park()` kind is cheap and does not give the
fork its "distinct region"; anything outside the run-state file lands outside the scope gate's
exemption set. **Settled by:** the owner reading "region" as "rows" or not — and by closing
`TOOL-aBoundedVerdict-6` (the 8 KB spill) first, which only one lens priced and which turns from
hypothetical to likely the moment a run emits proposals across N pieces.

---

## 8. What this lens did NOT check

- **No gate was written, staged-broken or observed RED.** Nothing here meets `AGENTS.md` §7's bar for a
  gate; `corpus-anatomy` and `hard-problems` are the only records in the set that staged failing cases,
  and I reproduced neither.
- **The full bar was not run.** Executed: `corpus_ids.py --report`, `govkit.py selfcheck`,
  `check-template-size.sh`, `gen_build_index.py --print-bindings`, plus `git` and `grep`/`python`
  reads. No `run-gates.sh`.
- **`external-instruction-design`'s external sources were not fetched.** Its 40-odd URLs, the AgentIF
  6,000-word cliff, the Compliance Gap's 97%/0–4% split, the 55-of-97 false-success figure and the
  SOP-Bench numbers are all taken on that record's word. It marks its own `UNVERIFIED` items
  (Microsoft's "seven steps", the "20–40%" formatting figure) and those marks were not audited either.
  **This is the largest unchecked surface in the set** and the only lens with no in-repo cross-check.
- **`hard-problems`' throwaway repos were not reproduced.** `repoB`, `repoC` and `repoP` are discarded;
  its five-arm scope table and its `--close` reproductions are taken on its word. Its in-tree
  measurements (13 runs, the 383-vs-17 ratio, the 2 non-`.md` records) — the two I could check —
  resolved.
- **`corpus-anatomy`'s three staged nicocares failing cases were not re-staged.** Its restoration claim
  was verified only to the extent that `git status --porcelain` in `C:/projects/nicocares/main` is
  empty, which is consistent with its md5 claim but does not prove it.
- **No adopter tree was inspected**, so every claim about what an adopter receives — including my own
  §1.6 verdict — rests on descriptors and grep, not on an install.
- **I did not re-litigate any of the seven forks.** Where a fork is reported as damaged, the damage is
  another lens's measurement, verified or refuted against source, not my opinion of the ruling.
