# TOOL-dSettledRoster-5 — name the bash executable, so a descriptor's leg stops running under WSL

**Status:** CLOSED · rev-1 · 2026-08-20 · node d · Tier-2 · base 2dc9df35 · streams tooling

*Written AFTER the work landed, at the owner's request, and dated the day it was written. It is a
record of what was built and why, not a plan that preceded it. §9 says so in one line so no reader
has to infer it, and the traceability consequence is carried in `memory/project/trace-waiver.txt`
rather than hidden: the product commits could not name a slug that did not exist when they landed.*

## 1. Goal

The `govkit acceptance matrix` leg was RED on clean `main` and blocked every push through
`tools/push-main.sh`. Make it green by fixing the cause rather than the symptom: govkit was handing
a descriptor's declared `bash` to the Windows loader, which answers that name with the WSL launcher.

## 2. Scope (IN)

- **S1** — `resolve_bash()` in `tools/govkit/govkit.py`: return a bash that shares this filesystem.
  Refuse any candidate under `/system32/` or `/windowsapps/`, accept one only if it RUNS, memoise
  the answer, and take `GOV_BASH` as an override that is a `Refusal` when set and unusable.
- **S2** — `resolve_shell_argv()`: rewrite a LEADING bare `bash` in a descriptor argv to that
  executable, and nothing else.
- **S3** — route govkit's four descriptor-execution sites through it: the adopter check arm, the
  hole discharge probe, the undischarged-hole predicate, and the CONFIGURE adopter call.
- **S4** — route `tools/govkit/matrix.py`'s leg runner through it, because the harness is a Windows
  python executing a leg that a real operator's runner would have run from inside bash.
- **S5** — arms in `tools/govkit/selftest.py` covering both functions and the override refusal.
- **S6** — `KIT_GOVKIT_VERSION` 1.8 -> 1.9; the engine gained behaviour.

## 3. Non-goals (OUT)

- **Converging the three `resolve_bash` copies.** The §10 audit found three, not two, and they do
  not agree on the probe. Filed as `TOOL-dSettledRoster-6` rather than done here: converging a
  function that three kits copy-install is its own unit, and doing it inside a run whose purpose was
  to unblock its own push is the shape the unattended protocol warns about.
- **Making `adopt-playbook.sh`'s `resolve_python` assert a floor.** Its probe is `-c 'import sys'`,
  which no python fails, so it cannot reject an interpreter below a kit's real requirement. That is
  a genuine weakness and it was NOT this bug — see §4 Alternatives rejected.
- **Making `render_playbook.py` tolerate python below 3.11.** A `tomli` fallback would have hidden
  the wrong shell rather than fixed it.
- **A gate on the CLASS.** The gotcha record says plainly that this class has no source-level
  signature worth banning. The copies are armed instead.

## 4. Design

A descriptor declares `argv = ["bash", "{prefix}/playbook/adopt-playbook.sh", "--target", "."]`.
govkit is a Windows python, so `subprocess` resolves that bare name through the Windows loader,
which finds `C:/Windows/System32/bash.exe` — the WSL launcher — before Git-Bash. WSL then sees a
different filesystem, which is why the traceback named a `/mnt/c/...` path for a file that plainly
exists, and it carries its own interpreter: `python3` is 3.10.12 there, so `render_playbook.py:64`
died on `import tomllib`, which needs 3.11.

The remedy is the one `memory/gotchas/subprocess-resolves-a-different-shell.md` already prescribes
for this class: name the EXECUTABLE, not the command.

`resolve_shell_argv` touches position 0 only. A `bash` appearing as an ARGUMENT is a value the
target chose and is none of govkit's business, and `sh` is left alone because substituting bash
would change the language a target asked for. It falls back to the argv unchanged when nothing
resolves, so a machine with no usable bash behaves as it does today instead of newly refusing.

### Files touched (estimate)

| File | Change |
|---|---|
| `tools/govkit/govkit.py` | `resolve_bash`, `resolve_shell_argv`, four call sites, version 1.9 |
| `tools/govkit/matrix.py` | the leg runner routes through `resolve_shell_argv` |
| `tools/govkit/selftest.py` | seven arms |
| `memory/gotchas/subprocess-resolves-a-different-shell.md` | the second and third carriers named |

### Alternatives rejected

- **Blame `resolve_python`.** This was the FIRST diagnosis and it was WRONG. It is recorded because
  the correction is the useful part: every python launcher on node `d` is 3.12 or newer, so no probe
  over them could have produced a 3.10. The 3.10 belonged to the WSL that the shell name pulled in.
  A wrong root cause reached `TOOL-dSettledRoster-3` for one commit and was replaced with the
  measured one.
- **Raise nothing, bypass with `git push --no-verify`.** Defensible on the facts — `origin/main`
  already pointed at a tree that failed this leg — and refused: the owner chose the repair.

## 5. Production-readiness checklist

- security — `resolve_bash` decides which EXECUTABLE runs a target's committed script, so it is a
  trust decision. It narrows rather than widens: it refuses two launcher locations that the previous
  bare-name behaviour accepted silently.
- perf / scale — the answer is memoised in `_BASH`; the probe runs at most once per process.
- a11y — N/A — no user interface.
- i18n — N/A — no user-facing strings.
- error / empty / loading states — an empty argv returns unchanged; an unusable `GOV_BASH` is a
  named `Refusal`; nothing resolvable falls back rather than refusing.
- observability — the `Refusal` names the override it rejected. No new logging.
- risks — a wrong bash silently changes which filesystem a target's scripts see, which is the defect
  itself. The arms pin the two launcher directories by path.
- testing + left-shift gates — seven arms in `tools/govkit/selftest.py`, observed RED under a staged
  break before landing.
- migration / rollback — none; no stored state, no descriptor change. Reverting the commit restores
  the previous behaviour exactly.
- user docs — N/A — internal kit behaviour; the gotcha record carries the reader-facing account.

## 6. Acceptance criteria

- **AC1** — When `python tools/govkit/matrix.py` runs on a node with WSL installed, it prints
  `govkit-matrix: all arms held` instead of failing five arms.
- **AC2** — When `govkit.resolve_bash()` is called, the path it returns contains neither
  `/system32/` nor `/windowsapps/`, and running it with `-c ":"` exits 0.
- **AC3** — When `resolve_shell_argv(["bash", "x.sh"])` is called, position 0 is the resolved
  executable and `["python", "x.py"]` and `["sh", "-c", "bash"]` come back unchanged.
- **AC4** — When `GOV_BASH` names something that does not run, `resolve_bash` raises `Refusal`
  rather than falling through to another shell.
- **AC5** — When `resolve_shell_argv` is neutered, `python tools/govkit/selftest.py` fails the
  rewrite arm; with it intact the suite prints `govkit-selftest: all arms held`.
- **AC6** — When `GATE_FULL=1 bash tools/run-gates/run-gates.sh` runs, it reports
  `gates GREEN — 88/88 legs passed`.

## 7. Gates

`govkit acceptance matrix` · `govkit selftest` · `lexicon naming predicates` ·
`codebase-map coverage + freshness` · `kit version markers`. No new leg: the arms ride the selftest
leg that already exists, which is what `tools/gate-legs.json` says a kit's arms do.

## 8. Open questions

none — the one fork this unit carried is resolved and recorded in §3, namely whether to converge the
three `resolve_bash` copies here or file them. Filed, as `TOOL-dSettledRoster-6`.

## 9. Revision log

- rev-1 · 2026-08-20 · written retroactively, after the work landed at `474043e` and `d2a40aa`, at
  the owner's request. No earlier revision existed; this is not a reconstruction of one.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "resolve the bash executable that shares this filesystem"`
was run and its answer changed this section from what the build assumed. THREE `resolve_bash`
functions exist, not the two the gotcha named:

| Copy | Probe | Shape |
|---|---|---|
| `tools/memory-tree/corpus_ids.py:158` | `-c ":"` | PATH scan, refuses System32/WindowsApps, raises |
| `tools/run-gates/profile_bar.py:239` | `test -f "$script"` | fixed candidate list, returns `(bash, tried)` |
| `tools/govkit/govkit.py:442` | `-c ":"` | PATH scan, refuses System32/WindowsApps, raises |

The govkit copy follows `corpus_ids`, deliberately: a kit that is COPY-INSTALLED as a standalone
directory cannot import across kit boundaries, which is the same constraint that makes
`tools/lib/resolve-python.sh` an inlined block rather than a shared module.

`profile_bar`'s probe is the stronger of the two and is worth reading before any convergence: it
asks whether this bash can STAT THE SCRIPT, which is the property that actually matters, where the
other two only ask whether it starts. No existing seam was reusable as-is, and the divergence is now
tracked rather than left for the next reader to rediscover.
