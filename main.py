
import os
import discord
import asyncio 
import random

from discord.ext import commands 
from discord.ui import Button,View
from discord import app_commands
from Assets.embeds import *
from Assets.gifs import *



class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='meow', 
                         intents=discord.Intents.all())
        self.synced=False
        
    async def setup_hook(self):
     for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        await self.load_extension(f'cogs.{filename[:-3]}')

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await client.tree.sync()
            self.synced=True
        print('Bot is Connected to Discord')
        count=1
        count=1
        while (count < 3):
          await self.change_presence(status=discord.Status.idle,activity=discord.Game("/stop_smiling"))
          await asyncio.sleep(15)
          await self.change_presence(status=discord.Status.idle,activity=discord.Game("/cutie_patootie"))
          await asyncio.sleep(15)
         
  
        
client=Client()
cilent=client


client.run("MTI1NTQ5MDIxMjIzOTI0OTQ0OQ.GoL6JQ.1RZMJhTUV-h1XdzUwJzdghJCVkpaS4ak-xBjxE")
    





