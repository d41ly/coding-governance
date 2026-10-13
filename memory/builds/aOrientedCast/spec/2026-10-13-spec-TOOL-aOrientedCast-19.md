# TOOL-aOrientedCast-19 — an inline stand-in for a role declares itself through its handoff, and needs a dated owner waiver row

**Status:** CLOSED · rev-2 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 19 · ratified 2026-10-13

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 TOOL-aOrientedCast-23 |
| [2026-10-13-build-TOOL-aOrientedCast-19-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-19-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 PLAY-aOrientedCast-2 |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-18 PLAY-aOrientedCast-2 |
| [2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md) | journal | TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled that work goes to its role agent unless a tool or run cannot spawn a sub-agent at
all, and that any inline stand-in for a role needs an owner waiver row, graded like the other
waiver registries. This unit builds that registry under the memory root's `project/` folder, the
declaration a stand-in makes by rendering its handoff with `--stand-in`, and one catalogue-checker
rule that joins the two in both directions.

## 2. Scope (IN)

- **S1** — `roles_lib.load_stand_in_waivers(root, memory_root, roles)` is the one reader of the
  registry `<MEMORY_ROOT>/project/role-stand-in-waiver.txt`. It returns the valid rows keyed by
  `(build, role)` and one defect line per invalid row, under the row grammar of §4. An absent file
  returns no row and no defect. Observed by AC1, AC2 and AC7.
- **S2** — `roles_lib.scan_stand_in_declarations(root, memory_root)` is the one reader of the
  declarations: every file under `<MEMORY_ROOT>/builds/<slug>/prompts/` whose name ends in
  `-stand-in.md`, read through its `gov:handoff` marker. The marker grammar `MARKER_RE` now lives in
  `roles_lib`, and `handoff.py` reads it from there. Observed by AC3 and AC7.
- **S3** — `python handoff.py render ... --stand-in` is how a stand-in is declared. It writes the
  handoff under the derived name with a `-stand-in` tail, and refuses with exit 1, writing nothing,
  when no valid row covers its build and role. `--stand-in` shares the mutually exclusive group of
  `--out` and `--stdout`. Observed by AC6.
- **S4** — `check_roles.py` gains rule R15. A declaration no row covers is a defect, a row no
  declaration consumes is a stale defect, and each loader and scan defect is a defect. Every valid
  row prints as one `roles: note: stand-in waiver` line on every run, and the summary line carries
  the two counts. R0 also refuses a conf whose `MEMORY_ROOT` is blank or absent, as
  `adopt-roles.sh` and `handoff.py` already do. Observed by AC4 and AC5.
- **S5** — Hygiene check 3 admits `role-stand-in-waiver.txt` under `<MEMORY_ROOT>/project/` by
  name, beside `pass-order-waiver.txt`, and the existing check-3 admission arm of the hygiene
  self-test names both registries. Observed by AC8.
- **S6** — The roles README gains a section, "Standing in for a role", holding the exception, the
  row grammar, the declaration and R15. The docstrings of `check_roles.py` and `handoff.py` name
  R15 and `--stand-in`, each with what it does not check. NOT OBSERVED by a criterion: prose, read
  by the review against §4.
- **S7** — The memory-tree kit moves one minor version, with every carrier of that version. The roles
  kit's move is `TOOL-aOrientedCast-20`'s, the last unit of the set to touch `tools/roles/`.
  Observed by AC9.

## 3. Non-goals (OUT)

- No hook change. The write gate's role arm and the spawn guard read no waiver row. In Claude Code
  a sub-agent can always be spawned, so the role arm keeps refusing an inline spec or product write
  from the main loop (`tools/hooks/scratch-guard.js:1041`) whatever the registry holds. A waiver
  relaxes the `[roles]` rule for a tool the hooks never see; it never relaxes a gate.
- No charter text, no Agent roles section and no help page: the `[roles]` rule that names the
  exception and the registry, and `help/roles.md`, are `PLAY-aOrientedCast-2`'s.
- No seeded registry. The kit ships none and gov holds none, because an absent registry waives
  nothing, which is the correct state wherever every role can be spawned.
- No bullet in `memory/HYGIENE.md`'s registry list. That file is a governance carrier, which M3
  veto 2 keeps from a delegated run; the follow-up is the owner's.
- No detection of an UNDECLARED inline stand-in in a hook-less tool. Nothing in the tree records
  work that was done inline and never declared.
- No reading of the `mandatory` field `TOOL-aOrientedCast-17` adds. A row may name any role whose
  `agent` is true, and a waiver for a role that is never mandatory is harmless.
- No harness change. A run whose harness cannot spawn is a run that cannot spawn, and its main loop
  declares each stage it stands in for through the same flag.
- No roles kit version move, and so no edit to the Skill template or the rendered `/build` Skill,
  whose `gov:kit roles@` marker was this unit's only reason to touch either. `TOOL-aOrientedCast-20`,
  order 22, also writes `tools/roles/` and carries the set's one move, under the rule the
  `TOOL-aOrientedCast-17` spec's §4 "Rollout" states.

### Edges

- **consumes-from** `TOOL-aOrientedCast-16` — a `handoff.py render` and a `check_roles.py` that
  read the v4.3 charter without refusing. AC4's exit codes and AC6's render rest on that re-key, and
  this unit edits both scripts after it.
- **hands-off** `PLAY-aOrientedCast-2` — the `[roles]` rule names the waiver registry,
  `role-stand-in-waiver.txt` under the memory root's `project/` folder, beside the no-spawning
  exception; its help page says a stand-in declares itself by rendering its handoff as a stand-in,
  and points at the roles README's "Standing in for a role" section for the row grammar. No tree
  holds the registry until an owner writes its first row, so there is no header to point at.

## 4. Design

### The exception, and what a waiver reaches

A stand-in is the main loop doing a role's work itself, because the tool or run it lives in cannot
spawn a sub-agent at all. It still renders the role's handoff and follows it, so the role's
constant block and its task reach the actor exactly as they would reach an agent. The difference is
recorded twice: the owner's waiver row grants it, and the handoff's file name declares it. The
catalogue checker joins the two. A waiver relaxes the `[roles]` rule for that build and role. It
never admits a write the hooks refuse, and it never removes a leg from the bar.

### Data model — the registry

`<MEMORY_ROOT>/project/role-stand-in-waiver.txt`. Blank lines and lines opening `#` are ignored.
Every other line is one row of five TAB-separated fields, split at the first four TABs so the
reason may hold anything:

```
<date>	owner <who>	<role>	<build>	<reason>
```

| Field | Valid when | Borrowed from |
|---|---|---|
| date | `\d{4}-\d{2}-\d{2}` that `datetime.date.fromisoformat` accepts | the `canon_unfrozen` stamp, `tools/lexicon/adopt-lexicon.sh:456` |
| attribution | `owner ` then one token with no whitespace | the §8 mark's `owner` resolver; a row signed otherwise is not the owner's |
| role | names a role file whose `agent` is not `false` | an `agent: false` role is never spawned, so nothing stands in for it |
| build | a slug, `^[A-Za-z]+$`, the renderer's own `SLUG_RE` | the declaration carries the build |
| reason | non-empty after trimming | `memory/project/spec-token-waivers.txt:4` |

The loader reads through `lib.load_text`, so the file is UTF-8 with CRLF folded. Each invalid row
yields exactly one line, `<registry>:<line>: R15 — <what>`, naming the first field that fails, in
the table's order. A second row for a
`(build, role)` already held is a defect naming the line it repeats; the first stays valid. The
loader never raises on a row: the checker wants every line, and the renderer wants the valid rows.

How it is graded like its siblings, each property with its source:

| Property | Source |
|---|---|
| an absent file waives nothing | `memory/project/pass-order-waiver.txt:9` |
| a stale row reds | `memory/project/pass-order-waiver.txt:11`, `memory/project/brief-recorded-waiver.txt:6` |
| a row with no reason reds | `memory/project/spec-token-waivers.txt:4` |
| every row prints on every run, green included | `memory/project/location-probe-waivers.txt:10`, `.lexicon.conf:528` |
| TAB-separated, comments and blanks ignored | `memory/project/pass-order-waiver.txt:6` |

It is NOT shrink-only. A new stand-in needs a new row, so a count pin would refuse the one act the
registry exists to record. It is read from the working tree, like every other input of the
checker, and not from HEAD as `brief-recorded-waiver.txt` is.

### The declaration

`handoff.py render` gains `--stand-in`, added to the `dest` group at `tools/roles/handoff.py:422`.
Before rendering, `main` loads the waivers through S1's reader. When no valid row holds
`(--build, --role)` it refuses with exit 1, naming the registry path, the role, the build and the
row the owner writes, followed by any loader lines. The check sits inside the `try` that already
turns a `RolesError` into exit 1, before `render_handoff` runs, so a refusal writes nothing.
`derive_prompt_name` (`:227`) gains a `tail` argument, default empty, inserted before `.md`, and
`render_handoff` (`:241`) gains the same keyword and passes it through; `main` passes `-stand-in`
when the flag is set. The file is `<date>-prompt-<id>-<n>-<role without gov->-stand-in.md`, with
the sequence rule unchanged. That name matches check 5's recording grammar through its optional tail
(`REC_TAIL`, `tools/memory-tree/check-memory-hygiene.sh:495`). The marker line, both hashes and
`handoff.py check` are unchanged.

`MARKER_RE` (`handoff.py:67`) moves into `roles_lib` unchanged, and `handoff.py` binds
`MARKER_RE = lib.MARKER_RE` so `check_handoff` (`:358`) reads one pattern. The hooks kit keeps its
own JavaScript copy, `HANDOFF_MARK_RE` (`tools/hooks/agent-cap.js:2041`), untouched.

The scan globs `<MEMORY_ROOT>/builds/*/prompts/*-stand-in.md`, sorted, and reads each file whole.
A file whose text yields no `MARKER_RE` match is a defect: it declares a stand-in by its name and
names no role. Otherwise it is one declaration `{path, role, build, unit}`, all four from the
marker. A handoff without the tail is never read, so an ordinary spawn's prompt file costs nothing.

### Rule R15 in the checker

`check_roles` (`tools/roles/check_roles.py:112`) reads `MEMORY_ROOT` with `lib.read_conf_key` from
the conf `resolve_charter_path` already proved exists; blank or absent raises the R0 `RolesError`,
exit 2. After the policy block (`:268`) it loads the waivers and scans the declarations, then:

| Case | Line |
|---|---|
| a loader or scan defect | the line as returned, a defect |
| a declaration whose `(build, role)` no row holds | defect at the declaration's path: no waiver row in the registry covers this stand-in |
| a row whose `(build, role)` no declaration holds | defect at `<registry>:<line>`: stale, it covers no declaration under that build's `prompts/` |
| a valid row | `roles: note: stand-in waiver <date> owner <who> <role> <build> — <reason>` |

The summary (`:288`) gains `%d stand-in waiver(s), %d stand-in declaration(s)` before its defect
count, whatever else `TOOL-aOrientedCast-16` and `-17` do to that line. The docstring gains the
R15 line, the R0 clause, and what R15 does not check: whether the tool truly could not spawn,
whether the `owner` who signed a row is the owner, whether a reason says anything, whether the
marker's build matches its folder, an undeclared stand-in, and a declared stand-in that was in
fact spawned, which is harmless overstatement.

### Hygiene check 3

One case line, `F:role-stand-in-waiver.txt) ;;`, sits directly below `F:pass-order-waiver.txt) ;;`
(`tools/memory-tree/check-memory-hygiene.sh:738`) and above the widening `F:*)` case (`:749`). Its
comment says the roles kit's catalogue checker reads the registry at this default path, naming the
kit in prose and never by path, as the install-prefix ban requires. The self-test's admission arm
(`tools/memory-tree/check-memory-hygiene.test.sh:3197`) writes the second registry into its
fixture and fails when check 3 names either; its assertion count does not move.

### The governing doc

This unit reads no section of the governing doc. The loader, the scan and the join read the
registry, the prompts folders and the role files, so a v3.x charter with `§` headings and a v4.3
charter with tagged rules grade identically. R0 still requires `CHARTER` to name a file, as today.

### Inventory

| Identifier | Cell |
|---|---|
| `load_stand_in_waivers` | `py.function`, verb `load`, answered OK by `lexicon.py --suggest` |
| `scan_stand_in_declarations` | `py.function`, verb `scan`, answered OK by `lexicon.py --suggest` |
| `STAND_IN_WAIVER` = `"role-stand-in-waiver.txt"` | a constant, which no cell grades |
| `STAND_IN_TAIL` = `"-stand-in"` | a constant, which no cell grades |
| `MARKER_RE` in `roles_lib` | a constant, its pattern unchanged |
| `--stand-in` | a flag of `handoff.py render` |
| rule R15 | the next free number after `TOOL-aOrientedCast-17`'s R13 and R14, §8 F5 |

### Rollout — the kit versions

This is the only unit of the set that moves the memory-tree kit, and it moves it once, by one minor
step. It moves no roles kit carrier: `TOOL-aOrientedCast-20`, order 22, is the last unit of the set
to touch `tools/roles/`, and the epoch leg clears every earlier move of the kit's shipped bytes once
a later commit bumps its version, so that unit's bump dates this unit's edits too.

| Kit | Constant | Every other carrier |
|---|---|---|
| memory-tree | `KIT_MEMORY_TREE_VERSION` at `tools/memory-tree/check-memory-hygiene.sh:64`, with its same-line marker | the `gov:kit memory-tree@` marker in each of the four kit templates and their four rendered copies under `memory/` |

`tools/check-kit-versions.sh` pairs the constant with its markers (`:259`), and the epoch leg is what
reds a kit whose shipped bytes moved with no bump.

### Migration

None. An absent registry and no declaration grade exactly as today. The one new refusal is R0 on a
conf with no `MEMORY_ROOT`, where `adopt-roles.sh` already exits 2, so no working install meets it.
Rollback is a revert of the unit's commit.

### Files touched (estimate)

`tools/roles/roles_lib.py`
`tools/roles/check_roles.py`
`tools/roles/handoff.py`
`tools/roles/README.md`
`tools/memory-tree/check-memory-hygiene.sh`
`tools/memory-tree/check-memory-hygiene.test.sh`
`tools/memory-tree/HYGIENE.template.md`
`tools/memory-tree/BUILD-METHOD.template.md`
`tools/memory-tree/SPEC-TEMPLATE.template.md`
`tools/memory-tree/ANNOTATION-STYLE.template.md`
`memory/HYGIENE.md`
`memory/TEMPLATE-SPEC.md`
`memory/guides/BUILD-METHOD.md`
`memory/guides/ANNOTATION-STYLE.md`

### Alternatives rejected

- A `[[stand-in]]` table in `tools/roles/house/policy.toml`, read by `load_policy` and graded as
  R12. It is the smallest diff, since the seed, its reader and its rule exist. It was rejected
  because the brief places the registry beside the other registries under `memory/project/`, where
  an owner audits every standing exception in one folder, and because the policy file is the
  adopter's tuning file, not a record of exceptions.
- A commit trailer as the declaration, F1 (b). It needs a history scan in a leg that reads only the
  tree today, and a stand-in in a tool with no trailer habit leaves nothing.
- A field on the `gov:handoff` marker, F1 (d). Two anchored readers would change, one of them in the
  hooks kit, for a fact the file name already carries.

## 5. Production-readiness checklist

- security — No new write surface beyond one file name under a folder the renderer already writes.
  An `owner` signature is a claim the shape cannot prove; every row prints on every run and lands in
  a reviewable commit, which is the lexicon door's trade. Hooked sessions stay fail-closed.
- perf / scale — One glob over the builds' prompts folders, reading only tailed files, and one small
  registry read, inside a leg whose ceiling is 120 s.
- error / empty / loading states — An absent registry waives nothing; an invalid row is one defect
  naming its line and field; a marker-less declaration is one defect; a blank `MEMORY_ROOT` is R0.
- observability — Every row prints as a note on every run, and the summary carries both counts, so
  a zero is visible as a zero.
- risks — R15's number moves only if a fold gives a sibling another rule, by §8 F5. A forged
  `owner` row passes the shape, and is visible on every run.
- testing — Fixture probes of the loader, the scan, the checker and the renderer in the pass; the
  catalogue arm and the hygiene self-test arm observed RED-first at the close.
- migration — None, as §4 states.
- user docs — The roles README section. The help page is `PLAY-aOrientedCast-2`'s, per §3.

## 6. Acceptance criteria

The fixture is a scratch root under the run's scratch directory, made a repository with
`git init`. It holds a copy of the kit directory at tools/roles, stub files under tools/workflows
for the three harness scripts the workflow table names, a copy of `AGENTS.md`, and a
`.memory-tree.conf` declaring `MEMORY_ROOT=memory` and `CHARTER=AGENTS.md`. Its build folder,
memory/builds/tFix, holds a README whose front matter carries an `ids:` line naming one unit of
slug `tFix`, and one spec file. Its registry is `role-stand-in-waiver.txt` under memory/project.
The GOOD ROW is the five TAB-separated fields `2026-10-13`, `owner a`, `gov-builder`, `tFix` and
`this tool exposes no sub-agent primitive`. The PROBE is
`python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; w, bad = r.load_stand_in_waivers('.', 'memory', r.load_roles('tools/roles')); print(sorted(w)); print(*bad, sep=chr(10))"`,
run from the fixture root. Every staged break is restored after its observation.

- **AC1** — When the registry holds the good row and eight staged rows below it, one per line —
  four fields; the date `2026-13-01`; the attribution `agent a`; the role `gov-ghost`; the role
  `gov-session`; the build `t-Fix`; an empty reason after a fifth TAB; a second good row — the
  probe prints `[('tFix', 'gov-builder')]` and eight lines, each carrying `R15` and its own line
  number.
  Red when: any staged row is accepted, or a defect on one line takes the good row with it.
- **AC2** — When the fixture holds no registry, the probe prints `[]` and nothing else; when the
  registry holds two `#` lines, a blank line and the good row, it prints `[('tFix', 'gov-builder')]`
  and nothing else.
  Red when: an absent registry raises or yields a row, or a comment line is read as a row.
- **AC3** — When the fixture's prompts folder holds a file named with the `-stand-in.md` tail whose
  marker line names `gov-builder` and build `tFix`, a copy of it named without the tail, and a
  second tailed file carrying no `gov:handoff` line,
  `python -c "import sys; sys.path.insert(0, 'tools/roles'); import roles_lib as r; d, bad = r.scan_stand_in_declarations('.', 'memory'); print([(x['build'], x['role']) for x in d]); print(*bad, sep=chr(10))"`
  prints `[('tFix', 'gov-builder')]` and one `R15` line naming the marker-less file.
  Red when: the untailed copy counts as a declaration, or the marker-less file passes unnamed.
- **AC4** — When the fixture holds AC3's tailed declaration and no registry,
  `cd tools/roles && python check_roles.py --root ../..` exits 1 with one `R15` line naming that
  file, `gov-builder` and `tFix`, and its summary carries `0 stand-in waiver(s)` and
  `1 stand-in declaration(s)`. With the good row added it exits 0, prints one
  `roles: note: stand-in waiver` line carrying the row's five fields, and the summary carries
  `1 stand-in waiver(s)`. With the declaration then deleted it exits 1 with one `R15` line naming
  the registry line as stale.
  Red when: a declaration with no row exits 0, a row is not printed on a green run, or a row that
  covers no declaration passes.
  fixture: the exit codes assume the fixture is otherwise clean, which `TOOL-aOrientedCast-16`'s
  re-key provides on a v4.3 `AGENTS.md`.
- **AC5** — When the fixture conf's `MEMORY_ROOT` line is deleted,
  `cd tools/roles && python check_roles.py --root ../..` exits 2 naming `MEMORY_ROOT`.
  Red when: it exits 0 or 1, or grades a registry at a guessed root.
- **AC6** — When `python tools/roles/handoff.py render --role gov-builder --build tFix --input spec=<the fixture spec> --stand-in`
  runs with no registry, it exits 1 naming `role-stand-in-waiver.txt`, `gov-builder` and `tFix`,
  and the prompts folder gains no file. With the good row it exits 0 and prints a path ending
  `-builder-stand-in.md`, and `python tools/roles/handoff.py check <that path>` exits 0. With
  `--stdout` beside `--stand-in` it exits 2.
  Red when: a stand-in renders with no row, its file lacks the tail, or a stand-in can render to
  stdout, where it declares nothing.
  fixture: the render rests on `TOOL-aOrientedCast-16`'s re-key, as AC4's exit codes do.
- **AC7** — When the AC1 probe and the AC3 probe run from the worktree root, they print `[]` and
  nothing else each.
  Red when: the scan reads beyond the prompts folders, where two specs of this build carry
  `gov:handoff` lines at column 0, or the loader raises on this tree.
  figure: DERIVED at observation; gov holds no registry and no declaration at `d518b483f`.
- **AC8** — When `grep -n -e "F:pass-order-waiver.txt) ;;" -e "F:role-stand-in-waiver.txt) ;;" -e "^  F:\*)" tools/memory-tree/check-memory-hygiene.sh`
  runs, it prints three lines in that order: the new case sits below the pass-order case and above
  the widening case.
  Red when: the new case is absent, or sits below `F:*)`, which answers first and refuses any name
  `PROJECT_REGISTRY_EXTRA` does not list.
- **AC9** — When `grep -c '^KIT_MEMORY_TREE_VERSION=2.147' tools/memory-tree/check-memory-hygiene.sh`
  runs, it prints 1; `grep -rl "gov:kit memory-tree@2.146" tools/memory-tree memory/HYGIENE.md memory/TEMPLATE-SPEC.md memory/guides`
  prints nothing; and on the unit's commit
  `git diff HEAD~1 HEAD -- tools/roles/roles_lib.py tools/roles/SKILL.template.md .claude/skills/build | grep -c "KIT_ROLES_VERSION\|gov:kit roles@"`
  prints 0.
  Red when: the memory-tree constant does not move, one of its carriers keeps the old marker, or
  this unit moves a roles kit carrier, which `TOOL-aOrientedCast-20` moves once for the set.
  figure: PINNED at `d518b483f`, where memory-tree reads 2.146; a bump another build lands first
  moves the expected value by the same one step.

## 7. Gates

The close's bar grades this unit with these legs; no pass runs one.

`roles catalogue` · `roles render wiring` · `roles render selftest` · `memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `verdict epoch (kit version dates the engine)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `install-prefix (shipped surface)` · `spec tokens (a spec's own names resolve)` · `govkit selfcheck`

New arm: tools/roles/check_roles.py · covers AC4 AC5 · a tailed stand-in handoff with no waiver row staged into a prompts folder of the tree, then a waiver row with no declaration · none
New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC8 · the rf10 fixture holds the stand-in registry, against the new case staged below the widening case so check 3 names it · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).

## 8. Open questions

- **F1 — How does a stand-in declare itself, so the grader has something to join?**
  Options: (a) `handoff.py render --stand-in` writes the handoff with a `-stand-in` tail, and the
  scan reads build and role from its marker; (b) a `Stand-in: <role>` commit trailer on the pass
  commit, joined by a history scan; (c) a second row kind in the registry, written by the run;
  (d) a new field on the `gov:handoff` marker line.
  (b) puts a history walk into a leg that reads only the tree, and records nothing in a tool that
  writes no trailer. (c) lets one file hold both the owner's grant and the run's claim, so the
  owner cannot tell them apart. (d) changes a pinned interface read by two anchored patterns, one in
  the hooks kit, widening the write set past this unit. (a) reuses the renderer the stand-in must
  run anyway to receive its role, and its output is a tracked record under the build.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), by M3. Every option survives the vetoes; (a) leaves
  the fewest follow-ups, since (b) and (c) leave a tool without trailers or an owner reading two
  kinds of row, and it wins the tie-break against (d) by reusing the renderer seam M5 found.
- **F2 — What does one waiver row grant?**
  Options: (a) one role in one build; (b) one role in every build; (c) one role for one unit.
  (b) is a standing global waiver, the shape the unattended protocol's §10 rejects for directives
  because it carries no run. (c) asks a row per unit for an inability that belongs to the tool, not
  the unit. (a) matches §10's "for that run only", and the declaration's marker carries the build.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a). It survives every veto and leaves no follow-up.
- **F3 — Is a row that no declaration consumes a defect?**
  Options: (a) yes, stale, as the pass-order and brief-recorded registries red a stale row; (b) a
  note only, so an owner may grant ahead of the work.
  (a) costs a red catalogue leg between a row's commit and its first declaration, a window the
  close's bar never sees because it runs after the last unit. (b) lets a waiver outlive its reason
  silently, which is the defect the sibling registries were written against.
  Recommendation: (a), the owner's "graded like the other waiver registries".
  RESOLVED (agent, 2026-10-13, delegated): (a). It satisfies AC4's stale clause.
- **F4 — How does hygiene check 3 admit the registry?**
  Options: (a) by name, in check 3's case block beside `pass-order-waiver.txt`; (b) through each
  repository's own `PROJECT_REGISTRY_EXTRA`.
  (b) leaves every adopter a check-3 red on its first waiver row, cured by a conf edit it must learn
  of. (a) follows the memory-tree README's rule that a registry a kit reads at its default path is
  admitted by name. The memory-tree bump it costs moves only `gov:kit` marker comments in four
  carriers, which change no rule, so veto 2 does not apply.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a). It is the more feature-rich survivor.
- **F5 — Which rule number does the checker's new rule take?**
  `TOOL-aOrientedCast-16` and `-17` are specced concurrently and both edit `check_roles.py` first.
  Read before this spec closed: `TOOL-aOrientedCast-17`'s spec takes R13 and R14, the next free
  numbers after R12 (`check_roles.py:30`), and `TOOL-aOrientedCast-16`'s §3 mints no new number.
  Options: (a) R13, the next number on this tree; (b) the next number after `-17`'s two; (c) a
  separate letter family.
  (a) collides with `-17`'s R13. (c) splits a namespace the docstring lists as one sequence.
  Recommendation: (b), R15.
  RESOLVED (agent, 2026-10-13, delegated): (b), R15. Should a fold give either sibling another
  number, this rule takes the next free number after theirs, and every R15 here reads as that.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.
- rev-2 · 2026-10-13 · S7 · AC9 · §3 · §4 · the roles kit's version move goes to
  `TOOL-aOrientedCast-20`, now the last unit of the set to touch `tools/roles/`. S7, AC9 and §4
  "Rollout" keep the memory-tree move alone, §3 says why, and the Skill template and the rendered
  `/build` Skill leave §4's files touched, because the `gov:kit roles@` marker was this unit's only
  edit to either. The brief asked for `check-wiring self-test` on the §7 leg line, since the rendered
  Skill's path tripped that leg's `.claude/` guard. With the path gone the guard no longer trips, so
  the leg is not added. Re-derived with the spec-token checker's guard join read from its source,
  not run: every leg the remaining paths trip is already on the leg line.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "owner waiver registry row dated attributed reasoned graded both directions stale row reds"`
ranked name-token neighbours, `rows`, `row` and `extract_row`, none of which reads a waiver
registry, so no existing seam fits as a mapped function. A second probe,
`"render a role handoff prompt file under the build prompts folder"`, ranked `RolesError` in
`tools/roles/roles_lib.py` and the render family. The seams extended, read against source at
`d518b483f`: `check_roles` and its summary in `tools/roles/check_roles.py`, the library's reader
pattern of `load_policy` in `tools/roles/roles_lib.py`, `derive_prompt_name` and the `dest` group in
`tools/roles/handoff.py`, and check 3's kit-registry case in
`tools/memory-tree/check-memory-hygiene.sh`. The row shape reuses the lexicon kit's dated,
attributed and reasoned stamp, and the grading reuses the sibling registries' rules, each cited in
§4. The recall probe surfaced this build's brief rows and the aHalvedInstall run record's ruling
that a waiver registry is a standing exception the owner grants; nothing stale was found.

Recall terms used: `waiver registry stale row owner reason dated attributed stand-in role spawn inline handoff`
