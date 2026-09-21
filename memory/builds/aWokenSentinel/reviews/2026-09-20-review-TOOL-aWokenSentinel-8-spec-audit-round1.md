**Serves:** spec-audit TOOL-aWokenSentinel-8 TOOL-aWokenSentinel-9 TOOL-aWokenSentinel-10 TOOL-aWokenSentinel-11 TOOL-aWokenSentinel-12 TOOL-aWokenSentinel-13 TOOL-aWokenSentinel-14
**Commissions:** TOOL-aWokenSentinel-15..20

# aWokenSentinel — spec audit of units 8 to 14, round 1

*Node `a`, 2026-09-20. A Tier-2 adversarial pass over the seven specs the first audit commissioned,
before any code: a fan of four primed finder lenses, a skeptic stage in five batches prompted to
REFUTE each finding, one synthesis. The mandate was the same as round 1 over units 1 to 7:
underspecification, contradiction between sibling specs on the four axes (scope, interface,
ordering, acceptance), unstated assumptions about the harness and the driver, and criteria that
cannot fail, with every code claim checked against the cited file and line at the build's base
`12b3701d`. The synthesis re-read at source every claim the blockers and the highs rest on; what it
re-read, and what it did not run, is listed at the end.*

**Round: 1.** Subjects, each pinned at the blob the commission named:

- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-8.md@c2fd0d5a5f32c7f751b3ea84b8df1bea09e6ad58`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-9.md@d241f4b7958d9662a2f9942e78b563f510fb4753`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-10.md@ff874698f65ca1fe2e903cf60462022072cd5280`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-11.md@953038571cd66161667301c45946d8bd83168ad0`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-12.md@4002785192264027d6cfec509630979692010324`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-13.md@3abcd944460363a52d783d4efd668ee0bb7b95fb`
- `memory/builds/aWokenSentinel/spec/2026-09-20-spec-TOOL-aWokenSentinel-14.md@ec32b199fcbb3d60e31c708e57ce3a54fe4a08bd`

Two of those pins do not name the text that was reviewed. Specs 8 and 14 sit in the working tree as
UNCOMMITTED rev-2 edits (blobs `f76fbb8d` and `cd122750`), and every lens read the working tree.
The synthesis re-verified that at the time of writing: `git rev-parse HEAD:<path>` prints the
pinned blob, `git hash-object <path>` prints the other, and `git status` lists both as modified. The
diff on each is confined to the Status line, the §3 edge bullets and a §9 log line; §4 to §8 and §10
are byte-identical between the pinned and the reviewed text, so every design finding below holds
against both.

## Verdict: BLOCKED

Two blockers stand, and both are provenance rather than design: the audit was commissioned at a blob
that is no longer the file for specs 8 and 14, and the rev-2 that replaced it is not yet committed,
so the next commit can move it again and no disposition recorded against the pinned blob is a
disposition of the text in the tree. Committing the two rev-2 folds and re-pinning closes both. Six
high defects follow, and these are design. Spec 8's central claim — that the new row closes the
`--landed` loop — is untrue for the landing shape the charter mandates, because `--landed` refuses
on check 34 after every `--no-ff` landing (an OPEN backlog row the spec cites for a different
reason), so the row spends its block budget and the record wedges at `LANDING` by another route.
Spec 9's §4 states the status line's field order backwards from the driver's own `printf` and its
AC1 cannot hold with its own sketch. Three arms are specced so that they can only ever be seen
passing (spec 9 AC3, spec 13 AC2's liveness half, and spec 14's S2, which no criterion runs), and
spec 11 rests its whole check on a count that no sibling criterion pins. Every unit but 10 drew at
least one confirmed finding; unit 10's one finding is a residue in spec 3 that its declared default
exposes.

## Review shape

Raw 53, confirmed 31, refuted 22, unverified 0, precision 0.58. That sits above the ~0.5 floor §8
sets, but closer to it than round 1's 0.80. Eight of the 31 confirmed ids are the two moved-spec
provenance findings reported once per lens, which the pipeline's dedup did not collapse; on the
design content alone the fan's precision is lower than the headline figure, and round 2 should run
the blob-pin check as a pre-flight of the commission rather than leave it to four lenses to find
four times each.

**Run integrity.** Lenses 4/4 returned, 0 died. Skeptic batches 5/5 returned, 0 died. 0
contradictory verdicts demoted to unverified, 0 spurious verdicts discarded, 0 duplicates removed by
the pipeline's dedup stage. The run is complete on its own terms. Because no lens died, no zero
below is a zero from absence; every unit was read by all four lenses. The pipeline's dedup found 0,
but the 31 confirmed ids contain several that name one defect from different lenses (four found each
moved spec, two found spec 9's field-order contradiction, two found the same gotcha-record gap on
specs 12 and 14, two found spec 13 AC4 from two angles). The fold below is editorial: it groups them
into 22 distinct defects and keeps every raw id. Each raw id takes the severity of the defect it
evidences, so the per-id tally and the integers returned with this report agree by construction.

| Defect | Severity | Raw ids folded in |
|---|---|---|
| B1 spec 8 moved after commissioning; the rev-2 is uncommitted | blocker | 1, 20, 32, 47 |
| B2 spec 14 moved after commissioning; the rev-2 is uncommitted | blocker | 2, 21, 33, 46 |
| H1 spec 8's row cannot close the loop on a `--no-ff` landing: check 34 refuses `--landed` there | high | 48 |
| H2 spec 9 §4 states the field order backwards from the driver; AC1 and the sketch contradict | high | 34, 49 |
| H3 spec 9 AC3's one-line arm cannot red against the named staged break | high | 3 |
| H4 spec 13 AC2's liveness half cannot red against the named staged break | high | 4 |
| H5 spec 14 S2 is observed by nothing that runs the adopter suite; §5 says AC2 does | high | 5 |
| H6 spec 11's "count is 1 by unit 2's AC7" is a false cross-reference; a comment makes it 2 | high | 36 |
| M1 spec 8 AC4's `grep -c` threshold is met by code alone; the header sentence is unobserved | medium | 6 |
| M2 spec 13 hands unit 6 a sentence spec 5 already writes; the edge has no reciprocal | medium | 22 |
| M3 spec 13 AC4 observes neither half of S2 (no differing key, no attempt lines) | medium | 18, 23 |
| M4 spec 12 AC2's header sentence has no writer on the expected path | medium | 24 |
| M5 spec 12's `consumes-from` unit 2 has no `hands-off` back | medium | 25 |
| M6 spec 9's `consumes-from` units 5 and 3 have no `hands-off` back | medium | 26 |
| M7 spec 13 §4 drops the empty-initialisation guard §10 cites; the environment can override | medium | 39 |
| M8 specs 12 and 14: the gotcha record as specced reds `gotchas.py --check` 17 and 18 | medium | 41, 42 |
| M9 spec 11 exempts the tick's second spelling on a reason `lib-unattended.sh` answers | medium | 50 |
| M10 spec 14's seed commit drops the kit's ambient-config guard; a third seed idiom | medium | 53 |
| L1 spec 8 Files touched rewrites an arm that does not exist and omits one that does | low | 27 |
| L2 spec 3 AC2 still carries `block 1/12`; spec 10's declared 6 contradicts it | low | 30 |
| L3 spec 11 §7 "no floor exists in this suite" is false | low | 38 |
| L4 spec 8 counts "six records at LANDING"; the tree holds four | low | 45 |

Tally by raw id: **8 blocker · 7 high · 12 medium · 4 low** = 31. One severity was RAISED from the
skeptic's verdict: 18 (skeptic: low) sits in M3 beside 23, because the two ids are two halves of one
defect — AC4 is the sole observation of S2 and observes neither the differing declaration nor the
cap — and one defect has one severity. No severity was folded down. H1 (raw 48) was weighed for
blocker and left at high, argued in its section: the unit does not invert its purpose the way round
1's B1 did, it degrades to the pre-build state on the mandated landing shape, and the fix is a
sentence in the reason text plus one payload.

## Findings

| # | Sev | Unit(s) | Address | One line |
|---|---|---|---|---|
| B1 | blocker | TOOL-8 | Status header; §3 Edges; §9 | Pinned `c2fd0d5a`, working tree `f76fbb8d`, uncommitted rev-2; the pin names a text that is now history. |
| B2 | blocker | TOOL-14 | Status header; §3 Non-goals and Edges; §9 | Pinned `ec32b199`, working tree `cd122750`, uncommitted rev-2; same defect. |
| H1 | high | TOOL-8, TOOL-7 | TOOL-8 §4 'The loop this closes' step 3, §2 S2, §5 risks, §10 | On a `--no-ff` landing the run worktree's HEAD is the merge's second parent; check 34 refuses `--landed` every time (OPEN `TOOL-dUnstalledConvoy-38`), each refusal spends a block, `blocks-exhausted` allows, the record wedges at `LANDING`. |
| H2 | high | TOOL-9 | §4 'The field' word-order paragraph; §6 AC1 last clause; §3 non-goal | `unattended.sh:2975` prints `$parked` as the LAST operand, so every suffix lands after `next`; §4 says the inverse while its sketch appends to `$parked`; AC1 cannot hold with §4's code. |
| H3 | high | TOOL-9 | §6 AC3 one-line arm, §6 preamble, §7 'New arm', §2 S4 | A driver copy with the field clause removed still prints one line; `wc -l` is 1 on both sides, so the arm is only ever seen passing. |
| H4 | high | TOOL-13 | §6 AC2 NOTE-path arm and REFUSED half; §2 S4 | Removing only the `. "$CONF"` line leaves `CONF=` set and the `[ -f ]` refusal in place; both NOTEs still name an existing path and the no-conf case still exits 2, so the liveness arm never reds. |
| H5 | high | TOOL-14 | §2 S2; §6 AC2; §5 risks row | AC2 runs `adopt-unattended.sh --check` once per fixture; nothing runs `adopt-unattended.test.sh`, which has no `gate-legs.json` row either, so the suite the edited seed feeds is exercised by no criterion and no bar. |
| H6 | high | TOOL-11, TOOL-2 | TOOL-11 §3 'No driver change', §4 'The check'; TOOL-2 §6 AC7 | Spec 2 AC7 pins `grep -c 'resolve_sidecar_dir'` ≥ 2, never the `rev-parse --git-dir` literal at 1; a header comment carrying it makes the unmodified driver read 2 at order 3 and no unit owns the red. |
| M1 | medium | TOOL-8 | §6 AC4; §2 S4; §4 'The block reason' | REASONS entry, `checkStop` branch and the `renderBlock` selector already make `grep -c` ≥ 3 with no header paragraph. |
| M2 | medium | TOOL-13, TOOL-6, TOOL-5 | TOOL-13 §3 Edges `hands-off` unit 6; TOOL-5 §4 Data model; TOOL-6 §2 S5, §3 | Spec 5 already writes the conf comment sentence; spec 6 expects to add none and declares no edge back; check 12 reds now on the full run. |
| M3 | medium | TOOL-13 | §6 AC4; §2 S2; §3 non-goal on a differing worktree value | The worktree conf holds no `RESUME_ATTEMPTS` (`grep -c` 0) so sourcing it cannot overwrite anything, and no attempt lines are seeded so "still caps it at 2" prints nothing distinguishable from 6. |
| M4 | medium | TOOL-12, TOOL-5 | TOOL-12 §6 AC2, §4 Files touched, §5; TOOL-5 §4 | AC2 greps the tick header for 'logged-out node kills nothing'; on the expected path neither spec writes that sentence into the header. |
| M5 | medium | TOOL-12, TOOL-2 | TOOL-12 §3 Edges `consumes-from` unit 2; TOOL-2 §3 | Spec 2 hands `pid-alive` to unit 5 only; check 12 reds now on the full run. |
| M6 | medium | TOOL-9, TOOL-5, TOOL-3 | TOOL-9 §3 Edges `consumes-from` units 5 and 3; TOOL-5 §3; TOOL-3 §3 | Spec 5 names unit 9 only inside the prose of its hands-off-7 bullet; spec 3 names it nowhere; two check-12 lines on the full run. |
| M7 | medium | TOOL-13 | §4 'The read, in the tick' snippet; §10 | `read_bound_key` reads `${!name}` from the calling shell including the environment; the driver clears the keys at `:336-339` before sourcing and the tick's snippet does not. |
| M8 | medium | TOOL-12, TOOL-14 | TOOL-12 §2 S4, §4 'The class, in `memory/gotchas/`', Files touched; TOOL-14 same | `gotchas.py --check` 17 needs `INDEX.md` regenerated and 18 needs a `gated by` / `no machine gate` phrase; neither spec names either; AC4 checks front matter only. |
| M9 | medium | TOOL-11, TOOL-5 | TOOL-11 §3 'No scan of resume-tick.sh or the hooks', §2 S2, §10; TOOL-5 §4 | `lib-unattended.sh` (the lib header's pointer, dUnstalledConvoy seq 22) is the ratified home for one spelling two scripts share, the tick already sources it, and spec 5 spells the root inline anyway; the exemption's reason is answered and not cited. |
| M10 | medium | TOOL-14 | §4 'The commit'; §10 | `check-playbook.test.sh:33-53` already commits under null global/system config for the ambient-state gotcha; the proposed `--no-verify` alone inherits global `commit.gpgsign` and the stated reason misreads config resolution. |
| L1 | low | TOOL-8, TOOL-3 | TOOL-8 §4 Files touched; TOOL-3 §6 AC3, §7 | No `FINISHED-UNSTAMPED` allow arm exists at order 6 to rewrite; the background-tasks arm §7 names is missing from the row. |
| L2 | low | TOOL-10, TOOL-3 | TOOL-3 §6 AC2 line 405 against line 408; TOOL-10 §2 S1 | AC2 requires a reason naming `block 1/12` three lines before it says the reason reads `block 1/6`; a rev-1 residue. |
| L3 | low | TOOL-11 | §7 'New arm' | `check-unattended.test.sh` declares `FLOOR_ASSERTIONS=410` at `:3252` and two shard floors at `:3277-3278`. |
| L4 | low | TOOL-8 | §2 S6; §4 'Why a BLOCK is the right answer'; §6 AC5 | Four run records sit at `LANDING` at base and at HEAD, not six; none carries `session:`, which is the property that matters. |

---

### B1 — blocker — TOOL-8 Status header, §3 Edges, §9 — raw 1, 20, 32, 47

**The defect.** The commission pinned spec 8 at blob `c2fd0d5a`; the file in the tree hashes to
`f76fbb8d` and `git status` lists it modified. The diff is the Status line (rev-1 → rev-2), the §3
Edges rewrite (the unit-2 `consumes-from` folded into the unit-3 bullet, the unit-6 `hands-off`
absence bullet dropped) and a §9 log line recording both as check-12 folds observed on a full hygiene
run at `12513c25`. Sections 4 to 8 and 10 are byte-identical. All four lenses read the working
tree, so every finding below on spec 8 is about `f76fbb8d`. A disposition recorded against the pinned
blob is a disposition of a text nobody can open in the tree, and because the rev-2 is uncommitted
the next commit could move it again before anything pins it.

**The fix.** Commit the rev-2 as it stands (the edits are the right folds for the check-12 lines the
§9 entry names) and re-pin this audit's subject at the committed blob in the build record, noting
that §4 to §8 and §10 did not move. Reverting to `c2fd0d5a` is the other closed option and re-opens
the two check-12 lines.

**Left-shift.** A pre-flight in the audit's commission step: `git hash-object` of each subject
against the pin, refusing to dispatch a lens while any differs or any subject is uncommitted. This
is gateable in the review harness and costs one process per subject; four lenses spent a finding
each on it here.

### B2 — blocker — TOOL-14 Status header, §3 Non-goals and Edges, §9 — raw 2, 21, 33, 46

**The defect.** Pinned `ec32b199`, working tree `cd122750`, modified and uncommitted. The diff is
the Status line to rev-2, the unit-2 `hands-off` absence bullet dropped from §3 Edges with its fact
moved into the first non-goal, and a §9 log line. Sections 4 to 8 and 10 are byte-identical. Same
disagreement between the commission's pin and the reviewed text as B1.

**The fix.** As B1: commit the rev-2 and re-pin at the committed blob, recording that the design
sections did not move.

**Left-shift.** The same pre-flight as B1; one check covers the class.

### H1 — high — TOOL-8 §4 'The loop this closes' step 3, §2 S2, §5 risks, §10, against `TOOL-dUnstalledConvoy-38` and `TOOL-aUnblockedFleet-7` — raw 48

**The defect.** The row's whole value is step 3 of the loop trace: the blocked session re-runs
`--landed`, which "prints `checked` and stamps `LANDED`". Two OPEN rows in `memory/backlog/TOOL.md`
say that re-run refuses in the ordinary case. `TOOL-dUnstalledConvoy-38`: on the `--no-ff` landing
the charter §3 mandates, `push-main.sh:118` writes the marker with the MERGE sha while the run
worktree's HEAD is the merge's second parent; check 34 at `unattended.sh:2476-2503` takes the
remote arm whenever HEAD is an ancestor of the advertised tip, sets `wit=$head`, and refuses unless
the marker carries it, so `--landed` refuses in the run worktree every time and its own text sends
the session to "re-run the lander", which cannot help. The recorded workaround is to fast-forward the
run branch onto the merge and re-run `--landed` in the same worktree. Running it from the primary
tree instead resolves a DIFFERENT per-worktree sidecar (spec 7 makes the sidecar per-worktree), so
that path reads `unchecked` or unit 7's S2 refusal rather than `checked`. `TOOL-aUnblockedFleet-7`
adds the concurrent-landing overwrite of the clone-shared marker. Spec 8 cites -38 only for its
idempotence half (§10) and names neither row in the loop trace or in §5, whose generic "anchor
mismatch" row prices the path as `blocks-exhausted → allow`. Under the new row each refusal ends a
turn and spends one of the shared `STOP_GUARD_BLOCKS`; after the budget the hook allows and the
record sits at `LANDING` with its work on `main` — the B1 outcome round 1 recorded, reached by a
longer route and after spending the budget every other row shares.

Why high and not blocker: unit 8 does not manufacture the wedge, it fails to route around one that
is already OPEN and recorded with its workaround, and the terminal state is the pre-build state
(a `LANDING` record with work on `main`) rather than a new trap. The fix is text plus one payload.

**The fix.** Cite -38 and -7 in §4 and §5. Have S2's reason text (or unit 7's check-34 refusal text,
through the existing `hands-off` edge) name the recorded workaround — fast-forward the run branch
onto the merge, then re-run `--landed` in the SAME worktree — so a session spends no block re-running
the lander. Add one stub-driver payload whose liveness is `FINISHED-UNSTAMPED` with a seeded marker
sha that differs from HEAD and observe that the reason still names the verb and the workaround.
State in §5 that the row's budget is shared and that a check-34 refusal costs one block per turn.

**Left-shift.** The real gate is -38's own fix (the marker's commit is on the remote default branch
AND has the witness as an ancestor), which is out of this unit's scope; until it lands, one arm in
`unattended.test.sh` that drives a `--no-ff` landing on a fixture remote and asserts `--landed`
reaches `LANDED` from the run worktree would be RED today and is the honest witness. For the audit
lens: a loop trace whose step is "re-run verb X" cites the backlog rows OPEN against verb X, as a
documented check.

### H2 — high — TOOL-9 §4 'The field' word-order paragraph, §6 AC1 last clause, §3 non-goal 'appended after them' — raw 34, 49

**The defect.** Re-read at source: `tools/unattended/unattended.sh:2975` is
`printf 'unattended: %s · phase %s · witness %s%s · next %s%s\n' "$slug" "$p" "${w:-NONE}" "$hc"
"$unit" "$parked"`. `$parked` is the LAST operand, so `· parked N`, `· noted M`, `· STALE briefs N`,
`· briefs gone N` and spec 5's resume-tick field (which spec 5 §4 also appends to `$parked`) all
print AFTER `next`; only `halt-code` sits before it. Spec 9 §4 says "the `next` field stays last and
this field sits before it, as `parked` and `noted` do" — false for `parked` and `noted` — while its own
sketch `parked="$parked · keepalive …"` puts the field after `next`. AC1's last clause requires "the
line still ends with the `next` field" and its red-when fires when "the field prints after `next`".
A builder following the sketch reds AC1; a builder satisfying AC1 inserts before `next`, breaking
the sibling convention the §3 non-goal keeps and the `sed 's/.*· next //'` reader at
`unattended.test.sh:1874` for every fixture that carries a suffix. That reader survives today only
because its fixture (`--preflight` then `--status`) accumulates nothing into `$parked`, which the
spec never states.

**The fix.** Restate §4 as the code has it: suffixes print after `next`, and the keepalive field is
appended to `$parked` as the last suffix. Drop the "before `next`" sentence and AC1's last clause;
assert instead that the field is the last `·`-separated field of the line and that the `:1874` and
`:1859` fixtures carry no suffix (or assert that precondition inside the arm), which is what actually
keeps those readers untouched.

**Left-shift.** One arm that runs `--status` on a fixture WITH a parked row and a stop line and
asserts the `:1874` extraction still yields the unit id; RED under the "before `next`" layout, green
under the sketch's. For the audit: a §4 claim about field order in a `printf` cites the line and its
operand order, a documented check the lens runs with one `sed -n`.

### H3 — high — TOOL-9 §6 AC3 one-line arm, §6 preamble, §7 'New arm', §2 S4 — raw 3

**The defect.** §6's preamble and §7 say every arm is observed red against "a driver copy with the
field clause removed". For the one-line arm of AC3 (`run --status tRun | wc -l` prints `1`) that
break reproduces the base: unit 7 at rev-2 prints no second line (spec 9's own §3 edge says "unit 7
S4 is retired at its rev-2 and prints no line"), so a driver without the field clause prints exactly
one status line and `wc -l` is 1 on both sides. §7 asserts the observation was made; as specced it
cannot be. This is the charter §7 "gate you have only ever seen pass" class, on the arm built to
catch round 1's H1 re-entering.

**The fix.** Name a second staged break for AC3: a driver copy that prints one extra stdout line
after the status line (unit 7 S4's retired shape), and observe `wc -l` print 2 against it before
wiring. Keep the field-clause break for AC1, AC2 and the field half of AC3.

**Left-shift.** The arm itself is the gate once it has been seen red; the audit-side check is that
§7's staged break is named PER ARM where arms observe different properties, documented.

### H4 — high — TOOL-13 §6 AC2 NOTE-path arm and REFUSED half, §2 S4, §6 preamble — raw 4

**The defect.** Verified `read_bound_key` at `unattended.sh:358-368`: it reads `${!_bk_name:-}`
and interpolates `$CONF` into the NOTE. Spec 13's staged break is "a tick copy with the `. "$CONF"`
line removed", which leaves S1's `CONF="$ROOT/.unattended.conf"` assignment and the `[ -f "$CONF" ]`
refusal in place. Against that break all three of AC2's observations stay green: both `declares no`
NOTEs print once each (the keys are unset either way), the NOTE's path is the fixture's conf and
exists, and the no-conf case still refuses with exit 2. §7 claims "the two NOTEs with a non-empty
path" were observed red against that break; that observation is impossible. AC1 and AC3 do red
against it. S4 is the liveness assertion for the whole read ("a NOTE that names a file proves CONF
was set before the call"), and the defect's own signature — `Declare one in  to change it`, an empty
path — is exactly what the named break does not produce.

**The fix.** Make AC2's staged break a tick copy with the whole four-line block of §4 removed (no
`CONF=`, no source, no refusal) and observe the NOTE with the empty path and the walk proceeding on a
rootless fixture; keep the source-line-only break for AC1 and AC3, and say in §7 which break each arm
was observed red against.

**Left-shift.** As H3: per-arm staged breaks, named. The NOTE-path arm is then a real liveness
assertion on the tick, which is the property the unit exists to add.

### H5 — high — TOOL-14 §2 S2, §6 AC2, §5 risks row — raw 5

**The defect.** S2 ("the adopter suite's own arms keep their assertions… Observed by AC2") and §5's
risks row ("AC2 runs the suite's arms as commands over a seeded fixture and reads no change") both
point at AC2, but AC2 as written runs `bash adopt-unattended.sh --check` once per fixture and a
`grep -c 'git commit'`; it exercises none of the suite's arms — the fragment-gone, hook-moved and
misfiled arms that act on the working tree, which are the ones a commit could change. Verified:
`tools/unattended/adopt-unattended.test.sh` has no row in `tools/gate-legs.json` (the only
`adopt-unattended` row is the adopter script at line 833); it lives under `GATE_SELFTESTS`, which no
boundary sets and which `--close` does not invoke. The one function this unit edits is the seed
every arm of that suite runs over, and nothing in the pass or in the close's bar executes those arms.
§5 states a mitigation §6 does not contain.

**The fix.** Add an AC that runs `bash tools/unattended/adopt-unattended.test.sh` at the tip,
redirected to a file, and asserts zero `FAIL` lines and the same pass count as at base (never through
`tail`, per this tree's own gotcha), or route it through `run-unattended-gates.sh`; correct the §5
risks sentence to name that AC.

**Left-shift.** A build's Gates section (§7) lists every suite whose fixture code the unit edits and
whether the bar runs it; where the bar does not, the pass runs it and the AC reads the file. Documented
check for the audit lens; for the kit, a row in `selftest-budgets.txt` already exists and the close
can be told to run it for KIT work, which the charter's DoD says is owed.

### H6 — high — TOOL-11 §3 'No driver change', §4 'The check', against TOOL-2 §6 AC7 — raw 36

**The defect.** Spec 11 §3 says "At this order the count is 1 by unit 2's AC7". Spec 2 AC7
(`2026-09-16-spec-TOOL-aWokenSentinel-2.md:452-457`) pins `grep -c 'resolve_sidecar_dir'` ≥ 2 with
a prose red-when "the root is spelled inline"; it never counts the `rev-parse --git-dir` literal. The
only exactly-one statement in spec 2 is a `hands-off` prose bullet (`:114-116`), not a criterion. §4
of spec 11 deliberately counts comment lines, in a driver whose idiom is a prose header beside every
function (the `--git-common-dir` comment at `unattended.sh:2489` is the shape), and spec 2 §4 item 9
itself spells `$(GIT rev-parse --git-dir)/unattended` in design prose a builder would carry into that
header. The base count is 0; a header mention makes the unmodified driver read 2 at order 3, AC1's
"unmodified driver fails" arm fires, and "No driver change" leaves unit 11 unable to fix it. The
premise the whole check rests on is asserted by nobody.

**The fix.** Either fold spec 2 AC7 to pin `grep -c 'rev-parse --git-dir'` at exactly 1
comments-included (and say so in spec 11 §3 as the criterion relied on), or have the check count only
non-comment occurrences (`grep -cE '^[^#]*rev-parse --git-dir'`) and move the "commented-out second
spelling" concern into the header's does-NOT-check list. Either way, note that `grep -c` counts lines,
not occurrences.

**Left-shift.** The check IS the gate once its predicate matches the population it means to bind;
the audit-side check is that a "by sibling's ACn" claim quotes the sibling criterion's predicate,
documented. Run the candidate predicate over the real tree before wiring, per §7, and print the
comment hits as near-misses.

### M1 — medium — TOOL-8 §6 AC4, §2 S4, §4 'The block reason' — raw 6

**The defect.** AC4 asserts `grep -c 'landing-unstamped' stop-guard.js` ≥ 3 and enumerates "the
REASONS entry, the `checkStop` branch and the header sentence". §4 states a third code carrier the
enumeration omits: "renderBlock selects by reason class", and the inventory adds the class on the
sidecar line. REASONS, `checkStop` and `renderBlock` reach 3 with no header paragraph, so the
red-when "the header does not name the row" is not observable, and AC4 is the only observation S4
names. S4 is the one prose carrier this unit keeps (the header states the row and the wedge B1 names),
and its criterion is satisfied by code alone.

**The fix.** Grep a phrase only the header carries, over the leading comment block cut with `awk`
before the first non-comment line (≥ 1 at tip, 0 at base), or pin the expected count at 4 with the
header named as the fourth.

**Left-shift.** A `grep -c` criterion whose threshold equals the number of code carriers cannot
observe a prose one; the audit lens enumerates the carriers a literal has at tip and compares to the
threshold, documented.

### M2 — medium — TOOL-13 §3 Edges `hands-off` unit 6, against TOOL-5 §4 Data model and TOOL-6 §2 S5, §3 — raw 22

**The defect.** Unit 13 hands unit 6 "the one sentence in the conf comments for the two keys saying
they are read from the ROOT conf by the tick". Spec 5 §4 already writes that sentence ("each comment
line says the tick reads the root's copy"); spec 6 S5 adds a rationale only where a key's own unit
left none and "expects to find none absent"; spec 6 §3 declares no `consumes-from
TOOL-aWokenSentinel-13`. Two specs name a different writer for one sentence, and the unreciprocated
edge is the class hygiene check 12's join reds. The skeptic observed it directly: a full
`check-memory-hygiene.sh` run over this worktree printed `check 12 FAILED` naming spec 13's
`hands-off TOOL-aWokenSentinel-6` with no `consumes-from` back. The same run listed further
unreciprocated edges on specs 4, 5, 6, 9 and 12; those on 9 and 12 are M5 and M6, the rest are
outside this set's scope and are reported here as seen.

**The fix.** Drop the bullet and state in a non-goal that the conf comment sentence is spec 5's (§4
Data model) and unit 6 finds it present; or, if unit 6 is meant to own it, add the reciprocal to spec
6 §3 and remove the sentence from spec 5's Data model. One writer, said which.

**Left-shift.** Check 12 already gates the edge join on the full run; what is missing is that the
`--staged` run at commit does not reach it, so the fold lands at the close. A build that edits §3
edges runs the full hygiene leg once before ratifying, documented.

### M3 — medium — TOOL-13 §6 AC4, §2 S2, §3 non-goal on a differing worktree value — raw 18, 23

**The defect.** Two halves. (a) S2's hazard is "a worktree's declaration overwriting the root's
bounds mid-walk", but AC4's fixture pins the worktree conf to hold NO `RESUME_ATTEMPTS` (`grep -c`
0), and sourcing a file that never assigns the key leaves the variable at 2 — `read_bound_key` at
`:358` assigns the default only when `${!name}` is empty — so a tick that wrongly sources every
worktree conf into its own shell still caps at 2 on this fixture. AC4's red-when ("absence of the
key resets the cap to the default") names a mechanism bash cannot produce. (b) "still caps it at 2"
names no observable: no attempt lines are seeded for the `mem2` record and no `ATTEMPTS EXHAUSTED`
read is asserted, so a cap of 2 and the default of 6 both launch attempt 1 identically. AC4 is the
sole observation of S2, and the non-goal "a worktree conf that declares a different value is not
read" has no observer.

**The fix.** Have the worktree conf declare a DIFFERENT value (`RESUME_ATTEMPTS="6"`) beside
`MEMORY_ROOT=mem2`; seed two post-move attempt lines for the `mem2` record; assert `ATTEMPTS
EXHAUSTED` with no launcher written for it, and against the staged break (the worktree conf sourced
into the tick's shell) assert attempt 3 launches. Rewrite the red-when as "the worktree's declaration
is read, which is the second conf sourced into the tick's shell".

**Left-shift.** The arm as fixed is the gate. For the audit: an AC that says "still X" names the
observation that distinguishes X from its default, documented.

### M4 — medium — TOOL-12 §6 AC2, §4 Files touched, §5, against TOOL-5 §4 — raw 24

**The defect.** AC2 requires `grep -c 'logged-out node kills nothing'` over the header of
`resume-tick.sh` to print 1. §4 Files touched says the tick is edited "if unit 5's pass did not
already build spec 5's rev-2 order; otherwise none"; §5 says "user docs — none; the tick's own header
states the order". Spec 5 rev-2, grepped whole, commits that sentence only to its own §4 and §5
prose and never to the tick's header. On the expected path (unit 5 builds the order) the sentence AC2
grades has no writer in either spec: it reds at the pass or is added off-spec. Spec 13 shows the
right shape: its Files touched row lists "the header sentence on root scope" unconditionally.

**The fix.** Make the header sentence an unconditional unit 12 edit in Files touched, or fold it into
spec 5's tick header and have AC2 read it as unit 5's; say which.

**Left-shift.** A criterion that greps a file lists that file in Files touched as this unit's edit or
names the sibling that writes it; documented, the lens joins §6 greps against §4 rows.

### M5 — medium — TOOL-12 §3 Edges `consumes-from` unit 2, against TOOL-2 §3 — raw 25

**The defect.** Unit 12 declares `consumes-from TOOL-aWokenSentinel-2` (`pid-alive: yes`); spec 2 §3
hands off to 3, 4, 5, 6, 7, 11 and external, never 12. Both specs are Tier-2 and dated after
`SPEC_EDGES_CUTOFF`, so both are in check 12's population; the skeptic's full hygiene run printed the
line for spec 12. The same shape spec 8 folded at rev-2 for its own unit-2 bullet.

**The fix.** Fold the `pid-alive` dependency into the unit-5 bullet ("through unit 5's own edge on
unit 2"), exactly as spec 8 rev-2 did, since this writer does not hold spec 2.

**Left-shift.** As M2: one full hygiene run before ratifying a §3 edit.

### M6 — medium — TOOL-9 §3 Edges `consumes-from` units 5 and 3, against TOOL-5 §3 and TOOL-3 §3 — raw 26

**The defect.** Spec 9 declares `consumes-from` 5 and 3. Spec 5 §3 hands off to 6, 7, 12, 13 and
external only; unit 9 appears solely inside the prose of the hands-off-7 bullet, and the join keys on
the backticked target after the verb, not on prose. Spec 3 §3 names unit 9 nowhere. The skeptic's full
run reds check 12 with two lines for spec 9.

**The fix.** Add `hands-off TOOL-aWokenSentinel-9` to spec 5 §3 (it already names the field), and
route the sidecar-line dependency through the unit-7 bullet (unit 7 consumes from 3) or add the
reciprocal in spec 3.

**Left-shift.** As M2.

### M7 — medium — TOOL-13 §4 'The read, in the tick' snippet, §10 — raw 39

**The defect.** `read_bound_key` reads `_bk_val="${!_bk_name:-}"` from the calling shell, which
includes the process environment. The driver defends that with `GATE_BOUND=""; UNIT_STALL_BOUND="";
REVIEW_ROUNDS=""` at `unattended.sh:339` BEFORE `. "$CONF"` at `:341` (re-read here). Spec 13 §10
cites exactly those lines and then says "the tick copies the sourcing and the calls and nothing
else"; the §4 snippet has no `RESUME_ATTEMPTS=""; RESUME_TURNS=""` line. So the §4 claim that the
keys "resolve exactly as `GATE_BOUND` does in the driver" is untrue: an exported value overrides the
kit default with no NOTE when the conf is silent, and a junk exported value exits every tick at 2
blaming the conf.

**The fix.** Add `RESUME_ATTEMPTS=""; RESUME_TURNS=""` before `. "$CONF"` in §4, and one arm that
exports `RESUME_ATTEMPTS=abc` into the tick's environment and asserts the conf's value (or the default
with its NOTE) wins.

**Left-shift.** That arm is the gate. For the kit, the cleaner home is inside `read_bound_key`
itself (clear before read, or take the value from a sourced-conf namespace), which would bind every
caller at once and is a unit 5 or unit 13 decision to record either way.

### M8 — medium — TOOL-12 §2 S4, §4 'The class, in `memory/gotchas/`', Files touched; TOOL-14 same three — raw 41, 42

**The defect.** `tools/memory-tree/gotchas.py --check`, run by the memory hygiene leg
(`check-memory-hygiene.sh:1880`), enforces check 17 (`memory/gotchas/INDEX.md` must equal the render,
regenerated by `--write`, `:263-270`) and check 18 (every `kind: class` body must match `gated by|gated
in|gated at|documented[ -]check|no machine gate`, `:58` and `:277-279`). Both specs describe the body
as class, instance and one-sentence remedy with no gate declaration; neither names `INDEX.md` nor any
declaring phrase (grep rc 1 on each); both Files touched tables omit `INDEX.md`. AC4 in each binds
front-matter parsing and `--for-diff` selection, which reach neither check. The pass runs no gates,
so memory hygiene — a gate §7 lists — reds at the close on both counts for records built as specced.

**The fix.** In each spec: add `memory/gotchas/INDEX.md` (regenerated by `gotchas.py --write`) to
Files touched; state in §4 that the body names its gate (`gated by` the named suite arm) or says `no
machine gate`; add `python tools/memory-tree/gotchas.py --check` exit 0 to AC4.

**Left-shift.** Checks 17 and 18 already gate it; the audit-side check is that a spec adding a
`memory/gotchas/` record cites `gotchas.py --check` in its ACs, documented. The `TEMPLATE-SPEC.md`
check 12 pointer could carry that line once, which is the cheaper home.

### M9 — medium — TOOL-11 §3 'No scan of resume-tick.sh or the hooks', §2 S2, §10, against TOOL-5 §4 — raw 50

**The defect.** `tools/unattended/lib-unattended.sh`'s header (the lib header's pointer, dUnstalledConvoy seq 22) ratifies
that a rule the driver and a sibling script must answer identically lives in that sourced file: "two
spellings of one rule is two-answers-to-one-question, and the fix is one spelling, which is this
file". Spec 5 §4 already has the tick source the lib and hoists `read_bound_key` into it for exactly
this reason, and in the same section has the tick spell `git rev-parse --git-dir` inline for the
sidecar root spec 2's `resolve_sidecar_dir` derives in the driver. Spec 11's non-goal exempts the
tick because a kit file "cannot source the driver's function without spawning it" — true of the
driver, irrelevant to the lib the tick already sources; the ratified mechanism is neither cited nor
rejected. S2 does disclose the exemption in the check's header, which meets §7's rule; but the check
then certifies one derivation while the same build writes a second bash spelling of the same root one
file over, the class the check exists to bind, declared out of population on a reason the kit answers.

**The fix.** Cite `lib-unattended.sh` and -22 in §3 and §10. Either define `resolve_sidecar_dir` in
the lib (a spec 2 hands-off; the tick reads through it) and have the check count the literal across
driver, lib and tick as exactly one, in the lib; or state in §3 why the tick keeps its own spelling
despite the ratified seam.

**Left-shift.** If the lib route is taken, the check's population widens to the three files and the
gate binds the class. Otherwise a documented check: a non-goal that exempts a sibling from a
one-spelling gate cites the seam record that decides where the spelling lives.

### M10 — medium — TOOL-14 §4 'The commit', §10 reuse audit — raw 53

**The defect.** The same kit already holds a `seed()` that commits:
`tools/unattended/check-playbook.test.sh:33-53` (`git add -A >/dev/null && git commit -qm seed`)
under `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null`, citing
`memory/gotchas/fixture-inherits-ambient-machine-state.md`; `check-unattended.test.sh:446` and nine
sibling lines commit with `-c commit.gpgsign=false --no-verify`. Spec 14 §4 proposes `git commit -q
-m seed --no-verify` alone and §10 names neither idiom. The stated reason for `--no-verify` — the real
tree's `core.hooksPath` is repo-global and "could otherwise reach a fixture created inside a
checkout" — misreads config resolution: a nested `git init` is its own repo and does not consult the
parent's `.git/config`; what reaches the fixture is GLOBAL config, and `--no-verify` covers global
hooks but not global `commit.gpgsign=true`, on which the new commit fails and reds the borrowing arms
of units 3 and 4 while naming the hooks. A third seed idiom in one kit dir, where §12 says extract at
the second.

**The fix.** Cite `check-playbook.test.sh`'s `seed()` and the gotcha in §10; take its shape in §4
(null global/system config for the seed, or `-c commit.gpgsign=false`) and state the ambient keys the
fixture declares; make the commit's failure the seed's own refusal rather than a silent subshell exit.

**Left-shift.** One arm in the adopter suite that runs `seed()` under `GIT_CONFIG_GLOBAL` pointing
at a file declaring `commit.gpgsign=true` and asserts a born HEAD; RED against the `--no-verify`-only
shape. For the kit: the gotcha exists; the reuse audit's documented check is `grep -n 'git commit'
tools/unattended/*.test.sh` before proposing a fourth spelling.

### L1 — low — TOOL-8 §4 Files touched, against TOOL-3 §6 AC3, §7 — raw 27

**The defect.** Files touched lists "the `FINISHED-UNSTAMPED` arm rewritten from allow to block".
Spec 3 AC3 says that verdict "is not observed here" and that unit 8 owns it and its arm; spec 3 §7
arms one arm per §6 payload with no such payload. At order 6 there is no allow arm to rewrite; spec
8's own S5 and §7 describe a NEW arm. The row lists three arms while §7 lists four payloads, omitting
the background-tasks arm S1 and AC3 grade.

**The fix.** Reword the row to "new arms: the `FINISHED-UNSTAMPED` block, the cap, the background-tasks
and the unbound payloads", matching §7's New arm line.

**Left-shift.** None gateable; the lens reads Files touched against §7's arm list, documented.

### L2 — low — TOOL-3 §6 AC2 (line 405 against 408), TOOL-10 §2 S1 — raw 30

**The defect.** Spec 10 S1 declares the value 6 "as spec 3 pins it at rev-2". Re-read: spec 3 rev-2
AC2 at line 405 still requires a reason "naming the slug, `block 1/12` and `--plan`" and at line 408
says the reason reads `block 1/6`. At rev-1 (blob at `12b3701d`) only `block 1/12` existed; the fold
appended the 6 clause without removing the 12. One reason string cannot carry both, and an arm taken
from the first clause reds against `BLOCKS_DEFAULT=6`, AC6's `1/6` and every carrier unit 10 declares
at 6. Unit 10 is right; the residue is in spec 3.

**The fix.** Fold spec 3 AC2's `block 1/12` to `block 1/6` and note it in spec 3 §9; unit 10 needs
no change.

**Left-shift.** A fold that changes a literal greps the whole spec for the old literal before
closing, documented. Cheap enough to make a habit: `grep -n '1/12'` over the build folder is one line.

### L3 — low — TOOL-11 §7 'New arm' — raw 38

**The defect.** "no floor exists in this suite" is false: `tools/unattended/check-unattended.test.sh`
declares `FLOOR_ASSERTIONS=410` at `:3252` and is sharded with `FLOOR_SHARD_1=91` and
`FLOOR_SHARD_2=319` at `:3277-3278`, selected by `SH_I` (re-read here). The floor is shrink-only, so
the omission does not red by itself, but the new arm's assertions are never re-pinned and the
sibling specs 9, 12 and 13 carry the re-pin note this one omits. Code outside both shard regions
runs in every invocation, so the "runs in neither shard" half of the raw finding overstates; the
false statement stands.

**The fix.** Replace the clause with the siblings' shape: name which shard the arm joins and that
`FLOOR_ASSERTIONS` and that shard's floor rise by its executed count.

**Left-shift.** The floor is the gate for a lost arm; the re-pin is the documented check, and the
build's own siblings already carry it.

### L4 — low — TOOL-8 §2 S6, §4 'Why a BLOCK is the right answer for a bound session', §6 AC5 — raw 45

**The defect.** S6 relies on "the six pre-unit-1 records at LANDING in this tree" and AC5's red-when
on "six such records". Counted at `12b3701d` and at HEAD: phase `LANDING` = 4 (aCollapsedScan,
dRatifiedSeam, dRetiredFork, dSealedTally), `BUILDING` = 2, `RUNNING` = 1 (this build), and zero
`RUN.md` files carry a `session:` line. §4's "six non-terminal records" is the only correct spelling
and only if BUILDING runs count as finished-without-a-stamp, which they are not. A typed count of a
derived population, wrong at the base the spec pins — the class the charter's §7 forbids outright. The
mechanism (an absent `session:` fact binds nothing) is correct.

**The fix.** Drop the number and state the property: every non-terminal record at base carries no
`session:` fact, so the hook's `resolveLease` binds none of them; have AC5 derive the population by
grep at observation.

**Left-shift.** AC5 as fixed derives the count; for the audit lens, any integer in prose beside a
derivable population is a hit, and the lexicon of the charter already says so — documented, run by
`grep -nE '\b(six|four|[0-9]+) (such )?records\b'` over the spec.

## The cross-read on the four axes

Where two specs disagree, both are named, because a fix to one that leaves the other is a fold.

- **Interface.** TOOL-9 §4's field order versus `unattended.sh:2975` and its own AC1 (H2). TOOL-11
  §3's "count is 1 by unit 2's AC7" versus what spec 2 AC7 actually pins (H6). TOOL-13 §4's "resolves
  exactly as `GATE_BOUND` does" versus the driver's clear-before-source at `:339` (M7). TOOL-14 §4's
  `--no-verify`-only commit versus the kit's two existing seed idioms (M10).
- **Ordering.** TOOL-8 at order 6 rewrites an arm spec 3 at order 2 never built (L1). TOOL-11 at
  order 3 pins a count spec 2 at order 1 does not, and a header comment moves it (H6). TOOL-12's AC2
  greps a header sentence whose writer depends on whether unit 5 at order 5 built the rev-2 order
  (M4). TOOL-8's loop trace assumes `--landed` succeeds after the lander, which on a `--no-ff`
  landing it does not (H1).
- **Scope.** TOOL-13 hands unit 6 a sentence spec 5 writes (M2). TOOL-11 exempts the tick's spelling
  from the one-spelling check while spec 5 writes it (M9). TOOL-12 and TOOL-14 scope a gotcha record
  without the index and the declaration its gate requires (M8). Three `consumes-from` edges name
  siblings that declare nothing back (M5, M6) — the same shape specs 8 and 14 folded at rev-2, which
  is B1 and B2's uncommitted diff.
- **Acceptance.** Criteria that cannot red against their named break: TOOL-9 AC3's one-line arm
  (H3), TOOL-13 AC2's liveness half (H4). Criteria satisfied by the wrong carrier: TOOL-8 AC4 (M1).
  Criteria whose fixture cannot show the defect: TOOL-13 AC4 (M3). Criteria with no writer: TOOL-12
  AC2 (M4). Properties observed by nothing: TOOL-14 S2 (H5). Criteria contradicting themselves:
  TOOL-3 AC2 (L2).

**Prior art the specs re-invent or misread.** `TOOL-dUnstalledConvoy-38` and `TOOL-aUnblockedFleet-7`,
both OPEN against the verb spec 8's loop re-runs (H1). The `printf` operand order at `:2975` (H2).
The driver's own clear-before-source guard, cited and then dropped (M7). `lib-unattended.sh` and
the lib header's pointer (dUnstalledConvoy seq 22), the ratified seam for a shared spelling (M9). `check-playbook.test.sh`'s
`seed()` and the ambient-state gotcha (M10). `gotchas.py` checks 17 and 18 (M8). The suite's
`FLOOR_ASSERTIONS` and shards (L3).

**Harness and driver assumptions, and which were verified.** That check 34 refuses `--landed` in
the run worktree after a `--no-ff` landing rests on the backlog rows' text and on
`unattended.sh:2476-2503` and `push-main.sh:118`, read here, not driven (H1). The `printf` at
`:2975` was re-read (H2). `read_bound_key` at `:358-368` and the guard at `:339-341` were re-read
(H4, M7). The `gate-legs.json` absence of the adopter suite was re-grepped (H5). Spec 2 AC7's
predicate was taken from the skeptic's line cite and not re-opened here (H6). The full hygiene run
that reds check 12 on specs 9, 12 and 13 is the skeptic's observation, reported as such (M2, M5, M6).

## What this pass did NOT do, said rather than implied

- **It read documents and the source they cite; it drove no fixture.** The synthesis re-read at the
  working tree: `tools/unattended/unattended.sh:334-342,356-369,2973-2977`;
  `tools/unattended/check-unattended.test.sh:3252,3277-3278`; `tools/gate-legs.json` for
  `adopt-unattended`; `memory/backlog/TOOL.md` rows -38 and -7; spec 3 lines 405-408; the two
  uncommitted diffs; and the blob pairs for all seven subjects. Reproductions that are the skeptic's
  and are reported as such: the full `check-memory-hygiene.sh` run (M2, M5, M6), `gotchas.py`'s
  check bodies at `:58,:263-279` (M8), `check-playbook.test.sh:33-53` (M10), the run-record phase
  count (L4), and spec 2's AC7 and hands-off lines (H6).
- **A spec audit grades what a document says.** H1 was found by reading two OPEN backlog rows
  against a loop trace; whether the recorded workaround still works after units 2 and 7 land is a
  question for the build, not this pass.
- **The units' §8 alternatives were read for what they resolve, not re-adjudicated.**
- **The 22 refuted findings were not re-opened.** The skeptic's verdicts stand; none was
  contradictory and none was spurious by the pipeline's own count.
- **Precision was 0.58.** Above the floor and reported. Round 2 should re-audit the revised set at
  its new blobs after B1 and B2 are committed, with the blob-pin check moved into the commission's
  pre-flight, one lens on H1's resolution across specs 7 and 8 together with the two backlog rows,
  and one on the cannot-red class (H3, H4, M1, M3), since four of the twenty-two defects here are
  arms that can only be seen passing and three more are edges the full hygiene run already reds.
