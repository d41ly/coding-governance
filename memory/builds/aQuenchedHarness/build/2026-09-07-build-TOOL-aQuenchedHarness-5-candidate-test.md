# Which mechanism removes the self-test cost — the four candidates, tested

**Serves:** research TOOL-aQuenchedHarness-5

Node `a`, 2026-09-07. `TOOL-aQuenchedHarness-5` §8 F1 is a FACT-QUESTION with four candidates, and
`memory/guides/BUILD-METHOD.md` M12 requires the test that REJECTED each loser to be recorded, not
just the winner. This is that record.

## The subject

`tools/check-line-length.test.sh`, chosen because it is mid-cost (320 s declared budget) and
structurally typical: a shared fixture, a `reset` before each arm, and one invocation of a shell
subject per arm. Traced with the technique
`memory/gotchas/process-creation-is-the-suite-cost.md` names:

```bash
PS4='+${LINENO} ' bash -x tools/check-line-length.test.sh > out 2> trace
```

**36 s wall, 18 arms, 432 traced lines.** The outer script alone spawns 31 `python`, 20 `rm`,
18 `grep` — and `bash -x` does NOT trace inside the subject, so the subject's own 12 python call
sites are additional and uncounted. At the 773 ms `python` and 319 ms bare-spawn costs measured on
this node, the traced 31 python alone are ~24 s of the 36 s.

**The dominant term is the SUBJECT'S OWN COST PER INVOCATION**, paid once per arm. It is not the
harness, and it is not fixture construction.

## The four candidates

**C1 — one fixture per suite instead of one per arm. REJECTED as a cost lever, KEPT as a
prerequisite.** The test: count fixture construction across the suites. Static `mktemp -d` counts run
2 to 12 per suite, not one per arm, and in this suite `reset()` is three file writes and an `rm` —
cheap. So rebuilding fixtures is not where the time goes and C1 buys nothing on its own. **But see
the winner: C1's mechanism turns out to be what makes C2 safe**, which is the opposite of how §8 F1
framed them. They compose; they do not compete.

**C2 — bounded intra-suite parallelism. WINS.** The arms are independent, each pays its own subject
invocation, and dividing them across workers divides the wall clock without changing a single thing
about what is asserted. It is also the only candidate that works regardless of what the subject is.

**C3 — batch the subject invocation so one checker process grades many staged subjects. REJECTED,
and the reason is structural rather than a missing feature.** Each arm stages a DIFFERENT break into
the fixture and asks the checker one question about it. A batched checker would have to accept N
trees and return N verdicts; `tools/check-line-length.sh` accepts one subject, and teaching it
otherwise would add a public surface to a shipped checker for the benefit of its own test. Recorded
rather than assumed: this is the candidate that looked strongest on paper.

**C4 — move arms in-process by rewriting suites in Python. REJECTED.** The subject here is
`tools/check-line-length.sh`, a bash script. Running its logic in-process means re-implementing it,
and then the suite grades the re-implementation — `memory/gotchas/second-implementation-is-not-a-
second-opinion.md`. It is also the only candidate that changes WHAT is being tested, which disqualifies
it independently of cost.

## The finding the test produced and the reasoning had not

**C2 IS UNSAFE WITHOUT C1, and the spec had them as alternatives.** Verified at source:

```
W="$TMP/repo"; mkdir -p "$W/tools"          # ONE directory, for the whole suite
reset() { line x 100 > "$W/subject.md"; printf 'subject.md\t450\n' > "$W/tools/line-length-limits.txt"; rm -f "$W/other.md"; }
arm()   { out=$(cd "$W" && bash tools/check-line-length.sh "$@" 2>&1); rc=$?; ... }
```

Every arm runs against the same `$W`, and `reset` MUTATES it in place immediately before each one.
Run two arms concurrently and the second's `reset` lands inside the first's subject invocation. Naive
parallelism does not make this suite faster; it makes it wrong, and wrong in the worst way — the arms
would still pass most of the time.

So the harness is C1 **and** C2, in that order: build the fixture once, snapshot it, and give each arm
a cheap private COPY of that snapshot. The copy is what buys isolation; the isolation is what makes
the pool safe; the pool is what removes the cost. C1's own justification in §8 F1 — that it saves
fixture-construction time — is refuted, and it is kept for a reason nobody wrote down.

## What this does NOT establish

The measurement is ONE suite. It is structurally typical of the ones read so far, but the top-cost
suites (`manifest-check self-test` at 2546 s, `run-gates canary` at 2436 s) have not been traced, and
a suite whose arms build a real git repository each would shift the balance back toward C1's original
justification. `TOOL-aQuenchedHarness-6` S3a's per-row condition reporting is where that gets
measured per suite rather than assumed from this one.

Nor does it establish the SPEED-UP. It establishes the mechanism. The factor comes from
`TOOL-aQuenchedHarness-6` S6's declared floor, measured per ported suite against its own before
reading, and no number is claimed here.
