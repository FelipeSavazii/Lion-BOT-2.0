import discord
import asyncio
from discord.ext import commands


class Configuration(commands.Cog, name="configuration"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        ...

async def setup(bot):
    await bot.add_cog(Configuration(bot))