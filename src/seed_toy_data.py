import argparse
import logging
import sys
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_data(project_id: str, dataset_id: str):
    client = bigquery.Client(project=project_id)
    dataset_ref = f"{project_id}.{dataset_id}"

    people_data = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
        {"name": "Diana", "age": 28},
        {"name": "Eve", "age": 40},
        {"name": "Filipe Gracio", "age": 35},
        {"name": "Mario Vlachakis", "age": 30}
    ]

    places_data = [
        {"name": "Central Park", "type": "Park"},
        {"name": "Empire State Building", "type": "Building"},
        {"name": "Statue of Liberty", "type": "Monument"},
        {"name": "Times Square", "type": "Square"},
        {"name": "Brooklyn Bridge", "type": "Bridge"}
    ]

    relationships_data = [
        {"source_entity": "Alice", "target_entity": "Central Park", "date": "2023-05-01", "relationship_type": "VISITED"},
        {"source_entity": "Bob", "target_entity": "Empire State Building", "date": "2023-06-15", "relationship_type": "VISITED"},
        {"source_entity": "Charlie", "target_entity": "Statue of Liberty", "date": "2023-07-20", "relationship_type": "VISITED"},
        {"source_entity": "Diana", "target_entity": "Times Square", "date": "2023-08-10", "relationship_type": "VISITED"},
        {"source_entity": "Eve", "target_entity": "Brooklyn Bridge", "date": "2023-09-05", "relationship_type": "VISITED"},
        {"source_entity": "Filipe Gracio", "target_entity": "Mario Vlachakis", "date": "2023-09-06", "relationship_type": "TALKED_TO"}
    ]

    try:
        logger.info("Inserting people data...")
        errors = client.insert_rows_json(f"{dataset_ref}.people", people_data)
        if not errors:
            logger.info("Successfully inserted 5 rows into people.")
        else:
            logger.error(f"Errors inserting into people: {errors}")

        logger.info("Inserting places data...")
        errors = client.insert_rows_json(f"{dataset_ref}.places", places_data)
        if not errors:
            logger.info("Successfully inserted 5 rows into places.")
        else:
            logger.error(f"Errors inserting into places: {errors}")

        logger.info("Inserting relationships data...")
        errors = client.insert_rows_json(f"{dataset_ref}.relationships", relationships_data)
        if not errors:
            logger.info("Successfully inserted 5 rows into relationships.")
        else:
            logger.error(f"Errors inserting into relationships: {errors}")

    except Exception as e:
        logger.error(f"Failed to seed data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Seed BigQuery property graph tables with toy data.")
    parser.add_argument("--project", default="filipegracio-ai-learning", help="GCP Project ID")
    parser.add_argument("--dataset", default="entities_graph_toy", help="BigQuery Dataset ID")
    
    args = parser.parse_args()
    seed_data(args.project, args.dataset)
