# TOOL-dTrackedAtlas-12 — the closing review's round-2 minors: one stamp-rules table for writer and reader, a relayed refusal the Atlas can act on, one `--ref` rule, the pane reds re-recorded

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · records-only · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-12-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-12-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-12-red-fix-10.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-12-red-fix-10.md) | red-fix | — |
| [2026-11-19-build-TOOL-dTrackedAtlas-12-red-fix-11.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-12-red-fix-11.md) | red-fix | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-12-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-12-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-12-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-12-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The round-2 closing review's five minors close together. The stamp's field rules live in one table
that the writer and the reader both check, so `--out` refuses a stamp `--check --page` would call
unstamped (M1). A refusal the Atlas relays from the derivation names a remedy the Atlas honours,
never an option it does not take (M2). `check_page` holds no second `--ref` rule beside
`read_options`'s (L3). And the main loop re-observes the two pane reds on pages named by the commit
that wrote them, recorded in the form spec 11 states (L1, L2).

## 2. Scope (IN)

- **S1** — M1: the read rules of the stamp move out of `read_stamp` into one module-level table,
  `STAMP_RULES`, read through one function, `check_stamp`. `read_stamp` answers through it with the
  reason text it gives today. Observed by AC1 and AC3.
- **S2** — M1: `build_stamp` checks the stamp's `commit` and `default_ref` against `STAMP_RULES`
  before any git call, the state's `default_commit` against the table's `commit` rule, and the whole
  stamp against every rule of the table before it returns it, raising `StampError` with
  `check_stamp`'s reason. So `--out` exits 1 with `atlas: cannot stamp the page:` on a stamp the
  reader would refuse, and every stamp it writes reads current. Observed by AC2, AC4 and AC5.
- **S3** — M2: a `StateError` the Atlas relays from `TOOL-dTrackedAtlas-1`'s module, in
  `derive_actual` and in `read_landings`, passes through `render_state_error`, which rewrites the
  module's trailing advice `pass --default-ref <rev>` into a remedy the Atlas honours, by §4 "The
  relayed refusal" and §7 F1. Observed by AC6, AC7 and AC8.
- **S4** — L3: `check_page` holds no refusal of its own for a `ref` starting with `-`, so the one
  rule for a dash value of `--ref` is `read_options`'s, with its one text `--ref takes a value`.
  Observed by AC9.
- **S5** — L1 and L2: the main loop re-observes `TOOL-dTrackedAtlas-2`'s AC12 and
  `TOOL-dTrackedAtlas-3`'s AC8 in the browser pane, each red on a page written by the generator at
  the commit that criterion's spec names, and rewrites both observations in ledgers 2 and 3 by §4
  "The pane observations at the close". NOT OBSERVED by this unit's criteria: the builder's pass
  cannot open the browser pane. The builder writes no pane observation, claims none, and does not
  edit ledger 2 or ledger 3.

## 3. Non-goals (OUT)

- The functions this unit edits are `build_stamp`, `read_stamp`, `check_page`, `derive_actual` and
  `read_landings` of the generator; it adds the constants and functions of §4 "Inventory". `main`,
  `read_options`, `derive`, `derive_input_digest`, the module docstring and the template stay as
  `TOOL-dTrackedAtlas-10` and `TOOL-dTrackedAtlas-11` leave them.
- The content of any rule. Each row of `STAMP_RULES` reads as `read_stamp`'s local table reads at
  `d23a030c9`; the `default_ref` rule is not widened to git's ref format, by §4 "Alternatives
  rejected".
- A `--default-ref` option on the Atlas, and a refusal of an unknown option: §7 F1. An unknown
  argument stays ignored, as `TOOL-dTrackedAtlas-11` leaves it.
- `TOOL-dTrackedAtlas-1`'s module. Its `resolve_default_ref` keeps its advice, which is true of its
  own command line.
- The left-shift gates the round-2 review names. The disposal files whatever
  `review.left-shift` earns; this unit builds no gate, no suite arm and no gotcha file.
- Any browser-pane observation, any edit to ledger 2 or ledger 3, and any claim that S5 is done:
  those are the main loop's at the close.
- The specs of units 1 to 11, which are CLOSED and stay frozen. `TOOL-dTrackedAtlas-11` §3 kept
  `check_page`'s dash guard; this unit, on top of it, takes the review's L3 instead.
- Any file under `tools/`, any new file under `memory/builds/dClosedLoop/build/`, and the page,
  which is never committed.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-10` — the stamp, `read_stamp`'s rules, `build_stamp`,
  `read_landings` and `check_page`, which this unit edits and whose exit codes it keeps.
- **consumes-from** `TOOL-dTrackedAtlas-11` — `read_options`, whose refusal of a dash value of
  `--ref` is what leaves `check_page`'s guard unreachable through `main`.
- **consumes-from** `TOOL-dTrackedAtlas-9` — `resolve_default_ref` and the advice text its
  `StateError` ends with, which `render_state_error` rewrites.
- **consumes-from** `TOOL-dTrackedAtlas-3` — the page check's exit table, and AC8, whose pane red
  the main loop re-observes.
- **consumes-from** `TOOL-dTrackedAtlas-2` — AC12, whose pane red the main loop re-observes.

## 4. Design

### Where it lands

The generator is `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`,
read at `d23a030c9` for every claim below. The reader's rules are a dict local to
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#read_stamp`; the
writer's checks are three inline tests in
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#build_stamp`, which
test `default_ref` only for being a string
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@d23a030c993ef3e14c4a860c0965f777db5edcfa:861`).
`read_stamp` requires the pattern `[A-Za-z0-9._][A-Za-z0-9._/-]*`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@d23a030c993ef3e14c4a860c0965f777db5edcfa:900`),
so a default branch named `release+2` is stamped and then read unstamped forever. Nothing checks
that `landings` is non-empty on the write side either: a state with no builds is stamped with `{}`,
which the reader refuses.

`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#resolve_default_ref`
ends three `StateError` texts with `pass --default-ref <rev>`. `derive_actual` relays them as
`atlas: chain state: <text>`, and `read_landings` as a `StampError` that `check_page` prints after
`atlas: cannot check:`. The Atlas reads no such option. Its fourth refusal,
`--default-ref takes a revision, not <name>`, is unreachable from the Atlas: the derive branch
passes no default ref, so the name is the ladder's `refs/remotes/<remote>/<branch>`, and the page
check passes the stamp's name, which the `default_ref` rule forbids to start with `-`.

`check_page` opens with `if ref.startswith("-")`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@d23a030c993ef3e14c4a860c0965f777db5edcfa:926`).
Its one caller is `main`, which refuses a dash value through
`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#read_options` first.

### The stamp-rules table

```python
STAMP_RULES = {field: rule, ...}   # read_stamp's seven rows, moved whole, beside STAMP_SCHEMA

def check_stamp(stamp, fields=None):
    """The reason `the stamp's <field> field fails its rule:<value>` for the first field of `fields`
    (None: every field of STAMP_RULES, in the table's order) whose rule `stamp.get(field)` fails,
    else None."""
```

The reason text is `read_stamp`'s today, byte for byte, so the reader's answers do not move.
`read_stamp` keeps its own refusals of a page that cannot be read, has no marker, does not parse or
carries no stamp, and then returns `(None, reason)` or `(stamp, None)` from `check_stamp(stamp)`.

### The writer

`build_stamp` keeps its order and its git reads, and checks in three places:

1. Before any git call, `check_stamp` over a dict of the state's `commit` and `default_ref`, with
   `fields` naming those two, so an unusable commit or ref never reaches git. Its reason is the
   table's, so a state with no commit now reads `the stamp's commit field fails its rule:null`.
2. The state's `default_commit`, which is no stamp field, by `STAMP_RULES["commit"]`, keeping its
   text `the chain state carries no 40-hex default_commit, but <value>`.
3. The stamp it is about to return, by `check_stamp(stamp)`.

A reason at any of the three raises `StampError(reason)`, which `main` already prints as
`atlas: cannot stamp the page: <reason>` with exit 1 before it writes a page.

### The relayed refusal

```python
STATE_ADVICE = "pass --default-ref <rev>"
DERIVE_REMEDY = "fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH"
CHECK_REMEDY = "fetch the default branch the stamp names, or regenerate the page"

def render_state_error(error, remedy):
    """The text of `error`, TOOL-dTrackedAtlas-1's StateError, with a trailing STATE_ADVICE,
    an option the Atlas does not take, rewritten as `remedy`; any other text unchanged."""
```

`derive_actual` exits with `atlas: chain state: {render_state_error(e, DERIVE_REMEDY)}`; the derive
branch reaches the remote ladder of `tools/lib/resolve_remote.py#resolve_remote`, which reads both
environment names. `read_landings` raises `StampError(render_state_error(e, CHECK_REMEDY))`; only
`check_page` reaches the advice through it, because `build_stamp` passes the state's
`default_commit` and so resolves no name. A `ChainError` carries no advice and passes unchanged.

### The page check's `--ref` rule

`check_page` loses its first two lines, the dash test and its `--ref takes a revision` refusal.
`read_options` stays the one rule, answering `--ref -x` through `main` with exit 2 and
`atlas: cannot check: --ref takes a value`. A library caller passing a dash ref to `check_page`
reaches `git rev-parse --verify -q` as an argument, which resolves no commit and answers exit 2;
`git rev-parse --verify -q "-x^{commit}"` exited 1 on 2026-11-19.

### The pane observations at the close

The main loop makes these after the last unit is terminal and before the bar. It serves each page
with `python -m http.server` from the run's scratch directory through a temporary launch
configuration that it deletes afterwards, and opens it in the browser pane.

| Ledger | Criterion | Green | Red page, written by |
|---|---|---|---|
| `2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md` | `TOOL-dTrackedAtlas-2` AC12 | the close tip's page, by that criterion | the generator at `9e21ac760`, run with `--out` alone, since `--claims` arrived with unit 2 |
| `2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md` | `TOOL-dTrackedAtlas-3` AC8 | the close tip's page, by that criterion, with `--check --page` on it answering `atlas: current` | the generator at `f1b02b3eb`, run with `--claims none --out` |

Each red page is written in a clone at `%TEMP%/ta12pn`, checked out detached at the named commit,
to the scratch directory, and named in the ledger by that commit and by `git hash-object` of the
written file. The ledger 3 red also runs the close tip's `--check --page` on its page and records
the `atlas: unstamped` line and exit 1. Whether each old generator runs in such a clone is
UNVERIFIED; if one does not, the main loop records that in the line in place of the red, and the
unit's disposition follows the unattended protocol.

In each ledger, the section opening `## Observed at the close` is deleted, and one paragraph is
written directly beneath the "Owed to the close" line, opening with the precedent's words
`Owed to the close, and since observed by the main loop in the browser pane:`
(`memory/builds/aClearedLedger/build/2026-11-13-build-TOOL-aClearedLedger-3-1-acceptance-ledger.md@d23a030c993ef3e14c4a860c0965f777db5edcfa:7`),
naming the criterion, what the pane showed for green at the close tip's commit, and for red the
commit and page hash. The words `page home's copy` appear in neither ledger after it. The edit is
made under a `Pass: none` commit. The main loop's own check is
`grep -c "since observed by the main loop in the browser pane"` printing `1` and
`grep -c "^## Observed at the close"` printing `0` over each ledger.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `STAMP_RULES` | constant, new | `{field: rule}`, `read_stamp`'s rows moved whole |
| `check_stamp(stamp, fields=None)` | function, new | the first failing field's reason, else `None` |
| `STATE_ADVICE` | constant, new | `pass --default-ref <rev>` |
| `DERIVE_REMEDY` | constant, new | the derive branch's remedy, by §4 "The relayed refusal" |
| `CHECK_REMEDY` | constant, new | the page check's remedy, by §4 "The relayed refusal" |
| `render_state_error(error, remedy)` | function, new | the relayed text, by §4 "The relayed refusal" |

Both new function names lead with a verb `.lexicon.conf` declares, checked with
`python tools/lexicon/lexicon.py --suggest <name> --as py.function` on 2026-11-19, and the four
constants are in the screaming case the `py.constant` cell grades.

### What it does not check

- A rewording of the module's advice: `render_state_error` matches `STATE_ADVICE` as a suffix, so a
  reworded advice passes through as written. AC6 and AC7 are the observation that it does not today.
- Whether a remedy works on a given clone: a clone with no remote has no default branch to fetch.
- That a field the writer never sets wrongly, such as `schema`, can be refused on the write side;
  the table checks it, and AC3 observes each rule on the read side.

### Files touched (estimate)

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-12-ledger.md`

### Alternatives rejected

- Widening the `default_ref` rule to git's ref format, the review's second M1 fix. The page check
  passes the stamp's name to `git rev-parse`, so the rule is a read boundary; admitting `@` admits
  `@{...}` revision syntax there. The brief picks the writer refusing what the reader refuses.
- One shared `default_ref` constant, finding 5's fix, judged INSTANCE-ONLY: the other fields keep
  two copies.
- Checking the whole stamp only at the end of `build_stamp`: a state with no commit would reach
  `read_git` with `None` and end in a traceback.

## 5. Acceptance criteria

The commands run in a clone of the worktree at `%TEMP%/ta12fx`, from the clone's root, with these
names set. Pages and probe output go to the run's scratch directory, never into the clone or the
worktree; every generation passes `--claims none`; the real repository's refs are never written.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
WT=<the worktree root>
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
S=<the run's scratch directory>
BEFORE=09b2b8f67dfb23e0d47b9fef155fce54dc8c54b8   # the generator's blob at d23a030c9
export PYTHONDONTWRITEBYTECODE=1
unset GOV_REMOTE GOV_DEFAULT_BRANCH
git clone -q --shared "$WT" "$TEMP/ta12fx" && cd "$TEMP/ta12fx"
cp "$WT/$ATLAS" "$ATLAS" && git commit -q --allow-empty -am "fixture: unit 12's generator"
T=$(git rev-parse HEAD)
git update-ref refs/remotes/origin/main "$T"
git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```

Each red runs the generator before this unit: `git show "$BEFORE" > "$ATLAS"`, the red command,
then `git checkout -q -- "$ATLAS"`. A red named as a staged break edits the clone's copy the same
way and restores it. The probes below sit in the scratch directory, each loading the generator by
path as `a`:

```python
# stamp_readers.py <generator>
import ast, sys
tree = ast.parse(open(sys.argv[1], encoding="utf-8").read())
funcs = {f.name: f for f in tree.body if isinstance(f, ast.FunctionDef)}
def calls(f, name):
    return any(isinstance(n, ast.Call) and ast.unparse(n.func) == name for n in ast.walk(f))
for name in ("build_stamp", "read_stamp", "check_stamp"):
    f = funcs.get(name)
    print(name, "absent" if f is None else
          f"check_stamp={calls(f, 'check_stamp')} re.fullmatch={calls(f, 're.fullmatch')}")
```

```python
# stamp_rules.py <generator> <page> <scratch>
import importlib.util as u, json, sys
s = u.spec_from_file_location("atlas", sys.argv[1]); a = u.module_from_spec(s); s.loader.exec_module(a)
stamp, reason = a.read_stamp(sys.argv[2])
print("fields", *a.STAMP_RULES, "| stamp", *(stamp or {reason: 0}))
bad = {"schema": 1, "commit": "abc", "default_ref": "refs/remotes/origin/release+2", "landings": {},
       "digest": "x", "inputs": ["../x"], "dirty": "x"}
for field in a.STAMP_RULES:
    broken = dict(stamp, **{field: bad[field]})
    copy = f"{sys.argv[3]}/bad-{field}.html"
    with open(copy, "w", encoding="utf-8") as f:
        f.write(a.MARK + json.dumps({"stamp": broken}) + "</script>")
    said = a.read_stamp(copy)[1]
    print(field, said == a.check_stamp(broken), said)
```

```python
# stamp_writer.py <generator>
import importlib.util as u, subprocess, sys
s = u.spec_from_file_location("atlas", sys.argv[1]); a = u.module_from_spec(s); s.loader.exec_module(a)
head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
one, ref = [{"slug": "dTrueNorth"}], "refs/remotes/origin/main"
cases = {
    "no-default-commit": {"commit": head, "default_ref": ref, "builds": one},
    "plus-ref": {"commit": head, "default_ref": "refs/remotes/origin/release+2", "default_commit": head, "builds": one},
    "no-builds": {"commit": head, "default_ref": ref, "default_commit": head, "builds": []},
    "whole": {"commit": head, "default_ref": ref, "default_commit": head, "builds": one},
}
for name, state in cases.items():
    try:
        a.build_stamp({"state": state})
        print(name, "stamped")
    except a.StampError as e:
        print(name, "refused:", e)
```

```python
# state_relay.py <generator>
import importlib.util as u, sys
s = u.spec_from_file_location("atlas", sys.argv[1]); a = u.module_from_spec(s); s.loader.exec_module(a)
m = a.load_build_state()
try:
    print("resolved", *m.resolve_default_ref(str(a.REPO), None))
except m.StateError as e:
    print(a.render_state_error(e, a.DERIVE_REMEDY))
```

- **AC1** — When `"$PY" "$S/stamp_readers.py" "$ATLAS"` runs, it prints
  `build_stamp check_stamp=True re.fullmatch=False`, `read_stamp check_stamp=True re.fullmatch=False`
  and `check_stamp check_stamp=False re.fullmatch=False`.
  Red when: the generator before this unit, where `build_stamp` and `read_stamp` each read
  `check_stamp=False re.fullmatch=True` and `check_stamp` reads `absent`.
- **AC2** — When `"$PY" "$ATLAS" --claims none --out "$S/p0.html"` runs at `$T` and
  `"$PY" "$ATLAS" --check --page "$S/p0.html"` follows, the check exits 0 with `atlas: current`.
  Red when: a staged `check_stamp` ignores `fields`, so the writer's first check grades the
  two-field dict against every row, and `--out` exits 1 with
  `atlas: cannot stamp the page: the stamp's schema field fails its rule:null`, writing no page.
  cost: one generation of the page, minutes.
- **AC3** — When `"$PY" "$S/stamp_rules.py" "$ATLAS" "$S/p0.html" "$S"` runs, its first line lists
  the same fields in the same order on both sides of `|`, and each following line reads
  `<field> True the stamp's <field> field fails its rule:` and the bad value, one per field.
  Red when: `STAMP_RULES` lacks a row, observed with its `dirty` row deleted, where the first line's
  two sides differ and no `dirty` line prints.
  figure: the field count is DERIVED from `STAMP_RULES`; seven at `d23a030c9`.
- **AC4** — When `"$PY" "$S/stamp_writer.py" "$ATLAS"` runs, it prints
  `no-default-commit refused: the chain state carries no 40-hex default_commit, but None`,
  `plus-ref refused: the stamp's default_ref field fails its rule:"refs/remotes/origin/release+2"`,
  `no-builds refused: the stamp's landings field fails its rule:{}`, and `whole stamped`.
  Red when: the generator before this unit, which prints `plus-ref stamped` and `no-builds stamped`;
  and, for the first case, a staged `build_stamp` with no `default_commit` check, which prints
  `no-default-commit stamped`.
- **AC5** — When `git update-ref refs/remotes/origin/release+2 "$T"` runs and
  `GOV_DEFAULT_BRANCH=release+2 "$PY" "$ATLAS" --claims none --out "$S/p-plus.html"` follows, it
  exits 1 with the stderr line
  `atlas: cannot stamp the page: the stamp's default_ref field fails its rule:"refs/remotes/origin/release+2"`,
  and `test -e "$S/p-plus.html"` exits 1. The ref is then deleted.
  Red when: the generator before this unit, which exits 0 writing the page, and on which
  `--check --page "$S/p-plus.html"` prints `atlas: unstamped` with exit 1.
  cost: two derivations, minutes each.
- **AC6** — When `"$PY" "$S/state_relay.py" "$ATLAS"` runs in each of three states, it prints one
  line ending `fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`, and
  `grep -c -- "--default-ref"` over the three lines prints `0`. The states are
  `git update-ref -d refs/remotes/origin/main`, whose line names
  `refs/remotes/origin/main resolves to no commit`; that ref restored to `$T` and
  `git symbolic-ref -d refs/remotes/origin/HEAD`, whose line begins
  `the remote ladder names no default branch here`; and `refs/remotes/origin/HEAD` restored as the
  setup writes it and `GOV_REMOTE=nosuch`, whose line names `export GOV_REMOTE=<remote>`. With every ref restored and `GOV_REMOTE` unset, it
  prints `resolved refs/remotes/origin/main` and `$T`.
  Red when: a staged `render_state_error` returns its error's text unchanged, where each of the
  three lines ends `pass --default-ref <rev>`.
- **AC7** — When `git update-ref -d refs/remotes/origin/main` runs and
  `"$PY" "$ATLAS" --check --claims none` follows, it exits 1 with one stderr line beginning
  `atlas: chain state: the default-branch ref refs/remotes/origin/main resolves to no commit` and
  ending `fetch the default branch, or name it with GOV_REMOTE and GOV_DEFAULT_BRANCH`. The ref is
  then restored to `$T`.
  Red when: the generator before this unit, whose line ends `pass --default-ref <rev>`.
  cost: two derivations, minutes each.
- **AC8** — When `git update-ref -d refs/remotes/origin/main` runs and
  `"$PY" "$ATLAS" --check --page "$S/p0.html"` follows, it exits 2 with nothing on stdout and one
  stderr line beginning `atlas: cannot check: the default-branch ref refs/remotes/origin/main` and
  ending `fetch the default branch the stamp names, or regenerate the page`. The ref is then
  restored to `$T`.
  Red when: the generator before this unit, whose line ends `pass --default-ref <rev>`.
- **AC9** — When `grep -c "takes a revision" "$ATLAS"` runs it prints `0`, and
  `"$PY" "$ATLAS" --check --page "$S/p0.html" --ref -x` exits 2 with nothing on stdout and the one
  stderr line `atlas: cannot check: --ref takes a value`.
  Red when: the generator before this unit, where the `grep` prints `1`.

## 6. Gates

The close runs the plain bar once. The legs below are those the files touched keep green, the last
two owed because `tools/gate-legs.json` guards `memory/builds/dClosedLoop/build/` with them. No
suite arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

- **F1 — Does the Atlas take the `--default-ref` its relayed refusal advises, or does the relayed
  text stop advising it?**
  (a) Take it in both branches: `main` reads `--default-ref` and passes it to `derive_actual`'s
  derivation and to `check_page`'s landing read. Rejected: in the page check it overrides the name
  the stamp's digest folds. Folding the override stales every page whose name is spelled another
  way, and folding the stamp's name while measuring on another gives the digest a second meaning.
  `TOOL-dTrackedAtlas-10` §7 F3 (c) rejected this option for the page check.
  (b) The relayed text stops advising it: the Atlas rewrites the advice into remedies it honours,
  the review's M2 fix, judged SOUND by its skeptic.
  (c) Take it in the derive branch only, and rewrite the advice in the page branch. Rejected: it
  adds an option no stated criterion and no caller needs, as `TOOL-dTrackedAtlas-9` §4
  "Alternatives rejected" found; the ladder's `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` already name the
  default branch in any clone with a remote, and the charter's `[yagni]` rule builds no surface for
  the remaining case, a clone with no remote, which no caller of the Atlas runs in.
  (d) Refuse every unknown option in `main`, the review's alternative. Rejected as the pick: it
  stops the silent drop but still prints a remedy the Atlas cannot take.
  The brief directs the pick by the review's fix; (b) satisfies every criterion here and trips none
  of M3's vetoes, adding no option, write path or governance carrier.
  RESOLVED (agent, 2026-11-19, delegated): (b), by the brief's direction and M3's rule.

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft, from the round-2 closing review's M1, M2, L1, L2 and L3
  (2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2) and the brief
  2026-11-19-prompt-TOOL-dTrackedAtlas-12-spec-brief.

## 9. Reuse audit

The seam extended is the generator's own stamp boundary: `read_stamp`'s rule table becomes the one
table, and `build_stamp` reads it rather than a copy. The relay reuses `read_landings` and
`derive_actual`'s existing catch, and the remedies name the remote ladder's own environment names.
`python tools/codebase-map/reuse_lookup.py "one table of field rules checked by both the writer and the reader of a record"`
ranked name-stem helpers only, `read_text`, `write`, `check` and the like, none a shared rule table
for a record's writer and reader, so no existing seam outside the generator fits. The recall probe
returned this build's own round-2 review, specs 10 and 11, and the loop kit's refusal-remedy work
for `TOOL-dBoundRoles-26`, which routes a remedy to an actor and is no relay rewrite.

Recall terms used: `python tools/memory-recall/query.py "how does a writer refuse what its reader would refuse, and how does a tool relay a refusal naming an option it does not take" --terms "stamp rules table writer reader refusal build_stamp read_stamp default-ref relayed remedy atlas dTrackedAtlas"`
