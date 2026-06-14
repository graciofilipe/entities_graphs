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

## Lessons Learned: Agent Deployment

During the development and deployment of the ADK Entity Extraction Agent, we encountered and resolved several critical deployment nuances with the Google Cloud Agent Runtime (Reasoning Engine):

1. **Model Region vs Engine Region**: The `ReasoningEngine` resource itself must be deployed to a standard regional location (like `us-central1`). Deploying the engine to `global` will fail with an error. 
2. **Global Model Access**: Conversely, the Gemini models (e.g., `gemini-3.5-flash`) must often be accessed via the `global` region in certain Google Cloud projects. If the deployed Reasoning Engine defaults to its own region (`us-central1`), you will encounter a `404 NOT_FOUND Publisher Model` error when the agent attempts to invoke the model.
3. **Environment Variable Injection**: To bridge this gap, you must pass the `GOOGLE_CLOUD_LOCATION` and `GOOGLE_CLOUD_REGION` environment variables set to `"global"` in the `env_vars` configuration dictionary when calling `client.agent_engines.create(...)`. This forces the backend Cloud Run instance executing the agent to use the global endpoint for Vertex AI.
4. **ADK Packaging Requirements**: When wrapping your agent in `AdkApp(agent=root_agent)`, ensure your `requirements.txt` includes `google-cloud-aiplatform[agent_engines,adk]`. Omitting the `[agent_engines,adk]` extras will cause missing dependency errors (like `cloudpickle`) during the remote build process.
5. **Remote Agent Invocation**: Deployed ADK agents expose specific methods defined in their `operation_schemas`. Instead of blindly calling a `.query()` method on the `AgentEngine` object, use `.stream_query(message=..., user_id=...)` and iterate over the generator to retrieve the asynchronous streaming responses.
