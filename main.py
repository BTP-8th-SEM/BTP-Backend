from fastapi import FastAPI
from routes import userApis;
# Initialize the app
app = FastAPI()

app.include_router(userApis.router)

# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Made with love by Shreyas"}