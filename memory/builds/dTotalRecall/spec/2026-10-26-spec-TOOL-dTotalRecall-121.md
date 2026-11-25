# TOOL-dTotalRecall-121 — the closing review's minors: the record door's names and stage, sessionless claims, hyphenated slugs, section containment, unrun plants, the floor and the map replay's byte term

**Status:** INPROGRESS · rev-2 · 2026-11-25 · node d · Tier-2 · base acbb74bb · streams tooling · order 49

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief.md) | journal | TOOL-dTotalRecall-120 |
| [2026-11-25-prompt-TOOL-dTotalRecall-121-build-brief.md](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-121-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's ten MEDIUMs and its LOW (findings 1, 3, 7, 10, 11, 13, 14, 15, 16, 20 and 18), one scope item
each, as the review's minors batch. Each ends in an arm seen red on today's code. Beside them stand two leftovers of units
already built: two guides that misstate the feed check `TOOL-dTotalRecall-115` changed, and the writer census's red on
`TOOL-dTotalRecall-117`'s reader.

## 2. Scope (IN)

- **S1** — M1, finding 1. `tools/memory-tree/build_records.py` refuses a field name outside the key grammar, or a name
  given twice, in `write_record` and `write_new_record` alike, through one `check_field_keys` (§4). Observed by AC1.
- **S2** — M2, finding 3, the skeptic's corrected fix. `build_records.py#read_mint_authority` never reads an unnamed claim
  holder as this session: it continues with an announced line; a named holder refuses every other session, an absent
  one included (§4). Observed by AC2.
- **S3** — M3, finding 7. One helper, `build_records.py#add_to_index`, stages a written record and answers git's refusal;
  the three call sites (DERIVED, the review's list) undo the write and refuse on it (§4). Observed by AC3.
- **S4** — M4, finding 10. `tools/memory-tree/gov-claim.sh#check_claim_args` pre-checks a slug as `tools/push-main.sh` does,
  a letter then letters, digits and dashes, and leaves the grammar to the `id_grammar.py` match below it. Observed by AC4.
- **S5** — M5, finding 11. `tools/memory-tree/record_find.py#read_section` takes a `#<tag>` section only inside the record's own
  extent, in the candidate loop and in the pick, and raises FindError otherwise (§4). Observed by AC5.
- **S6** — M6, finding 13. `check-memory-hygiene.test.sh` runs `record_kinds.py --selftest`, asserting exit 0 and its PASS
  line, and `run_selftest` fails where a `PLANTS` member is in none of the plant tables it runs. Observed by AC6.
- **S7** — M7, finding 14, the class-level set. `tools/memory-tree/shape_run.py` gains `--fixture --plant <case>`, a red case
  per red branch of `check_shape_runs` and one green, each run by the suite (§4 "The shape-run plants"). Observed by AC7.
- **S8** — M8, finding 15. The suite runs the three census plants, and a join there reds where a `PLANTS` member of
  `build_records.py`, `record_causes.py`, `record_find.py` or `shape_run.py` is on no live line of the suite (§4 "The
  join"). Observed by AC8.
- **S9** — M9, finding 16. `FLOOR_ASSERTIONS` of the suite is pinned to the count a whole run prints, skips carried by
  `n_skip`, with its comment line. Observed by AC9.
- **S10** — M10, finding 20, the class-level fix. `tools/workflows/replay_scorer.py` decides the first act by a closed
  reading of each call, prints `term bytes: unarmed` where every run reads zero, and `derive_map_verdict` refuses `win`
  there (§4 "The byte term"). Observed by AC10.
- **S11** — L1, finding 18. `tools/playbook/adopt-playbook.sh` runs `cardinality-refused`, and `prose-pass`, which the join
  finds unrun too, and gains S8's join over `edge_grammar.py`'s plants (§4 "The join"). Observed by AC11.
- **S12** — The `shell-role` rows of `gov-claim.sh`, `adopt-playbook.sh` and the suite take the measured count through
  `ratchet.py widen`, unit `TOOL-dTotalRecall-121`, each read at the pass, since `TOOL-dTotalRecall-120` moves the
  suite's after this revision. A row whose measure did not move is left. Observed by AC12.
- **S13** — The `--feed` entry of `tools/unattended/VERBS.template.md` and section 7 of `tools/unattended/STOPS.template.md` say what
  `check_feed` walks and names for record events since `TOOL-dTotalRecall-115` (§4 "The feed sentences"), and
  `memory/guides/UNATTENDED-VERBS.md` and `memory/guides/UNATTENDED-STOPS.md` are installed from them by `bash
  tools/unattended/adopt-unattended.sh`. Observed by AC13.
- **S14** — `build_records.py#write_new_record`'s `read_key_fields` finds a record's Serves line through `tree_lib.py#BIND_RE`, the
  one binding grammar, and spells no Serves literal, so the writer census reads no red there (§4 "The Serves reader").
  Observed by AC14.
- **S15** — The sentences of `tools/memory-tree/README.md` and `tools/workflows/README.md` this unit makes false, and the one
  `TOOL-dTotalRecall-117` left false, are rewritten (§4 "The kit READMEs"). Observed by AC15.

## 3. Non-goals (OUT)

- The INSTANCE-ONLY fixes of findings 14 and 20, and the rejected fix of finding 3.
- Any edit of spec `TOOL-dTotalRecall-17`, which is CLOSED and frozen: S10's definition stands here and in the scorer's
  docstrings, and replaces its §4 bullet from this unit on.
- The replay's recorded verdict, which recall lost alone, and the map units held on `TOOL-dTotalRecall-111`.
- A join over other modules' plants: `deviation_join.py`, `ratchet.py` and `asbuilt_view.py` run theirs through a
  selftest of their own.
- A leg ceiling, a selftest budget row or a policy key moved.
- Any behaviour of the feed or its check: S13 states what stands. `help/loop.md`'s sentence on the feed is true and stays.
- A raise of a guide's byte or line cap, or a trim of a guide past S13's two paragraphs.

### Edges

- **consumes-from** external — the closing review's report and the landed units whose code it read
- **consumes-from** `TOOL-dTotalRecall-115` — its bytes of the symbol map, the shell-role rows, the claim CLI, edited after it, and the feed check its guides misstate
- **consumes-from** `TOOL-dTotalRecall-116` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, the record finder, edited after it
- **consumes-from** `TOOL-dTotalRecall-117` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, the record factory and its door-header plant, the ask and record door, edited after it
- **consumes-from** `TOOL-dTotalRecall-118` — its bytes of the symbol map, edited after it
- **consumes-from** `TOOL-dTotalRecall-119` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, edited after it
- **consumes-from** `TOOL-dTotalRecall-120` — its bytes of the symbol map, the shell-role rows, the hygiene suite and its floor, edited after it
- **hands-off** external — the close's next bar, the held suites and the landing, each the main loop's

## 4. Design

Read at `acbb74bb` on 2026-11-25; each of the eleven holds. Where the code differs from the report it says so. Re-read at
`20e9bd298` for rev-2, over units 115 to 119 as built: the eleven still hold, and the blob branch S5 edits is the one
`TOOL-dTotalRecall-116` rev-2 wrote.

### S1 — the field names

```python
FIELD_KEY = r"[A-Z][a-z-]+(?: [a-z]+)?"
FIELD = re.compile(r"^- \*\*(" + FIELD_KEY + r"):\*\* (.+)$")

def check_field_keys(fields):
    """Why one of `fields`' names is refused, or an empty string: outside `FIELD_KEY` whole, or given twice."""
```

`FIELD` is today's pattern, whose group is the report's grammar (DERIVED, that constant). Every required and optional
field of `KINDS`, every shape-run field and every `fields` row of the registry matches it (DERIVED 2026-11-25, a probe
over the three), and the transition and mailbox writers capitalise their names. Both writers raise ValueError with its
text before any other read of the fields.

### S2 — the sessionless claim

```python
me = os.environ.get("CLAUDE_CODE_SESSION_ID") or "absent"
holder = sessions[-1] if sessions else "absent"
if holder == "absent":
    return lines + [f"minted under the session rule: the claim of {build} names no session"], "owner"
if holder != me:
    raise ValueError(...)      # as today
return lines, "owner"
```

A named holder against an absent caller refuses as it does today, which the rejected fix would have admitted.

### S3 — the stage

```python
def add_to_index(root, rel):
    """git's refusal to stage `rel`, or an empty string where it is staged."""
    p = subprocess.run(["git", "add", "--", rel], cwd=str(root), capture_output=True, text=True, encoding="utf-8",
                       errors="replace")
    return "" if p.returncode == 0 else (p.stderr.strip() or f"git add exited {p.returncode}")
```

`write_new_record` removes the file it created and raises `<rel> was not staged, so it was removed: <git>`.
`gov_record.py#write_new_ask` puts `BACKLOG.md` back as it was, or removes it where it was absent, and raises the same, the minted
id unused; its put-back path after a failed read-back appends git's refusal to the line it already prints, exit 3. The
two scaffold writers of `gen_build_index.py` stage through `run`, which raises.

### S5 — the containment

In the candidate loop `any(s[0] == tag and cand["line"] <= s[1] <= cand["end_line"] for s in held)`; the final pick loses
its `or` half. A spec's H1 row and a file-stem row span the whole file, so a unit's key and a record's stem reach every
section they did (DERIVED, `record_extract.py#extract_record`); a key with a short extent names its own lines alone, and
no extent is widened. The blob branch, as `TOOL-dTotalRecall-116` leaves it, takes the same pick. The plant
`section-outside` is one record file defining two ids with its only section under the second: `show <first>#<tag>` is
refused and `show <file stem>#<tag>` prints the section.

### The shape-run plants

`PLANTS`, each over a scratch repository with two build folders, a review record per plant and one shape-run record
written by `build_records.write_record` from its line's parsed fields, then edited:

| Plant | Edit | Check |
|---|---|---|
| `equal` | none | exit 0, `green` |
| `malformed` | a required field's line deleted | exit 1, the record and the field |
| `cause-none` | `Caused-by` names no review | exit 1, the record |
| `cause-two` | a second build holds a review of that stem | exit 1, both paths |
| `review-no-line` | the review's line deleted | exit 1, `gives no parsed line` |
| `review-refused-line` | the review's line misspelled | exit 1, `gives no parsed line` |
| `field-differs` | one field's value moved | exit 1, the record, the field and both values |
| `field-absent` | the record lacks an optional field its line carries | exit 1, the field and `absent` |

Each prints `check_shape_runs`' lines, then `shape-run: fixture <plant> · exit <n>`, and exits with that code. The fixture
environment and removal are `deviation_join.py`'s. A host with no git prints `SKIP`, which the suite counts in `n_skip`.

### The join

One inline Python per suite. Over the memory suite: for each of the four modules, every `PLANTS` member must be a
whole word of a line that is no comment, and `record_kinds.py" --selftest` must be on one, whose coverage S6's own test
holds. Over `adopt-playbook.sh`: every plant `edge_grammar.py` admits, which its new `FIXTURE_PLANTS` tuple names and its
argument parser reads, must open a row. Run today it names the three census plants and no other in the memory suite, and
`cardinality-refused` and `prose-pass` in the playbook's (DERIVED 2026-11-25, that predicate, the same at `acbb74bb` and `20e9bd298`). What it does not check is
whether the arm asserts anything.

`prose-pass` prints `edges: plant prose-pass` and exits 0 (DERIVED 2026-11-25, its run), and `cardinality-refused` prints
its PASS line and exits 0 (DERIVED, the same).

### S9 — the floor

`TOOL-dTotalRecall-116` and `-119` raised it by reading, `-117` added no assertion, and `-120` raises it after this revision; it
stands at 837 (DERIVED 2026-11-25, the suite at `20e9bd298`) and is read again at the pass. After the last suite edit the main loop runs the
suite whole once and hands the printed count; the pass sets the floor to it and its comment names the commit, the node
and `n_skip`, in the form of the suite's `TOOL-aHastenedSweep-7` line.

### The byte term

```python
#: TOOL-dTotalRecall-121 S10: what a lens may run before its first act and still be reading. A shell call is a
#: read when every segment's program is one of these and nothing in it redirects to a file.
READ_PROGRAMS = SEARCH_PROGRAMS | {"cat", "head", "tail", "sed", "wc", "cd", "echo"}
GIT_READS = GIT_SEARCHES | {"diff", "show", "log", "blame", "status", "cat-file", "rev-parse"}
NON_ACTING_TOOLS = frozenset({"ToolSearch"})
DUP_REDIRECT = re.compile(r"[0-9]*>&[0-9-]")           # `2>&1`: the segment reader would split on its `&`
FILE_REDIRECT = re.compile(r"[0-9]*>{1,2}(.*)", re.S)  # a word opening a redirect, its target the rest or the next word
```

`derive_segment_program(ex, words)` is the program walk `measure_call_searches` holds today, moved out and called by
both, answering the program and, for git, its subcommand. `check_read_call(ex, name, tool_input)` is True for a runlog
`read` tool, a search tool or a `NON_ACTING_TOOLS` member, and for a shell call whose segments, after `DUP_REDIRECT` is
cut from the command, each run a `READ_PROGRAMS` program or a `GIT_READS` subcommand, hold no file redirect but one to
`/dev/null` or `$null`, and, for `sed`, no word matching `-[A-Za-z]*i` or `--in-place`. `measure_bytes_before_act` breaks
at the first call it answers False for.

`measure_map_experiment` adds `figures["armed"]`, False where every run of both arms read zero; then the bytes line reads
`term bytes: unarmed · every lens run read 0 before its first act`, and `derive_map_verdict` returns
`("unarmed", ["bytes"])` in place of `win`, so the last line is `verdict unarmed bytes`. A set that loses a term still
loses. Not read, each said in the docstring: a quoted word that opens with `>`, read as a redirect; `sed`'s `w` command; a
`find -exec`; and a call nested in `bash -c`.

### The feed sentences

`check_feed`'s record arm walks from every logged `record` commit of the ref that a branch or remote-tracking branch
reaches, compares the key sets, and prints `duplicate` for a key a second line holds; `unread <ref>` carries
`MEMORY_ROOT <value>` for a refused root and `walk` for a walk git refuses (read at `19a209739`). The append leaves out a
key the log holds. Today both guides say the walk goes up to the newest event, VERBS lists no `duplicate` for a record event and no refused walk. The
sentences, wrapped as their neighbours are:

```text
VERBS  … the commit, each key once: one the feed already holds is left out. `--feed check` also walks from every such event's commit
       that any branch or remote-tracking branch reaches and holds the events to those walks' keys, as sets, naming `missing`,
       `extra`, `duplicate` for a key a second line holds, or `unread` for a `MEMORY_ROOT` that is no plain relative path or a walk
       git refuses; `--feed rebuild` then …
STOPS  … walking from the feed's newest `record` commit, so a landing this node only fetched joins too, and leaving out each key
       the feed already holds; an uncommitted write never does. `--feed check` walks from every logged `record` commit a branch
       reaches, compares the two key sets and names a key logged twice `duplicate`.
```

Each guide is its template's bytes with any CR cut, which the adopter writes and its `--check` compares. The ceilings: no
`template-size-limits.txt` row names either template or guide. Hygiene check 6 prices each guide by `GUIDE_CAP_BYTES` 98304 and
`GUIDE_CAP_LINES` 1200 (DERIVED, `check-memory-hygiene.sh`, no conf override), which warns under this repository's `budgets.enforce`.
STOPS is under both, at 70937 bytes and 893 lines (DERIVED 2026-11-25, `wc`); VERBS is already over both, at 151348
bytes and 1657 lines (DERIVED 2026-11-25, `wc`), so its entry grows by a few lines of an announced breach, none refused.

### The Serves reader

`python tools/memory-tree/record_causes.py --cause-writers` reads one red under the tool root, the line of `read_key_fields` testing
`ln.startswith("**Serves:** ")` (DERIVED 2026-11-25, its run at `20e9bd298`). It reads a line and writes none, and the census grades
spelling. Two answers: the census marker on the line, or a read that spells no literal. The read: `tree_lib.py` already owns
the Serves grammar, so a literal prefix test is a second spelling of it, and a marker would keep that and grow the
exemptions by one. `tree_lib` is imported in that function today.

```python
serves = next((ln for ln in lines if (b := BIND_RE.match(ln)) and b.group("key") == "Serves"), "")
```

The name is `b`: a walrus inside the generator binds in `read_key_fields`, where `m` is the head match read below it. The raw
line is still what the key holds, so the door's own render reads as it did; a hand-written line behind a comment
prefix now enters the key as itself where it entered as nothing, and equals no render either way. With the edit made to the text,
`read_open_literals` over `build_records.py` lists no unkept literal, where today it lists one (DERIVED 2026-11-25, a probe).

### The kit READMEs

- `tools/memory-tree/README.md`, the record door: a claim naming no session mints under the session rule, announced (S2); a field
  name outside the key grammar or given twice, and a file git will not stage, are refused with nothing left written
  (S1, S3); and its `WHAT IT DOES NOT CHECK` says what `gov_record.py`'s docstring says since `TOOL-dTotalRecall-117`, in place
  of two builds holding one stem, which that unit's key ended. Its `show` sentence says the section lies inside the record
  (S5), and the `shape_run.py` row gains `--fixture --plant` (S7).
- `tools/workflows/README.md`, the `map-replay` paragraph: the byte term's first act is the closed reading (S10), and the
  verdict may be `verdict unarmed bytes`.

### Inventory

Minted: `FIELD_KEY`, `check_field_keys` and `add_to_index` in `build_records.py`; `PLANTS`, `build_fixture` and `run_fixture`
in `shape_run.py`; `FIXTURE_PLANTS` in `edge_grammar.py`; `READ_PROGRAMS`, `GIT_READS`, `NON_ACTING_TOOLS`,
`DUP_REDIRECT`, `FILE_REDIRECT`, `derive_segment_program` and `check_read_call` in `replay_scorer.py`; plant names. Every
function is a python-function cell with the verb its name opens.

### Files touched (estimate)

- `tools/memory-tree/build_records.py`
- `tools/memory-tree/gov_record.py`
- `tools/memory-tree/gov-claim.sh`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/record_find.py`
- `tools/memory-tree/record_kinds.py`
- `tools/memory-tree/shape_run.py`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/playbook/edge_grammar.py`
- `tools/playbook/adopt-playbook.sh`
- `tools/workflows/replay_scorer.py`
- `tools/memory-tree/README.md`
- `tools/workflows/README.md`
- `tools/unattended/VERBS.template.md`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `memory/project/shell-role.txt`
- `memory/map/generated/`
- `memory/builds/dTotalRecall/build/` (the widen record and this unit's ledger)

### Alternatives rejected

- **The act where a writing class or segment appears (finding 20's own fix).** Runlog has no detector of a writing
  segment, and a non-shell `other` call would still end the measure.
- **A leg of its own for `record_kinds.py --selftest`.** It moves the gate manifest and the kickoff manifest's stamp; the
  suite already holds the sibling arms (§8 F2).
- **One join module shared by both suites.** The two kits install apart, and each join is one inline read.
- **The census marker on S14's line.** It keeps a second spelling of a grammar `tree_lib.py` owns and adds an exemption.
- **The feed sentences in one guide alone.** The entry is the verb's contract and section 7 the feed's; each is read without
  the other, and each is wrong today.

## 5. Production-readiness checklist

- security — S1 and S2 deny more at the write boundary; S4 widens one pre-check the derived grammar still bounds.
- perf / scale — S6 runs every plant of `record_kinds.py` in the suite, its one cost (§8 F2); the other arms are fixtures.
- error / empty / loading states — S3 leaves nothing unstaged; S10's term says unarmed instead of zero.
- observability — every refusal names its subject; S2's line names the claim.
- risks — S5 refuses addresses that today print another record's section; S10 reads a call outside the closed set as an act.
- testing — AC1 to AC15 by the pass; §7's arms by the main loop.
- migration — none.
- user docs — S13 and S15; no page under `help/` states any of these behaviours.

## 6. Acceptance criteria

- **AC1** — When `python build_records.py --fixture --plant door-header` runs from `tools/memory-tree/`, its new cases
  `field-name-newline` (a `--field` name holding a line break and a `**Commissions:**` line) and `field-name-twice` each exit 2
  naming the field, with a clean status; and a probe calling `write_record` with each raises ValueError.
  Red when: only the value is checked. Today the first writes and stages the forged line.
- **AC2** — When a probe stubs `gen_build_index.read_claim_lines` and the lease read as free, `read_mint_authority` answers: both
  absent, the announced line and `owner`; the holder named and the caller absent, ValueError naming the holder; the
  holder absent and the caller named, the announced line.
  Red when: two absent sessions compare equal. Today the first answers no line.
- **AC3** — When the plants `door-header` and `ask-door` run their new `index-lock` case, the fixture's index lock held, each
  door exits 2 naming git's refusal, the record is absent or `BACKLOG.md` is as it was, and with the lock gone the
  same call prints `wrote`.
  Red when: the stage's exit is discarded. Today each prints `wrote` over an untracked record.
- **AC4** — When a probe over a scratch clone and bare remote whose landed policy reads `builds.slug-date` `in-slug` runs
  `bash gov-claim.sh slug d2026-10-26ClosedLoop --claimant <key>` and the `ask` verb for it, each exits 0; and `slug -x`
  and `slug 9x` exit 2 before any remote call.
  Red when: the pre-check refuses a dash. Today the first two exit 2.
- **AC5** — When `python record_find.py --fixture --plant section-outside` runs there, it prints `names no section of` and
  `exit 2` for the first id and the section for the file's stem; and `--plant unheld-blob` and the `missing-section`
  plant stand.
  Red when: the pick falls back to any section of the tag. Today the first exits 0.
- **AC6** — When `grep -c 'record_kinds.py" --selftest' tools/memory-tree/check-memory-hygiene.test.sh` runs, it prints 1
  (DERIVED, S6), and a probe that adds a name to `PLANTS` in a scratch copy of the module and calls `run_selftest` over a
  table-only stub reads a failure naming it.
  Red when: the call is cut, or a plant in no table passes.
  permission: the selftest itself is the main loop's; the pass runs single plants by `--fixture --plant`.
  cost: minutes, in the suite (a plant took 2.5 to 13 s, PINNED 2026-11-25, node d, a loaded machine).
- **AC7** — When `python shape_run.py --fixture --plant <case>` runs from `tools/memory-tree/` for each plant of §4's table, it
  exits and prints as its row says; and with each red branch of `check_shape_runs` cut in a scratch copy, that branch's
  plant exits 0.
  Red when: a branch has no plant that turns on it.
- **AC8** — When `python record_causes.py --fixture --plant <case>` runs for `literal-without-cause`, `duplicate-cause` and
  `unmarked-writer`, each prints its PASS line, and the suite's join, run as its inline text over a scratch copy with one
  of the three arms cut, names that plant.
  Red when: the join reads a comment line, or a member passes unnamed.
- **AC9** — When the suite's last raise comment is read, it names the count, the commit, the node and `n_skip` of one whole
  run, and `FLOOR_ASSERTIONS` equals that count and `n_skip` together.
  Red when: the floor stands under the observed count.
  permission: the whole run is the main loop's, which hands the printed line in a brief.
  figure: PINNED at that run.
- **AC10** — When a probe writes a transcript of `git diff a..b` (its result 500 bytes, PINNED), `sed -n 1,5p a.py | head`, a `ToolSearch`, the
  map-transcript's two searches, a `Read`, then `sed -i s/a/b/ a.py` and a `Read`, `measure_bytes_before_act` sums every
  result before the `sed -i` (500 PINNED in the probe); and `derive_map_verdict` over the boundary figures answers
  `("win", [])` armed and `("unarmed", ["bytes"])` with `armed` False.
  Red when: the shell `git diff` is the act. Today the measure reads zero.
- **AC11** — When `python tools/playbook/edge_grammar.py --fixture --plant cardinality-refused` and `--plant prose-pass` run,
  each exits 0 with its line, `grep -cE '^(cardinality-refused|prose-pass)[|]' tools/playbook/adopt-playbook.sh` prints 2
  (DERIVED, S11), and the join over a scratch copy with one row cut names that plant.
  Red when: a plant the parser admits has no row.
- **AC12** — When `python tools/gate-lint/sh_hygiene.py --shell-role --measure . ':!memory/'` runs, the three paths of S12 read
  the counts their rows hold.
  Red when: a row stands under or over its measure.
- **AC13** — When `grep -c 'newest one' tools/unattended/VERBS.template.md tools/unattended/STOPS.template.md` runs, it prints 0 for each
  (DERIVED, S13); the `--feed` entry, cut from its bullet to the next, names `duplicate` twice and `walk git refuses` once its
  line breaks are folded; section 7 of the stops template names `duplicate`; and `cmp` of each template with its guide,
  any CR cut, finds no difference.
  Red when: either template keeps the old walk, or a guide is edited by hand. Today each template prints 1 (DERIVED, that grep).
- **AC14** — When `python tools/memory-tree/record_causes.py --cause-writers` runs, it prints no `RED` line naming
  `tools/memory-tree/build_records.py`, `grep -c 'startswith("\*\*Serves' tools/memory-tree/build_records.py` prints 0 (DERIVED, S14), and
  `python build_records.py --fixture --plant door-header` from `tools/memory-tree/` still prints its replay as `exists` and every other
  case as it does at `20e9bd298`.
  Red when: the literal stands, or the walrus takes the head match's name and the key loses its title. Today the census prints one red.
- **AC15** — When `grep -c 'two builds holding a' tools/memory-tree/README.md` runs, it prints 0 (DERIVED, S15), and the greps of `names no session`,
  `--fixture --plant` on the `shape_run.py` row, and `verdict unarmed bytes` in `tools/workflows/README.md` each print at
  least one line.
  Red when: a README still states what the code no longer does.

## 7. Gates

`memory hygiene` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `encoding posture (text IO names its encoding)` · `python reads (a name never bound, an import outside its guard)` · `portability (shell lines only shrink)` · `recall floor` · `recall floor arms` · `ratchet (never gains)` · `ratchet (both ways)` · `memory-hygiene self-test` · `build-index selftest` · `record causes (causes and orphans over the legacy population)` · `record-kinds` · `review-replay selftest` · `playbook render selftest` · `shape-run records (each record equals its review line)` · `remote literals (kit code names no remote)` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures` · `unattended kit gate` · `unattended skill wiring` · `docs`

S13 and S15 are prose, which no arm reads past the pair compares of the legs above. S14's arm stands: the `record causes` leg is
red on today's line, and the `door-header` cases red a key that loses a field.

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC1 AC3 · the `door-header` literal over the name, duplicate and index-lock cases, and `ask-door`'s index-lock case, red on today's door · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 · three claim arms beside the lease block (both absent, holder named and caller absent, holder absent and caller named), red on today's compare · `FLOOR_ASSERTIONS`, the three carried by `n_skip` with that block
New arm: tools/memory-tree/gen_build_index.py · covers AC4 · `test_slug_claims` runs the hyphenated slug through both verbs over a remote whose policy reads `in-slug`, red on today's pre-check · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 AC7 · the `section-outside` plant and the shape-run plants, red on today's pick and on each branch cut · `FLOOR_ASSERTIONS`
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC6 AC8 AC9 · the selftest call, the three census plants and the join, red on an arm cut · `FLOOR_ASSERTIONS`, pinned to the observed count
New arm: tools/workflows/replay_scorer.py · covers AC10 · `map-transcript` opens with the `git diff`, the `sed -n` pipe and the `ToolSearch` and acts on the `sed -i`, and `map-verdict` adds the unarmed set, red on today's loop · none, the declared arm count stands
New arm: tools/playbook/adopt-playbook.sh · covers AC11 · the two rows and the join, red on a row cut · none

## 8. Open questions

- **F1 — Which binding line does a unit the closing review added carry?** The carries join reds a chain spec carrying
  nothing and derived from nothing. Options: (a) `**Derived:**` naming `PLAY-dClosedLoop-2`, the ruling that a chain run
  carries the units it adds, as `TOOL-dTotalRecall-114` §8 F1; (b) a part of another unit's clause, which the parts join
  reds. RESOLVED (agent, 2026-11-25, delegated): (a), the one survivor. widens: none · relaxes: none
- **F2 — Does `record_kinds.py --selftest` run in the suite or on a leg of its own?** The review allows either. Options:
  (a) the suite, no manifest edit, its minutes inside the suite's 4800 s ceiling (DERIVED, the leg's row) and its
  selftest budget row; (b) a leg, which moves the gate manifest, the kickoff manifest's stamp and two evidence
  registries. Recommendation and pick: RESOLVED (agent, 2026-11-25, delegated): (a); where the main loop measures the
  suite past its ceiling it moves the call to a leg rather than the bound. widens: none · relaxes: none
- **F3 — Does S11 arm `prose-pass` too?** Options: (a) yes; (b) the join excepts it. An exception is the class the join
  ends. RESOLVED (agent, 2026-11-25, delegated): (a). widens: none · relaxes: none
- **F4 — Does S14 mark the line or stop spelling the literal?** Options: (a) read through `tree_lib.py#BIND_RE`; (b) the census
  marker. (b) keeps a second spelling of the Serves grammar. RESOLVED (agent, 2026-11-25, delegated): (a). widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft, from the closing review's M1 to M10 and L1.
- rev-2 · 2026-11-25 · S12 S13 S14 S15 §1 §3 §4 §5 §7 AC13 AC14 AC15 · two leftovers of built units taken, the feed guides and the
  Serves reader; the README claim corrected and the floor and shell-role counts read at the pass; from
  `2026-11-25-prompt-TOOL-dTotalRecall-120-divergence-fold-brief`.

## 10. Reuse audit

The seams, each read at `acbb74bb`: `build_records.py#FIELD` and `check_line_break`; `placement.py#read_lease_class`,
whose rule S2 takes; `gen_build_index.py#run_claim_cli` and `test_slug_claims`; `record_find.py#read_section`;
`deviation_join.py#set_fixture_env` and `remove_tree`; `replay_scorer.py#measure_call_searches`, whose program walk S10
moves out; `tools/runlog/extract.py#extract_segments`; `adopt-playbook.sh`'s `run_plant_rows`.
`python tools/codebase-map/reuse_lookup.py "check that every fixture plant a module declares is run by a suite"` and the
same over "stage a written file and undo the write when the add fails" ranked generic writers alone: no existing seam
fits the join or the stage helper. The task's build-folder walks and `id_grammar.py#read_kept_reason` are no seam here.

Recall terms used: `python tools/memory-recall/query.py "the closing review's minors over the record door, the claim CLI and the unrun plants" --terms "refusal-branch-with-no-arm failed-stage-reads-as-nothing-staged two-answers-to-one-question floor-left-below-the-arms-it-guards armed-but-unreachable-rule check_field_keys slug grammar map replay bytes"`
