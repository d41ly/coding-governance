# TOOL-dFairHearing-31 — the version-line check resolves the bar's own base first, and refuses by name when it cannot, rather than passing on an empty diff

**Status:** DEFERRED · rev-2 · 2026-10-23 · node d · Tier-2 · base 3708a705 · streams tooling · order 22 · advances TOOL-dFairHearing-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-23-build-TOOL-dFairHearing-31-deviation-311.md](../build/2026-10-23-build-TOOL-dFairHearing-31-deviation-311.md) | deviation | — |
| [2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-28-promoted-fix-brief.md) | research | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-32 |
| [2026-10-23-prompt-TOOL-dFairHearing-31-1-spec-writer.md](../prompts/2026-10-23-prompt-TOOL-dFairHearing-31-1-spec-writer.md) | journal | — |
| [2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md](../reviews/2026-10-23-review-TOOL-dFairHearing-28-32-spec-audit.md) | spec-audit | TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-32 |

<!-- /gen:spec-records -->

## 1. Goal

The round-3 spec audit's finding id 34 (item H3, HIGH,
`memory/builds/dFairHearing/reviews/2026-10-23-review-TOOL-dFairHearing-4-14-25-27-spec-audit.md`) is
closed. `TOOL-dFairHearing-27` S15 and AC10 check that no version line changed by diffing from
`$(git merge-base HEAD main)`, and pass when the pipeline prints nothing. With no local `main`, git
prints `fatal: bad revision ''` on stderr, stdout stays empty, and the check passes having diffed
nothing. This unit replaces that check with one that resolves its base first, the same base the merge
bar's guards diff against, refuses with exit 2 and the reason when it cannot, and only then reads the
diff.

## 2. Scope (IN)

- **S1** — The base. `GATE_BASE` when it is set, verified by `git rev-parse --verify`; otherwise the
  merge-base of `HEAD` with `refs/remotes/<remote>/<observed>`, where `resolve_remote` in
  `tools/lib/resolve_remote.py` names the remote and the branch its `HEAD` observes. That is the
  baseline `tools/run-gates/README.md:404-410` states and `tools/run-gates/run-gates.sh:395-405`
  computes. A local branch named `main` is never read. Observed by AC1 and AC2.
- **S2** — Every input is asserted before the diff is read. A ladder refusal, no remote, a remote
  whose `HEAD` names no branch, a `GATE_BASE` that does not resolve, no merge-base, or a `git diff`
  that exits non-zero each exits 2 with `version-lines: no base, nothing diffed:` and the reason. Each
  git call is its own call with its own exit status, never a command substitution inside a pipeline.
  Observed by AC2.
- **S3** — The rule's observation, on that base. The check prints `base <sha> from <source>`, then
  every base-side line of the diff, a line opening with `-`, over `tools/hooks`, `tools/roles`,
  `.claude/skills/build` and `tools/workflows` that matches unit 27 S15's version-line pattern, and
  exits 1 when it printed one and 0 when it printed none. Observed by AC1 and AC3.
- **S4** — Supersession. Unit 27 S15's sentence naming `git merge-base HEAD main` as the check's base,
  and unit 27's AC10, are answered by this unit's S1 to S3 and AC1 to AC3. Unit 27 S15's version rule
  itself stands. Unit 27's acceptance ledger records them superseded here (`TOOL-dFairHearing-23` §8
  F7's form). NOT OBSERVED by a criterion of this unit: it is a ledger entry in unit 27's record, read
  there.

## 3. Non-goals (OUT)

- No change to the version rule: no commit of this build changes the value of an existing version
  line, and a new file's marker carries its kit's version (unit 27 S15).
- No new gate leg and no committed checker. The check runs once at this unit's pass as a scratch
  probe, as unit 27 AC10 did, and `kit version markers` keeps its own job.
- No inline copy of the remote ladder. The probe imports the canonical module and ships nowhere, so
  the parity table in `tools/lib/resolve-python.test.sh` has no new copy to hold.
- No help page: `help/` covers no build-time check.

### Edges

- **consumes-from** `TOOL-dFairHearing-27` — S15's version rule and the version-line pattern AC10 reads; this unit corrects how that check finds its base
- **hands-off** `TOOL-dFairHearing-32` — finding id 20 of the same audit, the baseline from the bar's remote ladder rather than local `main`, which S1 takes and that unit names
- **hands-off** `TOOL-dFairHearing-33` — finding id 22 (item H1, shared with id 31) of the round-4 spec audit: every declared kit version constant read by its own pattern; S3's constant alternative and AC1's constant clause are superseded there
- **hands-off** `TOOL-dFairHearing-34` — finding id 31 (item H1, shared with id 22) of the same audit: every gov:kit marker in every file the build modified; S3's four-directory pathspec, its marker alternative and AC1's marker clause are superseded there
- **hands-off** `TOOL-dFairHearing-36` — the same audit's minors on this spec, ids 9, 18 and 19: GATE_BASE taken unchanged and the ladder base read through resolve_compare_base, superseding S1's computation in §4 (its S11 to S13)


## 4. Design

### Evidence

Measured on 2026-10-23 with the script below. In this worktree it printed `base 3708a705… from
origin/main` and exited 0. `GATE_BASE=nosuchref` exited 2 naming the ref. `GOV_REMOTE=nosuch` exited 2
with the ladder's own refusal. In a fixture clone under `%TEMP%` whose branch rewrote `const
KIT_X_VERSION = '1.0'` to `'1.1'`, it printed `-const KIT_X_VERSION = '1.0'` and exited 1; with the
fixture's remote removed it exited 2. The unit 27 AC10 command, run with `nosuchbranch` in place of
`main`, prints nothing on stdout and so passes (the audit's id 34).

### The check

```python
# version_lines.py <repo root> [<lib dir>] — unit 27 S15's version check, its base resolved or refused
import os, re, subprocess, sys
root = sys.argv[1]
sys.path.insert(0, sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, "tools", "lib"))
from resolve_remote import resolve_remote
def git(*a):
    p = subprocess.run(["git", "-C", root, *a], capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()
def refuse(why):
    print(f"version-lines: no base, nothing diffed: {why}", file=sys.stderr)
    sys.exit(2)
if os.environ.get("GATE_BASE"):
    ref, how = os.environ["GATE_BASE"], "GATE_BASE"
else:
    remote, _branch, observed, refusal = resolve_remote(root)
    if refusal or not remote or not observed:
        refuse(refusal or "no remote, or its HEAD names no default branch")
    ref, how = f"refs/remotes/{remote}/{observed}", f"{remote}/{observed}"
rc, tip, err = git("rev-parse", "--verify", "-q", ref)
if rc or not tip:
    refuse(f"{how} does not resolve: {ref}")
rc, base, err = git("merge-base", "HEAD", tip)
if rc or not base:
    refuse(f"no merge-base of HEAD and {how}: {err}")
rc, diff, err = git("diff", "-U0", base, "HEAD", "--",
                    "tools/hooks", "tools/roles", ".claude/skills/build", "tools/workflows")
if rc:
    refuse(f"git diff exited {rc}: {err}")
print(f"base {base} from {how}")
hits = [l for l in diff.splitlines() if re.match(r"^-.*(KIT_[A-Z_]+_VERSION = |gov:kit [a-z-]+@)", l)]
for l in hits:
    print(l)
sys.exit(1 if hits else 0)
```

The pass writes it with its file-writing tool under its scratch directory. It reads the OBSERVED
branch and never `GOV_DEFAULT_BRANCH`, as `run-gates.sh` does for its scope base (its comment above
`DEFBR`), so an environment value cannot move the base. Unlike the bar, it does not fall back to the
remote tip when the merge-base equals `HEAD`: the diff is then empty because nothing changed, which is
a true pass.

### Files touched (estimate)

None. The check is a scratch probe, and its result is a line in this unit's acceptance ledger.

### Alternatives rejected

- **Keep the shell one-liner and add `|| exit 2`.** In `$(git merge-base …)` inside a pipeline the
  status that reaches `||` is the last command's, the unreachable-branch class
  `TOOL-aWrittenMethod-4` records. Separate calls with separate statuses cannot hit it.
- **Use `GATE_PUSH_BASE`.** It is set only inside a bar run, and this check runs at a unit's pass,
  where no bar runs.

## 5. Production-readiness checklist

- security — N/A: a read-only scratch probe that runs git with argv lists and no shell.
- perf / scale — four git calls.
- error / empty / loading states — every input that can be empty or fail is asserted, and each
  refusal is exit 2 naming its cause, so an empty diff is never read from a failed call.
- observability — the base and where it came from print before any finding.
- risks — a run with no fetched remote refuses rather than passes; the pass fetches or sets
  `GATE_BASE`, and the refusal names that.
- testing — AC1 to AC3 as probes and a fixture.
- migration — none.
- user docs — N/A: no user-facing surface.

## 6. Acceptance criteria

`version_lines.py` is the script of §4, written under the pass's scratch directory.

- **AC1** — When `python version_lines.py .` runs at this unit's commit, it prints `base <sha> from
  origin/main`, where `<sha>` equals `git merge-base HEAD origin/main`, prints no `-` line, and exits 0.
  Red when: a version line that existed at the base changed on the branch, or the base printed is a
  local branch's merge-base.
- **AC2** — When the same probe runs with `GATE_BASE=nosuchref`, and again with `GOV_REMOTE=nosuch`,
  each exits 2 and prints `no base, nothing diffed` with its reason before any `base` line. In a
  fixture clone with its remote removed, it exits 2 the same way.
  Red when: any of the three exits 0, which is the vacuous pass finding id 34 names.
  fixture: the clone under `%TEMP%/fvb`, cloned from a one-commit repository under `%TEMP%/fva`, made
  by the probe and removed after it.
- **AC3** — When the fixture clone's branch rewrites `const KIT_X_VERSION = '1.0'` to `'1.1'` in its
  hook file `x.js`, under the fixture's hooks directory, and the probe runs over it with this
  repository's library directory as its second argument, it prints `-const KIT_X_VERSION = '1.0'` and
  exits 1.
  Red when: the probe exits 0 on a changed version line, which means its pattern or its base reads
  nothing.

## 7. Gates

`kit version markers` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the check is a scratch probe, observed directly by §6.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-23 · initial draft, promoting finding id 34 (item H3, HIGH) of the round-3 spec
  audit of specs 4, 14, 25, 26 and 27.
- rev-2 · 2026-10-23 · §3 · the round-4 spec audit's disposal: hands-off edges to TOOL-dFairHearing-33 and -34 (item H1,
  ids 22 and 31) and TOOL-dFairHearing-36 (three minors on the base).

## 10. Reuse audit

The seam extended is the remote ladder, `resolve_remote` in `tools/lib/resolve_remote.py`, which
`tools/run-gates/run-gates.sh` (its shell twin, :366-405) and `tools/push-main.sh` already use to find
the default branch. `python tools/codebase-map/reuse_lookup.py "resolve the merge base with the
remote default branch or refuse"` ranked `resolve_kit_dir`, `resolve_python` and the generic
`resolve` and `merge` stems; the ladder was found by reading the bar's baseline block. The recall query
returned `TOOL-aWrittenMethod-4`, the substitution-status class §4 avoids, and the audit's H3 item.

Recall terms used: `python tools/memory-recall/query.py "a check that passes on empty output when its command substitution failed" --terms "merge-base command substitution empty stdout vacuous pass version line hand bump GATE_BASE remote ladder default branch"`
