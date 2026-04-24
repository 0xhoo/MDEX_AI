from fastapi import FastAPI, HTTPException, Query
from database import MEME_DATA
from ai_engine import get_meme_recommendation

app = FastAPI(title="MDEX AI API")

@app.get("/")
def read_root():
    return {"status": "online", "developer": "Jang Si-hu"}

@app.get("/memes/ai-search")
def ai_search_meme(q: str = Query(...)):
    try:
        recommendation = get_meme_recommendation(q)
        return {
            "query": q,
            "ai_recommendation": recommendation
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))