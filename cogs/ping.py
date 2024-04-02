import discord
from discord.ext import commands
import asyncio

class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ping cog loaded")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")

def setup(client):
    client.add_cog(Ping(client))