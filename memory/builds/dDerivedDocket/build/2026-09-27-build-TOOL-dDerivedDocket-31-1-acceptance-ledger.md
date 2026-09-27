# TOOL-dDerivedDocket-31 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-31

Section 8 has a regular shape now, forward-only. From `FORK_ITEM_CUTOFF` an F-item opens on a
column-0 bullet whose bold label starts with the fork id, or on an F-id sub-head, and spans every line
up to the next one. Each span carries its own mark, with code spans and double-quoted spans removed
first. The hygiene engine grades that at a terminal status on either tier, and reds a Tier-2 section
of any other shape at any status and under `--staged`. `plan_state` takes the cutoff as its second
argument, and all six call sites pass it: four in the driver and two in the pass-order leg. Each
caller reads the one declaration through `read_fork_cutoff` in the unattended library, as text.
A spelling that reader does not model is refused, check 86 in the driver and exit 2 in the leg,
never resolved blank. BUILD-METHOD's M6 head now binds delegated passes and names the inline-author
exception. The §B kickoff bullet says the same, and `memory/DECISIONS.md` carries the ruling.

The spec went to rev-6 before the code. The hygiene section-8 block runs for both tiers, which S2
now says. The preflight spec-audit line was a fourth driver caller, and S5 now names it. AC13's
fixture half is amended, because three of its four callers act on MISSING and THIN alone.

AC8's figure, DERIVED at this pass: the newest tracked spec filename date at `c60e3109` is
2026-09-22, found with `git ls-files` over the spec folders. So gov declares
`FORK_ITEM_CUTOFF="2026-09-23"`, which is to be re-derived at landing.

No merge bar, no gate leg and no `*.test.sh` suite ran in this pass. The engine and the sliced
classifier ran directly over scratch fixtures. Every marker-contract case the harness now tables was
staged there, pre- and post-cutoff, and the two readers agreed on every row. With the key blank or
absent, both readers graded every post-cutoff row exactly as the section-wide reading does. The
driver's `--plan` and the pass-order leg ran in a scratch build. The contract-harness criteria (AC1,
AC2, AC3, AC4, AC5, AC7, AC13's count, AC14, AC15) are owed to the post-build bar, and so are AC8,
the new hygiene-suite arm, the driver-suite arm, and the ratchet half of AC12.

**Evidences:** TOOL-dDerivedDocket-31
- AC6 — `plan_state` — in a scratch fixture repo, the engine's `--staged` run named a live Tier-2 spec
  dated 2026-09-20 whose §8 opens with a bullet before F1 (`§8 is not F-item shaped`), and the
  sliced `plan_state` printed FORKED for the same bytes; dated 2026-09-01, or with the key blank,
  the engine stayed silent
- AC9 — `bash tools/memory-tree/kit-dogfood-parity.test.sh --check` — exit 0, 4 pairs agree after
  `--render`; the F-item grammar and the section-reading sentence sit in `memory/TEMPLATE-SPEC.md`
  where the fork-format unit moved M3's paragraph, check 12 in `memory/HYGIENE.md` carries the
  cutoff, and `memory/guides/BUILD-METHOD.md` carries the M6 head
- AC10 — `wc -c < memory/guides/BUILD-METHOD.md` — 27268 bytes and 349 lines before the edit,
  27264 bytes and 349 lines after, within the declared 27648 bytes and 350 lines; M6's head names
  delegated passes and the inline-author exception, and M3 kept its one pointer line
- AC11 — `python tools/memory-recall/query.py` — asked why an inline author may sequence disjoint
  passes, with M6 and inline-author terms, it ranked the new row first; the row names D12-i10 and
  TOOL-aHoistedPass-10
- AC12 — `wc -c < memory/guides/SESSION-KICKOFF.md` — 24451 bytes at the parent and 24432 after;
  the §B bullet now says M6 binds delegated passes, and `last-audit` is re-stamped in this commit
- AC13 — amended rev-6 — only `--plan` can report FORKED; `--dispatch`, the build-complete term and
  the pass-order leg act on MISSING and THIN alone, so their half is the call-site count. In a
  scratch build `--plan` printed `next: ARCH-tP-1 (FORKED)` for an unmarked F2 below a marked F1
