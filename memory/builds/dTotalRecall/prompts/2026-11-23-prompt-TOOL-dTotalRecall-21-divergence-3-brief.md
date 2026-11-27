**Serves:** journal TOOL-dTotalRecall-21
**Caused-by:** TOOL-dTotalRecall-21

# Brief — dTotalRecall: TOOL-dTotalRecall-21's third build pass diverged; fold the spec to rev-6

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's third builder returned a DIVERGENCE at base `426dd9dbd`,
recorded whole in `memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-21-3-builder-return.md`.

## The brief

### Goal

Revise the spec in place as a rev-6 bump, with one revision-log line naming this brief and that builder return by their
file stems, so the next builder can build it as written over HEAD. This is the third divergence on one edge (recall's
new requirement), so settle the edge's design whole, not one consequence at a time.

### Items

1. Read the builder return whole. Requiring `playbook-render` installs its adopter, which refuses a target carrying
   only the deployer suite's `DEPLOY_FULL` answers (`CI_FILE` derived by a probe that returns nothing, then
   `COMMAND_CATALOG` asked with no value), so AC9's second apply and every `tools/govkit/selftest.py` target that names
   the closure exits 1, and `selftest.py#run` writes no receipt pin on a non-zero exit. Settle it as a §8 fork decided by
   the build method's M3, reading the candidates against the code: (a) every closure-installing target carries
   `playbook-render`'s placeholder answers, reusing or factoring the stubs `tools/govkit/matrix.py#render_deploy_tail`
   derives from the playbook entry's placeholder rows, its seam named in §10; (b) AC9 and those arms state the exit and
   output `playbook-render`'s refusal gives; (c) recall's edge to the tag index re-decided (F3) so recall installs without
   the playbook kit's adopter, with what recall then does where `tag_index.py` is absent stated and given a criterion.
   Whatever survives, every `govkit selftest` arm the change reaches states what it expects, and the pin block still
   writes its receipt pin.
2. Pass 3's draft (`TOOL-dTotalRecall-21-pass3-draft.patch` in the run's scratch) holds the rest of the unit built; keep
   every decision it carries out unless the fork moves it.
3. A §8 resolution mark is exactly `RESOLVED (agent, 2026-11-23, delegated)`: nothing else inside the parentheses (check
   12 strips code spans and refuses the rest); cite the brief after the mark. A fork whose only survivor needs a new
   external dependency or a governance-carrier change is parked, not decided: name it in your return. Cite code as
   `path#symbol` or blob-pinned; every number carries an id, a path:line, PINNED or DERIVED on its line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-21`,
`python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/writing_practice.py check pinned-facts`, and
fix every finding they name in this spec. The status header keeps `INPROGRESS`; the write grant is the spec file alone;
do not commit.

### Acceptance

The three commands exit 0 or read green; the spec carries rev-6 and one revision-log line naming this brief and the
return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-21. No product code.
