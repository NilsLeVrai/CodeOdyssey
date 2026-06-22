import asyncio
import os
from dotenv import load_dotenv
from bot import init

load_dotenv()

async def start():
    init()
    token = os.getenv("DISCORD_TOKEN")
    id__ = os.getenv("APP_ID")
    print(f"DISCORD_TOKEN : {token}")
    await asyncio.sleep(2)
    print(f"ID__ : {id__}")

if __name__ == "__main__":
    asyncio.run(start())
