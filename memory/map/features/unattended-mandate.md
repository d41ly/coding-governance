# unattended-mandate — what authorizes a run, and what it was pointed at

```toml
feature = "unattended-mandate"
title = "The unattended run's authorization: the observed anchor and the ask mandate"
status = "building"
streams = ["tooling"]
decisions = ["TOOL-aStandingWrit-2", "TOOL-dNarrowedAnchor-1"]

[claims]
gate-legs = []
kits = []
git-hooks = []
workflow-scripts = []
skill-engines = []
rendered-skills = []
gotcha-classes = []
guides = []
backlog-shards = []
lexicon-verbs = []
[paths]
globs = [
  "tools/unattended/unattended.sh",
  "tools/unattended/check-unattended.sh",
  "tools/unattended/lib-unattended.sh",
  "memory/guides/UNATTENDED-PROTOCOL.md",
  ".unattended.conf",
]
```

Split out of `unattended` when that dossier reached its size cap, so it claims no keys: every key it
touches is claimed there. The split follows a real seam. That dossier is how a run proceeds; this one
is what lets it start and what it was asked to do.

## Constraints & why

**The anchor is an OBSERVATION of the remote, and the kit no longer claims more than that.** Kit 1.0
pinned BASE against `refs/remotes/origin/<default>` and justified it in a source comment claiming the
ref could not move without a push. False — `git update-ref` moves it offline — and it was
reproduced end to end: preflight printed OK over a base the run had authored, the leg agreed silently,
and the push landed. The ref name and tip now come from what the remote advertises for its own HEAD,
and `GOV_DEFAULT_BRANCH` is a cross-check that can only refuse. Both routes are inert, not detected:
neither value is read at all.

**A sha is a NAME, and the dereference is pinned separately.** `git replace` substitutes the object a
sha resolves to and a graft file rewrites the commit graph, both at a perfectly honest anchor, so
neither is closed by any amount of anchor hardening. Every read that turns a sha into bytes or into
ancestry goes through a wrapper pinning `core.useReplaceRefs=false` with `GIT_GRAFT_FILE` pointed
away from the repo. The two suppressions are not interchangeable and only the second stops a graft;
measured, not assumed.

**The boundary is stated rather than implied.** A design panel broke four independent anchor
mechanisms and converged on the reduction that a check under the run's own uid cannot
constitute authorization. The protocol's §9 enumerates what remains reachable — editing the kit,
shimming its tools, skipping the hook layer, relaying through a seeded endpoint, or never creating a
run-state file at all — and names the only control that binds: re-running the same leg in a clone the
run never touched.

**The mandate is a line in the build README, and preflight pins what it read.** An `asks:` line
names the asks a run is pointed at (`TOOL-dDerivedDocket-16`). `check_authorization` reads it out of
the one blob scan it already makes and refuses twice: check 71 when the resolved mode is not `slug`,
because `prompt` and `recipe` resolve at a tip the run pushed itself and could have written the line,
and check 70 when `ASKS_CMD` is blank, because then nothing can say whether an ask is executable.
Preflight asserts P5, that every mandated ask already has its row in its home backlog at `m-base:`,
then runs ONE bounded `ASKS_CMD --tsv --ready <ids> --target <slug> --at <m-base>` reading its stdout
alone, and pins `m-base:`, `asks:` and `asks-ready:` once each. P6 is its own predicate and sits above
`--resume`'s matrix. `--plan --asks` folds the folder's `unit` asks into the roster, `--dispatch`
holds under check 49, and `--rescope` refuses under check 76 an addition whose id is already one of
the build's filed asks of another kind.

**The leg second-opinions the ask mandate from inputs the run cannot move.** `asks:` against the
README at BASE, P5 from the home BACKLOG blob at `m-base:`, and `m-base:` as the merge-base of the
pinned `anchor-sha:` and HEAD at preflight, never `base:`. Check 37 bans a foreign anchor in the
run's folder by the recall kit's own `anchor_at`, reached through `RECALL_CLI`. `asks-ready:` and
the freeze are re-derived by re-running `ASKS_CMD` until the record is published.

## Shared seams

- `ASKS_CMD` — the declared producer of an ask's readiness and disposal. The driver and the leg both
  read it rather than folding status themselves, so the answer has one source.
- `RECALL_CLI` — the memory-recall kit's `anchor_at`, which check 37 reaches to ban a foreign anchor
  in the run's folder. It is reached through the declaration, never required as a sibling kit.

## Reuse affordance

seam: `asks:` — reuse for pointing a run at filed asks rather than a roster it writes itself; extend via `ASKS_CMD`'s `--tsv` columns.

## Gaps

- **The ask-mandate second opinions (`TOOL-dDerivedDocket-18`) have two named holes.** A producer
  that cannot run, breaches the bound or answers in a refused shape is UNANSWERED, so a forged
  `asks-ready:` or freeze behind a broken `ASKS_CMD` passes; and a record already on the advertised
  default tip is never re-derived. Both are in the leg's header. Re-derived 2026-09-21: the two
  check-9 rows this replaced are closed — the leg reads no local ref on the BASE path any more, and
  an unobserved remote fails check 9 closed by name.

- **The mandate is inert in gov until `ASKS_CMD` is declared.** This repo's `.unattended.conf`
  declares none, so an `asks:` line here refuses under check 70, and the one criterion that needs the
  real producer skips with a named skip. `TOOL-dDerivedDocket-35` arms the key.
