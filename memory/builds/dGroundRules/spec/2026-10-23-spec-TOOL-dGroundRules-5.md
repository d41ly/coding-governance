# TOOL-dGroundRules-5 — the JSON mirror, regenerated at each landing and read from the landed blob

**Status:** CLOSED · rev-5 · 2026-10-24 · node d · Tier-2 · base 3708a705 · streams tooling · order 3 · advances TOOL-dGroundRules-12

**Carries:** cl-dClosedLoop-0011@8312590d whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dGroundRules-5-deviation-53.md](../build/2026-10-23-build-TOOL-dGroundRules-5-deviation-53.md) | deviation | — |
| [2026-10-23-build-TOOL-dGroundRules-5-ledger.md](../build/2026-10-23-build-TOOL-dGroundRules-5-ledger.md) | journal | — |
| [2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-1-spec-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 |
| [2026-10-23-prompt-TOOL-dGroundRules-5-build-brief.md](../prompts/2026-10-23-prompt-TOOL-dGroundRules-5-build-brief.md) | journal | — |
| [2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md](../prompts/2026-10-25-prompt-TOOL-dGroundRules-1-close-arms-brief.md) | research | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 |
| [2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-11-spec-audit-round1.md) | spec-audit | TOOL-dGroundRules-1 TOOL-dGroundRules-11 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-10 TOOL-dGroundRules-9 |
| [2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md](../reviews/2026-10-23-review-TOOL-dGroundRules-1-52-closing-diff-round1.md) | diff-review | TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-65 TOOL-dGroundRules-14 TOOL-dGroundRules-15 TOOL-dGroundRules-16 TOOL-dGroundRules-17 TOOL-dGroundRules-18 TOOL-dGroundRules-19 TOOL-dGroundRules-20 TOOL-dGroundRules-21 TOOL-dGroundRules-22 TOOL-dGroundRules-23 TOOL-dGroundRules-24 TOOL-dGroundRules-25 TOOL-dGroundRules-26 TOOL-dGroundRules-27 TOOL-dGroundRules-28 TOOL-dGroundRules-29 TOOL-dGroundRules-30 TOOL-dGroundRules-31 TOOL-dGroundRules-32 TOOL-dGroundRules-33 TOOL-dGroundRules-34 TOOL-dGroundRules-35 TOOL-dGroundRules-36 TOOL-dGroundRules-37 TOOL-dGroundRules-38 TOOL-dGroundRules-39 TOOL-dGroundRules-40 TOOL-dGroundRules-41 TOOL-dGroundRules-42 TOOL-dGroundRules-43 TOOL-dGroundRules-44 TOOL-dGroundRules-45 TOOL-dGroundRules-46 TOOL-dGroundRules-47 TOOL-dGroundRules-48 TOOL-dGroundRules-49 TOOL-dGroundRules-50 TOOL-dGroundRules-51 TOOL-dGroundRules-52 |

<!-- /gen:spec-records -->

## 1. Goal

The hooks are JavaScript and cannot parse TOML, so they read policy through a JSON mirror,
`.governance/policy.json`. Nothing yet says when the mirror is regenerated, what pins it to the policy
it mirrors, or what a hook does when it is absent or stale, and a hook reading a hand-edited mirror in
the working tree would enforce whatever the edit says (the design audit's M11 and FM1). This unit
renders the mirror from the reader, regenerates it at every landing, reads it only from the landed
revision's blob and only while its hashes match the TOML there, and reads a stale or absent mirror
as `policy-file.on-invalid` says.

## 2. Scope (IN)

- **S1** — `render_mirror(repo, rev="HEAD")` in `tools/policy/policy.py` returns the mirror's bytes
  for one revision: the git blob ids of `.governance/policy.toml` and of the catalogue at that
  revision, and the `Resolution` of every key §4 lists, read through the reader's own resolution.
  Observed by AC1, AC3.
- **S2** — The verb `python tools/policy/policy.py mirror --write | --check`, `cmd_mirror`. `--write`
  writes `.governance/policy.json`; `--check` compares it with the render and exits 1 naming the
  first difference, so a hand-edited mirror is red. Both refuse when the policy file or the catalogue
  in the working tree differs from its blob at HEAD. Observed by AC1, AC2, AC3.
- **S3** — The landing regeneration: a `[[generated]]` row in `tools/policy/kit.toml` whose `write`
  and `check` are S2's verbs, so the run-gates kit's `regen.py --write` renders the mirror into every
  landing `tools/push-main.sh` makes, and the bar's preflight runs its `--check`. Observed by AC4.
- **S4** — The parity arm `arm_mirror_parity` in `tools/policy/check_policy.py`, run by the policy
  leg `TOOL-dGroundRules-1` declares over the real tree, red on a hand-edited or absent mirror, with
  the fixture cases `mirror-hand-edited` and `mirror-absent`. Observed by AC2.
- **S5** — The one mirror reader, `tools/policy/policy-mirror.js`: `readPolicy(key, { repo })` and a
  `get` CLI. It reads the mirror from the landed revision's blob, never from the working tree, and
  takes a key from it only while both recorded blob ids equal the blobs at that revision. A stale or
  absent mirror is read as `policy-file.on-invalid` says: under `last-valid` through the TOML reader,
  under `refuse` as a refusal naming the mirror. A key a fresh mirror does not hold is read through
  the TOML reader. Observed by AC5, AC6, AC7.
- **S6** — `tools/policy/policy-shim.sh`, the helper's shell half: the landed revision, found by the
  canonical remote ladder carried inline, and the TOML reader run under the canonical Python resolver
  carried inline. Both blocks are byte-identical to their canonicals. Observed by AC8, AC9.
- **S7** — `--json` on the reader's `get` verb: one JSON object holding the `Resolution`'s three
  fields, the refusal unchanged. It is the form the helper reads through the shim. Observed by AC10.
- **S8** — The hook arm `arm_mirror_landed` with its outcome cases: a fixture hook that enforces the
  landed limit while the working-tree mirror carries a loosened one, a stale mirror under each value
  of `policy-file.on-invalid`, an absent mirror, and the helper's landed revision against the
  reader's. Observed by AC5, AC6, AC7, AC9.
- **S9** — The class arm `arm_mirror_readers`: no tracked code file outside `tools/policy/` names
  the mirror's path, so every consumer reads it through the helper. Observed by AC11.
- **S10** — `.governance/policy.json` itself, rendered at the build commit, and its line in
  `.gitattributes` pinning it to LF, because the parity arm compares bytes. Observed by AC1, AC12.

## 3. Non-goals (OUT)

- Re-pointing any hook to the helper. `tools/hooks/agent-cap.js` reads `runtime.agents-in-flight`
  through it in `TOOL-dGroundRules-10`; at this build no tracked hook reads the mirror.
- A mirror reader for Python or shell consumers. They call the reader, which is cheaper than the
  mirror for them and is the source the mirror is checked against.
- Refusing agent writes to the mirror: the minimal guard's, `TOOL-dGroundRules-6`.
- What an invalid TOML file reads, `validate`, and the `refuse` refusal's push-time gate: unit 4's.
  This unit reaches them only through `resolve` and the `get` verb.
- Regenerating the mirror on a policy write: dDeclaredLoop's guarded policy command does that when it
  lands. Until then a branch carrying a policy change carries a stale mirror until its landing.
- A cache or a daemon. Each read spawns git and the shim; §5 prices it.
- A help page section. The mirror is regenerated by the lander and read by hooks; no user act
  changes, and its refusal line names its own remedy.

### Edges

- **consumes-from** `TOOL-dGroundRules-1` — the kit `tools/policy/`, its `kit.toml`, the catalogue, and `check_policy.py` with `ARMS`, `CASES`, its `--fixture` mode and the policy leg that runs every arm
- **consumes-from** `TOOL-dGroundRules-2` — `resolve`, `derive_landed_revision`, `read_policy_text`, `Resolution`, `Refusal` and the `get` verb, which this unit gives `--json`
- **consumes-from** `TOOL-dGroundRules-4` — `validate` and the invalid-file branch with its read of `policy-file.on-invalid`, which the render reaches once per revision
- **hands-off** `TOOL-dGroundRules-10` — `readPolicy` for `runtime.agents-in-flight` in `tools/hooks/agent-cap.js`, and `arm_mirror_landed`'s fixture hook replaced there by the real hook
- **hands-off** external — dDeclaredLoop's guarded policy command, which regenerates the mirror in the commit of each policy write it admits
- **hands-off** `TOOL-dGroundRules-65` — each reason's revision phrase rendered as a placeholder, so the mirror names no commit and is fresh at the commit that carries it (finding 1)
- **hands-off** `TOOL-dGroundRules-14` — the landing replay that observes the mirror fresh at a prepared merge (finding 31)
- **hands-off** `TOOL-dGroundRules-15` — `resolve_read` as the one home of the `.agent-cap.conf` lowering, so the render sees it (finding 2)
- **hands-off** `TOOL-dGroundRules-19` — `mirror --print`, the render at HEAD a staged mirror is compared with (finding 32)
- **hands-off** `TOOL-dGroundRules-21` — bash resolution for the shim, the adopter's absent mirror, the helper's exit mapping, `legacy_blobs`, the read-shape scanner, the mirror's eol pin and the shared single-reader arm (findings 17, 47, 48, 49, 50, 11, 26)
- **hands-off** `TOOL-dGroundRules-31` — `mirror --write`'s exit 2 and its `uncommitted changes` refusal line, which that unit's `--scaffold` defers on install day (finding 24)
- **hands-off** `TOOL-dGroundRules-64` — AC1's blob compare, which that unit runs as `POLICY_BLOB_WHOLE` with the policy file's path whole (the adopted discovery of the closing diff review, round 1)

## 4. Design

### Evidence

- The landing already regenerates every declared output. `run_regen` runs the run-gates kit's
  `regen.py --write` over the working tree (`tools/push-main.sh:757`); `--prepare` folds the result
  into the prepared merge with `commit-tree` (`tools/push-main.sh:908`, `:921`), and the attended
  path commits it with `--no-verify` (`tools/push-main.sh:1111`). Neither commit fires a pre-commit
  hook (`tools/push-main.sh:900`).
- `regen.py` declares an output by a `[[generated]]` row carrying `write`, `check` and `stage`
  (`tools/run-gates/regen.py:16`), read from every tracked `kit.toml` one directory below the tool
  root; the memory-tree kit's rows are the model (`tools/memory-tree/kit.toml:473-479`). The bar runs
  `regen.py --check` before its first leg (`tools/run-gates/run-gates.sh:1449`).
- No JavaScript in the tree resolves the remote ladder or a Python launcher: a search for
  `resolve_remote` and `resolve-python` over `*.js` under `tools/` finds nothing. Their canonicals
  are shell and Python blocks (`tools/lib/resolve-remote.sh:11-53`, `tools/lib/resolve-python.sh:24-54`),
  and the parity arm grades every inline copy it finds by `git grep` over `*.sh`
  (`tools/lib/resolve-python.test.sh:218`), so a new shell copy joins its population with no edit.
- The hooks already spawn `git` with `spawnSync` (`tools/hooks/scratch-guard.js:709-710`), so a
  helper that does the same adds no new kind of cost to a hook.
- The owner's AF-2: "A stale or absent mirror falls back to the TOML reader", the answer that became
  `policy-file.on-invalid`'s default, its other option being its one other value
  (`memory/builds/dClosedLoop/build/2026-10-18-build-PLAY-dClosedLoop-1-audit-fold.md:14-17`).

### Data model — the mirror

```json
{
  "catalogue_blob": "<blob id of the catalogue at the rendered revision>",
  "keys": {
    "budgets.enforce": {"reason": "set in .governance/policy.toml at 3708a705, ...", "source": "file", "value": "warn"},
    "...": {}
  },
  "policy_blob": "<blob id of .governance/policy.toml at the rendered revision, or null when absent>"
}
```

The bytes are `json.dumps(doc, indent=2, sort_keys=True, ensure_ascii=True) + "\n"`, written with
LF, so one revision renders one byte string. The catalogue path is the kit's own,
`<kit dir>/catalogue.toml`, never read from the mirror. A value TOML can hold and JSON cannot is a
`Refusal` naming the key.

**Which keys.** Every catalogue `name` holding no `*` and no `<...>` segment, and every key the
policy table at that revision sets that a pattern row matches. A pattern key the file does not set
is not in the mirror; the helper reads it through the reader (S5).

**Why blob ids and not the revision's commit id.** The brief's S6 says the mirror carries "the landed
revision's sha". A commit cannot carry its own id, and `--prepare` renders the mirror before the
merge commit that carries it exists. The clause's own words decide it: a consumer checks "its hash
against the TOML at that revision" (§8 F2).

### The render

`render_mirror(repo, rev)` resolves `rev` to a sha once, reads the policy text at it once, validates
it once, and runs the reader's per-key resolution for each listed key over that one read. The
reader as units 2 to 4 leave it reads git on every `resolve` call, which over about 270 keys is
hundreds of git spawns. So this unit splits `resolve` into the revision read and
`resolve_read(path, row, read)`, `read` holding the sha, the how-phrase, the text, `validate`'s
problems, the parsed table when valid, and the last valid revision computed once on first need.
`resolve(key, repo, rev)` keeps its signature and every behaviour by calling the two in turn, so
there is still one composition of `RESOLUTION_ORDER` and the invalid branch, and the cases units 2
to 4 put in `CASES` are the proof it did not move.

Under `refuse` with an invalid file and under no valid revision at all, `resolve` raises its
`Refusal`, and the render passes it through: `mirror --write` exits 2 printing the refusal line and
writes nothing, so the landing that carries the invalid file refuses and names the line.

### The verbs

- `mirror --write` first compares `git hash-object -- <path>` with `git rev-parse HEAD:<path>` for the
  policy file and the catalogue, each absent on both sides counting as equal. A difference exits 2:
  `policy: refused · <path>:0 · uncommitted changes; the mirror renders a revision, commit first`. It
  then renders at HEAD and writes the file only when the bytes differ, printing
  `policy: mirror written · <n> keys · policy <blob8> · catalogue <blob8>` or `policy: mirror fresh`.
- `mirror --check` makes the same comparison, renders at HEAD, and compares with the working-tree
  file. Equal exits 0 with `policy: mirror fresh`. Different exits 1 with
  `policy: mirror stale · .governance/policy.json · <first differing key, a blob field, or absent> ·
  run: python <kit>/policy.py mirror --write`.
- `get <key> --json` prints `json.dumps(resolution._asdict(), sort_keys=True)` on stdout. A
  `Refusal` prints its line on stderr, nothing on stdout, and exits 2, as `get` already does.

### The landing row

```toml
[[generated]]
path = ".governance/policy.json"
generator = "policy.py"
why = "the policy file's JSON mirror the hooks read, rendered at each landing (TOOL-dGroundRules-5)"
write = ["python", "{kit}/policy.py", "mirror", "--write"]
check = ["python", "{kit}/policy.py", "mirror", "--check"]
stage = 2
```

Stage 2, beside the record indexes: it reads no other generated output, and the map at stage 3 reads
the tree after it. In `--prepare` the render runs after the mint, at the merge commit, so the mirror
in the landed revision is the render of the policy file in that same revision.

### The reader for hooks

`tools/policy/policy-mirror.js` exports `readPolicy(key, { repo = process.cwd() } = {})`, returning
`{ value, source, reason }` or throwing a `PolicyRefusal` whose message is the reader's refusal line.
Its CLI is `node tools/policy/policy-mirror.js get <key> [--repo <dir>] [--explain]`: the value on
stdout, as the reader's `get` prints it, `--explain` adding `policy: <key> · <source> · <reason>` on
stderr, a refusal on stderr with exit 2. One evaluation order, written in its header comment:

1. `top` is `git -C <repo> rev-parse --show-toplevel`; the kit's place is `__dirname` relative to it.
2. `L`, the landed revision: `bash <kit>/policy-shim.sh landed` with `top` as its working directory.
   An exit 2 is a `PolicyRefusal` carrying the shim's reason.
3. The mirror text, `git cat-file blob L:.governance/policy.json`, and both blob ids,
   `git rev-parse L:.governance/policy.toml L:<kit>/catalogue.toml`, the policy file's absent at L
   being `null`. A missing mirror, or text that does not parse as JSON, is ABSENT.
4. Both recorded ids equal the ids at L: the mirror is FRESH; a key it holds is returned with its
   recorded source and reason. A key it does not hold goes to step 6.
5. Any id differing: the mirror is STALE.
6. ABSENT, STALE, or a missing key: `bash <kit>/policy-shim.sh get policy-file.on-invalid`. `refuse`
   throws `policy: refused · .governance/policy.json:0 · <absent|stale> at <L8>; policy-file.on-invalid
   is refuse`. A missing key is not a mirror failure and skips that refusal. Otherwise the shim's
   `get <key>` is returned, its reason prefixed `mirror <absent|stale> at <L8>; ` where the mirror
   failed.

The working-tree path is never opened. A shim refusal, exit 2 with the reader's line, is a
`PolicyRefusal` with that line, so a stale mirror over an invalid file with no valid revision
refuses exactly as the TOML reader does.

### The shim

`bash tools/policy/policy-shim.sh landed` prints the landed sha: `resolve_remote_sh`, then the branch
the ladder names, else `main`, at `refs/remotes/<remote>/<branch>`, or `refs/heads/<branch>` when the
ladder names no remote, which is `derive_landed_revision`'s rule (TOOL-dGroundRules-2 S1). A ladder
refusal or a ref that names no commit exits 2 printing the reason. `bash tools/policy/policy-shim.sh
get <key>` runs `resolve_python`, then `<python> <kit>/policy.py get <key> --json`, passing its
stdout, stderr and exit code through; no launcher exits 2 printing the resolver's own lines. The
file carries the `remote_ladder_sh` and `resolve_python` blocks between their markers, byte-identical,
and nothing else of either; the rule after the ladder is three lines, held to the reader's by the
`mirror-landed-parity` case.

### The arms and the cases

| Arm | Reads | Finds |
|---|---|---|
| `arm_mirror_parity` | the working-tree mirror against `render_mirror(repo, "HEAD")` | a mirror that differs, or is absent where the policy kit is present |
| `arm_mirror_landed` | `readPolicy` against the reader's `resolve`, for each key the policy file at L sets | a value the two answer differently |
| `arm_mirror_readers` | `git ls-files` of `*.js`, `*.mjs`, `*.cjs`, `*.py`, `*.sh` and `.githooks/*`, outside `tools/policy/`, the memory root and `help/` | a file naming `policy.json` |

`arm_mirror_landed` drives the helper through its CLI from Python, one `node` call per key.

| Case | Plant | Arm | Outcome |
|---|---|---|---|
| `mirror-hand-edited` | the working-tree mirror's `runtime.agents-in-flight` value set to 8, its blob ids kept | `arm_mirror_parity` | RED, naming the key |
| `mirror-absent` | the working-tree mirror deleted | `arm_mirror_parity` | RED, naming `absent` |
| `mirror-direct-reader` | a tracked `.js` file outside the kit reading `.governance/policy.json` with `readFileSync` | `arm_mirror_readers` | RED, naming the file |
| `mirror-worktree-loosened` | landed L sets `runtime.agents-in-flight = 2` with its mirror; the working-tree mirror says 8, blob ids kept; a fixture hook asked for 3 agents | `arm_mirror_landed` | the hook refuses, enforcing 2; a hook admitting is RED |
| `mirror-stale-last-valid` | L sets the limit to 3 and carries the mirror rendered when it was 2 | `arm_mirror_landed` | the helper reads 3, reason opening `mirror stale at` |
| `mirror-stale-refuse` | the same, L also setting `policy-file.on-invalid = "refuse"` | `arm_mirror_landed` | the helper exits 2, `policy: refused · .governance/policy.json:0` |
| `mirror-absent-refuse` | L carries no mirror, under `refuse` and then under `last-valid` | `arm_mirror_landed` | exit 2, then the reader's value |
| `mirror-landed-parity` | four ladder states: one remote; two remotes with `GOV_REMOTE`; two without; no remote | the shim's `landed` against `derive_landed_revision` | the same sha or both refusing, in each state |

The fixture hook is four lines of Node written into the case's temporary repository: it requires the
helper, reads the limit, and exits 2 when the planted request exceeds it. Each case builds its
repository from the fixture `TOOL-dGroundRules-1` gives every case, adding `policy.py`,
`policy-mirror.js` and `policy-shim.sh`, with a bare remote whose `main` is L; the working tree is
then planted. The outcome cases assert a stated outcome, as unit 4's `on-invalid-classes` does,
rather than RED as planted: a correct helper leaves `mirror-worktree-loosened` green, and the RED
the close observes is the helper broken to read the working-tree file.

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `render_mirror`, `resolve_read`, `cmd_mirror` | function | `tools/policy/policy.py` |
| `mirror --write`, `mirror --check`, `get --json` | CLI verb and flags | `tools/policy/policy.py` |
| `readPolicy`, `readLandedRevision`, `readMirrorAt`, `runReader` | function | `tools/policy/policy-mirror.js` |
| `PolicyRefusal` | type | `tools/policy/policy-mirror.js` |
| `landed`, `get` | shim verbs | `tools/policy/policy-shim.sh` |
| `arm_mirror_parity`, `arm_mirror_landed`, `arm_mirror_readers` | arm functions in `ARMS` | `tools/policy/check_policy.py` |
| the eight `mirror-*` names of the table above | `CASES` entries | `tools/policy/check_policy.py` |

Each Python function leads with a verb `.lexicon.conf` declares, under `py.function`'s snake case;
each JavaScript function leads with one under `js.function`'s camel case. The policy kit's version
marker moves with this unit.

### Rollout

The mirror lands with the build and no hook reads it until `TOOL-dGroundRules-10`. This unit shares
`tools/policy/check_policy.py` and `tools/policy/kit.toml` with `TOOL-dGroundRules-6`, so the two
passes sequence, by M6 clause 1, despite their shared order.

### Files touched (estimate)

- `tools/policy/policy.py`
- `tools/policy/policy-mirror.js`
- `tools/policy/policy-shim.sh`
- `tools/policy/check_policy.py`
- `tools/policy/kit.toml`
- `tools/policy/README.md`
- `.governance/policy.json`
- `.gitattributes`
- `memory/map/generated/symbols.json`
- `memory/map/generated/inventories.json`

### Alternatives rejected

- **A JavaScript port of the remote ladder and the Python resolver.** Two copies no parity row can
  grade byte for byte. The shim carries the canonical blocks, which the existing rows grade for free.
- **The helper spawning the reader on every read.** Correct, and it makes the mirror pointless: the
  mirror exists so the common read is git and JSON alone.
- **The render reading the working-tree policy file.** `resolve` reads revisions, so the render would
  need a second, text-fed composition of the resolution order; the clean-tree precondition keeps one.
- **A new manifest leg for the parity check.** The gotcha `a-new-leg-trips-a-growing-set-of-meta-gates`
  prices it, and the policy leg already runs every arm the kit adds (§8 F6).

## 5. Production-readiness checklist

- security — the helper never opens the working-tree mirror, takes a value only while both blob ids
  match the landed revision, and under `refuse` refuses rather than read defaults. A hand-edited
  mirror committed on a branch is overwritten by the landing's render and reds the parity arm before
  it. What escapes: a landed mirror whose values were edited while its ids were kept, if a landing
  ever skips `regen.py`; the landing's regeneration is what closes that, and the guard of
  `TOOL-dGroundRules-6` refuses an agent's commit of the file.
- perf / scale — a fresh read is one `bash` spawn running about four `git` calls, then two `git`
  calls from Node, roughly 0.3 s on a Windows node (UNVERIFIED, an estimate); a stale read adds a
  Python spawn per key. The render is one revision read and about 270 in-process resolutions.
- error / empty / loading states — an absent mirror, an unparsable mirror and a missing key each
  have a named path in §4's order; a shim exit 2 or a missing launcher is a refusal naming why.
- observability — `--explain` names the source and the reason, and a fallback's reason opens with
  `mirror absent at` or `mirror stale at` and the landed sha8.
- risks — a landing whose mint edits the policy file or the catalogue makes `mirror --write` refuse
  and the landing stop, loudly; neither file carries a version marker today. A branch carrying a
  policy change carries a stale mirror until it lands, so a bar run on that branch before its
  landing reds the parity arm; the bar a landing runs follows the regeneration.
- testing — the eight cases, each run by `check_policy.py --fixture`, with AC1 to AC12.
- migration — none: the mirror is new and no consumer reads it yet.
- user docs — N/A: no user act changes (§3).

## 6. Acceptance criteria

Every command runs from the repository root. The criteria spell the kit's files by bare name,
`policy.py`, `policy-mirror.js`, `policy-shim.sh` and `check_policy.py`, because the spec-token
checker grades a path-shaped token in a criterion against the tracked set and this run creates them.
Each fixture repository sits under `%TEMP%`, short-named.

- **AC1** — When `python policy.py mirror --write` runs on the built tree, `policy.json`
  parses as JSON, its `policy_blob` equals `git rev-parse HEAD:policy.toml`, its
  `catalogue_blob` equals the catalogue's blob at HEAD, its `keys` hold every catalogue name with no
  pattern segment, each with `value`, `source` and `reason`, and a second `--write` prints
  `policy: mirror fresh` and leaves the bytes unchanged.
  Red when: a blob id is missing or wrong, a catalogue name is missing, or two renders differ.
  figure: the key count is DERIVED from the catalogue at observation.
- **AC2** — When `python check_policy.py --fixture mirror-hand-edited` and `--fixture mirror-absent`
  run, each case is RED as planted, naming `runtime.agents-in-flight` and `absent` respectively, and
  green unplanted; on the built tree `python policy.py mirror --check` exits 0.
  Red when: a hand-edited or deleted mirror passes the parity arm.
- **AC3** — When the policy file in a scratch copy carries an uncommitted edit,
  `python policy.py mirror --write` and `mirror --check` each exit 2 printing `uncommitted changes`
  and the mirror file is unchanged.
  Red when: the render reads a revision that is not the working tree's, without saying so.
- **AC4** — When `python tools/run-gates/regen.py --list` runs on the built tree, it lists the item
  for `policy.json` at stage 2 with `mirror --write` and `mirror --check` as its argv.
  Red when: the row is absent, so a landing leaves the mirror as the branch had it.
- **AC5** — When `python check_policy.py --fixture mirror-worktree-loosened` runs, the fixture hook
  refuses the request of 3 and `node policy-mirror.js get runtime.agents-in-flight --repo <fixture>`
  prints `2`.
  Red when: the helper opens the working-tree mirror, prints `8` and the hook admits.
- **AC6** — When `--fixture mirror-stale-last-valid` runs, the helper prints `3`, and `--explain`
  prints source `file` with a reason opening `mirror stale at`.
  Red when: the stale mirror's `2` is returned, or a catalogue default is.
- **AC7** — When `--fixture mirror-stale-refuse` and `--fixture mirror-absent-refuse` run, the helper
  exits 2 printing `policy: refused · .governance/policy.json:0` under `refuse`, and under
  `last-valid` the absent mirror reads the reader's value.
  Red when: a stale or absent mirror is read under `refuse`, or refused under `last-valid`.
- **AC8** — When the `remote_ladder_sh` and `resolve_python` blocks are cut from `policy-shim.sh` and
  from their canonicals `tools/lib/resolve-remote.sh` and `tools/lib/resolve-python.sh` with the awk
  range the parity arm uses, and compared with `diff`, both diffs are empty.
  Red when: a block drifts from its canonical.
- **AC9** — When `--fixture mirror-landed-parity` runs, the shim's `landed` and
  `derive_landed_revision` answer the same sha in the one-remote, `GOV_REMOTE` and no-remote states,
  and both refuse in the two-remotes state.
  Red when: the shim falls back to another branch or refuses where the reader answers.
- **AC10** — When `python policy.py get runtime.agents-in-flight --json` runs on the built tree, it
  prints one JSON object whose keys are exactly `reason`, `source` and `value`; with a key no
  catalogue row names it prints nothing on stdout and exits 2 with a line opening `policy: refused ·`.
  Red when: `--json` changes the refusal, or prints a value the plain `get` does not.
- **AC11** — When `python check_policy.py --fixture mirror-direct-reader` runs, it is RED as planted,
  naming the planted file, and green unplanted; on the built tree `arm_mirror_readers` prints a
  non-zero population and no finding.
  Red when: a direct reader of the mirror passes, or the arm scans nothing.
- **AC12** — When `git check-attr eol -- policy.json` runs, it prints `eol: lf`.
  Red when: the mirror is unpinned and a CRLF checkout makes the parity arm red on a fresh mirror.

## 7. Gates

`python resolver (behaviour + inline parity + idiom ban)` · `remote literals (kit code names no remote)` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `kit epoch (shipped bytes move, the version moves)` · `install-prefix (shipped surface)` · `shell hygiene (a fork spent on builtin work)` · `push-main self-test` · `memory hygiene` · `recall floor` · `recall floor arms`

The policy legs `TOOL-dGroundRules-1` declares, `policy check` and `policy fixtures`, run every arm
and case below; they are named by the arm lines rather than on the leg line, because neither exists
at this spec's base.

New arm: tools/policy/check_policy.py (`arm_mirror_parity`, live and `--fixture mirror-hand-edited mirror-absent`) · covers AC2 · a hand-edited and a deleted working-tree mirror · none
New arm: tools/policy/check_policy.py (`arm_mirror_landed`, `--fixture mirror-worktree-loosened mirror-stale-last-valid mirror-stale-refuse mirror-absent-refuse`) · covers AC5 AC6 AC7 · the helper staged to read the working-tree mirror, then staged to skip the blob compare · none
New arm: tools/policy/check_policy.py (`--fixture mirror-landed-parity`) · covers AC9 · the shim's rule after the ladder staged to skip the `main` fallback · none
New arm: tools/policy/check_policy.py (`arm_mirror_readers`, live and `--fixture mirror-direct-reader`) · covers AC11 · a planted direct reader of the mirror · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a
  legal status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:28`, which the header
  regex at `tools/memory-tree/tree_lib.py:377` joins. Observation, 2026-10-23: the set is `OPEN
  SPECCED INPROGRESS BLOCKED DEFERRED CLOSED WONTDO`, so a `DRAFT` header parses as no header and the
  unit reads MISSING. Liveness: the tuple would carry `DRAFT` if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-23, delegated): `OPEN`, the token `memory/TEMPLATE-SPEC.md` gives
  drafting. widens: none · relaxes: none
- **F2 — What pins the mirror to "the landed revision": the revision's commit id, as the brief's S6
  spells it, or blob ids?** (a) The commit id: a commit cannot carry its own id, `--prepare` renders
  before the merge commit exists (`tools/push-main.sh:908-921`), and a `--check` comparing it would
  red every commit, so veto 1 discards it. (b) The blob ids of the policy file and the catalogue,
  which a consumer compares at the landed revision. Rung 1: the clause says "checking its hash
  against the TOML at that revision". The catalogue's id joins because a default comes from it.
  RESOLVED (agent, 2026-10-23, delegated): (b); S6's field is respelled here and only here.
  widens: none · relaxes: none
- **F3 — What does the render read: a revision, the working tree, or the index?** (a) HEAD, with a
  clean-tree precondition, through `resolve`'s own composition. (b) The working-tree text, which
  needs a text-fed resolution beside `resolve`, a second composition of one order. (c) The index,
  the same cost as (b). All three meet every criterion; (a) opens no second composition and leaves
  units 2 to 4's interface as S4 fixes it. Recommendation (a). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (a). widens: none · relaxes: none
- **F4 — What does a stale or absent mirror read under `last-valid`?** (a) The TOML reader at the
  landed revision. (b) The last landed revision whose mirror was fresh, a history walk inside every
  hook. Rung 1: the clause says "else reading through the TOML reader", and the owner's AF-2 says
  "A stale or absent mirror falls back to the TOML reader".
  RESOLVED (agent, 2026-10-23, delegated): (a); under `refuse` it refuses, AF-2's other option.
  widens: none · relaxes: none
- **F5 — How does JavaScript reach the landed revision and the Python reader?** (a) A JavaScript port
  of the ladder and the resolver. (b) A shell shim carrying both canonical blocks inline, graded by
  the parity rows that exist. (c) The reader for every read, which voids the mirror. (c) fails AC5's
  premise that the common read is the mirror, so veto 1 discards it; (a) and (b) meet every
  criterion. Tie-break: reuse of the seam M5 found. Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F6 — Is "a parity leg" a new manifest leg or an arm of the policy leg?** (a) A new leg running
  `mirror --check`. (b) `arm_mirror_parity` in the policy leg `TOOL-dGroundRules-1` declares, plus the
  bar's `regen.py --check` preflight over the same row. Both red on a hand-edited mirror; (b) trips
  no new meta-gates, the cost `memory/gotchas/a-new-leg-trips-a-growing-set-of-meta-gates.md`
  records. Recommendation (b). Rung 3.
  RESOLVED (agent, 2026-10-23, delegated): (b). widens: none · relaxes: none
- **F7 — Does the build's grant lift veto 2 for the mirror's public surface?** `mirror`, `get --json`,
  `policy-mirror.js`, `policy-shim.sh`, `.governance/policy.json` and the kit's `[[generated]]` row
  are new public surface, and `cl-dClosedLoop-0011` names the mirror, its consumers and its parity.
  RESOLVED (agent, 2026-10-23, delegated): lifted by `PLAY-dClosedLoop-3`, rung 3.
  grants: PLAY-dClosedLoop-3 the mirror, its verbs, its helper and shim, and its landing row ·
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, from the packet's Items 5, the brief's S6, the owner's AF-2,
  and the lander, regen and ladder code read at base `3708a705`.
- rev-2 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-65, TOOL-dGroundRules-14, TOOL-dGroundRules-15, TOOL-dGroundRules-19, TOOL-dGroundRules-21 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit's findings that repair this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-3 · 2026-10-23 · §3 · the **hands-off** edges to TOOL-dGroundRules-31 added, each the reciprocal of that unit's **consumes-from** line: the promotions of the round-1 spec audit of units 22 to 25 that build on this unit. No scope, design or acceptance moved here; the repair is the promoted unit's.
- rev-4 · 2026-10-23 · §3 · the hands-off edge to `TOOL-dGroundRules-64`, the reciprocal end of the round-1 closing diff
  review's promotions; no scope or criterion moved.
- rev-5 · 2026-10-23 · §3 · TOOL-dGroundRules-13 renamed TOOL-dGroundRules-65 by the owner's ruling, the id a landed dSafePassage ask holds; nothing else moved.

## 10. Reuse audit

The seams extended are the landing's regeneration, `run_regen` (`tools/push-main.sh:757`) driving
`regen.py`'s `[[generated]]` rows (`tools/run-gates/regen.py:16`), and the gated inline blocks
`remote_ladder_sh` (`tools/lib/resolve-remote.sh:11-53`) and `resolve_python`
(`tools/lib/resolve-python.sh:24-54`), whose parity rows grade a new copy with no edit. The reader is
units 2 to 4's `resolve`, split once and not copied. `python tools/codebase-map/reuse_lookup.py
"regenerate a JSON mirror of a config file at landing and check it fresh"` ranked name stems (`check`,
`render_inventories_json`) and named no mirror seam; `python tools/codebase-map/reuse_lookup.py "read
a file's blob at the landed default branch revision from a hook"` ranked `read_blobs_at`
(`tools/memory-tree/tree_lib.py`), a sibling kit's batch reader a kit may not import, and
`readConfKey` (`tools/hooks/scratch-guard.js`), which reads the working tree, the read this unit
exists to forbid. So the regeneration and the blocks were found by reading the lander, not by the
probe. The recall probe returned the design audit's M11 and FM1, which agree with source: no mirror
exists and no hook reads one. It returned the owner's AF-2, which this spec follows (§8 F4).

Recall terms used: `python tools/memory-recall/query.py "how is a JSON mirror of the policy file kept
fresh and read by hooks at the landed revision" --terms "policy mirror JSON landed revision blob
regen stale hook parity on-invalid generated"`
