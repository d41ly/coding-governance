# KICK-dKeptSession-80 widen 7 — quoting-sites widened

**Serves:** widen KICK-dKeptSession-80

- **Population:** quoting-sites
- **Keys:** `tools/unattended/pass-tree.test.sh	heredoc-source`, `tools/unattended/unattended.sh	tab-ifs-read`
- **Reason:** the eight tab-ifs-read sites added by this run split the mailbox's and the claim listing's own rows, whose writers print '-' for a blank optional field and refuse a blank required one, so no empty field can collapse (read_mailbox's awk); pass-tree.test.sh's second heredoc writes a fixture renderer into the suite's scratch repository, as its first does
- **Caused-by:** KICK-dKeptSession-80
