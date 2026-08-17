## Verdict: CLEAN WITH FIXES

**review-dClosedLexicon-10 — M4 RE-audit of `spec-dClosedLexicon-11` at rev-2** · node d · 2026-08-17 ·
base `b4f0cf1c`

**Subject:** `memory/builds/dClosedLexicon/spec/2026-08-17-spec-dClosedLexicon-11.md`, rev-2, folding
`review-dClosedLexicon-9` (BLOCKED, 3 blockers + 8 defects, all in this spec).

**Shape:** four lenses, 41 raw findings; batched skeptics refuted 10; 31 survived and collapse to
**10 distinct defects** — 3 major, 7 minor, **no blockers**. All three blockers are genuinely closed:
the rotation now runs where it can run, AC4 asserts a property the kit actually has, and the archive
name is admitted by the gate that would have rejected it. What survives is a rewrite's usual residue —
two acceptance criteria the design as written cannot satisfy, one unstated grammar, and a Files-touched
estimate that is short by four files and one bar leg.

**Stop rule (M4):** the DESIGN is clean. Fold the ten below into a rev-3 with its §9 line and **stop
reviewing spec 11** — no third audit. Nothing below changes the unit's shape; every one is a sentence,
a criterion, or a list entry.

### Did rev-2 fix the eleven?

Judged against the code the fix depends on, not against §9's claim.

| prior | verdict | why |
|---|---|---|
| **11-B1** AC4 names a refusal that does not exist | **FIXED** | AC4 now asserts non-rotation and names `unattended.test.sh:543-544` as the arm that must stay green — verified those two lines are `hit "preflight OK"` + `same "a re-run preflight leaves a reached phase alone"`. §3 adds the OUT, §4 the reasoning. |
| **11-B2** rotation before the preconditions refuses itself | **FIXED** | S3 splits an early collision TEST from a late RENAME at `scaffold_runmd`'s position (`unattended.sh:851-853`, below the write gate at `:847`); §5's security bullet is rewritten; AC1 carries the exits-0-on-a-clean-tree arm the fold asked for. |
| **11-B3** the archive name reds hygiene check 4 | **FIXED in design, MIS-PRICED** | S5 amends `:284`/`:337`/`:384` — all three citations verified — with AC7 and four §7 gates. But the version cascade covers 4 of 7 marker spots (**11-13**), the admitted GRAMMAR is unstated (**11-11**), and `check-memory-hygiene.test.sh` is in neither §4 nor S8 (**11-18**). |
| **11-1** "which is the same run" is false; AC3 refuses forever | **PARTLY** | The sentence is deleted and `git hash-object` makes the name total. But the collision branch the fold widened to serve — identical bytes, verb proceeds — cannot execute under S1's `GIT mv` (**11-9**). |
| **11-2** nothing says the rotation stages the rename | **PARTLY** | S1 now mandates `GIT mv` and cites `unattended.sh:558-560` for why. The arm the fold asked for, AC3, is unsatisfiable alongside AC1 (**11-10**). |
| **11-3** S4 has no AC and no gate that could see it | **FIXED** | S6 gains check 16 with AC8; S7 names the Skill step and §4 names both `SKILL.template.md` and the rendered copy — the route review-9 itself offered. |
| **11-4** an existing gated arm asserts the opposite of S1 | **PARTLY** | S8 and §7 now say arms CHANGE. They name two edits where three are needed, describe a shared nine-arm helper as an arm-local operand, and repeat review-9's own false coupling claim (**11-15**). |
| **11-5** an ABORTED witness need not be sha-shaped | **FIXED** | The blob hash removes the separator class outright, and §4 states why the `<phase>` half is safe (closed over `PHASES_TERMINAL`, `unattended.sh:74`). |
| **11-6** §4 credits the protocol pair to check 15 | **FIXED** | §4 reads "kept byte-equal by check 10 — rev-1 credited check 15"; verified check 10 opens at `check-unattended.sh:377` with `fail 10` at `:388`/`:392`. S4 gained the checks-9/13/15 line. |
| **11-7** §7 omits the leg that judges the kit version pair | **FIXED for that leg; the class recurs** | `bash tools/check-kit-versions.sh` is in §7. The identical omission is open for the meta-gate that judges this unit's three new `fail` branches (**11-14**). |
| **11-8** the §10 probe result is asserted, not measured | **FIXED, one citation wrong** | §10 now records probe 1's real output and its MISS. Probe 2's quotation is attributed to a file and line that do not carry it (**11-17**). |

---

## [MAJOR] 11-9 — `GIT mv` cannot perform the branch §4 introduced it to make total

*(§2 S1 · §4 "The name is derived from the record's BYTES" · §6 AC5 — descends from 11-1; consolidates
ids 0.1, 1.0, 2.3, 3.0 — four lenses, all four survived skepticism)*

S1 fixes the mechanism and its failure policy in one sentence: "The rename is `GIT mv`… A failed
rename is a named refusal, never a partial rotation." §4 and AC5 then require the identical-bytes
collision to PROCEED. **MEASURED** in a scratch repo with both paths committed and byte-identical:

```
$ git mv memory/builds/x/RUN.md memory/builds/x/RUN.ABORTED.deadbeef.md
fatal: destination exists, source=memory/builds/x/RUN.md, destination=memory/builds/x/RUN.ABORTED.deadbeef.md
rc=128
```

rc=128 with the destination TRACKED and with it merely present-and-untracked; only `git mv -f` returns
0, and `-f` appears nowhere in the spec. So an implementation faithful to S1 takes the named-refusal
path in exactly the case AC5 says it proceeds. Because the rename runs late (S3), it IS attempted —
there is no branch that skips it.

§4's justification for the proceed branch also names a state the driver cannot produce: "an existing
archive whose bytes MATCH is a completed rotation and the verb proceeds". After a completed rotation
`RUN.md` is the fresh RUNNING record (`scaffold_runmd` at `unattended.sh:851-853`, phase written at
`:878`), so `refuse_if_terminal` (`:574-581`) returns 0 and rotation is never re-attempted; an
interrupted rotation leaves no `RUN.md` at all. The only reachable producer of a byte-identical archive
is a hand-placed copy — which §4 assigns to the DIFFER branch ("impossible without a hand-placed file").

**FOLD.** Say in S1 which spelling the proceed branch uses — `GIT mv -f`, or skip the rename and
`GIT rm --cached` the retired path — and state that the early collision TEST is what makes the force
safe, since a byte-DIFFERING destination has already refused before the tree was touched. Keep "a
failed rename is a named refusal" scoped to the case where that test passed. Rewrite §4's sentence to
name the state that actually reaches the proceed branch (a hand-placed byte-identical copy), not "a
completed rotation". Then say in §3 that overwriting an archive with byte-identical content is the one
touch the "no editing a retired record's CONTENT" non-goal permits.

## [MAJOR] 11-10 — AC3 and AC1 cannot both hold; an arm written to AC3's words reds on a correct build

*(§6 AC3 vs §6 AC1 and §2 S1 — descends from 11-2; consolidates ids 0.0, 1.1)*

AC1: "`RUN.<phase>.<blob8>.md` and a fresh `RUN.md` both exist". AC3: "`git ls-files` lists the archived
path and does NOT list the retired path, after a REAL rotation". **The retired path IS
`<M>/builds/<slug>/RUN.md`**, and the same verb re-creates and stages it: `verb_preflight` scaffolds at
`unattended.sh:851-853` and calls `stage_or_fail "$rel"` at `:880`, whose body is `GIT add -- "$1"`
(`stage_runmd`, `:544-545`). `git ls-files` reads the index.

**REPRODUCED** end to end — `git mv RUN.md RUN.ABORTED.<blob8>.md`, write the fresh record, `git add --
RUN.md`:

```
$ git ls-files memory/builds/x/
memory/builds/x/RUN.ABORTED.a9f6852a.md
memory/builds/x/RUN.md
```

AC3's second clause can therefore hold only on a REFUSAL — the arm would pass by observing the failure
it was written to exclude, which is this repo's `fixture-passes-by-finding-nothing` class.

**FOLD.** Restate AC3 as the property 11-2 actually asked for: *"after a REAL rotation rather than a
hand-built fixture, `git ls-files` lists the archived path, and the blob it reports at `RUN.md` is the
fresh record — `git hash-object` over `RUN.md` no longer equals the pre-call value."* Drop the
does-NOT-list clause.

## [MAJOR] 11-11 — S5 never says WHAT grammar check 4 admits, and AC7 names a control the harness cannot perform

*(§2 S5 · §6 AC7 — NEW; neither pass filed it)*

Check 4's whitelist is **string equality**, not a pattern:
`check-memory-hygiene.sh:284` is
`if (k=="F:README.md"||k=="F:STATUS.md"||k=="F:RUN.md"||k=="D:prompts"||k=="D:spec"||k=="D:build"||k=="D:reviews") continue`.
Admitting a FAMILY of names therefore requires a new regex where today there is a literal list, and the
spec never says which. The two spellings are not equivalent and the difference is load-bearing:
`RUN\..*\.md` admits `RUN.notes.md` and `RUN.md.bak` at every build root forever — a permanent widening
of the folder-grammar gate, with no waiver registry and no ratchet, and nothing that reds. A tight
`RUN\.(LANDED|ABORTED)\.[0-9a-f]{8}\.md` keeps the gate closed but hard-codes the unattended kit's
`PHASES_TERMINAL` into the memory-tree engine, which is a cross-kit coupling worth stating out loud.
(Checks 6 and 7 need no such decision: `:337` and `:384` are already regexes.)

AC7 does not settle it either, because its falsifying half names an act the gate §7 lists cannot
perform. `check-memory-hygiene.test.sh` runs the REAL engine over scratch fixture trees (`SCRIPT=
"$HERE/check-memory-hygiene.sh"`, `TMP=$(mktemp -d)`); it has no engine-variant mode, so "when S5's
whitelist edit is reverted, it reds naming that path" is unassertable there. The house's own arm for
this exact amendment — kit 2.3 admitting `RUN.md` — is the near-miss pair, `cnot 4
'memory/builds/tRunOk/RUN.md'` at `:476` against `chit 4 'memory/builds/tRunOk/RUNSTATE.md'` at `:478`.
The `cnot` half already reds when the whitelist is un-amended; the `chit` half is the one that pins the
GRAMMAR, and it is named nowhere.

**FOLD.** Write the admitted regex into S5 verbatim, with one sentence on why it is tight or loose. Then
restate AC7 as the pair the harness can express: *"a fixture carrying `RUN.<terminal>.<8 hex>.md` at a
build root is NOT named by check 4, and a fixture carrying a near-miss the grammar must still reject
(e.g. `RUN.notes.md`) IS named"* — mirroring `check-memory-hygiene.test.sh:476-478` — and keep the green
clause over the whole engine.

## [MINOR] 11-12 — AC6's first clause is enforced by nothing and its second clause is unobservable

*(§6 AC6 vs §2 S4 — consolidates ids 0.8, 1.3, 2.1, 2.2, 3.1 — five lenses)*

S4 asserts "Every archived record must be terminal" and assigns enforcement to the unchanged live-run
rule. That rule is the whole of it: `nlive` increments at `check-unattended.sh:211` for any record
outside `PHASES_TERMINAL`, and `:375` is `[ "$nlive" -le 1 ] || fail 7 …`. **It fires at TWO.** A live
`RUN.md` that has since reached LANDED plus one archived record hand-edited to `RUNNING` gives
`nlive = 1` and the leg is silent — and that is the steady state after every completed second run. S6
spends the one new check number on the protocol grep, so nothing is left to own the archive rule.

The second clause is worse-shaped: "when an archived record reads LANDED, check 15's witness-ancestry
assertion runs over it" names no observation anyone can make. That assertion (`:316-321`) only ever
calls `fail 15`; on success it prints nothing and returns nothing, so "check 15 ran over the archive and
passed" and "the archive was never in the population" produce the same empty stdout and the same exit 0.
AC7 one bullet later gets this right by carrying its falsifying half; AC6 does not.

Mitigating, and why this is minor rather than major: the widening DOES stop a hidden second live run,
which is S4's actual safety content, and during a run (live record non-terminal) a non-terminal archive
does push `nlive` to 2 and red. The hole needs a hand-edited archive in the post-landing window.

**FOLD.** Pick one. Either give the rule its own branch — a per-file `fail` when a path matching the
archive grammar carries a phase outside `PHASES_TERMINAL`, armed in `check-unattended.test.sh` — and
restate AC6's first clause against that branch; or delete "Every archived record must be terminal" from
S4 and say plainly that check 7 is all that quantifies over the wider set. Restate the second clause as
its red: *"a fixture carrying an archived record at `phase: LANDED` whose witness is not reachable from
the anchor reds at check 15, and the same fixture with the population un-widened is silent."*

## [MINOR] 11-13 — the `KIT_MEMORY_TREE_VERSION` cascade is priced at 4 of 7 marker spots

*(§4 Files touched · §2 S5 — descends from 11-B3; consolidates ids 0.3, 1.2, 2.4)*

S5 says `memory/HYGIENE.md` + `tools/memory-tree/HYGIENE.template.md` "are edited as one pair", and §4's
S5 list names four things. **MEASURED**: edited only `check-memory-hygiene.sh:13` (2.17 → 2.18) and ran
`bash tools/check-kit-versions.sh` → rc=1 with three findings, `BUILD-METHOD.template.md`,
`HYGIENE.template.md` and `SPEC-TEMPLATE.template.md` each `marker != KIT_MEMORY_TREE_VERSION (2.18)`.
The loop at `check-kit-versions.sh:81-96` derives its population from
`git ls-files 'tools/memory-tree/*.template.md'` — three files today. `kit-dogfood-parity.test.sh:53`
pairs all three against `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md`,
and all six carry `<!-- gov:kit memory-tree@2.17 -->` at line 1; the seventh spot is the inline marker on
the constant's own line. Constant restored; `git status --porcelain` empty and the leg rc=0 afterwards.

Minor because §7 already lists both catching legs, so the mis-scope reds the bar rather than landing
wrong — but it is exactly the estimate 11-B3 asked to have priced.

**FOLD.** Extend §4's S5 list to `tools/memory-tree/{HYGIENE,SPEC-TEMPLATE,BUILD-METHOD}.template.md`,
`memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md`, `memory/guides/BUILD-METHOD.md` and the engine's own
inline marker at `check-memory-hygiene.sh:13`; say in S5 that a memory-tree bump moves THREE marker
pairs, not one, and that `bash tools/memory-tree/kit-dogfood-parity.test.sh --render` moves the renders.

## [MINOR] 11-14 — §7 omits the meta-gate that judges the three `fail` branches this unit adds

*(§7 — same class as 11-7, a NEW instance; consolidates ids 0.4, 1.5, 2.5, 3.2)*

The unit adds at least three new `fail` branches: S1's named rename refusal, AC5's collision refusal,
and S6's check 16 (confirmed no `fail 16` exists — `grep -oE '^\s*fail [0-9]+' tools/unattended/check-unattended.sh`
tops out at 15). Both files are in the meta-gate's discovered population — `python tools/memory-tree/check-arms.py --report`
prints `tools/unattended/unattended.sh` at 57 branches / 56 armed and `tools/unattended/check-unattended.sh`
at 38 / 38, floors in `.memory-tree.conf:87`. The leg is `{"name": "harness arms (fail branches armed or
pinned)", "argv": ["python3","tools/memory-tree/check-arms.py","--check"]}` in `tools/gate-legs.json`
with **no guard**, so it runs on every invocation, and `do_check` appends a failure for any branch that
is neither armed by a positive assertion naming its own failure text nor pinned. §7 lists nine commands
and this is not one; the house precedent writes it out (`memory/builds/aDeclaredCeiling/spec/2026-08-16-spec-TOOL-aDeclaredCeiling-3.md:155`
AC6 and `:178` §7).

Two claims a lens attached to this are **not** folded, and I checked both: the `ARMS_FLOORS` rows are
one-sided MINIMUMS, so an armed new branch moves 38/38 to 39/39 and no floor has to move —
`.memory-tree.conf` does not belong in §4; and `memory/project/unarmed-branches.txt` pins
`unattended.sh` check 9 branch 1 = the `fail 9` at `:559`, which the rename at `scaffold_runmd`'s call
site (~`:851`) sits below, so no ordinal is renumbered.

**FOLD.** Add `python tools/memory-tree/check-arms.py --check` to §7, and give S1's failed-rename
refusal an AC — an unarmed new branch is a red on every bar run.

## [MINOR] 11-15 — "two arms CHANGE" is wrong in both directions, and the third edit is named nowhere

*(§2 S8 · §7 — descends from 11-4; consolidates ids 0.5, 2.6, 2.9, 3.8)*

Three separate problems in one sentence.

**(a) `sum()` is a shared helper, not an arm-local operand.** `unattended.test.sh:137` defines it once —
`sum() { git hash-object memory/builds/tRun/RUN.md; }` — and `$(sum)` appears 18 times across nine arms
(`:142/145`, `:149/152`, `:443/446`, `:566/568`, `:809/811`, `:821/823`, `:867/869`, `:918/923`,
`:933/935`), every one proving a refused verb wrote nothing. §7 calls it "`unattended.test.sh:919`'s
drive list and its `sum()` operand". **MEASURED** that re-pointing the definition would be a dead probe
in eight unrelated places: `git hash-object <missing>` exits 128 with EMPTY stdout, so `before` and after
are both `""` and `same` passes.

**(b) S8's justification is false of the code.** "The population it drives is derived from source at
`:912` … so the drive list cannot shrink silently." What `:912` derives is a COUNT of phase writers in
the DRIVER — `writers=$(grep -c 'set_fact "$rel" phase' "$SCRIPT")`, measured 5 (`unattended.sh:699`,
`:745`, `:809`, `:878`, `:977`) — checked at `:913` against a literal 5. The drive list at `:919` is a
hand-written five-member literal with nothing tying it to `writers`. Deleting a member reds nothing. The
arm catches a SIXTH writer; it has never caught a shrinking list.

**(c) A third edit is required and unnamed.** Once S8 drops `--preflight`, the list holds four while the
literal stays 5 and the arm's own message — "this arm drives 5" — becomes false. Setting it to 4 reds
immediately. The spec leaves the implementer to guess.

**FOLD.** State it as one change plus one addition plus one restatement: the drive list at `:919` loses
`--preflight`; a NEW arm compares `git hash-object` over the computed archive path (AC2 already pins
byte-identity to `cmp -s` against a pre-call copy, which is the right mechanism — say so once);
`sum()` at `:137` is **unchanged**; and `:913`'s message is re-worded, or its literal replaced by a
derivation that counts the drive list plus the separately-armed member, so the ratchet still names what
it bounds.

## [MINOR] 11-16 — S4 and §8 F1 cite `:137`; the population selector is `:138`

*(§2 S4 · §8 F1 — consolidates ids 0.7, 1.6, 2.8, 3.5)*

```
132:FILES=$(git ls-files "$M/")
137:PRE=$(printf '%s\n' "$FILES" | grep -cE '(^|/)RUN\.md$' || true)
138:RUNS=$(printf '%s\n' "$FILES" | grep -E "^$M/builds/[^/]+/RUN\.md$" || true)
139:POP=$(printf '%s\n' "$RUNS" | grep -c . || true)
```

`:137` is the mis-segmentation PRECONDITION counter, consumed only by the guard at `:140-142`; `:138` is
the population every per-file check iterates (`while IFS= read -r f … done <<<EOF $RUNS`, `:194`/`:369-371`).
§8 F1 attributes the `:138` regex to `:137` verbatim, and S4 tells the implementer to widen `:137`. The
neighbouring citations are all correct — `:132` for `FILES`, `unattended.sh:434` for `check_single_live`'s
`GIT ls-files "$M/builds/*/RUN.md"` — which is what makes this a miss rather than drift
(`git diff b4f0cf1c..HEAD -- tools/unattended/` is empty).

**FOLD.** Re-cite as `check-unattended.sh:138` in both places, and say explicitly that `:137`'s `PRE`
stays as-is: it is the precondition, not the population, and an archives-only tree reading PRE=0 with
POP>0 is silent by design.

## [MINOR] 11-17 — §10 probe 2 quotes a sentence the cited line does not carry

*(§10 — descends from 11-8)*

§10 credits `TOOL-cFinalBerth-1` at `memory/DECISIONS.md:47` with "a terminal record cannot re-open".
**RE-RUN** the probe exactly as §10 records it — `python tools/memory-recall/query.py "<the §10
question>" --terms "<the §10 terms>"` — 36 hits, and the two rows are distinct: hit **[4]** is
`memory/DECISIONS.md:47`, which reads *"a terminal phase is written by a verb that EVALUATES what it
claims, never by a phase move…"*; hit **[10]** is `memory/archive/TOOL.2026-08-14.md:53`, the CLOSED
backlog row that carries the quoted sentence. `grep -n "re-open\|reopen" memory/DECISIONS.md` returns rc
1. The other half of §10 reproduces exactly: hit **[1]** is
`memory/builds/cFinalBerth/reviews/2026-08-13-review-cFinalBerth-2.md:98`, which is F2's heading line.

**FOLD.** Cite the quotation to `memory/archive/TOOL.2026-08-14.md:53`, and cite `memory/DECISIONS.md:47`
for what it says — a terminal phase is written by an EVALUATING verb, never by a phase move — which is
the sharper constraint on a rotation that hands a second run a fresh record.

## [MINOR] 11-18 — §4 Files touched omits `AGENTS.md` and the hygiene self-test

*(§4 · §2 S8 — consolidates ids 1.7, 2.10, 3.3, 3.4)*

Two omissions, both of files the unit certainly edits.

`AGENTS.md:138` reads "(fifteen checks — the declarations parse, the CORE phase and DoD sets have not
shrunk below their floor, …)" and `check-unattended.sh:2` reads "FIFTEEN checks over the tree". S6 adds
a sixteenth. §4 names the leg and not the charter, and **nothing gates the number**: the only charter
probe over the gate suite, `_charter_mentions_every_leg` (`tools/drift-audit/drift_signals.py:104-136`),
matches leg argv SCRIPT PATHS and never reads a count. Prior art puts it in Files touched for exactly
this move: `memory/builds/cBriefedPilot/spec/2026-08-14-spec-cBriefedPilot-12.md:111` carries the row
"| `AGENTS.md` | the gate-suite bullet's check count, fifteen to sixteen |".

Separately, AC7 requires an arm in `tools/memory-tree/check-memory-hygiene.test.sh` and §7 gates it, but
§4's S5 list ends without it and S8 scopes arms to "`tools/unattended/unattended.test.sh` and
`check-unattended.test.sh`" — no third file. The 11-B3 fold landed the Gates half and not the
Files-touched half.

**FOLD.** Add `AGENTS.md` to §4 with the reason (the gate-suite bullet's check count, fifteen to
sixteen) and the note that no gate watches it; add `tools/memory-tree/check-memory-hygiene.test.sh` to
§4 and name it in S8 alongside the two unattended self-tests.

---

## What was checked and found sound

Coverage, not courtesy — each of these was independently re-derived or re-run against source in this
worktree, and each is a claim a lens attacked and failed to break.

- **11-B2 is genuinely closed, including the residue a lens claimed survived.** The refusal string
  `the run-state file is unchanged` is emitted only at `unattended.sh:847`, above the rename's position,
  so it is never printed over a rotated tree. The four `fail` branches below the write gate
  (`fail 9` at `:863`/`:867`, `fail 17` at `:896`, `stage_or_fail`'s `fail 9` via `:880`) sit in the
  window the driver's own comment at `:849-850` already frames the same way, and `scaffold_runmd` writes
  there today.
- **S5's three hygiene citations are exact.** `:284` is the seven-entry whitelist, `:337` the
  `index_set` RUN.md line, `:384` the `ex7` prose exemption — all verified verbatim. The check 6 / check 7
  amendments are not decoration: `memory/builds/dClosedLexicon/RUN.md` carries an 868-character line, so
  widening `:337` without `:384` would red check 7 and AC7's green clause with it. AC7 is not a dead
  probe.
- **Check 8 needs no archive-awareness.** `check-unattended.sh:254` is `rd=${f%/RUN.md}/README.md`,
  which does not strip an archived basename — but `:255` is
  `case " $PHASES_TERMINAL " in *" $ph "*) rd="" ;;` immediately after it, so check 8 skips every
  terminal record whatever its path shape. The derivation is inert for the population S4 adds.
- **The blob-hash name is stable across this fleet.** `.gitattributes` pins `memory/**/*.md text eol=lf`,
  which covers `RUN.*.md` as well as `RUN.md`, and `git hash-object` applies the path's clean filter by
  default — so the derived name is the INDEX blob's on Windows and Linux alike.
- **The unit moves no generated map artifact.** `memory/map/generated/symbols.json` carries 464 rows and
  **zero** naming anything under `tools/unattended/`; the map's extractors do not read shell. §7's
  omission of `test_codebase_map.py` is correct, and the unit adds no leg, kit, hook or guide that its
  inventories count.
- **11-5's fix is real, not restated.** `PHASES_TERMINAL="LANDED ABORTED"` at `unattended.sh:74` is the
  closed set `is_terminal` tests against, so the `<phase>` half of the name cannot carry a separator, and
  the blob half cannot either. The witness-shape hole the name used to inherit
  (`check-unattended.sh:216-218` presence-only, `:222-227` skip-if-not-sha, `:239-244` guarded by
  `if [ "$ph" = LANDED ]`) is now simply off the name's path.
- **AC4's cited arm says what the spec says it says.** `unattended.test.sh:543-544` is
  `hit "$out" "preflight OK"` then `same "a re-run preflight leaves a reached phase alone" … "BUILDING"`.
  Building to rev-1's AC4 would have red it; rev-2's AC4 leaves it green.
- **§4's check-10 correction is right.** `check-unattended.sh:377` opens "10: the kit ships what this
  repo runs. ONE pair.", with `fail 10` at `:388` and `:392`. Check 15 is the LANDED-witness pair.
- **Ten of 41 raw findings were refuted by the skeptics and are not folded**, including: that the check 6
  index cap opens an unrepairable red (the cap already applies to the live terminal record, the largest
  today is 8141 B against a 20480 B cap, and `curation-debt.txt` is a declared escape); that S7 lacks a
  gate (the `--check` block at `adopt-unattended.sh:112-147` renders to a temp file, `diff -q`s it
  against the installed Skill and refuses a surviving `{{…}}`, which is
  exactly what S7 claims — the `--check` block opens at `adopt-unattended.sh:112`); that check 16's literal is unspecified (S2 fixes the token
  `RUN.<phase>.<blob8>.md`, and `grep -n 'RUN\.' memory/guides/UNATTENDED-PROTOCOL.md` returns one line
  today, so AC8's negative fixture is the pre-edit file); and that §5's `hygiene-parity.test.sh` sentence
  over-claims (it says only that the floor derives from the constant, which
  `hygiene-parity.test.sh:19-20` states in those words).

## Reproduction environment

Worktree `.claude/worktrees/run-gates-performance-f1f419`, base `b4f0cf1c`
(`git diff b4f0cf1c..HEAD -- tools/unattended/` empty). `git mv` measured in two scratch repos, one with
the destination tracked and one with it untracked; the AC1/AC3 sequence reproduced end to end in a third
(`git mv` → fresh `RUN.md` → `git add`, then `git ls-files`). The version cascade measured by editing
`check-memory-hygiene.sh:13` alone and running `bash tools/check-kit-versions.sh`, then restoring
(`git status --porcelain` empty, leg rc=0). `check-arms.py --report` and `--check` run on the real tree.
`git hash-object` on a missing path measured for its exit code and empty stdout. §10's probe 2 re-run
with the question and terms §10 records, verbatim.
