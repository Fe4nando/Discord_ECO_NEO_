import discord
from discord.ext import commands
from discord.ui import Button,View
import random
import json
import time
from Assets.access import *

class A2(commands.Cog):
    def __init__(self,client):
        self.client=client
     
    @commands.command()
    @commands.cooldown(1,120,commands.cooldowns.BucketType.user)
    async def beg(self,ctx):
     await open_account(ctx.author)
     users=await get_bank_data()
     user=ctx.author
     earnings=random.randrange(251)
     await ctx.send(f"Someone gave you {earnings} money!")
     users[str(user.id)]["Wallet"]+=earnings
     with open(r"./data/mainbank.json","w") as f:
        json.dump(users,f)
        
    @beg.error
    async def error(self,ctx,error):
     if isinstance(error,commands.CommandOnCooldown):
        msg="Oops! Try again <t:{}:R>".format(int(time.time() + error.retry_after))
        await ctx.send(msg)
        
    @commands.command()
    async def withdraw(self,ctx,amount=None):
     await open_account(ctx.author)
     if amount==None:
        await ctx.send("Please enter the amount")
        return
     bal = await update_bank(ctx.author)
     amount=int(amount)
     if amount>bal[1]:
        await ctx.send("You dont have that much money")
        return
     if amount<0:
        await ctx.send("Please Enter a Positive Value")
        return
     await update_bank(ctx.author,amount)
     await update_bank(ctx.author,-1*amount,"Bank")
     await ctx.send(f"{amount} has been withdrew from your account")
    
    @commands.command()
    async def dep(self,ctx,amount=None):
     await open_account(ctx.author)
     if amount==None:
        await ctx.send("Please enter the amount")
        return
     bal = await update_bank(ctx.author)
     amount=int(amount)
     if amount>bal[0]:
        await ctx.send("Insuffient Found")
        return
     if amount<0:
        await ctx.send("Please Enter a Positive Value")
        return
     await update_bank(ctx.author,-1*amount)
     await update_bank(ctx.author,amount,"Bank")
     await ctx.send(f"{amount} has been deposited to your account")
        


        
    @commands.command()
    @commands.cooldown(1,72000,commands.cooldowns.BucketType.user)
    async def daily(self,ctx):
     await open_account(ctx.author)
     users=await get_bank_data()
     user=ctx.author
     users[str(user.id)]["daily count"]+=1
     daily_check=users[str(user.id)]["daily count"]
     daily=5000
     if daily_check>9:
        daily=10000
     if daily_check>49:
        daily=25000
     if daily_check>99:
        daily=50000
    
     earning=daily
     users[str(user.id)]["Wallet"]+=earning
     await ctx.send(f"Your Daily Amount:{daily} has been given to you! Day Count:{daily_check}")
    
     with open(r"./data/mainbank.json","w") as f:
        json.dump(users,f)
        
    @daily.error
    async def error(self,ctx,error):
     if isinstance(error,commands.CommandOnCooldown):
        msg="Looks like you hit a roadblock! Try again <t:{}:R>".format(int(time.time() + error.retry_after))
        await ctx.send(msg)
     
async def setup(client):
    await client.add_cog(A2(client))

async def open_account(user):
    users=await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]={}
        users[str(user.id)]["Wallet"]=0
        users[str(user.id)]["Bank"]=0
        users[str(user.id)]["Net"]=0
        users[str(user.id)]["daily count"]=0
        users[str(user.id)]["Job"]=0
        users[str(user.id)]["Hours"]=0
        users[str(user.id)]["Tree"]=0
        
       

    with open(r"./data/mainbank.json","w") as f:
        json.dump(users,f)
       
        
    return True
        

async def get_bank_data():
    with open (r"./data/mainbank.json","r") as f:
        users=json.load(f)

        return users 
        
        
async def open_account(user):
    users= await get_level_data()
        
    if str(user.id)in users:
        return False
    else:
        users[str(user.id)]={}
        users[str(user.id)]['level']=1
        users[str(user.id)]['xp']=0
        users[str(user.id)]['charged']=0
        
    with open(r'./data/level.json','w') as f:
        json.dump(users,f)

    
async def get_level_data():
    with open(r'./data/level.json','r') as f:
        users=json.load(f)
    return users

async def update_bank(user,change=0,mode="Wallet"):
    users=await get_bank_data()
    users[str(user.id)][mode]+=change
    with open(r"./data/mainbank.json","w") as f:
        json.dump(users,f)
    bal=[users[str(user.id)]["Wallet"],users[str(user.id)]["Bank"]]
    return bal