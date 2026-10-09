**Serves:** diff-review TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1

# aLevelledCopy — Tier-2 CLOSING DIFF review, round 1

*Node `a`, 2026-10-09. This report is the synthesis pass of the `tier2-review` workflow over build
aLevelledCopy. The build is unattended, and its owner prompt is
`memory/builds/aLevelledCopy/prompts/2026-10-09-prompt-TOOL-aLevelledCopy-1.md`. Four units were
reviewed against their specs under `memory/builds/aLevelledCopy/spec/`. The receipt-sync leg grades
eol-only rows through the clean filter (TOOL-aLevelledCopy-1). check-wiring derives and sets the SSH
keepalive (TOOL-aLevelledCopy-2). check-wiring grades the index mode of the hooks (TOOL-aLevelledCopy-3).
govkit carries the exec bit upward on engine rows (DEPL-aLevelledCopy-1).*

**Range reviewed: `ce9192c0ba180a67b49b2ea3fc8edf2fb8afc0cb...bb6178eab4ef9bfc9b603398e1258119873b47b5`**

**Round: 1.**

## Verdict: CLEAN WITH FIXES

The review found no blocker and one high. That high is the ssh arm overriding an operator's
`GIT_SSH`, and it happens unattended at every SessionStart. Fix it before this build lands in an
adopter. Every other finding is contained: some are false reds on unusual hosts, some are coverage
gaps, and some are records out of step with the code.

Adjudicated tally by raw confirmed finding: 0 blocker, 1 high, 8 medium, 6 low (15). By report item:
0 blocker, 1 high, 7 medium, 5 low (13 items). The items and the raw counts differ because two
merges happened within a single binding grade. Ids 4 and 12 merge into one medium item, and ids 5
and 10 merge into one low item.

**Review shape:** intensity full, raw 19, confirmed 15, refuted 4, unverified 0 (0 uncertain), precision 0.79.

| lens | returned | raw | confirmed | refuted | uncertain | unverified | precision |
|---|---|---|---|---|---|---|---|
| security | yes | 2 | 0 | 2 | 0 | 0 | 0.00 |
| correctness | yes | 3 | 3 | 0 | 0 | 0 | 1.00 |
| seams | yes | 6 | 5 | 1 | 0 | 0 | 0.83 |
| verification | yes | 4 | 4 | 0 | 0 | 0 | 1.00 |
| intent | yes | 4 | 3 | 1 | 0 | 0 | 0.75 |

**Run integrity.** All 5 of 5 lenses returned, and none died. All 5 of 5 skeptic batches returned,
and none died. No contradictory verdict was demoted to unverified, no spurious verdict was discarded,
and there were no duplicates. Of the fixes on confirmed findings, 14 were judged sound, 1 was judged
UNSOUND (id 7), none lacked a proposal and none went unjudged. On severity, no confirmed finding was
left ungraded by the skeptic, and 2 were re-graded (ids 6 and 7, both from high to medium). There were
no unverified findings, so none was answered UNCERTAIN and none lacked a usable verdict. Every count
above is zero where a zero is clean, so the finding set is complete for the lenses that ran. No lens
notes were supplied, so every lens ran on the kit's generic brief. Intent was read from 5 spec
documents beside the range's commit messages. The 37-item checklist was split across the lenses as
security 8, correctness 8, seams 7, verification 7 and intent 7. By-design items came from the
caller's byDesign list.

**Security model the lenses were fed.** check-wiring runs at every SessionStart (`--session`). It must
never execute an operator-configured value, and it must never overwrite operator config.
`core.sshCommand` becomes the command git runs for SSH, so its source, a tracked kit file, is the trust
boundary. govkit update writes into an adopter's index and must not write anything beyond engine rows.
The two security-lens findings (ids 1 and 2) were both refuted. Their reasons are in the appendix.

## Blockers

None.

## High

### H1 — the ssh arm overrides an operator's `GIT_SSH` (id 3)

- **Where:** [tools/check-wiring.sh:1336](../../../../tools/check-wiring.sh)
- **Defect:** `check_ssh_keepalive` decides that "no scope sets it" by running
  `git config --show-scope --get core.sshCommand` and nothing else. git's connect.c resolves the SSH
  program in this order: `GIT_SSH_COMMAND` (env), then `core.sshCommand` (config), then `GIT_SSH` (env).
  A repo-local `core.sshCommand` therefore outranks the operator's `GIT_SSH`.
- **Impact:** Suppose a Windows node's operator chose PuTTY/plink in the Git for Windows installer,
  which sets `GIT_SSH=...plink.exe`, or pointed `GIT_SSH` at Windows OpenSSH. At every SessionStart,
  that node gets `core.sshCommand='ssh -o ...'` written. From then on git runs the bundled OpenSSH,
  which cannot see Pageant or the Windows agent, so pushes can fail authentication. This happens
  unattended and breaks the arm's own rule that operator config is never overridden. `--check` also
  prints a Fix line that tells the operator to make the same breaking change. The header (lines 42-45)
  names only `GIT_SSH_COMMAND` as unchecked.
- **Fix (judged SOUND by the skeptic):** Before the set branch and the UNWIRED branch, treat a
  non-empty `${GIT_SSH:-}` as an operator value. Print
  `note ssh — GIT_SSH is the operator's ...; NOT setting core.sshCommand, which would override it`,
  and write nothing and count nothing. Optionally, also skip when `git config ssh.variant` is set.
- **Left-shift gate:** Add an LC2 arm to `tools/check-wiring.test.sh` that exports
  `GIT_SSH=/bin/false` with an ssh-shaped remote. It runs `--session` and asserts three things: the
  note line is printed, `core.sshCommand` is still unset, and `--check` exits 0 for the ssh arm. Stage
  the current code against the arm and confirm it goes RED before landing it.

## Medium

### M1 — the same `GIT_SSH` override, as found by the seams lens (id 9)

- **Where:** [tools/check-wiring.sh:1340](../../../../tools/check-wiring.sh)
- **Defect and impact:** This is the same root cause as H1, found by a second lens and with a broader
  case list: `GIT_SSH` set to Windows OpenSSH or to plink, and `ssh.variant` / `GIT_SSH_VARIANT`.
  `--session` sets `DO_FIX=1` (line 223), so the write happens at SessionStart.
- **Grade note:** The skeptic bound this one at medium and id 3 at high, which is the binding grade
  for each. I judge them the same defect, and I would grade both high under the rubric (operator
  config overridden unattended, on a narrow path). They are kept as separate items only because two
  binding grades cannot share an item. H1's fix closes both.
- **Fix (judged SOUND by the skeptic):** Treat a non-empty `GIT_SSH`, and also `ssh.variant` or
  `GIT_SSH_VARIANT`, as an operator choice. Print `note ssh — GIT_SSH is the operator's; NOT setting
  core.sshCommand` and write nothing. At the very least, name `GIT_SSH` in the header's does-not-check
  list and in spec 2.
- **Left-shift gate:** The H1 arm, extended with a second case that sets `GIT_SSH_VARIANT` only.

### M2 — the receipt-sync fixtures inherit host gitattributes and the host object format (ids 4, 12)

- **Where:** [tools/run-gates/check-receipt.py:290](../../../../tools/run-gates/check-receipt.py)
  (`check_git_arms`, lines 285-326)
- **Defect:** Each fixture's `.git/config` pins `autocrlf`, `safecrlf`, `hooksPath`, `gpgsign` and
  `user`. gitattributes are not config, though. The host's `core.attributesFile` (or the XDG default
  `~/.config/git/attributes`), the system gitattributes and `init.defaultObjectFormat` all still reach
  the fixture's add, its checkout and the graded `hash-object --stdin-paths`.
- **Impact:** With a host-global `* text=auto` or `*.txt text`, fixture (c) 'bare' normalizes its
  untracked CRLF copy and grades it eol-only rather than DRIFTED, so the arm FAILs. With a host-global
  `eol=lf` or `-text`, the 'pinned' re-checkout writes no CR, the RuntimeError fires, and all four arms
  FAIL. With `init.defaultObjectFormat=sha256`, the oids never match `derive_blob_oid`'s SHA-1, so
  arm (a) FAILs. Any arm FAIL makes `main` return 1, so on such a host the receipt-sync leg reds on
  every run, in gov and in both adopters, for a reason that has nothing to do with the receipt. The
  docstring's claim that a host default cannot decide an arm is therefore false. This node's system
  `/etc/gitattributes` holds only `diff=astextplain` rules, so the path is narrow and the failure is
  loud.
- **Fix (judged SOUND by the skeptic, on both ids):** In each fixture's `[core]` block, write
  `attributesFile = <fixture>/.git/no-such-attributes`. Run the fixture spawns with
  `GIT_ATTR_NOSYSTEM=1`. Run `git init --object-format=sha1`. Rewrite the docstring sentence so it says
  exactly what local config pins and what it does not.
- **Left-shift gate:** Add a hermeticity arm that runs `check_git_arms` with `HOME` and
  `XDG_CONFIG_HOME` pointed at a scratch dir whose `git/attributes` holds `* text=auto eol=lf`, and with
  `GIT_CONFIG_GLOBAL` setting `init.defaultObjectFormat=sha256`. All four arms must still pass. This
  is the C14 class (fixture inherits ambient machine state), so the arm should be the class guard and
  not a per-key patch.

### M3 — a failed `core.sshCommand` write exits 0 with no verdict line (id 16)

- **Where:** [tools/check-wiring.sh:1340](../../../../tools/check-wiring.sh)
- **Defect:** `if git config core.sshCommand "$want"; then echo FIXED ...; add_health_event ...; fi`
  has no else branch. Spec 2 S2.4 allows only two outcomes for an unset key: set plus FIXED, or
  UNWIRED. The sibling `check_hook_modes` arm in this same diff reads its write back and prints UNWIRED
  when the write did not take.
- **Impact:** A locked or read-only `.git/config` makes `--fix` exit 0 with no `ssh` line while the
  key is still unset. git's own stderr is the only trace. The next `--check` does report UNWIRED.
- **Grade note:** This is the same defect as L1 (ids 5 and 10), and those bind at low. This lens tied
  it to the spec contract and to the inconsistency between the two sibling arms, which is why it binds
  at medium. Either grade is defensible. The fix is the same for all three ids.
- **Fix (judged SOUND by the skeptic):** Add an else branch:
  `echo "UNWIRED  ssh       — could not set core.sshCommand (local). Fix: git config core.sshCommand '$want'"; unwired=$((unwired+1))`.
- **Left-shift gate:** Add an LC2 arm that makes the fixture's `.git/config` unwritable (on MSYS, hold
  a pre-created `.git/config.lock`, since chmod is unreliable there) and runs `--fix`. Assert an
  `UNWIRED  ssh` line and exit 1.

### M4 — on git older than 2.26, a failed `--show-scope` reads as "unset at every scope" (id 6)

- **Where:** [tools/check-wiring.sh:1336](../../../../tools/check-wiring.sh)
- **Defect:** `got=$(git config --show-scope --get core.sshCommand 2>/dev/null || true)`. On git
  older than 2.26 the flag exits 129 with empty stdout. `got=""` then takes the unset branch, and under
  `--fix`/`--session` a local `core.sshCommand` is written that shadows the operator's global value.
  Spec 2 S2 step 4 forbids exactly that.
- **Impact:** This is a narrow path. It needs git older than 2.26 (for example Ubuntu 20.04's 2.25),
  an operator value at global or system scope, and an ssh remote. The write is local, reversible, and
  announced by a FIXED line. The skeptic re-graded it from high to medium.
- **Fix (judged SOUND by the skeptic):** Separate "unset" from "could not read". Decide set or unset
  with plain `git config --get core.sshCommand`, where exit 1 is the only status that means unset. Use
  `--show-scope` only for the label. On any other non-zero status, print
  `note ssh — cannot read core.sshCommand's scope` and write nothing.
- **Left-shift gate:** Add an LC2 arm that shadows `git` with a shell function that exits 129 on
  `--show-scope` and passes everything else through. With a global `core.sshCommand` set, assert that
  `--session` writes nothing at local scope. This is the "a failed probe reads as absence" class, so
  also grep check-wiring for other `2>/dev/null || true` reads that feed a write decision.

### M5 — a new check-wiring next to an old push-main reds wiring and the shipped self-test (id 7)

- **Where:** [tools/check-wiring.sh:1307](../../../../tools/check-wiring.sh)
- **Defect:** The ssh arm and its shipped LC2 self-test both depend on push-main.sh's new
  `GOV_SSH_KEEPALIVE=` line. Both kits declare `requires = []`, and push-main has no version constant.
  govkit update can narrow with `--kits` and can hold or roll back each kit on its own (govkit.py near
  8522 and 10771), so a target can end up with the new check-wiring.sh beside an older push-main.sh.
- **Impact:** In that mixed state, `--check` prints `UNWIRED ssh — cannot derive the keepalive` and
  exits 1. That is the adopter's `WIRING_CHECK`, so every unattended run is refused. The shipped
  `check-wiring self-test` leg also reds (test lines 1597 and 1665: `WANT` empty, LC2 AC1 and AC8 fail).
  The red is loud, but its cause is kit version skew, not missing wiring. The skeptic re-graded it from
  high to medium.
- **Fix (the skeptic judged the finder's fix UNSOUND, and this is its corrected fix):** Keep `n=0` as
  UNWIRED, as spec AC6 requires. Reword the `n=0` message to say that push-main.sh predates the
  `GOV_SSH_KEEPALIVE` line and that the fix is updating the push-main kit. Make the two kits update
  together: add `requires = ["push-main"]` to check-wiring.kit.toml, or have govkit hold check-wiring
  whenever push-main is held or out of scope. Gate the LC2 test block's skip on the installed push-main
  lacking the line ONLY outside gov (for example, when `PM` is not gov's own `tools/push-main.sh`), so
  that gov's own suite still reds if the line is deleted.
- **Left-shift gate:** Add a govkit selftest arm in which `update --kits check-wiring` runs on a
  target whose push-main receipt predates the line. Assert that check-wiring is held, or that push-main
  is pulled in. More generally, a kit-graph check could flag any kit file that greps a literal out of
  another kit's file without a `requires` edge to it.

### M6 — a renamed engine row drops an adopter-set exec bit (id 8)

- **Where:** [tools/govkit/govkit.py:9947](../../../../tools/govkit/govkit.py)
- **Defect:** On the renamed arm, the call is
  `land_through_index(root, target, new_dest, new_src, data, to_commit, index0)`. `index0` was read
  before `git mv`, so `index0.get(new_dest)` is None, and `resolve_landed_mode(None, gov)` returns
  gov's mode. S3 (around line 9257) correctly resolves the mode from the OLD entry against gov's new
  source, but `renamed` is a touching verdict, so the S4 mode arm (line 9773) skips it and `mode_to` is
  never read.
- **Impact:** Suppose the adopter's entry is 100755 and gov's new source is 100644. The row lands at
  100644 and no mode-carry line is printed. That contradicts DEPL-aLevelledCopy-1 S1 ("never down"),
  which explicitly puts `renamed` under the never-a-downgrade table. The path is narrow and affects one
  file's mode.
- **Fix (judged SOUND by the skeptic):** Make `land_through_index` take the entry mode to resolve from.
  On the renamed arm, pass the old path's `index0` entry, or re-read the index for `new_dest` after
  `git mv`. Alternatively, use `a.get("mode_to")` when it is set.
- **Left-shift gate:** Add a govkit selftest arm in which an adopter-100755 engine row is renamed by
  gov while the new source is 100644. It must land 100755. To cover the class, add an arm per touching
  verdict (`renamed` and any other verdict that lands through `land_through_index`) asserting the
  never-down rule.

### M7 — "read with sed, never sourced" has no arm that can fail (id 13)

- **Where:** [tools/check-wiring.sh:1309](../../../../tools/check-wiring.sh)
- **Defect:** Every LC2 arm (test lines 1600-1674) seeds a well-formed single-quoted definition line,
  or deletes or duplicates it. A regression to `eval "$(grep '^GOV_SSH_KEEPALIVE=' "$pm")"` would
  produce the same value, the same 31 and the same `grep -c` guard result, so AC1, AC2, AC6, AC8 and
  AC10 would all stay green.
- **Impact:** No live misbehaviour exists today. The sed regex
  `^GOV_SSH_KEEPALIVE='\([^']*\)'[[:space:]]*$` refuses a line carrying `$(...)`. The defect is that
  the trust-boundary invariant, which runs at every SessionStart, has no guard.
- **Fix (judged SOUND by the skeptic):** Add an LC2 arm. Seed the fixture's push-main.sh copy with
  `GOV_SSH_KEEPALIVE='ssh'$(touch "$D/ran")` and run `--session`. Assert that `$D/ran` does not exist,
  that the output contains `UNWIRED  ssh       — cannot derive`, and that `core.sshCommand` is still
  unset. Stage an eval-based derivation to observe the arm go RED.
- **Left-shift gate:** The arm above is the gate. Its staged-RED observation belongs in the acceptance
  ledger, as §7 requires for any new gate.

## Low

### L1 — the failed `core.sshCommand` write, as found by correctness and seams (ids 5, 10)

- **Where:** [tools/check-wiring.sh:1340](../../../../tools/check-wiring.sh)
- **Defect:** This is the same no-else-branch defect as M3. `--fix` exits 0 (line 1592) while the key
  is still unset. The hookspath arm at line 648 has the same shape, but that arm already existed at the
  base.
- **Fix (judged SOUND by the skeptic, on both ids):** Add the M3 else branch. Id 10 also asks for the
  same fix in the pre-existing hookspath arm, and doing both in one change keeps the two arms
  consistent.
- **Left-shift gate:** The M3 arm, plus a twin that runs against the hookspath arm.

### L2 — two branches of the ssh-URL classifier have no arm (id 14)

- **Where:** [tools/check-wiring.test.sh:1639](../../../../tools/check-wiring.test.sh)
- **Defect:** LC2 covers only the scp form, https and no remote. Neither the
  `ssh://|git+ssh://|ssh+git://` branch nor the one-character-host drive-path rule (`C:/x`) is exercised.
- **Impact:** If the drive-path rule regressed, a Windows local-mirror remote would read as ssh and
  `--check` would red unattended runs. If the `ssh://` branch were dropped, the arm would skip silently.
- **Fix (judged SOUND by the skeptic):** Extend the LC2 AC5 loop with `C:/x/origin.git`, expecting a
  skip with nothing set. Add an `ssh://git@example.invalid/o/r.git` case shaped like AC1, expecting
  FIXED under `--session`.
- **Left-shift gate:** Those two arms. A classifier with N case branches should carry at least N arms.

### L3 — the no-.git guard in `resolve_clean_oids` has no built-in arm (id 15)

- **Where:** [tools/run-gates/check-receipt.py:143](../../../../tools/run-gates/check-receipt.py)
- **Defect:** Every built-in fixture without a `.git` has rows without an `oid`, so the guard is never
  reached. Deleting it leaves every arm `ok`. Spec AC7 was a one-time ledger observation.
- **Impact:** If the guard regressed, a no-.git receipt tree on a host with `core.autocrlf=true` would
  grade CRLF copies as clean: a silent pass of the integrity leg.
- **Fix (judged SOUND by the skeptic):** Add a built-in arm: a fixture with no `.git` and one CRLF
  engine row carrying an LF sha256 and an LF oid. Assert one DRIFTED finding, one
  `GIT       hash-object --stdin-paths not consulted` line, and eol-only 0.
- **Left-shift gate:** That arm. Ledger-only observations of a guard should be promoted to built-in
  arms at close.

### L4 — the build README's roster still says OPEN (id 18)

- **Where:** [memory/builds/aLevelledCopy/README.md:51](../README.md)
- **Defect:** The authored `roster:units` table has a Status column that reads OPEN for all four units.
  The generated build-units block below it reads CLOSED rev-2. Sibling builds (aBatchedMinors,
  aBatchedLintel) carry no Status column.
- **Fix (judged SOUND by the skeptic):** Drop the Status column, or update it to CLOSED.
- **Left-shift gate:** Add a hygiene check that refuses a Status column in an authored `roster:units`
  table, because status is derived (§5).

### L5 — spec 3 AC6 names a fixture that never ran (id 19)

- **Where:** [memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md:246](../spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md)
- **Defect:** AC6 says `fixture: WSL ext4`. The ledger records the run on WSL `/tmp`, which `df -T`
  reported as tmpfs. The rev-2 revision log does not record the change. Only commit 788a74b79's
  Decided line does.
- **Fix (judged SOUND by the skeptic):** Amend AC6's fixture line to name a filesystem that honours the
  exec bit (WSL's own `/tmp`, tmpfs), and add the change to the rev-2 revision-log entry.
- **Left-shift gate:** This is the observed-by-claim-no-arm-discharges class. A close-time check could
  compare each AC's named fixture against the ledger's recorded fixture and red on a mismatch that the
  revision log does not mention.

## Refuted (for the record)

Four findings were refuted: ids 1, 2, 11 and 17. Each one's reason is in the appendix. None of them
is outstanding.

review-shape kind=diff-review round=1 intensity=full at=synth raw=19 confirmed=15 refuted=4 unverified=0 blocker=0 high=1 medium=8 low=6 agents=11 out-tokens=219076

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict | classes |
|---|---|---|---|---|---|---|---|---|
| 1 | security | tools/check-wiring.sh:173 | high | - | refuted | Spec 2 §5 places the trust boundary at the same level as core.hooksPath: a file in this tree's working copy. Anyone who can edit push-main.sh in the working tree, whether through a branch under review or an agent in a session, can equally edit tools/check-wiring.sh. That script itself runs at every SessionStart, so it could run `git config core.sshCommand <anything>` directly, or do anything else, and the result persists after the branch is gone just the same. A hostile GOV_SSH_KEEPALIVE value therefore grants no capability beyond what the attacker already has. push-main.sh also places the same value into GIT_SSH_COMMAND (line 183) whenever it runs. The value is read with sed and is never sourced or evaluated by check-wiring. No escalation is reachable through this diff. | sound | - |
| 2 | security | tools/run-gates/check-receipt.py:622 | medium | - | refuted | The hazard class is pre-existing and handled at a boundary by design. .githooks/pre-push (S2) and .githooks/pre-commit:8 already unset GIT_DIR, GIT_WORK_TREE, GIT_INDEX_FILE and the related variables before the bar runs, and the pre-push comment states that two existing bar legs already `git init` scratch repos under the same run-gates.sh. That runner's lack of an environment scrub for its legs is unchanged by this diff. The finding does not name a concrete invocation path in this tree or in an adopter that reaches run-gates with GIT_DIR exported and unscrubbed. This new leg only joins a population the existing hook-level scrub already covers. It was graded medium and could not be established as a defect this diff introduced or made reachable. | sound | C16 |
| 3 | correctness | tools/check-wiring.sh:1336 | high | high | confirmed | git's connect.c resolves the SSH program as GIT_SSH_COMMAND (env), then core.sshCommand (config), then GIT_SSH (env). check_ssh_keepalive (tools/check-wiring.sh:1336-1348) decides that no scope sets a value from `git config --show-scope --get core.sshCommand` alone. Under --session or --fix it then writes a repo-local core.sshCommand='ssh -o ServerAliveInterval=30 ...'. On a node where the operator chose plink in the Git for Windows installer, which sets GIT_SSH in the user environment, or pointed GIT_SSH at Windows OpenSSH, that unattended write silently replaces the operator's SSH program with the bundled ssh. That ssh cannot see Pageant or the Windows agent, so pushes can fail authentication. This contradicts the arm's own rule that an operator value is never overwritten. The header (lines 42-45) lists only GIT_SSH_COMMAND as unchecked, and the BY DESIGN list covers only push-main's GIT_SSH_COMMAND, not GIT_SSH. --check also prints a Fix line telling such an operator to make the same breaking change. The path is narrow (a plink or GIT_SSH user, an ssh remote, nothing in config), but the arm breaks the security rule unattended. | sound | - |
| 4 | correctness | tools/run-gates/check-receipt.py:290 | medium | medium | confirmed | check_git_arms writes autocrlf, safecrlf, hooksPath and gpgsign into each fixture's .git/config, but not core.attributesFile. git still reads the global attributes file (core.attributesFile, or the XDG default ~/.config/git/attributes even when unset) for `hash-object --stdin-paths`. Fixture (c), 'bare', holds an untracked CRLF f.txt with no local .gitattributes. Under a global `* text=auto` or `*.txt text`, the clean filter normalizes CRLF to LF, because a path not in the index is not exempted by the has-CRLF-in-index rule. The clean oid then equals derive_blob_oid(lf) while the raw blob differs, so the row grades eol-only, check_drifted fails, and arm (c) FAILs. check_fixtures runs on every invocation, and main returns 1 when any arm fails, so the receipt-sync leg reds on every run on such a host. That contradicts the docstring's claim that a host default cannot decide an arm. The defect is new in this diff, and its effect is a contained false red. | sound | - |
| 5 | correctness | tools/check-wiring.sh:1340 | low | low | confirmed | At bb6178e, tools/check-wiring.sh lines 1338-1344 run `if git config core.sshCommand "$want"; then echo FIXED...; add_health_event...; fi` and have no else branch. If the write fails (locked or read-only config), the arm prints no ssh line of its own and leaves `unwired` alone. Line 1592 (`[ "$unwired" = 0 ] && exit 0 \|\| exit 1`) therefore exits 0 while the key is still unset. The hookspath arm at line 648 has the same shape, but that arm already existed at the base; this ssh arm is new code and repeats the gap. It is not completely silent, because git config's own stderr is not suppressed. Even so, the exit status, which is the contract, reports a fix that did not happen. | sound | - |
| 6 | seams | tools/check-wiring.sh:1336 | high | medium | confirmed | Line 1336 is `got=$(git config --show-scope --get core.sshCommand 2>/dev/null \|\| true)`. `--show-scope` arrived in git 2.26, and an older git exits 129 with nothing on stdout. got="" then sends the arm into the unset branch, and under --fix/--session it runs `git config core.sshCommand "$want"` at local scope. That shadows an operator's global value, which spec 2 S2 step 4 explicitly forbids ('a global operator value carrying an identity must not be shadowed'). No minimum git version is enforced. Base check-wiring uses only `--path-format` (2.31), inside resolve_health_log, and that call degrades quietly (`\|\| return 1`), so nothing earlier in the script stops a pre-2.26 git. The path is real but narrow: it needs git older than 2.26 (for example Ubuntu 20.04's 2.25), plus an operator core.sshCommand at global or system scope, plus an ssh remote. The effect is contained: the write is local and reversible, and it is announced by a FIXED line and a health event. It is a wrong config write, not a security hole, because the value written is still the trusted kit-derived one. | sound | - |
| 7 | seams | tools/check-wiring.sh:1307 | high | medium | confirmed | Both kit entries declare `requires = []`, and push-main has no version constant (`version_from = { none = ... }`). govkit update supports `--kits` narrowing and rolls back held kits per kit (govkit.py near 8522 and 10771). A target can therefore end up with the new check-wiring.sh beside an older push-main.sh. In that state `grep -c '^GOV_SSH_KEEPALIVE='` returns 0 and the arm prints `UNWIRED ssh — cannot derive the keepalive`, so --check exits 1. The shipped self-test also fails: it resolves PM to the installed push-main.sh, WANT comes out empty at test line 1597, and AC1/AC8 (around line 1666) red the adopter's `check-wiring self-test` gate leg. Spec 2 does mandate UNWIRED for zero lines (S2 step 2, AC6). It also assumes the two kits always update together ('Both kits ship with a normal govkit update'), and the code does not enforce that. The failure is loud rather than silent, but it is a false wiring red with a misleading cause, on a reachable but uncommon path. | unsound | - |
| 8 | seams | tools/govkit/govkit.py:9947 | medium | medium | confirmed | On the renamed arm (line 9947), the call is `land_through_index(root, target, new_dest, new_src, data, to_commit, index0)`. index0 was read before `git mv` and is keyed by receipt paths, so `index0.get(new_dest)` is None, and resolve_landed_mode(None, gov) returns gov's mode. When the adopter's entry is 100755 and gov's new source is 100644, the file lands at 100644. S3 (line 9257) computes the renamed row's mode from the old entry and correctly gets 100755, so it prints no line. S4 (line 9773) skips touching verdicts, so the exec bit drops silently. Base behaved the same way: entry None, so gov's mode. But spec DEPL-aLevelledCopy-1 S1 is new in this diff and explicitly puts the `renamed` arm under its never-a-downgrade table, and S3 explicitly names the old entry against the new source. This unit claims a guarantee its own code does not deliver on that arm. The path is narrow (gov renames an engine row that the adopter made executable while gov ships it 100644), and the effect is one file's mode. | sound | - |
| 9 | seams | tools/check-wiring.sh:1340 | medium | medium | confirmed | In git's connect.c, the order is: GIT_SSH_COMMAND first, then core.sshCommand, and GIT_SSH only when neither is set. check_ssh_keepalive (tools/check-wiring.sh:1336-1343) looks only at `git config --show-scope --get core.sshCommand`. When that is empty it writes `ssh -o ...` under --fix and also under --session, since DO_FIX=1 for both (line 223). Nothing in the arm, its header (lines 42-45) or spec 2 mentions GIT_SSH or ssh.variant. Git for Windows' Plink/TortoisePlink installer option sets GIT_SSH at user level, so the path is real. On such a node the first SessionStart writes a local core.sshCommand. From then on every fetch and push in that tree runs the bundled OpenSSH instead of plink/Pageant, and authentication can fail. That overrides an operator choice, which the spec's own security model forbids. The by-design list covers only GIT_SSH_COMMAND. The effect is contained: one tree, recoverable with `git config --unset`, and only on the narrower GIT_SSH path. So it is medium. | sound | - |
| 10 | seams | tools/check-wiring.sh:1340 | low | low | confirmed | At lines 1340-1344 the `if git config core.sshCommand "$want"` has no else branch. On a failed write the arm prints no verdict line and does not increment `unwired`, so `--fix` exits 0 while the keepalive is still unset. Every other branch prints a verdict. The ssh arm is new in this diff, though it copies the pre-existing hooksPath pattern at line 648. The failure is not fully silent: git itself prints `error: could not lock config file ...` to stderr. It also needs an unwritable .git/config, and in that case the hooks arm fails the same way. Contained, so low. | sound | - |
| 11 | seams | memory/builds/aLevelledCopy/build/2026-10-09-build-TOOL-aLevelledCopy-2-1-acceptance-ledger.md:13 | low | - | refuted | The wrap is real: `install-prefix` and `(shipped surface)` sit on lines 13-14. But no reader joins a ledger's prose 'close still owes' sentence to leg names. The gotcha ledger-token-wrapped-across-a-line-joins-nothing describes hygiene check 23 in tools/memory-tree/check-memory-hygiene.sh. Check 23 joins the backticked tokens of AC answer lines (the `- ACn — ...` bullets) to that criterion's own tokens. The wrapped token is in the preamble paragraph, not in an AC bullet. Every AC1-AC9 bullet in this ledger keeps its tokens on one physical line. A grep of tools/ for any parser of 'still owes' in ledgers finds none. Commit 5eac1decf fixed wrapped tokens inside an AC7 bullet, which is a different case. The 'line-oriented join' the finding relies on does not exist, so nothing is dropped from what the close sees as owed. | sound | ledger-token-wrapped-across-a-line-joins-nothing |
| 12 | verification | tools/run-gates/check-receipt.py:290 | medium | medium | confirmed | check_git_arms (check-receipt.py:285-326) is new in this diff. It pins only config keys in each fixture's .git/config. Gitattributes are not config, so a host's global core.attributesFile, or the default ~/.config/git/attributes, still applies inside the fixtures, as does the system gitattributes. The fixture's add, checkout and the graded `hash-object --stdin-paths` all apply attribute-driven conversion. Consider arm (c) 'bare': autocrlf=false, no in-tree attributes, CRLF bytes, and nothing in the index. With a host-global `* text=auto` or `* text`, the clean filter normalizes it to the LF blob, so it grades eol-only rather than DRIFTED and the arm FAILs. A host-global eol=lf rule matching f.txt makes the 'pinned' re-checkout write no CR, the RuntimeError fires, and all four arms FAIL. The arms run on every invocation, and any FAIL makes main return 1, so the leg reds permanently on that host for a reason unrelated to the receipt. I checked this node: the Git for Windows system /etc/gitattributes holds only diff=astextplain rules and there is no user attributes file. So the path needs an operator-configured global text/eol rule (or init.defaultObjectFormat=sha256), which makes it narrow. The result is a visible false red, not a silent pass, so medium. | sound | C14 |
| 13 | verification | tools/check-wiring.sh:1309 | medium | medium | confirmed | The claim holds. Every LC2 arm (test lines 1600-1674) seeds only a well-formed single-quoted definition line, either the real one or one edited from 30 to 31, or deletes or duplicates that line. No arm puts a `$(...)` or other shell-active text on the GOV_SSH_KEEPALIVE line. An eval- or source-based derivation of a well-formed line yields the same value, the same 31, and the same grep -c guard result, so every arm would stay green. This leaves the 'read with sed, never sourced' trust-boundary property (check-wiring.sh comment above check_ssh_keepalive) with no check that can fail. There is no live misbehaviour today: the sed regex `^GOV_SSH_KEEPALIVE='\([^']*\)'[[:space:]]*$` refuses such a line. The defect is the missing guard on a security invariant that runs at every SessionStart, so medium. | sound | - |
| 14 | verification | tools/check-wiring.test.sh:1639 | low | low | confirmed | LC2 AC5 loops only over the https URL and the empty URL (test line 1640), and AC1 uses only the scp-form SSHURL (line 1598). No arm exercises the `ssh://\|git+ssh://\|ssh+git://` case branch or the `${#host} -gt 1` drive-path rule (check-wiring.sh, case block in check_ssh_keepalive). So a regression in either branch would go uncaught. This is a pure coverage gap with no current behavioural defect, so low. | sound | - |
| 15 | verification | tools/run-gates/check-receipt.py:143 | low | low | confirmed | In check_fixtures, the only fixtures written without .git carry no `oid` (`clean`, `drifted`, `absent`, `norows`), so `asked` is empty and resolve_clean_oids is never called for them. check_git_arms always uses real repos. So the `if not (tree / ".git").exists()` guard at line 143 is never reached by any built-in arm, and deleting it leaves every arm green. The guard itself is correct today, so this is a coverage gap: low. The proposed fix is sound. With the guard present, findings are one GIT line plus one DRIFTED and eol-only is 0. With the guard deleted, the GIT line disappears on any host (autocrlf true or false), so the arm reds regardless of host config. | sound | - |
| 16 | intent | tools/check-wiring.sh:1340 | medium | medium | confirmed | In check_ssh_keepalive, `if git config core.sshCommand "$want"; then echo FIXED ...; add_health_event ...; fi` has no else branch. Then it reaches `return` with nothing printed on stdout for the ssh arm and with `unwired` not incremented. A failed write (locked or read-only .git/config) therefore leaves --fix/--session exiting 0 with the key unset. Only git's own stderr error shows. This contradicts spec 2's two allowed outcomes and the sibling hook-mode arm's read-back-then-UNWIRED handling. The effect is contained because the next --check run reports UNWIRED, so medium. The proposed else branch, which prints UNWIRED with the Fix command and increments `unwired`, cures it and matches the arm's existing message shape. | sound | - |
| 17 | intent | tools/check-wiring.sh:1302 | low | - | refuted | The code does what spec 2 S2 step 1 says, word for word: the receipt rung first, then `${KIT_REL:+$KIT_REL/}push-main.sh`, with `first_of` doing the `[ -f ]` test (check-wiring.sh:1302). The §5 sentence is a summary of the normal case, so the code does not disagree with the spec's instruction. The attack in the finding also gains nothing. Planting an untracked file in the worktree needs local write access, and that same access can write .git/config, or core.sshCommand, directly. A tracked file at <kit>/push-main.sh that is not gov's is the adopter's own committed content. That is the same trust the tree already gives its own tracked .githooks through core.hooksPath. No boundary is crossed that was not already open, and the rung pattern is the one every other arm uses (SMERGE). The finder graded it low and I cannot establish real impact. | sound | - |
| 18 | intent | memory/builds/aLevelledCopy/README.md:51 | low | low | confirmed | At bb6178eab, memory/builds/aLevelledCopy/README.md has the authored roster:units table with a Status column reading OPEN for all four units. The generated build-units block just below it reads CLOSED rev-2 for each. The sibling builds aBatchedMinors and aBatchedLintel have roster tables with columns # \| Unit \| Tier \| Mechanism and no Status column. So this column is a second, hand-written copy of the status, and it went stale inside this diff. The page contradicts itself. It changes no behaviour. | sound | - |
| 19 | intent | memory/builds/aLevelledCopy/spec/2026-10-09-spec-TOOL-aLevelledCopy-3.md:246 | low | low | confirmed | Spec 3 AC6 (line 246) still says 'fixture: WSL ext4'. The acceptance ledger (build/...-TOOL-aLevelledCopy-3-1-acceptance-ledger.md:26) records the run on WSL's own /tmp, which `df -T` reported as tmpfs and not ext4. The rev-2 revision-log entry lists only the §4 skip and ok cases and Status CLOSED; it does not mention the fixture change. The criterion's real need is a filesystem that honours the exec bit, and tmpfs does, so the evidence is valid. Only the CLOSED spec's text is out of step with it. The defect is in documentation only. | sound | observed-by-claim-no-arm-discharges |
