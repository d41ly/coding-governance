# The owner's prompt, verbatim

**Serves:** research TOOL-aClosedDocket-1 TOOL-aClosedDocket-2 TOOL-aClosedDocket-3

Handed to `/unattended` as the `--prompt` value on 2026-08-31, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. Recorded here rather than in the build README for the three reasons that file's own heading
canon, byte ceilings and marker matcher impose.

```text
build TOOL-aProvenReuse-3 -4 and -6 per the protocol.
```

## How this run read it

Three backlog rows, named by id, to be built. "Per the protocol" is `memory/guides/UNATTENDED-PROTOCOL.md`
and the build method it points at — the ordinary discipline, not a special instruction.

**The instruction is also the veto-2 owner turn for unit 1**, and that reading is load-bearing rather
than convenient. `TOOL-aProvenReuse-3` names `memory/guides/BUILD-METHOD.md` M4 as the carrier to
change, and M3 veto 2 puts a change to a governance carrier outside what a standing mandate
delegates. An unattended run cannot grant itself that turn. Naming the row by id in the instruction
is the owner taking it — for the row as written, and no wider.

## The rows this build drains

| row | what it says is wrong |
|---|---|
| `TOOL-aProvenReuse-3` | M4 promotes standing blockers to units at a NON-CONVERGENT exit, which has no legal referent when the review subject is a SPEC: M2 forbids a unit that is not a mechanism, and the promoted unit's own spec would then owe an audit |
| `TOOL-aProvenReuse-4` | `tools/codebase-map/reuse_lookup.py` writes no log, so of M5's two probes only the recall half leaves evidence and `reuse-probed` is blind to the other |
| `TOOL-aProvenReuse-6` | the unattended suite's bounded-observation arms assert on the HARNESS's wall clock around a whole verb, which includes work the bound does not govern; measured at 35 s, 44 s and 66 s against a 25 s assertion under cross-session load, and clean on an unloaded run |

## The orientation probes this run ran before writing the roster

Per the Skill's prompt path step 1, both were run before this build folder existed.

```bash
python tools/codebase-map/reuse_lookup.py "recording a telemetry log line when a lookup tool runs so a later check can observe it"
python tools/memory-recall/query.py "how should a non-convergent review loop dispose of blockers when the subject is a spec, and how is a wall-clock timing assertion made robust" \
  --terms "non-convergent review loop blocker promotion spec subject mechanism unit disposition wall-clock timing assertion flake elapsed bound contention"
```

What they changed. The recall probe surfaced two prior NON-CONVERGENT exits that unit 1 must not
contradict: `aScouredKit` PROMOTED three units, and `aBoundedVerdict` promoted none because its
standing set was empty after the fold. So the rule is right for those shapes and unit 1 must ADD a
case rather than replace one. It also surfaced `TOOL-dHonouredPark-8`, which reports that `--review`
keys convergence on `--subject` alone — the reason this fleet's spec audits and diff reviews collide
when both name the slug, and a constraint unit 1 sits next to without touching. The map probe
returned no logging seam in `codebase-map` at all, which is the finding `-4` already records and the
evidence that unit 2 builds rather than extends.
