import discord
import random
import time
from discord.ext import commands

TOKEN = 'NTI3NTUzNDIzMjk4NTI3MjMz.DwVaRQ.gYCFjsXb6t-YduumsbEH5HK4fak'

client = commands.Bot(command_prefix = 'a!')
client.remove_command('help')

@client.event
async def on_ready():
    serverCount = len(client.servers)
    await client.change_presence(game=discord.Game(name='{} servers | a!help | version demo'.format(serverCount), type = 2, status=discord.Status.dnd))
    print('Hello')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='-Gamers-')
    await client.add_roles(member, role)

@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
@client.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name="{}'s info".format(ctx.message.server.name))
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Server Owner", value=(ctx.message.server.owner))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="Region", value=ctx.message.server.region, inline=True)
    embed.add_field(name="Server Created", value=ctx.message.server.created_at, inline=True)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level, inline=True)
    embed.add_field(name="Is Server Large", value=ctx.message.server.large, inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)
    
@client.command(pass_context=True)
async def flipcoin(ctx):
      await client.say(random.choice(['heads!', 'Tails!']))
    
@client.command(pass_context=True)
async def kick(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.kick_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.kick(user)
            embed = discord.Embed(description=f":white_check_mark:  Sucessfuly kicked **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing KICK_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ban(ctx, user: discord.Member = None):
    try:
        if ctx.message.author.server_permissions.ban_members:
            if user is None:
                embed = discord.Embed(description=":no_entry_sign: **You forgot a user!**", color=(random.randint(0, 0xffffff)))
                await client.say(embed=embed)
                return
            await client.ban(user)
            embed = discord.Embed(description=f":check: Sucessfuly banned **{user}**!", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
        else:
            embed = discord.Embed(description=":error: **You are missing BAN_MEMBERS permission.**", color=(random.randint(0, 0xffffff)))
            await client.say(embed=embed)
    except discord.Forbidden:
        embed = discord.Embed(description=":error: **I am missing permissions to use this command!**", color=(random.randint(0, 0xffffff)))
        await client.say(embed=embed)    
        
@client.command(pass_context=True)
async def ping(ctx):
    t = await client.say('Pong!')
    ms = (t.timestamp-ctx.message.timestamp).total_seconds() * 1000
    await client.edit_message(t, new_content='Pong! Took: {}ms'.format(int(ms)))
    
@client.command(pass_context=True)
@commands.has_permissions(administrator=True, manage_messages=True)
async def clear(ctx, amount=100):
    """Clear the specified number of messages, default 100 messages."""
    channel = ctx.message.channel
    messages = []
    amount = int(amount) + 1
    async for message in cleintt.logs_from(channel, limit=amount):
        messages.append(message)
    await bot.delete_messages(messages)
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await client.send_message(ctx.message.channel, "You do not have permission to use that command.".format(ctx.message.author.mention))
        
@client.command(pass_context=True)
async def say(ctx,*msg):
	user_msg=ctx.message
	await client.say('{}'.format(' '.join(msg)))
	await asyncio.sleep()
	await client.delete_message(user_msg)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.green()
    )

    embed.set_author(name='Help | prefix = a!')
    embed.add_field(name='Common Commands', value='a!help <shows his message> a!invite <link to invite me>', inline=False)
    embed.add_field(name=':tools: Moderation Commands', value='a!kick <user> a!ban <user> a!clear <number of msg> a!userinfo <shows info on a user>', inline=False)
    embed.add_field(name=':smiley: Fun Commands', value='a!ping <returns pong> a!!say <what u want it to say> a!flipcoin <random coin>', inline=False)
    embed.add_field(name=':page_facing_up: Info', value='a!info <shows my information> a!serverinfo <servers info>', inline=False)
    embed.add_field(name='Info', value='Created By Naruto Uzumaki#0001',inline=False)

    await client.send_message(author, embed=embed)
    await client.say('Check your dms.')
    
@client.command(pass_context=True)
async def invite(ctx):
	await client.say('Here is an invite link https://discordapp.com/oauth2/authorize?client_id=527553423298527233&permissions=8&scope=bot')
	
@client.command(pass_context=True)
async def info(ctx):
	await client.say('I was created on Monday December 7th 2018')
	await client.say('Made at DiscordBot.py')
	
@client.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
	await client.say('Name is: {}'.format(user.name))
	await client.say('User ID: {}'.format(user.id))
	await client.say('User Status: {}'.format(user.status))
	await client.say('High Rank: {}'.format(user.top_role))
	await client.say('Joined at: {}'.format(user.joined_at))
    
client.run(TOKEN)
