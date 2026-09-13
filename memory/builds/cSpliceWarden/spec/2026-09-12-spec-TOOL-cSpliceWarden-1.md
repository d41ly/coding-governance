# TOOL-cSpliceWarden-1 — rotation becomes a DECLARED mode, and one semantics replaces two

**Status:** CLOSED · rev-2 · 2026-09-13 · node c · Tier-2 · base 09a22d2b · streams tooling+playbook · order 1 · ratified 2026-09-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md](../build/2026-09-13-build-TOOL-cSpliceWarden-1-acceptance-ledger.md) | journal | TOOL-cSpliceWarden-2 TOOL-cSpliceWarden-3 TOOL-cSpliceWarden-4 TOOL-cSpliceWarden-5 |

<!-- /gen:spec-records -->

## 1. Goal

`memory/HYGIENE.md` states two incompatible rotation procedures in one paragraph, and the archive
this build repairs is what the pair produces. Replace them with a `ROTATION_MODE` key in
`.memory-tree.conf` whose two values name the two coherent disciplines, declare `cut` for this repo,
and write that one semantics into the HYGIENE pair and the charter template.

## 2. Scope (IN)

- **S1** — `ROTATION_MODE` declared in `.memory-tree.conf`, values `cut` and `snapshot`, with the
  house-shape comment block above it. Observed by **AC1**.
- **S2** — the same key in `tools/memory-tree/.memory-tree.conf.example`, declaring `snapshot`, which
  is what the kit's prose has always described and what inCMS practises. Observed by **AC1**.
- **S3** — an unrecognised value ABORTS the reader with `exit 2`, beside the existing `ENTRY_CAP_UNIT`
  validation, so a typo is never read as a mode. This is the whole of the key's readership in this
  build, and it is deliberately minimal: without it `ROTATION_MODE` would be prose with no reader,
  which `HYGIENE.md`'s own header calls the thing that rots. Observed by **AC2**.
- **S4** — the rotation paragraph in `tools/memory-tree/HYGIENE.template.md` rewritten to state the
  declared mode and what each value means, replacing both of today's contradicting sentences;
  `memory/HYGIENE.md` re-rendered from it, never hand-edited. The template states the VOCABULARY and
  never which mode this repo picked — it ships verbatim into an adopter's tree, where a
  "this repo declares `cut`" sentence would be false. The conf owns the value. Observed by **AC3**.
- **S5** — the charter template's §5 memory-tree bullet names rotation as declared rather than
  implied, at a NET-NON-POSITIVE byte cost. Observed by **AC4**.
- **S6** — `KIT_MEMORY_TREE_VERSION` bumped and the `gov:kit memory-tree@<v>` marker moved in the
  SAME commit, in both the template and its render. Observed by **AC5**.

## 3. Non-goals (OUT)

- Grading a tree against the declared mode. NOTHING in this build asserts that a rotated archive
  holds terminal rows only, or that no id sits in both a shard and its archive. That check is the
  left-shift §7 would ask for and it is deliberately unbuilt: the owner's ratified scope of
  2026-09-12 covers the repair, the declaration and the widening of checks 10 and 20, and a new
  grading check was not among the extras offered or approved. It is filed as a backlog row under this
  slug and named in the wrap-up. What this unit ships is the declaration, its validator and the
  prose.
- Repairing `memory/archive/TOOL.2026-08-17.md`. Unit 4.
- Changing check 6's cap arithmetic. Under `cut` a shard whose live rows alone exceed the cap cannot
  be rotated below it; that is the live-row floor `TOOL-aRelaxedShard-4` already records, reached
  sooner. Named here so unit 3 does not discover it as a surprise.
- Back-filling the key into an existing adopter conf. `adopt-memory-tree.sh` has never back-filled,
  and this key is not the place to change that.

### Edges

- **hands-off** `TOOL-cSpliceWarden-3` — that unit widens check 20 to the archives this mode governs,
  and its §8 F1 records that grading the mode itself is filed rather than built.
- **consumes-from** external — the owner's ratified 2026-09-12 decision that the mode is DECLARED per
  project rather than fixed by the kit, and that this repo declares `cut`.

## 4. Design

### Data model

One key, one line, two admissible bare-lowercase values, matching the `ENTRY_CAP_UNIT` idiom already
in the file:

```
ROTATION_MODE="cut"
```

The key governs STATUS-BEARING row documents — the backlog shards. `archive/DECISIONS.<date>.md`
carries no live/terminal distinction, so it rotates identically under both modes and is outside the
key's population. One key, not a `BACKLOG_ROTATION_MODE` plus a sibling nobody needs.

| value | meaning |
|---|---|
| `cut` | the archive holds TERMINAL rows only; non-terminal rows stay in the live shard; live and archive PARTITION the family, so every id is in exactly one file |
| `snapshot` | `git mv` the whole index and carry every non-terminal row forward; an id legitimately appears in both, the archive being the frozen prior state |

**There is no default and no forward resolution.** The two are different disciplines, not different
strictnesses, so neither is the safe fallback. A blank key is a question this repo has not answered,
and it stays merely unanswered here: turning a blank into a named refusal belongs with the check that
would consume the answer, which this build files rather than builds. An unrecognised value is a
different answer from a blank one and must not collapse into it — the rule
`check-memory-hygiene.sh`'s own `_cfgbad` block states — so it aborts at `exit 2`.

### Inventory

Identifiers this unit mints: `ROTATION_MODE` (conf key, UPPER_SNAKE, the cell every
`.memory-tree.conf` key is graded in).

### Migration

None for this unit's own change. An existing adopter conf lacks the key; a blank reads as undeclared
and nothing refuses it, so no adopter bar moves on upgrade. The cost of that leniency is stated
rather than hidden: an adopter can run forever undeclared, which is weaker than the prose's "has not
decided rather than defaulted", and it is the price of not breaking every tree on a kit upgrade.

### Files touched (estimate)

`.memory-tree.conf` · `tools/memory-tree/.memory-tree.conf.example` ·
`tools/memory-tree/check-memory-hygiene.sh` (the validation `case` only) ·
`tools/memory-tree/HYGIENE.template.md` · `memory/HYGIENE.md` (RENDERED) ·
`coding-governance-agents.template.md` · `AGENTS.md` (RENDERED).

The parity leg is a RENDER-and-diff, not a strip, and it is DIRECTIONAL: the template is the authored
source and the live copy its render. Editing `memory/HYGIENE.md` — the file a session naturally has
open — produces drift in the direction the leg calls an error, and the fix it prints would then
overwrite the hand edit. Template first, then `--render`, never the reverse. Neither file may be
written by a Python `write_text`: both are `eol=lf` pinned, that call emits CRLF on Windows, and
`git add` hides it.

### Alternatives rejected

- **Hardcode `cut` in the kit.** Rejected: inCMS runs `snapshot` deliberately and the kit ships to
  both. A kit that hardcodes one project's discipline makes the other's green meaningless.
- **Infer the mode from the tree.** Rejected: this repo's archives disagree with each other today, so
  inference would read the defect as the declaration.
- **Default to `cut` when blank.** Rejected: it silently converts every existing adopter to a
  discipline they did not choose, and the first they hear of it is a red bar.

## 5. Production-readiness checklist

- security — N/A — a declaration read by the gate, no new write path, no untrusted input.
- perf / scale — N/A — one shell variable read at conf source time.
- error / empty / loading states — the three states are DECLARED: valid value, blank, unrecognised.
  Blank and unrecognised resolve differently and are never collapsed.
- observability — the abort names the key and the offending value. Nothing reports an UNDECLARED key,
  which is the honest gap this unit leaves and §3 names.
- risks — the charter template sits 120 bytes under its gated ceiling, measured 2026-09-12 by
  `bash tools/check-template-size.sh`. S5 must be net-non-positive or the bar reds. This is the
  binding constraint on this unit.
- testing — AC1-AC5; the conf-validation arm joins `check-memory-hygiene.test.sh`.
- migration — none; see §4.
- user docs — `memory/HYGIENE.md` is the user doc and is S4.

## 6. Acceptance criteria

- **AC1** — When `grep -n '^ROTATION_MODE=' .memory-tree.conf tools/memory-tree/.memory-tree.conf.example`
  runs, it returns two lines, `cut` in the repo conf and `snapshot` in the example.
  Red when: either file carries no such line, or both carry the same value, which would mean the
  example was copied rather than authored.
- **AC2** — When `.memory-tree.conf` is staged with `ROTATION_MODE="Cut"` and
  `bash tools/memory-tree/check-memory-hygiene.sh` runs, it exits 2 and names `ROTATION_MODE`.
  Red when: the run exits 0 or 1, which would mean a typo was read as a mode or as a blank.
  fixture: the real conf, edited and reverted — no fixture tree needed for an abort path.
- **AC3** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it exits 0, and
  `grep -c 'carries forward every non-CLOSED/non-WONTDO row' memory/HYGIENE.md` returns 0.
  Red when: `memory/HYGIENE.md` was hand-edited instead of rendered, or the contradicting sentence
  survives the rewrite.
- **AC4** — When `bash tools/check-template-size.sh` runs after S5, it exits 0 and reports a byte
  count no greater than the 49032 measured at base `09a22d2b`.
  Red when: the §5 wording spends headroom instead of paying for itself.
  figure: 49032 is PINNED, measured 2026-09-12 at `09a22d2b`; the criterion re-derives the new
  count from the command rather than restating it. The high-water WARN stays lit and `--bump` is
  NOT run — 49032 already exceeds the recorded 48378, and that advisory should keep burning until a
  curation pass earns it back rather than being silenced by this unit.
- **AC5** — When `bash tools/check-kit-versions.sh` and `bash tools/memory-tree/check-verdict-epoch.sh`
  run, both exit 0.
  Red when: the `case` validation lands without the version bump, or the bump lands without the
  `gov:kit memory-tree@<v>` marker moving in both the template and its render. The epoch rule is
  TOPOLOGICAL — the newest behaviour-bearing engine commit must be an ancestor of, or equal to, the
  newest commit changing the version — so the two cannot be split across commits.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `template size <=48KiB` · `charter size` · `playbook parity`

New arm: `tools/memory-tree/check-memory-hygiene.test.sh` · a conf carrying `ROTATION_MODE="Cut"`, asserted to exit 2 · no assertion floor moves.

## 8. Open questions

none — the mode's declaration form, this repo's value and the example's value were all ratified by
the owner on 2026-09-12. RESOLVED (owner, 2026-09-12): rotation semantics is a declared per-project
mode; this repo declares `cut`.

## 9. Revision log

- rev-1 · 2026-09-12 · the first draft.
- rev-2 · 2026-09-13 · §2 S3 S6 · §3 · §4 · AC4 AC5 — the key's readership stated as minimal rather than implied; the grading check moved OUT of scope and §3's promise that unit 3 supplies it removed with it; the parity direction and the CRLF trap written into §4; the kit version bump added as S6 after `check-kit-versions.sh` red on three unbumped markers

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "backlog archive rotation reconcile status"` returns no
seam for rotation semantics, because none exists: no current code reads rotation semantics at all.
The seam this unit extends is instead the CONF DECLARATION seam — `load_conf` is shared by
`row_grammar.py`, `gen_build_index.py`, `gotchas.py`, `corpus_ids.py` and `drift_report.py`
(fan-in 15), and `ENTRY_CAP_UNIT` is the existing closed-set-value precedent this key copies rather
than inventing a validation form.
Recall terms used: `rotation archive backlog terminal carry-forward index cap shard hygiene check ratified supersede reconcile`
