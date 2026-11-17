# TOOL-dDeclaredLoop-77 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-77

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node `d`
(win32), at rev-3 of the spec, over the working tree: the three plants this pass adds, run alone by
`--fixture --plant`, standing in for the `loop position fixtures` leg; `failed-fetch`, `quiet-remote` and
`fetch-other-branch` run alone the same way, each still `held`, standing in for that leg's reading of the
sweep's local-path population; a `python -c` probe of `derive_fetch_url` over the tabled URLs and a
credential URL; the docs leg's `--fingerprints`, which still prints the `script:tools/loop/position.py`
anchor at `8d078234`; and `grep -c` probes. A `python -c` probe that put TOOL-dDeclaredLoop-74's body back
in place of `derive_fetch_url` printed `scp-remote` MISSED, its tracking ref read `from reflog` beside
`read — FETCH_HEAD · skipped — no line for main of origin`, and `url-forms` MISSED on the scp, scheme and
doubled-slash pairs, exit 1 each. The sweep re-run at this pass's base held its design claims:
`derive_fetch_url` and `check_fetch_head` as 74 built them, the restaged `stale-remote` scratch, the one
`from loop_witness import` line naming `read_clean_env`, the lexicon offender pin at 1215 PINNED,
`SHARED_RECORDS` naming the decision log and the readme contract, neither written, no row of this spec in
the positional registry, and neither edited path on the kickoff watch line. Its stale figures are
deviation 772.

Observed on the scratch here, which section 4 left UNVERIFIED: a fetch over the scp-form and the
`ssh://user@` shim exits 0 and writes a `FETCH_HEAD` line the kept reading reads, and a fetch failing at
connect over https with a password leaves the file empty, its skip entry `empty`. Still UNVERIFIED and
owed to the close: git's user-part rule read against git's source, the https case over a live network
remote, and that nothing listens on the plant's connect port on every host.

Owed to the close: every leg section 7 names, the `loop position fixtures` leg among them, and the re-price
of that leg's budget row from the close's timed reading. Owed RED-first, on the one `New arm:` line: the
`tools/loop/position.py` arm (`scp-remote`, `ssh-userinfo-remote` and `url-forms`, staged against 74's
`derive_fetch_url`).

**Evidences:** TOOL-dDeclaredLoop-77
- AC1 — `scp-remote` — `python position.py --fixture --plant scp-remote` printed the ref's line ending `· from FETCH_HEAD`, no line holding `skipped —`, the answer `act`, and `position: fixture · scp-remote · held`, exit 0.
- AC2 — `ssh-userinfo-remote` — that plant printed the ref's line ending `· from FETCH_HEAD`, the answer `act`, and `position: fixture · ssh-userinfo-remote · held`, exit 0.
- AC3 — `url-forms` — that plant printed six `position: fixture · url-forms ·` rows, the first four `equal` and the last two `unequal`, as tabled, then `position: fixture · url-forms · held`, exit 0.
- AC4 — `SECRET` — `python position.py --fixture --plant url-forms | grep -c SECRET` printed 0, and the plant printed `read — FETCH_HEAD · skipped — empty` with the answer `stale-remote`; the plant's own check reads `json.dumps` of the position for the word.
- AC5 — `user part` — in `help/`, `grep -c "url-forms" loop.md` printed 1 and `grep -c "user part" loop.md` printed 2; in `tools/loop/`, `grep -c "insteadOf" position.py` and `grep -c "spelled otherwise" position.py` each printed 1.
