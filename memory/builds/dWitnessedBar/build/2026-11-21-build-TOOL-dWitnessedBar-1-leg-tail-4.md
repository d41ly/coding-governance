# TOOL-dWitnessedBar-1 leg-tail 4 — shell hygiene (a fixed-name temp renamed into place) failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** shell hygiene (a fixed-name temp renamed into place)
- **Hash:** b826b300adeae7038be4e30a341ae656474fd62c
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg shell hygiene (a fixed-name temp renamed into place) | exit 1
sh-hygiene: temp names — 80 tracked shell source(s) scanned, 79 `mv` command(s) read
sh-hygiene:   [GATED] 29 site(s) in 15 file(s) — an `mv` whose source names a temp no unpredictable part names
sh-hygiene:   [admitted] 49 site(s) in 10 file(s) — the source, or the one binding it follows, holds `$(mktemp`, or is bound by a binder whose body holds `mktemp` and expands `SRANDOM` only beside `${SRANDOM:-`
sh-hygiene:   [unfollowed] 1 site(s) in 1 file(s) — a source that is one positional parameter, or one expansion with no binding in its scope or whose binding is itself one expansion or one positional, or no source on the line — counted, never gated
sh-hygiene:   unfollowed — tools/run-gates/run-gates.sh@db46050c:4898  "$f"
sh-hygiene: registered — .githooks/pre-push: `fixed-temp` × 2
sh-hygiene: registered — skills/session-kickoff/card-store.fixture.sh: `fixed-temp` × 8
sh-hygiene: registered — skills/session-kickoff/manifest-check.sh: `fixed-temp` × 5
sh-hygiene: registered — tools/branch-reconcile/adopt-branch-reconcile.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/check-template-size.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/check-wiring.sh: `fixed-temp` × 2
sh-hygiene: registered — tools/codebase-map/adopt-codebase-map.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/lib/health-log.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/memory-recall/adopt-memory-recall.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/memory-tree/adopt-memory-tree.sh: `fixed-temp` × 2
sh-hygiene: registered — tools/push-main.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/run-gates/post-merge.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/run-gates/run-gates.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/runlog/adopt-runlog.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/unattended/adopt-unattended.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/unattended/lib-unattended.sh: `fixed-temp` × 1
sh-hygiene: registered — tools/unattended/unattended.sh: `fixed-temp` × 2
sh-hygiene: 3 finding(s). A temp written at a name anyone can know before the write is a name a process that can write its directory can plant a link at, and the write goes through the link.
  .githooks/pre-push: the registry declares `fixed-temp` and the scan no longer finds it — delete the row, or a drained site leaves a widened exemption behind
  tools/run-gates/run-gates.sh: the registry declares 1 site(s) at `fixed-temp` and the scan measures 2 — the count may fall with the sites and may not rise
    tools/run-gates/run-gates.sh@db46050c:949  "$_hl_log.trim.$$"
    tools/run-gates/run-gates.sh@db46050c:6098  "$_tp.cut"
  tools/unattended/unattended.sh: the registry declares `fixed-temp` and the scan no longer finds it — delete the row, or a drained site leaves a widened exemption behind
sh-hygiene: remedy — name the temp so nobody can know it before the write creates it, beside its destination: `t=$(mktemp -u "$dest.XXXXXXXX")`, or a binder, a function whose body sets `printf -v "$1"` from `$SRANDOM` only behind the test `[ -n "${SRANDOM:-}" ]` and from `$(mktemp -u "$2.XXXXXXXX")` otherwise, called as `<binder> t "$dest"`
```
