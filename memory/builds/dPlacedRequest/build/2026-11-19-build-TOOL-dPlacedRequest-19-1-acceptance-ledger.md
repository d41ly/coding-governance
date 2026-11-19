# TOOL-dPlacedRequest-19 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-19

The unit was built from its spec at rev-7 (PINNED) on base `689ef0382`. The loop kit gains
`tools/loop/request.py`, whose `tools/loop/request.py#derive_request_content_key` keys a request through the
memory-tree kit's `tools/memory-tree/row_grammar.py#derive_content_key`, found by `read_memory_tree` in
`tools/loop/loop_lib.py`, and whose `key` verb reads the file through
`tools/loop/request.py#read_request_text`, strict `utf-8-sig`. The driver gains the verb `--request`,
`tools/unattended/unattended.sh#write_request_record`, the consent predicate
`tools/unattended/unattended.sh#check_request_consent` and the bounded existence read
`tools/unattended/unattended.sh#check_request_recorded`; `tools/unattended/unattended.sh#derive_lease_ref`
gains the kind `request` and reserves the slug; the awk tail classifier of
`tools/unattended/unattended.sh#read_claims`, the `case` of `tools/unattended/unattended.sh#derive_claim_keys`
and the `check_cross_run_overlap` call of `tools/unattended/unattended.sh#run_lease_verb` learn the kind.
The claim read's refspecs are unchanged. No `fail` call site joined the driver, so it stays at its refusal
ceiling.

The spec's citations were resolved by symbol before the first edit: `build_gov_commit` and `write_gov_ref`
in the `gov_ref_sh` block, the lease grammar's builder, the default arm of `run_lease_verb` writing
`slug: -` for a non-build kind, `branch_tip_quiet`'s `ls-remote --exit-code` reading rc 2 as "answered,
no such ref", and the five registries `git grep -n "loop claims fixtures"` names outside build records.

No gate, suite or bar ran in this pass. The driver criteria were observed by a probe script in the run's
scratch directory over a fixture under the node's short temp path: a bare origin, clone A as user
`daily-agent` (fleet tag `a`) under session `sA`, clone B as user `agent5` (fleet tag `b`) under session
`sB`, `RUN_CLAIMS="on"`, and a request file carrying `zq-request-marker-7`. The module criteria were
observed by its own CLI over files in that scratch directory, each plant run one at a time by
`--fixture --plant`, since a role agent runs no `--selftest`.

**Evidences:** TOOL-dPlacedRequest-19
- AC1 — `request.py --fixture --plant normalised-pair` printed one key for `Fix the lander push on
  2026-11-19` and `  fix   THE<tab>lander push on`, `ef0538c532f9` (DERIVED) twice, `held`;
  `--plant empty-refused` printed `request — refused: … the request is empty once normalised`, exit 2
  (PINNED), `held`; `key` over an empty file exited 2 (PINNED) the same way.
- AC2 — clone A's `--request req.md` printed `request — 89d77323e6ca · recorded
  refs/gov/requests/89d77323e6ca` (DERIVED key), exit 0 (PINNED); the record's message was
  `gov-request <key>`, a blank line and the three lines `content-key`, `fleet-tag: a` and `session: sA`,
  with no parent; `git -C <bare> cat-file --batch-all-objects --batch | grep -c zq-request-marker-7`
  printed 0 (PINNED); `cmp` of `req.md` against `<git-common-dir>/requests/<key>.md` was silent, and the
  `.typed` file held the one line `sA`.
- AC3 — a second `--request req.md` printed `request — <key> · already recorded`, exit 0 (PINNED), the
  ref's sha unchanged; as user `nobody` the verb printed `not written · this node has no row in
  fleet.toml`, exit 2 (PINNED), the origin holding 0 (PINNED) governance refs and clone A no `requests/`
  directory, so the refusal preceded every write.
- AC4 — clone B's `--lease acquire request <key>` printed `lease — request/<key> · create · epoch 1`
  (PINNED), exit 0 (PINNED), the record reading `kind: request`, `slug: -`, `fleet-tag: b`, `session: sB`;
  clone A's acquisition printed `lease refused — live-holder · request/<key> · node b`, exit 1 (PINNED);
  `acquire request 0123456789ab` printed `lease refused — no-record`, exit 1 (PINNED), and the origin held
  no such lease; `acquire build request` printed `the slug request is reserved`, exit 2 (PINNED);
  `acquire request ABC` exited 2 (PINNED) naming the twelve-hex key; clone A's `--claims` printed the row
  `request/<key>`, `b`, `live`, verdict `live`, and `--claims --with-key` keyed it `k1:?…`, `runstate=?`;
  in clone B `git for-each-ref refs/gov/` held 0 (PINNED) refs naming `requests/` and its
  `gov-feed.log` 0 (PINNED) lines naming `refs/gov/requests/`.
- AC5 — a probe sourcing the driver in clone A under session `sA` read `check_request_consent <key>` rc 0
  (PINNED); under `sA2` in clone A and under `sB` in clone B it read rc 1 (PINNED), printing
  `request — <key> · relayed: data with provenance, never consent`.
- AC6 — `grep -n -- "--request" tools/unattended/VERBS.template.md` found its entry,
  `grep -n "refs/gov/leases/request/" tools/unattended/STOPS.template.md` found the grammar line, and
  the stops guide names the reserved slug `request`; the `verb:unattended.sh:--lease` line of
  `help/loop.md` names `request <content key>` and `no-record`, `verb:unattended.sh:--request` is
  anchored once, and the anchors carry `b121c595` and `3ed0250c` (DERIVED), what
  `docs_leg.py --fingerprints` printed for each. Both guides' renders are byte-for-byte copies (`cmp`
  silent).
- AC7 — `--plant bom-pair` printed `f49fa541cb48` (DERIVED) for `Fix the lander` with and without the
  bytes `EF BB BF`, `held`; `--plant undecodable-refused` printed `request — refused: … is not UTF-8`,
  exit 2 (PINNED), its scratch directory holding only the request file; `key` over `Fix` and `E9` named
  byte 3 (PINNED), and over the same after a byte-order mark byte 6 (PINNED), the offset in the file.
  Through the driver, `--request` over that file exited 2 (PINNED) with the same line.
- AC8 — the four plants ran one at a time by `--fixture --plant`, each exit 0 (PINNED) printing `held`,
  in 0.4 s (PINNED) together; `git grep -c "loop request fixtures"` names `tools/gate-legs.json`,
  `tools/govkit/registry.toml`, `tools/govkit/subject-pins.tsv`, `memory/map/features/loop.md` and
  `tools/run-gates/selftest-budgets.txt`, and the manifest row's argv is `python
  {prefix}/loop/request.py --selftest`.
- S3 — with the origin renamed away, `--request` over a second file printed `not written, the text kept
  and a re-run retries`, exit 2 (PINNED), its `.md` and `.typed` present; with the origin back the re-run
  printed `recorded`, exit 0 (PINNED). With the origin away, `--lease acquire request <key>` printed
  `lease not written — the remote did not answer the record read`, exit 2 (PINNED).

**Owed at the close.**
- The `New arm:` line on `tools/unattended/unattended.test.sh`: the region-eight block
  `TOOL-dPlacedRequest-19`, 37 (DERIVED) assertions, 22 `same` and 15 `hit`, RED-first against the base
  driver, which has no request verb; the floors rose by the same 37 (DERIVED), `FLOOR_ASSERTIONS` and
  `FLOOR_SHARD_8`. Waived for this build's landing by README rule 8.
- The `New arm:` line on `tools/loop/request.py`: the leg `loop request fixtures`, its `--selftest`
  RED-first against a key taken over the raw bytes, and its first reading, which re-prices the budget
  row's proxy.
- The legs the spec's section 7 names, the kit gate's check 26 over the new verb among them.

**The checklist, acted on.** The bug-class checklist over the pass commit `60c744ca9` selected 60 (DERIVED)
classes by anchor and 6 (DERIVED) universal. One needed a change. refusal-branch-with-no-arm: the
lease's malformed key and third segment, a request that is not UTF-8, a session id outside letters,
digits and dashes, no file and a file that is not there, and the push and the record read that do not
answer, with the re-run recording the kept words, had no suite arm; the region-eight block gained 18
(DERIVED) assertions, each first observed by the probe above, as user `daily-agent` in clone A: the
session `q.A` printed `the session id is not letters, digits and dashes`, exit 2 (PINNED), no file and
two files each `the form is --request <file>`, exit 2 (PINNED), a missing file `the request file is not
readable`, exit 2 (PINNED), and `acquire request <key> extra` `a request lease takes no third segment`,
exit 2 (PINNED). Branches still with no arm, named: no python, no loop kit, other than one remote, a
local store, copy or `.typed` line that cannot be written, and a commit git cannot build, each
unreachable in the fixture without a stub of python, git or the file system; and `request.py key` over
an unreadable file or with no memory-tree kit, observed by the probe above for the missing file, exit 2
(PINNED). Named and left: held-suite-guard-misses-a-sibling-kit, since `loop request fixtures` reads
the memory-tree kit's normaliser and, like every loop leg registered as `loop claims fixtures` is,
carries no guard, so an edit to that normaliser alone selects the leg on no scoped bar;
budget-row-not-remeasured-after-added-arms, since the unattended suite's budget row keeps its reading
while the suite is waived; two-answers-to-one-question, since the content key's shape is held in the
driver's lease builder, its writer, its consent predicate and the claim read's awk, each a closed
twelve-hex test the suite arms; and a-new-leg-trips-a-growing-set-of-meta-gates, the leg's registry,
pin, budget and dossier joins being the close's to read. The rest read clean: the arms assert a positive
witness each, every count is `grep -c .` over a capture that may be empty, the existence read matches
the whole ref name, and the `.typed` read matches a whole line.
