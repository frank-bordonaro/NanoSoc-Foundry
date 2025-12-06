from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import random
import string

app = FastAPI()

# Enable CORS so UI can call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For stricter: ["http://localhost:8000"]
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_aws_honeytoken():
    """
    Generates an AWS-style Access Key ID:
    Format: AKIA + 16 uppercase alphanumeric chars
    """
    suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"AKIA{suffix}"

@app.get('/honey/{token}')
async def honey(token: str, request: Request):
    data = {
        'token': token,
        'ip': request.client.host,
        'path': str(request.url),
    }
    print('HONEYPOT HIT', data)
    return {'status': 'recorded', 'token': token}

@app.post('/generate_token')
async def gen_token():
    """
    Generates a honeytoken for the UI
    (AWS-style Access Key ID)
    """
    token = generate_aws_honeytoken()
    print(f"Honeytoken generated: {token}")
    return {'token': token}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9001)
