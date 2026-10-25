# TOOL-dPlacedRequest-19 — the project-level request record: pushed by its content key, its text kept where it was typed

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 10 · advances TOOL-dPlacedRequest-22

**Carries:** cl-dClosedLoop-0137@39b3ef9d whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-fix-return.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-reuse-scout-b.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-21 |
| [2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md](../build/2026-10-25-build-TOOL-dPlacedRequest-1-spec-stage-returns.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-fix-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-1-spec-brief.md) | research | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 |
| [2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-3 |

<!-- /gen:spec-records -->

## 1. Goal

An owner's request that is not yet a build becomes a project-level record any node may claim by
lease. The owner's words are kept verbatim on the node where they were typed; the remote holds only
the record `refs/gov/requests/<content key>`, carrying the key, the fleet tag and the session, until
dWellOiledMachine publishes the text redacted. A request travels between nodes only by that key, and
a request that arrived that way is data with provenance, never the owner's consent (gap-conc-17;
P40; the owner's CL-4 and FR-1).

## 2. Scope (IN)

- **S1** — The content key, `request_content_key` (I11): `derive_request_content_key(text)` in
  `tools/loop/request.py` returns the first 12 hex digits of SHA-256 over the UTF-8 bytes of
  `derive_content_key(text)`, imported from the memory-tree kit's `row_grammar.py` (`tools/memory-tree/row_grammar.py:1475`), resolved with
  `resolve_kit_dir`; an empty normalised text is refused. `python request.py key <file>` prints it.
  It keys the text alone, so an absent intake keys a request the same way (I11). Observed by AC1.
- **S2** — The local text: `unattended.sh --request <file>` copies the file's bytes unchanged to
  `<git-common-dir>/requests/<content key>.md`, keeping the first copy when one exists, and appends
  this session's id once to `<git-common-dir>/requests/<content key>.typed`. Nothing under
  `requests/` is tracked or pushed. Observed by AC2, AC5.
- **S3** — The record: the same verb builds one commit over the empty tree with
  `build_gov_commit "" <message>`, the message `gov-request <content key>`, a blank line, and exactly
  three lines, `content-key`, `fleet-tag` and `session`, each validated at the write: twelve lower-case
  hex digits, this node's tag as TOOL-dPlacedRequest-1's `resolve_fleet_tag` reads it from
  `tools/playbook/fleet.toml`, and a session id of letters, digits and dashes. It writes `refs/gov/requests/<content key>` with
  `write_gov_ref <ref> "" <commit>`, a create. A create that loses means the request is already
  recorded and exits 0 saying so; a write not completed exits 2 with the text kept, and re-running the
  verb retries. This commit is the ref's root; TOOL-dPlacedRequest-14's pre-claim draw rows follow it
  on the same ref, each parented on the tip it read (I21). Observed by AC2, AC3.
- **S4** — The claim by lease: TOOL-dPlacedRequest-1's `derive_lease_ref` gains the kind `request`,
  `derive_lease_ref request <content key>` building `refs/gov/leases/request/<content key>`, the key
  held to twelve lower-case hex digits; its `kind` key takes `request`; and `derive_lease_ref` refuses
  `request` as a build or unit lease's slug, as it refuses `run`. `unattended.sh --lease acquire
  request <content key>` acquires it through that verb's `lease` mode, after the same bounded fetch
  confirms `refs/gov/requests/<content key>` exists; a key with no record is refused before any write.
  Any node may claim; a live holder refuses the rest with `live-holder`. Observed by AC4.
- **S5** — The consent predicate: `check_request_consent <content key>` returns 0 only when this
  session's id is a line of `<git-common-dir>/requests/<content key>.typed`, and otherwise returns 1
  printing `request — <key> · relayed: data with provenance, never consent`. A node or session that
  received the key from another has no such line, so the predicate refuses it by default; the
  breakpoint disposition calls it before it fires. Observed by AC5.
- **S6** — The documentation: the verbs guide gains `--request` and the `request` kind of `--lease`,
  the stops guide's section 7 the request lease form beside the build, unit and run forms and the
  reserved slug `request`. Observed by AC6.

## 3. Non-goals (OUT)

- Publishing the text. dWellOiledMachine publishes it redacted (`cl-dClosedLoop-0335`), through the
  run-log kit's `scan_secrets` (`tools/runlog/runlog_lib.py:522`), which nothing in this unit calls
  because nothing in this unit publishes text.
- Binding the text to the owner's keystrokes. The hook-written intake is dWellOiledMachine's (FR-1);
  until it lands, `--request` trusts its caller that the file is the owner's words, and an agent in the
  typing session could record words the owner never typed. The consent predicate inherits that limit.
- The relay channel. A key travels in a mailbox message (dKeptSession) or an offer (the `fleet`
  expansion, TOOL-dPlacedRequest-20's keys); this unit ships no verb that sends a request anywhere.
- Placing a request, its budget, its probes and its claim commit: TOOL-dPlacedRequest-4,
  TOOL-dPlacedRequest-14, TOOL-dPlacedRequest-7 and TOOL-dPlacedRequest-21, which read
  `request_content_key`.
- The breakpoint disposition itself: TOOL-dPlacedRequest-5, which calls `check_request_consent`.
- The secret scan of coordination payloads (gap-rt-44): the record's three fields are shape-checked so
  no free text can ride them, which is the whole of this unit's boundary.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-11` — `write_gov_ref`, the one compare-and-swap writer whose empty expected sha makes the record a create, and `build_gov_commit`; without it the record would be another hand copy of the claim push
- **consumes-from** `TOOL-dPlacedRequest-1` — the lease grammar `refs/gov/leases/<slug>/build`, `derive_lease_ref`, the `--lease` verb and its `lease` mode, the record's `kind` key and `resolve_fleet_tag`, which the request lease and the record reuse; without it a request could not be claimed by lease
- **hands-off** `TOOL-dPlacedRequest-7` — `request_content_key`, the key the entry-time probe is keyed and filed by, taken as its `--request <content key>` argument
- **hands-off** `TOOL-dPlacedRequest-4` — `request_content_key`, the key placement records the disposition against, taken as its `--request <content key>` argument, and `--request`, the verb the unattended prompt path calls to record a prompt before placing it
- **hands-off** `TOOL-dPlacedRequest-14` — `request_content_key`, the key the pre-claim budget draws under, computed by `--request-text` through `derive_request_content_key`
- **hands-off** `TOOL-dPlacedRequest-21` — `request_content_key`, the `content-key` the claim commit carries, taken as its `--request <content key>` argument
- **hands-off** `TOOL-dPlacedRequest-5` — `check_request_consent`, which the breakpoint disposition calls and which refuses a relayed request
- **hands-off** `TOOL-dPlacedRequest-30` — `--request` and its first-copy rule, which that unit replaces with a collision refusal
- **hands-off** `TOOL-dPlacedRequest-31` — `check_request_consent` and the `.typed` line, which that unit binds to the bytes a session typed
- **hands-off** `TOOL-dPlacedRequest-32` — `--request` and `check_request_consent`, which that unit closes to an absent session
- **hands-off** `TOOL-dPlacedRequest-34` — the round-1 spec audit's minors this unit's code carries, which that unit amends in place as its §2 names
- **hands-off** `TOOL-dPlacedRequest-43` — the `.typed` file's table row, which that unit's item for finding 29 reads in the two-field grammar of `TOOL-dPlacedRequest-31`

## 4. Design

### Evidence

- No project-level request record exists. The verbatim record of a prompt today is build-scoped,
  under `<build>/prompts/` (`tools/unattended/unattended.sh:3548`, the prompt record reader).
- The node-local store precedent is the card: `<git-common-dir>/orientation/<sid>.md`, resolved from
  `git rev-parse --git-common-dir` (`skills/session-kickoff/manifest-check.sh:311-315`).
- `derive_content_key` normalises only, links to text, dates and emphasis dropped, case and whitespace
  folded (`tools/memory-tree/row_grammar.py:1475-1479`); the twelve-hex convention is
  `derive_section_sha` (`tools/roles/handoff.py:307`).
- A create is a compare-and-swap with an empty expected sha, and a lost one reads `(stale info)` or
  `(fetch first)` (`tools/unattended/unattended.sh:2285`, `:2423`, `:2434`), the parse
  TOOL-dPlacedRequest-11 moves into `write_gov_ref` (I1).
- The driver resolves a sibling kit's file with `resolve_kit_dir "$py" <kit> <file> "$KIT_DIR"`
  (`resolve_kickoff_checker`, `:3700-3706`).

### The record and the store

| Where | What | Pushed |
|---|---|---|
| `refs/gov/requests/<content key>` | `content-key`, `fleet-tag`, `session` | yes, create-only |
| `refs/gov/leases/request/<content key>` | the lease record, kind `request` | yes, by acquisition |
| `<git-common-dir>/requests/<content key>.md` | the owner's words, byte for byte | never |
| `<git-common-dir>/requests/<content key>.typed` | one session id per line, each session that recorded it here | never |

The record's session is the first typer's and is provenance; the `.typed` file is this node's own
evidence of who typed it, and is what consent reads.

### The verbs

```
--request <file>               -> key = request.py key <file>
                                  copy to requests/<key>.md (first copy kept), add session to .typed
                                  write_gov_ref refs/gov/requests/<key> "" <commit>
                                  rc 0 written · rc 0 "already recorded" on a lost create · rc 2 not written
--lease acquire request <key> -> bounded read of refs/gov/requests/<key>; absent -> refused
                                  acquire derive_lease_ref request <key>, kind request
check_request_consent <key>    -> rc 0 this session typed it here · rc 1 relayed
```

### Inventory

| Identifier | Kind | Where |
|---|---|---|
| `derive_request_content_key` | function returning the I11 key `request_content_key` | `tools/loop/request.py` |
| `key` | CLI verb | `tools/loop/request.py` |
| `--request` | verb | `tools/unattended/unattended.sh` |
| `request` | a kind of `--lease` and `derive_lease_ref`, and a reserved slug | `tools/unattended/unattended.sh` |
| `write_request_record`, `check_request_consent` | functions | `tools/unattended/unattended.sh` |
| `refs/gov/requests/` | ref namespace | the remote |
| `refs/gov/leases/request/<content key>` | lease form, kind `request` | the lease grammar |
| `requests/` | node-local directory | `<git-common-dir>` |

Every function name leads with a verb of the naming lexicon's `VERBS` table (`.lexicon.conf`). I11
names the key `request_content_key`; a function by that name leads with `request`, which the table
does not declare, and would add a verb offender past `VERB_OFFENDER_PIN`. The key keeps its name, and
the function that derives it is `derive_request_content_key`, which every reader of the key calls.

### Files touched (estimate)

- `tools/loop/request.py`
- `tools/loop/kit.toml`
- `tools/loop/selftest.py`
- `tools/unattended/unattended.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/unattended/STOPS.template.md`, rendered to `memory/guides/UNATTENDED-STOPS.md`
- `tools/unattended/unattended.test.sh`

### Alternatives rejected

- **The text in the record.** That is the red case: the remote then holds the owner's words before any
  scan has read them.
- **A key hashed in the shell.** The normalisation would be a second copy of `derive_content_key`.
- **Consent read from the record's `session`.** Two sessions typing the same words share one record,
  so the second owner's own words would read as relayed; and the predicate would need the remote.

## 5. Production-readiness checklist

- security — a new write path to the remote carrying three shape-checked fields and no text, so the
  owner's words never leave the typing node; the local store sits in the git dir, untracked; consent
  is denied unless this session recorded the words here.
- perf / scale — one Python start for the key, one commit and one push per request; one bounded read
  per claim.
- error / empty / loading states — an empty request is refused before any write; an unreachable
  remote keeps the text local and exits 2; a missing loop kit refuses `--request` naming it.
- observability — every outcome is one `request —` line naming the key; a refused consent names the
  key and says relayed.
- risks — the stand-in trusts `--request`'s caller to pass the owner's words until the intake hook
  lands; the `.typed` file is local state a clone loses with its git dir.
- testing — AC1 to AC5 on fixtures and the arm in §7.
- migration — none: both namespaces and the store are new.
- user docs — the verbs and stops guides; no page under `help/` describes the driver's verbs.

## 6. Acceptance criteria

The fixture for AC2 to AC5 is a bare remote and two clones under `%TEMP%` with short names, each a
different session id and fleet tag of a fixture `fleet.toml`, the lease switch on, and a request file
carrying the marker `zq-request-marker-7`. The unattended kit's own suites are waived for this build's
landing (README rule 8), so each driver probe below is the observation.

- **AC1** — When `python request.py key` runs on two files differing only in case, whitespace and an
  ISO date, it prints one 12-hex key for both, and an empty file is refused.
  Red when: the key moves with a normalised difference, or an empty text is keyed.
- **AC2** — When clone A runs `unattended.sh --request req.md`, the bare remote holds
  `refs/gov/requests/<key>`, its message has exactly the three key lines, and
  `git -C <bare> cat-file --batch-all-objects --batch` piped to `grep -c zq-request-marker-7` prints
  `0`, while the clone's `<git-common-dir>/requests/<key>.md` is byte-identical to `req.md`.
  Red when: the marker is found on the remote; the planted case is a writer that puts the text in the
  record's message.
- **AC3** — When clone A runs `--request req.md` a second time, it prints that the request is already
  recorded, exits 0 and the remote ref is unmoved; a fleet tag absent from the registry refuses before
  any commit is built.
  Red when: a repeated request rewrites the record, or an unregistered tag reaches the remote.
- **AC4** — When clone B runs `unattended.sh --lease acquire request <key>` for A's request, the
  remote gains `refs/gov/leases/request/<key>` with `kind: request` naming B; clone A's acquisition
  then refuses with `live-holder`; a key with no record is refused with the remote unchanged; and
  `unattended.sh --lease acquire build request` is refused naming the reserved slug.
  Red when: a request cannot be claimed by another node, two holders land, a lease is taken on a key
  with no record, or a build lease takes the slug `request`.
- **AC5** — When a probe sources `unattended.sh` in clone A's typing session and calls
  `check_request_consent <key>`, it returns 0; in clone B, which received only the key, and in a
  second session on clone A, it returns 1 and prints `relayed`. The planted case is a relayed request
  offered as a breakpoint's disposition; the breakpoint's call of the predicate is
  TOOL-dPlacedRequest-5's and is observed there.
  Red when: a session that did not type the request reads as consent.
- **AC6** — When `grep -n -- "--request" tools/unattended/VERBS.template.md` and
  `grep -n "refs/gov/leases/request/" tools/unattended/STOPS.template.md` run, each finds its row, and
  the stops guide names the reserved slug `request`.
  Red when: either guide omits the verb, the lease form or the reservation.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `memory hygiene` · `lexicon naming predicates`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · the marker absent from every remote object, a repeated request, a claim by a second clone and a relayed consent, staged against the base driver, which has no request verb · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14
New arm: tools/loop/selftest.py · covers AC1 · the normalised pair keyed alike and the empty text refused, staged against a key over the raw bytes · none

## 8. Open questions

- **F1 — How is a request claimed by lease?** (a) A request lease `refs/gov/leases/request/<content
  key>`, kind `request`, acquired through TOOL-dPlacedRequest-1's verbs; (b) the record ref's own
  history carrying the lease keys; (c) no lease until placement makes the request a build. (c) fails
  the clause's "any node may claim by lease"; (b) puts lease renewals into the history the pre-claim
  draw rows ride (TOOL-dPlacedRequest-14) and more than the three fields I12 allows into the record. Rung 3 under the grant: the clause names the claim, so the lease grammar's
  one added form is its change. RESOLVED (agent, 2026-10-25, delegated): (a). grants:
  PLAY-dClosedLoop-3 the request form of the lease grammar · widens: none · relaxes: none
- **F2 — What does consent read?** (a) This node's `.typed` list of sessions that recorded the words
  here; (b) the record's `session` on the remote; (c) both. (b) reads a second typer of the same words
  as relayed and needs the remote; (c) inherits (b)'s defect. (a) is local, deny by default, and a node
  that only received the key never holds a line. Rung 3. RESOLVED (agent, 2026-10-25, delegated): (a).
  widens: none · relaxes: none
- **F3 — Where does the content key live?** (a) `tools/loop/request.py`, importing
  `derive_content_key`, beside the Python readers that key on it; (b) a shell copy of the
  normalisation in the driver; (c) a new verb in `row_grammar.py`. (b) is a second copy of a
  normaliser; (c) puts a request concept in the memory tree's row grammar. Rung 3. RESOLVED (agent,
  2026-10-25, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft.
- rev-2 · 2026-10-25 · fix brief, the spec stage's gate hits: the hands-off bullets to TOOL-dPlacedRequest-7,
  -4 and -21 name the `--request <content key>` argument those units take, and the one to -14 the
  `--request-text` path through `derive_request_content_key`; §7's leg line gains `recall floor` and
  `recall floor arms`.
- rev-3 · 2026-10-25 · §3 · the round-1 spec audit's disposal: hands-off TOOL-dPlacedRequest-30,
  hands-off TOOL-dPlacedRequest-31, hands-off TOOL-dPlacedRequest-32, hands-off
  TOOL-dPlacedRequest-34, each the mirror of that promoted unit's own edge.
- rev-4 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirror
  hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seams extended are the one compare-and-swap writer `write_gov_ref`, which TOOL-dPlacedRequest-11
extracts from `write_claim` (`tools/unattended/unattended.sh:2396`), for the record's create; the
normaliser `derive_content_key` (`tools/memory-tree/row_grammar.py:1475`), imported, for the key; the
git-dir local store pattern of the card (`skills/session-kickoff/manifest-check.sh:311-315`); and the
driver's sibling-kit lookup `resolve_kit_dir` (`:3700-3706`). The probe
`python tools/codebase-map/reuse_lookup.py "record an owner request locally and push only its content
key to the remote"` ranked name-stem hits (`key`, `records`, `write_record`, `check_lease_only_diff`),
none a request record. Scout B cited the card store at `manifest-check.sh:310-314`, which at
`c63aabbb` runs `:311-315`; the prompt record reader at `unattended.sh:3548` and `scan_secrets` at
`runlog_lib.py:522` agreed with source.

Recall terms used: `python tools/memory-recall/query.py "how does an owner request reach another node
without its text leaving the node" --terms "request record content key relay lease claim owner
verbatim redacted publish provenance consent"`
