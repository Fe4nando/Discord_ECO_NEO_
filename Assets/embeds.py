import discord
from readme import * 

help1=discord.Embed(title="Available Bot Commands",color=discord.Color.from_rgb(0, 255, 255))
help1.add_field(name="`$balance`",value="Shows the balance of the account")
help1.add_field(name="`$dep amount`",value="Transfer Money from Wallet to Bank")
help1.add_field(name="`$withdraw amount`",value="Trasnfer Money from Bank to Wallet")
help1.add_field(name="`$beg`",value="Beg for money when your to poor")
#help1.add_field(name="`$transfer @mention amount`",value="Transfer Money from you to a member")
help1.add_field(name="`$daily`",value="Daily Earnings")
#help1.add_field(name="`$invest`",value="Invest in Companies and Earn!")
help1.add_field(name="`$work`",value="Work to Earn points!")
help1.set_footer(text="Slash Commands are available too!")

Version=Info_BASE["Version"]
Builds=Info_BASE["Builds"]

xzy=discord.Embed(title="Bot Updates",color=discord.Color.from_rgb(255,255,255))
xzy.add_field(name=f"Bug Fixes",value=Fixes)
xzy.set_footer(text=f"Version:{Version} Builds:{Builds}")