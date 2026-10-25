# TOOL-dDeclaredLoop-40 — the trailer reader finds the key table through the kit resolver, and reads a floor of keys where none is installed

**Status:** DEFERRED · rev-2 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-agent-ledger.md) | journal | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-16 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 TOOL-dDeclaredLoop-57 TOOL-dDeclaredLoop-58 TOOL-dDeclaredLoop-59 TOOL-dDeclaredLoop-60 TOOL-dDeclaredLoop-61 TOOL-dDeclaredLoop-62 TOOL-dDeclaredLoop-63 TOOL-dDeclaredLoop-64 TOOL-dDeclaredLoop-65 TOOL-dDeclaredLoop-66 TOOL-dDeclaredLoop-67 |
| [2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-36-promoted-fix-return.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-build-TOOL-dDeclaredLoop-40-deviation-401.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-40-deviation-401.md) | deviation | — |
| [2026-10-24-build-TOOL-dDeclaredLoop-40-deviation-402.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-40-deviation-402.md) | deviation | — |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-36-promoted-fix-brief.md) | research | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |
| [2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md](../reviews/2026-10-24-review-TOOL-dDeclaredLoop-36-spec-audit.md) | spec-audit | TOOL-dDeclaredLoop-36 TOOL-dDeclaredLoop-37 TOOL-dDeclaredLoop-38 TOOL-dDeclaredLoop-39 TOOL-dDeclaredLoop-41 TOOL-dDeclaredLoop-42 TOOL-dDeclaredLoop-43 TOOL-dDeclaredLoop-44 TOOL-dDeclaredLoop-45 TOOL-dDeclaredLoop-46 TOOL-dDeclaredLoop-47 TOOL-dDeclaredLoop-48 TOOL-dDeclaredLoop-49 TOOL-dDeclaredLoop-50 TOOL-dDeclaredLoop-51 TOOL-dDeclaredLoop-52 TOOL-dDeclaredLoop-53 TOOL-dDeclaredLoop-54 TOOL-dDeclaredLoop-55 TOOL-dDeclaredLoop-56 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit (`memory/builds/dDeclaredLoop/reviews/2026-10-24-review-TOOL-dDeclaredLoop-1-spec-audit-round1.md`)
confirmed finding **id 47 at HIGH**, its item **H13**, alone in that item. `TOOL-dDeclaredLoop-23` §4
"The trailer table" has `read_commits` refuse any key `tools/playbook/edges.toml` does not register.
That file does not exist at base (`ls tools/playbook/edges.toml` fails, 2026-10-24); it is
PLAY-dOrderedCharter-28's. The copies go into the memory-tree, unattended, loop and runlog kits, none
of which requires playbook, and the spec never says how a copy finds the table at another prefix or
what happens when it is missing. Every re-pointed reader would die with the table, `routed_commits.py`
a merge-bar leg among them. This unit takes the report's fix. It repairs `TOOL-dDeclaredLoop-23`.

## 2. Scope (IN)

- **S1** — The table's location: `read_commits` resolves it with `resolve_kit_dir("playbook",
  "edges.toml", here)`, `here` the copy's own directory, the block carried inline in the canonical and
  every copy under its existing `resolve_kit_dir` parity row, so a receipt-renamed playbook kit is found
  by its receipt row and a default one by the probe. Observed by AC1.
- **S2** — The floor: `FLOOR_KEYS = ("Pass", "Decided", "Gov-Transition", "Gov-Policy")`, the keys a
  shipped consumer of this build reads. When the resolver raises `LookupError`, or the table resolves
  and holds no `[[trailer]]` row, `read_commits` admits the floor keys, refuses any other key by name,
  and writes one line to stderr, `commit_trailers: unregistered-key check skipped: no edges.toml`, once
  per process. Nothing goes to stdout, which the shell consumers read. Observed by AC2, AC3.
- **S3** — Where the table is present it decides, and each floor key must be one of its rows: a floor
  key it lacks is refused by name, so the floor cannot widen what a present table registers.
  Observed by AC4.

## 3. Non-goals (OUT)

- Writing `tools/playbook/edges.toml` or its rows: PLAY-dOrderedCharter-28's table, which
  `TOOL-dDeclaredLoop-23` S2 adds two rows to.
- A copy-install fixture leg that runs every copied reader with each optional sibling absent, the
  finding's left-shift: AC2 and AC3 are that fixture for this reader, and a repository-wide leg is not
  named by any clause of this build.
- The reader's pins and line endings: `TOOL-dDeclaredLoop-39` and `-38`.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-23` — `commit_trailers.py` and `read_commits`, whose unregistered-key refusal this unit makes resolvable and survivable
- **hands-off** `TOOL-dDeclaredLoop-67` — the round-2 minors ids 10 and 60: the floor refuses only a requested key the table lacks, and a malformed table is a named refusal, each a scope item of that unit

## 4. Design

### Evidence

- `resolve_kit_dir` is canonical at `tools/lib/resolve_kit_dir.py` and already inlined under its parity
  row in Python and shell copies (`tools/lib/resolve-python.test.sh:168-183`); it resolves a receipt row
  first, then probes `<here>/<home>/<anchor>` and `<here>/../<home>/<anchor>`, and raises `LookupError`
  naming the places looked (`tools/check-spec-tokens.py:215-240`).
- The four floor keys are the keys `TOOL-dDeclaredLoop-23` §4's consumers and units 2 and 3 pass to
  `read_commits`: `Pass` (routed commits, attribution), `Decided` (runlog), `Gov-Transition`
  (`TOOL-dDeclaredLoop-3` S7) and `Gov-Policy` (`TOOL-dDeclaredLoop-2` S6).

### The read

```
read_commits(repo, revs, keys)
  table = resolve_kit_dir("playbook", "edges.toml", here) / "edges.toml"   # LookupError -> no table
  registered = trailer keys of table          if the table has [[trailer]] rows
             = FLOOR_KEYS, with one stderr note  otherwise
  refuse any requested key not in registered, naming it
  if a table decided: refuse any FLOOR_KEYS member it lacks, naming it     # S3
```

### Files touched (estimate)

- `tools/lib/commit_trailers.py`
- `tools/memory-tree/commit_trailers.py`
- `tools/unattended/commit_trailers.py`
- `tools/loop/commit_trailers.py`
- `tools/runlog/model.py`

### Alternatives rejected

- **A hard-coded `$KIT_DIR/../playbook/edges.toml`.** It breaks for a renamed kit directory, which is
  the case the receipt arm of `resolve_kit_dir` exists for.
- **Giving every copy's kit `requires` `playbook`.** It installs the playbook kit wherever runlog or
  unattended goes, a widened install surface for a check that has a safe floor.
- **Skipping the check entirely where the table is absent.** It would let a consumer read any key, the
  exact property `TOOL-dDeclaredLoop-23` AC6 asserts against.

## 5. Production-readiness checklist

- security — the floor is a closed list, so an absent table never admits an arbitrary key.
- perf / scale — one resolver call per process, its result kept.
- error / empty / loading states — absent table: the floor and one stderr note; present table missing a
  floor key: a named refusal.
- observability — the stderr note names the file not found.
- risks — a consumer reading a fifth key in an adopter without playbook is refused, which names the key
  and is the intended contract.
- testing — AC1 to AC4 as fixture probes; the arm under §7, observed at the close.
- migration — none.
- user docs — none.

## 6. Acceptance criteria

- **AC1** — When a probe builds a scratch tree whose install receipt, `install.json`, homes the playbook kit
  at `scripts/pb/` with an `edges.toml` registering `Pass`, and calls
  `read_commits(repo, "HEAD", keys=("Pass",))` from a copy under `tools/unattended/`, it reads the
  trailer with no stderr note.
  Red when: the copy looks only at `tools/playbook/`, so the renamed kit's table is missed.
  fixture: a scratch git repository under a short `%TEMP%` path; the tree holds none.
- **AC2** — When the same probe runs in a fixture with no `tools/playbook/` and no receipt row for it,
  `read_commits(repo, "HEAD", keys=("Pass",))` returns the planted ids and stderr carries
  `unregistered-key check skipped: no edges.toml` once.
  Red when: the absent table raises, so every re-pointed reader fails in that tree.
- **AC3** — When that fixture asks for `keys=("Gov-Nope",)`, the call refuses naming `Gov-Nope`, and
  the unattended kit's copy, `python commit_trailers.py tokens HEAD`, prints its lines to stdout with the note on
  stderr only.
  Red when: the floor admits any key, or the note reaches stdout and a shell consumer reads it as a
  commit line.
- **AC4** — When a fixture's `edges.toml` registers `Pass` and not `Decided`, a read of `Decided`
  refuses naming it.
  Red when: the floor is unioned with a present table, so the table no longer decides.

## 7. Gates

`routed-commits selftest` · `routed commits name a specced unit` · `python resolver (behaviour + inline parity + idiom ban)` · `runlog selftest` · `pre-push run-log line` · `run-gates run-log line` · `unattended kit gate` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/routed_commits.py · covers AC2 AC3 · the absent-table fixture, staged against `TOOL-dDeclaredLoop-23`'s refusing reader · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-24,
  delegated): `**Derived:** PLAY-dClosedLoop-2`, rung 3, as `TOOL-dDeclaredLoop-36` §8 F1 records.
  widens: none · relaxes: none
- **F2 — Which keys form the floor?** Options: (a) `Pass` and `Decided`, the keys read before this build;
  (b) those and the two keys this build's shipped readers pass, `Gov-Transition` and `Gov-Policy`. (a)
  leaves `TOOL-dDeclaredLoop-3`'s transition reader refusing in every adopter without playbook, the
  same defect one kit over. RESOLVED (agent, 2026-10-24, delegated): (b), rung 3.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, promoted from the round-1 spec audit's id 47 (HIGH, item H13).
- rev-2 · 2026-10-24 · §3 · the Edges block gains the hands-off bullets mirroring the
  consumes-from edges of TOOL-dDeclaredLoop-67, written by the round-2 spec audit's disposal; nothing else moved.

## 10. Reuse audit

The seam is `resolve_kit_dir` (`tools/lib/resolve_kit_dir.py`), carried inline under its existing parity
row, so no new resolver and no new parity row. `python tools/codebase-map/reuse_lookup.py "locate a
sibling kit file and fall back when absent"` ranked `kit_rel`, `resolve_kit_dir` and `kit_dir`;
`resolve_kit_dir` is the one that reads the receipt and refuses rather than guessing.

Recall terms used: edges.toml trailer table resolve_kit_dir sibling kit absent playbook floor keys copy install
