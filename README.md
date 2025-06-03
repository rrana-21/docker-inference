# Dockerized HuggingFace Inference API

This sampe project uses FastAPI and Docker to serve a pre-trained Hugging Face sentiment analysis model (`distilbert-base-uncased-finetuned-sst-2-english`).  
It supports parallel requests and can be tested via Swagger UI or Jupyter notebook.

## Run the App

```bash
docker build -t huggingface-fastapi .
docker run -p 8000:8000 huggingface-fastapi
