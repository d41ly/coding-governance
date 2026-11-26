# TOOL-dTotalRecall-78 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-78
**Caused-by:** TOOL-dTotalRecall-78

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-3 over
base `32fad8345c473d6fe0b5d8eb04476930d412eafb` on node a, 2026-11-24. The pass edits no code. §7's legs are the close's.

The main loop ran §4's sweep at `f1b815ced`, with unit 76's sweep output as `HAVE`, and handed its output in the brief
`2026-11-24-prompt-TOOL-dTotalRecall-78-build-brief.md`, which states that nothing printed on the error stream. The one
pass commit between that commit and this base is unit 77's, at step 36 and outside the population. §4's `awk` at the
base lists the population in the order the sweep visited it, and unit 81's `pass_of`, its fence run from a script file
over each unit, printed the sha or the named red the sweep prints for it, no line differing (DERIVED 2026-11-24, that
run). Every unit line of unit 76's block stands in this one. What the sweep read anew is the passes of units 76, 83 and
84, and units 8, 37, 14, 15 and 26 print their reds (DERIVED 2026-11-24, `comm` over the two blocks).

**Evidences:** TOOL-dTotalRecall-78
- AC1 — `population` — the sweep's output stands below, byte for byte. Its lines matching `^[0-9]+ ([0-9a-f]{40} rc=[0-9]+|red )` number 72, the value on its `population 72` line. Their first fields and the `awk` population at this base are one list by `cmp`, so each unit leads exactly one. No red line leads a CLOSED unit: the spec headers of units 8, 37, 14, 15 and 26 each read DEFERRED. The one non-zero status is unit 22's `rc=1`, with its check-9 line (DERIVED 2026-11-24, these reads).

```text
1 360b653fd27b7fefa4839bfb44884207230a66c6 rc=0
13 3dc09b8610f0046dcad7c3546f25f9e234241df0 rc=0
8 red no pass commit
18 305b6e9d1370cf97a92976e073aa564ae567d569 rc=0
37 red no pass commit
16 f36ec323c01b38a775873b202a0a71b23898b933 rc=0
25 a9f1e2a6839369d0b40006c53759845b73fd6d01 rc=0
5 202a354a4bc8b7eb317c2355fdd8e9809ad55e69 rc=0
38 2f59e5acb7c45d9a72b1cbdbb140ef1f09d55fe0 rc=0
4 dcd8b10f714157fb08b2af09e45f7c425ece7a46 rc=0
54 74af3faa40216c7a2a19aefd66b19847ac31b84f rc=0
40 dc1fd17e7ac27e25ffd729869a99c8b56699a4b7 rc=0
44 376f76cd2606e7b0c71599b8f21c55089da6a194 rc=0
45 c6fcf603b9ba3762af845e457f851d4068b19803 rc=0
46 63f283ddd38397f94a706bf942859d31179fd515 rc=0
6 ce198f66033d762db9ffe3d46f64752c8bb16264 rc=0
63 818591fc2b0b529588d9056aba6d39dc40df5aac rc=0
64 86360f071302e833e1b567e93b4c9453abc9a082 rc=0
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
47 a5f0166586158af426cc0cd3530d2bcb0b25f713 rc=0
48 4d1d9899acadbdd66f02af9e78d8100705447d85 rc=0
49 60424d69e5b45453e89edd5ce4aa4711a3c08916 rc=0
50 7f51d13ddb47c5ff3d66fd25fcff7d683349301f rc=0
51 30d1901d6aeaf615cab19366514dd0dadb1e52c0 rc=0
9 29b39e57245237223e3ce27112cc73f6ef547c89 rc=0
23 30d52b595b0b7c8477ac22b82eb14d4f92150be6 rc=0
61 778edd3a330784a2b68a75985d6fc629bf723145 rc=0
24 5d632d67de189b1025d43f044813223307d7bad3 rc=0
67 56390bab8cce52668b940893b8378621df78e4b7 rc=0
20 f6bdef7b4c6d70394c2ed7d0f80e7f905c829acb rc=0
71 5e004ad39095d3577d0368b8410c2fa190e39048 rc=0
72 35e956dc6b66e96e90e08f0a255b16aa61995d55 rc=0
17 30c21c834d24bdf968f0da62be6dd582add91642 rc=0
81 7e151e666b79e2438b7e65f8c8075b2843a3c7d5 rc=0
82 f4e82dad9d46c3e99619d3bdd96e461d0687537b rc=0
14 red no pass commit
15 red no pass commit
26 red no pass commit
12 6f7d5dd2c8773e973616589bc02b3f71e27d5e9b rc=0
43 b9b6e584a4812d37e37c2e18296f42a960c4a476 rc=0
52 926526b1c9125added7b6b2edbde490d99c0a3f4 rc=0
62 4975ccf29373577e7c1ba4608f13771144b4efb4 rc=0
53 6db81d070cea4ab52c719ffb0316748a32eaf840 rc=0
59 47afc89374e539d933728b5f0a06b9678a4ac388 rc=0
55 5b5895a493d4a47a0be4e417b1c5550cde92b001 rc=0
56 798f98fc1fa2c4af9feb68f8324f11c9d5339c8f rc=0
57 5ff76c2e273faa46b4490bde40ecb26478205de9 rc=0
58 7fd3f8e3817ee32b65edfd6f940d7dcc74518bcb rc=0
60 2ec3df383d4bf4be29d8b0cdc0ad6b9f073b69a9 rc=0
65 f1e11ac4933ff21ea5ee851f488dad17a313beef rc=0
66 17aac82e4c1eea50666618a8f62ead42d08364fa rc=0
68 7252440fd4871bbd72815d2f8dde38e4f404dbd5 rc=0
69 f7011dd6fc390d088e0d790c5e6c6901fd20edd6 rc=0
70 408d05723354b00d8e79aba5e6eb60868b8d15ce rc=0
73 6d0627dd6df306d627e2bbf841182d67499867a4 rc=0
75 59c4af40d0af08317a574eecf0485956a8c98429 rc=0
74 0114569d9558ebbd9440edadd97839306f60337b rc=0
87 073d03dd7df748eccc25079328c2199fa132c972 rc=0
76 67ffd12899cc7c20cc8399aca555360fec613886 rc=0
83 39ffc882ed18d2f5234fe4b86739ca4175a1d656 rc=0
84 f1b815ced4582351db667e5040288bdd9124d8f8 rc=0
population 72
```

- AC2 — `git grep -n "Evidences:\*\* TOOL-dTotalRecall-78" -- memory/builds/dTotalRecall/build` — run with `--untracked` before the commit, printed this ledger's block line, and the AC1 answer above holds the whole output in a fenced block. `git worktree list --porcelain` names no path ending `/gate-mc78`, and the common directory holds no such entry (DERIVED 2026-11-24, both reads).
