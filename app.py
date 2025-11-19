from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

# ------------ Telegram Bot -------------
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Bot is alive and running on Render!")

def run_bot():
    bot.run()


# ------------ Flask Server -------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Cobra! Bot is running."


def run_flask():
    app.run(host="0.0.0.0", port=8080)


# ------------ Start Both ---------------
if __name__ == "__main__":
    Thread(target=run_bot).start()
    run_flask()
