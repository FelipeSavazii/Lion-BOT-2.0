import discord
import traceback
import sys
from discord.ext import commands


class ErrorHandler(commands.Cog, name="error handler"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, 'on_error'):
            return

        cog = ctx.cog
        if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)

        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(
                description=f"Espere {error.retry_after:.2f} para executar outro comando.",
                color=0xff0000,
            )
            embed.set_footer(text=f"Executado por {ctx.author.name}.")
            embed.set_author(name="Erro do Lion BOT", icon_url=self.bot.user.avatar.url)
            await ctx.response.send_message(embed=embed)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except discord.HTTPException:
                pass

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


async def setup(bot):
    await bot.add_cog(ErrorHandler(bot))