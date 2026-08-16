# TOOL-aDeclaredCeiling-2 — the recall corpus reaches a constraint declared in a conf

**Status:** SPECCED · rev-2 · 2026-08-16 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

The retrieval corpus is rooted at `MEMORY_ROOT`, so a constraint declared in a repo-root conf is
unreachable by construction. `TOOL-aSiftedPlaybook-1` §10 hit this and recorded it: its own recall
query could not surface `READ_PATH_CEILING`, the live prior art its design was modelled on, and the
author found it by reading the conf. Admit declared constraints into the corpus as their own
document source.

## 2. Scope (IN)

- **S1 — a DECLARED source list.** `.memory-tree.conf` gains `RECALL_EXTRA_SOURCES`, a
  space-separated list of **repo-relative** files whose declarations join the corpus. Declared, not
  globbed: a glob would sweep whatever a project happens to keep, and the kit's habit — `watch:`,
  `verify-paths:`, `PRODUCT_GLOBS` — is an enumerated list whose membership is a decision.

  Seeded with `.memory-tree.conf`, `.unattended.conf` **and `tools/template-size-limits.txt`**, the
  declaration `TOOL-aDeclaredCeiling-1` creates. The paths are repo-RELATIVE and not repo-ROOT for
  exactly that reason: a first draft said root-only, which would have left this build's own newest
  declaration outside the corpus this unit widens, and made the README's "unit 4 last because unit 3
  creates the first declaration" an empty sentence.
- **S2 — the extraction.** For each declared file, each `KEY=value` assignment becomes one chunk:
  the key, its value, and the **contiguous comment block immediately above it**, which is where this
  tree puts the justification. `READ_PATH_CEILING` is fourteen lines of movement history above one
  number, and those fourteen lines are the entire retrievable content — a chunk of just
  `READ_PATH_CEILING="86476"` would be reachable and worthless.
- **S3 — they are CHUNKS, not records.** A record is keyed by a corpus id in this tree's `FAMILY-slug-seq` grammar; a
  declaration has a KEY, not an id. Admitting them to `records` would put un-id'd rows into the set
  `anchors.json` is built from. They join `chunks`, keyed `<file>:<KEY>`.
- **S4 — absent and empty are legal.** `RECALL_EXTRA_SOURCES` unset means today's behaviour exactly;
  a declared file that does not exist is skipped with one line, not a failure. An adopter's conf has
  no such key and their corpus must keep working.
- **S5 — the arms.** `tools/memory-recall/selftest.py` gains: a declared conf's key is retrievable
  by a term from its justification comment; a key with no comment block yields a chunk carrying at
  least the key and value; an undeclared repo-root file is NOT in the corpus; an unset
  `RECALL_EXTRA_SOURCES` reproduces the pre-change corpus exactly.
- **S6 — the reproduction becomes an arm.** The concrete miss — querying for a declared byte budget
  and not getting `READ_PATH_CEILING` — is the acceptance criterion this unit is FOR, and it is
  written against that key by name.

## 3. Non-goals (OUT)

- **Indexing conf files as prose.** A conf is not a document; sweeping the whole file into chunks
  would put shell syntax and section banners into retrieval. The unit of value is the declaration
  plus its justification, and S2 says so.
- **A quality floor for the widened corpus.** No recall quality floor rides the merge bar today
  (`tools/gate-legs.json` carries the kit selftest and the skill-wiring check, and neither grades
  retrieval). Adding one is a real unit and not this one; §5 records that this change is therefore
  unmeasured against precision.
- **Widening `DURABLE` or the `spine` set.** `spine` is decision homes. A conf declaration is a
  constraint, not a decision, and the decision that SET it already lives in `DECISIONS.md`.
- **Reaching confs outside the repo root.** Machine-level or user-level config is not repo content
  and is not reproducible for another node.

## 4. Design

### The gap, reproduced

Run at BASE, with terms composed from this corpus's own jargon:

```
python tools/memory-recall/query.py "why is a repo constraint declared in a conf file rather than
  hardcoded in the gate that enforces it" --terms "declared pin conf ceiling budget shrink-only
  floor ratchet constant gate justification movement recorded"
```

40 hits. Every one is inside `memory/`. `READ_PATH_CEILING` — the exact subject, declared at
`.memory-tree.conf:71` with fourteen lines of justification — is absent, because `corpus_files()`
runs `git ls-files <MEMORY_ROOT>/` and the conf is not under it.

### Why a declared list and not a glob

A glob over repo-root dotfiles is one line shorter and admits whatever a project keeps there. The
membership of a retrieval corpus is a decision about what counts as an answer, and this tree makes
that kind of membership explicit everywhere else it matters. A declared list also fails visibly: a
file named in the list and absent from disk gets a line (S4), where a glob that matches nothing says
nothing — the vacuous-selector shape.

### Where it hooks — there are TWO enumerators, not one

`extract.corpus_files(repo, rev)` walks tracked files under the root and takes an optional `rev`,
so the same walk serves a live tree and a git revision. **It is not the only one.** `query.py`
defines a second corpus walk of its own and calls it on the query path, and its local re-extraction
sits under a comment naming the dead-plumbing class this kind of duplication produces. An earlier
draft of this section called `corpus_files()` "the single place the corpus is enumerated", which is
false and would have shipped a widening that every one of this unit's ACs — all of which shell out
to `query.py` — could not see.

Both enumerators gain the declared paths, and `tools/memory-recall/query.py` is in Files touched
below. Honouring the list in only one would make `bench.py --rev` silently narrower than a live
run, and a benchmark measuring a different corpus than the one it reports on is worse than none.

**Unifying the two walks is explicitly NOT this unit's job** — it is a real cleanup with its own
blast radius across the query path, and doing it inside a corpus widening would make both
unreviewable. Recorded as the follow-up it is.

### Files touched

| File | Change |
|---|---|
| `tools/memory-recall/extract.py` | S1's conf read, S2's extraction, S3's routing, S4 |
| `tools/memory-recall/query.py` | the SECOND enumerator, which every AC here exercises |
| `tools/memory-recall/recall_conf.py` | `RECALL_EXTRA_SOURCES` joins the resolved conf object |
| `tools/memory-recall/selftest.py` | S5's arms and S6's reproduction |
| `.memory-tree.conf` | the declaration, seeded with two files |
| `tools/memory-recall/README.md` | the new conf key and what it admits |
| `tools/memory-recall/SKILL.template.md` | its corpus-membership sentence, which this unit falsifies |
| `.claude/skills/memory-recall/SKILL.md` | the render, or `adopt-memory-recall.sh --check` reds |

No depth-1 `tools/` path is created, so no `govkit` row is owed. `.memory-tree.conf` is a watched
pathspec, so a `last-audit` re-stamp rides this commit.

### Rollout

One commit. The conf key and the code that reads it cannot land apart in either order: the key alone
is inert, and the code alone reads a key nothing declares, which S4 makes indistinguishable from an
adopter's tree.

## 5. Production-readiness checklist

- security — the corpus gains repo-root confs, which in THIS tree hold no secrets. An adopter who
  declares a conf holding credentials would index them into a local cache. The README says so at the
  key, because the kit cannot know what an adopter puts in a file they name.
- perf / scale — two files, tens of declarations. The index rebuild is 0.43s today and this is noise
  against it.
- a11y / i18n — N/A.
- error / empty / loading states — S4 is the whole of this: unset, empty, and declared-but-absent all
  behave, and only the third prints.
- observability — the skipped-file line is the only new output.
- risks — **the corpus widens and nothing measures whether retrieval got worse.** Chunks are a graded
  set for `check_recall.py`, but no gate runs it, so this change is unfalsifiable against precision by
  construction. Stated rather than implied: the arms prove the new content is REACHABLE, not that the
  ranking is still good. The non-goal above records the missing floor as a real gap.
- testing + left-shift gates — S5, plus S6 which is the original miss turned into an arm.
- migration / rollback — revert; the index is a derived cache and rebuilds.
- user docs — the kit README **and the rendered recall Skill**, which DOES state corpus membership:
  `tools/memory-recall/SKILL.template.md` tells the reader the corpus is the tracked
  `{{MEMORY_ROOT}}/` of the repo root. That sentence is false the moment this unit lands, so the
  template and the render both move. An earlier draft of this bullet claimed the opposite and said
  "Verified by reading SKILL.template.md, not assumed" — the assertion-as-read failure that the
  predecessor build's closing blocker was, one kit over. AC10 observes the rendered file.

## 6. Acceptance criteria

- **AC1** — **The recorded miss is closed.** The §4 query, run unchanged, returns a hit whose body
  is `.memory-tree.conf`'s `READ_PATH_CEILING` declaration. **This is RED at BASE** — measured, 40
  hits and none of them that key — which is the point: it is the criterion the unit exists for, and
  an AC that were already green would prove nothing. Read as "the string appears somewhere in the
  output" it IS already green, because this build's own backlog rows quote the key; the criterion
  is the DECLARATION being retrievable, not the token being present.
- **AC2** — A term appearing ONLY in a declaration's justification comment retrieves that
  declaration: `python tools/memory-recall/query.py` with a term drawn from `.memory-tree.conf`'s
  READ_PATH_CEILING comment block — and absent from its key and value — returns it. This is what proves S2 captured the comment block rather than the
  assignment line.
- **AC3** — With `RECALL_EXTRA_SOURCES` unset, the corpus is byte-identical to the pre-change corpus:
  same record count, same chunk count. The widening is opt-in and an adopter sees no change.
- **AC4** — A repo-root file NOT named in `RECALL_EXTRA_SOURCES` is absent from the corpus, proved
  against a file that exists and is tracked.
- **AC5** — A declared file that does not exist is skipped with one line and the index still builds:
  `python tools/memory-recall/query.py` succeeds with a bogus path in `RECALL_EXTRA_SOURCES`.
- **AC6** — `anchors.json` and the `records` set are unchanged by the widening — no un-id'd entry
  reaches them (S3).
- **AC7** — `python tools/memory-recall/selftest.py` exits 0, and inverting any arm from S5 reds it
  naming that arm.
- **AC8** — `bash tools/memory-recall/adopt-memory-recall.sh --check` exits 0: the rendered Skill
  still matches its template and the conf.
- **AC10** — When the RENDERED `.claude/skills/memory-recall/SKILL.md` is read, its description of
  the corpus names the declared extra sources and no longer says the corpus is only the tracked
  `MEMORY_ROOT`. AC8's `--check` is a symmetric diff of template against render: it proves they
  AGREE and cannot notice that both are stale, so this AC reads the content and AC8 does not
  substitute for it.
- **AC9** — `bash tools/run-gates.sh` is green.

## 7. Gates

- `python tools/memory-recall/selftest.py` — the kit's own arms.
- `bash tools/memory-recall/adopt-memory-recall.sh --check` — Skill/conf parity.
- `bash skills/session-kickoff/manifest-check.sh` — `.memory-tree.conf` is watched; re-stamp.
- `bash tools/memory-tree/check-memory-hygiene.sh` — the conf drives it; confirm nothing moved.
- `bash tools/run-gates.sh` at the push boundary.

## 8. Open questions

none.

## 9. Revision log

- rev-2 · 2026-08-16 · folded the round-1 spec audit. **B2**: §4 called `extract.corpus_files` "the
  single place the corpus is enumerated" and there are two — `query.py` defines and calls its own,
  and every AC in this unit shells out to `query.py`, which was in no Files-touched row. Both
  enumerators are now in scope and unifying them is recorded as the separate cleanup it is.
  **H3**: §5 asserted "the rendered Skill … documents the CLI's arguments, not the corpus
  membership. Verified by reading SKILL.template.md" — the template states corpus membership
  explicitly, so the sentence asserted as read the one thing it had not read. That is the
  predecessor's closing blocker in a different kit; the template and its render are now in scope
  and **AC10** reads the rendered file, which AC8's symmetric diff cannot. **H6**: S1 takes
  repo-RELATIVE paths and seeds `tools/template-size-limits.txt`, so unit 3's declaration is
  actually reachable and the README's ordering reason stops being empty. **L4**: AC1 says plainly
  that it is RED at BASE and what would make it falsely green.
- rev-1 · 2026-08-16 · initial draft. The gap was recorded by `TOOL-aSiftedPlaybook-1` §10 as "a real
  gap in what the retrieval corpus covers" and reproduced live during this build's design pass —
  the same query, run again, still missing the same key. S6 turns that reproduction into an arm so
  the next widening cannot regress it silently.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "declared byte budget pin justified beside its value"`
returned `row_grammar.py:do_emit_pin` and the `row-grammar` dossier's `id_pattern(conf)` affordance —
the latter is on point as a PATTERN: a kit reading a declared value out of `.memory-tree.conf` and
failing closed when it is absent. `recall_conf.py` already implements that pattern for
`MEMORY_ROOT`, `FAMILIES` and `RECALL_CACHE_BUDGET_MB`, so **the seam this unit extends is
`recall_conf.resolve()`'s conf object**, not a new reader. S1 adds a key to a resolver that already
exists, which is why the change to `recall_conf.py` is one field.

`python tools/memory-recall/query.py …` (the §4 query) is itself the reuse probe for this unit, and
its result is the defect. Recorded per M5: a probe that misses is an answer, and here the answer is
the unit's own justification rather than a reason to retry with softer words.

**A hit verified against source rather than trusted:** `extract.py:130` carries the comment "FORKED:
the corpus root is a conf value, not a literal", and `corpus_files():167` repeats it. Both are
accurate at HEAD — the root really is `CONF.memory_root` — which is why the fix is to add a second
source rather than to re-root the walk.
