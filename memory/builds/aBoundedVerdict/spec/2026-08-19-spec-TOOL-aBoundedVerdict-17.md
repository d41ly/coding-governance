# TOOL-aBoundedVerdict-17 — a split fetch/push URL stops being an unsatisfiable authorization

**Status:** SPECCED · rev-1 · 2026-08-19 · node c · Tier-2 · base 098bebd9 · streams tooling

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
  that a caller may have discarded: it rides the same channel as the other close-path diagnostics, so
  `TOOL-aBoundedVerdict-12` is a dependency rather than an ornament.
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

`unattended.sh:231-235` reads:

```
uf=$(GIT ls-remote --get-url "$rem")
up=$(GIT remote get-url --push "$rem")
if [ "$uf" != "$up" ]; then  fail 25 …; return 1;  fi
```

A literal comparison. On this node the clone has one URL and no `pushurl`, so it passes — which is why
the defect is latent rather than observed here, and why it needs fixtures rather than a corpus
measurement. The split it refuses is produced by two independent mechanisms:

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

None. No clone in this fleet carries a split today, so nothing changes for anyone currently running;
the unit removes a trap rather than repairing damage.

### Rollout

S1 and S5 together — the normalisation and the surviving refusal are one edit and separating them would
ship a check that accepts everything. S2 next. S3 after `TOOL-aBoundedVerdict-12`, since a warning on a
channel that is discarded is not a warning. S4's fixtures land with S1.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the normaliser and check 25) ·
`tools/unattended/unattended.test.sh` (four fixtures: two split mechanisms, one equivalent-modulo-`.git`,
one genuinely different) · `.memory-tree.conf` (`ARMS_FLOORS`, if the warning is a new call site) ·
`memory/map/features/unattended.md` (the dossier states what check 25 proves) · the kit version constant.

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
  carries a line naming both URLs — observed in `--close`'s output, and dependent on
  `TOOL-aBoundedVerdict-12`.
- **AC7** — When `memory/map/features/unattended.md` is read, it states that check 25 proves
  same-spelling-modulo-transport rather than same endpoint, and
  `python tools/codebase-map/test_codebase_map.py` is clean.

## 7. Gates

`tools/unattended/unattended.test.sh` · `tools/unattended/check-unattended.sh` +
`check-unattended.test.sh` · `python tools/memory-tree/check-arms.py` ·
`python tools/codebase-map/test_codebase_map.py` · `tools/check-kit-versions.sh` ·
`tools/check-testsuite-counts.sh` · `bash tools/run-gates.sh`.

## 8. Open questions

- **F1 — does the normaliser live in the driver only, or is it shared with the gate leg?** The leg makes
  its own remote observations, so it may carry the same comparison. **Recommendation: check the leg
  first and share only if it duplicates the predicate** — a helper extracted for one caller is the
  abstraction this repo's rules refuse, and a second copy is the class this build keeps finding. The
  answer is a two-minute grep at build time, which is why this is a fork and not a design.
  RESOLVED (agent, 2026-08-19, delegated): share if and only if the leg duplicates it, decided by
  grep at build time. Mechanism-only.

- **F2 — is the surviving mismatch a warning on every verb, or only on `--close`?** `--preflight` is
  where an operator can still fix it, so warning there is more useful; `--close` is where an unattended
  run reads it. **Recommendation: both**, since the check runs in `observe_anchor` and both verbs call
  it — so this costs nothing and the choice is really about whether to suppress it anywhere.

## 9. Revision log

- rev-1 · 2026-08-19 · initial draft. Derived from the close-path audit's high 17, verified
  independently against `unattended.sh:231-235`: the comparison is `[ "$uf" != "$up" ]`, a literal
  string test whose failure branch returns 1 on the one item `verb_close` refuses to override. The
  defect is LATENT on this fleet — this clone has one URL and no `pushurl` — which is why the unit
  specifies fixtures and says plainly that no corpus arm exists. F1 resolved under the delegated fork
  rule; F2 carries a recommendation and is left open.

## 10. Reuse audit

The seam is `observe_anchor` itself and its numbered-refusal convention: this unit changes one check's
comparison and one check's severity, and adds no new observation. `GIT()` remains the only git path.

The second seam is the diagnostic channel `TOOL-aBoundedVerdict-12` widens — S3 is a caller of it, and
naming that dependency is what stops this unit inventing a second way to report a warning.

No `reuse_lookup.py` seam exists for URL normalisation in this tree, and the SET-level recall pass for
this build is recorded in the sibling specs with its terms. Recorded as the probe's answer: nothing here
normalises a git URL today, so this is the first such rule and it is deliberately textual and small.
