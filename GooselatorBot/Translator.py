import discord
import os
from discord.ext import commands

class CustomHelpCommand(commands.HelpCommand) :

    def __init__(self) :
        super().__init__()

    # !help
    async def send_bot_help(self, mapping) :
        file = discord.File("Translate.png")

        helps = ["About us - Team Goose : Yanny Patel, Krish Patel, Tom Croux and Tim Rozer"]
        embed = discord.Embed(title="Help", description="", color=discord.Color.orange())
        embed.set_footer(text = "Bot made with ❤️ by Team Goose") 
        embed.set_thumbnail(url = 'attachment://Translate.png')
        embed.set_author(name = "Translate", icon_url = 'attachment://Translate.png') 

        for i in range (len(helps)):
            embed.add_field(name=helps[i].split("- ")[0], value=helps[i].split("- ")[1], inline=True)
        
        await self.get_destination().send(file = file, embed=embed)

bot = commands.Bot(command_prefix = '&', help_command = CustomHelpCommand())

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs') :
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("Your Token")
