import asyncio
import os
from dotenv import load_dotenv
from bot import start

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
APP_ID = os.getenv("APP_ID")
PUBLIC_KEY = os.getenv("PUBLIC_KEY")

"""
run en tant que main
"""

if __name__ == "__main__":
    asyncio.run(start())
