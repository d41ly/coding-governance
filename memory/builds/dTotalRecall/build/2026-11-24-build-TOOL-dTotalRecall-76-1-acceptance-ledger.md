# TOOL-dTotalRecall-76 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-76
**Caused-by:** TOOL-dTotalRecall-76

No merge bar, no self-test suite and no gate leg ran in this pass. The builder built spec rev-4 over base
`b59778f81cc6693eea293a579a89bfd534ccee00` on node a, 2026-11-24, and ran each probe below there. §7's legs and its
`New arm:` RED-first observation are owed to the close.

No read was red, so no deviation record is written. The holding items, by id: S1 to S9, S11 to S15 and S19 to S23.
Built: S10 (AC5), S16 (AC10), S17 (AC11) and S18 (AC12). §B was re-read over the watched commits since `8b31081ac`,
of which there are none before this pass, and over this pass's two watched edits: none corrected. The 2026-11-10 dated
correction on `--act defer` stands and is reported, as unit 75's ledger reports it.

S2: unit 67's reading covers six of unit 61's eight amendments (DERIVED 2026-11-24, its AC1 line); its Goal's "each
amendment" is answered for the other two by AC1 here. S23: the ask is read by `record_causes.py#read_pinned_rows`.

The sweep of S19, as the main loop ran it at `073d03dd7`, this pass's base but for the spec commit `b59778f81`, which
carries no `Pass:` unit of its own (DERIVED 2026-11-24, that run). It is AC13's block, byte for byte:

```text
1 360b653fd27b7fefa4839bfb44884207230a66c6 rc=0
13 3dc09b8610f0046dcad7c3546f25f9e234241df0 rc=0
18 305b6e9d1370cf97a92976e073aa564ae567d569 rc=0
16 f36ec323c01b38a775873b202a0a71b23898b933 rc=0
25 a9f1e2a6839369d0b40006c53759845b73fd6d01 rc=0
5 202a354a4bc8b7eb317c2355fdd8e9809ad55e69 rc=0
54 74af3faa40216c7a2a19aefd66b19847ac31b84f rc=0
38 2f59e5acb7c45d9a72b1cbdbb140ef1f09d55fe0 rc=0
4 dcd8b10f714157fb08b2af09e45f7c425ece7a46 rc=0
63 818591fc2b0b529588d9056aba6d39dc40df5aac rc=0
64 86360f071302e833e1b567e93b4c9453abc9a082 rc=0
44 376f76cd2606e7b0c71599b8f21c55089da6a194 rc=0
46 63f283ddd38397f94a706bf942859d31179fd515 rc=0
40 dc1fd17e7ac27e25ffd729869a99c8b56699a4b7 rc=0
45 c6fcf603b9ba3762af845e457f851d4068b19803 rc=0
6 ce198f66033d762db9ffe3d46f64752c8bb16264 rc=0
22 491dfe31c4fb9890ce3086eb73793d40f10dce1d rc=1
22 491dfe31c4fb9890ce3086eb73793d40f10dce1d MANIFEST check 9 FAILED ? the manifest body has not changed across ten or more watched commits, so its front-loaded claims are drifting unverified; re-read ?B and advance last-body-change to a current sha: 10 non-merge commits since 2c621083fd91278f33ba1baba1ea15f4dada31b0
3 f8b950c13a5268c83b972599a4995df20ad88e29 rc=0
2 d91388c2f5cad72e9210e620b90910740f7c2dee rc=0
7 5688d011aca6312152d38a3c502ad51dce1835f3 rc=0
11 71ce746a07bcd5c8461c1ede47047ede33135d01 rc=0
41 c2814ccc0621de338a675ad15016599601dbbcf4 rc=0
10 d735e47b952d119bbf2425701a5f70bd75600498 rc=0
42 53496c0d164b756f358793f9f57bfbbe6561099a rc=0
19 6ea0038917b88da100410fad7c6831935375fb5d rc=0
21 bd6fe04f88e71f9f62dd797dd1108649b445b2bd rc=0
36 7ffe749aaf3510c6b087269597432efb930ad644 rc=0
39 d653803302f67dd57a492196a8f178e96c763558 rc=0
51 30d1901d6aeaf615cab19366514dd0dadb1e52c0 rc=0
47 a5f0166586158af426cc0cd3530d2bcb0b25f713 rc=0
48 4d1d9899acadbdd66f02af9e78d8100705447d85 rc=0
49 60424d69e5b45453e89edd5ce4aa4711a3c08916 rc=0
50 7f51d13ddb47c5ff3d66fd25fcff7d683349301f rc=0
9 29b39e57245237223e3ce27112cc73f6ef547c89 rc=0
23 30d52b595b0b7c8477ac22b82eb14d4f92150be6 rc=0
61 778edd3a330784a2b68a75985d6fc629bf723145 rc=0
67 56390bab8cce52668b940893b8378621df78e4b7 rc=0
24 5d632d67de189b1025d43f044813223307d7bad3 rc=0
20 f6bdef7b4c6d70394c2ed7d0f80e7f905c829acb rc=0
72 35e956dc6b66e96e90e08f0a255b16aa61995d55 rc=0
71 5e004ad39095d3577d0368b8410c2fa190e39048 rc=0
81 7e151e666b79e2438b7e65f8c8075b2843a3c7d5 rc=0
82 f4e82dad9d46c3e99619d3bdd96e461d0687537b rc=0
17 30c21c834d24bdf968f0da62be6dd582add91642 rc=0
12 6f7d5dd2c8773e973616589bc02b3f71e27d5e9b rc=0
43 b9b6e584a4812d37e37c2e18296f42a960c4a476 rc=0
62 4975ccf29373577e7c1ba4608f13771144b4efb4 rc=0
52 926526b1c9125added7b6b2edbde490d99c0a3f4 rc=0
53 6db81d070cea4ab52c719ffb0316748a32eaf840 rc=0
59 47afc89374e539d933728b5f0a06b9678a4ac388 rc=0
55 5b5895a493d4a47a0be4e417b1c5550cde92b001 rc=0
56 798f98fc1fa2c4af9feb68f8324f11c9d5339c8f rc=0
57 5ff76c2e273faa46b4490bde40ecb26478205de9 rc=0
58 7fd3f8e3817ee32b65edfd6f940d7dcc74518bcb rc=0
60 2ec3df383d4bf4be29d8b0cdc0ad6b9f073b69a9 rc=0
65 f1e11ac4933ff21ea5ee851f488dad17a313beef rc=0
68 7252440fd4871bbd72815d2f8dde38e4f404dbd5 rc=0
66 17aac82e4c1eea50666618a8f62ead42d08364fa rc=0
69 f7011dd6fc390d088e0d790c5e6c6901fd20edd6 rc=0
70 408d05723354b00d8e79aba5e6eb60868b8d15ce rc=0
73 6d0627dd6df306d627e2bbf841182d67499867a4 rc=0
75 59c4af40d0af08317a574eecf0485956a8c98429 rc=0
74 0114569d9558ebbd9440edadd97839306f60337b rc=0
87 073d03dd7df748eccc25079328c2199fa132c972 rc=0
live rc=1
live MANIFEST check 9 FAILED ? last-body-change names a commit unknown to this repository, so the stall baseline is foreign or predates a history rewrite: 0000000000000000000000000000000000000000
population 64
```

**Evidences:** TOOL-dTotalRecall-76
- AC1 — `holding only the build-folder rows this unit moves` — the blob probe printed 1 for it and 1 for the re-worded criterion naming `KEPT_PINNED` over unit 55's spec at `b9f735339150`, 1 for the hands-off and 1 for `git grep -n ALIAS_COMPARE_KEPT -- tools` over unit 56's at `1e9a5ebabf0d`, and 1 for the consumes-from over unit 57's at `c736ff00f780`; each printed 0 over the same spec at `653bed738`, and the older spelling of unit 55's criterion 0 at `b9f735339150` and 1 over spec 61. Both greps printed nothing, exit 1, at the tip, and the same grep for `CENSUS_KEPT_REGISTRY` printed four files (DERIVED 2026-11-24, these probes).
- AC2 — `absorbs` — the row left to unit 74; the nine other rows printed their wanted counts at pass(T)^: 1 for `no base re-key is built` (52), 0 for `it replaces unit 52's absorbed-population arm` (59), 1 for `ZED-aFoo-2`, 1 for `This unit's pass builds no body and observes that one`, 1 for `whose body unit 54 builds and this unit's criteria observe` and 0 for `whose body this unit rebuilds` (46), 1 each for the moved-rows sentences of 55 and 56 and 1 for `this one follows units 55 and 56` (57). Unit 70's AC1 line records that every row printed its wanted count, so each agrees. S6's two strings printed 0 each at `254057fa6d5b` and 1 each at `653bed738`; unit 70's AC8 line records 0 for each, so they agree (DERIVED 2026-11-24, the blob probe).
- AC3 — `git merge-base --is-ancestor <pass(38)> <pass(64)>` — exited 0, `git show --name-only` of pass(64) over unit 38's spec printed nothing, and the grep for `86360f071` printed deviation 1013 alone, whose Evidence names it and whose Departs from names unit 38's hands-off to unit 46 (DERIVED 2026-11-24, these commands).
- AC4 — `census-kept-paths.txt` — the `ast` probe printed one line, in `tree_lib.py`. `kept-row-editable`, `kept-row-drained` and `unkept-build-alias` each printed one `RED ` line naming the file, `marker-in-kept-script` one naming it under `memory/project/`, and `kept-row-docs-root` exited 0, its keep line ending `kept outside the write set` and its `read at` line naming `docs/memory/project/census-kept-paths.txt` (DERIVED 2026-11-24, these runs).
- AC5 — `GOV_REMOTE=nope GOV_DEFAULT_BRANCH=nope python record_causes.py --fixture --plant kept-row-drained` — exited 1 with the one `RED ` line it prints without them, and `alias-row-drained` under the same exports exited 1 with its own. At the base each exited 2, refused naming `GOV_REMOTE`. The grep for `kept-row-gained` and `compare_to_base` printed nothing, exit 1 (DERIVED 2026-11-24, these runs). The suite arm's own RED-first observation is owed to the close.
- AC6 — `%TEMP%` — the probe over the four files printed the one `user_skills` line of govkit's suite; over a scratch copy of `record_causes.py` holding a write to `/tmp/rc-fixed`, then to a drive-lettered temp path, it printed that line too (DERIVED 2026-11-24, this probe).
- AC7 — `write_rows` — the `factory` half printed one red, exit 1, for each plant but `kept-row-docs-root` and `adopter-no-registry`, exit 0 with none, each red the refusal its unit names; the `stale` half printed `not the key's fields, a count and every trailing field` for each plant that writes a registry and nothing for `adopter-no-registry`. Run at the base and again over this pass's edit, the two outputs equal. The source probe printed `True` (DERIVED 2026-11-24, these runs).
- AC8 — `git show <pass(68^)>:tools/lib/legacy_ledger.py` — read at `7252440fd^` it defines the four names, `ratchet.py` there defines `check_new_at_base`, and the grep over `tools/memory-tree` printed nothing, exit 1 (DERIVED 2026-11-24, these probes).
- AC9 — `ratchet.run_never_gains` — over the `legacy` fixture, a repository with no remote, printed `unresolved` with `no remote to compare against` and answered 1 (DERIVED 2026-11-24, this probe).
- AC10 — `['base', 'history']` — printed by the rows of `ratchet (never gains)`, `ratchet (seed laundering)` and `ratchet (rename)`, no class by every other row, and a non-empty `enforces` by each; the `resolve_compare_base` count printed 3; the second `leg_factory.py --write` found the manifest fresh and moved no byte (DERIVED 2026-11-24, these commands).
- AC11 — `grep -vE '^[[:space:]]*#' .memory-tree.conf | grep -c census-kept-paths` — printed 0 and the check-3 case count 1; check 3's verdict over gov is the pass legs' (DERIVED 2026-11-24, these commands).
- AC12 — `git merge-base --is-ancestor <W> <S>` — read before the commit as the staged diff: the watched paths `.memory-tree.conf` and `tools/gate-legs.json` move in the commit whose diff holds the new `last-audit:` line, so W and S are both this pass's commit; the count over the 11 watched paths since the new `last-body-change`, `b59778f81cc6693eea293a579a89bfd534ccee00`, is 0 before the commit and this commit's 1 after it, under the bound; unit 70's `408d05723` is an ancestor of the value, exit 0. The `Decided:` trailer names each §B claim re-read and `none corrected` (DERIVED 2026-11-24, these commands). The checker's own verdict is the pass legs'.
- AC13 — `MANIFEST check 9 FAILED` — the block above carries §4's sweep: 64 unit lines for `population 64`, and a `live` read of `rc=1` with its check-9 line. Its one red span is unit 22's `491dfe31c`, check 9, closed by unit 3's pass `f8b950c13`, the next pass commit read without it; no check-5 failure is printed and no span is `OPEN`. The line for pass(69), `f7011dd6f`, reads `rc=0` with no failure, which is C5's verdict there and answers unit 69's AC1 (DERIVED 2026-11-24, that run, read here).
- AC14 — `^- AC1 — .*Tip counts.*spec 55 .*spec 56 .*spec 57 .*form 1 in each of specs 55, 56 and 57` — the `grep -c` printed 1: six strings and three §9 forms on the one line, none void (DERIVED 2026-11-24, this command).
- AC15 — `git grep -n CAUSE_WRITER_PINNED -- tools` — printed nothing, exit 1, and `pinned-ask-is-spec` printed `PASS` with one `RED ` line naming its row and `TOOL-fRoot-1` (DERIVED 2026-11-24, these runs).
