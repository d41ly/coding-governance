# The policy file, `.governance/policy.toml`

**What it is.** One file holds a repository's policy: one value per key, such as whether a size
cap's breach warns or refuses. The policy kit's catalogue, `tools/policy/catalogue.toml` in this
repository, is the file's schema. It has one row per key, giving the values the key admits, its
default, and the build that owns it. A key the file does not set takes its default.

One reader reads the file: `python tools/policy/policy.py get <key>`, below. No gate or hook reads a
value through it yet. Later dGroundRules units re-point each consumer to it, one at a time, so a
value you set today is checked but changes no behaviour. The one exception is an invalid file, which
the push gate refuses when it has nothing to fall back to, below.

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
  default too.
- **Check the committed file:** `python tools/policy/policy.py check` checks the file as committed at
  `HEAD`, the commit a push lands; `--rev <rev>` checks another commit. It exits 0 with one
  `policy: check · ...` line when the file is valid, missing, or invalid with a valid commit to fall
  back to under `last-valid`, the line saying which, and exits 2 with the refusal otherwise. The
  `policy check` gate runs the same check on every push and landing, so an invalid file with nothing
  to fall back to blocks the push.
- **Check the file:** `python tools/policy/check_policy.py`. It refuses a value outside its key's
  allowed values, an empty set for a key that is never empty, and a key no catalogue row names. Each
  check prints one line with the number it read; a check that read nothing is red too.
- **Start a file in another repository:** `bash tools/policy/adopt-policy.sh --scaffold --target <repo>`.
  It writes the starter file only where none exists. `--check --target <repo>` checks that repository.
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

## The keys the file holds today

| Key | Default | What it sets |
|---|---|---|
| `policy-file.on-invalid` | `last-valid` | what a malformed file or an out-of-set value reads as: the last valid landed revision, or `refuse` |
| `budgets.enforce` | `warn` | whether a size cap's breach warns or refuses, for every cap not pinned |
| `budgets.pinned` | `[]` | the caps that refuse on a breach whatever `budgets.enforce` says |
| `runtime.agents-in-flight` | `6` | how many agents one session may have in flight; at least 1 |

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
