# PLAY-aDistilledCharter-4 — gov adopts v4.0: its wrapper folds into section 2 and its charter re-renders

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-1 · base 6473ae38 · streams playbook · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Gov is v4.0's first adopter. Its `AGENTS.md` carries an authored wrapper above and below the
rendered region: a product note, a layout, the four-row node registry, the merge bar and its
conventions. This unit moves what is still true and not stated elsewhere into gov's
`[charter] adopter_rules`, deletes the rest, and re-renders, so gov's charter is the region alone.

## 2. Scope (IN)

- **S1** — `.governance/deploy.toml` gains `[charter] adopter_rules`: one line per gov-specific
  rule the wrapper carries and nothing else states, the merge-bar guide pointer among them. It loses
  `drop_blocks = ["node-table"]` and the answers `machine_a`, `primary_tree_a`, `worktree_root_a`
  and `variances_a`, which TOOL-aDistilledCharter-2 retired. Observed by AC1.
  **Readers:** by name: `.governance/deploy.toml` itself, and `render_playbook.py`, whose retired
  placeholder rows were the only reader of the four answers; by value: NO VALUE READERS — the
  generated table takes the fleet registry's values, so nothing compares these any more.
- **S2** — `AGENTS.md` holds the rendered region and nothing outside it; its first
  `## Node registry` is the generated one. Observed by AC1 and AC2.
- **S3** — The `AGENTS.md` row of `tools/template-size-limits.txt` and
  `tools/template-size-highwater.txt` re-declares the charter ceiling just above its new size.
  Observed by AC3.

## 3. Non-goals (OUT)

- Any adopter other than gov.
- The template. PLAY-aDistilledCharter-1.

## 4. Design

Each wrapper paragraph at BASE gets one of three fates, recorded in the unit's build record: a
section-2 line, already stated by a v4.0 practice or guide (deleted), or stale (deleted, with the
evidence). The wrapper's node table is replaced by the generated one, whose rows carry the same four
tags.

### Files touched (estimate)

`AGENTS.md` · `.governance/deploy.toml` · `tools/template-size-limits.txt` · `tools/template-size-highwater.txt`

## 6. Acceptance criteria

- **AC1** — When `bash tools/playbook/adopt-playbook.sh --target . --check` runs, it prints
  `render-playbook OK`. Red when: it reports drift or a surviving placeholder.
- **AC2** — When `bash skills/session-kickoff/manifest-check.sh --card --write` runs on node `a`,
  its `node —` cell reads `a · daily-agent`. Red when: it reads UNKNOWN or another tag.
- **AC3** — When `bash tools/check-template-size.sh AGENTS.md` runs, it is green under the new row,
  and `wc -c AGENTS.md` is below the 32768 bytes a Codex agent reads.
  Red when: the row still reads 64512, or the file exceeds 32768.

## 7. Gates

`playbook render wiring` · `charter size` · `agent-instructions wiring` · `memory hygiene` · `kickoff-manifest ratchet`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
