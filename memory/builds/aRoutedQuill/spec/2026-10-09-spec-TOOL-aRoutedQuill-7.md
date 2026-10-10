# TOOL-aRoutedQuill-7 — the unattended prompt-brief check reads its sub-head list from the kickoff kit's `--brief-skeleton`

**Status:** CLOSED · rev-3 · 2026-10-10 · node a · Tier-2 · base 6473ae38 · streams tooling · order 6 · ratified 2026-10-09

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-09-build-TOOL-aRoutedQuill-7-1-acceptance-ledger.md](../build/2026-10-09-build-TOOL-aRoutedQuill-7-1-acceptance-ledger.md) | journal | — |
| [2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-1-0-run-handoff.md) | journal | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 TOOL-aRoutedQuill-5 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-6 |
| [2026-10-09-prompt-TOOL-aRoutedQuill-7-build-brief.md](../prompts/2026-10-09-prompt-TOOL-aRoutedQuill-7-build-brief.md) | journal | — |
| [2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md](../reviews/2026-10-10-review-TOOL-aRoutedQuill-1-closing-diff-round1.md) | diff-review | TOOL-aRoutedQuill-1 KICK-aRoutedQuill-1 TOOL-aRoutedQuill-2 TOOL-aRoutedQuill-3 TOOL-aRoutedQuill-4 PLAY-aRoutedQuill-1 TOOL-aRoutedQuill-5 |

<!-- /gen:spec-records -->

## 1. Goal

TOOL-aQuotedBrief-1 builds a preflight check that grades a prompt-mode record's `## The brief`
against five hard-coded sub-heads. KICK-aRoutedQuill-1 makes the kickoff checker's
`--brief-skeleton` the one home of the brief's shape, with two more sub-heads. This unit makes the
unattended driver read the required list from that verb, at the pinned BASE, for builds opened from
a new cutoff, so the attended and the unattended brief cannot drift apart. Records of builds opened
earlier keep the five.

## 2. Scope (IN)

- **S1** — `check_prompt_brief` takes rule 1's sub-head list from `read_brief_subheads` when the
  build README's `opened:` date at BASE is on or after `PROMPT_BRIEF_SKELETON_CUTOFF`. Before that
  date, or with the key blank, rule 1 keeps the five TOOL-aQuotedBrief-1 hard-codes and the checker
  is not run. F1's probe observed an exact match, so by its ruling (a) rule 1 becomes an in-order
  subsequence over whichever list applies, each listed sub-head non-empty, and its refusal names the
  first sub-head missing, empty or out of order after the record. The key is read the way
  `read_brief_cutoff` reads `PROMPT_BRIEF_CUTOFF`, at the default-branch side of BASE, and only once
  that key has graded the record. Observed by AC1, AC2, AC3 and AC4.
- **S2** — `read_brief_subheads` resolves the kickoff checker, reads its blob at the pinned BASE,
  runs that copy with `--brief-skeleton`, and prints the `### ` headings between `## The brief` and
  the next `## ` heading, in order. It runs once per preflight, and only when a graded record's
  README is on or after the key. Observed by AC2 and AC7.
- **S3** — `resolve_kickoff_checker` finds the checker through `resolve_kit_dir`, which reads the
  install receipt and then two probes beside this kit, and then through the one `manifest-check.sh`
  the repository tracks. No hit, or two tracked, refuses naming every place it looked. Observed by
  AC5.
- **S4** — The list read from the checker is refused unless it holds the five TOOL-aQuotedBrief-1
  hard-codes in their order. A checker blob that exits non-zero on the verb, or prints no
  `## The brief`, refuses too. Every refusal sits in the brief check, after the authorization read
  and before the write gate, so a refusal writes no run-state file. Every refusal of the read, S3's
  included, is one check, 117, whose message carries the cause. Observed by AC5 and AC6.
- **S5** — `PROMPT_BRIEF_SKELETON_CUTOFF` is a new date key on the terms of `PROMPT_BRIEF_CUTOFF`:
  blank means off and is announced on stderr. It is declared in `.unattended.conf` at the date this
  unit lands, shipped blank in `tools/unattended/.unattended.conf.example`, given a row in the
  protocol's §8 table, and added to the driver's key-initialiser block. Observed by AC4 and AC8.
- **S6** — The prompt path's step 3 in `tools/unattended/VERBS.template.md` names
  `<check-script> --brief-skeleton` as the source of `## The brief`'s sub-heads, as its step 2
  already names `<check-script> --task-skeleton` for the field set, and the render
  `memory/guides/UNATTENDED-VERBS.md` follows. Observed by AC9.
- **S7** — `tools/unattended/kit.toml` names `kickoff-manifest` in `requires`. Observed by AC10.
- **S8** — The kickoff manifest's `last-audit` moves, because `.unattended.conf` is in its
  `watch:`, and `memory/map/generated/symbols.json` is regenerated for the two new functions. The
  unattended kit version moves once, in the run's own mint after the last unit, never in this pass.
  NOT OBSERVED by a criterion: the kit-version, kit-epoch, kickoff-manifest and codebase-map legs
  that §7 names grade these.

## 3. Non-goals (OUT)

- `read_audit_ask_record` keeps reading only `## The prompt`. Nothing under `## The brief`, the two
  new sub-heads included, opts a build into the spec audit.
- TOOL-aQuotedBrief-3's `### Items` line format: one physical line ending in exactly one bracketed
  disposition. This unit changes which sub-heads a brief must carry, never what an Items line holds.
- Rules 2 to 5 of TOOL-aQuotedBrief-1's structural rule, the record's four `##` sections, and their
  two single-line forms.
- Grading an attended brief. The check runs at preflight, over prompt-mode records only.
- Records of builds opened before the key. They keep the five-sub-head rule and are never retrofitted.
- Prose in the unattended Skill. Its render sits 29 bytes under its ceiling (measured below), and the
  verbs file is where the shape is pointed at; only its version marker moves with the bump.
- A core Definition of Done item. A new core item moves every adopter's `CORE_FLOOR`, and adopters
  running `BACKLOG_MODE` shards have no `ASKS_CMD`, so this unit adds none.

### Edges

- **consumes-from** `KICK-aRoutedQuill-1` — the `--brief-skeleton` verb and its `### ` list under
  `## The brief`. Without it every preflight past the key refuses on a checker with no such verb.
- **consumes-from** external — TOOL-aQuotedBrief-1 must be landed on main: its `check_prompt_brief`,
  its rule 1 and `PROMPT_BRIEF_CUTOFF`.

## 4. Design

### Evidence

Read at `6473ae38` on 2026-10-09. TOOL-aQuotedBrief-1 is SPECCED and not on main, so every claim
about its code is UNVERIFIED until it lands and is taken from its spec.

- TOOL-aQuotedBrief-1 §4 names `check_prompt_brief`, a numbered check in `verb_preflight` after the
  authorization read and before the write gate. Its rule 1 requires `## The brief` to hold
  `### Goal`, `### Items`, `### Acceptance`, `### Gates` and `### Non-goals`, in that order, each
  non-empty. It grades a record only when the README's `opened:` is on or after
  `PROMPT_BRIEF_CUTOFF`, reading each record at BASE with one `git show`. UNVERIFIED as code.
- `verb_preflight` starts at `tools/unattended/unattended.sh:6371`, and `read_audit_ask_record` at
  `tools/unattended/unattended.sh:3066` reads only `## The prompt`.
- `resolve_kit_dir` is inlined at `tools/unattended/lib-unattended.sh:132-180`: the install receipt
  under `.governance/`, then `<here>/<home>/<anchor>` and `<here>/../<home>/<anchor>`, then a
  refusal naming all three. The driver calls it from `KIT_DIR` (`tools/unattended/unattended.sh:84`)
  with a kit home and an anchor basename, never a path (`tools/unattended/unattended.sh:1123`).
- Gov keeps no receipt (`.governance/` tracks only `deploy.toml`) and homes the kickoff kit at the
  repo root's `skills/` (`home_root_relative` in `tools/govkit/entries/kickoff-manifest.kit.toml`), so
  no probe from this kit reaches it. The kickoff kit's own `resolve_kit_file` closes that gap with
  the one tracked anchor (`skills/session-kickoff/manifest-check.sh:723-749`). In gov,
  `git ls-files -- manifest-check.sh '*/manifest-check.sh'` prints one path (measured 2026-10-09).
- At an adopter the checker lands flat at `{prefix}/manifest-check.sh`. The receipt row whose source
  ends in the kickoff home and the anchor `manifest-check.sh` is how `resolve_kit_dir` finds it.
- `--task-skeleton` answers before the repository probe
  (`skills/session-kickoff/manifest-check.sh:86-91`), and KICK-aRoutedQuill-1 S1 gives
  `--brief-skeleton` the same placement, so a blob copy run from a scratch directory answers it.
- `tools/unattended/kit.toml:10` requires `memory-tree`, `review-harness` and `settings-merge`.
  `kickoff-manifest` is in the default selection (`tools/govkit/registry.toml:38-46`), and
  `derive_unsatisfied_requires` (`tools/govkit/govkit.py:876-901`) makes `apply` refuse, and `plan`
  print `UNMET`, for a required kit neither selected nor installed.
- Check 22 (`tools/unattended/check-unattended.sh:3083`) joins the protocol's §8 key column to the
  example conf's `KEY=` lines in both directions; the initialiser block is
  `tools/unattended/unattended.sh:493-499`.
- `memory/guides/UNATTENDED-PROTOCOL.md` is 65692 bytes against a declared 65692, and the unattended
  Skill render is 10211 against 10240 (`tools/template-size-limits.txt`). Both PINNED at `6473ae38`
  on 2026-10-09.
- `--preflight` can run more than once in a run's life (TOOL-cBriefedPilot-5 records it re-pinning
  on every invocation), and a run may edit the kickoff kit itself.

### Data model

The list rule 1 compares against, by the build README's `opened:` date at BASE:

| `PROMPT_BRIEF_SKELETON_CUTOFF` | List | Checker run |
|---|---|---|
| blank | the five, and the key is announced as off on stderr | no |
| set, `opened:` before it | the five | no |
| set, `opened:` on or after it | the skeleton's list at BASE | yes |

The five stay as TOOL-aQuotedBrief-1 builds them. They are the grandfather list and the floor S4
checks the skeleton against, so a kickoff checker that renames or reorders one of them refuses
instead of silently loosening rule 1. At KICK-aRoutedQuill-1 rev-3 the skeleton's list is those five
followed by `### Limitations` and `### Reuse`.

`PROMPT_BRIEF_SKELETON_CUTOFF` is read beside `PROMPT_BRIEF_CUTOFF` and only matters for a record
that key grades: with `PROMPT_BRIEF_CUTOFF` blank nothing is graded and this key is never read.

### The read

`read_brief_subheads`, run at most once per preflight:

1. `resolve_kickoff_checker` returns the checker's repo-relative path, or refuses.
2. The checker's blob at BASE is written to a scratch file through the same BASE reader
   `check_prompt_brief` uses for records (UNVERIFIED until it lands), and removed on exit. A path
   absent at BASE refuses.
3. `bash <scratch file> --brief-skeleton` runs; a non-zero exit refuses, naming the blob and the code.
4. The `### ` lines between `## The brief` and the next `## ` heading are the list; an empty list
   refuses.
5. The five must appear in the list in their order; otherwise the read refuses, naming the first one
   missing or out of place.

The blob is read at BASE because the rule a record is graded by must be as old as the authorization
that record is part of. Its cost is one `git show`, one bash start and at most one `git ls-files`.

### Resolution

`resolve_kickoff_checker` tries three rungs and stops at the first hit:

- The receipt row, then the two probes, through
  `resolve_kit_dir "$py" session-kickoff manifest-check.sh "$KIT_DIR"`. The arguments are a kit home
  and an anchor basename, the form every sibling call in this driver passes, so no sibling path is
  spelled.
- `git ls-files -- manifest-check.sh '*/manifest-check.sh'`, accepted only when it prints exactly
  one path. It is the rung the kickoff kit uses for gov's own placement, derived from the index.

The refusal names the receipt path, both probe paths and the tracked count. It fires only past the
key, so a tree that grades nothing on the skeleton never pays for or trips over the lookup.

### The requires decision

`tools/unattended/kit.toml` names `kickoff-manifest` in `requires`. Past the key a prompt-mode
preflight cannot pass without the checker, so the dependency is hard, and `requires` surfaces it at
install time: `plan` prints `UNMET` and `apply` refuses. Relying on the default set leaves a
`--kits` selection that omits the kickoff kit installing cleanly and then refusing every prompt-mode
run. Check 7e (`tools/govkit/govkit.py:2344-2356`) still passes, because the unattended entry is
reachable through `--all`.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `PROMPT_BRIEF_SKELETON_CUTOFF` | conf key | none: conf keys carry no naming cell |
| `read_brief_subheads` | shell function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_brief_subheads --as sh.function` answered OK |
| `resolve_kickoff_checker` | shell function | `sh.function`; `--suggest resolve_kickoff_checker --as sh.function` answered OK |

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `tools/unattended/.unattended.conf.example` · `tools/unattended/PROTOCOL.template.md` · `tools/unattended/VERBS.template.md` · `tools/unattended/kit.toml` · `memory/guides/UNATTENDED-PROTOCOL.md` · `memory/guides/UNATTENDED-VERBS.md` · `.unattended.conf` · `.claude/skills/unattended/SKILL.md` · `memory/guides/SESSION-KICKOFF.md` · `memory/map/generated/symbols.json` · `tools/template-size-limits.txt`

### Rollout

- Lands at order 6, after TOOL-aQuotedBrief-1 is on main and after KICK-aRoutedQuill-1. It shares
  its step with the trial alone, which touches no file the kickoff manifest watches.
- `.unattended.conf` declares the key at the day after this unit lands, the rule its
  `PROMPT_BRIEF_CUTOFF` comment states, so no prompt-mode run in flight is refused by a merge.
  Gov's own prompt-mode builds opened from that day are graded on seven; earlier ones keep five.
- The protocol has no headroom, so the new §8 row is paid for by raising the protocol's declared
  ceiling in `tools/template-size-limits.txt` by the row's measured bytes, in the same commit, with
  the comment there naming this unit. That is the owner's ruling of 2026-10-09, which covers
  TOOL-aQuotedBrief-1's own row at the same ceiling too.
- The unattended kit version moves once, in the run's mint after its last unit, across every
  carrier `tools/check-kit-versions.sh` and `govkit.py selfcheck` name, the Skill render among them;
  `govkit.py selfcheck` runs after it.
- The kickoff manifest owes `last-audit` with a delta line in the commit message, and
  `gen_map.py --write` runs before the push.
- No adopter migration: the example ships the key blank, which is off and says so.

### Alternatives rejected

- **Adding the two sub-heads as more literals.** Two spellings of one shape in two kits is the drift
  this unit exists to remove.
- **Reading the working-tree checker.** A run can edit the kickoff kit, and preflight runs more than
  once, so the rule would move under a record already authorized.
- **A conf key naming the checker's path,** as `KICKOFF_ENGINE` names the engine. Every adopter would
  declare it and a blank would need its own refusal, while the receipt already records where govkit
  put the checker.
- **Deriving the checker beside `KICKOFF_ENGINE`.** At an adopter the engine is a per-machine link
  outside the repository, while the checker lands at the install prefix.
- **Grading seven sub-heads for every record.** It would red records written under the five.
- **Relying on the default selection instead of `requires`.** See "The requires decision".

## 5. Production-readiness checklist

- security — no new write path. The driver runs a checker blob from the pinned BASE, which the
  authorization already trusts, and never a working-tree copy a run could have edited.
- perf / scale — at most one `git ls-files`, one `git show` and one bash start per preflight, and
  none for a tree whose graded records all predate the key.
- error / empty / loading states — an unresolvable checker, an ambiguous one, a blob absent at BASE,
  a verb that fails, an empty list and a list missing one of the five each refuse by name.
- observability — each refusal names the record or the blob and the sub-head at fault; a blank key
  is announced on stderr.
- risks — whether TOOL-aQuotedBrief-1's rule 1 admits a sub-head outside its list is open until it
  lands (F1). The protocol's ceiling rises by the new row's bytes. An adopter that installed the
  unattended kit without the kickoff kit reads `UNMET` at its next `govkit plan`.
- testing — arms in `tools/unattended/unattended.test.sh` over the preflight fixtures
  TOOL-aQuotedBrief-1 adds, with a fixture checker whose skeleton the arm controls; observed RED
  first, and the suite runs once, after the build.
- migration — none: a blank key is off, and a set key grandfathers every README opened before it.
- user docs — the verbs file and the protocol's §8 row are this path's user docs.

## 6. Acceptance criteria

- **AC1** — When `--preflight` runs over a prompt-mode README opened on or after
  `PROMPT_BRIEF_SKELETON_CUTOFF` whose record at BASE carries the five sub-heads and no
  `### Limitations`, it refuses at the brief check naming the record, rule 1 and `### Limitations`,
  and creates no `RUN.md`.
  Red when: the five-sub-head record is admitted, or a run-state file is written before the refusal.
- **AC2** — When that record carries the seven sub-heads the fixture checker's `--brief-skeleton`
  prints, in that order and each non-empty, `--preflight` prints `preflight OK`.
  Red when: a record matching the skeleton is refused.
- **AC3** — When the README's `opened:` precedes a declared `PROMPT_BRIEF_SKELETON_CUTOFF`, a
  five-sub-head record prints `preflight OK`, and the fixture's spawn log holds no `--brief-skeleton`
  call.
  Red when: a grandfathered record is graded on seven, or the checker runs for it.
- **AC4** — When `PROMPT_BRIEF_SKELETON_CUTOFF` is blank, `--preflight` over AC1's fixture prints
  `preflight OK` and names the key as off on stderr.
  Red when: a blank key refuses, or stays silent.
- **AC5** — When no checker resolves (no receipt row, neither probe, no tracked `manifest-check.sh`),
  and again when two are tracked, `--preflight` past the key refuses naming the receipt, both probes
  and the tracked count.
  Red when: an unresolvable or ambiguous checker falls back to the five.
- **AC6** — When the checker blob at BASE exits non-zero on `--brief-skeleton`, prints a list without
  `### Items`, or prints `### Gates` before `### Acceptance`, `--preflight` refuses naming the blob and
  the sub-head at fault.
  Red when: a checker without the verb, or a skeleton that lost one of the five, passes.
- **AC7** — When the fixture commits a checker whose skeleton carries `### Reuse` and the working tree
  then edits it out, a record without `### Reuse` is still refused by `--preflight`.
  Red when: the list follows the working tree instead of BASE.
- **AC8** — When `grep -n PROMPT_BRIEF_SKELETON_CUTOFF` runs over
  `tools/unattended/.unattended.conf.example`, `memory/guides/UNATTENDED-PROTOCOL.md` and
  `tools/unattended/unattended.sh`, it finds the blank example line, the §8 row and the initialiser
  entry.
  Red when: any of the three is missing.
- **AC9** — When `grep -n -- '--brief-skeleton' memory/guides/UNATTENDED-VERBS.md` runs, it finds the
  prompt path's step 3 naming the verb as the source of `## The brief`'s sub-heads.
  Red when: the render names no source, or spells the sub-heads itself.
- **AC10** — When `python tools/govkit/govkit.py plan` runs for a scratch target with `--kits` naming
  the unattended kit and its other requirements but not the kickoff kit, it prints an `UNMET` row
  naming `kickoff-manifest`.
  Red when: that selection plans clean.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `unattended protocol size` · `unattended skill size` · `harness arms (fail branches armed or pinned)` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `kickoff-manifest ratchet` · `check-wiring self-test` · `lexicon naming predicates` · `memory hygiene` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · the driver TOOL-aQuotedBrief-1 lands, which grades the five and never runs the checker · none

## 8. Open questions

- **FACT-QUESTION · F1 — Does TOOL-aQuotedBrief-1's rule 1 admit an extra sub-head?**
  The question is whether that rule, as built, admits a `###` sub-head outside its list. Probe: once
  it lands, `--preflight` over a pre-key fixture whose record carries the five plus `### Limitations`. Deciding observation: `preflight OK` means rule 1 is an in-order subsequence; a
  refusal naming rule 1 means it is an exact match. Liveness: the same fixture without `### Goal`
  must refuse, so the probe can move.
  If it is an exact match, a README opened before the key but written from the seven-sub-head
  skeleton is refused. (a) This unit relaxes rule 1 to an in-order subsequence for both lists, which
  admits extra sub-heads and never a missing one. (b) Rule 1 stays exact, and the verbs file tells a
  pre-key run to write the five.
  Recommendation: (a), because it keeps one rule and one sentence in the verbs file.
  RESOLVED (owner, 2026-10-09): (a), if the probe shows an exact match.
  Observed (agent, 2026-10-10): rule 1's awk, run from the driver at `77d9cdf8` over a record with the
  five plus `### Limitations`, printed `rule 1`; the five alone printed nothing, and the five without
  `### Goal` printed `rule 1`, so the probe moved. Rule 1 was an exact match, and (a) is built.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft.
- rev-2 · 2026-10-09 · §4 · §5 · §8 · owner resolves F1 (a) and rules that the protocol's ceiling
  rises by the new row's bytes rather than the protocol being trimmed.
- rev-3 · 2026-10-10 · §2 · §4 · §8 · F1's probe observed an exact match, so S1 carries (a); the read's
  refusals are one check, 117; the key is read at the default-branch side of BASE; the conf date is
  the day after landing; the kit version moves in the run's mint, not in this pass.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` named `resolve_kit_dir` as a SEAM installed in 67 files, and it
is the seam this unit extends: `resolve_kickoff_checker` calls it, then adds the tracked-anchor rung
the kickoff kit's `resolve_kit_file` already uses for gov's placement. The list itself extends
`check_prompt_brief`, which TOOL-aQuotedBrief-1 builds, and reads the verb KICK-aRoutedQuill-1 adds;
no existing reader of a sibling kit's verb output at BASE fits.

Recall terms used: `preflight prompt record brief sibling kit resolve_kit_dir receipt cutoff opened
BASE task-skeleton requires` — which surfaced `TOOL-aQuotedBrief-1`, `TOOL-aQuotedBrief-3`,
`TOOL-dDerivedDocket-41`, `TOOL-dUnstuckLanding-4`, `TOOL-aSealedCaravan-6` and `TOOL-cBriefedPilot-5`.
