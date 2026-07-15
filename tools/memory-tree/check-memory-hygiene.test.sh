#!/usr/bin/env bash
# Fixture self-test for check-memory-hygiene.sh CHECK 12 (spec-format ratchet).
# Builds a scratch git repo with conforming + violating spec fixtures and asserts each check-12
# class fires (red) or stays silent (green), plus the disabled-when-blank conf contract. Only
# check-12 lines are asserted — the scratch repo intentionally reds other checks and that noise
# is ignored.
#   bash memory-tree/check-memory-hygiene.test.sh    # "PASS (14 assertions)" + exit 0 = good
set -u
HERE="$(cd "$(dirname "$0")" && pwd)"
SCRIPT="$HERE/check-memory-hygiene.sh"
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
cd "$TMP" || exit 2
git init -q . && git config user.email t@t.test && git config user.name t && git config core.autocrlf false
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\nSPEC_FORMAT_CUTOFF="2026-07-15"\n' > .memory-tree.conf

D=memory/architecture/builds/2026-08-01-ARCH-tFixture
mkdir -p "$D/spec/subspecs"
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

- AC1 When run, it passes.

## 7. Gates

- memory hygiene.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-08-01 · initial draft.
EOF
}

good > "$D/spec/2026-08-01-spec-tFixture-1.md"                                   # conforming -> silent
good | sed 's/$/\r/' > "$D/spec/2026-08-01-spec-tFixture-2.md"                   # CRLF twin -> silent
printf '# nested\nno header here\n## Wrong\nbody\n' > "$D/spec/subspecs/2026-08-01-spec-tFixture-3.md"  # nested+headerless -> red
good | sed 's/^## 4\. Design$/## 4. Blueprint/' > "$D/spec/2026-08-01-spec-tFixture-4.md"               # wrong canon -> red
printf '# t1\n\n**Status:** OPEN · rev-1 · 2026-08-01 · node a · Tier-1 · base 0123abcd\n\n## Whatever\n\nfree-form body\n' \
  > "$D/spec/2026-08-01-spec-tFixture-5.md"                                      # Tier-1 light profile -> silent
good | sed 's/^A goal\.$/Ship on YYYY-MM-DD./' > "$D/spec/2026-08-01-spec-tFixture-6.md"                # placeholder -> red
good | sed '/^The design\.$/d' > "$D/spec/2026-08-01-spec-tFixture-7.md"          # empty section body -> red
good | sed 's/rev-1 · 2026-08-01 · node/rev-2 · 2026-08-01 · node/' > "$D/spec/2026-08-01-spec-tFixture-8.md"  # header rev not in §9 -> red
good | sed 's/^\*\*Status:\*\* SPECCED/**Status:** WONTDO/' > "$D/spec/2026-08-01-spec-tFixture-9.md"   # bare WONTDO tail -> red
good | sed 's/^\*\*Status:\*\* SPECCED/**Status:** CLOSED/; s/^none$/- still deciding something/' \
  > "$D/spec/2026-08-01-spec-tFixture-10.md"                                     # terminal + open §8 -> red
printf '# old era\nfreeform, no header\n## Anything\n' > "$D/spec/2026-07-10-spec-tFixture-11.md"       # pre-cutoff -> silent
{ good; printf '\n```text\n~~~\n## bogus heading inside fence\n```\n'; } > "$D/spec/2026-08-01-spec-tFixture-12.md"  # fence torture -> silent

git add -A && git commit -q -m fixtures --no-verify

out=$(bash "$SCRIPT" 2>/dev/null)
st=0
hit()  { grep -qF "$1" <<<"$out" || { echo "FAIL missing: $1"; st=1; }; }
miss() { if grep -qF "$1" <<<"$out"; then echo "FAIL unexpected: $1"; st=1; fi; }

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

# disabled-when-blank contract: same tree, cutoff removed -> check 12 fully silent.
printf 'MEMORY_ROOT=memory\nDISCIPLINES="architecture"\nFAMILIES="architecture:ARCH"\n' > .memory-tree.conf
out2=$(bash "$SCRIPT" 2>/dev/null)
if grep -qF 'HYGIENE check 12' <<<"$out2"; then echo "FAIL: check 12 ran with blank SPEC_FORMAT_CUTOFF"; st=1; fi
if ! grep -qF 'HYGIENE check 12' <<<"$out"; then echo "FAIL: check 12 never fired with cutoff armed"; st=1; fi

[ "$st" = 0 ] && echo "PASS (14 assertions)"
exit "$st"
