import discord
from discord.ext import commands
from discord.ui import Button,View
import random
import json
import time
from Assets.presets import *
from Assets.access import *



class Jobs(commands.Cog):
    def __init__(self,client):
     self.client=client
     
    @commands.command()
    @commands.cooldown(1,2700,commands.cooldowns.BucketType.user)
    async def work(self,ctx):
     order=random.randint(1,2)
     fake1=random.randint(1,300)
     fake2=random.randint(1,300)
     a=random.randint(1,13)
     y=random.randint(10,201)
     z=random.randint(10,250)
     print(a)
     print(y)
     print(z)
     op1=(a*y)
     op2=(op1+z)
     print(op2)
     question=(f'{a}x + {z} = {op2}')
     embed=discord.Embed(title="Algebra",description=f'```\n  {question}  \n\n\n Find the value of X``` ',
                         color=blurple)
     button1=Wrong(label=fake1,style=discord.ButtonStyle.blurple)
     button2=Wrong(label=fake2,style=discord.ButtonStyle.blurple)
     buttonans=Button(label=y,style=discord.ButtonStyle.blurple)
     if order == 1:
      view=View()
      view.add_item(buttonans)
      view.add_item(button1)
      view.add_item(button2)
      await ctx.send(embed=embed,view=view)
     if order ==3:
      view=View()
      view.add_item(button1)
      view.add_item(button2)
      view.add_item(buttonans)
      await ctx.send(embed=embed,view=view)
     if order ==2:
      view=View()
      view.add_item(button2)
      view.add_item(buttonans)
      view.add_item(button1)
      await ctx.send(embed=embed,view=view)
     async def button_callback(interaction):
          earnings=5000
          await open_account(ctx.author)
          users=await get_bank_data()
          user=ctx.author
          users[str(user.id)]["Wallet"]+=earnings
          users[str(user.id)]["Hours"]+=1
          with open(r"./data/mainbank.json","w") as f:
           json.dump(users,f)
          embed=discord.Embed(title="Answer is Correct!",color=blurple)
          embed.add_field(name="Salary",value=f"You have earned {earnings} and has been placed into your wallet")
          await interaction.response.edit_message(embed=embed,view=None)
     buttonans.callback=button_callback
        
    @work.error
    async def error(self,ctx,error):
     if isinstance(error,commands.CommandOnCooldown):
        msg="It looks like you completed your work already! Try again <t:{}:R>".format(int(time.time() + error.retry_after))
        await ctx.send(msg)
      


            
class Wrong(Button):
    async def callback(self,interaction):
        embed=discord.Embed(title="Answer is Incorrect",color=blurple)
        await interaction.response.edit_message(embed=embed,view=None)
      


async def setup(client):
    await  client.add_cog(Jobs(client))


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