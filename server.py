from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def home():
  return "Now testing for multiplicative persistence."

def run():
  app.run(host='0.0.0.0',port=8080)

def bot_server():
  t = Thread(target=run)
  t.start()
