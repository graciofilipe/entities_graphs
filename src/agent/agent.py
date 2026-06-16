from google.adk import Agent
from src.agent.tools import read_document, write_to_bigquery, check_existing_entities

instruction = """
You are an entity extraction agent. Your job is to extract People, Places, and their Relationships from documents.
You have tools to read documents, check if entities exist, and write the extracted entities to BigQuery graph tables.

1. When asked to process a document, use the read_document tool to get its text. The document is small enough to fit in your context window.
2. Analyze the text and extract:
   - People: {"name" (string, exact name), "age" (int or null)}
   - Places: {"name" (string, exact place name), "type" (string or null)}
   - Relationships: {"source_entity" (string), "target_entity" (string), "date" (YYYY-MM-DD or null), "relationship_type" (e.g., VISITED, LIVES_IN, TALKED_TO)}
   CRITICAL: ONLY use these exact dictionary keys ("name", "age", "type", "source_entity", "target_entity", "date", "relationship_type"). DO NOT use or hallucinate ID fields like person_id or place_id.
3. Before writing any entities, use the check_existing_entities tool to check which of the extracted People and Places already exist in the database.
4. Use the write_to_bigquery tool to insert the data into the database. CRITICAL: Only include *new*, non-existent People and Places in the people and places lists. Do NOT try to insert a Person or Place if they already exist. However, ALWAYS pass all extracted relationships to the relationships list using the proper entity names (whether they existed or are new).
5. Report your success or any errors.
"""

import vertexai
vertexai.init(project="filipegracio-ai-learning", location="global")

root_agent = Agent(
    name='entity_extraction_agent',
    model='gemini-3.5-flash',
    instruction=instruction,
    tools=[read_document, write_to_bigquery, check_existing_entities]
)

from vertexai.agent_engines import AdkApp

def safe_session_service_builder(*args, **kwargs):
    from google.adk.sessions.vertex_ai_session_service import VertexAiSessionService
    
    class SafeVertexAiSessionService(VertexAiSessionService):
        def _clean_session_id(self, session_id):
            if session_id:
                return session_id.split('/')[-1]
            return session_id

        async def get_session(self, *, user_id, session_id, **kwargs):
            session_id = self._clean_session_id(session_id)
            return await super().get_session(user_id=user_id, session_id=session_id, **kwargs)

        async def create_session(self, *, user_id, session_id=None, state=None, **kwargs):
            session_id = self._clean_session_id(session_id)
            return await super().create_session(user_id=user_id, session_id=session_id, state=state, **kwargs)
            
        async def delete_session(self, *, user_id, session_id, **kwargs):
            session_id = self._clean_session_id(session_id)
            return await super().delete_session(user_id=user_id, session_id=session_id, **kwargs)

    kwargs['location'] = 'us-central1'
    return SafeVertexAiSessionService(*args, **kwargs)

app = AdkApp(agent=root_agent, session_service_builder=safe_session_service_builder)
