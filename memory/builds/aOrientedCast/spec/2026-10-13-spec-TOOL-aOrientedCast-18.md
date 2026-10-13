# TOOL-aOrientedCast-18 — the role roster, derived into the charter by the roles kit's own verb

**Status:** CLOSED · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams tooling · order 18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md](../build/2026-10-13-build-KICK-aOrientedCast-1-agent-ledger.md) | journal | KICK-aOrientedCast-1 KICK-aOrientedCast-2 PLAY-aOrientedCast-1 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 TOOL-aOrientedCast-1 TOOL-aOrientedCast-2 TOOL-aOrientedCast-3 TOOL-aOrientedCast-4 TOOL-aOrientedCast-5 TOOL-aOrientedCast-6 TOOL-aOrientedCast-7 TOOL-aOrientedCast-8 TOOL-aOrientedCast-9 TOOL-aOrientedCast-10 TOOL-aOrientedCast-11 TOOL-aOrientedCast-12 TOOL-aOrientedCast-13 TOOL-aOrientedCast-14 TOOL-aOrientedCast-15 TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 TOOL-aOrientedCast-23 |
| [2026-10-13-build-TOOL-aOrientedCast-18-1-acceptance-ledger.md](../build/2026-10-13-build-TOOL-aOrientedCast-18-1-acceptance-ledger.md) | journal | — |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-1-spec-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2 |
| [2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-16-2-build-brief.md) | journal | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-19 PLAY-aOrientedCast-2 |
| [2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md](../reviews/2026-10-13-review-TOOL-aOrientedCast-16-closing-diff-round1.md) | diff-review | TOOL-aOrientedCast-16 TOOL-aOrientedCast-17 TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 TOOL-aOrientedCast-22 PLAY-aOrientedCast-2 PLAY-aOrientedCast-3 |

<!-- /gen:spec-records -->

## 1. Goal

The charter's new Agent roles subsection needs one line per role, and the roles kit must stay the
one reader of role files. This unit gives the playbook renderer a derived `{{ROLE_ROSTER}}`
placeholder whose probe asks the roles kit's `roster` verb for those lines and substitutes them
verbatim. The probe reaches the roles kit through the sibling resolver, so the playbook kit names no
sibling kit by literal.

## 2. Scope (IN)

- **S1** — `tools/playbook/render_playbook.py` gains `derive_role_roster`, beside
  `derive_node_table`, and the `PROBES` table (`:530-542`) gains the entry
  `'role_roster': derive_role_roster`. The probe resolves the roles kit with `resolve_kit_dir` and
  runs its `roster` verb as §4 "The probe" states. It spells no kit path. Observed by AC1, AC2 and
  AC8.
- **S2** — The probe's miss path: when the kit does not resolve, the verb cannot start, the verb
  exits non-zero, or it exits 0 printing nothing, the probe prints one `render-playbook: ROLE_ROSTER:` line to stderr naming the
  cause and returns the empty string. An answer then outranks it, and an unanswered miss refuses at
  `resolve_placeholder_raw` (`:845-848`). Observed by AC3 and AC4.
- **S3** — `tools/govkit/entries/playbook.kit.toml` gains one `[[placeholder]]` row after
  `NODE_TABLE`'s: `key = "ROLE_ROSTER"`, `class = "derived"`, `probe = "role_roster"`,
  `kit = "roles"`, and a `why`. Observed by AC1 and AC5.
- **S4** — `run_selftest` in `tools/playbook/render_playbook.py` gains the four arms §7 declares,
  over the fixture §4 "The fixture" describes. Its arms re-observe AC2, AC3 and AC4 at the close.
- **S5** — `tools/playbook/README.md` gains a short "The role roster" section after "Nodes".
  NOT OBSERVED by a criterion: prose, read by the review against §4.
- **S6** — `memory/map/features/playbook.md` gains one bullet under "Constraints & why" naming the
  probe and the sibling it reaches. `memory/map/generated/symbols.json` is regenerated with
  `python tools/codebase-map/gen_map.py --write` in the same commit. Observed by AC7.
- **S7** — The playbook-render kit moves once: `KIT_PLAYBOOK_RENDER_VERSION` and its same-line
  `gov:kit playbook-render@` marker (`render_playbook.py:1728`) go from `1.27` to `1.28`.
  Observed by AC6.

## 3. Non-goals (OUT)

- No template edit, no re-render of `AGENTS.md` and no `help/roles.md`. Placing the token in the
  charter is `PLAY-aOrientedCast-2`'s.
- No `roster` verb and no role front-matter field. Both are `TOOL-aOrientedCast-17`'s.
- No formatting in the probe: it adds no `- `, truncates nothing and reorders nothing. The line
  shape and the 200-character cap belong to the verb, and the one-line region grades the result.
- No reader for the `kit` key on a `[[placeholder]]` row. No code reads it today, and the
  template's fence is what makes a token reachable (§4).
- No edit to `tools/hooks/README.md`. Its authoring rule already states the ban and the engine
  route this probe follows (`tools/hooks/README.md:450`, `:457-458`).
- No govkit render token for a sibling kit. `TOOL-aCollapsedScan-11` asks for one, and it stays
  that ask's.
- No change to any other probe, and no roles-kit version bump: this unit writes no file of that kit.

### Edges

- **consumes-from** `TOOL-aOrientedCast-17` — the roles kit's `roster` verb on `handoff.py`, run
  with no further argument, printing one `- ` bullet per role and exiting non-zero with its reason
  on stderr. Without it the probe refuses and AC1 cannot be observed.
- **hands-off** `PLAY-aOrientedCast-2` — putting `{{ROLE_ROSTER}}` into the template's Agent roles
  subsection, inside the roles fence and a one-line region, and re-rendering the charter. Until then
  no charter carries the roster.

## 4. Design

Line numbers below were read at `d518b483`.

### The probe

A sketch of the shape, not of the final text:

```python
def derive_role_roster(root: Path, _a: dict, _e: Path | None = None) -> str:
    here = _e or Path(__file__).resolve().parent
    top = root.resolve()
    home, anchor = 'roles', 'handoff.py'
    env = {k: v for k, v in os.environ.items() if not k.startswith('GIT_')}
    try:
        kit = resolve_kit_dir(home, anchor, here if top in here.parents else top)
        r = subprocess.run([sys.executable, str(kit / anchor), 'roster'], cwd=str(top), env=env,
                           capture_output=True, text=True, encoding='utf-8', errors='replace',
                           timeout=30)
    except LookupError as e:
        why = str(e)
    except (OSError, subprocess.SubprocessError) as e:
        why = f'the roster verb did not run: {e}'
    else:
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout.strip()
        said = (r.stderr.strip().splitlines() or ['it printed no line'])[0][:240]
        why = f'the roster verb exited {r.returncode}: {said}'
    print(f'render-playbook: ROLE_ROSTER: {why}', file=sys.stderr)
    return ''
```

- The engine directory is taken as `derive_node_table` takes it (`render_playbook.py:427`).
- The resolver call and the `home, anchor` pair copy `derive_gate_runner` (`:285`, `:298`). The
  search starts at the engine when it sits inside the target, and at the target's root otherwise. A
  `LookupError` message names the three places the resolver looked.
- The environment is the one `read_git` builds (`:143`), for its reason: a hook reached through a
  `.git` file exports `GIT_DIR`.
- Running a sibling kit's script with `sys.executable` is the shape of
  `tools/drift-audit/drift_report.py:3425-3430`, and the 240-character cap on a quoted stderr line
  is its `:3444`.
- Text mode folds a Windows verb's carriage returns, so the lines arrive joined by newlines.

An exit 0 with an empty stdout is a miss too, because a roster of no role is a dead probe and
not a value. The miss causes share one exit: one `render-playbook: ROLE_ROSTER: <why>` line on stderr and
the empty string returned, the shape `derive_default_branch` uses for its own refusal
(`:245-248`). Why it does not raise: §8 F2.

The value then passes through code this unit does not touch. `resolve_placeholder_value` refuses a
value carrying a one-line marker (`:820-822`). `check_one_line_regions` grades every line after
substitution: a `- ` bullet of at most `ONE_LINE_MAX` characters (`:126`, `:654-659`). The render
prints `derived   ROLE_ROSTER = <value>` as a note, as it prints `NODE_TABLE`'s.

### What it consumes from the roles kit

The verb is `handoff.py roster` (§8 F1), invoked with no argument and the target's root as its
working directory. The probe relies on four properties of it, which `TOOL-aOrientedCast-17` owns:

| Property | Why the probe needs it |
|---|---|
| Exit 0, one line per role on stdout | the value is substituted verbatim |
| Each line opens `- ` and is at most 200 characters | the one-line region admits nothing else |
| A refusal exits non-zero with its reason on stderr | the miss path quotes that reason |
| It reads role files only, never the charter | the render order is charter first, agents second |

The last row is the owner's render order (the addendum's "What gets built", item 4): the roster
needs only role files, and an agent type needs the rendered charter, so the charter render cannot
wait on an agent render.

### Where the token is reachable, and an older charter

`render` prunes the `kit:` fences a target did not select (`:985-987`), then resolves only the
tokens the pruned text still holds (`:995-1010`). A probe therefore runs only for a token that
survived. `PLAY-aOrientedCast-2` puts the token inside the roles fence, so the probe runs exactly
when `roles` is in the target's `kits`.

The `kit = "roles"` key records that fact for a reader, as `LEXICON_CONF` and `TOOLCHAIN_NOTES`
record theirs (`tools/govkit/entries/playbook.kit.toml:125`, `:238`). A grep for a reader of that
key on a placeholder row finds none in `tools/playbook/` or `tools/govkit/`: the one `kit` read in
the renderer, `render_playbook.py:919`, is deploy.toml's per-entry table.

An adopter's template is a seed `govkit update` never rewrites (the comment at
`playbook.kit.toml:134-138`). A v3.x template, and a v4.0 to v4.3 one, carries no
`{{ROLE_ROSTER}}`. Under one, the probe never runs, no subprocess starts and the region renders
byte-identically to today's. Nothing is noted for the missing roster, because a seeded template
already gets the render's reseed note when its major is behind (`:990-993`). The probe does not
read the charter at all, so the absence of tagged rules in a v3.x charter does not reach it.

`--answers ROLE_ROSTER` (`:1648-1654`) resolves the row through `resolve_answers`, which calls the
probe whatever the fences say (`:923-926`). That is the existing contract for every derived row,
and it is what AC1 uses to observe the probe on gov's own tree before any template carries the
token.

### The descriptor row

After the `NODE_TABLE` row of `tools/govkit/entries/playbook.kit.toml` (`:128-132`), before the
LEGACY comment:

```toml
[[placeholder]]
key = "ROLE_ROSTER"
class = "derived"
probe = "role_roster"
kit = "roles"
why = "section 3's Agent roles subsection: one `- ` line per role, printed by the roles kit's own `roster` verb so that kit stays the one reader of role files; only reachable when the roles block survives (TOOL-aOrientedCast-18)"
```

### The README section

`tools/playbook/README.md` gains "## The role roster" after "Nodes", in four or five sentences:
`{{ROLE_ROSTER}}` is filled by the roles kit's `roster` verb, found through the sibling resolver,
so this kit names no sibling kit by literal; the lines arrive verbatim and the one-line region
grades them; a missing kit or a failing verb prints its cause and refuses unless answered; and a
role edit stales the region, which `--check` reports.

### Freshness

The `playbook render wiring` leg has no guard (`tools/gate-legs.json`), so it runs on every bar and
compares the charter region with a fresh render. Once `PLAY-aOrientedCast-2` places the token, a
role edit that changes the roster stales the region and that leg reds until a re-render. That is the
owner's "a role edit stales the charter", and this unit adds nothing for it.

### The fixture

Shared by AC2 to AC4 and the four arms. All of it is written into a scratch directory `td` by the
probe or the arm itself.

| Path under `td` | Content |
|---|---|
| `engine` / `playbook.kit.toml` | the one `ROLE_ROSTER` row S3 adds |
| `engine` / `registry.toml` | entries `roles` and `lexicon`, one `[[entry]]` per id |
| `target` / `CHARTER.md` | a v4.4 marker, then a one-line region holding the token inside the roles fence; or, for the older-charter case, a `v3.5` marker and no token |
| `target` / `.governance` / `deploy.toml` | `kits` holding `roles` or only `lexicon`; `[answers] playbook_path = "CHARTER.md"`, and `role_roster = "- answered"` in the answered case |
| `home` / `anchor` | the stub verb, absent in the absent-kit case |

The stub writes a sentinel file `ran` beside itself, then either prints two `- ` bullets and exits
0 or prints a reason to stderr and exits 1. `home` and `anchor` are variables holding `'roles'` and
`'handoff.py'`, joined at run time and never as one literal. That is the spelling the install-prefix
gate cannot see and its README names for a fixture (`tools/hooks/README.md:471-473`), and the one the
run-gates arm of this selftest already uses (`render_playbook.py:1568-1574`). The engine directory
is `td/engine` and the target `td/target`, so the probe searches from the target's root and finds
the stub through the resolver's second probe, one level up.

The sentinel is what keeps the unreached case from passing by finding nothing: the kept-fence case
asserts it EXISTS, so the same stub is proved live before its absence means anything.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `derive_role_roster` | function, module level | `py.function`, snake, leads with `derive` |
| `write_roster_fixture` | function nested in `run_selftest` | `py.function`, snake, leads with `write` |
| `role_roster` | `PROBES` key and `probe` value | not graded |
| `ROLE_ROSTER` | placeholder key | not graded |

`python tools/lexicon/lexicon.py --suggest <name> --as py.function` answered OK for both
functions on this tree.

### Rollout

The playbook-render kit's shipped set is `tools/playbook/` plus the descriptor
`playbook.kit.toml`, which the kit ships root-relative (`tools/playbook/kit.toml:30-34`). This
unit is the only one in the brief's table that writes either, so it carries that kit's one bump,
S7, in its own commit. The kit's only version carrier is `render_playbook.py:1728`, the constant
and its marker on one line: `tools/check-kit-versions.sh` lists no row for playbook-render, and
`tools/playbook/kit.toml:11` reads `version_from` from that line. At landing,
`govkit.py mint` (`tools/govkit/govkit.py:13110`) reads the entry as `clean` if no later commit
moves it, and mints the next value itself if one does.

No migration. Gov's own `AGENTS.md` does not move in this unit, because gov's template carries no
token until `PLAY-aOrientedCast-2`.

### Files touched (estimate)

`tools/playbook/render_playbook.py`
`tools/govkit/entries/playbook.kit.toml`
`tools/playbook/README.md`
`memory/map/features/playbook.md`
`memory/map/generated/symbols.json`

### Alternatives rejected

- The probe reads role front matter itself, by importing `roles_lib` or parsing role files. That
  makes a second reader of role files, which the owner's design rules out, and an import across kits
  is the edge this engine's header refuses for the region helper (`render_playbook.py:62-65`).
- The probe adds the `- ` and cuts at 200 characters. Two formatters of one line would drift, and
  the cap would be enforced in two kits.
- A literal path to the verb. The install-prefix gate counts a kit segment followed by a file under
  any lead (`tools/check-install-prefix.sh:44-55`), and an adopter installed at another prefix
  would resolve it to nothing.
- A govkit token naming a sibling kit's directory. An engine is copied verbatim and never rendered
  (`tools/hooks/README.md:457`), so the token would need a new govkit value class: M3 veto 2.

## 5. Production-readiness checklist

- security — One subprocess of a kit-shipped script with a fixed argv, no shell, no operator value
  in the argv, a `GIT_*`-free environment and a 30-second timeout. Its output lands in the charter,
  where a one-line marker is refused and a surviving `{{` fails `--check`. A `gov:playbook` marker in
  the output is not graded at the probe; the role files are kit-authored, and the next render
  refuses a second region (`render_playbook.py:689-691`).
- perf / scale — One Python start per render, and only when the token survived the fences. The
  verb reads one file per role.
- error / empty / loading states — No kit, no verb, a failing verb and an empty stdout each end in
  the refusal at `:845-848` after a stderr line naming the cause, unless an answer is supplied.
- observability — The `derived ROLE_ROSTER` note on every render, and the stderr cause line on a
  miss.
- risks — A role edit stales every charter carrying the roster, by design. An adopter who answers
  `role_roster` pins a roster that no longer follows its role files; the note line shows the answer
  beside `probe would derive …`, as for every derived row.
- testing — Four selftest arms, observed RED-first at the close; the direct probes of §6 in the
  pass, AC1 on gov's own tree.
- migration — None, as §4 "Rollout" states. Older seeded templates render byte-identically.
- user docs — The playbook README's new section. `help/roles.md` is `PLAY-aOrientedCast-2`'s.

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each calls the unit's own code or
reads its output. The suite arms are under `New arm:` in §7.

- **AC1** — When `python tools/playbook/render_playbook.py --target . --answers ROLE_ROSTER` runs
  in gov, it exits 0, and the `ROLE_ROSTER` value of its JSON equals, line for line, the stripped
  stdout of `python tools/roles/handoff.py roster`.
  Red when: the probe adds, cuts or reorders a line, or `PROBES` lacks the key and the call exits 1
  naming the probe.
  fixture: gov's own tree after `TOOL-aOrientedCast-17` is built, which order 17 puts first.
  figure: the line count is DERIVED from the verb's output at observation time.
- **AC2** — When a `python -c` probe adds `tools/playbook` to `sys.path`, imports
  `render_playbook` and calls `render` over §4's fixture with `roles` selected, the body holds both
  stub bullets verbatim inside the one-line region and the stub's `ran` sentinel exists. With only
  `lexicon` selected, and again with `roles` selected under the `v3.5` template that carries no
  token, the render returns, its body holds neither bullet, and no sentinel exists.
  Red when: the probe runs for a token that did not survive the fences, or a bullet arrives altered.
- **AC3** — When the same probe's stub exits 1 with a reason, `render` raises `Refusal` naming
  `ROLE_ROSTER` and `role_roster`, and the captured stderr holds a `render-playbook: ROLE_ROSTER:`
  line quoting the stub's reason. With `role_roster = "- answered"` under `[answers]`, the render
  returns a body holding `- answered` and a note ending `(probe derives nothing)`.
  Red when: the probe raises, so no answer can outrank it; or it substitutes a failed verb's
  stdout; or the cause is never printed.
- **AC4** — When the fixture holds no stub, the captured stderr holds a
  `render-playbook: ROLE_ROSTER:` line carrying the resolver's `looked in` list, and `render`
  raises `Refusal` naming `ROLE_ROSTER`.
  Red when: the probe guesses a path, returns a value, or swallows the resolver's reason.
- **AC5** — When a `python -c` probe loads `tools/govkit/entries/playbook.kit.toml` with
  `tomllib`, exactly one `[[placeholder]]` row has `key = "ROLE_ROSTER"`, and it holds
  `class = "derived"`, `probe = "role_roster"` and `kit = "roles"`. In the same probe,
  `render_playbook.PROBES["role_roster"]` is `render_playbook.derive_role_roster`.
  Red when: the row is absent or doubled, or names another probe or kit.
- **AC6** — When `grep -n KIT_PLAYBOOK_RENDER_VERSION tools/playbook/render_playbook.py` runs, its
  one line holds `"1.28"` and `playbook-render@1.28`.
  Red when: either spelling still reads `1.27`, or the two disagree.
- **AC7** — When `git grep -n derive_role_roster -- memory/map/generated/symbols.json` runs, it
  prints the symbol's `id` line.
  Red when: the generated map was not rewritten in the unit's commit.
- **AC8** — When `git grep -nE "roles/|'roles' */|/ *'roles'" -- tools/playbook` runs, and again
  with `tools/govkit/entries/playbook.kit.toml` as its pathspec, each prints nothing.
  Red when: the probe, its fixture, a comment or the README spells the roles kit as a path segment.

## 7. Gates

`playbook render selftest` · `playbook render wiring` · `govkit acceptance matrix` · `govkit selftest` · `govkit refusal join` · `govkit selfcheck` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `install-prefix (shipped surface)` · `foreign-prefix parity (every self-test at three prefixes)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/render_playbook.py · covers AC2 · the kept-fence arm, against `derive_role_roster` staged to return its stdout without the first line · none
New arm: tools/playbook/render_playbook.py · covers AC2 · the unreached arm, a pruned fence and a token-less v3.5 template, against `render` staged to resolve every declared derived row before its token loop · none
New arm: tools/playbook/render_playbook.py · covers AC3 · the failing-verb arm with its answered case, against `derive_role_roster` staged to raise `Refusal` on a non-zero exit · none
New arm: tools/playbook/render_playbook.py · covers AC4 · the absent-kit arm, against `derive_role_roster` staged to swallow the resolver's `LookupError` without its stderr line · none

The main loop observes each arm RED on its staged break and GREEN once restored, at the close (M8).
No pass runs a leg above.

## 8. Open questions

- **F1 — Which roles-kit script carries the `roster` verb, and so names the anchor the probe
  resolves?**
  Options: (a) `handoff.py`, the kit's verb CLI, whose `harness-args` and `stage-efforts` verbs
  already answer without reading the charter (`tools/roles/handoff.py:414-439`); (b)
  `check_roles.py`, a flag CLI that is a gate leg's argv and has no verbs (`:295-306`); (c)
  `render_agents.py`, whose modes write agent types (`:472-488`).
  (b) would make the playbook render invoke a gate leg's script with a mode no leg runs, and (c)
  needs the rendered charter, the reverse of the owner's render order. The brief calls a
  subcommand of `handoff.py` a verb and nothing else in the kit by that word.
  Recommendation: (a). `TOOL-aOrientedCast-17` owns the verb, so if its spec names another script,
  M2's interface cross-read corrects THIS spec with a rev bump.
  RESOLVED (agent, 2026-10-13, delegated): (a), as §4 "What it consumes" states it.
- **F2 — On a miss, does the probe raise a refusal or return the empty string?**
  Options: (a) raise `Refusal` naming the cause, as `derive_node_table` does (`:447-449`); (b)
  print the cause to stderr and return the empty string, as `derive_default_branch` does
  (`:245-248`).
  Under (a), `resolve_placeholder_raw` calls the probe before it consults an answer (`:837-844`), so
  an answer could never outrank a failing roster. That breaks the engine's stated contract, "AN
  EXPLICIT ANSWER OUTRANKS THE PROBE" (`render_playbook.py:12-18`). Under (b) the answer wins, an
  unanswered miss still refuses naming the key, and the cause is printed above it.
  Recommendation: (b), which keeps every criterion and the engine's contract.
  RESOLVED (agent, 2026-10-13, delegated): (b), as S2 and §4 "The probe" state it.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

The `tools/codebase-map/reuse_lookup.py` probe, run with the phrase "derive a charter placeholder
value by running a sibling kit's command", ranked `resolve_kit_dir` as a SEAM whose installs
include `tools/playbook/render_playbook.py`.
That is the seam this unit extends: the inlined canonical copy at
`render_playbook.py:78-112`, called as `derive_gate_runner` calls it (`:285`). The probe joins the
`PROBES` table (`:530-542`) beside `derive_node_table`, the nearest derived example, and takes its
environment from `read_git` (`:143`). Running a sibling kit's Python script with `sys.executable`
reuses the shape of `read_stale_dossiers` in `tools/drift-audit/drift_report.py:3420-3434`. Nothing
new is minted beside the probe and its nested fixture writer. The recall probe surfaced
`TOOL-aRepatriatedFork-46`, whose answer to "how should a kit reach a sibling kit's file without a
literal kit segment" was `resolve_kit_dir`, and backlog row `TOOL-aCollapsedScan-11`, which asks for
a govkit sibling token and is left to that ask. Both were read against source; neither disagreed with
it.

Recall terms used: `derived placeholder probe PROBES render_playbook resolve_kit_dir sibling kit literal install-prefix NODE_TABLE one-line region roster`
