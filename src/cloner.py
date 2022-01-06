from .utils import *
import discord

class ServerCloner:
    def __init__(self, client: discord.Client, input_guild: discord.Guild, output_guild: discord.Guild, clear: bool = False):
        """ Create a new ServerCloner instance. 
        ``client``: the client you're cloning on: a user account, as a discord.Client object.
        ``input``: the guild to copy, as a discord.Guild object.
        ``output``: the guild to paste onto, as a discord.Guild object.
        ``clear``: whether to delete channels and roles on the output guild. defaults to ``False``.
        """
        self.created_map = {}
        self.client = client
        self.input_guild = input_guild
        self.output_guild = output_guild
        self.clear = clear
    
    async def clear_server(self):
        log(blue+'[ClearServer]'+r, 'Beginning clearing server.')
        log(blue+'[ClearServer]'+r, 'Current Stage: Roles')
        for role in self.output_guild.roles:
            try:
                await role.delete()
                log(green+'[ClearServer]'+r, f'Deleted role {cyan+str(role.id)+r}.')
            except:
                log(red+'[ClearServer]'+r, f'Failed to delete role {cyan+str(role.id)+r}.')
                continue

        log(blue+'[ClearServer]'+r, 'Current Stage: Channels')

        for channel in self.output_guild.channels:
            try:
                await channel.delete()
                log(green+'[ClearServer]'+r, f'Deleted channel {cyan+str(channel.id)+r}.')
            except:
                log(red+'[ClearServer]'+r, f'Failed to delete channel {cyan+str(channel.id)+r}.')

        log(green+'[ClearServer]'+r, 'Done clearing server, moving on to cloning process.')

    async def create_roles(self):
        server_roles = []
        for role in self.input_guild.roles:
            server_roles.insert(0, role)
        for role in server_roles:
            new_role = await self.output_guild.create_role(
                name=role.name, permissions=role.permissions, colour=role.colour, hoist=role.hoist, mentionable=role.mentionable
            )
            log(blue+'[ServerCloner]'+r, f'Created role {cyan+str(new_role.id)+r}.')
    
    async def create_categories(self):
        
        for category in self.input_guild.categories:
            overwrites_to = {}
            for key, value in category.overwrites.items():
                role = discord.utils.get(self.input_guild.roles, name=key.name)
                overwrites_to[role] = value
            new_category = await self.output_guild.create_category_channel(
                name=category.name, overwrites=overwrites_to
            )
            await new_category.edit(
                position=int(category.position), nsfw=category.is_nsfw()
            )
            log(blue+'[ServerCloner]'+r, f'Created category {cyan+str(category.id)+r}.')
            self.created_map[str(category.id)] = new_category.id
    
    async def create_text_channels(self):
        for channel in self.input_guild.text_channels:
            overwrites_to = {}
            for key, value in channel.overwrites.items():
                    role = discord.utils.get(self.input_guild.roles, name=key.name)
                    overwrites_to[role] = value
            if channel.category_id is not None:
                new_category_id = self.created_map.get(str(channel.category_id))

                new_category = await self.client.fetch_channel(int(new_category_id))
                new_channel = await new_category.create_text_channel(
                    name=channel.name, topic=channel.topic, position=channel.position, slowmode_delay=channel.slowmode_delay, 
                    nsfw=channel.is_nsfw(), overwrites=overwrites_to
                )
                log(blue+'[ServerCloner]'+r, f'Created channel {cyan+str(new_channel.id)+r}.')
            else:
                new_channel = await self.output_guild.create_text_channel(name=channel.name, topic=channel.topic, position=channel.position,
                                                slowmode_delay=channel.slowmode_delay, nsfw=channel.is_nsfw(),
                                                overwrites=overwrites_to)
                log(blue+'[ServerCloner]'+r, f'Created channel {cyan+str(new_channel.id)+r}.')

    async def create_voice_channels(self):
        for channel in self.input_guild.voice_channels:
            overwrites_to = {}
            for key, value in channel.overwrites.items():
                    role = discord.utils.get(self.input_guild.roles, name=key.name)
                    overwrites_to[role] = value
            if channel.category_id is not None:
                new_category_id = self.created_map.get(str(channel.category_id))
                new_category = await self.client.fetch_channel(int(new_category_id))
                new_channel = await new_category.create_voice_channel(name=channel.name, position=channel.position,
                                                    user_limit=channel.user_limit, overwrites=overwrites_to)
                log(blue+'[ServerCloner]'+r, f'Created channel {cyan+str(new_channel.id)+r}.')
            else:
                new_channel = await self.output_guild.create_voice_channel(name=channel.name, position=channel.position,
                                                 user_limit=channel.user_limit, overwrites=overwrites_to)
                log(blue+'[ServerCloner]'+r, f'Created channel {cyan+str(new_channel.id)+r}.')

    async def execute_clear_server(self):
        if self.clear:
            await self.clear_server()
        else:
            log(red+'[ClearServer]'+r, 'Clearing server was disabled in settings, skipping.')

    async def start(self):
        not_finished = True
        while not_finished:
            await self.execute_clear_server()
            await self.create_roles()
            await self.create_categories()
            await self.create_text_channels()
            await self.create_voice_channels()
            not_finished = False