# TOOL-dDerivedDocket-21 — remote-relative bases and complete leg guards

**Status:** SPECCED · rev-2 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-26 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

Two gate verdicts in this repository depend on something other than the tree being graded. The
`drift-audit records` leg judges ancestry and ratchets against the node's LOCAL default branch, so
the same commit reads differently on a node whose local main is stale: i12 recorded ORPHAN_ID_PIN
reading 0 against a stale local main and 5 against origin, and i152's drift half is the same shape.
And a guarded bar leg whose checker reads a root conf skips on a diff that touches only that conf,
because govkit's guard partition has no class a root file can fall into, so the guard cannot name
it (TOOL-aWalkedCorpus-5). Make drift's comparison base the remote-tracking ref and print it, give
root confs a declared guard class, and gate the class so no bar leg can read a root conf its guard
does not name.

## 2. Scope (IN)

- **S1** `tools/drift-audit/drift_report.py` resolves its comparison base remote-first. `--base-ref`
  stays verbatim. Otherwise the default-branch NAME comes from `GOV_DEFAULT_BRANCH` or from
  `refs/remotes/origin/HEAD` exactly as today, and the BASE is `refs/remotes/origin/<name>` when
  that ref resolves. Observed by AC1 and AC2.
- **S2** The two cases where that ref does not resolve are separated. A clone with no `origin`
  remote compares against `refs/heads/<name>` and says so on stderr; a clone that has `origin` but
  no tracking ref refuses with exit 2 naming `git fetch origin <name>`. The report header prints the
  base ref AND its sha. Observed by AC2.
- **S3** The sweep of `tools/` and `.githooks/` for bare default-branch comparison bases, recorded
  as §4's inventory with a disposition per site: converted, already remote-relative, a NAME rather
  than a base, or waived with the reason. Observed by AC3.
- **S4** govkit selfcheck's guard partition (`tools/govkit/govkit.py:1395`, check 7c) gains a
  sixth class, `root-conf`: a pathspec with no `/` that equals some registry descriptor's
  `[config] file` value. The set is DERIVED from the descriptors already loaded, never listed.
  Observed by AC4.
- **S5** A new govkit selfcheck check beside 7c: every leg in gov's own manifest that carries a
  non-empty guard and is not held — subject `repo` and chunk other than `selftests`, the runner's
  own hold predicate (`tools/run-gates/run-gates.sh:1228`) — and whose tracked argv files name a
  declared root conf, carries that conf in its guard. It reds naming the leg and the conf, and it
  prints how many legs it graded. It also prints, report-only, one near-miss line per guarded bar
  leg whose tracked argv file imports a module beside it by name, or sources a file by a literal
  path, whose bytes name a declared root conf the guard lacks — the residual §3 leaves ungraded.
  Observed by AC5, AC6 and AC9.
- **S6** The four bar legs S5 names at BASE gain their conf, in `tools/gate-legs.json` and in the
  descriptor `[[gate_leg]]` row that declares each: `lexicon naming predicates` gains
  `.lexicon.conf`, `codebase-map gate coverage` gains `.codebase-map.conf`, and
  `kit/dogfood doc parity` and `review-protocol parity (kit vs dogfood)` gain `.memory-tree.conf`;
  and `recall floor`, a gov-only row no descriptor declares, gains `.memory-tree.conf` by hand: its
  argv file reads `RECALL_FLOOR` through `recall_conf.CONF_NAME`
  (`tools/memory-recall/recall_conf.py:41`), a transitive read S5 does not grade, and it is the leg
  TOOL-aWalkedCorpus-5 was filed on. Observed by AC6 and AC9.
- **S7** The two comments that record the guard as impossible — `tools/lexicon/kit.toml:97` and
  the B1 block at `tools/lexicon/adopt-lexicon.sh:459` — are rewritten to name the new class. The
  `lexicon wiring` grade stays: it is unguarded, so it still grades the declaration if a guard is
  ever narrowed again. Observed by AC7.
- **S8** Under the build's one-owner rule this unit moves, once, the version of each kit whose move
  it is the earliest to scope: drift-audit, govkit, lexicon and codebase-map. Memory-tree's move is
  the memory-tree docs unit's under `check-verdict-epoch.sh`'s topological rule, and the review
  harness's is the review-durability unit's; the bytes S6 changes in those two kits ride those moves.
  Observed by AC8.

## 3. Non-goals (OUT)

- **Attributing a red leg** to this run or to another build. That is the red-attribution unit's;
  this unit only removes one environmental input from two verdicts it re-runs.
- **Held legs.** A `subject = kit` or `selftests` leg runs only when `GATE_SELFTESTS=1` asks for
  it, and the Definition-of-Done form of that run also sets `GATE_FULL=1`, which bypasses every
  guard. Grading their guards would reach seventeen held legs whose argv files name a root conf,
  measured at BASE, and whether each one reads the real conf or writes a fixture copy was not
  measured (UNVERIFIED). The residual is stated: a scoped run with `GATE_SELFTESTS=1` alone still
  guard-skips a held leg on a conf-only diff.
- **Transitive reads.** A conf read through a sourced library, a Python import or a name composed at
  runtime is not seen by S5. Its header says so. S5 prints such legs as near-misses so the residual
  is visible; it never reds on one.
- **Comparing a kit descriptor's guard with gov's manifest row.** TOOL-aPacedTurnstile-12 records
  that nothing compares the two. S6 edits both by hand for its four legs; the parity gate is that
  row's work.
- **The pre-push hook, the lander and `run-gates.sh`.** None needs a change: the runner and the
  lander already compare against `origin/<name>`, and the hook uses the name only to classify the
  pushed ref (§4). The hook also ships verbatim to adopters.
- **The attended profile wall and any run-gates behaviour.** Guards scope a run; nothing here moves
  a verdict of a leg that runs.

### Edges

- **hands-off** `TOOL-dDerivedDocket-23` — a drift verdict that does not depend on the node's local
  main, without which a stale-local-main red is red at both L and R and the re-run at R reads it
  INHERITED, blaming an owner who does not exist.

## 4. Design

### Data model

```
# drift-report at <head8> (base refs/remotes/origin/<name> @ <sha8>) · kit <v>
drift-report: this clone has no origin remote, so the base is local <name> @ <sha8>      (stderr)
drift-report: origin has no tracking ref for '<name>'; run `git fetch origin <name>`     (exit 2)

govkit selfcheck: guarded bar legs graded <n> · root-conf readers <m>
govkit selfcheck: leg '<name>' reads root conf <conf> (argv file <path>) and its guard does not name it
govkit selfcheck: near-miss: leg '<name>' may read root conf <conf> through <path> (not graded)
```

The `--json` shape is unchanged: the base is a header fact, not a signal.

### The base ladder

1. `--base-ref <ref>`, verbatim. An explicit ref is the escape hatch for every case below.
2. NAME := `GOV_DEFAULT_BRANCH`, else the last component of `refs/remotes/origin/HEAD`, else refuse
   exactly as today (`tools/drift-audit/drift_report.py:1869`).
3. BASE := `refs/remotes/origin/<NAME>` when `git rev-parse --verify --quiet` resolves it.
4. Else, when `git remote get-url origin` fails, BASE := `refs/heads/<NAME>`, announced. There is
   no staler or fresher copy in a clone with no remote, so local IS the record. The drift-audit
   selftest's fixtures take this rung and need no edit (`tools/drift-audit/selftest.py` sets
   `GOV_DEFAULT_BRANCH=main` in repos with no remote).
5. Else refuse, exit 2. A clone that has `origin` and has not fetched the branch cannot say what
   landed, and falling back to local is the defect this unit removes.

### Inventory — the sweep at BASE

Command, re-run at build time:

```bash
git grep -nE 'symbolic-ref|GOV_DEFAULT_BRANCH|origin/\$|DEFBR' -- tools .githooks ':!*.test.sh' ':!*selftest.py' ':!*.md' \
  | grep -vE '^[^:]+:[0-9]+:[[:space:]]*#'
```

Comment-only lines are dropped: a comment names a branch, it never compares against one. A hit
matches a row by FILE; each row records its file's hit count at BASE, so a new site in a listed file
raises the count.

| Site | Hits at BASE | What the name feeds | Disposition |
|---|---|---|---|
| `tools/drift-audit/drift_report.py` | 3 (`:1858`, `:1865`, `:1870`) | the NAME derivation, then ancestry, `git show <base>:<path>` and the trace walk | CONVERT (S1, S2): the name derivation stays exactly as today; the BASE becomes `refs/remotes/origin/<name>` |
| `tools/memory-tree/check-verdict-epoch.sh` | 3 (`:76`, `:77`, `:84`) | `merge-base` with `origin/<def>`, then local `<def>` | WAIVE: already remote-first; the local rung fires only when no tracking ref resolves, and a too-early base only widens the scan |
| `tools/run-gates/run-gates.sh` | 4 (`:121`, `:140`, `:1298`, `:1462`) | the name, the scoped-run base `origin/<def>`, and two printed labels | already remote-relative |
| `tools/push-main.sh` | 4 (`:20`, `:23`, `:24`, `:63`) | the pushed branch and `$remote/$def`, two refusal messages, the current branch's name | already remote-relative; the local push is the in-place landing unit's |
| `.githooks/pre-push` | 7 (`:91`–`:107`) | which pushed ref is the default branch, and a tracking-ref existence check | a NAME, not a base |
| `.githooks/pre-commit` | 3 (`:25`–`:27`) | the primary-tree branch guard | a NAME, not a base |
| `tools/unattended/unattended.sh` | 5 (`:777`, `:779`, `:795`, `:796`, `:1088`) | `check_branch` and `default_branch`, validated against the remote's advertisement | a NAME, not a base |
| `tools/playbook/render_playbook.py` | 1 (`:111`) | a value rendered into the charter | a NAME, not a base |

Total at BASE: 30 hits in 8 files, PINNED as that measurement.

### The `root-conf` class

The class's population is the set of `[config] file` values over every descriptor selfcheck has
already loaded, minus empties and anything carrying a `/`; a guard is `root-conf` when it is a member
of that set. The existing five classes are prefix tests
and a root file name matches none of them, so the partition stays exact: every pathspec still falls
into exactly one class. A root file that no descriptor declares, such as `.nosuch.conf`, still falls
into none and still reds 7c.

The emitter needs no change. It already renders a guard through `resolve_tokens` and keeps it only
when it matches a tracked path in the target (`tools/govkit/govkit.py:5042-5051`), so an adopter
that has adopted the kit receives the conf in the guard and one that has not drops it.

### The completeness check

For each manifest row with a non-empty `guard`, `subject` other than `kit` and `chunk` other than
`selftests`: read every argv element that `git ls-files` tracks, and for each declared root conf
whose file name occurs in those bytes, require it in the guard. A mention in a comment counts;
that direction costs one re-run on a conf-only diff and never hides a red. Measured at BASE with a
read-only probe over the real manifest: seven guarded bar legs, four of which name a root conf, and
all four lack it — the four S6 lists.

LIVENESS: zero guarded bar legs graded is a refusal naming the manifest, because it reads exactly
like a corpus with nothing to fix.

### Files touched (estimate)

`tools/drift-audit/drift_report.py` · `tools/drift-audit/selftest.py` · `tools/drift-audit/README.md`
· `tools/govkit/govkit.py` · `tools/govkit/selftest.py` · `tools/gate-legs.json` ·
`tools/lexicon/kit.toml` · `tools/lexicon/adopt-lexicon.sh` · `tools/codebase-map/kit.toml` ·
`tools/memory-tree/kit.toml` · `tools/workflows/kit.toml` · the drift-audit and govkit dossiers.

### Alternatives rejected

- **A held canary arm requiring an UNGUARDED reader of each conf in the same kit** (the lexicon B1
  shape, generalised). Rejected by running its predicate over the real manifest: it leaves
  `review-protocol parity (kit vs dogfood)` with no same-kit reader of `.memory-tree.conf`, because
  that conf belongs to another kit, so it reds on landing for a leg it cannot fix without changing
  the rule.
- **The same arm with ANY unguarded reader.** Rejected by the same probe: `drift-audit records`
  names `.lexicon.conf`, so giving `lexicon wiring` a guard — the break the arm exists for — still
  passes. An arm that cannot fail on its own staged break is not an arm.
- **Retiring the guards half as already done by the lexicon B1 fix.** B1 closes one instance for
  one kit; the probe found three more guarded bar legs with the same gap.
- **Drift keeping a bare name and fetching first.** A report that fetches is a network call on a
  leg that must run offline, and it still grades a ref the run could move.

## 5. Production-readiness checklist

- security — no new input surface. The base ladder reads refs and a remote URL that git already
  resolves; the completeness check reads tracked files govkit selfcheck already reads.
- perf / scale — one `git remote get-url` and one `rev-parse` per drift run; the completeness check
  reads each guarded bar leg's argv files once, seven of them at BASE.
- error / empty / loading states — an unfetched tracking ref refuses with exit 2 and names the
  fetch; a remote-less clone proceeds and announces; zero guarded bar legs refuses as a dead probe.
- observability — the header's base ref and sha on every drift run; the graded and reader counts on
  every selfcheck.
- risks — a CI checkout that fetches branches without `refs/remotes/origin/HEAD` still needs
  `GOV_DEFAULT_BRANCH`, as today. The concurrent adopter-wiring session is editing govkit's
  attribute emission; S4 and S5 sit in selfcheck, a different region, and landing reconciles.
- testing — arms in `tools/drift-audit/selftest.py` for the ladder and in `tools/govkit/selftest.py`
  for the class and the completeness check, each break staged and observed red.
- migration — none for gov beyond S6. An adopter's descriptor rows gain the conf at their next
  `govkit apply`, dropped where the target does not track it.
- user docs — `tools/drift-audit/README.md` states the base ladder; the drift-audit and govkit
  dossiers' prose is refreshed on touch.

## 6. Acceptance criteria

- **AC1** — When `tools/drift-audit/selftest.py` runs its new arm over a scratch repo with a bare
  remote whose origin tip raised a pin in the project layer, `drift_report.py --json` reports the
  same signal values with local main behind that raise, equal to origin, and ahead by an unrelated
  local commit.
  Red when: the base is the bare name, so the behind case reports the raised pin as a weakened
  ratchet the other two do not.
  permission: the drift-audit selftest is a held kit leg; it runs at the build's one post-build bar
  with `GATE_SELFTESTS=1`.
- **AC2** — When the same arm runs with `origin` configured and no tracking ref, the report exits 2
  naming `git fetch origin`; with no `origin` remote it names the local base on stderr and exits as
  the signals decide; and every header it prints carries the base ref, `@` and an eight-hex sha, the
  ref reading `refs/remotes/origin/<name>` whenever that ref resolves.
  Red when: the unfetched case falls back to `refs/heads/<name>` silently.
- **AC3** — When §4's `git grep` sweep command, comment filter included, is re-run at the build
  commit, every file it hits is a row of §4's inventory, and each file's hit count equals the count
  its row records, except where the row's disposition names the change.
  Red when: a comparison site is added between BASE and the build without a disposition — in a new
  file, or inside a listed one, whose count then rises.
- **AC4** — When `tools/govkit/selftest.py` feeds 7c a manifest whose guard names `.lexicon.conf`,
  the pathspec falls into exactly one class; a guard naming `.nosuch.conf` still reds.
  Red when: `root-conf` admits any file without a `/`, so an undeclared root file passes.
- **AC5** — When the completeness check grades a fixture manifest whose guarded, repo-subject leg's
  argv file names `.lexicon.conf` and whose guard lacks it, the fixture's
  `python tools/govkit/govkit.py selfcheck` reds naming the leg and the conf; with the conf added it
  passes; with the leg moved to chunk `selftests` it is not graded.
  Red when: the check reads the guard alone and never the argv bytes, so it passes over nothing.
- **AC6** — When `python tools/govkit/govkit.py selfcheck` runs over the real tree after S6, it is
  green and prints a graded count of at least one and a reader count equal to the S6 legs whose
  argv bytes name their conf, which excludes `recall floor` (AC9 observes that one); with any one of
  those legs' guards reverted it reds naming that leg.
  Red when: the population is empty and the check reports a green zero.
  figure: both counts are DERIVED at observation time from `tools/gate-legs.json`.
- **AC7** — When `tools/lexicon/kit.toml` and `tools/lexicon/adopt-lexicon.sh` are read after S7,
  neither states that a root conf falls into no guard class, and `lexicon wiring` still grades the
  declaration.
  Red when: the stale sentence survives beside a guard that now names the conf.
- **AC8** — When `bash tools/check-kit-versions.sh` runs, the drift-audit, govkit, lexicon and
  codebase-map version constants agree with their markers.
  Red when: a constant moves and its marker does not.
- **AC9** — When `python tools/govkit/govkit.py selfcheck` runs over the real tree after S6, the
  `recall floor` guard names `.memory-tree.conf` and no near-miss line names that leg; with that guard
  entry reverted in a scratch copy, selfcheck stays green and its near-miss line names `recall floor`,
  `.memory-tree.conf` and `tools/memory-recall/recall_conf.py`.
  Red when: the recall floor stays unguarded on its conf, so a `RECALL_FLOOR`-only commit still
  guard-skips the leg TOOL-aWalkedCorpus-5 was filed on while this unit claims to answer it.

## 7. Gates

`drift-audit selftest` · `drift-audit records` · `govkit selfcheck` · `govkit selftest` · `lexicon naming predicates` · `lexicon wiring` · `kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · a bare-remote fixture with local main behind, at and ahead of a raised pin, plus an unfetched tracking ref · none
New arm: tools/govkit/selftest.py · a root-conf guard, an undeclared root file, a conf-reading guarded leg without the conf, and a guarded leg reading a root conf through a same-directory module · none

## 8. Open questions

- **F1 — how does a root conf reach a guarded leg's verdict?** Options: (a) widen govkit's
  partition with a derived `root-conf` class, add the conf to each guard and gate completeness; (b)
  a held canary requiring an unguarded same-kit reader; (c) retire the half as done by lexicon's B1.
  (b) reds on landing and its looser form cannot fail (§4); (c) leaves three measured instances.
  RESOLVED (agent, 2026-09-14, delegated): (a), the most feature-rich survivor. It needs no new
  install location or public surface: the emitter already carries a guard verbatim and drops an
  untracked one. It answers TOOL-aWalkedCorpus-5: the leg that row was filed on, `recall floor`,
  gains the conf by hand in S6, because its read goes through a module S5 does not grade (§3).
- **F2 — what does drift compare against in a clone with no remote?** Options: refuse, or the local
  branch announced. Refusing breaks every remote-less fixture and adopter for a hazard that needs a
  second copy of the branch to exist. RESOLVED (agent, 2026-09-14, delegated): local, announced; an
  `origin` without the tracking ref still refuses.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U17. Three divergences, each recorded here. The
  DR's lexicon guard edit was struck twice at BASE because govkit's partition refuses a root conf
  (TOOL-aSurfacedLexicon-4), so F1 widens the partition first and extends the edit to the three
  more legs a probe found. The canary becomes a govkit selfcheck check, which binds on every bar,
  where a held canary would run only on demand. Tier-2 rather than the brief's Tier-1, by the
  kickoff manifest's tier rule: the unit changes drift-audit's and govkit's contracts. One edge the
  brief's table does not list is added inside this group: hands-off to unit 23.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H7, H9, M7, L3). H7: §4's sweep matches by
  file with recorded counts, comment lines dropped (30 hits in 8 files at BASE, re-measured by the
  fold); AC3 grades file and count, and its rpartition clause moves into AC2's header claim. H9: S6
  gives `recall floor` `.memory-tree.conf` by hand, S5 prints same-directory near-misses
  report-only, and F1's text names the leg (AC9); AC6's reader count excludes that leg, whose argv
  bytes never name the conf. M7 and L3: S8 and AC8 follow the build's
  one-owner rule for kit versions — drift-audit, govkit, lexicon and codebase-map move here, and
  memory-tree and the review harness ride their owners' moves.

## 10. Reuse audit

- **Probe result.** `reuse_lookup.py` over the phrase "compare ancestry against the
  remote-tracking default branch instead of local main" returned name-stem neighbours only —
  `tracked` in `tools/govkit/govkit.py`, `branches` in `tools/memory-tree/check-arms.py` — and no
  seam for a base resolver; its coverage line reports `.sh` unscanned. Reading source found the two
  seams this unit extends: the `Git` class and base ladder in `tools/drift-audit/drift_report.py`,
  and govkit selfcheck's 7c partition at `tools/govkit/govkit.py:1395`. No shared default-branch
  resolver exists to reuse; TOOL-aCollapsedScan-8 records why.
- **DR against BASE.** DR says the lexicon leg's guard simply gains `.lexicon.conf`; BASE refuses
  it in govkit 7c, the lexicon kit's own descriptor says so, and TOOL-aSurfacedLexicon-4 struck that
  edit after measuring it. DR's i120 is already answered at BASE by `lexicon wiring` grading the
  declaration on every bar (landed 2026-09-06); S6 closes the class that fix left open.
- **Rejected candidates and the test that rejected each** are in §4 Alternatives rejected.
- Recall terms used: drift_report base_ref origin/HEAD local-main stale GOV_DEFAULT_BRANCH guard
  lexicon.conf canary govkit partition ratchet — passed as `--terms` with the question "why does
  drift-audit compare ancestry against local main and why can a root conf not be a leg guard". Top
  hits: TOOL-aWalkedCorpus-5, the aSurfacedLexicon spec-audit record naming the struck edit,
  TOOL-aPacedTurnstile-12, and TOOL-aCollapsedScan-8.
