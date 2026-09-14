**Serves:** spec-audit KICK-aReplayedCard-1 KICK-aReplayedCard-2 KICK-aReplayedCard-3 TOOL-aReplayedCard-1 TOOL-aReplayedCard-2 TOOL-aReplayedCard-3 TOOL-aReplayedCard-4 TOOL-aReplayedCard-5

# aReplayedCard — spec audit of the four rev-2 units, round 2

*Node `a`, 2026-09-14. A Tier-2 adversarial pass over the four specs round 1 BLOCKED, at their rev-2
blobs: a fan of four primed finder lenses, a skeptic stage in five batches prompted to REFUTE each
finding, one synthesis. The mandate was the FOLD, not the original text: for each of round 1's 27
defects, does the rev-2 line that claims to close it actually close it, and did closing it open
something else — a widened merger schema, a `{here}` token across three readers, a deny set of
`commit` alone, a NEW-README exemption staged or untracked, `buildComparablePath` on both sides, a
manifest `registry:` key, `corpus_ids.py --print-defined-ids`. The four were cross-read against their
unchanged siblings KICK-2 (rev-2), TOOL-3 (rev-2), TOOL-4 (rev-1) and TOOL-5 (rev-2) on the four M2
axes, and every code claim was checked against the cited file and line. The synthesis re-read at
source every claim a blocker or high below rests on and reproduced three of them in a scratch
repository; what it re-read and what it did not run is listed at the end. The binding line names
all eight units because the cross-read read all eight and two fixes below land on siblings.*

**Round: 2.** Subjects, each pinned at the blob it was read at:

- `memory/builds/aReplayedCard/spec/2026-09-13-spec-KICK-aReplayedCard-1.md@cdc98a80a01637f8a53ceda00d74fc21f2b62857`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-KICK-aReplayedCard-3.md@11a6301a7be591d61f33e4cbcd5a033651508a96`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-1.md@50ce585dcb9c7f66e923ce1702b33fea4ce80d3e`
- `memory/builds/aReplayedCard/spec/2026-09-13-spec-TOOL-aReplayedCard-2.md@5d8568ff166bbd9768df3dd482959598a30294fc`

## Verdict: BLOCKED

One blocker stands, and it is a defect the fold itself created. Round 1's M11 asked `TOOL-aReplayedCard-1`
to fail open when no `orientation/` directory exists, so a hooks-kit-only adopter is never denied; rev-2
did that, and then rested its whole Rollout on "between the two commits no `orientation/` directory
exists here". It does exist: `KICK-aReplayedCard-1` at order 2 observes AC1, AC4, AC5 and AC6 "from this
worktree" and writes `<git-common-dir>/orientation/t1.md` into the real shared common dir, with no
cleanup stated. The hook runs from the working tree, so the moment TOOL-1's check is saved at order 3,
step 4 finds the directory, step 6 finds no card for the landing session's own id, and every
main-loop `git commit` from that point — including the one that lands TOOL-1 — is denied with a remedy
(`/session-kickoff`) that cannot append a READY line until order 5. The only exits are the escapes the
spec's own header names as evasion. Thirteen high defects follow, in four clusters: the fragment
markers TOOL-2 chose contain a space that `check-wiring.sh` strips before it looks; the class arm that
was round 1's B1 left-shift quantifies over an empty population; the tightened token grammar misses
the `git -C <dir> commit` spelling the charter prescribes on every node; and the `tree —` cell the deny
compares is written once and never rewritten, so a session that moves trees is denied for life with
a remedy that cannot change the cell. Of round 1's 27 defects, 17 are closed clean, 8 are closed with a
residue named below, and 2 are reopened in a new place (M5 twice, M11 as the blocker).

## Review shape

Raw 80, confirmed 39, refuted 41, unverified 0, precision 0.49. Precision sits just under the ~0.5
floor §8 sets before adding agents, one point above round 1; the refutations concentrated again in
findings that read a rev-2 sentence for rule conformance without checking the mechanism it names,
and half of the confirmed set is four lenses finding one defect from four angles. The response by §8's
own rule is unchanged: tighten priming, do not widen the fan.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0 contradictory
verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by the pipeline's
dedup stage. The run is complete on its own terms. Because no lens died, the zero on the four unchanged
siblings is a zero from a full cross-read by all four lenses, not a zero from absence; it remains a spec
audit's zero, which grades what a document says and not what a mechanism will do. The pipeline's dedup
found 0, but 39 confirmed findings name 23 distinct defects — four lenses found the space in the
marker, four found the empty class-arm population, four found `git -C`, four found the three-not-four
groups. The fold below is editorial and keeps every raw id. Each raw id takes the severity of the
defect it evidences, so the per-id table and the integers in the state block agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| B1 the Rollout's "no `orientation/` directory exists here" is false by the build's own order | blocker | 1, 22, 44 |
| H1 the fragment markers carry a space no reader can match | high | 2, 25, 45, 65 |
| H2 the class arm's population is empty | high | 3, 23, 43, 67 |
| H3 `git -C <dir> commit` escapes the token grammar | high | 4, 24, 55, 77 |
| H4 the `tree —` cell is written once and the remedy cannot rewrite it | high | 5 |
| M1 AC10 reads `--card --append` from a same-step sibling | medium | 6, 30 |
| M2 TOOL-3 AC2 reads KICK-3's Step 5b append in one step | medium | 35 |
| M3 Step 5's piped body omits `## task` and `## read` | medium | 8 |
| M4 the current branch is in neither Step 1 list | medium | 9 |
| M5 the repair commit's moment is unstated; §3 contradicts Files touched | medium | 10, 73 |
| M6 AC3's four groups are three under the merger's own rule | medium | 13, 27, 52, 66 |
| M7 `govkit apply --dry-run` does not exist | medium | 14 |
| M8 `/session-kickoff` loads the primary's engine through a junction | medium | 50 |
| M9 `registry:` misses the seed template and the version bump | medium | 69 |
| M10 S4 ships R8's fragment without citing R8 or fixing the adopter's remedy | medium | 71 |
| M11 the `{here}` flat-kit rule is undecidable for `tools/` | medium | 72 |
| M12 the untracked pathspec misses a top-level `builds/` | medium | 36 |
| L1 S4 "Observed by AC2" is a false join | low | 18 |
| L2 "5 B of headroom" is 3 B | low | 20 |
| L3 twelve arms, eleven rows | low | 37 |
| L4 `tool_use_id` fails open on a field the predicate never reads | low | 54 |
| L5 the include without its `claims` half reds selfcheck rule 4b | low | 75 |
| L6 `WIRE-INTO-PROJECT.md:610-612` contradicts S8's step | low | 76 |

Tally by raw id: **3 blocker · 13 high · 17 medium · 6 low** = 39. Four severities were RAISED from
the skeptic's verdict and are argued where they sit: 1 and 44 (skeptic: high) take B1's blocker, and
55 and 77 (skeptic: low) take H3's high, because each evidences the one defect its cluster names. One
was LOWERED: 66 (skeptic: high) sits in M6, because a criterion that reds loudly against a correct
merger is the wrong-document class, and the restructure it fears is a builder choice S3's own text
argues against.

## The fold, defect by defect

What rev-2 did with each of round 1's 27, read against the mechanism rather than the §9 line.

| Round 1 | Rev-2 fold | Verdict |
|---|---|---|
| B1 the deny catches the kickoff's own git | set is `commit` alone as a whole token; AC9 class arm | closed for the ff and `merge-base`; the class arm is dead (H2) and the grammar opened `-C` (H3) |
| B2 the push is denied | `push` dropped; §8 records why | closed |
| B3 the fragment schema cannot carry the commands | `interpreter` + `args`, whole-command repath | closed as a schema; the markers it enables are unmatchable (H1) and §5's quoting contradicts `merge():228` (H1) |
| B4 two path alphabets | `buildComparablePath` both sides; one declared spelling | closed for the alphabet; the cell is never rewritten (H4) and the cross-kit arm reads a same-step sibling (M1) |
| H1 the sentinel satisfies READY | tail-not-`none yet` in TOOL-1 S2 and KICK-2 S5 | closed |
| H2 `ff —` undecidable | cell removed; verb never fetches; AC9 asserts refs unchanged | closed |
| H3 two registry tables | manifest `registry:` key, first table under the heading, prefix match | closed here; the seed template and version bump were missed (M9) |
| H4 `git grep -l` cannot name the token | KICK-2 S1 `git ls-files -- <paths>` and `corpus_ids.py --print-defined-ids` | closed (cross-read, no finding) |
| H5 the re-match relocates the writer | two fragments, disjoint markers, re-match scoped marker+event, AC3 | partial: the markers cannot be found (H1); AC3's expected shape is wrong (M6) |
| H6 `{kit}` for a flat kit | `{here}` in three readers; flat-kit adopter rule; parity arm | partial: the rule is not a function for `tools/` (M11) |
| H7 no descriptor rows | S7 claims; `govkit selfcheck` in §7 | partial: include without `claims` reds 4b (L5); AC8 names a verb that does not exist (M7) |
| H8 the exemption reads an empty index | untracked arm on the NEW README | closed in principle; the pathspec and cwd are wrong (M12) |
| H9 the fixture reaps the live keepalive | TOOL-3 AC2 in a scratch clone | closed (cross-read); the clone inherits the junction gap (M8) |
| M1 keys no extractor mints | claim dropped as a dead key | closed |
| M2 three cells with no criterion | joined AC2; `live — skipped:` | closed |
| M3 a consumed card drops the STOP and pins a stale BASE | S1 keeps `rev-parse HEAD`, `status --short`, the ff | closed for BASE and STOP; the branch fell out of both lists (M4) |
| M4 replay carries no `--registry` | `--registry` removed everywhere; the manifest names it | closed |
| M5 a same-step acceptance input | KICK-3 and TOOL-3 to order 5 with edges | REOPENED twice: KICK-3/TOOL-3 share step 5 (M2); TOOL-1 AC10 reads KICK-2 in step 3 (M1) |
| M6, M7 TOOL-5 | not a subject; rev-2 read for the cross-read | no finding |
| M8 a mention-grep passes an orphan | `corpus_ids.py --print-defined-ids` | closed (cross-read) |
| M9 basename citations skipped | resolve when unique, annotate ambiguous | closed (cross-read) |
| M10 `ARMS_FLOORS` cannot cover an exit-coded refusal | env-error shape; `FLOOR_ASSERTIONS` alone | closed |
| M11 the hooks kit alone denies with no remedy | step 4 fails open on no `orientation/` directory | REOPENED as B1: the directory-keyed fail-open is what the Rollout rests on, and KICK-1 defeats it |
| L1 a kit README nobody builds | script header + runbook | closed |
| L2 two dossier writers | KICK-3 alone | closed |
| L3 TOOL-5's unlisted legs | not a subject | not re-checked |

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| B1 | blocker | TOOL-1, KICK-1 | TOOL-1 §4 Rollout and Migration, §4 step 4, §2 S5; KICK-1 §6 AC1/AC4/AC5/AC6, §2 S5 | KICK-1's in-repo ACs create the real `orientation/` at order 2; TOOL-1's step 4 is defeated at order 3 and the landing run is denied with no bootstrap. |
| H1 | high | TOOL-2 | §2 S1, S6; §5 security; §6 AC1, AC7 | Markers `--card --write` and `--card --replay` carry a space; `matchers_of` strips whitespace before `grep -F`, and passes the marker as an option. |
| H2 | high | TOOL-1, KICK-3 | TOOL-1 §2 S7, §6 AC9, §7 row 9; KICK-3 §6 AC5 | "Every fenced `git …` command from Steps 0–4" is zero commands; the DERIVED figure derives nothing and nothing refuses. |
| H3 | high | TOOL-1 | §2 S1, S6; §6 AC9 | `git -C /c/x commit` and `git -c k=v commit` never match: the value token is not dash-prefixed; the charter prescribes the form. |
| H4 | high | TOOL-1, KICK-1, KICK-2 | TOOL-1 §2 S2, S3, §6 AC3; KICK-1 §2 S3, S5; KICK-2 §2 S5 | The `tree —` cell is written once; `--replay`, `--append` and Step 5 never rewrite it; a moved session is denied for life. |
| M1 | medium | TOOL-1, KICK-2 | TOOL-1 §6 AC10, §2 S7 second arm, status header; build order step 3 | AC10 appends "through `--card --append`", KICK-2's verb, in the same parallel step. |
| M2 | medium | KICK-3, TOOL-3 | KICK-3 status header; TOOL-3 §3 Edges, §6 AC2; build order step 5 | TOOL-3 AC2 needs KICK-3's Step 5b append; both carry order 5. |
| M3 | medium | KICK-3 | §2 S2, §4 Data model; against KICK-2 §4 | S2's five items omit `## task` and `## read`, the card's scope and its entrypoints. |
| M4 | medium | KICK-3 | §2 S1, §6 AC1 | The current branch is neither card-satisfied nor still-run; the READY line and the STOP read a stale cell. |
| M5 | medium | KICK-3 | §2 S3, §3, §4 Files touched, §6 AC5 | The repair commit is "after the append" but before or after the halt is unsaid; §3 says Steps 2–4 are unchanged while Files touched edits 2b. |
| M6 | medium | TOOL-2 | §6 AC3; against §2 S3, S4 | Two of the four fragments share `startup|resume|clear`; `merge()` groups by matcher, so the result is three groups, and reversed order reverses the pair. |
| M7 | medium | TOOL-2 | §6 AC8 | `govkit.py` has no `--dry-run`; `plan` is the read-only verb. |
| M8 | medium | KICK-3, TOOL-3 | KICK-3 §6 AC1/AC2, §4 Migration; TOOL-3 §6 AC2 | `%USERPROFILE%\.claude\skills\session-kickoff` is a junction to the PRIMARY tree; `/session-kickoff` on this branch runs the old engine. |
| M9 | medium | KICK-1 | §4 Files touched and Migration, §5 migration | Every prior audit-block key rode a format bump and a template edit; `registry:` touches neither. |
| M10 | medium | TOOL-2 | §2 S4, S7; §9; §10 | aReapedSpinner R8 asked for this fragment and the adopter's two-fragment remedy; S4 ships the file, cites nothing, fixes no remedy. |
| M11 | medium | TOOL-2 | §2 S5, §6 AC5/AC6 | Ten flat descriptors declare `home = "tools"`; "the descriptor whose home is the fragment's directory" is not a function. |
| M12 | medium | TOOL-1 | §4 Data model step 5; §2 S4; §6 AC4/AC8 | `'*/builds/*/README.md'` misses a top-level `builds/x/README.md`; the spawn's cwd is unstated. |
| L1 | low | KICK-3 | §2 S4 | Step 5b's append says "Observed by AC2"; AC2 observes an attended Step 5 that never reaches 5b. |
| L2 | low | KICK-1 | §3 Edges, §4 Alternatives | The manifest is 25597 B against 25600 at c4f02308: 3 B, not 5. |
| L3 | low | TOOL-1 | §4 Files touched, §5 testing; §7 | "Twelve arms" twice; eleven New-arm rows; AC12's `ls` payload has none. |
| L4 | low | TOOL-1 | §2 S5, §4 step 3 | `scratch-guard.js` reads no `tool_use_id`; a silent fail-open on it is green-by-absence. |
| L5 | low | TOOL-2 | §2 S7, §6 AC8 | `check-wiring.kit.toml` declares `to` AND `claims`; an include with no claim reds selfcheck 4b. |
| L6 | low | TOOL-2 | §2 S8, §4 Files touched | The runbook's "add SessionStart by hand" line stands beside the new fragment step. |

---

### B1 — blocker — TOOL-1 §4 Rollout and Migration, §4 Data model step 4, §2 S5; against KICK-1 §6 AC1, AC4, AC5, AC6 and §2 S5 — raw 1, 22, 44

**The defect.** Rev-2 closed round 1's M11 with predicate step 4: "No `orientation/` directory under
the resolved common dir → allow, one stderr line." Rollout then rests on it: "Between the two commits no
`orientation/` directory exists here, so step 4 allows every commit." Read against the sibling that
runs first: KICK-1 AC1 runs `--card --write --session t1` "from this worktree" and asserts the file
lands under `git rev-parse --git-common-dir`/orientation/; AC4, AC5 and AC6 run in the same place;
nothing removes the directory. From this worktree that common dir is `C:/projects/coding-governance/.git`,
shared by every worktree on the node — verified absent at the synthesis, so KICK-1 is what will create
it. `.claude/settings.json` runs `node "${CLAUDE_PROJECT_DIR}/tools/hooks/scratch-guard.js"`, the working
tree's copy, so the check is live the moment the file is saved at order 3, before the commit that lands
it. At that moment step 4 finds the directory and step 6 finds no card for the landing session's own
`session_id`: the writer is wired at order 4, the engine appends at order 5, and the session started
before either. BUILD-METHOD M6 has the run commit at the end of every pass, on the main loop; the
unattended driver commits nothing itself (`unattended.sh:1591`, "NO driver verb commits"). So the
commit landing TOOL-1 and every main-loop commit after it is denied, with a remedy (`/session-kickoff`)
whose append clause does not exist until order 5.

The exits are the ones S6 names as the ceiling: delete `orientation/`, commit from a subagent, commit
through a script, or hand-write a card under the session id the deny's own stderr prints in the card
path. The build would land itself by the evasion its header describes. Migration's "inert until the
next session start" is inverted for the same reason the common dir is shared: once a NEW session's
startup writer creates the directory, every session already running on the node is denied until it
compacts (replay writes a fresh card, KICK-1 S5) and then kicks off — sessions that never had a
session start after the wiring.

**Why blocker, raised from the skeptic's high on 1 and 44.** Severity is what ships. What ships is a
Rollout paragraph that is false by the build's own order, a landing run that cannot make a main-loop
commit from order 3 to the end, and an exit that is the guard's named evasion — the same class round 1
called B4. A pass dispatched as a subagent whose shell carries `agent_id` passes step 2, and that is
the "commit from a subagent" escape, not a bootstrap.

**Fix.** The lazy one, which also makes the deny honest about what absence means: split step 6 —
card ABSENT → allow with one stderr line naming the writer that did not run for this session;
sentinel-only or tree-mismatch → DENY. Once wired the writer runs at every SessionStart and replay
rewrites a missing card, so absence means the harness skipped it; deleting one's own card is already
inside the S6 ceiling. Move AC1 to expect exit 0 plus the line, keep AC2 as the deny observation, and
drop step 4's directory probe, which becomes redundant. Alternatively keep step 6 and (a) move KICK-1's
AC1/AC4/AC5/AC6 into the self-test's scratch repository as AC9/AC10 already are, and (b) record in the
build README how the landing session writes and appends its own card before its first post-order-3
commit — the one hand-written card that is sanctioned. In every case rewrite Rollout to say what is
true at order 3, and rewrite Migration to state the shared-common-dir effect on running sessions.

**Left-shift.** An arm in `scratch-guard.test.sh` that stages exactly the landing state — directory
present, no card for the payload's `session_id` — and asserts the verdict Rollout claims, observed RED
first. And a KICK-1 self-test arm asserting the real common dir holds no `orientation/t*.md` after the
suite, so an in-repo observation cannot leave the fixture behind for a sibling to trip on.

---

### H1 — high — TOOL-2 §2 S1 and S6, §5 security, §6 AC1 and AC7 — raw 2, 25, 45, 65

**The defect.** S1 pins the markers as "equal to their argument strings": `--card --write` and
`--card --replay`. S6 builds the `card` arm "on the recall arm's pattern", which is `wired()` at
`tools/check-wiring.sh:168`, over `matchers_of` at `:157-166`. That function runs
`tr -d ' \t\r\n'` over `settings.json` BEFORE `grep -F "$1"`, so the rendered command reads
`manifest-check.sh"--card--write` by the time the marker is looked for, and a marker with a space can
never match. Reproduced at the synthesis over a correctly merged settings file: `grep -F "--card --write"`
exits 2 with `unknown option -- card --write`, because the marker is passed as an option with no `-e`
or `--` separator; with a separator it exits 1. Either way the arm prints `UNWIRED card` at every
SessionStart in every tree, forever, over a file the merger reports as wired. That is the "train every
node to ignore the verifier" state the recall arm's own header warns about, and AC7's `ok card` is
unreachable.

A second reader disagrees in the other direction. §5 says `args` are "rendered as separate quoted
tokens"; if so the command holds `"--card" "--write"`, `--card --write` is not a substring of it, and
`merge()` at `settings-merge.py:228` (`marker not in command`) never dedups — a second entry is
appended on every run and AC1/AC3's one-entry-per-group reds. Under unquoted rendering AC7 cannot
green; under quoted rendering AC1 and AC3 cannot. Every marker shipped today is a basename. S4 names
no marker at all for the check-wiring and procmon-session fragments.

One more thing the fold must know: `matchers_of` passes `"$1"` to `grep -F` with no `-e`, so ANY
marker beginning with a dash — including the space-free `--write` the obvious fix reaches for —
exits 2 as an option. Reproduced. The fix has to touch the reader, not only the marker.

**Fix.** Markers `--write` and `--replay` (a substring of the rendered command under either quoting,
distinct from each other, absent from every other command in `settings.json`), and `matchers_of` gains
`-e` before `"$1"` — one token in a file already in Files touched. §5 states the rendering as unquoted
argv tokens joined by single spaces, the shape the live `bash "…/check-wiring.sh" --session` entry
already has. S4 states the check-wiring fragment's marker as `check-wiring.sh` and procmon-session's
as `procmon-hook.js` (the re-match is scoped to marker AND event, so sharing a basename across events
is safe and should be said). AC7 gains an arm that runs the real `check-wiring.sh --check` over the
merger's own output.

**Left-shift.** A merger self-test arm that, for every tracked `*.fragment.json`, applies the fragment
and then runs `check-wiring.sh`'s `matchers_of` over the result, asserting the fragment's matcher comes
back. Two readers of one marker owe a parity arm, and this one exercises the stripped view the arm
actually reads rather than a Python substring beside it.

---

### H2 — high — TOOL-1 §2 S7 and §6 AC9, §7 New-arm row 9; mirrored in KICK-3 §6 AC5 — raw 3, 23, 43, 67

**The defect.** Round 1's B1 left-shift asked for a class arm over "every fenced `git …` command from
`skills/session-kickoff/SKILL.md` Steps 0–4", and rev-2 wrote exactly that: S7 "feeds every fenced
`git …` command … as a no-card payload expecting ALLOW", AC9 "figure: DERIVED — the arm extracts the
commands from the engine file at run time". Measured at base: Steps 0 through 4 span lines 33–195 and
hold exactly three fences, at `:71` (`bash <check-script> --locations`), `:138` (`--task-skeleton`) and
`:176` (`python <MEMORY_TREE_KIT>/gotchas.py --for-paths`). None is a git command. Every git command in
that range is an inline code span — eight of them, from `git -C` to `git worktree list` — and the Step 1
batch at `:49-51` is bare prose whose fast-forward is spelled `merge --ff-only <remote>/<default>` with
no `git` token at all. The population is zero. The arm extracts nothing, the DERIVED figure is 0, and
nothing in the spec refuses an empty extraction, so the arm passes on the four hand-typed literals
while reading as a class gate — the could-not-fail shape §7 forbids and the auto-memory note "a
zero-guard does not catch some" records. TOOL-1 lands at order 3, before KICK-3 touches the engine, so
nothing changes this at landing.

KICK-3 AC5's second clause, "the fenced git commands of Steps 0 through 4 contain no `git commit`",
is vacuously true for the same reason and can never red on the regression it names; the repair commit
is prose.

**Fix.** State the extraction rule that matches the file: every inline code span in Steps 0–4 that
begins `git ` (8 at base), PLUS the Step 1 batch spelled as literals in the arm (`git fetch`,
`git merge --ff-only origin/main`, `git rev-parse HEAD`, `git status --short`, `git worktree list`).
Assert the extracted count is at or above a floor stated with its base figure, and REFUSE (red, named)
on zero — the `check-hook-destinations.sh` precedent. KICK-3 AC5: replace the fenced clause with "no
inline `git commit` span exists in Steps 0–4 and Step 2b's ordering sentence is present by text".

**Left-shift.** The refusal on an empty population IS the gate. Beyond it, a `check-arms.py`-style
rule that any test arm whose spec line says DERIVED prints the count it derived, so a zero is visible
in the PASS line rather than inferred from it.

---

### H3 — high — TOOL-1 §2 S1 and S6, §6 AC9 near-miss literals, §4 Inventory `COMMIT_SHAPED` — raw 4, 24, 55, 77

**The defect.** The tightened grammar is "the argv token `git`, optional dash-prefixed flags, and then
the whole argv token `commit`". `-C <dir>` and `-c <key=val>` each take a value token that is not
dash-prefixed, so `git -C /c/projects/x commit -m y` and `git -c user.name=x commit` never match, and
an allow prints nothing. The charter's §2 registry row for node `a` and §11 prescribe `git -C` with
forward-slash paths on every registered node, the engine's own Step 0 (`SKILL.md:44-45`) repeats it,
this harness resets cwd between shell calls so an absolute `git -C` is routine, and the §16 layout note
says sessions often open at the worktrees' parent. A charter-prescribed spelling of the very command
the deny exists for passes silently; S6's ceiling does not list it, so the header claims coverage it
lacks — the §7 class the spec itself invokes. `--git-dir=`, `--work-tree=` and `--namespace=` share
the shape. The tree-cell compare is also undefined for `-C`: the cwd-derived toplevel is the parent
tree while the commit lands in the target.

**Why high on all four ids, raised from the skeptic's low on 55 and 77.** One defect, one grammar;
the two low verdicts read the same miss as one more near-miss literal, and it is not a near-miss — it
is a routine hit the header would say is covered.

**Fix.** State the grammar: after `git`, skip dash-prefixed tokens and the one value token following
`-C`, `-c`, `--git-dir`, `--work-tree`, `--namespace`, `--exec-path`, `--config-env` (or their `=`
forms); then require the whole token `commit`. Add `git -C /c/x commit -m y` and `git -c a=b commit`
to AC9 as DENY cases and to the New-arm row. State that the toplevel still comes from the payload
`cwd`, or resolve it from the `-C` target, and say which in S2 and the ceiling.

**Left-shift.** The two DENY literals are the gate. Beyond them, a near-HIT population for the arm:
every `git -C` spelling the charter and the engine print, fed with a sentinel-only card, expecting
exit 2 — the mirror of AC9's must-allow population, over the same two files.

---

### H4 — high — TOOL-1 §2 S2 and S3, §6 AC3; against KICK-1 §2 S3 and S5, KICK-2 §2 S5 — raw 5

**The defect.** S2 compares the card's `tree —` toplevel to the payload cwd's toplevel through
`buildComparablePath`, which closes round 1's B4. S3 names one remedy for every deny, `/session-kickoff`.
But the cell is written ONCE: KICK-1 S3 writes it at SessionStart, S5's `--replay` "prints the stored
card unchanged", KICK-2 S5's `--append` rewrites only the READY sentinel, and KICK-3's Step 5 pipes a
body and never touches the cell. In a linked worktree the payload's toplevel is the worktree itself,
so a session that moves trees — `EnterWorktree`, the charter's own §3 worktree flow, a `--resume`
opened in a sibling checkout — is denied "oriented in A, committing in B" on every later commit for
the rest of its life, and the remedy printed on every one of them cannot change the cell. The design
record's escape for this class was `--waive`, removed by owner decision 2; no spec replaces it, and
the only exits are S6's evasions or a new session.

**Fix.** Have KICK-2's `--append` rewrite the `tree —` cell to the append-time toplevel — the kickoff
ran THERE, which is what the cell asserts — and add a TOOL-1 arm: card written in A, READY appended
from B, payload cwd B, exit 0. Or, if the cell must stay immutable, make the tree-mismatch deny's
stderr name the real remedy (a kickoff run in that tree, which then must update the cell) and extend
AC3 to the re-kickoff case, stating the limit in S6.

**Left-shift.** The cross-kit arm AC10 already runs the writer's bytes; give it a second leg that
appends from a sibling worktree of the fixture and feeds the result, so the one mechanism that can
change the cell is exercised against the one compare that reads it.

---

### M1 — medium — TOOL-1 §6 AC10 and §2 S7 second class arm, status header order 3; against KICK-2 order 3 — raw 6, 30

**The defect.** The rev-2 cross-kit arm "appends a real READY line through `--card --append`", a verb
`KICK-aReplayedCard-2` builds in the SAME parallel step: both carry order 3 and the README's build-order
table renders them as one step, parallel. BUILD-METHOD M6 `parallel-when-disjoint` clause 2 forbids
exactly this — "neither writes a file the other reads … as an acceptance input" — so AC10 cannot be
observed in-step, which is the M5 class round 1 raised and the B4 fold re-opened here. Moving TOOL-1 to
order 4 is not free: TOOL-1 and TOOL-2 both list `tools/hooks/README.md` under Files touched. Raw 30's
adopter half — that the self-test reds in a hooks-kit-only tree — is wrong and dropped:
`tools/hooks/kit.toml` holds `scratch-guard.test.sh` as `project-owned`, withheld from adopters.

**Fix.** Drop the `--card --append` dependency from AC10: the arm runs the writer's `--card --write`,
then replaces only the `READY — none yet` line with a real READY line via the test's own `sed`,
leaving the `tree —` bytes untouched — the spelling fold is what the arm guards, and the READY line is
not that spelling. Keep the `consumes-from KICK-aReplayedCard-2` edge for the shipped behaviour.

**Left-shift.** `gen_build_index.py` renders the order table from the specs; a `consumes-from` edge
to a unit that shares the order value is a join it can red on, and this is its second instance in one
build.

---

### M2 — medium — KICK-3 status header order 5 and README build-order step 5; against TOOL-3 §3 Edges and §6 AC2 — raw 35

**The defect.** The M5 fold moved KICK-3 and TOOL-3 to order 5 together. TOOL-3 declares
`consumes-from KICK-aReplayedCard-3 — Step 5b's append`, and its AC2 requires the clone's card to end
with a READY line, which only KICK-3's engine change produces. `render_order` in `gen_build_index.py`
(line 993) derives `Parallel: yes` from the order value alone, so the table asserts a parallelism M6
clause 2 forbids — the same class the fold moved them to order 5 to escape.

**Fix.** TOOL-3 to order 6; KICK-3 keeps 5. Or mark TOOL-3 AC2 as observed at the build's close.

**Left-shift.** The same `gen_build_index.py` join as M1.

---

### M3 — medium — KICK-3 §2 S2 and §4 Data model; against KICK-2 §4 — raw 8

**The defect.** S2 enumerates what Step 5 pipes: the READY line, the manifest delta line, the gotcha
class names, the binding record ids, the open items. §4 says the body "is the shape
`KICK-aReplayedCard-2` §4 declares", and that shape has seven parts: `## task`, `## manifest`,
`## read`, `## records`, `## classes`, `## open`, READY. S2 omits `## task` (the sealed skeleton
fields) and `## read` (the up-to-12 `path:lo-hi — why` rows) — the scope and the entrypoints, the
path-bearing content KICK-2's citation check exists to grade and the orientation the build exists to
replay. Two answers to what the body is; AC2 checks only the READY line and `--card --check`, so a
card built from S2's list passes with no scope on it.

**Fix.** Rewrite S2 to say Step 5 pipes the six sections of KICK-2 §4 plus the READY line, naming
`## task` and `## read`, or state in §3 that those two are not appended and why.

**Left-shift.** An arm on `--card --check` that reds when a card carries a READY line and no
`## task` section — the shape that says a kickoff ran and left no scope on disk.

---

### M4 — medium — KICK-3 §2 S1 and §6 AC1 — raw 9

**The defect.** Today's Step 1 batch (`SKILL.md:49`) derives the current branch first. S1 splits the
batch into what the card satisfies (node tag, tree kind, worktree count, recent subjects) and what
still runs (`rev-parse HEAD`, `status --short`, the ff), and the branch is in neither. `status --short`
prints no branch; the ff condition and the branch-convention STOP both need it; the only in-context
source is the card's `tree —` cell written at session start, which the spec's own non-goal recognises
as stale for BASE by the same mechanism. AC1 asserts BASE only, so a stale-branch READY line and STOP
test are unobserved.

**Fix.** Add `git branch --show-current` to S1's still-run list and to AC1's expected batch; say the
card's branch is never consumed.

**Left-shift.** AC1's arm asserts the READY line's branch equals `git branch --show-current` at
kickoff, in a fixture that checked out a new branch after the card was written.

---

### M5 — medium — KICK-3 §2 S3, §3 non-goals, §4 Files touched, §6 AC5; prior art `memory/builds/aRatchetForge/spec/manifest-ratchet-spec.md:213-226` — raw 10, 73

**The defect.** S3 orders the repair commit "AFTER Step 5's append and never before it"; S2 has Step
5 "stop exactly as today". Whether the commit lands inside Step 5 after the append and before the
halt, or only after the user's go, is unstated, and two engine texts satisfy AC5's first clause with
different behaviour — in the attended path a staged repair can sit uncommitted through the user's
adjust or abort while the READY card's delta line names a commit that does not exist. §3 still reads
"No change to … Steps 2 through 4" while S3 and Files touched edit Step 2b, which sits inside that
range. And the ratchet record's "repair NOW as part of kickoff … in the repair commit message AND the
READY card" is reordered without naming the record amended (§6: supersede with a new id and a note).
AC5's second clause is the vacuous fenced-commands test H2 covers.

**Fix.** State the moment: the repair commit is made inside Step 5 between the append and the halt,
and in 5b before continuing. Strike Step 2b from §3's list. Cite the manifest-ratchet spec §4 as the
text amended. Replace AC5's second clause per H2.

**Left-shift.** `check-spec-tokens.py` already joins Files touched against the tree; a rule that a
§3 "No change to <X>" sentence naming a step the Files touched row also names is a contradiction it
can print.

---

### M6 — medium — TOOL-2 §6 AC3; against §2 S3, S4 and `tools/settings-merge.py` `merge()` — raw 13, 27, 52, 66

**The defect.** AC3 expects the four new fragments to yield "four SessionStart groups of one entry
each", byte-identical in file order, reverse order and again. S4 gives `check-wiring.fragment.json`
and `procmon-session.fragment.json` the SAME matcher `startup|resume|clear`. `merge()` at
`settings-merge.py:210` locates a group by matcher equality and at `:233` appends a second entry into
it rather than creating a second group, so a correct merger yields THREE groups (`startup|clear` ×1,
`resume|compact` ×1, `startup|resume|clear` ×2), and reversed application reverses the two entries
in the shared group, so the three results are not byte-identical either. AC4's "exactly one carries
`compact`" is consistent with three groups, so the two criteria disagree. S3's own re-match text
("moves to the fragment's group") relies on one-group-per-matcher, which is also what the existing
agent-cap `Workflow|Agent` wiring depends on; a builder who makes AC3 pass as written restructures
the merger against the spec's own text, which is why raw 66 is lowered from high.

**Fix.** Rewrite AC3: three SessionStart groups, the shared matcher holding both re-matched entries
and the other two one each, no empty group; assert entry SET equality within a group across the three
orders, or have the merger order entries by command before writing and keep byte-identity. Say in S3
that fragments sharing a matcher share a group.

**Left-shift.** The idempotence arm as rewritten is the gate; add a fixture pair sharing a matcher so
the arm exercises the shared-group case rather than only the disjoint one.

---

### M7 — medium — TOOL-2 §6 AC8 — raw 14

**The defect.** AC8 observes "`govkit apply --dry-run` against a scratch target". `tools/govkit/govkit.py`
contains no `dry` string (grep count 0); its `USAGE` names `plan` as the read-only verb and `apply`
takes `--target`, `--kits|--all` and `--resume` only. The shipping half of AC8 exits with a usage
error as written.

**Fix.** "`python tools/govkit/govkit.py plan --target <scratch> --kits kickoff-manifest,check-wiring,process-monitor`
lists all four fragments among the files it would write."

**Left-shift.** A spec-lint arm: every fenced or backticked `govkit.py <verb>` in a spec resolves to a
verb in `USAGE`. The verb table is one grep away and the class recurs.

---

### M8 — medium — KICK-3 §6 AC1 and AC2, §4 Migration; TOOL-3 §6 AC2 — raw 50

**The defect.** Verified on this node: `%USERPROFILE%\.claude\skills\session-kickoff` is a Junction
whose target is `C:\projects\coding-governance\skills\session-kickoff`, the PRIMARY tree, on `main` at
`c4f02308`. `/session-kickoff` in any session therefore loads the primary's unedited `SKILL.md`, not
this branch's. KICK-3 AC1/AC2 and TOOL-3 AC2 all name `/session-kickoff` as the observed act and their
fixtures say nothing about the installed engine. On the old engine Step 1 runs the whole batch and
Step 5/5b never appends, so the criteria RED (not green, as raw 50 first said) until the landing merge
fast-forwards the primary — a circular DoD in an unattended run whose only escape is re-pointing a
machine-global junction fourteen worktrees share. KICK-3 §4 Migration mentions the junction as an
adopter concern; no fixture addresses it.

**Fix.** State that AC1/AC2 (and TOOL-3 AC2) are observed at the build's close on the primary after
the merge; or that the fixture session re-points the junction to the worktree copy for the run and
restores it, recorded in the ledger with the session id.

**Left-shift.** `check-wiring.sh --session` already reports tracked-versus-installed mismatch; have
the acceptance ledger row for a `/session-kickoff` observation carry that line, so a row observed on
the wrong engine names it.

---

### M9 — medium — KICK-1 §4 Files touched and Migration, §5 migration — raw 69

**The defect.** Prior art, skeptic-verified: every audit-block key addition rode a manifest FORMAT
bump with a template edit — `check-script:` at v1.1 (`59f57aed`, aRatchetForge) and
`last-body-change:` at v1.3 (cKeyedLaunchpad-3/4) — carried by `MANIFEST-TEMPLATE.md:4-10`,
`KIT_MANIFEST_VERSION`, WIRE-INTO-PROJECT.md §4 retrofit step 6, and `check-kit-versions.sh:54-59`,
which pins the template marker to the kit version. The self-test's seed arm
(`manifest-check.test.sh:615-617`) exists because "the template an adopter instantiates must carry the
same region the checker enforces". KICK-1 adds `registry:` to this repo's manifest and the runbook
only. A fresh adopter instantiates a seed without the key and every card it writes reads
`node — UNKNOWN: no registry` for life, with no version WARN because the marker did not move — the
multi-carrier miss the auto-memory note "stamps are not one stamp" records.

**Fix.** `registry: {{REGISTRY_PATH}}` in the seed's audit block (C1 forces the fill), bump
`KIT_MANIFEST_VERSION` and the template's `kickoff-manifest:` marker together, extend WIRE §4's
retrofit list with the key, and list the template and the version bump in Files touched.

**Left-shift.** The seed arm already compares region shape; extend it to assert every key the card
verb READS is present in the seed, derived from the verb's own key list.

---

### M10 — medium — TOOL-2 §2 S4 and S7, §9, §10 — raw 71

**The defect.** aReapedSpinner's closing-diff round 2 R8
(`memory/builds/aReapedSpinner/reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round2.md:236-248`,
confirmed MEDIUM) asked for a second `SessionStart` fragment for procmon, the
`adopt-process-monitor.sh:203` remediation naming both fragments, and a per-event wiring count. The
fold commit left `tools/process-monitor/kit.toml` with one fragment and no backlog row carries R8
(grep over `memory/backlog/TOOL.md`: 0). S4 ships exactly that fragment without citing R8; the adopter's
remedy line still names one fragment and is not in Files touched; and the `process-monitor wiring` leg
the unit lists in §7 (`adopt-process-monitor.sh:192-204`, `grep -c procmon-hook` ≥ 1) cannot see a
missing event or matcher, so it observes nothing about the state S4 exists to fix.

**Fix.** Cite R8 in §9 and §10. Add the `adopt-process-monitor.sh` remediation line and a per-event
count to Files touched, or file the residue as a TOOL backlog row and say so.

**Left-shift.** R8's own left-shift: make the wiring leg decide per event, `hook entries 2/2` with the
missing event named.

---

### M11 — medium — TOOL-2 §2 S5, §6 AC5 and AC6 — raw 72

**The defect.** S5 says the destinations leg "finds the descriptor whose `home` is the fragment's
directory" for a `{here}` fragment. Ten flat descriptors under `tools/govkit/entries/` declare
`home = "tools"` (check-wiring, settings-merge, push-main, check-install-prefix, …), so for
`tools/check-wiring.fragment.json` that rule is not a function and the flat-kit adopter compare is
undecidable for one of the four fragments the unit introduces. Secondary: `check-wiring.sh` already
holds TWO inline `{kit}` resolvers (`:403` scratch arm, `:466` recall arm), each commenting "the one
place the value is read"; a `card` arm on the recall pattern adds a third, and a parity arm that
re-derives the resolution beside the arms rather than through them agrees with itself, not with the
arm that decides UNWIRED — the `second-implementation-is-not-a-second-opinion` class in
`memory/gotchas`.

**Fix.** State the rule as "the fragment's directory is the home of at least one `kind = flat`
descriptor" and compare `{prefix}/<basename>` against the WHOLE declared destination set. Extract one
`resolve_fragment_hook` helper in `check-wiring.sh` shared by the scratch, recall and card arms plus a
`--resolve-fragment <path>` print verb (and its twin on `settings-merge.py`), have the parity arm call
those, and list the helper in Inventory.

**Left-shift.** The parity arm through the print verbs IS the gate once it reads the arm's own value.

---

### M12 — medium — TOOL-1 §4 Data model step 5, §2 S4, §6 AC4 and AC8 — raw 36

**The defect.** Step 5 spawns `git ls-files --others --exclude-standard -- '*/builds/*/README.md'`.
Reproduced in a scratch repository: that pathspec lists `memory/builds/y/README.md` and misses a
top-level `builds/x/README.md`; run from a subdirectory cwd it lists nothing. S4's rule is "a
`README.md` under a `builds/` segment"; AC4/AC8 say only "under a `builds/` folder of the fixture"
and leave the spawn's cwd unstated. The untracked arm — the fold's fix for round 1's H8 — can pass or
red for a reason unrelated to the exemption.

**Fix.** Spell the rule once and derive the spawn from it: pathspec `'*builds/*/README.md'` (verified
to list both) or a JS filter on a `builds/` path segment; git spawned at the resolved toplevel; the
fixture path pinned in AC4/AC8.

**Left-shift.** AC8's arm with the README at BOTH `builds/x/` and `memory/builds/y/`, and the payload
issued from a subdirectory cwd.

---

### L1 — low — KICK-3 §2 S4 — raw 18

S4 (Step 5b appends the body plus the build slug and run-state path) says "Observed by AC2", but AC2
observes "that kickoff" from AC1, an attended session that stops at Step 5; 5b is the unattended
hand-back it never reaches. The only observation of the 5b append is TOOL-3 AC2. A scope item joined
to a criterion that does not read it, the SCOPE_JOIN class check 12 grades as a join. **Fix:** point
S4 at `TOOL-aReplayedCard-3` AC2 or mark it NOT OBSERVED here with that reason. **Left-shift:** none
beyond check 12; the join is machine-graded and the content is a read.

### L2 — low — KICK-1 §3 Edges consumes-from TOOL-4, §4 Alternatives first paragraph — raw 20

Both say "5 B of headroom at base". Measured:
`git show c4f02308:memory/guides/SESSION-KICKOFF.md | tr -d '\r' | wc -c` = 25597 against
`MAX_MANIFEST_BYTES=25600` (`manifest-check.sh:169`), so 3 B. The conclusion (the key does not fit
before TOOL-4 evicts) holds; the number does not. **Fix:** write 3 B, or "under the key's length,
measured at base". **Left-shift:** the §7 rule against a count in prose beside its source; the number
should be the gate's, not the spec's.

### L3 — low — TOOL-1 §4 Files touched, §5 testing; §7 New-arm rows — raw 37

§4 and §5 say twelve arms; §7 lists eleven New-arm rows (AC12's non-commit `ls` payload has none).
The shrink-only floor moves by whichever number the builder believes. **Fix:** drop the number or add
the twelfth row. **Left-shift:** `check-spec-tokens.py` can count New-arm rows against a `<n> arms`
phrase in the same spec.

### L4 — low — TOOL-1 §2 S5, §4 Data model step 3 — raw 54

`scratch-guard.js` reads no `tool_use_id` (grep: 0 hits; `agent-cap.js` reads it six times, for slot
idempotence). S5 and step 3 fail open SILENTLY when it is absent and claim this mirrors "the hook's
existing posture", which it does not: the file's fail-opens are on unparseable stdin, unknown tool and
missing command (`:372-376`). A silent skip on a field the predicate never reads is the green-by-absence
class §7 names, and AC7 arms only the `session_id` case. **Fix:** fail open on `session_id` and `cwd`
only; drop `tool_use_id` from S5, step 3 and AC7. **Left-shift:** an arm that feeds a payload with no
`tool_use_id` and a sentinel card, expecting exit 2.

### L5 — low — TOOL-2 §2 S7, §6 AC8 — raw 75

`tools/govkit/entries/check-wiring.kit.toml:10-14` declares both `to = "{prefix}/{relpath}"` and
`claims`; `govkit.py:1139-1175` rule 4b reds when a rule's resolved destination is not among its own
claims. S7's "adds `check-wiring.fragment.json` to its include list" omits the `claims` half, so the
prescribed edit reds the `govkit selfcheck` AC8 requires green. **Fix:** name
`tools/check-wiring.fragment.json` in that rule's `claims` beside the include. **Left-shift:** rule 4b
is the gate; the spec should say it will fire.

### L6 — low — TOOL-2 §2 S8, §4 Files touched — raw 76

`WIRE-INTO-PROJECT.md:610-612` reads "`settings-merge.py` handles only the agent-cap block — add
SessionStart by hand". S8 "gains one step" and Files touched lists "one step", leaving that
instruction standing beside a fragment step that contradicts it; an adopter following the older line
lands a matcher-less entry that fires at `compact`, the state S4 exists to end. **Fix:** S8 states
that lines 610-612 are REPLACED by the fragment step. **Left-shift:** `check-placeholders.sh`'s
population includes the runbook; a phrase-level assertion that "add SessionStart by hand" is absent
once the fragment ships is one grep.

---

## The cross-read on the four M2 axes

Where two specs disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-2 S1's markers versus `check-wiring.sh`'s whitespace-stripped view and
  `grep -F "$1"` (H1). TOOL-2 §5's quoted tokens versus `merge():228`'s substring dedup (H1). KICK-3
  S2's five items versus KICK-2 §4's seven parts (M3). TOOL-1 S2's compare versus KICK-1 S3/S5 and
  KICK-2 S5, none of which rewrites the cell (H4). TOOL-1 S1's grammar versus the charter's §2 and §11
  and the engine's Step 0 (H3). TOOL-2 AC3's group shape versus `merge()`'s grouping (M6). TOOL-2 S5's
  home rule versus ten descriptors sharing one home (M11).
- **Ordering.** TOOL-1's Rollout versus KICK-1's in-repo ACs at order 2 (B1). TOOL-1 AC10 versus
  KICK-2's verb at the same order 3 (M1). KICK-3 and TOOL-3 at order 5 with a consumes-from edge
  between them (M2). KICK-3 S3's repair commit versus Step 5's halt (M5). KICK-3 AC1/AC2 and TOOL-3
  AC2 versus the junction that serves the primary's engine (M8).
- **Scope.** KICK-3 §3 "no change to Steps 2 through 4" versus Files touched's Step 2b (M5). KICK-1's
  Files touched versus the seed template, the version constant and the retrofit list (M9). TOOL-2 S4
  versus R8 and the adopter's remedy line (M10). TOOL-2 S7's include versus the descriptor's `claims`
  (L5). TOOL-2 S8 versus the runbook line it leaves standing (L6). TOOL-1's fail-open on a field it
  never reads (L4).
- **Acceptance.** TOOL-1 AC9's DERIVED figure over an empty population, and KICK-3 AC5's mirror
  (H2, M5). TOOL-2 AC7 unreachable under S1's markers, and AC1/AC3 unreachable under §5's quoting
  (H1). TOOL-2 AC3's four groups (M6). TOOL-2 AC8's `--dry-run` (M7). KICK-3 S4's join to an AC that
  never reaches 5b (L1). TOOL-1 AC4/AC8's fixture location and cwd unstated (M12). KICK-3 AC1
  asserting BASE but not the branch (M4).

**The unchanged siblings.** `TOOL-aReplayedCard-4` (rev-1) drew no confirmed finding for the second
round. `TOOL-aReplayedCard-5` (rev-2) drew none. `KICK-aReplayedCard-2` (rev-2) drew none on its own
text; two fixes above land on it — H4's `--append` rewrite of the `tree —` cell, and M3's reference to
its §4 shape. `TOOL-aReplayedCard-3` (rev-2) drew one ordering finding (M2) and inherits M8.

**Prior art the fold re-invents or overlooks.** `matchers_of`'s stripped view, in the file the unit
edits (H1). The `check-hook-destinations.sh` refusal on an empty population, beside the arm that needs
it (H2). `MANIFEST-TEMPLATE.md` and `check-kit-versions.sh`'s marker pin, for a key the seed must carry
(M9). aReapedSpinner R8, the record that asked for the fragment S4 ships (M10). The two inline `{kit}`
resolvers already commenting "the one place the value is read" (M11).

**Harness assumptions, and which were verified.** That the hook runs the working tree's
`scratch-guard.js` — `settings.json` names `${CLAUDE_PROJECT_DIR}/tools/hooks/scratch-guard.js`, read
at the synthesis (B1). That the common dir is shared across worktrees — `git rev-parse --git-common-dir`
from this worktree resolves to the primary's `.git`, read (B1). That the installed skill is a junction
to the primary — read with `Get-Item` (M8). That M6 has the run, not a child, commit each pass — read
(B1). PreToolUse ordering and the SessionStart matcher vocabulary are as round 1 left them, not
re-verified here.

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture except three reproductions.** The
  synthesis re-read at source: `tools/check-wiring.sh:150-170`; `tools/settings-merge.py:199-235`;
  `skills/session-kickoff/SKILL.md:33-65,112-125,195-203` and its three fences at `:71,138,176`;
  `tools/govkit/govkit.py:8352-8360,1139-1175`; `tools/govkit/entries/check-wiring.kit.toml`; the ten
  `home = "tools"` descriptors; `WIRE-INTO-PROJECT.md:605-615`; `tools/process-monitor/adopt-process-monitor.sh:190-206`;
  `skills/session-kickoff/MANIFEST-TEMPLATE.md:1-10`; `tools/check-kit-versions.sh:50-62`;
  `skills/session-kickoff/manifest-check.sh:21,169`; `memory/guides/BUILD-METHOD.md:164-209`;
  `tools/memory-tree/gen_build_index.py:993`; `tools/unattended/unattended.sh:1589-1593`;
  `AGENTS.md:155-158`; the build README's roster and order tables; and the three sibling specs'
  §2/§4/§6. It reproduced in a scratch repository: the `'*/builds/*/README.md'` miss and the
  `'*builds/*/README.md'` fix (M12); the marker-with-space miss through `matchers_of`'s own pipeline,
  and the option-parse failure of any dash-leading marker (H1); the manifest byte count at
  `c4f02308` (L2). It measured the junction on this node (M8) and confirmed the real common dir holds
  no `orientation/` today (B1). The `59f57aed` and cKeyedLaunchpad prior-art claims in M9 are the
  skeptic's, reported as such.
- **A spec audit grades what a document says.** B1 was found by reading two specs against each other
  and the build order; H1 by running the reader the spec names over the marker it chose. The defect a
  correct-sounding sentence hides in an unbuilt mechanism is out of reach here, and the four siblings'
  zero is subject to it.
- **The design record was not re-audited.** Owner decisions 1–3 were read for what they say where a
  finding rests on them (B1 on the exemption's purpose, H4 on the removed `--waive`); their reasoning
  was not re-opened.
- **Precision was 0.49, under §8's floor.** Reported rather than smoothed; the correct response is
  the same as round 1's. Round 3 should re-audit the four at their new blobs with one lens on B1's fix
  and the bootstrap it states, one on the two readers of the markers, and one on the build order,
  since three of the twenty-three defects here are the same M6 clause-2 class.
