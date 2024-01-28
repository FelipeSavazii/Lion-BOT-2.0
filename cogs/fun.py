import discord
from discord import app_commands, ui
from discord.ext import commands
from datetime import datetime
import asyncio
import random

# JOKENPO CLASS
class Jokenpo(discord.ui.Select):
    def __init__(self, interaction, bot):
        self.interaction = interaction
        self.bot = bot
        options = [
            discord.SelectOption(label='Pedra', description='Jogue com pedra.', emoji='🪨'),
            discord.SelectOption(label='Papel', description='Jogue com papel.', emoji='📄'),
            discord.SelectOption(label='Tesoura', description='Jogue com tesoura.', emoji='✂️'),
        ]
        super().__init__(placeholder='Selecione uma opção.', min_values=1, max_values=1, options=options)
      
    async def callback(self, interaction: discord.Interaction):
        await self.interaction.delete_original_response()
      
        embed = discord.Embed(
          description=f"JO!",
          color=0x7900ff,
        )
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Jokenpô - Lion BOT", icon_url=self.bot.user.avatar.url)
        embed.set_image(url="https://www.kapo.com.br/images/gifs/games/desk/hora-do-jogo/jokempo-pedra-papel-e-tesoura.gif")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(1.5)
      
        embed.description = f"KEN!"
        await interaction.edit_original_response(embed=embed)
        await asyncio.sleep(1.5)
      
        embed.description = f"PÔ!"
        await interaction.edit_original_response(embed=embed)
        await asyncio.sleep(1.5)
      
        result = random.choice(['pedra', 'papel', 'tesoura'])
      
        if self.values[0] == 'Pedra':
          if result == 'pedra':
            final_result = '`empate`.'
          elif result == 'papel':
            final_result = '`você perdeu`!'
          elif result == 'tesoura':
            final_result = '`você venceu`!'
      
        elif self.values[0] == 'Papel':
          if result == 'pedra':
            final_result = '`você venceu`!'
          elif result == 'papel':
            final_result = '`empate`.'
          elif result == 'tesoura':
            final_result = '`você perdeu`!'
            
        elif self.values[0] == 'Tesoura':
          if result == 'pedra':
            final_result = '`você perdeu`!'
          elif result == 'papel':
            final_result = '`você ganhou`!'
          elif result == 'tesoura':
            final_result = '`empate`.'
            
        embed.description = f"Resultado: {final_result}\n- Você escolheu: **{self.values[0].lower()}**.\n- O BOT escolheu: **{result}**."
        await interaction.edit_original_response(embed=embed)


class JokenpoView(discord.ui.View):
  def __init__(self, interaction, bot):
      super().__init__()

      self.add_item(Jokenpo(interaction, bot))

class Fun(commands.Cog, name="fun"):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="dado",
        description="Gire um dado e obtenha um resultado aleatório.",
    )
    async def dado(self, interaction: discord.Interaction):
        embed = discord.Embed(
            description=f"Girando dado...",
            color=0x7900ff,
        )
        embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
        embed.set_author(name="Dado - Lion BOT", icon_url=self.bot.user.avatar.url)
        embed.set_image(url="https://media.tenor.com/i_L5KauoCcoAAAAi/dice.gif")
        await interaction.response.send_message(embed=embed)
        await asyncio.sleep(1.0)
        embed.description = f"Resultado: `{random.randint(1, 6)}`."
        await interaction.edit_original_response(embed=embed)

    @app_commands.command(
      name="jokenpô",
      description="Jogue jokenpo contra mim! Duvido que consiga ganhar :)",
      #aliases=["jokenpo", "ppt", "pedrapapeltesoura"]
    )
    async def jokenpo(self, interaction: discord.Interaction):
      embed = discord.Embed(
          description=f"Vamos começar...",
          color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Jokenpô - Lion BOT", icon_url=self.bot.user.avatar.url)
      embed.set_image(url="https://www.kapo.com.br/images/gifs/games/desk/hora-do-jogo/jokempo-pedra-papel-e-tesoura.gif")
      await interaction.response.send_message(embed=embed, view=JokenpoView(interaction, self.bot))

    @app_commands.command(
      name="roleta",
      description="Com a roleta, posso te ajudar a decidir entre algumas opções.",
    )
    async def jokenpo(self, interaction: discord.Interaction, opção1: str, opção2: str, opção3: str = None, opção4: str = None, opção5: str = None, opção6: str = None, opção7: str = None, opção8: str = None):
      options = [opção1, opção2]
      options_to_text  = [f"- {opção1}\n", f"- {opção2}\n"]
      if opção3:
        options.append(opção3)
        options_to_text.append(f"- {opção3}\n")
      if opção4:
        options.append(opção4)
        options_to_text.append(f"- {opção4}\n")
      if opção5:
        options.append(opção5)
        options_to_text.append(f"- {opção5}\n")
      if opção6:
        options.append(opção6)
        options_to_text.append(f"- {opção6}\n")
      if opção7:
        options.append(opção7)
        options_to_text.append(f"- {opção7}\n")
      if opção8:
        options.append(opção8)
        options_to_text.append(f"- {opção8}\n")

      options_text = ''.join(options_to_text)
      
      embed = discord.Embed(
          description=f"Vou sortear...",
          color=0x7900ff,
      )
      embed.set_footer(text=f"Executado por {interaction.user.display_name}.")
      embed.set_author(name="Roleta - Lion BOT", icon_url=self.bot.user.avatar.url)
      await interaction.response.send_message(embed=embed)
      await asyncio.sleep(1.0)
      embed.description = f"Opções recebidas:\n{options_text}\nResultado: `{random.choice(options)}`."
      await interaction.edit_original_response(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))