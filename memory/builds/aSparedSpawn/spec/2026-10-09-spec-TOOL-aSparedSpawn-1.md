# TOOL-aSparedSpawn-1 — the reuse key hashes what a dirty guarded file holds, and the toolchain it ran under

**Status:** OPEN · rev-1 · 2026-10-09 · node a · Tier-2 · base 22efab65 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`GATE_REUSE=1` today reuses a green for bytes that never ran: a guarded leg's `input_key` takes the
porcelain LINE of a dirty guarded file, and ` M tools/x.sh` reads the same after a second unstaged edit.
This unit makes the key take the content of every dirty and untracked guarded file, plus one digest of
the toolchain, environment and host class, plus a `REUSE_SCHEMA` constant. It is a correctness fix that
every later reuse unit builds on, so it lands first.

## 2. Scope (IN)

- **S1** — One walk at run start, beside `PORCELAIN_START` (`run-gates.sh:1955`): `git status
  --porcelain -z --untracked-files=all`, parsed with builtins into `<XY> <path>` rows (a rename's
  source field consumed, not read as a path), then ONE `git hash-object --stdin-paths` over the
  dirty paths that still exist. Each row becomes `<XY> <blob-or-dash> <path>`. The walk is skipped on
  a clean tree. Observed by AC1, AC2 and AC6.
- **S2** — `input_key`'s guarded branch (`run-gates.sh:2196-2215`) takes its dirt share from those
  rows, selected with the guard's pathspec semantics (`p == g`, or `p` under `g` when `g` ends in `/`),
  in place of the `grep -F` substring match over status lines. The `git ls-files -s` component is
  unchanged. Observed by AC1 and AC2.
- **S3** — `gate-fingerprint.sh`'s WORKING-TREE form walks with `--untracked-files=all` in both of its
  status calls, so a file inside an untracked directory is content-hashed rather than collapsed into a
  `?? dir/` line its `[ -f ]` test skips. The at-a-rev form is untouched, so the clean-tree equality
  `.githooks/pre-push` relies on holds. This is the same class as S2 on the unguarded key, which is
  the whole-tree fingerprint. Observed by AC3.
- **S4** — A toolchain, environment and host digest, computed ONCE per run before the first key and
  appended to every key, guarded and unguarded. Observed by AC4.
  - bash: `BASH_VERSION` and `MACHTYPE`, builtins.
  - the MSYS or Cygwin runtime: the first line of `/proc/version`, read with `read`, where it exists.
  - python: `PYBIN`'s path plus `sys.version` and `sys.flags.utf8_mode`, printed as one more line by
    the legs-parse python the run already starts, so no new python.
  - git: `git version` and `git config --get-regexp '^core\.(autocrlf|eol)$'`, two spawns per bar.
  - every other tool a leg names (`node` among them): its resolved location through `type -P`.
  - the environment the legs inherit, read after the runner's own unsets: the name and value of each
    variable matching `GATE_* GOV_* *_PY GIT_* PYTHON* LC_* LANG TZ PATH`, sorted, except `GATE_REUSE`.
- **S5** — A source constant `REUSE_SCHEMA`, hashed into every key. A runner change that redefines
  what a reusable `ok` means bumps it, which misses every recorded row at once. Observed by AC5.
- **S6** — `tools/run-gates/README.md`'s reuse section and its `gate-fingerprint.sh` row say what the
  key takes, what it does not, and the in-place-upgrade gap S4 leaves. NOT OBSERVED: prose, which no
  checker grades beyond the line-length and spec-token legs.

## 3. Non-goals (OUT)

- No change to WHO may reuse. `GATE_REUSE` stays opt-in, `.githooks/pre-push` keeps scrubbing it
  (`BAR_SCRUBBED_KNOBS`, `pre-push:1421`), and a run that reused anything still cannot stamp
  `gate-full-green`.
- No `reads` classes, no `BASE` out of the default key, no common-dir cache, no soundness sample. Those
  are the reuse report's U1 to U3 and sit with content-addressed reuse.
- No precompute of the keys once per bar. That is the runner spawn cut's, which must reproduce this
  definition byte for byte.
- No environment scrubbing of a leg to the hashed allowlist (Turborepo's strict mode). The report
  records it as a follow-up; it changes what every leg sees and is not a key fix.

### Edges

- **hands-off** `TOOL-aSparedSpawn-13` — content-addressed reuse keyed on declared read classes, built on
  this key once it is sound; a cache over an unsound key would launder stale greens across worktrees.
- **hands-off** `TOOL-aSparedSpawn-4` — computing every key once per bar instead of per leg; that unit
  re-implements the definition S1 to S5 fix here and proves parity against it.

## 4. Design

**The defect, re-verified at base 22efab65.** `input_key` (`run-gates.sh:2196`) builds a guarded
leg's component from `git ls-files -s -- <guards>` plus `$PORCELAIN_START` lines that `grep -F`
matches against each guard (`:2204-2207`). `PORCELAIN_START` is `git status --porcelain | sort`
(`:1955`). Neither carries content, so edit-run-edit on an unstaged guarded file keeps the key. The
original spec, `TOOL-aPacedTurnstile-6` S2, asked for "the path-and-blob-hash list"; the build
shipped status lines and said why in the comment above `input_key` ("reads no file content").

**A second instance, found while re-verifying.** Probed in a scratch repo on node a: a new file in a
new directory reports as `?? d/` under the default `-unormal`, and only `-uall` lists `?? d/f`.
`gate-fingerprint.sh`'s working-tree form hashes each porcelain path that passes `[ -f "$p" ]`, so a
directory entry is skipped and the file's content never reaches the digest. The unguarded key IS that
digest (`input_key`'s else branch), so the same stale reuse reaches every unguarded leg.

**The walk.** One `-z -uall` status at start feeds three readers: `TREE_CLEAN` (still "the listing is
empty"; `-uall` cannot make an empty listing non-empty), the per-leg dirt slice, and nothing else.
Content is hashed at START, the same instant `FPRINT_START` is taken, so a file edited while a leg runs
cannot give the earning row a key for bytes the leg did not read. A deleted path carries a dash for its
blob; its absence is already in the `XY` field.

**The digest** is one `git hash-object --stdin` over the S4 lines in a fixed order, held in a global
and appended to each key's input as a fourth `---` section, after `REUSE_SCHEMA`. Excluding
`GATE_REUSE` is what lets the earning run (unset) and the reusing run (set) agree; every other knob
stays in, which makes the key over-sensitive on purpose — a width change is a cache miss, never a
false hit.

**Migration.** Every recorded ledger key misses once, which is the "did more work" direction the reuse
block already promises. No reader parses the key, so its new shape breaks nothing.

### Files touched (estimate)

- `tools/run-gates/run-gates.sh` — the start-of-run walk, `input_key`, the digest, `REUSE_SCHEMA`.
- `tools/run-gates/gate-fingerprint.sh` — `--untracked-files=all` in the working-tree form.
- `tools/run-gates/run-gates.evidence.test.sh` — the arms beside the existing reuse arms (`ru_repo`).
- `tools/run-gates/README.md` — the reuse section and the fingerprint row.
- `tools/run-gates/kit.toml` — the kit version, moved once for the build per the bump-once rule.

### Alternatives rejected

- **Hash each guarded file per leg.** The comment above `input_key` rejected it for re-reading the
  tree per leg. One `--stdin-paths` over the dirty set at start hashes only what is dirty, once.
- **`--untracked-files=all` in the runner only.** It leaves the unguarded key, which is the
  fingerprint, with the same hole; S3 is one flag in the file that owns the digest.
- **A strict environment allowlist of named variables.** It misses the next variable someone adds;
  the prefix set with one exclusion fails toward a miss instead.
- **`git --version` replaced by `type -P git`.** A path cannot see an in-place upgrade, and git's
  behaviour reaches nearly every leg, so git pays its one spawn; lesser tools take the path only.
- **The runner's own blob in the key instead of `REUSE_SCHEMA`.** Every comment edit would invalidate
  every row, and the runner's comments move in most builds.

## 5. Production-readiness checklist

- security: the key decides whether a leg is skipped, so an unsound key is a coverage hole; S1 to S5 close the two found and keep pre-push's scrub.
- perf / scale: one status walk plus one `hash-object` on a dirty tree, two git spawns for the digest; a huge untracked tree pays `-uall`.
- error / empty / loading states: a failed walk or digest yields an empty component, which makes the key a dash and never matches.
- observability: the run header gains a `reuse_schema` key beside `fingerprint`, additive, so a reader can tell a schema miss from a content miss.
- risks: `-uall` changes the fingerprint of a dirty tree, read only by `tree_moved` and the unguarded key; the pre-push at-a-rev compare is clean-tree only.
- testing: arms in the evidence suite with a positive control each, plus a fingerprint arm; every new arm observed red on its staged break first.
- migration: recorded ledger keys miss once and are rewritten by the next executed run; nothing else reads them.
- user docs: `tools/run-gates/README.md` reuse section and fingerprint row (S6).

## 6. Acceptance criteria

- **AC1** — When a `ru_repo` fixture earns a green with `ga/f` edited and unstaged, then `ga/f` is edited
  again unstaged and the run repeats with `GATE_REUSE=1`, leg `pa` prints `GATE ok` and its sibling `pb`
  prints `GATE reuse`. Red when: `input_key` keys the dirt by its status line and `pa` is reused.
- **AC2** — When the same arm adds an untracked file inside a new untracked directory under `ga/`
  between the earning and the reusing run, then changes only that file's content and runs again,
  `pa` executes both times and `pb` is reused. Red when: the walk runs without `--untracked-files=all`.
- **AC3** — When `gate-fingerprint.sh` runs with no argument in a fixture holding a file inside an
  untracked directory, before and after that file's content changes, the two digests differ, and on a
  clean tree it still equals the `HEAD` form. Red when: the working-tree walk collapses the directory.
- **AC4** — When an earning run and a reusing run differ only in `PYTHONUTF8`, no leg is reused; when
  they differ only in `GATE_REUSE`, the existing precondition arm still sees every pure leg reused.
  Red when: the digest omits the environment, or hashes `GATE_REUSE` and the precondition arm reds.
- **AC5** — When a fixture copy of the runner has its `REUSE_SCHEMA` value changed between the earning
  and the reusing run, `GATE reuse` appears on no line. Red when: the constant is not in the key.
- **AC6** — When the reusing run follows an earning run on a dirty tree whose guarded file was only
  re-saved with identical bytes (`touch ga/f`), both legs print `GATE reuse`. Red when: the key reads
  mtime or status churn, so a content key never fires on a dirty tree.
  cost: each arm drives the real runner two or three times on a scratch repo, seconds quiet and
  tens of seconds on a loaded node `a`.

## 7. Gates

`run-gates evidence` · `run-gates canary` · `run-gates turnstile` · `run-gates run-log line` ·
`run-gates gov canary` · `run-gates adopter e2e` · `profile-bar selftest` · `pre-push run-log line` ·
`push-main self-test` · `check-wiring self-test` · `settings-merge selftest` ·
`foreign-prefix parity (every self-test at three prefixes)` ·
`python resolver (behaviour + inline parity + idiom ban)` · `install-prefix self-test` ·
`dead-path carriers self-test` · `lexicon naming predicates` · `spec-tokens self-test` ·
`kit-placeholders self-test` · `harness arms (fail branches armed or pinned)` ·
`shell hygiene (a loop fed by a command substitution)` · `codebase-map coverage + freshness` ·
`testsuite counts (every bar self-test prints one)` · `line length` · `memory hygiene` ·
`spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC1 AC2 AC4 AC5 AC6 · the porcelain-line key, the default-mode walk, an env-blind digest and a schema-blind key, each staged on a fixture copy of the runner · its `FLOOR_ASSERTIONS` rises by the assertions added
New arm: tools/run-gates/run-gates.evidence.test.sh · covers AC3 · the working-tree form without `--untracked-files=all` · same floor

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "hash dirty working-tree file content into a reuse key"`
ranked only name-token neighbours (`tree`, `key`, `load_map_tree`) and no hashing seam; the seam this
unit extends is the one the reuse report names, `gate-fingerprint.sh`'s working-tree form, which
already hashes dirty blobs and is `input_key`'s unguarded component, with `input_key` itself the reader.
Prior record: `TOOL-aPacedTurnstile-6` S2 specified the blob list this unit restores.

Recall terms used: GATE_REUSE input key ledger guard porcelain fingerprint reuse unit impure full-green stamp
