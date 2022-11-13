from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"text": "Hello World"}


@app.get("/{user_id}")
def info(user_id: int):
    return {"id": user_id}
