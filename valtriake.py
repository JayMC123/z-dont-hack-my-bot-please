import discord
import youtube_dl
from discord.ext import commands

TOKEN = 'NTI1ODE3NjU3NDU5NjA1NTA0.DwKHww.9uD4XuXFQcoSXoB2lG_t3I9V0wk'
client = commands.Bot(command_prefix = '.')

players = {}

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='24/7 music'))
    print('Bot is ready')

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()

@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()

client.run(TOKEN)
 
                      