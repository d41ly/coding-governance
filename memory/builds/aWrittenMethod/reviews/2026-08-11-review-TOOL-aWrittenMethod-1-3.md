# Review aWrittenMethod-3 — Tier-2 on the cumulative diff landing on main

**Serves:** diff-review TOOL-aWrittenMethod-1 TOOL-aWrittenMethod-2 TOOL-aWrittenMethod-3 TOOL-aWrittenMethod-4 TOOL-aWrittenMethod-5 TOOL-aWrittenMethod-6  <!-- inferred: cumulative diff landing on the default branch -->

**Date:** 2026-08-11 · **Tier:** 2 · **Streams:** tooling
**Subject:** `git diff 7f614a1...HEAD` @ `b1ea6b9` — 38 files, +2212/-169. The cumulative branch:
the unattended kit's authorization hardening plus its new terminal-phase exemption
(`check-unattended.sh`, `unattended.sh`, both test siblings, `PROTOCOL.template.md`), the whole new
`check-method-carriers.sh` leg with its self-test and adopter seed, the six-registry move across
`HYGIENE.template.md` / `check-memory-hygiene.sh` / `adopt-memory-tree.sh` / `AGENTS.md` /
`memory/README.md` / `memory/HYGIENE.md`, and the aWrittenMethod spec set.
**Question asked:** does the authorization the kit exists to enforce still hold, and does the new
carrier gate work in the tree it ships to rather than only in gov's?

## 1. Verdict

**One open blocker, and it is a reinstatement — the exact defect the code comment two lines above it
still describes as fixed.** Review -2's H2 (check 9 recomputing the merge-base for a *terminal*
record, which bricks the bar on the first successful landing) was legitimate and was fixed by adding
a terminal branch at `check-unattended.sh:181`. But the fix folded the *absent-`base:` refusal* into
the non-terminal arm of the new fork. Since check 13 — the mandate assertion, the whole reason the
leg exists — is independently gated on `[ -n "$rb" ]` at line 231, a run-state file whose run-written
`phase:` is terminal and whose `base:` line is simply **deleted** now skips check 9 *and* check 13.
The leg exits 0 with no output. Three reviewers reproduced it independently against the leg's own
fixture shape, and all three confirmed the control: the identical fixture against `d0c0485` exits 1
with "a run-state file records no BASE, and the record is written by the run" (**B1**, ids 1/9/16).

Both inputs are inside the subject's reach. `phase:` and `base:` are facts the driver's own
`set_fact` writes into a run-WRITABLE `RUN.md`, and every *landed* record is terminal by definition —
so terminal is precisely the state the bar judges at the landing push. One deleted line lets an
unattended run merge and push with a mandate reading "I hereby authorize myself." The comment at
lines 182-184 asserting the exemption "SKIPS THE MERGE-BASE REPRODUCTION ONLY — never the mandate
assertion below" is false in that state, and the two terminal arms added to the self-test (orphan
base, reachable base) both *supply* a base, which is why this shipped green.

The high beside it is the other half of the same fork and is distinct: the exemption is **keyed on a
field the run writes** and replaces the reproduction with `git merge-base --is-ancestor "$rb" HEAD`,
which every commit the run authored on its own branch satisfies. The dropped
`[ "$mb" != "$(git rev-parse HEAD)" ]` arm existed verbatim to refuse "the run authored every byte a
mandate comparison would read", and no equivalent survives on the terminal path. Reproduced with the
base **present**: commit a forged mandate on your own branch, point `base:` at it, write
`phase: LANDED`, and check 13 compares your mandate against your own commit — exit 0 (**H1**, id 2).
The motivation for the exemption is sound; the replacement predicate is satisfiable by the subject of
the test.

The second high is the new carrier gate's adopter seed, and it is a clean
`vacuous-selector-empty-population` — the class this repo guards against explicitly in check 2 of the
very leg being seeded. `adopt-memory-tree.sh:148` measures `git ls-files`, i.e. **tracked** files
only, but the documented adoption order (`WIRE-INTO-PROJECT.md` §3, and the kit README) is
`cp -r` the kit → `--scaffold` → commit, with no `git add` in between. Three reviewers each ran the
documented order end to end in a scratch repo and got the same result: a header-only registry, zero
rows, and then a first-run red naming three carriers the adopter never wrote —
`tools/memory-tree/HYGIENE.template.md`, `README.md`, `adopt-memory-tree.sh`. That is precisely the
outcome the seed block's own comment says it exists to prevent, and the cost spec S2c rejected F4(b)
to avoid (**H2**, ids 5/10/17).

Below that, three mediums that all share one property — **they are true in gov's tree and false in an
adopter's**. Two unquoted `for` loops in the new leg word-split both the measured population and the
registry, so a carrier path with a space produces two simultaneous false reds that *cannot be cleared
by declaring the file* (**M1**). And the doc layer split in two directions: an editing artifact
welded the `kit/dogfood doc parity` description onto the tail of the new `method carriers` bullet in
`AGENTS.md` — the charter every agent loads as project instructions — so the charter now describes a
gate leg as doing something a different leg does (**M2**); and `WIRE-INTO-PROJECT.md` was not in the
commit at all, so the shipped adopter runbook still says five registries in three places, one of
which is a §6 **verification step** that instructs the adopter to delete the sixth (**M3**).

The through-line is the same one review -2 named, arriving from a new direction. Review -2's finding
was "every new guard is a second read of an input the run can write." This diff's is narrower and
sharper: **the fix for a review finding was landed without an arm for the state the fix newly
creates.** B1 is a regression introduced by remedying H2 of the prior review; H1 is the same fork's
other exit. And the new leg — a gate whose stated purpose is that a carrier cannot appear unnoticed —
was validated only against gov's own tree, where every path is ASCII, whitespace-free, and tracked.
Every finding at H2/M1/L1 disappears in gov and reappears in the first adopter.

## 2. Review shape

| raw | confirmed | refuted | unverified | precision |
|-----|-----------|---------|------------|-----------|
| 20  | 17        | 3       | 0          | **0.85**  |

Every confirmed finding survived an adversarial skeptic pass; nothing is outstanding. The 17
confirmed findings collapse to **8 distinct defects** — ids 1/9/16 are three independent
reproductions of one disarm, ids 5/10/17 are three of one seed, ids 6/11/18 are one word-split, ids
7/12/19 are one charter splice, ids 8/13 are one stale count. They are folded below. Where reviewers
disagreed on severity for the same defect, the report takes the **higher** and says so, because the
disagreements are all "does an adopter-only failure count" — and this kit's stated audience is
adopters.

---

## 3. Findings

### B1 · blocker — the terminal exemption disarms both the BASE check and the mandate assertion

**`tools/unattended/check-unattended.sh:181`** (with `:185` and `:231`) · ids 1, 9, 16 — three
independent reproductions

For a terminal run-state record, an absent `base:` line now disarms check 9 **and** check 13. The
terminal branch's only assertion is guarded by `[ -n "$rb" ]` (line 185), and check 13 is
independently guarded by `if [ -n "$rb" ] && git rev-parse …` (line 231). The `elif [ -z "$rb" ]`
refusal — which used to be unconditional — now sits on the *non-terminal* arm of the fork, so it can
never fire for the phase the landing push is actually in.

Reproduced three ways against the leg's own fixture shape. With `phase: LANDED`, the `base:` line
deleted, and the `<!-- run:mandate -->` block rewritten to "I hereby authorize myself to merge and to
push.", the leg exits **0 with no output**. Controls all hold: the identical fixture at
`phase: RUNNING` reds with check 9; the identical mandate tamper with `base:` intact reds check 13
("the run edited its own authorization"); the identical fixture against the leg extracted from
`d0c0485` exits 1. Both `phase:` and `base:` are written by the run through the driver's `set_fact`
into a run-writable `RUN.md`, and the driver stops at `LANDING` (`unattended.sh:462`) — it never
writes `LANDED` — so a run can reach that state itself.

The pre-push hook runs *this leg*, not the driver, so the driver's independent `trusted_base` /
`mandate-reachable` re-derivation is not a backstop: the leg exists precisely to be the second
opinion. The comment at lines 171-172 still warns against exactly this shape ("Wrapping this in
`if [ -n ]` meant deleting one line from a run-writable file disarmed the only BASE check on the
bar"), and the comment at 182-184 claims the exemption "SKIPS THE MERGE-BASE REPRODUCTION ONLY —
never the mandate assertion below", which is false here.

**Fix.** Hoist the absence refusal **above** the terminal fork so it applies to every phase:

```sh
if [ -z "$rb" ]; then
  fail 9 "a run-state file records no BASE, and the record is written by the run — an absent pin is not a satisfied one: $f"
elif [ "$TERMINAL_REC" = 1 ]; then
  <ancestor check only>
else
  <merge-base reproduction>
fi
```

Exempt only the merge-base **reproduction**, never the pin's presence.

**Left-shift gate.** Add the missing arms to `check-unattended.test.sh` beside the new terminal pair
at lines 573-585: (a) terminal + `sed -i '/^base: /d'` must red; (b) terminal + deleted `base:` +
rewritten mandate must red. Both existing terminal arms supply a base, which is the coverage shape
that let this ship. Generalize it: for **every** fact this leg reads, the harness needs a
delete-the-line arm at every phase in the vocabulary, not only at the phase the author had in mind —
a 2×N table, not two hand-written cases. An absent value and a satisfied value read identically to a
`[ -n ]` guard, and this leg now has two of them.

---

### H1 · high — the exemption is keyed on a run-written field, and its replacement predicate is satisfiable by the run

**`tools/unattended/check-unattended.sh:181`** · id 2

Distinct from B1: here the base is **present**. The terminal branch keys on `ph=$(fact_of "$f" phase)`
— a field the run writes — and substitutes `git merge-base --is-ancestor "$rb" HEAD`, which any
commit on the run's own branch satisfies. That drops both the `[ "$mb" = "$rb" ]` reproduction and
the `[ "$mb" != "$(git rev-parse HEAD)" ]` arm whose stated purpose was refusing "the run authored
every byte a mandate comparison would read".

Reproduced: commit a `RUN.md` whose mandate block reads "The run authorizes ITSELF to merge and to
push.", point `base:` at that run-authored commit, set `phase: LANDED` — the current leg exits 0; the
`d0c0485` leg exits 1 with "a recorded BASE is not the merge-base this history reproduces". Check 13
then does `git show "$rb:$f"` against that same run-authored commit, finds the mandate identical, and
certifies it.

The doc half also holds: `AGENTS.md:109` and `memory/guides/UNATTENDED-PROTOCOL.md` still describe
check 9 as "the recorded BASE is the merge-base git reproduces", with no exemption — the documented
contract now overstates the leg.

**Fix.** Do not let a run-written field select its own exemption. Record the landing merge commit as
a fact (`landed:`) and keep the full reproduction as `git merge-base <base-ref> <landed>^1` — the
default-branch first parent excludes every commit the run authored. Failing that, at minimum require
a terminal record's `$rb` to be an ancestor of the commit that **first added** `$f`
(`git log --diff-filter=A --format=%H -- "$f" | tail -1`), so the anchor cannot be a commit that
introduced or edited the run-state file. Update the check-9 description in `AGENTS.md` and
`memory/guides/UNATTENDED-PROTOCOL.md` to state the exemption either way.

**Left-shift gate.** The kit needs one adversarial harness, not another value-forging arm: a test
that plays the run *trying to authorize itself*, with `git update-ref`, `git symbolic-ref`,
`set_fact` and line-deletion in its toolkit, asserting the leg reds for each. Review -2's B1/H1 and
this review's B1/H1 all fall out of that single test. Complementary and cheap: a grep leg refusing
any `fact_of "$f" <name>` result used as a **branch selector** (as opposed to a compared value)
anywhere in `check-unattended.sh` — a gate must not let its subject choose which check runs.

---

### H2 · high — the method-carriers seed measures tracked files, and the kit is untracked when it runs

**`tools/memory-tree/adopt-memory-tree.sh:148`** · ids 5, 10, 17 — three independent end-to-end
reproductions

The seed enumerates `git ls-files`. The documented adoption order (`WIRE-INTO-PROJECT.md` §3:
`cp -r <gov>/tools/memory-tree <project>/tools/memory-tree` at line 109 → `--scaffold` at line 123 →
commit; and the kit README's "Adopt — new project") has no `git add` in between, and the adopter's own
closing output stages only `memory/ .memory-tree.conf` — not `tools/`. So at scaffold time the kit is
`?? tools/`, the seed matches nothing, and `memory/project/method-carriers.txt` is written with its
five comment lines and **zero rows**.

All three reproductions agree on the consequence: after `git add -A && git commit`,
`check-method-carriers.sh` exits 1 on check 3 naming exactly `tools/memory-tree/HYGIENE.template.md`,
`tools/memory-tree/README.md` and `tools/memory-tree/adopt-memory-tree.sh` — three carriers the
adopter never wrote. (Before the commit it reds on check 2 instead, empty population.) That is
verbatim the outcome the block's own comment at lines 138-141 says it prevents ("an adopter handed an
empty registry reds on install with carriers they never wrote. The seed is measured from THEIR tree
with the same predicate the leg uses"), and what `AGENTS.md:85` promises adopters ("SEEDED from their
own measured population"). It is also the cost spec S2c
(`spec/2026-08-11-spec-aWrittenMethod-4.md:59-62`) was written to avoid. The selector runs at the one
moment its population is guaranteed empty.

**Fix.** Seed from tracked **and** untracked-but-not-ignored — the same "git can see" population
`check-review-join.sh` already uses: `git ls-files --cached --others --exclude-standard`. And refuse
loudly (non-zero, or a printed warning) when the measured set is empty while the kit dir contains
files matching the predicate, rather than writing a header-only file that reads identically to "no
carriers exist".

**Left-shift gate.** The absent leg is an **adopter e2e that runs the runbook's documented order and
grades the effects**, exactly as `adopt-codebase-map.test.sh` and `adopt-unattended.test.sh` already
do for their kits — copy the kit unstaged, scaffold, commit, then assert `check-method-carriers.sh`
exits 0 *and* that the seeded registry has ≥1 non-comment row. The existing
`check-memory-hygiene.test.sh` scaffold arm runs `--scaffold` in a repo where the kit is not present
at all, so it can never observe this. Standing rule worth a grep leg: any `git ls-files` inside an
`adopt-*.sh` is measuring a population the adopter has not staged yet — the kit's own e2e is the only
thing that can tell you which spelling you need.

---

### M1 · medium — two unquoted `for` loops word-split both the population and the registry

**`tools/memory-tree/check-method-carriers.sh:77`** and **`:84`** · ids 6, 11, 18 — reported
low/medium/medium; taken as **medium**, because the kit ships to arbitrary trees where a space in a
doc filename is ordinary

`for c in $carriers` (line 77) and `for d in $declared` (line 84) iterate unquoted expansions, so
both the measured population and the declared registry are word-split on IFS. Reproduced three times
with carriers named `my notes.md` / `My Notes.md` / `Design Notes.md`: check 3 reports two undeclared
fragments (`Design`, `Notes.md`) **and** check 4 reports the same two as declared carriers that no
longer exist. Because the split hits both sides, adding the correct row to the registry does not
silence it — the state is unfixable short of renaming the file.

Note the collection step at line 52 handles spaces correctly (`while IFS= read -r f`), so the loss
happens purely in these two loops, and `git ls-files` does not quote a plain space, so nothing
upstream saves it. This is not a deliberate convention: the comment at lines 73-75 explains that
`for` was chosen over a `while` pipeline to keep `st=1` in the main shell — which a `while` over a
here-string also achieves, without splitting. The glob half of the claim is weaker (one reviewer's
`notes[1].md` probe did not fire, since nullglob is off and the pattern matched nothing); the
word-splitting half is fully reproduced and is the substance.

Fail-closed, not fail-open — which is why it is not higher.

**Fix.** Iterate line-wise, keeping the assignments in the main shell:
`while IFS= read -r c; do …; done <<<"$carriers"` and the same for `$declared`, skipping empty lines.

**Left-shift gate.** The self-test needs a **hostile-path fixture** — one carrier with a space, one
with a non-ASCII character (see L1), one with a `[` — asserted green when correctly declared. Better
as a standing arm than a one-off: this repo ships four kits that walk an adopter's tree, and gov's own
tree is all-ASCII and whitespace-free, so *no* gov-tree gate can ever exercise this. A shared
`hostile-paths` fixture builder used by every adopter e2e is the leg that generalizes.

---

### M2 · medium — the charter's gate-suite edit welded one leg's description onto another's bullet

**`AGENTS.md:84`** (and `:85`) · ids 7, 12, 19 — reported low/medium/medium; taken as **medium**

The commit replaced one bullet with two and split the wrong way. Line 84 is now the bare
`- kit/dogfood doc parity — \`tools/memory-tree/kit-dogfood-parity.test.sh\`` with its entire
description removed, and that description reappears verbatim as the trailing parenthetical of the new
`method carriers` bullet on line 85: "(the shipped `HYGIENE.template.md`/`SPEC-TEMPLATE.template.md`,
RENDERED for this install's prefix, equal this repo's installed copies … a surviving placeholder is
its own arm)". The sentence is ungrammatical at the splice, so it is an editing artifact, not an
intentional merge.

`AGENTS.md` is the charter every agent and every adopter reads first (`CLAUDE.md` is a bare
`@AGENTS.md` import). As written it tells a reader that `check-method-carriers.sh` performs the
adopter's template substitution and arms on a surviving placeholder — neither of which that leg does
— while the parity leg is left undescribed. Two-answers-to-one-question: the leg's own header and its
map dossier are correct; the charter is not.

Verified that nothing catches it. The only relevant signal is drift's `_charter_mentions_every_leg`
(`tools/drift-audit/drift_signals.py:84-104`), which asks only whether each leg's argv script *path*
appears somewhere in the gate-suite section — both paths do, so it stays quiet.

**Fix.** Move the parenthetical back onto line 84's parity bullet, and end the method-carriers bullet
at "…not a fluent paraphrase, and says so." Keep both argv paths named on line 85 so the drift
gate-credit signal keeps crediting the leg and its self-test.

**Left-shift gate.** Strengthen `_charter_mentions_every_leg` from *path present* to *path present in
a bullet whose text is non-empty after the path* — a one-line predicate change that would have caught
line 84 the moment its description was cut. Cheap and general: it turns "the charter names every leg"
into "the charter describes every leg", which is what the signal is actually for.

---

### M3 · medium — the shipped adopter runbook still asserts five registries, and one assertion is a verification step

**`WIRE-INTO-PROJECT.md:512`** (also `:127`, `:146-149`) · ids 8, 13 — reported low/medium; taken as
**medium**, because line 512 actively instructs the adopter into a red bar

The diff moved the `project/` registry count from five to six in `AGENTS.md`, `memory/README.md`,
`memory/HYGIENE.md`, `HYGIENE.template.md`, `check-memory-hygiene.sh` and `adopt-memory-tree.sh` —
but `WIRE-INTO-PROJECT.md` was not in the commit's changed-file list at all. It still says five in
three places:

- `:127` — "`project/` — which holds the gate's own five waiver registries (`*.txt`) **and nothing
  else**"
- `:146` — inside the `.gitattributes` block an adopter copies verbatim: "the scaffolder writes FIVE
  registries under project/, not two", plus the five-name enumeration
- `:512` — the adopter's own §6 **verification** checklist: "Nothing under `memory/project/` but the
  five `*.txt` waiver registries."

A scaffolded tree now yields six (`corpus-path-unresolved`, `curation-debt`, `id-orphan-waiver`,
`legacy-files`, `method-carriers`, `unarmed-branches`). Line 512 is the one that bites: an adopter
following their own verification step counts six, reads the sixth as a hygiene violation, deletes it,
and `check-method-carriers.sh` then exits 1 on check 1 ("an absent registry is not an empty one").
The functional CRLF pinning is unaffected — the `.gitattributes` glob is broad and still correct, only
its comment is stale — but that does not rescue 127 or 512. The spec's measured eight-assertion sweep
(S2d, `spec/2026-08-11-spec-aWrittenMethod-4.md:64-71`) enumerated five files, and this runbook was
not among them.

**Fix.** Update all three to six and name `method-carriers` in the enumerations, matching the wording
already landed in `memory/README.md` and the adopter-written copy in `adopt-memory-tree.sh`.

**Left-shift gate.** A pin gate on the spelled count: grep
`\b(five|six|seven) (\`\*\.txt\` )?(waiver )?registries\b` across `WIRE-INTO-PROJECT.md`,
`AGENTS.md`, `memory/**` and `tools/memory-tree/**`, and refuse when the set of values is not a
singleton — or, better, derive the number from the scaffolder's own registry list so the prose has one
source. This is the *same left-shift* review -2 proposed for the five-vs-six-facts pair in the
unattended protocol (its L1/L2); that gate was not built, and the identical class recurred in a
different file one commit later. Build it once, parameterized on the noun.

---

### L1 · low — the population loop drops non-ASCII paths under the default `core.quotepath`

**`tools/memory-tree/check-method-carriers.sh:52`** · id 3

`carriers=$(git ls-files | while IFS= read -r f; …)` reads unquoted `git ls-files` output. Under the
default `core.quotepath=true`, git C-quotes any non-ASCII path: `docs/méthode.md` prints as
`"docs/m\303\251thode.md"`, the `grep -lF "$DOC" "$f"` on that literal name fails on a nonexistent
file, the failure is swallowed by the `2>/dev/null` at line 59, and the file is **silently excluded
from the population**. Verified in a scratch repo: a tracked `méthode.md` containing
`BUILD-METHOD.md` yields nothing.

Checks 3 and 5 only iterate that population, so an undeclared carrier at such a path passes green.
That fails **open** in a gate whose stated purpose (header, lines 7-10) is that a new carrier cannot
appear unnoticed. The identical loop at `adopt-memory-tree.sh:148` seeds an adopter's registry, so a
non-English adopter's seed silently omits the same files — the shipped-kit path is what makes this
more than theoretical for a repo that today has no non-ASCII paths.

**Fix.** Read NUL-delimited with quoting off, in **both** places:
`git -c core.quotepath=off ls-files -z | while IFS= read -r -d '' f; do …`.

**Left-shift gate.** Same hostile-path fixture as M1 — add a non-ASCII carrier and assert it appears
in the population. Worth one repo-wide grep leg alongside it: any bare `git ls-files` piped into a
loop that then *opens* the emitted name is quoting-unsafe; the safe spellings are `-z` with
`core.quotepath=off`. That predicate is mechanical and applies to every kit here, not just this one.

---

### L2 · low — the scaffold-coverage arm was not extended to the sixth registry

**`tools/memory-tree/check-memory-hygiene.test.sh:713`** · id 14

The arm pins the registry names by literal loop:
`for r in legacy-files.txt curation-debt.txt id-orphan-waiver.txt corpus-path-unresolved.txt unarmed-branches.txt`
— five, not six. No other assertion in the repo requires the scaffolder to emit
`method-carriers.txt`: hygiene check 3 only *admits* `F:method-carriers.txt`
(`check-memory-hygiene.sh:240`) and never requires it, and `check-method-carriers.test.sh` builds its
own hand-seeded scratch repos without ever invoking `adopt-memory-tree.sh`. The scaffolded-tree arm
at line 716 runs only `check-memory-hygiene.sh` over the fixture, so a scaffolder that stopped
writing the sixth registry keeps the whole suite green in gov's tree — where the registry is
committed — and surfaces only in an adopter's tree as `check-method-carriers.sh` check 1.

That is exactly the "absent and present-and-empty read identically" class the comment at lines
711-712 cites as what hid three registries before, and the new registry is the one member not
protected. Coverage gap only.

**Fix.** Add `method-carriers.txt` to the loop, and assert the scaffolded file carries at least one
non-comment row — which also catches H2.

**Left-shift gate.** Derive the loop from the scaffolder rather than hand-listing it: grep
`adopt-memory-tree.sh` for `project/*.txt` write targets and require every one to exist in the
scaffolded fixture. A hand-kept inventory of a machine-derivable set is a parity pair with no leg,
which is the same shape as M3.

---

## 4. Fix order

1. **B1** — the disarm, with its two test arms in the same change. Nothing else in the unattended kit
   means anything while one deleted line silences the bar's only mandate assertion, and terminal is
   the phase the landing push is in.
2. **H1** — the same fork's other exit, in the same change. Fixing the absent-base case while leaving
   a run-written field to select its own exemption leaves the forgery standing. Ship the
   `landed:`-fact reproduction, or the first-added-commit ancestor floor, plus the doc correction in
   `AGENTS.md` and `UNATTENDED-PROTOCOL.md`.
3. **H2** — the seed. This one fires for **every** adopter following the documented order, and it
   defeats the whole stated purpose of the block. Land it with the adopter e2e, not alone: the e2e is
   the only thing that can observe the failure.
4. **M1 + L1** — the two path-handling defects in `check-method-carriers.sh`, in one commit with the
   shared hostile-path fixture. Both are the same defect family (the population is read as words, not
   as paths) and one fixture arms both.
5. **M2 + M3** — the doc layer. M2 is a two-line restore; M3 is three counts and two enumerations.
   Land the count-pin gate with M3, because review -2 proposed it for the same class and it was not
   built.
6. **L2** — the scaffold-coverage loop, ideally derived rather than extended.

## 5. What the gates could not see

**Not one of these eight reddened the bar.** Review -2 could at least point at one finding a gate
caught; this diff has none, and the reason is structural in two ways.

**First: the fix for a review finding shipped without an arm for the state it creates.** B1 is a
regression *introduced by remedying review -2's H2*. The remedy was correct in substance — a terminal
record's branch point really is gone by construction — and it arrived with two new self-test arms, so
it looked well-tested. Both arms supply a base. The state the fix newly made reachable (terminal +
absent base) was never enumerated, and the guard it disabled (check 13's `[ -n "$rb" ]`) is 46 lines
away in a different check. The missing discipline is not "write a test for the fix" — that was done —
it is **enumerate the state space the fix partitions**, and check every already-existing `[ -n ]`
guard on the same variable. Two `[ -n "$rb" ]` guards now depend on a value the run can delete; the
harness tests neither at the phase that matters.

**Second: the new leg was validated only in the tree it cannot fail in.** H2, M1 and L1 are all
invisible in gov — where every path is ASCII, whitespace-free, and tracked before any gate runs — and
all three fire in the first adopter. The kit's entire value proposition is that it works in *their*
tree, and the single highest-leverage leg it is missing is the one this repo already built twice, for
codebase-map and for unattended: **an adopter e2e that runs the runbook's documented order and grades
the effects in the adopter's tree, not the exit code.** That one leg catches H2 outright, and with a
hostile-path fixture it catches M1 and L1 too — three of eight defects, including the high, from a
single arm the repo already knows how to write.

The doc findings (M2, M3) close the loop on the same theme from the other end: both are hand-kept
prose restating a machine-derivable fact, both were proposed as pin gates in the *previous* review's
left-shift section, and neither gate was built. The class recurred within one commit.
