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

## Running the Toy Setup

To initialize the toy dataset, tables, and property graph, and then seed it with toy data:

1. Create the dataset and graph:
   ```bash
   python3 src/bigquery_graph_setup.py --project your-project-id --dataset entities_graph_toy
   ```
2. Seed the tables with toy data (people, places, and relationships):
   ```bash
   python3 src/seed_toy_data.py --project your-project-id --dataset entities_graph_toy
   ```
