# TOOL-aQueuedIndex-3 — the queued-writers plant pins the busy timeout

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-1 · base 8c8e4412a · streams tooling · order 3

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-build-TOOL-aQueuedIndex-3-ledger.md](../build/2026-11-12-build-TOOL-aQueuedIndex-3-ledger.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-3-1-spec-writer.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-3-1-spec-writer.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-3-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-3-build-brief.md) | journal | — |
| [2026-11-12-prompt-TOOL-aQueuedIndex-3-spec-brief.md](../prompts/2026-11-12-prompt-TOOL-aQueuedIndex-3-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The busy timeout that TOOL-aQueuedIndex-1 raised to 600 s has no check that fails if it shrinks.
After this unit the `queued-writers` plant prints the timeout and goes red when it is below 600, so
the selftest leg that runs the plant catches a shrink. This folds item LOW-1 of the closing review
`2026-11-12-review-TOOL-aQueuedIndex-2-diff-review-round2`.

## 2. Scope (IN)

- **S1** — The plant prints `busy timeout <ti.BUSY_TIMEOUT> s` after its writer-one line, and its
  green verdict also requires the timeout to be 600 or more. With the timeout at 600 it still
  prints `both writers green` as its last line. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- No change to `tools/playbook/tag_index.py`. The timeout's value and the locking stay as they are.
- No change to the plant's row in `tools/playbook/adopt-playbook.sh`. That row already requires
  exit 0 and `both writers green`, so it reds when the verdict does.
- No plant that holds the write lock for longer than a short timeout. That stages a behaviour, and
  it costs a hold of minutes per run. This unit pins a constant.
- No join between the plant's floor and the `600 seconds` that `help/tags.md` states. The help page
  is unchanged and stays true.
- No permanent staged-break case in a selftest leg, as TOOL-aQueuedIndex-2's F1 resolved for its own
  breaks.

## 4. Design

### What is unpinned today

`BUSY_TIMEOUT = 600` sits at `tools/playbook/tag_index.py@46bfe37d:117`. `load_index` passes it as
the connection's timeout (`tools/playbook/tag_index.py@46bfe37d:519`). The `queued-writers` plant's
waiter queues only behind a 3 s staged parse (`tools/playbook/gov_tag.py@1dcf72fa:602-604`), so any
timeout of a few seconds or more leaves the plant green. TOOL-aQueuedIndex-1 records that blind
spot (`memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@94e7a730:207-210`).
Its pin, AC4, is a grep observed once and run by no leg
(`memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@94e7a730:310-311`). A
full tree build was measured at 95 s there
(`memory/builds/aQueuedIndex/spec/2026-11-12-spec-TOOL-aQueuedIndex-1.md@94e7a730:145`), PINNED
2026-11-12, which is why the value is 600 and why a shrink would bring the flake back.

### S1: print the timeout and grade it

After the plant's writer-one line (`tools/playbook/gov_tag.py@1dcf72fa:835`), it prints one line
through its `say`:

```
busy timeout <ti.BUSY_TIMEOUT> s
```

The verdict at `tools/playbook/gov_tag.py@1dcf72fa:837-838` gains one conjunct,
`ti.BUSY_TIMEOUT >= 600`, with a comment naming TOOL-aQueuedIndex-3 S1 and the 95 s build. The
green line at `tools/playbook/gov_tag.py@1dcf72fa:839-840` stays the last thing the plant prints,
and it prints only when the verdict holds. At a timeout of 60 the race itself still passes, because
the waiter queues for about 2.5 s. So the new conjunct is the only check that moves, and the plant
exits 1 with no green line.

The floor is the literal 600 in the plant. That is a second spelling of the value, held as a check
on the first. `tools/playbook/tag_index.py` stays the value's owner.

### What this check does not see

- A timeout above 600 passes. The floor guards against a shrink, which is the review's harm.
- A connection opened with its own timeout rather than `BUSY_TIMEOUT` is not read.
- The plant reads the constant; it does not stage a writer that holds the lock past the timeout.
- The help page's `600 seconds` is not compared with the constant.

### Inventory

This unit mints no function, constant, type or file. The floor is an inline literal, and the
printed line adds no local. The lexicon grades only the surfaces `function`, `type`, `file` and
`constant` (`tools/lexicon/lexicon_conf.py@1754d838:41`), so no new name has a cell for
`--suggest` to grade.

### Files touched (estimate)

`tools/playbook/gov_tag.py`

## 5. Acceptance criteria

- **AC1** — When `python tools/playbook/gov_tag.py --fixture --plant queued-writers` runs, it
  exits 0, prints `busy timeout 600 s`, and its last line ends `both writers green`.
  Red when: the plant prints no timeout line, or prints it after the green line.
  cost: about 10 s a run, as TOOL-aQueuedIndex-2's AC1 measured, PINNED 2026-11-12.
- **AC2** — When the same plant command runs over a scratch copy of the tree whose
  `tools/playbook/tag_index.py` reads `BUSY_TIMEOUT = 60`, it prints `busy timeout 60 s`, exits 1,
  and prints no `both writers green`. With that copy's line set back to `BUSY_TIMEOUT = 600`, the
  same command exits 0 and prints `both writers green` again.
  Red when: the verdict lacks the timeout conjunct, as at base, and the plant exits 0 at 60.
  fixture: a scratch copy of the tree made by the observer outside the repository. The tree holds
  none today.
  figure: the 60 is the pre-raise value at base `97e0841d`, PINNED by the review.

## 6. Gates

`playbook render selftest` · `govkit acceptance matrix` · `tags (the resolver's checks)` · `spec tokens (a spec's own names resolve)`

New arm: tools/playbook/adopt-playbook.sh · covers AC2 · the `queued-writers` row run over a scratch copy whose index module reads `BUSY_TIMEOUT = 60` · none

The arm runs in the `playbook render selftest` leg, inside its 300 s ceiling. The new conjunct and
line add microseconds to the plant's 10 s. What the arm does not check is listed in §4.

## 7. Open questions

- **F1** — Which of the review's two fixes pins the timeout?
  - (a) The plant prints `busy timeout <ti.BUSY_TIMEOUT> s`, and a row in
    `tools/playbook/adopt-playbook.sh` requires `busy timeout 600 s`. A row carries one must-print
    field (`tools/playbook/adopt-playbook.sh@b8d6bd17:273`) and each row runs the plant once
    (`tools/playbook/adopt-playbook.sh@b8d6bd17:276`). So keeping `both writers green` required
    costs a second row and a second 10 s run. A scratch copy at 60 leaves the plant itself exiting
    0, and only the row reds.
  - (b) The plant prints the same line, and its green verdict requires `ti.BUSY_TIMEOUT >= 600`.
    The plant itself reds at 60, the existing row reds with it, and no row or run is added. It pins
    a floor and not the exact value.
  - Recommendation: (b). It is the smaller diff, it reds on the plant run that AC2 observes, and it
    keeps the plant's last line `both writers green`.
  - RESOLVED (agent, 2026-11-12, delegated): (b) — the verdict conjunct and the printed line. The
    brief delegates the pick to the fix that reds on a scratch copy at 60, and asks for no open
    fork.

## 8. Revision log

- rev-1 · 2026-11-12 · initial draft.
