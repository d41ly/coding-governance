# TOOL-dTotalRecall-5 — the slug and id grammar exported once from `id_grammar.py` and read by every slug and id reader

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 7 · advances TOOL-dTotalRecall-27

**Carries:** cl-dClosedLoop-0216@f8936b35 whole
**Carries:** node:policy-key.builds.slug-words
**Carries:** node:policy-key.builds.slug-style
**Carries:** node:policy-key.builds.slug-date

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md](../build/2026-10-25-build-TOOL-dTotalRecall-1-reuse-scout-c.md) | research | TOOL-dTotalRecall-6 TOOL-dTotalRecall-11 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-17 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-agent-ledger.md) | journal | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-fix-return.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |
| [2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dTotalRecall-1-spec-stage-returns.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-3 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-10 TOOL-dTotalRecall-11 TOOL-dTotalRecall-12 TOOL-dTotalRecall-13 TOOL-dTotalRecall-14 TOOL-dTotalRecall-15 TOOL-dTotalRecall-16 TOOL-dTotalRecall-17 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-20 TOOL-dTotalRecall-21 TOOL-dTotalRecall-22 TOOL-dTotalRecall-23 TOOL-dTotalRecall-24 TOOL-dTotalRecall-25 TOOL-dTotalRecall-26 |
| [2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dTotalRecall-1-spec-fix-brief.md) | research | TOOL-dTotalRecall-1 TOOL-dTotalRecall-2 TOOL-dTotalRecall-4 TOOL-dTotalRecall-6 TOOL-dTotalRecall-7 TOOL-dTotalRecall-8 TOOL-dTotalRecall-9 TOOL-dTotalRecall-14 TOOL-dTotalRecall-18 TOOL-dTotalRecall-19 TOOL-dTotalRecall-21 TOOL-dTotalRecall-23 TOOL-dTotalRecall-26 |

<!-- /gen:spec-records -->

## 1. Goal

One slug grammar, declared by the three policy keys `builds.slug-words`, `builds.slug-style` and
`builds.slug-date` and derived once by `slug_grammar(root)` in the moved id-grammar module, is what
every slug and id reader in the tree reads, so an owner can change the grammar in one place and no
reader rejects a slug or id minted under it or before it (gap-mem-06). Today about fifteen readers in
seven kits each spell their own pattern, a digit date breaks six and a hyphenated date ten, and the
one setting that exists, `BUILD_SLUG_RE`, reaches check 4 alone (`layer-memory.md:531-560`).

## 2. Scope (IN)

- **S1** — `slug_grammar(root)` in `tools/memory-tree/id_grammar.py` (the module PLAY-dOrderedCharter-18
  S1 moves into memory-tree), returning the `SlugGrammar` of §4 "The grammar": `words`, `style`,
  `date`, the derived `BUILD_SLUG_RE`, the unanchored `slug_class`, the strict `mint_re` and the
  `record` string. It reads the three keys through `read_policy_value` (I8), the key literal first, and
  is cached per root. Observed by AC1 and AC2.
- **S2** — A changed grammar binds new mints only: `mint_re` is the grammar in force, and
  `BUILD_SLUG_RE` is the union of the legacy shape, the grammar in force and every grammar a build
  README records, so every reader accepts both an existing form and the new one. Observed by AC2.
- **S3** — Each new slug records the grammar in force at its minting: `render_new_build_readme`
  (`tools/memory-tree/gen_build_index.py:3969`) writes the front-matter key `slug-grammar:` with the
  value of §4 "The record", and `cmd_new_build` (`:4050`) checks the slug against `mint_re` in place of
  `backlog.SLUG_RE` (`:4069`). Observed by AC3.
- **S4** — The eras read the grammar: `_eras(node)` (today `tools/memory-recall/extract.py:136`, moved
  by PLAY-dOrderedCharter-18) builds its session era from `slug_class` instead of
  `[<node>][A-Za-z]{2,}`, so `grammar_for(root)`'s `ID_RE` parses an id whose slug carries an
  `in-slug` date in either form. Observed by AC4.
- **S5** — The export to shell and to JavaScript: `id_grammar.py --print slug-re|slug-class|slug-grammar`,
  and `check-memory-hygiene.sh --print-slug-re` and `--print-slug-class`, each running the module once
  through the script's resolved Python. Two `[[contract.clause]]` rows join the existing
  `memory-tree/hygiene-print-modes` contract of `tools/memory-tree/kit.toml`. The two workflow
  templates read a `{{SLUG_CLASS}}` placeholder, added to their `[[files]]` rows in
  `tools/workflows/kit.toml:62-79`; the kit's renderer, `check-protocol-parity.test.sh --render` (its
  `[[regenerate]]` row, `:115-116`), answers it from `check-memory-hygiene.sh --print-slug-class` the
  way it answers `FANOUT_CAP` from the hook's `--print-cap`, and with no memory-tree kit tracked it
  substitutes the legacy class and says so, as it already skips `MEMORY_TREE_DIR` out loud.
  Observed by AC5.
- **S6** — Check 4 reads the derived pattern: its awk binding `slugre`
  (`tools/memory-tree/check-memory-hygiene.sh:816`) takes `--print-slug-re`'s value, and the conf key
  `BUILD_SLUG_RE` is retired as an input: a non-blank value refuses with exit 2 naming the three policy
  keys. Observed by AC6.
  **Readers:** by name: `tools/memory-tree/check-memory-hygiene.sh` (the default at `:170`, the
  anchoring and empty-match refusals at `:216-228`, the declared-key loop at `:288`, check 4's binding
  at `:816`), `tools/memory-tree/.memory-tree.conf.example` (`:352-355`), `tools/memory-tree/kit.toml`
  (`optional_keys` at `:94`), `tools/memory-tree/check-memory-hygiene.test.sh` (`:3098-3124`) ·
  by value: check 4's folder-name predicate at `check-memory-hygiene.sh:816`, the only comparison of the
  value, which now reads the derived pattern instead.
- **S7** — Every reader the grammar's own search finds is re-pointed, by the disposition rule of §4
  "The readers". The search is `id_grammar.py --readers`, a predicate over tracked code, never an
  enumerated list; it is run at the pass before the first edit and after the last, and after the last
  it lists no site outside the grammar's own entry points. Observed by AC7.
- **S8** — The legacy fallback for a kit that does not require memory-tree: the canonical blocks
  `slug_legacy_py` and `slug_legacy_sh` in `id_grammar.py` and `check-memory-hygiene.sh`, each one
  constant, the legacy shape; inline Python copies in `tools/runlog/runlog_lib.py` and
  `tools/branch-reconcile/branch_reconcile.py`, inline shell copies in `tools/run-gates/run-gates.sh`
  and the workflows kit's renderer `tools/workflows/check-protocol-parity.test.sh`; two `PARITY_ROWS`
  rows in `tools/lib/resolve-python.test.sh`; and a `requires_if` row naming memory-tree in the
  runlog, branch-reconcile, run-gates and workflows kits' `kit.toml`. Observed by AC8.
- **S9** — The `shown` date: `SlugGrammar.label(slug, opened)` renders `<slug> (<opened>)` under
  `shown` and the bare slug under `none` and `in-slug`, and the generator's build-link texts in the
  LIVE and ledger rows (`gen_build_index.py:2098`, `:2127`, `:8146`) call it, so a date is rendered
  beside the slug and never inside an id. Under the default `none` every render is byte-identical.
  Observed by AC9.
- **S10** — The scratch-clone flip proof of the clause, `id_grammar.py --flip-probe <clone>`, over the
  six named flips of §4 "The flips". Observed by AC10.
- **S11** — The prose: `tools/memory-tree/HYGIENE.template.md`'s slug rule (rendered to
  `memory/HYGIENE.md:175`, "a fresh CamelCase adjective-noun, `[A-Za-z]` only") points at the three
  keys and `slug_grammar` instead of stating a shape. NOT OBSERVED by a criterion: a prose pointer,
  graded by the kit/dogfood parity leg at the close.

## 3. Non-goals (OUT)

- Moving `grammar_for`, `_eras` and the conf layer into memory-tree: PLAY-dOrderedCharter-18's. This
  unit extends the moved module and re-grounds on it as landed.
- The policy catalogue rows: TOOL-dGroundRules-1 S3 writes one row per v2 `[policies]` row, these
  three included, owner `dTotalRecall`. This unit is their first reader and adds no row.
- Generating a slug's words. `humorous` mints from a kit word list and `descriptive` from the plan
  record's title (`layer-memory.md:556-560`); no word list and no plan record kind exist, so the slug
  stays the owner's argument and the grammar checks its shape and records its style. The minting door
  is TOOL-dTotalRecall-2's.
- The slug claim ref and the ask-family counter: TOOL-dTotalRecall-3's.
- The front-matter schema that admits `slug-grammar:`: TOOL-dTotalRecall-4's. Until it lands front
  matter is open-world, so writing the key here refuses nothing.
- Renaming any existing slug or id, or rewriting any README to add the key: a README recording no
  grammar is read under the legacy shape.
- A gate over the reader population. The search is the inventory; the readers' own suites are the arms.

### Edges

- **hands-off** `TOOL-dTotalRecall-4` — `slug_grammar`, and the `slug-grammar:` front-matter key its
  schema admits as an authored key
- **hands-off** `TOOL-dTotalRecall-6` — `slug_grammar`, through whose `slug_class` a relation's slug
  and unit-id targets are parsed
- **hands-off** `TOOL-dTotalRecall-3` — `slug_grammar`, whose `mint_re` a slug claim checks before it
  pushes
- **hands-off** `TOOL-dTotalRecall-2` — `slug_grammar`, whose `mint_re` and `record` the door's
  `new build-readme` writes against
- **consumes-from** `TOOL-dTotalRecall-8` — `policy_value.py`, the memory-tree kit's `read_policy_value`
  adapter the three `builds.slug-*` keys are read through
- **consumes-from** external — PLAY-dOrderedCharter-18 S1's `tools/memory-tree/id_grammar.py` with
  `grammar_for`, `_eras` and the conf layer; TOOL-dGroundRules-1 S3's three catalogue rows and
  TOOL-dGroundRules-2's `policy.py get`, read through `read_policy_value` (PLAY-dOrderedCharter-19 S8,
  the contract of PLAY-dOrderedCharter-7 §4 "The policy reads")

## 4. Design

### The grammar

```python
SlugGrammar(words=(lo, hi), style, date, node, BUILD_SLUG_RE, slug_class, mint_re, record)
```

| Field | Source |
|---|---|
| `words` | `builds.slug-words`, `<lo>-<hi>` or `<n>` (read as `n-n`); default `1-3` |
| `style` | `builds.slug-style`, `humorous` or `descriptive`; default `humorous` |
| `date` | `builds.slug-date`, `none`, `shown` or `in-slug`; default `none` |
| `node` | the conf's node-tag class, the `_NODE` the eras already read |

One grammar `g` has the shape `<node-letter><date><word>{lo,hi}`, where a word is `[A-Z][a-z0-9]*`,
`<node-letter>` is one character of `[<node>]`, and `<date>` is empty unless `g.date` is `in-slug`, when
it is `\d{8}` or `\d{4}-\d{2}-\d{2}`, the digit and the hyphenated form. The date follows the node
letter, so a node's dated slugs sort by date. `style` is the minting source and never a shape
(`layer-memory.md:556`).

- `mint_re` is `^<shape of the grammar in force>$`.
- The legacy shape is `[<node>][A-Za-z]{2,}`, exactly the session era's slug part today
  (`tools/memory-recall/extract.py:136-160`). It is frozen and admits every slug and id in the tree:
  199 folders, 197 of two words and 2 of three, and 269 distinct cited slugs of which only the fixture
  slug `fixture` fails the strict one-to-three-word shape (PINNED, measured 2026-10-26 at `fb872a37e`).
- `slug_class` is the alternation of the legacy shape, the shape of the grammar in force, and the
  shape of every distinct grammar a tracked `memory/builds/*/README.md` records in `slug-grammar:`,
  in that order, deduplicated. `BUILD_SLUG_RE` is `^(?:<slug_class>)$`.

A README recording no `slug-grammar:` is a legacy README and is read under the legacy shape alone.
The recorded grammars are read from the front matter of the tracked READMEs once per process and
root, with `tree_lib.read_text`; a value that does not parse as §4 "The record" refuses by path.

### The record

`slug-grammar: words=<lo>-<hi> style=<style> date=<date>`, one line in the README's front matter,
written by `render_new_build_readme` directly after `slug:`. `SlugGrammar.record` renders it, and
`parse_slug_grammar(value)` is its one reader.

### The policy reads

The three keys are read with `read_policy_value("builds.slug-words", root)` and its two siblings, each
the key literal first. memory-tree's thin adapter `tools/memory-tree/policy_value.py` is built to the
contract of PLAY-dOrderedCharter-7 §4 "The policy reads": its own inline `resolve_kit_dir` block,
`policy.py get <key> --explain` run in `root`. TOOL-dTotalRecall-8 (order 3) creates it (its S10),
and this unit calls it and never creates it. A `PolicyRefused` because no policy kit resolves
applies the three v2 defaults above and prints one line, `slug grammar: no policy kit, the defaults
apply`; any other refusal, an exit 2 from `get`, refuses the caller by naming the key.

### The readers

The inventory is derived, never typed. `id_grammar.py --readers [<root>]` lists every line of a
tracked `*.py`, `*.sh` or `*.js` file under `tools/`, `skills/` and `.githooks/` that spells a slug
class followed by a hyphen and a digit class, `\d`, `[0-9]` or `[1-9]`, with at most a group's closing
and opening parenthesis between them (the id shape; `cmd_new_spec`'s
`gen_build_index.py:8590` is one such), or binds a name containing `SLUG` or
`slug` to a regex literal (the slug shape), outside the grammar's own entry points. Its id-shape half, in a
narrower form with no parenthesis between, found 58 lines in 26 files at `fb872a37e` (PINNED, measured
2026-10-26), among them every site scout C listed (`backlog.py:129`, `roles_lib.py:77`,
`unattended.sh:2890`, `runlog_lib.py:52`, `tree_lib.py:222`, `:432`, `:443`, `handoff.py:104`, `:122`,
`branch_reconcile.py:510`, `merge-rows.py:421`, `runlog/record.py:141`, `runlog/model.py:1456`,
`check-spec-tokens.py:387`, `gen_build_index.py:3162`, `check-memory-hygiene.sh:1833`,
`run-gates.sh:4916`) and the JavaScript `reviewSlug` (`tools/workflows/tier2-review.template.js:303`).

Each hit takes one disposition; the pass commit's `Decided:` trailer names any hit kept and why.

| The reader sits in | It reads the grammar through |
|---|---|
| memory-tree | a sibling import of `id_grammar` |
| a kit that requires memory-tree (roles, unattended's Python, memory-recall) | that kit's existing `resolve_kit_dir` copy, as PLAY-dOrderedCharter-18 S3 reaches the module |
| a repo-root tool (`tools/check-spec-tokens.py`) | its `resolve_kit_dir` copy |
| a kit that does not require memory-tree (runlog, branch-reconcile, run-gates) | its `resolve_kit_dir` copy; where memory-tree does not resolve, its inline `slug_legacy_*` block and one stderr line, `slug grammar: memory-tree not installed, the legacy shape applies` |
| shell (unattended, push-main, run-gates, the hygiene script) | `check-memory-hygiene.sh --print-slug-class` or `--print-slug-re`, resolved once per run |
| a workflow template | the `{{SLUG_CLASS}}` render token |

A hit that is not a slug or id reader at all (a scratch-path or agent-type shape the predicate's slug
half catches) is recorded as kept. Each re-pointed site keeps its own name (`SLUG_RE`, `UNIT_RE`,
`ID_RE`, `check_slug_shape`), bound from the grammar at first use, so no name retires and its callers
do not change.

### The flips

`id_grammar.py --flip-probe <clone>` runs in a scratch clone of the repository the pass makes under
`%TEMP%/<short>`. For each flip it writes `.governance/policy.toml` with the flipped key, plants one
README `memory/builds/<slug>/README.md` whose front matter records the flipped grammar, and checks
four things: the flip's new slug passes `mint_re`; a legacy two-word slug that the flipped grammar
does not admit fails `mint_re` and passes `BUILD_SLUG_RE`; every tracked folder name passes
`BUILD_SLUG_RE`; and `grammar_for(<clone>).ID_RE` matches `TOOL-<new slug>-3` whole with `3` as its
sequence. It prints one `flip <name>: ok` or `flip <name>: <which check failed>` line each and exits 1
on any failure.

| Flip | Key value | New slug planted |
|---|---|---|
| `slug-words` 1 | `builds.slug-words = "1"` | `dLoop` |
| `slug-words` 3 | `builds.slug-words = "3"` | `dClosedLoopTwo` |
| `slug-style` `descriptive` | `builds.slug-style = "descriptive"` | `dClosedLoop` |
| `slug-date` `shown` | `builds.slug-date = "shown"` | `dClosedLoop` |
| `slug-date` `in-slug`, digit | `builds.slug-date = "in-slug"` | `d20261026ClosedLoop` |
| `slug-date` `in-slug`, hyphenated | `builds.slug-date = "in-slug"` | `d2026-10-26ClosedLoop` |

Under `descriptive` and `shown` the shape does not change, which the probe states, and the `shown`
row also asserts `label` renders `dClosedLoop (2026-10-26)`. The readers' own self-tests over the
flipped clone are the suites of §7, run at the close.

### Inventory

Minted: `slug_grammar`, `SlugGrammar`, `parse_slug_grammar`, `SlugGrammar.label`, the CLI flags
`--print`, `--readers`, `--flip-probe` and `--mint-check` of `id_grammar.py`; the print modes
`--print-slug-re` and `--print-slug-class`; the front-matter key `slug-grammar`; the render token
`{{SLUG_CLASS}}`; the blocks `slug_legacy_py` and `slug_legacy_sh` and their `PARITY_ROWS` rows.
Naming cells: `slug_grammar` and
`parse_slug_grammar` are asked of the lexicon's `--suggest` under `--as py.function` at the pass.

### Migration

None for records. The conf key `BUILD_SLUG_RE` is blank in gov's own conf, so retiring it changes
nothing here; an adopter that set it is refused by name (S6) and moves the value to the three keys,
which TOOL-dTotalRecall-20's upgrade steps may grade.

### Files touched (estimate)

- `tools/memory-tree/id_grammar.py`
- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/.memory-tree.conf.example`
- `tools/memory-tree/kit.toml`
- `tools/memory-tree/HYGIENE.template.md` (the source), `memory/HYGIENE.md` (its render)
- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/tree_lib.py`
- `tools/memory-tree/row_grammar.py`
- `tools/memory-tree/merge-rows.py`
- `tools/memory-tree/migrate_backlog.py`
- `tools/memory-tree/deviation_join.py`
- `tools/memory-tree/routed_commits.py`
- `tools/memory-tree/check-arms.py`
- `tools/memory-tree/design_lib.py`
- `tools/memory-recall/extract.py` (its re-export of the moved eras)
- `tools/roles/roles_lib.py`
- `tools/roles/handoff.py`
- `tools/runlog/runlog_lib.py`
- `tools/runlog/record.py`
- `tools/runlog/model.py`
- `tools/runlog/kit.toml`
- `tools/branch-reconcile/branch_reconcile.py`
- `tools/branch-reconcile/kit.toml`
- `tools/check-spec-tokens.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.sh`
- `tools/unattended/check-pass-order.sh`
- `tools/unattended/check-brief-recorded.sh`
- `tools/push-main.sh`
- `tools/run-gates/run-gates.sh`
- `tools/run-gates/kit.toml`
- `tools/workflows/tier2-review.template.js` (the source), `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/unattended-build.template.js` (the source), `tools/workflows/unattended-build.js` (its render)
- `tools/workflows/kit.toml`
- `tools/workflows/check-protocol-parity.test.sh` (the renderer's `--render` mode)
- `tools/lib/resolve-python.test.sh`

The search of §4 "The readers" re-derives this list at the pass; a hit outside it joins the pass's
`--dispatch --writes` set before its edit.

### Alternatives rejected

- **`BUILD_SLUG_RE` strictly the grammar in force.** A flip to one word would red every two-word
  folder, which the clause forbids ("existing slugs and ids keeping their form").
- **A permissive closure over every legal value.** `builds.slug-words` takes any word range, so the
  closure is unbounded, and a reader would no longer follow the keys at all.
- **Each kit declaring `requires = ["memory-tree"]`.** It adds an install dependency to three kits
  whose adopters may run them alone; the inline legacy block keeps them independent, as the
  `remote_ladder_py` copies do.

## 5. Production-readiness checklist

- security — no write path beyond the README key the scaffold already writes; every policy value is
  parsed by `parse_slug_grammar` and a value outside its grammar refuses before it reaches a regex.
- perf / scale — the README scan reads about 200 front matters once per process and root; the print
  modes add one Python start per shell run.
- error / empty / loading states — no policy kit applies the defaults and says so; memory-tree absent
  applies the legacy shape and says so; a malformed recorded grammar refuses by path.
- observability — `--print slug-grammar` prints the grammar in force and every recorded grammar.
- risks — a reader the search cannot see (a pattern built at runtime) keeps its own spelling; the
  search's population is printed so the pass can read it, and the flip probe is the backstop.
- testing — AC1 to AC10 by a pass; the arms of §7 at the close.
- migration — none for records; a set conf `BUILD_SLUG_RE` is refused by name.
- user docs — none under `help/`: no page names the slug grammar; S11 updates the hygiene prose.

## 6. Acceptance criteria

- **AC1** — When `python id_grammar.py --print slug-grammar` runs from `tools/memory-tree/` at the pass
  tip with no `builds.slug-*` key set, it prints `words=1-3 style=humorous date=none`, and
  `--print slug-re` prints a pattern every tracked build folder name matches.
  Red when: the defaults are read wrongly, or the derived pattern rejects an existing folder.
- **AC2** — When a probe sets `builds.slug-words = "1"` in a scratch clone and calls `slug_grammar`,
  `mint_re` refuses `dTotalRecall` and admits `dLoop`, and `BUILD_SLUG_RE` admits both.
  Red when: `BUILD_SLUG_RE` is the grammar in force alone, so the existing two-word slug is refused.
  fixture: a scratch clone under `%TEMP%/<short>`; the tree holds none today.
- **AC3** — When a probe imports `gen_build_index` and calls `render_new_build_readme` for slug
  `dLoop`, its front matter carries `slug-grammar: words=1-3 style=humorous date=none` on the line after
  `slug:`; when `cmd_new_build` is handed `d2026-10-26Loop` under the default grammar, it refuses
  naming `mint_re`'s grammar before any write.
  Red when: the key is absent, or the scaffold still checks `backlog.SLUG_RE`.
- **AC4** — When `grammar_for(<clone>).ID_RE` is applied, in a clone whose one planted README records
  `date=in-slug`, to the line `see TOOL-d2026-10-26Loop-3 and TOOL-dTotalRecall-5`, it finds exactly
  those two ids.
  Red when: the session era keeps `[<node>][A-Za-z]{2,}`, so the hyphenated id matches nothing or a
  fragment.
- **AC5** — When `check-memory-hygiene.sh --print-slug-re` and `python id_grammar.py --print slug-re`
  run in the same tree, their outputs are byte-equal, and the same holds for `--print-slug-class`; and
  the workflows kit's `[[regenerate]]` render, run in a scratch clone, writes
  `tools/workflows/tier2-review.js` with no `{{SLUG_CLASS}}` left and the class spliced into its
  `PIN_ID`.
  Red when: the shell export re-derives the pattern instead of asking the module, or the renderer
  leaves the placeholder unsubstituted.
- **AC6** — When `check-memory-hygiene.sh --print-slug-re` runs in a scratch clone whose
  `.memory-tree.conf` sets `BUILD_SLUG_RE="^[a-z]+$"`, it exits 2 naming `BUILD_SLUG_RE`,
  `builds.slug-words`, `builds.slug-style` and `builds.slug-date`.
  Red when: the conf value is still read, so the slug grammar has two carriers.
- **AC7** — When `python id_grammar.py --readers` runs at the pass tip, it lists no line outside the
  grammar's entry points; when a scratch clone gains a planted `x.py` in its tools directory holding
  `re.compile(r"[A-Z]+-[A-Za-z]+-[0-9]+")`, it lists that line.
  Red when: the predicate misses the planted id-shape spelling, or the tip still holds an un-re-pointed
  reader.
  figure: the 58 lines in 26 files at `fb872a37e` are PINNED for the narrower form; the pass re-derives the before-count
  with the same command at its base.
- **AC8** — When `tools/memory-tree` is renamed away in a scratch clone and a probe calls runlog's
  slug reader in `tools/runlog/runlog_lib.py` on `dTotalRecall`, it accepts the slug and prints
  `slug grammar: memory-tree not installed, the legacy shape applies` once; and when the
  `slug_legacy_py` block is cut with the parity arm's `blk` awk range from `id_grammar.py` and from
  `runlog_lib.py`, the two are identical.
  Red when: the fallback raises, or a copy of the block drifts from its canonical.
- **AC9** — When a probe calls `SlugGrammar.label("dClosedLoop", "2026-10-26")`, it returns
  `dClosedLoop (2026-10-26)` under `shown` and `dClosedLoop` under `none`; and
  `gen_build_index.py --write` in a scratch clone of the pass tip under the default leaves
  `git status --porcelain` empty.
  Red when: `shown` puts the date into an id, or `none` changes a rendered byte.
- **AC10** — When `python id_grammar.py --flip-probe <clone>` runs over a scratch clone of the pass
  tip, it prints `flip <name>: ok` for each of the six flips `slug-words` 1 and 3, `slug-style`
  `descriptive`, `slug-date` `shown`, and `in-slug` in a digit and a hyphenated form, and exits 0.
  Red when: the session era is restored to `[<node>][A-Za-z]{2,}`, which turns both `in-slug` rows red.
  cost: one clone and six policy writes, about a minute.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `memory-recall kit selftest` · `branch-reconcile selftest` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `routed-commits selftest` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `verifier fan-out self-test` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `pass-order history` · `brief-recorded` · `push-main self-test` · `roles render selftest` · `spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `review-protocol parity (kit vs dogfood)` · `kit placeholders (a declared token its adopter substitutes)`

New arm: tools/lib/resolve-python.test.sh · covers AC8 · the `slug_legacy_py` and `slug_legacy_sh` parity rows, staged by one byte changed in the run-gates copy · that suite's assertion count, raised by the two rows
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC5 AC6 · the `BUILD_SLUG_RE` arms at `:3098-3124` rewritten: a set conf value refuses naming the three keys, and check 4 reds a planted folder `d_bad` the derived pattern refuses, staged by restoring the conf read · none
New arm: tools/memory-tree/gen_build_index.py · covers AC3 AC9 · its `--selftest` gains the `slug-grammar:` line in a scaffolded README and the `shown` label, staged by dropping the key from `render_new_build_readme` · none

## 8. Open questions

- **F1 — What does `BUILD_SLUG_RE` admit once a grammar changes?** Options: (a) the grammar in force
  alone; (b) a closure over every legal value; (c) the union of the legacy shape, the grammar in force
  and every grammar a README records. (a) fails the clause's "existing slugs and ids keeping their
  form"; (b) is unbounded, since the words key takes any range, and stops following the keys.
  RESOLVED (agent, 2026-10-26, delegated): (c), rung 1, the clause's "every reader accepting both and
  each slug recording the grammar in force at its minting". widens: none · relaxes: none
- **F2 — How does a reader in a kit that does not require memory-tree reach the grammar?** Options:
  (a) add `requires = ["memory-tree"]` to runlog, branch-reconcile and run-gates; (b) reach it through
  each kit's `resolve_kit_dir` and fall back to an inline, parity-gated legacy block with a named line;
  (c) keep those readers' own patterns. (c) fails the clause; (a) adds an install dependency to three
  kits, a public-surface change the grant covers but no acceptance criterion needs. RESOLVED (agent,
  2026-10-26, delegated): (b), rung 3, tie-broken by reuse of the inline-copy seam `PARITY_ROWS`
  already carries. widens: none · relaxes: none
- **F3 — Is the conf key `BUILD_SLUG_RE` kept as an override?** Options: (a) retire it as an input and
  refuse a set value by name; (b) keep it beside the keys. (b) leaves two carriers for one grammar.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, `layer-memory.md:542-543` ("so the slug grammar
  has one carrier"), named by cl-0216's "`BUILD_SLUG_RE` derived from the `builds.slug-*` keys".
  grants: PLAY-dClosedLoop-3 retiring a declared conf key of the memory-tree kit. widens: none ·
  relaxes: none
- **F4 — What does `shown` change, given every view already renders `opened`?** Options: (a) a label
  `<slug> (<opened>)` on the generator's build-link texts, byte-neutral under `none`; (b) nothing.
  (b) makes `shown` and `none` the same value, which the key's three values deny. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, `layer-memory.md:553-554` ("rendered from `opened:` beside the
  slug in every view, never inside an id"). widens: none · relaxes: none
- **F5 — Where does an `in-slug` date sit, and in which forms?** Options: (a) after the node letter,
  `\d{8}` or `\d{4}-\d{2}-\d{2}`; (b) after the words. (b) puts digits directly before the id's
  `-<seq>`, where a hyphenated date makes `-26-3` read as two sequences to every reader that splits on
  the last hyphen. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the forms the slug research's
  reader census probed (`research-memory-builds.md:92`). widens: none · relaxes: none
- **F6 — The parents are specced and not built.** PLAY-dOrderedCharter-18's module and
  TOOL-dGroundRules-1/-2's policy rows and reader are DEFERRED at `462d20f3`. RESOLVED (agent,
  2026-10-26, delegated): this spec calls them as their specs name them, and the build run re-grounds
  on the landed code, rung 1 (the brief's chain rule). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 5, the brief's shared interfaces I7 and
  I8, scout C's row for cl-0216, and the readers read at `fb872a37e`.

## 10. Reuse audit

The seam extended is the moved id grammar, `grammar_for` and `_eras` (`tools/memory-recall/extract.py:572`
and `:136` at HEAD, `tools/memory-tree/id_grammar.py` once PLAY-dOrderedCharter-18 lands), plus the
hygiene script's print-mode export (`check-memory-hygiene.sh:375-389`) and its `[[contract]]` rows
(`tools/memory-tree/kit.toml:443-455`), and the inline-copy mechanism `PARITY_ROWS`
(`tools/lib/resolve-python.test.sh:168`). The lookup,
`python tools/codebase-map/reuse_lookup.py "derive one slug and id pattern from configured grammar keys and export it to every reader"`,
ranked `grammar_for` and `grammar` (`corpus_ids.py`) as SEAMs with fan-in 8, `build_grammar`
(`backlog.py:178`), `read_conf_key` and `build_unit_id_re` (`runlog/model.py:1456`); it did not list
`check_slug_shape`, `SLUG_RE` or `reviewSlug`, which a regex-literal search found instead (the search
§4 "The readers" formalises). The recall probe returned scout C's row, the layer's `[names]`, the
fold brief's C3-F10 (the new-mints-only rule, carried here as S2) and the slug research's reader
census; none disagreed with source, except that the census's line numbers (`roles_lib.py:75`,
`tier2-review.js:296`) have moved to `:77` and `:303`.

Recall terms used: `python tools/memory-recall/query.py "where is the build slug pattern spelled and which readers parse slugs and ids" --terms "BUILD_SLUG_RE slug grammar grammar_for id_grammar SLUG_RE check 4 adjective-noun node tag era readers"`
