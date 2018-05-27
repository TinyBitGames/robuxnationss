import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
        print('Logged in as')
        print("Username: " + client.user.name)
        print("ID: " + client.user.id)
        print('------')
        
@client.event
async def on_message(message):
        if message.content.startswith('>ping'):
                await client.send_message(message.channel, 'Pong.')
        elif message.content.startswith('>youtube'):
                await client.send_message(message.channel, 'https://www.youtube.com/channel/UCwHx_8S2KxhRINpFCb_Htpg')
        elif message.content.startswith('>howtogetrobux'):
                await client.send_message(message.channel, '1st- Invite People. per every person you invite you get 1 robux and can redeem and minimum 5 invites. Each time you get robux from this method you get a +0.2x multiplier for the amount of robux you receive.')
        elif message.content.startswith('>help'):
                await client.send_message(message.channel, 'Check your DMs ;)')
                await client.send_message(message.author, '```>ping - Tests if the bot is running.```')
                await client.send_message(message.author, '```>youtube - The official youtube channel.```')
                await client.send_message(message.author, '```>howtogetrobux - How to get robux.```')
                await client.send_message(message.author, '```>rules - Shows the rules.```')
                await client.send_message(message.author, '```>creator - Shows creator of the bot.```')
        elif message.content.startswith('>rules'):
                await client.send_message(message.author, '```1. Do not spam (Warn then Mute for a day)```')
                await client.send_message(message.author, '```2. Do not swear (Warn then Mute for a day)```')
                await client.send_message(message.author, '```3. Do not show adult content (Kick)```')
                await client.send_message(message.author, '```4. Treat people how you want to be treated (Warn then Mute for a day)```')
                await client.send_message(message.author, '```5. Do not advertise your stuff without being a partner (Mute for a day)```')
                await client.send_message(message.author, '```6. Do not disrespect higher ranks (Mute for a day)```')
        elif message.content.startswith('>creator'):
                await client.send_message(message.channel, 'The creator of this bot is TinyBitGames.')
                
client.run(process.env.BOT_TOKEN)               
