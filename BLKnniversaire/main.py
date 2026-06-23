import asyncio
import os
from dotenv import load_dotenv
from bot import init

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = os.getenv("APP_ID")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")



async def start():
    print("testttt")
    await init()
    #print(f"DISCORD_TOKEN : {DISCORD_TOKEN}")
    #await asyncio.sleep(2)
    #print(f"ID__ : {APP_ID}")


"""
run en tant que main
"""

if __name__ == "__main__":
    asyncio.run(start())
