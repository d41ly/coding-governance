# TOOL-dRankedPlan-74 — an ANSI-C or locale quoted segment of a shell carrier is rendered into quoting `shlex` reads before unquoting

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 25 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-68-promoted-fix-return.md) | research | TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-77 |
| [2026-10-27-build-TOOL-dRankedPlan-74-deviation-741.md](../build/2026-10-27-build-TOOL-dRankedPlan-74-deviation-741.md) | deviation | — |
| [2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dRankedPlan-1-agent-ledger.md) | journal | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-34 TOOL-dRankedPlan-35 TOOL-dRankedPlan-36 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-39 TOOL-dRankedPlan-40 TOOL-dRankedPlan-41 TOOL-dRankedPlan-42 TOOL-dRankedPlan-43 TOOL-dRankedPlan-44 TOOL-dRankedPlan-45 TOOL-dRankedPlan-46 TOOL-dRankedPlan-47 TOOL-dRankedPlan-48 TOOL-dRankedPlan-49 TOOL-dRankedPlan-50 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-53 TOOL-dRankedPlan-54 TOOL-dRankedPlan-55 TOOL-dRankedPlan-56 TOOL-dRankedPlan-57 TOOL-dRankedPlan-58 TOOL-dRankedPlan-59 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-63 TOOL-dRankedPlan-64 TOOL-dRankedPlan-65 TOOL-dRankedPlan-66 TOOL-dRankedPlan-67 TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 TOOL-dRankedPlan-78 TOOL-dRankedPlan-79 TOOL-dRankedPlan-80 TOOL-dRankedPlan-81 TOOL-dRankedPlan-82 TOOL-dRankedPlan-83 |
| [2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-68-promoted-fix-brief.md) | research | TOOL-dRankedPlan-68 TOOL-dRankedPlan-70 TOOL-dRankedPlan-77 |
| [2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md](../prompts/2026-10-28-prompt-TOOL-dRankedPlan-1-parents-crosscheck.md) | research | TOOL-dRankedPlan-1 TOOL-dRankedPlan-2 TOOL-dRankedPlan-3 TOOL-dRankedPlan-4 TOOL-dRankedPlan-5 TOOL-dRankedPlan-6 TOOL-dRankedPlan-7 TOOL-dRankedPlan-8 TOOL-dRankedPlan-9 TOOL-dRankedPlan-10 TOOL-dRankedPlan-11 TOOL-dRankedPlan-12 TOOL-dRankedPlan-13 TOOL-dRankedPlan-14 TOOL-dRankedPlan-15 TOOL-dRankedPlan-16 TOOL-dRankedPlan-19 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-27 TOOL-dRankedPlan-28 TOOL-dRankedPlan-29 TOOL-dRankedPlan-30 TOOL-dRankedPlan-31 TOOL-dRankedPlan-32 TOOL-dRankedPlan-33 TOOL-dRankedPlan-37 TOOL-dRankedPlan-38 TOOL-dRankedPlan-42 TOOL-dRankedPlan-45 TOOL-dRankedPlan-48 TOOL-dRankedPlan-51 TOOL-dRankedPlan-52 TOOL-dRankedPlan-57 TOOL-dRankedPlan-60 TOOL-dRankedPlan-61 TOOL-dRankedPlan-62 TOOL-dRankedPlan-64 TOOL-dRankedPlan-67 TOOL-dRankedPlan-77 TOOL-dRankedPlan-81 |
| [2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md) | spec-audit | TOOL-dRankedPlan-68 TOOL-dRankedPlan-69 TOOL-dRankedPlan-70 TOOL-dRankedPlan-71 TOOL-dRankedPlan-72 TOOL-dRankedPlan-73 TOOL-dRankedPlan-75 TOOL-dRankedPlan-76 TOOL-dRankedPlan-77 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 63 to 67
(`memory/builds/dRankedPlan/reviews/2026-10-27-review-TOOL-dRankedPlan-63-spec-audit.md`) confirmed
**finding 25 at HIGH**, item **H4**. `TOOL-dRankedPlan-65` S1 sends every carrier that is not plainly
single-quoted through `shlex.split`, and `shlex` reads `$` as a literal and `'…'` as single quotes.
So `bash -c $'\"$py\" \"$d/ratify.py\" \"$slug\"'` unquotes to text whose words keep their
backslashes, none ends in `ratify.py` once its quotes are stripped, and the carrier passes the
deny-by-default ban, though bash decodes `\"` to `"` and runs `ratify.py`. Unit 65 §1 claims the
carrier is unquoted "the way the shell does". This unit lists the carrier quotings it reads and
rewrites the two `shlex` does not know into a form it does, so unit 65's reading runs on what bash
runs. It repairs `TOOL-dRankedPlan-65`, so it sits one order above it.

## 2. Scope (IN)

- **S1** — The rendering. Before `TOOL-dRankedPlan-65` S1's `shlex.split`, `render_carrier_quoting(word)`
  rewrites the carrier word segment by segment, tracking single and double quotes as bash does. A
  `$'…'` segment outside quotes becomes `shlex.quote` of its body with bash's ANSI-C escapes decoded.
  A `$"…"` segment outside quotes becomes its `"…"` segment. Every other character is kept, so `$'`
  and `$"` inside double quotes stay literal, as in bash. The carrier quotings read are then single,
  double, ANSI-C `$'…'`, locale `$"…"` and any concatenation of them. This supersedes unit 65 S1's
  "is unquoted by `shlex.split(word, posix=True)`" as a call over the raw word. Observed by AC1 to AC4.
- **S2** — The escapes. The decoded set is bash's: `\a`, `\b`, `\e`, `\E`, `\f`, `\n`, `\r`, `\t`, `\v`,
  `\\`, `\'`, `\"` and `\?`; `\nnn` with one to three octal digits; `\xHH` with one or two hex digits;
  `\uHHHH` and `\UHHHHHHHH` with up to four and eight; and `\cX` as the control character of `X`. Any
  other `\` sequence keeps its backslash, as bash keeps it. Observed by AC4.
- **S3** — The plants. Three cases join `ratify.py --fixture --plant <case>`, each in its own scratch
  repository laid out from `TOOL-dRankedPlan-30`'s anchors, each a `.githooks/pre-commit`. Observed by
  AC1 to AC3.
  - `caller-shell-c-ansi` holds `bash -c $'\"$py\" \"$d/ratify.py\" \"$slug\"'`. It is refused with
    exit 1.
  - `caller-shell-c-ansi-exit` holds the same with ` --exit` before the closing `'`. It is admitted.
  - `caller-shell-c-locale` holds `bash -c $"\"$py\" \"$d/ratify.py\" \"$slug\""`. It is refused with
    exit 1.

## 3. Non-goals (OUT)

- A `$'…'` carrier holding `\'`. `scan_shell_tokens` ends the segment at that quote and raises on the
  file, so `TOOL-dRankedPlan-41` S4 exits 2 before S1 runs, which fails closed.
- Translating a locale string. Bash looks `$"…"` up in a message catalogue, and no catalogue holds
  shell source here, so it is read as the double-quoted text it falls back to.
- The exit 2 of a carrier a reader cannot read: `TOOL-dRankedPlan-73`.

### Edges

- **consumes-from** `TOOL-dRankedPlan-65` — S1's `shlex` unquoting and the readers after it, which S1 feeds; without them the rendered word is read by nothing
- **hands-off** `TOOL-dRankedPlan-81` — S1, S2, AC4, §3, §4, §5 and §7, which that unit's items for findings 2, 5, 8, 19, 20 and 9 correct; carry S3, S5, S6, S11, S13 and S19 of that unit into this unit's pass (spec audit of units 68 to 77)

## 4. Design

### Evidence

- A probe run 2026-10-27 at a76dbde6 over `scan_shell_tokens` from `tools/lexicon/lexicon.py` read
  `bash -c $'\"$py\" \"$d/ratify.py\" \"$slug\"'` as three words, the last the whole `$'…'` word, and
  `shlex.split` over it returned one word that kept every `\"`. The same tokenizer raised
  `unterminated ' quote` on `bash -c $'it\'s "$d/ratify.py"'`. The outputs are PINNED.
- `shlex.quote("aA'b")` returned `'aA'"'"'b'`, and Git Bash ran `bash -c $"\"$py\" \"$d/ratify.py\"
  \"$slug\""` as `"$py" "$d/ratify.py" "$slug"`. The outputs are PINNED.
- `git grep -nE "(bash|sh) -c \$['\"]" -- '*.sh' '.githooks/*'` and the same for `<<< $'`, run
  2026-10-27 at a76dbde6, each printed 0 lines. The counts are PINNED, so no tracked file moves.

### The reading after this unit

| Carrier | After S1 | Answer |
|---|---|---|
| `$'\"$py\" \"$d/ratify.py\" \"$slug\"'` | `'"$py" "$d/ratify.py" "$slug"'` | caller |
| the same with ` --exit` | the same with ` --exit` | not a caller |
| `$"\"$py\" \"$d/ratify.py\" \"$slug\""` | `"\"$py\" \"$d/ratify.py\" \"$slug\""` | caller |
| `"echo $'x'"` | unchanged, `$'` inside double quotes | unit 65 S1, unchanged |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `render_carrier_quoting` | function, `tools/loop/ratify.py` | `py.function`; `python tools/lexicon/lexicon.py --suggest render_carrier_quoting --as py.function` answered OK |
| `caller-shell-c-ansi`, `caller-shell-c-ansi-exit`, `caller-shell-c-locale` | `ratify.py` fixture plants | none |

The minted function is rendered into `memory/map/generated/symbols.json` by `gen_map.py --write`, as
`TOOL-dRankedPlan-61` S1 states.

### Rollout

Live at landing, at order 25. Units 67, 73, 75 and 76 share the order and write
`tools/loop/ratify.py`, so by BUILD-METHOD M6 clause 1 they are sequenced inside it.

### Files touched (estimate)

- `tools/loop/ratify.py`: S1 to S3
- `memory/map/generated/symbols.json`: the render of S1's function

### Alternatives rejected

- **Refuse any carrier holding a `$'` segment with exit 2.** The audit offers it. Exit 2 says the
  check cannot read the input, and bash reads this one, so a hook that writes one would block the bar
  on readable input. The escape table is one function, and BUILD-METHOD M3's rule takes the option
  that satisfies more: the decoded reading also admits the `--exit` form.
- **Decode with Python's `unicode_escape` codec.** It lacks `\e`, `\E`, `\?` and `\cX`, reads
  non-ASCII text as Latin-1, and drops the backslash of an unknown escape that bash keeps.

## 5. Production-readiness checklist

- security — narrows: an ANSI-C or locale quoted carrier running the predicate's CLI is refused.
- perf / scale — one character pass per carrier that is not single-quoted; none is tracked today.
- error / empty / loading states — an unterminated `$'…'` never reaches S1: the file tokenizer raises
  first, and `TOOL-dRankedPlan-41` S4 exits 2.
- observability — the refusal names the file and the command's line.
- risks — a `$'…'` carrier naming `ratify.py` for a non-executing purpose is refused, which fails
  closed.
- testing — the three plants and the probe of AC4.
- migration — none.
- user docs — N/A — no user-facing surface.

## 6. Acceptance criteria

- **AC1** — When `python ratify.py --fixture --plant caller-shell-c-ansi` runs, the check exits 1
  naming `.githooks/pre-commit`.
  Red when: `shlex` reads the raw `$'…'` word, so every word keeps its backslashes.
- **AC2** — When the plant `caller-shell-c-ansi-exit` runs, the check exits 0 and prints `ratify —
  callers:`.
  Red when: a rendered carrier's `--exit` call is refused.
- **AC3** — When the plant `caller-shell-c-locale` runs, the check exits 1 naming
  `.githooks/pre-commit`.
  Red when: a `$"…"` segment keeps its `$`, so the first word reads `$"$py"`.
- **AC4** — When a probe imports the loop kit's `ratify.py` and calls `render_carrier_quoting("$'a\\x41\\'b\\q'")`,
  it returns `'aA'"'"'b\q'`, and `render_carrier_quoting('"echo $\'x\'"')` returns its input.
  Red when: `\xHH` or `\'` is left encoded, an unknown escape loses its backslash, or a `$'` inside
  double quotes is decoded.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms`

`loop selftest`, `loop breakpoints fixtures` and every other leg whose guard trips `tools/loop/`,
`build-index selftest` among them once `TOOL-dRankedPlan-45` S18 lands,
is owed once dDeclaredLoop's loop legs are in the manifest,
as `python tools/check-spec-tokens.py --legs-for tools/loop/ratify.py` derives them once that path
is tracked, and this unit's pass names each on the line above then, by `TOOL-dRankedPlan-45` S17's
rule.

New arm: tools/loop/ratify.py · covers AC1 AC3 · `caller-shell-c-ansi` reddened by `shlex` over the raw `$'…'` word, and `caller-shell-c-locale` reddened by a rendering that keeps the `$` of `$"`; AC2 is green-only · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 63 to 67, finding 25
  (HIGH, item H4), repairing `TOOL-dRankedPlan-65`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-81`, the reciprocal of that promoted unit's own edge (spec audit of units 68 to 77, `reviews/2026-10-27-review-TOOL-dRankedPlan-68-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams reused are the stdlib `shlex.quote`, which writes a decoded segment back as single-quoted
text, and `TOOL-dRankedPlan-65` S1's `shlex.split` and readers, which the rendered word feeds.
`python tools/codebase-map/reuse_lookup.py "decode ansi-c dollar single quoted shell string
escapes"`, run 2026-10-27, ranked `parse_shell_defs` and `scan_shell_layer`, which read no quoting,
`resolve_shell_argv` (`tools/govkit/govkit.py:1200`), which replaces a leading `bash` and decodes
nothing, and `ask_shell`, so no existing seam decodes ANSI-C quoting and S1 is new. The recall query
returned units 46, 53 and 65 to 67, and they agree with the source read.

Recall terms used: `python tools/memory-recall/query.py "how does the caller check read command substitutions inside an expanded heredoc body and ansi-c carriers" --terms "heredoc expanded command substitution span case esac arithmetic ansi-c carrier shlex caller ratify"`
