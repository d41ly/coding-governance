# TOOL-aNamedGesture-1 — the authorizing parameter is a declared conf key that carries the build

**Status:** SPECCED · rev-1 · 2026-08-25 · node a · Tier-2 · base 381008a1 · streams tooling · order 1

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Name the parameter that authorizes a prompt-mode unattended run, as a project-declared conf key
rendered into the Skill, and give it a value that carries the build's scope — a prompt file or a
literal prose block. Today the Skill says `the authorizing parameter` and no file in this repository
says what it is.

## 2. Scope (IN)

- **S1** — a new `.unattended.conf` key `AUTH_PARAM`, declared BLANK in both shipped confs
  (`tools/unattended/.unattended.conf.example` and this repo's `.unattended.conf`) and documented
  with a row in section 8 of `tools/unattended/PROTOCOL.template.md`. Check 22 of
  `check-unattended.sh` joins those two populations in both directions, so neither half is optional.
- **S2** — `tools/unattended/adopt-unattended.sh` pre-sets `AUTH_PARAM` to the kit default BEFORE
  sourcing the conf, and re-normalises a blank or absent value back to that default AFTER the source.
  The pre-set is the only place in the repository where the literal is written.
- **S3** — `render()` gains an eighth substitution, `{{AUTH_PARAM}}`, and the token renders at two
  sites in `tools/unattended/SKILL.template.md`: the `## Which path` routing row for the prompt path,
  and the fence that opens `## Start a run from a PROMPT`.
- **S4** — the VALUE GRAMMAR is stated in the Skill. The parameter takes one argument, which is
  either a path to a readable file holding the prompt, or a literal prose block stating the build.
  The discriminator is whitespace: a value containing whitespace is prose, a value containing none is
  a path. A whitespace-free value that does not resolve to a readable file is a REFUSAL and not a
  one-word prose block.
- **S5** — the prompt path's step 3 is amended. Where the value was a path, the run carries the
  file's CONTENT verbatim into the build README under the existing heading, and records the path it
  came from beside it. The build folder is the authorization, so it may not authorize by reference to
  a file that can change after the run starts.
- **S6** — `KIT_UNATTENDED_VERSION` moves to the next vintage in `tools/unattended/unattended.sh`,
  with the matching `gov:kit` marker in `SKILL.template.md`, because the kit's behaviour moved.
- **S7** — `tools/unattended/kit.toml` gains `AUTH_PARAM` in the SKILL render's `placeholders` list,
  and `ANCHOR_SCOPE` alongside it. That list has been missing `ANCHOR_SCOPE` since
  `TOOL-aPromptedMandate-5` landed the seventh placeholder, and a declared population undercounting
  the real one is the defect the list exists to prevent.
- **S8** — both rendered artifacts are regenerated: `.claude/skills/unattended/SKILL.md` and
  `memory/guides/UNATTENDED-PROTOCOL.md`. `bash tools/unattended/adopt-unattended.sh --check` is the
  observation that they match.

## 3. Non-goals (OUT)

- **No machine verification that the invocation carried the parameter.** No script in this kit sees
  the invocation, so no check can. The parameter is the authorization GESTURE; the anchor is still
  the pushed build folder, and protocol section 9 is unchanged.
- **No new gate leg and no new `fail` call site.** A new call site costs a row in
  `memory/project/unarmed-branches.txt` and an `ARMS_FLOORS` bump. The render's existing
  surviving-placeholder arm already catches the only machine-visible failure this key has.
- **No change to the slug or recipe start paths**, and none to the playbook-authoring path, which
  routes into the prompt path rather than restating its fence.
- **No driver change.** `unattended.sh` moves by one version constant and nothing else.
- **No authorization LEVEL vocabulary.** The parameter has one spelling and one argument, not a set
  of grades. A follow-up that wants grades is a different unit with a different refusal.

## 4. Design

### Data model

`AUTH_PARAM` is a single token. Its resolution is the same three-step seam `ANCHOR_SCOPE` uses in
`adopt-unattended.sh`: a pre-set default, then `. "$CONF"`, then a normalisation that runs after the
source. The normalisation is what makes a blank declaration mean the default rather than a hole,
because a blank line in a sourced conf overrides a pre-set variable WITH BLANK.

`TOOL-aWrittenMethod-1` says an interpolated key defaults to its own placeholder so an undeclared
value reds. `AUTH_PARAM` is the second declared exception, after `ANCHOR_SCOPE`, and for the same
reason that key gives: an adopter who declares nothing must receive a working Skill rather than a red
bar naming a key they have never heard of. The exception is legitimate here because a kit-owned
default EXISTS and is correct; the rule binds keys whose value only the project can know.

### The value grammar

The parameter takes one argument and there are exactly two readings of it.

| Value shape | Reading | What the run does |
|---|---|---|
| contains whitespace | a literal prose block | carries it verbatim into the build README |
| no whitespace, resolves to a readable file | a path | reads it, carries the CONTENT, records the path |
| no whitespace, resolves to nothing | a refusal | says the path did not resolve and does not start |

The whitespace discriminator is chosen over a file-existence test alone because a typo'd path must
not silently become the build's entire scope statement. A prose block stating a build is multi-word
in every case; a path containing whitespace is already refused elsewhere in this same adopter, for
the kit-path argument, so the rule is not new to this file.

### Why the value is carried by content

The build folder IS the authorization the merge bar re-derives. A README naming a prompt file instead
of holding its bytes would authorize by reference to something editable after the run began, which is
the property `playbook:` resolution at BASE exists to deny on the recipe path. Recording the path
beside the content keeps the provenance without keeping the dependency.

### Files touched (estimate)

`tools/unattended/adopt-unattended.sh` (the pre-set, the normalisation, the eighth substitution) ·
`tools/unattended/SKILL.template.md` (routing row, prompt-path fence, step 3, the version marker) ·
`tools/unattended/PROTOCOL.template.md` (the section 8 row) ·
`tools/unattended/.unattended.conf.example` · `.unattended.conf` · `tools/unattended/kit.toml` ·
`tools/unattended/unattended.sh` (the version constant alone) · `.claude/skills/unattended/SKILL.md`
and `memory/guides/UNATTENDED-PROTOCOL.md` (both rendered) · `memory/map/features/unattended.md`
(prose refresh on touch) · `memory/project/readme-contract.txt` (a bound row for this build).

### Alternatives rejected

**A bare gesture token with no argument**, which was the opening design and defaulted to a
thoroughness word. Rejected by the owner at kickoff: it named a degree rather than a grant, so no
value of it was obviously wrong, `GATE_FULL` already means something else in this tree, and it left
the build's prose sitting beside the parameter rather than inside it.

**Keeping the parameter kit-owned with no conf channel**, the way `AUTH_MODES` and
`SECOND_ANCHOR_MODES` are. Rejected because the argument that makes those kit-owned — an
adopter-declarable set is an adopter-reopenable hole — does not transfer. The mode VOCABULARY is a
security surface; the spelling of a token an owner types is not, and a project whose prose routinely
contains the default has a legitimate reason to change it.

**Declaring the literal in both shipped confs rather than blank.** Rejected: it puts the same string
in three files with no gate joining them, which is the `two-answers-to-one-question` class this
diff's own bug-class checklist selects.

## 5. Production-readiness checklist

- security — the parameter is the GESTURE, not the authorization; the anchor is unchanged. The
  failure directions are analysed in section 8, fork F2.
- perf / scale — N/A: one string substitution in a render that already performs seven.
- a11y — N/A: no user interface.
- i18n — N/A: the token is an ASCII literal an owner types, and the conf can change it.
- error / empty / loading states — a blank declaration normalises to the default; an unfilled
  placeholder reds the render's existing arm; an unresolvable path value is the S4 refusal.
- observability — the rendered Skill states the token, so the value is readable in the adopter's
  tree without running anything.
- risks (concurrency, data-loss, rollback hazards) — none: the change adds no write path. Rollback is
  a revert plus a re-render.
- testing + left-shift gates — AC5 stages the check-22 break and observes RED before the unit lands,
  which is this repo's rule for a gate arm newly relied on.
- migration / rollback — an existing adopter who never declares the key receives the default, so the
  kit update is not a breaking one. Section 8 fork F1 records the evidence.
- user docs — the protocol's section 8 key table is the adopter-facing documentation and is in scope
  as S1.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs on this tree, it exits 0,
  and `grep -nE '\{\{[A-Z_]+\}\}' .claude/skills/unattended/SKILL.md` prints nothing.
- **AC2** — When the rendered Skill is grepped for the token, it appears at BOTH the routing row and
  the prompt-path fence in `.claude/skills/unattended/SKILL.md`.
- **AC3** — When `adopt-unattended.sh` renders against a scratch tree whose `.unattended.conf`
  declares `AUTH_PARAM=""`, the rendered Skill carries the kit default and not an empty string.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs with the new key declared in
  `.unattended.conf` and its row present in section 8, it exits 0.
- **AC5** — When the section 8 row for `AUTH_PARAM` is deleted from
  `memory/guides/UNATTENDED-PROTOCOL.md`, `check-unattended.sh` fails naming check 22. Observed RED,
  then restored — a gate arm this unit relies on and has never seen fail is an assertion about
  nothing.
- **AC6** — When the rendered Skill is read at `## Start a run from a PROMPT`, it states the
  path-or-prose grammar and the refusal for an unresolvable whitespace-free value.
- **AC7** — When `bash tools/unattended/adopt-unattended.test.sh` runs, it exits 0.
- **AC8** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, every leg is green.

## 7. Gates

`unattended kit gate` (`bash tools/unattended/check-unattended.sh`) · `unattended skill wiring`
(`bash tools/unattended/adopt-unattended.sh --check`) · `playbook validity gate` · the memory-tree
hygiene gate · the codebase-map coverage and freshness legs · `govkit` selfcheck and selftest ·
`tools/check-kit-versions.sh` · the kickoff-manifest ratchet. The full bar is
`bash tools/run-gates/run-gates.sh`; the leg list is single-sourced from `tools/gate-legs.json`.

## 8. Open questions

- **F1 · FACT-QUESTION · does an existing adopter who never declares `AUTH_PARAM` go red on the kit
  update?** The probe is a read of `adopt-unattended.sh` and `check-unattended.sh`: whether the
  pre-set default survives an absent declaration, and whether check 1's required-key loop or check
  22's reverse direction name a key the adopter has not set. Liveness: the same read reports a red
  for a genuinely required key, which `HALT_FLOOR` demonstrates.
  RESOLVED (agent, 2026-08-25, delegated): the default survives. Check 1's loop is a fixed list this
  unit does not join, and check 22's project direction grades only keys a project DOES set. An
  adopter who declares nothing renders the default and stays green.

- **F2 · what do the failure directions of this key actually buy an attacker?** A misspelled key name
  is caught by check 22's project direction, which reds any key the project sets and the protocol
  does not document. A blank value normalises to the default rather than to an empty token, so the
  fence can never render as a sentence naming nothing. An adopter-chosen value that appears in
  ordinary prose is the one real hazard, and it is the adopter's to price — which is the argument for
  the key being project-declarable at all.
  RESOLVED (agent, 2026-08-25, delegated): normalising blank to the default is fail-CLOSED, because
  the alternative is a fence naming nothing, which authorizes every invocation rather than none.

- **F3 · which token, and does it collide?** Probed 2026-08-25 by grepping the whole tree and
  enumerating the driver's argument arms; the control found 37 verbs and none of them is the chosen
  token, nor is any of them a prefix of it.
  RESOLVED (owner, 2026-08-25): the token names the mode it starts, so the gesture and the
  `authorized-by:` value it produces are one word.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, after the owner replaced the opening thoroughness-word default
  with a mode-naming token and gave the parameter a path-or-prose argument.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a project-declared conf key rendered into the unattended
Skill"` returns `.unattended.conf` as the affordance seam and no symbol that fits — the render is a
bash pattern substitution in one file, not a library. The seam this unit extends is therefore
`render()` in `tools/unattended/adopt-unattended.sh`, together with the pre-set block above it.
`python tools/memory-recall/query.py` was run with the terms `authorizing parameter prompt mode
authorization gesture unattended conf key render placeholder adopter Skill declared`; it returned
`TOOL-aPromptedMandate-5` (the prompt path and its unfilled S2), `TOOL-aWrittenMethod-1` (the
placeholder-default rule this unit takes an exception to), `TOOL-dNarrowedAnchor-1` (the per-mode
anchor) and `TOOL-aUnmannedHelm-7` (parity is not placeholder completeness). All four were read
against source before this spec was written; none of them disagreed with the tree.
