# Manifest ratchet — spec (kickoff-manifest v1.0 → v1.1 + the enforcement chain)

*2026-07-12. Drives the change that makes per-project kickoff manifests LIVING documents. Problem: the
chain ships a read path (the engine loads the manifest every kickoff) but no write path — nothing
triggers an update after instantiation, no freshness signal exists, and nothing goes red when the
manifest lags the repo. Evidence: `nicocares/main/.claude/SESSION-KICKOFF.md` frozen at
`kickoff-manifest: v1.0 · instantiated from …` since instantiation, while the inCMS prototype
(210 lines) accreted dated corrections only through manual owner corpus-grooming the generic chain
never encoded.*

*Adversarially reviewed twice, 2026-07-12 — round 1: 18 agents (6 lenses → batched skeptics →
completeness critic), 52 raw → 39 confirmed + 5 gaps; round 2 over the folded revision: 3 verifiers
(git-mechanics breaker with throwaway-repo probes · fold-coherence auditor · goal skeptic), 22
surviving defects. All 66 folded; §13 maps them. Status: DRAFT v3 — owner approval, then build.*

---

## 0 · Goal, the three levers, and the enforcement floor

Goal: an instantiated manifest stays TRUE (claims match the repo) and ACCRETES (traps, corrections,
pointers, gate changes land in it as the project develops) — enforced by machinery, not aspiration.

- **Lever 1 — read-repair at kickoff** (engine Step 2b): every kickoff audits the manifest and repairs
  drift on the spot, so reading it stays safe and repair cost stays ≤2 minutes.
- **Lever 2 — write-back at close** (playbook DoD line + the manifest's own ratchet contract): a unit
  that changed what the manifest front-loads — or re-derived a fact it should have front-loaded, or
  caught a doc/memory claim being stale — writes the delta back before wrap-up.
- **Lever 3 — a machine gate** (`manifest-check.sh`): placeholder scan · block parse · anchor-sha
  validity · anchor tracked-ness · drift-vs-`last-audit` · watch-liveness — standing in the manifest's
  own gate-commands fence by default, hardened into pre-commit/CI when offered wiring is accepted.

**Supported enforcement floor (explicit):** a project with no CI and no pre-commit still gets lever 1
(kickoff-only) + lever 3 via the gate fence at every kickoff-derived unit's merge bar. In that mode
drift is detected at the NEXT kickoff/unit, not at commit time — pre-commit/CI wiring upgrades the
latency. (One stated semantic narrowing: the pre-commit `--staged` leg blocks the intermediate
watch-only commit, so it narrows C5's remedy to the bundle form — §3; WIRE states this at wiring
time.) This floor is a sanctioned mode, not a degraded one.

## 1 · Design principles (binding)

- The gate verifies **mechanical truth signals** (paths tracked, no placeholders, audit not overtaken
  by watched-file changes, watch list alive) — never the semantic truth of prose. Semantic repair is
  the engine's and the DoD's job; the gate makes skipping it visible and blocking.
- The `last-audit` stamp is an **assertion of verification** ("§B checked against reality"), never
  auto-updated by tooling on commit. The re-verify protocol (§4) leaves a delta-line evidence trail so
  a reflex stamp-to-green is at least visible in history, even if not machine-refutable.
- **Single source of the checks:** CI, pre-commit, the gate fence, and the engine all invoke
  `manifest-check.sh` — the checks are never reimplemented inline (house rule, per
  `check-memory-hygiene.sh`'s header).
- Keep the watch list SMALL and LOW-CHURN — false-red rate is the adoption killer; a red must almost
  always mean "the manifest really should be looked at".
- Kit conventions match the house: bash (Git-Bash locally, ubuntu CI), `set -u`, exit 0 + silence =
  clean, self-contained `MANIFEST check N FAILED — remedy` lines, engine-identical script overwritable
  wholesale, project-owned data (the audit block, the manifest body) never touched by kit updates.
- Precedence unchanged: `CLAUDE.md` > manifest > skill.
- **Named residuals (accepted, not solved):** (a) an adopter can deliberately narrow `watch` to
  silence reds — the audit block is project-owned and freely editable; manifest-diff review is the
  compensating control. (b) cross-repo claims are outside the sensing range and are tagged instead
  (§2). (c) a `verify-paths` anchor surviving as a dead stub passes C4 — the canary is cheap, not
  complete. (d) a repo with no resolvable default branch falls back to stamping `HEAD`, which a later
  history rewrite can orphan — C3's remedy is the recovery.

## 2 · The audit block (new, machine-readable — the only thing the checker parses)

One HTML-comment block, directly under the version marker:

```html
<!-- manifest-audit
last-audit: 2026-07-12T15:41:07+02:00 @ dacade1419ae6e951711252a374f4ab87446321b
watch: Makefile; .github/workflows/; scripts/
verify-paths: docs/PARALLEL.md; memory/architecture/DECISIONS.md
check-script: scripts/manifest-check.sh
-->
```

- `last-audit`: **ISO-8601 datetime with offset** · `@` · **full** commit sha. Datetime, not date — a
  genuine re-verify must ALWAYS produce a committable line change, even when the anchor sha is frozen
  (a unit branch's merge-base doesn't move; a date-only stamp would make a same-day re-stamp a
  textual no-op git refuses to commit, leaving C5 red with no remedy). The sha is the drift-scan
  anchor + the C3 ancestry claim; the datetime + the stamp COMMIT are the recency evidence.
- **Stamp rule:** ON the default branch → stamp `HEAD`. On any other branch → stamp
  `git merge-base <remote>/<default> HEAD`; no remote → `git merge-base <local-default> HEAD`
  (Step 0 already resolves the local default: `main`, else `master`). Only when no default branch is
  resolvable at all → `HEAD` (residual (d), §1). Rationale: only default-branch-history shas survive
  squash/rebase landings — a branch sha stamped into the file is orphaned the moment the branch is
  squashed, and reds C3 on the default branch forever.
- `watch`: `;`-separated **git pathspecs** passed verbatim to `git diff`/`git rev-list`. Directory
  prefix = whole subtree; prefer prefixes over globs. Derive from the files the manifest's OWN
  gate-commands fence and layout claims read — CI workflow files, `Makefile`, script dirs first.
  **Never lockfiles; treat `package.json`-class files as high-churn** (a dep bump reds the gate with
  no §B impact — watch them only if gate commands genuinely derive from them, and expect bot-PR reds:
  the maintainer re-stamps on the bot PR, or scopes the CI leg to non-bot branches). ≤~8 pathspecs.
- `verify-paths`: `;`-separated repo-relative paths that must exist as **tracked** content — capped at
  the 2–3 highest-value anchors (the playbook + the top governing doc/dir), NOT a mirror of the
  pointer map (a hand-kept second copy of §B would just drift against it; prose paths are verified
  semantically by the Step 2b repair pass, not by C4).
- `check-script` (optional): where this project keeps the checker; default
  `scripts/manifest-check.sh`. Read by the engine, the gate-fence line, and the wire docs — a
  non-default location must be machine-resolvable everywhere the checker is invoked.
- **Cross-repo tag:** a §B/trap claim whose truth lives in ANOTHER repo (e.g. nicocares' "tests run in
  inCMS core CI") is suffixed `(cross-repo — verify at use)` and is explicitly OUTSIDE the
  `last-audit` assertion — watch pathspecs are single-repo; don't fake-cover such claims with
  unmatchable specs.
- Parsing contract: keys one per line, case-sensitive, `\r` stripped, values trimmed, **empty elements
  after `;`-split dropped** (a trailing/doubled `;` must not reach git as an empty pathspec — that's
  a fatal 128); unknown keys ignored (forward-compat); exactly one block per manifest.
- **Unmanaged manifests:** a SESSION-KICKOFF.md with NO `kickoff-manifest:` marker (e.g. the inCMS
  prototype) is not ratchet-managed — the checker exits 0 with a one-line NOTE and the engine skips
  Step 2b in one stated clause. No recurring retrofit nag.

## 3 · `manifest-check.sh` (the gate) — ships at `skills/session-kickoff/manifest-check.sh`

Modes: `manifest-check.sh [<manifest-path>]` (full) · `--staged` (pre-commit leg). No args → discover
the manifest at the four fixed paths (`docs/claude/` → `docs/` → `.claude/` → repo root
`SESSION-KICKOFF.md`). The engine's 5th fallback (the `governance-template:` marker grep) is
**deliberately excluded** — a governance doc is not a manifest and would fail C2 confusingly. Exit 2
therefore means "not a git repo, or no SESSION-KICKOFF.md at the four paths" — wiring may gate on it
knowingly. The script carries `KIT_MANIFEST_VERSION="1.1"`; a manifest whose marker version is older
→ non-blocking `WARN: manifest format vX.Y < kit v1.1 — see the upgrade recipe in
coding-governance/WIRE-INTO-PROJECT.md §4` (the forward-drift signal that keeps v1.1 instances from
freezing the way v1.0 did — kit updates overwrite the script wholesale, carrying the new constant in).

Checks — each with a self-contained `fail N` message + remedy actionable WITHOUT this spec (a
supplementary pointer to the gov repo's WIRE doc is permitted; a load-bearing one is not):

- **C1 — no placeholder survives:** `grep -nE '\{\{[A-Z]'` over the manifest. The pattern is the
  placeholder SHAPE, not bare `{{` — gate fences legitimately hold `${{ secrets.X }}` Actions
  expressions, Go-template `{{.State.Status}}` format strings, Helm snippets. (v1.1 normalizes all
  template placeholders to UPPERCASE-keyed form so the pattern is complete — §5.)
- **C2 — audit block present + parseable:** all of `last-audit`/`watch`/`verify-paths` found with
  **non-empty** values after the empty-element drop. Missing block on a `kickoff-manifest: v1.0`
  manifest → fail, message inlining the retrofit short form and stating that the FULL recipe —
  including the body-delta step and the lever-2 playbook re-pull step, which the short form omits —
  lives in `coding-governance/WIRE-INTO-PROJECT.md §4`.
- **C3 — anchor sha is real and ours:** `git cat-file -e <sha>^{commit}` and
  `git merge-base --is-ancestor <sha> HEAD`, with DISTINCT remedies: unknown sha → "stamp is foreign
  or predates a history rewrite"; known-but-non-ancestor → "history was rewritten or the stamp was
  squash-merged". Both remedies inline the stamp rule itself — "re-verify §B, then re-stamp: HEAD on
  the default branch, else `git merge-base <remote>/<default> HEAD`" — because this spec's §2 does
  not ship to adopting repos. Shallow-clone exception: `git rev-parse --is-shallow-repository` true AND sha absent → WARN naming
  the fix ("set `fetch-depth: 0` on the checkout step") and skip C3+C5 — and the WIRE §4 CI recipe
  MANDATES `fetch-depth: 0`, because default shallow checkouts would otherwise silently skip the
  drift check on the primary enforcement surface.
- **C4 — every `verify-paths` entry is tracked:** files via `git ls-files --error-unmatch`, dirs via
  `git ls-files -- <path>/ | grep -q .` — tracked-ness, not `-e` (an untracked leftover at a dead
  path must not green the local leg while fresh-clone CI reds).
- **C5 — no unaudited drift (topological, not textual).**
  `W = git rev-list -1 <sha>..HEAD -- <watch…>` (newest watch-touching commit; empty → green).
  `S = git log -1 --format=%H -G'^last-audit:' <sha>..HEAD -- <manifest>` (newest commit that changed
  the stamp line; `git log`, not `rev-list` — rev-list rejects `-G`).
  **Green iff S is non-empty AND `git merge-base --is-ancestor W S`.** W==S (reflexive) is the
  one-commit bundle — a commit carrying the watched change plus the §B re-verify + re-stamp is green
  by construction; S a proper descendant is the follow-up re-stamp; and a stamp that does NOT descend
  from W — e.g. a mainline kickoff re-stamp predating a true-merged branch's drift — correctly reds.
  The ancestry test is the load-bearing part: a textual changed-in-range check (v2 of this spec) was
  empirically shown to launder unaudited drift through every conflict-free true merge, because any
  unrelated mainline stamp inside the range greened it. No `W^` is ever computed (multi-root
  histories made it fatal). Remedy: "for each file `git diff <sha>..HEAD --name-only -- <watch…>`
  lists, re-check the §B claims derived from it, update the manifest where stale, re-stamp (HEAD on
  the default branch, else the merge-base — the rule inlined, not referenced) — bundled with the
  watched change or as a follow-up in the same PR; after a merge that brought in watch-touching
  commits, the fresh post-merge audit + re-stamp IS the close."
- **C5s (`--staged` leg):** staged watch changes (`git diff --cached --name-only -- <watch…>`
  non-empty) require the STAGED manifest hunk to touch the `last-audit:` line
  (`git diff --cached -U0 -- <manifest> | grep -q '^+last-audit:'`) — co-staging an unrelated
  manifest edit does not count. **Deliberate narrowing (stated, not accidental):** a blocking staged
  leg cannot see a future follow-up commit, so its fail message says "bundle the re-verify +
  re-stamp into THIS commit" — the bundle form only. The guarantee is one-directional and that is
  the intended direction: every C5s-green commit is C5-green (verified); C5's follow-up remedy
  additionally exists for adopters without the pre-commit leg. C1/C2/C4/C6 run always (cheap).
- **C6 — watch list is alive:** every watch pathspec matches ≥1 tracked file
  (`git ls-files -- <spec> | grep -q .`) — a typo'd or restructure-orphaned pathspec is a silent
  permanent false-green on the only drift check we have (the freeze bug reintroduced one level up).
  Plus a breadth WARN when a single pathspec matches >100 tracked files (watching `src/` wholesale
  guarantees red-fatigue).
- Exit contract: `0` silent-clean (WARN/NOTE lines permitted) · `1` any check failed · `2` environment
  error. LF-forced in BOTH repos: the gov repo's `.gitattributes` covers the kit copy, and WIRE §4
  adds the rule to the adopting repo (§7) — a CRLF checkout on autocrlf Windows kills bash silently.

Self-test `skills/session-kickoff/manifest-check.test.sh` (NEW, mirrors `hooks/agent-cap.test.sh`):
throwaway git repo in the scratchpad/`$TMPDIR`; scenarios — clean pass → 0 · surviving `{{GATE}}` →
C1 · `${{ github.sha }}` in the gate fence → still 0 · missing block → C2 · empty `watch:` value →
C2 · bogus sha → C3 · valid-but-non-ancestor sha (simulated rewrite) → C3's second remedy · dead
verify-path → C4 · untracked-file-at-verify-path → C4 · watch commit without re-stamp → C5 · bundled
watch+re-stamp commit → 0 · follow-up-commit re-stamp → 0 · **cross-mode pair: the C5s-green staged
bundle, once committed, passes full-mode C5** · **true-merge laundering probe: branch with unaudited
watch drift + independent mainline re-stamp + conflict-free merge → C5 RED; post-merge fresh audit +
re-stamp → green** · same-day re-stamp on a frozen branch anchor commits and greens (datetime
monotonicity) · no-remote squash-merge with the §2 fallback stamp → C3 holds on main · merged
orphan-root watch history → clean fail-or-green, never a raw git fatal · staged watch without staged
stamp → C5s · staged watch with unrelated manifest edit → C5s · trailing `;` in watch → parsed
clean · dead watch pathspec → C6 · single pathspec matching >100 tracked files → breadth WARN + 0 ·
unmanaged manifest (no marker) → 0 + NOTE · v1.0 marker → C2 with retrofit message · shallow sim
(`git clone --depth 1`) → WARN + 0.

## 4 · Engine changes (`skills/session-kickoff/SKILL.md`)

- **NEW Step 2b — audit the manifest (read-repair):** resolve the checker — the manifest's
  `check-script:` value, else `scripts/manifest-check.sh`, else the copy shipped BESIDE this skill
  (the skill dir junction-resolves per Scaffolding step 1) — and RUN it; **never reimplement the
  checks inline** (single-source rule). No bash available → proceed unaudited, say so in one clause.
  Manifest unmanaged (no marker) → skip, one clause. Version WARN → relay it, don't block.
  - On failures: repair NOW as part of kickoff, per the **re-verify protocol**: for each file C5
    lists, name the §B claim(s) derived from it (gate fence ← CI/scripts; pointer map ← moved dirs;
    traps/corrections ← toolchain files), check those claims, fix or DELETE stale rows — and evaluate
    the dated-corrections section's prune-when conditions, deleting entries whose condition now holds.
    ≤2-minute pass; a deep restructure becomes a flagged §A task instead.
  - Re-stamp per the §2 stamp rule, and record the outcome as a mandatory delta line —
    `manifest-audit: delta <none | one-line summary incl. deletions> · watch-commits-since-stamp: <n>`
    (n from `git rev-list --count <sha>..HEAD -- <watch…>`) — in the repair commit message AND the
    READY card. The delta line is the evidence trail distinguishing "verified, nothing stale" from a
    reflex stamp, and supporting color for the §10.9 stall review (not its data source — squash
    merges destroy branch commit messages).
  - **Commit vehicle:** the repair rides the session's unit branch/worktree; where project conventions
    forbid direct primary-tree commits, it is NEVER one.
- **Scaffolding step 2 additions:** derive + fill the audit block (per §2's derivation rules); stamp
  per the §2 stamp rule — and if the repo has NO commits yet, make (or ask for) the initial commit
  first, then stamp it (an unborn branch has no sha C3 could ever accept); copy `manifest-check.sh`
  in (default `scripts/`, record any other choice in `check-script:`); `git add` the copied files
  before the first check run (C4/C6 test tracked-ness — index state satisfies `ls-files`); add
  `bash <check-script value>` as a **standing line in the manifest's gate-commands fence** — Step 3
  derives every unit's "gates it must pass" from that fence, so the gate rides every kickoff-derived
  merge bar with zero CI wiring (the enforcement floor); offer — separately, don't bundle — the
  pre-commit `--staged` leg + CI leg hardening.
- **Step 2 fallback fix:** the `governance-template:` marker grep skips files whose name contains
  `.template` or whose body still contains `{{`-shaped placeholders — a template is not an
  instantiated governance doc (today the fallback false-positives inside `coding-governance` itself).
- Search order UNCHANGED (back-compat: inCMS's `.claude/SESSION-KICKOFF.md` still resolves third —
  and now skips as unmanaged instead of nagging).

## 5 · Template changes (`MANIFEST-TEMPLATE.md` → v1.1)

- Marker bumps to `kickoff-manifest: v1.1`; audit block lands beneath it with placeholders
  `{{AUDIT_DATETIME}} @ {{AUDIT_SHA}}` · `{{WATCH_PATHSPECS}}` · `{{VERIFY_PATHS}}` (+ the
  `check-script:` line pre-filled with the default).
- **§B intro sentence REWRITTEN** — the current "§B is written once … thereafter each session READS
  it" is the freeze contract this whole spec exists to kill; it becomes "derived at instantiation;
  re-audited every kickoff (ratchet section below); accretes". Two conflicting standing directives in
  one file would have an agent obeying the older one.
- NEW section "**The ratchet — how this file stays true**" (one-line-per-directive): kickoff audit +
  read-repair · DoD write-back with the FULL trigger list (changed front-loads · a trap hit · a
  doc/memory claim found stale · **a fact this session had to re-derive that this file should have
  front-loaded** — the accretion trigger; repair alone never grows a thin-but-true manifest) ·
  `last-audit` = assertion, re-stamped only after actual re-verify, delta line required · the stamp
  rule itself (HEAD on the default branch, else the merge-base against it) · dated entries carry
  prune-when and get deleted when it holds.
- NEW section "**Current posture — dated corrections**" — the inCMS-P2 analogue, the prototype's
  single richest content class, which v1.0 had no home for (traps ≠ corrections: a correction
  OVERRIDES a stale doc/memory claim). Entry shape:
  `<date> · <what is stale where> · <the correction> · prune when <condition>`. **Starts empty;
  prunable per-ENTRY, never deletable as a section** — the template's "delete sections that don't
  apply" convention would otherwise remove the empty section at scaffold time, silently reopening the
  no-home-for-corrections hole this section exists to close.
- Traps section note: "this list ACCRETES — append the trap that cost this session time, prune the one
  that stopped being true".
- Gate-commands fence gains the standing checker line, written from the `check-script:` value (§4).
- **Placeholder normalization:** every body placeholder becomes named-UPPERCASE `{{X}}` form (the
  current template has unnamed prose blobs like `{{e.g. "feature/<name>…}}`), and the Customize block
  enumerates the full set by name (playbook v2.0 convention) — this is what makes C1's pattern
  complete and acceptance §10.3's both-direction parity checkable at all.

## 6 · Playbook change (`parallel-coding-governance.template.md` v2.1 → v2.2)

Two insertions (both §1), one after the memory/ledger DoD line, one into the Landing block:

> - Kickoff manifest (when the project keeps one) updated if this unit changed what it front-loads —
>   a gate command, entrypoint, governing doc, layout/branch convention, a trap hit, a doc/memory
>   claim found stale, or a fact re-derived that it should have front-loaded — re-stamp `last-audit`,
>   delta line in the write-back commit message; no delta → no touch.

> - (Landing/reconcile list) The kickoff manifest reconciles like other shared mutable files EXCEPT
>   its `last-audit` line: on a stamp conflict, resolve the conflicted line to EITHER side, complete
>   the merge, then immediately re-verify §B against the merged tree and re-stamp in a follow-up
>   commit, per the stamp rule — post-merge HEAD when the merge landed ON the default branch, the
>   merge-base otherwise (a branch-side sync merge stamped with branch HEAD would mint exactly the
>   squash-orphanable sha the rule exists to prevent; and a commit cannot embed its own sha, so
>   "stamp the merge from inside the merge" is unsatisfiable). The same post-merge fresh audit closes
>   any merge that brought in watch-touching commits, conflict or not. Prose sections reconcile
>   additively.

Version mechanics per house rule: snapshot current file as
`parallel-coding-governance.template-v-2-1.md`, bump header + `governance-template:` marker to v2.2;
v2.2 stays §-body-diffable against v2.1.

## 7 · Wire-docs changes

- **WIRE-INTO-PROJECT.md §4** gains, in order: copy `manifest-check.sh` → add the adopting repo's
  `.gitattributes` line (`scripts/manifest-check.sh text eol=lf`, or a repo-wide `*.sh` rule — mirror
  the memory-tree EOL step; the gov repo's own attributes don't travel with `cp`) → fill the audit
  block (derive, don't ask) → gate-fence line from the `check-script:` value → **`git add` the copied
  + edited files** (C4/C6 test tracked-ness; an unstaged fresh adoption can't pass) →
  `bash scripts/manifest-check.sh; echo $?` → 0 (path adjusted when `check-script:` is non-default,
  here and in the `.gitattributes` line) → offered hardening: pre-commit `--staged` leg
  (guarded so a scripts-less checkout stays green; the offer text states the bundle-only narrowing,
  §3 C5s) + CI leg **with `fetch-depth: 0` mandated on the checkout step**.
- **WIRE §4 also hosts the durable RETROFIT RECIPE** (the §9 steps with this spec's internal
  §-references resolved to their WIRE/manifest homes — WIRE's own § numbering differs; including the
  body-delta step and the lever-2 playbook re-pull); the gate's C2 message inlines the short form and
  points here. A note in the gov-repo template header cannot reach v1.0-instance readers, and this spec
  doesn't ship to adopting repos.
- **WIRE §6 (verify the chain)** — the red/green probe, corrected to committed-tree reality (C5 reads
  commit ranges; an uncommitted touch is invisible): *commit* a throwaway change to a watched file →
  full check red (C5) → re-stamp (bundled or follow-up) → green → **revert the throwaway AND the
  probe re-stamp together in ONE commit** → still green (the revert commit touches the watched file,
  so a bare revert would end the wiring session red — the combined commit's own stamp-line change
  satisfies C5). When a CI leg was wired: push the probe branch and confirm the CI leg actually reds
  (proves it isn't WARN-skipping on a shallow checkout).
- **WIRE Maintenance** adds: `manifest-check.sh` is engine-identical — overwrite wholesale from
  `<gov>` (this also delivers the version-WARN constant); the audit block + manifest body are
  project-owned — never overwritten; the playbook re-pull procedure now carries the §6 insertions to
  instantiated playbooks; and the **stall review** (§10.9) rides this same Maintenance cadence.
- **README.md** `skills/session-kickoff/` bullet gains the ratchet sentence.

## 8 · This machine — junction repair (config fix, not repo content)

`C:\Users\d41ly\.claude\skills\session-kickoff` is today a plain directory holding a stale copy of the
inCMS-tuned SKILL.md — the generic engine never fires. Repair: confirm the inCMS-tuned variant still
lives in the inCMS repo (`C:\projects\incms\main\.claude\skills\session-kickoff\`), delete the stale
user-level directory, create the junction per README
(`New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\session-kickoff" -Target "C:\projects\coding-governance\skills\session-kickoff"`),
restart, verify the listed description reads "Start a work-unit cleanly in ANY project". Reversible.

## 9 · Retrofit recipe (existing v1.0 manifests — first candidate: nicocares, separate follow-up unit)

1. **Body deltas first:** rewrite the §B intro/heading to the v1.1 wording; insert the ratchet
   section; insert the dated-corrections section (empty — never deleted); add the traps-accrete note.
   Without this the retrofitted file keeps its standing freeze directive ("written once … each
   session READS it") — the very sentence the spec diagnoses — and the older in-file contract wins.
2. Insert the audit block: `verify-paths` = the 2–3 anchors; `watch` derived from what its gate
   commands read; tag cross-repo claims `(cross-repo — verify at use)` while deriving (nicocares'
   inCMS-side claims are exactly this class); stamp `last-audit` **after actually re-verifying §B**,
   per the §2 stamp rule.
3. Copy `manifest-check.sh` + the `.gitattributes` line; add the gate-fence line (from
   `check-script:`); `git add` everything copied/edited; wire per §7.
4. Check → 0.
5. **Re-pull the §6 playbook insertions** into the project's instantiated playbook (nicocares: the
   v2.1 body pasted in `CLAUDE.md`) and bump its `governance-template:` marker to v2.2 — without this
   lever 2 never activates for retrofitted projects, the exact population the problem statement cites.
6. **Marker bump LAST:** set `kickoff-manifest: v1.1` only after steps 1–5 — the bump silences the
   kit's version WARN, which is the only standing signal that the body still predates the ratchet.

The durable copy of this recipe lives in WIRE §4 (§7); executing it in nicocares is OUT of this unit
(separate repo).

## 10 · Acceptance checks (the unit is done when all hold)

1. `manifest-check.test.sh` exits 0 — every §3 scenario red where specified, green after repair,
   explicitly including the cross-mode pair and the true-merge laundering probe.
2. A fresh scaffold (engine §4 flow against a scratch repo with ≥1 commit; the empty-repo clause makes
   its own initial commit) passes `manifest-check.sh` out of the box, including after a follow-up
   commit touching only unwatched files.
3. Placeholder parity on template v1.1 post-normalization: body `{{X}}` set == Customize-block set,
   both directions; and `grep -E '\{\{[A-Z]'` over an INSTANTIATED scratch manifest → empty.
4. Baseline-diff placeholder check: `grep -n '{{'` output over SKILL.md / WIRE-INTO-PROJECT.md /
   README.md captured BEFORE the change == the output after, minus deliberate edits (all three files
   legitimately contain `{{` today — an empty-grep check can never pass).
5. `hooks/agent-cap.test.sh` still exits 0 (no collateral).
6. Engine back-compat: Step 2 search order text unchanged; the gov-repo fallback false-positive probe
   now resolves to "no manifest"; a kickoff against inCMS's prototype manifest skips as unmanaged (no
   nag).
7. Playbook v2.2 diff vs the v2.1 snapshot = exactly the two §6 insertions + header/marker bump.
8. **Lever-1 end-to-end probe:** in a scratch repo, deliberately drift a manifest (move a verify-path
   target + commit a watch-file change), run the engine's Step 2b flow, and assert: manifest repaired,
   `last-audit` re-stamped per the stamp rule, delta line present in the READY card.
9. **Stall review defined where it survives:** the stall signal is git-derivable and squash-proof —
   at each WIRE-Maintenance/kit-re-pull pass, the OWNER (named reader, on that cadence) compares
   manifest BODY-change commits (diffs touching more than the `last-audit` line) against watch-commit
   volume and elapsed time: **≥10 watch-pathspec commits or ≥3 months with zero body growth = stall**
   → the §11 journal-mining revisit triggers. Step 2b's delta lines (with their
   `watch-commits-since-stamp` counter) are supporting color, NOT the data source — they live in
   branch commit messages and READY cards, which squash merges and chat ephemera don't preserve.
10. The memories (`MEMORY.md` index + task note) updated to the landed state.

## 11 · Non-goals (deliberately dropped — do not scope-creep back in)

- **inCMS retrofit** — its prototype is now cleanly handled as an UNMANAGED manifest (no marker, no
  nag); convergence is a separate decision.
- **Journal corpus-mining automation** — the widened DoD trigger list + dated-corrections section are
  the cheap 80%; revisit only on the §10.9 stall review.
- **Semantic truth verification of prose**, **auto-stamping hooks**, **time-based staleness** — as v1;
  the stamp asserts human/agent verification, drift-based only.
- **SessionEnd/Stop nudge hooks** — the DoD + red gate + gate-fence line suffice; revisit on evidence.
- **memory-tree coupling** — `manifest-check` stays standalone; no change to `check-memory-hygiene.sh`.
- **Prose↔block parity gate** (machine-diffing the pointer map against `verify-paths`) — rejected:
  capping `verify-paths` at 2–3 anchors removes the duplication instead of gating it; parsing real
  manifests' backticked cells (ids, remotes, PowerShell invocations) is too fragile.

## 12 · File-by-file change map

| # | File | Change |
|---|---|---|
| 1 | `skills/session-kickoff/MANIFEST-TEMPLATE.md` | v1.1: audit block · §B-intro rewrite · ratchet section · dated-corrections section (never-delete) · traps-accrete note · gate-fence line · placeholder normalization + full Customize enumeration |
| 2 | `skills/session-kickoff/manifest-check.sh` | NEW — the gate (§3), C1–C6 + version WARN + unmanaged NOTE |
| 3 | `skills/session-kickoff/manifest-check.test.sh` | NEW — the §3 scenario suite |
| 4 | `skills/session-kickoff/SKILL.md` | Step 2b (run-don't-reimplement, repair protocol, delta line, commit vehicle) · scaffolding additions incl. empty-repo clause + gate-fence line + git add · fallback template-skip fix (§4) |
| 5 | `parallel-coding-governance.template.md` | two §1 insertions; header v2.2 (§6) |
| 6 | `parallel-coding-governance.template-v-2-1.md` | NEW — snapshot of current v2.1 (§6) |
| 7 | `WIRE-INTO-PROJECT.md` | §4 wiring order incl. `.gitattributes` + `git add` + `fetch-depth: 0` + retrofit recipe home · §6 combined-revert probe + CI probe · Maintenance bullets + stall review (§7) |
| 8 | `README.md` | ratchet sentence in the skills bullet (§7) |
| 9 | *(machine config)* | user-level junction repair (§8) — not a repo change |

## 13 · Review provenance (what the two adversarial passes changed)

**Round 1** — 18 agents, 52 raw → 39 confirmed + 5 critic gaps: C5 same-commit incoherence (2
blockers) → drift check redefined; squash/rebase stamp orphaning → merge-base stamp rule + distinct
C3 remedies; shallow-CI false-green → `fetch-depth: 0` mandate; vacuous/high-churn watch lists → C6 +
breadth WARN + derivation guidance; inline-fallback duplication → engine runs the shipped checker;
gate unwired by default → standing gate-fence line + enforcement floor; scarcity ≠ freezing →
dated-corrections section + re-derive trigger + lever-1/stall acceptance; retrofit missed lever 2 →
playbook re-pull step; template self-contradiction → §B intro rewrite; plus parity, probe, EOL,
location, discovery, opt-out, reconcile, cross-repo, prune-when, version-WARN fixes.

**Round 2** (3 verifiers over the folded revision; git mechanics probed in throwaway repos) — 22
surviving defects: the v2 textual drift check laundered unaudited drift through conflict-free true
merges and any pre-drift mainline stamp → **C5 made topological** (`merge-base --is-ancestor W S`,
verified green/red on all seven probe scenarios, no `W^`); frozen branch merge-base made same-day
re-stamps uncommittable no-ops → **datetime stamps**; no-remote fallback reintroduced squash
orphaning → local-default merge-base fallback; C5s "semantics-identical" false → narrowing stated,
bundle-only message; §6 reconcile self-referential ("stamp the merge from inside the merge") →
two-step post-merge re-stamp; retrofit skipped the v1.1 body deltas and silenced the version WARN by
bumping first → body-deltas-first + marker-last; corrections section deletable-at-birth → never-
delete rule; stall signal unobservable (squash kills commit messages, counter resets) → git-derivable
owner review at Maintenance cadence with concrete thresholds; WIRE probe ended red on the revert →
combined revert+re-stamp commit; plus empty-repo scaffold, untracked-at-adoption `git add`,
check-script-aware fence line, "three lines"→two, §10.10→§10.9, four→six retrofit steps, cross-mode
self-test scenario, lever-2 delta-line home.
