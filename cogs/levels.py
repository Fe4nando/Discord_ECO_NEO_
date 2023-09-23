import discord 
import json
import random
import PIL
import io
import asyncio
from discord.ext import commands
from discord import app_commands
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO
from Assets.access import *


class Level(commands.Cog):
    def __init__(self,client):
        self.client=client
        
 
        
    @commands.Cog.listener()
    async def on_message(self,ctx):
        if ctx.author.bot:
           return
        else:
         xp=random.randint(350,700)
         max=10000
         await open_account(ctx.author)
         users=await get_level_data()
         user=ctx.author
         try:  
          check=users[str(user.id)]['charged']
         except:
          users[str(user.id)]['charged']=0
          check=users[str(user.id)]['charged']
          with open(r'./data/level.json','w') as f:
           json.dump(users,f)
         if check==1:
            xp=xp*3
            xp=round(xp)
         users[str(user.id)]['xp']+=xp
         with open(r'./data/level.json','w') as f:
            json.dump(users,f)
         await open_account(ctx.author)
         users=await get_level_data()
         xp=users[str(user.id)]['xp']
         if xp >= max:
            currentxp=xp-max
            users[str(user.id)]['level']+=1
            users[str(user.id)]['xp']=currentxp
            with open(r'./data/level.json','w') as f:
              json.dump(users,f)
            level=users[str(user.id)]['level']
            await ctx.reply(f'{ctx.author.display_name} has leveled up to {level}')
            
    @commands.command()
    async def level(self,ctx):
        await open_account(ctx.author)
        users=await get_level_data()
        eexp=users[str(ctx.author.id)]['xp']
        level=users[str(ctx.author.id)]['level']
        Zexp=users[str(ctx.author.id)]['charged']
        exp=eexp/10000
        exppre=exp*100
        exp=exppre*17
        exp=(int(exp))
        member=ctx.author
        pfp = member.avatar.with_size(1024)
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        pfp = pfp.resize((280,280))
        if Zexp==1:
            image=Image.open(r'./Template/Levels/progressbarx.png').convert('RGBA')
            image=image.resize((exp,80))
        else :
            image=Image.open(r'./Template/Levels/progressbar.png').convert('RGBA')
            image=image.resize((exp,80))
        background=Image.open(r'./Template/Levels/blank.png').convert('RGBA')
        background.paste(image,(110,525),image)
        background.paste(pfp,(110,70),pfp)
        background.save(r'./Template/Levels/bar.png')
        layer1=Image.open(r'./Template/Levels/bar.png').convert('RGBA')
        layer2=Image.open(r'./Template/Levels/level main card overlay.png').convert('RGBA')
        layer1.paste(layer2,(0,0),layer2)
        font=ImageFont.truetype(r'./Template/Levels/pasti.otf',115)
        font1=ImageFont.truetype(r'./Template/Levels/pasti.otf',64)
        write= ImageDraw.Draw(layer1)
        string=(f'Level-{level}')
        amount=f'{eexp}/10000'
        W, H = (1920,700)
        w, h = font.getsize(string)
        w1,h2=font1.getsize(amount)
        write.text
        write.text(((W-w)/2,(H-h)/2),string,font=font,fill='white')
        write.text(((W-w1)/2,420),amount,font=font1,fill='white')
        layer1.save(r'./Template/Levels/final.png')
        x = discord.File(r"./Template/Levels/final.png",filename="final.png")
        embed = discord.Embed()
        embed.set_image(url = r"attachment://final.png")
        await ctx.send(embed=embed,file=x)
        
    @app_commands.command(name="level",description="View your level card")
    async def user(self,interaction:discord.Interaction):
        user=interaction.user
        await open_account(interaction.user)
        users=await get_level_data()
        eexp=users[str(user.id)]['xp']
        level=users[str(user.id)]['level']
        Zexp=users[str(user.id)]['charged']
        exp=eexp/10000
        exppre=exp*100
        exp=exppre*17
        exp=(int(exp))
        member=user
        pfp = member.avatar.with_size(1024)
        data = BytesIO(await pfp.read())
        pfp = Image.open(data).convert("RGBA")
        pfp = pfp.resize((280,280))
        if Zexp==1:
            image=Image.open(r'./Template/Levels/progressbarx.png').convert('RGBA')
            image=image.resize((exp,80))
        else :
            image=Image.open(r'./Template/Levels/progressbar.png').convert('RGBA')
            image=image.resize((exp,80))
        background=Image.open(r'./Template/Levels/blank.png').convert('RGBA')
        background.paste(image,(110,525),image)
        background.paste(pfp,(110,70),pfp)
        background.save(r'./Template/Levels/bar.png')
        layer1=Image.open(r'./Template/Levels/bar.png').convert('RGBA')
        layer2=Image.open(r'./Template/Levels/level main card overlay.png').convert('RGBA')
        layer1.paste(layer2,(0,0),layer2)
        font=ImageFont.truetype(r'./Template/Levels/pasti.otf',115)
        font1=ImageFont.truetype(r'./Template/Levels/pasti.otf',64)
        write= ImageDraw.Draw(layer1)
        string=(f'Level-{level}')
        amount=f'{eexp}/10000'
        W, H = (1920,700)
        w, h = font.getsize(string)
        w1,h2=font1.getsize(amount)
        write.text
        write.text(((W-w)/2,(H-h)/2),string,font=font,fill='white')
        write.text(((W-w1)/2,420),amount,font=font1,fill='white')
        layer1.save(r'./Template/Levels/final.png')
        x = discord.File(r"./Template/Levels/final.png",filename="final.png")
        embed = discord.Embed()
        embed.set_image(url = r"attachment://final.png")
        await interaction.response.defer()
        await interaction.followup.send(embed=embed,file=x)
              
    @commands.command()
    async def supercharge(self,ctx):
     await open_account(ctx.author)
     users=await get_bank_data()
     user=ctx.author
     check=users[str(user.id)]["Wallet"] 
     if check<1999999:
         await ctx.send("```INSUFFICIENT FUNDS!!!```")
     if check==1:
      users=await get_level_data()
      user=ctx.author 
      check=users[str(user.id)]['charged']
      await ctx.send("```You already have Supercharged XP!```")
     else:
         users=await get_bank_data()
         user=ctx.author
         users[str(user.id)]["Wallet"]-=2000000
         await ctx.send("⚡Supercharged Xp Enabled!")
         with open(r"./data/mainbank.json","w") as f:
          json.dump(users,f)
         users=await get_level_data()
         user=ctx.author  
         users[str(user.id)]['charged']=1
         with open(r"./data/level.json","w") as f:
          json.dump(users,f)
         await asyncio.sleep(7200)
         users[str(user.id)]['charged']=0
         with open(r"./data/level.json","w") as f:
          json.dump(users,f)
          
        
async def setup(client):
    await client.add_cog(Level(client))

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
