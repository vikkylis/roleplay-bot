import discord

YOUR_TOKEN = 'whatever it is' # copy over from your dev portal. Keep the ' on either side.
source_channel = 1234 # replace 1234 with the ID of the channel you want to control the bots from. e.g. 853100609884127256
rp_channel = 5678 # replace 5678 with the ID of the channel that you want the bot's messages to appear in.
chat_channel = 9012 # same

class MyClient(discord.Client):
    async def on_ready(self):
        print('We have logged on as {0}!'.format(self.user))

    async def on_message(self, message: discord.Message):
        message_string = message.content
        message_channel: discord.TextChannel = message.channel

        if message.author == client.user or not message_channel.id == source_channel:
            return
        else:
            pass

        if message.content.startswith('{max} {rp}'):
            message_data = message_string.split("} ")
            message_text = message_data[2]
            channel = client.get_channel(rp_channel)
            await channel.send(message_text)

        elif message.content.startswith('{max} {chat}'):
            message_data = message_string.split("} ")
            message_text = message_data[2]
            channel = client.get_channel(chat_channel)
            await channel.send(message_text)
            
        else:
            message_text = 'invalid command'
            channel = client.get_channel(source_channel)
            await channel.send(message_text)


client = MyClient()
client.run(YOUR_TOKEN)
