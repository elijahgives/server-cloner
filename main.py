import discord, os
from colorama import init
from src.utils import *
from config import *

init(autoreset=True, convert=True) # feel free to remove this line if you are having print issues

client = discord.Client()
if windows:
    os.system("title ServerCloner - Starting...")
print("ServerCloner - Starting...\n")

from src import ServerCloner
            
async def clone():
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))

    cloner = ServerCloner(client, guild, new_guild, clear=clear_server)
    await cloner.start()
    log(blue+'[ServerCloner]'+r, 'Server cloning process completed.')
    if windows:
        os.system('title ServerCloner - Completed')
        os.system('pause')

@client.event
async def on_ready():
    await clone()

client.run(token, bot=False)