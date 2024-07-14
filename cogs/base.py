import discord
import random
import time

from discord.ext import commands
from discord.ui import Button,View
from discord import app_commands
from Assets.presentation import *
from Assets.presets import *
from Assets.embeds import *
from Assets.gifs import *
from Assets.mapping import*


textp = random.choice(plistr)
gifsp = random.choice(plistgif)
textn = random.choice(nlistr)
gifsn = random.choice(nlistgif)

milo_id="18052024"


class BASE(commands.Cog):
    def __init__(self,client):
        self.client=client


    class MyView(View):

        @discord.ui.button(label="Yes", style=discord.ButtonStyle.green)
        async def button1_callback(self, interaction: discord.Interaction, button: Button):
            text = random.choice(plistr)
            gifs = random.choice(plistgif)
            if textp == text:
                text = random.choice(plistr)
            if gifsp == gifs:
                gifs = random.choice(plistgif)

            embed = discord.Embed(title="", description=text, color=discord.Color.from_rgb(255, 255, 255))
            embed.set_image(url=gifs)
            await interaction.response.edit_message(embed=embed, view=self)

        @discord.ui.button(label="No", style=discord.ButtonStyle.red)
        async def button_callback(self, interaction: discord.Interaction, button: Button):
            textns = random.choice(nlistr)
            gifsns = random.choice(nlistgif)
            if textn == textns:
                textns = random.choice(nlistr)
            if gifsn == gifsns:
                gifsns = random.choice(nlistgif)

            embed = discord.Embed(title="", description=textns, color=discord.Color.from_rgb(255, 255, 255))
            embed.set_image(url=gifsns)
            await interaction.response.edit_message(embed=embed, view=self)

    @app_commands.command(name="stop_smiling", description="Do this!")
    async def stop_smiling(self, interaction: discord.Interaction):
        Embed = discord.Embed(title="", description="Stop Smiling Maariyah!", color=discord.Color.from_rgb(255, 255, 255))
        Embed.set_image(url=default) 
        view = BASE.MyView()
        await interaction.response.send_message(embed=Embed, view=view)

    @app_commands.command(name="image", description="your pookie")
    async def image1(self, interaction: discord.Interaction):
        Embed = discord.Embed(title="", description="meow", color=discord.Color.from_rgb(255, 255, 255))
        ier=random.choice(katts)
        Embed.set_image(url=ier) 
        await interaction.response.send_message(embed=Embed)

    @app_commands.command(name="ask_frosty", description="i will meow back")
    async def ask_me(self, interaction: discord.Interaction, question:str):
        Answers=random.choice(answers)
        Text=f"<:frosty:1255848519818936463> Question: {question} \n<:frosty:1255848519818936463> Answer: {Answers}"
        await interaction.response.send_message(Text)
        
    

    
    @app_commands.command(name="presentations", description="links to our presentations")
    async def present(self, interaction: discord.Interaction):
        embed=discord.Embed(title="**Presentations**", description="Made by us", color=blurple)
        for x in links:
            Name=x["name"]
            Link=x["Link"]
            By=x["By"]
            embed.add_field(name=f"**{Name}**\nBy:{By}", value=f"[Click Here]({Link})", inline=False)
        await interaction.response.send_message(embed=embed)
        
    class ClickGameView(View):
        def __init__(self, interaction):
            super().__init__(timeout=None)
            self.interaction = interaction
            self.winner = None

        @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary)
        async def click_button(self, interaction: discord.Interaction, button: Button):
            if self.winner is None:
                self.winner = interaction.user
                await interaction.response.edit_message(content=f"{interaction.user.mention} won the game!", view=None)
            else:
                await interaction.response.send_message("The game is already over!", ephemeral=True)

    @app_commands.command(name="love_roulette", description="prove your love")
    async def click_game(self, interaction: discord.Interaction):
        timer=random.randint(5,10)
        await interaction.response.send_message("Message Waiting...")
        time.sleep(timer)
        view = BASE.ClickGameView(interaction)
        await interaction.edit_original_response(content="Click the button as fast as you can!", view=view)

    @app_commands.command(name="about_me", description="mwah")
    async def about_me(self, interaction: discord.Interaction):
        Embed = discord.Embed(title="**About Me!**", description=string, color=discord.Color.from_rgb(255, 255, 255))
       
        await interaction.response.send_message(embed=Embed)

    @app_commands.command(name="pet",description="pet milo")
    async def transfer(self,interaction:discord.Interaction):
        coins=random.randint(100,150)
        _user=interaction.user
        _user=_user.id
        users=await get_bank_data()
        await open_account(_user)
        users[str(_user)]["Coin"]+=coins
        users[str(_user)]["Pet"]+=1
        with open(r"./data/users.json","w") as f:
            json.dump(users,f,indent=2)
        #_Milo
        await open_account(milo_id)
        users=await get_bank_data()
        users[str(milo_id)]["Pet"]+=1
        with open(r"./data/users.json","w") as f:
            json.dump(users,f,indent=2)
        await interaction.response.send_message(f"{interaction.user.display_name} petted milo and has earned {coins} coins!")

async def setup(client):
    await client.add_cog(BASE(client))