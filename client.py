from fastapi import FastAPI

app = FastAPI()

url = "localhost:8001/pet"

@app.get("/")
def read_root():
    return("Client for Virtual Cat")

@app.get("/scratch")
def scratch():
    return("*scratch*")

@app.get("/purr")
def purr():
    return("*purr*")

@app.get("/lose")
def purr():
    return("You have lost!")

@app.get("/win")
def win():
    return("You have won!")
