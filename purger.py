import discord, asyncio, time
from discord.ext import commands, tasks

token = ''
prefix = '+'

poop = discord.Client()
poop = commands.Bot(
    description='purger',
    command_prefix=prefix,
    self_bot=True
)

@poop.event
async def on_ready():
	print("ready! +purge (amount) to delete messages")

@poop.command(aliases=['p'])
async def purge(ctx, amount: int):#deletes your desired amount of previous messages
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount):
        try:
           await message.delete()
        except:
            pass

poop.run(token, bot=False)
