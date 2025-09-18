from fastapi import FastAPI

app = FastAPI(title = "Simple FastAPI website")


@app.get('/healthz')
def get_health():
    return {"msg": "ok"}

@app.get('/readyz')
def get_ready():
    return {"msg": "Application ready"}


@app.get('/')
def root():
    return {"msg": "Hello World!"}


@app.get('/version')
def version():

    return {"msg": "Version 2 with a new feature"}
