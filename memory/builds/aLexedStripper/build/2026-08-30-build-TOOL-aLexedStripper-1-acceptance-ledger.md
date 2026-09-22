# Acceptance ledger — the four `aLexedStripper` units

**Serves:** journal TOOL-aLexedStripper-1 TOOL-aLexedStripper-2 TOOL-aLexedStripper-5 TOOL-aLexedStripper-6

Node `a`, 2026-08-30. BASE `19d9b328`, build commit `eb76532e`. Every OBSERVED line names the command
that made the observation; every AMENDED line names the revision that changed the criterion.

The RED observations required by `-1` AC9 and `-2` AC10 were made by staging the pre-change code
back into the real tree, running the arms, and restoring — not in a scratch copy, because the corpus
arm SKIPS outside a git checkout and a skip there would have read as a pass.

**Evidences:** TOOL-aLexedStripper-1

- AC1 — `python tools/codebase-map/selftest.py` — corpus recall 100.0% against the 99% floor, up from
  88.6% for the three-regex chain.
- AC2 — `python tools/codebase-map/selftest.py` — corpus precision 98.1% against the 95% floor, up
  from 37.6%.
- AC3 — `python tools/codebase-map/selftest.py` — `tools/lexicon/lexicon.py` 61.5% -> 100% and
  `tools/codebase-map/selftest.py` 57.3% -> 100%. NOT amended, and the round-2 audit was right about
  why it nearly had to be: under rev-2's SIX-field design this criterion was unreachable by any
  implementation, measured at 99.7% with the sole miss `or` at `selftest.py:1139`, an f-string-only
  NAME. `TOOL-aLexedStripper-6`'s seventh field is what makes the number the spec already demanded
  observable, so the criterion stands as written and the DESIGN moved instead. That is the outcome
  `-6` S4 anticipated, which is why S4 turned out to be a no-op.
- AC4 — `python tools/codebase-map/selftest.py` — the class-1 arm, a `.py` docstring holding
  `application/*` with a later `on*/`, keeps `BRAVO` defined after it.
- AC5 — `python tools/codebase-map/selftest.py` — the class-3 and class-4 arms each keep an
  identifier that follows the marker on the same line, in `.ts`, `.js` and `.py`.
- AC6 — `python tools/codebase-map/selftest.py` — an undeclared suffix returns every token.
- AC7 — `python tools/codebase-map/selftest.py` — `$#` and `${path#/opt/}` keep `resolve_target` and
  `emit_result`, and the positive arm confirms a REAL `#` comment is still stripped.
- AC8 — `python tools/codebase-map/selftest.py` — an unmatched backtick in `.ts` and an unmatched
  triple quote in `.py` both leave every later line's identifiers intact.
- AC9 — `python tools/codebase-map/selftest.py` — staged RED in the real tree with the old chain
  behind the new signature: `FAIL identifier tokens: one arm per over-strip class: class1 /* in a
  Python docstring: lost ['BRAVO']` and `FAIL ... corpus recall 0.890 below the 0.99 floor`. Restored,
  both green.
- AC10 — `python tools/codebase-map/selftest.py` — the whole suite passes, including the `fan_in`
  assertions at `selftest.py:846-853`.
- AC11 — `bash tools/check-kit-versions.sh` — `KIT_CODEBASE_MAP_VERSION` is `1.3`, well-formed, and
  the three `codebase-map@` stamps in `memory/map/generated/` were regenerated to match.

**Evidences:** TOOL-aLexedStripper-2

- AC1 — `bash tools/hooks/agent-cap.test.sh` — a literal `...` in lens prose exits 0 in both the
  multi-line and one-line array shapes, against 2 and 2 at BASE.
- AC2 — `bash tools/hooks/agent-cap.test.sh` — an unmatched `[` exits 0 in both shapes, against 2
  and 2 at BASE.
- AC3 — `bash tools/hooks/agent-cap.test.sh` — an unmatched `]`, `)` or `}` exits 0 in the multi-line
  shape, against 2 at BASE for each.
- AC4 — `bash tools/hooks/agent-cap.test.sh` — an unmatched `(`, an unmatched `{`, ASCII apostrophes,
  U+2019 apostrophes and an em dash all exit 0, as at BASE. The ADMIT rows did not move.
- AC5 — `bash tools/hooks/agent-cap.test.sh` — a six-element lens array exits 2.
- AC6a — `bash tools/hooks/agent-cap.test.sh` — an unbounded fan inside a single-line interpolation
  exits 2, as at BASE.
- AC6b — `bash tools/hooks/agent-cap.test.sh` — the same fan inside a three-line interpolation exits
  2, as at BASE. Under rev-1's design this exited 0.
- AC6c — `bash tools/hooks/agent-cap.test.sh` — a provably bounded five-element fan inside an
  interpolation exits 0. The ADMIT counterpart that stops the view becoming a blanket deny.
- AC7 — amended rev-2 then superseded by `TOOL-aLexedStripper-5` — rev-1's AC7 asked only that the
  hook "does not throw", which the fail-open outcome satisfied; rev-2 pinned the verdict; `-5` then
  changed the mechanism from fail-closed to fallback. Observed under the shipped code: an unbounded
  fan below an unterminated backtick exits 2, as at BASE.
- AC8 — `bash tools/hooks/agent-cap.test.sh` — a nested template `` `a${`b`}c` `` followed by a
  correct five-lens fan exits 0.
- AC9 — `bash tools/hooks/agent-cap.test.sh` — 97 arms pass, 0 fail, including the
  `TOOL-dTieredTribunal-11` round-2 finding-4 escape, which exits 2 as at BASE, and the two-copy
  parity arm.
- AC10 — `bash tools/hooks/agent-cap.test.sh` — staged RED against the 1.8 hook: all five prose arms
  failed with `exit 2, want 0`, exactly the spellings §4's table records. Restored, 97/0.
- AC11 — `bash tools/check-kit-versions.sh` — `KIT_AGENT_CAP_VERSION` is `1.9` and all four carriers
  agree: `tools/hooks/agent-cap.js`, `tools/hooks/scratch-guard.js`, and both `.claude/hooks/` copies.

**Evidences:** TOOL-aLexedStripper-5

- AC1 — `bash tools/hooks/agent-cap.test.sh` — a five-lens harness prefixed with a regex literal
  containing a backtick exits 0, as at BASE. Under `-2` S3 as written it exited 2.
- AC2 — `bash tools/hooks/agent-cap.test.sh` — the regex character-class form exits 0, as at BASE.
- AC3 — `bash tools/hooks/agent-cap.test.sh` — an unbounded fan below an unterminated backtick exits
  2, as at BASE. The fail-open the branch existed to close is still closed.
- AC4 — `bash tools/hooks/agent-cap.test.sh` — a backtick inside a `'…'` string, a `"…"` string, a
  `//` comment and a `/* */` block each admit a legal harness.
- AC5 — `node <verify harness>` — the whole `-2` acceptance suite re-run against the shipped file:
  29/29 shapes hold. The harness is the one recorded in
  `2026-08-30-build-TOOL-aLexedStripper-2-base-measurements.md`.
- AC6 — `bash tools/hooks/agent-cap.test.sh` — every arm that passes at BASE passes.

**Evidences:** TOOL-aLexedStripper-6

- AC1 — `python tools/codebase-map/selftest.py` — `f"hi {name.upper()} and {other or fallback}"`
  returns `name`, `upper`, `other`, `or` and `fallback`.
- AC2 — `python tools/codebase-map/selftest.py` — ground-truth identifiers missed fell from **73 to
  0** and files affected from **25 to 0**.
- AC3 — `python tools/codebase-map/selftest.py` — `tools/codebase-map/selftest.py` scans at 100%
  recall, which `-1` AC3 demands.
- AC4 — `python tools/codebase-map/selftest.py` — `s = "{not_code}"` with no `f` prefix does NOT
  return `not_code`; the `b"…"` arm likewise.
- AC5 — amended rev-3 — the criterion demanded `k` from `f"{d['k'] …}"`, and `k` is the CONTENT of
  a string literal: stdlib `tokenize` reports it as a STRING, not a NAME, so the criterion asked for
  over-capture against the very oracle §6 grades by. Amended to require `d`, `flag` and `other`
  present and `k` ABSENT, and observed in that form by `python tools/codebase-map/selftest.py`. The
  §9 line records that the closing review's round-2 leak fix is what exposed it: bounding the
  interpolation walk made the arm fail, and the arm was wrong.
- AC6 — `python tools/codebase-map/selftest.py` — `f"{{literal}}"` does NOT return `literal`.
- AC7 — `python tools/codebase-map/selftest.py` — covered by `-1` AC9's staged RED, which ran the
  same arm set against the old chain.
- AC8 — `python tools/codebase-map/selftest.py` — the whole suite passes.

## What this ledger does not claim

The `-1` corpus arm SKIPS when `repo_root()` is not a git checkout, and prints
`NOT a pass.` when it does. In this repo it measured 46 tracked Python files and 10295 ground-truth
identifiers, so the figures above are observations rather than a skipped arm reading green. An
adopter who copy-installs the kit gets the skip, and the printed line says so.

`-2` AC7 is recorded as AMENDED twice rather than OBSERVED once, because the criterion genuinely
changed shape between revisions. Writing it as a single OBSERVED line would have hidden that rev-1's
version could not fail.

## Round 2 of the closing review, and the two criteria it moved

Two of this build's own claims did not survive, and both are recorded as AMENDED rather than quietly
re-observed.

**`TOOL-aLexedStripper-5` AC3 was observed against an insufficient fix.** The ledger recorded it
green after rev-2 widened the unterminated flag. Round 2 measured a shape that repair does not
reach — a block-comment opener borne in a regex literal and closed by a later ordinary closer — and
round 1 had already prescribed the larger fix this run declined to take. Re-observed after the block
branch was deleted: `bash tools/hooks/agent-cap.test.sh`, and the arm is now in the suite rather
than only in a scratch harness.

**`TOOL-aLexedStripper-2`'s refutation of round 1's blocker 2 was WRONG.** This ledger's earlier
revision cited four fixtures denying at both BASE and HEAD. The fixtures could not reach the
mechanism: the verdict only moves when the fan sits on the SAME line as the quote. Round 2 supplied
one that does, and it ADMITTED where its apostrophe-free control DENIED. The finding was real, the
refutation was not, and the fix — leaving an unpaired quote as ordinary text — is what the
refutation had falsely claimed was already true.

**Six regression arms landed with those fixes**, because round 2's HIGH was that the three previous
code fixes had none: an unterminated block opener, a regex-borne opener with a later closer, an
apostrophe in a regex with the fan on its line, its control, an unpaired double quote, and the
fail-closed posture arm for a primitive named inside a block comment.
