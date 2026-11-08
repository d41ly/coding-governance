# PLAY-dOrderedCharter-65 — the three kinds whose name is a namespace word are renamed under a qualifier, and every reader follows

**Status:** CLOSED · rev-1 · 2026-11-04 · node d · Tier-2 · base 40427f33 · streams playbook · order 11 · advances PLAY-dOrderedCharter-38

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md](../build/2026-10-25-build-PLAY-dOrderedCharter-1-agent-ledger.md) | journal | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-27 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-33 PLAY-dOrderedCharter-34 PLAY-dOrderedCharter-35 PLAY-dOrderedCharter-36 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-39 PLAY-dOrderedCharter-40 PLAY-dOrderedCharter-41 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-43 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-46 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-49 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-52 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-54 PLAY-dOrderedCharter-55 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 PLAY-dOrderedCharter-67 PLAY-dOrderedCharter-68 PLAY-dOrderedCharter-69 PLAY-dOrderedCharter-70 PLAY-dOrderedCharter-71 |
| [2026-11-04-build-PLAY-dOrderedCharter-65-1-builder-return.md](../build/2026-11-04-build-PLAY-dOrderedCharter-65-1-builder-return.md) | journal | — |
| [2026-11-04-build-PLAY-dOrderedCharter-65-ledger.md](../build/2026-11-04-build-PLAY-dOrderedCharter-65-ledger.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-65-1-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-65-2-spec-writer.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-2-spec-writer.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-65-build-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-build-brief.md) | journal | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-65-kind-rename-fold-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-kind-rename-fold-brief.md) | research | — |
| [2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief.md](../prompts/2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief.md) | research | — |
| [2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md](../reviews/2026-11-05-review-PLAY-dOrderedCharter-1-closing-diff-review-round1.md) | diff-review | PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-10 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-16 PLAY-dOrderedCharter-17 PLAY-dOrderedCharter-18 PLAY-dOrderedCharter-19 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-22 PLAY-dOrderedCharter-24 PLAY-dOrderedCharter-25 PLAY-dOrderedCharter-26 PLAY-dOrderedCharter-28 PLAY-dOrderedCharter-42 PLAY-dOrderedCharter-44 PLAY-dOrderedCharter-45 PLAY-dOrderedCharter-47 PLAY-dOrderedCharter-48 PLAY-dOrderedCharter-50 PLAY-dOrderedCharter-51 PLAY-dOrderedCharter-53 PLAY-dOrderedCharter-61 PLAY-dOrderedCharter-62 PLAY-dOrderedCharter-63 PLAY-dOrderedCharter-64 |

<!-- /gen:spec-records -->

## 1. Goal

Unit 7's `tools/playbook/kinds.toml` registers `kind.kit`, `kind.layer` and `kind.practice`. `kit`, `layer`
and `practice` are words `tools/playbook/namespaces.toml` registers, so the shape arm
(`tools/playbook/tag_index.py#check_tag_shape`) and the lexicon name-check
(`tools/lexicon/lexicon.py#check_tag_name`) each refuse all three, for six reds on the tags leg. This
repair renames the three kinds so each first segment names no namespace, and moves every reader in the
same pass, so `python tools/playbook/gov_tag.py check` exits green over the tree. Unit 7 is CLOSED, so
the fix is a repair unit and not an edit of unit 7.

## 2. Scope (IN)

Every line below was read at HEAD `40427f33c`.

- **S1** — The three rows of `tools/playbook/kinds.toml`, renamed. This item retires the tags `kind.kit`,
  `kind.layer` and `kind.practice`. Their names become `kind.tool-kit`, `kind.product-layer` and
  `kind.charter-practice`, the spelling the fork record settles. The practice row's `factory` becomes
  `python {prefix}/playbook/core.py new charter-practice`, because `core.py new <kind>` finds its row as
  `kind.<kind>` (`tools/playbook/core.py#read_kind_row`). Each row keeps its `owner`, `binds`,
  `population` and `gate`, and the layer row keeps its `factory`. The tag index has no cached row to
  edit. It is derived, never committed, and keyed by blob (`tools/playbook/tag_index.py`, module
  docstring), so the next build parses the new `kinds.toml` blob through
  `tools/playbook/tag_index.py#extract_kind`. Observed by AC1, AC2 and AC3.
  **Readers:**
  by name: `tools/playbook/kinds.toml` `tools/playbook/core.py` `tools/playbook/core-pending.txt`
  `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-10.md`
  by value: `tools/playbook/core.py` (`read_kind_row` matches `kind.<word>`; `run_kinds` joins the
  pending rows to the register), `tools/playbook/tag_index.py` (`extract_kind` takes the members,
  `check_tag_shape` grades them), `tools/playbook/gov_tag.py` (`run_name_check` passes them to the
  lexicon), `tools/lexicon/lexicon.py` (`check_tag_name`).
- **S2** — The rule, stated where kinds are added. The comment block at the head of
  `tools/playbook/kinds.toml` gains one sentence. A kind's name is never a namespace word. Where a kind's
  members form a namespace, its name puts a qualifier before that word, naming where the population
  lives. The `<kind>` that `core.py new` takes is that name. Observed by AC7.
- **S3** — The pending row follows S1. In `tools/playbook/core-pending.txt`, the row
  `kind TAB kind.kit TAB dShippedRelease` becomes `kind TAB kind.tool-kit TAB dShippedRelease`. The row
  count stays at 14 kind rows. Observed by AC5.
- **S4** — `tools/playbook/core.py` follows S1.
  - `run_practices` reads its row through `read_kind_row(root, kit_rel, "charter-practice")`, and its
    absent-row red names `kind.charter-practice`.
  - `run_new` compares its own-factory word with `"charter-practice"` where it compares `"practice"`
    today. `OWN_FACTORY`'s `[a-z-]+` already admits the hyphen.
  - `write_fixture`'s register rows become `kind.charter-practice`, with factory
    `python {prefix}/playbook/core.py new charter-practice`, and `kind.product-layer`. The fixture's pending
    row becomes `kind TAB kind.product-layer TAB dFx`.
  - `arm_practice` calls `run_new_in(["charter-practice", "demo", "--line", "x"])`. Its label becomes
    `practice: new charter-practice demo --line x`. Its needle `appended practice.demo` is unchanged,
    because members stay in the `practice` namespace.

  The verb `core.py kinds practice` and its dispatch in `main` are unchanged. Observed by AC4, AC5 and AC6.

## 3. Non-goals (OUT)

- **The tag grammar.** `check_tag_shape`, `check_tag_name`, `tools/playbook/README.md`'s grammar paragraph
  and `help/tags.md`'s rule text do not change. This is the first fork's loser.
- **The verb word of the practice population gate.** `core.py kinds practice` is the argv of the leg
  `core practices conformance` in `tools/gate-legs.json`. Its `[[exempt_leg]]` row in
  `tools/govkit/registry.toml` quotes that argv. Unit 7's commit `399788aca` decided the verb words. A
  gate verb is not a kind name, so the third fork's rule does not reach it.
- **The `kit`, `layer` and `practice` namespaces and their members.** `practice.demo` is still what the
  factory appends, and no `layer.*` or `kit.*` tag moves.
- **Other builds' specs.** Three DEFERRED specs of dShippedRelease spell names that S1 retires:
  - `memory/builds/dShippedRelease/spec/2026-10-30-spec-DEPL-dShippedRelease-10.md` spells `kind.kit` in
    its S5, in its kind-row block and in its AC6. That AC's `grep -c "kind.kit"` would count nothing
    after S1 and pass for no reason.
  - The DEPL-dShippedRelease-15 and DEPL-dShippedRelease-78 specs spell `core.py new kit`.

  The main loop rewrites their text as an outside write of this run, in this pass, with a rev bump on
  each. That rewrite is not this unit's diff. Their citations sit under `memory/builds/`, which the
  resolver counts and never grades (`tools/playbook/tag_index.py#check_resolves`), so they add no red
  to the tags leg in the meantime.
- **`kind.item` and `kind.role`.** Neither is red at HEAD. Each goes red when its namespace is
  registered: `item` by dDeclaredLoop and `role` by dBoundRoles (`tools/playbook/README.md`, the table
  of later namespaces). The shape arm names the row at that registration, and the registering build
  renames it under S2's rule. That is a follow-up for those builds and not part of this unit.
- **A kit version move.** The playbook-render kit ships `tools/playbook/` through its `**` include
  (`tools/playbook/kit.toml`). Unit 7's commit `399788aca` landed these three files without touching
  `render_playbook.py`'s version constant, and this unit follows that precedent.

### Edges

none

## 4. Design

### The renames

| Retired | New | `core.py new` word | Why the qualifier |
|---|---|---|---|
| `kind.kit` | `kind.tool-kit` | `tool-kit` | its population is `{prefix}/*/kit.toml`, a kit under the tool root |
| `kind.layer` | `kind.product-layer` | `product-layer` | `layers.toml` is "the product's layer register" (its header) |
| `kind.practice` | `kind.charter-practice` | `charter-practice` | `practices.toml` is the charter's practice catalogue, rendered into the charter |

In each name the head noun stays the namespace word, so the name still says what a member is. The
owner's precedent goes the same way: the systems record renamed a colliding segment rather than relax
the rule (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`, its
Grammar bullet: `adopter` for `repo`, and `policy-file.*` for `policy.*`). None of `tool-kit`,
`product-layer` or `charter-practice` opens with a word the registry holds today. None opens with a word
the later-namespace table names either (`step`, `item`, `policy`, `role`, `record`).

### The register's new lines

```toml
[[kind]]
tag = "kind.tool-kit"
owner = "dShippedRelease"
binds = ["principle.p16"]
population = "{prefix}/*/kit.toml"
factory = ""
gate = ""
```

```toml
[[kind]]
tag = "kind.charter-practice"
owner = "dOrderedCharter"
binds = ["principle.p14", "principle.p16"]
population = "{prefix}/playbook/practices.toml"
factory = "python {prefix}/playbook/core.py new charter-practice"
gate = "core practices conformance"
```

The layer row changes its `tag` line alone. Row order in the file is unchanged.

### The probes

AC2 and AC3 read the resolver's JSON summary. That is `gov_tag.py check --json`, which is not the
tags leg's argv. The summary's `reds` list holds the shape reds and the name-check reds alike
(`tools/playbook/gov_tag.py#run_check`). A line printed before the JSON is skipped:

```bash
reds() { python -c "import json,re,sys; s=sys.stdin.read(); r=json.loads(s[re.search(r'(?m)^\{', s).start():])['reds']; print(len(r)); [print(x) for x in r]"; }
```

The old-spelling fixture for AC3 runs from the repo root at the pass tip. It is a detached worktree of
the tip with one row re-spelled and left uncommitted. The index serves a worktree its own dirty paths
(`tools/playbook/tag_index.py`, the `dirty_path` table), so the re-spelled row is graded:

```bash
w="$(mktemp -d)/w"; git worktree add -q --detach "$w" HEAD
( cd "$w" && sed -i 's/^tag = "kind.tool-kit"$/tag = "kind.kit"/' tools/playbook/kinds.toml \
  && python tools/playbook/gov_tag.py check --json | reds
  git checkout -q -- tools/playbook/kinds.toml && python tools/playbook/gov_tag.py check --json | reds )
git worktree remove --force "$w"
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `kind.tool-kit`, `kind.product-layer`, `kind.charter-practice` | `kind` namespace tags, rows of `kinds.toml` | `tag.kind`, each graded OK by `lexicon.py --tags` (this writer, at `40427f33c`) |
| `tool-kit`, `product-layer`, `charter-practice` | the `<kind>` argument of `core.py new` | the same segments |

### Migration

None. `core.py` and the register are gov's own, and the four core legs that read them are gov-only
`[[exempt_leg]]` rows of `tools/govkit/registry.toml`. No adopter carries a `kind.*` row.

### Rollout

Live at landing. The tags leg drops from six reds to none, and no other leg's verdict moves.

### Files touched (estimate)

- `tools/playbook/kinds.toml`: S1, S2
- `tools/playbook/core-pending.txt`: S3
- `tools/playbook/core.py`: S4

### Alternatives rejected

- **A kind-scoped exception to the first-segment rule.** This is the first fork's loser (B).
- **Renaming the `kit`, `layer` and `practice` namespaces.** This is the first fork's third option (C).
- **A `retired` row for each old tag.** The `kind` extractor reads `tag` rows only
  (`tools/playbook/tag_index.py#derive_tag_rows`). The only citations of the old tags are build records
  and specs under `memory/builds/`, which the resolver counts and never grades.

## 5. Production-readiness checklist

- security: N/A. The change renames rows and literals. It adds no write path, input or surface. `core.py new`
  still refuses a word the register lacks before it writes anything (`run_new`).
- perf / scale: N/A. Three rows and one pending row change. The index re-parses one blob.
- error / empty / loading states: a retired word passed to `core.py new` prints
  `refused · kind.<word> is no kind the register holds` and exits 2 (AC6). A register that lacks the
  practice row reds `kinds practice` with the new tag in its message (S4).
- observability: the tags summary line `tags: green · 0 red` and the `core: kinds · 17 registered,
  14 pending` line (AC5).
- risks: a caller still typing `core.py new kit` or `new practice` is refused, not silently served. The
  three dShippedRelease specs are the known callers (the other builds' specs non-goal). The lexicon's
  noun canon maps none of `tool`, `product` or `charter` to another representative
  (`tools/lexicon/canon.py#build_form_index` returns none for each, probed by this writer). So the
  vocabulary check of TOOL-dMindYourWords-13, which has not been built, has nothing to refuse in them.
- testing: AC1 to AC7 by a pass. The `core selftest` leg re-runs S4's fixture rows at the close.
- migration: none (Migration, above).
- user docs: N/A. No page under `help/` spells the three tags or `core.py new`. `help/tags.md` states the
  grammar, which does not change.

## 6. Acceptance criteria

- **AC1** — When the tags the register holds go to the lexicon, through
  `python -c "import tomllib;print('\n'.join(r['tag'] for r in tomllib.load(open('tools/playbook/kinds.toml','rb'))['kind']))" | python tools/lexicon/lexicon.py --tags`,
  the run exits 0 and prints `lexicon: tags · 17 graded, 0 refused`.
  Red when: a row still opens with a namespace word. At HEAD the run exits 1 with `17 graded, 3 refused`
  and names `kind.kit`, `kind.practice` and `kind.layer`.
  figure: 17 is DERIVED from the register's row count; the 3 refusals at HEAD are PINNED at `40427f33c`.
- **AC2** — When `python tools/playbook/gov_tag.py check --json | reds` runs from the repo root at the pass
  tip, with `reds` the shell function from the Design section's probes, it prints `0` and no red line.
  Red when: a shape red or a name-check red remains. At HEAD the main loop's lint found six, three
  `· shape ·` and three `name-check ·` lines, one pair per retired tag.
  figure: six at HEAD is PINNED from the repair brief; the tip's count is DERIVED.
  permission: a role agent's scratch guard refuses this run, so the main loop observes it.
- **AC3** — When the Design section's old-spelling fixture runs, its first summary prints `2`, then one
  red carrying `· shape · kind.kit · first segment 'kit' is a namespace word` and one carrying
  `name-check · lexicon: tag kind.kit · first segment 'kit' is a namespace word`. Its second summary,
  with the row restored, prints `0`.
  Red when: the arms no longer refuse the old spelling, so the first summary prints `0`. Or the new
  spelling is refused, so the second does not print `0`.
  cost: one incremental index build in a fresh worktree, which shares the common index.
  permission: as AC2.
- **AC4** — When `python tools/playbook/core.py fixture --plant practice` runs, it exits 0, prints the
  label `practice: new charter-practice demo --line x`, and ends `fixture · green · 0 expectation(s) failed`.
  The same holds for `python tools/playbook/core.py fixture --plant kinds`.
  Red when: the fixture's register keeps `kind.practice` while `run_practices` reads
  `kind.charter-practice`. Then the gate reds `kinds.toml holds no kind.charter-practice row` and the
  plant fails.
- **AC5** — When the kinds contract runs over the real tree, through
  `python -c "import sys; sys.path.insert(0,'tools/playbook'); import core; l,rc=core.run_kinds(); print(rc); print(l[-2:])"`,
  it prints `0` and `core: kinds · 17 registered, 14 pending`. And
  `python -c "import sys; sys.path.insert(0,'tools/playbook'); import core; print(core.run_practices()[1])"`
  prints `0`.
  Red when: `core-pending.txt` keeps `kind.kit`. Then `run_kinds` reds that row as no kind the register
  holds, and it reds `kind.tool-kit` off the pending list for its empty factory. Or `run_practices` still
  reads `kind.practice` and prints `1`.
  figure: 17 and 14 are DERIVED from the register and the pending list at the tip. At `40427f33c` both
  probes printed `0`, and the first printed the same line.
- **AC6** — When `python tools/playbook/core.py new practice demo --line x` runs at the tip, it exits 2 and
  prints `refused · kind.practice is no kind the register holds`. `core.py new kit demo` and
  `core.py new layer demo` do the same, naming `kind.kit` and `kind.layer`. Afterwards
  `git status --porcelain tools/playbook` prints nothing.
  Red when: a retired word still finds a row, or a refused call writes a file.
- **AC7** — When `git grep -n -E '(^|[^-a-z])kind\.(kit|layer|practice)([^-a-z.]|$)' -- tools help skills`
  runs at the tip, it prints nothing. And `grep -n 'never a namespace word' tools/playbook/kinds.toml`
  prints S2's sentence.
  Red when: a reader under `tools/`, `help/` or `skills/` keeps a retired spelling, or the register states
  no rule. At HEAD the grep names seven lines, across `kinds.toml`, `core.py` and `core-pending.txt`.

## 7. Gates

`tags (the resolver's checks)` · `core kinds` · `core practices conformance` · `core meta-check` · `core selftest` · `govkit acceptance matrix` · `playbook render selftest`

`check-spec-tokens.py --legs-for`, run on the three Files-touched paths, printed two guarded legs that are
not broad: `govkit acceptance matrix` and `playbook render selftest`, each through `tools/playbook/`. It
printed every other tripped leg as a broad guard, and the guards join excludes those. The five core and
tags legs carry no guard and run on every change. They are named because this unit moves what they read.

No new arm. AC3's fixture is a probe of the real tree. The shape arm's first-segment class is already
planted, as the `ns-word` plant `practice.repo.x` of PLAY-dOrderedCharter-10. S4 re-spells the data of
`core selftest`'s existing arms, so it adds and moves none.

## 8. Open questions

- **F1 — How are the three kinds named so that the shape arm and the name-check pass?**
  - **(A)** Rename the three rows to segments that no namespace owns.
  - **(B)** Add a grammar rule that lets the `kind` namespace name a namespace word.
  - **(C)** Rename the three namespaces instead.

  Each option was tested against the shape arm, the lexicon name-check and the readers.
  - (A) moves three tracked files under `tools/` and the text of three dShippedRelease specs. Both
    arms use one predicate over the registry's words, and the new names pass it: this writer's
    `lexicon.py --tags` probe at `40427f33c` graded seven names and refused only the three old ones.
  - (B) must put the same exception in `check_tag_shape` and in `check_tag_name`. That means either
    typing the word `kind` into both, which PLAY-dOrderedCharter-10 rejected as a second spelling of the
    registry, or adding a registry field that both read. It also rewrites `help/tags.md`'s rule. It is
    the more feature-rich option, because `kind.item` and `kind.role` would then never go red.
  - (C) renames every member tag. For `layer` alone,
    `git grep -l -E '(^|[^a-z0-9.-])layer\.[a-z0-9]' -- tools skills help '*.md' ':!memory/builds'`
    listed 40 files at `40427f33c`. That is outside the brief's reader set.

  Recommendation: A. RESOLVED (agent, 2026-11-04, delegated): A, by
  `2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief`.

  The loser is B. The observation that rejected it is the systems record's Grammar bullet in
  `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-systems.md`. It reads "A first
  segment may not be a namespace word". It also says the core's shape check "refuses a name that breaks
  the rule in every registered namespace". The owner settled both on 2026-10-19 ("rename that segment
  to conform to tag grammar"; "yes, rename them and add the check"). B reverses that answer. That is
  dClosedLoop's settled design, not a fork of this build's specs or a part of its scope, so the build
  method's account of what a mandate delegates does not reach it. B needs an owner turn, and the fork
  rule discards an option that needs one. B therefore stays an owner question and is not filed here.
  C passes both arms as A does but leaves more follow-ups open: 40 files of member tags for `layer`
  alone, with `kind.item` and `kind.role` still unaddressed. So the feature-rich rule ranks it below A.
  widens: none · relaxes: none
- **F2 — How is each new name spelled?**
  - **(A)** `<qualifier>-<word>`: `tool-kit`, `product-layer` and `charter-practice`. The head noun stays
    the namespace word.
  - **(B)** `<word>-<artifact>`, the `policy-file` shape: `kit-descriptor`, `layer-row` and
    `practice-row`.

  Both pass `lexicon.py --tags`. The noun canon maps none of their subtokens
  (`tools/lexicon/canon.py#build_form_index`). Under B, `core.py new kit-descriptor` would name a
  descriptor, while the factory that DEPL-dShippedRelease-10 S4 specifies writes a whole kit: its
  descriptor, README, version module and registry entry. B therefore names the artifact and not the
  kind.

  Recommendation: A. RESOLVED (agent, 2026-11-04, delegated): A, the option whose name states what the
  factory makes, by `2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief`. The loser's observation is
  DEPL-dShippedRelease-10's S4 factory, which writes four files of which the descriptor is one.
  widens: none · relaxes: none
- **F3 — Does `core.py new <kind>` keep the old words?**
  - **(A)** The word follows the tag, as `read_kind_row` already derives `kind.<word>`. This needs no new
    code, and the dShippedRelease specs' `core.py new kit` is rewritten outside this diff.
  - **(B)** A `word` key on each kind row keeps `core.py new kit`.

  B spells a kind's name twice, as its tag and as its word, on every row. It also adds a key that
  `run_kinds`'s key check must require. That is two places holding one fact.

  Recommendation: A. RESOLVED (agent, 2026-11-04, delegated): A, tie-broken by reuse of `read_kind_row`,
  by `2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief`. The loser's observation is `run_kinds`'s
  required-key tuple (`owner`, `binds`, `population`, `factory`, `gate`), which B must widen on all 17
  rows. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-04 · initial draft, by `2026-11-04-prompt-PLAY-dOrderedCharter-65-repair-brief`, every
  reader found by `git grep` at HEAD `40427f33c`.

## 10. Reuse audit

The seam extended is the register itself and its existing lookup. S1 and S3 are data edits to
`tools/playbook/kinds.toml` and `tools/playbook/core-pending.txt`. S4 re-points the literals that
`tools/playbook/core.py#read_kind_row`'s `kind.<word>` derivation already serves, and it adds no
mechanism. The naming follows the owner's own rename precedent in the dClosedLoop systems record
(`adopter`, `policy-file`). The probe
`python tools/codebase-map/reuse_lookup.py "rename a kind tag whose first segment is a namespace word"`
ranked `TagError`, `read_namespaces` and `check_tag_shape` in `tools/playbook/tag_index.py`. These are
the arms this unit leaves unchanged, because the fork keeps the grammar. It also ranked
`derive_rename_map` (`tools/govkit/govkit.py`), which maps gov's file renames between two install
vintages and has nothing to do with tags. So no ranked seam fits beyond the register. The recall query
returned the repair brief, PLAY-dOrderedCharter-10's shape-check scout, and the owner's 2026-10-19
tag-grammar answer that the first fork's veto rests on. Where the brief and the source disagree: none
found. The brief's six reds are three per arm, which matches the two predicates read here.

Recall terms used: `python tools/memory-recall/query.py "how is a kind tag named when its word is a registered namespace word" --terms "kind kinds.toml namespace word first segment shape check lexicon name-check policy-file adopter rename core.py new read_kind_row"`
