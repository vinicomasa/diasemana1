from fastapi import FastAPI
import datetime
import json

app = FastAPI()

# GET POST PUT DELETE

@app.get('/diaslecionado/{dia_selct}')
def get_date(dia_selct:str):
  d = int(dia_selct[0:2])
  m = int(dia_selct[3:4])
  dia = datetime.date(2022,m,d)
  semana = dia.weekday()
  toJson = json.dumps({"dia": int(semana)})
  return json.loads(toJson)
