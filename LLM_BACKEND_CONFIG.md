# LLM Backend Configuration Guide

GeneAgent now supports multiple LLM backends:
- **Azure OpenAI** (default)
- **Ollama** (local models)
- **LM Studio** (local models)

## Configuration

The LLM backend is configured through the `config.py` file and environment variables.

### Option 1: Using Environment Variables (Recommended)

You can set the backend and configuration using environment variables:

```bash
# For Ollama
export LLM_BACKEND=ollama
export OLLAMA_BASE_URL=http://localhost:11434/v1
export OLLAMA_MODEL=llama3.1:70b

# For LM Studio
export LLM_BACKEND=lmstudio
export LMSTUDIO_BASE_URL=http://localhost:1234/v1
export LMSTUDIO_MODEL=local-model

# For Azure OpenAI (default)
export LLM_BACKEND=azure
```

### Option 2: Editing config.py Directly

Open `config.py` and modify the configuration variables:

```python
# Change this to "ollama" or "lmstudio"
LLM_BACKEND = "ollama"

# Ollama settings
OLLAMA_BASE_URL = "http://localhost:11434/v1"
OLLAMA_MODEL = "llama3.1:70b"  # or any model you have installed

# LM Studio settings
LMSTUDIO_BASE_URL = "http://localhost:1234/v1"
LMSTUDIO_MODEL = "local-model"
```

## Using Ollama

### 1. Install Ollama

```bash
# Linux
curl -fsSL https://ollama.com/install.sh | sh

# macOS
brew install ollama
```

### 2. Pull a Model

```bash
# For best results, use a large model
ollama pull llama3.1:70b

# Or other capable models:
ollama pull mistral:7b
ollama pull mixtral:8x7b
ollama pull codellama:34b
```

### 3. Start Ollama Server

```bash
ollama serve
```

The server will run on `http://localhost:11434` by default.

### 4. Configure GeneAgent

```bash
export LLM_BACKEND=ollama
export OLLAMA_MODEL=llama3.1:70b
```

### 5. Run GeneAgent

```bash
python main_cascade.py
```

## Using LM Studio

### 1. Install LM Studio

Download from [https://lmstudio.ai/](https://lmstudio.ai/)

### 2. Load a Model

1. Open LM Studio
2. Go to the "Discover" tab
3. Download a model (recommended: Llama 3.1 70B, Mixtral 8x7B, or similar)
4. Load the model in the "Chat" tab

### 3. Start the Local Server

1. In LM Studio, go to the "Local Server" tab
2. Click "Start Server"
3. The server will run on `http://localhost:1234` by default

### 4. Configure GeneAgent

```bash
export LLM_BACKEND=lmstudio
export LMSTUDIO_BASE_URL=http://localhost:1234/v1
```

### 5. Run GeneAgent

```bash
python main_cascade.py
```

## Model Recommendations

For best results with GeneAgent's complex biological analysis tasks:

### Recommended Models (in order of quality):
1. **Llama 3.1 70B** - Best overall performance
2. **Mixtral 8x7B** - Good balance of speed and quality
3. **Qwen 2.5 72B** - Strong reasoning capabilities
4. **Llama 3 70B** - Reliable for complex tasks

### Minimum Requirements:
- At least 7B parameters
- Models trained on scientific/technical content perform better
- Instruction-tuned models work best

### Hardware Requirements:
- **7B models**: 8GB+ RAM/VRAM
- **13B-34B models**: 16GB+ RAM/VRAM
- **70B models**: 64GB+ RAM or GPU with 40GB+ VRAM

## Function Calling Support

**Important Note**: Function calling (used by the AgentPhD verification system) may not work perfectly with all local models. 

- Azure OpenAI has full function calling support ✅
- Some Ollama models support function calling (check model documentation)
- LM Studio has experimental function calling support

If you encounter issues with function calling on local models:
1. Try a different model
2. Use quantized versions (Q4, Q5, Q8)
3. Ensure your server supports the OpenAI function calling API

## Troubleshooting

### Connection Issues

```bash
# Test Ollama connection
curl http://localhost:11434/v1/models

# Test LM Studio connection
curl http://localhost:1234/v1/models
```

### Model Not Responding

- Check that the server is running
- Verify the model is loaded
- Check the model name matches exactly
- Look at server logs for errors

### Out of Memory

- Use a smaller model
- Use quantized versions (e.g., Q4_K_M instead of full precision)
- Increase system swap/pagefile
- Use GPU acceleration if available

### Slow Performance

Local models are slower than cloud APIs. For large datasets:
- Use a smaller model
- Enable GPU acceleration
- Process in smaller batches
- Consider using fewer verification steps

## Switching Back to Azure OpenAI

```bash
export LLM_BACKEND=azure
```

Or edit `config.py`:
```python
LLM_BACKEND = "azure"
```

## Testing Your Configuration

Create a simple test script:

```python
from config import chat_completion

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Say hello!"}
]

response = chat_completion(messages=messages, temperature=0)
print(response.choices[0]["message"]["content"])
```

Run it to verify your configuration is working:
```bash
python test_config.py
```
