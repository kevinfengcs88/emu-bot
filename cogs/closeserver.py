from discord.ext import commands
import os

class Closeserver(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("closeserver cog loaded")

    @commands.command()
    async def closeserver(self, ctx):
        try:
            os.startfile("C:/Users/Kevin/Desktop/commando2.bat")
            await ctx.send("Server closed.")
        except:
            await ctx.send("I am currently running in the cloud, so I can't close the server for you.")

def setup(client):
    client.add_cog(Closeserver(client))







