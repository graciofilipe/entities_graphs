import vertexai
from src.agent.agent import app

def main():
    project_id = "filipegracio-ai-learning"
    location = "us-central1"

    # Initialize Vertex AI client
    client = vertexai.Client(project=project_id, location=location)

    # Deploy the agent
    print(f"Deploying agent to Google Cloud Agent Runtime in project {project_id}...")
    agent_engine = client.agent_engines.create(
        agent=app,
        config=dict(
            requirements="requirements.txt",
            extra_packages=["src"],
            staging_bucket="gs://filipegracio-ai-learning-agent-staging",
            env_vars={
                "GOOGLE_CLOUD_LOCATION": "global",
                "GOOGLE_CLOUD_REGION": "global"
            }
        )
    )
    
    print(f"Deployment successful: {agent_engine.api_resource.name}")

if __name__ == "__main__":
    main()
