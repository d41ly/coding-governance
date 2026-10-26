# TOOL-dSafePassage-6 — forwarding shims for a moved command, hook path or module import, held for their deprecation window

**Status:** DEFERRED · rev-6 · 2026-10-26 · node d · Tier-2 · base 3708a705 · streams tooling · order 4 · advances TOOL-dSafePassage-14 · ratified 2026-10-24

**Carries:** cl-dClosedLoop-0023@6e1e2e99 whole
**Carries:** node:policy-key.install.deprecation-window
**Carries:** node:policy-key.install.on-shim-call

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-6-deviation-137.md](../build/2026-10-23-build-TOOL-dSafePassage-6-deviation-137.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-6-deviation-151.md](../build/2026-10-24-build-TOOL-dSafePassage-6-deviation-151.md) | deviation | — |
| [2026-10-24-build-TOOL-dSafePassage-6-deviation-159.md](../build/2026-10-24-build-TOOL-dSafePassage-6-deviation-159.md) | deviation | — |
| [2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md](../build/2026-10-25-build-TOOL-dSafePassage-1-agent-ledger.md) | journal | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-15 TOOL-dSafePassage-16 TOOL-dSafePassage-17 TOOL-dSafePassage-18 TOOL-dSafePassage-19 TOOL-dSafePassage-20 TOOL-dSafePassage-21 TOOL-dSafePassage-22 TOOL-dSafePassage-23 TOOL-dSafePassage-24 TOOL-dSafePassage-25 TOOL-dSafePassage-26 TOOL-dSafePassage-27 TOOL-dSafePassage-28 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-31 TOOL-dSafePassage-32 TOOL-dSafePassage-33 TOOL-dSafePassage-34 TOOL-dSafePassage-35 TOOL-dSafePassage-36 TOOL-dSafePassage-37 TOOL-dSafePassage-38 TOOL-dSafePassage-39 TOOL-dSafePassage-40 TOOL-dSafePassage-41 TOOL-dSafePassage-42 TOOL-dSafePassage-43 TOOL-dSafePassage-44 TOOL-dSafePassage-45 TOOL-dSafePassage-46 TOOL-dSafePassage-47 TOOL-dSafePassage-48 TOOL-dSafePassage-49 TOOL-dSafePassage-50 TOOL-dSafePassage-51 TOOL-dSafePassage-52 TOOL-dSafePassage-53 TOOL-dSafePassage-54 TOOL-dSafePassage-55 TOOL-dSafePassage-56 TOOL-dSafePassage-57 TOOL-dSafePassage-58 TOOL-dSafePassage-59 |
| [2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md](../build/2026-10-25-build-TOOL-dSafePassage-1-parent-fixes-return.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26 |
| [2026-10-25-build-TOOL-dSafePassage-6-deviation-161.md](../build/2026-10-25-build-TOOL-dSafePassage-6-deviation-161.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md](../prompts/2026-10-23-prompt-TOOL-dSafePassage-1-spec-brief.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-dgroundrules-reground.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-5 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-13 |
| [2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-1-owner-forks.md) | research | TOOL-dSafePassage-1 |
| [2026-10-24-prompt-TOOL-dSafePassage-6-1-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-6-1-spec-writer.md) | journal | — |
| [2026-10-24-prompt-TOOL-dSafePassage-6-2-spec-writer.md](../prompts/2026-10-24-prompt-TOOL-dSafePassage-6-2-spec-writer.md) | journal | — |
| [2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md](../prompts/2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md) | research | TOOL-dSafePassage-1 TOOL-dSafePassage-9 TOOL-dSafePassage-13 TOOL-dSafePassage-26 |
| [2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md) | research | TOOL-dSafePassage-5 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-17 TOOL-dSafePassage-21 TOOL-dSafePassage-26 TOOL-dSafePassage-29 TOOL-dSafePassage-30 TOOL-dSafePassage-61 |
| [2026-10-26-prompt-TOOL-dSafePassage-6-build-brief.md](../prompts/2026-10-26-prompt-TOOL-dSafePassage-6-build-brief.md) | journal | — |
| [2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md](../reviews/2026-10-23-review-TOOL-dSafePassage-1-2-3-4-5-6-7-8-9-10-11-12-13-spec-audit-round1.md) | spec-audit | TOOL-dSafePassage-1 TOOL-dSafePassage-3 TOOL-dSafePassage-2 TOOL-dSafePassage-4 TOOL-dSafePassage-7 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-13 TOOL-dSafePassage-5 |

<!-- /gen:spec-records -->

## 1. Goal

When gov moves a command, a hook path or a module import, the old path keeps working as a generated
forwarder that warns or journals as the adopter's `install.on-shim-call` says, and gov may not take
the forwarder away until `install.deprecation-window` releases have been cut since it landed, every
shim held while no release exists. Today an adopter's call to a moved surface fails outright and no
window keeps the old surface working while the adopter catches up (`gap-deploy-24`, closed by this
unit). It is P38's "a surface an adopter can see keeps working, or warns, until its window closes",
counted as SA-8 answered: "windows start at the first cut release, every earlier shim held until
then".

## 2. Scope (IN)

- **S1** — The declaration: one `[[shim]]` row per moved surface, in a new file beside the registry,
  each with `id`, `kind` (`command`, `hook` or `module`), `from` (the old path, where the forwarder
  is written), `to` (the path it forwards to) and `closed` (false until the window allows it). The
  forwarder's language comes from the `from` path's extension: `.sh`, `.js` or `.py`, and a
  `module` row must be `.py`. Observed by AC1 and AC2.
- **S2** — The generator, `tools/govkit/shims.py`: `--write` renders every open row's forwarder at
  its `from` path from one template per language, each carrying a `gov:shim <id>` marker line, and
  `--check` compares every open row's file with its render and asserts every closed row's file is
  absent. A forwarder is never hand-written. Observed by AC1 and AC2.
- **S3** — The forward. A `sh` forwarder `exec`s bash on its target with every argument; a `js`
  forwarder spawns the running node on its target with every argument and inherited stdio and exits
  with its status; a `py` command forwarder runs its target as `__main__` with the arguments; a
  `py` module forwarder loads its target by path and stands in for itself in `sys.modules`. Each
  resolves its target relative to its own directory, so it works at any install prefix. Observed by
  AC3.
- **S4** — The call, under `install.on-shim-call`. Under `warn`, the default, the forwarder prints
  one stderr line naming the old path, the new path and that the forwarder is held only until its
  window closes, and adds one journal line. Under `journal` it adds the journal line and prints
  nothing. The value is the adopter's committed policy at its landed revision, as the parent's reader
  answers it, so an unset key or an absent policy file reads the catalogue default `warn`. A value
  outside the two never reaches the forwarder: the reader answers the last valid revision's value or
  refuses (TOOL-dGroundRules-4 S5). A read that fails, a refusal or a missing policy kit included,
  reads `warn`, and the stderr line adds that the policy could not be read. The journal line carries
  the time, the shim id, `from`, `to` and the mode, and never the call's arguments. Neither branch
  ever blocks the forward. Observed by AC4 and AC5.
- **S5** — The window, under `install.deprecation-window`. A row may be set `closed = true` only when
  at least one release has been cut and at least the window's count of releases has been cut since
  the commit that landed the row on the default branch. With no release cut every row is held,
  whatever the window, and a row not yet landed is held. The landing commit is derived from history,
  never typed. Today no release has been cut, so the release reader is the stand-in that returns
  none until dShippedRelease defines its release tags. Observed by AC6 and AC7.
- **S6** — The check in the deployer's own selfcheck, a new arm 11: it runs S2's comparison and S5's
  window over the declared rows and prints how many rows it graded, a zero included, since gov ships
  no shim today. Observed by AC8.
- **S7** — The two keys. dGroundRules lands both catalogue rows from v2's `[policies]` rows
  (v2:1404-1405) with their allowed values, default and owner, and with no `summary` or `usage`, on
  its shrink-only list (TOOL-dGroundRules-1 S3, S6): `install.deprecation-window`, values 0, 1, 2 or
  4, default 2; and `install.on-shim-call`, values `warn` or `journal`, default `warn`. This unit
  fills each row's `summary` and `usage` as `cl-dClosedLoop-0007` requires and drains both names
  with `policy.py lists --write` in the same commit. It adds no row. Each key keeps a reader in a
  shape the parent's reader-coverage arm counts (TOOL-dGroundRules-8, its Readers table). Observed by
  AC9.
- **S8** — The fixture, on the generator's own CLI: `--fixture --plant <case>` builds a scratch git
  repository with a planted moved surface, its forwarder and its target, runs the forwarder, and
  prints what it observed beside what the case expects. Observed by AC3 to AC7.
- **S9** — The docs: a page `help/shims.md` saying what an adopter sees when it calls a moved path,
  the two modes and that a mode is read from the committed policy at its landed revision, where the
  journal is, and how long a forwarder is held, and its line in `help/README.md`. Observed by AC10.

## 3. Non-goals (OUT)

- Any first shim. Gov moves no command, hook path or module in this build, so the declaration ships
  with no row. The first rows are the later builds' that move a surface, among them
  dWellOiledMachine's `/unattended` shim. dOrderedCharter's module re-export is no `[[shim]]` row: its
  spec 31 holds it under a `module-export` class row, and dConvergedCharter counts its window.
- Taking a forwarder away when its window closes: dConvergedCharter's "shims removed at window
  close". This unit only refuses a close before the window allows it.
- Release tags and how a release is cut: dShippedRelease's `kits.cut` and its release notes. This
  unit reads releases through one stand-in that returns none today.
- The adopter view of the journal, `kits.currency`'s shim-call reading and the fleet register:
  dShippedRelease's.
- The pair rule that binds `install.deprecation-window` to at least `currency.max-behind` (v2:1427):
  the schema check's, which applies pair rules to each preset.
- The step gate's red on a forwarder's file leaving the tree with no step row: TOOL-dSafePassage-10's,
  which sees the file as an installable member like any other.
- The release-0 fixture's untagged history holding every shim: TOOL-dSafePassage-5's case, which
  reads this unit's window decision and needs nothing more from it.
- Freezing a landed `[[shim]]` row against a hand edit or deletion. dWitnessedBar's append-only
  factory is where landed rows of every kind join; until it lands, a deleted row's forwarder file
  still needs a step row at the step gate, which is the guard that exists.

### Edges

- **consumes-from** external — dGroundRules, landed before the build run: the catalogue `tools/policy/catalogue.toml` with both rows and the list `tools/policy/unsummarised-keys.txt` (TOOL-dGroundRules-1 S3, S6), the reader `policy.py get` at the landed revision with the catalogue default and its reason (TOOL-dGroundRules-2 S7, TOOL-dGroundRules-3), its shell half `policy-shim.sh get` and the mirror's one reader `readPolicy` (TOOL-dGroundRules-5 S5, S6); without them S7 has no rows to fill, every forwarder's read fails and reads `warn`, and the window's read refuses and holds every closed row
- **hands-off** external — dShippedRelease replaces the release stand-in with its release tags and reads the journal for the adopter view; dConvergedCharter closes each forwarder whose window has closed
- **hands-off** `TOOL-dSafePassage-13` — `read_policy_value(key, root)` in `govkit.py`, which this unit defines when it builds before TOOL-dSafePassage-9 and which that unit's docs leg calls for `help.enforce`
- **hands-off** `TOOL-dSafePassage-26` — the minors batch of the round-1 spec audit, which repairs the findings that land on this unit after every unit is built

## 4. Design

### Data model

The declaration, `tools/govkit/shims.toml`, one row per moved surface:

```toml
[[shim]]
id = "memory-tree/hygiene-entry"                    # <entry>/<slug>, as a step id (brief S1)
kind = "command"                                     # command | hook | module
from = "{prefix}/memory-tree/check-old.sh"           # the old path: the forwarder is written here
to = "{prefix}/memory-tree/check-memory-hygiene.sh"  # the path it forwards to
closed = false                                       # true only once S5 allows it
```

That row is illustrative: the file ships with a header comment and no row (§3). `{prefix}` resolves
through govkit's own `derive_tool_root` and `resolve_prefix_token` (`govkit.py:154-195`), so a
forwarder lands where the descriptor's rule for that path lands. A pass that moves a surface keeps the
old path's `[[files]]` rule, which now ships the forwarder's bytes, and adds a rule for the new path.

The journal line, one JSON object per call, appended to the file
`git rev-parse --git-path govkit/shim-calls.jsonl` names in the repository the call runs in:

```json
{"utc": "2026-10-23T10:00:00Z", "shim": "memory-tree/hygiene-entry", "from": "tools/memory-tree/check-old.sh", "to": "tools/memory-tree/check-memory-hygiene.sh", "mode": "warn"}
```

It lives under the git directory, the place `git_path` already resolves for this deployer
(`govkit.py:7046-7063`), so a call never dirties the adopter's working tree. A call outside a git
work tree journals nothing and says so on stderr.

### The forwarders

One template per language, a string constant in `tools/govkit/shims.py` rendered by
`render_shim(row)`, each opening with its marker line and a prelude that reads
`install.on-shim-call` through the parent's reader for its language and acts as S4 says:

| Language | Reads the key through | Forwards by |
|---|---|---|
| `sh` | `bash "$policy/policy-shim.sh" get install.on-shim-call`, the policy kit's shell half, which resolves Python itself and prints `get --json` (TOOL-dGroundRules-5 S6, S7); the mode is `journal` only when that output ends `"value": "journal"}`, the last of its sorted keys | `exec bash "$here/<to, relative>" "$@"` |
| `js` | `require(<policy>/policy-mirror.js).readPolicy("install.on-shim-call", { repo: process.cwd() })`, the mirror's one reader (TOOL-dGroundRules-5 S5) | `spawnSync(process.execPath, [target, ...args], {stdio: "inherit"})`, then `process.exit` with its status |
| `py`, `command` | `subprocess.run([sys.executable, <policy>/policy.py, "get", "install.on-shim-call"])`, the reader's CLI (TOOL-dGroundRules-2 S7) | `runpy.run_path(target, run_name="__main__")` with `sys.argv[0]` set to the target |
| `py`, `module` | the same call, at import | `importlib.util.spec_from_file_location`, executed, then `sys.modules[__name__]` set to it |

`<policy>` is the policy kit's directory, written at render as the path from the forwarder's own
directory to `{prefix}/policy/`, resolved as `to` is (§8 F7). Each read runs in the caller's working
directory, so it answers the repository the call runs in, never gov's, since the mode is the
adopter's. It reads that repository's committed policy at its landed revision, never its working
tree (TOOL-dGroundRules-2 S2). No template spells the mirror's path, which `arm_mirror_readers` reds
in tracked code outside the policy kit (TOOL-dGroundRules-5 S9). The `js` template writes its call on
one line with unescaped double quotes, so the reader-coverage arm counts it in
`tools/govkit/shims.py` as `install.on-shim-call`'s reader. A prelude whose read fails for any reason
takes `warn` and forwards anyway, so a broken policy file or an absent policy kit never breaks the
adopter's call.

### The window

`check_shim_windows(root, releases=None)` grades each row with `closed = true`:

1. `releases` defaults to `read_releases(root)`, the stand-in, which returns an empty list with the
   reason "no release has been cut: dShippedRelease defines release tags".
2. `resolve_shim_landing(root, id)` is the oldest commit on the default branch's first-parent history
   whose `tools/govkit/shims.toml` carries the row's id, found with one `git log --first-parent
   --reverse -S` over that file. The default branch is the remote ladder's (`resolve_remote`,
   `govkit.py:558`). A row on no landed commit is held.
3. `derive_shim_window(landing, releases, window)` counts the releases that descend from the landing
   commit. The row is open-allowed when the release list is non-empty and that count is at least the
   window, and held otherwise.
4. A `closed = true` row that is held is one refusal line naming the row, its landing, the release
   count and the window.

The window value is gov's own: gov decides when it takes a forwarder away, and the adopter's
currency budget is what the pair rule binds it to. `shims.py` imports govkit as
`tools/govkit/matrix.py:51-52` does and calls `govkit.read_policy_value("install.deprecation-window",
root)`. That function, `read_policy_value(key, root)`, lives once in `tools/govkit/govkit.py` beside
its `resolve_kit_dir` block (`:196-233`), and specs 9 and 13 call the same one. It runs
`<sys.executable> <policy kit>/policy.py get <key>` with `root` as its working directory, so it reads
the committed policy at the landed revision, `get`'s default, and an unset key reads the catalogue
default 2. govkit reaches the policy kit as a subprocess and never imports it, finding it with that
`resolve_kit_dir`, called from the directory holding govkit itself. A refused read, or no policy kit
found, holds every `closed = true` row, its refusal line carrying the reader's line. The call's first
argument is the key as a literal, the `.py` shape the reader-coverage arm counts.

### The selfcheck arm

Arm 11 of `selfcheck` (`govkit.py:1832`) calls `check_shim_parity(root)` and
`check_shim_windows(root)` and prints `shims: <n> row(s) graded · <k> open · <c> closed` on every run,
`0 row(s)` today. The arm reads history for the landing commit, so the `govkit selfcheck` row in
`tools/gate-legs.json` gains a `reads` entry for `history`, as other history-reading legs declare one.

### The fixture

```
python tools/govkit/shims.py --write | --check
python tools/govkit/shims.py --fixture --plant <sh|js|py|module> [--mode warn|journal|unset|bogus]
python tools/govkit/shims.py --fixture --plant window --window <0|1|2|4> --releases <n> [--unlanded]
python tools/govkit/shims.py --fixture --plant parity-edit
```

A forwarding plant builds a scratch repository under `tempfile.mkdtemp(prefix="shim-")`, on a `main`
branch with no remote, holding a copy of gov's policy kit, a target that prints its arguments and its
stdin and exits 3, and the forwarder `render_shim` makes for a planted row whose `from` is the retired
path. It commits the mode in the scratch policy file, then renders the mirror with the copied kit's
`policy.py mirror --write` and commits it, so the `js` plant reads a fresh mirror and `shims.py`
never spells the mirror's path. `unset` commits no policy file. `bogus` commits a value the catalogue
refuses as the file's only revision, so the reader refuses and `mirror --write` refuses with it,
leaving no mirror. The plant runs the forwarder with the arguments `a` and `b c` and the stdin `in`,
and prints one line per observation: the exit, the arguments and stdin the target saw, the stderr
line or none, and the journal line count. A window plant commits the window in the scratch policy
file, then a landed row, then `<n>` commits it passes as the release list, and grades a
`closed = true` row. Every plant exits 0 when each observation matches its case and 1 otherwise, and
2 when it cannot observe (`node` not found for `js`).

### Inventory

Minted: the module `tools/govkit/shims.py`; the file `tools/govkit/shims.toml` and its `[[shim]]`
keys `id`, `kind`, `from`, `to` and `closed`; the kinds `command`, `hook` and `module`; the marker
`gov:shim`; the journal path `govkit/shim-calls.jsonl` under the git directory; the functions
`read_shim_rows`, `render_shim`, `write_shims`, `check_shim_parity`, `read_releases`,
`resolve_shim_landing`, `derive_shim_window`, `check_shim_windows`, `run_fixture` and `main`; the
CLI flags `--write`, `--check`, `--fixture`, `--plant`, `--mode`, `--window`, `--releases` and
`--unlanded`; selfcheck arm 11. `read_policy_value` is defined in `tools/govkit/govkit.py` by
whichever of this unit and TOOL-dSafePassage-9 builds first, both at order 4; the other calls it.
Naming cells: each minted function passes `py.function` (`tools/lexicon/lexicon.py --suggest <name>
--as py.function`, OK for all eleven, `read_policy_value` on 2026-10-24); the rest fall in no
declared cell. Owned nodes:
`policy-key.install.deprecation-window` and `policy-key.install.on-shim-call`, the two catalogue rows
S7 fills.

### Migration

Additive. The declaration ships empty and the selfcheck arm grades zero rows. No adopter file
changes until a later build declares a row.

### Rollout

Live at landing, dark in effect, since no row exists. The deployer never travels, so the generator
and the arm are gov-side only; only rendered forwarders reach an adopter, through the ordinary engine
rows of the kit whose surface moved. `govkit.py` is also written by TOOL-dSafePassage-9 and
TOOL-dSafePassage-10, so the three passes sequence rather than run concurrently (M6). A kit carrying a
forwarder declares no `requires` on the policy kit: without one, its forwarder reads `warn`.

S7 lands as two commits. The first fills the two rows and drains the list. The second holds only
`.governance/policy.json` as `policy.py mirror --write` regenerates it: the mirror records the
catalogue's blob id (TOOL-dGroundRules-5 S1), so filling a row stales it, and the guard admits a
mirror commit only when the policy file and the catalogue equal HEAD (TOOL-dGroundRules-19 S1).

### Files touched (estimate)

- `tools/govkit/shims.py` (new)
- `tools/govkit/shims.toml` (new)
- `tools/govkit/govkit.py` (selfcheck arm 11, and `read_policy_value` where this unit builds before
  TOOL-dSafePassage-9)
- `tools/govkit/selftest.py`
- `tools/gate-legs.json`
- `help/shims.md` (new)
- `help/README.md`
- `tools/policy/catalogue.toml`
- `tools/policy/unsummarised-keys.txt`
- `.governance/policy.json`, regenerated, in its own commit

The last three are dGroundRules' files, which the build run adds to this unit's `--dispatch --writes`.

### Alternatives rejected

- **Forwarders written by hand.** Four templates times every moved surface is a hand copy per move,
  and a hand edit to one forwarder is invisible. S2 renders them and `--check` reds a drifted one.
- **The mode baked in at render time.** A forwarder is gov's engine bytes, the same in every adopter,
  so a baked mode would be gov's choice, never the adopter's that `install.on-shim-call` is.
- **A forwarder that refuses.** `refuse` was dropped by the owner's FK-1-4 with FK-3-1, "Drop delete
  and refuse (Recommended)", because it broke an adopter's scripts against P38's "keeps working, or
  warns"; S4 never blocks the forward.
- **A journal in the working tree**, under `.governance/outbox/`. Every call would dirty the
  adopter's tree, and `update`'s own dirty-path guard reads that tree before every write.
- **Counting landings in the receipt until tags exist**, SA-8's third option. The owner answered
  "First cut release (Recommended)", so the stand-in counts no release rather than a substitute.

## 5. Production-readiness checklist

- security: a forwarder forwards to a path fixed at render and relative to itself, and reads through a policy kit at a path fixed the same way, never one read from the environment or the call; the journal never records arguments, so a secret passed on a command line stays off disk; the prelude reads one policy value, committed at the landed revision and never from the working tree, and nothing else.
- perf / scale: one policy read and one appended line per forwarded call. The read spawns the parent's reader: the shim, a Python start and its git calls from `sh`; the mirror helper's shim and git calls from `js`, which the parent prices near 0.3 s (TOOL-dGroundRules-5 §5, UNVERIFIED); a Python start from `py`. A `py` or `js` forwarder adds one interpreter start of its own, a `sh` one none beyond the `exec`.
- error / empty / loading states: a refused or failed policy read reads `warn` and says so; a refused window read holds every closed row; no git work tree journals nothing and says so; `node` absent makes the `js` fixture exit 2, never a pass; an empty declaration grades zero rows and prints the zero.
- observability: the stderr line under `warn`, the journal line under both modes, and the selfcheck arm's row count.
- risks: a policy kit homed away from `{prefix}/policy/` makes every forwarder read `warn` whatever the adopter set (§8 F7); a forwarder whose target moved again forwards to nothing, which `--check` cannot see and the step gate does, as a vanished member.
- testing: the fixture plants, run by AC3 to AC7 and by the new selftest arm (§7).
- migration: additive; §4 "### Migration".
- user docs: `help/shims.md` and its `help/README.md` line (S9).

## 6. Acceptance criteria

- **AC1** — When `python "tools/govkit/shims.py" --check` runs on the tree after the pass, it exits 0
  and prints `0 row(s)`; when `python "tools/govkit/shims.py" --fixture --plant parity-edit` runs, it
  exits 0, its observation line showing `--check` exit 1 on a forwarder edited by hand.
  Red when: `--check` compares nothing on an edited forwarder, or exits 0 over a closed row whose
  file is still present.
- **AC2** — When `python "tools/govkit/shims.py" --fixture --plant sh` runs, its observation lines
  print the rendered forwarder's first line, its `gov:shim` marker, and its target spelled as a path
  relative to the forwarder's own directory, and it exits 0.
  Red when: the target is written as an absolute or prefix-bound path, so an install at another prefix
  forwards to nothing.
- **AC3** — When `python "tools/govkit/shims.py" --fixture --plant <lang>` runs for each of `sh`, `js`,
  `py` and `module`, each exits 0, its observation lines showing the target's exit 3, the arguments
  `a` and `b c` and the stdin `in` arriving intact, and for `module` the planted import resolving to
  the target's names.
  Red when: a forwarder drops an argument, splits `b c`, loses stdin or exits 0 over the target's 3.
- **AC4** — When `python "tools/govkit/shims.py" --fixture --plant <lang> --mode warn` runs for each
  language, it exits 0 with one stderr line naming both paths and one journal line; `--mode unset`
  and `--mode bogus` observe the same, and `bogus`'s stderr line adds that the policy could not be
  read.
  Red when: an unset key reads as `journal` or as silence, or a refused read blocks the call.
- **AC5** — When `python "tools/govkit/shims.py" --fixture --plant <lang> --mode journal` runs for each
  language, it exits 0 with no stderr line and one journal line, which carries the shim id, both
  paths and the mode and none of the arguments.
  Red when: the `journal` value still prints, or the journal line carries the call's arguments.
- **AC6** — When `python "tools/govkit/shims.py" --fixture --plant window --window <w> --releases <n>`
  runs over each pair below, it exits as the table states, and `--unlanded` with any pair exits 1.
  Red when: a row closes with no release cut, or the count is not compared with the window.

  | `--window` | exits 1 at `--releases` | exits 0 at `--releases` |
  |---|---|---|
  | `0` | `0` | `1` |
  | `1` | `0` | `1` |
  | `2` | `0`, `1` | `2` |
  | `4` | `0`, `3` | `4` |

- **AC7** — When `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import shims; print(shims.read_releases('.'))"`
  runs on the tree, it prints an empty list, and `python "tools/govkit/shims.py" --fixture --plant window --window 0 --releases 0`
  exits 1: every row is held while no release exists.
  Red when: the stand-in reads some tag as a release before dShippedRelease defines one, or window 0
  closes a row with no release cut.
- **AC8** — When `git grep -n -e "check_shim_parity(" -e "check_shim_windows(" -e "shims: " -- tools/govkit/govkit.py`
  runs after the pass, it finds both calls and the row-count line inside `selfcheck`'s arm 11, and
  `python -c "import sys; sys.path.insert(0, 'tools/govkit'); import shims; print(shims.check_shim_windows('.'))"`
  prints an empty finding list over the empty declaration.
  Red when: the arm is not wired into `selfcheck`, or the window check grades a row the declaration
  does not hold.
  permission: the arm's own output is the `govkit selfcheck` leg's, which the main loop reads at the
  close; a build pass observes the wiring and the function directly.
- **AC9** — When `python -c "import tomllib; k = ('install.deprecation-window', 'install.on-shim-call'); print([(r['name'], r['owner'], bool(r.get('summary')), bool(r.get('usage'))) for r in tomllib.load(open( 'tools/policy/catalogue.toml' , 'rb'))['key'] if r['name'] in k])"`
  runs, it prints exactly two tuples, each owned by `dSafePassage` with both flags `True`;
  `python "tools/policy/policy.py" lists --check` exits 0, and `grep -c -e install.deprecation-window -e install.on-shim-call "tools/policy/unsummarised-keys.txt"`
  prints `0`; and `git grep -n -e 'readPolicy("install.on-shim-call"' -e 'read_policy_value("install.deprecation-window"' -- "tools/govkit/shims.py"`
  prints both lines.
  Red when: a key keeps no summary or usage, stays on the list, gains a second row, or loses the
  reader the parent's reader-coverage arm counts.
  fixture: the catalogue and the list are dGroundRules', untracked until it builds, so their paths
  are quoted as its own criteria quote them (TOOL-dGroundRules-1 §6).
- **AC10** — When `git grep -n -e "on-shim-call" -- help/` runs, it finds the page and its line in the
  help index.
  Red when: the forwarders ship with no page under `help/`.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `measure-legs selftest` · `run-gates canary` · `run-gates gov canary` · `memory hygiene` · `policy fixtures` · `spec tokens (a spec's own names resolve)`

dGroundRules' policy legs, `policy check` and `policy fixtures`, run `arm_summaries`,
`arm_mirror_parity`, `arm_mirror_readers` and the reader-coverage arm over this unit's files; they
are named here rather than on the leg line, because neither exists at this spec's base.

New arm: tools/govkit/selftest.py · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · a new arm runs the generator's fixture over every language and mode and every window pair of AC6, asserting each exit · none
New arm: tools/govkit/govkit.py · covers AC8 · selfcheck arm 11, its failing case staged by a fixture declaration holding one `closed = true` row with no release cut · none

## 8. Open questions

- **F1 — Where the forwarders' behaviour is declared.** Options: (a) `[[shim]]` rows in one
  deployer file, rendered by one generator; (b) a field on TOOL-dSafePassage-1's `[[upgrade]]` row;
  (c) hand-written forwarders. (b) changes a grammar the brief's S1 gives to another unit, and (c)
  is §4's first rejected alternative. RESOLVED (agent, 2026-10-23, delegated): (a), rung 3, the
  most feature-rich survivor. widens: none · relaxes: none
- **F2 — How a forwarder reads `install.on-shim-call` in each language.** Options: (a) each reads
  the JSON mirror directly, the bash forwarder shelling to an interpreter for it; (b) the `sh`
  forwarder carries the bash `KEY=value` parser `read_policy_key`, and the
  `py` and `js` forwarders parse the mirror with their stdlib; (c) every forwarder parses the TOML
  file directly; (d) each calls the parent's reader for its language: `policy-shim.sh get` from
  `sh`, `readPolicy` from `js`, `policy.py get` from `py`. (c) misses the resolution order and reads
  the working tree. RESOLVED (agent, 2026-10-24, delegated): (d), rung 1, the parent's landed specs.
  TOOL-dGroundRules-2 S8 keeps that parser `KEY=value` only, with no TOML parse, which rules out (b);
  TOOL-dGroundRules-5 S5 and S9 make `readPolicy` the mirror's one reader and red any other tracked
  code naming the mirror, which rules out (a) and (b); and its non-goals send Python and shell to the
  reader. widens: none · relaxes: none
- **F3 — Where a call is journaled.** Options: under the git directory; under `.governance/outbox/`;
  a user-level directory outside the repository. The outbox dirties the adopter's tree on every
  call, and a user-level path is a new install location, veto 2. RESOLVED (agent, 2026-10-23,
  delegated): the git directory through `git rev-parse --git-path`, rung 3, the place this deployer
  already resolves state that must not dirty a tree (`govkit.py:7046-7063`). widens: none ·
  relaxes: none
- **F4 — What `warn` does beside printing.** v2's row reads "a forwarded call prints and is
  journaled for the adopter view" (v2:1405), and the supersession research's F4 reads "warn
  (prints, and journals for the fleet view)". Options: `warn` prints only; `warn` prints and
  journals. RESOLVED (agent, 2026-10-23, delegated): prints and journals, rung 1, both records
  saying so; `journal` journals and is silent. widens: none · relaxes: none
- **F5 — The parent is unbuilt.** The catalogue rows of S7, the policy file both keys are read from,
  its reader and its JSON mirror are dGroundRules' (`cl-dClosedLoop-0007`, `cl-dClosedLoop-0008`),
  and none has landed. RESOLVED (agent, 2026-10-23, delegated): rung 1, v2's `[chain]` puts
  dGroundRules before this build; the build run re-grounds this spec against the landed parent first,
  spelling the catalogue file, the mirror and each language's reader as the parent ships them.
  widens: none · relaxes: none
- **F6 — How "kept for N releases counted from the first release" counts.** Options: (a) the
  releases cut after the row's landing commit, at least one release existing; (b) releases counted
  from the first release whatever the landing; (c) the window plus one. (b) closes a row landed after
  several releases at once, against "kept for" it. RESOLVED (agent, 2026-10-23, delegated): (a),
  rung 1: a row landed before the first release counts that release as its first, which is SA-8's
  "windows start at the first cut release, every earlier shim held until then". widens: none ·
  relaxes: none
- **F7 — How a forwarder finds the policy kit it reads through.** Options: (a) a path from the
  forwarder's own directory to `{prefix}/policy/`, written at render as `to` is; (b) `resolve_kit_dir`'s
  receipt and probe, the rule TOOL-dGroundRules-9 gives a copy-installed enforcer, with each kit that
  carries a forwarder declaring `requires` on the policy kit; (c) a path read from the environment.
  (c) lets the call's environment choose the code a forwarder runs, a wider surface than §5's
  security line prices, veto 3. (b) exists as Python only: each `py` template would carry the gated
  block, the `sh` template would resolve Python before its read, and JavaScript has no copy, the port
  TOOL-dGroundRules-5 F5 rejected, so `js` would be left a rule of its own to find. (a) is one rule
  for four languages, and its miss, a policy kit homed elsewhere, reads `warn`, the key's default.
  Both meet every criterion, and (a) is tie-broken by fewer open questions and by reuse of S3's own
  render rule. Its miss reads `warn` and forwards, so the pick breaks no adopter's call.
  RESOLVED (owner, 2026-10-24): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft.
- rev-2 · 2026-10-23 · §3 · the Edges gain the ends this unit owes the promotions of the round-1 spec audit's findings, written by the disposal stage: `TOOL-dSafePassage-26`; no other section moved.
- rev-3 · 2026-10-24 · S4 S7 S9 · §3 · §4 · §5 · AC4 AC9 · §7 · §8 F2 F7 · §10 · re-grounded on
  dGroundRules' landed specs by `2026-10-24-build-TOOL-dSafePassage-1-dgroundrules-crosscheck.md`,
  rows 19 to 22 and U5 to U7: S7 fills the two landed rows and drains the list, each forwarder reads
  through the parent's reader, the window through `policy.py get`, the regenerated mirror lands in
  its own second commit, `read_policy_value` lives once in `govkit.py` for specs 6, 9 and 13, with a §3 hands-off edge
  to TOOL-dSafePassage-13, F2
  re-resolved on rung 1, F7 added.
- rev-4 · 2026-10-24 · §8 F7 · the owner resolves F7 to (a), replacing the delegated mark, by
  `2026-10-24-prompt-TOOL-dSafePassage-6-2-spec-writer.md`.
- rev-5 · 2026-10-25 · §3 · the first shim rows drop dOrderedCharter's re-export, which its spec 31's
  `module-export` class row holds by the owner's F6 pick, from Item 4 of
  `2026-10-25-prompt-TOOL-dSafePassage-1-parent-fixes.md`.
- rev-6 · 2026-10-26 · §7 · the leg line names `policy fixtures`, whose guard
  `tools/govkit/govkit.py` from §4 Files touched trips, by
  `2026-10-26-prompt-TOOL-dSafePassage-5-tokens-a-1-spec-writer.md`; no other section moved.

## 10. Reuse audit

No existing seam forwards a moved path, so the generator is new, and it is built on these govkit
seams: `derive_tool_root` and `resolve_prefix_token` (`tools/govkit/govkit.py:154-195`) for `{prefix}`,
`git_path` (`:7046-7063`) for the journal's home, `resolve_remote` (`:558`) for the default branch,
and the engine-row write path an ordinary `update` already takes for changed bytes, which carries a
forwarder to an adopter with no new verb. `reuse_lookup.py "forward a call from a moved script path to
its new location and warn"` ranked path helpers only: `resolve_charter_path` and
`resolve_harness_path` (`tools/roles/roles_lib.py`), `test_routed_path`
(`tools/memory-tree/routed_commits.py`) and `alias_path` (`tools/agent-instructions/adopt-agent-instructions.sh`),
none of which forwards a call; `alias_path` maps a file name to its agent alias and writes nothing at
an old path. The map knows the bash `KEY=value` parser `read_policy_key` and its copies
(`tools/push-main.sh:404`, `tools/run-gates/post-merge.sh:171`, `tools/unattended/unattended.sh:9517`),
which the parent keeps for the legacy homes only, so F2 reads through the parent's readers instead.
`reuse_lookup.py "locate a sibling kit's script from a deployer module and run it as a subprocess"`
ranked `resolve_kit_dir` a seam with 72 installs, inlined in `tools/govkit/govkit.py:196-233`, which
the window's read reuses. Where a record and the source disagree: the supersession research's candidate B
cites "a forwarder that warns" as gov practice in two places, `map_lib`'s re-export and `/unattended`
as a client of `run`, and neither exists in the tree at `3708a705`; both are v2's plans. The recall
probe found the clause, v2's three `[policies]` rows (v2:1404-1406), the away pass's closing review
naming the missing shim unit (`reviews/2026-10-18-review-PLAY-dClosedLoop-1-away-pass-closing.md:58`)
and SA-8's answer.

Recall terms used: `python tools/memory-recall/query.py "how does a moved command or hook path keep working for adopters while they catch up, and how long is the old path kept" --terms "forwarding shim deprecation window on-shim-call moved command hook path module import release warn journal"`
