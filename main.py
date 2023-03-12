from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware


from db.database import engine


app = FastAPI(
    title='Agiliza MEI',
    description='API de aplicação para agilizar o processo de abertura de empresas MEI no município de Blumenau/SC',
    version='0.001beta',
    contact={
        "name": "Pyninjas",
        "email": "contact@pyninjas.com"
        }
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api import api


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return "Bem Vindos a Agiliza MEI"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", 
        host='127.0.0.1',
        port=8000, 
        log_level='info', 
        reload=True
    )
