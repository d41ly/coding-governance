# TOOL-aNimbleMend-1 — two policy keys, default on, and the ask each mechanism makes before it acts

**Status:** CLOSED · rev-1 · 2026-11-12 · node a · Tier-2 · base 97e0841d · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-brief.md) | research | TOOL-aNimbleMend-2 TOOL-aNimbleMend-3 TOOL-aNimbleMend-4 TOOL-aNimbleMend-5 TOOL-aNimbleMend-6 TOOL-aNimbleMend-7 TOOL-aNimbleMend-8 TOOL-aNimbleMend-9 TOOL-aNimbleMend-10 TOOL-aNimbleMend-11 TOOL-aNimbleMend-12 |
| [2026-11-12-prompt-TOOL-aNimbleMend-1-build-brief.md](../prompts/2026-11-12-prompt-TOOL-aNimbleMend-1-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Two catalogue keys switch this build's two mechanisms, each defaulting on, so an adopter turns the
inline red-fix lane or the pass legs off with one line of `.governance/policy.toml`. One written
contract says how a mechanism asks its key and what each answer means, so every later unit of this
build reads a switch the same way instead of deciding it again.

## 2. Scope (IN)

- **S1** — Two `[[key]]` rows in `tools/policy/catalogue.toml`, `bar.inline-red-fixes` and
  `pass.fast-legs`, each `allowed = ["on", "off"]`, `default = "on"`, `owner = "aNimbleMend"`, with
  `summary` and `usage`. Observed by AC1, AC2, AC3, AC4 and AC5.
- **S2** — The ask contract, one section of `tools/policy/README.md` headed
  `## A default-on switch`, holding §4's outcome table and the three call shapes. Observed by AC8.
- **S3** — `.governance/policy.json` re-rendered in a second commit after the catalogue commit, as
  §4's Rollout states. Observed by AC6 and AC7.

## 3. Non-goals (OUT)

- A new reader. The policy kit's two readers answer both keys as they stand, and §4's Alternatives
  rejected says why a third is not built.
- Any call that asks a key. Each asker writes its own literal call in its own unit, at the seam its
  language already has.
- The rule for which revision a build's own branch reads. The reader's landed-revision rule is
  unchanged, and §5 names its consequence.
- `help/policy.md`'s list of keys that have a consumer, and the two mechanisms' help pages.
- A conf key for either switch. `tools/policy/policy.py#check_legacy_homes` refuses a new legacy
  home, and an adopter with no policy kit has both mechanisms on.
- A reader of `verdict.red-route`, which stays dWitnessedBar's and is neither read nor changed.
- A kit version bump. The lander's `mint` moves every version once, after the last unit.

### Edges

- **hands-off** `TOOL-aNimbleMend-5` — the pass-leg adapter asks the pass-leg key under §4's contract before it starts a leg, and it is the one asker of that key: the hooks and the run point follow its answer
- **hands-off** `TOOL-aNimbleMend-7` — the run-point instruction names the pass-leg key as the switch the adapter asks
- **hands-off** `TOOL-aNimbleMend-8` — the write gate and the commit graders ask the lane key under §4's contract before they admit a write that names a red
- **hands-off** `TOOL-aNimbleMend-11` — the policy help page gains the two keys beside their consumers, and each mechanism's page names its key
- **hands-off** `TOOL-aNimbleMend-12` — observes each mechanism with its key off, in a fixture whose default branch carries the policy file
- **hands-off** external — the build's close: the policy kit's reader-coverage arm grades both keys for a reader once every spec of this build is terminal at the landed revision, so a key no unit asks by then is that arm's finding

## 4. Design

### The two keys

| Key | `allowed` | Default | `off` means |
|---|---|---|---|
| `bar.inline-red-fixes` | `["on", "off"]` | `on` | no lane: every product write needs its specced unit, as before this build |
| `pass.fast-legs` | `["on", "off"]` | `on` | no pass legs: a unit pass runs no gate leg, as before this build |

```toml
# TOOL-aNimbleMend-1: the two switches of the aNimbleMend mechanisms, each default on. They are no
# row of the design's [policies] table, so the header's order does not place them.
[[key]]
name = "bar.inline-red-fixes"
allowed = ["on", "off"]
default = "on"
summary = "Whether a red bar leg or pass leg may be fixed with no spec, its record written after: on, or off, every product write then needing its specced unit."
usage = 'bar.inline-red-fixes = "off"'
owner = "aNimbleMend"

[[key]]
name = "pass.fast-legs"
allowed = ["on", "off"]
default = "on"
summary = "Whether the declared fast gate legs run after every unit pass: on, or off, a pass then running no gate leg."
usage = 'pass.fast-legs = "off"'
owner = "aNimbleMend"
```

**Names.** The owner's prompt offers `bar.inline_red_fixes` and `pass.fast_legs`. The catalogue's
name grammar admits `[A-Za-z0-9_-]+` per segment (`tools/policy/README.md`, "A catalogue row"), and
no row at base spells an underscore in its name, so the two names are the owner's with hyphens:
`grep -c '^name = ".*_' tools/policy/catalogue.toml` prints 0. The lexicon declares no cell for a policy key:
`python tools/lexicon/lexicon.py --suggest pass.fast-legs --as toml.key` answers
`unknown surface 'key'`, its closed set being function, type, file and constant. The grader is
therefore `tools/policy/check_policy.py#arm_shape` alone. No placeholder row matches either name:
no row at base opens with a `bar` or a `pass` segment, and no row is two placeholder segments.

**Values.** `on` and `off` are the words the owner's prompt and the build README use for the
switches, and `build.reuse-check.second-pass` already carries that pair. A row needs no `direction`:
neither is a loop bound or a deadline (`tools/policy/policy.py#derive_bounds`).

**Placement.** The rows sit after the `review.spec-audit.chain-ceiling` row, beside the other three
rows that are no row of the design's table, under the comment above. Each row carries `summary` and
`usage`, so `tools/policy/unsummarised-keys.txt` does not grow. The policy file sets a key as
`[bar]` then `inline-red-fixes = "off"`, or `[pass]` then `fast-legs = "off"`.

**Defaults and presets.** A key the file does not set reads its row's `default` through
`tools/policy/policy.py#read_default_value`, with source `default`. That step names any `preset`
the file sets in its reason and applies none: no step of `RESOLUTION_ORDER` applies a preset until
dKeptSession adds one. So `on` holds under every preset today, and `get --explain` prints the
source and the reason.

### The ask contract

A mechanism asks its key once, immediately before the act the key switches, and never at load.

| The reader's answer | What the mechanism does |
|---|---|
| `on` | acts |
| `off` | is absent: it does what the tree did before this build, and prints nothing new |
| no policy kit resolves beside the asker | acts, and prints one NOTE line on stderr naming the key and `on` |
| the reader refuses, exit 2 or a `PolicyRefusal` | is absent, and prints the reader's own refusal line |
| any other value | is absent, and prints one line naming the key and the value |

The third row is the owner's "on by default in every repository": the catalogue is the policy
kit's, so a repository without that kit has no switch and keeps both mechanisms. The fourth and
fifth rows fail to the earlier behaviour, because the lane loosens the write gate and a switch that
cannot be read must not loosen anything. `read_spec_audit_switch` in
`tools/unattended/unattended.sh` is the precedent for all three rows.

The call shapes, one per language, each passing the key as a literal so
`tools/policy/check_policy.py#scan_reader_keys` counts it:

| Asker | Call | Policy kit found by |
|---|---|---|
| shell | `"$py" "$d/policy.py" get pass.fast-legs` | the kit's inline `resolve_kit_dir` |
| Python | a call whose first argument is the key literal, running `policy.py get` as a subprocess | the kit's inline `resolve_kit_dir` |
| JavaScript hook | `readPolicy('pass.fast-legs', { repo })` from `policy-mirror.js` | `resolveKitDir`, as `tools/hooks/agent-cap.js#resolvePolicyHelper` does |

A key passed through a variable reads as unread to the coverage arm. `tools/policy/README.md`,
"The mirror", already rules that Python and shell consumers call the reader and never the mirror.

**The revision read.** With no `--rev`, both readers read the landed revision, the remote default
branch or the local one where no remote exists (`tools/policy/README.md`, "The reader"). A run
therefore cannot flip its own switch on its branch. The catalogue is read from the kit's working
copy, so on this build's branch both keys answer `on` as soon as S1 is committed.

### Rollout

On by default from the commit that lands S1, and inert until an asker lands: nothing reads either
key in this unit.

The pass makes two commits. `policy.py mirror --write` refuses while an input the mirror records
differs from its blob at HEAD, and `tools/policy/guard.py` refuses a mirror staged beside a changed
input, so the catalogue commits first and the mirror renders what that commit holds.

| Commit | Holds | Trailer |
|---|---|---|
| first | `tools/policy/catalogue.toml`, `tools/policy/README.md` | `Pass: TOOL-aNimbleMend-1` |
| second | `.governance/policy.json`, and the unit's records | `Pass: TOOL-aNimbleMend-1` |

`TOOL-dFoldedAudit-7` landed its three rows the same way. The bar's preflight runs
`policy.py mirror --check`, so a branch that skips the second commit is refused at the close.

### Inventory

| Minted | Cell | Graded by |
|---|---|---|
| `bar.inline-red-fixes` | a catalogue `name`; the lexicon declares no cell for one | `arm_shape` |
| `pass.fast-legs` | a catalogue `name`; the lexicon declares no cell for one | `arm_shape` |

### Files touched (estimate)

`tools/policy/catalogue.toml`
`tools/policy/README.md`
`.governance/policy.json`

### Alternatives rejected

- **One new reader every asker calls.** The askers sit in four kits and three languages, and a kit
  imports no sibling: `tools/memory-tree/build_records.py` and `tools/playbook/policy_value.py`
  each carry `resolve_kit_dir` inline for that reason. A shared reader would cost each asker the
  same resolver call the policy kit's own reader costs, and would add a kit edge. A hook cannot
  call a Python reader cheaply either: `policy-mirror.js` exists because a hook reads the mirror.
- **A reader function per asker kit, built here.** Four files in three kits is four mechanisms'
  write sets in one unit, and each file is another unit's to change.
- **Conf keys.** `.unattended.conf` is a legacy home and its list is shrink-only.
- **Descriptive values, `inline` and `specced`.** The owner and every sibling brief say on and off,
  and a second vocabulary for one switch is two facts.
- **One key for both mechanisms.** The owner asks for either to be turned off alone.

## 5. Production-readiness checklist

- **security** — `bar.inline-red-fixes` loosens the write gate when on, which is the owner's ask.
  The contract fails closed: a refused read, or a value outside the pair, leaves the lane absent.
  The reader takes the landed revision, so a run cannot open a lane the owner closed. The policy
  file is on `tools/policy/guarded-paths.txt`.
- **perf / scale** — Nothing here runs on a hot path. The contract's "once, before the act" keeps a
  hook from spawning a reader on every tool call.
- **error / empty / loading states** — The contract's five rows. An absent policy file reads the
  default.
- **observability** — `get --explain` names the source and the revision. The absent-kit answer
  prints a NOTE, and both absent answers print the cause.
- **risks** — A key set to `off` on a branch has no effect until it lands, because the reader takes
  the landed revision. `TOOL-aNimbleMend-12` therefore commits the policy file on its fixture's
  default branch. After this build lands, a key no asker reads reds reader coverage, which the
  Edges line hands to the close.
- **testing** — Direct probes of the two readers in this tree and in one scratch repository. No new
  arm: `arm_shape`, `arm_schema` and the mirror arms already grade any row.
- **migration** — Additive. An unset key reads `on`, and no shrink-only list grows.
- **user docs** — `help/policy.md` and the mechanism pages are `TOOL-aNimbleMend-11`'s. Until an
  asker lands the page's sentence "every other key has no consumer yet" stays true of both keys.

## 6. Acceptance criteria

Fixture K is a scratch git repository under `%TEMP%` with a short name, on branch `main`, with no
remote, so `policy.py get` reads the local `main`. It holds copies of `tools/policy/policy.py`,
`tools/policy/budgets.py` and `tools/policy/catalogue.toml` at those paths, committed.

- **AC1** — When `python tools/policy/policy.py get bar.inline-red-fixes` and
  `python tools/policy/policy.py get pass.fast-legs` run in this repository, each prints `on` and
  exits 0.
  Red when: a row is absent, which exits 2 naming `is not a catalogue key`, or a default is `off`.
- **AC2** — When `python tools/policy/policy.py get pass.fast-legs --explain` runs in this
  repository, stderr carries `policy: pass.fast-legs · default ·`.
  Red when: the row carries a derived default, which refuses naming
  `a derived default no reader computes yet` and prints no `default` source.
- **AC3** — When K commits `.governance/policy.toml` setting `inline-red-fixes = "off"` under
  `[bar]` and `fast-legs = "off"` under `[pass]`, `python tools/policy/policy.py get` prints `off`
  for each key in K.
  Red when: a row's `allowed` lacks `off`, which exits 2 with a `policy: refused` line.
- **AC4** — When K's first commit instead sets `fast-legs = "sometimes"`,
  `python tools/policy/policy.py get pass.fast-legs` exits 2 in K and prints a `policy: refused`
  line naming `.governance/policy.toml`, with nothing on stdout.
  Red when: the row's `allowed` is a typed range that admits any word.
- **AC5** — When `python tools/policy/policy.py lists --check` runs in this repository it exits 0,
  and `grep -c -e 'bar.inline-red-fixes' -e 'pass.fast-legs' tools/policy/unsummarised-keys.txt`
  prints 0.
  Red when: a new row lacks `summary` or `usage`, which names the row as one the list lacks.
- **AC6** — When `python tools/policy/policy.py mirror --check` runs after
  `policy.py mirror --write` over the first commit, it prints `policy: mirror fresh`, and
  `grep -c -e '"bar.inline-red-fixes"' -e '"pass.fast-legs"' .governance/policy.json` prints 2.
  Red when: the mirror is not re-rendered, which prints `mirror stale`.
- **AC7** — When `node tools/policy/policy-mirror.js get pass.fast-legs` runs in this repository
  after the first commit, it prints `on` and exits 0.
  Red when: the row is absent, which exits 2 with the reader's refusal line.
  fixture: on this branch the mirror at the landed revision does not hold the key, so the helper
  answers through `policy-shim.sh get`; after the landing it answers from the mirror.
- **AC8** — When `grep -c -e 'bar.inline-red-fixes' -e 'pass.fast-legs' tools/policy/README.md`
  runs it prints 2 or more, and `grep -c '^## A default-on switch$' tools/policy/README.md`
  prints 1.
  Red when: the contract is written only in this spec, which prints 0 for the heading.

## 7. Gates

`policy check` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No arm is added or moved. The rows are graded by arms that already grade every catalogue row, and
the contract's rows are observed where each asker lands.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-12 · initial draft.

## 10. Reuse audit

The seam is the policy kit's two readers as they stand: `tools/policy/policy.py#resolve` behind
`policy.py get`, and `readPolicy` in `tools/policy/policy-mirror.js`. `reuse_lookup.py` named
`read_policy_value`, in `tools/playbook/policy_value.py` and `tools/govkit/govkit.py`, as the
candidate for this behaviour, and it is a per-kit caller of `policy.py get` and not a shared reader.
For one reader every asker calls, no existing seam fits, and the evidence is that every consumer at
base reads the policy kit directly through its own inline resolver: `read_spec_audit_switch` in
`tools/unattended/unattended.sh`, `resolvePolicyHelper` in `tools/hooks/agent-cap.js`, and the
`charter.override` read in `tools/memory-tree/build_records.py`. Recall returned
`TOOL-dFoldedAudit-7` as the precedent for rows outside the design's table, and
`DEPL-dShippedRelease-26` and `DEPL-dShippedRelease-7` for the absent-kit answer with a notice.

Where the records and the source disagreed: the build README's roster says this unit carries "the
reader each mechanism asks", and the source holds that reader already, so this unit writes the
contract for asking it and no reader.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "read a policy switch that defaults on before a mechanism acts"`.
Recall terms used: `python tools/memory-recall/query.py "how does a mechanism read a policy switch that defaults on, and what does it do when no policy kit resolves" --terms "policy.py get catalogue row default reader coverage mirror readPolicy resolve_kit_dir switch kit absent"`.
