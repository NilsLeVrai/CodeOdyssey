import discord
import asyncio
import os

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connecté en tant que {client.user} (ID: {client.user.id})")
    channel = client.get_channel(1364972857498796042)
    if channel:
        # await channel.send("@here test cedric")
        continue
    user_wadi = await client.fetch_user(193886188166184960)
    user_nils = await client.fetch_user(308381699639607306)
    await user_wadi.send("repond un truc mon Wado des sables")
    await user_nils.send("mim's toi")

    async def forward_reply(user, label):
        reply = await client.wait_for('message', check=lambda m: m.author.id == user.id and isinstance(m.channel, discord.DMChannel))
        if channel:
            await channel.send(f"{label} : {reply.content}")

    asyncio.create_task(forward_reply(user_wadi, "Wadi"))
    asyncio.create_task(forward_reply(user_nils, "Nils"))

async def init():
    await client.start(os.getenv("DISCORD_TOKEN"))
