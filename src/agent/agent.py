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
