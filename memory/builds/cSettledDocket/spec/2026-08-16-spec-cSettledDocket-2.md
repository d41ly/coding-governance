# TOOL-cSettledDocket-2 — `DIRECTIVES_EXTRA` is waivable and unshowable at once

**Status:** CLOSED · rev-3 · 2026-08-16 · node c · Tier-2 · base 1da67d9c · streams tooling

## 1. Goal

A project may declare `DIRECTIVES_EXTRA` in `.unattended.conf`. `directives()` composes it with the
core set, and `--waive` accepts any handle in that composition. Check 16 arm A joins only
`DIRECTIVES_CORE` against the Skill's directive table.

So an extra handle is **waivable by a verb and invisible to the agent**: the run can relax a rule the
table never showed it, and the project cannot fix that by adding a row, because the Skill is rendered
from a kit-owned template. Both halves are measurable — `directives()` at the driver composes both
sets, and check 16's `core` is `DIRECTIVES_CORE` alone.

This unit does not pick the answer. Both branches change a published contract, so §8 costs them and
names the owner as resolver.

## 2. Scope (IN)

- **S1** — whichever branch the owner takes is implemented whole, including the arms that prove the
  new refusal or the new join fires.
- **S2** — `memory/guides/UNATTENDED-PROTOCOL.md` §10 states the resolved rule in one paragraph, and
  the kit template stays byte-identical to it.
- **S3** — an arm proving the CURRENT hole is closed: a project declaring an extra handle can no
  longer waive something the agent was never shown, whichever way that is achieved.
- **S4** — `memory/map/features/unattended.md` records the resolved contract, since the dossier
  currently describes the directive layer without mentioning the asymmetry.

## 3. Non-goals (OUT)

- **Deleting `DIRECTIVES_EXTRA`.** §10 gives projects an extension point on purpose, and the
  argument that produced it — a conf key holding the WHOLE set lets a project declare zero
  directives — is unaffected by this defect.
- **A per-project Skill template.** Forking the template per adopter reintroduces the drift the
  pointer design removes, and check 16's join exists precisely because two hand-authored lists drift.
- **Touching `CORE_FLOOR` or `DIRECTIVES_FLOOR`.** Both pin counts of the CORE set and neither is
  implicated.
- **Extending the same question to `PHASES_EXTRA` and `DOD_EXTRA`.** They have the identical shape
  and may well have the identical hole, but measuring that is its own row, not scope creep into the
  unit the owner asked for.

## 4. Design

### What is actually broken

Three facts, each read at source:

1. `directives()` prints `"$DIRECTIVES_CORE $DIRECTIVES_EXTRA"`.
2. `check_waivers` accepts a handle when `" $(directives) "` contains `" $h:"` — so EXTRA is
   accepted.
3. Check 16 arm A builds `core` from `DIRECTIVES_CORE` and joins THAT to the table, both directions.

The join's two-directional refusal is what makes the hole visible rather than harmless: if arm A
covered the effective set, an extra handle would red as "declared in the registry and absent from the
Skill's table" — a refusal the project could not clear, because it cannot edit the template. So the
current behaviour is not an oversight that a one-line change fixes; it is the only configuration in
which `DIRECTIVES_EXTRA` is usable at all.

### Branch A — the join covers the effective set

Arm A joins `DIRECTIVES_CORE + DIRECTIVES_EXTRA` to the table. Consequence: declaring any extra
handle reds the bar immediately and permanently. `DIRECTIVES_EXTRA` becomes a key that exists, is
documented, and cannot be used — honest about the design as it stands.

It is NOT four characters, and rev-1 priced it as if it were. `core` is built ONCE above both guards
and read TWICE: by arm A's two `comm` joins and by arm B's `for pair in $core` section-resolution
loop. Widening the variable therefore also requires every project-declared extra to cite an `M<n>`
section present in the KIT's `BUILD-METHOD.md` — a second, differently-worded refusal that fires
even for a project whose extra directive points into its own method document. Branch A must either
introduce a separate `effective` for arm A alone, or accept that arm B's rule extends to extras and
say so. The audit rule this violated is worth keeping: cost a fork by its variable's READ SITES, not
by the line the change lands on.

Cost: a project that wants an extra directive has no route at all, and §10's promise that "the
project may only EXTEND" becomes false. The key should then be deleted rather than left as a trap,
which contradicts the non-goal above and widens this unit.

### Branch B — projects get a row source

The rendered Skill gains a project-owned region — a marker pair the adopter fills, the way the build
README carries `<!-- roster:units -->`. Arm A joins the effective set against the union of the
kit table and that region.

Cost: a new marker pair in a rendered artifact, which means `adopt-unattended.sh` must preserve the
adopter's region across a re-render — the same class as the memory-tree kit's four marker-region
implementations, one of which is recorded as having deleted authored data. That is the real price,
and it is not small.

### Branch C — EXTRA is accepted by `--waive` only when the table shows it

Leave arm A joining CORE. Change `check_waivers` to accept a handle only if it appears in the Skill's
TABLE, whatever set declared it. The table becomes the single source for what is waivable, which is
what §10 already says in prose: "the list an agent reads is the table in the rendered Skill".

Cost: the driver would read a markdown table at run time, which it does nowhere else, and the leg
would then be second-opinioning a parse the driver performs — a coupling the kit has avoided
deliberately.

### Recommendation

**B**, with the marker-region risk taken seriously and its arm written first — because it is the only
branch under which §10's stated contract stays true. A is defensible if the owner would rather delete
the extension point than build a safe one; that is a product decision about who this kit is for.

## 5. Production-readiness checklist

Branch-dependent. A is four characters plus arms. B adds a marker pair to a rendered artifact and
needs the re-render to preserve it, which is the one place this repo has recorded data loss. C adds a
markdown parse to the driver.

## 6. Acceptance criteria

- **AC1** — a project declaring an extra handle can no longer reach `--waive` for a directive the
  Skill's table does not show, demonstrated by an arm that declares one and asserts the refusal.
- **AC2** — the resolved rule is stated in `memory/guides/UNATTENDED-PROTOCOL.md` §10 and the shipped
  `PROTOCOL.template.md` is byte-identical to it, per the existing parity leg.
- **AC3** — under branch B only: `bash tools/unattended/adopt-unattended.sh` re-renders without
  destroying a project region, asserted by writing a region, re-rendering, and `git hash-object`
  comparison of the region's bytes.
- **AC4** — under BRANCH B: a project declaring an extra handle AND a matching row in its own region
  closes clean, which is the branch's whole promise. (Stated per-branch because under A and C this
  criterion is unfalsifiable — this repo declares `DIRECTIVES_EXTRA=""`, so "silent on a tree with no
  extras" passes without the change.)
- **AC5** — `memory/map/features/unattended.md` names the resolved contract.

## 7. Gates

`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/check-unattended.test.sh` ·
`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`bash tools/unattended/adopt-unattended.test.sh` · `bash tools/run-gates.sh`.

## 8. Open questions

### Which branch? — RESOLVED (owner, 2026-08-16): BRANCH B, projects get a row source

The three are costed in §4. Summarised: **A** makes the key unusable and honest, four characters,
and then §10's "the project may only EXTEND" is false. **B** keeps the contract true and buys a
marker-region preservation problem this repo has already lost data to once. **C** keeps both but
makes the driver parse markdown at run time and turns the leg into a second opinion on the driver's
own parse.

The owner took **B** on 2026-08-16, and the MECHANISM changed at build time — same branch, same
promise, a different way of keeping it.

rev-2 put the project's rows in a region INSIDE the rendered Skill, which made
`adopt-unattended.sh` responsible for preserving adopter bytes across a re-render. Reading that
render before writing the arm: it is a pure template substitution whose own comments record a
zero-byte write that `--check` then certified, and two failed attempts at escaping conf values.
Adding byte-preservation to it is the highest-risk change available in this kit, for a feature
no project uses yet.

**Built instead as a conf-declared table file.** `.unattended.conf` gains an optional
`DIRECTIVES_EXTRA_TABLE` naming a project-owned markdown file; check 16 arm A joins the
EFFECTIVE set against the kit table UNION that file's rows. The file is never rendered, so
there is nothing to preserve and the data-loss class does not arise. Undeclared, it is the
empty set and every existing adopter is unaffected — which is also what makes the change safe
to land before anyone uses it. The build order follows from its one real risk: the
marker-region preservation arm — write a project region, re-render, compare the region's bytes — is
written BEFORE the region is introduced, because `TOOL-aMouldedFolio-4` records that this repo's
four marker-region implementations disagree and that one of them deleted authored data.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from `TOOL-cBriefedPilot-31`.
- rev-3 · 2026-08-16 · build-time mechanism change WITHIN branch B: a conf-declared table file
  rather than a region inside the rendered Skill, because the render is the one mechanism here with a
  recorded data-loss incident and the file form has nothing to preserve. §4 carries the reasoning.
- rev-2 · 2026-08-16 · M4 audit fold, then OWNER RESOLUTION. Branch A was mis-costed at four
  characters: `core` is read by arm B as well as arm A, so widening it extends the section-resolution
  rule to extras. AC4 was unfalsifiable under two of three branches. **Owner took BRANCH B on
  2026-08-16**; §8 records it and the marker-preservation arm is written first.

## 10. Reuse audit

Branch B reuses the marker-region shape the build README already uses for `<!-- roster:units -->` and
the run-state file uses for its generated region, rather than inventing a third convention —
`region()` and `splice()` in the driver are the existing readers, and `TOOL-aMouldedFolio-4` records
that the four implementations of that primitive disagree, which is why the arm comes first. Branch A
reuses arm A's existing `comm` join with one variable widened. Branch C would reuse the leg's own
`tblpairs` awk, moved into the driver — and that move is what §4 argues against, since it makes two
components share a parse instead of second-opinioning each other.
