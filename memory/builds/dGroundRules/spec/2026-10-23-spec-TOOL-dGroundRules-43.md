# TOOL-dGroundRules-43 — the round-1 audit of units 33 and 34, its minors: fifteen findings closed in the code those units leave, one scope item each

**Status:** OPEN · rev-3 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-43-deviation-31.md](../build/2026-10-23-build-TOOL-dGroundRules-43-deviation-31.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with 23 confirmed findings. Its eight HIGH ids are promoted one unit each,
`TOOL-dGroundRules-35` to `TOOL-dGroundRules-42`. BUILD-METHOD M4 promotes the other fifteen,
eleven MEDIUM and four LOW, batched into one unit, and this is that unit. They land on units 33 and
34, and on 30 through id 6. They do not split into two disjoint write sets by M6's clauses: the
trace items (ids 20, 27 and 12) and the snapshot and census items (ids 11, 26, 15 and 16) all write
`tools/policy/check_policy.py`. One unit carries them all. It repairs no unit in particular, so it
builds at order 14, above every unit of this build, units 39 to 42 at order 13 included.

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
corrected fix.

## 2. Scope (IN)

- **S1** — Finding 3. `TOOL-dGroundRules-34` AC15 and AC16 are observed at this unit's close with
  their pairs whole, through `PAIRS_PY` and `PAIRS_SH` as `TOOL-dGroundRules-40` §6 spells them.
  Observed by AC1.
- **S2** — Finding 8. `TOOL-dGroundRules-34` AC11 and AC12 are observed at this unit's close with
  their paths whole, through `TREE_AMBIG` and `census-window-edge` as `TOOL-dGroundRules-39`
  spells them. Observed by AC2.
- **S3** — Finding 5. The build-order region's marker lines at each revision this build's specs
  cite are stated in §4 Evidence, PINNED, so `TOOL-dGroundRules-34` S32's citation is a checked
  piece of evidence: lines 165 and 179 at `f4d31452a`. Observed by AC3.
- **S4** — Finding 10. That `ORDER_ROWS` selects the region by its markers is observed by a break
  that can red it: the closing marker moved up in a scratch copy makes its count fall below the
  distinct `order` values. Observed by AC4.
- **S5** — Finding 4. `TOOL-dGroundRules-34` AC26's right-hand count reads the status lines only and
  requires a digit, `ORDERS` in §6, so the criterion's own text never counts. Observed by AC5.
- **S6** — Finding 9. AC26 is paired with its staged break: one unit's `order` changed in a scratch
  copy, with the README not re-rendered, makes the two counts differ. Observed by AC6.
- **S7** — Finding 6. `TOOL-dGroundRules-30` AC3, the zero count of `KIT_AGENT_CAP_VERSION` in
  `tools/workflows/check-protocol-parity.test.sh`, is observed at `TOOL-dGroundRules-34`'s close,
  after that unit's S5 takes the version-staging arm out, and `TOOL-dGroundRules-34` AC5's figure is
  made failable by staging that arm back into a scratch copy. Observed by AC7.
- **S8** — Finding 11. `adopter-fresh-target` compares the receipt's `gov_source` to the snapshot
  root as `Path(gov_source).resolve() == Path(snapshot_root).resolve()`, the normalisation
  `TOOL-dGroundRules-34` S9 applies to `SNAPSHOT_ROOTS`. Observed by AC8.
- **S9** — Finding 20. `add_source_read` keeps an `open` event only when `args[1]` is a string
  holding none of `w`, `a`, `x` or `+`, or, when `args[1]` is None, when the flags in `args[2]`
  carry none of `os.O_WRONLY`, `os.O_RDWR` or `os.O_CREAT`. `check_guard_trace` joins only the kept
  paths that exist when it runs, and prints the number it left out as
  `policy-fixture: guard-trace · <n> absent read(s) set aside`. Observed by AC9.
- **S10** — Finding 26. `build_source_snapshot` reads
  `git -C <source> config --type=path --get core.excludesFile`, which answers from every scope the
  source sees, its worktree configuration included, and when it is set passes it as
  `-c core.excludesFile=<that>` to the snapshot's `add -A`. Observed by AC10.
- **S11** — Finding 27. `check_guard_trace` parses the `--legs-for` output by its grammar: a header
  is a line that is not indented and does not open with `legs-for:`; its path is the text before an
  optional ` (not tracked at HEAD)`; its legs are the indented lines up to the next header; the
  `legs-for:` footer belongs to no path, and a `legs-for: REFUSING` line is the unreachable-checker
  `WRONG`. Observed by AC11.
- **S12** — Finding 12. The `--legs-for` subprocess runs with its working directory set to the
  source top level, the same top level `add_source_read` relativises against. Observed by AC12.
- **S13** — Finding 13. §4 Evidence states what `git ls-files .claude` holds by the exact command
  and output that answer `TOOL-dGroundRules-34` AC3's question. Observed by AC13.
- **S14** — Finding 15, the skeptic's corrected fix. `TOOL-dGroundRules-34` S21's prefix rule sits
  in one function, `check_receipt_prefix(value)`, which `arm_cap_census` calls; §10 names
  `demand_contained_dest` (`tools/govkit/govkit.py:1304`) as the rule it mirrors, and a probe runs a
  shared table of seven prefixes through both. Observed by AC14.
- **S15** — Finding 16. `resolve_govkit(root)` is
  `resolve_kit_dir("govkit", "govkit.py", <root>/<tool root>/policy) / "govkit.py"`, the inlined
  locator `check_policy.py` already carries (`TOOL-dGroundRules-16` §4 step 2), and the locate
  refusal `TOOL-dGroundRules-34` S8 names is that function's `LookupError`. Observed by AC15.

## 3. Non-goals (OUT)

- The HIGH ids: `TOOL-dGroundRules-35` to `TOOL-dGroundRules-42`.
- Rewriting any reviewed spec's text. Each defect a spec stated is closed here in the code and the
  observation it governs, and each repaired unit's §3 names this unit; nothing is folded
  (BUILD-METHOD M4).
- Moving `TOOL-dGroundRules-34` S5's arm change into unit 30. That is a fold of unit 30's scope;
  S7 places the observation instead.
- The review's left-shift checklist entries. Each is a bug-class follow-up for the closing review
  (BUILD-METHOD M8); the criterion class is `TOOL-dGroundRules-42`'s.
- Renumbering any unit's `order`.

### Edges

- **consumes-from** `TOOL-dGroundRules-33` — `add_source_read` and `check_guard_trace`, whose event filter, parse and working directory S9, S11 and S12 amend
- **consumes-from** `TOOL-dGroundRules-34` — `build_source_snapshot`, `resolve_govkit`, the receipt prefix rule, `adopter-fresh-target`'s `gov_source` assertion and the criteria AC5, AC11, AC12, AC15, AC16, AC26 and AC32, which S1 to S8, S10 and S13 to S15 amend or observe
- **consumes-from** `TOOL-dGroundRules-30` — AC3, the zero count S7 observes at `TOOL-dGroundRules-34`'s close
- **hands-off** `TOOL-dGroundRules-45` — AC1, which that unit observes through `PAIRS_TABLE` (id 20 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-51` — S3 and AC3, which that unit observes with the build README's path whole (id 21 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — `build_source_snapshot`'s excludes forwarding, the S9 event filter, and AC1, AC3, AC6 and AC13, which that unit amends or observes (ids 3, 7, 12, 14, 16, 18, 25 and 36 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-59` — AC1, which that unit observes through `PAIRS_TABLE_WHOLE` (id 13 of the closing diff review, round 1)

## 4. Design

### Evidence

Every line below was read or run on 2026-10-23 at `b9f7b5c4e`, unless it names another revision.

- The build-order markers of `memory/builds/dGroundRules/README.md`, by `git show <rev>:<that path>`
  and `grep -n gen:build-order` (PINNED): lines 105 and 108 at `3708a705`, 147 and 159 at
  `e9709240e`, 165 and 179 at `f4d31452a`, 169 and 185 at `b9f7b5c4e`. `TOOL-dGroundRules-32` §4
  cites 147 to 159 as read at `3708a705`; those lines hold at `e9709240e`.
- `git ls-files .claude | grep -cE '^\.claude/(worktrees/|scheduled_tasks\.lock|mailbox/)'` printed
  `0`; `git ls-files .claude` also lists `.claude/roles.json`, `.claude/settings.json`,
  `.claude/rules/product.md` and seven `.claude/skills/*/SKILL.md` files, beside the agents.
- A scratch audit-hook probe on Python 3.14.6 recorded `os.open(<f>, O_CREAT|O_WRONLY)` as
  `(<f>, None, 385)` and a failed `open` of an absent file as `(<f>, 'r', 32896)`, raised before
  the failure.
- `tools/check-spec-tokens.py:667` appends ` (not tracked at HEAD)` to an untracked path's header,
  `:676` prints the `legs-for:` footer, and `:1369` takes its root from `git rev-parse --show-toplevel`
  in the process working directory.
- `tools/govkit/govkit.py:122` resolves `GOVKIT_DIR`, and `:7981` and `:13030` write
  `"gov_source": str(root)`; `tempfile.gettempdir()` on this node is the 8.3 spelling
  `C:\Users\DAILY-~1\AppData\Local\Temp` (review id 11).
- `tools/govkit/govkit.py:1301` declares `DRIVE_PREFIX_RE` and `:1304` `demand_contained_dest`.
- `tools/lib/resolve_kit_dir.py:15` `resolve_kit_dir(home, anchor, here)` returns the kit directory
  or raises `LookupError("no <home> kit holding <anchor> in this install: looked in ...")`.
- `TOOL-dGroundRules-30` AC3 (:133-135) expects `0`, and its hands-off line (:57) says the zero
  holds once `TOOL-dGroundRules-34` takes the arm out; `TOOL-dGroundRules-34` AC5 (:456-460) claims a
  pre-unit count of at least 1.

### Per-item changes, by file

| File | Items |
|---|---|
| `tools/policy/check_policy.py` | S8 to S12, S14, S15 |
| the codebase map | S14, by regeneration |

S1 to S7 and S13 change no code of their own; each is the observation this unit owes for a defect
in a criterion or a stated outcome, made against the code units 30, 33 and 34 build.

### The trace after S9, S11 and S12

```text
add_source_read(event, args):
    if event != "open" or args[0] is an int: return
    mode, flags = args[1], args[2]
    if mode is None: return if flags & (O_WRONLY | O_RDWR | O_CREAT)      # S9
    elif any of "wax+" in mode: return
    (units 33, 35 and 38's path steps; keep)

check_guard_trace():
    present = [p for p in kept if (top / p).exists()]; print " · <n> absent read(s) set aside"   # S9
    (TOOL-dGroundRules-36's ignore set-aside over present)
    out = run(python <source tool root>/check-spec-tokens.py --legs-for -, cwd = top)           # S12
    blocks = parse: header = unindented, not "legs-for:"; path = header minus " (not tracked at HEAD)";
             legs = indented lines up to the next header                                         # S11
    WRONG if out holds "legs-for: REFUSING"
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `check_receipt_prefix` | py.function | `tools/policy/check_policy.py` |
| `absent read(s) set aside` | a `guard-trace` line | `tools/policy/check_policy.py` |

`lexicon.py --suggest check_receipt_prefix --as py.function` answered OK on 2026-10-23.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **Two batch units, the trace half and the snapshot half.** Both write
  `tools/policy/check_policy.py`, so M6's first clause fails.
- **`ls-files -co --exclude-standard` run in the source for S10** (`TOOL-dGroundRules-34` §8 F6
  option (c)). It meets the criterion too, and replaces the `add -A` that unit's S1 to S4 build on;
  the `-c` value is one argument on the call that exists.
- **S7 by moving the arm change into unit 30.** That rewrites unit 30's scope, a fold M4 forbids.

## 5. Production-readiness checklist

- security — S14 holds the receipt prefix rule to the deployer's own containment rule; no item
  widens a write surface.
- perf / scale — S10 adds one `git config` call per snapshot; S9 adds one existence test per kept
  path.
- error / empty / loading states — S9 counts the absent reads it leaves out; S11 turns a refusing
  checker into a named `WRONG`.
- observability — the absent-read count line; S15's refusal names the three places looked.
- risks — S10 passes the source's effective excludes file, which is what `git status` there reads.
- testing — the cases under `--fixture` and AC1 to AC15.
- migration — the codebase map regenerated in this unit's commit.
- user docs — N/A: gov-only legs and probes.

## 6. Acceptance criteria

Every command runs from the repository root unless it says otherwise. `check_policy.py` names the
policy kit's file under the kit, as `TOOL-dGroundRules-34` §6 does, and `ORDER_ROWS` is the
expression that section defines. A fixture repository is a `git init` repository under
`%TEMP%/<short name>`. Literal commands and stagings are spelled whole here, once, and the criteria
name them:

```text
EVIDENCE      = git show f4d31452a:README.md | grep -n gen:build-order
ORDERS        = grep -h '^\*\*Status:\*\*' memory/builds/dGroundRules/spec/*.md | grep -oE '· order [0-9]+' | sort -u | wc -l
MOVE_MARKER   = in a scratch copy of memory/builds/dGroundRules/README.md, "<!-- /gen:build-order -->"
                moved above the region's last row
ORDER_SHIFT   = in a scratch copy, one unit spec's "· order <n>" changed to a value no unit holds,
                the README not re-rendered
OLD_ARM       = in a scratch copy, the arm TOOL-dGroundRules-25 §7 declares for its AC18 staged back
                into tools/workflows/check-protocol-parity.test.sh
RAW_GOV       = in a scratch copy, the S8 comparison staged to compare the two strings as spelled
PLANT_WRITES  = in a scratch copy, build_fresh_target's first lines staged to os.open probe_w.lock
                under the source top level with O_CREAT|O_WRONLY, and to open() an absent
                probe_absent.txt there, each failure caught
EXCLUDES_REPO = a fixture repository with one committed file, an untracked kept.txt and an untracked
                secret.local, and a repository-local core.excludesFile naming a file that lists
                secret.local
PLANT_UNTRACKED = in a scratch copy, a new untracked tools/govkit/entries/probe_new.toml, read in
                process by build_fresh_target's first line
FAR_CWD       = cd "$TEMP/gr43" (a directory that is not a repository), then
                python <this repository>/tools/policy/check_policy.py --fixture adopter-fresh-target
PREFIX_PARITY = python -c probe with the kit directory and tools/govkit on sys.path that runs
                ../x  a/../../b  /x  \\srv\s  C:x  C:/x  tools  through check_receipt_prefix and
                through demand_contained_dest (a Refusal counted as refused) and prints
                "<value> <answer> <answer>" per value
NO_GOVKIT     = in a scratch copy, tools/govkit/govkit.py renamed to another name
```

- **AC1** — When `PAIRS_PY` and `PAIRS_SH` of `TOOL-dGroundRules-40` §6 run on the built tree, they
  print `True` then `False`, and `0` then `1`.
  Red when: either overlap rule misreads a directory over a file or a shared string prefix.
- **AC2** — When `python check_policy.py --fixture census-window-edge` runs, it prints
  `RED as planted` and no `WRONG`, and `python check_policy.py --repo <t>` over `TREE_AMBIG` of
  `TOOL-dGroundRules-39` §6 prints one `arm_cap_census` finding naming both paths.
  Red when: an input of AC11 or AC12 is shortened out of the window it probes.
- **AC3** — When `EVIDENCE` runs, it prints lines `165` and `179`.
  Red when: the evidence cites lines its stated revision does not hold.
  figure: PINNED, the revision being fixed; this is a check on evidence, not on the build.
- **AC4** — When `MOVE_MARKER` runs and `ORDER_ROWS | wc -l` runs over that copy, it prints a number
  below what `ORDERS` prints.
  Red when: the region is selected by something other than its markers, so a moved marker goes unseen.
- **AC5** — When `ORDER_ROWS | wc -l` and `ORDERS` run on the built tree, they print the same number.
  Red when: the region drops, repeats or adds a step.
  figure: both counts are DERIVED at observation time.
- **AC6** — When `ORDER_SHIFT` runs, `ORDERS` over that copy prints one more than `ORDER_ROWS | wc -l`.
  Red when: AC5's comparison cannot see a step the region failed to render.
- **AC7** — When `grep -c "KIT_AGENT_CAP_VERSION" tools/workflows/check-protocol-parity.test.sh` runs
  on the built tree, it prints `0`; after `OLD_ARM`, it prints `1` or more.
  Red when: unit 30's zero is read before the arm leaves, or AC5's count cannot fail.
- **AC8** — When `python check_policy.py --fixture adopter-fresh-target` runs on this node, it prints
  no `WRONG`; after `RAW_GOV`, it prints `WRONG` naming `gov_source`.
  Red when: an 8.3 temporary path and its resolved form are read as two checkouts.
  fixture: a node whose system temporary directory has an 8.3 spelling; this node's does.
- **AC9** — When `PLANT_WRITES` runs and then the AC8 command runs in that copy, it prints the
  `absent read(s) set aside` line with a count of 1 or more and no `guard-trace` line naming
  `probe_w.lock` or `probe_absent.txt`.
  Red when: a write through `os.open` or a probe of an absent file is joined as a source read.
- **AC10** — When `build_source_snapshot` runs over `EXCLUDES_REPO`,
  `git -C <s> ls-tree -r --name-only HEAD` lists `kept.txt` and not `secret.local`.
  Red when: the snapshot commits a file the source's own configuration hides from `git status`.
- **AC11** — When `PLANT_UNTRACKED` runs and then the AC8 command runs in that copy, it prints no
  `guard-trace` `WRONG` naming `probe_new.toml`.
  Red when: an untracked header's suffix makes a guarded path read as unguarded.
- **AC12** — When `FAR_CWD` runs, it prints the same `guard-trace` lines as the AC8 command from the
  repository root.
  Red when: the guard join reads another repository's manifest or tracked set.
- **AC13** — When `git ls-files .claude` is piped to the `grep -cE` §4 Evidence quotes, it prints `0`.
  Red when: a tracked `.claude` file matches the local-state pattern `TOOL-dGroundRules-34` AC3 greps.
- **AC14** — When `PREFIX_PARITY` runs, every line it prints carries two equal answers.
  Red when: the receipt checker and the deployer disagree on which prefix leaves the target.
- **AC15** — When `NO_GOVKIT` runs and then `python check_policy.py --fixture budgets-ships-join`
  runs in that copy, it prints `WRONG` carrying `no govkit kit holding govkit.py`.
  Red when: `check_policy.py` locates the deployer by a second locator with its own refusal.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the cases;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py --fixture · covers AC8 AC9 AC11 AC15 · the `gov_source` comparison staged to raw strings, a write and an absent read planted, an untracked guarded read planted, and the deployer renamed, each in a scratch copy · none

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

## 10. Reuse audit

Each item extends a seam already named in its row: `TOOL-dGroundRules-33`'s `add_source_read` and
`check_guard_trace` (S9, S11, S12), `TOOL-dGroundRules-34`'s `build_source_snapshot`, the
`gov_source` assertion and the receipt prefix rule (S8, S10, S14), the inlined `resolve_kit_dir` of
`tools/lib/resolve_kit_dir.py` (S15), which `TOOL-dGroundRules-34` §10 listed and did not reuse,
`demand_contained_dest` in `tools/govkit/govkit.py:1304`, the rule S14's parity mirrors, and the
literals `TOOL-dGroundRules-39` and `TOOL-dGroundRules-40` spell (S1, S2).
`python tools/codebase-map/reuse_lookup.py "drop paths git ignores from a list of file paths"` and
`python tools/codebase-map/reuse_lookup.py "decide whether two write sets overlap by path containment"`
ranked `run_git`, `read_git_output` and `overlaps` among name-stem hits; the other seams were found
by reading the files the review cites, each verified at `b9f7b5c4e`. The recall probe returned the
prior minors batches `TOOL-dGroundRules-32` and `TOOL-dGroundRules-34`, whose one-item-per-finding
table this unit follows, and this audit's own items.

Recall terms used: `python tools/memory-recall/query.py "how are review minors batched into one
repair unit" --terms "minors batch promoted medium low disposed severity spec-audit repair unit write
set"`
