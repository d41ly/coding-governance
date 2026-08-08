# TOOL-aFoldedQuarry-3 — U1: retire the discipline directory axis, keep the discipline signal

**Status:** CLOSED · rev-2 · 2026-08-08 · node a · Tier-2 · base 42c3f4dc · streams tooling · ratified 2026-08-08

## 1. Goal

Take the discipline out of the PATH and put it in the spec status header as a closed enum, so a build
that spans two disciplines is one build instead of two folders. Change the kit, then migrate this
repo's own tree as the kit's first customer.

## 2. Scope (IN)

- **S1** — build folders move from `<MEMORY_ROOT>/<disc>/builds/<date>-<FAMILY>-<slug>/` to
  `<MEMORY_ROOT>/builds/<slug>/`. No discipline segment, no date prefix, no FAMILY prefix.
- **S2** — the four `DECISIONS.md` files concatenate into one append-only
  `<MEMORY_ROOT>/DECISIONS.md`, rows verbatim, grouped by family in a stable order.
- **S3** — backlogs stay sharded and mutable, one file per FAMILY at
  `<MEMORY_ROOT>/backlog/<FAMILY>.md`.
- **S4** — the spec status header gains an optional `· streams <value>[+<value>…]` segment over the
  CLOSED enum `.memory-tree.conf` declares. Whenever present it is validated. It becomes REQUIRED
  for specs whose filename date is on or after `STREAMS_CUTOFF`.
- **S5** — `STREAMS_CUTOFF` is set STRICTLY AHEAD of every committed spec's filename date, so the
  required arm has no corpus to exercise it. That arm therefore ships with explicit red and green
  fixtures in the self-test, not with a comment claiming it works. The other half of that choice is
  said out loud: every spec written from the cutoff date onward MUST carry `streams`, so the next
  session meets the requirement from `SPEC-TEMPLATE.template.md` rather than from a red gate.
- **S6** — the recording-file grammar gains an OPTIONAL FAMILY qualifier,
  `<date>-<kind>-<FAMILY>-<slug>-<seq>.md`, which is how one slug shared by two families survives the
  merge into a single folder. It is required nowhere and permitted everywhere.
- **S7** — `.memory-tree.conf`'s `DISCIPLINES` stops naming directories and starts naming the enum's
  legal values. `FAMILIES` keeps its `value:FAMILY` shape and now maps an enum value to its backlog
  shard and id prefix.
- **S8** — `check-memory-hygiene.sh` checks 3, 4, 5, 8, 10 and 12, its `index_set`, and the
  `gen-memory-tree.sh` root render all move to the flat shape.
- **S9** — this repo's `memory/` migrates in the same commit, every move by `git mv`.
  `2026-07-19-PLAY-aPrunedCeremony` and `2026-07-19-TOOL-aPrunedCeremony` are ONE session under two
  disciplines and merge into `builds/aPrunedCeremony/`, which is the case the flatten exists for.
- **S10** — `HYGIENE.template.md`, `SPEC-TEMPLATE.template.md`, `adopt-memory-tree.sh`,
  `hygiene-parity.test.sh`, `memory/README.md`, `AGENTS.md` and the kickoff manifest's pointer map
  all describe the flat shape. Relative links inside a moved build folder are swept: the folder is
  one directory level shallower, so any link that climbs out of it resolves somewhere new.
- **S11** — every population this unit retargets ASSERTS IT IS NON-EMPTY. Six selectors change
  segment count at once, and a selector left at the old count matches nothing, prints nothing, and
  is indistinguishable from a passing check. A tree that demonstrably holds specs, build folders and
  status files must not yield an empty population, and the check says so when it does.
- **S12** — `gen-memory-tree.sh` narrows its unit list to `root` and its root render lists the flat
  children. In `--check` an absent target counts as drift, so leaving the discipline units in place
  would red check 9 on every run the moment their directories are deleted.

## 3. Non-goals (OUT)

- Draining `<MEMORY_ROOT>/project/`. The in-flight ledger, the journal and the memory index stay
  exactly where they are; the upstream build that drained them is not in this port's scope.
- Retiring the generated tree file. That is U2. This unit only narrows the generator to the root
  render, because the per-discipline files it wrote are being deleted with their directories.
- Renumbering or rewriting any ratified id. Six recording files gain a FAMILY qualifier in their
  FILENAME; their content and their ids are untouched.
- Repointing the citations that the moves invalidate. That is the dead-path registry in U3. This
  unit must not leave a broken markdown LINK, which hygiene check 2 already enforces.

## 4. Design

### Data model

```
<MEMORY_ROOT>/
├── README.md · TREE.md · HYGIENE.md · TEMPLATE-SPEC.md
├── DECISIONS.md          append-only, every family
├── backlog/<FAMILY>.md   mutable, one shard per family
├── decisions/ guides/ archive/     optional, opaque
├── builds/<slug>/        README.md · STATUS.md · prompts/ spec/ build/ reviews/
└── project/              unchanged
```

The status header becomes:

```
**Status:** <TOKEN> · rev-<N> · <date> · node <tag> · Tier-<1|2> · base <sha8>[ · streams <v>[+<v>]][ · <tail>]
```

`streams` is parsed by locating the segment anywhere after `base`, so it composes with an existing
pointer tail rather than fighting it for position.

The optional recording qualifier is `<date>-<kind>-<FAMILY>-<slug>-<seq>.md` where `<FAMILY>` comes
from the `FAM_ALT` alternation the kit already derives from `FAMILIES` — not a generic `[A-Z]+`,
which would admit a family that does not exist and make AC5's rejection arm vacuous.

### Inventory

| Check | Before | After |
|---|---|---|
| 3 structure | root: the discipline dirs; depth-2 per discipline | root: `DECISIONS.md`, `backlog/`, `builds/`, `decisions/`, `guides/`, `archive/`, `project/` |
| 4 build folder | `<date>-<FAMILY>-<slug>` under each discipline | `<slug>` under one `builds/`; FAMILY pairing retires with the directory |
| 5 recording name | `<date>-<kind>-<slug>-<seq>.md` | same, plus an optional FAMILY qualifier |
| 8 status vocab | `<disc>/BACKLOG.md` | `backlog/<FAMILY>.md` |
| 10 rotation | `<disc>/archive/` | `<MEMORY_ROOT>/archive/` |
| 12 spec format | header without streams | header with the validated optional enum, required past the cutoff |
| `index_set` | four sets of four discipline indexes | one `DECISIONS.md` plus the backlog shards |

### Migration

Every move is `git mv`, so history follows the file. Two folders merge:
`playbook/builds/2026-07-19-PLAY-aPrunedCeremony/` and `tooling/builds/2026-07-19-TOOL-aPrunedCeremony/`
become `builds/aPrunedCeremony/`. Their two build-root `README.md` files and their colliding
`spec-…-1.md` and `spec-…-2.md` names are the reason S6 exists: every recording inside that one
folder takes the FAMILY qualifier, and the two READMEs merge into one whose two sections are the two
original texts.

### Rollout

One commit: kit change plus migration plus the doc rewrites. Splitting them would leave the bar red
in between, because the kit's checks and the tree's shape are the same statement said twice.

### Files touched (estimate)

Seven kit files, about 60 tracked files under `memory/`, and four documents that point at the old
shape.

### Alternatives rejected

- **Disambiguate the collision by suffixing the folder slug.** Rejected: the two folders are one
  session under two disciplines, and expressing that is the whole point of the flatten.
- **Put the colliding family's recordings in a sub-folder under `spec/`.** Rejected: it is asymmetric
  (one family plain, the other nested) and it hides the family in a path segment, which is the axis
  this unit is removing.
- **Require `streams` on every spec.** Rejected: it would retroactively red every landed spec. The
  cutoff is the same grandfathering device `SPEC_FORMAT_CUTOFF` and `SPEC10_CUTOFF` already use.

## 5. Production-readiness checklist

- security — N/A. No new execution surface; the enum is compared, never evaluated.
- perf / scale — the per-discipline loops collapse into single passes, so the gate gets cheaper.
- a11y — N/A — no user interface.
- i18n — N/A.
- error / empty / loading states — a repo with no `builds/` yet, or an empty backlog shard, is a
  clean pass, not a crash.
- observability — the streams failure names the illegal value AND the legal set.
- risks — the migration is the risk. `git mv` only, one commit, and the gate is the acceptance test.
- testing + left-shift gates — hygiene self-test arms for the new shapes plus the two cutoff arms.
- migration / rollback — a single revert restores both the kit and the tree together.
- user docs — `HYGIENE.template.md` is rewritten; `AGENTS.md` and the manifest pointer map follow.

## 6. Acceptance criteria

- **AC1** — When the gate runs over the migrated tree, no path under `<MEMORY_ROOT>` contains a
  discipline directory segment and every leg is green.
- **AC2** — When a build folder is created whose name carries a date or a FAMILY prefix, check 4
  fails naming that folder.
- **AC3** — When a spec header carries `streams` with a value outside the enum, check 12 fails naming
  the illegal value and listing the legal set.
- **AC4** — When a spec whose filename date is on or after `STREAMS_CUTOFF` omits `streams`, check 12
  fails; when its filename date is before the cutoff, the same spec passes.
- **AC5** — When a recording file carries the optional FAMILY qualifier, check 5 accepts it; when it
  carries a FAMILY token that is not in `FAMILIES`, check 5 rejects it.
- **AC6** — When `hygiene-parity.test.sh` runs, the kit's built-in defaults and this repo's
  `.memory-tree.conf` still agree.
- **AC7** — When the migration diff is read, every pre-migration path under `<MEMORY_ROOT>` resolves
  to exactly one post-migration path, and the tracked file count is unchanged except for the
  deliberate merges. `git log --follow` is NOT the criterion: git does not record renames, so it
  returns the same answer for a rename and for a delete plus an add, and cannot fail.
- **AC8** — When any retargeted selector matches zero paths on this tree, its check fails naming the
  empty population, rather than printing nothing and passing.

## 7. Gates

`bash tools/run-gates.sh` in full. The legs that carry this unit's weight:
`tools/memory-tree/check-memory-hygiene.sh`, `check-memory-hygiene.test.sh` and
`hygiene-parity.test.sh`. The kickoff-manifest ratchet fires because `.memory-tree.conf` is watched.

## 8. Open questions

none — the two forks below are RESOLVED (owner-ratified 2026-08-08); kept for the record.

- **Fork A — what happens to the one slug shared by two disciplines.** Options: merge into a single
  build folder, or keep two folders under disambiguated slugs. RESOLVED (owner, 2026-08-08): merge,
  with the optional FAMILY qualifier on the recordings inside. A build spanning two disciplines is
  the case the flatten is FOR, and keeping two folders would re-encode the axis being removed.
- **Fork B — where `STREAMS_CUTOFF` is set.** Options: today, so the corpus exercises the required
  arm, or strictly ahead of the corpus. RESOLVED (owner, 2026-08-08): strictly ahead. Setting it to
  today would demand `streams` on specs written before the field existed. The cost is that the
  required arm is unexercised by real data, which S5 pays for with explicit fixtures.

## 9. Revision log

- rev-1 · 2026-08-08 · initial draft.
- rev-2 · 2026-08-08 · folded review 2: F1 adds S11 (a retargeted population asserts it is
  non-empty, because a mis-segmented selector passes silently) and AC8; F2 replaces the
  `git log --follow` criterion, which cannot fail; F3 adds S12 for the generator's unit list; F4
  extends S10 to the relative-link sweep; F5 states the cutoff's forward half; F6 pins the FAMILY
  qualifier to the closed alternation.

## 10. Reuse audit

Every mechanism this unit needs already exists in the kit and is retargeted rather than rebuilt. The
grandfather-by-filename-date device is `SPEC_FORMAT_CUTOFF` and `SPEC10_CUTOFF`, and `STREAMS_CUTOFF`
is a third instance of the same pattern read by the same awk. The batched single-awk idiom in checks
4, 8 and 12 is kept; only the path fields change. `FAMILY_of` and `FAM_ALT` already derive the family
alternation from `FAMILIES`, so the optional recording qualifier and the backlog shard names both
come from the existing accessor. `hygiene-parity.test.sh` already compares the kit defaults against
the repo conf and needs only the new key. The migration itself reuses `git mv` rather than a scripted
copy, so no new tool is written for a one-time move.
