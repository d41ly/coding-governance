**Serves:** research TOOL-dDeclaredLoop-18

# Brief: revise spec TOOL-dDeclaredLoop-18 after its builder's second divergence

## The prompt

> drop spec-audit: from this build's README and from the run's pinned fact; rearm the unattended session and continue

— owner, 2026-11-13. The third dispatch of TOOL-dDeclaredLoop-18 built rev-4 whole and observed AC1 to AC7, then failed AC8
on the live tree and restored its edits. The return is
`memory/builds/dDeclaredLoop/build/2026-11-13-build-TOOL-dDeclaredLoop-18-3-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-18.md` in place, as a rev-5 bump with one revision-log
line naming that return, so the unit lands with the tags leg green over the live tree.

### Items

1. Registering `command`, `item` and `policy` as namespace words makes three tags already defined in other namespaces break
   the namespace-word rule of `derive_tag_fault` and of the lexicon's twin: `kind.command` and `kind.item` in
   `tools/playbook/kinds.toml` and `kit.policy`, the policy kit's descriptor id. Read both rules and every citation of the three
   tags yourself, then state in section 4 how the three stay legal, and widen section 2, Files touched and AC8 to match.
2. The unit's clause names the four words `step`, `item`, `policy` and `command`, and this build's own clause 24 names the
   `item` kind in the kinds register, so weigh a narrowing of the namespace-word rule ahead of renaming rows the chain's design
   names. Whatever you choose, write it as a section 8 fork with its options and your recommendation, and write the spec body
   on the recommendation: the run takes it under its mandate.
3. Settle the return's smaller points: the second sentence of `help/tags.md` that goes stale once `item` is registered, the one
   generated map file the unit moves, and the `bad-ns` plant's count once `step` is in gov's registry.
4. Add one criterion a builder pass can observe without the tags leg: a probe of the changed checks over the live tree that
   prints no shape red, so the collision class is seen before the close.
5. Keep the unit one mechanism, its carries, its order and its `INPROGRESS` status. Write only that spec file. Do not commit
   and do not regenerate any index. Run `check-spec-tokens.py --spec` over the revised spec and fix every hit it names.

### Acceptance

- Every claim the revised spec makes about current code is one you read at HEAD, and the three colliding tags are each named
  with the rule that keeps them legal.

### Gates

- memory hygiene and spec tokens, at the close.

### Non-goals

- No product code, no sibling spec, no new unit.

### Limitations

- The spec format is `memory/TEMPLATE-SPEC.md`. Skip the whole-tree memory hygiene run: the main loop runs it at its commit.

### Reuse

- The seams are the ones both builder returns cite under `tools/playbook/`, with `tools/lexicon/lexicon.py` for the twin rule.
