**Serves:** research TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11

# Spec brief — dGroundRules, the eleven units and the interfaces they share

You author specs and write no product code. This is the build's SPEC RUN (README rule 1): every unit is specced and
audited here and built by the build run after it, so write each spec for a builder who has only it, the packet and
the tree. Read, in this order, before your first line:

1. The packet, `memory/builds/dGroundRules/prompts/2026-10-21-prompt-PLAY-dClosedLoop-1-packet.md`, whole. Its Items
   quote each clause verbatim with its id, hash and tokens; its Acceptance, Gates, Non-goals, Pins, Owned nodes,
   Gaps, Policy keys, Later builds and Obligations bind every unit.
2. The build README, `memory/builds/dGroundRules/README.md`: its build-level rules bind every spec, the fork-mark
   rule above all.
3. `memory/TEMPLATE-SPEC.md` and `memory/guides/BUILD-METHOD.md` M2, M3, M5. Every unit here is Tier 2: each is a
   new or changed kit contract.
4. v2's `[policies]` section, `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md`
   lines 1125-1408: the catalogue the schema encodes. Units 9 and 10 also read their research record whole:
   `B/2026-10-19-build-PLAY-dClosedLoop-1-research-caps.md` (unit 9) and
   `B/2026-10-19-build-PLAY-dClosedLoop-1-research-agent-cap.md` (unit 10), `B/` being
   `memory/builds/dClosedLoop/build/`.
5. Your units' sections below, and "Shared interfaces", which every writer reads.

You never edit v2, an instrument, the as-built view or the packet (the packet's Non-goals).

## Every spec, whatever its unit

- Path `memory/builds/dGroundRules/spec/2026-10-23-spec-TOOL-dGroundRules-<n>.md`; H1
  `# TOOL-dGroundRules-<n> — <title>`, an EM DASH, never a colon.
- Status header `DRAFT`, the `order` verb your roster names, `streams tooling`. Do not write `closes` or `advances`:
  the main loop sets the status and the ask verb when it defers the unit.
- The binding line at column 0 on a line of its own: `**Carries:** <the Items id>@<hash8> whole`, the hash being the
  one the packet's Items list gives. A unit whose clause names an owned node (the packet's Owned nodes) also carries
  `**Carries:** node:<node>` for each node it builds: `policy-key.policy-file.on-invalid` is unit 4's,
  `policy-key.budgets.*`, `policy-key.budgets.enforce` and `policy-key.budgets.pinned` unit 9's,
  `policy-key.runtime.agents-in-flight` unit 10's.
- Every token the packet's Items list for your clause appears in your spec verbatim, inside backticks.
- Each clause's own "seen red on" and "seen green on" cases are acceptance criteria, each its own, observed RED on
  its planted case and green without it, by a probe or fixture of the unit's own code a pass can run. No criterion
  names the merge bar, a `GATE_*=` prefix, a `*.test.sh` suite or a `--selftest` run: a new suite arm goes on a
  `New arm:` line in section 7 and the main loop observes it at the close.
- §10: run `python tools/codebase-map/reuse_lookup.py "<behaviour>"` and `python tools/memory-recall/query.py
  "<question>" --terms "<8-14 terms>"`, and record the seam, the terms and every hit's disagreement with source.
- §8 forks: settle each by README rule 6's rungs, in the §8 mark shape TEMPLATE-SPEC states. A choice on rung 5 or 6
  cites its ruling (ER:240, ER:388, ER:328 or P0.8 row 5) and carries `widens:` and `relaxes:`, each a value or
  `none`. Never leave an open question: a FACT-QUESTION names its probe and you run the probe now.
- A clause that names a later build's surface (the packet's Later builds) specs the stand-in the clause states and
  no more: that build's surface is a non-goal.
- Files touched: name every product path; they become the unit's `--dispatch --writes` set in the build run.

## Shared interfaces — one spelling for every writer

Fixed so eleven specs written by five writers agree on the interface axis (M2). A writer who finds one wrong says
so in its §8 as a fork and settles it there; it never silently respells one.

- **S1 · the file.** `.governance/policy.toml`, TOML 1.0 read through `tomllib` (the Python floor is 3.11). A key
  `a.b.c` is the dotted TOML path, so `budgets.enforce` is `[budgets] enforce = "warn"`. Unit 1 creates it holding
  only the keys this build owns, each at its catalogue default, and nothing else.
- **S2 · the kit.** One new kit, `tools/policy/`, with its `kit.toml` and its adopter, owned by unit 1. Every
  module below lives in it. The `may:` grant (PLAY-dClosedLoop-3) covers the public surface clause 0007 names.
- **S3 · the catalogue, which is the schema.** `tools/policy/catalogue.toml`, owned by unit 1: one `[[key]]` table per
  catalogue key with the fields `name`, `allowed` (an enum list, or a typed range such as `{ type = "count", min =
  1 }`), `default`, `empty` (`allowed` or `never`, set-valued keys only), `summary`, `usage`, `owner` (a build slug)
  and `direction` (unit 11's field). Its rows are v2's `[policies]` table, every key with its Owner, so unit 8's
  population and unit 3's default both read it. The shape audit (a set-valued key with no `empty`) and the
  summary/usage rule are unit 1's; the `direction` rule is unit 11's.
- **S4 · the reader.** `tools/policy/policy.py`, owned by unit 2, importable and a CLI. Python:
  `resolve(key, repo=".", rev=None) -> Resolution`, a named tuple `(value, source, reason)` where `source` is one
  of `file`, `preset`, `default`, `last-valid`. CLI: `python tools/policy/policy.py get <key> [--rev <rev>]`
  prints the value, `--explain` adds the source and the reason; a refusal exits 2 printing
  `policy: refused · <path>:<line> · <why>`. `rev=None` means the landed revision: the default branch's tip as the
  remote ladder resolves it in `tools/lib/resolve-remote.sh`, never the working tree. `read_policy_key` in
  `tools/unattended/unattended.sh` and its byte-identical copy keep their `KEY=value` contract for the legacy homes
  and gain no TOML parse. Unit 3 owns the resolution order inside `resolve`, unit 4 the invalid-file branch.
- **S5 · invalidity.** One function, `validate(text) -> list[Problem]`, `Problem` being `(line, key, why)`, in
  `policy.py`, owned by unit 4 and called by units 1, 5 and 6. The five failure classes are the clause's: absent,
  malformed, missing key, out-of-set value, and `refuse` followed by a malformed revision.
- **S6 · the mirror.** `.governance/policy.json`, owned by unit 5, written by
  `python tools/policy/policy.py mirror --write` and checked by `--check`. It carries the landed revision's sha, the
  TOML blob's sha, and every catalogue key's resolved value with its source. A JavaScript consumer reads it through
  one helper unit 5 specs, `tools/policy/policy-mirror.js`; unit 10's hook reads the limit through that helper.
- **S7 · the guarded paths.** `.governance/policy.toml`, `.governance/policy.json`, `.governance/instructions.toml`
  and `.governance/deploy.toml`, spelled once in `tools/policy/guarded-paths.txt`, owned by unit 6.
- **S8 · the derived lists.** Generated by `python tools/policy/policy.py lists --write`, checked by `--check`:
  unit 7's legacy-home list `tools/policy/legacy-homes.txt`, and unit 1's shrink-only list of keys lacking a summary
  or a usage `tools/policy/unsummarised-keys.txt`. Both shrink only.
- **S9 · the arms' home.** Each unit's arms are functions in `tools/policy/check_policy.py`, one CLI with a
  `--fixture` mode planting each red case in a temporary repository, so a pass observes them without a gate. The
  merge-bar leg that runs it is unit 1's `New arm:`; later units add arms to the same leg.

## Deviation records

None is owed by a writer: no unit here departs from its clause by plan. A writer who must depart (a stricter
acceptance, a stand-in the clause does not name) writes the record beside its spec under
`memory/builds/dGroundRules/build/`, named `2026-10-23-build-TOOL-dGroundRules-<n>-deviation-<k>.md` in the grammar
`deviations.py`'s header names, `<k>` the next free number in this build, says so in its summary, and does not
commit it.

## The units

**Writer groups and build order**, by the `order` verb: units 1 and 11 (order 1), units 2, 3 and 4 (order 2), units
5 and 6 (order 3), units 7 and 8 (order 4), units 9 and 10 (order 5).

- **TOOL-dGroundRules-1** — Items 1. S1, S2, S3 and the summary/usage list of S8: the file, the kit, the catalogue
  and its shape audit. Seen red on a planted empty value for each never-empty set-valued key, on a set-valued key
  with no `empty`, and on a planted new key with no summary.
- **TOOL-dGroundRules-11** — Items 11. The catalogue's `direction` field: every loop bound and deadline key declares
  that raising it is a loosening; seen red on a planted loop bound with no declared direction. Name the population
  rule (which catalogue rows are loop bounds or deadlines) so it is derived, never typed.
- **TOOL-dGroundRules-2** — Items 2. S4: the reader, at the landed revision, parsed and never sourced.
- **TOOL-dGroundRules-3** — Items 3. The resolution order inside `resolve`: file, then preset (a no-op branch until
  dKeptSession adds presets, stated as such), then the catalogue default with its reason.
- **TOOL-dGroundRules-4** — Items 4. S5 and `policy-file.on-invalid`: each failure class planted with its outcome,
  and the strict-preset plant the clause states.
- **TOOL-dGroundRules-5** — Items 5. S6: the mirror, its landing regeneration, the parity leg red on a hand-edited
  mirror, the hook arm, and a stale or absent mirror read as `policy-file.on-invalid` says.
- **TOOL-dGroundRules-6** — Items 6. The minimal guard over S7: the one admitted write shape and every refused shape
  the clause lists, each a criterion. Name the hook seam it wires into.
- **TOOL-dGroundRules-7** — Items 7. The legacy-home list of S8, derived by query from the files it guards, each row
  marked owner policy or mechanic as the clause lists.
- **TOOL-dGroundRules-8** — Items 8. The reader-coverage arm: a key whose Owner build has landed with no reader is
  red; its landed set derived from history.
- **TOOL-dGroundRules-9** — Items 9. `budgets.enforce`, `budgets.pinned` and `budgets.*`: every cap the caps research
  lists, its consumer re-pointed to the reader, `template-size-limits.txt` kept as a read legacy home.
- **TOOL-dGroundRules-10** — Items 10. `runtime.agents-in-flight`: the rendered harness settings, agent-cap's
  retirements and re-pointing, `.agent-cap.conf` as a lowering-only legacy home, every fixture case the clause lists.
