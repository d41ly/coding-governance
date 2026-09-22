# wave2 — LENS A: hardcoded values that should be owner-adjustable

**Serves:** research TOOL-aScouredKit-2

## Verdict: CLEAN WITH FIXES

Subject `093730e4`, whole product surface. Every claim below was RUN, in a scratch git repo built
from the shipped bytes, not reasoned about.

## The knob surface, enumerated first

Declared knobs read for this pass:

| carrier | keys that matter to this lens |
|---|---|
| `.memory-tree.conf` | `MEMORY_ROOT` (+ 20 pins/cutoffs) |
| `.codebase-map.conf` | `MAP_ROOT`, `GATE_FILE`, `MAP_DIFF_CMD`, `SEAM_FANIN_THRESHOLD`, `CLONE_COUNT_FILE` |
| `.lexicon.conf` | three offender pins, `LANGS`, `BANNED_SUFFIXES` |
| `.unattended.conf` | `MEMORY_ROOT`, `LANDER`, `GATE_CMD`, `GATE_BOUND`, `KICKOFF_ENGINE`, … |
| `tools/*/kit.toml` + `tools/govkit/entries/*.kit.toml` | `home`, `to = "{prefix}/…"`, `{kit}`, `{manifest_path}`, `{user_skills}` |
| declaration files | `tools/*-waivers.txt`, `tools/*-limits.txt`, `tools/*-highwater.txt`, `tools/run-gates/gate-profiles.txt` |

**No dead knob found (class (e)).** I traced a consumer for every one I suspected —
`CLONE_COUNT_FILE` (`tools/codebase-map/map_diff.py:131`), `RECALL_DARK_LAYERS`
(`tools/codebase-map/reuse_lookup.py:171`), `READ_PATH_WAIVER`
(`tools/memory-tree/corpus_ids.py:478`), `SEAM_FANIN_THRESHOLD` (`tools/codebase-map/map_lib.py:859`),
`AUTH_PARAM` (`tools/unattended/adopt-unattended.sh:146`), `RECALL_CACHE_BUDGET_MB`
(`tools/memory-recall/recall_conf.py:265`), `UNIVERSAL_BUDGET` (`tools/memory-tree/gotchas.py:285`),
`GATE_BOUND` (`tools/unattended/unattended.sh:188`). All live. That is a genuinely good result and
worth recording as a negative.

**What I found instead is class (d), in its nastiest shape: the knob exists, the deployer honours
it, and the ENGINE the deployer installs does not.** Four instances, all in the flat gates and the
kickoff ratchet. They share one root cause and one reason they were never caught, which is finding 5.

The reference implementation for doing it right is in this repo already, twice over:
`tools/run-gates/run-gates.sh:84` derives its manifest as `${GATE_LEGS:-$(dirname "$KITREL")/gate-legs.json}`
and `:178` derives its profile table the same way, each with an env override in front. Line 76 of
that file even names the class in prose: *"a hardcoded `tools/gate-legs.json` resolves to nothing at
any other prefix"*. And `tools/check-agent-cap-restatement.sh:74` reads `MEMORY_ROOT` out of
`.memory-tree.conf` with a fallback and a shape check. Both patterns are twenty lines away from the
defects below.

---

## F1 — `skills/session-kickoff/manifest-check.sh:33` · BLOCKER

The deployer asks the adopter where the manifest goes and then ships a ratchet that ignores the answer.

`tools/govkit/entries/kickoff-manifest.kit.toml:18` writes the seed to `to = "{manifest_path}"`. That
token is a target-supplied answer — `govkit.py:3175` records a past defect where `apply` with no
`manifest_path` answer wrote a file literally named `{manifest_path}`, so `plan` refuses an
unanswered one. Nothing anywhere constrains the value: `grep -n manifest_path` over `govkit.py`,
`registry.toml` and `WIRE-INTO-PROJECT.md` returns only that one comment and the descriptor line.

`manifest-check.sh:33` then hardcodes:

```
MANIFEST_LOCATIONS="memory/guides/SESSION-KICKOFF.md .claude/SESSION-KICKOFF.md"
```

with a header three lines above calling itself *"THE ONE LIST of places a kickoff manifest may
live"*. The file never opens `.memory-tree.conf` — `grep -c MEMORY_ROOT` returns 0.

The leg is `tools/govkit/entries/kickoff-manifest.kit.toml:37`,
`argv = ["bash", "{prefix}/manifest-check.sh"]`, `guard = []` — no path argument, no guard, so it
runs on **every** bar. And `kickoff-manifest` is in the registry's DEFAULT kit set
(`tools/govkit/registry.toml:36`), so this is not a conditional edge.

### Run

```
$ mkdir -p docs/mem/guides && git init -q .
$ printf 'MEMORY_ROOT=docs/mem\n' > .memory-tree.conf
$ cp MANIFEST-TEMPLATE.md docs/mem/guides/SESSION-KICKOFF.md
$ bash ./manifest-check.sh
MANIFEST env ERROR — no kickoff manifest at memory/guides/SESSION-KICKOFF.md,
.claude/SESSION-KICKOFF.md (and no valid path argument). Move an existing manifest to the first of
those, or run this script with --locations to see the list.
exit=2
$ bash ./manifest-check.sh --locations
memory/guides/SESSION-KICKOFF.md
.claude/SESSION-KICKOFF.md
```

The remedy the gate prints — *move it to the first of those* — instructs the adopter to abandon their
declared `MEMORY_ROOT` for this one file.

The script already accepts the path as `$1`, so the whole thing works when told:

```
$ bash ./manifest-check.sh docs/mem/guides/SESSION-KICKOFF.md
MANIFEST check 1 FAILED — unfilled {{PLACEHOLDER}} survives in docs/mem/guides/SESSION-KICKOFF.md
```

— that is the ratchet correctly grading a raw seed. The capability is there; the leg does not use it.

**Fix (smallest):** put `{manifest_path}` in the leg's argv at
`tools/govkit/entries/kickoff-manifest.kit.toml:37`. Durable: read `MEMORY_ROOT` at
`manifest-check.sh:33` the way `check-agent-cap-restatement.sh:74` does, and build the first location
as `$MEMORY_ROOT/guides/SESSION-KICKOFF.md`.

**What an adopter must change and cannot discover:** `skills/session-kickoff/manifest-check.sh` line
33, in the copy the deployer wrote into their tree. Nothing in `WIRE-INTO-PROJECT.md` mentions
`manifest_path` at all, and the gate's own `--locations` verb — the thing the runbook and the SKILL
point at instead of restating the list — prints the two literals as though they were the contract.

---

## F2 — `tools/check-testsuite-counts.sh:27` and `:28` · HIGH

Two hardcodes in one shipped gate, one per root:

```
27: MANIFEST=tools/gate-legs.json
28: WAIVERS=memory/project/testsuite-count-waivers.txt
```

The entry is `role = "engine"`, `to = "{prefix}/{relpath}"`
(`tools/govkit/entries/check-testsuite-counts.kit.toml:16`), and it is not conditional.

### Run — the install prefix half

Copied the shipped bytes into `vendor/gov/`, with the manifest where the run-gates kit actually puts
it at that prefix (`vendor/gov/gate-legs.json`):

```
$ bash vendor/gov/check-testsuite-counts.sh
testsuite-counts: no tools/gate-legs.json, so the population would be empty and this leg would pass
by finding nothing
exit=2
```

Exit 2 on every bar, forever. The gate's own header (`:16`) says *"THE POPULATION IS DERIVED from
`tools/gate-legs.json`, never hand-kept"* — it derives the population from the manifest and then
hand-keeps the path to the manifest.

There is a second, quieter half: the descriptor's guard at
`tools/govkit/entries/check-testsuite-counts.kit.toml:28` spells `"tools/gate-legs.json"` verbatim
while the sibling entry in the same list spells `{prefix}`. `govkit.py:4306-4317` DROPS a guard that
matches no tracked path in the target, so at a foreign prefix the leg is emitted with a partial guard
and runs more often, not less.

### The memory-root half

`MEMORY_ROOT` is read **zero** times in this file. `tools/check-agent-cap-restatement.sh:74-84` in the
same directory reads it, defaults it, and validates its shape. The descriptor's own
`why_no_adopter` (`:22`) admits the gap out loud: *"An adopter script would have to guess the memory
root's registry path, which the memory-tree kit already owns."* The knob is declared, the reading of
it is the thing that was skipped.

Consequence at `MEMORY_ROOT=docs/mem`: `[ -f "$WAIVERS" ]` at `:49` is false, `waived` is empty, and
the registry the gate's own docs tell the operator to seed by *"running the leg once and pasting what
it names"* can never be read. Every non-compliant suite reds with no waivable escape.

**Fix:** `MANIFEST=${GATE_LEGS:-$(dirname "$0")/gate-legs.json}` mirroring
`tools/run-gates/run-gates.sh:84`; read `MEMORY_ROOT` for `WAIVERS` the way the sibling gate does.

**Adopter-side file that would have to change:** `<prefix>/check-testsuite-counts.sh` lines 27–28,
plus `tools/govkit/entries/check-testsuite-counts.kit.toml:28`. Undiscoverable because the failure
prints as a population complaint (*"would pass by finding nothing"*), which reads as a manifest
problem rather than a path-resolution one.

---

## F3 — `tools/check-agent-cap-restatement.sh:54` · HIGH

```
54: WAIVERS=${1:-tools/agent-cap-restatement-waivers.txt}
```

The descriptor installs that registry at `to = "{prefix}/agent-cap-restatement-waivers.txt"`
(`tools/govkit/entries/check-agent-cap-restatement.kit.toml:22`) — the deployer knows the prefix
moves. The leg at `:39` is `argv = ["bash", "{prefix}/check-agent-cap-restatement.sh"]`, with **no
positional**. So the deployer writes the registry to one path and then invokes the engine in a way
that reads a different one. `:132` swallows the miss with `2>/dev/null`.

### Run — the full loop

```
$ git init -q . && printf 'MEMORY_ROOT=memory\n' > .memory-tree.conf
$ printf '# doc\n\nThe review fans out to at most 5 verify agents.\n' > DOC.md
$ printf 'at most 5 verify agents\tthe charter restatement, sanctioned\n' \
    > vendor/gov/agent-cap-restatement-waivers.txt

$ bash vendor/gov/check-agent-cap-restatement.sh          # exactly what the leg runs
AGENT-CAP-RESTATEMENT FAILED — live prose asserts a fan-out bound as a bare number.
  ... add a row to tools/agent-cap-restatement-waivers.txt
  DOC.md:3:The review fans out to at most 5 verify agents.
exit=1

$ bash vendor/gov/check-agent-cap-restatement.sh vendor/gov/agent-cap-restatement-waivers.txt
agent-cap-restatement: clean — 1 markdown file(s) scanned, 1 waiver(s)
exit=0
```

The registry the deployer installed one command earlier is invisible, and **the printed remedy names
a path that does not exist in the adopter's tree**. Following it creates a stray `tools/` directory
outside their chosen install prefix — the exact outcome `check-install-prefix.sh`'s own header
describes as the measured damage this whole gate family was built to prevent.

Same file, `:74`, reads `MEMORY_ROOT` from the conf correctly. One root parametric, the other not, in
one script.

**Fix:** `argv = ["bash", "{prefix}/check-agent-cap-restatement.sh", "{prefix}/agent-cap-restatement-waivers.txt"]`,
or default `WAIVERS` to `$(dirname "$0")/agent-cap-restatement-waivers.txt`. Either is one line.

Mitigation: the entry is `selectable = "conditional"`, so fewer adopters hit it than F1.

---

## F4 — `tools/check-install-prefix.sh:33`, `:46`, `:129` · HIGH

The gate that owns this defect class carries three instances of it and fails CLOSED in any adopter
not installed at `tools`.

```
 33: WAIVERS="tools/install-prefix-waivers.txt"
 46: kits=$(git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u)
129: CARRIED="tools/install-prefix-carried.txt"
```

Both declaration files are shipped to `to = "{prefix}/install-prefix-waivers.txt"` and
`to = "{prefix}/install-prefix-carried.txt"` (`tools/govkit/entries/check-install-prefix.kit.toml:26,32`)
— the descriptor moves them with the prefix, the engine looks for them at a fixed `tools/`. Same
shape as F3.

Line 46 is worse than a bad default: it is the gate's liveness assertion input, and at any other
prefix it derives an empty kit set and the gate short-circuits.

### Run

```
$ bash vendor/gov/check-install-prefix.sh
install-prefix: no kit directories under tools/ — that is not a pass
exit=1
```

The leg is `subject = "repo"` with `guard = []` (`check-install-prefix.kit.toml`, last block), so it
runs on every bar of any adopter that selects the kit, and reds every time. The message names no fix,
because from inside the script this state is indistinguishable from a broken repo.

**Relation to the tracked row.** `DEPL-dCarriedReceipt-15` (SPECCED) already asks for
*"make check-install-prefix.sh prefix-parametric"*. This is not a new ask — what is new is the
measured consequence, which that row does not record: the gate does not degrade, it hard-exits 1 on a
`guard = []` repo-subject leg, so the outcome for such an adopter is a permanently red merge bar
rather than reduced coverage. Worth carrying into the row before it is built.

---

## F5 — the structural blind spot in `tools/check-install-prefix.sh` · MEDIUM

*Why F1–F4 were never caught, which the task asked for explicitly.*

Both arms bind a **kit-directory segment** and an extension from a five-member set:

```
 46: kits=$(git ls-files -- 'tools/*/*' | awk -F/ 'NF>2 {print $2}' | sort -u)     # $alt
 63: RE="(^|[^/{}[:alnum:]._-])($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"     # arm 1, ROOT spelling
175: re_ship="(^|[^/{}[:alnum:]._-])tools/($alt)/[A-Za-z0-9_.-]+\.(sh|py|js|md|json|toml)"  # arm 2, SHIPPING spelling
```

Two consequences, neither of which the header's *"nothing this repo SHIPS may spell a root-install kit
path"* prepares a reader for:

1. **A literal naming a LOOSE file directly under `tools/` has no kit segment, so neither arm can
   see it.** That is every `tools/check-*.sh`, `tools/gate-legs.json`, `tools/push-main.sh`,
   `tools/settings-merge.py`, and every `tools/*-waivers.txt` / `*-limits.txt` / `*-highwater.txt`.
   Measured over the gate's own arm-2 population (the 182 descriptor-resolved sources, re-derived
   with the gate's own snippet): **55 shipped files carry at least one**, led by
   `tools/memory-tree/check-arms.py` (27), `tools/govkit/registry.toml` (15) and
   `tools/check-install-prefix.sh` itself (7).
2. **`.txt`, `.tsv`, `.example` and `.conf` are outside the extension alternation**, so a kit-dir
   path such as `tools/run-gates/gate-profiles.txt` is invisible too.

The two together are exactly why `WAIVERS="tools/install-prefix-waivers.txt"` sits unflagged on line
33 of the gate itself, and why F1, F2 and F3 are all currently green.

Both arms already assert liveness on their POPULATION (`:47`, `carried_live()`), which is right and
which is why the gate reads as trustworthy — but a population assertion says nothing about predicate
coverage. This is `memory/gotchas/` territory: the check is structural and reads as semantic to
everybody who did not write it.

**Fix, small and testable:** widen the extension class to include `txt|tsv|conf|example`, and add a
third arm keyed on `tools/<loose-file>` where the loose-file set is DERIVED from
`git ls-files -- 'tools/*' | grep -v /` — same derivation discipline as `$alt`, no new list. Run it
over the tree with `--list` before wiring it (the gate's own header prescribes exactly this), seed
the ratchet, and let it shrink. Expect ~55 rows on day one.

---

## Also looked at, NOT reported

- `.githooks/pre-push:195,203` hardcodes `tools/gate-legs.json` and both predicates fail open at a
  foreign prefix. **Already `TOOL-aBoundedCeiling-7`, OPEN.** I re-verified it is still live and the
  row's description is exactly right: `git diff --quiet A B -- <absent-path>` returns 0 (measured),
  and `git hash-object -- <absent-path>` returns empty (measured), so predicates 6 and 7 silently
  never fire. Nothing to add.
- `tools/check-line-length.sh:49` `DECL=${DECL:-tools/line-length-limits.txt}` — same class, but it
  has an env override, it announces the miss (`:124` *"NOT ADOPTED — no declaration at $DECL"*) rather
  than passing silently, and the descriptor deliberately does not ship the declaration. A skip that
  announces itself. Low; not worth a row on its own, but it is the fourth member of the family and
  should ride along with whatever fixes F2–F4.
- `tools/drift-audit/drift_signals.py` hardcodes six `memory/…` paths, but it is
  `role = "project-owned"` (`tools/drift-audit/kit.toml:14-15`) and never lands — the adopter gets
  `drift_signals.template.py`. Not a defect. Noting it because the gate's arm-2 population DOES
  include withheld `project-owned` sources, which inflates the ratchet with files no adopter
  receives. Strictness in the safe direction; mentioned, not filed.
- `tools/memory-tree/*` renders naming `memory/` at a renamed root: already `TOOL-aSealedCaravan-4`.
- `tools/install-prefix-waivers.txt` line-number keying: already `TOOL-aSealedCaravan-1`,
  `TOOL-aLoosenedCeiling-5`, `TOOL-dSpentCeiling-6`.
- `--write-ratchet` fixed point: already `TOOL-dTieredTribunal-27`.

## Commands run

```
bash tools/check-install-prefix.sh                       # clean: 170 shipped files, 12 waivers
python - <<…>  # re-derived the arm-2 shippable set: 183 sources
bash vendor/gov/check-install-prefix.sh                  # exit 1
bash vendor/gov/check-testsuite-counts.sh                # exit 2
bash vendor/gov/check-agent-cap-restatement.sh           # exit 1, waiver invisible
bash vendor/gov/check-agent-cap-restatement.sh <path>    # exit 0, 1 waiver
bash ./manifest-check.sh                                 # exit 2 at MEMORY_ROOT=docs/mem
bash ./manifest-check.sh docs/mem/guides/SESSION-KICKOFF.md   # grades it correctly
git diff --quiet HEAD~1 HEAD -- tools/gate-legs.json     # exit 0 on an absent path
git hash-object -- tools/gate-legs.json                  # empty on an absent path
```

Scratch trees under the session scratchpad (`…/scratchpad/adopter`, `…/ac`, `…/mc`); nothing was
written into this repo except this file.
