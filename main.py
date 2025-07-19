
from fastapi import FastAPI

one = FastAPI()

# Create a "path operation decorator". This tells FastAPI that the function below
# is responsible for handling requests that go to the path "/" with a GET method.
@one.get("/")
async def read_root():

    return {"massage": "Hello world"}

@one.get("/about")
async def read_root():

    return {"name": "Asha Melius Kisonga!" ,
            "Age" : 22, 
            "Pofessional": "MLOps Engineer",
            "Hobbies": "Coding"}
