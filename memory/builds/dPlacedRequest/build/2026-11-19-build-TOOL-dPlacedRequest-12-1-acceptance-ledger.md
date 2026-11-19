# TOOL-dPlacedRequest-12 — acceptance ledger

**Serves:** journal TOOL-dPlacedRequest-12

The unit was built from its spec at rev-5 (PINNED) on base `2125460bb`. `tools/unattended/unattended.sh#derive_ref_segment`
writes every byte outside `[A-Za-z0-9_-]` as `%HH` under `LC_ALL=C` and refuses an empty text (S1);
`tools/unattended/unattended.sh#derive_decision_key` joins the item's and the fork's segments with `+` (S2);
`tools/unattended/unattended.sh#derive_problem_id` cuts `git hash-object --stdin` over the session, the item,
the subject and the body, each followed by a NUL, to its first 12 hex digits (PINNED) (S3).
`tools/unattended/unattended.sh#write_register` holds the switch, the arity, each field, `check_slug`, the
component bound `REF_COMPONENT_CEILING` and the body in that order, then builds one parentless commit with
`build_gov_commit ""` and writes it with `write_gov_ref <ref> "" <commit>` (S4 to S7, S9); a lost create
prints `register — exists <ref>`, fetches that ref once through `observe_remote` into this node's cache
ref, sights it into the feed and prints its record. The `--register` arm of the parse loop calls it, and
`VERBS_INLINE`, the header, `tools/unattended/VERBS.template.md` (rendered byte for byte to
`memory/guides/UNATTENDED-VERBS.md`), the Skill's fenced verb list and `help/loop.md` name it (S8).

No gate, suite or bar ran in this pass. AC1 and AC2 were observed by sourcing the driver; AC3 to AC10 by a
probe script in the run's scratch directory over a fixture of the suite's own `mkconf`, read out of
`tools/unattended/unattended.test.sh` by `sed`: a bare origin and two clones under the node's short temp
path, clone A under session `sA` and clone B under `sB`, `RUN_CLAIMS` on in both.

**Evidences:** TOOL-dPlacedRequest-12
- AC1 — the sourced encoder printed `%2Egithooks%2Fpre-push`, `x%2Elock`, `a%20b`, `ns%3Atag` and `HEAD%7E1` for the table's five subjects, and `git check-ref-format "refs/gov/problems/<out>/x"` exited 0 (PINNED) on each;
  a planted copy whose class keeps `.` printed `.githooks%2Fpre-push` and `x.lock`, and
  `check-ref-format` exited 1 (PINNED) on both, the RED.
- AC2 — `a+b`, `a/b` and `a%2Bb` encoded as `a%2Bb`, `a%2Fb` and `a%252Bb`, three apart, and an empty text returned 1 (PINNED) printing nothing;
  `derive_decision_key entry.claim F1` printed `entry%2Eclaim+F1`.
- AC3 — clone A's `--register decision fx entry.claim F1 a.txt` exited 0 (PINNED) printing `register — written refs/gov/decisions/fx/entry%2Eclaim+F1`, and clone B's same slot with `b.txt` exited 1 (PINNED) printing `register — exists` and A's record;
  the origin's ref held one commit, no parent, authored `gov-claim`, its body `decide A` alone.
- AC4 — two problems with different texts against `tools/push-main.sh` each exited 0 (PINNED) and landed as two refs under `refs/gov/problems/tools%2Fpush-main%2Esh/`;
  the ids were `67e72741a70f` and `5c7050b18ff4`.
- AC5 — the first filing re-run with the same session, item, subject and text exited 1 (PINNED) printing `register — exists` and its record, and the origin still held 2 (DERIVED) problem refs;
  so a retried filing is refused rather than landed twice.
- AC6 — `--register problem` given a 4097-byte (PINNED) body exited 2 (PINNED) printing `the body is over 4096 bytes: 4097` (PINNED), and a body carrying a NUL exited 2 (PINNED), the origin's `for-each-ref` unchanged across both;
  a body of exactly 4096 bytes (PINNED) was written, and one ending in a CR was refused as a control
  byte.
- AC7 — with `RUN_CLAIMS="off"` in clone A's conf, `--register decision fx item2 F2 a.txt` printed `register — off` and exited 2 (PINNED), and the origin gained no ref;
  exit 2 is the not-written code the verbs guide names, as `--lease` takes it with the switch off.
- AC8 — `grep -n -- "--register" tools/unattended/VERBS.template.md` names both forms on the entry's lines and the exits 0, 1 and 2 (PINNED);
  the guide's render is byte-identical (`cmp` exited 0).
- AC9 — `--register problem` with a subject of 80 (PINNED) `/` bytes exited 2 (PINNED) printing `register — refused subject over 240 bytes encoded` (DERIVED), and `git ls-remote <origin> 'refs/gov/problems/*'` printed what it printed before;
  the refusal comes before any commit or remote read.
- AC10 — `--register decision` with an item and a fork of 120 (PINNED) plain bytes each exited 2 (PINNED) printing `register — refused decision key over 241 bytes encoded` (DERIVED), the origin's decisions unchanged;
  each segment alone is under the ceiling, so the bound is on the joined key.

The edges beyond the criteria: an empty item, a `../x` build (check 1 (PINNED), then `not written`), a subject
or fork carrying a newline or CR, a wrong arity and an unreadable body each exited 2 (PINNED) and wrote
nothing; `--feed check` exited 0 (PINNED) in both clones after every write and the exists read.

A clone declaring two remotes printed check 24 (PINNED) and `register — not written <ref> · the clone does
not declare exactly one remote, check 24`, and an origin moved away printed `register — not written <ref> ·
git push exited 128 (PINNED) and printed no status line`, each exiting 2 (PINNED) with no ref written.

**Owed at the close.** The `New arm:` line of section 7: the region-8 block `TOOL-dPlacedRequest-12` in
`tools/unattended/unattended.test.sh`, 36 assertions (DERIVED), RED-first against the base driver, which has
no register verb; the floors rose by the same 36 (DERIVED), 20 (DERIVED) in the pass commit and 16 (DERIVED)
in the checklist's. The suite is waived for this build's landing by README rule 8. The leg-observed criteria are the close's too: check 26 of the unattended kit gate over the new
verb's five carriers, the `unattended skill size` row, the `docs` usage anchor and the codebase map's
freshness.

**The checklist, acted on.** The bug-class checklist over the pass commit selected 57 classes (DERIVED), 51
(DERIVED) by anchor and 6 (DERIVED) universal. One needed a change. refusal-branch-with-no-arm: the arity,
an empty field, a field carrying a control byte, a build that is no build-folder name, an unreadable body, a
body ending in a CR, two remotes and an uncompleted push had no arm, so the block gained 16 (DERIVED)
assertions over them, each probed first over the scratch fixture. The branches no fixture reaches, a commit
git cannot build and a key or id that does not derive from fields already held non-empty, are named in the
block's header. id-matched-as-a-substring was read against `--register` beside `--register-task`: the parse
arm, `VERBS_INLINE` membership and check 26's joins each match the whole word, so no change.
