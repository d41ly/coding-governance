# KICK-dKeptSession-80 widen 6 — unread-params widened

**Serves:** widen KICK-dKeptSession-80

- **Population:** unread-params
- **Keys:** `tools/loop/loop_transition.py	check_stood_in	root`, `tools/loop/loop_transition.py	check_stood_in	slug`, `tools/loop/loop_transition.py	resolve_no_bash	script`, `tools/policy/check_policy.py	check_load	e`, `tools/policy/check_policy.py	load_absent_by_key	top`, `tools/policy/check_policy.py	load_accept_all	here`, `tools/policy/check_policy.py	load_accept_all	top`, `tools/policy/check_policy.py	seed_namespace_new	repo`, `tools/policy/check_policy.py	seed_namespace_new	rows`, `tools/policy/policy.py	read_default_value	build`, `tools/policy/policy.py	read_file_value	build`, `tools/policy/policy.py	read_preset_value	build`, `tools/policy/policy.py	read_preset_value	row`, `tools/policy/policy.py	read_scenario_value	table`
- **Reason:** every one is a parameter a fixed call shape passes: the four policy.py readers share one resolution-order signature, as read_file_value's docstring states, and the loop_transition.py and check_policy.py ones are stand-ins, plants and check callbacks that must take the shape of the function or list they stand in, so none can be dropped
- **Caused-by:** KICK-dKeptSession-80
