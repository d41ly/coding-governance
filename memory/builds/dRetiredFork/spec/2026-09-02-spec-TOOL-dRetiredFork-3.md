# TOOL-dRetiredFork-3 — a present-but-unparseable build README header stops reading as absent

**Status:** OPEN · rev-3 · 2026-09-02 · node d · Tier-2 · base b0108f13 · streams tooling · order 1 · ratified 2026-09-02

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round1.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-1-18-and-depl-1-7-spec-audit-round2.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-4 DEPL-dRetiredFork-5 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 TOOL-dRetiredFork-1 TOOL-dRetiredFork-2 TOOL-dRetiredFork-4 TOOL-dRetiredFork-5 TOOL-dRetiredFork-6 TOOL-dRetiredFork-7 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-10 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-18 |
| [2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md](../reviews/2026-09-02-review-TOOL-dRetiredFork-3-21-and-depl-1-9-spec-audit-round3.md) | spec-audit | DEPL-dRetiredFork-1 DEPL-dRetiredFork-2 DEPL-dRetiredFork-3 DEPL-dRetiredFork-6 DEPL-dRetiredFork-7 DEPL-dRetiredFork-8 DEPL-dRetiredFork-9 TOOL-dRetiredFork-5 TOOL-dRetiredFork-8 TOOL-dRetiredFork-9 TOOL-dRetiredFork-11 TOOL-dRetiredFork-12 TOOL-dRetiredFork-13 TOOL-dRetiredFork-14 TOOL-dRetiredFork-15 TOOL-dRetiredFork-16 TOOL-dRetiredFork-17 TOOL-dRetiredFork-19 TOOL-dRetiredFork-20 TOOL-dRetiredFork-21 |

<!-- /gen:spec-records -->

## 1. Goal

Absorb the `StaleHeader` mechanism NicoCares carries as `nc carve-out 9/20`, first applied at
`PKG-aMendedMetronome-1` and re-applied by hand at the 2.2 to 2.29 swap. gov's
`gen_build_index.py` treats a build README header that is PRESENT and unparseable exactly like one
that is ABSENT, so a corrupted header silently becomes a missing header and the index regenerates
around it. Those are different animals and the adopter has been paying for the distinction alone.

## 2. Scope (IN)

- **S1** — A `StaleHeader` exception class in `tools/memory-tree/gen_build_index.py`, raised by the
  parser when a header region exists and does not conform.
- **S2** — The raise site in the parser, and the handler at `collect()` that reports the file and
  the offending region rather than proceeding.
- **S3** — A shrink-only header waiver registry at `memory/project/stale-header-waiver.txt`,
  consulted at `collect()` and NOT inside the parser. The parser decides conformance; the caller
  decides tolerance, which is the seam NicoCares' own comment argues for.
- **S4** — The waiver file ships to adopters with its rows and NO entries, and the memory-tree
  `kit.toml` gains the matching `[[hole]]` with a discharge probe, because a waiver list measured on
  gov's corpus is vacuous in any other tree.
- **S5** — Arms: a conforming header parses; a corrupt header raises and is reported; a corrupt
  header with a waiver row is tolerated and SAYS so; an empty waiver file is not an error.
- **S6** — Add `F:stale-header-waiver.txt` to check 3's registry whitelist `case` in
  `tools/memory-tree/check-memory-hygiene.sh`, IN THE SAME COMMIT. Check 3's population comes from
  `git ls-files` and its whitelist is a hardcoded case naming nine registries, so a new tracked file
  under `memory/project/` reds this unit's own named gate on landing. `readme-contract.txt` was
  added with its own case line, which settles that this is a required scope item and not an
  inference. `TOOL-dRetiredFork-15` S2's `PROJECT_REGISTRY_EXTRA` is the durable answer and lands
  at order 5, three steps after this unit.
- **S7** — Bump `KIT_MEMORY_TREE_VERSION` and every paired marker.

## 3. Non-goals (OUT)

- Repairing any corrupt header this newly surfaces in gov's own tree. If the arm reds on a real
  build README, that repair is its own commit and its own record.
- Extending the same distinction to the spec status header. Check 8 already grades that surface and
  a second mechanism there is a separate unit.

## 4. Design

### Data model

`StaleHeader(Exception)` carries the path and the raw region text. The waiver registry is one
`<path>` per row with a reason after whitespace, matching the shape of the nine registries already
under `memory/project/`.

### Migration

The registry ships empty in gov and in every adopter, so the mechanism is inert on the day it lands
and becomes live only when a header actually corrupts. NicoCares deletes its carve-out and adds
whatever rows its own corpus needs; that is a data edit in its tree, not a code edit in a kit.

### Alternatives rejected

Consulting the waiver inside the parser. NicoCares' own comment rejects this and is right: a parser
that knows about tolerance cannot be reused by a caller that wants strictness, and the two readers
of this parser want different answers.

## 5. Production-readiness checklist

- security — N/A. No new input reaches a shell, and the registry is read as data.
- perf / scale — the waiver is read ONCE per `collect()`, not per file. Measured requirement, not a
  preference: the per-build subprocess class is already an open row at `TOOL-aGradedDoorway-5`.
- a11y — N/A. No user surface.
- i18n — N/A.
- error / empty / loading states — an empty registry is the expected state and must not be an error;
  a missing registry is a refusal, because a file nobody created is a decision nobody made.
- observability — the run names how many headers were tolerated by waiver on every invocation, so a
  growing tolerance is visible without reading the file.
- risks — a waiver row that outlives its header silently widens tolerance. Mitigated by the
  shrink-only rule and a staleness arm that reds on a row naming a path the tree no longer tracks.
- testing + left-shift gates — S5's four arms, each observed RED before wiring.
- migration / rollback — the mechanism is additive and inert with an empty registry; reverting is
  deleting the class, the handler and the file.
- user docs — one paragraph in `tools/memory-tree/README.md` naming the registry and its shrink-only
  rule.

## 6. Acceptance criteria

- **AC1** — When a build README's header region is present and malformed, `python3
  tools/memory-tree/gen_build_index.py --check` names that file and its region and exits non-zero;
  before the change the same tree exited `0`.
- **AC2** — When that path carries a row in `memory/project/stale-header-waiver.txt`, the same
  command exits `0` and prints the tolerated count.
- **AC3** — When a waiver row names a path the tree does not track, the command exits non-zero
  naming the stale row. Observed via `python3 tools/memory-tree/gen_build_index.py --check`.
- **AC4** — When the registry is absent, the command REFUSES rather than defaulting to empty. Observed via `python3 tools/memory-tree/gen_build_index.py --check`.
- **AC5** — When no header is malformed, `--check` output differs from the pre-change run by
  EXACTLY the unconditional `0 tolerated` line §5 requires and F2 resolves, and by nothing else.
  rev-1 demanded byte-identity, which that line makes impossible.
- **AC6** — When the kit is adopted into a fresh target, the waiver file arrives with its header
  and no entries, and the memory-tree `kit.toml` `[[hole]]` discharge probe reports it UNARMED
  rather than passing silently. This is S4, which rev-1 scoped and never observed.
- **AC7** — `bash tools/memory-tree/check-memory-hygiene.sh` exits `0` with check 3 reporting no
  unexpected entry for `memory/project/stale-header-waiver.txt`.
- **AC8** — `bash tools/check-kit-versions.sh` exits `0` after the bump.

## 7. Gates

`memory hygiene` · `build README slot contract` · `build-index selftest` · `kit version markers` ·
`dead-path carriers (deleted files still named)` for the new registry's rows.

## 8. Open questions

- **F1 — does the registry key on the build README path, or on the build slug?** Path is the shape
  every sibling registry uses and is what the staleness arm can grade against `git ls-files`. Slug
  survives a rename of the README, which does not happen. Recommendation: path, for consistency with
  `legacy-files.txt` and `readme-contract.txt`.
- **F2 — does an empty registry print a line?** The house rule is that a clean run printing nothing
  is indistinguishable from a check that never ran, so it should. Recommendation: print
  `0 tolerated`, unconditionally.

**RESOLVED (owner, 2026-09-02): every fork above is settled by its own stated Recommendation.** The owner ratified them as written on 2026-09-02 with the instruction to fold the recommendations. No fork is resolved against its recommendation and none by silence; where a later measurement contradicts a ratified pick, that is a new fork with a new id.

## 9. Revision log

- rev-1 · 2026-09-02 · initial draft, authored from the dRetiredFork classification of `nc carve-out
  9/20` against `tools/memory-tree/gen_build_index.py` at b0108f13.
- rev-2 · 2026-09-02 · folded spec-audit round 1, findings H7, M1, M2 and M8. H7: the new registry file reds check 3 on
  landing, because that whitelist is a hardcoded case; S6 now edits it in the same commit and AC7
  observes it. M1: AC5 demanded byte-identity while §5 requires an unconditional `0 tolerated` line,
  and the two cannot both hold. M2: S4's adopter-facing half had no criterion; AC6 is it. M8: §10
  cited a probe run for the install-prefix question, not this unit's.
- rev-3 · 2026-09-02 · folded spec-audit round 2, findings 17 and 18. 17: the M8 fold corrected §10's probe
  QUERY and left the rev-1 terms line, which is the half M7 regrounding actually re-runs. 18: §4
  said five registries where the tree holds nine and S6 edits a whitelist with nine arms.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "distinguish a present-but-unparseable record header from
an absent one"` — rev-1 recorded the probe run for a DIFFERENT unit's question, the install-prefix
one, which is a citation that cannot support this unit. No seam covers a parse-failure distinction,
so the closest existing pattern is the registry family under `memory/project/`, which
this unit extends rather than replaces — `legacy-files.txt` read into `LEGACY_SET` at
`tools/memory-tree/check-memory-hygiene.sh` is the shape copied, including its shrink-only rule and
its staleness arm.

Recall terms used: `StaleHeader`, `header`, `parse failure`, `waiver`, `registry`, `shrink-only`,
`gen_build_index`, `collect`, `build README`, `tolerated`, `memory/project`, `check 3`.

*(rev-3 replaces the rev-1 terms, which were the install-prefix unit's and which BUILD-METHOD M7
regrounding would have re-run against the wrong question. Superseded terms, for the record:*
`carve-out`, `install-prefix`, `KIT_REL`, `carried`, `relocate`, `rung`,
`adopter`, `divergence`, `repath`, `govkit`, `receipt`, `unattributed`, `derive`, `prefix`.
