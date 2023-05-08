from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import requests, random, asyncio

# url to the display client
cat_url = "http://localhost:8000"

cat_moods = {
    0: "/scratch",
    1: "/purr"
}

current_mood = 1

# body for http request
# @param message: if we need to send a message, can be omitted
# @param data: proyimity
class PetBody(BaseModel):
    message: str | None = None
    data: float

user_lives = 5
cats_made_happy = 0

random.seed()

app = FastAPI()

# starts the mood setter in the background
@app.get("/")
def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(update_mood_periodically, 4)
    return {"Virtual Cat"}

@app.post("/pet")
def pet_cat(body: PetBody):
    global user_lives
    global cats_made_happy
    global current_mood


    # check threshhold
    if(body.data < 10):
        return {"user did not pet"}

    # DEBUG
    # print("user pets!")
    
    r = requests.get(cat_url + cat_moods[current_mood])
    if(current_mood == 0):
        user_lives -= 1
        print(f"User petted an angry cat!\nLives left: {user_lives}\nCats to be made happy: {5-cats_made_happy}")
        if(user_lives <= 0):
            r = requests.get(cat_url + "/lose")
            print("User has lost!\n\nResuming game!")
            user_lives = 5
            cats_made_happy = 0
    else:
        cats_made_happy += 1
        print(f"User petted a sad cat. Now it's happy!\nLives left: {user_lives}\nCats to be made happy: {5-cats_made_happy}")
        if(cats_made_happy >= 5):
            r = requests.get(cat_url + "/win")
            print("User has won!\n\nResuming game!")
            user_lives = 5
            cats_made_happy = 0

    if(r.status_code != 200):
        return("Error: " + str(r.status_code))
    

    return(r.text)


async def update_mood_periodically(interval: int):
    while True:
        set_mood()
        await asyncio.sleep(interval)


def set_mood():
    global current_mood
    current_mood= random.randint(0, 1)

    if(current_mood == 1):
        print("Cat is sad right now :'(")
    elif(current_mood == 0):
        print("Cat is angry! >:(")

