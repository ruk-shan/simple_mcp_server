run ollama on docker 
    docker run -d --gpus=all -v ollama:/root/.ollama -p 11411:11434 --name ollama ollama/ollama

pull a model 
     ollama pull llama3.2:latest

setting up open-webui
docker run -d \
  --network host \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11411 \
  -e PORT=3000 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main

Create 
    python3 -m venv .venv

activate 
    source .venv/bin/activate

install pkgs
    pip install fastmcp

run mcp server
    uvx mcpo --host 0.0.0.0 --port 8003 -- .venv/bin/python3 mcp_server.py
