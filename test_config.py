"""
Simple test script to verify your LLM backend configuration.
Run this before using the main GeneAgent scripts.
"""

from config import chat_completion, get_llm_config

def test_connection():
    """Test the connection to the configured LLM backend."""
    print("Testing LLM backend configuration...\n")
    
    # Print current configuration
    config = get_llm_config()
    print(f"Backend: {config['backend']}")
    if config['backend'] == 'azure':
        print(f"Engine: {config['engine']}")
        print(f"API Base: {config['api_base']}")
    else:
        print(f"Model: {config['model']}")
        print(f"API Base: {config['api_base']}")
    print()
    
    # Test simple completion
    print("Sending test message...")
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello and confirm you are working!"}
    ]
    
    try:
        response = chat_completion(messages=messages, temperature=0)
        content = response.choices[0]["message"]["content"]
        print(f"\nResponse received:\n{content}\n")
        print("✅ Configuration test PASSED!")
        return True
    except Exception as e:
        print(f"\n❌ Configuration test FAILED!")
        print(f"Error: {e}\n")
        print("Please check:")
        print("1. Your LLM_BACKEND environment variable or config.py setting")
        print("2. The server is running (for Ollama/LM Studio)")
        print("3. The model is loaded and available")
        print("4. The API endpoint URL is correct")
        return False

if __name__ == "__main__":
    test_connection()
