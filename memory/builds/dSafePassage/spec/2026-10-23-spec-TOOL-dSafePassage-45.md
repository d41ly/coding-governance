# TOOL-dSafePassage-45 — the spec audit of units 36 to 42, the step contract's 21 minors: a derived pair count, a credential class over keys and values, a walk by git's own test, declared exits, and the readings that cite them

**Status:** OPEN · rev-1 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 11 · advances TOOL-dSafePassage-14

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dSafePassage-45-deviation-91.md](../build/2026-10-23-build-TOOL-dSafePassage-45-deviation-91.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 36 to 42
(`memory/builds/dSafePassage/reviews/2026-10-23-review-TOOL-dSafePassage-36-37-38-39-40-41-42-spec-audit-round1.md`)
exited CONVERGED with 26 confirmed findings: 2 HIGH, promoted as `TOOL-dSafePassage-43` and
`TOOL-dSafePassage-44`, and 24 minors. BUILD-METHOD M4 batches the minors, and they split into two
disjoint write sets by M6's clauses, so they are two units. This unit is the half whose writes are the
step module, its self-test and its help page: 13 MEDIUM and 8 LOW findings, each by its report id and
each its own scope item, where the report merged ids into one item too. The other half, the lander's
arm, the drift pin and the spec template, is `TOOL-dSafePassage-46`. These minors land on units 7, 26,
36, 37, 38, 39 and 42, so this unit repairs none in particular and builds after every unit, order 11.
Where a minor would bite an earlier pass, the faulted unit's own §3 hands-off bullet to this unit
names it, so that pass may build it; where a finding's defect is the text of a spec built before this
one, the item states the superseding reading, and a criterion here observes it where anything can.

| Report item | Severity | Report ids | Scope items |
|---|---|---|---|
| D-3 | MEDIUM | 1, 7, 14, 24 | S1, S2, S3, S4 |
| D-4 | MEDIUM | 9, 22 | S5, S6 |
| D-5 | MEDIUM | 10 | S7 |
| D-6 | MEDIUM | 19 | S8 |
| D-7 | MEDIUM | 20 | S9 |
| D-8 | MEDIUM | 21 | S10 |
| D-9 | MEDIUM | 3 | S11 |
| D-12 | MEDIUM | 18 | S12 |
| D-13 | MEDIUM | 23 | S13 |
| D-14 | LOW | 4, 26 | S14, S15 |
| D-15 | LOW | 11, 17 | S16, S17 |
| D-16 | LOW | 5 | S18 |
| D-17 | LOW | 6 | S19 |
| D-18 | LOW | 8 | S20 |
| D-19 | LOW | 12 | S21 |

That is 13 MEDIUM and 8 LOW findings by raw id; the report refuted none and left none unverified.
The skeptic re-graded id 1 from high to medium, and REJECTED the finder's fix of id 24, so S4 is built
from the skeptic's corrected fix. D-9 and D-15 share TOOL-dSafePassage-42's lock record and AC7, so
S11, S16 and S17 are one edit.

## 2. Scope (IN)

### The step environment's pair count (D-3)

- **S1** — id 1. TOOL-dSafePassage-37 S3 and AC2 are read as: `GIT_CONFIG_COUNT` equals 3 plus the
  line-ending pairs TOOL-dSafePassage-26 S13 carries, and the pair at index 2 is
  `protocol.ext.allow` = `never`. AC2's probe looks the pair up by key and index and asserts the count
  equals the pairs present, never a bare total. Observed by AC1.
- **S2** — id 7. TOOL-dSafePassage-37 §4 "The step environment's pairs after this unit" is read with
  §4 "The pairs" of this unit: indices 3 and up carry `core.autocrlf` and `core.eol`, each only when the
  parent sets it. Observed by AC1.
- **S3** — id 14. TOOL-dSafePassage-7's AC1 and its §4 table are read with the count derived as S1
  states, and TOOL-dSafePassage-26 S13's "2 plus those pairs" as "3 plus those pairs". The pass that
  lands the third pair edits the order-2 isolation arm in `tools/govkit/selftest.py`, and the "What a
  step can reach" section of `help/upgrade-steps.md` names the third pair in its statement of the step
  environment. TOOL-dSafePassage-37's and TOOL-dSafePassage-26's §3 hands-off bullets to this unit name
  the reading. Observed by AC2.
- **S4** — id 24, the skeptic's corrected fix. At this pass no arm of `tools/govkit/selftest.py`
  asserts a bare `GIT_CONFIG_COUNT` total: each asserts the count equals the `GIT_CONFIG_KEY_<n>` pairs
  present and finds `protocol.ext.allow` by key at index 2. The fixture runs with the parent's
  `core.autocrlf` set and with it unset. Observed by AC1 and AC2.

### The executor and credential keys (D-4, D-5, D-6, D-7, D-8, D-17)

- **S5** — id 9. TOOL-dSafePassage-42 S7's `sendemail.smtpServer` row is read with git-send-email's
  own absoluteness test (`file_name_is_absolute`, `git-send-email:1639-1648` in git 2.54.0.windows.1's
  `libexec/git-core`): a value is refused when it starts with `/` or matches `^[A-Za-z]:`, on every
  platform. Observed by AC3.
- **S6** — id 22. The row covers `sendemail.smtpServer` and `sendemail.<x>.smtpServer`, because
  git-send-email reads `sendemail.$identity` (`:541`) and `git help --config` lists
  `sendemail.<identity>.*`. Observed by AC3.
- **S7** — id 10. For `http.proxy`, `http.<x>.proxy` and `remote.<x>.proxy`, `test_credential_bearing`
  (TOOL-dSafePassage-38 S1) also applies the scheme-optional test
  `(?i)^(?:[a-z][a-z0-9+.-]*://)?[^/\s@]+@` to the value, since git-config gives the value as
  `[protocol://][user[:password]@]proxyhost[:port][/path]`. TOOL-dSafePassage-38 §7's "no URL rule can
  tell from a path" sentence is read as covering only keys whose value can be a path. The `isolation`
  family gains `proxy-schemeless-userinfo`. Observed by AC4.
- **S8** — id 19. The key text the predicate tests is the whole subsection, after the first dot and
  before the last, never its dot-split segments, so a dotted user name such as `first.last` is one
  text. `TOOL-dSafePassage-44`'s exemption reads its scheme inside that subsection. The `isolation`
  family gains `insteadof-dotted-userinfo`. Observed by AC5.
- **S9** — id 20. `render_redacted_config` (TOOL-dSafePassage-38 S2) replaces `<scheme>://` up to the
  last `@` before the first `/`, the pattern `(?i)\b([a-z][a-z0-9+.-]*)://[^/\s]*@`, so a raw `@`
  inside a password is redacted with the rest. The self-test asserts that no substring of a planted
  password longer than two characters appears in the output. Observed by AC6.
- **S10** — id 21. The credential-key table of TOOL-dSafePassage-38 §4 becomes `STEP_CREDENTIAL_KEYS`,
  held to a derivation: every key of `git help --config` whose last segment, lowercased, ends in an
  entry of `CREDENTIAL_KEY_SUFFIXES` matches one row of it, refused or kept with its reason, or a row
  of `STEP_REFUSED_KEYS`. The refused rows gain `imap.pass`, `sendemail.smtpPass`, `gitcvs.dbPass`,
  `sendemail.smtpSSLClientKey`, `sendemail.smtpSSLClientCert` and `receive.certNonceSeed`, with their
  `<x>` forms where git lists one. TOOL-dSafePassage-38 §7 is read with the derivation in place of
  "a key git adds later". Observed by AC7.
- **S19** — id 6. `test_credential_bearing` is the one source of the credential class:
  `STEP_REFUSED_KEYS` carries no `remote.<x>.url`, `remote.<x>.pushurl`, `http.proxy`,
  `remote.<x>.proxy`, `http.sslKey`, `http.sslCert` or `http.cookieFile` row, the rows
  TOOL-dSafePassage-35 S8 adds at order 8. TOOL-dSafePassage-38 S1's "supersedes" is read so.
  **Readers:** by name: READER NOT IN TREE, because `STEP_REFUSED_KEYS` and `test_credential_bearing`
  are minted in `tools/govkit/upgrade_steps.py` by TOOL-dSafePassage-29 and TOOL-dSafePassage-38,
  unbuilt at the base, so no tracked file spells them yet; at their landing the readers are
  `check_target_local_config` and the class arm in `tools/govkit/selftest.py` · by value:
  `check_target_local_config`, whose refused set is unchanged, since the predicate refuses each of
  those rows' keys. Observed by AC11.

### The lock record and its probe (D-9, D-15)

- **S11** — id 3. TOOL-dSafePassage-26 S33's lock record (`2026-10-23-spec-TOOL-dSafePassage-26.md:387`)
  is read as TOOL-dSafePassage-42 S10 spells it:
  `{pid, verb, started, started_utc, started_boot, host, platform, boot_id, pid_ns}`, `started_boot`
  present only where `CLOCK_BOOTTIME` exists (TOOL-dSafePassage-32 S2). TOOL-dSafePassage-26's §3
  hands-off bullet to this unit names it, so its order-6 pass keeps the key TOOL-dSafePassage-32 adds at
  order 4. Observed by AC8.
- **S16** — id 11. TOOL-dSafePassage-42 AC7's "one record writer" is read as an `ast` probe over
  `tools/govkit/govkit.py`: exactly one dict literal carries a `started_utc` key, inside
  `take_write_lock`. The `git grep -n "started_utc"` of that criterion prints a reader and a fixture
  beside the writer at the base (`govkit.py:7404`, `:7430`, `selftest.py:13875`). Observed by AC8.
- **S17** — id 17. The self-test fixture that writes a lock record by hand (`selftest.py:13875` at the
  base, `{"pid", "verb", "started_utc"}`) is a consumer this pass keeps valid against the widened
  record: `describe_write_lock` (`govkit.py:7394`) reads every key with `.get`, so a record holding a
  subset of S11's keys describes without raising. Observed by AC8.

### The repository walk and the submodule map (D-12, D-13)

- **S12** — id 18. TOOL-dSafePassage-36's walk of `<git_dir>/modules/` lists a directory as a
  repository when `git --git-dir=<d> rev-parse --git-dir` exits 0, never because it holds a `config`
  file. It descends only through directories that are not repositories and through each repository's
  own `modules/`, so a ref named `config` and every `objects/` tree are not walked. A `config --list`
  that exits non-zero on a listed repository is a refusal naming it. The `isolation` family gains
  `submodule-ref-named-config` and `submodule-config-malformed`. Observed by AC9.
- **S13** — id 23. TOOL-dSafePassage-42 S22's read is
  `git config -f <worktree>/.gitmodules -z --get-regexp '^submodule\..*\.path$'`: exit 0 maps the
  names it prints, exit 1 maps none and marks every name `by name`, and any other exit is a refusal
  naming the `.gitmodules` file. A nested row is mapped through its parent repository's worktree
  `.gitmodules` when that worktree is populated, and marked `by name` otherwise, its `reached_by`
  joined by `/` as TOOL-dSafePassage-30 §4 says. The `isolation` family gains `gitmodules-malformed` and
  `submodule-nested-name-differs`. Observed by AC10.

### Readings of criteria and records (D-14, D-16, D-18, D-19)

- **S14** — id 4. TOOL-dSafePassage-42's AC3, AC14 and AC15 are read as regression guards, green before
  that unit's pass and not counted as evidence of it, and its S5, S24 and S25 as recorded readings, as
  its S19, S20 and S23 already are. NOT OBSERVED: a reading of how another unit's ledger counts its
  criteria; TOOL-dSafePassage-42's §3 hands-off bullet to this unit carries it to that pass.
- **S15** — id 26. TOOL-dSafePassage-42 AC14's HEAD half is read as
  `grep -c '^BRANCH_PIN = ' tools/govkit/refusal_join.py` printing `1`, never a line number. NOT
  OBSERVED: the criterion is that unit's, observed at its pass under this reading.
- **S18** — id 5. TOOL-dSafePassage-39 S2's caller table is read as a recorded reading, NOT OBSERVED,
  and its "Row before" value `pending` as "none, or `failed` / `rolled-back`", TOOL-dSafePassage-3 S2's
  row states. NOT OBSERVED: no code carries the table; TOOL-dSafePassage-39's §3 hands-off bullet to
  this unit names the reading.
- **S20** — id 8. TOOL-dSafePassage-37 AC1 and its §5 observability are read with the key as git
  prints it, `gc.recentobjectshook`, matched case-insensitively. Observed by AC12.
- **S21** — id 12. TOOL-dSafePassage-38 §10 and §4 "Alternatives rejected" are read with a third
  existing userinfo masker, `derive_redacted` (`tools/run-gates/measure_legs.py:531`, its patterns
  `REDACT_BYTES` and `REDACT_TEXT` at `:527-528`), rejected because its pattern requires a `:` in the
  userinfo, so it misses `https://u@h/r`, and it lives in the run-gates kit. NOT OBSERVED: a reading of
  a reuse record, which no code carries.

## 3. Non-goals (OUT)

- Both highs: `TOOL-dSafePassage-43` and `TOOL-dSafePassage-44`.
- The lander's arm, the drift pin and the spec template: `TOOL-dSafePassage-46`.
- Rewriting a built spec. An item that corrects a built spec's text states the reading here.
- The report's left-shift checklist entries, and a template paragraph for `SPEC_HANDOFF_CUTOFF` and
  `SPEC_CARRIES_CUTOFF`, which the skeptic of id 16 found missing too.

### Edges

- **consumes-from** `TOOL-dSafePassage-7` — `build_step_env`'s pairs, AC1 and its §4 table, which S1 to S4 read with a derived count
- **consumes-from** `TOOL-dSafePassage-26` — S13's line-ending pairs and S33's lock record, which S3 and S11 read
- **consumes-from** `TOOL-dSafePassage-36` — the `modules/` walk, which S12 roots in git's own repository test
- **consumes-from** `TOOL-dSafePassage-37` — S3's third pair, AC1 and AC2, which S1 to S4 and S20 read
- **consumes-from** `TOOL-dSafePassage-38` — `test_credential_bearing`, `render_redacted_config`, its credential-key table and §10, which S7 to S10, S19 and S21 amend and read
- **consumes-from** `TOOL-dSafePassage-39` — S2's caller table, which S18 reads
- **consumes-from** `TOOL-dSafePassage-42` — S7, S10, S22, AC3, AC7, AC14 and AC15, which S5, S6, S11, S13 to S16 amend and read
- **consumes-from** `TOOL-dSafePassage-44` — the ssh-scheme exemption and its plant, which S8's whole-subsection text keeps green

## 4. Design

### The pairs

| Index | Key | Value | Present |
|---|---|---|---|
| 0 | `core.hooksPath` | an empty scratch directory | always (TOOL-dSafePassage-7) |
| 1 | `credential.helper` | the empty string | always (TOOL-dSafePassage-7) |
| 2 | `protocol.ext.allow` | `never` | always (TOOL-dSafePassage-37) |
| 3, 4 | `core.autocrlf`, `core.eol` | the parent's effective value | each only when set (TOOL-dSafePassage-26 S13) |

```
assert env["GIT_CONFIG_COUNT"] == str(count of n with "GIT_CONFIG_KEY_<n>" in env)
assert (env["GIT_CONFIG_KEY_2"], env["GIT_CONFIG_VALUE_2"]) == ("protocol.ext.allow", "never")
```

On node d `core.autocrlf` is `true` at the system and global scopes (read 2026-10-23), so the count
there is 4; on a machine where neither scope sets it, 3.

### The credential predicate after this unit

```
CREDENTIAL_KEY_SUFFIXES = ("pass", "key", "cert", "cookiefile", "seed")
USERINFO        = (?i)\b([a-z][a-z0-9+.-]*)://[^/\s@]+@            # TOOL-dSafePassage-38, per match
PROXY_USERINFO  = (?i)^(?:[a-z][a-z0-9+.-]*://)?[^/\s@]+@          # S7, the three proxy keys' values
REDACT          = (?i)\b([a-z][a-z0-9+.-]*)://[^/\s]*@              # S9
tested texts    = the value, and the subsection: key[first "." + 1 : last "."]   # S8
```

`STEP_CREDENTIAL_KEYS`, the derivation over git 2.54.0.windows.1's `git help --config` on node d,
2026-10-23 (PINNED that date; 17 of 1005 keys end in a suffix):

| Key | Row |
|---|---|
| `http.sslKey`, `http.sslCert`, `http.cookieFile`, `http.proxySSLKey`, `http.proxySSLCert`, each with its `http.<x>.` form | refused, any value (TOOL-dSafePassage-38) |
| `imap.pass`, `gitcvs.dbPass`, `receive.certNonceSeed` | refused, any value (S10) |
| `sendemail.smtpPass`, `sendemail.smtpSSLClientKey`, `sendemail.smtpSSLClientCert`, each with its `sendemail.<x>.` form | refused, any value (S10) |
| `core.askPass` | a `STEP_REFUSED_KEYS` row already (TOOL-dSafePassage-29) |
| `user.signingKey`, `http.pinnedPubkey` | kept: a public key or its id |
| `interactive.singleKey`, `http.sslAutoClientCert` | kept: a boolean |
| `trailer.<x>.key` | kept: a trailer's name |

### The walk's repository test

```
walk(d):                                     # d starts at <git_dir>/modules/
  for c in subdirectories of d:
    if git --git-dir=c rev-parse --git-dir exits 0:   list c; walk(c/modules)
    else:                                             walk(c)       # a name segment, never a ref
```

This unit's probe on node d, 2026-10-23, in a scratch repository under `%TEMP%` with a branch named
`config`: `.git` exits 0 and `.git/refs/heads` exits 128.

### The `.gitmodules` read

| Exit | Meaning | Outcome |
|---|---|---|
| 0 | the file maps names | each name's `reached_by` is its path |
| 1 | the file is missing or maps none | every name is marked `by name` |
| any other | the file does not parse, `fatal: bad config line <n>` | a refusal naming the file |

This unit's probe on node d, 2026-10-23: a well-formed file exited 0, an unterminated section 128, and
a missing file and a file with no `submodule.*.path` key 1.

### Inventory

Minted in `tools/govkit/upgrade_steps.py`: the constants `CREDENTIAL_KEY_SUFFIXES` and
`STEP_CREDENTIAL_KEYS`, the name TOOL-dSafePassage-38's table takes; the plants
`proxy-schemeless-userinfo`, `insteadof-dotted-userinfo`, `submodule-ref-named-config`,
`submodule-config-malformed`, `gitmodules-malformed` and `submodule-nested-name-differs`. No function,
conf key, gate leg or policy key. S12's and S13's refusals and S10's rows use TOOL-dSafePassage-24's
one `raise Refusal` site, so `tools/govkit/refusal_join.py`'s `BRANCH_PIN` does not move.

### Migration

None: no landed step row, lock record or receipt step exists before this build lands.

### Rollout

Live at landing. It builds at order 11, after every unit of the build, `TOOL-dSafePassage-44` (order
10) included. Its write set, `tools/govkit/upgrade_steps.py`, `tools/govkit/selftest.py` and
`help/upgrade-steps.md`, does not meet `TOOL-dSafePassage-46`'s, neither writes a file the other reads
as a contract or an acceptance input, and neither writes a shared mutable record, so the two passes at
order 11 run concurrently (M6).

### Files touched (estimate)

- `tools/govkit/upgrade_steps.py`
- `tools/govkit/selftest.py`
- `help/upgrade-steps.md`

### Alternatives rejected

- **One batch for all 24 minors.** M6's three clauses hold between this half and
  `TOOL-dSafePassage-46`'s, so M4 admits two units, and one unit would sequence work that can run at once.
- **Listing the six credential keys as instances (S10).** The report's own fallback; the next key git
  adds with a secret suffix would pass, the class-as-a-list defect TOOL-dSafePassage-38 rejects.
- **Typing each machine's pair count (S4).** The count depends on the parent's config, so a literal
  passes on one machine and reds on another.
- **Folding each minor into its unit's spec.** The disposal promotes, never folds (BUILD-METHOD M4).

## 5. Production-readiness checklist

- security: S7, S8 and S10 widen the credential class to scheme-less proxy values, dotted user names
  and six more secret keys; S9 stops a partial password printing; S12 reads a config only from a
  directory git recognises as a repository.
- perf / scale: S12 adds one `rev-parse` per directory under `modules/` that sits outside a repository,
  and walks no `objects/` tree.
- error / empty / loading states: S12's and S13's failed reads are refusals naming their file, never a
  crash or a silent `by name`.
- observability: each refusal names the key as git prints it, redacted, and its file.
- risks: S10 refuses a target whose config stores `sendemail.smtpPass` or `imap.pass`, which a
  credential helper replaces; S7 refuses a proxy value written as `user@proxy` with no password, since
  the user name alone may be a token.
- testing: the probes and plants of §6, through §7's arm.
- migration: none.
- user docs: `help/upgrade-steps.md` (S3, S7, S10).

## 6. Acceptance criteria

- **AC1** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path and calls
  `build_step_env` from a scratch directory outside any repository, with `GIT_CONFIG_NOSYSTEM=1` and
  `GIT_CONFIG_GLOBAL` naming a scratch config that sets `core.autocrlf=true`, `GIT_CONFIG_COUNT` is `4`,
  index 2 is `protocol.ext.allow` = `never` and index 3 is `core.autocrlf`; with an empty scratch config
  the count is `3`; in both, the count equals the `GIT_CONFIG_KEY_<n>` pairs present.
  Red when: the count is asserted or built as a bare total, or the third pair moves off index 2.
  figure: DERIVED from the scratch config at observation.
- **AC2** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation` runs under each of AC1's
  two scratch configs, both runs exit 0 and print `clean` as `ok`; and
  `git grep -n -e "protocol.ext.allow" -- help/upgrade-steps.md` prints a line of the "What a step can
  reach" section.
  Red when: the order-2 isolation report holds a bare count that one of the two configs breaks.
- **AC3** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path, `STEP_REFUSED_KEYS`
  refuses `sendemail.smtpserver` valued `/usr/bin/x`, `C:/x/sendmail.exe` and `c:evil`, and
  `sendemail.work.smtpserver` valued `/x`; it does not refuse `sendemail.smtpserver` valued
  `smtp.example.com`.
  Red when: a drive-letter value or the identity form passes, or a host name is refused.
- **AC4** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant proxy-schemeless-userinfo`
  runs, its `http.proxy = dspuser45:dsppass45@proxy:3128` is refused naming `http.proxy` and
  `.git/config`, neither planted token appears in stdout or stderr, and the run exits 1; and a probe
  of `test_credential_bearing` holds False for `("http.proxy", "proxy:3128")`.
  Red when: a scheme-less proxy credential passes, or a plain proxy host is refused.
- **AC5** — When the same family runs with `--plant insteadof-dotted-userinfo`, whose key is
  `url.https://first.last:dsppass45@host/.insteadof`, the step is refused, the password is absent from
  the output and the run exits 1; and `test_credential_bearing("url.https://first.last:pw@host/.insteadof", "https://h/")`
  holds True while `TOOL-dSafePassage-44`'s `url.ssh://git@github.com/.insteadof` case still holds False.
  Red when: a dotted user name splits the userinfo and passes.
- **AC6** — When a probe calls `render_redacted_config("http.https://u:p@ss@h/.sslkey")`, it returns
  `http.https://<redacted>@h/.sslkey`; and every plant of this unit and of TOOL-dSafePassage-38 run
  through the family prints no substring of its planted password longer than 2 characters.
  Red when: the tail of a password holding `@` prints.
- **AC7** — When `git help --config` runs on node d and a `python -c` probe applies
  `CREDENTIAL_KEY_SUFFIXES` to it, every kept key matches one row of `STEP_CREDENTIAL_KEYS` or of
  `STEP_REFUSED_KEYS`; with the `imap.pass` row taken out of a copy of `STEP_CREDENTIAL_KEYS` the probe
  names `imap.pass`; and `test_credential_bearing("sendemail.smtppass", "x")` holds True while
  `("user.signingkey", "ABCD")` holds False.
  Red when: a secret-suffixed key matches no row, or a public key id is refused.
  figure: the kept count is DERIVED; 17 was read on node d on 2026-10-23.
- **AC8** — When a `python -c` probe calls `take_write_lock` with `read_boot_clock` stubbed to a float
  and `read_pid_namespace` to `pid:[4026532221]`, the record's keys are S11's set; an `ast` walk of
  `tools/govkit/govkit.py` finds exactly one dict literal with a `started_utc` key, inside
  `take_write_lock`; and `describe_write_lock` over a file holding
  `{"pid": 999999, "verb": "apply", "started_utc": "2026-01-01T00:00:00Z"}` returns a line naming pid
  `999999`.
  Red when: the record drops `started_boot`, a second writer spells the record, or the reader raises on
  a subset.
- **AC9** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant submodule-ref-named-config`
  runs, its population holds one row per real repository, none under `refs/` or `logs/`, and the run
  exits 0; `--plant submodule-config-malformed` is refused naming that repository's config file and
  exits 1.
  Red when: a ref named `config` becomes a population row, or a failed read is skipped.
- **AC10** — When the same family runs with `--plant gitmodules-malformed`, the step is refused naming
  the `.gitmodules` file and the run exits 1; with `--plant submodule-nested-name-differs` the nested
  row's refusal reads `(submodule <outer path>/<inner path>)`, and with the outer submodule
  unpopulated it reads the inner name with `by name`.
  Red when: a malformed `.gitmodules` crashes the check, or labels every name `by name`.
- **AC11** — When a `python -c` probe imports `tools/govkit/upgrade_steps.py` by path,
  `STEP_REFUSED_KEYS` holds no row whose pattern is `remote.<x>.url`, `http.sslKey` or
  `http.cookieFile`; and `--plant local-url-userinfo` of TOOL-dSafePassage-35 is still refused.
  Red when: the credential class has a second source in the refused table.
- **AC12** — When `python3 "tools/govkit/upgrade_steps.py" fixture isolation --plant local-recent-objects-hook`
  runs, its refusal line holds `gc.recentobjectshook`, matched case-insensitively, and `.git/config`.
  Red when: the refusal re-cases the key git printed.

## 7. Gates

`govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `govkit selfcheck` · `recall floor arms` · `encoding posture (text IO names its encoding)` · `lexicon naming predicates` · `spec tokens (a spec's own names resolve)`

New arm: tools/govkit/selftest.py · covers AC1 AC4 AC5 AC6 AC7 AC9 AC10 · the self-test runs the derived pair count under both configs, the six plants and the credential class arm, its failing cases staged by an environment copy asserting `3`, a predicate copy that splits the key on dots, a table copy missing `imap.pass` and a walk copy that lists any directory holding `config` · none

What the check does not cover: a credential stored in a key no `git help --config` row names and no
suffix reaches, and a `.gitmodules` that parses but maps a name to a path outside the worktree.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, the batch of the spec audit of units 36 to 42's 13 MEDIUM and 8
  LOW findings of the step contract, one scope item per raw id.

## 10. Reuse audit

The seams extended are named per item: TOOL-dSafePassage-7's `build_step_env`, TOOL-dSafePassage-29's
class arm and tables, TOOL-dSafePassage-38's predicate and redactor, TOOL-dSafePassage-36's walk,
TOOL-dSafePassage-42's `.gitmodules` read, all specced and unbuilt at the base, and
`describe_write_lock` and `take_write_lock` (`tools/govkit/govkit.py:7394`, `:7409`).
`python tools/codebase-map/reuse_lookup.py "a credential key class derived from git config listing"`
ranked `git`, `key`, `keys` and `read_conf_key`, name-token matches, so no existing seam fits beyond
those specs. The credential set was derived from `git help --config` on node d, and the absoluteness
rule read from the shipped `git-send-email`, not from a record. Where the report and the source
disagreed: `derive_redacted` is defined at `measure_legs.py:531`; the report's `:527` is
`REDACT_BYTES`.

Recall terms used: `python tools/memory-recall/query.py "how a spec audit's minor findings are batched and their readings carried to the faulted unit" --terms "spec audit minors batch promoted reading hands-off consumes-from order disposal rescope severity"`
