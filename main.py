from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI()

# Include API routers
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
