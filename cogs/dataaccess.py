import discord
from discord.ext import commands
from Assets.presets import *
from Assets.access import *



class A1(commands.Cog):
    def __init__(self,client):
        self.client=client
     
    @commands.command()
    async def download(self,ctx):
        if ctx.author.id==738243110949355672:
         await ctx.send(file=discord.File(r'./data/mainbank.json'))
         await ctx.send(file=discord.File(r'./data/level.json'))
        else:
         await ctx.send("You Cant Download the Data unless your Fernando.")
        
async def setup(client):
    await client.add_cog(A1(client))