# TOOL-dMindYourWords-13 — the tag-name vocabulary check: a tag's verbs and nouns graded, its name answered by `--suggest`, and no namespace word in `.lexicon.conf`

**Status:** OPEN · rev-2 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 16 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0274@5185348f whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 TOOL-dMindYourWords-22 TOOL-dMindYourWords-23 TOOL-dMindYourWords-24 TOOL-dMindYourWords-25 TOOL-dMindYourWords-26 TOOL-dMindYourWords-27 TOOL-dMindYourWords-28 TOOL-dMindYourWords-29 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md](../build/2026-10-29-build-TOOL-dMindYourWords-11-reuse-scout-c.md) | research | TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md](../reviews/2026-10-29-review-TOOL-dMindYourWords-1-spec-audit-round1.md) | spec-audit | TOOL-dMindYourWords-1 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-12 TOOL-dMindYourWords-11 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-8 TOOL-dMindYourWords-10 TOOL-dMindYourWords-9 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

The lexicon grades four code surfaces and no tag, so no policy key, overlay row or other tag is named against the
declared vocabulary, and `--suggest` cannot answer one (`gap-lex-10`). This unit grades the verbs and nouns of every
tag's name the core hands to `lexicon.py --tags` against the declared verbs, the declared families and the noun canon,
makes `--suggest <name> --as tag.<namespace>` answer a tag's name as it answers a function's and never with a name
whose first segment is a namespace word, and refuses a namespace word declared in `.lexicon.conf`.

## 2. Scope (IN)

Build-run precondition: PLAY-dOrderedCharter-19 S1 and S2 (the grammar and `namespaces.toml`) and
PLAY-dOrderedCharter-10 S6 and S7 (the name-check point, `lexicon.py --tags`, the `--as tag.<ns>` cell in
`resolve_cell`, the first-segment refusal, the registry read through `resolve_kit_dir`) have landed; dOrderedCharter
is an ancestor of this build through dWitnessedBar and dDeclaredLoop. This unit calls those surfaces and never
re-specs them. It also needs TOOL-dMindYourWords-1, -6, -10 and -11 built (§3 Edges), each earlier in build order.

- **S1** — The grader, `check_tag_name` in `tools/lexicon/lexicon.py`. It splits a tag on `.`; the name is the
  segments after the namespace, and each segment's subtokens come from `subtokens` (`tools/lexicon/subtokens.py:33`),
  which splits kebab. Two rules, each returning `(rule, token, answer)` findings:
  - **`verb`** — the leading subtoken of the LEAF (the last segment) is a verb when the verb form index knows it:
    `canon.build_form_index` over `canon.build_clusters(conf["CANON"])`, plus every verb a family
    `read_declared_families` returns (TOOL-dMindYourWords-10 S3) lists. It is a finding when neither a `VERBS` row nor
    a declared family declares it; the answer is the representative the index maps it to. A word no cluster and no
    family holds is not known to be a verb and is not graded (§4).
  - **`noun`** — every other subtoken of every name segment that `canon.build_form_index` maps to a different
    representative is a finding, over the noun clusters as TOOL-dMindYourWords-10 builds them (`canon.build_clusters`
    over the `NOUNS:` rows with `clusters=canon.NOUNS`); the answer is that representative.
  Observed by AC1 and AC2.
- **S2** — The verdict inside `--tags`. Each finding becomes an `Offender` whose `Offender.grade` is `debt`, its key
  the `render_offender_keys` key `<path>\t<rule>\t<identifier>` with the rule `verb` or `noun`, the identifier the
  whole tag and the path the registry's repo-relative path (§8 F5). A key the `lexicon-debt` population holds prints as
  debt and leaves the exit alone; a key it does not hold is red, exit 1, under `lexicon.pin`'s default
  `shrink-only`, through `check_debt_pin`, the pin verdict TOOL-dMindYourWords-1 S4 gives a code offender absent from
  the population, so the key's other values reach tag rows exactly as they reach code rows and this unit adds no read
  of the key. `--tags` exits 1 when the parent's shape rule or this verdict reds. Observed by AC3 and AC8.
- **S3** — The tag answer, `render_tag_answer`, the `tag.<ns>` branch of `run_suggest` (`lexicon.py:3719`). It swaps
  the leaf's verb finding and each noun finding for its answer, then, when the first name segment is a namespace word
  the registry read returns, joins the first two segments with a hyphen (§8 F4). A one-segment name whose only
  segment is, or would become, a namespace word gets the rule and no answer. No path through it prints a name whose
  first segment is a namespace word. It reads committed tables only, so the no-corpus-pass contract
  (`lexicon.py:3727-3730`) holds. Observed by AC4 and AC5.
- **S4** — `--base` on a tag cell. TOOL-dMindYourWords-6 adds `--base <dotted.Base>` to `--suggest`; with a
  `tag.<ns>` cell it exits 2 naming that a tag's name is forced by no base. Observed by AC6.
- **S5** — No namespace word in `.lexicon.conf`. `check_namespace_key` in `tools/lexicon/lexicon_conf.py` raises
  `ConfError` naming the file, the line and `tools/playbook/namespaces.toml` as the one home of the words, on a scalar
  key or block header whose name contains `NAMESPACE` in any case (called from `load_conf`'s block and scalar
  branches, `lexicon_conf.py:139` and `:159`), and on a `CELLS:` row whose extension is `tag` (called from
  `_parse_cells`, `:260`, before `parse_cell_key`). It needs no registry, so an adopter without the playbook kit is
  refused the same way. It guards the declaration TOOL-dMindYourWords-11 carries as `record-kind.lexicon-declaration`.
  Observed by AC7.
- **S6** — Every tag, policy keys and the overlay's rows among them. They reach `--tags` through the core's one call
  per run (PLAY-dOrderedCharter-10 S6): catalogue keys as the `policy` namespace's tags, which dDeclaredLoop
  registers, and the overlay's rows as the `repo` namespace's, PLAY-dOrderedCharter-32's. The findings live at landing
  are seeded into `lexicon-debt` once (§4 Migration). Observed by AC8.
- **S7** — The docs: a section of `help/tags.md` (PLAY-dOrderedCharter-10's page) on the vocabulary grading and the
  tag answer, the `--suggest` paragraph of `tools/lexicon/SKILL.template.md` and its render
  `.claude/skills/lexicon/SKILL.md`, `tools/lexicon/README.md`, and `KIT_LEXICON_VERSION` (`lexicon.py:90`) moved once.
  Observed by AC9.

## 3. Non-goals (OUT)

- `--tags`, the `--as tag.<ns>` cell, the first-segment refusal in `--tags`, the registry and its reader:
  PLAY-dOrderedCharter-10 S6 and S7, and -19 S1 and S2.
- The noun canon `canon.NOUNS`, the `NOUNS:` and `FAMILIES:` blocks and the family resolution:
  TOOL-dMindYourWords-10. This unit reads them.
- One verb per declared family per object across tags: TOOL-dMindYourWords-10's split rule grades definitions with
  their landing history, which a tag on stdin does not carry. A follow-up if tag splits are wanted.
- Conf keys as a graded surface. `gap-lex-10` names them; the clause names tags only.
- Renaming the five live policy keys §4 lists: each is another build's catalogue row, so they enter the debt
  population and drain by their owners' renames.

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade` and `render_offender_keys`, the class a tag finding takes and its ledger key, with the `lexicon-debt` population and its verdict `check_debt_pin`; without them a tag finding has no debt route and S2 is a hard red
- **consumes-from** `TOOL-dMindYourWords-6` — `--base` on `--suggest`, which S4 refuses on a tag cell
- **consumes-from** `TOOL-dMindYourWords-10` — `canon.NOUNS` and `read_declared_families`, which S1 grades nouns and verbs against
- **consumes-from** `TOOL-dMindYourWords-11` — `read_vocabulary_record`, which names the re-baseline record the landing seed of tag rows cites (§4 Migration)
- **consumes-from** external — PLAY-dOrderedCharter-10 S6 and S7 and -19 S1 and S2 (the point, `--tags`, the cell, the registry); dDeclaredLoop's `policy` namespace and PLAY-dOrderedCharter-32's overlay rows as tag populations
- **hands-off** `TOOL-dMindYourWords-22` — the `--tags` verdict through `check_debt_pin`, which that unit scopes to the tag slice (review id 1)
- **hands-off** `TOOL-dMindYourWords-23` — the tag rows the Migration seeds, which that unit's writers carry (review id 43)
- **consumes-from** `TOOL-dMindYourWords-27` — the ledger home `.lexicon-debt.txt`, where the Migration seeds the tag rows, in place of `memory/project/lexicon-debt.txt` (review id 45)
- **hands-off** `TOOL-dMindYourWords-29` — `check_tag_name`'s noun rule and the Skill and conf edits, which the minors batch repairs (review ids 28, 41)

## 4. Design

### The grade

For a tag `policy.mailbox.fetch-seconds` the name is `mailbox.fetch-seconds`, the leaf `fetch-seconds`, its leading
subtoken `fetch`. The verb form index maps `fetch` to `load` (`tools/lexicon/canon.py`, the `load` cluster), `VERBS`
declares `load` and not `fetch`, so the finding is `(verb, fetch, load)`. Nouns are graded in every segment because a
tag's non-leaf segments are its scope and objects; the verb is graded at the leaf's head, as a function's verb is its
leading subtoken, because the design checks "the verbs and nouns in tag leaves" (lexicon review :445, §8 F1).

What it does not check, stated rather than left to be found: a verb no shipped cluster, `CANON:` row or declared
family holds (an unknown word is never guessed to be a verb); a verb in a non-leaf segment; the per-object family
split (§3); a namespace word under a conf key not naming namespaces (`FOO=practice`) or abbreviated (`NS=`).

### The verdict and the population

The live population over `tools/policy/catalogue.toml`'s 267 keys, measured 2026-10-29 with the kit's own
`canon.build_form_index` and `.lexicon.conf`'s 23 `VERBS` (PINNED; the build re-derives it over the index): five leaf
verb findings, `card.store` (`:210`), `mailbox.fetch-seconds` (`:598`), `build.push` (`:998`), `annotations.lookup`
(`:1338`) and `platforms.verify` (`:1622`); no catalogue key carries `sha`, `oid`, `hash` or `digest`. The overlay and
every other namespace add what the index holds at build time.

A tag row's key: `tools/playbook/namespaces.toml<TAB>verb<TAB>policy.card.store`. The path field is the registry's,
the one file every tag's namespace is declared in, so the key is a real repo path the ledger's move mapping can read
and the tag alone makes it unique.

### Inventory

Minted: `check_tag_name` and `render_tag_answer` (`py.function`, `tools/lexicon/lexicon.py`) and `check_namespace_key`
(`py.function`, `tools/lexicon/lexicon_conf.py`), each answered `OK` by `lexicon.py --suggest <name> --as py.function`
at writing; the rule values `verb` and `noun` are I4's, not new.

### Migration

At landing the builder writes one vocabulary record of tag `unit.lexicon.pins` through TOOL-dMindYourWords-11's
route, confirms `read_vocabulary_record` returns it, and admits the tag findings `--tags` prints over the index's tags
into `lexicon-debt` once, each row carrying a `widened:<record>` disposition naming that record, the shape
`python lexicon.py --rebaseline <record>` writes for corpus rows and `check_debt_pin` admits under `shrink-only`
(TOOL-dMindYourWords-11 S8); `--rebaseline` grades the corpus only, so the tag rows are written beside its run. Additive otherwise: no conf row, cell or
pin changes; a conf carrying a namespace key was never read by anything.

### Rollout

Live at landing on the core's `tags` leg through the name-check point, and on the `lexicon selftest` leg for the
fixtures.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`
- `tools/lexicon/lexicon_conf.py`
- `tools/lexicon/selftest.py`
- `tools/lexicon/SKILL.template.md`
- `.claude/skills/lexicon/SKILL.md` (the render of the template above, written by `adopt-lexicon.sh --render`)
- `tools/lexicon/README.md`
- `help/tags.md` (created by PLAY-dOrderedCharter-10)
- `memory/project/lexicon-debt.txt` (the seed rows; the file is TOOL-dMindYourWords-1's)

### Alternatives rejected

- **Every segment's leading subtoken, or every subtoken a cluster knows, as a verb**: the probe above counts 12 and 16
  hits against the leaf rule's 5, the extra ones `install` in `install.steps` (`:1652`) and its siblings, a noun naming
  a phase; rejected for the design record's "tag leaves", not for the counts (§8 F1).
- **Refusing any `VERBS`, `FAMILIES:` or `NOUNS:` word equal to a namespace word**: `.lexicon.conf:632` declares the
  verb `check`, and the systems record names `check` a namespace (systems :255), so it reds this repository's own
  conf the day that namespace registers, and a code verb is not a tag's namespace (§8 F2).
- **A tag ledger of its own**: a second pin beside the one pin cl-dClosedLoop-0262 makes (§8 F3).

## 5. Production-readiness checklist

- security: read-only grading; the namespace words are the parent's validated registry read, never spliced here.
- perf / scale: one call per run, one pass over the names, two dict lookups per subtoken; `--suggest` keeps no corpus pass.
- error / empty / loading states: an absent registry is the parent's not-installed slot line; an absent ledger is unit 1's refusal, never an empty pass.
- observability: one line per finding naming the tag, the rule, the token and the answer, and `debt` where the ledger holds it.
- risks: noun-like leaf words a cluster holds (`store`, `push`) read as verbs; they enter the ledger as debt, and a new one is answered by `--suggest` or suppressed with a reason through TOOL-dMindYourWords-5.
- testing: AC1 to AC9 and §7's arm.
- migration: §4 "### Migration".
- user docs: `help/tags.md`, the Skill and the kit README (S7).

## 6. Acceptance criteria

- **AC1** — When `printf 'policy.demo.fetch-rows\npolicy.demo.load-rows\n' | python tools/lexicon/lexicon.py --tags`
  runs after the pass, it names `policy.demo.fetch-rows` with rule `verb`, token `fetch` and answer `load`, exits 1,
  and passes `policy.demo.load-rows`.
  Red when: the leaf's undeclared verb passes, or a declared verb is named.
- **AC2** — When the same call reads `policy.demo.digest-path`, it names rule `noun`, token `digest` and the
  representative `canon.NOUNS` gives it.
  Red when: a noun variant passes.
  fixture: TOOL-dMindYourWords-10's `sha` cluster.
- **AC3** — When `lexicon-debt.txt` in a scratch copy carries the key AC1 printed for `policy.demo.fetch-rows`, the AC1
  call prints that tag as `debt` and exits 0; with the row deleted it exits 1.
  Red when: a tag finding the population holds reds, or one it lacks passes.
  fixture: a scratch copy under `%TEMP%`.
- **AC4** — When `python tools/lexicon/lexicon.py --suggest demo.fetch-rows --as tag.policy` runs, it prints
  `use demo.load-rows`; when `--suggest repo.x --as tag.practice` runs, it prints `use repo-x` naming the
  namespace-word rule.
  Red when: a verb is left unswapped, or an answer opens with a namespace word.
- **AC5** — When `--suggest validate --as tag.policy` runs in a scratch copy whose `namespaces.toml` carries a row with
  `ns = "check"`, it prints the namespace-word rule and no `use` line, exit 0.
  Red when: it answers `check`, a name opening with a namespace word.
  fixture: a scratch registry row, since `check` is not registered at HEAD.
- **AC6** — When `python tools/lexicon/lexicon.py --suggest demo.x --as tag.policy --base unittest.TestCase` runs, it
  exits 2 naming that a tag has no base.
  Red when: `--base` is accepted on a tag cell.
- **AC7** — When `python tools/lexicon/lexicon_conf.py --print-verbs` reads a scratch copy of `.lexicon.conf` carrying
  `TAG_NAMESPACES=practice`, it exits 1 naming the line and `namespaces.toml`; a copy carrying the `CELLS:` row
  `tag.practice kebab` exits 1 the same way; the unmodified `.lexicon.conf` exits 0.
  Red when: either plant loads.
- **AC8** — When `python gov_tag.py check` runs over the tree after the pass, it prints the slot line `filled` and exits
  0, and every vocabulary finding `--tags` prints over the index's tags reads `debt`, one per `lexicon-debt.txt` tag
  row and no more.
  Red when: a live finding is absent from the population, or a tag row there names a finding no longer printed.
  figure: DERIVED at observation; the 5 catalogue findings of §4 are PINNED at 2026-10-29.
- **AC9** — When `grep -n "namespace word" tags.md` runs over the help page and
  `bash tools/lexicon/adopt-lexicon.sh --check-render` runs, the page names the vocabulary grading and the tag
  answer, and the render matches its template.
  Red when: the page is silent or the Skill render is stale.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `check-wiring self-test` · `recall floor` · `recall floor arms`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · a fixture `namespaces.toml` and `lexicon-debt.txt` under a scratch root plant each case, and two scratch confs plant the namespace key and the `tag.` cell · none

## 8. Open questions

- **F1 — Which subtoken of a tag's name is graded as its verb.** Options: (a) the leaf's leading subtoken; (b) each segment's leading subtoken; (c) every subtoken a verb cluster knows. A probe over the 267 catalogue keys counted 5, 12 and 16 findings; it decides nothing, since (b) and (c) differ from (a) only by grading scope segments such as `install` in `install.steps`. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most capable survivor: the lexicon review the clause compresses says "it checks the verbs and nouns in tag leaves" (lexicon :445), and a leaf's head is where a function's verb sits. widens: none · relaxes: none
- **F2 — How a namespace word declared in `.lexicon.conf` is recognised.** Options: (a) a scalar or block key naming `NAMESPACE`, and a `CELLS:` row on extension `tag`, both a refusal naming the registry; (b) any `VERBS`, `FAMILIES:` or `NOUNS:` word equal to a registry word, which reds the live `check` verb (`.lexicon.conf:632`) once `check` registers; (c) no conf refusal, which fails the clause's third seen-red case. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the only survivor of veto 1, needing no registry at load so a playbook-less adopter is refused alike. widens: none · relaxes: none
- **F3 — What a tag finding's verdict is.** Options: (a) red outright, which reds the five live policy keys at landing and leaves renaming other builds' catalogue rows, veto 2 outside the grant; (b) report only, which fails the clause's seen-red; (c) debt in the one `lexicon-debt` population by name, red only when absent; (d) a tag ledger of its own, a second pin against cl-dClosedLoop-0262's one pin. RESOLVED (agent, 2026-10-29, delegated): (c), rung 3, the one survivor. widens: none · relaxes: none
- **F4 — The conforming answer to a name opening with a namespace word.** Options: (a) join the first two segments with a hyphen, the shape the owner's `policy-file.*` rename took; (b) drop the first segment, losing a word the author wrote; (c) refuse with no answer, which fails the clause's "answered with a conforming one". RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most capable survivor, a one-segment name getting the rule and no answer. widens: none · relaxes: none
- **F5 — The path field of a tag row's key.** Options: (a) the registry's repo-relative path; (b) the namespace row's `source`, which is no single file for `kit`; (c) a pseudo-path `tag.<ns>`, which the ledger's move mapping cannot read as a path. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, a real path for every tag and a unique key through the tag. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft.
- rev-2 · 2026-10-29 · §3 · the Edges gain the mirror of each edge the round-1 spec audit's promoted units declare toward this unit (TOOL-dMindYourWords-22, TOOL-dMindYourWords-23, TOOL-dMindYourWords-27, TOOL-dMindYourWords-29); no scope, design or criterion moved.

## 10. Reuse audit

The seams extended: `run_suggest` (`tools/lexicon/lexicon.py:3719`) gains its `tag.<ns>` branch beside the parent's
`resolve_cell` extension (`:3632`); `subtokens` and `leading_verb` (`tools/lexicon/subtokens.py:33`, `:39`) split and
head the leaf; `canon.build_clusters` and `canon.build_form_index` (`tools/lexicon/canon.py:84`, `:150`) build both
form indexes, the noun one through `clusters=canon.NOUNS`; `render_offender_keys` (`lexicon.py:3482`) keys the
finding; `load_conf`'s branches (`tools/lexicon/lexicon_conf.py:139`, `:159`) and `_parse_cells` (`:260`) host the conf
refusal, beside `check_declaration` (`:413`). The probe
`python tools/codebase-map/reuse_lookup.py "grade the verbs and nouns of a dotted tag name against a declared vocabulary"`
ranked `leading_verb` as a SEAM, which this extends, and `check_rule_tags`
(`tools/roles/roles_lib.py`), a roles tag check over another grammar, not reused. Where a record and source disagree:
scout B cites `canon.py:72` and `:135-158` for the canon functions; source has them at `:84`, `:150` and `:167`. Scout C
cites `resolve_cell` at `:3632`, `run_suggest` at `:3719` and `check_declaration` at `lexicon_conf.py:413`, all of
which hold at `ccd1292e`.

Recall terms used: `python tools/memory-recall/query.py "how does the lexicon grade a tag name's verbs and nouns and refuse namespace words" --terms "lexicon tag namespace word suggest verb noun canon families cell refusal registry gap-lex-10"`
