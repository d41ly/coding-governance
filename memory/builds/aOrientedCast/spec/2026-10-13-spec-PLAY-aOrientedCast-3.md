# PLAY-aOrientedCast-3 — the charter's `agent` and `returned` micro-formats, mandatory for every agent a turn dispatches or receives

**Status:** OPEN · rev-1 · 2026-10-13 · node a · Tier-2 · base 646d4a73 · streams playbook · order 21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md](../prompts/2026-10-13-prompt-TOOL-aOrientedCast-20-1-spec-brief.md) | journal | TOOL-aOrientedCast-19 TOOL-aOrientedCast-20 TOOL-aOrientedCast-21 PLAY-aOrientedCast-2 |

<!-- /gen:spec-records -->

## 1. Goal

The owner's third addendum makes every agent a session dispatches or receives visible in its output:
its role, effort, model, unit, the prompt it was oriented with, its write class and gate allowlist,
its run and agent ids, and on return what it produced, its wall time and its tokens. This unit puts
the two line shapes into the charter's micro-format fence and a rule making them mandatory, so the
roles kit's verb fills them and `format-guard` reads them from one source. The template moves to
v4.4, the build's one move of it.

## 2. Scope (IN)

- **S1** — The `<!-- microformats -->` fence of `coding-governance-agents.template.md` (`:55-67`)
  gains, on the line after the `SPEC` definition (`:64`), a `kit:roles` fence holding the `agent`
  and `returned` definitions of §4 "The new text", block E. Observed by AC1, AC2 and AC8.
- **S2** — The one-line region after the fence (`:69-79`) gains, on the line after `[events]`
  (`:71`), a `kit:roles` fence holding the `[agents]` rule of block F. Observed by AC1 and AC2.
- **S3** — The template marker (`:9`) moves from `v4.3` to `v4.4`: the playbook kit's one version
  move for this build, dating `PLAY-aOrientedCast-2`'s edit as well. Observed by AC4.
- **S4** — `AGENTS.md` is re-rendered with `bash tools/playbook/adopt-playbook.sh --target .`, and
  the agent types are left as they are. Observed by AC2 and AC6.
- **S5** — Both size subjects re-record their row in `tools/template-size-highwater.txt` with
  `--bump`, inside the ceiling §8 F1 settles. Observed by AC5.
- **S6** — The same commit re-stamps `last-audit` in `memory/guides/SESSION-KICKOFF.md`, whose
  `watch:` list holds the template, as `PLAY-aOrientedCast-2` S7 states the rule. Observed by AC7.

## 3. Non-goals (OUT)

- Deriving or printing either line, and the per-build agent ledger: `TOOL-aOrientedCast-20`'s.
- Refusing a final message that omits a line: `TOOL-aOrientedCast-21`'s.
- Any edit to a fence reader. `tools/check-microformats.sh` derives its head set from the block and
  pins only `committed` (`:30`, `:56`); `tools/runlog/prose.py` requires only `BUILD` and `SPEC`
  (`:71`); `tools/hooks/format-guard.js` requires `BUILD`, `SPEC`, `committed` and `merged`
  (`:162`). None of the three lists a head it would have to learn, so none moves here.
- A help page. The fields and where each comes from are the verb's to describe, so
  `TOOL-aOrientedCast-20` edits `help/roles.md`.
- Raising `AGENTS.md`'s ceiling without the owner's ruling (§8 F1).
- Rewording any other charter rule to make room.

### Edges

- **consumes-from** `PLAY-aOrientedCast-2` — the template carrying its blocks A to C, and
  `AGENTS.md` rendered with the role roster. This unit's bytes are measured on top of those, and its
  version move dates that unit's template edit.
- **hands-off** `TOOL-aOrientedCast-20` — the verb that fills every placeholder of both definitions
  by name, `<unit-id|label>` and `<run-id|direct>` included, reading the definitions from the
  governing doc rather than restating them; and the help page that says what each field means.
- **hands-off** `TOOL-aOrientedCast-21` — the `format-guard` arm that reads the `agent` and
  `returned` definitions from the fence of `AGENTS.md`, as it reads its other four, and treats a
  charter without them as a charter that asks for no line.

## 4. Design

### Evidence

Read at `1e89fa5cd` on 2026-10-13, the run branch's HEAD, where the template is v4.3 and
`PLAY-aOrientedCast-2` has not landed. Its block A adds three lines above the fence, so the builder
finds each site below by its text, not its number.

- The fence pair sits at `coding-governance-agents.template.md:55` and `:67`, eleven definitions
  between, `SPEC` at `:64`. The second one-line region is `:69-79`, `[events]` at `:71`, `[r1]` at
  `:72`, `[grammar]` at `:73`. No line carries an `[agents]` tag.
- `[grammar]` (`:73`): a head keyword, the ` — ` joiner, fields separated by ` · `. `[r1]` (`:72`):
  each shape is emitted as a bare `- ` list item at column 0.
- `tools/check-microformats.sh` grades every `- ` backticked line between the fence markers
  (`:46-47`): exactly one joiner (`:66-70`), a head with no space (`:79-81`), no parenthesis outside
  markdown-link syntax (`:83-86`), no `: ` label (`:88-90`), no `;` or bare `|` outside a placeholder
  (`:96-104`), lowercase placeholders (`:106-113`). A `kit:` marker line is not a definition line.
- The renderer accepts a `kit:` fence anywhere and strips a surviving one's markers
  (`check_fences` and `remove_fenced`, `tools/playbook/render_playbook.py:579`, `:610`).
- Three readers take shapes from the rendered fence, each keyed by the text before the joiner:
  `readCharterShapes` (`tools/hooks/format-guard.js:147-166`), `read_charter_shapes`
  (`tools/runlog/prose.py:55-74`), and the charter-copy fixture of `tools/hooks/format-guard.test.sh`
  (`:182-184`), which copies gov's own `AGENTS.md`. Each ignores a head it does not require.
- Every section 1 rule line is a tag a role may cite (`RULE_LINE_RE`, `tools/roles/roles_lib.py:56`),
  and the second region sits inside section 1, so `[agents]` becomes citable. No role cites it, so
  no agent type moves (AC6).

### The new text

**Block E**, inserted after `:64`, inside the fence:

```markdown
<!-- kit:roles -->
- `agent — <role> · effort <level> · model <model> · <unit-id|label> · prompt [<name>](<path>) · writes <class> · gates <legs|none> · run <run-id|direct>/<agent-id>`
- `returned — <role> · <outcome> · <wall> · <tokens> out · run <run-id|direct>/<agent-id>`
<!-- /kit:roles -->
```

**Block F**, inserted after `:71`, inside the one-line region:

```markdown
<!-- kit:roles -->
- [agents] Every agent a turn dispatches gets its `agent` line and every agent it receives its `returned` line, both derived by the roles kit and never typed.
<!-- /kit:roles -->
```

**Block G**, at `:9`: `<!-- governance-template: v4.4 -->`.

The draft shapes of the addendum change in two places. `<unit-id>` becomes `<unit-id|label>`,
because a harness agent such as a spec group or a lens reviewer serves no single unit and the line
then carries the agent's label. `<run-id>` becomes `<run-id|direct>`, because an `Agent` call starts
no workflow run, so a direct spawn's run field is the literal `direct` (§8 F2). Both alternations sit
inside a placeholder, the one place `check-microformats.sh` admits a pipe. The order of the fields
is the owner's, and every field is a run carrying no ` · `, which is what each reader's derived
pattern requires of a value.

Each definition passes every predicate the gate holds, read against its source: one joiner, the
heads `agent` and `returned`, the only parentheses in `[<name>](<path>)`, no colon, no semicolon,
both pipes inside placeholders, every placeholder lowercase. The rule renders at 155 characters, under
the one-line region's 200 (`ONE_LINE_MAX`, `render_playbook.py:126`).

### Why the blocks are fenced

The lines are derived by the roles kit's verb, so a target without that kit has nothing to derive
them with, and a charter demanding them there would demand typed lines. With the kit dropped, the
render is the v4.3 render apart from the marker (AC3). The rule's text names the kit rather than its
verb: the verb is `TOOL-aOrientedCast-20`'s, ordered after this unit, and the `/build` Skill and the
help page that unit edits are where an agent learns its name.

### Bytes, measured

PINNED on 2026-10-13 at `1e89fa5cd`. Block E costs 272 bytes with its newlines and block F 156;
the four marker lines render to nothing. Gov's `AGENTS.md` is 14762 bytes. `PLAY-aOrientedCast-2`
§4 "Bytes, measured" projects 14918 without the roster, and the roster measures 1383 bytes from
`handoff.py roster` here, so the charter reaches 16301 before this unit and 16729 after it. The
ceiling is 16384 (`tools/template-size-limits.txt:65`), so this unit cannot land under it: 345 bytes
over, which §8 F1 puts to the owner. The template grows by about 510 bytes to roughly 13700 against
its 49152 ceiling (`:33`). The builder re-measures both after `PLAY-aOrientedCast-2` lands.

### Kit version

The playbook kit's carrier is the marker at `:9`, read through `version_from`
(`tools/govkit/entries/playbook.kit.toml:6`); its render at `AGENTS.md:10` follows. This unit is the
last of the set to touch the template, so its bump is the set's one move, `v4.4`, and it dates
`PLAY-aOrientedCast-2`'s commit too: the epoch leg clears a move once a later commit bumps the
version (`derive_epoch_state`, `tools/govkit/govkit.py:12976`). v4.4 keeps major 4, so the parity
pair with `TEMPLATE_MAJOR` holds.

### Probes

Run from the repository root on the unit's commit.

```bash
# P3 (AC3): with the roles kit dropped, the template renders as its parent did, marker aside.
python -c "import sys,subprocess as s;sys.path.insert(0,'tools/playbook');import render_playbook as r;g=lambda c:s.run(['git','show',c+':coding-governance-agents.template.md'],capture_output=True,text=True,encoding='utf-8').stdout.replace('\r','');d={('kit','roles')};assert r.remove_fenced(g('HEAD'),d).replace('governance-template: v4.4','governance-template: v4.3')==r.remove_fenced(g('HEAD~1'),d),'a target without roles renders a change';print('drop ok')"

# P4 (AC8): the fence's consumers parse both shapes, and a line without its run field fails.
python -c "import sys,pathlib;sys.path.insert(0,'tools/runlog');import prose as p;s,e=p.read_charter_shapes(pathlib.Path('AGENTS.md'));a='- agent — gov-builder · effort high · model claude-opus-5-5 · TOOL-tFix-1 · prompt [x.md](memory/builds/tFix/prompts/x.md) · writes product · gates none · run wf_1/a1';r='- returned — gov-builder · wrote 3 files · 7m47s · 41.2k out · run direct/a1';assert not e,e;assert s['agent'][1].match(a) and s['returned'][1].match(r);assert not s['agent'][1].match(a.rsplit(' · ',1)[0]);print('shapes ok')"
```

### Inventory

Minted: the heads `agent` and `returned`, the section 1 tag `agents`, the placeholder alternations
`<unit-id|label>` and `<run-id|direct>`, and the template version `v4.4`. No function, file or
conf key is minted, so no `.lexicon.conf` cell grades a name here.

### Files touched (estimate)

`coding-governance-agents.template.md` · `AGENTS.md` · `tools/template-size-highwater.txt` · `tools/template-size-limits.txt` · `memory/guides/SESSION-KICKOFF.md`

The ceiling row is touched only under §8 F1 (a), in the commit that records the owner's ruling.

### Rollout

1. Apply blocks E to G to the template.
2. Render: `bash tools/playbook/adopt-playbook.sh --target .`.
3. `python tools/roles/render_agents.py --check`; on any drift, stop and report (AC6).
4. Measure `AGENTS.md` with carriage returns stripped. Past the ceiling §8 F1 settles, commit
   nothing and return the figure.
5. `bash tools/check-template-size.sh --bump`, then `bash tools/check-template-size.sh --bump AGENTS.md`.
6. Re-stamp `last-audit` as `PLAY-aOrientedCast-2` §4 "Rollout" step 7 states, check 9's count included.
7. Commit once, with the unit id in the subject.

Rollback is a revert of that commit. An adopter's seeded template keeps rendering without the blocks
until its owner merges them, as for `PLAY-aOrientedCast-2`'s blocks.

### Alternatives rejected

- **Extending `[events]` instead of a new rule.** At 188 characters it has no room for the two
  heads under the 200-character one-line limit, and a reworded `[events]` still leaves the shapes
  over the ceiling, so it buys nothing §8 F1 does not already decide.
- **Unfenced blocks.** A charter without the roles kit would demand lines nothing derives.
- **Labels dropped from the agent shape**, such as `effort` and `model`. It saves about 40 bytes,
  far short of the overage, and a bare `high` beside a bare model name reads ambiguously.
- **v5.0.** The change is additive, and a new major breaks the parity pair with `TEMPLATE_MAJOR`.

## 5. Production-readiness checklist

- security — no code and no write path. The lines carry ids, a role, a model and a repo-relative
  prompt path, and no secret. Claude Code's `Agent` result asks the main loop not to quote an agent
  id in a reply to the user; the owner's third addendum asks for the ids, and this unit follows the
  owner.
- perf / scale — every session reads `AGENTS.md`, which grows by 428 bytes (§4 "Bytes, measured").
- error / empty / loading states — a target without the roles kit renders none of this (AC3); a
  definition breaking the grammar reds `micro-format definitions` at the close.
- observability — the render's notes, and P4's line.
- risks — the charter ceiling (§8 F1). A role that later cites `agents` changes its agent type,
  which `render_agents.py --check` reports. Seeded templates lag, as for `PLAY-aOrientedCast-2`.
- testing — P3, P4 and the greps of §6; the size, line-length, micro-format, parity, render,
  placeholder, epoch, version, manifest and roles legs at the close. No new arm.
- migration — gov renders at this commit; adopters merge the blocks into their seed.
- user docs — the help page is `TOOL-aOrientedCast-20`'s (§3).

## 6. Acceptance criteria

No criterion runs a gate leg, a suite or a `--selftest` flag. Each reads a file, runs the render's
write mode or runs a probe of §4.

- **AC1** — When `grep -n "kit:roles\|SPEC — \|^- .agent — \|^- .returned — \|\[events\]\|\[agents\]\|microformats -->" coding-governance-agents.template.md`
  runs, the `agent` and `returned` definitions sit once each in a `kit:roles` pair whose opener is the
  line after the `SPEC` definition, inside the microformats fence; and `[agents]` sits once in a
  `kit:roles` pair whose opener is the line after `[events]`.
  Red when: a block is unfenced, outside its fence or region, or out of place.
- **AC2** — When `bash tools/playbook/adopt-playbook.sh --target .` runs on the unit's commit, it
  exits 0, `git diff --quiet -- AGENTS.md` exits 0 afterwards, `grep -c "kit:roles" AGENTS.md` prints
  0, and `grep -c "^- \[agents\] \|^- .agent — \|^- .returned — " AGENTS.md` prints 3.
  Red when: the committed charter differs from a fresh render, a marker survives, or a block is
  missing from the render.
- **AC3** — When probe P3 runs on the unit's commit, it prints `drop ok`.
  Red when: a target without the roles kit renders anything this unit added beyond the marker.
- **AC4** — When `git show HEAD:coding-governance-agents.template.md | grep -c "governance-template: v4.4"`
  and the same over `AGENTS.md` run, each prints 1, and both files at `HEAD~1` carry `v4.3`.
  Red when: the template's bytes moved without its marker, or the render's marker differs.
- **AC5** — When `tr -d '\r' < AGENTS.md | wc -c` runs on the unit's commit, it prints at most the
  `AGENTS.md` row of `tools/template-size-limits.txt`, and each of the two files equals its row in
  `tools/template-size-highwater.txt`.
  Red when: the charter passes its declared ceiling, or a row was not re-recorded.
  figure: DERIVED at observation; §4's 16729 is PINNED at `1e89fa5cd`.
- **AC6** — When `python tools/roles/render_agents.py --check` runs after the re-render, it exits 0
  and names no `drift`, `missing` or `stale` path.
  Red when: the new rule moved an agent type.
- **AC7** — When `git show` reads `memory/guides/SESSION-KICKOFF.md` at `HEAD` and `HEAD~1`, the
  two `last-audit:` lines differ and the first ends with the sha `git rev-parse HEAD~1` prints.
  Red when: the commit stages a watched file with no new stamp.
- **AC8** — When probe P4 runs on the unit's commit, it prints `shapes ok`.
  Red when: a reader of the fence cannot key either head, a well-formed line fails its shape, or a
  line without its run field passes.

## 7. Gates

`template size <=48KiB` · `charter size` · `line length` · `micro-format definitions` · `playbook parity` · `playbook render wiring` · `playbook placeholder catalogue` · `kickoff-manifest ratchet` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers` · `dead-path carriers (deleted files still named)` · `agent-instructions wiring` · `agent-cap restatement` · `format-guard self-test` · `roles catalogue` · `roles render wiring` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

This unit adds no gate arm. `format-guard self-test` is named because its fixture charter is a copy
of gov's `AGENTS.md`. The main loop runs the legs once, at the close; no pass runs one.

## 8. Open questions

- **F1 — `AGENTS.md` measures 16729 bytes after this unit, past its 16384-byte ceiling. What gives?**
  (a) Raise the `AGENTS.md` row of `tools/template-size-limits.txt` to 17408, one KiB more, with the
  owner's ruling recorded in `memory/DECISIONS.md`. That file and the size gate's own message make a
  raise an owner decision: M3 veto 2, so no delegated resolver exists.
  (b) Reword `[events]` to carry the two heads and drop the field labels: still about 190 bytes over,
  so AC5 fails: veto 1.
  (c) Trim other charter rules, or move the role roster out: a §3 non-goal and another unit's
  section: veto 1.
  (d) Land nothing, and leave the owner's addendum unshipped.
  Recommendation: (a). 17408 leaves 679 bytes for the next addition, and every byte of the growth is
  a line the owner asked for. This fork is the owner's; the builder takes no option before the ruling.
- **F2 — What does a direct spawn's `agent` line carry as its run id?**
  (a) The literal `direct`; (b) the session id; (c) the `Agent` call's tool-use id.
  (b) adds 36 characters to every line for a value every agent of the session shares. (c) names an
  internal id no surface shows the owner. With (a) the agent id alone still finds the transcript,
  and a reader tells a harness agent from a direct one at a glance.
  Recommendation: (a).
  RESOLVED (agent, 2026-10-13, delegated): (a), spelled `<run-id|direct>` in block E.

## 9. Revision log

- rev-1 · 2026-10-13 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "read a Claude Code session transcript and its subagent
workflow journal to report each agent's model, usage and timestamps"` ranked the fence readers
`read_charter_shapes` in `tools/runlog/prose.py` and `readCharterShapes` in
`tools/hooks/format-guard.js` among its candidates. The seam this unit extends is the micro-format
fence itself, the one source those two readers and `tools/check-microformats.sh` already key on, and
the `kit:` fence pass of `tools/playbook/render_playbook.py:579-627`, which `PLAY-aOrientedCast-2`
also extends. No reader needs an edit, verified against each one's required-head list. The recall
probe surfaced the addendum's record and the brief, read against source: the record's note that no
file records effort no longer holds on Claude Code 2.1.295, which `TOOL-aOrientedCast-20` takes up.

Recall terms used: `agent transcript journal workflow subagent usage effort model ledger format-guard microformat runlog`
