# TOOL-cMendedVintage-2 — gate-lint stops seeding into the memory tree

**Status:** CLOSED · rev-2 · 2026-09-16 · node c · Tier-2 · base 859daa67 · streams tooling · order 12

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-16-build-TOOL-cMendedVintage-2-acceptance-ledger.md](../build/2026-09-16-build-TOOL-cMendedVintage-2-acceptance-ledger.md) | journal | — |
| [2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md](../prompts/2026-09-16-prompt-DEPL-cMendedVintage-1-1-spec-briefs.md) | journal | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 TOOL-cMendedVintage-1 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 |
| [2026-09-16-prompt-TOOL-cMendedVintage-2-2-build-brief.md](../prompts/2026-09-16-prompt-TOOL-cMendedVintage-2-2-build-brief.md) | journal | — |
| [2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md](../reviews/2026-09-16-review-DEPL-cMendedVintage-1-spec-audit-round1.md) | spec-audit | TOOL-cMendedVintage-1 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 |

<!-- /gen:spec-records -->

## 1. Goal

`tools/gate-lint/kit.toml` ships a `seed` rule whose destination is
`{memory_root}/project/substitution-fed-loops.txt`, and check 3 of `check-memory-hygiene.sh` admits
only a closed set of names under `{memory_root}/project/`. So gov writes a file into every adopter's
memory tree that the adopter's own hygiene gate then refuses, and an adopter running a FORKED copy of
that checker cannot be reached by widening gov's case list at all. Withdraw the seed, make the
scanner's registry positional optional, and drop the registry path from the shipped leg argv, so a
target receives a leg that runs with no declaration instead of a file its gate rejects.

## 2. Scope (IN)

- **S1** `tools/gate-lint/sh_hygiene.py` makes the registry positional OPTIONAL. With no positional
  the run grades against an empty declaration, which is byte-identically what the shipped empty
  template produces and what that template's header documents as the correct first install. Observed
  by AC1.
- **S2** The same file keeps a REFUSAL for a positional that was supplied and does not resolve to a
  file. Absent and unreadable are different states: the first is a posture, the second is a typo, and
  collapsing them would let a mis-spelled registry path grade silently against nothing. Observed by
  AC2.
- **S3** The declaration resolution moves into one function taking the optional argument and
  returning the `(declared, malformed)` pair or a refusal, so the three cases are assertable without
  a tree scan. `FLOOR_ASSERTIONS` rises by the number of arms added. Observed by AC1.
- **S4** `tools/gate-lint/kit.toml` loses the `role = "seed"` file rule, and
  `tools/gate-lint/substitution-fed-loops.template.txt` is deleted. With the rule gone the surviving
  `include = "**"` rule would claim the template as an `engine` file and ship a template for a file
  nothing writes. Observed by AC5.
- **S5** The template's first-install prose — what a row is, why the key is the path plus the
  delimiter and never a line number, and how to fill the file from the first red run — folds into
  `tools/gate-lint/README.md`. The fold introduces no new `tools/` literal, because
  `tools/gate-lint/README.md` carries a carried-prefix ratchet row that may fall and may not rise.
  Observed by AC5.
- **S6** The `[[gate_leg]]` named `shell hygiene (a loop fed by a command substitution)` in
  `tools/gate-lint/kit.toml` loses its third argv element. S4 and S6 land in ONE commit: dropping the
  seed while the argv still names the path puts the leg back into `silenced_legs`, which is `apply`
  exit 1 at every adopter and no recorded coverage. Observed by AC4.
- **S7** gov's own `tools/gate-legs.json` row and gov's own
  `memory/project/substitution-fed-loops.txt` are UNCHANGED. Selfcheck arm 7h compares leg NAME and
  SUBJECT and never argv, so the descriptor and the manifest may differ in that element without
  disagreeing about a fact. Observed by AC3.

## 3. Non-goals (OUT)

- No widening of `check-memory-hygiene.sh`'s check 3 case list, and no new
  `PROJECT_REGISTRY_EXTRA` default. A widening reaches an adopter only on their next
  `update --kits memory-tree`, and reaches a FORKED checker never; inCMS's is forked.
- No move of the registry to a path under `tools/`. A kit file names nothing outside itself by
  literal, and a carried-prefix destination is what the install-prefix ban exists to stop.
- No change to `tools/gate-lint/ps-hygiene.py`, which is on no leg anywhere and stays that way.
- No version bump. gate-lint declares `version_from = { none = … }`, so the kit has no version
  constant to move and `check-kit-versions.sh` grades it by its sentinel path.
- No removal of gov's own registry rows. This repo's 18 declared sites are this repo's declaration
  and its own leg still names the file.

### Edges

- **hands-off** `DEPL-cMendedVintage-9` — this unit drains the ONE live destination that unit's new
  refusal grades, so that unit's arm observes a staged break rather than the tree and owes an
  explicit population count for its liveness.
- **hands-off** external — the two live adopters already hold a copied
  `memory/project/substitution-fed-loops.txt` whose receipt row is role `seed`. They keep the file
  and lose the leg's argument; the migration note is `DEPL-cMendedVintage-9`'s scope.
- **consumes-from** external — nothing. The three edits are self-contained and no unit in this build
  precedes them.

## 4. Design

### Data model

The scanner's contract becomes: argv 1 is an OPTIONAL registry path, argv 2 an optional root. Three
declaration states, and the middle one is what this unit adds.

| positional | resolution | exit behaviour |
|---|---|---|
| absent | `({}, [])` — no declaration | every measured site is reported as undeclared |
| a path that is a file | `read_registry(path)` | today's behaviour, unchanged |
| a path that is not a file | refusal | exit 2 naming the path |

The empty-population refusal at `sh_hygiene.py:437` is untouched and is this scanner's liveness
assertion: a run that graded no tracked `*.sh` still exits 2 rather than reporting the zero a clean
tree reports.

### Inventory

Minted by this unit: one function name in `tools/gate-lint/sh_hygiene.py` for the declaration
resolution, and nothing else. No new file, no new flag, no new descriptor key. This repo declares
naming cells for identifiers; the new name is a Python function in a kit engine and is graded by the
`python` cell, so it is checked with `python3 tools/lexicon/lexicon.py --suggest <name> --as <cell>`
before it is written.

Deleted by this unit: `tools/gate-lint/substitution-fed-loops.template.txt`, one `[[files]]` table,
and one argv element.

### Migration

An adopter who already took the seed keeps the file they own. After this unit their leg runs with no
argument, so their existing rows stop being compared and every site in their tree is reported as
undeclared on the first run — which is a RED leg, not a silent one. They restore comparison by
putting the path back into their own copy of the leg argv, which is theirs to edit because the leg
row lives in their `tools/gate-legs.json`. That is the residue `DEPL-cMendedVintage-9` records for
the runbook.

### Alternatives rejected

Widening check 3's case list with the registry's name: measured against the two live adopters, it
reaches neither. One takes gov's memory-tree kit and would receive the widened case only on a later
`update --kits memory-tree`; the other runs a FORK of the checker, which no gov edit reaches at all.

Moving the registry under `tools/`: closed by the carried-prefix ban. The destination would be a
`tools/`-rooted literal inside a kit descriptor, which is the class `tools/check-install-prefix.sh`
counts and refuses to let rise.

Keeping the seed and making check 3 silent about it: an admitted-but-unreachable name is a third
answer to the question that case list closes, and check 3's own comment records that a widening case
placed where it can accept anything stopped the check grading at all.

### Files touched (estimate)

| Path | Change |
|---|---|
| `tools/gate-lint/sh_hygiene.py` | optional positional, the resolution function, new selftest arms, floor raised |
| `tools/gate-lint/kit.toml` | one `[[files]]` table deleted, one argv element dropped |
| `tools/gate-lint/README.md` | the template's first-install prose folded in |
| `tools/gate-lint/substitution-fed-loops.template.txt` | deleted |

## 5. Production-readiness checklist

- security — no write path changes. The scanner reads tracked files and a declaration; withdrawing a
  seed removes bytes gov writes into a target rather than adding any.
- perf / scale — unchanged. The scan walks the same population; the declaration resolution is one
  file read or none.
- error / empty / loading states — the three declaration states are the section 4 table. The
  empty-population refusal stays, so a scan that graded nothing is still a refusal.
- observability — the scanner already prints its site and row totals on every run, green included,
  and a run with no declaration prints a row total of zero rather than omitting the line.
- risks — the coupling between S4 and S6 is the one real hazard: either edit alone reds `apply` at
  every adopter through `silenced_legs`. They are one commit for that reason, and AC4 observes the
  pair.
- testing — AC1 and AC2 are `--selftest` and direct invocations of the scanner. AC4 is `selfcheck`.
  No new suite; three new assertions inside the existing self-test.
- migration — section 4's Migration paragraph. An adopter keeps their file and loses the comparison
  until they put the path back into their own leg row.
- user docs — `tools/gate-lint/README.md` gains the first-install prose and its usage block drops the
  mandatory positional. That is the kit's own page and there is no other.

## 6. Acceptance criteria

- **AC1** — When `python3 tools/gate-lint/sh_hygiene.py --selftest` runs, it prints `PASS` with an
  assertion count at or above the raised `FLOOR_ASSERTIONS`, and the printed arms include one for an
  absent positional resolving to an empty declaration.
  Red when: the positional stays mandatory, so the absent case cannot be asserted at all and the
  count stays at the floor the file ships with.
  figure: DERIVED — the count is the number the self-test prints, not a literal this spec pins.
- **AC2** — When `python3 tools/gate-lint/sh_hygiene.py <scratch>/nosuch.txt <scratch>` runs against
  a scratch root holding one tracked-looking `*.sh`, it exits 2 and names the unresolved path.
  Red when: S2's refusal was deleted along with the mandatory positional, so a mis-spelled registry
  path grades against an empty declaration and reports every site as new.
  fixture: a scratch tree under this run's scratch root; the observation needs a root with at least
  one `*.sh` so the empty-population refusal is not what answers.
- **AC3** — When `python3 tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt`
  runs in this repo, it exits 0 and reports the same declared-site total it reports at BASE.
  Red when: gov's own leg row or its own registry was edited alongside the descriptor, so this
  repo's 18 declared sites stop being compared.
  figure: DERIVED — the total is the scanner's own printed figure at both revisions.
- **AC4** — When `python tools/govkit/govkit.py selfcheck` runs, it exits 0 and its `gate legs:` note
  reports zero legs naming a path no rule produces.
  Red when: S4 landed without S6 or S6 without S4, in which case the surviving half is either a leg
  argv naming a path no rule writes or a seed rule nothing reads.
- **AC5** — When `git grep -n substitution-fed-loops -- tools/gate-lint/` runs, it returns no hit in
  `tools/gate-lint/kit.toml`, the template file is absent from `git ls-files -- tools/gate-lint/`,
  and `tools/gate-lint/README.md` carries the first-install prose.
  Red when: the template is deleted and its prose is not folded, leaving an adopter with a registry
  they may create and no instruction for filling it.

## 7. Gates

`govkit selfcheck` · `shell hygiene (a loop fed by a command substitution)` · `shell-hygiene selftest` · `memory hygiene` · `install-prefix (shipped surface)` · `kit placeholders (a declared token its adopter substitutes)` · `testsuite counts (every bar self-test prints one)`

New arm: `tools/gate-lint/sh_hygiene.py` `--selftest` · three assertions over the declaration
resolution — absent, present, named-but-unresolvable · `FLOOR_ASSERTIONS` 24 to 27.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-09-16 · initial draft.
- rev-2 · 2026-09-16 · the build pass adds `memory/map/features/gate-lint.md` to the files touched.
  Section 4's Inventory listed no dossier and section 2 named none, but the dossier claims the glob
  `tools/gate-lint/*` and three of its paragraphs assert the seed rule ships the registry — claims
  this unit makes false. Refreshing them is the §1 Definition of Done's "dossier prose refreshed on
  touch", not new scope: no claim key moves, and `memory/map/generated/` names the deleted template
  nowhere, so nothing is regenerated. Also recorded here because section 5's testing line did not:
  a CLOSED Tier-2 spec dated after `ACCEPTANCE_LEDGER_CUTOFF` owes an acceptance ledger under the
  build folder, so this unit writes one.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "gate lint seed registry written into the memory tree"`
named `sh_hygiene.scan_file` as the gate-lint affordance seam and `check_registry` in the same file,
and reported `.sh` as an unscanned layer, so the descriptor and adopter halves of this change are
invisible to the map by construction. The seam this unit extends is therefore read from source:
`main()` in `tools/gate-lint/sh_hygiene.py`, whose registry branch at the `is_file()` test is the
one predicate this unit splits into three states, and `read_registry` beside it, which is reused
unchanged. The withdrawal half has no code seam at all — it is the deletion of one `[[files]]` table
in `tools/gate-lint/kit.toml` and one element of a `[[gate_leg]]` argv. The recall probe returned the
record that settles why the alternatives lose: the gate-lint dossier at `memory/map/features/gate-lint.md`
records that the seed rule was added because the leg's argv named a path no rule wrote, and
`TOOL-aLeakedHandle-1`'s closing review F1 is where that argv-versus-rule coupling was measured.

Recall terms used: `--terms "gate-lint sh_hygiene seed role registry memory project whitelist
check-memory-hygiene descriptor destination silenced_legs adopter apply"`, with the question "why
does the gate-lint kit ship a seed registry under the memory tree and what refuses it there".
