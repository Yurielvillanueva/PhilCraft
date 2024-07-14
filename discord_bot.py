import discord
import heroku
import heroku
from discord.ext import commands

import json
import os

# Check if config.json exists, otherwise create a default template
if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": "", "Prefix": "!"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
prefix = configData["Prefix"]

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def helpst(ctx):
    user = ctx.author.mention
    staff_role = discord.utils.get(ctx.guild.roles, name="Staffs")  # Adjust the role name to match your server's staff role

    embed = discord.Embed(
        title='Helpstaffs',
        description=f'Dear {user},\n\nThank you for reaching out. We appreciate your patience and understanding. Our team is here to assist you with any issues you may have. Please let us know how we can help, and we will get back to you as soon as possible.\n\n{staff_role.mention}',
        color=discord.Color.green()
    )

    await ctx.send(embed=embed)

bot.run('MTI2MDk4MTIzMjg4ODQ1MTE4Mw.Gbz8ZX.6H1JI4X0kqXb3ophoCjexbZrLbEkqpcZcL3XyQ')