# TOOL-aWrittenMethod-6 — escaping conf values before substitution

**Status:** SPECCED · rev-1 · 2026-08-11 · node a · Tier-2 · base 7f614a17 · streams tooling

## 1. Goal

`adopt-unattended.sh` interpolates repo-authored conf values unescaped into `sed s|…|…|`. A `|` in
`LANDER` or `KEEPALIVE_INTERVAL` makes sed fail; an `&` silently re-inserts the whole match. Unit 1
made the failure loud but left the values unescaped, because two escape attempts were wrong. Escape
them, and arm the fix with a hostile-value fixture so a third wrong attempt cannot pass.

## 2. Scope (IN)

- **S1** — replace the `sed`-based substitution in `render()` with one that has **no
  replacement-side metacharacters**: bash parameter expansion over the template read into a variable.
  `${v//pat/rep}` treats `&` and `|` as ordinary text, which removes the defect class rather than
  escaping around it.
- **S2** — a hostile-value fixture in `tools/unattended/adopt-unattended.test.sh`: a conf whose
  `LANDER` and `KEEPALIVE_INTERVAL` each carry `|`, `&` and a backslash, asserting the rendered Skill
  contains those values **byte-for-byte**. A round-trip assertion, not a non-empty one.
- **S3** — a NEGATIVE control in the same fixture: assert the rendered Skill does NOT contain the
  literal `{{LANDER}}` or `{{KEEPALIVE_INTERVAL}}`, so a render that silently drops a substitution
  cannot pass by leaving the token in place.
- **S4** — the same treatment for `tools/memory-tree/kit-dogfood-parity.test.sh`'s `render()` and
  `tools/memory-tree/adopt-memory-tree.sh`'s `render_doc()`, whose substituted values (`KIT_DIR`,
  `TOOL_ROOT`) are install paths. A path with a `&` is unlikely and a path with a backslash is a
  Windows spelling away; the two renderers are byte-identical in intent and must not diverge on this.
- **S5** — keep unit 1's emptiness refusals at both paths. They are the backstop for whatever the
  next defect in this area turns out to be, and they are cheap.

## 3. Non-goals (OUT)

No change to which keys are interpolated, to the conf schema, or to the required-key loop.

No general-purpose escaping library. The fix removes the metacharacters from the mechanism; it does
not add a layer that must itself be correct.

No `sed` retained "for portability". The kit already requires bash — it is a `bash` script with
`bash`-only syntax throughout — so parameter expansion is not a new dependency.

## 4. Design

### Why the previous attempts failed, recorded so the third does not

Two escape functions were written during unit 1 and both were wrong, in different ways:

1. `sed -e "s/[\\\\&|]/\\\\&/g"` inside double quotes emitted a bare `&` as the replacement, which
   sed then expanded to the whole match — so `|` became the literal text `{{KEY}}`. Values were
   corrupted worse than by no escaping at all.
2. The single-quoted spelling, and a pure-parameter-expansion attempt, both silently did nothing when
   typed through the tooling layer between the author and the shell.

Both failures share a cause: **the number of backslash-consuming layers between the source and the
regex engine was not known**, which is this repo's own `heredoc-escape-reaches-the-regex` class. The
lesson S1 encodes is to stop counting layers and remove the engine that needs them.

### Data model

`render()` becomes: read `$TEMPLATE` into a variable with `$(cat …)`, apply one `${v//\{\{KEY\}\}/$VAL}`
per key, print with `printf '%s\\n'`, strip CR. No subprocess sees the values, so no quoting layer can
eat them.

The trailing `tr -d '\\r'` and the emptiness refusal stay, and `set -o pipefail` becomes unnecessary
for this path but is kept for the others.

### Files touched (estimate)

Five. `tools/unattended/adopt-unattended.sh`, `tools/unattended/adopt-unattended.test.sh`,
`tools/memory-tree/kit-dogfood-parity.test.sh`, `tools/memory-tree/adopt-memory-tree.sh`, and
`tools/memory-tree/BUILD-METHOD.template.md` only if M5's stale-hit rule needs the new class named.

### Alternatives rejected

A correctly-escaped `sed`: rejected on evidence. Two attempts failed and the failure mode is silent
value corruption, which is worse than the bug being fixed.

`awk` with a literal replacement: correct, but it moves the value through another subprocess and
another quoting layer, which is the thing being removed.

Python: the adopters are pure bash by design, and adding an interpreter to an adopter that currently
needs none is a dependency an adopting repo did not ask for.

## 5. Production-readiness checklist

- security — an adopter-supplied string reaching a shell-adjacent substitution. Removing the engine
  that interprets it is the fix; the values are repo-authored, not remote, so this is robustness
  rather than an injection boundary.
- perf / scale — a 4 KB template in a shell variable. Irrelevant.
- a11y · i18n — N/A.
- error / empty / loading states — S5 keeps both emptiness refusals.
- observability — a dropped substitution now fails S3's negative control rather than shipping a token.
- risks — bash parameter expansion has its own escaping rules for the PATTERN side; the pattern is a
  fixed literal `{{KEY}}` written by us, not adopter input, so the risk is bounded to code review.
- testing + left-shift gates — S2 and S3, riding the existing adopter e2e leg. No new leg.
- migration / rollback — none; the render's output is byte-identical for values with no metacharacters,
  which AC4 asserts.
- user docs — none. The behaviour change is invisible to a correct conf.

## 6. Acceptance criteria

- **AC1** — When `.unattended.conf` sets `KEEPALIVE_INTERVAL='every 10 min | offset 3 & more'` and
  `bash tools/unattended/adopt-unattended.sh` runs, it exits 0 and the rendered Skill contains that
  string byte-for-byte.
- **AC2** — When the same conf sets `LANDER='bash tools/land.sh | tee log'`, the rendered Skill
  contains it byte-for-byte and `--check` exits 0.
- **AC3** — When a value contains a backslash, it survives byte-for-byte.
- **AC4** — When every conf value is metacharacter-free, the rendered Skill is byte-identical to the
  one the current `sed` implementation produces. Verified by rendering before and after and diffing.
- **AC5** — When the rendered Skill is greped for `{{LANDER}}` and `{{KEEPALIVE_INTERVAL}}`, neither
  appears — the negative control against a silently dropped substitution.
- **AC6** — When `bash tools/unattended/adopt-unattended.test.sh` runs, it passes with a grown
  assertion count including the hostile-value arm.
- **AC7** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` runs after S4, it reports
  three pairs and exits 0, and `memory/HYGIENE.md`, `memory/TEMPLATE-SPEC.md` and
  `memory/guides/BUILD-METHOD.md` are byte-unchanged.

## 7. Gates

`tools/unattended/adopt-unattended.test.sh` · `tools/unattended/adopt-unattended.sh --check` ·
`tools/unattended/check-unattended.sh` · `tools/memory-tree/kit-dogfood-parity.test.sh` ·
`tools/memory-tree/check-memory-hygiene.sh` · `python tools/memory-tree/check-arms.py` ·
`bash tools/run-gates.sh` at the push boundary. No new leg.

## 8. Open questions

### F1 — how far to carry S4

The memory-tree renderers substitute install paths, not free prose, so their exposure is smaller.
Options: convert both for symmetry; convert neither and note the asymmetry; convert only
`adopt-memory-tree.sh`, which writes into an adopter's tree. **Recommendation: convert both.** The
two renderers are documented as byte-identical in intent — `kit-dogfood-parity.test.sh` says so in
its own comment — and letting them diverge on escaping is how the next reader learns the wrong lesson
from whichever one they open first.

### F2 — whether the hostile fixture belongs in the shipped kit or only the dogfood

`adopt-unattended.test.sh` ships to adopters. A fixture carrying `|` and `&` is slightly startling in
a file an adopter reads. **Recommendation: ship it.** An adopter inherits the same renderer and the
same exposure, and a test whose fixture is blander than reality is this repo's
`fixture-passes-by-finding-nothing` class.

## 9. Revision log

- rev-1 · 2026-08-11 · initial draft. Raised by unit 1's closing review as id=1 and filed as
  `TOOL-aWrittenMethod-6` when two escape attempts failed and only the loud refusal shipped.

## 10. Reuse audit

The reuse probe run for this unit set (`reuse_lookup.py "resolve a trustworthy base commit the run
cannot move, and escape values before substitution"`) surfaced the gotcha class
`heredoc-escape-reaches-the-regex.md` by name, which is the class both failed attempts fell into and
is cited in §4. It surfaced no escaping seam, because the repo has none: `grep -rn` over `tools/`
finds three independent `sed`-based substitution sites (`adopt-unattended.sh` `render()`,
`kit-dogfood-parity.test.sh` `render()`, `adopt-memory-tree.sh` `render_doc()`) and no shared helper.

That absence is itself the finding, and it is why S4 exists: the correct move is not to add a fourth
implementation with an escape bolted on, but to change all three to a mechanism that needs no escape.
A shared helper was considered and rejected — the three live in different kits, `tools/lib/` is
gov-internal and ships nothing, and a copy-installed kit must start without it. The precedent is
`resolve-python.sh`, which every kit carries INLINE and byte-identical under a gate, and which is the
shape to copy if these three ever need to converge on one implementation rather than one technique.
