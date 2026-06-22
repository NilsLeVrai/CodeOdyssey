import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def start():
    token = os.getenv("DISCORD_TOKEN")
    id__ = os.getenv("APP_ID")
    print(f"DISCORD_TOKEN : {token}")
    await asyncio.sleep(2)
    print(f"ID__ : {id__}")

if __name__ == "__main__":
    asyncio.run(start())
