# Wave 2 — whole-product audit, synthesis

**Serves:** research TOOL-aScouredKit-2

**Subject:** the whole product surface at `093730e40355d6a04300966f791f2634379e8b45`.
**Lenses:** A hardcoded knobs · B govkit convergence · C prose load. **20 findings filed, 20 judged.**

## Verdict: BLOCKED

**Two blockers, both fail-closed, both one-line fixes.** `skills/session-kickoff/manifest-check.sh:33`
hardcodes the kickoff manifest's location, so the deployer asks the adopter where the manifest goes
and ships an engine that ignores the answer — the leg reds on every bar of every adopter whose
answer was not gov's, and `kickoff-manifest` is in the DEFAULT kit set. `tools/govkit/govkit.py:4401`
writes the target's gate-leg manifest only when the whole run has zero problems, so a normal `--all`
install recorded **57 emitted legs and wrote no manifest at all** — the target gets zero gate coverage
and a receipt claiming full coverage.

**12 confirmed · 7 partial · 1 refuted · 0 unverified. Precision 0.92.** Nothing died: all three
lenses returned, and every one of the 20 findings carries a skeptic verdict.

---

## 1. The three commissioning questions

### Q1 — are values that should be owner-adjustable hardcoded instead?

**Yes, in one specific and nasty shape, five times.** Not a dead knob anywhere: lens A traced a live
consumer for every declared knob it suspected (`CLONE_COUNT_FILE`, `RECALL_DARK_LAYERS`,
`READ_PATH_WAIVER`, `SEAM_FANIN_THRESHOLD`, `AUTH_PARAM`, `RECALL_CACHE_BUDGET_MB`,
`UNIVERSAL_BUDGET`, `GATE_BOUND`), which is genuine positive evidence and worth recording as such.
The defect class is the opposite: **the knob exists, the deployer honours it, and the engine the
deployer installs does not.** The descriptor moves a file with `{prefix}` or `{manifest_path}`, and
the shipped script then looks for it at a literal `tools/…` or `memory/…`. Confirmed instances at
`skills/session-kickoff/manifest-check.sh:33` (blocker, default kit set),
`tools/check-agent-cap-restatement.sh:54` (high), `tools/check-testsuite-counts.sh:27` (high,
partial), `tools/check-install-prefix.sh:46` (medium, partial — already specced as
`DEPL-dCarriedReceipt-15`), and the same shape one layer over in
`tools/drift-audit/adopt-drift-audit.sh:108` (high, filed under lens B). Every one of them fails
CLOSED — exit 1 or 2 on a leg that mostly runs unguarded — and three of them print a remedy naming a
path that does not exist in the adopter's tree. The reference implementation for doing it right is in
this repo twice over, twenty lines from two of the defects: `tools/run-gates/run-gates.sh:84` derives
its manifest as `${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}` and names the class in prose at
`:76`; `tools/check-agent-cap-restatement.sh:74` reads `MEMORY_ROOT` correctly in the same file whose
`:54` does not.

### Q2 — can every tool be DEPLOYED, UPDATED and WIRED into another project?

**DEPLOY: mostly, and nothing on the bar proves it.** 11 of 25 registry entries are never passed to
`apply` by any gate, and 7 of those are named nowhere in `selftest.py` or `matrix.py`. Their
deployability rests entirely on `selfcheck`'s declaration arms, which grade a descriptor and never an
install. **UPDATE: no.** `govkit update` classifies over the RECEIPT (`govkit.py:5124`), so a source
file gov newly ships for a kit the target already claims is not in the iteration space at all — the
verb reports the install clean and the adopter finds out at the next ImportError. Re-measured live at
this sha rather than read; not filed as a finding because `TOOL-aFlaggedScaffold-3` already tracks it,
but it is half the owner's question and the answer is still no. **WIRE: broken by a one-line guard**
(finding 6, blocker) and by a second defect above all four verbs — `plan` and `apply` ignore the
target's own committed `deploy.toml` `kits` list and silently substitute gov's registry default
(finding 7), which makes the documented three-command install path exit 2 for any target whose
selection is not gov's default six. **CHECK: the arm exists and gov does not run it on itself** —
`check-testsuite-counts.kit.toml` ships with no `[check]` table, which gov's own written rule forbids,
and the rule is enforced only against a target while gov's bar stays green (finding 10). The complete
per-entry table is §6, reproduced verbatim; every one of the 25 entries has a row.

### Q3 — can the load-bearing instruction .md files be optimized without breaking their instructions?

**Barely, and not where the byte pressure is.** The corpus is unusually disciplined about
duplication — the prose lens refused more cuts than it proposed and named each refusal with its
reason, including a ~600-byte lexicon overlap it declined because the charter is read every turn and
the Skill is not. What survives verification is two clean cuts totalling ~630 bytes, both in
`AGENTS.md`, both with every rule surviving in a named carrier in the same file: the third
restatement of the unattended-authorization rule at `:579-584` (~440 B, and the copy proposed for the
cut is measurably the least precise of the three) and a self-certified-obsolete timing pair at
`:529-530` (190 B). The pressure they relieve is real: `AGENTS.md` is 64471 against a declared 64512,
so **41 bytes**, on an unguarded leg — a staged 99-byte line reds the bar. But the larger answer to
this question is that prose-trimming is not the defect here. Four confirmed findings in this lens are
accuracy, not length: the hygiene catalog that calls itself the prose home stops at check 22 while
the gate implements 23; the README cell the charter *explicitly* delegates the check count to says
"23 checks" and enumerates 22, with its own opening paragraph still saying 21; a backlog row is false
at this sha; and the two documents that most need a ceiling — `WIRE-INTO-PROJECT.md` at 59833 B and
`.claude/skills/unattended/SKILL.md` at 48767 B — have no declared ceiling anywhere and are
unreachable by check 6.

### Did any lens or skeptic batch die?

**No.** All three lens writeups landed complete (`wave2-hardcoded-knobs.md`,
`wave2-govkit-convergence.md`, `wave2-prose-load.md`), and every finding filed across the three —
5 + 6 + 9 = 20 — carries a verdict with reproduction detail. No batch was truncated, timed out, or
returned partial.

---

## 2. CONFIRMED findings, severity-ordered

| id | sev | file:line | claim | fix |
|---|---|---|---|---|
| 1 | **blocker** | `skills/session-kickoff/manifest-check.sh:33` | `MANIFEST_LOCATIONS` hardcodes two paths and the file reads `MEMORY_ROOT` zero times, while the descriptor seeds the manifest to the target-supplied `{manifest_path}` and the leg argv passes no path — so at any other answer the leg exits 2 forever and its remedy tells the adopter to abandon their declared memory root. In the DEFAULT kit set. | One token: put `{manifest_path}` in argv at `tools/govkit/entries/kickoff-manifest.kit.toml:37` — the script already grades a path passed as `$1`. Durable: read `MEMORY_ROOT` the way `tools/check-agent-cap-restatement.sh:74` does. |
| 6 | **blocker** | `tools/govkit/govkit.py:4401` | The gate-leg manifest write-back is guarded on the GLOBAL `r.problems` accumulated since step 1, while LEGS is step 9 — so any earlier by-design problem withholds the entire manifest for every kit in the run, and `emitted` is still written into the receipt at `:4507`. A `--all` install recorded 57 emitted legs and wrote no manifest anywhere. | Snapshot `len(r.problems)` at the top of the LEGS step and guard on problems raised since that point; print an explicit withheld line; omit `emitted` from the receipt when the manifest was not written. |
| 3 | high | `tools/check-agent-cap-restatement.sh:54` | `WAIVERS=${1:-tools/agent-cap-restatement-waivers.txt}` while the descriptor installs the registry at `{prefix}/…` and the leg argv passes no positional; the miss is swallowed by `2>/dev/null` at `:132`. At `vendor/gov` the registry is invisible, exit 1, and the printed remedy names a path absent from the tree. Line 74 of the same file reads `MEMORY_ROOT` correctly. | Append `{prefix}/agent-cap-restatement-waivers.txt` to the leg argv at `tools/govkit/entries/check-agent-cap-restatement.kit.toml:39`, or default `WAIVERS` to `$(dirname "$0")/…`. One line either way. |
| 7 | high | `tools/govkit/govkit.py:434` | `resolve_selection`'s default branch reads the REGISTRY default and never `deploy['kits']`; only `cmd_adopt` (`:6232`) reads the target's own list. A target declaring `kits = ["check-wiring"]` gets a six-kit preview and then `apply` exits 2 over an `lf_pin` needing an answer intake never asked for. The documented no-`--kits` path is the broken one, and `plan` previews the same wrong set. | In the default branch prefer `deploy['kits']` when present, exactly as `cmd_adopt` already does; fall back to the registry default only when the target declares none. |
| 9 | high | `tools/drift-audit/adopt-drift-audit.sh:108` | `WORKFLOWS_REL="${KIT_REL%/*}/workflows"` hardcodes the sibling DIRECTORY NAME, but govkit lands those scripts under the entry id (`{kit} = f"{prefix}/{eid}"`, `govkit.py:790`) at `{prefix}/review-harness/` — so the rendered `SKILL.md:73-74` tells the agent to run two files govkit never creates. `--check` is blind because it re-renders from the same template; the unguarded `drift-audit wiring` leg reports green over a dead pointer. | Derive the sibling dir from the `review-harness` entry's resolved destination or make it an `[answers]` key, and make `--check` assert the rendered paths EXIST rather than only that the render matches the template. |
| 5 | medium | `tools/check-install-prefix.sh:63` | Both arms bind a kit-DIRECTORY segment (`$alt`, derived at `:46`) and an extension from `sh\|py\|js\|md\|json\|toml`, so a literal naming a LOOSE file under `tools/` and any `.txt`/`.tsv`/`.conf`/`.example` path is invisible to both. Measured: 260 hits across 55 shipped files — including the gate's own `WAIVERS` line at `:33`. This is why findings 1–4 are green. | Widen the extension class to `txt\|tsv\|conf\|example` and add a third arm over `git ls-files -- 'tools/*' \| grep -v /` (same derivation discipline as `$alt`). Run `--list` over the tree before wiring; expect ~55 rows. Roughly a fifth of the hits are scratch-repo fixture names inside `.test.sh` bodies, so the third arm needs a principled exclusion, not a blanket widening. |
| 10 | medium | `tools/govkit/entries/check-testsuite-counts.kit.toml:19` | The only descriptor in the tree with no `[check]` table at all. The rule forbidding that lives only in `run_kit_check` (`govkit.py:2455`), reached from `cmd_check` against a target; `selfcheck` carries the identical rule for `version_from` (`:1000`) and no equivalent arm for `[check]`. `selfcheck` exits 0 and never mentions it. | Add the reason (or an argv) to the descriptor, and lift the assertion into `selfcheck` so gov grades its own descriptors on the same terms as an adopter's. |
| 14 | medium | `tools/memory-tree/README.md:18` | The cell says "23 checks" and its parenthetical enumerates 22 (12 + 2 shell, 4 `corpus_ids.py`, 3 `gotchas.py`, 1 `row_grammar.py`); check 23 is in the shell and in no bucket. Charter §5 explicitly delegates this count here and says it is "deliberately not restated" — so this cell is the only carrier, and it now contradicts its own breakdown. Worse than filed: `:6` still says "a 21-check hygiene gate". | Change the shell bucket to "1-12, 21, 22 and 23" and fix `:6` in the same edit, or derive both the count and the split from the `fail <n>` sites so the cell cannot drift again. |
| 15 | medium | `AGENTS.md:579` | The unattended-authorization rule is stated three times in one file; the Conventions bullet at `:579-584` (559 bytes, measured) carries no property absent from `:127` and `:555-560`. The duplication has already drifted — `:558`'s "the remote's own HEAD advertisement … never named by the environment" is a property neither other copy carries, so the copy proposed for the cut is the least precise of the three. §1's own unattended block forbids exactly this shape. | Collapse `:579-584` to its first clause plus the pointer. ~440 bytes recovered — eleven times the current 41-byte margin — with every rule surviving in a named carrier in the same file. |
| 11 | low | `memory/backlog/TOOL.md:113` | `TOOL-dClosedLexicon-15` is OPEN and states the `playbook` entry declares BOTH files `project-owned` so the default selection installs no playbook. The entry now declares ONE file at `role = "seed"` (landable per `LANDABLE_ROLES`, `govkit.py:230`), the descriptor's comment at `:17-21` records the repair, and a measured default apply writes the charter to `AGENTS.md`. | Close the row, or rewrite it to whatever question about the playbook entry actually remains open. |
| 19 | low | `AGENTS.md:529` | 190 bytes of cold/warm timing that the next sentence certifies as describing "a bar that no longer exists". It carries no rule; the figures survive at `memory/builds/aShardedFloor/README.md:53` and `TOOL-aScannedThrottle-8` (which re-prices the same 39 s delta). It is also mislabelled — it is a hint-present/hint-absent pair, and `TOOL-aTimedTurnstile-4` holds the genuine cold/warm one. | Delete both sentences. The live pointer to `<git-dir>/gate-ledger.tsv` two lines above survives the cut. |
| 20 | low | `WIRE-INTO-PROJECT.md:1` | `WIRE-INTO-PROJECT.md` (59833 B / 816 lines) and `.claude/skills/unattended/SKILL.md` (48767 B / 731 lines) have no declared ceiling anywhere — no row in `template-size-limits.txt` or `line-length-limits.txt`, no size leg in `gate-legs.json`, and neither is under `MEMORY_ROOT` so check 6 never sees them. `UNATTENDED-PROTOCOL.md` is at 92.9 % of `GUIDE_CAP_BYTES` with 52 lines left. | Add rows to `tools/template-size-limits.txt` seeded from the landed measurement **and** a matching leg in `tools/gate-legs.json` — a row alone is inert, since `check-template-size.sh` only measures a subject it is invoked on. No prose cut proposed: the SKILL is a genuine re-derivation of the protocol, not a copy (longest shared run 20 words of 7896). |

---

## 3. PARTIAL findings — corrected severity beside the original

| id | sev (filed → corrected) | file:line | what survived | what was struck |
|---|---|---|---|---|
| 2 | high → **high** | `tools/check-testsuite-counts.sh:27` | `MANIFEST=tools/gate-legs.json` and `WAIVERS=memory/project/…` are both hardcoded roots in a shipped engine. At `prefix = "vendor/gov"` with a valid manifest in place, the gate exits 2 — `"no tools/gate-legs.json, so the population would be empty"` — and `GATE_LEGS=` does not override it, because this engine has no such seam. The sibling `run-gates.sh:84` derives the same manifest correctly and `:76` names the class in prose. | "`govkit.py:4310` drops the guard, so the leg runs unguarded" is **false**. The guard is a two-element list; `govkit.py:4338-4346` drops only the element matching no tracked path, `guards` stays non-empty with the `{prefix}` element, and the UNGUARDED print fires only `if dropped and not guards`. The leg loses one guard element, not its guard. Strike that clause; the exit-2 impact stands unchanged. |
| 4 | high → **medium** | `tools/check-install-prefix.sh:46` | The gate for this class is the class: `WAIVERS` (`:33`), `kits=$(git ls-files -- 'tools/*/*')` (`:46`) and `CARRIED` (`:129`) all pin `tools/` while the descriptor ships all three to `{prefix}/`. At `vendor/gov`: `"no kit directories under tools/ — that is not a pass"`, exit 1, on a `subject = repo` / `guard = []` leg, with a message naming no fix. | The ask is already SPECCED. `DEPL-dCarriedReceipt-15`'s text reads "make check-install-prefix.sh prefix-parametric", naming this exact file and this exact fix. The only increment is that the failure is a hard exit rather than degraded coverage — a severity annotation on a specced row, not a fresh defect. Narrowed further by `selectable = "conditional"`. |
| 8 | high → **medium** | `tools/govkit/matrix.py:5` | `tools/govkit/deployability.test.sh` has never existed (`git ls-files` and `git log --all --diff-filter=A` both empty), no leg runs it, `lands_nothing` — the key its AC7 rests on — is in no descriptor, and `DEPL-aTetheredConvoy-3` is Status CLOSED with AC7 requiring it. 11 of 25 entries are never passed to `apply` by any gate; 7 are named nowhere in either harness. | The cited line does not say what the finding says. `matrix.py:5` names a LEG, never the file path — the filename is the spec's. And `SCRATCH_KITS` is not narrowed on that ground: the comment above it states the ground as "the entries whose legs run against a DEPLOYED artifact", then says outright that every other entry's legs stay unexecuted "and that is a known ceiling, not an assertion about them". The closing argument — "worse than an acknowledged gap" — is contradicted by the acknowledgement three lines below the cited line. Records-vs-reality drift plus a declared ceiling, not a live defect. |
| 12 | high → **medium** | `tools/template-size-highwater.txt:1` | Every number reproduced: live 64471 / 48907 / 18225 against highwater 60930 / 48378 / 18215, so all three WARN on every bar; `AGENTS.md` is 41 bytes under 64512; a staged 99-byte append reds with `"64570 bytes, 58 over 64512"`. All three product legs are unguarded. Untracked in `TOOL.md` / `DEPL.md`. | "The ratchet no longer prices anything" is interpretation, contradicted by the gate shouting on every run. The gate itself prints "Advisory only; re-record with `--bump` when the growth is intended" — the WARN is by design, the ratchet DID make the growth visible three times, and `--bump` is deliberately kept out of the ceiling file so that raising is a visible act. Nothing is broken today; the fix is explicitly the owner call the limits file's header reserves. What survives is narrower: 41 bytes of headroom on an unguarded leg means the next wrapped line reds the bar. A headroom condition, not a live defect. |
| 13 | high → **medium** | `memory/HYGIENE.md:252` | The catalog headed "this file is the prose home" (`:115`) ends at item 22; `grep -n "23"` over the whole file returns ZERO hits. The shell implements 23 at `check-memory-hygiene.sh:1120` with three live `fail 23` arms at `:1285-:1287`. `HYGIENE.template.md` ends at 22 too, and `kit-dogfood-parity.test.sh:53` byte-compares the pair, so the parity leg is green over a shared gap. No gate compares the catalog to the shell's numbers. | The impact overstates: the rule check 23 grades DOES have prose in the same file, at "## Acceptance ledger" (`:291-:316`), which states the two-form ledger, the no-third-form rule and the coverage disclaimer. The defect is that the catalog's numbering does not route there, not that the spec is absent. Second, this is F2 of an already-committed review in this same build (`wave2-prose-load.md:130-160`) — still live and unfixed, so it survives, but it is a re-report rather than a discovery. |
| 16 | medium → **low** | `memory/guides/BUILD-METHOD.md:8` | M1 declares "≤24 KB, ≤350 lines" and "The BYTE half binds first"; live is 24549 bytes / 317 lines, so 27 bytes under 24 KiB while the line half has 33 lines of slack. Check 6 grades this file at the kit-default 61440/750, nowhere near. | The KB/KiB question is not open: `memory/DECISIONS.md:102` — the record that OWNS the figure — states "the BYTE half stays at 24576". The file is 27 bytes under a ratified ceiling and not in breach. "Nothing measures it" is a restatement of `TOOL-dHonouredPark-2` (CLOSED), which says so verbatim and closes with "Whether that pair ever gets a leg is a separate question nobody has been asked" — precisely the fix proposed here, already deferred to the owner. And "the row's recorded description is no longer the live condition" does not follow: that row is CLOSED and records a past raise. What genuinely survives is the 27-byte figure as a heads-up. |
| 17 | medium → **low** | `AGENTS.md:575` | "48 KiB" is typed in three prose carriers — `AGENTS.md:17`, `AGENTS.md:575`, `memory/guides/SESSION-KICKOFF.md:194` — beside `tools/template-size-limits.txt:27`, which owns 49152 and whose header records the single 32768 → 49152 move. `AGENTS.md:230` states the rule being broken. ~100 B in a file with 41. | The severity driver is refuted by git: `git log -S'32 KiB' -- AGENTS.md` and `git log -S'48 KiB' -- memory/guides/SESSION-KICKOFF.md` both resolve to `1640f680`, the commit that moved the ceiling — all three carriers were updated ATOMICALLY, so "each carrier was wrong for the duration of that move" is false, and "will be again" is unmeasured. `SESSION-KICKOFF.md:197` already carries its own mitigation in the same bullet: "Read the current margin FROM `bash tools/check-template-size.sh`, never from prose". A tidy-the-class cut, not a live rot. |

---

## 4. UNVERIFIED findings

**Zero. No finding went unreached by a skeptic.**

This is stated as its own section because a silent zero here is indistinguishable from a batch that
died. It did not: 20 findings were filed across three lenses (5 + 6 + 9), and 20 verdicts came back,
each carrying its own reproduction — commands run, exit codes observed, and in several cases a
sub-claim struck on measured evidence rather than on doubt. **That is positive evidence about this
review, not merely an absence of bad news:** the skeptic pass had enough budget to reach every
finding, so no severity in §2 or §3 rests on a finder's word alone, and no reader has to discount the
report for coverage they cannot see. The one refuted finding (§5) was refuted by git archaeology that
a coverage-starved pass would not have run.

---

## 5. REFUTED findings

| id | file:line | filed as | why it was dismissed |
|---|---|---|---|
| 18 | `memory/guides/SESSION-KICKOFF.md:121` | The `GATE_SELFTESTS` owner ruling is dated 2026-08-27 in `AGENTS.md:484` and 2026-08-26 here — the same rule with two provenance stamps, adjudicable from neither carrier nor the log. | They are **two distinct rulings on two distinct days**, and git proves it. `325d5f55` (2026-08-26) expanded the held population to `subject = kit` OR `chunk = selftests` — exactly what `SESSION-KICKOFF.md:121` attributes to that date. `75e0e5c0` (2026-08-27) is "kit self-checks run ON DEMAND only — owner ruling 2026-08-27", and its diff is the very hunk that introduced the `AGENTS.md:484` stamp; its body states the new fact ("No boundary runs a self-test now") that the 08-26 ruling did not yet say. Each carrier is correctly dated for the statement it makes, and the 08-27 commit message is a full recorded rationale including the argument that lost. The residual true fact — neither ruling has an id in `memory/DECISIONS.md` — is not the finding as written and does not carry its stated impact once the disagreement is gone. (The cited command is also partly inert: `memory/decisions/` does not exist in this tree.) |

---

## 6. The per-entry deploy / update / wire / check table (lens B, verbatim)

> `tools/govkit/registry.toml` declares 25 `[[entry]]` rows. Thirteen `tools/*/kit.toml` files exist and
> every one is a descriptor for one of those rows; the other twelve descriptors live under
> `tools/govkit/entries/`. There is no `kit.toml` that the registry does not claim and no entry whose
> descriptor is missing — `selfcheck` asserts both and it is silent on that arm.
>
> Columns:
>
> - **DEPLOY** — does `apply` land bytes for it, and is that ever exercised by a gate?
>   `apply@gate` = the entry is passed to `apply` somewhere in `selftest.py` or `matrix.py`.
> - **UPDATE** — every entry shares one classification loop (`govkit.py:5124`, `for row in rows_all`
>   over the RECEIPT), so no entry can receive a file gov newly ships. Per-entry variation is only in
>   the roles, so the column records the role hazard.
> - **WIRE** — what actually invokes it in the target after `apply`.
> - **CHECK** — `[check].argv` (runs a probe) · `none` + reason (declared absence) · **ABSENT**.

| # | entry | descriptor | DEPLOY | UPDATE | WIRE | CHECK |
|---|---|---|---|---|---|---|
| 1 | `playbook` | `entries/playbook.kit.toml` | 1 `seed` rule → `{playbook_path}`. apply@gate ✔ (default set + matrix shape 5) | receipt-bound | nothing runs the charter; it IS `AGENTS.md`. 0 legs, 1 authoring hole | `none` + reason |
| 2 | `playbook-render` | `tools/playbook/kit.toml` | 3 `engine` rules incl. two `root_relative` pulls of `tools/govkit/{entries/playbook.kit.toml,registry.toml}`. apply@gate ✔ (matrix) | receipt-bound | 2 legs (`playbook render wiring`, `… selftest`) | `argv` ✔ |
| 3 | `kickoff-manifest` | `entries/kickoff-manifest.kit.toml` | 3 rules; the engine dir is an ORDER (a junction the operator makes). apply@gate ✔ | receipt-bound | 1 leg (ratchet) | `none` + reason |
| 4 | `memory-tree` | `tools/memory-tree/kit.toml` | 3/6 landable; 3 `rendered` produced by its own adopter. apply@gate ✔ | receipt-bound | 16 legs | `none` + reason |
| 5 | `codebase-map` | `tools/codebase-map/kit.toml` | 3/4 landable. apply@gate ✔ | receipt-bound | 3 legs; one is SILENCED against a fresh target (argv names `{gate_file}`) | `none` + reason |
| 6 | `memory-recall` | `tools/memory-recall/kit.toml` | 1/4 landable; 3 `forked`, 3 `project-owned` withheld. apply@gate ✔ | receipt-bound; `forked` rows never written by design | 2 legs + rendered Skill | `argv` ✔ |
| 7 | `run-gates` | `tools/run-gates/kit.toml` | 1/2 landable; `run-gates.gov.test.sh` withheld. apply@gate ✔ | receipt-bound | 6 legs, and it OWNS the manifest the others land in — **see F1** | `argv` ✔ |
| 8 | `drift-audit` | `tools/drift-audit/kit.toml` | 2/4 landable. apply@gate ✔ | receipt-bound | 3 legs + rendered Skill — **the Skill names a directory govkit never creates, F4** | `argv` ✔ |
| 9 | `agent-instructions` | `tools/agent-instructions/kit.toml` | 1 `engine` rule. **apply@gate ✘ — never named in either harness** | receipt-bound | 2 legs | `argv` ✔ |
| 10 | `unattended` | `tools/unattended/kit.toml` | 1/4 landable; 3 `rendered`. **apply@gate ✘** | receipt-bound | 3 legs; adopter exits 1 `no-project-layer` on a fresh target and all 3 rendered docs stay absent (`DEPL-aTetheredConvoy-9`) | `argv` ✔ |
| 11 | `pytest-parallel-guardrails` | `tools/pytest-parallel-guardrails/kit.toml` | 1/2 landable; 1 `merged` → BLOCK. apply@gate ✔ | receipt-bound | 1 leg | `none` + reason |
| 12 | `gate-lint` | `tools/gate-lint/kit.toml` | 1 `engine` rule. **apply@gate ✘ — `intake` only** | receipt-bound | **0 legs.** Declared: hole `gate-lint-leg-wiring`, undischargeable by construction | `none` + reason |
| 13 | `lexicon` | `tools/lexicon/kit.toml` | 2/3 landable. **apply@gate ✘** | receipt-bound | 3 legs + rendered Skill; `landed-but-inert` on a fresh target (3 authoring holes) | `argv` ✔ |
| 14 | `agent-cap` | `tools/hooks/kit.toml` | 7 `engine` rules, one source → two destinations. **apply@gate ✘** | receipt-bound | 2 legs; the `.claude/settings.json` entry that WIRES the hook is a `merged` rule with no writer | `none` + reason |
| 15 | `review-harness` | `tools/workflows/kit.toml` | 1/2 landable; lands at `{prefix}/review-harness/`, NOT `workflows/`. **apply@gate ✘ (`plan` only)** | receipt-bound | 7 legs; `memory/guides/REVIEW-PROTOCOL.md` is `rendered` with `adopt.argv = []`, so nothing renders it and `check-protocol-parity.test.sh` exits 1 in the target | `none` + reason |
| 16 | `settings-merge` | `entries/settings-merge.kit.toml` | 1/2 landable; the `merged` rule BLOCKs. apply@gate ✔ (merged-refusal arm) | receipt-bound | 1 leg | `none` + reason |
| 17 | `push-main` | `entries/push-main.kit.toml` | 2/3 landable; 1 `merged` → BLOCK. apply@gate ✔ | receipt-bound | 2 legs + `.githooks/` | `none` + reason |
| 18 | `check-wiring` | `entries/check-wiring.kit.toml` | 1 `engine` rule. apply@gate ✔ (the harness workhorse, 27 uses) | receipt-bound | 1 leg (self-test) + SessionStart | `none` + reason |
| 19 | `check-kit-versions` | `entries/check-kit-versions.kit.toml` | 1 `seed` rule. **apply@gate ✘** | receipt-bound | 1 leg; hole `kit-versions-need-list` UNDISCHARGED on arrival by design | `none` + reason |
| 20 | `check-testsuite-counts` | `entries/check-testsuite-counts.kit.toml` | 1 `engine` rule. **apply@gate ✘** | receipt-bound | 2 legs; the repo-subject leg guards on the literal `tools/gate-legs.json` (dropped at emit, so the leg runs unguarded) | **ABSENT — F5** |
| 21 | `check-agent-cap-restatement` | `entries/check-agent-cap-restatement.kit.toml` | conditional; 1/2 landable. **apply@gate ✘** | receipt-bound | 2 legs | `none` + reason |
| 22 | `check-install-prefix` | `entries/check-install-prefix.kit.toml` | conditional; 1/3 landable. **apply@gate ✘ (`plan` only)** | receipt-bound | 2 legs | `none` + reason |
| 23 | `check-placeholders` | `entries/check-placeholders.kit.toml` | conditional; 1 `engine` rule. **apply@gate ✘** | receipt-bound | 2 legs | `none` + reason |
| 24 | `check-line-length` | `entries/check-line-length.kit.toml` | conditional; 1 `engine` rule. apply@gate ✔ (matrix shape 5) | receipt-bound | 2 legs | `none` + reason |
| 25 | `check-microformats` | `entries/check-microformats.kit.toml` | conditional; 1 `engine` rule. apply@gate ✔ (matrix shape 5) | receipt-bound | 2 legs | `none` + reason |

> **apply@gate ✘ count: 11 of 25** — `agent-instructions`, `unattended`, `gate-lint`, `lexicon`,
> `agent-cap`, `review-harness`, `check-kit-versions`, `check-testsuite-counts`,
> `check-agent-cap-restatement`, `check-install-prefix`, `check-placeholders`. Eight of those eleven are
> not named at all anywhere in `selftest.py` or `matrix.py`.
>
> Live install evidence for the whole table: a `--all` install into a fresh repo lands 165 files across
> 20 kits (5 entries are `selectable = "conditional"` and `--all` excludes them), leaves 19 orders in
> `.governance/outbox/`, and finishes with 7 problems.

**One correction to the table from the skeptic pass.** The row-20 parenthetical "dropped at emit, so
the leg runs unguarded" is the sub-claim struck in finding 2: `govkit.py:4338-4346` drops only the
guard element matching no tracked path, the `{prefix}` element survives, and the UNGUARDED print
fires only when the guard list ends up empty. The leg loses one guard element, not its guard. The
`ABSENT` verdict in the CHECK column stands and is finding 10. Row-8's "the Skill names a directory
govkit never creates" and row-7's F1 reference are both CONFIRMED.

**One count discrepancy worth recording.** The lens counted 8 of the 11 as named nowhere in either
harness; the skeptic re-counted 7 (`agent-instructions`, `lexicon`, `check-placeholders`,
`agent-cap`, `check-testsuite-counts`, `check-kit-versions`, `check-agent-cap-restatement`). The
11-of-25 figure is not in dispute.

---

## 7. How these defects enter, and what is one fix versus a class

**Class A — the deployer is parametric and the engine it installs is not. Five instances, one root.**
Findings 1, 2, 3, 4, 9. Somebody makes a path owner-adjustable at the descriptor layer — `{prefix}`,
`{manifest_path}`, `{kit}` — writes the seed or the registry to the answered location, and then leaves
the shipped script reading a literal. It is not carelessness about the concept: two of these files
read *another* root correctly twenty lines away (`check-agent-cap-restatement.sh:74` reads
`MEMORY_ROOT`; `adopt-drift-audit.sh` derives its own kit dir and hardcodes only its sibling's). The
pattern is that parametrising *one* root feels like finishing the job. Every instance fails closed on
a leg that mostly runs unguarded, and three print a remedy naming a path the adopter does not have —
so the class's signature failure is a red bar with an unfollowable message. **This is a class fix, not
five fixes:** derive from `$(dirname "$0")` with an env override in front, the way
`run-gates.sh:84` already does, and do all five in one pass. `DEPL-dCarriedReceipt-15` already scopes
part of it; it should absorb the measured hard-exit consequence before it is built.

**Class A′ — and the gate for class A cannot see class A.** Finding 5 is the reason the other four
sat green: `check-install-prefix.sh`'s two arms both require a kit-DIRECTORY segment and an extension
from a five-member set, so a loose `tools/<file>` literal and every `.txt`/`.conf` declaration file is
structurally invisible — including the gate's own `WAIVERS` line. This is the repo's own named
failure mode, "a structural check reads as a semantic one to everybody who did not write it", landing
on the gate whose header promises that "nothing this repo SHIPS may spell a root-install kit path".
Widening the predicate is the single highest-leverage fix in this report: it converts a five-instance
class into a ratchet that shrinks.

**Class B — the guard reads more state than it guards.** Finding 6, alone, and it is charter §7 word
for word: "a guard that shares a variable with the thing it guards is not a guard." The manifest
write-back was correctly moved *outside* a loop that had been failing it — the comment at
`govkit.py:4305-4308` records that repair with evident relief — and the new guard reads the global
problem list, so the same defect came back one scope up. **One fix**, four lines, and the receipt
change that goes with it.

**Class C — three verbs, two answers.** Finding 7: `deploy['kits']` is read in exactly one of four
call sites of one function. The defect is invisible because `plan` — the tool whose entire job is to
preview what `apply` will do — is wrong in the *same* direction, so the safety mechanism confirms the
error. **One fix**, and it is copying a line `cmd_adopt` already has.

**Class D — gov grades itself on a strict subset of what it grades an adopter on.** Findings 10 and 8.
The `[check]`-declaration rule lives only in the target-facing verb, so a defective descriptor gov
ships and gov's bar is green and the adopter is told. The deployability leg that would have driven
every registry entry through `apply` was specced, accepted, closed — and never written, leaving 11
entries whose only evidence is a declaration arm. These are two instances of the same asymmetry and
should be fixed together: lift the assertion into `selfcheck`, and either build the leg or amend the
docstring and widen `SCRATCH_KITS`.

**Class E — a number or a claim typed beside the source that owns it.** Findings 14, 13, 11, 12, 17,
16. The repo names this class in its own charter twice, in §7 ("NO count of a derived population is
written in prose") and §6 ("the one most often broken by the document that states it"), and then
breaks it in the README the charter *delegates a count to*, in the catalog that calls itself the prose
home, and in a backlog row that describes a repaired bug. Two of these are gateable and should be:
a leg comparing `HYGIENE.md`'s catalog to the shell's `fail <n>` sites, and size rows plus matching
legs for the two uncapped documents. The rest are one-line corrections.

**Class F — pure recoverable bytes.** Findings 15 and 19, ~630 B, one deletion each, every rule
surviving in a named carrier. They matter only because of finding 12's 41-byte margin, which is what
makes them worth doing this week rather than whenever.

**The through-line.** Nine of the twelve confirmed findings are green gates. In every one of them the
check exists, runs, and reports success over the defect: `check-install-prefix` cannot see the
literals it was built to ban; `adopt-drift-audit --check` diffs a render against the template that
produced it; `kit-dogfood-parity` byte-compares two carriers that share a gap; `selfcheck` exits 0 on
a descriptor `check --target` refuses; `plan` previews the same wrong selection `apply` installs; the
receipt records 57 legs nobody wrote. This repo's charter calls that outcome the worst one available —
"a green bar stops meaning anything" — and it is where the whole product's defect mass sits. The
hardcoded literals and the stale prose are symptoms; the checkable pattern is that a verifier which
shares an input with the thing it verifies cannot fail.

---

**Precision (confirmed / (confirmed + refuted)) = 12 / 13 = 0.92.** Counting the seven partials as
non-confirmations gives a stricter 12 / 20 = 0.60, and every one of those seven survived with real
verified facts — five were cut a severity band for overstated impact, one for citing a line that says
something else, one lost a single sub-claim and kept its band. Precision is above the ~0.5 floor at
which the charter says to tighten scope before adding agents, so the lens priming was sound; the
partial rate says the *impact* clauses ran ahead of the evidence more often than the claims did.
