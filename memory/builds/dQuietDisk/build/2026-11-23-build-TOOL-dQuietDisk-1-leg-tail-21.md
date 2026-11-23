# TOOL-dQuietDisk-1 leg-tail 21 — drift-audit selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** drift-audit selftest
- **Hash:** 76ba19fecc4dcb92720cff2748ee4ddde568c8a1
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
  ok   violated: it names the verb
  ok   the LANGS lookup SEES an in-place widening (a -S pickaxe cannot)
  ok   violated: a language surface widened after ratification fires the staleness signal
  ok   ...and the signal is LIVE by derivation, not a hardcoded True
  ok   a language armed ONLY by a PATTERNS row is read: the verb it defines stops being unused
  ok   ...and the signal stays LIVE over that widened population
  ok   H1: an unshipped `parser` pattern-set id does not raise out of the report
  ok   H1: ...and the report still returns every signal rather than none
lexicon marginal-offense-rate (four states, each distinguishable)
  ok   no .lexicon.conf: the rate is NOT ASKED, not a clean zero
  ok   no .lexicon.conf: it says why
  ok   empty window: NOT ASKED rather than a rate of 0
  ok   empty window: it names the reason, so 0 is never mistaken for clean
  ok   a window with definitions added reports offenders over that population
  ok   ...and is LIVE by derivation over a non-empty population
  ok   ...and carries the fresh-versus-pre-existing split the kill-rule reads
  ok   an ungradeable name is not counted as an offender
  ok   ...and the population grew by the CONTROL alone, so the ungradeable name left both operands
  ok   the marginal rate READS a language armed only by a PATTERNS row: its population grows
  ok   ...and the rate itself did not move, so the population grew by an ON-TABLE name
  ok   an all-ungradeable window is NOT ASKED, never a clean zero
  ok   ...and it says WHY, so the zero is never mistaken for a clean window
  ok   admitting a verb lowers the rate, so the table is read at HEAD and not frozen
  ok   the fixture clone really is shallow (or this arm proves nothing)
  ok   shallow clone: DEAD PROBE rather than a rate over a one-commit window
no signal hardcodes live:True
  ok   no signal returns a literal live:True
live backlog rows per shard
  ok   counts LIVE rows, not entries: 3 of 5
  ok   reports every shard, so a total cannot hide one
  ok   probe is LIVE with shards present
  ok   pinless: the record serialises a null tolerance and a null pin
  ok   pinless: its printed row reads 'report only, no pin' and nothing about being over
  ok   the empty shard reports 0 rather than being skipped
  ok   the busy shard reports its total beside its live count
  ok   closing a row lowers the count
  ok   the signal is not gateable
  ok   no shards at all reports DEAD rather than 0
builds-mode backlog signals (TOOL-dDerivedDocket-34)
  ok   [dDD-34] shards mode: backlog_asks_contested is NOT ASKED, never DEAD
  ok   [dDD-34] shards mode: backlog_evidence_sha is NOT ASKED, never DEAD
  ok   [dDD-34] shards mode: backlog_asks_unlabelled is NOT ASKED, never DEAD
  ok   [dDD-34] shards mode: the live-row count still reads the shards
  ok   [dDD-34] builds mode, no BACKLOG.md: backlog_asks_contested is NOT ASKED, never DEAD
  ok   [dDD-34] builds mode, no BACKLOG.md: backlog_evidence_sha is NOT ASKED, never DEAD
  ok   [dDD-34] builds mode, no BACKLOG.md: backlog_asks_unlabelled is NOT ASKED, never DEAD
Traceback (most recent call last):
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\drift-audit\selftest.py", line 4729, in <module>
    raise SystemExit(main())
                     ~~~~^^
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\drift-audit\selftest.py", line 4675, in main
    test_backlog_ask_signals(tmp)
    ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^
  File "C:\projects\coding-governance\.claude\worktrees\disk-churn-fixes-40450b\tools\drift-audit\selftest.py", line 1589, in test_backlog_ask_signals
    (r / _mt).mkdir()
    ~~~~~~~~~~~~~~~^^
  File "C:\Users\d41ly\AppData\Local\Python\pythoncore-3.15-64\Lib\pathlib\__init__.py", line 1210, in mkdir
    os.mkdir(self, mode)
    ~~~~~~~~^^^^^^^^^^^^
FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'C:\\Users\\d41ly\\AppData\\Local\\Temp\\gate-work.U2uJ4tRR\\tmp\\tmp357yokwj\\asksignals\\memory-tree'
```
