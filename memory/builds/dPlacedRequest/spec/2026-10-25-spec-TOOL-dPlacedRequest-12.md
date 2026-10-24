# TOOL-dPlacedRequest-12 — create-only decision and problem registers on the remote

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 8 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0130@57d242df whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-a.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |

<!-- /gen:spec-records -->

## 1. Goal

Two create-only registers on the remote, each ref written once by compare-and-swap and refused when
it exists. Decisions go to `refs/gov/decisions/<build>/<key>`, keyed by the item that raised the
question and its declared fork, never by the decision's wording, so a second session deciding the
same slot is refused and reads the first. Problems go to
`refs/gov/problems/<encoded subject>/<problem id>`, the subject encoded into a legal ref name and the
id derived from the filing act and the problem's content, so two problems on one path both land and a
retried filing is refused (gap-conc-08; the owner's NT-18).

## 2. Scope (IN)

- **S1** — The encoder: `derive_ref_segment <text>` in `tools/unattended/unattended.sh` prints `<text>`
  with every byte outside `[A-Za-z0-9_-]` written as `%` and two upper-case hex digits. A leading dot,
  a `.lock` ending, a space, `:` and `~` are therefore each escaped, and so are `/`, every other dot
  and every other byte `git check-ref-format` refuses, so the result is always one legal ref
  component. It refuses an empty text. Observed by AC1, AC2.
- **S2** — The decision key: `derive_decision_key <item> <fork>` prints
  `derive_ref_segment <item>`, a literal `+`, then `derive_ref_segment <fork>`. It reads no wording: the
  verb that calls it takes the decision's text only as the record body. `+` is always escaped inside
  either part, so the key splits back into exactly one pair. Observed by AC3.
- **S3** — The problem id: `derive_problem_id <session> <item> <subject> <file>` prints the first 12 hex
  digits of `git hash-object --stdin` over the session, the item, the subject and the file's bytes,
  each followed by one NUL. The filing act is the filer's session and the item it filed from, `none`
  outside an item. Observed by AC4, AC5.
- **S4** — The write: `unattended.sh --register decision <build> <item> <fork> <file>` and
  `unattended.sh --register problem <subject> <item> <file>` build one commit over the empty tree
  with TOOL-dPlacedRequest-11's `build_gov_commit "" <message>`, a create being its one parentless
  commit, and write it with `write_gov_ref <ref> "" <commit>`, the empty expected sha making every
  write a create.
  `<build>` passes `check_slug`. rc 0 prints `register — written <ref>`. Observed by AC3, AC4.
- **S5** — The refusal: a create that loses (`write_gov_ref` rc 1) prints `register — exists <ref>`,
  then fetches that ref once, bounded, and prints its record, and exits 1; a write not completed
  (rc 2) prints `register — not written <ref> · <GOVREF_WHY>` and exits 2. A second decision on one
  slot is never written beside the first. Observed by AC3, AC5.
- **S6** — The record: header `gov-decision <build>/<key>` or `gov-problem <encoded subject>/<id>`, a
  blank line, then `key: value` lines (decision: `build`, `item`, `fork`, `session`; problem:
  `subject`, the raw subject, `item`, `session`), a blank line, and the body file's text. The body
  is refused over 4096 bytes or with a NUL or a control byte other than tab and newline, before any
  commit is built. Observed by AC6.
- **S7** — The switch: both acts write only while the coordination switch TOOL-dPlacedRequest-1 leaves
  reads on (`RUN_CLAIMS` at base, `tools/unattended/unattended.sh:671-676`), and otherwise print
  `register — off` and write nothing. Observed by AC7.
- **S8** — The documentation: the verbs guide gains `--register` with both forms, the key and id
  derivations and the exit codes. Observed by AC8.

## 3. Non-goals (OUT)

- The work-order slot joining the decision key. The clause joins it "once work orders carry slots";
  the build that gives work orders slots adds a third part to `derive_decision_key`, and until then
  the key is the item and its fork.
- Readers that hand a work order the problems whose subject meets its item's seed (NT-18's last
  sentence), and any listing of the registers: the builds that cut work orders.
- Secret scanning of a register's body. Coordination payloads outside the scan's population are
  gap-rt-44, dWellOiledMachine's; this unit caps and shape-checks the body at the write.
- Deleting or rewriting a register entry. Neither act takes an expected sha other than empty.
- The change feed: TOOL-dPlacedRequest-13 appends every `write_gov_ref` write, these included.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, the one compare-and-swap ref writer whose empty expected sha makes each register write a create, and `build_gov_commit`; without it each register would be a third hand copy of the push
- **consumes-from** external — the coordination switch `RUN_CLAIMS` (`tools/unattended/unattended.sh:671-676`) as TOOL-dPlacedRequest-1 leaves it, and `check_slug` (`:2894`)

## 4. Design

### Evidence

- A create is already a compare-and-swap with an empty sha: `write_claim` pushes
  `--force-with-lease=<ref>:<sha read>` (`tools/unattended/unattended.sh:2423`), and the class table
  routes an absent claim to `CW_ACT=create` (`:2285`), so the empty sha is what reaches the push.
- A lost create reads `(stale info)` or `(fetch first)` on its porcelain line (`:2434`), the parse
  TOOL-dPlacedRequest-11 moves into `write_gov_ref` (I1).
- The claim record is a commit over the empty tree with a fixed `gov-claim` identity (`:2419`), its
  message a header, a blank line and `key: value` lines (`:2411-2412`).
- `git check-ref-format` refuses a component that begins with `.`, ends with `.lock`, or carries a
  space, `:` or `~` (each probed at writing: `git check-ref-format "refs/gov/problems/.githooks/x"`
  and its four siblings exit 1, and `refs/gov/problems/%2Egithooks%2Fpre-push/0123456789ab` exits 0).
- A ref cannot be both a file and a directory: `git update-ref refs/gov/leases/run/build/2026-10`
  failed while `refs/gov/leases/run/build` existed, probed at writing in a scratch bare repository.
  A subject kept with its `/` would put `tools/lib` and `tools/lib/x.sh` at that risk; one encoded
  component cannot.
- The id convention is the first 12 hex digits (`derive_section_sha`,
  `tools/roles/handoff.py:307`); the driver already cuts a `git hash-object` to 12 (`:8254`).

### The two registers

| Register | Ref | Key or id from | A second write |
|---|---|---|---|
| decision | `refs/gov/decisions/<build>/<key>` | `<item>` and `<fork>` | refused; the first is printed |
| problem | `refs/gov/problems/<encoded subject>/<problem id>` | the act and the content | a retry refused; new content lands beside |

### The encoder

```
derive_ref_segment "<text>":
  for each byte b of <text> under LC_ALL=C:
    b in [A-Za-z0-9_-]  -> b
    otherwise           -> printf '%%%02X' b
```

| Subject | Encoded |
|---|---|
| `.githooks/pre-push` | `%2Egithooks%2Fpre-push` |
| `x.lock` | `x%2Elock` |
| `a b` | `a%20b` |
| `ns:tag` | `ns%3Atag` |
| `HEAD~1` | `HEAD%7E1` |

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `--register` | verb, with the kind words `decision` and `problem` | `tools/unattended/unattended.sh` |
| `derive_ref_segment` | function | `tools/unattended/unattended.sh` |
| `derive_decision_key`, `derive_problem_id` | functions | `tools/unattended/unattended.sh` |
| `write_register` | function | `tools/unattended/unattended.sh` |
| `refs/gov/decisions/`, `refs/gov/problems/` | ref namespaces | the remote |

Every function name leads with a verb of the naming lexicon's `VERBS` table (`.lexicon.conf`). The
spec brief's I10 spells the encoder `encode_ref_segment`; `encode` is not in that table, so the name
would add a verb offender past `VERB_OFFENDER_PIN` and red `lexicon naming predicates`. The encoder
derives a value from its input, so it is `derive_ref_segment`; no other unit names it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **Escaping only the five bytes the clause names.** The result is still illegal for `^`, `?`, `*`,
  `[`, `\`, `..` and `@{`, and a subject kept with its `/` meets the file and directory collision.
- **A decision key hashed from the item and fork.** It is equally stable and unreadable on the
  remote; the encoded pair is both.
- **A timestamp in the problem id.** A retried filing would then land twice, which the clause's
  red case refuses.

## 5. Production-readiness checklist

- security — two new write surfaces on the remote, both through `write_gov_ref` and both create-only,
  so no write can rewrite or delete an entry; every field is validated at the write, the body capped
  and shape-checked, and both acts dark behind the coordination switch.
- perf / scale — one commit and one push per write; one bounded fetch on a refused write.
- error / empty / loading states — an empty subject, item or fork is refused before any commit; an
  unreachable remote is `register — not written` with the bounded runner's cause.
- observability — every outcome is one `register —` line naming the ref; a refused decision prints the
  first one's record.
- risks — an agent can file an unbounded number of problems, one ref each; a register entry is never
  pruned, by design, so the namespace only grows.
- testing — the fixture cases under AC1 to AC7 and the suite arm in §7.
- migration — none: both namespaces are new.
- user docs — the verbs guide; no page under `help/` describes the driver's verbs.

## 6. Acceptance criteria

The fixture for AC3 to AC7 is a bare remote and two clones under `%TEMP%` with short names, each a
different session id, the coordination switch on. The unattended kit's own suites are waived for this
build's landing (README rule 8), so each probe below is the observation.

- **AC1** — When a probe sources `unattended.sh` and passes `derive_ref_segment` each subject of §4's
  encoder table, it prints the encoded column, and `git check-ref-format "refs/gov/problems/<out>/x"`
  exits 0 on each.
  Red when: any of the five escapes is removed from the encoder, as a planted copy that keeps `.`
  does for `.githooks/pre-push` and `x.lock`, and that subject's ref fails `check-ref-format`.
- **AC2** — When `derive_ref_segment` runs on `a+b` and on `a/b`, the outputs differ from each other
  and from `derive_ref_segment` of `a%2Bb`, and an empty text is refused.
  Red when: two subjects encode alike, or an empty subject yields a ref.
- **AC3** — When clone A runs `unattended.sh --register decision fx entry.claim F1 a.txt` and clone B
  then runs the same slot with `b.txt`, A prints `register — written`, B prints `register — exists`
  and A's record and exits 1, and the bare remote's `refs/gov/decisions/fx/<key>` carries A's text
  only.
  Red when: B's decision is written, or B exits 0; the planted case is two clones deciding one slot.
- **AC4** — When clone A files two problems with different texts against the subject
  `tools/push-main.sh`, both land as two refs under one encoded subject.
  Red when: the second is refused; the planted case is two problems filed against one path.
- **AC5** — When clone A re-runs one problem filing with the same session, item, subject and text,
  the second run prints `register — exists` and exits 1, and the remote holds one ref for it.
  Red when: a retried filing lands twice.
- **AC6** — When `--register problem` is given a body of 4097 bytes, or one carrying a NUL, it is
  refused before a commit is built and the remote is unchanged.
  Red when: an oversized or binary body reaches the remote.
- **AC7** — When `RUN_CLAIMS` is off in the clone's conf, `--register decision …` prints
  `register — off` and the remote gains no ref.
  Red when: a register is written with the switch off.
- **AC8** — When `grep -n -- "--register" tools/unattended/VERBS.template.md` runs, the verbs guide
  names both forms and the exit codes 0, 1 and 2.
  Red when: the guide omits a form or a code.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC6 AC7 · each encoder escape, a second decision on one slot, two problems on one path, a retried filing and the switch off, staged against the base driver, which has no register verb · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is a subject encoded?** (a) Every byte outside `[A-Za-z0-9_-]` as `%HH`, the whole subject
  one component; (b) only the five named bytes escaped, `/` kept as hierarchy. (b) leaves other
  illegal bytes legal input and lets a directory subject and a file under it collide at the remote.
  Rung 3, the most capable option: (a) meets AC1, AC2 and AC4 on any subject. RESOLVED (agent,
  2026-10-25, delegated): (a). widens: none · relaxes: none
- **F2 — What is the filing act a problem id derives from?** (a) The filer's session and the item it
  filed from, with the subject and the content; (b) the session alone; (c) a timestamp. (c) makes a
  retry a new id, which the clause refuses; (b) merges one session's filings from two items. Rung 1,
  the clause's "the id derived from the filing act and the problem's content". RESOLVED (agent,
  2026-10-25, delegated): (a). widens: none · relaxes: none
- **F3 — Are the registers dark?** (a) Behind the coordination switch claims already use; (b) always
  on, being uncalled. (b) is a new write path on the shared remote with no switch, against the
  charter's small rule for risky behaviour. Rung 3. RESOLVED (agent, 2026-10-25, delegated): (a).
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: §7's leg line gains `recall floor` and
  `recall floor arms`, the legs `memory/guides/UNATTENDED-VERBS.md` in Files touched trips.

## 10. Reuse audit

The seam extended is the one compare-and-swap ref writer, `write_gov_ref`, which TOOL-dPlacedRequest-11
extracts from `write_claim` (`tools/unattended/unattended.sh:2396`, the empty-sha create at `:2285` and
`:2423`) and `write_red_ref` (`tools/run-gates/post-merge.sh:276`). The probe
`python tools/codebase-map/reuse_lookup.py "write a ref on the remote once by compare-and-swap and
refuse when it already exists"` ranked `write_claim` and `write_bar_green` among name-stem hits, both
the writer this unit calls. For the encoder no existing seam fits:
`python tools/codebase-map/reuse_lookup.py "encode an arbitrary path into a legal git ref name
segment"` ranked `GIT`, `run_git` and path helpers, none an encoder, and `git grep check-ref-format`
over `tools/`, `skills/` and `.githooks/` finds nothing, as scout A recorded. Scout A cited the create
at `:2361-2362` and `:2285`; at `c63aabbb` the first is `write_claim`'s header comment saying the
expected sha is empty for a create and the second the create row, both as cited, and the push itself
is `:2423`.

Recall terms used: `python tools/memory-recall/query.py "how is a decision kept from being recorded
twice by two sessions" --terms "decision register create-only compare-and-swap ref refs/gov second
session refused fork key"`
