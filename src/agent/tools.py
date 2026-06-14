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
    """Writes extracted entities and relationships to BigQuery graph tables.
    
    Args:
        people: List of dicts with 'person_id' (natural key), 'name', 'age'.
        places: List of dicts with 'place_id' (natural key), 'name', 'type'.
        relationships: List of dicts with 'person_id', 'place_id', 'visit_date', 'relationship_type'.
        project_id: GCP Project ID.
        dataset_id: BigQuery Dataset ID.
    """
    try:
        from google.cloud import bigquery
        import uuid
        
        client = bigquery.Client(project=project_id)
        dataset_ref = f"{project_id}.{dataset_id}"
        
        # Disambiguate and generate UUIDs
        person_uuid_map = {}
        for p in people:
            natural_key = p['person_id']
            if natural_key not in person_uuid_map:
                person_uuid_map[natural_key] = str(uuid.uuid4())
            p['person_id'] = person_uuid_map[natural_key]
            
        place_uuid_map = {}
        for p in places:
            natural_key = p['place_id']
            if natural_key not in place_uuid_map:
                place_uuid_map[natural_key] = str(uuid.uuid4())
            p['place_id'] = place_uuid_map[natural_key]
            
        for r in relationships:
            r['person_id'] = person_uuid_map.get(r['person_id'], r['person_id'])
            r['place_id'] = place_uuid_map.get(r['place_id'], r['place_id'])
            
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
