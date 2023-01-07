import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('бот заработал')

@client.event
async def on_message(message):
    if message.author == client.user:
            return
    if message.content.startswith('$привет'):
        await message.channel.send('Здарова!')

client.run('MTAzOTUwNDAxODU1ODQzNTMyOA.Gm9zW4.Iqd4ckk1-IqrVINFL0VBDQpvvgtxKDJAyC9d44')