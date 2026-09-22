**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 2 (the FOLD review)

**Range:** `60c40b62021384b49cf6aa361fa47c58da680ecb...a564ce2b98f4c8ea645b5f885ab9f26d535b9e19` —
the round-1 fold itself, not the whole build. 24 files, 1426 insertions, 76 deletions. **ROUND 2.**

**Review shape:** raw 17 · confirmed 16 · refuted 1 · unverified 0 · precision 0.94. The 16 confirmed
findings collapse to **9 distinct defects** — four clusters were found independently by two to four
lenses each, and that corroboration is recorded per finding rather than inflating the count.

## Verdict: BLOCKED

Two blockers, two highs. **Both blockers are the same shape, and it is the shape this round existed
to catch: the fix traded one silent failure for another.** Round 1's M1 found that `dod_met`'s
`set_checks` escape compared RAW text against the kit's own shipped template line, and therefore told
an author who had declared nothing that they had declared some. The fold fixed that field. It then
wrote a brand-new parser for the SIBLING field, `piece_checks`, eighty lines up — without the strip it
had just spent five comment lines arguing for. Round 1's HIGH 4 found that `--counts` read the
working-tree playbook the run can edit. The fold pinned two of the three fields it reads from that
file, and left the third — the one the new non-overridable Definition-of-Done term keys on.

Neither blocker is caught by anything in the diff. The leg does not red in either state (check 8
`note`s and never `fail`s; measured `rc=0`), and all three playbook fixtures in the test corpus —
`playbook.fixture.md`, the driver suite's `content/pb.md`, and the new `content/pb-first.md` — spell
both declaration keys with no trailing comment, so the 56-assertion leg suite and the 656-assertion
driver suite pass over the one spelling that cannot hit it. That is the population-of-one defect the
fold's own commit message says hid the round-1 blockers, reproduced in the corpus written to close
them.

### What the fold got right, because judging the repairs is the job

Ten of the sixteen repairs are correct, complete and carry no new defect, and three are better than
the finding asked for.

- **`drop_leg_row` (HIGH 2) is a correct and complete fix.** The quoted `case` pattern genuinely
  defeats a leg name spelling a glob — measured: legs named `.*` and `[a-z]*` both stay literal, and a
  leg named `tools/lint.sh` still matches. The temp-file rewrite cannot lose a record: `mv` is the
  function's last command so its status IS the return status, `stage_or_fail` follows on every path
  that reaches it, and the index mode stays `100644` (measured; `mktemp` yields `644` on this box).
  It is armed on BOTH writers, which the finding asked for.
- **The `unchecked` branch ordering is right.** unrecorded → run-scope → stale → failed → unchecked →
  verified. No piece that should read `stale` or `failed` can reach `unchecked`: both are tested and
  `continue` before the `piece_checks` loop runs.
- **The `#`-strip does NOT swallow a real declaration.** It requires WHITESPACE before the `#`, so
  `["a#b"]` and `["a", "b#c"]` both survive intact (measured). The comment at `unattended.sh:2116`
  says exactly this and is correct.
- **`--counts` positional 4/5 breaks no caller.** `dod_met:2052` is the only `--counts` caller in the
  tree; the merge-bar leg runs bare. Grepped.
- **The renumber is complete in code and in the arms.** Live `fail 26` / `fail 27` at
  `check-unattended.sh:1299-1347`, with no surviving `fail 22` / `fail 23` in the renumbered blocks.
  It is the PROSE that was missed, twice — findings 8 and 9 below.
- **Every one of the 42 new assertions reds against the pre-fix leg.** Staged: the current
  `check-playbook.test.sh` run against `check-playbook.sh@60c40b62` fails 12 arms, including all four
  new join arms and the B2 population arm. No new arm passes for the wrong reason. Their gap is
  coverage, not arming.
- Term 2b's `head -1` → `grep -m1 '^pieces='` (HIGH 5), the `_blob` liveness refusal and the `_rr`
  emptiness message (M2), the trimmed `_declared` escape (M1), the `playbook-sha` blob-sha fix (M6),
  the dead `unrecorded` term's removal (M7) and the `DOD_NO_OVERRIDE` declared set (AC7) are all
  correct as filed.

---

## BLOCKER 1 — `piece_checks` gets no trailing-comment strip, so the kit's own shipped template line grades every piece `unchecked` and wedges the close with no reachable exit

**`tools/unattended/check-playbook.sh:213`** *(round-1 ids 1, 5, 9, 15 — four independent lenses)*

The new per-piece reader parses the declared leg list with `tr -d '[]",'` and nothing else. Its two
siblings — `check-playbook.sh:288` and `unattended.sh:2116` — both carry
`sed 's/[[:space:]][[:space:]]*#.*$//'`, and `unattended.sh:2110-2114` spends five comment lines
arguing for exactly that strip on exactly this ground.

`tools/unattended/PLAYBOOK-TEMPLATE.template.md:55` ships the line an adopter fills in place:

```
piece_checks = []    # the checks that run over ONE piece.
```

Measured on the live tree by mutating the shipped fixture and reverting:

| fixture line | `--counts` result |
|---|---|
| `piece_checks  = ["fixture-shape"]` (as shipped) | `pieces=2 verified=2 failed=0 stale=0 unrecorded=0 unchecked=0` |
| `piece_checks  = ["fixture-shape"]  # the checks that run over ONE piece.` | `pieces=2 verified=0 … unchecked=2` |
| `piece_checks  = []    # the checks that run over ONE piece.` | `pieces=2 verified=0 … unchecked=2` |
| `piece_checks  = []` | `pieces=2 verified=2 … unchecked=0` |

The comment word-splits into eight phantom leg names — `#`, `the`, `checks`, `that`, `run`, `over`,
`ONE`, `piece.` — enumerated directly from the shipped pipeline. Human mode prints them verbatim:

```
playbook: unchecked — tools/unattended/fixture-pieces/one/piece.md records no verdict for declared leg(s): # the checks that run over ONE piece. (tools/unattended/playbook.fixture.md)
```

**A playbook declaring NO per-piece checks is graded as declaring eight.** The impact chain is
code-verified end to end: term 2b (`unattended.sh:2090`) returns 1 on `_xc != 0` for
`pieces-complete`; this same diff added `pieces-complete` to `DOD_NO_OVERRIDE` (`unattended.sh:184`);
`verb_close`'s override loop (`unattended.sh:1906`) `fail 21`s on any member (`:1912`). So
`--override` is refused and **`--abort` is the only exit** — for an unattended run with nobody present
to make the call. Nothing warns first: the leg emits this through `note`, not `fail`, and I measured
`rc=0` in the wedged state, so the merge bar stays green while the close is unwinnable.

This is M1's defect one field over, introduced by the commit that fixed M1.

**Fix.** Give `pchk` the identical pipeline its two siblings have:

```sh
pchk=$(printf '%s\n' "$body" | sed -n 's/^piece_checks[[:space:]]*=[[:space:]]*//p' | head -1 \
       | sed 's/[[:space:]][[:space:]]*#.*$//' | tr -d '\r"' \
       | sed 's/^\[//; s/\]$//; s/,/ /g' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
```

Better — and this is what the class demands rather than the instance — extract ONE `declared_list()`
helper and call it from `check-playbook.sh:213`, `check-playbook.sh:288` and `unattended.sh:2116`.
Three spellings of one parse is why the strip landed in two of them; a fourth edit will desynchronise
them again. The helper cannot live in a shared file (the kit is copy-installed standalone), so inline
it once per script and gate the two copies against each other.

**Left-shift gate.** A `check-playbook.test.sh` arm that appends the template's OWN comment to BOTH
declaration keys in the fixture and asserts `verified 2 · unchecked 0` with no `set checks unrecorded`
line. Stronger: a leg check that reads every `*_checks` key out of `PLAYBOOK-TEMPLATE.template.md` and
runs each parser over the template's own shipped line, asserting the parsers agree — the template is
the one input every adopter starts from, and no hand-written fixture will keep carrying its comment.

---

## BLOCKER 2 — `--counts` was handed BASE-pinned `grain` and `records` but not `piece_checks`, so the non-overridable item is defeated by one uncommitted line

**`tools/unattended/check-playbook.sh:213` / `tools/unattended/unattended.sh:2052`** *(round-1 ids 6, 14)*

HIGH 4's fix pins two of the three fields the enumerator reads off the playbook. `gr` takes
`COUNTS_GRAIN` (`:206`), `rr` takes `COUNTS_RECORDS` (`:209`), and `pchk` at `:213` comes straight off
`$body` — `tr -d '\r' < "$pb"`, the **working tree** file (`:109`).

REPRODUCED on the live tree, with the records genuinely carrying no verdict and both facts supplied:

```
# A: verdict stripped from one record, BASE-pinned grain+records supplied, playbook untouched
pieces=2 verified=1 failed=0 stale=0 unrecorded=0 unchecked=1

# B: identical call; ONE UNCOMMITTED line deleted from the working-tree playbook
#    (git diff --stat: 1 file changed, 1 deletion)
pieces=2 verified=2 failed=0 stale=0 unrecorded=0 unchecked=0
```

With `pchk` empty the `for lg_ in $pchk` body never executes, `miss_` stays empty, and every
hash-joined record falls through to `v=$((v+1))`. Term 2b and term 3 are then both satisfied and
`pieces-complete` goes MET — **the item this same diff made non-overridable on the stated ground that
"an override on it is the run certifying its own output"** (`unattended.sh:178-181`). The run
certifies its own output anyway, without needing an override.

The uncommitted route is live. `check_clean` is wired at `unattended.sh:1399` (`--landed`) and `:1595`
(preflight, `|| true`) and **nowhere in `verb_close` (`:1865`)** — grepped. So the tree may be dirty at
exactly the moment the count is taken, and the edit reverted before `--landed`. A committed edit works
regardless, since BASE is not HEAD. Nothing else closes the gap: `playbook-sha` is written (`:2669`)
and read by nothing, and `check-unattended.sh` has no playbook-immutability check.

The fix's own comment at `unattended.sh:2044-2049` states the threat model it then leaves open: *"the
run is the actor that can make that edit."* `memory/builds/dScriptedRepeat/README.md:175` states
**"`--counts` takes the recorded FACTS, not the working-tree playbook"**, which is true of two fields
out of three.

**Fix.** Close the CLASS, not the instance. In `--counts` mode read `$body` from the BASE blob rather
than from disk — `body=$(GIT show "$base:$pb" | tr -d '\r')` — passing the base as a sixth positional.
Then no future declaration added to that block can be forgotten, and `COUNTS_GRAIN`/`COUNTS_RECORDS`
become redundant rather than a list to keep in step. If the per-field shape is kept instead: add
`AUTH_PIECE_CHECKS` beside `AUTH_RECORDS` (`unattended.sh:946`), a `piece-checks` fact in
`verb_preflight` (`:1741`), a `COUNTS_CHECKS` positional, and correct README:175 to name which fields
are pinned.

**Left-shift gate.** A driver arm that runs `--close` twice over the same tree, once with the
committed playbook and once with `piece_checks` deleted from the WORKING TREE only, asserting the
verdict does not move. Plus a source-level arm asserting `check-playbook.sh` performs no read of
`"$pb"` off disk while `COUNTS_FOR` is set — the same shape as the existing
`grep -q "grep -m1 '^pieces='"` arm at `unattended.test.sh:1748`, which is the pattern this suite
already uses for exactly this class.

---

## HIGH 1 — `record_set` still interpolates a caller value into a sed REPLACEMENT, forging a verdict row past the newline guard added twelve lines above it

**`tools/unattended/unattended.sh:2606`** *(round-1 id 3, plus a second channel found this round)*

HIGH 2's fix removed the caller-supplied interpolation from the sed ADDRESS. It left one in the sed
REPLACEMENT, where GNU sed 4.9 (the sed on this box) expands a two-character `\n` into a real newline.

REPRODUCED end to end against the shipped driver in a throwaway repo:

```
$ unattended.sh --record-set - --records-root recs --run R1 --leg first  --verdict PASS --set 'AAAA'
$ unattended.sh --record-set - --records-root recs --run R1 --leg second --verdict PASS \
      --set 'AAAA\nleg forged · verdict PASS'
unattended: set verdict recorded — second PASS for R1

# recs/set-R1.md
run: R1
set: AAAA
leg forged · verdict PASS      <-- nothing wrote this

## Verdicts
leg first · verdict PASS
leg second · verdict PASS
```

`grep -qxF -- "leg forged · verdict PASS"` matches — verbatim the join `dod_met:2145` and
`check-playbook.sh:295` both perform. The new guard at `:2589` tests
`printf '%s' "$leg$verdict$runid$hashes" | wc -l`, which counts newline BYTES; I measured it returning
`0` for a literal `\n`. The separator guard (`case "$leg$runid"`, `:2592`) and the bypass guard
(`printf '%s%s' "$leg" "$runid"`, `:2593`) skip `$hashes` entirely.

Two more channels on the same line, both measured:

- `--set '&&&'` → `set: set: AAAAset: AAAAset: AAAA`. An `&` in a sed replacement inserts the whole
  match.
- `--set 'a|b'` → `sed: -e expression #1, char 19: unknown option to 's'`, and **`record_set`
  continues and reports `set verdict recorded — fourth PASS for R1`**. The `sed -i` exit status is
  unchecked, so a corrupt or unwritten `set:` line is reported as a successful record. That is the
  skip-that-looks-like-a-pass class this kit gates against everywhere else.

**A second, independent forged-row channel found this round, in the SIBLING writer, on a path with no
sed at all.** `record_piece`'s newline guard (`:2532`) covers `$leg$verdict$piece` and NOT `$pbsha`,
which is caller-supplied through `--playbook-sha` on the attended path:

```
$ unattended.sh --record-piece - --records-root recs --path pcs/one.md --leg L --verdict FAIL \
      --playbook-sha "$(printf 'deadbeef\nleg L2 · verdict PASS')"
unattended: piece verdict recorded — L FAIL on pcs/one.md

# recs/pcs~one.md.md
playbook-sha: deadbeef
leg L2 · verdict PASS          <-- a PASS beside an honest FAIL, on the FIRST write

## Verdicts
leg L · verdict FAIL
```

The comment at `:2584-2588` claims "same three refusals, same reasons, same wording as the piece
writer's". Neither writer covers all of its own caller-supplied fields, and the parity that comment
claims is the reason nobody looked.

Reachability: `--set` (`RP_SET`, parsed `:2993`) and `--playbook-sha` (`RP_PBSHA`, `:2991`) both reach
their writers through the `RP_ROOT` branch (`:2625`, `:2656`), which is evaluated BEFORE `check_slug`
and the run-state lookup. The slug path derives both values itself and is safe. The attended path is
the kit's declared second caller, shipped in `.claude/skills/unattended/SKILL.md:349` — this diff
edited that very line.

**Fix.** Stop rewriting `set:` with `sed`. Reuse `drop_leg_row`'s shape — a `case`-filtered temp-file
rewrite that emits `printf 'set: %s\n' "$hashes"` for the matched line — so no caller value ever
reaches a regex or a replacement, and do the same for `record_piece`'s `hash:` re-stamp at `:2559`
even though `$h` is currently derived. Then extend all three field guards in both writers to span
**every** caller-supplied field: `$hashes` in `record_set`, `$pbsha` and `$runid` in `record_piece`.
The §9 rule is one composite write-guard on every path that stores parseable content; two writers with
two different field sets is the bare-sibling-path hole that rule names.

**Left-shift gate.** A source-level arm asserting each writer's guarded field set equals its parameter
list minus the derived ones — the "declared population, asserted in both directions" shape §7 already
requires of tooling. Behaviourally: arms passing `--set` and `--playbook-sha` values spelling a
newline, ` · `, `--no-verify`, `&` and `|`, each asserting the record's blob hash does not move and the
verb refuses.

---

## HIGH 2 — `--counts` positional 4/5 are advisory, and `AUTH_RECORDS` has no emptiness refusal, so the BASE pin silently reverts to the file it exists to distrust

**`tools/unattended/unattended.sh:2051` / `tools/unattended/check-playbook.sh:206,209`** *(round-1 id 2)*

`[ -n "$COUNTS_GRAIN" ] && gr="$COUNTS_GRAIN"` — empty silently keeps the working-tree parse, with no
liveness assertion on either side of the call. Measured, with the fixture's working-tree grain narrowed
to one piece:

```
--counts <pb> dScriptedRepeat "tools/.../fixture-pieces/*/piece.md" "tools/.../fixture-records"  -> pieces=2 verified=2
--counts <pb> dScriptedRepeat "" ""                                                              -> pieces=1 verified=1
```

So the supply channel is load-bearing and optional at once, with no probe on the difference. `dod_met`
gained a `_counts`-empty guard at `:2054` this round and no sibling guard on `_gr`/`_rrf` — verified by
reading `:2044-2060`.

Two reachable routes to an empty fact:

1. **No `AUTH_RECORDS` refusal.** `AUTH_OUTPUTS` gets one (`:952`) and `AUTH_GRAIN` gets one (`:956`,
   `fail 46`). `AUTH_RECORDS` appears at `:359`, `:946` and `:1741` and **nowhere as a refusal** —
   grepped. A recipe playbook declaring a grain and no records root passes `check_authorization`,
   `set_fact records ""` writes an empty fact, and `dod_met`'s `_rrf` is empty at close.
2. **A run-state file with no `records:` line at all** — every run started under any earlier driver
   revision. `verb_close` calls none of preflight's fact writers (grepped: no `set_fact` for grain or
   records anywhere in it), so the fact is never backfilled. The kit is copy-installed, so a run in
   flight across the upgrade loses the pin silently.

This is the `inputs-inside-the-subjects-reach` class the gotchas checklist selects for this diff,
reopened through the door the fix's own comment (`:2049`) says is closed.

**Fix.** Refuse rather than fall back. Add an `AUTH_RECORDS` emptiness `fail 46` beside the
`AUTH_GRAIN` one at `:956`. In `dod_met`, block with a named message when `_gr` or `_rrf` is empty in
recipe mode, in the same shape as the `_counts`-empty guard at `:2054`. In `check-playbook.sh`,
distinguish "not supplied" from "supplied empty": require both or neither when `--counts` is given, and
refuse the mixed form. (Blocker 2's BASE-blob fix subsumes all of this and is the better repair.)

**Left-shift gate.** A driver arm running `--close` against a run-state file whose `records:` line has
been deleted, asserting a NAMED refusal rather than a verdict. A leg arm passing
`--counts <pb> <run> "" ""` and asserting a non-zero exit with a named message.

---

## MEDIUM 1 — both record writers re-stamp the record and then take the "already recorded, unchanged" early return, which skips `stage_or_fail`

**`tools/unattended/unattended.sh:2606-2611` and `:2559-2566`** *(round-1 ids 10, 17)*

REPRODUCED byte for byte with the shipped driver:

```
$ unattended.sh --record-set - --records-root recs --run R1 --leg S --verdict PASS --set 'aaa,bbb'
$ git add recs && git commit -m rec
$ unattended.sh --record-set - --records-root recs --run R1 --leg S --verdict PASS --set 'ccc,ddd'
unattended: set verdict already recorded, unchanged — S

worktree:   set: ccc,ddd
index:      set: aaa,bbb        (git show :recs/set-R1.md)
git status: M recs/set-R1.md
```

The `sed -i "s|^set: .*|set: $hashes|"` re-stamp at `:2606` runs BEFORE the `want`-row scan whose
`return 0` at `:2611` never reaches `stage_or_fail` at `:2616`. `record_piece` has the identical shape
with its `hash:` re-stamp at `:2559`.

The reachable path is the exact repair L1's new refusal forces. `dod_met:2158` reds on a SUPERSEDED
set; the repair is to re-run the set check, which yields the same verdict, which always takes the
early-return arm. So the re-stamp produces a working-tree-only diff in precisely the case that matters.
`dod_met`'s comparison reads `_set` and the per-piece `hash:` lines off the working tree on both sides,
so `set-checks-recorded` goes MET on bytes that are not in the index — while `stage_or_fail`'s own
message (`:1072`) says the leg's per-run population IS the index. `records-current` (`:2012-2024`)
checks marker-region well-formedness only and notices nothing. `--close` has no clean-tree guard, so
the run reaches LANDING and is then refused by the lander with a message blaming the operator's tree —
the shape `unattended.sh:1975` already records as a defect.

The message is also literally false at that point: the file WAS modified.

**Fix.** Move the re-stamp below the idempotence loop in both writers, or call `stage_or_fail "$rec"`
on the early-return path when the re-stamp changed the file. Change the message to distinguish
"verdict unchanged, member list refreshed" from a genuine no-op.

**Left-shift gate.** An arm that records a set PASS, commits, re-records the SAME leg and verdict with
a different member list, and asserts `git diff --name-only` is empty and `git show :<rec>` matches the
worktree. The same arm for `record_piece` with a moved `hash:`.

---

## MEDIUM 2 — the leg's new `set_checks` reader has neither the declared-null escape nor the trailing trim its driver sibling has, so two readers of one field give two answers forever

**`tools/unattended/check-playbook.sh:288-292`** *(round-1 ids 4, 7, 11)*

`dod_met:2120` escapes `''|'[]'|'none'*` after trimming both ends. The leg's reader strips comments,
brackets and commas, then tests only "is the result all whitespace" — no `none` arm, and the `s/\]$//`
anchor misses whenever any byte follows the bracket. All three states measured on the live tree by
mutating the fixture and reverting:

| declaration | leg output |
|---|---|
| `set_checks    = none — nothing distinguishes one piece from another` | `set checks unrecorded — …/set-dScriptedRepeat.md carries no verdict for declared check(s): none — nothing distinguishes one piece from another` |
| `set_checks    = []   ` (trailing spaces) | `… declared check(s): ]` |
| `set_checks    = ["fixture-distinct", "second-check"]  ` | `… declared check(s): second-check]` |

The last is the worst: **the final member of any multi-entry list becomes permanently unsatisfiable**
once a trailing byte follows the `]`. The first is the spelling the unit's own spec prescribes —
`memory/builds/dScriptedRepeat/spec/2026-08-20-spec-dScriptedRepeat-7.md:137`, AC6, which names
`bash tools/unattended/check-playbook.sh` in the criterion. The acceptance ledger's U7 AC6 row
(`…-acceptance-ledger.md:53`) evidences `unattended.sh` only, so the leg half of that criterion is
**unobserved** — which is how it shipped wrong.

The leg exits 0 in all three states (check 8 `note`s, never `fail`s), so AC6's literal "passes" claim
survives and the bar does not red. The cost is a permanent false gap report on the only grading surface
the attended path has, which trains its reader to ignore the one signal that path gets. That is
`two-answers-to-one-question`, selected for this diff by the checklist.

**Fix.** Give the leg `dod_met`'s escape verbatim and trim before the bracket strip:
`sed 's/^[[:space:]]*//; s/[[:space:]]*$//'` ahead of `s/^\[//; s/\]$//`, then
`case "$schk" in ''|'[]'|'none'*) ;; *) <the block> ;; esac`. This is the same `declared_list()` helper
Blocker 1 asks for; do it once, for all three call sites.

**Left-shift gate.** Leg arms mutating the fixture's `set_checks` to `none — <why>` and to
`["a", "b"]  ` (trailing space), asserting no `set checks unrecorded` line and both members satisfied
respectively. A cross-reader arm is stronger: assert `check-playbook.sh` and `dod_met` return the same
declared list for a table of ten spellings — the two parsers exist to answer one question, and nothing
currently makes them agree.

*Related, not filed separately:* `for lg_ in $pchk` (`:255`) and `for _sl in $(… tr -d '[]",')`
(`unattended.sh:2141`) are unquoted expansions, so a declared leg name spelling a glob is
pathname-expanded against the CWD. Latent today — `fixture-*` matched nothing and stayed literal in my
test — but nothing validates the member shape of either key. Fold a `case` shape refusal into the same
helper.

---

## MEDIUM 3 — the codebase-map dossier still routes readers to checks 22 and 23, which now denote two unrelated checks

**`memory/map/features/playbook-mode.md:81,85`** *(round-1 id 16)*

`:81` says the protocol and Skill verb carriers "are joined to the declaration by leg check 22"; `:85`
says "check 23 joins it to the `park()` call sites in BOTH directions". Both moved in this commit: the
verb-set join is now `fail 26` (`check-unattended.sh:1299-1308`), the parked-kind join `fail 27`
(`:1328-1347`). Live 22 and 23 are dUnstalledConvoy's rescope/roster join (`:1062-1076`) and dispatch
write-set join (`:1179-1216`).

**The dossier WAS edited in this diff** — 24 lines changed — and the numbering prose was left standing:
`git show 5b0d73c0 -- memory/map/features/playbook-mode.md | grep '^[+-].*check 2'` returns nothing, and
the file contains no occurrence of 26 or 27. A reader chasing "check 22" lands on an unrelated check and
concludes the join does not exist — the same wrong-pointer failure M3 was raised for, one document over.
Nothing gates dossier prose against the leg's numbering, so it will not self-correct.

**Fix.** `leg check 22` → `leg check 26` on `:81`, `check 23 joins it` → `check 27 joins it` on `:85`.
Better, per the charter's *point at the source, or gate the pair*: name each check by its subject ("the
verb-set join", "the parked-kind join") and cite the number once, beside the leg.

**Left-shift gate.** A memory-hygiene or codebase-map leg asserting every `check <N>` reference in
`memory/map/features/*.md` resolves to a live `fail <N>` in the named script. The numbers are now
demonstrably mobile, and this is the second document in two rounds left pointing at a stale one.

---

## LOW 1 — two of `record_set`'s three new field guards do not hold what their message claims

**`tools/unattended/unattended.sh:2594`, and identically `:2537`** *(round-1 id 12)*

The bypass-flag refusal says *"the gate greps these files whole for it, so recording this would red the
bar on a record no verb rewrites."* Verified: `check-unattended.sh:603` is the ONLY whole-file
`grep -qF -- "$BYPASS_BAN"` in the leg, and its `$f` comes from `RUNS` (`:186`), which is
`^memory/builds/[^/]+/RUN(\.[A-Z]+\.[0-9a-f]{8})?\.md$` — **run-state files only**. No leg anywhere
greps a piece or set record for the flag. The guard is defensible; its stated reason sends a reader to
a gate that does not exist, and the same false justification sits on the piece writer.

The field-coverage half of this finding is filed under HIGH 1, where it is reachable and reproduced.

**Fix.** Either widen check 11's population to the declared records roots so the sentence becomes true —
the better repair, since a bypass flag in a tracked evidence record is exactly as bad as one in a
run-state file — or drop the gate-grep clause from both messages and state the real reason.

**Left-shift gate.** If the population is widened: an arm writing the flag into a piece record and
asserting check 11 reds. If the message is corrected instead, the existing `check-arms.py` join already
covers the refusal; add a leg check asserting no refusal message names a gate behaviour absent from the
leg — the general form of "a gate's own header states what it does not check".

---

## LOW 2 — spec 9's revision log still names the checks it added by their pre-merge numbers, and the same commit flipped it to CLOSED

**`memory/builds/dScriptedRepeat/spec/2026-08-20-spec-dScriptedRepeat-9.md:143`** *(round-1 id 13)*

rev-6 reads *"Two new leg checks, 22 and 23, each staged RED before landing."* Those are now 26 and 27.
`git show 5b0d73c0 -- <that spec>` shows the ONLY change to the file was `INPROGRESS` → `CLOSED`, with
no superseding note. A reader auditing this build's own evidence against `check-unattended.sh` lands on
two unrelated checks — in the record that certifies the work.

A repo-wide grep confirms this and the dossier are the only two LIVE stale references; every other hit
is a frozen record correct for its era, or another script's own checks 22/23.

**Fix.** Append a revision-log line (do not rewrite rev-6) recording the renumber to 26 and 27 at the
merge collision, cross-referencing the acceptance-ledger entry.

**Left-shift gate.** Fold into MEDIUM 3's gate: extend the reference resolver to `memory/builds/**` for
non-frozen specs, or accept that frozen records cite their era and gate only `memory/map/` and open
specs.

---

## The project's own recurring-bug-class checklist, worked through

`python tools/memory-tree/gotchas.py --for-diff 60c40b62..a564ce2b` selected 7 anchored classes plus 3
universal. Each is answered against this diff.

| class | verdict |
|---|---|
| `fixture-passes-by-finding-nothing` | **HIT, twice.** All three playbook fixtures spell both declaration keys with no trailing comment (Blocker 1), and none narrows a working-tree field against a pinned one (Blocker 2). 42 new assertions and a 656-assertion suite pass over the one spelling that cannot fail. |
| `two-answers-to-one-question` | **HIT.** Three parsers for one field shape (Blocker 1, MEDIUM 2). Two stale check-number pointers (MEDIUM 3, LOW 2). One README sentence true of two fields out of three (Blocker 2). |
| `inputs-inside-the-subjects-reach` | **HIT, twice.** `pchk` off the working tree (Blocker 2); `grain`/`records` reverting to it on an empty fact (HIGH 2). |
| `heredoc-escape-reaches-the-regex` | **HIT, as its sibling.** A two-character `\n` reaching a sed REPLACEMENT rather than a heredoc — same mechanism, same invisibility (HIGH 1). |
| `assertion-between-two-derived-values` | Clear. `dod_met`'s L1 compare derives `_live` from the records and `_rec` from the set record — two acts at two times, not one derivation twice. |
| `second-implementation-is-not-a-second-opinion` | Clear, and deliberately so: `dod_met` CALLS `check-playbook.sh --counts` rather than re-deriving. That decision is what makes Blocker 2 a single-point fix. |
| `status-set-in-a-subshell` | Clear. Every new `fail`/`note` is in the parent shell; `st` is set outside every pipeline. |
| `containment-tested-one-way` | Clear — no new path-containment predicate in the diff. |
| `id-matched-as-a-substring` | Clear. Both new joins use `grep -qxF --`, whole-line and fixed-string. |
| `fixture-inherits-ambient-machine-state` | Clear. `check-playbook.test.sh` seeds a `mktemp -d` repo with `core.autocrlf false`; the driver suite resets its tree per block. |

## Landing order

1. **Blocker 1** — the `declared_list()` helper, all three call sites, plus the template-comment arm.
2. **Blocker 2** — read `$body` from the BASE blob in `--counts` mode; correct README:175.
3. **HIGH 1** — the `set:` and `hash:` re-stamps stop using `sed`; every caller-supplied field guarded
   in both writers.
4. **HIGH 2** — the `AUTH_RECORDS` refusal and the `_gr`/`_rrf` emptiness block (largely subsumed by 2).
5. **MEDIUM 1** — stage on the re-stamp path in both writers.
6. **MEDIUM 2** — folded into 1.
7. **MEDIUM 3, LOW 1, LOW 2** — prose and message corrections, plus the reference-resolver gate.

Items 1 and 2 are re-fixes of round-1 findings, and the kit is copy-installed into other repos, so
neither may land as a follow-up.

## Method and limits

Scope was the fix diff, not the build. Every finding above was re-derived from the tree at
`a564ce2b98f4c8ea645b5f885ab9f26d535b9e19`, not accepted from round 1. Nine were reproduced by staged
break-and-revert on the live tree or in a throwaway repo; the tree was verified clean
(`git status --porcelain` empty) after every mutation and at the end of the pass.

**Observed green:** `bash tools/unattended/check-playbook.test.sh` → PASS (56 assertions);
`bash tools/unattended/unattended.test.sh` → PASS (656 assertions, floor 636);
`bash tools/unattended/check-unattended.sh` → rc 0; `python tools/memory-tree/check-arms.py --check` →
rc 0. **Staged break:** the current `check-playbook.test.sh` run against `check-playbook.sh@60c40b62`
fails 12 arms, which is how the "no new arm passes for the wrong reason" claim above was established.

**Not verified, stated plainly:** the full merge bar was not run, and neither was
`check-unattended.test.sh` (295 assertions). Blocker 1's impact chain past the enumerator (term 2b →
`DOD_NO_OVERRIDE` → `fail 21`) is code-verified at named line numbers rather than executed end to end
through `--close`; the enumerator input that drives it was measured directly.

**A landing consequence of this record, not a finding against the diff.** Registering it regenerates
`memory/builds/dScriptedRepeat/README.md` (two additive rows, `python tools/memory-tree/gen_build_index.py --write`,
run and staged). That README was 25,419 B at `a564ce2b` — 181 B under the memory-hygiene 25,600 B index
cap — and the two rows push it to 25,829 B, so **HYGIENE check 6 reds until the README is trimmed.**
That is the only red on the hygiene gate with this record staged. Trimming it is the build owner's
call, not a reviewer's: the fold narrative in that README is the obvious place, and the cap was 99.3%
consumed before this record existed.
