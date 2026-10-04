# TOOL-aMendedFleet-9 — the daily held job's red suites reach the inherited-red HIGH auto-file

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 9

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-9-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-9-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The scheduled `held` job of the remote CI workflow reds suites on the default branch, and no record
names an owner for any of them. The unattended close already gives every INHERITED bar leg an owner
by auto-filing a HIGH ask. This unit routes the latest completed scheduled run's red held suites into
that same writer, so a red the daily job sees becomes one OPEN HIGH ask instead of a log nobody reads.

## 2. Scope (IN)

- **S1** — A reader in `tools/unattended/unattended.sh` reads the latest COMPLETED run of the declared
  workflow whose event is `schedule`, then every job of that run, through the public GitHub REST API
  with an anonymous HTTPS GET. It prints ONE liveness line naming the run id, its head sha, the count
  of held jobs read and the count red. Observed by AC1.
- **S2** — The reader is DEAD PROBE, printed as such and filing nothing, on each of these: the
  run's anchor URL is not a `github.com` repository; a response is not HTTP 200; no completed
  scheduled run exists; the run carries zero jobs named `held <suite>`; the jobs read do not equal the
  count the API declares. Observed by AC2.
- **S3** — The workflow file name comes from a new optional conf key `HELD_CI_WORKFLOW`, read from the
  project conf AS COMMITTED AT R with the existing `read_policy_key` parser, never from the working
  tree. Blank or absent is DARK: one announce line, no request made. A value outside
  `[A-Za-z0-9._-]+` ending `.yml` or `.yaml` is refused by name. Observed by AC5 and AC6.
- **S4** — For each held job whose conclusion is `failure` or `timed_out`, the writer files one ask in
  the running build's `BACKLOG.md` with a `SEV · HIGH` row and a `KEEP` row, through the existing
  `write_backlog_rows`, `derive_ask_seq` and `read_ask_back` helpers and the existing rollback, and,
  once after its loop when it filed at least one ask, the views helper `write_ask_views` that
  `TOOL-aMendedFleet-1` restores, called with the count filed exactly as `write_inherited_asks`
  calls it, so the generated views move with the rows. The ask text opens `held red: suite <name> red at <sha8> on the daily held job, run <run id>`, its
  `seen` locator is the suite's script at that sha when `read_leg_argv` resolves the suite in the leg
  manifest, else the workflow file at that sha, and its accept clause is that the suite is green on
  the daily held job at the default branch's tip. Observed by AC3.
- **S5** — REUSED BEFORE IT IS FILED: an ask whose text opens `held red: suite <name> red at ` for the
  same suite, in ANY build's `BACKLOG.md`, read back OPEN and HIGH by `ASKS_CMD` with its own home,
  is named and nothing is written. Observed by AC4.
- **S6** — Refusals at the write boundary: a suite name carrying a backtick, a control character,
  the ` · ` field separator or the ` → ` pointer arrow is not filed and is named; a head sha that is
  not an ancestor of R is not filed and is named. Observed by AC6 and AC7.
- **S7** — The `gates-green` item calls the writer once, after the bar has returned, on every return
  code, and the writer's outcome never changes the item's verdict. Observed by AC8.
- **S8** — The gates-green contract in `tools/unattended/STOPS.template.md`, its render
  `memory/guides/UNATTENDED-STOPS.md`, the kit README's close paragraph and
  `tools/unattended/.unattended.conf.example` name the route and the key; this repo's
  `.unattended.conf` declares `HELD_CI_WORKFLOW="remote-ci.yml"`. Observed by AC9.

## 3. Non-goals (OUT)

- Fixing any red suite. The census unit `TOOL-aMendedFleet-7` adds one unit per root cause.
- Making the CI job write anything. `.github/workflows/remote-ci.yml` declares `contents: read` and
  states it writes nothing to the repository; that stays true.
- Reading job LOGS. The logs endpoint wants credentials on this API, and the ask needs only the job's
  name and conclusion.
- A drift signal over the same API. `TOOL-aMendedFleet-8` owns `remote_ci_red_streak` in its own kit,
  and the kit ban forbids this kit naming that kit's file.
- Re-arming held self-tests at the push boundary, which would reverse the 2026-08-23 owner ruling.

### Edges

- **consumes-from** `TOOL-aMendedFleet-1` — `write_ask_views`, restored there; without it a filed
  held ask leaves the generated views stale and the close's records commit meets the freshness check.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified on 2026-10-04.

- `write_inherited_asks` in `tools/unattended/unattended.sh` files one OPEN HIGH ask per INHERITED
  leg of the bar's attribution record, reuses an OPEN one for the same leg and R, mints the id under
  the running slug, writes through `write_backlog_rows`, proves the write with `read_ask_back`, and
  rolls the file back from a `cmp`-proven backup when the read-back fails. It is called only from the
  `gates-green` item's red-bar branch.
- `read_gate_policy` reads conf keys at R through `read_policy_key`, parse-only, which is the read
  this unit reuses for its key.
- `.github/workflows/remote-ci.yml` names each held job `held ${{ matrix.name }}`, the matrix being
  the runner's `--list` population; the held job runs on `schedule` and `workflow_dispatch` only.
- Anonymous probe, 2026-10-04: the runs listing for `remote-ci.yml` with `event=schedule` answered
  200, the latest completed run `37196051126` at `c2ffcf87` carrying 86 jobs: 69 success, 15
  failure, 2 skipped. A workflow file that does not exist answered 404, which is the negative the
  liveness assertion needs. The report and the brief say this run redded 18 suites; the API says 15,
  the figure the synthesis also gave. Twelve of the fifteen names are legs in `tools/gate-legs.json`;
  the three unattended rows are not, which is why S4 has a fallback locator.

### Data model

The reader's output, one TAB row per held job, consumed by the writer and never persisted:

```
held<TAB><suite name><TAB><head sha 40-hex><TAB><run id><TAB><conclusion>
```

The ask, SEV and KEEP rows, in the grammar `tools/memory-tree/backlog.py` parses:

```
- <FAM>-<slug>-<n> · filed <date> · held red: suite <name> red at <sha8> on the daily held job, run <run id> · seen `<path>`@<sha8>[ run `<argv>`] · accept the suite is green on the daily held job at the default branch's tip
- SEV · <FAM>-<slug>-<n> · HIGH · a held self-test is red on the default branch's daily job
- KEEP · <FAM>-<slug>-<n> · filed by an unattended run for the owning build; outside this build's goal
```

### Inventory

- `read_held_reds` — the reader: anchor URL and the workflow file name in; TAB rows and the liveness
  line out. It re-checks the name's shape before building a URL from it.
- `write_held_asks` — the writer: slug, R, bar run dir in; reads `HELD_CI_WORKFLOW` from the conf at
  R, prints the DARK line or the refusal before any reader call, then staged rows and one line per
  suite out.
- `write_ask_rows` and `read_roster_family` — the backup, write, read-back and rollback block and the
  roster-family read, lifted out of `write_inherited_asks` unchanged so both writers share one copy.
- `HELD_CI_WORKFLOW` — the optional conf key, `kit.toml` `optional_keys`, defaulted blank on the
  driver's init block beside `ASKS_CMD`.

### The read, and its guard

Python through `resolve_python`, inline as `read_leg_argv` already does. The host is the literal
`api.github.com`; owner and repo are parsed from the anchor URL only when its host is `github.com`
and each part matches `[A-Za-z0-9._-]+`. HTTPS only, no redirect followed, no `Authorization`
header and no token read from anywhere, a 30-second timeout per request and a 4 MiB cap per
response. Jobs are paged at 100 until the API's `total_count` is reached. Two requests answer
today's population; the anonymous limit is 60 an hour.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/STOPS.template.md`
- `memory/guides/UNATTENDED-STOPS.md`
- `tools/unattended/README.md`
- `tools/unattended/.unattended.conf.example`
- `tools/unattended/kit.toml`
- `.unattended.conf`

### Rollout

Dark in every adopter, because the key ships blank. This repo arms it in `.unattended.conf`, so the
first close after landing files the standing reds as HIGH asks in that run's build. The kit version
bump is owed once, at this build's close, after the last move.

### Alternatives rejected

Candidates tested before choosing, per BUILD-METHOD M12, with the test that rejected each.

- **The `gh` CLI.** `git grep` for a `gh run` or `gh api` call over `tools`, `.githooks` and
  `skills` returned nothing, so it would be a new external dependency: M3 veto 2.
- **The CI job files the ask.** The workflow's `permissions:` block is `contents: read` and its
  header says it writes nothing; a write token is a repository setting, the owner's. M3 vetoes 2
  and 3.
- **A local re-run of the held suites through `--attribute`.** `run-selftests.sh --list` prices the
  population in hours, and the result would be this host's, not the daily job's. Fails the goal.
- **Firing at `--preflight`.** Its staged rows would sit under every pass of the run; `gates-green`
  already has the staging and commit path the inherited asks use.

## 5. Production-readiness checklist

- security — a new outbound read: fixed host, HTTPS only, no redirect, no credential, size and time
  capped. Untrusted job names reach a tracked file, so S6 refuses the grammar-breaking characters at
  the write boundary and the read-back proves the row parses.
- perf / scale — two HTTP requests per close, plus one `ASKS_CMD` read-back per candidate: about 3 s
  each at 457 live asks, measured on 2026-10-04.
- error / empty / loading states — every failure is a named DEAD PROBE line and files nothing; a
  green day prints `0 red` beside a non-zero job count.
- observability — one liveness line per close, and one line per suite: filed, reused or refused.
- risks — a persistent red files one ask the first time and is reused after. A renamed suite files a
  second ask under its new name.
- testing — fixture arms in the driver suite with the reader shadowed; a live read observed once.
- migration — none; the key is optional and blank by default.
- user docs — the gates-green contract and the kit README, S8.

## 6. Acceptance criteria

- **AC1** — When `read_held_reds` runs from a scratch script sourcing the reader's block of
  `tools/unattended/unattended.sh`, against this repository's anchor URL
  and `HELD_CI_WORKFLOW="remote-ci.yml"`, it prints a liveness line naming a run id, a sha and a
  non-zero held job count, and one TAB row per held job.
  Red when: the line reports zero held jobs over a run the API lists with jobs.
  cost: two anonymous HTTPS requests, seconds.
  figure: DERIVED from the API at observation time.
- **AC2** — When the same call is made with the anchor URL https://example.invalid/o/r.git, and again
  with `HELD_CI_WORKFLOW="no-such-workflow.yml"`, each prints a `DEAD PROBE` line naming the cause,
  the non-GitHub anchor and the HTTP 404 respectively, and emits no TAB row.
  Red when: either prints a zero red count instead of `DEAD PROBE`.
- **AC3** — When `write_held_asks` runs in a fixture clone under `%TEMP%` whose `.unattended.conf`
  declares `ASKS_CMD` as `python tools/memory-tree/gen_build_index.py --asks`, with `read_held_reds`
  shadowed to print two red rows at the fixture's HEAD, the build's `BACKLOG.md` gains two asks,
  each with a `SEV · HIGH` and a `KEEP` row, and `gen_build_index.py --asks <id>` reads each as OPEN
  and HIGH; stdout carries one `re-rendered the generated views for 2 filed ask(s)` line, and
  `python tools/memory-tree/gen_build_index.py --check` passes in the fixture.
  Red when: the rows are only printed, an ask reads back other than OPEN HIGH, or the views are left
  stale.
  fixture: a `git clone --local` of this repository under a short `%TEMP%` path.
- **AC4** — When `write_held_asks` runs a second time over the same two reds, and again with one of
  the two asks moved to another build's `BACKLOG.md`, it files nothing and prints `reused` for both.
  Red when: a second ask is filed for a suite that already has an OPEN HIGH one.
- **AC5** — When `HELD_CI_WORKFLOW` is blank in the fixture conf committed at R, `write_held_asks`
  prints the DARK line and the shadowed reader records no call.
  Red when: a request is made, or the key is read from the working tree rather than at R.
- **AC6** — When the shadowed reader emits a red row whose suite name carries a backtick, and the
  conf at R declares `HELD_CI_WORKFLOW` as the value ../x.yml, nothing is
  filed and each refusal is named.
  This is the staged break for both refusals.
  Red when: either row reaches `BACKLOG.md`, or the bad key value reaches a URL.
- **AC7** — When the shadowed reader emits a red row whose sha `git merge-base --is-ancestor` denies
  against the fixture's R, `write_held_asks` files nothing and its line names the sha.
  Red when: an ask is filed for a commit off the default branch.
- **AC8** — When `grep -n write_held_asks tools/unattended/unattended.sh` is run, the gates-green call
  site is a bare statement after the bar's loop and not inside any condition, and the AC2 and AC6
  calls each returned 0.
  Red when: the call's status reaches `DOD_OUT` or the item's return.
- **AC9** — When `bash tools/unattended/adopt-unattended.sh --check` runs, it reports the rendered
  guides current, and `grep -c HELD_CI_WORKFLOW` over `memory/guides/UNATTENDED-STOPS.md`,
  `tools/unattended/.unattended.conf.example` and `.unattended.conf` is non-zero in each.
  Red when: the template changed and its render did not.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · a shadowed held reader over a fixture backlog, against a writer that only prints · none

## 8. Open questions

- **F1 — Which channel reads the held job's verdicts?**
  Options: the `gh` CLI; a stdlib HTTPS read of the public API; the CI job writing the asks; a local
  re-run. §4 Alternatives rejected records the test that rejected each of the other three.
  RESOLVED (agent, 2026-10-04, delegated): a stdlib HTTPS read of the public REST API, anonymous,
  guarded as §4 states. It needs no new dependency and no write surface.
- **F2 — Where does the route fire?**
  Options: inside the red-bar branch beside `write_inherited_asks`; after the bar on every return
  code; at `--preflight`. The red-bar branch alone never sees the common case, a green bar over red
  held suites, because held suites are not bar legs.
  RESOLVED (agent, 2026-10-04, delegated): after the bar, on every return code, verdict untouched.
- **F3 — Over which records is an ask reused?**
  Options: this build's own, as `write_inherited_asks` does; any build's. A persistent daily red
  would otherwise collect one HIGH ask per closing build.
  RESOLVED (agent, 2026-10-04, delegated): any build's, read back OPEN and HIGH with its own home.
- **FACT-QUESTION · F4 — Is the job listing readable without a credential?**
  Probe: an anonymous GET of the runs and jobs endpoints for `remote-ci.yml`. Decides: 200 with jobs
  means S1 works without a token. Liveness: a non-existent workflow name answers 404.
  RESOLVED (agent, 2026-10-04, delegated): readable; 200 with 86 jobs, and 404 on the negative.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `write_inherited_asks` at base and an anonymous API probe.
- rev-2 · 2026-10-04 · S4 AC3 §3 §10 · cross-read with `TOOL-aMendedFleet-1`: base's
  `write_inherited_asks` is the copy a merge stripped of its views call, and that unit restores the
  call; this writer copied the stripped pattern. S4 now calls `write_ask_views` after its loop, AC3
  observes the render, and the edge declares the dependency.
- rev-3 · 2026-10-05 · §4 Inventory · build: the reader takes the workflow file name rather than the
  conf blob and R, because AC5 and AC6 need the DARK line and the key refusal printed with no reader
  call, so the writer reads the key at R and the reader has no use for R; the writer's rollback block
  and roster-family read are lifted into two shared helpers so `write_inherited_asks` and this writer
  run one copy of the existing rollback, as S4 says.

## 10. Reuse audit

The seam extended is the inherited-red auto-file in `tools/unattended/unattended.sh`:
`write_inherited_asks` as the pattern, and its helpers `write_backlog_rows`, `derive_ask_seq`,
`read_ask_back` and `read_leg_argv` called unchanged, with `read_policy_key` for the key at R, and
`write_ask_views` as `TOOL-aMendedFleet-1` restores it.
`python tools/codebase-map/reuse_lookup.py "file a HIGH ask for a red leg inherited from the default
branch"` printed `unscanned layers: .sh`, so it cannot see these shell seams; it named the
`run_bounded` seam and the `UNATTENDED-ASKS.md` guide, and the helpers were found by reading the
driver. Recall returned the owner ruling `TOOL-dDerivedDocket-76`, which owes the unattended kit's
compensating check to this same held job, and the inherited-red policy spec
`TOOL-dDerivedDocket-24`. Neither the report nor the tree disagree on the mechanism; they disagree on
the red count, 18 against 15, recorded in §4.

Recall terms used: inherited red auto-file HIGH ask held self-test daily schedule remote-ci gates-green ASKS_CMD backlog owner
