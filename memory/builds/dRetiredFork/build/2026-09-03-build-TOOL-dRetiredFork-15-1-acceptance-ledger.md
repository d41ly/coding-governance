# Acceptance ledger — TOOL-dRetiredFork-15

**Serves:** journal TOOL-dRetiredFork-15

Tier-2 · node d · 2026-09-03

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-15

- AC0 — MET, and observed before either key was wired — `bash tools/memory-tree/check-memory-hygiene.sh`
  exits 2 naming the key for a future `RECORD_SERVES_CUTOFF` and for a `BUILD_SLUG_RE` matching the
  empty string. The empty-match guard fires on its own: `^[A-Za-z0-9-]*$` passes both anchor tests
  and is still refused
- AC1 — MET — `diff` against a baseline captured before the first edit is byte-identical with no key
  set. gov's green output is two lines, so the comparison is exact
- AC2 — MET — `BUILD_SLUG_RE="^zzz[A-Za-z]+$"` rejects all 88 build folders and exits 1;
  `^[A-Za-z]+$`, which gov's own slugs satisfy, still passes
- AC3 — MET — `BUILD_SLUG_RE` unanchored and empty-matching values both ABORT naming the key,
  rc=2
- AC4 — MET — a probe file under `memory/project/` is reported without the key and silent with it,
  measured in both directions
- AC5 — MET — a 2020-dated record with no `Serves` line is reported without a cutoff and exempt with
  `RECORD_SERVES_CUTOFF="2026-01-01"`, measured 1 then 0
- AC6 — MET — check 4 now consults `LEGACY_SET`, which check 5 has read at its `in_legacy` line all
  along. No new key
- AC7 — MET as a DECLARATION — `ENTRY_CAP_UNIT` — and the measurement is more interesting than
  the criterion. On this
  node awk's default `length()` already counts BYTES: 200 em-dashes measure 600 by default, 600
  under `LC_ALL=C`, and 200 under `LC_ALL=C.UTF-8`. So `bytes` is a no-op here and `chars` is the
  value that changes anything — which is exactly the platform-dependence the key exists to make
  visible
- AC8 — MET — `bash tools/check-kit-versions.sh`, `check-verdict-epoch.sh` and
  `kit-dogfood-parity.test.sh` all exit 0 after the 2.58 to 2.59 bump

## This key disabled check 3 twice before it widened it once

`PROJECT_REGISTRY_EXTRA` only ADDS to a whitelist, so §2 correctly says it carries none of the
narrowing risk the two validated keys do. It still managed to turn check 3 off twice:

**First**, the `F:*)` case was placed ABOVE the named ones, where it matched every one of them and
accepted it. Check 3 stopped grading anything under `project/` and reported clean. A widening case
has to sit where it can only widen, and it now sits last with a non-match falling through to the
same refusal the catch-all gives — spelled out rather than reached by omission, because a case
ending in `;;` accepts.

**Second**, the comparison read `$bp` — which is the variable the whole command substitution is
being ASSIGNED to, and is therefore unset inside it. Under `set -u` that killed the subshell, so
check 3 emitted nothing at all and again reported clean. The case subject is `$e`.

Both were caught by an arm that asserts an UNLISTED file is still reported while a named one is
silenced. An arm that only checked the silencing half would have passed all three times.

## The cost, re-declared rather than hidden

These arms drive the checker over gov's real corpus, and the fixture is a `git archive` of the whole
tree. The suite went from roughly 6.6 s to **381 s measured**, so its declared ceiling moves from
6590 to 480000 ms.

The first cut was worse: it built a fresh scratch tree PER ARM, fourteen times, and the suite TIMED
OUT at ten minutes. One fixture, reused, with only the conf line varying between runs.

Trimming three full-corpus runs whose property was already carried elsewhere moved the wall by five
seconds, which located the cost precisely: it is the single fixture build, not the checker runs.
§7 permits re-declaring a ceiling with a reason and this is that; the leg is `chunk = selftests`, so
it is held off the ordinary bar and costs nothing on a normal push.

## An arm that forbade this unit's own change

`check-memory-hygiene.test.sh` carried an arm asserting check 7 takes NO locale prefix, because
pinning one would re-decide the cap for any adopter whose awk counts characters. That is the exact
concern F1 raised, and the arm was right to exist.

It is now widened from "no prefix" to "no prefix the conf cannot switch off", with a second arm
asserting the switch DEFAULTS TO EMPTY. A literal `LC_ALL=C awk` still reds, which is the case that
mattered; a prefix that is empty unless `ENTRY_CAP_UNIT` is set re-decides nothing.

## Not fixed here

The three remaining suite failures are pre-existing scaffold defects, measured before this unit
touched the file and filed as `TOOL-dRetiredFork-25`.
