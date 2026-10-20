# Research: the memory layer, code annotations, the gotchas and the lexicon

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 25's return, verbatim. Its question is in
`prompts/2026-10-15-prompt-PLAY-dClosedLoop-1-6-researcher.md`, and its use is in
`build/2026-10-15-build-PLAY-dClosedLoop-1-layer-memory.md`.

---

I have the answers for this part. Here is what I measured in the code, the transcripts and the git history.

## Inventory

| Piece | Where | What it is |
|---|---|---|
| Annotation convention | `memory/guides/ANNOTATION-STYLE.md` (4,813 B, the same size as `tools/memory-tree/ANNOTATION-STYLE.template.md`) | A writing convention only. A1 (`:7-10`) says "Nothing grades it, no grammar defines it, no marker declares it, and no gate reads it". A2 (`:17-29`) makes citing a record voluntary. A3 (`:33-50`) sets one MUST (state the counterfactual) and five MUST NOTs. A4 (`:55-71`) says a number in a comment must be FROZEN, GATED or POINTED. A5 (`:75-84`) is the one-line test: "Delete the id, and the block must still be worth reading". |
| Who points to it | `git grep -l ANNOTATION-STYLE -- . ':!memory/builds'` | Only kit plumbing and the map: `tools/memory-tree/{README.md,adopt-memory-tree.sh}`, `tools/gate-legs.json`, `memory/map/...`. The charter (`AGENTS.md`), HYGIENE, BUILD-METHOD and TEMPLATE-SPEC never name it. |
| Id grammar | `tools/memory-recall/extract.py:158-168` | Three id eras (flat, node-scoped, session), each `FAMILY-` prefixed. The families come from conf (`:129`). |
| `gov:` markers | 19 marker names on 164 comment lines | Read by checks (see Q1). |
| Gotchas | `memory/gotchas/` (122 files, 414,608 B) | Index and selection by `tools/memory-tree/gotchas.py` (1,360 lines). |
| Lexicon | `.lexicon.conf` (46,577 B), `tools/lexicon/` | The canon is `tools/lexicon/canon.py`. Read at point of use through `/lexicon` (`AGENTS.md:125`). |
| Point-of-use seams | `.claude/settings.json:65-72` | A PostToolUse `Read` hook runs `recall-opened.js`. It only **observes** and injects nothing (`recall-opened.js:17-18, 39-41`). |
| Comment lexer | `tools/codebase-map/map_lib.py:647-672` (`_LEX_PROFILES`) | A per-language comment syntax table. Today it is used to **strip** comments (`:698-709`). Nothing extracts them. |

## Sequence: how knowledge reaches an agent at the point of use today

| # | When | Mechanism | Pull or push |
|---|---|---|---|
| 1 | The agent opens code | It reads the comments inline. That is 2,866 code Reads in 60 days, 2,395 of them sliced with offset or limit. | pull, incidental |
| 2 | Before a review | `gotchas.py --for-diff` (`AGENTS.md:121`) | pull |
| 3 | Inside a Tier-2 review | The workflow passes the `--for-diff` stdout as `checklist` (`tools/workflows/tier2-review.js:451`). `--for-paths` runs at spec commit (`tools/workflows/README.md:220,234`). | push into lenses |
| 4 | Before naming something | `/lexicon` answers `--suggest` (`AGENTS.md:125`) | pull |
| 5 | On the bar | The lexicon naming leg (`tools/gate-legs.json:1414-1435`). For gotchas the bar runs only `--selftest` (`:500-512`), which never reaches the agent. | gate |
| 6 | At kickoff | `{{TRAPS}}` (`skills/session-kickoff/MANIFEST-TEMPLATE.md:167`) and the `## classes` gotcha names (`skills/session-kickoff/SKILL.md:200`) | push, session-wide |
| 7 | The agent opens a file | Nothing is injected. The Read hook only logs (`recall-opened.js:17`). | none |

## Measurements

### Q1, the annotation census

Scope: every tracked `.sh/.py/.js/.toml/.conf/.txt` file under `tools/`, `skills/` and `.githooks/`, plus the extensionless hooks. Python is counted with `tokenize` comments plus `ast` docstrings. JS counts `//` and `/* */`. I wrote the script to the scratchpad and ran it with `python -I census.py .`.

```
LANG files lines commentlines pct
sh 132 134841 46176 34.2%
py 88 129572 36821 28.4%
js 20 18265 6442 35.3%
toml 35 4591 1494 32.5%
txt 22 983 658 66.9%
conf 1 82 70 85.4%
TOTAL 298 288334 91661
```

By bytes, full-line comments are 35.3% of the `.sh/.py/.js` and hook files (6,426,105 of 18,195,242 B).

| Category | Comment lines | Share | Example (file:line) |
|---|---:|---:|---|
| Namespaced tag (`layer:`, `step:`, `kind:`, …) | 1 | 0.00% | `tools/unattended/unattended.sh:895`. This is a grammar term (`kind:act`), not a tag, so the real count is 0. |
| Charter tag (`[class]`, …) | 1 | 0.00% | `tools/check-wiring.sh:1966` |
| Build or record id | 6,540 | 7.13% | `.githooks/commit-msg:31` `(TOOL-aWindowedPass-3)` |
| Pointer to `memory/` | 260 | 0.28% | `.githooks/pre-commit:220` → `memory/gotchas/hand-named-gate-list-green-while-the-bar-reds.md` |
| Pointer to any file | 3,552 | 3.88% | `.githooks/commit-msg:50` |
| Directive (MUST, NEVER) | 306 | 0.33% | `.githooks/pre-push:217` "THE URL IS NEVER WRITTEN" |
| `gov:` marker | 164 | 0.18% | `.githooks/pre-commit:103` `gov:root-fixture` |

The `gov:` marker vocabulary, from `git grep -ohE "gov:[a-z][a-z-]*"`: kit 195, fixed-verifiers 50, bounded-fanout 40, sequential-agents 35, literal-python 21, playbook 18, handoff 15, conf-allow-end 10, conf-allow-begin 8, argv-begin 6, argv-end 5, resume-schedule-set 3, one-extractor 3, literal-resolve 3, lander-mode-set 3, resume-schedule-default 2, lander-mode-default 2, root-fixture 1, argv 1. These counts include doc mentions.

**Ids.** 1,121 distinct ids carry 6,666 citations; TOOL accounts for 960 of the distinct ids. Of these, 35 ids (52 citations) appear nowhere under `memory/`. All 10 of those in an own family (TOOL, DEPL, KICK, PLAY) are fixtures, for example `TOOL-aThing-1` at `tools/drift-audit/selftest.py:629` and `TOOL-169` at `tools/memory-recall/selftest.py:2173`. The rest are upstream-fork families such as PKG and ARCH (`tools/memory-tree/row_grammar.py:90`, `tools/memory-recall/query.py:60`). **No real dangling id was found.**

**How much code meets ANNOTATION-STYLE.**
- Only A5 can be measured mechanically. Of 19,788 comment blocks, 4,975 carry an id. 29 of those fall below 4 words once the id is removed, for example `tools/branch-reconcile/selftest.py:137` `"""TOOL-dSweptBranches-1 AC1 to AC5."""`. That is 0.6%.
- Most of the 29 are section rulers such as `tools/hooks/scratch-guard.js:792`.
- The A3 MUST (the counterfactual) and the A4 dispositions are semantic. No script can grade them, so their compliance is **unmeasured**.

**Checks that read annotations.**

| Reader | What it reads |
|---|---|
| `tools/hooks/agent-cap.js:461,482-485` | `gov:bounded-fanout` and `gov:fixed-verifiers` on a code line |
| `tools/unattended/check-unattended.sh` | `gov:conf-allow-*` and `gov:argv-*` |
| `.githooks/straggler-guard.sh`, `tools/check-wiring.sh:594` | `gov:literal-python` |
| `.githooks/pre-commit` | `gov:root-fixture` |
| `tools/drift-audit/drift_signals.template.py:34`, `drift_report.py:2098-2105` | Ids in product source, read as a "did it ship" signal for specs and live asks |
| `tools/check-dead-paths.sh:2` | Paths to deleted files anywhere outside `memory/`, comments included |
| `tools/codebase-map/map_lib.py:698` | Strips comments; it reads none |

**Where the record and the code disagree.** A1's "no gate reads it" holds for prose that cites a record. But markers in comments are read by four gates, and drift-audit reads the ids in comments. So "no marker declares it" understates what the code already does with comments.

### Q2, whether agents use annotations

I scanned 3,574 transcript files in `~/.claude/projects/*coding-governance*/` modified since 2026-08-16. Of these, 3,502 are subagent files and the total is 2.9 GB. The scan (`tx2.py`) re-reads each Read region from today's HEAD, which is a limitation: the file content has drifted since the Read happened.

```
code-reads 2866 · region-has-id-or-ptr 1870
...followed-by-ref-record-within10 205        (11.0%)
control: another file's ids followed 88/1449  (6.1%)
exact-id-or-path-within3 46                   (2.5%)
code-read->any-memory-within10 1941           (67.7%)
```

The lift is about 1.8× over the control, but small in absolute terms. Read through the samples, the hits are mostly sessions already working on that build. Reads of the style guide itself: one transcript has a Read of `ANNOTATION-STYLE`, and 371 merely mention the name.

**Verdict:** partly measurable. Comments are read at volume, but following a cited id to its record is rare (2.5% within 3 calls). The data cannot separate following a pointer from working on the same build.

### Q3, gotchas and lexicon

| | Gotchas | Lexicon |
|---|---|---|
| Holds | 121 records plus `INDEX.md`. 118 `class` and 3 `invariant` records, 6 marked universal against a budget of 6 (`gotchas.py --report`). Average about 3.4 KB. | `.lexicon.conf`: block keys VERBS (23 rows), CELLS (4), PINS (1), and scalars `BANNED_SUFFIXES`, `LANGS`, `VERB_OFFENDER_PIN="1087"` (`:268`), `SUFFIX_OFFENDER_PIN="0"`, `ratified`. 529 of its lines are comments. Two waiver files of 8 lines each. |
| Schema | Front matter `name/description/kind` (`a-spelling-change-strands-its-readers.md:1-5`). Sections: Symptom 117, Where it bit 97, The fix 85, Cause 14, Gate 17 / Gating 14. Anchors are derived from backticked paths (`gotchas.py:17-21,64`). | One reader, `lexicon_conf.py` (`.lexicon.conf:1-2`). Canon element 0 is prescriptive (`canon.py:3-10`). |
| Hooks | none | none |
| Gate legs | `gotchas selftest` only (`gate-legs.json:500-512`) | `lexicon naming predicates` (ceiling 300, `:1414-1435`), `lexicon selftest`, `lexicon wiring` |
| Kickoff | `## classes` (`SKILL.md:200`), `{{TRAPS}}` | none |
| Calls over 60 days (Bash) | `--for-diff` 747, `--for-paths` 198, `--write` 134, `--check` 27, `--selftest` 14, unparsed 320. 531 transcript files. Plus 197 Workflow inputs and 38 Agent inputs carrying the checklist. | bare 1,305, `--suggest` 542, `--list` 127, `--check` 114, `--measure` 86, `--help` 76, `--brief` 54, `--offenders` 20. 521 transcript files. |
| Evidence of value | 276 of 517 review files cite a gotcha slug, covering 89 distinct slugs. For example `memory/builds/aBatchedArm/reviews/2026-09-14-review-TOOL-aBatchedArm-1-closing-diff-round1.md:363,369` names classes against findings D3 and D12. 523 commit-message lines since 2026-08-16 name a slug, for example `e232cd41b` and `551027cb6`, each "the bug-class checklist on the … commit" leading to a fold. 114 code-comment lines point to `memory/gotchas/`. | `VERB_OFFENDER_PIN` history (`git log -G`): 412 → 1087, mostly **upward** (absorbing new offenders). One real drain: `95737bc85` "pin 463 -> 384, the first downward move it has ever made". The other downward moves are 1 to 7. The handed drift reading is 584 of 4,948 marginal. **Refusals acted on are rare. The pin mostly absorbs.** |

### Load of a push-at-Read delivery

Measured with `gotchas.py --for-paths <file>`, which is read-only.

| File | Classes | Bytes |
|---|---:|---:|
| `tools/unattended/unattended.sh` | 28 | 8,144 |
| `tools/run-gates/run-gates.sh` | 17 | 4,962 |
| `tools/govkit/govkit.py` | 13 | 3,893 |
| `tools/check-wiring.sh` | 11 | 3,416 |
| `tools/hooks/scratch-guard.js` | 10 | 3,022 |
| `tools/memory-tree/gotchas.py` | 10 | 2,993 |
| `tools/lexicon/lexicon.py` | 8 | 2,424 |
| `skills/session-kickoff/manifest-check.sh` | 7 | 2,190 |

Every one of those selections includes the 6 universal classes.

## Gaps

| # | Gap | Evidence |
|---|---|---|
| G1 | No tags in code at all. The owner's tag namespaces (level, layer, step, …) appear in 0 comment lines. | Census |
| G2 | The convention is untemplated and non-deterministic by its own design. It explicitly refuses a grammar, a marker and a gate. | `ANNOTATION-STYLE.md:7-10, 24-26` |
| G3 | The convention is unreachable: nothing in the charter or protocols routes to it, and agents read it once in 60 days. | `git grep`, transcripts |
| G4 | No annotation index. Ids (7.1% of comment lines) and pointers exist, but nothing extracts them, and the only comment lexer strips them. | `map_lib.py:698` |
| G5 | Nothing is pushed at the point of use. The PostToolUse Read hook observes only. | `recall-opened.js:17` |
| G6 | Pointers rarely land on records: 260 `memory/` pointers against 6,540 id lines, and follow-through runs at 2.5% to 11%. | Q1, Q2 |
| G7 | No check resolves code-cited ids. They happen to resolve (0 real dangles). | Q1 |
| G8 | The lexicon gate ratchets debt upward. Only one drain in 60 days. | Pin history |

## Candidates

| # | Mechanism | Test that could make it lose | Result |
|---|---|---|---|
| **A** | **Status quo:** voluntary prose, no grammar, no index | It must (a) meet the owner's "templated and deterministic" bar and (b) show agents following pointers well above the control. | **Loses.** (a) A1 refuses any grammar. (b) The lift is 11.0% against 6.1%, and 2.5% exact. **Rejected by the reachability measurement and G2.** |
| **B** | **An inline grammar inside the existing `gov:` marker family.** A block gains one head line, `gov:note <tags> — <short desc> → <action pointer> refs=<id/path>`. Citing stays voluntary, so the shape is gated but presence is not. A generated annotation index is extracted with the `_LEX_PROFILES` lexer and queried, never loaded whole. A resolve check covers refs. | (1) **A2's signal.** On the real tree, drift-audit's shipped signal must keep discriminating: run signal 2 before and after, and expect no new "cited ⇒ shipped" flips on unshipped specs. (2) **Drift.** Mutate the code under 30 annotated blocks, then check whether the resolve gate or the index notices. A ref-only gate cannot see semantic drift, so B must not claim it does. (3) **Load.** One line per id block is about +4,975 lines, +5.4% of comment lines; the build must measure the real figure. (4) **Ignored.** After landing, re-run `tx2.py`. If follow-through stays at or below the 11% baseline, B loses to C. | The predicate already exists: there are 0 real dangling refs among 1,121 ids, so a resolve gate is green on its first run. Tests 1 to 4 are owed by the build and **not yet run**. |
| **C** | **Out-of-band anchors, pushed at Read.** No inline grammar. Records such as gotchas and map dossiers already derive path anchors (`gotchas.py:17`), and a PostToolUse Read hook, extending the `recall-opened.js` seam, injects "records anchored here" for the opened file. | (1) **Load.** Measured at 2.2 to 8.1 KB per distinct file, 6 universal classes always included. Across 2,866 code Reads in 60 days, any session reading about 15 distinct files gets roughly 60 KB unless it dedupes per session. (2) **Over-selection.** Basename matching is tree-wide, documented as recall-biased (`gotchas.py:17-20, 44-46`). (3) **Ignored.** A/B test: does injected context change the next 10 calls? | Load has been measured, and it is heavy without dedupe. It has not failed outright. Tests 2 and 3 are owed. |
| **D** | **Pointer-only code.** Code carries bare `gov:` ids and all prose moves to records. | A5 and use: agents read code slices (2,395 sliced Reads) and records rarely (2.5%). Moving the 35.3% comment-byte share away from the code removes what is actually read. | **Loses** on A5 (`ANNOTATION-STYLE.md:75-84`) and on the Read and follow-through measurement. **Rejected.** |

A per-file header block, meaning one structured docstring per file, is a granularity variant of B rather than a separate mechanism. It is subject to B's tests, at 298 files instead of 4,975 blocks. I stopped there.

## Pick

**I recommend B, with C as the runner-up.** A and D are rejected by the tests named above.

| Reason | Basis |
|---|---|
| It extends the existing seam rather than building a new one. | `gov:` is already a comment-marker family read by four gates. The comment lexer exists (`map_lib.py:647`). The id grammar is single-sourced (`extract.py:158-168`). |
| It meets the owner's "tags, short description, action pointer, references, build ids" with a templated, deterministic grammar and a generated index. | The current zero-tag state (G1) |
| It keeps A2's load-bearing property. | The grammar governs shape when a block cites a record. It does not mandate citation. |
| Its gate is the class predicate already run on the real tree. | 0 real dangles among 1,121 ids |
| It reverses one record. | ANNOTATION-STYLE A1's refusal of grammar, marker and gate must be amended, and that record says it was refused "on measurement". That build's numbers were not re-read here, so the reversal owes a check against them. |

**What the build must run before B is final:**
- Signal-2 discrimination before and after (test B1).
- The 30-block mutation probe (B2).
- A post-landing re-run of `tx2.py` against the 11.0%/6.1%/2.5% baseline (B4). If follow-through does not rise, switch to C with per-session dedupe.

The census, dangling-id and transcript scripts are in `C:/Users/d41ly/AppData/Local/Temp/claude/C--projects-coding-governance--claude-worktrees-gov-architecture-plan-e34297/1799cb98-0882-4ab8-a308-19495d2a487a/scratchpad/`.
