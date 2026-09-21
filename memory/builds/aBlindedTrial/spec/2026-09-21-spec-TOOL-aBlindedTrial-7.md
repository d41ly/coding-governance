# TOOL-aBlindedTrial-7 — a project-wide spec-audit default, declared once in the conf and read at BASE

**Status:** INPROGRESS · rev-2 · 2026-09-21 · node a · Tier-2 · base 0e61932d · streams tooling · order 1 · ratified 2026-09-21

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round1.md](../reviews/2026-09-21-review-TOOL-aBlindedTrial-7-8-kick1-closing-diff-round1.md) | diff-review | TOOL-aBlindedTrial-8 KICK-aBlindedTrial-1 |

<!-- /gen:spec-records -->

## 1. Goal

An adopter who wants the pre-code spec audit on every build declares it once: `SPEC_AUDIT_DEFAULT="<date>"`
in `.unattended.conf`. The driver reads it at the pinned BASE beside the README's `spec-audit:` key and
treats an undeclared README as declared; the fan-out hook honours the same key from the worktree conf.
Blank or absent keeps today's per-build opt-in, so no adopter's behaviour moves until they write the
line.

## 2. Scope (IN)

- S1 — `check_authorization()` (`unattended.sh:1460-1516`): when the README front matter carries NO
  `spec-audit=` line at all, read `.unattended.conf` at BASE (`GIT show "$base:.unattended.conf"`, the
  `:1562` idiom), source the blob in a subshell and take `SPEC_AUDIT_DEFAULT`; a `<date>` value sets
  `AUTH_SPEC_AUDIT` with a new global `AUTH_SPEC_AUDIT_FROM=project`; a non-date is a new `fail 54`; an
  absent blob or blank key falls through as undeclared; a blob whose evaluation does not reach the end
  — a `return`, an `exit`, an unbound reference, a syntax error — is `fail 55`, never read as absent
  (rev-2). A README key, even malformed, wins (`fail 52` unchanged). Observed by AC1, AC2, AC3.
- S2 — `print_spec_audit_line` gains a third spelling for `AUTH_SPEC_AUDIT_FROM=project`: `unattended:
  spec-audit — opted in by project default SPEC_AUDIT_DEFAULT: <date>`; the two existing spellings keep
  their bytes. The `fail 53` sentence and the not-owed `DOD_OUT` name both sources; the driver suite's
  verbatim assertion at `:5645` moves in the same commit. Observed by AC1, AC4.
- S3 — the key exists in four carriers in ONE commit or check 22 reds: `SPEC_AUDIT_DEFAULT=""` in the
  driver's contiguous init block (`unattended.sh:339`, appended to that line), in `.unattended.conf`
  (blank — the trial ruled the audit bought nothing here), in `.unattended.conf.example` (blank), and a
  §8 row in `PROTOCOL.template.md` rendered into `memory/guides/UNATTENDED-PROTOCOL.md`. Observed by
  AC5.
- S4 — `agent-cap.js` rule 0: when the README carries no key, read `<args.repo>/.unattended.conf` from
  the worktree with a last-wins parse accepting both quote styles and a trailing comment; a `<date>`
  admits, a non-date denies by name, a missing file is no default. The asymmetry (hook worktree,
  driver BASE) is stated in the hook header and `tools/hooks/README.md`. Observed by AC6, AC7.
- S5 — prose: the MUST-by-default comment (`unattended.sh:466-469`) gains the project-default clause;
  `SKILL.template.md` and the protocol name the key beside the README key; the `unattended` dossier;
  the build method's M4 **When** sentence (`BUILD-METHOD.template.md` and its render), which the kickoff
  engine greps to decide whether the question is worth asking (rev-2). Observed by AC8.
- S6 — versions: `KIT_UNATTENDED_VERSION` 1.26 → 1.27 in every paired carrier, `agent-cap@` 1.16 →
  1.17 in both halves. Observed by AC8.

## 3. Non-goals (OUT)

- No per-build opt-OUT (`spec-audit: none`) under a project default; the default is for adopters who
  want every build audited, and a build that should not be is a conf change.
- No allow-list edit in `check-unattended.sh`: no leg reads the key; the driver sources the conf.
- No change to the harness: the caller still passes `specAudit` from the preflight line.
- Test floors in the driver suite are not raised (`-ge` floors, green).

### Edges

- **consumes-from** external — `TOOL-aBlindedTrial-2`'s key grammar and `AUTH_SPEC_AUDIT`, landed at
  `0e61932d`; this unit widens where the value comes from, never its shape.

## 4. Design

### Data model

`SPEC_AUDIT_DEFAULT="<date>"` — the day the project ruled audits on. Read at BASE by the driver so a run
cannot blank it to escape (the class the MUST-by-default ruling names); read from the worktree by the
hook, which guards the attended session. Precedence: README key present (any value) → the README
decides; README silent → the conf decides; both silent → not owed.

### Inventory

- `AUTH_SPEC_AUDIT_FROM` — `readme` | `project`, set beside `AUTH_SPEC_AUDIT`.
- `fail 54` — a non-date `SPEC_AUDIT_DEFAULT` at BASE, with a positive `hit` arm.
- `readSpecAuditDefault(bytes)` in `agent-cap.js` — leads with `read`; returns the date, `null`, or a
  deny-shaped error the caller renders.

### Files touched (estimate)

`tools/unattended/unattended.sh` · `tools/unattended/unattended.test.sh` · `.unattended.conf` ·
`tools/unattended/.unattended.conf.example` · `tools/unattended/PROTOCOL.template.md` ·
`memory/guides/UNATTENDED-PROTOCOL.md` · `tools/unattended/SKILL.template.md` ·
`.claude/skills/unattended/SKILL.md` · every `KIT_UNATTENDED_VERSION` carrier · `tools/hooks/agent-cap.js` ·
`tools/hooks/scratch-guard.js` (marker) · `tools/hooks/agent-cap.test.sh` · `tools/hooks/README.md` ·
`memory/map/features/unattended.md` · `memory/map/features/agent-cap.md`.

### Alternatives rejected

- A sed pipeline over the BASE conf blob: `KEY='v'`, `KEY="v" # note` and last-wins each read
  differently from the shell — the `two-readers-of-one-config-one-re-derived` class. Sourcing in a
  subshell is the file's own language.
- Letting the default override a malformed README key: a typo in the README would fall back silently,
  which is the read-as-absent opt-out `fail 52` exists to refuse.

## 5. Production-readiness checklist

- security — the BASE read is what binds; the worktree read guards a session where the owner is present
- perf / scale — one `GIT show` more per preflight and close
- error / empty / loading states — non-date → `fail 54`; absent blob or blank → undeclared; an `exit`
  inside the BASE conf ends the subshell before the read and reads as no default, stated in the comment
- observability — the third preflight spelling; `--status` unchanged
- risks — check 22's four-carrier lockstep; the verbatim `fail 53` assertion; the `mkconf` positional
  count in the fixture
- testing — driver slice arms, hook arms; the driver suite is not run whole
- migration — none; absent and blank both mean today's behaviour
- user docs — the Skill and protocol renders

## 6. Acceptance criteria

- **AC1** — When `.unattended.conf` at BASE declares `SPEC_AUDIT_DEFAULT="2026-09-21"` and the build
  README carries no key, `--preflight` prints `opted in by project default SPEC_AUDIT_DEFAULT: 2026-09-21`
  and `--status` shows the fact `spec-audit 2026-09-21`.
  Red when: the line is absent, or the fact is empty.
- **AC2** — When the conf default is declared on the run branch only and not at BASE, `--preflight`
  prints `not owed (opt-in)`.
  Red when: a working-copy conf opts a run in.
- **AC3** — When the conf declares `SPEC_AUDIT_DEFAULT="later"` at BASE, `--preflight` refuses with the
  `fail 54` text; when the README carries `spec-audit: later` beside a valid default, `fail 52` fires.
  Red when: a non-date default reads as absent, or a malformed README key falls back to the default.
- **AC4** — When the default is declared at BASE, a CLOSED unit has no `spec-audit` record and `--close`
  runs, the close blocks naming the missing record.
  Red when: a project-declared build closes unaudited.
- **AC5** — When `grep -c SPEC_AUDIT_DEFAULT` runs over `unattended.sh`, `.unattended.conf`,
  `.unattended.conf.example`, `PROTOCOL.template.md` and `UNATTENDED-PROTOCOL.md`, every count is ≥ 1
  and `bash tools/unattended/check-unattended.sh` exits 0.
  Red when: check 22 names the key as undocumented or phantom.
- **AC6** — When `node tools/hooks/agent-cap.js` reads a spec-audit payload for an undeclared README
  whose repo root holds `.unattended.conf` with `SPEC_AUDIT_DEFAULT="2026-09-21"`, it exits 0; with
  `SPEC_AUDIT_DEFAULT='2026-09-21' # note` it exits 0; with no conf file it exits 2.
  Red when: a declared project is denied, or a missing conf admits.
- **AC7** — When the conf declares `SPEC_AUDIT_DEFAULT="later"`, `agent-cap.js` exits 2 with a message
  naming `SPEC_AUDIT_DEFAULT`.
  Red when: a non-date default reads as absent at the hook.
- **AC8** — When `bash tools/check-kit-versions.sh` runs it exits 0, every `unattended@` marker reads
  1.27 and both `agent-cap@` halves read 1.17.
  Red when: a carrier is left behind.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `harness arms (fail branches armed or pinned)` · `agent-cap self-test` · `scratch-guard self-test` · `verifier fan-out self-test` · `review-join self-test` · `hook destinations self-test` · `check-wiring self-test` · `recall floor` · `recall floor arms` · `kit version markers` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `kickoff-manifest ratchet`

New arm: `tools/unattended/unattended.test.sh` · the `specs-audited` block, conf default at BASE then on the branch only · none
New arm: `tools/hooks/agent-cap.test.sh` · a conf beside the fixture README, dated then malformed then absent · none

## 8. Open questions

- **F1 — should gov's own conf declare a date.** RESOLVED (agent, 2026-09-21, delegated): blank. The
  trial this build sits in measured no quality the audit bought on this repo; declaring it here would
  reverse the ruling the previous units landed.

## 9. Revision log

- rev-1 · 2026-09-21 · initial draft from the scout of the driver, conf carriers and hook at 0e61932d.
- rev-2 · 2026-09-21 · §7 · S1 · S5 · closing diff review round 1 folded. R6: the leg line names every
  leg the §4 files-touched trips under the guards join at the fold — the four `tools/hooks/` self-tests,
  `check-wiring self-test` (`.claude/`) and the two `memory/` recall legs. R2: S1 states `fail 55` for a
  BASE conf whose evaluation does not finish; the sanctioned `exit` case of rev-1's comment is that
  refusal now. R5: S5 lists the build method as a carrier. R8, R9, R10 are wording in the hook header,
  the three conf carriers and the unevidenced-audit sentence; no criterion changed.

## 10. Reuse audit

Probe: `tools/codebase-map/reuse_lookup.py "read a project conf key at the pinned base as a second
source for a run fact"` returned no candidate in the layer this unit edits — it reports `unscanned
layers: .sh` — so the seam was found by reading the source. The seam is `check_authorization()`'s own
second-file-at-BASE read (`_pb=$(GIT show "$base:$AUTH_PLAYBOOK")`, `:1562`) and the `AUTH_SPEC_AUDIT`
path unit 2 built; the hook reuses `readFrontMatterKey`'s caller shape. Recall terms used: spec-audit
opt-in project default conf key BASE blob source subshell fail 52 fail 54 preflight line hook worktree
check 22.
