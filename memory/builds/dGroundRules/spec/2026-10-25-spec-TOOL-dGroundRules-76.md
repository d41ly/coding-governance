# TOOL-dGroundRules-76 — `policy.py lists --check` grades the legacy-homes list by the gate arm's rule

**Status:** DEFERRED · rev-1 · 2026-10-25 · node d · Tier-1 · base fce5603f · streams tooling · order 26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-prompt-TOOL-dGroundRules-76-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-76-1-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-76-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-76-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`policy.py lists --check` exits 1 in every adopter install, and the remedy it prints, `lists --write`,
cannot clear it. That is finding M2 (id 3) of the closing diff review, round 1. The verb grades the
legacy-homes list even where the list is absent, while the gate's `arm_legacy_homes` grades nothing
there. This unit gives both readers one predicate, the arm's rule, so `lists --check` and
`lists --write` grade the list only where the arm does, and a fixture case pins the install shape.

## 2. Scope (IN)

- **S1** — The one predicate. `tools/policy/policy.py` gains `check_legacy_graded(repo, kit)`, as
  §4 "The predicate" gives it. `derive_census_tree`, `check_receipt_prefix`, `RECEIPT_REL` and
  `REGISTRY_REL` move, bodies unchanged, from `tools/policy/check_policy.py` into
  `tools/policy/policy.py`, because the predicate needs the census tree and `policy.py` may not
  import `check_policy.py` (§4 "Why the derivation moves"). In `tools/policy/check_policy.py`, one
  line binds `RECEIPT_REL` and `REGISTRY_REL` to the core module's values, and the two other callers
  of `derive_census_tree`, in `arm_cap_census` and in the `census-window-edge` case, spell it
  `policy.derive_census_tree`. Observed by AC3 and AC5.
- **S2** — The two readers ask it. In `tools/policy/policy.py`, `cmd_lists` sets `held` from
  `check_legacy_graded(top, KIT)` inside its existing `try`, for both verbs. `--check` prints
  `policy lists: legacy-homes.txt · not graded · <LEGACY_WITHHELD>` where `held` is false, in place of
  the row-count line. In `tools/policy/check_policy.py`, `arm_legacy_homes` asks the same predicate
  in place of its own tree test and file test, and keeps its two answers. Observed by AC1, AC2, AC4
  and AC6.
- **S3** — The install-shape case. In `tools/policy/check_policy.py`, `LEGACY_CASES` gains
  `withheld`, and `run_legacy_homes` gains its branch, as §4 "The case" gives it. Its docstring
  names the case. Observed by AC7.
- **S4** — The docs. `tools/policy/README.md` (the `lists --check` and `lists --write` bullets, the
  legacy-homes paragraph that names `arm_legacy_homes`, the module row, and the `legacy-homes` case
  paragraph) and `help/policy.md` (the paragraph under "The policy that still lives elsewhere" that
  names the not-graded line) say that both verbs grade the list only where the arm does, as §4 "The
  docs" gives it. Observed by AC8.

## 3. Non-goals (OUT)

- The broader left-shift rule the report names, an install-shape fixture for every documented kit
  command. It is a follow-up the main loop files as an ask (§7).
- What `check_legacy_homes` reports when it does grade, the summary list, and `derive_census_tree`'s
  own answers.
- The kit version. `govkit.py epoch` prints `owed at the lander` for a moved kit, and the lander
  mints the bump, so a branch owes none (`cmd_epoch`'s docstring, `tools/govkit/govkit.py`).
- The other findings of the report, any other spec, and the inherited reds the close recorded.

### Edges

none

This unit repairs the read rule `TOOL-dGroundRules-17` (CLOSED) left in `cmd_lists`, and adopts in
the verb the adopter-tree rule `TOOL-dGroundRules-25` S11 and `TOOL-dGroundRules-32` S11 gave the
arm. It changes nothing in what either unit asserts.

## 4. Design

### Evidence

All line numbers are at `fce5603f`. Units 73 and 76 both touch `tools/policy/policy.py`, and units
75 and 77 both touch `tools/policy/check_policy.py`, so this spec names each site by its symbol.

`cmd_lists` (policy.py, line 1354) sets `held = argv == ["--check"] or (KIT / LEGACY_LIST).is_file()`
at line 1365. So `--check` always calls `check_legacy_homes`. With no list, `committed` is `[]`
(line 1189), and every derived row is reported as `stale list at <row>, re-run lists --write`
(line 1201). `--write` reads `held` as false where the file is absent and prints `not written ·
LEGACY_WITHHELD` (lines 1397-1401). `kit.toml` withholds `legacy-homes.txt` from every install with a
`project-owned` rule. `arm_legacy_homes` (check_policy.py, lines 385-408) answers not graded where
`derive_census_tree` answers `adopter` or `invalid`, or where the list is absent (line 399).

The premise holds at `fce5603f`. A probe was run with §5's `f76.sh`: a repository holding a copy of
the kit with no list, an install receipt and one `.unattended.conf` key. `lists --check` exited 1
with one `stale list` report, `lists --write` exited 0 printing `not written`, and a second
`--check` exited 1 again. With an adopter-written list beside the receipt, `--check` exited 1 and
`--write` rewrote the adopter's file.

### The predicate

```
def check_legacy_graded(repo, kit):
    """True where `kit`'s legacy list is graded over the tree at `repo`: the list is present and
    `derive_census_tree` answers neither `adopter` nor `invalid` (TOOL-dGroundRules-76). The one rule
    `cmd_lists` and the gate's `arm_legacy_homes` both ask. A Refusal from the derivation is the
    caller's to report."""
    tree, _held = derive_census_tree(repo)
    return tree not in ("adopter", "invalid") and (Path(kit) / LEGACY_LIST).is_file()
```

It sits in the legacy-homes section of `policy.py`, after `LEGACY_WITHHELD`. The moved block sits
directly above it. `RECEIPT_REL` is spelled `f"{posixpath.dirname(POLICY_REL)}/install.json"`, the
same `.governance/install.json`, and `import posixpath` joins the module's imports, which
`derive_census_tree` needs. In `derive_census_tree`, each `policy.Refusal` becomes `Refusal`, and
nothing else changes, docstring included. The derivation runs before the file test, so a Refusal
still fires with no list present, as the arm does today. The lexicon answers `OK` for
`check_legacy_graded` on `py.function`.

### Why the derivation moves

`check_policy.py` imports `policy` at its top. Run as `python policy.py`, the module is `__main__`,
so a lazy `import check_policy` in `cmd_lists` would load a second copy of `policy.py` under the name
`policy`. A Refusal raised there is that copy's class, and `cmd_lists`'s `except Refusal` would not
catch it. The core module owning the derivation keeps one class and one rule ([core]). Every reader
of the four moved names is in `check_policy.py`: `git grep` over the tree outside the memory root
finds no other.

### cmd_lists

The comment above the `held` line is respelled to say that both verbs ask the arm's rule. The `held`
line becomes, inside the `try`, after the `if not top` refusal:

```
        held = check_legacy_graded(top, KIT)  # the arm's rule (TOOL-dGroundRules-76)
        if held:
            reports, notes, rows, new = check_legacy_homes(top, KIT, compare)
```

A refused derivation takes the existing `except Refusal` path, exit 2. The `--check` row-count line
becomes:

```
        print(f"policy lists: {LEGACY_LIST} · " + (f"{len(rows)} row(s) derived from the legacy homes"
                                                   if held else f"not graded · {LEGACY_WITHHELD}"))
```

`--write` keeps its `if held` branch, so an adopter's own list is no longer rewritten. On gov's tree
`derive_census_tree` answers `source` and the list is present, so both verbs grade as before. A list
deleted on gov's tree now reads as not graded in the verb too. The `legacy-homes-present` case
(`run_legacy_present`) is what reds that deletion, as its docstring says, and it is unchanged. No
tracked file reads the verb's output lines: `git grep` for `derived from the legacy homes` and
`policy lists: ` outside the memory root finds only `policy.py` and the arm's own population string.

### arm_legacy_homes

```
    try:
        graded = policy.check_legacy_graded(repo, kit)
    except policy.Refusal as exc:
        return 0, "the tree under test did not derive", [(exc.path, exc.why)]
    if not graded:
        return None, policy.LEGACY_WITHHELD, []
```

This takes the place of the arm's `derive_census_tree` call and its line-399 test. The rest of the
arm, its docstring included, is unchanged.

### The case

In `run_legacy_homes`, before the closing `else`:

```
            elif case == "withheld":
                listed.unlink()  # the install shape: kit.toml withholds the list (TOOL-dGroundRules-17)
                check, out = check_legacy_lists(case, kit, "--check", 0, [])
                told = f"policy lists: {policy.LEGACY_LIST} · not graded · {policy.LEGACY_WITHHELD}" in out.split("\n")
                checks.append(check[:2] + (check[2] and told, check[3] + f" · {'announced not graded' if told else 'NO not-graded line'}"))
```

The fixture's tree holds no receipt and no registry, so `derive_census_tree` answers `unadopted`, and
the file test alone decides. Against `fce5603f`'s `cmd_lists` the case prints `WRONG` with exit 1 and
one `stale list` report per derived row.

What the case does not check: an adopter tree holding a list, and a copy built from `kit.toml`'s
real install set, which is the follow-up in §7. AC2 covers the first, and so does the
`adopter-fresh-target` case (`run_fresh_target`), whose adopter-written list reaches the shared
predicate through the arm.

### The docs

`tools/policy/README.md`: the `lists --check` bullet says it grades `legacy-homes.txt` where
`check_legacy_graded` answers true, and prints `policy lists: legacy-homes.txt · not graded · <why>`
otherwise. The `lists --write` bullet says it writes that list under the same rule. The legacy-homes
paragraph that names `arm_legacy_homes` says both verbs and the arm ask one predicate. The module
row names `check_legacy_graded` and `derive_census_tree`. The `legacy-homes` case paragraph names
`withheld`, and "over seven repositories" becomes "over one repository per name in `LEGACY_CASES`",
so no count is typed beside the tuple. `help/policy.md`: the sentence on the not-graded line adds
that `lists --check` there prints `policy lists: legacy-homes.txt · not graded`, and grades the
summary list alone.

### Alternatives rejected

- The verb's own copy of the arm's rule. That leaves two rules for one question, the class this
  finding is.
- A lazy `import check_policy` in `cmd_lists`. It loads `policy.py` twice when run as a script, and
  the Refusal class splits (§4 "Why the derivation moves").

### Rollout

The builder sets this spec's status from DEFERRED to INPROGRESS before its first write. Scratch-guard
admits writes under `ROUTED_PATHS` for a Tier-1 unit only at INPROGRESS, or at SPECCED once graded.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/check_policy.py`
- `tools/policy/README.md`
- `help/policy.md`

## 5. Acceptance criteria

All commands run from the repository root of the pass's worktree. `f76.sh` builds an install-shaped
repository in the directory it is given: a copy of the kit's code with no legacy list, an install
receipt, and one `.unattended.conf` key, committed. With `adopter-list` as its second argument it
also writes a list of the adopter's own. It runs `lists --check` and then `lists --write` in the
copy, and prints the check's exit code, its `  legacy homes: ` report count, its not-graded line
count, the write's exit code, and whether the list bytes stayed the same:

```
cat > "$TEMP/f76.sh" <<'EOF'
S="$PWD/tools/policy"; R="$1/r"; rm -rf "$1"; mkdir -p "$R/tools/policy" "$R/.governance"
for f in policy.py budgets.py caps.toml catalogue.toml unsummarised-keys.txt; do cp "$S/$f" "$R/tools/policy/"; done
printf 'REVIEW_ROUNDS="3"\n' > "$R/.unattended.conf"
printf '{"kits": ["policy"], "prefix": "tools/", "files": []}\n' > "$R/.governance/install.json"
[ "$2" != adopter-list ] || printf '# a list the adopter wrote\n' > "$R/tools/policy/legacy-homes.txt"
git -C "$R" init -q; git -C "$R" add -A; git -C "$R" -c user.name=f -c user.email=f@f commit -qm f
before=$(cat "$R/tools/policy/legacy-homes.txt" 2>/dev/null)
out=$(cd "$R/tools/policy" && python policy.py lists --check 2>&1); rc=$?
(cd "$R/tools/policy" && python policy.py lists --write >/dev/null 2>&1); wrc=$?
after=$(cat "$R/tools/policy/legacy-homes.txt" 2>/dev/null)
echo "$rc $(grep -c '^  legacy homes: ' <<<"$out") $(grep -c '^policy lists: legacy-homes.txt · not graded · ' <<<"$out") $wrc $([ "$before" = "$after" ] && echo same || echo changed)"
EOF
```

The third and fourth criteria read the repository AC1 leaves at `$TEMP/a76/r`, so AC1 runs first. The whole
`policy fixtures` leg is a suite this pass may not run. The main loop runs it at the close.

- **AC1** — When `bash "$TEMP/f76.sh" "$TEMP/a76" install` runs, it prints `0 0 1 0 same`.
  At `fce5603f` it printed `1 1 0 0 same`.
  Red when: `cmd_lists` keeps `argv == ["--check"]` in its `held` rule, which prints `1 1 0 0 same`.
- **AC2** — When `bash "$TEMP/f76.sh" "$TEMP/b76" adopter-list` runs, it prints `0 0 1 0 same`.
  At `fce5603f` it printed `1 1 0 0 changed`.
  Red when: `check_legacy_graded` tests only the file, without the tree, which prints
  `1 1 0 0 changed`.
- **AC3** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import policy; print(policy.check_legacy_graded('.', 'tools/policy'), policy.check_legacy_graded(sys.argv[1], 'tools/policy'))" "$TEMP/a76/r"` runs, it prints `True False`.
  Red when: the predicate's tree test is inverted, which prints `False True`, or it tests only the
  file, which prints `True True`.
- **AC4** — When `python -c "import sys; sys.path.insert(0, 'tools/policy'); import check_policy as c; print(*(c.arm_legacy_homes(d, c.KIT)[0] is None for d in ('.', sys.argv[1])))" "$TEMP/a76/r"` runs, it prints `False True`.
  At `fce5603f` it printed `False True`, so the arm's answers are unchanged.
  Red when: `check_legacy_graded` tests only the file, which prints `False False`.
- **AC5** — When `grep -c "^def derive_census_tree" tools/policy/check_policy.py tools/policy/policy.py` runs, it prints `tools/policy/check_policy.py:0` and `tools/policy/policy.py:1`.
  At `fce5603f` it printed `1` and `0`.
  Red when: a copy of the derivation stays in `tools/policy/check_policy.py`.
- **AC6** — When `grep -c "policy.check_legacy_graded(" tools/policy/check_policy.py` runs, it prints `1`.
  At `fce5603f` it printed `0`.
  Red when: `arm_legacy_homes` keeps its own tree test and file test, so the verb and the arm hold
  two rules again.
- **AC7** — When `python tools/policy/check_policy.py --fixture legacy-homes` runs, it prints `policy-fixture: legacy-homes · case withheld: green · lists --check · exit 0 · 0 report(s) · announced not graded`, and no line of its output holds `WRONG`.
  Red when: the case runs against `fce5603f`'s `cmd_lists`, whose `held` rule grades the absent
  list. The case line then holds `WRONG` with `exit 1` and one `stale list` report per derived row.
- **AC8** — When `grep -cF "policy lists: legacy-homes.txt · not graded" tools/policy/README.md help/policy.md` runs, it prints a count of at least `1` for each file.
  At `fce5603f` it printed `0` for each.
  Red when: either page still says only that `lists --write` does not create the list, so a reader
  of the docs expects `lists --check` to grade an install.

## 6. Gates

`policy fixtures` · `policy check` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `memory hygiene`

Run through `derive_guarded_legs` at `fce5603f`, `python tools/check-spec-tokens.py --legs-for`
names one non-broad guarded leg for each touched file: `policy fixtures`, through `tools/policy/`
for the three kit files and through `help/policy.md` for the help page. Every other leg it prints
trips only on the broad `tools/`. The legs named beside it carry no guard and read what this unit
changes. `policy check` runs `arm_legacy_homes` over gov's tree. `lexicon naming predicates` grades
the new name. `encoding posture` reads the moved text IO in `policy.py`. `codebase-map coverage +
freshness` records which file defines each symbol. `kit epoch` reads the policy kit's shipped bytes,
and prints `owed at the lander` for this move.

New arm: tools/policy/check_policy.py --fixture legacy-homes · covers AC7 · the case withheld against fce5603f's cmd_lists, whose held rule grades the absent list, prints WRONG with exit 1 and the stale-list reports · none

No floor or pinned count moves. The `policy fixtures` row in `tools/run-gates/selftest-budgets.txt`
counts outcome cases, and `legacy-homes` stays one case with one more repository inside it.

## 7. Open questions

none

Follow-up, not a fork, for the main loop to file as an ask: the report's left-shift rule that every
documented kit command gets an install-shape fixture, run against a copy built from `kit.toml`'s
install set so a withheld file is really absent. It reaches every kit and its install sets, which is
more than one arm of this mechanism.

## 8. Revision log

- rev-1 · 2026-10-25 · initial draft from the closing diff review's finding M2 (id 3) and this unit's
  spec brief, grounded at `fce5603f`. The premise was checked by a scratch install-shaped repository,
  not by running a suite. Takes the skeptic's SOUND fix and its "better" form: one shared predicate,
  which moves `derive_census_tree` into the core module because `policy.py` run as a script cannot
  import `check_policy.py` without splitting the Refusal class. `--write` asks the same predicate, so
  an adopter's own list is not rewritten. The report's left-shift case is in scope as S3, and its
  broader rule is §7's follow-up. The brief, untracked when this draft was written:

```
memory/builds/dGroundRules/prompts/2026-10-25-prompt-TOOL-dGroundRules-76-spec-brief.md
```

## 9. Reuse audit

The seam is the arm's own rule, `arm_legacy_homes` with `derive_census_tree` in
`tools/policy/check_policy.py`, lifted into `tools/policy/policy.py` as one predicate that both
readers call, rather than a second copy written into `cmd_lists`. The case reuses the `legacy-homes`
outcome case's builder `build_legacy_repo` and its judge `check_legacy_lists`, adding one name to
`LEGACY_CASES`. `python tools/codebase-map/reuse_lookup.py "decide whether the legacy homes list is graded in an adopter tree or when absent"`
ranked only name stems (`tree`, `absent`, `adopt`, `require_adopted_root`), none of which grades the
legacy list. The recall probe returned `TOOL-dGroundRules-17`, which withheld the list and left the
verb's rule, `TOOL-dGroundRules-7`, which built the list, and the review finding itself.

Recall terms used: `python tools/memory-recall/query.py "lists --check legacy homes list withheld adopter install not graded" --terms "LEGACY_WITHHELD arm_legacy_homes derive_census_tree cmd_lists held"`
