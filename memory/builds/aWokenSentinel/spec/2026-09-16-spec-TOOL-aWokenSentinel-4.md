# TOOL-aWokenSentinel-4 — `stall-recorder`, the `StopFailure` hook that writes an API-error stall to disk

**Status:** SPECCED · rev-1 · 2026-09-16 · node a · Tier-2 · base 5f9648d6 · streams tooling · order 4

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md](../build/2026-09-16-build-TOOL-aWokenSentinel-1-0-keepalive-research.md) | research | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 |
| [2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-TOOL-aWokenSentinel-1-1-spec-briefs.md) | journal | TOOL-aWokenSentinel-1 TOOL-aWokenSentinel-2 TOOL-aWokenSentinel-3 TOOL-aWokenSentinel-5 TOOL-aWokenSentinel-6 TOOL-aWokenSentinel-7 |

<!-- /gen:spec-records -->

## 1. Goal

A turn that ends on an API error — `rate_limit`, `overloaded`, `server_error`,
`max_output_tokens` — leaves nothing on disk that names the run, and four Tier-2 reviews that died
on limits were found by a human reading a journal. `stall-recorder.js`, a `StopFailure` hook in
the unattended kit, binds the failing session to its run through the module unit 3 extracted and
appends one line to `stall.<slug>.log` under the git dir, at zero API cost, after the turn the API
refused. `--liveness` reads that file's last line as `last-stall`.

## 2. Scope (IN)

- **S1** — the hook, `stall-recorder.js`: read stdin, bind `session_id` to a run through
  `run-lease.js` by `__dirname`, and exit 0 with zero writes and empty stdout when no record
  binds. Observed by AC1, AC5.
- **S2** — on a bound run, ONE appended line: `<utc> <session> <error-class-or-unknown> <the whole
  stdin JSON, compact>`, space-separated, the class taken from the payload's `error` field when it
  is a non-empty string and `unknown` otherwise. Observed by AC2, AC3, AC4, AC6.
- **S3** — nothing on stdout in any case, exit 0 in any case, and no attempt to block: the
  harness discards this event's output by documentation. Observed by AC1, AC2, AC5.
- **S4** — the fragment `stall-recorder.fragment.json` on event `StopFailure` with matcher `*`,
  so every error class is recorded, wired into `.claude/settings.json` by the merger in the same
  commit, asserted wired by the adopter's generalised fragment loop, and the suite in the
  descriptor's `project-owned` list. Observed by AC7, AC8, AC9.
- **S5** — the line is what `--liveness` prints as `last-stall:`, observed once against the real
  driver on a git fixture. Observed by AC10.
- **S6** — the suite, its budget row, the carried-prefix registry raise, and the symbols
  artifact regenerated. Observed by AC9, AC11, AC12.

## 3. Non-goals (OUT)

- **No field assumed beyond `session_id`.** The `StopFailure` stdin was never measured on this
  fleet. The harness documentation, fetched 2026-09-16, shows an `error` field carrying the
  matcher value, and the fetcher reported that example as inferred from the page's pattern rather
  than quoted, so the field name is UNVERIFIED. The hook tries `error` and falls back to
  `unknown`, and the whole compact payload rides the line so a later reader parses what was
  actually handed over.
- **No resume, no notification, no blocking.** The hook records; unit 5's tick acts on a stale
  lease and the sidecar this unit writes is one of its inputs through `--liveness`.
- **No prose carriers and no version bump.** Unit 6 and the close, as unit 3's §3 states.
- **No second binder.** The scan, the conf reader and the sidecar writer are `run-lease.js`; this
  hook adds a class extractor and a `main`, nothing else.
- **No matcher narrowing.** The documented matcher values are twelve today and the list can grow;
  a fragment naming them would record only the classes somebody typed.

### Edges

- **consumes-from** `TOOL-aWokenSentinel-3` — `run-lease.js` (`readStdin`, `resolveRepo`,
  `readMemoryRoot`, `resolveLease`, `deriveSidecarPath`, `writeSidecarLine`, `renderUtc`), the
  fragment shape with matcher `*`, the adopter's fragment loop and the seed that copies every
  fragment and hook. Without the module this hook has no binder; without the loop its fragment
  can ship unwired.
- **consumes-from** `TOOL-aWokenSentinel-1` — the `session:` fact; an unset one binds nothing.
- **consumes-from** `TOOL-aWokenSentinel-2` — the `last-stall` reader in `--liveness`, which
  prints the last line of this sidecar or `none`.
- **hands-off** `TOOL-aWokenSentinel-5` — acting on a stall: the tick reads `--liveness`, whose
  `last-stall` is this line.
- **hands-off** `TOOL-aWokenSentinel-6` — the README's sidecar layout paragraph, the Skill's
  hook section, the map dossier.
- **hands-off** external — a measurement of the `StopFailure` stdin on this fleet, which turns
  the `error` field from UNVERIFIED into a pinned key and the `unknown` fallback into a
  documented rarity; the first recorded stall is that measurement, and the backlog row filed at
  landing points at the sidecar.

## 4. Design

### The order of work inside the hook

```
stdin JSON                       unparseable: exit 0
  -> resolveRepo(cwd)            {root, gitDir}; no .git: exit 0
  -> readMemoryRoot(root)        .unattended.conf beside .git; default memory
  -> resolveLease(root, memoryRoot, session_id)
                                 no record whose session: equals it: exit 0, nothing written
  -> extractErrorClass(data)     data.error when a non-empty string, whitespace folded to `-`,
                                 else `unknown`
  -> writeSidecarLine(deriveSidecarPath(gitDir, 'stall', slug),
                      `${renderUtc()} ${session_id} ${class} ${JSON.stringify(data)}`)
  -> exit 0, nothing on stdout
```

`cwd`, the fallbacks and the walk are unit 3's. The four functions and the constant are the
whole file; the header states that it records and cannot block, that it assumes one field, and
that the payload is written whole for that reason.

### The line

`<git-dir>/unattended/stall.<slug>.log`, created with its directory on first write, append-only,
never tracked, one line per event:

```
2026-09-16T14:02:11Z 3f0c…-uuid rate_limit {"session_id":"3f0c…","hook_event_name":"StopFailure","error":"rate_limit",…}
```

The first three fields are space-free by construction — the utc is the driver's `--park`
spelling, the session is a uuid, and the class has its whitespace folded — so a reader that splits
on the first three spaces gets the payload whole. `--liveness` prints the LAST line verbatim as
`last-stall:`, which is why the line is one line: a compact `JSON.stringify` carries no newline.
An `error` value that is not a string, is empty, or is absent reads `unknown`; the payload still
shows what was there.

### The fragment and the wiring

```json
{ "name": "stall-recorder", "event": "StopFailure", "matcher": "*",
  "marker": "stall-recorder.js", "hook_path": "{kit}/unattended/stall-recorder.js" }
```

`StopFailure` supports matchers on the error type and the documentation's table reads `*` as
`Match all`, so one fragment records every class, the ones the docs list and any added later. The
merger writes a new `StopFailure` group; the adopter's loop enumerates the fragment beside
`gate-guard` and `stop-guard`, so its count reads three at this order; the settings render is the
last write of the pass. The `**` engine rule ships hook and fragment; the suite is `project-owned`.

### The fixture and the direct observation

`KIT` is a scratch directory holding `stall-recorder.js` and `run-lease.js` — no driver stub,
because this hook never spawns one; `FIX` and `P` are unit 3's shapes, `P` carrying
`hook_event_name` `StopFailure` and the arm's `error` value or none. One integration arm builds a
`git init` fixture seeded the way the adopter suite's `seed()` does, copies the real driver beside
the hook, feeds one payload, then runs that driver's `--liveness fx` and asserts its `last-stall:`
line equals the sidecar's last line, read from the file. The suite prints `PASS (<n> assertions)`
against a derived `FLOOR_ASSERTIONS`.

### Inventory

Cell `js.function camel`: `extractErrorClass` and `main` in `stall-recorder.js`, the rest
required from `run-lease.js`. Constant `KIT_STALL_RECORDER_VERSION`. Both exported, `main`
guarded by `require.main === module`.

### Files touched (estimate)

| file | change |
|---|---|
| `tools/unattended/stall-recorder.js` | new, the hook; header states it cannot block and assumes one field |
| `tools/unattended/stall-recorder.fragment.json` | new, the §4 shape, event `StopFailure`, matcher `*` |
| `tools/unattended/stall-recorder.test.sh` | new, the withheld suite; every fixture under the run's scratchpad, the git fixture under a short `%TEMP%` path |
| `.claude/settings.json` | one `StopFailure` group appended by the merger, never by hand; last write of the pass |
| `tools/unattended/kit.toml` | `stall-recorder.test.sh` joins the `project-owned` include list; no conf key |
| `tools/unattended/adopt-unattended.test.sh` | one arm: with the seeded fixture's `StopFailure` group removed, `--check` reads `the stall-recorder hook is UNWIRED`; restored, `rc=0` and the count line reads three |
| `tools/run-gates/selftest-budgets.txt` | one row, budget from the measured first green times 1.5 floored at 60 s |
| `tools/install-prefix-carried.txt` | the `selftest-budgets.txt` row raised by ONE by hand with its reason, from the value it holds at dispatch (16 once unit 3 lands); a row for the suite if the checker reports its literals |
| `memory/map/generated/symbols.json` | re-rendered by `python tools/codebase-map/gen_map.py --write` in the same commit, for the new kit `.js` |

### Alternatives rejected

- **Read `isApiErrorMessage` from the transcript.** Measured for an auth error only, and it needs
  a reader that runs; the hook runs at the moment of the error and needs no reader.
- **A JSON line like the stop sidecar.** The brief's shape is space-separated with the payload
  last, and `--liveness` prints the last line verbatim either way; the three leading fields make a
  stall greppable by class without a parser.
- **Try to block or notify.** Output is discarded for this event by documentation; a hook
  claiming an effect it cannot have is the vacuous-selector class.
- **Name the twelve matcher values in the fragment.** Every class not typed goes unrecorded.

## 5. Production-readiness checklist

- security — reads the tree, appends one line under the git dir, spawns nothing.
- perf / scale — unbound: one directory listing and 51 small reads (PINNED 2026-09-16, DERIVED by
  the scan); bound: one append. It runs after a turn the API already refused, so its cost is not
  on any turn's path.
- error / empty / loading states — two outcomes: silent exit 0 when unbound or unparseable, one
  line when bound. An unwritable sidecar prints one stderr sentence, which the harness discards,
  and exits 0.
- observability — the line names when, who, which class, and the whole payload; `--liveness`
  surfaces the last one to every reader.
- risks — the `error` field name is UNVERIFIED (§3): the fallback is `unknown` and the payload
  carries the truth. A run bound to a session whose failures are frequent grows the file by one
  line per failure, bounded by the harness's own retry behaviour.
- testing — the pass feeds the copied hook payloads in milliseconds and one arm against the real
  driver; the suite re-runs them at the close.
- migration — additive: a new event key in the settings file, no conf key, no protocol field.
- user docs — none here; unit 6.

## 6. Acceptance criteria

`KIT`, `FIX` and `P` are §4's; `HOOK` is the copied hook under `KIT`.

- **AC1** — When `P` carries a `session_id` no record under `FIX` names, `printf '%s' "$P" |
  node "$HOOK"; echo "rc=$?"` prints `rc=0`, stdout is empty, and no `stall.fx.log` exists under
  the fixture's git dir. Observed RED before the hook file exists.
  Red when: an unbound session writes a line or prints anything.
- **AC2** — When `FIX`'s record carries `session:` equal to `P`'s and `P` carries `error` equal to
  `rate_limit`, the invocation prints `rc=0` with empty stdout and the sidecar holds exactly one
  line whose third field is `rate_limit` and whose tail, from the fourth field on, parses as JSON
  deep-equal to `P` under `python -c 'import json…'`.
  Red when: the line is absent, the class is wrong, or the payload is truncated.
- **AC3** — When `P` carries no `error` key, and separately `error` as an object, and separately
  `error` as an empty string, the third field is `unknown` in each of the three lines.
  Red when: a missing field throws, or an object is stringified into the class.
- **AC4** — When `P` carries `error` equal to `server error 500`, the third field is
  `server-error-500` and the line still splits into a payload that parses.
  Red when: whitespace in the class shifts the payload's field position.
- **AC5** — When stdin is not JSON, the invocation prints `rc=0`, empty stdout, and writes nothing.
  Red when: the hook exits non-zero, which the harness discards but a reader of the suite would
  misread as a block.
- **AC6** — When two payloads are fed in sequence, the sidecar holds two lines in order, the first
  unchanged; when `FIX`'s `.git` is a FILE holding `gitdir: <path>`, the line lands under that
  path's `unattended/` and a `find` over the fixture prints one `stall.fx.log`.
  Red when: a second write truncates, or the worktree case writes beside the `.git` file.
- **AC7** — When `python tools/settings-merge.py --fragment` has run with the stall-recorder
  fragment as its argument, `python -c` over `.claude/settings.json` prints one group under
  `StopFailure` whose `matcher` is `*` and whose one command ends with the hook's basename; a
  second run leaves the file byte-identical.
  Red when: the merger refuses the fragment, or appends a second entry.
- **AC8** — When `bash tools/unattended/adopt-unattended.sh --check` runs with the fragment
  wired, it prints `hooks: 3 fragment(s) wired` and `in sync`, `rc=0`; with the `StopFailure`
  group removed from a copy of the settings file declared through `GOV_SETTINGS_JSON`, it prints
  `the stall-recorder hook is UNWIRED`, `rc=1`.
  cost: 12 s measured on node a 2026-09-15.
  figure: 3 is DERIVED by the loop and equals the kit's fragment count at this order.
  Red when: the loop reports two fragments as `in sync` with the third unwired.
- **AC9** — When `bash tools/check-hook-destinations.sh` runs after the fragment lands, it prints
  its clean line, `rc=0`, and a fragment count one higher than after unit 3. Observed RED first by
  pointing `hook_path` at a basename the kit does not ship.
  cost: 75 s measured on node a 2026-09-15.
  figure: DERIVED by the gate from `git ls-files`.
  Red when: the resolvers disagree on `{kit}`, or the destination is not shipped.
- **AC10** — When the real driver sits beside the hook in a `git init` fixture whose record is
  at BUILDING with `session:` equal to `P`'s, and one `rate_limit` payload has been fed, the
  copied driver's own `--liveness fx` prints a `last-stall:` line equal to the sidecar's last
  line, both read from the fixture; before the payload it prints `last-stall: none`.
  fixture: a `git init` tree seeded like the adopter suite's, under a short `%TEMP%` path; the
  driver needs unit 2's verb, landed by order.
  cost: the driver's startup, seconds, twice.
  Red when: the reader prints the line with its payload trimmed, or `none` after a write.
- **AC11** — When `python tools/codebase-map/gen_map.py --check` runs after the regen, `rc=0`;
  before it, with the new file present, it prints the drift and `rc=1`.
  Red when: the `kit-js` layer does not index the file, so the check cannot move.
- **AC12** — When `python tools/lexicon/lexicon.py` runs, its `js.function` row reports no new
  offender; `bash tools/check-install-prefix.sh` reports `tools/run-gates/selftest-budgets.txt` at
  its raised count and no unlisted literal in the kit dir.
  cost: 6 s and 83 s measured on node a 2026-09-15.
  Red when: a name leads with a verb outside the table, or the budget row lands without its raise.

## 7. Gates

`unattended skill wiring` · `hook destinations (every declared hook path ships)` · `install-prefix (shipped surface)` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `govkit selfcheck` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The pass runs none of these; it verifies with the direct checks §6 names, and the bar runs once
at the close.

New arm: tools/unattended/stall-recorder.test.sh · a fixture record bound to the payload's session, one arm per §6 payload, one arm against the real driver's `last-stall` on a git fixture; the break is the hook absent, then each §6 negation · `FLOOR_ASSERTIONS` derived at the suite's first green

New arm: tools/unattended/adopt-unattended.test.sh · the seeded fixture with its `StopFailure` group removed reads UNWIRED naming `stall-recorder`; the break is unit 3's loop with this fragment absent from the seed · no floor exists in this suite

## 8. Open questions

- **F1 — `error` as the class field, or record `unknown` for everything until measured.**
  RESOLVED (agent, 2026-09-16, delegated): try `error`, fall back to `unknown`, write the payload
  whole. The documented example names `error` and the fetch could not quote it verbatim; the
  fallback costs nothing and the payload on the line is the measurement the next reader makes.
  Vetoes clean.
- **F2 — a fragment naming the documented classes, or `*`.**
  RESOLVED (agent, 2026-09-16, delegated): `*`, the documented `Match all`; a typed list records
  only what somebody typed, and the same spelling passes every reader unit 3 §8 F1 names.
- **F3 — space-separated with the payload last, or one JSON object like the stop sidecar.**
  RESOLVED (agent, 2026-09-16, delegated): space-separated, the brief's shape, because the brief
  is what units 2 and 5 were specced against concurrently and a shape change here is a
  disagreement between three documents; the three leading fields are made space-free so the
  payload is recoverable without a parser.

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft, from the spec brief and the research record.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "a hook that appends an API error stall line to a
sidecar log under the git dir"` found no seam for a stall recorder: the candidates are error
classes by name stem (`MapError`, `ConfError`, `DriftError`), `git` helpers in govkit and the
recall kit, `append_backlog` in the map kit, and the `.unattended.conf` affordance seam; it
reports `unscanned layers: .sh`. The seam this unit extends is unit 3's `run-lease.js` — the
binder, the git-dir derivation and the sidecar append are consumed by `__dirname` and nothing is
re-implemented — with unit 3's `stop-guard.fragment.json` as the fragment shape and the adopter's
generalised loop as the wiring assertion. The recall query returned nothing prior on
`StopFailure`: the hits are this build's own research record and briefs, `TOOL-aProbedUnit-11` on
`--audit`'s idle bound, and `TOOL-aHoistedPass-16`'s limit that nothing under the run's uid binds
it, which is why the recorder writes under the git dir and claims no effect. Where the brief and
source disagreed: none for this unit; the docs fetch left the `error` field name UNVERIFIED and
§3 says so.

Recall terms used: `StopFailure API error rate limit overloaded usage limit turn ended silently
transcript isApiErrorMessage stall sidecar`, with the question "what records an API error or
usage limit stall of an unattended run on disk".
