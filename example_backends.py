"""
Example script demonstrating how to switch between different LLM backends.
"""

import os
from config import get_llm_config, chat_completion

def example_with_azure():
    """Example using Azure OpenAI"""
    print("=" * 60)
    print("Example 1: Using Azure OpenAI")
    print("=" * 60)
    
    # Set backend to Azure
    os.environ["LLM_BACKEND"] = "azure"
    
    config = get_llm_config()
    print(f"Backend: {config['backend']}")
    print(f"Engine: {config.get('engine', 'N/A')}")
    
    messages = [
        {"role": "system", "content": "You are a molecular biology expert."},
        {"role": "user", "content": "Briefly explain what the BRCA1 gene does."}
    ]
    
    try:
        response = chat_completion(messages=messages, temperature=0)
        print(f"\nResponse:\n{response.choices[0]['message']['content']}\n")
    except Exception as e:
        print(f"Error: {e}\n")

def example_with_ollama():
    """Example using Ollama"""
    print("=" * 60)
    print("Example 2: Using Ollama (Local Model)")
    print("=" * 60)
    
    # Set backend to Ollama
    os.environ["LLM_BACKEND"] = "ollama"
    os.environ["OLLAMA_MODEL"] = "llama3.1:70b"  # Change to your installed model
    
    # Need to reimport to pick up new environment variables
    from config import get_llm_config, chat_completion as ollama_chat
    
    config = get_llm_config()
    print(f"Backend: {config['backend']}")
    print(f"Model: {config.get('model', 'N/A')}")
    print(f"API Base: {config.get('api_base', 'N/A')}")
    
    messages = [
        {"role": "system", "content": "You are a molecular biology expert."},
        {"role": "user", "content": "Briefly explain what the BRCA1 gene does."}
    ]
    
    try:
        response = ollama_chat(messages=messages, temperature=0)
        print(f"\nResponse:\n{response.choices[0]['message']['content']}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure Ollama is running: ollama serve")
        print(f"Make sure the model is available: ollama pull {os.environ.get('OLLAMA_MODEL', 'llama3.1:70b')}\n")

def example_with_lmstudio():
    """Example using LM Studio"""
    print("=" * 60)
    print("Example 3: Using LM Studio (Local Model)")
    print("=" * 60)
    
    # Set backend to LM Studio
    os.environ["LLM_BACKEND"] = "lmstudio"
    
    # Need to reimport to pick up new environment variables
    from config import get_llm_config, chat_completion as lmstudio_chat
    
    config = get_llm_config()
    print(f"Backend: {config['backend']}")
    print(f"Model: {config.get('model', 'N/A')}")
    print(f"API Base: {config.get('api_base', 'N/A')}")
    
    messages = [
        {"role": "system", "content": "You are a molecular biology expert."},
        {"role": "user", "content": "Briefly explain what the BRCA1 gene does."}
    ]
    
    try:
        response = lmstudio_chat(messages=messages, temperature=0)
        print(f"\nResponse:\n{response.choices[0]['message']['content']}\n")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure LM Studio server is running on http://localhost:1234")
        print("Load a model in LM Studio and start the local server\n")

if __name__ == "__main__":
    print("\nGeneAgent - LLM Backend Examples\n")
    
    # Try each backend
    # Uncomment the ones you want to test
    
    # example_with_azure()      # Requires Azure OpenAI API key
    example_with_ollama()     # Requires Ollama installed and running
    # example_with_lmstudio()   # Requires LM Studio running
    
    print("\nDone! You can now use GeneAgent with your preferred backend.")
    print("Set LLM_BACKEND environment variable before running main scripts:")
    print("  export LLM_BACKEND=ollama    # For Ollama")
    print("  export LLM_BACKEND=lmstudio  # For LM Studio")
    print("  export LLM_BACKEND=azure     # For Azure OpenAI")
