from fastapi import FastAPI

# Initialize the app
app = FastAPI()


# GET operation at route '/'
@app.get('/')
def root_api():
    return {"message": "Made with love by Shreyas"}