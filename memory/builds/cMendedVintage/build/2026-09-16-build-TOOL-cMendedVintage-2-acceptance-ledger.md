# cMendedVintage — the acceptance ledger for unit 2

**Serves:** journal TOOL-cMendedVintage-2

*Node `c`, 2026-09-16, written by the pass that built the unit. Every line below was taken against
the real files in the unit's own worktree, never a copy with a simplified read. No merge bar and no
`*.test.sh` suite ran in this pass; each criterion was answered by replaying its own command at the
shell, which is stated per criterion below.*

## The one thing worth reading twice

**Both halves of the coupling were observed FAILING before either was written.** The `seed` rule was
deleted from `tools/gate-lint/kit.toml` on its own, with the leg argv left naming the registry, and
`govkit selfcheck` exited 1 with the finding the brief predicts: the leg's argv names a path `which
NO rule in any descriptor writes, seeds, orders or produces`, so `apply` withholds it and exits 1 at
every adopter. The descriptor was restored from the index before anything else was written. That is
the failure this unit exists to avoid re-creating in the other direction, and it is the reason the
rule, the template and the argv element land in one commit.

The scanner's refusal was staged the same way. With S2's refusal removed, a registry path that does
not resolve stopped refusing and printed `sh-hygiene: OK — 0 declared site(s) in 0 row(s)` at exit 0
— a typo grading against nothing and reporting a pass. The new self-test arm redded on the same
break, so the arm is not vacuous.

**Evidences:** TOOL-cMendedVintage-2

- AC1 — `python3 tools/gate-lint/sh_hygiene.py --selftest` — run from the repo root through the
  resolved launcher. Exit 0, printing `PASS (27 assertions)`, against a `FLOOR_ASSERTIONS` raised
  24 to 27. The three added arms are named in the source as the absent argument resolving to an
  empty declaration, an argument naming a file being read through the same parser, and an argument
  that was supplied and does not resolve refusing. At BASE the same command printed
  `PASS (24 assertions)` and the absent case could not be asserted at all, because the positional
  was mandatory.
- AC2 — `python3 tools/gate-lint/sh_hygiene.py <scratch>/nosuch.txt <scratch>` — the scratch root is
  a `git init` fixture under this run's scratchpad holding one tracked `*.sh`, so the
  empty-population refusal is not what answers. Exit 2, and the message names the unresolved path in
  full before saying the argument was SUPPLIED and does not resolve to a file. The staged break
  described above is this criterion's red, observed at exit 0.
- AC3 — `python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` — run in
  this repo at BASE and at the tip. Both exit 0 and both print
  `OK — 19 declared site(s) in 18 row(s)` over 107 tracked files, with every measured population
  identical. This repo's own registry and its own leg row were not touched.
- AC4 — `python tools/govkit/govkit.py selfcheck` — exit 0, and its `gate legs:` note reads
  `26 of 26 registry entries graded · 132 argv element(s) offered against a bare target · 0 naming a
  path no rule produces`. The argv total is 133 at BASE and falls by the one element this unit
  drops. The half-landed tree reported 1 naming a path no rule produces, and exit 1.
- AC5 — `git grep -n substitution-fed-loops -- tools/gate-lint/` — no hit, exit 1. The template is
  absent from `git ls-files -- tools/gate-lint/`, which now lists four files, and
  `tools/gate-lint/README.md` carries the folded first-install prose under a heading of its own: the
  row shape, the key being the path plus the delimiter and never a line number, both directions of
  the set equality, and how to fill the file from the first run. The first cut of this criterion
  FAILED on a history comment in `tools/gate-lint/kit.toml` that still spelled the filename; the
  comment was reworded rather than the criterion loosened.

## What this ledger does NOT claim

That the merge bar is green. No leg of it ran in this pass, by the pass's own constraint. Three legs
this change can move are unobserved here and are owed at the run's close: `memory hygiene`, whose
check 3 is the whole reason the seed is being withdrawn and whose check 23 grades this very file;
`install-prefix (shipped surface)`, whose carried row for `tools/gate-lint/README.md` must still
read 3 — counted by hand at 3 after the fold, which is the same number, but counted by a `grep` and
not by the gate that owns the ratchet; and `testsuite counts (every bar self-test prints one)`,
which owns the floor this unit raised and was not run.

That an adopter was tested. Neither live adopter was touched or measured from here. The migration
residue — an adopter keeping the file they already own and losing the comparison until they put the
path back into their own leg argv — is asserted from the descriptor and the scanner, not observed at
a target, and `DEPL-cMendedVintage-9` owns the runbook half.
