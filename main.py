from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scraper import get_metadata_from_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def on_fetch(request, env):
    import asgi

    return await asgi.fetch(app, request, env)


@app.get("/")
def health():
    return {"Ping": "Pong"}


@app.get("/metadata")
def fetch_metadata(url: str):
    if not url.startswith("http"):
        return {"error": "invalid url"}

    try:
        obtained_metadata = get_metadata_from_url(url.strip())
        return obtained_metadata
    except Exception as e:
        return {"error": str(e)}
