# TOOL-dWitnessedBar-52 — the scalar-pin seed reads every root conf the working tree holds, so a fresh install seeds its pin before its first commit

**Status:** OPEN · rev-1 · 2026-10-25 · node d · Tier-2 · base cdfbd1cf · streams tooling · order 11 · advances TOOL-dWitnessedBar-31

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dWitnessedBar-1-agent-ledger.md) | journal | TOOL-dWitnessedBar-1 TOOL-dWitnessedBar-2 TOOL-dWitnessedBar-3 TOOL-dWitnessedBar-4 TOOL-dWitnessedBar-5 TOOL-dWitnessedBar-6 TOOL-dWitnessedBar-7 TOOL-dWitnessedBar-8 TOOL-dWitnessedBar-9 TOOL-dWitnessedBar-10 TOOL-dWitnessedBar-11 TOOL-dWitnessedBar-12 TOOL-dWitnessedBar-13 TOOL-dWitnessedBar-14 TOOL-dWitnessedBar-15 TOOL-dWitnessedBar-16 TOOL-dWitnessedBar-17 TOOL-dWitnessedBar-18 TOOL-dWitnessedBar-19 TOOL-dWitnessedBar-20 TOOL-dWitnessedBar-21 TOOL-dWitnessedBar-22 TOOL-dWitnessedBar-23 TOOL-dWitnessedBar-24 TOOL-dWitnessedBar-25 TOOL-dWitnessedBar-26 TOOL-dWitnessedBar-27 TOOL-dWitnessedBar-28 TOOL-dWitnessedBar-29 TOOL-dWitnessedBar-30 TOOL-dWitnessedBar-40 TOOL-dWitnessedBar-41 TOOL-dWitnessedBar-42 TOOL-dWitnessedBar-43 TOOL-dWitnessedBar-44 TOOL-dWitnessedBar-45 TOOL-dWitnessedBar-46 TOOL-dWitnessedBar-47 TOOL-dWitnessedBar-48 TOOL-dWitnessedBar-49 TOOL-dWitnessedBar-50 TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-54 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md](../build/2026-10-25-build-TOOL-dWitnessedBar-52-round2-fix-return.md) | research | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-1-spec-writer.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-1-spec-writer.md) | journal | TOOL-dWitnessedBar-1 |
| [2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dWitnessedBar-52-round2-fix-brief.md) | research | TOOL-dWitnessedBar-51 TOOL-dWitnessedBar-53 TOOL-dWitnessedBar-55 TOOL-dWitnessedBar-56 TOOL-dWitnessedBar-57 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of units 40 to 51
(`memory/builds/dWitnessedBar/reviews/2026-10-25-review-TOOL-dWitnessedBar-40-spec-audit-round1.md`)
confirmed finding **id 1 at HIGH**, in its item **H1**, which it shares with id 13
(`TOOL-dWitnessedBar-53`). `TOOL-dWitnessedBar-46` S2 has the memory-tree adopter seed
`conf-scalar-pins` right after it scaffolds, measuring "the tree's tracked root confs". At that moment
`.memory-tree.conf` has just been copied from the example (`tools/memory-tree/adopt-memory-tree.sh:97-98`)
and is untracked: the scaffold stages only `git add "$M"` (`:688`, `:690`), and `:694` tells the user to
commit the conf later. The seed writes an armed, empty population; being absent-only it never runs
again; once the conf is committed, `ratchet (keys, not a scalar)` reds on the example's
`ROW_DUPLICATE_PIN="0"`, the defect unit 46 exists to close. This unit takes the report's fix: the seed
reads the root confs present in the working tree, tracked or not. It repairs `TOOL-dWitnessedBar-46`.

## 2. Scope (IN)

- **S1** — One conf set. `tools/memory-tree/ratchet.py` reads the root confs through one function,
  `root_confs(root)`: the files `git ls-files --cached --others --exclude-standard -- ':(glob).*.conf'`
  lists, run at the repository root. A conf copied but not yet committed is read, and a conf the
  repository ignores is not. `keys-not-scalar --measure`, the seed of unit 46 S2, calls it.
  Observed by AC1 and AC2.
- **S2** — The leg reads the same set. `keys-not-scalar` without `--measure`, the check of
  `TOOL-dWitnessedBar-14` S11, calls `root_confs` too, so the seed and the leg never measure two
  different sets. Observed by AC1 and AC3.
- **S3** — What it does not check, stated. `ratchet.py`'s docstring for `root_confs` names the blind
  spot: a root conf the repository ignores is never measured, so a pin assigned only in a machine-local
  ignored conf is neither seeded nor held. Observed by AC2.

## 3. Non-goals (OUT)

- The seed verb, its state table and its absent-only rule: `TOOL-dWitnessedBar-15`'s.
- The adopter's seed call, the population's home and check 3's named list: `TOOL-dWitnessedBar-46`'s.
- The suite arm that runs every seeding population in an uncommitted scaffold, the report's
  left-shift: `TOOL-dWitnessedBar-53`, id 13's unit.
- An armed population with zero rows that misses a pin: the minors batch's id 44 item
  (`TOOL-dWitnessedBar-57`).

### Edges

- **consumes-from** `TOOL-dWitnessedBar-46` — `keys-not-scalar --measure` and the adopter's seed of `conf-scalar-pins`, whose conf read this unit widens to the working tree
- **consumes-from** `TOOL-dWitnessedBar-14` — `ratchet.py keys-not-scalar`, the leg whose conf read S2 binds to the seed's
- **hands-off** `TOOL-dWitnessedBar-53` — `root_confs`, whose behaviour across a target's first commit unit 53's suite arm observes for every population the scaffold seeds

## 4. Design

### Evidence

- `cp "$HERE/.memory-tree.conf.example" "$ROOT/.memory-tree.conf"` with no `git add`
  (`tools/memory-tree/adopt-memory-tree.sh:97-98`); the scaffold's only stagings are `git add "$M"`
  (`:688`, `:690`); its next-step line is `git add $M/ .memory-tree.conf && commit` (`:694`).
- The adopter met this class once already: the `method-carriers.txt` seed reads
  `{ git ls-files; find . -type f ... }` because "`git ls-files` is EMPTY here and a tracked-only seed
  writes a header and nothing else" (`:645-650`).
- The example conf assigns `ROW_DUPLICATE_PIN="0"` (`tools/memory-tree/.memory-tree.conf.example:283`).
- Unit 15 §4: a live result with zero rows is written armed and empty, and a present armed home is
  left alone on a rerun.

### The read

```
root_confs(root) := git -C <root> ls-files --cached --others --exclude-standard -- ':(glob).*.conf'
                    (glob magic: `*` never crosses `/`, so only root-level files match)
keys-not-scalar --measure  -> one row per scalar *_PIN= assignment over root_confs(root)
keys-not-scalar            -> unheld pins over root_confs(root), against conf-scalar-pins
```

`--exclude-standard` rather than a raw directory listing keeps an ignored local conf out, which a
committed tree never holds either; so the set read before the first commit equals the set read after
it whenever the user commits what the scaffold told them to.

### Inventory

Minted: the function `root_confs`. Naming cells: asked of `python tools/lexicon/lexicon.py --suggest
root_confs --as py.function` at the pass.

### Migration

None for gov: every root conf of gov's tree is tracked, so the set is the tracked set.

### Rollout

Live at landing, one step after `TOOL-dWitnessedBar-46`.

### Files touched (estimate)

- `tools/memory-tree/ratchet.py`

### Alternatives rejected

- **Seed after the first commit.** The adopter never commits, by design
  (`tools/memory-tree/adopt-memory-tree.sh:694`), so the seed would move
  to a step nobody runs and the population would start unarmed.
- **Seed from the conf the adopter has just written.** It names one file where the leg reads every root
  conf; the two sets would differ on the first adopter carrying a second conf.
- **A raw directory listing.** It reads an ignored machine-local conf that no commit will ever carry.

## 5. Production-readiness checklist

- security — reads files git already lists; writes nothing new.
- perf / scale — one `git ls-files` per run, as before.
- error / empty / loading states — no root conf: no rows, an armed empty population, as unit 15 states.
- observability — the leg prints the confs it read.
- risks — an ignored conf's pin is invisible; S3 states it.
- testing — AC1 to AC3 by fixture and plant; the arm of §7 at the close.
- migration — none.
- user docs — none under `help/`; the docstring states the set.

## 6. Acceptance criteria

- **AC1** — When `adopt-memory-tree.sh --scaffold` runs in a scratch target whose `.memory-tree.conf` is
  the example, copied and untracked, `python ratchet.py keys-not-scalar` there exits 0 naming one row,
  `.memory-tree.conf` and `ROW_DUPLICATE_PIN`; after `git add -A && git commit` it exits 0 naming the same
  row.
  Red when: the measure reads tracked confs only, so the seed arms empty and the leg reds once the conf
  is committed.
  fixture: a scratch `git init` target under `%TEMP%/<short-name>` holding a copy of the kit; the tree
  holds none.
- **AC2** — When `python ratchet.py --fixture --plant untracked-conf` runs in `tools/memory-tree/`, an
  untracked root `.x.conf` assigning `FOO_PIN="3"` appears in `keys-not-scalar --measure`'s output; under
  `--plant ignored-conf`, the same conf named in `.git/info/exclude` does not; and
  `grep -n 'def root_confs' ratchet.py` names the function whose docstring states the ignored-conf
  blind spot.
  Red when: an untracked conf is unread, or an ignored conf is measured.
- **AC3** — When `grep -c 'root_confs(' ratchet.py` runs in `tools/memory-tree/`, it prints at least 3,
  the definition and the two readers, and `--plant untracked-conf` with no population row for `FOO_PIN`
  makes `keys-not-scalar` exit 1 naming it.
  Red when: the leg keeps its own conf list, so the seed and the leg read two sets.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit/dogfood doc parity`

`ratchet selftest`, which `TOOL-dWitnessedBar-14` adds to the manifest, runs the plants of AC2 and AC3
once it exists; it is named here in prose because the leg join reads only legs the manifest holds today.

New arm: tools/memory-tree/ratchet.py · covers AC2 AC3 · the plants `untracked-conf` and `ignored-conf`, staged red by dropping `--others` from `root_confs` · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** The carries join reds a chain
  spec carrying nothing and derived from nothing. Options: (a) `**Derived:**` naming
  `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of `TOOL-dWitnessedBar-46`'s clause. Unit 46 carries
  none, being itself derived, so (b) has nothing to split; veto 1 discards it. RESOLVED (agent,
  2026-10-25, delegated): (a), rung 3, the precedent `TOOL-dDeclaredLoop-36` §8 F1 set.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit of units 40 to 51, id 1
  (HIGH, item H1, shared with id 13).

## 10. Reuse audit

The seam is the adopter's own working-tree fallback for the `method-carriers.txt` seed
(`tools/memory-tree/adopt-memory-tree.sh:645-650`), the one place this repo already met the
tracked-only-seed class, expressed as one `git ls-files` call with `--others --exclude-standard` so the
leg and the seed share it. `python tools/codebase-map/reuse_lookup.py "seed measure untracked root conf
before first commit"` ranked `before`, `seed` (test helpers), `load_conf` and `repo_root`; none lists a
working tree's root confs, so no existing seam fits beyond the adopter's fallback.

Recall terms used: `python tools/memory-recall/query.py "why does an adopter seed read the working tree at scaffold time" --terms "method-carriers seed git ls-files empty scaffold untracked conf vacuous-selector-empty-population adopter first commit"`
