import csv
import datetime
import os
import logging

"""
Pas le plus palpitant, on parse le csv
"""
logging.basicConfig(level=logging.ERROR) 
filepath = os.path.dirname(os.path.abspath(__file__))

def check_if_task():
    print("if_task")
    check_today = 0
    check_tomorrow = 0
    today = datetime.datetime.today().strftime("%d-%m")
    tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m")
    with open(os.path.join(filepath, 'birthday.csv'), newline='') as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)
        for row in reader:
            if len(row) >= 3:
                if row[2][:5] == (tomorrow):
                    check_today = 1
                elif row[2][:5] == (today):
                    check_tomorrow = 2;
                else:
                    continue
    return check_today + check_tomorrow

def send_wishes():
    return None

async def send_messages():
    tomorrow_birthday = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m")
    birthday_boys = []
    wishing_boys = []
    with open(os.path.join(filepath, 'birthday.csv'), newline='') as data:
        reader = csv.reader(data, delimiter=',')
        next(reader)
        for row in reader:
            if len(row) >= 3:
                if row[2][:5] == tomorrow_birthday:
                    birthday_boys.append(row[1])
                else:
                    wishing_boys.append(row[1])
    for i in wishing_boys:
        for j in birthday_boys:
            user = client.fetch_user(wishing_boys[i])
            await user.send(f"Hello, demain c'est l'anniv de {birthday_boys[j]}! Emvoie lui un petit message pour le lui souhaiter :)")
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
            asyncio.create_task(forward_reply(user, ""))

def check_send(check):
    if check == 1 or check == 3: #at least one birthday today
        send_wishes() # send birthday wishes to the channel
    elif check == 2 or check == 3: #
        send_messages() # send birthday reminders in private messages
    return birthday_boys, wishing_boys
