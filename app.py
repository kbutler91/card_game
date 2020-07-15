import sys
from broker import Broker
from flask import Flask
app = Flask(__name__)

@app.route("/")

def main():

    rounds = 1000
    broker = Broker(rounds)
    broker.setup()
    broker.play()
    return broker.display_results()


