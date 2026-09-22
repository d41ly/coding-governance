# The owner's prompt, verbatim

**Serves:** research TOOL-aProvenReuse-1 TOOL-aProvenReuse-2

Handed to `/unattended` as the `--prompt` value on 2026-08-31, node `a`. The value carried
whitespace and named no readable file, so by the Skill's own routing table it is the prompt itself
and is taken verbatim. Recorded here rather than in the build README because that file's heading set
is closed and its slots are byte-capped, because its generated-marker matcher reads column 1 and is
blind to fencing, and because a mandate that points at an editable file is not a mandate.

```text
New work session in the unattended kit. One extremely important rule of the kit is that unattended sessions first and foremost review the repo they're working in and try their best to find EXISTING functionality seams to wire into instead of rebuilding/reinventing it. Keep their project consistent and wiring in UNIVERSAL existing functionality is the cornerstone of any unattended session. Coding anything from scratch only happens when no usable existing seams are genuinely found. Sessions must use their own toolkit (codebase map, reuse audit, memory recall, memory tree) to find what's available for reuse at session start.

## Task: ground in this prompt, understand the problem, adversarially review the unattended kit and related tools to find gaps in implementation, design an efficient and flexible solution to the problem across any relevant tools. Build it.
```

## How this run read it

The prompt states a RULE the kit already carries as prose and asks for the gaps in its
implementation. The reading this build acts on: the rule the prompt describes is `reuse-first`, one
of sixteen directive handles, and the gap is that it is the only one whose satisfaction leaves no
observable trace. The task is therefore not to write a new reuse mechanism — the probes, the log and
the spec section all already exist — but to wire the three of them together so the rule can be
observed rather than asserted.

## The orientation probes this run ran before writing the roster

Per the Skill's prompt path step 1, both were run against the live tree before this build folder
existed, not afterwards.

```bash
python tools/codebase-map/reuse_lookup.py "checking that a spec records a reuse audit before code is written"
python tools/memory-recall/query.py "why is the reuse audit obligation in a spec not machine-checked, and what was considered for enforcing it" \
  --terms "reuse-first reuse audit spec section 10 seam recall probe terms directive waiver silent unchecked machine-checked prose"
```

What they returned, and what it changed: the map probe surfaced the `unattended` affordance seam and
`check-memory-hygiene.sh`'s check family, which is where unit 1 lands rather than in a new checker.
The recall probe surfaced `dFramedEntrypoint`'s round-1 finding RECALL-1 — an eight-spec build with
zero recorded recall terms, reproduced by its own skeptic — which is the same defect this build
measures at corpus scale, and `TOOL-dPromptedSeam-1`'s finding that `check-memory-hygiene.sh:744` is
already "the forcing function in as many words". Both results moved the design from *write a reuse
checker* to *extend the one that already reads these files*.
