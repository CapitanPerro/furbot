import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='=', description='a simple test bot')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)


@bot.command(name="ping", aliases=["latency"], brief="Shows latency from bot!")
async def greet_back_command(ctx):
    await ctx.send(f"bot ping: **{'{:.2f}'.format(bot.latency)}**ms")


bot.run('NjIwOTkwMzQwNjMwOTcwNDI1.XphJPw.eE4vpvudxp5M2He-ki-QSURq6xE')
