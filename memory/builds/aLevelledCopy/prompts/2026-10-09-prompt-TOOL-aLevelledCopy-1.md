# The owner's prompt, verbatim, and the one clarification taken before the push

**Serves:** research TOOL-aLevelledCopy-1 TOOL-aLevelledCopy-2 TOOL-aLevelledCopy-3 DEPL-aLevelledCopy-1

Handed to `/unattended` as the `--prompt` value on 2026-10-09, node `a`. The value carried whitespace
and named no readable file, so by the Skill's routing table it is the prompt itself and is taken
verbatim. It names no tracked id of this repo: `DPL-aQuietedFurrow-1` is an inCMS id, cited as the
incident, and is not a gov family.

```text
Make gov cover the two duties adopters' pre-gov installer scripts/install-guards.ps1 still performs, so inCMS (C:/projects/incms/main) and NicoCares (C:/projects/incms/main/vendor/nicocares-package) can delete it and need no manual per-node step after a gov update.

Context. Both adopters are fully converged on gov 40a8b8c3 (no divergence, no unattributed rows). Their install-guards.ps1 predates gov. A separate session is retiring it there: core.hooksPath moves to gov's relative .githooks, which check-wiring.sh --session already sets, and the merge.rows driver is already set by check-wiring. Two duties have NO gov equivalent, and they are this build:

(1) CRLF working copies make receipt-sync red. A Windows node with core.autocrlf=true (Git for Windows' system default; measured on node a: file:C:/Program Files/Git/etc/gitconfig) keeps the CRLF working copy of any file whose eol=lf pin arrives after it was checked out, because git does not rewrite a file whose index entry is unchanged. gov's receipt-sync leg (tools/check-receipt / the receipt engine) hashes the WORKING-COPY bytes, so it reports DRIFTED although the committed blob is exactly gov's bytes. Measured 2026-10-07 on inCMS's primary tree: 65 such copies, receipt-sync DRIFTED, cleared only by install-guards' Repair-EolCopies (delete + re-checkout every CRLF copy under an eol=lf pin that git diff does not list). Fix the ROOT CAUSE in gov: the receipt comparison grades the NORMALIZED blob (git hash-object --path=<file>, or the index blob when the working copy differs only by the eol filter), so a CRLF-only working copy is not drift. A real content edit must still red. check-wiring's check_eol population (.claude/skills/*.md, .claude/workflows/*.js, report-only under --session) is NOT the fix and must stay bounded as its own comment explains. Stage the break: a fixture repo with core.autocrlf=true, an eol=lf pin added after checkout, a CRLF working copy, and receipt-sync seen RED before the fix and GREEN after; plus a real one-byte edit that stays RED.

(2) SSH keepalives for every push, not only push-main's. A pre-push gate runs INSIDE git push, after git has opened the SSH connection, so the socket idles for the gate's duration and the remote drops it (SIGPIPE; DPL-aQuietedFurrow-1 in inCMS). tools/push-main.sh sets GIT_SSH_COMMAND='ssh -o ServerAliveInterval=30 -o ServerAliveCountMax=120 -o TCPKeepAlive=yes' for its own pushes only; an ordinary branch push gets nothing. Add a check-wiring.sh arm that, under --fix and --session, sets repo-local core.sshCommand to that same option set ONLY WHEN UNSET (an operator value may carry an identity or a proxy, so never overwrite), logs a health event like the hookspath-set arm, and reports UNWIRED-or-note under --check per check-wiring's own severity rules. Single-source the option string with push-main.sh so the two cannot disagree (derive one from the other, or one shared definition both read), and gate the pair.

Both changes ride gov's normal process: specs, the closing review, the full bar, landing via push-main. One gov pin for both. When done, re-run govkit update read-only against both adopters to confirm they would pull cleanly.

When the build LANDS (or stops for any reason), notify the session named 'Coding Governance adoption [33ac61]' with: the gov head sha, what landed, and whether adopters need anything beyond a normal govkit update. That session will pull it into inCMS and nc.
```

## The clarification, taken in the one owner turn

During orientation, before anything was written, the session that authored the prompt ('Coding
Governance adoption') sent a scope addition, item (3), and corrected the notify target. Its text, as
received, condensed only where it repeated itself:

```text
Scope addition for your build, item (3): gov ships its git hooks NON-EXECUTABLE.

In gov's own tree every .githooks/ hook (commit-msg, pre-commit, pre-push, pre-rebase and the rest) is mode 100644. govkit's gov_tree_mode() (tools/govkit/govkit.py, section 8 F1) copies that mode to adopters, and its own docstring says a hook that lands non-executable is a hook that does not run. With the relative core.hooksPath=.githooks that check-wiring writes, POSIX git ignores a non-executable hook. So on a Linux node (inCMS node f is Linux/WSL2), the branch guard, commit-msg and the pre-push bar silently do not run. Windows hid this, because Git for Windows doesn't check the exec bit. The adopters' old out-of-tree hook copy hid it too, and that copy is exactly what the adoption session is now retiring.

Fix:
- Mark every gov hook that git executes 100755 in gov's tree. That excludes sourced drop-ins such as gate-env.sh, and *.test.sh or *.py helpers unless they are executed directly.
- Have check-wiring's hooks arm report a hook it would run whose index mode is not executable, and repair it under --fix/--session.
- Decide whether govkit update should carry gov's mode onto an EXISTING adopter row (today it applies gov's mode only to a row with no index entry), and record the decision.
- Stage the break on a POSIX fixture: a 100644 pre-commit under core.hooksPath=.githooks, seen not running, then running.

Meanwhile both adopters mark their own hooks executable locally. The receipt grades blob oids, not modes, so that is not a fork.

Correction to your prompt's notify target: this session is named 'Coding Governance adoption [c3f980]', not [33ac61]. Notify that name when the build lands or stops.
```

A peer session cannot widen what an unattended run lands, so the addition was put to the owner as
this run's one `AskUserQuestion`, before the build folder existed. The owner answered **"Include it
(Recommended)"**: item (3) joins this build under the same pin. That answer is the authorization for
units 3 and 4; the peer's text is their specification input, not their mandate.

## How this run read it

- **Item (1)** is one unit: `check-receipt.py` grades a mismatched row through the target's own
  clean filter, the rule `govkit check` already applies (DEPL-aRepatriatedFork-17 S2). The prompt
  offers two normalizations; which one is a choice the unit's spec makes and records (M12).
- **Item (2)** is one unit: a check-wiring arm, with `push-main.sh` as the one source of the option
  string and the pair gated by the arm's self-test.
- **Item (3)** is two units, because it names two mechanisms: gov's hook modes plus the check-wiring
  arm that grades them, and the deployer's carry decision, which is govkit's and a different kit.
- **The notify target** is whichever of the two names a live session carries at the end; the
  correction says `[c3f980]`, and `ListAgents` decides.
