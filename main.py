import discord
import os
import threading
import datetime
import time
from keep_alive import keep_alive
my_secret = os.environ['Token']

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

keep_alive()
client.run(my_secret)