import discord
from discord.ext import tasks
import asyncio
import logging
import os
import datetime
from zoneinfo import ZoneInfo
from parse import check_if_task, check_send

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

CHANNEL_ID = 1364972857498796042

async def forward_reply(user, birthday_name, channel):
    while True:
        reply = await client.wait_for(
            'message',
            check=lambda m: m.author.id == user.id and isinstance(m.channel, discord.DMChannel)
        )

        view = discord.ui.View()
        button_confirm = discord.ui.Button(label="Envoyer", emoji="✅", style=discord.ButtonStyle.green)
        button_again = discord.ui.Button(label="Refaire", emoji="🔄", style=discord.ButtonStyle.red)
        confirmed = False

        async def on_confirm(interaction, r=reply):
            nonlocal confirmed
            confirmed = True
            if r.attachments:
                files = [await a.to_file() for a in r.attachments]
                await channel.send(f"{user.name} :", files=files)
            else:
                await channel.send(f"{user.name} : {r.content}")
            await interaction.response.send_message("Message envoyé !", ephemeral=True)
            view.stop()

        async def on_again(interaction):
            await interaction.response.send_message("Envoie ton nouveau message :", ephemeral=True)
            view.stop()

        button_confirm.callback = on_confirm
        button_again.callback = on_again
        view.add_item(button_confirm)
        view.add_item(button_again)

        prompt_msg = await reply.channel.send("Envoyer ce message dans le salon ?", view=view)
        await view.wait()

        if confirmed:
            break
        await prompt_msg.delete()

async def send_message(birthday_boys, wishing_boys):
    channel = client.get_channel(CHANNEL_ID)

    if channel and birthday_boys:
        names = ', '.join(b['name'] for b in birthday_boys)
        await channel.send(f"@here Joyeux anniversaire à {names} !")

    for wisher in wishing_boys:
        for birthday_boy in birthday_boys:
            try:
                user = await client.fetch_user(wisher['id'])
                await user.send(
                    f"Hello ! Demain c'est l'anniv de {birthday_boy['name']} ! "
                    f"Envoie lui un petit message pour le lui souhaiter :)"
                )
                asyncio.create_task(forward_reply(user, birthday_boy['name'], channel))
            except discord.NotFound:
                logging.error(f"Utilisateur {wisher['name']} (ID {wisher['id']}) introuvable")

@tasks.loop(time=datetime.time(hour=9, minute=0, tzinfo=ZoneInfo("Europe/Paris")))
async def daily_check():
    check = check_if_task()
    if check:
        birthday_boys, wishing_boys = check_send(check)
        if birthday_boys:
            await send_message(birthday_boys, wishing_boys)

@client.event
async def on_ready():
    print(f"Bot connecté en tant que {client.user} (ID: {client.user.id})")
    if not daily_check.is_running():
        daily_check.start()

async def start():
    await client.start(os.getenv("DISCORD_TOKEN"))
