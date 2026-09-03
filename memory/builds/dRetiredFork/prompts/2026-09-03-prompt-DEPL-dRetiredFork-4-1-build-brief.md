# Build brief — DEPL-dRetiredFork-4

**Serves:** journal DEPL-dRetiredFork-4

## The crash, and why it is worse than a refusal

`apply`'s renormalize step passes every lf-pinned path as argv and blows the 32 KiB Windows command
line: `FileNotFoundError: [WinError 206]`, measured on inCMS whose `.gitattributes` is 28 KB.

It fires AFTER the write loop and AFTER configure, so the target is left with new files staged, a
conf scaffolded, a Skill rendered, a stale write lock under its governance dir, and no receipt
update — a half-applied install from a verb that reported nothing.

## The CLASS, enumerated by grep rather than memory

AC2b is the criterion rev-2 added because rev-1 fixed only the reported call site. Five sites
concatenate a derived population into a git argv:

- `:4349` — `add --` + `staged` (apply's staging; grows with the install)
- `:4512` — `diff --name-only HEAD --` + `lf_paths` ← **the reported crash**
- `:4521` — `add --renormalize --` + `lf_paths`
- `:4525` — `ls-files --eol --` + `lf_paths`
- `:6416` — `rm -q --ignore-unmatch --` + `deleted` (update's withdrawals)

`index_read` is NOT in the class and is named so the enumeration is complete rather than convenient:
it already chunks at 400 paths, which is a different mitigation for the same bound.

## The mechanism

`--pathspec-from-file=-` with `--pathspec-file-nul`, fed over stdin. That removes the bound rather
than raising it — a chunking loop would leave the same class open at a larger size, and the failure
would then be rarer and harder to attribute.

NUL-separated because a path may contain anything but NUL, and the newline form would split a path
with a newline in its name into two pathspecs that match nothing.

## The arm

S3 wants a pathspec exceeding 32 KiB constructed and the command observed to SUCCEED — and observed
RED first against the current code, or it is an assertion about nothing.
