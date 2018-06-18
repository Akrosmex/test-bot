import discord
import asyncio
import sqlite3

from discord.ext import commands
import random

des = 'Real af boi'
prefix = '='

bot = commands.Bot(command_prefix=prefix, description=des)

@bot.event
async def on_event():
    print('Logged on as: ')
    print(bot.user.id)

@bot.event

async def on_message(message):
    server = message.server
    if "kawaii" in message.author.display_name.lower():
        await bot.delete_message(message)
    else:
        if "+neko" in message.content.lower():
            await bot.send_message(message.channel, "https://cdn.nekos.life/neko/neko_288.jpg")



async def on_message(message):
    server = message.server
    #bot ignores it's and other bots' messages
    if message.author == bot.user:
        return
    if message.author.bot:
        return


    if "gay" in message.content.lower():
        msg = "no u".format(message)
        if "gaybriel" in message.author.display_name.lower() or "quinn" in message.author.display_name.lower():
            pass
        else:
            await bot.add_reaction(message, '\U0001F1F0')
            await bot.add_reaction(message, '\U0001F1FE')
            await bot.add_reaction(message, '\U0001F1F8')
            for i in range(0, 4):
                await bot.send_message(message.channel, msg)

    if "timmy" in message.content.lower():
        await bot.add_reaction(message, '\U0001F1F0')
        await bot.add_reaction(message, '\U0001F1FE')
        await bot.add_reaction(message, '\U0001F1F8')
        id = "@everyone"
        await bot.send_message(message.channel, "{0} don't forget to subscribe to <https://www.twitch.tv/playeronetimmy> !!!".format(id))

    if " die" in message.content.lower():
        msg = "die".format(message)
        await bot.add_reaction(message, '\U0001F1F0')
        await bot.add_reaction(message, '\U0001F1FE')
        await bot.add_reaction(message, '\U0001F1F8')
        for i in range(0, 4):
            await bot.send_message(message.channel, msg)

    if "protag x luke" in message.content.lower():
        if "gaybriel" in message.author.display_name.lower() or "quinn" in message.author.display_name.lower():
            pass
        else:
            msg = "protag x luke hot".format(message)
            await bot.add_reaction(message, '\U0001F1F0')
            await bot.add_reaction(message, '\U0001F1FE')
            await bot.add_reaction(message, '\U0001F1F8')
            for i in range(0, 30):
                await bot.send_message(message.channel, msg)

    if "" in message.content.lower():
        if "protag" in message.author.display_name.lower():
            myid = "<@310082674108923905>"
            await bot.send_message(message.channel, "die {0}".format(myid))
            await bot.add_reaction(message, '\U0001F1F0')
            await bot.add_reaction(message, '\U0001F1FE')
            await bot.add_reaction(message, '\U0001F1F8')
        else:
            if "hopetrash" in message.author.display_name.lower():
                myid = "<@324974677917171719>"
                await bot.send_message(message.channel, "die {0}".format(myid))
                await bot.add_reaction(message, '\U0001F1F0')
                await bot.add_reaction(message, '\U0001F1FE')
                await bot.add_reaction(message, '\U0001F1F8')

            else:
                if "gaybriel" in message.author.display_name.lower() or "quinn" in message.author.display_name.lower():
                    pass
                else:
                    if "yui" in message.author.display_name.lower() or "sigma" in message.author.display_name.lower():
                        await bot.delete_message(message)
                    else:
                        await bot.add_reaction(message, '\U0001F1F0')
                        await bot.add_reaction(message, '\U0001F1FE')
                        await bot.add_reaction(message, '\U0001F1F8')
    if "+neko" in message.content.lower():
        await bot.send_message(message.channel, "https://cdn.nekos.life/neko/neko_288.jpg")



@bot.command(pass_context = True)
async def send(self, *, ctx):
    await bot.say(ctx)
    await bot.delete_message(ctx.message)

@bot.command()
@commands.has_permissions(kick_members=True)
async def gay(ctx, userName: discord.Member):
    await bot.kick(userName)
    await bot.say("bye {0}".format(userName))

@bot.command()
async def status(*, game: str):
    await bot.change_presence(game=discord.Game(name=game))



bot.run('MzI1NzAzMzUyMjAzNzM5MTM2.DZWnyw.x6LZaTq9B2mPPQIqqjzIOdcm2mw')
