from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "유andy",
        "ando": "coco"
    }

