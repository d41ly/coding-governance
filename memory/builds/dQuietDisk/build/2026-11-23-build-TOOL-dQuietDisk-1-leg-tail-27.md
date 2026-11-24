# TOOL-dQuietDisk-1 leg-tail 27 — run-gates evidence failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** run-gates evidence
- **Hash:** 7b2d58665172e37473dff1026ef25e85e7442d38
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
  ok   — S2 the cut runner's bar over the output and key legs is green
  ok   — AC1 a one-second leg's seconds read 2.310 from EPOCHREALTIME
  ok   — AC1 an end stamp that lost its scale reds: '-1793615711.-610'
  ok   — AC2 every output leg's run-record copy and gate-logs copy equal the $(cat) capture's bytes, NUL, CRLF and trailing newlines included
  ok   — AC2 a strip that keeps the trailing newlines, or a guard that never redacts, moves 6 copies
  ok   — AC3 a name with a space, a slash and a two-byte character maps one underscore per byte
  ok   — AC3 the mapping in the caller's UTF-8 locale names a different log
  ok   — AC4 a credential URL is masked in the run-record copy
  ok   — AC4 a guard that never matches leaks the credential, so the arm can see it
  SKIP — AC4 the mode: chmod 600 gives -rw-r--r-- on this host, so no mask can be observed
  SKIP — AC4 the unmasked variant, for the same reason
  ok   — AC6 all 13 ledger keys equal input_key's, the glob and the absent guard included
  ok   — AC6 a union listing sorted backwards moves 2 key(s)
  ok   — AC6 a GATE_REUSE bar reuses all 13 legs on the precomputed keys
  ok   — AC7 tmp.Z7MoqgwFBM: head, worktree and the log dir are what git answers there
  ok   — AC7 wt: head, worktree and the log dir are what git answers there
  ok   — AC7 tmp.5TiLthVtHj: head, worktree and the log dir are what git answers there
  ok   — AC7 a bare rev-parse HEAD on an unborn branch reads the word, so the arm can see it
  ok   — AC1 a red post-merge exits 1, refs/gov/bar-red names c2, and gate-post-merge reads verdict RED, published pushed
  ok   — AC1 gate-run/<run_id>/ in the common dir holds the failing leg's output after the scratch worktree is gone
  ok   — AC2 a green descendant exits 0 and git ls-remote --exit-code of refs/gov/bar-red exits 2
hint: Support for <GIT_DIR>/info/grafts is deprecated
hint: and will be removed in a future Git version.
hint:
hint: Please use "git replace --convert-graft-file"
hint: to convert the grafts into replace refs.
hint:
hint: Turn this message off by running
hint: "git config set advice.graftFileDeprecated false"
  ok   — AC2 the common dir's gate-verdict/<c3 tree> reads GREEN, kind full, by runner, sha c3, and no gate-bar-green.shared is written
  ok   — AC2 the runner's gate-full-green.shared is present and no gate-pm. worktree is left
  ok   — AC3 a green on c2's parent exits 0, the ref still names c2, and the record reads published kept
  ok   — AC4 a red on c2 with the ref at c3 exits 1, keeps c3, and reads published kept
  ok   — AC5 the declared bar saw GATE_FULL=1, a holder, no GATE_REUSE, HEAD at the sha and a gate-pm. cwd
  ok   — TOOL-dWitnessedBar-60 AC3 an inherited GATE_SELECTION and GATE_BASE_FROM are named as not honoured and the declared bar sees neither
  ok   — AC6 a rejected publication exits 1, prints publish FAILED naming the rejection, and records published failed with a why
  ok   — AC7 an unlanded commit exits 2 with REFUSING, no bar ran and no ref was pushed
  ok   — AC8 export GOV_GATE_CMD= exits 2 naming the line, and no bar ran
  ok   — AC8 the accepted form GOV_GATE_CMD=\'bash\ bar.sh\'\\n resolves to bash bar.sh
  ok   — AC8 the accepted form GOV_GATE_CMD=\"bash\ bar.sh\"\ #\ the\ bar\\n resolves to bash bar.sh
  ok   — AC8 the accepted form GOV_GATE_CMD=\"bash\ bar.sh\"\\r\\n resolves to bash bar.sh
  ok   — AC8 the accepted form GOV_GATE_CMD=bash\ nothing.sh\\nGOV_GATE_CMD=\"bash\ bar.sh\"\\n resolves to bash bar.sh
  ok   — TOOL-17 AC2 a runner exiting 0 with verdict RED exits 1, refs/gov/bar-red stays, and no green record is written
  ok   — TOOL-17 AC3 a bar that moves the worktree's HEAD exits 2 with REFUSED and writes no green record
  ok   — AC9 two remotes, a detached HEAD and no GOV_REMOTE exit 2 naming GOV_REMOTE
  ok   — AC9 --remote second publishes the red on the second remote and the first shows none
  ok   — AC10 no argument exits 2 with a usage line and no bar
  ok   — AC10 a sha naming no commit exits 2 with a usage line and no bar
  ok   — 51-AC32 precondition: the quarantine planted at pa's row hash holds
  ok   — 51-AC32 a reworded purpose leaves pa quarantined
  ok   — 51-AC32 an argv changed releases it
  ok   — 51-AC24 a run in worktree A keeps the verdict B's run names and prunes the unnamed 31-day one
  ok   — 51-AC30 keep_tails.py --selftest holds the fence, the fields and the cut
  ok   — 63-AC16 read_record_keys keeps an empty last field's TAB in note
  ok   — 63-AC16 read_record_keys leaves a no-TAB reused line unset
  ok   — 65-AC11 read_record_keys strips one CR from verdict and keeps note's last TAB
  ok   — 65-AC11 read_record_keys keeps the last of a repeated head key
  ok   — 67-AC9 read_record_keys reads an unterminated last line head<TAB>z as z

FAIL (run-gates evidence durability, 344 assertions)
```
