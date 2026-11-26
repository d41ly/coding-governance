**Serves:** journal TOOL-dTotalRecall-120 TOOL-dTotalRecall-121
**Caused-by:** TOOL-dTotalRecall-120

# Brief — dTotalRecall: TOOL-dTotalRecall-120's first pass diverged, its spec folded as rev-2, and spec 121 takes two leftovers

## The prompt

> /unattended dTotalRecall

— owner, 2026-11-22, starting this build run, resumed on node a on 2026-11-24 by the owner's handoff.

## The brief

### Goal

Fold the divergence of `memory/builds/dTotalRecall/build/2026-11-25-build-TOOL-dTotalRecall-120-1-builder-return.md` into
`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-120.md` as rev-2, and put two leftovers of earlier
units into `memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-121.md` as rev-2. Each revision-log line
names this brief by its file stem.

### Items

1. Spec 120, §4 "The plant": `legacy_ledger.write_rows(root, reg, {})`, the empty mapping `write_rows` iterates. Verify
   the return's Why over HEAD first; nothing else of the spec moves unless your own read of HEAD finds it false.
2. Spec 121, a scope item for the stale documents of `TOOL-dTotalRecall-115`: the `--feed` paragraph of
   `tools/unattended/VERBS.template.md` and §7 of `tools/unattended/STOPS.template.md` still describe `--feed check`'s
   walk as "up to the newest one", and the VERBS paragraph names `missing`, `extra` and `unread` but omits `duplicate`
   for record events. Read what `TOOL-dTotalRecall-115` built (`19a209739`) and state the true sentence. The rendered
   `memory/guides/UNATTENDED-VERBS.md` and `memory/guides/UNATTENDED-STOPS.md` follow by the kit's adopter. Observed by
   an acceptance criterion a probe can read, and name each template's byte ceiling where one binds.
3. Spec 121, a scope item for a red of `TOOL-dTotalRecall-117`: `python tools/memory-tree/record_causes.py --cause-writers`
   reads RED at HEAD on `tools/memory-tree/build_records.py`, the line of the keyed-call reader that tests
   `ln.startswith("**Serves:** ")`. It READS a Serves line and writes none. Decide between the census marker the red
   names and a shared reader that spells no literal, say why, and give the criterion.
4. Widen 121's Files touched, its gates line and its `New arm:` lines, where an arm is owed, to match items 2 and 3.
5. Re-read spec 121's whole write set against units 115 to 120 as built, and correct a claim they made stale, the floor
   and shell-role counts named as read at the pass.
6. The checks: `python tools/check-spec-tokens.py` over both specs, the positional and pinned-facts checks of
   `tools/playbook/`, each naming no finding of either spec.

### Acceptance

The commands name no finding. Spec 120 states a plant that runs, and spec 121 carries both leftovers with a criterion each.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No product code. No scope beyond the three items.

### Limitations

The write grant is those two specs. Do not commit. Run no gate leg. Scratch goes under
`C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad`.

### Reuse

The draft patch the return names, `u120/draft.patch` in the scratch directory.
