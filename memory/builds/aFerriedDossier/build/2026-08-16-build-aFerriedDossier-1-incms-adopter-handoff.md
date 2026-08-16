<!-- Carried in from d41ly/incms, build memory/builds/aTetheredCistern/, unchanged in substance.
     Measured there against gov 96141ae and the aTetheredConvoy worktree at d594bf1, then verified
     by an adversarial pass (50 findings, 46 confirmed, 4 refuted, 0 unverified). Asks are
     DEPL-aFerriedDossier-1..3. -->

# Handoff to the `aTetheredConvoy` builder — from inCMS, node `a`

**Standalone by design.** This file is meant to be readable inside `coding-governance` with no
access to inCMS's memory tree. Every claim carries its own evidence. Measured against the gov
worktree `govkit-tooling-update-verb-74b3ef` at `d594bf1`, and against gov `main` at `96141ae`.

Provenance: inCMS cross-reviewed its vendored gov kits (94 claims, 84 confirmed, precision 0.89),
then mapped the resulting 26 upstream asks against `aTetheredConvoy`'s seven specs (50 findings,
46 confirmed, precision 0.92). inCMS is a hand-forked adopter carrying nine gov kits at the
`scripts/` prefix with no `.governance/` receipt, so it is an unusually harsh test target for this
build — which is the only reason this document is worth the builder's time.

---

## 1. The one thing this build does not cover, and nobody owns

**`aTetheredConvoy` gives every govkit-INSTALLED repo an update path and gives a hand-forked repo
nothing.** The README opens by naming the upgrade-orphan class it exists to end. inCMS is an
upgrade orphan of a different shape, and it stays one.

Measured at `d594bf1`: `adopt-existing|adopt_existing|hand-fork|from-commit|bootstrap` across all
seven specs returns **zero matches**.

Four independent readings put the same boundary in place:

| Unit | Sentence | What it presupposes |
|---|---|---|
| 2 · S1 | "classifies every file the receipt records against a newer gov commit" | a receipt exists |
| 2 · §4 | "the receipt's recorded gov commit does not resolve in this checkout — name the commit and DO NOT fall back to treating the target as a fresh install" | a receipt exists |
| 1 · §8 F2 | "A migration would rewrite records describing an install this unit cannot inspect, and the next apply corrects them anyway" | an `apply` has happened |
| 3 · §4 | "Per registry entry, in a hermetic scratch repo: `intake` … then `plan`, then `apply`, then `apply` again" | the fixture tree starts empty |

**The OUT clause is about a different case.** Verbatim from the README: "adding kits to an existing
install". Unit 2 §3 operationalises it into exactly one meaning — "`update` reports a registry entry
the receipt does not claim as AVAILABLE and refuses to install it, naming the flag that would
(`--add-kits`)". That predicate presupposes a receipt. It is *widening* an install that exists.
inCMS has no install to widen. So this case is not excluded; it is never contemplated — which is
worse, because an exclusion at least has an owner.

**It compounds with the clobber.** A hand-forked target's only gov-sanctioned route to a receipt
today is running `apply` against its own tree, and `apply` writes every non-`seed` role
unconditionally (`govkit.py:823-838`). The sole path from hand-fork to receipt runs through the
destruction of the fork.

**Cheapest form of the ask, riding a seam this build already has.** Not a new verb: one
`adopt-existing` variant inside unit 3 S5's per-entry fixture family — a scratch repo pre-populated
with a kit's bytes and no `.governance/`, asserting the receipt it produces has verifying sums.
Units 3 and 7 have already agreed that fixture FAMILIES are the extension seam, and both specs
record it. The schema half aims at unit 1.

Ask it as a **pair**, or half of it is useless: bootstrap the first receipt from foreign bytes,
**and** grow an existing one. A target that can bootstrap but not widen is stuck at whatever kit
set its first adoption named.

---

## 2. Defects measured in gov's tree, with line numbers

Each is either evidence this build lacks, or a defect in a spec that is still OPEN and therefore
still cheap to change.

| # | What | Where | Why the builder wants it |
|---|---|---|---|
| 1 | `intake` accepts `--answer prefix=scripts` and silently discards it. `prefix` sits in the `derived` set so `needed_answers()` filters it, and `cmd_intake` writes the literal `prefix = "tools"`. Measured: "2 answer(s) recorded", not 3, and the written descriptor says `tools`. `intake` then refuses to rewrite the file. | `govkit.py:884, 947, 951` (refusal at `:927-932`) | **Unit 4 AC13 requires a fixture where "the install prefix and memory root are non-default". That fixture cannot be built until this is fixed.** |
| 2 | The foreign-kit detection probe iterates the literal `for prefix in ("tools", "")`. Measured against inCMS's real tree it returns 2 of the 9 kits present; with `("tools","","scripts")` it also finds check-wiring, codebase-map, kickoff-manifest and settings-merge. | `govkit.py:722` | Unit 2 S5 arbitrates a row's role through descriptor resolution at the target's prefix. This is one of two places that resolution is literal, so S5 would refuse a non-default-prefix target's rows spuriously. |
| 3 | `sentinel` is appended unresolved — `if d.get("sentinel"): probes.append(d["sentinel"])` — never through `resolve_tokens`. Five descriptors carry `tools/` literals. | `govkit.py:734`; `agent-instructions/kit.toml:8`, `gate-lint/kit.toml:8`, `entries/check-kit-versions.kit.toml:9`, `entries/check-install-prefix.kit.toml:11`, `entries/push-main.kit.toml:9` | Same class as #2, one layer down, and it is the **sole** fallback for the three entries with `version_from = {none}`. Fixing `:722` alone does not reach them. Unit 1 S9's repair list does not contain it. |
| 4 | `apply`'s write loop has one existence check — `if role == "seed" and dp.exists(): continue` — then an unconditional `dp.write_bytes(data)`. No hash of the destination's pre-state is read anywhere. Every `role = "engine"` kit with `include = "**"` is clobbered. | `govkit.py:823-838` | Unit 2 §4 already cites this behaviour as an argument for a separate verb: "`apply`'s contract is 'land what is not there' and its re-run path already overwrites `engine` files without comparing." Whoever fixes it must **exempt receipt rows**, or unit 3 AC8's "a second `apply` changes no path and no hash" turns red. |
| 5 | `gov_source` is a machine-local absolute path written in two separator conventions — `root.as_posix()` by `intake`, `str(root)` by `apply`. Measured: `"C:/projects/coding-governance"` in `deploy.toml` against `"C:\\projects\\coding-governance"` in `install.json`. | `govkit.py:868, 945` | Unit 1 S4 freezes the receipt schema. Every field frozen wrong needs a migration to fix. inCMS runs six nodes across Windows and Linux; this field is wrong on arrival at five of six. Suggested shape: `gov_remote` + `gov_commit`, one convention. |
| 6 | Unit 2's verdict table iterates receipt rows only ("For each receipt row"), with one non-row cell for `unrecorded`. So a **gov-side rename** scores the old path `withdrawn` and deletes it while the new path lands nowhere; `blob_at` returns `None` on the old path. There is also no cell for a file gov ADDS, and none for a `moved` destination. | unit 2's verdict table | Follow renames with `git diff -M --name-status <base>..<to> -- <kit home>`. inCMS budgeted this at ~20 lines. Under `--write`, `withdrawn` deletes — so this is a data-loss path, not a reporting gap. |
| 7 | `install.sums` must be hashed **raw**: no newline normalisation, binary writes. | unit 3 AC8's hash comparison | AC8 depends on this and never states it. Without it the check reds on Windows and passes in CI, which is worse than no check. |
| 8 | A sums file that has gone EMPTY verifies silent-green. Two identical applies of a seed-bearing kit were measured leaving the file list empty and the sidecar empty with it. | unit 1's sidecar arm | This is the same shape as unit 3 S5's own liveness rule — "printing a derived count and reding when that count is zero". Worth applying to the sidecar arm too. |
| 9 | `gate-lint`'s hole `gate-lint-leg-wiring` declares `blocks_adopt = false` and `blocks_gate = false` alongside `discharge = { command = ["bash", "-c", "exit 1"] }`. | `tools/gate-lint/kit.toml` | Under unit 4 §4's exemption rule and unit 5's `[[outcome]]` evaluator, a probe hardcoded to `exit 1` is a permanently undischargeable declaration — it can never be observed CLOSING (unit 4 AC6). |
| 10 | `check-wiring.sh` resolves `ROOT` from CWD with a bare `git rev-parse --show-toplevel` and exits 0 with `skip — not a git repo` otherwise. It is wired as SessionStart in gov's own `.claude/settings.json:19`, which uses `${CLAUDE_PROJECT_DIR}` for the script path only — so any session opened outside the repo skips, exits 0, and the self-healing wiring path never runs. | `check-wiring.sh:25` | One line: try `git -C "$(dirname "$0")/.." rev-parse --show-toplevel` before falling back to CWD. Highest value-per-byte item inCMS found in gov. |
| 11 | `check-wiring.sh:368-369` falls back silently: `[ -n "$fams" ] || fams="ROWS"`. inCMS measured what that costs — the arm printed `ok merge — merge.rows.driver wired` while the driver keyed **zero** rows and every governed append-collision conflicted forever. | `check_merge_rows()` | Gov's own rule, applied to gov: a check that cannot fail is not a check. Replacement returns a loud `UNWIRED` naming the unreadable declaration, and strips CR in the same `tr` class (a CRLF worktree plus a CR-preserving `sed` harvests a family name with a trailing CR and reds the fleet). |
| 12 | Seven `subprocess.run(..., text=True)` sites with no `encoding="utf-8"`. `text=True` alone decodes with the machine locale — cp125x on a Windows node, UTF-8 in CI — so a non-ASCII message mis-decodes on one and not the other, and presents as a corrupt gate message rather than a locale bug. | `check-arms.py:65`, `corpus_ids.py:63,175`, `gen_build_index.py:90`, `gotchas.py:67`, `row_grammar.py:50,407` | Live on a Windows + Linux + CI fleet, not a theory. |
| 13 | `check-wiring`'s own `KIT_CHECK_WIRING_VERSION` sat at `1.0` on both gov and inCMS across **175 changed lines**. Any "am I in sync?" question answered from the constant answers *yes* over a 175-line fork. | `tools/memory-tree/check-verdict-epoch.sh` as the generalisation seam | Unit 3 S2 closes the version-CLAIM half. Nothing correlates changed BYTES with a bumped constant. The generalised leg: red when a kit's home changed between two commits and its `version_from` constant did not. |

---

## 3. The two-line request that is cheaper than any item above

Widen unit 3 S5's fixture family with two entries:

1. a **non-default prefix** entry, and
2. one **`adopt-existing`** variant.

Both are additions to a leg that is already per-entry and already builds scratch trees. Together
they convert the two things this build currently cannot see — a discarded prefix answer, and a
repository govkit never installed — into things the ratchet grades.

Without (1), the prefix fixes can land and regress a week later, because the only leg that executes
the product never exercises the token they fixed.

---

## 4. What inCMS is NOT asking for

Named so they are not read into the list above:

- **Not asking gov to support `tools/` alternatives as a general feature.** inCMS keeps `scripts/`
  by owner decision. Everything in §2 items 1–3 is a place where the descriptor's own `{prefix}`
  token is already the design and the code does not honour it.
- **Not asking for the three-way merge to be removed.** Unit 2 S4 builds it and gov owns the verb.
  inCMS's need is a strict mode where `diverged` REFUSES, keyed on the target's descriptor rather
  than on the operator remembering a flag — because inCMS's policy is that vendored kits carry zero
  local edits, so a `diverged` row is a policy violation rather than a merge.
- **Not asking for `remove`, fleet fan-out, or gate-runner grammars beyond one.** Those are the
  build's declared OUT list and inCMS agrees with all three.
- **Not upstreaming inCMS's `tier2-review-indexed.js`.** gov 1.2 already joins verdicts on an
  orchestrator-assigned integer and ships five degraded-shape counters inCMS lacks. inCMS's fork is
  strictly behind and will be retired.

---

## 5. Timing, where it matters

- **Items 10, 11 and 12, plus inCMS's `pre-push` refusal channel, want to land before unit 6.**
  Unit 6 S3 gives the branch-guard destination a refuse-and-order insert policy "because its
  position is SEMANTIC". inCMS's `fail_push` helper and the five bare `echo … ; exit 1` sites it
  replaces are edits to that same hook. Landing them after gov starts writing a marked region there
  is a merge nobody wants to author.
- **Item 5 wants to land before unit 1 is built**, because unit 1 §S4 freezes the receipt schema and
  `gov_source` is one of its fields.
- **Items 1, 2 and 3 want to land before unit 4**, which needs a fixture at a non-default prefix.
- Everything else can follow.
