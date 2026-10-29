# TOOL-dMindYourWords-6 — `--suggest` made forced-aware

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 11 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0267@06ce7948 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-5 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

`--suggest` proposes renames that break overrides: `do_GET` to `cmd_get`, `emit` to `print`, `handle`
to `run`, `get_queryset` to `read_queryset` and `setUp` to `set_up`, which silently stops unittest
calling it (gap-lex-02). This unit makes `--suggest` answer from the committed packs before it answers
from the verb table: a name a pack forces on the given base is answered FORCED and never renamed, a
generic name with no base gets a conditional answer, and the no-corpus-pass contract holds.

## 2. Scope (IN)

- **S1** — The flag. `main`'s `--suggest` parser (`tools/lexicon/lexicon.py:4396-4405`) reads
  `--suggest <name> --as <cell> [--base <dotted.Base>]`, the two flags in either order after the name.
  It exits 2 with its usage line on a flag with no value, a repeated flag, an unknown flag, a `--base`
  value that is not a dotted identifier (`^[A-Za-z_]\w*(\.[A-Za-z_]\w*)*$`), and `--base` on a cell
  whose surface is not `function`, since only a function's name can override a base member. The usage
  block (`:4362-4378`) names `--base`. Observed by AC6, AC7.
- **S2** — The forced answer. In `run_suggest` (`:3719`), after the empty-verb exit (`:3838-3844`) and
  before the debt lookup (`banned = build_banned_index(conf)` at `:3846`, the `want` block at
  `:3857-3876`), the name is matched against each pack whose `langs` holds the cell's extension
  through `Pack.read_row(base, name)` (TOOL-dMindYourWords-7 S3), the only code that matches pack rows,
  called with the given base in place of a resolved one: a member row on that base, a prefix row on
  that base the name starts with, or a host row naming the name. On a match it
  prints `FORCED — `<name>` is forced by `<base>` (<source>); keep it, never rename it`, `<source>` in
  I2's spelling `pack:<kit>:<row>`, and returns 0 before `render_convention` (`:3883`), so a forced
  name is never re-cased; a name that fails the cell's convention adds `note — a forced name keeps
  its host's spelling`. Observed by AC1, AC3.
- **S3** — The conditional answer. With no `--base`, `read_row` is asked once with base `None`; a host
  row it returns is FORCED by name, since a namespaced closed set applies by name (§8 F1). Otherwise
  it is asked for each distinct base the pack's `member` and `prefix` rows carry, and a name some
  base forces prints `CONDITIONAL — `<name>` is forced where its class derives from `<base>`
  (<source>); otherwise:` naming at most three bases sorted, then `and <n> more`, followed by today's
  answer unchanged. Observed by AC2, AC3.
- **S4** — The unmatched base. With `--base` given and no row matching, today's answer prints with
  `note — no pack row names `<name>` on `<base>`; it is graded as a free name here`, and the note adds
  that a repository base is not read by `--suggest`, the grader forcing an override by its parent.
  Observed by AC3.
- **S5** — The policy. `run_suggest` reads `read_policy_value("lexicon.forced", root)` (I7): under
  `verified` S2 to S4 hold; under `by-name` any member or prefix row name is FORCED by name whatever
  the base, the line saying `by name under lexicon.forced=by-name`, and no conditional prints; under
  `by-annotation` S2's FORCED line adds `note — under lexicon.forced=by-annotation a forced name needs a
  reasoned site suppression`. A refused read exits 2 naming the key. Observed by AC4.
- **S6** — No corpus pass. Every answer reads `.lexicon.conf`, the canon and pack data, never the
  tracked tree, as the contract at `:3727-3730` states. Observed by AC5.
- **S7** — Docs and version. `tools/lexicon/SKILL.template.md` documents `--base` and the FORCED and
  CONDITIONAL lines, and its render `.claude/skills/lexicon/SKILL.md` is re-written by
  `bash tools/lexicon/adopt-lexicon.sh --render`; `tools/lexicon/README.md` (`:466-475`, `:540`) and
  `tools/lexicon/LEXICON.md` (`:41-46`) say the same; `KIT_LEXICON_VERSION` (`lexicon.py:90`) moves.
  Observed by AC8.

## 3. Non-goals (OUT)

- The forced check of the corpus, its base resolution and its tally: TOOL-dMindYourWords-2. S2 calls
  `Pack.read_row`, the one row matcher the forced check calls too, and never writes a second one.
- Reading the site from the extraction. The lexicon review offers it beside `--base`; a site read is a
  corpus read, which the no-corpus-pass contract forbids, so the caller passes the base.
- A repository base passed as `--base`. Forcing an override by an in-repository parent is the grader's
  (TOOL-dMindYourWords-2's second case); S4 says so rather than reading a module.
- Which packs apply to a repository: TOOL-dMindYourWords-8 narrows S2's set to the selected one.
- Handing the declared base to a builder: the work order's vocabulary slot (TOOL-dMindYourWords-9).
  `--as tag.<namespace>`: TOOL-dMindYourWords-13, under which S1 refuses `--base`.

### Edges

- **consumes-from** `TOOL-dMindYourWords-7` — `load_pack` and `Pack.read_row`: the committed pack data every S2, S3 and S5 answer reads, `--suggest --base` answering from it without a corpus pass, and the one row matcher; without them there is nothing to be forced by
- **consumes-from** `TOOL-dMindYourWords-2` — `Offender.source`, the spelling of the source a FORCED or CONDITIONAL line names
- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value`, I7, through which S5 reads `lexicon.forced`
- **hands-off** `TOOL-dMindYourWords-9` — `--base`: the work order passes the base the spec declares for each name it hands a builder
- **hands-off** `TOOL-dMindYourWords-13` — `--base`: refused on a `tag.<namespace>` cell, whose surface is not `function`
- **hands-off** `TOOL-dMindYourWords-8` — `run_suggest`: its pack set becomes the selected one, custom packs `PACKS:` declares included

## 4. Design

### Evidence

Read at `ba8b3c8c4`; no product file differs from base `ccd1292e`.

- `run_suggest` (`tools/lexicon/lexicon.py:3719-3912`) answers in this order: the canon posture
  (`:3809`), the banned-suffix branch for a `type` cell (`:3828`), the empty-verb exit (`:3838`), the
  banned index (`:3846`) and the debt lookup (`:3857-3876`), then `render_swapped_name` (`:3878`) and
  `render_convention` (`:3883`). Nothing in it reads a base, so `emit` comes back as a rename.
- The contract "NO CORPUS PASS" is stated at `:3727-3730`, and the verb returns only 0 and 2 (`main`'s
  comment at `:4417-4418`).
- `main` reads `rest[0] == "--as"` by position (`:4399`); any other token after the name is dropped
  unread, so `--base` today is silently ignored.
- The renames gap-lex-02 lists are today's answers (research-lexicon-kit:151, population:82); the five
  bases this spec's fixtures use are `http.server.BaseHTTPRequestHandler`, `logging.Handler` (twice),
  `django.views.generic.list.MultipleObjectMixin` and `unittest.TestCase`.

### The answer order

| Step | Reads | Prints | Returns |
|---|---|---|---|
| 1 | the cell, the routing, the canon posture, as today | as today | 2 on a refusal |
| 2 | the banned-suffix branch on a `type` cell, as today | as today | 0 |
| 3 | `lexicon.forced` through I7 | nothing | 2 on a refused read |
| 4 | the packs, with `--base` or by host pattern | `FORCED — …` and its notes | 0 |
| 5 | the packs, no `--base`, member or prefix rows | `CONDITIONAL — …` | continues |
| 6 | the verb table and the canon, as today | today's answer | 0 |

Step 3 runs only on a `function` cell, so a `type` or `file` answer costs no subprocess.

### Files touched (estimate)

- `tools/lexicon/lexicon.py` — `main`'s parser and usage block, `run_suggest`, `KIT_LEXICON_VERSION`
- `tools/lexicon/SKILL.template.md`, and its render `.claude/skills/lexicon/SKILL.md`
- `tools/lexicon/README.md`
- `tools/lexicon/LEXICON.md`
- `tools/lexicon/selftest.py` — the fixtures of §6

### Alternatives rejected

- **A second matcher in `run_suggest`.** Two answers to one question: the grader and the advisor would
  disagree on a prefix row the moment one changed. S2 calls `Pack.read_row`, as the forced check does.
- **Reading the site's class from the working tree.** A corpus read; the measured test is AC5's broken
  file, which a site read would trip.
- **Answering the forced name re-cased to the cell's convention.** `do_GET` to `do_get` is gap-lex-02's
  break by another route; S2 returns before the re-casing.

## 5. Production-readiness checklist

- security — `--base` is validated at the parser, once, as a dotted identifier; it selects pack rows
  and is never imported, evaluated or used as a path.
- perf / scale — pack files are read, never the tree; one `policy.py get` subprocess per `function`
  answer.
- error / empty / loading states — no pack loaded answers as today; an unmatched `--base` says so
  (S4); a refused policy read exits 2 naming the key.
- observability — every forced answer names its base and its `pack:` source.
- risks — an agent trusting a CONDITIONAL answer without checking its class; the line says the
  condition before the rename.
- testing — the fixtures of §6, gap-lex-02's five names among them.
- migration — none.
- user docs — the Skill template and its render, `tools/lexicon/README.md` and `LEXICON.md`; no
  `help/` page covers the lexicon.

## 6. Acceptance criteria

- **AC1** — When `python lexicon.py --suggest <name> --as py.function --base <base>` runs from a kit
  copy in a fixture repository for each of gap-lex-02's pairs, `do_GET` on
  `http.server.BaseHTTPRequestHandler`, `emit` and `handle` on `logging.Handler`, `get_queryset` on
  `django.views.generic.list.MultipleObjectMixin` and `setUp` on `unittest.TestCase`, each prints one
  `FORCED` line naming its base and a `pack:` source, prints no `use ` line, and exits 0.
  Red when: any of the five is answered with a rename, which is today's answer.
  fixture: the selftest builds the repository under the temp root with a `.lexicon.conf` declaring
  `py.function` snake and `py.type` pascal, `py` armed; the copy holds the first-wave packs and one
  planted `django.toml`, since Django is a second-wave pack.
- **AC2** — When the same five run with no `--base`, `emit` and `setUp` each print a `CONDITIONAL` line
  naming `logging.Handler` and `unittest.TestCase`, followed by today's answer.
  Red when: a generic name with no base gets the rename alone, or a FORCED line.
- **AC3** — When `--suggest pytest_configure --as py.function` and `--suggest __str__ --as py.function`
  run with no `--base`, each prints `FORCED` naming its host row's pack; when `--suggest emit --as
  py.function --base mylib.Thing` runs, it prints today's answer and the `no pack row names` note.
  Red when: a host-row name is renamed, or an unmatched base is answered FORCED.
- **AC4** — When the fixture repository commits `.governance/policy.toml` setting `lexicon.forced` to
  `by-name`, `--suggest emit --as py.function` with no base prints `FORCED` with `by name under
  lexicon.forced=by-name`; set to `by-annotation`, `--suggest emit --as py.function --base
  logging.Handler` prints `FORCED` and the reasoned-site-suppression note; with no policy file the
  answers are AC1's and AC2's.
  Red when: `by-name` still answers conditionally, or `by-annotation` answers a rename.
  fixture: the policy kit beside the kit copy, as I7 resolves it; the file is committed because
  `policy.py get` reads the landed revision.
- **AC5** — When the fixture also tracks `broken.py`, which does not parse, with `py` armed, `--suggest
  emit --as py.function --base logging.Handler` still prints `FORCED` and exits 0, while `python
  lexicon.py --check` in the same fixture exits 1 naming `broken.py`.
  Red when: `--suggest` walks the corpus, which the broken file would refuse.
- **AC6** — When `--suggest emit --as py.function` runs with `--base` and no value, with `--base 9x`,
  with `--base a..b`, with `--base` given twice, with `--frob`, and with `--as py.type --base
  logging.Handler`, each exits 2 printing a usage line on stderr; `--suggest emit --base logging.Handler
  --as py.function` answers as AC1.
  Red when: a malformed or misplaced `--base` is accepted, or the swapped order is refused.
- **AC7** — When `python lexicon.py --nope` runs, the usage block it writes to stderr names
  `--base <dotted.Base>` on the `--suggest` line.
  Red when: the usage block omits the flag.
- **AC8** — When `grep -c -- "--base"` runs over `.claude/skills/lexicon/SKILL.md`,
  `tools/lexicon/SKILL.template.md` and `tools/lexicon/README.md`, each count is at least 1, and
  `KIT_LEXICON_VERSION` in `tools/lexicon/lexicon.py` differs from `1.24`.
  Red when: the Skill an agent reads omits the flag, or the render lags its template.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `check-wiring self-test` · `lexicon wiring` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the planted suggest fixtures, its failing case `setUp` on `unittest.TestCase` answered `set_up` · none

## 8. Open questions

- **F1 — A name a host row matches, asked with no `--base`: FORCED or conditional?** Options: (a)
  FORCED by name; (b) the conditional answer. RESOLVED (agent, 2026-10-29, delegated): (a), rung 1:
  the clause TOOL-dMindYourWords-2 carries reads "a namespaced closed set applied by name through its
  rows' namespace pattern (`pytest_*`, `__*__`)", so no base can make it conditional.
  widens: none · relaxes: none
- **F2 — `--base` on a cell whose surface is not `function`?** Options: (a) exit 2 naming it; (b) ignore
  it; (c) answer from the packs anyway. (b) is a flag that silently does nothing, which `main`'s own
  `--expand` refusal (`:4382-4393`) rules out; (c) answers a type or file name from member rows that
  cannot apply to it. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none
- **F3 — Which packs answer before TOOL-dMindYourWords-8 lands, given no corpus pass can detect a
  stack?** Options: (a) every shipped pack, the set TOOL-dMindYourWords-2's forced check loads until
  selection exists; (b) none until a declaration names them. (b) answers nothing forced and fails AC1.
  RESOLVED (agent, 2026-10-29, delegated): (a), rung 3; TOOL-dMindYourWords-8 narrows the set and adds
  the custom packs. widens: none · relaxes: none
- **F4 — Does `--suggest` read `lexicon.forced`?** Options: (a) read it through I7 and answer per value;
  (b) answer as `verified` always. (b) answers `emit` conditionally under `by-name`, where the grader
  exempts it wherever it appears, and omits the suppression route under `by-annotation`. RESOLVED
  (agent, 2026-10-29, delegated): (a), rung 3, the most feature-rich survivor; it costs one subprocess on
  a `function` answer and an edge to TOOL-dMindYourWords-1 the spec brief's table does not list, which
  this spec's return names. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Item 6, the lexicon review's `[forced]` "`--suggest`
  becomes forced-aware" and its other-values bullet, gap-lex-02, scout A's row 6, and the spec brief's
  I2, I6, I7 and I12.

## 10. Reuse audit

The seams extended are `run_suggest` (`tools/lexicon/lexicon.py:3719`), whose answer order gains two
steps before its debt lookup (`:3857-3876`); `main`'s `--suggest` parser (`:4396-4405`) and usage block
(`:4362-4378`); the existing `note — ` line shape `read_routed_cell` returns (`:3701-3703`); and
TOOL-dMindYourWords-7's `Pack.read_row`, called rather than copied. `python
tools/codebase-map/reuse_lookup.py "answer a rename suggestion for a name forced by its base class"`
ranked `resolve_compare_base`, `read_host_name`, `read_cap_answer` and `derive_rename_map` first, each a
name-stem match outside the lexicon; none answers a forced name, so the two answer steps are new and
every reader they call exists or is a parent unit's. Scout A's row 6 holds against source at
`ba8b3c8c4`: the debt lookup is at `:3857-3876` and the parser at `:4396-4405`. The recall probe
surfaced lexicon review A's finding that point-of-use answers are computed before any class exists
(review-a:155), which is why S3 answers conditionally and S1 takes the base from the caller.

Recall terms used: `python tools/memory-recall/query.py "how should lexicon suggest answer a name
forced by a base class instead of proposing a rename" --terms "lexicon suggest forced base rename
do_GET setUp get_queryset emit pack no-corpus-pass"`
