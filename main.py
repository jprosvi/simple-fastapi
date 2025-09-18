from fastapi import FastAPI

app = FastAPI(title = "Simple FastAPI website")


@app.get('/healthz')
def get_health():
    return {"msg": "ok"}

@app.get('/')
def root():
    return {"msg": "Hello World!"}



@app.get('/version')
def version():

    return {"msg": "Version 1"}
