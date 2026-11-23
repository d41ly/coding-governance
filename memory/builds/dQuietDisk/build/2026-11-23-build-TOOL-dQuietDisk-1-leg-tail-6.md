# TOOL-dQuietDisk-1 leg-tail 6 — check-arms selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** check-arms selftest
- **Hash:** d39c99cee80d0cb3d2fe36ce523d117809b545b0
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
refusal pin rows : 0 read, 0 not read
unbudgeted gates (3, no REFUSAL_CEILINGS token): tools/gate-a.sh tools/gate-b.sh tools/gate-c.sh
ERROR tools/gate-a.sh:2: check 1 branch 1 has no literal run long enough to assert on ('') — reword the message or the arm cannot name it
arm ok    ...and the same test quoting the whole signature reads ARMED with no STRANDED token
arm ok    S5+S6: a sidecar pin and a local-suite arm leave the gate green
arm ok    ...and --report names the sidecar that pinned the branch
arm ok    ...and --report names the local suite that armed the other
arm ok    S5: a branch pinned in the central file AND a sidecar is refused, naming both
arm ok    S5: a sidecar row whose gate left its directory is stale, named at the sidecar
arm ok    S6: without the local suite the same branch is named unarmed
arm ok    S1: a script with no fail() helper is discovered by a reasoned exit 1
arm ok    S1: a multi-line block's reason is its topmost print
arm ok    S1: a capture-print status=1 is a delegated site signed by its marker
arm ok    S1: a command-conditioned exit 1 is delegated, not reasoned
arm ok    S1: an exit 1 whose block prints nothing is counted unreasoned, not a site
arm ok    S1: exit 1 inside quotes, a comment or a here-document body is not a site
arm ok    S1: a *.test.sh and a script under the memory root are not discovered
arm ok    S1: a line carrying a fail call is signature 1's alone
arm ok    S1: a marker on a reasoned site is refused
arm ok    S1: a marker no delegated site reads is refused
arm ok    S2: a waived site is printed on every run
arm ok    S2: a second unarmed site of a pinned key reds over its key and count
arm ok    S2: a pin above the live count reds, naming the count to lower
arm ok    S2: a refusal inserted above a pinned site does not re-key its row
arm ok    S2: a test-less script passes with every site pinned, and one unpinned site names the missing test
arm ok    S3: the switch off grades no site, reads no exit row, and prints the OFF line
arm ok    S7: a switch value other than blank or graded is refused by name
arm ok    AC3+AC4: a gate at its ceiling passes and prints the ceiling with its date and id
arm ok    ...and the same tree is green
arm ok    AC3: a census one above its ceiling reds naming the gate and the review
arm ok    AC4: a ceiling token that lacks its date reds naming the token
arm ok    AC4: a ceiling token that lacks its id reds naming the token
arm ok    AC4: a ceiling naming an id the decision log does not carry reds naming the token's id
arm ok    ...and an id carried only as a prefix of a longer one is not carried
arm ok    AC5 control: a family at its ceiling passes and prints with its date and id
arm ok    AC5: one more site matching a family at its ceiling reds with the shared-table remedy
arm ok    AC7: a family pattern matching no refusal site reds naming the family
arm ok    S3 control: a sidecar naming a decision this log lacks reds
arm ok    S3 home-graded: a gov-installed sidecar's decision is gov's, so this log is not asked
arm ok    AC1 control: a retirement row whose survivor carries its signature passes
arm ok    AC1: a retirement row whose survivor lacks its signature reds naming the row's id
arm ok    AC2: a retirement row lacking its survivor field reds naming the field
arm ok    AC2: a retirement row lacking its replay field reds naming the field
arm ok    S2: a retirement row naming an id the decision log does not carry reds
Traceback (most recent call last):
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\memory-tree\check-arms.py", line 1804, in <module>
    sys.exit(main(sys.argv))
             ~~~~^^^^^^^^^^
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\memory-tree\check-arms.py", line 1780, in main
    return cmd_selftest()
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\memory-tree\check-arms.py", line 1736, in cmd_selftest
    tb12, cb12 = build_budget_tree("b12", f"{BG}:2:2026-10-12:TOOL-tBudget-1",
                 ~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                   rows=render_retirement_row(BG, "beta refusal message here", unit="a-retirement"))
                                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\memory-tree\check-arms.py", line 1653, in build_budget_tree
    os.makedirs(t)
    ~~~~~~~~~~~^^^
  File "<frozen os>", line 254, in makedirs
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\d41ly\\AppData\\Local\\Temp\\gate-work.U2uJ4tRR\\tmp\\tmpa17nicwb\\b12'
```
