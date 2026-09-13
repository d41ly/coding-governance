# TOOL-dPolishedVitrine-1 — the build harness is rendered at install, and its paths are derived

**Status:** INPROGRESS · rev-7 · 2026-09-13 · node d · Tier-2 · base 24f8c712 · streams tooling+deployer · ratified 2026-09-12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-12-build-TOOL-dPolishedVitrine-1-1-journal.md](../build/2026-09-12-build-TOOL-dPolishedVitrine-1-1-journal.md) | journal | — |
| [2026-09-12-prompt-TOOL-dPolishedVitrine-1-0-owner-ruling.md](../prompts/2026-09-12-prompt-TOOL-dPolishedVitrine-1-0-owner-ruling.md) | journal | — |
| [2026-09-12-review-TOOL-dPolishedVitrine-1-diff-review-round1.md](../reviews/2026-09-12-review-TOOL-dPolishedVitrine-1-diff-review-round1.md) | diff-review | — |
| [2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round2.md](../reviews/2026-09-13-review-TOOL-dPolishedVitrine-1-diff-review-round2.md) | diff-review | — |

<!-- /gen:spec-records -->

## 1. Goal

`tools/workflows/unattended-build.js` ships as an engine file, which apply writes verbatim, so its
four install paths reach an adopter installed at `scripts` still naming `tools/…`. Those paths are
the driver, the bug-class checklist, the review sub-workflow and the child the harness hands out.
This unit renders the harness at install through the review-harness kit's existing render channel.
The checklist's directory is PROBED from the tracked tree rather than guessed, and the unattended
Skill's copy of the same checklist line is fixed the same way.

## 2. Scope (IN)

- **S1** — `git mv` the harness to `tools/workflows/unattended-build.template.js`. Its four
  executable literals become `{{TOOL_ROOT}}`, `{{MEMORY_TREE_DIR}}` and `{{KIT_DIR}}` placeholders.
  The comment literals are reworded or tokenised so the template spells no `tools/` path, and the
  line-3 marker stops claiming the file is deployed verbatim. Observed by AC1, AC2 and AC7.
- **S2** — `tools/workflows/kit.toml` gains a `rendered` rule claiming `{kit}/unattended-build.js`
  from the template with the three placeholders, and a `[[regenerate]]` block running the parity
  script's `--render`. `why_no_adopter` names both renders. Observed by AC1 and AC7; what `govkit
  update` does with the block in a consumer is NOT OBSERVED, because no consumer is re-pulled here.
- **S3** — `tools/workflows/check-protocol-parity.test.sh` grades a PAIR LIST rather than one pair.
  It fills `{{KIT_DIR}}` and probes `{{MEMORY_TREE_DIR}}`. When the probe finds nothing it skips, by
  name, only the pair whose template carries that token, and an override naming nothing tracked is
  refused. Its `--render` creates a missing live copy, and `--tracked-only`, which the regenerate
  passes, skips one that is absent and untracked instead (rev-7). A template in the kit dir with no
  pair is a red. The kit dir is found by the logical walk to `.git` instead of a string strip.
  Observed by AC1, AC3, AC4, AC5 and AC19.
- **S4** — the unattended kit. `SKILL.template.md`'s checklist line takes `{{MEMORY_TREE_DIR}}`, and
  `adopt-unattended.sh` gains the same probe, refusal and override. `tools/unattended/kit.toml`
  declares the placeholder and a `[[regenerate]]` block running the adopter. `cross-component.test.sh`
  gets the missing entry in its hand-kept sed chain. Observed by AC8 and AC9.
- **S5** — version bumps. review-harness goes 1.7 to 1.8 and unattended 1.18 to 1.20, at every
  carrier `tools/check-kit-versions.sh` reads; 1.19 was taken by `main` while this branch was open. Then `--write-ratchet` DROPS the two carried rows
  that reached zero. Observed by AC7 and AC10.
- **S6** — the arms, in `tools/workflows/unattended-build.test.sh` and
  `tools/unattended/adopt-unattended.test.sh`, with their failing cases observed before the fix and
  recorded in the build journal. The adopter suite's `seed()` copies the kit's `*.template.md` by
  glob, because its hand list had fallen two templates behind the adopter and every adopt in it
  was red at base. The memory-hygiene self-test's project-keys fixture borrows the real object
  database, because this unit's own live spec left its `base` unresolvable there and redded that
  block. Observed by AC2, AC3, AC4, AC5, AC6, AC8, AC11 and AC12.
- **S7** — the knock-on declarations. The runbook's copy-install step names the render, both kit
  READMEs say what is rendered, `memory/project/method-carriers.txt` declares the template, the
  review-harnesses dossier claims the new inventory key and records the renderer as a seam, and the
  lexicon pin moves by the template's two forced names. Observed by AC11.
- **S8** — round 1's repairs, rev-5. govkit's `update` lands an unclaimed source before it runs a
  kit's `[[regenerate]]`, a failed regenerate says what its kit's check can and cannot roll back,
  selfcheck gains arm 7l over every kit declaring `[[regenerate]]`, and govkit moves 1.10 to 1.11.
  The parity script resolves `MEMORY_TREE_DIR` per pair, so an unanswered probe skips only the pair
  that needs it. The parity leg is unguarded in both carriers. The runbook's Maintenance section and
  the kit README carry the consumer migration. Observed by AC4, AC13, AC14, AC15 and AC16.
- **S9** — round 2's repairs, rev-7. The runbook's migration becomes two blocks the govkit selftest
  cuts out of `WIRE-INTO-PROJECT.md` and runs: block 1 stops on update's exit code, commits only
  update's own writes with the receipt, derives the pins from `plan`, and checks a read-only re-adopt
  that counts the rows it leaves unattributed; block 2 re-adopts, commits the renders with the
  receipt, and re-adopts once more. The `[-PV]` arms run it on an `adopt`-bootstrapped fixture with
  a receipt hook, over this repo's real parity script. The parity script gains `--tracked-only` and
  the regenerate argv passes it. Selfcheck arm 7l gains its negative half, and three carriers stop
  calling a flag-off update silent. Observed by AC13, AC17, AC18, AC19 and AC20.

## 3. Non-goals (OUT)

- **The Tier-B dual-spelling probes stay as they are.** `check-wiring.sh`'s `first_of`,
  `adopt-memory-recall.sh`'s settings-merge probe and `render_playbook.py`'s gate-runner rungs all
  miss a `scripts/` install. Each becomes its own backlog row.
- **The Tier-C remedy and usage strings stay as they are.** They misdirect a reader but never execute.
  One backlog row carries them.
- **`check-verdict-epoch.sh`'s `ENGINE=` literal stays.** It is a memory-tree kit file, so a fix would
  bump that kit and every one of its template markers. That is not a one-line fix on this token, so
  it is a backlog row.
- **No consumer is touched.** Core and NicoCares re-pull this release in their own trees.
- **govkit changes only where round 1 found the update path broken.** rev-5 amends this bullet,
  which read "govkit is not changed". The introducing update could not render the harness, so the
  landing now precedes the regenerate; S8 lists the rest. `update` still does NOT re-resolve a row's
  role at schema 3. That durable repair reaches every row whose descriptor role moved, including the
  self-tests `TOOL-aQuenchedHarness-3` withheld, so it waits for its own spec as
  `DEPL-dPolishedVitrine-1`, and the consumer migration in §4 Rollout stands in for it. rev-7 adds
  the negative half of selfcheck arm 7l and changes no verb; a withheld-stamp message naming the
  pinned re-adopt, and govkit reporting a file a regenerate created, are round 2's two govkit
  improvements, carried by `DEPL-dPolishedVitrine-1` and `DEPL-dPolishedVitrine-2`. There is
  still no write-time relocate of engine bodies. `govkit.py` calls its carry derivation a proof
  instrument, not a write-time transform, and a relocate would mis-carry the checklist line anyway
  (§4 Alternatives rejected).
- **The harness suite stays on no bar.** `TOOL-dBriefedPass-7` owns that question.
- **The override is not persisted.** `MEMORY_TREE_DIR` is read from the environment only. A tree whose
  bar needs it exports it for the gate too, which is the drift-audit adopter's recorded limit for its
  own sibling override.
- **The driver path is a convention, not a probe.** `{{TOOL_ROOT}}unattended/` is asserted by
  nothing at render time, because a review-harness adopter need not install the unattended kit, and a
  refusal there would red that adopter's parity leg over a harness they never run.
- **`check-kit-placeholders.py` keeps its review-harness exemption.** The kit still declares no
  adopter, and the parity script's surviving-placeholder arm grades the new tokens.

### Edges

- **consumes-from** external — the memory-tree kit's `gotchas.py` must be tracked at one of the two
  probed spellings, or named by the override, before the harness renders. The parity script still
  renders the protocol without it, and the unattended adopter refuses without it.
- **hands-off** external — the consumer re-pulls by the runbook's migration, not by `update` alone.
  On govkit 1.11 or later it runs the runbook's two blocks, verbatim, and reads block 1's FLAG lines
  between them. §4 Rollout says why each step is there (rev-7; rev-5's sequence wedged at core's
  commit-time receipt check). The hand-off also covers NicoCares carrying its cap carve-out into the
  template after block 2, retiring core's untagged Skill delta and NicoCares' untagged driver delta,
  and adding the parity leg core lacks.

## 4. Design

### Data model

The harness has no filesystem when it runs: it is evaluated as an AsyncFunction body, with `agent`,
`workflow` and the rest injected. So nothing inside it can find its siblings. The only derivation it
can have happens before it runs, when the kit is installed. The kit already has a channel for that.
A `rendered` row whose placeholders the kit's own renderer fills is how `REVIEW-PROTOCOL.template.md`
reaches an adopter, and `TOOL-dRetiredFork-12` took the playbook fixture through the same door for
this same class.

Three tokens, each derived by the renderer and none typed:

| token | derived how | gov | flat adopter (`scripts`) | root install |
|---|---|---|---|---|
| `KIT_DIR` | the logical walk from the kit dir to the nearest `.git` | `tools/workflows` | `scripts/workflows` | `workflows` |
| `TOOL_ROOT` | `KIT_DIR` minus its last segment, plus a slash | `tools/` | `scripts/` | empty |
| `MEMORY_TREE_DIR` | the first TRACKED of `${TOOL_ROOT}memory-tree/gotchas.py` and `${TOOL_ROOT}gotchas.py` | `tools/memory-tree` | `scripts` | `memory-tree` |

`MEMORY_TREE_DIR` is not derivable from `TOOL_ROOT`. Both measured adopters set
`[kit.memory-tree] kit = "scripts"`, which installs that kit FLAT, so `TOOL_ROOT` plus `memory-tree/`
names a file neither of them has. A fix that derived only the prefix would pass a nested fixture and
still break both real trees. That is why the flat fixture is the load-bearing one in §6.

The four literals, and what they render to:

| site | template | gov render |
|---|---|---|
| `DRIVER` | `bash {{TOOL_ROOT}}unattended/unattended.sh` | `bash tools/unattended/unattended.sh` |
| `CHECKLIST` | `python {{MEMORY_TREE_DIR}}/gotchas.py --for-diff HEAD~1..HEAD` | `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` |
| the AUDIT stage's nested `workflow()` | `{{KIT_DIR}}/tier2-review.js` | `tools/workflows/tier2-review.js` |
| `dispatch.scriptPath` | `{{KIT_DIR}}/unattended-unit.js` | `tools/workflows/unattended-unit.js` |

Every value derived from `DRIVER` or `CHECKLIST` follows them: the three agent prompts,
`dispatch.args.driver`, `dispatch.args.checklist` and `resolvePathsWith`. The two comment sites that
named this kit's own files take `{{KIT_DIR}}` too, so gov's render reproduces those lines byte for
byte. The two that named other kits are reworded. So gov's render differs from its base blob at three
comment lines and nowhere else. AC1 pins that.

### The probe and its refusal

The probe asks git, not the filesystem. A path counts only when `git ls-files --error-unmatch`
answers for it, so an untracked scratch copy cannot satisfy it. When neither spelling is tracked, the
parity script SKIPS the harness pair out loud, names `MEMORY_TREE_DIR` as the override, writes no
harness, and still renders and grades the protocol, because the review-harness kit requires only
agent-cap (rev-5, round 1 F3). The unattended adopter exits 2 there instead, because that kit
requires the memory-tree kit. An override is checked the same way in both: it must name a directory
whose `gotchas.py` is tracked, or it is refused. A wrong
answer typed by a person runs nothing either. Both renderers also refuse a value holding a character
outside a path's set, because the value lands inside a single-quoted JS string and inside a shell
command. There a quote ends the string and a space splits the command.

### The parity script, generalised

`PAIRS` holds two `<live>|<template>` rows. For each pair the script renders, refuses a surviving
placeholder and, in `--check`, diffs the render against the live copy. `--render` writes only after
every pair has rendered clean, so a half-written set cannot exist, and it creates a live copy that is
missing. The existing pointer arm over the protocol's two bound sections is unchanged. One new arm
reds when the kit dir tracks a `*.template.*` with no row in `PAIRS`. That keeps the hand list from
silently falling behind the kit, which is the class `TOOL-aKeyedAnnotation-10` names for a
neighbouring pair list.

The render moves from `sed` to bash parameter substitution with a quoted replacement. That form
treats `&`, `|` and `\` in a value as themselves. It is the unattended adopter's render, and it only
drops a CR that ends a line, exactly as the `sed` it replaces did.

The kit dir used to be found by stripping the repo root off `pwd` as two strings. Under MSYS a
fixture in `/tmp` has two spellings, so the strip no-ops and the script refuses a kit that is plainly
inside its repo. The unattended adopter's logical walk replaces it. `check-wiring.sh` copied the same
walk.

### The unattended half

`adopt-unattended.sh` probes after its conf check and its `AUTH_PARAM` refusals and before any
write, so a tree without a conf still gets the `no-project-layer` refusal its descriptor declares.
The override is captured before the conf is sourced, so the variable comes only from the
environment. The Skill rule in `tools/unattended/kit.toml` declares the new placeholder, which
`python tools/check-kit-placeholders.py` joins against the adopter's substitution. The
`[[regenerate]]` block runs the adopter without `--check`. That prevents a repeat of the 2026-09-11
NicoCares rollback: an update landed an unattended template, did not re-render it, and post-write
verification rolled the kit back.

### Inventory

Minted by this unit, with the cell that grades each:

- `tools/workflows/unattended-build.template.js`: a file, and a new `workflow-scripts` inventory key
  the review-harnesses dossier claims, beside a `seam:` line for the renderer.
- `MEMORY_TREE_DIR`: a placeholder token, and the environment variable that overrides it.
- `check_tracked` and `read_lf` in the parity script, and `check_tracked` in the adopter, all in cell
  `sh.function`. Each was asked of `--suggest --as sh.function` before it was written.
- `build_layout`, `run_layout`, `check_layout` and `read_field` in the harness suite, same cell, same
  question.

### Rollout

The template ships as an engine file under the kit's `**` rule, because an adopter's render reads
it. The render is claimed by the new `rendered` rule, so it drops out of the engine pool. In gov the
render stays tracked at its old path, because this repo runs its own harness.

That last fact is why `update` alone cannot migrate a consumer (rev-5, round 1 F1). Both consumer
receipts are schema 3 and row the harness as `engine`. `update` takes a row's role from the receipt,
and gov still tracks the source, so the raw arm writes gov's own `tools/`-spelled render. So the
consumer migrates by the runbook's two blocks, on govkit 1.11 or later (rev-7, round 2):

1. Block 1 runs `update --write` with `GOVKIT_RERENDER=1`: the template lands as an unclaimed
   source, and then every `[[regenerate]]` block renders. It STOPS unless update exits 0 with no
   conflict, the review-harness regenerate exits 0, and the parity check grades the harness green
   under `--tracked-only`. A conflicted three-way leaves the row at its old commit while the
   regenerate still runs, so the parity check alone would pass it (R2-6).
2. It commits update's own writes with the receipt that records them, and nothing the regenerate
   wrote. Until the re-adopt the row is still `engine`, so a commit-time check comparing staged
   engine blobs with the receipt reds the re-rendered harness, and the re-adopt refuses a staged
   tree (R2-1). The regenerate's changes to tracked files are recorded by name; a file it created is
   flagged and never staged (R2-3).
3. It derives the pins. A tracked row that records a commit, and that the plan still resolves, is
   pinned to that commit. A tracked destination that `plan` at the new vintage resolves as
   `rendered` is pinned to that vintage when its kit's regenerate ran at exit 0, and left unpinned
   otherwise, so a declined render is never recorded as current (R2-2). The rendered set comes from
   the plan, not the receipt, because a receipt `adopt` bootstrapped never rows a destination
   tracked after it was written (R2-5), and a rendered destination is never pinned to a recorded
   commit (R2-6).
4. It runs the re-adopt READ-ONLY and checks it. Every row new to the receipt is flagged, every row
   left `unattributed` is flagged with its reason, a row that loses a recorded base stops the block,
   and the last line counts the unattributed rows.
5. Block 2 runs `adopt --re-adopt --write` with the pins, which is the only verb that re-reads a role
   from the descriptor, so the harness row becomes `rendered`. It stages the recorded renders with
   the receipt and commits, which the receipt check exempts, because the rows are now `rendered`.
6. It re-adopts once more with the same pins, because step 5 read each render's identity from the
   index before the render was staged, and commits the receipt. The end state asserted is the one
   where the receipt's `oid` is the committed render's blob.

Done is: the harness row `rendered` and `pinned`, and the next `update --write` writes nothing to it
and either re-stamps or withholds the stamp over exactly the rows step 4 counted (R2-4). At both
consumers it withholds, because each carries rows that were unattributed before. That message
suggests the bare `adopt --re-adopt --write`, which drops every pin, so the runbook says to re-run
block 2 instead; making the message name the pinned form is `DEPL-dPolishedVitrine-1`'s.

With `GOVKIT_RERENDER` unset, `update` declines both regenerates without printing a line naming
them, yet it still prints each moved render's row as `re-rendered` although no render ran (R2-7).
The review-harness renders are then left stale, and the parity leg reds them at the next bar. The
unattended kit is worse off. Its template lands, its Skill is left stale, and its own post-write
check rolls the kit back, which is the 2026-09-11 NicoCares event. That was read from the code, not
run.

### Files touched (estimate)

The template and its render, the two `kit.toml` files, the parity script, the unattended adopter,
the Skill template and gov's render of it, the two suites and `cross-component.test.sh`, every
unattended version carrier, `tier2-review.js`, the two kit READMEs, `WIRE-INTO-PROJECT.md`,
`tools/install-prefix-carried.txt`, `.lexicon.conf`, `memory/project/method-carriers.txt`, the
review-harnesses dossier, the generated map, and this build's records.

### Alternatives rejected

- **Callers pass the paths in `args`.** The owner offered it and did not choose it.
- **A govkit write-time relocate of engine bodies.** `derive_carry_map` drops `tools/memory-tree` as
  ambiguous in both consumers' receipts and falls back to `tools -> scripts`. That carries the
  checklist to `scripts/memory-tree/gotchas.py`, which neither tree has. It would also contradict the
  deployer's own statement that carry is a proof instrument.
- **`{{TOOL_ROOT}}memory-tree/` for the checklist.** It is correct in gov and wrong in both adopters,
  and AC6 keeps it red.
- **Refusing a render whose driver path does not exist.** §3 records why.

## 5. Production-readiness checklist

- security — the render executes nothing it reads. Values are path-charset-checked before they are
  interpolated into a JS string and a shell command, and the override is refused unless git tracks
  what it names.
- perf / scale — one bash parameter substitution per token over a 58 KB template, plus one
  `git ls-files` per probe rung. The parity leg's cost moves by well under a second.
- error / empty / loading states — an empty render, an unreadable template, a surviving placeholder,
  an unpaired template and a missing live copy under `--check` each have their own refusal, and none
  of them writes anything. An unanswered probe is not one of them: it skips, by name, only the pair
  whose template needs the answer, and an override naming nothing tracked is the refusal (rev-7).
- observability — the parity leg's green line names the pair count and the probed directory, so a
  reader can see which checklist spelling a tree derived.
- risks — `MEMORY_TREE_DIR` and the driver path assume the kit layouts measured today. The first is
  probed, with its pair skipped out loud when the probe finds nothing and a misplaced override
  refused, and the second is not probed at all, as §3 states. The lexicon pin rises by two, because the
  template repeats two helper names that `agent-cap.js` recognises by name.
- testing — five harness fixtures, two negative controls, three parity refusals, and four adopter
  arms. Every new arm is observed red before the fix, and the journal records it.
- migration — none in gov: its render is byte-identical at every code line. Consumers migrate by
  the runbook's two blocks in §4 Rollout, handed off in §3, and not by `update` alone.
- user docs — N/A as a `help/` tree, which this repo does not ship. The runbook's copy-install step
  and both kit READMEs are the agent-facing docs, and S7 updates them.

## 6. Acceptance criteria

- **AC1** — When `bash tools/workflows/check-protocol-parity.test.sh --render` runs in this repo,
  the rewritten `tools/workflows/unattended-build.js` differs from base blob `75763c4e` at exactly
  three lines, which are the marker and the two reworded comments. The parity leg then exits 0.
  Red when: any code line differs, which would mean a token rendered to something other than gov's
  own path.
  figure: PINNED — three lines, against the blob both consumers' receipts record.
- **AC2** — When `bash tools/workflows/unattended-build.test.sh` builds the FLAT layout, renders it,
  and runs the render on its `run_wf` stub, arms (i)–(v) pass. The fixture paths are written plain
  here, because none of them is a path in this repo. The trace names the sub-workflow at
  scripts/workflows/tier2-review.js, `dispatch.scriptPath` is scripts/workflows/unattended-unit.js,
  `dispatch.args.driver` is bash scripts/unattended/unattended.sh, and `dispatch.args.checklist` is
  python scripts/gotchas.py --for-diff HEAD~1..HEAD. Every `.js`, `.sh` and `.py` path the harness
  emits is tracked in the fixture.
  Red when: any of the five fails. A prefix-only derivation reds (iv) and (v) here while passing a
  nested fixture.
- **AC3** — When `tools/workflows/unattended-build.test.sh` builds the NESTED layout, with the
  checklist script at scripts/memory-tree/gotchas.py, and a ROOT install, with the kit at workflows,
  both pass arms (i)–(v). At the root the driver renders as bash unattended/unattended.sh.
  Red when: a root install renders a leading slash or a stray prefix, or the nested spelling loses
  the probe to the flat one.
- **AC4** — When the flat layout carries no `gotchas.py`, `check-protocol-parity.test.sh --render`
  prints a SKIP naming the harness pair and `MEMORY_TREE_DIR`, exits 0 because the protocol pair still
  rendered, and leaves no harness render behind. With the override pointing at a tracked
  vendor/mt/gotchas.py, the checklist renders as python vendor/mt/gotchas.py --for-diff HEAD~1..HEAD,
  and an override naming nothing tracked still exits 2.
  Red when: the skip is silent, writes a harness, or names no override; or the override is ignored,
  or a misplaced one is accepted.
- **AC5** — When a green flat render is hand-edited, `check-protocol-parity.test.sh` exits 1 printing
  `DRIFT`. When the kit dir tracks a stray `*.template.*`, it exits 1 naming that file. When the live
  copy is absent, `--check` exits 1 and `--render` creates it.
  Red when: any of those runs exits 0.
- **AC6** — When the suite installs the flat layout with the harness spelled for gov's own install,
  which is what apply wrote before this unit, all five arms red. When the template's checklist is
  swapped to `{{TOOL_ROOT}}memory-tree/gotchas.py`, arms (iv) and (v) red while (i)–(iii) pass. Both
  are permanent negative controls in `tools/workflows/unattended-build.test.sh`.
  Red when: a negative control passes, which means the arm cannot fail.
- **AC7** — When `bash tools/check-install-prefix.sh` runs after `--write-ratchet`, it exits 0, and
  `tools/install-prefix-carried.txt` no longer holds rows for `tools/workflows/unattended-build.js`
  or `tools/unattended/SKILL.template.md`. No row names `tools/workflows/unattended-build.template.js`.
  Red when: the template carries a literal, which reports UNRECORDED; or the render is still counted
  as a shipped source, which would mean the `rendered` rule claims nothing.
- **AC8** — When `bash tools/unattended/adopt-unattended.test.sh` runs, the nested seed's Skill says
  `python <tool-root>memory-tree/gotchas.py`, and a flat seed's says `python <tool-root>gotchas.py`.
  A seed tracking neither exits 2 naming `MEMORY_TREE_DIR` with no Skill written. The override
  renders its own directory.
  Red when: any arm fails, or the refusal writes a Skill.
- **AC9** — When `bash tools/unattended/adopt-unattended.sh --check` runs in this repo, it exits 0.
  gov's `.claude/skills/unattended/SKILL.md` still reads
  `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD`, and
  `python tools/check-kit-placeholders.py` exits 0 with the placeholder declared.
  Red when: the adopter does not substitute the token, which reds the placeholder join; or gov's own
  checklist line changes.
- **AC10** — When `bash tools/check-kit-versions.sh` runs, it exits 0 with review-harness at 1.8,
  unattended at 1.20 and govkit at 1.11. With one carrier reverted, it exits 1 naming that carrier.
  Red when: a carrier is left at the old version and the gate stays green.
- **AC11** — When `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` runs on the
  branch tip, every leg is green except a leg that is also red at base, and the report names that
  leg. The suites `bash tools/unattended/run-unattended-gates.sh` delegates to show no FAIL at the
  tip that the same suite does not show at base.
  Red when: a leg that was green at base is red at the tip, or an unattended self-test arm that
  passes at base fails at the tip.
  cost: the full bar with self-tests, sixteen minutes of wall on node `d` at base, plus the
  unattended self-tests, which run on demand and are measured in hours.
  figure: PINNED — 07:41 to 07:57 UTC on 2026-09-12, the base run this unit's journal records.
- **AC12** — When `tools/workflows/unattended-build.test.sh` renders one layout through BOTH kits'
  renderers, flat and nested, the checklist command the harness hands out equals the one the
  rendered Skill tells the run to execute.
  Red when: the two copies of the probe drift, so the harness and the Skill name two different
  checklist scripts for one tree while each renderer's own arms still pass.
- **AC13** — When a target installed at vintage A rows a kit's file as `engine`, and gov's vintage B
  claims that destination `rendered` while still tracking the file, the §4 Rollout migration leaves
  the row `rendered` with the destination holding the target's render. An edited row keeps its
  recorded base, and the next `update` writes nothing to the harness and either re-stamps or
  withholds its stamp over exactly the rows the migration's check counted (rev-7). The govkit
  selftest's `[-PV] F1` arms run the runbook's own blocks, with an unpinned control.
  Red when: `update` alone is taken for the migration, so the row stays `engine` over gov's bytes; or
  the pins are dropped, so a render or an edited row comes back `unattributed`.
- **AC14** — When the introducing update of such a kit runs with `GOVKIT_RERENDER=1`, its
  `[[regenerate]]` exits 0 in that same run, reading a template the same run landed. When a
  regenerate fails in a kit whose `[check]` is `none`, the run fails and promises no rollback. The
  govkit selftest's `[-PV] F2` arms run both.
  Red when: the re-render runs before the unclaimed-source landing, or the failure text promises a
  rollback nothing performs.
- **AC15** — When a review-harness install tracks no `gotchas.py` anywhere, which `requires` allows,
  `check-protocol-parity.test.sh --render` still renders the protocol and names the skipped harness
  pair. `--check` then passes with the skip counted, and a drifted protocol still reds.
  Red when: the probe's refusal blocks the pair that carries no `MEMORY_TREE_DIR` token.
- **AC16** — When a kit declares `[[regenerate]]`, `govkit selfcheck` reds on any sentence in that
  kit's tracked files or descriptor that names `update` and a re-render without naming
  `GOVKIT_RERENDER`.
  Red when: a carrier promises a re-render the flag-off run does not perform, and selfcheck stays
  green.
- **AC17** — When the runbook's two blocks, cut from `WIRE-INTO-PROJECT.md`, run on a target whose
  pre-commit refuses a staged engine blob its receipt does not record, every commit they make lands,
  and the tree ends clean. The govkit selftest's `[-PV] R2-1` arms run them on an `apply`-built and
  an `adopt`-bootstrapped target, and a LIVENESS arm shows the hook refusing an engine edit.
  Red when: block 1 stages the regenerated harness before the re-adopt, as rev-5's `git add -A` did,
  and the hook refuses the commit.
- **AC18** — When the migration runs on a receipt `adopt` bootstrapped, holding rows unattributed
  before it, a render from a kit with no regenerate, and two tracked destinations it never rowed,
  the pins cover every tracked destination the plan renders whose kit regenerated, at the new
  vintage and never at an older commit; the declined render is left unpinned and the next update
  grades it `re-rendered`; block 1 flags both new destinations and counts the unattributed rows, and
  the next update withholds its stamp over exactly that count. A conflicted step 1 stops the block
  before its commit, with no pin derived. The `[-PV] R2-2`, `R2-4`, `R2-5` and `R2-6` arms run it.
  Red when: the pins come from the receipt, as rev-5's rule took them; the declined render is pinned
  and graded `patched`; the check is blind to rows new to the receipt; or step 1 carries on past
  update's exit 1.
- **AC19** — When the regenerate argv `tools/workflows/kit.toml` declares runs over an install that
  tracks the harness and has no protocol copy, it refreshes the harness, writes no protocol, and
  names the pair it skipped; `--check --tracked-only` passes over the same install and still reds a
  drifted harness; and a hand `--render` still creates the protocol. The `PV-R2-3` arms in
  `tools/workflows/unattended-build.test.sh` read that argv out of the descriptor, and a `[-PV]`
  arm runs it through `update`.
  Red when: the declared argv creates a live copy the install never had.
- **AC20** — When a kit declares `[[regenerate]]`, `govkit selfcheck` reds a sentence in its tracked
  files or descriptor that names `update`, the flag and a silence word without naming the
  `re-rendered` line a flag-off update still prints. And a flag-off `update` over a moved template
  prints that line while no render runs, which the `[-PV] R2-7` arms pin.
  Red when: a carrier says a flag-off update prints nothing and selfcheck stays green, or the
  printed line changes and no arm notices.

## 7. Gates

`review-protocol parity (kit vs dogfood)` · `workflow script syntax` · `verifier fan-out` · `install-prefix (shipped surface)` · `kit version markers` · `kit placeholders (a declared token its adopter substitutes)` · `govkit selfcheck` · `govkit selftest` · `kickoff-manifest ratchet` · `drift-audit records` · `unattended skill wiring` · `unattended kit gate` · `lexicon naming predicates` · `method carriers (every pointer declared)` · `codebase-map coverage + freshness` · `shell hygiene (a loop fed by a command substitution)` · `memory hygiene` · `memory-hygiene self-test` · `spec tokens (a spec's own names resolve)`

Two suites carry this unit's arms, and neither is on any bar. `unattended-build.test.sh` is on none
(`TOOL-dBriefedPass-7`), and `adopt-unattended.test.sh` runs only through
`run-unattended-gates.sh`. The recurrence guard an adopter keeps is the parity leg, which is on this
repo's bar and NicoCares'. Core has to add it.

New arm: `tools/workflows/unattended-build.test.sh` · HEAD's verbatim harness in the flat fixture, the half-fix template, and an adopter forced to the prefix-only answer · none
New arm: `tools/workflows/check-protocol-parity.test.sh` · a stray template, a missing gotchas.py, a hand-edited render · none
New arm: `tools/unattended/adopt-unattended.test.sh` · a seed tracking no gotchas.py · none
New arm: `tools/govkit/selftest.py` · the old hand-off, HEAD's engine order, a no-rollback promise · none
New arm: `tools/govkit/govkit.py` · the five carriers round 1 named, unfixed · none
New arm: `tools/workflows/unattended-build.test.sh` · a review-harness-only install · none
New arm: `tools/workflows/unattended-build.test.sh` · the regenerate argv without `--tracked-only` · none
New arm: `tools/govkit/selftest.py` · rev-5's `git add -A`, its receipt pin rule, a step 1 that ignores update's exit, a check blind to new rows, a relabelled flag-off verdict · none
New arm: `tools/govkit/govkit.py` · the three carriers calling a flag-off update silent · none

## 8. Open questions

- **F1 — which repair for the harness's install paths?** Options were deriving at install, having
  callers pass paths in `args`, or leaving it.
  RESOLVED (owner, 2026-09-12): derive at install. The verbatim ruling is this build's prompts record.
- **F2 — does this unit also fix the unattended Skill's checklist line?** Including it bumps a
  second kit. Leaving it makes the checklist command derived in one carrier and literal in the
  other.
  RESOLVED (agent, 2026-09-12, delegated): included, because the orchestrating session's brief put it
  in scope under the owner's ruling that one kit release fixes both adopters.
- **F3 — how does the lexicon pin absorb the template's two forced names?** The template repeats
  `boundedParallel` and `chunk`, which `agent-cap.js` recognises by name, so neither can be renamed.
  A text-keyed waiver would waive every copy corpus-wide. A pin raise names the two arrivals.
  RESOLVED (agent, 2026-09-12, delegated): raise the pin by two, naming the file and both names.
  `TOOL-aWeldedTribunal-12` still holds the underlying tension for the owner.

## 9. Revision log

- rev-1 · 2026-09-12 · initial draft, from the scouting report's section 5 and the owner's ruling.
- rev-2 · 2026-09-12 · S6 · S7 · §4 · AC11 · AMENDED while building. S7 named the unattended dossier
  for the new inventory key, and that dossier sits ten bytes under its declared cap, so the key and a
  `seam:` line for the renderer went to the review-harnesses dossier, whose kit renders the template.
  S6 grew the adopter suite's `seed()` fix: its hand list of templates had fallen two behind the
  adopter, every adopt in that suite was red at base, and the new arms could not be observed until it
  was fixed. §4's inventory gains `run_layout`. AC11's cost is replaced by the base run's measured
  wall.
- rev-3 · 2026-09-12 · S6 · §4 · AC12 · AMENDED after the build, from the bug-class checklist over
  its own diff. Two §4 lines still named the unattended dossier after rev-2 moved the key, which is
  the amendment-leaves-its-other-half-standing class, and both now name the review-harnesses
  dossier. The probe is written twice, once per kit, and two comments claimed the two carriers
  cannot disagree while nothing checked it, which is the two-answers class: AC12 and its arm
  compare the two renders, and S6 names it.
- rev-4 · 2026-09-12 · S6 · AC11 · AMENDED at the gate. AC11 asked the unattended kit's on-demand
  runner to print GREEN, and at base it cannot: its gate selftest carries reds measured at
  `24f8c712`, where a warning about an undeclared `DISPOSITION_CUTOFF` leaks into arms that expect
  empty output and a DoD-floor arm's `sed` no longer matches `DOD_CORE`. The criterion now compares
  the tip's FAIL set with base's. S6 grows the memory-hygiene self-test's fixture fix, which the
  full bar forced: that fixture drops history, and this spec's `base` cannot resolve without it.
- rev-5 · 2026-09-12 · S8 · §3 · §4 · §5 · AC4 · AC13–AC16 · §7 · AMENDED by the round-1 Tier-2 diff
  review, verdict BLOCKED on five defects. SCOPE grows into govkit, which §3 had excluded. The
  introducing `update` could not render the harness, because its re-render ran before the landing
  that brings in the template, so S8 moves that landing and takes govkit to 1.11. S8 also makes the
  regenerate's failure text truthful and adds selfcheck arm 7l for the class behind F5. §3's govkit
  bullet and its hand-off are rewritten. §4 Rollout is replaced by the fixture-verified consumer
  migration, because `update` keeps an existing receipt's `engine` role at schema 3. The durable
  govkit repair stays OUT as `DEPL-dPolishedVitrine-1`. AC4 inverts to a per-pair skip with the
  refusal kept for a misplaced override, and §4's probe paragraph follows it. AC13 to AC16 name the
  four new gates. The parity leg loses its guard in both carriers, and that needs no criterion,
  because the change adds nothing that could be observed failing.
- rev-6 · 2026-09-12 · S5 · AC10 · AMENDED at the merge of `main` at `09a22d2b`. That commit shipped
  its own unattended 1.19 for other content, and the two version lines merged byte for byte, so
  the merge takes unattended to 1.20 at every carrier the version gate reads and at the kit
  README's marker. AC10 now names 1.20, and govkit's 1.11 from rev-5 as well.
- rev-7 · 2026-09-13 · S3 · S9 · §3 · §4 · §5 · AC13 · AC17–AC20 · §7 · AMENDED by the round-2
  Tier-2 diff review, verdict BLOCKED on round 1's F1 still open at core, with eight defects in all.
  §4 Rollout is replaced by the runbook's two blocks, because rev-5's step-1 `git add -A` staged the
  regenerated harness while its row was still `engine`, core's commit-time receipt check refused
  it, and the re-adopt that would clear it refuses a staged tree (R2-1). The pins now come from
  `plan` and from each kit's regenerate, not from the receipt (R2-2, R2-5, R2-6); step 1 stops on
  update's exit code (R2-6); Done names the count block 1's check prints (R2-4). The regenerate argv
  passes `--tracked-only` (R2-3). Selfcheck arm 7l gains its negative half, and the flag-off
  sentences say the row still prints `re-rendered` (R2-7). S9 and AC17 to AC20 carry them. R2-8 is
  this rev's S3, §5 and build-README text, and its Check is this list of every `refus` clause that
  `grep -n` returns over the spec and the README, each with its disposition: S3 (:35) AMENDED to the
  per-pair skip; §5 error states and risks AMENDED; README "A missing checklist script" and "A path
  nobody has proved exists" AMENDED; KEPT, because each is true as written: S4's adopter refusal,
  §3's unbuilt driver-path refusal, §3 Edges' adopter refusal, the "probe and its refusal" section's
  heading and its override and charset refusals, the parity script's surviving-placeholder refusal,
  §4's history of the string strip, the adopter's `AUTH_PARAM` and `no-project-layer` refusals, §5
  security's override refusal, §5 testing's three parity refusals, AC8, AC15's red-when, rev-5's log
  line, and §10's probe-and-refuse provenance.

## 10. Reuse audit

The seam this unit EXTENDS is the review-harness kit's render channel. That is the `rendered` rule
in `tools/workflows/kit.toml`, filled by `tools/workflows/check-protocol-parity.test.sh --render`, and
already carrying `REVIEW-PROTOCOL.template.md`. The second seam is the unattended adopter's `render`,
which gains one substitution. The probe-and-refuse shape comes from `adopt-drift-audit.sh`, which
asserts a derived sibling path exists and names an override otherwise. The kit-dir walk comes from
`adopt-unattended.sh`. Nothing new is built to hold any of them.

The map probe did not find the seam. `python tools/codebase-map/reuse_lookup.py "render a shipped kit
file at install with its install paths derived"` returned name-stem neighbours, `kit_rel` and the
`render_*` family in the map kit, and reported `unscanned layers: .sh`. Both renderers here are
shell, so the probe is blind to them. The seams above were found by reading the two kits.

Recall terms used: `install prefix carried literal rendered template placeholder TOOL_ROOT KIT_DIR
parity render adopter verbatim engine`, against the question "why does the unattended build harness
spell tools paths that do not exist in an adopter installed at scripts". It returned
`TOOL-dRetiredFork-12`, `TOOL-dScrubbedConduit-2`, `TOOL-aGradedDoorway-2` and
`TOOL-aKeyedAnnotation-10`, each cited above where it bears.
