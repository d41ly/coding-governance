**Serves:** research TOOL-aScoutedSeam-3

# Agent prompt principles — what the reuse measurements generalize to, and how to apply them to a multi-step flow

aScoutedSeam spent a week measuring how agents find reuse seams. It went from 4 of 23 cases to 33 of
35 across a tuned and an untuned set, with no change of model. Almost all of the gain came from how
each agent's question was structured and how one step's output reached the next. Effort and the model
contributed little. This document states those findings as principles for any agent step in any flow,
and gives a procedure for applying them to a flow being designed.

Each principle is marked:
- **MEASURED** means a controlled arm in this build moved a blind-judged figure.
- **TRANSFER** means the principle is inferred for task kinds this build did not measure, which is
  everything except finding reuse seams. Treat a TRANSFER principle as a hypothesis to measure in your
  own flow.

## 1. The evidence in one table

| change | figure (blind judge unless marked) | record |
|---|---|---|
| open question → per-unit coverage prompt, same model and effort (`medium`) | 7 → 14 of 23 (path matcher 4 → 14) | `-1-10-d1v2-trial.md`, `-1-12` |
| the same coverage prompt, `medium` → `low` | 14 → 8 of 23, misleading 8% → 18% | `-1-12-judge-and-low.md` |
| the open question at `extra` effort vs the coverage prompt at `medium` | 11 vs 14 of 23 (path matcher 7 vs 14) | `-1-12` |
| diff check given the previous step's binding seams as checklist rows | 13 → 20 of 23 | `-3-1-system-and-held-out.md` |
| a needs-then-sketch checklist scout vs a plain or checklist scout | 16 vs 13 of 24 (path matcher) | `-1-7-m1c-trial.md` |
| the scout also drafts code and expands every cited file | 0 of 6 misses found | `-1-9-m1d-trial.md` |
| six more general rules added to the coverage prompt (T2) | tie, 31 vs 31 of 35, slightly noisier | `-3-1` |
| the two-step system on 12 cases no prompt was tuned on | 12 of 12 | `-3-1` |

Every row is one run, judged once per case. A gap of 6 or 7 cases is real, and a gap of 1 or 2 is noise.
The prompt texts are reproducible from `-1-10-d1v2.py` (`render_question`) and `-1-13-system.py`
(`render_orient_question`, `WIRING`). `-1-11-prompt-method.md` holds the original recipe.

## 2. The principles

### P1. Ask for coverage, not an answer — MEASURED

If the true answer is "every X that has property P", an open question gets one answer. The agent
stops at its first find, or calls the work clean after looking at what interested it. Effort only
changes how long it looks before stopping. Recast the task as a coverage job: "account for EVERY X,
one verdict each". Then define done as every X having a verdict, not as having found something.

- **Applies to:** reviews, audits, reuse checks, acceptance checks, risk passes, migration checks, test-gap
  checks: anything with a population.
- **Fails when:** the task has no population, such as pure creation. Use P8 there.

### P2. Enumerate the population outside the model — MEASURED (as part of the P1 bundle)

A deterministic lister produces the list of X, and the model is handed it. Coverage then becomes
countable: one row per item, or the step is incomplete. In this build the lister was about 40 lines
of regex over a diff:
- definitions, constants and shell functions;
- CSS properties and rules;
- schema fields and keyed JSON nodes;
- any 4-line-or-longer hunk with no named definition.

- **Applies to:** whatever is countable: a diff's units, a spec's scope items and acceptance criteria, gate
  legs, files touched, findings handed in, endpoints, fields, pages.
- **How:** cap the list (60 here), followed by "… and N more; cover them as you read". When the list is
  empty, say "enumerate them yourself from <source>". Never skip the step.

### P3. A row contract: fixed fields, closed verdicts, an escape verdict, proof of search — MEASURED (bundle)

Each listed item gets one row, in order, with fixed fields:
- **The verdict** comes from a closed set with stated meanings, such as `duplicate`, `should-extend`, `new`
  and `not-a-unit`.
- **One verdict is an escape for lister noise.** A bad list item then costs a row, not a false finding.
- **A negative must show its work.** `nearest: none` must come with what was searched, and the
  search must go by concept and synonyms across all file types, not by name.

Without a contract like this, the agent can quietly drop the items it found uninteresting.

### P4. Name the failure mode in the prompt — MEASURED (bundle)

State the known failure, and define done in terms of the list: "Do not stop at the first duplicate. A
review that leaves a listed unit without a row is incomplete." Put it after the rows and before the
output contract.

### P5. Keep the open search, and label it — MEASURED (bundle)

No lister sees everything. After the rows, ask for `added: true` rows aimed at the lister's
known blind spots, named concretely:
- repeated literals;
- hardcoded values beside an existing token;
- renamed copies;
- rebuilt nodes.

The label keeps judgement apart from coverage.

### P6. Derive strength from the verdict; never let the agent choose it separately — MEASURED (precision)

Set the binding mechanically from the verdict: MUST = `duplicate`, SHOULD = `should-extend`. Then add
these on top:
- a hard cap of 5 MUSTs;
- a MUST definition stated as a consequence: "writing new code instead of this would be a defect a
  reviewer should reject";
- a list of the commonest false positives, named as excluded: "files the build merely edits are not
  seams".

The coverage prompt raised volume from 34 to 130 seams, and the blind judge called about 8% of them
misleading. A free-choice binding at `low` reached 18%.

### P7. Feed each step's commitments to the next step as checkable rows — MEASURED (the largest gain)

When step N commits to something, step N+1 must receive it as rows, not prose:
- **What N commits to:** a seam to reuse, a criterion to meet, a constraint to honour, a finding to fix.
- **The row step N+1 answers:** `{item, verdict used|bypassed|not-applicable, why}`.
- **The bad verdict feeds the main output.** A `bypassed` row is also reported in step N+1's main
  findings, so nothing downstream needs a second reader.

This turns step N+1's hardest task from search ("is there an X?") into verification ("was X used?"),
and verification is far more reliable. Here, handing the diff check the orientation scout's MUST seams
took it from 13 to 20 of 23 with nothing else changed.

In a multi-step flow, every edge between steps should be a set of rows like these.

### P8. When nothing can be listed, make the agent build its own population first — MEASURED

A creation step has no diff. Its prompt asks the agent to write the population out before it works on
it:
1. **The needs:** 3 to 10, including implied ones. An image property implies choosing or uploading media.
2. **A concrete sketch:** 6 to 15 components a builder would have to write.
3. **The anchors:** resolve every named page or feature to the code that implements it today.
4. **A census:** where the work is a new instance of a kind, open 5 or more siblings and bind the
   majority convention, returning `<choice>: <majority> (<n> of <m>)`.
5. **The search:** search each sketched item by concept.
6. **Self-refutation:** try to knock down each candidate.

The sketch is the key step. "Add a plan card" cannot be searched for. "A card with an image, a heading
and a price formatter" breaks into three things that can.

### P9. Structure needs `medium`; effort does not substitute for structure — MEASURED

- **At `low`, the same structured prompt** made the agent list more and find less: 8 against 14 cases,
  with the most misleading output.
- **At `extra`, the open prompt** got 11 (path matcher 7), against 14 for the structured prompt at `medium`.

Fix the structure first, then use the lowest effort that holds it. In this build that was `medium`.
Measure before setting a step to `low`.

### P10. More rules and more reading are not more finding — MEASURED

- **More rules:** six well-motivated general rules added to the coverage prompt (T2) tied it and added
  noise.
- **More reading:** a scout that drafted the code and expanded every cited file found none of the six
  cases it had been missing.

Add a rule only when a measured miss class needs it, and check that the rule reaches that class. The
leftover misses here were visual conventions in a package over a host core. Neither variant reached
them.

### P11. Bound every output — MEASURED (it held across all arms)

Cap every list in the output:
- input lists, with an overflow line;
- seams (at most 12) and MUSTs (at most 5);
- constraints (at most 5);
- `why` fields, one line each.

An unbounded step costs more and grows noisier, and the noise lands on the next step's reader.

### P12. Fix the agent in time and scope — MEASURED (benchmark validity)

State the boundaries:
- read-only;
- only the trees named;
- no git history;
- no other checkouts.

In a benchmark, an agent that can see the future finds the answer in a later commit. In production, it
reaches for code that does not exist yet.

### P13. The machine contract goes last, as one fenced block, parsed tolerantly — MEASURED (instrument)

End the prompt with: "End your reply with ONE ```json block holding …". Name every key there, along
with how each key is derived from the rows.

The parser takes the last fence. If an agent quotes three backticks inside a JSON string, the parser
falls back to decoding one JSON value from that fence (`extract_reply` in `-1-13-system.py`). Count the
replies that failed to parse before reading any score.

## 3. The prompt skeleton

The blocks always run in this order: stakes, material, work, then contract.

```
1. ROLE + JOB KIND     "You are the <role> for <moment>. Your job is a COVERAGE job: account for
                        EVERY <X>, one verdict per <X>, so that <named failure> cannot happen."
                        Plus one line overriding any conflicting default in the role body.
2. MATERIAL            the trees, the diff or spec or request, and a reading order ("read the stat first").
3. BOUNDARIES          read-only · only these trees · no history · no other checkouts.
4. THE POPULATION      a deterministic list of <X> (P2), capped with an overflow line; or, with no
                        lister, the needs-then-sketch steps that make the agent produce it (P8).
5. UPSTREAM ROWS       each commitment of the previous step, to be answered used|bypassed|not-applicable,
                        with a bypassed commitment reported as a finding too (P7).
6. ROW CONTRACT        per <X>, in order: id · evidence-of-search · verdict from a closed set with an
                        escape · one-line why (P3).
7. ADDED ROWS          named hunts for what the list cannot see, marked `added: true` (P5).
8. NO-STOP LINE        the named failure, and "incomplete" defined against the list (P4).
9. RETURN CONTRACT     one ```json block: rows, the findings derived from the rows with strength set
                        by the verdict, the upstream rows, and the overall verdict (P6, P13).
```

## 4. Applying this to a multi-step flow

Work through the flow's own steps and roles in this order.

1. **Inventory every agent call.** For each one, record:
   - the step and role;
   - the input it receives;
   - the output it returns;
   - the step that reads that output;
   - its effort level.
2. **Classify each call's question.**
   - **Coverage** (every X with P): P1 to P6 apply in full.
   - **Creation** (writing a spec, code or a plan): P8 builds the population, and P7 applies to its inputs.
   - **Pure judgement on one item:** P3's closed verdicts and P13 apply, and P1 does not.
3. **Find a lister for every coverage call.** Deterministic sources are usually already in the repo:
   - a diff's added units (`extract_units` in `-1-10-d1v2.py`);
   - a spec's scope items `S<n>` and criteria `AC<n>`;
   - the gate legs a path set trips (`tools/gate-legs.json` guards);
   - a findings list;
   - the files a spec's §4 says it touches.
4. **Turn every edge into rows.** For each step N → N+1, write down what N commits to, and make N+1's
   prompt carry those commitments as `used|bypassed|not-applicable` rows. In the gov roles flow, for
   example:

   | edge | commitments step N makes | rows step N+1 answers |
   |---|---|---|
   | orient → spec | the `## reuse` MUST seams and the gotchas classes | the spec's §10 cites each seam as extended, or rejected with a reason |
   | spec → build | the S-items and the ACs | one row per S-item and AC: done, deferred or not-applicable, with evidence |
   | build → review | the S-items, the ACs and the `## reuse` MUSTs | one row each: met, missed or bypassed, plus the diff's own units (P2) |
   | review → skeptic | the findings | one row per finding: confirmed, refuted or plausible, with evidence |
   | skeptic → synthesis | the verdicts | one row per verdict, so nothing is dropped or merged silently |

   The orient → spec and build → review edges here are the measured ones. The rest apply the same
   shape and are TRANSFER.
5. **Set the vocabulary and the strengths.** Give each call a closed verdict set with an escape, a
   strength derived from the verdict, and caps.
6. **Measure before rolling out widely** (section 5). Start with the edge where misses cost the most.

## 5. How to measure a prompt change

1. **Collect cases with objective evidence.** Each case needs:
   - a real past failure;
   - proof that it was a failure, such as a later fix commit, a recorded finding or a verified copy;
   - ground truth checked at the parent commit;
   - the input as it was phrased at the time, with the answer not leaked into it.
   
   20 to 30 cases is enough to see a gap of 5 or more.
2. **Freeze a held-out set** of 10 or more cases before tuning, and never edit a prompt after reading
   its results on them. Write every prompt for the general case.
3. **Change one thing per arm:** the prompt, the effort, the lister or the upstream rows. An arm must
   prove it ran: count its parsed replies before reading its score.
4. **Judge blind.** One judge per case sees every arm under a label rotated per case, and grades with a
   fixed rubric (`-1-10-judge-task.md`). Read primary coverage first, then misleading output.
5. **Read the union.** Arms that miss different cases are steps of one system, not rivals.
6. **Budget it.** One arm on 35 cases is 35 agents. Run at most 5 at once. Expect a judge pass to cost about as
   much as an arm.

## 6. Anti-patterns this build hit

- An open "does this have any problems?" question asked of a population.
- Raising effort to fix a structural miss.
- Letting the agent choose MUST or SHOULD apart from its verdict.
- Passing the previous step's output as prose context rather than rows to answer.
- Adding rules without a measured miss class they reach.
- Reading a score without counting unparsed replies, or with a denominator that includes cases the arm
  could not see.
- A long-running agent's hung shell call taken as progress. One sat 42 minutes. Bound agents' wall
  time.

## 7. What is not established

- **One task family.** Only reuse finding was measured. Every principle applied to another kind of
  step is TRANSFER until it is measured there.
- **The P1 to P5 bundle has no ablation.** The lister, the rows, the no-stop line and the contract changed
  together. The upstream rows (P7) and effort (P9) are the cleanly isolated effects.
- **One run, one judge per case,** and judges sometimes stretched the rubric (`-1-12`, `-3-1`).
- **Visual conventions over a host core** stayed unsolved, so the principles here did not reach that class.
