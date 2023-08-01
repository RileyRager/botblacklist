import discord 
from discord import *


bot  = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready(): 
    print(f'loged in to {bot.user.name}')
    try:
        tree.sync()
        print("synced to discord")
    except Exception as e: 
        print({e})
        
        
@tree.command(name = "blacklist")
async def blacklist(interaction : discord.Interaction,discord_user : str,discord_id  : int ,reason : str, roblox_user : str = "N/A",roblox_id : int = 000000000,roblox_link : str = "N/A", blacklistdoc : str ="coming soon"):
    blacklistembed  = discord.Embed(title="**New blacklist**")
    blacklistembed.add_field(name=None,value=f"reason for black list : {reason}\n\n\n\n discord user : {discord_user}")