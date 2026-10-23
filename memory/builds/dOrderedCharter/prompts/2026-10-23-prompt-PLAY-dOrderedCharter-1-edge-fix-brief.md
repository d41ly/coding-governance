**Serves:** research PLAY-dOrderedCharter-1 PLAY-dOrderedCharter-2 PLAY-dOrderedCharter-3 PLAY-dOrderedCharter-4 PLAY-dOrderedCharter-5 PLAY-dOrderedCharter-6 PLAY-dOrderedCharter-7 PLAY-dOrderedCharter-8 PLAY-dOrderedCharter-9 PLAY-dOrderedCharter-11 PLAY-dOrderedCharter-12 PLAY-dOrderedCharter-13 PLAY-dOrderedCharter-14 PLAY-dOrderedCharter-15 PLAY-dOrderedCharter-20 PLAY-dOrderedCharter-21 PLAY-dOrderedCharter-23 PLAY-dOrderedCharter-29 PLAY-dOrderedCharter-30 PLAY-dOrderedCharter-31 PLAY-dOrderedCharter-32 PLAY-dOrderedCharter-37 PLAY-dOrderedCharter-33

# Edge-fix brief — hygiene check 12 over the staged spec set

Fix every hit `bash tools/memory-tree/check-memory-hygiene.sh --only 12` reports over the staged dOrderedCharter
specs, so check 12 prints no dOrderedCharter line, changing nothing else.

- A missing reverse edge: the sibling's §3 gains the matching edge back (`consumes-from` for a `hands-off`,
  `hands-off` for a `consumes-from`), naming the same token the first edge names, in the sibling's own words. Where
  reading both specs shows the first edge is wrong (the sibling neither produces nor needs what it names), remove or
  correct the first edge instead, and say which in your return.
- The order hit: PLAY-dOrderedCharter-30 (order 28) hands off to PLAY-dOrderedCharter-21 (order 23), which builds
  first. Keep the build order: re-express the dependency so no edge runs against it (21 reads whatever catalogue rows
  exist when it builds, and 30's row joins later as data, say), and fix both specs' §3 to match.
- PLAY-dOrderedCharter-33's acceptance criterion 6 plants `successor = "<new tag>"`, while PLAY-dOrderedCharter-15
  names the change-record field `**Successor:**`: spell it as unit 15 does (shared interface S13).
- The specs are uncommitted at rev-1 and unaudited, so edit them in place with no rev bump. Touch no deviation record.
- Do not commit, do not stage, and do not run the build-index generator. Re-run check 12 (`--only 12`) and report its
  dOrderedCharter lines (zero is the target).

## The hits, verbatim

- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-1.md (§3 declares **hands-off** `PLAY-dOrderedCharter-32` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-1` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-1` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-11` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-11.md (§3 declares **hands-off** `PLAY-dOrderedCharter-14` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-11` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-13` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-12` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-7` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-12` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-12.md (§3 declares **hands-off** `PLAY-dOrderedCharter-2` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-12` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-13.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-7` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-13` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-14.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-8` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-14` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-9` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-15` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-12` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-15` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-15.md (§3 declares **hands-off** `PLAY-dOrderedCharter-1` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-15` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md (§3 declares **hands-off** `PLAY-dOrderedCharter-2` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-20` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md (§3 declares **hands-off** `PLAY-dOrderedCharter-3` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-20` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-20.md (§3 declares **hands-off** `PLAY-dOrderedCharter-21` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-20` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-23.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-1` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-23` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-30` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-29` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-29.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-3` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-29` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-1` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-30` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-2` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-30` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md (§3 declares **hands-off** `PLAY-dOrderedCharter-21` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-30` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-31.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-6` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-31` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-37.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-6` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-37` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-5.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-2` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-5` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-7.md (§3 declares **hands-off** `PLAY-dOrderedCharter-1` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-7` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-8.md (§3 declares **consumes-from** `PLAY-dOrderedCharter-5` and that unit declares no matching **hands-off** `PLAY-dOrderedCharter-8` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-9.md (§3 declares **hands-off** `PLAY-dOrderedCharter-4` and that unit declares no matching **consumes-from** `PLAY-dOrderedCharter-9` back)
- memory/builds/dOrderedCharter/spec/2026-10-23-spec-PLAY-dOrderedCharter-30.md (§3 **hands-off** `PLAY-dOrderedCharter-21`, whose `order` 23 is BEFORE this unit at 28)
