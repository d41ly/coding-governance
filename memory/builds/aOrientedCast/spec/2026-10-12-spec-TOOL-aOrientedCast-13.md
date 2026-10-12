# TOOL-aOrientedCast-13 — a gate allowlist may name a leg the target lacks, marked optional

**Status:** INPROGRESS · rev-2 · 2026-10-12 · node a · Tier-2 · base 646d4a73 · streams tooling · order 13 · ratified 2026-10-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-12-1-spec-brief.md) | journal | TOOL-aOrientedCast-12 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 |
| [2026-10-12-prompt-TOOL-aOrientedCast-13-1-fold-brief.md](../prompts/2026-10-12-prompt-TOOL-aOrientedCast-13-1-fold-brief.md) | journal | TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 |

<!-- /gen:spec-records -->

## 1. Goal

This unit closes review item H2 of
[the closing review, round 1](../reviews/2026-10-12-review-TOOL-aOrientedCast-1-closing-diff-round1.md).
The seeded `tools/roles/house/policy.toml` grants `lexicon naming predicates`, a leg only the
lexicon kit declares, and a default install with a manifest runner holds no lexicon kit, so
`load_policy` raises R12 there and the roles catalogue, the render and `stage-efforts` all refuse.
A `[gates]` name may now carry a trailing `?`, which makes a leg the target's manifest lacks a note
rather than a defect, and the seed marks the lexicon grant that way.

## 2. Scope (IN)

- **S1** — `load_policy` in `tools/roles/roles_lib.py` (lines 210-310) reads a `[gates]` name ending
  in `?` as OPTIONAL. When the manifest reads and holds no leg of the name without its `?`, one line
  is appended to `notes`, when given, naming the slot, the name and the manifest, and no defect is
  raised. A bare name the manifest lacks keeps today's R12 defect, so a misspelt required leg still
  refuses. A name that is empty once its `?` is taken off is an R12 defect. Observed by AC1 and AC2.
- **S2** — The policy `load_policy` returns carries every `[gates]` list with the `?` taken off each
  name, so `render_agents.py`, which writes `policy["gates"]` into `.claude/roles.json`, and the
  hooks kit, which compares those strings with manifest leg names, read plain leg names and need no
  edit of their own. Observed by AC2 and AC3.
- **S3** — The seed `tools/roles/house/policy.toml` grants `["memory hygiene", "lexicon naming
  predicates?"]` to `gov-spec-writer` and `["lexicon naming predicates?"]` to `gov-builder`, with one
  comment line saying a trailing `?` marks a leg whose kit a target may not install. `memory
  hygiene` stays bare: the memory-tree kit declares it and the roles kit requires that kit. Observed
  by AC3 and AC4.
- **S4** — `render_agents.py --selftest` gains arm 13: a policy naming `["leg a", "absent?"]` over a
  fixture manifest holding only `leg a` renders with exit 0, prints a note naming `absent`, and
  writes `["leg a", "absent"]` as that role's index `gates`; arm 12's bare `nope` still exits 2.
  Observed by AC2.
- **S5** — `check_roles_install` in `tools/govkit/selftest.py` (line 2563) gains a `runner` flag. With
  it set, the scratch target's deploy text carries a `[gate_runner]` table built from the run-gates
  descriptor's `[gate_runner_seed]`, so the default apply writes the target's own
  `<prefix>/gate-legs.json`, and the target's `adopt-roles.sh --check` and `check_roles.py` must each
  exit 0. `main` calls it once more with the flag. Observed by AC4.
- **S6** — The roles README's `[gates]` paragraph (`tools/roles/README.md:87`) and the R12 line of
  `check_roles.py`'s docstring (`:30-35`) say what the `?` does. NOT OBSERVED by a criterion: prose,
  read by the review against §4.

## 3. Non-goals (OUT)

- No change to the hooks kit. The role index's `gates` lists keep their shape, so `checkRoleGate`
  and `readGateLegs` in `tools/hooks/scratch-guard.js` read them unchanged.
- No second seed file and no per-target policy render: the seed is still copied once and owned by
  the target afterwards.
- No `?` on `memory hygiene`, and no `?` inferred from a kit's absence: the marker is the policy
  author's statement, read as written.
- No kit-version bump for roles or govkit; each touched kit moves once at the close.

**What it is built on.** This unit extends `TOOL-aOrientedCast-11`'s `[gates]` table, its R12
grading in `load_policy` and the index's `gates` lists, without moving their shape. Its govkit arm
installs the case `TOOL-aOrientedCast-8` built: `check_roles_install` and the default selection that
ships roles without lexicon. Both specs are CLOSED and declare no edge to this unit, and a one-sided
edge reds the hygiene gate's join, so the dependency is stated here rather than as an edge.

### Edges

none

## 4. Design

### The mechanism

In `load_policy`'s `[gates]` loop (`roles_lib.py:293-305`), each name `n` that passes the
list-of-strings test is split into its leg name, `n[:-1]` when `n` ends in `?` and `n` otherwise,
and a flag. Then:

| The name | The manifest reads and holds the leg | The manifest reads and lacks it | The manifest does not read |
|---|---|---|---|
| bare | admitted | R12, as today | today's one note for the table |
| ends in `?` | admitted | a note naming slot, name and manifest | today's one note for the table |
| `?` alone, or empty | R12, "names no leg" | R12 | R12 |

The note reads: `<manifest> holds no leg '<leg>', which gates.<slot> marks optional, so <slot> is
granted no such leg here`. After the loop, and only when no defect was collected, each
`data["gates"][slot]` is rewritten to its leg names, so the returned policy holds no `?`. Every
caller that passes no `notes`, such as `handoff.py stage-efforts`, drops the note, as it drops
today's.

### Why a marker, and not a note for every unknown name

The skeptic's corrected fix offered two shapes: ship only required kits' legs in the seed, or treat
an unknown name as a note. The first cannot hold gov's own grant, because gov's policy IS the seed
file: `tools/roles/kit.toml` ships `house/policy.toml` as a `seed` byte for byte, so a seed without
the lexicon grant takes the owner's grant away from gov's builders. The second makes every misspelt
leg a note, which fails `TOOL-aOrientedCast-11` AC4's red condition, "a misspelt leg name passes".
The marker keeps that criterion for every bare name and tolerates absence only where the policy says
it may be absent. It reuses the kit's own optional spelling: a role's `reads` key marks an optional
input with the same trailing `?` (`handoff.py:288-298`). The fork is §8 F1.

### The govkit arm

`check_roles_install(tmp, charter=True, runner=False)`. With `runner` set, the target directory is
`roles-runner`, and the deploy text is `DEPLOY_REGISTRY_DEFAULT` plus a `[gate_runner]` table whose
keys and values are those of `[gate_runner_seed]` in the run-gates `kit.toml`, read with `tomllib`
and written as `govkit.py`'s intake writes them (`:12632-12670`), so no runner key is typed into the
suite. A hand-written `[gate_runner]` in a fixture's deploy text is already how the suite's CE1 arms
make `apply` emit a manifest (`selftest.py:2420-2440`). After the apply the arm asserts that `<prefix>/gate-legs.json`
exists and holds no `lexicon naming predicates` leg, which proves the fixture is the case under
test, then that the target's `adopt-roles.sh --check` exits 0, and that the target's
`check_roles.py` exits 0 with a `roles: note:` line naming `lexicon naming predicates`. The existing
assertions keep their tags; the new ones carry `OC13`.

### Migration

None. The roles kit has not landed: the base `646d4a73` holds no `tools/roles/`, so no adopter holds
the seed with a bare lexicon grant. Gov's `.claude/roles.json` is byte-identical after the change,
because the returned lists carry the same leg names.

### Inventory

No function, class or constant is minted. `check_roles_install` gains the `runner` parameter, and
`render_agents.py`'s self-test gains arm 13 inside its existing self-test function.

### Files touched (estimate)

`tools/roles/roles_lib.py`
`tools/roles/house/policy.toml`
`tools/roles/render_agents.py`
`tools/roles/check_roles.py`
`tools/roles/README.md`
`tools/govkit/selftest.py`

### Alternatives rejected

- A note for every name the manifest lacks: fails `TOOL-aOrientedCast-11` AC4, as above.
- A seed naming only `memory hygiene`: takes gov's owner-ruled lexicon grant away, as above.
- A kit-qualified name such as `lexicon:lexicon naming predicates`, tolerated when that kit's
  directory is absent: it needs the policy reader to locate a sibling kit by its home, a second
  spelling of what the manifest already answers, and a new syntax the hooks would have to strip.

## 5. Production-readiness checklist

- security — No new write path; the role gate stays fail-closed, because an optional leg the
  manifest lacks is a name no command can match.
- perf / scale — One string test per `[gates]` name, inside a read that already parses the manifest.
- error / empty / loading states — A bare missing leg refuses as today; an optional one is a note; a
  `?` with no name refuses; an unreadable manifest keeps today's single note.
- observability — The note names the slot, the leg and the manifest, and it prints wherever today's
  manifest note prints: the catalogue checker and the render.
- risks — A typo inside an optional name is a note rather than a red. The marker confines that to the
  names an author marked, and the seed marks one.
- testing — Render self-test arm 13 and the govkit runner arm, observed RED-first at the close; the
  direct probes of §6 in the pass.
- migration — None, as §4 states.
- user docs — The roles README paragraph and the policy file's own comment line.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag; each calls the unit's own code or reads
its output. The suite arms are under `New arm:` in §7.

- **AC1** — When a `python -c` call of `roles_lib.load_policy` runs over a scratch kit copy whose
  policy grants `gov-builder = ["lexicon naming predicates?"]`, beside a scratch `gate-legs.json`
  holding only `memory hygiene`, it returns with no raise, its `notes` list holds one line naming
  `lexicon naming predicates`, and the returned `gates.gov-builder` is `["lexicon naming
  predicates"]`; with the grant staged bare, the same call raises naming it.
  Red when: an optional missing leg raises, a bare missing leg is admitted, or a `?` survives into
  the returned policy.
  fixture: a scratch copy under a short `%TEMP%` root, built in the pass.
- **AC2** — When `python tools/roles/render_agents.py --write` runs from a scratch repository whose
  kit copy's policy grants `["memory hygiene", "absent?"]` to a role and whose manifest lacks
  `absent`, it exits 0, prints a `render_agents: note` line naming `absent`, and `.claude/roles.json`
  holds `["memory hygiene", "absent"]` for that role.
  Red when: the render refuses the optional name, writes it with its `?`, or prints no note.
- **AC3** — When `python tools/roles/render_agents.py --check` and `python tools/roles/check_roles.py`
  run in gov after the seed carries the `?`, each exits 0, and `.claude/roles.json` is byte-identical
  to its parent commit's.
  Red when: the stripped names differ from gov's index, or gov's catalogue reds.
- **AC4** — When the govkit suite's new runner arm runs, a default apply with a `[gate_runner]` from
  the run-gates seed writes a target manifest lacking `lexicon naming predicates`, and the target's
  `adopt-roles.sh --check` and `check_roles.py` both exit 0.
  Red when: the seed's lexicon grant is staged bare, which reds both with R12.
  permission: this run's builder may not execute the govkit suite; the main loop observes the arm at
  the close, sliced to the one function rather than the whole suite.
  cost: one default apply into a scratch target, as each sibling call of the function pays.

## 7. Gates

`roles catalogue` · `roles render wiring` · `roles render selftest` · `govkit selftest` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor arms` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/roles/render_agents.py --selftest · covers AC2 · arm 13, an optional name over a manifest that lacks it, against a `load_policy` whose optional branch is staged out so the name raises R12 · none
New arm: tools/govkit/selftest.py · covers AC4 · `check_roles_install` with `runner` set, against the seed staged back to a bare lexicon grant · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — How does a gate allowlist name a leg that may be absent in a target?**
  Options: (a) every name the manifest lacks is a note; (b) the seed names only legs of required
  kits, and gov keeps its lexicon grant in its own copy; (c) a trailing `?` marks a name optional,
  and only an optional name the manifest lacks is a note; (d) a kit-qualified name, tolerated when
  that kit is absent.
  (a) fails `TOOL-aOrientedCast-11` AC4's red condition, a misspelt leg name passing: M3 veto 1.
  (b) cannot keep gov's grant without a second seed source, a new install location: M3 veto 2.
  (d) needs the reader to locate a sibling kit and a syntax the index would have to strip, leaving
  more open than (c).
  Recommendation: (c), which satisfies H2's left-shift arm and keeps every criterion already written.
  RESOLVED (agent, 2026-10-12, delegated): (c), as §4 "The mechanism" states it.
- **F2 — Does the status header carry `closes H2`, as the spec brief asks?**
  `backlog.read_header_verbs` expands a `closes` value through the generator's id grammar, and `H2`
  is no id: a probe of `_read_backlog_verbs` on such a header raised "is not an id or an id range",
  which refuses every render of the build index. The build keeps no `BACKLOG.md` to name an ask from.
  Options: (a) write the verb; (b) name the review item in §1 and leave the verb out.
  RESOLVED (agent, 2026-10-12, delegated): (b). Option (a) fails the build-index leg, M3 veto 1.

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft.
- rev-2 · 2026-10-12 · §3. The two `consumes-from` edges to `TOOL-aOrientedCast-11` and
  `TOOL-aOrientedCast-8` had no `hands-off` at their CLOSED sources and redded check 12's join; they
  move to a "What it is built on" paragraph, as `TOOL-aOrientedCast-11` did, and Edges reads `none`.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "gate allowlist names a leg the target manifest lacks"`
ranked name-token neighbours, `legs`, `leg` and `manifest`, none of which reads a role policy. No
existing seam fits as a new function; the seam extended is `load_policy`'s `[gates]` loop in
`tools/roles/roles_lib.py`, with `load_gate_leg_names` beside it unchanged, and the optional
spelling is the one `reads` keys already use in `tools/roles/handoff.py`. The govkit arm extends
`check_roles_install` rather than adding a sibling. The recall probe surfaced
`TOOL-aOrientedCast-11` S1 and the brief's own interface 4, both read against source.

Recall terms used: `policy gates allowlist leg seed default install lexicon load_policy R12 optional note manifest`
