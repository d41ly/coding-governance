# The leg's git arity, measured through a shim that follows children

**Serves:** journal TOOL-aQuenchedHarness-10

Node `a`, 2026-09-07. Evidence for `TOOL-aQuenchedHarness-10` §6 at rev-1.

## How this was measured, and why the earlier attempt could not be

`bash -x` does not follow child processes. The first pass at this leg counted 2349 traced commands
and concluded the driver launches were the cost — but the 102 `bash unattended.sh --plan` children
were invisible to it, and so was every git process inside them. Every conclusion drawn from that
trace was drawn from the wrong half of the run.

The method that works is a shim: a shell function named `git` in `lib-unattended.sh` that appends
its argv and its two innermost call frames to a file and then calls `command git`. Because the leg
and the driver both source that library, the log follows children for free. It is instrumentation
and is not landed.

Two things it caught immediately, neither of which a reading of the code had suggested:

- **`set -u` matters in a shim.** The first version read `${BASH_SOURCE[2]##*/}` unguarded. At the
  leg's very first git call the stack is one frame deep, so the expansion was unbound, the function
  failed, and the leg exited with `not a git repo` in 146 ms. A measurement harness that dies at the
  first call looks exactly like a fast run.
- **A fixture that detaches the remote disables the code under test.** The A/B clone had its origin
  detached so nothing this session pushed could move what the leg observed. That also left
  `$ADV_HEAD` and `$ADV_TIPS` empty, so the entire published-anchor path — the path being optimised
  — never executed in either arm. The fix was a bare frozen origin advertising all 28 heads, which
  is stable AND representative. Recorded as its own class: `memory/gotchas/fixture-removes-the-path-under-test.md`.

## What the log said

1114 git processes: 777 the leg's own, 337 the driver's inside check 30. Ranked by exact argv, the
top three were one question about one commit:

| count | argv |
|---|---|
| 52 | `rev-parse --verify --quiet <HEAD>^{commit}` |
| 39 | `rev-parse HEAD` |
| 36 | `cat-file -e <HEAD>^{commit}` |

127 processes for two facts that cannot change while the leg runs. Timed directly on this tree, a
`cat-file -e` costs 389 ms and a `git log --follow` over one path 123 ms — the cost is process
creation, not the question, so the leg's wall clock is its process count.

Check 30 was measured separately, because it is the driver's cost rather than the leg's: one
`--plan` costs 3786 ms and spawns 29 external processes — 13 awk, 9 grep, 3 sort, 2 git — and it ran
102 times.

## Evidences

**Evidences:** TOOL-aQuenchedHarness-10

- AC1 — `GIT_ARGV_LOG` — the leg's own git spawns fell from 777 to 223 and the whole run's from
  1114 to 369; the most repeated single argv went from 52 to 5. Counted from the log at
  observation time, not asserted.
- AC2 — `check-unattended.sh` — check 30 asked the driver about the five builds its scan selected.
  The canary limb is unexercised on THIS corpus, because the selection is never empty here - but
  the kit's own `cross-component.test.sh` exercises it hard, and it is what found the unit's
  worst defect. Those fixtures hold ONE build, so the ask was one slug, so `--plan` took its
  unframed path and the frame-reading loop counted zero verdicts on a healthy tree. Every
  fixture built inside this unit had many builds and could not produce the shape.
  The canary is also a SAMPLE of three now rather than one build: liveness must not be hostage
  to whether the build that happens to sort first is in a state that grades.
- AC3 — `2026-09-07-spec-TOOL-aQuenchedHarness-9.md` — removing that spec's `**Status:**` header took
  the scan's selection from five builds to six, adding `aQuenchedHarness`, which the scan had not
  selected before. The file was restored and `git diff` over it is empty.
- AC4 — `diff` — stdout byte-identical to the pre-change leg over the frozen fixture: 37 lines,
  rc=0, both runs. This is the criterion that caught the `cat-file --batch-check` field offset: the
  reply is `<oid> <type> <size>` and the parser read the type one field late, so every advertised tip
  looked unreadable and every `is_published` answer became CANNOT TELL, redding check 9 on every
  record in the tree.
- AC5 — `grep -qF` — against a driver copy with `Status:` rewritten, the parity assertion fails and
  check 30 refuses. Observed on a doctored copy, not on the tracked driver.
- AC6 — `date +%s%3N` — 618 s to 316 s on the fixture, against a target of 334 s. Timed at
  observation, on the same clone, same remote, back to back. The recorded figure for this leg
  on the real bar was 541 s where this fixture measured 618 s, so the fixture runs about 14%
  slow and the real figure should land below this one rather than above it - but that is an
  inference and the bar has not been re-timed.

## What was left, and why it is not an oversight

Three sites keep one git process per record, and each is named in §3 with its reason:

- `GIT show <rev>:<path>`, 84 spawns. Batching needs a byte-counted `cat-file --batch` reader, and
  bash's `read -N` counts CHARACTERS — under a UTF-8 locale a single em dash desynchronises the
  stream and blobs are silently attributed to the wrong record. That is a mechanism of its own.
- `git log --follow`, 27 spawns. One walk would have to reconstruct rename chains, and the site's own
  header explains that the rotation of a run-state file is precisely the rename `--follow` exists to
  see through.
- `log -1 --format=%s` and `diff-tree` over the same commit set, 58 spawns.

Together they are roughly 22 s. They are distinct questions about distinct objects rather than the
same command repeated, which is the difference between arity and repetition.
