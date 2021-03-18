import os
import msvcrt as m
import time, random
from datetime import datetime
from flask import Flask

app = Flask(__name__)
os.system('cls')
dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime('%d-%b-%Y (%H:%M:%S)')

@app.route("/")
def home():
    return("<h1>reaction test<h1>")

    

if __name__ == "__main__":
    app.run()





