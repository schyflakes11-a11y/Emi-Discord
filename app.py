from flask import Flask
import threading
import os
import time

app = Flask(_name_)

@app.route("/")
def home():
    return "Bot is alive!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

def run_bot():
    while True:
        try:
            import bot  # runs your bot.py
        except Exception as e:
            print("Bot crashed:", e)
            time.sleep(5)

# start both
threading.Thread(target=run_web).start()
run_bot()
