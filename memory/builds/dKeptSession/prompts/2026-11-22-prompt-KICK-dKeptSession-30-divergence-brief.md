**Serves:** research KICK-dKeptSession-30

# Brief — dKeptSession: KICK-dKeptSession-30's divergence, resolved

## The prompt

> /unattended dKeptSession

## The brief

### Goal

KICK-dKeptSession-30's builder (run `wf_8f513fa2-dbf`) stopped before its first edit and returned a DIVERGENCE: S1 to S3
make three shipped texts false that the spec's Files touched does not name, all written by KICK-dKeptSession-14 after
this spec was grounded. `tools/runlog/README.md`'s `context` paragraph names `CONTEXT_WINDOW_TOKENS`, which S3 deletes,
calls the window one pinned constant, and gives `measure_context_fill`'s old return and `derive_context_fill`'s old
signature. `tools/policy/catalogue.toml`'s `context.threshold` summary ends with the runlog kit's pinned window. And the
comment above `skills/session-kickoff/manifest-check.sh#render_context_line`, in its WHAT THIS DOES NOT CHECK part, says
the window is a pinned constant in the runlog kit. Every other code claim in the spec held at the builder's base.
Revise the spec to the main loop's rulings below.

### Items

1. F-texts: resolved by the main loop: all three texts are corrected in this unit, none is left as it is, since each
   becomes false the moment S3 lands. Add a clause, or extend S3, that rewrites each to the derived window, and add each
   path to Files touched tied to that clause.
2. F-knock-on: the catalogue summary is one of the fields `tools/govkit/docs_leg.py#derive_usage_fingerprint` hashes, so
   rewording it moves `context.threshold`'s fingerprint: the `<!-- usage: policy:context.threshold <fp> -->` anchor on
   `help/orientation-card.md` is re-taken from `python tools/govkit/docs_leg.py --fingerprints` at build time,
   `help/reference/policy.md` is re-rendered by the playbook kit's renderer in its `--reference` mode, and the policy
   mirror `.governance/policy.json` is re-written by `python tools/policy/policy.py mirror --write`. Editing
   `manifest-check.sh` moves a path the kickoff manifest watches, so `memory/guides/SESSION-KICKOFF.md`'s `last-audit` is
   re-stamped. List each of these in Files touched, tied to the clause that moves it, and extend a criterion, or add one,
   that observes the three texts corrected, the reference page current against its render, the anchor's fingerprint
   current, and the mirror fresh.
3. F-selftest: the builder notes `tools/runlog/selftest.py#test_extract_context_fill` compares
   `measure_context_fill(...)` directly with a share; under S2's triple it unpacks the first member. Say so where S2 names
   its callers, as an observation.
4. Bump the spec to rev-6, with one revision-log line naming this brief by its file stem. Cite code by `path#symbol`,
   pin every figure with DERIVED or PINNED, write no `[..](..)` link shape outside the generated records table, keep within
   the live-spec size cap, and leave no fork open.

### Acceptance

`bash tools/memory-tree/check-memory-hygiene.sh --only 12,25 --spec <path>`, a plain
`bash tools/memory-tree/check-memory-hygiene.sh --only 2`, `python tools/check-spec-tokens.py --spec <path>`, a PLAIN
`python tools/playbook/writing_practice.py check pinned-facts` and
`bash tools/unattended/unattended.sh --check-specs dKeptSession KICK-dKeptSession-30` report nothing for the spec.

### Gates

The memory hygiene gate (`--only 12,25 --spec`, and `--only 2`), the spec-token checker, the pinned-facts check and the
driver's `--check-specs`; no other.

### Non-goals

No product code, no commit, no index render, and no spec other than KICK-dKeptSession-30's. Read files; edit only the
spec, in the run worktree.
