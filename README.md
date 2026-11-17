# Open Data Fieldnotes

Notes and reproducible examples for exploring public datasets and designing clear visualizations.

## Quick start

Requires Python 3.9 or newer; no additional dependencies are needed.

```sh
python3 scripts/profile_csv.py examples/sample.csv
```

The sample is synthetic, not a real public dataset. It contains three rows;
`observations` has one missing value. The command prints JSON counts for each
column without disclosing cell values.

Empty or whitespace-only fields count as missing. Source-specific markers such
as `NA` remain values: document and normalize these explicitly before analysis.
Duplicate or empty column names and inconsistent row widths are rejected.
Header-only tables produce zero rows; completely empty files are rejected.

## Workflow

1. Complete the [dataset checklist](docs/dataset-checklist.md).
2. Run the profiler against a local CSV encoded as UTF-8 (an optional BOM is accepted).
3. Investigate missing values before making comparisons or charts.
4. Record transformations and include the source and units with every figure.

The profiler streams rows and reports completeness only. It does not infer
numeric types, validate statistical assumptions, or detect duplicate records.
