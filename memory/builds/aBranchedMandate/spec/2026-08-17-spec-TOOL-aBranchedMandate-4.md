# TOOL-aBranchedMandate-4 — the unattended adopter decides repo membership without comparing path strings

**Status:** SPECCED · rev-3 · 2026-08-17 · node a · Tier-2 · base 96141aed · streams tooling · ratified 2026-08-17

## 1. Goal

`tools/unattended/adopt-unattended.sh` derives the kit's relative path by stripping `$ROOT` off
`$KIT_DIR` as a path string. **When the adopter is invoked by ABSOLUTE path** the two operands carry
different MSYS spellings of one directory, so the strip no-ops, the not-inside-the-repo guard
misfires ahead of every later guard, and the `unattended adopter e2e` leg is red on node `a` — which
blocks landing. Replace the strip with a derivation that never compares path strings across flavors,
without breaking the junction install shape this fleet uses.

The absolute-path qualifier is load-bearing and an earlier revision of this line omitted it. `cd
"$ROOT"` at `tools/unattended/adopt-unattended.sh:27` re-anchors the cwd to git's spelling before
`dirname "$0"` is resolved, so a RELATIVE `$0` — the invocation the file's own usage header
documents — inherits ROOT's flavor and the strip succeeds. Measured both ways in one fixture. Arms 2
and 3 of the e2e invoke absolutely, which is why they and only they fail.

## 2. Scope (IN)

- **S1** — `KIT_REL` and the kit's repo root come from a **logical upward walk** from the kit dir,
  building the relative path from basenames and stopping at the first `.git`. Nothing is asked to
  resolve a path, and no two spellings are ever compared. This is the seam
  `tools/codebase-map/adopt-codebase-map.sh` already uses. Two constraints the walk carries:
  the kit dir is resolved **before** the `cd` at line 27, since the walk starts from it and that `cd`
  is what re-anchors the cwd; and the boundary test is `-e "$_parent/.git"`, never `-d`, because a
  linked worktree's `.git` is a FILE and this fleet nests worktrees inside the repository.
- **S2** — the foreign-repo refusal is PRESERVED and re-expressed, in three parts.
  **(a) The predicate.** Repository IDENTITY, not path prefixes: both sides answer
  **`git rev-parse --path-format=absolute --git-common-dir`**. The path format is the load-bearing
  half. Measured: bare `--git-common-dir` prints `.git` from any toplevel, so two unrelated
  repositories compare EQUAL and the refusal never fires, while a linked worktree prints an absolute
  path and so compares UNEQUAL to its own primary tree — false-accepting every foreign repo and
  false-refusing the one case the owner picked this option to admit. With
  `--path-format=absolute` both fixtures print distinct absolute paths and the primary tree and its
  worktree print the same one. `--absolute-git-dir` is NOT a substitute: in a linked worktree it
  answers that worktree's private git dir, not the common one.
  **(b) The message.** After S1 the kit is inside the walk's root by construction, so "the kit is not
  inside $ROOT" can no longer BE the foreign-repo refusal. It names the kit dir and the OPERATOR's
  tree instead, as `adopt-codebase-map.sh` already phrases it.
  **(c) The arm.** `tools/unattended/adopt-unattended.test.sh`'s arm 2 asserts the old literal, so it
  is re-keyed in the SAME commit. That arm is green today only because the spelling defect fires the
  guard for every repo; after S1 it becomes the first real exercise of the membership predicate.
- **S3** — the junction contract is preserved, and **the write root is named**, which the first
  revision left ambiguous. `KIT_REL` is the path the CALLER traversed, because it is interpolated
  into the rendered Skill and must be copy-pasteable in the tree the operator is standing in.
  Membership is a different question and may resolve physically. **The tree the adopter WRITES into
  is the OPERATOR's toplevel** — the conf is read from it and every artifact lands in it. The walk's
  root feeds `KIT_REL` and the membership compare ONLY, and is never `cd`-ed into nor written to.
  Without this, copying the seam verbatim makes a run from a worktree write the Skill and the
  committed protocol copy into the PRIMARY tree at exit 0 while the operator's own tree gets nothing —
  a cross-tree write where today there is a refusal.
- **S4** — an arm that pins the spelling case, with its construction stated because the first
  revision named none. It creates a SECOND SPELLING on purpose (a directory symlink where one is
  real, a junction otherwise), **asserts the two spellings actually differ before asserting the
  refusal**, invokes the adopter by ABSOLUTE path, and skips LOUDLY when no second spelling can be
  made. Relying on `mktemp -d` landing under `/tmp` is not a construction: on a host where `/tmp` is
  an ordinary directory the arm passes with S1 reverted, which is the class AC5 exists to refuse.
- **S5** — the junction arm stops being skipped on this host, and its premise is corrected. It does
  NOT skip because `ln -s` fails: measured, `ln -s` exits 0 here and produces a real directory COPY
  (`-L` false, `-d` true, entries duplicated). The skip comes from the `[ -L ]` test afterwards. So
  the arm discriminates on `[ -L ]` AFTER creation and never on `ln -s`'s exit code, removes the copy
  residue before attempting a junction (`New-Item -ItemType Junction` fails on a non-empty path), and
  skips loudly only when neither a symlink nor a junction yields `-L` true. A junction created that
  way IS `-L` true under MSYS bash, so the existing discriminator accepts one unchanged.

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

All four lines, including the `cd` an earlier revision of this section dropped:

```
ROOT="$(git rev-parse --show-toplevel)"; ROOT="$(cd "$ROOT" && pwd)"
cd "$ROOT" || exit 2                       # <- line 27, and it decides who is affected
KIT_DIR="$(cd "$(dirname "$0")" && pwd)"
KIT_REL="${KIT_DIR#"$ROOT"/}"
```

That `cd` re-anchors the cwd to git's spelling BEFORE `dirname "$0"` resolves, so the trigger is the
INVOCATION FORM. Measured in one `mktemp -d` fixture, with the adopter's own lines:

```
relative $0   (cd $repo && bash tools/unattended/probe.sh)
  KIT_REL = tools/unattended                       -> strip SUCCEEDS
absolute $0   (bash "$repo/tools/unattended/probe.sh")
  KIT_REL = /tmp/tmp.X/spaced/tools/unattended     -> strip no-ops, guard FIRES
```

With a relative `$0` the kit dir inherits ROOT's flavor and everything works — which is the
invocation the file's own usage header documents. With an absolute `$0` the kit dir keeps the
caller's `/tmp` spelling, `/tmp` is an MSYS **mount point, not a symlink**, the two never converge,
`KIT_REL` equals `KIT_DIR`, the not-inside guard fires, and arm 3 reads its expected whitespace
message as missing. Arms 2 and 3 invoke absolutely; the other four do not, which is exactly the
observed one-FAIL-plus-one-SKIP result.

The source comment above that code says both sides go through the same `cd … && pwd` chain — they
do, and that is not sufficient, which is why the comment did not prevent this. An earlier revision of
THIS section repeated the same shape of unexamined sufficiency by quoting three lines of a four-line
chain.

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
| what relative path do I RENDER | the logical upward walk from the kit dir | it is interpolated into a Skill the operator runs from the tree they are standing in |
| is the kit in the ADOPTING repo | `--path-format=absolute --git-common-dir`, both sides | physical resolution is correct here — the same repository reached two ways is the same repository |
| which tree do I WRITE into | the OPERATOR's toplevel, always | the walk's root may be a different working tree of the same repository, and writing there is a cross-tree write |

The third row is the one the first revision omitted, and omitting it is not a documentation gap: the
seam S1 copies sets `ROOT` from its walk and then `cd`s into it and writes there, held safe only by
an inode compare that FORCES walk root == cwd root. S2 replaces that test with one that deliberately
admits a linked worktree, so the seam's safety property does not come along with its walk. Copied
verbatim, a run from a worktree would write `SKILL.md` and the committed protocol copy into the
primary tree, on the default branch, at exit 0, while the operator's tree got nothing — where today
it refuses.

The walk is `adopt-codebase-map.sh`'s, bounded by `.git`, building `KIT_REL` from basenames as it
climbs. It compares nothing, so no pair of spellings can disagree.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/unattended/adopt-unattended.sh` | S1, S2(a)(b), S3 |
| `tools/unattended/adopt-unattended.test.sh` | S2(c) — arm 2 re-keyed — plus S4 and S5 |

### Alternatives rejected

- **`git rev-parse --show-prefix`.** Measured above: breaks the junction contract.
- **Normalize both sides through `cygpath`.** Adds a Windows-only dependency to a kit that ships to
  POSIX adopters, and still compares strings.
- **Point `TMPDIR` off the mount point in the test harness.** Turns the leg green while the adopter
  stays broken for any real adopter installed under a mount point. It is the bypass shape.
- **Compare `realpath` of both sides.** Resolves physically, which is right for membership and wrong
  for `KIT_REL`; using it for both reintroduces the junction defect.

## 5. Production-readiness checklist

- security — this IS a trust-boundary predicate: it decides which tree the adopter may write to, and
  the audit found the first revision widening it twice. S2's PATH FORMAT is the load-bearing half:
  bare `--git-common-dir` makes the predicate always-true across unrelated repositories. S3's write
  root is the other: without it the unit converts a refusal into a cross-tree write. Neither is a
  wording risk; both were implementable exactly as written.
- perf / scale — N/A. A bounded upward walk over a few directory levels.
- a11y — N/A.
- i18n — N/A.
- error / empty / loading states — a walk that reaches the filesystem root without finding `.git`
  must refuse, not fall through with an empty root. `adopt-codebase-map.sh`'s walk has that branch
  and it is carried over.
- observability — the refusal messages keep naming both the kit dir and the root, which is what made
  this defect diagnosable from the leg's log alone.
- risks — the junction contract, which no gate covers today; S5 removes that gap on this host, and on
  a host with neither symlink nor junction the arm still skips and says so. The SAME host dependence
  applies to S4's spelling arm and the first revision recorded it for only one of the two: where no
  second spelling can be constructed the arm must skip loudly rather than pass, because a fixture that
  cannot reproduce the defect passes with the fix reverted.
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
- **AC3** — When the adopter runs from a repo that does not own the kit, it exits 2, its message
  names the kit dir and the OPERATOR's tree, and BOTH `.claude/skills/unattended/SKILL.md` and the
  protocol copy are absent from both trees. Arm 2 of `tools/unattended/adopt-unattended.test.sh` is
  re-keyed to that new literal in the same commit — it asserts the old "is not inside" wording, which
  S2(b) retires. Saying the existing arm "must stay green" was wrong: green today is produced by the
  defect, since the guard fires for every repo regardless of ownership.
- **AC4** — When the kit sits behind a junction inside the adopting repo, the rendered
  `.claude/skills/unattended/SKILL.md` names the path the caller traversed, not the junction's
  target. This is S5's arm and it is the contract no gate covers today.
- **AC5** — When S4's spelling arm in `tools/unattended/adopt-unattended.test.sh` runs against the
  adopter with S1 reverted, it FAILS; and when the two spellings cannot be constructed, it SKIPS with
  a named reason rather than passing. Both halves are the criterion — a fixture that passes either
  way is the `fixture-passes-by-finding-nothing` class this build already paid for once.
- **AC6** — When `bash tools/unattended/adopt-unattended.sh --check` runs in this repo, it still
  reports the rendered Skill in sync, proving the derivation change did not move `KIT_REL` for the
  ordinary install shape.
- **AC7** — When the adopter runs from a LINKED WORKTREE of the repository that owns the kit, it is
  admitted **and both artifacts land in the WORKTREE**, with the primary tree unchanged; when it runs
  from an unrelated repository, it still refuses. Three halves, not two. The admission proves the path
  format, since bare `--git-common-dir` refuses this case; the write-location assertion proves S3,
  since without it the artifacts land in the primary tree at exit 0; and the refusal proves the
  predicate did not degenerate to always-true, which bare `--git-common-dir` does.

## 7. Gates

- `bash tools/run-gates.sh`, and `GATE_FULL=1` at the push boundary. The leg's guard in
  `tools/gate-legs.json` is `tools/lib/` and `tools/unattended/`, and the defective file is
  `tools/unattended/adopt-unattended.sh` — so every diff that could introduce this DOES run the leg.
  An earlier revision of this line blamed the guard for the escape, which would send a reader to
  unguard the leg instead of to S4. The real escape routes are S4's (green wherever the fixture cannot
  produce two spellings) and §1's (green for the documented relative invocation).
- `bash tools/unattended/adopt-unattended.test.sh` — the leg this unit turns green.
- `bash tools/unattended/adopt-unattended.sh --check` — the wiring leg, for AC6.
- `bash tools/check-install-prefix.sh` — nothing shipped may spell a root-install kit path, and this
  unit edits path derivation.

## 8. Open questions

none — the fork below is RESOLVED.

- **F1 — which git question decides membership?** **(a) `rev-parse --git-common-dir` on both sides**
  treats a linked worktree of the same repository as the same repo, so adopting from a worktree
  works — which matters, because this fleet works in worktrees and the primary tree holds the kit.
  **(b) `rev-parse --show-toplevel`** demands the same working tree exactly, refusing a worktree
  install. **RESOLVED (owner, 2026-08-17): (a).** The contract the refusal exists for is "do not write
  into somebody else's repository", and a linked worktree is not somebody else's.

  **The RESOLUTION stands; the SPELLING it was put in was wrong, and is corrected here rather than
  re-put.** The option was offered as bare `--git-common-dir`, which was not measured before it was
  offered. It does not implement the owner's choice at all: it prints `.git` from any toplevel, so two
  unrelated repositories compare equal, and it prints an absolute path in a linked worktree, so the
  worktree compares unequal to its own primary tree — the predicate is false in BOTH directions, and
  the false-accept is a widened write surface rather than a nuisance. `--path-format=absolute
  --git-common-dir` implements exactly what was chosen: worktree admitted, foreign repo refused,
  measured on this node. Because the owner's decision was semantic ("a linked worktree counts as the
  same repository") and that semantics is unchanged, this is a correction, not a new fork.

## 9. Revision log

- rev-1 · 2026-08-17 · initial draft, from the lander's red leg and the junction measurement taken
  during the design pass.
- rev-2 · 2026-08-17 · F1 resolved by the owner: membership is `--git-common-dir` on both sides, so a
  linked worktree of the same repository is admitted. Folded into S2 with the reason, and AC7 added
  to observe BOTH halves — a criterion that only watched the refusal would pass under the option the
  owner did not pick.
- rev-3 · 2026-08-17 · folded the M4 audit recorded under this build's `reviews/`, which returned
  BLOCKED with three blockers. C1: the ratified F1 spelling does not implement the ratified decision —
  bare `--git-common-dir` false-accepts every foreign repo AND false-refuses the worktree case, so S2
  and F1 now name `--path-format=absolute --git-common-dir`, with `--absolute-git-dir` recorded as no
  substitute. C2: S1 and S2 created two roots and the spec never named the WRITE root, which would
  have turned today's refusal into a cross-tree write of the Skill and the committed protocol copy
  into the primary tree; S3 now names it and §4 gains a third row. C3: §4's chain omitted `cd "$ROOT"`
  at line 27, so §1's trigger was too broad — it is ABSOLUTE `$0`, and with a relative one the strip
  succeeds. Also folded: S4's construction, liveness assertion and loud skip (C4); the retirement of
  the not-inside message and arm 2's re-key (C5); §7's false escape story, the leg's guard does cover
  the defective file (C7); S5's premise, since `ln -s` succeeds here and produces a COPY so the skip
  comes from `[ -L ]` (C8); and the `-e` boundary test for a worktree's `.git` FILE (C9). AC3, AC5 and
  AC7 rewritten; §5's security and risks lines re-priced; §10 gains the seam's inode-compare half.

## 10. Reuse audit

Three candidate seams exist in this repo and the design pass measured all three rather than taking
the first. `tools/memory-recall/adopt-memory-recall.sh` uses `git rev-parse --show-prefix` and
documents this exact failure class — and is REJECTED here, because measurement showed git resolves a
junction physically and this kit alone carries a junction contract. `tools/drift-audit/adopt-drift-audit.sh`
computes a relative path through python's `os.path.relpath`, which is string arithmetic on two
possibly-different spellings and is the same defect in another language.
`tools/codebase-map/adopt-codebase-map.sh` performs a purely logical upward walk bounded by `.git`,
comparing nothing — that is the seam S1 adopts.

`adopt-codebase-map.sh` carries a SECOND half this spec must not copy and an earlier revision of this
section did not mention: an inode compare, `[ "$_CWD_ROOT" -ef "$ROOT" ]`, which measures SAME across
the mount-point spellings and would be an elegant membership test here. It is rejected on the owner's
F1 resolution, not on merit: `-ef` forces the walk root and the operator's tree to be one directory,
which refuses the linked-worktree install F1(a) exists to admit. It is recorded because it is the
right answer to a question this unit is not asking, and the next reader will reach for it.

The reuse conclusion worth recording: the four adopters in this tree derive one thing four ways, and
only one of them is correct for a kit with a junction contract. That spread is named as a non-goal
here rather than fixed, because three of the four have no junction contract to break.
