"""
Configuration file for LLM backend selection.
Supports Azure OpenAI, Ollama, and LM Studio.
"""

import os

# Try to load from .env file if it exists
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, that's okay
    pass

# LLM Backend Configuration
# Options: "azure", "ollama", "lmstudio"
LLM_BACKEND = os.getenv("LLM_BACKEND", "azure")

# Azure OpenAI Configuration
AZURE_API_TYPE = "azure"
AZURE_API_BASE = "******************"
AZURE_API_VERSION = "*******************"
AZURE_API_KEY = "*************************"
AZURE_ENGINE = "gpt-4o"

# Ollama Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.1:70b")  # Change to your preferred model
OLLAMA_API_KEY = "ollama"  # Ollama doesn't require a real API key

# LM Studio Configuration
LMSTUDIO_BASE_URL = os.getenv("LMSTUDIO_BASE_URL", "http://localhost:1234/v1")
LMSTUDIO_MODEL = os.getenv("LMSTUDIO_MODEL", "local-model")  # Will use whatever model is loaded
LMSTUDIO_API_KEY = "lm-studio"  # LM Studio doesn't require a real API key

def get_llm_config():
    """
    Returns the configuration dictionary for the selected LLM backend.
    """
    if LLM_BACKEND == "azure":
        return {
            "api_type": AZURE_API_TYPE,
            "api_base": AZURE_API_BASE,
            "api_version": AZURE_API_VERSION,
            "api_key": AZURE_API_KEY,
            "engine": AZURE_ENGINE,
            "backend": "azure"
        }
    elif LLM_BACKEND == "ollama":
        return {
            "api_base": OLLAMA_BASE_URL,
            "api_key": OLLAMA_API_KEY,
            "model": OLLAMA_MODEL,
            "backend": "ollama"
        }
    elif LLM_BACKEND == "lmstudio":
        return {
            "api_base": LMSTUDIO_BASE_URL,
            "api_key": LMSTUDIO_API_KEY,
            "model": LMSTUDIO_MODEL,
            "backend": "lmstudio"
        }
    else:
        raise ValueError(f"Unsupported LLM_BACKEND: {LLM_BACKEND}. Choose 'azure', 'ollama', or 'lmstudio'.")

def chat_completion(messages, temperature=0, functions=None):
    """
    Unified interface for chat completion across different backends.
    
    Args:
        messages: List of message dictionaries
        temperature: Temperature parameter for generation
        functions: Function definitions for function calling (Azure only)
    
    Returns:
        Chat completion response
    """
    import openai
    
    config = get_llm_config()
    
    if config["backend"] == "azure":
        openai.api_type = config["api_type"]
        openai.api_base = config["api_base"]
        openai.api_version = config["api_version"]
        openai.api_key = config["api_key"]
        
        kwargs = {
            "engine": config["engine"],
            "messages": messages,
            "temperature": temperature,
        }
        if functions is not None:
            kwargs["functions"] = functions
            
        return openai.ChatCompletion.create(**kwargs)
    
    elif config["backend"] in ["ollama", "lmstudio"]:
        # Ollama and LM Studio use OpenAI-compatible API
        openai.api_base = config["api_base"]
        openai.api_key = config["api_key"]
        
        kwargs = {
            "model": config["model"],
            "messages": messages,
            "temperature": temperature,
        }
        
        # Function calling support (may not work with all local models)
        if functions is not None:
            kwargs["functions"] = functions
            
        return openai.ChatCompletion.create(**kwargs)
    
    else:
        raise ValueError(f"Unsupported backend: {config['backend']}")
