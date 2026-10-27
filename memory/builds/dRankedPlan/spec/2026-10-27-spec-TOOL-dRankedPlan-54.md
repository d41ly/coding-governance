# TOOL-dRankedPlan-54 — every heredoc token kind reaches the body router, through one declared kind set

**Status:** OPEN · rev-1 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 23 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-54-deviation-541.md](../build/2026-10-27-build-TOOL-dRankedPlan-54-deviation-541.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 46 to 52
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-46-spec-audit.md`) confirmed
**finding 23 at HIGH**, item **H1**, which it shares with finding 3. `TOOL-dRankedPlan-52` S13 splits
the heredoc token of `TOOL-dRankedPlan-45` S10 into `heredoc` and `heredoc-expanded` at order 22. The
body router of `TOOL-dRankedPlan-46` S1 and `TOOL-dRankedPlan-47` S1 is built at order 21 against the
single `heredoc` kind, and no spec tells it to read the new one. A router that compares a token's kind
with `heredoc` leaves every unquoted-delimiter body unread, so `bash <<EOF` running `"$py"
"$d/ratify.py" "$slug"` reaches only `TOOL-dRankedPlan-38`'s textual rule, which matches the
predicate's name and not `ratify.py`, and passes the deny-by-default ban. This unit declares the kind
set once, makes the router select by membership, and probes the class so a later kind cannot slip
past the router. Finding 3, the reading of an expanded shell body, is `TOOL-dRankedPlan-53`'s. This
unit repairs `TOOL-dRankedPlan-52`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The kind set. `HEREDOC_KINDS = ("heredoc", "heredoc-expanded")` in `tools/loop/ratify.py`.
  The body router selects a separators-mode token as a heredoc body when its kind is in
  `HEREDOC_KINDS`, never by comparing it with one kind's name, and routes it by its command word as
  `TOOL-dRankedPlan-46` S1 and `TOOL-dRankedPlan-47` S1 state, whatever its kind. The kind decides only
  what `TOOL-dRankedPlan-52` S13 and `TOOL-dRankedPlan-53` add over the reader the command word picks.
  This supersedes the router's reading of `TOOL-dRankedPlan-45` S10's "one `heredoc` token" as the
  selection rule. Observed by AC1 and AC2.
- **S2** — The class probe. The fixture case `heredoc-kinds-routed` joins `ratify.py --fixture --plant
  <case>`. It tokenizes, with `scan_shell_tokens(seps=True)` from the loop kit's `extract_code.py`, a
  one-line body under each of the five delimiter spellings `<<EOF`, `<<'EOF'`, `<<"EOF"`, `<<\EOF` and
  `<<-EOF`, each opened by `bash`. It passes only when every body token's kind is in `HEREDOC_KINDS`
  and the router hands each body to `read_shell_callers`. Observed by AC1.
- **S3** — The plant. `caller-heredoc-shell-dashed` plants a `.githooks/pre-commit` feeding `bash
  <<-EOF` a body whose one line is a tab and then `"$py" "$d/ratify.py" "$slug"`. The unquoted
  delimiter makes its body a `heredoc-expanded` token. It is refused. It joins `ratify.py --fixture
  --plant <case>` in its own scratch repository laid out from `TOOL-dRankedPlan-30`'s anchors.
  Observed by AC2.

## 3. Non-goals (OUT)

- Which reader an expanded shell body gets, and the textual line rule beside it (finding 3, the same
  item): `TOOL-dRankedPlan-53`.
- The tokenizer's kinds. `TOOL-dRankedPlan-52` S13 mints them, and this unit reads them.
- A spec-token check that a unit splitting a token kind names every sibling reader of that kind, the
  audit's left-shift gate for H1. It is a gate over the spec corpus, a separate mechanism, and the
  close's left-shift step owns it.

### Edges

- **consumes-from** `TOOL-dRankedPlan-52` — S13's `heredoc` and `heredoc-expanded` kinds, which S1 names as one set; without them there is no second kind to route
- **hands-off** `TOOL-dRankedPlan-53` — `HEREDOC_KINDS` and the router's membership test, through which that unit's expanded shell body reaches `read_shell_callers`

## 4. Design

### Evidence

- `TOOL-dRankedPlan-52` S13 (its lines 121-129) mints the two kinds, and its §4 table "Token kinds in
  separators mode" lists them on one row.
- `TOOL-dRankedPlan-46` §3 Edges consumes "S10's `heredoc` token" from `TOOL-dRankedPlan-45`, and its
  three plants each use `<<'EOF'`, a quoted delimiter. `TOOL-dRankedPlan-47` §3 Edges reads the same
  token.
- The tokenizer reads all five delimiter spellings today: `tools/lexicon/lexicon.py:696-724` strips
  the quotes, a backslash and the `-` of `<<-` while collecting the delimiter, so each spelling queues a
  body.

### The router after this unit

| Body token kind | Command word `bash` | Command word `"$py"` |
|---|---|---|
| `heredoc` | `read_shell_callers` | `read_python_callers` |
| `heredoc-expanded` | `read_shell_callers`, with `TOOL-dRankedPlan-53`'s line rule | `TOOL-dRankedPlan-52` S13's textual rules |
| any kind outside `HEREDOC_KINDS` | not a body: AC1 reds before it ships | the same |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `HEREDOC_KINDS` | constant, `tools/loop/ratify.py` | none declared |
| `heredoc-kinds-routed`, `caller-heredoc-shell-dashed` | `ratify.py` fixture cases | none |

### Rollout

Live at landing, at order 23. `TOOL-dRankedPlan-53`, `TOOL-dRankedPlan-56` and `TOOL-dRankedPlan-61`
share order 23. This unit and units 53 and 56 write `tools/loop/ratify.py`, so by BUILD-METHOD M6
clause 1 they are sequenced inside that step, this unit first, because unit 53 consumes from it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3

### Alternatives rejected

- **Leave one `heredoc` kind and carry the quoting as a field.** `TOOL-dRankedPlan-52` S13 already
  chose two kinds and lands first, so this would rewrite a unit built before this one.
- **Name both kinds at each comparison site.** Two sites each spelling the pair is the defect this
  finding names, one level up: the next kind would again reach only the sites someone remembered.

## 5. Production-readiness checklist

- security — narrows: an unquoted-delimiter body reaches the deny-by-default ban's router.
- perf / scale — one set test per heredoc token.
- error / empty / loading states — a body the tokenizer cannot close exits 2, as
  `TOOL-dRankedPlan-41` S4 states for a file.
- observability — the refusal names the hook and the body's line.
- risks — none beyond `TOOL-dRankedPlan-53`'s ceiling.
- testing — the class probe and the dashed plant, each red and green.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant heredoc-kinds-routed` runs, it exits 0.
  Red when: a delimiter spelling yields a body kind outside `HEREDOC_KINDS`, or a body of one kind is
  not handed to `read_shell_callers`.
- **AC2** — When the plant `caller-heredoc-shell-dashed` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: the router selects only the `heredoc` kind, so an unquoted body is never read.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands, is owed once dDeclaredLoop's
loop legs are in the manifest, as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py`
derives them, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC2 · `heredoc-kinds-routed` and `caller-heredoc-shell-dashed`, staged by a router that compares a token's kind with `heredoc` only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 46 to 52, finding 23 (HIGH,
  item H1, shared with finding 3), repairing `TOOL-dRankedPlan-52`.

## 10. Reuse audit

The seam extended is the body router of `TOOL-dRankedPlan-46` S1 and `TOOL-dRankedPlan-47` S1, over the
kinds `TOOL-dRankedPlan-52` S13 adds to `scan_shell_tokens`' separators mode. `python
tools/codebase-map/reuse_lookup.py "route a heredoc body to a reader by its token kind and command
word"`, run 2026-10-27, ranked name stems only (`read`, `read_text`, `resolve_prefix_token`), and no
tracked file reads a heredoc token kind, because the loop kit's `ratify.py` does not exist at base
0689e7fa, so no existing seam fits beyond the router. The recall query returned units 38, 41, 45 to
47, 49, 51 and 52 and this audit's H1 item, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check route a heredoc body by its delimiter quoting and command word" --terms "heredoc expanded quoted delimiter kind router shell interpreter body reader textual rule caller ratify"`
