# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()


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
        await message.channel.send('%s' % message.content)

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


client.run(TOKEN)
