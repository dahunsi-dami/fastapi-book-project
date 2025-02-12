#!/bin/bash

echo "Pulling latest changes..."
git pull origin main

echo "Updating dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "Restarting FastAPI application..."
pkill -f "uvicorn main:app" || true
nohup uvicorn main:app --host 127.0.0.1 --port 8000 > api.log 2>&1 &

echo "Deployment complete!"
