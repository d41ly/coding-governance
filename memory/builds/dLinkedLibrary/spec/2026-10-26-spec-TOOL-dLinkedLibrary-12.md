# TOOL-dLinkedLibrary-12 — the `marker` namespace's members, one per existing `gov:` word, and the check that refuses an unregistered one

**Status:** OPEN · rev-3 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 3 · advances TOOL-dLinkedLibrary-26

**Carries:** cl-dClosedLoop-0249@49ce83a8 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-fix-return.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-23 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-reuse-scout-b.md) | research | TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-1 |
| [2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-spec-stage-returns.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md](../prompts/2026-10-26-prompt-TOOL-dLinkedLibrary-1-spec-brief.md) | research | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 |
| [2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md](../reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 |

<!-- /gen:spec-records -->

## 1. Goal

The `gov:` prefix marks a line for a machine: a version marker, a fan-out claim, a region pair, an
idiom-ban waiver. At base it is spelled 21 ways outside the memory tree, one of them in a comment that
claims a marker no file carries, one read by nothing since the check that read it retired, and two
written as fragments, and nothing says which words exist or which check reads each (the systems round's
M33, `systems.md:322-331`). TOOL-dTotalRecall-9 S1 registers the `marker` namespace and its extractor
`extract_marker`, tag `marker.<word>`; this unit gives the namespace its members, one per existing word
with the check that reads it, and refuses a `gov:` word no member declares.

## 2. Scope (IN)

Build-run precondition: TOOL-dTotalRecall-9 S1's `extract_marker` and its `marker` row in
`tools/playbook/namespaces.toml`, read through PLAY-dOrderedCharter-19 S2's `read_namespaces`. Neither
exists at base; the unit's build pass waits for both and adds no second extractor.

- **S1** — The member registry, `tools/memory-tree/marker-words.toml`: one `[[marker]]` row per word,
  with `word`, `reader` (the tracked path that reads it, or `none`), `reads` (one line: what the reader
  does with it), `kind` (`marker`, `pair`, `waiver` or `fixture`) and `owner` (the unit that registered
  it). `read_marker_words(root)` in `tools/memory-tree/annotations.py` reads it and refuses a row
  missing a field, a duplicate `word`, a `word` outside the namespace grammar's `seg`, or a `reader` that
  is neither `none` nor a tracked path. Observed by AC1 and AC4.
- **S2** — The members, one row per word of §4's census, re-counted at the pass by S3's own population:
  nineteen whole words and two family stems, `argv` and `conf-allow`, which name a begin and end pair
  and are written as stems in two places. Observed by AC1.
- **S3** — The check, `check_marker_words(root, conf)` in `tools/memory-tree/annotations.py`, the first
  arm of the module's CLI `python tools/memory-tree/annotations.py check [--only markers]`. It calls the
  `marker` namespace's extractor over every tracked file outside `MEMORY_ROOT`, strips one trailing
  hyphen from a word (a stem written as a prefix), and refuses both ways: a word no row declares, printed
  `annotations: markers: unregistered gov: word <word> at <path>:<line>`; a row whose word no file
  carries, printed `annotations: markers: <word> is registered and appears nowhere`. A row whose
  `reader` is `none` prints `annotations: markers: unread — <word>: <reads>` and does not red. Exit 1 on
  any refusal. Observed by AC2, AC3 and AC5.
- **S4** — The stale claim at its source. `.githooks/pre-commit:110` says a probe "carries an in-line
  `gov:root-fixture` marker"; TOOL-aRepatriatedFork-30 made the install-prefix gate a pure ban and no
  line carries the marker. The comment is rewritten to name no marker, so the word leaves the census
  rather than being registered. Observed by AC6.
- **S5** — The module, `tools/memory-tree/annotations.py`, created here with the CLI's `check` verb, its
  `--only <arm>` filter, an `ARMS` table holding `markers` alone, and its `--selftest`. Shared interface
  I10's other arms are TOOL-dLinkedLibrary-4's and TOOL-dLinkedLibrary-17's, each one more `ARMS` entry.
  Observed by AC2.

## 3. Non-goals (OUT)

- The extractor, the namespace row and the index rows: TOOL-dTotalRecall-9 S1's, called here.
- The `gov:note`, `gov:feature`, `gov:end` and `gov:legacy` words: TOOL-dLinkedLibrary-4,
  TOOL-dLinkedLibrary-17 and TOOL-dLinkedLibrary-23 each add their row with the first line that writes
  the word.
- Retiring `gov:bounded-fanout`, which nothing reads since TOOL-dGroundRules-10 (`2ebafd441`): the
  clause registers the existing words; S3 prints it `unread` on every run, and the 13 sites are the
  owner's to keep or clear.
- The waiver words as ledger populations: no clause of this build registers them; TOOL-dWitnessedBar-13
  owns the factory that would.
- The `annotations` leg: TOOL-dLinkedLibrary-7 adds the row that runs `annotations.py check`.
- `gov:` words inside `memory/`: records quote markers as evidence, and a quoted word marks nothing.

### Edges

- **hands-off** `TOOL-dLinkedLibrary-4` — `marker`, the namespace's member registry it adds the `note`, `feature` and `end` rows to, and `annotations.py`'s `ARMS` table its arms join
- **hands-off** `TOOL-dLinkedLibrary-7` — `marker`, the members whose rows the lookup's query arm reads, and `annotations.py --selftest` the `annotations selftest` leg runs
- **hands-off** `TOOL-dLinkedLibrary-23` — `marker`, the member registry its `legacy` row joins
- **consumes-from** external — dTotalRecall's `extract_marker` and the `marker` namespace row (TOOL-dTotalRecall-9 S1); dOrderedCharter's `read_namespaces` (PLAY-dOrderedCharter-19 S2)
- **hands-off** `TOOL-dLinkedLibrary-40` — `marker-words.toml`, the registry the `legacy` row joins (id 3)
- **hands-off** `TOOL-dLinkedLibrary-48` — `read_marker_words` and `check_marker_words`, whose reader resolution and owned-row rule unit 48 states for an adopter (id 59)
- **hands-off** `TOOL-dLinkedLibrary-52` — `annotations.py`'s selftest plants, which unit 52 composes at run time (id 14)
- **hands-off** `TOOL-dLinkedLibrary-62` — S1's refusal of an untracked `reader` and AC4, which unit 62 keeps live for rows this repository's builds own (id 26 of the spec audit of units 37 to 53)

## 4. Design

### The census

Read at base `5fede642` with `git grep -ohE "gov:[a-z0-9][a-z0-9-]*" -- . ':!memory' | sort | uniq -c`,
each reader verified at the line cited. The counts are PINNED at base; S3 re-derives them.

| word | sites | kind | reader | what it reads |
|---|---|---|---|---|
| `kit` | 201 | marker | `tools/check-kit-versions.sh` | each kit's version marker against its constant |
| `fixed-verifiers` | 52 | marker | `tools/hooks/agent-cap.js` | `FIXED_MARK` (:455), a fan-out split claim |
| `sequential-agents` | 36 | marker | `tools/hooks/agent-cap.js` | `SEQ_MARK` (:487), a sequential loop's bound |
| `playbook` | 21 | pair | `tools/playbook/render_playbook.py` | `REGION_OPEN`/`REGION_CLOSE` (:121-122) |
| `literal-python` | 21 | waiver | `tools/lib/resolve-python.test.sh` | the idiom ban's skip (:603) |
| `fixed-writers` | 18 | marker | `tools/hooks/agent-cap.js` | `WRITER_MARK` (:464) |
| `handoff` | 16 | marker | `tools/hooks/agent-cap.js` | `HANDOFF_MARK` (:1621); `tools/roles/handoff.py` writes it (:420) |
| `bounded-fanout` | 13 | marker | `none` | unread since TOOL-dGroundRules-10 retired agent-cap's counting |
| `conf-allow-begin`, `conf-allow-end` | 8, 10 | pair | `tools/unattended/check-unattended.sh` | check 22's allow-list region (:3303-3309) |
| `conf-allow` | 1 | pair | `tools/unattended/check-unattended.test.sh` | the stem a sed address names both by (:6404) |
| `argv-begin`, `argv-end` | 6, 5 | pair | `tools/unattended/check-unattended.sh` | `read_argv_flags`, check 26 (:221-226) |
| `argv` | 1 | pair | `tools/unattended/check-unattended.sh` | the stem its comment names the pair by (:4594) |
| `resume-schedule-set`, `resume-schedule-default` | 3, 2 | marker | `tools/unattended/check-unattended.sh` | check 46's closed set and default (:3356-3358) |
| `lander-mode-set`, `lander-mode-default` | 3, 2 | marker | `tools/unattended/check-unattended.sh` | check 45's closed set and default (:3330-3332) |
| `one-extractor` | 3 | waiver | `tools/memory-tree/check-memory-hygiene.test.sh` | the suite's one admitted extractor (:1742) |
| `literal-resolve` | 3 | waiver | `tools/codebase-map/selftest.py` | the `resolve()` ban's skip (:352) |
| `an-older-writer-mark` | 2 | fixture | `tools/workflows/unattended-build.test.sh` | a planted stale writer marker (:2107) |
| `root-fixture` | 1 | — | none | a claim in a comment; S4 corrects it |

Nineteen whole words, two stems, and one stale claim: 21 members. The systems record counted "20 words"
(`systems.md:325`) at an earlier tree.

### The registry row

```toml
[[marker]]
word = "argv-begin"
reader = "tools/unattended/check-unattended.sh"
reads = "read_argv_flags: the driver's top-level flags between the argv pair, check 26"
kind = "pair"
owner = "TOOL-dLinkedLibrary-12"
```

### The module's shape

```python
ARMS = {"markers": check_marker_words}        # TOOL-dLinkedLibrary-4 and -17 add theirs
def main(argv): ...                            # check [--only <arm>] · --selftest
```

Each finding line opens `annotations: <arm>: `, so the leg TOOL-dLinkedLibrary-7 adds reads one prefix.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `tools/memory-tree/marker-words.toml` | registry | none |
| `tools/memory-tree/annotations.py` | module, CLI `check` | none |
| `read_marker_words`, `check_marker_words`, `ARMS` | Python | `py.function`, asked at the pass |
| the 21 `[[marker]]` rows | registry rows | none |

### Migration

None: the registry is new, and every word the tree carries at the pass is a row, so the first run is
green over it.

### Rollout

Live as a CLI at landing; the bar reads it once TOOL-dLinkedLibrary-7's leg lands in this build.

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1, S3, S5
- `tools/memory-tree/marker-words.toml`: S2
- `.githooks/pre-commit`: S4's comment
- `tools/memory-tree/README.md`: the CLI and the registry, one paragraph
- `tools/memory-tree/check-memory-hygiene.sh`: `KIT_MEMORY_TREE_VERSION`

### Alternatives rejected

- **A `members` column on the namespace row.** The row is PLAY-dOrderedCharter-19 S2's schema; a list
  there changes a parent's registry, and a word's reader and kind do not fit one cell.
- **Registering `root-fixture`.** A row would make a false comment true by declaration; S4 corrects the
  comment instead.

## 5. Production-readiness checklist

- security — read-only over tracked text; no write path.
- perf / scale — one extractor pass over the tracked files outside the memory tree, as the index build
  already makes; a run over the index's rows needs no second read.
- error / empty / loading states — an empty `marker` namespace is the extractor's `unarmed`, which S3
  prints and exits 1 on, never green over nothing; an unreadable registry is a named refusal.
- observability — every refusal names the word, the path and the line; unread words print every run.
- risks — a new `gov:` word in a tool now needs a registry row in the same commit; the refusal names it.
- testing — AC1 to AC6 by a pass; the arm of §7 at the close.
- migration — none.
- user docs — no page under `help/` covers markers; `tools/memory-tree/README.md` gains the paragraph.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py check --only markers` runs at the pass tip, it exits 0, prints
  `annotations: markers: unread — bounded-fanout` once, and every word the census command of §4 prints
  has a row in `marker-words.toml`.
  Red when: a word of the tree has no row, or the unread word prints nothing.
  figure: DERIVED at the pass; 21 words at `5fede642`.
- **AC2** — When a scratch tool file carrying `# gov:planted-word` is added to a scratch clone and
  `python annotations.py check --only markers` runs there, it exits 1 printing `unregistered gov: word
  planted-word` and the file's path and line.
  Red when: the planted word passes.
- **AC3** — When a row `word = "never-written"` is added to the registry in a scratch clone, the check
  exits 1 printing `never-written is registered and appears nowhere`.
  Red when: a registered word with no site passes.
- **AC4** — When the registry in a scratch clone holds a row whose `reader` names an untracked path, or a
  second row for `kit`, `python annotations.py check --only markers` exits 1 naming the row.
  Red when: a malformed registry is read as valid.
- **AC5** — When the check runs over a scratch clone whose `memory/` carries a record quoting
  `gov:planted-word`, it exits 0.
  Red when: a word quoted in a record is refused.
- **AC6** — When `git grep -n "gov:root-fixture" -- . ':!memory'` runs at the pass tip, it prints nothing.
  Red when: the comment still claims the marker.

## 7. Gates

`memory hygiene` · `policy fixtures` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC2 AC3 AC4 AC5 · its selftest's scratch tree with a planted unregistered word, a registered word no file carries, a malformed row and a quoted word under the memory root, the failing case each passing the check · none

The arm runs under the `annotations` leg TOOL-dLinkedLibrary-7 lands, which runs this module's
`check` and `--selftest`; until it lands the main loop runs the arm at the close.

## 8. Open questions

- **F1 — Which text is the population: every tracked file, or every file outside the memory tree?**
  Options: (a) every tracked file, the extractor's own population; (b) outside `MEMORY_ROOT`. Records
  quote markers as evidence (this build's specs quote `gov:note` before TOOL-dLinkedLibrary-4 registers
  it), so (a) reds on a quotation that marks nothing and would make every record writer register words.
  Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-26, delegated): (b). widens: none · relaxes: none
- **F2 — How are the two fragments registered?** `gov:conf-allow-` sits in a sed address
  (`check-unattended.test.sh:6404`) and `gov:argv` in a comment naming the sentinel pair
  (`check-unattended.sh:4594`). Options: (a) rewrite both to whole words; (b) register each as a `pair`
  stem, the check stripping one trailing hyphen. (a) edits the unattended kit's own suite, whose run is
  waived for this landing (README rule 8), so its edit would land unobserved. (b) is true to what each
  site names, the pair by its stem. Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-26, delegated):
  (b). widens: none · relaxes: none
- **F3 — Is a word nothing reads refused?** Options: (a) refused, `bounded-fanout` cleared from 13 sites
  in this unit; (b) registered with `reader = "none"` and printed `unread` on every run. The clause asks
  for members over the existing words, and (a) edits eight workflow scripts and their templates for a
  marker the review protocol still documents (`tools/workflows/REVIEW-PROTOCOL.template.md:122`).
  Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-26, delegated): (b). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 12, the brief's I13, scout B's row 12 and
  census, every word re-counted and its reader verified at base `5fede642`.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-40, TOOL-dLinkedLibrary-48, TOOL-dLinkedLibrary-52, promoted from the round-1 spec audit of the 25 unit specs; nothing else moved.
- rev-3 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-62, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dTotalRecall-9 S1's `extract_marker` and `marker` namespace row, read through
PLAY-dOrderedCharter-19 S2's `read_namespaces`, so this unit adds members and a check and no second
scan; and the both-ways registry check `check_invariant` and `load_leg_names` already make for a token
against a declared set (`tools/memory-tree/gotchas.py:191`, :400-447), whose refusal shapes S1 and S3
follow. `python tools/codebase-map/reuse_lookup.py "refuse a comment marker word that no registry
declares"` ranked name stems (`declares` in `gotchas.py`, two refusal classes, `declared_list`); none
reads a marker vocabulary, so no existing seam fits the member registry, and S1 adds it beside the
module that grades the other annotation arms. Scout B counted 19 words and 2 fragments over `tools` and
`skills`; over every tracked file outside `memory/` the count adds `gov:root-fixture` in
`.githooks/pre-commit`, a stale claim S4 corrects, and `gov:literal-python` once more in
`.githooks/straggler-guard.sh`. The recall query returned scout B's row 12, TOOL-dTotalRecall-9 S1, and
the annotations research's census naming `.githooks/pre-commit:103`'s `gov:root-fixture`, which has
moved to :110.

Recall terms used: `python tools/memory-recall/query.py "which gov: marker words exist and which check reads each one" --terms "gov: marker namespace extract_marker marker.word registry unregistered word conf-allow argv-begin fixed-verifiers literal-python"`
