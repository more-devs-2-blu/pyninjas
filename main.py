from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware



from db.database import engine


app = FastAPI(
    title='Agiliza MEI',
    description='API - Acelerar o Processo de Criacao de MEI',
    version='0.5',
    contact={
        "name": "pyNinjas",
        "url": "https://github.com/more-devs-2-blu/pyninjas"
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


@app.get(
        "/", 
        status_code=status.HTTP_200_OK,
        tags=['index']
        )
def root():
    return "Agiliza MEI"

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app", 
        host='127.0.0.1',
        port=8000, 
        log_level='info',
        reload=True
    )
