# TOOL-dWitnessedBar-106 — the pre-push hook's three policy reads at R never read looser than R's committed policy file

**Status:** CLOSED · rev-1 · 2026-11-21 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 51 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-52 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 TOOL-dWitnessedBar-58 TOOL-dWitnessedBar-59 TOOL-dWitnessedBar-60 TOOL-dWitnessedBar-61 TOOL-dWitnessedBar-62 TOOL-dWitnessedBar-63 TOOL-dWitnessedBar-64 TOOL-dWitnessedBar-65 TOOL-dWitnessedBar-66 TOOL-dWitnessedBar-67 TOOL-dWitnessedBar-68 TOOL-dWitnessedBar-69 TOOL-dWitnessedBar-70 TOOL-dWitnessedBar-71 TOOL-dWitnessedBar-72 TOOL-dWitnessedBar-73 TOOL-dWitnessedBar-74 TOOL-dWitnessedBar-75 TOOL-dWitnessedBar-76 TOOL-dWitnessedBar-77 TOOL-dWitnessedBar-78 TOOL-dWitnessedBar-79 TOOL-dWitnessedBar-80 TOOL-dWitnessedBar-81 TOOL-dWitnessedBar-82 TOOL-dWitnessedBar-83 TOOL-dWitnessedBar-84 TOOL-dWitnessedBar-85 TOOL-dWitnessedBar-86 TOOL-dWitnessedBar-87 TOOL-dWitnessedBar-88 TOOL-dWitnessedBar-89 TOOL-dWitnessedBar-90 TOOL-dWitnessedBar-91 TOOL-dWitnessedBar-92 TOOL-dWitnessedBar-93 TOOL-dWitnessedBar-94 TOOL-dWitnessedBar-95 TOOL-dWitnessedBar-96 TOOL-dWitnessedBar-97 TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 |
| [2026-11-19-build-TOOL-dWitnessedBar-106-1-acceptance-ledger.md](../build/2026-11-19-build-TOOL-dWitnessedBar-106-1-acceptance-ledger.md) | journal | — |
| [2026-11-19-build-TOOL-dWitnessedBar-106-1-builder-return.md](../build/2026-11-19-build-TOOL-dWitnessedBar-106-1-builder-return.md) | journal | — |
| [2026-11-21-build-TOOL-dWitnessedBar-106-deviation-1061.md](../build/2026-11-21-build-TOOL-dWitnessedBar-106-deviation-1061.md) | deviation | — |
| [2026-11-21-build-TOOL-dWitnessedBar-106-widen-26.md](../build/2026-11-21-build-TOOL-dWitnessedBar-106-widen-26.md) | widen | — |
| [2026-11-19-prompt-TOOL-dWitnessedBar-106-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dWitnessedBar-106-build-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-brief.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-brief.md) | journal | — |
| [2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-spec-writer.md](../prompts/2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-spec-writer.md) | journal | — |
| [2026-11-21-review-TOOL-dWitnessedBar-106-closing-diff-review-round2.md](../reviews/2026-11-21-review-TOOL-dWitnessedBar-106-closing-diff-review-round2.md) | diff-review | TOOL-dWitnessedBar-107 TOOL-dWitnessedBar-108 |

<!-- /gen:spec-records -->

## 1. Goal

The closing diff review's round 1
(`memory/builds/dWitnessedBar/reviews/2026-11-21-review-TOOL-dWitnessedBar-1-closing-diff-review-round1.md`)
confirmed finding 1 at HIGH, item H1. `.githooks/pre-push#read_policy_at` starts `hooks.bypass` at
`allowed`, and reads it only after the policy kit resolves. A pushed tip that deletes the kit, a node
with no python, a reader that fails, or a tip whose catalogue drops `refused` therefore turns R's
`hooks.bypass = "refused"` into `allowed`, and unwitnessed pass commits land. `verdict.blocks` and
`verdict.held` share the class: with no kit both read their catalogue defaults whatever R declares.

This unit builds the skeptic's class-level fix. Each of the three reads at R gains a floor parsed out
of R's own committed `.governance/policy.toml`, never executed. The value the hook acts on is the
stricter of the reader's answer, or today's fallback, and that floor. A pushed tree can then no
longer read any of the three keys looser than R's own bytes declare.

## 2. Scope (IN)

- **S1** — `scan_policy_bytes`, a new hook function. It takes the text of R's policy file, a table, a
  key and the key's order, and prints one reading per line for each line that names `<table>.<key>`.
  A reading is the declared value when it is a member of the order, else `?`. It prints nothing when
  no line names the key. The grammar is §4 "The floor grammar". Observed by AC1, AC2 and AC5.
- **S2** — `derive_strictest`, a new hook function. It takes an order and values and prints the value
  latest in the order among those that are members, or nothing. The three orders and the policy
  file's path are declared once each, at column 0, beside the hook's existing `PP_READ_AT=""` line:
  `PP_BLOCKS_ORDER="own-only own-mixed-contended every-red"`,
  `PP_HELD_ORDER="on-demand peer-or-cadence push-selected"`,
  `PP_BYPASS_ORDER="allowed refused"` and `PP_POLICY_REL=.governance/policy.toml`. The three
  membership `case` tests inside `read_policy_at` read these orders through `derive_strictest`, so the
  hook spells each value list once. The `PP_WHY` text naming the admitted values renders
  `$PP_BLOCKS_ORDER`, byte-equal to today's quoted list. Observed by AC3 and AC8.
- **S3** — `read_policy_at` composes the floor. It reads R's blob of `$PP_POLICY_REL` once per sha.
  For each key it takes today's value as the base, the reader's answer or the fallback a missing
  python, a missing kit or a failing reader reads today. It then sets the key to `derive_strictest`
  over the base and the floor, by §4 "The composition". After `PP_READ_AT=$sha` the function has one
  exit, its end, so every path passes the floor. The no-kit branch keeps its wording, and a run with
  no python launcher says so in `PP_WHY` instead of naming the kit. Observed by AC1, AC2, AC3, AC4,
  AC5 and AC7.
- **S4** — The account of a raise. Where the floor makes a key stricter than its base, `PP_WHY` for
  `verdict.blocks` gains `; ` and one fragment, and `PP_BYPASS_WHY` for `hooks.bypass` is set to it.
  The fragments are §4 "The messages". `verdict.held` gains no new line: its one consumer prints
  `push-selected` when it acts. Observed by AC2, AC5 and AC6.
- **S5** — The hook's own comments say what it now does. The `WHICH RED BLOCKS, READ AT R` header
  states the floor where it now says a missing kit reads the catalogue default, and gains a
  `WHAT THE FLOOR DOES NOT CHECK` paragraph listing §5's residuals. The `EACH HOOK BYPASS RECORDED`
  block's comment names the floor beside its existing deny-by-default sentence. Observed by AC9.
- **S6** — The arms, in `.githooks/pre-push.test.sh`: the floor harness of §4 "The arms", one plant
  per reader state, the end-to-end missing-kit push, the single-exit measure and the parity check.
  The new test helper `run_floor_read` runs one plant. Observed by AC1 to AC8.
- **S7** — `help/policy.md` gains one bullet in its list of consumers naming the three keys, the
  hook that reads them at the remote tip, and the floor. Observed by AC10.
- **S8** — `memory/map/generated/symbols.json` is regenerated, gaining the test helper
  `run_floor_read`; the hook file itself is not a scanned layer. Observed by AC11.

## 3. Non-goals (OUT)

- The sibling readers of the same class. `tools/unattended/unattended.sh#read_gate_blocks` reads
  `verdict.blocks` as `own-only` when no kit resolves beside the unattended kit, and
  `tools/push-main.sh#check_landing_verdict` reads `hooks.bypass` at the landed revision. Each reads
  a kit beside itself, not the pushed tree's, so the reachable path H1 names does not reach them.
- A `check-arms.py` predicate that every `read_policy_at` exit has an arm, which the review's
  left-shift gate asks for. §8 F4 says why S3's single exit and AC7's arm take its place here.
- A new refusal class. §8 F1 says why the floor raises a value and never refuses on its own.
- Reading the policy reader or its catalogue from R instead of the pushed tree. The reader stays
  vetted at the tip by `check_reviewed_file`; the floor makes a tampered reader unable to loosen.
- Any edit to `tools/policy/`, its catalogue, or `help/reference/policy.md`, which is rendered
  from the catalogue.
- H2 and the other findings of the same review record.

The code this unit changes was built by three CLOSED units of this build, found from the `Pass:`
trailers of `git log -L` over `read_policy_at`: TOOL-dWitnessedBar-3 (`verdict.blocks` and the no-kit
branch, 930a5289d), TOOL-dWitnessedBar-5 (`verdict.held`, eef75404f) and TOOL-dWitnessedBar-2
(`hooks.bypass` and the bypass block, 7f3e24092). This unit edits only their built code and their
arms, never their specs, which are frozen.

### Edges

- **hands-off** external — the class's sibling readers named in the first bullet above, each a
  follow-up outside this build
- **hands-off** external — the `check-arms.py` population kind for a function's exits, a separate
  gate (`doc.build-method#m2-the-spec-set-decompose-detect-classify-act`) and a follow-up outside this build

## 4. Design

### Evidence

Read on 2026-11-21 at `63be790a2`. Its blobs are `.githooks/pre-push` 13e24816, the blob the review
cites, `.githooks/pre-push.test.sh` 45c73d4d, `tools/policy/catalogue.toml` 25076c3d,
`tools/policy/policy.py` 77f33396 and `help/policy.md` f0103fb0.

- `read_policy_at` sets `PP_BYPASS=allowed` before any read (`.githooks/pre-push@13e24816:1550`).
  It assigns all three keys only inside the `resolve_kit_dir` loop (`@13e24816:1561-1585`). It
  returns early from the `-z "$dir"` branch (`@13e24816:1587-1589`).
- Probe 1. `read_policy_key` and `read_policy_at` were cut by awk from 13e24816 and run over a
  scratch repo whose R file holds `[verdict]` `blocks = "every-red"`, `held = "push-selected"` and
  `[hooks]` `bypass = "refused"`. With `resolve_python` stubbed to fail they printed `own-only`,
  `on-demand` and `allowed`, and a `PP_WHY` naming a missing policy kit. With `resolve_kit_dir`
  stubbed to fail they printed the same. With the kit stubbed to a `policy.py` that exits 3 they
  printed `every-red`, `on-demand` and `allowed`. (PINNED 2026-11-21)
- Probe 2. The real `policy.py` was run over a second scratch repo with commit A, a file naming
  none of the three keys, then R as above. Its catalogue copy had each of the three `allowed` lists
  narrowed to exclude R's value. `get <key> --rev R` printed `own-only`, `on-demand` and `allowed`,
  each exit 0. R is invalid against that catalogue, so the reader reads the last valid revision, A.
  This is the review's tampered-catalogue path, and the answer is one the hook admits. (PINNED 2026-11-21)
- Probe 3. The real reader over a file holding
  `verdict = { blocks = "own-only", held = "on-demand" }` and `hooks = { bypass = "allowed" }`
  answered each value with `file · set in .governance/policy.toml`, exit 0. (PINNED 2026-11-21)
- Probe 4. AC7's measure over 13e24816 printed `1`, the `-z "$dir"` return. (PINNED 2026-11-21)
- `PP_HELD` has one consumer, `[ "$PP_HELD" = push-selected ]` (`@13e24816:2030`). `PP_BYPASS` has
  three, all in the bypass block (`@13e24816:2079-2085`). `PP_POLICY` is read by the doc class, the
  policy line, the inherited-green compare and the `GATE_VERDICT_BLOCKS` export.
- The hook defines no `fail()` (`grep -c '^fail()'` printed 0, PINNED 2026-11-21), so it is outside the
  `check-arms.py` population that the module docstring of `tools/memory-tree/check-arms.py` states.
- `tools/policy/policy.py#POLICY_REL` is `.governance/policy.toml`, a fixed root-relative path. The
  hook parses `INHERITED_RED_MAX_AGE` out of R's committed gate file the same way and never executes
  it (`.githooks/pre-push#read_policy_key`).
- The catalogue rows give the allowed lists: `tools/policy/catalogue.toml@25076c3d:109` for
  `hooks.bypass`, `tools/policy/catalogue.toml@25076c3d:905` and `tools/policy/catalogue.toml@25076c3d:913`. `verdict.blocks`'s summary says each later value blocks a superset of the classes the earlier
  one blocks. `hooks.bypass`'s says `refused` also refuses what `allowed` records.
- The existing fixtures that write a policy file and run with no kit or a failing kit write none at
  R: `build_ir_fixture`'s `nokit` and `broken` plants skip `write_ir_policy`
  (`.githooks/pre-push.test.sh#build_ir_fixture`). Every other fixture with a file at R carries the
  real reader, which confirms R's value. So no existing arm's expected value moves (DERIVED from those
  builders).
- `python tools/check-spec-tokens.py --legs-for` over each path in Files touched printed the legs §7
  owes; `.githooks/` alone trips a set it marks broad.

### The floor grammar

```
text     = git show <sha>:$PP_POLICY_REL, read once per sha; an absent blob names no key
line     = each line of text, one trailing CR stripped, the first line's UTF-8 BOM stripped
skip     = a blank line, or one whose first non-blank byte is '#'
header   = '[' name ']' then blanks and an optional '#' comment; name with blanks and quotes
           deleted is the current table; a '[[' header sets a table no key matches
lhs      = the text before the line's first '=', blanks and quotes deleted
names K  = (current table = T and lhs = k)
         | (no header yet and lhs = T.k)
         | (no header yet and lhs = T and the value opens '{')
value    = the text after the first '=', blanks trimmed: one "v" or 'v' with no quote inside v,
           then blanks and an optional '#' comment, and nothing else
reading  = v when v is a member of K's order; '?' for any other line that names K
```

K is `verdict.blocks`, `verdict.held` or `hooks.bypass`, with T its table and k its key. A spelling
the grammar does not name, such as a multi-line string, reads as no mention (§5).

### The composition

| reader state for K | base, today's value | floor from the readings |
|---|---|---|
| no python launcher resolves | the catalogue default | the strictest member read; K's strictest value if any reading is `?` |
| no policy kit resolves | the catalogue default | as above |
| the reader exits non-zero, or answers outside K's order | `every-red`, `on-demand`, `allowed` | as above |
| the reader answers a member A | A | the strictest member read; a `?` adds nothing (§8 F3) |

K reads `derive_strictest "$ORDER" "$base" <floor>`. No reading at all leaves the base, so a file that
names none of the keys reads exactly what it reads today.

### The messages

```
raise by a member:  <PP_POLICY_REL> at <sha8> declares <K> <v>, which the policy reader did not confirm, so <K> reads <v>
raise by a '?':     <PP_POLICY_REL> at <sha8> spells <K> in a form this hook does not parse and the policy reader did not answer, so <K> reads its strictest value, <v>
no python:          no python launcher resolves to run the policy reader, so the catalogue default own-only applies, with <bnd>
```

The bypass block already prints a non-empty `PP_BYPASS_WHY` (`@13e24816:2053`), and the policy line
prints `PP_WHY` (`@13e24816:2130`).

### The arms

All arms sit in `.githooks/pre-push.test.sh` after the bypass arms. The floor harness cuts the hook's
`read_policy_key`, `scan_policy_bytes`, `derive_strictest` and `read_policy_at` by awk range, as the
`TOOL-dWitnessedBar-63` AC11 arm cuts its readers. It takes the column-0 `PP_*_ORDER=` and
`PP_POLICY_REL=` lines by grep. Its scratch repo has three kit copies: `kr`, the real reader; `kb`,
a `policy.py` that exits 3; and `kt`, the real reader whose catalogue lists each of the three keys
without its strictest value. The repo commits three revisions of the policy file at the path
`tools/policy/policy.py#POLICY_REL` names, read by the arm. A names none of the three keys, as
`[runtime]` `agents-in-flight = 6`. R is probe 1's strict file. R3 is probe 3's inline-table file.

`run_floor_read <plant> <sha>` evals the cut in a subshell. It stubs `check_reviewed_file` to pass and
`resolve_python` and `resolve_kit_dir` per plant: `nopy` fails the first; `nokit` fails the second;
`broken`, `tampered` and `real` answer `kb`, `kt` and `kr`. It prints
`blocks=<v> held=<v> bypass=<v>`, then the `PP_WHY` and `PP_BYPASS_WHY` lines.

| plant | at A | at R | at R3 |
|---|---|---|---|
| nopy | `own-only on-demand allowed` | `every-red push-selected refused` | `every-red push-selected refused` |
| nokit | `own-only on-demand allowed` | `every-red push-selected refused` | not run |
| broken | `every-red on-demand allowed` | `every-red push-selected refused` | not run |
| tampered | not run | `every-red push-selected refused` | not run |
| real | not run | not run | `own-only on-demand allowed` |

The A column and the `real` row are controls, each green today and red under an over-fix that reads
every key at its strictest. The end-to-end arm builds `build_bp_fixture` with `refused` and
`peer-node`. It then commits `git rm` of the kit's `policy.py` on the tip and runs `run_bp_push`.
The single-exit arm runs AC7's measure, and the parity arm runs AC8's compare.

### Inventory

| identifier | kind | file | naming cell |
|---|---|---|---|
| `scan_policy_bytes` | function | `.githooks/pre-push` | VERBS `scan` |
| `derive_strictest` | function | `.githooks/pre-push` | VERBS `derive` |
| `PP_BLOCKS_ORDER`, `PP_HELD_ORDER`, `PP_BYPASS_ORDER` | variables | `.githooks/pre-push` | none |
| `PP_POLICY_REL` | variable | `.githooks/pre-push` | none |
| `run_floor_read` | test function | `.githooks/pre-push.test.sh` | VERBS `run` |

### Migration

None. No stored format changes, and a repository whose R file names none of the keys reads as today.

### Rollout

Lands live; there is no switch. A push whose R names a key the pushed tree reads looser now reads R's
value, a stricter result and never a looser one. A repository under `hooks.bypass = "refused"` whose
tip lacks the policy kit now meets its own refusal; the remedy is to restore the kit.

### Files touched (estimate)

- `.githooks/pre-push`
- `.githooks/pre-push.test.sh`
- `help/policy.md`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- The finder's instance fix: parse `hooks.bypass` alone from R's raw bytes. It leaves
  `verdict.blocks` and `verdict.held` in the class.
- Reading the reader and its catalogue from R with `git show`. It duplicates the kit-at-R machinery
  `check_reviewed_file` stands in for, and a broken R kit would still need a floor.
- K's strictest value whenever the reader cannot answer, whatever R declares. Every adopter whose tip
  carries no policy kit would then read `refused`, and under a `local-hook` verdict nothing lands.

## 5. Production-readiness checklist

- security — no new write path or surface. The floor reads R's committed bytes as data, never as
  code, the way `read_policy_key` reads the gate file. It can only make a value stricter.
- perf / scale — one `git show` per sha already read once, and one bash pass per key over a small file.
- error / empty / loading states — an absent file or a file naming no key leaves today's values; an
  unparsed mention reads the strictest value only when the reader also cannot answer.
- observability — each raise prints one line naming the file, the sha, the key and the value.
- risks — WHAT THE FLOOR DOES NOT CHECK, which S5 writes into the hook. It does not see a key in a
  spelling the grammar does not name, such as a multi-line string or a quoted dotted root key the lhs
  rule misses. A tampered reader over such an R stays as loose as today. A false mention only makes
  a key stricter. The three orders are the hook's own fact; AC8 holds their membership to the
  catalogue, not their rank. `verdict.held`'s rank between `on-demand` and `peer-or-cadence` changes
  no hook behaviour (§8 F2).
- testing — AC1 to AC8 by the arms at the close, AC9 to AC11 by grep.
- migration — none.
- user docs — `help/policy.md` (S7).

## 6. Acceptance criteria

- **AC1** — When `run_floor_read nopy` runs over the floor harness's A, R and R3, it prints the nopy
  row of §4 "The arms". At R and R3 `PP_WHY` names a python launcher, not a kit.
  Red when: a node with no python reads R's `refused` as `allowed`.
- **AC2** — When `run_floor_read nokit` runs over A and R, it prints the nokit row. At R the bypass
  line holds `declares hooks.bypass refused, which the policy reader did not confirm` and `PP_WHY`
  holds the same fragment for `verdict.blocks every-red`. At A `PP_WHY` still opens
  `no policy kit resolves, so the catalogue default own-only applies`.
  Red when: a tip with no policy kit reads any key looser than R declares.
- **AC3** — When `run_floor_read broken` runs over A and R, it prints the broken row.
  Red when: a reader that exits non-zero turns R's `push-selected` or `refused` into its default.
- **AC4** — When `run_floor_read tampered` runs over R, it prints `every-red push-selected refused`.
  Red when: a catalogue narrowed at the tip makes the reader's exit-0 answer loosen R's values.
  fixture: the `kt` kit copy, built by the arm from the real catalogue.
- **AC5** — When `run_floor_read` runs at R3 under `nopy`, the bypass line holds
  `spells hooks.bypass in a form this hook does not parse`; under `real` it prints
  `own-only on-demand allowed`.
  Red when: an unparsed spelling reads loose with no reader, or strict over a reader that answers it.
- **AC6** — When `run_bp_push` pushes a `build_bp_fixture refused refused peer-node` tip carrying
  `git rm` of the kit's `policy.py`, the push exits non-zero and `read_token` prints `bypass-refused`.
  The journal holds `bypass=unwitnessed-commit` naming `BP_UN` with `policy=refused`.
  Red when: the hook lands an unwitnessed pass commit because the tip has no policy reader.
- **AC7** — When `awk '/^read_policy_at\(\)/,/^}/' .githooks/pre-push` is piped to
  `awk '/PP_READ_AT=\$sha/ {f=1; next} f && /(^|[;&|[:space:]])return([[:space:]]|;|$)/ {n++} END {print n+0}'`,
  it prints `0`.
  Red when: a return after `PP_READ_AT=$sha` lets a path skip the floor.
  figure: PINNED; 1 at 13e24816 (§4 probe 4).
- **AC8** — When the parity arm compares the hook's three orders with the `allowed` lists the
  catalogue rows in `tools/policy/catalogue.toml` give, each pair is equal as a set. The hook's
  `PP_POLICY_REL` equals `POLICY_REL` in `tools/policy/policy.py`.
  Red when: a value the catalogue adds is absent from the hook's order, or the file moves.
- **AC9** — When `grep -c 'WHAT THE FLOOR DOES NOT CHECK' .githooks/pre-push` runs, it prints `1`.
  `grep -c 'NO POLICY KIT reads the catalogue default' .githooks/pre-push` prints `0`.
  Red when: the header still says a missing kit reads the default whatever R declares.
- **AC10** — When `grep -n 'which the pre-push hook reads' help/policy.md` runs, it prints one line
  in the consumers list, and that bullet names `hooks.bypass`, `verdict.blocks` and `verdict.held`.
  Red when: the page still tells a reader the hook reads only the policy reader's answer.
- **AC11** — When `grep -c '"run_floor_read"' memory/map/generated/symbols.json` runs, it prints `1`.
  Red when: the map is not regenerated after the suite gains its helper.

## 7. Gates

`pre-push self-test` · `run-gates gov canary` · `measure-legs selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

`run-gates gov canary` and `measure-legs selftest` are owed for `.githooks/pre-push`, `policy fixtures`
for `help/policy.md`, and both recall legs for the map file under `memory/`. Each arm below is seen
red against today's hook first, and the A column and `real` row controls are seen green both times.
The suite's budget row in `tools/run-gates/selftest-budgets.txt` reads 1020s (PINNED 2026-11-21).
This unit adds one push fixture and about a dozen subshell reads, and the main loop re-reads the row at
the close.

New arm: .githooks/pre-push.test.sh · covers AC1 · the nopy plant over R and R3, red today at both · none
New arm: .githooks/pre-push.test.sh · covers AC2 · the nokit plant over R, red today · none
New arm: .githooks/pre-push.test.sh · covers AC3 · the broken plant over R, red today on held and bypass · none
New arm: .githooks/pre-push.test.sh · covers AC4 · the tampered plant over R, red today on all three keys · none
New arm: .githooks/pre-push.test.sh · covers AC5 · the nopy and real plants over R3, nopy red today · none
New arm: .githooks/pre-push.test.sh · covers AC6 · a refused BP fixture whose tip runs git rm on the policy reader, exit 0 today · none
New arm: .githooks/pre-push.test.sh · covers AC7 · the single-exit measure, 1 today · none
New arm: .githooks/pre-push.test.sh · covers AC8 · the order and path parity, red today since no order is declared · none

## 8. Open questions

- **F1 — Does an unconfirmed declaration at R refuse the push outright, or raise the key?** Options:
  (a) raise each key to the stricter of its base and R's floor, with no new refusal; (b) refuse
  outright whenever the reader's answer, or its absence, leaves a non-default R value unconfirmed,
  the skeptic's literal wording; (c) refuse outright only where no reader answered. (b) refuses
  whenever R's own state makes the honest reader differ: R invalid under `last-valid`, or under
  `refuse`. A push cannot move R, so no push could land the repair. (b) and (c) also add a refusal
  site that the census in `.githooks/pre-push.runlog.test.sh` counts, a new public token; veto 2
  discards both. (a) meets AC1 to AC8, and for `hooks.bypass` the raise to `refused` yields the
  `bypass-refused` refusal the review's left-shift gate asserts. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3, the one survivor.
  widens: none · relaxes: none
- **FACT-QUESTION · F2 — Which rank does `verdict.held` take in the floor?** Probe:
  `grep -n 'PP_HELD' .githooks/pre-push` outside `read_policy_at`. Observation: one consumer,
  `[ "$PP_HELD" = push-selected ]` at `@13e24816:2030`, so `push-selected` is the one value that runs
  more at this push and ranks strictest. `on-demand` and `peer-or-cadence` both export nothing there,
  so their mutual rank changes no hook behaviour; the order puts the catalogue default first.
  Liveness: a second consumer line would print and reopen the rank. RESOLVED (agent, 2026-11-21,
  delegated): `on-demand peer-or-cadence push-selected`.
  widens: none · relaxes: none
- **F3 — Does an unparsed mention raise a key the reader answered?** Options: (a) no, a `?` adds
  nothing over an answering reader; (b) yes, to K's strictest value. Under (b) probe 3's valid
  inline-table file, which the reader confirms as `allowed`, would read `refused`. Under `local-hook`
  nothing would land, and the respelling that clears it is itself a landing. That is a wrong result
  on a valid R and a refusal the pushed tree cannot clear, so (b) fails AC5's `real` half; veto 1
  discards it. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the one survivor; its residual
  is §5's tampered reader over an unparsed spelling.
  widens: none · relaxes: none
- **F4 — Where does the left-shift gate's every-exit requirement live?** Options: (a) a new
  `check-arms.py` predicate over the hook; (b) S3's single exit after `PP_READ_AT=$sha`, held by AC7's
  arm; (c) both. `check-arms.py` discovers only a `*.sh` defining `fail()`, which the hook is not
  (§4 Evidence). So (a) is a new population kind in another kit's gate, a separate unit by
  `doc.build-method#m2-the-spec-set-decompose-detect-classify-act`,
  outside this H1 fold. (b) makes the class structural for this function, and AC7 reds a new early
  return. RESOLVED (agent, 2026-11-21, delegated): (b), rung 3, the most feature-rich survivor; (a)
  is handed off in §3.
  widens: none · relaxes: none
- **F5 — Which binding line does a unit the closing review promoted carry?** Options: (a)
  `**Derived:**` naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of a repaired unit's clause. The
  three units whose code this changes are CLOSED and frozen, so (b) has no clause to split.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3, the precedent `TOOL-dWitnessedBar-96` §8 F1
  set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-21 · initial draft, promoted from the closing diff review's round 1, H1 (finding 1),
  per 2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-spec-writer, the handoff of
  2026-11-21-prompt-TOOL-dWitnessedBar-106-promotion-brief.

## 10. Reuse audit

The seam is `.githooks/pre-push#read_policy_at`, the one R-scoped policy read of the hook. S3
composes the floor inside it, and every caller keeps reading `PP_POLICY`, `PP_HELD` and `PP_BYPASS`.
The raw parse follows `.githooks/pre-push#read_policy_key`, which reads R's committed gate file with
`git show` and parses it without executing it; its grammar is an env assignment, not TOML, so it is
reused as a pattern and not called. `python tools/codebase-map/reuse_lookup.py "read a policy key value from committed raw toml bytes at a revision when the reader cannot answer"`
ranked `read_text`, `key`, `read`, `read_policy_value`, `read_catalogue_row` and `parse_key` on
2026-11-21. Each is Python, and the floor must run where no python resolves.
`tools/policy/policy-shim.sh` passes `get` through a resolved python. So no existing seam fits for the
bash TOML scan, and `scan_policy_bytes` is its first instance.

Recall terms used: `python tools/memory-recall/query.py "how does the pre-push hook read a policy key at R when the policy kit is missing or its reader fails" --terms "read_policy_at hooks.bypass verdict.blocks verdict.held fail closed catalogue default reader refusal raw bytes remote sha"`
