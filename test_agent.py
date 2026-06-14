import vertexai

def main():
    project_id = "filipegracio-ai-learning"
    location = "us-central1"
    agent_id = "projects/257470209980/locations/us-central1/reasoningEngines/3917470319568224256"

    client = vertexai.Client(project=project_id, location=location)
    
    print("Fetching agent engine...")
    try:
        agent_engine = client.agent_engines.get(name=agent_id)
    except Exception:
        # Fallback if vertexai.Client doesn't have agent_engines.get or fails
        from vertexai.preview import reasoning_engines
        vertexai.init(project=project_id, location=location)
        agent_engine = reasoning_engines.ReasoningEngine(agent_id)

    test_input = "Filipe Gracio visited the British Museum in London. He then took a train to Paris to meet Yann LeCun."
    print(f"Sending input: '{test_input}'")
    
    try:
        # AdkApp exposes stream_query
        response = agent_engine.stream_query(message=test_input, user_id="test_user")
        print("\nResponse:")
        for chunk in response:
            print(chunk, end="")
        print()
    except Exception as e:
        print(f"\nError calling query(): {e}")
        print("Available methods on agent_engine:", dir(agent_engine))

if __name__ == "__main__":
    main()
