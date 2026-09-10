**Serves:** journal TOOL-aGradedDialect-5

# Acceptance ledger — TOOL-aGradedDialect-5, the records

Every observation below was made on node `a` on 2026-09-10, in this run's own worktree, at the
commit this ledger lands in.

**This unit moves no mechanism.** It writes prose, one version literal and one status flip, so
nothing here is a measurement of behaviour — every criterion rests on an existing merge-bar leg or
on reading a named file, which is what §5 and §7 say.

**Three of the seven criteria were already satisfied when this pass opened, and saying so is the
point.** AC3 and AC5's key half were discharged by `TOOL-aGradedDialect-3` and by the shape of the
map dossier's claims, not by anything written here; rev-5's §9 entry records both, because a scope
item nobody edited and a scope item nobody needed to edit produce the same diff and only one of them
is honest.

**Evidences:** TOOL-aGradedDialect-5

- AC1 — `parse_ts_defs.__doc__` — `tools/lexicon/LEXICON.md` gains a `.ts`/`.tsx` section whose mode
  token is `parser`, read off `KNOWN_EXTS` in `tools/lexicon/lexicon.py` (`ts: ("ts-tokens",
  "parser")`, `tsx: ("tsx-tokens", "parser")`) rather than off any run of this tree, which tracks
  zero `.ts` files. The section pairs all SIX refusals that header enumerates with the check that
  compensates for each: the untokenizable-source raise against `scan_corpus`'s named refusal; the
  `${…}`/JSX suppression, the overload signature and the computed key against the conformance floor
  the arm in `selftest.py` enforces; the empty import list against the self-containment refusal
  being the only import consumer; and `eval`/decorator/import names against the honest answer that
  no compensating check is OWED, since there is no definition site to grade. It carries NO figure
  from the measurement and points at the arm that prints one every run, per the brief.
- AC2 — `PATTERNS:` — both halves observed.
  NEGATIVE: `grep -n "TWO PARSERS SHIP\|could only declare their language" tools/lexicon/README.md
  tools/lexicon/lexicon.py memory/map/features/lexicon.md` exits 1 with no hit in any of the three.
  **LIVENESS, because a zero-hit grep and a broken grep are the same exit code:** the SAME command
  over the SAME three paths hit four times before the edit — `README.md:237` and `README.md:285`,
  `lexicon.py:26`, `map/features/lexicon.md:170` — so the probe was proven able to move on this
  population, and its silence now is an answer rather than a misfire.
  POSITIVE: "Arming a language this kit does not ship" still names `Go, Rust or C#`, still teaches
  the `PATTERNS:` block with a worked example, and now states in as many words that the kit does not
  decline to run an adopter's own extractor — what a declaration cannot hand itself is the `parser`
  standing. The section's example moved from `ts:ts-regex:probe` to `go:go-regex:probe`, because an
  example arming a language the kit now ships teaches the opposite of what the section is for. The
  modes-table `probe` cell and the "ships exactly one" sentence are corrected in the same pass, and
  so is the SECOND carrier of that table inside `lexicon.py`'s module docstring — see rev-5.
- AC3 — `grep -rn "dScaffoldedMirror-13" tools/` — two hits, both in `tools/lexicon/selftest.py`
  (lines 2361 and 4406) and neither describing that decision as the standing owner of the
  `.ts`/`.tsx` question. The `DEFINITION_SNIFF` header sentence AC3's Red-when names sat at
  `tools/lexicon/lexicon.py:144` at this spec's BASE `d1357673` and is gone from HEAD:
  `TOOL-aGradedDialect-3` S8 rewrote that whole header when it widened the sniffer. **So this unit
  wrote no edit for S3** and AC3 observes the tree rather than a change to it. Recorded in rev-5.
- AC4 — `builds/aGradedDialect/` — **HALF OBSERVED, and read the second paragraph before treating
  this row as satisfied.** A criterion with two clauses gets one ledger line, and this line takes the
  reading that DEMANDS something rather than the one that demands nothing. The half this pass owns:
  `memory/builds/dScaffoldedMirror/spec/2026-08-24-spec-dScaffoldedMirror-13.md`'s status-header TAIL
  now reads `SUPERSEDED IN PART by builds/aGradedDialect/`, naming what superseded it and stating why
  the status token stays `DEFERRED` — §8 F3, the adoption onto a real tree, is the owner's and
  untouched. That token did not move, per §8 F1.
  **The `memory/backlog/TOOL.md` half is NOT this pass's and this line does not claim it.** The
  build method names a backlog a shared mutable record, so `--dispatch` refuses the path outright and
  no pass may declare it; the row is moved off `DEFERRED` by the parent run in a pass of its own.
  Until that lands, AC4 is HALF observed, which is stated here rather than smoothed over.
- AC5 — `codebase-map coverage + freshness` — `python3 tools/codebase-map/test_codebase_map.py`
  exits 0 over six arms, `test_every_inventory_key_is_claimed_or_baselined` among them, both before
  and after this pass's edit to `memory/map/features/lexicon.md`. No key minted by units 2 to 4 is
  unclaimed and no claim names a dead one. It was ALREADY green: the dossier claims leading verbs,
  and `parse_ts_defs`, `parse_tsx_defs`, `scan_ts_tokens` and `resolve_extractor` lead with `parse`,
  `scan` and `resolve`, all three already claimed. The PROSE half of S5 — the map dossier's own
  copy of the language-list sentence — is what this unit actually wrote, and it is observed by AC2
  above.
- AC6 — `bash tools/check-kit-versions.sh` — exits 0 after `KIT_LEXICON_VERSION` moved `1.2` -> `1.3`
  and all FOUR gated markers moved with it: `tools/lexicon/lexicon.py`, `tools/lexicon/canon.py`,
  `tools/lexicon/README.md`, `tools/lexicon/LEXICON.md`. The three marker edits were made in BINARY
  mode with an asserted single-occurrence count per file, because a text-mode rewrite of a CRLF
  working copy is this repo's recorded way to corrupt a file it was only editing one line of.
  SECOND clause: `lexicon wiring` — `bash tools/lexicon/adopt-lexicon.sh --check` — exits 0 with
  `Skill in sync` over the RE-RENDERED `.claude/skills/lexicon/SKILL.md`, whose diff is exactly one
  line, LF, verified through `git diff | cat -A`. The Skill was produced by `--render`, never
  hand-edited. Staged red, before the render: with the four carriers bumped and the Skill left at
  `@1.2`, `check-kit-versions.sh` exited 0 — which is round 3's finding 11 reproduced, and the
  reason AC6 is two clauses over two legs rather than one.
- AC7 — `govkit:entry lexicon` — `WIRE-INTO-PROJECT.md` carries that anchor with a five-step body at
  `## 3f — Adopt the lexicon kit (if chosen in §0)`, written in the shape of the `codebase-map`
  section the same file already carries. Its `rm -f` line names exactly two paths,
  `tools/lexicon/selftest.py` and `tools/lexicon/ts-conformance-fixtures.json`, which are precisely
  the `role = "project-owned"` rule in `tools/lexicon/kit.toml`; it does NOT name
  `SKILL.template.md`, and the section says in its own words why deleting that one would disable the
  step immediately below it. `python tools/govkit/check_runbook_parity.py` no longer lists `lexicon`
  among the entries with no anchored section.

## The pre-existing red this landing DOES drain, confirmed

`python tools/drift-audit/drift_report.py --check` exited 1 before this pass with
`non_terminal_specs_cited_by_product_source = 3` against a shrink-only pin of 2, the third entry
being `tools/lexicon/kit.toml` citing this very unit at status `SPECCED`. Flipping this spec to
`CLOSED` in the same commit as the edits removes it. Re-run after the commit: recorded below in "What
was run after the commit", because the signal reads the COMMITTED status header and a staged flip is
invisible to it.

## The pre-existing red this landing does NOT drain

`bash tools/check-install-prefix.sh` exits 1:

```
  ROSE        tools/lexicon/selftest.py	22 -> 23
```

Not this unit's, and proven rather than asserted: `git diff HEAD -- tools/lexicon/selftest.py` is
empty across this whole pass, and `git log --oneline -- tools/lexicon/selftest.py` puts the last two
touches on `TOOL-aGradedDialect-4`. The row in `tools/install-prefix-carried.txt` is a hand-written
ratchet entry whose fourth column justifies every literal it counts as FIXTURE-INTERNAL — argv
elements handed to a `subprocess.run` inside a scratch tree — so the discharge is one more sentence
in that column naming the 23rd, and it is priced on the unit that added the literal. §3 forbids this
unit from touching `selftest.py` and the registry row is not in its declared write set, so it is
REPORTED here and in rev-5 rather than absorbed into a records-only diff where a closing review
would find it under the wrong name.

## What was run after the commit

- `python tools/memory-tree/gotchas.py --for-diff HEAD~1..HEAD` — the bug-class checklist over this
  unit's own diff. What it selected and what landed is the section below.
- `python tools/drift-audit/drift_report.py --check` — re-run against the committed status header,
  to confirm the shrink-only pin above is drained rather than assumed to be.

## What the bug-class checklist named, and what landed

`amendment-leaves-its-other-half-standing` landed on the spec itself and is the reason there is a
follow-up commit at all. rev-5 recorded three divergences in §9 and left §2's scope items and §4's
carrier table still asserting the old wording — S3 still read "the one comment … is rewritten" for an
edit this unit does not make, S2 still named the README alone, S5 still implied the key claims moved,
and §4 still described a `DEFINITION_SNIFF` sentence that no longer exists. rev-6 folds all four. A
revision log is not where a scope item gets corrected. Re-running the checklist over the fold
selected the same class again and it found two more halves — S4 read as though this unit moves the
backlog row, and §4's Files-touched named that backlog while omitting the ledger and the three
generated artifacts a `CLOSED` flip re-renders. Both folded into rev-6 rather than into a third
commit. The stopping rule is convergence, not the selector going quiet: this class stays selected
for as long as the diff touches a spec.

`two-answers-to-one-question` landed a third time, on this unit's own new prose, and both instances
are duplications AC1 REQUIRES rather than ones it could delete. The `.ts`/`.tsx` section restates the
six refusals that `parse_ts_defs`'s header enumerates, and it restates the `tsx.function` role rule
that the scaffolder emits beside the row. Both now carry an explicit direction of truth: the header
is the enumeration and this page is the pairing, so a seventh refusal the header gains and this page
lacks is a defect HERE; and the emitted comment is the copy to trust if the two ever disagree. A
required duplication with a named direction is the discharge; a required duplication with neither is
the class.

`two-answers-to-one-question` is the class this whole unit exists to close, and it landed on the unit
itself twice while it was being written. First, the modes table: correcting the README's `probe` cell
and leaving `lexicon.py`'s identical copy of it would have been the same defect one carrier over, in
the file that owns the behaviour. Both were corrected and rev-5 records the widening. Second, the
count: the replacement prose in both carriers deliberately writes NO number of shipped parsers, and
points at `PARSERS` instead — the old sentence spelled a count beside the dict that owns it, which is
how it went stale twice.

`fixture-passes-by-finding-nothing` was read against AC2's negative half and is the reason that
criterion has a positive half at all: a zero-hit grep is satisfied by deleting the section, so the
observation above asserts what SURVIVES as well as what is gone — and the AC2 line now carries the
liveness assertion that makes its exit 1 an answer.

`one-value-field-records-a-mixed-outcome` landed on AC4, whose two clauses split across two runs and
whose ledger grammar offers one line and two forms. The line leads with HALF OBSERVED rather than
with the half that is done.

**The remaining six were read and do not land.**
`heredoc-escape-reaches-the-regex` — the only heredoc in this pass drove a binary-mode byte
replacement of three version markers and carried no escape; the Go example's `\s`, `\w` and `\(`
were written with the edit tool and verified by compiling both rows in `re` and matching them
against a Go fixture (`groups 1 1`, funcs `Add` and `Serve`, type `Server`).
`inline-fence-swallows-the-rest-of-the-file` — every touched markdown file was counted for fence
parity: `WIRE-INTO-PROJECT.md` 20, `tools/lexicon/README.md` 14, `tools/lexicon/LEXICON.md` 2, this
ledger 2, the spec 0. All even.
`staged-break-substitutes-a-synthetic-value` — AC6's staged red used the SHIPPED state, four
carriers bumped with the real rendered Skill left behind, not a simplified stand-in.
`armed-but-unreachable-rule` — this unit arms no rule; every criterion is a read of a named file or
an existing leg, and §7's leg set is unchanged.
`empty-field-collapses-unless-it-is-last` — no shell field parsing is added or edited.
`fold-text-is-unreviewed-surface` — true of every line this unit wrote, including rev-5 and rev-6.
It is not dischargeable here: the closing diff review is what reads it, and this ledger names the
fold rather than claiming it was reviewed.

## What this unit did NOT observe, stated rather than left out

- **Nothing here was observed on a repository that declares TypeScript.** This tree tracks zero
  `.ts` and `.tsx` files. Every claim in the LEXICON.md section is derived from `KNOWN_EXTS`, from
  `parse_ts_defs`'s header and from the conformance arm's own output; none of it was watched running
  over a real TypeScript corpus by this unit.
- **The `lexicon selftest` leg was not run and is not owed.** It is `subject = kit`,
  `chunk = selftests` in `tools/gate-legs.json`, so no ordinary bar runs it, and this unit changes
  no kit predicate — only comments, a version literal and reader-facing prose.
- **The runbook section was not executed.** Nobody ran `cp -r`, the `rm -f` line or `--scaffold`
  against a real adopter tree from this pass; the section's steps were verified by reading
  `tools/lexicon/adopt-lexicon.sh` and `tools/lexicon/kit.toml`, including the exact `--check`
  messages it quotes. An adopter's tree is theirs and this unit installed nothing.
- **`memory/map/generated/symbols.json` did not move**, and did not need to: this unit defines no
  symbol.
- **The `TOOL-dScaffoldedMirror-15` backlog row is now stale in a second way** and it is not in this
  unit's write set. It says `check_runbook_parity.py` names 18 entries with `lexicon` among them at
  output line 12; the checker reported 19 before this pass, so the figure was already stale on
  arrival, and `lexicon` leaves the list here. Whoever writes the backlog pass gets both.
