# TOOL-dTotalRecall-79 — acceptance ledger

**Serves:** log TOOL-dTotalRecall-79
**Caused-by:** TOOL-dTotalRecall-79

No merge bar, no self-test suite, no gate leg and no run of the checker in this pass. The builder built spec rev-3 over
base `37805c48587f5453eca08ab23b59d6c5cdadc687` on node a, 2026-11-24. The pass edits no code and no stamp. §7's legs
are the close's.

The script is §4's fence, extracted from the spec to a file under the scratch directory and run from the repository
root. `$SWEEP` is the fenced block of `2026-11-24-build-TOOL-dTotalRecall-78-1-acceptance-ledger.md`, which holds no
`live` line. `$LIVE` is a `sep rc=0` line and the two `live` lines unit 77's AC1 answer quotes. Every sha the block
holds is in the history since `462d20f3`, so no read unit is placed by the script's default (DERIVED 2026-11-24, those
reads). The units it prints as `unresolved` are 8, 37, 14, 15 and 26, each DEFERRED with no pass commit.

The run with `$LIVE` appended, exit 0 (DERIVED 2026-11-24, that run):

```text
unresolved 8
unresolved 37
unresolved 14
unresolved 15
unresolved 26
span 22 22 checks 9 closed-by 3
span live live checks 9 closed-by OPEN
spans 2
```

The run over the sweep alone, exit 0 (DERIVED 2026-11-24, that run):

```text
unresolved 8
unresolved 37
unresolved 14
unresolved 15
unresolved 26
span 22 22 checks 9 closed-by 3
spans 1
```

The commits `git log --format=%h -G"^last-audit:" 462d20f3..HEAD -- memory/guides/SESSION-KICKOFF.md` prints, in its
order, 267 of them (DERIVED 2026-11-24, that command). The first 18 are the commits since the run's base `8b8b1374c`;
the rest are in that base's own history (DERIVED 2026-11-24, the same command from that base):

```text
67ffd1289 408d05723 f1e11ac49 6db81d070 926526b1c b9b6e584a 29b39e572 bd6fe04f8 6ea003891 71ce746a0
c34e46220 491dfe31c dcd8b10f7 202a354a4 305b6e9d1 3dc09b861 a9b4e3739 360b653fd 5e6582bea d5e93911a
275588a7f e6a1063fe f9ee3f8e0 f5200d5be 3fc130f1e ddf65d6a6 541f36073 6b3ebc830 7cf3999b8 bd7804842
b833648b1 0e5103294 563d828df fb276ac5e 6932f9604 f42c4ad16 4a7fff390 41efe4ddb 55e427e66 e52614f4e
636ec0364 79a4f9c20 ceeac2dcf dd90f8abb 38a68ee1d e896a6198 9991872c0 cf49c1ba4 8eabe6333 b843687cc
153d4bdb2 16942b7d6 f7526f6d8 b671830d8 6d1261958 ec34083bd 45786306b c91fc4e55 213693496 9a29f1e96
81657e77c 5a311c9fa c1eed311c e1efccc6b 450f7b322 25bfe539f 3a7a51471 25a3d2970 41e57fca5 6dee50847
0ccc23626 e4e4e7ef0 d92f12115 6b3f271c6 8b3aa5783 0179b44b6 7e5c9ae76 abe6ac994 4e6ac5f7c 9b4890561
177da4cba faf051f67 8eda4a5a0 511f0e560 b6c23d4fd c12df2635 6ffd8a882 a52352673 d065715b4 ffbe05eb4
c7f4ef116 29d86011b 1d284c8b4 aa9f30666 c06829447 2ef13a4f7 a62d74ea0 7d17b468d a4d443093 1c19bfc5a
37ecdd832 c9b504aa2 2e9ae09ab bb7da5acf e5758fbac a46ef3919 6ea5d9240 6f7655979 cf64f39df c0008f704
ad3c52205 a633e804c 0c8515bcf f9581f2c2 f77c5589d c83653a26 49cdded06 fd3540f17 a00867610 59f7c8466
1e11500da 9a03ec816 642b917ce ec4f22215 62c1a4ea4 1eb02bab3 bc12662b0 2535ad8cc 5cd36069d 063421425
634815f08 2a561b207 91e91ed35 613936d4f 817cda253 97f77a7f5 d0fc6bec7 ab2489c43 0ea0b59f6 32f7f9d33
95e4ae142 0742227b8 f261b5898 d46719074 b454f7be2 d3ee4c149 6b1c95b7d 29c9024c7 cf2c673f3 2ba17e9d6
cac14c195 796deda7a ef4855a15 8e4f578c3 a56828506 679697d7c 33a1a8676 de6e03312 25f552c45 cb1ee1c51
729762c56 0ea161c39 d4eb74047 e93d94201 6241e72bb 2990e7d32 c6c477853 aff14faae 229ba8652 56009a863
ee40561c9 2e8eade18 5e98256fe 0b5c6db20 26eda4214 3802bc13e 8b16e46fb 55d65f5c8 166c1fef7 e719dff11
19648821f 1aaeed338 f7a443aef da149de2f 06d9f5678 de358444f 1c542f9b8 9f9908aeb 8221b660d 8bf37ad53
c815d9d90 33aeaad98 60bbf65b2 b55a6494a 0fb95eeac e051539c1 af1d9fa91 778a60196 3ba738843 4b487529a
7067f1332 0bbaaa17d 9cc88e71d 4a505d04b fe437c995 399788aca dc84ea200 fe22fcf80 e3bd1ad45 0ccf8e449
1f078024a 3745b407a 34834d0c2 7b2153c28 df39f9560 9cb93347d 886c11fea f4d8db192 02b35d060 cc767f77a
e15a19acc 04bb021e6 1a804910b bcbbaea3f 5699553e8 a3430688d a3f5150b0 3e6336b05 f25d719e4 1f7d19660
5fe2dab8e ec870d637 0b3a27d7d f8f919882 09d6004c2 56aef62aa dfcef45a7 7c51ef25f 38d7f703a 0e392296e
8b379abf6 ec45d0f26 ed135af16 29ccb0652 64c85a989 263d31d59 82d3643cc 2550ccaa7 5e8c8c5e7 f2b41e328
4f52f18c9 f64846eb8 4f76c4b39 277c9e37f eb67e2cc8 5412bbecd 6fec8045b b663756ca 622aca88e f6674a6a2
4ad519f44 b441f50fc 47b56f1b2 69aa76517 5aca029f6 d939a396b c9bd97720
```

**Evidences:** TOOL-dTotalRecall-79
- AC1 — `span live live checks` — over the sweep with `$LIVE` appended the last span line is `span live live checks 9 closed-by OPEN`, and over the sweep alone the script prints `spans 1`. Both outputs stand in the fenced blocks above (DERIVED 2026-11-24, these two runs).
- AC2 — `git log --format=%h -G"^last-audit:" 462d20f3..HEAD -- memory/guides/SESSION-KICKOFF.md` — the one derived span is `span 22 22 checks 9 closed-by 3`. Unit 76's AC13 answer lists one red span, unit 22's `491dfe31c`, check 9, closed by unit 3's pass `f8b950c13`; it lists no check-5 span and none `OPEN`. By §4's rule they agree: AC13's check-9 span is inside the derived one and the closer is the same, unit 3. Unit 76's answer stands on a derivation seen to find a red. The stamp commits the command prints are the block above, whole; since the run's base they are `67ffd1289`, `408d05723`, `f1e11ac49`, `6db81d070`, `926526b1c`, `b9b6e584a`, `29b39e572`, `bd6fe04f8`, `6ea003891`, `71ce746a0`, `c34e46220`, `491dfe31c`, `dcd8b10f7`, `202a354a4`, `305b6e9d1`, `3dc09b861`, `a9b4e3739`, `360b653fd`. Between the red `491dfe31c` and the closer, `c34e46220` (`Pass: none`) moved `last-audit` and `last-body-change`. Those commits hold the passes unit 76's S19 names, `b9b6e584a`, `926526b1c`, `6db81d070` and `f1e11ac49`, and unit 70's `408d05723`, and none of units 60 and 69. No span differs, so no deviation record is written: `grep -l "AC13, the red spans" *-build-TOOL-dTotalRecall-76-deviation-*.md` lists nothing and exits 1, while `roster` for the pattern lists `2026-10-26-build-TOOL-dTotalRecall-76-deviation-761` (DERIVED 2026-11-24, these commands).
- AC3 — `base79 rc=` — the brief hands `base79 rc=0`, with no failure line beneath it, read at `07760b416cb73f8040eda7d29f6076d66fbce473`. `git diff --name-only` from that sha to this pass's base over each path of the `watch:` line and `memory/guides/SESSION-KICKOFF.md` prints nothing, and this pass writes none of them, so the tip answers the same; no remedy is owed and no stamp moved (DERIVED 2026-11-24, that command). The checker's verdict at the tip is the pass legs'.
