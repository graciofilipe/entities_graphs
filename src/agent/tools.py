def read_document(file_path: str) -> str:
    """Reads the content of a document (PDF or txt) and returns the text.
    
    Args:
        file_path: The path to the document file.
    
    Returns:
        The extracted text from the document.
    """
    try:
        if file_path.lower().endswith('.pdf'):
            import pypdf
            with open(file_path, 'rb') as f:
                reader = pypdf.PdfReader(f)
                text = ''
                for page in reader.pages:
                    text += page.extract_text() + '\n'
                return text
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
    except Exception as e:
        return f"Error reading document: {str(e)}"

def write_to_bigquery(people: list[dict], places: list[dict], relationships: list[dict], project_id: str = 'filipegracio-ai-learning', dataset_id: str = 'entities_graph_toy') -> str:
    """Writes extracted entities and relationships to BigQuery graph tables using names as keys.
    
    Args:
        people: List of dicts with 'name', 'age'.
        places: List of dicts with 'name', 'type'.
        relationships: List of dicts with 'source_entity', 'target_entity', 'date', 'relationship_type'.
        project_id: GCP Project ID.
        dataset_id: BigQuery Dataset ID.
    """
    try:
        from google.cloud import bigquery
        
        client = bigquery.Client(project=project_id)
        dataset_ref = f"{project_id}.{dataset_id}"
            
        # Insert into BigQuery
        errors = []
        if people:
            errs = client.insert_rows_json(f"{dataset_ref}.people", people)
            if errs: errors.extend(errs)
        if places:
            errs = client.insert_rows_json(f"{dataset_ref}.places", places)
            if errs: errors.extend(errs)
        if relationships:
            errs = client.insert_rows_json(f"{dataset_ref}.relationships", relationships)
            if errs: errors.extend(errs)
            
        if errors:
            return f"Errors inserting to BigQuery: {errors}"
        return f"Successfully wrote {len(people)} people, {len(places)} places, and {len(relationships)} relationships to BigQuery."
    except Exception as e:
        import logging
        logging.error(f"Error writing to BigQuery: {e}")
        return f"Error writing to BigQuery: {str(e)}"

def check_existing_entities(people_names: list[str], place_names: list[str], project_id: str = 'filipegracio-ai-learning', dataset_id: str = 'entities_graph_toy') -> str:
    """Checks which people and places already exist in BigQuery.
    
    Args:
        people_names: List of people names to check.
        place_names: List of place names to check.
        project_id: GCP Project ID.
        dataset_id: BigQuery Dataset ID.
        
    Returns:
        A JSON string containing lists of existing_people and existing_places.
    """
    try:
        from google.cloud import bigquery
        import json
        
        client = bigquery.Client(project=project_id)
        dataset_ref = f"{project_id}.{dataset_id}"
        
        existing_people = []
        if people_names:
            names_formatted = ", ".join([f"'{name.replace(chr(39), chr(39)+chr(39))}'" for name in people_names])
            query = f"SELECT name FROM `{dataset_ref}.people` WHERE name IN ({names_formatted})"
            job = client.query(query)
            existing_people = [row.name for row in job.result()]
            
        existing_places = []
        if place_names:
            names_formatted = ", ".join([f"'{name.replace(chr(39), chr(39)+chr(39))}'" for name in place_names])
            query = f"SELECT name FROM `{dataset_ref}.places` WHERE name IN ({names_formatted})"
            job = client.query(query)
            existing_places = [row.name for row in job.result()]
            
        return json.dumps({
            "existing_people": existing_people,
            "existing_places": existing_places
        })
    except Exception as e:
        import logging
        logging.error(f"Error checking entities: {e}")
        return f"Error checking entities: {str(e)}"
