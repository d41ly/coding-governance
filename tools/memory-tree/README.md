# memory-tree — structured, machine-linted project memory

A project-agnostic kit that turns the governance playbook's §5/§6 memory-and-decisions *principles*
into a concrete, gated folder structure: one `memory/` tree organised by development discipline, with
per-feature `builds/` folders, index budgets + rotation, a status vocabulary, a GENERATED work-state
index, and a hygiene gate that keeps it that way. The owner reads indexes, not files; sessions stop burning tokens
re-deriving what memory already records.

Opt-in. Everything project-specific lives in one repo-root `.memory-tree.conf`; the scripts and rules
below are identical across repos. (Reference implementation: adopter ic's `docs/`→`memory/` reorg,
ARCH-bOrderlyAtlas-1.)

## What's here

| File | Role |
|---|---|
| `.memory-tree.conf.example` | the per-repo config — `MEMORY_ROOT`, `DISCIPLINES`, discipline→`FAMILIES`, optional `TOMBSTONE_ROOTS`. Copy to your repo root as `.memory-tree.conf`. |
| `check-memory-hygiene.sh` | the gate — 26 checks (1-12, 21, 22, 23 and 25 in the shell, 13-16 delegated to `corpus_ids.py`, 17-19 to `gotchas.py`, 20 and 24 to `row_grammar.py`, 26 to `transition_audit.py`; 21 owns its fail branches in the shell and delegates only the PARSE to `gen_build_index.py`, because `check-arms.py` discovers its population from tracked shell and cannot see a Python raise), grandfather-aware, with a `--staged` pre-commit fast leg. THE single source; CI/hook/gate-runner all call it. |
| `row_grammar.py` | check 20 — one id, one row per row document. Pinned shrink-only by `ROW_DUPLICATE_PIN`; undeclared means 0, the strictest value. Arms live in its own `--selftest`, which is a gate leg, because the shell arm-scanner cannot reach a Python module. Also the backlog-row grammar other engines import (`parse_row`, `census`), the `SEVERITY_UNLABELLED_PIN` and `LIVE_ROW_PIN` shard ratchets (blank = unarmed, announced as NOT MEASURED), `--emit-pin` for all three pins, and `--ages`, row age DERIVED from git. |
| `gen_build_index.py` | the generated build index (`--write` / `--check` / `--selftest`); check 9 calls it. Renders each build README's generated region, `LIVE.md`, and `ledger/<month>.md` shards from build front matter plus every spec's status header — a build's status is a pure function of its units', so nothing is authored and nothing rots. With `LIVE_DORMANT_DAYS` set, `LIVE.md` gains a `Last record` column, the newest date the build's own records carry, and an `Activity` column reading `active` or `dormant` against the newest record date in the tree, active rows first; blank renders the file unchanged. With `LIVE_LANDED_UNCLOSED` set to `1`, `LIVE.md` also gains a trailing `Landed-unclosed` column, each live build's non-terminal units whose id tracked product source cites, read by calling the drift-audit kit's own `non_terminal_specs_cited_by_product_source` signal in-process, so it is a candidate to close and never a verdict; the key declares that tree carries that kit, an empty evidence population refuses rather than rendering zeros, and blank never imports it. Under `BACKLOG_MODE=builds` it also renders the family views and owns the `--asks` print modes and the `--new-build` scaffold; its `--selftest` compares [Backlog modes](#backlog-modes--authored-shards-and-per-build-asks) against `backlog.py`'s declarations. |
| `backlog.py` | the per-build ask model: the `BACKLOG.md` grammar, the spec-header verbs `closes` and `advances`, the order-free status fold, the verdicts as data (`VERDICT_CODES`), READY, and the family-view renderer with the one relocation recipe. A library that reads no tree; its arms run inside `gen_build_index.py --selftest`. |
| `migrate_backlog.py` | the switch from shards to per-build asks: the planner (`--plan`), the switch-over writer (`--write`), the relocation engine (`--relocate` / `--ingest` / `--repair`), the straggler census (`--stragglers`) and the recipe (`--recipe`), plus `--selftest`. It calls `backlog.py`'s grammar and fold and `transition_audit.py`'s delta, and spells neither. |
| `transition_audit.py` | hygiene check 26, the transition-merge audit: a merge joining a lineage that edits authored shards to one that renders them from build folders must account for every row change with one `RELOCATED` row. Dormant under `shards`; under `builds` it keys rows through the memory-recall kit's anchor grammar and refuses by name without it. |
| `transition-audit.test.sh` | check 26's arms, each over a throwaway repository running the real checker. A repo-subject leg rather than a held self-test, because one arm compares the tracked hooks with the wiring declaration. |
| `tree_lib.py` | the helpers two or more engines here share — the conf parser, the fence reader, the status vocabulary, `kit_rel` — so no engine imports a sibling engine. |
| `check-verdict-epoch.sh` | the kit version DATES the engine's verdicts: across a range, the newest bump of `KIT_MEMORY_TREE_VERSION` must come at or after the newest commit moving a behaviour-bearing line of the engine or a delegate it names. |
| `check-verdict-epoch.test.sh` | its arms, over synthetic engines in throwaway repositories. |
| `check-method-carriers.sh` | every file that points at the build method is declared, and points rather than copies. Structural: a fluent paraphrase under new headings passes. |
| `check-method-carriers.test.sh` | its arms, each in a scratch repository, green control first. |
| `hygiene-parity.test.sh` | a differential harness: a before and an after copy of the engine over the same scratch corpora must print byte-identical output. It needs a before-revision, so it is kept for the next rewrite and is not a gate leg. |
| `marker-contract.test.sh` | the reader contracts no shared code can carry across a kit boundary — marker-region well-formedness and the section-8 resolution mark — proven by the readers agreeing over one case table. |
| `merge-rows.sh` | the launcher git runs as the merge driver: it resolves a python inline and execs `merge-rows.py`, so a copy-installed kit starts the driver at any prefix. |
| `build-readme-slot-limits.txt` | the hard per-slot byte ceilings for a build README's authored half. A seed: an adopter receives the rows without gov's values. |
| `build-readme-slot-highwater.txt` | the advisory high-water per slot, rewritten by `gen_build_index.py --bump` and never by hand. |
| `BUILD-METHOD.template.md` | the build method, rendered to `memory/guides/BUILD-METHOD.md`; its displaced explanation is [below](#the-build-methods-displaced-sections). |
| `ANNOTATION-STYLE.template.md` | the annotation style guide, rendered to `memory/guides/ANNOTATION-STYLE.md`. |
| `kit.toml` | this kit's descriptor for the deployer: file roles, the withheld self-tests, and the `requires_if` rows naming the memory-recall kit. |
| `README.md` | this file. |
| `corpus_ids.py` | the id + path classifier behind checks 13-16 (13-15 pinned, 16 structural) (`--report` / `--check` / `--measure` / `--print-defined-ids` / `--selftest`): id collisions, orphan ids, dead repo-path citations with a four-rule registry, and read-path accounting. Declares NO grammar and NO set it does not own — the id grammar comes from the memory-recall kit and the append-only/index sets are asked of `check-memory-hygiene.sh` through its print modes. Every pin is measured per corpus; checks 13-15 are behind DEAD_PATH_PIN / ORPHAN_ID_PIN; check 16 is STRUCTURAL and behind none. `--print-defined-ids` prints the id grammar as a POSIX ERE on its first line, then every id the corpus DEFINES, for a caller that must join cited ids against the set without spelling the grammar — the kickoff checker's `--card --append` is that caller. |
| `gotchas.py` | the bug-class catalogue behind checks 17-19 (`--check` / `--write` / `--report` / `--for-diff <range>` / `--for-paths <path>...` / `--declares` / `--selftest`). Anchors are DERIVED from each record's body, not authored; `--for-diff`'s stdout IS the reviewer's checklist for that diff, ranked by anchor specificity (`path`, then `directory`, then `basename`, universals first and outside the ranking) and cut at a tier boundary: whole tiers print in full while they fit `CHECKLIST_FULL_BUDGET`, 12, and every class from the first tier that does not prints as one line. No class leaves it. |
| `check-arms.py` | the harness meta-gate: every `fail` BRANCH is armed by a positive assertion naming its own failure text, or pinned in a shrink-only list. Keyed on the call site, pinned in both directions, and excluded from its own scan. Arms are read from the gate's `<stem>.test.sh` and an optional `<stem>.local.test.sh`; pins from `<MEMORY_ROOT>/project/unarmed-branches.txt` and a sidecar `unarmed-branches.txt` beside the gate, and `--report` names the file that armed or pinned each branch. Floored per gate by `ARMS_FLOORS`, which is REFUSED blank while any gate is discovered; `--emit-floors` prints the measured line. Its helpers come from `tree_lib.py`, the one module the kit's engines share, so no engine imports a sibling engine. |
| `kit-dogfood-parity.test.sh` | the two docs this kit SHIPS must equal the two an adopting repo RUNS ON, modulo the tool-root install prefix (`--check` / `--render`). |
| `adopt-memory-tree.sh` | `--scaffold` an empty tree that passes once its conf declares the keys the gate reads from the config (new projects). `--render` re-renders the four rendered documents in a tree that already carries the adoption marker, and writes nothing else — the mode `[[regenerate]]` names, and the only one that refreshes them after adoption. It REFUSES on a tree with no marker, and on a kit directory missing any of the four templates, rather than replacing your committed rule set with a placeholder. |
| `HYGIENE.template.md` | the rule set, copied to `memory/HYGIENE.md` at scaffold time. |
| `SPEC-TEMPLATE.template.md` | the canonical spec/design-pass format, copied to `memory/TEMPLATE-SPEC.md` at scaffold time; check 12 enforces it once `SPEC_FORMAT_CUTOFF` is set. |
| `merge-rows.py` | the row-keyed three-way merge driver for the authored indexes (`DECISIONS.md`, `backlog/*.md`, and each build's `BACKLOG.md` under `builds`). TWO PLANES: one stateless predicate (`^\s*[-*]\s`) splits every line into ROW or STRUCTURE, structure is merged positionally by `git merge-file`, and only the row set is key-merged here. The two recombine through a SKELETON — each input projected to a line list where every row becomes a token (its id when the grammar keys it, else a digest of its text with the terminator and trailing whitespace dropped and LEADING whitespace kept, because indentation is nesting and nesting is content) and every other line passes through byte for byte — so placement comes from git's own diff rather than from a splice this driver computes. A conflict region that is entirely tokens on both sides resolves by concatenation, because both sides sit between the same context lines, so section membership is not in dispute and only sibling order is; ANY disputed structure line is always a conflict. Five postconditions run over the WRITTEN BYTES on every verdict: no row line or leading id written more often than any one input carried it, no row under a heading no input filed it under, per-key CONSERVATION (not uniqueness — a file may legitimately carry the same row line twice), and structure identity against the merged skeleton. The anchor grammar is IMPORTED from the sibling memory-recall kit (`grammar_for` / `anchor_at`), never vendored, and there is no degraded mode when it cannot be read: any failure becomes a conflict rather than a silent take-ours. Wiring is two facts in two places and the driver command carries the install prefix — see [Wire the row-keyed merge driver](#wire-the-row-keyed-merge-driver); do not hand-type it. NOT scaffolded by `adopt-memory-tree.sh` — wiring a merge driver is a per-node git config, not a file the scaffolder can write. The kit ships its own launcher, `merge-rows.sh`, carrying the python resolver inline, so a copy-installed kit at any prefix can start the driver. |
| `merge-rows.test.sh` | the driver's replay fixtures, built on ONE bar: **never worse than `git merge-file` on the identical three blobs**. Every case runs a live control and the comparison is arithmetic — losing a line git keeps, or writing a row more often than git does, fails the suite by name. Conflicting where git resolves correctly is acceptable and is COUNTED by name against a shrink-only constant, currently 2 — a row one side moved and the other deleted, in both directions, the one shape where the row plane and the skeleton disagree about intent. On top of that bar: id-set equality against a grammar-independent oracle, the audit line reconciled against the written file at BOTH exit codes, all seven newline sites, the three fail-closed grammar failures, an end-to-end two-branch `git merge` through the real attribute + config, and five sabotage arms that prove each postcondition is the sole net for a defect class. Every case runs a control — two of twenty-eight groups did before — but the arithmetic comparison can only bind where the control EXITS 0, which is 16 of 40 cases and is FLOORED so a fixture edit cannot quietly drop one. Stating that precisely is the point: a suite that reads stronger than it is, is how this driver twice signed off on rc-0 corruption. |
| `check-memory-hygiene.test.sh` | fixture self-test for check 12 (red + green classes in a scratch repo). |

**`gotchas.py --for-diff` takes a COMMITTED range, so it runs after the commit, not before it.**
Staged-but-uncommitted work is not in `HEAD`, so the pre-commit spelling `<pass-base>..HEAD`
resolves to an empty range and prints "touches no file" — which reads as a clean checklist and is
not one. Its stdout IS the checklist and it always exits 0 — finish it, do not read its status. If a
class it names is already violated, that is the next pass. Moved here from the build method's M6 by
TOOL-dDerivedDocket-20, because it is prose about this tool rather than a rule of the method; M6
keeps the one line that points here.

## Configure

Copy `.memory-tree.conf.example` to your repo root as `.memory-tree.conf` and edit:
- `MEMORY_ROOT` — the tree's root folder (default `memory`).
- `DISCIPLINES` — your development streams (add one only when content exists — no empty folders).
- `FAMILIES` — `discipline:FAMILY` pairs; FAMILY is the id-family prefix and the required build-folder FAMILY.
- `TOMBSTONE_ROOTS` — set to the old tree you migrated FROM (e.g. `docs`) so it can't resurrect; blank otherwise.
- `SPEC_FORMAT_CUTOFF` — the date you adopt the kit; specs dated ≥ it must follow `TEMPLATE-SPEC.md` (check 12). Blank disables the check; older specs are grandfathered by filename date either way.
- `SPEC10_EVIDENCE_CUTOFF` — a Tier-2 spec dated ≥ it must RECORD its reuse audit in §10: the recall terms used, AND the probe result (a `reuse_lookup` citation, an explicit "no existing seam fits", or a named `reuse-first` waiver). Blank disables it. Without it check 12 grades §10 on presence and non-emptiness alone, so `N/A — none` is a passing reuse audit and BUILD-METHOD M7's regrounding step 5 has no terms to re-run — measured on this kit's own corpus, a majority of specs recorded none. **Set it strictly ahead of every dated spec on every LIVE BRANCH, not just your own**: a cutoff on today's date reds this leg on the default branch for every in-flight branch carrying a spec dated today. What it does NOT check is whether either fact is true; that needs something watching the probes actually run.
- `READINESS_ROWS` — the §5 production-readiness row LABELS, in skeleton order, `|`-separated. This
  is the ONLY literal row set: the spec template renders it through `{{READINESS_ROWS}}` and no
  script carries a default copy. **IT IS YOURS TO CHANGE** — edit that one string and re-render, and
  nothing requires reading the checker. The example ships ten; this kit's own repo declares eight,
  having dropped `a11y` and `i18n` because it ships no user interface. Keep it on ONE line.
- `READINESS_ROWS_CUTOFF` — the date from which a Tier-2 spec dated ≥ it must carry every declared
  row in its §5 body (check 12). Blank disables it. An armed cutoff with an empty `READINESS_ROWS`
  is a REFUSAL rather than a silent pass, because that combination grades no row at all.

Disciplines are yours to name. A SWEBOK v4 mapping is a reasonable default lens (Software Architecture,
Construction, Testing, Security, Operations, …), but product streams (as adopter ic uses) work equally well —
put the KA tag in each discipline's `README.md`, not in the folder name.

## Adopt — new project (scaffold)

```bash
cp <kit>/.memory-tree.conf.example .memory-tree.conf   # then edit
bash <prefix>/memory-tree/adopt-memory-tree.sh --scaffold             # creates memory/ + project/ + backlog shards + the generated index
bash <prefix>/memory-tree/check-memory-hygiene.sh ; echo $?           # expect 0
git add memory/ .memory-tree.conf && git commit
```

## Adopt — existing tree (migrate)

Migrating an existing docs/notes tree is a ONE-TIME landing, done in your repo (the re-file map is
project-specific data, so it is not a generic script). Adopter ic's reorg is the worked reference; the
pattern:
1. Write a table-driven mover that `git mv`s the whole tree to `MEMORY_ROOT`, then re-files per-feature
   material into `builds/YYYY-MM-DD-<FAMILY>-<slug>/`, with a census-drift guard that hard-fails any
   unmapped path.
2. Rewrite every in-tree + out-of-tree reference (masking false-positives like URLs and unrelated paths).
3. Emit `legacy-files.txt` (migrated recordings keep historical names) + `curation-debt.txt` (the fat
   legacy indexes) so the caps/naming checks pass on day one and tighten later (Phase-3 curation).
4. Set `TOMBSTONE_ROOTS` to the old root; run this gate; land atomically.
   During the transition you can keep the old gate green by running the kit only after the flip — or make
   the gate dual-mode (old checks until the flip, `memory/` checks after).

## Wire the gate (all three)

- **CI:** a job running `bash <prefix>/memory-tree/check-memory-hygiene.sh` (no args = full check, includes TREE drift).
- **Local gate runner:** add it as a concurrent leg (cheap, parallel with your test/typecheck legs).
- **pre-commit hook:** BEFORE any linked-worktree early-exit, guarded so a hook-proof in a scripts-less repo
  stays green:
  ```sh
  top=$(git rev-parse --show-toplevel 2>/dev/null) || exit 0
  if [ -f "$top/<prefix>/memory-tree/check-memory-hygiene.sh" ] &&
     git diff --cached --name-only --diff-filter=ACMR -- 'memory/**' | grep -q .; then
    bash "$top/<prefix>/memory-tree/check-memory-hygiene.sh" --staged || exit 1
  fi
  ```

## Wire the row-keyed merge driver

TWO facts, wired in two different places. The attribute is COMMITTED, so it lands once for every node:

```gitattributes
memory/DECISIONS.md merge=rows
memory/backlog/*.md merge=rows
memory/builds/*/BACKLOG.md merge=rows
```

The third line covers the per-build ask files, which every build that files or disposes an ask
appends to once `BACKLOG_MODE` is `builds`; under `shards` no such file exists and the line matches
nothing. **The `memory/backlog/*.md merge=rows` line stays after the switch**, although those paths
are then generated views nobody edits: the driver's view-against-shard refusal is what stops a
pre-switch branch's shard edits from line-merging into a view, and git asks the driver only for a
path whose attribute names it, so without that line git's own text merge completes the merge with
nothing refusing it.

The driver COMMAND is git config, so it is per node — and both of its path arguments carry the
install prefix, so there is no single literal that starts in both layouts. Do not hand-type it; this
one spelling is correct in both, because the runbook installs `check-wiring.sh` at `<root>/<prefix>/`
either way:

```bash
bash <prefix>/check-wiring.sh --fix  # resolves both prefixes, then sets ONE string
```

`check-wiring.sh` probes for `merge-rows.sh` and `merge-rows.py` at each prefix and sets the one
command below, with `<prefix>/` read as the prefix it found, and as nothing for a kit copy-installed
at the repo root. It is quoted here so you can VERIFY what it set — not so you can retype it:

- `bash <prefix>/memory-tree/merge-rows.sh %O %A %B %P`

A command that MIXES the two prefixes names a driver that exists in neither layout, and that failure
is not loud. Git prints `CONFLICT (content)`, but a driver that never starts never writes `%A`, so
the path is left holding OURS-ONLY content with ZERO conflict markers and status `UU`: an author who
sees "conflict", opens a marker-free file and `git add`s it has silently dropped every incoming row.
Measured — that is what the previously published mixed-prefix literal did. Two guards keep this
section honest rather than merely correct today: `check-wiring.sh` RUNS the configured command on a
scratch three-way before it reports `ok`, and `check-wiring.test.sh` DERIVES both spellings above by
running `--fix` in a fixture of each layout, so a stray third spelling in this file reds the bar.

## Backlog modes — authored shards and per-build asks

Where an ask lives, and who decides its status, is one conf key. This section is the author-facing
statement of the per-build model: the grammar a row is written in, the fold that derives a status,
and the verdicts that name a record the fold disagrees with. The code is `backlog.py`, and
`gen_build_index.py --selftest` fails when a verdict code or a row kind that module declares has no
defining line below — it checks that each is DEFINED here, not that the definition is true.

| Part | What it is |
|---|---|
| default | `BACKLOG_MODE` absent or blank reads `shards`: the authored `backlog/<FAMILY>.md` files, one status slot per row, with every render, gate and merge behaving as it did before per-build asks existed. `builds` switches to them, and any other value refuses by name. `ASK_CUTOFF`, `BACKLOG_EXCERPT_CHARS` and `PROBE_ALLOW` matter only under `builds`. |
| row kinds | an ask row, filed once, and nine disposition kinds, each with its writer — [Row kinds](#row-kinds-and-who-writes-each) |
| the fold | an ask's status, derived from sets of records by `backlog.derive_statuses`, in the order [The fold](#the-fold-in-order) gives |
| verdicts | one code per record the fold disagrees with — [Verdicts](#verdicts) |
| ask clauses | `seen`, `accept`, `out`, `may`, `verify` and `data`, the READY grade over them, and `PROBE_ALLOW` — [Clauses and READY](#clauses-and-ready) |
| print modes | `gen_build_index.py --asks` and what qualifies it, and the `--new-build` scaffold — [Print modes](#print-modes) |
| stragglers | the transition audit, and `migrate_backlog.py --stragglers`, `--relocate`, `--ingest` and `--repair`; the recipe itself is what `migrate_backlog.py --recipe` prints and is not copied here — [Stragglers](#stragglers) |
| signed records | the two records an owner signs before the switch, their header cells `Ask`, `Verdict` and `Field`, and the verbs that read them — [Signed records](#signed-records) |

### Row kinds, and who writes each

The separator in every row is ` · `, U+00B7 between two spaces. A build's `BACKLOG.md` holds an H1,
optional `>` quote lines, then `## Asks` and `## Dispositions`, each at most once; every row is ONE
physical line.

- ask — `- <ID> · filed <YYYY-MM-DD> [· unit] · <text> [· <label> <value>]… [→ <pointer>]`, under
  `## Asks`. Written by sessions holding the id's own slug, in `builds/<that slug>/BACKLOG.md` and
  nowhere else. `unit` declares that the same-id spec is the ask's answer; the pairing is never
  inferred from two equal ids.

Every row below sits under `## Dispositions`, and its writer puts it in ITS OWN build's `BACKLOG.md`,
never in the ask's home file. A writer changes its mind by editing its own row.

- `CLOSED` — `CLOSED · <id> · by <id|sha> · <why>`: closes an ask after the fact, by a record or a
  commit. The forward tool is a spec status header's `closes`.
- `WONTDO` — `WONTDO · <id> · <why>`: declines it. Its Decided-by value is the writer's build slug.
- `BLOCKED` — `BLOCKED · <id> · on <id> · <why>`: holds a live ask while the target, an ask or a
  spec, is live.
- `DEFERRED` — `DEFERRED · <id> · until <id> · <why>`: the same hold, read as a deferral.
- `KEEP` — `KEEP · <id> · <why>`: somebody looked and the ask stays live. It derives no status; it
  answers V10 for an ask on a finished build.
- `REOPEN` — `REOPEN · <id> · of <spec-id|sha|slug> · <why>`: cancels the one closing or declining
  record it names.
- `SEV` — `SEV · <id> · <BLOCKER|HIGH|MED|LOW> · <why>`: a severity. The most severe row wins, and
  an ask with none reads `unlabelled`.
- `SCOPE` — `SCOPE · <id> · <label> <value>…`: adds clauses to somebody else's ask. It derives no
  status and may not carry `may`.
- `RELOCATED` — `RELOCATED · <id> · by <sha> · <kept|dropped|amended>: <why>`: provenance for a row
  a pre-switch branch changed. Written by `--relocate`, `--ingest` and `--repair`, never typed.

A spec's own status header carries `closes <ids>` and `advances <ids>`, written by that spec's build.
The family views, the build README regions, `LIVE.md` and the ledger are the generator's alone.

### The fold, in order

Terminality first, reading no hold at all; then the live statuses, reading terminality. A record a
`REOPEN` names leaves every set below before any rule reads it.

1. `CLOSED` — a closing record survives: a CLOSED spec whose header `closes` the ask, the ask's own
   same-id spec when the ask carries `unit` and that spec is CLOSED, or a `CLOSED` row.
2. `WONTDO` — else a declining record survives: a `WONTDO` row, or a `unit` ask's same-id spec
   reading WONTDO. A closing spec without `unit` that reads WONTDO declines nothing: one attempt was
   abandoned, not the ask.
3. `INPROGRESS` — a linked spec, one whose header `closes` or `advances` the ask, reads INPROGRESS.
4. `SPECCED` — a linked spec reads OPEN or SPECCED.
5. `BLOCKED` — a linked spec reads BLOCKED, or a `BLOCKED` row's target is still live.
6. `DEFERRED` — the same, for DEFERRED.
7. `UNRESOLVED` — a hold names a target that is neither a filed ask nor a spec H1.
8. `OPEN` — none of the above.

Every rule is a set test, and the Decided-by value each names is the least member of a sorted set,
so no date, file order or row order decides anything and a permuted corpus folds to the same bytes.
A hold cycle among live asks is V6, not an undecidable status.

### Verdicts

`gen_build_index.py --check` prints them under a `VERDICT` header, apart from drift, because the
remedy is an edit to the record named rather than `--write`. `--asks` still runs while one stands.
Forward-only means graded only for an ask filed on or after `ASK_CUTOFF`.

- `V1` — an ask's id slug is not the build folder it is filed in.
- `V2` — a line no row shape reads: a continuation line, a heading other than the two sections, a
  row under the wrong section or above both, a malformed row, or a file that parses to nothing.
- `V3` — two ask rows for one id, anywhere in the tree.
- `V4` — two status rows, or two `SEV` rows, for one target in one file.
- `V5` — a derived token, `OPEN`, `SPECCED`, `INPROGRESS` or `WITHDRAWN`, written as a verb.
- `V6` — a hold on itself, a hold whose target resolves to nothing (the ask reads `UNRESOLVED`), or a
  hold cycle among live asks.
- `V7` — a verb row, or a spec header's `closes` or `advances`, naming an ask nobody filed.
- `V8` — a `CLOSED` row `by` a value that is neither a filed ask nor a spec H1; a sha is checked for
  shape only.
- `V9` — forward-only: an ask whose id is also a spec H1 and which does not carry `unit`.
- `V10` — a finished build still holding an ask that derives OPEN with no status row anywhere.
- `V11` — a `REOPEN` naming no record that currently closes or declines its target.
- `V12` — forward-only: an ask with no `SEV` row anywhere.
- `V13` — the clause tail's grammar: an empty clause, one label twice on a row, a malformed `seen` or
  `may`, a `may` on a `SCOPE` row, a `SCOPE` row naming an unfiled ask, or two `SCOPE` rows for one
  target in one file.
- `V14` — forward-only: an ask whose merged clauses carry neither `accept` nor a `seen … run`.
- `V15` — `ASK_CUTOFF` blank under `builds`, which disarms the forward-only verdicts.
- `V16` — `ASK_CUTOFF` not a zero-padded date, which disarms them the same way.

The generator continues the same sequence with three verdicts about the population it walks:

- `V17` — a family view carrying content the view grammar never emits. `--write` leaves it
  byte-unchanged, and the remedy is the relocation recipe, never `--write`.
- `V18` — under `shards`, a tracked `BACKLOG.md` or a spec header carrying `closes` or `advances`:
  half a migration, inert and otherwise silent.
- `V19` — under `builds`, a rotated backlog archive named for a declared family.

### Clauses and READY

An ask row, and any `SCOPE` row naming it, may end in clauses. The tail is read right to left, so a
text that happens to contain a label costs its writer that one clause, which V13 then names.

`seen <locator>` says where the claim is observable — `` `<path>`@<sha>[:<line>] ``,
`` `<path>` matching `<pattern>` ``, or `<repo>:<path>@<sha>` in another repository — and may end in
`run` and a backticked command that re-observes it, which only `--probe` ever executes. `accept` says
what done looks like, `out` where the cut-line is, `verify` how to verify it (the bar when absent),
and `data` the data boundary an external locator owes. `may` lists grants, backticked paths or
decision ids, or `none`: it is a PROPOSAL, honoured only from a build README an owner committed.
Across an ask row and its `SCOPE` rows, five labels conjoin and `may` is a union with `none` absorbed.

`--asks --ready [IDLIST]` grades each ask `yes`, `legacy` or `no` over six rules, all graded every
time so every failing rule comes back at once: R1, filed exactly once in its own slug's folder; R2,
live — OPEN, BLOCKED or DEFERRED, SPECCED or INPROGRESS with no foreign live claim, or a `unit` ask
of the `--target` build; R3, every live hold names a target inside the mandate; R4, a pointer or
`seen` names a path the tree holds, or an external locator; R5, an `accept` or a `seen … run`; R6, an
external locator carries `data`. `legacy` is an ask filed before `ASK_CUTOFF` failing only one of R4
and R5; every other failure is `no`. A grade never sets the exit status.

`--asks --probe <id>` runs the one `seen … run` command an ask's merged clauses carry, and only when
a `PROBE_ALLOW` entry admits it by whole-token prefix. Blank, which the kit ships, refuses every
probe: ask text is written by whoever filed it.

### Print modes

`python <kit>/gen_build_index.py --asks` prints the live asks as a table and writes nothing.
`--asks <FAMILY>` narrows it to one family, and `--asks <ID>` prints one ask's detail, terminal or
not. `--all` adds the terminal asks. `--json` prints one object, `mode`, `examined` and `asks`, for a
program: under `shards` its `mode` reads `shards` and its asks are empty by design, so a reader
falls back to the authored shards. Every JSON row carries the ask's `pointer` tail and a `summary`
of its text, capped in UTF-8 bytes at `ASK_SUMMARY_BYTES`. `--path <path>…` keeps the asks whose
pointer or merged `seen` locator is one of those paths or a directory on either side of one, ranks
them by severity then newest filing, and caps them at `--limit <n>` (`ASK_PATH_LIMIT` when omitted,
0 lifts it); the JSON object then adds `paths`, `matched` and `cut`, and `--path` refuses an id,
`--probe`, `--tsv` and the READY options. `--tsv` prints the READY grades as TAB rows. `--status <token>`,
`--build <slug>`, `--ready [IDLIST]`, `--target <slug>`, `--live-builds <slug>…`, `--at <rev>` and
`--probe <id>` qualify `--asks` and never run alone; `--at` reads the records and the conf at that
revision. `--new-build <slug> --asks <IDLIST>` scaffolds the build README an owner lands: it prints
the readiness table first, refuses when an id is filed nowhere or every id grades `no`, and
otherwise writes and stages that README and its contract row, then renders.

### Stragglers

A branch that forked before the switch and kept editing authored shards carries row changes with no
file to land in. Hygiene check 26, `transition_audit.py`, finds every merge that joins such a lineage
to a switched one, and refuses until each row change it carries has exactly one `RELOCATED` row. It
is dormant under `shards`. `python <kit>/migrate_backlog.py --stragglers [--local] [--tsv]` lists
the refs still owing a relocation. `--relocate --as <slug>` moves a straggler's changes into build
files after it merges the default branch; `--repair <merge-sha> --as <slug>` does the same for a
transition that already landed; `--ingest <ref> --as <slug>` takes a ref nobody will revisit. Each
takes `--dry-run`. The recipe a straggler follows is what `migrate_backlog.py --recipe` prints — one
constant, rendered by every view banner, the row driver's refusal and V17's remedy.

### Signed records

The switch applies an owner's answer to two questions the planner cannot decide: which same-id pairs
are one subject, and what becomes of each open ask on a finished build. In order:

1. `migrate_backlog.py --plan --record <dir> --record-as <unit-id>` files the worksheets.
2. The owner signs two markdown records, one per worksheet.
3. `migrate_backlog.py --plan --signed same-id=<path> --signed triage=<path>` previews the result.
4. `migrate_backlog.py --write --as <slug> --signed same-id=<path> --signed triage=<path>` applies
   exactly what is signed; `--triage-ask <id>` names the ask the legacy holds naming no id are held on.

- Each record's header carries one line per worksheet it signs, naming the worksheet's path and
  its git blob sha: ``the same-id worksheet: `<path>` · blob `<40-hex sha>` ``, and the same with
  `triage`. `--write` refuses a record whose worksheet is untracked or has moved since it was signed.
- Columns are located by header cell, never by position, and a header lacking one refuses by name.
  The same-id record carries `Ask` and `Verdict`, where Verdict is `unit` or `not-unit`. The triage
  record carries `Ask`, `Verdict` and `Field`, where Verdict is `KEEP`, `CLOSED`, `WONTDO`, `BLOCKED`
  or `DEFERRED` and Field holds the `by`, `on` or `until` value, or `-`. Other columns are read by
  nobody; this repo's own records add `Rule`, `Spec`, `Evidence` and `Severity`.

## Upgrading to 2.73 — check 20's population widened, and your bar may red on arrival

Before 2.71, hygiene check 20 admitted a rotated archive only when its basename began `DECISIONS.`,
so **every rotated BACKLOG shard went unscanned**. From 2.73 an archive is recognised by the name of
the document it ROTATED — `DECISIONS` or a value declared in `FAMILIES`, plus a date and an optional
same-day disambiguator: a lower-case `b` after the date for the second rotation of one day.

**Your `ROW_DUPLICATE_PIN` may red on the first upgraded bar, with no change of your own.** A
duplicate id that has always been sitting in a rotated shard becomes visible, and the pin is an
EQUALITY: too high reds as well as too low.

**The remedy is the duplicate, not the pin.** Raising a shrink-only pin to absorb a defect our upgrade
made visible is a weakening move caused by us, and it is permanent slack nobody will drain. Run
`python <kit>/row_grammar.py --report`, read the named ids and lines, fix the rows, then re-run
`--emit-pin` and take the number it prints.

Two smaller changes ride along. Check 10 now resolves a rotated archive's live index by BASENAME
anywhere under the memory root instead of at `<MEMORY_ROOT>/<stem>.md` — if your backlog shards live
one level down, which the shipped layout does, that check has never graded them and may now have
something to say. And `ROTATION_MODE` is a new `.memory-tree.conf` key (`cut` or `snapshot`): leaving
it undeclared changes nothing and reds nothing, an unrecognised value aborts the engine at exit 2,
and **no check grades the declared mode** — it is validated and then read by nobody.

## Upgrading to 2.88 — `check-arms.py` refuses a blank `ARMS_FLOORS`, and two backlog-row pins arrive unarmed

**The harness meta-gate reds on arrival if your conf declares no `ARMS_FLOORS`.** A blank value left
both floor arms iterating an empty mapping, so neither could fire. The refusal applies once any gate
is discovered, and this kit installs one. Run `python <kit>/check-arms.py --emit-floors` and paste
the one line it prints into `.memory-tree.conf`; it exits 1 without a usable line if a gate errored.

**`SEVERITY_UNLABELLED_PIN` and `LIVE_ROW_PIN` are new, and blank is UNARMED.** Each takes one
`<shard-path>:<count>` token per backlog shard and is a shrink-only ceiling for it. Undeclared, check
20 counts the shard and prints a NOT MEASURED line naming it on every green run, and the hygiene gate
now shows that line rather than swallowing it. `python <kit>/row_grammar.py --emit-pin` prints both,
measured. A row that closes lowers its shard's live count, so a declared `LIVE_ROW_PIN` is lowered in
the same commit.

**`tree_lib.py` is a new engine file.** It holds the conf parser, the fence reader, the status
vocabulary and `kit_rel`, and `corpus_ids.py` and `gen_build_index.py` re-import them. A tree that
replaced either of those two with its own program no longer breaks `check-arms.py`, `row_grammar.py`
or `gotchas.py` on import.

## Upgrading to 2.100 — per-build asks arrive dark

**An upgrade changes nothing until `BACKLOG_MODE` is set to `builds`.** Absent or blank, the key
reads `shards`: your authored `backlog/<FAMILY>.md` files stay the backlog, no family view is
rendered, and check 26 prints its dormant line. `backlog.py`, `migrate_backlog.py` and
`transition_audit.py` arrive with the kit and grade nothing on a shards tree, with one exception that
reds only a tree already half-switched: V18 names a tracked build `BACKLOG.md`, or a spec header
carrying `closes` or `advances`, in a tree still on `shards`.

Switching is its own build in your repository, never a step of an upgrade: it migrates your corpus,
so it takes signed records and one switch-over commit, and the adopter runbook gives the order. The
grammar, the verdicts and the fold it switches to are
[Backlog modes](#backlog-modes--authored-shards-and-per-build-asks) above. Install the memory-recall
kit before you switch — check 26 keys every row through its anchor grammar and has no degraded mode.

## Arms and pins that travel with their gates — TOOL-aRepatriatedFork-18

**A shipped gate ships its sibling suite.** `check-arms.py` reads `<stem>.test.sh` for the arms of
every tracked gate, so a kit that withheld its suites shipped gates whose branches arrived unarmed,
and each pull left `gate-arms` red until someone hand-merged gov's suites. The arm-bearing suites of
the memory-tree, unattended, kickoff-manifest and line-length kits now land as `engine` files. They
are still no adopter's LEG: check-arms reads the text and never runs it.

**Fork a gate, arm it locally.** A branch your fork adds is armed in `<stem>.local.test.sh` beside
the gate, which check-arms reads after `<stem>.test.sh` and which no descriptor claims, so the
shipped suite stays byte-identical to gov's and an update never conflicts with your arms. An empty
or absent local suite arms nothing and is not an error.

**Gov's pins arrive beside the gates they pin.** A tracked `unarmed-branches.txt` in any directory
other than `<MEMORY_ROOT>/project/` is a SIDECAR: the same four tab-separated fields, with the gate
column relative to that directory, so gov's rows mean the same branch at your prefix. The unattended
kit ships one. Shrink-only, stale-signature and vanished-gate refusals apply to it exactly as to the
central file, and a branch pinned in both is refused. Delete any row of your own central pin that a
sidecar now carries.

**A signature drops a `$(...)` command substitution** the way it drops a variable, because no run
prints the call's source. A pin row of yours whose signature carried one now reads as stale:
re-key it from the row `--emit-pin` prints.

## Notes

- Determinism: the scripts export `LC_ALL=C` and emit LF, and the build index normalises CR before it
  compares — stable across Windows/Linux. Add `memory/LIVE.md text eol=lf` and
  `memory/ledger/*.md text eol=lf` (+ the two manifests) to `.gitattributes` anyway: check 9
  BYTE-COMPARES the generated index against an LF render, so an unpinned generated file on a Windows
  checkout is CRLF in the tracked copy — the normalisation keeps the gate honest, the pin keeps the
  committed bytes right, and you want both.
- The gate is Bash (git-bash on Windows works). The `--staged` leg scopes the file-checks to staged paths.
- **`memory/project/stale-header-waiver.txt` — a build README header that is PRESENT and unparseable
  is not one that is ABSENT.** The generator raises on the first and would otherwise treat it as the
  second, regenerating the index around a corrupted header. A row here (one build README path, then
  the reason) tolerates a known-bad header; the run prints how many it tolerated on EVERY invocation,
  so growing tolerance is visible without opening the file. **Shrink-only**: delete a row when the
  header is repaired, never add one to clear a red. A row naming a path the tree no longer tracks is
  a refusal, and the file itself is required even when empty — a file nobody created is a decision
  nobody made. It ships EMPTY, and the kit declares a `[[hole]]` whose discharge probe reports it
  unarmed rather than passing silently.
- No brand gate, no product-specific migration lives here — those stay in the adopting repo.

## Codebase-map interop

Adopting the sibling `codebase-map/` kit with `MAP_ROOT` under this tree (e.g. `memory/map`)?
The hygiene + TREE scripts read `.codebase-map.conf` and carve that subtree in automatically —
see the "Codebase-map interop" section the HYGIENE template ships. No conf keys here change.

## The build method's displaced sections

`memory/guides/BUILD-METHOD.md` DECLARES NO BUDGET OF ITS OWN. It held one until `TOOL-aHonedRuleset-6`
deleted the passage on an owner ruling, taking with it the admission that no gate enforced the pair; the
file is capped now only by the hygiene class cap for `guides/`. The two figures were retyped into this
README once and both were stale within a build, which is the argument against retyping
them. It is re-read WHOLE at every pass boundary, so it grows only by displacement. The sections below live here
because they are EXPLANATION: nothing below changes what an agent does next, and the rules that do stayed in the
method.

### M5 — the probe-failure taxonomy

**Never read a probe's exit status as a verdict — these exit 0 on a miss.** A clean "nothing found" is an ANSWER:
record it as the no-seam evidence, and do not re-run with softer words until it says something.

**A partial-recall or blind-layer notice means the probe cannot see that layer at all.** In this repo **bash is
recall-dark**, so the gates, adopters and hooks that ARE the product never surface as seams; `grep` that layer
specifically and say so in §10.

**A miss on one phrasing is not absence.** Try the behaviour, then the artifact noun, once.

**An absent tool does not remove the obligation.** Grep the tree and the nearest record, and write in §10 what you
did instead.

**A hit can be STALE.** A record describes what was true when it was written. Verify any claim about current code
against source before building on it, and say in §10 where a record and the source disagreed. This one is not
theoretical: a recall pass during `TOOL-aWrittenMethod-1` returned four hits asserting the parity render runs
LIVE to SHIPPED, which the source contradicts.

### M6 — why the disjointness clause 3 is worded as it is

The method's parallelism test names `memory/DECISIONS.md`, an authored backlog shard, the run-state file, and a
generated index TOGETHER WITH its generator. That last pairing is the whole point of the clause, and it replaced a
form that could not fail.

Which backlog file is which depends on `BACKLOG_MODE`. Under `shards` the family files under `memory/backlog/`
are the authored shards the clause names. Under `builds` they are generated views, so they fall under the
generator pairing instead, beside both files that render them, `gen_build_index.py` and `backlog.py`; and each
build's own `BACKLOG.md` is written only by that build's passes, a disposer writing in its own folder, so two
passes that could both write one already intersect under clause 1. The unattended kit's `--dispatch` is where both path lists
are recorded, and it refuses a declaration pairing an index with its generator.

The vacuous form was "neither touches a shared mutable record". Every pass touches some shared record, so read
strictly it forbade all parallelism and read loosely it forbade none — and which reading applied was decided by
whoever wanted an answer. A test whose verdict depends on how generously you read it is not a test.

Naming the files fixes the first half. The generator pairing fixes the second, which is the case nobody predicts:
two passes can write provably disjoint paths and still collide, because one edits a generated index while the
other edits the generator that renders it. The second pass regenerates and silently reverts the first. Neither
wrote the other's path, so clauses 1 and 2 both pass, and the loss surfaces later as a mystery diff.

### The method's pointer table

Read these, do not restate them — a rule appearing both in the method and in one of these is a defect in the
method.

- `skills/session-kickoff/SKILL.md` + `memory/guides/SESSION-KICKOFF.md` — starting a unit, closed scope,
  the tier rule. The six interactive exits moved to the unattended protocol's §13 (`TOOL-aHonedRuleset-3`).
- `memory/TEMPLATE-SPEC.md` — spec sections, tiers, sub-spec form, the §8 mark grammar, §10.
- `memory/guides/REVIEW-PROTOCOL.md` — fan-out and concurrency caps, find→verify→synthesize, the stop rule.
- `memory/HYGIENE.md` — record placement, filename grammar, size budgets, the status vocabulary.
- `coding-governance-agents.template.md` §1, §7, §8, §16 — DoR, DoD, landing,
  gate discipline, diff-scoping, the final-message format. (ONE file since v3.0: the activity-scoped
  companion sections converged into those §§.)
- `memory/guides/UNATTENDED-PROTOCOL.md` — mandate, run state, phases and witnesses, DoD, keepalive, landing.
- `memory/guides/UNATTENDED-VERBS.md` — the verb entries, the contract's second half. Same byte-compared pair discipline.

### M2 and M3 — the judgment calls, and why they are not procedure

**Sub-spec disagreement (M2)** is a read you perform, and its only trace is the §9 line naming what disagreed.
Nothing can check that you performed it.

**M3's vetoes 2 and 3** — a new dependency or install location, and a widened security, data or write surface — are
what a run under token pressure reads generously, because both are phrased as judgements about scope. Park is the
brake, and "no survivors → park" means park, not the least-bad option.

**M7's honest limit:** a compaction landing mid-pass is not caught until the next boundary. Small passes are the
only mitigation; there is no detector.

### M4 — the spec-audit lens catalogue

Three to five, primed with the mandate, the build overview and the spec format:

- **underspecification** — which §2 item has no §6 criterion, and which §6 criterion names no observation.
- **contradiction** — §2 against §3; a sub-spec against the main spec on M2's four axes; §4 Design against §7 Gates.
- **unstated assumption** — what must be true of existing code for §4 to work that §4 never says and §10 never
  checked.
- **prior art** — has a record already decided this? That is the recall probe, M5.

## Running this engine verbatim — the four adopter routes

A carve-out against `check-memory-hygiene.sh` or `HYGIENE.template.md` is a fork, and a fork goes
stale on every kit bump. Each shape an adopter has needed so far has a route that runs gov's bytes
unchanged:

| Carve-out shape | Route |
|---|---|
| an extra registry under `<MEMORY_ROOT>/project/` | `PROJECT_REGISTRY_EXTRA` in `.memory-tree.conf` |
| a pre-governance file or folder name — a build-root status file, a free-named record, an unbound old record | a row in `<MEMORY_ROOT>/project/legacy-files.txt`, which checks 4, 5 and 21 all read |
| undated build artifacts, a JSON result or an HTML report, that cannot carry a Serves line | `RECORD_UNDATED_ARTIFACTS="exempt"`, which prints its exempted count on every run |
| a rule gov does not have | a project leg in the gate manifest, above |

Two things are not carve-outs at all. A value in the rendered `HYGIENE.md` that states the shipping
repo's figure is a render gap, and `INDEX_CAP_LINES` and `ENTRY_CAP_UNIT` now render from your conf.
A registry a KIT ships, such as `pass-order-waiver.txt`, is admitted by name.

**The worked instance is adopter nc**, measured 2026-09-23 by running gov's engine over its tree:
its registries under `project/` go to `PROJECT_REGISTRY_EXTRA`; its ten build-root status
files and thirteen run-protocol records go to `legacy-files.txt`; its undated JSON, HTML and Python
artifacts go to `RECORD_UNDATED_ARTIFACTS`; and its check 90 becomes the project leg worked below.
The per-carve-out table is the spec for the unit that shipped these routes, `TOOL-aRepatriatedFork-10`
§4.

## Adding a check gov does not have — the extension point, and its limits

A project with a rule this kit does not implement does **not** edit the engine. It writes its own
script, under its own tree, and registers it as a leg it owns. `govkit apply` then leaves that leg
alone.

That is a MEASURED claim, not a reading of the code. The probe: a fixture target whose gate manifest
held exactly ONE leg — project-authored, named `project build-README comment convention` — then
`govkit apply`. Afterwards the manifest held 23: gov's 22 emitted alongside the project's own, byte
for byte unchanged, argv and ceiling intact.

```json
{ "name": "project build-README comment convention",
  "argv": ["bash", "scripts/check-build-readme-comments.sh"],
  "chunk": "product", "subject": "repo", "ceiling": 3000 }
```

The leg's script sources `.memory-tree.conf` for `MEMORY_ROOT` exactly as this kit's own checks do,
so it reads the same tree from the same declaration.

**Give it a ceiling.** The runner reds a leg that arrives without one, and finding that out from a
red bar is a worse first experience than reading it here.

**The worked example, runnable as written.** Adopter nc's check 90 is the case this seam was ruled
for: a `<!-- status derived: … -->` comment justifies a DECLARED `status:` key in a build README,
and once the key goes the comment is a false claim nothing regenerates. Save this as
`scripts/check-build-readme-comments.sh` beside the leg above:

```bash
#!/usr/bin/env bash
# Project leg: a '<!-- status derived:' comment in a build README whose front matter declares no
# 'status:' key. Exit 0 clean, 1 on a finding, 2 when it cannot run.
set -u
ROOT="$(git rev-parse --show-toplevel)" || exit 2
cd "$ROOT" || exit 2
MEMORY_ROOT=memory
[ -f .memory-tree.conf ] && . ./.memory-tree.conf
readmes=$(git ls-files "$MEMORY_ROOT/builds/" | grep -E "^$MEMORY_ROOT/builds/[^/]+/README\.md$")
[ -n "$readmes" ] || { echo "build-readme-comments: no build README under $MEMORY_ROOT/builds/ — graded nothing"; exit 2; }
bad=""
for f in $readmes; do
  grep -q '<!-- status derived:' "$f" || continue
  grep -q '^status:' "$f" && continue
  bad="$bad  $f
"
done
[ -z "$bad" ] && { echo "build-readme-comments: clean"; exit 0; }
printf 'build-readme-comments: a status-derived comment survives with no status: key — delete it:\n%s' "$bad"
exit 1
```

It refuses an EMPTY population at exit 2 rather than printing `clean`, for the reason this kit's
rule 5 gives. Two facts about the seam around it:

- **If the script is missing, the leg reds; it does not skip.** The leg's argv is `bash <path>`, and
  bash exits 127 naming the path: `bash: scripts/check-build-readme-comments.sh: No such file or
  directory`. That exit is observed directly. That the runner then reports the leg red rather than
  holding it is `TOOL-dRetiredFork-16`'s one unobserved claim, and the unit that shipped this
  example leaves its observation to the merge bar that closes it.
- **It runs at the push bar, not at pre-commit.** The engine ran nc's check 90 under `--staged`;
  a project leg does not, and gov ships no pre-commit hook to adopters. To keep the earlier signal,
  call the script from your own `.githooks/pre-commit`. Nothing in this kit needs to change for that.

### Two limits, both measured, neither of which is "declines and reports"

**A non-colliding leg is preserved SILENTLY.** The run says nothing about it at all. Do not expect a
line confirming your leg survived; its absence from the output is the normal case.

**A COLLIDING name aborts the verb, after a partial write.** If your leg's name is one gov also
emits and your receipt does not already claim it, `apply` refuses:

```
govkit: the target's runner already has a leg named 'memory hygiene' and this target's receipt
does not claim it — overwriting a leg the target wrote silently deletes their own coverage
```

Measured: exit 2, with **41 paths already changed in the working tree**. The refusal protects your
leg — it is not overwritten — but it arrives after the install has partly landed, so the tree needs
`git checkout` or a re-run once the name is changed. Pick a name gov will not: prefixing yours with
the project name is enough.

### What this kit will NOT grow

**No plugin loader, and no `PROJECT_CHECKS` conf key naming scripts the engine invokes.** An engine
that loads project code is an engine whose behaviour the kit cannot state, and every gate it runs
becomes ungradeable. The conf-key version is the same loader under another name: it inverts
ownership, making this kit responsible for a script it cannot read.

The seam is the gate manifest, and it is already the seam. Your check is your code, in your tree,
run by your bar.
