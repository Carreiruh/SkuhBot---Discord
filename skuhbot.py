import discord
import discord.client
import random
from discord.ext import commands

# Enter your bots custom token here
token = "Enter Your Token Here"

client = commands.Bot(command_prefix='!')

# Check if bot is running and print username of bot in terminal
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")

# 8Ball Function - ask a question and get a randomized response
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.',
                 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Dont count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'Bruh you crazy?']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

# Have bot say hello to user
@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("!hi"):
            await msg.channel.send(f"Hello, {msg.author.display_name}! You are looking very powerful and attractive today.")
    await client.process_commands(msg)

# Help Function - Provides users command inventory for the bot in channel
@client.command()
async def helpme(ctx):
    embed = discord.Embed(title = "----- Help Menu -----", description= '\n Current commands are:\n\n !8ball (Enter your question here without parenthesis) - Provides concrete reliable decision making guarenteed to work 100% of the time 20% of the time!\n\n !hi - Provides a nice hello message from the bot\n\n !poll (Poll topic here without parenthesis) - Call a vote in the current channel using emotes \n\n !coinflip - Flips a coin and spits out the randomized result\n\n'
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
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped a coin \n Result is: **Heads**!")
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped a coin\n Result is: **Tails**!")
        await ctx.send(embed=embed)

#Hydrate - Inform your homies that it's time to hydrate, with a counter implemented to help them remain focused! - Currently WIP
# counter = 0
# @client.command()
# async def hydrate(ctx, target:discord.Member = None):
#     global counter
#     if target == None:
#         await ctx.send("You didn't mention anyone!")
    
#     else:
#         await ctx.send(target.mention + " " + ctx.author.mention + " has reminded you to hydrate, do you accept? (y,n)")
#         def check(msg):
#             return msg.author == ctx.author and msg.channel == ctx.channel and \
#             msg.content.lower() in ["y", "n"]

#         msg = await client.wait_for("message", check=check)
#         if msg.content.lower() == "y":
#             counter += 1
#             await ctx.send("You have succesfully hydrated " + str(counter) + " time(s). Well done!")
#         elif msg.content.lower() == "n":
#             counter = 0
#             await ctx.send("You have failed sucessfully and reset the hydration counter. Very unfortunate")
#         else:
#             await ctx.send("Bzzzt Invalid Selection")


        


client.run(token)
