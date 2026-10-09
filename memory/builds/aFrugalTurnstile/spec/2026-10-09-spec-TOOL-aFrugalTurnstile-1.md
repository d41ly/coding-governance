# TOOL-aFrugalTurnstile-1 — staleness counts first-parent landings, and a runner stamp is trusted only for the runner's own manifest

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base bef97330 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md](../build/2026-10-09-build-TOOL-aFrugalTurnstile-1-1-design.md) | research | TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1-1-spec-brief.md) | journal | TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |
| [2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md](../prompts/2026-10-09-prompt-TOOL-aFrugalTurnstile-1.md) | research | TOOL-aFrugalTurnstile-2 TOOL-aFrugalTurnstile-3 TOOL-aFrugalTurnstile-4 TOOL-aFrugalTurnstile-5 TOOL-aFrugalTurnstile-6 TOOL-aFrugalTurnstile-7 TOOL-aFrugalTurnstile-8 TOOL-aFrugalTurnstile-9 TOOL-aFrugalTurnstile-10 PLAY-aFrugalTurnstile-1 DEPL-aFrugalTurnstile-1 |

<!-- /gen:spec-records -->

## 1. Goal

Two defects make every multi-commit landing pay a full bar at the push boundary. Predicate 3 of
`check_green_record` in `.githooks/pre-push` counts every commit between the recorded green and the
tip, so a green earned on a branch tip falls past the bound of 10 as soon as the default branch has
taken other builds' landings while that branch was open: each landing adds every commit it carried,
not one. And the runner's `gate-full-green` stamp does not say which leg manifest it
ran, so a nested runner inside an adopter's wrapper bar stamps a green of gov's SUBSET that only an
accidental blob mismatch keeps the boundary from trusting as the whole bar. This unit implements
design D1 and D2: the lag is counted in first-parent landings, the stamp names its manifest, and the
boundary trusts a runner stamp only when the push's bar is the runner reading that same manifest.

## 2. Scope (IN)

- **S1 — predicate 3 counts first-parent landings (design D1).** At base `.githooks/pre-push:1194`
  reads `lag=$(git rev-list --count "$r_sha..$main_local" …)`. It becomes
  `git rev-list --first-parent --count "$r_sha..$main_local"`, keeping the `|| echo 0` tail and
  the bound `GATE_FULL_MAX_LAG=10` unchanged. The force message at 1196 becomes
  `the recorded $label is $lag first-parent landings behind the tip (bound $GATE_FULL_MAX_LAG)`.
  Observed by AC1 and AC2.
- **S2 — the two scoped decision lines name the unit.** At 1457 and 1466 the clause
  `is ${lag:-0} commit(s) back, within $GATE_FULL_MAX_LAG` becomes
  `is ${lag:-0} first-parent landing(s) back, within $GATE_FULL_MAX_LAG`. Every other byte of both
  lines is unchanged. Observed by AC1 and AC8.
- **S3 — the runner stamps name their manifest (design D2).** In `tools/run-gates/run-gates.sh` the
  `gate-full-green` block (3885-3895) and the `gate-inherited-green` block (3931-3940) each gain
  one line after `manifest_blob`: `manifest<TAB><path>`. The path is `LEGS_FILE` made
  repo-relative: a leading `./` is stripped, so a root install records `gate-legs.json` and not
  `./gate-legs.json`; an absolute value under the work tree loses the top-level prefix; and an
  absolute value git cannot place inside the work tree stays absolute. The run header's existing
  `manifest` key (2230) is not changed. Observed by AC6 and AC7.
- **S4 — the hook reads the key, and an absent key reads as the kit sibling.** `read_green_file`
  (1140) sets a fifth field, `rec_man`, from the `manifest` key; the inherited-green read
  (1333-1338) sets `ig_man` the same way. `check_green_record` takes it as a new fourth argument,
  `sha · fingerprint · manifest blob · manifest path · selftests · label`, and both call sites pass
  it. An empty value is read as `${KP}gate-legs.json`, which is what every stamp written before
  this unit ran. Observed by AC5.
- **S5 — predicate 7 refuses a record earned on another manifest.** Before its blob compare,
  predicate 7 forces when the recorded path is not `${KP}gate-legs.json`, with the message
  `the recorded $label was earned on the leg manifest <path>, and the bar this push runs reads
  ${KP}gate-legs.json`. The blob compare that follows is today's, byte for byte. Observed by AC3.
- **S6 — no runner stamp is a candidate for a bar that is not the runner (design D2).** After the
  bar is vetted and `bar_record` is set (1363-1381), and before the decision line, a new block
  forces when `bar_record` is `other`: it sets `force` to
  `the bar this push runs is not this kit's runner, so no runner stamp is a candidate (gate-full-green
  and gate-inherited-green prove the runner's legs, not this bar's)` and clears `inh_sha` and
  `inh_why`. It applies whatever the candidate loop concluded, so the FULL line names this reason
  rather than a candidate's. A `stub` bar keeps today's behaviour, because every decision arm in the
  hook's own suite runs under the declared stub. Observed by AC4.
- **S7 — the hook states what the two rules do not check (charter §7).** The comment block above
  `GATE_FULL_MAX_LAG` gains the sentence in §4 "Header sentences", and the comment above
  predicate 7 gains its own. Observed by AC8.
- **S8 — the two carriers that state the lag in prose follow.** `memory/guides/MERGE-BAR.md:17`
  says "a declared number of commits behind it"; it becomes "a declared number of first-parent
  landings behind it". `tools/run-gates/README.md`'s stamp paragraph (351-354) gains one sentence:
  the stamp records `manifest`, and the pre-push hook trusts it only for a runner bar reading that
  manifest. Observed by AC9.
- **S9 — the suite's two lag arms follow the wording.** `.githooks/pre-push.test.sh` arm 12 (306)
  and arm DOCS AC7 (1526) match `commits behind`; each matches `first-parent landings behind`
  instead. Their fixtures are linear, so the count they build is unchanged. NOT OBSERVED by a
  criterion of this pass beyond AC10's grep, because the suite runs once at the close.

## 3. Non-goals (OUT)

- Changing `GATE_FULL_MAX_LAG` or moving it out of the source.
- Re-keying the inherited-green record beyond the `manifest` key, or changing when it is written.
- The bar-keyed record `gate-bar-green` and the `covered` decision (design D3, D4), which is how a
  wrapper bar such as inCMS's earns a usable green; this unit only stops the boundary trusting the
  nested runner's subset green. See Edges.
- Lineage reuse and a reusing run's stamp (design D5).
- The run header's `manifest` key, and every reader of the run header.
- Any kit-version bump; one bump per touched kit happens after the last unit.

### Edges

- **hands-off** `TOOL-aFrugalTurnstile-2` — the `covered` decision of design D4 tests the same
  candidates this unit filters: it takes S6's rule that a runner stamp is a candidate only for a
  runner bar, and S4's `manifest` field. At base `bar_record` is set after the candidate loop, so
  S6 applies its rule after the bar is vetted; a cover pass that must know the bar before it tests
  a candidate owns any move of that block.
- **hands-off** external — inCMS earning a usable green for its wrapper bar. After this unit its
  push forces FULL with S5's or S6's reason instead of the misleading manifest-blob reason; the
  record that lets it skip a bar is design D3's.

## 4. Design

### Evidence

Read at base `bef97330`; `.githooks/pre-push` and `tools/run-gates/run-gates.sh` are byte-identical
to the design record's base `5a836bf0f` (`git diff --stat` empty), so its line numbers hold.

- Predicate 3 at 1194 counts all commits. `INHERITED_RED_MAX_AGE` is already counted in
  first-parent landings by the runner (`run-gates.sh:3507`, `git rev-list --first-parent`), so the
  two bounds will count in one unit.
- With a green at a branch tip `B` landed as merge `M`, `git rev-list --first-parent --count B..M`
  counts `M` plus the default-branch landings since the branch last took the default branch, while
  the all-commit count adds every commit those landings carried in. The two differ only when the
  default branch took merges while the branch was open (§8 F2). Predicate 5 (1219-1222) already
  requires `M^2` to be an ancestor of the recorded sha, so a green NOT on the landed tip still
  forces there unless the push is doc-only, where the count is the only lag guard.
- `LEGS_FILE` (216) is `${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}`. For a root install,
  `KITREL` is `run-gates`, `dirname` answers `.`, and the value is `./gate-legs.json`, while the
  hook's sibling for an empty `KP` is `gate-legs.json`. Without S3's strip every root-install stamp
  would be refused by S5.
- `bar_record` (1363) is `runner`, `stub` or `other`, set after the candidate loop (1302-1315)
  and the inherited green (1330-1351). The suite's decision arms all run under
  `GOV_GATE_CMD_TEST=1` (`.githooks/pre-push.test.sh:113`), so they are `stub`; arm 25 (418) pushes
  a tracked `other` bar and asserts only that the push is accepted.
- The suite's hand-written stamps (264, 483, 637, 1068, 1463) carry no `manifest` key, so S4's
  default keeps every one of them adopted as before.

### The fixture

One driver script under the session scratch, building its repositories under `$TEMP/aft1` (a git
fixture needs a short path on Windows). It follows the prologue of `.githooks/pre-push.test.sh`
(lines 100-125): a bare `remote.git`, a `work` clone with `core.hooksPath` at a scratch hooks dir,
`GOV_DEFAULT_BRANCH=main`, the run-gates kit copied in at `tools/run-gates/` with
`GOV_KITROOT=tools` in a committed `.githooks/gate-env.sh`, a stub-legged `tools/gate-legs.json`
of two unguarded legs that `exit 0`, and a green stub bar under `GOV_GATE_CMD_TEST=1`. Two hook
copies sit side by side: `pre-push.base`, from `git show bef97330:.githooks/pre-push`, and
`pre-push.new`, the working file. Each case invokes a copy directly, the way arm 9b does:

```bash
bash "$H" origin "$REMOTE" <<<"refs/heads/main $(git rev-parse main) refs/heads/main $R" 2>&1 | grep 'gate on main push'
```

A stamp is written with the suite's `stamp()` shape (264), plus a `manifest` line where a case
needs one. Every case runs `pre-push.base` first and records its line, then `pre-push.new`.

### Header sentences

Above `GATE_FULL_MAX_LAG`:

> WHAT THE FIRST-PARENT COUNT DOES NOT CHECK: how many commits a landing's side branch carried. It
> trusts the recorded sha to speak for them, which predicates 2 and 5 constrain and the count does
> not; under a doc-only push, where predicate 5 is waived, a long doc branch now counts as one landing.

Above predicate 7:

> WHAT THE MANIFEST PATH DOES NOT CHECK: that the recorded path held these bytes when the stamp was
> written. The blob compare below checks that; the path only says which manifest the blob belongs to.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `manifest` | key in `gate-full-green` and `gate-inherited-green` | not a definition; no cell |
| `rec_man` | shell variable in `.githooks/pre-push` | not a definition; no cell |
| `ig_man` | shell variable in `.githooks/pre-push` | not a definition; no cell |

No function is added, so no lexicon cell is consulted.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/README.md`
- `memory/guides/MERGE-BAR.md`

### Rollout

Additive for every stamp on disk: one written before this unit lacks `manifest` and reads as the
kit sibling. A wrapper-bar adopter whose nested runner stamps an out-of-tree manifest keeps paying
a FULL bar, now with a reason that names it. The hook ships verbatim to adopters through the
push-main entry, so the change reaches them on their next `govkit update`.

### Alternatives rejected

- **Hashing the manifest the bar actually ran into `manifest_blob`**, the prompt's literal fix. The
  design record's §2 shows it would make inCMS's nested-runner stamp pass predicate 7, and the
  boundary would scope from a sha where an inCMS leg outside gov's subset was red.
- **Moving the candidate loop below the bar vetting** so S6 can skip it. It reorders the policy
  announcement and the bar refusals, which suite arms read in order, for a saving of one
  fingerprint call on an `other` bar. See §8 F1.
- **A new predicate number for S5 and S6.** The predicates are cited by number in comments, the
  README and the merge-bar guide; S5 is predicate 7's concern from the record's side, and S6 sits
  outside the per-record function because it is a property of the bar.

## 5. Production-readiness checklist

- security — S6 narrows what the boundary trusts; nothing here makes a run smaller. A stamp is
  still a file the bar's own process writes under the git dir, as today.
- perf / scale — `--first-parent` makes the walk shorter or equal. One extra `awk` read per
  candidate.
- error / empty / loading states — an absent `manifest` key reads as the kit sibling; an empty
  `LEGS_FILE` cannot occur, because the runner refuses a missing manifest before any leg runs.
- observability — each new force names its reason on the FULL line, and the scoped lines name the
  count's unit.
- risks — a doc-only landing of a long branch now scopes where it forced; the header sentence says
  so, and the doc class still runs every leg reading a moved doc.
- testing — the scratch fixture of §4, and the arms in §7 that the close runs.
- migration — none; old stamps read as before.
- user docs — `memory/guides/MERGE-BAR.md` and `tools/run-gates/README.md` (S8).

## 6. Acceptance criteria

Every criterion runs the §4 fixture driver; each case's base line is recorded before its new line.

- **AC1** — When a one-commit branch `feat` is cut from `main` and stamped at its tip, `main` then
  takes a `--no-ff` landing of a separate 12-commit branch, and `feat` is merged `--no-ff` on top
  (the §8 F2 shape), the base line reads `FULL gate` with `14 commits behind the tip`, and the new
  line reads `scoped gate` with `2 first-parent landing(s) back`, each observed with
  `bash "$H" origin "$REMOTE" <<<"refs/heads/main <tip> refs/heads/main <R>"`.
  Red when: the new copy still counts all commits and forces FULL.
  figure: 14 and 2 are DERIVED by the fixture's shape, measured by the F2 probe on 2026-10-09.
- **AC2** — When 11 commits land on `main` one by one past a stamp at the old tip, both copies print
  `FULL gate`, and the new line names `11 first-parent landings behind the tip (bound 10)`.
  Red when: the first-parent count lets a linear run past the bound scope.
- **AC3** — When the stamp carries a `manifest` line naming a path outside the kit sibling, the
  untracked elsewhere/legs.json, the base line is `scoped gate` and the new line is `FULL gate`
  naming both that path and `tools/gate-legs.json`. Red when: the new copy ignores the key, or forces without naming the path.
- **AC4** — When the fixture commits a `tracked-bar.sh` declared as `GATE_CMD` in `.unattended.conf`,
  `GOV_GATE_CMD_TEST` is unset, `GOV_GATE_CMD="bash tracked-bar.sh"` is exported, and a stamp at the
  tip is otherwise valid, the base line is `scoped gate` and the new line is `FULL gate` carrying
  `is not this kit's runner`. Red when: a runner stamp scopes a bar that is not the runner.
- **AC5** — When the stamp is the suite's shape with no `manifest` key, at the tip, both copies print
  `scoped gate`. Red when: an old stamp is refused, which would cost every adopter its next push.
- **AC6** — When the fixture's runner copy is run plain over its two unguarded stub legs on a clean
  tree, `awk -F'\t' '$1=="manifest"{print $2}' .git/gate-full-green` prints `tools/gate-legs.json`
  for the nested install, `gate-legs.json` for a second fixture with the kit at the repo root, and
  an absolute path for a run handed an out-of-tree manifest through the runner's manifest override;
  `pre-push.new` then scopes from the first two stamps and forces FULL on the third.
  Red when: the key is missing, keeps a `./` prefix, or records an in-tree path absolutely.
- **AC7** — When `awk '/THE INHERITED-GREEN STAMP/,/inherited-green stamp written/' tools/run-gates/run-gates.sh`
  runs, its output carries the same `manifest` line the full-green block writes.
  Red when: the inherited green is left without the key, so the hook reads it as the kit sibling
  whatever it ran.
- **AC8** — When `grep -nE 'commit\(s\) back|commits behind' .githooks/pre-push` runs it prints
  nothing, and `grep -c 'first-parent landing' .githooks/pre-push` prints at least 3; `grep -n
  'DOES NOT CHECK' .githooks/pre-push` names both S7 sentences.
  Red when: a decision line keeps the old unit, or a header sentence is missing.
- **AC9** — When `grep -n 'first-parent landings behind' memory/guides/MERGE-BAR.md` and
  `grep -n 'manifest' tools/run-gates/README.md` run, each hits the S8 sentence.
  Red when: either carrier still states the lag in commits or omits the key.
- **AC10** — When `grep -n 'commits behind' .githooks/pre-push.test.sh` runs it prints nothing.
  Red when: arm 12 or DOCS AC7 still greps the old wording and would red at the close.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `branch-guard self-test` · `pre-push self-test` · `pre-push run-log line` · `pre-push bar self-test` · `push-main self-test` · `check-wiring self-test` · `settings-merge selftest` · `recall floor` · `recall floor arms` · `run-gates canary` · `run-gates evidence` · `run-gates turnstile` · `run-gates gov canary` · `foreign-prefix parity (every self-test at three prefixes)` · `run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` · `install-prefix self-test` · `dead-path carriers self-test` · `lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` · `spec-tokens self-test` · `kit-placeholders self-test` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

Every leg whose guard a §4 path trips is named, the broad `.githooks/`, `tools/run-gates/` and
`tools/` guards included, as the build's brief asks. All run once, at the close.

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 · a stamped branch landed --no-ff after main took a 12-commit landing · none
New arm: .githooks/pre-push.test.sh · covers AC3 AC4 · a stamp naming a foreign manifest, then a tracked non-runner bar · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC6 · the control run's stamp asserted to carry the sibling manifest path · none

## 8. Open questions

- **F1 — where does S6's rule sit, given that `bar_record` is set after the candidate loop?**
  Options: (a) after the bar is vetted, overriding whatever the loop concluded; (b) move the
  candidate loop and the inherited green below the bar vetting, so the loop is skipped for an
  `other` bar. (b) reorders the policy announcement against the bar refusals, which arms read in
  order, to save one fingerprint call. (a) satisfies AC4 with no reordering. Neither trips an M3
  veto. RESOLVED (agent, 2026-10-09, delegated): (a); a later unit that needs the bar earlier owns
  the move.
- **FACT-QUESTION · F2 — does the brief's fixture (a), a 12-commit branch landed `--no-ff` with the
  green at its tip, observe design D1?** Probe: a scratch repository under `$TEMP`, comparing
  `git rev-list --count B..M` with `git rev-list --first-parent --count B..M`. Observation that
  decides it: whether the two counts differ on that shape. Liveness: the same probe on a second
  shape, where `main` takes a 12-commit `--no-ff` landing while the branch is open, must produce two
  DIFFERENT counts, or the probe cannot tell anything apart. Measured 2026-10-09: the briefed shape
  gives 1 and 1, because every branch commit is reachable from the green at its tip, so the old
  hook does not force there and the case observes nothing; the second shape gives 14 and 2. Design
  D1 stands; only the brief's fixture was wrong. RESOLVED (agent, 2026-10-09, delegated): AC1 uses
  the second shape.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, from the build's spec brief and design D1, D2, read against
  the hook and the runner at base.

## 10. Reuse audit

The seams are the hook's own: `check_green_record` predicates 3 and 7, `read_green_file`, the
inherited-green read and `bar_record`, all in `.githooks/pre-push`; and the two stamp blocks in
`tools/run-gates/run-gates.sh`. The first-parent walk reuses the form the runner's age probe
already uses at `run-gates.sh:3507`. `python tools/codebase-map/reuse_lookup.py "count how far a
recorded full green lags the pushed tip in first-parent landings"` returned name-stem matches only
(`counts`, `records`, `read_landing_commit`), with every layer scanned, so no existing seam fits
beyond those named. Recall ranked this build's own brief and design, `TOOL-dThriftyLanding-13` (the
lag bound kept for doc-only pushes, which the S7 sentence prices) and the dThriftyLanding specs that
added the candidate stamps. Where recall and source disagree: the design record's §5 repeats a
memory note that `reuse_lookup.py` cannot see `.sh`; at base it reports no unscanned layer.

Recall terms used: `python tools/memory-recall/query.py "which records decide how the pre-push full
green staleness bound counts lag and which manifest a runner stamp must name" --terms "pre-push
full green stamp staleness lag GATE_FULL_MAX_LAG first-parent manifest_blob predicate scoped
boundary GOV_GATE_CMD"`
