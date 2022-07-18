# Emu Bot
Emu Bot is a Discord bot that enables users to interact with a [dedicated server](https://theforest.fandom.com/wiki/Dedicated_Servers) for *[The Forest](https://store.steampowered.com/app/242760/The_Forest/)* remotely.

## Features
1. `!startserver` - Remotely start a server for *The Forest*
2. `!closeserver` - Remotely close a server for *The Forest*
3. `!remind` - Remind users about upcoming tasks after a specified amount of time (formatted as `!remind 10s buy milk`, where 10
can be substituted for any integer, 's' can be substituted for 'd', 'h', or 'm' for days, hours, or minutes, respectively, and
"buy milk" can be substituted for any alphanumeric string)
4. `!ping` - Responds back with "pong"
5. Says hello back to users who say "hi" in the Discord server

## Dedicated Servers
Dedicated servers for Endnight Games are a tool implemented in update v0.59 of the survival horror game. They are designed to allow players to keep servers running perpetually, either hosted locally or through server providers. Prior to dedicated servers, the game required the host to not only host the game, but also "play" the game. In other words, the host's computer would be forced to perform graphical computations, as the host would be in the game world as well. 

A dedicated server enables a host to run a game server without connecting to it; idling a dedicated server is much less taxing than idling a traditional game server. The server becomes even less taxing when paying for a server provider so that the game server is ran on another computer, owned by a hosting service.

The bot is able to start or close the game server via two batch files on my desktop. Each batch file is just one line of code and are as follows:

`commando.bat` corresponds to the command `!startserver`
```
start "" "C:\Program Files (x86)\Steam\steamapps\common\TheForestDedicatedServer\TheForestDedicatedServer.exe"
```
`commando2.bat` corresponds to the command `!closeserver`
```
taskkill /IM TheForestDedicatedServer.exe
```

## Limitations
Emu Bot is currently hosted using the popular method of [Replit](https://replit.com/) and [UptimeRobot](https://uptimerobot.com/). Since Replit utilizes cloud computing, certain Python packages, including the `os` package, are different from their local machine counterparts. As a result, when Emu Bot is running in the cloud, it is unable to perform the `!startserver` and `!closeserver` commands. However, when the bot is run locally on my desktop, it allows users in (a) server(s) with Emu Bot to both remotely start and close the dedicated server.
