# TOOL-aUnmannedHelm-9 — the adopter path, and the version marker that announces it

**Status:** CLOSED · rev-3 · 2026-08-10 · node a · Tier-2 · base f42980ce · streams tooling+deployer+playbook · ratified 2026-08-10 · review wf_077104e6

## 1. Goal

Make the kit installable into another repo, and make the playbook change it carries visible to a
re-pulling adopter. This is unit 7 of seven, the last; the master scope and the ratified decision
menu live in this build's `README.md`.

## 2. Scope (IN)

- **S1 · the adopter's refusals** — a foreign repo and an unsupported install prefix, both refusing
  before anything is written into either tree.
- **S2 · the junction shape ADOPTS.** A kit dir that is a junction inside the adopting repo anchors
  to the ADOPTING repo. The walk stays logical, never physical.
- **S3 · `tools/unattended/adopt-unattended.test.sh`**, the e2e, gated on EFFECTS rather than exit
  codes, with a LOUD skip where a host cannot create a link.
- **S4 · the fifth gate leg**, the e2e itself.
- **S5 · `governance-template` v2.5 -> v2.6** on the template and the companion in lockstep, with the
  v2.5 snapshot into `memory/archive/` and the re-pull note in `WIRE-INTO-PROJECT.md`.

## 3. Non-goals (OUT)

- **Installing the memory tree, the gate manifest or the conf for the adopter.** The adopter renders
  the Skill and PRINTS the remaining steps. Writing a project's gate manifest for it is a bigger
  decision than this script is allowed to make.
- **A `--scaffold` that writes `.unattended.conf`.** The conf holds a lander and a merge bar; a
  guessed value there is worse than an absent one, and the refusal already names what is missing.
- **Any agent-cap edit.** `TOOL-aNumeralWarden-1`'s.

## 4. Design

### The refusals, and the order they run in

Three questions, asked in this order, and the ORDER is load-bearing:

1. **Is the kit inside the repo I am adopting?** No → refuse, touch nothing.
2. **Is the install prefix supported?** The kit path is interpolated into shell commands in the
   rendered Skill, so whitespace in it renders `bash my kit/unattended.sh --status`, which runs
   `bash my` with three arguments. Refuse rather than emit a Skill that misfires at the first verb.
3. **Is the template there, and the conf?** Only now.

The ordering was wrong on the first cut and the e2e caught it. Run from a repo that does not own the
kit, the conf check fired FIRST — and its message ("no `.unattended.conf` at the repo root") sends
the operator to create a conf in the very repo the adopter must not adopt. A correct refusal with
the wrong remedy is a defect, not a rounding error.

### The junction contract, taken from the precedent rather than re-decided

`pwd` without `-P` keeps the path the caller traversed, so a kit dir that is a junction INSIDE the
adopting repo anchors to the adopting repo. That is the install shape this fleet uses, and the
codebase-map adopter's e2e scores a REFUSAL of it as a failure. Resolving physically would follow
the link and adopt the target's tree, silently.

The master README's row said "refuses a foreign repo and an unsupported prefix; ADOPTS correctly
through a junction", which is exactly this split, and it is the split the review corrected the rev-2
master spec into.

### Why the e2e is gated on effects

The adopter WRITES. An exit-code test passes on a script that refused correctly AND on one that
wrote into the wrong tree and then exited 2 for an unrelated reason. So every arm asserts what is on
disk in BOTH trees afterwards, and each refusal arm asserts that nothing was written at all. The
charter records why this is not paranoia: a Tier-2 review found four of seven defects, including a
blocker, in the codebase-map adopter — the one file no leg executed.

The junction arm SKIPS LOUDLY where the host cannot create a link. On a Windows node without the
privilege `ln -s` degrades to a copy, and a copy would score a refusal as success.

### The version marker

The template's §1 and §8 rules changed in unit 2, and the marker is the only re-pull signal the
product documents. So: banner and marker to v2.6, the companion's marker in lockstep, the v2.5
snapshot into `memory/archive/` — taken from the tree at the branch base, because the working copy
already carries the v2.6 edits — and a re-pull note in `WIRE-INTO-PROJECT.md` naming what moved and
pointing at the conditional-sections row first.

v2.5 had no snapshot of its own; `aCandidStub` released it on 2026-08-10 without one. This unit
takes it, which is why the archive gains two releases' worth of history in one commit.

### Files touched

New: `tools/unattended/adopt-unattended.test.sh`,
`memory/archive/parallel-coding-governance.template-v-2-5.md`. Edited:
`tools/unattended/adopt-unattended.sh` (the refusals and their order),
`parallel-coding-governance.template.md` (banner + marker + the v2.6 note),
`parallel-coding-governance.domain-rules.md` (marker), `WIRE-INTO-PROJECT.md` (the re-pull note),
`tools/gate-legs.json` (one entry), `AGENTS.md` (the leg citation).

### Alternatives rejected

- **Refusing a junctioned kit dir.** The precedent scores that as a failure, and this fleet installs
  that way.
- **Resolving the kit dir physically.** Adopts the link target, silently.
- **An exit-code e2e.** Passes on a script that wrote into the wrong tree.
- **Skipping the junction arm quietly.** A copy scores a refusal as success.
- **Bumping the marker without a snapshot.** The archive is what makes a re-pull a three-way merge
  rather than a guess.

## 5. Production-readiness checklist

- **security** — the adopter's write surface is one directory under the adopting repo, and the three
  refusals are what make "the adopting repo" unambiguous. All three are armed on effects.
- **perf / scale** — six scratch repos; seconds.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — every refusal names itself and writes nothing.
- **observability** — the adopter prints the remaining steps rather than performing them.
- **risks** — the dominant one is adopting the wrong tree. Both directions are asserted on disk.
- **testing + left-shift gates** — the e2e is a leg from this unit's landing.
- **migration / rollback** — the marker bump is the migration signal; the snapshot is the rollback.
- **user docs** — `WIRE-INTO-PROJECT.md`'s re-pull note.

## 6. Acceptance criteria

- **AC1** — Run from a repo that does not own the kit, the adopter refuses and NOTHING is written
  into either tree — not the caller's and not the kit owner's. All three observed.
- **AC2** — With whitespace in the kit path, the adopter refuses naming the interpolation hazard and
  writes nothing. Both observed.
- **AC3** — Through a junction inside the adopting repo, the adopter ADOPTS: it writes into the
  adopting repo, writes nothing into the link target, and the rendered commands carry the adopting
  repo's relative kit path. Observed, or LOUDLY skipped where the host cannot create a link.
- **AC4** — An ordinary adopt renders a Skill carrying the project's declared values, and
  `--check` immediately agrees with what `--render` wrote. Both observed.
- **AC5** — With the conf absent, and separately with the kit's template absent, the adopter refuses
  and leaves no half-stamped adoption. Both observed.
- **AC6** — The template and the companion both read `governance-template: v2.6`, the v2.5 snapshot
  exists in `memory/archive/`, and `bash tools/check-template-size.sh` is green with the remaining
  headroom recorded. All observed.

## 7. Gates

The standing bar, now 45 legs. Newly relevant: the run-gates canary and the template size gate.

**Build-wide constraint this unit inherits:** `non_terminal_specs_cited_by_product_source` measures
2 against a pin of 2, zero headroom.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 7 of seven, carrying the review's split of AC7 — refuse
  a foreign repo and an unsupported prefix, ADOPT through a junction — and the v2.6 bump with the
  v2.5 snapshot the previous release never took.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged, in the same pass. 19 assertions across six
  arms, one loudly skipped on this host for want of symlink privilege.

  **The refusal ORDER was wrong and the e2e caught it.** Run from a repo that does not own the kit,
  the conf check fired before the ownership check, so the operator was told "no `.unattended.conf` at
  the repo root" — a correct refusal with a remedy that points at the wrong repo. Ownership and
  prefix are now asked first, before the adopter reads anything at all.

  The unsupported prefix turned out to be concrete rather than theoretical: the kit path is
  interpolated into shell commands in the rendered Skill, so whitespace renders a command that
  word-splits at the first verb. That is the refusal, and it is armed on effects.

  Template headroom after the v2.6 note, read FROM the gate: 154 bytes.

- rev-3 · 2026-08-10 · LANDED on `main` in the merge commit that closes this build. CLOSED in this tree's vocabulary means built AND landed, which is true from the moment that commit exists; the push publishes it.

## 10. Reuse audit

- `tools/codebase-map/adopt-codebase-map.sh` and its e2e — the junction contract and the
  effects-gated arm shape, taken as precedent rather than re-decided. Its arm 5 scores a refusal of
  a junctioned kit dir as a FAILURE, which is the whole reason S2 reads the way it does.
- `tools/drift-audit/adopt-drift-audit.sh` — the render/`--check`/next-steps structure this script
  already followed at unit 5.
- `memory/archive/parallel-coding-governance.template-v-N-N.md` — the existing snapshot series,
  extended by one rather than replaced by a new convention.
- `WIRE-INTO-PROJECT.md`'s re-pull bullet — the existing mechanism, given a v2.6 paragraph rather
  than a parallel one.
- `parallel-coding-governance.customize.md`'s conditional-sections block — already carrying the
  unattended row from unit 2; the re-pull note points at it rather than restating it.
