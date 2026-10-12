# TOOL-aBriskPreflight-19 — the three inherited reds that read as this build's own are drained, so its landing push can land

**Status:** CLOSED · rev-1 · 2026-10-12 · node a · Tier-1 · base 37200355 · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-12-build-TOOL-aBriskPreflight-19-acceptance-ledger.md](../build/2026-10-12-build-TOOL-aBriskPreflight-19-acceptance-ledger.md) | journal | — |
| [2026-10-12-prompt-TOOL-aBriskPreflight-19-build-brief.md](../prompts/2026-10-12-prompt-TOOL-aBriskPreflight-19-build-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The owner ruled "land". The push boundary lands over a red only when every red leg reads INHERITED
against the remote's tip (`.githooks/gate-env.sh`, `INHERITED_RED=land`). Three legs are red at
origin/main `37200355` on offenders this build did not write, and read OWN or MIXED here only because
this build touches what they compare or what they print. So the landing is refused on other builds'
debt. This unit drains those offenders so the three legs are GREEN, which is strictly better on an
observable the bar measures and makes nothing worse. It was adopted as a blocker between the run and
its own landing (protocol §11).

## 2. Scope (IN)

- **S1** — `install-prefix (shipped surface)`. It reads OWN because this build's diff touches its
  comparator, `tools/check-wiring.sh`. Its only offenders are three kit-path spellings
  aFrugalTurnstile landed: `.githooks/pre-push.test.sh` around lines 2336 and 2339, the loose
  `tools/other-legs.json`, and `tools/unattended/unattended.test.sh` around line 11929, the literal
  `bash tools/run-gates/run-gates.sh`. Each is spelled through a value the suite already derives,
  such as `KIT_REL`, `RUN_GATES_DIR` or `RUN_GATES`, and never through a split literal that only hides
  the token from the scanner. Observed by AC1.
- **S2** — `lexicon naming predicates` and `lexicon wiring`. They read OWN because this build's diff
  touches `.lexicon.conf` (the `log::dark` declaration). `VERB_OFFENDER_PIN` is an EQUALITY at 1063,
  and the tree counts 1067, every one of them inherited from origin/main (this build's own offenders
  are none: `lexicon.py --offenders` at HEAD less the same at `37200355`). Exactly four inherited
  offenders are renamed to a declared verb, chosen from the suite helpers aFrugalTurnstile added to
  `.githooks/pre-push.test.sh` (`decide`, `decide_on`, `stamp`, `pfx_fixture`, `pfx_stamp`,
  `pfx_decide`), each name asked of `lexicon.py --suggest … --as sh.function` first, with every call
  site renamed with it. The pin does not move. Observed by AC2.
- **S3** — `harness arms (fail branches armed or pinned)`. It reads MIXED because this build adds
  waived exit sites, which the leg prints. Its one failure is inherited:
  `tools/run-gates/post-merge.sh:405` has "no POSITIVE assertion naming its own failure text
  ('post-merge: publish FAILED —')". The existing arm in `tools/run-gates/run-gates.evidence.test.sh`
  (around line 1724) asserts a regex prefix. The pass makes it assert the site's whole failure text
  in the form `check-arms.py` grades, or, if no arm can, pins the site in
  `memory/project/unarmed-branches.txt` with a reason, which that file's header allows. Observed by AC3.

## 3. Non-goals (OUT)

- No pin, ceiling or bound moves: `VERB_OFFENDER_PIN` stays 1063, and no waiver row is added where
  an arm can be written.
- Nothing outside the three legs. The held self-test reds have their asks (`TOOL-aBriskPreflight-13` to
  `-18`), and `playbook render wiring` reads INHERITED and lands under the policy.
- No behaviour change: S1 and S3 touch test suites, and S2 renames test helpers. No product file's
  behaviour moves, and no new refusal is added.
- The run-gates kit's version moves once, with the build's re-mint after this unit.

### Edges

none

## 4. Design

S1: each spelling is derived the way the surrounding suite already derives its kit paths (S1's
values exist at the top of each suite). S2: a rename is a whole-word replacement in one file, so
the population the VERBS table certifies loses four offenders and gains none. S3: read
`tools/memory-tree/check-arms.py` for what it accepts as a positive assertion naming a site's
failure text before choosing, and run its predicate over the real tree.

## 5. Production-readiness checklist

Testing: AC1 to AC3 are each the leg's own checker run directly. Rollback: revert the commit. No
security, data or migration surface.

## 6. Acceptance criteria

- **AC1** — When `bash check-install-prefix.sh` from the tool root, the argv the
  `install-prefix (shipped surface)` row of the gate manifest names, runs at the pass commit, it
  exits 0 and lists no kit-path spelling.
  Red when: any of the three sites still spells a kit path, or a split literal hides it.
- **AC2** — When `lexicon.py --check` runs at the pass commit, it exits 0 with
  `offenders=1063`, and `adopt-lexicon.sh --check` exits 0.
  Red when: the count is not exactly 1063, or a renamed helper keeps a call site under its old name
  (the suite's `bash -n` and a `grep -w` of each old name print nothing).
- **AC3** — When `check-arms.py --check` runs at the pass commit, it exits 0.
  Red when: the `post-merge.sh` site is still reported, or a waiver row was added where an arm could
  assert the whole text.

## 7. Gates

`install-prefix (shipped surface)` · `lexicon naming predicates` · `lexicon wiring` · `harness arms (fail branches armed or pinned)` · `memory hygiene`

The pass verifies with AC1 to AC3 only; the bar runs once, at the close.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-12 · initial draft, authored by the main loop after the owner's "land", adopted as
  a blocker between the run and its own landing.

## 10. Reuse audit

No code mechanism is added; every change runs an existing checker's own rule over existing files.
The derived values S1 names are the suites' own (`KIT_REL`, `RUN_GATES_DIR`, `RUN_GATES` in
`.githooks/pre-push.test.sh`), and S3's arm extends the existing one in
`tools/run-gates/run-gates.evidence.test.sh`.

Recall terms used: none; the offenders are located by each leg's own output at the close (`close2`),
and the attribution rule by `tools/run-gates/run-gates.sh`'s RULE 3 and RULE 5 comment.
