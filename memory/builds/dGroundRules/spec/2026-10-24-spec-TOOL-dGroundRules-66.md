# TOOL-dGroundRules-66 — `--dispatch`'s sibling set leaves out a terminal unit's keys, through the one open-pass reader `--audit` shares

**Status:** CLOSED · rev-1 · 2026-10-24 · node d · Tier-2 · base 3c2b69be · streams tooling · order 3

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dGroundRules-66-deviation-71.md](../build/2026-10-24-build-TOOL-dGroundRules-66-deviation-71.md) | deviation | — |
| [2026-10-24-build-TOOL-dGroundRules-66-ledger.md](../build/2026-10-24-build-TOOL-dGroundRules-66-ledger.md) | journal | — |
| [2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md](../build/2026-10-25-build-TOOL-dGroundRules-1-runlog-28554d7f.md) | journal | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 TOOL-dGroundRules-72 TOOL-dGroundRules-73 TOOL-dGroundRules-74 TOOL-dGroundRules-75 TOOL-dGroundRules-76 TOOL-dGroundRules-77 TOOL-dGroundRules-78 TOOL-dGroundRules-79 TOOL-dGroundRules-80 TOOL-dGroundRules-81 TOOL-dGroundRules-82 TOOL-dGroundRules-83 TOOL-dGroundRules-84 TOOL-dGroundRules-85 TOOL-dGroundRules-86 |
| [2026-10-24-prompt-TOOL-dGroundRules-66-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-66-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dGroundRules-66-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dGroundRules-66-spec-brief.md) | research | — |
| [2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md](../reviews/2026-10-25-review-TOOL-dGroundRules-1-71-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-52 TOOL-dGroundRules-55 TOOL-dGroundRules-56 TOOL-dGroundRules-60 TOOL-dGroundRules-61 TOOL-dGroundRules-62 TOOL-dGroundRules-63 TOOL-dGroundRules-64 TOOL-dGroundRules-65 TOOL-dGroundRules-67 TOOL-dGroundRules-68 TOOL-dGroundRules-69 TOOL-dGroundRules-70 TOOL-dGroundRules-71 |

<!-- /gen:spec-records -->

## 1. Goal

`--dispatch` reserves every open key of every unit, terminal or not, so a key that can never close
blocks every later pass that touches its paths. `TOOL-dGroundRules-19` is CLOSED and holds two such
keys, and check 49 refused `TOOL-dGroundRules-7` twice on them. This unit leaves a terminal unit's
keys out of the sibling set through one reader that `--audit` calls too, so the two verbs give one
answer to "which passes are open".

## 2. Scope (IN)

- **S1** — The reader. `read_open_passes <run-state file> [current]` in
  `tools/unattended/unattended.sh` prints the rows `read_pass_declarations` prints for the same
  arguments, keeping only keys that `check_pass_open` calls open and whose unit's spec does not read
  `CLOSED` or `WONTDO` in the loaded `SPEC_PATH` and `SPEC_ST` maps. For each open key it leaves out
  as terminal, it prints one line on stderr:
  `unattended: <anchor> <unit> left out as terminal (<STATUS>), so its declared paths reserve nothing: <paths>`.
  Observed by AC4.
- **S2** — The two callers. `verb_dispatch` builds `sibrows` from `read_open_passes "$rel"`, and
  `print_audit` builds `rows` from `read_open_passes "$rel" current`, called after its
  `load_spec_facts` probe. Neither verb keeps its own openness loop or status skip. Observed by AC1,
  AC2, AC5, AC8.
- **S3** — The note for a terminal unit's own dispatch. When the unit `--dispatch` declares for has a
  spec reading `CLOSED` or `WONTDO`, the verb prints on stderr, before it parks the row:
  `unattended: dispatch — <unit> is <STATUS>, so this declaration reserves nothing against a sibling; set its spec back to INPROGRESS for it to`.
  Observed by AC3.
- **S4** — The comments. The comment above `print_audit`'s status read
  (`tools/unattended/unattended.sh:8480-8488`) no longer calls the conservative answer right for
  `--dispatch`. It says why a terminal unit reserves nothing, names `ROUTED_PATHS` as the extent of
  the scratch guard's refusal, and names the follow-up-pass case §4 states. The sibling-set comment
  in `verb_dispatch` (`:13853-13863`) names `read_open_passes`. The comment in
  `check_commit_message` (`:13500-13501`) says that verb asks `check_pass_open` alone and why.
  Observed by AC6.
- **S5** — The verbs contract. `tools/unattended/VERBS.template.md` and its dogfood copy
  `memory/guides/UNATTENDED-VERBS.md` gain one sentence after "a unit's own rows are never siblings
  of each other": `A pass of a unit whose spec is CLOSED or WONTDO is not a sibling: it reserves nothing, and a later pass for such a unit reserves its paths only once its spec is set back to INPROGRESS.`
  The two files stay byte-identical. Observed by AC7.
- **S6** — The suite arm on the §7 `New arm:` line. NOT OBSERVED by a criterion here: it
  re-observes AC1 to AC3 on a synthetic fixture, and the main loop observes it red, then green, at
  the close.

## 3. Non-goals (OUT)

- `pass_commit`'s first-commit rule in `tools/unattended/lib-unattended.sh:1026`, which is what
  leaves `TOOL-dGroundRules-19`'s two keys open. A key whose first attributed commit writes outside
  its set stays open, and this unit only stops a terminal unit's such key from reserving paths.
- Check 23's grading in `tools/unattended/check-unattended.sh`. It reads every key through
  `read_pass_declarations` (`:4113`) and `pass_commit` (`:4170`) and records an unclosed key's window
  as open (`:4175`). That is a question about history, "did this pass write inside what it declared",
  and not about reservation.
- `--check-commit`'s open-pass rows (`tools/unattended/unattended.sh:13505-13514`). They keep
  `check_pass_open` without the status skip, for the reason §4 "What stays as it is" gives.
- Refusing a `--dispatch` for a terminal unit, or reopening its spec automatically. §4 "What it does
  not see" names this as the follow-up.
- The population `verb_dispatch` loads (`:13606`), which keeps the `_`-prefixed working folders that
  `print_audit`'s load leaves out through `drop_working_specs` (`:8489`).
- Any RUN.md row, and any other spec.

### Edges

- **consumes-from** external — `check_pass_open`, `pass_commit`, `read_pass_declarations` and `load_spec_facts` as they stand at base `3c2b69be`; this unit composes them and changes none
- **hands-off** external — check 23 still grades a terminal unit's never-closing key as an open window, so a later pass's undeclared write overlapping it is counted against `UNDECLARED_WRITE_BUDGET`; changing that is check 23's grading, a non-goal of this unit's brief
- **hands-off** external — a follow-up pass dispatched for a unit whose spec is already terminal reserves nothing; refusing such a dispatch, or requiring the spec reopened first, is a separate mechanism for an ask

## 4. Design

### Evidence

Measured 2026-10-24 at `31aa43f9b`, with `check_pass_open` called over every key
`read_pass_declarations` prints for `memory/builds/dGroundRules/RUN.md`: exactly two keys read open,
`729e5128 TOOL-dGroundRules-19` declaring `tools/policy/guard.py help/policy.md` and
`d88f7ddd TOOL-dGroundRules-19` declaring `.governance/policy.json`. The first commit after each
anchor whose `Pass:` trailer names the unit is `31aa43f9b`, which wrote only
`memory/builds/dGroundRules/build/2026-10-23-build-TOOL-dGroundRules-19-ledger.md`. The commits that
did write those paths, `d88f7ddda` and `1345b7f90`, carry `Pass: none`. So `pass_commit` will never
find a closing commit for either key.

- Condition 3 pairs `.governance/policy.json` with `tools/policy/policy.py` through the policy kit's
  `[[generated]]` row (`tools/policy/kit.toml:27-33`), resolved into `GENERATED_INDEXES` at
  `tools/unattended/unattended.sh:750`. Its loop reads the sibling paths (`:13903-13924`), so a pass
  declaring `tools/policy/policy.py` is refused while `d88f7ddd` reads open.
- Condition 1 (`:13925-13941`) refuses a pass declaring `help/policy.md` while `729e5128` reads open.
- Unit 7's §4 Files touched names both `tools/policy/policy.py` and `help/policy.md`.
- Both refusals were reproduced in a scratch clone of the run branch with `RUN_CLAIMS="off"` and a
  blank `SPEC_TOKENS_CLI`.
  `--dispatch dGroundRules --pass TOOL-dGroundRules-24 --writes tools/policy/policy.py`
  exited 1 with the condition-3 line, and the same with `help/policy.md` exited 1 naming
  `729e5128 TOOL-dGroundRules-19`. With `help/README.md` it was admitted, so the clone reaches the
  row.

`print_audit` already skips a terminal unit (`:8489-8494`). It resolves status through
`load_spec_facts` (`:4719-4742`), which fills `SPEC_PATH` and `SPEC_ST` from the working-tree spec
headers. `verb_dispatch` loads the same maps at `:13606`, and its order gate (`:13677-13678`) and edge
refusal (`:13753-13754`) already read terminal status from them.

### The reader

```
read_open_passes() { # run-state file · [current] -> the open keys of units whose spec is not terminal
  read_pass_declarations "$1" ${2:+"$2"} | while IFS= read -r _r; do
    <cut anchor, unit and declared paths with the expansions verb_dispatch uses today>
    check_pass_open "$_g" "$_u" "$1" "$_decl" || continue
    <status from SPEC_PATH[$_u] then SPEC_ST; on CLOSED or WONTDO print the S1 line on stderr and continue>
    printf '%s\n' "$_r"
  done
}
```

Openness is asked first, so the stderr line names only keys the skip actually releases. A closed key
of a terminal unit prints nothing. The reader reads the maps its caller loaded and loads nothing
itself, because each verb's load is also a probe with its own failure handling. It sits directly
above `check_pass_open` (`:13442`), so the two open-pass functions are read together.

A failed or partial spec read leaves a unit with no status, and a unit with no status is not
terminal. So the failure direction keeps every open key reserved, which is the direction a
disjointness proof wants. `print_audit` keeps its dead-probe refusal (`:8489`, `:8495`), unchanged.

### The two callers

- `verb_dispatch`: `sibrows=$(read_open_passes "$rel")` where the inline loop stood (`:13864-13871`).
  `sibpaths`, the empty-set announcement, condition 3 and condition 1 read `sibrows` as before.
- `print_audit`: `rows=$(read_open_passes "$rel" current | awk …)`, the awk unchanged (`:8477-8479`),
  moved below the `load_spec_facts` probe. The loop loses its status skip and its `check_pass_open`
  call (`:8492-8494`), and its `sp` and `st` locals with them.
- S3's note sits beside the order gate, which already holds `_d_spec`, and reads
  `SPEC_ST[$_d_spec]`.

### Why a terminal unit reserves nothing

A unit's spec goes terminal in its own pass commit under this harness (`:13619-13620`), and its work
has landed by then. The scratch guard admits a Tier-2 unit's writes only at INPROGRESS
(`tools/hooks/scratch-guard.js:796`), reading the spec from the working tree (`:884-896`). The refusal
covers `ROUTED_PATHS` only (`.memory-tree.conf:9`: `tools/`, `skills/`, the charter template and
`WIRE-INTO-PROJECT.md`). A later pass for the unit therefore needs its spec set back to INPROGRESS,
and that brings its keys back into the set (AC2).

### What stays as it is

- **`--check-commit`** asks `check_pass_open` alone (`:13509`). A pass commit flips its own spec to
  CLOSED in the commit being made. A status skip there would read that commit's pass as closed, and
  `pass_commit` would not name HEAD either. The verb would then refuse every pass commit as having "no
  open dispatched pass" (`:13543-13545`). That verb answers "which declaration grades this commit",
  not "which paths are reserved".
- **Check 23** grades history. A terminal unit's unclosed window there counts more writes as
  overlapping, not fewer. The direction is stricter, and the Edges hand it off.
- **`check_pass_open`** stays the one openness predicate. The status skip sits in the reader above
  it, so `--check-commit` keeps its answer.

### What it does not see

- **A follow-up pass for a terminal unit.** This run dispatched `729e5128` and `d88f7ddd` for
  `TOOL-dGroundRules-19` after its spec read CLOSED, and they wrote `help/policy.md` and
  `.governance/policy.json`, both outside `ROUTED_PATHS`. After this unit such a pass reserves nothing
  from the moment it is declared. S3's note and S5's sentence make that visible, and they name the
  remedy: set the spec back to INPROGRESS first.
- **The window between a spec's flip and its pass commit.** The status is read from the working
  tree, as `print_audit`, the order gate and the scratch guard read it. So a unit whose builder has
  flipped its spec to CLOSED but not yet committed stops reserving its paths before its commit. From
  that flip the scratch guard refuses the unit's further routed writes. Its writes still uncommitted
  are not protected from a sibling declared in that window.
- **A spec under a `_`-prefixed folder** that alone defines a unit id counts for `--dispatch` and not
  for `--audit`, as the two loads differ today (§3).

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `read_open_passes` | sh.function | `tools/unattended/unattended.sh` |
| `left out as terminal` | stderr line, S1 | `read_open_passes` |
| `reserves nothing against a sibling` | stderr line, S3 | `verb_dispatch` |

`read_open_passes` leads with `read`: `lexicon.py --suggest read_open_passes --as sh.function`
answered OK on 2026-10-24.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **The status test inside `check_pass_open`.** `--check-commit` would inherit it and refuse every
  pass commit that closes its own spec (§4 "What stays as it is").
- **Status read at HEAD rather than the working tree.** It would close the flip-to-commit window, but
  `verb_dispatch` would then answer "is this unit terminal" two ways in one call. Its order gate and
  edge refusal read the working tree, and so do `print_audit` and the scratch guard. That is the
  two-answers class, and the brief asks for the status read the way `--audit` reads it.
- **Leave out only a terminal unit's keys other than its current one.** It keeps the newest
  follow-up reserved. But in `current` mode every key is current, so `--audit` would grade a CLOSED
  unit with an open current key as STALLED again (the defect `:8486-8488` records), unless the two
  modes used two predicates.
- **Close `TOOL-dGroundRules-19`'s keys with a record commit.** `pass_commit` takes the first
  attributed commit, so no later commit closes them. Changing that rule is a non-goal, and the class
  recurs for any terminal unit whose first attributed commit writes outside a key's set.

## 5. Production-readiness checklist

- security — this narrows check 49's refusal set: an open key of a terminal unit no longer blocks a
  sibling. No new write path. The scratch guard still refuses a terminal unit's writes under
  `ROUTED_PATHS`, and the unguarded remainder is §4 "What it does not see", made visible by S1 and S3.
- perf / scale — `--dispatch` makes the same `check_pass_open` calls as today. `--audit` now also
  asks it of terminal units' current keys, one `pass_commit` walk each per keepalive tick, where it
  skipped them before.
- error / empty / loading states — a failed or partial spec read makes no unit terminal, so every
  open key stays reserved for `--dispatch`. `--audit`'s dead-probe refusal is unchanged. An empty
  sibling set still prints the existing "proof over an empty set" line.
- observability — one stderr line per released key (S1), and one when a terminal unit is dispatched
  (S3).
- risks — a follow-up pass for a closed unit reserves nothing, and an uncommitted flip releases a
  pass early. Both are stated in the reader's comment and the verbs contract.
- testing — AC1 to AC8, and the suite arm on the §7 `New arm:` line.
- migration — none. No row format changes, and existing records' terminal keys are released on the
  first `--dispatch` after the change.
- user docs — the verbs contract and its dogfood copy (S5). No page under `help/` covers the
  unattended verbs: it holds `README.md`, `measure-legs.md`, `policy.md` and `roles.md`.

## 6. Acceptance criteria

The criteria AC4 to AC7 run from the repository root of the pass's worktree. AC1 to AC3 and AC8
each run in a fresh scratch clone `D` of the run branch, made as below. `RUN_CLAIMS="off"` keeps every claim read
and write inside the clone. A blank `SPEC_TOKENS_CLI` keeps an unrelated checker verdict out of the
refusal under test, and the driver announces that skip. BEFORE is the driver at this spec's base, and
AFTER is the driver this pass built: run one of the block's last two lines, never both. Each driver
call runs from inside `D` with `2>&1`.

```
D="$TEMP/d66"; rm -rf "$D"
git -c core.longpaths=true clone -q --branch branch/unattended-dgroundrules-e47ae1 . "$D"
printf '\nRUN_CLAIMS="off"\nSPEC_TOKENS_CLI=""\n' >> "$D/.unattended.conf"
git -C "$D" show 3c2b69be:tools/unattended/unattended.sh > "$D/tools/unattended/unattended.sh"   # BEFORE
cp tools/unattended/unattended.sh "$D/tools/unattended/unattended.sh"                              # AFTER
```

Unit 7's write set, its §4 Files touched, for AC8:

```
bash tools/unattended/unattended.sh --dispatch dGroundRules --pass TOOL-dGroundRules-7 --writes tools/policy/policy.py --writes tools/policy/legacy-homes.txt --writes tools/policy/check_policy.py --writes tools/policy/README.md --writes tools/policy/kit.toml --writes help/policy.md 2>&1
```

- **AC1** — When `bash tools/unattended/unattended.sh --dispatch dGroundRules --pass TOOL-dGroundRules-66 --writes tools/policy/policy.py 2>&1`
  runs in `D` with BEFORE, it exits 1 printing `.governance/policy.json with tools/policy/policy.py`.
  In a fresh `D` with AFTER, it exits 0 printing `dispatch declared` and
  `d88f7ddd TOOL-dGroundRules-19 left out as terminal (CLOSED)`.
  Red when: AFTER still refuses on a CLOSED unit's never-closing key on the mirror, or admits it
  without the left-out line.
  fixture: the clone holds `TOOL-dGroundRules-19`'s two open keys while no commit closes them, measured
  at `31aa43f9b`.
- **AC2** — When `sed -i 's/^\*\*Status:\*\* CLOSED/**Status:** INPROGRESS/' memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-19.md`
  runs in a fresh `D` with AFTER, AC1's command exits 1 printing
  `.governance/policy.json with tools/policy/policy.py`. In another fresh `D`, with `WONTDO` in place
  of `INPROGRESS`, it exits 0 printing `left out as terminal (WONTDO)`.
  Red when: the skip keys on anything but the spec's status token, so a reopened unit stays released or
  a WONTDO unit stays reserved.
- **AC3** — When `bash tools/unattended/unattended.sh --dispatch dGroundRules --pass TOOL-dGroundRules-24 --writes help/README.md 2>&1`
  runs in a fresh `D` with AFTER, it exits 0 printing `reserves nothing against a sibling`. With BEFORE
  it exits 0 and prints no such line.
  Red when: a dispatch for a CLOSED unit is declared with no word that it reserves nothing.
- **AC4** — When `bash -c 'source tools/unattended/unattended.sh >/dev/null 2>&1; load_spec_facts $(git ls-files "memory/builds/dGroundRules/spec/*.md"); read_open_passes memory/builds/dGroundRules/RUN.md 2>&1'`
  runs, it prints no row carrying `TOOL-dGroundRules-19 · reason`, and exactly two
  `left out as terminal (CLOSED)` lines, naming `729e5128` and `d88f7ddd`. With `current` added after
  the run-state file, it prints no line naming `TOOL-dGroundRules-19`.
  Red when: the reader returns a terminal unit's open key as a row, or releases one silently.
  figure: two keys, PINNED, measured 2026-10-24 at `31aa43f9b` by the inline loop's own predicate.
  The count holds while no commit closes either key.
- **AC5** — When `bash -c 'source tools/unattended/unattended.sh >/dev/null 2>&1; for f in verb_dispatch print_audit check_commit_message; do echo "$f $(type $f | grep -c read_open_passes)"; done'`
  runs, it prints `verb_dispatch 1`, `print_audit 1` and `check_commit_message 0`.
  Red when: either verb keeps its own openness loop, or `--check-commit` inherits the status skip.
- **AC6** — When `sed -n '/^print_audit()/,/^}/p' tools/unattended/unattended.sh | grep -c "right answer for .--dispatch"`
  runs, it prints `0`. The same range piped to `grep -c ROUTED_PATHS` prints at least `1`, and
  `sed -n '/^check_commit_message()/,/^}/p' tools/unattended/unattended.sh | grep -c "check_pass_open alone"`
  prints at least `1`.
  Red when: the comment still calls the conservative answer right for `--dispatch`, or
  `--check-commit`'s difference is left unstated.
- **AC7** — When `grep -c "whose spec is CLOSED or WONTDO is not a sibling" tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md`
  runs, it prints `1` for each file, and
  `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` exits 0.
  Red when: the contract still says every open pass is a sibling, or the dogfood copy drifts from the
  template.
- **AC8** — When unit 7's command above runs in `D` made after this unit's pass commit, it exits 1
  with BEFORE, printing `.governance/policy.json with tools/policy/policy.py`, and exits 0 with AFTER,
  printing `dispatch declared` on a line naming `TOOL-dGroundRules-7 · tools/policy/policy.py`.
  Red when: this build's own state still refuses unit 7 on `TOOL-dGroundRules-19`'s keys.
  fixture: a clone made after the pass commit. Before that commit this unit's own spec sits at order 3
  and is not terminal, so the order gate holds unit 7 back.
  The main loop's own dispatch of unit 7 is the same command on the live run.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `memory hygiene` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · a two-unit fixture whose first unit declares the index of a `GENERATED_INDEXES` pair and closes its spec in a commit naming no unit, so its key never closes, then the second unit declares the generator: red against the base driver, which refuses it; the first spec set back to INPROGRESS, refused; the closed unit dispatched, printing its reserves-nothing line · FLOOR_ASSERTIONS and the floor of the region holding the arm, by the arm's count

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft from the build run's rescope add row for this unit and its spec
  brief, `memory/builds/dGroundRules/prompts/2026-10-24-prompt-TOOL-dGroundRules-66-spec-brief.md`,
  grounded at base `3c2b69be`, where `tools/unattended/` equals the run branch's tip `31aa43f9b`.

## 10. Reuse audit

The seams extended are the driver's own open-pass pair in `tools/unattended/unattended.sh`:
`check_pass_open` (`:13442`), hoisted by `TOOL-aProbedUnit-3` so `--dispatch` and `--audit` ask one
function, and `--audit`'s terminal skip (`:8492-8493`). Both are composed in one reader rather than
copied, and `read_pass_declarations` (`tools/unattended/lib-unattended.sh:1116`) stays the one
population (`TOOL-aGraftedHelix-39`). The probe
`python tools/codebase-map/reuse_lookup.py "skip a terminal unit's dispatched pass keys when deriving the open sibling set"`
ranked name stems only (`key`, `keys`, `units`, `skip`, `opened`). None of them derives an open-pass
set, so no other seam fits.
The recall probe returned `TOOL-aProbedUnit-3`, `TOOL-aGraftedHelix-39` and `TOOL-cMendedVintage-10`,
whose rules this unit keeps. It also returned the asks `TOOL-dCarriedReceipt-3` (a multi-unit pass
whose declarations never close) and `TOOL-aMendedFleet-107` (condition 3 under sequential dispatch).
Both are related, and this unit closes neither.

Recall terms used:
`python tools/memory-recall/query.py "dispatch sibling set leaves out a closed unit's open pass keys" --terms "dispatch sibling open pass terminal CLOSED WONTDO check_pass_open pass_commit audit disjointness condition generator"`
