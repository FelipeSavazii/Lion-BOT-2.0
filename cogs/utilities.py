import discord
from discord import app_commands, ui
from discord.ext import commands
from datetime import datetime
import asyncio
import aiohttp
from urllib.parse import quote

TOKEN = "cf357b1c5a39cd0af418007663f9ada3"

class Utilities(commands.Cog, name="utilities"):
    def __init__(self, bot):
        self.bot = bot

    usuário = app_commands.Group(name="usuário", description="Veja as informações de um usuário.")
    servidor = app_commands.Group(name="servidor", description="Veja as informações de um servidor.")

    @usuário.command(
        name="avatar",
        description="Veja o avatar de um usuário.",

    )
    async def usuário_avatar(self, interaction: discord.Interaction, usuário: discord.User = None):
        if usuário:
            pass
        else:
            usuário = interaction.user
        if usuário.avatar:
            embed = discord.Embed(
                description=f"Avatar de {usuário.name}:",
                color=0x7900ff,
            )
            if interaction.user.display_name == usuário.name:
                embed.set_footer(text=f"Quanto amor próprio, você ama se ver...")
            else:
                embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Avatar de usuário - Lion BOT", icon_url=self.bot.user.avatar.url)
            embed.set_image(url=usuário.avatar.url)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                description=f"Avatar de {usuário.name} não disponível.",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Avatar de usuário - Lion BOT", icon_url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)

    @usuário.command(
        name="banner",
        description="Veja o banner de um usuário.",
    )
    async def usuário_banner(self, interaction: discord.Interaction, usuário: discord.User = None):
        if usuário:
            pass
        else:
            usuário = interaction.user
        usuário = await self.bot.fetch_user(usuário.id)
        if usuário.banner:
            embed = discord.Embed(
                description=f"Banner de {usuário.name}:",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Banner de usuário - Lion BOT", icon_url=self.bot.user.avatar.url)
            embed.set_image(url=usuário.banner.url)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                description=f"Banner de {usuário.name} não disponível.",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Banner de usuário - Lion BOT", icon_url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)

    @usuário.command(
        name="info",
        description="Veja as informações de um usuário.",
    )
    async def usuário_info(self, interaction: discord.Interaction, usuário: discord.User = None):
        if usuário:
            pass
        else:
            usuário = interaction.user

        created_at = usuário.created_at
        unix_timestamp = int(created_at.timestamp())

        badges = []

        for flag in usuário.public_flags.all():
            if flag == discord.UserFlags.staff:
                badges.append("<:StaffBadge:1188007097443557376>")
            if flag == discord.UserFlags.partner:
                badges.append("<a:PartnerBadge:1188007447089139763>")
            if flag == discord.UserFlags.bug_hunter:
                badges.append("<:BugHunter:1188007743483813889>")
            if flag == discord.UserFlags.bug_hunter_level_2:
                badges.append("<:GoldBugHunter:1188007966780166164>")
            if flag == discord.UserFlags.hypesquad_balance:
                badges.append("<:BalanceBadge:1188008845176484002>")
            if flag == discord.UserFlags.hypesquad_bravery:
                badges.append("<:BraveryBadge:1188008848561295401>")
            if flag == discord.UserFlags.hypesquad_brilliance:
                badges.append("<:BrillianceBadge:1188008850490662932>")
            if flag == discord.UserFlags.hypesquad:
                badges.append("<:HypeEventsBadge:1188008852692668417>")
            if flag == discord.UserFlags.early_supporter:
                badges.append("<:EarlySupporterBadge:1188009969140908152>")
            if flag == discord.UserFlags.verified_bot_developer:
                badges.append("<:EarlyDevBadge:1188009966993420358>")
            if flag == discord.UserFlags.discord_certified_moderator:
                badges.append("<:AlumniModBadge:1188010670101364808>")
            if flag == discord.UserFlags.active_developer:
                badges.append("<:ActiveDeveloperBadge:1188010667664474164>")

        if usuário.premium_since != None:
            badges.append("<:NitroBadge:1188013024825581619>")

        badges_text = ' '.join(badges)

        embed = discord.Embed(
            description=f"**{usuário.name}** {badges_text}",
            color=0x7900ff,
        )
        embed.add_field(name="Nome", value=f"```{usuário.name}```")
        embed.add_field(name="ID do usuário", value=f"```{usuário.id}```")
        embed.add_field(name="Menção", value=f"{usuário.mention}")
        embed.add_field(name="Conta criada em", value=f"<t:{unix_timestamp}> (<t:{unix_timestamp}:R>)")
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Informações de usuário - Lion BOT", icon_url=self.bot.user.avatar.url)
        if usuário.avatar:
            embed.set_thumbnail(url=usuário.avatar.url)
        await interaction.response.send_message(embed=embed)
      
    @servidor.command(
        name="ícone",
        description="Veja o ícone de um servidor.",

    )
    async def servidor_ícone(self, interaction: discord.Interaction, servidor: str = None):
        if servidor:
            try:
                servidor = self.bot.get_guild(int(servidor))
                if servidor == None:
                    raise Exception
            except:
                embed = discord.Embed(
                    description=f"Servidor não encontrado.",
                    color=0x7900ff,
                )
                embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
                embed.set_author(name="Banner de servidor - Lion BOT", icon_url=self.bot.user.avatar.url)
                await interaction.response.send_message(embed=embed)
                return 
        else:
            servidor = interaction.guild
        if servidor.icon:
            embed = discord.Embed(
                description=f"Ícone de {servidor.name}:",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Ícone do Lion BOT", icon_url=self.bot.user.avatar.url)
            embed.set_image(url=servidor.icon.url)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                description=f"Avatar de {servidor.name} não disponível.",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Ícone do Lion BOT", icon_url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)

    @servidor.command(
        name="banner",
        description="Veja o banner de um servidor.",
    )
    async def servidor_banner(self, interaction: discord.Interaction, servidor: str = None):
        if servidor:
            try:
                servidor = self.bot.get_guild(int(servidor))
                if servidor == None:
                    raise Exception
            except:
                embed = discord.Embed(
                    description=f"Servidor não encontrado.",
                    color=0x7900ff,
                )
                embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
                embed.set_author(name="Ícone de servidor - Lion BOT", icon_url=self.bot.user.avatar.url)
                await interaction.response.send_message(embed=embed)
                return 
        else:
            servidor = interaction.guild
        if servidor.banner:
            embed = discord.Embed(
                description=f"Banner de {servidor.name}:",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Banner do Lion BOT", icon_url=self.bot.user.avatar.url)
            embed.set_image(url=servidor.banner.url)
            await interaction.response.send_message(embed=embed)
        else:
            embed = discord.Embed(
                description=f"Banner de {servidor.name} não disponível.",
                color=0x7900ff,
            )
            embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
            embed.set_author(name="Banner de servidor - Lion BOT", icon_url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed)

    @servidor.command(
        name="info",
        description="Veja as informações de um servidor.",
    )
    async def servidor_info(self, interaction: discord.Interaction, servidor: str = None):
        if servidor:
            try:
                servidor = self.bot.get_guild(int(servidor))
                if servidor == None:
                    raise Exception
            except:
                embed = discord.Embed(
                    description=f"Servidor não encontrado.",
                    color=0x7900ff,
                )
                embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
                embed.set_author(name="Informações de servidor - Lion BOT", icon_url=self.bot.user.avatar.url)
                await interaction.response.send_message(embed=embed)
                return 
        else:
            servidor = interaction.guild
        created_at = servidor.created_at
        unix_timestamp = int(created_at.timestamp())
        channels = len(servidor.channels)
        text_channels = len(servidor.text_channels)
        voice_channels = len(servidor.voice_channels)
        categories = len(servidor.categories)

        roles = []
        emojis = []

        for role in servidor.roles:
            roles.append(f"<@&{role.id}>")

        roles_text = ' '.join(roles)

        for emoji in servidor.emojis:
            if emoji.animated:
                emojis.append(f"<a:{emoji.name}:{emoji.id}>")
            else:
                emojis.append(f"<:{emoji.name}:{emoji.id}>")

        emojis_text = ' '.join(emojis)

        embed = discord.Embed(
            description=f"**{servidor.name}**",
            color=0x7900ff,
        )
        embed.add_field(name="Nome", value=f"```{servidor.name}```")
        embed.add_field(name="ID do servidor", value=f"```{servidor.id}```")
        embed.add_field(name="Canais", value=f"Categorias: {categories}\nTexto: {text_channels}\nVoz: {voice_channels}\n**Total:** {channels}")
        embed.add_field(name="Servidor criado em", value=f"<t:{unix_timestamp}> (<t:{unix_timestamp}:R>)")
        embed.add_field(name="Emojis", value=emojis_text)
        embed.add_field(name="Cargos", value=roles_text, inline=False)
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Informações de servidor - Lion BOT", icon_url=self.bot.user.avatar.url)
        if servidor.icon:
            embed.set_thumbnail(url=servidor.icon.url)
        if servidor.banner:
            embed.set_image(url=servidor.banner.url)
        await interaction.response.send_message(embed=embed)

    @app_commands.command(
        name="contador",
        description="Ative um contador (em segundos).",
    )
    async def contador(self, interaction: discord.Interaction, tempo: int):
        embed = discord.Embed(
            description=f"Iniciando a contagem...",
            color=0x7900ff,
        )
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Contador - Lion BOT", icon_url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(1.0)
        for i in range(0, tempo):
            embed.description=f"{tempo-i}..."
            await interaction.edit_original_response(embed=embed)
            await asyncio.sleep(1.0)
        embed.description=f"Contador encerrado."
        await interaction.edit_original_response(embed=embed)

    @app_commands.command(
      name="wiki",
      description="Pesquise algo na Wikipédia.",
    )
    async def wiki(self, interaction: discord.Interaction, pesquisa: str):
      embed = discord.Embed(
        description=f"Aguarde...",
        color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Ping - Lion BOT", icon_url=self.bot.user.avatar.url)
      await interaction.response.send_message(embed=embed)
      
      link = f"https://pt.wikipedia.org/w/index.php?search={pesquisa.replace(' ', '+')}&title=Especial%3APesquisar&ns0=1"
      encoded_link = quote(link, safe=':/?=&')
      url = f"https://api.screenshotapi.io/capture?token={TOKEN}&url={encoded_link}"
      print(url)
      print(link)
      print(endocoded_link)
      
      async with aiohttp.ClientSession() as session:
          async with session.get(url) as response:
              response.raise_for_status()

              data = await response.read()
              print(data)
        
      embed.description=f"['{pesquisa}' na Wikipédia]({link})"
      await interaction.edit_original_response(embed=embed)

async def setup(bot):
    await bot.add_cog(Utilities(bot))