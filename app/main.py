from fastapi import FastAPI, Header, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/checkout")
def checkout(idempotency_key: str | None = Header(default=None)) -> dict[str, str]:
    if not idempotency_key:
        raise HTTPException(status_code=400, detail="Idempotency-Key header required")
    return {"order_id": "TEST-001"}
