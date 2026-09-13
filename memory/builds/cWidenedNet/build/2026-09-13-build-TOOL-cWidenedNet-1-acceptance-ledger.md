**Serves:** journal TOOL-cWidenedNet-1

# cWidenedNet — acceptance ledger

Every line below was observed on node `c` on 2026-09-13, on the tree this build produced. Figures
are derived by the run named in each line, never copied from the spec.

**Evidences:** TOOL-cWidenedNet-1

- AC1 — `bash tools/check-install-prefix.sh` — arm 1 clean over 257 shipped files, 11 declared
  waivers and 23 marked fixture lines. The population was 207 before this unit, so the growth the
  criterion asks for is 50 received tests, selftests and example confs. The marked count is non-zero,
  which is the half that proves the growth reached fixtures rather than passing over an empty
  addition. `tools/memory-tree/README.md:57` was FIXED to the tree-wide `<kit>/` convention its own
  line 141 and `codebase-map/README.md` already use, not waived.
- AC2 — `bash tools/check-install-prefix.test.sh` — the arm pair `S1 a .txt sidecar at a root
  spelling is caught` and `S1 ...and the same sidecar at the declared prefix is clean`. Observed RED
  with the break staged: `EXT` narrowed back to the original six extensions made the red arm report
  `exit 0, wanted 1`, so the arm is grading the widening and not something else. Both arms drive
  `bash tools/check-install-prefix.sh` over a fixture, and the widening reached `re_ship` and the
  root predicate together because both now read the one `EXT` string.
- AC3 — `bash tools/check-install-prefix.sh --rebaseline` — `REBASELINED for predicate epoch 2 -> 3`,
  rows 135 to 137. Reason columns counted 35 before and 35 after. The second invocation printed
  `REFUSING to rebaseline` and exited 1, which the suite also holds as arm `B5`.
- AC4 — `bash tools/check-install-prefix.test.sh` — arm `S4 the gate resolves its sidecars beside
  ITSELF, not at tools/`. The fixture moves the gate to `vendor/gov/` and puts the only waiver
  registry beside it there; a gate still spelling the old literal finds no registry and reds on the
  waived hit. Observed RED with the break staged: `WAIVERS` restored to its hardcoded form made that
  arm fail.
- AC5 — `bash tools/check-install-prefix.test.sh` — three arms over one line carrying
  `gov:root-fixture`: unmarked reds, marker with a reason is clean and counted, marker without a
  reason reds as `MARKER WITH NO REASON`. Each arm drives `bash tools/check-install-prefix.sh`. A
  fourth arm holds the other direction, that an UNSHIPPED test keeps its exclusion. Observed RED with
  two separate breaks staged: disabling the population union made the received-test arm report
  `rc 0, wanted 1`, and accepting a bare marker made the no-reason arm do the same.
- AC6 — `bash tools/check-install-prefix.test.sh` — the arm named for this criterion runs
  `bash tools/check-install-prefix.sh` over a fixture with no govkit registry, and holds that it
  prints the line naming the population it did not grade. The helper `recv_arm` refuses any fixture
  that took the skip branch, so the three arms above cannot pass by grading nothing.
- AC7 — `bash tools/check-install-prefix.test.sh` — PASS, all arms held, exit 0. Four breaks were
  staged and each was observed RED before its fix was restored: the narrowed extension class, the
  hardcoded sidecar path, the accepted reasonless marker and the disabled population union.

## The defect this build introduced, and where it was left-shifted

Marking the twenty deliberate fixtures meant appending a comment to twenty lines a gate had named.
Three of them ended in a line continuation, where a trailing backslash escapes the space before the
comment instead of the newline — valid shell that silently truncates the statement. `bash -n` passes
on it. Two were caught when `tools/check-wiring.test.sh` went from 92 arms to `91 passed, 1 failed`;
the third, in `tools/hooks/agent-cap.test.sh`, was caught by reading, because that suite reported
`215 passed, 0 failed` both before and after — the truncated branch is a fallback no fixture reaches.

The first repair then reintroduced the class in its other form: a Bash-tool heredoc ate a backslash
level, so the intended backslash-newline arrived as the two literal characters backslash and `n`,
mid-line. The gate itself caught that one by naming the same two lines as unmarked again.

Then writing THIS paragraph did it a third time. The sentence above originally spelled those two
characters as an escape inside a heredoc, and the heredoc turned it into a real newline in the
middle of the sentence. Recorded rather than quietly fixed, because three occurrences in one build
is the evidence that the trap is in the tool boundary and not in anyone's care: the escape must be
built from bytes, or the edit must not go through a heredoc at all.

Left-shifted to `memory/gotchas/inline-marker-breaks-a-line-continuation.md` rather than to a gate.
The record says in as many words that it has no machine gate, names the two near-zero-false-positive
predicates a gate would use, and says why this build did not write one: a gate added in passing is
how a predicate lands without its failing case ever being observed, which is the rule this same
build spent its effort enforcing.

## What this ledger does not claim

The gate now grades 257 of 1917 tracked files. The remainder is `memory/`, this repo's own records,
plus its configs and front-door docs — not shipped, repo-root-relative by §6, and out of scope by
rule rather than by oversight. Nothing here asserts that the 137 recorded carried literals are
correct; they are a floor that `DEPL-dCarriedReceipt-15` owns draining, and epoch 3 made 31 more
occurrences visible without fixing any of them.

No kit version was bumped. Every changed shipped file is a comment, a marker or a usage header, and
each kit's version constant declares its own trigger as an engine or render change — `codebase-map`
says so in the line above the constant. Recorded as a judgment rather than left as an omission: the
one change an adopter would actually want to receive is the `memory-tree` README `cp` step, and
bumping that kit means editing every doc carrying its marker for a one-line doc fix.
