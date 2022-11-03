import uvicorn

from backend.app import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", log_level="debug", port=8000, workers=1, )
