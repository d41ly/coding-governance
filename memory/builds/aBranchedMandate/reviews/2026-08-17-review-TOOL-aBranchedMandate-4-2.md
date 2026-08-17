**Serves:** spec-audit TOOL-aBranchedMandate-4  <!-- inferred: its opening names the spec and rev it audits -->

## Verdict: BLOCKED

Base 96141aed · spec TOOL-aBranchedMandate-4 rev-2 · M4 synthesis pass · node a · 2026-08-17.

Five lenses produced 28 raw findings: 19 confirmed, 9 refuted, none unverified. The 19 confirmed
deduplicate to **nine defects**, three of them blockers. Two blockers sit in the ratified fork F1 and
the S2 it was folded into, so this is not a wording pass — the mechanism the owner ratified does not
do what the resolution says it does, and the fix has to be re-put before the unit is built. The
refuted findings are kept below with their reasons; several of them are the weaker cousins of a
confirmed one and the distinction is stated where it matters.

Everything below was re-measured on this node against git 2.54.0.windows.1 rather than taken from the
lens output.

## CONFIRMED

### C1 — §2 S2 and §8 F1: `--git-common-dir` is CWD-relative, so the membership compare is wrong in
both directions — BLOCKER

Raw findings 1, 7, 16, 21.

S2 (spec lines 20-26) makes membership `git rev-parse --git-common-dir` asked "on both sides ... so
both answers come from one speller", and §8 F1 records that as the owner's pick. The command's
default output format is relative-or-absolute depending on which tree is asked. Measured:

```
git -C <tmp>/r      rev-parse --git-common-dir   ->  .git
git -C <tmp>/other  rev-parse --git-common-dir   ->  .git       (two unrelated repos, EQUAL)
git -C C:/projects/coding-governance rev-parse --git-common-dir ->  .git
git rev-parse --git-common-dir   (in this worktree)             ->  C:/projects/coding-governance/.git
```

So the predicate FALSE-ACCEPTS every foreign repository — the exact fixture pair of arm 2
(`tools/unattended/adopt-unattended.test.sh` lines 96-105, `$TMP/host` and `$TMP/other`, each
standing at its own toplevel) — and FALSE-REFUSES the primary-tree/worktree pair that F1(a) was
chosen over F1(b) precisely to admit. AC3 and both halves of AC7 are unsatisfiable as written, and
§5's "the fix must not widen it" is false: implemented literally, the widening is to always-true.

One speller, two formats. §2's justification clause is the same shape of unexamined sufficiency that
§4 already records the source comment at `tools/unattended/adopt-unattended.sh` lines 34-37 making
about the strip this unit exists to delete.

**Edit.** §2 S2 and §8 F1(a) name `git rev-parse --path-format=absolute --git-common-dir` on both
sides, not `--git-common-dir`. Measured: that spelling prints `C:/projects/coding-governance/.git`
from BOTH the primary tree and this worktree, and distinct absolute paths for the two unrelated
fixtures — one comparable speller, worktree admitted, foreign repo refused. Record in §8 that
`--absolute-git-dir` is NOT a substitute: in a linked worktree it answers
`C:/projects/coding-governance/.git/worktrees/unattended-builds-worktrees-4868c1`, not the common
dir. §5's security line changes from "F1 names the exact git question" to naming the path format,
since the format is the load-bearing half.

### C2 — §2 S1/S2: two roots exist and the spec never says which one the adopter WRITES into —
BLOCKER

Raw findings 2, 9, 15, 22.

S1 makes the walk yield "KIT_REL and the kit's repo root"; S2 then compares "the root the walk found
and the adopting repo", and F1(a)'s stated motivation (spec lines 183-185) is exactly the case where
those are two different directories. The spec never names the write target. In the current script
there is one `ROOT`, taken from the CALLER's toplevel at `adopt-unattended.sh` line 25 with no `-C`,
and it is the write target for every sink: `cd "$ROOT"` (line 27), `CONF` (65), `SKILL_DIR` (75),
`PROTO_OUT` (79), `mkdir -p "$ROOT/$MEMORY_ROOT/guides"` (154) and the next-steps text (173).

The seam S1 tells the builder to copy does the opposite of leaving that alone:
`tools/codebase-map/adopt-codebase-map.sh` sets `ROOT` from the walk (line 33), `cd`s into it (53)
and writes there — and the only thing keeping that safe is the inode compare
`[ "$_CWD_ROOT" -ef "$ROOT" ]` at line 45, which FORCES walk root == cwd root. S2 replaces that test
with a repository-identity test that by design admits a linked worktree, i.e. a different directory.
Copy the seam as instructed and the two readings diverge:

- walk root wins — a run from `C:/projects/coding-governance/.claude/worktrees/<this one>` against
  the kit in the primary tree passes membership and then writes
  `.claude/skills/unattended/SKILL.md` and the committed `memory/guides/UNATTENDED-PROTOCOL.md` into
  the PRIMARY tree, on the default branch, at exit 0, while the operator's own tree gets nothing.
  Measured: the S1 walk from `C:/projects/coding-governance/tools/unattended` yields
  ROOT=`/c/projects/coding-governance`, KIT_REL=`tools/unattended`.
- caller root wins — `KIT_REL` is rendered relative to a tree it was not traversed from, defeating
  S3's own justification.

Today that shape REFUSES: the strip no-ops and the not-inside guard fires. So the resolved S2 turns a
refusal into a cross-tree write. That is M3 veto 3 (widens a write surface beyond what the tier
priced) and §5 line 128 denies it in terms. AC7 cannot see it — it asserts only that the run is
admitted.

**Edit.** §2 gains one explicit sentence, and it should be S3's, since S3 already owns the
caller-vs-physical split: the adopter's write root is the OPERATOR's toplevel and `.unattended.conf`
is read from it; the walk root feeds `KIT_REL` and the membership compare only, and is never `cd`-ed
into or written to. §4's "shape that satisfies both" table gains a third row for that question. AC7
stops asserting bare admission and asserts WHICH tree received the two artifacts and that the other
tree received nothing — the same both-trees discipline the rest of the suite already uses.

### C3 — §1 and §4: the reproduction omits `cd "$ROOT"`, so the trigger condition is misstated and
S1's own ordering constraint is missing — BLOCKER

Raw findings 8, 17.

§4's fenced chain (spec lines 55-59) quotes three lines and drops the fourth that sits between them:
`cd "$ROOT" || exit 2` at `adopt-unattended.sh` line 27. That `cd` is what selects who is affected.
Measured with the adopter's own lines in a `mktemp -d` fixture:

```
relative $0   (cd $repo && bash tools/unattended/probe.sh)
  ROOT=/c/Users/.../Temp/tmp.X/spaced   KIT_DIR=/c/Users/.../spaced/tools/unattended
  KIT_REL=tools/unattended              -> strip SUCCEEDS, adopter proceeds
absolute $0   (bash "$repo/tools/unattended/probe.sh")
  KIT_DIR=/tmp/tmp.X/spaced/tools/unattended -> strip no-ops, not-inside guard FIRES
```

The `cd` re-anchors the cwd to git's spelling before `dirname "$0"` is resolved, so a relative `$0`
inherits ROOT's flavor. §1's "never converge under an MSYS mount point" is therefore false, and §4
prints the absolute-`$0` result without naming absoluteness as the trigger. Corroborated by running
the suite: one FAIL plus the arm-4 skip — five of six arms pass, and the two absolute-invocation arms
are arms 2 and 3.

Three consequences the spec does not carry. (i) The documented in-repo invocation at
`adopt-unattended.sh` line 4 is relative and is green either way. (ii) S4's new arm, written the
ordinary relative way that arms 1, 1b, 5 and 6 use, reproduces nothing and is green with S1 reverted
— AC5's own named class. (iii) Under S1, `ROOT` comes from a walk starting at the kit dir, so
`KIT_DIR` must be resolved BEFORE line 27's `cd`. Both seams spell that ordering out explicitly
(`tools/memory-recall/adopt-memory-recall.sh` lines 22-24, `tools/codebase-map/adopt-codebase-map.sh`
line 15) and this spec never mentions the `cd` at all.

**Edit.** §4's fenced chain gains line 27 and one sentence naming absolute `$0` as the trigger; §1's
"never converge" narrows to "do not converge when the adopter is invoked by absolute path, which is
what arms 2 and 3 do". S1 gains a clause: the kit dir is resolved before any `cd`, and the walk
starts from it. S4 states that the new arm invokes the adopter by ABSOLUTE path.

### C4 — §2 S4 and §6 AC5: the mount-point arm has no construction, no liveness assertion and no
skip rule — HIGH

Raw findings 5, 12, 18, 26.

S4 asks for "a fixture whose repo lives under a path with two MSYS spellings" and names no mechanism
for building one. Measured: `mktemp -d` prints `/tmp/tmp.X` while `git rev-parse --show-toplevel` in
it prints `C:/Users/daily-agent/AppData/Local/Temp/tmp.X`, so the harness's own `TMP=$(mktemp -d)`
(`adopt-unattended.test.sh` line 17) already lands every fixture under the `/tmp` mount point. On
node `a`, arm 3 (`$TMP/spaced`, lines 110-115) IS the mount-point case — S4 as written adds a
duplicate here. On a host where `/tmp` is an ordinary directory the divergence cannot be inherited at
all: git and `pwd` agree, the adopter refuses on whitespace either way, and the arm passes with S1
reverted. That is AC5's own `fixture-passes-by-finding-nothing` class inside the arm written to
prevent it, and this leg ships to adopters.

The asymmetry is not something a builder can read past: S5 gets an explicit fallback clause and a §5
risks line; S4 gets neither. AC5 also carries no runnable witness — its single backticked token is
`fixture-passes-by-finding-nothing`, a defect-class name, not the command, file, flag or test
`memory/TEMPLATE-SPEC.md` lines 143-147 asks each acceptance bullet to name.

**Edit.** S4 states the construction (a second spelling made on purpose — a directory symlink on
POSIX, a junction on Windows, both measured creatable on this node — plus an absolute-path
invocation), states that the arm ASSERTS the two spellings actually differ before asserting the
refusal, and states a LOUD skip when they cannot be made to differ, in the same words S5 uses. AC5
gains a backticked witness naming the arm and the revert it is observed against. §5's risks line
names the mount-point arm's host dependence alongside the junction one.

### C5 — §2 S2, §4 files table and §6 AC3: after S1 the foreign-repo message cannot survive, so arm
2's literal must be re-keyed in the same commit — HIGH

Raw finding 11.

After S1, `ROOT` is the root the walk FOUND from the kit dir, so the kit is inside `ROOT` by
construction and the sentence at `adopt-unattended.sh` line 46 — "the kit at $KIT_DIR is not inside
$ROOT" — can no longer be the foreign-repo refusal. It has to name the operator's tree instead, the
way the seam does at `adopt-codebase-map.sh` lines 46-52 ("but you are standing in"). That reds
`adopt-unattended.test.sh` line 102, `hit "$out" "is not inside"`. AC3 meanwhile says the existing
arm "must stay green" and §4's files table allots the test file only S4 and S5, so no scope item
authorises the edit.

Second half, also measured: arm 2 invokes by absolute path from the mount-point spelling, and that
shape fires the not-inside guard for the SPELLING reason alone. Arm 2's green today is produced by
the defect; it currently cannot distinguish a foreign repo from any repo at all. After S1 it becomes
the first real exercise of the membership predicate, so re-keying its assertion is a deliberate act,
not incidental churn.

**Edit.** S2 states the new refusal names the kit dir and the OPERATOR's tree, and that arm 2's
assertion is re-keyed to it in the same commit. §4's files table row for
`tools/unattended/adopt-unattended.test.sh` carries S2 alongside S4 and S5. AC3 names the substring
the re-keyed arm asserts and keeps the exit code 2 and the two `absent` assertions explicit.

### C6 — build README, "Units — the authored roster" and "Build-level rules": the ordering prose
contradicts the roster it now sits under — HIGH

Raw finding 10.

The roster table (README lines 74-79) lists four units with unit 4 last and line 81 declares the
order TOTAL, while line 86 still reads "Unit 3 ... is sequenced last" and line 107 still reads
"`tools/` — which all three units edit". The consequence is mechanical, not cosmetic:
`tools/gate-legs.json` guards the `unattended adopter e2e` leg on `tools/lib/` and
`tools/unattended/`; unit 2 touches `tools/unattended/unattended.sh` and its test, unit 3 touches
`unattended.sh`, `check-unattended.sh`, both templates and both test files. Both units' diff-scoped
gate runs therefore execute the red leg that unit 4 exists to fix, and M6's pass loop does not
continue past a red gate. Unit 4 has to precede units 2 and 3.

**Edit.** README's roster section: reorder to put unit 4 first (or alongside unit 1), rewrite the
"sequenced last" sentence for unit 3, and change "all three units edit" to four. State the reason in
one line — the leg's guard covers `tools/unattended/`, so every later unit's diff-scoped run
inherits the red until unit 4 lands.

### C7 — §7: the escape story for how the defect reached the default branch is false — MED

Raw finding 13.

§7 line 171 says "the leg is guarded, so only the unguarded run exercises it, which is how this
defect reached the default branch". The leg's guard in `tools/gate-legs.json` is
`["tools/lib/", "tools/unattended/"]` and the defective file is
`tools/unattended/adopt-unattended.sh` — every diff that could have introduced it trips the guard and
runs the leg. The spec's own S4 states the real escape route ("green on any node whose fixtures land
off a mount point"), and C3 above adds a second (green for the documented relative invocation). As
written the reader is pointed at unguarding the leg instead of at S4's remedy, and the builder is
told their own diff-scoped runs will not exercise the leg they are fixing.

**Edit.** §7 drops the causal clause and states the guard as it is — the leg runs whenever
`tools/unattended/` moves — and points at S4 for why it stayed green anyway.

### C8 — §2 S5: the stated reason the junction arm skips is not the reason it skips — MED

Raw finding 25.

S5 says the arm "skips it because `ln -s` needs privilege here". Measured on this host:
`ln -s "$E/unattended" "$D/tools/unattended"` exits 0 and produces a real directory COPY — `-L` is
false, `-d` is true, and the target's entries are duplicated. The skip at
`adopt-unattended.test.sh` line 125 is caused by the second conjunct `[ -L "$D/tools/unattended" ]`,
not by `ln -s` failing. Two consequences follow that S5 does not state: an
`if ln -s …; then … elif <junction> …` structure can never reach the junction branch, because the
`if` always succeeds; and the successful-but-fake `ln -s` leaves a non-empty directory at the path
the junction must be created at, where `New-Item -ItemType Junction` fails with "not empty". One fact
in S5's favour is also unrecorded: a junction made with `New-Item -ItemType Junction` IS `-L` true
under MSYS bash, so the existing discriminator accepts one unchanged.

Left as written, S5 either delivers nothing on the one host it exists to enable, or invites dropping
the `[ -L ]` guard — which scores the `ln -s` copy as a passing junction arm, the class this build's
README already records paying for once.

**Edit.** S5 replaces its premise: the arm discriminates on `[ -L ]` AFTER creation and never on
`ln -s`'s exit code, removes the residue before attempting the junction, and skips loudly only when
neither a symlink nor a junction yields `-L` true.

### C9 — §2 S1: pin the `.git` test to `-e`, because this fleet nests worktrees and `.git` is a file
there — LOW

Raw finding 28 (raw findings 14 and 19 made the same claim and were refuted as duplicates; this one
survives on the AC-coverage argument below).

S1 says the walk stops "at the first `.git`" and does not say `.git` may be a FILE. Measured: this
worktree's `.git` is an 88-byte regular file; `C:/projects/coding-governance/.git` is a directory.
This fleet nests worktrees at `<primary>/.claude/worktrees/<name>`, so a walk written `[ -d ]` climbs
past the worktree root and lands on the primary tree, yielding KIT_REL
`.claude/worktrees/<name>/tools/unattended`. The seam uses `[ -e "$_parent/.git" ]`
(`adopt-codebase-map.sh` line 33) and gives no reason for it, so a builder who reads the seam for the
rationale finds none. What keeps this on the list rather than in the refuted pile: AC7 provably
cannot catch it — measured, `--git-common-dir` resolves to the same value from the worktree and the
primary, so a mis-rooted `-d` walk still passes the identity compare. Only AC6 catches it, and only
when the builder happens to be standing in a worktree.

**Edit.** S1 spells `-e` (or "a `.git` entry of any type") and names the nested-worktree reason in
the same clause. One character, plus the reason so the next reader does not undo it.

## REFUTED

- **3** — "no criterion observes what S2 newly admits": §6 does not end at AC6. AC7 (spec lines
  164-167) is exactly that criterion, added in rev-2 for the stated reason.
- **4** — "AC3 and S2 cannot both hold": as a pure wording conflict it is refuted — a spec cannot
  enumerate every literal an intentional message change touches, and AC1 forces the discovery on the
  first run. The structural half survives as C5, where the message provably cannot be kept.
- **6** — "two unspecified walk boundary paths": both claimed cases fail SAFE. A kit dir that is
  itself a repo root, and a nested `.git` between kit and root, each end in a refusal, not in a
  write to a tree nobody named. The dead `[ -n "$KIT_REL" ]` guard at `adopt-codebase-map.sh` line 97
  is real but is that kit's own precondition, not part of the walk being ported.
- **14** — "S1 must spell `-e`": duplicate of 28 and refuted as put, because the spec pins the walk
  to a named seam twice and that seam already uses `-e`. Kept at low severity under C9 on the
  narrower AC-coverage argument only.
- **19** — same claim as 14 and 28 with the AC6 argument inverted: AC6 does red on a `-d`
  implementation for this builder, since they are standing in a worktree. Refuted as a blocker-shaped
  claim; folded into C9.
- **20** — "the builder cannot satisfy S2 and AC3 at once": refuted on the reading that "re-expressed"
  targets the question rather than the string. Superseded by C5, which shows the string cannot
  survive S1 regardless of the reading.
- **23** — "§4's table row asks about the kit, S2 asks about the walk root": the noun in the
  three-column summary is loose, but S2 at spec lines 20-26 names both operands explicitly and is the
  normative text. No builder overrides it with a summary row.
- **24** — "F1 is an invented fork because the seam's `-ef` already answers membership": measured
  `[ /c/projects/coding-governance -ef <this worktree> ]` is FALSE, so `-ef` delivers F1(b) semantics
  — the option the owner declined. The fork is exactly the choice `-ef` cannot make.
- **27** — third restatement of the AC3/S2 wording tension; refuted for the same reason as 20 and
  superseded by C5.

## UNVERIFIED

none — every finding reached a verdict, and every measurement cited above was reproduced on node `a`
during this pass rather than carried over from the lens output.
