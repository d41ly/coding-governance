# TOOL-aBranchedMandate-4 — the unattended adopter decides repo membership without comparing path strings

**Status:** SPECCED · rev-1 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling

## 1. Goal

`tools/unattended/adopt-unattended.sh` derives the kit's relative path by stripping `$ROOT` off
`$KIT_DIR` as a path string. The two operands are produced by different chains and never converge
under an MSYS mount point, so the strip no-ops, the not-inside-the-repo guard misfires ahead of every
later guard, and the `unattended adopter e2e` leg is red on node `a` — which blocks landing. Replace
the strip with a derivation that never compares path strings across flavors, without breaking the
junction install shape this fleet uses.

## 2. Scope (IN)

- **S1** — `KIT_REL` and the kit's repo root come from a **logical upward walk** from the kit dir,
  building the relative path from basenames and stopping at the first `.git`. Nothing is asked to
  resolve a path, and no two spellings are ever compared. This is the seam
  `tools/codebase-map/adopt-codebase-map.sh` already uses.
- **S2** — the foreign-repo refusal is PRESERVED and re-expressed. It is a question about repository
  IDENTITY, not about path prefixes: the root the walk found and the adopting repo must be the same
  repository, compared by asking git on both sides so both answers come from one speller. F1 picks
  which git question.
- **S3** — the junction contract is preserved and stated in source. `KIT_REL` is the path the CALLER
  traversed, because it is interpolated into the rendered Skill and must be copy-pasteable in the
  tree the operator is standing in. Membership is a different question and may resolve physically.
- **S4** — an arm that pins the mount-point case: a fixture whose repo lives under a path with two
  MSYS spellings, asserting the whitespace refusal is reached. Without it this defect returns
  invisibly, because it is green on any node whose fixtures land off a mount point.
- **S5** — the junction arm stops being skipped on this host. `tools/unattended/adopt-unattended.test.sh`
  skips it because `ln -s` needs privilege here; a Windows **junction** does not, and one was created
  on this node during the design pass. The arm creates a junction where a symlink is unavailable and
  skips only when NEITHER is creatable.

## 3. Non-goals (OUT)

- The other three adopters. `adopt-memory-recall.sh`, `adopt-drift-audit.sh` and
  `adopt-codebase-map.sh` each derive this differently, and two of them would fail the junction
  contract if they had one. Auditing that spread is a separate unit and this one does not start it.
- The whitespace guard itself, which is correct and is merely unreachable today.
- The `ln -s` skip as a general condition. S5 removes it for THIS arm by using a junction; every
  other suite keeps whatever it does now.
- Bumping `KIT_UNATTENDED_VERSION`. Node `c`'s in-flight build owns that literal.
- Making the leg green by pointing `TMPDIR` somewhere the spellings converge. That hides a real
  defect and is a bypass wearing a different name; it was measured during the design pass precisely
  to prove the defect is real, and is recorded here so nobody mistakes it for a remedy.

## 4. Design

### What breaks, measured with the adopter's own chain

```
ROOT="$(git rev-parse --show-toplevel)"; ROOT="$(cd "$ROOT" && pwd)"
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
KIT_REL="${KIT_DIR#"$ROOT"/}"
```

Run in a fixture under `mktemp -d`:

```
ROOT     /c/Users/daily-agent/AppData/Local/Temp/tmp.KjnytylraD/spaced
KIT_DIR  /tmp/tmp.KjnytylraD/spaced/my tools/unattended
KIT_REL  /tmp/tmp.KjnytylraD/spaced/my tools/unattended     <- unchanged
```

`ROOT` is git's Windows spelling put through `cd … && pwd`; `KIT_DIR` is the caller's `/tmp`
spelling. `/tmp` is an MSYS **mount point, not a symlink**, so the two never converge and the strip
no-ops. `KIT_REL` then equals `KIT_DIR`, the not-inside guard fires, and arm 3 reads its expected
whitespace message as missing. The source comment above that code says both sides go through the
same `cd … && pwd` chain — they do, and that is not sufficient, which is why the comment did not
prevent this.

This is the trap the kickoff manifest front-loads verbatim: never compare path strings across
flavors, decide repo membership via git identity. It is reproduced inside the kit that documents it.

### Why the obvious fix is wrong, also measured

`adopt-memory-recall.sh` solves the same class with `REL="$(cd "$HERE" && git rev-parse --show-prefix)"`
and its comment describes the identical failure. It is NOT portable here. Measured on this node
against a real Windows junction:

| Derivation | Result for a junction at `repo/link` -> `repo/real` |
|---|---|
| `pwd` after `cd link` | `…/repo/link` — LOGICAL, what the contract requires |
| `git rev-parse --show-prefix` after `cd link` | `real/` — PHYSICAL |
| `git -C link rev-parse --show-prefix` | `real/` — PHYSICAL |

Git resolves the junction physically no matter how the shell arrived, so adopting the memory-recall
seam would render a Skill pointing at the junction's TARGET. `adopt-unattended.sh`'s own comment
states why that is fatal: a kit dir that is a junction inside the adopting repo must anchor to the
adopting repo, because that is the install shape this fleet uses, and resolving physically adopts the
wrong tree silently. **The junction arm is skipped today, so no gate would have caught it.**

### The shape that satisfies both

Two questions, two mechanisms, and conflating them is what produced the defect:

| Question | Answer | Why |
|---|---|---|
| what relative path do I RENDER | the logical upward walk | it is interpolated into a Skill the operator runs from the tree they are standing in |
| is the kit in the ADOPTING repo | git identity, on both sides | physical resolution is correct here — the same repo reached two ways is the same repo |

The walk is `adopt-codebase-map.sh`'s, bounded by `.git`, building `KIT_REL` from basenames as it
climbs. It compares nothing, so no pair of spellings can disagree.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/adopt-unattended.sh` | S1, S2, S3 |
| `tools/unattended/adopt-unattended.test.sh` | S4, S5 |

### Alternatives rejected

- **`git rev-parse --show-prefix`.** Measured above: breaks the junction contract.
- **Normalize both sides through `cygpath`.** Adds a Windows-only dependency to a kit that ships to
  POSIX adopters, and still compares strings.
- **Point `TMPDIR` off the mount point in the test harness.** Turns the leg green while the adopter
  stays broken for any real adopter installed under a mount point. It is the bypass shape.
- **Compare `realpath` of both sides.** Resolves physically, which is right for membership and wrong
  for `KIT_REL`; using it for both reintroduces the junction defect.

## 5. Production-readiness checklist

- security — this IS a trust-boundary predicate: it decides which tree the adopter may write to. The
  fix must not widen it. S2 keeps the foreign-repo refusal and F1 names the exact git question.
- perf / scale — N/A. A bounded upward walk over a few directory levels.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a walk that reaches the filesystem root without finding `.git`
  must refuse, not fall through with an empty root. `adopt-codebase-map.sh`'s walk has that branch
  and it is carried over.
- observability — the refusal messages keep naming both the kit dir and the root, which is what made
  this defect diagnosable from the leg's log alone.
- risks — the named one is the junction contract, which no gate covers today. S5 removes that gap on
  this host; on a host with neither symlink nor junction the arm still skips, and says so.
- testing + left-shift gates — S4 and S5. The mount-point arm is the one that would have caught this
  defect, and it did not exist.
- migration / rollback — none. No committed artifact changes shape; only the derivation does.
- user docs — the source comment is rewritten, since the existing one asserts a sufficiency that the
  measurement refutes.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.test.sh` runs with the default `TMPDIR` on
  node `a`, it PASSES. It fails today at `FAIL missing: the kit path contains whitespace`.
- **AC2** — When the full bar runs via `bash tools/push-main.sh`, the leg `unattended adopter e2e` is
  green and the push is no longer blocked by it.
- **AC3** — When the adopter runs from a repo that does not own the kit, it still refuses with its
  foreign-repo message and writes nothing. The existing arm in
  `tools/unattended/adopt-unattended.test.sh` covers this and must stay green.
- **AC4** — When the kit sits behind a junction inside the adopting repo, the rendered
  `.claude/skills/unattended/SKILL.md` names the path the caller traversed, not the junction's
  target. This is S5's arm and it is the contract no gate covers today.
- **AC5** — When S4's mount-point arm runs against the adopter with S1 reverted, it FAILS. A fixture
  that passes either way is the `fixture-passes-by-finding-nothing` class this build already paid
  for once.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs in this repo, it still
  reports the rendered Skill in sync, proving the derivation change did not move `KIT_REL` for the
  ordinary install shape.

## 7. Gates

- `bash tools/run-gates.sh`, and `GATE_FULL=1` at the push boundary — the leg is guarded, so only the
  unguarded run exercises it, which is how this defect reached the default branch.
- `bash tools/unattended/adopt-unattended.test.sh` — the leg this unit turns green.
- `bash tools/unattended/adopt-unattended.sh --check` — the wiring leg, for AC6.
- `bash tools/check-install-prefix.sh` — nothing shipped may spell a root-install kit path, and this
  unit edits path derivation.

## 8. Open questions

- **F1 — which git question decides membership?** **(a) `rev-parse --git-common-dir` on both sides**
  treats a linked worktree of the same repository as the same repo, so adopting from a worktree
  works — which matters, because this fleet works in worktrees and the primary tree holds the kit.
  **(b) `rev-parse --show-toplevel`** demands the same working tree exactly, refusing a worktree
  install. **Recommendation: (a).** The contract the refusal exists for is "do not write into
  somebody else's repository", and a linked worktree is not somebody else's. It is an owner turn
  because it changes which installs are refused.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, from the lander's red leg and the junction measurement taken
  during the design pass.

## 10. Reuse audit

Three candidate seams exist in this repo and the design pass measured all three rather than taking
the first. `tools/memory-recall/adopt-memory-recall.sh` uses `git rev-parse --show-prefix` and
documents this exact failure class — and is REJECTED here, because measurement showed git resolves a
junction physically and this kit alone carries a junction contract. `tools/drift-audit/adopt-drift-audit.sh`
computes a relative path through python's `os.path.relpath`, which is string arithmetic on two
possibly-different spellings and is the same defect in another language.
`tools/codebase-map/adopt-codebase-map.sh` performs a purely logical upward walk bounded by `.git`,
comparing nothing — that is the seam S1 adopts.

The reuse conclusion worth recording: the four adopters in this tree derive one thing four ways, and
only one of them is correct for a kit with a junction contract. That spread is named as a non-goal
here rather than fixed, because three of the four have no junction contract to break.
