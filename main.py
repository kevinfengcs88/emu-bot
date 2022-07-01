import asyncio
import discord
import random
import os
from dotenv import load_dotenv
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    roles = str(message.author.roles)
    print(f'{username}: {user_message} ({channel}) [{roles}]')

    # forest_role = discord.utils.get(ctx.guild.roles, name="The Forest")

    if message.author == client.user:
        return
    if user_message.lower() == 'hi':
        # if forest_role in message.author.roles:
        #     await message.channel.send(f'Hi {username}, you Forester!')
        # else:
        await message.channel.send(f'Hi {username}!')
    if user_message.lower() == '!startserver':
        os.startfile('C:/Users/Kevin/Desktop/commando.bat')
        await message.channel.send('Server started.')
    if user_message.lower() == '!closeserver':
        os.startfile('C:/Users/Kevin/Desktop/commando2.bat')
        await message.channel.send('Server closed.')
    await client.process_commands(message)

load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)