from fastapi import FastAPI
import uvicorn
from hello_world import router as hello_world_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello rodl"}

app.include_router(hello_world_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)