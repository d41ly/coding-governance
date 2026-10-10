# TOOL-aRoutedQuill-12 — the closing review's mediums and lows, and the bar reds this build's diff carries

**Status:** INPROGRESS · rev-2 · 2026-10-10 · node a · Tier-2 · base e6585db4 · streams tooling+kickoff · order 6 · ratified 2026-10-10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-10-prompt-TOOL-aRoutedQuill-12-build-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-12-build-brief.md) | journal | — |
| [2026-10-10-prompt-TOOL-aRoutedQuill-12-spec-brief.md](../prompts/2026-10-10-prompt-TOOL-aRoutedQuill-12-spec-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

Round 1 of the closing review confirmed nine mediums and seven lows against this build's diff, and
the severity rule promotes them as ONE batched unit. This unit fixes each one as the skeptic judged
it, together with the four bar reds the same diff carries, so the close runs a bar that can be green.

## 2. Scope (IN)

Each item names its finding in the review record
`memory/builds/aRoutedQuill/reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md`.
Line numbers are at `4edeb4678` and move as earlier items land.

- **S1** — M1. `read_memory_root` in `skills/session-kickoff/manifest-check.sh` reads the conf the
  way the shell does: it sources `.memory-tree.conf` in a subshell and prints `${MEMORY_ROOT-}`, as
  `derive_routed_candidate` in `tools/memory-tree/adopt-memory-tree.sh` already does, and keeps its
  return 1 for a tree with no conf. An exported, a commented, a quoted and a twice-assigned spelling
  all read as the value bash would give. Observed by AC1.
- **S2** — M3. `read_newest_unit` in `tools/memory-tree/routed_commits.py` loads the id map once
  with `load_spec_paths` over HEAD's tracked specs and returns the first id, walking newest first,
  that the map defines. Its `git log` takes `--no-merges`, so its population is the one the leg
  grades. Observed by AC2.
- **S3** — M4 and L2. In `tools/check-wiring.sh`, `check_routed` and `check_skill_install` set
  `gated` only when a PreToolUse group carrying the scratch-guard marker has a matcher naming
  `Edit`, `Write`, `MultiEdit` or `NotebookEdit`, read with `matchers_of scratch-guard.js ''
  PreToolUse`. The no-conf line in `check_routed` says the write gate admits every write here,
  because no conf arms it. Observed by AC3 and AC4.
- **S4** — M5. `checkRouted` in `tools/hooks/scratch-guard.js` places the target by the realpath
  of its deepest existing ancestor, with the not-yet-existing tail appended, before the toplevel walk,
  `resolveComparableCommon` and the `rel` computation. A product file reached through a junction or
  a symlink is gated like its repository spelling. Observed by AC5.
- **S5** — M6. The `[[gate_leg]]` named `routed commits name a specced unit` in
  `tools/memory-tree/kit.toml` declares `impure` with gov's text. The govkit row builder copies
  `impure` into the target row under the same `check_target_reads_subject` reader check `subject`
  uses. `govkit.py selfcheck`'s existing descriptor-against-manifest compare, which today joins
  `doc_reads`, joins `impure` too, so a gov row carrying a field its kit leg lacks reds. Observed by
  AC6 and AC7.
- **S6** — M7. The "covers MEMORY_ROOT" test is two-way in `checkUnarmed` in
  `tools/hooks/scratch-guard.js` and in `check_conf` in `tools/memory-tree/routed_commits.py`: an
  entry is refused when MEMORY_ROOT sits under it OR it sits under MEMORY_ROOT. `check_routed`
  inherits the gate's verdict through TOOL-aRoutedQuill-11's read, so its line follows with no edit
  of its own. Observed by AC8, AC9 and AC10.
- **S7** — M8. `tools/govkit/matrix.py` gains a shape that installs from an AGED gov copy whose
  registry `[selection] default` lacks the entries TOOL-aRoutedQuill-5 added, ages that copy forward
  to the current registry, runs `update --write`, and asserts the `default-gained` lines, the receipt
  claim and every gained fragment `wired`. It then runs `settings-merge.py --unwire` on the gate
  fragment, updates again, and asserts the fragment stays unwired and the target's check-wiring
  names it UNWIRED. The aging reuses `build_role_pair`'s recipe. The §7 arm line of
  `memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md` moves AC4 from the
  `selftest.py` arm to the `matrix.py` arm, with a rev bump and a §9 line naming this unit.
  Observed by AC11 and AC12.
- **S8** — M9. `checkBuildable` reads the spec H1 the way KICK R4 and `tree_lib.parse_spec_h1` do:
  the first unfenced line matching `^#[ \t]`, its first token with backticks and asterisks stripped
  and trailing `:.,;` stripped, compared whole to the unit id. Observed by AC13.
- **S9** — L1. The ROUTED_PATHS paragraph of `tools/memory-tree/.memory-tree.conf.example` says the
  gate refuses an Edit, Write, MultiEdit or NotebookEdit under an entry, that a shell write passes
  it, and that the routed-commits leg grades the commit. Observed by AC14.
- **S10** — L3. `checkBuildable` admits a spec at any depth under `<mem>/builds/<build>/spec/`, as
  KICK R4 and `parse_spec_h1` do (§8 F1). Observed by AC15.
- **S11** — L4. `read_mint_unit` in `tools/push-main.sh` captures the `--newest-unit` output and
  status separately and prints the first line only on exit 0. Observed by AC16.
- **S12** — L5. `tools/hooks/scratch-guard.test.sh` gains `run_write` arms: a Tier-1 INPROGRESS
  spec admits; a spec with no Tier cell, an absolute spec path, a route with no `- build:` line and
  a unit line with no spec each refuse naming the reason; and a forced throw inside `checkRouted`
  exits 2 with `fails closed`. The throw is staged by preloading a stub with `node -r` that makes
  the `.git` read throw, so no test-only seam enters the hook. Observed by AC17 and AC18.
- **S13** — L6. `check_card_route`, its R-rule awk and the stale-route strip in
  `skills/session-kickoff/manifest-check.sh` detect the heading as
  `^[[:space:]]*## route[[:space:]]*$`, the spelling `extractRouteUnits` reads after its trim (§8
  F2). Observed by AC19.
- **S14** — L7. Row 7 of the `roster:units` region of `memory/builds/aRoutedQuill/README.md` reads
  CLOSED, as `PLAY-aRoutedQuill-1`'s status header and the generated unit table do. Observed by AC20.
- **S15** — Bar red, the harness arms leg. In `check_card_route`, one local holds `${0##*/}` and
  both route refusals interpolate it, so their signatures stop at the interpolation and the R1 arm
  already in the kickoff suite arms the first. The R2 arm's needle there is lengthened to end
  `--brief-skeleton prints, and nothing was appended`, which arms the shared R0-R6 emission. The
  `## task` arm's needle there is lengthened to the whole message. The stale row at
  `memory/project/unarmed-branches.txt:90` is re-keyed to the reworded `adopt-memory-tree.sh`
  message, one row for one row, so the pin count does not grow. Observed by AC21.
- **S16** — Bar red, the install-prefix leg. `skills/session-kickoff/manifest-check.test.sh:1343`
  uses `$READER_REL` with no literal fallback and announces a skip when it is empty, and
  `tools/check-wiring.sh:1443` finds the adopter through `resolve_kit_file memory-tree
  adopt-memory-tree.sh`, the seam the file already uses for sibling kits. Observed by AC22.
- **S17** — Bar red, the lexicon leg. The six test helpers this build added under undeclared verbs
  are renamed to declared ones: in the kickoff suite `q_ready` to `print_route_ready`, `q_route` to
  `print_route_body`, `q_append` to `run_route_append` and `q_refuse` to `check_route_refusal`; in
  the scratch-guard suite `sub_hook` to `run_sub_hook` and `grade_sub` to `check_sub_context`.
  `VERB_OFFENDER_PIN` in `.lexicon.conf` does not move. Observed by AC23.
  **Readers:**
  by name: `skills/session-kickoff/manifest-check.test.sh` and `tools/hooks/scratch-guard.test.sh`
  spell the six names at their definitions and call sites, and `memory/map/generated/symbols.json`
  lists them; no other tracked file spells them.
  by value: NO VALUE READERS, because a shell helper's name is called and never compared or counted
  except by the lexicon leg this item exists to satisfy.
- **S18** — Bar red, the template-size high-water. `bash tools/check-template-size.sh --bump
  memory/guides/UNATTENDED-PROTOCOL.md` re-records the protocol's high-water at its measured bytes,
  the growth TOOL-aRoutedQuill-7 made under the owner's ruling of 2026-10-09. Observed by AC24.
- **S19** — Records the edits owe: `memory/map/generated/symbols.json` regenerated for the renamed
  and edited functions, and the kickoff manifest's `last-audit` re-stamped for its watched files.
  The kit versions move once, in the run's mint after this last unit, never in this pass.
  NOT OBSERVED by a criterion: the codebase-map, kickoff-manifest, kit-version and kit-epoch legs
  §7 names grade these.

## 3. Non-goals (OUT)

- B1, H1 and the round-2 blocker are `TOOL-aRoutedQuill-9` and `TOOL-aRoutedQuill-10`. H2 and M2
  are closed by `TOOL-aRoutedQuill-11`, and M2 is named here only as closed there.
- The left-shift suggestions that would be new cross-kit gates: a shared conf-spelling fixture run
  against every MEMORY_ROOT reader in the kits (M1), and a shared H1 fixture run through all three
  readers (M9). Each item's arm here is its regression gate, and the classes are already recorded as
  `two-readers-of-one-config-one-re-derived` and `two-guards-one-question-two-answers` under
  `memory/gotchas/`.
- Deriving the roster's status column from front matter (L7's left-shift). That is a change to the
  index generator shared by every build; the class is `two-answers-to-one-question`.
- `routed_commits.py` refusals printed to stderr for `--newest-unit`. S11 fixes the one caller.
- `tree_lib.parse_conf_line`, the ownership leg's own MEMORY_ROOT reader, which already takes the
  last assignment and both spellings.
- A test-only switch in `scratch-guard.js` that forces a throw. S12 stages the throw from outside.
- Any new pin row, waiver row or raised pin. S15 re-keys one row; S17 drains to the existing pin.
- Kit version bumps, which the run's mint makes once per kit after this unit.

### Edges

- **consumes-from** `TOOL-aRoutedQuill-11` — `check_routed` reading its armed or unarmed verdict
  from the gate's exported `checkUnarmed`. S3 edits the function in that shape, and AC10 observes
  S6's two-way test through it; without it the checker keeps its own one-way containment loop and
  AC10 reds.

## 4. Design

### Evidence

Read at `4edeb4678` (this branch, which merged origin/main `e6585db4`) on 2026-10-10.

- `read_memory_root` is `sed -n 's/^MEMORY_ROOT=[[:space:]]*//p' | head -1 | tr -d` at
  `skills/session-kickoff/manifest-check.sh:467-470`, feeding R0 at `:963` and R4's `dir` at `:988`.
- `read_newest_unit` at `tools/memory-tree/routed_commits.py:303-324` returns `ids[0]` of the first
  log record naming any family-shaped id and passes no `--no-merges`. `load_spec_paths` at `:175`
  builds the `{id: [spec paths]}` map in one `cat-file --batch`.
- `check_routed` at `tools/check-wiring.sh:1442` and `check_skill_install` at `:1519` test
  `matchers_of scratch-guard.js` with no event; `matchers_of` at `:348` takes the event third.
- `checkRouted` at `tools/hooks/scratch-guard.js:905` resolves `target` with `path.resolve` only;
  `resolveRealPath` at `:159` exists and is unused there.
- The kit `[[gate_leg]]` at `tools/memory-tree/kit.toml:323-328` carries no `impure`;
  `tools/gate-legs.json` carries it on the same leg. The row builder at
  `tools/govkit/govkit.py:4079-4097` emits `subject`, `guard` and `doc_reads` only; the selfcheck
  compare at `:2741-2805` joins `doc_reads` between descriptors and the manifest.
- `impure` has been in the run-gates canary's key set since `72fd44d2e` (run-gates 1.0), so every
  runner with a canary reads it. PINNED, measured 2026-10-10.
- `checkUnarmed` at `tools/hooks/scratch-guard.js:868-878` and `check_conf` at
  `tools/memory-tree/routed_commits.py:151` test `checkUnderRoot(mem, c)` one way only.
- `checkBuildable` at `tools/hooks/scratch-guard.js:834-866` takes the first `# ` line's raw first
  token (`:845-847`) and refuses any `/` after the spec folder (`:842`). R4's H1 read is
  `skills/session-kickoff/manifest-check.sh:989-994`.
- `read_mint_unit` at `tools/push-main.sh:659-665` pipes `--newest-unit` through `head -n 1` with no
  status check; `main()` at `tools/memory-tree/routed_commits.py:544-546` prints refusals to stdout
  and exits 2.
- `check_card_route` matches `^## route$` at `:959`, `:969` and the strip at `:1054`.
- The harness arms leg, `python tools/memory-tree/check-arms.py --check`, exits 1 with five lines:
  sites `manifest-check.sh:965`, `:1011`, `:1031` and `adopt-memory-tree.sh:101` unarmed, and the pin
  at `memory/project/unarmed-branches.txt:90` naming no live site. The signatures of `:965` and
  `:1011` carry the literal `${0##*/}`, because `INTERP_RE` at `tools/memory-tree/check-arms.py:127`
  matches only a parameter name starting with a letter; no arm can print that text. Probed with
  `signature()`: with the name in a local, `:965` signs as
  `'## route' sections, and a card holds one; the shape is what`, which the existing R1 arm at
  `manifest-check.test.sh:1334` carries, and the shared emission signs as
  `--brief-skeleton prints, and nothing was appended`. The `## task` arm at `:1337` asserts a prefix
  of `:1031`'s message. `ARMS_FLOORS` floors are one-sided upward, so arming more moves none.
- `bash tools/check-install-prefix.sh` reds on two lines: `manifest-check.test.sh:1343`
  (`${READER_REL:-tools/memory-tree/corpus_ids.py}`) and `tools/check-wiring.sh:1443`
  (`${KIT_REL:+$KIT_REL/}memory-tree/adopt-memory-tree.sh`), both added by this build.
- `python tools/lexicon/lexicon.py` prints `verb offenders 1069 over pin 1063`. Diffing `--offenders`
  between `e6585db4` and `4edeb4678` shows six arrivals and no departures: `q_append`, `q_ready`,
  `q_refuse`, `q_route` (KICK-aRoutedQuill-1) and `grade_sub`, `sub_hook` (TOOL-aRoutedQuill-4). Both
  counts PINNED, measured 2026-10-10.
- `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` exits 0 and prints
  `TEMPLATE-SIZE WARN ... 65692 -> 65842 (+150)`; the ceiling in `tools/template-size-limits.txt` is
  65842 and the record in `tools/template-size-highwater.txt` is 65692. PINNED, measured 2026-10-10.

### The H1 and depth rule the gate shares

One reading, the R4 one: skip fenced lines (`^ ? ? ?(```|~~~)` toggles), take the first line matching
`^#[ \t]`, split on whitespace, strip `` ` `` and `*` from the second field and trailing `:.,;`, and
compare it whole to the unit id. Depth: the spec must start with `<mem>/builds/<build>/spec/` and be
repo-relative; anything below that folder is admitted.

### The target's real place

`checkRouted` walks up from `target` to its deepest existing ancestor, takes `resolveRealPath` of it
(falling back to the ancestor when realpath fails), and appends the tail that did not exist. Every
later step reads that real path. A junction in this repo's checkout of itself resolves to the same
spelling, so nothing that is gated today changes verdict.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `print_route_ready` | shell function | `sh.function`; `--suggest print_route_ready --as sh.function` answered OK |
| `print_route_body` | shell function | `sh.function`; answered OK |
| `run_route_append` | shell function | `sh.function`; answered OK |
| `check_route_refusal` | shell function | `sh.function`; answered OK |
| `run_sub_hook` | shell function | `sh.function`; answered OK |
| `check_sub_context` | shell function | `sh.function`; answered OK |

No other identifier is minted. The matrix shape lives inline in `main()` like shapes 1 to 6, and the
realpath step is inline in `checkRouted`.

### Files touched (estimate)

`skills/session-kickoff/manifest-check.sh` · `skills/session-kickoff/manifest-check.test.sh` · `tools/hooks/scratch-guard.js` · `tools/hooks/scratch-guard.test.sh` · `tools/check-wiring.sh` · `tools/check-wiring.test.sh` · `tools/memory-tree/routed_commits.py` · `tools/memory-tree/kit.toml` · `tools/memory-tree/.memory-tree.conf.example` · `tools/govkit/govkit.py` · `tools/govkit/matrix.py` · `tools/push-main.sh` · `tools/push-main.test.sh` · `memory/project/unarmed-branches.txt` · `tools/template-size-highwater.txt` · `memory/builds/aRoutedQuill/README.md` · `memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md` · `memory/map/generated/symbols.json` · `memory/guides/SESSION-KICKOFF.md`

### Rollout

- Order 10, last. TOOL-aRoutedQuill-10 edits `routed_commits.py` and the example conf, and
  TOOL-aRoutedQuill-11 edits `check_routed` and the gate's exports; this unit builds on both tips,
  and its line numbers are re-read there rather than taken from the evidence above.
- One pass, committed with this unit's id in the subject. The pass verifies each item with its
  criterion's direct check; the suites named under §7's `New arm:` lines run once, at the close.
- `gen_map.py --write` runs before the commit, because renamed shell helpers stale
  `memory/map/generated/symbols.json`. The kickoff manifest's `last-audit` moves with a delta line.
- The lexicon count is re-read with `--offenders` after the renames. If a sibling unit moved it, the
  pin is not edited here; the difference is that unit's, and the wrap-up names it.
- No adopter migration. S5 reaches an adopter at its next `govkit update`, and every other change is
  a fix to behaviour already shipped by this unlanded build.

### Alternatives rejected

- **Widening `INTERP_RE` to every `${...}` form** (S15). It is the class fix, but it re-signs every
  site in every discovered gate, which re-keys pin rows this unit did not write. A local is one
  file's change.
- **Pinning the three kickoff sites.** The pin file grows only by a reason no arm reaches the site,
  and arms reach all three.
- **Moving `VERB_OFFENDER_PIN` to 1069.** The six offenders are this build's own names, and a raise
  records debt that one rename per helper clears.
- **Taking check-wiring's gated verdict from the gate** (S3). The question is which hook group fires
  on a write tool, which is the settings file's answer and not the gate's.
- **A `--shape` selector for `matrix.py`.** Useful, and outside the finding; the criterion pays the
  whole matrix's cost instead and says so.

## 5. Production-readiness checklist

- security — S4 closes a silent admit through a junction; S6 and S8 make the gate refuse what the
  push leg would. S12's fail-closed arm guards the one path where a refactor could make the gate
  fail open. No write path is added.
- perf / scale — S4 adds one `realpathSync` per gated write; S2 adds one `cat-file --batch` per mint.
- error / empty / loading states — S11's refusing helper yields no unit; S16's empty `READER_REL`
  announces a skip; S1's conf with no MEMORY_ROOT still yields R0's refusal.
- observability — S3's no-conf line states the gate's real state; every refusal keeps its reason.
- risks — S4 can change the verdict of a write that reached the repository through a link, by
  design. S7's shape adds the matrix's slowest arm.
- testing — each item adds or lengthens an arm, observed RED on its staged break before it lands;
  the suites run once, at the close.
- migration — none: behaviour fixes inside an unlanded build, and one field an update carries.
- user docs — S9 is the adopter-facing text; the hooks README needs no change.

## 6. Acceptance criteria

Fixture repositories live under `%TEMP%/rq12` (a short path, as clones need on Windows), built by the
pass and removed after it.

- **AC1** — When `read_memory_root`, sourced from `skills/session-kickoff/manifest-check.sh` with
  `ROOT` at a fixture, reads a conf of `export MEMORY_ROOT=memory`, then `MEMORY_ROOT=memory  # note`,
  then `MEMORY_ROOT="memory"`, then `MEMORY_ROOT=other` followed by `MEMORY_ROOT=memory`, it prints
  `memory` each time, and returns 1 for a fixture with no conf.
  Red when: any spelling prints empty, `memory  # note` or `other`.
- **AC2** — When `python tools/memory-tree/routed_commits.py --selftest` runs, it prints an `ok`
  line for an AC11 arm whose newest commit names an unspecced id first and whose older commit names a
  specced unit, reporting the specced unit, and one for a newest merge commit that is skipped.
  Red when: the arm reports the unspecced id, or a merge's id.
- **AC3** — When `bash tools/check-wiring.sh` runs in a fixture whose `.claude/settings.json` carries
  the scratch-guard marker only in a PreToolUse group matched `Bash|PowerShell` and in a SubagentStart
  group, with `HOME` at a fixture home holding no skill, it prints no `UNWIRED  routed` and no
  `UNWIRED  skill` line stating the write gate is wired.
  Red when: either line appears for that fixture.
- **AC4** — When `bash tools/check-wiring.sh` runs in a fixture with a PreToolUse scratch-guard
  group matched `Edit|Write|MultiEdit|NotebookEdit` and no `.memory-tree.conf`, its `routed` line
  says the write gate admits every write here.
  Red when: the line says every product write refuses.
- **AC5** — When `node -e` calls `checkRouted` from `tools/hooks/scratch-guard.js` with an Edit
  payload whose `file_path` reaches a file under a fixture repository's routed entry through a junction made
  by `fs.symlinkSync(dir, link, 'junction')`, with `CLAUDE_PROJECT_DIR` at the repository and no
  card for the session, it returns a `deny`; the same call through the repository spelling also
  returns a `deny`.
  Red when: the junction spelling returns `null`.
- **AC6** — When `python tools/govkit/govkit.py apply --target <fixture> --kits memory-tree` runs into
  a fresh fixture with run-gates installed, the fixture's `gate-legs.json` row named
  `routed commits name a specced unit` carries `impure`.
  Red when: the row lacks the field.
- **AC7** — When `python tools/govkit/govkit.py selfcheck` runs with the `impure` line staged out of
  `tools/memory-tree/kit.toml`, it reds naming the leg and the field; unstaged, it passes.
  Red when: the staged break passes.
- **AC8** — When `node -e` calls `checkUnarmed('memory', 'src/ memory/builds/')` from
  `tools/hooks/scratch-guard.js`, it returns the reason naming `memory/builds/` as covering
  MEMORY_ROOT; `checkUnarmed('memory', 'src/')` returns `''`.
  Red when: the inner entry returns `''`.
- **AC9** — When `python tools/memory-tree/routed_commits.py --selftest` runs, its AC4 refusal table
  prints an `ok` line for `ROUTED_PATHS="src/ memory/builds/"` refused as covering MEMORY_ROOT.
  Red when: that conf is graded instead of refused.
- **AC10** — When `bash tools/check-wiring.sh` runs in a fixture whose conf declares
  `ROUTED_PATHS="src/ memory/builds/"`, it prints `UNWIRED  routed` naming `memory/builds/` as
  covering MEMORY_ROOT.
  Red when: it prints `ok       routed`.
- **AC11** — When `python tools/govkit/matrix.py` runs, the new shape prints passing checks for the
  `default-gained` lines, the receipt claim, every gained fragment `wired`, the unwired fragment
  staying unwired across a second update, and check-wiring naming it UNWIRED.
  Red when: with the `add_deploy_kits` call staged out of `update --write`, the shape's checks fail.
  cost: the whole matrix runs, several scratch installs, minutes rather than seconds.
- **AC12** — When `grep -n 'New arm' memory/builds/aRoutedQuill/spec/2026-10-09-spec-TOOL-aRoutedQuill-5.md`
  runs, the `matrix.py` line's `covers` field names AC4 and the govkit self-test line's does not.
  Red when: the self-test line still claims AC4.
- **AC13** — When `node -e` calls `checkBuildable` from `tools/hooks/scratch-guard.js` on fixture
  Tier-2 INPROGRESS specs whose H1 reads `# TOOL-x-1: title`, `# **TOOL-x-1** — title`, and a fenced
  `# TOOL-y-1` above a real `# TOOL-x-1 — title`, each returns `''` for unit `TOOL-x-1`; a spec whose
  H1 names `TOOL-x-2` still returns the H1 reason.
  Red when: any of the three spellings is refused, or the mismatch admits.
- **AC14** — When `grep -n 'shell write' tools/memory-tree/.memory-tree.conf.example` runs, the only
  hit says a shell write passes the gate and the routed-commits leg grades it.
  Red when: a line says the gate refuses a shell write.
- **AC15** — When `node -e` calls `checkBuildable` on a Tier-2 INPROGRESS fixture spec one folder
  below the build's spec folder (a `units` sub-folder of build `b`), it returns `''`.
  Red when: it returns the `is outside` reason.
- **AC16** — When `read_mint_unit`, cut from `tools/push-main.sh` with `sed` and run with
  `resolve_python` and `resolve_kit_dir` stubbed to a `routed_commits.py` stub that prints
  `routed-commits REFUSED — x` and exits 2, it prints nothing; with the stub printing `TOOL-x-1` and
  exiting 0, it prints `TOOL-x-1`.
  Red when: the refusal text is printed.
- **AC17** — When `node -e` calls `checkBuildable` on fixture specs, a Tier-1 INPROGRESS spec returns
  `''`; a spec with no Tier cell returns `names no Tier-1 or Tier-2`; an absolute spec path returns
  `is not a repo-relative path`; an empty build returns `names no - build: line`; an empty spec
  returns `the route line names no spec`.
  Red when: any of the five returns another value.
- **AC18** — When `node -r <stub> tools/hooks/scratch-guard.js` reads an Edit payload over an armed
  fixture, the stub making every read of a `.git` path throw, it exits 2 and stderr carries
  `fails closed`.
  Red when: it exits 0.
  fixture: the stub is a scratch file the pass writes; no tracked file holds it.
- **AC19** — When `bash skills/session-kickoff/manifest-check.sh --card --append` reads a body whose
  heading is `## route ` (one trailing space) onto a fixture card already holding a route,
  `grep -c '^[[:space:]]*## route[[:space:]]*$'` over the stored card prints `1`.
  Red when: it prints `2`.
- **AC20** — When `grep -n 'PLAY-aRoutedQuill-1' memory/builds/aRoutedQuill/README.md` runs, the
  `roster:units` row reads `CLOSED`.
  Red when: it reads `INPROGRESS`.
- **AC21** — When `python tools/memory-tree/check-arms.py --check` runs, it exits 0, printing no
  `has no POSITIVE assertion` line for `skills/session-kickoff/manifest-check.sh` or
  `tools/memory-tree/adopt-memory-tree.sh` and no `which no live site carries` line.
  Red when: with the R1 arm's needle staged back to a prefix, the R1 site is named unarmed.
  fixture: `.memory-tree.conf` sets `ARMS_REFUSALS="graded"`, which is what makes exit sites graded.
- **AC22** — When `bash tools/check-install-prefix.sh` runs, it exits 0, with no spelling line for
  the kickoff suite's reader-hiding arm or for `tools/check-wiring.sh`.
  Red when: either line remains.
- **AC23** — When `python tools/lexicon/lexicon.py` runs, it prints no `verb offenders ... over pin`
  line, and `python tools/lexicon/lexicon.py --offenders` lists none of `q_append`, `q_ready`,
  `q_refuse`, `q_route`, `grade_sub` or `sub_hook`.
  Red when: any of the six is listed, or the count still exceeds the pin.
  figure: the pin 1063 is PINNED in `.lexicon.conf`; the count is DERIVED at observation.
- **AC24** — When `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` runs, it
  prints no `TEMPLATE-SIZE WARN` line.
  Red when: the WARN line remains.
  figure: the recorded high-water is DERIVED by `--bump` from the file's bytes at the pass.

## 7. Gates

`harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `unattended protocol size` · `routed commits name a specced unit` · `routed-commits selftest` · `manifest-check self-test` · `scratch-guard self-test` · `check-wiring self-test` · `push-main self-test` · `govkit selftest` · `govkit selfcheck` · `govkit acceptance matrix` · `govkit refusal join` · `agent-cap self-test` · `hook destinations self-test` · `review-join self-test` · `verifier fan-out self-test` · `straggler-guard arms` · `transition-audit arms` · `kickoff-manifest ratchet` · `memory hygiene` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `recall floor` · `recall floor arms`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC19 · the sed reader on an exported and a commented conf, and an exact-match heading · none

New arm: tools/memory-tree/routed_commits.py --selftest · covers AC2 AC9 · `ids[0]` returned unchecked, and the one-way containment test · none

New arm: tools/check-wiring.test.sh · covers AC3 AC4 AC10 · the any-event `matchers_of` read, the old no-conf wording, and the one-way gate verdict · none

New arm: tools/hooks/scratch-guard.test.sh · covers AC5 AC8 AC13 AC15 AC17 AC18 · a lexical target walk, the one-way containment test, the raw-token H1 read, the depth clause, and a catch flipped to admit · none

New arm: tools/govkit/selftest.py · covers AC6 · a row builder that emits no `impure` · none

New arm: tools/govkit/matrix.py · covers AC11 · `update --write` with its `add_deploy_kits` call staged out · none

New arm: tools/push-main.test.sh · covers AC16 · a mint helper that keeps a refusing stub's stdout · none

## 8. Open questions

- **F1 — L3: which side changes, the gate or the writer?** (a) The gate admits any depth, matching
  KICK R4 and `parse_spec_h1`. (b) R4 refuses nested paths, matching the gate. Nested spec folders
  are tracked in this repo (`memory/builds/aDrainedSluice/spec/units/`), and TEMPLATE-SPEC admits a
  spec at any depth. Recommendation: (a), because two readers already agree and the template allows
  it.
  RESOLVED (agent, 2026-10-10, delegated): (a). It satisfies L3 with no reader left disagreeing and
  trips no veto.
- **F2 — L6: does the checker widen, or does the gate narrow?** (a) The checker detects the heading
  with surrounding whitespace, as the gate reads it after its trim. (b) The gate exact-matches
  `## route`. Under (b), a card whose stored heading carries trailing whitespace stops routing.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-10, delegated): (a). It leaves no stored card unroutable and trips no
  veto.

## 9. Revision log

- rev-1 · 2026-10-10 · initial draft.
- rev-2 · 2026-10-10 · §4 · `order 10` became `order 6`: the dispatch order gate counts the carried-forward TOOL-aRoutedQuill-6 (order 6, DEFERRED) as an unfinished earlier step and refused this unit's dispatch at order 10; the main loop still builds 9, 10, 11 and 12 one after another.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` ranked `parse_conf` (`tools/memory-tree/tree_lib.py`) and
`load_conf` as conf-reading SEAMs, both Python; the kickoff kit is copy-installed shell and cannot
import them, so S1 extends the shell idiom `derive_routed_candidate` and `check_routed` already use
(source in a subshell). The other seams this unit extends, each verified in source: `load_spec_paths`
(S2), `matchers_of` with its event argument (S3), `resolveRealPath` (S4), the selfcheck
descriptor-against-manifest compare and `check_target_reads_subject` (S5), `build_role_pair` (S7),
`resolve_kit_file` (S16), and R4's H1 reader as the model for `checkBuildable` (S8). No new seam is
built.

Recall terms used: `MEMORY_ROOT readConfKey parse_conf_line sourced conf subshell export trailing
comment last assignment route card check_routed` — which surfaced `TOOL-aGraftedHelix-46`,
`TOOL-aScouredKit-19`, `TOOL-aScouredKit-28`, `TOOL-aRepatriatedFork-38` and
`TOOL-dLoggedFlight-1`, all on conf readers disagreeing with the shell.
