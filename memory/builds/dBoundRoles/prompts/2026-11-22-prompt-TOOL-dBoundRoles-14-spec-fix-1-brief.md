**Serves:** journal TOOL-dBoundRoles-14

# Brief — dBoundRoles: TOOL-dBoundRoles-14 revised over its first builder's divergence

## The prompt

> /unattended dBoundRoles

— owner, 2026-11-22, starting this build run. Unit 14's first builder (run `wf_0b85ec90-051`) stopped before its code
and returned a divergence: four claims of rev-5 no longer hold at HEAD `0b2529ccd`. Its return is
`memory/builds/dBoundRoles/build/2026-11-22-build-TOOL-dBoundRoles-14-1-builder-return.md`.

## The brief

### Goal

Revise `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` to rev-6 so every claim it makes about
current code holds at HEAD, and the next builder can build it as written.

### Items

1. Fold the four divergences the return names, each as the return words it: (1) READ_FAMILIES carries all 25 keys
   READ_KEYS holds at HEAD, `brief:prompt` and the `upstream` family included, the count table at 25, the
   later-family sentence reworded, and R3's must-be-optional checks graded on the native key `parse_read_key` returns;
   (2) eleven role files, `gov-tester` among them, the `role` count 11; (3) the extractor contract at HEAD,
   `fn(ctx, path, text=None)` returning 5-tuples of kind `tag`; (4) a `purpose-source` the purpose arm reads, and
   `source` spelled from `{prefix}/`.
2. Then re-verify every other claim the spec makes about current code against HEAD, reading that code: each cited
   path, line, function, count and behaviour. Re-point each moved citation (the return lists STAGE_KEY_RE, 
   parse_front_matter, check_rule_tags and R3), and re-ground any sentence whose code changed in behaviour.
3. Keep every acceptance criterion observable and passable on a correct build at HEAD; a criterion a fold changes
   keeps its number. Keep the status `INPROGRESS`. One revision-log line names this brief by its file stem and lists
   what changed.
4. `python tools/check-spec-tokens.py --spec <the spec>` and `check-memory-hygiene.sh --only 12 --spec <the spec>`
   exit 0 before you return.

### Acceptance

The spec is rev-6; each of the return's four items is folded where it names; both checks exit 0; the revision-log
line names this brief.

### Gates

memory hygiene · spec tokens (a spec's own names resolve)

### Non-goals

No other spec. No product code. No change to the unit's mechanism beyond what a divergence or a stale claim forces.

### Limitations

The write grant is `memory/builds/dBoundRoles/spec/2026-10-25-spec-TOOL-dBoundRoles-14.md` alone.

### Reuse

The spec's own §10; the return's "What held" section lists the seams already confirmed at HEAD.
