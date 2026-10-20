# Research: trust — every claim a session reads to orient or resume, its writer, witness class and freshness

**Serves:** research PLAY-dClosedLoop-1

The gov-researcher's return for handoff `prompts/2026-10-14-prompt-PLAY-dClosedLoop-1-8-researcher.md`
(dispatch 13), verbatim. The harness escaped `<`, `>` and `&` in the returned text as HTML entities;
they are restored here, and nothing else is changed.

---

## 1. Inventory

| Claim | Writer | Witness class | Invalidated by | Re-derivation, cost | Check comparing it |
|---|---|---|---|---|---|
| Card `tree —` (branch, BASE, dirty count) | SessionStart hook (`--card --write`) | hook-written | HEAD moved, tree edited | `git rev-parse HEAD` + `status --porcelain`, about 75 ms | stale BASE refused only at append (`manifest-check.sh:1159`). Replay prints a `now —` line and compares nothing (`:721-725`) |
| Card `worktrees —`, `recent —` | hook | hook-written | another session wrote | `git worktree list` / `log -5`, under 50 ms | none |
| Card `drift —` | hook, reading `drift-history.tsv` | verifier verdict, second-hand | HEAD moved; any worktree's bar appends | shows its own `HEAD`/`not HEAD` (`:473`); a full re-run is a bar leg | labels itself only |
| Card `claims —` | hook, through `unattended.sh --claims` | remote ref | remote moved, time passed | `git ls-remote origin 'refs/gov/runs/*'`, 551 ms | none at replay (`:647`) |
| Card `live —`, `overlaps —`, `health —` | hook | generated / local refs / hook log | HEAD moved, last fetch, time passed | under 1 s each | overlaps notes "as of this clone's last fetch" (`:554`) |
| Card READY + `## task/read/records` | agent, via `--card --append` | actor-typed (shape checked) | HEAD moved, scope changed | none, it is a judgment | `--card --check` checks that citations exist, not that they are true (`:728-735`). 5.1 s, rc=1 now |
| Manifest `last-audit` / `last-body-change` | agent at kickoff | actor-typed, ancestry checked | watched path changed | ratchet run, 966 ms | C3/C5/C9 (`manifest-check.sh:1433-1579`), a bar leg |
| `LIVE.md`, `ledger/*.md`, README `gen:` regions | `gen_build_index.py --write` | generated from spec headers | a spec header or README edited | `gen_build_index.py --check`, 4.06 s | that same `--check` (byte equality only) |
| README `status:` front matter (9 builds) | agent | actor-typed | the work moved | none | an authored status is an error when specs exist (`gen_build_index.py:747-751`) |
| Spec `**Status:**` (status, tier, order) | agent | actor-typed | the unit landed | join against merges: script below, about 3 s | none compares it to commits. `non_terminal_specs_cited_by_product_source` (`drift_signals.py:388`) only reports |
| `RUN.md` phase / witness / lease | `unattended.sh` | committed (run branch) | HEAD moved, run progressed | `git show <ref>:…/RUN.md`, under 50 ms | drift `run_records_nonterminal_but_merged` (`drift_signals.py:319`), report-only |
| `refs/gov/runs/<slug>` | driver, by compare-and-swap | remote ref | remote moved, time passed (beat) | `ls-remote`, 551 ms | the driver ages the beat (`unattended.sh:2177-2186`). Nothing joins a claim to `RUN.md` (absent: grep `refs/gov/runs` in drift-audit, memory-tree, run-gates) |
| Handoff `task-sha` | `handoff.py render` | generated | prompt file edited | `handoff.py check`, 167 ms | `agent-cap.js:2044` hook |
| Handoff `role-sha` | `handoff.py render` | generated | role or charter changed | `render --stdout`, 163 ms | never against the role (`agent-cap.js:59-60`) |
| `gate-full-green` (+`.shared`) | `run-gates.sh:5596` | verifier verdict | any byte of the tree | `gate-fingerprint.sh HEAD`, 97 ms | pre-push at-a-rev fingerprint |
| `refs/gov/bar-red` | `post-merge.sh:249` | remote ref | remote moved | `ls-remote`, about 550 ms | `.githooks/pre-push:1927` |
| Gate ledger / reuse cache | `run-gates.sh` | verifier verdict | the key moved (declared `reads`) | key recompute, inside the bar | reuse key (`run-gates.sh:3202-3212`) |
| Session logs (`build/*session-log.md`) | agent | actor-typed | another session wrote | none | none |
| Runlog journals (`.git/runlog/*.log`) | driver, gates, pre-push | hook-written | n/a (append-only) | n/a | grammar only (`tools/runlog/README.md`) |
| `DECISIONS.md` | agent / owner | committed, actor-typed content | superseded row | none | append-only (`check-memory-hygiene.sh:316`) |
| Auto-memory (`MEMORY.md` + 75 topic files) | agent | actor-typed, outside the repo | the tree moved | path grep, under 1 s | `dangling_pointers_in_own_ledger` (`drift_signals.py:470`), report-only |

## 2. Sequence

- **New session.** The hook writes the card, re-deriving tree, worktrees, claims (remote) and live. The drift cell is read from a file, not re-derived. Kickoff Step 1 fetches and re-derives BASE and is told to consume the card's node, worktree count and recent subjects as read (`SKILL.md:54-56`). Step 2b re-runs the ratchet. Steps 3-4 read `LIVE.md`, the ledger, `DECISIONS.md`, journals and recall output as read. Auto-memory is loaded by the harness as read, with no check. At append, the READY base must equal HEAD.
- **Resumed session.** `--card --replay` prints the stored card, re-derives only the `now —` line and reads no remote (`:647`). Nothing compares READY's base with `now —`. Every other cell is taken as read.
- **Agent.** It gets the handoff. The hook re-derives `task-sha`. `role-sha` and the card-derived inputs are taken as read.
- **Unattended run.** `--resume` re-reads `RUN.md` from the run branch and reads claims strictly (check 109, `unattended.sh:2146`). Spec headers and `LIVE.md` are taken as read.

## 3. Measurements

```
$ for f in memory/builds/*/README.md; do awk 'NR==1&&/^---/{f=1;next} f&&/^---/{exit} f&&/^status:/{print FILENAME": "$0}' "$f"; done
  … 9 files (aDeployScout SPECCED, aFerriedDossier OPEN, aWeighedCanon OPEN, dClosedLoop OPEN, 5 CLOSED)
$ (loop: LIVE.md row status vs README "**Build status:**")
compared=25 differ=0
$ gen_build_index.py --check
build-index: clean (1493 artifact(s))
```

```
$ (non-terminal spec headers vs later first-parent "merge: <slug>" on origin/main)
OPEN TOOL-aOrientedCast-28 product-commits-after=3 first-parent-merges-after=2
SPECCED TOOL-aTunedCompass-11 … merges-after=1
BLOCKED TOOL-aTunedCompass-2 product-commits-after=2 merges-after=1
INPROGRESS TOOL-dLandedVerdict-1/-2 merges-after=1
SPECCED TOOL-dPinnedHandoff-2/-3 merges-after=1
non-terminal specs: 30 · with later product commits: 2 · with a later merge: 7
```

```
$ git rev-list --count 742957fcf..HEAD ; git status --porcelain | wc -l ; git worktree list | wc -l
24 ; 0 ; 14          # card says: BASE 742957fc, dirty 11, worktrees 13
$ diff <(for-each-ref refs/gov/remote/runs/) <(git ls-remote origin 'refs/gov/runs/*') && echo IDENTICAL
IDENTICAL            # 17 claims; the card showed 9 and hid 8
```

```
$ (per claim: status, beat age, HEAD:memory/builds/<slug>/RUN.md phase, in LIVE)
aFrugalTurnstile claim=live beat=87h HEAD-RUN.md=LANDED
aBenchedProbe|aLevelledCopy|dSweptBranches claim=landed HEAD-RUN.md=LANDING
aRoutedQuill claim=landed inLIVE=1 (LIVE: DEFERRED)
8 claims held, 26-182h, for builds not in LIVE (aBriskPreflight, aGraftedHelix, …)
```

```
$ gate-fingerprint.sh HEAD → 01175d7b…; gate-fingerprint.sh d4debb1a → 38268b1b… = recorded 38268b1b…; 467 commits since
$ handoff.py render … --stdout | sha256(## Role) → 51b61c49e522 ; marker role-sha=51b61c49e522
$ (ledger: latest seconds per leg) legs=118 serial-sum=5590s longest=563s
```

```
$ (auto-memory: backticked paths not in git ls-files nor .git/)
path tokens=98 · absent=12 · topic files naming one=6 of 75   (e.g. repo-self-hosts-its-tools.md: .claude/SESSION-KICKOFF.md .domain-rules.md …)
flag tokens=67 · absent from tools/ skills/ .githooks/=2   (--ignore-cr-at-eol, --shared)
drift-history: dangling_pointers_in_own_ledger live 9/64
```

## 4. Gaps

- **HIGH.** A resumed session's card is 24 commits stale and nothing says so. Replay prints a `now —` line and never compares it with BASE (`manifest-check.sh:721-725`).
- **HIGH.** Run claims and `RUN.md` disagree, and no reader joins them. Measured 1 `live`/LANDED and 3 `landed`/LANDING. Absent: grep `refs/gov/runs` in drift-audit, memory-tree, run-gates.
- **HIGH.** `LIVE.md` is generator-valid (0/25 disagreements) but inherits actor-typed spec headers. 7 of 30 non-terminal headers sit under a build merged after the header last changed.
- **MED.** `SKILL.md:54-56` tells a session to trust the card's worktree count and recent subjects. Both moved (13 to 14 worktrees, 24 new commits).
- **MED.** `role-sha` is never compared with the role it was rendered from (`agent-cap.js:59-60`). It matched today only by re-render.
- **MED.** Auto-memory loads with no check. 12 of 98 paths are dead, and the drift signal only reports (9/64).
- **MED.** Held claims never hide (`:636`). 8 held claims (26-182 h) name builds absent from `LIVE.md`.
- **LOW.** The card's drift cell reads a common-dir file that every worktree's bar appends to. The last 3 readings came from other shas.
- **LOW.** `--card --check` shows existence only. It is rc=1 on `PLAY-dClosedLoop-1` (UNVERIFIED).

## 5. Candidates

**A — Witness-class ladder.** Trust committed history, hook-written records, remote refs and verifier verdicts. Re-derive anything actor-typed.
- Seam: the charter's settled point (5) and the card's `UNVERIFIED` tags (`manifest-check.sh:913`).
- LOSES if a non-actor-typed claim is stale now.
- Result: **LOST.** The hook-written `tree —` cell is 24 commits stale. The remote claim says `live` against a `RUN.md` that says LANDED.

**B — Input-key revalidation with a source floor.** Each claim stores a key over its declared read classes (`history`, `base`, `remote`, `clock`, plus a tree fingerprint). A reader trusts a claim only if the key recomputes equal and no source of the claim is actor-typed. Otherwise it re-runs the deriver, or treats an underivable claim as evidence only.
- Seam: the leg `reads` classes and reuse key (`run-gates.sh:2773-2778`, `:3202-3212`), `gate-fingerprint.sh`, `handoff.py check`.
- LOSES if a key-valid claim with only non-actor sources is false.
- Result: **SURVIVED.**
  - The full green's fingerprint matched at `d4debb1a` and differs at HEAD, so it is re-derived, correctly.
  - `role-sha` recomputes equal, so it is trusted, correctly.
  - The `live` aFrugalTurnstile claim's remote key is IDENTICAL, but its `clock` key moved (87 h beat), so it is re-derived to stale.
  - `LIVE.md` is key-valid but sourced from actor-typed headers, so it falls to evidence.
  - Without the floor, B loses on `LIVE.md` (0/25 disagreements, 7/30 stale headers).

**C — Re-derive at every read.** No stored claim is trusted, and records are caches.
- Seam: `--card --write`.
- LOSES if some claim's deriver is unaffordable or does not exist.
- Result: **LOST.** A full green costs 5590 s serial (118 legs). `DECISIONS.md`, session logs and auto-memory have no deriver.

## 6. Pick

I recommend B. Of the three, it alone passed a test written to make it lose, and it extends a seam the bar already enforces: the closed `reads` vocabulary and the reuse key. The mechanical rule is: trust a claim only when its key recomputes equal and its weakest source is not actor-typed; otherwise re-derive it or demote it to evidence. Most keys recompute in under 600 ms, against 5590 s to re-earn a green. It needs three things built:
- a stored key on the card cells, `RUN.md` and the claim rows;
- a `clock` read on claims;
- a claim-to-`RUN.md` join.

The routing researcher owns where each transition runs this check, and the cost researcher owns its budget.
