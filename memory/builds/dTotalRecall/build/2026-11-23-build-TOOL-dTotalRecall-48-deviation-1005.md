# TOOL-dTotalRecall-48 deviation 1005 — the run record schema leg's closed rule list gains check_cause_line's cause rule

**Serves:** deviation TOOL-dTotalRecall-48

- **Departs from:** TOOL-dTotalRecall-48@rev-3
- **Hand-off:** spec-to-code
- **Before:** TOOL-dTotalRecall-48 §4 Inventory mints nothing and its Files touched name tools/runlog/record.py and tools/runlog/selftest.py; no section names tools/runlog/record.py#RECORD_RULES, the schema leg's closed list every refusal of a record names, which does not carry check_cause_line's rule cause
- **After:** tools/runlog/record.py#RECORD_RULES carries cause, and tools/runlog/selftest.py#test_schema_ac2_refusals stages a cause unserved variant at line 4, so the arm's every-rule-staged assertion holds with the rule in the list
- **Cause:** builder discovery
- **Reason:** S1 wires check_cause_line into check_record_lines, so a record's refusal can name cause; the RECORD_RULES comment states every refusal names one of its rules, and the runlog selftest asserts the staged rules equal RECORD_RULES, which a cause refusal outside the list would red at the close
- **Evidence:** TOOL-dTotalRecall-48 S1 and S2; tools/runlog/record.py#RECORD_RULES and #check_cause_line, tools/runlog/selftest.py#test_schema_ac2_refusals in the pass's second commit
- **Risk:** additive
- **Approver:** author, the gov-builder pass of TOOL-dTotalRecall-48 under the build's author-recorded value (PLAY-dClosedLoop-4)
- **Follow-through:** ask TOOL-dTotalRecall-27
- **Caused-by:** TOOL-dTotalRecall-48
- **Made-by:** owner
