# TOOL-aUnmannedHelm-7 — the rendered skill, and the two ways it goes stale

**Status:** INPROGRESS · rev-2 · 2026-08-10 · node a · Tier-2 · base 930d50be · streams tooling · ratified 2026-08-10 · review wf_077104e6

## 1. Goal

Put the protocol where the agent actually reads it: a Skill, rendered from the kit's template plus
the project's declarations, so the tool calls it names are this repo's and not the kit author's.
This is unit 5 of seven; the master scope and the ratified decision menu live in this build's
`README.md`.

A rendered file has exactly two failure modes and this repo has been bitten by both. It can DRIFT
from its template, and it can arrive CRLF on a checkout while `git status` stays clean. Each gets
its own acceptance criterion, because a fix for one reads like a fix for the other.

## 2. Scope (IN)

- **S1 · `tools/unattended/SKILL.template.md`** — the agent-facing protocol summary, with the
  project's values as placeholders.
- **S2 · `tools/unattended/adopt-unattended.sh`** with `--render` (default) and `--check`. `--check`
  renders to a temp file and diffs, so a hand-edited Skill reds rather than being silently accepted.
- **S3 · the rendered `.claude/skills/unattended/SKILL.md`**, committed.
- **S4 · the `.gitattributes` `eol=lf` pin.** That is the whole of the CRLF work: `check-wiring.sh`'s
  eol population is DERIVED — tracked files under `.claude/` carrying the pin — so the new render
  joins it with no edit to that script.
- **S5 · the fourth gate leg**, `adopt-unattended.sh --check`, so the drift criterion is on the bar
  at this unit's landing rather than at unit 7's.

## 3. Non-goals (OUT)

- **The full adopter.** Unit 7 extends this same script with the foreign-repo and unsupported-prefix
  refusals, the junction behaviour, the conf and gate installation, and the e2e leg. This unit
  builds the render half only, and says so rather than pretending the script is finished.
- **Editing `check-wiring.sh`.** Its population is derived; an edit here would be a second spelling
  of a bound that already exists.
- **A `fail()` helper.** The existing adopters use plain `echo` + `exit`, and adding the helper would
  pull this script into `check-arms.py`'s discovered gate population, where an adopter does not
  belong. Following the precedent is the decision, not an omission.
- **Any agent-cap edit.** `TOOL-aNumeralWarden-1`'s.

## 4. Design

### The two failure modes, and why one pin is not enough

A gate that BYTE-COMPARES a rendered file needs both halves:

- the `eol=lf` pin, so the committed bytes are right on every node, and
- CR normalisation in the comparison, so a Windows checkout does not report every line as drift.

Either alone leaves the file green only right after a render. `--check` normalises CR on both sides;
`.gitattributes` supplies the pin. The recorded case is on this repo's own rendered skills: a
worktree checkout landed CRLF on an `eol=lf` path, `git status` stayed clean because the index
normalises on commit, and the byte-comparing leg reported every line of a file the session never
touched.

### What the Skill says, and what it refuses to say

It carries the protocol's obligations in the agent's second person, and the values that differ per
repo come from `.unattended.conf` at render time: the keepalive tool calls, the lander, the memory
root and the kit path. Nothing project-specific is written into the template, because the template
is what an adopter installs.

It states the keepalive obligation on BOTH ends — schedule before leaving the first phase, reap
before a terminal one — because that is the half no script can do, and a Skill that named only the
driver's verbs would leave the agent's own obligation unwritten.

### Files touched

New: `tools/unattended/SKILL.template.md`, `tools/unattended/adopt-unattended.sh`,
`.claude/skills/unattended/SKILL.md`. Edited: `.gitattributes` (one pin),
`tools/gate-legs.json` (one entry), `AGENTS.md` (the leg citation),
`memory/map/features/unattended.md` (the `rendered-skills` claim its `Gaps` currently declares
empty).

### Alternatives rejected

- **Writing the Skill by hand.** Then the project's tool names live in two places, and the one an
  adopter installs is this repo's.
- **Pinning without normalising, or normalising without pinning.** Each leaves the file green only
  immediately after a render; the trap is recorded because both were tried.
- **Adding the eol path to `check-wiring.sh` by name.** Its population is derived from the pin.

## 5. Production-readiness checklist

- **security** — the adopter writes two paths, both under the adopting repo, both derived from the
  repo root git reports. Unit 7 adds the refusals that make "the adopting repo" unambiguous.
- **perf / scale** — one `sed` and one `diff`.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — an unrendered Skill under `--check` is a named refusal, not a
  skip; a missing template is a named refusal.
- **observability** — `--check` prints the diff, capped, plus the command that fixes it.
- **risks** — the dominant one is green-by-accident right after a render. Both halves are specced
  and both are observed.
- **testing + left-shift gates** — the drift criterion runs on the bar from this unit's landing; the
  CRLF criterion is observed against `check-wiring.sh` in both `--check` and `--fix`.
- **migration / rollback** — additive.
- **user docs** — the Skill IS the doc; the protocol remains the binding source it summarises.

## 6. Acceptance criteria

- **AC1** — Hand-editing the rendered Skill makes `adopt-unattended.sh --check` red, naming the file
  and printing the diff; re-rendering clears it. Both states observed.
- **AC2** — With the rendered Skill absent, `--check` reds naming it rather than passing over a file
  that is not there. Observed.
- **AC3** — A CRLF copy of the rendered Skill is reported by `bash tools/check-wiring.sh --check`
  and byte-rewritten by `--fix`, and the eol population it belongs to is NON-EMPTY. The population
  assertion is the load-bearing half: a pin that never took would leave the file out of the
  population and the arm would report ok over nothing. Both states and the population observed.
- **AC4** — The rendered Skill contains this repo's declared keepalive tool calls and lander, not the
  template's placeholders. Asserted by grep in both directions: the values present, no `{{`-shaped
  placeholder surviving.
- **AC5** — `bash tools/run-gates.sh` runs `adopt-unattended.sh --check` as a leg, and the charter
  cites it by path.

## 7. Gates

The standing bar. Newly relevant: `tools/check-wiring.test.sh` (the eol arm's population now
includes this render), the run-gates canary, and the codebase-map coverage gate, whose
`rendered-skills` inventory reds until the dossier claims the new key.

**Build-wide constraint this unit inherits:** `non_terminal_specs_cited_by_product_source` measures
2 against a pin of 2, zero headroom.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 5 of seven. Carries the review's obligation that the
  `.gitattributes` pin is the whole of the `check-wiring.sh` work because that script's population is
  derived, and that drift and CRLF each get their own criterion. Adds one thing the master README's
  row did not: the fourth gate leg, so this unit's drift criterion is enforced at its own landing
  rather than waiting for unit 7's adopter work.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged. All five criteria observed directly, not
  inferred: drift reds at exit 1 and re-rendering clears it; an absent render reds rather than
  passing; a CRLF copy is reported by `check-wiring.sh --check` and rewritten by `--fix` with zero
  CRLF pairs left, over a population the same run reports as non-empty; and the render carries this
  repo's declared values with no `{{`-shaped placeholder surviving.

  One check was added beyond the spec, because rendering exposed the gap: a SURVIVING placeholder is
  its own refusal. A conf that declares nothing for a key renders a Skill telling the agent to call
  `{{KEEPALIVE_CREATE}}` — perfectly in sync with the template, and useless. Template parity and
  placeholder completeness are different questions and the second one had no answer.

  Found while wiring, and repaired: this node's `merge.rows.driver` pointed at
  `tools/memory-tree/merge-rows.sh`, which does not exist — only the `.py` and its test do. So
  `check-wiring.sh --check` exited 1, which would have made `--preflight` refuse on this very repo.
  The probe was right and `--fix` had correctly declined to overwrite a value someone might have set
  deliberately. Repointed at `bash tools/lib/pyrun.sh tools/memory-tree/merge-rows.py`. This is
  machine state, not repo content, so it travels with no commit and the next node must run
  `check-wiring.sh --fix` itself.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "render a project skill from a kit template and check it
for drift"` ranks the two existing adopters first, which is the answer: this is the third instance
of a kind that already has a shape, and the decision is to copy the shape rather than improve on it.

- `tools/drift-audit/adopt-drift-audit.sh` — the render/`--check` structure, the temp-file diff, the
  capped output and the fix line, followed deliberately rather than re-invented.
- `tools/memory-recall/adopt-memory-recall.sh` — the second instance of the same shape; between them
  they are what makes this a pattern rather than a precedent.
- `tools/check-wiring.sh` Check E — the DERIVED eol population, joined by adding a pin and nothing
  else.
- `.gitattributes` — the two existing rendered-skill pins, whose recorded reason is reused verbatim.
- `.unattended.conf` — the render's variable source, so no project value is written into the kit.
