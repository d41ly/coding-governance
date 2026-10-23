# TOOL-dGroundRules-41 — the help page's install section held to the deferral line `--scaffold` prints, by the case that prints it

**Status:** OPEN · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 13

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-41-deviation-29.md](../build/2026-10-23-build-TOOL-dGroundRules-41-deviation-29.md) | deviation | — |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-13 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |
| [2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-35-43-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-42 TOOL-dGroundRules-43 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 33 and 34
(`memory/builds/dGroundRules/reviews/2026-10-23-review-TOOL-dGroundRules-33-34-spec-audit-round1.md`)
exited CONVERGED with finding **id 21 at HIGH**, which shares item **H3** with ids 2
(`TOOL-dGroundRules-39`), 17 (`TOOL-dGroundRules-40`) and 25 (`TOOL-dGroundRules-42`). Id 21 is H3
seen from blast radius, and the one criterion it alone names is `TOOL-dGroundRules-34` AC36, which
greps a bare `policy.md` that does not resolve from the repository root, where S36 names the help
page's `## Install` section. That criterion can never pass, and even repaired it only finds the
words `mirror deferred` somewhere in the section: the help page restates a line `adopt-policy.sh`
prints, and nothing holds the two equal. This unit is id 21's promotion. `adopter-fresh-target`,
the case that already captures the deferral line (`TOOL-dGroundRules-31` S4), checks that the help
page's `## Install` section carries that line, and the `policy fixtures` guard holds the help page,
so an edit to either side reruns the check. It repairs `TOOL-dGroundRules-34`, which sits at order
12, so it builds at order 13.

## 2. Scope (IN)

- **S1** — The parity. After `adopter-fresh-target` asserts the deferral line of its first
  `--scaffold`, it reads the source's `help/policy.md`, takes the lines between `## Install` and the
  next `## ` heading, splits the printed deferral line at the input name it carries, and asserts
  that one line of the section holds both halves, in order. A missing page, a missing section or no
  such line is the case's `WRONG` naming `help/policy.md` and the printed line.
  Observed by AC1, AC2, AC3.
- **S2** — The guard. The `policy fixtures` row of `tools/gate-legs.json` gains `help/policy.md`,
  spelled without `{prefix}` because the help tree sits at the repository root. Observed by AC5.
- **S3** — `TOOL-dGroundRules-34` AC36 restated whole: the `## Install` section of `help/policy.md`
  holds `mirror deferred` at least once. Observed by AC4.

## 3. Non-goals (OUT)

- The wording of the deferral line, `TOOL-dGroundRules-31` S1, and of the section,
  `TOOL-dGroundRules-34` S36. This unit holds them equal; it moves neither.
- Any other help page or any other printed line. One restated line, one parity.
- The narrowed rule for spelling kit files by bare name in criteria: `TOOL-dGroundRules-42`.
- The other corrupted criteria of item H3: `TOOL-dGroundRules-39` and `TOOL-dGroundRules-40`.

### Edges

- **consumes-from** `TOOL-dGroundRules-34` — S36's `## Install` section of the help page, which S1 holds to the deferral line `adopter-fresh-target` captures and S3 observes whole
- **hands-off** `TOOL-dGroundRules-48` — AC4, which that unit observes with the page path whole and pairs with `HELP_MOVED` (id 2 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-49` — AC5 and S2's guard line, which that unit observes through the leg query with the page path whole and through the guard trace (id 11 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-50` — `adopter-fresh-target`'s parity, which that unit makes print the page line it found (id 22 of the round-1 spec audit of units 35 to 43)
- **hands-off** `TOOL-dGroundRules-52` — AC4 and AC5, which that unit observes through units 48 and 49's literals (id 31 of the round-1 spec audit of units 35 to 43)

## 4. Design

### Evidence

Every line below was read on 2026-10-23 at `b9f7b5c4e`.

- `TOOL-dGroundRules-31` S1 prints
  `adopt-policy: mirror deferred · <the input the refusal names> has uncommitted changes · commit, then re-run --scaffold`,
  and its S4 has `adopter-fresh-target` assert that line on the first `--scaffold`.
- `TOOL-dGroundRules-31` S6 has the help page quote the line, and `TOOL-dGroundRules-34` S36 moves it
  under `## Install`; `TOOL-dGroundRules-1` S8 places the page at `help/policy.md`.
- `TOOL-dGroundRules-34` AC36 (:580-582) greps a bare `policy.md`, and the §6 rule at :426-427 names
  only kit files as bare names (review id 21).
- `python tools/check-spec-tokens.py --legs-for help/policy.md` printed `no guarded leg` on
  2026-10-23, before the page exists.

### The check

```text
adopter-fresh-target, after its deferral assertion (TOOL-dGroundRules-31 S4):
    line = the printed "adopt-policy: mirror deferred · ..." line
    head, tail = line split at the input name it carries
    section = lines of <source top>/help/policy.md after "## Install", up to the next "## "
    WRONG naming help/policy.md and line unless some l in section has head and then tail in it
```

The page is read in process, so `TOOL-dGroundRules-33`'s trace sees the read, and S2's guard line is
what keeps that trace green.

### Inventory

No identifier is minted. The check sits inside `adopter-fresh-target`.

### Files touched (estimate)

- `tools/policy/check_policy.py`
- `tools/gate-legs.json`

### Alternatives rejected

- **AC36 repaired alone.** It finds `mirror deferred` and passes a section whose instructions have
  drifted from what the verb prints.
- **The parity in `tools/policy/adopt-policy.test.sh`.** That suite's leg guard would also need the
  help page, and the case already holds the printed line; a second capture is a second carrier.

## 5. Production-readiness checklist

- security — N/A: one read of a tracked help page.
- perf / scale — one file read in a case that already runs.
- error / empty / loading states — a missing page, section or line is a named `WRONG`.
- observability — the `WRONG` prints the line the verb printed, so the fix is a paste.
- risks — a reworded section that drops the line reds the leg; that is the intent.
- testing — AC1 to AC5.
- migration — none.
- user docs — `help/policy.md` is the subject; this unit holds it current.

## 6. Acceptance criteria

Every command runs from the repository root. `check_policy.py` names the policy kit's file under the
kit, as `TOOL-dGroundRules-34` §6 does. Literal commands and stagings are spelled whole here, once,
and the criteria name them:

```text
INSTALL_LINES = awk '/^## Install/{f=1;next} /^## /{f=0} f' policy.md | grep -c "mirror deferred"
HELP_LEGS     = python tools/check-spec-tokens.py --legs-for policy.md
HELP_DRIFT    = in a scratch copy's help/policy.md, "re-run --scaffold" in the deferral line
                respelled "run --scaffold again"
HELP_MOVED    = in a scratch copy's help/policy.md, the deferral line moved under another "## " heading
```

- **AC1** — When `python check_policy.py --fixture adopter-fresh-target` runs on the built tree, it
  prints no `WRONG`.
  Red when: the help page's install section and the verb's deferral line disagree today.
- **AC2** — When `HELP_DRIFT` runs and then the AC1 command runs in that copy, it prints `WRONG`
  naming `policy.md` and carrying `re-run --scaffold`.
  Red when: the page's instruction drifts from what the verb prints with the leg green.
- **AC3** — When `HELP_MOVED` runs and then the AC1 command runs in that copy, it prints `WRONG`
  naming `policy.md`.
  Red when: the line counts wherever it sits, not in the section an installer reads.
- **AC4** — When `INSTALL_LINES` runs on the built tree, it prints `1` or more.
  Red when: the deferral line sits outside the section an installer reads.
- **AC5** — When `HELP_LEGS` runs on the built tree, its output names `policy fixtures`.
  Red when: an edit to the help page alone skips the leg that holds it.

## 7. Gates

`run-gates gov canary` · `measure-legs selftest` · `memory hygiene` · `run-gates canary`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run the case;
they are named by the arm line, because neither exists at this spec's base.

New arm: tools/policy/check_policy.py (`--fixture adopter-fresh-target`) · covers AC2 AC3 · the help page's deferral line respelled, then moved out of `## Install`, each in a scratch copy · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 21 (HIGH, item H3) of the round-1 spec
  audit of units 33 and 34, from the skeptic's corrected AC36 path and a parity the restated line
  owes, with units 1, 31 and 34's help-page items read on 2026-10-23.
- rev-2 · 2026-10-23 · §3 · the hands-off edges to `TOOL-dGroundRules-48`, `TOOL-dGroundRules-49`, `TOOL-dGroundRules-50`, `TOOL-dGroundRules-52`, the reciprocal ends the disposal of
  the round-1 spec audit of units 35 to 43 wrote; no scope or criterion moved.

## 10. Reuse audit

The seams extended are `adopter-fresh-target`, which already captures the deferral line
(`TOOL-dGroundRules-31` S4), and the `policy fixtures` row of `tools/gate-legs.json`; the guard
trace `TOOL-dGroundRules-33` builds is what demands S2's line.
`python tools/codebase-map/reuse_lookup.py "hold a help page line equal to the line a script prints"`
ranked name-stem hits, `check_line` and `render_line` of the runlog kit and `parse_conf_line` and
`unfenced_lines` of the memory-tree kit, none of which compares a document to a verb's output, and a
kit may not import a sibling kit; no existing seam fits the parity itself. The recall probe returned this audit's H3 and
`TOOL-aKeyedAnnotation-9`, the open ask on the spec-tokens paths join that drove the respelling;
both agree with source.

Recall terms used: `python tools/memory-recall/query.py "how is a criterion's path respelled to pass
the spec-tokens paths join" --terms "acceptance criterion path stripped prefix paths join basename
respelled spec-tokens literal fixture"`
