#!/usr/bin/env bash
# Fixture self-test for check-memory-hygiene.sh — checks 3, 4, 5, 7 and 12 plus the empty-population
# guard. Builds a scratch git repo with conforming + violating fixtures and asserts each class fires
# (red) or stays silent (green), plus the disabled-when-blank conf contracts. Only the asserted
# checks' lines are read — the scratch repo intentionally reds others and that noise is ignored.
# Four more scratch trees at the bottom: half-migrated and young (the empty-population guard's two
# states), one carrying a .codebase-map.conf (the only place check 7's MAP_SUB branch is reachable),
# and one built by adopt-memory-tree.sh --scaffold itself, so the scaffolder is asserted against the
# GATE rather than against a second description of the scaffolder.
#   bash memory-tree/check-memory-hygiene.test.sh    # "PASS" + exit 0 = good
#
# The tree is FLAT (kit 1.5): builds/<slug>/, backlog/<FAMILY>.md, one root DECISIONS.md. The
# discipline is a value in the spec status header, not a directory.
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$HERE/check-memory-hygiene.sh"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
# The resolver, INLINE. This kit is copy-installed as a standalone directory, so `../lib/` does not
# exist in an adopting repo. The block below is byte-identical to tools/lib/resolve-python.sh and
# tools/lib/resolve-python.test.sh reds if any copy drifts.
#
# This file invoked `python3` BARE — the shape a ban keyed on `command -v` cannot see, which is how
# it survived the V5 migration. On a python3-only host it happened to work; on a host where the
# MS-Store stub answers for python3 it renders nothing and the young-tree arm below reds for a
# reason that has nothing to do with hygiene.
# >>> resolve_python — canonical copy: tools/lib/resolve-python.sh (byte-identical; gated)
resolve_python() {
  # Candidates in order: the caller's own published override, then $GOV_PYTHON, then the three
  # launcher names. Every candidate is ONE WORD — `py -3` cannot work here, because the probe quotes
  # the candidate and every consumer uses "$PY" as a single word (measured: exit 127).
  _rp_tried=""
  for _rp_c in "${1:-}" "${GOV_PYTHON:-}" python3 python py; do
    [ -n "$_rp_c" ] || continue
    _rp_tried="$_rp_tried $_rp_c"
    if "$_rp_c" -c "import sys" >/dev/null 2>&1; then
      printf '%s\n' "$_rp_c"
      return 0
    fi
  done
  {
    echo "resolve_python: no usable python launcher. Each candidate was RUN with -c 'import sys' and"
    echo "resolve_python: none exited 0 — being on PATH is not evidence (the Microsoft Store python3"
    echo "resolve_python: stub answers \`command -v\` and exits 9009 without running anything)."
    echo "resolve_python: tried:$_rp_tried"
    if [ -n "${1:-}" ]; then
      echo "resolve_python: the caller's override '$1' was tried FIRST and did not run."
    fi
    if [ -n "${GOV_PYTHON:-}" ]; then
      echo "resolve_python: GOV_PYTHON is set to '$GOV_PYTHON' and did not run. An override that is"
      echo "resolve_python: set and unusable is THIS failure, never a silent fall-through — the"
      echo "resolve_python: operator believes they chose, and would not have."
    fi
  } >&2
  return 1
}
# <<< resolve_python
_PY=$(resolve_python) || { echo "check-memory-hygiene.test: no usable python"; exit 2; }
cd "$TMP" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
# STREAMS_CUTOFF sits between the two fixture eras: the 2026-08-01 specs are grandfathered, the
# 2026-08-10 ones must carry `streams`. That is the arm the REAL corpus cannot exercise, because the
# cutoff is deliberately set ahead of every landed spec — so it is exercised here or nowhere.
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\nSTREAMS_CUTOFF="2026-08-05"\nSPEC_WITNESS_CUTOFF="2026-08-08"\nTOMBSTONE_ROOTS="docs"\nACCEPTANCE_LEDGER_CUTOFF="2026-08-10"\nACCEPTANCE_LEDGER_GRANDFATHER="ARCH-tFixture-73"\nFORK_MARK_CUTOFF="2026-08-05"\nREVIEW_VERDICT_CUTOFF="2026-08-05"\n' > .memory-tree.conf

D=memory/builds/tFixture
mkdir -p "$D/spec/subspecs" "$D/build" memory/backlog
printf 'sentinel\n' > memory/HYGIENE.md

good() { cat <<'EOF'
# ARCH-tFixture-1 — fixture

**Status:** SPECCED · rev-1 · 2026-08-01 · node a · Tier-2 · base 0123abcd

## 1. Goal

A goal.

## 2. Scope (IN)

- S1 something.

## 3. Non-goals (OUT)

- Nothing else.

## 4. Design

The design.

## 5. Production-readiness checklist

- security: N/A — fixture.

## 6. Acceptance criteria

- AC1 When run, `check-memory-hygiene.sh` passes.

## 7. Gates

- memory hygiene.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-01 · initial draft.
EOF
}
# The ten-section canon plus a post-SPEC10_CUTOFF date — the era the streams arms live in.
good10() { good | sed 's/2026-08-01/2026-08-10/g'; printf '\n## 10. Reuse audit\n\nNo existing seam fits.\n'; }

good > "$D/spec/2026-08-01-spec-tFixture-1.md"                                   # conforming -> silent
good | sed 's/$/\r/' > "$D/spec/2026-08-01-spec-tFixture-2.md"                   # CRLF twin -> silent
printf '# nested\nno header here\n## Wrong\nbody\n' > "$D/spec/subspecs/2026-08-01-spec-tFixture-3.md"  # nested+headerless -> red
good | sed 's/^## 4\. Design$/## 4. Blueprint/' > "$D/spec/2026-08-01-spec-tFixture-4.md"               # wrong canon -> red
printf '# t1\n\n**Status:** OPEN · rev-1 · 2026-08-01 · node a · Tier-1 · base 0123abcd\n\n## Whatever\n\nfree-form body

## 9. Revision log

- rev-1 · first\n' \
  > "$D/spec/2026-08-01-spec-tFixture-5.md"                                      # Tier-1 light profile -> silent
good | sed 's/^A goal\.$/Ship on YYYY-MM-DD./' > "$D/spec/2026-08-01-spec-tFixture-6.md"                # placeholder -> red
good | sed '/^The design\.$/d' > "$D/spec/2026-08-01-spec-tFixture-7.md"          # empty section body -> red
good | sed 's/rev-1 · 2026-08-01 · node/rev-2 · 2026-08-01 · node/' > "$D/spec/2026-08-01-spec-tFixture-8.md"  # header rev not in §9 -> red
good | sed 's/^\*\*Status:\*\* SPECCED/**Status:** WONTDO/' > "$D/spec/2026-08-01-spec-tFixture-9.md"   # bare WONTDO tail -> red
good | sed 's/^\*\*Status:\*\* SPECCED/**Status:** CLOSED/; s/^none$/- still deciding something/' \
  > "$D/spec/2026-08-01-spec-tFixture-10.md"                                     # terminal + open §8 -> red
printf '# old era\nfreeform, no header\n## Anything\n' > "$D/spec/2026-07-10-spec-tFixture-11.md"       # pre-cutoff -> silent
{ good; printf '\n```text\n~~~\n## bogus heading inside fence\n```\n'; } > "$D/spec/2026-08-01-spec-tFixture-12.md"  # fence torture -> silent
good > "$D/spec/2026-08-01-spec-tFixture-13.md"                                  # deleted after commit -> red
good | sed 's/^A goal\.$/Ship on YYYY-MM-DD./; /^The design\.$/d' \
  > "$D/spec/2026-08-01-spec-tFixture-14.md"                                     # TWO findings in ONE file -> red
good | sed 's/SPECCED/CLOSED/' > "$D/spec/2026-08-01-spec-tFixture-15.md"        # terminal + §8 `none` -> silent
# ---- §8's SECOND documented exit. TEMPLATE-SPEC promises a terminal spec may EITHER read `none`
# ---- OR have every question RESOLVED in place; only `none` was implemented, so a fully-resolved
# ---- spec could not go CLOSED. Fixture 15 above tests `none` (its comment used to claim RESOLVED
# ---- and did not test it), so these two arm the other exit and its boundary: ALL bullets resolved
# ---- is silent, ONE unresolved among resolved ones still reds.
good | sed 's/SPECCED/CLOSED/' \
  | sed 's/^none$/- **RESOLVED (owner, 2026-08-01): the only fork.** picked A/' \
  > "$D/spec/2026-08-01-spec-tFixture-43.md"                                     # terminal + all RESOLVED -> silent
# Derived from `good`, NOT hand-built like fixture 16: check 12 reports one finding per file, so a
# minimal spec fails the section canon first and never reaches the §8 branch at all — which is why
# fixture 16 carries a `miss` for this very message. A fixture that cannot reach the branch it names
# is the arm-passes-by-finding-nothing class. The second bullet is appended with `sed a\` because a
# newline in a sed REPLACEMENT does not expand portably, and a collapsed pair is one line containing
# RESOLVED — silent, and testing nothing.
good | sed 's/SPECCED/CLOSED/' \
  | sed 's/^none$/- **RESOLVED (owner, 2026-08-01): fork one.** picked A/' \
  | sed '/^- \*\*RESOLVED/a\- fork two, still open' \
  > "$D/spec/2026-08-01-spec-tFixture-44.md"                                     # one unresolved among resolved -> red
# ---- ...and the SAME PAIR in the OTHER sanctioned shape. TEMPLATE-SPEC says "One fork per bullet or
# ---- ### sub-head", and only the bullet was ever counted — so a spec using sub-heads scored zero
# ---- items, could never satisfy `items == resolved`, and could never go terminal however completely
# ---- its forks were answered. 45 is the arm that proves sub-heads are graded at all; 46 is the one
# ---- that proves they are still graded STRICTLY, because 45 alone would also pass if the branch
# ---- simply counted every sub-head as resolved.
good | sed 's/SPECCED/CLOSED/'   | sed 's/^none$/### F1 — the only fork · RESOLVED (owner, 2026-08-01): picked A/'   > "$D/spec/2026-08-01-spec-tFixture-45.md"                                     # sub-head + RESOLVED -> silent
good | sed 's/SPECCED/CLOSED/'   | sed 's/^none$/### F1 — fork one · RESOLVED (owner, 2026-08-01): picked A/'   | sed '/^### F1 /a\### F2 — fork two, still open'   > "$D/spec/2026-08-01-spec-tFixture-46.md"                                     # one sub-head unresolved -> red
# TRAILING BLANK LINES with §8 as the last section (TOOL-aBatchedLintel-1). Check 12 reproduces
# `sed "1d;\$d"`, whose deletes act on the CONCATENATED range output — so the range's last line, and
# therefore which line `\$d` removes, depends on whether the body still carries its trailing blanks.
# The pre-batch body lived in a command substitution, which DROPS them, so this file is SILENT on the
# terminal-§8 arm. A body array that retains them makes `- unresolved` the survivor and reds it.
printf '# t\n\n**Status:** CLOSED · rev-1 · 2026-08-01 · node a · Tier-2 · base 0123abcd\n\n## 8. Open questions\n\n- unresolved\n\n\n' \
  > "$D/spec/2026-08-01-spec-tFixture-16.md"
good | sed 's/^## /## X/' > "$D/spec/2026-08-01-spec-tFixture-17.md"             # every heading wrong -> long diff

# ---- STREAMS (kit 1.5). The discipline moved from the PATH into the header, so these four arms are
# ---- the only place the enum is exercised: on the real corpus the cutoff is set ahead of every
# ---- landed spec, which is what keeps the migration from retroactively redding history — and what
# ---- leaves the REQUIRED arm with no data. Upstream shipped exactly this arm vacuous once.
good10 | sed 's/base 0123abcd/base 0123abcd · streams architecture/' > "$D/spec/2026-08-10-spec-tFixture-18.md"  # post-cutoff WITH streams -> silent
good10 > "$D/spec/2026-08-10-spec-tFixture-19.md"                                # post-cutoff WITHOUT streams -> red
good | sed 's/base 0123abcd/base 0123abcd · streams bogus/' > "$D/spec/2026-08-01-spec-tFixture-20.md"   # illegal value, any date -> red
good | sed 's/base 0123abcd/base 0123abcd · streams architecture/' > "$D/spec/2026-08-01-spec-tFixture-21.md"  # pre-cutoff WITH streams -> silent
printf '# t22\n\n**Status:** OPEN · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd\n\n## Whatever\n\nbody\n' \
  > "$D/spec/2026-08-10-spec-tFixture-22.md"                                     # TIER-1 post-cutoff, no streams -> red

# ---- acceptance-witness arms. SPEC_WITNESS_CUTOFF sits between the eras exactly as
# ---- STREAMS_CUTOFF does, so the 2026-08-01 specs are grandfathered and the 2026-08-10 ones must
# ---- carry a witness. The real corpus cannot exercise this either: the cutoff is set ahead of
# ---- every landed spec. Every fixture below carries streams, or it would red for the STREAMS
# ---- reason instead and the arm would pass whether or not the branch it names exists.
wit() { good10 | sed "s/base 0123abcd/base 0123abcd · streams architecture/"; }
nowit() { sed 's|- AC1 When run, `check-memory-hygiene.sh` passes.|- **AC1** When run, it passes with nothing named.|'; }
unbold() { sed 's|- AC1 When run, `check-memory-hygiene.sh` passes.|- AC1. When run, it passes with nothing named.|'; }

wit | nowit  > "$D/spec/2026-08-10-spec-tFixture-50.md"   # post-cutoff, bolded, no witness -> red
wit          > "$D/spec/2026-08-10-spec-tFixture-51.md"   # post-cutoff, witness present    -> silent
good | sed "s/base 0123abcd/base 0123abcd · streams architecture/" | nowit \
             > "$D/spec/2026-08-01-spec-tFixture-52.md"   # PRE-cutoff, same bullet         -> silent
# the UNBOLDED label. A bold-requiring selector measured blind to 159 of 774 real bullets across 19
# specs, which made opting out of this rule two asterisks wide. This is the arm for that.
wit | unbold > "$D/spec/2026-08-10-spec-tFixture-53.md"   # post-cutoff, UNBOLDED, no witness -> red
# TIER-1, post-cutoff, witnessless. S3 says the rule runs on both tiers, and narrowing the branch
# guard to Tier-2 left this harness byte-identical until this fixture existed.
printf '# t54\n\n**Status:** OPEN · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture\n\n## 6. Acceptance criteria\n\n- **AC1** When run, it passes with nothing named.\n' \
  > "$D/spec/2026-08-10-spec-tFixture-54.md"
# ---- TOOL-cSettledDocket-3: Tier-1 twins for the two assertions HOISTED above the Tier-1 cut.
# ---- Before the hoist every one of these was silent, because `next` cut the record first.
printf '# t60

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 8. Open questions

**RESOLVED: prose, which the gate does not count as an item.**

## 9. Revision log

- rev-1 · first
' \
  > "$D/spec/2026-08-10-spec-tFixture-60.md"                                   # Tier-1 terminal, unresolved -> REDS
printf '# t61

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 8. Open questions

### Q — a question · RESOLVED (owner, 2026-08-10): settled at authoring

body

## 9. Revision log

- rev-1 · first
' \
  > "$D/spec/2026-08-10-spec-tFixture-61.md"                                   # Tier-1 terminal, resolved -> silent
printf '# t62

**Status:** CLOSED · rev-2 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 8. Open questions

none

## 9. Revision log

- rev-1 · only this one
' \
  > "$D/spec/2026-08-10-spec-tFixture-62.md"                                   # Tier-1, header rev-2 unlogged -> REDS
printf '# t63

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 7. Open questions

**RESOLVED: prose, numbered 7 because Tier-1 is canon-exempt.**

## 9. Revision log

- rev-1 · first
' \
  > "$D/spec/2026-08-10-spec-tFixture-63.md"                                   # §8 at ## 7. -> REDS only if keyed on TITLE
# PAST the cutoff, WITH items, one marked and one not: the per-item message, which no prose-only
# fixture can reach. The marked item carries its mark on a CONTINUATION line, which is where this
# corpus actually puts it — a fixture marking the opening line would pass under the loose reader too
# and would prove nothing about the tightening.
printf '# t65

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 8. Open questions

none - the forks below are RESOLVED in place.

- **F1 — answered?** options and a recommendation.
  RESOLVED (owner, 2026-08-10): picked A.

- **F2 — answered?** options, and nobody signed it.

## 9. Revision log

- rev-1 · first
'   > "$D/spec/2026-08-10-spec-tFixture-65.md"                                   # the PARKED gap: a fork below a `none` line, undetectable
printf '# t64

**Status:** CLOSED · rev-1 · 2026-08-10 · node a · Tier-1 · base 0123abcd · streams architecture

## 1. Goal

no open-questions section at all

## 9. Revision log

- rev-1 · first
' \
  > "$D/spec/2026-08-10-spec-tFixture-64.md"                                   # no such section -> must SAY SO, not pass
# The witness sits on a CONTINUATION line. The accumulator that folds continuations into their
# bullet had no fixture: deleting it left this harness unchanged while the real gate went red.
wit | sed 's|- AC1 When run, `check-memory-hygiene.sh` passes.|- **AC1** When run, the gate named below passes:\n  `bash tools/memory-tree/check-memory-hygiene.sh`|' \
  > "$D/spec/2026-08-10-spec-tFixture-55.md"   # witness on a continuation -> silent
# A hard-wrapped continuation that OPENS with a cross-reference to other ACs. The first selector
# read this as a new bullet head: it closed the real bullet early and invented a phantom label, so
# a spec whose every criterion carried a witness could red naming a label the file does not hold.
wit | sed 's|- AC1 When run, `check-memory-hygiene.sh` passes.|- **AC1** When the guard is removed, `run-gates.sh` reds and\n  AC1-AC3 all go with it.|' \
  > "$D/spec/2026-08-10-spec-tFixture-56.md"   # INDENTED continuation opens with an AC ref -> silent

# ---- CHECK 5: the optional FAMILY qualifier. It exists so one slug shared by two families survives
# ---- the merge into a single folder. The alternation is the CLOSED one from FAMILIES — a generic
# ---- [A-Z]+ would admit a family that does not exist and make the rejection arm vacuous.
# Both carry the UNBOUND binding line. Check 21 grades every record, and these two exist to exercise
# check 5's family alternation rather than the binding — without a line they would red check 21 and
# the global `miss` arm below would fire on a fixture that is doing exactly its job.
c5f='# f\n\n**Serves:** none — a check-5 fixture, exercising the family qualifier and not the binding\n'
printf "$c5f" > "$D/build/2026-08-01-build-ARCH-tFixture-1.md"                   # legal qualifier -> silent
printf "$c5f" > "$D/build/2026-08-01-build-XXXX-tFixture-2.md"                   # unknown family -> red

# ---- THE §9 REV RANGE, both sub-paths. The high-water scan used to run from `## 9.` to the end of
# ---- the body, so a rev-N in §10 satisfied the header rev. The branch has TWO conditions and the
# ---- range change makes BOTH newly reachable, so each gets its own fixture: one where §9 logs a
# ---- SMALLER rev, and one where §9 logs NONE at all. With only the first, an implementation that
# ---- closes the range for the maximum but leaves `seen` set below §9 passes while the masking
# ---- survives — which is the case the unit exists to fix.
good10 | sed 's/base 0123abcd/base 0123abcd · streams architecture/; s/^\*\*Status:\*\* SPECCED · rev-1/**Status:** SPECCED · rev-2/; s/^## 10\. Reuse audit$/## 10. Reuse audit\n\n- rev-99 · 2026-08-10 · a later section carrying a bigger number./' \
  > "$D/spec/2026-08-10-spec-tFixture-40.md"          # §9 logs rev-1, header rev-2, §10 has rev-99 -> RED
good10 | sed 's/base 0123abcd/base 0123abcd · streams architecture/; s/^- rev-1 · 2026-08-10 · initial draft\.$/- initial draft, with no rev token at all./; s/^## 10\. Reuse audit$/## 10. Reuse audit\n\n- rev-99 · 2026-08-10 · a later section carrying a bigger number./' \
  > "$D/spec/2026-08-10-spec-tFixture-41.md"          # §9 has NO rev token, §10 has rev-99 -> RED
good10 | sed 's/base 0123abcd/base 0123abcd · streams architecture/; s/^## 10\. Reuse audit$/## 10. Reuse audit\n\n- rev-99 · 2026-08-10 · a later section carrying a bigger number./' \
  > "$D/spec/2026-08-10-spec-tFixture-42.md"          # §9 logs rev-1, header rev-1 -> silent

# ---- CHECK 5 AT DEPTH. A recording one level deeper used to be governed by NOTHING: check 5 saw
# ---- only direct children, and check 12's population is files that already match the dated name, so
# ---- a free-named nested file was outside both by construction.
mkdir -p "$D/spec/units"
good > "$D/spec/units/2026-08-01-spec-tFixture-30-u1-nested-ok.md"   # conforming nested -> silent
printf 'x\n' > "$D/spec/units/scratch-notes.md"                      # free-named nested   -> RED
# A nested name carrying the unit tail — the shape that made the drafted grammar a red merge bar on
# 14 real files. Silent only because check 5's name ERE and check 12's selector now share one tail.
printf 'x\n' > "$D/spec/units/2026-08-01-spec-tFixture-31-u2-tail-ok.md"
mkdir -p memory/project memory/guides
# ---- CHECK 3: `project/` holds the five waiver registries and NOTHING else — no catch-all. The
# ---- `.md` on the stray is load-bearing rather than decoration: a stray `.txt`, an extensionless
# ---- file or a subdirectory already fell through to the reporting `*)` arm on the PRE-tightening
# ---- engine, so only a `.md` tells the two engines apart. These five are also the population the
# ---- selector-integrity guard measures — the half-migrated tree below is the same guard's red half.
printf '# legacy\n' > memory/project/legacy-files.txt
printf '# debt\n' > memory/project/curation-debt.txt
printf '# orphan waiver\n' > memory/project/id-orphan-waiver.txt
printf '# unresolved repo-path citations\n' > memory/project/corpus-path-unresolved.txt
printf '# unarmed branches\n' > memory/project/unarmed-branches.txt
printf '# stray\n' > memory/project/tstray.md          # a .md under project/ -> RED

# ---- CHECK 4: the folder is named for its SLUG alone. A date or FAMILY prefix is the pre-flatten
# ---- shape and must be rejected, or a half-migrated tree passes.
mkdir -p memory/builds/2026-08-01-ARCH-tBadFolder/spec
printf 'x\n' > memory/builds/2026-08-01-ARCH-tBadFolder/spec/2026-08-01-spec-tBadFolder-1.md

# ---- CHECK 3: backlog/ holds ONLY <FAMILY>.md. A stray name there is a backlog no status-vocabulary
# ---- check will ever read.
printf '# stray\n' > memory/backlog/notes.md

# ---- CHECK 7 fixture. The check had NO coverage here, and its per-file `_unfenced | awk` pair is
# ---- now one batched awk, so the exemptions and — above all — the line NUMBERING are what a
# ---- regression silently moves. The offending row sits at UNFENCED line 5 and RAW line 8; only a
# ---- counter over the unfenced stream reports 5. The 300/301 pair pins the threshold from both
# ---- sides, ASCII on purpose so bytes and characters agree on any awk build.
# ---- CHECK 1: a prompt-kind file belongs under builds/<slug>/prompts/ or archive/. The green
# ---- half is not decoration — the selector is a grep PAIR, and deleting the second grep is silent
# ---- unless something asserts that a correctly-placed prompt stays OUT of the report.
mkdir -p "$D/prompts"
printf 'x\n' > "$D/prompts/2026-08-01-prompt-tFixture-1.md"      # correctly placed -> silent
printf 'x\n' > memory/guides/kickoff-prompt.md                   # loose in the tree -> RED
# `guides/` because check 3 no longer admits a stray `.md` under `project/` — parking it there would
# make this fixture satisfy check 3 as well, and check 1's arm would no longer be its own evidence.
# `guides/` contents are unconstrained by check 3, and check 1 exempts only builds/*/prompts/ and
# archive/, so the arm still fires.

# ---- CHECK 2: link integrity, both states in ONE file. A resolver that stopped resolving anything
# ---- would still satisfy a red-only arm, so the live link is asserted absent from check 2's slice.
# ---- It moves WITH its live target: the resolving half is relative, so splitting the pair across
# ---- two directories would break the green arm for a reason that has nothing to do with check 2.
printf '# links\n\n[alive](kickoff-prompt.md)\n[dead](no-such-file.md)\n' > memory/guides/links.md

# ---- CHECK 10: a rotated archive is announced in lines 1-3 of the index it was cut from. Two
# ---- archives, one index, one mention — the referenced one is the control.
mkdir -p memory/archive
printf '# Decisions\n\nRotated: DECISIONS.2026-08-02.md\n\n- ARCH-tFixture-1 · a decision\n' > memory/DECISIONS.md
printf '# rotated\n' > memory/archive/DECISIONS.2026-08-01.md    # unreferenced   -> RED
printf '# rotated\n' > memory/archive/DECISIONS.2026-08-02.md    # named in the head -> silent

# ---- CHECK 6: the index byte/line cap. `guides/*.md` is in INDEX_SET — a guide is mandatory reading
# ---- the charter points a session at, and check 16 refuses a charter-cited file nothing caps — and
# ---- this file carries no other assertion, so growing it past 250 lines trips exactly one branch and
# ---- nothing else. It is entry-budget exempt (check 7), which the codebase-map tree below pins from
# ---- the other side: that exemption is the alternative the MAP_SUB branch used to overwrite.
{ printf '# tfixture guide\n'; i=1; while [ "$i" -le 760 ]; do printf -- '- row %d\n' "$i"; i=$((i+1)); done; } \
  > memory/guides/tfixture.md
# ---- ...and its GREEN counterpart, which is the arm that proves the guide cap actually widened.
# ---- 400 lines is OVER the row-document cap of 250 and UNDER the guide cap of 750, so it is named
# ---- by neither. Without this file the widening is unobservable: `tfixture.md` above would red at
# ---- 760 lines whether the guide cap were 750 or the original 250.
{ printf '# twide guide\n'; i=1; while [ "$i" -le 400 ]; do printf -- '- row %d\n' "$i"; i=$((i+1)); done; } \
  > memory/guides/twide.md

# ---- CHECK 11: the tombstone root, set in the conf above and BLANK in the two disabled-when-blank
# ---- runs further down — which is this branch's green half.
mkdir -p docs
printf '# resurrected\n' > docs/legacy-note.md

C7L=$(printf 'x%.0s' $(seq 1 340))
{ printf '# Backlog\n'
  printf '\n```text\n%s\n```\n' "$C7L"                             # >300 inside a fence  -> silent
  printf '# %s\n' "$C7L"                                           # >300 comment line    -> silent
  printf '|%s|\n' "$(printf -- '-%.0s' $(seq 1 340))"              # >300 table separator -> silent
  printf -- '- ARCH-tFixture-1 · OPEN · %s\n' "$C7L"               # >300 entry row       -> RED at :5
  printf '%s\n' "$(printf 'z%.0s' $(seq 1 300))"                   # exactly 300          -> silent
  printf '%s\n' "$(printf 'w%.0s' $(seq 1 301))"                   # exactly 301          -> RED at :7
  # CHECK 8 rides the same file, BELOW every line the check-7 arms number by hand. Two status
  # tokens in one row -> RED at :8; the one-token row at :5 above is the green control.
  printf -- '- ARCH-tFixture-9 · OPEN · CLOSED · two status tokens in one row\n'
} > memory/backlog/ARCH.md

# ---- RUN.md (2.3): the unattended run-state file, admitted at a build-folder root. Two hosts,
# ---- because every one of these contracts is silent-by-absence on its own.
# ---- tRunBig carries ALL THREE positive contracts in ONE file: check 6 names it (which is the only
# ---- proof RUN.md entered index_set at all), check 7 must NOT (the ex7 exemption, asserted on the
# ---- very file check 6 named — so it cannot be satisfied by a RUN.md that never joined the
# ---- population), and check 13 files its dash-row anchor under the owning build folder.
# ---- tRunOk is the under-cap control AND the check-13 control: it cites the same id INLINE IN
# ---- PROSE, which anchors nothing, so the collision arm is not merely "check 13 said something".
# ---- RUNSTATE.md is AC1's negative: a name matching NEITHER the whitelist NOR the dated-recording
# ---- grammar. Check 4 also admits `YYYY-MM-DD-<kind>[-<FAMILY>]-<slug>-<seq>.md` at a build root,
# ---- so an arbitrary dated name would red for the wrong reason and prove nothing.
runreadme() { printf -- '---\nslug: %s\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-%s-1\n---\n\n# %s\n' "$1" "$1" "$1"; }
mkdir -p memory/builds/tRunOk memory/builds/tRunBig
runreadme tRunOk  > memory/builds/tRunOk/README.md
runreadme tRunBig > memory/builds/tRunBig/README.md
printf '# run\n\nThe mandate names ARCH-tFixture-1 inline, in prose, so nothing anchors here.\n' \
  > memory/builds/tRunOk/RUN.md                                     # under cap, no anchor -> silent
printf '# not the run-state file\n' > memory/builds/tRunOk/RUNSTATE.md   # neither name nor grammar -> RED on 4
# ---- The ARCHIVED run-state file of kit 2.18. Check 4 admits it by GRAMMAR, not by equality — a
# ---- build gets more than one unattended run by ROTATING the finished record to this name, so the
# ---- family is unbounded and cannot be whitelisted the way RUN.md is. The NEAR-MISSES beside it
# ---- are what pin the grammar rather than merely the amendment: a loose spelling would pass the
# ---- admit arm while opening the build-folder grammar to anything at all, forever.
printf '# retired run\n\nNothing anchors here.\n' > memory/builds/tRunOk/RUN.ABORTED.a1b2c3d4.md
printf '# retired run\n' > memory/builds/tRunOk/RUN.notes.md              # no hash at all -> RED on 4
printf '# retired run\n' > memory/builds/tRunOk/RUN.ABORTED.a1b2c3.md    # 6 hex, not 8 -> RED on 4
printf '# retired run\n' > memory/builds/tRunOk/RUN.ABORTED.g1b2c3d4.md  # 'g' is not hex -> RED on 4
# ---- TWO further near-misses were WRITTEN AND REMOVED rather than left passing, because neither
# ---- tests the grammar on this fleet. A lowercase `RUN.aborted.<hash>.md` is the SAME PATH as the
# ---- admitted one on a case-insensitive filesystem — measured, only one file survives `git add`.
# ---- And a `.md.bak` tail never reaches the gate at all: this node's global excludesfile carries
# ---- `*.bak`, so `git ls-files` never sees it and check 4's population is the index. An arm that
# ---- passes because its fixture was never staged is this repo's fixture-passes-by-finding-nothing
# ---- class, and it would have read as coverage of an anchor it does not test.
# ---- tRunBig is over cap on BYTES, not lines. It used to be 265 lines / ~3 KB, and lines were its
# ---- only over-cap axis — which stopped being an axis when TOOL-aRelaxedShard-1 retired the row
# ---- class's line bound. THREE contracts are asserted THROUGH check 6 naming this file: that RUN.md
# ---- enters index_set at all, that check 7 EXEMPTS it, and the per-class scoping control. Letting it
# ---- fall silent would have vacated all three while every arm still passed.
{ printf '# run\n\n- ARCH-tFixture-1 · parked, and this dash row ANCHORS the id\n\n%s\n' "$C7L"
  RP=$(printf 'p%.0s' $(seq 1 80))
  i=1; while [ "$i" -le 260 ]; do printf -- '- note %d %s\n' "$i" "$RP"; i=$((i+1)); done; } \
  > memory/builds/tRunBig/RUN.md                                    # ~24 KB -> RED on 6 (BYTES); 340-char row -> silent on 7


# ---- acceptance-ledger fixtures (TOOL-dUnstalledConvoy-12). The cutoff sits between the eras, so the
# ---- same tree carries specs that owe a ledger and specs that cannot.
ledspec() {   # file · status · tier · heading · body
  { printf '# ARCH-tFixture-%s — a unit\n\n' "$1"
    printf '**Status:** %s · rev-1 · 2026-08-%s · node a · Tier-%s · base 1234abcd · streams architecture\n\n' "$2" "$3" "$4"
    printf '## 1. Goal\n\nA unit.\n\n## 2. Scope (IN)\n\n- S1 — a thing.\n\n## 3. Non-goals (OUT)\n\nnone.\n\n'
    printf '## 4. Design\n\nA mechanism.\n\n## 5. Production-readiness checklist\n\n- security — N/A.\n\n'
    printf '## %s\n\n%s\n\n' "$5" "$6"
    printf '## 7. Gates\n\nthe bar.\n\n## 8. Open questions\n\nnone\n\n## 9. Revision log\n\n- rev-1 · 2026-08-%s · initial draft.\n\n' "$3"
    printf '## 10. Reuse audit\n\nno existing seam fits.\n'
  } > "$D/spec/2026-08-$3-spec-tFixture-$1.md"
}
# 70: CLOSED Tier-2 after the cutoff, two criteria, ONE evidenced — the missing one is the whole check
ledspec 70 CLOSED 20 2 '6. Acceptance criteria' '- **AC1** — a thing, observed by `x`.
- **AC2** — another thing, observed by `y`.'
# 71: CLOSED Tier-2 after the cutoff whose acceptance section numbers NO criterion
ledspec 71 CLOSED 20 2 '6. Acceptance criteria' 'The unit works well.'
# 72: CLOSED Tier-2 whose ledger line is in NEITHER form
ledspec 72 CLOSED 20 2 '6. Acceptance criteria' '- **AC1** — a thing, observed by `x`.'
# 73: CLOSED Tier-2 after the cutoff, GRANDFATHERED by id
ledspec 73 CLOSED 20 2 '6. Acceptance criteria' '- **AC1** — a thing, observed by `x`.'
# 74: WONTDO owes nothing — a retired unit built nothing
ledspec 74 WONTDO 20 2 '6. Acceptance criteria' '- **AC1** — a thing, observed by `x`.'
# 75: CLOSED Tier-1 whose section 6 is GATES, which the format permits. Reading section 6 by NUMBER
#     rather than by heading text would red a spec that is legal under the format this gate enforces.
ledspec 75 CLOSED 20 1 '6. Gates' 'the bar.'
# 76: CLOSED Tier-2 dated BEFORE the cutoff — excluded, and it carries no ledger
ledspec 76 CLOSED 01 2 '6. Acceptance criteria' '- **AC1** — a thing, observed by `x`.'
sed -i 's/^- rev-1 · 2026-08-01 · initial draft.$/- rev-1 · 2026-08-01 · initial draft./' "$D/spec/2026-08-01-spec-tFixture-76.md"
mkdir -p "$D/build"
{ printf '# ledger\n\n**Serves:** journal ARCH-tFixture-70 ARCH-tFixture-72 ARCH-tFixture-73\n\n'
  # THE BOLD SPELLING, deliberately. The spec-side extractor accepts `- **AC1**` and the ledger
  # flattener accepted only `- AC1`, so one legal label was two labels depending on which half read
  # it — and the half nobody consults while writing a ledger was the strict one. Writing the fixture
  # in the bold form makes the `miss 'ARCH-tFixture-70/AC1'` arm below the pin for that.
  printf '**Evidences:** ARCH-tFixture-70\n- **AC1** — `x` — observed.\n\n'
  printf '**Evidences:** ARCH-tFixture-72\n- AC1 — it just works.\n\n'
  printf '**Evidences:** ARCH-tFixture-73\n- AC1 — `x` — observed.\n'
} > "$D/build/2026-08-20-build-ARCH-tFixture-70-1-ledger.md"
# CHECK 22's FIXTURES SIT ABOVE THE COMMIT, and that is load-bearing rather than tidy: the hygiene
# engine selects its population with `git ls-files`, so a fixture written after this commit is
# UNTRACKED and invisible to it. Written below, all six were ignored, check 22 graded nothing, and
# the four arms over them failed — which is how this suite went red at HEAD.
mkdir -p "$D/reviews"
# CHECK 22, four red fixtures plus a conforming control and a grandfather. Each differs from the
# control ONLY in its verdict token: a fixture that also moved the filename or the binding line could
# red for a reason that has nothing to do with the verdict, and would still look like coverage.
printf '**Serves:** spec-audit ARCH-tFixture-1\n\n## Verdict: CLEAN\n\nbody\n' \
  > "$D/reviews/2026-08-10-review-ARCH-tFixture-1-1.md"            # conforming -> silent
printf '**Serves:** spec-audit ARCH-tFixture-1\n\nbody with no verdict at all\n' \
  > "$D/reviews/2026-08-10-review-ARCH-tFixture-1-2.md"            # no verdict -> red
printf '**Serves:** spec-audit ARCH-tFixture-1\n\n## Verdict: SHIP WITH FIXES\n\nbody\n' \
  > "$D/reviews/2026-08-10-review-ARCH-tFixture-1-3.md"            # off-set token -> red
printf '**Serves:** spec-audit ARCH-tFixture-1\n\n## Verdict: BLOCKED\n\nb\n\n## Verdict: CLEAN\n' \
  > "$D/reviews/2026-08-10-review-ARCH-tFixture-1-4.md"            # two verdicts -> red
printf '**Serves:** spec-audit ARCH-tFixture-1\n\n## Verdict: BLOCKED - 2 blockers, 1 high\n\nb\n' \
  > "$D/reviews/2026-08-10-review-ARCH-tFixture-1-5.md"            # token plus a tally -> red
printf '**Serves:** spec-audit ARCH-tFixture-1\n\nno verdict, and dated BEFORE the cutoff\n' \
  > "$D/reviews/2026-08-01-review-ARCH-tFixture-1-6.md"            # grandfathered -> silent

git add -A && git commit -q -m fixtures --no-verify
rm -f "$D/spec/2026-08-01-spec-tFixture-13.md"   # tracked-but-absent only exists after the commit

out=$(bash "$SCRIPT" 2>/dev/null)
st=0; n=0
hit()  { n=$((n+1)); grep -qF "$1" <<<"$out" || { echo "FAIL missing: $1"; st=1; }; }
miss() { n=$((n+1)); if grep -qF "$1" <<<"$out"; then echo "FAIL unexpected: $1"; st=1; fi; }
hitl() { n=$((n+1)); grep -qxF "$1" <<<"$out" || { echo "FAIL missing exact line: $1"; st=1; }; }
lineno()  { grep -nF "$1" <<<"$out" | head -1 | cut -d: -f1; }
before()  { local a b; n=$((n+1)); a=$(lineno "$1"); b=$(lineno "$2")
            { [ -n "$a" ] && [ -n "$b" ] && [ "$a" -lt "$b" ]; } \
              || { echo "FAIL expected [$1] before [$2] (got '$a' vs '$b')"; st=1; }; }

hit  'tFixture-3.md (missing/invalid'
hit  'tFixture-4.md (## sections differ'
hit  'tFixture-6.md (unfilled skeleton placeholder'
hit  'tFixture-7.md (section with an empty body'
hit  'tFixture-8.md (header rev-2 not logged'
hit  'tFixture-9.md (WONTDO needs'
hit  'tFixture-10.md (terminal Status'
miss 'tFixture-1.md ('
miss 'tFixture-2.md ('
miss 'tFixture-5.md ('
miss 'tFixture-11.md ('
miss 'tFixture-12.md ('
# ---- check 22: the acceptance ledger (TOOL-dUnstalledConvoy-12).
hit  'ARCH-tFixture-70/AC2'                    # numbered, unevidenced — the defect this exists for
miss 'ARCH-tFixture-70/AC1'                    # ...and the evidenced sibling is silent
hit  'ARCH-tFixture-71'                        # a Tier-2 acceptance section numbering no criterion
hit  'ARCH-tFixture-72/AC1'                    # a line in neither legal form
miss 'ARCH-tFixture-73'                        # grandfathered BY ID, with its reason in the conf
miss 'ARCH-tFixture-74'                        # WONTDO owes nothing
miss 'ARCH-tFixture-75'                        # Tier-1 whose section 6 is Gates: legal, and located by HEADING
miss 'ARCH-tFixture-76'                        # dated before the cutoff
hit  'a CLOSED unit numbers an acceptance criterion that no journal record evidences, so nothing says which observation answered it and conformance is unreadable'
hit  'an acceptance-ledger line is in neither legal form, and there is no third: OBSERVED carries a backticked token, AMENDED names the revision, and anything else is a checkbox'
hit  'a CLOSED Tier-2 spec carries an acceptance-criteria section that numbers no criterion, so every claim about its coverage is vacuously true'

hit  'tFixture-13.md (tracked but missing from worktree'
hit  'tFixture-14.md (unfilled skeleton placeholder'
miss 'tFixture-15.md ('
miss 'tFixture-43.md ('                       # every §8 item RESOLVED satisfies a terminal status
# THE CUTOFF BOUNDARY, and these four arms are it. 44 and 46 are dated 2026-08-01, BEFORE the
# fixture cutoff, so they keep the loose first-line wording; 60 and 63 are dated 2026-08-10 and
# get the per-item wording. Same defect, two eras, two messages — which is what proves the gate
# is dated rather than merely strict.
hit  'tFixture-44.md (terminal Status with unresolved §8 Open questions'   # dated BEFORE the cutoff
miss 'tFixture-45.md ('                       # a ### sub-head fork, RESOLVED, satisfies a terminal status
hit  'tFixture-46.md (terminal Status with unresolved §8 Open questions'
hit  'tFixture-60.md (terminal Status and a §8 carrying neither an item nor a none form'   # PAST the cutoff: prose only
miss 'tFixture-61.md ('                      # resolved on Tier-1 is as green as resolved on Tier-2
hit  'tFixture-62.md (header rev-2 not logged in the §9 Revision log)'
# THE ARM THAT SEPARATES the fix from a half-fix: Tier-1 is canon-exempt, so a Tier-1 spec may
# legally number Open questions anything. Keyed on the NUMBER this is silent and the rule stays
# bypassable by doing exactly what the same gate permits; keyed on the TITLE it reds.
hit  'tFixture-63.md (terminal Status and a §8 carrying neither an item nor a none form'   # PAST the cutoff: prose only, §8 titled ## 7.
# ...and a range that never opens must SAY SO: silence and a resolved fork were the same byte.
hit  'tFixture-64.md (terminal Status and no Open questions section found'
# ---- check 22. The GRANDFATHER arm is what proves the cutoff is a date and not a switch, and the
# ---- token-plus-tally arm is what proves the check grades a MEMBER rather than a prefix — without
# ---- it, a predicate anchored on the leading word would pass and 44 corpus records would too.
# the check's own header text, which is what check-arms signs the branch with. The per-file lines
# below say WHICH record; this says the branch fired at all.
hit  'review records at/after REVIEW_VERDICT_CUTOFF whose verdict line is missing, duplicated, or outside the closed set'
hit  'review-ARCH-tFixture-1-2.md (no `## Verdict:` line'
hit  'review-ARCH-tFixture-1-3.md (verdict outside the closed set'
hit  'review-ARCH-tFixture-1-4.md (2 `## Verdict:` lines'
hit  'review-ARCH-tFixture-1-5.md (verdict outside the closed set'
miss 'review-ARCH-tFixture-1-1.md ('
miss 'review-ARCH-tFixture-1-6.md ('
# ---- THE PARKED GAP, PINNED AS A GAP. This fixture opens §8 with a `none` line and then carries two
# ---- option bullets, one marked and one not - an unresolved fork below an honest-looking `none`.
# ---- Neither reader catches it, and this arm says so rather than leaving the case unmentioned.
# ---- The per-item walk that WOULD catch it was withdrawn on measurement: this corpus does not
# ---- distinguish a fork bullet from an option bullet, so a per-item walk called a RESOLVED fork
# ---- unresolved on a live tracked spec, and any label-shape discriminator under-counts instead,
# ---- which is worse. Closing it needs §8 to have a regular shape, which is a scope change.
miss 'tFixture-65.md (terminal Status'
# ...while the canon check STAYS Tier-2-only. tFixture-5's `## Whatever` and its miss arm are that
# control, and it is what the cut still guards.
hit  'tFixture-16.md (## sections differ'
miss 'tFixture-16.md (terminal Status'
# Emission ORDER inside one file: a per-file loop got it for free, one awk over a driver does not.
before 'tFixture-14.md (unfilled skeleton placeholder' 'tFixture-14.md (section with an empty body'

# ---- the §9 range, both sub-paths. tFixture-42 is the silent control; the other two are the two
# ---- conditions of the branch. Each names the branch's OWN message.
hit  'tFixture-40.md (header rev-2 not logged in the §9 Revision log)'
hit  'tFixture-41.md (header rev-1 not logged in the §9 Revision log)'
miss 'tFixture-42.md ('

# ---- CHECK 5 AT DEPTH, three arms. Two of them would be satisfied by ABSENCE if the selector were
# ---- left unwidened — a file that is never selected is also silent — so the legacy arm is TWO-STATE
# ---- and the red arm is attributed inside check 5's OWN output slice. Check 5 prints a bare path and
# ---- checks 2, 9 and 12 all print paths from under spec/ too, so an unattributed `hit '<path>'`
# ---- would be satisfied by the wrong check.
c5block() { awk '/^HYGIENE check 5 FAILED/{g=1} g&&/^HYGIENE check [0-9]+ FAILED/&&!/check 5 FAILED/{g=0} g' <<<"$1"; }
# ...and the same slice for any check number. Attribution is not optional: checks 1, 2, 5, 9 and 12
# all print bare paths, so an unattributed `hit '<path>'` is satisfied by the wrong check's finding.
cblock() { awk -v n="$2" '
    index($0, "HYGIENE check " n " FAILED") == 1 { g = 1 }
    g && index($0, "HYGIENE check") == 1 && index($0, "HYGIENE check " n " FAILED") != 1 { g = 0 }
    g' <<<"$1"; }
chit()  { n=$((n+1)); cblock "$out" "$1" | grep -qF "$2" || { echo "FAIL check $1 did not report: $2"; st=1; }; }
cnot()  { n=$((n+1)); cblock "$out" "$1" | grep -qF "$2" && { echo "FAIL check $1 reported: $2"; st=1; }; }
c5hit()  { n=$((n+1)); c5block "$out" | grep -qF "$1" || { echo "FAIL check 5 did not report: $1"; st=1; }; }
c5miss() { n=$((n+1)); c5block "$out" | grep -qF "$1" && { echo "FAIL check 5 reported: $1"; st=1; }; }

c5hit  "$D/spec/units/scratch-notes.md"
c5miss "$D/spec/units/2026-08-01-spec-tFixture-30-u1-nested-ok.md"
c5miss "$D/spec/units/2026-08-01-spec-tFixture-31-u2-tail-ok.md"
# the conforming-nested arm is load-bearing for the KIND derivation: the kind comes from the
# SUBFOLDER (`spec`), not from the file's immediate parent (`units`). Do not delete it as redundant.
n=$((n+1))
grep -qF 'nesting is fine' <<<"$out" || { echo "FAIL the check-5 message does not say depth is allowed"; st=1; }

# ---- streams arms. Each asserts the branch's OWN text, not merely "check 12 fired": a bare
# ---- `check 12` mention is satisfied by any other finding in the same file.
miss 'tFixture-18.md ('
hit  'tFixture-19.md (filename date 2026-08-10 is on/after STREAMS_CUTOFF 2026-08-05'
hit  'tFixture-20.md (streams value(s) outside the enum: bogus'
miss 'tFixture-21.md ('
hit  'tFixture-22.md (filename date 2026-08-10 is on/after STREAMS_CUTOFF 2026-08-05'
# ---- acceptance-witness arms. Each asserts the branch's OWN text: a bare 'tFixture-50.md (' is
# ---- satisfied by any other check-12 finding in the same file.
hit  'tFixture-50.md (acceptance bullets naming no backticked witness'
miss 'tFixture-51.md ('
miss 'tFixture-52.md ('
hit  'tFixture-53.md (acceptance bullets naming no backticked witness'
hit  'tFixture-54.md (acceptance bullets naming no backticked witness'   # TIER-1: S3, both tiers
miss 'tFixture-55.md ('   # the witness is on a continuation line and counts for its bullet
miss 'tFixture-56.md ('   # a continuation opening with an AC reference is not a new bullet head
# the cutoff rides the message: check 12's own heading names SPEC_FORMAT_CUTOFF, which is the wrong
# cutoff for this violation and would misdirect the first author who hits it.
n=$((n+1))
grep -qF "required at/after SPEC_WITNESS_CUTOFF): 2026-08-08" <<<"$out" || { echo "FAIL the witness rejection does not name its own cutoff"; st=1; }
# and the offending LABEL, not merely the file
n=$((n+1))
grep -qE "tFixture-5[03][.]md .*AC1" <<<"$out" || { echo "FAIL the witness rejection does not name the bullet label"; st=1; }

# the legal set rides the message — a rejection that does not say what IS legal is a riddle
n=$((n+1))
grep -qF 'legal values: architecture' <<<"$out" || { echo "FAIL the streams rejection does not name the legal set"; st=1; }

# ---- FAMILY qualifier + flat folder naming + backlog shard naming
hit  'HYGIENE check 5 FAILED'
hit  '2026-08-01-build-XXXX-tFixture-2.md'
miss '2026-08-01-build-ARCH-tFixture-1.md'
hit  'memory/builds/2026-08-01-ARCH-tBadFolder (bad folder name'
hit  'memory/backlog/notes.md'

# ---- BRANCH ARMS. Each of these names its branch's OWN failure text, which is what
# ---- `check-arms.py` reads to decide a branch is armed. A bare `check N` mention is not an arm:
# ---- a substring test is satisfied by any other finding that happens to carry the same number, and
# ---- an ABSENCE assertion satisfies it too. Every unarmed branch is listed in
# ---- memory/project/unarmed-branches.txt and that pin is shrink-only.
hit  'unexpected entries (structure)'
# `project/` is defined as five named registries, so a stray `.md` there is check 3's finding and
# nobody else's — attributed through the slice, because checks 1, 2, 5, 9 and 12 also print bare paths.
chit 3 'memory/project/tstray.md'
# ...and the selector-integrity guard's GREEN half, on this tree: the five registries sit at exactly
# the depth the path expression expects, so check 3's population is non-empty and the
# empty-population report must NOT name it. Silence from check 3 itself would prove nothing — a
# mis-segmented selector is silent for the same reason a clean one is.
n=$((n+1))
grep -qE '^    check 3: ' <<<"$out" \
  && { echo "FAIL check 3 tripped the empty-population guard on a tree whose registries sit at the expected depth"; st=1; }
hit  'build-folder naming/shape'
hit  'prompt-kind files outside builds/*/prompts/ or archive/'
chit 1 'memory/guides/kickoff-prompt.md'
cnot 1 "$D/prompts/2026-08-01-prompt-tFixture-1.md"
hit  'broken relative .md links'
chit 2 'memory/guides/links.md -> no-such-file.md (MISSING)'
cnot 2 'links.md -> kickoff-prompt.md'
hit  'index files over cap (rotate to archive/<INDEX>.<YYYY-MM-DD>.md; a codebase-map dossier over cap is SPLIT into two dossiers instead — never rotate FOUNDATION.md, the map gate requires it)'
chit 6 'memory/guides/tfixture.md'
cnot 6 'memory/backlog/ARCH.md'
# ---- The guide is the ONE class that still carries a line bound, so its finding must still print
# ---- BOTH figures. The likeliest slip in the per-class message is dropping the line half from the
# ---- shared format for every class, which would name a guide for a LINE breach while printing only a
# ---- byte count under its own byte cap. TOOL-aRelaxedShard-1.
chit 6 '761L > 61440B/750L'
# ---- THE TWO HALVES OF THE PER-CLASS CAP. A guide between the row cap and the guide cap is silent;
# ---- a guide past the guide cap is named. Asserting only the second would pass identically under
# ---- one shared 250-line cap, which is the state this change moved away from.
cnot 6 'memory/guides/twide.md'
hit  'backlog rows without exactly one status token (OPEN SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO)'
chit 8 'memory/backlog/ARCH.md:8'
cnot 8 'memory/backlog/ARCH.md:5'

# ---- RUN.md, the four membership decisions of kit 2.3. Ordered so each one's evidence is visible.
# ---- (a) check 4 ADMITS the name at a build root and still rejects the near-miss.
cnot 4 'memory/builds/tRunOk/RUN.md'
cnot 4 'memory/builds/tRunBig/RUN.md'
chit 4 'memory/builds/tRunOk/RUNSTATE.md'
# ---- ...and the same pair for the ARCHIVED grammar of kit 2.18: admitted, with three near-misses
# ---- still named. The `chit` half is the one that pins the GRAMMAR — the `cnot` alone is satisfied
# ---- by any spelling loose enough to admit everything.
cnot 4 'memory/builds/tRunOk/RUN.ABORTED.a1b2c3d4.md'
chit 4 'memory/builds/tRunOk/RUN.notes.md'
chit 4 'memory/builds/tRunOk/RUN.ABORTED.a1b2c3.md'
chit 4 'memory/builds/tRunOk/RUN.ABORTED.g1b2c3d4.md'
# ---- (b) check 6 CAPS it. This is the load-bearing arm of the pair: a RUN.md that never entered
# ----     index_set is silent here for the same reason a compliant one is, so the green control
# ----     below proves nothing without it.
# ----     It is ALSO the scoping control for the per-class cap: at 265 lines it sits over the ROW
# ----     document cap and well under the guide cap, so it proves the widening did not leak out of
# ----     `guides/` into the row documents.
chit 6 'memory/builds/tRunBig/RUN.md'
cnot 6 'memory/builds/tRunOk/RUN.md'
# ---- (c) check 7 EXEMPTS it — asserted on the SAME file check 6 just named, so membership is
# ----     already established and only the exemption is under test. The file carries a 340-char
# ----     unfenced row: without the ex7 alternative this line fires.
n=$((n+1))
cblock "$out" 7 | grep -qF 'memory/builds/tRunBig/RUN.md' \
  && { echo "FAIL check 7 reported the run-state file's 340-char row — RUN.md lost its ex7 exemption"; st=1; }
# ---- (d) check 8 does NOT grow a RUN.md population. The run-phase vocabulary is deliberately not
# ----     the seven-token slot vocabulary — no token in it means "built and reviewed, not yet
# ----     landed" — and the unattended leg owns validating it. The dash row asserted on carries an
# ----     id and NO status token, which is exactly the shape check 8 reds on in a backlog shard.
cnot 8 'memory/builds/tRunBig/RUN.md'
# ---- (e) the anchor ban — the reason the authored region cites ids inline in prose — is armed in
# ----     its own scratch tree at the bottom of this file, NOT here. `armed()` in corpus_ids.py
# ----     turns checks 13-16 off outright when every pin is blank, and this conf deliberately sets
# ----     none, so a check-13 arm placed here would pass by exercising a disabled check. Measured:
# ----     `def_builds` held both slugs and `--check` still returned 0.
# check 9's green half is the freshly-scaffolded tree at the bottom of this file, which renders the
# index and then asserts the WHOLE gate exits 0. This tree never renders it, so it drifts.
hit  'generated build index differs from a fresh render'
hit  'rotated archives not referenced from their live index (lines 1-3)'
chit 10 'memory/archive/DECISIONS.2026-08-01.md'
cnot 10 'DECISIONS.2026-08-02.md'
hit  '/ is the only sanctioned memory root'
chit 11 'docs/legacy-note.md'
hit  'recording-file names not matching YYYY-MM-DD-<kind>[-<FAMILY>]-<slug>-<seq>.md (and not grandfathered)'
hit  'index entry lines over their declared cap'
hit  'spec files dated >='

# ---- the section-canon DIFF EXCERPT. The batched check 12 emits a sentinel record and rebuilds the
# ---- excerpt afterwards with the original `diff | head -6 | sed`, so BOTH halves need pinning: it
# ---- is a real diff, indented four spaces, capped at six lines, and the sentinel byte itself never
# ---- reaches the output. Without these, deleting the sentinel or shrinking the cap is invisible.
n=$((n+1))
hit  'tFixture-17.md (## sections differ'
hitl '    < ## 4. Design'
hitl '    > ## 4. Blueprint'
hitl '    ---'
case "$out" in *$'\001'*) echo "FAIL the check-12 diff sentinel leaked into the output"; st=1;; esac
n=$((n+1))
n17=$(awk '/tFixture-17\.md \(## sections differ/{g=1; next} g && /^    /{c++; next} g{exit} END{print c+0}' <<<"$out")
[ "$n17" = 6 ] || { echo "FAIL the diff excerpt for a wholly-renamed spec is $n17 lines, expected the head -6 cap"; st=1; }

# ---- CHECK 7: unfenced line NUMBERING and the three exemptions.
n=$((n+1))
hit  'HYGIENE check 7 FAILED'
# The finding now NAMES THE CAP it was measured against. With a per-class width (300 for an index,
# 350 for a build README) "419 chars" alone does not tell an operator whether that is a violation.
n7=$(grep -cE '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\)$' <<<"$out")
[ "$n7" = 2 ] || { echo "FAIL check 7 emitted $n7 findings, expected exactly 2 (fence, comment and separator are exempt; the 300-byte row is under the cap)"; st=1; }
n=$((n+1))
hitl 'memory/backlog/ARCH.md:7 (301 chars > 300)'
miss 'memory/backlog/ARCH.md:6 ('
c7line=$(grep -E '^memory/backlog/ARCH\.md:[0-9]+ \([0-9]+ chars > [0-9]+\)$' <<<"$out" | head -1)
case "$c7line" in 'memory/backlog/ARCH.md:5 ('*) ;;
  *) echo "FAIL check 7 reported '$c7line'; expected the offending row at UNFENCED line 5 (raw line 8)"; st=1;; esac

# ---- --staged: `in_scope` is the ONLY thing deciding selection there, so no full-mode arm above can
# ---- see a scoping regression. A red must be the committer's own file, never another stream's debt.
n=$((n+1))
git reset -q
printf 'x\n' >> "$D/spec/2026-08-01-spec-tFixture-4.md"
git add "$D/spec/2026-08-01-spec-tFixture-4.md"
outs=$(bash "$SCRIPT" --staged 2>/dev/null)
grep -qF 'tFixture-4.md (## sections differ' <<<"$outs" \
  || { echo "FAIL --staged missed the staged file's own finding"; st=1; }
n=$((n+1))
grep -qF 'tFixture-10.md (' <<<"$outs" \
  && { echo "FAIL --staged reported an UNSTAGED file's finding"; st=1; }
# check 7 carries its own `in_scope` filter, and the arm above stages only a SPEC — so an unstaged
# over-cap index file must stay silent. Without this, dropping check 7's in_scope is invisible.
n=$((n+1))
grep -qF 'HYGIENE check 7' <<<"$outs" \
  && { echo "FAIL --staged reported check 7 for an UNSTAGED index file"; st=1; }
# the empty-population guard must NOT fire in --staged mode: an empty staged set is the normal case.
n=$((n+1))
grep -qF 'selected an EMPTY population' <<<"$outs" \
  && { echo "FAIL --staged tripped the empty-population guard, which is the normal staged case"; st=1; }
git reset -q && git checkout -q -- "$D/spec/2026-08-01-spec-tFixture-4.md"
# ...and the other direction: staging the index file DOES surface its own over-cap row.
n=$((n+1))
printf '\n' >> memory/backlog/ARCH.md
git add memory/backlog/ARCH.md
outs7=$(bash "$SCRIPT" --staged 2>/dev/null)
grep -qF 'HYGIENE check 7' <<<"$outs7" \
  || { echo "FAIL --staged missed check 7 on the staged index file"; st=1; }
git reset -q && git checkout -q -- memory/backlog/ARCH.md

# ---- SOURCE-level assertions. These three hazards cannot be reached by any fixture on this
# ---- platform, so they are asserted against the engine's text instead.
#
# 1. Every getline loop strips a trailing CR. On Linux a CRLF worktree delivers the \r into awk and
#    the fence toggle and every compare break. On a Cygwin node the C runtime strips CR BEFORE awk
#    sees a byte — measured through a filename argument, through `getline line < f` AND through a
#    pipe — so the CRLF fixture above passes identically with and without the guard.
n=$((n+1))
ncr=$(awk '
  index($0, "while ((getline line < f) > 0)") { open[++n] = NR; guarded[n] = 0 }
  n > 0 && NR > open[n] && NR <= open[n] + 2 && index($0, "sub(/\\r$/, \"\", line)") { guarded[n] = 1 }
  END { for (i = 1; i <= n; i++) if (!guarded[i]) print "line " open[i]
        if (n < 3) print "only " n " getline loop(s) — expected at least 3" }
' "$SCRIPT")
[ -z "$ncr" ] || { echo "FAIL a getline loop with no trailing-CR strip within 2 lines: $ncr"; st=1; }
# 2. Interval expressions stay spelled out inside the batched awk. On a build that does not honour
#    `{8}` the header regex demands those literal bytes and never matches, so every post-cutoff spec
#    reds with "missing/invalid **Status:** header" — a loud break of a check that works today.
#    The predicate matches `{` followed by a DIGIT, not a bare `{` — every one of these lines ends in
#    the `) {` that opens its own if-block, so a bare-brace ban flags the innocent and passes nothing.
n=$((n+1))
ivl=$(grep -nE 'hdr [!=]~ /' "$SCRIPT" | grep -E '\{[0-9]' || true)
[ -z "$ivl" ] || { echo "FAIL an interval expression survives in a batched-awk regex: $ivl"; st=1; }
# 3. The §9 range CLOSES. `check-arms` cannot help here: check 12's per-spec findings are awk `print`
#    statements funnelled into one `fail 12` that is already armed, so deleting the reset moves no
#    branch, no floor and — measured — no corpus verdict. The fixtures above and this line are the
#    whole of the protection.
n=$((n+1))
r9=$(awk '/in9 = 1/{f=1} f&&/else if \(in9 && L ~ \/\^## \/\) in9 = 0/{ok=1} END{print ok+0}' "$SCRIPT")
[ "$r9" = 1 ] || { echo "FAIL the §9 rev-scan range no longer closes on the next ## heading"; st=1; }
# 4. Check 7 takes NO locale prefix. `length()` decides its verdict and its character-versus-byte
#    meaning belongs to the awk build and the ambient locale; check 8's `LC_ALL=C xargs` seventeen
#    lines below sorts, it does not measure, and is not the pattern to copy here.
#    Comment lines are stripped first: the region carries prose explaining exactly this ban, and a
#    predicate that fires on the comment documenting the fix is the classic self-inflicted red.
n=$((n+1))
lc7=$(awk '/^# 7 — /{f=1} /^# 8 — /{f=0} f && $0 !~ /^[[:space:]]*#/ && /LC_ALL/{print NR ": " $0}' "$SCRIPT")
[ -z "$lc7" ] || { echo "FAIL check 7 carries a locale prefix — length() must stay locale-dependent: $lc7"; st=1; }
# 5. Check 7's exemption expression keeps ONE spelling of the guides/ alternative. The MAP_SUB branch
#    used to REBUILD the whole expression, and the rebuild silently omitted `guides/` — so on any repo
#    carrying a .codebase-map.conf every guide entered the entry-budget population and no assertion
#    moved. The fixture below catches today's shape; this catches the RESHAPE that would lose it
#    again, which no fixture can, because the second spelling would still be a valid expression.
n=$((n+1))
ex7asg=$(grep -nE 'ex7=' "$SCRIPT")
ex7g=$(printf '%s\n' "$ex7asg" | grep -cF '/guides/')
[ "$ex7g" = 1 ] || { echo "FAIL the ex7 exemption carries $ex7g spellings of the guides/ alternative, expected exactly 1"; st=1; }
n=$((n+1))
ex7bad=$(printf '%s\n' "$ex7asg" | tail -n +2 | grep -vF '$ex7' || true)
[ -z "$ex7bad" ] || { echo "FAIL an ex7 re-assignment rebuilds the expression instead of appending to \$ex7: $ex7bad"; st=1; }

# disabled-when-blank contracts: same tree, each cutoff removed in turn.
n=$((n+1))
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSTREAMS_CUTOFF="2026-08-05"\n' > .memory-tree.conf
out2=$(bash "$SCRIPT" 2>/dev/null)
if grep -qF 'HYGIENE check 12' <<<"$out2"; then echo "FAIL: check 12 ran with blank SPEC_FORMAT_CUTOFF"; st=1; fi
n=$((n+1))
if ! grep -qF 'HYGIENE check 12' <<<"$out"; then echo "FAIL: check 12 never fired with cutoff armed"; st=1; fi
n=$((n+1))
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\n' > .memory-tree.conf
out3=$(bash "$SCRIPT" 2>/dev/null)
if grep -qF 'on/after STREAMS_CUTOFF' <<<"$out3"; then echo "FAIL: the streams requirement fired with a blank STREAMS_CUTOFF"; st=1; fi
n=$((n+1))
if grep -qF 'no backticked witness' <<<"$out3"; then echo "FAIL: the witness requirement fired with a blank SPEC_WITNESS_CUTOFF"; st=1; fi
# docs/legacy-note.md is still tracked in this run — only the conf key went away.
n=$((n+1))
if grep -qF 'is the only sanctioned memory root' <<<"$out3"; then echo "FAIL: check 11 ran with a blank TOMBSTONE_ROOTS"; st=1; fi
# an ILLEGAL value is still illegal with the cutoff blank — validation and the ratchet are separate
n=$((n+1))
grep -qF 'tFixture-20.md (streams value(s) outside the enum' <<<"$out3" \
  || { echo "FAIL: an illegal streams value went unchecked with a blank STREAMS_CUTOFF"; st=1; }
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\nSTREAMS_CUTOFF="2026-08-05"\n' > .memory-tree.conf

# ---- the legacy grandfather, BOTH STATES. Silence alone proves nothing here: an unwidened selector
# ---- is silent for exactly the same file. Listed -> silent; the line removed -> the same file reds.
n=$((n+1))
printf '# legacy\n%s\n' "$D/spec/units/scratch-notes.md" > memory/project/legacy-files.txt
git add -A >/dev/null 2>&1; git commit -q -m legacy --no-verify
outl=$(bash "$SCRIPT" 2>/dev/null)
awk '/^HYGIENE check 5 FAILED/{g=1} g&&/^HYGIENE check [0-9]+ FAILED/&&!/check 5 FAILED/{g=0} g' <<<"$outl" \
  | grep -qF "$D/spec/units/scratch-notes.md" \
  && { echo "FAIL a legacy-listed nested file still reds check 5"; st=1; }
n=$((n+1))
printf '# legacy\n' > memory/project/legacy-files.txt
git add -A >/dev/null 2>&1; git commit -q -m unlegacy --no-verify
outu=$(bash "$SCRIPT" 2>/dev/null)
awk '/^HYGIENE check 5 FAILED/{g=1} g&&/^HYGIENE check [0-9]+ FAILED/&&!/check 5 FAILED/{g=0} g' <<<"$outu" \
  | grep -qF "$D/spec/units/scratch-notes.md" \
  || { echo "FAIL removing the legacy line did not make the nested file red again"; st=1; }

# ---- the GRANDFATHER lists' stale-line guards, both of them. A list naming a path git no longer
# ---- tracks is a permanent silent exemption — the exempted file is gone, so nothing ever reds and
# ---- nothing ever says why. Each list gets a dead line AND a live one in the same run: the live one
# ---- must stay unreported, or the guard is merely "the list is non-empty".
n=$((n+1))
printf '# legacy\n%s\nmemory/project/gone-forever.md\n' "$D/spec/units/scratch-notes.md" > memory/project/legacy-files.txt
printf '# debt\nmemory/backlog/ARCH.md\nmemory/project/also-gone.md\n' > memory/project/curation-debt.txt
git add -A >/dev/null 2>&1; git commit -q -m stale --no-verify
outst=$(bash "$SCRIPT" 2>/dev/null)
grep -qF 'legacy-files.txt lists paths that no longer exist (stale-line guard)' <<<"$outst" \
  || { echo "FAIL the legacy-files stale-line guard did not fire on a dead entry"; st=1; }
n=$((n+1))
grep -qF 'memory/project/gone-forever.md' <<<"$outst" \
  || { echo "FAIL the legacy-files stale-line guard did not name the dead entry"; st=1; }
n=$((n+1))
grep -qF 'curation-debt.txt lists paths that no longer exist (stale-line guard)' <<<"$outst" \
  || { echo "FAIL the curation-debt stale-line guard did not fire on a dead entry"; st=1; }
n=$((n+1))
grep -qF 'memory/project/also-gone.md' <<<"$outst" \
  || { echo "FAIL the curation-debt stale-line guard did not name the dead entry"; st=1; }
# the LIVE debt entry is exempted, not reported: it is the over-cap arm's own file, and check 6
# branch 1 must now stay silent about it. That is the grandfather working and the guard not
# over-firing, in one assertion.
n=$((n+1))
awk -v n=6 'index($0,"HYGIENE check " n " FAILED")==1{g=1} g&&index($0,"HYGIENE check")==1&&index($0,"HYGIENE check " n " FAILED")!=1{g=0} g' <<<"$outst" \
  | grep -qF 'memory/backlog/ARCH.md (' \
  && { echo "FAIL a curation-debt-listed file was still capped by check 6"; st=1; }
printf '# legacy\n' > memory/project/legacy-files.txt
printf '# debt\n' > memory/project/curation-debt.txt
git add -A >/dev/null 2>&1; git commit -q -m unstale --no-verify

# ---- the EMPTY-POPULATION guard, in two scratch trees, because it has to tell two states apart.
#
# (a) A HALF-MIGRATED tree: the files exist, at the PRE-flatten paths. Every flat selector matches
#     nothing, prints nothing, and is indistinguishable from a passing check. This is the state the
#     guard exists for, and the state a mis-segmented selector would produce on a correct tree.
H=$TMP/halfmigrated
mkdir -p "$H/memory/project" "$H/memory/architecture/project" "$H/memory/architecture/builds/2026-08-01-ARCH-tOld/spec"
( cd "$H" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\n' > .memory-tree.conf
  printf '# r\n' > memory/README.md
  printf '# old\n' > memory/architecture/builds/2026-08-01-ARCH-tOld/spec/2026-08-01-spec-tOld-1.md
  printf '# b\n' > memory/architecture/BACKLOG.md
  # A registry at the PRE-flatten path. It is the PRECONDITION for check 3's guard and nothing else:
  # the un-segmented count asks "does a registry exist anywhere under the memory root?" and answers
  # yes, while the flat selector `memory/project/*.txt` matches none — which is exactly the
  # mis-segmented shape the guard exists to catch, and is silent without it.
  n=$((n+1))
  printf '# legacy\n' > memory/architecture/project/legacy-files.txt
  git add -A && git commit -q -m half --no-verify )
outh=$(cd "$H" && bash "$SCRIPT" 2>/dev/null); rch=$?
[ "$rch" = 0 ] && { echo "FAIL a half-migrated tree exited 0 — every flat selector matched nothing and the gate was green"; st=1; }
n=$((n+1))
grep -qF 'selected an EMPTY population' <<<"$outh" || { echo "FAIL no empty-population report on a half-migrated tree"; st=1; }
n=$((n+1))
for c in 3 4 5 8 12; do
  grep -qE "^    check $c: " <<<"$outh" || { echo "FAIL check $c did not report its empty population on a half-migrated tree"; st=1; }
done
n=$((n+1))
grep -qF 'the selector is mis-segmented' <<<"$outh" || { echo "FAIL the empty-population report does not name the cause"; st=1; }
#
# (b) A FRESHLY SCAFFOLDED tree: no builds at all, nothing mis-segmented. The guard MUST stay quiet,
#     or `adopt --scaffold` hands every new adopter a red tree on its first run. The precondition is
#     what separates this case from (a), and without this arm the guard's first draft did exactly
#     that — measured, not imagined.
Y=$TMP/young
mkdir -p "$Y/memory/project" "$Y/memory/backlog"
( cd "$Y" && git init -q . && git config user.email t@t.test && git config user.name t
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\n' > .memory-tree.conf
  printf '# r\n' > memory/README.md
  printf '# ARCH backlog\n' > memory/backlog/ARCH.md
  # the generator reads `git ls-files`, so stage first, render, then stage the render — the same
  # order `adopt-memory-tree.sh --scaffold` uses, because this arm is standing in for its output
  n=$((n+1))
  git add -A && "$_PY" "$HERE/gen_build_index.py" --write >/dev/null && git add -A
  git commit -q -m young --no-verify )
outy=$(cd "$Y" && bash "$SCRIPT" 2>/dev/null); rcy=$?
grep -qF 'selected an EMPTY population' <<<"$outy" \
  && { echo "FAIL a freshly scaffolded tree tripped the empty-population guard"; st=1; }
# This rc=0 is also the arm for "a tree with no RUN.md anywhere is green and silent" (kit 2.3): the
# run-state file is OPTIONAL, and a whitelist entry that quietly became a requirement would red here
# and in the scaffolder arm below. RUN.md joins no pop_guard population, deliberately — a young tree
# has no run to record, so there is no precondition that could make its absence a mis-segmentation.
n=$((n+1))
[ "$rcy" = 0 ] || { echo "FAIL a freshly scaffolded tree is not clean (rc=$rcy):"; printf '%s\n' "$outy" | sed 's/^/      /'; st=1; }

# ---- (c) A tree carrying a .codebase-map.conf. This is the ONLY place check 7's MAP_SUB branch is
# ----     reachable: every tree above writes no such conf, so `MAP_SUB` is empty throughout and the
# ----     branch that rebuilt the exemption expression was dormant in this whole file. It went live
# ----     the day this repo adopted codebase-map, and the rebuild had dropped the `guides/`
# ----     alternative — a LOOSENING, which nothing here could have seen: every guide silently
# ----     entered the entry-budget population and the gate stayed green. Three over-cap rows, one
# ----     per exemption state, so the arm cannot be satisfied by a check 7 that reports nothing.
n=$((n+1))
G=$TMP/mapped
mkdir -p "$G/memory/project" "$G/memory/guides" "$G/memory/map/features" "$G/memory/backlog"
( cd "$G" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  # ---- The two cap keys are declared APART here, and that is PART OF THE ARMS rather than setup.
  # ---- Both SHIP at 20,480, so a fixture declaring neither makes the row and dossier bounds ONE
  # ---- number, the band between them empty, and the dossier arm satisfiable by an engine carrying no
  # ---- dossier branch at all. Do not "simplify" these two settings away.
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nINDEX_CAP_BYTES="61440"\nINDEX_CAP_LINES="0"\nDOSSIER_CAP_BYTES="20480"\n' > .memory-tree.conf
  printf 'MAP_ROOT=memory/map\n' > .codebase-map.conf
  printf '# r\n' > memory/README.md
  printf '# ARCH backlog\n' > memory/backlog/ARCH.md
  printf '# legacy\n' > memory/project/legacy-files.txt
  L=$(printf 'x%.0s' $(seq 1 340))
  printf '# map index\n\n- %s\n' "$L" > memory/map/README.md          # NOT exempt      -> RED
  printf '# a guide\n\n- %s\n' "$L"  > memory/guides/tguide.md        # exempt (guides) -> silent
  printf '# a dossier\n\n- %s\n' "$L" > memory/map/features/tdoss.md  # exempt (map)    -> silent
  # ---- CHECK 6, the dossier class. ~31 KB sits BETWEEN DOSSIER_CAP_BYTES and INDEX_CAP_BYTES, so
  # ---- this pair is the only observation that tells a dossier class from a row class under a larger
  # ---- bound: the dossier is NAMED and a row document of the SAME SIZE is SILENT. Either one alone
  # ---- is satisfied by an engine with no dossier branch.
  BB=$(printf 'b%.0s' $(seq 1 120))
  { printf '# fat dossier\n'; i=1; while [ "$i" -le 250 ]; do printf -- '- %s\n' "$BB"; i=$((i+1)); done; } \
    > memory/map/features/tfat.md                                    # ~31 KB > 20480 -> RED on 6
  { printf '# fat rows\n'; i=1; while [ "$i" -le 250 ]; do printf -- '- %s\n' "$BB"; i=$((i+1)); done; } \
    > memory/backlog/ZFAT.md                                         # ~31 KB < 61440 -> silent on 6
  git add -A && "$_PY" "$HERE/gen_build_index.py" --write >/dev/null && git add -A
  git commit -q -m mapped --no-verify )
outm=$(cd "$G" && bash "$SCRIPT" 2>/dev/null)
cblock "$outm" 7 | grep -qF 'memory/map/README.md:' \
  || { echo "FAIL check 7 did not report the over-cap row in the map index, which carries no exemption"; st=1; }
n=$((n+1))
cblock "$outm" 7 | grep -qF 'memory/guides/tguide.md' \
  && { echo "FAIL check 7 reported a guide's over-cap row — the MAP_SUB branch dropped the guides/ exemption again"; st=1; }
n=$((n+1))
cblock "$outm" 7 | grep -qF 'memory/map/features/tdoss.md' \
  && { echo "FAIL check 7 reported a codebase-map dossier's over-cap row — dossiers are detail files"; st=1; }
# ---- CHECK 6, THE DOSSIER CLASS (TOOL-aRelaxedShard-1). The pair, and only the pair, discriminates.
n=$((n+1))
cblock "$outm" 6 | grep -qF 'memory/map/features/tfat.md' \
  || { echo "FAIL check 6 did not name a dossier over DOSSIER_CAP_BYTES — the dossier class is not applied"; st=1; }
n=$((n+1))
cblock "$outm" 6 | grep -qF 'memory/backlog/ZFAT.md' \
  && { echo "FAIL check 6 named a row document at the SAME size as the over-cap dossier — the dossier bound leaked onto the row class, which is what an unguarded MAP_SUB prefix does"; st=1; }
# ---- ...and the message for a dossier carries no line figure, because the class has no line bound.
n=$((n+1))
cblock "$outm" 6 | grep -qF '; no line cap for this class' \
  || { echo "FAIL a dossier finding did not carry the no-line-cap message shape"; st=1; }

# ---- (c2) THE EMPTINESS GUARD, in a tree with NO codebase map. `index(f, "")` is 1 for EVERY string,
# ----      so an unguarded dossier selector resolves to a bare prefix and hands the DOSSIER bound to
# ----      the whole tree — silently undoing the row cap. Asserting mere silence in a no-map tree
# ----      proves nothing: without a .codebase-map.conf no dossier path is in check 6's population at
# ----      all, so silence comes from index_set membership one layer ABOVE the branch under test. The
# ----      discriminating form is a ROW document sized BETWEEN the two declared bounds: correct under
# ----      the guard, RED under the degenerate selector.
n=$((n+1))
NG=$TMP/nomap
mkdir -p "$NG/memory/project" "$NG/memory/backlog"
( cd "$NG" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nINDEX_CAP_BYTES="61440"\nINDEX_CAP_LINES="0"\nDOSSIER_CAP_BYTES="20480"\n' > .memory-tree.conf
  printf '# r\n' > memory/README.md
  printf '# legacy\n' > memory/project/legacy-files.txt
  NB=$(printf 'n%.0s' $(seq 1 120))
  { printf '# fat rows\n'; i=1; while [ "$i" -le 250 ]; do printf -- '- %s\n' "$NB"; i=$((i+1)); done; } \
    > memory/backlog/ARCH.md                                         # ~31 KB: over the dossier bound, under the row bound
  git add -A && git commit -q -m nomap --no-verify )
outn=$(cd "$NG" && bash "$SCRIPT" 2>/dev/null)
cblock "$outn" 6 | grep -qF 'memory/backlog/ARCH.md' \
  && { echo "FAIL check 6 applied the DOSSIER bound to a row document in a tree with no codebase map — the dossier selector is missing its emptiness guard"; st=1; }

# ---- (d) THE RUN.md ANCHOR BAN (kit 2.3), in its OWN tree because `armed()` in corpus_ids.py turns
# ----     checks 13-16 off outright when every pin is blank, and the main fixture conf sets none.
# ----     Measured before writing this: on that tree `def_builds` held BOTH slugs and `--check`
# ----     still returned 0 — an arm placed there would have passed against a disabled check.
# ----
# ----     A dash row inside a build folder ANCHORS its id (`- <id> ·` is one of the four anchor
# ----     shapes), so a run-state file opening a parked entry that way makes its own build a second
# ----     claimant of an id another build defines. That is why the authored region cites ids inline
# ----     in PROSE. tRunOk is the control and cites the SAME id that way, so the arm cannot be
# ----     satisfied by a check 13 that merely said something.
# ---- (d2) ROTATION AND CORPUS MEMBERSHIP (TOOL-aRelaxedShard-4, settling TOOL-aRelaxedShard-1 F4).
# ----      cSteadyMetronome recorded that rotating a backlog shard to `archive/` ORPHANS every id the
# ----      moved rows defined, and a rotation was reverted on that report. Rotation between two
# ----      TRACKED paths cannot do that: check 14 is `cites` minus `defs`, a backlog row defines AND
# ----      cites its own id on one line, and `corpus_ids.py` walks `git ls-files` with no `archive/`
# ----      exclusion. Measured on the live corpus, 83 ids are defined only under `archive/` and none
# ----      is an orphan. So an arm that rotates and asserts zero orphans is green by ARITHMETIC.
# ----
# ----      The axis that CAN fail is corpus MEMBERSHIP. `git ls-files` is the corpus, so an archive
# ----      that exists on disk but is not staged contributes no definitions while the live shard's
# ----      copy is already gone — and the citations survive, because the moved ids are cited from
# ----      outside the archive. Both states are built here from the SAME rotation, so the pair
# ----      isolates membership rather than the move.
A=$TMP/rotarchive
mkdir -p "$A/memory/builds/tRot/spec" "$A/memory/archive" "$A/memory/backlog" "$A/memory/project"
( cd "$A" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nORPHAN_ID_PIN="0"\nDEAD_PATH_PIN="0"\n' > .memory-tree.conf
  printf '# r\n' > memory/README.md
  printf '# legacy\n' > memory/project/legacy-files.txt
  printf -- '---\nslug: tRot\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-tRot-1\n---\n\n# tRot\n' > memory/builds/tRot/README.md
  printf '# ARCH-tRot-1 — the owning unit\n\nIt cites ARCH-tMoved-1 in prose, so the moved id is CITED from outside the archive.\n' > memory/builds/tRot/spec/2026-08-01-spec-tRot-1.md
  # The live shard AFTER the rotation: the moved row is gone from here in both states below.
  printf '# ARCH backlog\n\n> Rotated 2026-08-01 to [../archive/ARCH.2026-08-01.md](../archive/ARCH.2026-08-01.md).\n\n- ARCH-tRot-1 · OPEN · the owning unit\n' > memory/backlog/ARCH.md
  printf '# rotated\n\n- ARCH-tMoved-1 · CLOSED · the moved row, which DEFINES its own id on this line\n' > memory/archive/ARCH.2026-08-01.md
  git add -A && "$_PY" "$HERE/gen_build_index.py" --write >/dev/null 2>&1; git add -A
  git commit -q -m rotated --no-verify )
outa=$(cd "$A" && bash "$SCRIPT" 2>/dev/null)
n=$((n+1))
# NOT cblock: check 14 emits a one-line `HYGIENE check 14: id ... is cited but never defined`,
# and cblock keys on the `HYGIENE check <n> FAILED` block header, so it returns nothing here and
# BOTH arms would pass by finding nothing. Measured before trusting either direction.
grep -qF 'ARCH-tMoved-1' <<<"$outa" \
  && { echo "FAIL check 14 called a rotated-and-STAGED id an orphan — rotation between two tracked paths cannot orphan anything, so this is the arithmetic going wrong"; st=1; }
# ---- ...and now the SAME rotation with the archive unstaged. This is the state cSteadyMetronome saw.
n=$((n+1))
( cd "$A" && git rm -q --cached memory/archive/ARCH.2026-08-01.md >/dev/null 2>&1 \
    && git commit -q -m "archive present but untracked" --no-verify )
outb=$(cd "$A" && bash "$SCRIPT" 2>/dev/null)
grep -qF 'ARCH-tMoved-1' <<<"$outb" \
  || { echo "FAIL check 14 did NOT flag a rotated id whose archive is present-but-unstaged — the corpus is git ls-files, so that id has no definition and this is the one state where rotation really does orphan"; st=1; }

R=$TMP/runanchor
mkdir -p "$R/memory/builds/tOwner/spec" "$R/memory/builds/tRunBig" "$R/memory/builds/tRunOk" \
         "$R/memory/backlog" "$R/memory/project"
( cd "$R" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  # ORPHAN_ID_PIN is what ARMS the unit; 0 is legal because every id below is defined.
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nORPHAN_ID_PIN="0"\nDEAD_PATH_PIN="0"\n' > .memory-tree.conf
  printf '# r\n' > memory/README.md
  printf '# ARCH backlog\n' > memory/backlog/ARCH.md
  printf '# legacy\n' > memory/project/legacy-files.txt
  rr() { printf -- '---\nslug: %s\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-tOwner-1\n---\n\n# %s\n' "$1" "$1"; }
  n=$((n+1))
  rr tOwner > memory/builds/tOwner/README.md
  rr tRunBig > memory/builds/tRunBig/README.md
  rr tRunOk > memory/builds/tRunOk/README.md
  printf '# ARCH-tOwner-1 — the owning unit\n\nbody\n' > memory/builds/tOwner/spec/2026-08-01-spec-tOwner-1.md
  printf '# run\n\n- ARCH-tOwner-1 · parked: this dash row ANCHORS the id\n' > memory/builds/tRunBig/RUN.md
  printf '# run\n\nThe mandate names ARCH-tOwner-1 inline, in prose, so nothing anchors here.\n' > memory/builds/tRunOk/RUN.md
  git add -A && "$_PY" "$HERE/gen_build_index.py" --write >/dev/null 2>&1; git add -A
  git commit -q -m runanchor --no-verify )
outr=$(cd "$R" && bash "$SCRIPT" 2>/dev/null)
grep -qF 'check 13: id ARCH-tOwner-1 is claimed by 2 build folders' <<<"$outr" \
  || { echo "FAIL a RUN.md dash row did not make its build folder a second claimant of the id"; st=1; }
n=$((n+1))
grep -F 'check 13: id ARCH-tOwner-1' <<<"$outr" | grep -qF 'tRunBig' \
  || { echo "FAIL check 13 did not name the run-state file's build folder as a claimant"; st=1; }
n=$((n+1))
grep -F 'check 13: id ARCH-tOwner-1' <<<"$outr" | grep -qF 'tRunOk' \
  && { echo "FAIL check 13 named tRunOk, whose RUN.md cites the id INLINE IN PROSE — prose is not an anchor"; st=1; }

# ---- THE SCAFFOLDER, asserted against the GATE rather than against a second description of itself.
# ---- A hand-built imitation asserts what this file BELIEVES adopt-memory-tree.sh emits, and that
# ---- belief is the copy that drifts; the young-tree arm above is exactly that, and stays as the
# ---- control. Here the real script builds the fixture. Scaffolding a shape the gate rejects and
# ---- rejecting a shape the scaffolder writes are both red bars, and only running both catches either.
# ---- Three preconditions, because the scaffolder refuses three ways before it writes anything: a
# ---- git repo, a .memory-tree.conf (absent -> it copies the example and exits 1), and NO existing
# ---- memory/ (present -> exit 0 "already scaffolded" over an unwritten tree, which would be a green
# ---- rc proving nothing).
n=$((n+1))
A=$TMP/scaffolded
mkdir -p "$A"
( cd "$A" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\n' > .memory-tree.conf
  bash "$HERE/adopt-memory-tree.sh" --scaffold >/dev/null 2>&1
  git add -A && git commit -q -m scaffolded --no-verify ) || { echo "FAIL adopt-memory-tree.sh --scaffold did not complete"; st=1; }
# The retired session machinery: five names under project/ the gate no longer admits, so writing any
# of them would hand every new adopter a red tree on their first run. The prefix is interpolated
# rather than spelled into each entry, so this arm cannot itself be mistaken for a surviving fixture
# by a sweep looking for the old paths.
n=$((n+1))
for p in MEMORY.md IN-FLIGHT.md README.md in-flight journal; do
  [ -e "$A/memory/project/$p" ] && { echo "FAIL adopt-memory-tree.sh still scaffolds memory/project/$p, which check 3 now rejects"; st=1; }
done
# ...and all FIVE registries, not two. Three of them are NAMED by gates and were created by nothing;
# "absent" and "present and empty" read identically to every consumer, which is what hid it.
n=$((n+1))
for r in legacy-files.txt curation-debt.txt id-orphan-waiver.txt corpus-path-unresolved.txt unarmed-branches.txt; do
  [ -f "$A/memory/project/$r" ] || { echo "FAIL adopt-memory-tree.sh did not scaffold memory/project/$r"; st=1; }
done
n=$((n+1))
outa=$(cd "$A" && bash "$SCRIPT" 2>/dev/null); rca=$?
[ "$rca" = 0 ] || { echo "FAIL a tree built by adopt-memory-tree.sh --scaffold is not hygiene-clean (rc=$rca):"; printf '%s\n' "$outa" | sed 's/^/      /'; st=1; }

# ---- CHECK 21 — every record names the spec it is evidence about.
# ---- Five fail sites behind one check number, each armed on its OWN literal signature and each
# ---- asserted inside check 21's own output block via chit(), never against a global hit: this
# ---- check prints bare paths, and a global grep cannot tell which branch produced one.
# ---- The GREEN control matters as much as the reds. A cross-build record correctly named for the
# ---- SERVED id's slug must stay silent, or branch 5 would be a rule the corpus cannot satisfy.
K=$TMP/c21
mkdir -p "$K"
( cd "$K" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nRECORD_UNBOUND_PIN="1"\n' > .memory-tree.conf
  mkdir -p memory/backlog memory/project memory/builds/tOne/spec memory/builds/tOne/reviews \
           memory/builds/tOne/build memory/builds/tTwo/spec memory/builds/tTwo/reviews
  printf '# r\n' > memory/README.md
  printf '# ARCH backlog\n' > memory/backlog/ARCH.md
  for r in legacy-files.txt curation-debt.txt id-orphan-waiver.txt corpus-path-unresolved.txt unarmed-branches.txt method-carriers.txt; do : > "memory/project/$r"; done
  rk() { printf -- '---\nslug: %s\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-%s-1\n---\n\n# %s\n' "$1" "$1" "$1"; }
  rk tOne > memory/builds/tOne/README.md
  rk tTwo > memory/builds/tTwo/README.md
  printf '# ARCH-tOne-1 — unit one\n\nbody\n' > memory/builds/tOne/spec/2026-08-01-spec-tOne-1.md
  printf '# ARCH-tTwo-1 — unit two\n\nbody\n' > memory/builds/tTwo/spec/2026-08-01-spec-tTwo-1.md
  # branch 1 — no line at all
  printf '# r\n\nbody\n' > memory/builds/tOne/reviews/2026-08-01-review-ARCH-tOne-1-a.md
  # branch 2 — an id no spec defines
  printf '# r\n\n**Serves:** spec-audit ARCH-tGhost-9\n' > memory/builds/tOne/reviews/2026-08-01-review-ARCH-tOne-1-b.md
  # branch 5 — the filename claims a real id the header does not list
  printf '# r\n\n**Serves:** spec-audit ARCH-tOne-1\n' > memory/builds/tOne/reviews/2026-08-01-review-ARCH-tTwo-1-c.md
  # branch 4 — two unbound records against a pin of 1
  printf '# r\n\n**Serves:** none — nothing to serve\n' > memory/builds/tOne/build/2026-08-01-build-ARCH-tOne-1-d.md
  printf '# r\n\n**Serves:** none — nothing to serve either\n' > memory/builds/tOne/build/2026-08-01-build-ARCH-tOne-1-e.md
  # the GREEN control — a CROSS-BUILD record, housed under tTwo, named for the id it SERVES
  printf '# r\n\n**Serves:** diff-review ARCH-tOne-1\n' > memory/builds/tTwo/reviews/2026-08-01-review-ARCH-tOne-1-f.md
  git add -A && "$_PY" "$HERE/gen_build_index.py" --write >/dev/null 2>&1; git add -A
  git commit -q -m c21 --no-verify )
out=$(cd "$K" && bash "$SCRIPT" 2>/dev/null)
chit 21 'records under build/, prompts/ or reviews/ whose head carries no conformant Serves line'
chit 21 'Serves or Commissions lines naming an id that no spec in this tree defines'
chit 21 'records carrying the unbound Serves form outnumber their pin — bind them, or move the pin in the same commit recording the old and new values beside it'
chit 21 'record filenames whose family, slug and ordinal name an id their own Serves line does not list'
cblock "$out" 21 | grep -qF '2026-08-01-review-ARCH-tOne-1-f.md' \
  && { echo "FAIL check 21 flagged a CROSS-BUILD record correctly named for the id it serves"; st=1; }
# branch 3 — the pin UNDECLARED is a refusal, not a disabled check.
( cd "$K" && printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\n' > .memory-tree.conf )
out=$(cd "$K" && bash "$SCRIPT" 2>/dev/null)
chit 21 'RECORD_UNBOUND_PIN is undeclared, so the count of records that serve no spec is unbounded — declare it in .memory-tree.conf, measured against this corpus'

# ---- CHECK 6 — the per-class caps are DECLARATIONS (TOOL-aLoosenedCeiling-2).
# ---- Every arm runs BOTH DIRECTIONS OVER ONE FIXTURE: the same file is silent at a loose cap and
# ---- named at a tight one. A one-directional arm over a tunable threshold proves nothing, because a
# ---- fixture under every cap passes whatever the cap says.
# ---- c6run() exists because the first cut of this block was itself the defect it guards against.
# ---- Its conf helper interpolated with %s, so a `\n` reached the file as two literal characters,
# ---- every declared-cap run aborted at status 2 with NO output, and each `cnot` read that silence
# ---- as "under the cap". Four arms passed by finding nothing. So the status is now asserted on
# ---- every run: a gate that refused to start is not a gate that found nothing.
C6=$TMP/caps
mkdir -p "$C6"
c6run() {  # $1 = extra conf lines (%b, so \n works); leaves $out set and asserts the gate RAN
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\n' > "$C6/.memory-tree.conf"
  [ -n "$1" ] && printf '%b' "$1" >> "$C6/.memory-tree.conf"
  out=$(cd "$C6" && bash "$SCRIPT" 2>/dev/null); c6rc=$?
  n=$((n+1))
  [ "$c6rc" != 2 ] || { echo "FAIL check-6 caps '$1' aborted the gate (status 2); a silent run below would prove nothing"; st=1; }
}
( cd "$C6" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  mkdir -p memory/backlog memory/project memory/guides memory/builds/tBig memory/builds/tLong memory/builds/tWide
  printf '# r\n' > memory/README.md
  for r in legacy-files.txt curation-debt.txt id-orphan-waiver.txt corpus-path-unresolved.txt unarmed-branches.txt method-carriers.txt; do : > "memory/project/$r"; done
  # ONE seq, reused. Building each line with its own command substitution cost this suite minutes.
  # 250 chars keeps every row under check 7's 300-char budget, so only check 6 speaks.
  R=$(printf 'y%.0s' $(seq 1 246))
  rows() { i=1; while [ "$i" -le "$1" ]; do printf -- '- %s\n' "$R"; i=$((i+1)); done; }
  fm() { printf -- '---\nslug: %s\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-%s-1\n---\n\n# %s\n\n' "$1" "$1" "$1"; }
  # (a) a GUIDE between the row-document cap and the guide cap: silent by default, named when the
  #     guide cap is declared below its size. ~30 KB over ~120 lines, so no line cap can be what fires.
  { printf '# tmid guide\n\n'; rows 120; } > memory/guides/tmid.md
  # (b) a ROW DOCUMENT over the shipped index cap: named by default, silent when the index cap is
  #     declared above its size. ~25 KB, ~100 lines — the BYTE cap is what fires, not the line cap.
  { printf '# ARCH backlog\n\n'; rows 100; } > memory/backlog/ARCH.md
  # (c) a BUILD README over the shipped build-README byte cap with NOTHING declared. This is the arm
  #     for the DEFAULT tier, which no arm in this suite reached before.
  { fm tBig; rows 120; } > memory/builds/tBig/README.md
  # (d) a BUILD README with more lines than the row-document tier allows and well under its OWN byte
  #     cap. Its silence is the proof that a zero LINE cap means NO line cap rather than a cap of zero.
  { fm tLong; i=1; while [ "$i" -le 400 ]; do printf -- '- row %d\n' "$i"; i=$((i+1)); done; } > memory/builds/tLong/README.md
  # (e) and (f) — check 7's ENTRY budget, one fixture per class at a width BETWEEN the two shipped
  #     tiers. 320 characters is over the row-document 300 and under the build-README 350, so with
  #     nothing declared the row is named and the README is silent: one width, both defaults, and
  #     neither arm can pass while the other is broken.
  W=$(printf 'w%.0s' $(seq 1 316))
  { printf '# BRAND backlog\n\n'; printf -- '- %s\n' "$W"; } > memory/backlog/BRAND.md
  { fm tWide; printf -- '- %s\n' "$W"; } > memory/builds/tWide/README.md
  # (e) an INDEX-CLASS row document over the shipped LINE cap and far under its byte cap: ~800 short
  #     rows, about 7 KB. Named by default because the line axis fires, SILENT once INDEX_CAP_LINES is
  #     declared 0 — which is the only pair in this suite that proves a project can RETIRE the line axis
  #     for the index class. TOOL-aRelaxedShard-1 declares exactly that, and (d) cannot show it: tLong is
  #     a build README, whose own class already ships a zero line cap, so it is silent either way.
  { printf '# ARCH status\n'; i=1; while [ "$i" -le 800 ]; do printf -- '- r%d\n' "$i"; i=$((i+1)); done; } > memory/builds/tLong/STATUS.md
  git add -A && git commit -q -m caps --no-verify )

# --- DEFAULTS, nothing declared: (b), (c) and (e) are named, (a) and (d) are silent.
c6run ''
chit 6 'memory/builds/tLong/STATUS.md'
chit 6 'memory/backlog/ARCH.md'
chit 6 'memory/builds/tBig/README.md'
cnot 6 'memory/guides/tmid.md'
cnot 6 'memory/builds/tLong/README.md'
n=$((n+1))
cblock "$out" 6 | grep -qE 'memory/backlog/ARCH\.md \([0-9]+B [0-9]+L > 20480B/250L\)' \
  || { echo "FAIL check 6 named the row document but not against the SHIPPED 20480B/250L default"; st=1; }
n=$((n+1))
cblock "$out" 6 | grep -qE 'memory/builds/tBig/README\.md \([0-9]+B > 25600B; no line cap for this class\)' \
  || { echo "FAIL check 6 named the build README but not against the SHIPPED 25600B default, or printed a line cap for a class that has none"; st=1; }
# --- CHECK 7's entry budget at the SHIPPED defaults. One 320-char fixture line in each class: the
# --- row document is over 300 and named, the build README is under 350 and silent. A single arm
# --- would pass under one merged tier; the pair is what observes the split.
chit 7 'memory/backlog/BRAND.md'
cnot 7 'memory/builds/tWide/README.md'

# --- the GUIDE cap declared BELOW the fixture: the file that was silent is now named, AGAINST THE
# --- DECLARED number — which is what proves the binding reached awk rather than the default surviving.
c6run 'GUIDE_CAP_BYTES=25000\nGUIDE_CAP_LINES=700\n'
chit 6 'memory/guides/tmid.md'
n=$((n+1))
cblock "$out" 6 | grep -qE 'memory/guides/tmid\.md \([0-9]+B [0-9]+L > 25000B/700L\)' \
  || { echo "FAIL check 6 named the guide but not against the DECLARED cap 25000B/700L"; st=1; }

# --- the INDEX cap declared ABOVE the fixture: the row document that was named goes silent, and a
# --- key that is not the build README's leaves that class exactly where it was.
c6run 'INDEX_CAP_BYTES=40000\n'
cnot 6 'memory/backlog/ARCH.md'
chit 6 'memory/builds/tBig/README.md'

# --- the BUILD-README cap declared above its fixture: named becomes silent, and the row document is
# --- untouched by a key that is not its own.
c6run 'BUILD_README_CAP_BYTES=60000\n'
cnot 6 'memory/builds/tBig/README.md'
chit 6 'memory/backlog/ARCH.md'

# --- CHECK 7 with the row budget declared ABOVE the fixture: the named line goes silent, and the
# --- build README stays silent because a key that is not its own does not reach it.
c6run 'ENTRY_CAP_CHARS=400\n'
cnot 7 'memory/backlog/BRAND.md'
cnot 7 'memory/builds/tWide/README.md'

# --- and with the BUILD-README budget declared BELOW its fixture: the silent one is named, while the
# --- row document returns to being named by its own untouched default.
c6run 'BUILD_README_ENTRY_CAP_CHARS=310\n'
chit 7 'memory/builds/tWide/README.md'
chit 7 'memory/backlog/BRAND.md'

# --- a zero LINE cap is LEGAL, and is not the same declaration as a zero byte cap. Without this the
# --- refusal below could have been written as "any zero is malformed", which would have made the
# --- build-README class undeclarable in the very conf this unit added.
c6run 'INDEX_CAP_LINES=0\n'
cnot 6 'memory/builds/tLong/README.md'
# --- ...and the arm that actually isolates the INDEX class: (e) is over the shipped line cap and
# --- under its byte cap, so only a retired line axis can silence it.
cnot 6 'memory/builds/tLong/STATUS.md'

# --- MALFORMED and ZERO-BYTE caps ABORT rather than fail a check. Own capture, because the shared
# --- idiom discards stderr and the status, and the whole point is that a gate which cannot read its
# --- thresholds must not report a clean tree. Asserted on stdout AND the status: either alone passes
# --- under the wrong choice of channel.
# '00' is here because the first cut of the guard matched the LITERAL 0 with a case pattern, so a
# leading zero walked past it and awk's +0 belt then coerced it to zero — every file in the class
# red, with no line pointing at the conf. The guard now compares ARITHMETICALLY; this arm is why.
for _bad in 'GUIDE_CAP_BYTES=abc' 'INDEX_CAP_LINES=' 'INDEX_CAP_BYTES=0' 'INDEX_CAP_BYTES=00' 'GUIDE_CAP_LINES=-5' 'ENTRY_CAP_CHARS=0' 'BUILD_README_ENTRY_CAP_CHARS=xyz'; do
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\n%s\n' "$_bad" > "$C6/.memory-tree.conf"
  outc=$(cd "$C6" && bash "$SCRIPT" 2>/dev/null); rcc=$?
  n=$((n+1))
  [ "$rcc" = 2 ] || { echo "FAIL a malformed check-6 cap ($_bad) exited $rcc, not the cannot-run status 2"; st=1; }
  n=$((n+1))
  printf '%s\n' "$outc" | grep -qF 'HYGIENE — cannot run: size cap(s) declared in .memory-tree.conf are unusable:' \
    || { echo "FAIL a malformed check-6 cap ($_bad) printed no cannot-run line on stdout"; st=1; }
  n=$((n+1))
  printf '%s\n' "$outc" | grep -qF "${_bad%%=*}" \
    || { echo "FAIL the cannot-run line did not name the offending key ${_bad%%=*}"; st=1; }
  n=$((n+1))
  printf '%s\n' "$outc" | grep -qF 'HYGIENE check' \
    && { echo "FAIL a malformed check-6 cap ($_bad) reported check findings instead of refusing to run"; st=1; }
done

# ---- the SHIPPED conf example declares every key this engine reads as an override. Nothing else
# ---- observes that file: no gate parses it, its only consumer is the adopt script that copies it,
# ---- and the rendered hygiene doc TELLS an adopter the keys are declared there. So a build can ship
# ---- the engine, the docs and the tests green with the example half-done — which is exactly what
# ---- happened here, and what the closing review caught.
EX="$HERE/.memory-tree.conf.example"
# ---- DERIVED from the engine's own validation loop, never retyped. The hand-kept version of this
# ---- list covered seven of the engine's keys and missed DOSSIER_CAP_* entirely, so adding two more
# ---- by hand would have been the same omission a third time. READ_PATH_HEADROOM is appended because
# ---- it is corpus_ids.py's key rather than this engine's, so no loop here can yield it.
_engkeys=$(sed -n 's/^for _k in \(.*\); do$/\1/p' "$HERE/check-memory-hygiene.sh" | head -1)
n=$((n+1))
[ -n "$_engkeys" ] || { echo "FAIL could not derive the cap-key list from the engine; the example-conf arms below would pass by finding nothing"; st=1; }
for _k in $_engkeys READ_PATH_HEADROOM; do
  n=$((n+1))
  grep -qE "^$_k=" "$EX" || { echo "FAIL the shipped .memory-tree.conf.example does not declare $_k, so an adopter cannot discover it"; st=1; }
done

# ---- ...and the DATE CUTOFFS, which the loop above structurally cannot reach: they are read as
# ---- `${NAME:-}` and never validated by the cap loop, so a cutoff key added to the engine and
# ---- forgotten in the example was invisible to a parity arm derived from that loop alone. That is
# ---- what happened to both ACCEPTANCE_LEDGER keys, and the arm above passed the whole time.
# ----
# ---- THE HONEST POPULATION is every `${NAME:-}` the engine reads, MINUS the names it assigns itself
# ---- (those are internals, not overrides), MINUS a DECLARED exclusion carrying its reason. The
# ---- exclusion is asserted in BOTH directions: a name it lists that the engine no longer reads reds
# ---- too, because a stale exemption silently widens the surface it was written to narrow.
# COMMENT-STRIPPED, and with NO subtraction of the names the engine assigns itself. The first cut
# subtracted them on the rationale that a self-assigned name is an internal rather than an override,
# and `comm -12` over its own two derivations returned exactly one name — SPEC10_CUTOFF — which is a
# live adopter key with a shipped default that the conf overrides on top of. It was silently outside
# the parity requirement, which is precisely the failure this arm exists to prevent, one level up.
# The comment strip matters for the same reason: the raw pattern matched prose, so a key could reach
# the population by being MENTIONED rather than read.
_engreads=$(sed 's/[[:space:]]#.*$//; s/^[[:space:]]*#.*$//' "$HERE/check-memory-hygiene.sh" \
  | grep -oE '\$\{[A-Z][A-Z0-9_]+:[-=]' | sed 's/^\${//; s/:[-=]$//' | sort -u)
# NOT conf keys, and each says why. GOV_PYTHON is an environment override for the python launcher and
# belongs to no conf; MAP_ROOT is the codebase-map kit's key, read from ITS conf by a check that
# integrates with it. Declaring either here would tell adopters to set a key this kit does not own.
_engexempt="GOV_PYTHON MAP_ROOT"
n=$((n+1))
[ -n "$_engreads" ] || { echo "FAIL could not derive the engine's conf reads; the cutoff-parity arm below would pass by finding nothing"; st=1; }
for _k in $_engexempt; do
  n=$((n+1))
  printf '%s\n' "$_engreads" | grep -qx "$_k" \
    || { echo "FAIL the example-conf exemption names $_k, which the engine no longer reads as an override — a stale exemption widens the surface it was written to narrow"; st=1; }
done
for _k in $_engreads; do
  case " $_engexempt " in *" $_k "*) continue ;; esac
  n=$((n+1))
  grep -qE "^$_k=" "$EX" \
    || { echo "FAIL the shipped .memory-tree.conf.example does not declare $_k, which the engine reads as an override, so an adopter cannot discover it"; st=1; }
done

# ---- SPEC10_CUTOFF is a CONF DECLARATION, and the environment no longer reaches it
# ---- (TOOL-aDeclaredBound-2). Four runs over ONE nine-section spec dated 2026-08-01, which is
# ---- BEFORE the shipped 2026-08-04: absent, declared-early, declared-blank, and hostile-env.
# ---- The declared-early run is the only one that may speak, and it is what proves the other three
# ---- are silent because the value said so rather than because check 12 was asleep.
S10=$TMP/spec10
mkdir -p "$S10"
s10conf() {
  printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\n' > "$S10/.memory-tree.conf"
  [ -n "$1" ] && printf '%b' "$1" >> "$S10/.memory-tree.conf"
  return 0
}
( cd "$S10" && git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
  mkdir -p memory/builds/tTen/spec memory/backlog memory/project
  printf '# r\n' > memory/README.md
  for r in legacy-files.txt curation-debt.txt id-orphan-waiver.txt corpus-path-unresolved.txt unarmed-branches.txt method-carriers.txt; do : > "memory/project/$r"; done
  printf -- '---\nslug: tTen\nnode: a\nopened: 2026-08-01\nstreams: architecture\nroster: ARCH\nids: ARCH-tTen-1\n---\n\n# tTen\n' > memory/builds/tTen/README.md
  { printf '# ARCH-tTen-1 — fixture\n\n**Status:** SPECCED · rev-1 · 2026-08-01 · node a · Tier-2 · base 0123abcd\n\n'
    for h in '1. Goal' '2. Scope (IN)' '3. Non-goals (OUT)' '4. Design' '5. Production-readiness checklist' \
             '6. Acceptance criteria' '7. Gates' '8. Open questions'; do
      printf '## %s\n\nbody.\n\n' "$h"
    done
    # §9 carries the header's rev or check 12 reds for a reason that has nothing to do with the
    # section canon — which is how the first cut of these arms measured the wrong thing three times.
    printf '## 9. Revision log

- rev-1 · 2026-08-01 · initial draft.
'; } > memory/builds/tTen/spec/2026-08-01-spec-tTen-1.md
  git add -A && git commit -q -m ten --no-verify )

# --- ABSENT: the shipped date applies, the spec predates it, the nine-section canon is enough.
s10conf ''
out=$(cd "$S10" && bash "$SCRIPT" 2>/dev/null)
cnot 12 'memory/builds/tTen/spec/2026-08-01-spec-tTen-1.md'

# --- DECLARED EARLIER than the spec: the ten-section canon is demanded and check 12 says so. This
# --- arm is the one that can speak, so it is what makes the three silences mean something.
s10conf 'SPEC10_CUTOFF="2026-07-01"\n'
out=$(cd "$S10" && bash "$SCRIPT" 2>/dev/null)
chit 12 'memory/builds/tTen/spec/2026-08-01-spec-tTen-1.md'

# --- DECLARED BLANK: resolves FORWARD to the shipped date, never to "off" and never to an empty
# --- string that compares earlier than every date. Identical verdict to absent.
s10conf 'SPEC10_CUTOFF=""\n'
out=$(cd "$S10" && bash "$SCRIPT" 2>/dev/null)
cnot 12 'memory/builds/tTen/spec/2026-08-01-spec-tTen-1.md'

# --- HOSTILE ENV with nothing declared: the retired channel has no effect. Before this unit the
# --- engine read `${SPEC10_CUTOFF:-<date>}` AFTER sourcing the conf, so this exact value would have
# --- demanded the ten-section canon here and reds 13 grandfathered specs in the real corpus.
s10conf ''
out=$(cd "$S10" && SPEC10_CUTOFF=1999-01-01 bash "$SCRIPT" 2>/dev/null)
cnot 12 'memory/builds/tTen/spec/2026-08-01-spec-tTen-1.md'

# ---- the verdict, printed AFTER the last arm. Upstream printed PASS ~150 lines early and landed a
# ---- red merge bar because the head of the output said success.
# FLOOR_ASSERTIONS — TOOL-cBriefedPilot-23, and it closes TOOL-cTracedPromise-4 rather than
# colliding with it. Both branches independently found that the number here was AUTHORED and had sat
# at 130 while arms were added under it more than once. main's fix was to DELETE it, on the reasoning
# that a tally which cannot be derived is the two-answers-to-one-question defect wearing a reassuring
# number — correct about the authored form, and exactly why this one is DERIVED instead: `n`
# increments in the assertion helpers, so nobody maintains it.
# TOOL-cSettledDocket-4 made the count WHOLE: the 52 inline sites (`<test> || { echo FAIL...; st=1; }`)
# now increment too, at each statement's start rather than inside its failure brace — inside, it
# would count failures and a green run would report near zero. main's static call-site count of 115
# "reconciled with nothing" for exactly this reason. Derivation, so a reader can re-check rather than
# trust: 88 helper-only -> 137 whole, and the sweep inserted 52. The gap is NOT arithmetic error
# and NOT — as this comment first claimed — sites on paths the run does not take. Measured: some
# increments sit inside SUBSHELLS, where `n=$((n+1))` mutates a copy that dies with the subshell.
# Those assertions DO run; only their count is discarded. The floor is therefore slightly lower
# than the true executed total, which is safe (it under-claims) but is not what it looks like.
# Written down twice now, because the first explanation was a guess dressed as a measurement.
# 137 -> 136 is a DELIBERATE lowering, and the only kind that is legitimate: the sweep had inserted
# one increment between two function DEFINITIONS, counting an assertion that does not exist. The
# floor went down because the count got HONEST, not because coverage shrank.
# Floored shrink-only, because an arm stranded past an `exit` stays in the file and only a runtime
# total can see it go dark.
n=$((n+1))
# ---- The hand-kept five-key version of this arm lived here and was DELETED, not left beside the
# ---- derived loop above it. A strict subset asserting the identical property over the identical
# ---- file can only under-cover, and it is the copy that silently falls behind the next engine
# ---- key -- the exact hand-kept-list drift the derived loop was written to remove. A reader
# ---- grepping for the assertion would have landed on whichever copy came first and concluded
# ---- coverage was five keys. The derived loop is now the ONLY site naming .memory-tree.conf.example.

# ---- THE README'S CHECK COUNT IS DERIVED, NEVER TRUSTED. AGENTS.md designates the kit README as THE
# ---- carrier of this number and the gate-leg names carry none, so it is the one figure a reader is
# ---- told to trust - and it has now been retyped wrong three times, most recently sitting at 21
# ---- through a whole build that added check 22. Nothing gated it, because a number in prose beside
# ---- the thing it counts is exactly the shape no check ever looks at.
#
# ---- The population is every site that can EMIT a check id: `fail <n>` in the shell, `check <n>:`
# ---- in the two delegated pythons, and row_grammar's `CHECK = <n>` module constant, which is the
# ---- one spelling the other two greps miss and the reason check 20 was invisible.
n=$((n+1))
_hy_ids=$( { grep -oE 'fail [0-9]+' "$HERE/check-memory-hygiene.sh" | grep -oE '[0-9]+'
             grep -rhoE 'check [0-9]+:' "$HERE/corpus_ids.py" "$HERE/gotchas.py" | grep -oE '[0-9]+'
             grep -oE '^CHECK = [0-9]+' "$HERE/row_grammar.py" | grep -oE '[0-9]+'; } | sort -n -u )
_hy_derived=$(printf '%s
' "$_hy_ids" | grep -c .)
# ANCHORED ON THE ROW, NOT ON THE DASH. The first spelling was `the gate . [0-9]+ checks`, and the
# separator is an EM DASH - three bytes in UTF-8, which a single `.` matches one byte of under this
# repo's own ambient locale. The read came back EMPTY and the arm refused, which is the behaviour it
# was written to have; it is still the wrong predicate. Same byte-offset trap check 12 carries a
# warning about, one file over.
_hy_claimed=$(grep -F 'check-memory-hygiene.sh' "$HERE/README.md" | grep -oE '[0-9]+ checks' | grep -oE '^[0-9]+' | head -1)
[ -n "$_hy_claimed" ] || { echo "FAIL the kit README states no check count in the shape this arm reads, so the figure AGENTS.md designates as canonical is now ungraded - fix the arm or the README, but do not leave the number unwatched"; st=1; }
n=$((n+1))
[ "$_hy_claimed" = "$_hy_derived" ] || { echo "FAIL the kit README claims $_hy_claimed checks and the engine defines $_hy_derived ($(echo $_hy_ids | tr '
' ' ')) - the one figure a reader is told to trust is wrong"; st=1; }

FLOOR_ASSERTIONS=224
[ "$n" -ge "$FLOOR_ASSERTIONS" ] || { echo "FAIL executed $n assertions against a floor of $FLOOR_ASSERTIONS — arms are UNREACHABLE rather than absent; look for a block stranded past an exit or a return"; st=1; }
[ "$st" = 0 ] && echo "PASS ($n assertions)"
exit "$st"
