# Research: the memory layer, builds

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 22's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-3-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`.

---

# Builds as a memory unit: what they are today, and a convention to make them deterministic

**Pick:** extend today's README front matter with a declared schema (candidate D) rather than move it into a separate manifest file.

- The citation-derived graph (C) loses its test: it recovers 11 of the 13 declared parent edges.
- Today's frontmatter as it stands (A) loses on owner-adjustability: 6 of 11 slug readers reject a date in the slug, and only 1 of 11 reads the slug setting that already exists.
- A separate manifest (B) adds nothing the schema doesn't give, and costs a migration across 173 folders.

I wrote and changed nothing in the repository. All probes ran from the scratchpad, read-only.

## Inventory

**[anatomy]** Command: `python kinds.py memory/builds` (walks every file and groups by kind). Sizes are in bytes.

| Kind | Files | Builds | Median | p90 | Template (file:line) | Check (id, file:line) |
|---|---|---|---|---|---|---|
| `README.md` | 167 | 167 | 6,478 | 15,621 | `render_new_build_readme`, `gen_build_index.py:3507` (only for builds opened from an ask list); `SLOT_CANON` at `:125-131` | check 9 at `check-memory-hygiene.sh:1240` with the front-matter parse at `gen_build_index.py:401-451`; check 6 cap at `:970`; leg "build README slot contract" at `gate-legs.json:475` (98 bound, 69 exempt in `memory/project/readme-contract.txt`) |
| `spec/*.md` (+`spec/units/`, 21 files) | 1,301 (+21) | 163 | 16,835 | 40,788 | `memory/TEMPLATE-SPEC.md:417`; `--new-spec` at `gen_build_index.py:6815` | check 5 at `:867`; checks 12 and 25 at `:1647` |
| `build/*.md` | 1,048 | 129 | 5,097 | 18,565 | none (only the `**Evidences:**` ledger, HYGIENE.md:595) | checks 5 and 21 (`:1324`) |
| `build/` non-md (sh, py, tsv, json, …) | 87 | ≤9 | — | — | none | check 4 admits it at `:852` |
| `prompts/*.md` | 565 | 69 | 3,268 | 8,639 | `tools/roles/handoff.py:312`, filename at `:298` (only 30 of 565 carry the `gov:handoff` marker) | checks 1, 5, 21 |
| `reviews/*.md` | 517 | 138 | 30,159 | 52,130 | report prompt `tier2-review.js:1680` (free-form) | checks 5, 21, 22 (`:1265`); 469 of 517 carry `## Verdict:` |
| `BACKLOG.md` | 126 | 126 | 3,628 | 14,795 | grammar in `backlog.py:2` | checks 4 (`:846`), 6, 13, 15 |
| `RUN.md` | 89 | 89 | 8,019 | 31,568 | writer `unattended.sh:1347` | check 4 (`:840`); `check-unattended.sh` |
| `RUN.<PHASE>.<hex>.md` | 9 | 9 | 7,369 | 49,556 | none | check 4 grammar at `:829` |

- Six folders hold only `BACKLOG.md`: aFlaggedScaffold, aResumedRelay, aSiftedFork, aTracedSpawn, aWidenedGuide and aWiredReckoning. This is legal: check 4 at `:846` lets a folder be a filing home for asks with no README.
- Filename kind tokens: spec 1,298, build 1,135, prompt 565, review 517. Six spec-folder entries don't match, and these are the `units/` directory listings.

## Sequence

How a build is minted, rendered and read today:

1. **Mint the slug.** The rule is prose only, at HYGIENE.md:173-190: "a fresh CamelCase **adjective-noun**" (`:175`), then grep the tree for collisions. Nothing checks it at mint time. The one exception is `--new-build` at `gen_build_index.py:3607`, which tests `backlog.SLUG_RE` and requires a lower-case first letter.
2. **Open the README.** It is written by hand, except for ask-mandate builds made by `cmd_new_build` (`:3588`), which writes `status: OPEN` (`:3536`).
3. **Render.** `--write` runs `collect` (`:1008`). It parses front matter and checks the required keys (`:190`, `:440`) and that slug equals the folder name (`:443`). It derives the roster (`:1096`), derives status (`:738`), and inverts `parents:` into children (`:2335-2347`). It then renders four regions: build-index, build-units, build-order and build-edges (`:103-104`).
4. **Gate.** Check 4 checks folder names and shape. Check 5 checks filenames: `[A-Za-z0-9]+` for the slug at `:885`, with no join to the folder name. One file is housed in a different build's folder: `aDrainedSluice/reviews/…TOOL-aBatchedTribunal-1-3.md`. Check 9 re-renders and byte-compares. Check 21 checks Serves bindings.
5. **Read.** The README's units table links only to specs (`:1414-1421`). Records render inside the spec they serve, through a `gen:spec-records` region present in 1,317 specs. No README routes by purpose ("read X to do Y"); 15 have an authored `## Start here` section.

## Measurements

**[read-path]** Command: `python reads.py`, over the `Read` tool_use calls and their tool_result bytes in 3,341 jsonl files (64 sessions, 3,277 subagents).

| Class | Reads | % | Bytes | % |
|---|---|---|---|---|
| `spec/` | 2,247 | 72.6 | 53,122,346 | 78.4 |
| `reviews/` | 322 | 10.4 | 8,988,508 | 13.3 |
| `build/` | 218 | 7.0 | 3,279,883 | 4.8 |
| `prompts/` | 178 | 5.7 | 1,470,036 | 2.2 |
| **README** | **111** | **3.6** | **706,840** | **1.0** |
| `RUN.md` / `BACKLOG.md` | 17 / 3 | 0.6 | 185,965 | 0.3 |

- **Past the README:** 96.4% of build-folder reads by count and 99.0% by bytes. For sessions alone, README is 19.6% of reads; for subagents, 2.3%.
- **Routing, per (transcript, build) pair** (`route.py`, 1,194 pairs):

  | Pattern | Pairs | % |
  |---|---|---|
  | Other files read, README never read | 930 | 77.9 |
  | Other files first, README later | 128 | — |
  | README first, then other files | 86 | 7.2 |
  | README only | 50 | — |

- **Bash channel, not counted in bytes above.** 10,455 `cat`/`sed -n`/`head`/`tail` calls name a build path. Of the top-10 path classes, README is 3,485 of 34,368 mentions (10.1%).
- **Most-read non-README files:**

  | Reads | File |
  |---|---|
  | 127 | `dDerivedDocket/build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md` |
  | 85 | `dDerivedDocket/spec/…-34.md` |
  | 55 | `dLoggedFlight/spec/…-8.md` |
  | 47 | `dDerivedDocket/spec/…-9.md` |
  | 46 | `…-22` |
  | 44 | `…-4` |
  | 42 / 41 | `dDerivedDocket/prompts/…-1-spec-brief.md` / `…-1-build-brief.md` |

**[slug]**
- Command: `ls memory/builds | sed 's/^[a-z]//' | awk '{print gsub(/[A-Z]/,"&")}' | sort | uniq -c` gives **173 slugs with 2 words, and none with 1 or 3**.
- Node letters: a 116, b 3, c 13, d 41.

Reader census: `blast.py` runs each reader's literal regex against `PLAY-<slug>-1`:

| Reader (file:line) | dClosedLoop / dLoop / dClosedLoopTwo | d20261015ClosedLoop | dClosedLoop20261015 | d2026-10-15ClosedLoop |
|---|---|---|---|---|
| `backlog.py:129` SLUG_RE | ok | ok | ok | REJECT |
| `roles/roles_lib.py:75` SLUG_RE `^[A-Za-z]+$` | ok | REJECT | REJECT | REJECT |
| `check-memory-hygiene.sh:818` check 4 default | ok | ok | ok | ok |
| `workflows/tier2-review.js:296` reviewSlug | ok | REJECT | REJECT | REJECT |
| `roles/handoff.py:104` UNIT_RE | ok | REJECT | REJECT | REJECT |
| `check-memory-hygiene.sh:885` check 5 | ok | ok | ok | REJECT |
| `gen_build_index.py:603` Serves id | ok | ok | ok | REJECT |
| `memory-recall/extract.py:160` ERA `[A-Za-z]{2,}` | ok | REJECT | REJECT | REJECT |
| `unattended/check-pass-order.sh:227` | ok | REJECT | REJECT | REJECT |
| `push-main.sh:583` | ok | REJECT | REJECT | REJECT |
| `unattended/lib-unattended.sh:1467` | ok | ok | ok | REJECT |

- **More id parsers with the same letters-only class:** `check-brief-recorded.sh:345`, `check-unattended.sh:778,785`, `check-arms.py:639`, `check-memory-hygiene.sh:1760`, `check-spec-tokens.py:318`, `handoff.py:122`.
- **More id parsers with a digits-allowed class:** `row_grammar.py:221`, `merge-rows.py:418`, `gen_build_index.py:817,2682`, `run-gates.sh:4898`, `unattended.sh:4818,5652`.
- **Configurable seam:** `BUILD_SLUG_RE` (`check-memory-hygiene.sh:166`) is read only by check 4, and gov's own `.memory-tree.conf` leaves it unset.
- **Word count:** no reader enforces 1 to 3 words.

**[relations]** Commands: `fm.py` and `rel.py`.

| Relation | Field | Builds declaring | Derived / checked |
|---|---|---|---|
| Parent / dependency | `parents:` (space-separated slugs) | 11 builds, 13 edges | Children derived by inversion (`:2335-2347`). Target must be an existing folder (`:2343`). No cycle check in that block. |
| Unit-to-unit inside a build | spec `### Edges`, `consumes-from` / `hands-off` | 64 builds, 744 specs | 1,511 edges. **0 cross-build**: the template requires the same build (TEMPLATE-SPEC.md:225). 414 are `external` and name no target. |
| Record-to-spec | `**Serves:**` / `**Commissions:**` | 155 / 14 builds | check 21; may cross builds (HYGIENE.md:577) |
| Build order | `· order N` in the spec header | 90 builds, 985 specs | rendered (`:1543`) |
| Ask closure | `closes` / `advances` verbs | 11 / 7 builds | backlog fold |
| Supersession | none; prose only | "supersed" appears in 110 builds | mined from prose by recall's regexes (`extract.py:663-665`), at id level, never at build level |
| Amendment | in-place `rev-N` plus a §9 entry | 1,092 specs at rev ≥ 2 | check 12 REV_SCOPE |

**[determinism]** Front-matter derivability (`derive.py`, which imports `parse_front_matter` read-only):

| Field | Derivable from other data |
|---|---|
| `node` | equals `slug[0]` in 167 of 167 |
| `roster` | equals the families of `ids` in 162 of 167 |
| `streams` | equals the disciplines of `ids` in 151 of 167 |

Typo probe: `parent: aGhostBuild` is **accepted silently**, and `parents` reads as None, because `:436-437` stores any key.

| Practice | Template | Check |
|---|---|---|
| Slug mint | prose (HYGIENE.md:173) | collision only (check 13); word count none |
| README front matter | scaffold for mandate builds only (`:3507`) | required keys and slug equality (`:440-445`); unknown keys pass |
| README authored slots | `SLOT_CANON` (`:125`) and slot limits | `--check-format`; 69 exempt |
| README generated regions | generator | check 9, byte-compared |
| Spec | TEMPLATE-SPEC.md | check 12 (deep) |
| Prompt | handoff.py | name and Serves only; 30 of 565 carry the handoff marker |
| Review body | free | verdict token only (check 22) |
| Build journal | free, plus `**Evidences:**` (774 of 1,052) | check 21 and the ledger arms |
| Relations between builds | `parents:` untyped | existence only |
| Build status | derived (`:738`) | check 9 |
| Opening a non-mandate build | none | none |

## Gaps

1. **A README is not what agents enter by.** 77.9% of (transcript, build) pairs never read it. It routes only to specs, and records route only through spec regions. Nothing sends a reader to a file by purpose.
2. **The slug rule disagrees with the owner.** HYGIENE.md:175 says "adjective-noun", which is exactly 2 words; the owner says 1 to 3. The default regex at `:818` admits anything shaped `[A-Za-z][A-Za-z0-9-]*`. Neither bound is checked.
3. **Making naming owner-adjustable is wide.** At least 11 readers across 7 kits each spell their own slug regex. A digit date in the slug breaks 6 of the 11 I probed; a hyphenated date breaks 10.
4. **Relations are untyped.** `parents:` cannot say *patches TOOL-x-3*, *amends TOOL-x-3@rev-2* or *supersedes build y*. It splits on whitespace and refuses anything that isn't a folder name (`:2343`). There is no cross-build Edges form, no supersession field, and no cycle check.
5. **Front matter is open-world.** A misspelled relation key disappears silently.
6. **Records disagree with code.**
   - The handed fact says status is "never typed", yet 9 READMEs type `status:`. The code permits that as a fallback for builds with no spec (`:741-746`), and the scaffold writes it (`:3536`).
   - HYGIENE.md:34 gives the filename grammar as `<kind>[-<FAMILY>]-<slug>-<seq>`, with the family optional (`:885`). The handed fact gives `<kind>-<id>`, with the family required.
7. **Bodies are mostly free prose.** Review bodies, build journals and 535 of 565 prompts have no template.

## Candidates

| | Mechanism | Losing test (written before running) | Result |
|---|---|---|---|
| **A** | Today's front matter, with rules hard-coded in each reader. Add typed relation keys in `parse_front_matter`. | (1) An owner changes the slug grammar through one setting; any reader that doesn't follow makes A lose. (2) A misspelled key must be refused. | **Loses both.** (1) `BUILD_SLUG_RE` has 1 of 11 readers, and a dated slug fails 6 of 11 (`blast.py`). (2) `parent:` is accepted silently (`derive.py`). |
| **B** | A typed manifest file per build (e.g. `build.toml`, parsed with tomllib like `map_lib.py:17`). It generates the README front matter, regions, LIVE.md and the graph. | (1) If the manifest holds nothing the front matter can't, B is storage churn. (2) It must not create a second answer next to the README. | **Loses (1) on cost, not on correctness.** The authored residue is slug (the folder name), `opened`, the relations, `authorized-by`/`asks`/`spec-audit` and fallback status. That is 11 flat keys today (`fm.py`), and node, roster and streams are already derivable (167, 162 and 151 of 167). Check 9 already makes the README front matter a byte-compared, generated-from-source record. B would add 173 files and a migration for no capability D lacks. |
| **C** | No declaration: derive relations from cross-build id citations in records. | It must recover the 13 declared parent edges, with each parent as the child's top citation. | **Loses.** It recovers 11 of 13 (aHoistedPass to dRatifiedSeam and dHonouredPark to dFramedEntrypoint are absent). The parent ranks first in only 5 of 13. 1,550 untyped edges, mean out-degree 10.1 (`derived.py`). Keep it only as an advisory "cited but not declared" report. |
| **D** | Today's front matter with a **declared schema**, held as values in `.memory-tree.conf` or a kit-shipped schema the conf names. It holds the key set and types, the relation kinds (`depends <slug>`, `patches <id>`, `amends <id>@rev-N`, `supersedes <slug>`, `parents` kept as an alias), and the slug grammar as policy values (node set, words 1 to 3, an optional date property). `parse_front_matter` refuses unknown keys; the generator inverts every relation kind (extending `:2335`) and renders typed edges in `build-edges`; the grammar is exported once through a print mode, the way the hygiene script already exports sets (`check-memory-hygiene.sh:312`). | (1) Flip the declared grammar in a scratch clone and run every slug reader's selftest; any reader that still hard-codes its class makes D lose. (2) Kit independence (aMouldedFolio-1 §7 reason 1, in `…aMouldedFolio-1-doc-template-census.md:273`): if the readers' kits cannot reach the conf, D needs a new shared dependency. (3) If the build front matter needs non-flat values, the schema is "a program" (same file, `:281`). | (1) **Not run.** It is the build's acceptance test and needs the change. (2) **Passes as a probe:** `.memory-tree.conf` is already read by about 15 kit directories, including roles (5 files), unattended (3), workflows (4), hooks (2) and memory-recall (3). (3) **Passes:** 11 flat keys, and every relation value is a token list. |

The date property: putting digits into the slug is what breaks 6 readers. A date can instead be a declared derived property rendered from `opened:` (owner-switchable, default off), which leaves every id parser untouched. Only an owner who enables "date in slug" would pay the 6-reader cost, and test (1) is what prices that.

## Pick

**D: declared schema over today's front matter.**

1. **It extends an existing seam.** That covers `parse_front_matter` (`gen_build_index.py:401`), the `parents` inversion (`:2335`), `render_edges` (`:1569`), and the `BUILD_SLUG_RE` setting (`check-memory-hygiene.sh:166`), which is armed today for 1 reader and needs to reach all 11.
2. **It fixes the two measured failures of A.** Unknown keys get refused, and there is one grammar source instead of 11 regexes.
3. **It gives typed relations that C cannot derive.** The derived graph misses 2 of 13 edges and outranks the true parent in 8 of 13.
4. **B's storage move buys nothing D lacks.**

**What the build must show before D counts as done:**
- Flipping the grammar on a scratch clone turns every reader in the table above green, or names each reader that stays red.
- A front matter with `parent:` is refused.
- An `amends TOOL-x-3@rev-2` declared in one build renders as an inverse edge in the target build's README, and check 9 stays byte-clean.

For the read-path finding, D's `build-edges` and a purpose-routing slot both live in the README. That only matters if the README becomes the entry point, which 77.9% of readers skip today. Whether to make it one is the owner's call, not the schema's.

Files:
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\gen_build_index.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\memory-tree\check-memory-hygiene.sh`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\HYGIENE.md`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\memory\project\readme-contract.txt`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\roles\roles_lib.py`
- `C:\projects\coding-governance\.claude\worktrees\gov-architecture-plan-e34297\tools\workflows\tier2-review.js`

Probe scripts, all read-only, are in `C:\Users\d41ly\AppData\Local\Temp\claude\C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297\1799cb98-0882-4ab8-a308-19495d2a487a\scratchpad\`: kinds.py, fm.py, rel.py, reads.py, route.py, bashr.py, derive.py, blast.py and derived.py.
