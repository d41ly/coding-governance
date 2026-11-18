**Serves:** research TOOL-dDeclaredLoop-18

# Brief: revise spec TOOL-dDeclaredLoop-18 after its builder's divergence

## The prompt

> /unattended dDeclaredLoop

— owner, 2026-11-13. The build run's first dispatch, TOOL-dDeclaredLoop-18 at order 1, came back as a divergence: the builder
stopped before its code because six claims of the spec at rev-3 do not hold against the code at `cb34ba603`. The return is
`memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md` in place, as a rev-4 bump with one revision-log
line naming the builder return, so a builder can build it as written over HEAD.

### Items

1. Settle each of the return's six numbered divergences against the code at HEAD, reading the code it cites yourself: the
   `purpose-source` each of the four namespace rows carries; the extractor's real row contract and which readers take a `family`
   kind; the Non-goal against `check_resolves` and AC6; the signal for a policy key a catalogue family row matches; the two
   dossier spans in `memory/map/features/policy.md`; and the printed text AC1, AC2 and AC3 quote.
2. Settle the return's smaller points too: how the `policy-family` plant reaches a copied kit, and the write set's missing
   `tools/playbook/adopt-playbook.sh`.
3. Keep the unit one mechanism, its clause and node carries, its order and its status header's `INPROGRESS` unchanged. A
   divergence that needs a mechanism this unit's scope does not name is a fork with options and a recommendation, never a silent
   widening; the run takes recommendations under its mandate.
4. Write only that spec file. Do not commit and do not regenerate any index.
5. Run `check-spec-tokens.py --spec` over the revised spec and fix every hit it names.

### Acceptance

- Every claim the revised spec makes about current code is one you read at HEAD, and each of the six divergences is answered by a
  changed section the revision-log line names.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.

### Limitations

- The spec format is `memory/TEMPLATE-SPEC.md`. Temporary files go under the scratchpad the dispatch names.

### Reuse

- The seams are the ones the builder return cites: `tools/playbook/tag_index.py`, `tools/playbook/gov_tag.py`,
  `tools/playbook/policy_value.py`, `tools/playbook/namespaces.toml` and `tools/policy/catalogue.toml`.
