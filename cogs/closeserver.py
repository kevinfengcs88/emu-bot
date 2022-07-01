import discord
from discord.ext import commands
import asyncio
import os

class Closeserver(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('closeserver cog loaded')

    @commands.command()
    async def closeserver(self, ctx):
        os.startfile('C:/Users/Kevin/Desktop/commando2.bat')
        await ctx.send('Server closed.')

def setup(client):
    client.add_cog(Closeserver(client))







