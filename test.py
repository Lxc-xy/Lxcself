import discord
from discord.ext import commands

# Replace with your token
TOKEN = 'YOUR_DISCORD_TOKEN'

# Create a bot instance
bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    """Respond with 'Pong!'"""
    await ctx.send('Pong!')

@bot.command()
async def echo(ctx, *, message: str):
    """Echo the message back to the user"""
    await ctx.send(message)

bot.run(TOKEN, bot=False)
