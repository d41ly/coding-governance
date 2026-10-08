# Acceptance ledger — dLadderedRemote, units 1 to 6

**Serves:** journal TOOL-dLadderedRemote-1 TOOL-dLadderedRemote-2 TOOL-dLadderedRemote-3 TOOL-dLadderedRemote-4 TOOL-dLadderedRemote-5 TOOL-dLadderedRemote-6

Node `d`, 2026-10-08. Every observation below was a direct check of one change: a truth-table arm,
an arm in the affected kit's own suite run alone, a staged break, or the cross-site probe recorded
beside this file. Every new arm was observed RED first, either against a staged break or against
the 40a8b8c3 version of its subject, and the break was then restored. No `tools/unattended/`
self-test suite was run, under the owner's standing instruction of 2026-08-23; `unattended.sh` was
probed by extracting its two changed functions. The merge bar is the main loop's, after the build.

**Evidences:** TOOL-dLadderedRemote-1
- AC1 — `resolve_remote` — the §2d arm printed `incms|main|main|` from both `resolve_remote` and
  `resolve_remote_sh` on the only-remote fixture.
- AC2 — `GOV_REMOTE` — both printed the `cannot choose a remote` refusal ending
  `export GOV_REMOTE=<remote>.`, with remote, branch and observed empty, on the two-remote fixture.
- AC3 — `incms` — with `GOV_REMOTE=incms` beside `origin`, both printed `incms|main|main|`.
- AC4 — `resolve_remote` — rows 4 to 8 matched; with rung 2 removed from `resolve_remote`, row 4
  printed the refusal instead of `origin|trunk|trunk|`.
- AC5 — `tools/push-main.sh` — one changed byte in its `resolve_remote_sh` copy made the parity loop
  print `inline copy of 'remote_ladder_sh' drifted ... tools/push-main.sh`.
- AC6 — `tools/push-main.sh` — run with remotes `incms` and `origin` and no `GOV_REMOTE`, it exited 2
  printing `can't determine which remote to land on — cannot choose a remote: GOV_REMOTE is unset`.

**Evidences:** TOOL-dLadderedRemote-2
- AC1 — `tools/drift-audit/drift_report.py` — on the only-remote `incms` fixture with every env value
  cleared, the header read `(base refs/remotes/incms/main @` and an eight-hex sha. The 40a8b8c3
  resolver over the same arm exited 2 with the handoff's exact `cannot resolve a default branch` text.
- AC2 — `GOV_REMOTE` — with a second remote, `drift_report.py` exited 2 naming `GOV_REMOTE`;
  `resolve_compare_base` returned `None` with the refusal; the bar runner printed
  `run-gates: no scope base — cannot choose a remote` and ran the guarded leg.
- AC3 — `GOV_REMOTE=incms` — the header named `refs/remotes/incms/main` beside an `origin` remote.
- AC4 — `resolve_compare_base` — it returned the merge-base with `incms/main` on that fixture; the
  runner on an `incms`-only fixture printed `GATE skip  guarded  (unchanged vs main)`, and the
  40a8b8c3 runner on the same fixture ran the leg.
- AC5 — `incms` — the cross-site probe in `2026-10-08-build-TOOL-dLadderedRemote-2-1-site-probe.md`
  read `incms`, its refusal or the declared fallback for every site and fixture, and `origin` nowhere.

**Evidences:** TOOL-dLadderedRemote-3
- AC1 — `bash tools/check-remote-literals.sh` — on the tree as it stood at 40a8b8c3 for every site it
  exited 1 with 54 hit lines naming every listed file, `tools/workflows/tier2-review.js` included.
- AC2 — `check-remote-literals.sh` — the self-test named one planted line per shape; deleting the
  default-after-`or` pattern left exactly that arm's planted line unnamed.
- AC3 — `DEAD PROBE` — planted lines in a `*.test.sh`, a `fixtures/` path and a `#` comment stayed
  clean, and an empty population exited 2 printing `DEAD PROBE`.
- AC4 — `check-remote-literals.sh` — after units 2 and 4 it printed `remote-literals: clean`.

**Evidences:** TOOL-dLadderedRemote-4
- AC1 — `tier2-review.js` — the new arm called a diff review with no `base` and with a blank one, and
  both threw the refusal `a diff review needs` before any agent; with the check disabled both arms red.
- AC2 — `base` — a spec audit with no `base` proceeded.
- AC3 — `tools/workflows/tier2-review.js` — `bash tools/check-remote-literals.sh` named neither file.

**Evidences:** TOOL-dLadderedRemote-5
- AC1 — `resolve_remote` — all twelve §2d rows matched in both languages; with `--short` restored in
  `resolve_remote`, the tag row printed `branch heads/feature has no configured remote`.
- AC2 — `check-remote-literals.sh` — the self-test named every planted spelling and both product
  files, 30 arms; the old `*`-is-a-comment rule left the `*)` case arm unnamed.
- AC3 — `check-remote-literals.sh` — the variable-named-like-the-remote arms stayed clean, and the
  real tree read `remote-literals: clean — 144 file(s)`.
- AC4 — `tools/gate-legs.json` — the python-resolver leg's guard lists `.githooks/`.
- AC5 — `resolve_compare_base` — with `GOV_DEFAULT_BRANCH=elsewhere` it still returned the
  `incms/main` merge-base; letting the environment select made it return `None`.
- AC6 — `git grep` — over the seven files, `set-head origin` and `origin/HEAD` matched nothing, and
  `WIRE-INTO-PROJECT.md` names `GOV_REMOTE` twice.

**Evidences:** TOOL-dLadderedRemote-6
- AC1 — `check-remote-literals.sh` — the self-test named all seven new spellings, 39 arms; with the
  argv-list pattern removed, the `--prune` argv row went unnamed.
- AC2 — `check-remote-literals.sh` — `self.origin = origin` in a `.py` file and `const base = origin;`
  in a `.js` file stayed clean, and the real tree read `remote-literals: clean — 144 file(s)`.
- AC3 — `WIRE-INTO-PROJECT.md` — the ladder bullet names the run-gates scope base, the codebase-map
  baseline assert and the playbook render as observed-only, and the guard bullet says `above`.
- AC4 — `.githooks/pre-commit` — with a tag named `main`, a commit on `main` was allowed, and with
  two remotes and the pin set the commit printed no `GOV_REMOTE` line; the guard reading
  `--short HEAD` refused the tagged commit.
