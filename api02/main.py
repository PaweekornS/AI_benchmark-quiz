from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/hello")
def say_hello():
    logging.info("API2 received request at /hello")
    return {"message": "Hello from API2"}
