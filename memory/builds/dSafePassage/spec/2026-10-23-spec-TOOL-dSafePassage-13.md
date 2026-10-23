# TOOL-dSafePassage-13 — the docs leg: each user-facing member's declared usage fingerprinted against its help page, under help.enforce

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 5 · advances TOOL-dSafePassage-14

**Carries:** cl-dClosedLoop-0030@274077d4 whole
**Carries:** node:policy-key.help.enforce

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-13-deviation-51.md](../build/2026-10-23-build-TOOL-dSafePassage-13-deviation-51.md) | deviation | — |
| [2026-10-23-build-TOOL-dSafePassage-13-deviation-52.md](../build/2026-10-23-build-TOOL-dSafePassage-13-deviation-52.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-deviation-after-fix.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-7 TOOL-dSafePassage-11 |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-6 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

From this build on, a landing that moves a user-facing surface's declared usage with no change to its
page under `help/` is refused, as `help.enforce` says. Today help is gated only at the chain's last
build, every earlier build ships surfaces under a prose rule that 6 of 216 product commits followed,
and nothing reads `help/` (`gap-found-35`, closed by this unit). The mechanism is the research's C5,
the one candidate that survived its losing test (`research-final-help.md`, section 5): each member's
usage is a declared row, its fingerprint is written into the page that documents it, the commands a
page shows are tested against those rows, and the page's links are checked offline. It is the
owner's FQ-5, "At dSafePassage (Recommended)", and P42's "its usage is fingerprinted and gated from
dSafePassage on".

## 2. Scope (IN)

- **S1** — The usage declaration, `tools/govkit/usage.toml`. One `[[class]]` row per class of
  TOOL-dSafePassage-10's class registry (`tools/govkit/surface-classes.toml`), naming the class's
  usage shape (`verb`, `key`, `hook`, `leg`, `page` or `none`), where its rows come from, and a
  `why`. One `[[usage]]` row per member or page-shown script whose own registry states no usage.
  Observed by AC6 and AC7.
- **S2** — The four row shapes the clause names, and one source each. A `verb` row is a verb and
  its flags; a `key` row a key with its values and default; a `hook` row a hook's event and matcher;
  a `leg` row a leg's name and argv. A member whose own registry already states its usage is read
  from there and never restated: a hook from its `*.fragment.json`, a policy key from the catalogue
  `cl-dClosedLoop-0007` defines, a CLI verb from the usage text TOOL-dSafePassage-10's verb class
  reads, a leg from `tools/gate-legs.json`. A `[[usage]]` row restating one of those is a finding.
  Observed by AC6.
- **S3** — The fingerprint and the page binding. A row's fingerprint is the first eight hex of the
  SHA-256 of its shape fields as canonical JSON. A page documents a member with the anchor
  `<!-- usage: <id> <fp8> -->`, and a `page`-shaped member with `<!-- usage: <id> -->`. Each member
  with a usage shape is anchored on exactly one page or listed in S6's list; an anchor whose
  fingerprint differs from its row's is a stale page; an anchor naming no member or row is an
  orphan. Observed by AC1 and AC5.
- **S4** — Each command a page shows, tested against its declared row (deviation-52). A command is a
  line of a fenced `bash`, `sh` or `console` block, or an inline code span opening with `python`,
  `python3` or `bash`. Its entrypoint resolved to a tracked path is looked up among the `verb` rows;
  its verb must be a declared verb and every `--flag` a declared flag of that verb, a value-taking
  flag consuming the token after it. A command whose entrypoint is a tracked file with no row is a
  finding unless that script is on S6's list. A command naming no tracked entrypoint, `git` or
  `sort` say, is counted and not tested. Observed by AC2 and AC3.
- **S5** — The offline link check over every page under `help/`, outside fenced blocks: a relative
  link resolves to a tracked path, and a `#fragment` resolves to a heading slug or an explicit
  anchor in its target page. An `http` or `https` link is counted and never fetched. Observed by AC4.
- **S6** — The shrink-only list of today's undocumented members, `memory/project/docs-undocumented.txt`,
  one `<id>\t<reason>` row each. A row naming a member now anchored is a finding, so the commit that
  documents a member shortens the list by its row; an undocumented member with no row is a finding;
  and the list's row count above its low-water mark on the first-parent history is a finding,
  read by drift-audit's `derive_low_waters` (`tools/drift-audit/drift_report.py:781`). The list joins
  drift-audit's `SHRINK_ONLY` table (`tools/drift-audit/drift_signals.py:129`). Observed by AC5.
- **S7** — `help.enforce`, owned here. Its catalogue row under `cl-dClosedLoop-0007` carries the
  values `refuse`, `warn` and `off`, the default `refuse`, a summary and a usage, from v2's
  `[policies]` row (v2:1294). It is read through the reader `cl-dClosedLoop-0008` lands. Under
  `refuse` any finding exits 1; under `warn` each finding prints as a `WARN` line and the leg exits 0;
  under `off` the leg prints one line, reads nothing else, and exits 0. Observed by AC8.
- **S8** — The states that are not a verdict, each exit 2 with its reason: a class whose usage shape
  is set and whose population is empty; pages that show commands of which none was tested; an
  unreadable `usage.toml` or class registry. A class of the registry with no `[[class]]` row here,
  or a `[[class]]` row naming no registered class, is a finding, which is how a later class's join
  is armed. Observed by AC7.
- **S9** — The module `tools/govkit/docs_leg.py`: the leg with no arguments, `--list`, and
  `--fixture --plant <case> [--enforce <value>]`, `--enforce` honoured under `--fixture` only.
  Observed by AC1 and AC3 to AC8.
- **S10** — The leg row `docs` in `tools/gate-legs.json` and the rows a new leg owes its meta-gates:
  an `[[exempt_leg]]` row in `tools/govkit/registry.toml`, a row in `tools/govkit/subject-pins.tsv`,
  a row in `tools/run-gates/ceiling-evidence.txt` written by `derive-ceilings.py --write` from the
  measured run, and the name in the `gate-legs` list of `memory/map/features/govkit.md`. Observed by
  AC10.
- **S11** — The real pages anchored. Every member and page-shown script the pages under `help/`
  document at this pass gets its row and its anchor, among them the `handoff.py` verbs
  `help/roles.md` shows, the `measure_legs.py` and `derive-ceilings.py` commands
  `help/measure-legs.md` shows, and the pages this build's earlier units land:
  `help/step-gate.md`, `help/upgrade-steps.md`, `help/shims.md`, `help/update-edits.md` and
  `help/python-floor.md`, the last anchoring the `platforms.provision` usage row and the
  `install.*` keys anchored on theirs. Every other member is a row of S6's list, seeded from
  `--list`. Observed by AC2 and AC5.
- **S12** — The docs: a page `help/docs-leg.md` saying what the leg reds, how to answer a stale page,
  what `help.enforce` does and how a later class joins, anchoring `help.enforce` and the leg's own
  verbs, and its line in `help/README.md`. Observed by AC9.
- **S13** — The two deviation records this spec owes, deviation-51 and deviation-52, beside it under
  `memory/builds/dSafePassage/build/`. Observed by AC11.

## 3. Non-goals (OUT)

- Rendering pages from the rows. The one renderer is dOrderedCharter's; this unit grades pages that
  are written, whoever writes them.
- Rationale rendered into its own tree (FQ-6, dConvergedCharter) and the atlas (FQ-8, dTotalRecall).
- Executing a page's commands (deviation-52, §8 F3).
- A fingerprint for the `file`, `installable`, `agent` and `entry` classes (deviation-51, §8 F4).
- A `leg` class. v2 joins leg tags to the step gate in a later build; this unit ships the `leg`
  shape and its row source, observed on a fixture member, and the class joins with its own
  `[[class]]` row (§8 F8).
- Fetching an external link.
- A writer that stamps fingerprints into pages. The red line prints the fingerprint the row now has,
  and the author edits the page.
- Grading prose: an anchor whose fingerprint is current over a paragraph that is wrong passes.
- The leg in an adopter. It grades gov's own pages against gov's own population, so it is an
  `[[exempt_leg]]` and never travels.
- Draining S6's list beyond the pages this pass anchors.

### Edges

- **consumes-from** `TOOL-dSafePassage-10` — `read_surface_classes`, `read_surface_population` and `VERB_SOURCES` in `tools/govkit/step_gate.py`, and the nine class ids of its class table; without them the leg has no population and exits 2
- **consumes-from** `TOOL-dSafePassage-11` — `help/python-floor.md` and the `platforms.provision` usage row, which S11 anchors and this leg fingerprints; without them the key sits on S6's list
- **consumes-from** external — dGroundRules' catalogue (`cl-dClosedLoop-0007`), whose rows give each policy key's values, default, summary and usage, and its reader (`cl-dClosedLoop-0008`), through which `help.enforce` is read; without them the `policy` class is empty and the leg exits 2
- **hands-off** `TOOL-dSafePassage-5` — a `[[usage]]` row in `tools/govkit/usage.toml` and an anchor for each `upgrade_walk.py` command its help section shows, since that unit's page lands after this leg
- **hands-off** external — each later build whose class joins the step gate adds its `[[class]]` row to `tools/govkit/usage.toml` and its members' rows, the clause's "each later class's rows joining when its build lands it"
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### Data model

`tools/govkit/usage.toml`:

```toml
[[class]]
class = "verb"          # a class id of tools/govkit/surface-classes.toml
usage = "verb"          # verb | key | hook | leg | page | none
rows = "usage-text"     # where this class's rows come from (table below)
why = "a CLI verb is a verb and its flags"

[[usage]]
id = "script:tools/roles/handoff.py#render"   # a member id, or script:<path>[#<verb>]
shape = "verb"
entry = "tools/roles/handoff.py"
verb = "render"
flags = ["--role=", "--build=", "--unit=", "--part=", "--stand-in"]   # a trailing = takes a value

[[usage]]
id = "conf:.memory-tree.conf#MEMORY_ROOT"
shape = "key"
values = "a repo-relative directory"
default = "memory"
```

The classes, as TOOL-dSafePassage-10's table spells them:

| Class | Shape | Rows from |
|---|---|---|
| `file` | `none` | an installed file's user-facing usage is the command or hook that runs it, graded in its own class |
| `installable` | `none` | the same |
| `hook` | `hook` | the `*.fragment.json` whose `name` is the member, its `event` and `matcher` (`tools/hooks/format-guard.fragment.json:1-7`) |
| `command` | `verb` | `usage.toml`, the Skill's name and its arguments |
| `agent` | `page` | presence only |
| `conf` | `key` | `usage.toml` |
| `policy` | `key` | the catalogue row `cl-dClosedLoop-0007` defines, its allowed values and default |
| `verb` | `verb` | the usage line of the `VERB_SOURCES` text that states the verb, its `--` flags, a flag followed by `<...>` or `x=y` taking a value |
| `entry` | `page` | presence only |

A `script:` row is a `verb` row for an entrypoint a page shows that no class holds. It is
fingerprinted and anchored like a member's row, and it exists only because a page documents it.

The `leg` shape reads a manifest row's `name` and `argv`; it is armed by a `[[class]]` row naming it.

### The fingerprint and the anchors

`derive_usage_fingerprint(row)` hashes `json.dumps(shape_fields, sort_keys=True, separators=(",",
":"))`, the shape fields being the row less its `id`, so an id change is the step gate's question and
not this leg's. An anchor is read by
`<!--\s*usage:\s*(?P<id>.+?)(?:\s+(?P<fp>[0-9a-f]{8}))?\s*-->`, outside fenced blocks, keyed on the
id as `govkit:entry` anchors are keyed in the runbook (`tools/govkit/check_runbook_parity.py:42`).
A member is documented when its anchor exists, whatever the prose around it; S3's stale line names
the page, the id, the fingerprint the page holds and the one the row has.

### The page commands

`read_page_commands(page)` yields each command with its line; `shlex.split` in POSIX mode, a
segment per `|`, `&&` or `;`, leading `NAME=value` assignments set aside, and a `...` token
skipped. For `python`, `python3`, `bash` or `sh` the entrypoint is the next token; otherwise it is
the first. A `<prefix>/` or `{prefix}/` spelling resolves to `tools/`, as gov's install prefix.
`check_page_command(cmd, rows)` returns `tested`, `skipped` (no tracked entrypoint), `unrowed` (a
tracked entrypoint with no row) or a red naming the undeclared verb or flag. A placeholder such as
`<slug>` is a value, never a flag.

### The link check

`check_page_links(page, tracked)` reads `\]\(([^)\s]+)\)` outside fences. A target opening `http:`,
`https:` or `mailto:` is counted. Any other is resolved against the page's directory, its
`#fragment` cut and checked against the target page's headings slugged as GitHub slugs them
(lowercase, punctuation but `-` and `_` dropped, spaces to `-`) and its explicit `<a id="...">`.

### The list and its low-water

`memory/project/docs-undocumented.txt` follows the waiver-list format (`<token>\t<reason>`, `#`
comments). `check_legacy_low_water` loads `tools/drift-audit/drift_report.py` by path, builds its
`Git(root, "HEAD")` (`:460`) and calls `derive_low_waters` over the list; a working-tree count above
the low-water is the red, and a list with no history yet is judged by its seed alone. The list is
seeded once, at this pass, from `docs_leg.py --list --undocumented`, which prints one id per line;
nothing writes it after.

### The leg and its output

```
python tools/govkit/docs_leg.py
python tools/govkit/docs_leg.py --list [--undocumented]
python tools/govkit/docs_leg.py --fixture --plant <case> [--enforce refuse|warn|off]
```

Every line opens `docs:`. The summary line carries the classes, members, rows, anchors, stale pages,
commands tested, skipped and unrowed, links checked and external, and the list's rows and low-water,
every count DERIVED at the run. The leg row:
`{"name": "docs", "argv": ["python", "{prefix}/govkit/docs_leg.py"], "chunk": "declarations",
"subject": "repo", "reads": {"history": "..."}, "doc_reads": ["help/", "memory/project/docs-undocumented.txt"]}`,
with no `guard`, since the population spans `tools/`, `skills/`, `.claude/` and `.governance/`, and a
`ceiling` from its measured time. A failure means this repository's pages are stale, so its subject
is `repo` (`tools/run-gates/run-gates.sh:2809-2812`). The module raises no `Refusal` and appends to
no report, so `govkit refusal join` gains no branch (`tools/govkit/refusal_join.py:197-208`).

### The fixture

`build_docs_fixture(tmp, plant)` makes a scratch git repository holding two pages, a `usage.toml`,
one fragment, a one-row manifest, a legacy list with a two-commit history, and an in-memory class
list and population of six members, one per shape and one `page` member, so plants compose. The
pages show a `script:` command, an inline command and a `sort` command. Each case's exit, under the
default `refuse`:

| Plant | What it stages | Exit |
|---|---|---|
| none | the base | 0 |
| `stale-page` | a flag added to a `verb` row, the page's anchor unchanged | 1 |
| `bad-flag` | a page command respelling `--part` as `--section` | 1 |
| `bad-verb` | a page command naming an undeclared verb | 1 |
| `unrowed` | a page command whose tracked entrypoint has no row | 1 |
| `broken-link` | a relative link to an absent file | 1 |
| `broken-fragment` | a link `#fragment` no heading slugs to | 1 |
| `external-link` | an `https` link | 0 |
| `undocumented` | a member with no anchor and no list row | 1 |
| `drained-row` | a list row for an anchored member | 1 |
| `grown-list` | a list row added in a later commit | 1 |
| `orphan-anchor` | an anchor naming no member | 1 |
| `restated-row` | a `[[usage]]` row for the fixture hook | 1 |
| `leg-row` | the fixture leg's argv changed, its anchor unchanged | 1 |
| `unclassed` | a registered class with no `[[class]]` row | 1 |
| `empty-class` | a `key` class with no member | 2 |
| `untested` | every page command made `unrowed` and listed | 2 |

`--enforce warn` with `stale-page` exits 0 printing a `WARN` line; `--enforce off` exits 0 printing
one line and reading no page.

### Inventory

Minted: the module `tools/govkit/docs_leg.py`; the file `tools/govkit/usage.toml` with its
`[[class]]` keys `class`, `usage`, `rows` and `why`, its `[[usage]]` keys `id`, `shape`, `entry`,
`verb`, `flags`, `values` and `default`, and the shape words `verb`, `key`, `hook`, `leg`, `page`
and `none`; the id form `script:<path>[#<verb>]`; the anchor `<!-- usage: ... -->`; the list
`memory/project/docs-undocumented.txt`; the functions `read_usage_classes`, `read_usage_rows`,
`derive_usage_fingerprint`, `read_page_anchors`, `read_page_commands`, `check_page_command`,
`check_page_links`, `read_legacy_rows`, `check_legacy_low_water`, `check_docs`,
`build_docs_fixture` and `main`; the flags `--list`, `--undocumented`, `--fixture`, `--plant` and
`--enforce`; the leg `docs`; the prefix `docs:`; the policy key `help.enforce`. Naming cells: each
function passes `py.function` (`python tools/lexicon/lexicon.py --suggest <name> --as py.function`,
OK for all eleven, 2026-10-23).

### Migration

Additive. Today's members start on S6's list, so the leg lands green; every member a later landing
adds must be documented, because the list may not grow. No adopter carries anything here.

### Rollout

Live at landing under `help.enforce = refuse`, the catalogue default. Order 5 holds this unit and
TOOL-dSafePassage-5, and their write sets meet at `tools/gate-legs.json`,
`tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`, `tools/run-gates/ceiling-evidence.txt`,
`tools/govkit/selftest.py` and `memory/map/features/govkit.md`, so the two passes sequence (M6), this
unit first: that unit's help section then lands under this leg. Every page landed by an earlier unit
of this build is graded at this pass, and S11 anchors it.

### Files touched (estimate)

- `tools/govkit/docs_leg.py` (new)
- `tools/govkit/usage.toml` (new)
- `tools/govkit/selftest.py`
- `tools/govkit/registry.toml`
- `tools/govkit/subject-pins.tsv`
- `tools/gate-legs.json`
- `tools/run-gates/ceiling-evidence.txt`
- `tools/drift-audit/drift_signals.py`
- `memory/project/docs-undocumented.txt` (new)
- `memory/map/features/govkit.md`
- `help/docs-leg.md` (new)
- `help/README.md`
- `help/roles.md`
- `help/measure-legs.md`
- `help/step-gate.md`, `help/upgrade-steps.md`, `help/shims.md`, `help/update-edits.md` and `help/python-floor.md`, the pages this build's earlier units land, for their anchors
- the catalogue file of `cl-dClosedLoop-0007`, for the `help.enforce` row, at the path dGroundRules lands
- `memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-13-deviation-51.md` (new, at the spec commit)
- `memory/builds/dSafePassage/build/2026-10-23-build-TOOL-dSafePassage-13-deviation-52.md` (new, at the spec commit)

### Alternatives rejected

- **A co-change rule**, a commit touching an entrypoint must touch a page: a renamed flag beside a
  whitespace page edit passes, and an internal refactor reds (the research's C3).
- **Membership alone**, each member mapped to an anchor: a renamed flag or a changed default leaves
  membership unchanged and the leg green (C4, kept as S3's presence half).
- **Fingerprints derived from code**, argparse or a script's header: the research's first prototype
  false-reddened 4 real examples on mutually exclusive groups, so a row is declared. The `verb`
  class's usage text is the declared line a user reads, which is why it is read and not restated.
- **A help.enforce in a conf key**: the key is the catalogue's, the parent's one reader.

## 5. Production-readiness checklist

- security: read-only over the tree; the fixture writes only in its own temp directory; `--enforce` is honoured under `--fixture` only, so the leg's argv cannot be relaxed past the policy file; a page command is parsed and never run.
- perf / scale: one population read through TOOL-dSafePassage-10's reader, a read of each page, and one `git log -p` over the list, DERIVED at the run; the `ceiling` is set from the measured time at the pass and recorded in `tools/run-gates/ceiling-evidence.txt`.
- error / empty / loading states: an empty shaped class, an untested page set and an unreadable declaration exit 2 with the reason; `off` prints one line naming the key and its source.
- observability: one summary line and one line per finding, each naming page, line and id.
- risks: the `verb` class's usage text grammar differs between `govkit.py` and `unattended.sh`, and a line the parser misreads yields a wrong flag set; the fixture's `bad-flag` plant and AC2's real-page run are what see it. A sibling class spelling a member id another way leaves that member undocumented, which reds rather than passes.
- testing: the fixture of §4 under every plant, AC2's scratch-clone respelling, and the selftest arm (§7).
- migration: additive; §4 "### Migration".
- user docs: `help/docs-leg.md` and its `help/README.md` line (S12), graded by this leg.

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/docs_leg.py" --fixture --plant stale-page` runs, it exits 1 with
  a `docs: STALE` line naming the fixture page, the member id, the page's fingerprint and the row's
  new one; with no plant it exits 0.
  Red when: the fingerprint is read from the page and never recomputed from the row, or a row's
  change leaves its fingerprint unchanged.
- **AC2** — When `python "tools/govkit/docs_leg.py"` runs on the tree after the pass, it exits 0 under
  the default `refuse`, with 0 stale pages and a non-zero `tested` count for `help/roles.md` and
  `help/measure-legs.md`; in a scratch clone whose `help/roles.md` respells `--part` as `--section`
  in its `handoff.py render` command, the same call exits 1 naming that page, its line and the flag.
  Red when: the real pages' commands are all `skipped` or `unrowed`, so the green tests nothing.
  fixture: a scratch clone under `%TEMP%`, since the respelling must not touch the worktree.
  figure: the `tested` counts are DERIVED at the run.
- **AC3** — When `python "tools/govkit/docs_leg.py" --fixture --plant bad-flag` runs, it exits 1 naming
  `--section`; `--plant bad-verb` exits 1 naming the verb; `--plant unrowed` exits 1 naming the
  entrypoint; and the base's `sort` command counts as `skipped`.
  Red when: a page command is matched against no row, or an unrowed tracked entrypoint passes.
- **AC4** — When `python "tools/govkit/docs_leg.py" --fixture --plant broken-link` runs, it exits 1
  naming the link and its page; `--plant broken-fragment` exits 1 naming the fragment; `--plant
  external-link` exits 0 with the link counted as external.
  Red when: a link inside a fenced block is graded, a fragment is not checked, or an external link
  is fetched.
- **AC5** — When `python "tools/govkit/docs_leg.py" --fixture --plant undocumented` runs, it exits 1
  naming the member; `--plant drained-row` exits 1 naming the row; `--plant grown-list` exits 1
  naming the list's count and its low-water; `--plant orphan-anchor` exits 1 naming the anchor.
  Red when: the list's count is compared with nothing in history, or an anchored member's row is
  left on the list.
- **AC6** — When `python "tools/govkit/docs_leg.py" --fixture --plant restated-row` runs, it exits 1
  naming the hook whose fragment states its usage; `--plant leg-row` exits 1 with a `STALE` line
  naming the fixture leg.
  Red when: a member's usage is read from `usage.toml` where its own registry states it, or the
  `leg` shape is never fingerprinted.
- **AC7** — When `python "tools/govkit/docs_leg.py" --fixture --plant unclassed` runs, it exits 1
  naming the class with no `[[class]]` row; `--plant empty-class` exits 2 naming the class;
  `--plant untested` exits 2 saying no page command was tested.
  Red when: a class with no usage declaration is skipped, or an empty population exits 0.
- **AC8** — When `python "tools/govkit/docs_leg.py" --fixture --plant stale-page --enforce warn` runs,
  it exits 0 with a `docs: WARN` line naming the stale page; with `--enforce off` it exits 0 printing
  one line that names `help.enforce`; and `python "tools/govkit/docs_leg.py" --list` on the tree
  prints `policy:help.enforce` with `refuse warn off`, default `refuse`, and the page that anchors it.
  Red when: `warn` exits 1, `off` still reads the pages, or the catalogue row lacks a value or a
  default.
  fixture: needs dGroundRules' catalogue and reader landed, which the build run lands first.
- **AC9** — When `git grep -n -e "help.enforce" -e "docs_leg" -- help/` runs, it finds the new page
  and its line in `help/README.md`, and AC2's run grades that page green.
  Red when: the leg ships with no page, or its page is not graded by it.
- **AC10** — When `git grep -n -E "(^docs\s|\"docs\")" -- tools/gate-legs.json tools/govkit/registry.toml tools/govkit/subject-pins.tsv tools/run-gates/ceiling-evidence.txt memory/map/features/govkit.md`
  runs, each of the five files carries the leg's name, and
  `git grep -n "docs-undocumented" -- tools/drift-audit/drift_signals.py` finds the `SHRINK_ONLY` row.
  Red when: the leg lands without a row one of its meta-gates owes, or the list is not on
  drift-audit's table.
- **AC11** — When `git grep -n -e "Departs from" -- memory/builds/dSafePassage/build/` runs, it lists a
  deviation-51 and a deviation-52 record of this unit, each departing from `cl-dClosedLoop-0030@274077d4`.
  Red when: either departure of §8 F3 and F4 is built with no record.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `govkit runbook parity` · `drift-audit selftest` · `drift-audit records` · `recall floor` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `codebase-map gate coverage` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The new leg `docs` is not on the list above, since that list names legs the manifest holds today; the
main loop observes it at the close through the arm lines below.

New arm: tools/govkit/docs_leg.py · covers AC2 · the new `docs` leg itself, its failing case staged by respelling a flag of a page command in `help/roles.md` · none
New arm: tools/govkit/selftest.py · covers AC1 AC3 AC4 AC5 AC6 AC7 AC8 · a new arm runs the leg's fixture over every plant of §4, and `stale-page` under `warn` and `off`, asserting each exit and named line · none

## 8. Open questions

- **F1 — A leg of its own, or an arm inside the step gate's leg.** The clause says "an arm of the step
  gate over its population"; the brief's S7 fixes a leg `docs` run by its own module importing the
  step gate's reader. Options: an arm inside `step_gate.py`; a leg sharing the population through its
  one reader. The step gate diffs a range and refuses unconditionally; this leg grades the whole tree
  and answers to `help.enforce`, so one exit cannot carry both. RESOLVED (agent, 2026-10-23,
  delegated): the leg, rung 1, the brief's S7 and the research's "an arm of its step gate over the
  same population, graded whole" (`research-final-help.md`, section 5, C5); "arm of" is read as
  "over the same population through one reader". widens: none · relaxes: none
- **F2 — How a moved fingerprint is joined to its page.** Options: (a) the page's anchor carries the
  fingerprint, graded over the whole tree; (b) a range check, a fingerprint that moved between base
  and tip with its page untouched in the range; (c) a committed ledger of fingerprints. (b) passes a
  whitespace edit of the page, the research's C3 loss, and needs a base; (c) is an inventory typed
  beside what it describes, which the charter's derive rule refuses. RESOLVED (agent, 2026-10-23,
  delegated): (a), rung 3, the survivor of both vetoes. widens: none · relaxes: none
- **F3 — What "each command a page shows run as a test" runs.** Options: (a) execute each command;
  (b) execute only commands with no placeholder; (c) test each command against its declared row.
  (a) fails the clause's own "green on the real ones": `help/roles.md` shows `<slug>` and
  `<unit-id>` placeholders, and `help/measure-legs.md`'s example runs every leg, a bar inside a leg.
  (b) still runs that example and leaves the rest untested. (c) fails the word "run" read as
  "execute". Every option fails a clause-tier bound, so rung 6: the weakest is "run" read as
  execution, since the research the owner's FQ-5 pick rests on defines the test as "doc-tested
  against the declared row" and its prototype ran exactly that over `help/roles.md`. RESOLVED (agent,
  2026-10-23, delegated): (c), recorded as deviation-52, per ER:328. widens: none · relaxes: the
  reading of "each command a page shows run as a test" as executing it
- **F4 — The classes whose members have no row shape the clause names.** Options: (a) invent a fifth
  shape per class, a file's path, an agent's name, a registry entry's id; (b) `none` for `file` and
  `installable`, presence for `agent` and `entry`. A path-only fingerprint cannot move without the
  member vanishing, which is the step gate's red, so (a) adds no observation and puts every
  installed file on the list for good. RESOLVED (agent, 2026-10-23, delegated): (b), rung 3,
  recorded as deviation-51 because it narrows "each member". widens: none · relaxes: none
- **F5 — Where a member's usage row lives.** Options: one `usage.toml` holding every row; each row
  read from the registry that already states it, `usage.toml` holding only the rest. RESOLVED
  (agent, 2026-10-23, delegated): the second, rung 3, the charter's one-fact rule; a restated row
  is S2's finding. widens: none · relaxes: none
- **F6 — How the list stays shrink-only.** Options: (a) a count pin in the module, as runbook parity
  pins `PROBLEM_PIN` (`tools/govkit/check_runbook_parity.py:60`); (b) the count compared with the
  landing's base; (c) the count compared with its first-parent low-water. (a) is raised by a hand
  edit in the same diff; (b) needs a base this leg does not otherwise read. RESOLVED (agent,
  2026-10-23, delegated): (c), rung 3, reusing drift-audit's `derive_low_waters`, so the leg and
  drift-audit's `shrink_only_lists_not_shrinking` read one history. widens: none · relaxes: none
- **F7 — The parent is unbuilt.** `help.enforce`'s catalogue row and its reader are
  `cl-dClosedLoop-0007` and `cl-dClosedLoop-0008`, and neither has landed. RESOLVED (agent,
  2026-10-23, delegated): rung 1, v2's `[chain]` puts dGroundRules before this build; the build run
  re-grounds this spec against the landed parent first, spelling the catalogue path and the reader
  call as the parent ships them. widens: none · relaxes: none
- **F8 — The `leg` row shape with no `leg` class.** TOOL-dSafePassage-10 registers nine classes and
  no leg class; v2 joins leg tags to the step gate in a later build. Options: register a `leg` class
  here, widening the step gate's population; ship the shape, observed on a fixture member, and let
  the class join. RESOLVED (agent, 2026-10-23, delegated): the second, rung 1, the clause's "each
  later class's rows joining when its build lands it". widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-26`; no other section moved.

## 10. Reuse audit

The seams extended: TOOL-dSafePassage-10's `read_surface_population` and `VERB_SOURCES`, the one
population and the one verb source (brief S7); the runbook's `govkit:entry` anchor and its
both-directions presence join (`tools/govkit/check_runbook_parity.py:42-121`), whose anchor shape
this leg's anchor follows and whose liveness half it keeps; drift-audit's `derive_low_waters`
(`tools/drift-audit/drift_report.py:781-818`) and its `SHRINK_ONLY` table
(`tools/drift-audit/drift_signals.py:129-137`), read by path rather than copied; the waiver-list row
format of `memory/project/spec-token-waivers.txt`. `reuse_lookup.py "check every user-facing surface
has a current help page and its usage fingerprint matches"` ranked `check`, `usage`
(`unattended.sh`), `fingerprint` (`run-gates.sh`, a run fingerprint and not a usage row) and
`build_usage` (`runlog/extract.py`, token usage): none fingerprints a declared usage.
`reuse_lookup.py "check relative markdown links resolve to tracked files offline"` ranked no link
checker; memory hygiene's check 2 (`tools/memory-tree/check-memory-hygiene.sh:653-680`) is one, in
awk over `MEMORY_ROOT` and `.md` targets only, with no fragment check, so it cannot grade `help/`
and the leg carries its own reader, its fence rule the same. The probe and the source disagree on
one point: the research measured 0 of 9 hook fragments carrying a purpose, and the fragments do carry
`event` and `matcher`, the two fields the `hook` shape reads, so hooks need no `usage.toml` row. No
existing seam tests a page's commands, so S4 is new.

Recall terms used: `python tools/memory-recall/query.py "how is a help page kept current with the usage of the command, key or hook it documents" --terms "help page docs leg usage row fingerprint stale page shrink-only undocumented link check help.enforce"`
