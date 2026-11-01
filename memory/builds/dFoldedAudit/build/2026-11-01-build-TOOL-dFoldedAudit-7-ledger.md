# TOOL-dFoldedAudit-7 — acceptance ledger

**Serves:** journal TOOL-dFoldedAudit-7

The acceptance criteria were observed by this unit's builder through the probes §6 names, over the tree committed at `3e6336b05`; the mirror's criterion was read after `policy.py mirror --write` rendered that commit. No gate, suite or bar ran in this pass. Each `New arm:` line of §7 is the close's to observe RED on its staged break and GREEN restored, and it records them here under a `Pass: none` commit.

**Evidences:** TOOL-dFoldedAudit-7

Fixtures K and N were scratch git repositories under `%TEMP%` on branch `main` with no remote, holding the files §6 lists at those paths.

- AC1 — `python tools/policy/policy.py get review.spec-audit.disposal` — run in this repository with `review.spec-audit.chain-stop` and `review.spec-audit.chain-ceiling` after it, they printed `by-nature`, `own-work` and `4`, each exit 0.
- AC2 — `promote-all` — K committed `.governance/policy.toml` setting the three old values under `[review.spec-audit]`, and the probe printed `promote-all`, `clean-only` and `2`, each exit 0.
- AC3 — `policy: refused` — K's first commit set `disposal = "fold-all"`, and the probe exited 1 printing one line, `policy: refused · .governance/policy.toml:2 · review.spec-audit.disposal: "fold-all" is not one of ["by-nature", "promote-all"]; no valid revision of the file precedes 8bfa6f39`, with no value line.
- AC4 — `no policy kit resolves beside this kit` — in N the probe printed `by-nature`, `own-work` and `4`, each exit 0, and stderr carried this text with the key and value each time.
- AC5 — `SPEC_AUDIT_DISPOSAL_DEFAULT` — with no policy file K's three answers read `by-nature own-work 4`, equal to N's three, which come from this constant and its two siblings.
- AC6 — `python tools/policy/policy.py lists --check` — it printed `policy lists: green · 0 finding(s)` with 263 summary rows against a base carrying 263, no `is a new legacy home` and no row for `review.spec-audit.`; `grep -c '^SPEC_FOLD_CUTOFF=' .unattended.conf tools/unattended/.unattended.conf.example` printed 1 for each file.
- AC7 — `SPEC_FOLD_CUTOFF is declared as 'soon', which is not an ISO date` — K's conf with `SPEC_FOLD_CUTOFF="soon"` made `--version` exit 2 with this text; blank, absent and `"2026-11-02"` each exited 0 printing `unattended 1.111` with the text absent.
- AC8 — `grep -c 'policy.py" get review.spec-audit\.' tools/unattended/unattended.sh` — printed 3, and the `sed` read of `load_driver_conf`'s body counted 0 for `read_spec_audit_switch` over 285 lines holding the cutoff's refusal, so the range reached the loader's end.
- AC9 — `policy: mirror fresh` — before the write `mirror --check` printed `policy: mirror stale · .governance/policy.json · catalogue_blob` and exited 1; after `policy.py mirror --write` over `3e6336b05`, which reported 257 keys, it printed this line and exited 0, and `grep -c '"review.spec-audit\.' .governance/policy.json` printed 3.
- AC10 — `bogus` — K's catalogue widened with `fold-all` let `policy.py get` answer `fold-all` with exit 0, and the probe then exited 1 printing `unattended: review.spec-audit.disposal answered 'fold-all', which is outside the closed set this driver branches on`, with no line that is the value alone; with `bogus` for its key it exited 1 printing a line naming `disposal`, `chain-stop` and `chain-ceiling`, in K and in N.

The reader's third row was also probed, beyond the criteria: a catalogue with the rows removed made it exit 1 printing `review.spec-audit.disposal is not a catalogue key`, so a policy kit older than these rows refuses and takes no default.

The same reader ran at the suite's fixture layout, the driver at `u/` beside the kit's home, as a scratch probe of 38 assertions, all green. Run with `GOV_REMOTE=origin` in the environment, as a push's bar can carry it, 16 of them went red, because a fixture with no remote refuses that name on every read; `run_switch_probe` now clears the ladder and all 38 are green under the same environment.
