# TOOL-dGroundRules-43 — the round-1 audit of units 33 and 34, its minors: fifteen findings closed in the code those units leave, one scope item each

**Status:** DEFERRED · rev-5 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 14 · advances TOOL-dGroundRules-12

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-43-deviation-31.md](../build/2026-10-23-build-TOOL-dGroundRules-43-deviation-31.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-43-deviation-65.md](../build/2026-10-23-build-TOOL-dGroundRules-43-deviation-65.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dGroundRules-43-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-43-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with 23 confirmed findings. Its eight HIGH ids are promoted one unit each,
`TOOL-dGroundRules-35` to `TOOL-dGroundRules-42`. BUILD-METHOD M4 promotes the other fifteen,
eleven MEDIUM and four LOW, batched into one unit, and this is that unit. They land on units 33 and
34, and on 30 through id 6. Four are built already by the units they land on or a sibling: ids 4,
11, 27 and 12 (S5, S8, S11, S12), each recorded with the observation that confirms it. Of the code
items left, the trace item (id 20) and the snapshot and census items (ids 26, 15 and 16) all write
`tools/policy/check_policy.py`, so they do not split into two disjoint write sets by M6's clauses,
and one unit carries them all. It repairs no unit in particular and builds at order 14, after units
39 to 42 at order 13, beside units 44 to 50 at the same step.

Ids 3 and 8, item M1, are the medium half of H3's overlap and census facets; the review grades them
medium and says they are one defect with H3. Each takes its own scope item, the re-observation of
the criteria it names at this unit's close, made through the literals units 39 and 40 spell whole.
Id 15 is taken at LOW, the grade the skeptic gave it.

| Finding id | Severity | Review item | Unit it lands on | Scope item | Criterion |
|---|---|---|---|---|---|
| 3 | MEDIUM | M1 | 34 | S1 | AC1 |
| 8 | MEDIUM | M1 | 34 | S2 | AC2 |
| 5 | MEDIUM | M2 | 34, 32 | S3 | AC3 |
| 10 | MEDIUM | M2 | 34 | S4 | AC4 |
| 4 | MEDIUM | M3 | 34 | S5 | AC5 |
| 9 | MEDIUM | M3 | 34 | S6 | AC6 |
| 6 | MEDIUM | M4 | 34, 30 | S7 | AC7 |
| 11 | MEDIUM | M5 | 34 | S8 | AC8 |
| 20 | MEDIUM | M6 | 33 | S9 | AC9 |
| 26 | MEDIUM | M7 | 34 | S10 | AC10 |
| 27 | MEDIUM | M8 | 33 | S11 | AC11 |
| 12 | LOW | L1 | 33 | S12 | AC12 |
| 13 | LOW | L2 | 34 | S13 | AC13 |
| 15 | LOW | L3 | 34 | S14 | AC14 |
| 16 | LOW | L4 | 34 | S15 | AC15 |

Each item's fix is the one the review's skeptic judged sound; for id 15 it is the skeptic's
corrected fix, held to the stricter rule `TOOL-dGroundRules-34` S21 chose.

## 2. Scope (IN)

- **S1** — Finding 3. `TOOL-dGroundRules-34` AC15 and AC16 are observed at this unit's close with
  their pairs whole, through `PAIRS_PY` and `PAIRS_SH` as `TOOL-dGroundRules-40` §6 spells them.
  Observed by AC1.
- **S2** — Finding 8. `TOOL-dGroundRules-34` AC11 and AC12 are observed at this unit's close with
  their paths whole, through `TREE_AMBIG` and `census-window-edge` as `TOOL-dGroundRules-39`
  spells them. Observed by AC2.
- **S3** — Finding 5. The build-order region's marker lines at each revision this build's specs
  cite are stated in §4 Evidence, PINNED, so `TOOL-dGroundRules-34` S32's citation is a checked
  piece of evidence: lines 165 and 179 of the build README at `f4d31452a`. Observed by AC3.
- **S4** — Finding 10. That `ORDER_ROWS` selects the region by its markers is observed by a break
  that can red it: the closing marker moved up in a scratch copy makes its count fall below the
  distinct `order` values. Observed by AC4.
- **S5** — Finding 4. Built in `TOOL-dGroundRules-34` AC26, whose right-hand count is `ORDERS` in
  §6 as spelled there: it reads the status lines only and requires a digit, so the criterion's own
  text never counts. S5 owes no code. Observed by AC5, whose staged half is AC6.
- **S6** — Finding 9. AC26 is paired with its staged break: one unit's `order` changed in a scratch
  copy, with the README not re-rendered, makes the two counts differ. Observed by AC6.
- **S7** — Finding 6. Built: `TOOL-dGroundRules-30` took the version-staging arm out of
  `tools/workflows/check-protocol-parity.test.sh` at `93e4b4d31`, as `TOOL-dGroundRules-34` S5
  records, so `TOOL-dGroundRules-30` AC3's zero count of `KIT_AGENT_CAP_VERSION` holds on the built
  tree. What this unit owes is that `TOOL-dGroundRules-34` AC5's figure can fail: `OLD_ARM` stages
  that file as it stood at `93e4b4d31^`, which still holds the arm, into a scratch copy. Observed by
  AC7.
- **S8** — Finding 11. Built by `TOOL-dGroundRules-34` at `75b1ffe59`: `run_fresh_target` compares
  the receipt's `gov_source` to the snapshot root as `Path(said).resolve() != s.resolve()`, the
  normalisation that unit's S9 applies to `SNAPSHOT_ROOTS`. S8 owes no code; its no-`WRONG` half is
  green before this unit, so AC8 observes its staged half. Observed by AC8.
- **S9** — Finding 20. `add_source_read` keeps an `open` event only when `args[1]` is a string
  holding none of `w`, `a`, `x` or `+`, or, when `args[1]` is None, when the flags in `args[2]`
  carry none of `os.O_WRONLY`, `os.O_RDWR` or `os.O_CREAT`. `check_guard_trace` joins only the kept
  paths that exist under `derive_source_top()` when it runs, and prints the number it left out as
  `policy-fixture: guard-trace · <n> absent read(s) set aside`. Observed by AC9.
- **S10** — Finding 26. `build_source_snapshot` reads
  `git -C <source> config --type=path --get core.excludesFile`, which answers from every scope the
  source sees, its worktree configuration included, and when it is set passes it as
  `-c core.excludesFile=<that>` to the snapshot's `add -A`. Observed by AC10.
- **S11** — Finding 27. Built by `TOOL-dGroundRules-25` at `b663756ca`: `read_legs_for` parses the
  `--legs-for` output by its grammar. A header is a line that is not indented and does not open with
  `legs-for:`; its path is the header with ` (not tracked at HEAD)` cut off its end, the suffix
  `KEEP_SUFFIX` in §6 stages back; its legs are the indented ` <- ` lines up to the next header; the `legs-for:`
  footer belongs to no path. Every `legs-for: REFUSING` line exits non-zero, which `read_legs_for`
  raises as the `RuntimeError` `check_guard_trace` prints as its `WRONG`. S11 owes no code; AC11
  observes its staged half. Observed by AC11.
- **S12** — Finding 12. Built by `TOOL-dGroundRules-25` at `b663756ca`: `read_legs_for` runs the
  checker with `cwd=top`, `top` being `derive_source_top()`, the top level `run_fixture` stores in
  `TRACE_ROOTS` and `add_source_read` relativises against. S12 owes no code; AC12 observes its
  staged half. Observed by AC12.
- **S13** — Finding 13. §4 Evidence states what `git ls-files .claude` holds by the exact command
  and output that answer `TOOL-dGroundRules-34` AC3's question. Observed by AC13.
- **S14** — Finding 15, the skeptic's corrected fix. The receipt prefix rule `derive_census_tree`
  spells inline moves into one function, `check_receipt_prefix(value)`, which answers True for a
  string that opens with neither `/` nor a backslash, matches no drive letter and holds no `..`
  segment split on either separator, and which `derive_census_tree` calls, its answers unchanged.
  `TOOL-dGroundRules-34` S21 makes that rule stricter than the deployer's `demand_contained_dest`
  on purpose: the deployer normalises first and admits a value whose `..` segments resolve inside,
  and this rule refuses every `..` segment. §10 names `demand_contained_dest` as the rule it is held
  to, and a probe runs a shared table through both: seven values they must agree on and the two
  where S21's strictness must show. Observed by AC14.
- **S15** — Finding 16. `resolve_govkit(root)` locates the deployer by `resolve_kit_dir`, home
  `govkit`, anchor `govkit.py`, here `<root>/<tool root>/policy`, the locator `check_policy.py`
  carries as `resolve_kit_dir = policy.resolve_kit_dir` (`TOOL-dGroundRules-16` §4 step 2), and
  returns that directory's deployer file. It catches the `LookupError` that function raises and
  raises the `RuntimeError` its callers `run_govkit`, `read_deploy_answers` and `run_ships_join`
  already catch, the lookup's text whole, so the locate refusal `TOOL-dGroundRules-34` S8 names
  prints as one `WRONG` naming the three places looked. Observed by AC15.

## 3. Non-goals (OUT)

- The HIGH ids: `TOOL-dGroundRules-35` to `TOOL-dGroundRules-42`.
- Rewriting any reviewed spec's text. Each defect a spec stated is closed here in the code and the
  observation it governs, and each repaired unit's §3 names this unit; nothing is folded
  (BUILD-METHOD M4).
- Staging the version arm back into the built tree: `OLD_ARM` stages it in a scratch copy only.
- The review's left-shift checklist entries. Each is a bug-class follow-up for the closing review
  (BUILD-METHOD M8); the criterion class is `TOOL-dGroundRules-42`'s.
- Renumbering any unit's `order`.
- Loosening the receipt prefix rule to the deployer's: S21's strictness is the decision S14 records.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read` and `check_guard_trace`, whose event filter and present-path join S9 amends, beside `read_legs_for` and `check_guard_lines`, which units 25 and 37 built and S11, S12 and AC8, AC9, AC11 and AC12 rest on
- **consumes-from** `TOOL-dGroundRules-34` — `build_source_snapshot`, `resolve_govkit`, the receipt prefix rule, `run_fresh_target`'s `gov_source` assertion and the criteria AC5, AC11, AC12, AC15, AC16, AC26 and AC32, which S1 to S8, S10 and S13 to S15 amend or observe
- **consumes-from** `TOOL-dGroundRules-30` — AC3, the zero count S7 observes on the built tree, and the arm that unit took out at `93e4b4d31`
- **hands-off** `TOOL-dGroundRules-45` — AC1, which that unit observes through `PAIRS_TABLE` (id 20 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-51` — S3 and AC3, which that unit observes with the build README's path whole (id 21 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — `build_source_snapshot`'s excludes forwarding, the S9 event filter, and AC1, AC3, AC6 and AC13, which that unit amends or observes (ids 3, 7, 12, 14, 16, 18, 25 and 36 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-59` — AC1, which that unit observes through `PAIRS_TABLE_WHOLE` (id 13 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-24 at `7a600abf5`, unless it names another revision.

- The build-order markers of `memory/builds/dGroundRules/README.md`, by `git show` at each revision
  and `grep -n gen:build-order` (PINNED): lines 105 and 108 at `3708a705`, 147 and 159 at
  `e9709240e`, 165 and 179 at `f4d31452a`, 169 and 185 at `b9f7b5c4e`. `TOOL-dGroundRules-32` §4
  cites 147 to 159 as read at `3708a705`; those lines hold at `e9709240e`. The root `README.md`
  holds no such marker at `f4d31452a`.
- `git ls-files .claude | grep -cE '^\.claude/(worktrees/|scheduled_tasks\.lock|mailbox/)'` printed
  `0`; `git ls-files .claude` also lists `.claude/roles.json`, `.claude/settings.json`,
  `.claude/rules/product.md` and seven `.claude/skills/*/SKILL.md` files, beside the agents.
- A scratch audit-hook probe on Python 3.14.6 recorded `os.open(<f>, O_CREAT|O_WRONLY)` as
  `(<f>, None, 385)` and a failed `open` of an absent file as `(<f>, 'r', 32896)`, raised before
  the failure. `add_source_read` reads a None mode as `r`, so the first is kept today.
- In `tools/check-spec-tokens.py`, `print_legs_for` appends ` (not tracked at HEAD)` to an
  untracked path's header, prints the `legs-for:` footer, and returns non-zero after every
  `legs-for: REFUSING` line; `main` takes its root from `git rev-parse --show-toplevel` in the
  process working directory.
- In `tools/policy/check_policy.py`, `read_legs_for` runs the checker with `cwd=top` and cuts the
  suffix with `removesuffix` (`git log -S` names `b663756ca`), and `run_fresh_target` compares the
  `gov_source` by `resolve()` (`75b1ffe59`). `derive_census_tree` spells the receipt prefix rule
  inline, and `resolve_govkit` joins a fixed path and raises
  `RuntimeError("no deployer to install with: ...")`.
- In `tools/govkit/govkit.py`, `GOVKIT_DIR` is resolved, and `_cmd_apply` and `_cmd_adopt` write
  `"gov_source": str(root)`; `tempfile.gettempdir()` on this node is the 8.3 spelling
  `C:\Users\DAILY-~1\AppData\Local\Temp` (review id 11).
- `DRIVE_PREFIX_RE` and `demand_contained_dest(dest, where)` sit together in that file. The probe
  of §6 `PREFIX_PARITY`'s nine values, the receipt rule read from `derive_census_tree`, printed
  `refused refused` for the six escapes, `admitted admitted` for `tools`, and `refused admitted`
  for `a/..` and `x/../y`.
- `resolve_kit_dir(home, anchor, here)` in `tools/lib/resolve_kit_dir.py`, and its copy inlined in
  `tools/policy/policy.py`, return the kit directory or raise
  `LookupError("no <home> kit holding <anchor> in this install: looked in ...")`.
- `TOOL-dGroundRules-30` AC3 expects `0`; `TOOL-dGroundRules-34` S5 records the arm out at
  `93e4b4d31` and its AC5 expects `0`, as at `eb67e2cc8`. `git show` of the parity suite at
  `93e4b4d31^` piped to `grep -c KIT_AGENT_CAP_VERSION` printed `2` (PINNED).
- `ORDER_ROWS | wc -l` and `ORDERS` each printed `19`; step 1 of the region holds two units.

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S9, S10, S14, S15 |
| the codebase map | S14, by regeneration |

S1 to S8 and S11 to S13 change no code of their own; each is the observation this unit owes for a
defect in a criterion or a stated outcome, made against the code units 25, 30, 33, 34 and 37 build.

### The trace after S9

```text
add_source_read(event, args):
    if event != "open" or args[0] is an int: return
    mode, flags = args[1], args[2]
    if mode is None: return if flags & (O_WRONLY | O_RDWR | O_CREAT)      # S9
    elif any of "wax+" in mode: return
    (units 33, 35 and 38's path steps; keep)

check_guard_trace():
    print " · <n> source read(s)"
    present = [p for p in kept if (top / p).exists()]; print " · <n> absent read(s) set aside"   # S9
    (TOOL-dGroundRules-36's ignore set-aside over present; read_legs_for at cwd = top, as built)
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_receipt_prefix` | py.function | `tools/policy/check_policy.py` |
| `absent read(s) set aside` | a `guard-trace` line | `tools/policy/check_policy.py` |

`lexicon.py --suggest check_receipt_prefix --as py.function` answered OK on 2026-10-24.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Two batch units, the trace half and the snapshot half.** Both write
  `tools/policy/check_policy.py`, so M6's first clause fails.
- **`ls-files -co --exclude-standard` run in the source for S10** (`TOOL-dGroundRules-34` §8 F6
  option (c)). It meets the criterion too, and replaces the `add -A` that unit's S1 to S4 build on;
  the `-c` value is one argument on the call that exists.
- **A parity table that demands agreement on every value for S14.** It would red on `a/..` and
  `x/../y` by S21's own design, or push the receipt rule down to the deployer's normalised one.

## 5. Production-readiness checklist

- security — S14 records the receipt prefix rule as stricter than the deployer's containment rule
  and probes both; no item widens a write surface.
- perf / scale — S10 adds one `git config` call per snapshot; S9 adds one existence test per kept
  path.
- error / empty / loading states — S9 counts the absent reads it leaves out; S15 turns a missing
  deployer into the `RuntimeError` every caller already prints as a named `WRONG`.
- observability — the absent-read count line; S15's refusal names the three places looked.
- risks — S10 passes the source's effective excludes file, which is what `git status` there reads.
- testing — the cases under `--fixture` and AC1 to AC15.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: gov-only legs and probes.

## 6. Acceptance criteria

Every command runs from the repository root. `ORDER_ROWS` is the expression `TOOL-dGroundRules-34`
§6 defines. A fixture repository is a `git init` repository under `%TEMP%/<short name>`. A scratch
copy is a `git clone` of the built tree under `%TEMP%/<short name>`, `<copy>` its root, and a
staging is an edit of its working tree; a command a criterion runs over the copy is spelled
`(cd <copy> && <command>)` or names its file under `<copy>`. `FIX <case>` stands for
`python tools/policy/check_policy.py --fixture <case>`, and `FIX <case>` in the copy for the same
with the script under `<copy>`. Literal commands and stagings are spelled whole here, once, and the
criteria name them:

```text
EVIDENCE      = git show f4d31452a:memory/builds/dGroundRules/README.md | grep -n gen:build-order
ORDERS        = grep -h '^\*\*Status:\*\*' memory/builds/dGroundRules/spec/*.md | grep -oE '· order [0-9]+' | sort -u | wc -l
MOVE_MARKER   = in a scratch copy of the build README, "<!-- /gen:build-order -->" moved above the
                region's last row
ORDER_SHIFT   = in a scratch copy, the "· order <n>" of one unit spec whose step the region shows
                holding more than one unit (step 1 holds two) changed to a value no unit holds,
                the README not re-rendered
OLD_ARM       = git -C <copy> checkout 93e4b4d31^ -- tools/workflows/check-protocol-parity.test.sh
RAW_GOV       = in a scratch copy, run_fresh_target's gov_source comparison staged to
                said != str(s), the two strings as spelled
PLANT_WRITES  = in a scratch copy, run_fresh_target's first lines staged to os.open
                <copy>/probe_w.lock with O_CREAT|O_WRONLY, and to open() an absent
                <copy>/probe_absent.txt, each failure caught
EXCLUDES_REPO = a fixture repository <r> with one committed file, an untracked <r>/kept.txt and an
                untracked <r>/secret.local, and a repository-local core.excludesFile naming a file
                that lists secret.local
SNAP_PROBE    = python -c "import sys; sys.path.insert(0, sys.argv[1]); import check_policy as c;
                print(c.build_source_snapshot(sys.argv[2]))" tools/policy <r>
PLANT_UNTRACKED = in a scratch copy, a new untracked <copy>/tools/govkit/entries/probe_new.toml,
                read in process by run_fresh_target's first line
KEEP_SUFFIX   = in that copy, read_legs_for's removesuffix staged to keep the header whole
NO_CWD        = in a scratch copy, read_legs_for's cwd=top staged out of its subprocess call
FAR_CWD       = R=<root>; mkdir -p "$TEMP/gr43" && (cd "$TEMP/gr43" &&
                python "$R/tools/policy/check_policy.py" --fixture adopter-fresh-target)
                where <root> is $PWD at the repository root, or <copy>; $TEMP/gr43 is no repository
PREFIX_PARITY = python -c probe with tools/policy and tools/govkit on sys.path that runs
                ../x  a/../../b  /x  \\srv\s  C:x  C:/x  tools  a/..  x/../y
                through check_receipt_prefix and through demand_contained_dest(value, "probe"),
                a Refusal read as refused, and prints "<value> <receipt answer> <deployer answer>"
NO_GOVKIT     = in a scratch copy, tools/govkit/govkit.py renamed to another name
```

- **AC1** — When `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6 run on the built tree, they
  print `True` then `False`, and `0` then `1`.
  Red when: either overlap rule misreads a directory over a file or a shared string prefix.
- **AC2** — When `FIX census-window-edge` runs, it prints `RED as planted` and no `WRONG`, and
  `python tools/policy/check_policy.py --repo <t>` over `TREE_AMBIG` of `TOOL-dGroundRules-39` §6
  prints one `arm_cap_census` finding naming both paths.
  Red when: an input of `TOOL-dGroundRules-34`'s AC11 or AC12 is shortened out of the window it probes.
- **AC3** — When `EVIDENCE` runs, it prints lines `165` and `179`.
  Red when: the evidence cites lines its stated revision does not hold in the build README.
  figure: PINNED, the revision being fixed; this is a check on evidence, not on the build.
- **AC4** — When `MOVE_MARKER` runs, `ORDER_ROWS | wc -l` over that copy prints a number below what
  `ORDERS` prints there.
  Red when: the region is selected by something other than its markers, so a moved marker goes unseen.
- **AC5** — When `ORDER_ROWS | wc -l` and `ORDERS` run on the built tree, they print the same number,
  the comparison `TOOL-dGroundRules-34` AC26 makes with `ORDERS` as spelled. It is green before this
  unit; the staged half it rests on is AC6.
  Red when: the region drops, repeats or adds a step.
  figure: both counts are DERIVED at observation time.
- **AC6** — When `ORDER_SHIFT` runs, `ORDERS` over that copy prints one more than
  `ORDER_ROWS | wc -l` there.
  Red when: the comparison of the two counts cannot see a step the region failed to render.
- **AC7** — When `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh`
  runs on the built tree, it prints `0`; after `OLD_ARM`, the same grep over that file in the copy
  prints `2`.
  Red when: the zero is read where the arm never was, so `TOOL-dGroundRules-34`'s zero figure cannot fail.
  figure: `2` PINNED at `93e4b4d31^`; `0` DERIVED at observation time.
- **AC8** — When `FIX adopter-fresh-target` runs on this node, it prints no `WRONG`, as it does
  before this unit; after `RAW_GOV`, `FIX adopter-fresh-target` in the copy prints `WRONG` naming
  `gov_source`.
  Red when: an 8.3 temporary path and its resolved form are read as two checkouts unseen.
  fixture: a node whose system temporary directory has an 8.3 spelling; this node's does.
  rests on: the no-`WRONG` half also needs `TOOL-dGroundRules-37`'s `check_guard_lines`, built at `7a600abf5` before this unit, to find no dead guard entry.
- **AC9** — When `PLANT_WRITES` runs and then `FIX adopter-fresh-target` in the copy runs, it prints
  the `absent read(s) set aside` line with a count of 1 or more and no `guard-trace` line naming
  either planted file.
  Red when: a write through `os.open` or a probe of an absent file is joined as a source read.
  rests on: the no-`WRONG` half also needs `TOOL-dGroundRules-37`'s `check_guard_lines`, built at `7a600abf5` before this unit, to find no dead guard entry.
- **AC10** — When `SNAP_PROBE` runs over `EXCLUDES_REPO`, `git -C <s> ls-tree -r --name-only HEAD`
  on the root it prints lists the fixture's kept.txt and not its secret.local.
  Red when: the snapshot commits a file the source's own configuration hides from `git status`.
- **AC11** — When `PLANT_UNTRACKED` runs and then `FIX adopter-fresh-target` in the copy runs, it
  prints no `guard-trace` `WRONG` naming the planted entry, as it does before this unit; after
  `KEEP_SUFFIX` too, the same run prints a `guard-trace` `WRONG` naming it.
  Red when: an untracked header's suffix makes a guarded path read as unguarded, unseen.
  rests on: the no-`WRONG` half also needs `TOOL-dGroundRules-37`'s `check_guard_lines`, built at `7a600abf5` before this unit, to find no dead guard entry.
- **AC12** — When `FAR_CWD` runs with the repository root, it prints the same `guard-trace` lines as
  `FIX adopter-fresh-target`, as it does before this unit; after `NO_CWD`, `FAR_CWD` with the copy
  prints a `guard-trace` `WRONG` naming `--legs-for`.
  Red when: the guard join reads another directory's manifest or tracked set, unseen.
  rests on: the no-`WRONG` half also needs `TOOL-dGroundRules-37`'s `check_guard_lines`, built at `7a600abf5` before this unit, to find no dead guard entry.
- **AC13** — When `git ls-files .claude` is piped to the `grep -cE` §4 Evidence quotes, it prints `0`.
  Red when: a tracked `.claude` file matches the local-state pattern `TOOL-dGroundRules-34` AC3 greps.
- **AC14** — When `PREFIX_PARITY` runs, each of its first seven lines carries two equal answers,
  `admitted` on the `tools` line alone, and the lines for `a/..` and `x/../y` carry `refused` then
  `admitted`.
  Red when: the two rules disagree on a value they share, or S21's stricter refusal of a `..` segment goes unseen.
- **AC15** — When `NO_GOVKIT` runs and then `FIX budgets-ships-join` in the copy runs, it prints
  `WRONG` carrying `no govkit kit holding govkit.py`.
  Red when: `resolve_govkit` locates the deployer by a second locator, or lets its `LookupError` past the callers' catch.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms` · `policy fixtures`

`policy fixtures` runs the cases these criteria name and the arm below.

New arm: tools/policy/check_policy.py --fixture · covers AC8 AC9 AC11 AC12 AC15 · the `gov_source` comparison staged to raw strings, a write and an absent read planted, the untracked suffix kept, the checker's working directory staged out, and the deployer renamed, each in a scratch copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting the eleven MEDIUM and four LOW findings of the
  round-1 spec audit of units 33 and 34 in one batch, from the review's sound fixes and the skeptic's
  corrected fix for id 15, with each cited line read at `b9f7b5c4e`.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-45`, `TOOL-dGroundRules-51`, `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.
- rev-3 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-59`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.
- rev-4 · 2026-10-24 · §7 · the policy fixtures leg added to the leg line, owed by its guard, which a §4 path trips; no design change.
- rev-5 · 2026-10-24 · §1 §2 §3 §4 §5 §6 §7 · S5 S7 S8 S11 S12 S14 S15 · AC3 AC5 AC6 AC7 AC8 AC9
  AC10 AC11 AC12 AC14 AC15 · restated against the built branch from the read-only probe of step 14
  at `0860b8c1e`. Its disagreements: S5, S8, S11 and S12 were stated as work when units 34 and 25
  had built them, leaving AC8, AC11 and AC12 green before the unit; S7 placed the arm's exit at
  unit 34, where unit 30 took it out at `93e4b4d31`; `EVIDENCE` read the root README; `ORDER_SHIFT`
  could move a lone unit and leave the distinct count flat; S14's parity demanded agreement S21
  refuses by design, called `demand_contained_dest` with one argument and named `arm_cap_census` as
  the caller; S15 let a `LookupError` past callers that catch `RuntimeError`; §1 claimed order 14 is
  above every unit of the build; §7 said the policy legs do not exist; criteria ran bare file names;
  `build_fresh_target` names no function. The run's rulings: S5, S8, S11 and S12 restated as built,
  each with its confirming observation, and each criterion green before the unit observes its staged
  half (`KEEP_SUFFIX` and `NO_CWD` added); `OLD_ARM` checks the file out at `93e4b4d31^`;
  `EVIDENCE` reads the build README; `ORDER_SHIFT` moves a unit from a step of two or more;
  AC14 asserts agreement on seven values and `refused admitted` on `a/..` and `x/../y`; S15 raises
  the `RuntimeError` its callers catch; §1 states order 14 beside units 44 to 50; AC8, AC9, AC11
  and AC12 name their rest on `TOOL-dGroundRules-37`'s dead-guard check; every moved line cited by
  symbol; every criterion command spelled from the repository root.

## 10. Reuse audit

Each item extends a seam already named in its row: `TOOL-dGroundRules-33`'s `add_source_read` and
`check_guard_trace` (S9), `TOOL-dGroundRules-25`'s `read_legs_for` (S11, S12, as built),
`TOOL-dGroundRules-34`'s `build_source_snapshot`, the `gov_source` assertion in `run_fresh_target`
and the receipt prefix rule in `derive_census_tree` (S8, S10, S14), the inlined `resolve_kit_dir`
of `tools/lib/resolve_kit_dir.py` (S15), which `TOOL-dGroundRules-34` §10 listed and did not reuse,
`demand_contained_dest` in `tools/govkit/govkit.py`, the rule S14's parity is held to, and the
literals `TOOL-dGroundRules-39` and `TOOL-dGroundRules-40` spell (S1, S2).
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"` and
`python tools/codebase-map/reuse_lookup.py "decide whether two write sets overlap by path containment"`
ranked `run_git`, `read_git_output` and `overlaps` among name-stem hits; the other seams were found
by reading the files the review cites, each verified at `7a600abf5`. The recall probe returned the
prior minors batches `TOOL-dGroundRules-32` and `TOOL-dGroundRules-34`, whose one-item-per-finding
table this unit follows, and this audit's own items.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
