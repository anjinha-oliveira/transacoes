from fastapi import FastAPI

app = FastAPI()


@app.get("/transacoes")
async def root():
    
    return {"message: Tudo certo!"}