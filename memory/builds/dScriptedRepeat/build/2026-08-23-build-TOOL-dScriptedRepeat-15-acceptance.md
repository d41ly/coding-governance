**Serves:** journal TOOL-dScriptedRepeat-15

# TOOL-dScriptedRepeat-15 — the acceptance record

Node `d`, 2026-08-23. One line per numbered criterion, naming the observation that answered it. Six
criteria; one of them was not run at all, and it says so here rather than being written as a pass.

**The headline is that S1 changed the unit.** Rev-2 listed two candidate levers and said "nothing is
built until S1 speaks". S1 spoke: the leg is not compute-bound at all — `real 14.4s user 0.33s
sys 0.62s` — and the 93% it spends waiting is process creation, because an on-access antivirus
scanner fronts every `exec` on this node at 0.019-0.039 s a spawn against roughly a millisecond
elsewhere. The suite's real unit of cost is about 114,000 process creations. So the spawn count was
cut and the per-arm scoping was declined, with the arithmetic for declining it recorded.

## The criteria

**Evidences:** TOOL-dScriptedRepeat-15

- **AC1** — `tools/unattended/run-unattended-gates.sh` takes the SECOND branch this criterion offers:
  the ceiling is re-declared, from 900 s to 1800 s, with the derivation written beside it in that
  file. It is not silence — the note says what the cost is, what was cut, what the projection is, and
  that the projection is derived rather than timed.
- **AC2** — `FLOOR_ASSERTIONS=392` in `tools/unattended/check-unattended.test.sh` is untouched and no
  line of that file is in this unit's diff. The criterion asked that it not move and it did not.
- **AC3** — `memory/builds/dScriptedRepeat/build/2026-08-23-build-TOOL-dScriptedRepeat-5-bar-cost-measurement.md`
  carries an `## S1` section where every figure is written with the command that produced it, and the
  four superseded claims are marked **SUPERSEDED** in place: the 22 s real-repo reading, the "eighty
  arms" count, the 13.2 s quotient, and the 28x and 23-minute claims that lived only in prose.
- **AC4** — observed, both directions. With `declared_list` gutted, `--only 28` exits 1 with 10 lines
  and `--skip 28` exits 0 with none; with the driver's `--plan` header renamed, `--only 28` exits 0
  and `--skip 28` exits 1. Each scope reds on its own region's break and is blind to the other's.
- **AC5** — `tools/unattended/check-unattended.sh` at HEAD against this working copy: **19 staged
  breaks, 18 of them RED**, each run through the pre-unit checker and the
  post-unit checker over the same fixture tree: stdout+stderr and exit status byte-identical in every
  case. It covers all THREE shapes of broken parser — an emptied body, a syntax error, and one
  returning a MULTI-LINE answer, which is what misaligns a record-per-specimen protocol and is the
  shape the batching had to keep indistinguishable from the unbatched form. Also: a drifted parser
  pair, a removed refusal, a lost comment strip, a lost comma strip, an emptied verb set, a renamed
  verb header, a commented-out key reader, an ad-hoc key pipeline, a flipped sha pin, an unpinned
  wrapper, a dropped call-site status, and an unenumerable call site.
- **AC6** — **NOT RUN, and not passed.** It tests that a deliberately wrong scope on a `miss` or
  `same` arm still reds. No arm carries a scope, because S3 and S4 were declined, so there is no
  classification to mis-apply and the criterion has no subject. Recorded as moot in the spec's rev-3
  rather than reported as green.

## What was measured, and what was derived

Measured: the spawn count, 469 → 220, from an execution trace taken both ways. The per-spawn cost,
0.019-0.039 s, from three 100-iteration loops. The per-region breakdown, from 18 timestamp writes
inside the fixture. The CPU/wall split. The 17-case equivalence corpus.

Derived: the suite's post-unit cost, 1342 s, by scaling the ledger's recorded 2859.7 s sharded pair by
220/469. Two independent routes agree — 243 invocations × 5.2 s + fixture overhead lands in the same
place — but neither is a stopwatch on the suite.

**Not observed: the suite end to end at this commit.** The owner stopped these suites after two days
of repeated runs and that instruction stands. One command settles it whenever the owner wants it
settled:

```
bash tools/unattended/run-unattended-gates.sh --selftests
```

## The measurement mistake this unit made and corrected inside itself

A line-level `set -x` profile attributed 4.33 s to 28b's two grep lines. Acting on it cut 231 grep
spawns and moved the wall clock by nothing measurable. The reason is that `set -x` writes one line per
command, so its overhead lands on whichever line comes next and is proportional to CALL COUNT — it was
a call-count profile wearing a time profile's clothes. The per-region timestamps that replaced it cost
18 writes and put 5.02 s of a 10.74 s invocation in the four parser loops, which is where the change
that mattered was then made. Recorded because the same trap is one command away for anyone profiling
a shell program.

## Round 7 refuted this record's central claim, and that is the entry worth reading

**AC5 said the batched harness is byte-identical to the per-specimen one in every failure shape. It
was not.** The 19-case corpus tested parsers broken for EVERY input; the shape that matters is a parser
broken for ONE input shape. A `declared_scalar` emitting an extra line only for multi-line input —
which is what the shipped template block is, and what a comment-leak regression looks like — left the
whole leg at **rc 0 with zero output**, because the misaligned-reply fallback answered every slot with
`(rc 0, "")` and that is the PASSING pair in both template arms.

Observed, both directions: pre-fold **rc 0, 0 lines**; post-fold **rc 1, 8 lines** naming the harness
refusal. The corpus missed it because gutting a parser for every input makes the fixed specimen arms
fail first, and their noise made the two outputs identical while the template loop went quiet behind
it. **A staged break must be scoped to the input shape the new code handles differently** — that is the
lesson, and it is minted as `fallback-fabricates-the-passing-value`.

AC1's `--help` text also still quoted the pre-unit cost beside the ceiling this unit re-declared, in
the same file. It derives the figure from the `BUDGET_*` declarations now.
