import discord 
from discord.ext import commands
from discord import app_commands
import json
from cogs.levels import *
from Assets.access import *


class user(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def balance(self,ctx):
     await open_account(ctx.author)
     user=ctx.author
     users=await get_bank_data()
     users1=await get_level_data()
     wallet_amt=users[str(user.id)]["Wallet"]
     bank_amt=users[str(user.id)]["Bank"]
     net_amt=users[str(user.id)]["Net"]
     net_amt=net_amt+wallet_amt+bank_amt
     work_hrs=users[str(user.id)]["Hours"]
     level=users1[str(user.id)]["level"]
     daily=users[str(user.id)]["daily count"]
     em=discord.Embed(title=f"{user.display_name}'s balance",color=discord.Color.from_rgb(225,215,0))
     em.add_field(name="💴 **Wallet**:",value=f"{wallet_amt:,}",inline=True)
     em.add_field(name="💳 **Bank**:",value=f"{bank_amt:,}",inline=True)
     em.add_field(name="💰 **Net Worth**:",value=f"{net_amt:,}",inline=False)
     em.add_field(name="🏅 **Level**:",value=f"{level:,}",inline=True)
     em.add_field(name="📅 **Daily count**:",value=f"{daily:,}",inline=True)
     em.add_field(name="🔨 **Work Hours**:",value=f"{work_hrs:,}",inline=True)
     await ctx.send(embed=em)
       
    @app_commands.command(name="hello",description="test")
    async def user(self,interaction:discord.Interaction):
     await interaction.response.send_message("HI!")

    @app_commands.command(name="inventory",description="View your cash and items")
    async def user(self,interaction:discord.Interaction):
       user=interaction.user
       await open_account(interaction.user)
       users=await get_bank_data()
       users1=await get_level_data()
       wallet_amt=users[str(user.id)]["Wallet"]
       bank_amt=users[str(user.id)]["Bank"]
       net_amt=users[str(user.id)]["Net"]
       net_amt=net_amt+wallet_amt+bank_amt
       work_hrs=users[str(user.id)]["Hours"]
       level=users1[str(user.id)]["level"]
       daily=users[str(user.id)]["daily count"]
       em=discord.Embed(title=f"{user.display_name}'s balance",color=discord.Color.from_rgb(225,215,0))
       em.add_field(name="💴 **Wallet**:",value=f"{wallet_amt:,}",inline=True)
       em.add_field(name="💳 **Bank**:",value=f"{bank_amt:,}",inline=True)
       em.add_field(name="💰 **Net Worth**:",value=f"{net_amt:,}",inline=False)
       em.add_field(name="🏅 **Level**:",value=f"{level:,}",inline=True)
       em.add_field(name="📅 **Daily count**:",value=f"{daily:,}",inline=True)
       em.add_field(name="🔨 **Work Hours**:",value=f"{work_hrs:,}",inline=True)
       await interaction.response.send_message(embed=em)
    

        
async def setup(client):
    await client.add_cog(user(client))