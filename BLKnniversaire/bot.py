import discord
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


"""
Tout est en vrac pour le moment, on fera la doc plus tard
"""

@client.event
async def on_ready():
    print(f"Bot connecté en tant que {client.user} (ID: {client.user.id})")
    channel = client.get_channel(1364972857498796042)
    if channel:
        # await channel.send("@here test cedric")
        pass
    #user_wadi = await client.fetch_user(193886188166184960)
    user_nils = await client.fetch_user(308381699639607306)
    #await user_wadi.send("repond un truc mon Wado des sables")
    await user_nils.send("mim's toi")

    async def forward_reply(user, label):
        while True:
            print(f"[{label}] En attente d'un message...")
            reply = await client.wait_for('message', check=lambda m: m.author.id == user.id and isinstance(m.channel, discord.DMChannel))
            print(f"[{label}] Message reçu : {reply.content}")

            view = discord.ui.View()
            button_confirm = discord.ui.Button(label="Envoyer", emoji="✅", style=discord.ButtonStyle.green)
            button_again = discord.ui.Button(label="Refaire", emoji="🔄", style=discord.ButtonStyle.red)
            confirmed = False

            async def on_confirm(interaction, r=reply):
                nonlocal confirmed
                confirmed = True
                if r.attachments:
                    files = [await a.to_file() for a in r.attachments]
                    await channel.send(f"{label} :", files=files)
                else:
                    await channel.send(f"{label} : {r.content}")
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

   # asyncio.create_task(forward_reply(user_wadi, "Wadi"))
    asyncio.create_task(forward_reply(user_nils, "Nils"))

async def init():
    await client.start(os.getenv("DISCORD_TOKEN"))
