# The acceptance ledger — what each closed unit's criteria were answered by

**Serves:** journal TOOL-dUnstalledConvoy-11 PLAY-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-1 TOOL-dUnstalledConvoy-2 TOOL-dUnstalledConvoy-3 TOOL-dUnstalledConvoy-4 TOOL-dUnstalledConvoy-5 TOOL-dUnstalledConvoy-6 TOOL-dUnstalledConvoy-7 TOOL-dUnstalledConvoy-8 TOOL-dUnstalledConvoy-9 TOOL-dUnstalledConvoy-10

The back-fill `TOOL-dUnstalledConvoy-11` S8 owes. The cutoff is this build's own date, so this build's
units are inside the population its own check creates — which is the point: a gate whose first run
measures an empty set is an assertion about nothing.

Every line is OBSERVED or AMENDED. Where a criterion could not be taken at its own unit's close, the
line says so rather than implying it was.

**Evidences:** PLAY-dUnstalledConvoy-1
- AC1 — `grep` — returns nothing in the template and nothing in `AGENTS.md`; the refuted clause is gone from both live carriers.
- AC2 — `coding-governance-agents.template.md` — the surviving bullet keeps the tool-call enforcement and states the no-fan-out-tool reason in its place.
- AC3 — `PreToolUse` — read back: the new text says nothing about a hook failing to fire, which stays recorded as unmeasured.
- AC4 — `bash tools/playbook/adopt-playbook.sh --target . --check` — exit 0, so `AGENTS.md` is the render and not a hand edit.
- AC5 — `bash tools/check-template-size.sh` — 48378 of 49152, and the commit message carries it.
- AC6 — `memory/backlog/TOOL.md` — `TOOL-dUnstalledConvoy-16` opened, naming the carrier-set class rather than the instance.
- AC7 — `bash tools/check-line-length.sh` — 0 over 450; the single-bullet form measured 560 and was split for exactly this.
- AC8 — `memory/archive/` — three version snapshots still carry the sentence and were not edited; frozen records of what those versions said.

**Evidences:** TOOL-dUnstalledConvoy-4
- AC1 — `grep` — the park instruction is gone from M3 in both carriers.
- AC2 — `Act` — M2 names AMEND with its three forms and states that an id may not leave the roster.
- AC3 — `bash tools/memory-tree/check-method-carriers.sh` — green, template and render agree.
- AC4 — `wc -l` — 288 of M1's 290 at this unit's commit, and the figure is in the message.
- AC5 — `python tools/memory-tree/corpus_ids.py --report` — read path under the ceiling after the edit.
- AC6 — `memory/guides/BUILD-METHOD.md` — read back: the four acts and the one refusal are answerable from M2 and M3 alone.
- AC7 — `grep` — M3 states both bounds, the goal invariant and the veto-2 carve-out.
- AC8 — `grep` — vetoes 1 and 3 unchanged; M12's second spelling of the rule is gone.
- AC9 — `wc -l` — 289 of 290, taken AFTER unit 8 landed. NOT takeable at this unit's own close, which is why the audit moved it here from unit 8; the line says so rather than implying otherwise.

**Evidences:** TOOL-dUnstalledConvoy-5
- AC1 — `tools/unattended/unattended.test.sh` — one row appended, kind token `rescope`.
- AC2 — `tools/unattended/unattended.test.sh` — the repeat reports unchanged and adds no row.
- AC3 — `tools/unattended/unattended.test.sh` — `--act sideways` refuses, naming the value and the three members.
- AC4 — `tools/unattended/unattended.test.sh` — supersede without a successor refuses; add WITH one refuses.
- AC5 — `tools/unattended/unattended.test.sh` — retiring an id absent from the region refuses, naming it.
- AC6 — `tools/unattended/unattended.test.sh` — adding an id already in the region refuses when no row explains it.
- AC7 — `tools/unattended/unattended.test.sh` — the bypass flag refuses from either field.
- AC8 — `refuse_if_terminal` — a finished record refuses the verb.
- AC9 — `bash tools/unattended/check-unattended.sh` — green; each refusal exercised by hand against the live record before the arms existed.
- AC10 — `tools/unattended/unattended.test.sh` — the no-op and the refusal are separated by whether a matching row exists.
- AC11 — `grep` — `--rescope` present in the rendered Skill and in the protocol's verb list.
- AC12 — `bash tools/unattended/adopt-unattended.sh --target . --check` — in sync.
- AC13 — `python tools/memory-tree/corpus_ids.py --report` — 106595 of 112987 after the protocol edit.
- AC14 — `grep` — the verb's header states what it cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-6
- AC1 — `tools/unattended/check-unattended.test.sh` — an unaccounted added id reds, naming it.
- AC2 — `tools/unattended/check-unattended.test.sh` — an `add` row accounts for it.
- AC3 — `tools/unattended/check-unattended.test.sh` — a `WONTDO` flip with no row reds, naming both acts.
- AC4 — `tools/unattended/check-unattended.test.sh` — a supersede whose successor is absent reds.
- AC5 — `tools/unattended/check-unattended.test.sh` — an unreadable baseline prints a named skip and does not red.
- AC6 — `check_authorization` — a removed id is not reported here; the driver still refuses it.
- AC7 — `ARMS_FLOORS` — every refusal and skip exercised; arms count matches the call sites.
- AC8 — `tools/unattended/check-unattended.test.sh` — a full supersession passes end to end.
- AC9 — `tools/unattended/check-unattended.test.sh` — a spec authored during `SPECCING` does not red.
- AC10 — `tools/unattended/check-unattended.test.sh` — the default channel still prints nothing; the green controls hold.
- AC11 — `grep` — the check's header states what it cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-7
- AC1 — `grep` — exactly one verdict-token line, reading `parallelism route: cleared`.
- AC2 — `git log --oneline` — the losing conditions are one commit EARLIER than the results.
- AC3 — `git status --porcelain` — E3 cites git and the per-path diff, never a pass's self-report.
- AC4 — `tools/memory-tree/merge-rows.py` — E4 states the driver was never reached, and the control reproduces the conflict when it is.
- AC5 — `memory/builds/dUnstalledConvoy/build/` — every criterion recorded CLEARED, FAILED or NOT OBSERVED; none passed on an argument.
- AC6 — `memory/HYGIENE.md` — the record carries its binding line and the filename projects the lowest id served.

**Evidences:** TOOL-dUnstalledConvoy-9
- AC1 — `tools/unattended/unattended.test.sh` — one row, carrying the group sha and the unit id.
- AC2 — `tools/unattended/unattended.test.sh` — an intersecting sibling refuses, naming both passes and the path.
- AC3 — `tools/unattended/unattended.test.sh` — a disjoint sibling is accepted.
- AC4 — `tools/unattended/unattended.test.sh` — the run-state file, the decision log and a backlog shard each refuse.
- AC5 — `tools/unattended/unattended.test.sh` — absolute, `..`, empty and whitespace-bearing paths each refuse.
- AC6 — `tools/unattended/unattended.test.sh` — identical no-ops, a superset widens, a narrowing refuses.
- AC7 — `tools/unattended/unattended.test.sh` — the declared key is read: a fixture with different names refuses about THOSE paths.
- AC8 — `tools/unattended/unattended.test.sh` — every refusal observed RED against a fixture.
- AC9 — `tools/unattended/unattended.test.sh` — a generated index ALONE is accepted; only the pairing with its generator refuses.
- AC10 — `tools/unattended/unattended.test.sh` — a whitespace-bearing path refuses, which the repeatable flag is what makes expressible.
- AC11 — `bash tools/unattended/adopt-unattended.sh --target . --check` — `--dispatch` present in the Skill render and the protocol verb list.
- AC12 — `grep` — the key appears in the project conf, the shipped example and the protocol's key table, asserted separately.
- AC13 — `grep` — the verb's header states what it cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-8
- AC1 — `grep` — the new framing sentence is present and the old one is gone.
- AC2 — `git show` — the three conditions are byte-identical to BASE, compared as CONTENT with newlines stripped, because they are not a numbered list and any correct edit changes their first line.
- AC3 — `bash tools/memory-tree/check-method-carriers.sh` — green, both carriers agree.
- AC4 — `wc -l` — 289 of 290 after both method-editing units; one line of the two available.
- AC5 — `.claude/skills/unattended/SKILL.md` — the directive cell was found INACCURATE, not accidentally right: it called M6 a `default` and M6 no longer has one. Corrected to name the obligation.
- AC6 — `parallelism route: cleared` — vacuous by construction, and stated as such: the measurement cleared, so the non-shipping branch never fired.

**Evidences:** TOOL-dUnstalledConvoy-10
- AC1 — `tools/unattended/check-unattended.test.sh` — a pass committing inside its declared set is clean.
- AC2 — `tools/unattended/check-unattended.test.sh` — a path outside it reds, naming the pass and the path.
- AC3 — `tools/unattended/check-unattended.test.sh` — an empty outcome announces; a declared path moving with no naming commit reds.
- AC4 — `tools/unattended/check-unattended.test.sh` — one commit naming two passes of a group reds on ambiguous attribution.
- AC5 — `tools/unattended/check-unattended.test.sh` — an unresolvable group anchor announces a skip.
- AC6 — `tools/unattended/check-unattended.test.sh` — declaring three paths and committing one passes.
- AC7 — `bash tools/unattended/check-unattended.sh` — the no-dispatch-rows skip prints on this repo and the default run stays silent.
- AC8 — `tools/unattended/check-unattended.test.sh` — every refusal observed RED against a fixture.
- AC9 — `tools/unattended/check-unattended.test.sh` — a later commit naming the same unit passes; it is outside the group by construction.
- AC10 — `grep` — the check's header states what it cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-3
- AC1 — `bash tools/unattended/check-unattended.sh` — check 10 green; the shipped protocol and the installed copy agree.
- AC2 — `memory/guides/UNATTENDED-PROTOCOL.md` — section 6 states the remote arm is attempted first, and argues the ordering rather than listing it.
- AC3 — `memory/guides/UNATTENDED-PROTOCOL.md` — section 9 names the `update-ref` lever explicitly.
- AC4 — `LANDED_ANCHOR_CUTOFF` — present in the shipped example and the protocol's key table. Filed by unit 2, which owns the reader; this unit's S3 was DELETED for claiming the same carriers.
- AC5 — `python tools/memory-tree/corpus_ids.py --report` — 109209 of 112987, in the commit message.
- AC6 — `bash tools/unattended/adopt-unattended.sh --target . --check` — in sync. AMENDED at rev-2: the first draft named `check-wiring.sh`, which does not compare this pair at all.
- AC7 — `grep` — section 3 names both anchors and the recorded anchor-kind fact.
- AC8 — `grep` — the Skill's landing section names the fallback, both facts and the pointer to section 9.

**Evidences:** TOOL-dUnstalledConvoy-1
- AC1 — `bash tools/unattended/unattended.sh --landed <slug>` — the remote arm behaves as before and records `remote`.
- AC2 — `tools/unattended/unattended.test.sh` — a run merged into local main but absent from the remote reaches `LANDED` with `local`.
- AC3 — `tools/unattended/unattended.test.sh` — neither anchor refuses, and the message names both tests.
- AC4 — `tools/unattended/unattended.test.sh` — the unpushed count carries a figure and the oldest sha.
- AC5 — `unpushed-at-landing` — an unresolvable branch records `unknown`, never `0`.
- AC6 — `bash tools/unattended/check-unattended.sh` — green across the change; both new arms observed RED with the fixture standing ON the default branch.
- AC7 — `tools/unattended/unattended.test.sh` — an unmerged branch tip is refused by arm 2; this is the arm's real failing case and the first draft had none.
- AC8 — `grep` — the verb's header states what the local anchor cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-2
- AC1 — `tools/unattended/check-unattended.test.sh` — a `remote` record off the advertised tip reds with the original message.
- AC2 — `tools/unattended/check-unattended.test.sh` — a `local` record on the local default branch passes, where it previously red.
- AC3 — `tools/unattended/check-unattended.test.sh` — AMENDED at rev-3. The drafted refusal for a witness on neither branch became an announced SKIP: a run-state file travels and a local ref does not, so another clone cannot judge a local-anchored claim. The arm asserts the skip.
- AC4 — `tools/unattended/check-unattended.test.sh` — an anchor kind outside the closed set reds, naming the value and the set.
- AC5 — `tools/unattended/check-unattended.test.sh` — an absent kind reds at or after the cutoff and passes before it.
- AC6 — `bash tools/unattended/check-unattended.sh` — the announced skip prints on the report channel and the leg exits 0.
- AC7 — `grep` — the key appears in the project conf, the shipped example and the protocol's key table.
- AC8 — `tools/unattended/check-unattended.test.sh` — an omitted key runs to a normal verdict; a blank one behaves as the shipped date.
- AC9 — `tools/unattended/check-unattended.test.sh` — the branch NAME resolves from the advertisement, and the node-scope skip prints rather than redding.
- AC10 — `grep` — the check's header states what it cannot buy.

**Evidences:** TOOL-dUnstalledConvoy-11
- AC1 — `memory/HYGIENE.md` — the `Acceptance ledger` sub-section is present, states the two forms, and its template is byte-identical.
- AC2 — `memory/TEMPLATE-SPEC.md` — section 6 points at the grammar in one sentence and does not restate it.
- AC3 — `ACCEPTANCE_LEDGER_CUTOFF` — declared with a comment stating what moving it either way costs.
- AC4 — `bash tools/memory-tree/check-memory-hygiene.sh` — green over the corpus with the documentation landed and before the check was armed.
- AC5 — `bash tools/check-kit-versions.sh` — green without this unit bumping anything; the bump belongs to the later unit of the pair.
- AC6 — `tools/memory-tree/check-memory-hygiene.sh` — the example in the sub-section parses under this file's own parser, read back once the check landed.
- AC7 — `python` — every unit closed before this one carries a block, verified mechanically: 103 criteria, no gaps and no extras.

**Evidences:** TOOL-dUnstalledConvoy-12
- AC1 — `tools/memory-tree/check-memory-hygiene.test.sh` — a fully evidenced closed spec passes.
- AC2 — `tools/memory-tree/check-memory-hygiene.test.sh` — a missing criterion reds, naming the unit and the label.
- AC3 — `tools/memory-tree/check-memory-hygiene.test.sh` — a line in neither form reds, naming both legal forms.
- AC4 — `tools/memory-tree/check-memory-hygiene.test.sh` — a Tier-2 spec numbering no criterion reds.
- AC5 — `tools/memory-tree/check-memory-hygiene.test.sh` — a `WONTDO` spec with no ledger passes.
- AC6 — `tools/memory-tree/check-memory-hygiene.test.sh` — a spec dated before the cutoff is excluded.
- AC7 — `bash tools/memory-tree/check-memory-hygiene.sh` — run against this repo, the check measures this build's own back-filled units rather than an empty set; it fired on real gaps before they were filled.
- AC8 — `tools/memory-tree/check-memory-hygiene.test.sh` — each refusal observed RED against a fixture.
- AC9 — `tools/memory-tree/check-memory-hygiene.test.sh` — a CLOSED Tier-1 spec whose section 6 is Gates passes, which is why the heading is located by TEXT.
- AC10 — `grep` — the kit README's check count and its delegation breakdown updated, and the dossier agrees.
- AC11 — `bash tools/check-kit-versions.sh` — green with the kit-version bump carried by this unit as the last commit of the pair.
- AC12 — `grep` — the check's header states what it cannot buy.
