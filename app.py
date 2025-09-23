from fastapi import FastAPI


app = FastAPI(title="Hello world App")


@app.get("/hello/", response_model=dict[str, str])
async def get_hello() -> dict[str, str]:
    return {"detail": "Hello world !"}
