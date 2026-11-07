# backup-retention-validator

Check each backup against the retention policy in days: anything older is purge-due, oldest first, so storage is reclaimed on schedule.

## How to run

```sh
python3 main.py backups.csv --retention-days 30
```

## Example output

```
DB-2026-09-01: PURGE DUE (64 days old)
DB-2026-10-30: KEPT (5 days old)
1 purge-due backup(s).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
