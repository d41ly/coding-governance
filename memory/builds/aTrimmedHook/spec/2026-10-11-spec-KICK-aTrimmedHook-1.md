# KICK-aTrimmedHook-1 — manifest-check's staged leg returns at once when nothing it reads is staged

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-2 · base b726385f · streams kickoff · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-KICK-aTrimmedHook-1-1-acceptance-ledger.md](../build/2026-10-11-build-KICK-aTrimmedHook-1-1-acceptance-ledger.md) | journal | — |
| [2026-10-11-prompt-KICK-aTrimmedHook-1-1-build-brief.md](../prompts/2026-10-11-prompt-KICK-aTrimmedHook-1-1-build-brief.md) | journal | — |
| [2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md) | research | TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-2 TOOL-aTrimmedHook-3 |

<!-- /gen:spec-records -->

## 1. Goal

`skills/session-kickoff/manifest-check.sh --staged` runs from the pre-commit hook on every commit,
whatever it stages, and costs 70 s traced on node a for a one-file `RUN.md` commit (2026-10-11, base
profile, 60-80 host bash processes; 114 s untraced in the baseline run). Its answer can only change
when the commit stages the manifest, a watched path or a verify-path. This unit returns at once,
announced, when it stages none of them, and makes the two loops that remain cheap.

## 2. Scope (IN)

- **S1 — the early exit.** Under `--staged`, right after the manifest resolves, the audit block is
  read and `watch:` and `verify-paths:` are split. When the block parsed, both lists are non-empty
  and `git diff --cached --name-only -- "$MF" "${WATCH[@]}" "${VPATHS[@]}"` prints nothing, the
  script prints `NOTE: staged leg skipped — nothing staged touches the manifest, its watch list or
  its verify-paths; the full leg runs at the push boundary` and exits 0. A block that did not parse,
  or an empty list, falls through to the BASE staged leg, which reports it. Observed by AC1 to AC4.
- **S2 — a fork-free reader.** `getval` reads the key from the block text with a bash loop and
  `[[ =~ ]]`, returning the same value the BASE `sed | head | sed` pipeline returns (first match,
  with the whitespace after the colon and at the end trimmed). `read_block` strips CR inside
  its one `awk` instead of piping to `tr`. Both modes. Observed by AC5.
- **S3 — C6 in one spawn.** C6 runs ONE `git ls-files -- "${WATCH[@]}"` and counts each literal
  pathspec's matches from that listing in bash: the entry equal to the spec, or under `<spec>/`. A
  pathspec carrying glob magic (`*`, `?`, `[`, or a leading `:`) and any literal spec counted ZERO
  keep their own `git ls-files` call, so a zero verdict is always git's. Both modes. Observed by AC5
  and AC6.
- **S4 — the arms.** `skills/session-kickoff/manifest-check.test.sh` gains arms for AC1 to AC4 and
  AC6. Observed by AC1 to AC4 and AC6.

## 3. Non-goals (OUT)

- **N1** — no change to which checks the staged leg runs when it does run, or to the full leg's
  checks; C9, C10 and C11 stay full-run only.
- **N2** — C4's per-verify-path loop is not batched; it runs only when the early exit did not fire.
- **N3** — the card verbs (`--card …`, `--locations`, the skeletons) are untouched; they return
  before the manifest checks at BASE and still do.
- **N4** — no change to `KIT_MANIFEST_VERSION` in this pass; the build bumps it once after the last
  unit. `MANIFEST_FORMAT` does not move.
- **N5** — no change to `.githooks/pre-commit`, which still runs this leg on every commit.

### Edges

none

## 4. Design

### Why the exit is sound

Every staged-leg check reads one of three things. C1, C2, C7, C8 and C12 read the manifest file
alone. C4 reads whether each verify-path is tracked. C6 reads whether each watch pathspec matches a
tracked file. C5s reads whether a watched path is staged. A commit staging none of the manifest, the
watch paths and the verify-paths cannot move any of them: `git diff --cached --name-only` lists
deletions too, so a staged deletion of a watched file or a verify-path is "touching" and runs the leg.
A manifest already broken at HEAD no longer reds an unrelated commit; it reds at the push boundary,
where the full leg runs, which is the scope the owner asked for.

### Where it sits

After `MF` resolves and the unmanaged-marker test (~1118-1124 at BASE), before the format warning and
C1. It parses the block with the S2 reader; the parse is repeated by the BASE path when the exit does
not fire, which costs no process after S2.

### The C6 count

`git ls-files -- <specs…>` prints the union of matches. For a literal spec `w`, its matches in that
union are the entries equal to `w` or starting `w/`; git's pathspec semantics for a literal are
exactly those two. The WARN threshold (>100) reads the same count. A literal counted zero in bash is
re-asked of git with its own call before C6 fails, so a case-folding filesystem where git matches and
a byte compare does not cannot produce a red git would not.

### Files touched (estimate)

- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`

### Rollout

Order 1, disjoint from the other three units. `manifest-check.sh` is in the manifest's `watch:`, so
the pass commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md` in the same commit, or
C5s refuses it. The kickoff-manifest version bump is the build's, after the last unit, in every
carrier `tools/check-kit-versions.sh` names.

### Alternatives rejected

- **The owner's wording, manifest or watch only.** A staged deletion of a verify-path that no watch
  pathspec covers would escape C4; adding `verify-paths:` costs nothing.
- **Skip the leg from the hook instead.** The hook cannot read the watch list without parsing the
  manifest, which is this script's job; a second parser is a second reader of one rule.

## 5. Production-readiness checklist

- security — N/A — reads tracked files and the index; no new input surface.
- perf / scale — the skipped path costs the setup, one `awk` and one `git diff`; S2 and S3 save about
  35 s of the full leg too.
- error / empty / loading states — an unparseable block or an empty list never exits early.
- observability — the skip prints one NOTE naming the three inputs and the push boundary.
- risks — a staged-leg check reading an input outside the three would be skipped wrongly; the design
  enumerates every staged-leg check's inputs, and AC2 to AC4 exercise each input class.
- testing — AC1 to AC4 and AC6 are self-test arms; AC5 is a byte comparison of the full leg's output.
- migration — none.
- user docs — the script header's `--staged` usage line names the early exit.

## 6. Acceptance criteria

- **AC1** — When `manifest-check.sh --staged` runs in a fixture repo that stages only a file no watch pathspec or verify-path
  covers and runs `--staged`, the output is the NOTE line and the exit is 0, with the fixture's
  manifest deliberately carrying a C1 placeholder.
  Red when: the placeholder is reported, or the NOTE is absent.
  cost: one fixture repo; seconds.
- **AC2** — When `manifest-check.sh --staged` runs in a fixture repo that stages a watched file with no re-stamp, `--staged` reports C5s.
  Red when: it exits early. Observed RED first with the exit's diff list emptied.
- **AC3** — When `manifest-check.sh --staged` runs in a fixture repo that stages a manifest edit introducing a placeholder, `--staged` reports C1.
  Red when: it exits early.
- **AC4** — When `manifest-check.sh --staged` runs in a fixture repo that stages the deletion of a verify-path, `--staged` reports C4.
  Red when: it exits early.
- **AC5** — When `bash skills/session-kickoff/manifest-check.sh` runs with no argument on the real
  tree at BASE and after this unit, the outputs are byte-identical, and `--staged` with the
  manifest staged is too.
  Red when: any byte differs.
- **AC6** — When `manifest-check.sh` runs on a fixture manifest naming a watch pathspec matching nothing, C6 still reports
  it, and a glob pathspec still counts through git.
  Red when: the dead pathspec passes.

## 7. Gates

`kickoff-manifest ratchet` · `manifest-check self-test` · `scratch-guard self-test` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates`

New arm: skills/session-kickoff/manifest-check.test.sh staged early exit · covers AC1 AC2 AC3 AC4 AC6 · the exit's diff list emptied, and the C6 zero-confirm removed · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the brief and the base profile.
- rev-2 · 2026-10-11 · the acceptance witnesses name the checker run on a fixture, not the suite that hosts the fixture, after `--dispatch`'s spec-token check refused the suite form; §7 names `scratch-guard self-test`, whose guard `manifest-check.sh` trips

## 10. Reuse audit

No seam to extend beyond the script's own: S1 reuses `read_block`, `getval` and `splitspecs`, and
S3 keeps C6's verdicts. `python tools/codebase-map/reuse_lookup.py "skip a staged pre-commit check when
nothing it watches is staged"` returned only name-stem matches (`check`, `pre`, `skip`,
`build_commit`). Recall returned the `KICK-cKeyedLaunchpad-1` review, which kept C9 out of the staged
leg because the hook fires on every commit, the same reason this unit exists.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
