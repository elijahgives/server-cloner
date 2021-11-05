import discord, os, datetime
from colorama import init, Fore, Style

from src.utils import *

init(autoreset=True, convert=True)

client = discord.Client()

from config import input_guild_id, output_guild_id, clear_server, token

os.system("title ServerCloner - Starting...")
print("ServerCloner - Starting...")
print("")

from src.cloner import ServerCloner
            
@client.event
async def on_ready():
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))
    cloner = ServerCloner(client, guild, new_guild, clear=clear_server)
    await cloner.start()
    os.system('title ServerCloner - Completed')
    log(blue+'[ServerCloner]'+r, 'Server cloning process completed.')
    os.system('pause')

client.run(token, bot=False)