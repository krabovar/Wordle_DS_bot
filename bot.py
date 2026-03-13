import discord
import asyncio
import os
import random
from datetime import datetime

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = 536620023326965764

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

MESSAGE = "WORDLE IN 5!!!!!! :D"

intents = discord.Intents.default()
client = discord.Client(intents=intents)

last_sent_date = None

async def scheduler():
    global last_sent_date
    await client.wait_until_ready()

    while not client.is_closed():
        now = datetime.now()
        today = now.date()

        if now.hour == 13 and now.minute == 11 and last_sent_date != today:
            channel = await client.fetch_channel(CHANNEL_ID)

            gif = random.choice(GIFS)

            embed = discord.Embed(description=MESSAGE)
            embed.set_image(url=gif)

            await channel.send(embed=embed)

            last_sent_date = today
            print("Message sent")

            await asyncio.sleep(60)

        await asyncio.sleep(20)

@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    client.loop.create_task(scheduler())

client.run(TOKEN)
