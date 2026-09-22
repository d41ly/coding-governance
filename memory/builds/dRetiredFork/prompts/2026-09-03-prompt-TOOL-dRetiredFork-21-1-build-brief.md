# Build brief — TOOL-dRetiredFork-21

**Serves:** journal TOOL-dRetiredFork-21

## Two of six scope items are already done, and saying so beats rebuilding them

`TOOL-dRetiredFork-14` landed one unit earlier and overlapped this one.

**S1 is DONE.** Both fragments carry `{kit}/hooks/scratch-guard.js` and
`{kit}/memory-recall/recall-opened.js`. The spec asked for `{prefix}/...`; what shipped is a `{kit}`
token expanded **against the fragment's own location** — two directories up from the
`.fragment.json`. That is stronger than a fixed prefix: it is correct for a repo whose kits sit at
more than one prefix, which is exactly what check-wiring's own fixtures are. `grep` for
`.claude/hooks/` across the fragments returns nothing, so AC1 already holds.

**S3 is ANSWERED, and the answer is the permissive one.** The repath compares a fragment-supplied
`hook_path`, not only the built-in default: `merge()` takes the fragment, `resolve_hook_path()`
expands its token, and a command whose marker matches but whose path differs is rewritten in place.
So S1's edits ARE sufficient for an already-wired tree. Recorded here and in §9 per AC3.

## What is genuinely left, and one of it is live

**S2 is the real find.** `tools/memory-recall/adopt-memory-recall.sh:179-181` still does
`mkdir -p "$ROOT/.claude/hooks"`, copies `recall-opened.js` into it, and its closing line tells the
operator that is where the hook went. It re-creates the exact file the previous unit withdrew,
whatever the descriptor says — and that closing line is the last thing an adopter reads at the
moment they wire the hook, so a stale path there is worse than a stale one in a descriptor.

**S4 is the gate that would have caught all of this**: every `hook_path` in
`tools/**/*.fragment.json`, and every hook destination an adopter script WRITES, must resolve to a
destination some `kit.toml` rule declares. A fragment naming a path no descriptor ships is a wiring
hole whoever created it — and this build created two, in the unit written to prevent them.

**S5 requires the RED observed before wiring**, by reverting one fragment. **AC5** requires the gate
to REFUSE on an empty fragment population, because a gate that found no fragments reports the same
zero as a clean tree.

## The population is two

`git ls-files '*.fragment.json'` returns exactly two files. A gate over two subjects is worth having
precisely because the failure it catches is silent, but the anti-vacuity arm matters more than usual
at that size.

## Not this unit

agent-cap (TOOL-14 owns it). Withdrawing the `.claude/hooks/` destinations (done, and doing it here
would be the unwiring this unit exists to prevent). Deleting an adopter's installed copy — S6's
ordering says the wired command moves BEFORE the old copy goes, and `DEPL-dRetiredFork-3` owns
enforcing that.
