import discord
from discord import app_commands, ui
from discord.ext import commands
from datetime import datetime
import asyncio
import aiohttp
from PIL import Image
from io import BytesIO
import os

async def GenImage(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
        response.raise_for_status()

        data = await response.read()
        img = Image.open(BytesIO(data))
      
        return img

class Utilities(commands.Cog, name="utilities"):
    def __init__(self, bot):
        self.bot = bot

    usuário = app_commands.Group(name="usuário", description="Veja as informações de um usuário.")
    servidor = app_commands.Group(name="servidor", description="Veja as informações de um servidor.")
    pesquisar = app_commands.Group(name="pesquisar", description="Pesquise em sites famosos.")

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

    @pesquisar.command(
      name="wiki",
      description="Pesquise algo na Wikipédia.",
    )
    async def wiki(self, interaction: discord.Interaction, pesquisa: str):
      await interaction.response.defer()
      
      link = f"https://pt.wikipedia.org/w/index.php?search={pesquisa.replace(' ', '+')}&title=Especial%3APesquisar&ns0=1"
      url = f"https://image.thum.io/get/{link}"

      img = await GenImage(url)
      img.save(f'./media/wiki/{interaction.user.id}.png')

      embed = discord.Embed(
        description=f"['{pesquisa}' na Wikipédia]({link})",
        color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Pesquisar na Wikipédia - Lion BOT", icon_url=self.bot.user.avatar.url)
      try:
        file = discord.File(f"./media/wiki/{interaction.user.id}.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await interaction.followup.send(file=file, embed=embed)
      except:
        await interaction.followup.send(embed=embed)

      os.remove(f"./media/wiki/{interaction.user.id}.png")

    @pesquisar.command(
      name="google",
      description="Pesquise algo no Google.",
    )
    async def google(self, interaction: discord.Interaction, pesquisa: str):
      await interaction.response.defer()
    
      link = f"https://www.google.com/search?client=&q={pesquisa.replace(' ', '+')}&sourceid=&ie=UTF-8&oe=UTF-8"
      url = f"https://image.thum.io/get/{link}"
    
      img = await GenImage(url)
      img.save(f'./media/google/{interaction.user.id}.png')
    
      embed = discord.Embed(
        description=f"['{pesquisa}' no Google]({link})",
        color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Pesquisar no Google - Lion BOT", icon_url=self.bot.user.avatar.url)
      try:
        file = discord.File(f"./media/google/{interaction.user.id}.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await interaction.followup.send(file=file, embed=embed)
      except:
        await interaction.followup.send(embed=embed)
      
      os.remove(f"./media/google/{interaction.user.id}.png")

    @pesquisar.command(
      name="youtube",
      description="Pesquise algo no YouTube.",
    )
    async def youtube(self, interaction: discord.Interaction, pesquisa: str):
      await interaction.response.defer()
    
      link = f"https://www.youtube.com/results?search_query={pesquisa.replace(' ', '+')}"
      url = f"https://image.thum.io/get/{link}"
    
      img = await GenImage(url)
      img.save(f'./media/youtube/{interaction.user.id}.png')
    
      embed = discord.Embed(
        description=f"['{pesquisa}' no YouTube]({link})",
        color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Pesquisar no YouTube - Lion BOT", icon_url=self.bot.user.avatar.url)
      try:
        file = discord.File(f"./media/youtube/{interaction.user.id}.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await interaction.followup.send(file=file, embed=embed)
      except:
        await interaction.followup.send(embed=embed)
    
      os.remove(f"./media/youtube/{interaction.user.id}.png")

async def setup(bot):
    await bot.add_cog(Utilities(bot))