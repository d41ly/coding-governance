# TOOL-aClearedLedger-5 — the bar join denies a direct-check form the manifest declares above the bound, and its parity arm reads all three direct-check words

**Status:** CLOSED · rev-2 · 2026-11-13 · node a · Tier-1 · base 8db6f4be · streams tooling · order 5 · closes TOOL-aNimbleMend-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-13-build-TOOL-aClearedLedger-5-red-fix-1.md](../build/2026-11-13-build-TOOL-aClearedLedger-5-red-fix-1.md) | red-fix | — |
| [2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md](../build/2026-11-14-build-TOOL-aClearedLedger-1-2-observations.md) | journal | TOOL-aClearedLedger-1 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 TOOL-aClearedLedger-11 TOOL-aClearedLedger-12 TOOL-aClearedLedger-13 TOOL-aClearedLedger-14 TOOL-aClearedLedger-15 TOOL-aClearedLedger-16 |
| [2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-1-brief.md) | research | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |
| [2026-11-13-prompt-TOOL-aClearedLedger-5-1-spec-writer.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-5-1-spec-writer.md) | journal | — |
| [2026-11-13-prompt-TOOL-aClearedLedger-5-brief.md](../prompts/2026-11-13-prompt-TOOL-aClearedLedger-5-brief.md) | research | — |
| [2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md](../reviews/2026-11-13-review-TOOL-aClearedLedger-1-2-3-4-5-6-7-9-10-diff-review-round1.md) | diff-review | TOOL-aClearedLedger-1 TOOL-aClearedLedger-2 TOOL-aClearedLedger-3 TOOL-aClearedLedger-4 TOOL-aClearedLedger-6 TOOL-aClearedLedger-7 TOOL-aClearedLedger-9 TOOL-aClearedLedger-10 |

<!-- /gen:spec-records -->

## 1. Goal

The spec-token suite's manifest parity arm has been red since two landings moved the manifest past
it, and one cause prints two failure lines. This unit lets the bar join read a leg's ceiling from
the manifest it already parses, and lets the arm read every direct-check word, so the arm reads
green with three named exemptions deleted and none added.

## 2. Scope (IN)

- **S1** — `tools/check-spec-tokens.py` gains `DIRECT_CHECK_BOUND`, `DIRECT_CHECK_WORDS`,
  `derive_flag_suites` and `check_bar`. The bar join's three call sites ask `check_bar`, so a token
  spelling a `chunk = selftests` leg in a direct-check form, with a ceiling above the bound, is a
  `[bar]` hit whose reason names the leg and its ceiling. Observed by AC1, AC2 and AC3.
- **S2** — A direct-check form at or under the bound, and a case-scoped or longer spelling of a
  leg above it, stay admitted. Observed by AC2.
- **S3** — The parity arm of `tools/check-spec-tokens.test.sh` exempts a leg carrying any of the
  three direct-check words only at or under the bound, and grades every other leg through
  `check_bar`. `PARITY_EXEMPT` keeps `test_recall_floor.py` alone, and the branch that counted a
  leg neither graded nor exempt is deleted. Observed by AC4 and AC6.
  **Readers:**
  by name: `tools/check-spec-tokens.test.sh` alone spells this list, as `PARITY_EXEMPT`: at its
  assignment, in the argument list of the arm's inline python, and in the comment above it, which
  declares the three members by script name and is rewritten with them. The deleted branch's
  message is spelled at its one line of that file and nowhere else in product code.
  `tools/unattended/gate-guard.test.sh` spells a variable of the same name and a branch of the same
  wording; they are that suite's own, read nothing of this file, and stay as section 3 says.
  by value: `tools/check-spec-tokens.test.sh` again, in the same arm and nowhere else: the
  membership test that exempts a leg by its script name, the stale-exemption clause that reds a
  member naming no leg, and the count of printed exemptions that the third parity assertion adds
  to the graded count. No other file reads the list, its members or the arm's printed lines.
- **S4** — Three assertions are added beside the parity arm: the suite's own bound and word list
  equal the module's, the set derived from rows the suite stages, and the shorter and longer
  spellings of a staged leg. Observed by AC2, AC4 and AC6.
- **S5** — The `bar` entry of the module docstring and the comment above `BAR` say what S1 makes
  true. NOT OBSERVED: prose, which no criterion grades.
- **S6** — The tracked tree gains no `[bar]` hit from S1. Observed by AC5.

## 3. Non-goals (OUT)

- Any edit to the pattern `BAR`. It stays the textual half, and its `check_policy.py --fixture`
  alternative stays as written.
- A deny of a direct-check form at or under the bound. The three playbook `fixture` legs sit at
  the bound and stay the direct check a criterion may name.
- Any edit to `tools/unattended/gate-guard.js` or its suite. That reader is TOOL-aClearedLedger-3's,
  and this unit builds on nothing it builds. Both specs state one rule, and section 4 names where.
- Moving a self-test entrypoint to a `selftest.py` file, the cure ask TOOL-aDeferredBar-12 names.
- The `test_recall_floor.py` exemption, which ask TOOL-aDeferredBar-11 owns.
- Any edit to `tools/gate-legs.json`. No ceiling moves and no argv moves.
- Any edit to `memory/TEMPLATE-SPEC.md`. Its bar paragraph names `a --selftest flag or a fixture`
  as the direct check and says nothing of the bound. It is a kit document with rendered copies, so
  a correction is a unit of its own.
- A new entry in `PARITY_EXEMPT`, or a waiver row, to make the arm pass.
- Any kit version, which the lander's `mint` moves.

## 4. Design

### Evidence

Read at `8db6f4be`. The reproduction is the brief's `a18.out`, taken on a frozen clone of that sha.

| Line the arm printed | Cause, verified |
|---|---|
| `routed_commits.py --selftest`, ceiling 660 s (PINNED, 2026-11-13), above the bound and not declared | `cf2c673f3` raised the ceiling past the bound of 300 s (PINNED, 2026-11-13), and `tools/check-spec-tokens.py#BAR` reads no ceiling |
| `core.py fixture`, `instruction_units.py fixture`, `instructions_edit.py fixture` | `399788aca` and `4b487529a` added the legs at ceiling 300; the arm's exemption tests the one word `--selftest` |
| `graded 57 + exempt 16 != the manifest's 74` (PINNED, 2026-11-13) | the arm's undeclared-flag branch appends to `bad` and counts the leg in neither total |

The third line is the first line's leg, uncounted. It is an arm defect, and S3 deletes the branch.

### Which side is wrong

The reader, for a flag-form leg above the bound. `routed-commits selftest` read 330 s alone <!-- PINNED 2026-11-13 -->
(PINNED, 2026-11-13, at `2ba17e9d6`, in `tools/run-gates/ceiling-evidence.txt`), so it is a suite by
cost, and a spec may name it as an acceptance observation today. The reader cannot see a ceiling,
which is also why three more flag-form suites sit in `PARITY_EXEMPT` by name.

The arm, for the three `fixture` legs. They sit at the bound, like the twelve `--selftest` legs the
arm already exempts, and a fixture is a direct check the spec format names. The arm's rule names
one spelling of a class that has three.

This is the rule TOOL-aClearedLedger-3 states for the hook: one bound, three direct-check words,
and a leg in such a form above the bound denied by reading the manifest. The two constants carry
the same names and values in both readers.

### S1 and S2 — the manifest read

```python
DIRECT_CHECK_BOUND = 300
DIRECT_CHECK_WORDS = ("--selftest", "--fixture", "fixture")

def derive_flag_suites(rows, bound=DIRECT_CHECK_BOUND):
    """The manifest's suites in a direct-check form, as `(name, ceiling, words)` in manifest order:
    each `chunk = selftests` row whose `ceiling` is a number above `bound` and whose `words` hold a
    member of DIRECT_CHECK_WORDS after the first. `words` is the argv from its first word carrying
    a slash on, with a leading `{prefix}/` taken off that word."""

def check_bar(tok, flag_suites=()):
    """The reason `tok` is a bar or suite invocation, or None: BAR_WHY when `BAR` matches it, and
    BAR_WHY with a clause naming the leg and its ceiling when a simple command of it spells a
    member of `flag_suites`."""
```

A simple command is a stretch of the token between `&&`, `;`, `|` and `(`, split on whitespace,
with each redirection word dropped: a word matching `^(?:\d*|&)(?:>>?|<{1,3})`, and the word after
it when the target is not glued. A simple command spells a leg when all three hold.

1. One of its words, with `\` folded to `/` and lower-cased, equals the leg's first word
   lower-cased, or ends with `/` followed by it. The candidate is that word and every word after.
2. The candidate has no more words than the leg, and each later word equals the leg's word at
   that place.
3. The candidate reaches the leg's first direct-check word.

Rules 2 and 3 make a shorter spelling a hit and a longer or different one a miss, so a case named
after `--fixture` stays the direct check. `main` already parses the manifest into `rows` for the
leg join. It derives the set once there and passes it to the three sites that call `BAR.search`
today: the leg line, the acceptance bullets and the `--list` near-miss rows.

A fixture manifest carries no `ceiling`, so every fixture run of the suite derives an empty set and
no existing arm changes verdict.

### S3 and S4 — the arm

| A leg | The arm |
|---|---|
| its script is `test_recall_floor.py` | exempt, printed |
| its argv carries a direct-check word and its ceiling is at or under the bound | exempt, printed with its ceiling |
| every other leg | graded: `check_bar` over the argv, with the set derived from the same manifest |

Graded plus exempt then equals the leg count by construction. The stale-exemption clause stays.

The suite keeps its own `DIRECT_CHECK_BOUND` and its own word list, and one new assertion compares
both to the module's, so the arm and the reader share no state. For a flag-form leg above the bound
the grade is a derivation from the manifest the arm also reads, so on the real manifest it cannot
fail. The two other new assertions stage their own rows instead:

| Staged | Expected |
|---|---|
| six rows: `--selftest` at ceiling 300, at 301, at 301 in another chunk, with no ceiling; `fixture --strict x` at 301; a bare script at 301 | `derive_flag_suites` returns the 301 `--selftest` row and the `fixture` row, in that order |
| the staged `fixture` leg, spelled to `fixture`, then with a case word, then as the script alone | `check_bar` gives a reason, then None, then None |

`FLOOR_ASSERTIONS` rises by the three, 245 to 248, with a comment line in the file's own form. The
suite executed 250 assertions at `8db6f4be` (PINNED, 2026-11-13).

### The probes

Probe P1, the arm's rule over the real manifest, run from the repository root:

```python
import importlib.util, json
spec = importlib.util.spec_from_file_location("cst", "tools/check-spec-tokens.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
rows = json.load(open("tools/gate-legs.json", encoding="utf-8"))
flags = m.derive_flag_suites(rows)
legs = [r for r in rows if r.get("chunk") == "selftests"]
named = [r for r in legs if any(a.endswith("/test_recall_floor.py") for a in r["argv"])]
direct = [r for r in legs if r not in named and set(r["argv"]) & {"--selftest", "--fixture", "fixture"}
          and r.get("ceiling", 0) <= 300]
graded = [r for r in legs if r not in named and r not in direct]
bad = [" ".join(r["argv"]) for r in graded if not m.check_bar(" ".join(r["argv"]), flags)]
print("flag suites", ", ".join(sorted(name for name, _ceiling, _words in flags)))
print("legs", len(legs), "graded", len(graded), "direct", len(direct), "named", len(named), "unmatched", len(bad))
```

Probe P2, the discrimination, with `m` and `flags` bound as in P1:

```python
for tok, want in (("python3 tools/memory-tree/routed_commits.py --selftest", True),
                  ("python3 tools/memory-tree/routed_commits.py --selftest > x.log 2>&1", True),
                  ("python3 tools/memory-tree/routed_commits.py --selftest | tail -1", True),
                  ("python3 tools/memory-tree/routed_commits.py --selftest --quiet", False),
                  ("python3 tools/memory-tree/gotchas.py --selftest", False),
                  ("python tools/playbook/core.py fixture", False),
                  ("python tools/policy/check_policy.py --fixture one-case", False),
                  ("grep -c selftest tools/memory-tree/routed_commits.py", False)):
    print(bool(m.check_bar(tok, flags)) == want, tok)
print(m.check_bar("python3 tools/memory-tree/routed_commits.py --selftest") is None)
staged = m.derive_flag_suites([
    {"name": "at", "chunk": "selftests", "ceiling": 300, "argv": ["python", "t/at.py", "--selftest"]},
    {"name": "over", "chunk": "selftests", "ceiling": 301, "argv": ["python", "t/over.py", "--selftest"]},
    {"name": "plant", "chunk": "selftests", "ceiling": 301,
     "argv": ["python", "{prefix}/t/plant.py", "fixture", "--strict", "x"]},
    {"name": "other", "chunk": "e2e", "ceiling": 301, "argv": ["python", "t/other.py", "--selftest"]},
    {"name": "bare", "chunk": "selftests", "argv": ["python", "t/bare.py", "--selftest"]},
    {"name": "plain", "chunk": "selftests", "ceiling": 301, "argv": ["python", "t/plain.py"]}])
print([name for name, _ceiling, _words in staged] == ["over", "plant"])
print([bool(m.check_bar(t, staged)) for t in ("python t/plant.py fixture", "python t/plant.py fixture one",
                                             "python t/plant.py")] == [True, False, False])
```

### The rule over the real tree

A prototype of the two functions, written to the rule above and kept outside the repository, was
run over the tree on 2026-11-13, at `8db6f4be` with this build's specs beside it.

- P1 printed the two lines AC1 states, and P2 printed `True` eleven times.
- No token on a leg line or in an acceptance bullet of any live spec gained a hit.
- Outside that graded population, one of aMendedLedger's specs and the design section of
  TOOL-aClearedLedger-3's spec spell such a leg. The join lists those under `--list` and grades
  neither.

### What it does not check

- A flag-form suite in a repository whose manifest carries no `ceiling`. The set is empty there.
- A direct-check leg at or under the bound that is slow in fact. The ceiling is a declaration.
- A leg spelled by its bare file name, with no directory. Rule 1 wants the leg's first word whole.
- A leg run through `python -m`, or behind a variable.
- The hook. A role agent's command is refused by other rows, which this unit does not read.

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`

### Alternatives rejected

- **Declaring `routed_commits.py` in `PARITY_EXEMPT`.** It is the arm's own interim remedy, and the
  brief refuses it: no exemption is added to make the arm pass. It also leaves the 330 s suite <!-- PINNED 2026-11-13 -->
  (PINNED, 2026-11-13) free to stand as an acceptance observation.
- **Moving the entrypoint to a `selftest.py` file.** It cures both readers, and it is ask
  TOOL-aDeferredBar-12's unit: a new kit file, a manifest argv, a guard and the pass-leg list.
- **Naming the four scripts in the pattern.** A list typed beside the manifest goes stale at the
  next ceiling raise, which is how this arm went red.
- **A bare `fixture` alternative in `BAR`.** It would deny the three playbook legs by their word.
  The arm's rule is the ceiling and never the word, twelve `--selftest` legs at the same ceiling
  are admitted by it, and the hook's spec admits these three. Two readers of one bound, each with
  its own answer for one leg, is the defect this build exists to stop re-attributing.
- **Reading the bound and the word list from the module in the suite.** The arm would then share
  state with the reader it grades.

## 5. Acceptance criteria

A role agent's hook refuses a manifest leg's argv and a suite, so AC5 and AC6 are the main loop's.
The others are probes a builder runs with `python -c` or from a scratch file.

- **AC1** — When probe P1 of section 4 runs over `tools/check-spec-tokens.py` and
  `tools/gate-legs.json`, its first line reads
  `flag suites build-index selftest, corpus-ids selftest, measure-legs selftest, policy fixtures, routed-commits selftest`
  and its second reads `legs 74 graded 58 direct 15 named 1 unmatched 0`.
  Red when: a flag-form leg above the bound is not derived, or `check_bar` misses one, which
  prints an `unmatched` figure above 0. At `8db6f4be` the probe raises `AttributeError`.
  figure: both lines are PINNED, 2026-11-13, from the manifest at `8db6f4be`; a later ceiling or
  leg moves them, and `unmatched 0` still decides.
- **AC2** — When probe P2 of section 4 runs against `tools/check-spec-tokens.py`, each of its
  eleven lines opens `True`.
  Red when: a redirected or piped spelling is missed, a longer spelling or a case-scoped one is a
  hit, a form at or under the bound is a hit, a read of the file by `grep` is a hit, `check_bar`
  with no set denies a flag, a row at the bound is derived, or the script alone is a hit.
- **AC3** — When `grep -cE '^(DIRECT_CHECK_BOUND = 300|DIRECT_CHECK_WORDS = |def derive_flag_suites\(|def check_bar\()' tools/check-spec-tokens.py`
  runs it prints 4, and `grep -c 'BAR\.search(' tools/check-spec-tokens.py` prints 1.
  Red when: a call site of the join still asks the pattern alone, which prints 2 or more. At
  `8db6f4be` the two commands print 0 and 3.
- **AC4** — When `grep -E '^(PARITY_EXEMPT|DIRECT_CHECK_BOUND|FLOOR_ASSERTIONS)=' tools/check-spec-tokens.test.sh`
  runs, it prints `PARITY_EXEMPT="test_recall_floor.py"`, `DIRECT_CHECK_BOUND=300` and
  `FLOOR_ASSERTIONS=248`, and `grep -c 'is not declared exempt' tools/check-spec-tokens.test.sh`
  prints 0.
  Red when: a named flag-form exemption survives, the floor did not follow S4's three assertions,
  or the uncounted branch is still there. At `8db6f4be` the second command prints 1.
- **AC5** — When the main loop runs the leg `spec tokens (a spec's own names resolve)` by its own
  argv over the tree, the output holds no row carrying `[bar]`.
  Red when: a live spec dated at or after `SPEC_DIRECT_CUTOFF` spells a flag-form suite above the
  bound in an acceptance bullet or on its leg line.
  permission: the main loop's; the command is a leg's own.
- **AC6** — When the main loop runs the suite the `New arm:` lines of section 6 name, on a frozen
  clone, the output holds no line carrying `arm FAIL  parity`, holds the three lines opening
  `arm ok    parity:`, and ends `PASS (` with a total of 248 or more.
  Red when: a `selftests` leg is neither matched nor printed as exempt, or an assertion of S4 is
  absent and the total falls under the floor.
  permission: the main loop's; a role agent's hook refuses a suite.
  figure: 248 is DERIVED, the floor `FLOOR_ASSERTIONS` after S4.

## 6. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test`

The first is the leg whose reader this unit changes, and the second runs the suite it edits. The
main loop runs both at the close, with the plain bar after the last unit. Each arm below is
observed RED and then GREEN there.

New arm: `tools/check-spec-tokens.test.sh` · covers AC2 · `derive_flag_suites` edited to admit a row at the bound, so the staged 300 row is returned · `FLOOR_ASSERTIONS` 245 to 248
New arm: `tools/check-spec-tokens.test.sh` · covers AC2 · rule 2 dropped from `check_bar`, so the staged leg with a case word is a hit · the same floor move
New arm: `tools/check-spec-tokens.test.sh` · covers AC3 AC4 · `DIRECT_CHECK_WORDS` in the module losing `fixture`, so the suite's own list differs · the same floor move

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-13 · initial draft.
- rev-2 · 2026-11-13 · S3 gains its `**Readers:**` clause, which hygiene check 25 asked of an item
  that retires three members of `PARITY_EXEMPT` and one branch. No other text moved.

## 9. Reuse audit

The seam is the bar join of `tools/check-spec-tokens.py` and the manifest rows `main` already
parses for the leg join; S1 reads two more fields of rows that are in hand. `python
tools/codebase-map/reuse_lookup.py "decide whether a command token is a self-test suite invocation
by reading the gate manifest ceiling"` ranked name-stem neighbours only, `resolve_prefix_token`
among them, and named no helper that reads a ceiling, so for the flag-suite set no existing seam
fits and it is derived in the one file that uses it. `tools/hooks/scratch-guard.js#checkGateSuite`
denies every `--selftest` to a role agent and reads no ceiling, so it is no source for the rule,
and it is JavaScript. The match rule is the one TOOL-aClearedLedger-3 writes for the hook, stated
here in full so neither spec reads the other. `gotchas.py --for-paths` over the estimate selected
`fixture-passes-by-finding-nothing`, which is why S4 stages its own rows. The recall probe returned
asks TOOL-aDeferredBar-11 and TOOL-aDeferredBar-12, the two exemptions' owners; section 3 cites
both.

Recall terms used: `parity arm BAR selftests chunk direct-check bound ceiling flag-form suite
exemption manifest gate-guard`
