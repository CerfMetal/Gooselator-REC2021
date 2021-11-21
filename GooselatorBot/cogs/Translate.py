import discord
from discord.ext import commands
from googletrans import Translator
import os
from dotenv import load_dotenv


English = ['hello','water','morning','afternoon','evening','child','money','spirit','thanks','story','supper','farmer','hunter','program','history','mother','father','school','lunch','dinner']

Cree = ['tânisi','nîpîy','wapan','pôn-âpihtâ-kîsikâw','miyotakosin','nihtâwikihâkan','soniyaw','ahcâhk','ay','âcimowin','otâkwanimitisowin','okistikêw','omâcîw','kîkwayisihecikewin','ayamihcikêwikamik','okâwîmâw','ohtâwîmâw','âwatawâsiswâkan','nemâwin','âpihtâkîsikan']

Ojibway = ["gwekwe'",'waaboo','waaban','gii-ishkwaa-naawakweg','gabe-onaagosh','abinoojiinh','zhooniyaa','aadisookaan','miigwechiwitaagozi','babaamaajimowin','onaagoshi-wiisiniwin','gitige-inini','gaayosed','igewin','mewizhaizhi-bimaadiziwin','oga','weyoosimind','gikinaamaadinaan','miijiwin','wiisini']

Mohawk = ['sekoh','ohné:ka','ohron’kéhstsi’','iotohétstonnénkie','o’karasnéhanonkwá:ti','eksá:’a','ohwíhsta','atóhnhets','niawenhkó:wa','oká:ra','okara’snéhai','raién:thos','rató:rats','tyataterakwén:nis','raonawirà:ke','iakoiá:ner','rake’níha','tsiionterihwaienhstáhkwa','énkie','teyontska’hónhkwa']

class Translate(commands.Cog):
    # Reference to the client from the main file
    def __init__(self, client):
        self.client = client

    # Run at start
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online")

    # Read all messages
    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages coming from the bot
        if message.author == self.client.user :
            return

        msg = message.content

        if msg in Cree :
            await message.channel.send(f"`{message.author.name}:`  {English[Cree.index(msg)]}        *{msg}*")
            await message.delete()

        elif msg in Ojibway :
            await message.channel.send(f"`{message.author.name}:`. {English[Ojibway.index(msg)]}        *{msg}*")
            await message.delete()

        elif msg in Mohawk :
            await message.channel.send(f"`{message.author.name}:`  {English[Mohawk.index(msg)]}        *{msg}*")
            await message.delete()


# Function to connect this file to the bot
def setup(client):
    client.add_cog(Translate(client)) 
