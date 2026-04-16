from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/checkout")
def checkout() -> dict[str, str]:
    return {"order_id": "TEST-001"}
