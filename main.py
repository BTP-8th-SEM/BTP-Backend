from fastapi import FastAPI
from routes import userApis, answerApis, questionApis
# Initialize the app
app = FastAPI()

app.include_router(userApis.router)
app.include_router(answerApis.router)
app.include_router(questionApis.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Made with love by Shreyas, Gaurav, Prasad and our beloved Tarun"}