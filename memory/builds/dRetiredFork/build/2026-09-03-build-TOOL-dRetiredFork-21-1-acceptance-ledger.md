# Acceptance ledger — TOOL-dRetiredFork-21

**Serves:** journal TOOL-dRetiredFork-21

Tier-2 · node d · 2026-09-03

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-21

- AC1 — MET, already — `grep -rn '.claude/hooks/' tools/*/*.fragment.json` returns nothing. Both
  fragments were repathed by `TOOL-dRetiredFork-14` one unit earlier
- AC2 — MET — `bash tools/memory-recall/adopt-memory-recall.sh --with-hook` against a fixture writes
  nothing under `.claude/hooks/` and its closing line names
  `tools/memory-recall/recall-opened.js`, the path that actually ships
- AC3 — MET — the answer is recorded in this spec's §9 and it is the permissive one: `merge()` DOES
  rewrite a fragment-supplied path, so S1's edits suffice for an already-wired tree
- AC4 — MET — `bash tools/check-hook-destinations.sh` exits 1 naming both the fragment and the
  undeclared destination when one is reverted. Observed before the leg was wired, then restored
- AC5 — MET — with no `*.fragment.json` tracked the gate REFUSES, saying it has no subject rather
  than printing a zero
- AC6 — MET — `bash tools/check-wiring.sh` exits 0 at gov, and its own suite exits 0 against its
  fixtures
- AC7 — MET — `bash tools/check-testsuite-counts.sh` exits 0; the leg declares a ceiling and the
  suite pins `FLOOR_ASSERTIONS=8` and compares against it

## Two of six scope items were already done

`TOOL-dRetiredFork-14` overlapped this unit. **S1** was delivered there, with a difference worth
keeping: the spec asked for `{prefix}/...` and what shipped is a `{kit}` token expanded against the
fragment's own location. That is stronger, because it is correct for a repo whose kits sit at more
than one prefix — which is exactly what `check-wiring`'s own fixtures are.

**S3** was answered there too, and the answer decides whether S1 was sufficient. It was.

## Why the gate needed two populations

The obvious gate quantifies over fragments. It would have passed the entire time
`adopt-memory-recall.sh --with-hook` was re-creating `.claude/hooks/recall-opened.js`, because that
installer reads no fragment. A gate over declarations cannot see an installer.

So arm 2 quantifies over the adopter SCRIPTS and reds on a write into a destination no `kit.toml`
rule ships. Its failing case is not hypothetical — it is the state this repo was in an hour ago, and
the arm was written by staging that state back.

## The three-reader agreement

`{kit}` is now expanded in three places: `settings-merge.py` writes the command,
`check-wiring.sh` verifies it, and `check-hook-destinations.sh` grades the declaration. All three
resolve it the same way — two directories up from the `.fragment.json` — and they have to, or the
writer wires a path the checkers cannot find. That is stated in each of them rather than left as a
coincidence.

## Not done

S6 is a constraint this unit inherits and does not implement: the wired command moves BEFORE the old
copy is withdrawn. `DEPL-dRetiredFork-3` S5 and AC9 own enforcing it. Nothing here withdraws
anything.

## The gate is gov-side only, and that is a limit rather than a detail

`check-hook-destinations.sh` resolves the descriptors through `tools/govkit` — the deployer, which
is a registry exemption itself and never travels into a target. An adopter has fragments and adopter
scripts but no deployer, so this gate **cannot run in an adopter tree at all**.

Declared as an exemption with that reason rather than left to look like an oversight. The argument
for it being enough: gov is where fragments and descriptors are AUTHORED, so gov is where a fragment
naming an unshipped destination gets created. An adopter inherits the mistake; it does not make one.

That argument is sound and it is not complete. An adopter who edits their own fragment gets no
protection from this, and nothing in this build gives them any. Saying so is cheaper than a reader
later assuming the coverage is symmetric.

## One more thing the change broke, and the suite caught

`tools/memory-recall/selftest.py:979` asserted that `--with-hook` had written
`.claude/hooks/recall-opened.js` and compared its bytes. That arm was **pinning the defect in
place**: it would have failed any correct fix and passed the whole time the installer was
re-creating a withdrawn file. It now asserts the opposite — that nothing appears under
`.claude/hooks/` — and that the closing instruction names the copy it wired.

Its own title promised the old behaviour too ("copies NO hook without --with-hook"), so the title
moved with the assertion.
