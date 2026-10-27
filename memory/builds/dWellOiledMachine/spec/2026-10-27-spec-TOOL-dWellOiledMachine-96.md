# TOOL-dWellOiledMachine-96 — an arm line's suite path is its first path-shaped token, so an annotated arm still joins the build-order write set

**Status:** OPEN · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 67 · advances TOOL-dWellOiledMachine-62

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dWellOiledMachine-96-deviation-961.md](../build/2026-10-27-build-TOOL-dWellOiledMachine-96-deviation-961.md) | deviation | — |
| [2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md](../reviews/2026-10-27-review-TOOL-dWellOiledMachine-95-spec-audit.md) | spec-audit | TOOL-dWellOiledMachine-95 TOOL-dWellOiledMachine-97 |

<!-- /gen:spec-records -->

## 1. Goal

Promoted from the spec audit of the round-3 promotions
(`memory/builds/dWellOiledMachine/reviews/2026-10-27-review-TOOL-dWellOiledMachine-91-spec-audit.md`),
finding 25, item H2, at HIGH. TOOL-dWellOiledMachine-93 S3 takes an arm's suite path as all the text
between `New arm:` and the first ` · `, backticks stripped. 274 live arm lines carry words after the
path, such as `tools/run-gates/measure_legs.py --selftest` or `tools/lib/resolve-python.test.sh, the
S12 ban`, and the overlap rule tests containment only, so such a segment never meets the real path. Two
units sharing an annotated suite would still render `yes` for parallel, the misreading 93 exists to
remove, and 93 S5's tree-wide re-render would publish it into other builds' READMEs. This unit fixes
the parse: the suite path is the first whitespace-delimited token of the first field, kept only when
it is path-shaped, read through one field split the covers join shares.

## 2. Scope (IN)

- **S1** — One field split. `tools/memory-tree/design_lib.py` gains `read_arm_fields(line)`: the text
  of an arm line after `New arm:`, split on ` · `, each field stripped. `scan_arm_covers`
  (`tools/check-spec-tokens.py:1355`) reads its fields through it, so the covers join and the write
  set split one arm line one way. Observed by AC1, AC6.
- **S2** — The suite path. `design_lib` gains `derive_arm_suite_path(line)`: `None` when
  `read_arm_fields` gives fewer than two fields; otherwise the first field with backticks removed, its
  first whitespace-delimited token, one trailing comma stripped, returned only when `check_dir_shaped`
  (`tools/memory-tree/design_lib.py:579`) holds for that token with any trailing `/` replaced by one
  `/`, which is two or more real segments and no deploy-time token or glob; else `None`. So `none`, a
  bare filename and a line with no ` · ` add nothing. Observed by AC1, AC3.
  **Readers:** by name: `tools/memory-tree/design_lib.py`, which gains the reader, and `tools/memory-tree/gen_build_index.py`, its caller. by value: `tools/memory-tree/gen_build_index.py`, whose write set takes the returned path.
- **S3** — Spec 93 carries the parse. Spec 93 takes a rev bump, its §9 line naming this unit and
  finding 25 of the round-3 promotions audit: S3's suite path of each `read_spec_arm_lines` line is
  `derive_arm_suite_path(line)`, a `None` adding nothing; S2 re-points `scan_arm_covers`' field split
  to `read_arm_fields`; §4 Inventory lists both functions; §6 gains an AC7 that renders a step from two
  fixture specs, one whose arm line is
  `New arm: tools/memory-tree/design_lib.py (its selftest) · covers AC1 · s · none` and one listing
  `tools/memory-tree/design_lib.py` under Files touched, and reads `no`; and §7 gains
  `New arm: tools/memory-tree/gen_build_index.py · covers AC7 · a selftest case staged against a suite path read verbatim up to the first field separator · none`.
  Observed by AC2, AC4.
- **S4** — The rev bump lands before unit 93's pass, by the route TOOL-dWellOiledMachine-95 §8 F1
  takes: the build run's main loop makes it at BUILD-METHOD M2's cross-read, before its first code
  pass, as one spec pass whose commit subject names this unit, so unit 93's builder builds S1 to S3.
  At this unit's own pass, at order 67, nothing is written: the pass runs AC1 to AC7 and records them.
  Observed by AC5.

## 3. Non-goals (OUT)

- No change to the overlap rule, `check_writes_intersect`, or to `derive_parallel_step`'s own path
  filter.
- No change to which arm lines exist or how `read_spec_arm_lines` joins continuations: 93 S1 stands.
- A bare filename such as `check_roles.py` stays outside the write set: it names no path the overlap
  rule could meet, and 31 live arm lines are of that shape (§4).
- No lint over free-text spec fields parsed by a tool: the report's left-shift line, a separate
  mechanism (M2).
- Moving `extract_gates` into `design_lib` is finding 18 (M7), carried by the minors batch
  TOOL-dWellOiledMachine-97.

### Edges

- **consumes-from** `TOOL-dWellOiledMachine-93` — `read_spec_arm_lines` and S3's caller-side join, whose suite-path parse this unit specifies and amends into spec 93 before unit 93 builds
- **hands-off** `TOOL-dWellOiledMachine-102` — S4, which states the commit pair the ordering claim compares (round-4 promotions audit, finding 12)
- **hands-off** `TOOL-dWellOiledMachine-103` — AC5 and the §6 preamble, rewritten to load and call the ordering probe for spec 93 (round-4 promotions audit, finding 20)
- **hands-off** `TOOL-dWellOiledMachine-104` — §4, §5's testing line and §6, which gain the fixture and AC8 that observe the ordering check red (round-4 promotions audit, finding 30)
- **hands-off** `TOOL-dWellOiledMachine-108` — §1, S2, S3, §3, §4, AC1 and AC3, amended before this unit builds (round-4 promotions audit, findings 2, 3, 6, 9, 14, 17, 22, 23 and 28)

## 4. Design

### Evidence

- 93 S3 defines the suite path as the text between `New arm:` and the first ` · `, backticks stripped
  (`spec-93.md:42-48`), and no AC of spec 93 reads an annotated arm line (`:140-166`).
- `check_writes_intersect` holds when `check_guard_trips` holds either way, exact path or containment
  (`tools/memory-tree/design_lib.py:589-605`), so `tools/run-gates/measure_legs.py --selftest` never
  meets `tools/run-gates/measure_legs.py`.
- `derive_parallel_step` filters each write word with a local two-segment test
  (`tools/memory-tree/gen_build_index.py:1732-1734`), and the unit entry's `writes` is set in
  `parse_spec_text` (`:494`, `:548`).
- `check_dir_shaped` holds for a `/`-terminated token of two or more real segments that is not a
  deploy-time token and carries no space or glob (`tools/memory-tree/design_lib.py:565-585`).
- `scan_arm_covers` splits the joined arm line with `" ".join(arm).split(" · ")`
  (`tools/check-spec-tokens.py:1355`), so 93 S3's caller would spell a second split.
- The arm lines' shapes, MEASURED 2026-10-27 over `git grep -h "^New arm:" -- 'memory/builds/*/spec/*.md'`
  (2496 lines; PINNED, re-derived by re-running that survey):

| Shape of the first field | Lines | S2 yields |
|---|---|---|
| a bare path, backticked or not | 2195 | the path |
| a path followed by words | 141 | the path |
| a backticked path followed by words, backticked or not | 75 | the path |
| a path with a trailing comma, then words | 28 | the path |
| a one-segment name such as `row_grammar.py --selftest` | 31 | `None` |
| `none` | 9 | `None` |
| no ` · ` at all, 16 opening `none` | 17 | `None` |

- An earlier spec audit proposed the same rule for another build's suite paths, the first
  whitespace-delimited word of the first field
  (`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-1-spec-audit-round1.md:142`).

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `read_arm_fields` | function, `design_lib.py` | `read`, OK |
| `derive_arm_suite_path` | function, `design_lib.py` | `derive`, OK |

### Files touched (estimate)

- `memory/builds/dWellOiledMachine/spec/2026-10-27-spec-TOOL-dWellOiledMachine-93.md` (S3's rev bump)
- `memory/builds/dWellOiledMachine/README.md` (re-rendered by
  `python tools/memory-tree/gen_build_index.py --write`, since 93's rev cell moves)

The code S1 and S2 name is written by unit 93's pass, under 93's Files touched, which already lists
`tools/memory-tree/design_lib.py`, `tools/check-spec-tokens.py` and
`tools/memory-tree/gen_build_index.py`.

### Alternatives rejected

- **The segment verbatim, 93 S3 as written.** It is the finding: 274 annotated lines never join.
- **Every path-shaped token of the first field.** A field such as
  `tools/memory-tree/check-arms.py, its --selftest` names one suite; prose after it may name a fixture
  path the arm only reads, which would serialise steps on files nobody writes.
- **A second split in `parse_spec_text`.** The covers join already splits the line; two splits of one
  grammar is the copy the charter's reuse rule forbids (S1).
- **This unit's code at its own pass, after 93 builds.** 93's pass would render, and publish into
  other builds' READMEs, the misreading this unit removes, and a landing that carries this unit
  forward ships it.

## 5. Production-readiness checklist

- security — N/A — no write path, secret or surface; a render's input widens.
- perf / scale — one split and one token test per arm line per render.
- error / empty / loading states — a line with no ` · `, a `none` field or a one-segment name adds
  nothing to the write set.
- observability — the re-rendered build order shows which steps an annotated arm makes serial.
- risks — steps of other builds sharing an annotated suite flip to `no`; that is the correct reading,
  and 93 S5's re-render carries them.
- testing — AC1 to AC7, and the arm S3 adds to spec 93's §7.
- migration — none: the README regions are generated.
- user docs — none: no verb or key a user types changes.

## 6. Acceptance criteria

Each `python -c` call runs from `tools/memory-tree/` and imports `design_lib`; `<spec 93>` is the file
under Files touched, and `<BASE>` is the build run's pinned `base:` fact in
`memory/builds/dWellOiledMachine/RUN.md`.

- **AC1** — When `python -c` prints `derive_arm_suite_path` over seven lines, one per shape class of
  §4's table: `New arm: tools/memory-tree/design_lib.py · covers AC1 · s · none`,
  `New arm: tools/memory-tree/design_lib.py (its selftest) · covers AC1 · s · none`, the same path
  backticked and followed by a backticked `--selftest`,
  a `New arm:` line whose first field is the resolver library's path with a trailing comma and the words `its arm`,
  `New arm: row_grammar.py --selftest · s · none`, `New arm: none · s · none` and
  `New arm: none. prose`, it prints `tools/memory-tree/design_lib.py` three times,
  `tools/lib/resolve-python.sh`, then `None` three times.
  Red when: an annotated segment is returned verbatim, or a one-segment name or `none` is returned.
- **AC2** — When `python -c` imports `gen_build_index`, builds two unit entries with `parse_spec_text`
  from two fixture spec texts sharing `order 1`, one whose §7 arm line is
  `New arm: tools/memory-tree/design_lib.py (its selftest) · covers AC1 · s · none` and whose Files
  touched lists `tools/memory-tree/gen_build_index.py`, the other listing
  `tools/memory-tree/design_lib.py` under Files touched, and prints
  `derive_parallel_step` over the two, it prints `no`.
  Red when: the annotated arm never meets the sibling's path and `yes` prints.
- **AC3** — When `python -c` runs `derive_arm_suite_path` over every line
  `git grep -h "^New arm:" -- 'memory/builds/*/spec/*.md'` prints, it prints 0 for the paths carrying a
  space, a backtick, a parenthesis or a trailing comma, and prints `tools/govkit/govkit.py` among the
  paths, from the annotated line `tools/govkit/govkit.py selfcheck 7j4`.
  figure: 0 is the bound; the path set is DERIVED from the tree at observation time.
  Red when: an annotated segment reaches the write set verbatim.
- **AC4** — When `awk '/^- \*\*S3\*\*/{p=1} /^- \*\*S4\*\*/{p=0} p' <spec 93> | grep -c derive_arm_suite_path`
  runs, it prints 1 or more, and `grep -c "^New arm: .*gen_build_index.py" <spec 93>`
  prints 1.
  Red when: 93's S3 still reads the segment verbatim, or the annotated case has no arm.
- **AC5** — When `git log --reverse --format=%s <BASE>..HEAD | grep -E "TOOL-dWellOiledMachine-(93|96)([^0-9]|$)" | head -1`
  runs at this unit's pass, it prints this unit's amendment commit.
  Red when: the amendment lands after unit 93's pass, and 93 builds the verbatim parse.
- **AC6** — When `grep -c 'split(" · ")' tools/check-spec-tokens.py` runs, it prints 0, and
  `grep -c "read_arm_fields" tools/check-spec-tokens.py` prints 1 or more.
  Red when: the covers join keeps its own split beside the kit's.
- **AC7** — When `python tools/memory-tree/gen_build_index.py --check` and
  `python tools/codebase-map/gen_map.py --check` run at this unit's pass, each exits 0.
  Red when: a README whose build order the parse moved, or the symbol render, is left stale.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `tier2-review self-test` · `policy fixtures`

No arm is added at this unit's pass: the selftest case S3 declares lands on spec 93's §7 as its
`New arm:` line, and the close observes it there.

## 8. Open questions

- **F1 — Where does the parse land, given this unit's order is 67 and unit 93's is 66?** (a) in this
  unit's own code at its pass, replacing 93's parse; (b) in spec 93 by rev bump at the build run's M2
  cross-read, so unit 93 builds it, the route TOOL-dWellOiledMachine-95 §8 F1 takes; (c) a re-order.
  (a) leaves 93's pass rendering and re-rendering other builds' READMEs with the misreading, and a
  landing that carries this unit forward ships it. (c) moves a unit for a text change. (b) gives one
  build of the parse, in the unit whose mechanism it is. RESOLVED (agent, 2026-10-27, delegated): (b).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of the round-3 promotions, finding
  25 (H2).
- rev-2 · 2026-10-27 · §3 · Edges: the reciprocal of each edge the spec audit of the round-4
  promotions' promoted units declare on this unit, mirrored from TOOL-dWellOiledMachine-102, TOOL-dWellOiledMachine-103, TOOL-dWellOiledMachine-104, TOOL-dWellOiledMachine-108.

## 10. Reuse audit

The seams reused are `check_dir_shaped` and `derive_dir_segments`
(`tools/memory-tree/design_lib.py:565-585`), which already decide what a declared path token is for the
guard-legs join and the build-order render, and `scan_arm_covers`' field split
(`tools/check-spec-tokens.py:1355`), moved into the kit as `read_arm_fields` rather than copied. The
probe `python tools/codebase-map/reuse_lookup.py "take the path token from an annotated free-text field"`
ranked `read_text`, `write_text`, `field` and `resolve_prefix_token` by name stem, none an arm-line
parser; the recall query below ranked TOOL-dWellOiledMachine-93 and this finding's record first, and
an earlier audit's identical first-word rule fourth.

Recall terms used: `python tools/memory-recall/query.py "how is the suite path read from an annotated
New arm line" --terms "New arm suite path annotation selftest token pathlike write set
derive_parallel_step check_dir_shaped covers field"`
