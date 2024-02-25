import asyncio
import platform, os
import logging, random
from dotenv import load_dotenv

import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

from modules.loggingformatter import LoggingFormatter, logger
# from cogs.general import Ajuda

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True

bot = Bot(
    command_prefix=commands.when_mentioned_or("/"),
    intents=intents,
    help_command=None,
)
bot.logger = logger

load_dotenv()
token = os.getenv("TOKEN")

@bot.event
async def on_ready():
    bot.logger.info(f"Logado como {bot.user.name}")
    bot.logger.info(f"Versão do discord.py: {discord.__version__}")
    bot.logger.info(f"Versão do Python: {platform.python_version()}")
    bot.logger.info(f"Rodando em: {platform.system()} {platform.release()} ({os.name})")
    bot.logger.info(len(f"Rodando em: {platform.system()} {platform.release()} ({os.name})") * "-")
    bot.logger.info("Sincronizando comandos globalmente...")
    await bot.tree.sync()
    statuses.start()

# @bot.event
# async def setup_hook():
#    bot.add_view(TESTE())

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        embed = discord.Embed(
            description=f"O Lion BOT funciona somente com slash commands (/). Use `/ajuda` e veja mais sobre mim.",
            color=0x7900ff,
        )
        embed.set_footer(text=f"Mencionado  por {message.author.display_name}.")
        embed.set_author(name="Olá, eu sou o Lion BOT", icon_url=bot.user.avatar.url)
        await message.channel.send(embed=embed)

@tasks.loop(minutes=1.0)
async def statuses():
    choice = random.randint(1, 2)
    guilds = len(bot.guilds)
    members = 0
    for guild in bot.guilds:
        members += guild.member_count
    if choice == 1:
            statuses = [f"{guilds} servidores me usarem"]
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(statuses)))
    elif choice == 2:
            statuses = [f"{members} usuários cantarem"]
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(statuses)))

async def cogs():
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"cogs.{extension}")
                bot.logger.info(f"Extensão '{extension}' carregada")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                bot.logger.error(f"Erro ao carregar as extensões {extension}\n{exception}")
    for file in os.listdir(f"{os.path.realpath(os.path.dirname(__file__))}/libs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                await bot.load_extension(f"libs.{extension}")
                bot.logger.info(f"Configuração '{extension}' carregada")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                bot.logger.error(f"Erro ao carregar as configurações {extension}\n{exception}")

asyncio.run(cogs())
bot.run(token=token)