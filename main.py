# bot.py
import os
import requests
import json
import discord
from dotenv import load_dotenv
from discord.ext import tasks, commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(".")

quotes_channel = 812474792103903283
tasks_channel = 812474792103903282

def get_quote():
    response = requests.get\
    ("https://zenquotes.io/api/random")
    json_represenation = json.loads(response.text)
    quote = json_represenation[0]['q'] + " -" + json_represenation[0]['a']
    return quote

@client.event
async def on_ready():
    print('Bot is ready.')

#@client.event
#async def on_message2(message):
#    if message.author == client.user:
#        await message.add_reaction('✅')

@client.event
async def on_message(message):
    if message.author == client.user:
        await message.add_reaction('✅')
        return
    if message.content.startswith('T:'):
        await client.get_channel(tasks_channel).send('%s' % message.content)
    elif message.content.startswith('*inspire'):
        quote = get_quote()
        await client.get_channel(quotes_channel).send(quote)

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
    channel = reaction.message.channel
    msg_id = reaction.message.id

    if reaction.emoji == '✅':
        msg = await channel.fetch_message(msg_id)
        await msg.edit(content="~~%s~~" % msg.content)

@client.event
async def on_reaction_remove(reaction, user):
    if user == client.user:
        return
    channel = reaction.message.channel
    msg_id = reaction.message.id

    if reaction.emoji == '✅':
        msg = await channel.fetch_message(msg_id)
        await msg.edit(content="%s" % msg.content.replace('~~', '' ))

client.load_extension('cogs.DailyQuotesCog')
client.run(TOKEN)
