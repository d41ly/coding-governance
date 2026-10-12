# TOOL-aSparedSpawn-33 — the pre-push hook restores the caller's environment for the reuse digest

**Status:** INPROGRESS · rev-3 · 2026-10-12 · node a · Tier-2 · base 950dc27f · streams tooling · order 6 · closes TOOL-aSparedSpawn-25 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aSparedSpawn-33-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aSparedSpawn-33-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Make push-time cache reuse fire. `TOOL-aSparedSpawn-13` lets a push reuse a `remote` or `history`
leg's cached `ok` at the exact pushed sha, but the reuse digest hashes the environment the legs
inherit, and a pre-push hook's environment is not the caller's: git adds `GIT_EXEC_PATH` and a PATH
prefix, and Git for Windows adds `LC_CTYPE=C.UTF-8` where the caller set none. So an entry earned by
a direct bar never matches at push, and the owner-ruled saving is inert (closing review M3, findings
11 and 21). The owner ruled on the parked ask `TOOL-aSparedSpawn-25`: the hook restores the caller's
pre-git environment, and the digest is computed over that, never over git's additions.

## 2. Scope (IN)

Every site was read at 950dc27f; this unit builds after `TOOL-aSparedSpawn-32`'s merge, whose
read site and schema it extends, so its line numbers are re-read then.

- **S1** — The hook builds the RESTORED VIEW of the environment, the caller's as it was before git
  started the hook, by the table in §4: `GIT_EXEC_PATH`, `GIT_PREFIX` and `GIT_CONFIG_PARAMETERS`
  absent, `GIT_DIR` absent, the PATH components git prepends stripped from PATH's head, and
  `LC_CTYPE` absent where it is Git for Windows' injection. Every other variable keeps its value.
  The builder first measures the full difference on node a, `env` in a plain shell against `env`
  inside a real hook, and records it in the ledger; a name the table lacks is added to it with its
  rule, or the pass stops naming it. Observed by AC2.
- **S2** — The hook hands the runner the restored view for the DIGEST ONLY. On a SCOPED decision
  where it exports `GATE_REUSE_PUSH`, it writes the restored view's digest lines to a file in its git
  dir (rev-3) and exports `GATE_REUSE_DIGEST_ENV` naming that file. It clears an inherited
  `GATE_REUSE_DIGEST_ENV` for every bar, a STUB included, beside `GATE_REUSE_PUSH`, and names it on
  the `not honoured from the environment by this bar:` line. The legs' own environment is not
  touched: they run under the hook's environment exactly as today. Observed by AC3 and AC4.
- **S3** — The runner reads `GATE_REUSE_DIGEST_ENV` at the one knob read site `TOOL-aSparedSpawn-32`
  builds, beside `REUSE_ASK_PUSH`, into `REUSE_ASK_DIGEST_ENV`, and unsets it there. In the `push`
  mode only, `REUSE_DIGEST`'s env lines come from that file in place of `compgen -e`, filtered by the
  same name patterns, and each `tool` line resolves with `type -P` under the file's PATH. In every
  other mode the knob is ignored. A named file that is missing or unreadable empties the digest, so
  nothing is reused or cached, with `TOOL-aSparedSpawn-16` S18's line naming the step. Observed by AC1
  and AC5.
- **S4** — `REUSE_SCHEMA` moves up by one from the value `TOOL-aSparedSpawn-32`'s merge leaves, so no
  entry keyed under the old digest is trusted. Observed by AC6.
- **S5** — The end-to-end arm the review asked for, in `.githooks/pre-push.test.sh`: earn an entry
  with a direct bar, push through the real `.githooks/pre-push` under a scoped decision to a local
  bare remote, and assert `GATE reuse` on a remote leg. Observed by AC1.
- **S6** — `tools/run-gates/README.md`'s cache push subsection and the hook's SCOPED branch comment
  state the rule once each: the digest reads the caller's restored environment, and the legs read the
  hook's. Observed by AC7.
- **S7** (rev-2, adopted from the brief) — `tools/run-gates/post-merge.sh`'s scrub and the
  unattended driver's `_gknobs` clear `GATE_REUSE_LINEAGE` beside `GATE_REUSE`. Both bars run with
  `GATE_FULL`, under which an inherited lineage knob turns the runner's `lineage` mode on, so a
  post-merge or close bar would reuse. Observed by AC8.
- **S8** (rev-2, adopted from the brief) — the H49 knob-class table in `.githooks/pre-push.test.sh`
  (`BAR_INERT_KNOBS`) classifies every `GATE_*` knob this build added to the runner, this unit's
  `GATE_REUSE_DIGEST_ENV` included, each with its reason in the table's comment, so the arm's
  predicate reports nothing unclassified. Observed by AC9.

## 3. Non-goals (OUT)

- Changing the environment a leg runs under. The restored view feeds the digest alone.
- The digest's coverage of variables outside its name patterns, which the runner's
  `WHAT IT DOES NOT SEE` comment already states.
- Lineage reuse, which keys on ledger rows and reads no digest, and the mode precedence, both
  `TOOL-aSparedSpawn-32`'s.
- Running any suite or the bar inside the pass, and a kit version bump, which the lander mints.

### Edges

- **consumes-from** `TOOL-aSparedSpawn-32` — the one knob read site and the `push` mode of the
  composed runner; without that merge this unit would extend code the merge rewrites.

## 4. Design

### What the hook can observe of the pre-git environment

Git starts a hook with the caller's environment plus a known set of additions. The hook cannot read
the caller's environment directly, so it reconstructs each addition's prior state from what is
observable. Where a caller value is indistinguishable from git's own, the view marks the name
absent: an entry earned with the name set then misses, which costs a saving and never a verdict.

| Name | What git does | How the hook restores it |
|---|---|---|
| `GIT_EXEC_PATH` | exported for every hook | absent |
| PATH | git's exec path prepended, and on Git for Windows any further components node a's measurement shows | the leading run of exactly those components stripped, matched in native and MSYS spelling; anything after the first non-match kept |
| `GIT_PREFIX` | exported; the hook already unsets it at `:38` | absent |
| `LC_CTYPE` | Git for Windows sets `C.UTF-8` when the caller set none | absent when `GIT_EXEC_PATH` is a drive-letter path (rev-2), the value is `C.UTF-8`, and `LC_ALL` and `LANG` are unset; otherwise the caller's value, kept |
| `GIT_DIR`, `GIT_CONFIG_PARAMETERS` | present under an alias child or a `git -c` push | absent; `GIT_DIR` is already unset for execution at `:38` |

**Rev-2, what node a's measurement forced.** `env` in a plain Git-Bash shell against `env` inside a
real pre-push hook (git 2.54.0.windows.1) differs in seven digest-relevant ways: `GIT_EXEC_PATH`
(native spelling `C:/Program Files/Git/mingw64/libexec/git-core`), `GIT_PREFIX=` (empty),
`LC_CTYPE=C.UTF-8`, PATH's head `/mingw64/libexec/git-core:`, and every `/bin` component of the
caller's PATH reading `/usr/bin`, since a native git round-trips PATH through Windows spelling and
both mounts map to one directory. Three rules change by it:

- **PATH's head**: a leading component is git's when it ends in `/git-core` and `GIT_EXEC_PATH`
  ends with it, which matches the native spelling verbatim and the MSYS mount spelling as its tail.
  A drive-letter MSYS spelling (`/c/...`) is not matched and stays, which costs a miss.
- **`/bin` against `/usr/bin`**: the hook cannot tell which `/usr/bin` was a `/bin`, so the RUNNER
  reads each `/bin` component of PATH as `/usr/bin` when `[ /bin -ef /usr/bin ]`, in every mode, both
  for the PATH line and for the PATH its `tool` lines resolve under. Sound, because the test proves the
  two are one directory; elsewhere nothing is rewritten.
- **`LC_CTYPE`'s Windows test**: `GIT_EXEC_PATH` is a drive-letter path, which only a native Windows
  git exports, in place of a `git version` spawn on every push.

The view is written at ONE site, after the decision block, wherever `GATE_REUSE_PUSH` was exported:
the hook's own later exports (`GATE_RUN_ID`, `GATE_ATTRIBUTE`, the inherited-red pair) are not in it,
and the runner unsets or excludes each of them before its digest anyway. The hook lists exported names
with `compgen -e` redirected into the view file and read back by `mapfile`, then rewrites that file
with the view lines, so no fork is spent and no value but an admitted one reaches the disk. The
hook's admitted-name patterns are a copy of the runner's digest patterns, kept in step by an arm of
the S5 suite that compares the two pattern texts.

### The handoff

The view file holds one `env NAME=value` line per variable the digest's name patterns admit, in
the digest's own format, written with `printf` to `<git dir>/gate-reuse-view.<hook pid>`, an absolute
path, since the hook has no scratch directory of its own. It is removed once the bar returns, and by
the signal handler (rev-3): not by the EXIT trap, whose exact line `.githooks/pre-push.runlog.test.sh`
pins, and whose run-log writer an exec on that line would be charged to. The runner reads it with
`mapfile` and spawns nothing more than today. Values carrying a newline are written with `printf %q`,
and the runner's own listing writes them the same way in every mode, so a line is always one variable
and the two listings agree.

### Inventory

New knob `GATE_REUSE_DIGEST_ENV`, read by the runner and set by the hook. New runner variable
`REUSE_ASK_DIGEST_ENV`. No function is minted.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/README.md`
- `tools/run-gates/run-gates.evidence.test.sh`
- `tools/run-gates/post-merge.sh` (rev-2, S7)
- `tools/unattended/unattended.sh` (rev-2, S7)

### Alternatives rejected

These are the options the owner was offered and did not pick (`RUN.md`'s decision row for
`TOOL-aSparedSpawn-25`):

- **(a) The runner strips `GIT_EXEC_PATH`, `GIT_PREFIX` and git's PATH prefix from the digest, and
  keeps `LC_CTYPE`.** Push reuse would stay inert on Git for Windows, where every hook carries the
  injected locale, and the runner would carry a list of one caller's additions.
- **(b) The runner also drops `LC_CTYPE`.** A leg reading the locale could then be reused across two
  callers whose locales differ, a false hit traded for a miss.

The pick restores what the caller had, so a locale the caller DID set stays in the key, and the
reconstruction lives in the one program that knows it was started by git.

## 5. Production-readiness checklist

- security: the hook clears an inherited `GATE_REUSE_DIGEST_ENV` for every bar, so the environment cannot hand the runner a digest view; the runner honours the knob only in the hook-set `push` mode.
- perf / scale: one file written by builtins in the hook and one `mapfile` in the runner; no spawn added on the measured fork rows.
- error / empty / loading states: a missing or unreadable view file empties the digest and reuses nothing, with the existing named line.
- observability: the run header's `reuse` key reads `push`, and the ledger records the measured difference S1 restores.
- risks: a leg whose verdict depends on one of git's additions is keyed on the caller's environment, which is the trade the owner ruled on; a git release adding a new variable widens the difference until the table names it.
- testing: the end-to-end arm in S5, and fixture checks per criterion, each observed red on today's code first.
- migration: `REUSE_SCHEMA` moves up by one, so every old entry misses once and ages out under the prune.
- user docs: `tools/run-gates/README.md`'s cache push subsection states the rule.

## 6. Acceptance criteria

Each criterion runs on a hand-built fixture: a scratch repository holding a copy of the runner, the
hook and a two-leg manifest with one `remote` leg, and a local bare remote as `origin`.

- **AC1** — When a fixture bar earns an `ok` from a plain shell, and a commit is then pushed through
  the real `.githooks/pre-push` under a scoped decision, the push bar prints `GATE reuse` for the
  `remote` leg. Red when: it executes the leg, which today's code does because the digest hashes the
  hook's `GIT_EXEC_PATH`, PATH prefix and, on Git for Windows, `LC_CTYPE`.
- **AC2** — When a fixture push runs with a stub bar that copies the file `GATE_REUSE_DIGEST_ENV`
  names, the copy carries no `GIT_EXEC_PATH`, `GIT_PREFIX` or `GIT_CONFIG_PARAMETERS` line, its PATH
  line equals the caller's PATH once each `/bin` component of both is read as `/usr/bin` (rev-2), and with the caller's `LC_CTYPE` unset on node a it carries no
  `LC_CTYPE` line; with the caller's `LC_CTYPE=en_US.UTF-8` that line is present. Red when: any
  addition survives, or the caller's own locale is dropped.
- **AC3** — When a fixture leg prints `$GIT_EXEC_PATH` during a push, its output shows the value
  set. Red when: the restored view reached the legs' environment.
- **AC4** — When a fixture push runs with `GATE_REUSE_DIGEST_ENV` exported by the caller, the hook's
  `not honoured from the environment by this bar:` line names it. Red when: the inherited value
  reaches the bar.
- **AC5** — When a fixture bar runs with `GATE_REUSE=1` and a `GATE_REUSE_DIGEST_ENV` naming a file
  of altered lines, it reuses the entry a plain bar earned. Red when: the env mode reads the file.
- **AC6** — When `grep -n '^REUSE_SCHEMA=' tools/run-gates/run-gates.sh` runs, it prints a value one
  above the one `TOOL-aSparedSpawn-32`'s merge commit holds. Red when: the value is unchanged.
- **AC7** — When `grep -c 'restored' tools/run-gates/README.md` runs, it counts the cache push
  subsection's one statement of the rule. Red when: the README is silent on it.
- **AC8** (rev-2) — When `post-merge.sh` runs with `GATE_REUSE_LINEAGE=1` exported, its
  `not honoured from the environment:` line names `GATE_REUSE_LINEAGE`; and the driver's `_gknobs`
  list, read by the sed the unattended suite's parity arm uses, holds it. Red when: the exported knob
  is not named, which is today's code.
- **AC9** (rev-2) — When the H49 class arm's own predicate, `check_knob_classes`, runs over
  `tools/run-gates/run-gates.sh` with the table and hook constants it reads, it prints nothing.
  Red when: it names an unclassified knob, as it names eight at this unit's base.

## 7. Gates

`pre-push self-test` · `pre-push bar self-test` · `pre-push run-log line` · `push-main self-test` ·
`branch-guard self-test` · `python resolver (behaviour + inline parity + idiom ban)` ·
`lexicon naming predicates` · `transition-audit arms` · `straggler-guard arms` ·
`run-gates evidence` · `run-gates canary` · `run-gates gov canary` · `run-gates turnstile` ·
`run-gates run-log line` · `run-gates adopter e2e` · `profile-bar selftest` ·
`shell hygiene (a fork spent on builtin work)` · `spawn budget (forks per hot entrypoint)` ·
`harness arms (fail branches armed or pinned)`

New arm: .githooks/pre-push.test.sh · covers AC1 AC2 AC3 AC4 AC9 · a direct bar's entry pushed through the real hook, a stub copying the view, a leg printing git's exec path, an inherited view knob, the hook's and the runner's digest patterns compared, the class table's new rows · none
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC5 · the env mode handed a view file · none

## 8. Open questions

- **F1 — How does the reuse digest see a pre-push hook's environment?** The options were (a) strip
  git's additions in the runner and keep `LC_CTYPE`, (b) also drop `LC_CTYPE`, or (c) have the hook
  restore the pre-git environment for the digest. Recommendation at the park: none, since a locale
  entering or leaving the key is a soundness ruling.
  RESOLVED (owner, 2026-10-12): the hook restores the pre-git environment for the digest.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, adopting the owner's ruling on `TOOL-aSparedSpawn-25` (option
  (c)); options (a) and (b) are recorded in §4 Alternatives rejected.
- rev-2 · 2026-10-12 · node a's measured difference (§4, Rev-2) adds the `/bin` reading in the
  runner, matches git's PATH head by `GIT_EXEC_PATH`'s tail, tests Windows by that path's drive letter
  rather than a `git version` spawn, and fixes the view's one write site; AC2 reads PATH under the
  `/bin` rule. S7, S8, AC8 and AC9 adopt the brief's two knob-scrub discoveries left by
  `TOOL-aSparedSpawn-32`'s reconcile.
- rev-3 · 2026-10-12 · the view file lives in the git dir and is removed after the bar and by the
  signal handler, not by the EXIT trap the run-log suite pins (§4, The handoff); the runner's mode
  block moves, unchanged, above the digest, which now reads the mode it decides.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py "restore the caller's environment before git started a hook"`
ranks generic `git` wrappers and `build_git_env` in `tools/memory-tree/tree_lib.py`, a Python
helper that builds a child's git environment and reconstructs no caller's; no existing seam fits.
The hook's own `ENV_CLEARED` scrub and its
`BAR_SCRUBBED_KNOBS` loop are the code this unit extends for the new knob, and `REUSE_DIGEST`'s env
loop in `tools/run-gates/run-gates.sh` is the reader it redirects in the `push` mode.

Recall terms used: REUSE_DIGEST GIT_EXEC_PATH LC_CTYPE GIT_PREFIX pre-push hook environment push reuse
GATE_REUSE_PUSH digest schema caller environment
