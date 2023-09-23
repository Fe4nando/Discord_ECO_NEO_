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