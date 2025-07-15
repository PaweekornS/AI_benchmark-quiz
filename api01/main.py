from fastapi import FastAPI
import requests
import logging
import os

# set destination url to request (handle both running from local and docker)
API2_HOST = os.getenv("API2_HOST", "localhost")
API2_PORT = os.getenv("API2_PORT", "8001")
URL = f"http://{API2_HOST}:{API2_PORT}/hello"

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/relay")  # endpoint of this API
def relay():
    logging.info("API1 received request at /relay")
    
    try:
        response = requests.get(URL)  # calling API2
        logging.info("API1 got response from API2")
        return response.json()
    except Exception as e:
        logging.error(f"Error calling API2: {e}")
        return {"error": str(e)}
