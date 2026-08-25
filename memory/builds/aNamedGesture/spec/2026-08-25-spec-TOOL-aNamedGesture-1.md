# TOOL-aNamedGesture-1 — the authorizing parameter is a declared conf key that carries the build

**Status:** SPECCED · rev-2 · 2026-08-25 · node a · Tier-2 · base 381008a1 · streams tooling · order 1

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
  `check-unattended.sh` joins those populations in three directions, so neither half is optional.
- **S2** — `tools/unattended/adopt-unattended.sh` pre-sets `AUTH_PARAM=""` before sourcing the conf
  and derives `AUTH_EFFECTIVE` in a post-source `case`, byte-for-byte the seam `ANCHOR_SCOPE` uses at
  that file's lines 119 to 134. The kit default literal appears exactly ONCE, in that `case`.
- **S3** — the adopter REFUSES a malformed value, with an `echo` and an `exit`, in the shape the
  existing whitespace refusal for the kit path already uses. A value is malformed when it does not
  begin with `-`, or when it contains whitespace, a pipe, or a backtick. The reasons are in section 4.
- **S4** — `render()` gains an eighth substitution, `{{AUTH_PARAM}}`, appended LAST, after
  `{{ANCHOR_SCOPE}}`.
- **S5** — the token renders at two sites in `tools/unattended/SKILL.template.md`: the `## Which path`
  routing row for the prompt path, and the fence that opens `## Start a run from a PROMPT`. Routing
  row 4 also declares `prompt` and is handled by S6's pointer rather than by a third substitution.
- **S6** — the VALUE GRAMMAR is stated in the Skill. The parameter takes one argument, which is
  either a path to a readable file holding the prompt, or a literal prose block stating the build.
  The discriminator is whitespace: a value containing whitespace is prose, a value containing none is
  a path. A whitespace-free value that does not resolve to a readable file is a REFUSAL and not a
  one-word prose block. Routing row 4 gains one clause saying it inherits this fence.
- **S7** — the prompt path's step 3 is amended. Where the value was a path, the run carries the
  file's CONTENT verbatim into the build README under the existing heading, and records the path it
  came from beside it. The build folder is the authorization, so it may not authorize by reference to
  a file that can change after the run starts.
- **S8** — the kit vintage moves across EVERY carrier `tools/check-kit-versions.sh` asserts, which is
  nine lines in six tracked source files, not the two an earlier revision of this spec named. The
  inventory is in section 4.
- **S9** — `tools/unattended/kit.toml` gains `AUTH_PARAM` in the SKILL render's `placeholders` list
  and in `[config] optional_keys`, and `ANCHOR_SCOPE` in both. `ANCHOR_SCOPE` has been absent from
  the placeholders list since `TOOL-aPromptedMandate-5` landed the seventh substitution.
- **S10** — the SECOND hand-kept renderer is updated: the `sed` chain in
  `tools/unattended/cross-component.test.sh` gains a `{{AUTH_PARAM}}` entry. Nothing reds if this is
  missed, which is why it is a numbered scope item rather than a step.
- **S11** — `tools/unattended/adopt-unattended.test.sh` gains an arm that seeds `AUTH_PARAM=""` and
  asserts the default renders. Without it the whole suite passes with S2's normalisation deleted,
  because the fixture conf declares no such key and the pre-set alone satisfies every existing
  assertion.
- **S12** — all THREE installed artifacts are re-installed by RUNNING `adopt-unattended.sh`, never by
  hand: `.claude/skills/unattended/SKILL.md`, `memory/guides/UNATTENDED-PROTOCOL.md`, and
  `memory/guides/PLAYBOOK-TEMPLATE.md`. The third is byte-diffed by the same `--check` leg and drifts
  on the version bump alone.
- **S13** — the kickoff manifest is re-audited and `last-audit` re-stamped.
  `memory/guides/SESSION-KICKOFF.md` carries `.unattended.conf` in its `watch:` list, so this unit's
  conf edit obliges the ratchet.

## 3. Non-goals (OUT)

- **No machine verification that the invocation carried the parameter.** No script in this kit sees
  the invocation, so no check can. The parameter is the authorization GESTURE; the anchor is still
  the pushed build folder, and protocol section 9 is unchanged.
- **No gesture for `recipe`.** `SECOND_ANCHOR_MODES` is `prompt recipe`, so `recipe` is the other
  mode that may author the folder authorizing it, and this unit gives it no token. The asymmetry is
  deliberate and is recorded here because the prompt fence's claim that the parameter IS the
  authorization gesture is therefore true of one of the two self-authoring modes, not both. A gesture
  for `recipe` is a separate unit.
- **No `{{AUTH_PARAM}}` token and no rendered VALUE in the protocol or playbook templates.** Both are
  byte-COPIED rather than rendered, both declare `placeholders = []`, and no check greps either for a
  surviving brace shape. A placeholder written there would ship verbatim into every adopter's tree
  with nothing to catch it. Section 8's row names the KEY and nothing else.
- **No new gate leg and no new `fail` call site.** `adopt-unattended.sh` deliberately defines no
  `fail()` helper — its own line 14 says so — and the file is absent from `ARMS_FLOORS`, so S3's
  refusal costs no arm.
- **No change to the slug or recipe start paths**, and no restatement of the fence in the
  playbook-authoring path, which routes into the prompt path.
- **No driver change.** `unattended.sh` moves by its version constant and marker and nothing else.
- **No authorization LEVEL vocabulary.** The parameter has one spelling and one argument, not a set
  of grades.

## 4. Design

### Data model

`AUTH_PARAM` is a single token. Its resolution copies `ANCHOR_SCOPE`'s three-step seam in
`adopt-unattended.sh`: pre-set to empty, then `. "$CONF"`, then a `case` that derives an EFFECTIVE
value. Deriving rather than normalising in place is what keeps the literal to one occurrence — a
pre-set default plus a blank-normalisation writes the same string twice, which is the
`two-answers-to-one-question` class this diff's own checklist selects.

`TOOL-aWrittenMethod-1` says an interpolated key defaults to its own placeholder so an undeclared
value reds. `AUTH_PARAM` is the second declared exception, after `ANCHOR_SCOPE`, and for the reason
that key gives: an adopter who declares nothing must receive a working Skill rather than a red bar
naming a key they have never heard of. The rule binds keys whose value only the project can know, and
this one has a correct kit-owned default.

### Why the substitution goes LAST

`render()` performs its substitutions in sequence over one string. A conf value containing another
key's placeholder text would be re-substituted by any pass that follows it. Appending
`{{AUTH_PARAM}}` after `{{ANCHOR_SCOPE}}` means such a value survives into the output as a brace
shape, where the existing surviving-placeholder arm reds it. Order is the fail-closed direction here,
not a preference.

### The value guard

Three characters and one prefix are refused, each for a reason that is not taste.

| Refused | Why |
|---|---|
| a value not beginning with `-` | check 24 reads the LAST whole-cell backticked lowercase token of each routing row as an authorization mode. A bare word rendered as a cell could be picked up as one. A leading hyphen cannot match `[a-z]`. |
| whitespace | the token is one argv word; a value with a space renders a fence naming two things and reads as prose |
| a pipe | the token renders inside a markdown table row, which a pipe closes |
| a backtick | the token renders inside a code span, which a backtick closes |

The refusal is an `echo` and an `exit`, matching the existing refusal for a kit path containing
whitespace. It is not a `fail()` call and owes no arm.

### The value grammar

The parameter takes one argument and there are exactly three readings of it.

| Value shape | Reading | What the run does |
|---|---|---|
| contains whitespace | a literal prose block | carries it verbatim into the build README |
| no whitespace, resolves to a readable file | a path | reads it, carries the CONTENT, records the path |
| no whitespace, resolves to nothing | a refusal | says the path did not resolve and does not start |

The whitespace discriminator is chosen over a file-existence test alone because a typo'd path must
not silently become the build's entire scope statement. A prose block stating a build is multi-word
in every case.

### Why the value is carried by content

The build folder IS the authorization the merge bar re-derives. A README naming a prompt file instead
of holding its bytes would authorize by reference to something editable after the run began, which is
the property `playbook:` resolution at BASE exists to deny on the recipe path. Recording the path
beside the content keeps the provenance without keeping the dependency.

### Inventory

The kit vintage, every carrier. `tools/check-kit-versions.sh` pairs the two engine constants AND the
same-line marker each carries, then enumerates the marker on every tracked `tools/unattended/*.template.md`
— a DERIVED population, so the list below is what that derivation currently resolves to and not a
second spelling of it.

| Carrier | What it holds |
|---|---|
| `tools/unattended/unattended.sh` | the constant and its same-line marker |
| `tools/unattended/check-unattended.sh` | a SECOND constant and its same-line marker |
| `tools/unattended/SKILL.template.md` | the marker |
| `tools/unattended/PROTOCOL.template.md` | the marker |
| `tools/unattended/PLAYBOOK-TEMPLATE.template.md` | the marker |
| the three installed artifacts | regenerated by the adopter, never hand-edited |

`1.9` to `1.10` is a safe spelling: `check-kit-versions.sh` compares by equality, and `govkit`'s only
numeric comparison is a tuple of ints, which orders `(1, 10)` above `(1, 9)`.

### Files touched (estimate)

`tools/unattended/adopt-unattended.sh` · `tools/unattended/SKILL.template.md` ·
`tools/unattended/PROTOCOL.template.md` · `tools/unattended/PLAYBOOK-TEMPLATE.template.md` ·
`tools/unattended/unattended.sh` · `tools/unattended/check-unattended.sh` ·
`tools/unattended/.unattended.conf.example` · `tools/unattended/kit.toml` ·
`tools/unattended/cross-component.test.sh` · `tools/unattended/adopt-unattended.test.sh` ·
`.unattended.conf` · the three installed artifacts · `memory/guides/SESSION-KICKOFF.md` ·
`memory/map/features/unattended.md` · `memory/DECISIONS.md` · `memory/backlog/TOOL.md` ·
`memory/project/readme-contract.txt`.

### Alternatives rejected

**A bare gesture token with no argument**, which was the opening design and defaulted to a
thoroughness word. Rejected by the owner at kickoff: it named a degree rather than a grant, so no
value of it was obviously wrong, `GATE_FULL` already means something else in this tree, and it left
the build's prose sitting beside the parameter rather than inside it.

**Keeping the parameter kit-owned with no conf channel**, the way `AUTH_MODES` and
`SECOND_ANCHOR_MODES` are. Rejected because the argument that makes those kit-owned — an
adopter-declarable set is an adopter-reopenable hole — does not transfer. The mode VOCABULARY is a
security surface; the spelling of a token an owner types is not.

**Declaring the literal in both shipped confs rather than blank.** Rejected: it puts the same string
in three files with no gate joining them.

**A pre-set default plus a blank-normalisation, instead of a derived effective value.** Rejected on
the same one-spelling ground, after a grounding probe pointed out that the pre-set form writes the
literal twice while claiming to write it once.

## 5. Production-readiness checklist

- security — the parameter is the GESTURE, not the authorization; the anchor is unchanged. The
  failure directions are analysed in section 8, fork F2, and the value guard is section 4's.
- perf / scale — N/A: one string substitution in a render that already performs seven.
- a11y — N/A: no user interface.
- i18n — N/A: the token is an ASCII literal an owner types, and the conf can change it.
- error / empty / loading states — a blank declaration derives the default; a malformed one is S3's
  refusal; an unfilled placeholder reds the render's existing arm; an unresolvable path value is
  S6's refusal.
- observability — the rendered Skill states the token, so the value is readable in an adopter's tree
  without running anything.
- risks (concurrency, data-loss, rollback hazards) — none: the change adds no write path. Rollback is
  a revert plus a re-render.
- testing + left-shift gates — S11 adds the arm that makes S2 falsifiable, and AC5 stages the check-22
  break and observes RED. A gate arm this unit relies on and has never seen fail is an assertion
  about nothing.
- migration / rollback — an existing adopter who never declares the key receives the default, so the
  kit update is not breaking. Section 8 fork F1 records the evidence.
- user docs — the protocol's section 8 key table is the adopter-facing documentation, in scope as S1.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/adopt-unattended.sh --check` runs on this tree, it exits 0,
  and `grep -nE '\{\{[A-Z_]+\}\}' .claude/skills/unattended/SKILL.md` prints nothing.
- **AC2** — When `.claude/skills/unattended/SKILL.md` is grepped for the token, it appears at BOTH
  the routing row and the prompt-path fence.
- **AC3** — When `adopt-unattended.sh` renders against a fixture whose conf declares `AUTH_PARAM=""`,
  the rendered Skill carries the kit default and not an empty string. The arm lives in
  `tools/unattended/adopt-unattended.test.sh` and FAILS when S2's derivation is deleted.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs with the new key declared in
  `.unattended.conf` and its row present in section 8, it exits 0.
- **AC5** — When the `AUTH_PARAM` row is deleted from section 8 of
  `memory/guides/UNATTENDED-PROTOCOL.md`, `check-unattended.sh` fails naming check 22. Observed RED,
  then restored.
- **AC6** — When a fixture conf declares a malformed value, `adopt-unattended.sh` exits non-zero and
  names the value. Both a bare word and a value containing a pipe are exercised.
- **AC7** — When `bash tools/check-kit-versions.sh` runs after the bump, it exits 0, and
  `grep -rn 'unattended@1\.9' tools/unattended/ .claude/skills/unattended/ memory/guides/` prints
  nothing.
- **AC8** — When `bash tools/unattended/adopt-unattended.test.sh` and
  `bash tools/unattended/cross-component.test.sh` run, both exit 0.
- **AC9** — When `bash skills/session-kickoff/manifest-check.sh` runs after the conf edit, it exits 0.
- **AC10** — When `bash tools/run-gates/run-gates.sh` runs at the push boundary, every leg is green.

## 7. Gates

`unattended kit gate` (`bash tools/unattended/check-unattended.sh`) · `unattended skill wiring`
(`bash tools/unattended/adopt-unattended.sh --check`) · `playbook validity gate` ·
`tools/check-kit-versions.sh` · the kickoff-manifest ratchet · the memory-tree hygiene gate · the
codebase-map coverage and freshness legs · `govkit` selfcheck and selftest. The full bar is
`bash tools/run-gates/run-gates.sh`; the leg list is single-sourced from `tools/gate-legs.json`.

## 8. Open questions

- **F1 · FACT-QUESTION · does an existing adopter who never declares `AUTH_PARAM` go red on the kit
  update?** The probe is a read of `adopt-unattended.sh` and `check-unattended.sh`: whether the
  derived default survives an absent declaration, and whether check 1's required-key loop or check
  22's reverse direction name a key the adopter has not set. Liveness: the same read reports a red
  for a genuinely required key, which `HALT_FLOOR` demonstrates.
  RESOLVED (agent, 2026-08-25, delegated): the default survives. Check 1's loop is a fixed literal
  list this unit does not join, and check 22's project direction grades only keys a project DOES set.
  An adopter who declares nothing renders the default and stays green.

- **F2 · what do the failure directions of this key actually buy an attacker?** A misspelled key name
  is caught by check 22's project direction, which reds any key the project sets and the protocol
  does not document. A blank value derives the default rather than an empty token, so the fence can
  never render as a sentence naming nothing. A malformed value is S3's refusal. The residual hazard
  is an adopter-chosen value that appears in that project's ordinary prose, which is the adopter's to
  price — and is the argument for the key being project-declarable at all.
  RESOLVED (agent, 2026-08-25, delegated): deriving the default from blank is fail-CLOSED, because
  the alternative is a fence naming nothing, which authorizes every invocation rather than none.

- **F3 · which token, and does it collide?** Probed 2026-08-25 by grepping the whole tree and
  enumerating the driver's argument arms; the control found 37 verbs and none of them is the chosen
  token, nor is any of them a prefix of it.
  RESOLVED (owner, 2026-08-25): the token names the mode it starts, so the gesture and the
  `authorized-by:` value it produces are one word.

- **F4 · should routing row 4 carry the token, or a pointer to the fence?** Row 4 is the
  playbook-authoring entry and declares `prompt`; its section says in as many words that it uses the
  prompt path. A third substitution would put the token in a row whose own procedure is stated
  elsewhere, and check 24 reads that table.
  RESOLVED (agent, 2026-08-25, delegated): a pointer clause, per S6. The fence is one place and the
  routing table is a router, so the row says which fence binds it rather than restating the token.

## 9. Revision log

- rev-1 · 2026-08-25 · initial draft, after the owner replaced the opening thoroughness-word default
  with a mode-naming token and gave the parameter a path-or-prose argument.
- rev-2 · 2026-08-25 · folded workflow `wf_38add5e5-594`, a five-lens read-only grounding probe.
  Four blockers: the version bump has nine carriers in six files rather than two, the adopter installs
  three artifacts rather than two, `.unattended.conf` is a watched file so the manifest ratchet is
  owed, and the pre-set-plus-normalise form wrote the literal twice while claiming once. Added S3's
  value guard, the LAST-substitution rule, the second hand-kept renderer, AC3's missing arm, the
  `recipe` asymmetry, and the ban on a placeholder in the byte-copied templates.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a project-declared conf key rendered into the unattended
Skill"` returns `.unattended.conf` as the affordance seam and no symbol that fits — the render is a
bash pattern substitution in one file, not a library. The seam this unit extends is therefore
`render()` in `tools/unattended/adopt-unattended.sh`, together with the pre-set and post-source
`case` block above it, which is the `ANCHOR_SCOPE` seam this unit copies rather than reinvents.
`python tools/memory-recall/query.py` was run with the terms `authorizing parameter prompt mode
authorization gesture unattended conf key render placeholder adopter Skill declared`; it returned
`TOOL-aPromptedMandate-5` (the prompt path and its unfilled S2), `TOOL-aWrittenMethod-1` (the
placeholder-default rule this unit takes an exception to), `TOOL-dNarrowedAnchor-1` (the per-mode
anchor) and `TOOL-aUnmannedHelm-7` (parity is not placeholder completeness). All four were read
against source. `TOOL-aWrittenMethod-1` is the one that disagreed with the plan as first written, and
section 4 records why the exception is legitimate rather than working around it.
