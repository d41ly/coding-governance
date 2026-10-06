# TOOL-aMendedFleet-1 — acceptance ledger

**Serves:** journal TOOL-aMendedFleet-1

**Evidences:** TOOL-aMendedFleet-1
- AC1 — `grep -c write_ask_views tools/unattended/unattended.sh` — prints 3 after the restore and 0 at HEAD `d3695f29`; `grep -c -F 'filed=$((filed + 1))' tools/unattended/unattended.sh` prints 1 after, 0 before
- AC2 — `awk '/^write_ask_views\(\)/{p=1} p{print} p&&/^}/{exit}'` — the 79-line cut from the working file is `diff`-empty against the same cut from `ef1dcdb61` and from `e6e55d5ab`
- AC3 — `python tools/lexicon/lexicon.py --suggest write_ask_views --as sh.function` — prints `OK — write_ask_views leads with write`; `grep -c 'fail 69 ' tools/unattended/unattended.sh` prints 1. The slice is the driver suite's prologue (lines 1 to 142, `add_facts`, `slice_fn`), its closing-review F4 block and its `TOOL-dMendedRecall-2` section, cut into one script under the session scratchpad with `HERE` pinned to the kit it grades. Over a clone of HEAD `d3695f29` it executed 61 assertions and FAILED 20 of them, `f4-views-double: 1 filed` among them; over the restored driver the same 61 PASSED
- AC4 — `grep -c -F` — `asks as pinned`, `asks moved at HEAD`, `worktree holds the run`, `worktree not the run` and `worktree unanswerable` each print 1 over `tools/unattended/VERBS.template.md`; the entry cut by `awk '/^- .--status. /,/^- .--audit. /'` carries `check 73` and `check 58` twice each and `lease-utc` once; `LANDED (attended)` prints 0. The cut is `diff`-empty against the same cut of `ef1dcdb61`, and `verb_status` is byte-identical at `ef1dcdb61` and at HEAD, so the entry describes the line HEAD prints
- AC5 — `cmp tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` — exits 0 after `bash tools/unattended/adopt-unattended.sh` re-copied the render, and `--check` prints `in sync`
- AC6 — `grep -c dUnstuckLanding tools/unattended/unattended.sh` — prints 0 after the restore, as at HEAD. The census of every other file merge `01c22e155` conflicted on, and any restore it owes, is `TOOL-aMendedFleet-2`'s; this unit restores only the driver and the verb contract

## Per conflicted file of `01c22e155`

- `tools/unattended/unattended.sh` — restored here: the header sentences, `write_ask_views`, the `filed` counter and the call.
- `tools/unattended/VERBS.template.md` — restored here: the `--status` entry, with its render re-copied.
- Every other path that merge resolved is `TOOL-aMendedFleet-2`'s census.

## For the reconciler when node d's branch lands

Three hunks meet this restore: the auto-file header paragraph, `write_inherited_asks`'s `local`
line, and the `--status` entry's phase sentence. In each, node d's side is this side plus its own
units' additions (the BLOCKER-counts-as-HIGH sentence with its `sev` local, and the attended LANDED
phase form), so the reconcile takes node d's side and loses nothing.

## A stale figure in the spec

§4's table calls HEAD's `--status` entry a 3-line entry; it was 6 lines (87 to 92 of the template).
The act is unchanged, the whole entry is replaced by the parent's 29 lines, so no rev bump was owed.
