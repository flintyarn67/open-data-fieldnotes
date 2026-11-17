"""Summarize CSV completeness using only the Python standard library."""
import argparse
import csv
import json
from pathlib import Path


def profile(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        reader = csv.reader(source)
        headers = next(reader, None)
        if not headers or any(not name.strip() for name in headers):
            raise ValueError("CSV must contain nonempty column names")
        if len(set(headers)) != len(headers):
            raise ValueError("CSV column names must be unique")
        missing = [0] * len(headers)
        rows = 0
        for row in reader:
            if len(row) != len(headers):
                raise ValueError(f"Record {rows + 2} has an unexpected column count")
            rows += 1
            for index, value in enumerate(row):
                missing[index] += not value.strip()
    return {"rows": rows, "columns": [
        {"name": name, "missing": count, "present": rows - count}
        for name, count in zip(headers, missing)
    ]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_path", type=Path)
    args = parser.parse_args()
    try:
        result = profile(args.csv_path)
    except (OSError, UnicodeError, csv.Error, ValueError) as error:
        parser.exit(2, f"error: {error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
