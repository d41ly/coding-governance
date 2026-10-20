# Research: Cloud coordination: the platform's limits, terms and security

**Serves:** research PLAY-dClosedLoop-1

This is dispatch 152's return, verbatim, except that a title line would be demoted to keep one H1 per record. Its question is in `prompts/2026-10-19-prompt-PLAY-dClosedLoop-1-27-researcher.md`, and its use is in `build/2026-10-19-build-PLAY-dClosedLoop-1-cloud-and-scale.md`.

---

**THE PLATFORM: what Anthropic's limits, terms and security allow and require of node units and a head**

All outside sources below were read on 2026-10-19. I wrote nothing in the repository. The scratch folder `.../scratchpad/d152/` was created for the hardware probe and then deleted. `git status` shows no change apart from the five untracked prompt files that were already there.

**Re-verified handed facts.**
- **Principles:** P3, P5, P21, P22, P23, P25, P26, P28, P36 and P39 read as handed (architecture-v2 `[principles]`, lines 680–900).
- **Policy rows:** `runtime.act-auth` (v2:1193), `memory.mirror` (v2:1165), `leases.offline` (v2:972) and `run.host` (v2:1030) read as handed. So do `kits.host` (v2:1108), `maintain.host` (v2:1112), `notify.channel` (v2:1032) and `notify.owner-items` (v2:1033).
- **Coordination records:** the mailbox ref `refs/gov/mail/<slug>/<fleet tag>/<session>` is at coordination `[feature]` unit 6. Runtime's `[extend]` has eleven points, and every adapter row carries a grant (layer-runtime:834–863).
- **Claims on the remote:** `git ls-remote origin 'refs/gov/*'` returned `17 refs/gov/runs`. The claim is pushed by `git push --force-with-lease ... $c:$CLAIM_NS/$slug` (`tools/unattended/unattended.sh:2423`), with `CLAIM_NS="refs/gov/runs"` (`:2087`). The fleet register lists tags a to d (`tools/playbook/fleet.toml`).
- **Charter:** the `[security]` line is at `coding-governance-agents.template.md:38`.
- **Records against code:** I found no case where a record and the code disagree.

## 1. Plan limits and how a node can measure them

**Findings**
- **Pro and Max** have "a five-hour session limit and a weekly limit… shared across Claude and Claude Code" (support 11145838). Max adds "a separate weekly limit for Fable". Weekly amounts are not published.
- **Team and Enterprise:** "each member's Claude Code usage draws from a per-seat allowance that resets on a rolling five-hour window and a weekly window", sized by seat tier (costs doc). Usage-based Enterprise has "no per-seat usage limits… billed at API rates" (support 11845131).
- **Scope of a subscription limit:** it is per account or per seat, not per machine. Cloud sessions "share rate limits with all other Claude and Claude Code usage within your account". Routines "draw down subscription usage the same way". The consequence: every node signed into one account draws on one five-hour and one weekly pool.
- **Model-family limits:** "You've hit your Opus limit" can be avoided by switching model family. Session and weekly limits are "shared across all models" (costs doc).
- **API keys:** limits are "set at the organization level", measured as requests, input tokens and output tokens per minute, "for each model class". They use a token bucket that refills continuously, plus a monthly spend cap per tier. Workspaces can have lower spend and rate limits, and "organization-wide limits always apply" (rate-limits doc).

**Five ways to read remaining allowance, each with the test that would make it lose**

| Candidate | Losing test | Result |
|---|---|---|
| (a) Transcript `quotaLimits` (what `tools/runlog/extract.py:648-653` reads today) | Does it ever carry a non-rejected reading? | **Loses as a live reading.** Measured over this node's `~/.claude/projects/**/*.jsonl` (read only): 650 occurrences in 208 files, every one `"status":"rejected"`. That is 365 `five_hour` and 285 `seven_day`, with no utilization field. It records the hit after the fact, never the headroom. |
| (b) Status-line JSON `rate_limits.five_hour/seven_day.used_percentage` and `resets_at` | Is it present on every plan, in headless (`-p`) acts? | **Partly loses.** It is documented as "only for claude.ai Pro and Max subscribers… and only after the first API response". Team and Enterprise seats get nothing. The status line is an interface feature under the workspace-trust rule, and the docs do not say it runs under `-p`. The build must test this: run `claude -p` with a `statusLine` that writes its stdin to a file; if no file appears, headless acts cannot read it. |
| (c) stream-json / Agent SDK `rate_limit_event` | Does it carry utilization while allowed? | **Loses on current evidence.** Only third-party issue reports exist, and they say utilization is absent while the status is `allowed` (claudeissues 77018, 50518). The official headless doc documents only `system/api_retry` with `error: rate_limit`. |
| (d) API response headers (`anthropic-ratelimit-*-remaining`, `-reset`) | Is the reading fresh, and is it the node's own? | **Fresh, but organization-wide.** It comes on every response, which is the freshest reading available. It shows "the most restrictive limit currently in effect" for the organization or workspace, not the node. It exists only on API-key authentication. |
| (e) Usage and Cost Admin API | Fresh enough for scheduling? Covers subscriptions? | **Loses for scheduling.** "typically… within 5 minutes", polling "once per minute"; "unavailable for individual accounts"; covers API usage only. The Enterprise Analytics API is daily. |

The one mechanism the platform itself enforces is **one API workspace per node, each with its own workspace rate limit or spend limit**. That turns allocation into a platform-enforced cap rather than a head's estimate, and it is API-key only.

**Hardware load on a node**, measured on this node (Windows 11, Python 3.14.5, 16 CPUs):
- `os.getloadavg` is missing (`getloadavg False`) and `psutil` is not installed.
- Standard-library `ctypes` (`GlobalMemoryStatusEx` + `GetSystemTimes`) returned `mem_load=76% avail_GB=7.4 cpu_busy=4%` in about 1 ms plus the 250 ms sampling window.
- PowerShell `Get-CimInstance` took 4359, 2152 and 1958 ms. That is too slow to run at every item.
- Linux and macOS have `os.getloadavg` ("Availability: Unix", docs.python.org). Memory comes from `/proc/meminfo` on Linux or a `sysctl`/`vm_stat` subprocess on macOS. I did not measure those here; the build must time them.

**What this means for each shape**
- **Headless:** each node can report only its own hardware load, plus subscription headroom on Pro/Max interactive sessions. Claims must assume nodes on one account share one pool.
- **Agentless head:** it can schedule only on readings the nodes push. On subscriptions those readings are coarse and partly post-hoc, so it needs a "pool" concept: nodes grouped by the account they draw from.
- **Agent head:** the same as the agentless head, plus the head's own usage counts against its own pool.

## 2. Terms

**Clauses, quoted**
- **Consumer Terms** (effective 8 Oct 2025, §3 item 7), which govern Free, Pro and Max: users may not "access the Services through automated or non-human means, whether through a bot, script, or otherwise", "Except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it". §2 adds: "You may not share your Account login information… or make your Account available to anyone else." The page I fetched says it is written for EEA/Swiss residents. The same clause appears in the archived versions search returned.
- **Claude Code Legal and compliance:**
  - "Advertised usage limits for Pro and Max plans assume ordinary, individual usage of Claude Code and the Agent SDK."
  - "OAuth authentication… is designed to support ordinary use of Claude Code and other native Anthropic applications."
  - "Developers building products or services… including those using the Agent SDK, should use API key authentication… developers may not collect, store, or intermediate Claude.ai credentials or session tokens."
  - It also says this does not prevent "an end user from signing in to the unmodified Claude Code binary with their own Claude subscription".
  - For hosted products: "Customers may not pay for, resell, or intermediate Claude usage on their end users' behalf."
- **Agent SDK overview:** "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK."
- **Automation the platform explicitly permits on a subscription:** `claude setup-token` is "for CI pipelines and scripts". GitHub Actions takes `claude_code_oauth_token`. Routines run on the subscription.
- **Usage Policy** (the page shows "Effective November 12, 2026", a date after today): it prohibits "Resell, proxy, or otherwise provide access to Claude through unauthorized means" and "create multiple accounts, to avoid detection, circumvent product guardrails". It also says "Agentic use cases must comply with the Usage Policy."
- **Commercial Terms** (effective 17 Jun 2025): "Anthropic may not train models on Customer Content." It also bars building a competing product.
- **Background:** the weekly limits announced in July 2025 named "running Claude Code continuously in the background, 24/7" and account sharing (TechCrunch, 28 Jul 2025, a secondary source).

**Where the terms are ambiguous**
1. Whether one owner's subscription login on several of the owner's own machines, running unattended, is "ordinary, individual usage". It is not sharing with "anyone else". But the stated limits assume ordinary use, and nothing defines what an ordinary fleet looks like.
2. Whether a gov supervisor (a third-party program) launching the unmodified `claude` binary under the user's own subscription is "explicitly permitted" automation. The setup-token and CI text points to yes for the user's own scripts. gov is also a shipped product, which points to API keys.
3. Whether the Agent SDK is allowed for an individual's own use on their own subscription. The February-2026 ban text quoted in third-party GitHub issues is gone from the current page, and the SDK overview's note still covers only offering login to third parties.

The legal page itself directs these questions to sales. Treat this as an owner action, not a design fork.

**What this means for each shape**
- **Headless:** the safest shape. Each node is the user's own unmodified Claude Code on the user's own credential. The endpoint carries no Anthropic credential and no usage.
- **Agentless head:** it is not an Anthropic customer itself. It must never hold, mint or relay node credentials or setup tokens, and never pay for or route usage for adopters.
- **Agent head:** on an API key it is clearly permitted and metered. On a subscription it is ambiguous (points 1 to 3). If gov ships it to adopters as a product, it falls under "Developers… should use API key".

## 3. Cloud runtimes

| Runtime | Authentication | Persistence | Network | Limits |
|---|---|---|---|---|
| **Cloud sessions** (claude.ai/code, `claude --cloud`) | Subscription only; an API key in the environment "doesn't override" it. Pro, Max, Team, and Enterprise premium seats. | Fresh VM per session; setup-script snapshot cached for about 7 days; an idle VM pauses and "can later be reclaimed". | Trusted allowlist by default; GitHub only through a proxy. The proxy "rejects branch deletions and pushes of anything other than a branch, such as a tag" and rejects GraphQL. | 4 vCPU, 16 GB RAM, 30 GB disk; usage counts against the plan. |
| **Routines** (scheduled / API `/fire` / GitHub) | claude.ai account only; each routine has its own bearer token. | One cloud session per run. | As cloud sessions. | Research preview. Minimum interval 1 hour. 100 scheduled runs/hour per account; 30/hour per routine for Run now and API fires. Fire text is wrapped as untrusted, and "can't act as approval or consent". Pushes go to `claude/` branches by default. |
| **Self-hosted environments** | Shared environment key; sessions use "Anthropic-issued, session-scoped OAuth". | Your own hosts. | Outbound only. The runner holds a lease of about 60 s and locks to one owner. | Team and Enterprise public beta, off by default. Session content still goes to `api.anthropic.com`. |
| **Remote Control server mode** (`claude remote-control --spawn worktree --capacity N`) | Full claude.ai login. "API keys are not supported", and setup tokens "can't establish Remote Control sessions". | Local machine. | Outbound only. | Capacity defaults to 32; the server exits after about 10 minutes when it loses the connection. |
| **Projects** | Subscription. | Project memory files; instructions up to 16,000 characters. | Cloud threads. | Public beta, Pro/Max only. Thread limits "aren't a hard cap". |
| **GitHub Actions** (`claude-code-action`) | API key, setup token, or workload identity federation (no stored secret). For a shared org secret, use an API key. | Runner. | GitHub-hosted. | Action minutes plus tokens; `--max-turns`. Custom refs are writable (GitHub itself serves today's 17). |
| **Agent SDK on a server** | `ANTHROPIC_API_KEY`; bare mode never reads OAuth. | Local disk unless a `SessionStore` is set; transcripts only. | Whatever you allow. | No session timeout of its own; about 1 GiB RAM and 1 CPU per agent. |
| **Managed Agents** | API key only; beta header. | Sessions stored server-side. | Managed or self-hosted sandbox. | 300 create / 1,200 read requests per minute; not eligible for zero data retention. |

**Losing test against the planned design:** gov's leases, claims and mailbox all live under `refs/gov/*`. Those pushes are not branches, so Anthropic-hosted cloud sessions and routines **cannot write them**, according to the cloud-environments doc. The build must confirm this by pushing `refs/gov/leases/probe` from a cloud session and expecting a rejection. A cloud node can only join through self-hosted git credentials, GitHub Actions, or a ref namespace placed under branches.

There is also a timing risk. `--bare` "will become the default for `-p`", and bare mode reads neither the OAuth login nor `CLAUDE_CODE_OAUTH_TOKEN`. When that happens, `runtime.act-auth: setup-token, oauth-shared` breaks on headless acts unless the harness adapter opts out of bare mode explicitly.

**What this means for each shape**
- **Headless:** runs on any of the runtimes, but each cloud host must declare whether it can write refs.
- **Agentless head:** fits a small always-on service, a GitHub Actions cron, or a routine (one-hour minimum, so not real time).
- **Agent head:** fits the Agent SDK on a server or Managed Agents on an API key. Anthropic's own Projects is a first-party example of an agent head on a subscription, but only inside Anthropic's product. That is one line for the agent-head researcher.

## 4. Security and tenancy

**What relaying to an endpoint exposes**
- **Retention of model traffic:** prompts and outputs go to Anthropic on every path. Consumer accounts keep them 30 days, or 5 years if training is allowed; commercial accounts 30 days or zero retention (data-usage doc).
- **The endpoint is a new copy of the code:** memories, decisions and diffs relayed to it put the adopter's code on a third system. Neither of Anthropic's retention terms covers it; the endpoint's own retention and access policy do.
- **Secrets in shared configuration:** cloud environment variables are "visible to anyone who uses the environment". Network secrets stay outside the VM, injected by Anthropic's agent proxy.
- **Untrusted relayed text:** the routine `/fire` design treats relayed text as untrusted and never as consent. gov's P13 makes the same rule for unenveloped text.
- **Isolation between adopters:** the SDK hosting doc lists what a shared host needs: per-tenant `CLAUDE_CONFIG_DIR`, `setting_sources=[]`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, a per-tenant `cwd` and per-tenant egress. Self-hosted runners lock to one owner.
- **Credential storage on Windows:** the credential file is `%USERPROFILE%\.claude\.credentials.json`, protected by the profile's access controls, not an OS keychain.

**What the charter's `[security]` rule and `runtime.act-auth` require**
- The endpoint or head never receives an Anthropic credential: no token in a record, a mailbox message or a capacity report.
- Each node authenticates itself.
- The head's own grant (git write, an API key) sits in a registered adapter's grant row, held by reference (layer-runtime:860–863), at the narrowest scope. Workload identity federation lets a GitHub Actions head hold no stored secret at all.
- The secret value scan (`runtime.secret-scan`) must also run at the endpoint's publish boundary.

**Offline-first (P3)**
- **Headless:** with the endpoint down, a node keeps its local verdict, its leases as `leases.offline` says, and the mailbox ref in git as the record.
- **Agentless and agent head:** a head may only advise or assign. It is never a verdict path and never the only holder of a lease or an assignment. Otherwise a node with the head down cannot reach a verdict, which breaks P3 and P22.

## Seams and invariants the architecture must carry now

| # | Seam or invariant | Owning layer | Cost while gov stays offline |
|---|---|---|---|
| S1 | **Capacity is a typed, sourced reading.** The node registry's runtime facts (layer-runtime:825) gain a node-scope reading command adapter: hardware via the standard library, plus allowance with its source (`statusline`, `quota-rejected`, `api-headers`, `admin-api`, `unknown`), its freshness, and its **pool id** (the account, seat or workspace it draws on). Under P23, a head trusts it only by key and source. | Runtime (registry, reading adapter); Memory declares the record kind | One record kind. The hardware probe costs about 1 ms on Windows through ctypes; never use PowerShell CIM per item. |
| S2 | **The pool, not the node, is the limit unit.** Admission (`runtime.agents-in-flight`) and P39's waits read a pool's reset time (`resets_at`) as a deadline. A rejected-quota hold resumes at the reset instant, as `unattended.sh:1195` already does. | Runtime | None; it generalizes today's hold. |
| S3 | **Auth is per process role, not global.** `runtime.act-auth` stays for acts. A head or endpoint adapter declares its own auth class in its grant row (api-key or WIF by default). Host adapters declare the auth class they require: routines, `--cloud` and Remote Control need a full claude.ai login and refuse setup tokens. The harness adapter's capability rows (P36) record bare-mode credential reading as a row. | Runtime (grant rows, harness rows) | Two capability rows plus one fixture; no new key yet. |
| S4 | **Coordination refs sit behind a transport adapter, not a hard-coded `refs/gov/*`.** Each host declares a `can-write-custom-refs` capability. An Anthropic-hosted cloud host fails it, so it either uses a branch-namespaced fallback or cannot acquire a lease. | Flow owns the lease and mail contract; Runtime owns host capability | One capability row; the ref grammar stays as is. |
| S5 | **No credential crosses a coordination record.** The secret value scan covers lease, mail and mirror payloads, and Memory's write door refuses token shapes in those kinds. | Runtime (scan); Memory (`record` door) | The existing scan, given more surfaces. |
| S6 | **A relayed prompt is data with provenance, never consent or an instruction.** An owner query reaches a node as a typed `intake` record (P26) naming its sender. Only the owner's own session can confirm a breakpoint. | Flow (mail kinds); Instruction (P13 envelope) | None; this restates P13 and P26 for a new carrier. |
| S7 | **A head is advisory and expansion-only (P28).** Assignment is a lease the node acquires itself (P5). The head never holds the only copy of state, and its absence drops back to headless. | Expansions (integrations: a head adapter); core unchanged | None. |
| S8 | **Per-adopter isolation.** A head or mirror adapter declares its tenancy (single adopter, or multi-adopter with per-adopter config directory, working directory and egress). `memory.mirror` adapters declare retention and region. | Runtime (adapter row fields) | Two fields on adapter rows. |
| S9 | **Terms are an owner-held fact, not a policy guess.** A registry row records which auth classes the owner has confirmed for unattended fleet use. The `oauth-shared` and `setup-token` defaults carry the ambiguity note above until the owner records an answer from Anthropic. | Instruction (owner decision record) | One decision entry. |

**Out of my scope, one line each:**
- A git-remote mailbox as the headless endpoint belongs to the census researcher.
- Anthropic's self-hosted runner (queue, lease of about 60 s, capacity, single-owner lock) is prior art for the agentless head.
- Projects is prior art for the agent head.

Sources:
- [Use Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan)
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Claude Code: Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance)
- [Claude Code: Authentication](https://code.claude.com/docs/en/authentication)
- [Claude Code: Manage costs](https://code.claude.com/docs/en/costs)
- [Claude Code: Status line](https://code.claude.com/docs/en/statusline)
- [Claude Code: Headless](https://code.claude.com/docs/en/headless)
- [Claude Code in the cloud](https://code.claude.com/docs/en/claude-code-on-the-web)
- [Cloud environments](https://code.claude.com/docs/en/cloud-environments)
- [Routines](https://code.claude.com/docs/en/routines)
- [Projects](https://code.claude.com/docs/en/claude-projects)
- [Self-hosted environments](https://code.claude.com/docs/en/self-hosted-environments)
- [Remote Control](https://code.claude.com/docs/en/remote-control)
- [GitHub Actions](https://code.claude.com/docs/en/github-actions)
- [Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)
- [Agent SDK hosting](https://code.claude.com/docs/en/agent-sdk/hosting)
- [Data usage](https://code.claude.com/docs/en/data-usage)
- [API rate limits](https://platform.claude.com/docs/en/api/rate-limits)
- [Usage and Cost API](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
- [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)
- [Consumer Terms](https://www.anthropic.com/legal/consumer-terms)
- [Commercial Terms](https://www.anthropic.com/legal/commercial-terms)
- [Usage Policy](https://www.anthropic.com/legal/aup)
- [Python os module](https://docs.python.org/3/library/os.html)
- [TechCrunch, weekly limits, 2025-07-28](https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/)
- [claudeissues 77018](https://claudeissues.com/issue/77018-expose-rate-limit-utilization-used-percentage-in-headless-contexts-stream-json-o)
- [claudeissues 50518](https://claudeissues.com/issue/50518-claude-agent-sdk-expose-per-bucket-rate-limit-utilization-to-headless-sdk-consum)
- [Aperant issue 1871](https://github.com/AndyMik90/Aperant/issues/1871)
- [Autonomee terms explainer](https://autonomee.ai/blog/claude-code-terms-of-service-explained/)
