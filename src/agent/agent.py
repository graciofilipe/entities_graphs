from google.adk import Agent
from src.agent.tools import read_document, write_to_bigquery

instruction = """
You are an entity extraction agent. Your job is to extract People, Places, and their Relationships from documents.
You have tools to read documents and to write the extracted entities to BigQuery graph tables.

1. When asked to process a document, use the read_document tool to get its text. The document is small enough to fit in your context window.
2. Analyze the text and extract:
   - People: {person_id (string, natural key like their name), name, age (int or null)}
   - Places: {place_id (string, natural key like the place name), name, type (string or null)}
   - Relationships: {person_id, place_id, visit_date (YYYY-MM-DD or null), relationship_type (e.g., VISITED, LIVES_IN)}
3. The write_to_bigquery tool will automatically handle converting these natural keys to UUIDs and resolving collisions when inserting into the database.
4. Once extracted, use the write_to_bigquery tool to insert the data into the database.
5. Report your success or any errors.
"""

import vertexai
vertexai.init(project="filipegracio-ai-learning", location="global")

root_agent = Agent(
    name='entity_extraction_agent',
    model='gemini-3.5-flash',
    instruction=instruction,
    tools=[read_document, write_to_bigquery]
)

from vertexai.agent_engines import AdkApp
app = AdkApp(agent=root_agent)

