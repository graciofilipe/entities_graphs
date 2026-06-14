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
        {"person_id": "p1", "name": "Alice", "age": 30},
        {"person_id": "p2", "name": "Bob", "age": 25},
        {"person_id": "p3", "name": "Charlie", "age": 35},
        {"person_id": "p4", "name": "Diana", "age": 28},
        {"person_id": "p5", "name": "Eve", "age": 40}
    ]

    places_data = [
        {"place_id": "pl1", "name": "Central Park", "type": "Park"},
        {"place_id": "pl2", "name": "Empire State Building", "type": "Building"},
        {"place_id": "pl3", "name": "Statue of Liberty", "type": "Monument"},
        {"place_id": "pl4", "name": "Times Square", "type": "Square"},
        {"place_id": "pl5", "name": "Brooklyn Bridge", "type": "Bridge"}
    ]

    relationships_data = [
        {"person_id": "p1", "place_id": "pl1", "visit_date": "2023-05-01", "relationship_type": "VISITED"},
        {"person_id": "p2", "place_id": "pl2", "visit_date": "2023-06-15", "relationship_type": "VISITED"},
        {"person_id": "p3", "place_id": "pl3", "visit_date": "2023-07-20", "relationship_type": "VISITED"},
        {"person_id": "p4", "place_id": "pl4", "visit_date": "2023-08-10", "relationship_type": "VISITED"},
        {"person_id": "p5", "place_id": "pl5", "visit_date": "2023-09-05", "relationship_type": "VISITED"}
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
