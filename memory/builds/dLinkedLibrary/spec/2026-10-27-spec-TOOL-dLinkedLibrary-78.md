# TOOL-dLinkedLibrary-78 — the CI census folds a `>` block as YAML folds it and joins a continued command before matching

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 24 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 |
| [2026-10-27-build-TOOL-dLinkedLibrary-78-deviation-781.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-78-deviation-781.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-75-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 65 to 74
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-65-spec-audit.md`) confirmed
finding **id 35 at HIGH**, report item **H4**. No other id shares the item; id 34, item H3, is the header
half of the same reader and its own unit, `TOOL-dLinkedLibrary-77`.

`TOOL-dLinkedLibrary-73` S1 keeps each line of a `>` block as its own line, as for `|`, and S2 treats each
line as a line the job runs. YAML folds a `>` block's same-indent lines into one line, and a shell joins a
line ending in a backslash to the next. `TOOL-dLinkedLibrary-51` S3 normalises leading options only and
joins nothing. So `script: >` holding `npm` then `publish` runs `npm publish`, and so does `run: |`
holding `npm \` then `publish`; the census matches `npm` and `publish` apart, 51 S4's pattern never
fires, and the job grades `importable`.

This unit turns a block's lines into the commands the job runs before any pattern is matched: YAML's fold
first, the shell's continuation second. It repairs `TOOL-dLinkedLibrary-73` and builds one step after it
(order 24).

## 2. Scope (IN)

- **S1** — The fold. In `tools/memory-tree/adopt_program.py`'s block-scalar reader, once a `>` block's
  lines are read (73 S1 and S2) without their indentation, they are folded as YAML 1.2.2 §8.1.3 folds
  them: consecutive non-empty lines at the block's own indentation join into one line with one space
  between them; an empty line ends the run, so the lines either side stay separate commands; a line
  indented deeper than the block's indentation is never folded with its neighbours. A `|` block is not
  folded. Observed by AC1 and AC3.
- **S2** — The continuation. In every block scalar, after S1, a line whose last character is a backslash
  that is not itself escaped, an odd count of trailing backslashes, is joined to the next line: the
  backslash, the line break and the next line's leading whitespace become one space, repeated while the
  joined line still ends so. The join runs before 51 S3's normalisation and 51 S4's patterns. Observed by
  AC2.
- **S3** — A scalar continued on a later line. A line key's scalar, or a list item's, that continues onto
  a following line indented deeper than its own and opening neither a list item nor a key, a multi-line
  plain or quoted scalar, refuses the job as `refused: unreadable multi-line scalar <key>`. Observed by
  AC4.
- **S4** — The plants, cases of `adopt_program.py --fixture --plant ci-census`: a GitLab `script: >` block
  holding `npm` and `publish` at one indent; a GitHub `run: |` block holding `npm \` and then `publish`; a
  GitLab `script: >` block holding `npm`, an empty line and `publish`; and a GitLab `script:` list whose
  item `- npm` continues on a deeper line `publish`. Observed by AC1 to AC4.

## 3. Non-goals (OUT)

- The header that opens a block: `TOOL-dLinkedLibrary-77`.
- The block's extent: 73 S1 and S2, unchanged.
- Reading a multi-line plain or quoted scalar: 73 §3 keeps the census from reading one, and S3 refuses
  the job instead, so the census still reads none.
- Shell quoting beyond a trailing backslash: a census that matches verbs does not parse the shell.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-73` — S1's `>` block and S2's per-line reading, which S1 folds and S2 joins before matching (id 35)
- **hands-off** `TOOL-dLinkedLibrary-86` — S2's continuation and S3's split-scalar refusal, which unit 86 reads with CRs stripped, exempts comment-only lines from and documents (ids 17, 29 of the spec audit of units 75 to 80)

## 4. Design

### Evidence

- 73 S1: "Blank lines inside it are kept as lines of the block"; S2: "each of its lines is a line the job
  runs"; neither folds a `>` block.
- 51 S3 folds a command's leading options (`git -C <dir> push`) and strips `npx`-style prefixes; it joins
  no lines.
- YAML 1.2.2 §8.1.3, folded style: line folding joins non-empty lines with a space, an empty line
  becomes a line break, and more-indented lines are not folded.

### A block after S1 and S2

```yaml
release:
  script: >
    npm
    publish            # S1: folded to "npm publish"; refused: npm publish
deploy:
  run: |
    npm \
      publish          # S2: joined to "npm publish"; refused: npm publish
```

### Rollout

Order 24 beside `TOOL-dLinkedLibrary-76` and `TOOL-dLinkedLibrary-77`. All three write
`adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences the passes; this unit owns the step from a
block's lines to its commands and 77 owns the header.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4

### Alternatives rejected

- **Matching each pattern across a line break.** Every pattern of 51 S4 would need a multi-line form, and
  a folded block can also split an option from its verb, which 51 S3's normalisation then misses.
- **Reading a multi-line plain scalar by folding it.** It contradicts 73 §3, which keeps such scalars
  unread; refusing the job holds deny by default without reading them.

## 5. Production-readiness checklist

- security — closes the bypass of the publish refusal by a folded block, a continued command or a scalar
  split over lines.
- perf / scale — one pass over a block's lines.
- error / empty / loading states — a block ending in a backslash joins with nothing and ends there.
- observability — a refusal names the folded command's verb, as 51 states, or the key of the split scalar.
- risks — a test job whose command is a multi-line plain scalar is refused; the owner may rule it in.
- testing — S4's plants under `adopt_program.py --fixture`.
- migration — none: a census re-run at a new SHA re-reads.
- user docs — none under `help/`: the page names the keys read, and folding is YAML's own.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs `adopt census`, the GitLab job
  whose `script: >` block holds `npm` and `publish` at one indent reads `refused: npm publish`.
  Red when: a folded block's lines are matched one at a time.
- **AC2** — When the same plant runs, the GitHub job whose `run: |` block holds `npm \` and then `publish`
  reads `refused: npm publish`.
  Red when: a backslash-continued command is matched as two lines.
- **AC3** — When the same plant runs, the GitLab job whose `script: >` block holds `npm`, an empty line
  and `publish` reads `importable`, its two commands `npm` and `publish` kept apart.
  Red when: the fold joins lines across an empty line and invents `npm publish`.
- **AC4** — When the same plant runs, the GitLab job whose list item `- npm` continues on the deeper line
  `publish` reads `refused: unreadable multi-line scalar script`.
  Red when: a scalar split over lines reads `importable`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 AC2 AC3 AC4 · the `ci-census` plant's folded, continued, blank-separated and split-scalar jobs, the failing case staged by 73's one-line-at-a-time reading · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — What does the census do with a scalar continued on a later line (S3)?** Options: (a) leave it
  under 73 §3, unread, so `- npm` and a deeper `publish` grade `importable`; (b) fold it as YAML folds a
  plain scalar; (c) refuse the job as an unreadable multi-line scalar. (b) reads a form 73 §3 keeps
  unread, so the two specs would disagree (BUILD-METHOD M2); (a) leaves the multi-line-command class this
  unit closes open for one form. RESOLVED (agent, 2026-10-27, delegated): (c), rung 3, the most
  feature-rich survivor; deny by default, as 63's F2 settled. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 65 to 74, id 35 (HIGH, item
  H4).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-86, promoted from the spec
  audit of units 75 to 80; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-51` S2's block-scalar reader and S3's normalisation in
`tools/memory-tree/adopt_program.py`, with one step between them. `python
tools/codebase-map/reuse_lookup.py "fold a yaml folded block scalar and join backslash continued lines"`
ranked `check_line`, `render_line`, `parse_conf_line` and `unfenced_lines`, none a YAML or shell line
joiner, so no existing seam fits beyond the census's reader.

Recall terms used: `python tools/memory-recall/query.py "how does a census refuse a ci job whose text or credentials come from a block it does not read" --terms "census ci-job refused opaque step credentials default variables block scalar fold header promoted"`
