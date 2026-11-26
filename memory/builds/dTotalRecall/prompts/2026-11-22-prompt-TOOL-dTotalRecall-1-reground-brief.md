**Serves:** journal TOOL-dTotalRecall-1

# Brief — dTotalRecall: TOOL-dTotalRecall-1 re-grounded on the tree as built, before dispatch

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run. The spec run wrote every spec DEFERRED at base `462d20f3`; 4140
commits (DERIVED, `git log --oneline 462d20f3..8b8b1374c | wc -l`) have landed since, the three parent builds
dDeclaredLoop, dWitnessedBar and dPlacedRequest among them, so each spec is re-grounded before its dispatch.

## The brief

### Goal

Revise the spec named here in place, as a rev bump with one revision-log line naming this brief by its file stem,
so a builder can build it as written over HEAD. Where every claim already holds, change nothing and say so.

### Items

1. Read the spec whole against the code at HEAD and settle every claim the landed code has moved: every path,
   symbol, line citation, section name, count, population and edge, and every parent spec it leans on (the
   PLAY-dOrderedCharter, TOOL-dWitnessedBar, TOOL-dPlacedRequest, TOOL-dSafePassage and TOOL-dDeclaredLoop ids it
   cites): read what each parent actually landed, not what its spec planned. Re-derive each PINNED count with the
   command the spec states and re-pin it with today's date. A population the spec enumerates is re-derived, every
   new member listed in Files touched with the legs its guard names on the gates section's leg line. Cite moved
   code-file lines as `path#symbol` or blob-pinned at a commit HEAD holds, never a bare `path:line`; leave a
   carried clause token (`**Carries:**` lines) byte-identical.
   What is built so far: nothing of this build; this unit is build order 1 and builds alone.
2. Trace behaviour, not only text: (a) run or read each acceptance criterion's command for its real exit codes and
   output; (b) grep every caller of a function the unit changes and every suite that copies the files it touches;
   (c) check each new rule against the fallback its reader takes on an invalid or absent file; (d) where the spec
   names a seam (a factory, a ledger, a leg row, a class row), confirm the seam exists at HEAD with the shape the
   spec uses, and re-point the spec where a parent landed it differently.
3. Settle the 87 unwaived spec-token hits the build-wide sweep found where they name this spec (`python
   tools/check-spec-tokens.py --spec <path>` lists them), each by naming the tripped leg on the gates section's leg
   line or by correcting Files touched.
4. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. A fork whose only survivor needs a new
   external dependency or a governance-carrier change is parked, not decided: name it in your return.
5. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. A spec over its ceiling of 49152 B (PINNED 2026-11-20 by the spec size check) is tightened
   in prose you touch, never by dropping a criterion. Name every new function the spec introduces with a verb from
   `.lexicon.conf`'s VERBS table, nested helpers included.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-1` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-1. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-1.md` alone. Temporary files go under the
scratch directory the task names. Do not commit: the main loop commits the re-ground.

### Reuse

The spec's §10 seam, re-verified at HEAD.
