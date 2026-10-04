**Serves:** diff-review DEPL-aHalvedInstall-1 DEPL-aHalvedInstall-2 DEPL-aHalvedInstall-3 DEPL-aHalvedInstall-4

# Tier-2 closing diff review — aHalvedInstall, ROUND 1

*The build's closing Tier-2 review over all four units: govkit reads each kit's required conf keys
(unit 1), selfcheck 6b refuses a hole probe that passes on an empty tree (unit 2), playbook-render
declares `[[regenerate]]` and selfcheck 3b-iii refuses an adopter with neither a regenerate nor a
reason (unit 3), and `update` holds back a kit whose row was refused (unit 4). Node `a`, 2026-10-02.
Five lenses (security, correctness, seams, verification, intent) ran over a 27-item checklist and
six spec documents. Every finding was then put to a skeptic prompted to REFUTE it, and one synthesis
pass followed.*

**Reviewed range:** cd90f7fa5c8cddf152e3a2a065f5df7ad64f355b...5362917a64a60d6eda0bcaa7b2356ad574002e35
— ROUND 1.

## Verdict: BLOCKED

There are no blockers. Two HIGH findings (ids 1 and 4, merged into item H1) show that unit 4 has not
closed the half-install class it claims to close. Refusals from the unclaimed-source landing loop and
from the classification walk never reach the held set. The relayed owner mandate asks for this class
closed "in any flexible form", so the build does not land until H1 is fixed. Nine MEDIUM items and one
LOW item are also owed. None is dangerous alone, but four of them are coverage holes on the exact
classes this build closes.

## Review shape

- Intensity full. Raw 17, confirmed 13, refuted 4, unverified 0 (0 uncertain). Precision 0.76.
- Adjudicated tally by item: 0 BLOCKER, 1 HIGH, 9 MEDIUM, 1 LOW (11 items).
- Adjudicated tally by raw confirmed finding: 0 BLOCKER, 2 HIGH, 10 MEDIUM, 1 LOW (13 findings).
- Merges: ids 1 and 4 (one defect, two refusal channels), and ids 2 and 7 (one descriptor defect seen
  from both sides).

## Run integrity

- Lenses: 5/5 returned, 0 DIED.
- Skeptic batches: 5/5 returned, 0 DIED.
- Verdict hygiene: 0 contradictory verdicts demoted to unverified, 0 spurious verdicts discarded,
  0 duplicates.
- Fixes on confirmed findings: 9 judged sound, 4 judged UNSOUND, 0 none proposed, 0 NOT JUDGED.
- Severity on confirmed findings: 0 UNGRADED by the skeptic, 0 RE-GRADED by the skeptic.
- Unverified findings: 0 answered UNCERTAIN, 0 with no usable verdict.
- Lens notes: none were supplied, so every lens ran on the kit's generic brief.
- Intent: 6 spec documents were supplied as `specs`, beside the range's commit messages.
- Checklist: 27 items, each assigned to exactly one of 5 lenses (security 6, correctness 6, seams 5,
  verification 5, intent 5).

Every integrity count is zero, so this run is complete. The security lens returned no confirmed
finding. Because no lens died, that zero is a real result for this lens and checklist, not proof that
no security defect exists.

## Blockers

None.

## HIGH

### H1 — the held set misses two refusal channels, so the half-install class stays open (ids 1, 4)

- **Where:** `tools/govkit/govkit.py:9637` (the held set is final at 9637-9641), `tools/govkit/govkit.py:9284`
  (the held set is filled only in the write loop). The missed channels are the landing loop's `_refused_new`
  at 9840 (the target already holds the path), 9863 (write OSError) and 9912 (git-add refusal), and the
  classification walk's `r.fail` + `continue` arms at 8490 (unknown role), 8532 (schema-1 role mismatch)
  and 8625 (refuse disposition).
- **Defect:** `_held` is filled only by the `for a in acted` write loop and its trailing compare. The
  landing loop for unclaimed sources runs after the held set is final and printed. The classification
  walk's refusals happen before a row ever enters `acted`. Neither channel holds the kit back.
- **Failure:** take a kit whose new vintage adds a sibling script, and suppose the target already holds
  that path outside the receipt. The kit's other rows land at the new vintage and its `[[regenerate]]`
  runs over the mixture. Verify does not roll it back: `[check] none` reads as UNVERIFIED, and a green
  check stays green. Landing-loop refusals never call `r.fail`, so with no other finding the receipt
  re-stamps at the new vintage. The only signal is a `REFUSED <dest>` line near the end of the output.
  For the classification channel, `r.fail` withholds the re-stamp, but nothing rolls back the kit's
  other writes under `[check] none`.
- **Fix:** the skeptic judged both finders' fixes UNSOUND. The corrected fix, merged from both
  verdicts, has four parts:
  1. Carry the kit on each `_refused_new` entry as `(dest, why, eid)`. After the landing loop and
     before the re-render step, add the kit to `_held` only when both of these hold:
     - the refused destination's source did not exist at that kit's recorded receipt commit
       (`blob_at(root, <kit row commit>, src) is None`);
     - no `[[decline]]` covers `(kit, dest)`.
  2. For the classification walk's `r.fail` + `continue` arms, add
     `_held.setdefault(str(row.get('kit') or ''), []).append(row['path'])` when the kit is non-empty.
  3. Move the HELD BACK print to after the landing loop, so a landing-held kit is announced.
  4. Add an aHI-4 arm in which a new engine file, whose path the target already occupies, holds back a
     changed sibling row. Add a second arm in which a declined, occupied gap does NOT hold its kit.

  The rejected form, which holds the kit on every `_refused_new` entry, must not be written. Standing
  refusals recur on every run whatever the vintage. Examples are an adopter-occupied path that the
  landing loop does not filter by `[[decline]]`, and an unresolved optional token. Holding on those
  would wedge the kit's updates permanently.
- **Left-shift gate:** a govkit selfcheck arm that lists every refusal site in `_cmd_update`, meaning
  every `r.fail` and every `_refused_new.append`. It requires each site either to reach `_held` or to
  carry a named exemption marker that states why the refusal is standing. A new refusal channel added
  without that decision then reds.

## MEDIUM

### M1 — drift-audit marks MEMORY_ROOT required even though its code defaults it, so check reds falsely (ids 2, 7)

- **Where:** `tools/drift-audit/kit.toml:60`, read by `read_conf_key_gaps` at `tools/govkit/govkit.py:4377`.
- **Defect:** drift-audit declares `required_keys_render = ["MEMORY_ROOT"]` with no `[config].defaults`.
  Its adopter defaults the key (`adopt-drift-audit.sh:64`, `${MEMORY_ROOT:-memory}`), and so does
  `drift_report.py:2400`. The conf's owner, memory-tree, also defaults it. Until this diff, nothing read
  the list as an enforced set. `read_conf_key_gaps` now enforces it.
- **Failure:** a `.memory-tree.conf` that omits MEMORY_ROOT is legal, yet `govkit check` reds with
  `required key MEMORY_ROOT is ABSENT — its adopter refuses or its gate reds`, and `update` prints a
  spurious CONF GAP. memory-tree stays green on the same file.
- **Fix:** id 2's finder fix was judged UNSOUND and id 7's was judged sound. Both corrected fixes agree:
  - Add `defaults = { MEMORY_ROOT = "memory" }` to drift-audit's `[config]`, or move the key to
    `optional_keys`.
  - Bump drift-audit's version in every carrier.
  - Do NOT make `read_conf_key_gaps` subtract the conf owner's defaults. memory-recall shares the same
    owner, and that change would silence memory-recall's true positive, since `recall_conf.py` really
    refuses an absent MEMORY_ROOT.
- **Left-shift gate:** a selfcheck arm that reads each adopter for `${KEY:-default}` reads of its
  declared `required_keys_*`. A key that the adopter itself defaults, and that the descriptor neither
  defaults nor marks as refused-without, reds. That keeps the declaration and the adopter as one answer.

### M2 — an empty value (`KEY=""`) counts as satisfied (id 3)

- **Where:** `tools/govkit/govkit.py:4393` (`read_conf_key_gaps`).
- **Defect:** an empty value is neither absent nor a `<...>` placeholder after quote stripping, so it
  produces no gap. Several readers disagree:
  - The kit's own gate fails it as undeclared (`check-unattended.sh:446-448`).
  - memory-tree's adopter refuses an empty READINESS_ROWS.
  - This diff's own unit-2 probe requires "neither empty nor angle-bracketed".
- **Failure:** `LANDER=""` or `KEEPALIVE_CREATE=""` is silent in both `check` and `update`. It reds only
  at the kit gate or the adopter, which is the silence unit 1 set out to end.
- **Fix (judged SOUND by the skeptic):** in `read_conf_key_gaps`, give an assigned value that is empty
  or whitespace-only after quote stripping its own state, such as `empty`. Word it in check's message as
  equivalent to ABSENT. Add a `DEMO_KEY=""` case to the aHI-1 AC1-AC2 loop.
- **Left-shift gate:** the `DEMO_KEY=""` arm above. Also add a parity arm that feeds one fixture conf
  to `read_conf_key_gaps` and to the unattended kit's gate key loop, and asserts both give the same
  verdict for absent, empty and placeholder.

### M3 — fragment wiring runs over a held kit and cannot be fully rolled back (id 5)

- **Where:** `tools/govkit/govkit.py:10161`.
- **Defect:** `_fr_skip` excludes inert kits and kits this run did not touch, but not held kits. So
  `run_fragment_merges` wires a held kit's half-landed fragments. A stale command it rewrote in place is
  not recorded in `_wired_new`, so `remove_wired_fragments` cannot take it back.
- **Failure:** take a held hooks kit whose fragment command changed. The rollback restores the old
  fragment and script, and `.claude/settings.json` keeps the new command. The run's "none of this
  kit's writes will stand" line is then false.
- **Fix (judged SOUND by the skeptic):**
  - Change the line to `_fr_skip = read_inert_kits(deploy) | set(_held) | {...}`.
  - For each skipped fragment, print the existing `landed UNWIRED` line with a held reason.
  - Add an arm in which a held hooks-kit fixture with a changed fragment leaves `settings.json`
    byte-identical.
- **Left-shift gate:** that arm. More generally, a selftest that runs every target-side step of
  `update` (regenerate, fragment merge, anything added later) under a held fixture and asserts that
  each step is a no-op for the held kit.

### M4 — the narrowed keepalive probe reads the conf differently from the adopter (id 6)

- **Where:** `tools/unattended/kit.toml:333` (hole `keepalive-tool-names`).
- **Defect:** the probe greps the first line-anchored `^KEY=` match. The adopter sources the conf, so
  the last assignment wins and `export`, single quotes and trailing comments are all accepted.
- **Failure:** the skeptic measured an rc of 1 from the probe on three valid spellings that the adopter
  accepts: `RESUME_SCHEDULE='off'`, `RESUME_SCHEDULE=off  # opt out`, and an `export` spelling of the
  carrier keys. The hole has `blocks_gate = true`, so each is a false red introduced by this diff. Two
  more cases also pass but were already passing at base, so they are out of scope for this finding:
  a duplicate `off` followed by `on` with no carrier pair, and a single-quoted `'<tool>'` placeholder.
- **Fix:** the skeptic judged the finder's fix UNSOUND. The corrected fix is the subshell form, with the
  variables reset first and a `test -f` guard:
  `test -f .unattended.conf && ( RESUME_SCHEDULE=; RESUME_SCHEDULE_CREATE=; RESUME_SCHEDULE_DELETE=; . ./.unattended.conf >/dev/null 2>&1; [ "$RESUME_SCHEDULE" = off ] || for v in "$RESUME_SCHEDULE_CREATE" "$RESUME_SCHEDULE_DELETE"; do case $v in ''|'<'*'>') exit 1;; esac; done )`.
  Pin these as fixture confs in the AC15 arm: the off/on duplicate, the single-quoted off, the
  commented off, the export spelling, the single-quoted placeholder and the absent pair.
- **Left-shift gate:** the fixture set above. Also add a rule that a hole probe reading a sourced conf
  must source it rather than grep it. Selfcheck can enforce that by refusing a discharge that greps
  `^[A-Z_]+=` in a file the kit's adopter sources.

### M5 — the two new selfcheck arms have no committed negative case (id 10)

- **Where:** `tools/govkit/govkit.py:1579` (3b-iii) and the 6b arm near 2034.
- **Defect:** 3b-iii and 6b were each observed red only by hand-staging. `selftest.py` has no arm for
  either, and both run only over the real descriptors, where they are green.
- **Failure:** an edit that makes either predicate match nothing passes every gate. Examples are
  renaming the `why_no_regenerate` key read, inverting `_rc6 == 0`, or running probes inside the gov
  checkout.
- **Fix (judged SOUND by the skeptic):** in the selftest's gcopy block (around `selftest.py:2645`), add
  three arms, each followed by a restore-to-green assertion like its siblings:
  1. Strip a descriptor's `[[regenerate]]` and assert 3b-iii names it.
  2. Set `why_no_regenerate = "   "` and assert it is named.
  3. Set a hole discharge to `["bash","-c","! grep -q x missing"]` and assert 6b names it.
- **Left-shift gate:** a meta-check that every lettered selfcheck arm id appears in at least one gcopy
  negative in `selftest.py`. A new selfcheck arm then reds until its failing case is committed, which
  is the charter's rule that a gate is not landed until its failing case has been observed.

### M6 — the held-row compare after the loop is never exercised (id 11)

- **Where:** `tools/govkit/govkit.py:9637`.
- **Defect:** in both aHI-4 fixtures, the refused row (`demo/conf.sh`) is followed by other acted rows
  of the same kit. So its refusal is always recorded at the top of the next iteration, and the compare
  after the loop never fires.
- **Failure:** deleting the compare after the loop leaves every arm green. A refusal on the last acted
  row would then go unrecorded, which reopens the half-installed kit.
- **Fix (judged SOUND by the skeptic):** add a fixture variant in which the conflicting row sorts after
  every other acted row of the kit, for example `zconf.sh`. Assert HELD BACK, the DECLINED regenerate
  and the restored clean row there too.
- **Left-shift gate:** that variant. Also run each aHI-4 fixture in both orders (refused row first and
  refused row last), so the arm covers both recording points by construction.

### M7 — nothing committed exercises playbook-render's new regenerate (id 12)

- **Where:** `tools/playbook/kit.toml:53`. The path it relies on is `render_playbook.py:394-397`
  (`build_region` replaces the region of a charter that already has one).
- **Defect:** unit 3's cure relies on the adopter's write mode re-rendering a charter that is already
  adopted. AC2 was checked by hand, and `run_selftest` has no run-twice or region-replacement arm.
  3b-iii checks only that a block is declared.
- **Failure:** if the write mode later regresses to a no-op or to an append, every adopter rolls
  playbook-render back on every renderer change again, which is observation #2, with every gate green.
- **Fix (judged SOUND by the skeptic):** add a render selftest arm that runs `main(['--target', tgt])`
  twice over an adopted fixture. Assert that a second run with an unchanged body is byte-identical, and
  that a changed body replaces the region and keeps the authored prose. Optionally, add a govkit arm in
  which an adopter-shaped `[[regenerate]]` moves the engine and the kit's check stays green.
- **Left-shift gate:** that arm. Also extend 3b-iii so that a declared `[[regenerate]]` must name a
  selftest arm that executes it twice.

### M8 — an unreadable conf raises instead of producing a finding (id 14)

- **Where:** `tools/govkit/govkit.py:4383`.
- **Defect:** `p.read_text` has no `try/except`. Spec 1 §5 promises that an unreadable conf is a finding
  naming the read error.
- **Failure:** in `update`, the read happens in the re-render step after rows are written and staged,
  so a PermissionError aborts the run with a traceback. The verify and rollback pass never runs, which
  leaves the half-landed state unit 4 exists to prevent. In `check`, the run ends in a traceback
  instead of a named finding.
- **Fix (judged SOUND by the skeptic):** wrap the read in `try/except OSError` and return the error.
  `check` then calls `r.fail(f"kit '{eid}' conf {file}: unreadable: {e}")`, and `update` prints a CONF
  GAP line naming the error. Neither verb raises.
- **Left-shift gate:** an aHI-1 arm with an unreadable conf (a directory at the conf path works
  cross-platform). Also a selfcheck grep that refuses a bare `read_text` reachable from `_cmd_update`
  after the write loop with no enclosing `except OSError`.

### M9 — the AC15 arm still tests the old probe and never the absent pair (id 15)

- **Where:** `tools/unattended/kit.toml:333`, and its arm in `unattended.test.sh` at about lines
  9329-9345.
- **Defect:** the probe became a presence test, but AC15 still exercises only placeholder versus
  filled. Its header still describes an alternation that no longer exists. Spec 2 AC3 (absent gives 1,
  off gives 0) was verified by hand only.
- **Failure:** a regression to `test -f .unattended.conf && ! grep ...` passes both 6b (which catches
  only a missing conf file) and AC15, and that reopens observation #1.
- **Fix (judged SOUND by the skeptic):** extend AC15 with the AC3 cases:
  - the pair deleted from the fixture conf (expect 1);
  - `RESUME_SCHEDULE="off"` with neither key set (expect 0);
  - one key empty (expect 1).

  Rewrite the arm's header to describe the presence test. This shares its fixture set with M4's fix,
  so land them together.
- **Left-shift gate:** the extended arm. Also a rule that every spec acceptance criterion recorded as
  hand-observed in a ledger names its committed arm, or is listed in the ledger as an explicit
  exemption.

## LOW

### L1 — the AC5 arm asserts one of the four candidate files (id 17)

- **Where:** `tools/govkit/selftest.py:1479`.
- **Defect:** spec 4 AC5 requires the conflict order and its four candidate files. The arm checks the
  order file and `candidate` only. The sibling aRF-17 AC5 arm already asserts all four.
- **Failure:** a forced rollback that deleted `base`, `ours` or `theirs` from the outbox would leave
  AC5 green, and the operator needs those files to resolve the refused row. This affects test
  coverage only.
- **Fix (judged SOUND by the skeptic):** assert all four of `base`, `ours`, `theirs` and `candidate`
  under `update-conflict-<slug>/`.
- **Left-shift gate:** factor the four-file assertion into one selftest helper that both AC5 arms
  call, so the two arms cannot drift apart.

## Refuted (not owed)

- **id 8:** a duplicate of id 6. Its headline single-quoted-placeholder case also passed at base, so
  it is pre-existing.
- **ids 9 and 13:** by design. Spec 2 says a probe that cannot launch is counted, not refused, and the
  6b note prints all three counts.
- **id 16:** 6b's separate loop has semantics that differ from `run_hole_probes` by design. The
  missing timeout is pre-existing, and no hang was shown.

## Appendix — every finding

| id | lens | ref | severity | skepticSeverity | verdict | reason | fixVerdict |
|---|---|---|---|---|---|---|---|
| 1 | correctness | tools/govkit/govkit.py:9637 | high | high | confirmed | Read govkit.py:9284-9641. _held is filled only inside the `for a in acted` write loop and the post-loop tail check. Then it is printed and final. The unclaimed-source landing loop (9715-9926) runs after that. It records its refusals only in _refused_new: already-held 9840, write OSError 9863, git-add refusal 9912. None of those call r.fail or touch _held. The decline at 10007 and the verify-pass rollback at 10268 read only _held, so a kit whose new-vintage file is refused there still has its sibling rows land new and its regenerate run. With no other finding the receipt re-stamps, and the only signal is the REFUSED line at 10998. The channel existed unchanged at base (base 9537-9734). It is still in scope as an incomplete closure. Spec 4 section 1 claims 'a refused row holds its whole kit back'. The relayed user mandate asks for the half-install class closed 'in any flexible form', and that outranks the computed pre-existing rule. The path is narrow: the target must already hold the new path, git must ignore it, or the write must fail. So the grade is high. The proposed fix is UNSOUND. Holding on EVERY _refused_new entry wedges a kit permanently. The landing loop does not consult [[decline]], since _gap_declined is computed later at 10940 for reporting only. The 'already holds this path' and 'unresolved token(s)' refusals are standing states that recur on every run, whatever the vintage. So a kit with one declined, adopter-occupied gap would be rolled back whole on every future update. The fix also leaves the HELD BACK print at 9639, before the landing loop, so a landing-held kit would never be announced. | unsound |
| 2 | correctness | tools/govkit/govkit.py:4377 | medium | medium | confirmed | Verified that read_conf_key_gaps (govkit.py:4354-4395) subtracts only the reading kit's own [config].defaults. drift-audit (tools/drift-audit/kit.toml:57-60) declares required_keys_render = ["MEMORY_ROOT"] with no defaults. Its adopter defaults the key (adopt-drift-audit.sh:64, ${MEMORY_ROOT:-memory}), and so does drift_report.py:2400. The conf owner memory-tree also defaults it (memory-tree/kit.toml:96). So a conf omitting it is valid, yet cmd_check (4838) r.fails 'required key MEMORY_ROOT is ABSENT' for drift-audit and update prints a CONF GAP (10051). The reader is new in this diff and drift-audit's kit.toml is unchanged, so this diff introduced the false red. The effect is contained: one spurious finding. The proposed fix is UNSOUND as written. Its first option (drop the key from drift-audit) is sound. Its alternative, subtracting the conf owner's defaults, contradicts its own instruction to keep memory-recall's entry. memory-recall's owner is also memory-tree, so that would also silence memory-recall's true positive (recall_conf.py refuses an absent MEMORY_ROOT). | unsound |
| 3 | correctness | tools/govkit/govkit.py:4393 | medium | medium | confirmed | Verified at read_conf_key_gaps, govkit.py:4381-4394. After one quote layer is stripped, an empty value is stored and is neither 'absent' nor startswith('<'), so it produces no gap. The kit gate disagrees: check-unattended.sh:446-448 fails `[ -n "$v" ]` as 'undeclared'. memory-tree's adopter refuses an empty READINESS_ROWS (adopt-memory-tree.sh:91). The unit-2 probe in this same diff requires a value that is 'neither empty nor angle-bracketed'. The shipped adopters read keys as ${X:-}, which treats empty and absent alike. So KEY="" is silent in govkit check and update and reds only at the kit gate or adopter, which is the silence unit 1 set out to end. It is not covered by by-design (c), which concerns assignment syntax. The effect is contained because the kit's own gate still reds. | sound |
| 4 | seams | tools/govkit/govkit.py:9284 | high | high | confirmed | Its landing-loop half duplicates finding 1, and the verification there holds: _refused_new at 9840/9863/9912 never reaches _held, which is final at 9641. Its distinct addition is also real. The classification walk's r.fail+continue arms run before acted.append at 8818: unknown role at 8490, the schema-1 role mismatch at 8532, and the refuse disposition at 8625. Those rows never enter `acted`, so the write loop's problem-count comparison never sees them. Their kit's sibling rows land new and its regenerate runs. r.fail withholds the receipt re-stamp, but nothing rolls back the kit's other writes under [check] none. The class was pre-existing, and it is in scope as an incomplete closure for the reason given on finding 1. The path is narrow (schema-1 receipts, unknown roles), so the grade is high. The fix is UNSOUND for its landing-loop half. Appending to _held at every _refused_new.append holds a kit back on standing refusals that recur every run whatever the vintage, such as an adopter-occupied path the loop does not filter by [[decline]], or an unresolved optional token. That wedges the kit's updates permanently. The HELD BACK print at 9639 also runs before the landing loop, so such a hold would go unannounced. | unsound |
| 5 | seams | tools/govkit/govkit.py:10161 | medium | medium | confirmed | govkit.py:10161 builds _fr_skip from read_inert_kits(deploy) and the not-touched kits only. _held, which this diff introduced at 9284 and consults at 10007 to decline the regenerate, is not consulted there, so run_fragment_merges wires a held kit's landed fragments. run_fragment_merges (5211-5270) records only non-stale additions, by its own docstring. A fragment whose command it rewrote in place is therefore not in _wired_new[eid], and remove_wired_fragments at 10348 cannot take it back. The held rollback (10296) then restores the old fragment and script, leaving settings.json pointing at the new command. The diff made this reachable: before it, a refused-row kit was never rolled back, so its wiring matched the bytes that stood. The path is narrow, since it needs a held kit that ships a fragment whose command changed, and the effect is confined to settings.json. | sound |
| 6 | seams | tools/unattended/kit.toml:333 | medium | medium | confirmed | I measured the probe at kit.toml:333 in a temp dir. RESUME_SCHEDULE='off' gives rc 1, and so does RESUME_SCHEDULE=off with a trailing '# opt out' comment. A conf that uses export for both carrier keys also gives rc 1, even though the adopter's source at adopt-unattended.sh:155 reads every one of these as valid. The hole has blocks_gate = true, so each of these is a false red, and the diff introduced them. The base probe was only a refutation (`! grep '^KEY="<.*>"'`) and passed all of them. A duplicate assignment, off and then on, still passes with no pair, and so does a single-quoted '<tool>' placeholder (rc 0). Both of those also passed at base, so they are pre-existing and not in scope. The shipped example uses the double-quoted form, which the probe handles, so the false red needs a hand-edited spelling. That keeps the effect contained. | unsound |
| 7 | seams | tools/drift-audit/kit.toml:60 | medium | medium | confirmed | drift-audit/kit.toml:60 declares required_keys_render = ["MEMORY_ROOT"] with no [config].defaults. read_conf_key_gaps (govkit.py:4354, new in this diff) exempts only keys in the kit's OWN cfg.defaults (4375-4377). So a .memory-tree.conf without MEMORY_ROOT now reds drift-audit in check, while memory-tree, which declares defaults = { MEMORY_ROOT = "memory" } at kit.toml:96, stays green on the same file. drift-audit's adopter defaults the key (adopt-drift-audit.sh:64), and so does drift_report.py:2400, so the red names a refusal that does not happen. The diff introduced this false red. It needs a conf that omits a key the example ships, so the effect is contained. | sound |
| 8 | verification | tools/unattended/kit.toml:333 | high | - | refuted | This duplicates finding 6: same probe at kit.toml:333, same two-readers defect, and an equivalent fix. The in-scope parts, the false reds on 'off', on a commented off and on export, are confirmed under 6. The headline case is not new. A single-quoted '<your-tool>' placeholder that discharges the hole also passed at base, whose probe `! grep -qE '^(...)="<.*>"'` matched only double-quoted placeholders. So that part is pre-existing and does not support the high grade. | sound |
| 9 | verification | tools/govkit/govkit.py:2055 | medium | - | refuted | The behaviour is by design. Spec 2 line 29 says a probe that cannot launch is NOT a finding, and line 87 says it is counted, not refused. The arm's own header (govkit.py:2023-2025) says a probe that cannot LAUNCH is counted apart and never refused. AC2's red-when is an acceptance observation: the observer reads the note's count against the declared holes. It is not a requirement that the arm itself red. The note prints ran, exited-0 and could-not-launch counts, which satisfies the charter's 'a probe that cannot move says so'. Live selfcheck prints '20 ran, 0 exited 0, 0 could not launch'. Check 6 already refuses a hole with no discharge. The non-list-command and stdin-hang cases are speculative: no shipped probe has that shape, and grep-style probes with file arguments do not read stdin. A probe that times out did not exit 0 on the empty tree, so leaving it unrefused is consistent with the question the arm asks. | sound |
| 10 | verification | tools/govkit/govkit.py:1579 | medium | medium | confirmed | selftest.py has no arm for 3b-iii or 6b. A grep finds aHI-1 and aHI-4 arms only, nothing for aHalvedInstall-2 or -3. The gcopy block at selftest.py:2645 onward already stages selfcheck negatives such as r7d, r7e, r18 and rsd, each with a restore-to-green assertion. Both new arms run only over the real descriptors, where they are green. A predicate that later stops matching anything would therefore pass every gate. By-design item (g) covers the selftest arms observed red by hand-staging, not these selfcheck arms. | sound |
| 11 | verification | tools/govkit/govkit.py:9637 | medium | medium | confirmed | In both aHI-4 fixtures (selftest.py:1443-1484) the conflicting row is demo/conf.sh, and acted rows of the same kit follow it: eng.txt and plain.txt. The refusal is therefore always recorded at the top of the next iteration (govkit.py:9287). The after-loop compare at govkit.py:9637-9638 never fires in any asserted fixture, and no other selftest asserts HELD BACK or DECLINED. Spec 4 line 78 names 'once more after the loop' as part of the design. Deleting it would leave a refusal on the last acted row unrecorded, which reopens the half-installed kit with no arm going red. | sound |
| 12 | verification | tools/playbook/kit.toml:53 | medium | medium | confirmed | Unit 3's cure for observation 2 relies on the adopter's write mode re-rendering an already-adopted charter, via build_region's 'charter with a region -> replaced' path (render_playbook.py:394-397). Nothing committed exercises that path. run_selftest has no region-replacement or run-twice arm. Its only main() write-path arm is the template-is-its-own-charter refusal at line 864. Spec 3 rev-2 records that AC2 was observed by hand over the selftest's fixture. 3b-iii checks only that a block is declared. If the write mode regressed to append or to a no-op, every adopter would roll playbook-render back on each renderer change again, with all gates green. Graded medium rather than high because the replace path works today and the regression is prospective. | sound |
| 13 | intent | tools/govkit/govkit.py:2046 | medium | - | refuted | Spec 2 S1 says in so many words that a probe which cannot launch is NOT a finding because it did not report discharged, and section 5 repeats that it is counted, not refused. The arm header at govkit.py:2023-2027 states the same limit. AC2's 'Red when' clause is the mutation the observer must catch when reading the note count. It is not a promise of code. The note prints ran, exited-0 and could-not-launch, so an all-no-launch run announces itself, which is what the 'a skip must announce itself' rule asks for. A probe that times out also did not exit 0, so it is not the vacuous-pass class the arm exists for. Folding it into the no-launch count is a labelling imprecision with no behavioural effect. | unsound |
| 14 | intent | tools/govkit/govkit.py:4383 | medium | medium | confirmed | read_conf_key_gaps (govkit.py:4382-4383) checks p.is_file() and then calls p.read_text with no try/except. errors='replace' removes decode errors, but an OSError such as PermissionError still propagates. No other govkit path reads the conf: target_context does not. So the diff introduces this raise and does not merely extend one. In update the call sits at :10051, inside the re-render step after the write loop. cmd_update (:8008-8011) only does try/finally release_write_lock, so a traceback skips the verify and rollback pass and leaves rows written. In check it ends the run in a traceback. Spec 1 section 5 promises an unreadable conf is a finding naming the read error. The path is narrow (an unreadable conf) and git still holds the prior state, so the effect is contained. | sound |
| 15 | intent | tools/unattended/kit.toml:333 | medium | medium | confirmed | The diff turned keepalive-tool-names (kit.toml:333) into a presence test because the absent-pair case was the observed defect. The diff left unattended.test.sh unchanged, and its AC15 arm (:9329-9345) exercises only placeholder (expect 1) and filled (expect 0). It never covers the pair absent from a present conf, nor RESUME_SCHEDULE=off. The ledger records spec 2 AC3 as hand-observed. Selfcheck 6b covers only a missing conf FILE, so a regression to `test -f .unattended.conf && ! grep ...` would pass both 6b and AC15 and reopen the first observation. The header's 'alternation still names the keepalive keys alone' no longer describes the probe. The gap has no runtime effect today, but it is a real coverage hole on the exact class the build closes. | sound |
| 16 | intent | tools/govkit/govkit.py:2034 | low | - | refuted | 6b needs different semantics from run_hole_probes. It runs with no stand-down resolution, resolves a missing token to its own name instead of returning needs-answer, uses an empty temp cwd, and reads a different verdict (exit 0 is the failure). A separate loop of about 20 lines is a reasonable design and causes no defect. The cited divergence is the missing timeout, and it is pre-existing. cmd_check's probe loop at base had no timeout. Probes are grep or test commands over named files, and no reachable hang was shown, so update now running the same loop adds no demonstrated consequence. | unsound |
| 17 | intent | tools/govkit/selftest.py:1479 | low | low | confirmed | Spec 4 AC5 (spec line 126) requires 'the conflict order and its four candidate files'; the [aHI-4 AC5] arm at tools/govkit/selftest.py ~1479 checks only update-conflict-<slug>.md and candidate, and the build's acceptance ledger restates AC5 narrowed to 'its candidate file'. govkit.py:7997 writes base, ours, theirs and candidate, and the sibling [aRF-17 AC5] arm already asserts all four, so the narrowing is a real arm-vs-spec gap. Consequence is contained to test coverage: no product behaviour changes, and a forced rollback that selectively removed three of the four files is an unlikely regression. | sound |
