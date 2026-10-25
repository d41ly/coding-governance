**Serves:** research TOOL-dGroundRules-30

# Divergence brief — TOOL-dGroundRules-30, a fallback no old hook admits

## The prompt

> Its builder probed TOOL-dGroundRules-30 at HEAD b8b4f0815 and handed it back as a DIVERGENCE before writing anything. It ran the `node <hook> --only=scripts` predicate `tools/workflows/check-verifier-fanout.sh` delegates to over scratch renders of `tools/workflows/unattended-build.js`. The writer split passes the HEAD hook (exit 0) and is refused by the HEAD hook with `WRITER_MARK` staged to another string (AC1's clone): "agent() fanned over `specGroups`, which this file does not show to be bounded". The fallback §3 hands to TOOL-dGroundRules-25 S18, `Math.ceil(slices.length / Math.min(SPEC_WRITERS, 5))) // gov:fixed-verifiers`, is refused by the HEAD hook, the staged hook and the base 3c2b69be hook: "carries gov:fixed-verifiers but its bounded split names a cap which this file does not show to be bounded". A literal `5` in the split passes the HEAD hook but the base hook still refuses it, because `boundedParallel(thunks, cap = 6)` and `SPEC_WRITERS` resolving to 6 at its call site exceed `MAX_VERIFIERS`. So no one-line fallback passes an old hook, and AC1's `Math.min(` cannot survive. Stale citations: `tools/hooks/agent-cap.js:104` (the constant is now at :85); `check-protocol-parity.test.sh:529-545` (now :532-557); the S18 floor S2 deletes sits at :559-575 as the spec expects.

## The brief

### Goal
Revise `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-30.md` to the run's ruling: this unit owns the fallback shape, and the fallback renders the verifier-shaped split every hook admits. Author only: no product code, no commit, no gate.

### Items
1. S3 (and any §2 item that renders the fallback): below the writer-split version the render substitutes the whole verifier-bounded shape, not one line: `SPEC_WRITERS` and the `boundedParallel` cap at the call site both rendered at the hook's `MAX_VERIFIERS` (5) as literals the hook can read, and the split line carrying `gov:fixed-verifiers` over that bound. The shape is derived from the template's own writer split by substitution, so no second copy of the template is authored.
2. §3 takes the fallback shape back from TOOL-dGroundRules-25 S18 into this unit's scope, naming S18's floor in `tools/workflows/check-protocol-parity.test.sh` as the line S2 replaces; the hands-off edge to TOOL-dGroundRules-25 is reworded to match.
3. AC1 drops `Math.min(` and expects the rendered fallback to carry `gov:fixed-verifiers` with the bound 5 and to pass the hook predicate at both the base 3c2b69be hook and the HEAD hook; a criterion or the `New arm:` line observes that a render whose cap exceeds 5 is refused by the base hook.
4. Re-cite `KIT_AGENT_CAP_VERSION` in `tools/hooks/agent-cap.js` by symbol and `check-protocol-parity.test.sh`'s ranges by their current lines or by symbol.
5. The status header's rev rises by one, with a §9 line naming the disagreement and the ruling. Keep the file under 48600 bytes measured with its records region; every §6 code span stays on one line; introduce no retirement word in §2; no path inside a code span is followed by a quote or other punctuation.

### Acceptance
`python tools/check-spec-tokens.py` exits 0 with this spec read as INPROGRESS (the main loop runs it); every `**Carries:**`/`**Derived:**` line, the H1 and the §8 RESOLVED marks survive; every §6 code span sits on one line.

### Gates
No gate runs in this pass.

### Non-goals
Any other spec; product code; the status cell, which stays `DEFERRED`.

### Limitations
The builder's hook probes stand; its scratch renders are in the session scratchpad.

### Reuse
The writer split TOOL-dGroundRules-18 built is the template the substitution reads.
