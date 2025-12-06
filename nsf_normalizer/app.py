from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from nsf_normalizer.normalizer_core import normalize


app = FastAPI()

class RawEvent(BaseModel):
    raw: dict

@app.post('/ingest')
async def ingest(event: RawEvent):
    canonical = normalize(event.raw)
    # In MVP send canonical back and print
    print('INGEST', canonical)
    return {"status": "ok", "canonical": canonical}

@app.get('/health')
async def health():
    return {'status': 'healthy'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8001)
