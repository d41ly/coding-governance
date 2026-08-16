# TOOL-aQuarriedLantern — closing-review fixes, group G2 (interpreter, docs and diagnosis)

**Serves:** journal TOOL-aQuarriedLantern-1  <!-- inferred: this build defines exactly one spec id, so the record can serve nothing else -->

Items F4, F3, F9, F10, F11, F12, F13 from
`memory/tooling/builds/2026-08-03-TOOL-aQuarriedLantern/reviews/2026-08-03-review-TOOL-aQuarriedLantern-1-2.md`.
Every number below came from a command run in-session, against a GREEN baseline of
`python tools/memory-recall/selftest.py` **19/19, exit 0** at `b3b800b`.

**Applied** 2026-08-03 · node `a` · base `b3b800b`

## F4 — a bare `python` launcher on both agent-facing surfaces

`adopt-memory-recall.sh:76` rendered `{{QUERY_CLI}}` as `python $REL/query.py` and
`query.py:100` was `CLI = "python " + _self_path()`, so the Skill's description, both of its code
blocks, the CLI's own `--terms` refusal and its `--opened` hand-back all printed a launcher a stock
Debian/Ubuntu host without `python-is-python3` does not have. Both now render `python3`; the kit
README's four copy-pasteable lines went with them.

`python3` is a LITERAL, not the script's resolved `$PY`: the rendered Skill is a committed artifact
shared across a fleet, so baking one node's answer reds `--check` on every node that resolves
differently.

Gated on both surfaces, and deliberately not on a third:

- `t_skill_description_invariants` scans the rendered Skill for `\bpython(?!3)\s+\S*query\.py`, plus
  a non-vacuity assert that it saw ≥2 `query.py` lines (it sees **3**).
- `t_printed_invocations_resolve` scans `query.py`'s own stdout+stderr for any bare-`python`
  launcher of a `.py`, plus a non-vacuity assert that at least one `python3` launcher was printed.
- The adopt script's OWN printed lines are excluded on purpose: those carry the resolved `$PY`, and
  on a node with no `python3` the correct token there is `python`. A rule banning it would
  false-red the terminal success state on exactly the population the fix is for.

## F12 — REL from git, not a prefix strip of two independently-derived spellings

Reproduced on this node with no second checkout: MSYS mounts `%TEMP%` at `/tmp`, so `pwd` inside a
kit under Temp spells the tree `/tmp/…` while `git rev-parse --show-toplevel` spells the same tree
`C:/Users/daily-agent/…`. The prefix strip then no-ops and REL stays absolute.

| expression, same tree, same cwd | value |
|---|---|
| `REL="${HERE#"$ROOT"/}"` (pre-fix) | `/tmp/claude/…/f12probe/tools/memory-recall` — absolute, machine-local |
| `REL="$(cd "$HERE" && git rev-parse --show-prefix)"` (fix) | `tools/memory-recall` |

End to end in that probe repo, invoked through the `/tmp/…` spelling: the fixed script scaffolds
`python3 tools/memory-recall/query.py` and `--check` returns **EXIT 0**; the pre-fix expression on
the same tree returns **EXIT 1, DRIFTED**, its diff carrying a 187-character absolute launcher.
`--check` is the loud direction — `--scaffold` writes that path into a committed artifact silently.

`t_printed_invocations_resolve` now asserts every printed path is RELATIVE, and asserts it BEFORE
the existing exists-on-disk check: `root / p` discards `root` when `p` is absolute, so on a POSIX
node the absolute spelling would sail through the exists check.

## F10 — the fork header undercounted its own fork and cited the wrong sha

`extract.py:4-7` claimed the fork was "five constructs wide … Everything else is upstream's, byte
for byte". It is six. Measured against the upstream blob:
`git show 5318064:scripts/recall/extract.py | grep -c "dont_write_bytecode\|recall_conf"` → **0**,
in 411 lines. Provenance corrected to **958bd35c3** (`git log -1 5318064 -- scripts/recall/extract.py`);
`fd6274d` is that revision's tip and its `--stat` lists 9 files, none of them `extract.py`.

The undercount was load-bearing, not bookkeeping: two of the preamble's three lines fail loudly if a
re-pull drops them (`FAMILIES = CONF.families` is a NameError without `CONF`), but
`sys.dont_write_bytecode` is the whole of the kit's "writes nothing inside your worktree" property
on this file and drops in silence. The review mutation-proved deleting it SURVIVED 18/18.
`t_zero_records_is_loud` already calls `extract.py` directly, so the gate is one path scan there —
`__pycache__` under the fixture, never a `git status` (a status is clean whether nothing was written
or the write was merely hidden by a near-universal ignore rule).

## F11 — 0 records AND 0 chunks was structurally excluded from every diagnosis

`if n_records or not n_chunks: return None` meant the state a one-character `MEMORY_ROOT` typo
produces got no message at all. Split into `if n_records: return None` plus an `EMPTY CORPUS` branch
that names MEMORY_ROOT as the prime suspect — the chunk arm is family-blind, so FAMILIES cannot
cause an empty chunk arm — and names the tracked-only corpus rule as the other way to reach it. Both
branches share one resolved-values block. New arm `t_empty_corpus_names_memory_root` points
MEMORY_ROOT at `no-such-corpus` and asserts `(0, 0)` counts plus the diagnosis.

## F3 — the runbook's step-2 verification was unsatisfiable on the tree it scaffolds

`WIRE-INTO-PROJECT.md:198-200` taught zero records as necessarily a FAMILIES bug, while the CLI
itself prints the dual diagnosis. §3 step 2 scaffolds header-only `DECISIONS.md` files and nothing
before §3c step 2 writes a record, so the documented check could not pass on a correct conf.

Step 2 now seeds one throwaway record (`- <FAM>-aSeed-1 · …` appended and `git add`ed, because the
corpus is read from the index) and the prose mirrors the CLI: two causes, the empty tree is the
expected one, and the seed is what tells them apart. The §6 chain-verification bullet was reworded
the same way.

## F9 — the kickoff probe hardcoded one kit spelling

`skills/session-kickoff/SKILL.md:148-150` gated the Step-4 recall probe on "a `memory-recall/`
directory" and gave a command with that path — false in the very repo that owns the kit, which keeps
it at `tools/memory-recall/`. Both spellings are now named and the command uses `<KIT>`, matching
`tools/check-wiring.sh:110`. Taken over the `{{MEMORY_RECALL}}` manifest-slot option: one clause
against a new template slot plus a fill in every adopter's manifest.

## F13 — the refusal shipped another project's domain vocabulary

`query.py:163-165` printed "why did the editor stop saving my page" with `puck_data` and
`document_guard` — inCMS module names, in the first message a new adopter sees, in a governance
template repo that has no editor. Replaced with a gate-refusal question and generic terms, plus one
line naming the KINDS of word that belong there. The measured recall figures above it are kept.
Recorded in `query.py`'s own fork header, construct (3), so the header keeps matching the file.

## Mutations — five, each asserted APPLIED on disk (byte length compared) and reverted

| # | Mutation | Result |
|---|---|---|
| M1 | render `{{QUERY_CLI}}` as bare `python` again | KILLED — `the rendered skill launches query.py with a bare python`, 3 lines listed |
| M2 | `REL="$HERE"` (what the no-op strip produces) | KILLED — `printed invocations carry an absolute path`, 18/20 |
| M3 | delete `sys.dont_write_bytecode` from extract.py | KILLED — `extract.py wrote bytecode into the worktree: ['memory-recall\\__pycache__\\recall_conf.cpython-314.pyc']` |
| M4 | restore `if n_records or not n_chunks` | KILLED — `0 records + 0 chunks was reported as success` |
| M5 | `CLI = "python " + _self_path()` | KILLED — `the CLI prints a bare-python launcher`, 7 lines listed |

M1–M4 were scored as one bundle (four distinct arms, no cross-talk), M2 and M5 re-scored singly
because both land in the same arm. Shell probed as `Msys` before any of it; a bare `bash` here can
be the WSL shim, which exits 127 with no stdout and scores fake kills.

Mutation runs used `MRECALL_NESTED=1` to skip the nested adopter-layout arm (≈3.5 min vs ≈7 min);
the authoritative full run is below.

## Gates — all green over the FINAL bytes

- `python tools/memory-recall/selftest.py` — **20/20 checks passed, exit 0** (18 pre-existing arms
  + the new `t_empty_corpus_names_memory_root` + the live-log identity arm); the nested
  adopter-layout run inside it reports `19/20, 1 skipped`. Baseline at `b3b800b` was 19/19.
- `bash tools/run-gates.sh` — **18/18 legs passed, 1 skipped** (`manifest-check self-test —
  unchanged vs main`), including `memory hygiene (12 checks)`, `memory-recall kit selftest`,
  `memory-recall skill wiring`, `kickoff-manifest ratchet` and `template size <=32KiB`.
- `bash tools/memory-recall/adopt-memory-recall.sh --check` — EXIT 0, re-run after the last edit.
- `bash tools/memory-tree/check-memory-hygiene.sh` — exit 0, silent.
- `bash tools/check-wiring.sh` — hooks ok · agent-cap ok · recall on its true `skip` (the opt-in is
  not taken in this repo).
- `bash tools/check-wiring.test.sh` — **18 passed, 0 failed**.
- `bash tools/check-kit-versions.sh` — exit 0.
- `bash tools/memory-recall/recall-opened.test.sh` — **8 passed, 0 failed**.
- `python tools/settings-merge.py --selftest` — PASS.
- `git diff --cached --stat` is byte-identical to `--stat --ignore-cr-at-eol` (8 files, +151/-40),
  so nothing became a whole-file CRLF rewrite; `git diff --cached --check` is clean.

One side effect worth recording: eyeballing the new refusal text ran the CLI, which appended one
`refused` row (qid 19) to this repo's live query log under `.git/recall/`. Untracked, and the
selftest's log-identity arm ran after it, so no gate saw a torn read.
