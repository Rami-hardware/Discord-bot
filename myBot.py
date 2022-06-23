import os
from tracemalloc import stop
import discord 
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix= ".")

mess = "ace"
@bot.event
async def on_message(message):
	if message.content.find(mess) == True:
		await message.channel.send("pies are better than cakes. change my mind.")
        
bot.run(DISCORD_TOKEN)