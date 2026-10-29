# TOOL-dMindYourWords-5 — a reasoned site suppression, recorded and counted, as the owner's fallback

**Status:** OPEN · rev-1 · 2026-10-29 · node d · Tier-2 · base ccd1292e · streams tooling · order 6 · advances TOOL-dMindYourWords-18

**Carries:** cl-dClosedLoop-0266@db50d898 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-agent-ledger.md) | journal | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-reuse-scout-a.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 |
| [2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md](../build/2026-10-29-build-TOOL-dMindYourWords-1-spec-stage-returns.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-fix-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 |
| [2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md](../prompts/2026-10-29-prompt-TOOL-dMindYourWords-1-spec-brief.md) | research | TOOL-dMindYourWords-1 TOOL-dMindYourWords-2 TOOL-dMindYourWords-3 TOOL-dMindYourWords-4 TOOL-dMindYourWords-6 TOOL-dMindYourWords-7 TOOL-dMindYourWords-8 TOOL-dMindYourWords-9 TOOL-dMindYourWords-10 TOOL-dMindYourWords-11 TOOL-dMindYourWords-12 TOOL-dMindYourWords-13 TOOL-dMindYourWords-14 TOOL-dMindYourWords-15 TOOL-dMindYourWords-16 TOOL-dMindYourWords-17 |

<!-- /gen:spec-records -->

## 1. Goal

A reasoned site suppression as the owner's counted fallback (lexicon review `[forced]` item 4). Today a
waiver row is a bare name with an optional reason: `load_waivers` (`tools/lexicon/lexicon.py:2324`)
keeps `parts[1] if len(parts) > 1 else ""`, and the verdict matches `o.text in waivers` (`:3049`), so
one row exempts that name in every file (gap-lex-06). This unit keys each row to one definition site,
requires its reason, refuses a row whose commit carries no write-path record, counts and prints every
suppression on green and red, and writes the three outcomes an uncovered forced name routes to into the
refusal, suppression never first unless `lexicon.forced` names it as the route.

## 2. Scope (IN)

Build-run precondition: TOOL-dMindYourWords-12's context accessor, for a method's qualified name, and
TOOL-dMindYourWords-11's record reader, for provenance, are built first; both order before this unit.

- **S1** — The site key (I3). `Offender` gains the slot `site`, set once in `measure_pass`:
  `<repo-relative path>::<qualified name>`, the qualified name read from `read_definition_context`
  (TOOL-dMindYourWords-12, I5) for a `python-ast` definition, so a method keys as
  `<path>::<Class>.<name>`, and the bare name for every other extension. It is the code record's
  definition key (TOOL-dTotalRecall-8 §4 "The derivation"), one spelling. Observed by AC1, AC2.
- **S2** — The registry grammar. Each row of `lexicon-verb-waivers.txt` and `lexicon-suffix-waivers.txt`
  is `<site key><whitespace><reason>`. `load_waivers(kit, kind)` returns `(rows, problems)`, `rows`
  mapping each site key to `(reason, lineno)`: a row whose reason is empty after stripping is an `EMPTY
  REASON` problem naming the file and line; a row whose key carries no `::`, or an empty path or name
  either side of it, is a `MALFORMED SUPPRESSION`; a key written twice is a `DUPLICATE SUPPRESSION`
  naming both lines. Each problem reds, as `STALE WAIVERS` does today. Observed by AC3, AC4.
- **S3** — Matching. An offender is suppressed when its `site` is a row's key, and it takes
  `Offender.grade` `forced` (I1, TOOL-dMindYourWords-1), so it leaves the debt count. A key no
  offender's `site` matches still reds as `STALE WAIVERS`. The four readers of the old key move to
  `site`: the split in `measure_pass` (`lexicon.py:3046-3053`), `--list` (`:3270`, its prefix
  `suppressed`), and the waived-unruled count of `run_expand` (`:4072-4074`). Observed by AC1, AC2, AC6.
- **S4** — Provenance. `check_suppression_provenance(root, kit, rows)` runs one `git blame --porcelain`
  per registry holding a row, and for each row's commit asks `read_vocabulary_record(root,
  ("unit.lexicon.suppressions",), rev=<commit>)` (TOOL-dMindYourWords-11, I11): a commit that adds no
  such record leaves its rows `SUPPRESSION WITHOUT PROVENANCE`, naming the file, the line, the site and
  the commit. A row git blames to no commit, staged or in the working tree, is admitted only when the
  index adds such a record (`rev` `index`). A registry with no rows spawns nothing. Observed by AC5.
- **S5** — The count. `check_pass` prints, after the P1 and P2 lines and on green as on red,
  `lexicon: suppressed=<n> (verb=<a>, suffix=<b>)`, and `--measure` prints the same line. Observed by
  AC9.
- **S6** — The owner item's three outcomes. Where `check_pass` refuses a P1 or P2 offender, it prints the
  three ways out: rename it; add a custom pack row, if a host forces it (TOOL-dMindYourWords-8's
  `PACKS:`); or suppress the site with a reason, in a commit carrying its record. The order is read from
  `read_policy_value("lexicon.forced", root)` (I7, TOOL-dMindYourWords-1): under `verified` and
  `by-name` suppression is printed last, never the default; under `by-annotation`, the value whose
  route is a reasoned annotation per site, it is printed first. Where unit 1's `POLICY_DEFAULTS`
  (TOOL-dMindYourWords-1 §4 "The policy read") lacks a row for `lexicon.forced` or `lexicon.at-commit`,
  this unit adds it at the catalogue's default, `verified` and `refuse`
  (`tools/policy/catalogue.toml`), so an install without the policy kit reads the same values; the
  owner units, TOOL-dMindYourWords-2 and TOOL-dMindYourWords-9, find the rows present. Observed by AC7.
- **S7** — The unattended route. Under `read_policy_value("lexicon.at-commit", root)` reading `refuse`,
  the refusal adds one line: an unattended run renames the name or parks its unit, and never writes a
  suppression, since the write path admits only the owner's proof under its default
  (PLAY-dOrderedCharter-15 S3). Under `warn` and `off` the line is not printed. Observed by AC8.
- **S8** — The text. Both registries' headers state the site key, the mandatory reason and the record,
  and why a site key is not the positional key TOOL-aLoosenedCeiling-5 refused (TOOL-dScaffoldedMirror-4
  §4's table); the `Offender` docstring (`lexicon.py:238-248`) and the lexicon README's waiver section
  say the same. NOT OBSERVED by a criterion: prose, read by the reviewer at the close.

## 3. Non-goals (OUT)

- Folding the count into the forced tally and printing a suppression's source `suppressed:<path>::<name>`:
  TOOL-dMindYourWords-2 owns `Offender.source` and the tally line (I2), and reads S2's `load_waivers`.
- Which value of `lexicon.forced` routes which names: TOOL-dMindYourWords-2. This unit reads the value
  for the order of S6's outcomes only.
- The commit-time refusal of a staged suppression with no record: TOOL-dMindYourWords-11's
  `--check-record`, whose tag `unit.lexicon.suppressions` covers both registries. S4 is the bar's half.
- A `<path>:<line>` key, ever (TOOL-aLoosenedCeiling-5), and any reason grammar beyond non-empty
  (TOOL-dScaffoldedMirror-4 §3).
- Two scope items of TOOL-dScaffoldedMirror-4, its S4 (P3's key, a predicate deleted since)
  and its S6 (a drift-audit watermark): the clause asks for a count printed by the lexicon, which S5 is.
- Moving the registries out of the kit directory: they stay `seed` files (`tools/lexicon/kit.toml:57-64`).

### Edges

- **consumes-from** `TOOL-dMindYourWords-1` — `Offender.grade`, the field a suppressed site takes as
  `forced`; without it a suppression cannot leave the debt count
- **consumes-from** `TOOL-dMindYourWords-1` — `read_policy_value`, I7's one policy read, which S6 and S7
  call with `lexicon.forced` and `lexicon.at-commit`
- **consumes-from** `TOOL-dMindYourWords-11` — `read_vocabulary_record`, with `rev` a commit or
  `index`, the provenance S4 requires
- **consumes-from** `TOOL-dMindYourWords-12` — `extract_ranges` with `context=True`, read through
  `read_definition_context`, whose `qualname` spells S1's method key
- **hands-off** `TOOL-dMindYourWords-2` — `load_waivers`, its `(rows, problems)` shape and the site
  key, which unit 2 reads for the forced tally's `suppressed` count and source

## 4. Design

### The key and why it is a site

TOOL-dScaffoldedMirror-4 §4 settled the keying and this unit takes its table whole: `<path>::<name>`
survives an edit above the site, covers one site, and stops matching when the definition is renamed or
moved, which `STALE WAIVERS` names. Its line numbers and its "three registries" are stale at base:
`load_waivers` sits at `:2324`, not `:195-208`, and there are two registries, the third predicate
having been deleted (scout A disagreement 2). This unit adds one refinement: a method keys by its
qualified name, so two classes in one file overriding `emit` are two sites.

### The provenance join

```
for registry with rows:
    blame = git blame --porcelain -- <kit-relative registry>        # one spawn
    for row: commit = blame[row.lineno]
        if commit is the zero id:  ok = read_vocabulary_record(root, TAG, rev="index")
        else:                      ok = read_vocabulary_record(root, TAG, rev=commit)
        if not ok: problem("SUPPRESSION WITHOUT PROVENANCE", registry, row, commit)
```

Blame attributes a row to the commit that last wrote it, so an edited reason needs its own record,
which is what "changed only through the write path" asks. A rebase keeps the pair in one commit; a
squash merge does too. A registry outside the repository, a kit installed outside it, cannot be
blamed and reds `cannot judge provenance`, naming the path, rather than passing.

### The refusal's outcomes

| `lexicon.forced` | Printed order |
|---|---|
| `verified` (default) | rename · custom pack row · suppression |
| `by-name` | rename · custom pack row · suppression |
| `by-annotation` | suppression · rename · custom pack row |

### Inventory

Minted: the slot `Offender.site`; `check_suppression_provenance` in `tools/lexicon/lexicon.py`, cell
`py.function`, answered `OK` by `lexicon.py --suggest check_suppression_provenance --as py.function` at
base; the problem names `EMPTY REASON`, `MALFORMED SUPPRESSION`, `DUPLICATE SUPPRESSION` and
`SUPPRESSION WITHOUT PROVENANCE`; the count line `lexicon: suppressed=`.

### Migration

None in gov: both registries hold 0 rows at base (PINNED, eight header lines each at `ba8b3c8c4`). An
adopter's bare-name rows are refused as `MALFORMED SUPPRESSION` on upgrade, naming each row, and the
remedy is to re-key it to its site with its record; §8 F3 says why no upgrade step converts them.

### Rollout

Live when built. In gov nothing moves on landing: no row exists to re-key or to blame.

### Files touched (estimate)

- `tools/lexicon/lexicon.py`
- `tools/lexicon/lexicon-verb-waivers.txt`
- `tools/lexicon/lexicon-suffix-waivers.txt`
- `tools/lexicon/selftest.py`
- `tools/lexicon/README.md`

### Alternatives rejected

- **A registered row kind in the overlay**, written by `instructions_edit.py` (scout A disagreement 7,
  option a). Rejected by the clause's source: the lexicon review's item 4 reads "It extends today's
  waiver files and `load_waivers`", and a row kind would be read across a kit boundary by subprocess.
- **A row naming its record**, `<site> <record> <reason>`. Rejected: a pointer can name any old record
  of the tag, so it proves a record exists, never that the row's own change carried one; blame ties the
  row to the commit that wrote it.
- **The bare name kept beside the site key** for module functions. Rejected by TOOL-dScaffoldedMirror-4's
  measurement: 44 of 395 offender names span more than one file at `af4de2d5`, so a bare key exempts a
  sixth arrival before it is written.

## 5. Production-readiness checklist

- security — deny by default: an empty reason, a malformed key, a duplicate and a row without provenance
  each red; an unjudgeable registry reds rather than passes.
- perf / scale — one `git blame` per registry holding a row, and one `read_vocabulary_record` per
  distinct commit; with no rows, no spawn.
- error / empty / loading states — an absent registry is no suppression, the legal state `load_waivers`
  documents (`:2325-2326`); the count line prints `suppressed=0`.
- observability — S5's line on every run; each problem names file, line, site and, for provenance, the
  commit.
- risks — an adopter's bare-name rows red on upgrade (§4 Migration); the price of a site key the clause
  asks for.
- testing — the arms of §7, on planted registries in fixture repositories.
- migration — none in gov; the refusal names each adopter row to re-key.
- user docs — the registries' headers and the lexicon README's waiver section, S8.

## 6. Acceptance criteria

- **AC1** — When the lexicon runs over a fixture corpus whose `a.py` and `b.py` each define
  `frobnicate_index`, with the verb registry holding `a.py::frobnicate_index  deliberate, see the spec`
  committed beside a `unit.lexicon.suppressions` record, `a.py`'s site is not counted, `b.py`'s is, and
  the run prints `lexicon: suppressed=1 (verb=1, suffix=0)`.
  Red when: the row exempts `b.py` too, which today's text key does.
  fixture: the selftest's `run_case` repository, the record committed with the row.
- **AC2** — When `a.py` defines `class H(logging.Handler)` with method `emit`, and also a module
  function `emit`, the row `a.py::H.emit  logging calls it` suppresses the method and not the function;
  a row `a.py::emit` suppresses the function only.
  Red when: a method row matches a same-named module function.
- **AC3** — When the registry holds `a.py::frobnicate_index` with no reason, the run exits 1 naming
  `EMPTY REASON` with the registry's file name and the row's line.
  Red when: the empty reason is accepted, the clause's first planted case.
- **AC4** — When the registry holds `frobnicate_index  a reason`, the run exits 1 naming
  `MALFORMED SUPPRESSION`; when it holds the same site key twice, it exits 1 naming
  `DUPLICATE SUPPRESSION` with both lines.
  Red when: a bare name is read as a key.
- **AC5** — When `check_suppression_provenance` grades the row of AC1 committed in a commit adding no
  vocabulary record, the run exits 1 naming `SUPPRESSION WITHOUT PROVENANCE`, the row and that commit's short id; committed with a
  `unit.lexicon.suppressions` record it passes; staged with that record staged it passes; staged alone
  it exits 1.
  Red when: a row with no provenance record passes, the clause's second planted case.
  fixture: as AC1, one commit per case.
- **AC6** — When the registry holds `a.py::gone_symbol  a reason` with its record and no `a.py`
  definition by that name, the run exits 1 naming `STALE WAIVERS`.
  Red when: a stale site row passes.
- **AC7** — When the fixture repository commits `.governance/policy.toml` with `[lexicon]` `forced =
  "by-annotation"` and the lexicon refuses an offender over the pin, the refusal prints the suppression
  outcome first; with no policy file, and with `forced = "by-name"`, it prints rename first and
  suppression last.
  Red when: suppression leads under the default, or trails under `by-annotation`.
  fixture: the policy kit resolved beside the fixture's kit copy; the file committed, since `policy.py
  get` reads the landed revision.
- **AC8** — When `check_pass` prints the same refusal with no policy file, it prints the line naming an
  unattended run's rename-or-park; with `[lexicon]` `at-commit = "warn"` committed, it does not.
  Red when: the line prints under `warn`, or is absent under the default `refuse`.
  fixture: as AC7.
- **AC9** — When `python lexicon.py` runs on gov's tree after this unit, it prints
  `lexicon: suppressed=0 (verb=0, suffix=0)`.
  Red when: the line is absent on green.
  figure: 0 is DERIVED from the registries at the run.

## 7. Gates

`lexicon selftest` · `codebase-map kit selftest` · `lexicon naming predicates` · `lexicon wiring` · `spec tokens (a spec's own names resolve)`

New arm: tools/lexicon/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 AC8 · the planted registries and policy files in fixture repositories, the failing cases staged by an empty reason, a bare-name key, a row committed without its record and a site row matched by name · none

The arms of `tools/lexicon/selftest.py` that plant bare-name rows (its S8 waiver block and the
`ZZZ_STALE` stale-waiver agreement) are rewritten to site keys in the same pass.

## 8. Open questions

- **F1 — Where does a suppression live, given that `instructions_edit.py` writes only manifest rows?**
  Options: (a) a registered row kind in the overlay; (b) today's registries, each row admitted only by
  the write path's record in its own commit. RESOLVED (agent, 2026-10-29, delegated): (b), rung 1: the
  lexicon review's `[forced]` item 4 reads "It extends today's waiver files and `load_waivers`", and the
  same choice is TOOL-dMindYourWords-11 §8 F1's for the declaration. widens: none · relaxes: none
- **F2 — How is a row's provenance found?** Options: (a) blame each row to the commit that wrote it and
  require that commit to add a `unit.lexicon.suppressions` record; (b) a pointer column naming the
  record; (c) any record of the tag anywhere in the tree. (b) and (c) admit a row whose own change
  carried no record. RESOLVED (agent, 2026-10-29, delegated): (a), rung 3, the most feature-rich
  survivor. widens: none · relaxes: none
- **F3 — Does an upgrade step convert an adopter's bare-name rows?** Options: (a) refuse each, naming the
  re-key; (b) an upgrade step through TOOL-dSafePassage-1's `[[upgrade]]` rows. (b) cannot choose the
  site: a bare name exempted every file, and narrowing it to one is a choice of the owner's, so the step
  would either guess or write one row per file, which is the corpus-wide exemption again. RESOLVED
  (agent, 2026-10-29, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-29 · initial draft, from the packet's Items 5, the lexicon review `[forced]` item 4
  :268-274 and :279-282, debt-fold rows `suppression-path` and `no-pack-owner-route`,
  TOOL-dScaffoldedMirror-4 §2 to §4, scout A's row 5 and disagreements 2 and 7, and the spec brief's
  I3 and I11.

## 10. Reuse audit

The seam extended is `load_waivers` (`tools/lexicon/lexicon.py:2324`) with `WAIVER_FILES` (`:93`) and
its four readers (`:3046-3053`, `:3270`, `:4072-4074`), on the design TOOL-dScaffoldedMirror-4 settled.
`python tools/codebase-map/reuse_lookup.py "key a waiver to one definition site with a mandatory
reason"` ranked `key`, `read_conf_key` and `load_stand_in_waivers` (`tools/roles/roles_lib.py`); the last
reads the roles kit's stand-in waivers, a different registry, and the lexicon imports no sibling kit
(`check_self_containment`, `:2359`), so it is not reused; no existing reader joins a row to its commit's
record, and S4 is new. Where record and source disagree: TOOL-dScaffoldedMirror-4 cites `:195-208` and
three registries, and source holds `:2324-2337` and two (scout A disagreement 2, re-verified at
`ba8b3c8c4`); scout A's other line numbers hold. The recall probe's fifth hit is that unit's own ask,
TOOL-dScaffoldedMirror-4 in dScaffoldedMirror's `BACKLOG.md`, still open: S1 and S2 do its S1 to S3, and
this unit changes no row of that backlog.

Recall terms used: `python tools/memory-recall/query.py "how is a lexicon waiver keyed and what reason does it need" --terms "load_waivers waiver path::name site key mandatory reason suppression provenance STALE WAIVERS"`
