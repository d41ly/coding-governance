# Review 1 — adversarial pass over the wave-1 sub-specs (V1, V3, V4)

**Scope:** the three sub-specs whose units change the `fail`-branch set, reviewed before any code.
**Method:** three independent reviewers, one per spec, each told to hunt the two shapes this repo
cares about — a gate that would be VACUOUS and a change that would make a gate PERMANENTLY RED — and
to RUN what settles a claim rather than read it. Nineteen findings. Every high-severity one below was
reproduced by measurement, not argued.

| # | Sev | Spec | Finding |
|---|---|---|---|
| M1 | blocker | V3 | widening only the SELECTOR reds 14 conforming files: the name grammar has no room for the unit-slug tail |
| M2 | high | V3 | check 12 is already MORE permissive than check 5 by exactly that tail — two EREs for one grammar |
| M3 | high | V1 | `FAIL_RE` captures to end of line; five manifest-check signatures would contain shell source and be permanently unarmable |
| M4 | high | V1 | S3's stated failure mode does not exist — the arm scan is per-pair; the real collision is in the PIN |
| M5 | high | V1 | the self-exclusion clause is unreachable, and its stated cause is wrong |
| M6 | high | V4 | `check-arms` does not see awk `print` branches, so V4's "this branch is ARMED" was already true |
| M7 | medium | V1 | aggregate floors let one gate's deleted guard be masked by another gate's addition |
| M8 | medium | V1 | the gate predicate would classify a `*.test.sh` quoting a fail line as a gate |
| M9 | medium | V3 | check 4 does NOT govern non-md inside the four subfolders — a documented rule with no implementation |
| M10 | medium | V3 | two of three fixtures are satisfied by ABSENCE; the red one is attributable to the wrong check |
| M11 | medium | V3 | rewording `fail 5`'s first line breaks its arm and drops the armed count below its floor |
| M12 | medium | V3, V4 | the doc edit direction is backwards: edit the LIVE copy, then `--render` |
| M13 | medium | V4 | the `!seen` sub-path has no fixture, so a partial implementation passes |
| M14 | low | V1 | `Problem` aborts the whole run, so one bad gate hides every other gate's findings |
| M15 | low | V1 | extensionless shell gates (`.githooks/pre-commit`, `pre-push`) fall outside a `*.sh` glob |
| M16 | low | V4 | the comment being rewritten lives inside a single-quoted awk program — no apostrophes |

## M1 — the unit as drafted lands a red merge bar (blocker)

V3 widened check 5's SELECTOR to any depth and left its NAME grammar alone. Check 5's basename ERE
is `<date>-<kind>[-<FAMILY>]-<slug>-<seq>.md` with nothing after the sequence number, and every real
nested spec carries a trailing unit slug — `…-spec-aFoldedQuarry-2-u6-indexed-join.md`.

Reproduced twice, independently. The reviewer patched a copy of the engine with exactly the spec's
two changes and got `HYGIENE check 5 FAILED` naming six files. Re-measured here against the tree as
it stands: **14 of 14 nested spec files fail the drafted grammar; 0 of 14 fail once check 12's
existing optional tail `(-[a-z0-9][a-z0-9-]*)?` is appended.** `memory hygiene` is the first leg of
the bar and the pre-push hook runs the full bar, so the unit as written blocks every push until
someone renames fourteen cited files or bulk-grandfathers the shape the kit calls canonical.

The spec measured the population's SIZE and called it conformance. Folded as S1b, with the number.

## M2 — one grammar, two EREs, and the divergence becomes load-bearing (high)

Check 12's spec selector already permits the trailing segment check 5 forbids. So the change as
drafted would make the two rules disagree on exactly the files that motivated the unit, and would
render check 12's optional-tail group dead — no file could carry it and survive check 5.

The fix is not just "append the tail to check 5" but "stop having two copies": the tail is hoisted to
one variable beside `FAM_ALT` and `DISC_ALT`, and both checks interpolate it. That is the
`two-answers-to-one-question` class, caught before it became load-bearing rather than after.

## M3 — five signatures would contain shell source, and no assertion can ever match them (high)

`FAIL_RE` captures to end of line. `check-memory-hygiene.sh` always ends the line at the message, so
that was safe. `manifest-check.sh` writes five of its branches inline —
`{ fail 2 "…"; BLOCK_OK=0; }` — so their captured messages carry the trailing shell, and the derived
signature ends in `"; BLOCK_OK=0; }`.

A test can never emit that: it is the gate's source, not its output. The unit would have written five
permanently-unarmable signatures into a shrink-only pin, so those rows could never legitimately
leave, and a correct arm asserting the real message would still be reported as missing. A gate that
lies about its own subject, minted inside the gate whose job is detecting vacuity. Folded: the
capture terminates at the closing quote of the shell string, with an inline-form fixture whose green
side asserts only the real message.

## M4, M5 — two of V1's own guarantees were untestable as written (high)

S3 justified the widened key with "one gate's arm would silence another's branch". That cannot
happen: the design pairs each gate with its own sibling test and the arm scan reads only that file.
So AC1 was green before and after the change — the headline guarantee, shipped untested, inside the
meta-gate that forbids exactly that. The collision that IS real lives in the PIN, whose keys are
global; the reviewer simulated it and found four manifest-check branches colliding with hygiene's pin
rows. S3 and AC1 now speak about the pin.

S6's self-exclusion is unreachable under an `*.sh` population, and its stated cause was wrong: the
matcher does not match its own matcher line (`(\d+)` is not digits) — what matches is the selftest's
own fixture strings. Folded: the clause is stated as an extension-scope fact in §3, and the rationale
names the fixture rather than an invented one.

## M6 — V4's acceptance criterion was already true before the unit (high)

`check-arms` keys on SHELL `fail` call sites. Check 12's per-spec findings, including the rev
message, are awk `print` statements funnelled into one `fail 12 "spec files dated >= …"`, which is
already ARMED. So V4's "this branch is ARMED" was green before a line of code, and V2's ordering
premise — "V4 changes the branch set" — is false.

Folded three ways: V4's S5/AC5 now say plainly that awk-level findings are not branches and that the
harness assertion is the only protection this change has; V4 gains a SOURCE-level assertion that the
reset line is present, beside the three source-level assertions the harness already carries; and V2's
S3 drops V4 from its ordering premise while keeping the V1 dependency, which is real.

## M9 — a documented rule with no implementation (medium)

V3's S4 declined to widen non-markdown handling on the grounds that check 4 covers it. Measured: it
does not. Check 4 inspects only the first segment under the build folder and `continue`s on the four
subfolder names, so nothing inside them is examined at any depth — a scratch repo with
`spec/notes.txt`, `spec/units/whatever.txt` and `spec/units/free-named.md` produced zero findings
from checks 3, 4 and 5. `HYGIENE.md` check 4's "non-md only in `build/`" describes a rule nothing
enforces.

Folded: S4 states the measurement instead of citing a guard that does not exist, and the missing
non-md rule becomes its own backlog row rather than a silently half-closed gap.

## M10, M11, M12, M13, M16 — the medium and low findings, all folded

M10: two of V3's three fixtures pass by ABSENCE if the selector is left unwidened, and the red one
asserts a bare path that three other checks also print. Folded: the legacy arm becomes two-state
(listed → silent, unlisted → red) and the red arm is attributed inside check 5's own output slice.

M11: check 5's first message line IS its `check-arms` signature and its arm sits at the armed floor
with no slack, so rewording it reds two gate legs. Folded: the reword lands on a continuation line.

M12: `kit-dogfood-parity` renders LIVE → SHIPPED, so editing the template alone reds the leg and the
printed remedy overwrites the edit. Folded into both specs: edit `memory/HYGIENE.md`, then render.

M13: V4's `!seen` sub-path — no `rev-` token anywhere in §9, a larger one in §10 — is newly reachable
and had no fixture; a partial implementation would pass. Folded as a third fixture.

M16: the comment V4 rewrites lives inside a single-quoted awk program, which is why the existing text
reads "engine s". Folded as a constraint, not a typo to fix.

## Disposition

All sixteen folded before any code. M1 alone would have cost a red merge bar and either fourteen
renames or a bulk grandfather of the canonical shape; it was found by patching the engine and running
it, which is the only way it could have been found.
