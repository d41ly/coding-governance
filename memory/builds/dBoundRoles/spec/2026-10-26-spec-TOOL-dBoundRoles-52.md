# TOOL-dBoundRoles-52 — unit 47's cross-unit render pair runs on a role that reads both of its inputs: `gov-orienter`, the span typed in `input:question` and handed in `input:prompt`

**Status:** DEFERRED · rev-3 · 2026-10-26 · node d · Tier-2 · base 462d20f3 · streams tooling · order 22 · advances TOOL-dBoundRoles-27

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dBoundRoles-1-agent-ledger.md) | journal | TOOL-dBoundRoles-1 TOOL-dBoundRoles-2 TOOL-dBoundRoles-3 TOOL-dBoundRoles-4 TOOL-dBoundRoles-5 TOOL-dBoundRoles-6 TOOL-dBoundRoles-7 TOOL-dBoundRoles-8 TOOL-dBoundRoles-9 TOOL-dBoundRoles-10 TOOL-dBoundRoles-11 TOOL-dBoundRoles-12 TOOL-dBoundRoles-13 TOOL-dBoundRoles-14 TOOL-dBoundRoles-15 TOOL-dBoundRoles-16 TOOL-dBoundRoles-17 TOOL-dBoundRoles-18 TOOL-dBoundRoles-19 TOOL-dBoundRoles-20 TOOL-dBoundRoles-21 TOOL-dBoundRoles-22 TOOL-dBoundRoles-23 TOOL-dBoundRoles-24 TOOL-dBoundRoles-25 TOOL-dBoundRoles-26 TOOL-dBoundRoles-37 TOOL-dBoundRoles-38 TOOL-dBoundRoles-39 TOOL-dBoundRoles-40 TOOL-dBoundRoles-41 TOOL-dBoundRoles-42 TOOL-dBoundRoles-43 TOOL-dBoundRoles-44 TOOL-dBoundRoles-45 TOOL-dBoundRoles-46 TOOL-dBoundRoles-47 TOOL-dBoundRoles-48 TOOL-dBoundRoles-49 TOOL-dBoundRoles-50 TOOL-dBoundRoles-51 TOOL-dBoundRoles-53 TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 TOOL-dBoundRoles-59 TOOL-dBoundRoles-60 TOOL-dBoundRoles-61 TOOL-dBoundRoles-62 TOOL-dBoundRoles-63 TOOL-dBoundRoles-64 TOOL-dBoundRoles-65 TOOL-dBoundRoles-66 TOOL-dBoundRoles-67 TOOL-dBoundRoles-68 TOOL-dBoundRoles-69 |
| [2026-10-26-build-TOOL-dBoundRoles-52-deviation-521.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-deviation-521.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-52-deviation-522.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-deviation-522.md) | deviation | — |
| [2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md](../build/2026-10-26-build-TOOL-dBoundRoles-52-round3-fix-return.md) | research | TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58 |
| [2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md](../prompts/2026-10-26-prompt-TOOL-dBoundRoles-52-round3-fix-brief.md) | research | TOOL-dBoundRoles-53 TOOL-dBoundRoles-55 TOOL-dBoundRoles-58 |
| [2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md](../reviews/2026-10-26-review-TOOL-dBoundRoles-52-spec-audit-round1.md) | spec-audit | TOOL-dBoundRoles-54 TOOL-dBoundRoles-55 TOOL-dBoundRoles-53 TOOL-dBoundRoles-56 TOOL-dBoundRoles-57 TOOL-dBoundRoles-58 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the seven promoted specs 45 to 51
(`memory/builds/dBoundRoles/reviews/2026-10-26-review-TOOL-dBoundRoles-45-spec-audit-round1.md`) confirmed
finding **id 13 at HIGH**, report item **H1**. Id 30 shares the item at HIGH and takes
`TOOL-dBoundRoles-53`; ids 2 and 39 report the same defect at MEDIUM, item M1, and are
`TOOL-dBoundRoles-58`'s.

Id 13 is the grounding face of the item. `TOOL-dBoundRoles-47` S1 renders `--role gov-builder` with
`--input spec=` and `--input question=`. `tools/roles/agents/gov-builder.agent.md:7` reads
`input:spec, card:route?, brief:non-goals?`, and `tools/roles/handoff.py:1025-1028` calls `ap.error` for
any input other than `prompt` that the role does not read, before `render_handoff` or `check_anchors`
runs. Both renders exit 2 with a usage error, so 47 AC1 and AC2 cannot pass on a correct build, and the
easy green is to widen `gov-builder`'s `reads`, which no spec authorizes.

This unit moves the render pair onto a role whose `reads` hold one typed input and one handed path
input, and restates unit 47's criteria for it. It repairs `TOOL-dBoundRoles-47` and builds one step
after it (order 22).

## 2. Scope (IN)

- **S1** — The role and its two inputs. The case unit 47 adds to `tools/roles/adopt-roles.test.sh`
  renders `--role gov-orienter`. Its typed input is `--input question=`, holding the span
  `record:TOOL-tFix-9@000000000000`; its handed input is `--input prompt=`, naming a scratch file inside
  the fixture repository whose prose quotes the same span. `gov-orienter` reads
  `input:question, input:prompt?` (`tools/roles/agents/gov-orienter.agent.md:8`), and `prompt` is in
  `PATH_INPUTS` (`tools/roles/handoff.py:99`), so `TOOL-dBoundRoles-38` fences it as handed content and
  `TOOL-dBoundRoles-45` §4 "The one answer" lists it among the fenced blocks. The refusal render exits
  non-zero naming the span once; the plain-words render exits 0 and writes its prompt file. Observed by
  AC1.
- **S2** — Seen accepted before relied on. Before editing the case, the pass renders the plain-words
  pair on the tree unit 47 left and records the command, its exit 0 and the written file in this unit's
  acceptance ledger. Observed by AC2.
- **S3** — Unit 47's spec follows the case. The pass bumps `TOOL-dBoundRoles-47`'s spec with S1, AC1,
  AC2 and its `New arm:` line restated for `gov-orienter` and `input:prompt`, and a §9 line naming this
  unit, before it edits the case (BUILD-METHOD M2, READY). Unit 47's ledger answers AC1 and AC2
  `amended rev-<n>`, naming that revision. Observed by AC3.

## 3. Non-goals (OUT)

- The guard that the case's role reads every key it passes, and the refusal half's distinction from a
  usage error: `TOOL-dBoundRoles-53`'s, for id 30.
- A second render over `input:diff`, and deriving the case's typed inputs from their set:
  `TOOL-dBoundRoles-58`'s, for ids 2 and 50.
- Widening any role's `reads`. `gov-builder` keeps the keys it reads at base.
- The fence, the strip and the graded text: units 38, 45, 24 and 41, read through 47's case.

### Edges

- **consumes-from** `TOOL-dBoundRoles-47` — the cross-unit case, its staged break and its producers' comment, whose render pair S1 re-roles (id 13)
- **hands-off** `TOOL-dBoundRoles-53` — the re-roled pair on `gov-orienter`, which unit 53 guards so the case cannot pass or fail on argument parsing (ids 13 and 30)
- **hands-off** `TOOL-dBoundRoles-60` — S1, AC3, §3, §4 Rollout and §7, which unit 60 restates: the shared suite's writers, the restated criterion, the read-key citation and the floor move (ids 4, 6, 14, 23, 27 and 37 of the round-1 audit of units 52 to 58)
- **hands-off** `TOOL-dBoundRoles-64` — §4 Rollout and §3, which unit 64 corrects where the wrapped disjointness claim survives and extends by the hands-off bullet for unit 63 (ids 25 and 26 of the round-1 audit of units 61 to 63)

## 4. Design

### Evidence

Read at base `462d20f3` on 2026-10-26:

- `tools/roles/agents/*.agent.md` `reads:` lines: no role reads both `input:spec` and `input:question`;
  the four that read `input:question` are `gov-orienter`, `gov-researcher`, `gov-reuse-scout` and
  `gov-session`, and only `gov-orienter` also reads a path input.
- `tools/roles/handoff.py:1027` exempts `prompt` from the reads check; `:331-336` resolves a path input
  to a repository file.
- `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-1.md` §4 "The roster" keeps
  `gov-orienter`, and no spec of this build changes its `reads`.

### Why a handed `prompt` stands in for a handed `spec`

The case separates a typed copy of one span from a handed copy of it. Which handed key carries the
file does not matter to that question, only that the render fences it as handed content, and every
`PATH_INPUTS` member is fenced under 38 S2. `input:prompt` is that member on the one role that also
reads a typed input.

### Inventory

Minted: none. The case keeps its name, its scratch file and its span.

### Migration

None: no stored data changes.

### Rollout

Live at landing, at order 22, after unit 47 at order 21. `TOOL-dBoundRoles-26` holds order 22 and writes
no file this unit writes; `TOOL-dBoundRoles-53` shares the order, consumes from this unit and writes the
same suite, so `--dispatch` holds it until this unit is CLOSED.

### Files touched (estimate)

- `tools/roles/adopt-roles.test.sh`
- the spec of TOOL-dBoundRoles-47, a rev bump (S3), named here for the dispatch write set

### Alternatives rejected

- **Add `input:question?` to `gov-builder`'s reads.** It widens a write-class role's inputs for a test's
  convenience, a surface no clause of this build prices (BUILD-METHOD M3 veto 3).
- **A scratch role declared in the fixture's catalogue.** It tests a role no adopter has; the real
  roster already holds one that reads both kinds of input.
- **`gov-skeptic` with a typed `diff` beside a handed `spec`.** Sound, and `TOOL-dBoundRoles-58` adds it
  as the second render for id 2; the question is 47's own typed input, so the first render keeps it.

## 5. Production-readiness checklist

- security — keeps the anchor check's cross-unit regression observable without widening a role's inputs;
  no new write path.
- perf / scale — the same two renders 47 adds.
- error / empty / loading states — the refusal render writes no file, which the case asserts.
- observability — the case's comment still names its four producers (47 S3).
- risks — a later unit that drops `input:prompt?` from `gov-orienter` breaks the pair; unit 53's guard
  then fails the case naming the role and the key.
- testing — AC1 to AC3 by render, ledger and grep; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`: no user-facing surface changes.

## 6. Acceptance criteria

- **AC1** — When the roles adopter fixture runs `handoff.py render --role gov-orienter` with
  `--input question=` holding `record:TOOL-tFix-9@000000000000` and `--input prompt=` naming the scratch
  file that quotes it, the render exits non-zero, its stderr names the span once, and no prompt file is
  written; with the question holding plain words it exits 0 and writes its prompt file.
  Red when: the role refuses an input at argument parsing, the typed span passes, or the handed span
  refuses.
  fixture: a scratch repository with the roles kit installed, under `%TEMP%`, short-pathed.
- **AC2** — When `grep -n 'gov-orienter' <this unit's acceptance ledger>` runs over this unit's own
  `**Evidences:**` block, it names the plain-words render the pass ran before editing the case, with
  exit 0 and the prompt file it wrote.
  Red when: the case is re-roled with no render showing the pair accepted first.
- **AC3** — When `grep -n -- '--role gov-builder' tools/roles/adopt-roles.test.sh` runs, no line it prints
  sits in the case whose comment names `TOOL-dBoundRoles-47`, and unit 47's spec carries a §9 line naming
  `TOOL-dBoundRoles-52`.
  Red when: the case still renders a role that does not read its typed input, or 47's criteria still
  name it.

## 7. Gates

`roles adopter self-test` · `roles catalogue` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/adopt-roles.test.sh · covers AC1 · the re-roled render pair, staged by a `render_handoff` that wraps typed values in `render_handed_fence`, which stops the planted span from refusing · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. Unit 47 carries no
  clause; veto 1 discards (b). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the precedent
  `TOOL-dDeclaredLoop-36` §8 F1 set. widens: none · relaxes: none
- **F2 — Which role carries the pair?** Options: (a) `gov-orienter`, typed question and handed prompt;
  (b) `gov-builder` with `input:question?` added; (c) a scratch fixture role; (d) `gov-skeptic` with a
  typed diff. (b) widens a role's inputs no clause prices, veto 3. (c) tests no shipped role. (a) and (d)
  survive; (a) keeps 47's own typed input, and (d) lands as the second render in unit 58. RESOLVED
  (agent, 2026-10-26, delegated): (a), rung 3, the report's first sound option. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of units 45 to 51, id 13
  (HIGH, item H1, shared with id 30; ids 2 and 39 share the defect at MEDIUM, item M1), on the report's
  first sound fix.
- rev-2 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-60, the minors batch of the round-1 audit of units 52 to 58; nothing else moved.
- rev-3 · 2026-10-26 · §3 · the Edges block gains the bullet mirroring TOOL-dBoundRoles-64, the minors batch of the round-1 audit of units 61 to 63; nothing else moved.

## 10. Reuse audit

The seam is the roles adopter suite's render fixture (`tools/roles/adopt-roles.test.sh`), where unit 47
puts the case, and the shipped roster's `reads:` lines, from which the role is chosen rather than added.
`python tools/codebase-map/reuse_lookup.py "a render case whose role must read every input key it passes"`
ranked `read`, `read_text`, `key` and `render`, none a render case of the roles kit, so no existing seam
fits beyond the suite's fixture and the roster.

Recall terms used: `python tools/memory-recall/query.py "how does a render case pick a role whose reads accept its inputs" --terms "handoff render role reads input question prompt spec typed handed refusal fixture"`
