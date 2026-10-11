# Spec brief — TOOL-aBriskPreflight-1: check-wiring's per-item loops become one batched call per arm

**Serves:** research TOOL-aBriskPreflight-1

Read first: the build README, the prompt record
(`prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md`) and the baseline record
(`build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md`), which carries the measured cost of
each site named here.

## The mechanism, one

In `tools/check-wiring.sh`, a loop that starts one process PER ITEM becomes ONE call over all the
items, inside the arm that owns the loop. Three sites, all in two arms:

1. `check_merge_rows`' family harvest (the `seen=$(printf … | while IFS= read -r p; do [ -f "$p" ] && sed -n '…' "$p"; done | LC_ALL=C sort -u)` block): 120 `sed` starts, 131 s at BASE. The
   existence test is a builtin; keep it, collect the existing paths, and run the SAME `sed`
   expression once over all of them. A command line has a length limit on Windows (about 32 K
   characters), so the spec must say how a large population is split, and the split must not drop
   or duplicate a path.
2. `check_merge_rows`' smoke assertion (`for f in $fams; for n in 001 002 003; grep -c …`): one
   `grep -c` per family per id. One pass over `$smoke/a` that counts every expected id, giving the
   same `miss` list in the same order. The two `sed` reads of the audit line (`kd`, `hs`) may become
   one.
3. `check_eol`'s population (`git ls-files … | grep -E … | while read _p; git check-attr eol -- "$_p" | sed …`): one `git check-attr --stdin eol` over the same filtered list. The comment above
   it records WHY it went per-path: `xargs` word-split a path with a space. `--stdin` reads one path
   per line, so a space survives; the spec must keep a path with a space in the population and say
   how that is observed.

## What may not move

- Every line each arm prints, byte for byte, on the same tree, and every verdict (`ok`, `skip`,
  `note`, `UNWIRED`, `FIXED`) and the exit status. The prompt's role statement: "You weaken no
  check. Every refusal and every UNWIRED line it can print today it still prints, observed RED on a
  staged break."
- No timeout or bound is raised.

## Out of scope

- The `$(first_of …)` and `$(resolve_receipt_path …)` substitutions: aSparedSpawn-8 S3 plans
  `first_of` as a fork-free reader. Do not convert either.
- The settings and fragment readers (`json_str`, `matchers_of`, `settings_json`) and the python
  resolution: unit 2.
- The straggler inventory's own cost (`migrate_backlog.py --stragglers`): unit 3 decides whether
  preflight runs that arm at all.

## Acceptance shape

- Equivalence: the arms' printed lines before and after, on one tree, compared byte for byte.
- Spawn count: the build's `trace-spawns` instrument over a traced `--check`, before and after.
- RED on a staged break, GREEN restored, through a SLICED arm of `tools/check-wiring.test.sh`
  (memory note: prologue plus one block in a temp script inside the kit dir), never the whole suite:
  a merge=rows index leading with an undeclared family must still print the `does not declare`
  UNWIRED line; a CRLF in a pinned Skill, including one under a directory whose name has a space,
  must still print the eol `note` (and `fixed` under `--fix`).
- Witnesses in §6 by basename (`check-wiring.sh`, arm names), never a full path: §6 path tokens are
  joined against `git ls-files`.

## Conventions this repo grades

- A new shell function leads with a declared lexicon verb: ask
  `python tools/lexicon/lexicon.py --suggest <name> --as sh.function` before naming one.
- A new or renamed function stales `memory/map/generated/symbols.json`: the build pass runs
  `python tools/codebase-map/gen_map.py --write`.
- `check-wiring.sh` is a kit file with `KIT_CHECK_WIRING_VERSION`; the build bumps it ONCE, after the
  kit's last move in this build, not in this unit.
- Tier: mechanical, no new write path or contract — Tier-1 unless the spec finds otherwise.
- Order: 1, with units 5 and 6 (disjoint write sets).
