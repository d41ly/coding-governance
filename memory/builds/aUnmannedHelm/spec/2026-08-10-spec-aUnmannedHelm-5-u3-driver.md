# TOOL-aUnmannedHelm-5 — the driver, and the four verbs it is allowed to have

**Status:** INPROGRESS · rev-2 · 2026-08-10 · node a · Tier-2 · base 09b9bd1c · streams tooling · ratified 2026-08-10 · review wf_077104e6

## 1. Goal

Give the protocol an executable surface: one script, four verbs, every one of them checkable. This
is unit 3 of seven; the master scope and the ratified decision menu live in this build's `README.md`.
Unit 2 declared what the run must be able to assert; this unit is the thing that asserts it.

The design constraint that shapes every verb is negative. The review found two verbs claiming
effects they cannot produce and one delegating to a repairing mode, and the fix in each case was to
make the driver do LESS: record instead of schedule, check instead of fix, assert instead of write.

## 2. Scope (IN)

- **S1 · `--preflight`.** Refuses on a dirty tree, on the default branch, on an unwired repo, and on
  an absent or unreachable mandate. On success it pins the BASE, records the keepalive id the agent
  hands it, renders the generated region, and moves the phase out of its initial value.
- **S2 · the mandate assertion.** The mandate must already exist in the run-state file AT THE PINNED
  BASE, byte-identical to the working copy's. That single comparison enforces both properties the
  review demanded — the run did not author it, and it is reachable from the BASE — without a second
  mechanism for each.
- **S3 · `--status`.** One line: the phase, its witness, and the first non-terminal unit.
- **S4 · `--resume`.** Re-enters from the run-state file and prints what `--status` prints, plus the
  next action. The two must agree; a resume that disagrees with status is two answers to one
  question.
- **S5 · `--close`.** Evaluates the DoD set from the declarations, blocks on any unmet item, and
  records a named override as a parked entry. Agent-attested items are labelled and never counted
  against the override budget.
- **S6 · the generated region, by COPY not by re-derivation.** See §4.
- **S7 · the sibling test**, arming every refusal branch positively.

## 3. Non-goals (OUT)

- **Scheduling or reaping the keepalive.** Unreachable from a script; the protocol assigns both to
  the agent.
- **Repairing wiring.** `--preflight` delegates to the declared non-repairing check.
- **Writing the mandate.** Ever, under any flag. A `--scaffold` that emitted a fillable mandate would
  not defeat the reachability property, but it would put the shape in reach of the run, and the
  cheapest way to keep a hole closed is to not build the door.
- **The gate leg.** Unit 4 runs over the tree; this unit runs over one build.
- **Deriving unit status.** `gen_build_index.py` already does, and the memory-tree gate already
  byte-compares its output.
- **Any agent-cap edit.** `TOOL-aNumeralWarden-1`'s.

## 4. Design

### The generated region is a COPY, and that is the whole trick

The region must carry the unit list and per-unit status. Both are already derived, by
`gen_build_index.py`, into the build README's own generated block — and the memory-tree gate already
byte-compares that block against a fresh render, so its freshness is somebody else's solved problem.

So the driver does not derive anything. It EXTRACTS the README's generated slice and SPLICES it into
the run-state file between the run-state file's own marker pair. One derivation in the tree, one
copy, and unit 4's leg asserts the copy equals the source. A second derivation path would be the
two-answers class in the file this build exists to institutionalise.

This also removes what would otherwise be a cross-kit dependency: the driver never calls a script
inside `tools/memory-tree/`, which matters because each kit is copy-installed standalone and an
adopter may hold one and not the other. It reads a FILE, at a path the conf declares.

The splice obeys the same contract as the source: exactly one open marker, exactly one close, close
after open, replace the slice, never a whole-file regex.

### The mandate assertion, in one comparison

```
git show <BASE>:<run-state path>   →  extract the mandate block  →  compare with the working copy's
```

- Absent at BASE → refuse. The mandate was introduced after the branch point, which is the
  self-authored case.
- Present but different → refuse. The run edited its own authorization.
- Identical → accept.

No separate reachability check and no separate provenance check, because at a pinned merge-base
those are the same question. The BASE is pinned by `--preflight` itself and written to the authored
region, so every later verb re-runs the identical comparison against a value it cannot quietly move
(unit 4's leg re-derives the merge-base and reds if the recorded BASE disagrees).

### The authored region's shape

Marker-delimited, key-per-line, deliberately dull:

```
<!-- run:authored -->
## Mandate
<!-- run:mandate -->
   … the owner's block, verbatim …
<!-- /run:mandate -->

## Run facts
phase: RUNNING
witness: <sha | tag | run id>
base: <40-hex>
keepalive: <id the agent handed --preflight>

## Parked
… question · options seen · why the run refused …
<!-- /run:authored -->
```

No row leads with a dash-and-id, per unit 1's anchor ban. `phase`, `witness`, `base` and `keepalive`
are one key per line so a grep is the parser and no verb needs a second one.

### The refusals, and why each is its own branch

Every precondition gets a distinct message naming itself, because a shared exit code is not a
diagnosis and this script runs where nobody is watching:

| Refusal | Why it is checked before anything is written |
|---|---|
| not a git repo / no conf | nothing below can be resolved |
| dirty tree | the BASE would pin a state that is not what runs |
| on the default branch | the run's own commits would land unreviewed on the branch it means to merge INTO |
| wiring check fails | a dormant hook makes every later green meaningless |
| no run-state file at BASE | the mandate cannot be reachable if the file is not |
| mandate absent / differs | the two provenance properties, in one comparison |
| keepalive id not supplied | the agent's half of the split was skipped, and only the agent can do it |
| a second non-terminal run-state file | "the run" would not be well-defined |

`--preflight` writes NOTHING until every one of them passes.

### Files touched

New: `tools/unattended/unattended.sh`, `tools/unattended/unattended.test.sh`. Edited: none — the
gate leg, its manifest entries and the charter's gate-suite citation are unit 4's.

### Alternatives rejected

- **Re-deriving the unit table in the driver.** Two derivations of one fact, in the build whose
  thesis is that the derived half never rots.
- **Calling `gen_build_index.py` directly.** Couples two independently installable kits and hardcodes
  one repo's install prefix.
- **A `--scaffold` verb that writes a mandate skeleton.** See §3.
- **One `--check` verb with sub-flags.** Four verbs with four exit meanings is what `--status` and
  `--resume` having to AGREE is built on.

## 5. Production-readiness checklist

- **security** — this unit adds the only write path in the kit. It writes exactly two regions of one
  file, at a path derived from the declared memory root and a slug argument; the slug is validated
  against the same grammar hygiene check 4 enforces, so a traversal argument is a refusal, not a
  write. No other file is touched by any verb.
- **perf / scale** — four git invocations and one file rewrite. Nothing measurable.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — every refusal names itself; an empty declaration set is a
  refusal, not a pass.
- **observability** — `--status` is the observable, and `--resume` must reproduce it.
- **risks** — the dominant one is a verb writing before a precondition is evaluated, which is why
  the order is stated as a contract and armed. Second: the copy of the generated region going stale
  against its source, which unit 4's leg compares.
- **testing + left-shift gates** — a positive arm per refusal branch, plus the write-nothing-on-
  refusal arm, which is the one a message-only test would miss.
- **migration / rollback** — additive; the script is new and nothing calls it yet.
- **user docs** — the protocol document already describes the four verbs; this unit implements them
  and adds no second description.

## 6. Acceptance criteria

- **AC1** — On a dirty tree, on the default branch, and with the wiring check failing, `--preflight`
  refuses, names the failed precondition, and the run-state file is UNCHANGED on disk. All three
  refusals and the no-write property observed.
- **AC2** — With no run-state file at the pinned BASE, `--preflight` refuses naming reachability.
  With the mandate present at BASE but edited in the working copy, it refuses naming the difference.
  With them identical, it proceeds. All three observed.
- **AC3** — With no keepalive id supplied, `--preflight` refuses naming the agent's half of the
  split. With one supplied, it is recorded verbatim in the authored region and readable by
  `--status`. Both observed.
- **AC4** — After a successful `--preflight`, the run-state file's generated region is byte-identical
  to the build README's generated slice, and the authored region carries the BASE that
  `git merge-base` reproduces. Both observed.
- **AC5** — `--status` prints one line naming the phase, its witness and the first non-terminal
  unit; `--resume` prints the same phase, witness and unit. Divergence reds. Both observed.
- **AC6** — `--close` with an unmet machine-checked item blocks and names it. With `--override
  <item> --reason <text>` it proceeds AND a parked entry appears in the authored region carrying the
  reason. With an unmet AGENT-ATTESTED item it blocks and labels it agent-attested, and overriding
  it writes the parked entry without counting against the override budget. All observed.
- **AC7** — A slug argument that is not a legal build-folder name is refused and writes nothing.
  Observed with a traversal argument.

## 7. Gates

The standing bar. Newly relevant: the kit self-test as its own leg (unit 4 registers it), the
python-launcher resolver ban (this script uses no python, asserted by grep so the ban cannot be
satisfied vacuously), the LF discipline on a new `.sh`, and `check-arms.py`, which discovers this
script as a gate the moment it defines `fail() {` and calls `fail <n> "` — so either it uses that
helper and gets a sibling test with a positive arm per branch, or it deliberately does not and says
why here. It DOES use it, and the sibling test is `unattended.test.sh`.

**Build-wide constraint this unit inherits:** `non_terminal_specs_cited_by_product_source` measures
2 against a pin of 2, zero headroom. No file under `tools/` may cite this build's ids while the
owning sub-spec is non-terminal.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 3 of seven. Carries the three obligations the Tier-2
  review pinned on this unit — assert the mandate rather than write it, record the keepalive rather
  than schedule it, delegate to the non-repairing wiring check — and adds the design that removes the
  cross-kit dependency they would otherwise have needed: the generated region is a COPY of the build
  README's already-verified slice, not a second derivation.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged. 26 refusal branches, all 26 armed by a
  positive assertion naming their own text; 44 assertions in the sibling test; `ARMS_FLOORS` gains
  `26:26`. `check-arms.py` discovered the driver on its own the moment it defined the `fail` helper,
  which is the design working rather than a surprise.

  Four things were found by building rather than by specifying, each one a defect in the first cut:

  1. **A merge-base fallback would have voided the whole unit.** `--preflight` originally fell back
     to HEAD when the merge-base could not be resolved. HEAD holds whatever the run just wrote, so
     the mandate comparison would have passed BY CONSTRUCTION — the one hole this kit exists to
     close, open with every gate green. It is now a named refusal.
  2. **`set_fact` dropped silently** when the file carried neither the key nor a heading to put it
     under, so preflight could report success over a file holding none of the facts it claimed to
     record. Now its own refusal.
  3. **A positional in a refusal message cannot be armed.** `check-arms.py` treats `${?[A-Za-z_]…`
     as an interpolation and a bare `$1` as literal text, so `$1` lands IN the signature and no
     assertion can name it. Measured on two branches. Every message now leads with its literal and
     trails its values, and positionals are bound to names first — which also reads better.
  4. **Every fixture that edits a file must COMMIT it.** Preflight evaluates all preconditions
     before writing, so a dirty fixture still arms the message branches — but it never reaches the
     write phase, where checks 9 and 17 live. Those three arms silently exercised the dirty-tree
     branch instead until the fixture committed.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a driver that asserts preconditions then splices a
generated region into a state file"` returns no affordance seam for the verb dispatch. The seams
this unit wires through rather than reinvents:

- `tools/memory-tree/gen_build_index.py` `apply_region()` — the splice contract, obeyed exactly:
  one open marker, one close, close after open, replace the slice, never a whole-file regex.
- The build README's generated block — the SOURCE of the copied region, whose freshness the
  memory-tree gate's check 9 already owns.
- `.unattended.conf` — every project-specific value, read and never restated.
- `tools/check-wiring.sh --check` — the non-repairing probe, invoked through the `WIRING_CHECK`
  declaration rather than by path.
- `tools/memory-tree/check-memory-hygiene.sh` check 4's folder grammar — the slug validation, so a
  traversal argument is refused by the same rule that would have refused the folder.
- `fail() {` plus `fail <n> "` — this repo's gate-script convention, which is also what makes
  `check-arms.py` discover the script and demand an armed sibling test.
