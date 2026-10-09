# TOOL-aQuotedBrief-4 — the brief cutoff is read at the owner's side of BASE, and term 7 says when it is off

**Status:** SPECCED · rev-1 · 2026-10-09 · node a · Tier-2 · base 6473ae38 · streams tooling · order 3

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`check_prompt_brief` and `build-complete` term 7 gate on `PROMPT_BRIEF_CUTOFF` from the working-copy
conf, while every other input they grade is pinned to BASE. A run that blanks the key, or moves it
past its README's `opened:` date, after preflight closes green with no brief item graded, and term 7
says nothing when it is off. This unit reads the key at the default-branch side of the pinned BASE,
the way `SPEC_AUDIT_DEFAULT` is read, and announces an off cutoff at close. It closes closing-review
round 1 H1 and the three medium duplicates of it, M1 (ids 6, 2, 11 and 18).

## 2. Scope (IN)

- **S1** — `read_brief_cutoff` in `tools/unattended/unattended.sh` takes a commit and prints the
  value `PROMPT_BRIEF_CUTOFF` holds in `.unattended.conf` at that commit. It evaluates the blob in a
  subshell with the key blanked first and a sentinel printed from inside the evaluated text, the idiom
  `check_authorization` uses for `SPEC_AUDIT_DEFAULT`. It returns 2 when the blob does not evaluate to
  the end, and prints nothing for an absent blob. Observed by AC1 and AC4.
- **S2** — The commit read is the default-branch side of the pinned BASE: BASE itself on the
  default-branch anchor, and the merge-base of the observed anchor tip and BASE on the run-branch
  anchor, exactly as `check_authorization` computes `_cb`. Observed by AC2.
- **S3** — `check_prompt_brief` and `check_brief_items` both gate on that value and on nothing read
  from the working copy. An unevaluable blob refuses at preflight with a new numbered check and leaves
  term 7 unmet with a message naming it. Observed by AC1, AC2 and AC4.
- **S4** — When the value is blank or not a date, term 7 is met and the close says the term is off,
  through the same channel term 6 uses for a blank `SPEC_THIN_CUTOFF`. Observed by AC3.
- **S5** — The prompt-record arms of `tools/unattended/unattended.test.sh` that append the cutoff to
  the fixture conf put it where the reader now looks: on the fixture's default branch for a run-branch
  run. Observed by AC5.

## 3. Non-goals (OUT)

- Refactoring the existing `SPEC_AUDIT_DEFAULT` read onto the new reader. It works and carries its own
  numbered refusals; moving it is a change nobody measured.
- `SPEC_THIN_CUTOFF` and `UNITS_REGION_CUTOFF`, which round 1 noted are read from the working copy
  the same way. They are not this build's keys.
- Recording whether preflight graded the run as a run-state fact. Reading the same commit at both
  ends gives one answer without a second record.

### Edges

- **hands-off** `TOOL-aQuotedBrief-6` — the cutoff read at BASE, which that unit's arms set up for.

## 4. Design

### Evidence

Read at `5e2187386` on 2026-10-09.

- `check_prompt_brief` tests `${PROMPT_BRIEF_CUTOFF:-}` from the conf sourced at startup and prints a
  NOTE when it is off; `check_brief_items` tests the same variable and returns 0 silently.
- `check_authorization` reads `SPEC_AUDIT_DEFAULT` from `GIT show "$_cb:.unattended.conf"`, evaluated
  with `exec 3>&1` and an `OK` sentinel, and refuses an unevaluable blob at check 55.
- Term 6's off-state is announced in `DOD_OUT` on its met path, the `note — the project declares no
  SPEC_THIN_CUTOFF` line in the `build-complete` arm of `dod_met`.
- This build committed a conf edit itself, and nothing grades a run's own edit to this key.

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `read_brief_cutoff` | function | `sh.function`; `python tools/lexicon/lexicon.py --suggest read_brief_cutoff --as sh.function` answered OK |

The refusal takes the next free driver fail number at build time.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `memory/map/generated/symbols.json`

### Alternatives rejected

- **A run-state fact written at preflight, keyed on by term 7.** It is a second record of one
  decision, and a run edits its own run-state file.
- **No announcement at close.** Spec 3's S3 silence covers runs term 7 does not apply to; a cutoff that
  is OFF is a switch the owner should see, as term 6's is.

## 5. Production-readiness checklist

- security — narrows what a run can turn off by editing its own conf; grants nothing.
- perf / scale — one `git show` and one subshell per check, read once each.
- error / empty / loading states — an absent blob is off; an unevaluable blob refuses rather than
  reading as off.
- observability — the off state is announced at both ends.
- risks — a project whose default branch lacks the key sees the term off until it lands there, which
  is the intended reading.
- testing — arms in `tools/unattended/unattended.test.sh`, run once at VERIFYING.
- migration — none.
- user docs — none: no carrier states where the key is read.

## 6. Acceptance criteria

- **AC1** — When a prompt-mode run commits `PROMPT_BRIEF_CUTOFF=""` on its own branch over a default
  branch declaring a date, `--preflight` still grades its record and refuses a record with no brief.
  Red when: the run's own blank turns the check off.
- **AC2** — When the same blank is committed after preflight, `--close` still reports term 7 unmet for
  an unbuilt `planned` item.
  Red when: term 7 reads the working-copy value.
- **AC3** — When the default branch's conf leaves the key blank, `--close` meets term 7 and its
  `build-complete` output names `PROMPT_BRIEF_CUTOFF` as off.
  Red when: an off term is silent.
- **AC4** — When the default branch's conf ends in `return`, `--preflight` refuses at the new check.
  Red when: an unevaluable conf reads as an off cutoff.
- **AC5** — When `grep -c "PROMPT_BRIEF_CUTOFF" tools/unattended/unattended.test.sh` runs, every
  prompt-record arm still passes in the slice of its block.
  Red when: an arm grades nothing because its cutoff landed where the reader no longer looks.

## 7. Gates

`unattended kit gate` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the pre-unit driver, which reads the working copy · none

## 8. Open questions

- **F1 — Is an off cutoff announced at close?**
  Round 1's duplicate fixes disagreed. RESOLVED (agent, 2026-10-09, delegated): yes, through term 6's
  channel; it is the option that satisfies the most criteria, and it trips no veto.

## 9. Revision log

- rev-1 · 2026-10-09 · initial draft, promoted from closing review round 1 H1 and M1.

## 10. Reuse audit

`reuse_lookup.py "record a self-contained brief of an unattended prompt-mode run, quoting session
context, and refuse unrelated commits on the run branch"` found no seam for a conf read at a commit.
The extended seam is the `SPEC_AUDIT_DEFAULT` read in `check_authorization`, whose blank-first,
sentinel-evaluated subshell this unit copies for one more key, and the `_cb` merge-base it computes.

Recall terms used: `prompt record verbatim authorized-by prompt published anchor branch tip
self-authorization orientation AskUserQuestion owner turn build folder roster` — the build's query,
which surfaced `TOOL-aEvidencedLens-22` and the `SPEC_AUDIT_DEFAULT` default-branch-side ruling.
