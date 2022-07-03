from discord.ext import commands
import os
import main

class Closeserver(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("closeserver cog loaded")

    @commands.command()
    async def closeserver(self, ctx):
        if (main.server_status == True):
            try:
                os.startfile("C:/Users/Kevin/Desktop/commando2.bat")
                main.server_status = False 
                await ctx.send("Server closed.")
            except:
                await ctx.send("I am currently running in the cloud, so I can't close the server for you.")
        else:
            await ctx.send("The server has already been closed.")

def setup(client):
    client.add_cog(Closeserver(client))







