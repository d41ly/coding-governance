**Serves:** journal TOOL-aGraftedHelix-1..15

# Build brief — aGraftedHelix, every unit

You build ONE unit, the one your dispatch names, from its spec. This brief adds what the harness
prompt does not carry. The shared spec brief beside this file
(`2026-10-04-prompt-TOOL-aGraftedHelix-1-1-spec-brief.md`) states twelve invariants; they bind the
build exactly as they bound the spec. Read your spec WHOLE, then the files its §4 names WHOLE.

## Fast checks only, nothing held

The only checks you run are the direct ones your spec's §6 names: a checker on a staged break, a
`--selftest` arm or a slice of one, a fixture, a grep over a rendered file. Fast, diff-scoped,
seconds to a few minutes. No merge bar, no self-test suite, no `*.test.sh`, no `GATE_*=` prefix: the
main loop runs them once at VERIFYING, and the gate-guard hook denies them on this branch until then.
A criterion only a suite observes is named in your `summary` and left for that run. To debug one arm
of a long suite, slice it: copy the prologue plus that one block into a temp script INSIDE the kit dir
and run that (`memory/gotchas/` and the owner's notes both record 22 s against 90 minutes).

## The commit sequence

1. The spec is already committed. If you must diverge, bump its rev with a §9 line in a commit of its
   own (`Pass: none`) BEFORE the code commit — a spec edit riding the code commit reds
   `pass-order history`.
2. The build commit carries the code, the spec's status flip to `CLOSED`, and every bookkeeping file
   the change owes (below), with `Pass: <unit-id>` in the trailer block.
3. The acceptance ledger: `memory/builds/aGraftedHelix/build/2026-10-04-build-<unit-id>-1-acceptance-ledger.md`,
   carrying `**Serves:** journal <unit-id>` and one line per acceptance criterion in the grammar
   `memory/HYGIENE.md` "Acceptance ledger" states — what ran, what it printed, at which sha. Write it
   in the build commit or in a records commit right after it.

## What a change here owes, every time — each gate names only its own

- **Kit versions.** Every kit whose shipped bytes moved is bumped once, after your last move, in every
  carrier `bash tools/check-kit-versions.sh` pairs; then `python tools/govkit/govkit.py epoch --base
  <your unit's starting HEAD>` must list none. A version marker can sit outside the files you edited:
  grep every carrier for the old version string before committing.
- **The codebase map.** A new function, file, leg, conf key or verb is an inventory key; claim it in
  the dossier under `memory/map/features/` that owns the surface, in the same commit, and re-render
  with the map's own `--write`. `python tools/codebase-map/reuse_lookup.py` names the dossiers.
- **The kickoff manifest.** If you touch a file on `memory/guides/SESSION-KICKOFF.md`'s watch list
  (`.unattended.conf`, `.memory-tree.conf`, `tools/gate-legs.json` and the rest it names), re-stamp
  its `last-audit` in the same commit; `bash skills/session-kickoff/manifest-check.sh` tells you.
- **Rendered copies.** Edit the template, never its render: `tier2-review.template.js` and
  `unattended-build.template.js` re-render through `bash tools/workflows/check-protocol-parity.test.sh
  --render`; the unattended kit's `*.template.md` re-install through
  `bash tools/unattended/adopt-unattended.sh`; the memory-tree kit's guides through its adopter.
- **Names and bytes.** New functions lead with a declared verb (`python tools/lexicon/lexicon.py
  --suggest <name> --as <cell>`); text IO names its encoding; `.sh` stays LF. On node `a`, Bash
  heredocs mangle backslashes and Python text mode eats a bare CR: author with the Write and Edit
  tools, and open shell files in binary mode when a script must edit them.
- **Every new arm is observed RED on a staged break** before it lands; the break is real (not a
  synthetic value the arm never reads) and is unstaged after.

## Per-unit notes

- **Units 1, 10, 11, 12** all edit the unattended driver. Fixture remotes are bare repos under
  `%TEMP%/<short-name>` (the scratchpad path is too long for a clone). No unit pushes to the real
  `origin` in a test: the real remote was probed once at spec time and that probe is recorded.
- **Units 5, 7** both edit `tools/run-gates/run-gates.sh`, a large file: read the dispatch loop and
  the run-record writer before editing, and keep every existing `GATE ` output line byte-stable.
- **Units 2, 8** edit `skills/session-kickoff/manifest-check.sh`, which is installed per machine
  through a junction; `bash tools/check-wiring.sh` reports whether the installed engine still matches.
- **Units 6, 13, 9, 14** edit the memory hygiene gate; a new check reads the real tree first and
  prints its hits before it may red.
