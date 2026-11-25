# TOOL-dTotalRecall-122 — the closing review's round 2: the rollback that checks its bytes, one section read for a pinned and an unpinned address, the arms no branch could red, the runlog floor, the lost decisions and the feed line's wrap

**Status:** CLOSED · rev-1 · 2026-11-25 · node d · Tier-2 · base 146df780 · streams tooling · order 50

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-dTotalRecall-122-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-dTotalRecall-122-1-acceptance-ledger.md) | log | — |
| [2026-11-25-build-TOOL-dTotalRecall-122-deviation-1018.md](../build/2026-11-25-build-TOOL-dTotalRecall-122-deviation-1018.md) | deviation | — |
| [2026-11-25-build-TOOL-dTotalRecall-122-widen-33.md](../build/2026-11-25-build-TOOL-dTotalRecall-122-widen-33.md) | widen | — |
| [2026-11-25-build-TOOL-dTotalRecall-122-widen-34.md](../build/2026-11-25-build-TOOL-dTotalRecall-122-widen-34.md) | widen | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-122-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-122-build-brief.md) | journal | — |
| [2026-11-25-prompt-TOOL-dTotalRecall-122-spec-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-122-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's second round converged with no BLOCKER and no HIGH
(`2026-11-25-review-TOOL-dTotalRecall-115-closing-diff-review-round2.md`). This unit closes its nine MEDIUMs and two LOWs,
findings 1 to 12, one scope item each (DERIVED, that report). M1 and M2 are behaviour the fold introduced; the rest are
branches no arm reds, records that say what is not so, and one line's wrap.

## 2. Scope (IN)

- **S1** — M1, finding 1, the class-level fix. One helper beside `add_to_index`, `build_records.py#write_prior_bytes`, undoes a write only
  where the file still holds the bytes the call wrote; both rollbacks of `tools/memory-tree/gov_record.py#write_new_ask` and
  `build_records.py#write_new_record`'s refused stage call it (§4). Observed by AC1.
- **S2** — M2, finding 2. `tools/memory-tree/record_find.py#read_section`, given a blob, reads every record row of the key in line
  order and, given a tag, takes the first whose extent holds a section of it, indexed and unindexed alike (§4).
  Observed by AC2.
- **S3** — M3, finding 4. The slug pre-check's arm of `tools/memory-tree/gen_build_index.py#test_slug_claims` compares the whole reason
  for `9x`, `x_y` and `x/y`, asserts no claim ref of theirs on the remote, and labels `-x` the option parser's (§4).
  Observed by AC3.
- **S4** — M4, finding 5. `tools/workflows/replay_scorer.py` gains the arm `map-experiment`, which drives `check_experiment` to the byte
  term's figures, unarmed and armed (§4). Observed by AC4.
- **S5** — M5, finding 6. The plant `section-second-file` of `record_find.py`: a key with two rows, the first path's file holding the
  tag outside the key's extent, the second inside it (§4). Observed by AC5.
- **S6** — M6, finding 7, the class-level fix as corrected in §4. The plants `other-tree` and `other-tree-unpathed`: a blob only
  another worktree's tree holds, at two paths, and the same with its path rows gone. Observed by AC6.
- **S7** — M7, finding 8, the corrected fix. The `door-header` plant gains the case `unread header` over a record of its own. Observed
  by AC7.
- **S8** — M8, finding 10. `ASSERTION_FLOOR` of `tools/runlog/selftest.py` is raised by reading over the two arms it left out, its
  comment says which arms each raise counts, and nothing is pinned at the close (§4, §8 F2). Observed by AC8.
- **S9** — M9, finding 11. The pass commit's final trailer block restates the three decisions as `Decided:` lines, each naming
  its sha, and the commit-time check refuses a line opening `Decided:` that git does not parse (§4 "The decisions"). Observed by
  AC9 and AC10.
- **S10** — L1, findings 3 and 9, the class-level and corrected fixes joined. `replay_scorer.py#check_read_call` answers False for
  a read program's or a git read's writing option; the `map-transcript` arm gains each such act, a quoted `>` and a heredoc; the
  README points at the listed gaps; and the class `read-allowlist-admits-a-writing-option` is authored in
  `memory/gotchas/`, claimed by `memory/map/features/review-harnesses.md`, its `INDEX.md` regenerated (§4). Observed by AC11
  and AC12.
- **S11** — L2, finding 12. The `--feed` entry's last sentence in `tools/unattended/VERBS.template.md` is re-wrapped to its
  neighbours, and `memory/guides/UNATTENDED-VERBS.md` is installed by `bash tools/unattended/adopt-unattended.sh`. Observed by
  AC13.
- **S12** — The floors and literals the arms move are raised by reading, and the `shell-role` rows of `tools/unattended/unattended.sh`,
  `tools/unattended/unattended.test.sh` and `tools/memory-tree/check-memory-hygiene.test.sh` are widened through `ratchet.py widen`,
  unit `TOOL-dTotalRecall-122`, then set to the measure, a `Decided:` trailer naming them. Observed by AC14.

## 3. Non-goals (OUT)

- The INSTANCE-ONLY fixes of findings 1, 3 and 7 and the rejected ones of findings 8 and 9.
- Any edit of `TOOL-dTotalRecall-118` or `TOOL-dTotalRecall-121`, both CLOSED and frozen. Spec 118 §4's "what the 1711 already counts" and
  spec 121 S12's "a `Decided:` trailer … as `TOOL-dTotalRecall-116`'s commit does" are corrected here: the first counted
  seven arms of nine, and the second's commit carries the line outside git's trailer block (DERIVED, the report).
- A rewrite of `19a209739`, `8451b1de2` or `07486a8f8`, whose prose stands in their bodies.
- The same loss in eight earlier commits of this build, `289db6c05`, `6db81d070`, `491dfe31c`, `ce198f660`, `c6fcf603b`, `dc1fd17e7`,
  `a9f1e2a68` and `f36ec323c`, outside the round's range (DERIVED 2026-11-25, S9's check over this build's own commits
  since `3d6c1702a`): the brief names three, and the main loop is told of the rest.
- The pin of the hygiene suite's floor, which `TOOL-dTotalRecall-121` AC9 owes at the close; this unit's arms raise it by reading first.
- A stem key's row in the index, which the index writes once per blob from the first path parsed (§4 "The other tree").
- The `d0e02120b` limits red, the units held on owner asks, and any policy key or bound moved.

### Edges

- **consumes-from** external — the closing review's second report and the landed units whose code it read
- **hands-off** external — the close's next bar, the held suites, the hygiene floor's pin and the landing, each the main loop's

## 4. Design

Read at `146df780` on 2026-11-25. Each item's claim about the code holds but where a sub-head says so.

### S1 — the rollback

```python
def write_prior_bytes(root, rel, wrote, prior):
    """Undo this call's write of `rel` where the file still holds `wrote`: removed where `prior` is None, else put back.
    -> what happened, for the refusal. A file another writer moved is left as it stands (TOOL-dTotalRecall-122 S1)."""
    path = pathlib.Path(root, rel)
    if (path.read_bytes() if path.is_file() else None) != wrote:
        return "and it moved since it was written, so it is left as it stands, unstaged"
    if prior is None:
        path.unlink()
        return "so it was removed"
    from legacy_ledger import _write_atomic
    _write_atomic(path, prior)
    return "so it was put back as it was"
```

`write_new_ask` keeps the bytes it hands `_write_atomic` and calls the helper in its refused branch; the read-back
branch calls it too, and runs its `git rm --cached` or its `add_to_index` only where the helper undid the write, printing
what it answered in place of "put back as it was" otherwise, exit 3 as today. `write_new_record` keeps the text it
wrote, the typed branch's captured in `check_written`, which already receives it. The messages of the undone cases stand, so
the `index-lock` cases do. What it does not check: a writer inside the spawn-free window between its read and its replace.

The arms run a child that rebinds `build_records.add_to_index`, as `run_planted_door` rebinds the renderer: the planted
one appends a foreign line to the file, then answers a refusal, or stages and answers nothing. The `ask-door` cases are
`foreign row`, over no `BACKLOG.md` and over a held one, and `foreign read-back`, a foreign ask row staged with the write;
the `door-header` case is `foreign line`. Each asserts the foreign bytes survive and the refusal says the file moved. On
today's code each loses them.

### S2 — the pinned row

```python
held = con.execute("SELECT DISTINCT b.line, b.end_line … AND b.text=? ORDER BY b.line", (sha, key)).fetchall()
…                                                     # `held is None` becomes `not held`, `is not None` its converse
        held, path = found, cand                      # every row the text defines, in line order
…
held = next((h for h in held if any(s[0] == tag and h[0] <= s[1] <= h[1] for s in secs)), held[0])
```

The pick below stays. Probed over a fixture file with two `## TOOL-bFix-21` headings and `### Outcome` under the second: today
the unpinned address prints the section, and the pinned one and an unheld blob's exit 2; fixed, all three print it, and a
pinned read with no tag still prints the first row (DERIVED 2026-11-25, that probe). The plant is `section-later-row`, its
three reads and that fourth each asserting exit 0.

### S3 — the pre-check's arm

The arm moves above the policy-kit skip, since no grammar is read before the pre-check refuses. `got` is the whole line:
`refused the slug is not a letter, then letters, digits or dashes` for each of `9x`, `x_y` and `x/y`, and `refused -x is
no option` under its own arm, labelled the option parser's; then `git for-each-ref refs/gov/claims` over the bare remote
names none of them. With the line cut, each is refused by the derived grammar in other words.

### S4 — the experiment

`map-experiment` builds, in one temporary folder, a known record of six items (PINNED, the arm) with one finding each, two arms,
two runs per arm of one case, and one lens transcript per run. The with-map reports confirm all six and the without reports
one, so recall passes; the without transcripts make one search after their act, so the search term passes. With every
transcript's first call an `Edit`, the last lines are `term bytes: unarmed · every lens run read 0 before its first act` and
`verdict unarmed bytes`; with a ten-byte `Read` (PINNED, the arm) ahead of each act, the figures line and `verdict win`.
Probed whole over today's scorer, which prints those lines, and with `armed` pinned True the first prints `verdict
win` (DERIVED 2026-11-25, that probe). It skips as `map-transcript` does where no runlog kit resolves. `ARMS_DECLARED` rises by one.

### S5 — the second file

Two record files of the fixture's build, in path order: the first holds `TOOL-bFix-31` with no section, then another id over
`### Outcome`; the second holds `TOOL-bFix-31` over its own `### Outcome`. `show TOOL-bFix-31#section.outcome` prints the second's text and
exits 0; with the loop's containment cut it is refused (DERIVED 2026-11-25, a probe over both).

### S6 — The other tree

**The report's plant does not reach the branch.** It asks for one branch holding the edited record at two paths, the stem
path and one sorting before. The index extracts a blob once, under the first path it parses, so its stem row is that path's: over such
a branch `blob_row` held the earlier path's stem alone, and the addressed stem took the unindexed route (DERIVED
2026-11-25, a probe). So the plant commits twice in the second worktree and indexes after each: first the edit at the
record's own path, then the same bytes at a path sorting before it. Then the addressed key is the blob's indexed row, the
blob stands at two paths, and neither is the first tree's.

Run whole from the first tree, `show <stem>#section.findings-2@<blob>` prints the other tree's text and `read_section` the record's own
path; the lookup's path cut to empty answers `''`, a plain `min` the earlier path, and the blob's `path_row` rows deleted
exit 2 with `stands at no path the index holds`, so the refusal is reachable and stays (DERIVED 2026-11-25, a probe per
variant). The plant prints the path the read answers on a line of its own, since `show` prints text alone. A break is
staged in the kit the fixture copies, before the worktree is made: an edit in one tree alone moves that tree's extractor
version, and the read takes the unindexed route (DERIVED 2026-11-25, the same probes). `other-tree-unpathed` deletes the
rows through `sqlite3` on the fixture's own index file. Neither name opens `blob-`, whose plants `run_fixture` reads by a table.

### S7 — the unread header

After the key loop, the case writes `n-unread` through the door and commits, appends a second `**Caused-by:**` line inside the
head of that file and commits, and repeats the same call: exit 2, `unread, its header refusing to read`, and no `exists `. The
shared record is not touched, so the cases above keep their meaning.

### S8 — the floor

The pass raises by reading and the close pins nothing: `parse_floor_raise` grades the newest raise line's arithmetic against
the floor, so a figure read off a run would need an equation nobody derived. A new raise line,
`# RAISED 1724 -> 1746 by TOOL-dTotalRecall-122: …` (DERIVED, the next clause), counts `test_memory_dtr43_paths`, 10 checks and 3 decoy
checks, and `test_memory_dtr53_paths`, 6 and 3 (DERIVED, the two arms), closing on `# 13 + 9 = 22` (DERIVED, that sum). The line of
`TOOL-dTotalRecall-118` keeps its figures and says the seven arms of `TOOL-dTotalRecall-12` came back counted and the two
path arms did not. What the close owes is the `runlog selftest` run at or above the floor.

### The decisions

The pass commit's final trailer block carries, beside its own, these three lines, each one line:

```text
Decided: 19a209739's widened shell-role counts are set to the measure by hand after the door — the door raises a row by one and names no count, as widen-22's rows were written
Decided: 8451b1de2's widened shell-role count is set to the measure by hand after the door — the door raises a row by one and names no count, as widen-28's rows were written
Decided: 07486a8f8's kit README key sentence and new class's map claim ride that commit — deviation 1016, S1 made the sentence false and an unclaimed class reds coverage
```

**The gate is scoped.** `.githooks/commit-msg` runs `unattended.sh --check-commit` on every commit, and `check_commit_message` already
reads the message through `commit_trailers.py` and refuses on check 49. So one function joins the `commit_trailers_py`
block, `check_message_decisions(raw)`: the lines of `extract_message_lines` opening `Decided:` against the `Decided:` lines of
`git interpret-trailers --parse` over the message, the parse `read_message_ids` makes; it answers `refused` naming the first line where
the parse returns fewer, else `ok`. A verb `decided <file>` prints `DECIDED <state> · <detail>` and exits 1 on a refusal and
exit 2 on an unreadable message. Over this build's commits it refuses the three and admits the commits of `TOOL-dTotalRecall-118`, `-119` and
`-121` (DERIVED 2026-11-25, a probe). The driver asks it after the attribution check and refuses through check 49, `put every 'Decided:' line in the
message's final trailer block, with no blank line after it: …`; another exit says the check did not run. Three carriers hold the
block. It is one more interpreter on a bound run's commit. What it does not check: a commit no run binds, a
`--no-verify` commit, and a `Decided:` line git parses with another key's value folded into it.

### S10 — the writing options

```python
GIT_WRITE_OPTION = re.compile(r"--output(?:=.*)?", re.S)     # never `-o`: `git grep -o` and `git ls-files -o` read
FIND_WRITE_OPTIONS = frozenset({"-delete", "-fprint", "-fprint0", "-fprintf", "-fls", "-exec", "-execdir", "-ok", "-okdir"})
…
        if sub in GIT_READS and any(GIT_WRITE_OPTION.fullmatch(w) for w in words):
            return False
        if program == "find" and FIND_WRITE_OPTIONS.intersection(words):
            return False
```

The docstring names the two beside `sed`'s in-place option and drops `find -exec` from its gaps. Today `git diff a..b --output=x.txt`,
`git diff --output x a b`, `find . -delete`, `find . -fprint x` and `find . -exec rm {} ;` each answer True, and so do `git grep -o x`,
`git ls-files -o` and `git log --output-indicator-new=+`, which stay True (DERIVED 2026-11-25, those calls). A search stays a
search to `measure_call_searches`, which this does not touch. The `map-transcript` calls gain a `grep -n "a > b" f` and a heredoc
read ahead of the act, and one transcript per option whose first call is it, reading zero bytes. `tools/workflows/README.md`'s
"writing no file" ends by pointing at `check_read_call`'s list of what it does not read.

The gotcha is in the shape of `refusal-branch-with-no-arm.md`: an allow-list of reading programs admits a program's own
writing option; where it bit; the fix, an option check per admitted program, seen red per option; its gate, the `map-transcript`
cases. It names its near match, the one `python tools/memory-tree/row_grammar.py --check-relations 3d6c1702a` prints, by a relation.

### S11 — the wrap

```text
  `unread` for a `MEMORY_ROOT` that is no plain relative path or a walk git refuses; `--feed rebuild`
  then appends the record events of the remote default branch's tracking ref, and exits 2 with
  `feed: no record events were rebuilt: <why>` where none resolves.
```

The same entry's neighbour, `--check-commit`, gains S9's sentence: it also refuses a `Decided:` line outside the message's
final trailer block. No arm fits the wrap, as the report says; its class `fold-text-is-unreviewed-surface` stands.

### Inventory

Minted: `write_prior_bytes` in `build_records.py`; `check_message_decisions` and the verb `decided` in `commit_trailers.py`;
`GIT_WRITE_OPTION` and `FIND_WRITE_OPTIONS` in `replay_scorer.py`; the arm `map-experiment`; the plants `section-later-row`,
`section-second-file`, `other-tree` and `other-tree-unpathed`; the stage plants' names; the gotcha's slug. The lexicon admits the two
functions for cell `py.function` (DERIVED 2026-11-25, its `--suggest`).

### Files touched (estimate)

- `tools/memory-tree/build_records.py`
- `tools/memory-tree/gov_record.py`
- `tools/memory-tree/record_find.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/README.md`
- `tools/memory-tree/commit_trailers.py`
- `tools/lib/commit_trailers.py`
- `tools/unattended/commit_trailers.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`
- `tools/runlog/selftest.py`
- `memory/gotchas/read-allowlist-admits-a-writing-option.md`
- `memory/gotchas/INDEX.md`
- `memory/map/features/review-harnesses.md`
- `memory/map/generated/`
- `memory/project/shell-role.txt`
- `memory/LIVE.md` and `memory/builds/dTotalRecall/README.md`, which `python tools/memory-tree/gen_build_index.py --write` renders
- `memory/builds/dTotalRecall/build/` (the widen record and this unit's ledger)

`tools/memory-tree/README.md` states the record door's refused stage as "nothing left written"; it gains S1's moved file. No carrier of the
`commit_trailers_py` block but the three stands (DERIVED 2026-11-25, `git grep` over the block's marker).

### Alternatives rejected

- **The helper in `gov_record.py`.** The record door's unlink would stand, the INSTANCE-ONLY fix.
- **The decision check inside the `attribution` verb.** Its refusal's repair is the charter's line, which is not this one's.
- **The class filed as its standing gotcha, with no gate.** The brief takes a gate where a hook reads the message and takes one
  check; one does.
- **The raise and a pin at the close (S8).** The figure derives by reading, and the run confirms it.

## 5. Production-readiness checklist

- security — a rollback no longer destroys bytes it did not write; the write allow-list narrows.
- perf / scale — one interpreter more per commit a run binds; the new fixture plants are the cost below.
- error / empty / loading states — each undo says which of its three outcomes happened.
- observability — the refusal names the moved file, the decision line and the repair.
- risks — S9's check refuses a message that quotes a line opening `Decided:` in prose; the repair is an indent.
- testing — AC1 to AC14 by the pass; §7's arms by the main loop. Before these cases the `door-header`
  plant ran 9 minutes and `ask-door` four (PINNED 2026-11-25, `TOOL-dTotalRecall-121`'s second return), and `other-tree` runs past two minutes, its reads 25 to
  50 s each (PINNED 2026-11-25, node d, a loaded machine): the builder runs each in the background under a bound.
- migration — none.
- user docs — `tools/memory-tree/README.md`, `tools/workflows/README.md` and the verbs guide; no page under `help/` states any of these.

## 6. Acceptance criteria

- **AC1** — When `python build_records.py --fixture --plant ask-door` and `--plant door-header` run from `tools/memory-tree/`, the cases `foreign
  row` (both), `foreign read-back` and `foreign line` each print the exit their door answers, the foreign bytes stand in the
  file, and the refusal says it moved; the `index-lock` cases print what they print at `146df780`.
  Red when: a rollback writes or unlinks without the compare. Today each foreign case loses its bytes.
  cost: minutes each, in the background.
- **AC2** — When `python record_find.py --fixture --plant section-later-row` runs there, the unpinned, the pinned and the unheld-blob
  address each print the later row's section, and the pinned address with no tag the first row, every read `exit 0`.
  Red when: one unordered row is taken. Today the second and third exit 2.
- **AC3** — When a probe over a scratch clone and bare remote runs `bash gov-claim.sh slug <s> --claimant <key>` for `9x`, `x_y` and `x/y`,
  each prints `refused the slug is not a letter, then letters, digits or dashes` and exits 2 and the remote holds no
  `refs/gov/claims/` ref; with the pre-check line cut from a scratch copy, none prints that text; and `grep -c 'not a letter, then letters'
  tools/memory-tree/gen_build_index.py` prints at least 1 (DERIVED, S3).
  Red when: the arm's text is one the grammar's refusal also prints.
  permission: `test_slug_claims` itself is the main loop's, under the build-index selftest.
- **AC4** — When a probe builds S4's manifest and calls `check_experiment`, the last lines are the unarmed pair for act-first transcripts
  and the figures line with `verdict win` for read-first ones; with `armed` pinned True in an in-memory copy the first
  ends `verdict win`. The arm, run as a function cut from `run_selftest`, answers None.
  Red when: the arm reads the pure function alone.
- **AC5** — When `python record_find.py --fixture --plant section-second-file` runs there, it prints the second file's outcome and `exit 0`;
  with the candidate loop's containment cut in a scratch copy, it exits 2.
  Red when: the plant's key has one row.
- **AC6** — When `python record_find.py --fixture --plant other-tree` runs there, it prints the other tree's text, a line naming the
  record's own path and `exit 0`; `--plant other-tree-unpathed` prints `stands at no path the index holds` and `exit 2`. With the
  lookup's path cut to empty, and with a plain `min`, in a scratch copy of the kit, `other-tree` prints another path; with
  the refusal cut, the second plant no longer exits 2 naming it.
  Red when: the branch is reached by neither, or the break is staged in one tree alone and takes the unindexed route.
  cost: past two minutes, in the background under a bound.
- **AC7** — When the `door-header` plant runs, its `unread header` case exits 2 printing `unread, its header refusing to read` and no
  `exists `; with `read_key_fields` answering the fields without the cause in a scratch copy, the case fails.
  Red when: an unreadable header keys as anything.
- **AC8** — When `grep -nE '^ASSERTION_FLOOR|^# RAISED 1724' tools/runlog/selftest.py` runs, it prints the raise line and a floor of its upper
  figure, 1746 (DERIVED, S8); a probe calling `parse_floor_raise` over the file answers those two figures; and an `ast` count of the
  `check` calls the two arms make, looped rows read from their tables, gives 10 and 6 (DERIVED, the arms).
  Red when: the floor stands under what its comments say it counts.
- **AC9** — When `git log -1 --format='%(trailers:key=Decided,valueonly)'` runs over the pass commit, it prints the three lines of §4 and S12's,
  each whole.
  Red when: a decision sits above the final block, as the three it restates do.
- **AC10** — When `python tools/unattended/commit_trailers.py decided <file>` runs over a message whose `Decided:` paragraph stands above its
  trailer block, it prints `DECIDED refused` naming the line and exits 1; over one carrying it in the block, and over one with
  none, it exits 0; over the three commits' own messages it exits 1; and the three carriers' blocks are byte-identical.
  Red when: the scan reads git's parse alone, so a line outside it reads as absent.
- **AC11** — When a probe calls `check_read_call` over the five writing calls of §4 S10 and `-fprint0`, `-fprintf`, `-fls`, `-execdir`, `-ok` and
  `-okdir` forms of `find`, each answers False; the three `-o` and `--output-indicator-new` reads, `grep -n "a > b" f`
  and a quoted-delimiter heredoc answer True; and `map-transcript`, run as a cut-out function, answers None, failing with `QUOTED_SPAN` a
  no-op or either option test cut.
  Red when: an option is admitted, or a read is refused. Today the writing calls answer True.
- **AC12** — When `python tools/memory-tree/gotchas.py --check` runs, it names no finding of the new file; `--check-relations 3d6c1702a` after the
  commit prints no `check 27:` line naming it; and `grep -c 'read-allowlist-admits-a-writing-option.md' memory/map/features/review-harnesses.md`
  prints 1 (DERIVED, S10).
  Red when: the class is unclaimed, unindexed or names no relation.
- **AC13** — When `awk 'length($0) > 110' tools/unattended/VERBS.template.md | grep -c 'no record events were rebuilt'` runs, it prints 0 (DERIVED,
  S11), the `--check-commit` entry names `Decided:`, and `cmp` of the template with its guide, any CR cut, finds no difference.
  Red when: the line stays joined, or the guide is edited by hand.
- **AC14** — When `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` runs, the three paths of S12 read the counts
  their rows hold; the hygiene suite's `PASS door-header` and `PASS ask-door` literals equal what the plants print; and each floor
  the arms move, the hygiene suite's, the unattended suite's whole and its fourth shard's, has one raise comment naming this unit
  whose difference is the assertions the pass adds, counted by reading.
  Red when: a row, a literal or a floor stands while its arms land.
  permission: the observed counts are the main loop's at the close.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `ratchet (never gains)` · `ratchet (both ways)` · `memory-hygiene self-test` · `build-index selftest` · `gotchas selftest` · `review-replay selftest` · `runlog selftest` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `unattended skill wiring` · `docs` · `shell hygiene (a fork spent on builtin work)` · `scratch-guard self-test` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC7 · the `ask-door` and `door-header` literals over the foreign cases and `unread header` · each foreign case red on today's unconditional rollback; `unread header`, green today, red on `read_key_fields` staged to answer a partial key · none, literals of standing assertions
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC5 AC6 · the four `record_find.py` plants · `section-later-row` red on today's pinned read; `section-second-file` red on the candidate loop's containment cut; `other-tree` red on the path lookup cut and on a plain `min`; `other-tree-unpathed` red on its refusal cut · `FLOOR_ASSERTIONS` by the assertions added
New arm: tools/memory-tree/gen_build_index.py · covers AC3 · the pre-check arm's whole reasons and its empty remote · red on the pre-check line cut from `gov-claim.sh` · none
New arm: tools/workflows/replay_scorer.py · covers AC4 AC11 · `map-experiment`, red on `armed` pinned True; `map-transcript`'s writing options, each red on today's `check_read_call`, its quoted `>` red on `QUOTED_SPAN` a no-op and its heredoc on the heredoc removal cut · `ARMS_DECLARED` by one
New arm: tools/unattended/unattended.test.sh · covers AC10 · `--check-commit` over a `Decided:` paragraph above the block, refused, and in the block, admitted, with the reader's `--fixture` cases · red on today's driver, which admits both · `FLOOR_ASSERTIONS` and the fourth shard's floor by the assertions added
New arm: tools/runlog/selftest.py · covers AC8 · the raised `ASSERTION_FLOOR` · red on either path arm deleted from a scratch copy, which the floor of `146df780` passes · `ASSERTION_FLOOR`

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-121` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none
- **F2 — Is the runlog floor raised by reading or pinned at the close (S8)?** Options: (a) by reading, the two arms' figures
  derivable from their tables, the close running the suite over it; (b) a pin to the run's count, which `parse_floor_raise` then
  reds without an equation. RESOLVED (agent, 2026-11-25, delegated): (a). widens: none · relaxes: none
- **F3 — Is the commit-msg gate built or the class left to its gotcha (S9)?** Options: (a) built, the hook already reading the
  message through `commit_trailers.py` and refusing on check 49; (b) the gotcha alone, which caught none of the three. The brief's
  rule picks (a) where a hook reads the message and takes one check. RESOLVED (agent, 2026-11-25, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's round 2.

## 10. Reuse audit

The seams, each read at `146df780`: `build_records.py#add_to_index` and `legacy_ledger.py`'s `_write_atomic`;
`build_records.py#run_planted_door`, whose child the stage plants extend; `record_find.py#read_section` and its plant table;
`gen_build_index.py#test_slug_claims`; `replay_scorer.py#check_experiment` and its `map-transcript` line builder;
`tools/lib/commit_trailers.py`'s `extract_message_lines` and `read_message_ids`; `unattended.sh`'s `check_commit_message`;
`tools/runlog/selftest.py#parse_floor_raise`. `python tools/codebase-map/reuse_lookup.py "put a file back as it was only where it
still holds the bytes this call wrote"` and the same over "refuse a commit message whose trailer line is not parsed" ranked generic
readers and writers alone: no existing seam fits the undo or the decision check beyond these.

Recall terms used: `python tools/memory-recall/query.py "closing review round 2 minors rollback section row worktree blob trailer" --terms "destructive-step-before-its-precondition add_to_index read_section path_row trailer-parse-reads-only-the-final-block Decided measure_map_experiment refusal-branch-with-no-arm floor-left-below-the-arms-it-guards"`
