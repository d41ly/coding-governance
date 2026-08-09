# TOOL-aMendedLedger-7 — U8: a fully keyed decision corpus

**Status:** SPECCED · rev-2 · 2026-08-09 · node a · Tier-2 · base 663ca427 · streams tooling

## 1. Goal

Widen the shared id grammar's session era by four characters, so that all 73 rows of
`memory/DECISIONS.md` key instead of 35 and this repo's own retrieval tool can see its whole
decision record.

The justification is retrieval and nothing else. Measured read-only against this worktree,
`tools/memory-recall/` resolves 53 records over its 138-file corpus today and 91 under the widened
grammar. The 38 it cannot see are the letter-suffixed correction ids this repo mints for
sub-decisions, and each of them is currently swallowed into the body of the row above it — so a
question about any of those 38 decisions returns a neighbouring record or nothing. That is a live
defect in the tool this repo runs to answer "why is it this way", and it is independent of any
merge driver.

Two further defects are folded in rather than filed away, because the widening triggers both and
each turns a gate that should have caught it into one that stays silent. `check-verdict-epoch.sh:52`
stops one hop short of the grammar that decides hygiene checks 13-16, so the widening would move
check 14's answer with `KIT_MEMORY_TREE_VERSION` untouched. And `recall_conf.Conf.digest()` omits
the eras whose edits its own docstring promises will invalidate a warm cache, so every already-built
retrieval cache would stay warm and stay half-blind.

De-authoring the `## FAMILY` headings and the `*(none yet)*` placeholders inside the row block was
S5 of this unit at rev-1 and is NOT in it now. Its load-bearing justification was that a fully keyed
row block makes the merge driver's reproduced corruptions unreachable, and that premise was
falsified by reproduction. The work is carried to §8 F1 for the owner, the falsification is stated
in §4 Alternatives rejected, and §9 rev-2 records how the claim died.

## 2. Scope (IN)

- **S1** Widen the session era from `\d+` to `\d+[a-z]*` in the ONE place the era tuple is
  constructed, having first collapsed the two copies of that tuple inside
  `tools/memory-recall/extract.py` into a single helper.
- **S2** Re-ground hygiene checks 13-16 on the measured post-widening numbers and hold every pin
  where it is: `ORPHAN_ID_PIN` stays 5, `DEAD_PATH_PIN` stays 0, `READ_PATH_CEILING` stays 37060.
  The four new orphans are fixture ids quoted in landed review narrative and are elided, not waived.
- **S3** Add `tools/memory-recall/extract.py` to `check-verdict-epoch.sh`'s `DELEGATES`. Checks 13-16
  compute their verdicts with a grammar that file owns, and the epoch gate cannot currently see it.
- **S4** Fold the memory-recall kit version into `recall_conf.Conf.digest()`, so a grammar change
  invalidates a warm retrieval cache instead of leaving it half-blind.
- **S5** Re-fixture `tools/memory-tree/merge-rows.test.sh` wherever the widening moves what an arm
  asserts: the 0d oracle block, the unkeyable-duplicate arm, and the two delete arms whose adjacent
  correction row becomes a keyed row. Every re-pointed id must be a shape the WIDENED grammar still
  misses, shown by assertion rather than asserted by comment.
- **S6** Keep `merge-rows.py:272`'s `_ID_RE` postcondition and re-ground it on the population it
  demonstrably still has, per §8 F4.
- **S7** Re-true the five statements the WIDENING itself falsifies: `merge-rows.py:78-83`, `:101-107`
  and `:272`, the suite comment at `merge-rows.test.sh:479-480`, and `:49-50` of the codebase-map
  dossier `memory/map/features/memory-tree-merge-driver.md`. All five state that the driver keys 35
  of 73 rows, or that the `…-9b` form does not key at all.
- **S8** Bump both kit versions where the widening forces them, in render order, never by
  hand-editing a rendered artifact.
- **S9** Record it. The decision rows go into `memory/DECISIONS.md` by APPEND only — check 6 leaves
  413 B of headroom against a 270 B mean row, so this unit gets one row and no furniture line is
  touched. The deferred fourth driver repair (§4 Alternatives rejected) gets a row in
  `memory/backlog/TOOL.md`, so the residual risk has a home outside this spec.

## 3. Non-goals (OUT)

- **Making the merge driver safe.** U8 does not, and no sentence in this spec may be read as
  claiming it does. The widening moves 38 rows from CONTENT to keyed rows on this corpus, which
  changes what four fixtures assert; it leaves untouched the property that produces the corruptions.
  `_ROW_RE` at `merge-rows.py:266` is `^\s*[-*]\s`, so no `#` line is ever counted as a row and both
  duplicate postconditions are blind to headings by construction. A fourth driver repair is
  DEFERRED, not avoided; S9 files it in `memory/backlog/TOOL.md`.
- **De-authoring the row block's furniture.** Forked to §8 F1 and out of this unit entirely. Nothing
  here edits `memory/DECISIONS.md:3-4` or its heading and placeholder lines, `adopt-memory-tree.sh`,
  `memory/README.md:13`, `memory/HYGIENE.md:24` or its template mirror, or the dossier's `:38-44`.
- **Widening the node-tag class or either flat era.** `recall_conf.py:43` pins the node class at
  `a-z` already, and `tools/check-wiring.sh:314` builds its driver smoke fixture on the flat
  `\d{3}` era precisely because that era is unconditional. Both stay untouched.
- **Rotating `memory/DECISIONS.md` into `memory/archive/`.** It is 413 B under check 6's cap, which
  is one mean row, so the rotation is now due sooner than this unit's own decision rows would like.
  Rotation is still a separate decision: it empties the driver's row block. See §8 F3.
- **Repairing `extract.py:104-108` `DURABLE`.** Master spec §3 already books it: its regex requires a
  pre-flatten `memory/<x>/…` shape and matches 0 of 138 corpus files. Widening does not touch it and
  does not make it worse.
- **Changing what `tools/memory-tree/adopt-memory-tree.sh` scaffolds.** With the de-authoring forked
  out, the scaffolder writes exactly the shape it writes today, so no adopter tree changes shape and
  there is nothing to migrate. The upgrade note U6 owns is unaffected.
- **Raising any pin.** `ORPHAN_ID_PIN` is shrink-only and is not to be spent on review prose.
- **Editing any existing line of `memory/DECISIONS.md`.** S9 appends. The append-only contract
  question rev-1 argued in §4 Migration belongs to the de-authoring and travels with it to §8 F1.

## 4. Design

### Inventory

Every number below was measured against this worktree, read-only, by binding a widened `Grammar` and
re-running the shipped walkers. Nothing was patched in the tree. The `corpus_ids` rows are measured
with this spec file and all three review reports under `memory/builds/aMendedLedger/reviews/`
TRACKED, because `corpus_ids.walk` builds its corpus from `git ls-files` (`corpus_ids.py:190`) and
`h1_re` (`:194`) harvests this file's own H1 as a definition. Two of those files are untracked at
`68b90fe`; a builder who measures before committing them sees `56 / 61` and `94 / 103` instead.

| measurement | current era `\d+` | widened era `\d+[a-z]*` |
|---|---|---|
| `memory/DECISIONS.md` rows keyed / total | 35 / 73 | 73 / 73 |
| `corpus_ids` ids defined (spec tracked) | 57 | 95 |
| `corpus_ids` ids cited (spec tracked) | 62 | 104 |
| `corpus_ids` orphan ids (check 14) | 5 | 9 |
| `corpus_ids` id-definition domain (check 13, `def_builds`) | 41 | 41 |
| `corpus_ids` build collisions (check 13) | 0 | 0 |
| `corpus_ids` dead path citations (check 15) | 0 | 0 |
| `corpus_ids` read path (check 16) | 4 files, 33172 B | 4 files, 33172 B |
| memory-recall `records` documents | 53 | 91 |
| memory-recall ids anchored | 46 | 84 |
| memory-recall indexed chars, `records` | 22872 | 22834 |

The 38 rows the current grammar misses are the letter-suffixed correction ids this repo mints for
sub-decisions — `TOOL-aDrainedSluice-9b`, `TOOL-aBatchedTribunal-6g`, `TOOL-aMendedLedger-1b` and 35
more. The session era is bounded by `\b` on both sides (`extract.py:78`), so `-9` matches and the
following `b` kills the word boundary; the whole id then fails to match at all rather than matching a
prefix. This is a CD-only gap: upstream mints no suffixed ids, so the fork that widened the node
class from `[a-f]` to `[a-z]` never had a reason to look at the era.

The record-count delta is exact and worth stating because it is the one number that goes DOWN. A row
anchor's record runs to the next anchored line (`extract.py:375`), so each of the 38 rows was
previously swallowed into the body of the row above it. Splitting them removes 38 joining newlines:
22872 − 38 = 22834. No text is lost; 38 records stop hiding inside 35.

**The unkeyed content inside the governed row block, which U8 does not remove.** The widening keys
rows. It does not key `#` headings or the `*(none yet)*` placeholder, and it neither removes nor
forbids them.

| file | bytes | rows | keyed, widened | `#` headings |
|---|---|---|---|---|
| `memory/DECISIONS.md` | 20067 | 73 | 73 | 5 |
| `memory/backlog/TOOL.md` | 3356 | 17 | 17 | 1 |
| `memory/backlog/PLAY.md` | 338 | 1 | 1 | 1 |
| `memory/backlog/KICK.md` | 87 | 0 | 0 | 1 |
| `memory/backlog/DEPL.md` | 88 | 0 | 0 | 1 |

Each backlog shard carries exactly one heading, its H1, which precedes the first anchor and is
therefore preamble under `merge-rows.py:210-215`'s region rule. `memory/DECISIONS.md` is the only
governed file with `#` headings INSIDE its row block: `## KICK — kickoff` at line 10, `*(none yet)*`
at 12 and `## TOOL — tooling` at 14, between the first anchor at line 8 and the last at line 87.
`## PLAY — playbook` (line 6) is preamble; `## DEPL — deployer` (89) and its placeholder (91) are
trailer. Measured under both grammars, the block boundaries do not move: first anchor 8, last anchor
87, before and after the widening.

Six furniture lines are present today, 114 bytes. That number sizes the fork in §8 F1; it is NOT the
population of the driver's defect class. The population is any non-blank unkeyed line inside the row
block, six of which happen to exist right now, and a merge input is a commit rather than the file at
rest — see §4 Alternatives rejected.

### Data model

**The regex edit, by line.** `tools/memory-recall/extract.py` constructs the era tuple TWICE, and
the second copy is the failure mode `corpus_ids.py:15-19` names in its own docstring — "upstream
re-typed one alternation with its branches reordered and would never have noticed". Edit both, but
edit them by removing the duplication rather than by touching two literals:

```python
def _eras(node: str) -> tuple[str, ...]:
    """The three id eras, from ONE construction. A second copy is the catalogue-drift class."""
    return (
        r"\d{3}",                              # flat            ARCH-001
        rf"[{node}]\d{{2,3}}",                 # node-scoped     ABL-d119
        rf"[{node}][A-Za-z]{{2,}}-\d+[a-z]*",  # session         ABL-bSiftedArchive-3, and its -3b
    )
```

- Insert `_eras` immediately after `_NODE = CONF.node_tag_class` at `extract.py:65`. It must precede
  the module-level use below it.
- `extract.py:70-74` — replace the `ERAS = (…)` literal with `ERAS = _eras(_NODE)`. Lines 57-63 and
  66-69 are the comment block that documents the three eras by example; the session-era example line
  gains the suffixed form. `:77-78` (`ID`, `ID_RE`) and `:87-92` (the four anchor regexes) are built
  by concatenation from `ERAS` and need no edit.
- `extract.py:331` — replace the re-typed local `eras = (…)` inside `grammar_for(root)` with
  `eras = _eras(node)`. This is the copy every consumer outside memory-recall actually runs:
  `corpus_ids.grammar()` (`corpus_ids.py:117`) and `merge-rows.anchors()` (`merge-rows.py:199`)
  both reach the grammar through `grammar_for(root)`, never through the module-level constants.
- `extract.py:4-15` — the fork inventory says the fork is "SIX constructs wide" and names item (2) as
  "the node-tag class inside `ERAS`". After this edit the era itself is forked too. Amend item (2) to
  name both, or the next upstream re-pull three-way-merges against a wrong inventory.

**Sites that must NOT move, each checked against source.**

| site | why it stays |
|---|---|
| `tools/memory-recall/recall_conf.py:43` `NODE_TAG_CLASS` | declares the node class only; orthogonal to the era |
| `tools/memory-tree/corpus_ids.py:117` | returns `extract.grammar_for(root)`; declares nothing |
| `tools/memory-tree/corpus_ids.py:194` `h1_re` | interpolates `E.ID`; widens automatically |
| `tools/memory-tree/corpus_ids.py:220`, `:265-269` | use `E.ID_RE` and `extract.anchor_at(line, E)` |
| `tools/memory-tree/merge-rows.py:204-207` `key()` | delegates to `anchor_at`; widens automatically |
| `tools/memory-tree/gen_build_index.py:54` `H1_RE` | `[A-Za-z0-9][A-Za-z0-9-]*` already admits a suffix |
| `tools/memory-tree/check-memory-hygiene.sh:304`, `:491` | FILENAME grammar (`<slug>-<seq>` plus `REC_TAIL`), not an id grammar; no suffixed recording name is minted |
| `tools/check-wiring.sh:314-340` | the driver smoke fixture uses the flat `\d{3}` era deliberately |

**`merge-rows.py:272` `_ID_RE` — keep it, re-ground it.** Today it is justified as "deliberately
WIDER than the driver's own anchor grammar … the ratified `…-9b` correction form, which the shared
session era's trailing `\b` rejects". After S1 that sentence is false, and review round 3 already
found the claim wrong in the other direction too: `_ID_RE` is `\b[A-Z]+-[A-Za-z0-9]+-[0-9]+[a-z]*\b`,
which is NARROWER than the anchor grammar for both flat eras. The postcondition still has a live
population, and it is a different one: a row-shaped line that carries an id but not an anchor
SEPARATOR. Measured under the widened grammar, `- TOOL-zFix-<n>b · text` keys, while
`- TOOL-zFix-<n>b carries an id but no anchor separator` does not key and IS matched by `_ID_RE`.
So the docstring is rewritten to name that population, and S5 arms it. Deriving `_ID_RE` from the
merge grammar remains rejected for the reason already in the file: a self-consistent oracle is blind.

**The verdict-epoch delegate gap, discovered while measuring S1.**
`tools/memory-tree/check-verdict-epoch.sh:52` reads:

```sh
DELEGATES="tools/memory-tree/gen_build_index.py tools/memory-tree/corpus_ids.py tools/memory-tree/gotchas.py"
```

`corpus_ids.py` is in the list, but `corpus_ids.py` deliberately declares no grammar (`:12`), so the
regex that decides checks 13-16's verdicts lives one hop further out, in `extract.py`. Widening it
moves check 14's answer from 5 orphans to 9 with `KIT_MEMORY_TREE_VERSION` untouched, and this gate
stays silent. That is exactly the defect `TOOL-aBatchedTribunal-6o` closed for the three modules
already listed — "8 of 19 verdicts lived outside the diffed file" — one hop short. S3 appends the
path; the existing `for _d in $DELEGATES; do [ -f "$_d" ]` guard at `:55` already tolerates an
adopter who has not installed the memory-recall kit. `check-verdict-epoch.sh` is neither the engine
nor a delegate, so the edit does not demand a bump of its own.

**The stale-cache gap, same class, one kit over.** `recall_conf.Conf.digest()` (`:152-160`) hashes
`memory_root`, `families` and `node_tag_class`, and its docstring claims "an id-grammar or
corpus-root edit invalidates a warm cache". The eras are id grammar and are not in the blob.
`query.py:377` writes that digest into the cache manifest and `:598` compares it for freshness, so
after S1 every already-built cache stays warm and stays blind to 38 records. S4 folds
`KIT_MEMORY_RECALL_VERSION` into the digest blob: the kit version is already the declared epoch for
this kit's behaviour, it is bumped by S8 anyway, and it needs no knowledge of a regex that lives in a
sibling module. The alternative — passing the resolved era tuple down from `extract.py` — inverts the
layering, since `recall_conf` is the module `extract` imports.

**What the WIDENING changes for the merge driver, guard by guard.** Rev-1 stated this table for a
furniture removal that is no longer in scope, and stated two of its cells wrongly. Re-measured
against the shipped module for the widening alone:

| guard | site | population on `memory/DECISIONS.md` after U8 |
|---|---|---|
| lead-in three-way merge and dedup | `merge-rows.py:511-556` | live and UNCHANGED — the six furniture lines stay, and the blank-lead-in exemption at `:551-552` is untouched |
| `no_new_duplicates`, line half | `:352-374` | live and unchanged (a row line can still repeat) |
| `no_new_duplicates`, id half | `:375-381` | live, population CHANGES — `…-9b` now keys, so what remains is the row-shaped line carrying an id and no anchor separator |
| `no_misfiled_rows` / `sections` | `:384-429` | live, population GROWS from 35 ids to 73, still two-valued (`## PLAY — playbook` x1, `## TOOL — tooling` x72) |
| the row-scoped delete comparison | `:576`, `:612` | changed: the adjacent unkeyable correction row is now a keyed row emitted by its own branch |
| unkeyed lines after the last anchor | `:632-634` | live and unchanged — the last anchor stays at line 87, and `## DEPL — deployer` plus its placeholder stay in the trailer |

No guard's population is emptied, so nothing is disarmed. Two arms change what they assert, and S5
exists so that neither changes silently: `sections()` does NOT return the empty string for any id on
this corpus, it returns the nearest preceding `#` heading, and after the widening it answers for 73
ids instead of 35. Rev-1's claim that it returns `""` was false against the module in both scope
readings — `sections()` (`:384-400`) initialises `cur = ""` and walks the WHOLE file from line 1, so
line 1's H1 `# decisions — index` sets `cur` before any anchor is reached.

**The named residual risk, stated because U8 does not close it.** The lead-in dedup's blank-lead-in
exemption at `merge-rows.py:551-552` returns without updating `prev_new_sig`, so a furniture-less row
landing between two furniture-carrying rows does not break the adjacency chain and the third row's
identical lead-in is suppressed. Ours mints three rows in one commit, rows one and three each opening
a `### 2026-08` sub-heading, row two led by a blank; theirs edits preamble prose only. The driver
exits 0 having silently deleted ours' own heading, where `git merge-file -p` preserves both. This is
live TODAY, it is live after U8, and it is live after the §8 F1 de-authoring. S9 files it.

### Migration

**The four review-prose orphans.** Widening raises check 14 from 5 to 9. All four additions are
fixture ids inside landed review narrative, none is a record:

The four ids are spelled here in the elided form the remedy produces, because writing them literally
in this spec would keep all four orphaned after the reviews are repaired — the same trap the remedy
exists for. The line numbers locate them exactly.

| id, elided | file and lines | occurrences |
|---|---|---|
| `TOOL-aMendedLedger-<n>b` | `reviews/2026-08-09-review-aMendedLedger-1-closing-diff.md:132, :427` | 2 |
| `TOOL-zFixture-<n>b` | `reviews/2026-08-09-review-aMendedLedger-2-repair.md:75` | 1 |
| `TOOL-zFix-<n>b`, one-digit | `reviews/2026-08-09-review-aMendedLedger-2-repair.md:157, :158, :160` | 3 |
| `TOOL-zFix-<n>b`, two-digit | `reviews/2026-08-09-review-aMendedLedger-2-repair.md:219, :220, :226` | 3 |

Nine occurrences, two files. The remedy is the elision this build already established and which the
third review report uses throughout: replace the trailing numeral with `<n>`, giving forms such as
`TOOL-zFix-<n>b`. Verified against the widened grammar: `<n>b` carries no digit, so neither `ID_RE`
nor any anchor pattern harvests it, and check 14 returns to exactly 5. Reviews are not an append-only
area — `APPEND_ONLY_ERE` covers `DECISIONS.md`, `decisions/` and `archive/` only — so the edit is
legal.

The four ids must be located by `corpus_ids.py --report`, never by a hand-written pattern. Measured:
a pattern wide enough to catch the review-1 fixture id also catches `TOOL-aMendedLedger-1b` and
`TOOL-aMendedLedger-1c` at `:117`, `:122` and `:426` of the same file, and those two are ratified
correction records rather than fixtures. Eliding them would delete a real citation of a real
decision and orphan nothing, which is the opposite of the remedy.

The commit message must disclose that SIX of the nine occurrences sit inside fenced quoted tool
output, and that eliding the token there trades a little reporting fidelity for not spending a
shrink-only pin on prose. Verified fence positions in `2026-08-09-review-aMendedLedger-2-repair.md`:
one fence spans `:155-161`, enclosing `:157`, `:158` and `:160`; a second spans `:217-227`, enclosing
`:219`, `:220` and `:226`. Only `review-2:75` and `review-1:132` and `:427` are prose. Rev-1 wrote
"one of the nine", which understates the trade by six times and ships a record that does not match
reality in the build whose own drift-audit thesis is that it must. Waiving the four instead would
require `ORPHAN_ID_PIN` to go 5 to 9, which is the ratchet running backwards for four ids that
describe no work.

**The warm retrieval caches.** After S4 the digest blob changes for every resolved `Conf`, so every
cache built before this unit is stale by construction and `query.ensure_cache` rebuilds it on first
use. Nothing is migrated by hand and no cache is deleted by the build; AC9 asserts the rebuild rather
than assuming it.

**`memory/DECISIONS.md` is not migrated.** Rev-1 specced a de-furnishing here and argued the
append-only contract question at length. Both travel to §8 F1 with the fork. Under this unit the file
is APPEND-only, and the byte math rev-1 measured is preserved in F1 so the owner does not have to
re-measure it.

**Pins, stated explicitly.**

- `ORPHAN_ID_PIN` stays `"5"`. Measured 5 before, 9 after widening, 5 after the elision.
- `DEAD_PATH_PIN` stays `"0"`. Measured 0 before and after. The path harvest at
  `corpus_ids.py:227-257` reads backticked tokens and markdown link targets and never consults
  `E.ID_RE`, so no id change can reach it.
- `READ_PATH_CEILING` stays `"37060"`. Measured 4 files / 33172 B before and after; `read_set`
  (`corpus_ids.py:278-305`) derives its population from charter path tokens under `MEMORY_ROOT`,
  not from ids. Headroom is 3888 B, and no work in this unit spends from it.

### Rollout

Order is a dependency chain, and the first two rows must be ONE commit.

| step | work | stages a kickoff-manifest watched path? |
|---|---|---|
| A | `_eras` helper, era widened, fork inventory amended; `check-verdict-epoch.sh` `DELEGATES` gains `extract.py`; `KIT_MEMORY_TREE_VERSION` 1.8 to 1.9 at its two sites plus a `--render`; `KIT_MEMORY_RECALL_VERSION` 1.0 to 1.1 in `recall_conf.py:4`, `:39` and `README.md:3`; `digest()` folds the kit version; the four review-prose elisions | **yes** — `check-memory-hygiene.sh` |
| B | `merge-rows.test.sh` re-fixtured; `merge-rows.py`'s three falsified docstring claims and its suite comment corrected; `_ID_RE` rationale re-grounded | no |
| C | the codebase-map dossier's `:49-50` keying measurement re-trued | no |
| D | one decision row appended; the deferred driver repair filed in `memory/backlog/TOOL.md`; build front matter `ids:` widened to include this unit | no |

Step A is indivisible: widening the grammar without the delegate entry ships a verdict change under a
stale epoch constant, and bumping the constant without widening dates nothing. Step B must not
precede step A, because until the grammar widens the re-pointed fixture ids still key the old way and
every re-fixtured arm would be asserting the wrong thing. Step C is free-standing but must not be
skipped: the dossier is the record this repo's own drift-audit thesis says must still describe the
code.

Two couplings a builder will otherwise meet the hard way. Writing this spec file adds a seventh row
to the generated region of `memory/builds/aMendedLedger/README.md`, so
`python tools/memory-tree/gen_build_index.py --write` must run in the same commit or hygiene check 9
reds; the hand-authored `ids: TOOL-aMendedLedger-1..-6` in that README's front matter must widen too,
since `gen_build_index.py` requires the key but does not derive its value. And the kickoff manifest's
watch list contains `check-memory-hygiene.sh`, so the commit that bumps the kit constant carries its
own `last-audit` re-stamp; `manifest-check.sh --staged` accepts only a re-stamp bundled in that same
commit.

### Files touched (estimate)

Grammar and its epoch: `tools/memory-recall/extract.py` (`:4-15`, `:65`, `:70-74`, `:331`),
`tools/memory-recall/recall_conf.py` (`:4`, `:39`, `:152-160`), `tools/memory-recall/README.md:3`,
`tools/memory-tree/check-verdict-epoch.sh:52`, `tools/memory-tree/check-memory-hygiene.sh:13`,
`memory/HYGIENE.md:1`, `tools/memory-tree/HYGIENE.template.md:1` (rendered, never hand-edited).

Driver and its suite: `tools/memory-tree/merge-rows.py` (docstring `:78-83` and `:101-107`, plus the
`_ID_RE` comment at `:272`), `tools/memory-tree/merge-rows.test.sh` (the 0d oracle block at
`:196-211`, the comment at `:479-480`, and the groups at `:496`, `:507`, `:519`, `:523`, `:531`,
`:586-594`, `:635`).

Records: `memory/builds/aMendedLedger/reviews/2026-08-09-review-aMendedLedger-1-closing-diff.md`,
`memory/builds/aMendedLedger/reviews/2026-08-09-review-aMendedLedger-2-repair.md`,
`memory/map/features/memory-tree-merge-driver.md:49-50`, `memory/DECISIONS.md` (append only),
`memory/backlog/TOOL.md`, `memory/builds/aMendedLedger/README.md` front matter.

Selftests that will need arms rather than edits: `tools/memory-recall/selftest.py`,
`tools/memory-tree/corpus_ids.py --selftest`, `tools/memory-tree/check-verdict-epoch.test.sh`.

**Adopter blast radius.** Small, and smaller than rev-1 claimed, because the shape statements that
travel to adopters describe the FURNITURE and the furniture is no longer touched.
`tools/memory-tree/HYGIENE.template.md:24`, `adopt-memory-tree.sh:51` and `:62-73`,
`tools/memory-tree/README.md`, `memory/README.md:13` and `merge-rows.py:55` all keep saying what they
say today; each of them is an obligation of §8 F1, not of this unit. What does travel is the grammar:
an adopter who takes kit 1.9 gets an era that keys suffixed ids, which can only ADD anchors to a
corpus, never remove one. An adopter's `ORPHAN_ID_PIN` may need re-measuring on their own corpus, and
that is the whole of the upgrade note.

### Alternatives rejected

**Vendoring a widened grammar into `merge-rows.py` instead of widening the shared one.** Rejected on
the same ground the driver already states at `:32-33`: a second copy of a regex is this repo's
catalogued drift class, and a stale-but-single grammar beats two that disagree. It would also leave
retrieval — the actual reported harm — unfixed.

**Widening the era to `[A-Za-z0-9]*` or `\w*`.** Rejected on upstream's measurement, quoted at
`extract.py:66-69`: a loose tail swallows `ARCH-codebase`, `DES-admin`, `BLOCK-arm` and bare session
slugs, measured at +348 phantom ids and a 27% orphan rate against a true 9-10%. `[a-z]*` admits the
one form this corpus actually mints and nothing else; measured here it adds 38 real ids and four
fixture citations, and no phantom.

**Removing the furniture instead of hardening the driver a fourth time — REJECTED, because the
argument for it is FALSE and was reproduced false.** Rev-1 argued it on the record of three review
rounds, three repairs and three new corruptions, every one in the handling of unkeyed content inside
the row block, and concluded that removing six lines "is the only one of the two that ends the
sequence". It is not. The argument conflates the file AT REST with the MERGE INPUTS. A merge input is
a commit, and any commit may write an unkeyed line inside the row block; U8 — and the §8 F1
de-authoring — would remove six such lines today without forbidding, gating or detecting their
reintroduction. Reproduced on a post-de-authoring corpus (preamble plus contiguous keyed rows, zero
furniture at rest), ours minting three rows of which the first and third each open a `### 2026-08`
sub-heading, theirs editing preamble prose only:

```
DRIVER  : merge-rows: 5 row(s) from ours, 0 new from theirs, 0 dropped (delete honoured), clean
          rc=0 · '### 2026-08' x1 · markers 0      <- ours' own heading SILENTLY DELETED
CONTROL : git merge-file -p                 rc=0 · '### 2026-08' x2 · markers 0
```

Three facts make it unreachable from any furniture count. `_ROW_RE` (`merge-rows.py:266`) never
counts a `#` line as a row, so `census()` and both duplicate postconditions are blind to headings by
construction. The blank-lead-in exemption (`:551-552`) returns without updating `prev_new_sig`, so a
furniture-less row between two furniture-carrying rows does not break the adjacency chain. And
`merge-rows.py`'s own docstring names this exact shape twice, at `:92-94` and `:527-533`, as
legitimate furniture on this very index. Nothing on the bar objects: `check-memory-hygiene.sh` and
`corpus_ids.py --check` are both silent on a `###` inside `DECISIONS.md`. The population is not six
lines; it is any non-blank unkeyed line inside the row block, six of which happen to be present
today. So the fourth driver repair is DEFERRED, not avoided, and this unit stands on retrieval alone.

**Waiving the four new orphans instead of eliding them.** Rejected: `ORPHAN_ID_PIN` is shrink-only by
design (`corpus_ids.py:354-356`) and the four ids name no work. Spending a ratchet on prose is the
`pin-copied-from-another-corpus` failure in its other direction.

**Rotating `memory/DECISIONS.md` to `memory/archive/` as part of this unit.** Rejected here and
retained as §8 F3. It would give S9 unlimited headroom and it is already sanctioned by
`check-memory-hygiene.sh:348`, but it empties the live file's row block, so `split_regions` treats
the whole file as preamble and the merge driver is inert on `memory/DECISIONS.md` until rows
re-accumulate. Trading a working driver for byte headroom is the wrong trade in the same build that
spent three review rounds making the driver correct.

## 5. Production-readiness checklist

- security — N/A. No auth, egress or sanitization surface; the change is one regex alternation, one
  shell variable, one hash blob and a set of doc corrections.
- perf / scale — the widened alternation adds one bounded quantifier to one branch of a three-branch
  era group. Corpus walks are unchanged in shape; `records` grows 53 to 91 documents, which is inside
  the retrieval cache's existing 512 MB budget by four orders of magnitude.
- a11y — N/A. No user interface.
- i18n — N/A. No user-facing strings.
- error / empty / loading states — the zero-record diagnosis at `extract.py:251-291` already covers a
  grammar that recognises nothing and is unaffected, because the widening can only add anchors. The
  empty-row-block case belongs to the rotation in §8 F3, not to this unit.
- observability — the instrument is `corpus_ids.py --report` and `--measure`, plus the
  `merge-rows:` audit line. The driver's guards keep their populations under this unit, so the
  DEAD-PROBE hazard rev-1 carried does not arise; what does arise is two arms whose ASSERTION changes
  meaning, and S5 exists for those.
- risks — the live risk is a silently changed fixture: after the widening, the 0d oracle's suffixed
  id keys, so an arm written to prove the oracle sees what the driver cannot would prove nothing
  while still passing. Closed by AC5, which requires that arm to fail loudly on an un-widened tree.
  Secondary risk is a stale retrieval cache silently answering from the narrow grammar, closed by S4
  and AC9. Rollback is `git revert`; no external state, no adopter data moves.
- testing + left-shift gates — no new gate leg. Existing legs gain arms:
  `merge-rows.test.sh`, `corpus_ids.py --selftest`, `memory-recall/selftest.py`,
  `check-verdict-epoch.test.sh`.
- migration / rollback — nothing in the tree is rewritten except the four elided review tokens; every
  warm retrieval cache rebuilds itself on first use after S4. No adopter tree changes shape.
- user docs — S7 and S8. The adopter upgrade note is one line about re-measuring `ORPHAN_ID_PIN`,
  and it belongs to the `WIRE-INTO-PROJECT.md` surface U6 already owns.

## 6. Acceptance criteria

- **AC1** When `python tools/memory-tree/corpus_ids.py --report` is run at the end of step A, it
  prints `ids defined : 95`, `ids cited : 100` and `orphan ids : 5`, and the orphan list is exactly
  the five ids already in `memory/project/id-orphan-waiver.txt`. The counts assume this spec file and
  all three review reports are TRACKED — `corpus_ids.walk` reads `git ls-files`, so an uncommitted
  spec measures `94 / 99 / 5` instead. The pre-elision control on the same tracked basis is
  `95 / 104 / 9`; a run that reports 9 orphans means the elisions did not land, and a run that
  reports 104 citations means the same thing. Measured baseline before the change, same basis:
  `57 / 62 / 5`.
- **AC2** When `python tools/memory-tree/corpus_ids.py --measure` is run after step A, it prints
  `ORPHAN_ID_PIN="5"` and `DEAD_PATH_PIN="0"`, matching the values it prints today, and
  `.memory-tree.conf` is unchanged. The measure output's ceiling line reports a measured 33172 B plus
  headroom and is not the pinned 37060; the criterion is that the measured byte total does not move,
  not that the two numbers match.
- **AC3** When the anchor grammar is applied to every `- ` row of `memory/DECISIONS.md` and each
  `memory/backlog/<FAMILY>.md`, every row keys. Measured baseline: 35 of 73 in `DECISIONS.md`, 18 of
  18 across the backlog shards. The control is `python tools/memory-recall/query.py` answering a
  question whose only record is one of the 38 suffixed rows, which returns a neighbouring record
  before the change and the right one after it.
- **AC4** When the four elisions are applied, the nine occurrences §4 Migration names are the only
  tokens that changed: `git diff --stat` shows exactly two files, both under
  `memory/builds/aMendedLedger/reviews/`, and every changed line differs only by a trailing numeral
  replaced with `<n>`. The four ids are located by `python tools/memory-tree/corpus_ids.py --report`
  rather than by a hand-written pattern, because a pattern loose enough to catch all four also
  catches the ratified correction records `TOOL-aMendedLedger-1b` and `-1c` — measured, at three
  further lines of `2026-08-09-review-aMendedLedger-1-closing-diff.md` — and eliding those would
  delete a real citation of a real decision. The commit message must state that six of the nine
  elided occurrences sat inside fenced quoted tool output.
- **AC4b** When the elisions have landed, `wc -c memory/DECISIONS.md` is unchanged and
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 0 with no output. The byte assertion is
  `wc -c` and never the gate: the script's own header at `:11` is "Exit 0 + no output = clean",
  check 6 prints only through `fail 6` on breach (`:348-349`) and has no byte-report mode, so a
  criterion phrased as "the gate reports a byte count" cannot be observed through the command it
  names.
- **AC5** When `bash tools/memory-tree/merge-rows.test.sh` is run after step B, it passes, and its
  0d oracle block asserts BOTH halves against the widened grammar: that the oracle keys a row the
  driver's `key()` does not, using a row-shaped line carrying an id and no anchor separator; and that
  a row with no id at all is keyed by neither. The current block at `merge-rows.test.sh:197-208`
  asserts `key()` returns `None` for a suffixed `- TOOL-zFixture-<n>b · …` row, which the widened
  grammar keys, so that arm fails loudly with its own "pick a shape the grammar really misses"
  message rather than silently — a builder who sees it pass unchanged has not widened anything.
- **AC6** When each of the three reviews' reproductions is re-run against the post-U8 tree, the
  outcome is the one named here, and each is asserted by a fixture in `merge-rows.test.sh` rather
  than by hand. Only (b) changes; the criterion for the other three is that the arm is shown to still
  FIRE on its existing fixture, not merely to pass:
  (a) round 1 and round 3's doubled `## FAMILY` heading — UNCHANGED and still constructible, on this
  repo's own file as well as on an adopter's, because U8 removes no furniture and `_ROW_RE` still
  never counts a `#` line as a row;
  (b) round 2's honoured delete discarding an adjacent unkeyable correction row — the correction row
  is now a keyed row emitted by its own branch of the case analysis, so the expected verdict CHANGES
  from rc 1 with the row preserved to rc 0 with the delete honoured AND the incoming row present; the
  fixture asserts row presence, never rc alone, and the `ADJ` id at `merge-rows.test.sh:519` is
  re-pointed onto a shape the widened grammar still misses or the arm silently changes meaning;
  (c) round 2 B5 and round 3's misfiled `PLAY` row under `## KICK` — `no_misfiled_rows` stays live
  and its population GROWS, because `sections()` now answers for 73 ids instead of 35 across the same
  two headings. `sections()` returns the nearest preceding `#` heading and never the empty string on
  this corpus: it walks the whole file from line 1, so the H1 `# decisions — index` sets `cur` before
  any anchor is reached;
  (d) round 3's repeated-lead-in loss through the blank-lead-in exemption at `merge-rows.py:551-552`
  — UNTOUCHED by U8 and reproduced live in §4, so the arm stays exactly where it is and the deferred
  repair is filed by S9 rather than claimed here.
- **AC7** When `python tools/memory-tree/check-arms.py --check` is run after every step, both gates
  sit at or above their `ARMS_FLOORS`, and no `fail` branch is newly pinned in
  `memory/project/unarmed-branches.txt`.
- **AC8** When a commit that widens `tools/memory-recall/extract.py` is made WITHOUT moving
  `KIT_MEMORY_TREE_VERSION`, `bash tools/memory-tree/check-verdict-epoch.sh` fails and names
  `extract.py`. The control is the same run on the tree before S3, where it exits 0 — a green result
  on a widened grammar is the gap this criterion exists to close, and both directions must be
  observed. An implementation that only appends the path without observing the red control has not
  proved the gate can see the file.
- **AC9** When a retrieval cache built before step A is queried after step A,
  `python tools/memory-recall/query.py` rebuilds rather than answering from it, and
  `python tools/memory-recall/selftest.py` gains an arm asserting that two `Conf` objects differing
  only in `KIT_MEMORY_RECALL_VERSION` produce different digests. That arm must be run against the
  unfixed `digest()` and seen to FAIL there, because on today's blob the two digests are equal and an
  arm that passes before the fix asserts nothing.
- **AC10** When `bash tools/memory-tree/kit-dogfood-parity.test.sh` and
  `bash tools/check-kit-versions.sh` are run after step A, both exit 0 with
  `KIT_MEMORY_TREE_VERSION` at 1.9 and `KIT_MEMORY_RECALL_VERSION` at 1.1, and every `gov:kit` marker
  agrees with its constant. `tools/memory-tree/HYGIENE.template.md` was produced by
  `kit-dogfood-parity.test.sh --render` and not hand-edited, which is observable as the render being
  a no-op when re-run.
- **AC11** When the unit lands, `git diff` on `memory/DECISIONS.md` shows additions at the end of the
  file and no deletion or modification of any existing line, and `memory/backlog/TOOL.md` carries a
  row naming the blank-lead-in exemption at `merge-rows.py:551-552`, its reproduction, and the fourth
  driver repair as owed. `wc -c memory/DECISIONS.md` stays at or below 20480.
- **AC12** When `bash tools/run-gates.sh` is run at the end of every step's commit, it is green, and
  the leg count reported in the commit message is the count the run PRINTED, verbatim. Measured at
  `68b90fe` with this spec at rev-2 in the worktree, the runner prints
  `gates GREEN — 38/38 legs passed (1 skipped)`, the skip being
  `manifest-check self-test (unchanged vs main)`. The commit message must not round that to a leg
  total the runner never emitted, and step A must move the skip to a pass, because step A stages
  `check-memory-hygiene.sh` and therefore changes the manifest.

## 7. Gates

Existing legs that must stay green, all of them, with these load-bearing here: `memory hygiene (19
checks)`, `corpus-ids selftest`, `harness arms (fail branches armed or pinned)`, `check-arms
selftest`, `verdict epoch (kit version dates the engine)` and `verdict-epoch self-test`, `kit version
markers`, `kit/dogfood doc parity`, `row-keyed merge driver replay`, `memory-recall kit selftest`,
`memory-recall skill wiring`, `memory-hygiene self-test`, `codebase-map coverage + freshness`.

No new leg. Every assertion this unit adds belongs inside a leg that already runs, which is
deliberate: `handkept_inventories_disagreeing_with_source` rises by one for each new leg whose argv
script path is absent from `AGENTS.md`'s gate-suite section, and this unit has no gate to add that
an existing one does not already own.

Four couplings, each verified against source:

1. **Widening `extract.py` forces the memory-tree kit version, and the bump has an ORDER.** Only
   after S3 — that is the point of S3. `tools/memory-tree/HYGIENE.template.md` is a RENDERED
   artifact: `kit-dogfood-parity.test.sh:41` pairs `memory/HYGIENE.md` with it and `:54` is
   `--render) norm "$live" > "$ship"`, so hand-editing the template and then rendering reverts it,
   while rendering without editing the live copy leaves `memory/HYGIENE.md:1` stale. Three sites, in
   this order: `check-memory-hygiene.sh:13`, which carries the `KIT_MEMORY_TREE_VERSION` constant AND
   the `gov:kit memory-tree@` marker on the same line; `memory/HYGIENE.md:1`, the marker, which is
   the hand-edit site rev-1 never named; then
   `bash tools/memory-tree/kit-dogfood-parity.test.sh --render`. Never hand-edit
   `HYGIENE.template.md`. `check-kit-versions.sh:30-31` reads the constant from the engine and
   requires the marker in the TEMPLATE to match it, so both legs only agree after the render.
2. **The memory-recall version is a triple, and its selftest already checks it.**
   `selftest.py:1008-1019` reads every `gov:kit memory-recall@` marker in `README.md` and
   `recall_conf.py` and asserts each equals `KIT_MEMORY_RECALL_VERSION`. Bumping one of the three
   literals and not the others reds that leg, not just `check-kit-versions.sh`.
3. **The kickoff-manifest ratchet.** `check-memory-hygiene.sh` is one of the seven watched
   pathspecs and step A stages it for the constant bump, so step A carries its own `last-audit`
   re-stamp in the same commit; `manifest-check.sh --staged` accepts nothing else. No pin moves in
   this unit, so `.memory-tree.conf` is not staged and does not add a second re-stamp.
4. **Check 9 and the build README.** This spec file adds a unit row to the generated region of
   `memory/builds/aMendedLedger/README.md`; `gen_build_index.py --write` runs in the same commit, and
   the front matter `ids:` value is hand-authored and must widen with it.

Run `python tools/memory-tree/gotchas.py --for-diff 663ca427..HEAD` before the review, not after.
Three classes in the catalogue bear directly on this diff and should be read first:
`two-answers-to-one-question` (the era tuple is constructed twice and S1 collapses it before
touching it), `fixture-passes-by-finding-nothing` (the 0d oracle's suffixed id becomes keyable, so
the arm that proves the oracle wider than the subject stops proving anything while still passing),
and `grammar-bound-to-the-wrong-root` (every consumer outside memory-recall runs the
`grammar_for(root)` copy, never the module-level constants, so editing only the constants would ship
a widening no gate exercises).

## 8. Open questions

- **F1 — de-authoring the row block's furniture: does it happen at all, and on what justification?**
  Forked OUT of this unit at rev-2. It was S5 at rev-1 and its stated justification was safety:
  a fully keyed row block was said to make the driver's reproduced corruptions unreachable, ending a
  three-round sequence instead of deferring a fourth repair. **That premise is falsified and must not
  be re-argued from the safety angle** — the reproduction, the mechanism and the three source facts
  that make it unreachable from any furniture count are in §4 Alternatives rejected. Two arguments
  survive, both weaker. The first is `two-answers-to-one-question`: the id prefix already carries the
  family, so a `## FAMILY` heading restates it, and a mis-filed row makes the two answers disagree.
  The second is frequency: today's six lines are the only unkeyed content in the governed row block,
  and removing them makes the residual class rarer on this repo's own file without making it
  unreachable anywhere. The measured cost, carried forward so the owner does not re-measure it — on
  the worktree bytes check 6 actually reads, the file being CRLF in the worktree:

  | state | bytes | lines | headroom under 20480 B | rows until the cap |
  |---|---|---|---|---|
  | today | 20067 | 91 | 413 | 1 |
  | furniture removed, one blank kept between regions | 19941 | 79 | 539 | 1 |
  | furniture removed, rows contiguous | 19939 | 78 | 541 | 2 |

  Mean row size is 270 B, so de-furnishing buys one more row before check 6 demands a rotation and
  does not avert one. Options. *(a) De-author AND add a standing furniture check.* Promote what rev-1
  wrote as a one-time observation — `git grep -nE '^(#|\*\(none yet\)\*)'` over every governed index
  — into a standing assertion inside a leg that already runs, so the row block is KEPT furniture-free
  rather than observed furniture-free once. This is the only option under which anything like the
  original premise becomes true, and §7's no-new-leg rule already prescribes where the arm goes, so
  it costs no `handkept_inventories_disagreeing_with_source` increment. *(b) De-author without the
  standing check.* This is exactly the falsified shape: it removes six lines and forbids nothing.
  *(c) Leave the furniture.* Zero cost, and it keeps `merge-rows.py`'s five furniture statements true.
  **Recommendation: (a) or (c); (b) is the shape the reproduction killed.** Whichever is taken, three
  things travel with it and none of them is in this unit. First, the append-only contract question:
  `memory/DECISIONS.md:3-4` and `memory/HYGIENE.md:47` are ROW-scoped and ORDER-scoped, a `## FAMILY`
  heading is not a landed row, order is preserved, and the repo already sanctions rotation, which
  moves every byte of the same file — but `APPEND_ONLY_ERE` at `check-memory-hygiene.sh:47` is
  FILE-scoped, and every consumer that asks the gate (check 2's link exemption at `:49`,
  `corpus_ids.walk` at `:196` and `:225`, `gotchas.append_only_re` at `:112`) gets a file-level
  answer. Nothing mechanical enforces it either way, so it is a contract question for the owner.
  Second, where the grouped-by-family view then lives — the four options rev-1 measured are carried
  in F2 below. Third, the record obligations, which no gate catches and which rev-1 undercounted:
  `merge-rows.py:43-45`, `:51-58` (the SPLICE rule's whole justification quotes
  `memory/DECISIONS.md:4`'s "Grouped by family for reading", which the de-authoring rewrites),
  `:87-94`, `:221-229` and `:387-389`; `memory/README.md:13`, which `adopt-memory-tree.sh:51` writes;
  `memory/HYGIENE.md:24` and its rendered template mirror; and
  `memory/map/features/memory-tree-merge-driver.md:38-40` and `:43-44`. Note also that under
  de-authoring `sections()` becomes SINGLE-VALUED, mapping all 73 ids to the H1 `# decisions — index`
  — not empty, which is what rev-1 claimed — so `no_misfiled_rows` goes vacuous rather than dead, and
  re-arms the moment any second heading enters the file.
- **F2 — if F1 is taken, where does the grouped-by-family view live?** Dependent on F1 and answerable
  only after it. Four options, measured at rev-1 and carried unchanged.
  *(a) A generated pointer index rendered by `gen_build_index.py`*, alongside `LIVE.md` and
  `ledger/<month>.md`. The machinery and the convention already exist — that script renders three
  artifacts today and `plan()` at `:330-350` is the single seam. Cost: `check-memory-hygiene.sh:211`
  gains a root-allowlist entry and `index_set()` at `:313-328` gains a selector, so it is a kit
  contract change with a version bump, a template render, an `adopt-memory-tree.sh` line and a
  selftest arm. Constraint, measured: the file must be a POINTER index (id, family, date, row
  pointer), never a copy of the row text — a copy is a second 20 KB file and instantly over check 6's
  20480 B cap, while a pointer index of 73 ids is roughly 4.4 KB and grows at about 60 B per row
  against `DECISIONS.md`'s 270 B. Second constraint: it enters check 16's read path only if
  `AGENTS.md` cites it, and the read path has 3888 B of headroom under its ceiling. The feature that
  makes this the richest honest option is that a generated index can span the LIVE file AND
  `archive/DECISIONS.*.md`, which no grep over one file can do.
  *(b) A generated region inside `DECISIONS.md` between markers.* Arithmetically dead: measured
  headroom is 413 B today and 541 B de-furnished, against roughly 2.5 to 4.4 KB for the region. It
  also asks a generator to rewrite part of an append-only file, which contradicts F1's contract
  residue rather than answering it.
  *(c) Drop the grouped view.* Zero cost, and the honest baseline: the id prefix already carries the
  family, `grep '^- TOOL-' memory/DECISIONS.md` reproduces the grouping in one command, and
  `python tools/memory-recall/query.py` is this repo's actual answer to "find the record". What it
  loses is the cross-rotation view.
  *(d) `memory/guides/decisions-by-family.md`.* Passes the bar with NO change to
  `check-memory-hygiene.sh` — check 3 treats `D:guides` as opaque and `index_set()` at `:326` already
  caps `guides/*.md`. Rejected on category: `index_set()`'s own comment says a guide is prose, not
  index rows, and guides carry an explicit exemption from the 300-char entry budget, so a generated
  index filed there would sit under no entry budget at all.
  **Recommendation: (a)**, with (c) as the fallback if the owner does not want another kit-contract
  change in this build. Both are defensible; (b) and (d) are not.
- **F3 — `memory/DECISIONS.md` is 413 B from check 6's cap and this unit needs to append.** One mean
  row of headroom, and this unit has more than one decision worth recording (the widening, the two
  folded defects, and the falsification itself). Options: *(a)* append ONE combined row, as S9
  specs, and let the rotation arrive on its own schedule; *(b)* rotate to
  `memory/archive/DECISIONS.<date>.md` first and append freely to a fresh live file, which edits
  nothing at all and is already sanctioned by `check-memory-hygiene.sh:348`, but leaves the merge
  driver inert on an empty row block until rows re-accumulate; *(c)* record the surplus decisions in
  `memory/backlog/TOOL.md` instead, which is not the durable home for a decision. **Recommendation:
  (a)**, because the driver is the thing three review rounds were spent on and this unit should not
  be the one that switches it off, and because the rotation deserves its own commit and its own
  decision row rather than riding in as a side effect of a grammar widening.
- **F4 — does `merge-rows.py`'s `_ID_RE` postcondition survive the widening?** Live in this unit; S6
  depends on the answer. Its stated justification dies with S1, and round 3 already found the
  docstring wrong in the other direction as well. Options: delete it as redundant now that `key()`
  covers the suffixed form; or keep it and re-ground it on the population it demonstrably still has —
  a row-shaped line carrying an id but no anchor separator, which `key()` misses and `_ID_RE`
  catches, verified against the widened grammar. **Recommendation: keep and re-ground**, with an arm
  on that shape, because an oracle derived from the subject's own grammar is self-consistent and
  blind, which is the property the original comment got right even though its example became wrong.

## 9. Revision log

- rev-1 · 2026-08-09 · initial draft. Grounded on `tools/memory-recall/extract.py`,
  `tools/memory-tree/corpus_ids.py`, `tools/memory-tree/merge-rows.py` and its suite, and
  `tools/memory-tree/check-memory-hygiene.sh` read at `68b90fe`, and on the three review reports
  under `memory/builds/aMendedLedger/reviews/`. Every number in §4 Inventory was produced read-only,
  by binding a widened `Grammar` and re-running the shipped walkers rather than by patching the tree.
  Two defects were discovered while measuring and are folded into scope rather than filed away:
  `check-verdict-epoch.sh:52`'s `DELEGATES` stops one hop short of the grammar that decides checks
  13-16, and `recall_conf.Conf.digest()` omits the eras it claims to cover, so a warm retrieval cache
  would survive the widening unchanged. The append-only question is argued in §4 Migration and its
  residue is carried to §8 F2 for the owner rather than assumed.
- rev-2 · 2026-08-09 · **the unit's premise was falsified and the scope narrowed to match.** Folded
  the adversarial U8 spec review `u8-spec-review.md` (24 findings raised, 11 refuted, 13 survivors
  collapsing to 7 distinct defects — 3 blocking, 4 non-blocking — against rev-1 at `68b90fe`).
  THE PREMISE. Rev-1 justified two changes on one claim: that a fully keyed row block makes the merge
  driver's reproduced corruptions unreachable, so removing six furniture lines "ends the sequence"
  rather than deferring a fourth driver repair. The review falsified it and the orchestrator
  reproduced the falsification independently. On a post-de-authoring corpus with zero furniture at
  rest, ours minting three rows of which the first and third each open a `### 2026-08` sub-heading
  and theirs editing preamble prose only, the driver exits 0 having silently deleted ours' own
  heading, where `git merge-file -p` preserves both. The claim conflated the file AT REST with the
  MERGE INPUTS: a merge input is a commit, any commit may write an unkeyed line inside the row block,
  and `_ROW_RE` (`merge-rows.py:266`) never counts a `#` line as a row, so both duplicate
  postconditions are blind to headings BY CONSTRUCTION. Removing six lines forbids and detects
  nothing. THE CONSEQUENCE. The grammar widening stays, justified by retrieval alone — 53 of 91
  records reachable today, 73 of 73 rows keyed after — which is a live defect independent of any
  merge driver. The two defects rev-1 surfaced while measuring stay, because the widening triggers
  both, and each now carries an AC that must be seen to FAIL on the unfixed code (AC8, AC9). The
  heading de-authoring goes OUT, to §8 F1, carrying the falsified premise so nobody re-argues it from
  the safety angle, the measured byte math so nobody re-measures it, and the ten record obligations
  it drags with it. §1, §2, §3, §4 and §6 were rewritten so that nothing in this spec argues the
  driver becomes safe; §3 states the fourth repair as DEFERRED and S9 files it in
  `memory/backlog/TOOL.md`. Rev-1's §8 F2 (append-only legality) and F1 (the grouped-family view)
  were both contingent on the de-authoring and travel with it; the `_ID_RE` fork is renumbered F4 and
  the rotation question, which this unit now meets directly at 413 B of headroom, becomes F3.
  THE OTHER SIX FINDINGS. **B2**: AC1 asserted `94 / 103 / 5`, which occurs in no tree state — the
  nine elisions remove four ids from `cites`, so 103 is reachable only in the 9-orphan state AC1's
  own tripwire forbids, and `corpus_ids.walk` reads `git ls-files` so this untracked spec's own H1
  is invisible until it is committed. Re-measured on one stated basis and restated at `95 / 100 / 5`
  with a `95 / 104 / 9` pre-elision control; §4 Inventory's `corpus_ids` rows were re-measured on the
  same tracked basis (`57 / 62` narrow, `95 / 104` widened) so the table and the criterion can no
  longer disagree. **B3**: §4's guard table and AC6(c) claimed `sections()` returns `""` for all 73
  ids. It does not and cannot — it initialises `cur = ""` and walks the whole file from line 1, so
  the H1 `# decisions — index` sets `cur` first, and AC4 explicitly kept that H1. Both sites now
  state the observable, and the SINGLE-VALUED correction travels to F1 where the de-authoring lives.
  **N1 and N2**: rev-1 scheduled 2 of at least 5 falsified `merge-rows.py` docstring claims and
  missed `memory/README.md:13` and the codebase-map dossier entirely. Split by cause — the five
  statements the WIDENING falsifies are S7 and in scope; the ones only the de-authoring falsifies are
  F1's obligation list. **N3**: coupling 1 named `HYGIENE.template.md` as a hand-edit site. It is a
  rendered artifact, so following rev-1 reds the bar in either order; the real hand-edit site,
  `memory/HYGIENE.md:1`, appeared nowhere. Coupling 1 now states three sites in render order and bans
  hand-editing the template. **N4**: AC4 asked a silent gate to report a number — `fail 6` prints
  only on breach and check 6 has no byte-report mode — so the byte assertion moved to `wc -c`; and
  the elision disclosure said "one of the nine occurrences" sits inside quoted tool output when the
  verified fence spans `:155-161` and `:217-227` make it SIX of nine, understating the fidelity trade
  by six times. Three corrections beyond the review, each measured here. AC4 was split: its elision
  half must locate the four fixture ids through `corpus_ids.py --report`, because any hand-written
  pattern wide enough to catch the review-1 fixture id also catches the ratified correction records
  `TOOL-aMendedLedger-1b` and `-1c` at three further lines of the same file, and eliding those would
  delete a real citation of a real decision. AC12's "39 legs" baseline was a number
  `tools/run-gates.sh` never prints — the runner emits `38/38 legs passed (1 skipped)` — which is the
  same defect as N4(a) one gate over. And §2's S6 pointed at the fork number the `_ID_RE` question
  carried at rev-1. Every file:line in this spec was re-opened at `68b90fe`, and the corpus counts,
  record counts, anchor positions, block boundaries and `sections()` values above were re-measured
  read-only rather than carried over.

## 10. Reuse audit

`CODEBASE_MAP_ROOT="$(git rev-parse --show-toplevel)" python tools/codebase-map/reuse_lookup.py "id
grammar anchor regex record id"` over 258 symbols, 71 inventory keys, 3 affordance seams and 2
dossiers returns three seams and two sub-threshold accessors: `records`
(`tools/memory-tree/gotchas.py`, fan-in 6, SEAM), `anchors` (`tools/memory-tree/merge-rows.py`,
fan-in 5, SEAM), `grammar` (`tools/memory-tree/corpus_ids.py`, fan-in 4, SEAM), plus `anchor_at` and
`grammar_for` in `tools/memory-recall/extract.py` at fan-in 2 each.

**The seam this unit wires through is `grammar_for` / `anchor_at`, and the whole point is that it is
edited rather than bypassed.** The two SEAM entries with the higher fan-in are already consumers of
it: `corpus_ids.grammar` returns `extract.grammar_for(root)` (`corpus_ids.py:117`) and
`merge-rows.anchors` returns `EX.grammar_for(str(root))` plus `EX.anchor_at` (`merge-rows.py:199-200`).
So the correct reuse decision is the negative one — no new grammar, no widened copy, no per-consumer
override. One alternation, edited once, and S1 reduces it from two constructions to one before
touching it. `gotchas.records` is the third seam and does not fit: it parses front matter and derives
anchors from backticked path tokens, never from ids.

Two caveats stated rather than hidden. `reuse_lookup.py` is dark at this repo's non-canonical
`tools/` install prefix and returns a confident `no seam fits` over a zero-symbol corpus unless
`CODEBASE_MAP_ROOT` is exported — the invocation above carries it, and the defect is recorded in
`memory/map/features/codebase-map.md` under its gaps. And 69 of 71 inventory keys are still in the
shrink-only baseline, so the map ratchets coverage without yet describing the system; the two
dossiers that do exist, `codebase-map` and `memory-tree-merge-driver`, are both in this unit's path,
and the second one is edited by S7 because its keying measurement is one of the five the widening
falsifies.
