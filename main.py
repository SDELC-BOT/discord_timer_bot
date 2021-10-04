import discord
import os
import threading
import datetime
import time
from keep_alive import keep_alive
my_secret = os.environ['Token']

client = discord.Client()

# Function wrapper
def periodic_task(interval, times = -1):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            stop = threading.Event()
            def inner_wrap():
                i = 0
                while i != times and not stop.isSet():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
@periodic_task(10)
def my_periodic_task():
    # This function is executed every 3 hours
    await message.channel.send("I am executed at {}".format(datetime.datetime.now()))

# Call the function once to launch the periodic
print(my_periodic_task())

keep_alive()
client.run(my_secret)