# KICK-dKeptSession-5 red-fix 17 — shell hygiene (a loop fed by a command substitution) fixed in f453dc51

**Serves:** red-fix KICK-dKeptSession-5

- **Leg:** shell hygiene (a loop fed by a command substitution)
- **Red line:** sh-hygiene: tools/unattended/unattended.sh: the registry declares 2 site(s) at <<< and the scan measures 4 — write_mail_ack and print_mailbox each fed a while-loop by a here-string over a command substitution
- **Files:** tools/unattended/unattended.sh
- **Commit:** f453dc51897813e8234ca1753f20e72d23d12eea
- **Rerun:** bash tools/run-gates/pass-legs.sh --base c9e89a057e57904a6525ac6e7b09cfce4eb04e99 · gates RED 3/28 at f453dc51897813e8234ca1753f20e72d23d12eea: this leg green; lexicon naming predicates, lexicon wiring and memory hygiene inherited from origin/main 8b8b1374
- **Caused-by:** KICK-dKeptSession-5
