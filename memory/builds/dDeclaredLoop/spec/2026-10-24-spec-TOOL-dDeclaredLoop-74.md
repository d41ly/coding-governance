# TOOL-dDeclaredLoop-74 — a FETCH_HEAD counts as a fetch only when it holds the default branch of the resolved remote

**Status:** CLOSED · rev-3 · 2026-11-17 · node d · Tier-2 · base ed497191 · streams tooling · order 38 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-68-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 |
| [2026-10-24-build-TOOL-dDeclaredLoop-74-deviation-741.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-74-deviation-741.md) | deviation | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-74-1-acceptance-ledger.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-74-1-acceptance-ledger.md) | journal | — |
| [2026-11-17-build-TOOL-dDeclaredLoop-74-deviation-742.md](../build/2026-11-17-build-TOOL-dDeclaredLoop-74-deviation-742.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-68-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-74-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-74-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-dDeclaredLoop-74-reground-brief.md](../prompts/2026-11-16-prompt-TOOL-dDeclaredLoop-74-reground-brief.md) | research | — |
| [2026-11-17-prompt-TOOL-dDeclaredLoop-74-build-brief.md](../prompts/2026-11-17-prompt-TOOL-dDeclaredLoop-74-build-brief.md) | journal | — |
| [2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-75 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round1.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |
| [2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md](../reviews/2026-11-17-review-TOOL-dDeclaredLoop-1-closing-diff-round2.md) | diff-review | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-40 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 TOOL-dDeclaredLoop-68 TOOL-dDeclaredLoop-69 TOOL-dDeclaredLoop-70 TOOL-dDeclaredLoop-71 TOOL-dDeclaredLoop-72 TOOL-dDeclaredLoop-73 TOOL-dDeclaredLoop-75 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-77 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 TOOL-dDeclaredLoop-80 TOOL-dDeclaredLoop-81 TOOL-dDeclaredLoop-82 TOOL-dDeclaredLoop-83 TOOL-dDeclaredLoop-84 TOOL-dDeclaredLoop-85 TOOL-dDeclaredLoop-86 TOOL-dDeclaredLoop-87 TOOL-dDeclaredLoop-88 TOOL-dDeclaredLoop-89 TOOL-dDeclaredLoop-90 TOOL-dDeclaredLoop-91 TOOL-dDeclaredLoop-92 TOOL-dDeclaredLoop-93 TOOL-dDeclaredLoop-94 TOOL-dDeclaredLoop-95 TOOL-dDeclaredLoop-96 TOOL-dDeclaredLoop-97 TOOL-dDeclaredLoop-98 TOOL-dDeclaredLoop-99 TOOL-dDeclaredLoop-100 TOOL-dDeclaredLoop-112 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-57-spec-audit.md`)
confirmed finding **id 45 at HIGH**, its item **H7**; its other-branch half is item M6 at medium (id 8),
batched into `TOOL-dDeclaredLoop-75`. `TOOL-dDeclaredLoop-65` S1 takes the mtime of every `FETCH_HEAD`
under the common git directory as a fetch time, with no look at the file's content. A failed fetch, an
unreachable remote or a branch that does not exist, empties `FETCH_HEAD` and gives it a current mtime
(§4 "Evidence"). So an offline run reads its tracking ref as fetched just now `from FETCH_HEAD`, and the
engine ranks `act` above `stale-remote` on a stale base. 65's AC3 dates a valid `FETCH_HEAD` back and
cannot see it.

This unit makes the file's content validate its mtime. It repairs `TOOL-dDeclaredLoop-65`.

## 2. Scope (IN)

- **S1** — In `tools/loop/position.py`, a `FETCH_HEAD` joins the population of 65 S1 only when it is
  non-empty and holds a line `<sha>\t<flag>\tbranch '<default>' of <url>` for the default branch of the
  resolved remote, where `<url>`, spelled by the new `derive_fetch_url`, equals the spelling of
  `git remote get-url <remote>`. `derive_fetch_url` strips one trailing `/` and then one trailing `.git`.
  The test is the new `check_fetch_head`, which answers the empty string for a kept file and the skip
  reason otherwise: `empty`, or `no line for <default> of <remote>`; a file `os.stat` answers but that
  cannot be opened reads `unreadable`. A skipped file's time is never read, by 65 S2's fallback or
  otherwise. Observed by AC1, AC2, AC3.
  **Readers:**
  by name: `tools/loop/position.py`, its fetch-time reader, the one reader of the population
  by value: `tools/loop/position.py`, its answer derivation through the remote claim's verdict and its plant checks
- **S2** — Each skipped file prints one entry on the read list, right after the tracking ref's entry:
  `<name> · skipped — <reason>`, where `<name>` is the file's path under the common directory in `/`
  form, `FETCH_HEAD` or `worktrees/<w>/FETCH_HEAD`. It names the remote by name and never prints a URL.
  With every `FETCH_HEAD` skipped, the reading falls to 65's other sources, the tracking ref's reflog
  and, where the population is then empty, the clone entry, as 65 S2 says. Observed by AC1, AC3.
- **S3** — The plant `failed-fetch` joins `PLANTS`, listed ahead of `plan-line` and `status-line` so
  those two stay the last two, staged as §4 "The plant" gives: an aged tracking ref, then a fetch from a
  path that does not exist. Its check owes the answer `stale-remote`, the entry
  `FETCH_HEAD · skipped — empty` and the tracking ref's entry ending `from reflog`, and it prints one
  in-process probe of `check_fetch_head` over a `main` line fetched from a second URL. Observed by AC1,
  AC3.
- **S4** — `help/loop.md`'s `stale-remote` paragraph states that a `FETCH_HEAD` counts only when it holds
  the default branch fetched from the remote's own URL and that a skipped one prints its own `read —`
  line, and its fixture list names `failed-fetch`. The module docstring of `position.py` states the same
  test in the answer's `stale-remote` clause, and its "WHAT THIS DOES NOT CHECK" paragraph names, in the
  place 65 S5 gave an unread `FETCH_HEAD` content, a `FETCH_HEAD` whose URL git spelled otherwise than
  the configured URL past one trailing `/` and `.git`, which reads skipped. Observed by AC4.
  **Readers:**
  by name: `tools/loop/position.py`, its module docstring
  by value: NO VALUE READERS — prose a person reads; no code parses the docstring or the page's paragraph

## 3. Non-goals (OUT)

- The other-branch fetch's own plant: the audit's id 8, batched into `TOOL-dDeclaredLoop-75`. S1 already
  skips that file; the plant is that unit's.
- The relative `--git-common-dir` and the fixture's inherited git config: ids 15 and 25, batched into
  `TOOL-dDeclaredLoop-75`.
- A URL carrying a user part, an scp form or a token: `TOOL-dDeclaredLoop-77` spells it through
  `derive_fetch_url`. Until it lands such a remote's `FETCH_HEAD` reads skipped, the conservative side.
- A `--explain` flag: the skip entries ride the read list every line output already prints (§8 F2).
- A checklist entry that a freshness signal taken from an mtime is validated by content, the finding's
  left-shift: the class is recorded at the close; S3 is this reading's failed-writer fixture.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-65` — the last-fetch population of S1 in `tools/loop/position.py`, whose `FETCH_HEAD` members this unit validates by content
- **hands-off** `TOOL-dDeclaredLoop-75` — the validated population, beside which that unit plants the other-branch fetch, resolves the common directory absolutely and isolates the fixture's git config (ids 8, 15, 25)
- **hands-off** `TOOL-dDeclaredLoop-77` — S1's URL normalisation, which that unit spells as git writes the URL into `FETCH_HEAD`, its user part stripped from both sides (the round-4 spec audit's id 8)

## 4. Design

### Evidence

- Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch clone under `%TEMP%`: PINNED, that
  date. After `git fetch`, `FETCH_HEAD` held `<sha>\t\tbranch 'main' of C:/Users/.../up` and a
  `not-for-merge` line for the other branch; `git fetch origin other` rewrote it to the single line
  `branch 'other' of ...`; with the remote's URL set to `.../up/` the line still read `of .../up`; and
  with the URL pointed at a path that does not exist, `git fetch` exited 128 and left `FETCH_HEAD` at
  0 bytes: PINNED, that date.
- This pass could not re-run the probe: the worktree it ran in refuses a git command aimed at a scratch
  repository outside it. AC1 and AC2 re-observe it at the close, and a git that writes otherwise turns
  them red.
- Read through `git show` at the branch tip `e0a7e54b3`:
  - `tools/loop/position.py#read_remote_claim` still reads the tracking ref's age from its newest reflog
    entry alone; `tools/loop/position.py#derive_position_into`, its one caller, appends `<ref>@<sha8>` to
    the read list where the sha resolves, and `tools/loop/position.py#render_position_lines` prints each
    entry as `read — <entry>`. 65's `read_fetch_time` is unbuilt there, so this design is written on
    `TOOL-dDeclaredLoop-65` rev-3 §4 "The reading" and on `TOOL-dDeclaredLoop-56` rev-6 S36.
  - `position.py` has no `--explain` flag; the `script:{prefix}/loop/position.py` row of
    `tools/govkit/usage.toml` lists `--json`, `--next-line`, `--frontier`, `--check-refusal=`,
    `--fixture`, `--plant=` and `--selftest`.
  - `tools/loop/claims.py#resolve_remote` answers the remote, the default branch, the observed branch
    and a refusal. `tools/loop/loop_witness.py#read_git` returns the exit and stdout and raises nothing;
    `tools/loop/loop_witness.py#run_fixture_git` raises on a failed git.
  - `PLANTS` holds 21 PINNED plants, `plan-line` and `status-line` last.
  - The read list's other readers: `tools/loop/composition.py#run_composition_plant` asks whether one
    `composition@` entry is a member, and `tools/loop/position.py#check_plant`'s `steps` entry whether
    any entry opens `memory/`.

### The reading, restated

```
read_fetch_time(repo, remote, ref, branch) -> (at, source, skipped)     # 65's, extended
  want = None                                                            # read once, where a FETCH_HEAD exists
  for f in common/FETCH_HEAD, sorted(common/worktrees/*/FETCH_HEAD) where os.stat(f) answers:
      if want is None: rc, url = read_git(repo, "remote", "get-url", remote); want = derive_fetch_url(url) if rc == 0 else ""
      why = "unreadable" where f cannot be opened, else check_fetch_head(text of f, remote, branch, want)
      if why: skipped.append("%s · skipped — %s" % (f relative to common, "/" form, why)); continue
      times.append((mtime of f, "FETCH_HEAD"))
  then 65's reflog source, and its clone fallback where times is empty, unchanged

check_fetch_head(text, remote, branch, want) -> "" or the reason
  "empty" where text holds no non-blank line
  "" where some line matches ^[0-9a-f]{40,64}\t[^\t]*\tbranch '<re.escape(branch)>' of (.+)$
     and want and derive_fetch_url(group 1) == want
  "no line for <branch> of <remote>" otherwise

derive_fetch_url(url): one trailing "/" stripped, then one trailing ".git"
```

`read_remote_claim` passes the remote it already resolves. Its second value becomes the list of read
entries, the tracking ref's entry of 65 S3 first and the skip entries after it, and
`derive_position_into` extends the read list with it where it appended one entry. Where 65's built shape
differs from its rev-3 text, the skip entries join the read list right after the tracking ref's entry.

### The plant

| Plant | Staged | Owed |
|---|---|---|
| `failed-fetch` | the restaged `stale-remote` scratch of 56 S36, whose tracking ref's newest reflog entry is older than the bound and which holds no clone entry and no `FETCH_HEAD`; `git remote set-url origin <top>/gone.git`, a path that does not exist; then `git fetch -q origin` in `r` through `read_git`, whose exit is owed nonzero; the engine reads `r` | the answer is `stale-remote`; the read list holds `FETCH_HEAD · skipped — empty`; the tracking ref's entry ends `from reflog`; the plant prints `position: fixture · failed-fetch · another url reads <reason>` for `check_fetch_head` over `<zero sha>\t\tbranch 'main' of <top>/up2` against `derive_fetch_url` of `<top>/o.git`, owed `no line for main of origin` |

The owed reading is one entry of `tools/loop/position.py#check_plant`'s table, beside 65's three.
`run_plant`'s `remove_tree(top)` takes the scratch with the rest.

### Inventory

| Minted | Kind | Where | Lexicon |
|---|---|---|---|
| `check_fetch_head` | Python function | `tools/loop/position.py` | `py.function`, `OK` |
| `derive_fetch_url` | Python function | `tools/loop/position.py` | `py.function`, `OK` |
| `failed-fetch` | plant | `PLANTS` of `tools/loop/position.py` | not graded |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` printed OK for both, leading with
`check` and `derive`. The same verb run over `normalise_fetch_url` printed that `normalise` is not a
declared verb (§8 F3). It ran in this spec's worktree at `179486e8f`, whose lexicon kit differs from the
branch tip's only in tag-name grading, the `stage` keys of its two legs and `VERB_OFFENDER_PIN`.

### Files touched (estimate)

- `tools/loop/position.py`
- `help/loop.md`
- `memory/map/generated/symbols.json`, with any generated sibling `gen_map.py --write` rewrites
- `tools/run-gates/selftest-budgets.txt`, only where the close's timed reading re-prices the leg's row

### Alternatives rejected

- **The size check alone.** A fetch of another branch writes a non-empty file and leaves the default
  branch's tracking ref as stale as before.
- **Matching the branch and ignoring the URL.** A fetch from a second remote names its own `main`.
- **Staging the plant on a clone.** A clone with every `FETCH_HEAD` skipped falls to its clone entry,
  which is fresh in a scratch made seconds ago, so the plant could not read stale; the `git init`
  scratch holds no clone entry.
- **Writing the 0-byte file by hand.** The plant would then not observe the writer the finding names.

## 5. Production-readiness checklist

- security — reads only; the skip entry names the remote by name, so a token in a configured URL never
  reaches a printed line.
- perf / scale — one `git remote get-url` spawn per reading, only where a `FETCH_HEAD` exists; each file
  read once, a few lines.
- error / empty / loading states — an empty, unreadable or non-matching file is skipped and named, never
  fresh; a failed `get-url` skips every non-empty file as `no line for`, the conservative side.
- observability — S2's skip entry names the file and the reason on the `read —` lines and in `--json`'s
  `read` list.
- risks — a remote URL git writes beyond the trailing `/` or `.git` reads skipped until 77 lands, and the
  skip entry names it; this repository's own remote is an https URL with no user part, which matches.
  The leg's ceiling, 300 PINNED seconds in `tools/gate-legs.json`, and its budget row, 411 PINNED
  seconds, each gain one plant of a few seconds; this unit moves no ceiling, and a reading past it is
  recorded at the close.
- testing — AC1 to AC3 as plants, AC4 as a page probe; the arm under §7, observed RED then GREEN at the
  close. `unreadable` is not planted: a scratch cannot hold a file `os.stat` answers and `open` refuses
  on every host.
- migration — none; no stored data changes shape.
- user docs — `help/loop.md` (S4).

### The sweep

Read at the branch tip `e0a7e54b3`; counts PINNED there unless named DERIVED.

| Changed | Population | What keeps it green |
|---|---|---|
| `read_fetch_time` (65's) gains the remote and returns the skip entries (S1) | `read_remote_claim`, its one caller | the remote is the value `read_remote_claim` already resolves; the time and source keep 65's meaning over a smaller population |
| the population loses empty and foreign files (S1) | `derive_answer` through the claim's verdict; `check_plant`'s `steps` entry, which reads the remote claim's name, key and verdict; 65's `fresh-clone`, `quiet-remote` and `offline-stale` entries | the claim's fields keep their shape; `steps` and `fresh-clone` hold no `FETCH_HEAD`; `quiet-remote` and `offline-stale` fetch the default branch of `origin`, so their files are kept, and AC2 owes it |
| `read_remote_claim`'s second value becomes a list (S2) | `derive_position_into` alone | it extends the read list where it appended one entry |
| the skip entries on the read list (S2) | `render_position_lines`, `--json`'s `read` list and the driver's `--status`, which print them; `run_composition_plant`, which asks for a `composition@` entry; `check_plant`'s `steps` entry, which asks for an entry opening `memory/` | no reader parses another entry; neither membership test can match `FETCH_HEAD ·` or `worktrees/` |
| `PLANTS` gains `failed-fetch` (S3) | `run_selftest`, which runs every entry; the leg `loop position fixtures` and its budget row, 411 PINNED seconds; `tools/loop/README.md`'s "the last two over the unattended driver" and `help/loop.md`'s "the last two run the unattended driver" | the plant sits ahead of `plan-line` and `status-line`; it runs no driver; the row is re-priced from a timed reading of the leg alone where that reading passes it |
| the `--plant` values | the `script:{prefix}/loop/position.py` row of `tools/govkit/usage.toml`, its `--plant=` flag; the anchor `script:tools/loop/position.py 8d078234` on `help/loop.md` | `tools/govkit/docs_leg.py#derive_usage_fingerprint` hashes the row's fields, which name the flag and not its values, so the anchor stays current; no flag is added |
| `check_fetch_head` and `derive_fetch_url` minted | `memory/map/generated/symbols.json` under `codebase-map coverage + freshness`; the lexicon's verb census | the map is re-rendered by `gen_map.py --write` in the pass commit; both names grade OK |
| the docstring and the help paragraph (S4) | `install-prefix (shipped surface)`, whose population holds `position.py` and not `help/`; `docs` and `help page commands`; 76's `no-own-conf-read` rule, which keys on string constants naming a conf | the new text spells no kit path and adds no command span, no link and no flag; the change adds no conf-name constant |
| this spec | `memory/project/positional-refs.txt`, 0 PINNED rows for this spec, under `positional (the citation check alone)` | this revision cites symbols only |
| sibling specs | `TOOL-dDeclaredLoop-75` S12 (the other-branch skip), `TOOL-dDeclaredLoop-77` S1, S4 and AC1, `TOOL-dDeclaredLoop-79` and `TOOL-dDeclaredLoop-82`, which name `normalise_fetch_url` and the `--explain` read-set | the skip reasons keep 74 rev-2's spelling, so 75's and 77's `no line for main of origin` stand; the read-set is the `read —` lines (F2), and the normaliser is `derive_fetch_url` (F3); each re-grounds at its own pass |

```
B=branch/unattended-declared-loop-d56bf0
git grep -n -e 'read_remote_claim' "$B" -- tools                        # position.py alone: the def and one call
git grep -n -e '\["read"\]' "$B" -- tools/loop                          # position.py, and composition.py's membership check
git grep -n -e 'FETCH_HEAD' "$B" -- tools skills help                   # no reader of its content
git grep -n -e '--explain' "$B" -- tools/loop                           # none
git show "$B:tools/loop/position.py" | grep -c '^          "'            # PLANTS' continuation rows: 20, beside its first row
git show "$B:tools/run-gates/selftest-budgets.txt" | grep '^loop position fixtures'   # 411
git show "$B:tools/govkit/usage.toml" | grep -A3 'script:{prefix}/loop/position.py'
git show "$B:help/loop.md" | grep -n 'usage: script:tools/loop/position.py'          # 8d078234
git show "$B:memory/project/positional-refs.txt" | grep -c 'spec-TOOL-dDeclaredLoop-74.md'   # 0
git grep -n -e 'normalise_fetch_url' -e 'read-set' "$B" -- memory/builds/dDeclaredLoop/spec
```

### Budgets and records

- The lexicon offender pin: `VERB_OFFENDER_PIN` in `.lexicon.conf` stays 1215 PINNED, since both names
  minted grade OK (§4 "Inventory").
- The shared records: `SHARED_RECORDS` in `.unattended.conf` names `memory/DECISIONS.md` and
  `memory/project/readme-contract.txt`. The pass writes neither, and no decision row is owed ahead, since
  no ceiling or pin is raised.
- The refusal ceilings and families: `tools/memory-tree/check-arms.py#scan_refusal_sites` reads tracked
  `*.sh` files alone, and this unit edits none. The driver's ceiling in `REFUSAL_CEILINGS` stays
  343 PINNED, and `tools/unattended/unattended.families.txt` does not move.
- Help anchors: no verb and no flag is added; `failed-fetch` is a value of the anchored `--plant`.
- Subject pins, epoch delegates, upgrade rows and the kickoff watch list: no leg is added; no file of the
  memory-tree engine `check-verdict-epoch.sh` delegates to is edited; no data changes shape, so no
  `[[upgrade]]` row is owed; neither edited path is on the `watch:` line of
  `memory/guides/SESSION-KICKOFF.md`.
- Shipped bytes: the loop kit's version is minted at the lander, as `tools/govkit/govkit.py#cmd_epoch`
  states, so the branch owes no bump.

```
B=branch/unattended-declared-loop-d56bf0
git show "$B:.lexicon.conf" | grep '^VERB_OFFENDER_PIN'                  # "1215"
git show "$B:.unattended.conf" | grep '^SHARED_RECORDS'
git show "$B:.memory-tree.conf" | grep '^REFUSAL_CEILINGS'               # the driver's 343
git show "$B:memory/guides/SESSION-KICKOFF.md" | grep '^watch:'
git grep -c -e 'loop/position' -e 'help/loop' "$B" -- tools/memory-tree/check-verdict-epoch.sh   # none
```

### Dependency

`TOOL-dDeclaredLoop-65` (order 37, committed rev-3) is read throughout: `read_fetch_time`, its population
and clone fallback, the tracking ref's `read —` entry `fetched <n>s ago · from <source>`, its three
plants and its S5 docstring and help paragraph, each of which this unit edits after it.
`TOOL-dDeclaredLoop-56` (order 36, committed rev-6) S36 restages the `stale-remote` scratch the plant
stages on, and keeps a non-resolving ref out of the reading. `TOOL-dDeclaredLoop-33` (order 34, committed
rev-7, rev-8 coming) extracts `read_build_items` out of `derive_position_into`, and
`TOOL-dDeclaredLoop-72` (order 36, committed rev-6) moves its memory-root read onto
`resolve_memory_root`; neither touches the remote read. At order 37, `TOOL-dDeclaredLoop-68` edits the
witness normaliser of `tools/loop/loop_witness.py` and leaves `read_git` and `run_fixture_git` as they
are, and `TOOL-dDeclaredLoop-76` mints the conf-read rule S4's row names. At order 38,
`TOOL-dDeclaredLoop-67` (committed rev-3) adds `writer-unexpected` to `PLANTS` and imports one constant
into `position.py`, apart from the remote read; both plants sit ahead of the last two whichever lands
first. `TOOL-dDeclaredLoop-66` and `TOOL-dDeclaredLoop-80` touch no file of this unit. At order 39,
`TOOL-dDeclaredLoop-75` and `TOOL-dDeclaredLoop-77` read this reading. `TOOL-dDeclaredLoop-34` is
deferred against ask TOOL-dDeclaredLoop-113 and `TOOL-dDeclaredLoop-33`'s numeric direction against ask
TOOL-dDeclaredLoop-114; neither shares the remote read. Every code claim was read through `git show` at
the branch tip; the lexicon and the reuse probe ran on the worktree at `179486e8f`, cut from main.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant failed-fetch` runs in `tools/loop/`, it prints
  `position: fixture · failed-fetch · held`, the answer is `stale-remote`, a line reads
  `read — FETCH_HEAD · skipped — empty`, and the tracking ref's `read —` line ends `from reflog`.
  Red when: the truncated file's fresh mtime is counted and the answer reads fresh.
- **AC2** — When `python position.py --fixture --plant quiet-remote` and `--plant offline-stale` run in
  `tools/loop/`, they print `position: fixture · quiet-remote · held` and
  `position: fixture · offline-stale · held`, each tracking ref's line ends `from FETCH_HEAD`, and
  neither prints a `skipped —` line.
  Red when: the content check rejects a real fetch of the default branch, so `quiet-remote` reads stale
  by its aged reflog and `offline-stale` reads fresh by its clone entry.
- **AC3** — When `python position.py --fixture --plant failed-fetch` runs in `tools/loop/`, it prints
  `position: fixture · failed-fetch · another url reads no line for main of origin`.
  Red when: the URL is not compared, so a `main` line fetched from a second remote is kept.
- **AC4** — When `grep -c "failed-fetch" loop.md` and `grep -c "skipped — " loop.md` run in `help/`,
  each prints 1 or more, and `grep -c "spelled otherwise" position.py` in `tools/loop/` prints 1 or more.
  Red when: the page or the docstring still says any `FETCH_HEAD` mtime is a fetch.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

The pass keeps the sibling-minted `loop position fixtures` leg green, which runs every plant of
`position.py`. That leg is in the branch's `tools/gate-legs.json` and not in main's, which the spec-token
checker reads, so it is named here and not on the leg line.

New arm: tools/loop/position.py · covers AC1 AC2 AC3 · the failed-fetch plant beside 65's quiet-remote and offline-stale plants, staged against TOOL-dDeclaredLoop-65's mtime-only reading · the `loop position fixtures` budget row, re-priced where the close's timed reading passes it

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Where does a skipped file print?** rev-2 named an `--explain` read-set, which `position.py` does
  not have. Options: (a) one entry per skipped file on the read list, printed as a `read —` line and in
  `--json`; (b) a new `--explain` flag printing them; (c) a field on the tracking ref's own entry.
  (b) adds a flag, a usage row change that moves the help anchor's fingerprint, and a surface 77 S4 must
  then keep URL-free; (c) packs a list of files onto one entry. Recommendation: (a). RESOLVED (agent,
  2026-11-16, delegated): (a), under the run's mandate, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-74-1-spec-writer`. widens: none · relaxes: none
- **F3 — Which name spells a fetched URL?** The comparison spells both sides, so it is one function.
  Options: (a) mint `derive_fetch_url` here, which 77 extends with the user-part rule; (b) inline the
  strip here and let 77 mint `normalise_fetch_url`; (c) mint `normalise_fetch_url` here. The lexicon's
  suggest verb answers that `normalise` is not a declared verb, so (b) and (c) each add one offender to
  `VERB_OFFENDER_PIN`, and (b) spells the rule twice until 77 lands. Recommendation: (a). RESOLVED
  (agent, 2026-11-16, delegated): (a), under the run's mandate, per the brief
  `2026-11-16-prompt-TOOL-dDeclaredLoop-74-1-spec-writer`. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-3 spec audit's id 45 (HIGH, item H7).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-77, written by the round-4 spec audit's disposal; nothing else moved.
- rev-3 · 2026-11-16 · §1 to §10 · S1 to S4 · AC1 to AC4 · §8 F2, F3 · re-grounded on branch
  `unattended-declared-loop-d56bf0` at `e0a7e54b3` and on the committed specs of TOOL-dDeclaredLoop-65
  rev-3 and TOOL-dDeclaredLoop-56 rev-6, per the brief `2026-11-16-prompt-TOOL-dDeclaredLoop-74-1-spec-writer`:
  S1 names its two functions and the remote it now takes; S2's skip entry rides the read list by F2;
  S3 stages the plant on 56's restaged scratch and adds the second-URL probe, AC3; S4 and AC4 bring the
  help page and the docstring current; the URL helper is `derive_fetch_url` by F3; the sweep.

## 10. Reuse audit

The seam is 65's `read_fetch_time` in `tools/loop/position.py`, unbuilt at the branch tip, extended by a
content check on the files it already stats; its caller `tools/loop/position.py#read_remote_claim`
already resolves the remote and branch the check needs. `python tools/codebase-map/reuse_lookup.py
"validate that a FETCH_HEAD file holds the default branch of the remote url"`, run on the worktree at
`179486e8f`, which lacks the loop kit, ranked `write_file`, `branches`, `derive_kit_file`, `corpus_files`
and `resolve_remote`; `resolve_remote` names which remote and branch, and none reads a `FETCH_HEAD` or
spells a fetched URL. A `git grep` at the branch tip for `get-url` and for a `.git` suffix strip in
`tools/` found no URL normaliser. So no existing seam fits beyond the engine's own reader.

Recall terms used: FETCH_HEAD mtime failed fetch truncated default branch remote url get-url stale-remote freshness position engine skipped read list
