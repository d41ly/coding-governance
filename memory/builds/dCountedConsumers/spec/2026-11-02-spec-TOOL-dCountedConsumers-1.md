# TOOL-dCountedConsumers-1 — help/policy.md names every policy key family a reader consumes today

**Status:** CLOSED · rev-1 · 2026-11-02 · node d · Tier-1 · base 8bec4cef · streams tooling · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCountedConsumers-1-1-builder-return.md](../build/2026-11-02-build-TOOL-dCountedConsumers-1-1-builder-return.md) | journal | — |
| [2026-11-02-prompt-TOOL-dCountedConsumers-1-brief.md](../prompts/2026-11-02-prompt-TOOL-dCountedConsumers-1-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`help/policy.md` says that only the agent limit and the size caps have consumers. That has been wrong
since `help.enforce` gained a reader. Since dFoldedAudit landed, it is also wrong for the three
`review.spec-audit` keys. Its consumer paragraph will name every key family a reader consumes today,
each with one link to the page that documents it. The paragraph will also keep its last claim true:
a value set for any other key is checked but changes no behaviour.

## 2. Scope (IN)

- **S1** — The consumer paragraph, `help/policy.md:8-15`, is rewritten. It becomes one opening
  sentence and a list of the eight key families in §4's table. Each family's bullet names its keys
  in backticks and says what reads them. It carries exactly one link, to the page in the table.
  Observed by AC1.
- **S2** — After the list, a closing sentence keeps the paragraph's last claim in a true form. Every
  other key has no consumer yet, and the build its catalogue row names as `owner` adds one. So a
  value set for any other key today is checked but changes no behaviour. The invalid-file exception
  stays. Observed by AC2.
- **S3** — The page's usage anchors are unchanged, so the `docs` leg has nothing STALE or TWICE to
  report. The region tests no command beyond the one on line 8, and every link resolves. Observed by
  AC3.
- **S4** — Only the paragraph moves. No other line of `help/policy.md` changes, `## Install`
  included, so the `policy fixtures` leg reads the same section. No other file changes. Observed by
  AC4.

## 3. Non-goals (OUT)

- BUILD-METHOD M6's dispatch sentence. TOOL-dIndexedDesign-36 owns it (owner, 2026-11-02).
- HYGIENE's deviation paragraph (owner, 2026-11-02).
- Any catalogue row, usage line or key behaviour, and any reader added or removed.
- Any other part of `help/policy.md`. That includes the reader-coverage section at
  `help/policy.md:119-147` and the keys table at `:206-213`.
- A usage anchor for any key on this page. Each consumed key is already anchored once, on the page
  §4's table links. A second anchor is the `docs` leg's TWICE finding.
- `tools/policy/README.md:686-688`, which makes the same stale claim: "No consumer reads the file
  yet". It is a separate document under a routed kit path, so by M2 it is a separate unit. Whoever
  dispatched this unit reports it as a follow-up.
- The reader-coverage scan crediting `verdict` as read. It matches `dict.get("verdict")` calls in
  `tools/run-gates/held_halves.py:182` and `tools/run-gates/measure_legs.py:2728`, which is the blind
  spot `help/policy.md:145-147` already states. Its owner, dWitnessedBar, has 88 specs, all
  `DEFERRED`. This unit does not name it and does not change the scan.
- A gate that joins this paragraph's family list to the reader set. It would be a separate mechanism
  (M2). See §4 Limitations.
- Running the `docs`, `policy fixtures` or `memory hygiene` leg inside the pass. The main loop runs
  them at the close (§6).

## 4. Design

Line numbers are this tree's at `201ac868`, PINNED 2026-11-02. `help/policy.md` is byte-identical
at the base `8bec4cef`, because the build's only commit since adds records.

### The consumed keys, derived from the readers

The reader-coverage arm's own scan, `scan_reader_keys` and `check_key_read`
(`tools/policy/check_policy.py:481-517`), was run over the tracked tree on 2026-11-02. It credits 14
of 270 catalogue keys as read. Thirteen are real consumers, each verified at its call site:

| Family | Keys | Read at | Its page |
|---|---|---|---|
| the agent limit | `runtime.agents-in-flight` | `tools/hooks/agent-cap.js:469`, `:1801`; rendered into settings by `tools/policy/policy.py:951` | `agent-limit.md` |
| the size caps | `budgets.enforce`, `budgets.pinned`, `budgets.<cap>` | `tools/policy/budgets.py:240`, `:270` | `size-caps.md` |
| the docs leg | `help.enforce` | `tools/govkit/docs_leg.py:727` | `docs-leg.md` |
| spec-audit chains | `review.spec-audit.disposal`, `.chain-stop`, `.chain-ceiling` | `tools/unattended/unattended.sh:1456-1458` | `spec-audit.md` |
| forwarders | `install.on-shim-call`, `install.deprecation-window` | `tools/govkit/shims.py:111`, `:138`, `:358` | `shims.md` |
| retired edits | `install.retired-edits` | `tools/govkit/govkit.py:9282` | `update-edits.md` |
| the Python floor | `platforms.provision` | `tools/lib/resolve-python.sh:137`, and the inlined copy of that block in every script that carries it | `python-floor.md` |
| the invalid file | `policy-file.on-invalid` | `tools/policy/policy.py:652`, `:674` | this page, `#how-to-use-it` |

The 14th is `verdict`, which §3 excludes. The brief named the first four families. Its item 1 says to
verify against the readers and add any other consumer found, so the last four are added on that
instruction, not as a choice. Each page in the last column already carries the `policy:` usage anchor
for its keys (`help/agent-limit.md:3`, `help/size-caps.md:5-11`, `help/docs-leg.md:59`,
`help/spec-audit.md:42`, `:119`, `:133`, `help/shims.md:11`, `:46`, `help/update-edits.md:12`,
`help/python-floor.md:52`, `help/policy.md:61`). That makes each page the documented home of its
keys.

### The rewritten paragraph

Line 8 keeps its first sentence and its anchor, `<!-- usage: script:tools/policy/policy.py#get af650e87 -->`,
at the end of the same line. The docs leg reads an anchor on the line that introduces its member.
The rest of line 8 and lines 9-15 are replaced by:

1. **A lead-in.** Line 8 continues and line 9 finishes it, saying these keys have consumers today,
   each documented on its own page.
2. **The list.** One `- ` bullet per family, in the table's order. A bullet names the keys in
   backticks, then says in one clause what reads them, then gives the link. The clauses follow the
   table: the agent-cap hook and `policy.py settings --write`, every gate that enforces a size cap,
   the docs leg, the unattended driver, a forwarder and gov's forwarder hold, `update`, the Python
   resolver, and the reader itself.
3. **The closing sentence**, S2's claim, followed by the existing exception sentence unchanged: "The
   one exception is an invalid file, which the push gate refuses when it has nothing to fall back
   to, below."

The link texts follow the pointer style the page already uses, lowercase and parenthesised:

| Link text | Target |
|---|---|
| the agent limit | `agent-limit.md` |
| the size caps | `size-caps.md` |
| the docs leg | `docs-leg.md` |
| spec-audit chains | `spec-audit.md` |
| forwarders for a moved path | `shims.md` |
| what update does with your edits | `update-edits.md` |
| the Python floor | `python-floor.md` |
| below | `#how-to-use-it` |

`#how-to-use-it` is the slug of `## How to use it` (`help/policy.md:20`), the section whose bullet at
`:59-74` documents `policy-file.on-invalid`. `#install` at `:86` is the in-page precedent. Three
spelling rules follow from how the leg reads a page:

- **Each link sits on one line.** `check_page_links` matches a link line by line
  (`tools/govkit/docs_leg.py:354-373`), so a link that wraps is never checked.
- **No inline span opens with `python`, `python3` or `bash`.** The leg tests such a span as a
  command (`tools/govkit/docs_leg.py:253-300`), and the region should test only line 8's.
  `policy.py settings --write` stays as the page spells it today.
- **No `<!-- usage: ... -->` anchor is added.** See §3.

The size-caps family spells `budgets.<cap>`, as the page already does. Its catalogue key is
`budgets.*`. Hard-wrap near 100 columns. No size cap or line-length gate grades `help/policy.md`: it
is in no budgets row, and 22 of its lines already exceed 100.

### The probe

Probe A is `probe.py` in `P`, the pass's own scratch directory, spelled absolute. It runs from the
worktree's root. It calls the reader-coverage scan and the docs leg's own functions and runs no gate.
It prints:

- one `read` line, with the count of keys the scan credits and any read key the family table does
  not list (`none` when there is none);
- one `family` line per family, saying `named` or `MISSING` and how many links the region carries to
  that family's target;
- a `region` line, giving the region's bounds, the count of "Two families" and the count of the
  closing claim;
- an `anchors` line, a `commands` line and a `links` line.

The region runs from the line carrying the `policy.py#get` anchor to the line before
`The kit README,`.

```python
import pathlib, re, subprocess, sys
sys.path[:0] = ["tools/policy", "tools/govkit"]
import check_policy as c, policy, docs_leg as d
FAMILIES = [  # (catalogue keys, the spelling the page uses, the link target)
    (["runtime.agents-in-flight"], ["runtime.agents-in-flight"], "agent-limit.md"),
    (["budgets.enforce", "budgets.pinned", "budgets.*"], ["budgets.enforce", "budgets.pinned", "budgets.<cap>"], "size-caps.md"),
    (["help.enforce"], None, "docs-leg.md"),
    (["review.spec-audit.disposal", "review.spec-audit.chain-stop", "review.spec-audit.chain-ceiling"], None, "spec-audit.md"),
    (["install.on-shim-call", "install.deprecation-window"], None, "shims.md"),
    (["install.retired-edits"], None, "update-edits.md"),
    (["platforms.provision"], None, "python-floor.md"),
    (["policy-file.on-invalid"], None, "#how-to-use-it"),
]
NOT_CONSUMED = {"verdict"}  # dict .get("verdict") calls the scan credits; owner dWitnessedBar is DEFERRED
rows = policy.load_catalogue(c.KIT)
names = {str(r["name"]) for r in rows}
spelled = c.scan_reader_keys(".", c.KIT)
read = {k for k in names if c.check_key_read(k, spelled, names)}
listed = {k for keys, _s, _t in FAMILIES for k in keys}
print("read", len(read), "unlisted", *(sorted(read - listed - NOT_CONSUMED) or ["none"]))
page = pathlib.Path("help/policy.md")
lines = page.read_text(encoding="utf-8").split("\n")
a = next(i for i, ln in enumerate(lines) if "usage: script:tools/policy/policy.py#get" in ln)
b = next(i for i, ln in enumerate(lines) if ln.startswith("The kit README,"))
region = "\n".join(lines[a:b])
spans = set(re.findall(r"`([^`\n]+)`", region))
links = re.findall(r"\]\(([^)\s]+)\)", region)
for keys, spell, target in FAMILIES:
    print("family", target, "named" if all(s in spans for s in (spell or keys)) else "MISSING", "links", links.count(target))
print("region", a + 1, b, "two-families", region.count("Two families"),
      "closing", len(re.findall(r"checked\s+but\s+changes\s+no\s+behaviour", region)))
print("anchors", *sorted(f"{aid} {fp}" for _r, _n, aid, fp in d.read_page_anchors(page, "help/policy.md")))
print("commands", *[n for n, _cmd in d.read_page_commands(page) if a < n <= b])
tracked = set(filter(None, subprocess.run(["git", "ls-files", "-z"], capture_output=True, text=True,
                                          encoding="utf-8").stdout.split("\0")))
checked, _ext, found = d.check_page_links(".", page, "help/policy.md", tracked)
print("links", checked, *found)
```

On today's page, observed 2026-11-02 at `201ac868`, the probe prints `read 14 unlisted none`. The
first two `family` lines read `named links 1` and the other six `MISSING links 0`. The rest read
`region 8 16 two-families 1 closing 1`, `commands 8` and `links 3`. The `anchors` line names seven
anchors:

| Anchor | Fingerprint |
|---|---|
| `policy:policy-file.on-invalid` | `89965eb1` |
| `script:tools/policy/adopt-policy.sh` | `f6cd6f1b` |
| `script:tools/policy/check_policy.py` | `49bb87e8` |
| `script:tools/policy/policy.py#check` | `a787d169` |
| `script:tools/policy/policy.py#get` | `af650e87` |
| `script:tools/policy/policy.py#lists` | `54ff8bae` |
| `script:tools/policy/policy.py#mirror` | `f4887510` |

The `unlisted` half is live: delete any row from `FAMILIES` and that row's keys print there.

### Limitations

The list is typed beside the readers it describes, the `two-answers-to-one-question` class. A build
that adds a reader leaves the list one family short until someone edits it. The reader-coverage arm
guards the opposite direction only, a landed key with no reader. Probe A's `unlisted` half is the
join that would catch it, but here it runs once, at this pass. Gating it is a separate unit (§3).

### Files touched (estimate)

`help/policy.md`

### Alternatives rejected

- **A table in place of the list.** The page already uses `- ` bullets for task lists, and a bullet
  keeps each family's link on one line at this width. A table row would carry four keys, a reader
  clause and a link, and run past 200 columns.
- **Anchoring the newly named keys on this page.** Each key is already anchored once elsewhere, and
  the leg reds a member anchored twice.
- **Naming only the brief's four families.** The brief says to verify against the readers and add any
  consumer found, and naming four would keep the page's claim false for four more families.

## 5. Acceptance criteria

Run from the worktree's root, with `P` set as §4 sets it and probe A written there.

- **AC1** — When `python -B "$P/probe.py"` runs after the rewrite, it prints `read 14 unlisted none`.
  It prints eight `family` lines, each reading `named links 1`.
  figure: DERIVED, the read set and its count are re-derived by the scan at observation; the 14 is
  PINNED, measured 2026-11-02 at `201ac868`. A different count with `unlisted none` still passes.
  Red when: a family's keys are not all backticked in the region, its link is missing or doubled, or
  a reader landed since names a key no family lists, which prints after `unlisted`.
- **AC2** — When `python -B "$P/probe.py"` runs, its `region` line reads `two-families 0` and
  `closing 1`. Running `grep -c "The one exception is an invalid file" help/policy.md` prints 1.
  Red when: the old "Two families" wording survives, the closing claim is dropped or doubled, or the
  invalid-file exception is lost.
- **AC3** — When `python -B "$P/probe.py"` runs, its `anchors` line names the same seven anchors with
  the same fingerprints as §4's before-table. Its `commands` line reads `commands 8`, and its `links`
  line reads `links 9` with nothing after it.
  figure: PINNED, the seven anchors and fingerprints were measured 2026-11-02 at `201ac868`. The 9 is
  DERIVED from that measurement: today's 3 links, less the 2 the paragraph carries, plus the 8 the
  list carries.
  Red when: an anchor is added, moved off line 8 or altered, which the leg prints as TWICE or STALE.
  Also red when a new inline span opens with an interpreter, which it tests as a COMMAND, or a link
  names an untracked file or no heading of its page, which it prints as LINK or FRAGMENT.
- **AC4** — On the pass commit, `git diff --name-only HEAD~1 HEAD` prints `help/policy.md` alone.
  Every hunk header `git diff -U0 HEAD~1 HEAD -- help/policy.md` prints has an old range inside lines
  8-15.
  Red when: the pass touches a second file, or edits a line outside the paragraph, such as one under
  `## Install`, which the `policy fixtures` leg reads.

## 6. Gates

`docs` · `policy fixtures` · `memory hygiene`

The main loop runs these legs after the pass. The `docs` leg, `python tools/govkit/docs_leg.py`,
must exit 0 and print no STALE, LINK, FRAGMENT, COMMAND or TWICE line naming `help/policy.md`.
`policy fixtures` is owed because its guard names `help/policy.md` (`tools/gate-legs.json:1888`). Its
one read of the page is the `## Install` section (`tools/policy/check_policy.py:1309-1337`), which
AC4 holds unchanged. The plain bar runs once at the close. No arm is added or moved.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-02 · initial draft.

## 9. Reuse audit

The seam is the page's own pointer style: the parenthesised links to `agent-limit.md` and
`size-caps.md` at `help/policy.md:10-12`, extended to six more families. No code seam fits, because
no code is written. `reuse_lookup.py` ranked name stems only, `key` and `policy`, with
`read_policy_value` and `readPolicy` the nearest. Those are the readers this paragraph describes,
not a seam it extends. The derivation of which keys are consumed reuses the reader-coverage arm's own
`scan_reader_keys` and `check_key_read`, called from probe A rather than re-implemented. The recall
query returned this build's brief and README, TOOL-dFoldedAudit-18's F1, which named this paragraph,
and a dGroundRules closing review that had already flagged `help/policy.md:12-14`. None disagreed
with the source as read.

Reuse probe used: `python tools/codebase-map/reuse_lookup.py "a help page paragraph naming which policy keys have a consumer, with a link to each key's page"`.
Recall terms used: `python tools/memory-recall/query.py "which policy keys have consumers and where does help/policy.md say so" --terms "help/policy.md consumer paragraph policy key reader coverage help.enforce review.spec-audit agent-limit size-caps catalogue owner"`.
