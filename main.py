from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import optionsApis, userApis, questionApis, testApi, studentTestMapApi, OLAPApis, responcesApis

# Initialize the app
app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(userApis.router)
app.include_router(studentTestMapApi.router)
app.include_router(optionsApis.router)
app.include_router(questionApis.router)
app.include_router(testApi.router)
app.include_router(OLAPApis.router)
app.include_router(responcesApis.router)
# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Made with love by Shreyas, Gaurav, Prasad and our beloved Tarun"}