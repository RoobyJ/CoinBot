import time
import discord
import logging
from DBCommands import DataManager
from discord.ext.commands import Bot, Command
from datetime import datetime

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
client = Bot(command_prefix='&')

# here place your token


@client.command(pass_context=True)
async def refreshuserlist(ctx):
    user_list = DataManager().get_data(ctx.message.guild.id, 'user_id')
    for user in ctx.message.guild.members:
        if user.id not in user_list:
            DataManager().data_entry(ctx.message.guild.id, user.id)


@client.command(pass_context=True)
async def shop(ctx):
    await ctx.message.channel.send("""
&subscription7
&subscription30
    """)


@client.command(pass_context=True)
async def coins(ctx):
    await ctx.message.channel.send('you have: ' +
                                   str(DataManager().get_data(ctx.message.guild.id,
                                                              'coins', user_id=ctx.message.author.id)[0][0]) + ' coins')


@client.command(pass_context=True)
async def sendcoins(ctx):
    pass


@client.command(pass_context=True)
async def subscription(ctx):
    pass


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# record all messages in the chats
@client.event
async def on_message(message):
    # print(f"{datetime.now()}: {message.channel}: {message.author}: {message.author.name}: {message.content}\n")
    try:
        with open('/coinbotdata/chatlogs.txt', 'a') as f:
            f.write(f"{datetime.now()}: {message.guild}: {message.channel}: {message.author}: "
                    f"{message.author.name}: {message.content}\n")
    except:
        pass
    await client.process_commands(message)


@client.event
async def on_member_join(message):
    user_list = DataManager().get_data(message.guild.id, 'user_id')
    for user in message.guild.members:
        if user.id not in user_list:
            DataManager().data_entry(message.guild.id, user.id)


client.run(token)
Command(refreshuserlist(), hidden=True)
Command(coins(), brief='Displays your actual amount of coins')
Command(shop(), brief='Displays your actual shop offer')
Command(sendcoins(), brief='Enables to send someone coins')
Command(subscription(), brief='Displays time to expire of your subscription')
# this is just a comment
