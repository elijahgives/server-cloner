import discord, os
from colorama import init, Fore, Style
from src.utils import *
from config import *

init(autoreset=True, convert=True)

client = discord.Client()

os.system("title ServerCloner - Starting...")
print("ServerCloner - Starting...\n")

from src.cloner import ServerCloner
            
async def start(client, input_guild, output_guild):
    guild = client.get_guild(int(input_guild_id))
    new_guild = client.get_guild(int(output_guild_id))

    cloner = ServerCloner(client, input_guild, output_guild, clear=clear_server)
    await cloner.start()

async def finish():
    os.system('title ServerCloner - Completed')
    log(blue+'[ServerCloner]'+r, 'Server cloning process completed.')
    os.system('pause')

@client.event
async def on_ready():
    await start()
    await finish()

client.run(token, bot=False)