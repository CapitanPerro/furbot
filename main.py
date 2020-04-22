import discord

from discord.ext import commands
bot = commands.Bot(command_prefix='=', description='a simple test bot')


@bot.event
async def on_ready():
    activity = discord.Game(name="with tennis balls | =help", type=2)
    await bot.change_presence(status=discord.Status.dnd, activity=activity)
    print("Toothless is ready ^-^")
    print(f"Toothless is currently in {len(bot.guilds)} guilds")
    print('Bot has started successfully')

@bot.command(name="ping", aliases=["latency"], brief="Shows latency from bot!")
async def greet_back_command(ctx):
    await ctx.send(f"bot ping: **{'{:.2f}'.format(bot.latency)}**ms")

@bot.command(name="invite", aliases=["inv"], brief="Shows the bot's oauth link")
async def greet_back_command(ctx):
    await ctx.send(f"invite link: __**https://discordapp.com/api/oauth2/authorize?client_id=620990340630970425&permissions=8&scope=bot**__")

@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")
async def greet_back_command(ctx):
	embed=discord.Embed(title="Statistics Toothless:", description="Global Bot Statistics", color=0x00ff00)
	embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
	embed.add_field(name="Total users", value=len(bot.users), inline=False)
	embed.add_field(name="More:", value="Coming soon...", inline=False)
	await ctx.send(embed=embed)

bot.run("NjIwOTkwMzQwNjMwOTcwNDI1.Xp9PAg.VmsaQQaYAxglQ83I8Bv8sSFSWG4")