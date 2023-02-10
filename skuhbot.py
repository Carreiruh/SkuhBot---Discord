import discord
import discord.client
import random
import asyncio
from discord.ext import commands

# Enter your bots custom token here
token = "Enter Your Token Here"

# Enable intents and define in developer portal to enable auto-role functionality
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)


# Check if bot is running and print username of bot in terminal
@client.event
async def on_ready():
    introart = """
 $$$$$$\  $$\                 $$\       $$$$$$$\             $$\     
$$  __$$\ $$ |                $$ |      $$  __$$\            $$ |    
$$ /  \__|$$ |  $$\ $$\   $$\ $$$$$$$\  $$ |  $$ | $$$$$$\ $$$$$$\   
\$$$$$$\  $$ | $$  |$$ |  $$ |$$  __$$\ $$$$$$$\ |$$  __$$\\_$$  _|  
 \____$$\ $$$$$$  / $$ |  $$ |$$ |  $$ |$$  __$$\ $$ /  $$ | $$ |    
$$\   $$ |$$  _$$<  $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | $$ |$$\ 
\$$$$$$  |$$ | \$$\ \$$$$$$  |$$ |  $$ |$$$$$$$  |\$$$$$$  | \$$$$  |
 \______/ \__|  \__| \______/ \__|  \__|\_______/  \______/   \____/ 
                                                                     
"""
    print(introart)                                
    print(f"Bot logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for directive"))

# 8Ball Function - ask a question and get a randomized response
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.',
                 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'Bruh you crazy?']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Have bot say hello to user
@client.command(name="hi")
async def greeting(ctx):
    await ctx.send(f"Hello {ctx.message.author.mention}! You are looking very powerful and attractive today.")

#Auto assigns guest role to users when invited to server
role = "Guest"
@client.event
async def on_member_join(member): 
    rank = discord.utils.get(member.guild.roles, name=role)
    await member.add_roles(rank)  

# Help Function - Provides users command inventory for the bot in channel
@client.command()
async def helpme(ctx):
    embed = discord.Embed(title="----- Help Menu -----", description='\n Current commands are:\n\n !8ball (Enter your question here without parenthesis) - Provides concrete reliable decision making guarenteed to work 100% of the time 20% of the time!\n\n !hi - Provides a nice hello message from the bot\n\n !poll (Poll topic here without parenthesis) - Call a vote in the current channel using emotes \n\n !coinflip - Flips a coin and spits out the randomized result\n\n !hydrate - Prompt another user and remind them to drink water. Must enter the command followed by the @user'
                          )
    await ctx.send(embed=embed)


# Poll Function - call a vote with a user defined topic with results handled with emotes
@client.command()
async def poll(ctx, *, text: str):
    poll = await ctx.send("Current vote topic is: " + f"{text}")
    await poll.add_reaction("✅")
    await poll.add_reaction("❌")
    await poll.add_reaction("❓")

# Coin Flip - Random coin flip functionality
@client.command()
async def coinflip(ctx):
    cointoss_options = [0, 1]
    if random.choice(cointoss_options) == 1:
        embed = discord.Embed(
            title="Coinflip", description=f"{ctx.author.mention} Flipped a coin \n Result is: **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(
            title="Coinflip", description=f"{ctx.author.mention} Flipped a coin\n Result is: **Tails**!")
        await ctx.send(embed=embed)


#Hydration command to allow primary user to prompt secondary user to drink water
drinks_consumed = 0

@client.command(name="hydrate")
async def drink_water(ctx):
    global drinks_consumed
    author_user = ctx.message.author
    target_user = ctx.message.mentions[0] if len(ctx.message.mentions) > 0 else None
    if target_user is None:
        await ctx.send("You must declare another user to use this command. Ex: !hydrate @user")
        return
    msg = await ctx.send(f"{target_user.mention}, {author_user.mention} challenges you to drink water. Do you accept? (yes/no)")

    def check(x):
        return x.author == target_user and x.channel == ctx.message.channel

    try:
        response = await client.wait_for("message", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("You have taken too long and I have become bored - now exiting.")
        return

    if response.content.lower() == "yes":
        drinks_consumed += 1
        await ctx.send(f"You have hydrated {drinks_consumed} times!\nImpressive, {target_user.mention} Very nice.")
    elif response.content.lower() == "no":
        drinks_consumed = 0
        await ctx.send(f"You have failed successfully. Counter has been reset")
    else:
        await ctx.send("Invalid response. Please enter 'yes' or 'no'.")

client.run(token)