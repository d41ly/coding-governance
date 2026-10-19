# TOOL-dRenderedAnchor-6 — the review protocol and the unattended Skill resolve their harness citations through the receipt-aware resolver

**Status:** SPECCED · rev-1 · 2026-10-19 · node d · Tier-2 · base 05357638 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-19-prompt-TOOL-dRenderedAnchor-6-brief.md](../prompts/2026-10-19-prompt-TOOL-dRenderedAnchor-6-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

In an adopter, the rendered `memory/guides/REVIEW-PROTOCOL.md` and
`.claude/skills/unattended/SKILL.md` name `tools/workflows/` harnesses that do not exist there,
because govkit lands the review-harness kit at `<prefix>/review-harness/` and both renderers
substitute `{{TOOL_ROOT}}` as plain text. This unit renders each `{{TOOL_ROOT}}<home>/<file>`
citation of both documents through `derive_kit_paths` first, as the memory-tree adopter already does
for `BUILD-METHOD.md`. Both documents then name the paths the install holds, and gov's own renders
stay byte-identical.

## 2. Scope (IN)

- **S1** — `tools/lib/render-doc.sh` gains a third canonical block, `render_kit_cites`. It rewrites
  the caller's `out` by substituting each line of `KIT_PATHS` whose placeholder is `{{TOOL_ROOT}}`
  followed by at least one character. It reads `KIT_PATHS` with every CR stripped, and it leaves
  every other line unapplied. Observed by AC4.
- **S2** — `tools/lib/resolve-python.test.sh` gains a `render_kit_cites` row in `PARITY_ROWS` and a
  behaviour section 2g that runs the canonical over one cite line, one bare `{{TOOL_ROOT}}` line and
  one adopter-placeholder line. Observed by AC4 and AC5.
- **S3** — `tools/workflows/check-protocol-parity.test.sh` carries `derive_kit_paths` and
  `render_kit_cites` inline, byte-identical to their canonicals. It resolves a python and refuses
  with exit 2 when it cannot, and derives `KIT_PATHS` once over every template its `PAIRS` names.
  Its `render` calls `render_kit_cites` after the `{{KIT_DIR}}` substitution and before the
  `{{TOOL_ROOT}}` one. Its header's "WHAT THIS DOES NOT CHECK" paragraph says which citations now
  resolve. Observed by AC1, AC5 and AC6.
- **S4** — The same script's render mode writes its pairs, then derives `KIT_PATHS` again. When the
  two derivations differ and `PROTOCOL_PARITY_REPASS` is unset, it re-runs itself once with the same
  arguments and that variable set to 1, and exits with the re-run's status. Observed by AC2.
- **S5** — `tools/unattended/adopt-unattended.sh` carries the same two blocks inline. After its
  `MEMORY_TREE_DIR` derivation it resolves a python and derives `KIT_PATHS` over `$TEMPLATE`, the
  Skill's template. Its `render` calls `render_kit_cites` between the same two substitutions, so
  `--check` grades exactly what a render writes. Observed by AC3, AC5 and AC6.
- **S6** — Both scripts exit 2 when no python resolves or `derive_kit_paths` fails. NOT OBSERVED:
  every host this repository runs on has a python, so the branch needs a PATH emptied of every
  launcher. `resolve_python` prints the reason, and its own refusal is the python resolver leg's.
- **S7** — Two arms in `tools/workflows/unattended-build.test.sh`, labelled `RA6-1` and `RA6-2`, over
  one renamed-directory layout behind a receipt. `FLOOR_ASSERTIONS` rises by their executed
  assertion count. Observed by AC1, AC2 and AC3.
- **S8** — `tools/workflows/README.md` and `tools/unattended/README.md` say that each harness citation
  resolves through the install receipt first, and the workflows README states the render mode's
  second pass. No page under `help/` describes how either document renders, so none changes.
  Observed by AC8.
- **S9** — A fresh scratch install shows both documents naming `tools/review-harness/`, recorded in
  this unit's acceptance ledger. Observed by AC7.

## 3. Non-goals (OUT)

- `roles_lib.resolve_harness_path`'s probe order, and `render_doc`'s own substitution loop in
  `tools/lib/render-doc.sh`. The brief rules both out, so `render_doc` keeps applying every line.
- Any edit to `derive_kit_paths`, `resolve_kit_dir` or their copies. They are carried as they stand.
  That includes the `resolve()` in `derive_kit_paths` that follows a junction (§5, risks).
- govkit's install layout and the receipt.
- An edit to `tools/workflows/REVIEW-PROTOCOL.template.md` or `tools/unattended/SKILL.template.md`.
  Their citations keep the `{{TOOL_ROOT}}<home>/<file>` shape, which is what this unit resolves.
- Running the unattended kit's own suites, under the owner's standing rule (`TOOL-dDerivedDocket-76`
  in `memory/DECISIONS.md`). The new unattended arm lives in a review-harness suite that already
  runs `adopt-unattended.sh` on the bar (§4).
- The four reds inherited from the last bar: spec-tokens, measure-legs, govkit selftest and
  foreign-prefix.
- Kit version bumps. The lander's `mint` writes them, and merge and push wait for the owner's ask.

Units 1 to 5 are CLOSED and landed at `05357638`. They are this unit's base, not a sibling's
pending work, so no edge names them.

### Edges

none

## 4. Design

### The base

`base 05357638` is the default branch, which carries units 1 to 5. The branch tip `912145ae` adds
records only (`git diff --stat 05357638 912145ae` names two build records and the kickoff manifest).
Every claim below about current code was read at that tip.

### What renders today

`render` in the parity script substitutes `{{KIT_DIR}}`, then `{{TOOL_ROOT}}`, as plain text
(`tools/workflows/check-protocol-parity.test.sh:253-262`, the two lines at `:258-259`). The adopter's
`render` does the same (`tools/unattended/adopt-unattended.sh:451-452`), with `TOOL_ROOT` derived
from the kit's own location (`:116-117`). Those are the two renderers the brief names. The citations
they reach:

| Template | Line | Citation |
|---|---|---|
| `tools/workflows/REVIEW-PROTOCOL.template.md` | 9, 13, 41, 163, 176, 179, 224 | `{{TOOL_ROOT}}hooks/agent-cap.js` |
| same | 34, 202 | `{{TOOL_ROOT}}workflows/tier2-review.js` |
| same | 92 | `{{TOOL_ROOT}}workflows/check-verifier-fanout.sh` |
| same | 109 | `{{TOOL_ROOT}}hooks/scratch-guard.js` |
| `tools/unattended/SKILL.template.md` | 125 | `{{TOOL_ROOT}}workflows/unattended-build.js`, `{{TOOL_ROOT}}workflows/unattended-unit.js` |
| same | 159 | `{{TOOL_ROOT}}runlog/runlog.py` |
| `tools/workflows/unattended-build.template.js` | 557 | `{{TOOL_ROOT}}unattended/unattended.sh` |

The scratch install `%TEMP%/rh3`, made from `54344d9a7` on 2026-10-19, reads `tools/workflows/` on
lines 34, 92 and 202 of its `memory/guides/REVIEW-PROTOCOL.md`. Its receipt places the kit at
`tools/review-harness/` and agent-cap at `tools/hooks/`. It has no unattended Skill, because no
`.unattended.conf` was written.

Measured on 2026-10-19 by sourcing `tools/lib/render-doc.sh` and running `derive_kit_paths python
<kit> REVIEW-PROTOCOL.template.md SKILL.template.md unattended-build.template.js`:

- over `%TEMP%/rh3`, with the kit at `tools/review-harness`, it prints each workflows cite under
  `tools/review-harness/`, the hooks, runlog and unattended cites at their gov spellings, and a bare
  `{{TOOL_ROOT}}<TAB>tools/` line, because the receipt carries `"prefix": "tools"`;
- over this worktree, with the kit at `tools/workflows`, every line it prints equals the plain
  substitution, and there is no bare line, because gov holds no receipt.

### The apply factory (S1, S2)

The memory-tree renderers apply `KIT_PATHS` inside `render_doc` (`tools/lib/render-doc.sh:45-48`),
and that loop applies every line, the bare `{{TOOL_ROOT}}` one included. These two renderers need
that loop with one filter, and they are two instances of it. The charter's `[reuse]` rule extracts
the factory at the second instance, so it is a gated canonical and not two copies:

```bash
# >>> render_kit_cites — canonical copy: render-doc.sh in gov's lib dir (byte-identical; gated)
# `render_kit_cites` rewrites the CALLER's `out`, by dynamic scope as `render_doc` reads the caller's
# KIT_REL, with every `{{TOOL_ROOT}}<home>/<file><TAB><path>` line of KIT_PATHS, each cite replaced
# whole. A bare `{{TOOL_ROOT}}` line and an adopter-placeholder line are left unapplied: the caller
# derives its tool root from its own location, and a receipt prefix beside it is a second answer.
render_kit_cites() {
  local kp kv
  while IFS=$'\t' read -r kp kv; do
    case "$kp" in '{{TOOL_ROOT}}'?*) out=${out//"$kp"/"$kv"} ;; esac
  done <<<"${KIT_PATHS//$'\r'/}"
}
# <<< render_kit_cites
```

It uses no nameref, because `local -n` needs bash 4.3 and no shipped script uses one today
(`git grep 'local -n '` over the shipped `*.sh` finds none). Both callers already name their render
buffer `out`. Its two-field `read` keeps the value last, so an empty value cannot shift a field.

The parity row is `render_kit_cites|$ROOT/$KIT_REL/render-doc.sh|$KIT_REL/render-doc`, beside the
`derive_kit_paths` row (`tools/lib/resolve-python.test.sh:168-182`). Its population grep reads every
tracked `*.sh` (`:211`), so both new copies of each block join their rows with no further edit.
Each copy of `derive_kit_paths` carries a nested `resolve_kit_dir` block, and the parity script
already carries one of its own, so that file holds two. The row grades every block in a file
(`:206`, `:217-219`).

Section 2g follows 2f (`:377-390`) and uses its shape, sourcing `$HERE/render-doc.sh` in a
`bash -c`:

| Input | Value |
|---|---|
| `KIT_PATHS` | three CRLF lines: `{{TOOL_ROOT}}h/t.js<TAB>p/k/t.js`, `{{TOOL_ROOT}}<TAB>q/`, `{{GATE_RUNNER}}<TAB>x` |
| `out` | `a {{TOOL_ROOT}}h/t.js b {{TOOL_ROOT}}c {{GATE_RUNNER}}` |
| expected `out` | `a p/k/t.js b {{TOOL_ROOT}}c {{GATE_RUNNER}}` |

The case filter taken out reads `q/c` and `x`. The CR drop taken out leaves a CR after `t.js`.

### The parity script (S3, S4)

Placement, in order, after the unpaired-template check (`:269-286`) and before `TMPD` (`:288`):

1. The `derive_kit_paths` and `render_kit_cites` blocks, beside the `resolve_kit_dir` function
   (`:146-199`).
2. A python is resolved with `$(resolve_python) || exit 2`. The by-design arm already refuses the
   same way (`:420`).
3. The template list is the second field of every line of `PAIRS` (`:91-95`), read from that
   variable by a `while IFS='|' read` loop, never a substitution. `KIT_PATHS` is
   `derive_kit_paths "$PY" "$KITREL" <those templates>`. A failure prints
   `protocol-parity: could not resolve the citations the templates make` and exits 2, which is the
   memory-tree suite's handling (`tools/memory-tree/kit-dogfood-parity.test.sh:309`).

`render` gains `render_kit_cites` between `:258` and `:259`. It renders every pair, and the
citations each template does not carry change nothing in it.

**The second pass is required by the brief's acceptance.** `apply` skips the four rendered harnesses
(repro record, Instrument 2), and the hand render writes them. The resolver holds a receipt row only
when its `path` is a file (`tools/lib/render-doc.sh:123`). So on a fresh install the first derivation
cannot see `tier2-review.js`, which the same run is about to write. The protocol would render
`<prefix>/workflows/tier2-review.js`, and the next check-mode run would derive the held path and red
DRIFT. The render mode writes only after every pair rendered clean (`:343-358`). So after its write
loop and before its `exit 0`, it derives again. When the lines differ and `PROTOCOL_PARITY_REPASS`
is unset, it prints one line naming the re-run and runs
`PROTOCOL_PARITY_REPASS=1 bash "$HERE/${0##*/}" "$@"`, then exits with that status. A child is used
rather than `exec`, because `exec` skips the `EXIT` trap that removes `TMPD` (`:289`). The argument
loop does not shift (`:57-63`), so `"$@"` is the caller's. Under `--tracked-only` the run creates
nothing, so the two derivations agree and no re-run follows. That is what govkit's regenerate runs
(`tools/workflows/kit.toml`, the `[[regenerate]]` block).

### The unattended adopter (S5, S6)

The two blocks go beside its `resolve_kit_dir` (`tools/unattended/adopt-unattended.sh:255-310`). After
the `MEMORY_TREE_DIR` block (`:312-353`) and before the stamp (`:355`), it runs these, each refusing
with exit 2:

```bash
_cite_py=$(resolve_python) || exit 2
KIT_PATHS=$(derive_kit_paths "$_cite_py" "$KIT_DIR" "$TEMPLATE") || exit 2
```

Only `$TEMPLATE` is passed (`:119`). It is the one template this adopter renders that takes
`TOOL_ROOT`. The fixture templates carry `{{KIT_DIR}}` only (`tools/unattended/README.md:70-73`), and
the copied templates carry no placeholder. A copied template that one day spelled an engine-answered
placeholder would make `derive_kit_paths` consult the playbook engine, and the refusal would be this
adopter's.

The refusal uses exit 2, the file's misconfigured code (`:7`). `check-arms.py` grades exit 1 only
(its docstring, "WHAT SIGNATURE 2 DOES NOT CHECK"), so no new branch enters the arms population. The
comment at `:111-115` names the build-method carrier as the second carrier of these two paths. That
carrier already resolves through `derive_kit_paths` (unit 2's §4), so this restores the one route it
asks for, and the comment says so.

**The first `apply` can still render the old path**, as unit 2 found for the `/build` Skill. When
the adopter runs before the hand render has written `unattended-build.js`, that cite falls through
to the prefix. `adopt-unattended.sh --check` then reads the Skill out of sync and names the re-render
as the remedy. In practice the adopter refuses at `apply` with no `.unattended.conf`, and the
operator runs it after the hand render.

### Agreement with the other carriers

Both callers pass the kit directory as `here`, which is the call `derive_kit_paths` makes for
`BUILD-METHOD.md`. For a harness this answers what the role index answers. The receipt rung ignores
`here`, and the kit directory's parent is the tool root `resolve_harness_path` probes. Unit 3's §4
settled the same agreement for the `/build` Skill.

### The arms (S7)

Both arms build on `build_layout` and `run_layout` (`tools/workflows/unattended-build.test.sh:1960-1987`)
and sit after PV-AC12 (`:2239-2276`), inside its unattended-adopter guard (`:2246`). One layout,
`$LAY/renamed`, is `build_layout` with the kit directory `scripts/rh`, the unattended directory
`scripts/$UNK` and the checklist `scripts/gotchas.py`. Then the arm:

- deletes `scripts/rh/tier2-review.js`, the fresh-install case S4 exists for;
- writes `.governance/install.json` with four rows, each `source` under a neutral `g/$WFK/`:

| role | source file | path |
|---|---|---|
| rendered | `tier2-review.template.js` | `scripts/rh/tier2-review.js` |
| rendered | `unattended-build.template.js` | `scripts/rh/unattended-build.js` |
| engine | `unattended-unit.js` | `scripts/rh/unattended-unit.js` |
| engine | `check-verifier-fanout.sh` | `scripts/rh/check-verifier-fanout.sh` |

- runs `git add -A` and `run_layout` once in render mode.

`RA6-1` asserts that the protocol names `scripts/rh/` for the three workflows cites and
`scripts/$WFK/` nowhere. It then asserts that a check-mode `run_layout` reads `rc=0`. `RA6-2` copies
the unattended kit and writes the seven-key conf as PV-AC12 does (`:2251-2259`), runs the fixture's
`adopt-unattended.sh`, and asserts that the Skill names `scripts/rh/unattended-build.js` and
`scripts/rh/unattended-unit.js` and `scripts/$WFK/` nowhere. It then asserts that `--check` exits 0.
Every kit segment is `$WFK` or `$UNK`, never typed, because a literal kit segment followed by a file
is an install-prefix hit. `rh` and `g` are neutral. With no receipt the layouts above it are
unchanged: the resolver's probe answers exactly what the plain prefix does there.

### Inventory

| Minted | Where | Naming cell |
|---|---|---|
| `render_kit_cites` | `tools/lib/render-doc.sh`, inline in the two renderers | `sh.function`; `lexicon.py --suggest` answered OK on 2026-10-19 |
| `PROTOCOL_PARITY_REPASS` | `tools/workflows/check-protocol-parity.test.sh`, an environment guard | none: `.lexicon.conf` declares no variable cell |
| parity row `render_kit_cites`, section 2g | `tools/lib/resolve-python.test.sh` | — |
| arms `RA6-1`, `RA6-2` | `tools/workflows/unattended-build.test.sh` | — |

No receipt field, conf key, leg or file is minted.

### Rollout

Tier-2: a shipped edit to two kits and a new carried block. `govkit update` carries the bytes. The
review-harness regenerate re-renders the protocol, and the next adopter run re-renders the Skill.
Kit versions are minted at landing.

### Files touched (estimate)

- `tools/lib/render-doc.sh`, `tools/lib/resolve-python.test.sh`
- `tools/workflows/check-protocol-parity.test.sh`, `tools/workflows/unattended-build.test.sh`,
  `tools/workflows/README.md`
- `tools/unattended/adopt-unattended.sh`, `tools/unattended/README.md`
- `memory/builds/dRenderedAnchor/build/`, for this unit's acceptance ledger

### Alternatives rejected

| Candidate | The test that rejected it | Verdict |
|---|---|---|
| C1 — apply every `derive_kit_paths` line, as `render_doc` does | over `%TEMP%/rh3` it prints a bare prefix line; applied, the receipt's prefix answers every unresolved `{{TOOL_ROOT}}` beside the location-derived one, two answers to one value | Rejected |
| C2 — cite the kit's own harnesses as `{{KIT_DIR}}/…` in the protocol template | edits a governance carrier the brief does not list (M3 veto 2), and the Skill's cross-kit cites still need the resolver | Rejected |
| C3 — no second pass; the runbook says to render twice | the brief's acceptance runs one hand render, after which check mode reds DRIFT (§4) | Rejected |
| C4 — a four-line apply loop written into each renderer | the charter's `[reuse]` rule extracts a factory at the second instance, and two ungated loops drift | Rejected |
| C5 — call `render_doc` whole | it substitutes the memory-tree conf facts these renderers do not own, and applies the bare line | Rejected |
| C6 — derive only over the protocol template in the parity script | a typed subset beside `PAIRS`; every pair renders through one `render` | Not taken |
| C7 — the factory takes a variable name through `local -n` | needs bash 4.3, which no shipped script assumes today | Rejected |

## 5. Production-readiness checklist

- security — No new write path. The citation pass applies only paths the resolver admits: inside the
  tree, existing, with no `..` part (`tools/lib/render-doc.sh:122-124`). The re-run carries the
  caller's arguments, and an environment guard bounds it to once.
- perf / scale — One python start per parity run and per adopter run, and one more for the second
  derivation in render mode. A re-run happens once, on a fresh install.
- error / empty / loading states — No python, or a failed derivation, is exit 2 with the reason.
  A citation nothing holds falls through to the plain prefix, as today.
- observability — The re-run prints one line naming why it happened. The render mode's existing
  `rendered` lines print once per pass.
- risks — `derive_kit_paths` resolves its kit directory physically (`tools/lib/render-doc.sh:152`).
  Under a junction into another repository, a held citation is spelled relative to the link target,
  which the memory-tree adopter shares today. The unattended kit's own suites are not run here
  (owner's rule). Whether their fixtures carry a receipt that moves a Skill line is UNVERIFIED. The
  govkit selftest, an inherited red, runs the parity script over fixtures
  (`tools/govkit/selftest.py:14634`), and its verdict is the close's to read.
- testing — AC1 to AC5 are fixture or in-process probes; AC6 and AC7 render in this worktree and in a
  scratch install. The main loop observes each new arm RED, then GREEN, at the close (§7).
- migration — N/A — no receipt, conf or deploy field moves, and an update re-renders both documents.
- user docs — The two kit READMEs (S8). No `help/` page covers these renders: `grep -n
  'REVIEW-PROTOCOL\|unattended' help/*.md` names only harness names in `help/roles.md`.

## 6. Acceptance criteria

`<p1>` is this unit's build pass commit. `$L` is `$LAY/renamed` of §4, built by a bash probe that
copies the arm's steps into a scratch directory. `$T` is a fresh scratch install at `%TEMP%/rh6`,
made by Instruments 1 to 3 of the repro record run from `<p1>`. A `.unattended.conf` holding
PV-AC12's seven keys is then added and staged in it. The parity script is the review-harness kit's
`check-protocol-parity`, named in prose here because its file is a suite-shaped name.

- **AC1** — When the parity script's fixture copy runs once in render mode in `$L`, `grep -c
  'scripts/rh/tier2-review.js'` over `$L/memory/guides/REVIEW-PROTOCOL.md` prints 2, `grep -c
  'scripts/rh/check-verifier-fanout.sh'` prints 1, and `grep -c 'scripts/workflows/'` prints 0.
  Red when: the `render_kit_cites` call is taken out of the parity script's `render`, and the last
  count reads 3.
  figure: 2 and 1 are PINNED from the template's lines 34, 202 and 92 at `05357638`.
- **AC2** — When the fixture copy then runs in check mode in `$L`, it prints `protocol-parity: in
  parity` and exits 0.
  Red when: the render mode's second pass is taken out, the first render names
  `scripts/workflows/tier2-review.js`, and check mode prints `DRIFT` and exits 1.
- **AC3** — When `bash scripts/unattended/adopt-unattended.sh` runs in `$L` after AC1, `grep -c
  'scripts/rh/unattended-build.js'` and `grep -c 'scripts/rh/unattended-unit.js'` over
  `$L/.claude/skills/unattended/SKILL.md` each print 1, `grep -c 'scripts/workflows/'` prints 0, and
  `adopt-unattended.sh --check` exits 0.
  Red when: the `render_kit_cites` call is taken out of the adopter's `render`, and line 125 names
  `scripts/workflows/` twice.
- **AC4** — When `bash -c '. tools/lib/render-doc.sh; render_kit_cites; printf %s "$out"'` runs with
  section 2g's `KIT_PATHS` and `out` exported, it prints `a p/k/t.js b {{TOOL_ROOT}}c
  {{GATE_RUNNER}}`.
  Red when: the case filter is taken out of the canonical, and it prints `q/c` and `x`; or the CR drop
  is, and a CR follows `t.js`.
- **AC5** — When `diff <(awk '/^# >>> render_kit_cites/,/^# <<< render_kit_cites/' tools/lib/render-doc.sh) <(awk '/^# >>> render_kit_cites/,/^# <<< render_kit_cites/' <copy>)`
  runs for each of the two renderers, and the same with `derive_kit_paths`, CRs dropped, each of the
  four prints nothing.
  Red when: one byte of either block changes in one copy, and its diff names that line.
- **AC6** — When the parity script runs in render mode and `bash tools/unattended/adopt-unattended.sh`
  runs, both in this worktree at `<p1>`, `git status --porcelain` prints nothing.
  Red when: the citation pass substitutes each cite with its kit directory instead of its file, and
  the status names `memory/guides/REVIEW-PROTOCOL.md` and `.claude/skills/unattended/SKILL.md`.
- **AC7** — When `bash tools/unattended/adopt-unattended.sh` has run in `$T`, `grep -n
  'tools/review-harness/'` over `$T/memory/guides/REVIEW-PROTOCOL.md` prints lines 34, 92 and 202,
  and over `$T/.claude/skills/unattended/SKILL.md` prints line 125. `grep -c 'tools/workflows/'`
  over each prints 0. The commands and their output go in this unit's acceptance ledger.
  Red when: the render is as at `%TEMP%/rh3`, whose protocol reads `tools/workflows/` on lines 34,
  92 and 202, as measured on 2026-10-19.
  cost: the 26-kit install of the repro instruments; its duration is UNVERIFIED.
- **AC8** — When `grep -c 'derive_kit_paths'` runs over `tools/workflows/README.md` and
  `tools/unattended/README.md`, each prints at least 1.
  Red when: either README is as at `05357638`, where both read 0.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended skill wiring` · `unattended skill size` · `unattended-build self-test` · `tier2-review self-test` · `verifier fan-out self-test` · `review-join self-test` · `shell hygiene (a loop fed by a command substitution)` · `shell hygiene (a location probe asked from a moved directory)` · `shell hygiene (a fork spent on builtin work)` · `shell hygiene (a fixed-name temp renamed into place)` · `spawn budget (forks per hot entrypoint)` · `harness arms (fail branches armed or pinned)` · `install-prefix (shipped surface)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `codebase-map coverage + freshness` · `memory hygiene` · `recall floor` · `recall floor arms`

The brief names the first three, the shell hygiene legs, memory hygiene and kit version markers.
The four `{prefix}/workflows/` legs and the two recall legs are owed by the guards the Files touched
paths trip. They were derived on 2026-10-19 from `tools/gate-legs.json` with the breadth floor at
`tools/check-spec-tokens.py:262`, which excludes `{prefix}/` and `{prefix}/lib/` as broad. The arms,
install-prefix, epoch and map legs read the shipped files and the minted function. New shell lines
take the no-fork forms those legs require, and no registry row is added or raised. The close runs
the bar once, after the unit is terminal; no pass runs a leg.

New arm: tools/workflows/unattended-build.test.sh, RA6-1 · covers AC1 AC2 · the render_kit_cites call taken out of the parity script's render, then separately the render mode's second pass · FLOOR_ASSERTIONS rises by the arm's executed count
New arm: tools/workflows/unattended-build.test.sh, RA6-2 · covers AC3 · the render_kit_cites call taken out of adopt-unattended.sh's render · FLOOR_ASSERTIONS rises by the arm's executed count
New arm: tools/lib/resolve-python.test.sh, section 2g · covers AC4 · the case filter taken out of render-doc.sh's render_kit_cites, then separately its CR drop · none
New arm: tools/lib/resolve-python.test.sh, parity row render_kit_cites · covers AC5 · one byte changed in the parity script's copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-19 · initial draft from the unit's brief. The fresh-install case was derived from
  the resolver's existence test and the render mode's write order, and it makes the second pass part
  of the scope. The apply loop is a gated factory because the two renderers are its second
  instance. Both rendered documents and the resolver's answers were measured on `%TEMP%/rh3` and in
  this worktree.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a kit template's tool-root citations to the paths
the install receipt holds"` ranked `render` a SEAM at fan-in 13. Its definitions include both files
this unit edits, `tools/workflows/check-protocol-parity.test.sh` and
`tools/unattended/adopt-unattended.sh`. It ranked `resolve_kit_dir` a SEAM at fan-in 11 with 71
installs. Those are the seams this unit extends. Each renderer's `render` gains one call, and
`resolve_kit_dir` is reached through `derive_kit_paths`, the canonical citation resolver in
`tools/lib/render-doc.sh` that the memory-tree adopter already carries inline. The lookup did not rank
`derive_kit_paths` itself, a shell function. It was read at source instead, and §4 cites it. No
existing seam fits the filtered apply step: `render_doc`'s loop applies every line, and the roles
kit's pass is Python. So `render_kit_cites` is new, and it is gated as `derive_kit_paths` is. The
gate-side seams are extended in place: `build_layout`, `run_layout` and PV-AC12's adopter run in
`tools/workflows/unattended-build.test.sh`, and section 2f's shape and `PARITY_ROWS` in
`tools/lib/resolve-python.test.sh`.

The recall probe returned the unit's brief, units 2 and 3's specs and their closing reviews, and
`TOOL-dPolishedVitrine-8`, an open ask about this parity script's unattended-kit probe. That ask
does not overlap: it concerns the build harness's driver path, which no line here changes. The brief
says the scratch install `%TEMP%/rh3` reads `tools/workflows/`. That was confirmed for its protocol,
and the same install has no unattended Skill to read (§4).

The gotchas checklist for the touched paths selected `fixture-passes-by-finding-nothing`, which is
why every arm asserts a positive count beside its absence count. `staged-break-substitutes-a-synthetic-value`
is why each red half removes the shipped call rather than swapping a value. `empty-field-collapses-unless-it-is-last`
is why the factory's `read` keeps the value last. `two-answers-to-one-question` is why the bare
prefix line is not applied. `test-oracle-read-from-a-historical-sha` is why no criterion compares
against a `git show` of a past sha.

Recall terms used: `python tools/memory-recall/query.py "how do the review protocol and the
unattended Skill render their harness citations in an adopter whose review-harness kit is renamed"
--terms "derive_kit_paths citation TOOL_ROOT rendered receipt resolve_kit_dir check-protocol-parity
adopt-unattended review-harness SKILL render"`
