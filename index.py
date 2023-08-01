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
        