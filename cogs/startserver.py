import discord
from discord.ext import commands
import asyncio
import os

class Startserver(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("startserver cog loaded")

    @commands.command()
    async def startserver(self, ctx):
        os.startfile("C:/Users/Kevin/Desktop/commando.bat")
        await ctx.send("Server started.")

def setup(client):
    client.add_cog(Startserver(client))