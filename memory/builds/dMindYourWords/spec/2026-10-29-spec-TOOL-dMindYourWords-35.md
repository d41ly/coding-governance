# TOOL-dMindYourWords-35 — the drain edit `--measure > <home>` reads the rows it carries from a copy the redirect cannot truncate

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 TOOL-dMindYourWords-30 TOOL-dMindYourWords-31 TOOL-dMindYourWords-32 TOOL-dMindYourWords-33 TOOL-dMindYourWords-34 TOOL-dMindYourWords-36 TOOL-dMindYourWords-37 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 30 of `reviews/2026-10-29-review-TOOL-dMindYourWords-22-to-29-spec-audit-round1.md`,
HIGH, item H4. TOOL-dMindYourWords-23 makes `--measure` carry the tag rows and each corpus row's sha and
disposition by reading the ledger home, while TOOL-dMindYourWords-1 names `--measure > <home>` as the
drain edit. The shell truncates the home before Python starts, so the drain edit as named still deletes
every tag row, drops the corpus rows' sha and disposition, and prints an honest-looking `carried 0`. This
unit makes `--measure` detect that its stdout is the home and read the rows it carries from the home's
index copy, and refuse when no copy survives, so the documented drain edit is safe as written.

## 2. Scope (IN)

- **S1** — The redirect detected. Before it reads the home, `--measure` compares its stdout with the
  home: `os.path.samestat(os.fstat(sys.stdout.fileno()), os.stat(<home>))`. When they are one file, the
  rows it carries, tag rows and corpus sha and disposition alike (TOOL-dMindYourWords-23 S1), come from
  the home's index copy, `git show :<home>`, and stderr prints `lexicon: --measure writes over the
  ledger home, so the rows it keeps come from its index copy`. Observed by AC1.
- **S2** — No surviving copy, no write. When stdout is the home and the index holds no copy of it, or
  when the home exists and is empty while its index copy holds rows, `--measure` prints nothing to
  stdout, exits 2, and stderr names the state and the remedy: `lexicon: the ledger home <home> was
  emptied before --measure could read it and no committed copy survives` or `... restore it with git
  checkout -- <home>`. Observed by AC2 and AC3.
- **S3** — One reader of the home. The choice of source is one function, `read_ledger_source(root,
  home)`, returning the home's rows and naming where they came from; the `--measure` merge
  (TOOL-dMindYourWords-23 §4 "The merge") reads through it, and S2's refusal is its raise. Observed by
  AC1 and AC4.
- **S4** — The docs. The debt-ledger section of `tools/lexicon/README.md` keeps `--measure > <home>` as
  the drain edit and states that the rows it keeps come from the index copy, so a drain is staged first.
  NOT OBSERVED as behaviour: prose has no grader beyond the carriers' own legs.

## 3. Non-goals (OUT)

- Which rows a writer carries: TOOL-dMindYourWords-23 S1 and S2, and TOOL-dMindYourWords-22's slice
  predicate.
- `--rebaseline`, which writes the home through the factory's `write_rows` and is never redirected over
  it.
- The tally lines `--measure` still prints to stdout before TOOL-dMindYourWords-29 S1 routes them to
  stderr: this unit's observations compare rows only, so they hold at either order.
- A `--write` flag: the documented edit becomes safe, so a second spelling of the drain edit is not
  needed (§8 F1).
- The left-shift checklist entry and selftest arm the report names under H4: a gate is its own unit
  (BUILD-METHOD M2).
- Kit version constants: minted at landing (`tools/push-main.sh:26-31`), so this unit moves none.

### Edges

- **consumes-from** `TOOL-dMindYourWords-23` — the `--measure` merge that reads the home for the rows it carries; without it there is no read to re-source
- **hands-off** `TOOL-dMindYourWords-37` — the redirect-safe drain edit, over which the batch re-observes unit 23's AC1 and carries the drift rows a shallow run does not measure (ids 5, 37)

## 4. Design

### Evidence

- Unit 23 §4 "The merge": `home_rows = read_rows(home) if home exists else []`, and S1 keeps each row's
  sha and disposition "the home already gives it" (`spec/2026-10-29-spec-TOOL-dMindYourWords-23.md`).
- Unit 1 calls `--measure > <home>` the drain edit (`spec/2026-10-29-spec-TOOL-dMindYourWords-1.md`, as
  unit 23 §4 Evidence quotes it).
- Measured on this Windows node under Git Bash, Python 3: with `> h.txt`, `os.path.samestat(
  os.fstat(sys.stdout.fileno()), os.stat('h.txt'))` printed `True` and `os.path.getsize('h.txt')`
  printed `0` from inside the process; piped to `cat` or redirected to another file it printed `False`.
  PINNED 2026-10-29.

### The source

```
def read_ledger_source(root, home):
    if home exists and samestat(fstat(stdout), stat(home)):
        blob = git show :<home>          # the index copy; absent -> raise S2's first refusal
        return parse(blob), "index"
    if home exists and size(home) == 0 and index copy holds rows:
        raise S2's second refusal
    return read_rows(home) if home exists else [], "worktree"
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_ledger_source` | function, `tools/lexicon/lexicon.py` | `py.function`; `lexicon.py --suggest read_ledger_source --as py.function` answered `OK` at writing |

### Rollout

Live at landing, one order after TOOL-dMindYourWords-23. Unit 23's AC1, which redirects over the home
and asks for an unchanged file, cannot pass on unit 23 as written; its builder meets it through M2's
AMEND route at that pass, and this unit's AC1 is the observation that replaces it.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`: S1, S2, S3
- `tools/lexicon/selftest.py`: the arm of §7
- `tools/lexicon/README.md`: S4

### Alternatives rejected

- **Document `--measure > tmp && mv tmp <home>`**: the edit an operator types first is still the
  destructive one, and the loss stays silent.
- **A `--write` flag that rewrites the home through `write_rows`**: safe, but it leaves the documented
  redirect destructive beside it, two spellings of one edit.
- **Read the carried rows from the index copy always**: a hand drain staged in the working file but not
  yet added would be resurrected from the index on every run.

## 5. Production-readiness checklist

- security — no new write path: stdout is still the only output, and the index read is a read.
- perf / scale — one `fstat` and, under a redirect, one `git show` per `--measure` run.
- error / empty / loading states — S2: an emptied home with no surviving copy refuses with exit 2 and
  never prints a ledger missing the carried rows.
- observability — S1's stderr line names the source on every redirected run; unit 23's `carried <n>`
  line follows it.
- risks — an operator who edited the home by hand and redirected without staging loses that unstaged
  edit to the shell's truncation; the index copy is the newest copy that survives, and the README says
  to stage a drain first.
- testing — AC1 to AC4 and the arm of §7.
- migration — none.
- user docs — `tools/lexicon/README.md` (S4).

## 6. Acceptance criteria

- **AC1** — When `python <kit>/lexicon.py --measure > .lexicon-debt.txt` runs, literally, in a fixture
  whose committed home holds two corpus rows and one tag row, `grep -c -F '<the tag row>'
  .lexicon-debt.txt` prints 1 and `diff <(git show :.lexicon-debt.txt | grep -v '^lexicon:' | tr -d '\r')
  <(grep -v '^lexicon:' .lexicon-debt.txt | tr -d '\r')` exits 0, and stderr names `index copy`.
  Red when: the redirect truncates the home before it is read and the tag row is gone.
  fixture: a scratch repository under `%TEMP%/<short>` with the kit copied and the home committed.
- **AC2** — When the same command runs in a fixture whose home is untracked and holds rows, it exits 2
  and stderr names `no committed copy survives`.
  Red when: the run prints a ledger without the rows it could not read.
- **AC3** — When `python <kit>/lexicon.py --measure > other.txt` runs after the home was emptied with
  `: > .lexicon-debt.txt` while its index copy holds rows, it exits 2 and stderr names `git checkout --`.
  Red when: an emptied home reads as a ledger with no rows to carry.
- **AC4** — When `python <kit>/lexicon.py --measure | cat` runs in AC1's fixture, stdout carries the tag
  row and stderr carries no `index copy` line.
  Red when: a non-redirected run reads the index instead of the working home.

## 7. Gates

`lexicon naming predicates` · `lexicon selftest` · `codebase-map kit selftest`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 · the drain edit run verbatim over a committed home holding a tag row, its failing case the `samestat` test cut out of `read_ledger_source`, under which AC1's home loses the tag row · none

## 8. Open questions

- **F1 — How does the drain edit stop deleting what it carries?** Options: (a) `--measure` detects
  stdout is the home and reads the index copy, refusing when none survives; (b) a `--write` flag that
  rewrites the home atomically, with the drain edit renamed; (c) document a temporary file and a move.
  (b) and (c) leave the documented redirect destructive. RESOLVED (agent, 2026-10-29, delegated): (a),
  rung 3, the one option under which the edit unit 1 documents is safe as typed. widens: none · relaxes:
  none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, promoted from review id 30 (HIGH, item H4) of the round-1 audit of
  units 22 to 29, with the redirect detection measured on a Windows node.

## 10. Reuse audit

The seam is the `--measure` merge TOOL-dMindYourWords-23 adds to `run()` (`tools/lexicon/lexicon.py:3518`)
and the factory's `read_rows`, which this unit feeds from one of two sources. `python
tools/codebase-map/reuse_lookup.py "keep the rows another producer owns when rewriting a shared ledger
file"` ranked name-stem helpers (`rows`, `row`, `extract_row`) and no reader that guards against a
redirect over its own input, so no existing seam fits the source choice itself.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon debt ledger keep its rows when tag findings and corpus findings share one population" --terms "lexicon-debt ledger drain measure rebaseline tags slice check_debt_pin widened shallow provenance"`
