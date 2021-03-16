import discord
import random

from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot(command_prefix='.')
status = cycle(['Online', 'Upgrading'])


@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.auther.voice.voice_channel
    await bot.join_voice_channel(channel)


bot.command(pass_context=True)


async def leave(ctx):
    server = ctx.message.server
    voice_client = bot.voice_client_in(server)
    await voice_client.disconnect()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required arguments')


@bot.event
async def on_ready():
    change_status.start()
    print('bot is online')


@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def owner_info(ctx):
    await ctx.send('The owner of this bad boi is Ross')


@bot.command()
async def ping(ctx):
    await ctx.send(f"pong {round(bot.latency * 1000)}ms")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@bot.command()
async def find(ctx):
    await ctx.send("find")  # for using google search later on !


@bot.command()
async def lol(ctx):
    await ctx.send('https://www.youtube.com/watch?v=QxnY2SWZTvk')


@bot.command()
async def simp(ctx):
    await ctx.send('hahahahah hayden is a simp')


@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain',
                 'It is decidedly so',
                 'Without a doubt',
                 'Yes – definitely',
                 'You may rely on it',
                 'As I see it, yes',
                 'Most likely',
                 'Outlook good',
                 'Yes Signs point to yes.',
                 'Reply hazy try again',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Concentrate and ask again.',
                 'Dont count on it',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.', ]
    await ctx.send(f'question: {question}\nanswer:{random.choice(responses)}')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send('Error please try again or .help for commands list.')


@bot.event
async def on_member_join(member):
    print(f'{member} has joined the server.')


@bot.event
async def on_member_remove(member):
    print(f'{member} has left the server.')


bot.run('')
