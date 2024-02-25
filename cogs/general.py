import discord
from discord import app_commands, ui
from discord.ext import commands
from datetime import datetime
import asyncio

class Ajuda(discord.ui.View):
  def __init__(self):
      super().__init__()

      self.add_item(discord.ui.Button(label='Lista de comandos', url="https://lionbot.felipesavazi.com/comandos"))
      self.add_item(discord.ui.Button(label='Normas e diretrizes', url="https://lionbot.felipesavazi.com/normas-e-diretrizes"))
      self.add_item(discord.ui.Button(label='Dashboard', url="https://lionbot.felipesavazi.com/dashboard"))
      self.add_item(discord.ui.Button(label='Discord oficial', url="https://lionbot.felipesavazi.com/discord"))

class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    lion = app_commands.Group(name="lion", description="Vejas as informações do Lion BOT.")

    @app_commands.command(
        name="ajuda",
        description="Aprenda mais sobre o BOT.",
    )
    async def ajuda(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description=f"Descubra mais sobre o Lion BOT aqui.\n\nCom funcionalidades **diversas** e **muitas utilidades**, o {self.bot.user.mention} é um **BOT completo** que supre as necessidades de um servidor, deixando-o mais **dinâmico e interativo** em seus mínimos detalhes.\n\nSelecione uma opção abaixo para saber mais sobre mim.",
            color=0x7900ff,
        )
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Ajuda - Lion BOT", icon_url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, view=Ajuda())

    @lion.command(
        name="avatar",
        description="Veja o avatar do BOT.",
    )
    async def avatar(self, interaction: discord.Interaction):
      embed = discord.Embed(
        description=f"Avatar do {self.bot.user.display_name}:",
        color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Avatar - Lion BOT", icon_url=self.bot.user.avatar.url)
      embed.set_image(url=self.bot.user.avatar.url)
      await interaction.response.send_message(embed=embed)

    @lion.command(
        name="info",
        description="Veja as informações do BOT.",
    )
    async def info(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description=f"""
Olá, {interaction.user.mention}. Eu sou o Lion BOT, uma recém-criada aplicação, e estou atualmente ajudando {len(self.bot.guilds)} servidores. Tenho {len(self.bot.commands)} comandos e {len(self.bot.users)} usuários, e estou sempre à sua disposição.

**Informações:**

- Criado em: <t:1703269860:d> (<t:1703269860:R>)
- Criador: [Felipe Savazi](https://felipesavazi.com)
- Suporte: Bruno Guedes
- Linguagem: [Python](https://python.org)
- Biblioteca: [discord.py](https://discordpy.readthedocs.io/en/stable/)
- Hospedagem: [Replit](https://replit.com)
- Versão: [1.0.0x](https://lionbot.felipesavazi.com/versao/1.0.0x)
            """,
            color=0x7900ff,
        )
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Informações - Lion BOT", icon_url=self.bot.user.avatar.url)
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed, view=Ajuda())

    @lion.command(
      name="ping",
      description="Cheque a latência da BOT.",
    )
    async def ping(self, interaction: discord.Interaction):
      embed = discord.Embed(
          description=f"Latência da API: `{round(self.bot.latency * 1000)}ms`.",
          color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Ping - Lion BOT", icon_url=self.bot.user.avatar.url)
      await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))