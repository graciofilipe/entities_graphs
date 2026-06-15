# Gemini Context

This project leverages BigQuery's new Graph capabilities. Whenever assisting with graph modeling, data ingestion, or querying, you **must** consult the official documentation to ensure the correct syntax and best practices are applied.

## Key Documentation Links:
- [Graph Overview](https://docs.cloud.google.com/bigquery/docs/graph-overview)
- [Create Graphs](https://docs.cloud.google.com/bigquery/docs/graph-create)
- [Schema Overview](https://docs.cloud.google.com/bigquery/docs/graph-schema-overview)
- [Query Overview](https://docs.cloud.google.com/bigquery/docs/graph-query-overview)
- [Query Best Practices](https://docs.cloud.google.com/bigquery/docs/graph-query-best-practices)
- [Graph Measures](https://docs.cloud.google.com/bigquery/docs/graph-measures)
- [Graph Modeler](https://docs.cloud.google.com/bigquery/docs/graph-modeler)
- [Graph Visualization](https://docs.cloud.google.com/bigquery/docs/graph-visualization)
- [Graph Chat](https://docs.cloud.google.com/bigquery/docs/graph-chat)
- [Graph Visualization Integrations](https://docs.cloud.google.com/bigquery/docs/graph-visualization-integrations)
- [Graph Search](https://docs.cloud.google.com/bigquery/docs/graph-search)

## Lessons Learned: ADK & Reasoning Engine Integrations

When building Agents with the Agent Development Kit (ADK) and integrating them with Google Cloud Reasoning Engine (or Gemini Enterprise App):

1. **Gemini Enterprise App Session IDs**: The Enterprise app natively manages user sessions and passes a full Google Cloud Resource Path as the `session_id`. However, ADK's `VertexAiSessionService` expects clean alphanumeric IDs (`^[A-Za-z0-9_-]+$`) and will fail regex validation. You must wrap the session service and extract the clean ID: `session_id.split('/')[-1]`.
2. **Session Serverless Persistence**: Avoid `InMemorySessionService` for production multi-turn agents. Reasoning Engine load-balances requests across different Cloud Run worker instances, meaning subsequent multi-turn requests will throw `SessionNotFoundError` if the session is strictly in memory. Always use `VertexAiSessionService`.
3. **Region Constraints (`global` vs `us-central1`)**: Gemini models (like `gemini-3.5-flash`) often require `vertexai.init(location="global")`. However, the `ReasoningEngine` resource is deployed regionally (e.g., `us-central1`). To prevent `VertexAiSessionService` from inheriting the global context and failing with a `404 NOT_FOUND`, you must explicitly inject the correct region into its constructor: `kwargs['location'] = 'us-central1'`.
