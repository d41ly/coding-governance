**Serves:** diff-review TOOL-dScriptedRepeat-5 TOOL-dScriptedRepeat-6 TOOL-dScriptedRepeat-7 TOOL-dScriptedRepeat-9 TOOL-dScriptedRepeat-10 TOOL-dScriptedRepeat-11

# dScriptedRepeat — diff review, round 1

**Range:** `d163804cbf399cbc0c145b4a547c68ca8c31ea8f...60c40b62021384b49cf6aa361fa47c58da680ecb` —
the cumulative diff landing on `main`. 34 files, 1928 insertions, 115 deletions. **ROUND 1.**

**Review shape:** raw 35 · confirmed 32 · refuted 3 · unverified 0 · precision 0.91. The 32 confirmed
findings collapse to **16 distinct defects** — six clusters were found independently by three or four
lenses each, and that corroboration is recorded per finding rather than inflating the count.

## Verdict: BLOCKED

Two blockers, five highs. Both blockers are the same shape and it is this repo's own named #1 failure
mode: **a check satisfied by its own comment prose.** The mode's flagship Definition-of-Done item,
`pieces-complete`, certifies that a recipe run "made what was asked, with its declared checks green".
It does not. It certifies that a file exists at a path whose hash matches, and it will pass over
pieces that nothing ever checked. Three documents assert the join that the code does not perform, and
one of them — `memory/guides/UNATTENDED-PROTOCOL.md` — is the binding contract the charter points at.

The second blocker is positional rather than semantic: the entire per-piece record reader was added
one line below the `done` that closes the playbook loop, so it grades the LAST playbook and no other.
It is invisible today because this repo's playbook population is exactly 1, and every arm of the
kit's own self-test mutates that single fixture. Unit 11 ships the playbook CREATION path, which
makes a second playbook the expected next state.

**The merge itself is clean.** See "The merge" below — that was the highest-risk part going in, and it
is the one part that came back green.

## The merge — the seven hand-resolved files

`main` advanced ten commits mid-build (`lib-unattended.sh`, `--rescope`/`--dispatch`, both self-test
suites sharded, memory-hygiene check 22). The reconcile is `9a962cb8`, parents `acbd9dc5` (branch) and
`d163804c` (main). Seven files were resolved by hand. I hunted specifically for the half-applied merge
shapes — a function body swallowed by a neighbour's brace, a dropped arm, a double-applied hunk,
main's behaviour silently reverted, a name that now means two things — and found **one**, M3 below.

Evidence that the other six shapes are absent:

- `bash -n` is clean on all ten shell files in the kit.
- No duplicate function definition anywhere in `unattended.sh`
  (`grep -hoE '^[a-z_][a-z0-9_]*\(\)' | sort | uniq -d` is empty), so no hunk was double-applied and
  no body was swallowed.
- `python tools/memory-tree/check-arms.py --check` exits 0 — every `fail` branch in every gate is
  armed by a positive assertion in its sibling suite. Worth stating plainly, because it is ALSO the
  measure of what the meta-gate cannot see: B1 and B2 are both armed and both still wrong. B1's arm
  asserts a predicate that does not mean what the document says; B2's arm runs at a population of one,
  where the positional bug cannot manifest.
- `bash tools/unattended/check-playbook.test.sh` — PASS, 43 assertions.

The one merge artifact is M3: the branch forked before `main` added checks 22 and 23 to
`check-unattended.sh`, and the two new checks reused those numbers. That is the "a name that now means
two things" shape, caught.

---

## BLOCKER 1 — `verified` never joins `piece_checks`, so `pieces-complete` certifies unchecked pieces

**`tools/unattended/check-playbook.sh:229`** · unit 5, consumed by units 6/7
*(corroborated independently by three lenses)*

`verified` is computed as: a record exists, its `hash:` joins the piece, and no line matches
`^leg .* · verdict FAIL$`. The playbook's declared `piece_checks` is never read. `grep -rn piece_checks
tools/` returns exactly two hits — `PLAYBOOK-TEMPLATE.template.md:55` and `playbook.fixture.md:14`.
**The declaration has no reader anywhere in the kit.**

So `verified` means "the hash matches and nobody wrote the word FAIL". A piece record carrying ZERO
verdict rows is verified. A record whose only row names a leg the playbook never declared is verified.

**Reproduced in this pass**, hermetic clone of the kit:

```
baseline                                   -> pieces=2 verified=2 failed=0 stale=0 unrecorded=0
delete every '^leg ... · verdict' row      -> pieces=2 verified=2 failed=0 stale=0 unrecorded=0
                                              (grep -c '^leg ' on both records returns 0)
playbook declares piece_checks = ["fixture-shape"]
```

**Three carriers assert the join that does not exist**, and they are the reason the green looks
meaningful:

- `tools/unattended/unattended.sh:2044-2046` — "`verified` requires the hash join AND every declared
  leg recording PASS, which is what makes 'its declared legs green' implemented rather than merely
  cited."
- `tools/unattended/check-playbook.sh:225-227` — "the verdicts answer the second, and `verified`
  requires BOTH".
- `tools/unattended/PROTOCOL.template.md:270` and the installed
  `memory/guides/UNATTENDED-PROTOCOL.md:270` — "each recording a PASS for every declared per-piece
  leg."

`pieces-complete` keys term 3 on `_vc` (`unattended.sh:2049`). A recipe run that ran no per-piece check
at all closes green, and the unattended landing rule leans on that close.

**Fix.** Parse `piece_checks` out of the playbook blob into a list. In the census, require per piece a
`leg <declared> · verdict PASS` row for every declared name before counting it `verified`; anything
short of that becomes a sixth state (`unchecked`) that `pieces-complete` blocks on. `NA` counts only
with an explicit reason row. **If the join is deferred, delete the three sentences above in the same
commit** — a documented guarantee the code does not provide is worse than an absent one, because the
reader stops looking for the gate.

**Left-shift gate.** An arm in `check-playbook.test.sh` that declares `piece_checks = ["x"]`, writes a
record whose only verdict row is `leg y · verdict PASS`, and asserts the census does NOT report it
verified. Stage it, confirm RED against today's code, then fix. Second arm: a corpus check that every
key the PLAYBOOK-TEMPLATE tells an author to declare has at least one reader in `tools/` — that class
of dead declaration is what produced both blockers-by-documentation here.

---

## BLOCKER 2 — check 8 sits outside the playbook loop, so it grades only the LAST playbook

**`tools/unattended/check-playbook.sh:190`** (block spans 190-252; the loop opens at 101 and its `done`
is at 188) · unit 5 *(corroborated independently by four lenses)*

The whole per-piece record reader — the census, the five states, the orphan-record sweep, and the
`fail 8` refusal for "declares a grain and no records root" — is indented two spaces as if it were
loop body, and is not. It runs once, over the `$pb` and `$body` left over from the final iteration.

**Reproduced in this pass**, and the proof is positional rather than circumstantial. The SAME violating
playbook (a copy of the fixture with its `records` line stripped, which must fire `fail 8`) was run in
two positions:

```
population order: aaa/aaa-playbook.md, tools/unattended/playbook.fixture.md   (violator FIRST)
  -> one 'pieces ...' line, naming tools/unattended/playbook.fixture.md
  -> fail 8 never fires
  -> exit 0

population order: tools/unattended/playbook.fixture.md, zzz/zzz-playbook.md   (violator LAST)
  -> PLAYBOOK check 8 FAILED - a playbook declares a piece grain and no records root ...
  -> exit 1
```

Identical content, opposite verdict, decided by `git ls-files` order. `steps 6` in both runs proves
checks 2-7 walked both playbooks; only check 8 did not.

For every non-last playbook there is no hash join, no `stale` detection, no `failed` count, no
`unrecorded` count, no orphan-record direction, and `fail 8` is structurally unreachable. This is the
leg carrying the whole of this mode's enforcement.

**Why it is latent here and live for adopters.** This repo's tracked population is 1 — the leg's own
header line says `population 1 playbook(s)`. The kit SHIPS `tools/unattended/playbook.fixture.md`, and
`git ls-files` is sorted, so an adopter's real playbook under `content/`, `docs/` or `memory/` sorts
BEFORE the fixture and loses. Every adopter gets a confident green over the one playbook nobody cares
about. Unit 11 ships the creation path, so a second playbook is the expected next state, not a
hypothetical.

**Fix.** Move the `done` from line 188 to after check 8's closing `fi` at line 252. Check 9's
`TOTAL_*` aggregate prints stay outside.

**Left-shift gate.** `check-playbook.test.sh` currently mutates one fixture, so the whole suite runs at
population 1 and structurally cannot see this. Add an arm that seeds a SECOND tracked playbook — grain
declared, `records` stripped, sorting FIRST — and asserts the leg reds. That arm is RED against today's
code, which is the only evidence that makes the fix worth landing (§7: a gate whose failing case has
not been observed is an assertion about nothing).

---

## HIGH 1 — `set-checks-recorded` never joins `set_checks` and never requires PASS

**`tools/unattended/unattended.sh:2058-2067`** · unit 7 *(corroborated by three lenses)*

`_declared` is captured raw from the BASE blob and used for exactly one thing: deciding whether the
item applies at all (`case "$_declared" in ''|'[]'|'none'*)`). It is never split into names, and no
name is ever compared against the record. The entire remaining evidence is `[ -f "$_set" ]` plus
`! grep -q '^leg .* · verdict FAIL$'`.

A playbook declaring `set_checks = ["a","b","c"]` is fully satisfied by one
`--record-set <slug> --leg z --verdict NA` naming a leg the playbook never declared. An empty
`## Verdicts` section satisfies it too.

`PROTOCOL.template.md:271` claims the opposite twice in one row: "every set-scoped check the playbook
declares recorded a PASS for THIS run's set" and "It reads the VERDICT and not merely its existence —
unlike the prose review `closing-review-recorded` can only assert the existence of." **It is exactly
the existence check it disclaims.** "For THIS run's set" is unenforced as well: `record_set` re-stamps
the `set:` member list on every write (2472) and `dod_met` never reads that line.

The set-scoped population is the one a per-piece review structurally cannot see. That is this item's
entire reason to exist.

**Fix.** Split `_declared` into names; require a `^leg <name> · verdict PASS$` row per declared name;
report the missing names in `DOD_OUT`, with "declared but not recorded" and "recorded but not PASS" as
two distinct messages. Additionally compare the record's `set:` line against the hash list
`verb_record_set` derives, so the verdict is bound to the members it claims to cover. If deferred,
reword `PROTOCOL.template.md:271` AND the installed `memory/guides/UNATTENDED-PROTOCOL.md:271` in the
same commit so check 10's byte parity stays green.

**Left-shift gate.** A `unattended.test.sh` arm: playbook declares `set_checks = ["a","b"]`, run records
`--leg a --verdict PASS` only, assert `set-checks-recorded` is UNMET and names `b`. Plus the same
corpus check proposed under B1 — every template-declared key needs a reader.

---

## HIGH 2 — a caller-supplied leg name is interpolated into a `sed` ADDRESS in both record writers

**`tools/unattended/unattended.sh:2450`** (`record_piece`) and **`:2480`** (`record_set`) · units 5, 7
*(corroborated by three lenses)*

```sh
sed -i "/^leg $leg · verdict /d" "$rec"
```

The three field guards above it (2411 newline, 2414 the ` · ` separator, 2416 the bypass flag) reach
none of this: `$leg` reaches a regex address unescaped, and the rewrite's exit status is never checked
before the append on the next line.

**Both arms reproduced in this pass** against the shipped driver:

```
--record-piece ... --leg lint  --verdict FAIL      -> record holds: leg lint · verdict FAIL
--record-piece ... --leg '.*'  --verdict PASS      -> record holds: leg .* · verdict PASS
                                                      (the FAIL row is GONE; driver exits 0)

--record-piece ... --leg 'tools/lint.sh' --verdict FAIL
--record-piece ... --leg 'tools/lint.sh' --verdict PASS
  stderr: sed: -e expression #1, char 14: extra characters after command
  exit 0, "unattended: piece verdict recorded"
  record holds BOTH: leg tools/lint.sh · verdict FAIL
                     leg tools/lint.sh · verdict PASS
```

Two consequences, in opposite directions:

- **A metacharacter erases evidence.** `.*` mass-deletes every recorded verdict. The erased FAIL then
  makes `check-playbook.sh:229` read the piece as `verified`, and `pieces-complete` passes.
- **A slash wedges the run permanently.** Slash-bearing leg names are ordinary under this kit's own
  tag grammar (`check-playbook.sh:153`, `GATE [A-Za-z0-9_.:/-]+`), and the fixture playbook's registry
  maps legs to `tools/unattended/check-playbook.sh`. The record ends in the two-verdicts-for-one-leg
  state the comment at 2448-2449 says this line prevents; the reader still sees the stale FAIL, so the
  piece is `failed` forever, `pieces-complete` can never be met, and no verb repairs it. In an
  unattended run there is no owner to diagnose it.

**Fix.** Stop building a regex from caller input. Filter literally — `grep -vF -- "leg $leg · verdict "`
into a temp file guarded by a prefix test, or `awk -v L="$leg"` — and check the rewrite's exit status
before appending. Add `/` and regex metacharacters to the field guards, or declare a closed character
class for `--leg`.

**Left-shift gate.** Three `unattended.test.sh` arms, on BOTH writers: a leg containing `.`, one
containing `*`, one containing `/`. Each asserts the pre-existing unrelated row survives and that
exactly one verdict row exists for the named leg afterwards.

---

## HIGH 3 — `record_set` carries none of the field guards its four sibling writers carry

**`tools/unattended/unattended.sh:2456-2485`** · unit 7 *(corroborated by two lenses)*

Four record writers in this driver carry the newline / separator / bypass-flag trio — `record_park`
(2297), the proposal writer (2355), `record_piece` (2411), the rescope writer (2579). `record_set`
validates the verdict enum and nothing else. It is the one exception, and the guards were not
forgotten in the abstract: `record_piece`'s own comment at 2408-2410 says each exists because of a
recorded defect.

**Reproduced in this pass:**

```
--record-set - --records-root recs --run R1 \
  --leg $'fixture-distinct · verdict PASS\n#hidden' --verdict FAIL
  -> exit 0, "unattended: set verdict recorded"
  -> record holds:  leg fixture-distinct · verdict PASS
                    #hidden · verdict FAIL
  -> grep -q '^leg .* · verdict FAIL$' finds NO match
```

The second line does not start with `leg `, so `set-checks-recorded` (2063) does not see it. **A run
that recorded a FAILING set check closes with the item MET**, and a PASS row nothing ran was forged in
the same write. `record_piece` refuses the identical input at 2411. The guards are missing on the slug
path too, not only under `--records-root`.

`$hashes` is likewise unescaped into `sed -i "s|^set: .*|set: $hashes|"` at 2472, so a `--set` value
containing `|` breaks that rewrite unchecked while the verb reports success.

**Fix.** Hoist the trio into a shared `check_record_fields` helper — four call sites already want it —
and call it from `record_set` over `$leg` and `$hashes` before any write. Check the `sed -i` exit
status at 2472.

**Left-shift gate.** Mirror `record_piece`'s refusal arms onto `record_set`. The suite currently arms
eight refusals on one writer and three on its twin; that asymmetry is what made this invisible. A
cheap structural check is better: assert that every function matching `^record_` or `^verb_.*park`
contains the `wc -l` newline guard.

---

## HIGH 4 — `pieces-complete` measures the WORKING-TREE playbook while its sibling arm reads BASE

**`tools/unattended/unattended.sh:2029`** vs **`:2056`** · units 6, 7 *(corroborated by two lenses)*

Line 2029 hands `check-playbook.sh --counts` the playbook PATH, and that script reads
`body=$(tr -d '\r' < "$pb")` at line 103 — the working tree. Twenty-seven lines later, in the same
`dod_met` arm, `set-checks-recorded` reads the playbook from the BASE blob
(`GIT show "$(fact "$rel" base):$_pb"`). Two halves of one arm, two different files.

**Reproduced in this pass:**

```
committed grain:  "tools/unattended/fixture-pieces/*/piece.md"
--counts ...   -> pieces=2 verified=2

UNCOMMITTED one-line worktree edit narrowing grain to ".../one/piece.md"
git show HEAD:<playbook> still declares the wide glob
--counts ...   -> pieces=1 verified=1
```

The run is the actor that can make that edit, and nothing refuses it — "a piece-producing run may not
edit its own playbook" is prose only (`SKILL.template.md:328`). So the population that
`pieces-complete` counts, and term 3's `verified == pieces` equality, are defined by a file inside the
subject's reach. That is this project's own `inputs-inside-the-subjects-reach` class, named in the
checklist this diff selected.

The BASE-pinned `grain` fact exists and is dead: `unattended.sh:1730` writes it, and repo-wide grep
finds no reader. Preflight refusal 46 goes to the trouble of reading the grain from the blob at BASE
precisely so the run cannot supply it — then the close throws that away and asks the working tree.

It breaks in the honest direction too: a legitimately amended `records` root makes the two halves of
one arm read two different directories.

**Note on §9.** The protocol's shell-access admission does not cover this one. The inconsistency is
between two lines of the same arm, and the BASE read four lines down shows which one was intended.

**Fix.** Give `--counts` the blob (or an `--at <sha>` argument) and resolve `grain`/`records` via
`GIT show "$(fact "$rel" base):$_pb"`, the source line 2056 already uses. Simpler alternative: pass the
recorded `grain` and `records` FACTS into `--counts` and stop re-parsing the file — which also gives
the dead fact at 1730 a reader.

**Left-shift gate.** A `check-unattended.sh` arm asserting the working-tree playbook is byte-identical
to its BASE blob for any run whose recorded mode is `recipe` — the refusal the prose currently asks for
and nothing enforces. Plus a `unattended.test.sh` arm: edit the grain in the worktree, assert
`pieces-complete`'s population is unchanged.

---

## HIGH 5 — `head -1` parses across a text boundary, and a legal coverage mode wedges the close

**`tools/unattended/unattended.sh:2029`** · **`tools/unattended/check-playbook.sh:172`** · unit 6
*(corroborated by three lenses)*

`dod_met` takes `head -1` of `--counts` and assumes line 1 is the machine `pieces=` line. `--counts`
suppresses the population line (78) and check 9's notes (255-256), but `check-playbook.sh:172` — the
`coverage = probe` admission — is the one `note` in the file NOT guarded by `[ -n "$COUNTS_FOR" ] ||`,
and `fail()` (line 27) is unguarded too. Both print to stdout ahead of the machine line.

**Reproduced in this pass**, on a playbook whose only change is a legal, documented coverage mode:

```
--counts <pb> <run> :
  line 1: playbook: coverage probe on ... - existence only; whether a declared target TESTS ...
  line 2: pieces=2 verified=2 failed=0 stale=0 unrecorded=0

head -1 captures line 1. Then:
  _pc = "playbook:"   _sc = "playbook:"
  [ "playbook:" -eq 0 ]  ->  "[: playbook:: integer expected", status 2, reads FALSE
  the VACUITY GUARD silently does not fire
  the STALE term fires:  "a piece this run produced is STALE ... : playbook: stale"
```

`pieces-complete` reds on a perfectly healthy run, with a message describing a state that does not
exist. A `probe`-coverage playbook can NEVER satisfy it. The same corruption happens whenever the named
playbook fails any of checks 2-7. It fails closed, but an unattended run is then wedged on a
Definition-of-Done item whose stated reason is fiction, with nobody to read it, and the only exit is
spending the `--close` override budget on a lie.

Latent here only because the repo's own fixture declares `resolvable`.

**Fix.** Two independent halves, both cheap, and take both. (a) Guard `check-playbook.sh:172` with
`[ -n "$COUNTS_FOR" ] ||` like every other note, and send `fail()` to stderr while `--counts` is
active. (b) Select the line by shape rather than by position at 2029: `| grep -m1 '^pieces='`, and red
with a named `DOD_OUT` refusal when that grep yields nothing, rather than parsing whatever arrived.

**Left-shift gate.** An arm that fires `--counts` against a playbook whose leg reds, and asserts the
machine line is still the one read. A second arm for each of the three legal coverage modes.

---

## MEDIUM 1 — the "no set checks declared" escape is defeated by the exact line the kit ships

**`tools/unattended/unattended.sh:2058-2060`** · **`tools/unattended/PLAYBOOK-TEMPLATE.template.md:56`**

The escape matches `''|'[]'|'none'*` against raw, untrimmed text. The shipped template line is:

```
set_checks   = []    # the checks that run over ALL N. See section 8; this is the one
```

**Verified in this pass**: the extraction yields `[]    # the checks that run over ALL N. See section
8; this is the one`, and the `case` prints NO MATCH. An author with no set-scoped checks who keeps the
template's own comment gets "the playbook declares set-scoped checks and this run recorded no set
verdict". `'[] '` and `'[]\r'` fail identically. The sibling `_rr` extraction two lines above (2056)
uses awk with `gsub(/^[[:space:]"]+|[[:space:]"]+$/,"",v)` and DOES strip — the inconsistency is
internal.

Not strictly unmeetable (the run could record a bogus set verdict, or spend an override), but on an
unattended run there is nobody to make that call.

**Fix.** Strip a trailing `#` comment, surrounding whitespace and CR before the `case`, mirroring 2056.

**Left-shift gate.** An arm that runs the extraction over the SHIPPED template line verbatim and
asserts the escape matches — a template/code pair that must not drift is exactly the
`two-answers-to-one-question` class.

---

## MEDIUM 2 — `set-checks-recorded` cannot tell "declares nothing" from "the blob is unreadable"

**`tools/unattended/unattended.sh:2056-2060`**

`_rr` and `_declared` both come from `GIT show ... 2>/dev/null`. A wrong path, a wrong base, or a
swallowed failure all yield the empty string, and the very next `case` treats that as a declared null
and returns MET. No liveness assertion. The sibling arm has one — `[ "${_pc:-0}" -eq 0 ]` fails
explicitly on the same broken read — so the asymmetry is internal and the coverage is accidental:
spend `--override pieces-complete` and this item certifies set coverage over a playbook nothing could
read.

Second half: with `set_checks` declared and `records` absent, `_rr` is empty and `_set` degenerates to
the absolute path `/set-<slug>.md`, so the item reds naming a path outside the repo.

This is the charter's own "a probe that cannot move says so" rule — implemented one arm over, absent
here.

**Fix.** Capture the blob once into a variable; red with a named refusal if `GIT show` fails or the
blob carries no declaration block; only then treat an empty `set_checks` as a declared null. Guard
`_rr` non-empty before composing `_set`. Arm both branches.

**Left-shift gate.** An arm that points a run's `playbook` fact at a path absent from BASE and asserts
`set-checks-recorded` is UNMET with a DEAD-PROBE-shaped message.

---

## MEDIUM 3 — check numbers 22 and 23 each name two unrelated checks *(the merge artifact)*

**`tools/unattended/check-unattended.sh:1284`** and **`:1313`** · unit 10

The branch forked at `381345dd`, before `main` landed check 22 (the rescope-amendment record, fail
sites 1062/1068/1076) and check 23 (the dispatch write-set, `TOOL-dUnstalledConvoy-10`, fail sites
1179/1200/1216). The hand reconcile kept both and added `# ---- 22: THE VERB SET` (fail sites
1299/1303/1305/1308) and `# ---- 23: every park() CALL SITE` (fail sites 1328/1332/1340/1347).

Seven `fail 22` sites and seven `fail 23` sites now emit under two identifiers, split across four
unrelated checks. `UNATTENDED check 23 FAILED` means either "a pass wrote outside its declared set" or
"a park kind nobody declares", and an operator reading a red bar cannot tell which spoke.

The concrete cost is in the suite. `check-unattended.test.sh` carries 4 `miss ... "check 22 FAILED"`
arms (1463/1471/1490/1498) and 9 `miss ... "check 23 FAILED"` arms (1516-1696) — **13 negative
substring assertions that now silently span two checks each.** An arm written to isolate the dispatch
check is grading the park-kind check too, and a future failure of the new check inside those fixtures
will red an arm whose message blames the old one.

**Fix.** Renumber the two new blocks to 26 and 27 (24 and 25 are taken by the mode-set and
content-scope checks this build also added) — headers, every `fail N` call, and the matching `hit`/`miss`
arms.

**Left-shift gate.** A one-line self-check in `check-unattended.test.sh` asserting
`grep -oE 'fail [0-9]+' check-unattended.sh | sort -n | uniq -d` is empty, keyed to the `# ---- N:`
headers. The number is the check's only identifier and nothing currently guards its uniqueness — which
is why a ten-commit merge could collide two of them silently.

---

## MEDIUM 4 — three documents say the playbook leg reads the set record; it never opens one

**`tools/unattended/SKILL.template.md:344`** · **`.claude/skills/unattended/SKILL.md:344`** ·
**`memory/map/features/playbook-mode.md:97`** · unit 10

The attended-path paragraph reads: "The per-piece records and the set record are tracked files,
hash-joined to the pieces, and the playbook leg reads them without knowing who wrote them or how", and
concludes "the attended path is gated on what it produced". The dossier repeats it: the records are
"the only surface the merge bar grades it on".

**Verified in this pass:** `grep -n "set-" tools/unattended/check-playbook.sh` returns nothing. The leg
never opens a set record. `record_for` (90-97) and the orphan loop (246-251) both key on a `piece:`
line, which a set record does not carry, so both `continue`. `set_checks` and `set-<run>.md` are read
in exactly one place in the whole tree — `dod_met` at `unattended.sh:2056-2064`, which runs only inside
the unattended `--close`.

So on the attended path the set-scoped verdicts — the population the Skill itself says a per-piece
review structurally cannot see — are graded by absolutely nothing. The sentence is true of the
per-piece half and false of the half that matters most, and the reader stops looking for the gate.

**Fix.** Either add a set-record reader to check 8 (declared `set_checks` present implies a set record
exists for each run id seen in the piece records, and holds no `verdict FAIL`), or rewrite the sentence
to name the honest split: the leg reads the PER-PIECE records; the set record is read only by
`--close`, so on the attended path it is evidence for a human and not a gate. Fix all three carriers in
one commit.

**Left-shift gate.** This is the `two-answers-to-one-question` class and it needs a joiner, not a
proofread: extend the leg check that already joins `AUTH_MODES` to the routing table so it also joins
each artifact the Skill claims the leg reads against the set of paths `check-playbook.sh` actually
opens.

---

## MEDIUM 5 — the binding contract calls `--record-piece` unattended-only; the Skill hands it to attended agents

**`tools/unattended/PROTOCOL.template.md:360`** · **`memory/guides/UNATTENDED-PROTOCOL.md:360`** ·
**`tools/unattended/SKILL.template.md:352`** · unit 5

The protocol says: "The writer takes a records ROOT rather than a slug, so the attended path reaches
the same function; the VERB requires a run-state file and is therefore unattended-only." The clause
contradicts its own first half, and both halves of the sentence contradict the code.

**Verified in this pass:** `verb_record_piece` (2509) returns through the `[ -n "${RP_ROOT:-}" ]` branch
at 2521-2524, BEFORE `check_slug` (2525) and before the run-state existence test (2527). So
`--record-piece - --records-root <root> ...` works with no run at all — which is precisely the
invocation `SKILL.template.md:352` hands attended agents, and which `unattended.test.sh:2554-2570`
exercises and asserts WRITES.

AGENTS.md makes `memory/guides/UNATTENDED-PROTOCOL.md` THE binding contract, so the contract and the
Skill now give two answers to one question. Check 22 joins verb NAMES only — it cannot see a
description going false.

**Fix.** Replace the trailing clause with what is true: the verb requires a run-state file only in its
SLUG form; passing `--records-root` reaches the writer with no run, which is the attended path. Fix the
template and the installed copy in the same commit so check 10's byte parity stays green.

**Left-shift gate.** Extend check 22 from a name join to a shape join for the two verbs the attended
path uses: assert the protocol's description of each verb names the same required arguments the
driver's own header docstring declares.

---

## MEDIUM 6 — `playbook-sha` is filled with a PATH, or with nothing, and no reader exists

**`tools/unattended/unattended.sh:2531`** (unattended) and **`:2522`** (attended) · unit 5

Line 2531 passes `$(fact "$rel" playbook)` as `record_piece`'s fifth positional, whose local is `pbsha`
(2402) and which is printed under the label `playbook-sha:` (2432). The same expression is used two
lines earlier as the PATH half of `GIT show "$(fact "$rel" base):$(fact "$rel" playbook)"`, so it is
unambiguously a path. The attended invocation documented at `SKILL.template.md:352` omits
`--playbook-sha`, so `${RP_PBSHA:-}` expands empty.

**Three producers write three different things into one field**, and the third is the only correct one:
both committed fixture records carry `playbook-sha: 0c88a36e7b9b28da4e3c0774d6fb39be8c29542d`, which
**verified in this pass** equals `git hash-object tools/unattended/playbook.fixture.md`.

Repo-wide grep for `playbook-sha` finds the writer, the arg-parse arm (2852), and the two fixtures.
**No reader in `tools/`, no mention in either document, and zero assertions in any `*.test.sh`.** The
field is unfalsifiable today, and its only committed evidence agrees with neither live writer. The
instant anyone wires the provenance join it was created for, every unattended-written record fails it.

**Fix.** Pass `GIT rev-parse "$(fact "$rel" base):$(fact "$rel" playbook)"` on the unattended path;
default the attended path to the same derivation from the records root's playbook. Or delete the
field — dead plumbing carrying wrong data is worse than no plumbing.

**Left-shift gate.** One arm asserting the recorded value is a 40-hex sha matching `git hash-object` of
the playbook. Note the broader gap it closes: the unattended SUCCESS path of both record verbs has no
self-test arm at all, which is why this went unseen.

---

## MEDIUM 7 — the `unrecorded` term of `pieces-complete` can never fire

**`tools/unattended/unattended.sh:2043`** · **`tools/unattended/check-playbook.sh:214`** · unit 6

`check-playbook.sh:214` does `[ -n "$COUNTS_RUN" ] && continue` on a piece with no record, on line 214,
BEFORE `un=$((un + 1))` on line 215. `dod_met` (2029) is the only non-test caller of `--counts` and it
always passes `"$slug"`, which `check_slug` has already forced non-empty. So `_uc` is structurally
always 0 and the term at 2043 is an arm nothing can reach.

Reproduced: three pieces under the grain with records for two returned `pieces=3 ... unrecorded=1`
unscoped and `pieces=2 verified=2 ... unrecorded=0` run-scoped.

The enumerator's exclusion is deliberate and documented — a piece belonging to no run should not make a
run answerable for it. That rationale does not extend to the consumer keeping a term it can never
reach, whose message ("a piece this run produced carries no record, so nothing says whether its
declared checks ran at all") reads as enforcement. Impact is bounded: term 3's count comparison catches
the condition under a different message.

**Fix.** Either delete the term and say in the item's comment that unrecorded pieces are out of run
scope by construction, or give `--counts` a separate `unattributed=` field so the DoD can distinguish
"somebody else's piece" from "a piece this run forgot to record". Do not leave a branch no fixture can
fire.

**Left-shift gate.** `check-arms.py` already proves every `fail` branch in every GATE is armed. This is
the same class one layer over, in `dod_met`'s terms, and it is currently unmeasured — extend the
meta-gate to `DOD_OUT` assignments, or add an arm per term asserting each is reachable.

---

## LOW 1 — the `set:` member list has no reader, so the `superseded` state it names has no detector

**`tools/unattended/unattended.sh:2467-2472`** · unit 7

**Verified in this pass:** the only occurrences of `^set: ` in the tree are the writer (2469) and its
own re-stamp `sed` (2472). No check, leg or DoD item reads the line, and `superseded` appears nowhere
outside the comment at 2471.

The re-stamp fires only when `record_set` is called AGAIN — which is the one case where nothing is
stale. The reachable stale path: record a set PASS, then re-record a piece (which re-stamps that
piece's `hash:` at 2438), and the set verdict now points at a member list describing a different set.
`set-checks-recorded` only greps for `verdict FAIL`, so it passes. A comment asserting a guarantee the
code does not implement, in a kit whose stated failure mode is exactly that.

**Fix.** Make `set-checks-recorded` compare the recorded `set:` list against a live re-derivation of
this run's piece hashes and red with a `superseded` message, or delete the field and the comment naming
the state.

**Left-shift gate.** Fold into HIGH 1's arm — once the name join exists, the member-list comparison is
three more lines in the same place.

---

## LOW 2 — the attended `--record-set` example omits `--run`, contradicting its own next paragraph

**`tools/unattended/SKILL.template.md:353`** · unit 10

Line 352 passes `--run <label>`; line 353 does not. Lines 357-359 immediately below tell the reader
`--run` is what "labels the batch so a later reader can tell one sitting's pieces from another's".

**Reproduced in this pass:** running line 353 verbatim writes `<root>/set--.md` containing `run: -`,
because `verb_record_set`'s `--records-root` branch calls `record_set "$RP_ROOT" "${RP_RUN:-$slug}"`
with `$slug` bound to the literal `-` from the documented positional, and `rec="$root/set-$runid.md"`.
Pieces written from line 352 carry `run: <label>`. An agent following the page verbatim produces a set
record whose run identity matches none of the pieces it covers.

**Fix.** Add `--run <label>` to the example, and refuse an empty or `-` run id in `record_set` rather
than composing `set--.md` from it.

**Left-shift gate.** An arm that extracts every `unattended.sh` invocation from `SKILL.template.md` and
runs it against a scratch tree — the Skill's examples are meant to be copied, and nothing currently
executes them.

---

## Recurring-bug-class checklist — `gotchas.py --for-diff`, ten classes

Run first, as the protocol requires. Seven classes selected by anchor plus three universal. Where each
landed:

| Class | Result |
|---|---|
| `fixture-passes-by-finding-nothing` | **HIT — B2.** Every arm in `check-playbook.test.sh` mutates one fixture, so the suite runs at population 1 and cannot see the positional bug. Also HIGH 3: eight refusal arms on `record_piece`, three on its twin. |
| `two-answers-to-one-question` | **HIT — B1, HIGH 1, M4, M5, M1.** The dominant class in this diff by a distance. Five separate places where a document, a comment or a template states a guarantee the code does not implement. |
| `inputs-inside-the-subjects-reach` | **HIT — HIGH 4.** `pieces-complete` counts a population defined by a file the run can edit. |
| `assertion-between-two-derived-values` | Clear. `record_for` deliberately keys on the record's own `piece:` field rather than re-deriving the writer's path rule, and says so at 87-89. Correctly avoided. |
| `second-implementation-is-not-a-second-opinion` | Clear, same reason. |
| `status-set-in-a-subshell` | Clear. Every `fail` in both legs is a function call in the parent shell; no `FAILED` is printed from inside a pipeline. `bash -n` clean, exit codes verified live (B2's two runs returned 0 and 1 correctly). |
| `heredoc-escape-reaches-the-regex` | Clear in the shipped code. `<<CANONEOF` at 185 carries data, not source. |
| `id-matched-as-a-substring` | **ADJACENT — M3.** Not an id, but the same shape: 13 negative arms assert on the substring `check 2N FAILED`, and that substring now names two checks. |
| `containment-tested-one-way` | Not reached — the output-scope refusal (unit 8) that would have carried this risk is WITHDRAWN, not deferred, and the withdrawal is recorded honestly at spec-8 rev-6. |
| `fixture-inherits-ambient-machine-state` | Clear. Reproductions ran in hermetic scratch clones with their own `git init`; the only ambient dependency found was `.unattended.conf`, which the driver refuses to run without — a loud failure, not a silent one. |

## What this review did NOT cover

- **The full merge bar was not run.** I ran `check-playbook.sh` (green, exit 0),
  `check-playbook.test.sh` (PASS, 43 assertions), and `check-arms.py --check` (exit 0). The two long
  suites — `unattended.test.sh` (626 assertions, ~6 min) and `check-unattended.test.sh` (305, ~5 min) —
  were NOT run in this pass, nor was `run-gates.sh`. Every finding above was reproduced against the
  shipped code directly instead. A DoD still owes `GATE_FULL=1 bash tools/run-gates/run-gates.sh`.
- **No fix was applied and nothing was staged.** Every reproduction ran in a scratch clone outside the
  worktree; the tree is untouched by this review.
- **Unit 8 was not reviewed** — it is withdrawn from the landing, and only its spec's revision log is
  in the diff.
- **The rendered-Skill parity** between `tools/unattended/SKILL.template.md` and
  `.claude/skills/unattended/SKILL.md` was spot-checked at the two lines M4 and M5 name, not compared
  in full.

## Recommended landing order

1. B2 — one-line move, plus the two-playbook arm that reds first. Cheapest, and it unblocks trusting
   the leg at all.
2. B1 and HIGH 1 together — they are one join implemented twice, and the documents must be corrected
   in the same commit whichever way the decision goes.
3. HIGH 2 and HIGH 3 together — one shared helper, both writers, arms on both.
4. HIGH 5 — two lines, and it is the only finding that wedges a healthy run.
5. HIGH 4 — needs a small interface decision on `--counts`, so it wants its own commit.
6. M3 before anything else touches `check-unattended.sh`, so the renumber does not collide with
   further edits.
7. The remaining mediums and lows.
