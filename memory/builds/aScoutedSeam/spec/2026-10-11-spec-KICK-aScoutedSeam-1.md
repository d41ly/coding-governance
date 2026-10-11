# KICK-aScoutedSeam-1 — kickoff asks once, runs the scout on opt-in, and carries its seams onto the card and into the brief

**Status:** SPECCED · rev-1 · 2026-10-11 · node a · Tier-2 · base d19938f3 · streams kickoff · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md](../build/2026-10-11-build-TOOL-aScoutedSeam-1-1-failure-analysis.md) | research | TOOL-aScoutedSeam-1 TOOL-aScoutedSeam-2 TOOL-aScoutedSeam-3 DEPL-aScoutedSeam-1 |

<!-- /gen:spec-records -->

## 1. Goal

Make the reuse scout a fixed step of orientation rather than a probe a session may skip. The measured
inCMS lookup log held one row ever, so a step left to the session's judgement is not run. On the
owner's opt-in, kickoff runs `TOOL-aScoutedSeam-1`'s harness before any spec is written. It puts the
binding seams on the READY card, as the owner asked, and into the brief the builder reads.

## 2. Scope (IN)

- **S1** — The opt-in, three sources in this precedence, mirroring the spec audit's:
  - a dated `reuse-scout:` key in the build README's front matter, such as `reuse-scout: 2026-10-11`;
  - a dated `REUSE_SCOUT_DEFAULT` in `.unattended.conf`, the project-wide "run it every time";
  - else the owner's answer to ONE Step 3 question, asked only when the task writes product code and
    neither of the above is declared.

  One checker verb resolves the first two, `manifest-check.sh --reuse-opt-in [--base <sha>]`, and
  prints the source and the date or `absent`. With `--base` it reads the README and the conf at that
  commit, never the worktree. The answer is recorded on `## open` as `reuse scout: declared <date>`,
  `reuse scout: project default <date>` or `reuse scout: not declared (owner)`. A malformed key reads
  as absent, never as yes.
  - AC1 and AC5 observe it.
- **S2** — The invocation. The manifest command catalog gains one line, in `MANIFEST-TEMPLATE.md` and
  in this repo's `memory/guides/SESSION-KICKOFF.md`. The line runs `handoff.py harness-args
  reuse-scout` for the `roles` object, then the `Workflow` call by `scriptPath` with the args
  `TOOL-aScoutedSeam-1` declares. Engine Step 4 gains one clause pointing at that line; the engine
  carries no procedure.
  - AC2 observes it.
- **S3** — Step 5 appends the harness's `section` as a SEVENTH section of the READY body, in the same
  single `--card --append`, so the READY tail never erases it. `--card --append` grades the section:
  - every line under `## reuse` is one of the five line kinds of `TOOL-aScoutedSeam-1`'s grammar;
  - the section holds exactly one `scout` line;
  - a malformed line refuses the append, naming that line.
  - AC3 observes it.
- **S4** — The brief's `### Reuse` sub-head carries the harness's FULL return in the same line
  grammar: every seam, every constraint, every unmet need and the `scout` line. The card's section is
  the capped view of that list. `BRIEF_SKELETON`'s placeholder under `### Reuse` says so. When the
  scout did not run, the placeholder's old text stands.
  - AC4 observes it.
- **S5** — The card's `**Reuse:**` task field, which aOrientedCast's first kickoff unit adds, becomes
  the one line `see ## reuse` whenever the section exists, so reuse has one answer on the card.
  - AC3 observes it.
- **S6** — An unattended run resolves the opt-in with `--reuse-opt-in --base <BASE>`, so a key its own
  worktree gained after BASE does not count. The orientation step of `UNATTENDED-VERBS.md`, rendered
  from the unattended kit's template, names the scout and that verb, on both the slug and the prompt
  path.
  - AC5 observes it.

## 3. Non-goals (OUT)

- The harness, the role and the section grammar: `TOOL-aScoutedSeam-1`.
- Grading that a spec cites the seams: `TOOL-aScoutedSeam-2`.
- Host-tree resolution for a package repository. Until `DEPL-aScoutedSeam-1` lands, the caller passes
  an empty `hostTrees`.
- The attended router's orient stage. aOrientedCast's router runs the same harness through the
  catalogue's `reuse` row; this unit edits kickoff only.
- A hook that refuses a spec-writer spawn when the scout did not run. Opt-in is the owner's, and a
  build without it is legal.

### Edges

- **consumes-from** `TOOL-aScoutedSeam-1` — the harness, its args and its section grammar.
- **hands-off** `TOOL-aScoutedSeam-2` — the brief's `### Reuse` lines this unit writes are what
  check 12 joins a spec's §10 against.
- **hands-off** `DEPL-aScoutedSeam-1` — resolving `hostTrees` for a package repository.
- **hands-off** `TOOL-aScoutedSeam-3` — the card's `## reuse` section, which the diff mode's wiring
  half reads.
- **consumes-from** external — aOrientedCast's two kickoff units, which edit `manifest-check.sh` and
  `SKILL.md` first and add the `**Reuse:**` task field. This unit builds after them and reconciles if
  it lands second.
- **consumes-from** external — aRoutedQuill's landed brief flow: `BRIEF_SKELETON`, the brief written
  at Step 5 and committed with the specs.

## 4. Design

### Data model

`.unattended.conf` gains one key, documented beside `SPEC_AUDIT_DEFAULT`:

```bash
REUSE_SCOUT_DEFAULT=""   # date; an owner's standing opt-in to the reuse scout at every orientation. Blank = ask at kickoff
```

The `## open` answer line takes one of three forms, the same shapes `spec audit:` uses.

### Flow

1. Step 3 resolves the opt-in (S1). With none declared, and a task that writes product code, it asks
   once.
2. Step 4, on opt-in, runs the catalog line (S2). The card is not touched yet.
3. Step 5 writes the brief with `### Reuse` filled from the return (S4). It appends the READY body
   with `## reuse` as its seventh section (S3), and rewrites the `**Reuse:**` field to its pointer
   (S5).
4. After the owner's go, the brief is committed with the specs, under aRoutedQuill's flow.

### The grammar check

`--card --append` parses `## reuse` with a closed set of line heads: `- MUST `, `- SHOULD `,
`- constraint `, `- unmet ` and `- scout `. A seam line must carry ` :: ` and ` — `. The check grades
SHAPE: a well-formed line naming the wrong seam passes, and that is `TOOL-aScoutedSeam-2`'s and the
diff mode's to catch.

### Inventory

| identifier | cell |
|---|---|
| `REUSE_SCOUT_DEFAULT` | conf key |
| `--reuse-opt-in` | checker verb, no naming cell |
| `check_reuse_section`, `resolve_reuse_opt_in` | sh.function |
| `reuse-scout` (README front-matter key) | front-matter key |

### Files touched (estimate)

- `skills/session-kickoff/SKILL.md`
- `skills/session-kickoff/MANIFEST-TEMPLATE.md`
- `skills/session-kickoff/manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`
- `memory/guides/SESSION-KICKOFF.md`
- `.unattended.conf`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`

### Rollout

Default OFF. Nothing runs until the owner declares a key or answers yes. The card check binds only a
card that carries `## reuse`, so no existing card reds.

### Alternatives rejected

- **Appending `## reuse` at Step 4.** The READY append replaces the card's tail, so a section appended
  before it is erased (`manifest-check.sh` `add_card_body`).
- **The full list on the card.** A six-section card measured 6547 of its 8192 bytes, so the full list
  would refuse the append; the brief carries it instead.
- **A hook that forces the scout before any spec spawn.** The owner asked for opt-in, and the spec
  join catches a dropped seam deterministically.

## 5. Production-readiness checklist

- security: no new write path. The opt-in keys are read, and a run cannot write its own, by the
  existing self-opt-in rule.
- perf / scale: the scout's cost is `TOOL-aScoutedSeam-1`'s; kickoff adds one append and one brief
  sub-head.
- error / empty / loading states: a dead lens is announced in the section and on the READY hand-back.
  A refused append names the line, and the session repairs it before the hand-back.
- observability: the `## open` answer line and the section's `scout` line.
- risks: the engine is 176 bytes under its 18432-byte ceiling, measured this session, and aOrientedCast's
  kickoff units edit it first. The clause is priced against the high-water before it is written.
- testing: `manifest-check.test.sh` gains arms for the grammar check and the opt-in precedence.
- migration: N/A — a new optional key and a new optional section.
- user docs: the manifest template's catalog line and the conf key's comment.

## 6. Acceptance criteria

- **AC1** — When a fixture README carries `reuse-scout: yes` and the conf a dated
  `REUSE_SCOUT_DEFAULT`, `manifest-check.sh --reuse-opt-in` prints `project default <date>`; with the
  README key dated it prints `declared <date>`.
  Red when: an undated key reads as yes.
- **AC2** — When the engine is measured by `check-template-size.sh`, `SKILL.md` stays under its
  ceiling with the Step 4 clause, and the clause names the manifest's catalog line rather than the
  procedure.
  Red when: the procedure is written into the engine and the size gate reds.
- **AC3** — When `manifest-check.sh --card --append` receives a body whose `## reuse` holds a line
  starting `- maybe `, it refuses naming that line and writes nothing. A conforming section appends
  and survives `--card --replay`.
  Red when: the append accepts an unknown line head.
- **AC4** — When `manifest-check.sh --brief-skeleton` prints the skeleton, its `### Reuse` placeholder
  names the scout's line grammar and the fallback for a build with no opt-in.
  Red when: the placeholder still names only the two probes.
- **AC5** — When a fixture worktree's README gains a dated `reuse-scout:` key after BASE,
  `manifest-check.sh --reuse-opt-in --base <BASE>` prints `absent`, and without `--base` it prints
  `declared <date>`.
  Red when: the `--base` read falls back to the worktree copy.

## 7. Gates

`kickoff-manifest ratchet` · `kickoff engine size <=18KiB` · `manifest-check self-test` · `unattended protocol size` · `memory hygiene` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `scratch-guard self-test`

New arm: skills/session-kickoff/manifest-check.test.sh · covers AC1 AC3 AC4 AC5 · fixture cards, READMEs and a fixture repo with a post-BASE commit, staged per arm · none

## 8. Open questions

- **F1 — Should the project default be armed in gov itself when this lands?** Arming it makes every
  gov kickoff that writes product code run the scout, at the measured cost. Recommendation: leave it
  blank and let the owner arm it after `TOOL-aScoutedSeam-1`'s calibration reports the cost at
  effort `medium`.
- **F2 — Does the Step 3 question also cover a task that writes only records?** The measured
  reinventions were all product code. Recommendation: product code only, the same trigger that writes
  a brief.

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

The opt-in extends the spec audit's pattern: the README key, the conf default read at BASE, the one
kickoff question and the self-declaration refusal. The front-matter reader is `readFrontMatterKey` in
`tools/hooks/scratch-guard.js`, and the card writer is `add_card_body` in
`skills/session-kickoff/manifest-check.sh`. The brief sub-head is the `### Reuse` of `BRIEF_SKELETON`,
which aRoutedQuill landed. `tools/codebase-map/reuse_lookup.py "ask the owner once for a dated opt-in
declared in the build README front matter or a project conf default"` ranked `build`, `load_conf` and
`parse_conf` by stem and missed all four, so they were found by reading.

Recall terms used: spec-audit opt-in README front matter SPEC_AUDIT_DEFAULT kickoff question card append brief skeleton
