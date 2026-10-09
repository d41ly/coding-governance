**Serves:** journal TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1

# Spec brief — aLevelledCopy, all four units

You author the spec for each unit you are handed, and you write no code. The mandate is the
owner's prompt and its one clarification, recorded beside this file in
`2026-10-09-prompt-TOOL-aLevelledCopy-1.md`; read it first. Every spec is **Tier-2**, under the
spec template's full ten sections including `§3 ### Edges` and `§10 Reuse audit`, with filename
`memory/builds/aLevelledCopy/spec/2026-10-09-spec-<FAMILY>-aLevelledCopy-<n>.md`, status `OPEN`,
`rev-1`, `node a`, `base ce9192c0`, and `streams tooling` (`deployer` for DEPL-aLevelledCopy-1).
Header `order`: units TOOL-1, TOOL-2 and DEPL-1 are `order 1`; TOOL-3 is `order 2`, because it
writes `tools/check-wiring.sh` after TOOL-2 does. Name the specs you author in `authored` by unit
id, never by path.

**Invariants for all four.**
- A pass runs no merge bar, no self-test suite and no `*.test.sh`; the owner runs kit suites later
  from the merged tree (ruling of 2026-10-06). Each acceptance criterion is observed by a DIRECT
  check: a fixture, a `--selftest` flag, or one named arm run alone. Say which in §6.
- Every new gate arm has its failing case OBSERVED: stage the break, see RED, unstage, see GREEN.
- §6 criteria never name a file the unit itself creates as a backticked path (check-spec-tokens
  joins those against `git ls-files`): name the observing command or the leg instead.
- Run `python tools/check-spec-tokens.py --list` and put every `NEAR [guards]` leg it prints for
  your §4 `### Files touched (estimate)` on the §7 leg line.
- No kit-version bump inside a unit. One bump per touched kit happens once, after the last unit.
- Do not edit `memory/DECISIONS.md` or any backlog. Note discoveries in §8 or §3 Edges.

## TOOL-aLevelledCopy-1 — receipt-sync grades a mismatched row through the target's clean filter

**Where.** `tools/run-gates/check-receipt.py`, `check_engine_rows`, line ~91: `got =
hashlib.sha256(found.read_bytes())`, compared to `row["sha256"]`, else `DRIFTED`. The module
docstring's last "does not check" bullet calls an eol-filter red "a true reading"; that bullet is
what this unit narrows, and the spec must rewrite it rather than leave two answers.

**The rule to port, not invent.** `govkit cmd_check` already grades this case
(`tools/govkit/govkit.py` ~4940, DEPL-aRepatriatedFork-17 S2). When `sha256` mismatches: if the row
carries `oid`, and `git hash-object --path=<p>` of the working file equals `oid`, AND the raw bytes'
own blob oid is NOT `oid`, the row is `eol-only` and counts as verified. The second half keeps a
tampered `sha256` over untouched bytes red. Reuse the predicate verbatim so the leg and `govkit
check` cannot disagree (the two-answers class).

**Cost.** Spawn git ONCE for all mismatched rows: `git -C <tree> hash-object --stdin-paths`, which
applies each path's own filters. On inCMS this is 65 rows; a spawn costs ~0.75 s on node a, so
per-row spawns would cost ~50 s. Spawn nothing when every row matches. A row with no `oid` (a
receipt below schema 3) stays `DRIFTED` and the spec says so. Neither adopter has one: engine
rows carrying `oid` measured 196/196 in inCMS and 190/190 in nc on 2026-10-09.

**Output.** The summary line gains the eol-only count, as `cmd_check`'s does, so a green over
normalized rows is distinguishable from a green over raw-equal rows.

**Fixture arms.** The file's built-in arms run on EVERY invocation and gov's own tree has no
receipt, so the new arms must be built-in arms too, over a temp git repo: (a) `core.autocrlf=true`,
the file committed LF, deleted and re-checked-out (a CRLF copy), then an `eol=lf` pin committed
after it → graded clean, eol-only 1; (b) the same copy with one real byte changed → `DRIFTED`;
(c) `core.autocrlf=false`, no pin, a CRLF copy written by hand → `DRIFTED`; (d) the tamper half:
LF bytes equal to the blob and a wrong `sha256` → `DRIFTED`. An arm whose git call fails must FAIL
rather than pass by grading nothing. The `git` dependency is new for these arms only; say what
happens on a host without git (a named refusal, not a silent pass).

**M12, already measured** (the instrument and results are in this build's `build/` record
`2026-10-09-build-TOOL-aLevelledCopy-1-m12-probe.md`, committed beside the specs). Three candidates:
A — the clean-filter oid (above); B — `git diff --quiet` then sha256 of the index blob; C — sha256
of the bytes with CR stripped. Fixture verdicts: eol-only copy A/B/C GREEN; real edit A/B/C RED; a
CRLF copy with no filter A/B RED, C GREEN. **C loses**: git would commit those CRLF bytes, so
green is false. A receipt written on a CRLF box graded on an LF clone reds under both A and B (the
tamper half fires), so it does not discriminate; state it as a non-goal (receipt portability across
install machines). A and B survive; **A wins by M3's tie-break**, reuse of the `cmd_check` seam, at
one spawn where B needs two. Record all of this in §4 `### Alternatives rejected` and §10.

**Staged break, the prompt's own wording.** A fixture repo with `core.autocrlf=true`, an `eol=lf`
pin added after checkout and a CRLF working copy: receipt-sync RED before the fix, GREEN after, and
a one-byte edit that stays RED. Observed by running the pre-fix file from BASE against the fixture,
then the fixed file.

**Non-goals.** `check-wiring.sh`'s `check_eol` population stays exactly as bounded (its own comment
says why). No change to `govkit`. No re-checkout or rewrite of any working copy.

## TOOL-aLevelledCopy-2 — check-wiring sets core.sshCommand from push-main's keepalive string

**Single source.** `tools/push-main.sh` ~180 holds the only literal:
`: "${GIT_SSH_COMMAND:=ssh -o ServerAliveInterval=30 -o ServerAliveCountMax=120 -o TCPKeepAlive=yes}"`.
Split it into a one-line single-quoted definition, `GOV_SSH_KEEPALIVE='ssh -o …'`, and
`: "${GIT_SSH_COMMAND:=$GOV_SSH_KEEPALIVE}"`. The `:=` keeps a caller's own `GIT_SSH_COMMAND`. Keep
the long comment above it accurate. `check-wiring.sh` DERIVES the value by reading that definition
line out of the resolved `push-main.sh`, with one anchored `sed` that must match exactly one line.
It never spells the option string.

**Why derive, not share a third file.** The two are separate kits (`push-main`, `check-wiring`)
with `requires = []`, and the `tools/lib/` home is gov-internal: copy-installed kits carry their
contents inline. And the dependency points the right way: `push-main` ships `.githooks/pre-push`,
the gate that idles the socket. A tree without push-main has no pre-push bar to outlast, so the arm
SKIPS there, saying so.

**The arm, `check_ssh_keepalive`, called after `check_merge_ours`.**
1. Resolve `push-main.sh` with the receipt-first rungs every other arm uses
   (`resolve_receipt_path`, then the kit-layout probe). Absent → `skip ssh — push-main is not
   adopted here, so no pre-push bar holds a push open`.
2. Extract `GOV_SSH_KEEPALIVE`. Zero or several matches → `UNWIRED ssh — cannot derive the
   keepalive from <path>` (liveness: a derivation that found nothing never reads as ok).
3. Remotes: any `git remote get-url --push --all <r>` that is ssh-shaped (an `ssh://`-family URL,
   or scp-like `[user@]host:path` with a host longer than one character, so `C:/x` is a path).
   `get-url` applies insteadOf rewriting. None → `skip ssh — no remote pushes over ssh`.
4. `cur=$(git config core.sshCommand)` reads EVERY scope, and that is deliberate. "Only when
   unset" means unset at any scope: a global operator value carrying an identity must not be
   shadowed by a repo-local one.
   - Unset, under `--fix` or `--session`: `git config core.sshCommand "$want"` (repo-local),
     `FIXED ssh` and one health event, `sshcommand-set`, through `add_health_event` exactly as the
     hookspath arm does. Under `--check`: `UNWIRED ssh — … Fix: <command>`, counted. That is dormant
     wiring, the same class as an unset `core.hooksPath`.
   - Equal to `$want`: `ok ssh`.
   - Any other value: never overwritten. If it carries `ServerAliveInterval`, `ok`, naming it the
     operator's value. Otherwise `note ssh — core.sshCommand is the operator's (<scope>); NOT
     overwriting; it carries no keepalive …`, which is `note` and not `UNWIRED`, by the script's
     header vocabulary: a deliberate operator value is not dormant wiring.
5. Update the header comment: the auto-fix list, the health-event list, and what the arm does not
   check (GIT_SSH_COMMAND in someone's environment, which outranks core.sshCommand; HTTPS remotes).
   Check whether the health-log token set or the orientation card's event counter is a closed set
   (grep `merge-driver-set`) and extend it where it is.

**Gate the pair** in `tools/check-wiring.test.sh`, over a fixture holding copies of both scripts
and a remote `git@example.invalid:o/r.git` (no network is touched; nothing pushes):
(a) `--session` sets `core.sshCommand` to exactly the value obtained by sourcing push-main's
definition line in a subshell; (b) the copy's definition is mutated, and the arm sets the MUTATED
value, which proves derivation rather than a matching second literal; (c) a pre-set operator value
survives `--fix` and `--session` byte-for-byte; (d) an https-only remote → `skip`, nothing set;
(e) the definition line deleted → `UNWIRED`; (f) `--check` on an unset ssh tree → `UNWIRED`,
non-zero exit; (g) `push-main.sh` holds exactly one `ServerAliveInterval` literal, on the
definition line, and its `GIT_SSH_COMMAND:=` default names `$GOV_SSH_KEEPALIVE`. Each arm's
failing case is staged and observed. Run the new arms alone, not the suite.

**Observed adopter state, for the spec's §4.** inCMS's `.git/config` already carries exactly this
value as `core.sshCommand` (set by the installer being retired), so after the update the arm reads
`ok` there. Its `origin` push URL is `git@github.com:d41ly/incms.git`. gov pushes over HTTPS, so
the arm SKIPS in gov's own tree.

**Out of scope, name it in §3 Edges as LEFT:** `push-main.sh`'s `:=` overrides an operator's
`core.sshCommand`, because env outranks config, and so drops an identity it carries. That
predates this build. A fix would change who wins between two operator settings, which is not
strictly beneficial, so it is filed as an ask, not built here.

## TOOL-aLevelledCopy-3 — gov's executed hooks are 100755, and check-wiring grades a hook's index mode

**Data.** `git ls-files -s .githooks` shows every file 100644. Mark 100755 exactly the files git
EXECUTES: `.githooks/commit-msg`, `pre-commit`, `pre-push`, `pre-rebase`. Not `gate-env.sh` or
`straggler-guard.sh` (sourced: verify by grep), not `*.test.sh`, not `pre_push_bar_selftest.py`.
That set is the one `GOV_WIRING_HOOKS` already names; say whether the arm reads that variable or
a wider fixed list of git's hook names (githooks(5)), and why. An adopter's own hooks (inCMS has
`post-merge` and `commit-msg` at 100644) are only reached by the wider list, which favours it. The
mode change is `git update-index --chmod=+x`, and the spec says how the staged break shows it.

**The arm**, inside or beside `check_hooks`, after the hooks dir resolves. For each TRACKED file in
that dir whose basename is a git hook name, read its index mode from the index of the checkout
that SUPPLIES the dir (`git -C <that checkout> ls-files -s`).
- The dir is inside THIS worktree, mode 100644: under `--check`, `UNWIRED hooks — <hook> is
  tracked 100644; git on a POSIX node will not run it. Fix: …`. Under `--fix`, `git update-index
  --chmod=+x -- <path>` plus `chmod +x <path>`, a `FIXED` line, and health event `hookmode-set`.
  Under `--session`, REPORT ONLY.
- The dir names ANOTHER checkout (this repo's linked worktrees point at the primary's absolute
  `.githooks`): `note` naming the checkout. This mirrors `check_hook_blobs`, whose header explains
  why a sibling checkout's state never gates here. Until the primary takes this landing, every
  worktree on a node would otherwise go UNWIRED.

**The fork to record in §8 and resolve under delegation.** The peer's text asks for repair under
`--fix/--session`. The eol arm's recorded rule says `--session` sets an unset git config "and
nothing bigger"; a SessionStart that stages an index change widens that write surface. Options:
(a) `--session` repairs, which is the most feature-rich; (b) `--session` reports and `--fix`
repairs. M3 veto 3 (a write surface beyond what the tier priced) discards (a), so ratify (b) and
write the reason. It is not lost capability: DEPL-aLevelledCopy-1 makes the normal `govkit update`
commit carry the bit for every shipped hook, and `--fix` covers an adopter's own hooks.

**Staged break on a POSIX git.** Node `a` has WSL2 with git 2.53 (`wsl.exe -e sh -c …`). A
fixture repo with `core.hooksPath=.githooks` and a 100644 `pre-commit` that exits 1: the commit
SUCCEEDS (the hook did not run, and git prints its ignored-hook hint). After `check-wiring.sh
--fix`, the same commit is REFUSED. Record it as an acceptance observation in the ledger. The
`check-wiring.test.sh` arms are host-independent (they grade index mode, report and repair); the
"does it run" half is POSIX-only, so on a host where `uname` is MINGW/MSYS the arm announces its
skip in words rather than passing silently.

## DEPL-aLevelledCopy-1 — govkit update carries gov's exec bit onto an existing engine row

**Today.** `land_through_index` (`tools/govkit/govkit.py` ~8242):
`mode = entry[0] if entry else ((gov_tree_mode(...)) or "100644")`. An existing index entry's mode
always wins, so `.githooks/pre-push` (an `engine` row in both adopters, index 100644) stays 100644
forever, even after gov ships 100755. The aScouredKit wave-3 cross-OS lens recorded this as a
finding on 2026-08-31 (`memory/builds/aScouredKit/reviews/2026-08-31-review-TOOL-aScouredKit-2-wave3-lens-crossos.md`);
no unit built it.

**The decision this spec records** (the peer asked for it explicitly): YES, carry, but UPGRADE
ONLY, and only for `role = engine` rows. Engine rows are gov's bytes verbatim, so gov's mode is
part of what it ships. Never DOWNGRADE: an adopter that set a bit gov lacks keeps it, which loses
nothing and cannot break a hook. `merged`, `seed`, `project-owned` and `rendered` rows keep the
adopter's mode, because the file is theirs. Symlinks (120000) are untouched.

**The hard half.** When gov's BYTES did not change between the receipt's commit and the target
commit, update's verdict grid likely never reaches `land_through_index` at all, so a mode-only
delta must be detected separately: gov's mode at the target commit is 100755, and the target's
index entry is 100644 with an unchanged blob. Read the `update` flow (`VERDICT_GRID`, its
`o_state`/`t_state`, the read-only report and `--write`) and say where the mode-only row joins it,
how it is REPORTED in read-only mode (one line per row, so the adoption session's read-only dry run
predicts it), and that `--write` applies it with `update-index --cacheinfo <mode>,<oid>,<path>` and
`chmod +x` on the working file. The receipt grades oids, not modes, so no receipt field changes;
confirm that against the receipt writer. Say whether `govkit check` should report a mode deficit,
and resolve it under M3.

**Acceptance shape.** Fixture targets driven through govkit's own selftest harness style
(`tools/govkit/selftest.py`, one arm or one slice, never the whole suite): (a) an engine row at
100644 with gov at 100755 and the same bytes → read-only update names the mode change, `--write`
leaves index mode 100755, and a second update is a no-op; (b) an adopter's engine row at 100755
where gov is 100644 → stays 100755; (c) a `merged` row at 100644 where gov is 100755 → unchanged;
(d) a row whose bytes AND mode both change lands both in one write. Observe (a) RED at BASE.

**Edges.** TAKES: TOOL-aLevelledCopy-3's 100755 modes, which are this unit's real-world input.
The fixture builds its own gov tree, so the build order does not bind the test.
