# TOOL-dTotalRecall-115 widen 28 — shell-role widened

**Serves:** widen TOOL-dTotalRecall-115

- **Population:** shell-role
- **Keys:** `tools/lib/gov-feed.sh`, `tools/push-main.sh`, `tools/run-gates/post-merge.sh`, `tools/unattended/unattended.sh`, `tools/memory-tree/gov-claim.sh`, `tools/unattended/unattended.test.sh`
- **Reason:** the change feed's record append tests each key the log holds and its check walks from every logged commit, and the suite's record-feed block gains the merge landing
- **Caused-by:** TOOL-dTotalRecall-115
