# The policy file, `.governance/policy.toml`

**What it is.** One file holds a repository's policy: one value per key, such as whether a size
cap's breach warns or refuses. The policy kit's catalogue, `tools/policy/catalogue.toml` in this
repository, is the file's schema. It has one row per key, giving the values the key admits, its
default, and the build that owns it. A key the file does not set takes its default.

One reader reads the file: `python tools/policy/policy.py get <key>`, below. Two families of keys
have consumers so far: `runtime.agents-in-flight`, the agent limit, which `policy.py settings
--write` renders into the harness's settings and the agent-cap hook holds them to ([the agent
limit](agent-limit.md)); and `budgets.enforce`, `budgets.pinned` and `budgets.<cap>`, which every
gate that enforces a size cap reads ([the size caps](size-caps.md)). Later dGroundRules units
re-point each other consumer, one at a time, so a value you set for any other key today is checked
but changes no behaviour. The one exception is an invalid file, which the push gate refuses when it
has nothing to fall back to, below.

The kit README, `tools/policy/README.md`, is the full reference: the row fields, the grammar of
allowed values and every check.

## How to use it

- **Set a key:** a key `a.b.c` is a dotted TOML path, so `budgets.enforce` is written

  ```toml
  [budgets]
  enforce = "refuse"
  ```

- **Read a key:** `python tools/policy/policy.py get budgets.enforce` prints the key's value: a
  string as itself, a number or `true`/`false` as TOML spells it, a list one member per line. It
  reads the file **as committed at the landed revision**: the tip of the remote's default branch,
  or, in a clone with no remote, your local `main`. It never reads your working tree, so an edit
  you have not committed and pushed does not change what it prints, and once a gate reads its
  policy through it, an uncommitted edit cannot change what that gate enforces.
  - `--rev <rev>` reads the file at that commit instead, `--rev HEAD` for your last commit.
  - `--explain` adds one line on stderr naming where the value came from and the commit:
    `policy: budgets.enforce · file · set in .governance/policy.toml at 3708a705, <remote>/main, the landed revision`.
  - It refuses, exit 2 with one `policy: refused · <path>:<line> · <why>` line, a key no catalogue
    row names, a string that is not one TOML key, a revision that names no commit, an invalid file
    it cannot fall back from (below), and a key whose catalogue row carries no default when the
    file does not set it.
  - With several remotes and none chosen it refuses too: `export GOV_REMOTE=<remote>` names one.
  - The file is parsed as TOML and never run, so a line in it cannot execute anything.
- **Where a value comes from:** every key resolves in one order, `RESOLUTION_ORDER` in
  `tools/policy/policy.py`: the value the file sets, else the catalogue default. `--explain` says
  which, after the sha and how the revision was found:
  - the file sets the key: `file · set in .governance/policy.toml at <sha>, <how>`;
  - the file does not set it: `default · not set in .governance/policy.toml at <sha>, <how>; the catalogue default`;
  - there is no file at that revision: `default · .governance/policy.toml is absent at <sha>, <how>; the catalogue default`.

  A file that names a `preset` reads the catalogue default too, for now: the reason adds
  `; the file names preset <name>, not applied until dKeptSession adds presets to this reader`.
  A value you set in the file always wins over the default.
- **When the file is invalid:** a file that is not TOML, sets a value outside its key's allowed
  values, or sets a key no catalogue row names is invalid, and an invalid file NEVER reads the
  catalogue defaults, because a default may be looser than what you chose. `policy-file.on-invalid`
  decides what it reads instead, and it is itself read from the last valid revision of the file,
  never from the invalid one, so an out-of-set value of it is one more problem:
  - `last-valid` (the default): every key reads the newest earlier commit whose file was present and
    valid, the whole file and never one key, with source `last-valid` and a reason naming the
    invalid commit, the line, the problem and the valid commit. With no valid commit before it, the
    read refuses, naming the line.
  - `refuse`: every read refuses, naming the invalid file's line.

  A missing file is not invalid: every key reads its default. A key the file does not set reads its
  default too, except a key whose catalogue default is prose, `{ derived = "..." }`: no reader
  computes it yet, so `get` refuses it, naming the row, until the file sets the key. A file saved in
  another encoding than UTF-8, as a PowerShell redirect writes it, is invalid, and a clone too
  shallow to reach a valid commit refuses saying `history is shallow`; fetch more history.
- **Check the committed file:** `python tools/policy/policy.py check` checks the file as committed at
  `HEAD`, the commit a push lands; `--rev <rev>` checks another commit. It exits 0 with one
  `policy: check · ...` line when the file is valid, missing, or invalid with a valid commit to fall
  back to under `last-valid`, the line saying which, and exits 2 with the refusal otherwise. The
  `policy check` gate runs the same check on every push and landing, so an invalid file with nothing
  to fall back to blocks the push.
- **Check the file:** `python tools/policy/check_policy.py`. It refuses a value outside its key's
  allowed values, an empty set for a key that is never empty, and a key no catalogue row names. Each
  check prints one line with the number it read; a check that read nothing is red too, unless reading
  nothing is a legal state, no policy file yet, no tracked code, no owner build landed, or no landed
  revision yet, which it prints as `not graded`.
- **Start a file in another repository:** `bash tools/policy/adopt-policy.sh --scaffold --target <repo>`.
  It writes the starter file only where none exists, then renders the harness settings from the agent
  limit and the policy mirror wherever the repository has a commit, so the first agent spawn passes
  and the merge bar finds the mirror fresh. The mirror renders a commit, so run it again once the
  policy file is committed. `--check --target
  <repo>` checks that repository.
- **See which keys are documented:** a catalogue row with no `summary` or no `usage` is named on
  `tools/policy/unsummarised-keys.txt`. That list may only shrink. To document a key, give its row a
  `summary` and a `usage`, then run `python tools/policy/policy.py lists --write` to drain it from the
  list. `python tools/policy/policy.py lists --check` reds a list that grew past the one the default
  branch carries.
- **Know which keys are loop bounds or deadlines:** raising one loosens the policy, so its catalogue
  row says so with `direction = "raise-loosens"`. A row is one when its allowed values are a retry,
  round or route-back count, or a number of hours, days or seconds. The check reds such a row that
  says nothing, and any row with another `direction`. Adding a new key of one of those kinds? Give
  its row `direction = "raise-loosens"`.

## Every key whose build has landed has a reader

Each catalogue row names the build that owns the key. Once that build has landed, a key no code
reads is a setting you can change to no effect, so `python tools/policy/check_policy.py` reds it:

```
reader coverage: budgets.enforce (owner dGroundRules, landed at 3708a705) has no reader
```

- **Landed** means: on the default branch as `policy.py get` reads it, the build's folder
  `memory/builds/<owner>/spec/` holds at least one spec and every spec there is `CLOSED` or
  `WONTDO`. A build whose specs are still `DEFERRED` or open has not landed, and your working tree
  never counts: only what is committed on the default branch does.
- **A reader** is a line of tracked code that passes the key to the policy reader, in one of two
  shapes: a call whose first argument is the key in quotes, such as `resolve("budgets.enforce")` in
  Python or `mirror.get('budgets.enforce')` in JavaScript, or `policy.py get budgets.enforce` in a
  shell script or a git hook. A comment, a test file, a help page, the memory tree, the JSON mirror
  and the catalogue never count. For a key with a `*` or `<name>` part, such as `budgets.*`, a
  variable in that part counts too: `policy.py get "budgets.$cap"`, or a quoted part holding the
  variable, `resolve(f'budgets."{cap}"')`.
- **To clear it,** do one of two things: add the reader, a call of that shape where the code uses the
  value; or, if the key's build has not really landed, make the row's `owner` a build that has not
  landed yet.
- **Every run says what it graded:** `reader coverage: graded <n> of <m> catalogue key(s); landed
  owners: <builds>`, and while no owner build has landed,
  `reader coverage: graded 0, so this arm checked nothing at <commit>`, which passes.
- **What it does not see:** a reader in another language, or one that builds the key's name at run
  time from pieces, reds as unread; a call that only mentions the key, in a message say, counts as a
  reader.

## Who may change the policy file

An agent that could commit any change to the policy file could loosen any rule, so this repository's
pre-commit hook guards four paths, listed in `tools/policy/guarded-paths.txt`:

- `.governance/policy.toml`, the policy file;
- `.governance/policy.json`, its JSON mirror;
- `.governance/instructions.toml`, the instruction manifest;
- `.governance/deploy.toml`, the deployer's answers.

- **The owner commits from a terminal.** A commit made at a terminal is the owner's proof, and the
  hook admits it, printing `policy guard — <paths> staged, admitted on the owner's terminal proof.`
  An agent's shell has no terminal, so the hook judges its commit instead.
- **An agent may change the policy file one way: raise one measured-file cap.** One key under
  `[budgets]` whose name is the path of a tracked file, set to a larger whole number, and nothing
  else in the four files changed. The commit must carry its argument and its record:
  - comment lines added directly above the cap, one of them `RAISED <old> -> <new>`;
  - at least one row added to `memory/DECISIONS.md`, with no row removed.

  Other files may ride in the same commit: a raise belongs in the commit of the unit whose change
  needed it. Worked example, raising the cap on `AGENTS.md` from 20480 to 24576:

  ```toml
  [budgets]
  # RAISED 20480 -> 24576, 2026-10-24, TOOL-x-1: the new role section measured 21900 bytes
  "AGENTS.md" = 24576
  ```

  with a row such as `- TOOL-x-1 · AGENTS.md cap 20480->24576: the role section needs it` added to
  `memory/DECISIONS.md`. The hook prints
  `policy-guard: admitted · budgets."AGENTS.md" 20480 -> 24576 · its change record attached`.
- **An agent may also commit the mirror it regenerated, in a commit of its own.** A change to the
  policy file or to `tools/policy/catalogue.toml` leaves the mirror stale, so it takes two commits:
  first the policy or catalogue change, then `python tools/policy/policy.py mirror --write` and a
  commit of `.governance/policy.json` with neither of those two files staged beside it. The hook
  renders the mirror at `HEAD` itself and admits the staged one only when its bytes are that render,
  printing `policy-guard: admitted · .governance/policy.json · equals its render at HEAD`.
- **Everything else is refused**, each reason on its own `policy-guard: refused · <path> · <why>`
  line: a lowered cap, two caps changed, a cap added or removed, a class row such as
  `memory/builds/*/spec/` (it names no one file), `budgets.enforce` or `budgets.pinned`, any other
  key, a raise missing its `RAISED` line or its decision row, another line of the file changed, and
  any change to the instruction manifest or the deployer's answers. A mirror staged beside a change
  to any file it is rendered from, the policy file, the catalogue or `.agent-cap.conf`, is refused
  with `the mirror renders HEAD and its input <path> is staged changed: commit <path> first, then
  regenerate`; one that is
  not its render, a hand edit say, with `differs from its render at HEAD`. Unstage it with
  `git restore --staged --worktree .governance/policy.json`; the landing renders it too.
- **A merge that takes one side's file** writes nothing new and is admitted; a merge that writes a
  third text is judged like any other change.
- **What the guard does not catch.** It stops forgetting, not evasion: `git commit --no-verify`, a
  wrapper that gives an agent's commit a terminal, a line removed from the list in one commit and the
  file changed in the next, a commit made in another clone, a cherry-pick or a rebase (no pre-commit
  runs), and the guard file deleted from the working tree all pass it. The hook binds once it is on
  `main` in the primary checkout, whose hooks every worktree runs. The push gate does not re-check
  who made a change.

## The keys the file holds today

| Key | Default | What it sets |
|---|---|---|
| `policy-file.on-invalid` | `last-valid` | what a malformed file or an out-of-set value reads as: the last valid landed revision, or `refuse` |
| `budgets.enforce` | `warn` | whether a size cap's breach warns or refuses, for every cap not pinned |
| `budgets.pinned` | `[]` | the caps that refuse on a breach whatever `budgets.enforce` says |
| `runtime.agents-in-flight` | `6` | how many agents one session may have in flight; at least 1 |

## The policy that still lives elsewhere

Some policy has not moved into `.governance/policy.toml` yet. It lives in three older places: the
kit settings files at the repository root (`.unattended.conf`, `.memory-tree.conf` and the other
`.*.conf` files), the gate settings file `.githooks/gate-env.sh`, and the roles kit's
`house/policy.toml`. `tools/policy/legacy-homes.txt` lists every key those places hold. It is
generated, never typed: `python tools/policy/policy.py lists --write` writes it.

The list is coding-governance's own and is never installed into another repository. There the policy
check prints `arm_legacy_homes · not graded · the list is gov's own and is withheld from installs; …`,
even if that repository writes a list of its own, and `lists --write` does not create the file. The
deployer's `plan` shows the list as an `ORDER [project-owned]` row: that row is for information, and
the list is not yours to write.

- **A row** is `<place> <key> <mark>`, for example `.unattended.conf REVIEW_ROUNDS owner-policy`. The
  roles file's place is written `<tool-root>/roles/house/policy.toml`, which means the roles kit
  wherever this repository installed it, and its keys are its tables, `[effort]` and `[gates]`.
- **The marks.** `owner-policy` is a choice the owner makes, which a later build moves into
  `.governance/policy.toml`. `mechanic` is plumbing that stays where it is, such as which Python the
  hooks use. Every settings-file and roles-file key is `owner-policy`; a gate settings key takes the
  mark `GATE_ENV_MARKS` in `tools/policy/policy.py` gives it, and a key that table does not name is
  `unmarked`, which `lists --check` reds until someone adds it there.
- **Left off on purpose:** a settings key ending `_CUTOFF` or `_PIN`, which a later build converts
  rather than moves.
- **The list only shrinks.** `python tools/policy/policy.py lists --check` compares it with the places
  it is read from and with the copy on the default branch. Removed a key from its place? The check
  says `stale list at <row>`; run `lists --write` and the row goes. Added a key? The check says
  `<place> <key> is a new legacy home and the list is shrink-only`, and `lists --write` refuses to add
  it. Do not add the key to the old place: carry it as a key in `tools/policy/catalogue.toml`
  instead. A row typed into the list by hand reads `typed row <row>`.

## Example

```bash
python tools/policy/check_policy.py
# policy-check: arm_schema · 0 finding(s) · 4 key(s) of .governance/policy.toml against 267 row(s)
# policy-check: arm_shape · 0 finding(s) · 267 row(s), 19 set-valued, 10 never-empty
# policy-check: arm_summaries · 0 finding(s) · 263 of 267 row(s) unsummarised · ...
# policy-check: arm_direction · 0 finding(s) · 19 loop bound and deadline row(s)
# policy-check: arm_on_invalid · 0 finding(s) · .governance/policy.toml at 7c8c0c4f is valid
```

With `runtime.agents-in-flight = 0` in the file, the first line reads `1 finding(s)` and the next
line names the key: `runtime.agents-in-flight: 0 is below the minimum 1`.
