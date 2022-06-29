from fastapi import FastAPI
from datetime import date
import json

app = FastAPI()

# GET POST PUT DELETE

@app.get('/date')
def get_date():
  toJson = json.dumps({"date": str(date.today())})
  return json.loads(toJson)
