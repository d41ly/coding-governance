# Pre-code review — TOOL-aBatchedLintel (port the check-12/check-7 fork collapse into memory-tree)

**Reviewed:** `memory/tooling/builds/2026-08-03-TOOL-aBatchedLintel/spec/2026-08-03-spec-aBatchedLintel-1.md`
**Base:** `e8d046cc` (coding-governance, clean tree) · upstream source `C:/projects/incms/main` at `7e169b796`
**Verdict:** ready after the edits below — plus one hard precondition (next section)
**Raw findings 35 · surviving 26 · de-duplicated to 11 distinct defects · 0 dropped outright**

---

## Precondition — the spec file is not on disk

`memory/tooling/builds/2026-08-03-TOOL-aBatchedLintel/` does not exist in this repo. `git status
--porcelain` is empty (clean, no untracked files), `find` over both repos and over the session temp
tree returns nothing for `aBatchedLintel`, and `git worktree list` shows one worktree. The spec was
authored untracked and has since been removed.

Consequence for this review: I could verify every claim the findings make about **the kit source, the
upstream source, and the measurements** — that is the load-bearing half, and I re-ran all of it. I
could **not** re-read the spec to confirm the quoted sentences. I am relying on the fact that four
independent finder lenses quote the same sentences byte-identically (`"4 assertions today, covering
neither check 7 nor the spec ratchet"`, `"BOTH hand-kept literals"`, `"spec files in the check-12
population | 16"`, `"the total is below the 27.4s baseline"`). That is strong corroboration, not
proof. **Restore and commit the spec before acting on this report**, and re-check the quoted strings
against the restored text.

Nothing can be built from a spec that does not exist, so this blocks the unit regardless of the
findings below.

---

## Findings, most severe first

### F1 — HIGH · S5, AC4 and Q2 rest on a false self-test baseline

*(merges the same defect seen by four lenses)*

**Claim in the spec:** the self-test has "4 assertions today, covering neither check 7 nor the spec
ratchet"; AC4 requires the post-change count be "strictly greater than the current 4"; Q2 repeats
"this kit has 4 in total".

**Verified:** `tools/memory-tree/check-memory-hygiene.test.sh` has **14** assertions and is
**exclusively** the check-12 spec ratchet. Line 2 reads "Fixture self-test for
check-memory-hygiene.sh CHECK 12 (spec-format ratchet)". Twelve fixtures at :64-77 drive 7 `hit`
(:86-92) plus 5 `miss` (:93-97), plus 2 blank-cutoff conf-contract assertions (:102-103). Line 105
prints `PASS (14 assertions)`. It is the only test file under `tools/memory-tree/`.

So the sentence is wrong on the count and **inverted** on coverage — the ratchet is the file's entire
subject; only the check-7 half is true.

**Consequences.** AC4 is inert: 14 > 4 is satisfied at HEAD by building nothing, and a rewrite that
deletes 9 of the 14 existing check-12 assertions and adds 1 still clears it. S5 also mis-scopes the
work — the builder is told to write check-12 arms that already exist, while the real gaps are check 7
(zero coverage), the CR source assertion, and `--staged` (F9). Upstream anchored its own AC4 on the
right number: PERF-aSlothfulCapstan-1 AC4 reads "not lower than the current 14".

**Edit.** S5 → "14 assertions today, all check-12 fixture classes; check 7 has no coverage."
AC4 → "all 14 existing assertions still pass **unmodified**, and the new arms are additive" — a floor
on the *surviving set*, not on a count, since a count cannot distinguish new coverage from old.
Q2 → re-derive the arm menu against 14, not 4.

---

### F2 — HIGH · No locale constraint on the check-7 awk, and the in-file precedent carries `LC_ALL=C`

*(merges three lenses)*

Check 7's verdict is `length($0)>300`, whose char-vs-byte meaning is a property of the awk build and
the ambient locale. The spec's S2 names only two things to preserve (the unfenced `FNR` numbering and
the `$ex7`/`$MAP_SUB` exemption) and §4 tells the builder to reuse the file's existing collapsed
idioms. Nothing in the spec mentions locale.

**Verified.** Kit check 7 (`check-memory-hygiene.sh:242`) carries no locale prefix. The other batched
awk in the same file, 17 lines below at `:259`, is `printf '%s\n' "$files8" | LC_ALL=C xargs -r awk`.
Upstream wrote the prohibition into the very code being ported — `check-docs-hygiene.sh:368-370`:
"NO `LC_ALL=C` here, deliberately. `length()` is what decides the verdict... Pinning the locale would
silently re-decide the cap on any node where awk counts characters today."

**Why no AC catches it.** Measured on this node (gawk 5.4.0, `LANG` empty, `LC_ALL` unset):
`printf 'a·b' | awk '{print length($0)}'` returns **4** ambiently and **4** under `LC_ALL=C`, but
**3** under `LC_ALL=en_US.UTF-8`. Ambient already equals C here, so an AC1/AC2 byte-identical parity
run on this node is structurally blind to the flip. The exposure is adopter-side — a UTF-8-locale
node such as the Linux `f` node — and the kit is project-agnostic by design.

**Edit.** Add to S2: "the check-7 awk takes NO `LC_ALL=` prefix and no `xargs` wrapper that sets one
— locale-dependent `length()` is the current, deliberate behaviour; check 8's `LC_ALL=C xargs` at
:259 is not the pattern to copy here." Add a self-test arm with an ASCII 300/301 pair plus one row
that is ≤300 characters and >300 bytes, asserted silent — the only shape that catches the flip.

---

### F3 — HIGH · AC6 is pinned to a wall-clock number that does not reproduce, and half of it has no baseline at all

*(merges four lenses; I re-measured)*

AC6: "check 12 and check 7 are each under a second, and the total is below the 27.4s baseline."

**Measured, unmodified script, this tree, this session:** `real 2m3.465s · user 0m6.769s · sys
0m18.795s`. CPU roughly reproduces the spec's `6.0s / 17.3s`; wall is **4.5×** the claimed 27.4s
baseline with no code change. The four finder agents independently measured 45.6s, 48.6s, 52.4s,
55.1s, 82.2s, 1m29s, 3m12s, 4m50s, 4m7s and 6m6s on the same unchanged tree. Upstream banks the same
instability in its build record: "Its wall time swings 2-8 minutes at fixed code on this node."

So AC6 can fail a correct port and pass a broken one. It is not a decidable acceptance criterion on
an agent machine.

The other half is worse: **the spec records no before-value for either check.** §4 gives check 12 and
check 7 only a line range and a fork count, and the 11s figure is an extrapolation from upstream's
per-spec rate, not a measurement. Nothing in S1-S7 adds per-check instrumentation, so the unit as
scoped ships no means to make the observation AC6 demands.

**Measured per-check baseline** (timers injected around each `# N —` block, one run, this tree):

| check | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| s | 0.46 | 2.45 | 11.35 | 5.34 | 2.58 | 4.50 | **7.86** | 1.84 | 0.87 | 1.38 | 0.26 | **42.88** |

**Edit.** Put that table in §4 as the measured baseline. Restate AC6 against a deterministic quantity
— fork count for the two checks, or `user+sys` measured before and after **in the same session on
the same machine** — and drop the bare 27.4s wall threshold. Add the per-check instrumentation to §2
as a scope item, or the AC names an observation the unit cannot make.

---

### F4 — MED · Every count in the §4 Inventory table is wrong

*(merges four lenses)*

| §4 says | Actual | How verified |
|---|---|---|
| "spec files in the check-12 population \| 16" | **12** | 16 files sit under `builds/*/spec/`; the check-12 glob at `:325` matches 13; `SPEC_FORMAT_CUTOFF="2026-07-15"` (`.memory-tree.conf:18`, enforced at `:326-327`) drops `2026-07-14-spec-aKitHardener-1.md` |
| "tracked files under memory/ \| 74" | **75** | `git ls-tree -r --name-only e8d046cc -- memory/ \| wc -l` |
| "about 13 forks per spec" | upstream's figure | presented in a table headed "Measured on this repo" |

The three files under `spec/` that never match the glob are the free-named legacy specs the script's
own comment at `:312-313` describes: `governance-deployer-research.md`, `manifest-ratchet-spec.md`,
`template-v2-rework-spec.md`.

The 33% overstatement is not cosmetic — 16 is the direct multiplicand of "about 11s of this repo's
27.4s is the same defect", which is the unit's headline justification. At the true population it is
~8.6s. The conclusion survives (measured check 12 is 42.9s, far more than either estimate), but the
stated arithmetic does not reproduce.

**Edit.** Correct the row to "spec files entering the check-12 per-spec body | 12 (13 match the glob,
one is pre-cutoff; 3 more under `spec/` are legacy-named and never match)", the tracked count to 75,
and label the fork-per-spec row as upstream's measurement of upstream's larger check 12. Replace the
extrapolation with the measured 42.88s from F3.

---

### F5 — MED · Q3's justification is false, and its recommended branch breaks the unit's own §3 and AC1/AC2

*(merges two lenses)*

Q3 recommends adding the missing `/^## /{f=0}` reset to the §9 rev scan "now", calling it
"behaviour-neutral against a nine-section canon" because "§9 is the last canonical section, so
nothing can follow it".

That conflates *the canon has nine sections* with *no spec file carries a tenth heading*. Check 12
runs the rev scan on **non-conforming** specs too — the canon-differ branch at `:344-347` emits its
finding and does **not** `continue`, so control falls straight through to the `lrev` awk at `:352`
for exactly the population check 12 exists to catch.

**Reproduced.** Against a file `## 9. Revision log / - rev-1 / ## 10. Appendix / see rev-99`:
the current no-reset awk yields `mx=99`; with the reset it yields `mx=1`. The reset can only shrink
the scanned range, so `mx` can only fall and the `hrev > lrev` test at `:353` can only produce **more**
findings. That is a verdict change, which §3 declares "a bug in this unit" and AC1/AC2 forbid.

Corollary: upstream's **pre**-change revision already had it (`53180648d:scripts/check-docs-hygiene.sh:485`
— `{f=1; next} /^## /{f=0}`), and upstream's ported harness ships shape 13 for it. The kit is the
copy that dropped the reset, not upstream that added it late.

**Tempering fact.** I ran both awk variants over every spec in this corpus: zero divergence — no spec
carries any `## ` heading after §9. So AC1 against the real tree would not catch it; the exposure is
confined to AC2's hand-authored pathological corpus, written by the same builder.

**Edit.** Rewrite Q3: state that the reset is a **verdict change** on non-conforming specs and
therefore cannot ride this unit under §3/AC1/AC2. Offer two branches only — (a) a BACKLOG row for a
separate unit, or (b) explicitly carve the rev scan out of AC1/AC2 here and add a fixture pinning the
new verdict. Delete "add it now, it is behaviour-neutral".

---

### F6 — MED · S6 says two version literals; four carry `1.3`, and the two ungated ones have drifted before

*(merges three lenses)*

S6 bumps "BOTH hand-kept literals" and AC7 leans on `check-kit-versions.sh` to prove it. Grep over
the worktree finds **four** live `1.3` sites:

1. `tools/memory-tree/check-memory-hygiene.sh:13` — `KIT_MEMORY_TREE_VERSION=1.3` **and**
2. the inline `# gov:kit memory-tree@1.3` marker on that same line
3. `tools/memory-tree/HYGIENE.template.md:1`
4. `memory/HYGIENE.md:1` — this repo's own dogfooded install (`adopt-memory-tree.sh:39` is a plain
   `cp` of the template; `:30` greps that marker as the installed-kit signal)

`check-kit-versions.sh:30-34` reads only the constant and the **template** marker — its own comment
even says "TWO hand-kept literals". So AC7 goes green with the engine advertising a version it no
longer is, and with this repo reporting 1.3 while running 1.4.

**Not hypothetical.** `git show d510bc7` (the previous bump) says verbatim: "Kit bumped memory-tree
1.2->1.3 (constant + both markers agree; also fixed HYGIENE.md's stale @1.1)" — the installed marker
had silently missed a whole version.

Today's blast radius is small (`check-kit-versions.sh`'s own header notes no consumer reads these
constants until the unbuilt Phase-1 deployer), but a self-contradictory identity comment in the
shipped engine is a trap for exactly the repo-wide grep that deployer will use.

**Edit.** Enumerate all four sites in S6. Add `memory/HYGIENE.md` to the §4 files-touched table.
Restate AC7 as "`check-kit-versions.sh` passes **and** `grep -rn 'memory-tree@1\.3'` over the
worktree returns nothing" — the gate alone cannot prove the bump landed.

---

### F7 — MED · §4 names only `ARGIND` as an awk-portability hazard; five interval expressions move into awk unmentioned

§4 justifies bash-side tagging by citing `ARGIND` as gawk-only. That is the lesser hazard. Every
regex this port moves from `grep -E` into awk carries interval expressions:
`check-memory-hygiene.sh:332` has `[0-9]{4}-[0-9]{2}-[0-9]{2}` and `[0-9a-f]{8}`; `:338` has
`[0-9a-f]{8,}`.

Interval support is not universal in awk. On a build that treats `{8}` literally, the Status-header
regex demands the literal bytes `{8}` in the text and therefore **never** matches — every spec dated
≥ the cutoff reds with "missing/invalid **Status:** header". The port would break a check that works
today under `grep -E` on every platform, which violates the spec's own §3 non-goal.

Upstream spelled every interval out by hand for exactly this reason, with the rationale in-line at
`check-docs-hygiene.sh:542-543`: "mawk is what CI runs, and a `{4}` that a build does not honour
turns a shape assertion into a substring match without saying so." Its expanded form is at `:545`
and `:551` (eight bracket classes for the sha).

Failure here is loud, not silent (the shipped `miss` arms red on the affected machine), and
mawk ≥ 1.3.4 and busybox awk both honour intervals — so the exposed adopter population is narrow.
It is still one sentence of prophylaxis the spec should carry, given the kit ships to arbitrary
adopters including a Linux node.

**Edit.** Add to §4: "every interval expression is spelled out character-by-character in the batched
awk, because interval support is not universal and a non-honouring build turns the header assertion
into a never-matching literal." Add a self-test arm asserting the batched awk source contains no
`{n}`/`{n,}` in a regex literal.

---

### F8 — MED · The §8 `sed` reproduction is specified for one hazard; three range behaviours decide the same verdict

§4 correctly nails the `$d`/trailing-blank hazard, but describes `$d` as deleting "the LAST line of
the range". It deletes the last line of the **concatenated range output**, and the range has three
further properties the spec never states: it **restarts** on every later `/^## 8\. Open questions/`
match, it runs to **EOF** when `/^## 9\. /` never matches after the opener, and a range shorter than
three lines yields nothing.

**Both divergences reproduced with real `sed`:**

- Shape A — `## 8` heading twice, empty first body. The current pipeline yields `## 8. Open
  questions`, which matches neither `none*` nor `N/A*` nor `''` → **FINDING**. A naive per-range awk
  that drops both headings yields `none` → **silent**.
- Shape B — `## 8. Open questions` / `- unresolved` / `## 10. Appendix`, no §9. The range runs to
  EOF, `$d` removes the `## 10.` line, survivor is `- unresolved` → **FINDING**. An implementation
  stopping at the next `^## ` heading drops it as the range's last line → **silent**.

Upstream states all three in one comment at `check-docs-hygiene.sh:608-609` and its `rng[]` loop
implements them. AC2 names exactly one pathological shape; these two meet the spec's own inclusion
criterion (absent from the committed corpus, therefore invisible to the fixture suite).

**Edit.** Restate the §4 sentence as "the two deletes act on the **concatenated range output**", add
the restartable / run-to-EOF / <3-line properties, and name both shapes above as required members of
AC2's corpus.

---

### F9 — MED · `--staged` mode is the only mode where the rewritten `in_scope` filter does anything, and the spec never mentions it

Both rewritten checks carry `in_scope "$f" || continue` — check 12 at `:328`, check 7 at `:241`.
`in_scope` (defined at `:68`) short-circuits with `return 0` whenever `STAGED=0`, so it is a no-op in
full mode and decides the whole selection in `--staged` mode — the pre-commit fast leg every adopter
wires, and the one whose red must never be another stream's debt.

The string "staged" appears nowhere in the spec: not in S4's enumerated upstream corrections, not in
S5, not in any AC. `check-memory-hygiene.test.sh` invokes the script only at `:81` and `:101`, both
bare. AC1 and AC2 are full-mode comparisons and are therefore structurally incapable of seeing a
scoping regression.

Upstream gives it a dedicated arm: `scripts/hygiene-parity.test.sh:189-202` (`say "-- --staged
mode"`, `b_stg=$(run "$BEFORE" --staged)`, **plus a guard that the staged run actually produced a
check-12 finding** so the comparison is not vacuously equal on empty output), and `:220` runs the
spoiled-side check in `--staged` too. The port cannot be verbatim — the kit has no
`--print-index-set` flag — so the builder must select arms, and the spec names only two to keep.

**Edit.** Add the `--staged` arm (including upstream's non-vacuity guard) to S4's list of corrections
to port, add a `--staged` arm to S5, and extend AC1/AC2 to "in both full and `--staged` mode".

---

### F10 — MED · §3's blanket exclusion states a reason that is measurably false for check 3

§3 excludes every other check because "Their cost is not measured as significant on the kit's own
corpus". No per-check measurement appears anywhere in the spec, and when taken (F3's table) it
refutes the claim for check 3: **11.35s**, against check 7's **7.86s** — check 3 costs ~1.4× one of
the two checks being rewritten, and sits inside the excluded range "1 through 6".

The honest exclusion axis is **growth**, not magnitude. Check 3 forks per top-level entry (`:125`,
`printf '%s\n' $DISCIPLINES | grep -qxF "$d"`) and per discipline, both O(disciplines) and flat as an
adopter tree grows. Check 10 forks three times per rotated archive (`:291-293`; 3 archives here).
Only checks 7 and 12 are O(files). The spec gestures at this once ("the cost belongs to whichever
adopter tree grows") and then states the wrong reason in the non-goal.

Check 9 is separately and correctly excluded — TOOL-bThriftyBellows-2 is DEFERRED on a measured
negative result.

**Edit.** Replace the "not measured as significant" clause with the F3 table plus the growth
argument, and name `:125` and `:291-293` explicitly as known, out-of-scope fork sites so a later
sweep does not re-find them.

---

### F11 — LOW · The TAB guard is a runtime branch on a compile-time constant, and its message is underspecified

*(merges two lenses)*

§4 keeps upstream's `C<TAB><heading>` canon records and adds a `case` guard on `$SPEC_CANON` for the
TAB truncation those records introduce — describing it as reddening "once with the artifact named",
in the same bullet that establishes "there is no `CANON_FILE`, and therefore no missing-artifact arm
to hang a guard on". A builder cannot implement that sentence: there is no artifact and no
regeneration command to put in the message.

**Verified.** `.memory-tree.conf` is sourced at `:21`; `SPEC_CANON` is assigned unconditionally at
`:316-324` as a nine-line inline string; the comparison is one equality at `:344`. No config or
environment path can put a TAB in it — only a source edit can. Upstream needed the array because it
derived a nine- **and** a ten-heading variant from one generated **file** (`7e169b796:469, :476,
:479`); §4 deletes that requirement one paragraph earlier ("the comparison stays one equality").

I confirmed the simpler shape works: `awk -v canon="$SPEC_CANON"` with embedded newlines compares
EQUAL against a `got` built from `^## ` lines. So the C records, the TAB hazard and the guard are all
self-inflicted here.

Also undefined: what "reds once" does to the rest of check 12. Upstream's arm explicitly *skips the
per-spec section-canon compare* (`check-docs-hygiene.sh:477-479`); the spec says nothing, and
"skip the compare" silently disarms the section-canon assertion.

**Edit.** Pass the canon via `awk -v canon="$SPEC_CANON"` and drop the `C` record and the runtime
guard. If a TAB invariant is still wanted, assert it at source level in
`check-memory-hygiene.test.sh` next to S5's CR assertion — the mechanism the spec already chose for
the sibling hazard. If a runtime guard is kept anyway, state its message text and exactly what it
does to the remainder of check 12.

---

## Sub-claims I dropped

Reported by finders, refuted or unprovable on re-check. Listed so nobody re-finds them:

- **"the 27.4s baseline is wrong."** Unreproducible, not wrong. The CPU half (`user 6.0 / sys 17.3`)
  reproduces within noise; a quiet machine could plausibly produce a ~27s wall. Kept only as
  "unreproducible on an agent machine" inside F3.
- **"`memory/tooling/builds/2026-07-22-TOOL-bConvergentLodestar/README.md:19` straddles the check-7
  cap."** That file is not in check 7's selected set — `index_set()` at `:204-214` never includes
  build-folder READMEs. Its line 19 is also 310 bytes / 309 chars, over the cap under both readings.
  F2 survives on the structural argument; that evidence line is gone.
- **"check 10's rotated-archive population is 0."** Three archive files exist under
  `memory/*/archive/`.
- **"this node's awk counts characters, matching the ≤300-chars doc."** Measured false — `LANG` is
  empty and `LC_ALL` unset, so gawk is already in byte mode here and `LC_ALL=C` is a no-op on this
  node. F2's exposure is adopter-side, which is exactly why no AC on this machine can see it.
- **"the TAB guard names an artifact that does not exist" as a design refutation.** "with the
  artifact named" reads acceptably as naming `$M/TEMPLATE-SPEC.md`. Kept only the concrete
  under-specification in F11.

---

## Verdict

**Ready after the listed edits — once the spec file is restored.** Not a re-spec.

The design is sound and correctly derived: collapsing checks 12 and 7 to one awk over a TAB-tagged
driver stream is the right shape, the trailing-blank `$d` divergence is carried, the CR platform trap
is handled at source level rather than by a fixture, and the parity-harness-defaults-to-HEAD trap is
named. Every defect above is a wrong number, a missing constraint, or an unpinned acceptance
criterion — all of them rev-2 edits to a spec whose plan does not change.

Two things make it not-ready as it stands. The self-test baseline is false in both directions (F1),
which kills one of the acceptance criteria outright and points S5's scope at work that already
exists. And three of the ACs cannot decide anything: AC4 passes at HEAD unchanged, AC6 is pinned to a
wall clock that moved 4.5× on an unchanged tree in my own measurement, and AC1/AC2 are structurally
blind to both the locale flip (F2) and the `--staged` selection (F9). A gate bar that green-lights
the unmodified tree is not a gate bar.

Fix F1, F2 and F3 first — they are the ones that let a wrong build pass. F4 through F11 are
correctness of the record and of the fixture corpus.

## Revision log

- rev-1 · 2026-08-03 · node a · synthesis pass over 26 surviving findings from 5 lenses; every
  source, upstream and measurement claim independently re-verified at base `e8d046cc`; 11 distinct
  defects after de-duplication; 5 sub-claims dropped.
