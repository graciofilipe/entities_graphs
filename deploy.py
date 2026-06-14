import vertexai
from src.agent.agent import app
from google.cloud import aiplatform_v1beta1
import os

def set_display_name(resource_name, display_name, location):
    client_options = {"api_endpoint": f"{location}-aiplatform.googleapis.com"}
    gapic_client = aiplatform_v1beta1.ReasoningEngineServiceClient(client_options=client_options)
    engine = aiplatform_v1beta1.ReasoningEngine(name=resource_name, display_name=display_name)
    request = aiplatform_v1beta1.UpdateReasoningEngineRequest(
        reasoning_engine=engine,
        update_mask={"paths": ["display_name"]}
    )
    gapic_client.update_reasoning_engine(request=request)
    print(f"Set display name to '{display_name}'")

def deploy():
    project_id = "filipegracio-ai-learning"
    location = "us-central1"
    vertexai.init(project=project_id, location=location)
    client = vertexai.Client(project=project_id, location=location)
    
    config = dict(
        requirements="requirements.txt",
        extra_packages=["src"],
        staging_bucket="gs://filipegracio-ai-learning-agent-staging",
        env_vars={
            "GOOGLE_CLOUD_LOCATION": "global",
            "GOOGLE_CLOUD_REGION": "global"
        }
    )
    
    deployment_file = "deployment_id.txt"
    agent_id = None
    
    if os.path.exists(deployment_file):
        with open(deployment_file, "r") as f:
            agent_id = f.read().strip()
            
    if agent_id:
        print(f"Updating existing agent {agent_id}...")
        try:
            agent_engine = client.agent_engines.update(
                name=agent_id,
                agent=app,
                config=config
            )
            print(f"Update successful: {agent_engine.api_resource.name}")
        except Exception as e:
            print(f"Update failed: {e}. Falling back to create...")
            agent_id = None
            
    if not agent_id:
        print("Deploying new agent to Google Cloud Agent Runtime...")
        agent_engine = client.agent_engines.create(
            agent=app,
            config=config
        )
        agent_id = agent_engine.api_resource.name
        print(f"Deployment successful: {agent_id}")
        
        with open(deployment_file, "w") as f:
            f.write(agent_id)
            
    set_display_name(agent_id, "entity relationship extraction agent", location)

if __name__ == "__main__":
    deploy()
