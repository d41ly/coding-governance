# run-gates — the merge bar as a deployable kit

```toml
feature = "run-gates"
title = "The gate runner, its harnesses, and the adopter that keeps a target's verdict reader honest"
status = "shipped"
streams = ["tooling"]
decisions = ["TOOL-aPacedTurnstile-1", "TOOL-aPacedTurnstile-2"]

[claims]
gate-legs = ["run-gates gov canary", "run-gates adopter e2e", "run-gates wiring"]
kits = ["run-gates"]
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/run-gates/run-gates.sh",
  "tools/run-gates/adopt-run-gates.sh",
  "tools/run-gates/kit.toml",
  "tools/run-gates/gate-profiles.txt",
]
```

## Constraints & why

**The leg manifest is the kit dir's SIBLING, derived and never spelled.** `<prefix>/gate-legs.json`,
computed from the runner's own location. A hardcoded `tools/gate-legs.json` resolves to nothing at any
other install prefix, and this is a kit whose whole point is that it installs somewhere else.
`GATE_LEGS` outranks the derivation, and that seam is what both harnesses drive so a nested run never
re-enters the real bar.

**The manifest does NOT travel, and the canary that grades it splits in two.** A target's leg list is
emitted from the selected kits' `[[gate_leg]]` blocks; seeding an adopter with gov's leg names is
`memory/gotchas/pin-copied-from-another-corpus.md`. So `run-gates.test.sh` SHIPS and asserts only what
is true in any tree, while `run-gates.gov.test.sh` takes every arm keyed on this repo's corpus and is
withheld from the payload by a `project-owned` rule — the same mechanism, and the same stated reason,
as the memory-recall kit's recall-floor split. The gov-only file is a leg on gov's bar and an
`[[exempt_leg]]` row in the registry; it is deliberately NOT a `[[gate_leg]]` in `kit.toml`, because a
descriptor row naming a leg a target's manifest cannot carry is exactly what reds the deployer's
selfcheck.

**The gov-only harness REFUSES rather than passing on a foreign corpus.** It asserts a witness leg
name and exits 2 when the manifest is not gov's. A gov-only harness that quietly succeeds elsewhere is
the split failing open: every arm inside it would pass by finding nothing, and the next unit to add one
would inherit a green that means nothing.

**Membership is decided by GIT IDENTITY, never by comparing path strings.** The adopter asks git for
the toplevel from inside the kit dir and from inside the target, and compares those two answers.
Under MSYS one directory has two spellings — a `/tmp/...` mount and the `/c/Users/.../Temp/...` it
resolves to — and mount points are not symlinks, so a prefix strip across the two reports a kit
sitting INSIDE the target as being outside it. Measured: that refusal fired against a scratch target
the kit's own e2e had just built around it.

**The report tail is a two-space contract.** `<verb>  <leg name>  <tail>` on every verb, so a reader
splits the remainder on a double space and recovers the bare leg name. A single space returned a
truncated name for any leg whose name contains one, which is most of them, and the deployer reads a
target's verdicts exactly that way. The gov-only canary forbids a double space inside a leg NAME,
which is what makes the split unambiguous rather than usually right.

**The pool's knobs are DECLARED, and no knob may make the bar check less.** `gate-profiles.txt`
maps detected cores and RAM to a named row; the FIRST row satisfying both thresholds wins and the
last row is a zero-threshold catch-all, so unknown hardware is matched rather than special-cased.
Cores alone were the wrong question — each heavy leg builds its own scratch repo, so a 16-core / 8 GB
box used to select width 8 and thrash. The invariant is that a knob may cost SPEED or convert a hang
into a bounded RED, never turn a leg into a pass or a skip; the runner declares the implemented set
and the shipped canary PINS the same set separately, so a new knob reds until an author edits the pin
and reads the rule. An ABSENT table falls back to the built-in formula and is the documented
rollback; a MALFORMED one refuses, because a silently ignored knob is a knob the operator believes
they set. Matching NOTHING is a refusal too, and deliberately not the same state as absent.

**`--check` is the join nothing else asserts.** A target's `[gate_runner]` declaration names the line
heads the deployer matches to read verdicts; those heads are strings in the runner's own `printf`
calls. When the runner's output moves and the declaration does not, the deployer reports a bar that
ran nothing — silently, because "no lines matched" and "no legs ran" are one observation to a reader.

## Shared seams

**The inlined `resolve_python` block.** Between the `>>> resolve_python` / `<<< resolve_python`
markers in the runner and in both shipped harnesses, byte-identical to
`tools/lib/resolve-python.sh`. The parity gate derives its copy population by GREPPING for that
opening marker, so pasting the block enrols a new copy automatically — no table row, no gate edit.

**The `GATE_LEGS` seam.** The one override that lets any harness drive the real runner against a
fixture manifest. Without it the only way to exercise the runner is to invoke it against the repo,
which re-runs the whole bar recursively and clobbers the live summary mid-run.

**The manifest derivation.** Four lines carried identically by the runner and both harnesses, and the
gov-only canary asserts that identity as SOURCE PARITY rather than by recomputing it — an earlier
draft of that arm recomputed and compared two answers, which is `two-answers-to-one-question` inside
the arm written to prevent it, and it duly disagreed with itself.

**The `[gate_runner_seed]` table in `kit.toml`.** The seed `govkit intake` emits a target's own
`[gate_runner]` declaration from, resolving path tokens ONLY: the runner's `{name}` placeholder passes
through verbatim, because that substitution is the runner's and not the deployer's.

## Reuse affordance

seam: `KITDIR`/`ROOTN`/`KITREL`/`LEGS_FILE` — the four-line prefix derivation; reuse whenever a kit
file must resolve a sibling of its own install dir, and extend by copying the block verbatim so the
gov canary's source-parity arm keeps covering it.
seam: `GATE_LEGS` — reuse whenever a harness must drive the real runner without re-entering the bar;
extend by pointing it at a fixture manifest, never by adding a second seam.
seam: `[gate_runner_seed]` — reuse for any kit that needs a target-side declaration emitted at intake
time; extend by adding keys the deployer resolves, leaving runner-side placeholders untouched.

## Affordances

- **Run the bar** — `bash tools/run-gates/run-gates.sh`; `GATE_JOBS=1` for the serial path through the
  same code, `GATE_FULL=1` to ignore every leg guard.
- **Drive it against a fixture** — `GATE_LEGS=<file> bash tools/run-gates/run-gates.sh`, which is how
  every harness exercises the runner without re-entering the real bar.
- **Check a target's declaration** — `bash tools/run-gates/adopt-run-gates.sh --check`, which reports
  NOT ADOPTED and exits 0 where no target declares one.

## Gaps

- The shipped canary's threshold arms read their seam values FROM the table rather than pinning
  figures, because the table is data an adopter is expected to tune and a pinned figure would red on
  their tree while saying nothing about it. The cost is that the arms grade the mechanism, not gov's
  particular thresholds; nothing observes a gov threshold that drifts away from gov's hardware.

- `adopt-run-gates.sh` has no WRITE path today: the `[gate_runner]` declaration is emitted by
  `govkit intake` from this kit's `[gate_runner_seed]`, because a declaration written at configure
  time cannot reach the same run's leg-emission step. The adopt verb exists for `--check`.
- The descriptor's declared `[[gate_leg]]` guards and gov's manifest rows for the same leg names are
  joined by NAME only — `govkit selfcheck` never compares the two guards, so they can diverge with
  every gate green. `TOOL-aPacedTurnstile-12`.
