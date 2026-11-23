# TOOL-dQuietDisk-1 leg-tail 25 — measure-legs selftest failed in run unattended-179540992358805920005-2030153

**Serves:** leg-tail TOOL-dQuietDisk-1

- **Leg:** measure-legs selftest
- **Hash:** 9ed2f4d1069aff9c953b9a986811cddeb7221fa4
- **Run:** unattended-179540992358805920005-2030153
- **Sha:** 87fdd8497b08c75f63e601a265ac6f30eb285324
- **Cause:** run:dQuietDisk

```
  FAIL AC35 a failed launch is a failed leg, and the run goes on  ((2, 0.3, None, None, None))
  FAIL AC35 ...the next leg runs after it and reads `ok`, and the table holds both  ((None, None, ['no run dir']))
  ok   AC35 ...and its suspended root is terminated
measure-legs: REFUSED — the runner's resolve_python found no usable python under the legs' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"'
  FAIL AC38 a dead run's raw capture is redacted, recorded and deleted  ((2, 134398871515575635, True, False, ['0.out'], []))
  ok   AC38 ...and a live run's is left alone
  FAIL AC1 the recovered log lands in this run's own record, never in the record owner.json names  (([('C:\\Users\\d41ly\\AppData\\Local\\Temp\\gate-work.U2uJ4tRR\\tmp\\measure-legs-selftest.c57dz62f\\sweep-arm.3x_3tpto\\elsewhere', [], [])], '', {}))
  FAIL AC1 ...and this run's own owner.json holds pid and created alone  ("FileNotFoundError(2, 'No such file or directory')")
  FAIL AC2 a capture reached through a second name, a link or a junction is not read, and named  ({'hln': {}, 'jnr': {}, 'sym': {}})
  ok   AC2 ...nothing behind a plant is copied, deleted or followed, and the plants stay
  ok   AC2 ...and a scratch dir that is a junction is left alone and unlisted
  ok   AC3 LIVENESS a plain scratch file reads, with its identity
  ok   AC3 a junction on the way is refused by its check
  ok   AC3 ...and one swapped in after the check is refused by the pin, naming its final path
  ok   AC4 LIVENESS an unswapped dead capture is recovered and deleted
  ok   AC4 a capture swapped between its read and its delete stays, `not deleted: `
measure-legs: REFUSED — the runner's resolve_python found no usable python under the legs' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"'
  FAIL AC9 a capture name already taken fails the leg, `capture: `, and the run goes on  ((2, None, None, None))
  FAIL AC9 ...writes nothing through the plant, keeps it, and names it in raw_kept  ((b'SECRET-TOKEN=abc123', '', None))
  ok   AC9 a dangling link at the capture's name is refused before any open
  ok   AC9 LIVENESS a free name gives a descriptor naming the identity returned
  ok   AC9 a junction swapped in after the check is refused by the pin, naming its final path
  ok   AC10 a hard link at the capture's name is not read: `unreadable: `, no log, the link kept
  ok   AC10 a plain file planted at the name is not this run's capture: `unreadable: `, no log
  ok   AC10 a row with no capture_id opens nothing
  ok   AC10 LIVENESS the capture this run made is read, redacted and deleted
  ok   AC11 a junction swapped in for raw/ after the read deletes nothing through it: `not deleted: `
  ok   AC11 ...and one past the delete-time check meets the identity compare
  ok   AC6 the rename population is non-empty and holds write_replace's
  FAIL AC6 every rename under the kit renames a tempfile.mkstemp temp, opened by no name  (held_halves.py:181 init_owned_tempdir: renames no tempfile.mkstemp(dir=...) temp; held_halves.py:181 init_owned_tempdir: opens a file by name beside the rename; leg_factory.py:200 init_owned_tempdir: renames no tempfile.mkstemp(dir=...) temp; leg_factory.py:200 init_owned_tempdir: opens a file by name beside the rename; measure_legs.py:236 init_owned_tempdir: renames no tempfile.mkstemp(dir=...) temp; measure_legs.py:236 init_owned_tempdir: opens a file by name beside the rename; product_tests.py:183 init_owned_tempdir: renames no tempfile.mkstemp(dir=...) temp; product_tests.py:183 init_owned)
  ok   AC6 every *.py the walk finds trips this leg's own guard, so a new one runs the leg
  ok   AC5 write_atomic writes nothing through a second name planted at the old fixed temp
  ok   AC5 ...nor creates the target of a dangling link planted there
  ok   AC5 a failed write_atomic returns False and leaves no temp
  ok   AC5 write_held_stamp writes nothing through a second name planted at the old fixed temp
  ok   AC5 a failed write_held_stamp raises and leaves no temp
  ok   AC29 the fixture population is non-empty, so the comparison below can fail
  ok   AC29 every fixture, and only fixtures, is named project-owned
  ok   AC29 no project-owned element carries a glob, which a list include would drop
  FAIL AC2 the interrupt is staged  (no non-final capture was kept, so the interrupt never came: the orphan left its job or ended first (exit 2))
  ok   AC3 the interpreter probe over a venv's python reads a difference of 1
  ok   AC3 LIVENESS ...where a child spawned through sys.executable reads 2, the redirector
  ok   AC3 every program line spawning sys.executable carries _base_executable
  FAIL AC11 measure_job_children refuses with exit 2, one named line and nothing written  ((2, ['measure-legs: REFUSED — the runner\'s resolve_python found no usable python under the legs\' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"\''], [], 'measure-legs: REFUSED — the runner\'s resolve_python found no usable python under the legs\' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"\'\n'))
  FAIL AC11 check_app_alias refuses with exit 2, one named line and nothing written  ((2, ['measure-legs: REFUSED — the runner\'s resolve_python found no usable python under the legs\' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"\''], [], 'measure-legs: REFUSED — the runner\'s resolve_python found no usable python under the legs\' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"\'\n'))
  ok   AC11 a launcher os.lstat cannot read refuses
  ok   AC11 LIVENESS ...and a real non-alias file is no substitution
  ok   AC11 an alias whose printed interpreter is no file refuses
  ok   AC11 LIVENESS ...and one printing a plain file returns it
  ok   AC15 at least three arms subtract two legs' procs_total
  ok   AC15 every such arm reads its legs' verdicts
  ok   AC15 LIVENESS each arm's copy with its verdict conditions taken out is named blind
measure-legs: REFUSED — the runner's resolve_python found no usable python under the legs' environment (exit 2): measure-legs: -c: line 135: unexpected EOF while looking for matching `"'
  FAIL AC9 every legs.tsv row is render_legs_row over its leg's final <i>.json  ((2, [], []))
  FAIL AC9 LIVENESS the orphan's capture moved after its root's exit: `late`, 11 bytes, none kept, and `hold` saw the mark  ((b'', None, None, None))
  FAIL AC5 the loop's admissions pass through check_admit: two, each with no leg running  ((0, []))
  ok   AC16 LIVENESS the README's profiler section is found
  ok   AC16 the docstring and the README say the same about signalling
  ok   AC16 the README this arm reads trips its own leg's guard
FAIL (82 assertions)
```
