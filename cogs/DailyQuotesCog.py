from discord.ext import tasks
from discord.ext import commands
from main import get_quote
from main import quotes_channel

#adding events @client.event -> @commands.Cog.listener()
#first parameter of functions in class = self
class MyQuote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(hours = 24.0)
    async def printer(self):
        quote = get_quote()
        channel = await self.bot.fetch_channel(quotes_channel)
        await channel.send(quote)


def setup(bot):
    bot.add_cog(MyQuote(bot))
