**Serves:** spec-audit TOOL-aNamedGesture-1

## Verdict: CLEAN WITH FIXES

# Spec audit — TOOL-aNamedGesture-1 at rev-2

*Workflow `wf_c6fdfda7-723`. Four primed lenses, batched default-refute skeptics, one synthesis, per
M4 and `memory/guides/REVIEW-PROTOCOL.md`. Node a, 2026-08-25.*

**Review shape.** Raised 40, confirmed 15, refuted 25, unverified 0, **precision 0.38**. That is below
the protocol's 0.5 lever, and the diagnosis is priming rather than scope: the lenses were handed a
spec whose prose the unit had not written yet, so a large share of the refuted set was speculation
about wording that does not exist. Four of the ten surviving items were acceptance-coverage, which is
where the spec was thinnest and where a spec audit is worth most.

## What the audit found, ranked

**1. No acceptance criterion rendered a NON-DEFAULT value.** AC1 ran against this tree, whose conf S1
requires to declare the key blank; AC3 rendered the blank case; AC6 rendered malformed values; the
existing fixture at `tools/unattended/adopt-unattended.test.sh` declares no such key at all. The whole
set was therefore satisfied by an implementation that hardcodes the default and never reads the conf —
which is the one behaviour the owner's mandate asks for. Folded as AC4 and as the second arm of S11.

**2. The leading-hyphen guard was justified by a mechanism that cannot fire.** rev-2 argued it from
check 24 of `check-unattended.sh`. That check binds `tmpl="$HERE/SKILL.template.md"` and reads the
TEMPLATE, whose routing cell holds `{{AUTH_PARAM}}`; nothing parses the rendered routing table. The
rule survives on its real reason — the value is an argv flag, and a bare word reads as a positional
argument — and section 4 now records the false reason so nobody re-derives it.

**3. The whitespace discriminator was argued in one direction.** "A prose block is multi-word" is
true; the property the rule actually needed is its converse, "a path is single-word", which is false
for any quoted path containing a space. A real prompt file at a spaced path would have been read as
prose and become the build's entire scope statement. The grammar now runs the FILE TEST first and has
four rows, with the ambiguous case a refusal rather than a guess.

**4. The carrier count reproduced against nothing.** rev-2 said nine lines in six tracked source
files. `git grep -c 'gov:kit unattended@' -- tools/unattended/` gives five lines in five files
carrying seven values, plus three installed artifacts that belong to a different leg entirely. The
figure had been carried in from a probe rather than derived. S8 now points at the derivation and
section 4 records the measurement as a measurement.

**5. Verbatim bytes into the build README could inject a generated-region marker.** `region()` in
`unattended.sh` matches with `index(ln, o) == 1` and is blind to fencing, so a prompt quoting
`<!-- gen:build-index -->` at column 1 — ordinary in a prompt about this repository — makes preflight
raise the malformed-markers refusal, after the push, where the prompt path itself says no owner turn
remains. The audit proposed indentation. **The fold went further and changed mechanism:** the carried
value goes to a `prompts/` record, which this memory tree already sanctions as the only home for
prompt-kind files. That also clears the README's closed heading canon and its per-slot byte ceilings,
and moves the failure from preflight to the hygiene gate — before the commit rather than after the
push.

**6. Four smaller items**, all folded: the argument's termination rule and the root a relative path
resolves against (S6); AC7 exercising all four guard refusals rather than two; S10 gaining an
observation, since a `sed` entry nothing asserts is unobservable; and the `ratified` pointer on the
status header.

## What this audit did NOT cover

- **Nothing was executed.** The pass is read-only, so AC6's staged check-22 break, `check-kit-versions.sh`
  after the bump, and the full bar are unobserved.
- **The prose the unit will write does not exist yet.** Only the instructions that produce it were
  graded, so its interaction with check 24's extraction and check 25's literal greps is ungraded.
- **F1's resolution was re-read, not re-executed** against a fixture adopter tree.
- **The `recipe` asymmetry non-goal was not graded** against the driver's `SECOND_ANCHOR_MODES`
  handling.
- **No security lens ran** beyond section 8's own F2 analysis.
- **S14 was not found by this audit.** The read-path ceiling movement came out of measuring the
  margin by hand while the audit was running.

## Disposition

Every item is a spec-prose or acceptance-coverage gap closed by the rev-3 fold; none makes the design
unbuildable, which is why the verdict is CLEAN WITH FIXES rather than BLOCKED. Per M4 this spec is now
reviewed and is not re-reviewed: the next pass is the build.
