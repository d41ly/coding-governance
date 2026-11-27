**Serves:** journal TOOL-dTotalRecall-114
**Caused-by:** TOOL-dTotalRecall-100

# Brief — dTotalRecall: TOOL-dTotalRecall-114, the merged bar's reds, specced for one build pass

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Write the spec of TOOL-dTotalRecall-114, a new unit, order 42, Tier-2, at
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-114.md`: one scope item per red of the record below,
each naming the files it edits, the edit and the observation that proves it, so one builder pass repairs them all.

### Items

1. Read `memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-100-close-bar-reds.md` whole: every red but
   the routed-commits one is a scope item of this unit. `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/bar1.log` is that bar's log,
   each red leg's output under its `GATE FAIL` line; read it for the exact sites.
2. Scaffold through the door, `python tools/memory-tree/gov_record.py new spec TOOL-dTotalRecall-114 --tier 2 --order 42`;
   where it writes a file of another date, rename it to the path above and say so. Follow `memory/TEMPLATE-SPEC.md`
   and the shape of `2026-10-26-spec-TOOL-dTotalRecall-92.md`, an earlier batch of this build.
3. Ground each item in source at HEAD. Prefer the smallest edit that repairs the cause. Where a red has a ledger route
   (`python tools/memory-tree/ratchet.py widen <population> --key <k> --reason <text> --unit TOOL-dTotalRecall-114`) and the
   cause is a real need, the item names the route and its keys; where a conversion is a few lines, it converts.
   A `landed-steps` row is appended in that ledger's own grammar. Guards are edited in the kit descriptor or
   `tools/govkit/registry.toml` row that declares the leg, with the manifest re-rendered by its generator.
4. The drafts `fix1.py`, `fix2.py` and `fix3.py` in `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/` ran in a scratch
   clone; take their edits into the spec's §4 where they hold.
5. The layer edges: name the descriptor's optional row for each edge from a core kit to a kit that is none, after the
   rows `tools/memory-tree/kit.toml` already carries; where the read is a hard one, the item makes it optional.
6. Before returning, run `bash tools/unattended/unattended.sh --check-specs dTotalRecall TOOL-dTotalRecall-114`,
   `python tools/check-spec-tokens.py --spec <path>` and `python tools/playbook/positional.py check` over the spec, and
   fix every finding naming it. Every number carries an id, a path:line, PINNED or DERIVED on its line, and no code
   line is cited bare as a file, a colon and a number.

### Acceptance

The commands name no finding of the spec, every red of the record but the routed-commits one is a scope item with an
acceptance criterion, and §3 names the routed-commits red and the landing as out of scope.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

The `d0e02120b` limits red and any history rewrite. The units held on owner asks. A policy key or a bound moved so that a
red passes.

### Limitations

The write grant is the spec file alone; the README's ids line is the main loop's and already names the unit. The status is `OPEN`, rev-1, base `e5b7ee15b`.
Temporary files go under `C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/114/`, spelled absolute. Do not commit. A
command past two minutes runs in the background and is waited for, never polled. An isolated worktree session refuses
an inline command that embeds git: put it in a script file. Run no gate leg: each criterion is a probe the builder can make.

### Reuse

The drafts of item 4, the existing optional rows of the kit descriptors, and the ledgers' own widen door.
