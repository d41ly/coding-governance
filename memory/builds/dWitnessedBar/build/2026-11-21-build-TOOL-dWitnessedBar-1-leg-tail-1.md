# TOOL-dWitnessedBar-1 leg-tail 1 — drift-audit records failed in run unattended-179529481580044524711-1640412

**Serves:** leg-tail TOOL-dWitnessedBar-1

- **Leg:** drift-audit records
- **Hash:** b930f547759c2f680a7db50efcbc1928921f3593
- **Run:** unattended-179529481580044524711-1640412
- **Sha:** f9ee3f8e0f2e994c7bad52ae0779fcf31c9c94db
- **Cause:** run:dWitnessedBar

```
# run-gates | leg drift-audit records | exit 1
lexicon: 8 file(s) not graded here — kit files .governance/install.json installed at gov's own bytes, which gov grades, and .governance/, the deployer's state

drift-report: non_terminal_specs_cited_by_product_source = 2 against drift-baselines (1 listed) — this set is shrink-only
  new   PLAY-dClosedLoop-1 — an offender the set does not list: remove its cause, never list it
# drift-report at f9ee3f8e (base refs/remotes/origin/main @ c2a407b0) · kit 1.35
# dead-for-N: 173 readings recorded at C:\projects\coding-governance\.git\drift-history.tsv · limit 10
# signal                                             value     of  status
  lexicon_marginal_offense_rate                        968  10214  report only, no pin
  ledger_rows_contradicting_git                          0      0  empty by declaration — nothing to measure here yet
  non_terminal_specs_cited_by_product_source             2     30  OVER BASELINE — gateable
  shrink_only_lists_not_shrinking                       23     36  over pin 0 (report only)
  handkept_inventories_disagreeing_with_source           0     28  ok (pin 0)
  dangling_pointers_in_own_ledger                       11    115  report only, no pin
  closed_specs_with_no_product_commit                    1   2024  ok (baseline 1)
  lexicon_verbs_declared_but_unused                      0     23  ok (pin 0)
  lexicon_ratified_older_than_language_surface           0      1  ok (pin 0)
  live_backlog_rows_per_shard                          813    164  report only, no pin
  asks_disposed_overrides                                0    121  ok
  readme_mechanism_drift                                 6     39  over pin 4 (report only)
  backlog_asks_contested                                 0   1210  ok
  backlog_evidence_sha                                   0     77  ok
  backlog_asks_unlabelled                              432    813  ok (pin 447, drain it)
  open_asks_cited_by_product_source                     55    813  report only, no pin
  cutoff_keys_armed                                     39     39  ok (pin 39, drain it)
  source_cited_ids_resolving_to_no_record               24   1985  over pin 2 (report only)
  backlog_stragglers                                     0    198  ok
  run_records_nonterminal_but_merged                    12    137  over pin 2 (report only)
  aborted_work_landed                                    0     13  ok
  discarded_work_landed                                  0     13  DEAD PROBE for 173 readings — take it out of SIGNALS, or file an ask and declare it in DEAD_FILED
  legs_retried_after_timeout                            10    161  over pin 0 (report only)
  fleet_over_budget                                      0      5  ok
  remote_ci_red_streak                                   0      0  not asked — skipped under --check and --offenders: the merge bar's leg makes no network call for a value it does not grade
  dossiers_older_than_their_paths                       33     34  over pin 26 (report only)
  live_builds_without_activity                          21     43  report only, no pin
  gate_health                                           -1    119  n/a

# detail: rerun with --json
drift-report: 28 history rows appended to C:\projects\coding-governance\.git\drift-history.tsv
```
