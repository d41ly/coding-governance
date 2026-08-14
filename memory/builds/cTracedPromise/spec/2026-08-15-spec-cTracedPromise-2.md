# TOOL-cTracedPromise-2 — an acceptance criterion has to name something a machine can find

**Status:** OPEN · rev-1 · 2026-08-15 · node c · Tier-2 · base 37c05e1b · streams tooling

## 1. Goal

Make `## 6. Acceptance criteria` name concrete artifacts by rule rather than by habit: once a spec's
filename date reaches a new `SPEC_WITNESS_CUTOFF`, every `AC<n>` bullet in it must carry at least one
backticked token. A forward ratchet, so no landed spec is retroactively red.

## 2. Scope (IN)

- **S1** — `SPEC_WITNESS_CUTOFF` declared in `tools/memory-tree/check-memory-hygiene.sh` beside
  `STREAMS_CUTOFF`, blank-defaulting to off, and read from `.memory-tree.conf` by the same loader.
- **S2** — a new branch in check 12's awk body: for a spec whose filename date is on or after the
  cutoff, walk `## 6. Acceptance criteria` and report every bullet matching `**AC<n>**` that contains
  no backtick pair. Reports the bullet labels, not the prose.
- **S3** — the rule applies on BOTH tiers, like the streams ratchet and unlike the section canon. A
  Tier-1 spec that writes acceptance criteria at all is held to the same bar for them.
- **S4** — `SPEC_WITNESS_CUTOFF="2026-08-15"` in `.memory-tree.conf`, set strictly ahead of every
  spec committed before today, with the measurement and the reason in a comment.
- **S5** — the §6 body of `tools/memory-tree/SPEC-TEMPLATE.template.md` states the rule, and the
  rendered `memory/TEMPLATE-SPEC.md` carries it identically.
- **S6** — red and green fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`: a post-cutoff
  spec with a witnessless AC reds and the message names the bullet; the same spec with a backticked
  token passes; a PRE-cutoff spec with the same witnessless AC passes.
- **S7** — `KIT_MEMORY_TREE_VERSION` bumped, because a non-comment line of
  `tools/memory-tree/check-memory-hygiene.sh` moves and `check-verdict-epoch.sh` gates exactly that.
- **S8** — `ARMS_FLOORS` in `.memory-tree.conf` raised for `check-memory-hygiene.sh`, since
  `tools/memory-tree/check-arms.py` counts a new `fail` branch and its arm.

## 3. Non-goals (OUT)

- **Checking that the witness EXISTS.** The gate reads shape: it asserts an AC names something in
  backticks, never that the named file, flag or test is real or that the build satisfied it. Stated
  the way `tools/memory-tree/check-method-carriers.sh` states its own structural bound, because a
  gate that is believed to check more than it does is worse than one nobody trusts.
- **Retrofitting the corpus.** Measured: 140 of 597 AC bullets carry no backtick, across 43 specs.
  Every one is grandfathered by filename date and none is touched.
- **A phrasing rule.** An earlier design required each bullet to open `**AC<n>** — When …`. Measured
  against the corpus it flagged 247 of 597 bullets, and the samples were formatting variance — the
  corpus legitimately writes both `**AC1** — When` and `**AC1** When`. It punished good criteria for
  punctuation and is dropped.
- **Requiring a witness per bullet in the STRONGEST form.** A per-section anchor rule — §6 must name
  one artifact somewhere — was measured at 2 violating specs of 75 and rejected as too weak to be
  worth a ratchet. The per-bullet rule is the one with teeth.
- **A new gate leg.** The rule rides `memory hygiene (20 checks)` and its existing self-test leg. No
  entry is added to `tools/gate-legs.json`, and the check count stays at 20.

## 4. Design

### Data model

No new data. One cutoff string, threaded from `.memory-tree.conf` into check 12's awk invocation as
`-v wcut=`, joining `scut` and `cut10` which are already threaded the same way.

### Inventory

| Item | Where | Change |
|---|---|---|
| `SPEC_WITNESS_CUTOFF` default | `tools/memory-tree/check-memory-hygiene.sh` | new, blank = off |
| `-v wcut=` and the branch | `tools/memory-tree/check-memory-hygiene.sh` | new fail branch inside check 12 |
| `KIT_MEMORY_TREE_VERSION` | `tools/memory-tree/check-memory-hygiene.sh` | bumped |
| `SPEC_WITNESS_CUTOFF`, `ARMS_FLOORS` | `.memory-tree.conf` | new key, floor raised |
| §6 rule text | `tools/memory-tree/SPEC-TEMPLATE.template.md` | states the rule |
| §6 rule text | `memory/TEMPLATE-SPEC.md` | re-rendered, byte-identical |
| three fixtures | `tools/memory-tree/check-memory-hygiene.test.sh` | red, green, grandfathered |

### Where the branch sits

Above the `Tier-1` early exit, beside the streams ratchet, because S3 puts it on both tiers. The
`fdate` it needs is already computed there for exactly that reason.

The scan walks `body[i]` from the `## 6. Acceptance criteria` heading to the next `## ` heading, and
within it treats a line matching `^[ \t]*[-*][ \t]*\*\*AC[0-9]` as a bullet head. A bullet's
continuation lines are indented, so a backtick on a continuation counts toward its own bullet — the
scan therefore accumulates until the next bullet head or the end of the section.

### The failure message

One sentence, then only interpolations. `tools/memory-tree/check-arms.py` reads a positional or an
interleaved literal as part of the signature, and an arm must reproduce the whole thing, so the
message ends its prose before the first variable and puts the bullet list last.

### Alternatives rejected

- **A witness-SHAPED token** — a backticked token additionally matching a path, extension or
  callable pattern. Measured at 218 of 597 bullets, and the samples were false positives on tokens
  like `.map` and `legacy-files.txt`. The added precision was the regex's opinion, not the corpus's.
- **A cutoff earlier than today.** At `2026-08-14` the rule would red 4 bullets in 2 specs that
  landed under no such rule. `STREAMS_CUTOFF` sets the precedent in this very conf: strictly ahead of
  the corpus, with the self-test carrying the arm the corpus cannot.

## 5. Production-readiness checklist

- security — N/A. A read-only text scan inside an existing gate.
- perf / scale — one extra pass over `## 6` per Tier-2 spec, inside an awk already reading the body.
- a11y — N/A. Gate output on a terminal.
- i18n — N/A. Backticks and ASCII labels only.
- error / empty / loading states — a blank `SPEC_WITNESS_CUTOFF` disables the branch; a spec with no
  `## 6` section or no AC bullets is silent rather than red.
- observability — the message names each offending bullet label.
- risks — the shape-not-truth bound is §3 and is stated in `memory/TEMPLATE-SPEC.md` too, so an
  author reads it where they write the criteria.
- testing + left-shift gates — three fixtures in `tools/memory-tree/check-memory-hygiene.test.sh`,
  and `tools/memory-tree/check-arms.py` refuses the branch unless it carries an arm.
- migration / rollback — blank the cutoff in `.memory-tree.conf`. No state, no data migration.
- user docs — the §6 body of `memory/TEMPLATE-SPEC.md`, which is where a spec author already looks.

## 6. Acceptance criteria

- **AC1** — When a spec dated on or after the cutoff carries an AC bullet with no backtick,
  `bash tools/memory-tree/check-memory-hygiene.sh` exits 1 and its output names that bullet's label.
- **AC2** — When that same bullet gains a backticked token, the same command exits 0, with no other
  fixture change.
- **AC3** — When the identical witnessless bullet sits in a spec whose filename date is before the
  cutoff, `bash tools/memory-tree/check-memory-hygiene.sh` is silent about it.
- **AC4** — When `SPEC_WITNESS_CUTOFF` is blank in `.memory-tree.conf`, the branch is inert and the
  red fixture of AC1 passes.
- **AC5** — When `bash tools/memory-tree/check-memory-hygiene.test.sh` runs, every arm passes; when
  the new branch is deleted from the engine, that harness reds.
- **AC6** — When `python tools/memory-tree/check-arms.py` runs, it exits 0 against the raised
  `ARMS_FLOORS` value, proving the new branch carries an arm naming its own failure text.
- **AC7** — When `bash tools/memory-tree/check-verdict-epoch.sh` runs, it exits 0, so the engine
  change and the `KIT_MEMORY_TREE_VERSION` bump landed together.
- **AC8** — When `bash tools/memory-tree/kit-dogfood-parity.test.sh` runs, it exits 0: the rendered
  `memory/TEMPLATE-SPEC.md` still equals the shipped template for this install's prefix.
- **AC9** — When this spec itself is checked, it passes: it is dated on or after the cutoff, so it is
  the first spec its own rule judges.

## 7. Gates

`memory hygiene (20 checks)` · `harness meta-gate (check-arms)` · `verdict epoch` ·
`kit/dogfood doc parity` · `method carriers` · `kit version markers` ·
`codebase-map coverage + freshness`, and the full bar at the push boundary.

## 8. Open questions

- **F1 — both tiers, or Tier-2 only?** RESOLVED (agent, 2026-08-15, delegated): both. A Tier-1 spec
  is exempt from the section canon but not from meaning what it writes, and the streams ratchet
  already sets that precedent in the same block.
- **F2 — is a bare backtick pair enough?** It admits `` `it` ``. RESOLVED (agent, 2026-08-15,
  delegated): yes, and §3 says so. Every stronger predicate measured worse on this corpus, and a
  gate whose false positives teach authors to work around it is worse than a weak one they respect.
- **F3 — should the cutoff be today or the next working day?** RESOLVED (agent, 2026-08-15,
  delegated): today, `2026-08-15`. It is strictly ahead of every committed spec, and it makes this
  spec the rule's first live subject rather than leaving the population empty.

## 9. Revision log

- rev-1 · 2026-08-15 · initial draft, written against the three predicates measured over 597 AC
  bullets and the 43 specs that would have been retrofitted.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "spec acceptance criteria gate"` and a read of
`tools/memory-tree/check-memory-hygiene.sh` put the seam inside check 12's existing awk body, beside
the `STREAMS_CUTOFF` ratchet: it already computes `fdate`, already receives its cutoff through
`-v`, already walks `body[i]`, and already runs on both tiers. No new file, no new selector, no new
population walk. A separate gate script was rejected for the same reason the streams ratchet is not
one — it would re-derive the spec population that check 12 already holds.
