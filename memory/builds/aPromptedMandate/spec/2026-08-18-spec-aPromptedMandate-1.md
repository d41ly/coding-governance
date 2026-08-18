# TOOL-aPromptedMandate-1 — the prompt-mode declaration, and where it is carried

**Status:** SPECCED · rev-2 · 2026-08-18 · node a · Tier-2 · base 6517579f · streams tooling

## 1. Goal

Make a run started from the owner's prose distinguishable, after the fact and by machine, from a run
started on a slug someone already specced. Without that bit nothing downstream can be scoped to the
mode, and the owner cannot tell which discipline a landed run was under.

## 2. Scope (IN)

- **S1** — the mode is declared as a front-matter key in the build README the run authors:
  `authorized-by: prompt`. Absent means slug mode, which is every build in the tree today.
- **S2** — the owner's verbatim prose, and every clarification taken at the one owner turn, are
  written into that same README under an authored heading before the anchor push.
- **S3** — `--preflight` reads the key AT THE PINNED BASE, through the blob it already fetches in
  `check_authorization`, and records `mode: prompt` (or `mode: slug`) into the run-state file's Run
  facts block beside `anchor-kind:`.
- **S4** — the leg asserts the recorded `mode:` against the same blob at the recorded BASE — a second
  opinion, derived independently, in the shape check 13 already uses.
- **S5** — a refusal when `authorized-by:` carries any value outside the closed set
  `prompt` / `slug`.
- **S6** — protocol §1 gains one sentence saying the mode is a RECORD and not a verdict, in BOTH
  copies (`tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md`), which
  leg check 10 byte-compares. Added at rev-2: §5 already committed to this artifact and §2 never
  scoped it, so nothing observed it.

## 3. Non-goals (OUT)

- **No new argv flag on the driver.** A `--from-prompt` flag was considered and cut: the build README
  is already the authorization carrier, already at BASE, already parsed by both the driver and the
  leg, and §1 already says only its SHAPE is checked. A second carrier for one bit is the
  two-answers-to-one-question class.
- **No change to `check_authorization`'s verdict, `resolve_base`, the anchor observation, or leg
  check 13.** The reproduction record establishes none is needed.
- **No claim that the mode bit is unforgeable.** Protocol §9's reduction holds unchanged; this is a
  RECORD, and the build states it as one.
- Follow-up not taken here: teaching `--status` to print the mode.

## 4. Design

### Data model

One key in the build README's existing front matter:

```
authorized-by: prompt
```

Read by the awk that already extracts `slug:` from the BASE blob in `check_authorization` — but that
awk **must change shape**, and rev-1's "one more arm, no second parse" was unimplementable. The
existing program is `/^slug:/ { …; print; exit }`, and every README in the tree orders `slug:` first,
so a second arm below it never runs; putting the new arm first makes ITS `exit` starve `fmslug` and
trips the fail-20 slug mismatch instead. The fold: **remove the `exit`, print both keys KEY-TAGGED in
one pass, and let the front-matter close terminate the scan** — which it already does, on its own
line. One read, one program, two answers.

### Why the README and not the run-state file

The run-state file is written by the run, at preflight, with no anchor behind it. The build README is
at BASE — under the branch anchor, the tip the remote advertises. The prose and the clarifications
carried there are therefore provably older than the commit that authorizes the run, which is the
strongest statement available about "the owner turn happened before the run started" and is strictly
better than a flag on argv, which is contemporaneous with the run.

### Flows

`--preflight` already fetches the BASE blob once. It gains: extract `authorized-by:` through the
re-shaped awk above, validate against the closed set, refuse outside it, and write `mode:` into Run
facts. The leg re-derives from its own read of the same blob and compares.

The value returns through a GLOBAL out-parameter with the return code as the verdict, which is this
file's established idiom — `observe_anchor`, `resolve_base`, `trusted_base` and `dod_met` all do it.
§3's ban is on changing `check_authorization`'s VERDICT, not on changing the function.

### Files touched (estimate)

`tools/unattended/unattended.sh` (the awk, the closed-set refusal, the Run-facts write) ·
`tools/unattended/check-unattended.sh` (the second opinion) · `tools/unattended/PROTOCOL.template.md`
and `memory/guides/UNATTENDED-PROTOCOL.md` (S6, byte-compared by leg check 10, so both or neither) ·
`tools/unattended/unattended.test.sh` and `tools/unattended/check-unattended.test.sh`.

### Alternatives rejected

- **A `--from-prompt <path>` flag.** Cut per §3.
- **Deriving the mode from `anchor-kind: run-branch`.** Refuted: a slug-mode run on an unlanded build
  folder also gets `run-branch`, so the two are not the same question.
- **A `.unattended.conf` key.** The mode is per-RUN, not per-project.

## 5. Production-readiness checklist

- security — the mode bit is run-writable like every other local input; §9's boundary is unchanged
  and §1 gains a sentence saying the bit is a record, not a verdict
- perf / scale — N/A, one more awk arm over a blob already read
- a11y — N/A
- i18n — N/A
- error / empty / loading states — absent key is slug mode, the majority case; malformed value is a
  named refusal, not a default
- observability — the value lands in Run facts, which the wrap-up derives from
- risks — the closed-set refusal must not fire on a build README written before this unit; absence is
  the legal slug case and is arm'd as such
- testing + left-shift gates — driver arms, a leg arm, and unit 6's cross-component arm
- migration / rollback — none; every existing README is slug mode by absence
- user docs — protocol §1 and the rendered Skill

## 6. Acceptance criteria

- **AC1** — When a build README at BASE carries `authorized-by: prompt`, `--preflight` writes
  `mode: prompt` into `RUN.md`'s Run facts and exits 0.
- **AC2** — When the key is absent, `--preflight` writes `mode: slug` and exits 0, over a fixture
  built from an existing build README with no edit.
- **AC2b** — When a build README at BASE orders `authorized-by: prompt` AFTER `slug:`, `--preflight`
  still writes `mode: prompt` — the arm that discriminates a working reader from a dead one, since
  AC1 and AC2 together are both satisfied by an awk that returns nothing.
- **AC3** — When the key carries a value outside the closed set, `--preflight` refuses by name and
  `git hash-object` on the run-state file is unchanged.
- **AC4** — When a run-state file records a `mode:` the build README at its recorded BASE does not
  declare, `check-unattended.sh` fails by name.
- **AC5** — When `unattended.test.sh` runs, its printed assertion count has grown, and
  `bash tools/check-testsuite-counts.sh` stays green.
- **AC6** — When `bash tools/unattended/check-unattended.sh` runs, leg check 10 finds
  `tools/unattended/PROTOCOL.template.md` and `memory/guides/UNATTENDED-PROTOCOL.md` byte-identical
  with S6's sentence in both.

## 7. Gates

`bash tools/unattended/unattended.test.sh` · `bash tools/unattended/check-unattended.test.sh` ·
`bash tools/unattended/check-unattended.sh` · `bash tools/unattended/adopt-unattended.sh --check` ·
`bash tools/check-testsuite-counts.sh` · `python tools/codebase-map/test_codebase_map.py` ·
`bash tools/run-gates.sh`

## 8. Open questions

none — the forks below are RESOLVED.

- **Carrier for the mode bit** — RESOLVED (agent, 2026-08-18): the build README's front matter, per
  §4's provenance argument. The argv-flag option was discarded by veto 2 (a new public surface for
  one bit) and by the two-answers-to-one-question class.

## 9. Revision log

- rev-1 · 2026-08-18 · initial draft.
- rev-2 · 2026-08-18 · folded the M4 spec audit. The awk was unimplementable as stated (ids 46);
  S6 and its Files-touched sub-head added for the protocol pair §5 already committed to (id 25);
  AC2b added because AC1 and AC2 both pass over a dead reader.

## 10. Reuse audit

`reuse_lookup.py "start an unattended run from an owner's natural-language prompt rather than a
committed build slug"` returned the `unattended` affordance seam and `UNATTENDED-PROTOCOL.md`; no
symbol-level seam. Recall terms: `unattended mandate authorization build folder preflight anchor slug
owner prompt self-authorization AskUserQuestion directive waiver` — which surfaced
`TOOL-aStandingWrit-1` (the move to build-folder authorization) and protocol §1's cost list, both of
which this unit is built on rather than around.

**The seam extended** is `check_authorization` in `tools/unattended/unattended.sh` — it already
fetches the BASE blob, and leg check 13 already re-derives the same blob independently for its second
opinion. No new READ of the build README is introduced by this unit; the existing awk is re-shaped to
answer two questions instead of one, per §4. Rev-1 said "one arm inside an existing parse" and that
was refuted against source — the parse exits on its first hit.
