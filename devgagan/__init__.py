#devggn

from telethon.sync import TelegramClient
import asyncio
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN


sexxx = Client(
    ":seex:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

try:
    sexxx.start()
    print("Bot started ... ")
except Exception:
    print("Something went wrong")

sex = TelegramClient('ggneditz', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


loop = asyncio.get_event_loop()

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)
app = Client(
    ":gndmaraobsdk:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)
async def madarchod_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name
        
loop.run_until_complete(madarchod_bot())



