import discord

class MyClient(discord.Client):
    async def on_ready(self):
      print('We have logged on as {0}!'.format(self.user))

    async def on_message(self, message):
      
      message_string = message.content

      if message.author == client.user:
        return
      else:
        pass

      if message.content.startswith('{max}'):
        message_data = message_string.split("} ")
        message_text = message_data[1]
        channel = client.get_channel(853146237255286814)
        await channel.send(message_text)


client = MyClient()
client.run('ODUzMzUwNjgyOTQ1NTE5NjE3.YMUGwQ.mz-8-6luJU40Hkq7mvo9tot1wOc')
