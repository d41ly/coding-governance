**Serves:** research TOOL-dTendedCadence-1 TOOL-dTendedCadence-16

# dTendedCadence — the parents cross-check readers' returns, verbatim

The `gov-spec-reviewer` returns the cross-check record [`2026-11-03-build-TOOL-dTendedCadence-1-parents-crosscheck`](2026-11-03-build-TOOL-dTendedCadence-1-parents-crosscheck.md) is assembled from, extracted by script from each agent's transcript and not retyped. The brief is [`2026-11-03-prompt-TOOL-dTendedCadence-1-parents-crosscheck`](../prompts/2026-11-03-prompt-TOOL-dTendedCadence-1-parents-crosscheck.md); each group's handoff sits beside it.

## Group, led by spec 1 (specs 1, 2, 8, 16, 50 and 69)

I found no MISMATCH. Specs 1 and 16 rely only on wm6 S1 and S12. Commit `66f7b8d32` left both sections unchanged: its diff has hunks only in the status line, the records table, S6, S7, §8 F4 and §9. None of the six specs cites wm58, wm41 or tr2, and none reads a lease's `session`, `lease`-mode class or `epoch`.

**1. Assumptions**

| Spec | Assumption about the parent | Rule | Verdict | Evidence |
|---|---|---|---|---|
| 1 | The flow's executor is the supervisor. It asks `position.py <slug>`, so it walks a build keyed by slug, and no parent walks a cadence program keyed by (cadence, period). | cite | AGREES | tc1:156-158 "The flow's executor is the supervisor (TOOL-dWellOiledMachine-6 S1), which asks `position.py <slug>` … and so walks a build, keyed by slug" · wm6:45-50 "`python supervise.py run <slug> --epoch <n>` … the position engine's answer, read by running the loop kit's verb `python position.py <slug> --json`". S1 has no hunk in `66f7b8d32`. |
| 1 | F2 (b): the supervisor walks only a build and has no key for a period, so `maintain.py` walks the items and ask TOOL-dTendedCadence-28 retires it. | cite | AGREES | tc1:293-296 "(b) the supervisor, which asks `position.py <slug>` and so walks only a build (TOOL-dWellOiledMachine-6 S1 …). (b) has no key for a period" · wm6:45-50, as above. |
| 1 | The program never reads a lease holder. It learns its key from `GOV_CADENCE_KEY` (F3 (a)), and F3 rejects (c), reading back the lease and parsing the lease record. | RH | AGREES | tc1:301-304 "(c) reading back the lease this node holds … (c) parses a lease record format TOOL-dPlacedRequest-1 owns" · tr2:345-347 (c) "a second parser of the record its S2 keeps in `read_claims`", rejected; wm6:343-345 (c) "a second parser of the record `read_claims` is the one parser of". |
| 16 | `act-launch`, `act-exit` and `act-killed` are journal classes wm6 S12 adds, each line keyed by `act=`. | cite | AGREES | tc16:38-39 "TOOL-dWellOiledMachine-6 S12 and -47 S4, the journal classes `act-launch`, `act-exit` and `act-killed`" · tc16:165 · wm6:141-143 "`act-launch`, `act-adopt`, `act-killed`, `act-exit`, `relaunch` and `limit-hold` join `JOURNAL_CLASSES` … each line keyed by `act=`". S12 is unchanged. |
| 16 | S1's population: an `act-launch` with no later `act-exit` or `act-killed` is a missed reap, and "a supervisor that died mid-act leaves exactly this". The reconcile's kills close such lines with `act-killed`. | cite | AGREES | tc16:50-57 · wm6:100-106 (rev-5 S6): "every other live candidate has its tree killed through `run_kill_tree` … and is journaled `act-killed`". The revision moved only S6's epoch source (wm6:101-103, now the holder verb), not what it journals. The fence keeps `act-killed` too: wm6:110-111 "journal `act-killed` with `reason=fenced`". |
| 16 | Under `lease-holder`, the period run (the holder itself) reads its own node-scoped rows and names as unread the nodes whose `<period>.<node>` node-pass lease key appeared in an earlier period but not this one. No foreign session or epoch is read. | RH | AGREES | tc16:101-107, tc16:339-345 "(a) reads only Maintain's own leases" · tr2:340-355 and wm6:97-111. The verb is needed only for `session`, `lease`-mode class or `epoch`, and the node is a segment of the lease key. |

**2. MISMATCH**

- None.

**3. UNKNOWN UNTIL BUILT**

- None. No assumption in these six specs depends on the holder verb's output shape, which only dPlacedRequest's build run (asked by dTotalRecall's run) decides.

**4. Rule-wide hits RH does not bind**

- tc2:45-49 ("only the period's lease holder reads node-scoped readings"): this describes TOOL-dTendedCadence-16 §8 F5's fallback. The holder is the node that took its own period lease, and nothing reads another session's holder or epoch.
- tc2:41, :89-92 (`every-session` keyed by the waking session): the waking session's own `session_id` comes from the SessionStart payload, and no lease is read.
- tc2:202-203 ("a build no lease holds"): this describes the wake behaviour of TOOL-dWellOiledMachine-18 S4 in a rejected alternative, so nothing is read.
- tc8:62-66: `<event>.<sha12>` is the period segment of a lease that `run_cadence_period` takes and releases itself (wm13 S6). It reads no holder or epoch.
- tc1:66-72, :177, :217-218: `run_cadence_period` takes and releases the period lease itself (wm13 S6). The program reads its key only from `GOV_CADENCE_KEY`.
- tc50:182 and tc69:137: `read_claims` is cited only as the bounded fetch shape that the maintain-record verb ports. It fetches `refs/gov/maintain-record/<key>` (tc50:35, tc69:31-40), not a lease.
- tc16:34, :91-107, :134-135, :280-283 (`lease-holder`): this is the policy value of `maintain.node-readings`, the same class the brief already judged unbound for 6, 48, 55 and 74. The S6/F3 unread-nodes read takes the node from the lease key and is covered by the RH row above.
- Parent text, no verdict: wm6:343 and wm6:366 cite TOOL-dTotalRecall-2 §8 F6 as `tr2:337-354`, but F6 runs from tr2:340 to tr2:358, and tr2:336-339 is F5.

**5. Revised sections cited but not depended on**

- Spec 1: none. It cites only wm6 S1, which is unrevised, and both of its assumptions depend on it. It does not cite the revised S6, S7 or §8 F4.
- Spec 16: none. It cites only wm6 S12, which is unrevised and depended on. Its S1 reading also relies, without citing them, on S6 and S7 journaling `act-killed`, which the revision kept.

Probes, all read-only, on `66c5b8dbf`:
- `git show 66f7b8d32 -- <wm6 spec>`: hunks only at the status line, the records table, S6/S7 (wm6:97-111), F4 (wm6:340-351) and the rev log.
- `git log --oneline 7e48dac37..66c5b8dbf -- memory/builds/{dWellOiledMachine,dTotalRecall,dPlacedRequest}/spec`: printed only `66f7b8d32`.
- `grep -nE 'WellOiledMachine-(6|41|58)\b|dTotalRecall-2\b|--claims|read_claims|holder|epoch|refs/gov/leases|--lease'` over the six specs: no `--claims`, `--lease`, wm41, wm58 or tr2 hits.

Files:
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-1.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTendedCadence\spec\2026-11-01-spec-TOOL-dTendedCadence-16.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dWellOiledMachine\spec\2026-10-26-spec-TOOL-dWellOiledMachine-6.md
- C:\projects\coding-governance\.claude\worktrees\modest-gates-539d2a\memory\builds\dTotalRecall\spec\2026-10-26-spec-TOOL-dTotalRecall-2.md
