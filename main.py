import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='=', description='a simple test bot')


@bot.event
async def on_ready():
    print(f"Toothless is currently in {len(bot.guilds)} guilds")
    print('bot has started successfully')

@bot.command(name="ping", aliases=["latency"], brief="Shows latency from bot!")
async def greet_back_command(ctx):
    await ctx.send(f"bot ping: **{'{:.2f}'.format(bot.latency)}**ms")

@bot.command(name="invite", aliases=["inv"], brief="Shows the bot's oauth link")
async def greet_back_command(ctx):
    await ctx.send(f"invite link: __**https://discordapp.com/api/oauth2/authorize?client_id=620990340630970425&permissions=8&scope=bot**__")

bot.run('NjIwOTkwMzQwNjMwOTcwNDI1.XphJPw.eE4vpvudxp5M2He-ki-QSURq6xE')