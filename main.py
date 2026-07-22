from fastapi import FastAPI
app = FastAPI()

@app.get("/WELCOME")
def read_root():
    return {"Hello": "World"}