# aHomedAnchor — asks

## Asks
- TOOL-aHomedAnchor-8 · filed 2026-10-09 · held red: suite codebase-map kit selftest red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/codebase-map/selftest.py`@40a8b8c3 run `python3 {prefix}/codebase-map/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-9 · filed 2026-10-09 · held red: suite foreign-prefix parity (every self-test at three prefixes) red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/run-gates/foreign-prefix.gov.test.sh`@40a8b8c3 run `bash {prefix}/run-gates/foreign-prefix.gov.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-10 · filed 2026-10-09 · held red: suite corpus-ids selftest red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/memory-tree/corpus_ids.py`@40a8b8c3 run `python3 {prefix}/memory-tree/corpus_ids.py --selftest` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-11 · filed 2026-10-09 · held red: suite lexicon selftest red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/lexicon/selftest.py`@40a8b8c3 run `python {prefix}/lexicon/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-12 · filed 2026-10-09 · held red: suite govkit selftest red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/govkit/selftest.py`@40a8b8c3 run `python {prefix}/govkit/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-13 · filed 2026-10-09 · held red: suite python resolver (behaviour + inline parity + idiom ban) red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/lib/resolve-python.test.sh`@40a8b8c3 run `bash {prefix}/lib/resolve-python.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-14 · filed 2026-10-09 · held red: suite runlog selftest red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/runlog/selftest.py`@40a8b8c3 run `python {prefix}/runlog/selftest.py` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-15 · filed 2026-10-09 · held red: suite run-gates gov canary red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/run-gates/run-gates.gov.test.sh`@40a8b8c3 run `bash {prefix}/run-gates/run-gates.gov.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-16 · filed 2026-10-09 · held red: suite run-gates canary red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/run-gates/run-gates.test.sh`@40a8b8c3 run `bash {prefix}/run-gates/run-gates.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-17 · filed 2026-10-09 · held red: suite run-gates run-log line red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/run-gates/run-gates.runlog.test.sh`@40a8b8c3 run `bash {prefix}/run-gates/run-gates.runlog.test.sh` · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-18 · filed 2026-10-09 · held red: suite unattended driver selftest shard 2/8 red at 40a8b8c3 on the daily held job, run 37770195629 · seen `.github/workflows/remote-ci.yml`@40a8b8c3 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-19 · filed 2026-10-09 · held red: suite unattended driver selftest shard 8/8 red at 40a8b8c3 on the daily held job, run 37770195629 · seen `.github/workflows/remote-ci.yml`@40a8b8c3 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-20 · filed 2026-10-09 · held red: suite unattended gate selftest shard 1/8 red at 40a8b8c3 on the daily held job, run 37770195629 · seen `.github/workflows/remote-ci.yml`@40a8b8c3 · accept the suite is green on the daily held job at the default branch's tip
- TOOL-aHomedAnchor-21 · filed 2026-10-09 · held red: suite unattended-build self-test red at 40a8b8c3 on the daily held job, run 37770195629 · seen `{prefix}/workflows/unattended-build.test.sh`@40a8b8c3 run `bash {prefix}/workflows/unattended-build.test.sh` · accept the suite is green on the daily held job at the default branch's tip

## Dispositions
- SEV · TOOL-aHomedAnchor-8 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-8 · by d006cfc569f22e9f893ae9b57998b47a8bda6c1b · green on the daily held job's run 38045767386 at d006cfc5, which carries this build's landing
- SEV · TOOL-aHomedAnchor-9 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-9 · by TOOL-aHomedAnchor-22 · red only through corpus-ids, whose CLI now writes UTF-8
- SEV · TOOL-aHomedAnchor-10 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-10 · by TOOL-aHomedAnchor-22 · corpus_ids.py writes UTF-8; observed with PYTHONUTF8=0
- SEV · TOOL-aHomedAnchor-11 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-11 · by TOOL-aHomedAnchor-22 · lexicon.py writes UTF-8; observed with PYTHONUTF8=0
- SEV · TOOL-aHomedAnchor-12 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-12 · by TOOL-aHomedAnchor-27 · govkit reads guarded paths as UTF-8, and its selftest prints UTF-8 (unit 22)
- SEV · TOOL-aHomedAnchor-13 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-13 · by d006cfc569f22e9f893ae9b57998b47a8bda6c1b · green on the daily held job's run 38045767386 at d006cfc5, which carries this build's landing
- SEV · TOOL-aHomedAnchor-14 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-14 · by TOOL-aHomedAnchor-22 · runlog.py writes UTF-8; its schema arms pass with PYTHONUTF8=0
- SEV · TOOL-aHomedAnchor-15 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-15 · by d006cfc569f22e9f893ae9b57998b47a8bda6c1b · green on the daily held job's run 38045767386 at d006cfc5, which carries this build's landing
- SEV · TOOL-aHomedAnchor-16 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-16 · by d006cfc569f22e9f893ae9b57998b47a8bda6c1b · green on the daily held job's run 38045767386 at d006cfc5, which carries this build's landing
- SEV · TOOL-aHomedAnchor-17 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-17 · by d006cfc569f22e9f893ae9b57998b47a8bda6c1b · green on the daily held job's run 38045767386 at d006cfc5, which carries this build's landing
- SEV · TOOL-aHomedAnchor-18 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-18 · by TOOL-aHomedAnchor-23 · the launcher arm reads only invocations; the shard itself not re-run, by the owner's ruling
- SEV · TOOL-aHomedAnchor-19 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-19 · by TOOL-aHomedAnchor-26 · the F4 harness initialises the filer's globals; the arm sliced green, the shard not re-run
- SEV · TOOL-aHomedAnchor-20 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-20 · by TOOL-aHomedAnchor-24 · --overlaps is on all three surfaces; the shard not re-run, by the owner's ruling
- SEV · TOOL-aHomedAnchor-21 · HIGH · a held self-test is red on the default branch's daily job
- CLOSED · TOOL-aHomedAnchor-21 · by TOOL-aHomedAnchor-28 · budget re-declared from readings; the suite passes 853 assertions alone
