# TOOL-dSafePassage-74 — the introducing commit is found by the TOML parse alone, so a row id in any string spelling the reader accepts is found

**Status:** DEFERRED · rev-3 · 2026-10-28 · node a · Tier-2 · base 83817478 · streams tooling · order 16 · advances TOOL-dSafePassage-14

**Derived:** TOOL-dSafePassage-1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dSafePassage-72-spec-brief.md) | research | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-75 |
| [2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-72 TOOL-dSafePassage-73 TOOL-dSafePassage-75 TOOL-dSafePassage-76 TOOL-dSafePassage-77 TOOL-dSafePassage-78 TOOL-dSafePassage-80 TOOL-dSafePassage-81 TOOL-dSafePassage-82 TOOL-dSafePassage-83 |

<!-- /gen:spec-records -->

## 1. Goal

`derive_introduced` parses a declaring blob only where its raw text holds the id in double quotes
(`tools/govkit/upgrade_steps.py:963`). `read_steps` parses with `tomllib` and accepts any TOML
string, so a row written `id = 'lib/x-1'`, `id = '''lib/x-1'''` or with an escape such as
`"lib/x-1"` is read but never found in history. It reads `unlanded`, sorts after every landed
row, and `derive_reverse_steps` downs it on every rollback whatever `--to` says. This unit closes H4
(id 8) of the closing diff review, round 1: the parse decides, with no raw-text test in front of it.

## 2. Scope (IN)

- **S1** — The parse decides. In `derive_introduced` (`tools/govkit/upgrade_steps.py:911-980`),
  each declaring blob the walk reads is parsed with `tomllib`, and an id counts as held where a
  `[[<table>]]` row's parsed `id` equals it, as the code after the test already does
  (`:966-974`). The raw-text test at `:963-965` is not kept, and `for i in hits:` becomes
  `for i in want & held:`, a new set, because the loop's body discards each found id from `want`
  and iterating `want` itself would raise on the change in size. Observed by AC1 and AC2.
- **S2** — Three readers inherit it. `read_steps` (`:861-864`) and `read_retired` (`:907-908`) call
  `derive_introduced`, so a succession row's derived commit is found in any spelling too, and so
  does `resolve_shim_landing` (`tools/govkit/shims.py:330`), so a `[[shim]]` id lands in any
  spelling. Observed by AC2 for the first two; the third is NOT OBSERVED by a new criterion, for
  the reason §3 gives.
- **S3** — The docstring. `derive_introduced`'s last sentence, "a blob is parsed only where it
  spells a wanted id" (`:919-920`), says every declaring blob is parsed and the walk still stops
  at the last hit. Observed by AC3.

## 3. Non-goals (OUT)

- A rule that refuses a row id not spelled as a basic string. The review offers it as an
  alternative; §4 rejects it.
- `check_frozen` and the step gate. They compare parsed rows and never read raw text, so they need
  no change.
- `help/upgrade-steps.md`. Its opening paragraph already says the introducing commit is the first
  first-parent commit that holds the row (lines 7-9), which is what the code will now do.
- A criterion of its own for the shim reader. gov declares no `[[shim]]` row
  (`tools/govkit/shims.toml` holds none at `83817478`), so no shim id is walked today. The shims
  kit's own window plants, `window-prefix-id` and `window-comment-id`
  (`tools/govkit/shims.py:525-538`), drive `resolve_shim_landing` over double-quoted ids and a
  comment that spells one, and both read the same under a parse with no raw-text test in front of
  it. That agrees with the function's own docstring (`:317-319`), which promises the row with
  exactly that id and never a substring search.

### Edges

none

Read and closed, so named here rather than joined: TOOL-dSafePassage-1's derived introducing
commit and its reader; TOOL-dSafePassage-26 S37's walk over each vintage's declaring files; and
TOOL-dSafePassage-4's `derive_reverse_steps`, which downs an `unlanded` row. The edge join counts
CLOSED specs, and a CLOSED spec cannot take the matching `hands-off` line.

## 4. Design

### Observed at base

A scratchpad probe on node a on 2026-10-28 committed one `steps.toml` holding four rows, each id
spelled one way, and called `derive_introduced(g, "HEAD", ["steps.toml"], "upgrade", ids)` at
`83817478`.

| Spelling | Found at base | Found under a prefilter widened to both quotes |
|---|---|---|
| `id = "lib/dq-1"` | yes | yes |
| `id = 'lib/sq-1'` | no | yes |
| `id = '''lib/ml-1'''` | no | yes |
| `id = "lib/esc-1"` | no | no |

The fourth row is why the test goes rather than widens. A basic string may spell any character
by escape, `ID_RE` checks the decoded value, so no raw-text test short of the parser accepts every
spelling the parser accepts.

### What the parse costs

The same probe counted `tomllib.loads` calls over gov's own history, with the test and without it,
on 2026-10-28 (PINNED).

| Landed ref | With the test | Without it |
|---|---|---|
| `HEAD` | 105 parses | 368 parses |
| `origin/main` | 97 parses | 359 parses |

Process time measured 1.06 to 1.80 s for every variant, with no ordering between them. The walk's
cost is `git log` and `cat-file --batch`, which the test never avoided, since every changed
declaring blob is read before the test runs (`:950`). The shim walk is not measured: with no
`[[shim]]` row declared, `resolve_shim_landing` is called for no id outside its own plants.

### Inventory

Minted: the arm tag `[dSP-74]`. No function, `Refusal` site, conf key, gate leg or constant.

### Migration

None. A receipt records `introduced` as the walk derived it. A row a past walk recorded as
`unlanded`, written as `null`, keeps `null`, and no shipped row is spelled other than in double
quotes (`tools/govkit/steps.toml`, `tools/*/kit.toml` at `83817478`).

### Rollout

Live at landing, in order 16 with TOOL-dSafePassage-72, -73 and -75, sequenced by M6 because all
four write `tools/govkit/upgrade_steps.py` and `tools/govkit/selftest.py`.

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`

### Alternatives rejected

- **Widen the test to both quote styles.** It misses an escaped basic string, as the probe's fourth
  row shows.
- **Test for the bare id with no quotes.** It also misses the escaped row.
- **Make `read_steps` refuse an id not spelled as a basic string.** A second reader of the raw text
  beside the parser, to keep a prefilter whose saving the measurement above does not show.

## 5. Production-readiness checklist

- security: N/A — no path, spawn, input or environment changes. The parse already ran on every
  blob the test admitted.
- perf / scale: about 3.5 times the parses over gov's history, with no measurable change in time
  (§4).
- error / empty / loading states: an unparsable vintage still holds no row (`:969-970`).
- observability: `list` prints each row's introducing commit, so a row that reads `unlanded` is
  visible.
- risks: a vintage whose TOML the parser refuses was skipped by the test before the parse when it
  did not spell an id. It is now parsed and skipped by the same `except`.
- testing: the `[dSP-74]` arm in `check_upgrade_steps`, under §7's `New arm:` line.
- migration: none.
- user docs: N/A — `help/upgrade-steps.md` lines 7-9 already state the rule the code now meets.

## 6. Acceptance criteria

- **AC1** — When the probe below commits one `steps.toml` holding a row in each of the four
  spellings of §4 and calls `derive_introduced` over it, it prints
  `['lib/dq-1', 'lib/esc-1', 'lib/ml-1', 'lib/sq-1'] True`: every id is found, at that commit.
  Red when: the raw-text test stays, so only `lib/dq-1` is found, as at base; or it is widened to
  quotes, so `lib/esc-1` is not.

  ```python
  import pathlib, subprocess, sys, tempfile
  sys.path.insert(0, "tools/govkit")
  import upgrade_steps as us
  bs = chr(92)
  rows = {"lib/dq-1": '"lib/dq-1"', "lib/sq-1": "'lib/sq-1'",
          "lib/esc-1": '"lib' + bs + 'u002Fesc-1"', "lib/ml-1": "'''lib/ml-1'''"}
  with tempfile.TemporaryDirectory() as td:
      g = pathlib.Path(td)
      def git(*a):
          return subprocess.run(["git", "-C", td, "-c", "commit.gpgsign=false", "-c",
                                 "core.hooksPath=" + td, *a], capture_output=True, text=True,
                                check=True).stdout.strip()
      git("init", "-q", "-b", "main"); git("config", "user.email", "t@e"); git("config", "user.name", "t")
      (g / "steps.toml").write_text("".join(f"[[upgrade]]\nid = {v}\n\n" for v in rows.values()),
                                    encoding="utf-8")
      git("add", "-A"); git("commit", "-q", "-m", "rows")
      got = us.derive_introduced(g, "HEAD", ["steps.toml"], "upgrade", list(rows))
      print(sorted(got), all(v[0] == git("rev-parse", "HEAD") for v in got.values()))
  ```

- **AC2** — When `check_upgrade_steps`' scratch gov holds a descriptor row `id = 'demo/single'`
  committed after a double-quoted row, and a `[[retired]]` row whose `id` is single-quoted, then
  `read_steps(g, "HEAD", "main")` gives `demo/single` its committing sha, never `unlanded`, and
  orders it after the earlier row; and `read_retired(g, "HEAD", "main")` gives the retired row its
  committing sha.
  Red when: either reader still reads a single-quoted row `unlanded`.
  fixture: the scratch gov `build_steps_gov` builds (`tools/govkit/selftest.py:2895-2912`), with
  `render_row`'s double-quoted `id` (`:2922-2927`) as the control.
- **AC3** — When `git grep -n -F "f'\"{i}\"' in text" -- tools/govkit/upgrade_steps.py` and
  `git grep -n "parsed only where" -- tools/govkit/upgrade_steps.py` run, each prints nothing.
  Red when: the raw-text test itself, or the docstring's claim about it, is kept. A correct rewrite
  of the loop does not trip it, since neither pattern is a substring of `for i in want & held:`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `recall floor arms` · `policy fixtures` · `step-rows-frozen` · `upgrade-walk` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC2 · `check_upgrade_steps` gains `[dSP-74]` checks, a single-quoted step row and a single-quoted `[[retired]]` row each committed on the scratch gov; observed RED at base 83817478, where both read `unlanded`, and GREEN after the build · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, closing H4 (id 8) of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-1-71-closing-diff-round1.md`,
  by `memory/builds/dSafePassage/prompts/2026-10-28-prompt-TOOL-dSafePassage-72-1-spec-writer.md`.
- rev-2 · 2026-10-28 · §7 · the leg line names `policy fixtures`, the leg whose guard
  `tools/govkit/selftest.py`, listed in §4's files touched, trips.
- rev-3 · 2026-10-28 · S1 · S2 · §3 · §4 · AC3 · folded L2 and L13 of
  `memory/builds/dSafePassage/reviews/2026-10-28-review-TOOL-dSafePassage-72-73-74-75-76-77-78-80-81-82-83-spec-audit-round1.md`:
  S1 spells the loop as `for i in want & held:` and AC3 greps the raw-text test itself;
  S2 names `resolve_shim_landing` as a third reader, §3 says why it takes no criterion
  and §4 says its walk is unmeasured. The header's node reads `a`, the host the probes ran on.

## 10. Reuse audit

The seam extended is `derive_introduced` itself (`tools/govkit/upgrade_steps.py:911-980`), the one
derivation both `read_steps` and `read_retired` call. Its parse-and-compare already exists below
the test, so S1 keeps that half and lets it see every blob. `python tools/codebase-map/reuse_lookup.py
"find the commit that introduced a TOML row id along first-parent history"` ranked `rows`, `row`,
`build_commit`, `extract_row`, `load_toml` and `write_commit`, all name-token matches, none a history
derivation, so no existing seam fits beyond the function itself. A `git grep` for a quoted-id test
of the same shape (`f'"{i}"' in`) over `tools/govkit/`, `tools/lib/` and `tools/push-main.sh` found
this one site alone. The recall probe ranked the review's H4 second and TOOL-dSafePassage-20's
reading of the derived commit third; neither names another prefilter.

Recall terms used: `python tools/memory-recall/query.py "how is a step row's introducing commit derived from history and why does a blob get parsed" --terms "derive_introduced introducing commit first-parent blob prefilter tomllib unlanded quote spelling read_steps retired"`
