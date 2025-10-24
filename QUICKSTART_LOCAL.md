# Quick Start Guide: Using GeneAgent with Local Models

This guide will help you get started with GeneAgent using Ollama or LM Studio in just a few minutes.

## Choose Your Path

### Path A: Ollama (Command Line) ⭐ Recommended for Linux/Mac
### Path B: LM Studio (GUI) ⭐ Recommended for Windows/Mac

---

## Path A: Ollama Setup (5 minutes)

### Step 1: Install Ollama

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**macOS:**
```bash
brew install ollama
```

**Windows:**
Download from https://ollama.com/download

### Step 2: Start Ollama & Pull a Model

```bash
# Start Ollama server (in one terminal)
ollama serve

# In another terminal, pull a model
ollama pull llama3.1:70b
```

**Alternative models** (if you have limited RAM/VRAM):
```bash
ollama pull llama3.1:8b     # 8GB RAM
ollama pull mixtral:8x7b    # 32GB RAM
ollama pull mistral:7b      # 8GB RAM
```

### Step 3: Configure GeneAgent

```bash
cd /path/to/GeneAgent

# Set environment variables
export LLM_BACKEND=ollama
export OLLAMA_MODEL=llama3.1:70b  # Match the model you pulled

# Test the configuration
python test_config.py
```

### Step 4: Run GeneAgent

```bash
python main_cascade.py
```

**That's it!** 🎉

---

## Path B: LM Studio Setup (5 minutes)

### Step 1: Install LM Studio

1. Download from https://lmstudio.ai/
2. Install and open LM Studio

### Step 2: Download and Load a Model

1. In LM Studio, click **"Discover"** tab
2. Search for and download one of these models:
   - **llama-3.1-70b** (best quality, needs 64GB+ RAM)
   - **mistral-7b** (good balance, needs 8GB RAM)
   - **mixtral-8x7b** (very good, needs 32GB RAM)
3. Go to **"Chat"** tab
4. Load the downloaded model

### Step 3: Start Local Server

1. In LM Studio, go to **"Local Server"** tab
2. Click **"Start Server"**
3. Verify it says "Server running on http://localhost:1234"

### Step 4: Configure GeneAgent

```bash
cd /path/to/GeneAgent

# Set environment variables
export LLM_BACKEND=lmstudio

# Test the configuration
python test_config.py
```

### Step 5: Run GeneAgent

```bash
python main_cascade.py
```

**That's it!** 🎉

---

## Troubleshooting

### Test fails with "Connection refused"
- **Ollama**: Make sure `ollama serve` is running
- **LM Studio**: Check that local server is started in LM Studio

### Model not found
- **Ollama**: Run `ollama list` to see installed models
- **LM Studio**: Make sure a model is loaded in the Chat tab

### Out of memory
- Use a smaller model (7B or 8B parameters)
- Close other applications
- Use quantized versions (Q4, Q5)

### Slow performance
- This is normal for local models
- Use GPU acceleration if available
- Consider using a smaller model for testing
- For production, use larger models on GPU or cloud APIs

---

## Performance Comparison

| Model Size | Quality | Speed | RAM/VRAM Needed |
|------------|---------|-------|-----------------|
| 7-8B       | Good    | Fast  | 8GB             |
| 13-34B     | Better  | Medium| 16-32GB         |
| 70B        | Best    | Slow  | 64GB+           |

---

## Next Steps

✅ Your local model is working!

Now you can:
- Run all GeneAgent scripts (`main_cascade.py`, `main_CoT.py`, etc.)
- Switch models by changing `OLLAMA_MODEL` environment variable
- Read `LLM_BACKEND_CONFIG.md` for advanced configuration
- Try different models to find the best balance of speed/quality

---

## Tips for Best Results

1. **Use the largest model your hardware can support**
   - 70B models give the best results for complex biological analysis

2. **Enable GPU acceleration**
   - Ollama automatically uses GPU if available
   - LM Studio: Check GPU settings in preferences

3. **For faster iteration**
   - Test with smaller models (7-8B)
   - Deploy with larger models (70B) for final results

4. **Monitor resource usage**
   - Use `htop` (Linux/Mac) or Task Manager (Windows)
   - If swapping to disk, use a smaller model

---

## Support

- **Ollama Issues**: https://github.com/ollama/ollama/issues
- **LM Studio Issues**: https://lmstudio.ai/support
- **GeneAgent Issues**: Check `LLM_BACKEND_CONFIG.md`

Happy analyzing! 🧬🤖
