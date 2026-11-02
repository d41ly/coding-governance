# TOOL-dFoldedAudit-18 — the help page for the spec-audit switches and the chain verbs, so the docs leg anchors them

**Status:** INPROGRESS · rev-1 · 2026-11-02 · node d · Tier-1 · base 84acebdc · streams tooling · order 180

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dFoldedAudit-18-1-spec-return.md](../build/2026-11-02-build-TOOL-dFoldedAudit-18-1-spec-return.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-18-1-spec-writer.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-18-1-spec-writer.md) | journal | — |
| [2026-11-02-prompt-TOOL-dFoldedAudit-18-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dFoldedAudit-18-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The `docs` leg, which reached this branch with the landing merge `30396a42`, prints `UNDOCUMENTED` for
five members this build added. One new page under `help/` documents the three spec-audit policy keys
and the two chain verbs and anchors each member once, so the leg passes with no row added to the
shrink-only list.

## 2. Scope (IN)

- **S1** — A new page, `help/spec-audit.md`, says what a spec-audit chain is, how to record a round and
  ask its verdict, and what each value of each key does. It takes every fact from the sources §4
  names and states no other. Observed by AC1 and AC2.
- **S2** — The page carries the five usage anchors of §4's table, each once, outside any fence, with
  the fingerprint its row has. No other page carries them. Observed by AC1 and AC3.
- **S3** — The page's command lines name only declared verbs and flags, and its relative links reach
  tracked paths. Observed by AC2.
- **S4** — `help/README.md` lists the page, one bullet after the docs-leg bullet. Observed by AC4.
- **S5** — The pass commit is one single-parent commit on top of the landing merge, touching the two
  help files alone, and ends with the charter's trailer. Observed by AC5.

## 3. Non-goals (OUT)

- Any change to a member's behaviour, its catalogue row, its usage line or its verbs-guide entry.
- A row added to, or removed from, `memory/project/docs-undocumented.txt`. None of the five is
  listed there, so anchoring them drains nothing.
- Any write outside `help/` beyond this spec. That includes `help/policy.md`, whose consumer sentence
  §7's F1 raises, and `tools/govkit/usage.toml`, since all five rows come from readers.
- A second merge, a rebase or an amend of the landing merge. The landing refuses a second merge.
- Running the `docs` leg inside the pass. A role agent runs no gate; the main loop runs it after the
  pass, as §6 says.
- This spec's status flip, its acceptance ledger and the commit of this spec. They are the main loop's.

## 4. Design

Line numbers are this tree's at `f1b6d71b`, PINNED 2026-11-02.

### The five members

Each row comes from a reader, not from `tools/govkit/usage.toml`: the keys from the policy catalogue
(`tools/govkit/docs_leg.py:106-112`), the verbs from the driver's usage lines
(`tools/govkit/docs_leg.py:115-153` over `tools/unattended/unattended.sh:31-32`). A fingerprint is
the first eight hex of the SHA-256 of the row less its id (`tools/govkit/docs_leg.py:83-86`). The
leg reds an anchor whose fingerprint differs (`:425-426`), a member anchored twice (`:427-429`) and
a member no page anchors and the list does not name (`:437-438`).

| Member | Row fields | Fingerprint | Section of the page |
|---|---|---|---|
| `policy:review.spec-audit.disposal` | default `by-nature`, values `by-nature` `promote-all` | `d6f3b3b9` | How a round disposes |
| `verb:unattended.sh:--record-round` | flags `--audited`, `--blockers=`, `--finding=`, `--highs=`, `--sibling=`, `--subject=` | `60847ce3` | Recording a round |
| `verb:unattended.sh:--chain-verdict` | no flags | `5fdc7c80` | Asking the verdict |
| `policy:review.spec-audit.chain-stop` | default `own-work`, values `own-work` `clean-only` | `b0668fc2` | When a chain stops |
| `policy:review.spec-audit.chain-ceiling` | default 4, a round count, min 1 | `35f3e681` | The ceiling |

The fingerprints are PINNED, derived 2026-11-02 at `f1b6d71b` by calling the leg's own
`derive_usage_fingerprint` over its own readers. The probe below re-derives them, and a row that
has moved since takes the probe's value. Each anchor is spelled as the docs-leg page shows it,
`<!-- usage: <id> <fingerprint> -->`, on the line that introduces the member, the way
`help/docs-leg.md` anchors `help.enforce`.

### The page

The shape is `help/docs-leg.md`'s: a bold **What it is.** paragraph, then task sections, a table
per key with one row per value, and a closing section on what it does not do. Hard-wrap near 100
columns. The sections, in order, and the source each takes its facts from:

| Section | What it says | Source |
|---|---|---|
| title and What it is | a declared spec audit disposes each round's confirmed findings, and the chain of rounds stops on a derived verdict; three keys switch it and two driver verbs record and answer | `memory/guides/BUILD-METHOD.md:146-148` |
| When a chain runs | an audit is owed only where the build's README declares `spec-audit:` or `.unattended.conf` declares `SPEC_AUDIT_DEFAULT`, and the opt-in is the owner's | `memory/guides/BUILD-METHOD.md:117-120` |
| How a round disposes | LOCAL and NEW MECHANISM as M4 defines them; a local finding, a BLOCKER too, folds into each spec it touches with a rev bump and a revision-log line; a new-mechanism finding is promoted, a BLOCKER or HIGH to its own unit, MEDIUMs and LOWs batched; a repair edits an unbuilt sibling's spec and a CLOSED spec stays frozen; then the disposal table | `memory/guides/BUILD-METHOD.md:146`, `memory/guides/UNATTENDED-VERBS.md:860-871` |
| Recording a round | the `--record-round` command, the `--finding` row grammar and its closed severities and natures, `--sibling`, the one append-only chain record and its file name, who commits it, and what it refuses | `memory/guides/UNATTENDED-VERBS.md:280-294`, `tools/unattended/unattended.sh:1172-1174` |
| Asking the verdict | the `--chain-verdict` command, its one output line, the three words and five reasons in M4's order, and what to do on each word, the HOLD recipe included | `memory/guides/UNATTENDED-VERBS.md:295-307`, `memory/guides/BUILD-METHOD.md:148` |
| When a chain stops | the chain-stop table | `memory/guides/UNATTENDED-VERBS.md:310-316` |
| The ceiling | the round that HOLDs for the owner; raising it loosens; it is no `CEILING` state | `memory/guides/UNATTENDED-VERBS.md:311-313`, `memory/guides/UNATTENDED-VERBS.md:872-874`, `tools/policy/catalogue.toml:749-755` |
| Reading and setting the keys | read with `policy.py get <key>`; with no policy kit each key takes its kit default with a note; a value outside the closed set refuses; only the owner moves the guarded policy file | `tools/unattended/unattended.sh:1440-1467`, `help/policy.md:149` |
| What it does not change | a closing diff review still disposes by severity, and the verdict is computed once, in the driver | `memory/guides/BUILD-METHOD.md:144`, `memory/guides/UNATTENDED-VERBS.md:307` |

The three key tables:

| Key | Value | What it does |
|---|---|---|
| `review.spec-audit.disposal` | `by-nature`, the default | the nature rule above, for a spec exit past `SPEC_FOLD_CUTOFF` |
| | `promote-all` | the rule before: every confirmed finding is promoted |
| `review.spec-audit.chain-stop` | `own-work`, the default | the clean stop and, from round 2, the own-work stop |
| | `clean-only` | the clean stop alone |
| `review.spec-audit.chain-ceiling` | 4, the default; a round count, at least 1 | at that round a chain neither stop ended HOLDs for the owner |

The page names `SPEC_FOLD_CUTOFF` in `.unattended.conf` and does not restate its date, so the one
value lives in the conf (`.unattended.conf:489`). The verdict's output line is quoted from
`memory/guides/UNATTENDED-VERBS.md:297` in a `text` fence, which the leg does not test.

### What the leg tests on the page

A `bash`, `sh` or `console` fence line, and an inline span opening `python`, `python3` or `bash`,
is tested as a command (`tools/govkit/docs_leg.py:253-300`). The page's command lines are these
two, in a `bash` fence, copied from the usage lines:

```bash
bash tools/unattended/unattended.sh --record-round <slug> --subject <s> --audited "<ids>" --blockers <b> --highs <h> --finding <id>/<severity>/<nature>/<spec>[,<spec>]/<unit>/<rev> --sibling <unit>@rev-<n>
bash tools/unattended/unattended.sh --chain-verdict <slug>
```

They split onto two fences if the sections need it. `--audited` is declared without a value, so the
page spells it `--audited "<ids>"` and never `--audited=` (`:331-335`). Every other command the page
names, `policy.py get <key>` and the HOLD recipe's `--park` and `--handoff`, sits in an inline span
that does not open with an interpreter, so it is prose to the leg. Relative links stay inside
`help/`, to `policy.md` and `docs-leg.md` with no fragment. The method guides are named as backticked
paths, not links, so a heading renamed there cannot red this page.

Both lines were trial-run on 2026-11-02 through the leg's own `read_page_commands` and
`check_page_command`, each answering `tested`, and both links through `check_page_links`, with no
finding.

### The index

`help/README.md:15` is the docs-leg bullet. The new bullet follows it, in the same shape: a markdown
link whose text is `Spec-audit chains` and whose target is the bare file name `spec-audit.md`, then
an em dash and this description:

```text
how a spec audit's round disposes its findings, how `--record-round` and `--chain-verdict` record a round and answer CONTINUE, STOP or HOLD, and what `review.spec-audit.disposal`, `.chain-stop` and `.chain-ceiling` do.
```

The link is described rather than shown because this spec sits where the hygiene gate's link check
would resolve it against the spec folder.

### The probe

Probe A, `probe.py` in `P="$TEMP/dFoldedAudit-18-probes"`, run from the worktree's root, calls the
leg's own functions and runs no gate. It prints one `anchor` line per member, one `command` line per
command the page shows, and one `links` line with the findings after the count.

```python
import pathlib, subprocess, sys
sys.path.insert(0, "tools/govkit")
import docs_leg as d
IDS = ["policy:review.spec-audit.chain-ceiling", "policy:review.spec-audit.chain-stop",
       "policy:review.spec-audit.disposal", "verb:unattended.sh:--chain-verdict",
       "verb:unattended.sh:--record-round"]
verbs = d.read_verb_usage(".")
rows = {**{f"policy:{k}": v for k, v in d.read_policy_usage(".").items()},
        **{f"verb:{k}": v for k, v in verbs.items()}}
anchors = [a for p in sorted(pathlib.Path("help").glob("*.md"))
           for a in d.read_page_anchors(p, p.as_posix())]
for i in IDS:
    at = [(rel, fp) for rel, _n, aid, fp in anchors if aid == i]
    good = len(at) == 1 and at[0][1] == d.derive_usage_fingerprint(rows[i])
    print("anchor", i, len(at), at[0][0] if at else "-", "ok" if good else "BAD")
page = pathlib.Path("help/spec-audit.md")
by_entry = {}
for r in verbs.values():
    by_entry.setdefault(r["entry"], {})[r["verb"]] = set(r["flags"])
tracked = set(filter(None, subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True,
                                          encoding="utf-8").stdout.split("\0")))
for n, cmd in d.read_page_commands(page):
    print("command", n, *(d.check_page_command(cmd, by_entry, tracked, "tools") if cmd else ("split", "-")))
checked, _ext, found = d.check_page_links(".", page, "help/spec-audit.md", tracked)
print("links", checked, *found)
```

At `f1b6d71b` the five anchor lines read `0 - BAD`, observed 2026-11-02 over a scratch page.

### The brief's acceptance

The brief's first item, the leg exiting 0 with none of five finding words, is the `docs` leg's own
run, which §6 hands to the main loop. AC1 and AC2 observe the same three predicates in the pass. The
brief's second item spells `--undocumented` alone, which the leg answers with its usage line and exit
2 (`tools/govkit/docs_leg.py:710`, `:737-739`), so AC3 spells `--list --undocumented`.

### Files touched (estimate)

`help/spec-audit.md`
`help/README.md`

### Alternatives rejected

- **Listing the five in `memory/project/docs-undocumented.txt`.** The list only shrinks, and the leg
  reds a list above its low-water.
- **Anchoring the keys on `help/policy.md`.** The leg anchors each member on one page, and the keys
  only mean something beside the verbs that read them. That page is also under the `policy fixtures`
  guard.
- **A `[[usage]]` row for each verb.** The driver's usage lines already state them, and the leg reds a
  row that restates a registry (`RESTATED`).

## 5. Acceptance criteria

Run from the worktree's root, with `P` set as §4 sets it and probe A written there.

- **AC1** — When `python "$P/probe.py"` runs after the page is written, it prints five `anchor` lines,
  each with the count `1`, the new page's path and `ok`.
  figure: DERIVED, each fingerprint re-derived by `derive_usage_fingerprint` at observation.
  Red when: a member is anchored on no page, on two, inside a fence, or with a fingerprint other than
  its row's, which the leg would print as `UNDOCUMENTED`, `TWICE` or `STALE`.
- **AC2** — When `python "$P/probe.py"` runs, every `command` line it prints ends `tested` and names
  `tools/unattended/unattended.sh`, there are at least two, and the `links` line carries a count and
  nothing after it.
  Red when: a line spells an undeclared flag such as `--audited=`, an undeclared verb, a command the
  shell grammar cannot split, or a link to an untracked path, which the leg would print as `COMMAND`,
  `SPLIT` or `LINK`.
- **AC3** — When `python tools/govkit/docs_leg.py --list --undocumented | grep -c -e review.spec-audit -e unattended.sh:--record-round -e unattended.sh:--chain-verdict`
  runs, it prints 0.
  figure: PINNED, it prints 5 at `f1b6d71b`, measured 2026-11-02.
  Red when: any of the five is still anchored on no page.
- **AC4** — When `grep -c '(spec-audit[.]md)' help/README.md` runs, it prints 1.
  Red when: the index does not list the page, or lists it twice.
- **AC5** — On the pass commit, `git rev-list --parents -1 HEAD` prints two shas, the second
  `30396a42` or a commit descending from it, and `git diff --name-only HEAD~1 HEAD` prints the index
  and the new page alone. `git diff --quiet HEAD~1 HEAD -- memory/project/docs-undocumented.txt`
  exits 0, and `git log -1 --format=%B` ends with
  `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>`.
  Red when: the pass is a merge, touches a third path, edits the list, or lacks the trailer.

## 6. Gates

`docs`

The main loop runs the `docs` leg after the pass, and it must exit 0 printing no `UNDOCUMENTED`,
`STALE`, `COMMAND`, `LINK` or `TWICE` line. No §4 path sits under a leg's guard: `help/policy.md` is
the only help page any guard names, under `policy fixtures`, and this unit does not touch it. No arm is
added or moved.

## 7. Open questions

- **F1 — Does this unit also correct `help/policy.md`'s consumer sentence?** Lines 8-14 there say two
  key families have consumers and that any other key's value changes no behaviour today. The driver
  now reads all three spec-audit keys (`tools/unattended/unattended.sh:1455-1458`), so the sentence is
  wrong for them, as it already was for `help.enforce`.
  - (a) Leave it. The brief asks for one new page, `help/policy.md` sits under the `policy fixtures`
    guard, and the sentence's staleness predates this build. The main loop reports it as a follow-up.
  - (b) Add one clause naming the spec-audit keys and linking the new page. It widens the write set
    to a third file and owes `policy fixtures` on §6's line.
  - Recommendation: (a), because the sentence is stale for a key this build did not add, so its fix
    is a class fix for another unit, not a clause here.
  - RESOLVED (agent, 2026-11-02, delegated): (a), leave `help/policy.md:8-14` unchanged, because the
    main loop takes the sentence's staleness as a wrap-up follow-up rather than this unit's work.

## 8. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 9. Reuse audit

The seam is the docs leg's own anchor grammar and the page shape of `help/docs-leg.md` and
`help/policy.md`, both read above. `reuse_lookup.py` ranked name stems only, `key`, `leg`, `anchors`
and `usage`, none a page, so no code seam fits and none is built. The handoff's list names this
build's earlier seams, `verb_review`, the DISPOSAL stage, check 2's awk, `deviation_join.scan` and
`derive_past_pin_ids`, and none sits on a help page's path.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "a help page documenting policy keys and driver verbs with usage anchors for the docs leg"`.
Recall terms used: `python tools/memory-recall/query.py "how is a new help page written so the docs leg anchors an undocumented member" --terms "help page usage anchor fingerprint docs leg UNDOCUMENTED docs-undocumented.txt help.enforce help/README.md shrink-only"`.
