# TOOL-cBriefedPilot-23 — the arms meta-gate grades EXECUTION, not text

**Status:** CLOSED · rev-2 · 2026-08-16 · node c · Tier-2 · base 709d260d · streams tooling · ratified 2026-08-16

## 1. Goal

`check-arms.py` certified nine branches as armed while the arms sat past an unconditional `exit`, and
three of those nine could not have produced the state they asserted even if reached. Every other gate
in the suite held. The M8 review named this the one recommendation above all sixteen individual
fixes, and the owner added this unit for it.

Two mechanisms, both cheap: a per-file floor on the number of assertions a suite actually EXECUTES,
and a helper that refuses a fixture mutation which mutated nothing.

## 2. Scope (IN)

- **S1** — each self-test suite that COUNTS declares `FLOOR_ASSERTIONS=<n>` near its top and its summary refuses
  when the executed count is below it. The count is RUNTIME, not a static grep: an arm past an `exit`
  is still present in the file, so only an executed count can see it go dark.
- **S2** — the refusal names both numbers and says the arms are unreachable rather than absent, since
  that is the failure this exists for.
- **S3** — a `mutate` helper: `mutate <file> <sed-script>` snapshots the file, applies the edit, and
  fails the suite when the bytes did not change.
- **S4** — the helper is ADOPTED by the arms whose fixtures this build caught doing nothing: the
  column-anchored grep, the raw-newline `s///`, and the fetch-by-path anchor advance.
- **S5** — `tools/memory-tree/check-arms.py --report` already prints branch and armed counts; nothing
  in it changes. This unit adds no Python.

## 3. Non-goals (OUT)

- **A new gate leg.** Both mechanisms live INSIDE suites that are already legs. A separate leg would
  have to re-run every suite to read its count, doubling the bar's cost to learn what the suites
  already know as they finish.
- **Making the floor machine-derived.** A floor a script recomputes is not a ratchet. It is a
  constant someone must lower in a reviewed diff, exactly like `ARMS_FLOORS` and every other
  shrink-only pin here.
- **Retrofitting `mutate` across every arm.** S4 takes the three shapes this build measured failing.
  A sweep would be a large diff with no evidence behind most of it.
- **Counting assertions per BRANCH.** `check-arms.py` owns the branch-to-arm join. This unit answers
  a different question: did the arms run at all.

## 4. Design

### Why the count must be runtime

The dead block was nine syntactically perfect arms after `exit "$st"`. A static count of `hit(`
occurrences sees all nine and reports no change; `check-arms.py` text-matches the assertion strings
and sees all nine; the suite's own summary printed `PASS (86 assertions)` and 86 was simply never
compared to anything. The only signal that moved was the executed total, and nothing read it.

### Why it lives in the suite and not in a gate

Each suite ends by printing its count. Adding `[ "$n" -ge "$FLOOR_ASSERTIONS" ]` beside that print
costs one comparison and catches the regression at the moment it happens, in the leg that already
runs. Any external checker would have to execute the suite to obtain the number.

### The mutate helper

```sh
mutate() { # file · sed-script — a fixture edit that changes nothing is a fixture that tests nothing
  local f="$1" before; before=$(git hash-object "$f")
  sed -i "$2" "$f"
  n=$((n+1))
  [ "$(git hash-object "$f")" != "$before" ] || { echo "FAIL fixture no-op on $f: $2"; st=1; }
}
```

It is an assertion, so it increments `n` and participates in the floor. Three failure shapes this
build paid for would each have been caught by it: a grep anchored at column 0 against indented rows,
an `s///` whose replacement carried a raw newline (a sed syntax error that edits nothing), and a
`git fetch` by path that moved no remote-tracking ref.

### Files touched

`tools/unattended/check-unattended.test.sh` · `tools/unattended/unattended.test.sh` ·
`skills/session-kickoff/manifest-check.test.sh` · `tools/memory-tree/check-memory-hygiene.test.sh`.

## 5. Production-readiness checklist

Runs inside existing legs; no new process, no new dependency, no new configuration file. The floors
are constants in the files they govern, so a copy-installed kit carries its own.

## 6. Acceptance criteria

- **AC1** — lowering a suite's executed count below its `FLOOR_ASSERTIONS` makes that suite exit 1:
  move an arm below the summary in `tools/unattended/check-unattended.test.sh` and observe the refusal.
- **AC2** — the refusal names the observed count, the floor, and says `arms are UNREACHABLE rather than absent`, so the reader is pointed at a stranded block rather than a deleted one.
- **AC3** — `mutate` with a sed script that matches nothing fails the suite naming the file.
- **AC4** — `mutate` with a sed script that matches leaves the suite green.
- **AC5** — every suite touched still prints `PASS (` with a count at or above its own `FLOOR_ASSERTIONS`.

## 7. Gates

`bash tools/unattended/check-unattended.test.sh` · `bash tools/unattended/unattended.test.sh` ·
`python tools/memory-tree/check-arms.py` · `bash tools/run-gates.sh`.

## 8. Open questions

none — the design pass took both decisions it had, and §4 records the reasoning for each: the count
is runtime because a static one cannot see an unreachable arm, and it lives in the suite because any
external reader would have to run the suite to get it.

## 9. Revision log

- rev-1 · 2026-08-16 · authored from the M8 review's single headline recommendation, after the owner
  added the unit.
- rev-2 · 2026-08-16 · S1 narrowed to the suites that count. Three shipped floors; the hygiene suite
  needed a counter first and its ~50 inline sites stay uncounted (TOOL-cBriefedPilot-34), and
  `manifest-check.test.sh` has no summary at all to floor (TOOL-cBriefedPilot-35). Both filed rather
  than swept in, because a floor over a count nobody maintains is the defect this unit exists for.

## 10. Reuse audit

`git hash-object` is already this repo's byte-comparison idiom — `unattended.test.sh` uses it for
`sum()` and the roster arm uses it for a region hash — so `mutate` reuses it rather than adding a
checksum. The floor mechanism reuses the shrink-only-constant pattern of `ARMS_FLOORS`,
`CORE_FLOOR`, `DIRECTIVES_FLOOR` and the drift pins rather than inventing a registry. `check-arms.py`
already owns the branch-to-arm join and is not touched.
