import discord
import asyncio
import os
import random
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 1465648809966174240

GIFS = [
    "https://tenor.com/tPOPFXrjLjm.gif",
    "https://tenor.com/bPmJh.gif",
    "https://klipy.com/gifs/tole-tole-cat-1",
    "https://klipy.com/gifs/wordle-wordle-in-5",
    "https://klipy.com/gifs/daitaku-helios-wordle-in-5",
    "https://klipy.com/gifs/wordle-in-five-1",
    "https://klipy.com/gifs/wordle-2",
    "https://tenor.com/vmKMSNlPgue.gif",
    "https://tenor.com/up54wwsGldI.gif",
    "https://tenor.com/lk7ZpoIUjpo.gif",
    "https://tenor.com/qbbPJ0Q3zHn.gif",
    "https://tenor.com/hC438wGCHDn.gif"
]

MESSAGE = "WORDLE IN 5!!!!!!  :D"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_sent_date = None

async def scheduler():
    global last_sent_date
    await client.wait_until_ready()

    while not client.is_closed():
        now = datetime.now()
        today = now.date()

        if now.hour == 23 and now.minute == 55 and last_sent_date != today:
            channel = client.get_channel(CHANNEL_ID)

            if channel is not None:
                gif = random.choice(GIFS)

                await channel.send(MESSAGE)
                await channel.send(gif)

                last_sent_date = today
                print("Message sent")

            else:
                print("Channel not found")

            await asyncio.sleep(60)

        await asyncio.sleep(20)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    client.loop.create_task(scheduler())

client.run(TOKEN)
