---
name: ab-arm-never-did-the-work
description: a timing A/B whose arms are not each asserted to have DONE the work measures a refusal against a run, and the fast arm looks like the good one
kind: class
---

# An A/B arm that exited early is not a fast arm

## Symptom

You change something, you suspect it costs time, and you do the responsible thing: an interleaved
A/B, several rounds, alternating the binary so load drift cannot explain the gap. The gap is huge and
stable. You report a regression.

The old arm never ran. It failed early — a config refusal, a missing file, an unparseable flag — and
exited in the time a fast bar takes. **Nothing in a duration says whether work happened.** The
interleaving that made the measurement feel rigorous does nothing about this: it repeats the same
error three times and the consistency reads as confirmation.

The signature is a gap that is too clean. Real per-item costs scale with the item count and move with
load; a refusal is a flat constant, and it is usually *suspiciously round* next to the process
startup cost of the platform.

## Where it bit

`TOOL-aQuenchedHarness-1`, node `a`, 2026-09-06. A whole-run wall was added to
`tools/run-gates/run-gates.sh`, and `tools/run-gates/gate-profiles.txt` gained a `wall=` knob on
every row. The A/B copied the NEW profile table into a scratch fixture and then swapped only
`run-gates.sh` between `HEAD` and the working tree.

`HEAD`'s runner does not carry `wall` in `KNOWN_KNOBS`, and that table's governing invariant is that
an unknown knob is a refusal — so it hit `prof_die` and **exited 2 having run zero legs**, in 7.7 to
8.7 s. A real bar on the same box took 50 to 57 s. The reported result was **"+44 s per bar, a 6.4x
regression"**, three rounds, interleaved. It was a config refusal timed against a bar.

Re-measured with each arm carrying its OWN table: old 25679 / 25867 / 27082 ms against new 22520 /
23026 / 29312 ms. **No measurable difference.** The real cost of the thing under test was +4.7 s
quiet, and it was removed for other reasons.

The wrong number was reported to the owner as a measured fact before anyone checked it.

## The fix

**Assert the work, not the exit code — and assert it per arm, before the timing is recorded.**

```bash
run() {                      # -> milliseconds, or -1 if this arm did not do the work
  local s e rc
  s=$(date +%s%3N)
  <the command> > "$out" 2>&1
  rc=$?
  e=$(date +%s%3N)
  if [ "$rc" != 0 ] || ! grep -q '<the line only a completed run prints>' "$out"; then
    echo "!! arm did not do the work (rc=$rc): $(tail -1 "$out")" >&2
    printf -- '-1'; return
  fi
  printf '%s' "$(( e - s ))"
}
```

The predicate is a POSITIVE artifact of the work — a success line, a written file, a row count — never
`rc = 0` alone, because a program can exit 0 having skipped everything, and never the absence of an
error, because that is the same claim inverted.

Two more that cost nothing:

- **Swap the whole configuration with the binary, not just the binary.** The two travel together in
  the product; separating them in the fixture creates a pairing that ships nowhere.
- **Print each arm's own report line beside its time.** The refusal was on stdout in every one of the
  three rounds, in a file nobody opened, and the top line said `unknown knob key 'wall'`.

## What it is not

Not the same as `fixture-passes-by-finding-nothing`, which is about a test arm whose *predicate*
matches nothing. Here the predicate is a stopwatch and it is working correctly; what is empty is the
thing being timed.

Not fixed by more rounds, more interleaving, or a quieter box. Those address variance. This is bias,
and it survives every one of them.
