# TOOL-dDeclaredLoop-77 — a FETCH_HEAD URL is compared in the spelling git writes it, its user part stripped from both sides

**Status:** OPEN · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 39 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-76-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-10-24-build-TOOL-dDeclaredLoop-77-deviation-771.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-77-deviation-771.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-76-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-79 |
| [2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-76-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-78 TOOL-dDeclaredLoop-76 TOOL-dDeclaredLoop-79 |

<!-- /gen:spec-records -->

## 1. Goal

The round-4 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-68-spec-audit.md`)
confirmed finding **id 8 at HIGH**, its item **H2**. Its https half is item M16 at medium (id 36),
batched into `TOOL-dDeclaredLoop-79`. `TOOL-dDeclaredLoop-74` S1 keeps a `FETCH_HEAD` line only when its
URL equals `git remote get-url <remote>` after one trailing `/` and one `.git` are stripped. git writes
that URL without the user part, so over an scp-form or `ssh://user@` remote the two never match. Every
successful fetch of an SSH adopter is skipped; with the default branch unmoved no tracking-ref reflog
entry is written either, and the engine reads `stale-remote` above `act` indefinitely. 74's AC2 fetches
from a local path, which has no user part, so it cannot see this.

This unit compares both URLs in the spelling git writes into `FETCH_HEAD`. It repairs
`TOOL-dDeclaredLoop-74`.

## 2. Scope (IN)

- **S1** — `normalise_fetch_url(url)` in `tools/loop/position.py` spells a URL as git writes it into
  `FETCH_HEAD`, in two steps. First the user part is stripped: for a URL carrying `://` whose scheme is
  letters, digits, `+`, `.` and `-`, the bytes from just after `://` through the first `@` that comes
  before the first `/` after `://`; for an scp form, no `://` and an `@` followed later by a `:`, the
  bytes up to and including that `@`. A URL with no `@`, a drive-letter path such as `C:/` or a `/`
  before its first `:` is a local path and is left whole. Then every trailing `/` is stripped, then one
  trailing `.git`. Both sides of 74 S1's comparison pass through it; this supersedes 74 S1's "a trailing
  `/` and a trailing `.git`". Observed by AC1, AC2, AC3.
- **S2** — The plant `scp-remote` joins `position.py --fixture`: a bare repository under the fixture's
  scratch root, the remote's URL set to `git@example.com:up.git`, and `GIT_SSH_COMMAND` set in the fetch's
  own environment to a shim that runs `git-upload-pack` on that bare repository whatever host it is
  given. After `git fetch`, the reading ends `from FETCH_HEAD`. The plant `ssh-userinfo-remote` does the
  same over `ssh://user@example.com/up.git`. Observed by AC1, AC2.
- **S3** — The plant `url-forms` runs S1 over a table of configured and written pairs, each asserted
  equal or unequal: the two pairs probed in §4, a local path with a trailing `/`, an scp form with a
  trailing `/`, a different host (`git@other.example:up.git` against `example.com:up`, unequal) and a
  local drive path whose directory name holds an `@`, left whole. Observed by AC3.
- **S4** — No line the reading prints carries a configured URL: the `--explain` read-set names the remote
  by name, as 74 S1's skip line does, because a configured URL's user part may carry a token.
  Observed by AC4.

## 3. Non-goals (OUT)

- The https form with a user or a token: id 36, batched into `TOOL-dDeclaredLoop-79`, which plants it over
  S1; S1 already strips it, since git's rule is one rule for every scheme.
- A URL git rewrites through `url.<base>.insteadOf`: still skipped and named, 74 §5's conservative side.
- A bug-class checklist entry that a comparison against a URL git wrote runs a fixture over scp-form and
  user-part remotes, the finding's left-shift: the class is recorded at the close; S2 and S3 are this
  reading's fixtures.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-74` — S1's `FETCH_HEAD` line match and its URL normalisation in `tools/loop/position.py`, which this unit spells as git writes the URL
- **hands-off** `TOOL-dDeclaredLoop-79` — `normalise_fetch_url`, over which that unit plants the https remote carrying a user and a token (id 36)
- **hands-off** `TOOL-dDeclaredLoop-82` — the `url-forms` plant, S2's shim and §4, §5, §7 and §10, which that unit takes past the mismatch skip line, gives a git-written oracle and scp regression pairs, spells through `Path.as_posix()`, and corrects (the round-5 spec audit's ids 3, 9, 15, 16, 18, 22, 27)

## 4. Design

### Evidence

Probed 2026-10-24 on node `d`, git 2.54.0.windows.1, in a scratch repository under `%TEMP%`, fetching
through a `GIT_SSH_COMMAND` shim that runs `git-upload-pack` on a local bare repository: PINNED, that date.

| configured (`git remote get-url`) | written into `FETCH_HEAD` |
|---|---|
| `git@example.com:up.git` | `branch 'main' of example.com:up` |
| `ssh://user@example.com/up.git` | `branch 'main' of ssh://example.com/up` |
| `example.com:up.git/` | `branch 'main' of example.com:up` |

- The audit's skeptic recorded the same two user-part rows with git 2.54 (the report, id 8's verdict).
- The scheme check and the "`@` before the first `/`" bound are git's own `transport_anonymize_url`, as
  the report's id 36 cites it from `builtin/fetch.c`'s `store_updated_refs`; the https row is that
  documented rule and is UNVERIFIED by a live fetch here, which needs a network remote.
- 74 §4 recorded that a local path's trailing `/` is not written either.
- AC2's planted remote is the table's second row, configured as `ssh://user@example.com/up.git`. AC4's
  planted remote is configured as `https://u:SECRET@127.0.0.1:9/r.git`: its password is `SECRET`, and
  its port 9 makes the fetch fail at once.

### The normaliser

```
normalise_fetch_url(url):
    if "://" in url and scheme(url) matches [A-Za-z0-9+.-]+:
        rest = after "://" ; at = index of "@" in rest ; slash = index of "/" in rest
        if at >= 0 and (slash < 0 or at < slash): url = scheme + "://" + rest[at+1:]
    elif "@" in url and not local(url) and ":" in url[index("@"):]:
        url = url[index("@")+1:]
    url = url.rstrip("/")
    if url.endswith(".git"): url = url[:-4]
    return url
local(url) = no "@" in url, or url matches ^[A-Za-z]:[/\\], or a "/" precedes the first ":"
```

### Files touched (estimate)

- `tools/loop/position.py`

### Alternatives rejected

- **Comparing the tracking ref's sha with the `FETCH_HEAD` line's sha, ignoring URLs.** A fetch from a
  second remote naming its own `main` at the same sha would count, the case 74 §4 rejects URL-blind
  matching for.
- **Stripping the user part from the configured URL only.** The written side is already stripped, so the
  result is the same, but the trailing-`/` rule must still apply to both; one function over both sides
  states it once.

## 5. Production-readiness checklist

- security — S4 keeps a token in a configured URL off every printed line; the shim exists only in the
  fixture's scratch environment.
- perf / scale — string work per `FETCH_HEAD` line, nothing new spawned.
- error / empty / loading states — a URL form S1 does not equate is still skipped and named, never fresh.
- observability — the skip line names the remote and the branch, unchanged.
- risks — a scheme URL whose user part itself holds `/` or a second `@` reads skipped, the conservative
  side; `--explain` names it.
- testing — AC1 to AC4 as fixture plants; the arm under §7, observed at the close.
- migration — none: the reading is unbuilt at base.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When `python position.py --fixture --plant scp-remote` fetches the default branch through the
  `GIT_SSH_COMMAND` shim from a remote configured as `git@example.com:up.git`, the reading ends
  `from FETCH_HEAD` and the read-set names no `skipped` line for that file.
  Red when: the configured URL is compared with its user part, so the file is skipped as
  `no line for main of origin`.
  cost: one bare repository and one fetch over the shim, seconds.
- **AC2** — When `--plant ssh-userinfo-remote` does the same over the `ssh://` remote with the user part
  `user@` that §4's Evidence names, the reading ends `from FETCH_HEAD`.
  Red when: only the scp form is stripped.
- **AC3** — When `--plant url-forms` runs S3's table, every pair reads as tabled, the different host
  unequal and the drive path with an `@` left whole.
  Red when: a local path is cut at its `@`, or two hosts compare equal.
- **AC4** — When `--plant url-forms` also runs the reading over the `https://` remote §4's Evidence names,
  whose user part carries the password `SECRET` and whose fetch fails, the reading's output does not
  contain `SECRET`.
  Red when: a skip or read-set line prints the configured URL.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

This pass keeps the sibling-minted `loop position fixtures` leg (`TOOL-dDeclaredLoop-7`) green, which runs
`position.py --fixture`; the leg is outside the base manifest.

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 · the scp-remote, ssh-userinfo-remote and url-forms plants, staged against TOOL-dDeclaredLoop-74's trailing-slash-and-.git normalisation · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Normalise the URLs as git does, or match by branch and sha?** The fix offers both. (a) strip the
  user part from both sides; (b) compare `refs/remotes/<remote>/<default>` with the line's sha. (b) counts
  a second remote's fetch at an equal sha, which 74 §4 rejects, so it fails 74's own design; (a) keeps the
  remote check. RESOLVED (agent, 2026-10-24, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-4 spec audit's id 8 (HIGH, item H2).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the bullets mirroring the edges of
  TOOL-dDeclaredLoop-82, written by the round-5 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is 74's reading in `tools/loop/position.py`, unbuilt at base, whose normalisation this unit
restates. `python tools/codebase-map/reuse_lookup.py "strip the user part from a remote url before comparing"`
ranked `before`, `resolve_compare_base`, `resolve_remote` (`tools/lib/resolve_remote.py`) and
`build_remote_ci_red_streak`; none strips a URL's user part. The nearest code is `derive_redacted`
(`tools/run-gates/measure_legs.py:531`), whose `REDACT_TEXT` (:528) masks `user:password@` with `***`
in scheme URLs only: it leaves an scp form and a password-less user untouched and writes a mask where git
writes nothing, so no existing seam fits.

Recall terms used: FETCH_HEAD remote url scp ssh userinfo anonymize transport git fetch normalise stale-remote position engine
