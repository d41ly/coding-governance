# TOOL-aBlindedTrial-8 — a spec's §7 leg line must name every leg its files-touched trips

**Status:** INPROGRESS · rev-1 · 2026-09-21 · node a · Tier-2 · base 0e61932d · streams tooling · order 1 · ratified 2026-09-21

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`tools/check-spec-tokens.py` gains a `guards` arm: for a live spec dated at or after a new cutoff, every
leg in `tools/gate-legs.json` whose `guard` any path under the spec's §4 `### Files touched` sub-head
trips must be named on the §7 leg line, else a finding names the spec, the leg and the path. Unit 4 of
this build omitted `scratch-guard self-test` while editing `scratch-guard.js`, and only the closing
review found it — the class is machine-derivable from two files that already exist.

## 2. Scope (IN)

- S1 — a new cutoff key `SPEC_GUARD_LEGS_CUTOFF` in `.memory-tree.conf` (and blank in
  `.memory-tree.conf.example`), read the way `SPEC_DIRECT_CUTOFF` is (`check-spec-tokens.py:104,
  :184`); blank is OFF; the value set at landing is the day after the setting commit, per the conf's
  relation rule. Observed by AC1.
- S2 — the arm reads the §4 sub-head spelled either `### Files touched` or `### Files touched (estimate)`,
  takes its backticked tokens through `check_path_shaped` (`:215-232`), and joins each against every
  manifest leg carrying a `guard` (`.get`, since fixture manifests omit it) with git-pathspec semantics:
  `p == g or p.startswith(g.rstrip('/') + '/')`. Observed by AC2, AC3.
- S3 — one-segment guards (`tools/`, `memory/`) are EXCLUDED from the join and reported as near-misses
  under `--list`: eleven legs carry the bare `tools/` guard, so naming them adds no information and
  buries the specific one; the header states the exclusion. Observed by AC4.
- S4 — a hit is `(spec, 'guards', '<leg> <- <path>', why)`: the composite token keeps a guards hit from
  being swallowed by an existing `[leg]` waiver row (`spec-token-waivers.txt` is keyed by token alone).
  The report line and the summary follow `:429-435`; the refusal-on-None cutoff pattern at `:291` is
  extended, not duplicated. Observed by AC2, AC5.
- S5 — `check-spec-tokens.test.sh` gains the arms, each observed RED against the pre-edit checker:
  a post-cutoff spec touching a two-segment-guarded path with the leg absent (hit) and present (clean),
  a one-segment guard (near-miss, no hit), a pre-cutoff spec (silent), a blank cutoff (announced OFF), the
  short sub-head spelling, a waiver row with the composite token; `FLOOR_ASSERTIONS` raised per arm with
  the RAISED comment. Observed by AC2–AC6.
- S6 — `tools/memory-tree/SPEC-TEMPLATE.template.md` §7 gains one paragraph naming the rule and the key
  (spelling `{{TOOL_ROOT}}gate-legs.json`); `memory/TEMPLATE-SPEC.md` re-rendered; `memory-tree@` 2.80 →
  2.81 in every carrier and render; the checker's header "WHAT THIS DOES NOT CHECK" block gains the
  arm's limits. Observed by AC7.

## 3. Non-goals (OUT)

- Paths named in §4 prose outside the sub-head are not read; the sub-head is the declared write set.
- No change to which legs carry a guard, and no change to `tools/gate-legs.json`.
- The checker stays a repo-root tool (a govkit registry exemption); adopters receive only the
  template paragraph and the blank example key, which the paragraph says.
- Hygiene check 12 is untouched: it grades §7 as a non-empty canon heading and parses no leg line.

### Edges

- **consumes-from** external — `tools/gate-legs.json`'s `guard` field and `check_path_shaped`, both
  landed; the arm reads them, never redefines them.

## 4. Design

### Inventory

- `SPEC_GUARD_LEGS_CUTOFF` — conf key, blank = OFF.
- `extract_files_touched(text)` — the sub-head's path-shaped tokens; leads with `extract`.
- `derive_guarded_legs(manifest)` — `(name, guards)` pairs with one-segment guards split out; leads with
  `derive`.
- hit kind `guards`, token `<leg> <- <path>`.

### Files touched (estimate)

`tools/check-spec-tokens.py` · `tools/check-spec-tokens.test.sh` · `.memory-tree.conf` ·
`tools/memory-tree/.memory-tree.conf.example` · `tools/memory-tree/SPEC-TEMPLATE.template.md` ·
`memory/TEMPLATE-SPEC.md` · every `memory-tree@` carrier and render · `memory/map/features/` dossier for
the checker · `memory/map/generated/symbols.json` (regen).

### Alternatives rejected

- Bare `startswith` over guards: over-matches an exact-file guard (`tools/x.sh` would trip on
  `tools/x.sh.bak`).
- Joining every guard including `tools/`: eleven names on every kit spec's leg line, the signal lost in
  boilerplate; the bar already runs those legs on the guard, the leg line is for what a reader must
  know.
- A hygiene arm instead of a spec-tokens arm: hygiene never parses the leg line; spec-tokens already
  joins it to the manifest.

## 5. Production-readiness checklist

- security — N/A
- perf / scale — one manifest read and a sub-head scan per live spec; the leg's ceiling is 60 s at 1 s
- error / empty / loading states — blank cutoff announces OFF; a manifest leg without `guard` is
  skipped; a spec without the sub-head is silent (nothing declared, nothing joined — stated in the header)
- observability — the `[guards]` report row and the `--list` near-miss rows
- risks — the cutoff relation refuses a value not strictly past the setting day; symbols.json freshness;
  the nine memory-tree carriers
- testing — the checker's own suite, run by hand and on demand
- migration — none; the arm binds only specs dated after the cutoff
- user docs — the template paragraph

## 6. Acceptance criteria

- **AC1** — When `.memory-tree.conf` sets `SPEC_GUARD_LEGS_CUTOFF` blank, `python tools/check-spec-tokens.py`
  prints an announced `guards` OFF line and exits as today.
  Red when: a blank cutoff silently skips or reds.
- **AC2** — When a fixture spec dated after the cutoff lists `tools/hooks/scratch-guard.js` under its
  `### Files touched (estimate)` and its §7 line omits `scratch-guard self-test`, `check-spec-tokens.py`
  exits 1 with a `[guards]` row naming the spec, the leg and the path; with the leg named it exits 0.
  Red when: the omission passes, or the named leg still hits.
- **AC3** — When the fixture spells the sub-head `### Files touched` without the parenthetical, AC2
  holds unchanged.
  Red when: the short spelling is silently skipped.
- **AC4** — When a fixture spec lists a path under a one-segment guard only, the checker exits 0 and
  `--list` prints a `NEAR` row for it.
  Red when: a bare `tools/` guard produces a hit.
- **AC5** — When `spec-token-waivers.txt` carries the row `<leg> <- <path>` for AC2's hit, the checker
  exits 0 and reports the waiver as consumed; a bare `[leg]` row for the same leg does not consume it.
  Red when: a leg-only waiver swallows a guards hit.
- **AC6** — When a fixture spec is dated before the cutoff, `check-spec-tokens.py` prints no `[guards]`
  row for it and its summary says how many specs the arm graded.
  Red when: a grandfathered spec reds.
- **AC7** — When `bash tools/check-kit-versions.sh` runs it exits 0 with every `memory-tree@` marker at
  2.81, and `grep -c SPEC_GUARD_LEGS_CUTOFF memory/TEMPLATE-SPEC.md` is ≥ 1 after the render.
  Red when: a render or a marker is left behind.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `kit/dogfood doc parity` · `kit version markers` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `install-prefix (shipped surface)` · `kickoff-manifest ratchet`

New arm: `tools/check-spec-tokens.test.sh` · a post-cutoff fixture spec with and without the guarded leg named · `FLOOR_ASSERTIONS` raised per arm

## 8. Open questions

- **F1 — join every guard, or only guards deeper than one segment.** RESOLVED (agent, 2026-09-21,
  delegated): deeper than one segment, reported as near-miss otherwise. Eleven legs guard bare
  `tools/`; a rule that owes eleven names per kit spec is obeyed by paste and read by nobody.

## 9. Revision log

- rev-1 · 2026-09-21 · initial draft from the scout of the checker, its suite and the manifest at 0e61932d.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "join a spec's declared write set against gate guards"`
named `check-spec-tokens.py`'s own leg-line join as the nearest symbol and nothing closer. The seam is
that join (`:275` rows, the loop over the leg line) and `check_path_shaped`; the arm adds a second
population to the same walk. Recall terms used: spec tokens leg line gate-legs guard files touched
cutoff waiver composite token near miss self-test scratch-guard closing review F7.
