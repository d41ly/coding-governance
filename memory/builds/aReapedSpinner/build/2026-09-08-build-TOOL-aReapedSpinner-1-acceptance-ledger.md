# Acceptance ledger — aReapedSpinner, all seven units

**Serves:** journal TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

One line per numbered criterion, in the two forms the grammar allows and no third. The token names
the arm, command or file that made the observation, and it is taken FROM the criterion — so a line
here is answerable against the spec rather than a restatement of it.

**What the suites were when this was written.** The kit suite ran 65 assertions with 0 failures and
one announced environmental skip; the adopter suite ran 31 with 0 failures, including the hook's
census bound observed firing at 90s. The gate-runner teardown arms ran 5, and were observed RED
against the pre-change runner first — 0 passed, 5 failed, with the leg and its grandchild both
surviving.

**One criterion is NOT observed and says so.** Unit 7's AC5 covers the DELEGATED kill path, and
every bar run in this environment left the runner unattributable, so that branch was never entered.
The fallback it falls back to is observed three ways. The gap is carried in that unit's section 8
and in the wrap-up, not hidden behind a green line.

**Evidences:** TOOL-aReapedSpinner-1
- AC1 — `test_row_contract_is_complete` — observed in the kit suite, 57 assertions, 0 failed
- AC2 — `test_both_kinds_are_present_and_distinguished` — observed in the kit suite, 57 assertions, 0 failed
- AC3 — `test_posix_fixture_collapses_both_namespaces` — observed in the kit suite, 57 assertions, 0 failed
- AC4 — `test_no_backend_refuses` — observed in the kit suite, 57 assertions, 0 failed
- AC5 — `test_live_read_sees_itself` — observed in the kit suite, 57 assertions, 0 failed
- AC6 — `test_hung_backend_is_bounded` — observed in the kit suite, 57 assertions, 0 failed
- AC7 — `test_partial_rows_survive_and_are_counted_apart` — observed in the kit suite, 57 assertions, 0 failed
- AC8 — `test_continuation_rows_are_rejected_and_counted` — observed in the kit suite, 57 assertions, 0 failed
- AC9 — `test_non_utf8_backend_output_survives` — observed in the kit suite, 57 assertions, 0 failed
- AC10 — `test_summary_counts_are_derived` — observed in the kit suite, 57 assertions, 0 failed
- AC11 — `test_every_live_row_answers_its_own_liveness_probe` — observed in the kit suite, 57 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-2
- AC1 — `test_scope_over_the_frozen_corpus_is_exact` — observed in the kit suite, 57 assertions, 0 failed
- AC2 — `test_declared_root_admits_and_names_it` — observed in the kit suite, 57 assertions, 0 failed
- AC3 — `test_closure_reaches_bare_argv_and_native_descendants` — observed in the kit suite, 57 assertions, 0 failed
- AC4 — `test_self_chain_is_in_scope_but_not_killable` — observed in the kit suite, 57 assertions, 0 failed
- AC12 — `test_live_scope_is_not_empty` — observed in the kit suite, 57 assertions, 0 failed
- AC13 — `test_msys_edges_are_translated_before_the_union` — observed in the kit suite, 57 assertions, 0 failed
- AC14 — `test_cyclic_graph_terminates` — observed in the kit suite, 57 assertions, 0 failed
- AC5 — `test_blank_roots_refuses` — observed in the kit suite, 57 assertions, 0 failed
- AC6 — `test_root_that_claims_everything_refuses` — observed in the kit suite, 57 assertions, 0 failed
- AC7 — `test_prefix_is_separator_anchored` — observed in the kit suite, 57 assertions, 0 failed
- AC8 — `test_assignment_inside_a_dash_c_body_does_not_admit` — observed in the kit suite, 57 assertions, 0 failed
- AC9 — `test_recycled_parent_edge_is_dropped_and_counted` — observed in the kit suite, 57 assertions, 0 failed
- AC10 — `test_explain_answers_one_row` — observed in the kit suite, 57 assertions, 0 failed
- AC11 — `test_no_command_row_can_be_a_descendant_but_not_a_root` — observed in the kit suite, 57 assertions, 0 failed
- AC15 — `test_shipped_conf_admits_this_repo` — observed in the kit suite, 57 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-3
- AC1 — `test_every_verdict_member_has_a_producing_fixture` — observed in the kit suite, 57 assertions, 0 failed
- AC2 — `test_ceiling_decides_before_any_label` — observed in the kit suite, 57 assertions, 0 failed
- AC3 — `test_orphan_outranks_rate` — observed in the kit suite, 57 assertions, 0 failed
- AC4 — `test_native_parentless_row_is_orphan_and_reaped` — observed in the kit suite, 57 assertions, 0 failed
- AC5 — `test_live_windows_parent_is_not_an_orphan` — observed in the kit suite, 57 assertions, 0 failed
- AC6 — `test_rate_boundary_and_unknown` — observed in the kit suite, 57 assertions, 0 failed
- AC7 — `test_summary_counts_are_derived` — observed in the kit suite, 57 assertions, 0 failed
- AC8 — `test_unreadable_input_is_not_a_clean_report` — observed in the kit suite, 57 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-4
- AC1 — `test_mixed_namespace_tree_dies_completely` — observed in the kit suite, 57 assertions, 0 failed
- AC2 — `test_leaves_are_killed_first` — observed in the kit suite, 57 assertions, 0 failed
- AC3 — `test_survivor_is_derived_from_a_re_read` — observed in the kit suite, 57 assertions, 0 failed
- AC4 — `test_member_outside_the_scope_set_is_dropped` — observed in the kit suite, 57 assertions, 0 failed
- AC5 — `test_mode_bounds_the_act` — observed in the kit suite, 57 assertions, 0 failed
- AC6 — `test_dry_run_walks_the_same_set_and_kills_nothing` — observed in the kit suite, 57 assertions, 0 failed
- AC7 — `test_explicit_kill_still_obeys_membership` — observed in the kit suite, 57 assertions, 0 failed
- AC8 — `test_out_of_scope_root_refuses_before_the_walk` — observed in the kit suite, 57 assertions, 0 failed
- AC9 — `test_msys_row_is_signalled_by_the_kill_binary` — observed in the kit suite, 57 assertions, 0 failed
- AC10 — `test_non_msys_row_is_signalled_by_taskkill` — observed in the kit suite, 57 assertions, 0 failed
- AC11 — `test_unaddressable_row_is_reported_not_claimed` — observed in the kit suite, 57 assertions, 0 failed
- AC12 — `test_sweep_counts_are_derived_and_complete` — observed in the kit suite, 57 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-5
- AC1 — `test_hook_reports_a_flagged_row` — observed in the adopter suite, 26 assertions, 0 failed
- AC2 — `test_throttle_suppresses_the_second_run` — observed in the adopter suite, 26 assertions, 0 failed
- AC3 — `test_throttled_path_spawns_nothing` — observed in the adopter suite, 26 assertions, 0 failed
- AC4 — `test_clean_is_silent` — observed in the adopter suite, 26 assertions, 0 failed
- AC5 — `test_wiring_is_idempotent` — observed in the adopter suite, 26 assertions, 0 failed
- AC6 — `test_session_start_ignores_the_throttle` — observed in the adopter suite, 26 assertions, 0 failed
- AC7 — `test_broken_monitor_fails_open` — observed in the adopter suite, 26 assertions, 0 failed
- AC9 — `govkit.py selfcheck` — observed in the adopter suite, 26 assertions, 0 failed
- AC8 — `test_hung_census_does_not_block_the_hook` — observed in the adopter suite, 26 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-6
- AC1 — `govkit.py selfcheck` — observed in the adopter suite, 26 assertions, 0 failed
- AC2 — `test_blank_roots_refuses` — observed in the adopter suite, 26 assertions, 0 failed
- AC3 — `test_check_refuses_without_repairing` — observed in the adopter suite, 26 assertions, 0 failed
- AC4 — `check-kit-placeholders.py` — observed in the adopter suite, 26 assertions, 0 failed
- AC5 — `govkit.py selfcheck` — observed in the adopter suite, 26 assertions, 0 failed
- AC5b — `test_roots_hole_probe_fails_when_blank` — observed in the adopter suite, 26 assertions, 0 failed
- AC8 — `test_shipped_roots_exclude_the_temp_root` — observed in the adopter suite, 26 assertions, 0 failed
- AC6 — `test_readme_states_what_it_does_not_check` — observed in the adopter suite, 26 assertions, 0 failed
- AC7 — `test_version_from_names_a_file_this_unit_ships` — observed in the adopter suite, 26 assertions, 0 failed

**Evidences:** TOOL-aReapedSpinner-7
- AC1 — `test_signal_path_reaps_the_tree` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC2 — `reap.py` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC3 — `bash tools/run-gates/run-gates.sh` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC4 — `scope.py --explain` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC5 — `test_wrong_namespace_id_refuses_with_its_own_message` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC7 — `test_teardown_reap_cannot_strand_the_turnstile` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
- AC6 — `test_walked_and_killed_are_reported_apart` — observed in the teardown arms, 5 assertions; observed RED first against the pre-change runner
