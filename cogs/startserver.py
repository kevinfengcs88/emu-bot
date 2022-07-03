from discord.ext import commands
import os
import main

class Startserver(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("startserver cog loaded")

    @commands.command()
    async def startserver(self, ctx):
        if (main.server_status == True):
            await ctx.send("The server is already running.")
        else:
            try:
                os.startfile("C:/Users/Kevin/Desktop/commando.bat")
                main.server_status = True
                await ctx.send("Server started.")
            except:
                await ctx.send("I am currently running in the cloud, so I can't start the server for you.")
def setup(client):
    client.add_cog(Startserver(client))