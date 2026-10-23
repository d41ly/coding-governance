# TOOL-dFairHearing-21 — the held-out freeze check hashes the bytes it scores and refuses a shallow history

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 15 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-21-deviation-211.md](../build/2026-10-23-build-TOOL-dFairHearing-21-deviation-211.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief-2.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-22 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-20-promoted-fix-brief.md) | research | TOOL-dFairHearing-20 TOOL-dFairHearing-22 TOOL-dFairHearing-23 |
| [2026-10-23-prompt-TOOL-dFairHearing-21-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-21-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-20-23-spec-audit.md) | spec-audit | TOOL-dFairHearing-22 TOOL-dFairHearing-20 TOOL-dFairHearing-23 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit's finding id 39 (item H2, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-1-spec-audit.md`) is closed: the
scorer factory's `check_held_out_frozen` certifies a held-out set as frozen only when the working-tree
bytes it scores hash to the blob the freeze committed, and only in a history that is not shallow.
Today `TOOL-dFairHearing-14` S3 checks only that `git log --format=%H -- <path>` lists one commit, so an
uncommitted edit after the freeze, or a shallow clone whose boundary commit is the only one listed,
still prints `frozen at <sha>`.

## 2. Scope (IN)

- **S1** — `check_held_out_frozen` in `tools/workflows/replay_scorer.py` refuses, exit 2, when
  `git rev-parse --is-shallow-repository` prints `true`, naming the path and that a shallow history
  cannot show a freeze. The refusal runs before the history read. Observed by AC2.
- **S2** — After the history read finds its one commit `<freeze>`, `check_held_out_frozen` compares
  `git hash-object -- <path>` with `git rev-parse <freeze>:<path>` and refuses, exit 2, when they
  differ, naming the path, the working-tree object id and the freeze's blob id. The first output line
  `frozen at <sha>` prints only after both checks pass. Observed by AC1 and AC3.
- **S3** — The factory's paragraph in `tools/workflows/README.md` states that the freeze is the bytes
  scored, hashed through the checkout's filters, and that a shallow history refuses. Observed by AC4.
- **S4** — The arms the `New arm:` line in §7 declares, in the factory's runner. Observed by AC1 and
  AC2 through that line, RED-first at the close.

## 3. Non-goals (OUT)

- No check that a prompt author never read the held-out file: `TOOL-dFairHearing-14` §4 "What the rules
  do not check" keeps that recorded, not checked.
- No change to the tuning-overlap rule, the one-commit rule or any other rule of `check_experiment`.
- No `--no-filters` hashing: the comparison is of the bytes git would store, so a CRLF checkout of an
  LF blob compares equal (§4 Evidence).
- No deepening of a shallow clone. The factory reads and spawns nothing that fetches.

### Edges

- **consumes-from** `TOOL-dFairHearing-14` — `check_held_out_frozen`, its `heldOut` manifest key and its `frozen at <sha>` first line, which S1 and S2 tighten; without them there is no freeze check to tighten
- **hands-off** `TOOL-dFairHearing-27` — finding ids 14, 16, 30 and 35 of the spec audit of units 20 to 23: the held-out path normalised before any `<rev>:<path>` read and a failed git call refused by name, superseding S2's verbatim path (its S7, S8, AC5); `ARMS_DECLARED` raised by this unit's arms, superseding the floor "none" (its S19, AC14); the clone-path reason marked UNVERIFIED (its S28, AC23)

## 4. Design

### Evidence

Measured 2026-10-23 in this checkout, PINNED.

- The held-out file `memory/builds/aScoutedSeam/build/2026-10-18-build-TOOL-aScoutedSeam-1-13-held-out-cases.json`
  has one commit, `b6c828a92`. Its working-tree copy carries CRLF line endings under
  `core.autocrlf=true`, and `git hash-object -- <path>` prints `078445c223a144268fbfff32b2244d14dbc2eb52`,
  equal to `git rev-parse b6c828a92:<path>`. So the filtered hash agrees with the freeze on a
  correct checkout, and a raw-byte hash would not.
- `git rev-parse --is-shallow-repository` prints `false` here, so the shallow refusal is exercised by
  a fixture, never by this tree.

### The check, in order

```
check_held_out_frozen(path, repo):
  path opens with "-" or leaves repo                 -> exit 2   (TOOL-dFairHearing-14 §5, unchanged)
  git rev-parse --is-shallow-repository == "true"    -> exit 2   shallow history, no freeze provable
  git log --format=%H -- <path> lists != 1 commit    -> exit 2   (TOOL-dFairHearing-14 S3, unchanged)
  git hash-object -- <path> != git rev-parse <freeze>:<path>
                                                     -> exit 2   working tree differs from the freeze
  otherwise print "held-out: frozen at <freeze> · ..."
```

Every git call runs with argv and `cwd=repo`, never through a shell. `hash-object` is given `--` so a
path that passed the leading-dash refusal still cannot be read as an option.

### Inventory

None minted: S1 and S2 extend `check_held_out_frozen`, which `TOOL-dFairHearing-14` mints.

### Files touched (estimate)

- `tools/workflows/replay_scorer.py`
- `tools/workflows/README.md`

### Alternatives rejected

- **Compare against HEAD's blob instead of the freeze's.** With exactly one commit in the history the
  two are the same blob, so it adds a rev-parse and proves nothing more; the freeze is the commit the
  first line names.
- **Hash with `--no-filters`.** A CRLF checkout of the frozen file then differs from its blob, so the
  real held-out set here would refuse (§4 Evidence).

## 5. Production-readiness checklist

- security — two more git calls with argv on a path already refused when it opens `-` or leaves the
  repository; no write path.
- perf / scale — two git calls per held-out path.
- error / empty / loading states — a shallow history and a moved working tree each exit 2 by name.
- observability — the refusal names the path and both object ids, so a reader sees which bytes moved.
- risks — a checkout whose filters differ from the freeze's (a changed `.gitattributes`) can hash
  differently; it refuses loudly, never passes silently.
- testing — scratch fixture repositories under `%TEMP%`; the arms in §7 are observed RED then GREEN by
  the main loop at the close.
- migration — none: the manifests that name `heldOut` are new in this build.
- user docs — the factory paragraph of `tools/workflows/README.md`; no page under `help/`.

## 6. Acceptance criteria

- **AC1** — When a scratch fixture repository under `%TEMP%/fhh` commits a held-out file once and a
  manifest names it as `heldOut`, `python replay_scorer.py --experiment <m>` (the factory §4 Files
  touched names) prints
  `frozen at <sha>` first; after one byte is appended to that file and left uncommitted, the same run
  exits 2 and its stderr names the path and both object ids.
  Red when: only the history is read, so the edited file still prints `frozen at <sha>`.
  fixture: the repository goes under `%TEMP%/fhh`, since a clone path under the session scratchpad
  exceeds the Windows path limit; the tree holds none today.
- **AC2** — When the same fixture is cloned with `git clone --depth 1 file://<fixture> "$TEMP/fhs"` and
  `--experiment` runs over the shallow clone, it exits 2 naming the shallow history before any figure
  line.
  Red when: the shallow clone's single boundary commit is read as the freeze.
- **AC3** — When `--experiment` runs over a manifest whose `heldOut` names the real held-out file of §4
  Evidence in this checkout, the first line reads `frozen at b6c828a92` and the run proceeds.
  Red when: the bytes are hashed without the checkout's filters, so a CRLF checkout of the frozen
  blob refuses.
  figure: the sha and blob id are PINNED, measured 2026-10-23.
- **AC4** — When `grep -n "hash-object\|shallow" tools/workflows/README.md` runs, it prints the
  factory paragraph's sentences on the filtered hash and the shallow refusal.
  Red when: the README still describes the freeze as a one-commit history alone.

## 7. Gates

`review-replay selftest` · `verifier fan-out self-test` · `tier2-review self-test` · `unattended-build self-test` · `review-join self-test` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/workflows/replay_scorer.py (its runner, in the `review-replay selftest` leg) · covers AC1 AC2 · a fixture held-out file edited after its freeze and a shallow clone of it, staged against the factory at `TOOL-dFairHearing-14`'s commit, which prints frozen for both · none

## 8. Open questions

- **F1 — Which bytes does the freeze compare?** Options: (a) the working-tree file through
  `git hash-object` with the checkout's filters, against the freeze's blob; (b) the raw bytes, with
  `--no-filters`; (c) HEAD's blob, not the working tree. (b) refuses the real held-out set, whose CRLF
  checkout differs from its LF blob (§4 Evidence), failing AC3; (c) never sees an uncommitted edit, the
  finding itself. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 39 (item H2) of the round-1 spec audit.
- rev-2 · 2026-10-23 · §3 · the disposal of the spec audit of units 20 to 23: a hands-off edge to TOOL-dFairHearing-27, naming the four findings it closes on this spec and what it supersedes.

## 10. Reuse audit

The seam is `check_held_out_frozen` in the factory `TOOL-dFairHearing-14` builds, extended in place; the
filtered-hash comparison is the shape `TOOL-aLevelledCopy-1`'s brief already uses for an eol-only row
(`git hash-object` over the working file against the recorded oid). `python
tools/codebase-map/reuse_lookup.py "compare working tree file bytes with the blob at a commit"`
ranked `read_blobs_at` in `tools/memory-tree/tree_lib.py` and `blob_oid` in `tools/govkit/govkit.py`;
neither is importable from the review kit, which carries no memory-tree or deployer dependency, so
the two git calls stay inline. The recall query returned the audit's H2 item, spec 14's S3 and
`TOOL-aLevelledCopy-1`'s hash-object recipe.

Recall terms used: `python tools/memory-recall/query.py "how is a held out benchmark set proven frozen" --terms "held-out frozen freeze commit blob hash-object working tree shallow clone provenance bytes"`
