# TOOL-aUnmannedHelm-4 — the protocol document, and the authorization it rests on

**Status:** CLOSED · rev-3 · 2026-08-10 · node a · Tier-2 · base 1005e696 · streams tooling+playbook · ratified 2026-08-10 · review wf_077104e6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-10-review-TOOL-aUnmannedHelm-1-2.md](../reviews/2026-08-10-review-TOOL-aUnmannedHelm-1-2.md) | diff-review | TOOL-aUnmannedHelm-1 TOOL-aUnmannedHelm-5 TOOL-aUnmannedHelm-6 TOOL-aUnmannedHelm-7 TOOL-aUnmannedHelm-8 TOOL-aUnmannedHelm-9 |

<!-- /gen:spec-records -->

## 1. Goal

Turn the block of chat the owner retypes to launch an unattended run into a committed document with
an enforceable shape. This is unit 2 of seven; the master scope and the ratified decision menu live
in this build's `README.md`. Units 3 and 4 consume every declaration made here — the phase
vocabulary, the Definition-of-Done set, the mandate grammar — so this unit is specced before them.

Unit 1 gave the run a legal place to write state. This unit says what goes in it, who may authorize
the run, and what the run must be able to assert before it stops.

## 2. Scope (IN)

- **S1 · the protocol document, as a kit/dogfood pair.** `tools/unattended/PROTOCOL.template.md` is
  what an adopter installs; `memory/guides/UNATTENDED-PROTOCOL.md` is this repo's own installed copy
  and is charter-cited, so it enters the read-path budget visibly. The pair is byte-compared modulo
  the install prefix.
- **S2 · the phase vocabulary, kit-owned core plus project extensions.** A closed set that is
  deliberately NOT the seven-token slot vocabulary, with its terminal members named. Per F3 the
  project layer may EXTEND it and may not delete a core member.
- **S3 · the DoD assertion set, same shape.** Six kit-owned core items, each stating who checks it —
  machine or agent-attested. F4's blocking `--close` buys its safety from a named item, a mandatory
  reason and a parked entry, so a deletable core item would be a silent, reason-free override.
- **S4 · the keepalive, split by actor.** Per B3 the protocol owns scheduling and reaping as AGENT
  obligations naming the tool calls; the driver only records the id and asserts a recorded reap. The
  cron store is in-memory and session-scoped, reachable only through the agent's own tool calls.
- **S5 · the landing step.** `bash tools/push-main.sh` by name, never `--no-verify`, stated in the
  protocol and in the DoD set. The pre-push hook refuses a default-branch push lacking the lander's
  marker, so an unattended run without this either stalls or learns to bypass the whole bar.
- **S6 · F1's amendment at all FOUR live statements of the explicit-ask rule** — `AGENTS.md`, the
  playbook template's §1 and §8, and `.claude/SESSION-KICKOFF.md` §B — each carrying the in-line
  fallback so a non-adopting repo inherits a rule its merge bar can still make true.
- **S7 · the conditional-section wiring.** Companion §1 is droppable-per-project, keyed on adopting
  the kit, and `parallel-coding-governance.customize.md` says so in the block that already
  enumerates exactly this kind of line.

## 3. Non-goals (OUT)

- **The driver.** Unit 3 writes `tools/unattended/`; this unit writes the document it obeys.
- **Validating any of it.** Unit 4's leg parses the declarations and checks the run-state file
  against them. A document that validates itself is the two-answers class.
- **The rendered skill.** Unit 5.
- **The template version marker and its archive snapshot.** Unit 7, per the master README. This unit
  changes template rules and leaves the marker alone, which is a transient the build closes before
  it lands and is stated here so it is not read as an oversight.
- **Editing `agent-cap.js`, its test, its wired copy, or the review protocol's text.** All
  `TOOL-aNumeralWarden-1`'s after the F2 fold.
- **A second parity ENGINE.** See §4 — the duplication is forced by the standalone-install contract
  and is bounded to one pair.

## 4. Design

### Where the rules live, and why not in the template

The playbook template is under a strict 32 KiB gate with 80 bytes free, and the review already
found the load-bearing objection: F1 loosens a universal-core rule whose only enforcement ships in
an opt-in kit, so a re-pulling adopter would inherit the loosened clause with no run-state file, no
mandate grammar and no leg. A whole new template section for a kit-conditional affordance would
make that worse and cost roughly 620 bytes the gate does not have.

So the template gains no section. It gains exactly F1's two amended lines, each carrying an in-line
fallback that stays true without the kit — the merge bar validates the mandate's shape, and a
project with no such bar has no mandate — plus a pointer to the companion. The companion is not byte
gated, so the checklist lands there in full.

The companion's numbering rule is one-to-one: companion §N extends template §N. The unattended rules
are a work-unit lifecycle concern — how a unit is authorized and how it lands — which is template
§1. The companion therefore gains **§1**, its first new section since the eight it shipped with, and
its header sentence and the customize companion's count move with it.

Recorded correction: the master README calls this "domain-rules §15". Template §15 is Voice and has
been for several versions, and the companion mirrors template numbers, so §15 was unreachable. The
number is §1 on the rule the companion states about itself, not on a preference.

### The phase vocabulary

Kit-owned core, in run order, with the terminal members named:

`PREFLIGHT` · `RUNNING` · `VERIFYING` · `LANDING` · `LANDED` · `ABORTED`

`LANDED` and `ABORTED` are terminal. `LANDING` is the state the slot vocabulary cannot express —
built and reviewed, not yet merged — which is the whole reason unit 1 kept the run-state file out of
check 8. A project may append its own members and may not delete a core one; the leg asserts core
membership against a shrink-only floor, the shape `baseline.toml` and `ARMS_FLOORS` already use.

Every phase claim carries a git-checkable witness — a sha, a tag, or a workflow id — and witness
PRESENCE is its own refusal, separately from witness resolution. The drift oracle counts a claim
with no sha of its own as unjudgeable and skips it, so absence is the cheapest way for a run that
cannot substantiate a phase to say nothing, and the run is the sole author of that field.

### The DoD assertion set

Six kit-owned core items. Each names its checker, because F4's override budget must not be spent on
something no machine could have checked anyway:

| Item | Checked by | What it asserts |
|---|---|---|
| `gates-green` | machine | the project's full merge bar ran on the tip being landed and passed |
| `records-current` | machine | every unit's status header and the build's generated regions match a fresh render |
| `mandate-reachable` | machine | the mandate blob is reachable from the pinned BASE and was not introduced by a commit on the run's own branch |
| `landed-via-lander` | machine | the landing step used the project's declared lander and emitted no bypass flag |
| `keepalive-reaped` | agent-attested | the scheduled keepalive was deleted; the driver can only read back the id it recorded |
| `parked-decisions-surfaced` | agent-attested | every parked entry reaches the wrap-up, so "parked" is distinguishable from "forgotten" |

`--close` blocks on any unmet item. The override is named and recorded and costs a parked entry.
The two agent-attested items do not spend the override budget, because attestation is not a machine
verdict and pretending otherwise is what makes an override look like a check.

### The mandate

A committed block naming the build and both authorized actions. Three properties, all mechanical:

- **It authorizes, it is not authored by the run.** `--preflight` ASSERTS it. A mandate introduced
  by a commit on the run's own branch grants nothing — otherwise the run writes the block that
  authorizes its own merge and push, and the leg certifies it.
- **It is reachable from the pinned BASE.** Reachability is the machine-checkable form of "the owner
  wrote this before the run started".
- **Its SHAPE is checked, never its intent.** No gate can tell whether the owner meant it. The two
  properties above are what make the shape worth checking.

### The keepalive, split by actor

The cron store is in-memory and session-scoped: the job is gone when the agent process exits, and
`delete` removes it from that same store. No script in `tools/unattended/` can reach it. So:

- The PROTOCOL obliges the agent to schedule the keepalive before the run leaves `PREFLIGHT` and to
  reap it before the run reaches a terminal phase, naming the tool calls its own project layer
  declares.
- The DRIVER records the id the agent hands it and asserts a recorded reap. It never schedules and
  never deletes, and it labels the item agent-attested wherever it reports.

The tool names are a PROJECT declaration, not a kit constant: an adopter's harness may expose a
different scheduler, and a kit that hardcodes this repo's spelling is wrong on every other node.

### Files touched

`tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` (new pair);
`parallel-coding-governance.domain-rules.md` (new §1 + the header sentence);
`parallel-coding-governance.template.md` (§1 and §8, two lines);
`parallel-coding-governance.customize.md` (the conditional-sections row and the section count);
`AGENTS.md`; `.claude/SESSION-KICKOFF.md`; `memory/README.md` (the guides row).

Not touched: `agent-cap.js`, its test, its wired copy, the review protocol's text, `gate-legs.json`
(unit 4), `tools/memory-tree/kit-dogfood-parity.test.sh` (see below).

### Why the parity comparison is written twice

Each kit is copy-installed as a standalone directory, so `tools/unattended/` cannot call a script
that ships inside `tools/memory-tree/` — an adopter may install one and not the other, and the
memory-tree parity harness hardcodes its own two pairs. The duplication is therefore forced, and it
is bounded: ONE pair, and the normalisation discipline (strip the install prefix, strip CR) is
copied deliberately rather than re-derived, the same way every kit carries `resolve_python` inline
and byte-identical. Unit 4's leg owns running it.

### Alternatives rejected

- **A new template §18.** Costs ~620 bytes against 80 free, and makes a kit-conditional affordance
  read as universal core — the exact objection the review raised about F1.
- **Companion §15.** Template §15 is Voice; the companion mirrors template numbers.
- **Leaving the amendment to `AGENTS.md` alone.** Two of four sites amended leaves the template
  self-contradictory across §1 and §8 and leaves this repo's own kickoff manifest still forbidding
  the push the run must make.
- **A machine-checked keepalive item.** No script can reach the store. It would be a check that
  cannot fail, spending F4's override budget on nothing.
- **Generalizing the memory-tree parity harness to a pair manifest.** Couples two independently
  installable kits and changes a shipped gate for a reason that has nothing to do with it.

## 5. Production-readiness checklist

- **security** — the mandate is an authorization artifact, so its two hardening properties
  (not-self-authored, reachable-from-BASE) are the security surface and are specced above. No new
  write path here; the document is inert. Unit 3 owns the write guards.
- **perf / scale** — a byte comparison of one pair. No measurable cost against the 239 s bar
  measured at `b476a55` on node a.
- **a11y · i18n** — N/A.
- **error / empty / loading states** — every declaration the leg reads has a defined empty case: an
  empty phase vocabulary and an empty DoD set are refusals, not silent passes.
- **observability** — the protocol is what `--status` explains itself against.
- **risks** — the dominant one is the loosened §1 rule reaching a non-adopting re-puller. The
  in-line fallback and the conditional-sections row are the two answers to it, and both are
  observable. Second: the template byte budget; the amendment is measured against the gate, not
  estimated.
- **testing + left-shift gates** — the amendment parity check is a grep over four named paths, armed
  in both directions. Unit 4 owns the declaration-parsing arms.
- **migration / rollback** — additive except the four amended lines, which revert independently.
- **user docs** — the protocol IS the user doc; `memory/README.md`'s guides row names it.

## 6. Acceptance criteria

- **AC1** — When the un-amended phrasing of the explicit-ask rule survives at any of the four named
  paths, the amendment check reds naming the path; when all four carry the amended phrasing, it is
  green. Both states observed.
- **AC2** — When the shipped protocol and this repo's installed copy differ by anything other than
  the install prefix, the parity comparison reds and prints the diff; re-rendering clears it. Both
  observed.
- **AC3** — `bash tools/check-template-size.sh` is green after the two template edits, and the
  remaining headroom is recorded in the revision log as a measured number read FROM the gate.
- **AC4** — When a core phase member or a core DoD item is deleted from the project declaration, the
  membership assertion reds naming the item; when a project member is ADDED, it is green. Both
  observed. (The assertion ships with unit 4; this unit's obligation is that the core set is
  declared in the kit, in one place, and is machine-readable.)
- **AC5** — The protocol names `bash tools/push-main.sh` as the landing step and no path in it emits
  `--no-verify`. Asserted by grep over the document, both directions: the lander is present, the
  bypass flag is absent.
- **AC6** — `memory/guides/UNATTENDED-PROTOCOL.md` is under check 6's caps and inside the charter's
  read-path ceiling, and the ceiling's remaining headroom is recorded. Observed by running the
  hygiene gate, which owns both.
- **AC7** — The keepalive obligation names the agent as the actor for BOTH scheduling and reaping,
  and the driver's role is stated as record-and-assert. Asserted by grep: the document must not
  claim the driver schedules or deletes.

## 7. Gates

The standing bar, `bash tools/run-gates.sh`. Newly relevant legs: template size, memory hygiene
(checks 6, 7 and 16 all bind the new guide), kit/dogfood parity for the memory-tree twins (untouched
here, asserted as untouched), the kickoff-manifest ratchet — `.claude/SESSION-KICKOFF.md` is itself
amended, so `last-audit` re-stamps with a delta line — and the codebase-map coverage gate, whose
guides inventory reds until a dossier claims the new guide.

Before the review of this unit's diff, run the recurring-bug-class checklist for the diff range.

**Build-wide constraint this unit inherits:** the drift signal
`non_terminal_specs_cited_by_product_source` measures 2 against a pin of 2, with zero headroom. No
file under `tools/`, `skills/`, `.claude/`, the playbook template, its two companions, or
`WIRE-INTO-PROJECT.md` may cite this build's own ids while the owning sub-spec is non-terminal.
Records under `memory/` may.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-10 · initial draft, as unit 2 of seven, carrying the obligations the Tier-2 review
  pinned on it: the keepalive split by actor, the lander named and the bypass flag banned, and a
  kit-owned core DoD set the project layer may only extend. Two placements were decided against the
  master README's wording and the reasons recorded in §4: the companion section is §1, not §15,
  because template §15 is Voice and the companion mirrors template numbers; and the template gains
  no new section at all, because a kit-conditional affordance in universal core is the objection the
  review already raised about F1.
- rev-2 · 2026-08-10 · BUILT on the unit branch, unmerged. Three things landed differently from
  rev-1 and each was decided by measuring rather than by argument.

  **The template budget.** The two amended lines cost 114 bytes against 80 free, measured before
  writing them. Funded by EXTERNALIZING the kickoff-manifest merge exception — a ~490-byte procedure
  that applies only when the project keeps a manifest, which is precisely what the charter says goes
  in a companion — into the new companion §1, leaving a stub pointer behind. Headroom after, read
  FROM the gate: 190 bytes, up from 80. The playbook shed an activity-scoped procedure and gained a
  universal-core clause, which is the right direction for a byte-gated ruleset.

  **AC5 restated.** The protocol is project-agnostic, so it cannot name `bash tools/push-main.sh` —
  the shipped copy would hand every adopter this repo's path. The lander is the `LANDER` declaration
  in `.unattended.conf`, which is where the concrete command lives, and the protocol names the
  declaration and bans the bypass flag. The obligation the review pinned is unchanged and is now
  machine-readable instead of prose-only: the leg reads `LANDER` and `BYPASS_BAN` and greps the close
  path in both directions.

  **The read-path budget moved and was re-measured, not estimated.** The charter now cites the new
  guide, so it entered the read path: 16580 B before, 28788 B after, and `READ_PATH_CEILING` moves
  16580+20480 -> 28788+20480 on the kit's own one-sided rule. A binding doc spending visibly from a
  session's mandatory reading is the point of that check, not a side effect of it.

  Also recorded: the new dossier claims `gate-legs = []` on purpose, with the hole named in its
  §Gaps. Nothing validates the declarations until unit 4 lands, and a claimed key with a stated hole
  is a better record than an unclaimed one.

- rev-3 · 2026-08-10 · LANDED on `main` in the merge commit that closes this build. CLOSED in this tree's vocabulary means built AND landed, which is true from the moment that commit exists; the push publishes it.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a shipped protocol document with a kit-owned core
assertion set a project may extend"` returns no affordance seam for the assertion set. The ranked
hits are `kit_rel` and `owners_of` in `map_lib.py` (both fan-in 3, both about install prefixes, not
about declarations) and, by inventory, `REVIEW-PROTOCOL.md` — which is the right structural
precedent and is reused as one: a binding, charter-cited guide under `memory/guides/`, pointed at by
the charter's gate-suite list, whose authority comes from being cited rather than from being long.

The seams this unit wires through rather than reinvents:

- `memory/guides/REVIEW-PROTOCOL.md` — the shape of a BINDING guide in this tree: charter-cited, in
  `index_set()`, entry-budget exempt, and enforced by a leg rather than by its own prose.
- `tools/memory-tree/kit-dogfood-parity.test.sh` — the normalisation discipline for a kit/dogfood
  pair (strip the install prefix, strip CR, print the diff, offer `--render`), copied deliberately
  and bounded to one pair for the standalone-install reason in §4.
- `parallel-coding-governance.customize.md`'s conditional-sections block — the sanctioned way a
  kit-conditional rule enters the playbook, already carrying four codebase-map lines and a
  memory-recall line in exactly this shape.
- `tools/push-main.sh` and `.githooks/pre-push` — the lander and the marker that makes it mandatory,
  named rather than re-described.
- `tools/drift-audit/drift_report.py`'s judgeability discipline — reused for witness RESOLUTION, and
  deliberately NOT for witness presence, which unit 4 arms separately.
