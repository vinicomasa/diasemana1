from fastapi import FastAPI
from datetime import date

app = FastAPI()

# GET POST PUT DELETE

@app.get('/date')
def get_date():
  return date.today()

