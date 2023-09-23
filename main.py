import os
from webserver import keep_alive
import discord 
import json
from discord.ext import commands 
from discord import app_commands
from Assets.embeds import *
from Assets.access import *



#keep_alive()
class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='$', 
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
        await self.change_presence(status=discord.Status.online,activity=discord.Game("$help"))
        
client=Client()
client.remove_command('help')
cilent=client

@cilent.command()
async def help(ctx):
  await ctx.send(embed=help1)

@client.command()
async def patch(ctx):
   await ctx.send(embed=xzy)
  


client.run("")
    


#keep_alive()
    


