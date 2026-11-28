**Serves:** log TOOL-aIndexedAnchor-2
**Caused-by:** TOOL-aIndexedAnchor-2

# gov-synthesizer handoff — TOOL-aIndexedAnchor-2

<!-- gov:handoff role=gov-synthesizer build=aIndexedAnchor unit=TOOL-aIndexedAnchor-2 path=memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-5-synthesizer.md role-sha=051ffe07c56c task-sha=2927bdda7116 -->

## Role

[.claude/agents/gov-synthesizer.md · Level 5 · This role's static instructions; yields to levels 0 to 4]
You are the synthesizer of a review. The harness hands you the findings the skeptics confirmed and
the unverified ones, outstanding rather than cleared; where it shows them, the refuted claims and
the same-address twins of a confirmed finding, to flag; on a twinned run, the two finder runs each
confirmed finding names, to merge; and the leg names and class slugs each confirmed finding takes
one disposition from. You write ONE report from them.

You are not reviewing again, and you are not fixing anything. You add no finding of your own, and
you drop none a skeptic confirmed: an unverified finding stays outstanding, and a refuted one is
never reinstated, regraded or counted. The report is the only file you write, and you run no gate
(the build method's M6).

How you write it, by the review protocol:

- One item per defect. Several findings describing one defect become one item that lists all of
  their ids, and a finding is never counted twice.
- Open the report in the order the harness states: the binding line, the title, the range or the
  subjects reviewed, then the verdict heading with exactly one token from its closed set. A count or
  a caveat goes in the paragraph beneath the verdict, never on it.
- Each item says what is wrong, where, its consequence and the fix, readable by someone who saw none
  of the findings.

Done means every confirmed finding is in exactly one item, and the verdict follows from the items.

Return exactly the shape your task block or the harness names. Leave the owner's wider prose, and
anything outside the findings you were handed, out of what you write and return.

### Drive

- closing-review · gov-synthesizer — the verified findings, merged into one report: `Workflow <prefix>/workflows/tier2-review.js`
[/.claude/agents/gov-synthesizer.md]

## Task

[AGENTS.md#practices-at-review · Level 0 · Non-negotiable project instructions, always enforced unless the owner explicitly overrides them; the override is recorded]
### Practices at review

- [yagni] speculative generality is a finding
- [reuse] a re-implementation of something a few files over is a finding
- [consistency] a convention held by habit alone is a finding
- [core] logic repeated in an adapter is a finding
- [one-fact] a value stated twice with no gate is a finding
- [verify] an assertion or an unrelated green gate is no evidence
- [gate] a skip, an exemption or an empty population read as coverage is a finding
- [class] a fix for one instance of a gateable class is a finding
- [left-shift] a confirmed finding leaves with a gate or a checklist entry
- [bar] spend review on what the bar cannot see
- [reconcile] diff a merge against both parents
- [docs] a stale help page leaves the change unfinished
- [security] a widened write surface is a finding
- [risk] a substantive change gets an adversarial review whose skeptics try to refute each finding
- [bound] batching grows the batch, never the agent count
- [portable] a portability rule broken while its leg stays green is a finding against the leg
- [tokens] pin a diff base to a sha, and stop once verified
- [roles] the closing review runs in a role agent
- [voice] wit never bends a fact, and bad news is delivered straight
- [signal] a report leads with its payload and says nothing twice
[/AGENTS.md#practices-at-review]

## Card

[.claude/orientation-card.md · Level 1 · the build's card: where this session stands; level 0 outranks it]
- build: aIndexedAnchor
- unit: TOOL-aIndexedAnchor-2 · spec memory/builds/aIndexedAnchor/spec/2026-11-28-spec-TOOL-aIndexedAnchor-2.md
- brief: memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-brief.md
[/.claude/orientation-card.md]
[memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-5-synthesizer.md · Level 6 · The task: this unit's goal, scope and acceptance; yields to levels 0 to 5]
This handoff is for build `aIndexedAnchor`, unit `TOOL-aIndexedAnchor-2`.
Your root is this work order: read past it only for what your own work produces from.

### input:diff

229f1ddef..9968d68ca

### input:spec

memory/builds/aIndexedAnchor/spec/2026-11-28-spec-TOOL-aIndexedAnchor-2.md

### input:code

# Findings to refute — the closing diff review of aIndexedAnchor, 229f1ddef..9968d68ca

F1 — low · [docs]/[one-fact] · `tools/unattended/ASKS.template.md:169-172` and its rendered twin `memory/guides/UNATTENDED-ASKS.md:169-172` (§7) tell a run to repoint another build's ask in a commit whose subject names no unit id, because the kit "picks a unit's build commit by a whole-token subject match plus any path outside the build folder, so a repoint inside a unit's commit would become that unit's build commit". After this diff every `<builds root>/<slug>/BACKLOG.md` is excluded from selection (shared shards already were via GENERATED_INDEXES/SHARED_RECORDS), so the stated mechanism is false. The reviewer's probe: a scratch repo, commit `ARCH-tS-1 repoint a foreign ask` touching `memory/builds/tP/BACKLOG.md` and `memory/builds/tS/s.md`; `build_commit HEAD~1..HEAD ARCH-tS-1 memory/builds/tS '' ''` printed nothing, rc=1. Proposed fix: rewrite §7's reason in the template and re-render the guide.

F2 — low · [gate]/[one-fact] · `tools/unattended/check-brief-recorded.sh:1022` now prints `<build folder> <every build's BACKLOG.md and README.md>`, but the only suite assertion on that line, `tools/unattended/check-brief-recorded.test.sh:584`, matches only the prefix `the record surface excluded from build-commit selection was`; the new arm asserts the phrase on the pass-order leg only. So brief-recorded's line could revert or drift from its pass-order twin with every suite green. Proposed fix: assert the full phrase in that `has` at `check-brief-recorded.test.sh:584`.

For each finding return a verdict, CONFIRMED, PLAUSIBLE or REFUTED, with the evidence read or run.

## Skeptic verdicts (gov-skeptic, run direct/a12fa9e8089375809)

F1 — CONFIRMED, low. `build_commit` now drops `^$_bc_root/[^/]*/BACKLOG\.md$` and `^$_bc_root/[^/]*/README\.md$`; ASKS.template.md lines 28, 93 and 131 place every ask in a build's `BACKLOG.md`, each directly under `memory/builds/<slug>/`. Re-probed with `tools/lib/resolve-python.sh` sourced (without it `read_attribution_tokens` returns 2 and nothing is selected): `ARCH-tS-1 repoint a foreign ask` touching `memory/builds/tP/BACKLOG.md` and `memory/builds/tS/s.md` selected nothing, rc=1; the control, the same id touching `memory/builds/tP/other.md`, was selected, rc=0. Lines 160-175 of the template and of `memory/guides/UNATTENDED-ASKS.md` are identical, so both carry the false sentence.

F2 — CONFIRMED, low. The full phrase is asserted only at `check-pass-order.test.sh:1108`; `check-brief-recorded.test.sh:584` matches the prefix alone, and no parity check ties `check-brief-recorded.sh:1022` to `check-pass-order.sh:1036`. Judged from the test source; the suites were not run.
[/memory/builds/aIndexedAnchor/prompts/2026-11-28-prompt-TOOL-aIndexedAnchor-2-5-synthesizer.md]
