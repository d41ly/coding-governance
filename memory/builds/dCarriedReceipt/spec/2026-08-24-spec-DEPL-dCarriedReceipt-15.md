# DEPL-dCarriedReceipt-15 — gov stops shipping its own prefix inside kit bodies

**Status:** SPECCED · rev-1 · 2026-08-24 · node d · Tier-2 · base 9ddcc5c9 · streams deployer · ratified 2026-08-24

## 1. Goal

`apply` writes gov's bytes verbatim — `blob_at` at `:2453`, `write_bytes` at `:2469`, with no
substitution between them. `resolve_tokens` (`:516`) reaches destinations, gate-leg argv and guards,
hole discharge commands, adopt and check argv, and `lf_pin` patterns (`:1820`), and it reaches no
file body anywhere. So every literal `tools/<kit>/…` path a kit body spells arrives unchanged in a
target installed at another prefix. Measured over govkit's own shippable set at `9ddcc5c9` — the 168
source blobs `resolve_entry` (`:270`) resolves across the registry — **93 files carry such a path,
across 534 lines**; excluding test and selftest sources, 64 files across 219 lines. That is what
manufactured inCMS's divergence: its `scripts/lexicon/lexicon.py` carries seven `tools/`-prefixed
paths right now, none of which resolve in its tree, and hand-editing them is the only remedy an
adopter has ever had. Every sync would re-manufacture the same edit. `-9`'s needle map papers over
the symptom row by row; this unit removes the bytes that produce it.

## 2. Scope (IN)

- **S1** — `tools/check-install-prefix.sh` gains a second arm over a second population: the
  SHIPPING prefix (`tools/<kit>/<file>`) inside the set `resolve_entry` declares shippable, rather
  than the root spelling the existing arm owns over a glob-derived surface. The existing arm and its
  line-granular waivers are untouched.
- **S2** — the new arm's population is derived, never listed. It walks the registry through
  `read_descriptors` and `resolve_entry`, so a new kit and a new shipped file both enrol the day
  they land, exactly as the kit-name alternation at `:38` already does.
- **S3** — the new arm is INERT where the repo is not a kit source, detected by the absence of
  `tools/govkit/registry.toml`, and it says so in one line rather than passing silently. This kit is
  deployed to NicoCares, which installs at `scripts/`; an arm keying on the LOCAL prefix would red
  every usage header in every kit NC received.
- **S4** — a shrink-only ratchet at `tools/install-prefix-carried.txt`, one `<path><TAB><count>` row
  per shippable file. The count may fall and never rise, and a row falling to zero must be deleted.
  Per FILE rather than per line, because the existing `<path>:<line>` waiver shape goes stale on
  every edit above a waived line, and 534 rows of it would rot within a week.
- **S5** — the executable population fixes itself by DERIVING its own path rather than spelling one.
  `tools/lexicon/lexicon.py` is the demonstration: its runtime usage line (`:559`) computes the path
  from `__file__` against the repo root, and its docstring usage block (`:5-7`) moves into that one
  runtime printer, so the literal has exactly one home and that home is derived.
- **S6** — `render_doc` gets ONE canonical copy under the `resolve_python` pattern this repo already
  runs: the canonical body in `tools/lib/`, a `>>> render_doc — canonical copy:` marker in every
  inlined copy, and the parity population derived by grepping that marker. It retires the second
  spelling at `tools/memory-tree/kit-dogfood-parity.test.sh:58-72`, whose own comment already names
  itself as the drift class.

## 3. Non-goals (OUT)

- **Not** converting all 534 lines. S5 converts the lexicon kit and the ratchet holds the rest; a
  unit that rewrites every shipped body is a unit nobody can review.
- **Not** rendering placeholders at the write seam. The eager version of this unit teaches `apply`
  to substitute into file bodies, and it must not: the receipt's `sha256` at `:2458` is computed
  from the bytes about to be written, so a rendered body recorded against a single identity reads
  `differs` forever afterwards. Two identities belong to `-7` and the `relocate` rung to `-9`. This
  unit adds no substitution to any write path, which is what keeps it landable alone.
- **Not** touching `-9`'s needle map, `carry`, or any rung name.
- **Not** a reverse transform, an upstream verb, or a free-form rewrite rule. Build-wide cut line.
- **Not** widening the EXISTING arm's population or relaxing any of its twelve waivers.
- **Land-alone:** this unit leaves gov green on its own and changes nothing in either adopter tree
  beyond the lexicon kit's own bytes. It has no landing partner. Its only ordering constraint is the
  negative one above — the write-seam render is not in it, so `-7` is not a prerequisite.

## 4. Design

### Inventory

Measured at `9ddcc5c9` over the 168 shippable source blobs, at prefix `tools`:

| population | files carrying a literal `tools/<kit>/…` path | lines |
|---|---|---|
| all shippable sources | 93 | 534 |
| non-test shippable sources | 64 | 219 |
| of those, executables (`.sh` `.py` `.js`) | 44 | 156 |
| of those, docs and data | 20 | 63 |

The three heaviest files are `tools/gate-legs.json` (57), `tools/check-kit-versions.sh` (27) and
`WIRE-INTO-PROJECT.md` (27). The first two are gov-internal and reach no target through
`resolve_entry`, which is precisely why the new arm's population is the shippable set rather than
the existing arm's `tools/*` glob.

### Data model

`tools/install-prefix-carried.txt` is tracked, comment-tolerant, `<path><TAB><count>`. It is a FLOOR
file in the same sense inCMS's `.governance/row-count.txt` is: the number may fall, never rise. A
file absent from it may carry zero hits and no more.

### Alternatives rejected

- *Make the existing regex prefix-parametric in place.* The two questions have different populations
  and different remedies. The root spelling is a mistake with twelve deliberate exceptions; the
  shipping prefix is 534 lines of standing debt. Folding them into one predicate means one waiver
  file where a real root-spelling regression hides among the debt rows.
- *Placeholders in executable bodies, rendered at install.* `check-install-prefix.sh:52-54` already
  blesses `{{TOOL_ROOT}}` and the shipped `*.template.md` set already uses it, so the mechanism is
  real — but it needs a render step, and gov RUNS its own executables from its own tree. A
  `{{TOOL_ROOT}}` in `lexicon.py`'s usage printer is wrong in gov and wrong in every adopter until
  something substitutes it. Runtime derivation is correct in both with no step at all, and the
  existing gate's own rationale at `:8` already says every engine derives its own prefix.
- *Keep `render_doc` duplicated.* Two spellings of one substitution is what
  `kit-dogfood-parity.test.sh:55` names in its own comment, and
  `tools/unattended/cross-component.test.sh:53-56` is already a further spelling using `sed` with a
  `|` delimiter, the exact hazard `render_doc`'s comment at `:65-67` warns against.

### Files touched (estimate)

`tools/check-install-prefix.sh` (~60 lines), `tools/install-prefix-carried.txt` (new, ~93 rows),
`tools/check-install-prefix.test.sh` (4 arms), `tools/lexicon/lexicon.py` (~12 lines),
`tools/lib/render-doc.sh` (new, ~15 lines), plus marker enrolment in
`tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`.

## 5. Production-readiness checklist

- security — N/A: the arm reads tracked bytes and writes nothing, and no path in it reaches a target.
- perf / scale — one registry walk plus one read of 168 blobs, on a leg that already reads 162 files.
  Same order of magnitude as the arm beside it.
- a11y — N/A: CLI.
- i18n — N/A.
- error / empty / loading states — a repo with no `tools/govkit/registry.toml` prints the announced
  skip and exits 0. An empty shippable set is a failure and not a pass, matching the existing arm's
  two empty-population guards at `:39` and `:50`.
- observability — `--list` gains a `carried-prefix` section printing per-file counts against their
  floors, so the debt is readable rather than inferred from an exit code.
- risks — the material risk is redding an adopter's bar with a gate they receive. S3 is the answer
  and AC3 is its proof. The residual risk is a per-file count hiding a swap, one literal removed and
  another added in the same file. Accepted, and named, because per-line granularity was measured to
  rot faster than it guards.
- testing + left-shift gates — four arms in `tools/check-install-prefix.test.sh`, each observed RED
  before the fix. The left-shift is S1 itself: the class becomes a standing predicate over a derived
  population, so a new kit shipping a literal prefix reds on its landing commit.
- migration / rollback — the ratchet file is new and additive, and deleting it with the arm restores
  `9ddcc5c9` behaviour exactly. `lexicon.py`'s change is a pure move of one string into a printer.
- user docs — `WIRE-INTO-PROJECT.md` gains one line under the install step saying a kit body never
  spells the install prefix, and how the ratchet is read. Its own 27 literal paths are prescriptive
  install instructions and stay, entered in the ratchet with that reason.

## 6. Acceptance criteria

- **AC1** — `bash tools/check-install-prefix.sh --list` prints a `carried-prefix` section naming 93
  shippable files and 534 lines. Observe RED first: at `9ddcc5c9` the command prints no such section
  and exits 0 with every one of those lines unmeasured.
- **AC2** — Adding one literal `tools/lexicon/lexicon.py` to a shippable file that
  `tools/install-prefix-carried.txt` records at its current count makes
  `bash tools/check-install-prefix.sh` exit 1 and name that file. Removing a hit and lowering the row
  keeps it at 0. Staged, observed red, unstaged.
- **AC3** — Run against a fixture with no `tools/govkit/registry.toml`, the same command prints one
  line naming the skipped arm and its reason, and exits 0. A NicoCares-shaped fixture at
  `prefix = "scripts"` carrying `scripts/lexicon/lexicon.py` in a usage header is NOT a hit.
- **AC4** — `python tools/lexicon/lexicon.py --nosuchmode` prints a usage line reading
  `tools/lexicon/lexicon.py`, and the same file copied to `scripts/lexicon/lexicon.py` in a scratch
  repo prints `scripts/lexicon/lexicon.py`. Observe RED first: at `9ddcc5c9` both print
  `tools/lexicon/lexicon.py`, which is inCMS's seven unresolvable paths.
- **AC5** — `grep -cE 'tools/[A-Za-z0-9_-]+/' tools/lexicon/lexicon.py` returns 0, and
  `tools/install-prefix-carried.txt` carries no row for that file.
- **AC6** — Editing one inlined `render_doc` copy without the other reds
  `bash tools/memory-tree/kit-dogfood-parity.test.sh`, and the marker-derived population names both
  `tools/memory-tree/adopt-memory-tree.sh` and `tools/memory-tree/kit-dogfood-parity.test.sh`.
- **AC7** — `bash tools/run-gates/run-gates.sh` is green, and green again under `GATE_SELFTESTS=1`,
  so the `install-prefix self-test` kit-subject leg is exercised rather than held past this change.

## 7. Gates

`bash tools/run-gates/run-gates.sh` full bar. Specifically the `install-prefix (shipped surface)`
leg, its `install-prefix self-test` kit-subject sibling, `kit/dogfood doc parity`, and the
`python resolver (behaviour + inline parity + idiom ban)` leg whose marker mechanism S6 reuses.
Adds four arms and one tracked ratchet file. **Adds no gate leg**, deliberately: extending the
existing script leaves `tools/gate-legs.json` unchanged and therefore does not re-stamp the kickoff
manifest.

## 8. Open questions

- **F1 — per-file counts, or per-line waivers like the existing arm?** Per file. Measured: the
  existing shape is `<path>:<line>`, and 534 rows of it would go stale on the first edit above any
  waived line, at which point the stale-waiver arm at `:92-97` reds for a reason unrelated to the
  class. Per file trades swap-blindness for a ratchet that survives ordinary editing.
  RESOLVED (agent, 2026-08-24, delegated): per file, under the full-scope approval.
- **F2 — should `WIRE-INTO-PROJECT.md`'s 27 prescriptive paths be converted?** No. They are the
  instructions for choosing a prefix, so they must show a concrete one. They enter the ratchet with
  that reason and stay; converting them would make the install document teach a placeholder nobody
  substitutes.
  RESOLVED (agent, 2026-08-24, delegated): ratcheted, not converted.

## 9. Revision log

- rev-1 · 2026-08-24 · initial draft, from the kit-sync design pass. Three corrections to the
  design-pass brief, each re-measured at `9ddcc5c9`. **(a)** The brief's "59 files under gov `tools/`
  contain a literal `tools/<kit>/` path" does not reproduce at any population tried: 93 of 168
  shippable sources (534 lines), 64 non-test (219 lines), 77 files over the existing arm's
  glob-derived shipped surface (340 lines), or 70 of those restricted to `tools/`. This spec carries
  the measured numbers and states its population. **(b)** The brief asks that `render_doc` be
  promoted "into govkit as the ONE renderer". It cannot be: every consumer is shipped bash running
  standalone in the adopter's tree, and govkit is Python that never runs there —
  `adopt-memory-tree.sh`, `kit-dogfood-parity.test.sh`, `adopt-unattended.sh`,
  `adopt-memory-recall.sh` and `cross-component.test.sh` are five shell spellings and there are zero
  Python callers. S6 promotes it under the `resolve_python` canonical-copy pattern instead, which is
  this repo's existing answer to exactly this shape. **(c)** The brief reads
  `check-install-prefix.sh:53` as blessing the placeholder form; the blessing is implemented at
  `:55`, by the `{}` characters in the excluded lead-character class, and `:52-54` is the comment
  explaining it. Verified and unchanged from the brief: `blob_at` at `:2453`, `write_bytes` at
  `:2469`, `resolve_tokens` at `:516`, `render_doc` at `adopt-memory-tree.sh:64-78`, and lexicon's
  seven paths in both trees.

## 10. Reuse audit

No new mechanism. S2's population comes from `read_descriptors` plus `resolve_entry` (`:270`), the
same pair `planned_writes` (`:1359`) uses, rather than a second path map — the duplicate-answer
defect this build fixes elsewhere. S4's ratchet reuses the shrink-only shape and the stale-row rule
already implemented for `tools/install-prefix-waivers.txt`, in a second file only because the two
populations differ. S6 reuses the `resolve_python` canonical-copy machinery at
`tools/lib/resolve-python.sh`, whose parity gate already derives its population by grepping an inline
marker, so `render_doc` enrols into an existing gate rather than earning a new one. S3's announced
skip reuses the existing arm's two empty-population refusals at `:39` and `:50`. Nothing here touches
`resolve_tokens`, which stays a substituter for paths and argv and never becomes a body renderer.
