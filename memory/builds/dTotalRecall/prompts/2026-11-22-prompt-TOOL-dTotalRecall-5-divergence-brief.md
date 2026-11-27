**Serves:** journal TOOL-dTotalRecall-5

# Brief — dTotalRecall: TOOL-dTotalRecall-5's first build pass diverged; fold the spec

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The unit's first builder returned a DIVERGENCE at base `44c6800aa`
before writing anything, recorded whole in
`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-5-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-5.md` in place as a rev bump, with one
revision-log line naming this brief and the builder return by their file stems, so the next builder can build it as
written.

### Items

1. Read the builder return whole. Settle its three findings:
   (1) §6 AC12, its Red-when and §8 F10 contradict §4 "The grammar" and S13: §4's word `[A-Z][a-z0-9]*` admits the
   one-word slug `dX`, so the bound class matches `TOOL-dX-2`, and the same shape widens `grammar_for().ID_RE`'s
   session era unstated. Decide between the return's (a) a word of `[A-Z][a-z0-9]+` and (b) dropping the refusal and
   stating the widening, by the build method's M3, marked RESOLVED in §8; the return measured that every build
   folder, every flip slug and every id `read_bindings` reads at HEAD fits (a).
   (2) §4 "The readers" says runlog and branch-reconcile reach the grammar through their `resolve_kit_dir` copies;
   neither `tools/runlog/runlog_lib.py` nor `tools/branch-reconcile/` holds one. State that this pass adds the
   canonical block to both, say whether those copies join the `resolve_kit_dir` row of
   `tools/lib/resolve-python.test.sh#PARITY_ROWS`, correct S8's row count, and put each file in Files touched.
   (3) §4's census command does not reproduce its pinned figures on this node; spell its backslash-d arm bracketed,
   as the return found, and re-pin every figure it stands on with the command that now reproduces it.
2. Keep every other rev-8 claim unless a finding forces it; name any forced change in the revision-log line.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-5`,
`python tools/check-spec-tokens.py --spec <path>` and `bash tools/memory-tree/check-memory-hygiene.sh --only 12 --spec
<path>`, and fix every finding they name. The status header keeps `INPROGRESS`; the write grant is the spec file
alone; do not commit.

### Acceptance

Every command exits 0; the spec carries its next rev and one revision-log line naming this brief and the return.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec but unit 5's. No product code. No change to Goal or Scope intent beyond what the findings force.
