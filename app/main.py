from fastapi import FastAPI
import json, random

import config, models

app = FastAPI()

@app.get("/")
def root():
     return get_restaurant()

def get_restaurant():
     f = open(config.RESTAURANT_DATA_PATH)
     restaurants = json.load(f)

     rand_int = random.randint(0, len(restaurants))

     return models.Restaurant(
            id=restaurants[rand_int]["business_id"]
          , name=restaurants[rand_int]["name"]
          , address=restaurants[rand_int]["address"]
          , city=restaurants[rand_int]["city"]
          , state=restaurants[rand_int]["state"]
     )