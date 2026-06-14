import logging
from google.cloud import bigquery

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GraphSetup:
    """Sets up the BigQuery datasets, tables, and property graphs."""
    
    def __init__(self, project_id: str, dataset_id: str):
        self.client = bigquery.Client(project=project_id)
        self.dataset_id = dataset_id
        self.dataset_ref = f"{project_id}.{dataset_id}"

    def create_dataset(self):
        dataset = bigquery.Dataset(self.dataset_ref)
        dataset.location = "US"  # Adjust location as needed
        dataset = self.client.create_dataset(dataset, exists_ok=True)
        logger.info(f"Dataset {dataset.dataset_id} created or already exists.")

    def create_node_tables(self):
        # People Table
        people_schema = [
            bigquery.SchemaField("person_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("age", "INTEGER"),
        ]
        people_table = bigquery.Table(f"{self.dataset_ref}.people", schema=people_schema)
        self.client.create_table(people_table, exists_ok=True)
        
        # Places Table
        places_schema = [
            bigquery.SchemaField("place_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("type", "STRING"),
        ]
        places_table = bigquery.Table(f"{self.dataset_ref}.places", schema=places_schema)
        self.client.create_table(places_table, exists_ok=True)
        logger.info("Node tables (people, places) created.")

    def create_edge_tables(self):
        # Relationships Table (e.g., VISITED)
        relationships_schema = [
            bigquery.SchemaField("person_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("place_id", "STRING", mode="REQUIRED"),
            bigquery.SchemaField("visit_date", "DATE"),
            bigquery.SchemaField("relationship_type", "STRING"), # e.g., "VISITED", "LIVES_IN"
        ]
        relationships_table = bigquery.Table(f"{self.dataset_ref}.relationships", schema=relationships_schema)
        self.client.create_table(relationships_table, exists_ok=True)
        logger.info("Edge tables (relationships) created.")

    def create_property_graph(self, graph_name: str = "entities_graph"):
        # BigQuery Graph creation query
        query = f"""
        CREATE PROPERTY GRAPH IF NOT EXISTS `{self.dataset_ref}.{graph_name}`
          NODE TABLES (
            `{self.dataset_ref}.people` AS Person
              KEY (person_id)
              PROPERTIES (name, age),
            `{self.dataset_ref}.places` AS Place
              KEY (place_id)
              PROPERTIES (name, type)
          )
          EDGE TABLES (
            `{self.dataset_ref}.relationships` AS RelatesTo
              KEY (person_id, place_id)
              SOURCE KEY (person_id) REFERENCES Person (person_id)
              DESTINATION KEY (place_id) REFERENCES Place (place_id)
              PROPERTIES (visit_date, relationship_type)
          );
        """
        job = self.client.query(query)
        job.result() # Wait for the job to complete
        logger.info(f"Property graph {graph_name} created.")

    def setup_all(self):
        """Run the full setup pipeline."""
        self.create_dataset()
        self.create_node_tables()
        self.create_edge_tables()
        self.create_property_graph()
        logger.info("Complete graph setup finished.")

if __name__ == "__main__":
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="Set up BigQuery datasets, tables, and property graphs.")
    parser.add_argument("--project", default="filipegracio-ai-learning", help="GCP Project ID")
    parser.add_argument("--dataset", default="entities_graph_toy", help="BigQuery Dataset ID")
    args = parser.parse_args()
    
    try:
        setup = GraphSetup(project_id=args.project, dataset_id=args.dataset)
        setup.setup_all()
    except Exception as e:
        logger.error(f"Failed to setup graph: {e}")
        sys.exit(1)

