import discord 
from discord import *
from bottoken import token

bot  = discord.Client(intents=discord.Intents.all())
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready(): 
    print(f'loged in to {bot.user.name}')
    try:
        await tree.sync()
        print("synced to discord")
    except Exception as e: 
        print({e})
        
        
@tree.command(name = "blacklist")
async def blacklist(interaction : discord.Interaction,discord_user : str,discord_id  : discord.Member| discord.User,reason : str, roblox_user : str = "N/A",roblox_id : int = 000000000,roblox_link : str = "N/A", blacklistdoc : str ="coming soon",ping : str = None):
    blacklistembed  = discord.Embed(title="**New blacklist**",color=discord.Color.from_rgb())
    blacklistembed.add_field(name=None,value=f"reason for black list : {reason}\n\n\n\n discord user : {discord_user}\n discord id : {discord_id}\n\n,Roblox user : {roblox_user}\n,roblox id : {roblox_id}\n\n\n roblox profile : {roblox_link}\n,black list doc : {blacklistdoc}")
    interaction.channel.send({ping},embed=blacklistembed)
    discord_id.ban(reason=reason)

    
    
bot.run(token)
    