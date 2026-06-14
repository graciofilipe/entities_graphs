# Entities Graphs

This project uses BigQuery graph capabilities to analyze entities and relationships, starting with "people" and "places".

## Setup

1. Create a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`

## Testing

Run the test suite using pytest:
`python -m pytest tests/`

## Documentation

When developing for this project, you must consult the BigQuery Graph Documentation:
- [Graph Overview](https://docs.cloud.google.com/bigquery/docs/graph-overview)
- [Create Graphs](https://docs.cloud.google.com/bigquery/docs/graph-create)
- [Graph Query Best Practices](https://docs.cloud.google.com/bigquery/docs/graph-query-best-practices)
(See `gemini.md` for a full list of documentation links).
