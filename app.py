from flask import Flask
import threading
import os
import time
import bot

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

def run_bot():
    bot.start_bot()

# start both
threading.Thread(target=run_web).start()
start_bot()
