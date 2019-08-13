## Benjamin Chappell ##

import discord

client = discord.Client()

TOKEN = NjEwNjE2MDE3NzA1NzYyODI2.XVH6LA.wfrk4P3y9GZ78p6a99_YtPTuvAo


@client.event
async def on_ready():
    print ("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "Hello":
        await client.send_message(message.channel, "World")

    
client.run(TOKEN)