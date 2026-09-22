---
name: suite-invalidated-by-a-commit-under-it
description: a suite that pins gov's revision at import and stamps fixtures from live HEAD is silently invalidated by any commit made while it runs, and the failures name the product
kind: class
---

# A long suite invalidated by an ordinary commit made while it ran

## Symptom

A held self-test takes twenty minutes. You start it, carry on working, commit a few times, and it
comes back with dozens of failures naming the product — receipts, vintages, downgrades, tallies.
None of them names the thing you actually changed. Re-running it on a frozen copy of the same tree
returns clean.

The failures are real assertions failing for a real reason. The reason is that the repository moved.

## Where it bit

`tools/govkit/selftest.py`, node `a`, 2026-09-06. Run against the live worktree while the session
committed four times, it reported **28 failures**. The same tree, cloned and frozen, reported **2** —
the same 2 the pre-session baseline reported. All 26 extra failures were the commits.

The mechanism is two facts that only interact while HEAD moves:

- `GOV_PIN = resolve_gov_pin(...)` is evaluated **once at module import**, and returns a ref-reachable
  commit carrying the working tree.
- `_cmd_apply` stamps a fixture's receipt with `git rev-parse HEAD` **at apply time**, and
  `write_receipt_pin` only corrects it `if GOV_PIN != GOV_HEAD` — false on a branch, so on a branch
  it corrects nothing.

So every fixture applied after a commit carries a receipt NEWER than the pin the suite will later
hand `update --to`, and `demand_forward_vintage` refuses it:

```
--to resolves to <import-time pin> and this target's receipt records <later commit>,
which is not an ancestor of it. A DOWNGRADE IS NOT AN UPDATE
```

The refusal is correct. The suite is measuring a repository that changed underneath it.

**It cost two wrong attributions before anyone looked at the message.** The first read was "these are
pre-existing drift in a held leg" — refuted by a baseline run. The second was "my kit changes broke
them" — refuted by a frozen clone. Neither was true, and both were reported before the measurement
that could distinguish them had been taken.

## The fix

**Run a long suite against a FROZEN tree, and hold commits while it runs.**

```bash
B=$TMP/gk; rm -rf "$B"
git clone -q --local --no-hardlinks <repo> "$B"
( cd "$B" && python tools/<kit>/selftest.py ) > "$B.out" 2>&1
```

A `--local` clone is cheap, the suite runs against a HEAD nothing can move, and the working tree stays
free for other work. It is also the only form in which two runs are comparable, which is what makes
a baseline possible at all.

The suite could defend itself, and does not: it prints its vintage pin on the first line, and nothing
re-checks that pin against HEAD at the end. **One assertion — HEAD is the same at exit as at import,
else the run is UNSOUND rather than failed** — turns twenty silent minutes into a named refusal in
the first second after the drift.

## What it is not

Not `fixture-inherits-ambient-machine-state`, which is about machine-global config a fixture reads
without declaring. Here the fixture declares its input correctly; what moves is the repository the
suite is a test OF.

Not flakiness. It is perfectly deterministic given the commit timing, which is what makes it so
convincing: the failures are stable across the run and they cluster in one subsystem, so they read
like a real regression in that subsystem.

## The gate

There is **no machine gate** for this class, because the defect is a race between a suite and the
session running it, and no state in the tree records that the two overlapped. What replaces it is a
documented check with a cheap mechanical form: **run a long suite on a FROZEN CLONE, never on the
tree you are editing** — `git clone --local --no-hardlinks <tree> <short-temp-path>` and run there.
The clone pins the commit the suite grades, so a commit landing mid-run cannot reach it. See
[[run-long-suites-on-a-frozen-clone]] for the invocation and the MAX_PATH trap that goes with it.
