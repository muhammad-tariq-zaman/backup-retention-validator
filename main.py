"""Backups vs the retention policy.

Usage: python3 main.py backups.csv --retention-days 30
CSV columns: backup,age_days.
KEPT within retention, PURGE DUE past it. Oldest first.
"""
import argparse, csv, sys

def validate(rows, retention):
    out = []
    for row in rows:
        age = int(row["age_days"])
        verdict = "PURGE DUE" if age > retention else "KEPT"
        out.append((row["backup"], age, verdict))
    return sorted(out, key=lambda r: -r[1])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--retention-days", type=int, default=30)
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        result = validate(list(csv.DictReader(f)), args.retention_days)
    for backup, age, verdict in result:
        print(f"{backup}: {verdict} ({age} days old)")
    print(f"{sum(1 for _, _, v in result if v == 'PURGE DUE')} purge-due backup(s).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
