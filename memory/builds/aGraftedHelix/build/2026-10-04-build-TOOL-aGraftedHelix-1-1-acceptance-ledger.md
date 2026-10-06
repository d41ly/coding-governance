# Acceptance ledger — TOOL-aGraftedHelix-1

**Serves:** journal TOOL-aGraftedHelix-1

Node `a`, 2026-10-05. The build commit is `72ef6159`, over the spec's rev-6 commit `f3f9d28c`. No merge
bar and no self-test suite ran in this pass. The driver-suite criteria were observed by the suite's
new run-claim block run ALONE behind its own prologue, as a slice under `tools/unattended/`, and the
tick criterion by the tick suite's prologue with its LIVE arms; each new arm was observed RED against
a staged break first. The breaks were staged in two driver copies and one tick copy, nineteen of them
in the driver, and restored byte-for-byte after each run. The whole suites are the main loop's at
VERIFYING, and the slice counts are the evidence for their raised floors.

**Evidences:** TOOL-aGraftedHelix-1
- AC1 — `bash tools/unattended/unattended.sh --claims` — over the suite fixture's empty bare origin it
  printed exactly `claims: none` and exited 0. Red under the staged break that made an unanswering
  read print `claims: none`, which is AC3's own arm.
- AC2 — `--claims` — five seeded `gov-claim` commits printed five rows of five TAB-separated fields,
  `gA:live gB:stale gC:held gD:terminal gE:unknown` in slug order, the malformed claim aged `-`, the
  split read from the fixture's `RESUME_STALE_BOUND`. Red when the stale split ignored the bound:
  `gB:live`.
- AC3 — `UNATTENDED check 91 FAILED` — with the origin re-pointed at a path that does not exist,
  `--claims` exited 2 naming check 91 and never printed `claims: none`. Red under the break that
  answered a failed read with an empty list.
- AC4 — `--preflight` — the first preflight left the claim naming `fixture-session` with
  `status: live`; a clone of the fixture under `other-session` and keepalive `k2` exited non-zero with
  `UNATTENDED check 89 FAILED` naming `node`, `session fixture-session` and the beat age, and held no
  run-state file. Red when the take-over column took a live foreign claim.
- AC5 — `claim taken over` — a seeded stale claim and a seeded landed one were each taken by a new
  session's `--preflight`, the claim then naming `fixture-session` with `status: live`, and only the
  stale take-over printed `claim taken over — tFresh · node other · session s-old`. Red when the
  stale row was moved out of the take, announced cell.
- AC6 — `UNATTENDED check 90 FAILED` — a `git` shim on `PATH` moved `refs/gov/runs/<slug>` to a
  racer commit before forwarding the push; `--preflight` printed check 90's full sentence and wrote
  no run-state file, and over a committed ABORTED `tRun` the record hashed the same and no archive
  appeared. Red when a lost race was classed as not completed, and red again when the claim write was
  moved after the rotation: the record was retired before the CAS lost.
- AC7 — `--resume <slug> --keepalive-id <recorded id>` — the holder's resume exited 0 and left a young
  claim's sha unchanged; a claim of its own aged a third of the bound had its `beat-utc` moved; a
  claim rewritten to `s-other` live gave `UNATTENDED check 90 FAILED` naming `--code claim-lost`, the
  record unchanged, and `--abort <slug> --code claim-lost` was then accepted. Red when the holder was
  always due, and when the holder column took a foreign claim. Over the tree,
  `grep -c '^HALT_FLOOR="8"$' .unattended.conf tools/unattended/.unattended.conf.example` printed 1 for
  each file; the core halt set counts eight.
- AC8 — `run_takeover` — under `s-new`, a presumed-stopped `tRun` (an empty commit dated 2000) whose
  claim `s-third` held live was refused at `UNATTENDED check 89 FAILED` with the record byte-unchanged;
  the same claim aged past the bound was taken, `claim taken over` printed and the claim then named
  `s-new`. Red when the take-over column took a live foreign claim.
- AC9 — `git ls-remote` — `--hold` wrote `held`, the released `--resume` wrote `live` under `k2`, and
  `--abort` wrote `aborted`, with `refs/gov/runs/<slug>` still listed on the origin; under a foreign
  live claim `--abort` exited 0 and printed `claim not written`. Red when `--hold` and `--abort` wrote
  no status.
- AC10 — `UNATTENDED check 90 FAILED` — `--close` under a foreign live claim refused before any
  Definition-of-Done line, no `UNATTENDED check 13 FAILED` printed, and the phase stayed RUNNING. Red
  when `--close` read no claim.
- AC11 — `claim(s) on the remote` — with one claim of another slug per verdict, `--preflight` printed
  `4 claim(s) on the remote for other slugs` listing the live, stale, held and unknown ones and not the
  aborted one; with none it printed no such line. Red when the terminal filter was removed.
- AC12 — `tools/unattended/resume-tick.sh` — the tick over a LIVE fixture with a bare remote and a
  claim of its own aged 1000 s printed `beat · unattended: beat — tRun · renewed` and the claim's
  `beat-utc` moved; with `--dry-run` the line ended ` (dry-run)` and the ref was unchanged. Red when
  the LIVE row was removed (the generic `skip · verdict LIVE`), and red when the dry-run guard was
  removed: the dry run pushed.
- AC13 — `bash tools/unattended/adopt-unattended.sh --check` — exit 0, `in sync`;
  `grep -n -- '--claims' memory/guides/UNATTENDED-VERBS.md` found the entry at line 219; the
  `For the holder it writes nothing` probe printed 0 over the rendered Skill and over
  `tools/unattended/SKILL.template.md`, both 1 at `HEAD` before the edit; the §7-to-§9 slice of
  `memory/guides/UNATTENDED-STOPS.md` counted 11 lines naming a claim, against 0 before.
- AC14 — `bash tools/check-kit-versions.sh` — exit 0, `clean — 16 declared carrier(s) under tools/`,
  unattended at 1.61 in every carrier; `python tools/govkit/govkit.py epoch --base 5266d22e` at the
  build commit printed `epoch: unattended · clean · 1.61` with no kit in the range red.
- AC15 — `--claims` — against the real remote on node `a`, 2026-10-04T23:22Z, with 9 bash processes
  on the node: 5906, 5934 and 5326 ms per call, driver start-up included, each `claims: none`. One
  claim write against a bare repository on node `a`, 2026-10-04T23:23Z, with 8 bash processes, the
  driver's own sequence (`git mktree`, `git commit-tree` under the fixed identity, a bounded
  `git push --porcelain --force-with-lease`): 1075, 1042 and 1163 ms; a `--claims` read against
  that bare repository took 2393 ms. A pooled self-test run from another worktree was loading the
  node during the later slice runs, not during these.
- AC16 — `2026-02-30T00:00:00Z` — a claim with that `beat-utc` sorting before a fresh live one made
  `--claims` print `gA:-:unknown;gB:-:unknown;`, every claim of the one `date -u -f -` call. Red when
  the answer-count alignment was removed: `gA` read an age and `live`.
- AC17 — `UNATTENDED check 91 FAILED` — a `git` shim on `PATH` answering the claim push with a `!`
  line reading `[remote rejected] (pre-receive hook declined)`, and then exiting 124, made
  `--preflight` refuse at check 91 both times, never check 90, with no run-state file. Red when both
  classes were read as a lost race.
- AC18 — `--resume <slug> --replaces <old> --keepalive-id <new>` — with `CLAUDE_CODE_SESSION_ID` unset
  the claim's `keepalive` became `k2`, and the next `--resume <slug> --keepalive-id <new>` exited 0
  with `git ls-remote` unchanged; the LANDING re-bind over the prior session's stale claim wrote `k2`
  into it, and over a fresh foreign live claim printed `claim not written` and exited 0; a holder
  meeting a claim of its own session under `k-older` rewrote it under `k1` and exited 0. Red when
  `--replaces` and the re-bind wrote nothing, when the holder was always due, and when the
  `same session` row was removed from the holder column.
- AC19 — `--close` — a `git` shim failing only the fetch of `refs/gov/runs/*` made `--close` refuse at
  `UNATTENDED check 91 FAILED` before any DoD line; `--dispatch` under a foreign live claim refused at
  `UNATTENDED check 90 FAILED` with the record byte-unchanged and no row; under a foreign stale claim
  both `--close` and `--dispatch` refused naming `--code claim-lost` and the ref did not move. Red when
  `--close` read no claim and when the holder column took a foreign claim.
- AC20 — `--landed` — over a pushed LANDING whose claim was its own and live, the claim then read
  `status: landed` and `--claims` printed it `terminal`; under `LANDER_MODE=in-place`, where
  `--landed` only observes, the claim read `landed` too (spec rev-7). Red when `--landed` wrote no
  status, and the in-place arm was red against the driver before its rev-7 write: `live`.
- AC21 — `RUN_CLAIMS` — with the line removed from the fixture's `.unattended.conf`, `--preflight`
  exited 0 with exactly one `unattended: NOTE` naming `RUN_CLAIMS` and `git ls-remote <bare> 'refs/gov/*'`
  printed nothing; `RUN_CLAIMS="maybe"` exited 2 naming the key. In the tree,
  `grep -c '^RUN_CLAIMS="on"$' .unattended.conf` and
  `grep -c '^RUN_CLAIMS="off"$' tools/unattended/.unattended.conf.example` each printed 1. Red when
  an undeclared switch read `on`.
