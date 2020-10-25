import discord, asyncio, subprocess, os, shutil
from os import system

client = discord.Client()

token = ""

os.system('mode con: cols=45 lines=10')

def owo(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print("======================".center(width))
        print("Discord Message Purger".center(width))
        print("======================".center(width))
        print("User: {0}".format(client.user).center(width))
        print("======================".center(width))
        print("Type .clear to purge all messages".center(width))
        print("Type .cleardms to purge in dms".center(width))
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '.clear':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '.cleardms':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                print(msg)
                        except:
                             pass

client.run(token, bot=False)
