# The policy file, `.governance/policy.toml`

**What it is.** One file holds a repository's policy: one value per key, such as whether a size
cap's breach warns or refuses. The policy kit's catalogue, `tools/policy/catalogue.toml` in this
repository, is the file's schema. It has one row per key, giving the values the key admits, its
default, and the build that owns it. A key the file does not set takes its default.

Nothing reads the file yet. Later dGroundRules units re-point each consumer to it, one at a time, so
a value you set today is checked but changes no behaviour.

The kit README, `tools/policy/README.md`, is the full reference: the row fields, the grammar of
allowed values and every check.

## How to use it

- **Set a key:** a key `a.b.c` is a dotted TOML path, so `budgets.enforce` is written

  ```toml
  [budgets]
  enforce = "refuse"
  ```

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
```

With `runtime.agents-in-flight = 0` in the file, the first line reads `1 finding(s)` and the next
line names the key: `runtime.agents-in-flight: 0 is below the minimum 1`.
