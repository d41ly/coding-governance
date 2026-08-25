**Serves:** spec TOOL-dPromptedSeam-1

# TOOL-dPromptedSeam-1 — a refused name carries a reuse prompt

**Status:** OPEN · rev-1 · 2026-08-25 · node d · Tier-2 · base 70df24ea · streams tooling

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

When `lexicon.py --suggest <name>` refuses a name, it also reports whether the OBJECT of that name
already has a seam in this repo — so the author learns both what to call the thing and that the thing
may not need writing. The lexicon kit must remain adoptable with no `codebase-map` present, so this
is an optional adapter and never a dependency.

## 2. Scope (IN)

- **S1 — the object query.** On the refusal path only, `run_suggest` derives `read_object(name)` and,
  when it is non-empty, asks `codebase-map`'s `reuse_lookup.py` for seams matching it.
- **S2 — optional discovery.** The adapter resolves the sibling kit by the repo's own idiom: the
  adopted-root marker `.codebase-map.conf`, then the first of the candidate prefixes that actually
  holds `reuse_lookup.py`. No hardcoded single path, no import.
- **S3 — a bounded, non-authoritative call.** Subprocess, with a timeout DECLARED in `.lexicon.conf`
  rather than hardcoded. The adapter cannot change `run_suggest`'s exit code or its primary line
  under any outcome, including a crash.
- **S4 — every outcome is named.** Five distinct terminal states — hint printed, map not adopted,
  object empty, lookup refused, lookup timed out — each with its own sentence. A silent omission is
  not one of the five.
- **S5 — a declared switch.** `.lexicon.conf` gains `REUSE_HINT="on|off"`, defaulting ON where the
  map resolves, so an adopter who finds it noisy turns it off without editing the kit.
- **S6 — arms.** Selftest coverage for all five outcomes, each observed to fail against the code it
  guards, plus a non-vacuity arm proving the hint path is reached at all.
- **S7 — docs.** `LEXICON.md`'s delivery section and `tools/lexicon/README.md` gain the behaviour;
  the rendered Skill gains one line, and its byte-comparison gate re-renders.

## 3. Non-goals (OUT)

- **No auto-rename, and this is the load-bearing OUT.** The table's value is SCOPING: a name that
  will not fit reports an unclear responsibility. Rewriting the identifier would silence exactly the
  signal the table exists to produce, and leave a repo that passes P1 with its seams still wrong.
- **No hint on the OK path.** A declared verb is not an occasion to re-litigate reuse, and paying the
  lookup cost on every conforming name is how a supply verb becomes one nobody runs.
- **No new gate leg, and no effect on P1/P2/P3.** The hint is an addendum to one CLI verb. Nothing
  about grading, pins, coverage or waivers changes.
- **No import from `codebase-map`, in either direction.** Subprocess only.
- **No caching in rev-1.** A cache is a freshness problem, and the measured cost does not yet justify
  taking one on. Revisit only if `--suggest` becomes hot.
- **No freshness assertion about the map.** `reuse_lookup.py` reads committed artifacts; their
  freshness is already a merge-bar leg's job and re-asking here would be a second answer to it.

## 4. Design

**D1 — the seam is a SUBPROCESS, and the reason is the port.** `tools/lexicon/subtokens.py` exists as
a copy of `map_lib.subtokens()` so the kit ships self-contained. An import here would reintroduce the
dependency that port was written to avoid, for a feature that is by definition optional. The adapter
therefore shells out, and treats a missing sibling as an ordinary outcome rather than an error.

**D2 — it fires on the REFUSAL branch only.** `run_suggest` has three terminal branches today: the
verb is declared (`OK`), the verb is off-table and a row bans it by name (the suggestion), and the
verb is off-table with no row naming it. The hint attaches to the second and third — the two where
the author is about to write something — and never to `OK`.

**D3 — the query is the OBJECT, and it was measured before being specced.** `read_object("fetch_conf")`
is `conf`; on this corpus that query returns `load_conf` at fan-in 16 marked SEAM. `index` returns
`build_index` and `build_form_index`; `verbs` returns `leading_verb`. The premise that a bare object
token is a useful query is therefore established rather than assumed. A single-token name has no
object, which is S4's `object empty` outcome and not a failure.

**D4 — cost is the binding constraint, and it is DECLARED.** One lookup measured **1.85 s** on this
corpus. That is affordable on a refusal, where the author is about to spend minutes, and unaffordable
on every call. `REUSE_HINT_TIMEOUT_S` lives in `.lexicon.conf` with a shipped default; the adapter
kills the subprocess at the bound and prints the timed-out sentence. A number a reader can find and
change is the difference between a budget and a magic constant.

**D5 — THERE IS NO CYCLE, though the wiring looks like one.** `codebase-map`'s `lexicon-verbs`
extractor imports `lexicon_conf`, and this adapter calls `reuse_lookup.py`. Those do not close:
`reuse_lookup.py` reads only committed artifacts, the dossiers and the conf, and explicitly needs no
project `map_extractors.py`. So the map's dependency on the lexicon is at ARTIFACT-BUILD time and the
lexicon's on the map is at QUERY time, and neither reaches the other's entry point. Stated here
because the next reader will see two arrows and assume a loop.

**D6 — the hint is visibly SECONDARY.** It prints after the suggestion, under its own marker, and its
wording proposes rather than instructs. `--suggest` answers "what do I call this"; the hint answers
"does this already exist". Two questions, and the output must not let them blur into one.

**D7 — output shape.** The primary line is unchanged, byte for byte, so anything parsing it today
keeps working. The addendum is appended lines, capped at the top three candidates, each carrying the
symbol, its file and its fan-in as `reuse_lookup` already prints them. No reformatting: a second
renderer for another tool's output is a second answer to how that output reads.

## 5. Production-readiness checklist

- **security** — the adapter execs a resolved in-repo path with a fixed argv and no shell. The query
  is `read_object()` output, which `subtokens` has already reduced to word characters, so no
  identifier can carry a separator into the argv. N/A beyond that: no network, no credentials.
- **perf / scale** — 1.85 s measured, refusal-path only, bounded by a declared timeout. The cost
  scales with the map corpus, not with the query, so it is flat per call.
- **a11y** — N/A, a CLI addendum.
- **i18n** — N/A, but note the ASCII limit inherited from `subtokens`: a non-ASCII identifier yields
  no object and takes S4's `object empty` path. That is correct behaviour here and is a symptom of
  the carried finding, not a new one.
- **error / empty / loading states** — the five outcomes of S4 are exactly this list, and each is a
  sentence rather than a silence.
- **observability** — the hint prints its own outcome every time; there is no state to inspect later.
- **risks** — the material one is NOISE: a hint that fires on every refusal and is usually irrelevant
  trains the reader to skip the whole output, including the suggestion. Mitigated by capping at three
  candidates, by firing only on refusal, and by `REUSE_HINT="off"`. Rollback is deleting the adapter;
  it holds no state and writes no file.
- **testing + left-shift gates** — S6. Each of the five outcomes gets an arm, each staged to fail
  against the code it guards; plus a non-vacuity arm asserting the hint path is entered, because four
  of the five outcomes are ABSENCES and a suite of absences passes on a broken adapter.
- **migration / rollback** — none. New optional behaviour on one verb; no data, no format change.
- **user docs** — S7.

## 6. Acceptance criteria

- **AC1** — When `python tools/lexicon/lexicon.py --suggest fetch_conf` runs in this repo, the output
  keeps its existing first line unchanged AND appends a hint naming `load_conf`.
- **AC2** — When the same command runs with `REUSE_HINT="off"` in `.lexicon.conf`, no hint is printed
  and the exit code is unchanged.
- **AC3** — When `--suggest` runs in a fixture repo with no `.codebase-map.conf`, the output says the
  map is not adopted, in one sentence, and exits exactly as it does today.
- **AC4** — When `--suggest fetch` runs, a single-token name whose `read_object` is empty, the output
  says there is no object to look up rather than printing an empty or unfiltered hint.
- **AC5** — When the adapter's subprocess is forced to exceed `REUSE_HINT_TIMEOUT_S`, the output names
  the timeout and the exit code is unchanged.
- **AC6** — When the adapter is made to raise, `python tools/lexicon/selftest.py` still reports the
  suggestion arms green, proving the hint cannot take the primary answer down with it.
- **AC7** — When each of the five outcomes is staged broken in turn, `python tools/lexicon/selftest.py`
  reds naming that outcome's arm, and the clean tree reds none.
- **AC8** — When `bash tools/lexicon/adopt-lexicon.sh --check` runs after S7, it reports the Skill in
  sync, so the rendered Skill carries the new line rather than drifting from the declaration.

## 7. Gates

Adds no leg. Rides `lexicon selftest` (S6's arms), `lexicon naming predicates` (the adapter's own
identifiers are graded by the table it serves), and `lexicon wiring` (S7's Skill re-render). The
codebase-map legs are untouched — nothing in that kit changes.

## 8. Open questions

- **Q1 — does the hint fire on the third branch too?** D2 says it attaches to both off-table branches,
  including "no row bans it by name". That branch means the canon has no opinion, which is arguably
  where reuse advice is MOST useful and also where it is least grounded. RESOLVED: fire on both. The
  object is a fact about the identifier and does not depend on the canon having a row.
- **Q2 — three candidates, or fewer?** `reuse_lookup` ranks and this spec caps at three. Unresolved
  by measurement; three is the shipped default of the tool's own shortlist head and is adopted rather
  than re-derived. Revisit only if noise is reported.
- **Q3 — should the timeout default be shipped or required?** RESOLVED: shipped with a default, since
  a required key would make every existing `.lexicon.conf` refuse on upgrade, and the kit's own
  grammar treats absence as "the kit's default" elsewhere.

## 9. Revision log

- rev-1 · 2026-08-25 · node d · OPEN. Written from the measured premise: the object query was tested
  against this corpus before the spec was written, and the 1.85 s cost was measured before the
  design chose a subprocess with a declared bound. Q1 and Q3 resolved in-spec; Q2 deliberately left
  adopted-not-derived and marked as such.

## 10. Reuse audit

- `read_object()` (`tools/lexicon/lexicon.py`) — EXTENDED, not re-implemented. It already performs
  the verb-strip this unit needs and gains its second consumer.
- `reuse_lookup.py` (`tools/codebase-map/`) — CALLED as shipped. Its ranking, its shortlist head and
  its partial-recall notice are consumed verbatim; this unit adds no second renderer for them.
- `first_of` (`tools/check-wiring.sh`) — the candidate-prefix idiom is REUSED in shape. The adapter is
  Python and cannot call the bash helper, so it reproduces the pattern rather than the code, which is
  the same relationship `subtokens.py` already has with `map_lib`.
- `lexicon_conf.load_conf` — REUSED for the two new keys. No second parser.
