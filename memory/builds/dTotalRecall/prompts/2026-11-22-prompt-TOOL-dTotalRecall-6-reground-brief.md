**Serves:** journal TOOL-dTotalRecall-6

# Brief — dTotalRecall: TOOL-dTotalRecall-6 re-grounded on the tree as built, before dispatch

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
   What is built so far: TOOL-dTotalRecall-1 (order 1) and -13 (order 2) are CLOSED: the record-kind registry
   `tools/memory-tree/record-kinds.toml` with `record_kinds.py` (leg `record-kinds`), and the `extract_code` block.
   TOOL-dTotalRecall-18 (order 4) is CLOSED at `305b6e9d1`: every registry column required, `record_kinds.py new`'s
   `--layer`, `--lifecycle`, `--reader` and `--readers-none`, `tree_lib.py#KIND_ALIASES` and `#resolve_kind` (the
   `journal` kind renamed `log`, read through the alias). TOOL-dTotalRecall-8 and -37 are DEFERRED to owner ask
   TOOL-dTotalRecall-109 (no code record; a memory-tree reader reads policy through `tree_lib.py#read_policy_value`),
   and no live spec consumes from unit 8. TOOL-dTotalRecall-16 (order 5) builds now; re-grounded, not yet built:
   TOOL-dTotalRecall-25 rev-6 (order 6), -5 rev-7 (order 7: `derive_slug_grammar`, `SlugGrammar.render_label`, an ERE
   export, and `tree_lib.py#build_id_token_re`'s slug class bound to the grammar), and -38 rev-5, -4 rev-5 and -54
   rev-3 (order 8: `parse_id_parts` on `build_id_token_re`'s named groups, its arm in `tools/memory-recall/selftest.py`).
   Read each built unit's code at HEAD and each unbuilt one's spec where this spec consumes from it. This unit is build
   order 9, beside its order-9 siblings, each re-grounded in its own spec.
2. Trace behaviour, not only text: (a) run or read each acceptance criterion's command for its real exit codes and
   output; (b) grep every caller of a function the unit changes and every suite that copies the files it touches;
   (c) check each new rule against the fallback its reader takes on an invalid or absent file; (d) where the spec
   names a seam (a factory, a ledger, a leg row, a class row), confirm the seam exists at HEAD with the shape the
   spec uses, and re-point the spec where a parent landed it differently.
3. Settle every unwaived spec-token hit that names this spec (`python
   tools/check-spec-tokens.py --spec <path>` lists them), each by naming the tripped leg on the gates section's leg
   line or by correcting Files touched.
4. A choice the re-ground forces that the spec cannot derive is a fork: decide it by the build method's M3, mark it
   RESOLVED in §8 with the delegated mark, and name it in your return. A fork whose only survivor needs a new
   external dependency or a governance-carrier change is parked, not decided: name it in your return.
5. A `[[ledger]]` home spelled under `tools/<kit>/` reds `install-prefix (shipped surface)`; keep every home under
   `memory/project/`. A spec over its ceiling of 49152 B (PINNED 2026-11-20 by the spec size check) is tightened
   in prose you touch, never by dropping a criterion. Name every new function the spec introduces with a verb from
   `.lexicon.conf`'s VERBS table, nested helpers included. A new leg's `ceiling` clears its evidenced maximum by max(120 s, 1.0x) (PINNED 2026-11-22)
   (`memory/builds/dTotalRecall/build/2026-11-22-build-TOOL-dTotalRecall-1-deviation-15.md`), and a new surface
   class needs its `[[class]]` row in `tools/govkit/usage.toml`; every number the spec states carries an id, a
   path:line, PINNED or DERIVED on its line (`python tools/playbook/writing_practice.py check pinned-facts`).

6. A `consumes-from` edge to an unbuilt sibling needs that sibling's matching `hands-off`, or hygiene check 12 refuses both. Where the sibling's spec (DEFERRED, not CLOSED) lacks it, add that one bullet to the sibling's edges as a rev bump with a revision-log line naming this brief; that sibling spec joins your write grant for that bullet alone. A CLOSED sibling stays frozen: state the dependency in Scope and name it in your return.

Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-6` and
`python tools/check-spec-tokens.py --spec <path>` over the spec, and fix every finding either names. Write no
numeric fact without an id, a path:line, PINNED or DERIVED on its line.

### Acceptance

Both commands exit 0 for the spec; it carries the next rev and one revision-log line naming this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No spec outside TOOL-dTotalRecall-6. No product code. No change to Goal or Scope intent beyond what the tree forces.

### Limitations

The status header keeps its status (`DEFERRED`). The write grant is
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-6.md` alone. Temporary files go under the
scratch directory the task names. Do not commit: the main loop commits the re-ground.

### Reuse

The spec's §10 seam, re-verified at HEAD.
