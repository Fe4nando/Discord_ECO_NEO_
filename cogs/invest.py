import discord
from discord.ext import commands
from discord.ui import Button,View
import random
import json
import time
from Assets.access import *

class Invest(commands.Cog):
    def __init__(self,client):
        self.client=client
     
    @commands.command()
    @commands.cooldown(1,600,commands.cooldowns.BucketType.user)
    async def invest(self,ctx,amount):
     await open_account(ctx.author)
     users=await get_bank_data()
     user=ctx.author
     xp=random.randint(1,2)
     precentage=random.randint(1,100)
     amount=int(amount)
     if xp == 1:
      earnings=amount+(amount*(precentage/100))
      type="Gained"
     if xp== 2:
      type="Loss"
      earnings=amount-(amount*(precentage/100))   
     users[str(user.id)]["Net"]+=earnings
     with open(r"./data/mainbank.json","w") as f:
        json.dump(users,f)
     await ctx.send(f"{type}:{earnings}")
 
        
    @invest.error
    async def error(self,ctx,error):
     if isinstance(error,commands.CommandOnCooldown):
        msg="Oops! Try again <t:{}:R>".format(int(time.time() + error.retry_after))
        await ctx.send(msg)
        

        


 
     
async def setup(client):
    await client.add_cog(Invest(client))










































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