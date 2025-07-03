from fastapi import FastAPI

app=FastAPI()

@app.get('/')
def home():
    return "you built your first CI/CD pipeline"