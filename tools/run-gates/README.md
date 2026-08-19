# run-gates kit

`gov:kit run-gates@1.0` — the marker a deployer greps; paired with `KIT_RUN_GATES_VERSION` in
`run-gates.sh` and asserted EQUAL by `tools/check-kit-versions.sh`. Presence of a marker is not
agreement between a marker and a constant, and this repo has twice had a half-bumped pair pass a
presence-only check.

## What this is

The merge-bar runner, its two harnesses, and the adopter that keeps a target's verdict-reading
declaration honest. The runner is a thin iterator over a leg manifest: it holds no leg command of
its own, and the canary asserts that.

## Why it became a kit

It was a registry EXEMPTION, with two stated reasons that were both exact. It sourced `tools/lib/`,
which is gov-internal and never travels; and with that path absent, `bash` sourcing a missing file
under `set -u` continues, `resolve_python` is undefined, and the guard on the next line fires — the
runner exited 2 having run ZERO legs. So `govkit apply` wired legs into a runner the target was
assumed to already own, and a target that owned none received a merge bar that could not start.

the aPacedTurnstile build's spec set under `memory/builds/aPacedTurnstile/spec/` cut that dependency by inlining the canonical resolver into every shipped
file that had one, byte-identically, under the markers `tools/lib/resolve-python.test.sh` greps for
— so each copy enrols itself in the parity gate rather than needing a table row.

## The pieces

| file | what it is |
|---|---|
| `run-gates.sh` | the runner. Legs run through a bounded pool, at the width `gate-profiles.txt` declares for the detected hardware; `GATE_JOBS` overrides the width alone |
| `gate-profiles.txt` | the DECLARED knob table: rows of name, minimum cores, minimum RAM MB, knobs, most-capable-first with a zero-threshold catch-all last. `GATE_PROFILE=<row>` selects one by name and skips detection; `GATE_PROFILES=<path>` reads a different table, and an absent path falls back to the built-in formula — which is the rollback. `GATE_CORES` / `GATE_RAM_MB` override the readings |
| `run-gates.test.sh` | the SHIPPED canary — every assertion here is true in any tree |
| `run-gates.gov.test.sh` | the GOV-ONLY arms, withheld from the payload; see below |
| `run-gates.evidence.test.sh` | the durability arm: a red leg's output survives on disk |
| `adopt-run-gates.sh` | `--check` asserts a target's `[gate_runner]` declaration still matches this runner's output strings |
| `adopt-run-gates.test.sh` | the adopter e2e, gated on EFFECTS rather than exit codes |
| `kit.toml` | this entry, declared as data |

## The leg manifest is the kit dir's SIBLING

`<prefix>/gate-legs.json`, DERIVED from this kit's own location rather than spelled, so a one-segment
install resolves it at any prefix. `GATE_LEGS` still outranks the derivation, which is the seam both
harnesses drive so a nested run never re-enters the real bar.

The manifest does NOT travel. A target's leg list is emitted from the selected kits' `[[gate_leg]]`
blocks; seeding an adopter with gov's leg names is the class
`memory/gotchas/pin-copied-from-another-corpus.md` exists for, and the adopter starts with an empty
list instead.

## The gov-only harness

`run-gates.gov.test.sh` is withheld from the payload by a `project-owned` rule in `kit.toml`, exactly
as the memory-recall kit withholds its recall-floor program and fixture, and for the same stated
reason: arms keyed on THIS repo's corpus are meaningless in another tree. It is a leg on gov's own
bar and carries an `[[exempt_leg]]` row in the registry — deliberately not a `[[gate_leg]]` here,
because a descriptor row naming a leg a target's manifest cannot carry is what reds the deployer's
selfcheck.

It REFUSES with exit 2, rather than passing, when the manifest it is pointed at is not gov's. A
gov-only harness that quietly succeeds against a foreign corpus is the split failing open.

## The report tail contract

Every tailed line is `<verb>  <leg name>  <tail>` — TWO spaces before the parenthesised tail, on
every verb. A reader splits the remainder on a double space and gets the bare leg name back; a
single space made that split return a truncated name for any leg whose name contains a space, which
is most of them, and the deployer reads a target's verdicts exactly that way. The gov-only canary
forbids a double space INSIDE a leg name, which is what keeps the split unambiguous rather than
merely usually right.
