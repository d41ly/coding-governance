# Brief — dRenderedAnchor: unit 6's closing-review findings, and the build's close

**Serves:** research TOOL-dRenderedAnchor-7

## The prompt

> Unit 7, no review (Recommended)

## The brief

### Goal
Close every confirmed finding of unit 6's closing diff review as one batch unit, the build's last: a junction-installed kit renders its own install's harness paths, a receipt-held path cannot reach a JS literal or shell command without the renderers' charset guard, the self-re-run never degrades silently, and every new refusal and the re-run's exit pass-back have an arm. No review round follows this unit.

### Items
1. H1 — the canonical `derive_kit_paths` in `tools/lib/render-doc.sh` uses `pathlib.Path(sys.argv[1]).absolute()`, as `resolve_kit_dir` does, not `.resolve()`; every inline copy re-synced byte-identical through the existing parity row; an arm with a junction kit dir under a prefix differing from its target's, RED with `.resolve()`.
2. M1 — after each derivation, both renderers refuse with exit 2 any `{{TOOL_ROOT}}<home>/<file>` line of `KIT_PATHS` whose path holds a character outside `[A-Za-z0-9._/+@-]`, the guard each script already applies to its own substituted values; an arm, RED without the check.
3. L1 — `tools/workflows/README.md`, the comment in `tools/workflows/check-protocol-parity.test.sh` and unit 6's record state that `--tracked-only` re-runs once after recreating a tracked harness deleted from the worktree. Unit 6's spec is CLOSED; this unit's spec and ledger carry the correction.
4. L2 — when the derivations differ and the re-run is suppressed, the parity script prints one line naming `PROTOCOL_PARITY_REPASS` and exits non-zero; the guard tests `"${PROTOCOL_PARITY_REPASS:-}" != 1`.
5. L3 — RA6-1 grades the render mode's re-run announcement and the exit status passed back from the re-run, by the review's corrected fix.
6. L4 — an arm with stub `python3`, `python` and `py` launchers that exit 9009 and `GOV_PYTHON` unset: the parity script and `adopt-unattended.sh --check` each exit 2 with the `resolve_python` reason, RED with `|| exit 2` replaced by `|| :`.

### Acceptance
Each item's fix as the review record states it, with the skeptic's corrected fix where it judged the finder's UNSOUND. Each new arm observed RED on its staged break, then GREEN, by the main loop. All four shell-hygiene legs stay green with no registry row added or raised. Gov's own renders stay byte-identical.

### Gates
The spec's §7 derives them; at least review-protocol parity (kit vs dogfood) · python resolver (behaviour + inline parity + idiom ban) · the unattended-build self-test · the unattended wiring leg · the shell hygiene legs · memory hygiene; then the full bar once.

### Non-goals
`roles_lib.resolve_harness_path`'s probe order; `render_doc`'s unanchored loop; the four inherited reds; running the unattended kit's own self-test suites (owner rule); any further review round (owner, 2026-10-19).

### Limitations
New shell lines take the no-fork forms. Kit versions move through the lander's `mint`. Merge and push wait for the owner's explicit ask.

### Reuse
The review record names each fix and the skeptic's verdict: `memory/builds/dRenderedAnchor/reviews/2026-10-19-review-TOOL-dRenderedAnchor-6-closing-diff-round1.md`. The charset guard already in `tools/workflows/check-protocol-parity.test.sh` (around lines 457-466) and `tools/unattended/adopt-unattended.sh` (around lines 535 and 590).

## Drawn from the session

> Unit 7, no review (Recommended)
— owner, after unit 6's closing review

## Owner confirmation

Asked: Unit 6's review: 1 high … 1 medium … 4 lows … How do we close?
Answer: Unit 7, no review (Recommended)
