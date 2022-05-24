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

# Help Function - Provides users command inventory for bot in a private DM
@client.command()
async def helpme(ctx):
    await ctx.author.send('\t\t----------------- Help Menu -----------------\n Current commands are:\n !8ball (Enter your question here without parenthesis) - Provides concrete reliable decision making guarenteed to work 100% of the time 20% of the time!\n !hi - Provides a nice hello message from the bot\n !poll (Poll topic here without parenthesis) - Call a vote in the current channel using emotes'
    )


# Poll Function - call a vote with a user defined topic with results handled with emotes
@client.command()
async def poll(ctx, *, text: str):
    poll = await ctx.send("Current vote topic is: " + f"{text}")
    await poll.add_reaction("✅")
    await poll.add_reaction("❌")
    await poll.add_reaction("❓")


client.run(token)
