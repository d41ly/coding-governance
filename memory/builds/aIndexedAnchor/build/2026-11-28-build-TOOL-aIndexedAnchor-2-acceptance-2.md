# TOOL-aIndexedAnchor-2 acceptance 2 — re-run at 9968d68c

**Serves:** acceptance TOOL-aIndexedAnchor-2

- **Sha:** 9968d68ca7fb97828c512e62a8c07efb8ef2d9e7
- **Writer:** stand-in
- **Caused-by:** TOOL-aIndexedAnchor-2

run · 0 · e3b0c44298fc · bash -c '. tools/lib/resolve-python.sh && . tools/unattended/lib-unattended.sh && G=$(resolve_generated_indexes "$PWD" "$(read_conf_value .unattended.conf GENERATED_INDEXES)" memory); S=$(read_conf_value .unattended.conf SHARED_RECORDS); test "$(build_commit 229f1ddef..7a7566928 TOOL-aIndexedAnchor-1 memory/builds/aIndexedAnchor "$G" "$S")" = 398ba9252b2f1317024e200856c72cc7764a435a'
