# KICK-dKeptSession-80 red-fix 21 — govkit selfcheck fixed in bfe2c300

**Serves:** red-fix KICK-dKeptSession-80

- **Leg:** govkit selfcheck
- **Red line:** govkit: entry 'unattended': tools/unattended/mail-notice.js carries gov:kit unattended@1.135 but the constant is 1.137
- **Files:** tools/unattended/mail-notice.js
- **Commit:** bfe2c300dbe24a7ce2ccfd60124e19aabf35bb7b
- **Rerun:** python tools/govkit/govkit.py selfcheck · no problem line printed
- **Caused-by:** KICK-dKeptSession-80
