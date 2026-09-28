**Serves:** diff-review TOOL-aRepatriatedFork-42

# aRepatriatedFork: Tier-2 closing diff review of unit 42, round 1

*Node `a`, 2026-09-29. This reviews `TOOL-aRepatriatedFork-42`, which makes the four memory-tree
renders take every adopter path from the adopter's own declarations through the playbook engine's
new `--answers` verb. Two primed finder lenses ran: correctness and contract, and adopter
integration seams at inCMS, nc and swydee. Every reproduction ran in a scratch clone under `$TEMP`;
no adopter tree was written.*

**Range reviewed: `012d9dd5..f02a3a56`** (branch `branch/arepatriated-fork-build-e42158`, records
excluded).

**Round: 1.**

## Verdict: CLEAN WITH FIXES

Two HIGH findings reproduced: an answer carrying a newline silently deletes text from all four
renders, and a memory-tree kit landed beside a playbook engine older than the one it calls cannot
render at all. The rest are MEDIUM and LOW contract gaps in the same derivation block. Every one
reproduced red on the `f02a3a56` bytes and is FOLDED into the unit's spec as a rev-3 bump.

## Review shape and run integrity

- **No skeptic ran.** The owner authorised the fold without one. In its place, every finding had to
  be reproduced RED on `f02a3a56`'s bytes in a scratch clone before any code moved for it; a finding
  that did not reproduce would have been marked REFUTED with its evidence and left alone. None was.
- **Raw findings:** 11 (C1-C7, I1-I4). Two pairs are one defect seen from two lenses: C2 is I1, and
  C3 is I2. That leaves 9 distinct defects, all reproduced.
- **Run integrity:** lenses 2/2 returned, 0 died.

## Red-first, on `f02a3a56`

One scratch fixture per finding: a flat adopter at `scripts/`, memory root `notes`, the playbook
engine beside it with a two-row descriptor. Rendered by that commit's own adopter script.

- **C1** — `[charter] gate_runner = """bash run.sh\nbuild\nz"""`: `--render` exits 0, and
  BUILD-METHOD.md's count of `build` falls from the template's 41 to 0.
- **C2 / I1** — the `012d9dd5` engine (playbook-render 1.9) beside the new kit: exit 2,
  `render_playbook.py: error: unrecognized arguments: --answers GATE_RUNNER kits ...`.
- **C3** — `gate_runner` carrying U+2014 under `PYTHONUTF8=0`: exit 0 and BUILD-METHOD.md is invalid
  UTF-8 at byte 327. Carrying U+2192: exit 2 on `UnicodeEncodeError`.
- **I2** — `kits` naming `lexcon` under `PYTHONUTF8=0`: exit 2 on `UnicodeDecodeError` then
  `AttributeError: 'NoneType' object has no attribute 'strip'`, and the named refusal never prints.
- **C4** — `[kit.kickoff-manifest] manifest_path = "x.md"` with no `[answers]` row: exit 2,
  `answers no manifest_path`, where govkit seeds and gates `x.md`. With `[answers] memory_root =
  "docs/mem"` against a conf of `notes`, the render exits 0 naming `notes/guides/REVIEW-PROTOCOL.md`
  while govkit installs the protocol under `docs/mem/`.
- **C5** — no engine, `notes/guides/UNATTENDED-PROTOCOL.md` present: three lines say the protocol
  is `(not installed here)`.
- **C6** — `--answers MEMORY_ROOT memory_root kits KITS` returns `"notes"`, `null`, the graded list
  and `null`.
- **C7** — the adopter's TEMPLATE-SPEC.md reads that gov's checker, not installed here, resolves a
  gate name against the adopter's `gate-legs.json`.
- **I3** — `user_skills = ".claude/skills"` with the skill tracked as a single file: the render names
  `.claude/skills/session-kickoff/SKILL.md`, which git does not track.
- **I4** — `review-harness` selected with no receipt at all: the render names
  `notes/guides/REVIEW-PROTOCOL.md`, a hand-typed copy of the descriptor's `to`.
- **I1, second half** — a scratch clone of inCMS at `f1d1c75a3`, whose engine is playbook-render
  1.9, taken through `govkit update --kits memory-tree --write --to f02a3a56`: both `--render` argv
  print `exit 2  REFUSED`, the run exits 1, and neither `unrecognized` nor `--answers` appears
  anywhere in its output. The argv's stderr is captured and never printed.

## Findings, verdicts and dispositions

| id | finder severity | red-first | final | disposition |
|---|---|---|---|---|
| C1 | HIGH | reproduced | HIGH | FOLDED S7 — a value carrying a tab, CR or newline is a named refusal before any file is written |
| C2 | HIGH | reproduced | HIGH | FOLDED S8 — the render reads the engine's version first; below the floor it states the phrases with one stderr line |
| I1 | HIGH | reproduced | HIGH | FOLDED S8 — same defect as C2; the edge is declared, and update prints a refused argv's stderr |
| C3 | MEDIUM | reproduced | MEDIUM | FOLDED S9 — UTF-8 in both directions |
| I2 | MEDIUM | reproduced | MEDIUM | FOLDED S9 — same defect as C3, from the refusal side |
| C4 | MEDIUM | reproduced | MEDIUM | FOLDED S10 — `--answers` takes govkit's per-entry overlay; a memory root declared twice must agree |
| C5 | MEDIUM | reproduced | LOW | FOLDED S11 — a neutral phrase, like the other four |
| C6 | LOW | reproduced | LOW | FOLDED S10 — keys compare case-insensitively, as `[answers]` and `[charter]` already do |
| C7 | LOW | reproduced | LOW | FOLDED S11 — the sentence names no gate-leg path |
| I3 | MEDIUM | reproduced | MEDIUM | FOLDED S11 — a repo-relative skill path renders only when git tracks it |
| I4 | LOW | reproduced | LOW | FOLDED S11 — the protocol paths come from the kit's rendered receipt row |

C5 grades LOW rather than MEDIUM: the phrase is false only where the protocol exists and the render
could not ask, and it names no path, so nothing resolves to a dead one.

## The coupling C2 and I1 asked for, and why it is not a `requires`

govkit has no version-floor syntax. A plain `requires = ["playbook-render"]` on memory-tree would
refuse every default `apply`, because the default selection carries memory-tree and not
playbook-render (`derive_unsatisfied_requires`, called by `_cmd_apply`). And no descriptor key makes
`update` roll two kits back together: a rollback is per kit by design. So the edge is recorded as a
`requires_if` row whose kit name selfcheck grades, and the render's own floor check is what binds.
Below the floor the render states the phrases rather than refusing. A tree whose engine was rolled
back after its docs were rendered then shows a named parity drift, and that stderr line says which
update repairs it.
