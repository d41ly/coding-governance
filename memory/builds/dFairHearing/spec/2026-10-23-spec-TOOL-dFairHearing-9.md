# TOOL-dFairHearing-9 — portability, topology and adopter migration as anchored checklist classes, and lens notes derived per preset after a swap

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dFairHearing-19

**Carries:** cl-dClosedLoop-0076@8bf57ee9 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-9-deviation-98.md](../build/2026-10-23-build-TOOL-dFairHearing-9-deviation-98.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-mark-rewrap-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-16 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-1-spec-brief.md) | research | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |
| [2026-10-23-prompt-TOOL-dFairHearing-3-readers-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-3-readers-fix-brief.md) | research | TOOL-dFairHearing-3 |
| [2026-10-23-prompt-TOOL-dFairHearing-9-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-9-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md) | spec-audit | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 |

<!-- /gen:spec-records -->

## 1. Goal

Portability, topology and adopter migration are the classes most post-review escapes fell into, and
no lens is aimed at them by default; the design keeps them off the universal checklist, whose budget
of six is full, and puts each on the checklist only for a review whose subject touches the paths it
concerns. This unit adds one class record per domain, anchored to the files where that domain's
recorded defects bit, never universal. It also lets the callers pass lens notes keyed per preset, and
derives the run's notes after a swap, so a note keyed to a default lens an opt-in replaced is reported
unread instead of refusing the run at the `lensNotes` boundary check.

## 2. Scope (IN)

- **S1** — Three class records under `memory/gotchas/`: `portability-sweep.md`, `topology-sweep.md`
  and `adopter-migration-sweep.md`, each `kind: class` and `universal: false`. Each body states the
  domain's sweep, a `## Members` section naming its member records by name, one per bullet, with no
  backticks and no extension, the files §4 lists as its only path-like backticked tokens, and the line
  that it has no machine gate. `memory/gotchas/INDEX.md` is re-rendered by `gotchas.py --write`.
  Observed by AC1, AC2 and AC3.
- **S2** — `lensNotes` in `tier2-review.template.js` accepts a per-preset form: an object whose every
  key is a literal name, `diff-review` or a member of `PRESETS`, each mapping to today's flat note map.
  The run takes the entry for its own literal, `SLOT_LITERAL`, and an absent entry is `{}`. The flat
  form keeps its meaning. An object mixing literal-name keys with lens keys is refused naming both
  forms. Only the run literal's entry is checked; another preset's entry is checked when that preset
  runs. Observed by AC4 and AC6.
- **S3** — The legal note keys are the run literal's default keys, `SLOT_DEFAULTS`, plus the opt-in
  keys swapped in. A note keyed to a default a swap displaced is accepted and reported unread, in the
  log and in RUN INTEGRITY, exactly as a skipped light lens's note is (:895-901); a note keyed to a
  swapped-in opt-in reaches that slot's prompt. Every other key still refuses by name. Observed by AC5
  and AC6.
- **S4** — The review key's input print takes the derived run notes, so a flat-form caller and a
  per-preset caller passing the same notes derive one key, and every existing caller keeps its key.
  Observed by AC7.
- **S5** — `unattended-build.template.js` forwards `lensNotes`, when its caller passes it, to the audit
  stage's review call (:1636-1663), unchanged and unchecked, and its input header block documents it.
  Observed by AC8.
- **S6** — `tools/workflows/README.md`'s `lensNotes` section (:169-174) documents the per-preset form
  and the unread report after a swap. Observed by AC9.

## 3. Non-goals (OUT)

- Making any of the three universal: `UNIVERSAL_BUDGET="6"` (`.memory-tree.conf:561`) holds six
  universal records today, and the clause says never universal.
- Editing the member records, or anchoring the three classes to a directory such as `tools/`, which
  selects most of the catalogue (`TOOL-aWeighedCompass-14`, its ask row).
- The checklist's selection by pinned range and its order by anchors: `TOOL-dFairHearing-15`.
- A conf declaring lens notes. The review-system record has the notes "declared in the review kit's
  conf"; the clause names the callers only, and a new root conf is a governance carrier it does not
  name (§8 F4).
- The swap itself, the light run's slot selection and `LIGHT_LENSES`' validity: `TOOL-dFairHearing-3`.
- The opt-in lenses for these three domains: catalogued by `TOOL-dFairHearing-3`, each awaiting its
  losing test.

### Edges

- **consumes-from** `TOOL-dFairHearing-3` — the swap, `SLOT_DEFAULTS` and each swapped slot's `replaces` field the note derivation reads
- **consumes-from** `TOOL-dFairHearing-2` — `PRESETS`, the preset names a per-preset note map is keyed by
- **consumes-from** `TOOL-dFairHearing-13` — the catalogue rule that no lens key equals a literal name, which keeps the two note forms apart
- **hands-off** `TOOL-dFairHearing-23` — finding ids 11, 35 and 51 of the round-1 spec audit: AC3's three records observed by name (its S39, AC30), AC7's key arm re-derived (its S29, AC20) and the per-preset note entry shape-checked (its S47, AC38)

## 4. Design

### Evidence

- A class record reaches a checklist only through anchors derived from the backticked path-like
  tokens of its body (`tools/memory-tree/gotchas.py:16-21`, `ANCHOR_RE` at :65); check 18 wants a
  named gate or the words "no machine gate" (:66-74), and check 19 reds an unanchored, non-universal
  class and counts the universal ones against the budget (:530-548).
- Six records are universal at base (`fixture-passes-by-finding-nothing`,
  `guard-above-a-fold-makes-its-fallback-dead`, `heredoc-escape-reaches-the-regex`,
  `inline-fence-swallows-the-rest-of-the-file`, `staged-break-substitutes-a-synthetic-value`,
  `two-answers-to-one-question`), so the budget has no room, as the review-system review found
  (`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-b.md:116`).
- The `lensNotes` check accepts only keys of the literal that runs (`LENS_KEYS`, :859-876); after
  TOOL-dFairHearing-3's swap that literal carries the opt-in's key, so a note keyed to the replaced
  default throws. A note for a lens the run skips is already accepted and reported unread (:895-901,
  the RUN INTEGRITY lines at :1788-1790).
- The review key's print carries `lensNotes` whole (:985).
- No caller in the tree passes `lensNotes`; the audit stage's review call carries none (:1636-1663).

### The three records

Each record's sweep is its domain's opt-in brief from the lens research (`[candidates]`, lines
160-172), and its anchors are files where a member bit, each one an anchor of at least one member.

| Record | Members | Anchors |
|---|---|---|
| `portability-sweep.md` | bash-c-multiline-flattens-under-msys, msys-grep-counts-cr-on-every-line, text-mode-read-eats-a-bare-cr, gate-green-by-accident-on-generated-bytes, worktree-crlf-outside-the-gated-population, signal-killed-hook-reads-as-success, process-creation-is-the-suite-cost, allowlist-narrower-than-the-root-it-guards, async-job-starts-with-sigint-ignored | `tools/check-wiring.sh`, `tools/settings-merge.py`, `tools/unattended/check-unattended.sh`, `tools/memory-tree/gen_build_index.py`, `.githooks/pre-push.test.sh`, `tools/push-main.test.sh`, `tools/unattended/run-unattended-gates.sh`, `tools/hooks/scratch-guard.js`, `tools/run-gates/run-gates.runlog.test.sh` |
| `topology-sweep.md` | a-gate-that-walks-the-repo-root-reads-other-worktrees, a-merge-of-the-default-branch-read-as-additions, hookspath-resolves-into-another-checkout, inherited-git-dir-pins-the-work-tree-to-the-cwd, merge-keeps-both-sides-of-one-derivation, witness-graded-against-a-fact-written-after-it, a-merged-in-check-can-refuse-a-pinned-record | `tools/gate-lint/sh_hygiene.py`, `tools/codebase-map/map_lib.py`, `tools/unattended/unattended.sh`, `.githooks/pre-push`, `tools/lib/kit-rel.sh`, `tools/process-monitor/adopt-process-monitor.sh`, `tools/push-main.sh` |
| `adopter-migration-sweep.md` | shipped-checker-edit-is-an-adopter-contract-change, sourced-conf-blank-overrides-the-default, a-spelling-change-strands-its-readers | `skills/session-kickoff/manifest-check.sh`, `WIRE-INTO-PROJECT.md`, `tools/memory-tree/check-memory-hygiene.sh`, `tools/govkit/registry.toml`, `tools/check-kit-versions.sh` |

Every anchor is tracked at base, read 2026-10-23 with `git ls-files --error-unmatch`. The sweeps:

- portability — CRLF and autocrlf in fresh worktrees, text-mode reads, MSYS argument and path
  rewriting, path length, Git for Windows signal semantics, spawn cost under antivirus, clock skew;
- topology — worktrees, merges and concurrent runs: a linked worktree's `GIT_DIR`, an absolute hooks
  path, a merge read as additions, a half-staged move, a lease outliving its holder, a commit under a
  running suite;
- adopter migration — what an adopter on the prior version meets: a changed key, shape, render or gate
  with no upgrade step, non-additive data, versions that must move in lockstep with no check, and an
  assumed install layout.

### The note derivation

```js
const LITERAL_NAMES = ['diff-review'].concat(PRESETS)
// per-preset when every key of a non-empty lensNotes is a literal name; flat otherwise
const runNotes = perPreset ? (lensNotes[SLOT_LITERAL] || {}) : lensNotes
// legal keys: SLOT_DEFAULTS plus the keys of slots carrying `replaces`
// read: keys of slots that run; unread: legal keys of slots that do not run, and replaced defaults
```

`runNotes` takes the place `lensNotes` holds today in the finder prompt (:1201), the read and unread
lists, RUN INTEGRITY and the input print, so the flat form's behaviour and key are unchanged.

### Files touched (estimate)

- `memory/gotchas/portability-sweep.md`
- `memory/gotchas/topology-sweep.md`
- `memory/gotchas/adopter-migration-sweep.md`
- `memory/gotchas/INDEX.md` (its render)
- `tools/workflows/tier2-review.template.js`
- `tools/workflows/tier2-review.js` (its render)
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js` (its render)
- `tools/workflows/tier2-review.test.sh`
- `tools/workflows/unattended-build.test.sh`
- `tools/workflows/README.md`

### Alternatives rejected

- **The member records as the entries, nothing new.** They are anchored and non-universal already,
  but each names one instance; a diff touching a launch site is handed the trap that bit there and
  none of the domain's others (§8 F1).
- **The notes derived in the build harness.** It holds no literal's keys, which exist only in the
  rendered review harness, so it cannot tell a replaced default from a typo (§8 F3).

## 5. Production-readiness checklist

- security — note values are caller strings appended to one lens's prompt, as today; no new surface.
- perf / scale — three more class records; each selects only for a subject touching its anchors.
- error / empty / loading states — an absent per-preset entry is `{}` and announced as today's
  no-notes warning; an empty map is the flat form's empty map.
- observability — replaced-default notes are reported unread in the log and RUN INTEGRITY.
- risks — the umbrellas widen a checklist on the paths they anchor; `TOOL-dFairHearing-15` owns
  selection and ordering.
- testing — AC1 to AC9; the arms in §7.
- migration — none: the flat form, its refusals and its key are unchanged; the records are additive.
- user docs — `tools/workflows/README.md`; no `help/` page covers the review harness.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths tools/check-wiring.sh`,
  `--for-paths tools/push-main.sh` and `--for-paths tools/govkit/registry.toml` run, the first lists
  `portability-sweep`, the second `topology-sweep` and the third `adopter-migration-sweep`; and
  `python tools/memory-tree/gotchas.py --for-paths tools/workflows/README.md` lists none of the three.
  Red when: a record is unanchored, universal, or selected for a subject outside its anchors.
- **AC2** — When a python probe builds each new record with `build_record` from
  `tools/memory-tree/gotchas.py` and each member its `## Members` section names, every anchor of the
  record is an anchor of a member, every member shares at least one anchor with it, and its
  `universal` is false.
  Red when: an anchor rests on no recorded defect, or a member is left off its domain's anchors.
- **AC3** — When `python tools/memory-tree/gotchas.py --check` runs, it exits 0, and
  `python tools/memory-tree/gotchas.py --report` counts 6 universal records.
  Red when: the index is stale, a record declares no gate, an anchor is inert, or the budget moved.
- **AC4** — When a scratch AsyncFunction run of `tools/workflows/tier2-review.js`, the shape
  the tier2-review suite's full-run arms use, runs a unit-spec audit with
  `lensNotes: { 'unit-spec': { reuse: 'N1' }, 'design-audit': { 'alternatives-and-cost': 'N2' } }`,
  the `reuse` finder prompt carries `N1` and no prompt carries `N2`; with `preset: 'design-audit'`
  the `alternatives-and-cost` prompt carries `N2` and none carries `N1`.
  Red when: a run reads another preset's notes, or drops its own.
  cost: a scratch harness modelled on that suite's stub agents.
- **AC5** — When the scratch harness, over a scratch catalogue shipping `topology`, runs a unit-spec
  audit with `optIn: { topology: 'blast-radius' }` and `lensNotes: { 'blast-radius': 'B', topology: 'T' }`,
  it proceeds, the `topology` prompt carries `T`, no prompt carries `B`, and its RUN INTEGRITY block
  names `blast-radius` among the unread notes.
  Red when: the boundary check throws on the replaced key, or the replaced note reaches a prompt.
- **AC6** — When the scratch harness runs with `lensNotes: { nope: 'x' }`, with
  `lensNotes: { 'unit-spec': { nope: 'x' } }` and with `lensNotes: { 'unit-spec': { reuse: 'x' }, reuse: 'y' }`,
  each throws before the first agent: the first two naming the legal keys, the third naming both
  forms.
  Red when: a typo'd key or a mixed object reviews on the generic brief.
- **AC7** — When the scratch harness derives the review key for one subject set with
  `lensNotes: { reuse: 'N' }` and with `lensNotes: { 'unit-spec': { reuse: 'N' } }`, the two keys are
  equal, and equal to the key base's harness derives for the flat form.
  Red when: the form of the notes, rather than the notes, moves the key.
- **AC8** — When a scratch AsyncFunction run of `tools/workflows/unattended-build.js`, the shape
  the unattended-build suite uses, with `specAudit` set passes a per-preset
  `lensNotes`, the audit's `workflow()` stub receives it unchanged; without it, it receives no
  `lensNotes` key.
  Red when: the build harness drops, rewrites or invents the notes.
- **AC9** — When `grep -n "unit-spec" tools/workflows/README.md` runs, the `lensNotes` section shows
  the per-preset form.
  Red when: the form is accepted but undocumented.

## 7. Gates

`tier2-review self-test` · `unattended-build self-test` · `verifier fan-out self-test` · `review-join self-test` · `review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/tier2-review.test.sh · covers AC4 AC5 AC6 AC7 · per-preset notes, a note keyed to a replaced default, the three refusals and the key, red against the harness TOOL-dFairHearing-3 leaves, whose check throws on the replaced key · FLOOR_ASSERTIONS in that suite, raised by the arms added
New arm: tools/workflows/unattended-build.test.sh · covers AC8 · an audit-stage run with and without `lensNotes`, red against the base harness that forwards none · that suite's assertion floor, raised by the arms added

## 8. Open questions

- **F1 — What form do the three domains take as checklist entries?** (a) One class record per domain,
  anchored to files where its member records bit, never universal. (b) Nothing new: the member
  records are anchored and non-universal already. (c) Universal records, the lens research's first
  proposal. (c) fails the clause's "never universal" and check 19's budget of six: veto 1. (b) puts
  no domain on any checklist, only its instances, so the domain sweep the clause names exists
  nowhere. (a) adds three records and states each domain's sweep where its traps bit.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F2 — What does each domain record anchor to?** (a) Directories its members touch, `tools/` and
  `.githooks/`, which select most of the catalogue on any tooling diff. (b) The files where its
  members bit, each anchor an anchor of a member. (a) is universal in all but name.
  Recommendation (b). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (b).
  widens: none · relaxes: none
- **F3 — Where are a run's notes derived per preset?** (a) In the review harness, from a per-preset
  map, against the swapped literal it holds. (b) In each caller, which holds no literal's keys.
  Recommendation (a). Rung 3. RESOLVED (agent, 2026-10-23, delegated): (a).
  widens: none · relaxes: none
- **F4 — Do lens notes need a declaration file?** The review-system record (`[lenses]`, lines 139-141) has
  the notes declared in the review kit's conf. (a) A new conf the callers read. (b) The callers'
  own arguments, which the clause names. (a) adds an install location and a root conf, a governance
  carrier `cl-dClosedLoop-0076` does not name, so veto 2 outside the grant. Recommendation (b).
  Rung 1, v2's `cl-dClosedLoop-0076`. RESOLVED (agent, 2026-10-23, delegated): (b).
  widens: none · relaxes: none
- **F5 — Does the build's grant lift veto 2?** `tools/workflows/` is a governance carrier on
  `PLAY-dClosedLoop-10`'s list; `memory/gotchas/` is on none of its six selectors.
  `cl-dClosedLoop-0076` names the lens notes passed by the callers and derived per preset after a
  swap. RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3. grants:
  PLAY-dClosedLoop-3 per-preset lens notes in the review harness and their forwarding by the build
  harness · widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the round-1 spec audit's disposal: hands-off edges to TOOL-dFairHearing-23, naming each finding the promoted unit closes on this spec and the criterion of its own it supersedes, if any.

## 10. Reuse audit

The seams extended are the bug-class catalogue and its derived anchors, `tools/memory-tree/gotchas.py`
with `records` and `build_record`, which select the three new records with no code change, and the
`lensNotes` check and its unread report in `tools/workflows/tier2-review.template.js` (:852-901),
whose skipped-lens precedent the replaced-default case reuses. `python
tools/codebase-map/reuse_lookup.py "select bug-class checklist entries by the paths a diff touches"`
ranked `build_spec_path_re` and `resolve_charter_path`, name-stem neighbours; the selection itself is
`gotchas.py --for-paths`, which the lookup did not rank and grep found, so no new selector is built.
No hit disagreed with source. The recall query's second hit, the review-system review at
`memory/builds/dClosedLoop/reviews/2026-10-16-review-PLAY-dClosedLoop-1-review-system-b.md:116`, is
why these records are not universal.

Recall terms used: `python tools/memory-recall/query.py "where do portability and topology bug classes
reach a review" --terms "portability topology adopter migration checklist anchored universal budget
gotchas lensNotes callers"`
