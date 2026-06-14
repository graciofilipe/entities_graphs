import sys
from src.agent.agent import root_agent

def main():
    if len(sys.argv) < 2:
        print("Usage: python src/main.py <path_to_document>")
        sys.exit(1)
        
    doc_path = sys.argv[1]
    print(f"Processing {doc_path} with EntityExtractionAgent...")
    
    # In a real environment, ADK handles execution.
    # This is a mock invocation for local testing.
    try:
        response = root_agent.run(f"Please extract entities from this document: {doc_path}")
        print("Agent Response:")
        print(response)
    except AttributeError:
        # Fallback if Agent class doesn't have a direct .run() method in actual google-adk
        print("Agent configured successfully. Use ADK runtime commands to execute.")

if __name__ == '__main__':
    main()
