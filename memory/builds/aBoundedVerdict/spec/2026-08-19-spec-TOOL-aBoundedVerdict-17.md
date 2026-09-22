# TOOL-aBoundedVerdict-17 — a split fetch/push URL stops being an unsatisfiable authorization

**Status:** CLOSED · rev-4 · 2026-08-21 · node c · Tier-2 · base 098bebd9 · streams tooling

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-08-19-review-TOOL-aBoundedVerdict-1-2.md](../reviews/2026-08-19-review-TOOL-aBoundedVerdict-1-2.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-11 TOOL-aBoundedVerdict-12 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-14 TOOL-aBoundedVerdict-15 TOOL-aBoundedVerdict-16 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 |
| [2026-08-20-review-TOOL-aBoundedVerdict-1-round2.md](../reviews/2026-08-20-review-TOOL-aBoundedVerdict-1-round2.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 |
| [2026-08-20-review-TOOL-aBoundedVerdict-1.md](../reviews/2026-08-20-review-TOOL-aBoundedVerdict-1.md) | spec-audit | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |
| [2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md](../reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round3.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |
| [2026-08-21-review-TOOL-aBoundedVerdict-1-round4.md](../reviews/2026-08-21-review-TOOL-aBoundedVerdict-1-round4.md) | diff-review | TOOL-aBoundedVerdict-1 TOOL-aBoundedVerdict-2 TOOL-aBoundedVerdict-3 TOOL-aBoundedVerdict-4 TOOL-aBoundedVerdict-5 TOOL-aBoundedVerdict-13 TOOL-aBoundedVerdict-18 TOOL-aBoundedVerdict-19 TOOL-aBoundedVerdict-21 |

<!-- /gen:spec-records -->

## 1. Goal

`observe_anchor`'s check 25 compares the fetch URL and the push URL as literal strings and returns a
refusal on any difference — so a clone configured to fetch over HTTPS and push over SSH, which is an
ordinary and correct setup, can never satisfy `authorization-reachable`, and that is the one
Definition-of-Done item `verb_close` refuses to override. Make the check compare endpoints rather
than spellings, and make a residual mismatch a warning rather than a wedge.

## 2. Scope (IN)

- **S1** — the comparison normalises both URLs to a host-and-path pair before comparing: scheme
  dropped, an `scp`-style `git@host:owner/repo` form recognised as equivalent to `ssh://host/owner/repo`,
  a trailing `.git` and a trailing slash ignored, and the host compared case-insensitively.
- **S2** — a mismatch that survives normalisation is a WARNING that does not return 1. The check's own
  comment already states what it is: *"A cost-raiser, NOT the property … Kept because it is free and
  catches the honest misconfiguration."* A cost-raiser that wedges the un-overridable item is
  disproportionate to its own stated purpose.
- **S3** — the warning is recorded where an unattended run's reader will find it, not only on stdout
  that a caller may have discarded: it rides the same channel as the other close-path diagnostics —
  `DOD_OUT` plus the `observe_anchor` output `TOOL-aBoundedVerdict-12` stopped silencing. **That unit
  is CLOSED as of 2026-08-20**, so this is a caller of a channel that already exists at HEAD, not a
  dependency on unlanded work; what the builder owes is a re-read of the landed channel's shape, not a
  wait.
- **S4** — `remote.<name>.pushurl` and `url.<base>.pushInsteadOf` are both exercised by fixtures,
  because they are two different mechanisms that produce the same split and only one of them is
  visible in `remote.origin.url`.
- **S5** — the check keeps its refusal for the case it was written for: two URLs naming genuinely
  DIFFERENT hosts or different paths. That is the honest misconfiguration, and it stays a refusal
  because the anchor and the landing would then observe and push to two different repositories.

## 3. Non-goals (OUT)

- Not the anchor's security property. Check 25 is explicitly a cost-raiser and not the property — the
  driver's own comment says a relay the run seeded satisfies it with one URL and one config source. This
  unit does not strengthen it and must not claim to.
- Not the transport bound. `TOOL-aBoundedVerdict-13` owns what happens when the endpoint does not
  answer; this unit owns what happens when two spellings name the same one.
- Not URL parsing in general, and no dependency added to do it. The normalisation is a bounded set of
  textual rules over the forms git itself accepts, written in shell, because the kit ships as shell.
- Not credential or auth differences between the two transports. Whether the run CAN push over its
  push URL is the lander's business and the pre-push hook's; this check only asks whether the two
  endpoints are the same place.
- No change to which items are overridable. The fix is to stop the item being unsatisfiable, not to
  make it waivable.

## 4. Design

### What was measured

`unattended.sh:231-235`, at this spec's declared base, reads:

```
uf=$(GIT ls-remote --get-url "$rem")
up=$(GIT remote get-url --push "$rem")
if [ "$uf" != "$up" ]; then  fail 25 …; return 1;  fi
```

A literal comparison, and it is **unchanged at HEAD** — re-read 2026-08-20, byte for byte; only its
line numbers moved. The reference above is deliberately left at the declared base rather than
renumbered to a HEAD that will move again. Locate it with
`grep -n 'fail 25' tools/unattended/unattended.sh`. On this node the clone has one URL and no
`pushurl`, so it passes — which is why the defect is latent rather than observed here, and why it
needs fixtures rather than a corpus measurement. The split it refuses is produced by two independent mechanisms:

| mechanism | visible in `remote.origin.url` | produces a split |
|---|---|---|
| `remote.origin.pushurl` | no — it is a separate key | yes |
| `url.<base>.pushInsteadOf` | no — it rewrites at use time | yes |

S4 exists because a fixture built with only the first would leave the second untested, and the second
is the one an operator sets globally and forgets.

### Normalisation, and its limit

The rules are textual and deliberately few. What they do NOT do is resolve DNS, follow redirects, or
canonicalise a host alias — so two names for one server still mismatch, and under S2 that is a warning
rather than a wedge, which is the whole reason S2 is in scope. Stating the limit is what keeps a later
reader from believing the check proves same-endpoint identity; it proves same-spelling-modulo-transport.

### Inventory

| Concern | Today | After |
|---|---|---|
| fetch HTTPS, push SSH, same repo | refusal, on the un-overridable item | equivalent; no refusal |
| `pushInsteadOf` rewriting the push URL | refusal | equivalent |
| a trailing `.git` on one side only | refusal | equivalent |
| two genuinely different hosts or paths | refusal | refusal, unchanged |
| a residual mismatch after normalisation | refusal | warning, on the diagnostic channel |
| what the check claims to prove | same endpoint | same spelling modulo transport, stated |

### Migration

None. This node's clone has one URL and no `pushurl` (re-verified 2026-08-20 with
`git config --get-regexp 'remote\..*\.(url|pushurl)|url\..*\.pushinsteadof'`), so nothing changes for
it. The claim is scoped to what is observable from here: the other registered nodes' local config
cannot be read from this tree, so "no clone in the fleet carries a split" is not a claim this spec
can make and no longer makes one. The unit removes a trap rather than repairing damage either way.

### Rollout

S1 and S5 together — the normalisation and the surviving refusal are one edit and separating them would
ship a check that accepts everything. S2 next. S3 needs the close-path diagnostic channel to exist,
which it now does — `TOOL-aBoundedVerdict-12` is CLOSED — so S3 waits on nothing and only has to name
the channel as landed rather than as planned. S4's fixtures land with S1.

### Files touched (estimate)

- `tools/unattended/unattended.sh` — the normaliser and check 25.
- `tools/unattended/unattended.test.sh` — four fixtures: two split mechanisms, one
  equivalent-modulo-`.git`, one genuinely different.
- `.memory-tree.conf` (`ARMS_FLOORS`, if the warning is a new call site).
- `memory/map/features/unattended.md` — the dossier states what check 25 proves.
- `memory/guides/SESSION-KICKOFF.md` — `.memory-tree.conf` is on the kickoff manifest's watch list
  (the list is that file's manifest-audit block), so the claims derived from it are re-audited and
  `last-audit` re-stamped in the SAME commit as the change, or the manifest ratchet reds it. This
  rides the `ARMS_FLOORS` edit above and is conditional in exactly the same way: no `.memory-tree.conf`
  edit, no re-stamp owed by this unit.
- **the kit version bump, which is NOT one carrier.** `tools/check-kit-versions.sh` forces the whole
  set: `KIT_UNATTENDED_VERSION=` **and** its same-line `gov:kit` marker in both
  `tools/unattended/unattended.sh` and `tools/unattended/check-unattended.sh`; the `gov:kit` marker in
  `tools/unattended/PROTOCOL.template.md` and in `tools/unattended/SKILL.template.md`; and the
  re-rendered `.claude/skills/unattended/SKILL.md`, which `check-wiring.sh` compares against the
  tracked template. Read the enforcing script for the set rather than trusting a count typed here —
  "the constant", singular, is how a bump lands half-done and reds the bar.

### Alternatives rejected

- **Drop check 25 entirely.** Tempting, since its own comment calls it a cost-raiser. Rejected: it does
  catch the honest misconfiguration, and deleting a check because it is imperfect loses the case it
  gets right. S2 keeps the signal and removes the wedge.
- **Keep the refusal and let the operator set `pushurl` to match.** Rejected: it asks an operator to
  break a working configuration to satisfy a check that admits it is not the property, and an
  unattended run cannot do it at all.
- **Compare the two URLs by asking git to resolve both.** git has no "resolve this remote to a
  canonical endpoint" verb; `ls-remote --get-url` and `remote get-url --push` are already the two
  resolutions, and they disagree by design.
- **Make `authorization-reachable` overridable for this case.** Refused, twice over: an override on the
  authorization check IS the authorization check, and a per-cause override is a wider hole than the one
  it patches.
- **Normalise by stripping everything but the final path segment.** Rejected: two different owners' repos
  of the same name would compare equal, which turns a cost-raiser into a false assurance.

## 5. Production-readiness checklist

- **security** — the one line to read carefully. Normalisation must not make two DIFFERENT repositories
  compare equal; S5 and the rejected final-segment alternative are the guard, and the fixture for
  genuinely-different endpoints is what proves it. The check's status as a cost-raiser rather than the
  property is unchanged and is restated in the dossier by S1's file list.
- **perf / scale** — N/A. Two string transforms.
- **a11y** — N/A.
- **i18n** — the host comparison is case-insensitive ASCII; an internationalised hostname is out of
  scope and would compare as a literal, which is the conservative direction.
- **error / empty / loading states** — an empty fetch or push URL must not normalise to equal-empty and
  pass. That is the `fixture-passes-by-finding-nothing` shape and it needs its own arm.
- **observability** — S2's warning names both URLs and says it did not refuse, so a reader can tell the
  difference between "checked and equivalent" and "checked, different, allowed".
- **risks** — low, and the residual is stated: the check proves less than its name suggests, and §4 says
  so rather than implying otherwise.
- **testing + left-shift gates** — four fixtures in S4 plus the empty-URL arm. No corpus arm exists,
  because no clone here carries a split — which the spec states rather than letting the absence read as
  coverage.
- **migration / rollback** — none; revert is the normaliser.
- **user docs** — the map dossier's claim about what check 25 proves.

## 6. Acceptance criteria

- **AC1** — When a fixture clone sets `remote.origin.pushurl` to the SSH form of its HTTPS fetch URL,
  `bash tools/unattended/unattended.sh --close <slug>` does not refuse on check 25; against the shipped
  driver it does.
- **AC2** — When the split is produced by `url.<base>.pushInsteadOf` instead, the same holds — the
  second mechanism's arm, which a `pushurl`-only fixture would not reach.
- **AC3** — When one side carries a trailing `.git` and the other does not, the two compare equivalent.
- **AC4** — When the two URLs name different paths on the same host, check 25 still refuses and its
  message names both — the arm in `tools/unattended/unattended.test.sh` that proves S1 did not turn the
  check into a tautology.
- **AC5** — When either URL is empty, the check does not report equivalence — the
  `fixture-passes-by-finding-nothing` arm, which sets `remote.origin.pushurl` to the empty string.
- **AC6** — When a mismatch survives normalisation, the run does not refuse and the diagnostic channel
  carries a line naming both URLs — observed in `--close`'s output, on the channel
  `TOOL-aBoundedVerdict-12` already landed.
- **AC7** — When `memory/map/features/unattended.md` is read, it states that check 25 proves
  same-spelling-modulo-transport rather than same endpoint, and
  `python tools/codebase-map/test_codebase_map.py` is clean.

## 7. Gates

`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` · `python tools/memory-tree/check-arms.py` ·
`python tools/codebase-map/test_codebase_map.py` · `tools/check-kit-versions.sh` ·
`tools/check-testsuite-counts.sh` · `bash tools/run-gates/run-gates.sh`.

## 8. Open questions

none - every fork below is RESOLVED in place, each naming the resolver and the authority.
This line is the machine-read one; the bullets carry the reasoning.

- **F1 — does the normaliser live in the driver only, or is it shared with the gate leg?** The leg makes
  its own remote observations, so it may carry the same comparison. **Recommendation: check the leg
  first and share only if it duplicates the predicate** — a helper extracted for one caller is the
  abstraction this repo's rules refuse, and a second copy is the class this build keeps finding. The
  answer is a two-minute grep at build time, which is why this is a fork and not a design.
  RESOLVED (agent, 2026-08-19, delegated): share if and only if the leg duplicates it, decided by
  grep at build time. Mechanism-only.
  Read on 2026-08-20, and recorded as an observation rather than as a re-resolution: the leg's only
  remote observations are its two `ls-remote` calls and it carries no fetch-versus-push URL comparison
  at all, so on that reading the answer is DO NOT share. Re-run the grep at build time — the point of
  the fork was that the answer is cheap and dated, and this note does not spend it.

- **F2 — is the surviving mismatch a warning on every verb, or only on `--close`?** `--preflight` is
  where an operator can still fix it, so warning there is more useful; `--close` is where an unattended
  run reads it. **Recommendation: both**, since the check runs in `observe_anchor` and both verbs call
  it — so this costs nothing and the choice is really about whether to suppress it anywhere.
  RESOLVED (agent, 2026-08-20, delegated): BOTH verbs. Mechanism-only and the feature-rich
  survivor at zero cost — the check runs inside `observe_anchor`, which both verbs already call, so
  warning on one of them would mean adding suppression rather than saving work. `--preflight` is
  where an operator can still fix it; `--close` is where an unattended run reads it.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's high 17, verified
  independently against `unattended.sh:231-235`: the comparison is `[ "$uf" != "$up" ]`, a literal
  string test whose failure branch returns 1 on the one item `verb_close` refuses to override. The
  defect is LATENT on this fleet — this clone has one URL and no `pushurl` — which is why the unit
  specifies fixtures and says plainly that no corpus arm exists. F1 resolved under the delegated fork
  rule; F2 carries a recommendation and is left open.

- rev-2 · 2026-08-20 · M3 fork sweep, before any code. F2 RESOLVED as recommended, both verbs — the
  check already runs where both call, so the narrow option costs a suppression the wide one does not.
  §8's first non-blank line is now the machine-legal `none` form.

- rev-3 · 2026-08-20 · the M4 spec audit's 2026-08-20 round, folded, plus a re-verification of every
  factual claim this spec makes about the driver and the leg — its figures were taken at a base five
  landed units ago. What was wrong:
  **H20** — Files touched said "the kit version constant", one file, where `tools/check-kit-versions.sh`
  forces a set: the `KIT_UNATTENDED_VERSION=` assignment **and** its same-line `gov:kit` marker in the
  driver and in the leg, the marker in `PROTOCOL.template.md` and in `SKILL.template.md`, and the
  re-rendered `.claude/skills/unattended/SKILL.md`. Named singular, a bump lands half-done and reds the
  bar; the carriers are now enumerated with the enforcing script named as their source rather than a
  count.
  **M13** — `.memory-tree.conf` is on the kickoff manifest's watch list and
  `memory/guides/SESSION-KICKOFF.md` was absent from Files touched, so the ratchet would have redded the
  commit both staged and committed. Added, with the same-commit re-stamp note and the honest caveat
  that it is conditional in exactly the way the `ARMS_FLOORS` edit it rides is.
  **The re-verification, and it found one claim that had gone false.** `TOOL-aBoundedVerdict-12` is
  CLOSED, so S3's "a dependency rather than an ornament", the Rollout's "S3 after
  `TOOL-aBoundedVerdict-12`" and AC6's "dependent on" all described a wait that no longer exists. All
  three now name the channel — `DOD_OUT` plus the `observe_anchor` output that unit stopped silencing —
  as landed, and what the builder owes is a re-read of its shape rather than a sequencing constraint.
  Three claims that still HOLD, checked rather than assumed: check 25's five lines are byte-identical at
  HEAD (only the line numbers moved, and the base-era reference is left alone per the fold rule, with a
  grep given instead); `authorization-reachable` is still in `DOD_CORE` and still the item the close
  path refuses to override; and `tools/check-testsuite-counts.sh` and `memory/map/features/unattended.md`
  both still exist under the paths §7 and Files touched give. One claim NARROWED rather than deleted:
  Migration said "no clone in this fleet carries a split", which this tree cannot observe — it is now
  scoped to this node's config, with the command that read it. And F1 gains a dated observation, not a
  re-resolution: the leg carries no fetch-versus-push comparison at HEAD, so today's answer to "share
  the normaliser?" is no, re-grep at build time.

- rev-4 · 2026-08-21 · **built, and both of its fixtures were passing by finding nothing.** `norm_endpoint` now detects
  scp-style by git's own rule - a colon before any slash - rather than by the presence of a user. The
  old key was wrong two ways, both measured against the shipped function: a USERLESS
  `github.com:alice/repo` fell through to the scheme path, where the host split DELETED the first
  path segment, so `alice/repo` and `bob/repo` both normalised to `github.com/repo` - two
  repositories comparing EQUAL, which would let a run anchor on one repo and land on another. And
  `git@github.com:alice/repo` normalised differently from `github.com:alice/repo`, so one place in
  two spellings compared DIFFERENT, which is the wedge this unit exists to remove.

  **The acceptance fixtures did not exercise the branch at all**, and the closing review caught it.
  MECHANISM ONE wrapped the URL in `ssh://` and a second `s|...|` stripped it straight back off a
  drive-letter path; MECHANISM TWO mapped `pushInsteadOf` to the base it already used, an identity
  rewrite. Both produced fetch == push, so the warn-and-continue branch - this unit's entire runtime
  behaviour - never ran and two `miss` assertions passed by finding nothing. Reproduced in a scratch
  clone, then replaced: a trailing slash for one, the userless-vs-user scp pair for the other, each
  with a `same` assertion proving the fixture actually splits, and POSITIVE assertions on the note.
  An absence assertion cannot tell a branch that warned from a branch that never ran.

  Also built here: the split-URL note no longer writes to `DOD_OUT`. That channel reached no reader -
  `gates-green` opens with an unconditional clear - and when that item was OVERRIDDEN the stale text
  survived and printed as the NEXT unmet item's detail. `dod_met` clears the channel on entry now.

## 10. Reuse audit

The seam is `observe_anchor` itself and its numbered-refusal convention: this unit changes one check's
comparison and one check's severity, and adds no new observation. `GIT()` remains the only git path.

The second seam is the diagnostic channel `TOOL-aBoundedVerdict-12` widens — S3 is a caller of it, and
naming that dependency is what stops this unit inventing a second way to report a warning.

No `reuse_lookup.py` seam exists for URL normalisation in this tree, and the SET-level recall pass for
this build is recorded in the sibling specs with its terms. Recorded as the probe's answer: nothing here
normalises a git URL today, so this is the first such rule and it is deliberately textual and small.
