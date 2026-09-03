# Build brief — TOOL-dRetiredFork-13

**Serves:** journal TOOL-dRetiredFork-13

Recorded BEFORE the pass. Units 11 and 12 were not, and their briefs say so.

## AC0, re-derived from the ratchet before anything else

**33 test/selftest rows summing to 259**, out of 112 rows and 652 occurrences today. The spec's AC0
said the ratchet holds 33 and rev-1 said 32; the ratchet says **33**, so rev-1 was wrong.

`.githooks/pre-push.test.sh` (2 occurrences) belongs to **this** unit. `TOOL-dRetiredFork-11` added
an arm to that file but swept no literals from it, and its own ratchet row moved only for
`.githooks/pre-push`, not the suite beside it.

The total is 652 rather than the spec's 656 because three earlier units in this build re-baselined
the ratchet. AC4's "strictly below 656" is therefore measured against 652, and saying so is cheaper
than a criterion that passes on someone else's arithmetic.

## The mechanism, already proven

One line — `KIT_REL="${KIT_REL:-<prefix>}"` — then every kit-path literal beneath it reads through
it. `check-unattended.test.sh` retired 127 sites this way and `adopt-unattended.test.sh` 28 more.

**Two prefix shapes, not one.** A kit-local suite takes `tools/<kit>`, matching the proven idiom. A
suite sitting directly under `tools/` references SEVERAL kits, so a single `tools/<kit>` cannot
serve it; those take `tools` — the kit ROOT — and keep the kit name at each site. The shape is
derived per file from the longest common prefix of its own literals, never assumed.

## What the idiom does NOT touch, and why the floor is not zero

The two already-swept files still carry 2 and 3 occurrences, and that is correct rather than
incomplete. Comment and usage lines keep their literal — `bash tools/unattended/check-unattended.sh`
in a header is what a human types — and a cross-kit reference inside an assertion string names
another kit's path, which `KIT_REL` must not rewrite because it does not point there.

So AC0b's "per-file rows expected to reach zero" is unmeetable as worded for most files. The
measurable claim is that FUNCTIONAL sites reach zero and the residue is comments and cross-kit
references. The ledger names each file's residue rather than reporting a total.

## The safety net

AC1 is automatable and is the whole reason this sweep is safe: expand `$KIT_REL` back to its
default, remove the added line, and the file must reproduce its pre-change bytes exactly. Every
touched file gets that check mechanically, not a sample.

AC3 is the honest half — a suite proven equivalent but never RUN at a foreign prefix is named as
unexercised. An equivalence proof covers regression and says nothing about the new capability.
