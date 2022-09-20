from fastapi import FastAPI
import sys
import os
import uvicorn
app = FastAPI()
@app.get("/")
def home():
    return {"message":"Welcome to ZEE5"}

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 8080))
        uvicorn.run(app, host = "127.0.0.1", port = port)