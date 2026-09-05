<!-- gov:kit unattended@1.18 -->
# Unattended runs — the verbs

*This file is the second half of the binding contract; `UNATTENDED-PROTOCOL.md` is the first. Two
legs byte-compare it against the template it ships from. **They compare the two copies to each
other, so a claim FALSE IN BOTH is green** — a parity leg is a copy check, not a truth check, and
only a reader grades a sentence against the code. This file was created by moving section 7 of the
protocol verbatim, and one bullet arrived carrying a sentence the same build then measured false.*

- `--preflight` — asserts the authorization, pins the BASE, CREATES and stages the run-state file,
  records the keepalive id the agent hands it, and accepts `--waive <handle> --reason <text>` where no
  other verb does (`UNATTENDED-PROTOCOL.md` §10). It refuses on a dirty tree, on the default branch, and on an unwired repo. It
  OBSERVES the anchor from the remote rather than reading a local ref, and refuses when the remote
  does not answer or advertises no default branch of its own — failing closed there costs nothing
  real, since a run that cannot reach the remote cannot land on it either. It delegates wiring to the
  project's **check** mode, never the repairing one: that mode rewrites tracked bytes and sets git
  config, and the run's first act must not be the mode whose past over-firing this protocol cites.
- `--phase` — writes a phase and its witness. Without it the vocabulary is decorative: only
  `--preflight` and `--close` ever wrote one, so every member between them entered the file only by
  hand-editing an artifact this kit calls generated.
- `--park` — writes a decision the run REFUSED to take: the question, the options seen, the reason.
  Refused on a terminal record, and with no run-state file: a park minted for a run that never
  started records nothing about a run.
- `--brief` — records WHAT a build pass was handed: the unit, and the hash of a TRACKED brief file,
  through `park()` as a `history` kind. `--status` reads it, grading each unit's LATEST row.
- `--propose` — writes a PROPOSAL: an amendment a run would make to the playbook it is following,
  joined to the step that provoked it. Nothing blocks on it, and it is not an edit: a run that
  rewrites the checklist it is graded by has no rules left. It reuses `--park`'s newline, separator,
  bypass and terminal refusals over the new step field, and its exact-line idempotence — with the
  step inside the identity, so one amendment at two steps is two rows.
- `--attest` — writes one of the two agent-checked Definition-of-Done items, deriving the record key
  so no operator spells one, and REFUSING a machine-checked item by reading its declared checker.
  Before it existed those keys had no writer, and `--abort` — which requires both — was reachable
  only by hand-editing a file this kit calls generated.
- `--record-piece` — writes one leg's verdict for one PIECE into a tracked record joined to that
  piece by content hash. It reuses `--park`'s newline, separator and bypass refusals and its
  exact-line idempotence. The writer takes a records ROOT rather than a slug, and `--records-root`
  reaches it BEFORE the slug and run-state checks — so the attended path calls the same function with
  no run at all, which is what makes it a second CALLER rather than a second implementation. Without
  that flag the verb resolves a slug and requires a run-state file. An earlier revision of this line
  called the verb "unattended-only", which contradicted its own first half and the code.
- `--record-set` — writes one leg's verdict for the WHOLE set of pieces, over an ordered hash list
  naming which pieces it covers. That population is the one a per-piece review structurally cannot
  see, and a verdict not naming its members cannot be re-checked.
- `--plan` — takes its unit SET and its ORDER from the GENERATED units region, which is why its
  "next" and `--status`'s are the same unit by construction rather than by coincidence. It prints
  each unit's id, status and the build method's M2 classification, and names the next one. It
  COMPUTES that vocabulary and does not define it; M2 does. It reads the SPEC FILES for two things
  the region cannot carry: that classification, and the two `NOT A UNIT` conditions, since a file
  with no parseable status header has no rendered row to appear in. A region that is absent OR
  malformed is a named refusal, never a fall-back to the older spec-derived listing. It still joins
  the build README's AUTHORED roster pair against the tracked specs, so a planned unit nobody has
  specced is reported as MISSING — that question cannot be answered from a region rendered out of
  the specs that exist.
- `--status` — one line: the phase, the first non-terminal unit, and the parked counts.
- `--resume` — re-enters the run from the run-state file; must agree with `--status`.
- `--close` — evaluates the DoD set, blocks on any unmet item, records any override. The only writer
  of `LANDING`, and it runs BEFORE the landing it authorises, so it cannot observe one.
- `--landed` — the sole producer of `LANDED`, an OBSERVATION rather than a claim. It accepts a record
  only at `LANDING`, re-observes the anchor, and refuses unless HEAD is an ancestor of the tip the
  remote advertises. Where `LANDER_MARKER` is declared it ALSO refuses unless the marker names HEAD
  exactly — equality, not ancestry, so any commit between the push and this verb is a refusal. It does
  not refuse the default branch: the mandated lander refuses every other one, so landing happens
  exactly where that guard would otherwise fire.
- `--rescope` — records an AMENDMENT to the build's own scope: `--act retire|supersede|add`, the unit
  as `--item`, an optional `--successor`, and a reason. M3 delegates that scope and M2 names the three
  acts; this verb is the record. It RECORDS rather than acts: a row derived from the change it just
  made is a summary, and a check comparing the two confirms the driver instead of
  checking it. Nothing forces the call to precede the edit, so the row is a declaration in shape
  rather than in enforced ordering: the pair catches an amendment made with NO record, never a
  truthful-looking row attached to a different edit.
- `--dispatch` — records the WRITE-SET DECLARATION a concurrent dispatch owes: `--pass <unit-id>`
  and a REPEATABLE `--writes <path>`, one path per occurrence. The build method requires two path
  lists written down before two passes run together, and until this verb nothing read one. It decides
  two of that condition's three clauses — the intersection test, and the shared-record refusal in
  BOTH halves, so a generated index alone is accepted and only the index TOGETHER WITH its generator
  is refused. The third clause is a judgement about meaning and is refused as undecidable rather than
  faked. A re-declaration of a pass still OPEN widens or no-ops; it never narrows. Once that pass has
  COMMITTED, a further declaration of the same unit is a new pass — M6 sanctions several pass kinds
  per unit — recorded as its own row rather than judged against the previous one. The driver
  distinguishes them by OVERLAP: a narrowing is a strict subset and always overlaps, so it stays
  refused; a disjoint set is a new pass. One that PARTLY overlaps is read as
  a narrowing and refused, which is the conservative direction and is stated here rather than
  discovered.
- `--review` — records ONE review round for a subject and reports what the loop is doing:
  `CONVERGING`, `CONVERGED`, `NON-CONVERGENT` or `CEILING`. The round is an append-only `review` line
  in the parked region, a `history` kind, so it never inflates the count of decisions the owner must
  be shown. A round re-arms the loop only if its confirmed-blocker count is STRICTLY smaller than the
  round before. At a TERMINAL exit — `NON-CONVERGENT` or `CEILING` — the round RECORDS which
  disposition the run took, `fold` or `promote`: `--disposition` is REQUIRED there and REFUSED on any
  round that is not one. Both values are legal, because the method admits folding a blocker back into
  the specs it belongs to as readily as promoting it to a unit, and a record naming neither leaves the
  gate inferring one from ids. It refuses a verdict or a disposition outside its closed set, a missing
  subject or count, a terminal exit carrying no disposition, a disposition on a round that is not a
  terminal exit, and a round on a subject whose loop has already ended.
- `--version` — prints the kit's own version and exits, touching no record. It is here because it is
  DECLARED, and a declared verb nobody documents is one nobody uses to answer the question this kit
  cannot answer for them: which build of it they are talking to. It takes no slug and no run, so it
  is the one verb safe to call before a run exists.

- `--abort` — the sole producer of `ABORTED`. It requires a recorded reason, a HALT CODE from the
  effective vocabulary, and both agent-attested items, and no machine item: an aborted run landed
  nothing, so the machine items assert obligations it does not have, while the keepalive is still
  orphaned and the parked decisions still unseen. The code is validated before it is recorded and the
  refusal names the legal set; it is the twelfth authored fact, and it exists because one terminal
  phase said a run stopped and never said why.
