import discord
import random
import os

client = discord.Client()

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
        await message.channel.send(f'Hi {username}')
    if user_message.lower() == '!startserver':
        os.startfile('C:/Users/Kevin/Desktop/commando.bat')
        await message.channel.send('Server started')
    if user_message.lower() == '!closeserver':
        os.startfile('C:/Users/Kevin/Desktop/commando2.bat')
        await message.channel.send('Server closed')

client.run(TOKEN)