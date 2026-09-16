# TOOL-cMendedVintage-4 — the three settings-merge remedies resolve at the install prefix

**Status:** SPECCED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams tooling · order 15

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

Three shipped files tell an operator to run `settings-merge.py` at a path spelled `tools/…`, and at
any other install prefix that path names nothing. `tools/check-wiring.sh:353` resolves the merger
against `tools/` or the repo root only, and eight emission sites then carry a
`:-tools/settings-merge.py` fallback; `tools/process-monitor/adopt-process-monitor.sh:219` hardcodes
`$ROOT/tools/settings-merge.py` two lines below fragment paths the same file derives correctly; and
`tools/memory-recall/adopt-memory-recall.sh:192` carries the same two-rung loop plus a hardcoded
fallback, under a comment describing a fix the code no longer has. Derive all three from the prefix
each file already knows.

## 2. Scope (IN)

- **S1** `tools/check-wiring.sh` derives the merger's canonical location once —
  `${KIT_REL:+$KIT_REL/}settings-merge.py`, because this file sits directly under the tool root, so
  its own `KIT_REL` IS that root — and uses it both as the first `first_of` rung and as the value
  `SMERGE` falls back to when nothing resolves. Observed by AC1 and AC2.
- **S2** With `SMERGE` never empty, the eight `${smerge:-tools/settings-merge.py}` and
  `${SMERGE:-tools/settings-merge.py}` tails at `:414`, `:423`, `:425`, `:473`, `:475`, `:521`,
  `:579` and `:581` collapse to the bare variable. The literal is deleted rather than repathed,
  which is what removes the class instead of moving it. Observed by AC2.
- **S3** `tools/process-monitor/adopt-process-monitor.sh` derives `TOOL_ROOT` from its own
  `KIT_REL`, modelled line-for-line on `tools/unattended/adopt-unattended.sh:116-117`, and `:219`
  becomes `$ROOT/${TOOL_ROOT}settings-merge.py`. Observed by AC3.
- **S4** `tools/memory-recall/adopt-memory-recall.sh` derives `TOOL_ROOT` from `REL` the same way.
  The two-rung loop at `:192`, the hardcoded fallback at `:195` and the `cp` instruction at `:194`
  all spell the target-side path through it; the `<gov>/tools/…` half of that instruction stays
  literal, because it names gov's OWN checkout and is correct at gov's prefix. Observed by AC4.
- **S5** The comment above `:189` in that file, which describes a resolution the code no longer
  performs, is rewritten to describe what it now does. Observed by AC4.
- **S6** `bash tools/check-install-prefix.sh --write-ratchet` re-runs in the SAME commit and
  `tools/install-prefix-carried.txt` is committed with it. Two rows fall and a fall is SLACK, which
  reds `--check` until the ratchet is rewritten. Observed by AC5.

## 3. Non-goals (OUT)

- No change to `tools/process-monitor/adopt-process-monitor.sh:16`. That is a USAGE line a human
  reads, its ratchet row's fourth column already records the reason, and deriving it would hand the
  operator a variable to expand.
- No shared helper for the `TOOL_ROOT` derivation. It is two lines, adopters cannot import, and a
  kit file names nothing outside itself by literal — so a helper under `tools/lib/` would be exactly
  the cross-kit literal the ban exists to stop. These kits already inline `resolve_python` for the
  same reason; section 4 records the trade.
- No change to `tools/settings-merge.py` itself, and no repair of its cwd-dependent `_kit_rel()`.
  That is `TOOL-dRetiredFork-35`'s second half and is a different defect in a different file.
- No new carried-prefix waiver row. Every literal this unit touches is deleted, not justified.
- No change to the predicate that counts these literals. That is `TOOL-cMendedVintage-5`, and it is
  sequenced after this unit.

### Edges

- **consumes-from** `TOOL-cMendedVintage-3` — `${KIT_REL:+$KIT_REL/}` in S1 resolves to a
  filesystem-derived garbage prefix at a root install until that unit's loop lands. Spelling S1 on
  the broken derivation would replace a dead literal with a wrong path.
- **hands-off** `TOOL-cMendedVintage-5` — that unit widens the carried predicate to see a
  `${VAR:-tools/…}` default. Eight of the ten occurrences it would newly catch are the tails S2
  deletes, so this unit must land first or that unit's one-shot rebaseline blesses them and the
  class goes invisible again.
- **hands-off** external — an adopter installed at a prefix other than `tools/` starts receiving
  remedies that resolve on their next pull. No runbook step in this repo delivers them.

## 4. Design

### Data model

The carriers, each with the prefix it already knows and the exemplar that gets it right:

| file | line | what it spells today | what it knows |
|---|---|---|---|
| `tools/check-wiring.sh` | `353` | `first_of tools/settings-merge.py settings-merge.py` | `KIT_REL`, which IS the tool root for this file |
| `tools/check-wiring.sh` | eight sites | `${smerge:-tools/settings-merge.py}` | the same, once S1 makes `SMERGE` non-empty |
| `tools/process-monitor/adopt-process-monitor.sh` | `219` | `$ROOT/tools/settings-merge.py` | `KIT_REL` at `:81`, already used two lines above |
| `tools/memory-recall/adopt-memory-recall.sh` | `192`, `194`, `195` | `tools/settings-merge.py` | `REL` at `:44` |
| `tools/unattended/adopt-unattended.sh` | `426` | `$ROOT/${TOOL_ROOT}settings-merge.py` | the exemplar; `TOOL_ROOT` derived at `:116-117` |

### Migration

MEASURED on 2026-09-16 at BASE `859daa67`, by running the gate's own `re_ship` predicate over the
shipped population, the carried-literal counts this unit moves:

| path | row today | row after |
|---|---|---|
| `tools/check-wiring.sh` | 3 | 2 — `:353` goes; `:681` and `:714` are unrelated and stay |
| `tools/memory-recall/adopt-memory-recall.sh` | 8 | 6 — `:192` and `:195` go |
| `tools/process-monitor/adopt-process-monitor.sh` | 5 | 5 — `:219` is `/`-preceded and the predicate never counted it |

That last row is the honest part: the process-monitor defect is caught by NEITHER the predicate today
nor the widened one `TOOL-cMendedVintage-5` ships, because `/` stays in the lead-exclusion class for
reasons that unit records. It is in this unit because a review found it, and no gate will notice if a
later edit puts it back. Both falls above are SLACK, which reds `--check`, which is why S6 re-runs
the ratchet in the same commit.

### Inventory

Minted by this unit: `SMERGE_DEFAULT` in `tools/check-wiring.sh`, and `TOOL_ROOT` in each of the two
adopters — a name this repo already uses for exactly this value in
`tools/unattended/adopt-unattended.sh`, so the spelling is reused rather than chosen. Shell variables
are graded by this repo's `shell` naming cell; each is checked with
`python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>` before it is written.

### Alternatives rejected

Repathing the eight tails to `${smerge:-${KIT_REL:+$KIT_REL/}settings-merge.py}`: correct and eight
times longer, and it leaves eight copies of one derivation where one variable does. Making `SMERGE`
non-empty at the resolution site is the shorter diff and the one that deletes the idiom.

A shared `tool_root()` helper sourced by all three: an adopter script that sources a sibling kit's
file names that file by literal, which is the ban this unit is working inside. The measured cost of
inlining is two lines in each of two files; the measured cost of the helper is one new cross-kit
literal per consumer, permanently.

Deriving `TOOL_ROOT` in process-monitor from a `tools/` default rather than from `KIT_REL`: that is
the defect with a variable wrapped around it.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/check-wiring.sh` | one derived default at `:353`, eight tails collapsed |
| `tools/process-monitor/adopt-process-monitor.sh` | `TOOL_ROOT` derivation, one remedy string |
| `tools/memory-recall/adopt-memory-recall.sh` | `TOOL_ROOT` derivation, three spellings, one comment |
| `tools/install-prefix-carried.txt` | two rows fall, written by `--write-ratchet` |

## 5. Production-readiness checklist

- security — no write path changes. Every edit is to a string an operator reads and then types.
- perf / scale — none. One extra parameter expansion per run.
- error / empty / loading states — the not-installed-here case is the one the fallback exists for,
  and after S1 it names the prefix the operator actually installed at instead of a dead literal.
- observability — each remedy prints the path it resolved, so a wrong derivation is visible in the
  message itself rather than discovered when the command fails.
- risks — S1 changes what `SMERGE` holds when nothing resolves, from empty to a path. Any arm testing
  `[ -z "$SMERGE" ]` would silently stop firing; none exists today, and AC2 is written over the
  file's own text rather than over one site so a missed carrier reds.
- testing — AC1, AC3 and AC4 each run one real script in a scratch repository installed at
  `<prefix>/`. AC2 gates the CLASS across all three files. The permanent arm is declared in section 7.
- migration — section 4's Migration table, and S6's ratchet rewrite in the same commit.
- user docs — `WIRE-INTO-PROJECT.md` §3c step 4 and §3e each name the merger's install path in
  runbook prose. Those are instructions a human follows at gov's own prefix and are outside this
  unit; the three SHIPPED carriers are what it repairs.

## 6. Acceptance criteria

- **AC1** — When `check-wiring.sh` and `agent-cap.js` are installed at `<prefix>/` in a scratch git
  repository whose `settings.json` carries no agent-cap hook and NO `settings-merge.py` is present,
  `bash <prefix>/check-wiring.sh --check` prints an `UNWIRED  agent-cap` remedy naming
  `<prefix>/settings-merge.py`.
  Red when: the fallback still spells `tools/settings-merge.py`, so the operator is handed a path
  that does not exist in their tree.
  fixture: a scratch git repository under this run's short fixture root; `TOOL-cMendedVintage-3`
  must have landed or `KIT_REL` resolves to a filesystem-derived prefix here.
- **AC2** — When `git grep -n 'tools/settings-merge.py' -- tools/check-wiring.sh
  tools/process-monitor/adopt-process-monitor.sh tools/memory-recall/adopt-memory-recall.sh` runs,
  the only surviving hits are `adopt-process-monitor.sh:16`'s usage line and the `<gov>/tools/…`
  half of the memory-recall `cp` instruction.
  Red when: one of the three carriers is fixed and a sibling is not, which is the patch-the-reported-
  path shape this unit exists to avoid.
- **AC3** — When `process-monitor` is installed at `<prefix>/process-monitor/` in a scratch repository
  with a valid `.process-monitor.conf` and no wired hook, `bash <prefix>/process-monitor/adopt-process-monitor.sh --check`
  prints a remedy naming `<prefix>/settings-merge.py`.
  Red when: `TOOL_ROOT` is derived from a `tools/` default instead of from `KIT_REL`, which produces
  the identical string at gov's own prefix and a dead one everywhere else.
  fixture: the conf must parse, or the run exits at the declaration refusal before reaching `:219`.
- **AC4** — When `memory-recall` is installed at `<prefix>/memory-recall/` in a scratch repository and
  `bash <prefix>/memory-recall/adopt-memory-recall.sh --scaffold --with-hook` runs with no
  `settings-merge.py` present, the printed `cp` line and the following invocation both name
  `<prefix>/`, and the comment above them describes the resolution the code performs.
  Red when: only the invocation is derived and the `cp` destination is left literal, so the operator
  installs the tool where the next line will not look for it.
- **AC5** — When `bash tools/check-install-prefix.sh --check` runs after the commit, it exits 0, and
  the two rows named in section 4's Migration table read lower than they do at BASE `859daa67`.
  Red when: the ratchet is not rewritten in the same commit, so the fall reports as SLACK and the
  gate reds on a repair.
  figure: DERIVED — both counts come from the gate's own report at observation time; the BASE values
  are PINNED to that sha.

## 7. Gates

`check-wiring self-test` · `install-prefix (shipped surface)` · `process-monitor wiring` · `process-monitor adopter selftest` · `memory-recall skill wiring` · `hook destinations (every declared hook path ships)` · `settings-merge selftest`

New arm: `tools/check-wiring.test.sh` · a `<prefix>/` install with no merger present, asserting the
agent-cap remedy names the install prefix · no assertion floor to move.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · §6 · TOKEN SPELLING, no criterion changed. AC1, AC3 and AC4 named the scratch fixture's installed files with a literal scripts/ prefix. `tools/check-spec-tokens.py` reds on a backticked path-shaped token `git ls-files` cannot resolve, and it is right to: those are paths inside a fixture the arms build, not paths in this tree. `--dispatch` refuses every unit of the build while that checker is red, so nothing could be dispatched. They now read `<prefix>/…`, because `check_path_shaped`'s `NOT_A_TOKEN` excludes a token opening `<` — an escape by SHAPE rather than a waiver, and a truer statement of the criterion, which must hold at any install prefix that is not the tool root rather than at one spelling of it. The waiver registry was deliberately not used: it is shrink-only so a new hit cannot be waived away quietly, which is the property that forced the real fix.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the install prefix for a remedy string printed by
a wiring checker"` returned `resolve_root`, `resolve_dests` and `resolve_entry` — all govkit and
codebase-map symbols that resolve a DESCRIPTOR's paths, none of which a shell adopter can call — and
it reported `.sh` as an unscanned layer, so every carrier here is invisible to the map by
construction. The seam this unit extends was therefore read from source and is
`tools/unattended/adopt-unattended.sh:116-117`, the `TOOL_ROOT` derivation whose remedy at `:426`
already spells the merger correctly; this unit copies those two lines into the two adopters that
lack them and reuses `first_of` in `tools/check-wiring.sh:179` for the resolution rung. The recall
probe returned the record that measured the class: `TOOL-aReapedSpinner-1`'s closing diff review,
round 2, names both `settings-merge.py` sites and states that the prefix is derivable from
`$KIT_REL` and that `check-wiring.sh:299` already solves the same problem with `first_of` — a claim
verified against today's source, where that rung has moved to `:353`.

Recall terms used: `--terms "check-install-prefix carried predicate KIT_REL boundary walk repo root
empty prefix settings-merge remedy adopter install prefix ratchet rebaseline PREDICATE_EPOCH
check-wiring"`, with the question "why do shipped kit files carry a literal tools/ prefix and what
predicate catches a carried prefix at a scripts install".
