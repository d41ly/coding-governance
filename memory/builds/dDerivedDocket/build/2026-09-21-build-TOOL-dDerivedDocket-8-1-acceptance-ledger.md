# TOOL-dDerivedDocket-8 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-8

The hygiene engine, `corpus_ids.py` and `row_grammar.py` now read the declared backlog layout. AC1,
AC8, AC10, AC12 and AC14's leg run each carry a `permission:` line deferring the observation to a run
the main loop makes after the last unit is terminal; those get no line here and the orchestrator
writes them after that run. Everything below was observed in this pass, against a fixture or a staged
break.

**Evidences:** TOOL-dDerivedDocket-8
- AC2 — `BACKLOG.md` — in the builds-mode fixture the one over the row cap is named on the branch
  carrying the never-rotate remedy, and the family view over the same cap is not named at all; over
  the same tree under `shards` the oversized shard is named with today's rotate message. Staged RED:
  with the resolved mode pinned to `shards` in a scratch copy of the engine, the builds run names the
  shard and never the ask file.
- AC3 — `BACKLOG.md` — the fixture's 500-character ask row is exempt from the entry budget and the
  view's 320-character line is named, `memory/backlog/ARCH.md:103 (320 chars > 300)`. Staged RED:
  with the `ex7` append deleted in a scratch copy, the run adds
  `memory/builds/tAsk/BACKLOG.md:5 (500 chars > 300)`.
- AC4 — `builds` — over the builds-mode fixture the engine prints
  `memory-hygiene: check 8: backlog layout builds — graded by check 9` and no check 8 failure, no
  graded-row line and no empty-population line; over the shards fixture it prints
  `memory-hygiene: check 8 graded 201 backlog row(s) across 2 shard(s)`. Staged RED: with the mode
  pinned to `shards`, the builds run prints the graded-row line instead of the announcement.
- AC5 — `python3 tools/memory-tree/corpus_ids.py --selftest` — the arms are written, and each was
  observed by hand against a scratch corpus, which is the in-pass check this criterion's permission
  line names. A post-cutoff ask anchored in a second folder is a check 13 collision; the same shape
  filed before the cutoff raises nothing and is still not an orphan under check 14; a `2026-9-30`
  cutoff skips every ask row naming V16; a blank one skips every ask row naming V15. Staged RED, two
  breaks: a blanket skip loses the collision, and comparing an unusable cutoff as a raw string loses
  both notes and reds the legacy anchors.
- AC6 — `BACKLOG.md` — under the builds layout the ask's dead path citation is graded and the view's
  is not; under `shards` over the same tree the shard's is graded and the ask file's is not. Staged
  RED, two breaks: dropping `backlog/` without adding the ask file takes the ask's token out of the
  check, and leaving the corpus untouched grades the view's.
- AC7 — `python3 tools/memory-tree/row_grammar.py --selftest` — PASS, all arms held, six of them new.
  Under the builds layout the row documents are the decision log and its archive, the decision log's
  own duplicate still fails check 20, the view's duplicate is not named, and check 24 grades exactly
  one archive. Staged RED in a scratch copy, two breaks: the stem set returning every family, and the
  `backlog/` prefix admitted unconditionally.
- AC9 — `BACKLOG_MODE` — over one fixture the shell and the Python reader both report `shards` for an
  absent key, a blank one and `shards`, and `builds` for `builds`, read through the engine's
  `--print-backlog-mode`; `buildz`, `Builds` and a leading-space `builds` each exit 2 naming the key
  and its legal values.
- AC11 — `curation-debt.txt` — with the family view listed in it, the builds run reds check 6 with
  the stale-entry guard naming `memory/backlog/BRAND.md`; under `shards` the same row earns check 6
  and the guard is silent.
- AC13 — `ARMS_FLOORS` — asked through `check-arms`'s own `branches()` and `armed_signatures()` over
  the real files, because the leg's argv is a gate command this pass does not run. The engine carries
  32 fail branches, all armed, the new check 6 branch among them; with that arm's assertion line
  deleted in memory the branch reads unarmed. The engine's entry moves 27:27 to the measured 32:32,
  which rev-6 records and explains.
- AC14 — `grep -c 'corpus_ids.py' tools/install-prefix-waivers.txt` — prints 0, and both fixture
  lines in `tools/memory-tree/corpus_ids.py` carry `gov:root-fixture` with a reason. The gate's first
  arm reports clean over 269 shipped files with 27 marked fixture lines.
