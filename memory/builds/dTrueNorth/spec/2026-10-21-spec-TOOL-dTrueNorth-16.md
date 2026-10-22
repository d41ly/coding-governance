# TOOL-dTrueNorth-16 — the round-1 spec audit's 37 minors: one key rule, one revision reader, one conf read, honest exits and the docs that name them

**Status:** CLOSED · rev-4 · 2026-10-22 · node d · Tier-2 · base 271aa59d · streams tooling · order 5

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-21-build-TOOL-dTrueNorth-16-deviation-15.md](../build/2026-10-21-build-TOOL-dTrueNorth-16-deviation-15.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-16-deviation-5.md](../build/2026-10-21-build-TOOL-dTrueNorth-16-deviation-5.md) | deviation | — |
| [2026-10-21-build-TOOL-dTrueNorth-16-ledger.md](../build/2026-10-21-build-TOOL-dTrueNorth-16-ledger.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-16-build-brief.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-16-build-brief.md) | journal | — |
| [2026-10-21-prompt-TOOL-dTrueNorth-16-deviation-5.md](../prompts/2026-10-21-prompt-TOOL-dTrueNorth-16-deviation-5.md) | research | — |
| [2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md](../reviews/2026-10-21-review-TOOL-dTrueNorth-8-spec-audit.md) | spec-audit | TOOL-dTrueNorth-8 TOOL-dTrueNorth-9 TOOL-dTrueNorth-10 TOOL-dTrueNorth-11 TOOL-dTrueNorth-12 TOOL-dTrueNorth-13 TOOL-dTrueNorth-14 TOOL-dTrueNorth-15 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build (`memory/builds/dTrueNorth/reviews/2026-10-21-review-TOOL-dTrueNorth-1-spec-audit.md`)
exited CONVERGED with 45 confirmed findings. Its 8 highs are units 8 to 15. This unit is the batch
BUILD-METHOD M4 makes of the rest: every MEDIUM and every LOW, each by its report id, each its own
item in §2. Where the report merged ids into one item, each id still has its own scope item here.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| M1 | MEDIUM | 2 | S1 |
| M2 | MEDIUM | 3 | S2 |
| M3 | MEDIUM | 4, 13 | S3, S4 |
| M4 | MEDIUM | 5, 23, 43 | S5, S6, S7 |
| M5 | MEDIUM | 6 | S8 |
| M6 | MEDIUM | 14 | S9 |
| M7 | MEDIUM | 15 | S10 |
| M8 | MEDIUM | 19 | S11 |
| M9 | MEDIUM | 20 | S12 |
| M10 | MEDIUM | 21 | S13 |
| M11 | MEDIUM | 22 | S14 |
| M12 | MEDIUM | 27 | S15 |
| M13 | MEDIUM | 29 | S16 |
| M14 | MEDIUM | 31 | S17 |
| M15 | MEDIUM | 32 | S18 |
| M16 | MEDIUM | 42 | S19 |
| M17 | MEDIUM | 44 | S20 |
| M18 | MEDIUM | 45 | S21 |
| M19 | MEDIUM | 46 | S22 |
| M20 | MEDIUM | 47 | S23 |
| L1 | LOW | 8, 26 | S24, S25 |
| L2 | LOW | 10 | S26 |
| L3 | LOW | 16 | S27 |
| L4 | LOW | 17, 35 | S28, S29 |
| L5 | LOW | 18 | S30 |
| L6 | LOW | 24 | S31 |
| L7 | LOW | 25 | S32 |
| L8 | LOW | 33 | S33 |
| L9 | LOW | 34 | S34 |
| L10 | LOW | 36 | S35 |
| L11 | LOW | 37 | S36 |
| L12 | LOW | 38 | S37 |

That is 23 MEDIUM and 14 LOW by raw id. Most land on units 1 to 6's code; a few restate a frozen
spec's criterion as the observation it should have named, which this pass makes.

## 2. Scope (IN)

- **S1** — id 2. Deviation-2 and deviation-3 are written by `TOOL-dTrueNorth-10` at kind `deviation`
  from their first commit, so `TOOL-dTrueNorth-4` §4 Migration's upgrade step has no file to act on
  and `TOOL-dTrueNorth-7` §4 Rollout step 4's "was written with this spec" is superseded by that unit.
  This item observes the tree that reading claims. Observed by AC1.
- **S2** — id 3. `--dispatch` in `tools/unattended/unattended.sh` gains a refusal beside its order
  gate: a unit whose spec's §3 Edges consumes from a unit of the same build, read by
  `read_consumes_from` (`tools/unattended/lib-unattended.sh:327`), is refused with code 49 while that
  producer's spec is neither `CLOSED` nor `WONTDO`, naming both units and the edge. The orders this
  build's units carry stand; the refusal is what makes an order that ties a consumer to its producer
  unable to dispatch the consumer first. Settled at rung 5 (§8 F3), so this pass also writes
  deviation-5, byte for byte from §4 "Deviation-5". Observed by AC2 and AC38.
- **S3** — id 4. The parity probe `TOOL-dTrueNorth-2` §4 Fixtures describes hands `carries.py`'s
  `fixture()` builds adapted to its shape: each `(text, hash8, since)` of `read_design` becomes
  `(text, hash8, extract_clause_tokens(text))`, and `scan_carries` takes the `read_design` value
  itself. The `token` plant is re-observed with a liveness assertion: the planted token is one of the
  clause's own tokens, and the plant returns a `token` finding naming it. Observed by AC3.
- **S4** — id 13. The same adapter re-observes the `moved-token` plant (`TOOL-dTrueNorth-2` AC9), with
  the liveness assertion that its `token` finding is read from the receiving build's carrier.
  Observed by AC4.
- **S5** — id 5. One off rule for the `DESIGN_*` keys, in `tools/memory-tree/design_lib.py`:
  `read_design_keys(root, conf)` returns None when all four of `DESIGN_RECORD`, `DESIGN_BASELINE`,
  `DESIGN_VIEW` and `DESIGN_NODES` are blank or absent; raises `DesignRefusal` naming each blank key
  when some are set and some are not; and otherwise returns the validated values, `DESIGN_BASELINE`
  resolved to a commit or refused by name. `read_design` builds on it. `deviation_join.py` takes its
  off and partial states from it, superseding `TOOL-dTrueNorth-4` S8's "the three S2 keys" and its
  AC12's single blank key. Observed by AC5.
- **S6** — id 23. `asbuilt_view.py` and its host in `gen_build_index.py` take their off and partial
  states from `read_design_keys` too, superseding `TOOL-dTrueNorth-6` S7's "any S2 key blank", so no
  reader of the keys hand-rolls them. Observed by AC6.
- **S7** — id 43. How `SPEC_CARRIES_CUTOFF` combines with S5's rule, stated once in `design_lib.py`'s
  docstring and applied by the carries join and the coverage read: the cutoff blank is off whatever
  the design keys hold; the cutoff set with every design key blank is a refusal naming the cutoff and
  the keys; the cutoff set with a partial set is S5's refusal. `TOOL-dTrueNorth-6` AC10's off case is
  observed with all four `DESIGN_*` keys and the cutoff blank. Observed by AC7.
- **S8** — id 6. `TOOL-dTrueNorth-3` AC6, AC7 and AC9 are observed without the hygiene engine, which
  is a gate leg no role agent runs: AC6 and AC7 through `gen_build_index.py --check-coverage`'s exit
  and lines over the same plant, AC9 through check 6's pricing awk run directly
  (`tools/memory-tree/check-memory-hygiene.sh:1018-1025`). The engine's own verdict stays with the
  `New arm:` lines unit 3 declares. Observed by AC8.
- **S9** — id 14. The `WONTDO` filter's one home is `read_carries_specs`, as `TOOL-dTrueNorth-2` S1
  places it. `scan_carries` parses no status; a status read there, if unit 2's pass wrote one, moves
  to `read_carries_specs`. `TOOL-dTrueNorth-2` AC11's `WONTDO` half is observed through
  `read_carries_specs` then `scan_carries`. Observed by AC9.
- **S10** — id 15. The revision read is bytes: S12's reader takes `git cat-file --batch`'s stream
  undecoded, slices each body by its header's byte size, and decodes each blob as UTF-8 with CRLF
  folded, the discipline `read_blobs_at_rev` documents (`tools/memory-tree/gen_build_index.py:2934-2943`).
  Observed by AC10.
- **S11** — id 19. `read_carries_specs` takes each spec's status from `gen_build_index.parse_spec_text`
  (`tools/memory-tree/gen_build_index.py:490`), loaded by path from the kit beside the checker, so the
  carries join and the units table read one header grammar. A spec whose header does not parse is set
  apart under its own skip reason, `unparsed`, and counted. Observed by AC11.
- **S12** — id 20. One revision reader for one population: `read_spec_revisions(root, paths)` in
  `design_lib.py` returns `{path: [(sha, before, after)]}`, oldest first, one entry per non-merge
  commit that changed the path, `before` the text at its first parent or None at creation, from one
  `git log --full-history --no-merges --no-renames --date-order --reverse` and one
  `git cat-file --batch`. `read_carries_specs` and `deviation_join.read_population` both call it,
  superseding `TOOL-dTrueNorth-2` §4 "Revisions" and `TOOL-dTrueNorth-4`'s per-path port of the
  instrument's reader. Observed by AC12.
- **S13** — id 21. The first-pass rule keeps the trailer-replaces-subject reading the instrument's
  `read_first_pass` uses, and is named for what it is: `deviation_join.py`'s docstring and its kit
  README row call it the unattended driver's pass rule (`read_attribution_tokens`, `pass_commit`) and
  say it deliberately differs from the union `routed_commits.py` attributes by
  (`tools/memory-tree/routed_commits.py:22-25`). A `subject-trailer` plant credits a commit whose
  subject names X and whose trailer names Y to Y alone. Observed by AC13.
- **S14** — id 22. One read of the conf for the carries keys: `read_design_conf(root)` in
  `design_lib.py` parses `.memory-tree.conf` with `tree_lib.parse_conf`, and
  `derive_carries_coverage(root, files=None, conf=None)` reads `SPEC_CARRIES_CUTOFF` and the
  `DESIGN_*` keys from the conf its caller passes or from that parse. The ISO-date test is
  `check_cutoff_value(key, value)`, the body of `read_cutoff_key` (`tools/check-spec-tokens.py:650-670`)
  factored out, which `read_cutoff_key` calls unchanged for every other key. `gen_build_index.py`
  passes its parsed conf. Observed by AC14.
- **S15** — id 27. The reader's side of `_expand_ids`' contract: `backlog.read_header_verbs`'s
  docstring names `expand(value) -> (ids, bad)`, and a return that is not a pair raises
  `backlog.Problem` naming the contract and the spec path, so a stranded caller is a named refusal
  rather than a bare `ValueError`. Observed by AC15.
- **S16** — id 29. `read_carries_coverage(root, conf, resolve=None)`: an injected `resolve` supplies
  the coverage function, the shape `read_landed_unclosed` takes
  (`tools/memory-tree/gen_build_index.py:1678`), and the generator's self-test passes a stub, so its
  check-29 and region arms run in an adopter that holds no checker. The hygiene suite's check-29 arms
  print a named SKIP when `check-spec-tokens.py` is not beside the kit. Observed by AC16.
- **S17** — id 31. As-built verdicts get a verb of their own. `gen_build_index.py --check` reports
  only the view's byte drift, under its `--write` remedy; `--check-asbuilt`, `cmd_check_asbuilt`,
  prints `TOOL-dTrueNorth-6` S4's other findings under `as-built VERDICT` and exits 1, 0 off with one
  line, 2 on an unreadable pin; under `--staged` it runs when a staged path is a deviation record,
  `DESIGN_RECORD`, `DESIGN_VIEW` or the conf, else prints one held line. Hygiene check 30 delegates to
  it as check 29 delegates, with its catalogue entry in `tools/memory-tree/HYGIENE.template.md`
  rendered into `memory/HYGIENE.md`. Check 9's drift message and the runner's regeneration check then
  read only what `--write` cures. This supersedes `TOOL-dTrueNorth-6` S5's verdict exit on `--check`
  and the verdict half of its AC8. Observed by AC17.
- **S18** — id 32. The view is a declared generated output: `GENERATED_INDEXES` in `.unattended.conf`
  gains two pairs, the view with `tools/memory-tree/gen_build_index.py` and the view with
  `tools/memory-tree/asbuilt_view.py`, so a pass that re-renders it stages it without declaring it,
  and a pass may not write it beside a sibling writing either generator. Observed by AC18.
- **S19** — id 42. `asbuilt_view.py`'s fixture builds its design in its scratch repository, as
  `TOOL-dTrueNorth-12` S3 makes the deviation fixture do; at this second instance the builder moves
  into `design_lib.py` as `write_design_fixture(repo)`, which both fixtures call. Each of
  `TOOL-dTrueNorth-6`'s plants reads its clause from that design. Observed by AC19.
- **S20** — id 44. One `--write` reaches a fixed point: `cmd_write` renders and writes `DESIGN_VIEW`
  before it calls `plan()`, so the coverage regions read the view just written. A view verdict still
  blocks no write, as `TOOL-dTrueNorth-6` §4 "The host" requires. Observed by AC20.
- **S21** — id 45. Check 29's staged trigger is the render's: `gen_build_index.py --check-coverage
  --staged` runs when any staged path satisfies `check_index_input` (`:831-857`) or is
  `check-spec-tokens.py` beside the kit, and prints the held line otherwise; check 29 passes
  `--staged` through instead of testing paths itself. Observed by AC21.
- **S22** — id 46. A pipe in `**After:**`: `read_record` lists a record whose `**After:**` holds a `|`
  as malformed, naming the field and the table cell the pipe would split; `asbuilt_view.py` renders
  that clause's baseline row and reports the record as a finding. A `pipe-after` plant joins both
  fixtures. Observed by AC22.
- **S23** — id 47. Each "nothing measured" cause exits 2 on its own: a declared `DESIGN_BASELINE`
  naming no commit, whatever the specs; and a readable pin with no chain-build spec. The
  `unmeasured-pin` and `unmeasured-specs` plants each exit 2 under both policies naming their reason,
  superseding `TOOL-dTrueNorth-4` S8's conjunction. Observed by AC23.
- **S24** — id 8. `TOOL-dTrueNorth-2` AC17 is observed by a command that is red at base: the module
  header, `sed -n 1,162p tools/check-spec-tokens.py`, grepped for `SPEC_CARRIES_CUTOFF` and for
  `carries join`. Observed by AC24.
- **S25** — id 26. Each of the three things AC17 names is asserted by its own grep of that header:
  the population, the key, and the two limits, the semantic blind side and the rename. Observed by
  AC25.
- **S26** — id 10. Two halves. `TOOL-dTrueNorth-3` AC10 is observed on item 9 too, in both copies of
  the catalogue. And `read_carries_coverage`'s docstring says why the join sits outside the kit: the
  grammar and the population are `design_lib.py`'s, inside it; the join is gov's checker, reached by
  path only under a set key and never shipped; and the self-test injects a stub (S16).
  Observed by AC26.
- **S27** — id 16. `VIEW_HEAD` holds the literal `**Serves:** research PLAY-dClosedLoop-1` line, as
  the instrument holds it (`asbuilt.py:75`), in place of v2's first Serves line, so the view's bytes
  cannot move with an edit to v2. Observed by AC27.
- **S28** — id 17. The three homes that say `--print-bindings` "always exits 0", `memory/HYGIENE.md:589`,
  `tools/memory-tree/HYGIENE.template.md:589` and the docstring at
  `tools/memory-tree/gen_build_index.py:701`, name its exit 2 on a malformed cutoff and its `P` and
  `Q` rows, the `Q` row in the four-field shape `TOOL-dTrueNorth-14` gives it, graded, cutoff and
  exempt. Observed by AC28.
- **S29** — id 35. `tools/memory-tree/kit.toml` gains three `[[contract.clause]]` rows under
  `memory-tree/gen-build-index`, consumer `check-memory-hygiene.sh`: `--print-bindings` expecting
  `(?m)^Q\t`, `--check-coverage` expecting `(?m)^build-index: coverage`, and `--check-asbuilt`
  expecting `(?m)^(build-index: as-built|as-built view: off)`. Observed by AC29.
- **S30** — id 18. `TOOL-dTrueNorth-3` AC2's comparison strips the `memory/builds/<slug>/` prefix and
  the backticks from the derived-spec field before it compares the region with `carries.py --report`,
  which prints that path repo-relative (`carries.py:311`). Observed by AC30.
- **S31** — id 24. `check_view` matches rows with `design_lib.VIEW_ROW`, imported, never a second copy
  of `asbuilt.py:33`'s grammar. Observed by AC31.
- **S32** — id 25. One spec filename date pattern: `SPEC_FILE_DATE` in `design_lib.py` is the
  checker's pattern, `/([0-9]{4}-[0-9]{2}-[0-9]{2})-spec-`; `scan_chain_specs` builds on it and on
  `tree_lib.build_spec_path_re` (`tools/memory-tree/tree_lib.py:197-200`); and the checker's `SPEC_DATE`
  is bound to it. Observed by AC32.
- **S33** — id 33. `TOOL-dTrueNorth-1` AC6 is observed with the `since` cells the records make true:
  `baseline` for `cl-dClosedLoop-0001`, `-0003`, `-0005` and `-0006`; deviation-3 for
  `cl-dClosedLoop-0002`; deviation-4 for `cl-dClosedLoop-0004`. Observed by AC33.
- **S34** — id 34. `DELEGATES` in `tools/memory-tree/check-verdict-epoch.sh:184` gains
  `${_kit}design_lib.py`, `${_kit}asbuilt_view.py` and `${_kit}../check-spec-tokens.py`, the modules
  checks 29 and 30 run; its `[ -f ]` guard passes over one that is absent. Observed by AC34.
- **S35** — id 36. The three hand-offs with no owner are filed as ask rows, each with its `SEV` row,
  in `memory/builds/dClosedLoop/BACKLOG.md`, the texts under §4 "The asks": the pin-aware
  `specs-audited` term, the binding grammar's template section, and `check_prompt_brief`'s route
  through `read_roster_at`. Observed by AC35.
- **S36** — id 37. `memory/map/features/build-readme-surface.md` names four generated regions in its
  title, its region paragraph and its seam line, and says `--check` demands the coverage pair on a
  chain build's README; `tools/memory-tree/README.md:18` gives the check count the catalogue holds
  after this unit, 30, with 29 and 30 delegated to `gen_build_index.py`. Observed by AC36.
- **S37** — id 38. The rollout wording: the kit README rows for `deviation_join.py` and
  `asbuilt_view.py`, and `design_lib.py`'s docstring, say the `DESIGN_*` keys are gov's, absent from
  the example conf, so an adopter's engines read them as off. Observed by AC37.

## 3. Non-goals (OUT)

- The eight highs: units 8 to 15, each its own unit. Where a minor here shares a defect with one of
  them, ids 2, 27, 32, 33 and 42, the high's unit owns the mechanism it names and this item owns only
  what §2 states.
- Editing the frozen specs of units 1 to 7. A criterion this unit restates is superseded here and
  observed by this unit's pass.
- Renumbering any unit's order: S2 makes the order gate's blind spot a refusal instead.
- The unattended verbs carrier. `memory/guides/UNATTENDED-VERBS.md` does not enumerate `--dispatch`'s
  gates, the order gate included, and the refusal's own message names its cause.
- The VERBS and STOPS carriers of `TOOL-dTrueNorth-7`, and its suites' verdict, which README rule 8
  waives at this landing.
- This unit's departure record as an added unit: deviation-5, whose follow-through is this unit, is
  the record its `rescope · item add` row joins.

### Edges

- **consumes-from** `TOOL-dTrueNorth-1` — `design_lib.py`, its `read_design`, `read_design_view`, `VIEW_ROW` and `scan_chain_specs`; S5, S7, S12, S14, S19, S31, S32 and S33 extend or observe them
- **consumes-from** `TOOL-dTrueNorth-2` — the carries join, `read_carries_specs`, `scan_carries` and `derive_carries_coverage` in `tools/check-spec-tokens.py`; S3, S4, S9 to S12, S14, S24 and S25 extend or observe them
- **consumes-from** `TOOL-dTrueNorth-3` — `read_carries_coverage`, `cmd_check_coverage` and hygiene check 29; S8, S16, S20, S21, S26, S30 and S36 extend or observe them
- **consumes-from** `TOOL-dTrueNorth-4` — `deviation_join.py`, `read_record` and the population; S5, S12, S13, S22 and S23 extend them
- **consumes-from** `TOOL-dTrueNorth-5` — `cmd_print_bindings`' `P` and `Q` rows; S28 and S29 document and contract them
- **consumes-from** `TOOL-dTrueNorth-6` — `asbuilt_view.py`, `check_view`, `VIEW_HEAD` and the host in `gen_build_index.py`; S6, S17, S19, S20, S22, S27 and S31 extend them
- **consumes-from** `TOOL-dTrueNorth-10` — deviation-2 and deviation-3 in the tree; S1 and S33 observe them
- **consumes-from** `TOOL-dTrueNorth-12` — `build_design_fixture`, which S19 moves into `design_lib.py` at its second instance
- **consumes-from** `TOOL-dTrueNorth-14` — the `Q` row's four-field shape, which S28 and S29 spell
- **hands-off** `TOOL-dTrueNorth-20` — the round-2 spec audit's minors on this spec, ids 2, 3, 4, 6, 7, 9, 16, 23, 28, 30 to 32 and 39 to 43

## 4. Design

### Why one unit and not two

M6's clause 2 refuses a split where one half writes a file the other reads as a contract. The two
write sets that would otherwise separate, the checker and `design_lib.py` on one side and the
generator, the hygiene engine and the docs on the other, are joined by contracts both read:
`gen_build_index.py` loads `derive_carries_coverage` (S14, S16) and `design_lib.py` (S5, S20), and
the docs spell rows the code prints (S28, S29). So the minors are one unit.

### The key rule (S5 to S7)

| `SPEC_CARRIES_CUTOFF` | `DESIGN_*` keys | carries join and coverage | deviation join and as-built view |
|---|---|---|---|
| blank | any | off, one line | off if all four blank, refusal if partial, armed if all set |
| set | all blank | refusal naming the cutoff and the keys | off, one line |
| set | partial | refusal naming each blank key | refusal naming each blank key |
| set | all set | armed | armed |

### The revision reader (S10, S12)

```python
def read_spec_revisions(root, paths) -> dict:
    """{path: [(sha, before, after)]}, oldest first. Two spawns: one git log, one cat-file --batch.
    Bytes in, UTF-8 out per blob, CRLF folded; `before` is the first parent's text, None at creation."""
```

### The dispatch refusal (S2)

Read at base: the order gate is `tools/unattended/unattended.sh:13510-13553`, and it blocks only on a
unit at an earlier order that is neither terminal nor dispatched. The edge refusal runs after it,
over `read_consumes_from` of the dispatched unit's spec, skipping an id that is not a unit of the
build (`unit_ids_of`), and blocks while the producer's status, read as the order gate reads it, is
neither `CLOSED` nor `WONTDO`. A dispatched but unbuilt producer still blocks: a consumer needs the
producer's code, not its dispatch row.

### Deviation-5

`memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-16-deviation-5.md`, written in
this unit's pass, the commit re-rendering the view as `TOOL-dTrueNorth-8` S1 requires, byte for byte
from the fenced block of `memory/builds/dTrueNorth/prompts/2026-10-21-prompt-TOOL-dTrueNorth-16-deviation-5.md`.

### The asks (S35)

Each id is the next `PLAY-dClosedLoop-<n>` above every one the tree spells at the pass's base, taken
in this order, and each row's date is the pass's.

```markdown
- PLAY-dClosedLoop-<n> · filed <date> · THE SPECS-AUDITED TERM IS NOT PIN-AWARE. TOOL-dTrueNorth-5 pins each spec-audit record's revisions as @rev-N, and the unattended driver's specs-audited term at --close still joins any spec-audit record naming a unit, so a spec revised past its pin closes as audited; TOOL-dTrueNorth-5 §8 F3 left it out because the driver was TOOL-dTrueNorth-7's alone in that build. · accept --close's specs-audited term reads a unit as audited only when a spec-audit record pins its current header revision, seen red on a planted revision past the pin
- PLAY-dClosedLoop-<n+1> · filed <date> · THE BINDING-LINE GRAMMAR HAS NO TEMPLATE HOME. TOOL-dTrueNorth-1 states the grammar of the Carries, Derived, Moved, Retired and Deferred lines in design_lib.py's docstring and the conf comment, and memory/TEMPLATE-SPEC.md names none of them, so a chain spec writer learns it from a refusal. · accept memory/TEMPLATE-SPEC.md and its kit template carry a section stating the five binding keys' grammar and pointing at design_lib.py as its one parser
- PLAY-dClosedLoop-<n+2> · filed <date> · THE PROMPT-MODE BRIEF CHECK READS THE AUTHORED ROSTER ITS OWN WAY. TOOL-dTrueNorth-7 adds read_roster_at, the one reader of a build README's authored roster pair at a commit, and check_prompt_brief in the unattended driver reads the same pair without it; TOOL-dTrueNorth-7 §8 F7 left the route out because PLAY-dClosedLoop-2 does not cover a prompt-mode preflight carrier change. · accept check_prompt_brief reads the authored roster through read_roster_at, its verdict unchanged on every case of its suite
- SEV · PLAY-dClosedLoop-<n> · LOW · a spec revised after its audit closes as audited at --close, while the build index's past-pin line still names it
- SEV · PLAY-dClosedLoop-<n+1> · LOW · a chain spec writer meets the binding grammar as a refusal rather than in the format
- SEV · PLAY-dClosedLoop-<n+2> · LOW · two readers of one roster pair can disagree on a malformed pair
```

The three ask rows go under `## Asks` and the three `SEV` rows under `## Dispositions`.

### Inventory

| Identifier | Kind | Lexicon cell |
|---|---|---|
| `read_design_keys` | function, `design_lib.py` | `py.function`, OK |
| `read_design_conf` | function, `design_lib.py` | `py.function`, OK |
| `read_spec_revisions` | function, `design_lib.py` | `py.function`, OK |
| `write_design_fixture` | function, `design_lib.py` | `py.function`, OK |
| `SPEC_FILE_DATE` | compiled pattern, `design_lib.py` | none |
| `check_cutoff_value` | function, `tools/check-spec-tokens.py` | `py.function`, OK |
| `cmd_check_asbuilt`, `--check-asbuilt` | function and verb, `gen_build_index.py` | `py.function`, OK |
| check 30 | hygiene check | `check-memory-hygiene.sh`, `HYGIENE.template.md` |
| `subject-trailer`, `pipe-after`, `unmeasured-pin`, `unmeasured-specs` | fixture plants | none |

### Files touched (estimate)

- `tools/memory-tree/design_lib.py`
- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/asbuilt_view.py`
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/check-verdict-epoch.sh`
- `tools/memory-tree/HYGIENE.template.md`
- `memory/HYGIENE.md`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/README.md`
- `memory/map/features/build-readme-surface.md`
- `.unattended.conf`
- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/builds/dClosedLoop/BACKLOG.md`
- `memory/builds/dTrueNorth/build/2026-10-21-build-TOOL-dTrueNorth-16-deviation-5.md` (new)
- `memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-as-built.md` (re-rendered by `--write`, never edited)

### Alternatives rejected

- **For S2, a `gen_build_index.py --check` Problem for two same-order units joined by an edge.** It
  is a third parse of the edge grammar, beside the hygiene engine's and `read_consumes_from`, and it
  reports at the next check rather than refusing the act.
- **For S17, amending check 9's message and the runner's regeneration check to tell a verdict from
  drift.** Two consumers would each learn a second meaning of one exit, and `--write` would still be
  printed as the remedy for a finding it cannot cure.
- **For S22, escaping the pipe in the view and unescaping it before the hash.** The view's bytes would
  then differ from the clause text they render, and every reader of the table would owe the unescape.

## 5. Production-readiness checklist

- security — S2 adds a refusal, never a write; S5 refuses a partial key set; S18 narrows a pass's
  declarable paths. No new input crosses a trust boundary.
- perf / scale — S12 reads revisions in two spawns, not two per revision.
- error / empty / loading states — each off state is one line, a partial state a refusal naming its keys, and
  each "nothing measured" cause exits 2 (S5, S7, S23).
- observability — check 30's verdicts, S16's SKIP lines, S2's refusal naming the edge.
- risks — S2 stops a consumer whose edges and orders disagree; S17 moves the as-built
  verdicts from check 9 to check 30, which every full run carries.
- testing — AC1 to AC38 by probe and fixture; the arms under §7.
- migration — none: all additive.
- user docs — `memory/HYGIENE.md` items 9 and 30, the kit README, the build-README dossier.

## 6. Acceptance criteria

Every command runs from the repository root. A scratch clone is under a short `%TEMP%` path.

- **AC1** — When `git log --diff-filter=A --format=%s -- 'memory/builds/dTrueNorth/build/*-deviation-2.md' 'memory/builds/dTrueNorth/build/*-deviation-3.md'`
  runs, it prints subjects naming `TOOL-dTrueNorth-10`, and `git grep -h '^\*\*Serves:\*\*' -- 'memory/builds/*/build/*-deviation-*.md'`
  prints kind `deviation` on every line.
  Red when: either record entered the tree under another kind and rests on unit 4's upgrade step.
- **AC2** — When a scratch repository holds a build of two units at one order, the second's spec
  declaring `consumes-from` the first and both `OPEN`, `unattended.sh --dispatch` for the second
  exits 49 naming both units and the edge; with the first's spec `CLOSED` it proceeds.
  Red when: the consumer is dispatched while its producer is open.
  cost: minutes, for a preflight fixture built the way `TOOL-dTrueNorth-7`'s FX fixtures are.
  fixture: a scratch repository under a short `%TEMP%` path; the tree holds none.
- **AC3** — When the parity probe hands `scan_carries` the `token` plant through S3's adapter, it
  returns a `token` finding naming a token that `extract_clause_tokens` finds in the planted clause.
  Red when: the planted token is a single character of the `since` cell, or no `token` finding returns.
- **AC4** — When the probe hands it the `moved-token` plant, the `token` finding names the receiving
  build's carrier and a token of the moved clause.
  Red when: the plant iterates a string's characters, or the finding is read from the owner's folder.
- **AC5** — When `python3 "tools/memory-tree/deviation_join.py"` runs in a scratch clone whose conf blanks
  all four `DESIGN_*` keys, it prints one off line and exits 0; with `DESIGN_VIEW` alone blank it exits
  2 naming `DESIGN_VIEW`.
  Red when: a partial key set reads as off.
- **AC6** — When `python3 "tools/memory-tree/asbuilt_view.py" --check` runs in that clone with all four
  keys blank, it prints `as-built view: off` and exits 0; with `DESIGN_NODES` alone blank it exits 2
  naming `DESIGN_NODES`.
  Red when: the generator counts three keys, so a blank `DESIGN_NODES` reads as armed.
- **AC7** — When `python3 tools/memory-tree/gen_build_index.py --check` runs in a scratch clone whose conf
  blanks the four `DESIGN_*` keys and `SPEC_CARRIES_CUTOFF`, it prints the as-built off line, the
  coverage off line and no Problem; with only the four keys blank and the cutoff set it names a
  Problem naming `SPEC_CARRIES_CUTOFF` and the keys.
  Red when: a set cutoff over a blank design reads as off.
- **AC8** — When `python3 tools/memory-tree/gen_build_index.py --check-coverage` runs in a scratch clone
  with `TOOL-dTrueNorth-1`'s header at `INPROGRESS` and `TOOL-dTrueNorth-3` AC6's planted view row, it
  exits 1 naming that spec and `uncarried cl-dClosedLoop-0599`, and exits 0 with the row taken out or
  every spec `OPEN`; check 6's pricing awk, cut from `tools/memory-tree/check-memory-hygiene.sh` and run
  over the padded README `TOOL-dTrueNorth-3` AC9 describes, bills the coverage region to the generated
  half.
  Red when: an `INPROGRESS` spec passes over a red build, or the region is priced as authored.
- **AC9** — When a probe runs `read_carries_specs` over a scratch clone holding a second whole carrier
  of one clause whose header reads `WONTDO`, then `scan_carries` over the result, no `ambiguous`
  finding names the clause and `skipped` counts one `wontdo`.
  Red when: the `WONTDO` carrier reaches `scan_carries`.
- **AC10** — When a probe calls `read_spec_revisions` over a scratch repository whose spec has two
  revisions, the first holding a multi-byte character before the second's changed line, the second
  revision's `after` equals `git show <sha>:<path>` decoded as UTF-8.
  Red when: the stream is decoded before it is sliced, so the second blob is cut short.
- **AC11** — When `read_carries_specs` reads a scratch spec whose status header misses its `base`
  field, it sets the spec apart under `unparsed`, and `parse_spec_text` returns None for the same text.
  Red when: the join reads a status the units table does not.
- **AC12** — When a probe calls `read_carries_specs` and `deviation_join.read_population` over one
  scratch repository, both see the same revision list for each chain spec, and the reader makes two
  git spawns whatever the revision count.
  Red when: the two arms disagree on which revisions a spec has.
- **AC13** — When `python3 "tools/memory-tree/deviation_join.py" --fixture --plant subject-trailer --policy refuse`
  runs, the commit naming X in its subject and Y in its trailer is the first pass of Y and of no X.
  Red when: the arm credits X, the union rule its docstring does not name.
- **AC14** — When a scratch clone's conf declares `SPEC_CARRIES_CUTOFF` twice, and separately as
  `export SPEC_CARRIES_CUTOFF=…`, the carries join's report line and `gen_build_index.py --check-coverage`
  report the same state and the same date in each case.
  Red when: one reader takes the first declaration and the other the last.
- **AC15** — When a probe calls `backlog.read_header_verbs` on a header carrying `closes` with an
  `expand` stub returning three values, it raises `backlog.Problem` naming `(ids, bad)` and the path.
  Red when: it raises a bare `ValueError`.
- **AC16** — When a probe copies `tools/lib/` and `tools/memory-tree/` into a scratch repository with
  no `check-spec-tokens.py` and calls `read_carries_coverage` with the cutoff set and a stub `resolve`,
  it returns the stub's value; without the stub it raises the named Problem.
  Red when: the generator's self-test needs the checker to run its coverage arms.
- **AC17** — When a scratch clone holds a record departing through `gap gap-mem-47`,
  `python3 tools/memory-tree/gen_build_index.py --check` exits 0 with no `as-built VERDICT` line, and
  `python3 tools/memory-tree/gen_build_index.py --check-asbuilt` exits 1 naming the record; a hand edit
  of the view makes `--check` exit 1 under `build-index DRIFT`.
  Red when: a verdict `--write` cannot cure still exits `--check` non-zero.
- **AC18** — When a probe sources `tools/unattended/lib-unattended.sh` and calls
  `resolve_generated_indexes` with the conf's declared value, its output holds both of S18's pairs.
  Red when: a pass staging the re-rendered view is refused by `--check-commit` as undeclared.
- **AC19** — When `python3 "tools/memory-tree/asbuilt_view.py" --fixture` runs in a scratch clone whose conf
  blanks every `DESIGN_*` key and which holds no `DESIGN_RECORD` file, it exits 0, and each plant exits
  as `TOOL-dTrueNorth-6` AC1 to AC5 and AC9 state.
  Red when: the fixture reads the live tree's design record.
- **AC20** — When a scratch clone gains an `amends` record changing a clause a chain spec carries,
  one `python3 tools/memory-tree/gen_build_index.py --write` followed by
  `python3 tools/memory-tree/gen_build_index.py --check` exits 0.
  Red when: the coverage regions render from the view as it was before the write.
- **AC21** — When a scratch clone stages only `TOOL-dTrueNorth-3` AC6's planted view row with a spec
  at `INPROGRESS`, `python3 tools/memory-tree/gen_build_index.py --check-coverage --staged` exits 1;
  staged with nothing the render reads, it prints the held line and exits 0.
  Red when: a staged view row is held.
- **AC22** — When `python3 "tools/memory-tree/deviation_join.py" --fixture --plant pipe-after --policy refuse`
  runs it exits 1 naming the record and `**After:**`, and `python3 "tools/memory-tree/asbuilt_view.py" --fixture --plant pipe-after`
  exits 1 with that clause's row rendered from the baseline.
  Red when: the pipe reaches a table cell and splits the row.
- **AC23** — When `python3 "tools/memory-tree/deviation_join.py" --fixture --plant unmeasured-pin` and
  `--plant unmeasured-specs` run under each policy, each exits 2 naming its own reason.
  Red when: either condition alone exits 0 over nothing measured.
- **AC24** — When `sed -n 1,162p tools/check-spec-tokens.py | grep -nE 'SPEC_CARRIES_CUTOFF|carries join'`
  runs after the pass it prints at least one line, and over `git show "271aa59d:tools/check-spec-tokens.py"`
  it prints none.
  Red when: the command finds hits at base, so it cannot fail.
- **AC25** — When the header is grepped once each for the population phrase, `SPEC_CARRIES_CUTOFF`,
  `semantic` and `rename`, each grep prints a line inside the carries join's entry.
  Red when: one of the three items the criterion names is absent.
- **AC26** — When `grep -n 'gen:build-coverage' memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md`
  runs, each file names the pair in item 6 and in item 9; and the docstring of `read_carries_coverage`
  names the set key and the stub of S16.
  Red when: item 9 lags item 6, or the out-of-kit join goes unexplained.
- **AC27** — When a scratch clone edits v2's first `**Serves:**` line and runs
  `python3 "tools/memory-tree/asbuilt_view.py" --write --out <scratch>/p.md` beside the instrument's
  `--write --out <scratch>/i.md`, `cmp` exits 0.
  Red when: the product copies v2's line and the instrument holds its literal.
- **AC28** — When `grep -n 'always exits 0' memory/HYGIENE.md tools/memory-tree/HYGIENE.template.md tools/memory-tree/gen_build_index.py`
  runs it prints nothing about `--print-bindings`, and `grep -n 'exempt' memory/HYGIENE.md` prints the
  sentence naming the `Q` row's four fields.
  Red when: a home still promises exit 0 alone.
- **AC29** — When `grep -c 'consumer = "check-memory-hygiene.sh"' tools/memory-tree/kit.toml` runs it
  counts three more than at base, and `grep -n '\^Q' tools/memory-tree/kit.toml` prints the new clause.
  Red when: a row check 21 or checks 29 and 30 require has no contract clause.
- **AC30** — When the probe of `TOOL-dTrueNorth-3` AC2 compares the region's derived-spec field with
  `carries.py --report dTrueNorth`'s after stripping `memory/builds/dTrueNorth/` and the backticks,
  the two are equal.
  Red when: the comparison still reads two spellings of one path as a difference.
- **AC31** — When `git grep -n -e 'VIEW_ROW' -e 're.compile' -- "tools/memory-tree/asbuilt_view.py"` runs,
  `check_view` reads `design_lib.VIEW_ROW` and the module compiles no row grammar of its own.
  Red when: a ported row regex sits beside the import.
- **AC32** — When `git grep -n -e '-spec-' -- tools/check-spec-tokens.py "tools/memory-tree/design_lib.py"`
  runs, one compiled date pattern prints, in `design_lib.py`, and the checker's `SPEC_DATE` is bound to it.
  Red when: the date pattern is spelled twice.
- **AC33** — When `python3 "tools/memory-tree/design_lib.py" --design --build dTrueNorth` runs after the
  records stand, `cl-dClosedLoop-0001`, `-0003`, `-0005` and `-0006` read `baseline`,
  `cl-dClosedLoop-0002` cites deviation-3 and `cl-dClosedLoop-0004` cites deviation-4.
  Red when: any cell differs from the record that amends it.
- **AC34** — When `grep -n '^DELEGATES=' tools/memory-tree/check-verdict-epoch.sh` runs it names
  `design_lib.py`, `asbuilt_view.py` and `check-spec-tokens.py`.
  Red when: a delegate of check 29 or check 30 can move its verdict with no epoch.
- **AC35** — When `grep -n -e 'NOT PIN-AWARE' -e 'NO TEMPLATE HOME' -e 'READS THE AUTHORED ROSTER ITS OWN WAY' memory/builds/dClosedLoop/BACKLOG.md`
  runs after the pass it prints the three ask rows, and each id has its `SEV` row.
  Red when: a hand-off still names a follow-up no row records.
- **AC36** — When `grep -n 'four generated regions' memory/map/features/build-readme-surface.md` and
  `sed -n 18p tools/memory-tree/README.md` run, the first prints the title and the second names 30
  checks with 29 and 30 delegated to `gen_build_index.py`.
  Red when: either carrier still counts three regions or 28 checks.
- **AC37** — When `grep -n 'DESIGN_' tools/memory-tree/README.md` runs, the rows for `deviation_join.py`
  and `asbuilt_view.py` say the keys are absent in an adopter, so off.
  Red when: a row still says the keys ship blank.
- **AC38** — When `python3 "tools/memory-tree/deviation_join.py" --approval by-risk` runs after the pass,
  no `refused:` or malformed line names `2026-10-21-build-TOOL-dTrueNorth-16-deviation-5`, and its
  `**Surface:**` line names the `--dispatch` verb.
  Red when: the widening S2 takes is recorded nowhere, or its record falls outside the grammar.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `routed-commits selftest` · `routed commits name a specced unit` · `spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `verdict epoch (kit version dates the engine)` · `verdict-epoch self-test` · `govkit selfcheck` · `build README slot contract` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `harness arms (fail branches armed or pinned)`

New arm: tools/check-spec-tokens.test.sh · covers AC9 AC10 AC11 AC12 AC14 AC32 · a WONTDO carrier, a multi-byte revision, an unparsed header, two readers of one revision list and a doubled or exported cutoff, each staged against the base join · none
New arm: tools/memory-tree/gen_build_index.py (its selftest) · covers AC7 AC15 AC16 AC17 AC19 AC20 AC21 AC22 AC27 AC31 · the key rule over the generator, a three-value expand stub, a stubbed coverage resolver, a gap record under --check and --check-asbuilt, the as-built plants over the fixture design, an amends record before one --write, and a staged view row · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 AC16 AC17 AC21 · check 29 over a planted uncarried clause and a staged view row, its SKIP without the checker, and check 30 over a gap record · that suite's assertion floor, raised by the arms added
New arm: tools/memory-tree/routed_commits.py (its selftest) · covers AC5 AC12 AC13 AC22 AC23 · the deviation fixture's key rule, subject-trailer, pipe-after and the two unmeasured plants · none
New arm: tools/unattended/unattended.test.sh · covers AC2 · a consumer dispatched while its producer is open, and after it closes · none

README rule 8 waives the unattended suites' verdict at this landing, so AC2's red-then-green reading
at the close is its targeted probe, run before and after, as `TOOL-dTrueNorth-7` §7 states for its own.

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Unit 2's join reds an unbound
  spec. (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`, the owner's ruling that a run carries the units it adds (ER:320).
  (b) None. (c) A `part k/n` carry of a repaired unit's clause. (b) reds `unbound` and (c) reds
  `parts` against the repaired unit's whole carrier; veto 1 discards both. Recommendation (a).
  Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none
- **F2 — One batch unit or two?** M4 admits two only when the minors split into disjoint write sets by
  M6. §4 shows the halves share contracts, which M6's clause 2 refuses. Rung 3. RESOLVED (agent, 2026-10-21, delegated): one.
  widens: none · relaxes: none
- **F3 — Which mechanism closes id 3 without renumbering?** (a) A `--dispatch` refusal of a consumer
  whose producer is not terminal. (b) A `gen_build_index.py --check` Problem for an edge between two
  units of one order. (c) Renumbering the units' orders, which the disposition forbids and which would
  fold the finding into frozen specs. Veto 1 discards (c). (a) and (b) each change a governance carrier
  no dTrueNorth clause names, so veto 2 holds outside the grant and rung 3 has no survivor. Rung 5 takes
  the most capable: (a) refuses at the act and reuses the edge reader that exists; (b) parses the edges
  a third time and reports later. RESOLVED (agent, 2026-10-21, delegated): (a), citing ER:388
  (`PLAY-dClosedLoop-6`), recorded as deviation-5. widens: the --dispatch verb of
  tools/unattended/unattended.sh gains a code-49 refusal of a consumer whose producer is not terminal ·
  relaxes: none
- **F4 — For id 21, the replace rule or the union?** (a) Keep the trailer-replaces-subject rule and
  name it; (b) switch to `routed_commits.py`'s union and record the departure. The instrument's
  `read_first_pass` uses the replace rule, and `TOOL-dTrueNorth-4` AC6's plants are its plants, so (b)
  moves their verdicts. Rung 3. RESOLVED (agent, 2026-10-21, delegated): (a).
  widens: none · relaxes: none
- **F5 — For id 46, refuse the pipe or escape it?** §4 says why escaping loses. Rung 3. RESOLVED (agent, 2026-10-21, delegated): refuse.
  widens: none · relaxes: none
- **F6 — For id 31, a verb of its own or amended consumers?** §4's rejected alternative for S17 says
  why. Rung 3. RESOLVED (agent, 2026-10-21,
  delegated): a verb and check 30. widens: none · relaxes: none
- **F7 — Does the build's grant lift veto 2 for every other carrier edit here?** Each is a change a
  dTrueNorth clause names: the key rule, the revision reader, the conf read and the date pattern are
  `cl-dClosedLoop-0001`'s parser and `cl-dClosedLoop-0002`'s join; S8, S16, S21, S26, S30, S34 and S36
  are `cl-dClosedLoop-0003`'s region and refusal; S13, S22 and S23 are `cl-dClosedLoop-0004`'s record
  and join; S28 and S29 are `cl-dClosedLoop-0005`'s rows; and S17 to S20, S27 and S31 are
  `cl-dClosedLoop-0006`'s view and gate. RESOLVED (agent, 2026-10-21, delegated): lifted by
  `PLAY-dClosedLoop-3`, rung 3, for all but S2, which F3 settles. grants: PLAY-dClosedLoop-3 the
  memory-tree kit, spec-token checker, verdict-epoch, HYGIENE catalogue, kit README, kit.toml and
  .unattended.conf edits S1 and S3 to S37 make for cl-dClosedLoop-0001 to cl-dClosedLoop-0006 ·
  widens: none · relaxes: none
- **F8 — For id 25, where does the date pattern live?** (a) `design_lib.py`, inside the kit, the
  checker binding to it; (b) the checker, passed to `scan_chain_specs` as a parameter. Under (b) the
  kit's other caller, the deviation join, has no pattern to pass. Rung 3.
  RESOLVED (agent, 2026-10-21, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-21 · initial draft, batching the round-1 spec audit's 23 MEDIUM and 14 LOW findings.
- rev-2 · 2026-10-21 · §3 · Edges gains the hands-off mirroring TOOL-dTrueNorth-20's consumes-from.
- rev-3 · 2026-10-21 · §5 §6 §8 §10 · criteria name this build's new modules quoted or bare, so the spec-tokens paths join stops refusing `--dispatch` before they exist; §5, §8 and §10 tightened under the 49152-byte ceiling. No observation moves.
- rev-4 · 2026-10-21 · §4 · deviation-5's text moved to a prompts record, unchanged, so the generated records region can grow under the 49152-byte ceiling.

## 10. Reuse audit

Every item extends a seam the units build: `design_lib.py`'s readers (unit 1), the carries join (unit 2), the coverage read and
check 29 (unit 3), `deviation_join.py` (unit 4), `cmd_print_bindings` (unit 5), the as-built
generator and its host (unit 6). At base the seams cited are `read_blobs_at_rev`
(`tools/memory-tree/gen_build_index.py:2934`), `read_landed_unclosed`'s injectable resolver (`:1678`),
`check_index_input` (`:831`), `tree_lib.parse_conf` and `build_spec_path_re`, `read_consumes_from` and
the dispatch order gate, and `resolve_generated_indexes`. `python tools/codebase-map/reuse_lookup.py
"refuse a dispatch whose producer unit is not closed"` ranked `baseline_units` and `asks_unit_in` by
name stem and missed `read_consumes_from`, found by reading `tools/unattended/lib-unattended.sh`, the
one place the probe and the source disagreed; `"resolve a sibling kit directory with an injectable
resolver"` ranked `resolve_kit_dir`, the seam S16 follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit and its generated view kept fresh" --terms "spec-audit promoted unit repairs order
as-built view deviation record re-render guard selftest pin"`
