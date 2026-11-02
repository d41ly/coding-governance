# TOOL-dFoldedAudit-13 — one read-only driver read answers whether a run takes the fold rule

**Status:** CLOSED · rev-2 · 2026-11-02 · node d · Tier-2 · base f055a11b · streams tooling · order 100

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-13-ledger.md](../build/2026-11-02-build-TOOL-dFoldedAudit-13-ledger.md) | journal | — |
| [2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-1-promotion-notes.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-2-spec-stage-returns.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-9-3-cross-read-return.md) | journal | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |
| [2026-11-02-prompt-TOOL-dFoldedAudit-13-build-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-13-build-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-13-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-13-spec-brief.md) | research | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-9-fix-brief.md) | research | TOOL-dFoldedAudit-9 TOOL-dFoldedAudit-10 TOOL-dFoldedAudit-11 TOOL-dFoldedAudit-12 TOOL-dFoldedAudit-14 TOOL-dFoldedAudit-15 |

<!-- /gen:spec-records -->

## 1. Goal

The `disposal` a caller passes comes from one driver answer that applies the cutoff, the run's date
and the policy key together, so an attended run keeps the old rule under a blank cutoff, an adopter
with no policy kit has a route, and a fold under any other answer is refused with no run-state file.
This closes H5, M1 and M6 of
`memory/builds/dFoldedAudit/reviews/2026-11-02-review-TOOL-dFoldedAudit-1-2-3-4-5-6-7-8-closing-diff-round1.md`.

## 2. Scope (IN)

- **S1** — `read_spec_disposal`, a new function in `tools/unattended/unattended.sh`, derives the one
  answer from `read_spec_exit_rule` (`tools/unattended/unattended.sh:12754`): `by-nature`, `promote-all`,
  `absent` or `refused`. With no run-state file it dates the run today. It writes nothing. Observed by
  AC1, AC2, AC3, AC4, AC5 and AC6.
- **S2** — `--plan <slug> --paths` prints one `spec-disposal:` line between its `roster:` and `next:`
  lines. Every other `--plan` form prints what it prints today. Observed by AC1 and AC7.
- **S3** — `--record-round` refuses a `local` finding row or a `--sibling` row when the answer is not
  `by-nature`, before it writes a byte, through `check_chain_fault`. Observed by AC8 and AC11.
- **S4** — `tools/roles/SKILL.template.md` and its render tell the caller to copy that line. Neither
  gains a line. Observed by AC9 and AC10.
- **S5** — The sentence H5 and M6 name in the "Drive the build as ONE program" bullet of
  `tools/unattended/VERBS.template.md`, and its render, states that line and tells a caller to copy
  it. No other sentence of that carrier moves. Observed by AC9.
- **S6** — The args header of `tools/workflows/unattended-build.template.js`, and its render, name
  that line and not the policy read. A comment alone moves. Observed by AC9.
- **S7** — The existing arms that S2 and S3 reach move with them. The two `--plan --paths` parity arms
  read past the new line, and `write_chain_fixture`, with any suite fixture that writes a `local` or
  `--sibling` round by then, declares a dated cutoff. NOT OBSERVED by a criterion: a suite edit, which
  the close observes through the `New arm:` lines of §7.

## 3. Non-goals (OUT)

- No new verb. Check 26 joins a verb to three carriers, and `--paths` is the output mode this repo
  already chose for that reason (`tools/unattended/unattended.sh:744-747`).
- No `--status` line. `verb_status` refuses with no run-state file
  (`tools/unattended/unattended.sh:8244`), and an attended run has none.
- `--plan` with no `--paths`, and `--plan --framed` with no `--paths`, do not move. Check 30 runs the
  framed form over every build (`tools/unattended/check-unattended.sh:5686`), and this read costs a
  `git log` per build there and a Python start past a dated cutoff.
- The harness does not read the line. It still takes `disposal` from its caller and refuses a value
  outside its pair (`tools/workflows/unattended-build.template.js:340`), and nothing else in it moves.
- `--review`, `check_spec_exit` and check 2 do not move. They already read the rule through
  `read_spec_exit_rule`.
- `tools/roles/SKILL.template.md:19`, which still calls `--plan` the one driver verb, is L4 of the
  report and the batch unit's work. `disposal` reaching `tier2-review` is M12, the same unit's.
- This unit reads the cutoff through `read_spec_exit_rule` and adds no read of its own at BASE. That
  is M4, which `TOOL-dFoldedAudit-9` owns, and this read inherits it.
- An attended run on a build that holds a finished `RUN.md` answers by that record's date. It is the
  only date in the tree, and a pre-cutoff record then answers `absent`, the conservative side.

### Edges

- **hands-off** `TOOL-dFoldedAudit-15` — the `--plan` bullet of `tools/unattended/VERBS.template.md` does
  not gain this line here. The report orders no such sentence, and that unit's batch writes it.
- **hands-off** external — the `--record-round` refusal list of `tools/unattended/VERBS.template.md` does
  not gain S3's refusal. The report orders no such sentence and no sentence there turns false. The
  wrap-up names it for the owner.

## 4. Design

Line citations are to the tree at the header's base.

### The read

```bash
# THE ONE ANSWER A CALLER COPIES (TOOL-dFoldedAudit-13). `_sd_value` is by-nature, promote-all, absent
# or refused, and `_se_why` holds a refused read, as `read_spec_exit_rule` leaves it. Read-only, and
# called in the caller's shell, because a refusal in `$( )` loses its status.
#
# NO RUN-STATE FILE IS AN ATTENDED RUN, WHICH BEGINS TODAY. `read_spec_exit_rule` reads a path with no
# history as past any cutoff, which is right for a record nothing has committed yet and wrong for a
# run with no record at all under a cutoff dated ahead of it.
read_spec_disposal() { # run-state file · slug -> sets _sd_value
  local now
  _se_why=""
  if [ ! -f "$1" ]; then
    now=$(read_utc_now)
    if [ -n "$now" ] && [[ "${now%%T*}" < "$SPEC_FOLD_CUTOFF" ]]; then _sd_value=absent; return 0; fi
  fi
  read_spec_exit_rule "$1" "$2" "$2-spec-set"
  case "$_se_rule:$_se_why" in
    old:) _sd_value=absent ;;
    folds:) _sd_value=by-nature ;;
    counted:) _sd_value=promote-all ;;
    *) _sd_value=refused ;;
  esac
}
```

The third argument is any subject that is not the slug, which is all `read_spec_exit_rule` asks of
it at `:12757`. The harness's subject is `<slug>-spec-set-r<N>`, and this spells its stem. A blank
cutoff sorts below every date, so the first test falls through and the read answers `old`, which
spawns no Python. An unavailable clock leaves the read on `read_spec_exit_rule`'s answer. Any
non-empty `_se_why` reads as refused whatever `_se_rule` holds, because `TOOL-dFoldedAudit-9` sets it
beside `old` for a cutoff it cannot know.

### The line

In `verb_plan` (`tools/unattended/unattended.sh:5986`), directly above `echo "next: ..."` at `:6195`:

```bash
if [ -n "$PLAN_PATHS" ]; then
  runmd_of "$slug" >/dev/null
  read_spec_disposal "$_runmd" "$slug"
  printf 'spec-disposal: %s\n' "$_sd_value${_se_why:+ - ${_se_why%%$'\n'*}}"
fi
```

| Line | When |
|---|---|
| `spec-disposal: by-nature` | past the cutoff and the key answers `by-nature`, or the kit default where no policy kit resolves, with the reader's note on stderr |
| `spec-disposal: promote-all` | past the cutoff and the key answers `promote-all` |
| `spec-disposal: absent` | blank cutoff, a record begun before it, or no record today ahead of it |
| `spec-disposal: refused - <why>` | the policy read refused, its first line |

The caller's rule is one sentence: pass the value as `disposal`, and omit the arg on `absent`. A copied
`refused - ...` meets `TYPED` at `tools/workflows/unattended-build.template.js:340` and throws, so a
refused read stops at the harness with no further rule. `--plan` itself still exits 0 and prints every
row, because it is the resume route and a policy file must not take that down with it.

The line carries no TAB, so every `--paths` caller, which skips a line with fewer than four fields
(`tools/unattended/unattended.sh:5896-5898`), skips it. It sits above `next:`, so `next:` stays last.

### The `--record-round` refusal

`write_chain_round` (`tools/unattended/unattended.sh:13494`) marks a fold in its two row loops, at
`:13525` and `:13531`: a `local` nature in the first, any row in the second, since a sibling edit is a
fold (`tools/unattended/VERBS.template.md:287`). After the second loop and before the count test at
`:13535`:

```bash
if [ -n "$folds" ]; then
  runmd_of "$slug" >/dev/null
  read_spec_disposal "$_runmd" "$slug"
  [ "$_sd_value" = by-nature ] || { check_chain_fault "a local or --sibling row folds, and this run's spec disposal reads $_sd_value${_se_why:+, $_se_why}, which folds nothing"; return 1; }
fi
```

The block takes its own `runmd_of`, because the batch unit takes `rel` out of this function. The read
is lazy, so a round of `new-mechanism` rows spawns nothing and passes under every answer.
`check_chain_fault` is the verb's one refusal site, so the driver stays at 318 raw `fail` sites and
`fail 118` stays at one. M1's judged text names the `local` row. The `--sibling` half is the same
class by the verbs carrier's own sentence, so it is the same branch and not a second one.

### The carriers

`tools/roles/SKILL.template.md:50-52` becomes:

```
`handoff.py stage-efforts spec-write`; `specAudit` only where the build
README declares `spec-audit:`; `disposal` beside it, the value on that read's
`spec-disposal:` line, omitted on `absent`. Act on its `nextAction`.
```

"That read" is the `--plan <slug> --paths` the stage opens with, so the Skill spawns nothing new. The
file stays at 102 lines. `bash tools/roles/adopt-roles.sh --scaffold` writes the render.

The sentence at `tools/unattended/VERBS.template.md:777-778` becomes:

> A caller passes `disposal`, the value of the `spec-disposal:` line `--plan <slug> --paths` prints,
> and omits the arg on `absent`. That line is the one answer `SPEC_FOLD_CUTOFF`, the run's first-commit
> date and `review.spec-audit.disposal` give together: `by-nature`, `promote-all`, `absent`, or
> `refused - <why>`, with the run dated today where no run-state file exists and the key at its kit
> default where no policy kit resolves.

The sentence at `:779` follows unchanged. `bash tools/unattended/adopt-unattended.sh` writes the render,
as the kit's `[[regenerate]]` (`tools/unattended/kit.toml:193-194`) does. This is the one sentence of
that carrier the report orders changed, which is why §3's edges leave the rest to the batch unit and the
wrap-up.

`tools/workflows/unattended-build.template.js:183-184` becomes, on the same two lines:

```
//   disposal: "by-nature" | "promote-all",          // optional: the `spec-disposal:` line of `--plan --paths`,
//                                                   //   which this runtime cannot read. ABSENT = a run
```

The render follows through the kit's `[[regenerate]]` (`tools/workflows/kit.toml:116-117`).

### The arms that move

`tools/unattended/unattended.test.sh:3267` and `:3269` compare `--paths` with the padded table line
for line, and S2 adds a line to one side. Each reads `--paths` through `grep -v '^spec-disposal: '`,
and the padded side stays unfiltered, so the arm still pins that nothing else differs.

`write_chain_fixture` (`tools/unattended/unattended.test.sh:2634`) holds a conf with no cutoff, so
under S3 all of its `local` rows would refuse. It appends `SPEC_FOLD_CUTOFF="2000-01-01"` before its
commit, which leaves the fixture on the kit default `by-nature`, and no arm depends on the day it
runs. A unit ahead of this one may have added a fixture of the same shape, so the builder greps the
suite for `/local/` and `--sibling` rounds, and each fixture they run in takes the same line.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `read_spec_disposal` | `sh.function` | `lexicon.py --suggest` answered OK on 2026-11-02 |
| `_sd_value`, `folds` | variables | none |
| `spec-disposal:` | a `--plan --paths` output line, spelled as `roster:` and `next:` are | this spec's arms |

No verb, flag, conf key, policy key or check number is minted.

### Rollout

Every answer is `absent` while `SPEC_FOLD_CUTOFF` is blank, which `.unattended.conf:488` is until this
build's close writes the landing date. From then on a kit update moves no adopter whose conf is blank.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`
- `memory/guides/UNATTENDED-VERBS.md`
- `tools/roles/SKILL.template.md`
- `.claude/skills/build/SKILL.md`
- `tools/workflows/unattended-build.template.js`
- `tools/workflows/unattended-build.js`

The harness pair is beyond the brief's estimate. Its header is a third carrier of the sentence H5 names,
and leaving it would keep the old route written down.

### Alternatives rejected

- **A new read-only verb**, M1's first example. It owes a header line, a verbs entry and a Skill
  invocation under check 26, and the Skill row is pinned. M6's judged fix names this output mode.
- **The lesser fix, a conditional Skill sentence.** It leaves the comparison to the caller, keeps two
  readers of one cutoff, and gives an adopter with no policy kit no route.
- **The line on every `--plan`.** The cost §3 states, and it breaks the byte-identical default the
  padded table's arm pins at `tools/unattended/unattended.test.sh:3242-3243`.
- **`--plan` exiting 1 on a refused read.** It is the resume route, and the unit rows are still true.

## 5. Production-readiness checklist

- **security** — No new write path. S3 narrows one: `--record-round` now refuses a fold the run's rule
  does not admit, which was M1's gap, because the value a caller passes was its own copy. The read
  takes no input beyond the slug `check_slug` already screens.
- **perf / scale** — `--plan --paths` adds at most one `git log`, one `git diff --cached`, one
  `--follow` walk and, past a dated cutoff, one Python start. It runs between dispatches, not per
  build. `--record-round` adds the same only on a round carrying a fold.
- **error / empty / loading states** — A refused policy read prints `refused - <why>` and exits 0. No
  run-state file is the attended case and answers by today. A blank cutoff answers `absent`.
- **observability** — The answer is on stdout on every read a caller already makes. An absent policy
  kit keeps the reader's note on stderr.
- **risks** — S3 reds `write_chain_fixture`'s every round until S7 lands, so both land in one pass.
  The fixture confs of units 10 and 11 each declare `SPEC_FOLD_CUTOFF="2000-01-01"`, so neither builder
  meets S3 as a divergence.
  AC8's fixture carries a real rev, so unit 11's fold join passes there whichever runs first.
  `policy-value-with-no-route` is the class this closes, and `promote-all` is witnessed by AC3 and AC8.
- **testing** — Fixture repositories with no policy kit unless the arm is about the switch, committer
  dates pinned, and a dated cutoff either side of the record. No arm reads today's date except AC5,
  whose cutoff is 2099 and whose control is the year 2000.
- **migration** — None. The line is additive under `--paths`, and every caller skips a line with no TAB.
- **user docs** — `grep -ln -e 'disposal' -e 'SPEC_FOLD' help/*.md` prints nothing, so no page moves.

## 6. Acceptance criteria

Fixture U is a scratch git repository at `%TEMP%/fa13u` on branch `main` with no remote, holding a copy
of `tools/unattended/` whole, a `.unattended.conf` carrying `MEMORY_ROOT=memory`,
`DISPOSITION_CUTOFF="2000-01-01"` and `REVIEW_ROUNDS="1"`, and a build `memory/builds/tFix/` whose README
carries a roster and a `gen:build-units` region with one row, as the suite's `readme`, `mkspec` and
`roster` helpers write them, for one tracked spec `TOOL-tFix-1`. That spec sits at `rev-2` with a
Revision log line for it, so a fold row's rev resolves against the tree. Each criterion states
`SPEC_FOLD_CUTOFF`. Fixture U holds no `RUN.md` unless a criterion adds one, and an added one is
built as the suite's `write_fold_fixture` builds it, with its first commit dated by
`GIT_COMMITTER_DATE`. Fixture P is U plus `tools/policy/policy.py`, `tools/policy/budgets.py` and
`tools/policy/catalogue.toml` at those paths. `$D` is `bash "$F/tools/unattended/unattended.sh"`, run with
the fixture as the working directory, with `GOV_REMOTE` and `GOV_DEFAULT_BRANCH` cleared. `$P` is
`$D --plan tFix --paths`, its stdout read alone unless a criterion says so.

- **AC1** — When fixture U's cutoff is blank, `$P` prints `spec-disposal: absent` between its `roster:`
  and `next:` lines, and its stderr holds no `no policy kit resolves`.
  Red when: the line reads the switch ahead of the cutoff, so it prints `by-nature`. This is H5's
  left-shift gate.
- **AC2** — When fixture U's cutoff is `2026-11-01` and it holds no `RUN.md`, `$P` prints
  `spec-disposal: by-nature` and its stderr holds `no policy kit resolves`. With a `RUN.md` first
  committed `2026-11-02T12:00:00 +0000`, the same line prints and
  `$D --review tFix --subject S1 --verdict "CLEAN WITH FIXES" --blockers 0 --highs 1 --minors 2 --folded 3 --promoted 0 --disposition fold`
  exits 0.
  Red when: an install with no policy kit has no answer, or the line and the exit rule disagree. This
  is M6's left-shift gate.
- **AC3** — When fixture P's cutoff is `2026-11-01` and it commits `.governance/policy.toml` setting
  `disposal = "promote-all"` under `[review.spec-audit]`, `$P` prints `spec-disposal: promote-all`. With a
  `RUN.md` as in AC2, `--highs 1 --minors 0 --folded 1 --promoted 0 --disposition fold` refuses with
  `which folds nothing`, and `--folded 0 --promoted 1 --disposition promote` exits 0.
  Red when: the line ignores the key.
- **AC4** — When fixture U's cutoff is `2026-11-01` and its `RUN.md` is first committed
  `2026-10-30T12:00:00 +0000`, `$P` prints `spec-disposal: absent`, and `--folded 0` on AC2's call refuses
  with `--folded and --promoted are counted only`.
  Red when: the line reads today's date for a run that has a record.
- **AC5** — When fixture U holds no `RUN.md` and its cutoff is `2099-01-01`, `$P` prints
  `spec-disposal: absent`. With a cutoff of `2000-01-01` it prints `spec-disposal: by-nature`.
  Red when: a run with no record reads as past a cutoff dated ahead of it.
- **AC6** — When fixture P's cutoff is `2026-11-01` and it commits `.governance/policy.toml` setting
  `disposal = "fold-all"` in its first commit, `$P` exits 0, prints a line opening
  `spec-disposal: refused - ` and still prints the `TOOL-tFix-1` row.
  Red when: a refused read takes `--plan` down, or reads the kit default.
- **AC7** — When `$D --plan tFix` and `$D --plan tFix --framed` run under any cutoff, their output
  piped through `grep -c 'spec-disposal:'` prints 0. In `$P`'s output the `spec-disposal:` line carries no
  TAB, and `next:` is the last line.
  Red when: the line reaches the padded table, or a four-field caller reads it as a row.
- **AC8** — When fixture U's cutoff is blank,
  `$D --record-round tFix --subject tFix-spec-set-r1 --audited TOOL-tFix-1 --blockers 0 --highs 1 --finding 7/HIGH/local/TOOL-tFix-1/TOOL-tFix-1/2`
  exits 1 printing `UNATTENDED check 118 FAILED — the spec-audit chain record refuses this: a local or --sibling row folds`,
  and no `-chain-rounds.md` file exists. Under fixture P with `disposal = "promote-all"` and a dated cutoff
  that call refuses the same way, and so does `--highs 0 --sibling TOOL-tFix-1@rev-2` in place of the
  `--finding`, while `--finding 8/HIGH/new-mechanism/TOOL-tFix-1/TOOL-tFix-2/1` exits 0. Under fixture U
  with a dated cutoff the first call exits 0.
  Red when: the verb reads neither the cutoff nor the switch, so a fold records under `promote-all`. This
  is M1's left-shift gate, and every case has no run-state file.
- **AC9** — When `grep -c 'spec-disposal:' tools/roles/SKILL.template.md .claude/skills/build/SKILL.md tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md tools/workflows/unattended-build.template.js tools/workflows/unattended-build.js`
  runs, every file prints at least 1, and the same `grep -c` for `policy.py get review.spec-audit.disposal`
  over the same six files prints 0 for each.
  Red when: a carrier keeps the old route, or a render was not regenerated.
- **AC10** — When `wc -l tools/roles/SKILL.template.md .claude/skills/build/SKILL.md` runs, each prints 102.
  figure: PINNED at 2026-11-02 at this spec's base.
  Red when: the Skill grows a line.
- **AC11** — When `grep -cE '(^|[^a-zA-Z_])fail [0-9]+ "' tools/unattended/unattended.sh` runs it prints
  318, and `grep -c 'fail 118' tools/unattended/unattended.sh` prints 1.
  figure: PINNED at 2026-11-02 at this spec's base. A unit ahead of this one in order shares a site by
  the same rule, so the figures hold through the build.
  Red when: S3 adds a `fail` site instead of calling `check_chain_fault`.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `unattended skill wiring` · `roles render wiring` · `roles render selftest` · `check-wiring self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `policy fixtures` · `workflow script syntax` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `kit version markers`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC4 AC5 AC6 AC7 · each answer of `--plan --paths` under its cutoff, staged with `read_spec_disposal` answering `by-nature` at its head · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 · the line and the spec exit over one fixture, with no policy kit and under `promote-all`, staged with the line printing the kit default · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/unattended.test.sh · covers AC8 · a `local` row and a `--sibling` row under `absent` and `promote-all` with no run-state file, staged with the fold branch deleted · `FLOOR_ASSERTIONS` raised by the executed count
New arm: tools/unattended/unattended.test.sh · covers AC7 · the two `--plan --paths` parity arms moved at `:3267` and `:3269`, staged with the filter dropped, which reds the line count · none
New arm: tools/unattended/unattended.test.sh · covers none · `write_chain_fixture` moved onto a dated cutoff, staged by blanking the cutoff, which reds every `local` round · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the closing review's H5, M1 and M6 and the promotion notes.
- rev-2 · 2026-11-02 · §3 · §4 · §5 · The `--plan` bullet is a `hands-off` to `TOOL-dFoldedAudit-15`, whose
  §8 F3 writes it, and the fixture edge retires with the conf lines units 10 and 11 now carry. M2's
  cross-read: the edge read that unit as leaving this carrier alone, and §4 and §5 pointed at the old
  edges. S3's refusal in the `--record-round` list stays `hands-off external`.

## 10. Reuse audit

The seams are `read_spec_exit_rule` (`tools/unattended/unattended.sh:12754`), which already holds the
cutoff, the record's date and the switch; the `--paths` output mode (`:744-747`), which the repo chose
over a new verb for this reason; `check_chain_fault` (`:13462`), the verb's one refusal site; and
`read_utc_now` (`:1712`). `reuse_lookup.py` ranked only dossiers and name-stem hits for this behaviour
and no seam beyond those. Recall returned the closing review's items and the `--plan` bullet of
`memory/guides/UNATTENDED-VERBS.md`, whose contract this line keeps.

Where the records and the source disagreed. The report's H5 and M1 fixes read as a new verb, and
the [budgets] tag of the promotion notes prices that against the Skill, so M6's judged form is the one
built: all three findings name "one driver answer", and M6 names where it prints. That tag and the
build brief call the Skill row pinned. `tools/template-size-limits.txt:162` pins the unattended Skill
and no row pins this one, so AC10 is this spec's own bound, kept for the brief's preference. M1 names
the `local` row, and the verbs carrier counts a sibling edit as a fold, so S3 takes both.

Recall terms used: `python tools/memory-recall/query.py "how does an attended build learn the spec audit disposal value and the cutoff" --terms "attended disposal cutoff policy-value route spec-exit plan paths output-mode switch read-only adopter"`.
Reuse probe used: `python tools/codebase-map/reuse_lookup.py "one read-only driver answer a caller copies for the disposal value"`.
